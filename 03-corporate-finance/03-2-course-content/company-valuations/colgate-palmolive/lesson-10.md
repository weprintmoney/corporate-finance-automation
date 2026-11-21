---
title: "Colgate-Palmolive (CL) — Lesson 10: Bottom-Up Betas"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 10: Bottom-Up Betas

### Lesson 10 — Bottom-Up Betas

- **Lesson 10, Session 10 · Part 1 — "Bottom-Up Betas — Why They Beat Regression"** ([transcript](../../01-foundations-and-discount-rates/lesson-10/session-10-part-1.md))
    - Quote: "A bottom-up beta is more precise, more forward-looking, and more dynamic than a regression beta."
    - Question for Colgate-Palmolive: Is Colgate-Palmolive single-business enough to use one industry unlevered beta, or does it have segments different enough to need separate betas weighted by value? Which comparable set, and why?
    - Sources needed: Segment sales and profit; industry unlevered betas; the regression for comparison.
    - Where to find: ledger `beta.segments`, `beta.unlevered_bottom_up`, `facts.industry-beta-detail`, `facts.segment-results-2025`, `facts.segment-hurdle-rates`, `facts.regression-diagnostics`, `facts.cost-of-capital-alternatives`, `facts.shareholder-return-2020-2025`, `facts.peer-betas-capital-iq`, `facts.damodaran-beta-method`, `facts.ginzu-peer-beta-cases`; `sources/market-data/industry-betas-2026-01-05.json`; `module-1-cross-checks-output.md` §1, §2 and §4.
    - Answer: Two businesses, two betas. Oral, Personal and Home Care is 77.37% of sales and takes the Household Products beta, 0.7411 unlevered, from 110 firms. Hill's Pet Nutrition is 22.63% and takes Food Processing, 0.4694, from 78 firms (`beta.segments`). Weighted: 0.6796. The Hill's choice is the owner's decision. Reason: Hill's makes and sells packaged food, its costs are ingredients and factories like any food company's, and the listed companies that own the big pet food brands are classified as food processors; two of them, General Mills and J. M. Smucker, are in Capital IQ's list of Colgate's comparables (`sources/capital-iq/quick-comps.tsv`). Damodaran's table has no pet food industry. The alternative was to treat Hill's as one more household product and use 0.7411 for the whole company. That would raise the cost of capital from 8.34% to 8.67% (`facts.cost-of-capital-alternatives`). It lost because Hill's sells through vets and pet stores, not alongside soap, and its demand is steadier than cosmetics. The weights are by sales, because the filing gives no value by segment. Weighting by operating profit instead puts Hill's at 21.18% and the beta at 0.6835, so the weighting method does not matter (`facts.segment-hurdle-rates`).

      Why the bottom-up beta and not the regression: three readings, and what separates them. Colgate's own regression says 0.315, with a standard error of 0.158. Its six large household peers have five-year betas of 0.28 to 0.58, with a median of about 0.41 (`facts.peer-betas-capital-iq`). The industry average, levered at Colgate's debt, is 0.73. The gap of 0.42 between the first and the last is 2.6 standard errors of the regression (`facts.regression-diagnostics`), so it is not just noise in the regression; the readings disagree, and one has to say why.

      1. The regression measured low correlation, not low risk. Colgate's monthly returns were 1.24 times as volatile as the index's, but the correlation between them was 0.25. A beta is the product of the two, about 0.31. Colgate was a risky stock whose ups and downs had little to do with the market's.

      2. The gap is about which companies are averaged, not about the period. Damodaran's industry betas are built from the same recent years: weekly returns, with two-thirds weight on a two-year regression and one-third on a five-year one (`facts.damodaran-beta-method`). What differs is the sample. The industry tables average 110 household products firms and 78 food processors, many of them small. The two readings closest to Colgate, its own regression and its six largest peers, agree on a beta of roughly 0.3 to 0.4. As a description of these years: the index returned 96.2% over five years to December 2025 while Colgate returned 4.0%; in 2022 the index lost 18.1% and Colgate lost 5.4%; in the 36 months the index rose it gained 3.94% on average and Colgate 1.74% (`facts.regression-diagnostics`, `facts.shareholder-return-2020-2025`). That is how Colgate and its large peers behaved. It is not a reason to prefer the industry beta.

      3. The regression's answer fails a check that needs no statistics. A beta of 0.315 gives a cost of equity of 6.51%, 0.77 points above the 5.74% at which Colgate borrows (`facts.cost-of-capital-alternatives`; model-output.md §1). Equity that returns nothing to holders until lenders are paid cannot be that close to debt.

      4. The bottom-up figure errs too, in the other direction. It is an average over 110 household products firms, most of them far smaller and less essential than Colgate. Their average says what the business of selling such products is worth in risk terms; it probably overstates the risk of the largest toothpaste maker, and the large-peer median of about 0.41 says so directly.

      The base case keeps 0.73, for three reasons. It is the course's method. An average over 188 companies is far more precise than one regression or a median of six. And a beta near 0.3 gives a cost of equity of 6.51% against a borrowing rate of 5.74%. But the peer evidence says 0.73 is probably too high for Colgate. The honest range for the levered beta is 0.41, the large-peer median, to 0.80, the all-household-products figure. That is a cost of capital of 6.77% to 8.67%, against the 8.34% used (`facts.peer-betas-capital-iq`, `facts.cost-of-capital-alternatives`), and confidence in the beta is low. The low end matters to value: with 6.77% for five years, fading to the mature-company rate, a share is worth $68.32; with 6.77% forever, about $91.88. The base case is $61.83 and the price $98.71 (`facts.ginzu-peer-beta-cases`).

- **Lesson 10, Session 10 · Part 2 — "Bottom-Up Beta by Business — Aggregating and Levering"** ([transcript](../../01-foundations-and-discount-rates/lesson-10/session-10-part-2.md))
    - Quote: "Because the movie business is riskier than Disney as a company, you should demand much more of it, a higher hurdle rate."
    - Question for Colgate-Palmolive: If Colgate-Palmolive has businesses with different risk, what hurdle rate should each carry, which one is riskier than the company as a whole, and where would using one company-wide rate lead to the wrong investment decision?
    - Sources needed: Segment betas relevered; cost of equity and capital by segment; recent investments by segment.
    - Where to find: ledger `facts.segment-hurdle-rates`, `facts.segment-results-2025`, `facts.uses-of-cash-2025`, `facts.skin-health-writedown-2025`, `beta.segments`; `module-1-cross-checks-output.md` §4.
    - Answer: Relevering each industry beta at the company's debt-to-equity ratio and using the company's weighted premium: Oral, Personal and Home Care has a levered beta of 0.7984, a cost of equity of 9.12% and a cost of capital of 8.67%. Hill's has 0.5057, 7.54% and 7.24%. The company is 0.7321, 8.76% and 8.34% (`facts.segment-hurdle-rates`). Oral, Personal and Home Care is the riskier one. A single company rate of 8.34% goes wrong in both directions. It sets the bar 1.10 points too high for Hill's, so pet food projects such as the Prime100 purchase and new Hill's plants look worse than they are. It sets the bar 0.33 points too low for household and personal products, and that understates the problem, because the investments that failed were at the risky end of that segment: premium skin care sold in China (`facts.skin-health-writedown-2025`). A deal like Filorga deserved a hurdle rate above the segment's, with a discretionary-product beta and a China premium, not the company average. Two limits. The segments' debt ratios are not disclosed, so both are levered alike. And Hill's sells 66.4% in the United States against 22.8% for the other segment (`facts.segment-results-2025`), so its true premium is lower than the company's and its true hurdle rate lower still than 7.24%; the gap between the two businesses is wider than these figures show.

## Module 1 Step — Questions for This Lesson

- **Bottom-up unlevered beta**
  - What is the bottom-up unlevered beta from comparable firms, cash-corrected? 0.6796 (`beta.unlevered_bottom_up`). Both industry betas are Damodaran's January 2026 figures already corrected for the cash the comparable firms hold (`facts.industry-beta-detail`).
  - If the company has several businesses, what is each segment's beta and the weighted average? Oral, Personal and Home Care 0.7411 at a 77.37% weight; Hill's Pet Nutrition 0.4694 at 22.63%; weighted 0.7737 × 0.7411 + 0.2263 × 0.4694 = 0.6796 (`beta.segments`).

## Notes

This is the lesson where the valuation's biggest Module 1 judgment is made. Two owner's decisions are recorded with their reasons and alternatives: the bottom-up beta over the regression (the regression's 6.31% cost of capital was the alternative), and Food Processing for Hill's (0.7411 for the whole company, giving 8.67%, was the alternative).

Confidence: low on the beta. We are confident that 0.315 alone cannot carry the valuation, because it puts the cost of equity next to the borrowing rate, and that the industry average is precise as an average. We are not confident that the average fits Colgate: the peer evidence says 0.73 is probably too high. The range 0.41 to 0.80 is the honest statement, and the report should show value per share at 6.77% and 8.67% as well as 8.34%. The industry betas are dated 2026-01-05, ten months before the analysis date, inside the validator's 400-day window.

What would raise confidence: bottom-up betas for a hand-picked set of large consumer staples companies, estimated by the course's method in place of Capital IQ's five-year figures, and a pet food pure play, which Damodaran's US table does not have.
