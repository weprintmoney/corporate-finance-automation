# Company Valuation: Venn
*Applied Corporate Finance — Module 1 Analysis*

**Date:** September 16, 2026
**Analyst:** Charlcye Mitchell
**Course:** Corporate Finance — Module 1 (Damodaran Framework)
**Context:** Prepped live, ahead of an interview with Dvir Shapira (Chief Product Officer, Venn)

**Name collision flag:** "Venn" is also the rebrand of a Toronto fintech (formerly Vault, all-in-one financial platform for Canadian businesses, $21.5M Series A from Left Lane Capital, Feb 2025) — a completely different company. This report is about **Venn Software / Venn Technology Corporation (venn.com)**, the NYC-based BYOD/endpoint security company where Dvir Shapira is CPO. Confirmed via his LinkedIn + The Org listing him at "Venn Software."

---

## Step 1 — Company Overview

**Company:** Venn (legally Venn Technology Corporation, d/b/a Venn)
**Status:** Private, VC-backed
**Headquarters:** New York, NY
**Founded:** 2019, by **David Matalon** (CEO) and **Alex Osipov** (CTO)
**Core business:** "Secure Enclave" / **Blue Border** — creates an isolated, encrypted workspace on an employee's *personal* (unmanaged/BYOD) laptop that separates work apps and data from personal use on the same device, without full MDM (mobile device management) of the whole machine. Patented (per 2023 NewSpring release). Positioned against enterprise-browser vendors (Island, Palo Alto Prisma Access Browser/formerly Talon) and full-device MDM, and marketed heavily as a Zscaler/SASE alternative for the unmanaged-device gap. Target industries: BPOs, financial services, healthcare, legal, technology, education.
**Stated positioning (2026):** "Securing the distributed workforce in the age of AI."

**Key financials:** Not public. No revenue, EBIT, or balance-sheet figures disclosed — this is a small private company, several orders of magnitude thinner on public data than the OpenAI/SolarWinds reports in this folder. Steps 5–12 below lean on industry proxies rather than company filings; treat every rate as an estimate framework, not a precise output.

**Funding (as found, [VERIFY] — could not fully reconcile timeline):**
- $29M Series A led by **NewSpring Capital**. NewSpring's own press release describing this round is dated 2023, though Crunchbase/BankInfoSecurity references tie the round closer to the company's 2019 founding — the exact close date is inconsistent across sources and not resolved here.
- No later round (Series B+) surfaced in the time available. Given Dvir Shapira (a senior operator who built Incapsula/Imperva's Cloud WAF from $0 to hundreds of millions) joined as CPO in June 2022, it's plausible there's a later round not showing up in a quick search — worth listening for in the interview rather than assuming $29M is the total raised to date.

**Interviewer context — Dvir Shapira, CPO since June 2022:** Physics/EE undergrad + MBA, Tel Aviv University. Built Incapsula/Imperva's first Cloud WAF from zero to hundreds of millions in revenue in under ten years. Cisco Director of Product Management, Sept 2020–June 2022, immediately before Venn. He's a product-scaling operator, not a GTM/sales hire — expect the conversation to go toward product strategy, roadmap prioritization, and what "scaling from early-stage to category leader" actually requires, not deal mechanics.

---

## Step 2 — Corporate Governance

### Board of Directors
Only one board member surfaced publicly: **Hart Callahan** (per Preqin/PitchBook). [VERIFY] — could not independently confirm his firm affiliation in the time available, but a single NewSpring-appointed board seat is the expected structure for a company on one disclosed institutional round.

### Governance Assessment
Classic early-stage, founder-controlled structure: founder-CEO (Matalon) + a single lead-investor board seat, no independent directors, no public shareholders. There's no governance apparatus here comparable to OpenAI's dual-board structure or a public company's audit/comp committees — decisions run through the founder and the lead VC.

### Power Structure
Power sits with David Matalon operationally, with NewSpring Capital holding board-level oversight tied to its Series A stake. No evidence of a large, diversified investor base able to exert market discipline the way public shareholders would.

---

## Step 3 — Stated Objectives

### Stated Goals
No public statement of financial targets (normal for a private company with no disclosure obligation). The stated *mission* is security-outcome framed: protect distributed/BYOD workforces "in the age of AI."

### Inferred Focus (no financial targets disclosed)
Venn runs an aggressive SEO/content strategy — dozens of "vs. [competitor]" and "[competitor] alternatives" pages (Island, Talon, Zscaler, Hysolate, Menlo). That's a category-capture, demand-generation play: the company is optimizing for inbound pipeline and market-share/mindshare, not visible profitability. Consistent with a Series-A-stage company whose job is to prove growth for the next round, not to harvest margin yet.

---

## Step 4 — Share Classes and Marginal Investor

### Share Structure
Not public. Typical early-stage cap table structure inferred: founder common stock + employee option pool + Series A preferred (NewSpring Capital, possibly co-investors).

### Largest Shareholders
Founders (Matalon, Osipov) and NewSpring Capital.

### Marginal Investor
This is the step where the textbook answer breaks for a company like Venn. In a public-market DCF, the "marginal investor" is assumed to be a diversified institutional holder who only prices *market* (systematic) risk — which is the entire justification for using a market beta in CAPM. Venn has no such investor. Its actual capital providers are:
- **Venture investors** (NewSpring) who hold a concentrated, illiquid, non-diversifiable position in this one company and price it accordingly — VC return underwriting (often 30%+ target IRR at Series A) reflects total risk, not just market risk.
- **The founders themselves**, whose personal wealth is even more concentrated in the company than the VC's.

### Likely Diversification
Not diversified. **This is the single most important methodological flag in this report** — see Step 11, where it becomes load-bearing.

---

## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
USD — Delaware/New York incorporated.

### Revenue Currencies
Presumed ~100% USD. Target customer base (BPOs, financial services, healthcare, legal, education) and NYC HQ both point to a US-centric customer base; no disclosed international revenue.

### Analysis Currency and Rationale
USD — matches both reporting and revenue currency, no cross-currency adjustment needed.

### Risk-Free Rate
US 10-year Treasury yield: **~5.01%** as of September 15, 2026 — a notable regime shift; yields crossed 5% for the first time since July 2007 after the Fed's latest hike (Sept 2026), per contemporaneous reporting. Source: CNBC market coverage, Sept 16, 2026.

---

## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
Damodaran's implied ERP for the S&P 500 stood at **~4.2%** over the Treasury rate at the start of 2026 (his January data update). He now refreshes this monthly on his site; the exact September 2026 figure wasn't retrievable via search in the time available. **[VERIFY]** — use 4.2%–4.5% as a working range; note in the interview that you'd pull the live monthly number before finalizing, rather than presenting the range as precise.

### Method and Source
Implied ERP (forward-looking, market-price-based), not historical — Damodaran's preferred method. Source: aswathdamodaran.blogspot.com / Stern data page.

---

## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
Revenue mix — no better public measure available (no disclosed production/reserves; this is a software company).

### Geographic Breakdown
| Region/Country | % of Revenue | Country ERP |
|----------------|---------------|-------------|
| United States  | ~100% (assumed) | 0 (mature market, no added premium) |

### Weighted Average ERP
= Mature market ERP = **~4.2%–4.5%**, since exposure is effectively all US.

### Why ERP Might Change
If Venn expands internationally (plausible — enterprise security vendors expand into EU/UK for compliance-driven demand), a country-risk premium would need adding. No evidence of that yet.

---

## Step 8 — Regression Beta

**Not applicable.** Venn has no traded equity — there is no regression beta to compute or cite. This is the clearest marker that the standard CAPM/WACC toolkit is being adapted, not applied directly, for a company at this stage.

---

## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
B2B enterprise security SaaS, subscription revenue. Security spend has some "must-have" (breach/compliance-driven) defensiveness, but is still a discretionary IT line item that can get cut or delayed in a downturn — moderate-to-somewhat-high beta expectation, in line with application software broadly.

### Operating Leverage Effect
High fixed cost (engineering-heavy), low marginal cost per seat — typical SaaS operating leverage, which amplifies beta versus a low-fixed-cost business.

### Financial Leverage Effect
Likely minimal. No disclosed debt; early-stage companies on preferred-equity financing typically carry little to no interest-bearing debt (occasionally venture debt, not surfaced here). Financial leverage is not expected to be a material beta driver for Venn.

---

## Step 10 — Bottom-Up Unlevered Beta

### Comparable Firms / Industry Group
No segment split — Venn is a single-product security company. Using Damodaran's **Software (System & Application)** industry group (January 2026 data, 309 firms) as the closest available proxy — Damodaran doesn't publish a standalone "cybersecurity" bucket:

| Segment | Industry | Avg Unlevered Beta | Weight |
|---------|----------|---------------------|--------|
| Core (BYOD/endpoint security SaaS) | Software (System & Application) | 1.23 | 100% |

Illustrative public comps in the same demand space: CrowdStrike, Zscaler, Cloudflare, Palo Alto Networks (which now owns the former Talon enterprise-browser product Venn competes against directly).

### Estimated Unlevered Beta
**1.23** — adopted directly from the industry average; no company-specific adjustment justified given the absence of segment-level data.

---

## Step 11 — Levered Beta and Total Beta

### Inputs
- Unlevered beta: 1.23
- Industry average D/E: 5.58% (for reference)
- Venn's own D/E: likely ~0% — no disclosed debt
- Marginal tax rate: ~26–27% (US federal + NY combined statutory) — but see caveat below

### Levered Beta (Hamada)
With Venn's own D/E near zero, relevering barely moves the number: **levered beta ≈ 1.23–1.28** (the low end assumes Venn's actual near-zero leverage; the high end is what you'd get applying the industry-average D/E instead). Either way, this is the beta a **diversified public-market investor** would use to price Venn's risk.

### Total Beta
This is the number that actually matters for how Venn's own founders and its VC think about risk. Total beta = market beta ÷ (correlation of the stock with the market) — it strips out the diversification benefit, because a concentrated, illiquid holder (a founder or a Series-A VC) doesn't get that benefit. For a single-industry-comparable proxy like this, total beta typically runs **2–3x** the market beta. Applied here: **total beta ≈ 2.5–3.7**.

### Interpretation
Two very different "right answers" coexist, and the gap between them is the most decision-relevant number in this whole report:
- **Levered/market beta (~1.25):** what a diversified investor — public markets, if Venn ever lists — would use to price the stock.
- **Total beta (~3.0):** what Venn's founders and its VC actually bear, and the correct lens for their own decisions (how much personal risk they're carrying, why VC hurdle rates run so much higher than public-market costs of equity).

---

## Step 12 — Cost of Debt

### Bond Rating and Spread
None — private company, no rated public debt.

### Synthetic Rating
Cannot be computed — EBIT and interest expense aren't public. **[VERIFY]** — if Venn carries venture debt (common at this stage, e.g. from a Silicon Valley Bank-type lender), it isn't visible from public sources found here.

| Metric | Value |
|--------|-------|
| EBIT | Not disclosed |
| Interest expense | Not disclosed |
| Interest coverage ratio | N/A |
| Synthetic rating | Cannot estimate |
| Default spread | N/A |
| Pre-tax cost of debt | N/A |

### Actual vs. Synthetic Rating
N/A — no data either way.

### Market Value of Debt
Assumed ~$0 or immaterial, consistent with an equity-financed Series-A-stage company.

### Lease Debt Capitalization
Unknown — likely a modest NYC office lease; immaterial to WACC either way.

### Marginal Tax Rate
Statutory ~26–27% (US federal + NY), but note: pre-profitability startups typically carry accumulated net operating losses and a near-0% *effective cash* tax rate. Which rate to use depends on whether Venn is cash-tax-paying yet — unknown, flag as an assumption.

---

## Summary — Cost of Capital Inputs

| Input | Value |
|-------|-------|
| Risk-free rate | ~5.0% |
| Mature market ERP | ~4.2%–4.5% [VERIFY monthly figure] |
| Weighted ERP (country-adjusted) | Same as mature market (~100% US revenue) |
| Regression beta | N/A — not publicly traded |
| Unlevered beta (industry proxy) | 1.23 |
| Levered beta (market/diversified-investor lens) | ~1.25–1.28 |
| Total beta (founder/VC lens) | ~2.5–3.7 |
| Cost of equity — diversified-investor lens (CAPM) | ~5.0% + 1.25 × 4.3% ≈ **10.4%** |
| Cost of equity — founder/VC lens (total beta) | ~5.0% + 3.0 × 4.3% ≈ **18%+** (still below typical VC underwriting hurdles of 30%+, which price in illiquidity/failure risk beyond even total beta) |
| Pre-tax cost of debt | N/A — no disclosed debt |
| Debt/Capital ratio | ~0% |
| **WACC** | **≈ cost of equity, ~10–11%** under the diversified-investor lens; the number that actually governs internal capital-allocation decisions at Venn is much closer to the 18%+ founder/VC figure |

---

## What this is actually useful for in the interview

Dvir Shapira is CPO, not the CFO — this isn't likely to be a valuation quiz. Where this framework is genuinely useful:
- **The marginal-investor / total-beta point (Steps 4 and 11)** is the one piece of real insight here: it explains *why* a small, concentrated, VC-backed company's leadership makes different risk tradeoffs than a public-company PM would assume — relevant if the conversation goes toward "how do you think about prioritization/risk at a company this size."
- **The name-collision catch at the top** is a good instinct to bring, generally — verifying you're looking at the right company before building an opinion is a defensible habit to mention if the conversation touches research process.
- Everything from Step 8 onward (beta, cost of debt) is **industry-proxy estimation**, not Venn-specific fact — don't present the 10.4%/18% numbers as precise; they're a framework demonstration, not a claim about Venn's actual cost of capital.
