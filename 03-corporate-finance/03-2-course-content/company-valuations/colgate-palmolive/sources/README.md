---
title: "Colgate-Palmolive (CL) — Source Manifest"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Compiled Sources

Every document the final project needs, what it feeds, and whether it is in this folder yet. Fetched 2026-11-21. Prices and Capital IQ market figures are as of the 2026-11-20 close.

Filings are the source of record. Capital IQ is a cross-check, and the source only for what filings do not carry (agency rating, holder breakdown, analyst estimates, peer multiples).

## Documents by project section

| Project section (professor's checklist) | Documents | Status |
|---|---|---|
| Corporate governance | 2026 proxy; Capital IQ board, compensation, takeover defenses, public ownership | In folder |
| Risk and hurdle rate: regression | Monthly prices, CL and S&P 500 | In folder |
| Risk and hurdle rate: riskfree rate, equity risk premium, country risk | Damodaran ERP workbook, country risk, regional premiums, FRED 10-year | In folder |
| Risk and hurdle rate: beta by business | FY2025 10-K segment note; Damodaran industry betas (household products, pet food) | In folder |
| Risk and hurdle rate: default risk and cost of debt | Capital IQ credit ratings and debt tranches; 10-K debt note; Damodaran ratings table | In folder |
| Past and future investments | FY2025 and FY2024 10-Ks; twelve-year XBRL series | In folder |
| Optimal capital structure | Professor's `capstru.xlsx`; 10-K; sector debt ratios (Damodaran) | In folder (`../professor-spreadsheet/originals/`) |
| Debt design | Capital IQ bond list (currency, maturity, fixed or floating); professor's `macrodur.xlsx` | In folder |
| Dividend analysis | Twelve-year cash flow series (dividends, buybacks, capex, debt issued and repaid); professor's `dividends.xlsx` | In folder (`../professor-spreadsheet/originals/`) |
| Valuation | Professor's `fcffsimpleginzu.xlsx`; latest 10-Q for trailing twelve months; analyst estimates; peer multiples | In folder |

## `filings/` — the company's own statements (SEC EDGAR, CIK 0000021665)

Converted from the EDGAR HTML to plain text, tables kept as tab-separated rows.

| File | What it is | Filed |
|---|---|---|
| `cl-10k-fy2025.txt` | FY2025 10-K, the base year. Accession 0000021665-26-000006 | 2026-02-23 |
| `cl-10k-fy2024.txt` | FY2024 10-K. Accession 0000021665-25-000008 | 2025-02-13 |
| `cl-10q-2026-q3.txt` | 10-Q for the quarter ended 2026-09-30: trailing twelve months, 794,920,513 shares on the cover. Accession 0000021665-26-000048 | 2026-10-30 |
| `cl-def14a-2026.txt` | 2026 proxy: board, pay, beneficial ownership, one vote per share. Accession 0001308179-26-000136 | 2026-03-25 |
| `cl-multi-year-financials-fy2014-fy2025.tsv` | Every us-gaap and dei annual value CL reported for FY2014–FY2025 (299 tags), from the SEC XBRL company-facts API. Latest-filed value wins for each year | fetched 2026-11-21 |

## `capital-iq/` — NYU academic account, classic platform, company ID 262247

Each file is one Capital IQ page, tables as tab-separated rows.

| File | Contents |
|---|---|
| `key-stats.tsv` | FY2022–FY2025, LTM Sep-2026, consensus 2026–2028; capitalization; multiples |
| `income-statement.tsv`, `balance-sheet.tsv`, `cash-flow.tsv` | FY2021–FY2025 and LTM Sep-2026 |
| `ratios.tsv`, `multiples.tsv`, `capitalization.tsv` | Returns, margins, leverage, coverage; trading multiples history |
| `segments.tsv` | Revenue, operating profit, D&A and capex for the five Oral, Personal and Home Care regions and Hill's Pet Nutrition, FY2020–FY2025 |
| `capital-structure-summary.tsv`, `capital-structure-details.tsv`, `fixed-income-securities.tsv` | Debt by type; each note with coupon, maturity and currency |
| `credit-ratings.tsv` | S&P issuer rating A+ (stable), rated 2024-04-19, and each rated note |
| `public-ownership.tsv` | Institutions 87.19%, insiders 0.13%; top holders; activists |
| `board-members.tsv`, `compensation.tsv`, `corporate-governance.tsv` | Directors and tenure, executive pay, takeover defenses |
| `ciq-estimates.tsv` | Consensus revenue, EBITDA, EPS to 2030; target price; guidance |
| `quick-comps.tsv`, `competitors.tsv` | Ten peers (KMB, PG, CLX, EL, CHD, Reckitt, Henkel, GIS, COTY, SJM) |
| `pension-opeb.tsv` | Pension and retiree-benefit obligations |
| `peer-betas.tsv` | Five-year beta and dividend yield for the ten companies on Capital IQ's comparison list and Colgate |
| `peer-cash-returned.tsv` | Net income, dividends, buybacks and share issuance for Colgate and six household peers, last five fiscal years |
| `transcript-notes.md` | Paraphrased notes on growth statements from three 2026 transcripts |

Capital IQ standardizes some lines. Its FY2025 EBIT of $4,238M leaves out restructuring and impairment charges that GAAP operating income of $3,306M includes.

## `market-data/`

| File | What it is |
|---|---|
| `market-rates-2026-11-19.json`, `ratings-spreads-2026-01-01.json`, `industry-betas-2026-01-05.json`, `country-risk-2026-07-01.json` | Damodaran and FRED snapshots written by `scripts/refresh-market-data.py` on 2026-11-21, named by their own dates |
| `country-risk-regions-2026-01-01.md` | Regional country risk premiums and US industry averages read from the professor's valuation workbook |
| `cl-vs-sp500-monthly-2020-12-to-2026-11.tsv` | Month-end close and dividend-adjusted close for CL, S&P 500 and S&P 500 total return, from Yahoo Finance's chart endpoint. The November 2026 row is the 2026-11-20 close, not a month-end |

## Still to get

| What | Where | Why not yet |
|---|---|---|
| Moody's rating | Moody's site or a CL press release | The 10-K does not state its ratings |
| Peer fundamentals from each peer's own filings | `fetch-peer-facts.py` | Peers are taken from Capital IQ's comparison list; the ledger's `peers` block is not filled |
| Revenue by country | 10-K gives United States and emerging markets only | The country risk premium will rest on regional segments |
