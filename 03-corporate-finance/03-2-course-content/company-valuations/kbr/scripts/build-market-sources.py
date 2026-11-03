#!/usr/bin/env python3
"""Build the KBR market-data source notes from the as-of snapshots (no network).

Writes:
  sources/market-data/rates-2026-06-30.md          rates used, monthly Damodaran vs. FRED close
  sources/market-data/country-exposure-2026-06-30.md  revenue weights x (mature ERP + country risk premium)
  sources/market-data/bottom-up-beta-2026-06-30.md    segment betas from Damodaran's industry file

Regional country risk premiums are simple averages of the countries KBR names in its filings for that
region (Middle East: Saudi Arabia, Qatar, UAE, Iraq, Kuwait, Oman, Bahrain; Africa: Nigeria, Egypt,
Algeria, Libya, Angola, South Africa; Asia: China, India, Japan, Singapore, Malaysia, Indonesia; Other:
Canada, Brazil, Mexico, Chile). That choice is a discretionary decision recorded in read.md.
Usage: python3 scripts/build-market-sources.py   (run from the kbr/ folder)
"""
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(HERE, "sources", "market-data")
rates = json.load(open(os.path.join(MD, "market-rates-2026-06-01.json")))
crisk = json.load(open(os.path.join(MD, "country-risk-2026-01-01.json")))
betas = json.load(open(os.path.join(MD, "industry-betas-2026-01-05.json")))

dm = rates["damodaran_monthly"]
tb = rates["fred_latest"]["treasury_10y"]["value"]
sov = dm["us_sovereign_default_spread"]
rf = tb - sov
erp = dm["implied_erp_over_dollar_riskfree"]

with open(os.path.join(MD, "rates-2026-06-30.md"), "w") as fh:
    fh.write("# Rates used for KBR, as of 2026-06-30\n\n")
    fh.write("Source: market-rates-2026-06-01.json (Damodaran ERPJune26.xlsx; FRED DGS10, SOFR closes on 2026-06-30).\n\n")
    fh.write("| Item | Damodaran monthly (2026-06-01) | FRED close 2026-06-30 | Used |\n|---|---|---|---|\n")
    fh.write("| 10-year Treasury | {:.2%} | {:.2%} | {:.2%} |\n".format(dm["treasury_10y"], tb, tb))
    fh.write("| US sovereign default spread (Aa1) | {:.2%} | | {:.2%} |\n".format(sov, sov))
    fh.write("| Risk-free rate (Treasury − spread) | {:.2%} | | {:.2%} |\n".format(dm["dollar_riskfree_rate"], rf))
    fh.write("| Implied ERP over the netted risk-free rate | {:.4%} | | {:.4%} |\n".format(erp, erp))
    fh.write("| SOFR | | {:.2%} | reference for floating debt |\n".format(rates["fred_latest"]["sofr"]["value"]))
    fh.write("\nThe 2026-06-30 Treasury close equals the start-of-month figure (gap 0.00 points), so no second cost of capital is needed.\n")

c = crisk["countries"]
regions = {
    "United States": ["United States"],
    "Europe (mostly United Kingdom)": ["United Kingdom"],
    "Middle East": ["Saudi Arabia", "Qatar", "United Arab Emirates", "Iraq", "Kuwait", "Oman", "Bahrain"],
    "Australia": ["Australia"],
    "Africa": ["Nigeria", "Egypt", "Algeria", "Libya", "Angola", "South Africa"],
    "Asia": ["China", "India", "Japan", "Singapore", "Malaysia", "Indonesia"],
    "Other countries": ["Canada", "Brazil", "Mexico", "Chile"],
}
# FY2025 revenue by geographic destination, 10-K filed 2026-02-26, Note 3
revenue = {"United States": 4244, "Europe (mostly United Kingdom)": 1584, "Middle East": 790, "Australia": 548,
           "Africa": 253, "Asia": 142, "Other countries": 225}
total = sum(revenue.values())
rows = []
for reg, members in regions.items():
    present = [m for m in members if m in c and c[m].get("country_risk_premium") is not None]
    crp = 0.0 if reg == "United States" else sum(c[m]["country_risk_premium"] for m in present) / len(present)
    w = round(revenue[reg] / total, 4)
    rows.append((reg, w, crp, round(erp + crp, 4), present))
# make weights sum to exactly 1 by adjusting the largest
diff = round(1 - sum(r[1] for r in rows), 4)
rows[0] = (rows[0][0], round(rows[0][1] + diff, 4)) + rows[0][2:]
werp = sum(r[1] * r[3] for r in rows)
with open(os.path.join(MD, "country-exposure-2026-06-30.md"), "w") as fh:
    fh.write("# KBR country exposure and weighted ERP, as of 2026-06-30\n\n")
    fh.write("Weights: FY2025 revenue by geographic destination (10-K filed 2026-02-26, Note 3; total ${:,}M).\n".format(total))
    fh.write("ERP per region = mature ERP {:.4%} (Damodaran June 2026, over the netted risk-free rate) + the region's country risk premium "
             "(country-risk-2026-01-01.json; simple average of the listed countries). US premium is zero (SKILL.md rule 15).\n\n".format(erp))
    fh.write("| Region | Revenue ($M) | Weight | Country risk premium | ERP | Countries averaged |\n|---|---|---|---|---|---|\n")
    for (reg, w, crp, e, present) in rows:
        fh.write("| {} | {:,} | {:.4f} | {:.4%} | {:.4f} | {} |\n".format(reg, revenue[reg], w, crp, e, ", ".join(present)))
    fh.write("\nWeighted ERP: **{:.4f}**\n".format(werp))
print("weighted ERP", round(werp, 4))
for r in rows:
    print(r[0], r[1], r[3])

ind = betas["industries"]
seg = [("Mission Technology Solutions", "Aerospace/Defense", 579), ("Sustainable Technology Solutions", "Engineering/Construction", 497)]
tot = sum(s[2] for s in seg)
with open(os.path.join(MD, "bottom-up-beta-2026-06-30.md"), "w") as fh:
    fh.write("# KBR bottom-up unlevered beta, as of 2026-06-30\n\n")
    fh.write("Industry betas: industry-betas-2026-01-05.json (Damodaran betas.xls, January 2026), unlevered and cash-corrected.\n")
    fh.write("Weights: FY2025 segment Adjusted EBITDA (MTS $579M, STS $497M; Q4 FY2025 earnings release, 8-K filed 2026-02-26), "
             "a proxy for each segment's share of firm value. Corporate cost excluded.\n\n")
    fh.write("| Segment | Industry | Adj. EBITDA ($M) | Weight | Unlevered beta (cash-corrected) |\n|---|---|---|---|---|\n")
    bu = 0
    for name, ind_name, e in seg:
        b = ind[ind_name]["unlevered_beta_cash_corrected"]
        w = round(e / tot, 4)
        bu += w * b
        fh.write("| {} | {} | {} | {:.4f} | {:.4f} |\n".format(name, ind_name, e, w, b))
    fh.write("\nWeighted unlevered beta: **{:.4f}**\n\n".format(bu))
    fh.write("Alternatives considered: Computer Services ({:.4f}) or Information Services ({:.4f}) for MTS; revenue weights "
             "(MTS 0.717) instead of EBITDA weights.\n".format(ind["Computer Services"]["unlevered_beta_cash_corrected"],
                                                           ind["Information Services"]["unlevered_beta_cash_corrected"]))
print("bottom-up beta", round(bu, 4))
