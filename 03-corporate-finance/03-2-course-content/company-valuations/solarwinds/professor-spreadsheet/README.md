---
title: "SolarWinds (SWI) — Valuation in the professor's spreadsheet"
status: active
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

# SolarWinds (SWI) — Valuation in the professor's spreadsheet

From 2026-11-03 the final report's discounted cash flow (section 9 of [../final-report.md](../final-report.md)) comes from Prof. Damodaran's `fcffsimpleginzu.xlsx`, the course's FCFF valuation spreadsheet, February 2026 edition. The repo's own model (`.claude/skills/value-company/tools/model.py`, output in [../model-output.md](../model-output.md)) is kept as the cross-check; it is not the deliverable's number any more.

## What the sheet is

`fcffsimpleginzu.xlsx` values a company from a handful of inputs (revenue, operating income, growth and margin targets, cost of capital, shares, debt and cash) and the professor's default assumptions for the stable period: cost of capital fades to risk-free plus the mature-market premium over years 6–10, growth after year 10 equals the risk-free rate, return on new capital equals the cost of capital, and reinvestment equals the change in revenue over an industry sales-to-capital ratio. Everything in the "Valuation output" sheet follows from those inputs.

- Download: <https://pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx>
- The filled copy in Google Sheets: <https://docs.google.com/spreadsheets/d/18RyIfGFiUzE5I04PMv2s-q_DOStTX9J6N0QHt-7kT9U/edit>
- The filled copy in this folder: [solarwinds-fcffsimpleginzu-2025-02-05.xlsx](solarwinds-fcffsimpleginzu-2025-02-05.xlsx) (Git LFS, like every other `.xlsx` in the repo)

The sheet needs **iterative calculation on** (the cost of capital, market value of equity and value per share refer to each other). In Google Sheets: File → Settings → Calculation → Iterative calculation: On, 50 iterations, threshold 0.0001. In Excel: File → Options → Formulas → Enable iterative calculation.

## Files

| File | What it is |
|---|---|
| [inputs.md](inputs.md) | Every cell entered, its value, and why |
| [results.md](results.md) | The sheet's base run, the sensitivity runs, and a comparison with the repo model |
| [exhibit-values.yaml](exhibit-values.yaml) | The sheet's per-share values that [../report-exhibits/make-exhibits.py](../report-exhibits/make-exhibits.py) reads for the DCF bars in exhibit 4 |
| `solarwinds-fcffsimpleginzu-2025-02-05.xlsx` | The filled workbook |

## How to re-run

1. Open the workbook (or download a fresh `fcffsimpleginzu.xlsx` from the link above) and turn iterative calculation on.
2. Enter the inputs table from [inputs.md](inputs.md) on the "Input sheet", and on the "Cost of capital worksheet" set B11 to "I will input" and B12 to 0.1067. Leave every default assumption (B45–B72) at "No".
3. Read the "Valuation output" sheet: value per share is in **B33** (expected $15.32). Value of equity is B29, the options claim B30, shares B32.
4. For the sensitivity runs, change one input at a time as [results.md](results.md) lists, read B33, then restore the input.
5. If a number changes, update [results.md](results.md) and [exhibit-values.yaml](exhibit-values.yaml), re-run `make-exhibits.py`, and carry the change into the final report's section 9 and the README change log.
