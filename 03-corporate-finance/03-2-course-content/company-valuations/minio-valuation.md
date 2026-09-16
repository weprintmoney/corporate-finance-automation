---
title: "MinIO, Inc. — Module 1 Valuation: Cost of Capital Analysis"
status: active
owner: weprintmoney
created: 2026-09-16
last_updated: 2026-09-16
---

# Company Valuation: MinIO, Inc.
*Applied Corporate Finance — Module 1 Analysis*

**A note on data availability:** MinIO is a private company (last priced at $1B in a January 2022 Series B). It has no ticker, no public financial statements, no regression beta, no bond rating, and no disclosed board minutes. None of the repo's pre-fetched data files apply (`companies/<ticker>.json` doesn't exist for a private company; `market-rates.json` and populated `industry-betas.json`/`country-risk.json` were not available in this checkout — the JSON files exist but their `industries`/`countries` objects are empty stubs pending a CI refresh). Every input below is either live-web-sourced (rates, MinIO facts) or drawn from the Damodaran dataset spreadsheets checked into this repo's lesson folders (industry betas, ratings-to-spread table), which is exactly what Module 1 teaches you to do when a company has no ticker: fall back to bottom-up, fundamentals-based estimation instead of top-down market data. Every estimated (not sourced) figure is flagged inline and again in the Data Provenance section at the end.

---

## Step 1 — Company Selected

**MinIO, Inc.** — S3-compatible, AGPL-licensed object storage software, historically distributed as a free "Community Edition" binary with a paid enterprise tier, now consolidating around a paid product called **AIStor** ("the data backbone for enterprise AI"). Founded by Anand Babu (AB) Periasamy, Garima Kapoor, and Harshavardhana Gowda. Last primary-market valuation: $1B (Series B, January 2022).

---

## Step 2 — Corporate Governance

### Board of Directors
No public board roster is filed anywhere (private company, no SEC reporting obligation). What's publicly confirmable: the board includes co-founders AB Periasamy (CEO) and Garima Kapoor, alongside institutional board representation historically associated with General Catalyst and Nexus Venture Partners — participants in MinIO's earlier Seed/Series A rounds. Intel Capital led the $103M Series B (Jan 2022) with SoftBank Vision Fund 2 as a new participant and Dell Technologies Capital as an existing one; standard late-stage VC terms would give at least the Series B lead (Intel Capital) a board seat or observer right, but no public source confirms specific individual appointments from that round.

### Governance Assessment
There is no independent public-company governance apparatus here — no audit committee, no outside/independent directors bound by exchange listing rules, no proxy statement, no shareholder vote. Governance runs entirely through privately negotiated stockholder/voting agreements between the founders and each round's preferred-stock investors. That's normal for a private company at this stage; the point of naming it is that none of the public-market accountability mechanisms Module 1 assumes (activist investors, hostile takeover threat, proxy contests) are available levers on MinIO's decisions. The 2025 relicensing decision, in other words, was not disciplined or vetoed by any outside governance mechanism — it was a private board-and-founder call.

### Power Structure
Founder- and VC-controlled, not shareholder-broad. Power sits with a small, concentrated set of preferred stockholders (the seed-through-Series-B syndicate) plus the three founders, not with a diversified public shareholder base. This matters directly for Steps 4 and 11 below: the people actually bearing MinIO's risk are not diversified investors holding it as one position in a broad portfolio.

---

## Step 3 — Stated Objectives

### Stated Goals
MinIO has never had a stock price to maximize (private company), so the Module 1 "stock price maximization" framing doesn't apply literally. The nearest public proxy for a stated objective is the ARR growth figure the company chose to publicize: a February 2025 press release announcing **149% ARR growth over the prior two years**, framed explicitly around AI-driven demand for data storage. In 2025 the company also rebranded its commercial product as "AIStor," positioning itself as "the data backbone for enterprise AI" — a stated pivot toward capturing AI-infrastructure spend specifically, not owning "open source object storage" broadly.

### Inferred Focus (if no stated goals)
Behavior says more than the press release. Over 2025–2026, MinIO progressively restricted the free Community Edition: admin console features removed from the codebase (change landed late February 2025, felt by users on upgrade around May 2025), official binaries and container images discontinued around October 2025, the project placed into "maintenance mode" via a December 3, 2025 README change, and the GitHub repository archived in February 2026, briefly reopened, then archived again April 25, 2026. Read together with the ARR headline, the inferred objective is **near-term revenue/ARR growth to support the next financing event or an eventual exit at or above the 2022 $1B mark** — not stock price (none exists), and arguably not long-run enterprise value maximization in the DCF sense the course teaches, since the sequence traded a decade of open-source distribution and community trust for a shorter-term conversion push. That's a growth-and-liquidity objective, not a value objective, and the two aren't the same thing — which is exactly the distinction Lesson 3 asks you to test for.

---

## Step 4 — Share Classes and Marginal Investor

### Share Structure
Standard private-company structure: founder common stock plus a stack of preferred stock issued at each round (Seed → Series A $20M → Series B $103M, Jan 2022). No information is public on liquidation preference multiples, participation rights, or anti-dilution terms for any round — normal for a private company, but worth flagging because those terms change who actually bears downside risk (preferred holders with a liquidation preference are economically closer to senior creditors than to common risk-bearing equity until the exit value clears their preference stack).

### Largest Shareholders
Founders (AB Periasamy, Garima Kapoor, Harshavardhana Gowda) plus the institutional syndicate: Intel Capital, SoftBank Vision Fund 2, Dell Technologies Capital, General Catalyst, Nexus Venture Partners. Exact ownership percentages are not disclosed.

### Marginal Investor
There is no public marginal investor in the CAPM sense (no continuous trading, no price discovery from a diversified market). The party who actually "prices" MinIO's equity is the lead investor in whatever the next transaction is — practically, that was Intel Capital at the Series B, and would be either a growth-equity/PE buyer, a strategic acquirer, or public-market investors in the event of an eventual IPO. Since no round has priced since January 2022 and reported secondary marks in 2026 have come in below the $1B mark, the current answer to "who is pricing this equity" is genuinely unsettled — which is itself informative about where this company sits in its lifecycle.

### Likely Diversification of Marginal Investor
Not diversified in the way Module 1's baseline CAPM investor is assumed to be. VC funds hold concentrated stakes in a relatively small number of portfolio companies and are themselves accountable to LPs for fund-level (not single-position) returns, and the founders' net worth is overwhelmingly concentrated in this one company. This is precisely the setup Lesson 11 flags as needing **total beta**, not market beta — see Step 11.

---

## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
USD. MinIO, Inc. is US-headquartered (originally incorporated in the US after a re-domestication from an earlier structure), and all disclosed funding figures are reported in USD.

### Revenue Currencies
Not disclosed in a segmented way. MinIO sells globally (object storage / AI-data-infrastructure customers across North America, Europe, and Asia), but enterprise software contracts of this kind are overwhelmingly USD- or major-hard-currency-denominated even when the customer is non-US, so currency mismatch risk is assumed low. This is an inference, not a sourced fact — flagged in Data Provenance.

### Analysis Currency and Rationale
USD — matches the company's reporting currency and its home-market risk-free rate is the most liquid, deepest sovereign curve available, which is the standard Damodaran justification for defaulting to USD when a company's own reporting currency is USD.

### Risk-Free Rate
**5.01%** — US 10-year Treasury yield, September 15, 2026 (live-sourced; multiple financial-data outlets, including CNBC and TradingEconomics, reported the 10-year crossing above 5% that day, its highest level since 2007, amid a broader bond selloff and a widely anticipated Fed rate move). This is materially higher than the sub-2% risk-free-rate environment much of Module 1's example material was built around — worth remembering when comparing this analysis to older worked examples in the lesson slides.

---

## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
**4.23%** — Damodaran's implied ERP for the US market, from his most recent confirmed annual data update (start of 2026). This is an *implied* (forward-looking) estimate, not a historical-average or survey-based one.

### Method and Source
Implied ERP method: back out the discount rate that equates the current S&P 500 level to the present value of expected future cash flows (dividends + buybacks, grown at expected earnings growth), then subtract the risk-free rate. Damodaran favors this over historical-average ERP (backward-looking, sample-period-dependent) and survey ERP (reflects investor sentiment, not market-implied pricing) for exactly the reason Lesson 6 gives: it's forward-looking and updates with the market in real time. Caveat: 4.23% is his confirmed *January 2026* figure; his monthly updates since then were not independently verifiable via web search at the time of this report, and given the sharp September 2026 rate/equity selloff noted in Step 5, the live implied ERP today plausibly sits somewhat above 4.23% (ERP and rates have moved together in past selloffs of this kind). Treated as a soft, dated input — flagged in Data Provenance.

---

## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
Revenue geography (standard for a software/services company — production and reserves-based measures apply to extractive industries, not applicable here).

### Geographic Breakdown
Not disclosed. MinIO markets and sells globally, but its named enterprise case studies and go-to-market motion skew toward developed markets (North America, Western Europe, developed Asia-Pacific) — consistent with enterprise AI/data-infrastructure buyers generally being concentrated in mature economies with large existing data estates.

| Region/Country | % of revenue (assumed) | Country ERP |
|----------------|-------------------------|-------------|
| United States | Majority (assumed) | 0.00% (Aaa, mature-market baseline) |
| Other developed markets (EU, UK, developed APAC) | Remainder (assumed) | ≈0.00%–0.3% (most Aaa/Aa-rated markets carry negligible spreads) |

### Weighted Average ERP
**≈4.23%** — effectively equal to the mature-market ERP, since no material emerging-market revenue concentration is disclosed or plausible given MinIO's customer profile. This is an assumption, not a sourced figure — flagged in Data Provenance.

### Why This ERP Might Change
If MinIO's AIStor motion succeeds in emerging sovereign-AI or data-localization markets (a real trend in 2025–2026 AI infrastructure buying), country risk exposure would rise and so would the weighted ERP. Conversely, if the AGPL-to-AIStor pivot pushes MinIO toward a narrower set of large developed-market enterprise accounts (which the community backlash and self-hosting risk profile arguably favors), weighted ERP would stay near the mature-market baseline.

---

## Step 8 — Regression Beta

### Regression Beta
**Not available.** MinIO has no publicly traded shares, so there is no return series to regress against a market index. This is the expected, correct answer for a private company — Lesson 10's entire justification for the bottom-up approach is exactly this scenario (no trading history, or a trading history too short/noisy to trust), and Step 10 below is where the actual beta estimate is built.

### Index, Time Period, R-squared
N/A — no regression exists.

### Reliability Assessment
N/A. Proceeding directly to bottom-up estimation (Step 10), which the lesson explicitly recommends for companies with limited or no trading history.

---

## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
MinIO sells enterprise infrastructure software — a discretionary-ish enterprise IT capital/operating expenditure that tracks the broader enterprise data-infrastructure and (currently) AI-capex cycle. That points toward a moderate-to-high business beta, roughly in line with enterprise software peers, and currently amplified by MinIO's specific exposure to the AI-infrastructure demand cycle it is explicitly marketing into — a cycle that itself carries above-market risk (highly sentiment- and capex-cycle-dependent as of 2026). No disclosed business-line segmentation, so a single blended beta is used rather than a segment-weighted one.

### Operating Leverage Effect
High fixed-cost structure typical of software: engineering headcount (~218 employees as of mid-2026) and R&D are largely fixed in the short run, while the direct cost of serving an additional customer (support, minor incremental cloud spend) is low. High fixed-cost, low-variable-cost structures mean operating income is more sensitive to revenue swings than revenue itself — pushing the unlevered business beta above 1.0, consistent with the industry data used in Step 10.

### Financial Leverage Effect
Effectively none. No disclosed interest-bearing debt or bond issuance — MinIO's financing has been entirely equity (Seed/Series A/Series B preferred stock), which is typical for a company at this stage. That means essentially all of MinIO's risk is *business* risk, not leverage-amplified risk — levering up the beta in Step 10/11 will barely move it, because there's no debt to lever with. Worth stating plainly: whatever risk MinIO's owners are exposed to, it comes from the business model itself, not from the balance sheet — the moat problem in the LinkedIn piece is a business-model risk, not a capital-structure risk.

---

## Step 10 — Bottom-Up Unlevered Beta

### Business Segments
Not disclosed as separate reporting segments; treated as a single business (enterprise object storage / AI data infrastructure software).

### Comparable Firms / Industry Group
Used Damodaran's US industry-beta dataset (`03-corporate-finance/03-2-course-content/01-foundations-and-discount-rates/lesson-10/spreadsheet-totalbeta24.md`, dataset dated January 2024 — the most recent version checked into this repo; flagged as a ~2-year-old vintage in Data Provenance). Classified MinIO under **Software (System & Application)** — the bucket Damodaran uses for infrastructure/enterprise systems software (the same bucket comparable database/infrastructure companies like MongoDB or Elastic would fall into), rather than "Computer Services" (more IT-services-oriented) or "Software (Internet)" (consumer-internet-oriented).

| Segment | Industry | Avg Unlevered Beta | Correlation w/ Market | Weight |
|---------|----------|--------------------:|------------------------:|-------:|
| Object storage / AI data infrastructure | Software (System & Application) | 1.2725 | 0.3374 | 100% |

### Estimated Unlevered Beta
**≈1.27** — above 1.0, consistent with Step 9's expectation of a high-fixed-cost, capex-cycle-linked enterprise software business. No adjustment applied for cash balance (MinIO's cash position isn't disclosed, so the standard cash-adjustment Damodaran's spreadsheet applies for public comps couldn't be replicated) — flagged in Data Provenance.

---

## Step 11 — Levered Beta and Total Beta

### Inputs
- Unlevered beta: 1.2725 (Step 10)
- Debt/Equity ratio: **≈0%** — no disclosed interest-bearing debt (Step 9)
- Marginal tax rate: ~25% assumed (blended US federal + state; moot here given D/E≈0)
- Correlation with market: 0.3374 (industry average, Step 10)

### Levered Beta (Hamada)
β_levered = β_unlevered × [1 + (1 − t) × D/E] = 1.2725 × [1 + (0.75 × 0)] = **1.2725** — unchanged from the unlevered beta, because there's no debt to lever with. This is the beta a diversified public-market investor (e.g., a future IPO buyer) would use to price MinIO's equity risk.

### Total Beta
This is the more relevant number for MinIO's *actual* current owners (Step 4/Step 2 — a concentrated founder/VC syndicate, not a diversified public shareholder base). Per Lesson 11's total beta formula:

Total Beta = Levered Beta / Correlation with market = 1.2725 / 0.3374 = **≈3.77**

### Interpretation
The gap between 1.27 (market beta) and 3.77 (total beta) is the whole point of Lesson 11. A diversified investor only cares about the market-correlated slice of MinIO's risk (1.27×), because everything else diversifies away in a broad portfolio. MinIO's actual owners — three founders and a small VC syndicate holding concentrated, illiquid stakes — can't diversify it away. From their vantage point, the true risk they're carrying is nearly **3x** what a public-market beta implies. That has a direct bearing on the article's thesis: a founder/VC group bearing total-beta-level risk on an asset whose visible moat (best open-source technology) has a short competitive-advantage period has a much stronger private incentive to force monetization quickly than a diversified public shareholder would — total beta, not market beta, is the more honest lens on why the 2025 relicensing squeeze happened when it did.

---

## Step 12 — Cost of Debt

### Bond Rating and Spread
None — MinIO has no public bond rating (private, no public debt issuance).

### Synthetic Rating
**Not computable in the standard sense, and that's the finding, not a gap.** The synthetic-rating method (interest coverage → rating → spread, per `spreadsheet-ratings.md` in Lesson 12) requires EBIT and interest expense, neither of which is disclosed. More importantly: there is no public evidence MinIO carries any meaningful interest-bearing debt at all. Late-stage venture-backed software companies at MinIO's scale typically finance entirely through equity, with at most an undrawn or lightly-drawn venture debt facility — not a funded, amortizing debt load. Forcing a synthetic-rating estimate by inventing an EBIT/interest-expense pair would manufacture false precision. The correct Module-1 answer for a company in this position is: **treat MinIO as unlevered (D/V ≈ 0%) for cost-of-capital purposes**, which is itself a real and common outcome the lesson's own methodology anticipates for young, private, growth-stage companies.

| Metric | Value |
|--------|-------|
| EBIT | Not disclosed |
| Interest expense | Not disclosed |
| Interest coverage ratio | N/A — no disclosed interest-bearing debt |
| Synthetic rating | N/A |
| Default spread | N/A |
| Pre-tax cost of debt | N/A (treated as immaterial; D/V ≈ 0%) |

### Actual vs. Synthetic Rating — Differences and Explanation
Not applicable — no actual rating exists to compare against, and no synthetic rating could be responsibly computed from disclosed data.

### Market Value of Debt
No disclosed interest-bearing debt. Assumed **$0** (or immaterial) for WACC purposes.

### Lease Debt Capitalization
MinIO's office/facilities lease commitments are not disclosed. Given the company's headcount (~218) this is likely a modest office-lease footprint relative to its $1B-scale valuation — plausibly a few million dollars of capitalized lease debt at most — but with no disclosed lease schedule, capitalizing it (per the Lesson 12 methodology shown in `spreadsheet-ratings.md`) would require fabricated inputs. Treated as immaterial to the capital structure conclusion (D/V ≈ 0%) rather than estimated.

### Marginal Tax Rate
~25% (blended US federal + state statutory assumption) — moot for WACC given D/V ≈ 0%, included only for completeness.

---

## Summary — Cost of Capital Inputs

| Input | Value |
|-------|-------|
| Risk-free rate | 5.01% (US 10-yr Treasury, Sept 15, 2026 — sourced) |
| Mature market ERP | 4.23% (Damodaran implied ERP, Jan 2026 update — sourced, dated) |
| Weighted ERP (country-adjusted) | ≈4.23% (assumed ~all-developed-market revenue — estimated) |
| Unlevered beta (bottom-up, Software System & Application) | 1.27 (Damodaran Jan 2024 industry dataset — sourced, dated) |
| Levered beta (Hamada, D/E≈0) | 1.27 (unchanged — no debt to lever) |
| **Total beta (undiversified-owner lens)** | **3.77** (=levered beta / 0.337 correlation) |
| Cost of equity — diversified/market-beta basis | **10.4%** (5.01% + 1.27 × 4.23%) |
| **Cost of equity — total-beta basis (concentrated founder/VC ownership)** | **21.0%** (5.01% + 3.77 × 4.23%) |
| Pre-tax cost of debt | N/A — no disclosed funded debt |
| After-tax cost of debt | N/A |
| Debt/Capital ratio | ≈0% (assumed unlevered) |
| **WACC — market-beta basis** | **≈10.4%** (= cost of equity, since D/V≈0) |
| **WACC — total-beta basis** | **≈21.0%** (= cost of equity, since D/V≈0) |

**Read this as two answers to two different questions.** ~10.4% is what MinIO's cost of capital looks like to a diversified buyer — a future IPO market, or a strategic acquirer valuing it as one asset among many. ~21.0% is what it costs the people who actually hold the company today, bearing risk they can't diversify away. A private company financed entirely by equity has to clear whichever hurdle its *actual* owners are using to judge the business — and 21% is an extremely high bar for "best open source object storage" to clear on its own, especially once a hyperscaler can host a compatible service for less. That gap between the two WACC numbers is, in cost-of-capital terms, the same story the LinkedIn piece tells in moat terms: the technology was never going to earn a 21% return for long enough to justify a $1B mark: which is the arithmetic behind why the 2025–2026 pivot to AIStor and the community-edition squeeze happened.

---

## Data Provenance — What's Sourced vs. Estimated

**Sourced (live web search or repo dataset, confirmed):**
- Risk-free rate (5.01%, Sept 15, 2026 10-yr Treasury)
- Mature market ERP (4.23%, Damodaran's Jan 2026 implied-ERP update)
- Industry unlevered beta and correlation (1.2725 / 0.3374, Damodaran Jan 2024 industry-beta dataset, via this repo's `spreadsheet-totalbeta24.md`)
- Ratings-to-spread mapping methodology (`spreadsheet-ratings.md`)
- MinIO facts: founders, Series B amount/date/investors/valuation, ARR growth claim (149%, Feb 2025 press release), Community Edition feature removal / binary discontinuation / maintenance-mode / repo-archival timeline, ~218 employees (mid-2026)

**Estimated or assumed (flagged, not fabricated as fact):**
- Weighted (country-adjusted) ERP ≈ mature market ERP — assumes predominantly developed-market revenue; not disclosed
- Revenue currency mix — assumed predominantly USD/hard-currency; not disclosed
- D/E ≈ 0% and cost of debt treated as N/A — no disclosed funded debt found; standard treatment for a company at this stage, but not independently confirmed as literally zero
- Marginal tax rate (~25%) — standard blended assumption, moot given D/V≈0
- Lease debt — assumed immaterial rather than estimated, given no disclosed lease schedule

**Stale/vintage inputs (best available in this repo, not necessarily current):**
- Damodaran industry-beta dataset used is dated January 2024 (~2 years old relative to this report's Sept 2026 date). The repo's own `industry-betas.json` (intended to be CI-refreshed) currently has an empty `industries` object — the automated refresh has not populated it.
- Mature market ERP (4.23%) is Damodaran's confirmed start-of-2026 figure; his more recent monthly updates were not independently verifiable via search at time of writing, and the September 2026 rate spike (Step 5) makes it plausible the live figure has moved since.

---

## Final Output

Report file: `03-corporate-finance/03-2-course-content/company-valuations/minio-valuation.md`

Per this repo's convention (sole-contributor, always admin-merge), this report will be committed on a branch and merged to `main` directly rather than left open for review.
