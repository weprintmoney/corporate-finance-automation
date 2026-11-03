---
title: "The Coca-Cola Company (KO) — Lesson 31: Estimating Growth in Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 31: Estimating Growth in Cash Flows

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 31 — Estimating Growth in Cash Flows

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Cumulative Project — Questions for This Lesson

- **What is the historical growth rate in your company's revenues? EBIT? Net income?** (`l31-q1`, signal: lifecycle)

Revenue 2.36% a year 2023–2025 as reported (`forecast.stress_cases[0]`); the proxy gives 5% organic growth for 2025 (`sources/statements/ko-stated-positions.md`), the difference being currency and refranchising. Operating income before impairments grew from $13,052M to $14,814M, 6.5% a year (section 8). Net income rose from $10,714M to $13,107M, but 2025 includes the $1,952M Coke Consolidated gain (`facts.coke-consolidated-stake-sale`).

- **What are analysts or managers projecting as an expected growth rate in the future?** (`l31-q2`, signal: value-vs-price)

Management's long-term plan: 4%–6% organic revenue and 6%–8% operating income growth (`forecast.management_growth` 5%, proxy line 2195). Q1 2026 ran well ahead: revenue +12.07% and operating income +19.13% (`facts.q1-2026-revenue-growth`, `facts.q1-2026-operating-income-growth`), helped by six extra days and favourable currency the 10-Q expects to persist. No analyst consensus was permitted in the blind run (`meta.omitted`).

> ⚠️ **Discretionary Decision: forecast source**
> **Chose:** management's plan midpoints, 5% revenue and margin rising so operating income grows 7% (`forecast.years`). **Why:** pay is set at these midpoints, so management has to deliver them; 2025 organic growth was 5%.
> **Alternative:** history (2.36% revenue, margin held) → $47.56 a share; plan revenue with margin held → $52.21 (`model-output.md` section 6 stress cases).
> **Confidence:** medium.

- **Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?** (`l31-q3`, signal: value-vs-price)

Fundamental growth = reinvestment rate × return on capital. In 2023, the last year without one-off payments, 28.30% × 26.05% = 7.4% (section 8 by year). The 2024 and 2025 reinvestment rates (97.25% and 83.92%) are inflated by the IRS deposit and the fairlife payment and should not be projected. 7.4% is consistent with management's 6%–8% operating income plan.

## Notes

Quick mode answered only the signal questions (l31-q1, l31-q2, l31-q3). Not answered in quick mode: l31-q4, l31-p1, l31-p2.
