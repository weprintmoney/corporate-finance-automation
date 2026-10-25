---
title: "SolarWinds (SWI) — Lesson 28: Me-Too Dividend Policy and Peer Group Assessment"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 28: Me-Too Dividend Policy and Peer Group Assessment

### Lesson 28 — Me-Too Dividend Policy and Peer Group Assessment

- **Lesson 28, Session 28 · Part 1 — "Me-Too Corporate Finance: Benchmarking Dividend Policy Against the Peer Group"** ([transcript](../../04-dividends-and-valuation/lesson-28/session-28-part-1.md))
    - Quote: "Much of corporate finance is what I call 'me-too corporate finance.'"
    - Question for SolarWinds: How does SolarWinds' payout compare with its peers, and what would a regression of payout on growth, beta and leverage predict for a company with its characteristics? Is the company copying its sector, or diverging for a reason?
    - Sources needed: Peer payout ratios; sector averages; the lesson's regression; SolarWinds' growth, beta and debt ratio.
    - Where to find: `peers` (`payout`, `growth`, `debt_ratio`) and `company.history` in `inputs.yaml`; model-output.md §1 and §5; `04-dividends-and-valuation/lesson-28/spreadsheet-divfcfe24.md` (Damodaran sector table, January 2025); `lesson-28/slides.md` (regression).
    - Answer: SolarWinds diverged in 2024, and not for a reason the peers share.
        - Peers (`peers`): five of the eight pay no dividend (payout 0.0 for Akamai, NetScout, OneSpan, Qualys, Teradata); Progress pays 46.05%; NetApp and Open Text pay dividends that the SEC data did not tag, so the ledger leaves them null. The sector norm is no dividend, with some buybacks.
        - Sector table: Damodaran's Software (System & Application) group of 351 firms paid out 27.22% of net income as dividends and returned 80.36% counting buybacks, and returned 86.53% of FCFE before debt flows (facts.sector-software-payout).
        - SolarWinds 2024: dividends of $168.2M on net income of $111.9M is a 150% payout; with the $26.5M of buybacks, 174%; cash returned over FCFE is 153% ($194.7M ÷ $127.0M, §5). In 2022 and 2023 it paid no dividend.
        - Regression: the lesson's market regression (January 2014 US companies) is payout = 0.649 − 0.296 × beta − 0.800 × expected growth + 0.300 × debt-to-capital (facts.payout-regression-2014; signs checked by reproducing the slide's Disney figure of 26.95%). With SolarWinds' levered beta of 1.6714 and debt-to-capital of 33.03% (§1) and management's growth of 8.12% (`forecast.management_growth`, since analyst growth is omitted), predicted payout is 18.8% (facts.predicted-payout-swi). Caveats: the coefficients are ten years old and the lesson reports an R-squared of only 19.6%, so treat the prediction as a rough marker.
        - Copying or diverging: not copying. The actual 2024 payout was eight times the predicted one. It is a special dividend by two controlling holders, not a payout policy. In the two years without one, SolarWinds looked like its peers.

## Cumulative Project — Questions for This Lesson

- **How does your company dividend and cash return policy measure up against other companies in the sector?**
  Against the eight peers (`peers`) it is an outlier in 2024: a 150% dividend payout against a peer median of 0.0 among those with a recorded payout, and 27.22% for the wider software group (facts.sector-software-payout). Counting buybacks, 174% of net income against the group's 80.36%. Over the three years it looks closer: $224.6M returned in all (§5), mostly in one year.

- **Given how much other companies in the sector are returning to stockholders, is your company returning too much or too little?**
  In 2024, too much against the sector and against the regression's 18.8%; it also exceeded its own FCFE by 53%. Over 2023–2024 together it returned 115% of FCFE ($213.5M against $186.4M, §5), which is not far above capacity. Given returns on capital below the cost of capital (§8: 6.66% against 10.23%), returning cash is the right direction; the issue is that it was lumpy and paid to a holder base where two sponsors held 66.35% (`governance.controlling_holders`).

## Notes

Payout was not modeled in the course DCF (lesson 34 values cash flow to the firm). The peer payout field is thin, which limits the benchmark: two of eight are null and five are zero. The peer set is the eight fairness-opinion companies, not Datadog, Dynatrace and PagerDuty. A true re-run of the regression would need the January 2025 coefficients, which are not in the lesson folder.
