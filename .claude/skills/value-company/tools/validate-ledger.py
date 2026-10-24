#!/usr/bin/env python3
"""Check a /value-company ledger (inputs.yaml) before the model runs.

Checks:
  - every field the schema requires for this company type is present (or listed in meta.omitted)
  - every input leaf is {value, source, as_of}; estimates carry a range
  - list rows (history, exposures, forecast years, peers, controlling holders) carry source and as_of
  - identities: equity = shares × price, debt_total = debt + leases, weights sum to one,
    weighted ERP matches exposures, terminal growth ≤ risk-free rate, years are consecutive
  - staleness: market inputs older than 90 days at the analysis date (warning)

Usage: python3 validate-ledger.py <inputs.yaml> [--schema <ledger-schema.yaml>]
Exit 1 on any ERROR. Warnings do not fail.
"""
import os
import sys
from datetime import date, datetime

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCHEMA = os.path.join(HERE, "..", "ledger-schema.yaml")

LEAF_SECTIONS = ["market", "beta", "company", "debt", "forecast"]
LIST_FIELDS_WITH_SOURCE = ["company.history", "country.exposures", "forecast.years", "peers", "governance.controlling_holders"]
SCALAR_LISTS = ["company.history", "country.exposures", "beta.segments", "forecast.years", "peers",
                "governance.board", "governance.controlling_holders", "meta.omitted"]


def get(data, path):
    cur = data
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def val(x):
    return x.get("value") if isinstance(x, dict) and "value" in x else x


def parse_date(s):
    try:
        return datetime.strptime(str(s), "%Y-%m-%d").date()
    except Exception:
        return None


def main(argv):
    if not argv:
        sys.exit("usage: validate-ledger.py <inputs.yaml> [--schema <ledger-schema.yaml>]")
    ledger_path = argv[0]
    schema_path = argv[argv.index("--schema") + 1] if "--schema" in argv else DEFAULT_SCHEMA
    with open(ledger_path) as fh:
        L = yaml.safe_load(fh)
    with open(schema_path) as fh:
        S = yaml.safe_load(fh)

    errors, warnings = [], []
    ctype = get(L, "meta.type")
    is_fixture = "/examples/" in os.path.abspath(ledger_path).replace(os.sep, "/")

    # --- placeholders ----------------------------------------------------------------------------
    # `source: placeholder` marks a made-up value in the skill's test fixture. It is never allowed
    # in a real company ledger.
    def walk_sources(x, path):
        if isinstance(x, dict):
            src = x.get("source")
            if isinstance(src, str) and src.strip().lower().startswith("placeholder"):
                (warnings if is_fixture else errors).append("{} is a placeholder{}".format(
                    path, "" if is_fixture else " (only allowed in the skill's examples/ fixture)"))
            for k, v in x.items():
                walk_sources(v, "{}.{}".format(path, k) if path else k)
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk_sources(v, "{}[{}]".format(path, i))

    walk_sources(L, "")
    omitted = {o.get("field") for o in (get(L, "meta.omitted") or []) if isinstance(o, dict)}

    # --- required fields -------------------------------------------------------------------------
    for section, fields in S.items():
        for name, spec in fields.items():
            if name == "_row":
                path = section
            else:
                path = "{}.{}".format(section, name)
            req = spec.get("required_for", []) if isinstance(spec, dict) else []
            if ("all" in req or ctype in req) and get(L, path) is None and path not in omitted:
                errors.append("missing required field {} (required for {})".format(path, ", ".join(req)))

    # --- leaf shape ------------------------------------------------------------------------------
    for section in LEAF_SECTIONS:
        block = L.get(section) or {}
        for name, leaf in block.items():
            path = "{}.{}".format(section, name)
            if path in SCALAR_LISTS:
                continue
            if not isinstance(leaf, dict) or "value" not in leaf:
                errors.append("{} must be a mapping with value, source, as_of".format(path))
                continue
            for k in ("source", "as_of"):
                if not leaf.get(k):
                    errors.append("{} is missing {}".format(path, k))
            extra = set(leaf) - {"value", "source", "as_of", "note", "estimate", "range"}
            if extra:
                errors.append("{} has unexpected keys {} (an unquoted comma in a string?)".format(path, sorted(map(str, extra))))
            if leaf.get("as_of") and not parse_date(leaf["as_of"]):
                errors.append("{} as_of is not YYYY-MM-DD".format(path))
            if leaf.get("estimate") and not leaf.get("range"):
                errors.append("{} is an estimate without a range".format(path))
    for path in ["country.weighted_erp", "governance.share_classes", "governance.marginal_investor", "governance.objectives"]:
        leaf = get(L, path)
        if leaf is not None and (not isinstance(leaf, dict) or "value" not in leaf or not leaf.get("source")):
            errors.append("{} must be a mapping with value, source, as_of".format(path))

    # --- list rows ---------------------------------------------------------------------------------
    for path in LIST_FIELDS_WITH_SOURCE:
        rows = get(L, path) or []
        if not isinstance(rows, list):
            errors.append("{} must be a list".format(path))
            continue
        for i, row in enumerate(rows):
            if not isinstance(row, dict):
                errors.append("{}[{}] must be a mapping".format(path, i))
                continue
            for k in ("source", "as_of"):
                if not row.get(k):
                    errors.append("{}[{}] is missing {}".format(path, i, k))
            if row.get("estimate") and not row.get("range"):
                errors.append("{}[{}] is an estimate without a range".format(path, i))

    # --- identities --------------------------------------------------------------------------------
    def num(path):
        v = val(get(L, path))
        return float(v) if isinstance(v, (int, float)) and not isinstance(v, bool) else None

    sb, price, E = num("company.shares_basic"), num("company.share_price"), num("company.equity_value")
    if sb and price and E:
        if abs(sb * price - E) / E > 0.01:
            errors.append("company.equity_value {:.1f} differs from shares_basic × share_price {:.1f} by more than 1%".format(E, sb * price))
    D, Df, Db, Dl = num("company.debt_total"), num("company.debt_face"), num("company.debt_book"), num("company.lease_debt")
    if D is not None and Dl is not None:
        candidates = [x + Dl for x in (Df, Db) if x is not None]
        if candidates and all(abs(c - D) / D > 0.005 for c in candidates):
            errors.append("company.debt_total {:.1f} is neither debt_face nor debt_book plus lease_debt ({})".format(
                D, ", ".join("{:.1f}".format(c) for c in candidates)))
    exposures = get(L, "country.exposures") or []
    if exposures:
        wsum = sum(float(r.get("weight", 0)) for r in exposures)
        if abs(wsum - 1) > 0.005:
            errors.append("country.exposures weights sum to {:.3f}, not 1".format(wsum))
        werp = sum(float(r.get("weight", 0)) * float(r.get("erp", 0)) for r in exposures)
        stated = num("country.weighted_erp")
        if stated is not None and abs(werp - stated) > 0.0005:
            errors.append("country.weighted_erp {:.4f} does not match the exposures ({:.4f})".format(stated, werp))
    segments = get(L, "beta.segments") or []
    if segments:
        wsum = sum(float(r.get("weight", 0)) for r in segments)
        if abs(wsum - 1) > 0.005:
            errors.append("beta.segments weights sum to {:.3f}, not 1".format(wsum))
    g, rf, t = num("market.terminal_growth"), num("market.risk_free_rate"), num("market.tax_rate_marginal")
    if g is not None and rf is not None and g > rf:
        errors.append("market.terminal_growth {:.4f} exceeds the risk-free rate {:.4f}".format(g, rf))
    if t is not None and not 0 <= t <= 0.5:
        errors.append("market.tax_rate_marginal {} is outside 0 to 0.5".format(t))
    for path in ["company.history", "forecast.years"]:
        rows = get(L, path) or []
        yrs = [int(r.get("year")) for r in rows if isinstance(r, dict) and r.get("year") is not None]
        if yrs and yrs != list(range(yrs[0], yrs[0] + len(yrs))):
            errors.append("{} years are not consecutive: {}".format(path, yrs))
    ebit, interest = num("company.ebit"), num("company.interest_expense")
    if ebit is not None and interest:
        print("coverage check: EBIT {:.1f} / interest {:.1f} = {:.2f}x".format(ebit, interest, ebit / interest))

    # --- staleness -------------------------------------------------------------------------------
    adate = parse_date(get(L, "meta.analysis_date"))
    if adate:
        for name, leaf in (L.get("market") or {}).items():
            d = parse_date(leaf.get("as_of")) if isinstance(leaf, dict) else None
            if d and (adate - d).days > 90:
                warnings.append("market.{} is {} days older than the analysis date".format(name, (adate - d).days))

    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("{}: {} error(s), {} warning(s)".format(ledger_path, len(errors), len(warnings)))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
