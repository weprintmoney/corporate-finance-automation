---
title: "SolarWinds (SWI) — Lesson 24: Trends and Measures"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 24: Trends and Measures

### Lesson 24 — Trends and Measures

Lesson 24 has no lecture transcript in the repo (`lesson-index.yaml` lists none), so there are no transcript-layer entries. The two project questions are answered from the ledger and filings. The slides define the measures: payout ratio is dividends divided by net income (not computable when net income is negative); yield is dividends per share divided by the stock price.

## Cumulative Project — Questions for This Lesson

- **How much (if any) has your company paid out in dividends each year for the last 5 years?**
  Two payments in five years, both special, neither a regular dividend. Years are fiscal years ending 12-31; amounts in $ millions.

| Year | Cash dividend | Per share | Other cash returned | Source |
|---|---|---|---|---|
| 2020 | 0 | none | | FY2020 10-K: "never declared or paid any cash dividends" (facts.div-2020) |
| 2021 | 237.2 | $1.50, record 2021-08-09, paid 2021-08-24 | plus N-able shares (below) | FY2023 10-K (facts.special-dividend-2021) |
| 2022 | 0.0 | none | buybacks 11.1 | `company.history` |
| 2023 | 0.0 | none | buybacks 18.8 | `company.history` |
| 2024 | 168.2 | $1.00, record 2024-04-03, paid 2024-04-15 | buybacks 26.5 | `company.history`; FY2024 10-K (facts.special-dividend-2024-per-share) |

  The five-year cash dividend total is $237.2M + $168.2M = $405.4M. Two notes. First, the 2021 payment came with the spin-off of N-able on 2021-07-19, in which holders received one N-able share for every two SolarWinds shares held (before the 2:1 reverse split of 2021-07-30), valued at the $13.00 opening price of one N-able share (facts.corporate-actions-2021); SolarWinds also received a $238.2M one-time dividend from N-able at separation (facts.nable-dividend-to-swi). Second, the buybacks in the ledger are shares withheld to cover employees' taxes on vesting stock (`company.history` notes), not open-market repurchases.

- **What dividend yield and payout ratio does this translate into?**
  Payout ratio (dividends ÷ net income):
  - 2024: $168.2M ÷ $111.9M = 150.3%. Counting the $26.5M of share withholding, cash returned is $194.7M (model-output.md §5), 174.0% of net income.
  - 2023 and 2022: no dividend; net income was −$9.1M and −$929.4M, so a ratio is not defined.
  - 2021: net income was −$51.4M (facts.ni-2020-2021), so the $237.2M payout is not defined as a ratio. 2020: $0 on net income of $132.7M (facts.ni-2020-2021) is 0%. Years before 2022 include N-able and are not comparable (`company.history` note).
  - Five-year total: net income summed over 2020–2024 is negative (132.7 − 51.4 − 929.4 − 9.1 + 111.9 = −745.3), so a cumulative ratio is not defined either.
  - Against free cash flow to equity, the measure that matters when earnings are distorted by the 2022 goodwill write-off: 2024 FCFE was $127.0M and cash returned was $194.7M, $67.7M more (model-output.md §5). Lesson 26 takes this up.

  Dividend yield (dividend per share ÷ price): 2024 only. No price series exists for the record date (the ticker is delisted, `meta.omitted`). Two anchors in the filings: the 2024-02-14 close of $12.89, six weeks before the dividend was declared, gives $1.00 ÷ $12.89 = 7.76% (facts.price-2024-02-14); the 2025-02-05 unaffected price of $15.18 gives 6.59%. The record-date yield lies near that range; the true figure is not recoverable from the files. 2021: not computed. The spin-off, the reverse split and the in-kind N-able shares make a single price for the date misleading, and the 10-K gives only the pre-split $15.72 close on 2021-02-24 (facts.price-2021-02-24).

  Against the market patterns the slides describe (dividends are sticky, track earnings, buybacks are replacing dividends): SolarWinds fits none. Its payments are irregular, followed no earnings, and were tied to a spin-off and a cash build.

## Notes

SolarWinds paid two special dividends in the five years (2021 and 2024); the filings show no regular dividend. The key facts for later lessons: $405.4M of cash dividends in five years, a 150.3% payout in 2024, and no regular policy. Lesson 25 asks why; lesson 26 tests whether FCFE supported them.
