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

Record both the last unaffected share price (`company.share_price`) and the deal price (`company.deal_price`). `meta.analysis_date` is the date of the unaffected price, and every market input is fetched for that date with `scripts/refresh-market-data.py --as-of`. Regression beta uses the last clean pre-announcement window and the ledger notes the window; free price sources drop delisted tickers, so expect to omit it.

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
| Ratings-to-spread table (current `ratings-spreads.json` snapshot) | synthetic rating from whatever EBIT and interest can be bounded | `market-data/ratings-spreads-<as_of>.json` |

Every estimated number is a `{value, source, as_of, estimate: true, range: [low, high]}` leaf. The walkthrough calls each one an estimate. Questions tagged `applies_to: [public, delisted]` are skipped and listed.

## Market data, all types

| Item | Origin | Check first |
|---|---|---|
All of these come from `python3 scripts/refresh-market-data.py`, which writes them to `03-corporate-finance/03-3-supplemental-data/` with an `as_of` date. A weekly CI job runs the same script; run it again at the start of every valuation anyway.

| Item | Ledger fields | File and key |
|---|---|---|
| 10-year Treasury on the analysis date | `market.govt_bond_rate` | `market-rates.json` → `fred_latest.treasury_10y` |
| US sovereign default spread (Aa1) | `market.sovereign_default_spread` | `market-rates.json` → `damodaran_monthly.us_sovereign_default_spread` |
| Risk-free rate | `market.risk_free_rate` | govt_bond_rate − sovereign_default_spread |
| Mature-market ERP, implied, over the risk-free rate | `market.mature_erp` | `market-rates.json` → `damodaran_monthly.implied_erp_over_dollar_riskfree` |
| SOFR (floating-rate debt benchmark) | `debt.kd_pretax_observed` check | `market-rates.json` → `fred_latest.sofr` |
| Country risk premiums and sovereign default spreads | `country.exposures[].erp`, non-US `sovereign_default_spread` | `country-risk.json` → `countries` |
| Industry unlevered betas, cash-corrected | `beta.unlevered_bottom_up`, `beta.segments` | `industry-betas.json` → `industries` |
| Ratings-to-spread tables (large, small, financial) | `market.ratings_table` | copy `ratings-spreads.json` to `sources/market-data/ratings-spreads-<as_of>.json` |
| Marginal tax rate by country | `market.tax_rate_marginal` | `country-risk.json` has no tax column; use lesson 12 `spreadsheet-countrytaxrates24.md` and check the country's current statutory rate |

The lesson spreadsheets teach the method; their numbers are as old as the lesson. Never take a current rate, premium, beta or spread from them. If the refresh fails, stop and report which source broke.

## Peers, all types

Three to ten comparable listed companies in the same business and at a similar stage (growth and margins, not only product overlap), same fiscal period as the base year. For a company that was sold, the set a fairness opinion used is a defensible starting point.

Run `python3 .claude/skills/value-company/tools/fetch-peer-facts.py --date <analysis_date> TICKER ... > sources/peer-filings/peer-facts-<analysis_date>.md`. It takes each peer's latest fiscal year ended by the analysis date from SEC XBRL company facts and its closing price on that date, and lists the XBRL tag behind every figure; check any `n/a` or flagged tag by hand against the 10-K. Copy the rows into `peers[]`. Say in the manifest why each peer was chosen and which candidates were rejected.

## What not to do

- Do not take a number from a data aggregator when the filing has it. Aggregators quote stale figures as current.
- Do not store a web search result as a source. Fetch the page, save it, cite the saved file.
- Do not fill a ledger field from memory. If it can't be sourced, it is omitted or marked as an estimate with a range.
