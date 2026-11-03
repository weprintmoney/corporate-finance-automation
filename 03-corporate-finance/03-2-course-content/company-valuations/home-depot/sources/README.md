---
title: "Home Depot — source manifest (blind, as of 2026-06-30)"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Source manifest

Every file here was published on or before 2026-06-30; `published.yaml` lists each with its date. All fetched on 2026-11-03.

| File | What it is | Origin | Published |
|---|---|---|---|
| filings/hd-10-k-2026-03-18.md | 10-K, fiscal 2025 (to 2026-02-01) | EDGAR via `tools/fetch-filings.py` | 2026-03-18 |
| filings/hd-10-k-2025-03-21.md | 10-K, fiscal 2024; source of fiscal 2022 figures | EDGAR | 2025-03-21 |
| filings/hd-10-q-2026-05-27.md | 10-Q, Q1 fiscal 2026 (to 2026-05-03) | EDGAR | 2026-05-27 |
| filings/hd-def14a-2026-04-07.md | 2026 proxy | EDGAR | 2026-04-07 |
| filings/hd-8-k-2026-05-19-items-202-901.md | Q1 fiscal 2026 earnings release, guidance reaffirmed | EDGAR (exhibit refetched, see below) | 2026-05-19 |
| filings/hd-8-k-2026-02-24-items-202-901.md | Q4 fiscal 2025 release, fiscal 2026 guidance, dividend +1.3% | EDGAR | 2026-02-24 |
| filings/hd-8-k-2025-11-18-items-202-901.md | Q3 fiscal 2025 release | EDGAR | 2025-11-18 |
| filings/hd-8-k-2025-08-19-items-202-901.md | Q2 fiscal 2025 release | EDGAR | 2025-08-19 |
| filings/hd-8-k-2026-05-26-items-503-507-901.md | 2026 annual meeting votes, charter amendments | EDGAR | 2026-05-26 |
| filings/hd-8-k-2025-11-24-items-503-801-901.md | Bylaw/charter item and other event | EDGAR | 2025-11-24 |
| filings/hd-8-k-2025-09-10-items-801-901.md, filings/hd-8-k-2025-09-15-items-801-901.md | September 2025 senior notes offering documents | EDGAR | 2025-09-10, 2025-09-15 |
| filings/index.md | All HD filings 2023-06-28 to 2026-06-30 by form and month | EDGAR submissions API | 2026-06-30 |
| market-data/market-rates-2026-06-30.json | June 2026 Damodaran ERP workbook figures + FRED closes on 2026-06-30 | `scripts/refresh-market-data.py --as-of 2026-06-30` | 2026-06-30 |
| market-data/ratings-spreads-2026-01-01.json | Damodaran coverage-to-rating table, January 2026 | same | 2026-01-01 |
| market-data/country-risk-2026-01-01.json | Damodaran country risk premiums, January 2026 | same | 2026-01-01 |
| market-data/industry-betas-2026-01-05.json | Damodaran US industry betas, January 2026 | same | 2026-01-05 |
| market-data/rates-2026-06-30.md | The rates used, both monthly and FRED | written from the json above | 2026-06-30 |
| peer-filings/peer-facts-2026-06-30.md | XBRL fundamentals for HD, LOW, FND, TSCO, BLDR, POOL; closes on 2026-06-30 | `tools/fetch-peer-facts.py --date 2026-06-30` | 2026-06-30 |
| statements/hd-stated-positions.md | Verbatim passages on each signal | excerpts of the filings above | 2026-05-27 |

## Peers

Lowe's (the only full-line peer); Floor & Decor and Tractor Supply (US big-box specialty retail); Builders FirstSource and Pool Corp (Pro distribution, comparable to SRS/GMS). Rejected: QXO/Beacon and GMS (acquired or transformed in 2025, no clean fiscal year), Sherwin-Williams (manufacturer), Walmart and Costco (general retail).

## Could not be obtained

- Regression beta: no price-history tool is allowed in the blind run.
- Agency credit rating: not disclosed in the fetched filings.
- Fiscal 2021 statements and the fiscal 2022 balance sheet: only the two latest 10-Ks are fetched, so `company.history` has four years and fiscal 2022 lacks invested capital and debt.
- Analyst consensus growth: no allowed source.

## Tool problems worked around

- `tools/fetch-filings.py` line 177: the exhibit filter `ex[-_]?\d` misses HD's exhibit names (`hd_exhibit991x05032026.htm`), so the first fetch saved the earnings 8-Ks without their press releases. Re-ran a copy with `ex(hibit)?[-_]?\d` from the scratchpad; same EDGAR filings, same cutoff.
- `tools/make-exhibits.py` `returns()` (line 181) fails on any history row whose ROIC is `n/a`; drew the returns chart with a copy that skips those rows (fiscal 2022 has no invested capital).
