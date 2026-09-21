---
title: "SolarWinds (SWI) — Multi-Year Financial Summary (XBRL-derived)"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-09-07
---

# SolarWinds (SWI) — Multi-Year Financial Summary

Derived from SEC EDGAR's XBRL "company facts" API (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001739942.json`), fetched 2026-09-07. This is a distillation, not a replacement for the full 10-Ks in this folder — cross-check any figure used in analysis against the underlying filing.

## Revenue, EBIT, Net Income, R&D, Capex ($ thousands)

| Fiscal Year | Total Revenue (ASC 606) | Operating Income (EBIT) | Net Income | R&D Expense | Capex |
|---|---|---|---|---|---|
| FY2017 | 728,017 | 69,654 | -39,761 | 86,618 | 7,594 |
| FY2018 | 833,089 | 115,185 | -14,743 | 96,272 | 15,945 |
| FY2019 | 669,103 | 79,862 | 13,223 | 75,882 | 11,397 |
| FY2020 | 716,770 | 52,253 | 132,713 | 85,754 | 16,882 |
| FY2021 | 718,632 | -32,871 | -51,408 | 101,813 | 9,252 |
| FY2022 | 719,367 | **-819,579** | **-929,413** | 92,330 | 7,463 |
| FY2023 | 758,740 | 150,373 | -9,109 | 100,173 | 4,353 |
| FY2024 | 796,895 | 208,419 | 111,903 | 108,599 | 5,611 |

**Note on FY2017–2018:** these two years used a different XBRL tag (`Revenues`) than FY2019 onward (`RevenueFromContractWithCustomerExcludingAssessedTax`, the post-ASC-606 tag) and are not perfectly comparable to later years on a like-for-like recognition basis — treat the FY2019–2024 series as the clean, comparable run.

**Note on FY2022:** the -$819.6M operating loss and -$929.4M net loss are real, not a data error — SolarWinds recorded a large goodwill/intangible impairment charge in FY2022 (consistent with the broad 2022 software-sector multiple compression). Cross-check the impairment footnote in `swi-10k-fy2023.md` (which reports FY2022 as a comparative year) or `swi-10k-fy2022` if a copy is ever added — this repo currently holds FY2018/2020/2023/2024 only (see README for why those four years were chosen).

## Balance Sheet Anchors (FY2024, from `swi-10k-fy2024.md`)

| Item | Value | Source line in `swi-10k-fy2024.md` |
|---|---|---|
| Cash and cash equivalents | $251.85M | Balance sheet, line ~1726 |
| Cash + short-term investments | $259.3M | MD&A liquidity discussion, line ~1467 |
| First Lien Term Loan (principal) | $1.236B (original; see filing for amortized/current balance) | Debt footnote, line ~1481 |
| Revolving Credit Facility (undrawn capacity) | $130.0M ($17.5M USD tranche + $112.5M multicurrency tranche) | Debt footnote, line ~1481 |

## What this does NOT cover

- Segment-level or product-line (legacy on-prem vs. observability/subscription) financial splits — SolarWinds reports as a single operating segment; several lesson-questions entries ask for a split that **does not exist** in the public filings at that granularity.
- Full XBRL tag coverage — only the tags listed above were pulled. The raw `swi-companyfacts.json` response (not committed — 1.6MB, regenerate via the API call above if a different tag is needed) has hundreds more tagged data points per period.
