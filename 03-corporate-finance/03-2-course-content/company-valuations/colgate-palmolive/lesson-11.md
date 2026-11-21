---
title: "Colgate-Palmolive (CL) — Lesson 11: The Right Beta"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 11: The Right Beta

### Lesson 11 — The Right Beta

- **Lesson 11, Session 11 · Part 1 — "Bottom-Up Betas Across Companies — Multi- and Single-Business Cases"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-1.md))
    - Quote: "My sample size would be far too small if I focused just on Brazilian companies."
    - Question for Colgate-Palmolive: Should Colgate-Palmolive's comparable set be global rather than home-country only, to get a large enough sample? What does the broader sample change in the unlevered beta, and does it introduce companies that are not really comparable?
    - Sources needed: Size of the US samples; global industry betas; the candidate peer list.
    - Where to find: ledger `facts.industry-beta-detail`, `beta.segments`, `country.exposures`; `sources/market-data/industry-betas-2026-01-05.json` (US companies only); `sources/capital-iq/quick-comps.tsv`.
    - Answer: The US samples are large enough: 110 household products firms and 78 food processors (`facts.industry-beta-detail`). Sample size is the reason to go global, and it does not apply. There is a different argument for a global set: Colgate sells about two-thirds of its product abroad (`country.exposures`), and two of the ten comparables Capital IQ lists, Reckitt and Henkel, are European. A global household products beta would be the natural cross-check. It is not in `sources/`; the industry file holds US companies only, so the effect on the unlevered beta is not computed here and no number is given. The risk of going broader is the one already present in the US sample: more small, local, discretionary-product firms that are not like Colgate. The better refinement is narrower, not wider: a hand-picked set of large global staples companies, which lesson 35 will fix.

- **Lesson 11, Session 11 · Part 2 — "Betas and Cost of Equity for Private Businesses — Total Beta"** ([transcript](../../01-foundations-and-discount-rates/lesson-11/session-11-part-2.md))
    - Quote: "You cannot use a market beta to come up with the cost of equity because that market beta focuses only on the risk you cannot diversify away."
    - Question for Colgate-Palmolive: Is Colgate-Palmolive's owner or marginal investor diversified? If not, what is the total beta (market beta divided by the square root of R-squared) and the resulting cost of equity, and when during Colgate-Palmolive's ownership history would total beta have been the right measure?
    - Sources needed: Ownership; regression R-squared; relative volatility.
    - Where to find: ledger `governance.marginal_investor`, `meta.omitted` (`beta.total_beta`), `beta.regression_r2`, `facts.total-beta-illustration`, `facts.regression-diagnostics`; `module-1-cross-checks-output.md` §2.
    - Answer: Diversified, so total beta is not used and `beta.total_beta` is listed under `meta.omitted`. Institutions hold 87% of the shares and the three largest are index-fund managers (`governance.marginal_investor`). As an illustration only: total beta is the market beta divided by the correlation with the market, which is the same thing as the stock's volatility over the market's. For Colgate that is 0.315 ÷ 0.25, about 1.24, and the cost of equity at that beta would be 11.50% against 8.76% (`facts.total-beta-illustration`). The 2.74-point difference is what it would cost to hold Colgate as your only asset. No one who sets the price does. In the period our filings cover Colgate has been widely held throughout, so there is no point in its recent history at which total beta was the right measure. It would become relevant only in a sale to a private, undiversified owner, which nothing in the filings suggests; the 10-K says the company knows of no arrangement that could result in a change in control.

## Module 1 Step — Questions for This Lesson

- **Levered beta and total beta**
  - What is the levered beta at the company's current debt-to-equity ratio and marginal tax rate? 0.7321 = 0.6796 × (1 + (1 − 0.25) × 0.1030) (model-output.md §1). With a risk-free rate of 4.82% and a weighted premium of 5.38%, the cost of equity is 4.82% + 0.7321 × 5.38% = 8.76%.
  - What would the total beta be if all risk counted, and when would that be the right measure? About 1.24, giving a cost of equity of 11.50% (`facts.total-beta-illustration`). It would be right for an owner with most of their wealth in Colgate. It is not right here.

## Notes

The cost of equity is 8.76%. This lesson adds no new judgment; it levers the beta chosen in lesson 10 and confirms that the market beta, not the total beta, fits Colgate's owners. The total-beta illustration is useful for one thing: it shows that Colgate's low market beta is not low risk. A stock 1.24 times as volatile as the index earns a below-market required return only because almost all of that volatility can be diversified away.

The debt-to-equity ratio uses the market value of debt, $8,084.0M including leases, which lesson 12 establishes. Because debt is under a tenth of the firm's value, even a large error in the debt figure would move the levered beta very little.
