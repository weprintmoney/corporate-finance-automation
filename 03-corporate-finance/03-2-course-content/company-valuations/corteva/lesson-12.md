---
title: "Corteva (CTVA) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Corteva (CTVA) — Lesson 12: Debt: Measure and Cost

Quick mode, blind as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers come from `inputs.yaml` or `model-output.md`.

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  The filings refer to 'investment grade credit ratings' but disclose no agency rating, so `debt.rating_actual` is null.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  EBIT $2,438M ÷ interest $180M = 13.54x, which maps to AAA. Spread 0.40%, pre-tax cost of debt 4.84% (model-output.md section 2). The rating is AAA under all three numerators.

- **If the two differ, why?**
  There is no agency rating to compare. A AAA synthetic rating overstates Corteva's real credit standing. Agencies weigh agricultural cyclicality, Latin American receivables and legacy DuPont/Chemours liabilities. The coupon-weighted rate on its notes is about 4.8%, which is consistent (`meta.omitted` debt.kd_pretax_observed).

- **What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?**
  Fair value of long-term borrowings was $2,448M at 2026-03-31 against roughly the same carrying value (10-Q Note 11). Book is used (`company.debt_book` $3,356M including $667M of commercial paper).

- **What is the debt value of lease commitments, including leases signed but not yet started?**
  $415M, the present value of operating lease liabilities (`company.lease_debt`, 10-K Note 13). No uncommenced leases are disclosed.

- **Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts that pass the debt test?**
  It guarantees customer financing programs and has $183M of lease residual value guarantees. Both are contingent, so they are not added (`meta.omitted` company.off_balance_sheet_debt). The $2,434M pension and OPEB liability is debt-like and is tested as an alternative.

## Notes

Total debt $3,771M (`company.debt_total`).

> ⚠️ **Discretionary Decision: Debt measured at 2026-03-31, not at year end**
> **Chose:** the latest balance sheet before the analysis date (borrowings $3,356M, cash $1,966M). **Why:** it is closest to the price date. Corteva's debt is seasonal: commercial paper funds spring working capital, and the year-end balance is the trough.
> **Alternative:** year-end 2025 (borrowings $2,580M, cash $4,530M) → optimum 28%, value $52.05 (alternatives/debt-year-end-output.md).
> **Confidence:** medium.

> ⚠️ **Discretionary Decision: Pension not counted as debt**
> **Chose:** course default, borrowings plus leases. **Alternative:** add the $2,434M unfunded pension/OPEB → cost of capital 8.82%, optimum 23%, value $43.59 (alternatives/pension-as-debt-output.md). **Confidence:** medium. The $1.5B contribution the board approved for July 2026 turns part of this liability into actual cash spending.

> ⚠️ **Discretionary Decision: Coverage numerator is operating EBIT before other income and expense**
> **Chose:** EBIT $2,438M. **Alternative:** including exchange losses and the Bayer settlement (EBIT $1,732M) → optimum 17% (alternatives/ebit-after-other-expense-output.md). **Confidence:** medium.
