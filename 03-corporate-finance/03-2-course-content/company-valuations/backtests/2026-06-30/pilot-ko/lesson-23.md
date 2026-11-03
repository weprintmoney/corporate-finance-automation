---
title: "The Coca-Cola Company (KO) — Lesson 23: Designing the Right Type of Financing"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 23: Designing the Right Type of Financing

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 23 — Designing the Right Type of Financing

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Cumulative Project — Questions for This Lesson

- **Given its asset/project characteristics, what is the right type of debt for your firm?** (`l23-q1`, signal: debt-design)

The assets are brands and franchise contracts with very long lives, cash flows in dozens of currencies (60% of revenue outside the US, 10-K Note 3), and steady demand. The right debt is long-term, mostly fixed-rate, spread across the currencies the cash comes in, and straight (no conversion features needed for a company with stable cash flows).

- **What are the actual debt characteristics?** (`l23-q2`, signal: debt-design)

Long-term fixed-rate notes due 2027–2093, partly swapped, plus commercial paper (`debt.rate_type`: mixed). Currency: US dollars and euros, with euro notes $15,470M of $43,941M long-term debt (35%) and a small Swiss franc tranche (`debt.currency`). Weighted maturity about 11 years (estimate, range 9–14, `debt.maturity_years`). $4,817M matures in 2027 (`facts.long-term-debt-maturing-2027`). Unused backup lines $6,150M (`debt.revolver_undrawn`). No maintenance covenants (`debt.covenants`).

- **If there is a mismatch, what is the best way to fix it?** (`l23-q3`, signal: debt-design)

Little mismatch. The euro share roughly matches European earnings, and maturities match long-lived assets. The gap is Latin American, African and Asian cash flows with no debt in those currencies, which the company covers with derivatives (10-K Note 5) and by selling the bottlers that carry local-currency risk. No change needed; the debt was designed for the business, not for a deal.

## Notes

Quick mode answered only the signal questions (l23-q1, l23-q2, l23-q3). Not answered in quick mode: l23-p1, l23-p2.
