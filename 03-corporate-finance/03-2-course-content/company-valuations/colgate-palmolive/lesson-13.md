---
title: "Colgate-Palmolive (CL) — Lesson 13: Financing Weights"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 13: Financing Weights

### Lesson 13 — Financing Weights

- **Lesson 13, Session 13 · Part 1 — "Why Book Value Weights Don't Hold Up: Converting Book Debt to Market Debt"** ([transcript](../../02-investment-returns-and-financing/lesson-13/session-13-part-1.md))
    - Quote: "There is no good reason for using book value weights."
    - Question for Colgate-Palmolive: What are Colgate-Palmolive's market-value debt and equity weights, with lease debt included, and how different are they from book weights? Does including leases change the weights enough to matter?
    - Sources needed: Market value of equity, market value of debt, lease liabilities, book equity and book debt.
    - Where to find: ledger `company.equity_value`, `company.debt_market`, `company.lease_debt`, `company.debt_total`, `company.debt_book`, `company.equity_book`, `facts.weights-and-divisions`; model-output.md §1; modules-2-4-cross-checks-output.md §1.
    - Answer: At market value, debt is 9.34% of the firm and equity 90.66%: debt of $8,084.0M against equity of $78,466.6M, firm value $86,550.6M (model-output.md §1). At book value the picture reverses: debt with leases is $8,554M and Colgate shareholders' book equity is $54.0M, so book debt is 99.37% of book capital (`facts.weights-and-divisions`). The two sets of weights describe different things. Book equity is what is left of past share issues and retained profit after years of buybacks; it says nothing about what the business is worth. The market values the equity at about 1,453 times its book value. A lender or a shareholder deciding what return to demand looks at what the claim is worth today, which is why the course uses market weights, and why Colgate, which looks almost entirely debt-funded on its balance sheet, is in fact lightly borrowed.
      Leases do not change the answer. Without them the debt ratio would be 8.74%; with them it is 9.34%. Leases are 7.00% of total debt (`facts.weights-and-divisions`). They are included because they pass the debt test from lesson 12, not because they move the number.

- **Lesson 13, Session 13 · Part 2 — "Bringing Cost of Equity and Debt Together: WACC as Hurdle Rate"** ([transcript](../../02-investment-returns-and-financing/lesson-13/session-13-part-2.md))
    - Quote: "That cost of capital is going to become a hurdle rate for your company."
    - Question for Colgate-Palmolive: What is Colgate-Palmolive's cost of capital, and should different parts of the business carry different hurdle rates? If the company reports one segment but runs businesses with different risk and growth, what would the divisional rates be?
    - Sources needed: Cost of equity, after-tax cost of debt, weights; a beta and a debt ratio for each business.
    - Where to find: model-output.md §1; ledger `beta.segments`, `facts.segment-hurdle-rates`, `facts.weights-and-divisions`, `facts.industry-averages-2026`; modules-2-4-cross-checks-output.md §1.
    - Answer: The company's cost of capital is 8.34%: 90.66% equity at 8.76% and 9.34% debt at 4.30% after tax (model-output.md §1). It should not be the hurdle rate for everything Colgate does. Colgate reports two segments with different risk: Oral, Personal and Home Care (household products, unlevered beta 0.7411) and Hill's Pet Nutrition (priced as food processing, unlevered beta 0.4694). Using the company's debt ratio for both, the hurdle rates are 8.67% for Oral, Personal and Home Care and 7.24% for Hill's (`facts.segment-hurdle-rates`). A pet food plant judged at 8.34% is held to too high a bar, and a skin care acquisition judged at 8.34% to too low a one. That second case is not hypothetical: the $919M write-down in 2025 was on a skin care business.

## Cumulative Project — Questions for This Lesson

- **Counting both interest bearing debt and lease commitments, what is the market debt ratio for the firm?**
  9.34%. Interest-bearing debt at fair value $7,518.0M plus operating leases $566.0M is $8,084.0M; market value of equity is $78,466.6M (model-output.md §1). Debt to equity is 0.1030. Both debt figures are disclosed in the 10-K; nothing is estimated. Confidence: high.

- **What is the levered beta for the firm?**
  0.7321: the bottom-up unlevered beta of 0.6796 × (1 + (1 − 0.25) × 0.1030) (model-output.md §1). Debt adds 0.0525, or 7.2% of the levered beta (`facts.segment-hurdle-rates`). The uncertainty is in the unlevered beta (lesson 10: a range of 0.63 to 0.80 for the levered figure), not in the levering.

- **If you can allocate debt across different divisions/businesses, what is the debt ratio for each business that the firm is in?**
  The filings do not allocate debt: the debt note describes the company's notes as a whole, and the segment note gives no debt or interest by segment. Two allocations, both judgment (`facts.weights-and-divisions`):

  | Segment | A: company ratio for both (chosen) | B: industry ratios scaled to Colgate's total debt |
  |---|---|---|
  | Oral, Personal and Home Care | 9.34% | 7.73% |
  | Hill's Pet Nutrition | 9.34% | 15.32% |

  Allocation A is used, because Colgate borrows as one company and nothing in the filings says the pet food business supports more debt. Allocation B is the alternative the lecture describes: assume each division borrows like its industry. The industry averages are 15.36% for household products and 30.43% for food processing (`facts.industry-averages-2026`), which weighted by each segment's share of operating profit is 18.55%, twice what Colgate carries. Scaling both down by the same factor so they add back to Colgate's actual debt gives the B column.

- **What is the levered beta for each division/business?**
  Under allocation A: Oral, Personal and Home Care 0.7984 and Hill's 0.5057 (`facts.segment-hurdle-rates`). Under allocation B: 0.7877 and 0.5331 (`facts.weights-and-divisions`). The allocation moves each beta by 0.03 or less; the choice of industry for Hill's (lesson 10) matters far more.

- **What is the cost of capital of the firm, using market values for weights? How different would it have been, if you had used book values?**
  8.34% at market weights. At book weights it would be 4.33% (model-output.md §1), because 99.37% of book capital is debt and debt costs 4.30% after tax. The book figure is wrong by about four points, and wrong in the dangerous direction: a hurdle rate of 4.33% would wave through projects that destroy value. This is the clearest case the course could offer for market weights: a company with almost no book equity whose shares are worth $78.5 billion.

- **What are the costs of capital of each of the company's divisions/businesses?**

  | Segment | Cost of equity | Cost of capital (A, chosen) | Cost of capital (B) |
  |---|---|---|---|
  | Oral, Personal and Home Care | 9.12% | 8.67% | 8.69% |
  | Hill's Pet Nutrition | 7.54% | 7.24% | 7.17% |
  | Company | 8.76% | 8.34% | 8.34% |

  Costs of equity are under allocation A (`facts.segment-hurdle-rates`); allocation B gives 9.06% and 7.69% (`facts.weights-and-divisions`). The two allocations agree to within 0.07 points, so the divisional rates are robust to how debt is split. They are not robust to geography: the same toothpaste business has a dollar cost of capital of 7.38% in North America and 10.56% in Latin America (lesson 16, `facts.regional-hurdle-rates`).

## Notes

The cost of capital stays at 8.34%; this lesson adds no new input. What it adds is the contrast between market weights (9.34% debt) and book weights (99.37%), and two divisional hurdle rates, 8.67% and 7.24%. The book-weight contrast matters again in lesson 14, where return on equity turns out to be unusable for the same reason, and in lesson 17, where Colgate looks heavily borrowed on its balance sheet and lightly borrowed in fact.

Confidence: high on the weights, which are disclosed market values. Moderate on the divisional rates, which rest on the judgment that pet food carries the risk of food processing.
