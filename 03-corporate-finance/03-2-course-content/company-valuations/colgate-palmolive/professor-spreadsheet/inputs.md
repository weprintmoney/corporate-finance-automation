---
title: "Colgate-Palmolive (CL) — inputs for the professor's spreadsheets"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Inputs for the professor's spreadsheets, analysis date 2026-11-20

Amounts in $M. Each value comes from [../inputs.yaml](../inputs.yaml) unless noted. Percent cells in Google Sheets must be entered as `=0.0574`; typing `5.74%` leaves text and breaks the circular formulas.

## capstru.xlsx — Inputs sheet

| Cell | Label | Value | Why |
|---|---|---|---|
| B7 / B8 / B9 | Company / country / date | Colgate-Palmolive / United States / 2026-11-20 | |
| B11 | EBITDA | 4,855 | Reported operating profit 3,306 plus the 919 goodwill and intangible write-down (4,225), plus depreciation and amortization 630. Restructuring and litigation charges stay in: Colgate books them most years. |
| B12 / B13 / B14 | D&A / capital spending / interest expense | 630 / 564 / 267 | FY2025 |
| B15 | Marginal tax rate | leave (25%, the sheet's US lookup) | |
| B16 / B17 | Current rating / pre-tax cost of debt | A1/A+ / 5.74% | S&P A+; 10-year Treasury 5.04% plus the 0.70% spread |
| B19 / B20 | Shares / price | 794.9 / 98.71 | |
| B21 | Beta | 0.7321 | Bottom-up levered beta; the sheet unlevers it to 0.6796 |
| B22 | Cash and marketable securities | 1,395 | |
| B23 | Book value of debt | 8,554 | Carrying value 7,988 plus operating leases 566 |
| B24 / B25 / B26 | Market value of debt supplied? / value / estimate it? | Yes / 8,084 / No | Fair value 7,518 from the 10-K plus leases 566 |
| B28 | Operating leases? | No | Leases are already inside B23 and B25 |
| B30, B34, B42–B44 | Interest limits, bankruptcy cost, table, refinancing | defaults (No, No, 1, No, No) | |
| B37 / B38 / B39 | Riskfree / risk premium / country default spread | 4.82% / 5.38% / 0.22% | B38 and B39 are formulas in the original; overwritten with the ledger's weighted premium and the US spread |

Workbook: `colgate-capstru-optimal-debt.xlsx`, calculated in Google Sheets with iterative calculation on (200 iterations, threshold 0.00001). Results in [results.md](results.md).

## dividends.xlsx — Inputs sheet

Workbook: `colgate-dividends-2026-11-20.xlsx`. Results in [results.md](results.md).

Eight years, 2025 first. Debt issuance tags are incomplete before 2018, so the history stops there.

| Year | Net income | D&A plus non-cash impairments | Capex plus acquisitions | Change in non-cash working capital | Net debt issued | Dividends | Buybacks | Book equity | Stock return |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 2,132 | 1,549 | 857 | −344 | −456 | 1,823 | 1,210 | 54 | −10.98% |
| 2024 | 2,889 | 605 | 561 | −360 | −408 | 1,789 | 1,739 | 212 | 16.57% |
| 2023 | 2,300 | 567 | 705 | −466 | −314 | 1,749 | 1,128 | 609 | 3.78% |
| 2022 | 1,785 | 1,266 | 1,505 | 675 | 1,647 | 1,691 | 1,308 | 401 | −5.44% |
| 2021 | 2,166 | 1,127 | 567 | 142 | −175 | 1,679 | 1,320 | 609 | 2.08% |
| 2020 | 2,695 | 539 | 763 | −407 | −597 | 1,654 | 1,476 | 743 | 27.17% |
| 2019 | 2,367 | 519 | 2,046 | 22 | 1,433 | 1,614 | 1,202 | 117 | 18.60% |
| 2018 | 2,400 | 511 | 1,164 | 119 | −179 | 1,591 | 1,238 | −102 | −19.19% |

Sources: `../sources/filings/cl-multi-year-financials-fy2014-fy2025.tsv` (net income, D&A, impairments 571 / 721 / 919 in 2021 / 2022 / 2025, capital spending, acquisitions, receivables, inventories and payables changes, debt proceeds and repayments, dividends, buybacks, equity); the FY2025 10-K cash flow statement for the 2025 payables change (251). Stock returns are year-end to year-end dividend-adjusted closes from Yahoo Finance's chart endpoint, read 2026-11-21 (2017 to 2025: 60.909, 49.220, 58.373, 74.232, 75.777, 71.654, 74.365, 86.684, 77.169). Capital IQ shows net debt issued of −100 for 2021 against −175 here.

| Cell | Label | Value |
|---|---|---|
| E2 / E3 / E4 | Years / current debt ratio / change it? | 8 / 9.34% / No |
| D37 | Beta | 0.7321 |
| D41:E48 | T-bill and market return | point at rows 99 down to 92 of the Historical sheet (2025 to 2018) |
| E55 / E57 / E58 | Growth in revenue, capex, depreciation | 3.57% (consensus revenue, 2025 to 2028) |
| E56 | Growth in net income | 5.45% (analysts' long-term EPS growth) |
| E59 | Working capital as % of revenue | 6.01% (household products average) |
| E60 / E61 / E62 / E63 / E64 | Revenue / net income / capex / depreciation / dividends | 20,382 / 3,051 (2,132 plus the 919 impairment) / 564 / 630 / 1,823 |
| D66 | Growth in dividends | 2% (dividends paid grew 2.1% a year from 2021 to 2025) |

## fcffsimpleginzu.xlsx — Input sheet

Workbook: `colgate-fcffsimpleginzu-2026-11-20.xlsx`, iterative calculation on. Results in [results.md](results.md).

| Cell | Label | Value | Why |
|---|---|---|---|
| B3 / B4 / B7 | Date / company / country | 2026-11-20 / Colgate-Palmolive / United States | |
| B8 / B9 | Industry (US / global) | Household Products | 77% of sales |
| B11 / C11 / D11 | Revenues: trailing / last 10-K / years since | 21,285 / 20,382 / 0.75 | 20,382 + 16,055 − 15,152 |
| B12 / C12 | Operating income | 4,080 / 4,225 | Reported (3,161 trailing; 3,306 FY2025) plus the 919 write-down booked in Q4 2025 |
| B13 / C13 | Interest expense | 250 / 267 | 267 + 186 − 203 |
| B14 / C14 | Book equity, with noncontrolling interests | 640 / 365 | |
| B15 / C15 | Book debt | 8,282 / 8,554 | Debt 7,716 at 2026-09-30 plus operating leases, assumed unchanged at 566 |
| B16 / B17 | Capitalize R&D? / operating leases? | No / No | Leases are inside B15 |
| B18 / C18 | Cash and marketable securities | 1,612 / 1,395 | |
| B19 / C19 | Cross holdings | 82 / 82 | Equity-method investments at 2025-12-31 |
| B20 / C20 | Minority interests | 352 / 311 | |
| B21 / B22 | Shares / price | 797.9 / 98.71 | 794.9 plus 2.988 of restricted and performance units |
| B23 / B24 | Effective / marginal tax rate | 23.5% / 25% | 10-K: 23.1% for 2025 excluding the write-down; 10-Q: 23.8% for the first nine months of 2026 |
| B26 | Revenue growth next year | 2.25% | Consensus next-twelve-months revenue 21,764 against 21,285 |
| B27 | Operating margin next year | 20.5% | Consensus 21.2% less about 0.7 points for restructuring and similar charges, which consensus leaves out and this valuation keeps in |
| B28 | Growth, years 2–5 | 3.1% | Consensus revenue grows 3.07% a year from 2027 to 2030 (21,888 to 23,969) |
| B29 / B30 | Target margin / year of convergence | 21.3% / 5 | Consensus 2028 margin 21.83%, rounded to 22%, less the same 0.7 points |
| B31 / B32 | Sales to capital | 2.2 | Colgate's own ratio (20,382 ÷ 9,169 = 2.22) and the US household products average (2.21). The sheet default is the global average, 1.79 |
| B34 | Riskfree rate | 4.82% | |
| B37–B41 | Options: number / strike / maturity / standard deviation | Yes / 12.619 / 79 / 4 / 19.08% | Maturity is an assumption; standard deviation from 60 monthly returns |
| B45 / B46 | Override stable cost of capital | Yes / 8.43% | Riskfree 4.82% plus the 3.61% mature premium. The sheet's own default would use its January premium of 4.23% and give 9.05%, above today's 8.34% |
| B48 / B49 | Override stable return on capital | Yes / 20% | Judgment: under half of today's 42%. The default (return equals cost of capital) is quoted beside it |
| B67 / B68 | Override growth in perpetuity | Yes / 3% | The default is the riskfree rate, 4.82%. Consensus revenue growth is 2.3% to 3.5%, and sales grew 3.3% a year from 2016 to 2025. With the stable return above the cost of capital, growth adds value, so the default would overstate it |
| Other defaults | Failure, tax convergence, losses | No | |
| Cost of capital worksheet B11 / B12 | Approach / cost of capital | I will input / 8.34% | From the ledger, so the three spreadsheets agree |
