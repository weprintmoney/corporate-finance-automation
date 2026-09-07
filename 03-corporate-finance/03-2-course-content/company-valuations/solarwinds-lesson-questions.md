---
title: "SolarWinds (SWI) — Lesson-by-Lesson Question & Source Log"
status: active
owner: weprintmoney
created: 2026-09-07
last_updated: 2026-09-07
---

# SolarWinds (SWI) — Lesson-by-Lesson Question & Source Log
*Applied Corporate Finance — all 4 modules, working through the course video-by-video*

## Purpose & method

This is a study log, not a valuation. For every lecture video transcript across all 36 lessons, it captures:

- **A quote** — one short, verbatim line from the lecture that anchors the concept being taught
- **A question for SWI** — the specific thing that concept raises about SolarWinds when you actually try to apply it, not a generic textbook question
- **Sources needed** — what data or document would answer that question
- **Where to find it** — a concrete pointer, using the Source Key below

Each entry is a planning artifact: it identifies what's needed and where it lives, but does **not** do the research itself. That's the next pass — either by hand or by running `/evaluate-company` (see [company-valuations/solarwinds-valuation.md](solarwinds-valuation.md), the existing Module-1-scoped 12-step valuation already in this folder) against a specific question here.

Lesson 24 has no transcript on the course's video channel — flagged in place, not fabricated.

## Company context: SolarWinds (SWI)

IT infrastructure monitoring/observability SaaS company. Taken private 2016 by Thoma Bravo + Silver Lake (~$4.5B LBO), re-IPO'd Oct 2018 (NYSE: SWI). December 2020: the SUNBURST nation-state supply-chain cyberattack (~18,000 customers affected, including federal agencies) — CEO Kevin Thompson resigned days later; Sudhakar Ramakrishna became CEO January 2021. April 2025: acquired by Turn/River Capital and taken private again, $18.50/share (~$4.4B, ~5.5x 2024 revenue). FY2024 is the final full year of public filings. Silver Lake was the controlling shareholder (~75%) driving the sale.

## Source Key

Cited by these short codes throughout:

| Code | What it is |
|------|-----------|
| **SEC-EDGAR** | SEC EDGAR filings for SWI — 10-K (esp. FY2024, final full public year), 10-Q, 8-K (SUNBURST Dec 2020, Turn/River deal), DEF 14A proxy, and the going-private Schedule 13E-3 / DEFM14A merger proxy (contains the banker's own fairness-opinion DCF/comps) |
| **REPO-SWI-VAL** | [solarwinds-valuation.md](solarwinds-valuation.md) — this folder's existing 12-step governance/objectives/cost-of-capital research on SWI |
| **REPO-RATES** | [`03-3-supplemental-data/market-rates.json`](../../03-3-supplemental-data/market-rates.json) — 10Y Treasury, SOFR, Fed Funds; CI-refreshed weekdays |
| **REPO-BETAS** | [`03-3-supplemental-data/industry-betas.json`](../../03-3-supplemental-data/industry-betas.json) — Damodaran sector unlevered/levered betas |
| **REPO-COUNTRY-RISK** | [`03-3-supplemental-data/country-risk.json`](../../03-3-supplemental-data/country-risk.json) — country equity risk premiums |
| **DAMODARAN-SITE** | pages.stern.nyu.edu/~adamodar — live Damodaran datasets/spreadsheets. The repo's local mirror at `03-5-damodaran-online/` is currently excluded from navigation (corrupted import, pending re-fetch) — go to the live NYU site instead |
| **DAMODARAN-BLOG** | [`03-4-blogs/posts/`](../../03-4-blogs/posts/) — ~680 "Musings on Markets" posts, fully imported and searchable locally |
| **PEER-FILINGS** | SEC EDGAR filings of comparable public observability/IT-ops SaaS peers — Datadog (DDOG), Dynatrace (DT), PagerDuty (PD) |
| **DEAL-DOCS** | Turn/River Capital's acquisition press release + the DEFM14A fairness opinion |
| **LESSON-MATERIALS** | That lesson's own `slides.md` / `reading-*.md` / `spreadsheet-*.md` in the same lesson folder |
| **NEWS-WEB** | General news/analyst commentary not otherwise covered |


## Module 1 — Foundations & Discount Rates (Lessons 1–12)

### Lesson 01 — Valuation: The Big Picture / What is Corporate Finance?

- **Lesson 01, Session 1 · Part 1 — "The Financial Balance Sheet and the Singular Objective of Maximizing Firm Value"** ([transcript](../01-foundations-and-discount-rates/lesson-01/session-1-part-1.md))
    - Quote: "You want to make your business the most valuable business you can."
    - Question for SWI: Splitting SolarWinds' FY2024 balance sheet into "assets in place" (legacy Orion/on-prem monitoring) versus "growth assets" (observability/AIOps platform, the Squadcast acquisition) — how did actual FY2024 capital allocation (R&D spend, capex, M&A dollars) divide between defending the existing base and funding the growth story, and does that split match management's subscription-transition narrative?
    - Sources needed: FY2024 R&D/capex breakdown by product line, business-combination footnote for Squadcast, segment disclosure (if any) separating legacy vs. observability revenue.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 7 (MD&A) and Notes to Financial Statements (R&D expense, capex, Squadcast acquisition note).

- **Lesson 01, Session 1 · Part 2 — "Companies Age Like Human Beings — Placing SolarWinds on the Corporate Life Cycle"** ([transcript](../01-foundations-and-discount-rates/lesson-01/session-1-part-2.md))
    - Quote: "The third theme is that companies, just like human beings, age."
    - Question for SWI: Given ~5% FY2024 revenue growth, 48% EBITDA margins, and a controlling PE shareholder that chose to sell rather than keep harvesting cash flows — does SolarWinds sit in the mature/financing-and-dividend stage of the life cycle the lesson describes, or does the observability/AI pivot argue for reclassifying it as still investment-stage, and which classification did Silver Lake's own decision to exit imply?
    - Sources needed: 5-year revenue growth and margin trend, capex/R&D-to-revenue ratio trend, buyback/dividend history, Turn/River deal rationale commentary.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (Selected Financial Data / 5-year trends) and prior 10-Ks FY2019–2023 for trend; DEAL-DOCS — Turn/River press release for stated acquisition rationale.

### Lesson 02 — The Objective: Utopia and Let Down (corporate governance)

- **Lesson 02, Session 2 · Part 1 — "The Four Linkages Behind the Utopian World of Stock Price Maximization"** ([transcript](../01-foundations-and-discount-rates/lesson-02/session-2-part-1.md))
    - Quote: "Finally, in this Utopian world, there are no social costs or social benefits."
    - Question for SWI: Existing repo research already documents Silver Lake's ~75% control (the stockholder-manager linkage). One level deeper — on the "lenders are fully protected" linkage, did SolarWinds' credit-agreement/indenture covenants contain change-of-control or asset-sale protections against a sponsor-driven sale like the Turn/River deal, or were creditors as exposed as RJR Nabisco's bondholders were pre-1988?
    - Sources needed: SWI credit agreement / indenture covenant terms, change-of-control provisions, post-2025 refinancing terms tied to the Turn/River deal.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (debt footnote, Item 7A) and 8-K covering Turn/River deal financing; REPO-SWI-VAL for existing governance/control baseline.

- **Lesson 02, Session 2 · Part 2 — "Golden Parachutes, Poison Pills, and Managerial Self-Interest at Shareholder Expense"** ([transcript](../01-foundations-and-discount-rates/lesson-02/session-2-part-2.md))
    - Quote: "Given a choice between their interest and what's in the best interest of stockholders, managers often put their interest over stockholder interests."
    - Question for SWI: Beyond the repo's existing board-composition findings, did SolarWinds' executive change-of-control agreements include golden-parachute payouts to Ramakrishna and other officers triggered by the Turn/River close, and did that payout structure reward closing the deal at $18.50/share specifically, or closing at any price?
    - Sources needed: Item 402(t) "golden parachute compensation" table (required in going-private merger proxies), DEF 14A executive change-in-control agreements.
    - Where to find: SEC-EDGAR — SWI DEF 14A; DEAL-DOCS — Turn/River DEFM14A/Schedule 13E-3 golden-parachute disclosure table.

- **Lesson 02, Session 2 · Part 3 — "Where the Power Lies — Reading Top Shareholders to Judge Minority Protection"** ([transcript](../01-foundations-and-discount-rates/lesson-02/session-2-part-3.md))
    - Quote: "Institutional investors, when they don't like the way a company is run, tend to sell their shares and move on."
    - Question for SWI: Unlike Vale's government golden share or Tata's family cross-holdings, did SolarWinds structure any minority protection (special committee of independents, majority-of-minority vote) into the Turn/River merger vote, given Silver Lake was simultaneously the controlling shareholder and the party driving the sale?
    - Sources needed: Merger background/process disclosure — special committee formation, independent financial advisor engagement, vote structure/thresholds.
    - Where to find: DEAL-DOCS — Turn/River DEFM14A/Schedule 13E-3 ("Background of the Merger" and special-committee sections); REPO-SWI-VAL for existing shareholder/power-structure baseline.

### Lesson 03 — The Objective: Reality and Reaction (stated objectives)

- **Lesson 03, Session 3 · Part 1 — "Intermediate Objectives — Why Market Share and Revenue Growth Are Not Enough"** ([transcript](../01-foundations-and-discount-rates/lesson-03/session-3-part-1.md))
    - Quote: "Maximizing market share by itself is a dumb objective, and here's why."
    - Question for SWI: The repo's existing stated-objectives research shows subscription ARR growth and a defended ~48% EBITDA margin as SolarWinds' headline metrics. One level deeper — is ARR growth functioning as a genuine intermediate objective toward higher firm value, or is management discounting/bundling to hit ARR targets in ways that quietly erode the margin they also claim to be protecting?
    - Sources needed: ARR by cohort, net revenue retention, discounting/promotional disclosures, gross margin trend by product line.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (MD&A KPI section for ARR/NRR); REPO-SWI-VAL for the existing stated-objectives baseline (subscription/EBITDA metrics already gathered).

- **Lesson 03, Session 3 · Part 2 — "Self-Correcting Markets — Bond Covenants, Activist Investors, and the Imperial CEO"** ([transcript](../01-foundations-and-discount-rates/lesson-03/session-3-part-2.md))
    - Quote: "Left to their own devices, markets figure out ways to punish companies that essentially violate the rules."
    - Question for SWI: SUNBURST (Dec 2020) was arguably SolarWinds' own "social cost" event, followed by CEO Thompson's resignation days later — an apparent self-correction. Did the market's "day of reckoning" actually leave a lasting value discount through the 2025 sale, or did SWI trade back to a normal multiple with no lasting stigma by the time Turn/River paid $18.50/share?
    - Sources needed: SWI stock price/trading multiple history 2020–2025 vs. observability peers, outcome of the SEC's 2023 fraud charges against SWI and its CISO.
    - Where to find: SEC-EDGAR — SWI 8-Ks (Dec 2020 SUNBURST disclosure) and SEC litigation release re: 2023 CISO charges; PEER-FILINGS — DDOG/DT/PD trading multiples for comparison; NEWS-WEB — stock price history and analyst commentary on any "SUNBURST discount."

### Lesson 04 — Define and Measure Risk

- **Lesson 04, Session 4 · Part 1 — "Danger Plus Opportunity — The Ingredients of a Good Risk and Return Model"** ([transcript](../01-foundations-and-discount-rates/lesson-04/session-4-part-1.md))
    - Quote: "Risk is equal to danger plus opportunity."
    - Question for SWI: Testing CAPM's single-beta framework against the lesson's five requirements — does it adequately price SolarWinds' concentrated federal/government customer base and demonstrated tail risk (a nation-state supply-chain attack), or does that risk fall into the "diversifiable, unpriced" bucket even though it clearly hit the actual marginal shareholder, Silver Lake, who was not diversified?
    - Sources needed: SWI government/federal customer revenue concentration disclosure, confirmation of Silver Lake's ownership concentration and trading behavior.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 1A (Risk Factors, customer concentration) and Item 1 (business/customer mix); REPO-SWI-VAL — existing marginal-investor analysis (Step 4) for Silver Lake's diversification status.

- **Lesson 04, Session 4 · Part 2 — "Climbing the Risk Ladder — From Firm-Specific Risk to the Market Portfolio"** ([transcript](../01-foundations-and-discount-rates/lesson-04/session-4-part-2.md))
    - Quote: "Beta is not a measure of total risk."
    - Question for SWI: The lesson's "climbing the ladder" logic treats a firm-specific shock (a bad movie for Disney) as diversifiable — SUNBURST looks like exactly that kind of firm-specific event. Since Silver Lake, SWI's true marginal investor, held a concentrated ~75% stake and was not diversified, does the repo's regression beta of 0.88 understate the risk actually borne, because it implicitly assumes a diversified marginal investor that didn't exist here?
    - Sources needed: SWI weekly/monthly return regression vs. S&P 500 (beta + R²), evidence of whether Silver Lake actively traded shares or held a static position.
    - Where to find: REPO-SWI-VAL — Step 8 (regression beta 0.88) and Step 4 (marginal investor); DAMODARAN-SITE — total-beta/undiversified-investor adjustment methodology to re-run the calculation.

- **Lesson 04, Session 4 · Part 3 — "Proxy Models and the Weakness of Beta — Does the CAPM Actually Work?"** ([transcript](../01-foundations-and-discount-rates/lesson-04/session-4-part-3.md))
    - Quote: "The actual number is well below 10%."
    - Question for SWI: Given the repo's own regression beta (0.88) was flagged as low-to-moderate reliability, should a Fama-French-style proxy beta (using SWI's small-cap size and price-to-book at delisting) replace it, and would that produce a materially different cost of equity than the CAPM-only estimate already in the valuation file?
    - Sources needed: SWI market cap and price-to-book ratio at FY2024 year-end, Fama-French size/value factor return data.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 balance sheet (book equity) plus market cap from shares outstanding × price; DAMODARAN-SITE — for small-cap/proxy premium data; REPO-SWI-VAL — Step 8/9 for the existing beta baseline.

### Lesson 05 — The Risk Free Rate

- **Lesson 05, Session 5 · Part 1 — "Matching the Risk-Free Rate to Currency and Time Horizon"** ([transcript](../01-foundations-and-discount-rates/lesson-05/session-5-part-1.md))
    - Quote: "There is no global risk-free rate."
    - Question for SWI: The valuation currently uses the 10-year UST as the risk-free rate given USD reporting — but SolarWinds draws ~31% of revenue internationally and, post-2025, sits inside Turn/River's private capital structure with new acquisition debt. Does the "match currency to the analysis" principle still hold cleanly, or does the new ownership structure require a blended/entity-specific risk-free rate going forward?
    - Sources needed: Post-acquisition (2025) financing structure and debt currency mix for the $4.4B Turn/River deal; current international revenue mix.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (revenue by geography) and going-private 8-K/DEFM14A (financing sources); REPO-RATES — current 10Y UST already used as the analysis risk-free rate.

- **Lesson 05, Session 5 · Part 2 — "Netting Out the Default Spread — Risk-Free Rates in Difficult Currencies"** ([transcript](../01-foundations-and-discount-rates/lesson-05/session-5-part-2.md))
    - Quote: "The key to currency is to stay consistent, pick a currency and do both your returns and your hurdle rate in that currency."
    - Question for SWI: The repo's country-risk weighting bundles SWI's ~11% APAC/LatAm revenue into a single blended CRP. Should that slice instead get country-specific risk-free rates (netting local default spreads per this lesson's method) rather than folding everything back into one USD discount rate, and would that meaningfully move the already-computed weighted cost of capital?
    - Sources needed: Country-level (not just region-level) revenue breakdown for SWI's APAC/LatAm segment, local government bond rates and sovereign ratings for those specific countries.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 geographic revenue footnote (may only disclose region-level); REPO-COUNTRY-RISK — country ERP/default-spread data by country; REPO-SWI-VAL — Step 7 (existing region-level country-risk weighting).

### Lesson 06 — Equity Risk Premiums

- **Lesson 06, Session 6 · Part 1 — "Survey, Historical, and Implied Premiums — Three Ways to Estimate the ERP"** ([transcript](../01-foundations-and-discount-rates/lesson-06/session-6-part-1.md))
    - Quote: "That 10-year risk premium is pure noise, so I have to go back as far as I can because I need the data."
    - Question for SWI: The repo uses Damodaran's implied ERP (4.42%, July 2026) rather than a historical premium, consistent with the lesson's stated preference. But now that SolarWinds is privately held with no public trading in 2026, is a market-implied ERP still the theoretically correct input, or should the analysis shift to a PE-required-return benchmark — the lesson's own point that private status replaces the public ERP with "PE return hurdles"?
    - Sources needed: PE target IRR/required-return benchmarks for software buyouts of this size and hold period; Turn/River's stated fund return targets.
    - Where to find: DEAL-DOCS — Turn/River press release/fund materials on hold period and return profile; DAMODARAN-BLOG — local archive search for posts on private-company ERP/required-return adjustments; REPO-SWI-VAL — Step 6/7 existing implied-ERP calc, which already flags this private-status caveat.

- **Lesson 06, Session 6 · Part 2 — "Scaling Sovereign Default Spreads Into Country Equity Risk Premiums"** ([transcript](../01-foundations-and-discount-rates/lesson-06/session-6-part-2.md))
    - Quote: "I would argue that equities are riskier than bonds."
    - Question for SWI: The repo's Step 7 weighted-ERP calc applies Damodaran's country ERPs but doesn't specify whether they use the lesson's "scaled" approach (default spread × relative equity/bond volatility) versus the simpler "add the raw default spread" approach — which method underlies the country-risk dataset, and would switching methods meaningfully move SWI's ~11% APAC/LatAm-weighted CRP and its overall 4.56% weighted ERP?
    - Sources needed: Documentation of Damodaran's current country-risk-premium methodology and the raw default spreads/CDS spreads by country used to build it.
    - Where to find: REPO-COUNTRY-RISK (country-risk.json) — methodology notes/field definitions; DAMODARAN-SITE — live "Country Default Spreads and Risk Premiums" dataset; REPO-SWI-VAL — Step 7 existing weighted-ERP calc for comparison.

### Lesson 07 — Country Risk Premiums

- **Lesson 07, Session 7 · Part 1 — "Implied Equity Risk Premiums and Building Country Risk Off Them"** ([transcript](../01-foundations-and-discount-rates/lesson-07/session-7-part-1.md))
    - Quote: "a company's risk does not come from where it's incorporated but from where it does business."
    - Question for SWI: SWI is US-incorporated — but how much of its revenue is actually generated internationally, and should its equity risk premium reflect a revenue-weighted blend of country premiums rather than the flat US number?
    - Sources needed: SWI's revenue-by-geography breakdown; current implied ERP for the US and premiums for whatever countries appear.
    - Where to find: SEC-EDGAR (10-K FY2024, geographic revenue disclosure, typically in the segment/geographic-information footnote); DAMODARAN-SITE for the current implied ERP and country premium table; REPO-COUNTRY-RISK as a repo-cached fallback.

- **Lesson 07, Session 7 · Part 2 — "Company Equity Risk Premiums and Implied ERP"** ([transcript](../01-foundations-and-discount-rates/lesson-07/session-7-part-2.md))
    - Quote: "For every one of these companies, I'm looking past the country of incorporation to where they do business."
    - Question for SWI: What would a revenue-weighted equity risk premium look like for SWI given its actual customer/revenue geography, versus just using the flat US implied premium?
    - Sources needed: SWI 10-K/10-Q geographic revenue split (domestic vs. international, ideally by region); country-level ERP table.
    - Where to find: SEC-EDGAR (10-K geographic revenue note); DAMODARAN-SITE (current ERP by country); REPO-COUNTRY-RISK; REPO-SWI-VAL (check whether a cost-of-equity section already exists and what ERP it assumed).

### Lesson 08 — Regression Betas

- **Lesson 08, Session 8 · Part 1 — "Estimating Regression Betas — The Four Choices"** ([transcript](../01-foundations-and-discount-rates/lesson-08/session-8-part-1.md))
    - Quote: "There's a reason why services latch on to the S&P 500 for U.S. companies."
    - Question for SWI: Since SWI was delisted in April 2025, a regression run today has no live price data — what's the last usable 2–5 year pre-acquisition window, and does a regression beta from that stale window still represent SWI's risk today?
    - Sources needed: Historical daily/weekly SWI (NYSE: SWI) price and dividend data through the April 2025 delisting; S&P 500 index returns for the same window.
    - Where to find: NEWS-WEB / financial data providers (Yahoo Finance, Nasdaq historical data) for SWI's 2018–2025 price history; SEC-EDGAR (10-K/10-Q) confirms SWI paid no common dividend, simplifying the return calc.

- **Lesson 08, Session 8 · Part 2 — "Interpreting the Regression Beta — Jensen's Alpha, Standard Error, R-Squared"** ([transcript](../01-foundations-and-discount-rates/lesson-08/session-8-part-2.md))
    - Quote: "Standard errors are features, not bugs. They're part of the process, we've got to learn to deal with them."
    - Question for SWI: Using SWI's actual pre-delisting regression beta and its standard error, how wide is the confidence interval — and is it too wide to trust a standalone regression-based cost of equity for SWI?
    - Sources needed: SWI's regression beta output (beta, standard error, R-squared) against the S&P 500 over ~5 years of monthly returns pre-April 2025.
    - Where to find: NEWS-WEB / a financial data terminal (Bloomberg/Capital IQ) beta page if accessible; otherwise self-computed from the raw price data in Part 1's sources; REPO-BETAS gives an industry-level cross-check rather than a firm-specific number.

### Lesson 09 — Beta Fundamentals

- **Lesson 09, Session 9 · Part 1 — "Determinants of Beta and Regression Pitfalls — Stories Behind Company Betas"** ([transcript](../01-foundations-and-discount-rates/lesson-09/session-9-part-1.md))
    - Quote: "Companies that produce very discretionary products will have high betas."
    - Question for SWI: Is SWI's core product (IT infrastructure monitoring/observability software) a discretionary or non-discretionary spend for its customers, and does that explain where its historical beta sat relative to peers like Datadog and Dynatrace?
    - Sources needed: A qualitative read of SWI's product line (mission-critical monitoring vs. discretionary IT spend) from its business description; comparable betas for observability/IT-ops peers.
    - Where to find: SEC-EDGAR (10-K Item 1, Business); PEER-FILINGS for comparable public peers' betas and business descriptions; REPO-BETAS for the broader software industry beta as a sanity check.

- **Lesson 09, Session 9 · Part 2 — "The Three Determinants of Beta — Business, Operating Leverage, Financial Leverage"** ([transcript](../01-foundations-and-discount-rates/lesson-09/session-9-part-2.md))
    - Quote: "It makes your equity earnings much more volatile and through that, it makes your beta higher."
    - Question for SWI: Given SWI's LBO-era debt load, how much of its (formerly public) equity beta was inflated by financial leverage versus its underlying unlevered business beta?
    - Sources needed: SWI's total debt and market value of equity (last public-era market cap) to compute debt-to-equity; marginal tax rate; unlevered beta for the observability/IT-ops software sector.
    - Where to find: SEC-EDGAR (10-K FY2024 balance sheet for total debt; income statement for effective/marginal tax rate; last 10-K/DEF14A for share count and price); REPO-BETAS (Damodaran sector unlevered betas — software/IT services).

### Lesson 10 — Bottom-up Betas

- **Lesson 10, Session 10 · Part 1 — "Bottom-Up Betas — Why They Beat Regression"** ([transcript](../01-foundations-and-discount-rates/lesson-10/session-10-part-1.md))
    - Quote: "A bottom-up beta is more precise, more forward-looking, and more dynamic than a regression beta."
    - Question for SWI: Is SWI single-business enough (core: IT infrastructure monitoring/observability) to use one industry-average unlevered beta directly, or does it have distinct enough product lines (legacy monitoring vs. the newer AIOps/Squadcast observability push) to warrant a segment-weighted bottom-up beta like Disney's five-business breakdown?
    - Sources needed: SWI's segment/product-line revenue breakdown, if disclosed; a list of comparable public companies for each product line.
    - Where to find: SEC-EDGAR (10-K Item 1 and segment footnote — check whether SWI still reports as a single operating segment for FY2024); PEER-FILINGS (Datadog, Dynatrace, PagerDuty) for unlevered betas by business line.

- **Lesson 10, Session 10 · Part 2 — "Bottom-Up Beta for Disney by Business — Aggregating and Levering"** ([transcript](../01-foundations-and-discount-rates/lesson-10/session-10-part-2.md))
    - Quote: "Because the movie business is riskier than Disney as a company, you should demand much more of it, a higher hurdle rate."
    - Question for SWI: If SWI's newer AI-driven observability/AIOps initiatives (e.g., the Squadcast acquisition) are riskier than its legacy monitoring business, should a project-level hurdle rate for that segment exceed the company-wide cost of equity derived from peer betas?
    - Sources needed: Revenue/segment split between legacy monitoring and newer AIOps/observability lines; peer betas for each sub-category.
    - Where to find: SEC-EDGAR (10-K Item 1 business/product discussion); PEER-FILINGS for comparable pure-plays (Dynatrace/Datadog skew toward modern observability); DEAL-DOCS (Turn/River's stated rationale may discuss strategic segments).

### Lesson 11 — The "Right" Beta

- **Lesson 11, Session 11 · Part 1 — "Bottom-Up Betas Across Companies — Multi- and Single-Business Cases"** ([transcript](../01-foundations-and-discount-rates/lesson-11/session-11-part-1.md))
    - Quote: "My sample size would be far too small if I focused just on Brazilian companies."
    - Question for SWI: Since SWI is essentially single-business, should its unlevered beta be built from a *global* sample of observability/IT-ops SaaS peers rather than staying US-only, the way Damodaran went global for Tata Motors and Vale to get sample size?
    - Sources needed: A list of global (not just US) publicly traded observability/ITSM/network-monitoring peers, their regression betas, debt-to-equity ratios, and cash balances.
    - Where to find: PEER-FILINGS (expand beyond DDOG/DT/PD to any listed international peers); DAMODARAN-SITE global industry beta datasets, broader than the repo's cached snapshot.

- **Lesson 11, Session 11 · Part 2 — "Betas and Cost of Equity for Private Businesses — Bookscape and Total Beta"** ([transcript](../01-foundations-and-discount-rates/lesson-11/session-11-part-2.md))
    - Quote: "You cannot use a market beta to come up with the cost of equity because that market beta focuses only on the risk you cannot diversify away."
    - Question for SWI: Now that SWI is privately held by Turn/River Capital rather than diversified public shareholders, should its cost of equity going forward use a "total beta" adjustment (market beta ÷ √R²), the way Damodaran did for Bookscape?
    - Sources needed: SWI's last public-era regression beta and R-squared (pre-April 2025); how diversified Turn/River's own portfolio is (a diversified PE fund holding many companies argues against needing the total-beta adjustment).
    - Where to find: NEWS-WEB / financial data terminal for SWI's last regression beta and R² before delisting; Turn/River's own investor materials (fund size, number of portfolio companies) via DEAL-DOCS or NEWS-WEB.

### Lesson 12 — Debt: Measure and Cost

- **Lesson 12, Session 12 · Part 1 — "Cost of Debt and What Counts as Debt"** ([transcript](../01-foundations-and-discount-rates/lesson-12/session-12-part-1.md))
    - Quote: "All interest-bearing obligations are, obviously, debt. All lease commitments are debt."
    - Question for SWI: What does SWI's total debt load actually include once lease commitments are counted per Damodaran's three criteria (fixed payment, tax-deductible, loss-of-control on default) — not just what's labeled "debt" on the balance sheet?
    - Sources needed: SWI's 10-K balance sheet (term loan/notes) and lease footnote (operating lease right-of-use assets/liabilities under ASC 842).
    - Where to find: SEC-EDGAR (10-K FY2024 — Debt note and Leases note).

- **Lesson 12, Session 12 · Part 2 — "From Ratings to Cost of Debt — Actual vs. Synthetic Ratings"** ([transcript](../01-foundations-and-discount-rates/lesson-12/session-12-part-2.md))
    - Quote: "If you have an actual rating, don't go looking for trouble. Just use the actual rating."
    - Question for SWI: Does SWI carry an actual credit rating on its LBO-era term loan/notes, or does it need a synthetic rating built from its interest coverage ratio — and how did either change once Turn/River's 2025 acquisition likely added leverage?
    - Sources needed: SWI's credit rating, if any (S&P/Moody's on its credit facility); operating income and interest expense (for interest coverage ratio); current default spread by rating.
    - Where to find: SEC-EDGAR (10-K Debt note may disclose facility ratings; income statement for interest coverage inputs); NEWS-WEB for S&P/Moody's rating actions around the 2025 Turn/River deal financing; DAMODARAN-SITE for the current interest-coverage-to-rating lookup table (repo mirror excluded — go direct).

## Module 2 — Investment Returns & Financing (Lessons 13–19)

### Lesson 13 — Cost of Capital Weights (Market vs. Book Value)

- **Lesson 13, Session 13 · Part 1 — "Why Book Value Weights Don't Hold Up: Converting Book Debt to Market Debt"** ([transcript](../02-investment-returns-and-financing/lesson-13/session-13-part-1.md))
    - Quote: "There is no good reason for using book value weights."
    - Question for SWI: SWI's cost-of-capital weights in the repo's existing analysis treat the First Lien Term Loan as book ≈ market (floating rate), but do they capture SWI's operating lease commitments as debt the way Damodaran's Disney bond-equivalent method does — and if converted to a present value at SWI's pre-tax cost of debt, would adding lease-debt shift the 76.9%/23.1% equity/debt weighting meaningfully?
    - Sources needed: FY2024 lease footnote (future minimum lease payments by year, weighted-average remaining lease term/discount rate) and the pre-tax cost of debt to discount them.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Notes to Financial Statements (Leases); REPO-SWI-VAL (Step 12 debt figures, for the discount rate to apply).

- **Lesson 13, Session 13 · Part 2 — "Bringing Cost of Equity and Debt Together: WACC as Hurdle Rate"** ([transcript](../02-investment-returns-and-financing/lesson-13/session-13-part-2.md))
    - Quote: "That cost of capital is going to become a hurdle rate for your company."
    - Question for SWI: SolarWinds reports as a single segment, so the repo uses one company-wide WACC (10.33%) — but given the lecture's divisional cost-of-capital approach (different hurdle rates for Disney's theme parks vs. gaming), should legacy on-prem/Orion monitoring and newer SaaS/observability offerings inside SWI actually carry different hurdle rates given their different risk and growth profiles?
    - Sources needed: Product-line revenue/margin split (even if not formally segment-reported) and comparable pure-play betas for on-prem vs. cloud-native observability peers.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 1 Business (product description); PEER-FILINGS (Datadog, Dynatrace 10-Ks for product-line economics); REPO-BETAS (industry-betas.json, software subsector splits).

### Lesson 14 — Cash Flows vs. Accounting Earnings (Return on Invested Capital)

- **Lesson 14, Session 14 · Part 1 — "Show Me the Money: From Accounting Earnings to Cash Flows"** ([transcript](../02-investment-returns-and-financing/lesson-14/session-14-part-1.md))
    - Quote: "It's not show me the accounting income, it's not show me the earnings, it's show me the money."
    - Question for SWI: SWI carries a large EBIT-to-Adjusted-EBITDA gap ($208.4M vs. $384.7M per the repo, driven largely by amortization of intangibles from the 2016 LBO) — applying the lecture's three adjustments (add back D&A, subtract capex, subtract change in working capital), what is SWI's actual FY2024 free cash flow to the firm, and how much of that EBIT/EBITDA gap is genuinely non-cash amortization versus real, ongoing capitalized R&D needs?
    - Sources needed: FY2024 Consolidated Statement of Cash Flows (D&A add-back, capex line) and balance sheet working-capital accounts (AR, AP, deferred revenue).
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Consolidated Statement of Cash Flows and Item 7 MD&A (non-GAAP Adjusted EBITDA reconciliation).

- **Lesson 14, Session 14 · Part 2 — "Return on Invested Capital vs. Cost of Capital, and the Country Risk Premium"** ([transcript](../02-investment-returns-and-financing/lesson-14/session-14-part-2.md))
    - Quote: "It looks like Disney is generating a 4.8% excess return over and above its cost of capital."
    - Question for SWI: Running the same excess-return test the lecture runs for Disney/Vale/Baidu — what is SWI's company-wide return on invested capital (after-tax operating income ÷ book invested capital) for FY2024, and does it clear the repo's 10.33% WACC, and does the answer flip materially depending on whether 2016-LBO-vintage goodwill/intangibles are included in invested capital?
    - Sources needed: After-tax operating income (EBIT × (1 − tax rate)) and total invested capital, computed both with and without acquisition-related goodwill/intangibles.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Balance Sheet (goodwill/intangibles line) and Income Statement; REPO-SWI-VAL (WACC = 10.33%, Step 12 EBIT figure).

### Lesson 15 — Incremental Cash Flows and Time-Weighted Returns

- **Lesson 15, Session 15 · Part 1 — "Sunk Costs, Non-Incremental G&A, and Time-Weighting Cash Flows"** ([transcript](../02-investment-returns-and-financing/lesson-15/session-15-part-1.md))
    - Quote: "The first rule in capital budgeting is you have sunk cost, money were already spent, don't consider them."
    - Question for SWI: Using the lecture's "what happens if I take it / what happens if I don't" test, how much of SWI's pre-close diligence and integration spend on the Squadcast acquisition (~March 2025) should be excluded as a sunk cost when evaluating the incremental cash-flow return on continued observability-platform integration, and how much corporate G&A allocated to legacy Orion support is genuinely non-incremental?
    - Sources needed: Disclosed Squadcast deal/integration costs to date; any product-line allocation of corporate G&A that would reveal what's truly incremental versus reallocated elsewhere.
    - Where to find: SEC-EDGAR — SWI 8-K (Squadcast acquisition, ~March 2025) and 10-K FY2024 Item 7 MD&A (M&A/integration cost discussion); REPO-SWI-VAL (Step 4, stated objectives re: Squadcast).

- **Lesson 15, Session 15 · Part 2 — "NPV, IRR, and Terminal Value via the Growing Perpetuity"** ([transcript](../02-investment-returns-and-financing/lesson-15/session-15-part-2.md))
    - Quote: "If you take a project with an NPV of $3.3 billion, your value will increase by $3.3 billion."
    - Question for SWI: What terminal-value growth rate is defensible for SWI's SaaS/observability-transition cash flows beyond a 10-year explicit forecast, given intensifying disruption risk from cloud-native competitors (Datadog, Dynatrace), and does the Turn/River deal's fairness-opinion DCF use a terminal growth rate consistent with the lecture's constraint that it cannot exceed overall economic growth?
    - Sources needed: Banker's DCF assumptions (discount rate, terminal growth rate) from the merger proxy; peer long-term growth assumptions for comparison.
    - Where to find: DEAL-DOCS (Turn/River DEFM14A fairness opinion DCF); PEER-FILINGS (DDOG, DT growth-rate context); DAMODARAN-SITE (long-term GDP growth constraint data).

### Lesson 16 — Currency Consistency and Uncertainty in Investment Analysis

- **Lesson 16, Session 16 · Part 1 — "Currency Consistency: Redoing the DCF in a Foreign Currency"** ([transcript](../02-investment-returns-and-financing/lesson-16/session-16-part-1.md))
    - Quote: "A good project in U.S. dollars should remain a good project in nominal Reais."
    - Question for SWI: SWI derives roughly 31% of revenue internationally (EMEA/APAC per the repo) — if a hypothetical EMEA-currency investment (e.g., a European data-center buildout) were evaluated in EUR using purchasing power parity to project the EUR/USD path, would a nominal-EUR DCF (at a EUR-adjusted WACC) reproduce the same NPV as the repo's existing USD analysis, and what US–Eurozone inflation differential would that conversion require?
    - Sources needed: US and Eurozone inflation forecasts/differential; SWI's EUR-denominated revenue and cost mix.
    - Where to find: REPO-RATES (market-rates.json, US rates); DAMODARAN-SITE or NEWS-WEB (Eurozone/ECB inflation outlook); SEC-EDGAR — SWI 10-K FY2024 (revenue-by-geography footnote).

- **Lesson 16, Session 16 · Part 2 — "Payback, What-If Analysis, Monte Carlo, and the Hedging Decision"** ([transcript](../02-investment-returns-and-financing/lesson-16/session-16-part-2.md))
    - Quote: "Does hedging that risk create a benefit that is greater than the cost?"
    - Question for SWI: Post-SUNBURST, SolarWinds significantly increased cybersecurity spend and governance oversight (Cybersecurity Committee) — applying the lecture's hedging cost/benefit test, did that incremental risk-mitigation spend since 2021 produce benefits (customer retention, avoided reputational/legal costs, a lower perceived-risk cost of capital) that exceeded its cost, or was it spend the market could have priced in more cheaply some other way?
    - Sources needed: Disclosed cybersecurity opex trend since 2021; customer churn/retention data pre- vs. post-SUNBURST; disclosed total cost of the SUNBURST incident (legal, remediation) vs. ongoing security spend.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2021–FY2024 (MD&A cybersecurity expense discussion; Legal Proceedings/SUNBURST litigation costs); SEC-EDGAR — DEF 14A (Cybersecurity Committee charter); NEWS-WEB (analyst estimates of total SUNBURST cost).

### Lesson 17 — The Financing Principle: Debt vs. Equity Trade-Off

- **Lesson 17, Session 17 · Part 1 — "Debt vs. Equity and the Corporate Life Cycle"** ([transcript](../02-investment-returns-and-financing/lesson-17/session-17-part-1.md))
    - Quote: "One of the most common problems among corporations is corporations that refuse to act their age."
    - Question for SWI: SWI is a mature, low-growth (~5% YoY), high-margin (48% Adjusted EBITDA margin) software company that nonetheless carries leverage inherited from a 2016 Thoma Bravo/Silver Lake LBO rather than organically chosen debt — per the life-cycle framework, does SWI's current ~23–30% debt weight look mature-appropriate, or is it a legacy LBO artifact rather than a level SWI's own cash-flow stability would independently justify?
    - Sources needed: SWI's debt ratio pre-2016 LBO, post-LBO, and at IPO (2018) vs. current; mature-software peer debt ratios for comparison.
    - Where to find: SEC-EDGAR — SWI historical 10-Ks/S-1 (2018 IPO prospectus) for pre-existing leverage; PEER-FILINGS (Dynatrace, other mature software peers, debt ratios); REPO-SWI-VAL (current debt figures).

- **Lesson 17, Session 17 · Part 2 — "The Trade-Off on Debt: Tax Benefits, Discipline, Bankruptcy and Agency Costs"** ([transcript](../02-investment-returns-and-financing/lesson-17/session-17-part-2.md))
    - Quote: "The biggest plus of using debt is the tax code rewards you for borrowing money."
    - Question for SWI: Given SWI's 25% marginal tax rate (per the repo) and its intangible-heavy balance sheet (making lenders less able to monitor collateral, per the lecture's agency-cost point) now that it's a privately held Turn/River portfolio company needing continued SaaS-transition R&D flexibility — do the tax benefits of the ~$1.235B term loan actually exceed its agency costs (covenants) and lost-flexibility costs?
    - Sources needed: Term loan covenant terms (financial maintenance covenants, restricted payments/R&D baskets); R&D spend trend; intangible assets as a percentage of total assets.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (debt footnote covenants; balance sheet intangibles/goodwill %); DEAL-DOCS (Turn/River acquisition financing/credit agreement terms, if disclosed via 8-K).

### Lesson 18 — The Cost of Capital Approach to the Optimal Debt Ratio

- **Lesson 18, Session 18 · Part 1 — "The Cost of Capital Approach to the Optimal Debt Ratio"** ([transcript](../02-investment-returns-and-financing/lesson-18/session-18-part-1.md))
    - Quote: "The optimal debt ratio for this company, if I stay true to the notion of minimizing cost of capital, is 40% debt."
    - Question for SWI: Running the same cost-of-capital-schedule exercise (levering SWI's unlevered beta of 1.27 via Hamada at each debt ratio, and estimating synthetic ratings/cost of debt from interest coverage at each level per Damodaran's lookup table), where does SWI's WACC bottom out — and does its current ~23–30% debt weight sit below, at, or above that minimizing point?
    - Sources needed: SWI's EBIT/EBITDA held constant under the "recapitalization" assumption at each hypothetical debt level; Damodaran's current interest-coverage-to-rating lookup table (smaller-firm version); unlevered beta.
    - Where to find: LESSON-MATERIALS (lesson-18 spreadsheet-cost-of-capital-optimal.md — the optimal-debt-ratio template); REPO-BETAS (industry-betas.json); REPO-SWI-VAL (Step 10 unlevered beta 1.2725, Step 12 EBIT $208.4M); DAMODARAN-SITE (current synthetic rating table).

- **Lesson 18, Session 18 · Part 2 — "The Iterative Rating Loop and the Kink in the Cost of Capital Curve"** ([transcript](../02-investment-returns-and-financing/lesson-18/session-18-part-2.md))
    - Quote: "My advice to companies is if you're going to make a mistake, be under-levered rather than over-levered."
    - Question for SWI: The repo's own Step 12 shows SWI's EBIT-based synthetic rating (B-/B3) sitting two notches below its actual B+ rating because EBITDA-based coverage is more favorable — when running the iterative interest-coverage-to-rating loop across hypothetical debt ratios for SWI, should the lookup use EBIT-based or EBITDA-based coverage, since that choice could shift where SWI's optimal-debt "kink" appears?
    - Sources needed: Damodaran's current interest-coverage-to-rating lookup table (EBIT-based and any EBITDA-adjusted variant); rating agencies' actual methodology commentary on SWI post-Turn/River.
    - Where to find: DAMODARAN-SITE (live synthetic rating/ratings lookup table); SEC-EDGAR — SWI 8-K (S&P/Moody's rating action rationale post-Turn/River deal); REPO-SWI-VAL (Step 12, EBIT vs. EBITDA divergence discussion).

### Lesson 19 — Follow-Up: Value Impact and Stress-Testing the Optimal Debt Ratio

- **Lesson 19, Session 19 · Part 1 — "From Lower Cost of Capital to Real Value: Financing Savings and the Buyback Premium"** ([transcript](../02-investment-returns-and-financing/lesson-19/session-19-part-1.md))
    - Quote: "That 19.6 billion is not value creation in the traditional sense, it's a value transfer."
    - Question for SWI: SWI is now private (Turn/River-owned, no public buyback mechanism) — how should the lecture's "annual financing savings" value-transfer calculation be reframed for a PE-owned company (e.g., via a dividend recapitalization to the sponsor instead of a share buyback), and what would that annual financing-savings figure be using SWI's current $1.235B term loan, its actual WACC (10.33%), and its optimal WACC from the Lesson 18 exercise?
    - Sources needed: SWI's current enterprise value (Turn/River deal EV or updated comps, since it's private); the WACC delta between actual and optimal; any post-acquisition recapitalization/dividend activity.
    - Where to find: DEAL-DOCS (Turn/River acquisition EV ~$4.4B); REPO-SWI-VAL (WACC 10.33%); NEWS-WEB (any post-2025 dividend recap news on Turn/River-owned SolarWinds).

- **Lesson 19, Session 19 · Part 2 — "Breakeven Buyback Pricing, Stress-Testing the Optimal, and Rating Constraints"** ([transcript](../02-investment-returns-and-financing/lesson-19/session-19-part-2.md))
    - Quote: "Just because of excess debt capacity doesn't mean they can use it to do whatever they want."
    - Question for SWI: Applying the lecture's operating-income stress test (dropping Disney's operating income 10/20/30% to see if the optimal debt ratio holds) to SWI — whose FY2024 EBIT of $208.4M gives only 1.95x interest coverage against $107.2M of interest expense (per the repo) — how much of an operating-income decline would push SWI toward covenant breach or a rating downgrade, and is SWI's current leverage already this fragile at its existing, sub-optimal debt level?
    - Sources needed: SWI's historical operating-income volatility across past downturns; term loan covenant thresholds (minimum coverage triggers); rating agency downside scenarios.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (debt footnote covenants) and historical 10-Ks 2019–2024 (EBIT trend across any downturn); REPO-SWI-VAL (Step 12, 1.95x interest coverage).

## Module 3 — Financing Mix & Dividends (Lessons 20–26)

### Lesson 20 — Weak Links in the Cost-of-Capital Approach & Optimal Debt Ratios Across Company Types

- **Lesson 20, Session 20 · Part 1 — "Letting Operating Income React to Distress: Adapting the Model for Disney, Tata Motors, and Vale"** ([transcript](../03-financing-mix-and-dividends/lesson-20/session-20-part-1.md))
    - Quote: "In other words, the caution I'd added earlier about it's better to be underlevered than overlevered, applies in spades now."
    - Question for SWI: SWI's own actual rating (B+) sits two notches above its EBIT-based synthetic rating (B3/B-) per the repo's existing valuation work — how much would a further downgrade actually depress SWI's operating income through customer flight, given its security-sensitive federal/enterprise base already rattled once by SUNBURST? Is 5% (Disney's low-indirect-cost case) or something closer to 15% the right distress-sensitivity assumption for SWI?
    - Sources needed: SWI's operating income/revenue trend immediately around the Dec 2020 SUNBURST disclosure (a real-world proxy for a distress/reputational shock), plus industry benchmarks for indirect bankruptcy/distress costs in security-sensitive SaaS.
    - Where to find: SEC-EDGAR — SWI 8-Ks (Dec 2020 SUNBURST disclosures) and 10-Ks FY2020–FY2022 (revenue/customer-count trend); REPO-SWI-VAL (existing B+ vs. B3/B- synthetic-rating gap, Step 12); DAMODARAN-BLOG (search "indirect bankruptcy cost" / "cost of distress" posts) for sector-level distress-cost benchmarks.

- **Lesson 20, Session 20 · Part 2 — "The Four Drivers of Optimal Leverage: Tax Rate, Cash-Flow Capacity, Risk, and the Relative Price of Debt vs. Equity"** ([transcript](../03-financing-mix-and-dividends/lesson-20/session-20-part-2.md))
    - Quote: "If you pay no taxes, if you have zero tax rate, debt cannot help you."
    - Question for SWI: The lesson ties optimal leverage to EBIT as a percent of enterprise value. SWI's FY2024 EBIT ($208.4M per REPO-SWI-VAL) against its take-private enterprise value (~$4.4B) gives a fairly low EBIT/EV ratio — does that argue SWI's actual ~23% adjusted debt-to-value (per REPO-SWI-VAL) is already near or above what this driver would support, or does it have more room given a 25% marginal tax rate? How does that ratio compare to peer observability SaaS names that carry far less debt?
    - Sources needed: SWI's EBIT/EV ratio computed consistently across FY2018–FY2024 (post-IPO), and the same ratio for comparable public SaaS peers to benchmark against.
    - Where to find: REPO-SWI-VAL (SWI EBIT $208.4M, adjusted debt $1,317M, D/V 23.1%, marginal tax rate 25% — Steps 11–13); SEC-EDGAR — SWI 10-Ks FY2018–FY2024 for historical EBIT; PEER-FILINGS (DDOG, DT, PD 10-Ks/10-Qs for EBIT and market cap to build comparable EBIT/EV ratios).

### Lesson 21 — Adjusted Present Value and the Relative Approach to Debt Ratios

- **Lesson 21, Session 21 · Part 1 — "APV: Unlevered Firm Value, Tax Benefits, and Expected Bankruptcy Costs (Disney's 40% Optimal, Revisited)"** ([transcript](../03-financing-mix-and-dividends/lesson-21/session-21-part-1.md))
    - Quote: "As you borrow more money, you're increasing the probability that you will go bankrupt, right?"
    - Question for SWI: Disney's APV analysis used a 25% cost-of-bankruptcy assumption picked "right in the middle" of a 10%–40% range with, in the lecturer's own words, "no solid reason." For SWI — an intangible-asset-heavy SaaS business rather than a tangible-asset one — what's the defensible indirect-bankruptcy-cost assumption, and does SUNBURST (a real distress-adjacent reputational shock, absent balance-sheet distress) give a better empirical anchor than assuming a mid-range number?
    - Sources needed: Comparable-company or sector-level indirect bankruptcy-cost estimates for software/SaaS firms, plus concrete SUNBURST-era customer attrition/revenue data to calibrate an SWI-specific figure.
    - Where to find: DAMODARAN-SITE / DAMODARAN-BLOG (bankruptcy/distress-cost data by industry); SEC-EDGAR — SWI 8-Ks and 10-Ks FY2020–FY2021 (customer/revenue impact disclosures following SUNBURST); NEWS-WEB for contemporaneous analyst commentary on customer churn.

- **Lesson 21, Session 21 · Part 2 — "The Relative Approach: Comparing to Sector Averages and Regression-Based Refinement"** ([transcript](../03-financing-mix-and-dividends/lesson-21/session-21-part-2.md))
    - Quote: "By staying close to the sector, you're, in effect, making sure that if you make a mistake, you'll always have lots of company."
    - Question for SWI: SWI's ~23% adjusted D/V (REPO-SWI-VAL) is a legacy of its 2016 LBO capital structure. How does that compare to the observability/IT-ops SaaS peer set (DDOG, DT, PD), most of which run near-zero leverage as newly public growth companies — and does that sector comparison strengthen or contradict the intrinsic cost-of-capital/APV read on SWI's leverage, the same "convenient consensus vs. contradiction" test the lesson runs for Disney vs. Vale?
    - Sources needed: Peer debt-to-capital and debt-to-EV ratios for DDOG, DT, PD from a comparable fiscal period; a narrower "observability SaaS" sector average rather than Damodaran's broad software-industry average.
    - Where to find: PEER-FILINGS (DDOG/DT/PD 10-Ks and 10-Qs for debt and market cap); REPO-BETAS (Damodaran's broad software-industry debt-ratio averages, as a fallback since no observability-specific subsector exists); REPO-SWI-VAL for SWI's own current debt-ratio figures to run the comparison against.

### Lesson 22 — Moving to the Optimal Debt Ratio

- **Lesson 22, Session 22 · Part 1 — "Under-Levered vs. Over-Levered: Takeover Risk, Bankruptcy Threat, and the 'Good Projects' Test"** ([transcript](../03-financing-mix-and-dividends/lesson-22/session-22-part-1.md))
    - Quote: "Having too little debt might make you the target of a hostile acquisition."
    - Question for SWI: SWI was acquired (again) by Turn/River in April 2025 while carrying only ~23% adjusted D/V and a B+ rating — fitting the lesson's profile of an under-levered acquisition target. Using the lesson's own diagnostic tools (Jensen's alpha / stock-performance history, size, insider concentration), was SWI's under-leverage relative to its intrinsic debt capacity a material driver of the take-private, and could a pre-emptive debt-funded buyback have defended against it the way the lesson recommends for vulnerable under-levered firms?
    - Sources needed: SWI total shareholder return/Jensen's alpha 2018–2025 vs. a market or sector benchmark; insider/institutional ownership concentration; deal background narrative on valuation and timing rationale.
    - Where to find: SEC-EDGAR — SWI 10-Ks/DEF 14A proxies (stock performance graph, beneficial ownership tables) and the going-private Schedule 13E-3/DEFM14A ("Background of the Merger" section, which narrates rationale and timing); REPO-RATES (risk-free rate history for the Jensen's alpha calc); DEAL-DOCS (Turn/River press release + fairness opinion) for the deal's stated premium/rationale; NEWS-WEB for analyst commentary on whether the take-private was opportunistic.

### Lesson 23 — Designing the Right Type of Financing

- **Lesson 23, Session 23 · Part 1 — "Matching Debt to Assets: The Five Questions That Design the 'Perfect' Financing"** ([transcript](../03-financing-mix-and-dividends/lesson-23/session-23-part-1.md))
    - Quote: "You'd like to issue debt that behaves like equity, that gives you the flexibility of equity while giving you the tax benefits of debt."
    - Question for SWI: SWI's First Lien Term Loan ($1.235B per REPO-SWI-VAL) is floating-rate — which the lesson says only fits a company with real pricing power, so that cash flows rise with the same base rate driving up interest payments. Given SWI sells multi-year subscription contracts with negotiated, largely fixed pricing rather than continuous inflation pass-through, does SWI actually have the pricing-power profile floating-rate debt requires, or is its debt structurally mismatched to its cash flows?
    - Sources needed: Actual coupon/rate-reset terms of SWI's term loan (SOFR-linked spread, reset frequency); average subscription contract length and any price-escalation/CPI-linked clauses in customer agreements.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 debt footnote (term loan rate terms) and revenue-recognition/contract-terms notes (Item 8); REPO-SWI-VAL (existing $1,235M floating-rate term loan detail, Step 12); LESSON-MATERIALS (this lesson's slides.md, likely holding Damodaran's duration/currency/rate-type scoring framework) for the exact rubric to apply.

- **Lesson 23, Session 23 · Part 2 — "Fixing Debt/Asset Mismatches: Swaps vs. New-Project Financing, Applied to Disney, Vale, Tata Motors, and Baidu"** ([transcript](../03-financing-mix-and-dividends/lesson-23/session-23-part-2.md))
    - Quote: "There are two ways in which companies can adjust debt that doesn't match."
    - Question for SWI: Disney's FX mismatch (18% foreign revenue vs. only 5.49% FX-denominated debt) is the model case here. What is SWI's actual international revenue mix, and is its (presumably all-USD) term loan similarly under-hedged against a meaningful non-US enterprise/government customer base — a mismatch now potentially harder to unwind given reduced disclosure as a private Turn/River-owned entity?
    - Sources needed: SWI's revenue-by-geography breakdown; confirmation of the term loan's currency denomination and any disclosed FX hedging program.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 7A (market-risk disclosures covering geographic revenue mix and FX hedging) and debt footnote (loan currency); REPO-SWI-VAL for the $1,235M debt figure to confirm the currency assumption being tested.

### Lesson 24 — no transcript available (not on channel)

- Not distributed on the course's video channel; topic unknown. Check `lesson-overview.md` and `slides.md` in `03-corporate-finance/03-2-course-content/03-financing-mix-and-dividends/lesson-24/` if/when materials become available — do not fabricate content for this lesson.

### Lesson 25 — Three Schools of Thought on Dividends; Good and Bad Reasons to Pay Them

- **Lesson 25, Session 25 · Part 1 — "Three Schools of Thought on Dividends (Neutral, Bad, Good) and the Ex-Dividend Day as a Tax-Preference Test"** ([transcript](../03-financing-mix-and-dividends/lesson-25/session-25-part-1.md))
    - Quote: "The more the tax rates diverge, the more dividends will matter."
    - Question for SWI: SWI paid no common dividend across its public life, prioritizing debt paydown under Silver Lake/Thoma Bravo LBO-sponsor control — so there's no ex-dividend day to observe. Given Silver Lake's ~75% stake (per REPO-SWI-VAL) sits inside fund vehicles with different tax treatment than a typical taxable retail or index-fund holder, does the lesson's "three schools of thought" framework even apply to a company this closely and unusually held, or does the concentrated-ownership structure make the whole question moot?
    - Sources needed: Confirmation SWI paid zero common dividends throughout 2018–2025; detail on Silver Lake's/Thoma Bravo's fund structure and typical tax treatment of fund-level distributions vs. a retail dividend clientele.
    - Where to find: SEC-EDGAR — SWI 10-Ks, Item 5 ("Market for Registrant's Common Equity," dividend policy statement) and DEF 14A (beneficial ownership table, Silver Lake/Thoma Bravo fund entities); REPO-SWI-VAL (existing governance section on the ~75% Silver Lake stake) for cross-reference.

- **Lesson 25, Session 25 · Part 2 — "Bad Reasons vs. Good Reasons to Pay Dividends: Clientele, Signaling, and Wealth Transfer From Bondholders"** ([transcript](../03-financing-mix-and-dividends/lesson-25/session-25-part-2.md))
    - Quote: "When you pay a dividend, you might be transferring wealth from the bondholders or lenders to the equity investors."
    - Question for SWI: SWI's zero-dividend, debt-paydown-first policy under PE-sponsor control could reflect this wealth-transfer logic running in reverse — i.e., are SWI's term-loan lenders the protected party here, with covenant-restricted distribution capacity a deliberate lender-favorable term? Would even a modest dividend initiation have doubled as the "bad signal" the lesson describes (implying slower growth) on top of triggering the bondholder wealth-transfer effect, given SWI's still-active subscription transition?
    - Sources needed: Actual restrictive covenants on SWI's First Lien Term Loan governing dividends/distributions; any management/board commentary explicitly justifying the no-dividend capital-allocation policy.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (Item 5 dividend policy statement; debt footnote/credit agreement exhibit for distribution covenants) and MD&A capital-allocation discussion; DEF 14A for any board-level rationale.

### Lesson 26 — Assessing Dividend Policy and Free Cash Flow to Equity

- **Lesson 26, Session 26 · Part 1 — "FCFE as the 'Potential Dividend': Computing It and Reading Disney's Debt-Funded Payout Gap"** ([transcript](../03-financing-mix-and-dividends/lesson-26/session-26-part-1.md))
    - Quote: "If you're already in a hole, you need to stop digging."
    - Question for SWI: Applying the lesson's FCFE formula (net income + D&A − CapEx − ΔWC − debt repayments + new debt issuance) to SWI's FY2024 statement of cash flows, what was SWI's actual FCFE — and does its payout (zero dividends, presumably net debt paydown) fall short of, match, or exceed that number, the same three-way test the lesson runs for Disney (paid more than operating FCFE, funded by added debt) vs. Bookscape/Baidu (paid nothing)?
    - Sources needed: SWI FY2024 (and prior years) statement of cash flows — net income, D&A, CapEx, working-capital changes, debt issuance/repayment lines.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Consolidated Statement of Cash Flows (Item 8); REPO-SWI-VAL (existing EBIT $208.4M / adjusted EBITDA $384.7M figures, Step 11) as a cross-check on the FCFE build.

- **Lesson 26, Session 26 · Part 2 — "Cash Accumulation, FCFE for Banks, and the Chrysler/Kerkorian Case: What Happens When Payout Falls Short of Capacity"** ([transcript](../03-financing-mix-and-dividends/lesson-26/session-26-part-2.md))
    - Quote: "The point I'm trying to make is when you hold back cash, your cash balance balloons out."
    - Question for SWI: With a 48% adjusted-EBITDA margin and modest CapEx needs (per REPO-SWI-VAL), did SWI actually build up a large cash balance in any year of its public life rather than paying it out or paying down debt — and if so, did Silver Lake (as ~75% controlling holder) function as its own internal "activist," pushing debt reduction instead of letting cash accumulate the way Chrysler did before Kerkorian intervened in 1994?
    - Sources needed: SWI's year-by-year cash-and-equivalents balance FY2019–FY2024; FCFE computed for the same years to see whether cash consistently under- or over-shot what was paid out or used for debt paydown.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2019–FY2024, balance sheets (cash & equivalents line item) and selected financial data; REPO-SWI-VAL for FY2024 baseline EBIT/EBITDA/debt figures to cross-reference the trend.

## Module 4 — Dividends & Valuation (Lessons 27–36)

### Lesson 27 — Dividend Policy Assessment

- **Lesson 27, Session 27 · Part 1 — "Companies Earn the Right to Accumulate Cash: The Dividend Assessment Matrix"** ([transcript](../04-dividends-and-valuation/lesson-27/session-27-part-1.md))
    - Quote: "Companies earn the right to accumulate cash. They're not endowed with that right."
    - Question for SWI: Applying the trust test from the Disney Eisner→Iger case (ROIC vs. WACC plus stock-return track record before vs. after a CEO change), does SWI's performance under Ramakrishna (2021–2024, post-SUNBURST) look more like pre-2003 Eisner or post-2009 Iger — i.e., had SWI actually earned the right to hold cash rather than return it, going into the Turn/River deal?
    - Sources needed: SWI's ROIC vs. WACC and stock-price performance (a Jensen's-alpha proxy) for each year 2021–2024 since Ramakrishna became CEO.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2021–FY2024 (Item 7 MD&A + Item 8 financials for ROIC inputs); REPO-SWI-VAL (WACC already built at Step 12, reusable as the hurdle-rate side of the comparison; ROIC/stock-return track record not yet computed there); NEWS-WEB (SWI share-price history 2021–2025 for the Jensen's-alpha proxy).

- **Lesson 27, Session 27 · Part 2 — "Dividend Addicts, Family Subsidies, and Control: Assessing Dividend Policy Across Vale, BP, The Limited, and Tata Motors"** ([transcript](../04-dividends-and-valuation/lesson-27/session-27-part-2.md))
    - Quote: "So BP kept putting off the bad decision year after year after year hoping that something good will happen."
    - Question for SWI: SWI carries debt from its 2016 Thoma Bravo/Silver Lake LBO; did any dividend or buyback SWI made as a public company (2018–2025) get funded by new borrowing rather than by free cash flow to equity — a BP-style "borrowing to pay distributions" pattern — and did that pressure factor into Silver Lake's decision to sell rather than keep running SWI as a public dividend/buyback payer?
    - Sources needed: SWI's cash-flow statements 2019–2024 (dividends paid, buybacks executed, debt issuance/repayment) to compute FCFE and compare it against actual cash returned.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2019–FY2024, Item 8 cash flow statements (financing activities section); REPO-SWI-VAL (no FCFE or distribution-history work exists there yet — would need to be built fresh).

### Lesson 28 — Peer Group Benchmarking (Dividend Policy)

- **Lesson 28, Session 28 · Part 1 — "Me-Too Corporate Finance: Benchmarking Dividend Policy Against the Peer Group"** ([transcript](../04-dividends-and-valuation/lesson-28/session-28-part-1.md))
    - Quote: "Much of corporate finance is what I call 'me-too corporate finance.'"
    - Question for SWI: SWI competes in the observability/IT-ops SaaS sector alongside Datadog, Dynatrace, and PagerDuty — none of which pay dividends. Does SWI's own dividend/buyback policy match that "me-too" zero-payout sector norm, or did SWI diverge because its PE-controlled, EBITDA-margin-focused profile behaves more like a mature company than a growth SaaS peer — and what would a payout regression against peer growth, beta, and leverage predict for SWI specifically?
    - Sources needed: dividend yield / payout ratio (or documented absence) for DDOG, DT, and PD, plus regression inputs (beta, growth, debt ratio) for that peer set and for SWI.
    - Where to find: PEER-FILINGS — DDOG/DT/PD 10-Ks (capital-return footnotes); SEC-EDGAR — SWI 10-K FY2024 (capital-return disclosures); REPO-SWI-VAL (beta already computed at Steps 8–11, reusable as a regression input; no payout-ratio work exists there yet).

### Lesson 29 — Intrinsic Valuation Foundations

- **Lesson 29, Session 29 · Part 1 — "Three Ways to Value a Company and the Four Questions Behind Every DCF"** ([transcript](../04-dividends-and-valuation/lesson-29/session-29-part-1.md))
    - Quote: "When you have shifting, unstable, or unpredictable debt ratios, you should be valuing the entire firm."
    - Question for SWI: Given SWI's debt ratio has shifted materially — high leverage from the 2016 LBO, paydown after the 2018 IPO, and a fresh capital structure imposed by the 2025 Turn/River take-private — does the "shifting debt ratio → value the firm, not just equity" rule mean a FCFF/firm-value DCF is the right frame for SWI's FY2024 (final public-year) valuation, rather than a FCFE/equity-only approach?
    - Sources needed: SWI's book and market debt ratio history, 2018–2024, to confirm how unstable it actually was.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2019–FY2024, balance sheets (debt levels) and Item 7 MD&A (any stated leverage targets); REPO-SWI-VAL (Step 12 capital structure section has only a current-point-in-time snapshot, not the multi-year trend needed here).

### Lesson 30 — DCF Cash Flows & Discount Rates

- **Lesson 30, Session 30 · Part 1 — "Three Cash Flow Definitions and Matching Discount Rates: Deutsche Bank, Tata Motors, and Disney"** ([transcript](../04-dividends-and-valuation/lesson-30/session-30-part-1.md))
    - Quote: "So free cash flow to equity is after debt payments, free cash flow to the firm is before debt payments."
    - Question for SWI: Building SWI's FY2024 free cash flow to the firm (after-tax operating income minus net CapEx minus change in working capital) — what number results, what reinvestment rate does it imply relative to SWI's ~48% adjusted EBITDA margin, and how does that base-year cash flow pair with the cost of capital REPO-SWI-VAL already computed at Step 12 for a firm-value DCF?
    - Sources needed: SWI FY2024 operating income, effective tax rate, CapEx, depreciation, and change in working capital.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 8 (income statement + cash flow statement); REPO-SWI-VAL (WACC/cost of capital already computed at Step 12 — reusable as the discount rate; base-year FCFF itself is not yet built there).

### Lesson 31 — Growth Estimation

- **Lesson 31, Session 31 · Part 1 — "Growth Has to Be Earned: Reinvestment, Return, and the Fundamental Growth Rate"** ([transcript](../04-dividends-and-valuation/lesson-31/session-31-part-1.md))
    - Quote: "The growth of a company is not something that you and I can come up with or endow the company with."
    - Question for SWI: SWI is transitioning from perpetual-license to subscription SaaS revenue — what does SWI's actual FY2022–FY2024 fundamental growth rate (reinvestment rate × return on invested capital) imply for future growth, and how does that compare to the analyst-consensus or deal-implied growth rate embedded in the $18.50/share Turn/River price?
    - Sources needed: SWI's operating income, tax rate, CapEx, change in working capital, and invested capital for FY2022–FY2024 (to compute reinvestment rate and ROIC); analyst-consensus or management long-term growth projections.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2022–FY2024; REPO-SWI-VAL (partial ROIC/beta inputs exist at Steps 8–11, but no fundamental-growth computation yet); DEAL-DOCS (DEFM14A fairness opinion typically discloses management's internal financial projections/growth assumptions); NEWS-WEB (sell-side analyst consensus estimates pre-deal).

- **Lesson 31, Session 31 · Part 2 — "From ROE Decomposition to Baidu's Revenue-Based Growth Model"** ([transcript](../04-dividends-and-valuation/lesson-31/session-31-part-2.md))
    - Quote: "This approach to estimating growth based on fundamentals works if you have a stable return on equity and a stable return on capital."
    - Question for SWI: Since SWI's operating margin is in flux amid its perpetual-to-subscription transition (unlike Disney/Tata's assumed-stable-margin approach), should SWI's growth instead be modeled the Baidu way — project revenue growth, a margin glide path, and a sales-to-capital ratio to derive reinvestment — and what sales-to-capital ratio would fit SWI's asset-light SaaS cost structure?
    - Sources needed: SWI's multi-year revenue growth and operating-margin trend by segment/mix (subscription vs. license), plus CapEx and working-capital investment per dollar of incremental revenue.
    - Where to find: SEC-EDGAR — SWI 10-Ks FY2021–FY2024 (MD&A subscription ARR and margin disclosures); PEER-FILINGS — DDOG/DT sales-to-capital ratios as an asset-light SaaS cross-check; REPO-SWI-VAL (no growth-rate or sales-to-capital work exists there yet).

### Lesson 32 — Terminal Value

- **Lesson 32, Session 32 · Part 1 — "Capping the Growth Rate: How Long Should the Growth Period Last?"** ([transcript](../04-dividends-and-valuation/lesson-32/session-32-part-1.md))
    - Quote: "The bigger your competitive advantages and the more sustainable they are, the longer your growth period can be."
    - Question for SWI: How sustainable are SWI's competitive advantages post-SUNBURST — given ~18,000 customers were compromised in a nation-state supply-chain attack — does SWI still command enough of a durable moat (e.g., deployment switching costs) to justify a longer (5–10 year) growth period, or does reputational damage plus a crowded observability market (Datadog, Dynatrace) argue for a shorter growth period and an earlier shift to mature-company terminal-value assumptions?
    - Sources needed: SWI's customer/net-revenue-retention trend 2021–2024 (evidence of moat durability post-SUNBURST); comparative growth and market-share data for DDOG/DT/PD.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, MD&A (net retention rate, customer counts); NEWS-WEB (post-SUNBURST customer-churn commentary); PEER-FILINGS (DDOG/DT/PD growth and market positioning); REPO-SWI-VAL (Step 9 "Beta Fundamentals" touches business/competitive characteristics — check before redoing this analysis).

- **Lesson 32, Session 32 · Part 2 — "Valuing Vale as a Mature Company and Avoiding the Terminal Value Inconsistency Trap"** ([transcript](../04-dividends-and-valuation/lesson-32/session-32-part-2.md))
    - Quote: "If your net CapEx is zero, and your change in working capital is zero, you're reinvesting nothing, right?"
    - Question for SWI: If SWI is modeled entering stable growth post-take-private, what reinvestment rate is internally consistent with a 2–3% perpetual growth rate given a plausible stable-growth ROIC — and does SWI's true maintenance CapEx (SaaS infrastructure spend plus any capitalized software development) get correctly represented, avoiding the "CapEx exactly offsets depreciation, so reinvestment is zero" trap the lecture flags?
    - Sources needed: SWI's D&A vs. CapEx run-rate and capitalized-software-development policy; an assumed stable-growth ROIC for the terminal period.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (CapEx/D&A and capitalized-software footnotes); REPO-RATES (risk-free rate as the terminal growth-rate cap); REPO-SWI-VAL (Step 12 WACC as the pre-convergence starting cost of capital; no terminal-value work exists there yet).

### Lesson 33 — Firm-to-Equity Bridge

- **Lesson 33, Session 33 · Part 1 — "From Firm Value to Equity Value: Discounting Cash, Premiuming Cash, and Valuing Cross-Holdings"** ([transcript](../04-dividends-and-valuation/lesson-33/session-33-part-1.md))
    - Quote: "A dollar in cash is valued at about 69 cents. That's a 31% discount."
    - Question for SWI: Given SWI's ROIC-vs-WACC track record and the fact the market ultimately accepted a going-private sale at $18.50/share, does SWI's cash sit closer to the "neutral" (ROIC≈WACC) bucket or the "discounted" (bad-projects, market doesn't trust the cash) bucket — and would that partly explain why a going-private discount was acceptable to public shareholders rather than a fight for a higher price?
    - Sources needed: SWI's ROIC vs. WACC track record 2021–2024, cash balance size, and any market commentary on cash-balance discounting ahead of the deal.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 balance sheet (cash position); REPO-SWI-VAL (WACC built at Step 12; ROIC not yet computed there); DEAL-DOCS (fairness opinion may discuss treatment of cash in its own DCF); NEWS-WEB (pre-deal market commentary on SWI's cash use).

- **Lesson 33, Session 33 · Part 2 — "Cross-Holding Shortcuts, Other Assets, and Equity Options as a Second Claim on Equity"** ([transcript](../04-dividends-and-valuation/lesson-33/session-33-part-2.md))
    - Quote: "You have to net out the value of that second claim if you want the value per share as a common stockholder."
    - Question for SWI: How large was SWI's outstanding equity option/RSU overhang in FY2024, and using the lecture's prescribed method (value equity first, subtract options valued as options via an option-pricing model, then divide by actual — not diluted — shares), how much does per-share intrinsic value change versus a naive diluted-share-count treasury-stock-method treatment?
    - Sources needed: SWI's FY2024 outstanding stock options/RSUs, exercise prices, remaining contractual life, and the diluted share count used in reported EPS.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 8 stock-based-compensation footnote, plus DEF 14A proxy (equity grant detail); REPO-SWI-VAL (no equity-bridge or options work exists there yet).

### Lesson 34 — Applied DCF Valuation and the Value of Control

- **Lesson 34, Session 34 · Part 1 — "Stories Into Numbers: Building the Full Disney DCF Valuation"** ([transcript](../04-dividends-and-valuation/lesson-34/session-34-part-1.md))
    - Quote: "A good valuation is a bridge between stories and numbers."
    - Question for SWI: What is the actual "story" behind SWI's FY2024 DCF — status-quo continuation of the subscription transition at roughly its current growth and margin — and, building the full Disney-style valuation picture (base-year FCFF, cost of capital, growth/transition period, terminal value, value per share), does the resulting intrinsic value land above, at, or below the $18.50/share Turn/River paid?
    - Sources needed: a complete SWI FY2024 base-year FCFF build, a growth/transition schedule, starting and mature-company cost of capital, terminal growth rate, and the cash/debt/options bridge to value per share.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 (full financials for the base-year build); REPO-SWI-VAL (Step 12 WACC reusable as the starting cost of capital — the rest of the DCF is not yet built there); REPO-RATES (risk-free rate for the terminal growth cap); LESSON-MATERIALS (lesson-34's own slides/spreadsheet template for the "valuation picture" layout); DEAL-DOCS ($18.50/share, ~5.5x revenue, as the real-world value to check the result against).

- **Lesson 34, Session 34 · Part 2 — "The Value of Control: Status Quo vs. Optimal, and the Four Levers to Restructure a Company"** ([transcript](../04-dividends-and-valuation/lesson-34/session-34-part-2.md))
    - Quote: "The value of control in any company is the difference between two values: the status quo value and the optimal value."
    - Question for SWI: REPO-SWI-VAL's governance assessment (Step 2) already found weak public-shareholder governance under Silver Lake's ~75% control — per this lesson's rule that weak governance leaves the market price near the status-quo value rather than the optimal value, is the Turn/River price better read as partly capturing "value of control" that public minority shareholders never got access to, and how large is that gap using the four levers (base-year efficiency, reinvestment/ROIC mix, cost of capital, growth-period length)?
    - Sources needed: an "optimal" restructured SWI valuation (alternate reinvestment/ROIC mix, an optimal debt ratio if one can be derived) to compare against the status-quo DCF from Lesson 34 Part 1, plus SWI's unaffected pre-announcement trading price.
    - Where to find: REPO-SWI-VAL (Step 2 governance assessment documents the weak-governance finding already; an optimal-debt-ratio/optimal-value analysis is not yet built there); SEC-EDGAR (SWI pre-announcement trading price, 8-K deal announcement); DEAL-DOCS (Turn/River offer premium over the unaffected share price).

### Lesson 35 — Multiples

- **Lesson 35, Session 35 · Part 1 — "Pricing vs. Valuing: Defining, Describing, Analyzing, and Applying Multiples"** ([transcript](../04-dividends-and-valuation/lesson-35/session-35-part-1.md))
    - Quote: "You're trying to attach a number to a company based on how similar companies are being priced out there."
    - Question for SWI: Using EV/Revenue as the multiple (the metric implicit in the deal's "~5.5x 2024 revenue" framing) and a consistently defined peer set (DDOG, DT, PD) with matching numerator/denominator, where does SWI's own pre-deal EV/Revenue sit relative to the peer median distribution — is 5.5x a premium, a discount, or in line with the sector?
    - Sources needed: EV/Revenue multiples for DDOG, DT, and PD at a comparable point in time (or trailing-twelve-months matching FY2024), and SWI's own pre-deal enterprise value and revenue.
    - Where to find: PEER-FILINGS — DDOG/DT/PD 10-Ks and market caps (for the EV build); SEC-EDGAR — SWI 10-K FY2024 and pre-announcement market cap; DEAL-DOCS (the $4.4B / ~5.5x figure to benchmark against).

- **Lesson 35, Session 35 · Part 2 — "Backing Out What Drives a Multiple: Why Cheap Stocks Usually Deserve to Be Cheap"** ([transcript](../04-dividends-and-valuation/lesson-35/session-35-part-2.md))
    - Quote: "Most companies that look cheap deserve to be cheap."
    - Question for SWI: If SWI's pre-deal EV/Revenue or EV/EBITDA looked cheap relative to observability-sector peers, was that "deserved" — explained by lower growth, a higher risk premium from lingering SUNBURST reputational overhang, or lower margins/ROIC — the way the lecture explains Deutsche Bank's low price-to-book via its low ROE once regressed against peer drivers?
    - Sources needed: SWI's and peers' growth rates, margins, and a risk/beta proxy, to run a comparable-firms regression of the chosen multiple against those drivers.
    - Where to find: PEER-FILINGS — DDOG/DT/PD financials (growth, margin, ROIC inputs); REPO-SWI-VAL (beta and risk inputs already built at Steps 8–11); SEC-EDGAR — SWI's own growth/margin history (10-Ks FY2021–FY2024).

### Lesson 36 — Course Synthesis

- **Lesson 36, Session 36 · Part 1 — "Ten Lessons Revisited: Governance, Risk, and the Marginal Investor"** ([transcript](../04-dividends-and-valuation/lesson-36/session-36-part-1.md))
    - Quote: "Not everyone will agree on every decision being the best decision from their interests."
    - Question for SWI: Applying the four-stakeholder-conflict lens (stockholders / bondholders / managers / society) to the SUNBURST crisis and the subsequent Turn/River sale — whose interests actually drove the sale decision (Silver Lake's exit-value maximization vs. public minority stockholders vs. customers/society still exposed by the original breach) — and does REPO-SWI-VAL's existing governance write-up already answer this, or leave it open?
    - Sources needed: the merger proxy's "background of the merger" narrative, board voting record, and any dissenting-shareholder or appraisal-rights litigation over the Turn/River deal.
    - Where to find: SEC-EDGAR — SWI DEFM14A merger proxy / Schedule 13E-3 ("Background of the Merger" section); REPO-SWI-VAL (Steps 2–3 already cover governance and stated objectives — check before redoing); NEWS-WEB (any shareholder-litigation coverage of the deal).

- **Lesson 36, Session 36 · Part 2 — "The Trade-Off on Debt and the Three First Principles of Corporate Finance"** ([transcript](../04-dividends-and-valuation/lesson-36/session-36-part-2.md))
    - Quote: "If you cannot find investments that make your hurdle rate, find a way to get the cash back to your stockholders."
    - Question for SWI: Tying together all three first principles for SWI's final public year (FY2024) — did its investment returns (ROIC) clear its hurdle rate (WACC, per REPO-SWI-VAL Step 12), was its capital structure near an optimal debt/equity mix (or over/under-levered given its LBO legacy debt), and did its dividend/buyback policy correctly reflect the answers to those first two questions — and does that three-part synthesis explain why Silver Lake chose to sell rather than keep running SWI as a public company?
    - Sources needed: SWI's ROIC vs. WACC (investment principle), actual vs. optimal debt ratio (financing principle), and dividend/buyback history vs. FCFE (dividend principle) — a full synthesis across all three, most of which is not yet built.
    - Where to find: REPO-SWI-VAL (WACC and capital structure at Step 12 is the one piece already done; ROIC, optimal-debt-ratio, and dividend/FCFE analysis are not yet in the file and would need fresh work); SEC-EDGAR — SWI 10-K FY2024 full financials; DEAL-DOCS (Turn/River deal rationale as the real-world "answer key").
