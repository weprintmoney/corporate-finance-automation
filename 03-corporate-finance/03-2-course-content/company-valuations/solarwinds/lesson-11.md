---
title: "SolarWinds (SWI) — Lesson 11: The \"Right\" Beta"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 11: The "Right" Beta

### Lesson 11 — The "Right" Beta

- **Lesson 11, Session 11 · Part 1 — "Bottom-Up Betas Across Companies — Multi- and Single-Business Cases"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-1.md))
    - Quote: "My sample size would be far too small if I focused just on Brazilian companies."
    - Question for SolarWinds: Should SolarWinds' comparable set be global rather than home-country only, to get a large enough sample? What does the broader sample change in the unlevered beta, and does it introduce companies that are not really comparable?
    - Sources needed: The size of the US sample; whether a global beta file is in `sources/`; SolarWinds' revenue by region; the peer notes on non-US companies.
    - Where to find: `sources/market-data/industry-betas-2025-01-05.json`; `inputs.yaml` `country.exposures`, `beta.unlevered_bottom_up`; `sources/peer-filings/peer-facts-2025-02-05.md` ("Why these companies").
    - Answer: Not needed, and not done. Damodaran needed global samples for Brazil because Brazil has too few listed firms in a sector. The US software group has 333 firms (`beta.unlevered_bottom_up` source), so sample size is not the constraint. SolarWinds is a US company that sells worldwide: 64.82% of revenue is US and 35.18% international (`country.exposures`), and its customers buy the same product in every region, so the business risk is the same as that of its US-listed peers. A global file is not in `sources/market-data/`, and the compiled data cannot say how much it would move the number. What a broader sample would add is firms reporting under other accounting standards and facing other regulation. The same reasoning kept three of Jefferies' non-US peers out of the relative-valuation set: Check Point, TeamViewer and Trend Micro file outside the US on different accounting standards (`sources/peer-filings/peer-facts-2025-02-05.md`). The international revenue enters the valuation through the equity risk premium (4.92% weighted, `country.weighted_erp`), where it belongs, not through the beta. Judgment call: if the international share were much larger than 35.18%, a global group would be worth testing.

- **Lesson 11, Session 11 · Part 2 — "Betas and Cost of Equity for Private Businesses — Total Beta"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-2.md))
    - Quote: "You cannot use a market beta to come up with the cost of equity because that market beta focuses only on the risk you cannot diversify away."
    - Question for SolarWinds: Is SolarWinds' owner or marginal investor diversified? If not, what is the total beta (market beta divided by the square root of R-squared) and the resulting cost of equity, and when during SolarWinds' ownership history would total beta have been the right measure?
    - Sources needed: Who owned and priced the stock; an R-squared or correlation to the market.
    - Where to find: `inputs.yaml` `governance.marginal_investor`, `governance.controlling_holders`; `beta.regression_r2` (omitted); `sources/filings/swi-def14a-2024.md`; lesson spreadsheet `01-foundations-and-discount-rates/lesson-10/spreadsheet-totalbeta24.md`.
    - Answer: The marginal investor was diversified, so market beta is the right measure. Diversified institutions holding the roughly 34% public float set the traded price (`governance.marginal_investor`). Silver Lake (36.56%) and Thoma Bravo (29.79%) together held 66.35% (`governance.controlling_holders`; arithmetic), but each is a private-equity firm that owns many companies, so SolarWinds is one position in a diversified portfolio, even though the ledger notes they were not diversified within this one holding. The total-beta formula needs SolarWinds' own R-squared. There is none, because the stock has no price history to regress (`meta.omitted`: `beta.regression_r2`). As an illustration only, using Damodaran's industry-average correlation to the market of 0.3374 for this group (January 2024, lesson spreadsheet, the only one compiled; facts.industry-correlation-software-2024): total beta = levered beta ÷ correlation = 1.6714 ÷ 0.3374 = 4.95 (facts.total-beta-illustration), and a cost of equity of 4.43% + 4.95 × 4.92% = 28.8% (facts.total-coe-illustration), against the 12.65% in model-output.md §1. This figure is not used anywhere. It mixes a 2024 correlation with 2025 inputs, and it describes an owner who holds nothing else. Total beta would have been the right measure only if SolarWinds had been owned by one person with all of their wealth in it. That was never the case: not under the sponsors from 2016 to 2018, not in the public period, and not after the 2025 sale to Turn/River Capital, a private-equity buyer. The one place a partial adjustment has an argument is the public period, when two holders with 66.35% could not easily sell. Their consent was needed for the sale (`governance.marginal_investor`), and that shows up as a control premium in the deal price, not in the discount rate.

## Module 1 Step — Questions for This Lesson

- **Levered beta and total beta** (`m1-step-11`)
    - What is the levered beta at the company's current debt-to-equity ratio and marginal tax rate? 1.6714 = 1.22 × (1 + (1 − 0.25) × 0.4933) (model-output.md §1).
    - What would the total beta be if all risk counted, and when would that be the right measure? 4.95 on the illustrative 2024 correlation (above; `beta.total_beta` is listed in `meta.omitted` because no R-squared exists). It is the right measure for an owner who cannot diversify, which describes no SolarWinds owner.

## Notes

Lesson 11 closes the beta arc without changing it: the sample stays US, the beta stays market beta, and the number carried forward is the 1.6714 levered beta. The total-beta figure is an illustration so the cost of ignoring diversification is visible: 28.8% against 12.65%.

Lesson 12 moves from equity to debt.
