---
title: "The Coca-Cola Company (KO) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 07: Country Risk Premiums

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 07 — Country Risk Premiums

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Module 1 Step — Questions for This Lesson

- **Country risk and weighted ERP: What is the best measure of the company's country exposure (revenues, production, assets)? What is the geographic breakdown of that measure? What is the weighted average ERP? Why might that ERP change?** (`m1-step-07`, signal: hurdle)

Measure: revenue by operating segment, because the 10-K reports no revenue by country and unit case volume (16% in the US, `facts.us-share-of-unit-case-volume`) overstates emerging markets where Coca-Cola sells low-priced concentrate. Breakdown (`country.exposures`): North America 40.1%, EMEA 23.6%, Latin America 13.0%, Asia Pacific 11.6%, Bottling Investments 11.8%. Each region's premium is the June 2026 implied premium 4.57% plus a country premium averaged over its main markets (weights in the ledger notes).
Weighted ERP: 6.30% (`country.weighted_erp`, `model-output.md` section 1).
Why it might change: the implied premium moves monthly; Argentina, Nigeria, Egypt and Turkey carry premiums of 4.7%–9.7% and move with each sovereign rating action; and the sale of the African bottlers to CCHBC (expected by end-2026, `facts.africa-bottling-held-for-sale-assets`) will shrink the Bottling Investments weight.

> ⚠️ **Discretionary Decision: country risk in the equity risk premium**
> **Chose:** revenue-weighted premiums with country premiums for EMEA, Latin America, Asia Pacific and the bottlers (6.30%). **Why:** the course weights the premium by where the company earns, and 60% of revenue is outside the US.
> **Alternative:** the mature-market premium alone (4.57%) → cost of capital 6.70% and value $73.09 a share instead of 7.67% and $56.79 (`alternatives/alt-erp-mature-only-output.md`).
> **Confidence:** medium; this is the single largest driver of value against price, and segment revenue is a rough proxy for country exposure.

## Notes

Quick mode answered only the signal questions (m1-step-07). Not answered in quick mode: l07-p1, l07-p2.
