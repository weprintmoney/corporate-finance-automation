---
title: "Eaton (ETN) — Sources manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Sources manifest

All fetched 2026-11-03. Publication dates are in `published.yaml`; none is after 2026-06-30.

## filings/ (EDGAR, via `tools/fetch-filings.py ETN --cutoff 2026-06-30 --cik 1551182`, re-run with an exhibit-name fix)

| File | What it is |
|---|---|
| etn-10-k-2026-02-26.md | 10-K for 2025: statements, debt, lease, tax, equity, segment and geographic notes, ratings |
| etn-10-k-2025-02-27.md | 10-K for 2024: 2022 income and cash flow columns, 2023 balance sheet |
| etn-10-q-2026-05-05.md | 10-Q for Q1 2026: post-acquisition balance sheet, Boyd/Ultra purchase accounting, notes issued, buyback pause |
| etn-def14a-2026-03-13.md | 2026 proxy: board, ownership, pay design |
| etn-8-k-2026-06-11-items-701-801-901.md | Mobility–Dana Reverse Morris Trust, press release |
| etn-8-k-2026-03-10-items-102-203-901.md | $8.5B U.S. and €1.2B euro notes; term loan terminated |
| etn-8-k-2026-02-06-items-101-203-901.md | $8B term loan (undrawn) and revolver upsize |
| etn-8-k-2025-09-29-items-101-102-203-901.md | New $3B five-year revolver |
| etn-8-k-2026-03-02-items-502-901.md, etn-8-k-2026-03-02-items-502.md | CFO appointment; 2026 incentive metrics |
| etn-8-k-2025-11-20-items-502-701-901.md | CFO Leonetti departure |
| etn-8-k-2025-07-21-items-502.md, etn-8-k-2025-07-23-items-502-901.md | CHRO departure; director added |
| etn-8-k-2025-08-05/2025-11-04/2026-02-03/2026-05-05 (items 202-901) | Earnings releases with guidance |
| index.md | Every filing 2023-06-28 to 2026-06-30 by form and month |

## market-data/ (`scripts/refresh-market-data.py --as-of 2026-06-30`)

market-rates-2026-06-01.json, ratings-spreads-2026-01-01.json, country-risk-2026-01-01.json, industry-betas-2026-01-05.json, rates-2026-06-30.md.

## peer-filings/

peer-facts-2026-06-30.md (`tools/fetch-peer-facts.py --date 2026-06-30 ETN HUBB VRT EMR ROK PH AME NVT GEV`). Peers chosen for electrical and industrial-technology overlap at similar margins and scale. Rejected: Schneider Electric, ABB and Siemens (no 10-K, so outside the blind run's tools), Honeywell (conglomerate in mid-breakup), Dana (the counterparty, not a comparable for the continuing business).

## statements/

etn-stated-positions.md: verbatim passages from the filings above, grouped by signal.

## Could not be obtained

- A regression beta: the permitted tools give no price series.
- Analyst consensus: no permitted source.
- Dana's own 2026-06-11 release and presentation: filed by Dana, not fetched by the tool.
- The 2026-01-26 8-K (Item 7.01, Mobility spin intent): the tool's material-item list skips 7.01-only filings. Its content is restated in the 2025 10-K.
- 2022 year-end balance sheet: not in either 10-K; 2022 cash, debt and invested capital are estimates (see `inputs.yaml`).
