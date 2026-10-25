---
title: "SolarWinds (SWI) — Lesson 06: Equity Risk Premiums"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 06: Equity Risk Premiums

### Lesson 06 — Equity Risk Premiums

- **Lesson 06, Session 6 · Part 1 — "Survey, Historical, and Implied Premiums — Three Ways to Estimate the ERP"** ([transcript](../../01-foundations-and-discount-rates/lesson-06/session-6-part-1.md))
    - Quote: "That 10-year risk premium is pure noise, so I have to go back as far as I can because I need the data."
    - Question for SolarWinds: Which equity risk premium does the valuation of SolarWinds use (survey, historical, implied), why, and what would the cost of equity be under the other two? If SolarWinds is private, does a market-implied premium still apply, or does the owner's required return replace it?
    - Sources needed: Damodaran's implied premium for February 2025; the historical premium table; survey premiums.
    - Where to find: ledger `market.mature_erp`, `governance.marginal_investor`, `country.weighted_erp`; `sources/market-data/market-rates-2025-02-05.json`; `01-foundations-and-discount-rates/lesson-06/spreadsheet-histretsp.md`.
    - Answer: The implied premium, 4.27%, from Damodaran's February 2025 workbook (the S&P 500 at 6040.53; `market.mature_erp`). It uses today's prices and today's expected cash flows rather than a long look back, so it belongs to the valuation date. Cost of equity at SolarWinds' relevered beta of 1.6714 and risk-free rate of 4.43% (model-output.md §1), with a US-only premium so the methods compare cleanly: implied 4.27% gives 11.57% (arithmetic, 4.43% + 1.6714 × 4.27%). The country-weighted premium actually used, 4.92%, gives 12.65% (model-output.md §1). Historical premium, 1928–2022, stocks over Treasury bonds: 6.64% arithmetic average with a standard error of 2.15%, and 5.06% geometric (`facts.hist-erp-1928-2022`; lesson spreadsheet, which stops at 2022). That gives 15.53% and 12.89%. The standard error is the lecture's point: it is a third the size of the premium. Survey premiums: no survey figure for February 2025 is in `sources/`, so no cost of equity is computed. Private status: not an issue at the valuation date. SolarWinds was listed and traded through 2025-02-05 (`meta.analysis_date`), and a premium is the market's price of risk, not an attribute of the firm. A buyer's required return after leverage and fees would replace it only in a valuation for that buyer, which is not this one.

- **Lesson 06, Session 6 · Part 2 — "Scaling Sovereign Default Spreads Into Country Equity Risk Premiums"** ([transcript](../../01-foundations-and-discount-rates/lesson-06/session-6-part-2.md))
    - Quote: "I would argue that equities are riskier than bonds."
    - Question for SolarWinds: Which method produced the country risk premiums applied to SolarWinds (the raw default spread, or the spread scaled by relative equity volatility), and how much does the choice of method move the weighted equity risk premium?
    - Sources needed: Damodaran's country table for January 2025 and its method; the regional premium used for the international slice.
    - Where to find: `sources/market-data/country-risk-2025-01-01.json`; ledger `country.exposures`, `country.weighted_erp`.
    - Answer: The scaled method. In the January 2025 table every country's equity premium over the mature market equals its default spread times 1.3475, the relative equity volatility Damodaran applies (`facts.country-erp-scalar`; for example the United Kingdom, 0.59% spread, 0.80% premium). The United States has a spread of 0.00% (`market.sovereign_default_spread`), so scaling does nothing to the 64.82% US slice. The international slice uses the EMEA regional premium of 1.84 points, from the same workbook's regional averages, added to the 4.27% mature premium, for 6.11% (`country.exposures`). Had raw spreads been used, that 1.84 would be about 1.37 (1.84 ÷ 1.3475), and the weighted premium would be about 4.75% instead of 4.92%, 0.17 points lower. The cost of equity would be about 0.28 points lower (1.6714 × 0.17). The method choice is small next to the choice of region (lesson 7).

## Module 1 Step — Questions for This Lesson

- **Mature-market equity risk premium**
  - What is the equity risk premium for a mature market today, by which method, from which source? 4.27%, implied by the S&P 500 level and expected cash flows, from Damodaran's ERPFeb25.xlsx, dated 2025-02-01 (`market.mature_erp`). "Today" is the analysis date, 2025-02-05. The country workbook's January figure for mature markets is 4.33%; the February figure is used because it is the later of the two.

## Notes

The premium is measured over the dollar risk-free rate, with the 0.11-point date gap noted in lesson 5. It feeds the country-weighted premium of 4.92% (lesson 7) and the cost of equity of 12.65% (lesson 12). The historical premium comes from a lesson spreadsheet that ends in 2022, so it is used only to show the range, not as an input.
