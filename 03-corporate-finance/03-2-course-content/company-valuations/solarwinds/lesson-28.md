---
title: "SolarWinds (SWI) — Lesson 28: Peer Group Benchmarking (Dividend Policy)"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Lesson 28: Peer Group Benchmarking (Dividend Policy)

### Lesson 28 — Peer Group Benchmarking (Dividend Policy)

- **Lesson 28, Session 28 · Part 1 — "Me-Too Corporate Finance: Benchmarking Dividend Policy Against the Peer Group"** ([transcript](../../04-dividends-and-valuation/lesson-28/session-28-part-1.md))
    - Quote: "Much of corporate finance is what I call 'me-too corporate finance.'"
    - Question for SWI: SWI competes in the observability/IT-ops SaaS sector alongside Datadog, Dynatrace, and PagerDuty — none of which pay dividends. Does SWI's own dividend/buyback policy match that "me-too" zero-payout sector norm, or did SWI diverge because its PE-controlled, EBITDA-margin-focused profile behaves more like a mature company than a growth SaaS peer — and what would a payout regression against peer growth, beta, and leverage predict for SWI specifically?
    - Sources needed: dividend yield / payout ratio (or documented absence) for DDOG, DT, and PD, plus regression inputs (beta, growth, debt ratio) for that peer set and for SWI.
    - Where to find: PEER-FILINGS — DDOG/DT/PD 10-Ks (capital-return footnotes); SEC-EDGAR — SWI 10-K FY2024 (capital-return disclosures); REPO-SWI-VAL (beta already computed at Steps 8–11, reusable as a regression input; no payout-ratio work exists there yet).
    - Answer: SWI diverged from the sector norm, and it was right to. All three peers have zero dividend payout — Datadog "never declared or paid any cash dividends" (`ddog-datadog-10k.md`), Dynatrace "never declared or paid any dividends" (`dt-dynatrace-10k.md`), PagerDuty "never declared or paid any cash dividends" (`pd-pagerduty-10k.md`) — but two of them do buy back stock: DT completed a $500M program in February 2026 and authorized a fresh $1B, and PD ran $100M (2024) plus $200M (2025) programs. SWI is the mirror image: $405.4M of special dividends ($237.2M in 2021, $168.2M in 2024) and essentially no discretionary buybacks. A payout regression on the standard drivers predicts exactly that divergence: SWI grew 5.0% versus DDOG's 27.7% ($3,427.2M revenue) and DT's 18.8% ($2,018.4M), its 48.3% adjusted EBITDA margin dwarfs DT's 12.2% GAAP operating margin and DDOG's −1.3%, its levered beta is 1.55 versus Damodaran's 1.2766 sector average (`damodaran-industry-betas-software.md`), and it carries $1.21B of term debt against peers' $0–$1.0B of converts. Low growth, high margin, high leverage and sub-hurdle returns all load the predicted payout upward — copying the peers' zero-dividend template would have been textbook me-too corporate finance.

## Notes

Lesson 28's "me-too corporate finance" idea — that firms often copy peer policy rather than deriving it from their own drivers — gets a clean test here, and SWI passes it by *not* being a me-too follower. Every payout-relevant driver (growth, margin, leverage, ROIC) points the opposite direction from its zero-dividend observability peers, so SWI's divergence into special dividends was the analytically correct call, not an anomaly to explain away. This closes the loop opened in Lessons 25–27: the dividend-policy assessment across this project consistently finds SWI's actual behavior — return cash, don't chase peer-template growth investing — matches what the fundamentals prescribe. It connects to Lesson 35's multiples work, which runs a similar peer-regression exercise (there for pricing multiples rather than payout) and reaches the same "the discount/premium is deserved by the fundamentals" conclusion.
