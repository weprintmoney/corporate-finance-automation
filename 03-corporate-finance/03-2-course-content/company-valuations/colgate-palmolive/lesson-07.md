---
title: "Colgate-Palmolive (CL) — Lesson 07: Country Risk Premiums"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 07: Country Risk Premiums

### Lesson 07 — Country Risk Premiums

- **Lesson 07, Session 7 · Part 1 — "Implied Equity Risk Premiums and Building Country Risk Off Them"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-1.md))
    - Quote: "a company's risk does not come from where it's incorporated but from where it does business."
    - Question for Colgate-Palmolive: How much of Colgate-Palmolive's revenue (or production, if that is the better measure) comes from outside its home country, and what is its revenue-weighted equity risk premium compared with the flat home-country number?
    - Sources needed: Revenue by geography; regional equity risk premiums.
    - Where to find: ledger `country.exposures`, `country.weighted_erp`, `market.mature_erp`, `facts.segment-results-2025`; `sources/filings/cl-10k-fy2025.txt` note 14; `sources/market-data/country-risk-regions-2026-01-01.md`.
    - Answer: About two-thirds. The 10-K says approximately two-thirds of net sales come from outside the United States and approximately 45% from emerging markets (`country.exposures`). Summing the two disclosed United States figures gives $6,658M, 32.67% of net sales, so the ledger's 33.33% is a rounding of the company's own words and close to the computed share (`facts.segment-results-2025`). Revenue is the right measure for Colgate. Toothpaste, soap and pet food are sold to local consumers in local currency, and the risk that matters is whether those consumers keep buying and what their currency is worth. Production is local too in most regions, so it would give a similar picture, but the 10-K does not report production by country. The revenue-weighted premium is 5.38%, against a flat 3.61% (`country.weighted_erp`, `market.mature_erp`). That difference of 1.77 points is worth 1.30 points of cost of equity and 1.17 points of cost of capital: 8.76% and 8.34% with it, 7.46% and 7.17% without (`facts.cost-of-capital-alternatives`). It is the largest adjustment in the cost of capital, and ignoring it because Colgate is a New York company would be the mistake this lesson warns about.

- **Lesson 07, Session 7 · Part 2 — "Company Equity Risk Premiums and Implied ERP"** ([transcript](../../01-foundations-and-discount-rates/lesson-07/session-7-part-2.md))
    - Quote: "For every one of these companies, I'm looking past the country of incorporation to where they do business."
    - Question for Colgate-Palmolive: What is Colgate-Palmolive's weighted equity risk premium in numbers, which single country exposure moves it most, and what would make that exposure change?
    - Sources needed: Weights and premiums by region; sensitivity to the emerging-market share.
    - Where to find: ledger `country.exposures`, `facts.country-premium-method`, `facts.us-country-premium-treatment`, `facts.segment-results-2025`; `module-1-cross-checks-output.md` §3.
    - Answer: 5.38% = 33.33% × 3.61% + 45% × 7.05% + 21.67% × 4.65% (`country.exposures`). The emerging-market slice moves it most: it adds 1.55 of the 1.77 points, and other developed markets add 0.23 (`facts.country-premium-method`). Inside that slice Latin America is the largest piece, $4,776M of sales at a 4.39% country risk premium, ahead of Asia Pacific at $2,814M and 1.49% and Africa/Eurasia at $1,172M and 4.26% (`country.exposures` source note). What would change it: the mix, and the premiums. If emerging markets were 40% or 50% of sales and not 45%, the weighted premium would be 5.21% or 5.55% (`facts.country-premium-method`). Latin American sales were flat in dollars in 2025 while Europe grew, which pulls the mix slowly toward lower-risk markets. Damodaran also re-rates every country each January and July.

## Module 1 Step — Questions for This Lesson

- **Country risk and weighted ERP**
  - What is the best measure of the company's country exposure (revenues, production, assets)? Revenues, by where the customer is. Consumer staples are sold and largely made in the same market, and revenue is the only measure the 10-K reports by region.
  - What is the geographic breakdown of that measure? United States 33.33%, emerging markets 45%, other developed markets 21.67% (`country.exposures`). The first two come from the company's own statement in note 14; the third is the remainder.
  - What is the weighted average ERP? 5.38% (`country.weighted_erp`; model-output.md §1).
  - Why might that ERP change? A shift in the sales mix; a change in sovereign ratings; a move in the mature-market premium, which has already happened since 2026-11-01 (lesson 6); or a different reading of the United States' own premium, below.

## Notes

The weighted premium is 5.38%. Three limits on confidence, in order of size.

First, the emerging-market premium of 3.44% is built from regional averages weighted by the Oral, Personal and Home Care regions' sales, because the 10-K gives no sales by country. A regional average treats Mexico and Argentina alike. This is an estimate, and it could be off by half a point either way.

Second, the three-way split uses the company's rounded statements ("approximately two-thirds", "approximately 45%"). The computed United States share is 32.67%.

Third, an open point for review, not changed here. Damodaran's tables now give the United States, rated Aa1, a country risk premium of 0.22% over the mature market (`facts.us-country-premium-treatment`). The ledger prices United States sales at 3.61% with nothing added and adds the regional premiums to the same 3.61%. If 3.61% is the mature premium, the United States slice should carry 3.83% and the weighted premium would be 5.45%. If 3.61% is the United States premium, the mature premium is 3.39% and the weighted premium would be 5.23%. The ledger's 5.38% sits between the two, and the gap either way is under 0.15 points of premium, about 0.1 points of cost of equity. It does not change any conclusion, but the report should state which reading it adopts.

Hill's sells 66.4% of its product in the United States, and Oral, Personal and Home Care only 22.8% (`facts.segment-results-2025`). Lesson 10 uses one weighted premium for both; a segment-level valuation would give Hill's a lower one.
