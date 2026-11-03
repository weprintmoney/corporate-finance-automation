---
title: "The Coca-Cola Company (KO) — Lesson 26: Assessing Dividend Policy and Free Cash Flow to Equity"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 26: Assessing Dividend Policy and Free Cash Flow to Equity

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 26 — Assessing Dividend Policy and Free Cash Flow to Equity

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Cumulative Project — Questions for This Lesson

- **How much has your company returned to its stockholders, in the form of dividends and stock buybacks in the last five years?** (`l26-q1`, signal: payout)

2023–2025 (three years; earlier balance sheets were not in the fetched filings, `meta.omitted`): dividends $7,952M, $8,359M, $8,779M and buybacks $2,289M, $1,795M, $746M, a total of $29,920M (`model-output.md` section 5).

- **How much cash could your company have returned in the last five years? (Estimate FCFE)** (`l26-q2`, signal: payout)

FCFE: $11,542M in 2023, $6,954M in 2024, $4,848M in 2025, total $23,344M (section 5). 2024 carries the $6.0 billion IRS deposit (`facts.irs-tax-litigation-deposit`) and 2025 the $6.1 billion fairlife payment (moved to capex in the ledger, `company.history` note). Without those two one-off payments FCFE would be about $35.4 billion (arithmetic: 23,344 + 6,000 + 6,100).

> ⚠️ **Discretionary Decision: FCFE built from cash from operations**
> **Chose:** change in working capital defined so that net income + impairments + D&A − change_wc equals cash from operations; the fairlife payment moved from operating cash flow to capex. **Why:** net income includes $1,952M of non-cash gain on the Coke Consolidated sale and equity income above dividends received; starting from cash from operations keeps those out.
> **Alternative:** the reported working-capital change alone would add about $1.7 billion a year of non-cash income to FCFE and halve the gap in section 5.
> **Confidence:** medium.

- **If there is a difference, where is it showing up (cash balances, debt ratios)?** (`l26-q3`, signal: payout)

Returned exceeded FCFE by $6,576M over three years (section 5). It did not show up as more debt (net new debt was $13M in 2025) or less cash (cash rose $2,143M). It was paid for by selling assets: $7,482M of divestiture proceeds 2023–2025 (`facts.divestiture-proceeds-2023-2025`) plus $1,338M from selling a minority stake in a subsidiary (`facts.noncontrolling-interest-sale-proceeds`). See `exhibits/exhibit-payout.png`.

## Notes

Quick mode answered only the signal questions (l26-q1, l26-q2, l26-q3). Not answered in quick mode: l26-p1, l26-p2.
