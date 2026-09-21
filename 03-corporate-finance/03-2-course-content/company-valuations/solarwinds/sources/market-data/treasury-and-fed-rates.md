---
title: "Market Rates Snapshot (Treasury, Fed Funds, SOFR)"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-09-07
---

# Market Rates Snapshot

Fetched directly from FRED (Federal Reserve Economic Data) on 2026-09-07, because this repo's own `03-3-supplemental-data/market-rates.json` — the file the course materials are supposed to point to — **does not exist** (see the parent `sources/README.md` for the full note on this).

## Latest values (as of 2026-09-03, most recent business day at fetch time)

| Series | Value | FRED series ID |
|---|---|---|
| 10-Year Treasury Yield | 4.77% | [DGS10](https://fred.stlouisfed.org/series/DGS10) |
| Effective Federal Funds Rate | 3.63% | [DFF](https://fred.stlouisfed.org/series/DFF) |
| SOFR (Secured Overnight Financing Rate) | 3.66% | [SOFR](https://fred.stlouisfed.org/series/SOFR) |

## How to refresh

```bash
curl -L "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10" | tail -5
curl -L "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF" | tail -5
curl -L "https://fred.stlouisfed.org/graph/fredgraph.csv?id=SOFR" | tail -5
```

No API key needed for the CSV graph endpoint. This is a point-in-time snapshot, not a live feed — re-fetch before using in a time-sensitive calculation (e.g. cost of capital as of a specific valuation date).
