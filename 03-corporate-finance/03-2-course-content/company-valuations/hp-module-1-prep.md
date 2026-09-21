---
title: "HP (HWP/HPQ) — Module 1 Prep: Project Questions & Document Sourcing Plan"
status: active
owner: weprintmoney
created: 2026-09-11
last_updated: 2026-09-11
---

# HP — Module 1 Prep: Project Questions & Document Sourcing Plan
*Applied Corporate Finance — Module 1 (Foundations & Discount Rates, lessons 1–12), scoped to a Hewlett-Packard valuation covering the 1990s–2000s*

## Purpose

This is a prep document, not a finished analysis. It answers three things:

1. What questions does Module 1 actually require you to answer for the Cumulative Project?
2. What does the professor ask, verbatim, in the slide decks themselves?
3. For HP specifically, over a 1990s–2000s window, what documents answer those questions and where do you get them?

---

## 0. Three things to know before you start

**A. The project is cumulative across all 4 modules — this covers only the cost-of-capital quarter of it.** The syllabus weights the Cumulative Project at 40% of the grade and it isn't due until 2026-12-11. Module 1 (lessons 1–12) only builds the *cost of capital* inputs (risk-free rate, ERP, beta, cost of debt, WACC). Modules 2–4 (investment returns/financing, financing mix/dividends, intrinsic valuation) will need their own question-and-source pass later — worth doing this same exercise again once you're there.

**B. The repo's `/evaluate-company` skill is built for exactly this, but its file paths are stale.** [.claude/commands/evaluate-company.md](../../../.claude/commands/evaluate-company.md) walks through these same 12 steps automatically, but it still points at `03-corporate-finance/modules/module-1/lesson-NN/...` and `03-corporate-finance/modules/company-valuations/...` — both paths from before a repo reorg. The real paths are `03-corporate-finance/03-2-course-content/01-foundations-and-discount-rates/lesson-NN/` and `03-corporate-finance/03-2-course-content/company-valuations/`. I didn't fix it yet — say the word and I will (it's a ~15-line path find/replace, low risk) — but as written today, running `/evaluate-company` will fail to find its own reading material.

**C. HP-specific anchors, confirmed directly against SEC EDGAR** (CIK `0000047217`, ticker `HPQ`; traded as **HWP** on the NYSE before the Compaq merger):
- Fiscal year ends October 31 (10-Ks file ~Jan–Feb for the prior FYE, shifting to Dec by FY2005 as accelerated-filer deadlines tightened).
- **Earliest 10-K on EDGAR: filed 1994-01-28** (FY1993). Nothing earlier is on EDGAR — 1990–1992 needs non-SEC sources (see §3).
- The **Compaq merger** (announced Sept 2001, shareholder vote March 2002, closed May 2002) was a genuinely contested proxy fight — Walter Hewlett (son of co-founder) publicly opposed it and ran a dissident campaign. HP filed a **DEFC14A** (contested proxy) on **2002-02-05**. This is an unusually good primary source for the governance/objectives/marginal-investor lessons (2, 3, 4) — most companies never generate a document like this.
- Agilent Technologies was spun off from HP in 1999 (test-and-measurement business) — relevant to the "corporate life cycle" framing in Lesson 1.

---

## 1. Lesson-by-lesson: the professor's question, the project's version, and the HP angle

For each lesson: the verbatim **Task** from `slides.md` (the professor's own application-test prompt), the corresponding numbered question(s) from the `/evaluate-company` skill (the operationalized version), and a one-line note on why it's interesting for HP specifically.

### Lesson 1 — Valuation: The Big Picture / What is Corporate Finance?
No "Task" slide (it's the framing lesson). The skill's Step 1 is just "pick a company." **HP angle:** worth using this lesson's "corporate life cycle" framework to place HP explicitly — mature hardware/printing business generating cash (assets in place) vs. whatever HP was investing in as growth (enterprise/services in the 2000s, before Agilent and the eventual 2015 HP/HPE split). Not a required deliverable, but useful framing for everything after it.

### Lesson 2 — The Objective: Utopia and Let Down (Corporate Governance)
**Slide Task:** *"Assess corporate governance at your company"* — sub-prompts: *Who are the top stockholders in your firm? What are the potential conflicts of interest that you see emerging from this stockholding structure?*
**Project Step 2 asks:**
1. Who sits on the board of directors?
2. Whose interests are they most likely to serve?
3. What does any corporate-governance-strength measure reveal about where power lies?
**HP angle:** the Compaq DEFC14A and the ordinary DEF 14A proxies bracketing it (2001, 2002) are a rare chance to answer this with a real contested vote rather than a hypothetical — Walter Hewlett sat *on the board* while publicly opposing management's deal.

### Lesson 3 — The Objective: Reality and Reaction (Stated Objectives)
**Slide Task:** *"Based on its actions, assess your company's objective"*
**Project Step 3 asks:**
1. If the firm has stated goals, what is it targeting — growth, profitability, stock price, or value?
2. If no stated goals, what does behavior suggest?
**HP angle:** Carly Fiorina's stated rationale for the Compaq deal (scale, cost synergies, competing with Dell/IBM) vs. Walter Hewlett's public argument that it destroyed value — you have both sides' own words on the record.

### Lesson 4 — Define and Measure Risk (Share Classes / Marginal Investor)
**Slide Task:** *"Who is the marginal investor in your firm?"*
**Project Step 4 asks:**
1. How many share classes, and voting rights of each?
2. Who are the largest shareholders?
3. Individual or institutional marginal investor?
4. Is that investor likely diversified?
**HP angle:** HP has a single share class (no supervoting founder stock) — confirm this from the proxy, don't assume it. The genuinely interesting part is the Hewlett and Packard family trusts/foundations, which were large, publicly-tracked blockholders during the merger vote — a good real example of a non-diversified, non-institutional holder sitting alongside index-fund-scale institutional ownership.

### Lesson 5 — The Risk-Free Rate
**Slide Task:** *"Estimate the risk-free rate in the currency of your choice"*
**Project Step 5 asks:**
1. Reporting currency?
2. Revenue currencies?
3. Analysis currency and why?
4. Current (i.e., era-appropriate) risk-free rate in that currency?
**HP angle:** straightforward — USD reporting, but meaningfully international revenue even in the 1990s. The only real work is pulling the *historical* 10-year Treasury yield for whatever valuation date you pick, not today's.

### Lesson 6 — Equity Risk Premiums
**Slide Task:** *"Estimate the historical equity risk premium in the market of your choice (if you can)"*
**Project Step 6 asks:** what's the ERP for a mature market (US) as of the analysis date, method (implied vs. historical), and source?
**HP angle:** no HP-specific work here — this is a market-wide number for whatever year(s) you pick, historical not current.

### Lesson 7 — Country Risk Premiums
**Slide Task (Application Test 6):** *"Estimate the ERP for your company (based on exposure)"* — also: *"With your company, what concerns would you have about your [revenue-based] estimate being too high or too low?"*
**Project Step 7 asks:**
1. Best measure of country risk exposure (revenue, production, etc.)?
2. Geographic breakdown?
3. Weighted-average ERP using country ERPs?
4. Why might this change in the future?
**HP angle:** HP's geographic revenue split (10-K segment/geographic footnote) — this is one of the harder items historically, see §3.

### Lesson 8 — Regression Betas
**Slide Task (Application Test 6):** the most detailed prompt in Module 1 — point estimate and 67%/95% confidence range for beta, R², proportion of risk market vs. firm-specific, Jensen's alpha, and the implied required return.
**Project Step 8 asks:** the regression beta, index/period/R², and a reliability assessment.
**HP angle:** you need an actual monthly-return regression of HWP/HPQ against the S&P 500 for whichever window you're studying — this is the item most dependent on getting real historical price data (see §2).

### Lesson 9 — Beta Fundamentals
**Slide Task:** *"Evaluate the business risk, operating leverage and financial leverage for your company"*
**Project Step 9 asks:**
1. Product/service mix → expected beta (high or low)?
2. Cost structure (fixed vs. variable) → expected beta?
3. Financial leverage's effect on beta?
**HP angle:** hardware manufacturing (higher fixed-cost, higher operating leverage) blended with services/printing supplies (much more variable, higher-margin, lower operating leverage) — a genuinely mixed-business case, and the mix shifted over the two decades.

### Lesson 10 — Bottom-Up Betas
**Slide Task:** *"Estimate a bottom-up beta for your company"*
**Project Step 10 asks:** comparable-firm unlevered beta, segment weighting if multi-business, showing the comp set and math.
**HP angle:** the comp set has to be era-appropriate — Dell, IBM, Compaq (pre-merger), Sun Microsystems, Gateway, Apple, NCR — not today's peer set.

### Lesson 11 — The "Right" Beta (Total Beta)
**Slide Task:** *"Estimate the beta your company would have, if it were a private business"*
**Project Step 11 asks:** levered beta (Hamada), total beta, and what the gap between them implies.
**HP angle:** HP was always public and broadly held in this window (not a concentrated PE-style owner), so the standard levered beta is the operative number — total beta is worth computing for the exercise but isn't the realistic discount rate here, unlike, say, a founder-controlled or PE-owned company.

### Lesson 12 — Debt: Measure and Cost
**Slide Task (Application Test 6):** *"Estimate the cost of debt for your company"*
**Project Step 12 asks:** actual bond rating and spread; synthetic rating via interest coverage; reconciling the two; market value of debt; lease-debt capitalization; marginal tax rate — plus the final WACC summary table.
**HP angle:** HP ran with very little leverage and a strong credit rating through most of this period (verify the actual rating/spread rather than assuming — see §2) — a useful contrast case to a highly-levered company.

---

## 2. Document & data sourcing map (HP, 1990s–2000s)

**Status: primary sources now compiled locally in [`hp-sources/`](hp-sources/)** — see [`hp-sources/README.md`](hp-sources/README.md) for the full manifest (9 SEC filings including the Compaq contested proxy, plus historical Treasury/HPQ/S&P 500 price series). The table below still names where each item came from; anywhere it's now sitting in `hp-sources/` is noted inline.

| Need | Where to get it | Notes for this era |
|---|---|---|
| **10-Ks, 10-Qs, 8-Ks (financials, MD&A, segment data, debt footnotes)** | [SEC EDGAR — HP Inc, CIK 0000047217](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000047217&type=10-K) — **7 fetched: `hp-sources/sec-filings/hp-10k-fy{1993,1996,1999,2001,2002,2005,2009}.md`** | Confirmed: earliest 10-K is **1994-01-28** (FY1993). FY1993 and FY1996 incorporate financials by reference to Exhibit 13 — the companion `-ex13-annual-report.md` files carry those. FY1999 onward, statements are in the 10-K body directly. |
| **Ordinary annual proxy (DEF 14A)** — board composition, exec comp, share structure | Same EDGAR company page, filter `DEF 14A` — **fetched: `hp-sources/sec-filings/hp-def14a-2001.md`** (filed 2001-01-25, immediately pre-merger-announcement) | Filed every January in this period; refetch other years the same way if needed. |
| **Compaq merger — the contested proxy fight** | EDGAR: `DEFC14A` filed **2002-02-05** — **fetched: `hp-sources/sec-filings/hp-defc14a-2002.md`** | Turned out to be **Walter Hewlett's own dissident filing**, not management's proxy — a board member's own campaign against his company's deal, on the record. This is the single richest document for Lessons 2–4. |
| **Historical stock price / total return series (for the beta regression, Lesson 8)** | **Fetched: `hp-sources/market-data/hpq-monthly-prices-1990-2009.csv`** and the matching `sp500-monthly-prices-1990-2009.csv` — 240 monthly observations each, via Yahoo Finance's chart API | Stooq (originally suggested here) blocks automated fetches behind a JS challenge — Yahoo's API worked directly with no auth, and unlike a delisted ticker, HP's continuous HWP→HPQ history came through with no gap. |
| **Risk-free rate, historical (Lesson 5)** | **Fetched: `hp-sources/market-data/dgs10-daily-1989-2009.csv`** — [FRED DGS10](https://fred.stlouisfed.org/series/DGS10), daily, 1989–2009 | Free, exact — pull the rate as of whatever specific valuation date(s) you choose from this file. |
| **Equity risk premium, historical (Lesson 6)** | Damodaran's own site — historical implied ERP by year (Data page, "Historical Returns"/"Implied ERP by year" datasets), `pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html` | Important: the repo's `03-3-supplemental-data/industry-betas.json` and `country-risk.json` are **current-year snapshots only** (and are currently empty stubs — the CI refresh appears broken, same issue flagged in the SolarWinds question log). Even if fixed, they wouldn't help here — you need the *historical by-year* series, which lives in Damodaran's data archive, not the CI-refreshed current file. |
| **Country risk premium, historical (Lesson 7)** | Same Damodaran data page — but flag: his formal country-risk-premium-by-country tables are reliably archived from roughly 1999–2002 onward; earlier years may only support a simple mature-market-ERP approximation (no country adjustment) rather than a true country-weighted ERP. Decide and state this as an assumption. |
| **Bond rating / credit spread history (Lesson 12)** | HP's own 10-Ks (MD&A "Liquidity and Capital Resources" sections usually state the then-current S&P/Moody's rating); Moody's/S&P historical rating actions (subscription, or via Capital IQ once you have access); WSJ/NYT archives for rating-change news if you need exact change dates | If a formal rating history isn't accessible, the synthetic-rating method (interest coverage ratio → rating table, already spelled out in Step 12) is a full substitute and only needs HP's own EBIT/interest-expense from the 10-K. |
| **Comparable-firm data for bottom-up beta (Lesson 10)** | Same EDGAR approach applied to era-appropriate peers — IBM, Dell, Compaq (pre-2002), Sun Microsystems, Gateway, Apple, NCR | Pull each comp's own 10-K/proxy for the relevant year rather than using today's industry-average beta datasets, which reflect today's industry composition, not the 1990s/2000s one. |
| **Geographic/segment revenue mix (Lesson 7, 9)** | 10-K "Segment Information" / geographic footnote (usually in Notes to Consolidated Financial Statements) | Present in HP's 10-Ks throughout this window. |
| **Narrative / qualitative context (stated objectives, CEO framing, life-cycle positioning)** | HP's own annual reports (glossy shareholder-letter version, distinct from the 10-K) — HP's investor relations archive, [annualreports.com](https://www.annualreports.com), or the Wayback Machine's archive of HP's investor site; contemporaneous WSJ/NYT/Fortune coverage of the Compaq fight | Useful for Lessons 1–3; not required for the quantitative cost-of-capital work. |

---

## 3. Known gaps — decide these before you start, don't discover them mid-project

- **1990–1992 is a real gap.** EDGAR has nothing for HP before the 10-K filed 1994-01-28 (FY1993). If your "1990s" window needs to reach back that far, you'll need a non-SEC source — Moody's Industrial Manual (library/archive.org), ProQuest historical annual reports, or simply narrow the stated window to FY1993 onward and say so explicitly in the report's methodology section.
- **The repo's CI-refreshed supplemental-data files are currently broken/missing** (`market-rates.json` doesn't exist, `industry-betas.json` and `country-risk.json` are empty stubs — the same issue independently found and documented in `solarwinds/README.md`). This doesn't actually cost you anything here, since those files only ever held *current* data and this project needs *historical* data regardless — but don't waste time checking them expecting HP-relevant content.
- **Ticker discontinuity (HWP → HPQ)** around the 2002 merger can trip up naive historical-data pulls — confirm whichever price-history source you use is stitching the pre- and post-merger series together correctly rather than truncating at the ticker change.
- **Country-level ERP data thins out the further back you go** — see the Lesson 7 row above. Pick a defensible simplification and state it rather than forcing false precision.

---

## 4. Suggested order of operations

1. Decide on the specific valuation date(s) — the "1990s and 2000s" framing spans ~20 years; Module 1's inputs (risk-free rate, ERP, beta) all require picking a specific point (or a couple of points, e.g. pre- and post-Compaq-merger) rather than one blended "the 1990s–2000s" number.
2. If you want to run this through the repo's `/evaluate-company` skill automatically, say so and I'll fix its stale paths first (see §0-B).
3. Pull the HP EDGAR filing set for your chosen date(s) — 10-K, proxy, and (if your window includes early 2002) the DEFC14A — as your primary source packet, mirroring how `solarwinds/sources/` was organized for the SolarWinds pass.
4. Get the historical stock-price series for the beta regression — the one item most worth sourcing early, since it's the slowest to chase down if a free source falls short.
5. Work lessons 1–12 in order using the table in §1 — each lesson's Task/Step is designed to be answerable from the sources in §2.
