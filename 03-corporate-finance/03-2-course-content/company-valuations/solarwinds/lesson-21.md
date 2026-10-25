---
title: "SolarWinds (SWI) — Lesson 21: Adjusted Present Value Approach"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 21: Adjusted Present Value Approach

### Lesson 21 — Adjusted Present Value Approach

- **Lesson 21, Session 21 · Part 1 — "APV: Unlevered Firm Value, Tax Benefits, and Expected Bankruptcy Costs"** ([transcript](../../03-financing-mix-and-dividends/lesson-21/session-21-part-1.md))
    - Quote: "As you borrow more money, you're increasing the probability that you will go bankrupt, right?"
    - Question for SolarWinds: Under the adjusted-present-value approach, what are SolarWinds' unlevered value, the present value of its tax benefits from debt, and its expected bankruptcy cost? What indirect-cost assumption is defensible for this kind of business, and what evidence supports it?
    - Sources needed: Firm value, debt, marginal tax rate, the synthetic rating at each debt ratio, a default-probability table by rating, and evidence on what distress would cost a software vendor.
    - Where to find: `company.debt_total`, `company.equity_value`, `market.tax_rate_marginal`; model-output.md §3 (schedule of ratings and interest rates); the default-probability table on the lesson 21 slides (facts.altman-10yr-default-probabilities); `sources/filings/swi-10k-fy2024.md` (retention rates, goodwill, Item 1A) and `sources/filings/swi-10k-fy2020.md` (SUNBURST).
    - Answer: Method follows the lecture's Disney example, with SolarWinds' numbers. The model computes it in §9, solving the unlevered value so that the bankruptcy cost is a share of it; the bankruptcy cost is the ledger field `debt.bankruptcy_cost` (25%).
        - Firm value now: debt $1,285.0M (`company.debt_total`) plus equity $2,604.9M (`company.equity_value`) is $3,889.9M (model-output.md §1).
        - Tax benefit on current debt, perpetual: 25% × $1,285.0M = $321.2M (model-output.md §9).
        - Expected bankruptcy cost today: the 33% schedule row is rated B (model-output.md §3), which carries a 36.80% ten-year default probability (facts.altman-10yr-default-probabilities). With a bankruptcy cost of 25% of value (`debt.bankruptcy_cost`, judgment, below): 36.80% × 25% of the unlevered value is $361.6M (model-output.md §9).
        - Unlevered value: $3,889.9M − $321.2M + $361.6M = $3,930.2M (model-output.md §9).
        - Indirect-cost assumption (judgment): 25% of firm value in total, the midpoint of the lecture's 10% to 40% range, tested at both ends. Reasons it is not low: goodwill is $2,363.2M (`company.goodwill`) of $2,348.0M of invested capital (`company.invested_capital`), so almost nothing is worth much in a sale; the company sells trust (security-adjacent IT monitoring) and customers renew annually (10-K: "the majority of our contracts include annual subscription periods"), so a vendor in court gives customers a reason to leave at the next renewal. Reasons it is not high: the SUNBURST attack in 2020 did not drive customers away; by FY2024 the maintenance renewal rate was 97% and the subscription net retention rate 99% (facts.maintenance-renewal-rate, facts.net-retention-subscription). SUNBURST tested trust, not solvency, so it bounds the cost from below and does not settle it.
        - Schedule at 25% (model-output.md §9; value = unlevered + tax benefit − expected bankruptcy cost; interest over EBIT of $208.4M caps the tax benefit once interest exceeds operating income):

| Debt ratio | Rating (model §3) | Default prob. | Tax benefit $M | Expected bankruptcy cost $M | Firm value $M |
|---|---|---|---|---|---|
| 0% | AAA | 0.07% | 0.0 | 0.7 | 3,929.5 |
| 10% | AA | 0.51% | 97.2 | 5.0 | 4,022.5 |
| 20% | A- | 2.50% | 194.5 | 24.6 | 4,100.2 |
| 21% | A- | 2.50% | 204.2 | 24.6 | 4,109.9 |
| 30% | B+ | 25.00% | 291.7 | 245.6 | 3,976.3 |
| 33% | B | 36.80% | 320.9 | 361.6 | 3,889.6 |
| 40% | B- | 45.00% | 389.0 | 442.2 | 3,877.1 |
| 50% | C | 85.00% | 261.4 | 835.2 | 3,356.5 |
| 60% | D | 100.00% | 222.4 | 982.6 | 3,170.0 |
| 70% | D | 100.00% | 222.4 | 982.6 | 3,170.0 |

- **Lesson 21, Session 21 · Part 2 — "The Relative Approach: Comparing to Sector Averages and Regression-Based Refinement"** ([transcript](../../03-financing-mix-and-dividends/lesson-21/session-21-part-2.md))
    - Quote: "By staying close to the sector, you're, in effect, making sure that if you make a mistake, you'll always have lots of company."
    - Question for SolarWinds: How does SolarWinds' debt ratio compare with its sector and its closest peers, and does the comparison agree with or contradict the cost-of-capital answer? If they conflict, which one is wrong and why?
    - Sources needed: Debt ratios for the eight peers and the software industry, on the same basis as SolarWinds' 33.03%.
    - Where to find: `peers[].debt_ratio` in inputs.yaml (debt over debt plus market value of equity, same debt definition as the ledger per `sources/peer-filings/peer-facts-2025-02-05.md`); `sources/market-data/industry-betas-2025-01-05.json` (Software (System & Application), 333 firms, debt-to-equity 4.9%); model-output.md §1 and §3.
    - Answer: They agree on direction and disagree on size. SolarWinds' debt ratio is 33.03% (model-output.md §1). The eight peers range from 0.88% (Qualys) to 45.28% (Open Text); their median is 11.72% (average of the fourth and fifth values, NetApp 9.54% and Teradata 13.90%; facts.peer-debt-ratio-median). SolarWinds is 2.8 times the peer median (33.03 ÷ 11.72). The software industry's debt-to-equity is 4.9% (facts.industry-software-de-ratio), about 4.7% of capital. Only Open Text, which borrowed to buy Micro Focus (`peers` growth 28.6%, per the ledger note), carries more. The cost-of-capital answer is 21% against the current 33% (model-output.md §3), so both say over-levered. The conflict is the size of the gap: the sector says about 12%, the cost-of-capital approach says 21%. Neither is wrong; the sector figure is the weaker one. The peers are larger, mostly older businesses and none is a sponsor-controlled company that kept its 2016 buyout debt. The lecture's own adjustments point down for SolarWinds: heavy intangibles and weak coverage (1.85x, model-output.md §2) argue for less debt than the sector, not more. A regression of debt ratio on tax rate, earnings stability and cash flow needs a sector sample; eight peers cannot support one, so it was not run. Conclusion: SolarWinds is over-levered on all three views (sector 12%, cost of capital 21%, APV 21%); the only open question is how far.

## Cumulative Project — Questions for This Lesson

- **What is the expected tax benefit from borrowing money in the APV approach?**
  Perpetual-debt convention: marginal tax rate × debt = 25.00% × $1,285.0M = $321.2M (`market.tax_rate_marginal`, `company.debt_total`; model-output.md §9). Interest of $112.4M (`company.interest_expense`) is well under EBIT of $208.4M, so the full deduction is usable today. The assumption is generous: the term loan matures 2030-02-05 (`debt.maturity_years`) and is refinanced, not repaid. At the 21% optimum the benefit is $204.2M; at 40% it peaks at $389.0M, then shrinks because interest exceeds operating income.

- **What is the bankruptcy cost as a percent of value at your firm? (If you can estimate it)**
  Judgment: 25% of firm value if SolarWinds defaults, with 10% and 40% as the tested ends (reasons in Part 1). The expected cost is that percentage times the default probability for the rating. At today's 33% debt ratio (rated B, 36.80%) it is 36.80% × 25% = 9.2% of the unlevered value, $361.6M (§9). At 21% (rated A-, 2.50%) it is 0.625% of value, $24.6M. The Altman probabilities are for ten-year bonds, so the table overstates a one-year risk; the lecture uses it unadjusted and so does this answer.

- **What is the optimal debt ratio using the APV approach?**
  21%, where firm value peaks at $4,109.9M (model-output.md §9). This holds at a 40% bankruptcy cost too (§9). If the cost is only 10% the peak moves to 40% (§9): the answer depends on the bankruptcy cost, which the lecture calls the weakest input. The 40% case also sits on a B- rating with coverage of 1.51x (model-output.md §3), so a 10% cost is not a view this file holds. Grid limitation: only the debt ratios in model-output.md §3 were rated, so 21% is the best of those rows, not a searched optimum.

- **If it is different from the optimal using the cost of capital approach, how would you explain the difference?**
  At the 25% cost it is the same: 21% under both (model-output.md §3 for the cost of capital). The dollar gain differs: APV says moving from 33% to 21% adds $4,109.9M − $3,889.6M = $220.3M (§9), against the cost-of-capital value of moving of $144.4M (model-output.md §3). The two methods price distress differently: the cost-of-capital approach feeds it through the interest rate (the pre-tax cost of debt rises from 5.38% at A- to 7.43% at B and 19.93% at C, model-output.md §3) and the APV approach through a default probability times a 25% loss. They would also split if the bankruptcy cost were 10% (APV optimum 40%). The cost-of-capital approach holds firm value fixed and so shows only part of the gain.

## Notes

APV and the cost-of-capital approach land on the same 21%, which is the strongest support in the project for calling SolarWinds over-levered at 33.03%. The relative approach agrees on direction at about 12%. Lesson 22 uses that conclusion to set the path from 33% down. Two judgments carry the APV result: the 25% bankruptcy cost and the assumed 100% default probability at a D rating. Neither changes the 21% peak at 25% or 40%.
