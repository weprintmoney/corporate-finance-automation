---
title: "Corteva (CTVA) — Lesson 10: Bottom-Up Betas"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Corteva (CTVA) — Lesson 10: Bottom-Up Betas

Quick mode, blind as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers come from `inputs.yaml` or `model-output.md`.

## Module 1 Step — Questions for This Lesson

- **What is the bottom-up unlevered beta from comparable firms, cash-corrected?**
  0.8366 (`beta.unlevered_bottom_up`), from Damodaran's January 2026 industry betas (cash-corrected).

- **If the company has several businesses, what is each segment's beta and the weighted average?**
  Seed: Farming/Agriculture 0.8458, weight 56.9%. Crop Protection: Chemical (Specialty) 0.8245, weight 43.1%. Weights are 2025 segment sales (`beta.segments`). Relevered at 6.24% debt, the beta is 0.8784 (model-output.md section 1).

## Notes

⚠️ Discretionary Decision: Chemical (Specialty) for crop protection. **Alternative:** Chemical (Basic), 0.6368, gives a blended 0.7557, cost of capital 8.43% and value $48.05 (alternatives/beta-basic-chemicals-output.md). Specialty fits a business that sells patented active ingredients and biologicals. Confidence medium. No regression beta (`meta.omitted`).
