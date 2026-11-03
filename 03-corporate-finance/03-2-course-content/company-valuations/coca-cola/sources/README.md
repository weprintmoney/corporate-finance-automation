---
title: "The Coca-Cola Company — source manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Source manifest

All files fetched 2026-11-03. Publication dates are in `published.yaml`; none is after 2026-06-30.

| File | What it is | Origin |
|---|---|---|
| `filings/ko-10-k-2026-02-20.md` | FY2025 10-K | EDGAR via `tools/fetch-filings.py KO --cutoff 2026-06-30 --cik 21344` |
| `filings/ko-10-k-2025-02-20.md` | FY2024 10-K (2022-2024 statements) | same |
| `filings/ko-10-q-2026-04-30.md` | Q1 2026 10-Q | same |
| `filings/ko-def14a-2026-03-16.md` | 2026 proxy statement | same |
| `filings/ko-8-k-2025-07-22…`, `-2025-10-21…`, `-2026-02-10…`, `-2026-04-28-items-202-901.md` | Earnings releases (Item 2.02) with exhibits | same |
| `filings/ko-8-k-2025-10-16…`, `-2025-12-10…`, `-2026-01-14…`, `-2026-02-20…`, `-2026-06-25-items-502-901.md` | Director and officer changes (Item 5.02) | same |
| `filings/index.md` | Every EDGAR filing 2023-06-28 to 2026-06-30 by month | same |
| `peer-filings/peer-facts-2026-06-30.md` | FY2025 XBRL facts and 2026-06-30 closes: KO, PEP, KDP, MNST, CELH, COKE | `tools/fetch-peer-facts.py --date 2026-06-30` |
| `market-data/market-rates-2026-06-01.json` | Damodaran June 2026 ERP workbook; FRED DGS10, SOFR, fed funds closes on 2026-06-30 | `scripts/refresh-market-data.py --as-of 2026-06-30` |
| `market-data/ratings-spreads-2026-01-01.json` | Coverage → rating → spread tables | same |
| `market-data/country-risk-2026-01-01.json` | Country default spreads and premiums | same |
| `market-data/industry-betas-2026-01-05.json` | Industry betas | same |
| `market-data/rates-2026-06-30.md` | The rates used, side by side | written from the JSON above |
| `statements/stated-by-signal.md` | Verbatim stated-side passages by signal | excerpted from the filings above |

## Peer choices

PepsiCo and Keurig Dr Pepper (the closest beverage peers), Monster (energy drinks; Coca-Cola owns 21%), Celsius (high-growth energy). Coca-Cola Consolidated was fetched but left out: no share count in XBRL (dual class) and negative book equity. Rejected: Coca-Cola Europacific Partners (the tool crashes on it; it files no 10-K XBRL facts the tool can read), Primo Brands (ticker not in SEC's list as PRMW).

## Not obtained

- Regression beta and any price history: no allowed source in a blind run.
- Analyst consensus: no allowed source.
- 2022 balance sheet: not in either fetched 10-K, so 2022 debt and invested capital are omitted.
- Country-level revenue split: not disclosed; regional baskets used (see `inputs.yaml` `country.exposures`).
