---
title: "Eaton Corporation plc (ETN) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Eaton Corporation plc (ETN) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

Quick mode: only the question-bank entries with a `signals` field are answered here. No transcript-layer entries carry a signal, so none are listed.

## Module 1 Step — Questions for This Lesson

- **What is the best measure of the company's country exposure (revenues, production, assets)?**
  Revenues by destination, the only full geographic split the 10-K gives for sales. Long-lived assets are also split, but are a narrower base.

- **What is the geographic breakdown of that measure?**
  2025 net sales (`country.exposures`): United States 62.4%, Europe 18.5%, Asia Pacific 9.9%, Latin America 5.3%, Canada 3.9%.

- **What is the weighted average ERP?**
  5.03% (`country.weighted_erp`; model-output.md section 1). Each region's premium is the 4.57% mature premium (`market.mature_erp`) plus that region's country risk premium (rule 15): 0 for the US and Canada, about 1.1% for Europe and Asia Pacific, 2.85% for Latin America.

- **Why might that ERP change?**
  Boyd Thermal (sales in North America, Asia and Europe) and the Mobility exit (Mobility has large Latin American and Asian operations) will change the mix; the net effect is small. A larger change would come from the mature premium itself.

## Notes

> ⚠️ **Discretionary Decision: regional country risk premiums**
> **Chose:** simple averages of each region's largest markets (Europe: Germany, UK, France, Italy, Spain; Asia Pacific: China, Japan, India, Australia, Korea; Latin America: Brazil, Mexico). **Why:** the 10-K gives regions, not countries, and Damodaran's file has no regional aggregates. **Alternative:** the mature premium alone → cost of capital 9.19% and value $175.84 a share (alternatives/erp-us-only-output.md), against 9.69% and $156.54. **Confidence:** medium; a country split of sales would raise it.
