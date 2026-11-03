---
title: "Corteva (CTVA) — Lesson 04: Define and Measure Risk"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Corteva (CTVA) — Lesson 04: Define and Measure Risk

Quick mode, blind as of 2026-06-30: only the question-bank entries tagged with a signal are answered. Numbers come from `inputs.yaml` or `model-output.md`.

## Module 1 Step — Questions for This Lesson

- **How many classes of shares exist and what are the voting rights of each?**
  One class of common stock with one vote per share. The EIDP preferred stock ($4.50 and $3.50 series, $243M carried as noncontrolling interest) sits at the subsidiary and does not vote at Corteva (`governance.share_classes`, `company.minority_interests`).

- **Who are the largest shareholders?**
  Vanguard 12.0%, BlackRock 8.0%, State Street 5.3% (`governance.controlling_holders`, DEF 14A as of 2026-03-02). Three Schedule 13G filings in April–May 2026 are on the EDGAR index but were not fetched, so any new 5% holder is unknown (sources/README.md).

- **Is the marginal investor an individual or an institution?**
  An institution (`governance.marginal_investor`).

- **Is that marginal investor diversified?**
  Yes. The large holders are index and diversified managers, so only market risk should be priced, and the beta-based cost of equity applies (lesson 10).

## Notes

No controller. The shares used are 668.8M basic from the 10-Q cover (`company.shares_basic`).
