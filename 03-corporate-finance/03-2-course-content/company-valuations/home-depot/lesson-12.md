---
title: "The Home Depot (HD) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Home Depot (HD) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

Quick mode, blind as of 2026-06-30: only the question-bank entries with a `signals` field are answered. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

## Module 1 Step — Questions for This Lesson

- **Agency rating, synthetic rating, market value of debt, leases, guarantees**

  No agency rating is disclosed in the fetched filings (`debt.rating_actual` null). Synthetic: EBIT 20,890 ÷ interest 2,412 = 8.66x → AAA on the large-firm table, spread 0.40%, pre-tax cost 4.84% (model-output.md section 2); AAA on all three numerators. From memory (outside knowledge) the agency ratings are A/A2; at the A spread the cost of debt is 5.22% and the cost of capital 9.87% (alternatives/kd-agency-rating-a-output.md). The two differ because coverage ignores operating-lease interest and because agencies weight leverage after two debt-funded deals.

  Market value: senior notes fair value $42,510M against carrying $46,443M (10-Q fair-value note), so debt at market is $49,576M including commercial paper $3,503M, finance leases $2,932M, other $631M (`company.debt_market`). Operating leases $9,648M (`company.lease_debt`). Leases signed not yet started ~$675M undiscounted and no JV guarantees: left out, under 1% of debt (`company.off_balance_sheet_debt`). Total debt $59,224M (`company.debt_total`).

  > ⚠️ **Discretionary Decision: cost of debt**
  > **Chose:** synthetic AAA, 4.84%. **Why:** the filings disclose no rating and the checklist bars an undisclosed one. **Alternative:** remembered A rating, 5.22% → cost of capital 9.87%, value $213.50 (alternatives/kd-agency-rating-a-output.md). **Confidence:** medium; immaterial to value.

  > ⚠️ **Discretionary Decision: debt at market, leases in**
  > **Chose:** market value of notes plus operating leases. **Why:** lesson 12; fair value is disclosed. **Alternative:** book debt → D/V 15.23%, value $210.20 (alternatives/debt-at-book-output.md); leases excluded → D/V 12.36%, value $223.16 (alternatives/leases-excluded-output.md). **Confidence:** high on direction.

## Notes

Checked for inflated coverage (review item 14d): the 10-K reports interest only net of an undisclosed, immaterial capitalized amount and no change in depreciation lives in fiscal 2023–2025, so no adjustment. Other entries for this lesson are outside quick mode and were not answered. Transcript-layer entries were not needed.
