---
title: "JPMorgan Chase & Co. (JPM) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# JPMorgan Chase & Co. (JPM) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

Quick mode: only the question-bank entries tagged with a signal. Source lesson: [../../01-foundations-and-discount-rates/lesson-07/lesson-overview.md](../../01-foundations-and-discount-rates/lesson-07/lesson-overview.md).

## Module 1 Step — Questions for This Lesson

- **What is the best measure of the company's country exposure (revenues, production, assets)?**
  Revenues by client domicile, from Note 31 of the 10-K (sources/filings/jpm-10-k-2026-02-13.md line 11869). Assets would put more weight abroad (24% of assets vs. 23% of revenue) but most foreign assets are trading and liquidity books in developed markets.

- **What is the geographic breakdown of that measure?**
  2025: North America 76.6% ($139,689M), Europe/Middle East/Africa 13.4%, Asia-Pacific 7.7%, Latin America/Caribbean 2.3% (`country.exposures`).

- **What is the weighted average ERP?**
  4.82% (`country.weighted_erp`): the 4.57% implied premium over the netted risk-free rate (`market.mature_erp`) plus country risk premiums of 0% (US, rule 15), 0.78% (UK, standing in for EMEA), 0.91% (Japan/China, both A1, for Asia-Pacific) and 3.24% (Brazil, for Latin America).

- **Why might that ERP change?**
  The 4.57% mature premium moves monthly with the S&P 500 (it is implied); the regional proxies are judgment calls. All-US exposure would give 4.57% and a cost of equity of 8.06% instead of 8.27% (alternatives/erp-us-only-output.md).

## Notes

> ⚠️ **Discretionary Decision: regional country risk proxies**
> **Chose:** UK for EMEA, Japan/China for Asia-Pacific, Brazil for Latin America. **Why:** the 10-K gives regions, not countries; each proxy is the region's largest JPMorgan market as far as the filing shows. **Alternative:** treat all revenue as US → cost of equity 8.06% vs. 8.27% (alternatives/erp-us-only-output.md). **Confidence:** medium; the choice moves the cost of equity by 0.2 points and does not change any conclusion.
