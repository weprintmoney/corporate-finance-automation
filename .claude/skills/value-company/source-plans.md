---
title: "Source plans — where each ledger field comes from, by company type"
status: active
owner: weprintmoney
created: 2026-10-24
last_updated: 2026-10-24
---

# Source plans

Phase 1 of `/value-company` compiles `sources/` according to the company's type. The plan says which documents to fetch, what to name them, and which ledger fields each one feeds. Every file saved into `sources/` goes into `sources/README.md` with its origin and fetch date.

## Folder layout

```
sources/
  README.md              manifest: file, what it is, origin, fetched on, what could not be obtained
  filings/               the company's own statements and disclosures
  peer-filings/          one annual report per comparable company
  market-data/           rates, ERP, country premiums, industry betas, ratings table — each dated
  deal-docs/             merger, tender, or financing documents, if any
```

## Company types

### `public` (listed in the US, files with the SEC)

| Document | Feeds | Name as |
|---|---|---|
| 10-K, latest three fiscal years (five if available via XBRL) | `company.*`, `company.history`, `debt.*`, lease note, options note, segment note, geographic revenue | `filings/<ticker>-10k-fy<year>.md` |
| Latest 10-Q | `company.shares_basic` (cover page), any post-year-end debt change | `filings/<ticker>-10q-<quarter>.md` |
| DEF 14A (latest proxy) | `governance.board`, `governance.controlling_holders`, `governance.change_of_control_payouts`, `governance.share_classes` | `filings/<ticker>-def14a-<year>.md` |
| 8-Ks for material events in the base year | context, rating actions, financing changes | `filings/<ticker>-8k-<date>-<topic>.md` |
| XBRL company-facts (SEC API) | `company.history` numeric series | `filings/<ticker>-multi-year-financials.md` |
| Credit agreement or indenture (10-K exhibit) | `debt.covenants`, `debt.rate_type`, `debt.maturity_years`, `debt.currency` | `filings/<ticker>-credit-agreement.md` |

### `delisted` (filings exist up to a date, no live price)

Everything in `public`, plus:

| Document | Feeds | Name as |
|---|---|---|
| The going-private document: DEFM14A (proxy vote) or DEFM14C (written consent) or Schedule 13E-3 | deal terms, management forecasts (`forecast.years`), fairness-opinion assumptions, background of the merger | `deal-docs/<ticker>-<form>-<year>-merger.md` |
| 8-K announcing and 8-K closing the deal | deal price, financing | `deal-docs/<ticker>-8k-<date>-<topic>.md` |

Record both the last unaffected share price and the deal price in the ledger; `meta.price_basis` says which one `company.share_price` is. Regression beta uses the last clean pre-announcement window and the ledger notes the window.

### `foreign-public` (listed outside the US)

| Document | Feeds | Name as |
|---|---|---|
| Annual report, latest three years (IFRS or local GAAP) | as for 10-K; note the accounting basis in `meta.accounting_basis` | `filings/<ticker>-annual-report-<year>.md` |
| Local regulator filings or the stock exchange's disclosure portal | governance, shareholders | `filings/<ticker>-<form>-<year>.md` |
| Home-country government bond yield and sovereign rating | `market.risk_free_rate` after netting the default spread (lesson 5) | `market-data/<country>-government-bond-and-rating.md` |
| Damodaran country risk premium (global dataset) | `country.exposures[].erp` | `market-data/damodaran-country-risk-premium.md` |

Decide the analysis currency in Phase 0; if it is not the reporting currency, convert consistently and say so in `meta`.

### `private` (no public filings)

| Document | Feeds | Name as |
|---|---|---|
| Company statements: website, press releases, funding announcements, any audited numbers released | revenue, headcount, funding, ownership | `filings/<slug>-company-statements.md` |
| Trade press and reputable profiles | bounding ranges for revenue, margins, debt | `filings/<slug>-press-profile.md` |
| Industry unlevered beta and total beta (lesson 11) | `beta.unlevered_bottom_up`, `beta.total_beta` | `market-data/damodaran-industry-betas-<sector>.md` |
| Ratings-to-spread table (lesson 12 / 18 spreadsheet) | synthetic rating from whatever EBIT and interest can be bounded | `market-data/ratings-and-spreads.md` |

Every estimated number is a `{value, source, as_of, estimate: true, range: [low, high]}` leaf. The walkthrough calls each one an estimate. Questions tagged `applies_to: [public, delisted]` are skipped and listed.

## Market data, all types

| Item | Origin | Check first |
|---|---|---|
| Risk-free rate (10-year government bond in the analysis currency) | FRED (US) or the central bank | `03-corporate-finance/03-3-supplemental-data/market-rates.json` |
| Mature-market ERP (implied) | Damodaran's current ERP page | none |
| Country risk premiums | Damodaran country risk dataset | `03-3-supplemental-data/country-risk.json` |
| Industry unlevered betas, cash-corrected | Damodaran betas dataset | `03-3-supplemental-data/industry-betas.json` |
| Ratings-to-spread tables (large and small firm) | lesson 18 `spreadsheet-cost-of-capital-optimal.md`, "Default Spreads and Ratios" | in repo |
| Marginal tax rate by country | lesson 12 `spreadsheet-countrytaxrates24.md` | in repo |

If a supplemental-data file is missing or its data block is empty, fetch directly, save under `market-data/` with the fetch date, and note it in the manifest.

## Peers, all types

Three to six comparable listed companies in the same business, same fiscal period as the base year. For each: latest annual report → `peer-filings/<ticker>-<form>-fy<year>.md`, feeding `peers[]` (enterprise value, revenue, EBITDA, net income, book equity, growth, margin, beta, debt ratio, payout). Say in the manifest why each peer was chosen and which candidates were rejected.

## What not to do

- Do not take a number from a data aggregator when the filing has it. Aggregators quote stale figures as current.
- Do not store a web search result as a source. Fetch the page, save it, cite the saved file.
- Do not fill a ledger field from memory. If it can't be sourced, it is omitted or marked as an estimate with a range.
