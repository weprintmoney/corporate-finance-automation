---
title: "The Coca-Cola Company (KO) — Lesson 12: Debt: Measure and Cost"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 12: Debt: Measure and Cost

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 12 — Debt: Measure and Cost

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Module 1 Step — Questions for This Lesson

- **Cost of debt: Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply? What synthetic rating does interest coverage imply, and what cost of debt? If the two differ, why? What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book? What is the debt value of lease commitments, including leases signed but not yet started? Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet? How much interest was capitalized into construction, and what does coverage look like once it is added back? Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income? What marginal tax rate applies to the after-tax cost of debt?** (`m1-step-12`, signal: hurdle)

Agency rating: A+ (S&P) and A1 (Moody's) (`debt.rating_actual`). Spread 0.70% over the 4.44% Treasury gives a pre-tax cost of debt of 5.14% (`model-output.md` section 1).
Synthetic rating: EBIT coverage 8.32x gives AA, spread 0.55%, cost of debt 4.99%; EBITDA coverage 8.96x gives AAA (section 2).
Why they differ: the agencies look through to the bottlers' debt (CCEP, Coke Consolidated, Coca-Cola FEMSA, CCHBC) because Coca-Cola has an incentive to keep them viable (10-K line 1391), and they see the $14 billion tax contingency (`facts.irs-potential-liability-2010-2025`). Coverage on Coca-Cola's own operating income alone misses both.
Market value of debt: $40,936M (fair value of long-term debt plus commercial paper) against book $45,492M (`company.debt_market`, `company.debt_book`): the notes carry a 3.3% average rate (`debt.kd_pretax_observed`) against 5.14% today, so they trade about 10% below book.
Leases: $1,722M (`company.lease_debt`); none signed but not started. Guarantees of third-party debt: $786M, contingent, excluded (`facts.guarantees-of-third-party-debt`). Capitalized interest: none disclosed. Depreciation lives: no change disclosed (10-K Note 1 line 1919). Marginal tax rate: 25% (`market.tax_rate_marginal`). Total debt used: $42,658M (`company.debt_total`).

> ⚠️ **Discretionary Decision: cost of debt**
> **Chose:** the agency rating's spread (5.14%). **Why:** meetup guidance says build it from today's rate plus a spread, not the 3.3% book rate; the agency rating captures the bottler look-through and the tax case that coverage misses.
> **Alternative:** the synthetic AA rate (4.99%) → cost of capital 7.66% and value $56.82 (`alternatives/alt-kd-synthetic-output.md`).
> **Confidence:** high; the choice barely moves value.

> ⚠️ **Discretionary Decision: debt at market value; held-for-sale debt and guarantees excluded**
> **Chose:** market value $40,936M plus leases; the $1,248M of African bottler debt in liabilities held for sale and the $786M of contingent guarantees are left out. **Why:** the course weights by market value; the African debt leaves with the bottler.
> **Alternative:** book debt $47,214M with leases → cost of capital 7.66%, value $55.76 (`alternatives/alt-book-debt-output.md`).
> **Confidence:** high.

## Notes

Quick mode answered only the signal questions (m1-step-12). Not answered in quick mode: l12-p1, l12-p2.
