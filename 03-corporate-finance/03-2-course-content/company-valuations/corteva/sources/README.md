---
title: "Corteva (CTVA) — Source manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Source manifest

All fetched 2026-11-03 under the blind rules (cutoff 2026-06-30). Publication dates are in `published.yaml`.

| File | What it is | Origin |
|---|---|---|
| filings/ctva-10-k-2026-02-12.md | FY2025 10-K | EDGAR via fetch-filings.py |
| filings/ctva-10-k-2025-02-14.md | FY2024 10-K (2022–2023 history) | EDGAR via fetch-filings.py |
| filings/ctva-10-q-2026-05-06.md | Q1 2026 10-Q | EDGAR via fetch-filings.py |
| filings/ctva-def14a-2026-03-19.md | 2026 proxy | EDGAR via fetch-filings.py |
| filings/ctva-8-k-2025-10-01-items-202-901.md | Separation announcement | EDGAR via fetch-filings.py |
| filings/ctva-8-k-2026-04-14-items-502-701-901.md | Leadership of both companies; Kissam letter | EDGAR via fetch-filings.py |
| filings/ctva-8-k-2026-06-29-items-502-701-901.md | Post-separation boards; Vylor name | EDGAR via fetch-filings.py |
| filings/ctva-8-k-2025-08-26-items-502-701-901.md | Chief legal officer change | EDGAR via fetch-filings.py |
| filings/ctva-8-k-2025-11-04 / 2026-02-03 / 2026-05-05 (items 202-901) | Earnings releases Q3 2025, Q4 2025, Q1 2026 | EDGAR via fetch-filings.py; exhibits appended separately (tool regex miss) |
| filings/index.md | Every filing in the three years to the cutoff | fetch-filings.py |
| peer-filings/peer-facts-2026-06-30.md | Peer XBRL facts and closes | fetch-peer-facts.py --date 2026-06-30 |
| market-data/*.json | Rates, ERP, spreads, country risk, betas | refresh-market-data.py --as-of 2026-06-30 |
| statements/stated-side-2026-06-29.md | Quoted passages for the stated side | compiled from the filings above |

## Peers

Chosen: FMC (crop protection, closest US-listed rival), American Vanguard (crop protection), Mosaic and CF Industries (crop inputs: fertilizer), Scotts Miracle-Gro (lawn and garden inputs). Rejected or unavailable: Bayer, Syngenta, BASF, KWS, UPL (no 10-K filings); Nutrien (fetch-peer-facts.py crashed on its 40-F data: `fiscal_year_end` returned None, line 164); ADM (grain processor, not an input maker).

## Not obtained

- Vylor, Inc. Form 10 (filed late June 2026 under Vylor's own SEC number). It would show the post-spin capital structures, but the blind tools fetch only CTVA's filings.
- The 8-K/A of June 2026, the 5.07 voting-results 8-Ks, and three Schedule 13G filings from April–May 2026 are on the index but were not fetched by the tool.
- Agency credit ratings: not disclosed in the filings.
- Regression beta: no price series under the blind rules.
- 2022 year-end balance sheet (debt, invested capital): not in the two 10-Ks fetched.
