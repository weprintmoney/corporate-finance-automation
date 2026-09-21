---
title: "Damodaran Country Risk Premium — United States"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-09-07
---

# Damodaran Country Risk Premium — United States

Extracted from Damodaran's live current dataset (`https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xlsx`, sheet "ERPs by country", dated by Damodaran as updated 2026-01-01, sovereign ratings refreshed 2026-02-16), fetched 2026-09-07 — because this repo's own `03-3-supplemental-data/country-risk.json` is an **empty stub** (`"countries": {}`, its CI refresh never actually populated it — see the parent `sources/README.md`).

SolarWinds is US-domiciled (Austin, TX), so the United States row is the relevant one for the base-case cost of equity. Country risk only becomes relevant to the SWI analysis when a lesson asks about the geographic-revenue mix (SWI's non-US revenue, ~31% of total per `swi-10k-fy2024.md`) or an explicit Eurozone/ECB comparison.

| Metric | Value |
|---|---|
| Mature-market (implied, S&P 500) equity risk premium | 4.23% |
| US Moody's sovereign rating | Aa1 |
| US total equity risk premium | 4.46% |
| US country risk premium (component of the above) | 0.23% |

## How to refresh

```bash
curl -o ctryprem.xlsx "https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xlsx"
```

Damodaran updates this a few times a year (ratings changes trigger updates outside the main January refresh) — the URL is his evergreen "current" file, no year suffix needed.
