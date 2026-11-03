---
title: "Corteva (CTVA) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Corteva (CTVA) — Lesson 07: Country Risk Premiums

Quick mode, blind as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers come from `inputs.yaml` or `model-output.md`.

## Module 1 Step — Questions for This Lesson

- **What is the best measure of the company's country exposure (revenues, production, assets)?**
  Revenues. Corteva sells seed and chemicals to farmers whose incomes depend on local currencies and policy. Brazil and Argentina show up directly in the 10-K as price and currency losses (2025 exchange loss $181M, of which Argentina $34M; 10-K Note 6). Production is more US-weighted: 68% of net property is in the US (10-K Note 21).

- **What is the geographic breakdown of that measure?**
  2025 net sales (`country.exposures`): United States 47.5%, Canada 4.3%, EMEA 17.9%, Brazil 16.7%, other Latin America 5.9%, Asia Pacific 7.7%.

- **What is the weighted average ERP?**
  5.75% (`country.weighted_erp`, model-output.md section 1). Each region is the mature premium 4.57% (`market.mature_erp`) plus its country risk premium (rule 15; the US adds zero). EMEA, other Latin America and Asia Pacific use proxies flagged as estimates with ranges.

- **Why might that ERP change?**
  Brazil and Argentina carry most of the extra premium. A Brazilian downgrade or an Argentine recovery moves it. So does the spin: Seed is more North American (seed North America sales $1,770M of $3,023M in Q1 2026) than Crop Protection, which sells more in EMEA and Latin America. New Corteva's ERP will be higher than the combined company's.

## Notes

⚠️ Discretionary Decision: revenue-weighted ERP with regional proxies. **Alternative:** US-only premium 4.57%. That lowers the cost of capital to 7.91% and raises value to $56.77 (alternatives/us-only-erp-output.md). Confidence medium.
