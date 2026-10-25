---
title: "SolarWinds (SWI) — Lesson 09: Beta Fundamentals"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 09: Beta Fundamentals

### Lesson 09 — Beta Fundamentals

- **Lesson 09, Session 9 · Part 1 — "Determinants of Beta and Regression Pitfalls — Stories Behind Company Betas"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-1.md))
    - Quote: "Companies that produce very discretionary products will have high betas."
    - Question for SolarWinds: Is what SolarWinds sells discretionary or essential for its customers, and does that explain where its beta sits relative to its peers? Has the business changed enough that a historical beta no longer describes it?
    - Sources needed: Business description and retention data from the 10-K; the industry beta the ledger uses; the peer set; a regression beta if one exists.
    - Where to find: `sources/filings/swi-10k-fy2024.md` (Item 1; MD&A, Revenue); `sources/market-data/industry-betas-2025-01-05.json`; `inputs.yaml` fields `beta.unlevered_bottom_up`, `peers`; `meta.omitted` for `beta.regression_beta`.
    - Answer: Mostly essential. SolarWinds sells software that monitors networks, servers, databases and applications. Customers renew it because the alternative is running IT blind. The 10-K shows this in retention, not adjectives: subscription net retention was 99% and the perpetual-license maintenance renewal rate was 97% (facts.net-retention-subscription, facts.maintenance-renewal-rate). Recurring revenue (subscription plus maintenance) was 93.5% of the $796.9M total (facts.recurring-revenue-share; `company.revenue`), across more than 300,000 customers (facts.customer-count). Only the $51.8M of new perpetual licenses (6.5%, facts.license-revenue) is a one-time purchase a customer could defer. That points to a business beta at or below the market. The ledger's unlevered beta is 1.22 (`beta.unlevered_bottom_up`, the cash-corrected average of 333 US firms in Damodaran's Software (System & Application) group, January 2025), above the all-market figure of 0.82 (facts.industry-beta-all-market) and below the 1.60 of Software (Internet) (facts.industry-beta-software-internet). So the group SolarWinds sits in is riskier than average, because software demand rises and falls with technology budgets and software firms carry heavy fixed costs. SolarWinds' own product is stickier than the group's typical product. We kept 1.22 and did not lower it: one company's retention figures are a reason to doubt the group beta, not a measurement that replaces it. The business has changed enough that a historical beta would mislead. Silver Lake and Thoma Bravo bought it in 2016, it re-listed in 2018, the 2020 SUNBURST attack changed how customers viewed it, and and the 2021 spin-off of N-able split off its managed-service-provider business. In 2022 it repaid $664.4M of debt (`company.history`, 2022 `debt_repaid`). A beta from price history before those events measures a different company with a different debt load. No regression beta exists anyway: the stock was delisted in April 2025 and free sources no longer serve its price history (`meta.omitted`). The eight peers in the ledger were chosen for relative valuation and carry no betas in the ledger, so no peer-by-peer beta comparison is made.

- **Lesson 09, Session 9 · Part 2 — "The Three Determinants of Beta — Business, Operating Leverage, Financial Leverage"** ([transcript](../../01-foundations-and-discount-rates/lesson-09/session-9-part-2.md))
    - Quote: "It makes your equity earnings much more volatile and through that, it makes your beta higher."
    - Question for SolarWinds: Separate SolarWinds' equity beta into business risk, operating leverage and financial leverage. At its current debt-to-equity ratio and marginal tax rate, how much of the levered beta comes from debt alone?
    - Sources needed: Debt, equity value, unlevered beta, marginal tax rate; cost structure for the operating leverage view.
    - Where to find: `inputs.yaml` fields `company.debt_total`, `company.equity_value`, `beta.unlevered_bottom_up`, `market.tax_rate_marginal`; model-output.md §1; 10-K income statement.
    - Answer: Business risk and operating leverage are both inside the 1.22, because the industry average is taken across firms that have the same kind of cost structure; the lesson's point is that they cannot be separated by arithmetic, only judged. Financial leverage is the part we can compute. Debt of $1,285.0M against equity of $2,604.9M gives debt to equity of 0.4933 (model-output.md §1). Levered beta = 1.22 × (1 + (1 − 0.25) × 0.4933) = 1.6714 (model-output.md §1). Debt alone adds 1.6714 − 1.22 = 0.4514 of beta (arithmetic). That is 37.0% on top of the business beta, and 27.0% of the levered beta. Operating leverage: the 10-K shows cost of revenue of only $83.3M (10.5% of revenue, facts.cost-of-revenue-2024) against operating expenses of $505.2M (63.4%, facts.operating-expenses-2024), and most of those are salaries for 2,107 employees (facts.employees-2024). Those costs do not fall when a quarter is weak. The 2023 to 2024 record shows the effect: revenue grew 5.0% (`company.history`, 758.7 to 796.9) while operating income grew 38.6% (150.4 to 208.4; arithmetic; 2023 includes lease impairment and restructuring charges, so the true multiple is somewhat lower). A high fixed-cost base is why the industry beta is 1.22 and not near 0.8. Both amplifiers, fixed costs and borrowing, are present, and the second one is a choice the 2016 buyout made.

## Module 1 Step — Questions for This Lesson

- **Beta fundamentals** (`m1-step-09`)
    - From what the company sells, should its beta be high or low? Do its businesses differ? Low to middling on product: renewals of 99% and 97% and 93.5% recurring revenue (facts above) describe a product customers keep. The businesses do not differ in any way the filings let us measure: SolarWinds reports one segment (10-K note 16, "We operate as a single reportable segment"). It sells through three contract types (subscription $304.5M, maintenance $440.6M, license $51.8M; facts.subscription-revenue, facts.maintenance-revenue, facts.license-revenue), which is a way of billing, not a different line of business.
    - From its cost structure (fixed vs. variable), what beta would you expect? Higher than the product alone suggests. Variable cost is small (cost of revenue 10.5% of revenue) and fixed cost is large (operating expenses 63.4%). A sales dip falls almost entirely to operating income. The 38.6% profit rise on 5.0% revenue growth is the same effect running upward.
    - How much does its borrowing raise its beta? From 1.22 to 1.6714, a rise of 0.4514 or 37.0%, at debt to equity of 0.4933 and a 25% tax rate (model-output.md §1).

## Notes

This lesson names the three things that set a beta: what the firm sells, how fixed its costs are, and how much it borrows. For SolarWinds the first is moderate, the second is high, and the third is the one that moves the most, because debt lifts 1.22 to 1.6714. The ledger carries no regression beta (delisting) and no segment betas (one segment), so the bottom-up beta is the only estimate; lessons 10 and 11 defend that choice. Lesson 13 uses the 1.6714 in the weighted average cost of capital.

The quote in Part 1 is true of SolarWinds in reverse: its product is not discretionary, so the high beta comes from cost structure and debt, not from the product.

Facts used here that are not yet in the ledger are listed in the run report: facts.net-retention-subscription, facts.maintenance-renewal-rate, facts.recurring-revenue-share, facts.customer-count, facts.subscription-revenue, facts.maintenance-revenue, facts.license-revenue, facts.cost-of-revenue-2024, facts.operating-expenses-2024, facts.employees-2024, facts.industry-beta-all-market, facts.industry-beta-software-internet.
