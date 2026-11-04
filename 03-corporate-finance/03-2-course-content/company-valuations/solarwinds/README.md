---
title: "SolarWinds (SWI) — Course Project Overview"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-11-03
---

# SolarWinds (SWI) — Course Project Overview

The full Applied Corporate Finance project for SolarWinds Corporation, built with `/value-company` (scope `full`, all 36 lessons). Rerun from scratch on 2026-10-25; it replaces the September–October 2026 hand-built project, whose files are in git history before this rerun's PR.

## Company context

SolarWinds sells IT monitoring and observability software. Silver Lake and Thoma Bravo took it private in February 2016 and re-listed it on the NYSE in October 2018. In December 2020 the SUNBURST supply-chain attack, carried in its Orion software, became public. In July 2021 it spun off its managed-service-provider business as N-able. It paid special dividends of $1.50 a share (2021) and $1.00 a share (April 2024). On 2025-02-07 it agreed to be bought by Turn/River Capital for $18.50 a share in cash. Silver Lake (36.56%) and Thoma Bravo (29.79%) approved the deal by written consent, so no stockholder vote was held. It closed on 2025-04-16. FY2024 is the last full year of public filings.

**Type:** delisted. **Base year:** FY2024. **Currency:** US dollars. SolarWinds reports in dollars and its debt is in dollars. It also sells in euros, pounds and Australian dollars (10-K Item 7A), but 64.82% of revenue is from the US.

**Analysis date: 2025-02-05.** This was the last undisturbed trading day, when the stock closed at $15.18, and the date both fairness opinions priced from. Every market input is from that date: the 10-year Treasury, the equity risk premium, the January 2025 ratings table, and the January 2025 industry betas. That way the value can be set against the $15.18 market price and the $18.50 deal price on the rates that held when the deal was struck. Valuing with October 2026 rates would compare the deal with a world that did not exist when it was signed.

**This is a retrospective valuation.** It uses the FY2024 10-K (filed 2025-02-19) and the merger information statement (filed 2025-03-27), which were not yet public on 2025-02-05. Management had the FY2024 results by then (the board adopted the 2025 plan on the full-year numbers on 2025-01-12), and the forecasts in the information statement are the ones the board and its advisers used. Market inputs, however, are strictly as of 2025-02-05.

## Headline results

- **Valuation (final report, section 9):** $15.32 a share at the status quo, $16.08 at the optimal debt ratio (lever $0.76, $139.1M), $12.65 and $7.77 in the stress cases, from the professor's spreadsheet, fcffsimpleginzu.xlsx (February 2026 edition), with the inputs, results and filled workbook in [professor-spreadsheet/](professor-spreadsheet/). 1.01 times the $15.18 unaffected price and 0.83 times the $18.50 deal price.

The rest are from [model-output.md](model-output.md); from 2026-11-03 the model's DCF is the cross-check for the sheet, not the report's number:
- **Cost of debt:** 8.85%, the synthetic B- rate (interest coverage 1.85x on operating income; `modeling_choices.kd_source: synthetic`), the course's method. The term loan's own 7.11% (`debt.kd_pretax_observed`) is the cross-check; using it would give 10.23% and $16.13 a share, a 3% difference.
- **Cost of capital:** 10.67% for the forecast years; 8.23% in the terminal period (beta 1.0, 21% debt, and the cost of debt the §3 schedule assigns to an A- borrower at 21%, 5.38%, not the 8.85% used to 2030).
- **Stable return on capital:** equal to the 8.23% stable cost of capital, so growth after 2030 adds no value. A judgment (`forecast.stable_roic`): ROIC is 6.66% on all capital and 6.53% with R&D capitalized (model §8); the marginal dollars have been acquisitions, which is where the goodwill came from. The 87.35% return on operating capital excluding goodwill is after-tax operating income over about three years of R&D: it shows the business is capital-light, not what a new dollar earns. 12% is kept as the upside sensitivity ($17.73; the deal price needs about 14.4%).
- **Discounted cash flow value (model, cross-check):** $15.66 a share, on the course method (consistent reinvestment in the terminal value; options subtracted as a claim). The sheet's $15.32 differs mainly in the terminal defaults (8.66% stable cost of capital and growth at the 4.43% risk-free rate, against 8.23% and 2.5% here) and in reinvestment (sales-to-capital 1.54, against the plan's own).
- **Against the prices:** the model's $15.66 is 1.03 times the $15.18 unaffected price and 0.85 times the $18.50 deal price; the deal was 18% above that value and 22% above the market.
- **Stress cases (model §6):** revenue at the 2022–2024 rate of 5.25% instead of the plan's 8.12% gives $12.65 with the plan's margins, $9.57 with the margin held at 32.69% and $7.79 with it held at 29.11%, the 2024 margin on the plan's own definition (adjusted EBITDA − SBC − D&A; the 26.15% GAAP margin is not comparable).
- **Stable-beta sensitivity (model §6):** 0.80 gives $17.24 and 1.46 (today's unlevered beta 1.22 relevered at 21%) gives $12.96, both with no excess returns; the stable beta is the largest single assumption.
- **Optimal debt ratio:** 21%, against the actual 33%.

[final-report.md](final-report.md) is the submission; [valuation-report.md](valuation-report.md) explains what the model's figures mean. [walkthrough.md](walkthrough.md) builds them step by step for a reader with no finance background.

## File map

| File | What it is |
|---|---|
| [study-guide.md](study-guide.md) | Study guide, one chapter per lesson: key terms, what the project asked, information required and its source, and the steps worked with SolarWinds' numbers |
| [inputs.yaml](inputs.yaml) | The ledger: every input number with its source and date |
| [model-output.md](model-output.md) | Generated by `.claude/skills/value-company/tools/model.py` from the ledger; never hand-edited |
| [final-report.md](final-report.md) | The deliverable, in the course's nine-question format; its section 9 DCF comes from the professor's spreadsheet |
| [professor-spreadsheet/](professor-spreadsheet/) | The final report's DCF in Damodaran's fcffsimpleginzu.xlsx (February 2026 edition): [README](professor-spreadsheet/README.md), [inputs](professor-spreadsheet/inputs.md), [results](professor-spreadsheet/results.md), the filled workbook, and the exhibit-4 override |
| [valuation-report.md](valuation-report.md) | The longer report on the model's figures; its DCF section is the cross-check since 2026-11-03 |
| [report-exhibits/](report-exhibits/) | Charts and tables for the final report, built by `make-exhibits.py` |
| [walkthrough.md](walkthrough.md) | Plain-language trail, one section per lesson |
| `lesson-01.md` … `lesson-36.md` | Every course question for this lesson, answered for SolarWinds |
| [sources/](sources/) | Compiled filings, deal documents, market data and peer data; manifest in [sources/README.md](sources/README.md) |

| Module | Lessons |
|---|---|
| 1 — Foundations and discount rates | [01](lesson-01.md) · [02](lesson-02.md) · [03](lesson-03.md) · [04](lesson-04.md) · [05](lesson-05.md) · [06](lesson-06.md) · [07](lesson-07.md) · [08](lesson-08.md) · [09](lesson-09.md) · [10](lesson-10.md) · [11](lesson-11.md) · [12](lesson-12.md) |
| 2 — Investment returns and financing | [13](lesson-13.md) · [14](lesson-14.md) · [15](lesson-15.md) · [16](lesson-16.md) · [17](lesson-17.md) · [18](lesson-18.md) · [19](lesson-19.md) |
| 3 — Financing mix and dividends | [20](lesson-20.md) · [21](lesson-21.md) · [22](lesson-22.md) · [23](lesson-23.md) · [24](lesson-24.md) · [25](lesson-25.md) · [26](lesson-26.md) |
| 4 — Dividends and valuation | [27](lesson-27.md) · [28](lesson-28.md) · [29](lesson-29.md) · [30](lesson-30.md) · [31](lesson-31.md) · [32](lesson-32.md) · [33](lesson-33.md) · [34](lesson-34.md) · [35](lesson-35.md) · [36](lesson-36.md) |

## Source key

Short codes used in the lesson files. Paths are relative to this folder.

| Code | What it is | Files |
|---|---|---|
| **10-K** | Annual reports, FY2024 (primary), FY2023, FY2020, FY2018 | `sources/filings/swi-10k-fy<year>.md` |
| **PROXY** | 2024 proxy statement: board, pay, ownership | `sources/filings/swi-def14a-2024.md` |
| **S-1** | 2018 IPO prospectus | `sources/filings/swi-s1-2018-ipo-prospectus.md` |
| **SUNBURST 8-Ks** | December 2020 attack disclosures | `sources/filings/swi-8k-2020-12-*.md` |
| **DEAL** | Merger information statement (DEFM14C): background, fairness opinions, management forecasts, golden parachutes | `sources/deal-docs/swi-defm14c-2025-merger.md` |
| **DEAL 8-Ks** | Merger announcement and closing | `sources/deal-docs/swi-8k-2025-*.md` |
| **MARKET** | Rates, ERP, ratings table, betas, country risk as of 2025-02-05 | `sources/market-data/` |
| **PEERS** | Eight peers' FY2024 fundamentals and 2025-02-05 prices | `sources/peer-filings/peer-facts-2025-02-05.md` |
| **CIQ** | Capital IQ pulls (2026-10-05), used only as a cross-check | `sources/capital-iq/` |
| **LESSON** | The lesson's own slides, transcripts and spreadsheets | `<CC>/<module>/lesson-NN/` |
| **BLOG** | Damodaran's blog archive | `03-corporate-finance/03-4-blogs/posts/` |

## Corrections log

One line per correction: date, what changed, which files.

### Changes from the 2026-09/10 project this rerun replaced

- 2026-10-25 — **Valuation date.** Moved to 2025-02-05, from rates as of 2026-09/10. Risk-free rate 4.43% (was 4.17%–5.07% across versions); ERP 4.27% before the country adjustment.
- 2026-10-25 — **Ratings table.** Now the January 2025 edition; the lesson 18 spreadsheet's 2013 table is no longer used.
- 2026-10-25 — **Equity value.** 171.6M record-date shares × $15.18 unaffected price = $2,604.9M. Was $3,142.1M at the $18.31 pre-close price, which already reflected the deal.
- 2026-10-25 — **Debt.** Face value plus leases, $1,285.0M. Was carrying value plus leases, $1,256.0M. Cloud purchase commitments of $68.4M checked and ruled out.
- 2026-10-25 — **Operating income.** GAAP EBIT of $208.4M. Was Capital IQ's standardized $218.7M.
- 2026-10-25 — **Unlevered beta.** 1.22 from the January 2025 dataset. Was 1.2482 from January 2026.
- 2026-10-25 — **Equity risk premium.** Weighted by US and international revenue, 4.92%. Was the mature premium alone.
- 2026-10-25 — **Terminal value.** Uses consistent reinvestment (lesson 32). Was final-year cash flow grown at g, which assumed no reinvestment in perpetuity.
- 2026-10-25 — **Peers.** Now the eight US-listed companies from Jefferies' fairness-opinion set. Was Datadog, Dynatrace and PagerDuty, which grew 9–26% against SolarWinds' 5%.
- 2026-10-25 — **History.** Capex, working capital and history rows now come from the cash flow statements. They were partly placeholders in the skill's old test fixture.

### Corrections during this run

- 2026-10-25 — **FCFE add-back.** Model §5 now adds back the 2022 non-cash impairments ($906.4M, `company.history` 2022 `impairment`). The 2022 FCFE went from −$1,512.6M to −$606.2M. Touched lessons 26 and 27 and walkthrough steps 26 and 27.
- 2026-10-25 — **Book-weight cost of capital.** Now includes leases on the debt side: 9.19%, was 9.27%. Touched lesson 13 and step 13.
- 2026-10-25 — **Optimal debt by APV.** Now from the model's section 9, not a hand script over a coarse grid. Optimum unchanged at 21%; gain $220.3M, was $216.8M. Touched lesson 21 and step 21.
- 2026-10-25 — **Relative-valuation per-share values.** These now subtract the $187.0M option and RSU claim, as the DCF does. The revenue multiple gives $8.34 (was $9.43) and the EBITDA multiple $19.95 (was $21.04). Touched lesson 35, step 35 and the report.
- 2026-10-25 — **Three measures of the gain from reaching the optimal debt ratio.** These are now reconciled in model §6: DCF $0.52, capitalized savings $0.84 and APV $1.28 a share. Touched lessons 19 and 34, steps 19 and 34, and the report.
- 2026-10-25 — **Report attributions.** The report attributed the 2030 cash-flow excess to depreciation; it is deferred-revenue growth (`facts.forecast-2030-detail`). It also cited base-year capex as the forecast. Both fixed in report sections 3 and 6.
- 2026-11-01 — **2023 market check.** Lesson 32 said Party A's indication of about $14.00 was the only one. There were three: Party A $13.00, revised down from about $14.00; Party B $12.00 to $13.00; Party C $12.50 (`facts.market-check-2023`). Touched lesson 32.
- 2026-11-01 — **Sponsor ownership.** The proxy states 66.34%; 66.35% is the sum of the rounded holdings (36.56% + 29.79%). Lesson 2 cited the 66.34% fact with the 66.35% figure in two places; now matched. Mentions labelled as the sum are unchanged. Touched lesson 2.
- 2026-11-01 — **Stable-period cost of capital.** The terminal value now uses beta 1.0 and 21% debt (8.51%) per lesson 32, with the stable return on capital set equal to it (was 10% at the current 10.23%). Value per share $15.63 at the time, was $13.00; financing lever $0.22, was $0.52. Touched model.py, the ledger, model-output, lessons 15, 19, 22, 24, 29, 31–36, the walkthrough, both reports, the study guide and the exhibits. Superseded the same day by the next entry.
- 2026-11-01 — **Stable return on capital.** 12%, was 8.51% (equal to the stable cost of capital). Model §8 now capitalizes R&D over a 3-year life: adjusted ROIC 6.53% against 6.66% unadjusted, because the capital base is the 2016 buyout goodwill; return on operating capital excluding goodwill 87.35% (60.56% on a 5-year life). The 12% is a 3.5-point spread over the 8.51% stable cost of capital (`forecast.stable_roic`). Model §6 adds stress cases at the 2022–2024 revenue growth rate ($14.17, $10.81, $7.32 a share at the time). Value per share $17.45 at the time, was $15.63; financing lever $0.24, was $0.22. Touched model.py, the ledger, model-output, lessons 14, 15, 19, 27, 29, 31–36, the walkthrough, both reports, the study guide, this README and the exhibits. Superseded the same day by the next entry.
- 2026-11-01 — **Stable return on capital and stable cost of debt.** Return on new capital now equal to the stable cost of capital, 8.23%; was 12% earlier today. A fresh-context review found the 12% asserted rather than earned: the 87.35% return on operating capital is after-tax operating income over about three years of R&D and shows the business is capital-light, not what a new dollar earns; the marginal dollars have been acquisitions, on which the company earns 6.66%. The stable period now takes the cost of debt the §3 schedule assigns at 21% (A-, 5.38%) instead of holding today's 7.11%, which contradicted the schedule; stable cost of capital 8.23%, was 8.51%. Model §6 adds a stable-beta sensitivity (0.80 → $17.74; 1.46 → $13.36). The third stress case now holds the 2024 margin on the plan's own definition, 29.11% (was the 26.15% GAAP margin). Value per share $16.13, was $17.45; financing lever $0.22, was $0.24; stress cases $13.05 / $9.89 / $8.08. Touched model.py, the ledger schema, the ledger, model-output, lessons 14, 15, 19, 27, 29, 31–36, the walkthrough, both reports, the study guide, this README and the exhibits.
- 2026-11-03 — **Payout regression.** Lesson 28's benchmark now uses Damodaran's January 2025 US payout regression (payout = 0.990 − 0.478 × beta − 0.115 × ROE, 1,532 firms, R-squared 2.6%), the edition in force on the analysis date, instead of the lesson slides' 2014 regression. Predicted payout 18.2%, was 18.8%; the 2014 version is kept as a cross-check. Conclusion unchanged. Value per share unchanged. Touched the ledger, lesson 28, the walkthrough, the study guide, this README and the source manifest (new `sources/market-data/dividend-regression-2025-01.md`).
- 2026-11-03 — **Cost of debt from the synthetic rating.** `modeling_choices.kd_source` is now `synthetic`, the course's method: the professor's spreadsheets build the cost of debt from a rating, and 2024 interest coverage of 1.85x (EBIT $208.4M over interest $112.4M) maps to B- and a 4.42% spread over the 4.43% Treasury, 8.85%; was the term loan's observed 7.11%, which stays in `debt.kd_pretax_observed` as the cross-check. After-tax cost of debt 6.64%, was 5.33%; cost of capital 10.67%, was 10.23% (book weights 9.81%, was 9.19%). Value per share $15.66, was $16.13; enterprise value $3,899.8M, was $3,979.8M; financing lever $0.69 ($117.9M), was $0.22 ($37.9M); EVA −$94.1M, was −$84.0M; stress cases $12.65 / $9.57 / $7.79, were $13.05 / $9.89 / $8.08; stable-beta sensitivity $17.24 / $12.96, was $17.74 / $13.36; stable-ROIC row $15.66 / $16.83 / $17.73 / $18.64 / $19.54. Unchanged: the 21% optimum and 10.03%, the $16.35 at the optimum, the 8.23% stable period, multiples, APV, FCFE and dividend figures. Conclusion unchanged. model.py's §6 reconciliation label now names the cost-of-debt basis from `kd_source`. Touched model.py, the ledger, model-output, lessons 10, 12–19, 22, 25, 27–36, the walkthrough, both reports, the study guide, this README and the exhibits.
- 2026-11-03 — **Valuation moved to the professor's spreadsheet; the model's DCF is now the cross-check.** The final report's section 9 is rebuilt from Damodaran's fcffsimpleginzu.xlsx (February 2026 edition), the course's method, with the same inputs (10.67% cost of capital entered directly, management's plan, 25% tax, debt $1,285.0M, cash $259.3M) and the sheet's defaults where we had nothing better: a 10-year horizon, the cost of capital fading to 8.66% (risk-free plus the 4.23% mature-market premium) over years 6–10, growth after year 10 at the 4.43% risk-free rate, return on new capital equal to the cost of capital, reinvestment at the software sales-to-capital ratio of 1.54, and the 12.2M restricted units counted as shares (183.8M) with only the 0.1M options valued as a claim ($1.6M). Value per share $15.32, was $15.66; at the optimal debt ratio $16.08, was $16.35; financing lever $0.76 ($139.1M), was $0.69 ($117.9M); enterprise value $3,843.2M, was $3,899.8M; PV of explicit cash flows $1,642.7M over ten years, was $1,303.2M over six; PV of terminal value $2,200.5M, was $2,596.7M; stress cases $12.65 / $7.77, were $12.65 / $7.79. The report drops the stable-period table, the return-on-new-capital paragraph, the stable-ROIC and stable-beta sensitivities and the $24.29 other-terminal-value sentence, and adds the sheet's own sensitivities ($14.52 at 2.5% perpetual growth; $16.94 with near-zero reinvestment). Sections 1–8 unchanged except the executive-summary rows. Conclusion unchanged: in line with the $15.18 market price. model.py, the ledger's inputs and model-output.md unchanged (one `facts` entry added so the sheet's figures trace for `check-walkthrough.py`). Exhibit 4's DCF bars now read `professor-spreadsheet/exhibit-values.yaml`. Touched the final report, the valuation report (notes at §6 and §8), the walkthrough (notes at steps 34 and 36), the study guide, lessons 19 and 29–36, this README, the exhibits, and the new `professor-spreadsheet/` folder.

## Questions skipped or answered with a stand-in

| Entry | Why |
|---|---|
| l08-p2: regression beta, standard error, R², Jensen's alpha | No price history for a delisted ticker; the four fields are under `meta.omitted`. Answer it if price data is added |
| m1-step-08: regression beta | Same reason. Lesson 8 explains what the regression would show and uses the bottom-up beta |
| m1-step-10 and m1-step-11: segment betas and total beta | One reporting segment; no R² for total beta. Lesson 11 shows an illustration from the January 2024 industry correlation |
| l27-p1 (Jensen's alpha) and lesson 31 (analyst growth) | Fields omitted; the lessons use management's forecast and total-return history instead |
| Lesson 13 divisional questions | Answered as single-business cases (one segment) |
