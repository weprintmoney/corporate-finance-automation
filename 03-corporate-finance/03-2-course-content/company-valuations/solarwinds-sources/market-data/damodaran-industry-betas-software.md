---
title: "Damodaran Industry Betas — Software Sector"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-09-07
---

# Damodaran Industry Betas — Software Sector

Extracted from Damodaran's live current dataset (`https://pages.stern.nyu.edu/~adamodar/pc/datasets/betas.xls`, sheet "Industry Averages", dated by Damodaran as updated 2026-01-05), fetched 2026-09-07 — because this repo's own `03-3-supplemental-data/industry-betas.json` is an **empty stub** (`"industries": {}`, its CI refresh never actually populated it — see the parent `solarwinds-sources/README.md`).

SolarWinds' relevant classification is **Software (System & Application)**.

| Industry | # Firms | Levered Beta | D/E Ratio | Effective Tax Rate | Unlevered Beta | Cash/Firm Value | Unlevered Beta (cash-corrected) |
|---|---|---|---|---|---|---|---|
| Software (System & Application) | 309 | 1.2766 | 5.58% | 5.51% | 1.2254 | 1.83% | 1.2482 |
| Software (Entertainment) | 77 | 1.0283 | 2.04% | 5.29% | 1.0128 | 0.78% | 1.0207 |
| Software (Internet) | 29 | 1.6887 | 12.30% | 3.05% | 1.5461 | 2.80% | 1.5905 |

## Using this for SWI's cost of equity

To re-lever for SWI's own FY2024 capital structure (rather than using the industry-average D/E), take the **Unlevered Beta (cash-corrected)** of 1.2482 and re-lever with SWI's own D/E and marginal tax rate:

```
Levered Beta = Unlevered Beta × [1 + (1 − tax rate) × (D/E)]
```

SWI's FY2024 D/E and effective tax rate are derivable from `../sec-filings/swi-multi-year-financials.md` and `../sec-filings/swi-10k-fy2024.md`.

## How to refresh

```bash
curl -o betas.xls "https://pages.stern.nyu.edu/~adamodar/pc/datasets/betas.xls"
```

Damodaran refreshes this dataset annually in January — re-check `pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html` each January for the year's file, since the filename itself doesn't change but the "Date updated" cell inside does.
