---
title: "Datadog, Inc. — Module 1 Valuation: Cost of Capital Analysis"
status: active
owner: weprintmoney
created: 2026-10-07
last_updated: 2026-10-07
---

# Company Valuation: Datadog, Inc.
*Applied Corporate Finance — Module 1 Analysis*

**A note on data.** Market, financial, ownership and capital-structure inputs are S&P Capital IQ pulls dated 2026-10-07 (classic platform, company ID 134521275). Governance facts come from web search of the 2026 proxy statement and are marked where they rest on secondary sources. Damodaran inputs (industry beta, ratings table) come from the spreadsheets checked into this repo's Lesson 10 and 12 folders, because `industry-betas.json` and `country-risk.json` are empty stubs. Capital IQ consensus estimates are deliberately not reproduced in this public repo. This report uses the same method and the same market inputs as the companion [Dynatrace valuation](dynatrace-valuation.md) refreshed the same day, so the two can be compared line by line; a comparison table follows the Summary.

---

## Step 1 — Company Selected

**Datadog, Inc.** (NasdaqGS: DDOG) — a cloud monitoring, observability and security platform sold as usage-based software-as-a-service. Founded in 2010 by Olivier Pomel and Alexis Lê-Quôc, headquartered in New York, IPO'd on Nasdaq in September 2019. Fiscal year ends December 31.

| Snapshot (Capital IQ, 2026-10-07) | Value |
|---|---:|
| Share price | $271.34 |
| 52-week range | $98.01 – $292.72 |
| Shares outstanding | 359.1M |
| Market capitalization | $97,431M |
| LTM revenue (to 2026-06-30) | $3,966.7M (+31.5%) |
| LTM EBITDA / EBIT | $82.9M / $19.2M |
| LTM net income | $177.6M |
| LTM cash from operations / capex | $1,229.0M / $46.9M |
| LTM R&D | $1,733.2M (43.7% of revenue) |
| LTM stock-based compensation | $823.0M (20.7% of revenue) |
| Cash and short-term investments | $4,985.4M |
| Total debt | $1,277.8M |
| Float | 92.7% |

From the Q2 2026 earnings call (paraphrased): quarterly revenue of about $1.12B, up 36%; about 33,400 customers; about 4,720 customers above $100K of ARR, who make up roughly 91% of ARR; net retention in the low 120s; about 750 AI-native customers, 31 above $1M and 8 above $10M; and a nine-figure renewal with an AI lab that came with a usage reduction.

Datadog is the fast grower in a category where Dynatrace is the profitable compounder. It is also the competitor most likely to set the price and the pace in AI observability, which is why it is valued here.

---

## Step 2 — Corporate Governance

### Board of Directors
Classified (staggered) board. The 2026 Class I directors — **Olivier Pomel, Dev Ittycheria, Shardul Shah and Titi Cole Vora** — hold terms to 2029. Three directors are not independent: **Pomel** (CEO and co-founder), **Lê-Quôc** (CTO and co-founder) and **Amit Agarwal**. Secondary sources put the board at about 11 directors and report that shareholders approved a reincorporation from Delaware to Nevada in 2026; both points should be verified against the proxy before being relied on.

### Governance Assessment
Datadog has every entrenching feature in the Lesson 2/3 taxonomy at once: **dual-class stock with 10 votes per Class B share, a classified board, and founders who are also the CEO and CTO.** A Nevada reincorporation, if confirmed, adds weaker fiduciary-duty exposure for directors and officers. There is no activist: Capital IQ's activism screen shows no meaningful campaign, and with the vote counts in Step 4 a campaign could not win.

### Power Structure
Power sits with the two founders. Officers and directors together hold about 35.5% of the voting power on roughly 5.4% of the shares. The contrast with Dynatrace is direct: there, a 3.07% holder won two board seats in nine weeks; here, the institutions that own most of the equity cannot change the board without the founders.

---

## Step 3 — Stated Objectives

### Stated Goals
Management frames the objective as long-term growth through platform expansion: more products per customer, new categories (security, AI observability, an AI site-reliability agent), and reinvestment ahead of revenue. Datadog pays no dividend and Capital IQ shows **no share repurchases**. Cash is retained: $5.0B of cash and short-term investments against $1.3B of debt.

### Inferred Focus (Tension With Stated Goals)
The accounts match the words. R&D is 43.7% of revenue, GAAP operating margin is 0.5%, and free cash flow of about $1.18B (29.8% of revenue) is accumulated rather than returned. The tension is not between stated and actual goals; it is between who bears the cost and who decides. Stock-based compensation of $823M a year is paid by Class A holders through dilution, while Class B holders decide how much to issue. The usual check — an activist asking for buybacks and margin, as at Dynatrace — is structurally unavailable. That is a governance cost in principle. In practice the stock has nearly tripled from its 52-week low, so holders have no present reason to object.

---

## Step 4 — Share Classes and Marginal Investor

### Share Structure
**Dual class.** At the 2026-04-22 record date: **330,775,832 Class A shares (1 vote each) and 25,166,391 Class B shares (10 votes each).** Class B is 7.1% of the shares and **43.2% of the votes** (251.7M of 582.4M votes; computed here). Per the 2026 proxy as reported by secondary sources, Pomel holds about 17.3% and Lê-Quôc about 15.5% of total voting power.

### Largest Shareholders (Capital IQ ownership summary, 2026-10-07)

| Holder | % of shares |
|---|---:|
| BlackRock | 9.90% |
| Vanguard Capital Management | 6.55% |
| FMR (Fidelity) | 5.17% |
| Vanguard Portfolio Management | 4.89% |
| State Street | 4.10% |
| Insiders (all) | 5.44% |

### Marginal Investor
The investor setting the price is a large, diversified institution trading Class A shares. The investors controlling the company are two founders holding Class B. They are different people.

### Likely Diversification of Marginal Investor
Highly diversified, so **market (levered) beta** is the right risk measure for pricing the stock. The founders are the opposite: most of their wealth is in one company, and total beta (Step 11) describes the risk they personally carry. That gap is a reason to expect founder-controlled firms to be more cautious with debt than a diversified shareholder would want, which fits Datadog's $3.7B net-cash position.

---

## Step 5 — Currency and Risk-Free Rate

### Reporting Currency
**USD.** US SEC filer, US GAAP.

### Revenue Currencies
Predominantly USD. Datadog bills largely in dollars; 71% of 2025 revenue came from North America (Step 7).

### Analysis Currency and Rationale
USD.

### Risk-Free Rate
**5.06%** — the US 10-year Treasury par yield of 5.28% on 2026-10-07, less Damodaran's 0.22% US default spread. The netting follows this repo's SolarWinds work of 2026-10-06: the 4.46% US equity risk premium already includes a 0.23% US country risk premium, so using the gross Treasury would count US default risk twice. Same rate as the Dynatrace refresh.

---

## Step 6 — Equity Risk Premium (Mature Market)

### Current Mature Market ERP
**4.23%** — Damodaran's implied ERP at the start of 2026.

### Method and Source
Implied ERP from the S&P 500 level and expected cash flows. Later readings found: 4.37% at the start of March 2026 and 4.51% in mid-March. **The October 2026 figure was not found**, so January's is used and the sensitivity shown: each 0.25 point of ERP moves Datadog's bottom-up cost of equity by about 0.32 points.

---

## Step 7 — Country Risk and Weighted ERP

### Best Measure of Country Exposure
Revenue by customer geography.

### Geographic Breakdown
Capital IQ geographic segments, calendar 2025:

| Region | Revenue ($M) | % of Revenue | ERP used |
|---|---:|---:|---|
| United States | 2,320.3 | 67.7% | 4.46% (4.23% + 0.23% US country risk premium) |
| North America ex-US | 112.8 | 3.3% | 4.23% — estimated |
| International | 994.1 | 29.0% | ≈5.0% — estimated |

Datadog discloses only one "International" line, so the 5.0% is an estimate for a mix of Western Europe and Asia Pacific with some emerging-market exposure.

### Weighted Average ERP
0.677×4.46% + 0.033×4.23% + 0.290×5.0% = 3.02% + 0.14% + 1.45% = **≈4.61%**.

That is 0.18 points below Dynatrace's 4.79%. Dynatrace sells 54% of its revenue outside the US, including 7.9% in Latin America; Datadog sells 29% abroad.

### Why This ERP Might Change
International is the under-penetrated side of Datadog's business, and sovereign-cloud and data-residency demand is pulling vendors toward local regions. If the international share rises toward Dynatrace's, the weighted ERP rises by 0.1–0.2 points.

---

## Step 8 — Regression Beta

### Regression Beta
**1.51** — Capital IQ 5-year beta, 2026-10-07.

### Index, Time Period, R-squared
5 years against the S&P 500. **R-squared not found** (not shown on the tearsheet; Chart Builder is broken in this account).

### Reliability Assessment
1.51 is almost exactly twice Dynatrace's 0.77, for two firms selling overlapping products to overlapping buyers. Part of that is real (Step 9: usage-based revenue and thin GAAP margins). Part is the window: Datadog fell about 70% in the 2021–2022 growth-stock drawdown and has risen from $98 to $271 in the last year, both moves amplified versions of the market's. Coincidentally, 1.51 equals Damodaran's unlevered beta for the "Software (Internet)" bucket. As with Dynatrace, treat the regression as one soft reading and carry it alongside the bottom-up number.

---

## Step 9 — Beta Fundamentals

### Product/Service Beta Expectation
Observability is close to non-discretionary once embedded, which argues for a moderate beta. But **Datadog bills on usage**, so customers can cut spend within a quarter by sending less data, as they did during the 2022–2023 cloud-optimization cycle. Revenue is also increasingly tied to AI-native customers (about 750, 8 of them above $10M), whose own spending follows the AI investment cycle; the Q2 2026 nine-figure renewal with a usage reduction shows how concentrated and how elastic that revenue can be. Expect a business beta **above** Dynatrace's and at or above the software average.

### Operating Leverage Effect
Very high. R&D is 43.7% of revenue and GAAP EBIT is $19.2M on $3,967M of revenue (0.5%). A one-point change in revenue growth moves GAAP operating income by a multiple of itself. Much of the "fixed cost" is stock-based compensation ($823M) and growth R&D that an accountant expenses and Damodaran would capitalize, so GAAP overstates the fragility; cash from operations is $1.2B. The direction still holds: more operating leverage than Dynatrace, hence a higher beta.

### Financial Leverage Effect
Negligible. Debt is about 1% of capital and the company holds $3.7B of net cash. Financial leverage is not what makes Datadog's regression beta high.

---

## Step 10 — Bottom-Up Unlevered Beta

### Business Segments
One reportable segment.

### Comparable Firms / Industry Group
Same treatment as the Dynatrace report: the pure-play observability set is too thin to average (New Relic is private, Splunk is inside Cisco), so the Damodaran **"Software (System & Application)"** bucket is used (n=351, January 2024 vintage, `lesson-10/spreadsheet-totalbeta24.md`).

| Segment | Industry | Avg Unlevered Beta | Correlation w/ Market | Weight |
|---|---|---:|---:|---:|
| Cloud observability and security platform | Software (System & Application) | 1.2725 | 0.3374 | 100% |

### Estimated Unlevered Beta
**≈1.27.** The alternative bucket, "Software (Internet)" (n=35), has an unlevered beta of 1.51. A case can be made for it given usage-based billing, and it would add about 1.1 points to the cost of equity. The broader bucket is kept so that Datadog and Dynatrace share one business-risk input and every difference between their costs of capital is traceable to leverage, geography or the regression.

---

## Step 11 — Levered Beta and Total Beta

### Inputs
- Unlevered beta: 1.2725
- Market value of equity: **$97,431M**
- Debt: **≈$1,046M** — straight-debt component of the convertible notes (≈$753M, Step 12) plus lease liabilities ($292.3M)
- Debt/Equity: **≈1.07%**
- Marginal tax rate: 25%
- Correlation with market: 0.3374

### Levered Beta (Hamada)
1.2725 × [1 + 0.75 × 0.0107] ≈ **1.28**.

### Total Beta
1.283 / 0.3374 ≈ **3.80**.

### Interpretation
For pricing the stock, use the levered market beta: **1.28 bottom-up vs. 1.51 regression**. Note the direction: Datadog's regression beta is *above* its bottom-up beta, Dynatrace's is far *below*. The bottom-up method pulls both toward the same ≈1.3. Total beta is not the pricing input, but it is a fair description of the founders' own exposure (Step 4).

---

## Step 12 — Cost of Debt

### What Datadog Owes

| Instrument | Amount | Terms | Source |
|---|---:|---|---|
| 0.00% Convertible Senior Notes due 2029-12-01 | $985.5M carrying value; face assumed ≈$1,000M | Zero coupon; conversion price not retrieved, but the stock has roughly tripled off its low, so the notes are almost certainly deep in the money | Capital IQ capital-structure detail |
| Operating lease liabilities | $292.3M (current $44.2M + long-term $248.0M) | 6.69% weighted discount rate | Capital IQ |
| **Total debt** | **$1,277.8M** | | Capital IQ |

### Bond Rating and Spread
**No rating found.** Capital IQ's ratings pages for Datadog return no data.

### Synthetic Rating
The mechanical answer is poor and should not be believed.

| Read | EBIT | Interest | Coverage | Rating (large-firm table) | Spread |
|---|---:|---:|---:|---|---:|
| **As reported (used)** | $19.2M | $11.4M | **1.7×** | **B2/B** | **4.35%** |
| Imputed straight-debt interest | $38.8M (incl. lease interest) | ≈$114M | 0.3× | C2/C | 14.0% |
| Common sense | — | — | — | Investment grade | ≈1–2% |

GAAP EBIT is $19.2M because Datadog expenses $1,733M of R&D and $823M of stock-based compensation. The same company produces $1.2B of operating cash flow, earns $192.7M of interest income on its cash (17 times its interest expense), and could repay all of its debt four times over from cash on hand. The coverage table was built for firms whose operating income is the source of debt service; it mis-rates a firm that under-earns by choice and holds cash well above its debt. This is the Lesson 12 limit of synthetic ratings, shown on a live case.

**Pre-tax cost of debt used: 5.06% + 4.35% = ≈9.41%**, the mechanical figure, kept for method consistency. With debt at 1.1% of capital, replacing it with a 2% investment-grade spread changes WACC by less than 0.03 points. The rating does not matter to the answer; it matters as an illustration.

### Market Value of Debt
- Straight-debt component of the notes: $1,000M ÷ 1.0941^3.15 ≈ **$753M**
- Conversion option (equity): ≈$247M at face; worth much more in the market with the stock at $271
- Lease liabilities: $292.3M
- **Debt for the cost of capital ≈ $1,046M (1.1% of capital)**

### Lease Debt Capitalization
Already on the balance sheet under ASC 842: $292.3M at a 6.69% discount rate.

### Marginal Tax Rate
**25%** by convention. The effective rate is 11.1% for the LTM and 15.2% for 2025 ($22.2M of tax on $199.8M of pre-tax income), held down by stock-compensation deductions and accumulated losses.

---

## Summary — Cost of Capital Inputs

| Input | Value |
|---|---|
| Risk-free rate | 5.06% (5.28% 10-yr Treasury on 2026-10-07 less 0.22% US default spread) |
| Mature market ERP | 4.23% (Damodaran, January 2026; October figure not found) |
| Weighted ERP | ≈4.61% (Capital IQ region weights; International premium estimated) |
| Regression beta (5Y, S&P 500) | 1.51 (Capital IQ; R² not found) |
| Bottom-up unlevered beta | 1.27 |
| Debt/Equity | ≈1.07% |
| Levered beta (Hamada) | ≈1.28 |
| Total beta (founders' lens only) | ≈3.80 |
| **Cost of equity — bottom-up (primary)** | **≈11.0%** (5.06% + 1.283 × 4.61%) |
| Cost of equity — regression (cross-check) | ≈12.0% (5.06% + 1.51 × 4.61%) |
| Pre-tax cost of debt (mechanical B2/B; see Step 12) | ≈9.41% |
| After-tax cost of debt (25%) | ≈7.06% |
| Debt/Capital | ≈1.1% |
| **WACC — bottom-up (primary)** | **≈10.9%** |
| WACC — regression (cross-check) | ≈12.0% |

### Datadog vs. Dynatrace (both as of 2026-10-07)

| | Datadog | Dynatrace |
|---|---:|---:|
| Market cap | $97.4B | $17.3B |
| LTM revenue | $3,967M | $2,096M |
| LTM revenue growth | +31.5% | ≈+19% (FY2026) |
| GAAP EBIT margin (LTM) | 0.5% | 13.0% |
| Free cash flow margin (LTM) | 29.8% | 27.2% |
| R&D / revenue | 43.7% | 24.3% |
| Stock-based compensation / revenue | 20.7% | 14.4% |
| Buybacks (LTM) | none | $728M |
| Cash less debt | +$3.7B | ≈0 pro forma (was +$1.0B in June) |
| Enterprise value / LTM revenue | ≈23.6× | ≈8.3× |
| Revenue outside the US | 32% | 54% |
| Control | Founders, 10-vote Class B | None; 99.3% float; activist with board seats |
| Regression beta | 1.51 | 0.77 |
| Bottom-up levered beta | 1.28 | 1.34 |
| Weighted ERP | 4.61% | 4.79% |
| **WACC, bottom-up** | **≈10.9%** | **≈11.1%** |
| WACC, regression | ≈12.0% | ≈8.5% |

**What the comparison says.** On a consistent bottom-up basis the two companies have the same cost of capital, about 11%. The market pays nearly three times as much per dollar of Datadog revenue. Since the discount rates match and the cash margins match, the entire gap is expected growth and its duration. The regression betas tell the opposite story about risk (Datadog twice as risky), which is a statement about how the two stocks have traded, not about how different the two businesses are.

The two firms have also made opposite capital-allocation choices from similar cash margins. Datadog reinvests 44% of revenue in R&D, returns nothing and sits on $3.7B of net cash, and no shareholder can make it do otherwise. Dynatrace spends 24% on R&D, returned more than its free cash flow in buybacks under activist pressure, and borrowed $1.44B to buy the AI capability Datadog is building in-house.

---

## Data Provenance — What's Sourced vs. Estimated vs. Not Found

**Capital IQ (classic platform, company ID 134521275, pulled 2026-10-07):** tearsheet (price, range, shares, market cap, beta, float); income statement and cash flow (LTM to 2026-06-30 and 2025); balance sheet and capitalization; capital-structure detail (convertible notes, lease rate); geographic segments (2025); ownership summary; activism screen; ratings pages (no data).

**Web search / company materials:** share counts by class at the 2026-04-22 record date; founders' voting power; classified board and Class I directors; non-independent directors; Q2 2026 call metrics (paraphrased); 10-year Treasury yield; Damodaran ERP readings, US default spread and US country risk premium; Damodaran industry beta and ratings table (this repo's Lesson 10 and 12 spreadsheets).

**Computed here:** Class B share of votes (43.2%); weighted ERP; convertible split; all betas and costs of capital; the comparison table ratios.

**Estimated or assumed:** North America ex-US and International ERPs; 25% marginal tax rate; ≈$1,000M face value of the 2029 notes (inferred from the $985.5M carrying value); use of the mechanical B2/B rating.

**Not found / to verify:** October 2026 Damodaran ERP; regression R-squared; conversion price and market price of the 2029 notes; any credit rating; exact board size and the Nevada reincorporation (secondary sources only); the full director list.

**Deliberately omitted:** Capital IQ consensus estimates.
