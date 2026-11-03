---
title: "Comcast (CMCSA) — sources manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Sources manifest

All fetched 2026-11-03 with the blind-run tools; publication dates in `published.yaml`. Nothing published after 2026-06-30.

| File or group | What it is | Origin |
|---|---|---|
| `filings/*.md`, `filings/index.md` | Comcast 10-Ks (FY2024, FY2025), 10-Q Q1 2026, DEF 14A 2026, 8-Ks to 2026-06-29 | `tools/fetch-filings.py CMCSA comcast --cutoff 2026-06-30 --cik 1166691` (SEC EDGAR) |
| `peer-filings/peer-facts-2026-06-30.md` | FY figures and 2026-06-30 closes for CMCSA, CHTR, T, VZ, TMUS, DIS, FOXA | `tools/fetch-peer-facts.py --date 2026-06-30` (SEC XBRL + closing prices) |
| `market-data/market-rates-2026-06-01.json` | Damodaran June 2026 ERP workbook values; FRED 10-year, SOFR, fed funds closes on 2026-06-30 | `scripts/refresh-market-data.py --as-of 2026-06-30` |
| `market-data/ratings-spreads-2026-01-01.json` | Damodaran coverage-to-rating tables, January 2026 | same |
| `market-data/country-risk-2026-01-01.json` | Damodaran country risk premiums, January 2026 | same |
| `market-data/industry-betas-2026-01-05.json` | Damodaran US industry betas, January 2026 | same |
| `statements/cmcsa-stated-positions.md` | Quoted passages from the filings above, by signal | compiled from `filings/` |

Peer choice: Charter (closest cable peer), AT&T, Verizon, T-Mobile (connectivity and wireless), Disney and Fox (media, parks, studios). Rejected: Warner Bros. Discovery (the peer tool could not resolve the ticker, see below), Paramount Skydance and Altice USA (not tried; small or in transition).

## Could not be obtained

- Revenue by country: Comcast does not publish it; estimated in `inputs.yaml`.
- Versant's full-year 2025 results: Comcast's filings give only Q1 2025; the Versant filings are under another registrant and outside the blind fetch.
- An agency credit rating: none of the filings states one.
- Charter revenue: the XBRL tag picked returned 889 (millions), clearly wrong; left out of `peers`.
- WBD: `fetch-peer-facts.py` raised an error for this ticker; dropped from the peer set.
- 2022 balance sheet: not in the two fetched 10-Ks; 2022 invested capital estimated.
