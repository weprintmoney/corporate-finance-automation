---
title: "Coca-Cola (KO) — source manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Sources

All fetched on 2026-11-03 for a blind run as of 2026-06-30. Publication dates are in `published.yaml`.

| File | What it is | Origin |
|---|---|---|
| `filings/ko-10-k-2026-02-20.md` | 10-K FY2025 | EDGAR via `fetch-filings.py --cutoff 2026-06-30` |
| `filings/ko-10-k-2025-02-20.md` | 10-K FY2024 | same |
| `filings/ko-10-q-2026-04-30.md` | 10-Q Q1 2026 | same |
| `filings/ko-def14a-2026-03-16.md` | Proxy statement 2026 | same |
| `filings/ko-8-k-*.md` | 8-Ks, item 5.02 (2025-10-16, 2025-12-10, 2026-01-14, 2026-02-20, 2026-06-25) | same |
| `filings/index.md` | Every filing 2023-06-28 to 2026-06-30 by month, with 8-K items | same |
| `market-data/market-rates-2026-06-01.json` | Damodaran June 2026 ERP workbook + FRED closes on 2026-06-30 | `scripts/refresh-market-data.py --as-of 2026-06-30` |
| `market-data/ratings-spreads-2026-01-01.json` | Coverage → rating → spread tables | same |
| `market-data/country-risk-2026-01-01.json` | Country ratings, default spreads and premiums (January 2026) | same |
| `market-data/industry-betas-2026-01-05.json` | US industry betas (January 2026) | same |
| `market-data/rates-2026-06-30.md` | The rates used, monthly vs. FRED | compiled from the above |
| `market-data/us-marginal-tax-rate.md` | US marginal rate 25% | lesson 12 country tax table |
| `peer-filings/peer-facts-2026-06-30.md` | Peer XBRL facts and closes on 2026-06-30, plus KO's own close | `fetch-peer-facts.py --date 2026-06-30 KO PEP KDP MNST COKE CELH` |
| `statements/ko-stated-positions.md` | What the company says, by signal, quoted with line numbers | compiled from the filings |

## Peers

PepsiCo, Keurig Dr Pepper, Monster, Celsius and Coca-Cola Consolidated are the US-listed beverage companies that file 10-Ks. Coca-Cola FEMSA, CCEP and Coca-Cola HBC are bottlers that file 20-Fs or are listed abroad, and Coca-Cola holds equity stakes in them, so they were not used. None of the peers is a concentrate business like Coca-Cola.

## Known problems with the tool output

- KO borrowings show as 0.0 in `peer-facts-2026-06-30.md` because KO's debt is not tagged with the tags the tool reads. KO's debt comes from the 10-K, not the tool.
- Monster: the Yahoo close is split-adjusted. The 2025-12-31 close comes back as $38.33, while KO's 10-K Note 6 values its Monster stake at about $76 a share. The tool's market cap (close × pre-split shares) is therefore wrong, and Monster's market values are left out. Net income is untagged.
- Coca-Cola Consolidated: the share count is untagged (dual class), so there is no market cap. Its book equity is negative.

## Not obtained

- Earnings releases (8-K item 2.02, 2026-02-10 and 2026-04-28) carrying full-year 2026 guidance: the fetch tool does not take item 2.02.
- Balance sheets before 2023 (only two 10-Ks fetched), so the history covers 2023–2025.
- Regression beta and analyst consensus: no permitted source in a blind run.
