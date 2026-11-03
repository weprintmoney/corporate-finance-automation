---
title: "Corteva (CTVA) — Lesson 31: Estimating Growth in Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Corteva (CTVA) — Lesson 31: Estimating Growth in Cash Flows

Quick mode, blind as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers come from `inputs.yaml` or `model-output.md`.

## Cumulative Project — Questions for This Lesson

- **What is the historical growth rate in your company's revenues? EBIT? Net income?**
  Revenue 2022→2025: $17,455M → $17,401M, flat. EBIT: $1,565M → $2,438M, about 16% a year. Net income: $1,147M → $1,094M, with the Bayer settlement and discontinued operations in between (`company.history`).

- **What are analysts or managers projecting as an expected growth rate in the future?**
  Management: 7% growth in Operating EBITDA and Operating EPS in 2026 at the guidance midpoint (`forecast.management_growth`). No analyst consensus is available under the blind rules.

- **Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?**
  About zero or negative. Base-year reinvestment was negative (−63.06% of after-tax operating income, or −27.84% excluding acquired amortization; section 8), so ROIC × reinvestment rate gives no growth. The 2023–2025 earnings growth came from margins (price/mix, cost programs, fewer royalty payments), which cannot compound indefinitely.

## Notes

> ⚠️ **Discretionary Decision: Forecast source and margin basis**
> **Chose:** the 2026 guidance for year one, then 3% revenue growth with margins rising from 18.4% to 19.9% on operating income before acquired-intangible amortization (`forecast.years`), with reinvestment at a sales-to-capital ratio of 1.5. **Why:** the $644M of amortization of 2017 merger intangibles needs no replacement spending, and 2025 FCFF was $2,981.5M (section 8), which a GAAP-margin forecast would not reproduce. **Alternative:** GAAP EBIT margins (14.5%–16.0%) → value $36.63 (alternatives/forecast-gaap-ebit-output.md). Stress cases: flat revenue at a 17.7% margin → $38.20; a crop-protection price war → $32.81 (section 6). **Confidence:** medium.
