---
title: "Colgate-Palmolive (CL) — Lesson 09: Beta Fundamentals"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 09: Beta Fundamentals

### Lesson 09 — Beta Fundamentals

- **Lesson 09, Session 9 · Part 1 — "Determinants of Beta and Regression Pitfalls — Stories Behind Company Betas"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-1.md))
    - Quote: "Companies that produce very discretionary products will have high betas."
    - Question for Colgate-Palmolive: Is what Colgate-Palmolive sells discretionary or essential for its customers, and does that explain where its beta sits relative to its peers? Has the business changed enough that a historical beta no longer describes it?
    - Sources needed: Product mix; behaviour in market downturns; industry betas; changes in the business.
    - Where to find: ledger `facts.product-mix-2025`, `facts.industry-beta-detail`, `facts.regression-diagnostics`, `facts.shareholder-return-2020-2025`, `beta.segments`; `peers` is omitted (`meta.omitted`), so the comparison is with Damodaran's industry averages.
    - Answer: Essential. Oral care is 44% of sales, personal care 17%, home care 16% and pet nutrition 23% (`facts.product-mix-2025`). People do not stop buying toothpaste, soap or pet food in a recession. Low-priced necessities should have a low beta, and Colgate's history agrees in direction: in the 24 months the index fell it lost 3.28% on average and Colgate lost 0.80% (`facts.regression-diagnostics`). Relative to peers: the peer set is not yet fixed, so the benchmark is the industry. The 110 US household products firms have an average beta of 0.8155 and an unlevered beta of 0.7411; the whole market's unlevered beta is 0.7557 (`facts.industry-beta-detail`). So the industry as a whole is about as risky as the average business, which is higher than the product story suggests, because the industry average includes many small makers of cosmetics and specialty products whose sales are more discretionary than toothpaste. Colgate's own 0.315 is far below the industry. Product type explains why Colgate should be below the industry average. It does not explain a number as low as 0.315. Has the business changed? Not much. The mix has been stable; Hill's has grown to 23% of sales, and the skin health push was small and has been written down. A change in the business is not why the historical beta misleads here.

- **Lesson 09, Session 9 · Part 2 — "The Three Determinants of Beta — Business, Operating Leverage, Financial Leverage"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-2.md))
    - Quote: "It makes your equity earnings much more volatile and through that, it makes your beta higher."
    - Question for Colgate-Palmolive: Separate Colgate-Palmolive's equity beta into business risk, operating leverage and financial leverage. At its current debt-to-equity ratio and marginal tax rate, how much of the levered beta comes from debt alone?
    - Sources needed: Unlevered beta; cost structure; debt-to-equity ratio; tax rate.
    - Where to find: ledger `beta.unlevered_bottom_up`, `company.debt_total`, `company.equity_value`, `market.tax_rate_marginal`, `facts.growth-and-margin-history`, `facts.uses-of-cash-2025`, `facts.segment-hurdle-rates`; model-output.md §1.
    - Answer: Business risk and operating leverage together are the unlevered beta, 0.6796 (`beta.unlevered_bottom_up`). They cannot be split with a number, but the cost structure says operating leverage is low. Gross profit is 60.1% of sales, so the cost of making the product is under half the price. The largest cost below that is advertising, $2,703M or 13.3% of sales, and advertising can be cut in a bad year (`facts.growth-and-margin-history`, `facts.uses-of-cash-2025`). A company whose biggest overhead is a choice has flexible costs. The history is consistent: operating income has changed less from year to year than sales have, 0.9% against 3.3% on average since 2017. That is not fixed costs magnifying swings; it is margin being spent on advertising as sales grew. Financial leverage is small. Debt is $8,084.0M against equity of $78,466.6M, a ratio of 0.1030. Levered beta = 0.6796 × (1 + (1 − 0.25) × 0.1030) = 0.7321 (model-output.md §1). Debt adds 0.0525, which is 7.2% of the levered beta (`facts.segment-hurdle-rates`). Nearly all of Colgate's equity risk is business risk.

## Module 1 Step — Questions for This Lesson

- **Beta fundamentals**
  - From what the company sells, should its beta be high or low? Do its businesses differ? Low: everyday necessities. The two businesses differ in degree. Household and personal products carry an industry unlevered beta of 0.7411; packaged food, the closest industry to pet food, 0.4694 (`beta.segments`).
  - From its cost structure (fixed vs. variable), what beta would you expect? Lower than a typical manufacturer's. A 60.1% gross margin and a large, adjustable advertising budget mean profits are cushioned when sales dip.
  - How much does its borrowing raise its beta? By 0.0525, from 0.6796 to 0.7321, or 7.2% of the total (model-output.md §1; `facts.segment-hurdle-rates`).

## Notes

All three determinants point the same way: essential products, flexible costs, little debt. A below-average beta is what the fundamentals predict, and the bottom-up levered beta of 0.7321 is below the market's. The fundamentals also say something about the direction of error. If anything, Colgate should sit below its industry's average, since it is the largest and most staple-heavy firm in a group that includes riskier ones. So 0.73 is more likely too high than too low, and the regression's 0.315 is more likely too low than too high. Confidence in the direction is good; in the exact figure, moderate. Lesson 10 turns that into a range.

The operating-leverage ratio of 0.28 (`facts.growth-and-margin-history`) is a rough measure on nine yearly changes and should not be quoted as a precise elasticity.
