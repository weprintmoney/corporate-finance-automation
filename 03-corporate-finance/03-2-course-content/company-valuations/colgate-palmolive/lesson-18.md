---
title: "Colgate-Palmolive (CL) — Lesson 18: The Cost of Capital: Approach"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 18: The Cost of Capital: Approach

### Lesson 18 — The Cost of Capital: Approach

Two sources are quoted in this lesson and they are kept apart. "The workbook" is the professor's `capstru.xlsx`, filled in with Colgate's inputs (`professor-spreadsheet/results.md`; ledger `facts.capstru-detail`). "The model" is the repo's `model.py` (model-output.md §3), plus the same function run on a one-point grid (modules-2-4-cross-checks-output.md §6; ledger `facts.cost-of-capital-grid`). Both the workbook's summary and its per-ratio schedule are on operating income of $4,225M (`professor-spreadsheet/results.md`). The workbook steps in tens, so finer per-ratio detail below comes from the model.

- **Lesson 18, Session 18 · Part 1 — "The Cost of Capital Approach to the Optimal Debt Ratio"** ([transcript](../../02-investment-returns-and-financing/lesson-18/session-18-part-1.md))
    - Quote: "The optimal debt ratio for this company, if I stay true to the notion of minimizing cost of capital, is 40% debt."
    - Question for Colgate-Palmolive: Where does Colgate-Palmolive's cost of capital bottom out as the debt ratio is varied from 0% to 70%, and does its current ratio sit below, at, or above that point? How steep is the curve on each side of the minimum?
    - Sources needed: Operating income, firm value, unlevered beta, risk-free rate, equity risk premium, tax rate, the ratings table.
    - Where to find: model-output.md §3; ledger `facts.cost-of-capital-grid`, `facts.capstru-detail`, `modeling_choices.firm_size_table`, `market.ratings_table`.
    - Answer: At 30%, in both the workbook and the model. Colgate's 9.34% sits well below it. The model's schedule (model-output.md §3):

        | Debt ratio | Levered beta | Cost of equity | Coverage | Rating | Pre-tax cost of debt | Cost of capital |
        |---|---|---|---|---|---|---|
        | 0% | 0.680 | 8.48% | n/a | AAA | 5.44% | 8.48% |
        | 9% (current) | 0.730 | 8.75% | 9.97x | AAA | 5.44% | 8.33% |
        | 10% | 0.736 | 8.78% | 8.97x | AAA | 5.44% | 8.31% |
        | 20% | 0.807 | 9.16% | 4.12x | A- | 5.93% | 8.22% |
        | 30% (optimum) | 0.898 | 9.65% | 2.65x | BBB | 6.15% | 8.14% |
        | 40% | 1.019 | 10.30% | 0.88x | CCC | 13.89% | 10.56% |
        | 50% | 1.189 | 11.22% | 0.46x | C | 21.04% | 15.15% |

      The shape matters more than the minimum. On the left side the curve is nearly flat: from no debt at all to 30% debt the cost of capital falls from 8.48% to 8.14%, about a third of a point. On the right side it is a cliff: at 40% the rating is CCC and the cost of capital is 10.56%. So the gain from being at the optimum is small, and the penalty for overshooting it is large.
      The one-point grid shows how close the cliff is (`facts.cost-of-capital-grid`). The cost of capital reaches 8.14% twice: at 26%, the last ratio rated A−, and at 30%, the last rated BBB. At 31% the synthetic rating is BB+, below investment grade, and the cost of capital is back to 8.19%. By 35% it is 8.51%. The optimum is one point from the edge.

- **Lesson 18, Session 18 · Part 2 — "The Iterative Rating Loop and the Kink in the Cost of Capital Curve"** ([transcript](../../02-investment-returns-and-financing/lesson-18/session-18-part-2.md))
    - Quote: "My advice to companies is if you're going to make a mistake, be under-levered rather than over-levered."
    - Question for Colgate-Palmolive: Which coverage numerator (operating income, operating income plus acquisition amortization, or EBITDA) does Colgate-Palmolive's optimum depend on, and how far does the optimum move between them? Which one is defensible for this company, and where is the kink in the curve?
    - Sources needed: The three earnings measures; the model's schedule under each.
    - Where to find: model-output.md §2 and §3; ledger `modeling_choices.coverage_numerator`, `company.ebit`, `company.ebitda_standardized`, `company.acquisition_amortization`, `facts.cost-of-capital-grid`, `facts.capstru-coverage-reconciliation`, `facts.cash-flow-bridge-2025`.
    - Answer: The optimum does not move: 30% under all three (model-output.md §3). What changes is the rating at 30% and so the cost of capital there.

        | Numerator | Optimum | Rating at optimum | Cost of capital at optimum |
        |---|---|---|---|
        | Operating income, $4,225M (chosen) | 30% | BBB | 8.14% |
        | Plus acquisition amortization, $4,303M | 30% | BBB | 8.14% |
        | EBITDA, $4,855M | 30% | A− | 8.09% |

      Operating income is the defensible one for Colgate. Depreciation is a real cost here: capital spending is 1.02 times depreciation once the $78M of acquired amortization is set aside (`facts.cash-flow-bridge-2025`), so the cash that EBITDA counts is cash that has to be spent on replacing equipment. It is not available to pay interest.
      The workbook and the model agree on 30% and disagree on the rating there: the workbook says A3/A− with coverage of 3.18 and a cost of capital of 8.09%; the model says BBB with coverage of 2.65 and 8.14%. We traced the difference (`facts.capstru-coverage-reconciliation`). The workbook leaves the $267M of interest on existing debt as it is and charges the new rate only on the $17,881M of new debt: $267M + $17,881M × 5.93% = $1,327M, and $4,225M ÷ $1,327M = 3.18. The model reprices all $25,965M at the new rate: interest of $1,597M and coverage of 2.65. The same arithmetic reproduces the workbook's earlier 20% row to two decimals. That the workbook's "refinance existing debt" switch, left at its default, is the cause is our inference from that match, not something read from its formulas.
      Both are right about different moments. The workbook describes the first years after borrowing, while Colgate's old notes still pay coupons averaging 2.9%. The model describes where things settle once those notes are replaced at current rates. A capital structure is a long-term choice, so the model's BBB is the more cautious reading, and it is the one used for per-ratio detail here.
      The kinks: a small one between 26% and 27% (A− to BBB), a second between 30% and 31% (BBB to BB+, the line between investment grade and junk), and the cliff between 39% and 40% (B to CCC), where the cost of debt jumps to 13.89%.

## Cumulative Project — Questions for This Lesson

- **What is your firm's current debt ratio (and cost of capital)?**
  9.34% debt and a cost of capital of 8.34% (model-output.md §1; the workbook's current column agrees). One detail when comparing with the schedule: the 8.34% prices today's debt at 5.74%, the rate for Colgate's actual A+ rating. The schedule prices every row at the synthetic rating, which at 9% debt is AAA and 5.44%, so its current row shows 8.33%, and the model's value-of-moving figures start from 8.32% (model-output.md §3). The difference is two hundredths of a point and comes from the rating choice in lesson 12.

- **Based upon the cost of capital approach, what is the optimal debt ratio for your firm?**
  30%, from both sources.

  | | Workbook (`capstru.xlsx`) | Model |
  |---|---|---|
  | Optimal debt ratio | 30% | 30% |
  | Debt at the optimum | $25,965M | $25,965M |
  | Rating at the optimum | A3/A− | BBB |
  | Cost of capital, current to optimal | 8.34% to 8.09% | 8.32% to 8.14% |
  | Beta and cost of equity at the optimum | 0.90, 9.65% | 0.898, 9.65% |

  Colgate would need $17,881M more debt to get there (model-output.md §3), more than double what it has. How sure are we? Confident that the optimum is well above 9.34%: every earnings measure and both tools say so. Less confident that it is 30% and not 25%: the curve is flat between 20% and 30% (8.22% to 8.14%), the workbook steps in tens, and the model shows 26% and 30% tied. And 30% is the unconstrained answer. It ignores that the synthetic rating at 9% debt is AAA while S&P's actual rating is A+, two steps lower; if the agencies stay two steps below the table as debt rises, 30% would not be investment grade. Lesson 19 applies that and the other constraints. On reported operating income of $3,306M, with the write-down left in, the model's optimum is 23% (`facts.capstru-detail`); we do not use it, because the write-down is not a recurring cost.

## Notes

The unconstrained optimum is 30% debt against 9.34% today, lowering the cost of capital by about a fifth to a quarter of a point (0.19 in the model, 0.25 in the workbook). The direction is high-confidence. The exact figure is not, and the lesson's main finding is about shape: a flat curve up to 30% and a cliff just beyond it. With that shape, the professor's advice in the quote applies with force. Aiming for the exact minimum risks a great deal to gain very little.

Carried to lesson 19: the gain in value from moving, the stress test, and a recommended ratio below 30%. A correction to how lesson 12's note is read: the "8.32% and not 8.34%" starting point it flagged is confirmed and explained above.
