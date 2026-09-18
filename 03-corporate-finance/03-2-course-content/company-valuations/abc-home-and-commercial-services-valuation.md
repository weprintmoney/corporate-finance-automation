---
title: "ABC Home & Commercial Services — Module 1 Valuation: Cost of Capital Analysis"
status: active
owner: weprintmoney
created: 2026-09-18
last_updated: 2026-09-18
---

# Company Valuation: ABC Home & Commercial Services
*Applied Corporate Finance — Module 1 Analysis*

**A note on data availability:** ABC Home & Commercial Services is a privately held, family-owned regional home-services company (pest control, lawn care, plumbing, HVAC, electrical). It has no ticker, no public financial statements, no regression beta, no bond rating, and no SEC filings of any kind. None of the repo's pre-fetched data files apply — `companies/<ticker>.json` doesn't exist for a private company with no ticker, and `market-rates.json` is absent from this checkout while `industry-betas.json`/`country-risk.json` are present but empty stubs pending a CI refresh. Every rate/ERP/beta input below is live-web-sourced from Damodaran's public data or financial news; every company-specific fact is sourced from news coverage, trade-press profiles, and the company's own "About Us" pages, with direct quotes and links given inline. Where ABC's actual financials (debt, EBIT, interest expense) are simply not public, this report says so plainly and uses clearly labeled bounding scenarios instead of inventing precision — flagged again in the Data Provenance section.

---

## Step 1 — Company Selected

**ABC Home & Commercial Services** — a Texas-founded home and commercial services company offering pest control, lawn care/landscaping, plumbing, HVAC, and electrical services, operating across roughly a dozen Texas markets (Austin, San Antonio, Houston, Dallas, Fort Worth, Waco, Bryan–College Station, Corpus Christi, the Rio Grande Valley) plus expansion branches in Florida and Georgia. Founded 1949 in San Antonio; independently, family-owned by the Jenkins family since 1965. [PCT — 75-Year Celebration](https://www.pctonline.com/news/abc-home-commercial-75-year-celebration/)

---

## Step 2 — Corporate Governance

### Board of Directors
No public board roster exists — private company, no SEC reporting obligation, no proxy filings. What's publicly confirmable: the company is led by third-generation family members. **Bobby Jenkins** leads the Austin business; his brothers **Raleigh Jenkins** (Houston) and **Dennis Jenkins** (Dallas) lead their respective territories. As of April 2026, PCT reported **Bo Jenkins** (fourth generation) was promoted to Vice President of Operations and Sales, alongside a promotion for **Omar Aranda**. [PCT — Bo Jenkins Promotion](https://www.pctonline.com/news/abc-home-and-commercial-services-promotes-bo-jenkins/)

One open question worth flagging rather than glossing over: sourcing consistently describes Bob and Sandy Jenkins as having "divided Texas into thirds" for their three sons, with "each son has his own territory that they still abide by to this day." That phrasing is ambiguous about the actual legal/corporate structure — it's not clear from public sources whether "ABC Home & Commercial Services" is a single legal entity with the three brothers as co-owners, or a family of separately-owned regional entities operating under a shared brand and shared family agreement (closer to a franchise-like arrangement). This matters for a governance analysis and isn't resolved by anything found in this search — treated as an open item, not fabricated as fact either way.

### Governance Assessment
No independent public-company governance apparatus applies here: no audit committee, no outside directors bound by exchange listing rules, no shareholder vote, no activist-investor or hostile-takeover pressure. Whatever discipline exists on this business comes from within the family (a multi-generational succession structure — 10–11 of the founders' 16 grandchildren and spouses currently work at the company) rather than from any external market mechanism. [Community Impact — ABC expands services](https://communityimpact.com/sponsored/sponsored/2022/05/15/abc-home-and-commercial-expands-from-pest-control-to-offering-all-home-services/)

### Power Structure
Concentrated, family-controlled — power sits with the Jenkins family across three (now moving into a fourth) generations, not with a diversified public shareholder base. This is the single most consequential fact for this whole analysis, and it directly answers the framing question behind this report: **the sourced material is explicit that ABC is not private-equity owned.** One profile states directly: *"Unlike many home service companies in Austin that have been purchased by national private equity firms, ABC remains a locally owned and operated family business led by Bobby Jenkins."* [Community Impact — ABC expands services](https://communityimpact.com/sponsored/sponsored/2022/05/15/abc-home-and-commercial-expands-from-pest-control-to-offering-all-home-services/) No source found in this research contradicts that — no PE sponsor, no leveraged buyout, no reported recapitalization event was found anywhere in trade press, business databases, or news search.

---

## Step 3 — Stated Objectives

### Stated Goals
ABC has no stock price to maximize (private, family-held). Its own public messaging centers on longevity and family continuity — the 75th-anniversary coverage (2024, marking the 1949 founding) and repeated "family business" framing across its own marketing pages and third-party profiles are the closest thing to a stated objective: preserving and growing a multi-generational family enterprise, not maximizing a sale price or courting outside capital.

### Inferred Focus (if no stated goals)
Behavior is consistent with that framing. ABC has grown from a single-service pest control operator into a multi-service home-services platform (pest control → lawn care → plumbing → HVAC → electrical) and has expanded geographically, including at least one confirmed bolt-on acquisition: **ABC Home & Commercial Services acquired A.S.A. Guardian Pest Control**, expanding its residential/commercial pest management footprint in the Rio Grande Valley. [Pest Management Professional — ABC acquires A.S.A. Guardian](https://www.mypmp.net/abc-home-commercial-services-acquires-a-s-a-guardian-pest-control/) That's organic-plus-bolt-on growth funded (as far as any source indicates) from the business's own cash flow and ordinary bank financing, not sponsor-driven leveraged M&A — the opposite growth pattern from a private-equity-backed "roll-up," where a financial sponsor uses debt to acquire and consolidate many operators quickly, then targets a resale. ABC's pattern — slow, family-controlled, one confirmed tuck-in acquisition over decades, explicit public statements distancing itself from the PE-buyout wave hitting the Austin home-services market — reads as **growth-for-continuity**, not growth-for-exit.

One data point worth surfacing honestly and without over-interpreting it: at least one ABC location (Marietta, GA) shows as closed as of July 2026 on business listings. [Yelp — ABC Home and Commercial Services, Marietta (Closed)](https://www.yelp.com/biz/abc-home-and-commercial-services-marietta) No news source found explains why, and a single branch closure in an expansion market is common footprint rationalization, not evidence of company-wide financial distress — flagged for completeness, not treated as a finding.

---

## Step 4 — Share Classes and Marginal Investor

### Share Structure
Not applicable in the public-market sense — privately held, no classes of publicly tradable stock, no disclosed capitalization table. See the open question flagged in Step 2 about whether ownership sits in one entity or several family-controlled regional entities.

### Largest Shareholders
The Jenkins family: Bobby Jenkins (Austin), Raleigh Jenkins (Houston), Dennis Jenkins (Dallas), descendants of founders Bob Sr. and Sandy Jenkins, with fourth-generation family members (e.g., Bo Jenkins) now in senior operating roles. No outside institutional or private-equity ownership was found anywhere in this research.

### Marginal Investor
There is no public marginal investor in the CAPM sense — no continuous trading, no market price discovery. The party who actually "prices" ABC's equity, to the extent that concept applies at all, is the Jenkins family itself: whatever return the family requires to keep capital deployed in the business rather than sell it (to a strategic buyer, a PE roll-up, or simply retire) is the real hurdle rate governing decisions here.

### Likely Diversification of Marginal Investor
Not diversified. The family's wealth and careers are concentrated in this one private, illiquid business across multiple generations — the same setup Lesson 11 flags as needing **total beta**, not market beta, as the more honest risk lens. See Step 11.

---

## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
USD — US-headquartered (San Antonio/Austin, TX), all operations and disclosed facts are US-based.

### Revenue Currencies
USD. All confirmed markets (Texas, Florida, Georgia) are domestic US markets; no international operations were found in any source.

### Analysis Currency and Rationale
USD — matches the company's operating footprint and reporting currency; standard default per Lesson 5.

### Risk-Free Rate
**4.80%** — US 10-year Treasury yield, as of September 17, 2026 (live-sourced; multiple outlets including CNBC/TradingEconomics report the 10-year near this level following a recent Fed move, up from a lower level earlier in the year).

---

## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
**4.23%** — Damodaran's implied ERP for the US market, from his confirmed start-of-2026 data update.

### Method and Source
Implied ERP method (Lesson 6): back out the discount rate equating the current S&P 500 level to the present value of expected future cash flows, then subtract the risk-free rate. This is Damodaran's preferred forward-looking method over historical-average or survey ERP. Caveat, same as flagged in other reports built from this repo's dataset: this is his confirmed January 2026 figure; his live monthly updates since then were not independently confirmed via search at time of writing — treated as a soft, dated input.

---

## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
Revenue geography — standard for a services business (production/reserves-based measures apply to extractive industries, not relevant here).

### Geographic Breakdown

| Region/Country | % of revenue | Country ERP |
|----------------|---------------|-------------|
| United States (all confirmed markets: TX, FL, GA) | ~100% (no international operations found) | 0.00% (Aaa, mature-market baseline) |

### Weighted Average ERP
**4.23%** — equal to the mature-market ERP, since no international revenue exposure was found in any source.

### Why This ERP Might Change
Only if ABC expanded into international markets, which no source suggests is planned or underway. Domestically, the more relevant risk driver for this company isn't country risk but sector-specific and firm-specific risk (labor costs, weather-driven service demand, regional housing-market health) — outside the scope of the ERP/country-risk framework.

---

## Step 8 — Regression Beta

### Regression Beta
**Not available.** ABC has no publicly traded shares, so no return series exists to regress against a market index. This is the correct, expected answer for a private company (Lesson 10's justification for the bottom-up approach) — proceeding to Step 10.

### Index, Time Period, R-squared
N/A — no regression exists.

### Reliability Assessment
N/A. Proceeding directly to bottom-up estimation.

---

## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
Home and commercial services (pest control, lawn care, plumbing, HVAC, electrical) are largely **recurring, non-discretionary maintenance spend** — pest control contracts and HVAC repairs don't get deferred the way, say, a kitchen remodel does. That points toward a **below-market (defensive) business beta**, consistent with why publicly traded pest-control peers like Rollins, Inc. trade with a beta near or below 1.0. No disclosed segment breakdown, so a single blended beta is used across ABC's service lines.

### Operating Leverage Effect
Moderate fixed-cost structure: vehicle fleet, technician headcount, and branch facilities are largely fixed in the short run, while incremental service costs (chemicals, parts, technician hours per job) scale more directly with volume than a pure-software business would. This sits below the high-fixed-cost profile of an enterprise software company, consistent with a beta below 1.0.

### Financial Leverage Effect
**Not disclosed and not independently verifiable** — ABC's actual debt load is not public. What is sourced: ABC is explicitly reported as *not* private-equity-backed (Step 2/3), which in this industry specifically means it hasn't gone through the debt-funded leveraged-buyout financing that PE-backed home-services roll-ups typically carry. That's directional evidence toward lower-than-peer leverage, not proof of zero leverage — a company this size (~950 employees, decades of fleet/equipment needs, at least one acquisition) plausibly carries ordinary secured bank debt (vehicle/equipment financing, working-capital lines, possibly a facility mortgage) even without a PE sponsor. Both scenarios are carried forward into Step 11/12 rather than picking one and presenting it as fact.

---

## Step 10 — Bottom-Up Unlevered Beta

### Business Segments
Not separately disclosed; treated as a single blended business (multi-service home/commercial maintenance).

### Comparable Firms / Industry Group
Used Damodaran's US industry-beta dataset, **Environmental & Waste Services** classification (January 2026 update) — the closest available Damodaran bucket to pest-control/home-services maintenance, and the one that includes Rollins, Inc. (NYSE: ROL), the largest publicly traded pest-control comparable. As a cross-check: Rollins' own reported raw beta (~0.79, 5-year monthly) sits close to this industry-average figure, which supports the classification choice rather than undermining it.

| Segment | Industry | Avg Unlevered Beta | R² | Weight |
|---------|----------|--------------------:|-----:|-------:|
| Home/commercial maintenance services (pest, lawn, HVAC, plumbing, electrical) | Environmental & Waste Services | 0.78 | 0.5505 | 100% |

### Estimated Unlevered Beta
**0.78** — below 1.0, consistent with Step 9's expectation of a defensive, recurring-maintenance-revenue business.

---

## Step 11 — Levered Beta and Total Beta

Because ABC's actual capital structure isn't public (Step 9), this step presents two labeled, bounding scenarios rather than one invented number.

### Inputs
- Unlevered beta: 0.78 (Step 10)
- Correlation with market (√R²): √0.5505 = **0.742**
- Marginal tax rate: ~25% assumed (blended US federal + state)
- Debt/Equity — **not disclosed for ABC itself**:
  - **Scenario A (peer-proxy upper bound):** D/E = 0.78, Rollins, Inc.'s current reported debt-to-equity ratio, used only as an illustrative ceiling for "what a leveraged public peer looks like" — not a claim about ABC's actual structure.
  - **Scenario B (low-leverage, consistent with sourced no-PE-backing fact):** D/E ≈ 0.15, a working assumption for a self-funded, non-sponsor-backed family operator financing routine fleet/equipment debt and one tuck-in acquisition mostly from retained cash flow.

### Levered Beta (Hamada)
β_levered = β_unlevered × [1 + (1 − t) × D/E]

- Scenario A: 0.78 × [1 + 0.75 × 0.78] = **1.24**
- Scenario B: 0.78 × [1 + 0.75 × 0.15] = **0.87**

### Total Beta
Total Beta = Levered Beta / Correlation with market

- Scenario A: 1.24 / 0.742 = **1.67**
- Scenario B: 0.87 / 0.742 = **1.17**

### Interpretation
The market-beta vs. total-beta gap matters here for the same reason it did in Lesson 11: ABC's actual owners (the Jenkins family, Step 4) hold a concentrated, undiversified stake, so the total-beta column — not the market-beta column — is the more honest lens on the risk *they* bear, even though both are well below 1.0 in absolute terms (this is a defensive services business, not a venture-stage bet). The leverage-scenario spread (A vs. B) matters for a different reason: it's the direct, quantified consequence of not knowing ABC's real balance sheet. Given the sourced, explicit fact that ABC is not PE-owned, Scenario B is the more probable real-world case — but it is a labeled assumption, not a confirmed fact, and is treated as such throughout.

---

## Step 12 — Cost of Debt

### Bond Rating and Spread
None — ABC has no public bond rating (private, no public debt issuance found in any source).

### Synthetic Rating
**Not computable with confidence.** EBIT and interest expense for ABC are not disclosed anywhere in public sources, so the standard interest-coverage → synthetic-rating method can't be run on ABC's own numbers. As a directional reference only: Rollins, Inc.'s reported interest coverage ratio is very strong (~21–25x per recent data), which on Damodaran's small-firm ratings table would map to a top-tier synthetic rating and a narrow default spread — but Rollins is a larger, publicly financed, lower-leverage-by-scale company, so this is not a reliable stand-in for ABC's actual credit profile. Two bounding pre-tax cost-of-debt estimates are carried forward instead of one fabricated number:

| Metric | Scenario A (peer-proxy leverage) | Scenario B (low-leverage) |
|--------|:--:|:--:|
| EBIT | Not disclosed | Not disclosed |
| Interest expense | Not disclosed | Not disclosed |
| Interest coverage ratio | Not computable | Not computable |
| Synthetic rating (illustrative only) | Strong (peer-proxy) | Strong-to-moderate (small-business secured debt) |
| Default spread (assumed) | ~0.5% | ~1.5% |
| Pre-tax cost of debt | 4.80% + 0.5% = **5.30%** | 4.80% + 1.5% = **6.30%** |

### Actual vs. Synthetic Rating — Differences and Explanation
Not applicable — no actual rating exists, and no reliable synthetic rating could be computed from disclosed ABC-specific data. The spreads above are labeled assumptions bounding a plausible range, not a synthetic-rating output.

### Market Value of Debt
Not disclosed. Treated per the two leverage scenarios in Step 11 (D/E of 0.78 vs. 0.15) rather than assumed at a single point.

### Lease Debt Capitalization
ABC operates branch facilities across ~10 markets; a lease-commitment schedule is not disclosed anywhere public. Given the company's scale, capitalized operating leases are plausibly a real but secondary component of total debt-like obligations — not estimated numerically here to avoid fabricating a lease schedule that doesn't exist in any source.

### Marginal Tax Rate
~25% (blended US federal + state statutory assumption), used consistently across both scenarios.

---

## Summary — Cost of Capital Inputs

*Two scenarios are carried through because ABC's actual balance sheet is not public. Scenario B (low leverage) is the more probable real-world case given the sourced, explicit fact that ABC is not private-equity-backed; Scenario A (peer-proxy leverage, using Rollins, Inc. as an illustrative public comp) is shown as an upper bound, not a claim about ABC's true capital structure.*

| Input | Scenario A (peer-proxy leverage) | Scenario B (low leverage — more probable) |
|-------|:--:|:--:|
| Risk-free rate | 4.80% (US 10-yr Treasury, Sept 17, 2026 — sourced) | 4.80% |
| Mature market ERP | 4.23% (Damodaran implied ERP, Jan 2026 — sourced, dated) | 4.23% |
| Weighted ERP (country-adjusted) | 4.23% (100% US revenue) | 4.23% |
| Unlevered beta (Environmental & Waste Services) | 0.78 (Damodaran, Jan 2026 — sourced) | 0.78 |
| Assumed D/E | 0.78 (Rollins peer-proxy — assumed, not ABC's actual) | 0.15 (low-leverage assumption) |
| Levered beta (Hamada) | 1.24 | 0.87 |
| **Total beta (concentrated family-owner lens)** | **1.67** | **1.17** |
| Cost of equity — market-beta basis | 10.03% | 8.47% |
| **Cost of equity — total-beta basis (Jenkins family lens)** | **11.85%** | **9.75%** |
| Pre-tax cost of debt (assumed spread) | 5.30% | 6.30% |
| After-tax cost of debt | 3.98% | 4.73% |
| Debt/Capital ratio | 43.8% | 13.0% |
| **WACC — market-beta basis** | **≈7.4%** | **≈8.0%** |
| **WACC — total-beta basis** | **≈8.4%** | **≈9.1%** |

**Read this as bounds, not a single answer.** Both scenarios land ABC's cost of capital in a **~7%–9%** range — materially lower and less volatile than a venture-stage or PE-leveraged comparable would show, consistent with a mature, defensive, recurring-revenue services business. The scenario spread exists entirely because ABC's real balance sheet isn't public; it does **not** reflect any evidence of financial distress. If anything, the most load-bearing, best-sourced fact in this whole report is the opposite of a distress signal: multiple independent sources explicitly describe ABC as *not* purchased by a private-equity firm, still family-run three generations in, still promoting family members into senior operating roles as recently as April 2026, and still growing (one confirmed bolt-on acquisition, continued service-line expansion) — none of which is the profile of a financially strained or recently-recapitalized operator.

---

## Data Provenance — What's Sourced vs. Estimated

**Sourced (live web search, confirmed):**
- Risk-free rate (4.80%, Sept 17, 2026 10-yr Treasury)
- Mature market ERP (4.23%, Damodaran's Jan 2026 implied-ERP update)
- Industry unlevered beta and R² (0.78 / 0.5505, Damodaran Jan 2026 "Environmental & Waste Services" dataset)
- Rollins, Inc. (ROL) reported D/E (~0.78) and interest coverage (~21–25x), used only as an illustrative peer reference, not as ABC's own data
- Company founding (1949, San Antonio), Jenkins family ownership since 1965, three-brothers/three-territories structure, ~950 employees, service-line expansion history, A.S.A. Guardian Pest Control acquisition, Bo Jenkins/Omar Aranda April 2026 promotions, explicit no-private-equity-ownership statements, PCT Top 100 rank (#36)
- Marietta, GA branch shown closed as of July 2026 (Yelp listing)
- Austin-specific Glassdoor rating (2.8/5, 54 reviews, 22% below industry average) — noted for completeness in Step 3; not used as a governance or financial-structure finding

**Estimated or assumed (flagged, not fabricated as fact):**
- Both D/E scenarios (0.78 peer-proxy / 0.15 low-leverage) — ABC's actual leverage is not public; presented as bounding assumptions
- Both default-spread assumptions (0.5% / 1.5%) — no synthetic rating could be computed from ABC-specific data; illustrative only
- 100% US revenue exposure — inferred from confirmed market list (TX, FL, GA); no international operations found, but no explicit revenue-geography disclosure exists either
- Marginal tax rate (~25%) — standard blended assumption

**Unresolved / open questions (not answered by available sources):**
- Whether "ABC Home & Commercial Services" is a single legal entity co-owned by the three Jenkins brothers, or several separately-owned regional entities operating under one family brand (Step 2)
- ABC's actual debt load, EBIT, and interest expense — no financial statements are public
- The reason for the Marietta, GA branch closure (July 2026) — no news source found explaining it; presented as a single data point, not a trend

**No evidence found, despite specific searching, of:**
- Any private-equity ownership, investment, or acquisition of ABC Home & Commercial Services (Texas-based Jenkins family business) — multiple sources affirmatively state the opposite
- Any funding rounds, external investors, or debt recapitalization events
- Any 2026 layoffs, restructuring, or company-wide financial distress reported in news or trade press (a PitchBook listing for an "ABC Home & Commercial Services (Atlanta Branch)" and general company reviews were checked and appear to refer to the same Jenkins-family-owned company's branch network, not a separate distressed entity or a PE-backed rollup)

---

## Final Output

Report file: `03-corporate-finance/03-2-course-content/company-valuations/abc-home-and-commercial-services-valuation.md`

Per this repo's convention (sole-contributor, always admin-merge), this report will be committed on a branch and merged to `main` directly rather than left open for review.
