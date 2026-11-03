---
title: "Eaton Corporation plc (ETN) — Lesson 10: Bottom-Up Betas"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Eaton Corporation plc (ETN) — Lesson 10: Bottom-Up Betas

### Lesson 10 — Bottom-Up Betas

Quick mode: only the question-bank entries with a `signals` field are answered here. No transcript-layer entries carry a signal, so none are listed.

## Module 1 Step — Questions for This Lesson

- **What is the bottom-up unlevered beta from comparable firms, cash-corrected?**
  1.1332 (`beta.unlevered_bottom_up`), from Damodaran's January 2026 US industry betas, cash-corrected (sources/market-data/industry-betas-2026-01-05.json).

- **If the company has several businesses, what is each segment's beta and the weighted average?**
  Weighted by 2025 segment sales (`beta.segments`): Electrical 73.2% at 1.1898 (Electrical Equipment), Aerospace 15.5% at 0.8694 (Aerospace/Defense), Mobility 11.3% at 1.1283 (Auto Parts). Weighted: 1.1332. Relevered at today's debt-to-equity of 0.1325, the levered beta is 1.2458 (model-output.md section 1).

## Notes

> ⚠️ **Discretionary Decision: beta**
> **Chose:** bottom-up, segment-weighted by 2025 sales, Mobility kept in. **Why:** Mobility is still consolidated on the analysis date, and sales are the only consistent weight across segments. **Alternative:** Electrical Equipment alone (1.1898), which is roughly the post-separation company → cost of capital 9.97%, value $152.27 (alternatives/beta-electrical-equipment-only-output.md). **Confidence:** medium. Value weights would lean further toward Electrical.
