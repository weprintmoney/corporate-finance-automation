---
title: "The Coca-Cola Company (KO) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

Quick mode: no transcript-layer entries carry a signal for this lesson, so none are answered here.

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  A1/A+ (`debt.rating_actual`): spread 0.70%, pre-tax cost 5.14% (`model-output.md` section 1).
  
  > ⚠️ **Discretionary Decision: cost of debt**
  > **Chose:** the actual rating's rate, 5.14%. **Why:** the 3.3% average effective rate (`debt.kd_pretax_observed`) is the coupon on bonds issued when rates were low, not what new debt costs. **Alternative:** observed 3.3% → cost of capital 7.63%, value $50.99 (`alternatives/kd-observed-output.md`). **Confidence:** high.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  EBIT coverage 8.32x → AA, 4.99%; EBITDA coverage 8.96x → AAA, 4.84% (`model-output.md` section 2).

- **If the two differ, why?**
  Agencies rate on gross debt, include the $6.0B tax dispute and look at a less flattering year; the synthetic rating uses one year of coverage.

- **What is the market value of interest-bearing debt?**
  40,936 (`company.debt_market`): fair value of long-term debt 39,385 plus commercial paper 1,551, against a book value of 45,492 (`company.debt_book`). The gap is low-coupon euro notes issued before 2022.
  
  > ⚠️ **Discretionary Decision: debt at market value**
  > **Chose:** market value. **Why:** rates rose since much of the debt was issued. **Alternative:** book debt (48,000 incl. leases and guarantees) → cost of capital 7.77%, value $49.43 (`alternatives/debt-book-output.md`). **Confidence:** high.

- **What is the debt value of lease commitments, including leases signed but not yet started?**
  1,722 of operating lease liabilities (`company.lease_debt`). The 10-K discloses no material leases not yet commenced.

- **Off-balance-sheet guarantees or take-or-pay contracts?**
  Guarantees of third-party debt of 786 (`company.off_balance_sheet_debt`), included in debt. The Africa bottler's 1,435 of debt held for sale is excluded because it leaves with the sale (`company.debt_total` note).

- **How much interest was capitalized?**
  None disclosed (`company.interest_capitalized` not set); coverage is unchanged.

- **Did the company lengthen depreciation lives?**
  No change disclosed in the FY2025 10-K.

- **What marginal tax rate applies?**
  25% (`market.tax_rate_marginal`), federal 21% plus state. The effective rate was 17.88% (`market.tax_rate_effective`).
  
  > ⚠️ **Discretionary Decision: tax rate in the cash flows**
  > **Chose:** the 25% marginal rate (model convention). **Why:** course default for the tax benefit of debt. **Alternative:** effective 17.88% throughout → cost of capital 7.85%, value $54.45 (`alternatives/tax-effective-output.md`). **Confidence:** medium; Coca-Cola's foreign income has been taxed below 25% for decades, so the default understates cash flow.

## Notes

Debt 43,444 at market including leases and guarantees (`company.debt_total`); A1/A+ cost of debt 5.14%.
