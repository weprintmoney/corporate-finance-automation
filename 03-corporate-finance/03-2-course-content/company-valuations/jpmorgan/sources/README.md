---
title: "JPMorgan Chase — sources manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Sources manifest

Everything here was fetched on 2026-11-03 by the tools named, with a cutoff of 2026-06-30. Publication dates are in `published.yaml`; none is after 2026-06-30.

| File or group | What it is | Origin | Fetched |
|---|---|---|---|
| `filings/jpm-10-k-2026-02-13.md` | 10-K, fiscal 2025 | SEC EDGAR via `tools/fetch-filings.py JPM jpmorgan --cutoff 2026-06-30 --cik 19617` | 2026-11-03 |
| `filings/jpm-10-k-2025-02-14.md` | 10-K, fiscal 2024 | same | 2026-11-03 |
| `filings/jpm-10-q-2026-05-01.md` | 10-Q, quarter ended 2026-03-31 | same | 2026-11-03 |
| `filings/jpm-def14a-2026-04-06.md` | 2026 proxy statement | same | 2026-11-03 |
| `filings/jpm-8-k-*.md` (19 files) | Earnings supplements (Ex. 99.2 only), stress-test capital releases, item 5.02 officer and pay filings, note issuances, preferred redemption, bylaw changes | same | 2026-11-03 |
| `filings/index.md` | Filing index written by the tool | same | 2026-11-03 |
| `peer-filings/bank-peer-facts-2026-06-30.md` | FY2025 net income, dividends, buybacks and equity for JPM, BAC, C, WFC, GS, MS, PNC and USB, from 10-Ks filed on or before 2026-06-30; shares filed on or before 2026-06-30; closes on 2026-06-30 | Scratch wrapper calling `tools/fetch-peer-facts.py`'s own functions with bank tags | 2026-11-03 |
| `peer-filings/peer-facts-2026-06-30.md` | Stock tool output for JPM, BAC, C and WFC (GS and MS crashed it); kept as a record, not used | `tools/fetch-peer-facts.py --date 2026-06-30` | 2026-11-03 |
| `market-data/market-rates-2026-06-01.json` | Damodaran ERPJune26 plus FRED 10-year, SOFR and fed funds closes on 2026-06-30 | `scripts/refresh-market-data.py --as-of 2026-06-30` | 2026-11-03 |
| `market-data/ratings-spreads-2026-01-01.json` | Damodaran ratings-to-spread tables, January 2026 | same | 2026-11-03 |
| `market-data/country-risk-2026-01-01.json` | Damodaran country risk premiums, January 2026 | same | 2026-11-03 |
| `market-data/industry-betas-2026-01-05.json` | Damodaran US industry betas, January 2026 | same | 2026-11-03 |
| `statements/jpm-stated-positions.md` | Stated side of each signal, quoted from the filings above | Extracted by hand from the files above | 2026-11-03 |

Peers chosen: the large US banks (BAC, C, WFC), the two investment-bank holding companies (GS and MS, for the CIB mix) and two large regionals (PNC and USB) to widen the ROE range for the P/B-on-ROE line. Rejected: foreign banks, which file no 10-K XBRL.

Could not be obtained within the rules:
- Exhibit 99.1 (the earnings release narrative) of the earnings 8-Ks: `fetch-filings.py` saved only Exhibit 99.2. The 10-Q repeats the outlook, so nothing material is missing.
- A regression beta for JPM: no allowed source.
- Analyst consensus: no allowed source.
- A numeric management CET1 target: the filings do not disclose one (statements S-9).
- Peer common equity for BAC, MS, PNC and USB: preferred stock is untagged in their XBRL, so total equity is used.
