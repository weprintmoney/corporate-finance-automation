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
    - Where to find: ledger `beta.segments`, `beta.unlevered_bottom_up`, `facts.industry-beta-detail`, `facts.segment-results-2025`, `facts.segment-hurdle-rates`, `facts.regression-diagnostics`, `facts.cost-of-capital-alternatives`, `facts.shareholder-return-2020-2025`; `sources/market-data/industry-betas-2026-01-05.json`; `module-1-cross-checks-output.md` §1, §2 and §4.
    - Answer: Two businesses, two betas. Oral, Personal and Home Care is 77.37% of sales and takes the Household Products beta, 0.7411 unlevered, from 110 firms. Hill's Pet Nutrition is 22.63% and takes Food Processing, 0.4694, from 78 firms (`beta.segments`). Weighted: 0.6796. The Hill's choice is the owner's decision. Reason: Hill's makes and sells packaged food, its costs are ingredients and factories like any food company's, and the listed companies that own the big pet food brands are classified as food processors; two of them, General Mills and J. M. Smucker, are in Capital IQ's list of Colgate's comparables (`sources/capital-iq/quick-comps.tsv`). Damodaran's table has no pet food industry. The alternative was to treat Hill's as one more household product and use 0.7411 for the whole company. That would raise the cost of capital from 8.34% to 8.67% (`facts.cost-of-capital-alternatives`). It lost because Hill's sells through vets and pet stores, not alongside soap, and its demand is steadier than cosmetics. The weights are by sales, because the filing gives no value by segment. Weighting by operating profit instead puts Hill's at 21.18% and the beta at 0.6835, so the weighting method does not matter (`facts.segment-hurdle-rates`).

      Why the bottom-up beta and not the regression: the gap, explained. The bottom-up levered beta is 0.73 and the regression says 0.315. The gap of 0.42 is 2.6 standard errors of the regression (`facts.regression-diagnostics`), so it is not just noise in the regression; the two methods disagree, and one has to say why.

      1. The regression measured low correlation, not low risk. Colgate's monthly returns were 1.24 times as volatile as the index's, but the correlation between them was 0.25. A beta is the product of the two, about 0.31. Colgate was a risky stock whose ups and downs had little to do with the market's.

      2. That is a fact about the window as much as about Colgate. From 2021 to 2026 the index nearly doubled, 96.2% over five years to December 2025, while Colgate returned 4.0%. In 2022 the index lost 18.1% and Colgate lost 5.4%. In the 36 months the index rose it gained 3.94% on average and Colgate 1.74% (`facts.regression-diagnostics`, `facts.shareholder-return-2020-2025`). The market's big moves in these years came from things that do not change how much toothpaste is sold. Our files do not show what drove the index, so naming causes would be guesswork; what the data does show is that a five-year beta against this index describes these five years. The cost of capital is for cash flows over decades.

      3. The regression's answer fails a check that needs no statistics. A beta of 0.315 gives a cost of equity of 6.51%, 0.77 points above the 5.74% at which Colgate borrows (`facts.cost-of-capital-alternatives`; model-output.md §1). Equity that returns nothing to holders until lenders are paid cannot be that close to debt.

      4. The bottom-up figure errs too, in the other direction. It is an average over 110 household products firms, most of them far smaller and less essential than Colgate. Their average says what the business of selling such products is worth in risk terms; it probably overstates the risk of the largest toothpaste maker.

      So the truth is probably between the two, and nearer the bottom-up figure. A defensible range for the levered beta is 0.63, the top of the regression's interval, to 0.80, the all-household-products figure. That is a cost of capital of 7.84% to 8.67% around the 8.34% used (`facts.cost-of-capital-alternatives`). The bottom-up beta is used because its error is the smaller and the more cautious one, and because it describes the business and not the last sixty months.

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

Confidence: moderate. We are confident the regression beta is too low to use and confident of the direction of each method's error. We are not confident of the figure to two decimals; the range 0.63 to 0.80 is the honest statement, and the report should show value per share at 7.84% and 8.67% as well as 8.34%. The industry betas are dated 2026-01-05, ten months before the analysis date, inside the validator's 400-day window.

What would raise confidence: a peer set of large consumer staples companies with their own betas (lesson 35 fixes the peers), and a pet food pure play, which Damodaran's US table does not have.
