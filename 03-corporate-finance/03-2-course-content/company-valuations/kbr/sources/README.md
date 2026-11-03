---
title: "KBR, Inc. — Sources manifest"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# Sources manifest (blind run, cutoff 2026-06-30)

Fetched 2026-11-03. Publication dates are in `published.yaml`; nothing published after 2026-06-30 is here.

| File | What it is | Origin | Published |
|---|---|---|---|
| filings/kbr-10-k-2026-02-26.md | 10-K FY2025 (base year) | EDGAR via tools/fetch-filings.py | 2026-02-26 |
| filings/kbr-10-k-2025-02-25.md | 10-K FY2024 (2022 history) | EDGAR via tools/fetch-filings.py | 2025-02-25 |
| filings/kbr-10-q-2026-05-05.md | 10-Q Q1 FY2026 (shares, debt, spin financing plan) | EDGAR via tools/fetch-filings.py | 2026-05-05 |
| filings/kbr-def14a-2026-03-30.md | 2026 proxy | EDGAR via tools/fetch-filings.py | 2026-03-30 |
| filings/kbr-8-k-*.md (7 files) | 8-Ks 2025-07-09 to 2026-05-05 with EX-99 exhibits (spin announcement, CFO change, four earnings releases) | EDGAR; exhibits re-fetched with a scratchpad copy of fetch-filings.py whose exhibit regex also matches `exhibit99-…` names (the tool's regex missed them) | per file |
| filings/index.md | Every EDGAR filing for the CIK to the cutoff, by month | tools/fetch-filings.py | 2026-06-30 |
| market-data/market-rates-2026-06-01.json | Damodaran June 2026 ERP workbook figures; FRED closes 2026-06-30 | scripts/refresh-market-data.py --as-of 2026-06-30 | 2026-06-30 |
| market-data/ratings-spreads-2026-01-01.json | Damodaran coverage-to-rating tables, January 2026 | same | 2026-01-01 |
| market-data/country-risk-2026-01-01.json | Damodaran country risk premiums, January 2026 | same | 2026-01-01 |
| market-data/industry-betas-2026-01-05.json | Damodaran US industry betas, January 2026 | same | 2026-01-05 |
| market-data/rates-2026-06-30.md, country-exposure-2026-06-30.md, bottom-up-beta-2026-06-30.md | Derived notes | scripts/build-market-sources.py | 2026-06-30 |
| peer-filings/peer-facts-2026-06-30.md | KBR and seven peers' latest 10-K XBRL facts and 2026-06-30 closes | tools/fetch-peer-facts.py --date 2026-06-30 | 2026-06-30 |
| statements/kbr-stated-positions.md | Quoted stated positions by signal (S1–S22) | from the filings above | 2026-05-05 |

## Peers

LDOS, SAIC, CACI, BAH (government technical services, for MTS); PSN, J, ACM (engineering and technical services, for STS). Rejected: Fluor and Technip Energies (EPC-construction risk KBR no longer takes), Honeywell UOP (inside a conglomerate). Leidos' dividends and SAIC's net income were not XBRL-tagged; left null.

## Not obtained

- 8-K 2026-05-18 (annual-meeting vote results) and the 13G filings of 2026-04 and 2026-05: not fetched by the tool; their content is unknown to this run.
- FY2023 10-K: not fetched, so 2022 balance-sheet debt and invested capital are missing from `company.history`.
- Agency credit ratings: no filing names one.
- Outstanding balance of receivables sold to MUFG: not disclosed.
