---
title: "SolarWinds (SWI) — Lesson 13: Weights for Cost of Capital"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 13: Weights for Cost of Capital

### Lesson 13 — Weights for Cost of Capital

- **Lesson 13, Session 13 · Part 1 — "Why Book Value Weights Don't Hold Up: Converting Book Debt to Market Debt"** ([transcript](../../02-investment-returns-and-financing/lesson-13/session-13-part-1.md))
    - Quote: "There is no good reason for using book value weights."
    - Question for SolarWinds: What are SolarWinds' market-value debt and equity weights, with lease debt included, and how different are they from book weights? Does including leases change the weights enough to matter?
    - Sources needed: Debt, lease debt, market equity value, book equity, book debt.
    - Where to find: `inputs.yaml` fields `company.debt_total`, `company.lease_debt`, `company.equity_value`, `company.equity_book`, `company.debt_book`; model-output.md §1.
    - Answer: Market weights: debt $1,285.0M and equity $2,604.9M (171.6M shares × the $15.18 unaffected price) make a firm value of $3,889.9M, so debt is 33.03% and equity 66.97% (model-output.md §1). Book weights: book equity of $1,400.7M against book debt of $1,206.6M plus leases of $49.4M give a debt share of 47.28% (model-output.md §1). The two differ by 14.25 points (47.28 − 33.03) because the market values the equity at 1.86 times its book value (2,604.9 ÷ 1,400.7), and the book debt is nearly equal to its market value. The book equity understates what shareholders' claim is worth, so book weights push the weight toward debt, the cheaper capital, and understate the cost of capital. Leases: they add $49.4M (`company.lease_debt`), 1.3 points of the 33.03% (49.4 ÷ 3,889.9). That is small, so including them does not change the weights much, but the lesson's rule is to count them and we do. Face value adds $29.1M more against book debt. Equity here is basic shares at the market price. The $187.0M of options and restricted stock units (`company.options_value`) is not added to the equity weight; adding it would raise equity by 7.2% (187.0 ÷ 2,604.9) and cut the debt weight a little. Judgment call; the DCF treats options and units as a separate claim on equity (model-output.md §6), so the weights keep them out. The model's book-weight figure includes leases, so the two weightings count debt the same way.

- **Lesson 13, Session 13 · Part 2 — "Bringing Cost of Equity and Debt Together: WACC as Hurdle Rate"** ([transcript](../../02-investment-returns-and-financing/lesson-13/session-13-part-2.md))
    - Quote: "That cost of capital is going to become a hurdle rate for your company."
    - Question for SolarWinds: What is SolarWinds' cost of capital, and should different parts of the business carry different hurdle rates? If the company reports one segment but runs businesses with different risk and growth, what would the divisional rates be?
    - Sources needed: Cost of equity, cost of debt, weights; segment information.
    - Where to find: model-output.md §1; 10-K note 16; `beta.segments` (listed in `meta.omitted`: one segment).
    - Answer: The cost of capital is 10.23% (model-output.md §1): 66.97% × 12.65% cost of equity + 33.03% × 5.33% after-tax cost of debt. Cost of equity is 4.43% risk-free + 1.6714 levered beta × 4.92% weighted equity risk premium. It is the minimum return a new investment must earn on its capital for SolarWinds' owners and lenders to come out ahead. Divisions: SolarWinds reports one segment and gives no profit or capital by product line, so there are no divisional rates, and a split could not be built from the filings without inventing weights (lesson 10). If one were tried, the observability subscription business would carry a higher unlevered beta than the maintenance base, so a rate above 10.23% for new product bets and below it for renewal conversions. That is a reason to treat 10.23% as a company-wide hurdle with judgment on top, not a measured divisional schedule.

## Cumulative Project — Questions for This Lesson

- **Counting both interest bearing debt and lease commitments, what is the market debt ratio for the firm?**
  33.03%. Debt of $1,285.0M ($1,235.7M term loan at face plus $49.4M leases) over firm value of $3,889.9M (model-output.md §1).

- **What is the levered beta for the firm?**
  1.6714 = 1.22 × (1 + (1 − 0.25) × 0.4933) (model-output.md §1).

- **If you can allocate debt across different divisions/businesses, what is the debt ratio for each business that the firm is in?**
  SolarWinds is one reportable segment (10-K note 16), so there is one business with a debt ratio of 33.03%. All of the debt is a single corporate term loan that is not allocated to products.

- **What is the levered beta for each division/business?**
  One business, so 1.6714. No segment betas are in the ledger.

- **What is the cost of capital of the firm, using market values for weights? How different would it have been, if you had used book values?**
  10.23% at market weights. At book weights it is 9.19% (book debt share 47.28%; model-output.md §1), 1.04 points lower (10.23 − 9.19). The book version overweights debt, the cheaper source, and keeps the same cost of equity and cost of debt. Market weights are the right ones, because the cost of capital is what investors require on what their claims are worth today. The book comparison includes leases.

- **What are the costs of capital of each of the company's divisions/businesses?**
  One business, so 10.23%.

## Skipped

- None. The three divisional questions are answered as single-business cases, because SolarWinds reports one segment.

## Notes

This lesson fixes the weights: 33.03% debt and 66.97% equity at market value, giving a cost of capital of 10.23%. That number discounts the forecast cash flows in the DCF (model-output.md §6) and is the starting point for the optimal debt analysis (§3), where the current 33% is compared with an optimum of 21%. It is a hurdle rate for the company, and lesson 14 tests whether SolarWinds earned it. Hybrid securities: none. One class of common stock, and 50 million preferred shares authorized but none issued (`governance.share_classes`), and no convertible debt appears in the debt note, so there is nothing to split into debt and equity.

The weights use the $15.18 unaffected price, not the $18.50 deal price, so the debt weight is not understated by the takeover premium.
