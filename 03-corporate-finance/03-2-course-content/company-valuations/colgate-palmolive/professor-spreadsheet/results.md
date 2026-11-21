---
title: "Colgate-Palmolive (CL) — results from the professor's spreadsheets"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Results from the professor's spreadsheets, analysis date 2026-11-20

Read on 2026-11-21 from the filled workbooks, which are `.xlsx` files calculated in Google Sheets. Inputs and their sources are in [inputs.md](inputs.md). Amounts in $M.

## capstru.xlsx — optimal debt ratio (cost of capital approach)

| Item | Current | Optimal | Change |
|---|---|---|---|
| Debt to capital | 9.34% | 30.00% | +20.66 points |
| Total debt | 8,084 | 25,965 | +17,881 |
| Beta | 0.73 | 0.90 | +0.17 |
| Cost of equity | 8.76% | 9.65% | +0.89 points |
| Rating | A1/A+ (actual) | A3/A− (synthetic) | |
| After-tax cost of debt | 4.31% | 4.45% | +0.14 points |
| Cost of capital | 8.34% | 8.09% | −0.25 points |
| Enterprise value | 85,154 | 90,960 | +5,806 |
| Value per share | $98.71 | $106.01 | +$7.30 |
| Interest coverage | 15.82 | 3.18 | |

The current column agrees with `../model-output.md` section 1 (cost of capital 8.34%, unlevered beta 0.6796).

| Debt ratio | Debt | Beta | Cost of equity | Interest | Interest coverage | Rating | Pre-tax cost of debt | Cost of capital |
|---|---|---|---|---|---|---|---|---|
| 0% | 0 | 0.68 | 8.48% | 0 | n/a | Aaa/AAA | 5.44% | 8.48% |
| 10% | 8,655 | 0.74 | 8.78% | 298 | 14.18 | Aaa/AAA | 5.44% | 8.31% |
| 20% | 17,310 | 0.81 | 9.16% | 803 | 5.26 | A2/A | 5.82% | 8.20% |
| 30% | 25,965 | 0.90 | 9.65% | 1,327 | 3.18 | A3/A− | 5.93% | 8.09% |
| 40% | 34,619 | 1.02 | 10.30% | 3,953 | 1.07 | Caa/CCC | 13.89% | 10.35% |
| 50% | 43,274 | 1.27 | 11.63% | 7,671 | 0.55 | C2/C | 21.04% | 14.89% |

The sheet steps in tens. The repo model, on a one-point grid, puts the lowest cost of capital between 26% and 30% and rates the firm BBB at 30%, because it reprices all debt at the new rate. The workbook was run with "existing debt is refinanced" set to No, so it keeps current debt at its present interest; that is why its interest at 30% is 1,327 and its rating is A−.

## dividends.xlsx — cash returned against free cash flow to equity, 2018–2025

| Item | Eight-year total | Yearly average |
|---|---|---|
| Net income | 18,734 | 2,342 |
| Free cash flow to equity, before debt | 17,868 | 2,234 |
| Net debt issued | 951 | |
| Free cash flow to equity, at actual debt | 18,819 | |
| Dividends | 13,590 | 1,699 |
| Buybacks | 10,621 | 1,328 |
| Dividends plus buybacks | 24,211 | 3,026 |
| Dividend payout ratio | 72.54% | 73.95% |
| Cash returned as % of net income | 129.24% | |

| Year | Payout ratio | Cash paid as % of FCFE | Return on stock | Required return | Jensen's alpha |
|---|---|---|---|---|---|
| 2025 | 85.51% | 111.84% | −10.98% | 14.10% | −25.08% |
| 2024 | 61.92% | 122.29% | 16.57% | 19.60% | −3.03% |
| 2023 | 76.04% | 124.33% | 3.78% | 20.49% | −16.71% |
| 2022 | 94.73% | 119.10% | −5.44% | −12.65% | 7.21% |
| 2021 | 77.52% | 124.49% | 2.08% | 20.85% | −18.77% |

The sheet's return on equity (3,948% in 2025, 1,363% in 2024) is not usable: book equity was 54 and 212. Return on invested capital carries the project-quality argument instead.

The 2018–2020 rows of the yearly table, the averages of the performance ratios and the Forecasted Dividends & FCFE sheet were not read.

### Cash returned, net of option proceeds

Free cash flow to equity leaves out cash received when employees exercise options. Proceeds from option exercises (`../sources/filings/cl-multi-year-financials-fy2014-fy2025.tsv`, ProceedsFromStockOptionsExercised) were 329, 498, 874, 424, 418, 380, 638 and 101 for 2018 to 2025.

| Period | Cash returned less FCFE | Option proceeds | Gap net of option proceeds |
|---|---|---|---|
| 2018–2025 | 5,392 | 3,662 | 1,730 |
| 2021–2025 | 2,598 | 1,961 | 637 |

Buybacks net of option proceeds were 6,959 over 2018–2025 against 10,621 gross. The eight-year net gap is 7% of the 24,211 returned: Colgate returned about what it generated.

## fcffsimpleginzu.xlsx — valuation

| Case | Value of operating assets | Present value of terminal value | Value per share | Price as % of value |
|---|---|---|---|---|
| Base case: stable return on capital 20%, growth in perpetuity 3%, stable cost of capital 8.43% | 56,717 | 32,940 | $61.83 | 159.64% |
| Growth in perpetuity at the sheet default, 4.82% | 71,007 | not read | $79.74 | 123.78% |
| Stable return equal to the cost of capital, growth 4.82%, stable cost of capital 8.43% | 50,324 | not read | $53.82 | 183.40% |
| All sheet defaults: return equals cost of capital, growth 4.82%, stable cost of capital 9.05% | 47,989 | 24,519 | $50.90 | 193.9% (98.71 ÷ 50.90) |
| Base case with cost of capital 7.84% (beta 0.63) | not read | not read | $63.82 | 154.66% |
| Base case with cost of capital 8.67% (beta 0.80) | not read | not read | $60.56 | 163.00% |
| Base case with cost of capital 6.77% for years 1–5 (peer-median beta 0.41), stable rate 8.43% | 61,892 | 36,481 | $68.32 (computed from the operating-asset cell) | 144.5% (98.71 ÷ 68.32) |
| Base case with 6.77% as the stable cost of capital as well | 80,690 | not read | about $91.88 (computed from the operating-asset cell) | 107.4% (98.71 ÷ 91.88) |

Base case detail:

| Item | Value |
|---|---|
| Present value of ten years of cash flow | 23,776 |
| Terminal cash flow | 3,995 |
| Terminal value | 73,570 |
| Value of operating assets | 56,717 |
| − Debt | 8,282 |
| − Minority interests | 352 |
| + Cash | 1,612 |
| + Non-operating assets | 82 |
| Value of equity | 49,777 |
| − Value of options | 439 |
| Value of equity in common stock | 49,338 |
| Shares | 797.9 |
| Value per share | $61.83 |

The workbook is left in the base-case state. The sheet's return on invested capital is 42.70% in the base year.

## Evidence behind the valuation inputs

| Input | Evidence |
|---|---|
| Option maturity 4 years | FY2025 10-K stock option table: weighted-average remaining contractual life 4 years; options have an eight-year term |
| Effective tax rate 23.5% | FY2025 10-K MD&A: 26.1% reported, 23.1% excluding the write-down and other items. Q3 2026 10-Q: 23.8% for the first nine months of 2026 |
| Operating leases 566 at 2026-09-30 | The 10-Q gives no lease liability, so the year-end figure is carried forward |
| Stable return on capital 20% | A judgment. Benchmarks: the sheet's base-year return 42.70%; US household products after-tax return on capital 34.42% (Damodaran, January 2026) |
| Growth in perpetuity 3% | Consensus revenue growth 2.3% to 3.5% (Capital IQ); sales grew 3.3% a year from 2016 to 2025 |
| Margins 20.5% rising to 21.3% | Consensus margins (21.2% rising to 22%) leave out restructuring and similar charges; see the table below |

Charges the company leaves out of its adjusted operating profit, other than write-downs:

| Period | Reported operating profit plus write-downs | Company-adjusted operating profit | Charges left out |
|---|---|---|---|
| 2023 | 3,984 | 4,036 | 52 |
| 2024 | 4,268 | 4,353 | 85 |
| 2025 | 4,225 | 4,347 | 122 |
| First nine months of 2026 | 3,069 | 3,396 | 327 |

Sources: FY2025 and FY2024 10-K MD&A; Q3 2026 10-Q MD&A. The total is 586 over 3.75 years, about 156 a year, or roughly 0.7% of sales. The Strategic Growth and Productivity Program (approved July 2025, expanded April 2026) is estimated at 350 to 550 in total, of which 346 has been booked (10-Q note).
