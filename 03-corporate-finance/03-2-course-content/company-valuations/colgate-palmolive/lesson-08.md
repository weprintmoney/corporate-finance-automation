---
title: "Colgate-Palmolive (CL) — Lesson 08: Regression Betas"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 08: Regression Betas

### Lesson 08 — Regression Betas

- **Lesson 08, Session 8 · Part 1 — "Estimating Regression Betas — The Four Choices"** ([transcript](../../01-foundations-and-discount-rates/lesson-08/session-8-part-1.md))
    - Quote: "There's a reason why services latch on to the S&P 500 for U.S. companies."
    - Question for Colgate-Palmolive: For Colgate-Palmolive, which index, return interval and window are available for a regression beta, and are they clean enough (listing age, thin trading, a delisting, a change in the business) to give a usable estimate?
    - Sources needed: Monthly prices and dividends for Colgate; the S&P 500 with dividends; any event that breaks the series.
    - Where to find: ledger `beta.regression_beta` and its source note, `governance.marginal_investor`, `facts.product-mix-2025`; `sources/market-data/cl-vs-sp500-monthly-2020-12-to-2026-11.tsv`; `module-1-cross-checks.py`.
    - Answer: Index: the S&P 500, with dividends, because the investors who set Colgate's price are US institutions whose portfolios look like it (`governance.marginal_investor`). Interval: monthly. Window: five years, 60 monthly returns, November 2021 to October 2026 (prices from October 2021); November 2026 is left out because it is a part-month. Returns include dividends on both sides, which matters for a stock that pays out about 2% a year. The data is as clean as data gets: a continuous listing, heavy trading, no spin-off, no split in the window, and the same four product lines throughout (`facts.product-mix-2025`). That is the important point for what follows. When the regression gives a strange answer for Colgate, bad data is not the excuse.

- **Lesson 08, Session 8 · Part 2 — "Interpreting the Regression Beta — Jensen's Alpha, Standard Error, R-Squared"** ([transcript](../../01-foundations-and-discount-rates/lesson-08/session-8-part-2.md))
    - Quote: "Standard errors are features, not bugs. They're part of the process, we've got to learn to deal with them."
    - Question for Colgate-Palmolive: What are Colgate-Palmolive's regression beta, standard error, R-squared and Jensen's alpha, what do they say about past performance and about how much of its risk is firm-specific, and is the confidence interval too wide to trust on its own?
    - Sources needed: Regression output; a short-term risk-free rate for the window; returns against peers.
    - Where to find: ledger `beta.regression_beta`, `beta.regression_se`, `beta.regression_r2`, `beta.jensens_alpha`, `facts.regression-diagnostics`, `facts.jensens-alpha-estimate`, `facts.shareholder-return-2020-2025`, `facts.cost-of-capital-alternatives`; `module-1-cross-checks-output.md` §1 and §2; `professor-spreadsheet/results.md`.
    - Answer: Beta 0.315, standard error 0.158, R-squared 0.064, intercept 0.39% a month (`beta.*`). Capital IQ shows 0.31, so the estimate is reproduced. Reading each in turn. Beta: Colgate moved about a third as much as the market. Standard error: two standard errors either side is 0.00 to 0.63 (`facts.regression-diagnostics`). The data cannot rule out a beta of zero, which would mean shareholders in a consumer products company require no more than the risk-free rate. The interval is too wide to use on its own. R-squared: 6.4% of the risk is market risk and about 94% is the company's own. Jensen's alpha, which measures whether the stock did better than its beta predicted: the intercept has to be compared with the risk-free rate times (1 − beta). Monthly Treasury bill rates for the window are not in our files, so the figure is an estimate. Using today's 3.88% federal funds rate for every month gives about +0.17% a month, roughly +2.1% a year, and the alpha stays positive at any average short rate below 6.9% (`facts.jensens-alpha-estimate`). So on its own beta Colgate did slightly better than required. That sits oddly with a stock that returned 4.0% in five years while the index returned 96.2% (`facts.shareholder-return-2020-2025`), and the oddness is the lesson: with a beta of 0.315 almost nothing was required of it. Judge the same years with the bottom-up beta of 0.73 and the verdict reverses; the professor's dividend spreadsheet, which uses 0.73, shows returns below the required return in four of the five years 2021 to 2025 (`professor-spreadsheet/results.md`). The regression does not settle how Colgate performed. It shows that the answer depends on the beta, and the beta is what is in doubt.

## Module 1 Step — Questions for This Lesson

- **Regression beta**
  - What is the regression beta, against which index, over what window and interval? 0.315, against the S&P 500 total return index: 60 monthly returns, November 2021 to October 2026 (prices from October 2021) (`beta.regression_beta`).
  - What are the standard error and R-squared, and is the estimate reliable? 0.158 and 0.064 (`beta.regression_se`, `beta.regression_r2`). Not reliable enough to carry a valuation. The range runs from zero to 0.63, the estimate drifts between halves of the window (0.35 in the first thirty months, 0.25 in the last thirty, the second with a standard error of 0.34), and at 0.315 the cost of equity would be 6.51% (`facts.regression-diagnostics`, `facts.cost-of-capital-alternatives`). That is 0.77 points above the 5.74% Colgate would pay to borrow (model-output.md §1). Shareholders are paid after lenders and bear more risk, so a required return that close to the borrowing rate is not believable.

## Notes

The regression beta is reported and not used: owner's decision, with `modeling_choices.beta_source: bottom_up`. The alternative was to use 0.315, which would cut the cost of capital from 8.34% to 6.31% (`facts.cost-of-capital-alternatives`) and raise any discounted value by a large amount. The reasoning for the gap between 0.315 and the bottom-up 0.73 is analysis, and it is set out in lesson 10. What this lesson contributes is the evidence about the regression itself: clean data, a wide interval, and a cost of equity that fails a simple sanity check against the company's own borrowing rate. The low figure is not a quirk of the five-year window. The six large household peers have five-year betas of 0.28 to 0.58, with a median of about 0.41 (`facts.peer-betas-capital-iq`), and Damodaran's industry betas are built from the same recent years (`facts.damodaran-beta-method`).

The ledger's `beta.jensens_alpha` holds the raw intercept (0.0039 a month), not Jensen's alpha proper; the adjusted estimate is in `facts.jensens-alpha-estimate`. A file of monthly Treasury bill rates would turn the estimate into a computed figure.
