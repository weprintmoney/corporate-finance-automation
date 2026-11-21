---
title: "Colgate-Palmolive (CL) — Lesson 21: Alternative Approaches"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 21: Alternative Approaches

### Lesson 21 — Alternative Approaches

- **Lesson 21, Session 21 · Part 1 — "APV: Unlevered Firm Value, Tax Benefits, and Expected Bankruptcy Costs"** ([transcript](../../03-financing-mix-and-dividends/lesson-21/session-21-part-1.md))
    - Quote: "As you borrow more money, you're increasing the probability that you will go bankrupt, right?"
    - Question for Colgate-Palmolive: Under the adjusted-present-value approach, what are Colgate-Palmolive's unlevered value, the present value of its tax benefits from debt, and its expected bankruptcy cost? What indirect-cost assumption is defensible for this kind of business, and what evidence supports it?
    - Sources needed: Firm value, debt, marginal tax rate, the rating at each debt ratio, default probabilities by rating, a bankruptcy cost.
    - Where to find: model-output.md §9 and §3; modules-2-4-cross-checks-output.md §6b; ledger `debt.bankruptcy_cost`, `facts.apv-sensitivity`, `facts.altman-10yr-default-probabilities`, `facts.bankruptcy-cost-guidance`, `market.tax_rate_marginal`, `company.debt_total`, `company.equity_value`.
    - Answer: The adjusted present value (APV) approach values the firm as if it had no debt, adds the tax savings debt brings, and subtracts the expected cost of bankruptcy. For Colgate today (model-output.md §9):

        | Item | $M |
        |---|---|
        | Firm value now | 86,550.6 |
        | Less the tax benefit of today's debt, 25% × $8,084.0M | 2,021.0 |
        | Plus expected bankruptcy cost at today's synthetic rating (AAA, default probability 0.07%) | 8.9 |
        | Unlevered firm value | 84,538.5 |

      The bankruptcy cost is the one new judgment in this lesson: 15% of firm value (`debt.bankruptcy_cost`), with a range of 10% to 25%. The lecture puts direct costs (lawyers, courts) at 5% to 10% of value and says indirect costs are higher where customers or suppliers abandon a firm in trouble; its Disney example uses 25% (`facts.bankruptcy-cost-guidance`). Colgate belongs near the low end. Its customers do not stop buying staples because the maker is in distress (lesson 20), and its brands would keep their value under a new owner. It is not at the very bottom, because suppliers and short-term lenders would tighten terms. The alternative, 25%, is the figure for a business whose customers care about its survival; it would move the optimum from 30% to 26% (`facts.apv-sensitivity`). The default probabilities are Altman's ten-year rates by rating from the lecture slides (`facts.altman-10yr-default-probabilities`), applied to the model's rating at each debt ratio.

        | Debt ratio | Rating | Default probability | Tax benefit $M | Expected bankruptcy cost $M | Firm value $M |
        |---|---|---|---|---|---|
        | 0% | AAA | 0.07% | 0.0 | 8.9 | 84,529.6 |
        | 9% (current) | AAA | 0.07% | 1,947.4 | 8.9 | 86,477.0 |
        | 10% | AAA | 0.07% | 2,163.8 | 8.9 | 86,693.4 |
        | 20% | A- | 2.50% | 4,327.5 | 317.0 | 88,549.0 |
        | 30% (APV optimum) | BBB | 7.54% | 6,491.3 | 956.1 | 90,073.6 |
        | 40% | CCC | 59.01% | 7,604.4 | 7,482.9 | 84,659.9 |
        | 50% | C | 85.00% | 5,020.2 | 10,778.7 | 78,780.0 |

      Value peaks at 30%, at $90,073.6M against $86,477.0M on the current row: a gain of $3,596.7M, or $4.52 a share. At 40% the expected bankruptcy cost ($7,482.9M) nearly cancels the whole tax benefit. At 50% and beyond the tax benefit itself shrinks, because interest exceeds operating income and the excess cannot be deducted.

- **Lesson 21, Session 21 · Part 2 — "The Relative Approach: Comparing to Sector Averages and Regression-Based Refinement"** ([transcript](../../03-financing-mix-and-dividends/lesson-21/session-21-part-2.md))
    - Quote: "By staying close to the sector, you're, in effect, making sure that if you make a mistake, you'll always have lots of company."
    - Question for Colgate-Palmolive: How does Colgate-Palmolive's debt ratio compare with its sector and its closest peers, and does the comparison agree with or contradict the cost-of-capital answer? If they conflict, which one is wrong and why?
    - Sources needed: Industry debt ratios; debt ratios for comparable companies.
    - Where to find: ledger `facts.industry-averages-2026`, `facts.peer-leverage-capital-iq`, `facts.industry-beta-detail`; model-output.md §1. `peers` is omitted from the ledger; the candidate list is in `sources/capital-iq/quick-comps.tsv`.
    - Answer: They agree on direction. Colgate's 9.34% is below every benchmark we have.

        | Benchmark | Debt ratio | Basis |
        |---|---|---|
        | Colgate | 9.34% | Gross debt with leases over market value of the firm (ledger) |
        | US household products industry, 110 companies | 15.36% | Market debt to capital, Damodaran, January 2026 |
        | US food processing industry, 78 companies | 30.43% | Same |
        | The two weighted by Colgate's segment sales | 18.77% | Same |
        | Colgate, Capital IQ basis | 7.2% | Net debt over enterprise value |
        | Median of ten candidate peers, Capital IQ basis | 17.6% | Same; range 5.6% to 42.0% |

      The industry says about 19% and the cost-of-capital approach says 30% unconstrained. Our recommended 20% (lesson 19) sits almost on the industry figure. That is a coincidence of method, not a derivation: the 20% came from a rating constraint, and the 18.77% is what similar companies happen to do. But the agreement is some comfort, for the reason in the quote. A Colgate at 20% would look like its industry; a Colgate at 30% would be among the most indebted of its peers on a debt-to-EBITDA basis (5.35 times against a peer median of 2.46 times net, `facts.debt-to-ebitda-at-targets`, `facts.peer-leverage-capital-iq`).
      Neither approach is wrong; they answer different questions. The relative approach tells you what is normal, and normal can be a shared mistake. Colgate's closest peers by size and pricing (Procter & Gamble, Kimberly-Clark, Church & Dwight) are all at 5.6% to 6.9% on Capital IQ's basis, so the companies most like Colgate are as lightly borrowed as it is. Either they are all leaving value on the table, or companies of this kind value a high rating for reasons the model does not price. Lesson 20's point about earnings relative to market value is part of the answer.
      The lecture's refinement, a regression of debt ratios on tax rate, earnings stability and cash flow across a sector, needs a fixed peer set with ledger-quality data. Ten candidates from a data service cannot support one, so it was not run.

## Cumulative Project — Questions for This Lesson

- **What is the expected tax benefit from borrowing money in the APV approach?**
  Treating debt as permanent, the tax benefit is the marginal tax rate times the debt: 25% × $8,084.0M = $2,021.0M today (model-output.md §9). At the 30% optimum it is $6,491.3M; at the recommended 20%, $4,327.5M. The assumption that the full deduction is usable is safe for Colgate up to 30%: operating income covers interest 2.65 times there (model-output.md §3).

- **What is the bankruptcy cost as a percent of value at your firm? (If you can estimate it)**
  15% of firm value if Colgate failed, by judgment, with a range of 10% to 25% (reasons in Part 1). The expected cost is that figure times the probability of default. Today: 0.07% × 15% of $84,538.5M is $8.9M, effectively nothing. At 20% debt (A−, 2.50%): $317.0M, 0.4% of value. At 30% (BBB, 7.54%): $956.1M, 1.1%. At 40% (CCC, 59.01%): $7,482.9M, 8.9%. Two cautions. The probabilities are ten-year rates from a table dated 2018, used as the lecture uses them. And Colgate has never been near distress, so the 15% is reasoned from the kind of business, not observed.

- **What is the optimal debt ratio using the APV approach?**
  30% at our 15% bankruptcy cost. The model also reports the two ends of the lecture's range: at 10% the optimum is 34%, and at 40% it is 26% (model-output.md §9). At 25%, the top of our own range, it is also 26% (`facts.apv-sensitivity`). So across every bankruptcy cost anyone would defend, the APV optimum is between 26% and 34%. Those are the same two ratios the cost of capital approach found tied at 8.14% (26% and 30%, lesson 18), plus the last ratio before the rating falls to B+. The judgment moves the answer within that band and never out of it, because the default probability rises so sharply below BBB that it swamps the choice of cost.

- **If it is different from the optimal using the cost of capital approach, how would you explain the difference?**
  It is not different: 30% under both. The dollar gains differ because the methods price distress differently.

  | Measure of the gain from moving to 30% | $M | Per share |
  |---|---|---|
  | Cost of capital approach, model (lesson 19) | 3,064.4 | $3.86 |
  | APV, model | 3,596.7 | $4.52 |
  | Cost of capital approach, professor's workbook | 5,806 | $7.30 |

  The cost of capital approach passes distress through the interest rate and the beta; the APV approach through a probability times a loss. APV is a little higher here because it treats the tax saving as a permanent amount (25% of the debt) and charges only $956.1M for risk at BBB, where the cost of capital approach charges a higher cost of equity on all of the equity. Both rest on the same synthetic ratings, so they share the weakness noted in lesson 19: the table is more generous than S&P has been.

## Notes

Three approaches now point the same way: cost of capital 30%, APV 30% (26% to 34% across bankruptcy costs of 10% to 40%), industry about 19%. All are above Colgate's 9.34%. That agreement is the strongest evidence in the project that Colgate is under-borrowed, and it is why confidence in the direction is high.

On the size: the two computed methods share one model of ratings and so are not independent, and the industry figure is the only one that does not depend on it. We keep the recommendation at 20%. It is inside the range the industry occupies, it holds a single-A synthetic rating under stress, and by APV it is worth $2,072.0M of the $3,596.7M available, 57.6% (`facts.apv-sensitivity`).

New ledger input in this lesson: `debt.bankruptcy_cost` of 15%, marked as an estimate with a range. It turned on section 9 of the model and changed nothing in sections 1 to 8.
