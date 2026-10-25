---
title: "SolarWinds (SWI) — Source Manifest"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Compiled Sources

Every document the ledger (`../inputs.yaml`) cites. Filings were fetched from SEC EDGAR (CIK 0001739942) on 2026-09-07. Market and peer data were fetched on 2026-10-25, as of the analysis date, 2025-02-05.

## `filings/` — the company's own statements

| File | What it is | Filed |
|---|---|---|
| `swi-10k-fy2024.md` | FY2024 10-K, the base year and last full year as a public company. Feeds most `company.*` and `debt.*` fields and the 2023–2024 history rows | 2025-02-19 |
| `swi-10k-fy2023.md` | FY2023 10-K, for the 2022 balance sheet | 2024-02-16 |
| `swi-10k-fy2020.md` | FY2020 10-K, the SUNBURST year | 2021-03-01 |
| `swi-10k-fy2018.md` | FY2018 10-K, the first after the October 2018 IPO | 2019-02-25 |
| `swi-def14a-2024.md` | 2024 proxy, the last before the deal: board, pay, beneficial ownership, stockholders' agreement | 2024-04-11 |
| `swi-s1-2018-ipo-prospectus.md` | IPO prospectus: pre-IPO capital structure and use of proceeds | 2018-09-21 |
| `swi-8k-2020-12-09-sunburst-disclosure.md`, `swi-8k-2020-12-14-sunburst-followup.md` | SUNBURST disclosures | 2020-12 |
| `swi-multi-year-financials.md` | Revenue, EBIT, net income, R&D and capex for FY2017–2024 from the SEC XBRL company-facts API | fetched 2026-09-07 |

**Not fetched:** the FY2019, FY2021 and FY2022 10-Ks. Years before 2022 include N-able, which was spun off in July 2021, so they are not comparable. FY2022 flows come from the FY2024 10-K's three-year statements, and the 2022 balance sheet from the FY2023 10-K. Accessions for the missing 10-Ks: FY2019 0001739942-20-000011, FY2021 0001739942-22-000020, FY2022 0001739942-23-000019, at `https://www.sec.gov/Archives/edgar/data/1739942/<accession-no-dashes>/`.

## `deal-docs/` — the going-private transaction

| File | What it is | Filed |
|---|---|---|
| `swi-defm14c-2025-merger.md` | Definitive information statement (Schedule 14C). Silver Lake and Thoma Bravo approved by written consent, so there was no vote, no DEFM14A and no 13E-3. Background of the merger, Goldman Sachs and Jefferies fairness opinions, management forecasts 2025–2030 (`forecast.years`), golden parachutes, record-date share count | 2025-03-27 |
| `swi-8k-2025-02-07-merger-agreement.md` | Merger agreement announced | 2025-02-07 |
| `swi-8k-2025-04-16-merger-closing.md` | Closing | 2025-04-16 |

## `market-data/` — as of 2025-02-05

Written by `python3 scripts/refresh-market-data.py --as-of 2025-02-05 --out <dir>` on 2026-10-25, then copied here with their dates in the names.

| File | What it is | Feeds |
|---|---|---|
| `rates-2025-02-05.md` | The rates used, with both the monthly Damodaran and the daily FRED figures | read first |
| `market-rates-2025-02-05.json` | Damodaran ERPFeb25.xlsx (start of February 2025) and FRED closes on 2025-02-05 | `market.govt_bond_rate`, `market.mature_erp` |
| `ratings-spreads-2025-01-01.json` | Damodaran's coverage-to-rating-to-spread tables, January 2025 edition (`ratings24.xls`) | `market.ratings_table` |
| `industry-betas-2025-01-05.json` | Damodaran US industry betas, January 2025 (`betas24.xls`) | `beta.unlevered_bottom_up` |
| `country-risk-2025-01-01.json` | Damodaran country risk, January 2025 (`ctryprem24.xlsx`). The regional EMEA premium and the US 25% marginal tax rate come from the same workbook's Regional Weighted Averages and Country Tax Rates sheets (URL in the file's `source_url`) | `market.sovereign_default_spread`, `country.exposures`, `market.tax_rate_marginal` |

## `peer-filings/`

| File | What it is |
|---|---|
| `peer-facts-2025-02-05.md` | Eight peers from Jefferies' fairness-opinion set: fiscal-2024 fundamentals from SEC XBRL company facts, plus closing prices on 2025-02-05. Explains why each was chosen, and why Datadog, Dynatrace and PagerDuty were rejected |

## `capital-iq/` — cross-check only

Capital IQ pulls from the NYU academic account, 2026-10-05; see `capital-iq/README.md`. The ledger cites filings, not these files, wherever a filing has the number. Capital IQ standardizes some lines differently: its EBIT of $218.7M excludes $10.3M of unusual items that GAAP operating income of $208.4M includes. Its governance page reflects the post-closing charter; use the proxy.

## Could not be obtained

| What | Why | Effect |
|---|---|---|
| SWI daily price history | Free sources no longer serve delisted tickers (Yahoo: "symbol may be delisted"; Nasdaq drops them; Stooq blocks scripts), and Capital IQ's chart module did not load | No regression beta, R², or Jensen's alpha. The bottom-up beta is used, and those fields are listed under `meta.omitted` |
| Analyst consensus growth | Capital IQ estimates grid was empty | Management's forecast in the deal document is used |
| Agency credit rating | The 10-K and the deal document disclose none; agency reports are subscription-only | `debt.rating_actual` is null; the synthetic rating is used |
| Informatica's price on 2025-02-05 | Acquired since; not in free price sources | Dropped from the peer set |
