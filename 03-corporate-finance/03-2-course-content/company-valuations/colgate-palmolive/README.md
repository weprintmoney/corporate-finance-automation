---
title: "Colgate-Palmolive (CL) — Valuation Run"
status: draft
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL)

A `/value-company` run for the course final project. Colgate-Palmolive is a US-listed consumer products company with two segments: Oral, Personal and Home Care (77% of 2025 sales) and Hill's Pet Nutrition (23%). About two-thirds of sales come from outside the United States.

| Item | Value |
|---|---|
| Type | public |
| Base year | FY2025 (10-K filed 2026-02-23) |
| Trailing twelve months | to 2026-09-30 (10-Q filed 2026-10-30) |
| Analysis date | 2026-11-20 |
| Currency | USD |

## Where the run stands

Done: sources compiled; ledger filled and validated; model run; lessons 1–36 and walkthrough steps 1–36 written, with the walkthrough summary and glossary; the professor's `capstru.xlsx`, `dividends.xlsx` and `fcffsimpleginzu.xlsx` filled in Google Sheets (`professor-spreadsheet/results.md`); debt design numbers from `macrodur.xlsx` (`professor-spreadsheet/macro-sensitivity-output.md`); valuation history, sensitivities and peer pricing in `valuation-cross-checks-output.md`. Not started: the valuation report and the review pass.

Where the valuation landed: $61.83 a share in the base case against a price of $98.71; $50.90 on all the workbook's defaults and $79.74 with growth in perpetuity at 4.82%; about $89 on the multiples of six household and personal care companies from Capital IQ's default list. The debt recommendation of 20% stands, with the cash paid out as dividends, not buybacks, while the price is above the estimated value (`lesson-22.md`, `lesson-34.md`).

The report's valuation runs in the professor's `fcffsimpleginzu.xlsx`. Section 6 of `model-output.md` is the repo cross-check on a three-year consensus forecast, not the valuation.

## Decisions made (2026-11-21)

| Decision | Choice | Alternative quoted beside it |
|---|---|---|
| Base operating income | 4,225: reported 3,306 plus the 919 non-cash write-down. Restructuring and litigation charges stay in; 2,211 of write-downs since 2021 is added back to invested capital | 3,306 as reported |
| Cost of debt | S&P's A+ rating, 5.74% | Synthetic AAA from coverage, 5.44% |
| Equity risk premium date | Damodaran's start-of-November implied premium, 3.61% | A premium recomputed after the 8.8% fall in the S&P 500 |
| Beta for Hill's | Food Processing, 0.47 | No pet food industry in the dataset |
| Beta | Industry average, 0.73 levered: the course's method and an average over 188 companies. Confidence is low; the honest range is 0.41 to 0.80 | Median of six large household peers, about 0.41: cost of capital 6.77%, value $68.32 if it fades to the mature rate and about $91.88 if it lasts forever |
| Stable return on capital | 20% | The spreadsheet default: return equals cost of capital |
| Growth in perpetuity | 3%: consensus revenue growth is 2.3% to 3.5% and sales grew 3.3% a year from 2016 to 2025 | The spreadsheet default, the 4.82% riskfree rate |
| Forecast margins | 20.5% rising to 21.3%: consensus less about 0.7 points for restructuring and similar charges, which consensus leaves out and operating income here keeps in | Consensus as published, 21.2% rising to 22% |
| Sales to capital | 2.2: Colgate's own ratio and the US household products average | The spreadsheet's global default, 1.79 |
| Valuation headline | Base case with both stable-period overrides, quoted beside the all-defaults result | All sheet defaults only |
| Bankruptcy cost for the adjusted present value (lesson 21) | 15% of firm value, range 10% to 25%; added to the ledger as `debt.bankruptcy_cost` | 25%, the lecture's Disney figure; the optimum moves from 30% to 26% |
| Recommended debt ratio (lesson 19) | 20%: holds a synthetic A− rating with operating income 20% lower | 30%, the unconstrained optimum in `capstru.xlsx` and the model; 25% as a middle course |
| How the borrowed cash is paid out (lesson 34) | Dividends, regular or special, while the price is above the estimated value. A judgment that depends on the valuation being right | Buybacks, which become the better route only at or below value |
| Comparison companies (lesson 35) | Capital IQ's default list of ten, priced on the six household and personal care companies; the ledger's `peers` block stays empty | A peer set built for Colgate, weighted for Hill's, with `fetch-peer-facts.py` |

## Open questions

| Question | Where raised |
|---|---|
| US sales are priced at the 3.61% mature premium with nothing added, while Damodaran's tables give the US (Aa1) 0.22% over the mature market. The weighted premium is 5.38% as built, or 5.45% or 5.23% on the other readings | `lesson-07.md` |
| Moody's rating is not sourced | `sources/README.md` |
| `capstru.xlsx` rates the firm A− at 30% because it keeps existing debt at its present interest; the model reprices all debt and gets BBB. The report should say which it relies on | `lesson-18.md`, `professor-spreadsheet/results.md` |
| Currencies behind the 3,942 of foreign currency debt designated as a net investment hedge, and the duration of the notes, are not in the files | `lesson-23.md` |
| Ex-dividend price test not run (no daily prices); peer dividend data waits for the peer set | `lesson-25.md`, `lesson-28.md` |
| Minority interests are subtracted at book value, 352. On the earnings they receive (129 in 2025) an estimate is 2,117, which would put the base case at 59.62 | `lesson-33.md` |
| The pension and retiree-benefit shortfall of 1,283 is not subtracted in the valuation; after tax it is worth 1.21 a share | `lesson-33.md` |
| Kimberly-Clark's next-twelve-months figures on the Capital IQ page are 90% above its trailing revenue; the cause is not in the files and its forward multiples are left out | `lesson-35.md` |

## File map

| File | What it is |
|---|---|
| `inputs.yaml` | The ledger: every input with its source and date |
| `model-output.md` | Generated by `tools/model.py`; never hand-edited |
| `sources/` | Filings, Capital IQ pulls, market data; manifest in `sources/README.md` |
| `lesson-01.md` … `lesson-12.md` | Module 1 question logs with answers (cost of capital) |
| `lesson-13.md` … `lesson-28.md` | Question logs for investment returns, financing mix and dividends |
| `lesson-29.md` … `lesson-36.md` | Question logs for valuation, value of control, relative valuation and the closing narrative |
| `walkthrough.md` | Plain-language trail, steps 1 to 36, with the ten-sentence summary and the glossary |
| `valuation-cross-checks.py`, `valuation-cross-checks-output.md` | Arithmetic quoted in lessons 29–36 (market value and cash flow history, growth, a replication of the valuation workbook with sensitivities, buybacks above value, peer multiples and regressions); generated, not hand-edited |
| `modules-2-4-cross-checks.py`, `modules-2-4-cross-checks-output.md` | Arithmetic quoted in lessons 13–28 (divisional rates, one-point debt schedule, stress tests, APV at other bankruptcy costs, FCFE by year, sector comparisons); generated, not hand-edited |
| `module-1-cross-checks.py`, `module-1-cross-checks-output.md` | Alternatives quoted in lessons 1–12 (regression diagnostics, cost of capital under other choices); generated, not hand-edited |
| `professor-spreadsheet/originals/` | The professor's spreadsheets as downloaded 2026-11-21: `fcffsimpleginzu.xlsx`, `macrodur.xls`, `apv.xls`, `divfund.xls` |
| `final-report.md` | The report for submission: verdict, nine sections, judgment-call tables |
| `final-report.docx` | The Word version, built from `final-report.md` by `report-exhibits/build-report-docx.js` |
| `report-exhibits/` | The four charts and the script that draws them |
| `peer-payout-check.py`, `peer-payout-check-output.md` | Five-year dividends and buybacks against net income for Colgate and six household peers |

## Corrections log

None yet.
