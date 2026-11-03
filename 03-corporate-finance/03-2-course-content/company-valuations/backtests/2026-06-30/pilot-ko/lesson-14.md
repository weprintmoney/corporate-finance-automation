---
title: "The Coca-Cola Company (KO) — Lesson 14: From Hurdle Rates to Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# The Coca-Cola Company (KO) — Lesson 14: From Hurdle Rates to Cash Flows

Quick mode, blind, as of 2026-06-30. Numbers cite `inputs.yaml` fields or `model-output.md` sections.

### Lesson 14 — From Hurdle Rates to Cash Flows

No transcript-layer question in this lesson carries a signal, so quick mode answers none.

## Cumulative Project — Questions for This Lesson

- **What return on capital did your firm generate last year?** (`l14-q1`, signal: returns)

2025: 22.71% on reported operating income (after $1,261M of other operating charges), 24.45% with non-cash impairments added back (`model-output.md` section 8). Invested capital of $45,448M is measured on an operating basis: equity-method stakes are taken out because their income sits below operating income (`company.invested_capital`).

> ⚠️ **Discretionary Decision: invested capital excludes equity-method stakes**
> **Chose:** equity + debt + leases − cash − $20,235M of equity-method investments. **Why:** operating income excludes $2,031M of equity income, so the stakes must leave the denominator too; they are valued separately as cross-holdings.
> **Alternative:** leaving them in would put invested capital near $65,700M and ROIC near 16%, still twice the cost of capital (arithmetic on `company.invested_capital` + 20,235).
> **Confidence:** high.

- **If you have returns on capital over time for your firm, is there a trend in those returns?** (`l14-q2`, signal: returns)

2023 26.05%, 2024 26.60%, 2025 24.45% (operating income before impairments, `model-output.md` section 8 by year). Flat to slightly down: invested capital rose from $37,572M to $45,448M, mostly because equity grew with gains on stake sales and the fairlife payment went into the asset base, while operating income grew 6.5% a year.

- **How do the returns on capital (equity) compare to the costs of capital (equity)?** (`l14-q3`, signal: returns)

Return on capital 22.71% against a cost of capital of 7.67%: an excess return of 15.04% and economic value added of $6,833.8M (`model-output.md` section 8). Return on equity 40.74% against a cost of equity of 8.14% (section 8). The core concentrate business creates value by a wide margin every year (`exhibits/exhibit-returns.png`).

- **Are the projects in the future likely to look like the projects in the past? Why or why not?** (`l14-q5`, signal: returns)

No. The past returns come from a concentrate franchise built decades ago; the new money goes into bought brands. BodyArmor ($1,720M of impairments in two years, `facts.bodyarmor-impairments-2024-2025`) and fairlife (a $6,173M earn-out payment, `facts.fairlife-final-milestone`) are the recent projects, and goodwill is already 34.09% of invested capital (`model-output.md` section 8). Refranchising (India, Philippines, Nigeria, Africa to CCHBC) raises the measured return by shrinking capital, not by finding better projects. Expect new investments to earn well below 24%, likely closer to the 15% assumed for the stable period (`forecast.stable_roic`).

## Notes

Quick mode answered only the signal questions (l14-q1, l14-q2, l14-q3, l14-q5). Not answered in quick mode: l14-q4, l14-p1, l14-p2.
