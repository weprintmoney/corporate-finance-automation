---
title: "Dynatrace, Inc. — Module 1 Valuation: Cost of Capital Analysis"
status: active
owner: weprintmoney
created: 2026-09-28
last_updated: 2026-10-07
---

# Company Valuation: Dynatrace, Inc.
*Applied Corporate Finance — Module 1 Analysis*

**Refreshed 2026-10-07 with S&P Capital IQ data.** The 2026-09-28 version of this report was built from SEC filings and free aggregator sites. This version replaces the market, ownership, capital-structure and geography inputs with Capital IQ pulls dated 2026-10-07 (classic platform, company ID 628406634), and it changes three conclusions:

1. **"No funded debt" is no longer true.** On 2026-08-20 Dynatrace LLC closed **$1.4375B of 0.00% Exchangeable Senior Notes due 2031**. Steps 9, 11 and 12 are rebuilt around that.
2. **The risk-free rate is netted.** Following the Meetup 2 lens this repo applied to SolarWinds on 2026-10-06, the risk-free rate is the 10-year Treasury less Damodaran's 0.22% US default spread, and US revenue carries a 4.46% equity risk premium (4.23% mature premium plus a 0.23% US country risk premium).
3. **The Arize acquisition has closed** (2026-10-01), so the balance sheet is shown pro forma for the notes and the purchase.

A **"What changed"** table sits directly under the Summary. Capital IQ's latest reported balance sheet is 2026-06-30, which predates both the notes and the Arize close; every pro forma figure is flagged as an estimate. Capital IQ consensus estimates are deliberately not reproduced in this public repo. Damodaran inputs (industry beta, ratings table) still come from the spreadsheets checked into the Lesson 10 and 12 folders, because `industry-betas.json` and `country-risk.json` are still empty stubs.
---

## Step 1 — Company Selected

**Dynatrace, Inc.** (NYSE: DT) — an AI-powered, cloud-native "unified observability and security" software platform (application performance monitoring, infrastructure monitoring, log analytics, digital experience, and security), founded in 2005, headquartered in Waltham, Massachusetts, ~5,600 employees (2026), roughly 4,100 customers. Originally a Compuware product line, carved out and taken private by Thoma Bravo in 2014, then IPO'd on NYSE in August 2019. Fiscal year ends March 31.

FY2026 (ended March 31, 2026): revenue **$2,018.4M, +19% reported / +17% constant currency** (the prior version of this report said +16%; that was wrong), ARR $2,053.6M at year-end and $2,136.0M at 2026-06-30 (+17%), net retention 110%, GAAP operating margin 12%, non-GAAP operating margin 29%. Last twelve months to 2026-06-30 per Capital IQ: revenue $2,095.6M, EBITDA $291.4M, EBIT $273.1M, net income $151.4M, cash from operations $598.4M, capex $27.8M, stock-based compensation $301.3M (14.4% of revenue), R&D $509.0M (24.3%).

| Market snapshot (Capital IQ, 2026-10-07) | Value |
|---|---:|
| Share price | $59.81 |
| Shares outstanding | 289.0M |
| Market capitalization | $17,285M |
| Cash and short-term investments (2026-06-30) | $1,108.9M |
| Long-term marketable securities (2026-06-30) | $47.1M |
| Total debt (2026-06-30, operating leases only) | $159.3M |
| Float | 99.3% |

**The Arize AI acquisition closed on 2026-10-01** — $915 million (~$815M cash plus replacement equity awards), signed 2026-08-13. Dynatrace guided it as ~200 basis points accretive to FY2027 ARR growth (~$40M) and ~175 basis points dilutive to FY2027 non-GAAP operating margin, with margin expansion resuming from FY2028. Arize's co-founders (Jason Lopatecki and Aparna Dhinakaran) joined Dynatrace; Lopatecki continues to lead the Arize team reporting into CEO Rick McConnell's organization.

**Five days after signing Arize, Dynatrace priced its first funded debt since 2022** — the exchangeable notes described in Step 12 — and on 2026-09-24 signed a new credit agreement. The purchase was therefore financed with convertible debt, not the revolver draw the prior version of this report assumed.
---

## Step 2 — Corporate Governance

### Board of Directors
Per the FY2026 DEF 14A (filed 2026-07-10, annual meeting 2026-08-26), Dynatrace's board has **10 directors, 9 of whom are independent**, organized as a **classified (staggered) board** — only one class stands for election each year. The 2026 Class I nominees were **Rick McConnell** (CEO), **Michael Capone**, **Stephen Lifshatz**, and **George Riedel**. The board maintains a dedicated **Cybersecurity Committee**, notable given Dynatrace's security-adjacent product surface.

Two directors were added in quick succession in mid-2026: **George Riedel and Dan Streetman** (effective July 1, 2026) "following constructive and collaborative engagement with Starboard Value LP," and **Chandu Thota** (effective July 27, 2026), a 20+-year AI/cloud-infrastructure executive with a Google/Microsoft background. This timing is not incidental — see below.

### Governance Assessment
Dynatrace was a Thoma Bravo **"controlled company" at IPO**: per the 2019 S-1/424B4, Thoma Bravo funds held ~59.6%–69.3% of voting power pre-offering; per the 2020 secondary-offering prospectus, ~52.1% post-offering. Controlled-company status under NYSE rules meant the board did not need an independent majority or independent nominating/compensation committees at that time. **That era is over.** Per Dynatrace's own proxy disclosures, Thoma Bravo's stake had fallen to under 5% by mid-2024 (see Step 4) — the board is now majority-independent (9 of 10) and no single sponsor controls it.

The classified-board structure is, on its own, a management-entrenching feature in the Lesson 2/3 governance taxonomy (it slows a takeover or a full board replacement to multiple annual cycles). In practice, though, an activist investor — **Starboard Value LP**, which disclosed a "significant stake" in Dynatrace in April 2026 and publicly (via a letter from managing member Peter Feld) argued the stock was undervalued versus peers and pushed for margin expansion, a much larger buyback ($2.5B+ over three years, versus the $1B program Dynatrace had just announced in February 2026), and consideration of "all options to maximize shareholder value" — won two board seats within about nine weeks, without a proxy contest reaching a shareholder vote. That is a real (if imperfect) demonstration of shareholder accountability operating alongside a nominally entrenching board structure.

### Power Structure
Two distinct forces are visible in 2026: (1) a large, diversified institutional shareholder base (BlackRock, Vanguard, etc. — see Step 4) that is largely passive and price-taking, and (2) a concentrated activist (Starboard) that is actively and successfully steering capital-allocation decisions via board representation. The party setting Dynatrace's share price on the margin (diversified index/active managers) and the party currently disciplining management's capital-allocation choices (a concentrated activist) are not the same investor — a live instance of the tension Lessons 2 and 3 ask you to identify.
---

## Step 3 — Stated Objectives

### Stated Goals
Management has stated a combined growth-and-profitability target: having discussed a "Rule of 40" framework historically, Dynatrace announced it will hold an **Investor Day following its Q2 FY2027 results to lay out a path to "Rule of 50" by fiscal 2029** — i.e., an explicit target that revenue growth plus non-GAAP operating margin should sum to 50, not a pure growth or pure stock-price framing. Separately, under direct activist pressure, management reiterated a shareholder-return commitment: it completed a $500M buyback program in February 2026 (11.4M shares repurchased for $478.7M in FY2026) and immediately authorized a new **$1B program** the same month; it repurchased a further $275M of stock (7.1M shares) in Q1 FY2027 alone.

### Inferred Focus (Tension With Stated Goals)
Here is the tell: **six weeks after Starboard's directors joined the board** (2026-07-01 to 2026-08-13) — an investor explicitly asking for *more* capital discipline and *less* strategic spending — Dynatrace signed the $915M Arize deal, which management itself disclosed as ARR-accretive but margin-dilutive for FY2027. Buybacks continued in parallel (Q1 FY2027 repurchases occurred before the Arize signing). Read together, this is not "stock price maximization" in the simple textbook sense, nor is it pure capital-return discipline as Starboard wanted. It looks like management is pursuing **category-leadership / strategic-value maximization** (first-mover claim on the emerging "AI observability" layer, ahead of Datadog or others building or buying the same capability) while *simultaneously* trying to keep the activist's capital-return ask satisfied — a genuine attempt to do both at once, which is exactly the kind of real-world conflict-of-objectives Lesson 3 asks you to name rather than paper over.

### Update 2026-10-07 — How the tension was financed
The financing makes the "do both at once" reading concrete. Capital IQ shows **$728.3M of buybacks in the twelve months to 2026-06-30**, against $570.6M of free cash flow (cash from operations less capex). Then, alongside the notes, Dynatrace repurchased about 2.83M more shares at $47.61 (~$134.7M) and paid ~$145.9M for a note hedge. Management returned more cash than the business generated, bought Arize, and filled the gap with zero-coupon exchangeable debt. The stated "Rule of 50 by fiscal 2029" target is the scoreboard that has to justify it; the Investor Day that will lay out the path has not happened yet.
---

## Step 4 — Share Classes and Marginal Investor

### Share Structure
**Single class of common stock, one vote per share** — confirmed via Dynatrace's 2019 S-1/424B4 and 2020 424B4 secondary-offering prospectuses. No dual-class structure. **289.0M shares outstanding** (Capital IQ, 2026-10-07; 290.2M at the July 6, 2026 proxy record date, before the August repurchase).

### Largest Shareholders (Capital IQ ownership summary, 2026-10-07)

| Holder | % of shares | Type |
|---|---:|---|
| BlackRock | 12.09% (34.95M shares) | Index / diversified |
| Vanguard Portfolio Management | 5.47% | Index / diversified |
| Vanguard Capital Management | 5.22% | Index / diversified |
| UBS Asset Management | 5.02% | Diversified |
| Pictet Asset Management | 4.95% | Active, diversified |
| **Starboard Value** | **3.07% (8,866,692 shares)** | Activist, concentrated |
| D.E. Shaw | 1.35% | Hedge fund |

By holder type: traditional investment managers 81.4%, hedge funds 11.9%. **Thoma Bravo does not appear among the top holders**, which settles the question the prior version left open: the "50.6%" figure still served by aggregator sites is the 2020 number and should be ignored.

The prior version could only describe Starboard's stake as "significant". Capital IQ puts it at **3.07%**. Capital IQ's activism screen records the Starboard campaign as launched 2026-04-27 and "Successful" on 2026-07-01, and a separate Pictet campaign dated 2026-01-16 with status "Announced". A 3% holder won two board seats in about nine weeks.

### Marginal Investor
Large, diversified institutional asset managers (index funds and active managers) — not a founder/sponsor bloc. With a 99.3% float there is no controlling holder at all.

### Likely Diversification of Marginal Investor
Highly diversified. BlackRock, Vanguard, UBS and Pictet hold DT as one position among thousands. This supports using **market (levered) beta**, not total beta, as the discount-rate input — see Step 11. The qualifier stands: Starboard is concentrated and is actively shaping capital allocation, even though at 3.07% it is not the investor setting the price.
---

## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
**USD.** Dynatrace is a US SEC filer reporting under US GAAP.

### Revenue Currencies
Materially mixed, and disclosed: Dynatrace stated in its Q1 FY2027 commentary that **"nearly 40% of the company's business [is] denominated in foreign currency,"** citing a $23M incremental FY2027 ARR headwind from USD strength. Capital IQ's geographic segments (Step 7) put 54% of FY2026 revenue outside the United States.

### Analysis Currency and Rationale
USD — matches the reporting currency and the currency of the new notes.

### Risk-Free Rate
**5.06%** — the US 10-year Treasury par yield of **5.28% on 2026-10-07** (it traded above 5.35% intraday, the highest since 2002) **less Damodaran's 0.22% US default spread**.

Why net it: the US is no longer rated Aaa by Moody's, so the Treasury yield includes a small default premium and is not a clean risk-free rate. Damodaran's 2026 equity risk premium for the US (4.46%) already carries a 0.23% US country risk premium. Using the gross 5.28% and the 4.46% together would count US default risk twice. This is the same adjustment this repo made for SolarWinds on 2026-10-06. The prior version of this report used the gross 5.20%.

The Treasury has risen 8 basis points since the 2026-09-28 version and 27 since the mid-September MinIO report.
---

## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
**4.23%** — Damodaran's implied ERP at the start of 2026 (S&P 500 at 6,845.5; expected return on stocks 8.41% minus the then 10-year T-bond rate of 4.18%).

### Method and Source
Implied (forward-looking) ERP: solve for the discount rate that equates the current index level to the present value of expected future cash flows, then subtract the risk-free rate. Damodaran updates it monthly. The later readings found were **4.37% at the start of March 2026 and 4.51% in mid-March 2026**. **The October 2026 figure was not found.** This report stays on the January 4.23% so it matches the 0.22% / 0.23% US spread figures and the SolarWinds work, and shows the sensitivity instead: each 0.25 point on the ERP moves Dynatrace's bottom-up cost of equity by about 0.33 points. At 4.51% the bottom-up WACC would be about 11.4% rather than 11.1%.
---

## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
Revenue by customer geography — standard for an enterprise software company.

### Geographic Breakdown
Capital IQ geographic segments, FY2026, $2,018.4M total. Capital IQ splits the United States from the rest of North America, which the prior version (10-K continent-level percentages) could not.

| Region | Revenue ($M) | % of Revenue | ERP used |
|--------|-------------:|-------------:|----------|
| United States | 927.7 | 46.0% | 4.46% (4.23% + 0.23% US country risk premium) |
| North America ex-US | 89.8 | 4.4% | 4.23% (Canada, Aaa) — estimated |
| EMEA | 648.9 | 32.1% | ≈4.6% — estimated |
| Asia Pacific | 193.1 | 9.6% | ≈5.0% — estimated |
| Latin America | 158.9 | 7.9% | ≈7.5% — estimated |

**Caveat, unchanged:** neither the 10-K nor Capital IQ gives country-level revenue, and `country-risk.json` is an empty stub, so the non-US regional premiums are estimates from standard Damodaran-style groupings.

### Weighted Average ERP
0.460×4.46% + 0.044×4.23% + 0.321×4.6% + 0.096×5.0% + 0.079×7.5% = 2.05% + 0.19% + 1.48% + 0.48% + 0.59% = **≈4.79%**, rounded to **≈4.8%** (prior version: ≈4.7%, with the US at 4.23%).

### Why This ERP Might Change
Arize's customers are largely US-based AI engineering teams, so the acquisition tilts the mix toward the US at the margin. The larger effect runs the other way over time: 54% of Dynatrace revenue is outside the US, and 32% is in EMEA, where the EU AI Act obligations fall. Latin America at 7.9% of revenue contributes 12% of the weighted premium.
---

## Step 8 — Regression Beta

### Regression Beta
**0.77** — Capital IQ 5-year beta, 2026-10-07. Free sources a week earlier showed 0.71–0.74 (stockanalysis.com, Yahoo Finance). The prior version used ≈0.72.

### Index, Time Period, R-squared
5 years of returns against the S&P 500. **R-squared is still not found**: Capital IQ's tearsheet shows the beta without regression statistics, and the Chart Builder that would produce them is broken in this account.

### Reliability Assessment
A 0.77 beta says Dynatrace moves less than the market, while Damodaran's "Software (System & Application)" bucket (Step 10) has an unlevered beta of 1.27 and Datadog's Capital IQ beta is 1.51. Two explanations compete: (1) the business is more defensive than the median software name — contracted ARR, 110% net retention, 27% free-cash-flow margin, and for most of the window a net-cash balance sheet with heavy buybacks; or (2) the window is unrepresentative — it spans the 2022 software drawdown, the 2023–2025 recovery, and a 2026 in which an activist campaign and a re-rating drove the stock on company-specific news, which lowers correlation with the index and therefore beta. The second reading matters more now: the 52-week move from $31.64 to about $60 is mostly Starboard, the buyback and Arize, not the market. Treat 0.77 as a soft input.
---

## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
Dynatrace sells a recurring-revenue, subscription-based observability platform embedded in customers' production infrastructure — high switching costs, low short-run demand elasticity, but tied to enterprise IT and cloud budgets. Expect a **moderate** business beta, below the broader software average. No separately disclosed business segments, so a single blended beta is appropriate. Arize adds a younger, usage-driven, AI-budget-exposed revenue line; at ~$40M of ARR against $2.14B it is under 2% of the base and does not move the blended beta yet.

### Operating Leverage Effect
High fixed-cost structure: R&D is 24.3% of revenue and stock-based compensation 14.4% (Capital IQ, LTM). GAAP operating margin is ~13% against ~29% non-GAAP; the gap is mostly stock-based compensation and acquisition amortization, which will grow with Arize. High fixed costs push beta up; a contracted ARR base pulls realized volatility back down.

### Financial Leverage Effect
**Changed since the prior version.** Dynatrace had no funded debt from December 2022 until 2026-08-20, when it closed $1.4375B of 0.00% exchangeable notes (Step 12). On the convertible-split treatment in Step 11, debt is now about 6.5% of capital and lifts the bottom-up beta from 1.27 to 1.34. It is still a lightly levered company. The more meaningful change is the cash position: about $1.16B of cash and securities and no funded debt at 2026-06-30 has become, on this report's pro forma estimate, roughly $1.5B of cash against $1.6B of debt and leases. **Net cash of about $1.0B has become roughly zero.**
---

## Step 10 — Bottom-Up Unlevered Beta

### Business Segments
Not separately reported; treated as a single business (unified observability/AIOps platform software) both today and, until Dynatrace begins segment reporting for it, after the Arize close.

### Comparable Firms / Industry Group
The direct pure-play comp set has shrunk materially since the course's underlying Damodaran datasets were built: **New Relic** was taken private (TPG/Francisco Partners, 2023) and **Splunk** was acquired by Cisco (2024) — neither trades independently anymore. That leaves **Datadog (DDOG)** as the main remaining large pure-play public comp, alongside Dynatrace itself and smaller names (e.g., Elastic) — too thin a set to average directly with any statistical confidence. Consistent with this repo's own Module 1 methodology (and with how the MinIO report in this same repo handled an analogous data gap), this report instead uses Damodaran's broader **"Software (System & Application)"** industry bucket from `03-corporate-finance/03-2-course-content/01-foundations-and-discount-rates/lesson-10/spreadsheet-totalbeta24.md` — the same January-2024-vintage dataset (n=351 firms) used in the MinIO report, since the repo's live `industry-betas.json` is still an empty stub.

| Segment | Industry | Avg Unlevered Beta | Correlation w/ Market | Weight |
|---------|----------|--------------------:|------------------------:|-------:|
| Unified observability / AI observability platform | Software (System & Application) | 1.2725 | 0.3374 | 100% |

### Estimated Unlevered Beta
**≈1.27.** This is notably higher than Dynatrace's own regression beta (≈0.72, Step 8) — the industry bucket includes a large tail of smaller, higher-beta, less-profitable software names, while Dynatrace itself is a large, profitable, low-volatility outlier within that bucket. Both numbers are carried forward below rather than collapsed into one, so the divergence stays visible.
---

## Step 11 — Levered Beta and Total Beta

### Inputs
- Unlevered beta: 1.2725 (Step 10)
- Market value of equity: **$17,285M** (289.0M shares × $59.81, Capital IQ 2026-10-07)
- Debt: **≈$1,194M** — the straight-debt component of the exchangeable notes (≈$1,034M, Step 12) plus operating lease liabilities ($159.3M)
- Debt/Equity: **≈6.9%** (prior version: 0.98%, leases only)
- Marginal tax rate: 25%
- Correlation with market: 0.3374 (industry average, Step 10)

### Levered Beta (Hamada)
β_levered = 1.2725 × [1 + (1 − 0.25) × 0.0691] = 1.2725 × 1.0518 ≈ **1.34** (prior version: 1.28).

Two alternative treatments give nearly the same answer: counting the notes at full face value ($1,437.5M) gives D/E 9.2% and a levered beta of 1.36; adding the conversion-option value to equity gives D/E 6.75% and 1.34. The convertible treatment is not what drives the answer.

### Total Beta
1.338 / 0.3374 ≈ **3.97**. Shown for completeness only.

### Interpretation
**Total beta is not the right lens for Dynatrace.** Step 4 established a 99.3% float held by diversified institutions. The number that matters is the levered market beta, and the two candidates still diverge sharply: **≈1.34 bottom-up vs. 0.77 regression**. Both are carried into the summary.
---

## Step 12 — Cost of Debt

### What Dynatrace Now Owes

| Instrument | Amount | Terms | Source |
|---|---:|---|---|
| 0.00% Exchangeable Senior Notes due 2031-09-01 (issuer Dynatrace LLC) | $1,437.5M face (includes the $187.5M option) | Priced 2026-08-18, closed 2026-08-20; exchange price ≈$64.27, a 35% premium to $47.61 | Company press releases / 8-K (web) |
| Note hedge and warrants | ≈$145.9M hedge cost; warrant strike ≈$107.12 | Lifts the effective dilution threshold from $64.27 to $107.12 | Same |
| Revolving credit facility | Undrawn | New credit agreement signed 2026-09-24; Capital IQ still shows the old facility maturing 2027-12-02 | Capital IQ capital-structure detail / Key Developments |
| Operating lease liabilities | $159.3M (current $23.1M + long-term $136.2M) | 4.0% weighted discount rate | Capital IQ balance sheet, 2026-06-30 |

At $59.81 the stock is 7% below the $64.27 exchange price, so the notes are close to the money.

### Bond Rating and Spread
**No rating found.** Capital IQ's S&P ratings page for Dynatrace is empty. The notes are unrated and pay no coupon, so there is no traded straight-debt spread to read.

### Synthetic Rating
The prior version called the coverage ratio "not economically meaningful" because there was no interest expense. There is still almost none in the accounts (Capital IQ LTM interest expense $0.8M, interest income $45.1M), because the coupon is zero. But a zero coupon is not a zero cost: Dynatrace paid for the borrowing with a conversion option. The honest test is what the interest bill would be if the same $1,437.5M were straight debt.

| Read | Interest used | Coverage | Rating (large-firm table) | Spread |
|---|---:|---:|---|---:|
| As reported | $0.8M | 341× | Aaa/AAA | 0.74% |
| **Imputed straight debt (used)** | **$106M** ($1,437.5M × 6.95% + $6.4M lease interest) | **2.6×** | **Baa2/BBB** | **1.89%** |
| Stress: same interest, EBIT 10% lower | $106M | 2.4× | Ba1/BB+ | 2.20% |

EBIT is Capital IQ's LTM $273.1M plus the $6.4M of lease interest. The BBB row is self-consistent: assume a 1.89% spread, compute the interest, and the coverage (2.6×) maps back to BBB. It sits near the bottom of the BBB band (2.5×–3.0×). The read is conservative in two ways. It uses GAAP EBIT, which is after $301M of stock-based compensation; and it ignores about $1.5B of pro forma cash. It will weaken in FY2027 as Arize dilutes margin and adds amortization.

**Pre-tax cost of debt: 5.06% + 1.89% = ≈6.95%** (prior version: 5.94% at the Aaa spread). The ratings table is the dated vintage checked into Lesson 12.

### Market Value of Debt
Following the course treatment of convertibles, the notes are split into straight debt and an equity option:

- Straight-debt component: $1,437.5M ÷ 1.0695^4.9 ≈ **$1,034M**
- Conversion option (equity): ≈ **$403M**
- Plus lease liabilities: $159.3M
- **Debt for the cost of capital ≈ $1,194M**, or 6.5% of capital

The market price of the notes was not found, so the option value is the residual at face, not a traded value.

### Pro Forma Cash (estimate)
$1,108.9M cash and short-term investments + $47.1M long-term securities + $1,437.5M note proceeds − $145.9M note hedge − $134.7M concurrent buyback − $815M Arize cash ≈ **$1.5B**. This ignores issuance fees, warrant proceeds, cash generated since June 30 and any further buybacks, so treat it as ±$150M. Against $1,596.8M of face debt plus leases, net debt is roughly zero.

### Lease Debt Capitalization
Under ASC 842 the balance sheet already carries the capitalized leases: $159.3M at 2026-06-30 ($164.3M at fiscal year-end), 8.0-year weighted remaining term, 4.0% discount rate.

### Marginal Tax Rate
**25%** (blended US federal and state statutory convention). The reported effective rate is unusable: Capital IQ shows **49.4% for the LTM and 45.7% for FY2026** ($147.8M of tax on $299.2M of pre-tax income), after a $260.3M tax *benefit* in FY2025 tied to the IP transfer to Switzerland. Because the notes pay no cash coupon, the tax shield in practice comes from the note hedge's tax treatment, not from interest; the 25% is a convention here, and at 6.5% debt it moves WACC by under 0.1 point.
---

## Summary — Cost of Capital Inputs

| Input | Value |
|-------|-------|
| Risk-free rate | **5.06%** (5.28% 10-yr Treasury on 2026-10-07 less 0.22% US default spread) |
| Mature market ERP | 4.23% (Damodaran, January 2026; October figure not found) |
| Weighted ERP (country-adjusted) | ≈4.79% (Capital IQ region weights; US at 4.46%; non-US regional premiums estimated) |
| Regression beta (5Y, S&P 500) | 0.77 (Capital IQ; R² not found) |
| Bottom-up unlevered beta (Software System & Application, Jan-2024 vintage) | 1.27 |
| Debt/Equity | ≈6.9% (notes' debt component + leases, over market cap) |
| Levered beta (Hamada) | ≈1.34 |
| Total beta (contrast only) | ≈3.97 |
| **Cost of equity — bottom-up (primary)** | **≈11.5%** (5.06% + 1.338 × 4.79%) |
| Cost of equity — regression (cross-check) | ≈8.75% (5.06% + 0.77 × 4.79%) |
| Pre-tax cost of debt (synthetic Baa2/BBB on imputed interest) | ≈6.95% |
| After-tax cost of debt (25%) | ≈5.21% |
| Debt/Capital | ≈6.5% |
| **WACC — bottom-up (primary)** | **≈11.1%** |
| WACC — regression (cross-check) | ≈8.5% |

### What changed from the 2026-09-28 version

| Input | 2026-09-28 | 2026-10-07 | Why |
|---|---:|---:|---|
| Share price / market cap | ≈$57.95 / ≈$16.8B | $59.81 / $17.3B | Capital IQ |
| Risk-free rate | 5.20% gross | 5.06% netted (5.28% gross) | Treasury up 8bp; US default spread netted out |
| Weighted ERP | ≈4.7% | ≈4.79% | US at 4.46%; Capital IQ splits US from rest of North America |
| Regression beta | ≈0.72 | 0.77 | Capital IQ |
| Funded debt | $0 | $1,437.5M face 0% exchangeable notes | Issued 2026-08-20; missed by the prior version |
| D/E | 0.98% | ≈6.9% | Notes |
| Levered beta | 1.28 | 1.34 | Notes |
| Synthetic rating / spread | Aaa-equivalent / 0.74% | Baa2/BBB / 1.89% | Coverage on imputed straight-debt interest |
| Pre-tax cost of debt | 5.94% | 6.95% | Rating |
| Cost of equity (bottom-up) | ≈11.1% | ≈11.5% | Leverage and ERP up, risk-free down |
| **WACC (bottom-up)** | **≈11.0%** | **≈11.1%** | Higher cost of equity offset by 6.5% debt at 5.2% after tax |
| WACC (regression) | ≈8.55% | ≈8.5% | — |
| Starboard stake | "significant" | 3.07% | Capital IQ |
| FY2026 revenue growth | +16% | +19% reported / +17% cc | Correction |

**The headline number barely moved; what sits underneath it did.** Use the bottom-up ≈11.1% as the hurdle rate, for the reasons Lessons 9–10 give: the regression beta is backward-looking, its R² is unknown, and its window is dominated by company-specific events. The two changes that matter for judgment are that Dynatrace is now a BBB-type borrower on an honest coverage test rather than a AAA-by-default one, and that its $1B net-cash cushion has been spent.

**Applied to Arize:** at an 11.1% cost of capital, $915M has to earn about **$100M a year of after-tax operating income with no growth, or about $65M growing at 4% forever**, to be worth what was paid. Arize is guided to add about $40M of ARR in FY2027 while costing 175 basis points of margin (about $40M on $2.3B of revenue). The purchase only clears the hurdle through cross-sell into Dynatrace's ~4,100 customers.
---

## Data Provenance — What's Sourced vs. Estimated vs. Not Found

**Capital IQ (classic platform, company ID 628406634, pulled 2026-10-07):**
- Tearsheet: price, shares, market cap, 5-year beta, float
- Income statement and cash flow (LTM to 2026-06-30 and FY2026): revenue, EBITDA, EBIT, net income, interest expense and income, tax, R&D, stock-based compensation, cash from operations, capex, buybacks
- Balance sheet and capitalization: cash, securities, lease liabilities, total debt
- Geographic segments (FY2026)
- Ownership summary and holder-type split; investor activism screen (Starboard, Pictet)
- Capital-structure detail (revolver status and maturity); S&P ratings page (empty)

**SEC filings, company releases and web search:**
- Exchangeable notes terms: size, pricing and closing dates, exchange price, hedge cost, warrant strike, concurrent repurchase
- Arize terms, guidance and 2026-10-01 close; new credit agreement dated 2026-09-24
- Board composition and Starboard settlement (DEF 14A, 8-K exhibits, press)
- ARR, net retention, customer count, constant-currency growth, Rule of 50 target (10-K, earnings materials)
- 10-year Treasury yield, 2026-10-07 (Treasury par yield; Trading Economics showed 5.32%)
- Damodaran implied ERP (January and March 2026), US default spread 0.22% and US country risk premium 0.23% (as used in this repo's SolarWinds work)
- Damodaran industry beta and ratings table (this repo's `spreadsheet-totalbeta24.md`, `spreadsheet-ratings.md`)

**Estimated or assumed:**
- Non-US regional ERPs in Step 7
- Marginal tax rate of 25%
- Synthetic rating: built on imputed straight-debt interest, not on reported interest
- Split of the notes into debt (≈$1,034M) and option (≈$403M) at face value
- Pro forma cash of ≈$1.5B (no fees, warrant proceeds, post-June cash flow or later buybacks)

**Not found:**
- October 2026 Damodaran implied ERP
- Regression R-squared
- A credit rating, or a market price for the notes
- Terms of the 2026-09-24 credit agreement (size, pricing, maturity)
- Full 10-person board roster (Capital IQ's board page did not load)
- Arize's standalone revenue, margin or retention

**Deliberately omitted:** Capital IQ consensus estimates (kept out of this public repo).
---

## Appendix — Reading This for a Job Candidate

### 1. How is Dynatrace doing right now?
Well, and the market agrees. FY2026 revenue grew 19% to $2.02B, ARR is $2.14B growing 17%, net retention is 110%, and free cash flow runs at about 27% of revenue. The stock has gone from a 52-week low of $31.64 to about $60; market cap is $17.3B. Three warts: GAAP operating margin is ~13% against ~29% non-GAAP because stock-based compensation is 14% of revenue; the GAAP tax rate is running near 49%; and the balance sheet that used to carry $1B of net cash is now roughly neutral. The category has consolidated (New Relic private in 2023, Splunk into Cisco in 2024). Dynatrace is the profitable compounder; Datadog is the fast grower. The companion [Datadog valuation](datadog-valuation.md) shows the two have nearly the same cost of capital (≈11%), so the gap in their revenue multiples is a growth gap, not a risk gap.

### 2. What does this suggest about the Arize acquisition's real purpose?
Read Steps 2, 3 and 12 together. Dynatrace settled with an activist that wanted more capital return and less strategic spending, added two Starboard-linked directors on 2026-07-01, signed a $915M margin-dilutive acquisition six weeks later, and five days after that sold $1.44B of zero-coupon exchangeable notes while buying back more stock. It did not choose between Starboard and Arize; it borrowed to do both. That is a board-approved bet that position in AI observability is worth giving up the net-cash balance sheet. **Success for leadership means:** hitting the disclosed +200bps ARR / −175bps margin numbers, showing a measurable attach rate into the ~4,100-customer base within 12–18 months, resuming margin expansion in FY2028, getting the stock above the $64.27 exchange price for the right reasons, and keeping Arize's standing with the open-source developer community.

### 3. What should a Senior AI Product Manager, Observability joining Arize/Dynatrace expect in year one?
- **The ARR-accretion commitment is the scoreboard.** About $40M of ARR in FY2027 was promised publicly. Expect cross-sell and attach rate into Dynatrace accounts to outweigh Arize-standalone new logos.
- **The hurdle is high and now explicit.** At an ≈11% cost of capital the purchase needs roughly $65–100M a year of after-tax operating income to pay for itself. Standalone Arize cannot do that; only attach into the base can. Roadmap proposals that shorten time-to-value for a Dynatrace enterprise customer are the ones that map to the number.
- **Margin discipline is real.** An activist-aligned board, a BBB-type balance sheet rather than a cash pile, and a promise of margin recovery by FY2028 mean a provable-payback bar on new investment.
- **Geography matters to the roadmap.** 54% of revenue is outside the US and 32% is in EMEA. Data residency, sovereign deployment and EU AI Act evidence are revenue-protection features for this base, not nice-to-haves.
- **Developer credibility is a tracked asset.** Phoenix and OpenInference adoption are part of what was bought.
- **Integration is the first job.** The deal closed 2026-10-01. Year one starts with packaging Arize into Dynatrace's subscription model and clearing enterprise procurement and security bars.
- **Watch the Investor Day.** The Rule of 50 path for FY2029 will state what Arize is expected to contribute. That is the number to design toward.
