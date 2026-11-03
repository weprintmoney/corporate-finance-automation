---
title: "JPMorgan Chase & Co. (JPM) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# JPMorgan Chase & Co. (JPM) — Lesson 12: Debt: Measure and Cost

### Lesson 12 — Debt: Measure and Cost

Quick mode: only the question-bank entries tagged with a signal. Source lesson: [../../01-foundations-and-discount-rates/lesson-12/lesson-overview.md](../../01-foundations-and-discount-rates/lesson-12/lesson-overview.md).

## Module 1 Step — Questions for This Lesson

- **Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?**
  Parent senior long-term A1 (Moody's), A (S&P), AA- (Fitch), all stable; Moody's moved the outlook to stable from positive on 2025-11-03 (`debt.rating_actual`). An A rating implies 5.22% pre-tax on the January 2026 large-firm table (model-output.md section 1). It is not used: debt is 0 in the cost of capital.

- **What synthetic rating does interest coverage imply, and what cost of debt?**
  Not applicable. model.py prints CC (0.74x coverage, model-output.md section 2) because a bank's interest expense ($97,898M in 2025) is mostly interest on deposits ($45,112M) and repo, the cost of its raw material. The course says the same of Deutsche Bank: 'We will not try to estimate a synthetic rating for the bank. Defining interest expenses on debt for a bank is difficult' (lesson 12 slides).

- **If the two differ, why?**
  Because the synthetic rating measures the wrong thing for a bank; the agency rating rests on capital and liquidity, which are in bank-equity-output.md section A.

- **What is the market value of interest-bearing debt?**
  Not estimated. Long-term debt was $448,764M at 2026-03-31, $134,559M of it already at fair value at 2025-12-31 (facts `long-term-debt-2026q1`; `debt.rate_type`). It is recorded only for the debt-design signal.

## Notes

The cost of debt and synthetic rating do not apply to a bank. Everything downstream that needs them (sections 2–4 of model-output.md) is marked not applicable.
