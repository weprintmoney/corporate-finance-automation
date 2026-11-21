---
title: "Colgate-Palmolive (CL) — Lesson 06: Equity Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 06: Equity Risk Premiums

### Lesson 06 — Equity Risk Premiums

- **Lesson 06, Session 6 · Part 1 — "Survey, Historical, and Implied Premiums — Three Ways to Estimate the ERP"** ([transcript](../../01-foundations-and-discount-rates/lesson-06/session-6-part-1.md))
    - Quote: "That 10-year risk premium is pure noise, so I have to go back as far as I can because I need the data."
    - Question for Colgate-Palmolive: Which equity risk premium does the valuation of Colgate-Palmolive use (survey, historical, implied), why, and what would the cost of equity be under the other two? If Colgate-Palmolive is private, does a market-implied premium still apply, or does the owner's required return replace it?
    - Sources needed: Implied premium on the analysis date; historical premiums; a survey premium; the effect of each on the cost of equity.
    - Where to find: ledger `market.mature_erp`, `facts.rates-snapshot`, `facts.hist-erp-1928-2022`, `facts.cost-of-capital-alternatives`, `facts.erp-november-bound`, `facts.sp500-november-2026`; `module-1-cross-checks-output.md` §2; `sources/market-data/market-rates-2026-11-19.json`.
    - Answer: Implied: 3.61%, Damodaran's figure for the start of November 2026, measured over the dollar risk-free rate (`market.mature_erp`). Reason: it is forward-looking, it is what investors were paying for risk this month, and it is the figure the professor's own spreadsheets pair with a netted risk-free rate. Under the historical premium the cost of equity would be far higher. Stocks beat Treasury bonds by 6.64% a year from 1928 to 2022 as a simple average, with a standard error of 2.15%, and by 5.06% compounded (`facts.hist-erp-1928-2022`). With Colgate's country risk added, those give a cost of equity of 10.98% or 9.82%, against 8.76% in the base case, and a cost of capital of 10.35% or 9.31% against 8.34% (`facts.cost-of-capital-alternatives`). A standard error of 2.15% on a 6.64% estimate is why the historical figure lost: it cannot tell 4% from 9%. No survey premium for November 2026 is in our files, so none is shown. Colgate is public, so the private-owner question does not arise. The date problem, which is the real weakness: the 3.61% was measured with the S&P 500 at 7,580.07. By the analysis date the index had fallen 8.8% to 6,910.39 (`facts.sp500-november-2026`). When prices fall and expected cash flows have not, the implied premium rises. The owner's decision is to keep the published 3.61% and say so. The alternative was to recompute the premium for 2026-11-20, which needs the cash flow inputs inside Damodaran's workbook; those are not in `sources/`. A rough bound, assuming cash flows unchanged, puts the premium near 3.96% and the cost of capital at 8.57% instead of 8.34% (`facts.erp-november-bound`). So the base case cost of capital is, if anything, about a fifth of a point low.

- **Lesson 06, Session 6 · Part 2 — "Scaling Sovereign Default Spreads Into Country Equity Risk Premiums"** ([transcript](../../01-foundations-and-discount-rates/lesson-06/session-6-part-2.md))
    - Quote: "I would argue that equities are riskier than bonds."
    - Question for Colgate-Palmolive: Which method produced the country risk premiums applied to Colgate-Palmolive (the raw default spread, or the spread scaled by relative equity volatility), and how much does the choice of method move the weighted equity risk premium?
    - Sources needed: Regional country risk premiums; the scaling ratio; the weighted premium under each method.
    - Where to find: ledger `country.exposures`, `country.weighted_erp`, `facts.country-premium-method`; `sources/market-data/country-risk-regions-2026-01-01.md`; `sources/market-data/country-risk-2026-07-01.json`; `module-1-cross-checks-output.md` §3.
    - Answer: The scaled method. Damodaran multiplies each country's default spread by about 1.55, the ratio of equity risk to bond risk in his table, because a share in an emerging market is riskier than that government's bond (`facts.country-premium-method`). The ledger uses his regional premiums as published: 3.44% for Colgate's emerging-market mix and 1.04% for other developed markets, each added to the 3.61% (`country.exposures`). With raw default spreads the two would be 2.21% and 0.67%, the weighted premium 4.75% and not 5.38%, and the cost of equity 8.30% and not 8.76%. The method is worth 0.63 points of premium, which is more than any other single choice in this lesson except the historical alternative. We follow the course. The scaled figure is the cautious one for a company with 45% of sales in emerging markets.

## Module 1 Step — Questions for This Lesson

- **Mature-market equity risk premium**
  - What is the equity risk premium for a mature market today, by which method (implied, historical, survey), from which source? 3.61%, implied from the level of the S&P 500 and expected cash flows at the start of November 2026, from Damodaran's monthly workbook (`market.mature_erp`; `sources/market-data/market-rates-2026-11-19.json`). It is dated 2026-11-01, nineteen days before the analysis date, inside the validator's 45-day window but before an 8.8% fall in the index.

## Notes

The mature-market premium is 3.61% by the owner's decision, with the reason and the alternative stated above. Confidence is moderate, and lower than usual for this input, for one specific reason: the market moved sharply between the measurement date and the analysis date. The direction of the error is known (the true premium on 2026-11-20 is higher) and its size is bounded at roughly 0.35 points of premium and 0.23 points of cost of capital. The valuation report should carry that sensitivity next to its value per share. Each 0.25-point rise in the premium adds 0.17 points to the cost of capital (`facts.cost-of-capital-alternatives`).

One open point, raised in lesson 7: whether 3.61% is the mature-market premium or the United States premium, which in Damodaran's own tables now differ by 0.22% (`facts.us-country-premium-treatment`).
