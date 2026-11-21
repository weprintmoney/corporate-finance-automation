---
title: "Colgate-Palmolive (CL) — Lesson 30: Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 30: Cash Flows

### Lesson 30 — Cash Flows

- **Lesson 30, Session 30 · Part 1 — "Three Cash Flow Definitions and Matching Discount Rates"** ([transcript](../../04-dividends-and-valuation/lesson-30/session-30-part-1.md))
    - Quote: "So free cash flow to equity is after debt payments, free cash flow to the firm is before debt payments."
    - Question for Colgate-Palmolive: What is Colgate-Palmolive's base-year free cash flow to the firm (after-tax operating income minus net capital spending minus the change in working capital), what reinvestment rate does it imply, and which discount rate pairs with it?
    - Sources needed: Operating income, tax rate, capital spending, depreciation, working capital change, stock-based compensation.
    - Where to find: model-output.md §8; ledger `facts.cash-flow-bridge-2025`, `facts.fcff-fcfe-2021-2025`, `company.sbc`, `modeling_choices.sbc_treatment`.
    - Answer: $3,578.8M for 2025 (model-output.md §8).

        | Step | 2025 $M |
        |---|---|
        | Operating income before the write-down | 4,225 |
        | Less tax at 25% | 1,056.2 |
        | After-tax operating income | 3,168.8 |
        | Less capital spending net of depreciation (564 − 630) | −66 |
        | Less change in working capital | −344 |
        | Reinvestment | −410 |
        | Free cash flow to the firm | 3,578.8 |

      The reinvestment rate, reinvestment divided by after-tax operating income, is −12.94%. It is negative: Colgate spent less on plant than it charged in depreciation, and working capital handed back cash. So free cash flow was 112.9% of after-tax operating income (`facts.cash-flow-bridge-2025`). No business can do that forever, which is why the valuation does not project this year forward as it stands (lesson 31).
      Three choices sit inside the figure.
        - The $919M write-down is added back, and restructuring and litigation charges are left in, because Colgate books such charges most years (README, decisions). The alternative, reported operating income of $3,306M, would treat a non-cash, one-time charge as a yearly cost.
        - Stock-based compensation, $155M, is left as an expense and not added back (`modeling_choices.sbc_treatment`). Shares given to employees are a real cost to the other shareholders.
        - Acquisitions are left out of this figure and shown separately. Colgate paid $293M for one in 2025. Counted, FCFF is $3,285.8M (`facts.fcff-fcfe-2021-2025`).
      The discount rate that pairs with FCFF is the cost of capital, 8.34%, because the cash flow is before payments to lenders and so belongs to lenders and shareholders together. FCFE pairs with the cost of equity, 8.76%. Dividends, the third cash flow the lecture names, would also pair with the cost of equity. Mixing them, for instance discounting FCFF at the cost of equity, is the error the lecture warns against.

## Cumulative Project — Questions for This Lesson

- **What is the current cost of equity and capital for your firm? How might these numbers change in the future?**
  Cost of equity 8.76%; cost of capital 8.34% (model-output.md §1). Built from a riskfree rate of 4.82%, a levered beta of 0.7321, an equity risk premium of 5.38% weighted by where Colgate sells, a pre-tax cost of debt of 5.74%, and debt at 9.34% of value.
  How they might change, and what the valuation assumes:

  | Reason for change | Cost of capital | Treatment |
  |---|---|---|
  | None: today's rate | 8.34% | Used for years 1 to 5 |
  | The company matures further | 8.43% | Used from year 10 on, reached in steps over years 6 to 10. It is the riskfree rate plus the 3.61% premium for a mature market, the rate of a typical mature company |
  | The workbook's own default for a mature company | 9.05% | Not used; quoted. It adds the workbook's January premium of 4.23% to today's riskfree rate, mixing two dates |
  | Colgate moves to 20% debt, as lesson 19 recommends | 8.22% | Not in the base case; valued in lesson 34 |
  | The beta is wrong: 0.63 to 0.80 | 7.84% to 8.67% | Sensitivity: $63.82 to $60.56 a share |
  | The equity risk premium is higher after the November fall in share prices | up to 8.57% | Sensitivity only (`facts.erp-november-bound`) |

  Two things to notice. First, for most companies the cost of capital falls as they mature. For Colgate the stable rate (8.43%) is a little above today's (8.34%), because Colgate is already less risky than the average mature company. We accept the small rise: assuming Colgate stays safer than average forever is a stronger claim than we want to make, and it is worth only $0.81 a share (`facts.ginzu-sensitivities`). Second, the beta uncertainty that dominated lessons 8 to 10 barely matters to value. The whole 0.63 to 0.80 range moves value by $3.26, about 5% of it (`facts.valuation-arithmetic`) (`facts.ginzu-base-case-detail`). The cost of capital is not where this valuation is won or lost.

- **Estimate the free cash flows to the firm & equity in the most recent five years for your firm?**
  In $ millions (`facts.fcff-fcfe-2021-2025`):

  | Year | Operating income before write-downs | After tax at 25% | Reinvestment | Reinvestment rate | FCFF | Acquisitions | FCFF after acquisitions | FCFE |
  |---|---|---|---|---|---|---|---|---|
  | 2021 | 3,903 | 2,927.2 | 153 | 5.23% | 2,774.2 | 0 | 2,774.2 | 2,409 |
  | 2022 | 3,614 | 2,710.5 | 826 | 30.47% | 1,884.5 | 809 | 1,075.5 | 2,518 |
  | 2023 | 3,984 | 2,988.0 | −328 | −10.98% | 3,316.0 | 0 | 3,316.0 | 2,314 |
  | 2024 | 4,268 | 3,201.0 | −404 | −12.62% | 3,605.0 | 0 | 3,605.0 | 2,885 |
  | 2025 | 4,225 | 3,168.8 | −410 | −12.94% | 3,578.8 | 293 | 3,285.8 | 2,712 |
  | Five years | | 14,995.5 | −163 | −1.09% | 15,158.5 | 1,102 | 14,056.5 | 12,838 |

  Definitions. FCFF is after-tax operating income, plus depreciation, less capital spending, less the change in working capital. FCFE is the definition used in the professor's `dividends.xlsx` (lesson 26): net income plus depreciation and write-downs, less capital spending and acquisitions, less the change in working capital, plus net new debt. The 2023 to 2025 FCFF rows are the model's (model-output.md §8); 2021 and 2022 are built the same way from the SEC data file.
  Reading the table.
    - FCFF averaged $3,032M a year and FCFE $2,568M. Both are steady except for 2022, when working capital absorbed $675M and Colgate bought a business for $809M.
    - Over five years Colgate reinvested nothing, net: −$163M, or −1.09% of after-tax operating income. Counting the $1,102M of acquisitions, it reinvested $939M, 6.26%. Either way this is a business that turns almost all its profit into cash.
    - FCFE is lower than FCFF by roughly the after-tax interest bill and the acquisitions, and higher by net borrowing; the two tell the same story.

## Notes

What this lesson establishes: the base cash flow, the pairing of FCFF with the 8.34% cost of capital, and the fact that reinvestment has been near zero.

Why the valuation's starting point differs from the 2025 figures above. The workbook starts from the twelve months to 2026-09-30: operating income of $4,080M (reported $3,161M plus the $919M write-down), taxed at the 23.5% rate Colgate actually pays, rising to the 25% statutory rate by year 10 (`facts.ginzu-inputs`). The model's section 6 cross-check starts from 2025 and taxes at 25% throughout. Each is stated where used.

Confidence: high on the five-year figures, which come from filed statements. The judgment that matters is the treatment of charges. If restructuring charges were treated as one-time and taken out, base operating income would be about $156M a year higher (`facts.valuation-input-evidence`); we keep them in because Colgate has booked them in every one of the last four periods.

Used later: the near-zero reinvestment rate is why lesson 31 cannot use the simple growth formula.
