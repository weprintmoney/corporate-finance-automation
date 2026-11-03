---
title: "Comcast Corporation (CMCSA) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Comcast Corporation (CMCSA) — Lesson 12: Debt: Measure and Cost

Quick mode, blind, as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  None of the fetched filings states one (`debt.rating_actual` is null); the revolver margin is tied to 'Comcast's credit rating'. From memory, Comcast was rated A3/A-/A- before the cutoff (read.md, Outside knowledge); that is not used in the ledger.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  EBIT $18,155M ÷ interest $4,409M = 4.12x → A- in the large-firm table, spread 0.89%, pre-tax cost of debt 5.33% (model-output.md section 2). Adding back acquisition amortization gives A (5.22%); EBITDA gives AA (4.99%).

- **If the two differ, why?**
  The synthetic A- matches the remembered agency A-/A3, so there is no gap to explain.

- **What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?**
  $84,600M at fair value against $94,612M carrying (`company.debt_market`, `company.debt_book`), about 11% below book: the debt is fixed rate (`debt.rate_type`) with long maturities (`debt.maturity_years` ≈ 13.9 years) and coupons set when rates were lower (4.0% effective, `debt.kd_pretax_observed`). Face value is about $100,500M (`company.debt_face`, estimate).

- **What is the debt value of lease commitments, including leases signed but not yet started?**
  $6,097M (`company.lease_debt`), the present value at 4.2% over an 18-year average term; the note says leases entered into or modified in the year were not material and reports none signed but not yet commenced.

- **Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet?**
  No guarantee of unconsolidated debt (Universal Beijing's debt is consolidated). $313M of undrawn letters of credit and a theme-park revenue-interest put are contingent, not debt (`company.off_balance_sheet_debt` = 0). Programming and sports-rights commitments are large but are executory content purchases, not borrowing.

- **How much interest was capitalized into construction, and what does coverage look like once it is added back?**
  None disclosed after Epic Universe opened in May 2025 (`company.interest_capitalized` = 0); coverage unchanged at 4.12x.

- **Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income?**
  No change in useful lives is disclosed in the 2025 10-K or the Q1 2026 10-Q.

- **What marginal tax rate applies to the after-tax cost of debt?**
  25% (`market.tax_rate_marginal`): after-tax cost of debt 4.00% (model-output.md section 1).

## Notes

A- synthetic rating; market value of debt used in the weights.
