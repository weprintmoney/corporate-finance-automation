---
title: "JPMorgan Chase & Co. (JPM) — Lesson 10: Bottom-up Betas"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# JPMorgan Chase & Co. (JPM) — Lesson 10: Bottom-up Betas

### Lesson 10 — Bottom-up Betas

Quick mode: only the question-bank entries tagged with a signal. Source lesson: [../../01-foundations-and-discount-rates/lesson-10/lesson-overview.md](../../01-foundations-and-discount-rates/lesson-10/lesson-overview.md).

## Module 1 Step — Questions for This Lesson

- **What is the bottom-up unlevered beta from comparable firms, cash-corrected?**
  For a bank the course does not unlever (lesson 11 slides, Deutsche Bank: 'We do not unlever or relever betas, because estimating debt and equity for banks is an exercise in futility'). The beta used is the revenue-weighted levered industry beta, 0.8486 (`beta.unlevered_bottom_up`, mislabeled by the schema), and the model's levered beta equals it because `company.debt_total` is 0 (model-output.md section 1).

- **If the company has several businesses, what is each segment's beta and the weighted average?**
  Markets plus CIB investment banking fees, $45,517M of $185,581M managed revenue (24.5%): Brokerage & Investment Banking 1.1715. Asset & Wealth Management, 13.0%: Investments & Asset Management 0.6600. Everything else (consumer banking, payments, lending, securities services, Corporate), 62.5%: Bank (Money Center) 0.7610. Weighted: 0.8486 (`beta.segments`; industry-betas-2026-01-05.json).

## Notes

> ⚠️ **Discretionary Decision: beta**
> **Chose:** revenue-weighted levered industry betas, 0.849, no relevering. **Why:** the course's bank method (lesson 11) and JPMorgan's mix of trading, banking and asset management. **Alternative:** money-center beta alone 0.761 → cost of equity 7.85% (alternatives/beta-money-center-output.md); market beta 1.0 → 9.00% (alternatives/beta-market-output.md); all brokerage 1.17 → 9.83% (alternatives/beta-brokerage-output.md). **Confidence:** medium. No regression beta was available from the allowed sources; a regression beta for JPM would settle it.
