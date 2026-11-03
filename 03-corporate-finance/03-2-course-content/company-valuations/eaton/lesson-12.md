---
title: "Eaton Corporation plc (ETN) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Eaton Corporation plc (ETN) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

Quick mode: only the question-bank entries with a `signals` field are answered here. No transcript-layer entries carry a signal, so none are listed.

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  S&P A-, Moody's A3, both stable as of the 2025 10-K (`debt.rating_actual`). On the January 2026 large-firm table the A- spread is 0.89%, so the pre-tax cost of debt is 4.44% + 0.89% = 5.33% (model-output.md section 1). No rating action appears in filings through 2026-06-30.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  EBIT 5,173 ÷ run-rate interest 873 = 5.93x → A+, 5.14% (model-output.md section 2). The interest figure is an estimate (`company.interest_expense`, range 800-950) built from the filed coupons on the March 2026 notes and the commercial paper balance, because 2025's interest (351 paid) predates the $11.1B debt build.

- **If the two differ, why?**
  Agencies look at debt to EBITDA as well as coverage. Debt to EBITDA went from 1.73x at 2025 year-end to 3.55x at 2026-03-31 on 2025 EBITDA (`facts.debt-to-ebitda-2025-12-31`, `facts.debt-to-ebitda-2026-03-31`), a level agencies usually tolerate at A- only with a credible deleveraging plan. The synthetic rating also uses pre-acquisition EBIT. The agency rating is the better guide to the marginal cost of borrowing.

- **What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?**
  Fair value 20,575 against carrying value 21,129 (`company.debt_market`, `company.debt_book`), 2.6% below book, mostly on the low-coupon euro notes (0.577% due 2030) and older fixed coupons. The ledger uses book (`company.debt_total` 21,918 with leases), and the difference is too small to matter.

- **What is the debt value of lease commitments, including leases signed but not yet started?**
  789 of operating lease liabilities (`company.lease_debt`, 2025 lease note). The 10-K lease note discloses no material leases signed but not yet started.

- **Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet?**
  None disclosed. Letters of credit of 350 are performance guarantees, not borrowings (`company.off_balance_sheet_debt` 0).

- **How much interest was capitalized into construction, and what does coverage look like once it is added back?**
  No capitalized interest is disclosed; coverage is unchanged.

- **Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income?**
  No change in useful lives is disclosed in the 2025 10-K or the Q1 2026 10-Q.

- **What marginal tax rate applies to the after-tax cost of debt?**
  25% (`market.tax_rate_marginal`), the Irish statutory rate Eaton reconciles from, and close to the US federal-plus-state rate where most of the debt sits. The 2025 effective rate was 17.1% (`market.tax_rate_effective`).

## Notes

> ⚠️ **Discretionary Decision: cost of debt**
> **Chose:** the agency rating's spread (A-, 5.33%). **Why:** it is the marginal cost of new money, and the March 2026 ten-year notes priced at 4.80%, close to it. **Alternative:** the observed blended rate of 4.13% → cost of capital 9.59%, value $158.19 (alternatives/kd-observed-output.md). **Confidence:** high.

> ⚠️ **Discretionary Decision: debt date**
> **Chose:** debt at 2026-03-31 (21,918 with leases), after the Boyd Thermal financing, with 2025 operating income. **Why:** that debt exists on the analysis date and the share price reflects it. **Alternative:** 2025 year-end debt (10,684) → debt ratio 6.07%, optimum 20%, value $184.19 (alternatives/debt-at-2025-year-end-output.md). That value is too high because it keeps the acquired revenue but drops the debt that paid for it. **Confidence:** high on the date; medium on pairing it with 2025 EBIT, which excludes the acquired businesses.
