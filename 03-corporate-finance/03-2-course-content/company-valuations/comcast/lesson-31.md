---
title: "Comcast Corporation (CMCSA) — Lesson 31: Estimating Growth in Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Comcast Corporation (CMCSA) — Lesson 31: Estimating Growth in Cash Flows

Quick mode, blind, as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

## Cumulative Project — Questions for This Lesson

- **What is the historical growth rate in your company's revenues? EBIT? Net income?**
  Revenue 0.62% a year 2022–2025 (fact `revenue-growth-2022-2025-annual`); EBIT before impairments −2.95% a year (fact `ebit-ex-impairment-growth-2022-2025-annual`); net income is distorted by the 2022 impairment, the 2024 tax benefit and the 2025 Hulu gain, and on the cleaned series in `company.history` went from $15,388M (2023) to $12,941M (2025).

- **What are analysts or managers projecting as an expected growth rate in the future?**
  Management gives no numeric guidance in the filings (meta.omitted); analyst consensus is not a permitted source. The ledger uses 1% revenue growth at the base-year 15.57% margin (`forecast.years`).

- **Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?**
  About 0.7% a year (fact `fundamental-growth-estimate`): an average reinvestment rate of 7.3% times an average ROIC of about 9.5%. On the base year alone, reinvestment is negative (−4.55% excluding acquisition amortization, section 8), which implies no growth at all.

## Notes

History, not guidance, drives the forecast.
