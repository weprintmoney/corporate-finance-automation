---
title: "JPMorgan Chase & Co. (JPM) — Lesson 13: Financing Weights"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# JPMorgan Chase & Co. (JPM) — Lesson 13: Financing Weights

### Lesson 13 — Financing Weights

Quick mode: only the question-bank entries tagged with a signal. Source lesson: [../../02-investment-returns-and-financing/lesson-13/lesson-overview.md](../../02-investment-returns-and-financing/lesson-13/lesson-overview.md).

## Cumulative Project — Questions for This Lesson

- **Counting both interest bearing debt and lease commitments, what is the market debt ratio for the firm?**
  Not applicable as built. Set to 0% by choice (`company.debt_total` 0; model-output.md section 1), following lesson 11: for a bank, debt is raw material and the firm is valued as its equity. The leverage that matters is regulatory: CET1 14.1% (Advanced, binding) against an 11.5% requirement; Tier 1 leverage 6.6% against 4.0%; SLR 5.6% against 4.3% (bank-equity-output.md section A).

- **What is the cost of capital of the firm, using market values for weights? How different would it have been, if you had used book values?**
  The cost of capital equals the cost of equity, 8.27% (model-output.md section 1: 4.18% risk-free + 0.8486 × 4.82%). Book weights do not apply, for the same reason.

## Notes

> ⚠️ **Discretionary Decision: debt set to zero**
> **Chose:** `company.debt_total` = 0, so the hurdle rate is the cost of equity. **Why:** lessons 11 and 26 treat a bank's debt as raw material; the task brief says the same. **Alternative:** counting long-term debt ($448,764M) as financing would give a 34% debt ratio and a meaningless WACC; not run, because the method itself says not to. **Confidence:** high.
