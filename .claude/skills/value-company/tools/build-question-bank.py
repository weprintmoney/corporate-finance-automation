#!/usr/bin/env python3
"""Build question-bank.yaml for /value-company from three layers:

  module-1-step   seeds/module-1-steps.yaml            12 steps, lessons 1-12
  project         "## Project Questions" in each lesson-overview.md, lessons 13-36 (verbatim)
  transcript      seeds/transcript-questions.yaml      one entry per lecture video part

Usage:
  python3 build-question-bank.py            # writes question-bank.yaml next to the seeds
  python3 build-question-bank.py --check    # exit 1 if question-bank.yaml is out of date

Output is deterministic (no timestamps) so --check can run in CI.
"""
import io
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.normpath(os.path.join(HERE, ".."))
REPO = os.path.normpath(os.path.join(SKILL, "..", "..", ".."))
CC = os.path.join(REPO, "03-corporate-finance", "03-2-course-content")
OUT = os.path.join(SKILL, "question-bank.yaml")

# Ledger fields the project questions of each lesson typically need. Coarse by design; the
# transcript layer carries finer tags.
PROJECT_INPUTS = {
    13: ["company.debt_total", "company.lease_debt", "company.equity_value", "company.equity_book",
         "beta.unlevered_bottom_up", "beta.segments", "market.risk_free_rate", "country.weighted_erp", "market.tax_rate_marginal"],
    14: ["company.ebit", "company.invested_capital", "company.goodwill", "market.tax_rate_marginal", "company.history"],
    15: ["company.capex", "company.history"],
    16: ["country.exposures", "meta.currency", "market.risk_free_rate"],
    17: ["debt.rate_type", "debt.covenants", "company.debt_total", "market.tax_rate_marginal", "company.history"],
    18: ["company.ebit", "company.debt_total", "company.equity_value", "beta.unlevered_bottom_up", "modeling_choices.coverage_numerator"],
    19: ["company.debt_total", "company.equity_value", "market.terminal_growth", "debt.covenants"],
    20: ["company.history", "governance.controlling_holders", "meta.type"],
    21: ["market.tax_rate_marginal", "company.debt_total", "company.equity_value", "peers"],
    22: ["company.debt_total", "company.equity_value", "governance.controlling_holders", "beta.jensens_alpha"],
    23: ["debt.rate_type", "debt.maturity_years", "debt.currency", "country.exposures"],
    24: ["company.history", "company.share_price", "company.net_income"],
    25: ["governance.marginal_investor", "debt.covenants", "company.history"],
    26: ["company.history", "company.cash", "company.debt_total"],
    27: ["company.history", "company.cash", "company.invested_capital"],
    28: ["peers", "company.history"],
    29: ["company.equity_value", "company.net_income", "company.history"],
    30: ["company.ebit", "company.capex", "company.da", "company.change_wc", "market.tax_rate_marginal", "company.history"],
    31: ["company.history", "company.invested_capital", "forecast.management_growth", "forecast.analyst_growth", "forecast.sales_to_capital"],
    32: ["forecast.growth_period_years", "market.terminal_growth", "forecast.stable_roic", "forecast.wacc_stable"],
    33: ["company.cash", "company.cross_holdings", "company.minority_interests", "company.options_value", "company.shares_basic"],
    34: ["forecast.years", "company.debt_total", "company.cash", "company.shares_basic", "governance.controlling_holders"],
    35: ["peers", "company.revenue", "company.ebitda_standardized", "company.net_income", "company.equity_book",
         "company.equity_value", "company.debt_total", "company.cash"],
    36: ["governance.objectives", "company.history"],
}


def load_yaml(path):
    with open(path) as fh:
        return yaml.safe_load(fh)


def lesson_index():
    idx = load_yaml(os.path.join(CC, "lesson-index.yaml"))
    return {int(l["lesson"]): l for l in idx["lessons"]}


def project_questions(index):
    out = []
    for n in range(13, 37):
        folder = os.path.join(CC, index[n]["folder"])
        path = os.path.join(folder, "lesson-overview.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"^## Project Questions\s*\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S)
        if not m:
            continue
        for i, q in enumerate(re.findall(r"^- (.+)$", m.group(1), flags=re.M), start=1):
            q = q.strip()
            if q.count('"') % 2 == 1 and q.endswith('"'):
                q = q[:-1]
            out.append({
                "id": "l{:02d}-q{}".format(n, i),
                "lesson": n,
                "layer": "project",
                "topic": index[n]["topic"],
                "source": os.path.relpath(path, REPO),
                "question": q,
                "inputs": PROJECT_INPUTS.get(n, []),
                "applies_to": ["all"],
            })
    return out


def module1_entries(index):
    out = []
    for step in load_yaml(os.path.join(SKILL, "seeds", "module-1-steps.yaml")):
        out.append({
            "id": step["id"],
            "lesson": step["lesson"],
            "layer": "module-1-step",
            "topic": index[step["lesson"]]["topic"],
            "title": step["title"],
            "read": step["read"],
            "questions": step["questions"],
            "produces": step.get("produces", []),
            "applies_to": step.get("applies_to", ["all"]),
        })
    return out


def transcript_entries(index):
    out = []
    for e in load_yaml(os.path.join(SKILL, "seeds", "transcript-questions.yaml")):
        transcript = os.path.join(REPO, e["transcript"])
        if not os.path.exists(transcript):
            sys.exit("transcript not found: {}".format(e["transcript"]))
        out.append({
            "id": e["id"],
            "lesson": e["lesson"],
            "layer": "transcript",
            "topic": index[e["lesson"]]["topic"],
            "part": e["part"],
            "title": e["title"],
            "transcript": e["transcript"],
            "quote": e["quote"],
            "concept": e["concept"],
            "question": " ".join(e["question"].split()),
            "inputs": e.get("inputs", []),
            "applies_to": e.get("applies_to", ["all"]),
        })
    return out


def build():
    index = lesson_index()
    entries = module1_entries(index) + project_questions(index) + transcript_entries(index)
    order = {"module-1-step": 0, "project": 1, "transcript": 2}
    entries.sort(key=lambda e: (e["lesson"], order[e["layer"]], e.get("part", 0), e["id"]))
    counts = {}
    for e in entries:
        counts[e["layer"]] = counts.get(e["layer"], 0) + 1
    header = (
        "# Question bank for /value-company. GENERATED by tools/build-question-bank.py; do not edit.\n"
        "# Layers: module-1-step ({}), project ({}, verbatim from lesson-overview.md), transcript ({}).\n"
        "# Fields: id, lesson, layer, topic, then layer-specific fields. `inputs` are ledger paths\n"
        "# (see ledger-schema.yaml). `applies_to` gates by meta.type.\n".format(
            counts.get("module-1-step", 0), counts.get("project", 0), counts.get("transcript", 0))
    )
    body = yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=110, default_flow_style=False)
    return header + body, counts


def main(argv):
    text, counts = build()
    if "--check" in argv:
        current = open(OUT).read() if os.path.exists(OUT) else ""
        if current != text:
            print("question-bank.yaml is out of date; run tools/build-question-bank.py")
            sys.exit(1)
        print("question-bank.yaml is current ({} entries)".format(sum(counts.values())))
        return
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote {} ({} entries: {})".format(os.path.relpath(OUT, REPO), sum(counts.values()), counts))


if __name__ == "__main__":
    main(sys.argv[1:])
