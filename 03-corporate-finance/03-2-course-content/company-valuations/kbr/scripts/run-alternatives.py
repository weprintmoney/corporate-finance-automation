#!/usr/bin/env python3
"""Rule 14: each discretionary decision's alternative is a model run. Copies inputs.yaml with one field
changed to alternatives/<choice>.yaml and runs model.py into alternatives/<choice>-output.md.
Usage (from the kbr/ folder): python3 scripts/run-alternatives.py
"""
import copy
import os
import subprocess

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.path.join(HERE, "..", "..", "..", "..", ".claude", "skills", "value-company", "tools", "model.py")
base = yaml.safe_load(open(os.path.join(HERE, "inputs.yaml")))
os.makedirs(os.path.join(HERE, "alternatives"), exist_ok=True)


def leaf(v, src):
    return {"value": v, "source": src, "as_of": "2026-06-30"}


def alt_large(L):
    L["modeling_choices"]["firm_size_table"] = "large"


def alt_synthetic(L):
    L["modeling_choices"]["kd_source"] = "synthetic"


def alt_beta_revenue(L):
    # revenue weights MTS 5581 / STS 2205 (10-K Note 2) on the same industry betas
    w = 5581 / 7786
    L["beta"]["unlevered_bottom_up"] = leaf(round(w * 0.8694 + (1 - w) * 1.1374, 4),
                                            "Alternative: revenue weights (MTS 0.717) on sources/market-data/bottom-up-beta-2026-06-30.md")


def alt_beta_computer(L):
    L["beta"]["unlevered_bottom_up"] = leaf(round(0.5381 * 0.9617 + 0.4619 * 1.1374, 4),
                                            "Alternative: MTS as Computer Services (0.9617), sources/market-data/bottom-up-beta-2026-06-30.md")


def alt_us_erp_only(L):
    L["country"]["weighted_erp"] = leaf(0.0457, "Alternative: mature ERP only, no country premiums")
    L["country"]["exposures"] = [{"country": "United States", "weight": 1.0, "erp": 0.0457, "measure": "revenues",
                                  "source": "sources/market-data/country-exposure-2026-06-30.md", "as_of": "2026-06-30"}]


def alt_acq_as_capex(L):
    acq = {2022: 73, 2023: 0, 2024: 738, 2025: 14}
    for r in L["company"]["history"]:
        r["capex"] = r["capex"] + acq[r["year"]]


def alt_stable_debt_optimum(L):
    L["forecast"]["stable_debt_ratio"] = leaf(0.42, "Alternative: section 3 optimum (EBIT)")


def alt_growth_25(L):
    L["market"]["terminal_growth"] = leaf(0.025, "Alternative terminal growth")


def alt_q1_balance(L):
    # 10-Q filed 2026-05-05: face debt 977+980+250+395 = 2602; cash 380
    L["company"]["debt_face"] = leaf(2602, "sources/filings/kbr-10-q-2026-05-05.md Note 8")
    L["company"]["debt_total"] = leaf(2903, "2602 + leases 301 (FY2025 note; Q1 lease PV not re-read)")
    L["company"]["debt_book"] = leaf(2583, "sources/filings/kbr-10-q-2026-05-05.md Note 8")
    L["company"]["cash"] = leaf(380, "sources/filings/kbr-8-k-2026-05-05-items-202-901.md balance sheet")


def alt_margin_ex_lng(L):
    for r in L["forecast"]["years"]:
        r["ebit_margin"] = 0.087
    L["company"]["ebit"] = leaf(675, "Alternative: FY2025 EBIT 778 less the $103M rise in equity earnings (LNG project), 10-K MD&A")


ALTS = {
    "firm-size-large": alt_large,
    "kd-synthetic": alt_synthetic,
    "beta-revenue-weights": alt_beta_revenue,
    "beta-mts-computer-services": alt_beta_computer,
    "erp-us-only": alt_us_erp_only,
    "acquisitions-as-capex": alt_acq_as_capex,
    "stable-debt-at-optimum": alt_stable_debt_optimum,
    "terminal-growth-2-5": alt_growth_25,
    "q1-2026-balance-sheet": alt_q1_balance,
    "margin-ex-lng-uplift": alt_margin_ex_lng,
}

for name, fn in ALTS.items():
    L = copy.deepcopy(base)
    L["market"]["ratings_table"]["value"] = "../" + L["market"]["ratings_table"]["value"]
    fn(L)
    yp = os.path.join(HERE, "alternatives", name + ".yaml")
    with open(yp, "w") as fh:
        fh.write("# Alternative to inputs.yaml: {} (one choice changed; see scripts/run-alternatives.py)\n".format(name))
        yaml.safe_dump(L, fh, sort_keys=False, allow_unicode=True, width=200)
    out = subprocess.run(["python3", MODEL, yp], capture_output=True, text=True)
    with open(os.path.join(HERE, "alternatives", name + "-output.md"), "w") as fh:
        fh.write(out.stdout)
    if out.returncode:
        print(name, "FAILED", out.stderr[-300:])
    else:
        print(name, "ok")
