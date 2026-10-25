---
title: "SolarWinds (SWI) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

- **Lesson 07, Session 7 · Part 1 — "Implied Equity Risk Premiums and Building Country Risk Off Them"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-1.md))
    - Quote: "a company's risk does not come from where it's incorporated but from where it does business."
    - Question for SolarWinds: How much of SolarWinds' revenue (or production, if that is the better measure) comes from outside its home country, and what is its revenue-weighted equity risk premium compared with the flat home-country number?
    - Sources needed: revenue by geography; staff by location; the premium for each region.
    - Where to find: ledger `country.exposures`, `country.weighted_erp`, `market.mature_erp`; `sources/filings/swi-10k-fy2024.md` (Note 16; Item 1, Human Capital).
    - Answer: 35.18% of revenue, $280.3M of $796.9M, is international by customer shipping address (`country.exposures`; 10-K FY2024, Note 16). The revenue-weighted premium is 4.92% against the flat US figure of 4.27%, 0.65 points higher (`country.weighted_erp`, `market.mature_erp`). Production tells a different story. Of 2,107 employees, 1,379 work outside the United States and 728 inside (`facts.employees-2024`), and the company operates in the United States, Europe, Singapore, the Philippines and India, running much of its research outside the United States (10-K FY2024, Item 7A and Item 1A). Revenue is still the better measure for the equity premium, because customers' economies drive the cash flows, and it is the only geographic split the filing gives. The staffing mix matters for costs and for currency, not for the premium.

- **Lesson 07, Session 7 · Part 2 — "Company Equity Risk Premiums and Implied ERP"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-2.md))
    - Quote: "For every one of these companies, I'm looking past the country of incorporation to where they do business."
    - Question for SolarWinds: What is SolarWinds' weighted equity risk premium in numbers, which single country exposure moves it most, and what would make that exposure change?
    - Sources needed: the exposure weights and premiums; alternative premiums for the international slice.
    - Where to find: ledger `country.exposures`, `country.weighted_erp`; `sources/market-data/country-risk-2025-01-01.json`.
    - Answer: 4.92%: 64.82% × 4.27% for the United States plus 35.18% × 6.11% for international (`country.exposures`; `country.weighted_erp`). The international slice moves it most, since it is the only exposure above the mature-market figure. Its 1.84-point premium adds 0.65 points to the total (0.3518 × 1.84). That 1.84 is a judgment: the 10-K gives no regional split, so the EMEA regional premium stands in for all international revenue because most international offices are in Europe. The alternatives are the Western Europe premium of 1.12 points, which gives a weighted premium of 4.66%, and the global average of 1.43 points, which gives 4.77% (`country.exposures` note; arithmetic, 4.27% + 0.3518 × premium). The disclosed currencies are the euro, pound and Australian dollar, from governments rated Aaa to Aa3 (lesson 5), so the Western Europe figure could be argued as the better fit and EMEA is the cautious choice. At the cost-of-equity level, 4.66% against 4.92% is 0.26 points of premium, about 0.43 points of cost of equity at a beta of 1.6714. What would change it: a filing that splits revenue by region; Damodaran's January and July updates of the regional figures; and a rating change for the US itself, such as Moody's May 2025 downgrade, which puts a spread on the 64.82% slice that is zero today.

## Module 1 Step — Questions for This Lesson

- **Country risk and weighted ERP**
  - What is the best measure of the company's country exposure (revenues, production, assets)? Revenues. They are the only split disclosed that follows customers (Note 16). Staff and long-lived assets exist but are not the cash-flow driver.
  - What is the geographic breakdown of that measure? United States 64.82%, $516.6M; international 35.18%, $280.3M (`country.exposures`). No country other than the United States reached 10% of revenue.
  - What is the weighted average ERP? 4.92% (`country.weighted_erp`).
  - Why might that ERP change? A regional revenue disclosure; Damodaran's twice-yearly update; the US sovereign rating falling from Aaa; or a shift in the international share, which the company says it intends to grow.

## Notes

The 4.92% is the equity risk premium in the cost of equity: 4.43% + 1.6714 × 4.92% = 12.65% (model-output.md §1). The international weight and the EMEA proxy are the two judgment calls; the sensitivity range of 4.66% to 4.92% moves the cost of equity by about 0.4 points. The weighted figure replaces a flat mature-market premium.
