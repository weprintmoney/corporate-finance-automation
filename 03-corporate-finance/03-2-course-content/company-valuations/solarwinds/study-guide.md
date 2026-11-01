---
title: "SolarWinds (SWI) — Study Guide by Lesson"
status: active
owner: weprintmoney
created: 2026-11-01
last_updated: 2026-11-01
---

# SolarWinds (SWI) — Study Guide by Lesson

One document for the whole course, lesson by lesson, applied to the final project: a valuation of SolarWinds on **2025-02-05**, the last trading day before the $18.50-a-share buyout by Turn/River Capital was announced. Each lesson has four parts:

1. **Key terms.** Plain-language definitions, copied from [key-terms.md](../../key-terms.md).
   - **Key documents.** The filings and data sources that lesson's work drew on: what each is, when it's used and where to find it.
2. **What the project asked.** The assignment questions for that lesson. Lessons 13–36 quote the "Project Questions" in each `lesson-overview.md` word for word. Lessons 1–12 have no project questions in the course material, so they use the twelve Module 1 cost-of-capital steps the `/value-company` skill defines (`.claude/skills/value-company/seeds/module-1-steps.yaml`).
3. **Information required and where we got it.** Each input, its SolarWinds value, and the original document. Source files are in [sources/](sources/), and every number is in the ledger, [inputs.yaml](inputs.yaml).
4. **Steps to complete the assignment.** The sequence, worked through with SolarWinds' numbers.

This guide restates work done elsewhere in this folder. If a number here ever disagrees with [model-output.md](model-output.md) or a `lesson-NN.md` file, those files are right. The full answers are in each lesson's `lesson-NN.md`, and the plain-language reasoning is in [walkthrough.md](walkthrough.md).

**Headline results** (model-output.md): cost of capital 10.23%; DCF value $13.00 a share, against the $15.18 unaffected price and the $18.50 deal price; optimal debt ratio 21%, against the actual 33%.

---

# Module 1 — Foundations & Discount Rates (lessons 1–12)

## Lesson 01 — Valuation: The Big Picture / What is Corporate Finance?

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Corporate finance** | Any decision that affects a business's finances. Damodaran defines it broadly: everything a business does falls under it. |
| **First principles** | The few basic rules that govern all corporate finance (the investment, financing and dividend principles). He calls them common sense, says they apply to every business, and says breaking them eventually causes a disaster. |
| **Investment principle** | Invest in assets that earn a return greater than the minimum acceptable hurdle rate. Example from the slides: taking investments that make 9% with money that costs 10% is obviously a bad idea. |
| **Hurdle rate** | The minimum return an investment must earn to be acceptable. It depends on the risk of the investment and on the mix of debt and equity used to fund it (Lessons 4-13 build it up). |
| **Financing principle** | Find the right kind of debt for your firm and the right mix of debt and equity to fund operations. A mix that costs 10% beats one that costs 11%. |
| **Dividend principle** | If you cannot find investments that earn your minimum acceptable rate, return the cash to the owners. |
| **Maximizing the value of the business** | The single objective that gives corporate finance its focus. Damodaran's warning: if you accept this objective everything in corporate finance makes sense, and if you do not, nothing will. |
| **Balance sheet** | The accounting snapshot of what a firm owns (assets: fixed, current, financial investments, intangibles) against how it is funded (liabilities, debt and equity). The course re-cuts it into a "financial view" built around the three principles. |
| **Intangible assets** | Assets that are not physical, such as patents and trademarks. |
| **Life cycle** | The idea (Theme 3) that a firm's financial focus changes as it ages, as the business moves through stages of its life. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |

### What the project asked

Module 1 step 1: **Pick a company**

1. Which company, and why is it a good subject (data available, decisions to judge)?
2. Where does it sit on the corporate life cycle, judged by growth, margins, reinvestment and cash use?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Company, type, base year, valuation date | SolarWinds Corporation (NYSE: SWI), delisted, FY2024 base year, valued 2025-02-05 | Ledger `meta` (`inputs.yaml`); source list in `sources/README.md` |
| Revenue, 2024 and 2023 | $796.9M and $758.7M | FY2024 10-K (annual report filed with the SEC) income statement (`sources/filings/swi-10k-fy2024.md`); ledger `company.revenue`, `company.history` |
| GAAP operating income (EBIT, profit before interest and tax) | $208.4M | FY2024 10-K income statement; ledger `company.ebit` |
| Revenue by contract type | Maintenance $440.6M, license $51.8M, subscription $304.5M (up from $234.2M) | FY2024 10-K, Note 16 (`sources/filings/swi-10k-fy2024.md`); ledger `facts.maintenance-revenue`, `facts.license-revenue`, `facts.subscription-revenue` |
| R&D, capital spending, acquisitions, D&A (depreciation and amortization) in 2024 | $108.6M; $20.5M; $0; $74.4M | FY2024 10-K income and cash flow statements; ledger `company.rd_expense`, `company.capex`, `facts.acquisitions-cash-2024`, `company.da` |
| Special dividends | $168.2M ($1.00 a share, 2024); $237.2M ($1.50 a share, 2021) | FY2024 10-K and FY2023 10-K (`sources/filings/swi-10k-fy2023.md`); ledger `company.history`, `facts.special-dividend-2021` |
| Free cash flow to equity (FCFE) vs cash returned, 2024 | $127.0M vs $194.7M | Computed in model-output.md section 5 |
| 2023 sale process | 13 buyers approached, 3 indications, all withdrew by 2023-11-23 | Merger information statement (DEFM14C), Background of the Merger (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `facts.market-check-2023` |
| Management's forecast growth, 2025-2030 | 8.12% a year | DEFM14C management forecasts; ledger `forecast.management_growth` |
| Stated strategy | "subscription-first approach" | FY2024 10-K Item 1; ledger `governance.objectives` |
| Unaffected price and deal price | $15.18 and $18.50 | DEFM14C (Goldman Sachs opinion; Per Share Merger Consideration); ledger `company.share_price`, `company.deal_price` |
| Debt in capital | 33.03% | Computed in model-output.md section 1 |

### Steps to complete the assignment

1. Pick a company with data and decisions to judge. SolarWinds has four annual reports, a 2024 proxy and a 2025 merger information statement with a forecast, two fairness opinions and the full sale history. Decisions to judge: two special dividends, 33.03% debt in its capital, a two-firm control group and a sale at $18.50. Limit: no price history survives, so no regression beta.
2. Split the balance sheet into assets in place and growth assets. No filing does this (one reporting segment), so use revenue type as a proxy. Assets in place are the perpetual-license base: maintenance $440.6M plus license $51.8M = $492.4M, 61.8% of $796.9M. Growth assets are subscriptions: $304.5M, 38.2%, up from $234.2M. This is a judgment, and much of the subscription growth is existing customers converting.
3. Compare where the 2024 cash went. R&D $108.6M (13.6% of revenue) plus capital spending $20.5M (2.6%) is $129.1M, and acquisitions were $0. The special dividend was $168.2M, 1.30 times that. Capital spending ran $53.9M below D&A of $74.4M.
4. Check the story management tells. It says it will extend leadership in observability through a subscription-first approach, but that push is funded from R&D and the existing sales team, with no acquisitions. The biggest discretionary use of cash was the payout.
5. Measure the life-cycle indicators. Growth: revenue rose 5.0% in 2024 ($758.7M to $796.9M) and 5.5% in 2023 ($719.4M to $758.7M). Margin: $208.4M ÷ $796.9M = 26.2%. Reinvestment: capital spending below depreciation in all three years. Payout: FCFE of $127.0M against $194.7M returned.
6. Test behavior against the placement. In 2023 the board and its banks approached 13 buyers; three gave indications and all three withdrew by 2023-11-23, citing the early stage of the subscription transition. Turn/River then offered $18.50, a 21.9% premium to $15.18.
7. Note the one mismatch. Management's plan grows revenue 8.12% a year against the 5.0% just reported. Later lessons (DCF, lesson 32) test that.
8. Answer. SolarWinds is the chosen company, and it sits in the mature stage of the life cycle: 5.0% growth, 26.2% GAAP operating margin, capital spending below depreciation, cash paid out, and a failed 2023 sale process followed by a 2025 sale.

**Result for SolarWinds:** Mature company (5.0% growth, 26.2% operating margin, $194.7M returned against $127.0M of FCFE) whose plan assumes 8.12% growth. No filing separates legacy from growth, so the 61.8% / 38.2% split is a proxy.
Full answers: [lesson-01.md](lesson-01.md) · Walkthrough: [Step 1](walkthrough.md#step-1-what-kind-of-company-is-solarwinds-and-how-old-is-it-in-business-terms)

## Lesson 02 — The Objective: Utopia and Let Down

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Maximize the value of the firm** | The objective in traditional corporate finance for decision making. |
| **Maximize stockholder wealth** | The narrower objective: do what makes owners richest. When the stock is traded and markets are efficient (prices reflect true value), this becomes maximizing the stock price. |
| **The classical objective** | Maximizing stock price, which works only if managers act for stockholders, lenders are protected, markets are efficient and society bears no hidden costs. The lesson walks through what happens when each assumption fails ("What can go wrong?"). |
| **Greenmail** | When a hostile bidder buys a stake, the target's managers buy it back at a price well above what the bidder paid, in return for a promise (a "standstill agreement") not to pursue the takeover. It protects managers, not stockholders. |
| **Golden Parachutes** | Employment-contract clauses paying managers a lump sum or stream of cash if they lose their jobs in a takeover. |
| **Poison Pills** | Securities whose rights or cash flows are triggered by an outside event, usually a hostile takeover, making the target too costly to buy. |
| **Shark Repellents** | Anti-takeover charter amendments. Unlike poison pills, they require stockholder approval to be put in place. |
| **Overpaying on takeovers** | Managers' acquisitions are often driven by management interests (size, power) rather than stockholder interests, so they pay too much. |
| **Splintering of stockholders** | Ownership so spread among many small holders that none can pressure managers (the Disney 2003 case). Managers then stop fearing stockholders and pursue their own interests. |
| **Voting versus non-voting shares & Golden shares** | Share classes where some holders get control without owning most of the economics (Vale: a holding company nominated ten of eleven directors). Golden shares give special veto rights, often to governments. |
| **Cross and pyramid holdings** | Companies owning stakes in each other, or in layers, so a controlling group runs many firms with little of its own money (the Tata case). It makes control and true ownership hard to see. |
| **Variable Interest Entity (VIE)** | A shell company structure used to get around limits on foreign ownership of Chinese firms (the Baidu case). It is unclear how much legal power shell-company shareholders have over the operating business. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **Credit agreement** | The contract between the company and its lenders: how much it borrowed, the interest rate, when it must repay and the conditions (covenants) it must meet. | Measuring debt and its cost, and judging how much room the company has before lenders can step in. | Filed as an exhibit to a 10-K, 10-Q or 8-K on SEC EDGAR; key terms are summarized in the 10-K debt note. |

### What the project asked

Module 1 step 2: **Corporate governance**

1. Who sits on the board of directors?
2. Whose interests are they most likely to serve?
3. Where does power lie (shareholders, managers, inside shareholders, another party), and what measure of governance strength supports that?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Board of directors | 9 directors: Ramakrishna (President and CEO), Bock (Chairman), Hao, Smith, Widmann (Silver Lake designees), Benko, Howard, Kinney, Sundaram; 8 of 9 independent under NYSE rules | 2024 proxy statement (`sources/filings/swi-def14a-2024.md`); ledger `governance.board` |
| Silver Lake ownership | 61,473,871 shares, 36.56% | 2024 proxy, beneficial ownership table; ledger `governance.controlling_holders` |
| Thoma Bravo ownership | 50,090,648 shares, 29.79% | 2024 proxy, beneficial ownership table; ledger `governance.controlling_holders` |
| Two sponsors combined | 66.35% of shares at the proxy date; about 65% of votes (111,564,519 shares) at the 2025-02-07 written consent | Sum of the two holdings (`facts.sponsors-pct-2024-proxy`); DEFM14C Written Consent section (`sources/deal-docs/swi-defm14c-2025-merger.md`; `facts.sponsor-voting-power-2025-02`) |
| All officers and directors | 1.95% | 2024 proxy; ledger `facts.officers-directors-pct` |
| Sponsor consent rights | Veto over change of control, new debt above $300.0M, asset deals above $300.0M, choice of CEO | 2024 proxy, Stockholders' Agreement; ledger `facts.sponsor-consent-rights` |
| Share classes | One class of common stock, one vote a share; 50 million preferred authorized, none issued | FY2024 10-K note 10 (`sources/filings/swi-10k-fy2024.md`); ledger `governance.share_classes` |
| Lender protection | Term loan face value $1,235.7M; change of control is an event of default; one financial test if revolver over 35% drawn, first-lien net leverage 7.40 to 1 | FY2024 10-K note 9 and Item 1A; ledger `company.debt_face`, `debt.covenants` |
| Golden parachutes | $38.96M total (Ramakrishna $22.99M, Black $8.54M, Bliss $7.43M); cash severance $3.2M; transaction bonuses $1.2M | DEFM14C Golden Parachute Compensation; ledger `governance.change_of_control_payouts` |
| Merger process | Transaction Committee of Bock, Sundaram, Widmann; Goldman Sachs and Jefferies fairness opinions; appraisal rights | DEFM14C Background of the Merger; ledger `facts.transaction-committee` |
| Float | Non-affiliate stock worth $661.3M on 2024-06-28 vs equity value $2,604.9M | FY2024 10-K cover page; ledger `facts.float-nonaffiliate-value`, `company.equity_value` |

### Steps to complete the assignment

1. List the board and classify each seat. Nine directors; eight are independent under NYSE (New York Stock Exchange) rules, but three of the eight (Hao, Smith, Widmann) are Silver Lake designees. Only the CEO is not independent.
2. Read the ownership table. Silver Lake 36.56% + Thoma Bravo 29.79% = 66.35%. Officers and directors hold 1.95%. No other 5% holder is listed.
3. Read the contract that gives them power. Each sponsor needs to consent in writing to a change of control, new debt above $300.0M, asset deals above $300.0M and the CEO choice. Each nominates three directors while holding 20% or more.
4. Check how the sale was approved. The sponsors signed a written consent on 2025-02-07 (111,564,519 shares, about 65% of votes), so no stockholder vote was held and there was no majority-of-minority condition. A three-person Transaction Committee ran the process; Widmann is a Silver Lake managing director. The minority got two fairness opinions and appraisal rights.
5. Test the four linkages of the course's "utopia" (managers, stockholders, lenders, markets, society) for the weakest. Managers-to-minority is weakest because the sponsors decide. Lenders are best protected: the credit agreement restricts debt, liens, mergers and dividends, and at closing on 2025-04-16 the old loan was paid off. The market link is thin ($661.3M float vs $2,604.9M equity).
6. Test what pay rewards. Parachutes total $38.96M, of which about $34.4M is equity valued at $18.50 (moves with price) and $1.2M is a closing bonus paid at any price. That is 1.2% of the roughly $3,206M paid to stockholders. Day-to-day pay tracks revenue and adjusted EBITDA (bonus, 50% each) and Subscription ARR and revenue (stock units, 70% and 30%). Defenses: classified board, no poison pill mentioned.
7. Answer. Power lies with the two sponsors (66.35% of shares, about 65% of votes, consent vetoes), not with managers (1.95%). The board will most likely serve the sponsors' interests. The proxy gives no governance score, so the ownership and consent evidence is the measure.

**Result for SolarWinds:** Controlled company: Silver Lake (36.56%) and Thoma Bravo (29.79%) hold 66.35% and approved the sale by written consent; managers hold 1.95%. Filings do not say whether institutions fought or sold.
Full answers: [lesson-02.md](lesson-02.md) · Walkthrough: [Step 2](walkthrough.md#step-2-who-really-controls-solarwinds)

## Lesson 03 — The Objective: Reality and Reaction

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Alternative corporate governance system** | Giving the job of monitoring managers to someone other than stockholders. Germany relies on banks at the core of cross holdings, Japan on keiretsus (groups of firms holding each other's shares), other Asian countries on family groups. |
| **Cross holdings** | Firms in a group owning each other's shares. At best the strong firms prop up weak ones; at worst weak firms drag the strong ones down, and outsiders cannot tell how the group is doing. |
| **Keiretsus** | The Japanese corporate groups built on cross holdings. |
| **Intermediate objective functions** | Substitute goals such as maximizing earnings, revenues, firm size, market share or EVA. They work only to the degree they track long-term firm value; otherwise the firm can end up with a disaster. |
| **EVA** | Economic Value Added: operating profit after tax minus a charge for the capital used. Damodaran lists it as one of the substitute objectives, not a replacement for value. |
| **Market based solution** | Letting markets discipline managers, for example through a hostile bid, stockholders withholding votes, or activist investors. Disney is the case: Comcast's 2004 hostile bid and 43% of votes withheld from Eisner. |
| **Activist investors** | Investors who push a company publicly to change management, governance or strategy (CalSTRS at Disney). |
| **Institutional Shareholder Services (ISS)** | A firm that gauges corporate governance at companies and flags concerns such as pay and board monitoring. |
| **Constrained stock price maximization** | Keep stock price as the objective but limit the damage: make managers and employees stockholders, protect lenders from expropriation, give markets honest and prompt information, and minimize social costs. |
| **Protect lenders from expropriation** | Stop stockholders and managers from transferring wealth away from lenders (for example by taking on much riskier projects after borrowing). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |

### What the project asked

Module 1 step 3: **Stated objectives**

1. If the firm states goals, what is it targeting (growth, profitability, stock price, value)?
2. If it states none, what does its behaviour say the primary focus is?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Stated objective | "extend our leadership in observability and IT infrastructure management and grow our market share in adjacent areas", through a "subscription-first approach" | FY2024 10-K Item 1 (`sources/filings/swi-10k-fy2024.md`); ledger `governance.objectives` |
| Pay metrics (2023) | Bonus: 50% revenue, 50% adjusted EBITDA; stock units: 70% Subscription ARR, 30% revenue | 2024 proxy, Compensation Discussion and Analysis (`sources/filings/swi-def14a-2024.md`); ledger `facts.pay-metrics-2023` |
| Subscription ARR (annual recurring revenue) | $233.2M to $311.7M, up 33.7% | FY2024 10-K Item 7; ledger `facts.subscription-arr-2023`, `facts.subscription-arr-2024` |
| Total ARR | $684.1M to $729.0M, up 6.6% | FY2024 10-K Item 7; ledger `facts.total-arr-2023`, `facts.total-arr-2024` |
| Net retention on subscriptions | 99% (2024), 97% (2023) | FY2024 10-K Item 7; ledger `facts.net-retention-subscription` |
| Sales and marketing | $249.3M to $224.9M, down 9.8% ($13.8M reclassification, $11.4M cut programs) | FY2024 10-K operating expenses; ledger `facts.sales-marketing-2024`, `facts.sm-decrease-detail-2024` |
| Adjusted EBITDA vs standardized EBITDA | $384.7M (48.3% of revenue) vs $282.8M | FY2024 10-K non-GAAP reconciliation; ledger `company.ebitda_adjusted`, `company.ebitda_standardized` |
| SUNBURST attack | About 33,000 customers notified; fewer than 18,000 believed affected; net cost $26.2M (2022), $2.1M gain (2023), $10.3M (2024); class action settled for $26 million; SEC sued 2023-10-30 | SUNBURST 8-Ks (`sources/filings/swi-8k-2020-12-14-sunburst-followup.md`), FY2024 10-K Note 15; ledger `facts.sunburst-customers`, `facts.cyber-net-expense`, `facts.class-action-settlement`, `facts.sec-complaint` |
| CEO change decided | 2020-12-07 | 8-K of 2020-12-09 (`sources/filings/swi-8k-2020-12-09-sunburst-disclosure.md`); ledger `facts.ceo-change-2020-12-07` |
| EV to next-twelve-months EBITDA multiple, SolarWinds vs software peers | 15.9 vs 10.9 (2019); 15.7 vs 10.8 (2020); 8.8 vs 12.8 (2024) | DEFM14C, Goldman Sachs analysis; ledger `facts.ev-ntm-ebitda-history` |
| Deal premium and Goldman software-deal premia | 21.9% over $15.18; 25th percentile 19%, 75th percentile 50% | DEFM14C; ledger `facts.goldman-premia-study` |

### Steps to complete the assignment

1. Read the stated objective and the pay plans to find what management steers by. It states growth and market position, not value. Pay is tied to revenue, adjusted EBITDA and Subscription ARR.
2. Check whether the headline metric is a real proxy for value. Subscription ARR grew $233.2M to $311.7M (33.7%) but Total ARR only $684.1M to $729.0M (6.6%). Subscription growth of $78.5M added only $44.8M of total recurring revenue, so about 43% of the headline growth was existing customers converting from maintenance. Net retention of 99% and 97% means the installed base held its dollars rather than grew.
3. Look for value-damaging ways to hit targets. Discounting and bundling: no filing quantifies either, so it cannot be tested. Under-investment: sales and marketing fell 9.8% ($249.3M to $224.9M), including $13.8M of reclassification and $11.4M of cut marketing programs.
4. Check the margin metric. Adjusted EBITDA of $384.7M exceeds standardized EBITDA of $282.8M by $101.9M, mostly $78.3M of stock-based pay and related payroll tax that management adds back and our model treats as a cost.
5. Look for a day of reckoning. SUNBURST (disclosed 2020-12-14): about 33,000 customers notified, net costs of $26.2M, a $2.1M gain and $10.3M over 2022-2024, a $26 million class-action settlement paid by insurance, and an SEC suit from 2023-10-30 with most claims dismissed.
6. Ask who corrected it. Not the board in the way the question assumes: the CEO change was decided 2020-12-07, a week before disclosure. No lender action or activist campaign appears in the sources.
7. Measure the lasting mark. SolarWinds' multiple fell from 15.9 and 15.7 (above peers at 10.9 and 10.8) to 8.8 in 2024 (below peers at 12.8). The cause is not proven: the bidders who withdrew in 2023 cited the early stage of the subscription transition, so the discount mixes SUNBURST, the transition and the 2021 spin-off. A $100 investment at the end of 2019 was worth $51 at the end of 2023 against $211 for the proxy peer group.
8. Answer. Stated objective: growth and market position, with no value target. Behavior adds operating profit and cash payout ($168.2M paid in 2024): the focus is recurring-revenue growth and cash margin, not value per share.

**Result for SolarWinds:** Management steers by Subscription ARR, revenue and adjusted EBITDA, which flatter (43% of ARR growth is conversion; $101.9M gap between adjusted and standardized EBITDA). The SUNBURST attack left a lasting multiple discount (8.8 vs peers' 12.8).
Full answers: [lesson-03.md](lesson-03.md) · Walkthrough: [Step 3](walkthrough.md#step-3-what-is-solarwinds-trying-to-achieve-and-did-anything-ever-hold-it-to-account)

## Lesson 04 — Define and Measure Risk

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Hurdle rate** | (Re-listed for a new angle; first defined in Lesson 01.) Here Damodaran writes it as the riskless rate plus a risk premium, higher for riskier projects. Formula: Hurdle rate = Riskless Rate + Risk Premium |
| **Risk** | Damodaran's view: a mix of danger and opportunity (the two Chinese characters), so neither good nor bad. The question is not whether to avoid risk but how to build it into decisions. |
| **Capital Asset Pricing Model** | The default risk and return model in finance. It measures risk as variance, says only the non-diversifiable part is rewarded, measures that part with beta, and turns beta into a required return. Formula: Expected Return = Riskfree rate + Beta * Risk Premium |
| **Mean-variance framework** | Measuring an investment's risk as variance, the gap between actual and expected returns. |
| **Diversification** | Holding many investments so that the risks specific to each one cancel out. Only the risk that cannot be diversified away (market risk) earns a reward. |
| **Marginal investor** | The investor most likely to be the buyer or seller on the next trade, who sets the stock price. Must own a lot of stock and trade regularly, so the largest holder (e.g. a founder) may not be one. All models assume the marginal investor is well diversified. |
| **Market portfolio** | A portfolio of every asset in the economy in proportion to market value, the limit of diversification if it costs nothing. Investors choose their risk level by mixing it with a riskless asset such as a T-Bill (or borrowing to hold more of it). |
| **Covariance** | How much an asset moves with the market. The risk of an asset is the risk it adds to the market portfolio. |
| **Beta** | The standardized measure of non-diversifiable risk: the asset's covariance with the market divided by the market's variance. Average risk is 1. Formula: Expected Return = Riskfree Rate + Beta * (Expected Return on the Market Portfolio - Riskfree Rate) |
| **APM** | Arbitrage Pricing Model. If there are no arbitrage opportunities, market risk is captured by betas against several unspecified factors found by factor analysis, not one market portfolio. |
| **Multi-Factor Model** | Like the APM but with betas against specified, named market factors. These explain past returns better than the CAPM but are less reliable at predicting expected returns. |
| **Limitations of the CAPM** | Unrealistic assumptions, parameters that cannot be estimated precisely (index choice, a firm that changed), and weak empirical fit (size and price/book seem to explain returns better than beta). It persists as the default model anyway. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

Module 1 step 4: **Share classes and the marginal investor**

1. How many classes of shares exist and what are the voting rights of each?
2. Who are the largest shareholders?
3. Is the marginal investor an individual or an institution?
4. Is that marginal investor diversified?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Share classes | One class of common stock, one vote a share; 50 million preferred authorized, none issued | FY2024 10-K note 10 (`sources/filings/swi-10k-fy2024.md`); ledger `governance.share_classes` |
| Basic shares outstanding | 171.6M | Merger information statement (DEFM14C), record-date share count (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `company.shares_basic` |
| Largest holders | Silver Lake 36.56%, Thoma Bravo 29.79%; no other 5% holder | 2024 proxy ownership table (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders` |
| Public float and marginal investor | About 34%, held by diversified institutions | Proxy ownership table; ledger `governance.marginal_investor` |
| Stock held by non-affiliates | $661.3M on 2024-06-28 | FY2024 10-K cover page; ledger `facts.float-nonaffiliate-value` |
| EV to next-twelve-months EBITDA multiple | SolarWinds 14.0 (2021), 9.9 (2022); software peers 12.0 (2021), 11.0 (2022) | DEFM14C, Goldman Sachs analysis; ledger `facts.ev-ntm-ebitda-history` |
| Goodwill write-down in 2022 | $891.1M | FY2024 10-K 2022 column; ledger `company.history` |
| Equity value, book equity, goodwill | $2,604.9M; $1,400.7M; $2,363.2M | Ledger `company.equity_value` (171.6M shares x $15.18), `company.equity_book`, `company.goodwill` (FY2024 10-K balance sheet) |
| Price to book, SolarWinds vs peers | 1.86x vs 4.58x median | model-output.md section 7 |
| Bottom-up beta, unlevered and relevered | 1.22 and 1.6714 | Damodaran January 2025 industry betas (`sources/market-data/industry-betas-2025-01-05.json`); model-output.md section 1 |
| Customers | Over 300,000 | FY2024 10-K; ledger `facts.sunburst-customers` / `facts.customer-count` |

### Steps to complete the assignment

1. Count the share classes and votes: one class of common stock, one vote a share, no preferred issued.
2. List the largest holders from the proxy: Silver Lake 36.56% and Thoma Bravo 29.79%, no other 5% holder. Basic shares are 171.6M.
3. Identify the marginal investor, the buyer or seller whose trades set the price. The sponsors are not trading at the margin; diversified institutions holding the roughly 34% float are. Answer: an institution, and diversified.
4. Ask whether firm-specific risk matters. The attack, the SEC suit and the 2021 N-able spin-off are firm-specific, so a diversified investor washes them out of beta. They belong in the cash-flow forecast, not the discount rate. Customer concentration is low (over 300,000 customers).
5. Separate market-wide from firm-specific in the 2022 multiple collapse. Peers fell from 12.0 to 11.0, a 1.0 market-wide drop; SolarWinds fell from 14.0 to 9.9, so its further 3.1 turns were its own. The same year it wrote down $891.1M of goodwill.
6. Check whether a proxy model (cost of equity from size and price-to-book) should replace CAPM (the capital asset pricing model). Equity value of $2,604.9M is under the $5 billion small-firm line and price to book is 1.86x against 4.58x, which would score as riskier. But $2,363.2M of goodwill sits in $1,400.7M of book equity, so the low ratio reflects accounting more than risk. No proxy number was computed because the course coefficients are not in the ledger.
7. Answer. Keep CAPM with the market beta: unlevered 1.22, relevered to 1.6714, cost of equity 12.65%. Firm-specific events: the attack, the SEC suit and the spin-off. Both: the 2022 multiple collapse.

**Result for SolarWinds:** One share class; Silver Lake (36.56%) and Thoma Bravo (29.79%) hold the control blocks, but diversified institutions holding about 34% set the price, so market beta (1.6714 levered) is the right risk measure.
Full answers: [lesson-04.md](lesson-04.md) · Walkthrough: [Step 4](walkthrough.md#step-4-who-sets-solarwinds-share-price-and-does-that-investor-spread-their-bets)

## Lesson 05 — The Risk Free Rate

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Riskfree rate** | Damodaran's definition: the rate on an asset whose actual return always equals its expected return. That needs two things: no default risk (generally a government issuer, though not every government qualifies) and no reinvestment-rate uncertainty. |
| **Default risk** | The chance the issuer fails to pay. This is why a riskfree security generally has to be issued by a government that cannot default. |
| **Zero coupon security** | A bond that pays only at maturity, with no interim payments to reinvest. It removes reinvestment uncertainty, so the theoretically right riskfree rate for a cash flow in year N is the N-year zero coupon rate. |
| **Reinvestment rate uncertainty** | Not knowing what rate you will earn when interim payments are reinvested. It is one of the two conditions that must be absent for an asset to be riskfree. |
| **Long term government rate** | The practical bottom line: use a long-term government bond rate as the riskfree rate on all cash flows in a long-term analysis (a short-term rate for short-term analysis). Example: the ten-year US treasury rate (2.75% in November 2013). |
| **Currency consistency** | The riskfree rate must be in the same currency as the cash flows (dollar cash flows get a dollar rate, euro flows a euro rate). The rate comes from the government that controls issuing that currency. |
| **Default spread** | The extra yield a government's (or company's) bonds pay over a riskless rate to compensate for default risk. |
| **Sovereign default spread** | The default spread on a government's bonds, estimated from its sovereign rating. A government with default risk has a bond rate that is not riskfree. |
| **Riskfree rate when the government has default risk** | Three options: subtract the default spread from the local government rate (India 8.82% - 2.25% = 6.57%), do the analysis in another currency where a riskfree rate is easy (e.g. US dollars), or work in real terms. |
| **Real riskfree rate** | A riskfree rate with inflation removed, measured by the inflation-indexed treasury rate. Use it only when the analysis is in real terms. |
| **Expected market risk premium** | The premium expected for investing in risky assets (the market portfolio) over the riskless asset. It is one of the three CAPM inputs, along with the riskfree rate and beta. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

Module 1 step 5: **Currency and risk-free rate**

1. What currency does the company report in?
2. What currencies are its revenues in?
3. What currency will the analysis use, and why?
4. What is the 10-year government bond rate in that currency on the analysis date, and what is the government's rating?
5. What default spread goes with that rating, and what risk-free rate is left after netting it?
6. Is the equity risk premium measured over that same risk-free rate, or over the gross bond rate?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Reporting currency | US dollars; forecast and term loan also in dollars | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `meta.reporting_currency`, `forecast.years`, `debt.currency` |
| Revenue by customer location | United States $516.6M, international $280.3M, of $796.9M | FY2024 10-K Note 16; ledger `country.exposures` |
| Other currencies sold in | Euro, British pound, Australian dollar | FY2024 10-K Item 7A; ledger `facts.fx-currencies` |
| 10-year US Treasury yield, 2025-02-05 | 4.43% | FRED series DGS10 (`sources/market-data/market-rates-2025-02-05.json`, `rates-2025-02-05.md`); ledger `market.govt_bond_rate` |
| Government rating and default spread | Moody's Aaa; 0.00% | Damodaran January 2025 country risk table (`sources/market-data/country-risk-2025-01-01.json`); ledger `market.sovereign_default_spread` |
| Damodaran start-of-month Treasury rate | 4.54% | Damodaran ERPFeb25.xlsx (`sources/market-data/rates-2025-02-05.md`); ledger `market.mature_erp` note |
| Foreign governments' ratings and spreads | Germany and Australia Aaa, 0.00%; UK Aa3, 0.59% | Damodaran January 2025 country table; ledger `facts.default-spreads-2025-01` |
| Buyer's new dollar debt | $2,225.0M first-lien loan, $200.0M revolver, $525.0M second-lien | Closing 8-K (`sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`); ledger `facts.new-debt-2025` |
| Revolver at year-end | Undrawn | FY2024 10-K note 9; ledger `debt.revolver_undrawn` |

### Steps to complete the assignment

1. Find the currency of the cash flows. SolarWinds reports, forecasts and borrows in US dollars, so the analysis is in dollars. Revenue is $516.6M US and $280.3M international of $796.9M, but the filing does not say how much of the international part is billed in foreign currency.
2. Decide whether foreign sales change the currency. They do not: euro, pound and Australian-dollar sales affect the dollar size of cash flows, which the forecast already states in dollars. Cash flows and the discount rate must be in the same currency.
3. Take the 10-year government bond rate in that currency on the analysis date: the US 10-year Treasury closed at 4.43% on 2025-02-05 (FRED DGS10).
4. Net out the default spread. Moody's rated the US Aaa that day, so the spread is 0.00% and the risk-free rate is 4.43% - 0.00% = 4.43%. (Moody's downgraded the US on 2025-05-16, after the analysis date.)
5. Check the equity risk premium (ERP) uses the same base. Damodaran's 4.27% premium is measured on his start-of-month rate of 4.54%; the 4.43% close is 0.11 points lower, inside the 0.25-point tolerance, so the daily close is used.
6. Rule out distractions. Foreign slice: the filing gives no revenue split by currency, so no separate netting; Germany and Australia carry 0.00% spreads and the UK 0.59% anyway. The buyer's $2,225.0M, $200.0M and $525.0M loans change leverage (beta and weights), not the risk-free rate.
7. Answer. Currency: US dollars. 10-year rate: 4.43%; rating Aaa; default spread 0.00%; risk-free rate 4.43%.

**Result for SolarWinds:** Dollar analysis with a risk-free rate of 4.43% (Treasury close on 2025-02-05, zero default spread under the Aaa rating).
Full answers: [lesson-05.md](lesson-05.md) · Walkthrough: [Step 5](walkthrough.md#step-5-what-return-could-an-investor-earn-with-no-risk-at-all-in-dollars-on-the-day-we-value-solarwinds)

## Lesson 06 — Equity Risk Premiums

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Equity risk premium** | The extra return investors demand for putting money in an average-risk investment (stocks) instead of the riskless asset. It should be above zero, rise with investors' risk aversion and rise with the riskiness of the average investment. It changes over time. |
| **Risk aversion** | How much investors dislike risk. The more of it in a market, the higher the equity risk premium (it rises after a crash). |
| **Survey approach** | Estimating the premium by asking investors, CFOs, analysts or academics what they require. Limits: no reasonability constraints, very volatile answers, and horizons of a year or less. |
| **Historical risk premium** | Assuming the premium actually delivered over long periods equals the expected premium, e.g. US stocks minus T-bonds from 1928. |
| **Standard error** | The noise in an estimate, here the historical premium. Formula: Standard error = Annualized standard deviation in stock prices / Square root of the number of years of data. Hence "go back as far as you can". |
| **Arithmetic average** | Simple average of annual returns. Damodaran's rule: use arithmetic premiums for one-year estimates of the cost of equity. |
| **Geometric average** | Compounded annual return. Use geometric premiums for long-term estimates of the cost of equity. Be consistent in which riskfree rate (T-bill or T-bond) you subtract. |
| **Implied premium** | The third estimating approach: back out the premium from today's asset prices, i.e. what investors are paying for stocks. (Developed further in Lesson 07.) |
| **Country risk premium** | Extra premium added to a mature-market premium for riskier countries. Sovereign default spread approach: add the country's default spread (from its rating) to the US premium. Formula: Total ERP = Mature market ERP + Country default spread |
| **CDS** | Credit default swap spread: the market price of insuring a government's debt against default, used instead of the rating-based default spread. |
| **Scaled up default spread** | Because equities are riskier than bonds, scale the default spread by the ratio of equity volatility to bond volatility. Formula: Country risk premium = Country default spread * (Standard deviation of equity / Standard deviation of country bond) |
| **Historical premiums for other markets** | Data for non-US markets cover much shorter periods, especially in emerging markets, so estimates carry much greater error. Damodaran's point: if you distrust the US history, trust the rest even less. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

Module 1 step 6: **Mature-market equity risk premium**

1. What is the equity risk premium for a mature market today, by which method (implied, historical, survey), from which source?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Implied ERP, mature market | 4.27% (S&P 500 at 6040.53), dated 2025-02-01 | Damodaran ERPFeb25.xlsx (`sources/market-data/market-rates-2025-02-05.json`); ledger `market.mature_erp` |
| Historical ERP, 1928-2022, stocks over Treasury bonds | 6.64% arithmetic (standard error 2.15%); 5.06% geometric | Course spreadsheet (`01-foundations-and-discount-rates/lesson-06/spreadsheet-histretsp.md`); ledger `facts.hist-erp-1928-2022` |
| Survey ERP | Not available for February 2025 | No file in `sources/` |
| Risk-free rate | 4.43% | FRED DGS10 on 2025-02-05; ledger `market.risk_free_rate` |
| Levered beta | 1.6714 | model-output.md section 1 |
| Country-risk scalar | 1.3475 (equity premium = default spread x 1.3475) | Damodaran January 2025 country workbook (`sources/market-data/country-risk-2025-01-01.json`); ledger `facts.country-erp-scalar` |
| US default spread | 0.00% | Same workbook; ledger `market.sovereign_default_spread` |
| Weighted ERP used, and resulting cost of equity | 4.92%; 12.65% | Computed in lesson 7; model-output.md section 1 |

### Steps to complete the assignment

1. List the three ways to estimate the ERP: survey, historical average, implied from today's prices. Choose the implied premium because it is forward-looking and tied to the valuation date.
2. Take the implied premium from Damodaran's February 2025 workbook: 4.27%. (The January country workbook shows 4.33% for mature markets; the later February figure is used.)
3. Compute the cost of equity under the implied premium with a US-only premium so methods compare cleanly: 4.43% + 1.6714 x 4.27% = 11.57%.
4. Compute under the historical premiums: 6.64% gives 15.53%; 5.06% gives 12.89%. The 2.15% standard error is a third the size of the 6.64% premium, so the historical figure is too noisy to anchor on.
5. Survey: no February 2025 figure is in the files, so no cost of equity is computed.
6. Private status: not an issue at the valuation date. SolarWinds was listed through 2025-02-05, and the premium is the market's price of risk, not a firm attribute.
7. Country-risk method: use the scaled method. Each country's equity premium over the mature market is its default spread x 1.3475. The US spread is 0.00%, so scaling does nothing to the 64.82% US slice. Using raw spreads for the international slice instead would give a weighted premium of about 4.75% instead of 4.92%, about 0.28 points lower in cost of equity.
8. Answer. Mature-market ERP: 4.27%, implied from the S&P 500 and expected cash flows (Damodaran, dated 2025-02-01). Used with the country weighting (lesson 7), the weighted 4.92% gives the 12.65% cost of equity.

**Result for SolarWinds:** Mature-market ERP of 4.27% (implied method). Cost of equity would be 11.57% at that premium, 15.53% or 12.89% on the historical premiums, and 12.65% with the country-weighted 4.92% actually used.
Full answers: [lesson-06.md](lesson-06.md) · Walkthrough: [Step 6](walkthrough.md#step-6-how-much-extra-return-do-investors-demand-for-owning-stocks-instead-of-risk-free-bonds)

## Lesson 07 — Country Risk Premiums

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Implied ERP** | (Re-listed for a new angle; introduced in Lesson 06.) "Watch what I pay, not what I say": from the price investors pay for stocks and expected cash flows, back out the expected return and the implied premium. It is forward-looking and updated, and was 5.5% in November 2013 versus a 4.20% historical figure. |
| **Mature market ERP** | The premium Damodaran uses for all mature markets: 5.5% in November 2013 (set equal to the implied US premium) and 5% in January 2014. |
| **Mature market** | Damodaran's measurable definition: any AAA rated country. |
| **Composite way of estimating ERP for countries** | A three-step recipe: (1) estimate a mature-market ERP, (2) define a mature market (AAA rating), (3) add an extra premium for non-mature markets, either the default spread or a scaled-up default spread. |
| **Emerging Market ERP** | The mature market premium plus a country risk premium. Formula: Emerging Market ERP = Mature market ERP + Country Default Spread * (Standard deviation of equity / Standard deviation of country bond) |
| **TRP and CRP** | In the country tables, TRP is the total risk premium (total ERP) and CRP is the country risk premium, the part above the mature-market premium. |
| **ERP by incorporation** | The conventional practice: use the premium of the country where the company is incorporated (a US firm gets the US premium, Vale gets Brazil's). |
| **ERP by operations** | Damodaran's "more sensible" practice: weight the premiums of the regions where the company operates, by revenue. Disney in 2013: 5.76% from its revenue mix, not the US 5.50%. |
| **Anatomy of a crisis** | The slides track the implied ERP from September 2008 to January 2009, showing it moving sharply during a crisis, so premiums are not constant. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

Module 1 step 7: **Country risk and weighted ERP**

1. What is the best measure of the company's country exposure (revenues, production, assets)?
2. What is the geographic breakdown of that measure?
3. What is the weighted average ERP?
4. Why might that ERP change?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Revenue by customer shipping address | United States $516.6M (64.82%), international $280.3M (35.18%), total $796.9M; no other country at 10% | FY2024 10-K Note 16 (`sources/filings/swi-10k-fy2024.md`); ledger `country.exposures` |
| Mature-market ERP (February 2025) | 4.27% | Damodaran ERPFeb25.xlsx (`sources/market-data/market-rates-2025-02-05.json`); ledger `market.mature_erp` |
| Mature-market ERP (January 2025) and EMEA regional ERP | 4.33% and 6.17%, a 1.84-point difference | Damodaran January 2025 country workbook, Regional Weighted Averages (`sources/market-data/country-risk-2025-01-01.json`) |
| Alternative regional premiums | Western Europe 1.12 points; global average 1.43 points | Same workbook; ledger `country.exposures` note |
| Employees | 2,107 total: 1,379 outside the US, 728 inside | FY2024 10-K; ledger `facts.employees-2024` |
| Risk-free rate and levered beta | 4.43%; 1.6714 | FRED DGS10; model-output.md section 1 |

### Steps to complete the assignment

1. Choose the measure of country exposure. Revenue, because it follows customers and is the only geographic split disclosed (Note 16). Staff location (65% abroad) matters for costs and currency, not for the premium.
2. Split revenue: US $516.6M ÷ $796.9M = 64.82%; international $280.3M ÷ $796.9M = 35.18%.
3. Assign the US the mature-market premium of 4.27% (its default spread is 0.00%).
4. Build the international premium. The filing gives no regional split, so use the EMEA (Europe, Middle East and Africa) premium for all of it, since most international offices are in Europe. EMEA 6.17% less the January mature premium of 4.33% = 1.84 points, added to the February mature 4.27% = 6.11%.
5. Weight by revenue: 64.82% x 4.27% + 35.18% x 6.11% = 4.92%. This is 0.65 points above the flat US 4.27%.
6. Test the judgment call. Western Europe (1.12 points) would give 4.66%; the global average (1.43 points) 4.77%. EMEA is the cautious choice; the gap between 4.66% and 4.92% is 0.26 points of premium, about 0.43 points of cost of equity at a beta of 1.6714.
7. Answer. Best measure: revenue. Breakdown: US 64.82%, international 35.18%. Weighted ERP: 4.92%. It would change with a regional revenue disclosure, Damodaran's January and July updates, a US rating cut (as in May 2025), or a shift in the international share.

**Result for SolarWinds:** Weighted ERP of 4.92% (64.82% US at 4.27%, 35.18% international at 6.11%), which feeds a 12.65% cost of equity (4.43% + 1.6714 x 4.92%).
Full answers: [lesson-07.md](lesson-07.md) · Walkthrough: [Step 7](walkthrough.md#step-7-does-where-solarwinds-sells-change-the-price-of-risk)

## Lesson 08 — Regression Betas

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Regression beta** | The standard way to estimate beta: regress the stock's returns against market returns and take the slope as beta. Formula: Rj = a + b Rm, where a is the intercept and b the slope (beta). It is also called the top-down beta (see Lesson 10). |
| **Slope** | The slope of the regression line. It is the stock's beta, how much the stock moves per unit move in the market. |
| **R squared** | The share of a firm's risk (variance) that comes from market risk. The remainder is firm-specific risk. Disney's 73% means 73% market and 27% firm-specific. |
| **Firm-specific risk** | The part of a stock's risk (1 - R squared) that is diversifiable and therefore not rewarded. |
| **Intercept** | The regression's constant: a simple measure of how the stock performed in the period relative to what the CAPM predicted. |
| **Jensen's alpha** | Performance versus the CAPM: the intercept minus the riskfree rate times (1 - beta), with the riskfree rate converted to the return period (monthly = annual rate/12). Positive means the stock did better than expected. Formula: Jensen's alpha = Intercept - (Riskfree Rate/n)(1 - Beta) |
| **Standard error of the beta** | The estimation error on the beta. Add and subtract one standard error for roughly 67% confidence and two for 95%. Disney: 1.25 +/- 0.10 gives a 67% range of 1.15 to 1.35. |
| **Estimation period** | The window of data for the regression. Services use 2 to 5 years. Longer gives more data but the firm changes; shorter is more affected by firm-specific events. |
| **Return interval** | How often returns are measured (daily, weekly, monthly). Shorter intervals give more observations but more noise, because non-trading biases all betas toward one. |
| **Market index** | The proxy for the market portfolio in the regression (e.g. S&P 500). Returns include dividends. |
| **Cost of equity** | The expected return equity investors need to break even. It is also the project hurdle rate from an equity standpoint. Formula: Cost of equity = Riskfree Rate + Beta * Risk Premium. Disney 2013: 2.75% + 1.25 (5.76%) = 9.95%. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **Capital IQ** | S&P's paid database of company financials, market data, deals, ownership and credit information, standardized across companies. | Cross-checking figures and quickly assembling comparables or deal histories. Cite the filing itself when the filing has the number. | Subscription only (this course provides an NYU academic account through the final-project due date). |

### What the project asked

Module 1 step 8: **Regression beta**

1. What is the regression beta, against which index, over what window and interval?
2. What are the standard error and R-squared, and is the estimate reliable?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Trading life of the stock | NYSE from 2018-10-19 to delisting at closing on 2025-04-16 | FY2018 10-K cover (`sources/filings/swi-10k-fy2018.md`); closing 8-K (`sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`); ledger `facts.listing-dates` |
| N-able spin-off and reverse split | 2021-07-19; one-for-two on 2021-07-30 | FY2023 10-K (`sources/filings/swi-10k-fy2023.md`); ledger `facts.corporate-actions-2021` |
| Special dividends | $1.50 paid 2021-08-24; $1.00 ($168.2M) paid 2024-04-15 | FY2023 and FY2024 10-Ks; ledger `facts.special-dividend-2021`, `company.history` |
| Deal announcement | 2025-02-07 (price pinned near $18.50 afterward) | Merger 8-K (`sources/deal-docs/swi-8k-2025-02-07-merger-agreement.md`) |
| Non-affiliate float | $661.3M on 2024-06-28 | FY2024 10-K cover page; ledger `facts.float-nonaffiliate-value` |
| Price history | Not obtainable (delisted ticker); regression fields listed as omitted | `sources/README.md` "Could not be obtained"; ledger `meta.omitted` |
| Stock return data in the proxy | Four annual points | 2024 proxy pay-versus-performance table; ledger `facts.tsr-2023` |
| Substitute beta | Unlevered 1.22, relevered 1.6714 | Damodaran January 2025 industry betas; model-output.md section 1 |

### Steps to complete the assignment

1. State the regression design: index S&P 500, weekly or monthly returns, five-year window, returns including dividends.
2. Check the listing window: NYSE from 2018-10-19 to 2025-04-16.
3. Check the series for breaks: N-able spin-off 2021-07-19, one-for-two reverse split 2021-07-30, $1.50 special dividend paid 2021-08-24, $1.00 special dividend paid 2024-04-15. Dividends must be in the returns.
4. Set the usable window. After the 2025-02-07 announcement the price sat near $18.50, so the window ends on 2025-02-05; after the spin-off that leaves about three and a half years, including the cyberattack and a thin float ($661.3M non-affiliate value).
5. Try to get the data. Free sources no longer serve delisted tickers and Capital IQ's chart did not load, so no regression was run. Standard error, R-squared and Jensen's alpha are therefore not available either. The proxy's four annual points are too few to substitute.
6. Decide. Use the bottom-up beta instead: industry unlevered 1.22, relevered to 1.6714. A price history, if found later, would be a cross-check.
7. Answer. Regression beta, index, window: not computed (`beta.regression_beta` and related fields are listed in `meta.omitted`). Standard error and R-squared: not available. The bottom-up 1.22 is used.

**Result for SolarWinds:** No regression beta exists; the delisted ticker's price history could not be obtained and the series would have been broken by the spin-off, reverse split, special dividends and the pending deal. The bottom-up beta (1.22 unlevered, 1.6714 levered) is used.
Full answers: [lesson-08.md](lesson-08.md) · Walkthrough: [Step 8](walkthrough.md#step-8-can-solarwinds-own-share-price-history-tell-us-how-risky-it-is)

## Lesson 09 — Beta Fundamentals

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Index effects on risk parameters** | The market index chosen changes beta, standard error and R squared (Deutsche Bank on the DAX versus the FTSE European index; Baidu on the S&P 500 versus the NASDAQ). A regression beta depends on the index used. |
| **Determinants of beta** | Damodaran's three fundamental drivers of a firm's beta: product type, operating leverage and financial leverage. |
| **Product type** | The beta depends on how sensitive demand for the firm's products and its costs are to the macroeconomy. Cyclical and discretionary-product firms have higher betas. |
| **Cyclical companies** | Firms whose sales move strongly with the economy. They have higher betas than non-cyclical firms. |
| **Operating leverage** | The proportion of a firm's total costs that are fixed. Higher operating leverage means more volatile earnings and a higher beta. |
| **Fixed Costs Measure** | A measure of operating leverage. Formula: Fixed costs / Variable costs. |
| **EBIT Variability Measure** | A measure of operating leverage showing how fast operating earnings move with sales. Formula: % Change in EBIT / % Change in Revenues. |
| **Financial leverage** | Borrowing. Interest payments are fixed costs that make earnings to equity investors more volatile, so equity beta rises. |
| **Levered beta** | Also called equity beta. The beta of a firm's equity including the effect of its debt. A regression beta is levered, reflecting the average market D/E during the regression period. |
| **Unlevered beta** | Also called asset beta. The beta of the business with the effect of debt removed. Formula: bL = bu (1 + (1 - t) D/E), where D/E is market value debt to equity and t the marginal tax rate. Disney: 1.25 / (1 + (1 - 0.361)(0.1944)) = 1.1119. |
| **Marginal tax rate** | The tax rate on the next dollar of income, used in levering and unlevering betas because interest is tax deductible. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

Module 1 step 9: **Beta fundamentals**

1. From what the company sells, should its beta be high or low? Do its businesses differ?
2. From its cost structure (fixed vs. variable), what beta would you expect?
3. How much does its borrowing raise its beta?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Customer behavior | Subscription net retention 99%; maintenance renewal 97%; recurring revenue 93.5% of $796.9M; over 300,000 customers | FY2024 10-K Item 7 (`sources/filings/swi-10k-fy2024.md`); ledger `facts.net-retention-subscription`, `facts.maintenance-renewal-rate`, `facts.recurring-revenue-share`, `facts.customer-count` |
| Segment disclosure | "We operate as a single reportable segment"; subscription $304.5M, maintenance $440.6M, license $51.8M | FY2024 10-K Note 16 |
| Cost structure | Cost of revenue $83.3M (10.5% of revenue); operating expenses $505.2M (63.4%); 2,107 employees | FY2024 10-K income statement; ledger `facts.cost-of-revenue-2024`, `facts.operating-expenses-2024`, `facts.employees-2024` |
| Operating income, 2023 and 2024 | $150.4M and $208.4M; revenue $758.7M and $796.9M | FY2024 10-K; ledger `company.history` |
| Debt and equity | $1,285.0M and $2,604.9M; D/E 0.4933 | Ledger `company.debt_total`, `company.equity_value`; model-output.md section 1 |
| Marginal tax rate | 25% | Damodaran January 2025 country tax rates (`sources/market-data/country-risk-regions-2025-01-01.md`); ledger `market.tax_rate_marginal` |
| Industry unlevered beta | 1.22 (333 US software firms); all-market 0.82; Software (Internet) 1.60 | Damodaran January 2025 betas (`sources/market-data/industry-betas-2025-01-05.json`); ledger `beta.unlevered_bottom_up`, `facts.industry-beta-all-market`, `facts.industry-beta-software-internet` |

### Steps to complete the assignment

1. Ask what the company sells. Customers keep the product (99% and 97% renewal, 93.5% recurring revenue, over 300,000 customers), pointing to a beta at or below the market. Only the $51.8M of licenses (6.5%) is deferrable. The three contract types are billing methods, not different businesses (one segment).
2. Ask about the cost structure. Variable cost is small (cost of revenue 10.5%) and fixed cost is large (operating expenses 63.4%). Revenue grew 5.0% in 2024 while operating income grew 38.6% ($150.4M to $208.4M), showing operating leverage that cuts the other way in a bad year.
3. Compute debt to equity: $1,285.0M ÷ $2,604.9M = 0.4933.
4. Relever the business beta: 1.22 x (1 + (1 - 0.25) x 0.4933) = 1.6714.
5. Size the debt effect: 1.6714 - 1.22 = 0.4514, which is 37.0% on top of the business beta and 27.0% of the levered beta.
6. Judgment. Do not lower 1.22 for the sticky product: one firm's retention is a reason to doubt the group beta, not a replacement for it. Business risk and operating leverage are both inside the 1.22 and cannot be separated by arithmetic; only the debt part is computed. No regression beta exists.
7. Answer. Product: low to middling beta. Cost structure: higher than the product alone suggests. Borrowing lifts beta from 1.22 to 1.6714, a rise of 0.4514 or 37.0%.

**Result for SolarWinds:** The product is sticky but fixed costs and debt amplify risk: beta rises from 1.22 to 1.6714 (+0.4514, or 37.0%) at debt to equity of 0.4933.
Full answers: [lesson-09.md](lesson-09.md) · Walkthrough: [Step 9](walkthrough.md#step-9-why-is-solarwinds-stock-risky-and-how-much-of-that-risk-comes-from-its-debt)

## Lesson 10 — Bottom-up Betas

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Betas are weighted averages** | The beta of a portfolio is the market-value-weighted average of its parts. This applies to mutual funds and to a firm after a merger, and is why a firm's beta can be built from its businesses. |
| **Top-down beta** | The beta from a regression of the firm's own stock returns (see Lesson 08). |
| **Bottom-up beta** | Damodaran's preferred beta. Find the businesses the firm is in, take the unlevered betas of other firms in those businesses, weight by sales or operating income, then lever up using the firm's D/E. It has a much lower standard error and reflects the current mix of businesses. |
| **Pure play beta** | The unlevered beta of one business alone, backed out of comparable firms' regression betas (e.g. Disney's movie business). |
| **Median regression beta** | The step-one number: the median beta across comparable firms, used to reduce noise. Studio entertainment median: 1.24. |
| **Gross D/E ratio** | Debt (not netted for cash) divided by equity, used to unlever the comparables' betas (27.06% for movie companies). |
| **Net D/E ratio** | (Debt - Cash) / Equity. It is an alternative to unlevering with gross debt and then removing the cash effect separately. |
| **Cash effect** | Cash is close to riskless (beta of zero) and dilutes a firm's beta. To get the pure business beta: Unlevered beta corrected for cash = Unlevered beta / (1 - Cash/Firm Value). Movies: 1.0668 / (1 - 0.0296) = 1.0993. |
| **Unlevered beta of the company** | Operating-asset beta and cash beta (zero), weighted by value. Disney: 0.9239 x (135,132/139,063) + 0 = 0.8978. |
| **Levered beta of divisions** | Allocate the firm's debt to divisions (Disney used identifiable assets), compute D/E per division, and relever each division's beta. |
| **Divisional cost of equity** | Each business has its own risk, so its own cost of equity. The CFO discussion: a movie-division project promising 9.5% should be judged against the movie business's cost of equity, not Disney's overall one. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

Module 1 step 10: **Bottom-up unlevered beta**

1. What is the bottom-up unlevered beta from comparable firms, cash-corrected?
2. If the company has several businesses, what is each segment's beta and the weighted average?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Segment structure | Single reportable segment | FY2024 10-K Note 16 (`sources/filings/swi-10k-fy2024.md`) |
| Revenue by contract type | Subscription $304.5M (38.2%), maintenance $440.6M (55.3%), license $51.8M (6.5%) | FY2024 10-K Note 16; ledger `facts.subscription-revenue`, `facts.maintenance-revenue`, `facts.license-revenue` |
| Comparable group | Damodaran US Software (System and Application): 333 firms | Damodaran January 2025 industry betas (`sources/market-data/industry-betas-2025-01-05.json`) |
| Group levered beta, debt-to-equity, unlevered beta | 1.24; 4.9%; 1.1960 | Same file; ledger `facts.industry-software-levered-beta`, `facts.industry-software-de-ratio`, `facts.industry-software-unlevered-raw` |
| Cash as share of firm value | 1.74% | Same file; ledger `facts.industry-software-cash-share` |
| Cash-corrected unlevered beta | 1.22 | Same file; ledger `beta.unlevered_bottom_up` |
| Growth by product | Subscription revenue +30.0%; maintenance -4.6% | FY2024 10-K; ledger `facts.subscription-growth-2024`, `facts.maintenance-decline-2024` |
| Higher-beta illustration | Software (Internet) 1.60 | Same file; ledger `facts.industry-beta-software-internet` |
| Company-wide hurdle rates | Cost of equity 12.65%; cost of capital 10.23% | model-output.md section 1 |

### Steps to complete the assignment

1. Find out whether SolarWinds is one business or several. The 10-K says "We operate as a single reportable segment", and the CEO assesses performance at the consolidated level.
2. Check the only breakdown available. Contract type (subscription 38.2%, maintenance 55.3%, license 6.5%) describes how customers pay, not what they buy, and no filing gives profit or capital by product. So no segment weights are built.
3. Choose the comparable group: Damodaran's US Software (System and Application), 333 firms, January 2025 file (valuation date is 2025-02-05).
4. Unlever and correct for cash. Group levered beta 1.24 unlevered at the group's debt to equity of 4.9% and tax gives 1.1960. Cash (1.74% of firm value) has a beta near zero and dilutes the business beta, so removing it gives 1.22.
5. Apply one beta, 1.22, at 100% weight. Segment betas are not built (`beta.segments` is empty and listed in `meta.omitted`).
6. Note the weakness. The observability subscription business (revenue +30.0%) is a candidate for a riskier piece than shrinking maintenance (-4.6%). Software (Internet) at 1.60 shows how far apart they could be, but that is illustration only, not an input.
7. Answer. Bottom-up unlevered beta: 1.22. Segment betas: none, one business at 100%. Company-wide hurdle rates are a 12.65% cost of equity and a 10.23% cost of capital; a single rate is too low for a bet on a new observability product and too high for renewals.

**Result for SolarWinds:** One segment, one beta: unlevered 1.22 from 333 US software firms (cash-corrected, January 2025), used company-wide.
Full answers: [lesson-10.md](lesson-10.md) · Walkthrough: [Step 10](walkthrough.md#step-10-how-risky-is-solarwinds-business-measured-from-similar-companies)

## Lesson 11 — The "Right" Beta

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Bottom-up beta for a multi-business firm** | Compute a cost of equity business by business (Vale: metals & mining, iron ore, fertilizers, logistics) using each business's unlevered beta and the firm's D/E, then weight them. |
| **Sample size** | Slides stress using many comparables (Tata Motors: 76 auto firms; Baidu: 42 online advertising firms). The slide motto is "the law of large numbers is your best friend", meaning bigger samples reduce estimation error. |
| **Differential inflation approach** | Converting a discount rate from one currency to another with only the expected inflation rates of the two. Formula: Cost of equity in R$ = (1 + $ cost of equity) * (1 + Brazil inflation)/(1 + US inflation) - 1. Vale: 11.23% in dollars becomes 18.87% in reais. |
| **Nominal cost of equity** | A cost of equity that includes expected inflation in its currency (nominal $R is higher than the dollar rate). Compute it either by converting or from the local riskfree rate: 10.18% + 1.15 (7.38%) = 18.67%. |
| **Banks** | For banks, Damodaran does not unlever or relever betas, because estimating debt and equity for a bank is "an exercise in futility". |
| **Non-traded assets** | Assets with no stock price or return history (a private business like Bookscape), so regression betas are impossible. Two routes: comparable firms, or accounting earnings. |
| **Comparable firms approach** | Estimate the private firm's beta from the median unlevered beta of public comparables, then relever. Bookscape: 0.8130 / (1 + (1 - 0.4)(0.2141)) = 0.7205, / (1 - 0.05) = 0.7584, relevered 0.8558. |
| **Book versus market D/E** | Levering needs market D/E, but a private firm has only a book ratio. Bookscape assumes the industry median market D/E of 21.41%. |
| **Total risk versus market risk** | A beta measures only market risk, because it assumes a diversified owner. Owners of most private firms are not diversified, so market beta understates the risk they bear. |
| **Total beta** | A beta adjusted for total risk. Formula: Total Beta = Market Beta / Correlation of the sector with the market (the square root of R squared). Bookscape: 0.8558 / 0.5099 = 1.6783, so cost of equity is 2.75% + 1.6783 (5.5%) = 11.98%. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

Module 1 step 11: **Levered beta and total beta**

1. What is the levered beta at the company's current debt-to-equity ratio and marginal tax rate?
2. What would the total beta be if all risk counted, and when would that be the right measure?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| US comparable sample size | 333 firms | Damodaran January 2025 industry betas (`sources/market-data/industry-betas-2025-01-05.json`) |
| Revenue geography | US 64.82%, international 35.18% | FY2024 10-K Note 16 (`sources/filings/swi-10k-fy2024.md`); ledger `country.exposures` |
| Ownership | Silver Lake 36.56%, Thoma Bravo 29.79%, together 66.35%; float about 34% held by diversified institutions | 2024 proxy (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders`, `governance.marginal_investor` |
| Unlevered beta, debt-to-equity, tax rate | 1.22; 0.4933; 25% | Ledger `beta.unlevered_bottom_up`; model-output.md section 1 |
| Levered beta | 1.6714 | model-output.md section 1 |
| Industry correlation with the market | 0.3374 (Damodaran January 2024 industry average) | Course spreadsheet (`01-foundations-and-discount-rates/lesson-10/spreadsheet-totalbeta24.md`); ledger `facts.industry-correlation-software-2024` |
| Risk-free rate and weighted ERP | 4.43%; 4.92% | FRED DGS10; ledger `country.weighted_erp` |
| Cost of equity actually used | 12.65% | model-output.md section 1 |
| Excluded non-US peers | Check Point, TeamViewer, Trend Micro (non-US accounting standards) | Peer facts (`sources/peer-filings/peer-facts-2025-02-05.md`) |

### Steps to complete the assignment

1. Compute the levered beta at the actual debt-to-equity and marginal tax rate: 1.22 x (1 + (1 - 0.25) x 0.4933) = 1.6714.
2. Decide whether a global sample is needed. The US group has 333 firms, so sample size is not the constraint (Damodaran needed global samples for Brazil because of too few firms). SolarWinds' customers buy the same product everywhere, and the 35.18% international revenue enters through the ERP, not the beta. Stay with US firms. A global file was not compiled.
3. Decide whether market beta or total beta is right by asking who the marginal investor is. Diversified institutions holding the roughly 34% float set the price. Silver Lake and Thoma Bravo (66.35% together) are private-equity firms that each own many companies. So ordinary market beta fits.
4. Illustrate total beta, which divides by the correlation with the market (SolarWinds has no R-squared of its own because there is no price history): 1.6714 ÷ 0.3374 = 4.95.
5. Illustrate the cost of equity at that beta: 4.43% + 4.95 x 4.92% = 28.8%, against 12.65% in the model.
6. Do not use it. It mixes a 2024 correlation with 2025 inputs and describes an owner holding nothing else; no SolarWinds owner (sponsors in 2016-2018, public holders, Turn/River) fits that. Any argument for a partial adjustment (two holders with 66.35% could not easily sell) belongs in the control premium in the deal price, not the discount rate.
7. Answer. Levered beta: 1.6714. Total beta: 4.95 on the illustrative 2024 correlation (`beta.total_beta` is in `meta.omitted`); it is right only for an owner who cannot diversify, which describes no SolarWinds owner.

**Result for SolarWinds:** Levered beta 1.6714 from the US sample of 333 firms; total beta would be 4.95 (cost of equity 28.8%) but it is not used, because the marginal investor is diversified.
Full answers: [lesson-11.md](lesson-11.md) · Walkthrough: [Step 11](walkthrough.md#step-11-is-the-market-wide-measure-of-risk-the-right-one-for-solarwinds-and-is-the-sample-big-enough)

## Lesson 12 — Debt: Measure and Cost

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Cost of capital** | The composite cost to the firm of raising financing from both equity and debt. This is the hurdle rate for the whole firm (the weights come in Lesson 13). |
| **Debt** | Anything with a commitment to make fixed, tax-deductible payments, where failing to pay means default or loss of control. Damodaran includes any interest-bearing liability (short or long term) and any lease obligation, operating or capital. |
| **Cost of debt** | What the firm pays to borrow, estimated in the same currency as the cost of equity and the valuation cash flows. |
| **Yield to maturity** | The return a buyer gets on a bond bought today and held to maturity. For a firm with traded bonds, use the yield to maturity on a long-term straight bond (no special features) as the cost of debt. |
| **Bond rating** | A rating agency's judgment of default risk. If the firm is rated, use the rating plus the typical default spread for that rating. |
| **Default spread** | (Re-listed; first defined in Lesson 05 for governments.) Here it is the premium over the riskfree rate that bonds with a given rating pay. A-: 1.30% in November 2013. |
| **Interest coverage ratio** | How easily a firm can pay its interest bills. Formula: Interest coverage ratio = EBIT / Interest expenses. Disney: 10,023 / 444 = 22.57. |
| **Synthetic rating** | A rating estimated from the firm's financials (in its simplest form, only the interest coverage ratio) using a table that maps coverage to rating and spread. Used for unrated firms (Bookscape: A-). |
| **Synthetic versus actual ratings** | Actual ratings use many ratios and qualitative factors, allow for sector effects, use normalized earnings, and reflect country risk (Vale is rated lower for being Brazil-based), so they can differ from synthetic ones. |
| **Pre-tax cost of debt** | Riskfree rate plus default spread. Formula: Pre-tax cost of debt = Riskfree Rate + Default Spread. Bookscape: 2.75% + 1.30% = 4.05%. |
| **After-tax cost of debt** | The cost of debt after the tax deduction on interest. Formula: After-tax cost of debt = Pre-tax cost of debt * (1 - tax rate). Bookscape: 4.05% x (1 - 0.40) = 2.43%. |
| **Differential inflation approach** | (Re-listed; defined in Lesson 11 for cost of equity.) The same conversion applies to the cost of debt: Vale's dollar cost of debt of 4.05% becomes 11.19% in reais. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Credit agreement** | The contract between the company and its lenders: how much it borrowed, the interest rate, when it must repay and the conditions (covenants) it must meet. | Measuring debt and its cost, and judging how much room the company has before lenders can step in. | Filed as an exhibit to a 10-K, 10-Q or 8-K on SEC EDGAR; key terms are summarized in the 10-K debt note. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

Module 1 step 12: **Cost of debt**

1. Does the company have an agency rating? What default spread and pre-tax cost of debt does it imply?
2. What synthetic rating does interest coverage imply, and what cost of debt?
3. If the two differ, why?
4. What is the market value of interest-bearing debt? If the debt is fixed-rate and rates have moved since it was issued, how far is market value from book?
5. What is the debt value of lease commitments, including leases signed but not yet started?
6. Does the company guarantee debt of joint ventures or special-purpose vehicles, or have take-or-pay capacity contracts, that pass the debt test but sit off the balance sheet?
7. How much interest was capitalized into construction, and what does coverage look like once it is added back?
8. Did the company lengthen the depreciation lives of servers or equipment, and how much did that raise operating income?
9. What marginal tax rate applies to the after-tax cost of debt?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Term loan face value | $1,235.7M (SOFR + 2.75%, due 2030-02-05) | FY2024 10-K note 9 (`sources/filings/swi-10k-fy2024.md`); ledger `company.debt_face` |
| Term loan book value | $1,206.6M (after $29.1M of unamortized discount and fees) | FY2024 10-K note 9; ledger `company.debt_book` |
| Lease liabilities | $49.4M | FY2024 10-K note 7; ledger `company.lease_debt` |
| Other items tested | Deferred revenue $389.3M; cloud purchase commitments $68.4M; revolver $130.0M undrawn; no guarantees | FY2024 10-K balance sheet and notes 7, 9, 15; ledger `company.deferred_revenue`, `company.off_balance_sheet_debt` |
| Agency rating | None disclosed | FY2024 10-K and DEFM14C (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `debt.rating_actual` |
| EBIT and interest expense | $208.4M; $112.4M | FY2024 10-K income statement and MD&A; ledger `company.ebit`, `company.interest_expense` |
| Other earnings measures | EBIT + acquisition amortization $261.3M (amortization $52.9M); standardized EBITDA $282.8M | FY2024 10-K; model-output.md section 2 |
| Ratings table | Damodaran January 2025, small firms (market value under $5 billion) | `sources/market-data/ratings-spreads-2025-01-01.json`; ledger `market.ratings_table` |
| Observed loan rate | 7.11% effective rate at year-end 2024 (9.11% at year-end 2023) | FY2024 10-K note 9; ledger `debt.kd_pretax_observed`, `facts.term-loan-rate-2023` |
| Risk-free rate and marginal tax rate | 4.43%; 25% | FRED DGS10; Damodaran January 2025 tax table; ledger `market.tax_rate_marginal` |
| Capitalized interest; depreciation lives | $0.0M; unchanged, 3 to 5 years | FY2024 10-K note 9 and note 2; ledger `company.interest_capitalized`, `company.depreciation_life_change` |

### Steps to complete the assignment

1. Apply the debt test (payments fixed, tax-deductible, missing them can cost the owners control). The term loan passes at face value, $1,235.7M, because lenders are owed the full principal; book value of $1,206.6M is $29.1M lower from an accounting entry. The loan floats with SOFR (secured overnight financing rate), so market value is face.
2. Add leases: $49.4M of operating lease liabilities pass the test. No leases signed but not started.
3. Test the look-alikes. Deferred revenue ($389.3M) is cash received for service owed, so it is not debt. Cloud purchase commitments ($68.4M) are a contract claim, not a default that hands lenders control: ruled out by judgment (adding them would raise debt 5.3% to $1,353.4M). No guarantees; the $130.0M revolver was undrawn.
4. Total debt: $1,235.7M + $49.4M + $0.0M = $1,285.0M.
5. Look for a rating. None is disclosed, so build a synthetic one. Coverage = EBIT ÷ interest expense: $208.4M ÷ $112.4M = 1.85x, rated B-, default spread 4.42%, cost of debt 4.43% + 4.42% = 8.85%. With EBIT plus acquisition amortization ($261.3M): 2.32x, B, 7.43%. With EBITDA ($282.8M): 2.52x, B+, 7.04%. EBIT is chosen because stock compensation of $76.5M is a real cost.
6. Compare to the observed rate. The loan's effective rate is 7.11%, set by lenders with the credit agreement in hand, so it beats the synthetic estimates: use 7.11%. The EBIT-based synthetic rate is 1.74 points higher (8.85% - 7.11%); reasons: lenders price off EBITDA and recurring revenue (93.5% of revenue), the loan is first-lien secured, the table's bands come from a broad sample, and the margin was negotiated.
7. Other adjustments: capitalized interest is zero (coverage stays 1.85x); no change in depreciation lives is disclosed (property and equipment depreciation is only $8.7M of $74.4M).
8. Compute the after-tax cost of debt at the 25% marginal tax rate: 7.11% x (1 - 0.25) = 5.33%.
9. Answer. No agency rating; synthetic rating B- (1.85x, 8.85%), with B / 7.43% and B+ / 7.04% on the other numerators; observed 7.11% used. Debt at market value: $1,235.7M (floating loan), leases $49.4M, total $1,285.0M; after-tax cost of debt 5.33%.

**Result for SolarWinds:** Total debt is $1,285.0M ($1,235.7M term loan at face plus $49.4M leases) at an observed 7.11% pre-tax and 5.33% after tax, versus a synthetic 8.85%.
Full answers: [lesson-12.md](lesson-12.md) · Walkthrough: [Step 12](walkthrough.md#step-12-how-much-does-solarwinds-really-owe-and-what-does-it-pay-to-borrow)

---

# Module 2 — Investment Returns & Financing (lessons 13–19)

## Lesson 13 — Financing Weights

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Weights** | The share of a firm's financing that comes from equity and from debt, used to blend their costs into one cost of capital. Damodaran says these must be based on market values, not book values. |
| **market values** | What the firm's equity and debt are worth at today's prices. Damodaran insists on these for cost-of-capital weights because they reflect what investors would actually pay now. Formula: Equity weight = E / (D + E); Debt weight = D / (D + E). |
| **Book value** | The value of equity or debt as recorded in the accounting statements (historical cost). Damodaran rejects the three common defenses of book weights (more stable, more conservative, consistent with accounting returns); for most firms book weights actually give a lower, misleading cost of capital. |
| **market value of debt** | Debt is often not traded, so most people use book value as a proxy. Damodaran instead treats all the debt as a bond: the PV of the interest payments plus the PV of the principal, discounted at the pre-tax cost of debt over the debt's weighted average maturity (the size-weighted average time until each repayment is due; 7.92 years at Disney). Formula: MV of debt = Interest x [1 - 1/(1+Kd)^n] / Kd + Book value of debt / (1+Kd)^n. |
| **Operating leases** | Long-term lease commitments (such as renting stores or buildings) that Damodaran treats as debt. Their "debt value" is the present value of the future lease payments, discounted at the pre-tax cost of debt, and it is added to both book and market debt. |
| **Cost of Capital** | The blended rate a firm must earn on its investments, weighting the cost of equity and the after-tax cost of debt by market-value weights. Formula: Cost of capital = Cost of equity x E/(D+E) + After-tax cost of debt x D/(D+E). |
| **After-tax cost of debt** | What borrowing really costs once the tax deduction on interest is counted. Formula: (Riskfree rate + Default spread) x (1 - t). |
| **Divisional costs of capital** | A separate cost of capital for each business a firm is in, using that business's own bottom-up beta, debt ratio and cost of debt. Riskier or more debt-light divisions get higher rates (Disney Parks & Resorts 6.61% versus Interactive 8.96%). |
| **Total Beta** | Beta that treats all of a business's risk as relevant (used for an undiversified owner, like Bookscape's), versus Market Beta, which counts only risk that diversified investors cannot eliminate. It gives a much higher cost of equity and cost of capital. |
| **Hurdle rate** | The minimum return an investment must earn to be acceptable. Use the cost of equity if returns are measured to equity investors, and the cost of capital if returns are measured to all capital providers (the firm). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

1. Counting both interest bearing debt and lease commitments, what is the market debt ratio for the firm?
2. What is the levered beta for the firm?
3. If you can allocate debt across different divisions/businesses, what is the debt ratio for each business that the firm is in?
4. What is the levered beta for each division/business?
5. What is the cost of capital of the firm, using market values for weights? How different would it have been, if you had used book values?
6. What are the costs of capital of each of the company's divisions/businesses?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Term loan at face value | $1,235.7M | FY2024 10-K note 9 (`sources/filings/swi-10k-fy2024.md`); ledger `company.debt_face` |
| Operating lease debt | $49.4M | FY2024 10-K note 7; ledger `company.lease_debt` |
| Shares outstanding | 171.6M | Merger information statement (DEFM14C), Written Consent section (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `company.shares_basic` |
| Unaffected share price (2025-02-05 close) | $15.18 | DEFM14C, Opinion of Goldman Sachs; ledger `company.share_price` |
| Book equity | $1,400.7M | FY2024 10-K balance sheet; ledger `company.equity_book` |
| Book debt | $1,206.6M | FY2024 10-K note 9; ledger `company.debt_book` |
| Risk-free rate | 4.43% | 10-year US Treasury close on 2025-02-05, FRED (`sources/market-data/rates-2025-02-05.md`); ledger `market.risk_free_rate` |
| Levered beta and equity risk premium | 1.6714 and 4.92% | Beta from lesson 9, premium from lessons 6–7; Damodaran Jan-2025 data (`sources/market-data/`); model-output.md §1 |
| Pre-tax cost of debt and tax rate | 7.11% and 25% | FY2024 10-K note 9 (`debt.kd_pretax_observed`); Damodaran country tax rates (`market.tax_rate_marginal`) |
| Stock options and restricted stock units (RSUs) | $187.0M | FY2024 10-K note 10; ledger `company.options_value` |
| Segments | One reportable segment | FY2024 10-K note 16 |

### Steps to complete the assignment

1. Build the market-value debt: add the term loan at face and the leases. $1,235.7M + $49.4M = $1,285.0M. Face value is used because the loan floats, so its market value equals its face value.
2. Build the market value of equity: 171.6M shares × $15.18 = $2,604.9M. We used the $15.18 undisturbed price, not the $18.50 deal price, because the deal price includes the buyer's premium.
3. Add them to get firm value: $1,285.0M + $2,604.9M = $3,889.9M. Debt is 33.03% of it and equity 66.97%.
4. Compute the levered beta (risk of the shares, including the effect of debt): 1.22 × (1 + (1 − 0.25) × 0.4933) = 1.6714, where 0.4933 is debt divided by equity.
5. Compute the cost of equity: 4.43% + 1.6714 × 4.92% = 12.65%. Cost of debt after tax is 5.33% (7.11% pre-tax, 25% tax).
6. Blend them into the weighted average cost of capital (WACC): 66.97% × 12.65% + 33.03% × 5.33% = 10.23%.
7. Compare with book weights: book debt share is 47.28% (book equity $1,400.7M against book debt $1,206.6M plus leases $49.4M), giving WACC of 9.19%, which is 1.04 points lower. Book weights lean too far toward cheap debt because the market values equity at 1.86 times book. Leases add only 1.3 points to the 33.03%, but we count them as the course teaches.
8. Judgment calls: the $187.0M of options and RSUs stays out of the weights and is subtracted separately in the valuation. SolarWinds has one segment, so there are no divisional rates and no divisional debt ratios. There is no preferred stock or convertible debt to split.
9. Answers: market debt ratio 33.03%; levered beta 1.6714; one business, so the same 33.03% and 1.6714 for the division; cost of capital 10.23% at market weights versus 9.19% at book weights; 10.23% for the one division.

**Result for SolarWinds:** The market debt ratio is 33.03% (debt $1,285.0M of a $3,889.9M firm), the levered beta is 1.6714, and the cost of capital is 10.23% at market weights against 9.19% at book weights.
Full answers: [lesson-13.md](lesson-13.md) · Walkthrough: [Step 13](walkthrough.md#step-13-what-mix-of-debt-and-equity-funds-solarwinds-and-what-does-the-blend-cost)

## Lesson 14 — Earnings and Cash Flows

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Accrual Accounting** | Accounting that records revenue when a product or service is delivered and expenses when they are incurred, not when cash moves. That is why earnings and cash flows differ. |
| **Operating versus Capital Expenditure** | Only costs that produce this period's revenue are expensed now (operating expenses); costs that create benefits over several periods (capital expenditures) are spread over time as depreciation or amortization. |
| **Time-weighted, Incremental Cash Flow Return** | Damodaran's "Return Mantra" for measuring investment returns correctly: use cash flows (you cannot spend earnings), only the extra cash flows caused by the decision, and give earlier cash more weight than later cash. |
| **Accounting view of return** | The return on a project measured from accounting numbers: after-tax operating income divided by the book value of capital invested (at the start of the year or averaged over the year). It is not time-weighted and is only as good as the book values. |
| **Return on capital (ROC)** | After-tax operating income earned per dollar of capital invested in the business. Formula: ROC = EBIT (1 - t) / (BV of debt + BV of equity - Cash), using the previous year's capital. |
| **Country risk premium** | Extra return demanded for investing in a riskier country. Damodaran adds it to the cost of equity for emerging-market projects (Brazil) because that political risk cannot be fully diversified away. Exchange rate risk is treated as diversifiable and gets no premium. |
| **Assets in place** | The existing investments that generate cash flows today (fixed assets plus working capital), as opposed to growth assets, which are the value expected from future investments. |
| **Return Spread** | The gap between the return a firm earns on its capital and what that capital costs. Positive means value creation. Formula: Return Spread = After-tax ROC - Cost of Capital. |
| **Economic Value Added (EVA)** | The dollar version of the return spread: the excess return times the capital invested. Damodaran calls it "old wine in a new bottle" for the idea that value comes from excess returns. Formula: EVA = (ROC - Cost of Capital) x (Book Value of Capital Invested). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Credit agreement** | The contract between the company and its lenders: how much it borrowed, the interest rate, when it must repay and the conditions (covenants) it must meet. | Measuring debt and its cost, and judging how much room the company has before lenders can step in. | Filed as an exhibit to a 10-K, 10-Q or 8-K on SEC EDGAR; key terms are summarized in the 10-K debt note. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. What return on capital did your firm generate last year?
2. If you have returns on capital over time for your firm, is there a trend in those returns?
3. How do the returns on capital (equity) compare to the costs of capital (equity)?
4. Is there a typical project for this firm? If yes, what does it look like in terms of life (long term or short term), investment needs and cash flow patterns?
5. Are the projects in the future likely to look like the projects in the past? Why or why not?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Operating income (EBIT, earnings before interest and tax) | $208.4M | FY2024 10-K income statement (`sources/filings/swi-10k-fy2024.md`); ledger `company.ebit` |
| Marginal tax rate | 25% | Damodaran country tax rates (`sources/market-data/country-risk-regions-2025-01-01.md`); ledger `market.tax_rate_marginal` |
| Depreciation and amortization (D&A) | $74.4M, of which $52.9M is acquisition amortization | FY2024 10-K cash flow statement; ledger `company.da`, `company.acquisition_amortization` |
| Capital spending | $20.5M | FY2024 10-K cash flow statement; ledger `company.capex` |
| Increase in working capital | $38.8M | FY2024 10-K cash flow statement; ledger `company.change_wc` |
| Invested capital | $2,348.0M | Computed: book equity + book debt - cash (FY2024 10-K balance sheet); ledger `company.invested_capital` |
| Goodwill | $2,363.2M | FY2024 10-K balance sheet; ledger `company.goodwill` |
| Net income and book equity | $111.9M and $1,400.7M | FY2024 10-K income statement and balance sheet |
| Cost of capital and cost of equity | 10.23% and 12.65% | Computed in lesson 13 (model-output.md §1) |
| Three-year history (2022 to 2024) | Invested capital $2,422.9M, $2,356.3M, $2,348.0M | FY2024 10-K statements; ledger `company.history` |

### Steps to complete the assignment

1. Tax the operating income: $208.4M × (1 − 0.25) = $156.3M after-tax operating income.
2. Compute return on invested capital (ROIC): $156.3M ÷ $2,348.0M = 6.66%.
3. Compare with the cost of capital: 6.66% against 10.23% is 3.58 points short. Economic value added (the shortfall times the capital) is -$84.0M (model-output.md §8). SolarWinds does not clear its hurdle.
4. Compute return on equity: $111.9M ÷ $1,400.7M = 7.99%, against a cost of equity of 12.65%, a shortfall of 4.66 points.
5. Test goodwill: goodwill is 100.65% of invested capital. Without it, invested capital is -$15.2M (2,348.0 − 2,363.2), so the return has no meaning. Read 6.66% as a verdict on the 2016 buyout price, not on current operations, which are mostly paid for by customers in advance (deferred revenue of $389.3M).
6. Look at the trend: ROIC was 2.69% in 2022, 4.79% in 2023 and 6.66% in 2024. Invested capital hardly moved, so profit drove the rise. Operating income was -$819.6M in 2022 as reported ($86.8M without $906.4M of non-cash write-downs), then $150.4M in 2023 and $208.4M in 2024.
7. Convert operating profit to cash (free cash flow to the firm): $156.3M + $74.4M − $20.5M − $38.8M = $171.4M. Of the $74.4M gap between EBITDA and operating income, $52.9M is old acquisition cost wearing off. The other $21.5M roughly matches capital spending of $20.5M.
8. Judgment calls: stock compensation of $76.5M is treated as a real cost and not added back. Research and development of $108.6M is left expensed, since capitalizing it changes profit and capital but not cash.
9. Describe the typical project: product development is a small, repeated spend paid back over years of renewals, and acquisitions are large, lumpy and debt-funded, and they built the goodwill. Future projects are mostly the first kind, because the credit agreement restricts acquisitions and management's forecast is organic (revenue from $832.0M in 2025 to $1,273.0M in 2030).
10. Answers: return on capital 6.66%; trend rising from a low base; return on equity 7.99% against 12.65%, and return on capital 6.66% against 10.23%, both below the hurdle.

**Result for SolarWinds:** ROIC was 6.66% against a 10.23% cost of capital (economic value added -$84.0M), and return on equity was 7.99% against 12.65%. Free cash flow to the firm was $171.4M.
Full answers: [lesson-14.md](lesson-14.md) · Walkthrough: [Step 14](walkthrough.md#step-14-did-solarwinds-earn-more-on-its-investments-than-they-cost)

## Lesson 15 — Time Weighting Cash Flows

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Incremental cash flows** | The project's cash flows after adding back non-cash charges like depreciation, subtracting capital expenditures and subtracting the change in non-cash working capital. Costs already sunk and expenses that exist anyway (such as the fixed two-thirds of allocated G&A) are excluded. |
| **Change in non-cash working capital** | The extra money tied up in day-to-day items like inventory and receivables as the project grows. It is a cash outflow that earnings do not show. |
| **discounting** | Bringing a future cash flow back to today's value, because cash received earlier is worth more. Formula: PV = CF / (1 + r)^t. |
| **compounding** | The reverse of discounting: taking a cash flow today forward to its value at a future date. Cash flows at different times cannot be added up until they are moved to the same point in time. |
| **Net Present Value (NPV)** | The sum of the present values of all project cash flows, including the initial investment, discounted at the hurdle rate. It is the dollar value the project adds to the firm. Decision rule: accept if NPV > 0. |
| **Internal Rate of Return (IRR)** | The discount rate that makes the NPV equal zero; the percentage return on the incremental, time-weighted cash flows. Decision rule: accept if IRR > hurdle rate. |
| **IRR versus NPV differences** | They usually agree but can rank projects differently. A project can have only one NPV but more than one IRR; NPV is a dollar number that favors big projects while IRR is a percentage that favors small ones; NPV assumes cash flows are reinvested at the hurdle rate while IRR assumes reinvestment at the IRR itself. |
| **Salvage value** | For a finite, short-lived project, the expected proceeds from selling off the investment at the end of its life, usually set equal to the book value of fixed assets and working capital. |
| **Terminal value** | For a very long-lived project, the present value at the end of the forecast period of all cash flows after it. Formula: Terminal value in year n = CF in year n+1 / (Cost of Capital - Growth Rate). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

1. If you can identify a typical project for your firm, what pattern of cash flows do you foresee for the project?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Goodwill (sunk cost) | $2,363.2M | FY2024 10-K balance sheet (`sources/filings/swi-10k-fy2024.md`); ledger `company.goodwill` |
| 2022 goodwill write-off already taken | $891.1M | FY2024 10-K; ledger `company.history` (2022 note) |
| Deferred revenue | $389.3M | FY2024 10-K balance sheet; ledger `company.deferred_revenue` |
| R&D expense, capital spending, revenue | $108.6M, $20.5M, $796.9M | FY2024 10-K income and cash flow statements; ledger `company.rd_expense`, `company.capex`, `company.revenue` |
| General and administrative expense, segments | $125.8M; one segment | FY2024 10-K income statement and note 16 |
| Risk-free rate | 4.43% | FRED, 10-year Treasury close 2025-02-05; ledger `market.risk_free_rate` |
| Banks' terminal growth ranges | Goldman Sachs 2% to 3%; Jefferies 2.5% to 3.5% | DEFM14C, fairness opinions (`sources/deal-docs/swi-defm14c-2025-merger.md`) |
| Management revenue forecast | $796.9M (2024) to $1,273.0M (2030), 8.12% a year | DEFM14C management forecasts; ledger `forecast.management_growth` |
| 2030 free cash flow and operating income | $419.0M and $511.0M | DEFM14C management forecasts; ledger `forecast.years` |
| Terminal values under two methods | $5,552.5M and $3,808.9M | Computed, model-output.md §6 |

### Steps to complete the assignment

1. Define the typical project. SolarWinds sells subscriptions and maintenance contracts that renew, so a project is one customer contract or one bought product, not a plant.
2. Remove sunk costs (money already spent that nothing can recover). The $2,363.2M of goodwill is sunk, and $891.1M of it was already written off in 2022. Neither changes what a new project costs or earns.
3. Decide on overhead. SolarWinds reports one segment, so the $125.8M of general and administrative expense is not allocated to products. Ask "what happens if I take the project and what happens if I don't?" Only sales, support and hosting costs that rise with a project count.
4. Map the cash pattern. Customers pay annually or multi-annually in advance (deferred revenue $389.3M), so cash arrives before revenue is recognized. The platform investment is thin: R&D of $108.6M and capital spending of $20.5M on revenue of $796.9M. Value depends on renewal, not on a payback period.
5. Set the terminal growth limit. A company cannot grow forever faster than the economy, and the 4.43% risk-free rate is the proxy. We chose 2.5%, the midpoint of Goldman's 2% to 3% and the low end of Jefferies' 2.5% to 3.5%. That is a judgment, and it is well below 4.43%.
6. Check the explicit forecast: revenue growth of 8.12% a year is above the risk-free rate, but it lasts six years only.
7. Check the cash flow that gets grown. Management's 2030 free cash flow is $419.0M, above after-tax operating income of $511.0M × (1 − 25%) = $383.3M. Growing it forever assumes no reinvestment, giving a terminal value of $5,552.5M. With reinvestment the terminal value is $3,808.9M, the version the model uses (decided in lesson 32).
8. Answer: the typical project's cash flow has three phases, the first invoice (cash in), ratable recognition over the term, and renewal. The acquisition version is the opposite, a large outlay up front followed by cash flows that must earn the 10.23% cost of capital to avoid an impairment.

**Result for SolarWinds:** The typical project is a subscription customer, cash-positive from the first invoice, with goodwill ($2,363.2M) treated as sunk. Terminal growth of 2.5% is defensible against a 4.43% risk-free rate, and the real risk is the terminal cash flow ($5,552.5M versus $3,808.9M terminal value).
Full answers: [lesson-15.md](lesson-15.md) · Walkthrough: [Step 15](walkthrough.md#step-15-what-does-a-typical-solarwinds-project-look-like-in-cash-and-what-growth-rate-can-it-assume-forever)

## Lesson 16 — Loose Ends

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **$R NPV** | Analyzing the project in dollars or in Brazilian Reais should give the same NPV, as long as the discount rate and cash flows are in the same currency. Formula: Reais cost of capital = (1 + $ cost of capital) x (1 + Reais inflation) / (1 + $ inflation) - 1. |
| **Payback** | The number of years needed to recover the money invested, ignoring what happens afterward and the time value of money. A crude measure for investors afraid of losing their investment (Rio Disney 10.3 years). |
| **Discounted Payback** | Payback computed on present-valued cash flows, so it accounts for the time value of money and is longer (Rio Disney 16.8 years). |
| **Sensitivity Analysis** | Checking how much NPV or IRR changes when you change one key assumption. Damodaran's cautions: variables usually move together in real life, and the goal is better decisions, not more tables ("less is more"). |
| **What-if** | Asking how a decision measure responds to a change in an input, such as revenues falling short or costs rising. It is the basic question behind sensitivity analysis. |
| **Probabilistic estimates** | Using ranges and probability distributions for inputs rather than a single expected value. |
| **Simulation** | Running thousands of trials that draw each uncertain input from its distribution, producing a distribution of NPVs rather than one number (Rio Disney: NPV from -$1 billion to +$8.5 billion, negative 12% of the time). |
| **Hedging** | Reducing a risk, such as exchange rate risk, with offsetting positions. The slide poses whether to do it as an open question; the lesson's task asks which risks, if any, to hedge. |
| **opportunity costs** | The side costs of a project from using resources the business already owns, plus lost revenue on other projects. They must be included in the project's return. |
| **synergies** | Side benefits where a project's cash flows boost other projects, not captured in a standard capital-budgeting analysis. |
| **options embedded in projects** | The flexibility to delay, expand or abandon a project, which has value that traditional analysis misses. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

1. If your firm has foreign operations, what currency are the operations reported in?
2. What cost of equity/capital would you use for the foreign operations, given currency choice and business?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Reporting currency | US dollars | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `meta.currency` |
| Revenue by geography | International 35.18% ($280.336M of $796.895M), US 64.82% | FY2024 10-K note 16; ledger `country.exposures` |
| Currencies sold in, hedging policy | Euros, pounds, Australian dollars; no interest rate swaps; limited currency hedging | FY2024 10-K Item 7A and Item 1A |
| Risk-free rate | 4.43% | FRED, 10-year Treasury close 2025-02-05; ledger `market.risk_free_rate` |
| Equity risk premium by region | US 4.27%, international 6.11% (4.27% + 1.84% Europe, Middle East and Africa), blend 4.92% | Damodaran Jan-2025 country risk data (`sources/market-data/`); ledger `country.weighted_erp` |
| Unlevered beta | 1.22 | Damodaran Jan-2025 industry betas, Software (System & Application) (`sources/market-data/industry-betas-2025-01-05.json`); ledger `beta.unlevered_bottom_up` |
| Interest-rate sensitivity | About $12.4M a year per 1 point; interest expense $112.4M | FY2024 10-K Item 7A and MD&A |
| Cyber and D&O insurance limits | $15M cyber, $50M directors-and-officers (D&O) | FY2024 10-K Note 15 |
| Net cyber-incident costs | $26.2M (2022), $2.1M recovery (2023), $10.3M (2024) | FY2024 10-K MD&A non-GAAP reconciliation |
| Maintenance renewal rate | 94% (2019), 91% (2020), 93% (2022), 96% (2023), 97% (2024) | 10-K filings (`sources/filings/`) |

### Steps to complete the assignment

1. Pick the currency. SolarWinds reports in US dollars, though its European subsidiaries first keep books in euros. International revenue is 35.18% of the total.
2. Apply the consistency rule: cash flows and discount rate must be in the same currency. A euro rate would equal (1 + dollar rate) × (1 + euro inflation) ÷ (1 + dollar inflation) − 1. No euro inflation forecast is in the sources, so we stay in dollars and avoid adding an assumption.
3. Choose the discount rate for foreign operations. The business is the same product in every country, so the 1.22 unlevered beta does not change by geography. Foreign risk goes into the equity risk premium: 64.82% × 4.27% + 35.18% × 6.11% = 4.92%. The result is the same dollar cost of capital, 10.23%.
4. Note the judgment on the 6.11%: it applies the Europe, Middle East and Africa premium to all international revenue, since most international offices are in Europe. Western Europe alone would add 1.12% and the global average 1.43%, so 4.92% could be a little high.
5. Test the hedging. Interest rates are not hedged: a 1-point rise adds about $12.4M of interest against $112.4M of expense and $208.4M of operating income, small enough to leave open. Currency is hedged only a little, and investors can diversify it themselves, so a big corporate hedge is hard to justify.
6. Test insurance. Cyber cover of $15M was small against costs of tens of millions, but the $26M class-action settlement was repaid fully by D&O insurance. The SEC lawsuit is carried unhedged.
7. Check the benefit evidence: the maintenance renewal rate fell from 94% to 91% after the 2020 attack and was 97% in 2024. Security spending was never disclosed, so the cost side cannot be measured.
8. Answers: operations are reported in US dollars; the cost of capital for foreign operations is the same 10.23%. For illustration only, a project wholly in Europe would have a cost of equity of 14.64% and a cost of capital of about 11.57% (not used).

**Result for SolarWinds:** Everything is valued in US dollars at one cost of capital, 10.23%, with foreign risk carried in the 4.92% equity risk premium. Open interest-rate and currency exposures are small against $208.4M of operating income.
Full answers: [lesson-16.md](lesson-16.md) · Walkthrough: [Step 16](walkthrough.md#step-16-in-what-currency-does-solarwinds-operate-and-does-a-foreign-dollar-deserve-a-different-discount-rate)

## Lesson 17 — The Trade Off

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Debt to Capital Ratio** | The share of a firm's total financing that is debt, using market values and counting all debt. Formula: Debt to Capital Ratio = Debt / (Debt + Equity). |
| **Tax Benefits** | The tax code favors debt because interest is tax deductible while dividends to equity are not, but you need enough income to use the deduction. Formula: Tax benefit each year = Tax Rate x Interest Payment. |
| **Proposition 1** | Other things equal, the higher a business's marginal tax rate, the more debt it will have in its capital structure. |
| **Adds discipline to management** | Debt forces managers to earn at least enough on projects to cover interest or risk bankruptcy and losing their jobs, which cures the complacency of cash-rich, debt-free firms. |
| **Bankruptcy Costs** | Expected bankruptcy cost = the probability of bankruptcy times the cost of going bankrupt. Direct costs are legal and other deadweight costs; indirect costs come from customers and suppliers perceiving you to be in trouble. |
| **Propositions 2 and 3** | More volatile earnings mean a higher chance of bankruptcy at any debt level (2); the larger the indirect bankruptcy cost, the less debt a firm can afford (3). |
| **Agency Costs** | The friction and cost from stockholders and lenders wanting different things: stockholders may take riskier projects or pay big dividends, while lenders want their money back. Proposition 4: the greater the agency problems, the less debt the firm can use. |
| **Loss of Future Flexibility** | Borrowing to the limit today leaves no debt capacity for unexpected opportunities or shortfalls later. Proposition 5: the more uncertain a firm's future financing needs, the less debt it will use now. |
| **debt capacity** | How much more a firm can borrow before costs outweigh benefits. It is used up as a firm borrows. |
| **Miller-Modigliani Theorem** | In a world with no taxes, default risk or agency costs, capital structure is irrelevant: firm value depends only on project cash flows and the cost of capital does not change with leverage, since the cost of equity rises just enough to offset cheaper debt. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **S-1 (IPO prospectus)** | The registration statement a company files to sell shares to the public for the first time: its history, finances, risks, owners and what it will do with the money raised. | Understanding how a company was owned and financed before it listed, and what investors were told at the IPO. | SEC EDGAR (filing type S-1, or 424B4 for the final prospectus). |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. What are the different kinds or types of financing that this company has used to raise funds? Where do they fall in the continuum between debt and equity?
2. How large, in qualitative or quantitative terms, are the advantages to this company from using debt? How large, in qualitative or quantitative terms, are the disadvantages to this company from using debt? From the qualitative trade off, does this firm look like it has too much or too little debt?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Funding instruments | Leases $49.4M; term loan $1,235.7M face; revolver $130.0M undrawn; deferred revenue $389.3M; options and RSUs $187.0M | FY2024 10-K notes 7, 9, 10 and balance sheet (`sources/filings/swi-10k-fy2024.md`); ledger `company.*`, `debt.revolver_undrawn` |
| Debt history | $2,358.1M (2017, incl. $680.0M second lien); $1,970.1M (2018); $1,319.2M (2022); $1,300.4M (2023); $1,285.0M (2024) | FY2018 10-K (`sources/filings/swi-10k-fy2018.md`); FY2024 10-K; ledger `company.history` |
| IPO | $375.0M raised at $15.00 a share, October 2018 | FY2018 10-K / IPO prospectus (`sources/filings/swi-s1-2018-ipo-prospectus.md`) |
| Interest expense and tax rate | $112.4M and 25% | FY2024 10-K MD&A; Damodaran country tax rates |
| Cash taxes, cash interest, operating cash flow | $61.5M, $104.5M, $188.3M | FY2024 10-K cash flow statement |
| Covenant and revolver | 7.40 to 1 first-lien net leverage test, active only if more than 35% of the revolver is drawn | FY2024 10-K note 9; ledger `debt.covenants` |
| Debt ratios now and for peers | 33.03% market, 47.28% book; eight peers 0.88% to 45.28%, median 11.7% | Computed in lesson 13 (model-output.md §1); peer filings (`sources/peer-filings/peer-facts-2025-02-05.md`); ledger `peers` |
| Interest coverage | 1.85x, synthetic B- | Computed, model-output.md §2 |
| Turn/River closing debt | $2.225 billion first lien, $200.0M revolver, $525.0M second lien | DEFM14C and closing 8-K (`sources/deal-docs/`) |

### Steps to complete the assignment

1. List the funding types from most debt-like to most equity-like: leases ($49.4M), first-lien term loan ($1,235.7M), undrawn revolver ($130.0M), the second-lien loan (gone by end of 2018), then deferred revenue ($389.3M, neither debt nor equity), options and RSUs ($187.0M), and common stock from the 2018 IPO. There are no convertibles and no preferred shares, so the company uses both ends and never the middle.
2. Place SolarWinds in its life cycle. Revenue grew 5.0% in 2024 ($758.7M to $796.9M), 93.5% of revenue is recurring, and EBIT is $208.4M. That is a mature company, which can carry debt.
3. Read the debt history. After the 2016 buyout, debt was $2,358.1M at the end of 2017 against a book equity deficit of $729.8M. The IPO repaid $315.0M of the second lien, and debt then fell to $1,285.0M by 2024. The leverage is a legacy of the buyout being managed down, not a chosen target.
4. Compare with peers: 33.03% against a peer median of 11.7%. Only Open Text (45.28%) and Progress Software (38.46%) carry more.
5. Size the benefit of debt: interest of $112.4M × 25% = $28.1M a year of tax saved, and it is usable because cash taxes were $61.5M. Capitalized at 7.11%, that is about $395M (rough). The discipline benefit is small.
6. Size the costs: coverage is 1.85x (B-), and cash interest of $104.5M is 55.5% of operating cash flow of $188.3M. Each 1-point rate rise adds about $12.4M. A sale triggers default, so the loan had to be refinanced. There was no near-term default risk, since the covenant applies only if more than 35% of the revolver is drawn and the revolver was undrawn.
7. Judgment: the weighing leans to somewhat too much debt, and lesson 18 tests it with numbers (optimum 21% against 33.03%).
8. Answers: financing types as listed above; advantages are a $28.1M a year tax shield and little else; disadvantages are interest consuming 55.5% of operating cash flow, 1.85x coverage, rate exposure and refinancing on a sale. SolarWinds has somewhat too much debt.

**Result for SolarWinds:** Debt is a leftover of the 2016 buyout, down from $2,358.1M (2017) to $1,285.0M, and now 33.03% of firm value against a peer median of 11.7%. The tax shield is $28.1M a year, but interest takes 55.5% of operating cash flow, so the company carries somewhat too much debt.
Full answers: [lesson-17.md](lesson-17.md) · Walkthrough: [Step 17](walkthrough.md#step-17-how-has-solarwinds-paid-for-itself-and-is-debt-helping-or-hurting)

## Lesson 18 — The Cost of Capital: Approach

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Cost of Capital Approach** | Firm value is the PV of cash flows to the firm discounted at the cost of capital, so with cash flows held constant, the debt mix that minimizes the cost of capital maximizes firm value. |
| **U-shaped cost of capital graph** | Cost of capital falls at first as cheap, tax-advantaged debt is added, then rises as costs of equity and debt climb with default risk. The bottom of the U is the optimal debt ratio. |
| **Cost of capital schedule** | The table of beta, cost of equity, after-tax cost of debt and cost of capital at each debt ratio from 0% to 90%. Disney's minimum is 7.16% at 40% debt. |
| **Unlevered beta** | The beta of a business before any debt. Damodaran gets it by unlevering the regression beta or, better, by combining the unlevered betas of the firm's businesses weighted by value. Formula: Unlevered beta = Levered beta / [1 + (1 - t)(D/E)]. |
| **Levered beta** | The beta of equity once debt is added; it rises with the D/E ratio, which pushes up the cost of equity. Formula: Levered Beta = Unlevered beta x (1 + (1 - t)(D/E)). |
| **D/E ratio** | Debt divided by equity, the form that goes into the levered beta formula. Convert from debt to capital: D/E = (D/(D+E)) / (1 - D/(D+E)), so 10% debt to capital is D/E of 11.11%. |
| **Interest coverage ratio** | How many times operating income covers the interest bill; Damodaran uses it to estimate a bond rating at each debt level. Formula: Interest coverage ratio = EBIT / Interest expense. |
| **Ratings table** | A lookup table mapping interest coverage ranges to a likely bond rating, default spread and interest rate for a firm of a given size. Pre-tax cost of debt = riskless rate + spread. |
| **Iteration** | Interest depends on the rating, and the rating on interest, so you recompute the cost of debt at the new rating until it stops changing (the 30% debt test moves from AAA to AA rates). |
| **Stated versus effective tax rates** | Interest is only tax deductible up to your operating income. When interest exceeds EBIT, the effective rate falls. Formula: Adjusted marginal tax rate = (EBIT x Marginal tax rate) / Interest expense. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

1. What is your firm's current debt ratio (and cost of capital)?
2. Based upon the cost of capital approach, what is the optimal debt ratio for your firm?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Debt and equity (market) | $1,285.0M and $2,604.9M | Computed in lesson 13 (model-output.md §1); ledger `company.debt_total`, `company.equity_value` |
| Operating income (EBIT) | $208.4M | FY2024 10-K income statement (`sources/filings/swi-10k-fy2024.md`); ledger `company.ebit` |
| Interest expense | $112.4M | FY2024 10-K MD&A; ledger `company.interest_expense` |
| Unlevered beta | 1.22 | Damodaran Jan-2025 industry betas (`sources/market-data/industry-betas-2025-01-05.json`); ledger `beta.unlevered_bottom_up` |
| Risk-free rate and equity risk premium | 4.43% and 4.92% | FRED 2025-02-05 (`market.risk_free_rate`); Damodaran Jan-2025 country data (`country.weighted_erp`) |
| Tax rate | 25% | Damodaran country tax rates; ledger `market.tax_rate_marginal` |
| Ratings and spreads table (small firms) | Interest coverage to rating to interest rate | Damodaran Jan-2025 ratings table (`sources/market-data/ratings-spreads-2025-01-01.json`); ledger `modeling_choices.firm_size_table` (market value of $2.6B is under his $5B line) |
| Alternative coverage numerators | Standardized EBITDA $282.8M; acquisition amortization $52.9M; adjusted EBITDA $384.7M | FY2024 10-K MD&A non-GAAP reconciliation; ledger `company.ebitda_standardized`, `company.acquisition_amortization` |
| Cost-of-capital schedule | 0% to 70% debt | Computed, model-output.md §3 |

### Steps to complete the assignment

1. Compute the current position: debt $1,285.0M ÷ firm value $3,889.9M = 33.03%. Cost of equity is 12.65%, after-tax cost of debt 5.33%, and cost of capital 10.23% (model-output.md §1). At book weights the ratio is 47.28% and the cost of capital 9.19%, for comparison only.
2. Set up a schedule of debt ratios from 0% to 70%. At each ratio, re-lever the beta (more debt makes shares riskier), compute interest coverage (EBIT ÷ interest), and look up the synthetic rating and interest rate from the ratings table.
3. Repeat the loop at each ratio, because the new interest changes coverage, which can change the rating, until the rating stops changing.
4. Compute the cost of capital at each ratio: equity share × cost of equity + debt share × after-tax cost of debt. Cost is 10.43% at 0% debt, 10.22% at 10%, 10.05% at 20%, 10.03% at 21% (the minimum, A- rating), 10.24% at 30% (B+, debt at 7.04%), 10.31% at 33%, 10.72% at 40% (B-, debt at 8.85%) and 16.44% at 50% (C, debt at 19.93%).
5. Read the curve: shallow on the low side, steep past 30%, and a cliff beyond 40%. Being at 33% costs only about 0.28 points more than the optimum (10.31% − 10.03%), but the slope steepens quickly.
6. Reconcile 10.23% and 10.31%: the first uses the observed 7.11% rate on the loan, while the schedule reprices all debt at the synthetic B rate of 7.43%. This is a method difference, not an error.
7. Judgment on the coverage measure: we used EBIT (coverage 1.85x, B-). EBITDA of $282.8M is rejected because non-acquisition depreciation of $21.5M roughly equals capital spending of $20.5M, so it is not free cash. The company's adjusted EBITDA of $384.7M is rejected because it adds back stock compensation. Adding back only acquisition amortization gives an optimum of 26%, and EBITDA gives 28%. Because "better under-levered than over-levered", the low end is the better guide.
8. Answers: current debt ratio 33.03% and cost of capital 10.23%; the optimal debt ratio is 21%, with a cost of capital of 10.03%, $468.1M less debt than today.

**Result for SolarWinds:** The cost of capital bottoms at 10.03% with 21% debt (A- rating), against 33.03% debt and 10.23% today. The optimum is 26% or 28% under looser coverage measures, and all put SolarWinds above its optimum.
Full answers: [lesson-18.md](lesson-18.md) · Walkthrough: [Step 18](walkthrough.md#step-18-how-much-debt-would-make-solarwinds-cost-of-capital-lowest)

## Lesson 19 — The Cost of Capital: Follow Up

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **optimal debt ratio** | The debt level where the cost of capital is lowest and firm value highest (Disney: 40%). It depends on the riskiness of the business and the tax rate. |
| **excess debt capacity** | The additional borrowing available to reach the optimal: optimal dollar debt less current debt (Disney: $55.1 billion less $15.96 billion = about $39.14 billion). The slides then have Disney borrow it and buy back stock. |
| **Free cash flow to the firm** | Cash left for all capital providers after tax, reinvestment and working capital. Formula: EBIT (1 - Tax Rate) + Depreciation and amortization - Capital expenditures - Change in noncash working capital. |
| **Implied growth rate** | The perpetual growth rate that, with the current cost of capital, makes the cash flows worth today's market value. Formula: g = (Firm Value x Cost of Capital - CF to Firm) / (Firm Value + CF to Firm). |
| **Full valuation** | Measuring the gain from recapitalizing by revaluing the whole firm at the new cost of capital. Formula: Firm value = FCFF0 (1+g) / (Cost of Capital - g). |
| **Incremental approach** | Measuring the gain as the present value of the annual savings in financing cost. Formula: Increase in value = Annual savings next year / (Cost of Capital - g). |
| **Rational investor solution** | The increase in firm value goes to stockholders and is spread evenly across everyone, so value per share rises by the gain divided by shares outstanding (Disney: $19,623M / 1,800M = $10.90). Sellers and holders end up indifferent. |
| **buyback price** | The price at which the firm repurchases shares to fund the recapitalization. Shares after buyback = shares before - debt issued / buyback price; value per share after = equity value after buyback / shares after buyback. |
| **Downside risk** | What happens to the optimal debt ratio if operating income drops. Two methods: a statistical approach (cut base income by one standard deviation or more) and an economic scenario approach (apply the decline seen in the last recession). |
| **Ratings constraint** | A management cap on how far the bond rating may fall. It protects against downside risk and so should not be combined with that analysis, and each constraint has a cost. |
| **Cost of the rating constraint** | Value at the unconstrained optimal minus value at the constrained debt ratio (Disney: $5,696M for AA, $12,125M for AAA). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |

### What the project asked

1. If you move to the optimal debt ratio (given the cost of capital) approach, what consequences do you see for the value of your firm and the value of equity in the firm?
2. Bringing in reasonable constraints into the cost of capital approach, what would your recommended debt ratio be for this firm?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Cost of capital at current and optimal debt | 10.31% and 10.03% | Computed in lesson 18, model-output.md §3 |
| Firm value | $3,889.9M | Computed in lesson 13, model-output.md §1 |
| Terminal growth | 2.5% | Judgment from the banks' ranges in DEFM14C (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `market.terminal_growth` |
| Basic shares | 171.6M | DEFM14C, Written Consent section; ledger `company.shares_basic` |
| DCF values at status quo and at optimal cost of capital | Enterprise value $3,444.3M and $3,533.4M; $13.00 and $13.52 a share | Computed, model-output.md §6 |
| Adjusted present value (APV) gain | $220.3M | Computed, model-output.md §9 |
| Stress test of EBIT | Optimum 21%, 19% (EBIT $187.6M), 16% ($166.7M), 14% ($145.9M) | Computed, model-output.md §4 |
| Covenant and revolver | 7.40 to 1 first-lien net leverage test; $130.0M revolver undrawn | FY2024 10-K note 9 (`sources/filings/swi-10k-fy2024.md`); ledger `debt.covenants`, `debt.revolver_undrawn` |
| Cash, first-lien debt, standardized EBITDA | $259.3M, $1,235.7M, $282.8M | FY2024 10-K balance sheet, note 9 and MD&A; ledger `company.cash`, `company.debt_face`, `company.ebitda_standardized` |
| EBIT history | $150.4M (2023), $208.4M (2024) | FY2024 10-K income statement; ledger `company.history` |

### Steps to complete the assignment

1. Compute the annual saving from moving to 21% debt: the cost of capital falls from 10.31% to 10.03% on a firm value of $3,889.9M, saving $10.9M a year (model-output.md §3). Debt falls by $468.1M.
2. Capitalize the saving as a growing perpetuity (a payment growing forever at a steady rate): saving ÷ (cost of capital − growth), at 2.5% growth. The value of moving is $144.4M, or $0.84 a share on 171.6M shares.
3. Cross-check with the discounted cash flow (DCF) valuation rerun at the lower rate: enterprise value rises from $3,444.3M to $3,533.4M ($89.1M) and the value per share from $13.00 to $13.52 ($0.52). APV gives $220.3M ($1.28 a share). These are three measures on different bases, so $0.52 to $1.28 is the range, with the DCF as the working number.
4. Identify who captures it. SolarWinds is over-levered, so it would cut debt by $468.1M, not buy back shares. Lenders are repaid at face, so the gain goes to shareholders. The equity value rises by the full gain, since the retired debt is replaced by equity (about 18% of $2,604.9M market equity).
5. Stress-test the optimum by cutting EBIT: it moves to 19% (down 10%), 16% (down 20%) and 14% (down 30%). SolarWinds' own EBIT in 2023 was 27.8% lower than in 2024 ($208.4M to $150.4M), between the 20% and 30% rows.
6. Check the covenant: net first-lien debt of $1,235.7M less $259.3M cash is $976.4M, which is 3.45 times standardized EBITDA of $282.8M against the 7.40 limit, and the test applies only if more than 35% of the revolver ($45.5M) is drawn. The covenant does not bind. Today's rating is B- on actual interest, and the schedule says to stay at or below about 20% to stay out of the B range.
7. Judgment: recommend about 15% debt, a cushion below the 21% optimum justified by the stress test, not a rival optimum. This costs about 0.1 points of cost of capital (10.22% at 10% debt, 10.05% at 20%). 15% of $3,889.9M is $583.5M of debt, so $701.5M would have to be repaid, which cash of $259.3M does not cover alone.
8. Answers: moving to the optimum gains $144.4M (perpetuity) or $0.52 to $1.28 a share (DCF to APV), small against the $13.00 DCF value, so capital structure does not decide the valuation. Recommended debt ratio is about 15%.

**Result for SolarWinds:** Moving to 21% debt saves $10.9M a year, worth $144.4M, or $0.52 to $1.28 a share on three measures. With the stress test, we recommend about 15% debt as a cushion.
Full answers: [lesson-19.md](lesson-19.md) · Walkthrough: [Step 19](walkthrough.md#step-19-what-is-moving-to-the-best-debt-level-worth-and-how-far-should-the-company-really-go)

---

# Module 3 — Financing Mix & Dividends (lessons 20–26)

## Lesson 20 — The Cost of Capital: Wrap Up

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Enhanced cost of capital approach** | The cost of capital method for finding the best debt ratio, upgraded so that the hidden costs of distress are built into the firm's expected operating income. As the credit rating falls, operating income is cut to reflect customers, suppliers and investors pulling back. |
| **Indirect bankruptcy costs** | The damage a risky firm suffers before it ever files for bankruptcy, because customers, suppliers and investors lose confidence and business shrinks. In the enhanced approach this shows up as a drop in EBITDA (operating earnings before depreciation and amortization) that gets bigger as the rating gets worse. |
| **Distress effect (drop in EBITDA by rating)** | A lookup table of how much operating income is assumed to fall at each lower rating, in low, medium and high scenarios (for Disney, from no effect at A to a 30%-100% drop at D). It is what makes the value "cliff" steeper at high debt ratios. |
| **Dynamic analysis** | Instead of using one operating income number, you draw from a distribution of possible operating incomes so the optimal debt ratio reflects different outcomes. |
| **Family group company** | A firm that belongs to a group of related companies (Tata Motors in the Tata Group) and may lean on the group's debt capacity. Its actual debt can exceed its stand-alone optimal; Tata Motors was 29% actual versus 20% optimal. |
| **Volatile earnings (normalized operating income)** | For cyclical or commodity firms, replace current operating income with an average over several years (Vale: three-year average) before running the analysis. Doing so raised Vale's optimal debt ratio to 50%, because today's number is not a fair picture of typical earnings. |
| **Private business optimal debt ratio** | For a firm with no traded stock (Bookscape), estimate equity value as net income times the average PE of publicly traded comparables, and count leases as debt. Then run the same cost of capital table. Formula: Debt ratio = Debt / (Debt + Estimated market value of equity). |
| **Bank capital structure (regulatory capital approach)** | For banks, the equity needed is set by a regulatory capital ratio (equity as a percent of loans), not by a WACC search. Formula: New equity needed = Target equity ratio x Loans after expansion - Existing equity. Need for external equity rises with growth and under-capitalization, and falls with higher earnings. |
| **Marginal tax rate (determinant of optimal debt)** | The primary benefit of debt is the tax deduction, so the higher the marginal tax rate, the higher the optimal debt ratio. |
| **Pre-tax cash flow return (EBITDA/EV, EBIT/EV)** | Operating earnings as a percent of enterprise value (EV, the value of the whole business including debt). Firms with higher pre-tax cash flow return can support more debt, so they tend to have higher optimal debt ratios. |
| **Operating risk (determinant of optimal debt)** | Firms with more variable operating income have lower optimal debt ratios. It enters the cost of capital in two places: a higher unlevered beta (business risk before debt) and lower bond ratings for a given income. |
| **Equity vs debt risk premiums** | The only macro determinant of optimal debt ratio. The relative price of equity risk versus debt risk in the market shifts how attractive borrowing is. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. If your company is a commodity or cyclical company, how would you adjust your optimal debt ratio to reflect earnings volatility?
2. If your company is part of a family group, what other considerations might come into play in determining your optimal debt ratio?
3. If your company is privately owned, how would your optimal debt ratio be computed differently?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Customers hit by the December 2020 SUNBURST attack (hackers inserted malicious code into the Orion software) | About 33,000 told; fewer than 18,000 with the bad software; over 300,000 customers overall | 8-K of 2020-12-14 (`sources/filings/swi-8k-2020-12-14-sunburst-followup.md`) |
| Maintenance renewal rate | 94% (2019), 91% (2020), 93% (2022), 96% (2023), 97% (2024) | 10-Ks FY2020, FY2023, FY2024 (`sources/filings/`); ledger `facts.maintenance-renewal-rate` |
| Revenue history | $669.1M (2019), $716.8M (2020), $718.6M (2021), $719.4M (2022), $758.7M (2023), $796.9M (2024) | 10-Ks (`sources/filings/`); ledger `company.history` |
| Operating income (EBIT, earnings before interest and tax) | $208.4M (2024); $150.4M (2023); loss of $819.6M (2022, includes an $891.1M goodwill write-down) | FY2024 and FY2023 10-Ks; ledger `company.ebit`, `company.history` |
| Enterprise value (EV: share value plus debt minus cash) | $3,630.6M | model-output.md §7 |
| Eight peers' EBIT as a share of EV and debt ratios | Median EBIT/EV 4.29%; debt 0.88% to 45.28% of value; peer median debt ratio 11.7% | Peer filings and 2025-02-05 prices (`sources/peer-filings/peer-facts-2025-02-05.md`); ledger `peers` |
| Unlevered beta (business risk) and marginal tax rate | 1.22; 25% | Damodaran Jan-2025 industry betas and tax table (`sources/market-data/`); ledger `beta.unlevered_bottom_up`, `market.tax_rate_marginal` |
| Cost of debt and equity at 33% and 21% debt | 7.43% and 12.65% at 33%; 5.38% and 11.63% at 21% | model-output.md §1, §3 |
| Owners | Silver Lake 36.56%, Thoma Bravo 29.79% | 2024 proxy (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders` |
| Financing at the 2025 sale | $2.225 billion first-lien loan, $200.0M revolver, $525.0M second-lien loan | Merger documents (`sources/deal-docs/`); ledger `facts.new-debt-2025` |

### Steps to complete the assignment

1. Pick a past shock to test whether a lower credit rating would cost operating income. We used SUNBURST in 2020, which hurt reputation more than a downgrade would.
2. Measure customer reaction. About 33,000 customers were told, fewer than 18,000 had the compromised software, out of more than 300,000. The renewal rate slipped from 94% to 91%, then recovered to 97% by 2024.
3. Measure revenue reaction. Revenue stayed flat at $716.8M, $718.6M and $719.4M for two years, then grew to $758.7M and $796.9M. Judgment: the indirect cost of distress is small, so we assume about 5% of operating income is lost in a one- or two-notch downgrade. This is not in the filings. Supplier terms add nothing: the only commitment is $68.4M of cloud hosting minimums, not linked to the rating.
4. Stress-test the assumption. At 10% lower operating income ($187.6M) the best debt level moves from 21% to 19%. At 30% lower ($145.9M) it falls to 14%.
5. Check the four drivers of optimal debt. Tax: 25%, usable because it paid $61.5M of cash taxes. Operating income to value: $208.4M ÷ $3,630.6M = 5.74%, above the peer median of 4.29%. Business risk: unlevered beta 1.22, above the market's 1.0, which argues for less debt. Price of debt against equity: 7.43% against 12.65% at 33% debt, but 5.38% against 11.63% at 21%.
6. Compare with peers on debt. The three peers above SolarWinds on EBIT/EV carry 1.25% (OneSpan), 45.28% (Open Text) and 13.90% (Teradata) debt, so the ratio alone does not set debt. SolarWinds at 33.03% is above the peer median of 11.7%.
7. Answer the three assigned questions. Commodity or cyclical: not applicable. Revenue rose from $719.4M to $758.7M to $796.9M and 93.5% is recurring. The 2022 loss comes from a one-off goodwill write-down. Family group: the nearest equivalent is the two sponsors, who are separate and not diversified, so the board should choose a ratio at or below the model's. Private company: SolarWinds went private on 2025-04-16, so market equity would be replaced by the $18.50 deal price, and an owner can choose far more debt than the 21% optimum.

**Result for SolarWinds:** The rating-distress cost is small (about 5% of operating income), and on the four drivers SolarWinds is mid-range on three and unfavorable on the fourth. That puts the optimum at 21% against an actual 33.03%.
Full answers: [lesson-20.md](lesson-20.md) · Walkthrough: [Step 20](walkthrough.md#step-20-when-does-the-debt-level-calculation-break-down-and-what-does-that-mean-for-solarwinds)

## Lesson 21 — Alternative Approaches

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Adjusted present value (APV) approach** | Values the firm as what it would be worth with no debt, plus the value of debt's tax benefits, minus the expected cost of bankruptcy. The optimal dollar debt is the amount that maximizes firm value. Formula: Firm Value = Unlevered Firm Value + (Tax Benefits of Debt - Expected Bankruptcy Cost from the Debt). |
| **Unlevered firm value** | What the firm would be worth with no debt. Estimate it by discounting at a cost of equity based on the unlevered beta, or back it out of today's value. Formula: Unlevered Value = Current Market Value - Current Tax Benefits of Debt + Expected Bankruptcy Cost. |
| **Tax benefits of debt (APV)** | The value of interest deductions, simply assumed to last forever. Formula: Tax benefits = Dollar Debt x Tax Rate. |
| **Expected bankruptcy cost** | The probability of going bankrupt times the cost if it happens, covering both direct and indirect costs. Formula: Expected Bankruptcy Cost = Probability of Bankruptcy x Cost of Bankruptcy. |
| **Probability of bankruptcy (synthetic rating and Altman study)** | Estimate the rating the firm would have at each debt level, then look up how often bonds with that rating defaulted over ten years in Altman's study (AAA 0.07% up to C 85%). |
| **Direct vs indirect bankruptcy cost** | Direct costs (legal and administrative) are generally 5%-10% of firm value. Indirect costs are harder to estimate and are bigger where default risk hurts operating income (airlines) than where it does not (groceries); Disney's was set at 25% of firm value. |
| **Relative analysis** | Anchor on the industry average debt ratio, since the "safest" place to be is near peers, then adjust subjectively. Higher tax rates, more stable income and lower insider ownership (more outside discipline) argue for more debt; more intangible assets (more agency problems) argue for less debt. |
| **Debt to capital ratio vs net debt to capital ratio** | Debt to capital is debt divided by debt plus equity (book or market value). Net debt to capital subtracts cash from debt first. |
| **Regression approach to debt ratios** | Regress debt ratios across companies on likely drivers (tax rate, earnings variability, EBITDA/Firm Value), check statistical significance (t statistics) and predictive power (R squared), then plug in a firm's own values to get a predicted debt ratio and compare with its actual. Formula: Debt Ratio = a + b (Tax rate) + c (Earnings Variability) + d (EBITDA/Firm Value). |
| **Predicted debt ratio (over levered / under levered)** | The regression output for one firm. If actual is above predicted the firm is over levered relative to peers; Tata Motors' predicted 18.54% versus actual 29.28%. |
| **CVOI (coefficient of variation in operating income)** | A measure of earnings variability: standard deviation of operating income over 10 years divided by its 10-year average. Higher CVOI goes with lower debt ratios in the market-wide regression. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. What is the expected tax benefit from borrowing money in the APV approach?
2. What is the bankruptcy cost as a percent of value at your firm? (If you can estimate it)
3. What is the optimal debt ratio using the APV approach?
4. If it is different from the optimal using the cost of capital approach, how would you explain the difference?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Debt | $1,285.0M | FY2024 10-K, note 9 (`sources/filings/swi-10k-fy2024.md`); ledger `company.debt_total` |
| Equity (market value) | $2,604.9M | Share price of $15.18 on 2025-02-05 times shares; ledger `company.equity_value` |
| Marginal tax rate | 25% | Damodaran Jan-2025 marginal tax rates by country (`sources/market-data/`); ledger `market.tax_rate_marginal` |
| Rating at each debt ratio | e.g. A- at 21%, B at 33% | Computed in lesson 18; model-output.md §3 |
| Ten-year default probability by rating | e.g. 2.50% (A-), 36.80% (B) | Altman table on the lesson 21 slides; ledger `facts.altman-10yr-default-probabilities` |
| Bankruptcy cost (judgment) | 25% of firm value (tested at 10% and 40%) | Midpoint of the lecture's 10% to 40% range; ledger `debt.bankruptcy_cost` |
| Goodwill and invested capital | $2,363.2M and $2,348.0M | FY2024 10-K balance sheet; ledger `company.goodwill`, `company.invested_capital` |
| Customer retention evidence | Maintenance renewal 97%, subscription net retention 99% (FY2024) | FY2024 10-K; ledger `facts.maintenance-renewal-rate`, `facts.net-retention-subscription` |
| Peer debt ratios and industry debt-to-equity | Peers 0.88% to 45.28%, median 11.72%; software industry debt-to-equity 4.9% | `sources/peer-filings/peer-facts-2025-02-05.md`; `sources/market-data/industry-betas-2025-01-05.json` (Damodaran Jan-2025, 333 firms) |

### Steps to complete the assignment

1. Set firm value today: debt $1,285.0M plus equity $2,604.9M is $3,889.9M.
2. Compute the tax benefit of current debt, assuming it stays forever: 25% × $1,285.0M = $321.2M. Interest of $112.4M is below EBIT of $208.4M, so the full deduction is usable.
3. Look up the current rating (B on the 33% schedule row) and its ten-year default probability, 36.80%.
4. Pick the loss if default happens. Judgment: 25% of value. Not lower, because goodwill ($2,363.2M) is almost all of invested capital ($2,348.0M) and would fetch little in a sale, and customers sign annual contracts. Not higher, because after SUNBURST renewals reached 97%. SUNBURST tested trust, not solvency, so it only sets a floor.
5. Compute expected bankruptcy cost: 36.80% × 25% of the unlevered value is $361.6M.
6. Back out the value with no debt: $3,889.9M − $321.2M + $361.6M = $3,930.2M.
7. Repeat for each debt ratio (value = unlevered + tax benefit − expected bankruptcy cost). At 21%: tax benefit $204.2M, expected bankruptcy cost $24.6M, firm value $4,109.9M. At 33%: $320.9M, $361.6M, $3,889.6M. Tax benefit peaks at 40% ($389.0M) then shrinks because interest exceeds operating income.
8. Compare with peers. SolarWinds' 33.03% is 2.8 times the peer median of 11.72% and far above the industry's 4.9% debt-to-equity. Both views say over-levered. We did not run a regression: eight peers are too few.
9. Answer the assigned questions. Tax benefit $321.2M. Bankruptcy cost 25% of value ($361.6M expected today, $24.6M at 21%). APV optimum 21%, the same as the cost-of-capital method. At a 40% bankruptcy cost it is still 21%, but at 10% it moves to 40%. The dollar gain from moving from 33% to 21% is $4,109.9M − $3,889.6M = $220.3M, against $144.4M from the cost-of-capital method, because the methods price distress differently.

**Result for SolarWinds:** Adjusted present value (APV) gives an optimum of 21%, where firm value peaks at $4,109.9M against $3,889.6M today, matching the cost-of-capital answer. The 25% bankruptcy cost is the one judgment that matters.
Full answers: [lesson-21.md](lesson-21.md) · Walkthrough: [Step 21](walkthrough.md#step-21-if-we-count-the-tax-savings-and-the-cost-of-failure-separately-what-debt-level-is-best)

## Lesson 22 — Moving to the Optimal

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Right financing mix / under levered / over levered** | After the analysis, a firm has one of three outcomes: its actual debt ratio equals its optimal (right mix, leave it alone), is below it (under levered, too little debt), or is above it (over levered, too much debt). |
| **Recapitalization** | Changing the debt ratio by changing only the capital mix: borrow and buy back stock (or pay a special dividend), or raise equity and retire debt. |
| **Moving through investments** | The other way to shift the debt ratio: fund new projects disproportionately with debt (to raise the ratio) or with equity (to lower it). |
| **Immediate vs gradual change in leverage** | The speed decision. The slides frame the choices as an immediate change, a gradual change, or no change, depending on how urgent the firm's situation is. |
| **Takeover threat (under levered firms)** | An under levered firm can be a hostile acquisition target because a buyer can borrow against its assets to buy it. A small firm with weak stock performance should move quickly; a large or well-performing firm has time. |
| **Bankruptcy threat (over levered firms)** | An over levered firm with a very low rating (CCC) must cut debt fast, usually by negotiating with lenders. One with time can fund good projects from retained earnings (equity grows, so the debt ratio falls) or, lacking good projects, use retained earnings to pay down debt. |
| **Good projects test** | When time is available, the key question is whether the firm has a record of earning more than its cost of capital (positive NPV). If yes, borrow to take those projects, which both lowers the cost of capital and adds value. Disney: 12.61% return on capital versus 7.81% cost of capital. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |

### What the project asked

1. Is your firm under, over or correctly levered?
2. If under levered, is it under threat of a hostile acquisition? If over levered, how imminent is the bankruptcy threat?
3. How good are the potential projects that the company can invest in?
4. What is the best path that you see for your firm to get from its actual to its optimal debt ratio?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Actual and optimal debt ratio | 33.03% actual; 21% optimum; debt $468.1M above optimum | model-output.md §1, §3 |
| Interest coverage and synthetic rating | 1.85x, B- | model-output.md §2 |
| Cash and undrawn revolver | $259.3M cash; $130.0M undrawn revolver | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `company.cash`, `debt.revolver_undrawn` |
| Covenant and maturity | Only financial test springs when revolver is more than 35% drawn; loan due 2030-02-05 | FY2024 10-K note 9; ledger `debt.covenants` |
| Owners and consent rights | Silver Lake 36.56%, Thoma Bravo 29.79%; both must consent to a change of control | 2024 proxy, stockholders' agreement (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders` |
| Return on invested capital and cost of capital | 6.66% against 10.23% | model-output.md §8, §1 |
| Management's free cash flow to the firm | $212.0M (2025), $258.0M (2026) | Merger information statement, DEFM14C (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `forecast.years` |
| Interest expense | $112.4M | FY2024 10-K; ledger `company.interest_expense` |
| Sale-process history | 13 parties approached in 2023, three offers of $12.00 to $13.00 withdrawn; unaffected price $15.18 against deal $18.50 (21.9% premium) | DEFM14C "Background of the Merger" (`sources/deal-docs/swi-defm14c-2025-merger.md`) |
| 2024 special dividend and share withholding | $168.2M and $26.5M | FY2024 10-K; ledger `company.history` |

### Steps to complete the assignment

1. Compare actual with optimal debt: 33.03% against 21%, so SolarWinds is over-levered by $468.1M. The other two coverage measures give optima of 26% and 28%, still below 33%.
2. Because it is over-levered, the takeover branch does not apply. It is also closed by structure: any change of control needed both sponsors' consent (36.56% and 29.79%).
3. Test how close distress is. Coverage is 1.85x (B-), but cash is $259.3M, the $130.0M revolver is undrawn, the covenant springs only above 35% drawn, the loan is due in 2030, and 2024 free cash flow to equity was $127.0M. With operating income down 30% the optimum falls to 14%, not default. Not imminent.
4. Test project quality: $208.4M × (1 − 25%) = $156.3M on invested capital of $2,348.0M is 6.66%, below the 10.23% cost of capital. Goodwill from the 2016 buyout inflates the base, and management's plan (margin 32.69% in 2025 to 40.14% in 2030) is not yet a record.
5. Choose the path. The lecture's rule for over-levered, not distressed, and poor projects is to retire debt gradually from cash flow. Annual after-tax interest is $112.4M × 75% = $84.3M, leaving $127.7M (2025) and $173.7M (2026), or $301.4M over two years. The $468.1M gap closes in the third year (2027 adds $212.7M).
6. Reject the alternatives: the value of moving is only $144.4M, or $10.9M a year, so borrowing to rush is not worth it. A recapitalization with new debt is the wrong direction, and new debt above $300.0M needed both sponsors' consent.
7. Note what the company did instead: the April 2024 $168.2M special dividend and $26.5M share withholding, with debt unchanged at about $1.24 billion. That is the opposite of the advice.
8. Answer the assigned questions. Over-levered; bankruptcy threat not imminent and hostile takeover impossible; projects weak on the record (6.66% against 10.23%; FY2024 revenue growth 5.0% against management's 8.12% a year); best path is to pay debt down from operating cash flow over about three years with no new payouts, no recapitalization and no equity issue.

**Result for SolarWinds:** SolarWinds is over-levered (33.03% against 21%, $468.1M too much debt) but not in distress, with projects earning 6.66% against a 10.23% cost of capital. The path is to repay debt from cash flow over about three years.
Full answers: [lesson-22.md](lesson-22.md) · Walkthrough: [Step 22](walkthrough.md#step-22-is-solarwinds-borrowing-too-much-or-too-little-and-how-should-it-get-to-the-right-level)

## Lesson 23 — The Right Financing

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Matching debt to assets (fundamental principle of designing debt)** | Make the cash flows on debt line up as closely as possible with the cash flows the firm earns on its assets. This reduces default risk, increases debt capacity and increases firm value. |
| **Perfect financing instrument** | A security with all the tax advantages of debt while keeping the flexibility of equity. |
| **Line drawn by the tax code** | A custom security only works if the tax authority still treats it as debt so interest stays deductible; there can be a trade-off between better matching and better tax benefits. |
| **Ratings agency, analyst and regulator tension** | Rating agencies prefer more equity (safer), equity analysts dislike new equity (dilutes earnings per share), and regulators care about capital ratios (usually book value). Financing that satisfies all three is the goal. |
| **Trust preferred stock** | A hybrid with a fixed, tax-deductible dividend, where skipping payments can give holders voting rights. Rating agencies first treated it as equity, then only gave partial equity credit. |
| **Duration (vs maturity)** | The effective life of debt as a stream of payments, shorter than its stated maturity. Debt should match the duration of the firm's assets; Disney's recommended duration is about 4 to 5 years. |
| **Fixed vs floating rate debt** | Floating rate debt resets with market rates. It fits a firm whose operating income rises with interest rates and that can pass inflation through to customers (Disney). |
| **Currency matching (foreign currency debt)** | Borrow in the currencies in which the firm earns its revenues so exchange-rate moves hurt assets and debt together. Disney's recommended foreign currency share is about 18%. |
| **Convertible debt** | Debt that can turn into equity. Suited to young, high-growth, risky firms such as Baidu (recommended convertible, Chinese Yuan debt). |
| **Commodity-linked debt** | Debt whose payments move with commodity prices, recommended for a miner like Vale whose revenues track commodity prices. |
| **Not locking in market mistakes** | If a firm is under rated or its securities are under priced, avoid long-term issuance. Issuing under priced equity or convertibles transfers wealth to new stockholders, and issuing long-term debt when under rated locks in rates that are too high. |
| **Swapping debt** | Exchanging existing debt for a different type (for example fixed rate dollar debt for floating rate foreign currency debt) to fix a mismatch without a new issue. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |

### What the project asked

1. Given its asset/project characteristics, what is the right type of debt for your firm?
2. What are the actual debt characteristics?
3. If there is a mismatch, what is the best way to fix it?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Term loan face value, rate type, currency | $1,235.7M; floating at SOFR (a benchmark short-term rate) plus 2.75%; US dollars | FY2024 10-K, note 9 (`sources/filings/swi-10k-fy2024.md`); ledger `company.debt_face`, `debt.rate_type`, `debt.currency` |
| Maturity and effective rate | 5.0 years (due 2030-02-05); 7.11% | FY2024 10-K note 9; ledger `debt.maturity_years`, `debt.kd_pretax_observed` |
| Revolver | $130.0M undrawn, of which $112.5M multicurrency | FY2024 10-K note 9; ledger `debt.revolver_undrawn`, `facts.revolver-tranches` |
| Leases | $49.4M | FY2024 10-K; ledger `company.lease_debt` |
| Contract length and pricing power | Mostly annual contracts; annual price increases; 97% maintenance renewal, 99% net retention | FY2024 10-K Item 1A and MD&A; ledger `facts.maintenance-renewal-rate`, `facts.net-retention-subscription` |
| Revenue by geography | 64.82% US, 35.18% international | FY2024 10-K; ledger `country.exposures` |
| Employees outside the US | 1,379 of 2,107 | FY2024 10-K; ledger `facts.employees-2024` |
| Interest-rate sensitivity | About $12.4M a year per 100 basis points; no swaps | FY2024 10-K Item 7A and Item 1A; ledger `facts.interest-sensitivity-100bp` |
| Capital spending, depreciation and amortization, R&D | $20.5M, $74.4M, $108.6M | FY2024 10-K; ledger `company.capex`, `company.da`, `company.rd_expense` |
| Foreign currency translation effect | Loss of $39.5M (2024), gain of $19.9M (2023) | FY2024 10-K; ledger `facts.fx-translation-adjustment-2024` |

### Steps to complete the assignment

1. Assess how long the assets last. The product is software, so spending is mostly salaries (R&D $108.6M) with little equipment (capital spending $20.5M against depreciation and amortization of $74.4M). Contracts are annual, but 97% renew, so cash flows outlast any contract. That points to medium-term debt of four to six years.
2. Assess currency. 64.82% of revenue is US and 35.18% international, an upper bound on foreign-currency revenue. 1,379 of 2,107 employees are outside the US, so foreign costs offset part of it. The net exposure cannot be sized from the filing.
3. Assess pricing power, which floating-rate debt needs. Annual price increases, 97% renewal and 99% net retention. Judgment: enough to justify floating debt, though maintenance revenue still fell 4.6% as customers moved to subscriptions.
4. Assess growth or mature. Operating income is positive and interest is covered 1.85x, so cash flow is already here and straight (not convertible) debt fits.
5. Write the target design: floating-rate, medium-term, straight debt, partly in euros, with at most 35.18% in foreign currency.
6. Describe the actual debt: one first-lien term loan of $1,235.7M at SOFR plus 2.75%, in dollars, 5.0 years left, 7.11% effective rate; $49.4M of leases; an undrawn $130.0M revolver; no swaps.
7. Find the mismatches. Rate type matches, but a 100 basis point rise would cost about $12.4M a year, 5.95% of EBIT of $208.4M. Maturity is a single 2030 bullet, a refinancing risk. Currency: 0% of debt foreign against up to 35.18% of revenue.
8. Choose the fix. Finance future needs differently rather than swap, because SolarWinds has no new projects. Leave the loan floating, add a cap or swap only if the sponsors want the $12.4M protected, and at the 2030 refinancing stagger the maturity and add a euro tranche. Of the revolver, $112.5M is multicurrency (8.8% of total debt of $1,285.0M). Swap cost is not computed because no swap quotes are in the filings.

**Result for SolarWinds:** The right design is floating, medium-term, straight debt partly in euros. The actual loan ($1,235.7M, SOFR plus 2.75%, 5.0 years, dollars only) matches on rate type and roughly on maturity and misses on currency.
Full answers: [lesson-23.md](lesson-23.md) · Walkthrough: [Step 23](walkthrough.md#step-23-is-solarwinds-borrowing-the-right-kind-of-debt)

## Lesson 24 — Trends and Measures

### Key terms

Slides here are thin: the main trend charts are images with no text, and there is no transcript in the folder. Terms below come from the slide text only.

| Term | Plain-language definition |
|------|---------------------------|
| **Dividends are sticky** | Companies are very reluctant to change dividends, so dividends change rarely (the slide charts dividend changes at US companies). |
| **Dividends tend to follow earnings** | Dividend changes track changes in earnings (shown in a chart). |
| **Dividends are affected by tax laws** | Payouts respond to dividend tax rates. In late 2012, with rates expected to revert to pre-2003 levels, 233 companies paid out $31 billion in dividends, 101 of them with insider holdings above 20%. |
| **Stock buybacks** | A company buying back its own shares as another way to return cash. More and more firms use buybacks rather than dividends. |
| **Dividend Payout** | The percent of earnings paid out as dividends; cannot be computed if net income is negative. Formula: Dividend Payout = Dividends / Net Income. |
| **Dividend Yield** | The return an investor earns from dividends alone, which becomes part of the expected return on the stock. Formula: Dividend Yield = Dividends per share / Stock price. |
| **Dividend policy differences across countries and growth classes** | Payout ratios and yields vary by country (G7 comparison) and by growth class of firm. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |

### What the project asked

1. How much (if any) has your company paid out in dividends each year for the last 5 years?
2. What dividend yield and payout ratio does this translate into?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| 2020 dividend | None ("never declared or paid any cash dividends") | FY2020 10-K (`sources/filings/swi-10k-fy2020.md`); ledger `facts.div-2020` |
| 2021 special dividend | $237.2M, $1.50 a share, paid 2021-08-24 | FY2023 10-K (`sources/filings/swi-10k-fy2023.md`); ledger `facts.special-dividend-2021` |
| 2022 and 2023 dividends | None | Ledger `company.history` |
| 2024 special dividend | $168.2M, $1.00 a share, paid 2024-04-15 | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `company.history`, `facts.special-dividend-2024-per-share` |
| Buybacks (shares withheld for employee taxes on vesting stock) | $11.1M (2022), $18.8M (2023), $26.5M (2024) | Ledger `company.history` |
| Net income | $132.7M (2020), $-51.4M (2021), $-929.4M (2022), $-9.1M (2023), $111.9M (2024) | 10-Ks; ledger `facts.ni-2020-2021`, `company.history` |
| Share price on 2024-02-14 | $12.89 | FY2024 10-K; ledger `facts.price-2024-02-14` |
| Unaffected share price on 2025-02-05 | $15.18 | Ledger market data (`sources/market-data/`) |
| Cash returned in 2024 | $194.7M | model-output.md §5 |

### Steps to complete the assignment

1. List cash dividends by year from the 10-Ks: 2020 none, 2021 $237.2M ($1.50 a share), 2022 none, 2023 none, 2024 $168.2M ($1.00 a share).
2. Total them: $237.2M + $168.2M = $405.4M. Both were special (one-time) payments, never regular.
3. Note the 2021 context. The payment came with the N-able spin-off, in which holders received one N-able share for every two SolarWinds shares. The buybacks in the table are shares withheld for employee taxes, not open-market repurchases.
4. Compute the payout ratio (dividends divided by net income) for 2024: $168.2M ÷ $111.9M = 150.3%. Counting the $26.5M of share withholding, cash returned is $194.7M, or 174.0%.
5. Mark the years where the ratio is not defined: 2021, 2022 and 2023 had net income of $-51.4M, $-929.4M and $-9.1M. For 2020 it is 0% ($0 on $132.7M). The five-year net income total is negative ($-745.3M), so no cumulative ratio exists.
6. Compute the dividend yield (dividend per share divided by price) for 2024. The record-date price is not recoverable, so show a range. $1.00 ÷ $12.89 = 7.76%, and $1.00 ÷ $15.18 = 6.59%. Judgment: a range rather than a pick. We did not compute 2021, because the spin-off and the reverse split make one price misleading.
7. Answer the assigned questions: two special payments in five years totalling $405.4M; 2024 payout ratio 150.3%; yield between 6.59% and 7.76%. This matches none of the usual market patterns of steady dividends that track earnings.

**Result for SolarWinds:** SolarWinds paid $405.4M in two special dividends over five years (2021 and 2024), with a 2024 payout ratio of 150.3% and a yield of 6.59% to 7.76%.
Full answers: [lesson-24.md](lesson-24.md) · Walkthrough: [Step 24](walkthrough.md#step-24-how-much-has-solarwinds-paid-its-shareholders-over-five-years)

## Lesson 25 — The Trade Off

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Three schools of thought on dividends** | (1) With no tax disadvantage and costless stock issuance, dividends do not matter. (2) If dividends are taxed worse than capital gains, dividends are bad and raising them reduces value. (3) If dividends have a tax advantage or stockholders like them, dividends are good and raising them increases value. |
| **Miller-Modigliani Hypothesis** | Dividends do not affect firm value if investment policy is unchanged. More dividends mean issuing new equity to fund the same projects, so lower price appreciation is offset by higher yield. It assumes no tax difference between dividends and capital gains, costless stock issuance, and no bad use of retained cash. |
| **Ex-dividend day** | The day the stock starts trading without the right to the declared dividend, so its price typically drops. How much it drops reveals how investors view dividends versus capital gains. |
| **Ex-dividend day price change formula** | Setting an investor indifferent between selling before and after ex-dividend day gives the price drop as a share of the dividend. Formula: (Pb - Pa) / D = (1 - t_o) / (1 - t_cg). Equal taxes mean the price falls by the dividend; higher dividend taxes mean it falls by less. |
| **Bird in the hand fallacy** | The claim that dividends now are safer than capital gains later, so dividend stocks deserve a higher value. The counter is that the stock price drops on ex-dividend day, so the right comparison is dividends against price appreciation today. |
| **Excess cash argument (bad reason to pay dividends)** | "We have excess cash this year" is a weak reason for dividends; the firm could repurchase stock instead, and one-time payouts ignore future needs, since raising new equity later can be very costly. |
| **Clientele effect** | Investors sort themselves by tax bracket: high-tax investors prefer non-dividend stocks, low-tax investors (in the study, older and poorer ones) hold high-dividend stocks. |
| **Signalling story** | Dividends tell the market management expects good cash flows. Increases are usually good news, but higher or new dividends can also signal a lack of good projects, and dividend changes are becoming less informative. |
| **Wealth appropriation story** | Dividends move wealth from lenders to equity investors, which is good for stockholders and bad for bondholders (excess returns on stocks and bonds around dividend changes). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |

### What the project asked

1. What does the trade off on dividends look like for your firm? (What are the benefits of paying more dividends? What are the costs of paying more dividends?)
2. Given that trade off, do you think that your company should be paying high, low or no dividends?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Ownership | Silver Lake 36.56%, Thoma Bravo 29.79% (about 66%); public float about 34% | 2024 proxy (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders`, `governance.marginal_investor` |
| Holders of record | 33 (2025-02-13), 39 a year earlier | FY2024 10-K Item 5 (`sources/filings/swi-10k-fy2024.md`); ledger `facts.holders-of-record` |
| Dividend policy and loan limits | Board discretion; loan limits dividends "subject to certain exceptions"; financial test only above 35% revolver draw | FY2023 and FY2024 10-K Item 5 and note 9; ledger `debt.covenants`, `debt.revolver_undrawn` |
| 2024 special dividend and withholding | $168.2M; $26.5M | FY2024 10-K; ledger `company.history` |
| Debt above the optimum | $468.1M | model-output.md §3 |
| Return on invested capital and cost of capital | 6.66% against 10.23% | model-output.md §8, §1 (lesson 22) |
| Free cash flow to equity (FCFE) and cash returned, 2024 | $127.0M; $194.7M | model-output.md §5 |
| Pre-tax cost of debt | 7.11% | FY2024 10-K note 9; ledger `debt.kd_pretax_observed` |
| Reason three bidders withdrew in 2023 | "the relative early stage of the Company's ongoing transition to a subscription-first business model" | DEFM14C "Background of the Merger" (`sources/deal-docs/swi-defm14c-2025-merger.md`) |

### Steps to complete the assignment

1. Identify the holders: Silver Lake 36.56% plus Thoma Bravo 29.79% is 66.35%. Diversified institutions in the float set the traded price.
2. Try the tax-preference test (compare the share price before and after the ex-dividend date, the first day a buyer no longer gets the dividend). It cannot be run: SolarWinds is delisted, no price history survives, and the sponsors' tax status is not in the files. So the answer is a reasoned lean.
3. Pick the school of thought. For the controlling holders, the neutral school (same total return either way) fits best. The clientele school has no support: there was no regular dividend and 33 holders of record.
4. Compare each possible reason for paying with the facts. Signalling: avoided, since both payments were labelled special. Lender restrictions: they did not stop $168.2M in 2024, because the revolver was undrawn. Habit: no, two payments in five years. Controlling-holder preference: strongest candidate. The sponsors would have received 66.35% × $168.2M = $111.6M, if their stakes were unchanged. This is an inference, not a disclosed motive.
5. Judge whether the reasons were good. The 2024 payment is hard to defend: debt was $468.1M above the optimum, return on capital (6.66%) was below the cost of capital (10.23%), and cash returned of $194.7M exceeded FCFE of $127.0M. Paying down 7.11% debt was worth more.
6. Consider the signal. A regular dividend would say the subscription transition is done, which bidders in 2023 had doubted.
7. List the trade-off. Benefits: cash kept inside earns less than its cost, and the controlling holders can use cash directly. Costs: debt above optimum, the payout already exceeded FCFE by $67.7M, and a wrong signal. Tax costs to holders are unknown.
8. Answer: pay no regular dividend and no special dividend until debt is near the 21% optimum. Afterwards return any excess by special dividend, not a regular one.

**Result for SolarWinds:** The files give a process but no stated reason for the payouts; the best reading is a controlling-holder preference ($111.6M of $168.2M). SolarWinds should pay no dividends until debt nears 21%.
Full answers: [lesson-25.md](lesson-25.md) · Walkthrough: [Step 25](walkthrough.md#step-25-should-solarwinds-pay-dividends-and-why-did-it)

## Lesson 26 — Assessments

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Cash/trust assessment** | A three-step test of dividend policy: how much the company could have paid out, how much it actually paid, and how much you trust management with excess cash (judged by past investment results and stock performance). |
| **Cash returned to stockholders (dividends plus buybacks)** | Because firms increasingly buy back stock, cash returned must count both dividends and buybacks. Formula: Cash returned = Dividends + Buybacks. |
| **Free Cash Flow to Equity (FCFE)** | The cash left over after non-equity claimholders (debt and preferred stock) are paid and after reinvestment needed to sustain the firm and its growth; the measure of what a firm could have paid out. Formula: FCFE = Net Income + Depreciation & Amortization - Preferred Dividends - Capital Expenditures - Working Capital Needs - Principal Repayments + Proceeds from New Debt Issues. |
| **FCFE with stable leverage** | If the firm keeps a constant debt ratio (DR = Debt/Capital), it funds that share of reinvestment with new debt. Formula: FCFE = Net Income - (1 - DR)(Capital Expenditures - Depreciation) - (1 - DR)(Change in Working Capital). |
| **Normalized debt ratio (FCFE at target debt)** | Computing FCFE with the firm's current or target debt ratio rather than its actual borrowing in each year, to give a steadier picture of what it could pay out. |
| **FCFE for a bank** | A bank's reinvestment is the extra regulatory capital (book equity) it must hold to grow. Formula: FCFE (Bank) = Net Income - Increase in Regulatory Capital. Example: 150 - 1,000 x 0.075 = 75 (millions). |
| **Cash accumulators** | Firms whose FCFE exceeds dividends plus buybacks, so cash piles up on the balance sheet. |
| **Over payers** | Firms whose dividends plus buybacks exceed FCFE (including those with negative FCFE that still pay out). |
| **Consequence of not paying FCFE** | The undistributed FCFE shows up elsewhere, for example as higher cash balances (Microsoft 1996: $2,127 million of FCFE, no payout), which is why the assessment ends by asking where the cash went. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |

### What the project asked

1. How much has your company returned to its stockholders, in the form of dividends and stock buybacks in the last five years?
2. How much cash could your company have returned in the last five years? (Estimate FCFE)
3. If there is a difference, where is it showing up (cash balances, debt ratios)?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Net income | $-929.4M (2022), $-9.1M (2023), $111.9M (2024) | 10-Ks FY2023, FY2024 (`sources/filings/`); ledger `company.history` |
| Non-cash impairments added back (2022) | $906.4M (goodwill $891.1M plus intangibles) | FY2023 10-K; ledger `company.history` 2022 impairment |
| Net capital spending (capex minus D&A) | $-74.2M (2022), $-63.9M (2023), $-53.9M (2024) | model-output.md §5 |
| Change in working capital | $-7.0M, $-13.9M, $38.8M | model-output.md §5 |
| Net new debt | $-664.4M (2022), $-9.3M (2023), $0.0M (2024) | 10-Ks; ledger `company.history` |
| Dividends and buybacks | $11.1M (2022), $18.8M (2023), $194.7M (2024: $168.2M dividend plus $26.5M buybacks) | 10-Ks; ledger `company.history` |
| Year-end cash | $148.9M (2022), $289.2M (2023), $259.3M (2024) | 10-Ks; ledger `company.history` |
| Debt at year end | $1,319.2M (2022), $1,285.0M (2024) | 10-Ks; ledger `company.history` |
| Owners and board | Silver Lake 36.56%, Thoma Bravo 29.79% (66.35% together) | 2024 proxy (`sources/filings/swi-def14a-2024.md`); ledger `governance.controlling_holders`, `governance.board` |
| 2020 and 2021 flows | 2021 special dividend $237.2M; $14.2M and $12.1M of withholding repurchases | FY2023 and FY2020 10-Ks; ledger `facts.special-dividend-2021`, `facts.withholding-buyback-2020-2021` |

### Steps to complete the assignment

1. Choose the years. Build only 2022 to 2024, because earlier years include N-able (spun off in July 2021) and are not comparable.
2. Apply the FCFE formula: net income plus non-cash impairments, minus (capex minus D&A), minus change in working capital, plus net new debt. For 2024: $111.9M + $53.9M − $38.8M + $0.0M = $127.0M. The same formula gives $-606.2M (2022) and $59.4M (2023), a total of $-419.8M.
3. Add dividends and buybacks: $11.1M, $18.8M and $194.7M, a total of $224.6M.
4. Compare. 2024: $194.7M returned against $127.0M of FCFE is $67.7M more, or 153%. 2023 returned $40.6M less than FCFE. 2022's FCFE was negative.
5. Explain the 2022 distortion. Net income includes $906.4M of non-cash write-downs, which we add back. What remains is mostly $664.4M of term loan repaid. Before that repayment FCFE would have been about $58.2M.
6. Find where the gap shows up. 2022: debt repayment funded from cash left by the N-able separation (cash $148.9M, debt $1,319.2M). 2023: cash built to $289.2M. 2024: the dividend drew cash down to $259.3M with no new debt. Over 2022 to 2024 cash rose by $110.4M.
7. Check for an activist. None appears. Silver Lake and Thoma Bravo hold 66.35% and sit on the board, and received about $111.6M of the 2024 payout.
8. Answer the assigned questions. Returned over 2022 to 2024: $224.6M. Adding 2021 ($237.2M dividend plus $14.2M) and 2020 ($12.1M, consolidated with N-able), the five-year total is $488.1M. FCFE over 2022 to 2024 was $-419.8M, or about $253.9M before $673.7M of debt repayment, so the company paid out about what it could and used the rest of its cash to repay debt.

**Result for SolarWinds:** FCFE was $-419.8M over 2022 to 2024 against $224.6M returned; in 2024 it returned $194.7M against $127.0M of FCFE, funded from cash, not debt. No activist was needed because the two sponsors hold 66.35%.
Full answers: [lesson-26.md](lesson-26.md) · Walkthrough: [Step 26](walkthrough.md#step-26-did-solarwinds-hand-back-more-cash-than-it-could-afford)

---

# Module 4 — Dividends & Valuation (lessons 27–36)

## Lesson 27 — Action and Follow Up

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Dividend Matrix** | A two-by-two grid for judging dividend policy: are the firm's projects good or poor (return on equity versus cost of equity), and does it have a cash surplus or deficit (dividends paid relative to FCFE)? Cash surplus plus poor projects means pressure to pay out more; cash surplus plus good projects means maximum flexibility; cash deficit plus poor projects means the real problem is investment policy; cash deficit plus good projects means reduce the payout. |
| **Dividends paid out relative to FCFE** | The test of whether a firm pays out less or more than it could afford: compare dividends (plus buybacks) with free cash flow to equity, the cash left over for stockholders after reinvestment and debt flows. Paying out less than FCFE builds up cash; paying out more means the gap is funded by borrowing or by drawing down cash. Formula: Cash paid as % of FCFE = (Dividends + Buybacks) / FCFE |
| **Quality of projects taken: ROE versus Cost of Equity** | The measure of whether managers have used stockholders' money well: compare the return on equity earned on the firm's projects with the return stockholders require. A return below the cost of equity means the projects destroyed value. Formula: ROE - Cost of Equity (Disney earned about 2% less than its cost of equity, 1994-2003). |
| **Cash Surplus / Cash Deficit** | A cash surplus means the firm generates more free cash flow to equity than it pays out; a cash deficit means FCFE is negative or smaller than the payout. The two together with project quality decide which dividend cell a firm sits in. |
| **Cash payout as % of target FCFE** | Total cash returned divided by the FCFE you would get if the firm borrowed at its target debt ratio rather than its actual debt. It shows whether a payout (Vale's 223.63%) is too high even after allowing for sensible borrowing. |
| **Jensen's alpha** | The stock's return minus the return its risk level says it should have earned. A positive alpha (Disney by 2009) means the stock beat what its risk required; a negative alpha means it underperformed. |
| **ROC versus cost of capital** | The same project-quality test applied to the whole firm: return on capital compared with cost of capital. Disney's ROC moved from well below to above its cost of capital between 2004 and 2008, which is why stockholders became more willing to let it keep cash. |
| **Dividend payout ratio** | The share of net income paid out as dividends. Formula: Dividends / Net Income |
| **Cash payout ratio** | The share of net income returned to stockholders through dividends and stock buybacks together. Formula: (Dividends + Buybacks) / Net Income |
| **Voting vs preferred shares (Vale)** | Vale has common shares with votes and preferred shares without; it committed to paying 35% of earnings as dividends to the preferred, who gain voting rights if it fails. This shows a dividend commitment can be contractual rather than a free management choice, so cutting the dividend may not be possible. |
| **Managing changes in dividend policy** | Dividend cuts are read as bad news: stocks fall around the announcement (about -8% when a cut came with an earnings decline) and recover more only when the cut is paired with new investment or growth opportunities (+8.79% the following quarter). The lesson is to explain the reason for the change. |
| **Growth firms and dividends** | The argument that high-growth firms should start paying dividends to widen their stockholder base (some investors, such as pension funds, cannot hold non-payers). The slides pose it as a question to challenge, not as an endorsement. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. If your firm has returned less cash than it can over time and has a big cash balance, do you trust the firm with your cash?
2. If your firm has returned more cash than it can over time, should it scale back cash return?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Operating income (EBIT, earnings before interest and tax) | $208.4M | FY2024 10-K income statement (`sources/filings/swi-10k-fy2024.md`); ledger `company.ebit` |
| Marginal tax rate | 25% | Damodaran January 2025 country tax table (`sources/market-data/country-risk-regions-2025-01-01.md`); ledger `market.tax_rate_marginal` |
| Invested capital (book equity + debt - cash) | $2,348.0M | FY2024 10-K balance sheet; ledger `company.invested_capital` |
| Cost of capital / cost of equity | 10.23% / 12.65% | Computed in earlier lessons; model-output.md §1 |
| Operating income history, 2022-2024 (2022 with $906.4M non-cash impairments added back) | $86.8M, $150.4M, $208.4M | FY2024 10-K (2022-2024 columns) and FY2023 10-K; ledger `company.history` |
| Total return on $100 invested end of 2019 (SolarWinds vs peer index) | $81, $57, $38, $51 vs $142, $190, $135, $211 (2020-2023) | 2024 proxy, Pay versus Performance table (`sources/filings/swi-def14a-2024.md`); ledger fact `tsr-2023` |
| Free cash flow to equity (FCFE) and cash returned, 2023-2024 | FCFE $59.4M and $127.0M; returned $18.8M and $194.7M | Computed from the 10-K cash flow statements; model-output.md §5 |
| 2024 dividend and net new debt | $168.2M dividend; net new debt $0.0M ($10.0M drawn, $10.0M repaid) | FY2024 10-K cash flow statement; ledger `company.history` |
| 2021 special dividend and N-able cash | $237.2M dividend; $505.6M from N-able at the spin-off | FY2023 10-K cash flow statement and Item 5; ledger facts `special-dividend-2021`, `spin-distribution-2021` |
| Controlling holders | Silver Lake 36.56%, Thoma Bravo 29.79% | 2024 proxy, beneficial ownership table; ledger `governance.controlling_holders` |

### Steps to complete the assignment

1. Compute after-tax operating income: $208.4M x (1 - 25%) = $156.3M.
2. Divide by invested capital to get return on invested capital (ROIC): $156.3M / $2,348.0M = 6.66%.
3. Compare with the cost of capital: 6.66% against 10.23% is a gap of -3.58 points, so economic value added is $-84.0M a year. Return on equity is 7.99% against a cost of equity of 12.65% (-4.66 points).
4. Check the trend over management's tenure using the same method each year: 2022 was 2.69% ($65.1M after tax on $2,422.9M of capital), 2023 was 4.79% ($112.8M on $2,356.3M), 2024 was 6.66%. It is rising but never reached 10.23%. Judgment: goodwill is 100.65% of invested capital, mostly from the 2016 buyout, so part of the low ROIC measures the price the sponsors paid.
5. Test the stock. There is no price history for a delisted ticker, so Jensen's alpha (return beyond what risk predicts) cannot be computed. Use the proxy's index instead: $100 became $51 by 2023, while the peer index became $211.
6. Place the company on the dividend matrix (good or bad projects, cash surplus or deficit). Projects: bad (ROIC below cost of capital). Cash: in 2023 it returned $18.8M against FCFE of $59.4M (surplus); in 2024 it returned $194.7M against $127.0M (deficit). The cell is "bad projects".
7. Check whether dividends were borrowed. 2024: the $168.2M dividend came with net new debt of $0.0M. 2021: the $237.2M dividend came from the $505.6M N-able sent to SolarWinds. Silver Lake and Thoma Bravo together held 66.35%, so $111.6M of the 2024 dividend went to them. Nothing in the filings says they needed the cash, so we do not infer it. The decision being deferred was the exit, which came with the February 2025 sale.
8. Answer the project questions. Trust the firm with cash? No: ROIC 6.66% against 10.23%, and the index fell to 51 against 211. But the premise only partly holds: 2022-2024 returned $224.6M against FCFE of $-419.8M, and cash ended at $259.3M, 6.7% of firm value of $3,889.9M, so there is no big hoard. Scale back cash return? Not on 2024 alone: it was 153% of FCFE, but 2023-2024 together returned $213.5M against FCFE of $186.4M (115%), and the real problem is low returns.

**Result for SolarWinds:** ROIC of 6.66% is below the 10.23% cost of capital, the stock trailed its peers ($51 against $211), and the company sits in the "bad projects" cell of the matrix; no dividend was paid with new debt.
Full answers: [lesson-27.md](lesson-27.md) · Walkthrough: [Step 27](walkthrough.md#step-27-should-shareholders-trust-solarwinds-with-its-cash)

## Lesson 28 — The End Game

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **peer group approach** | Setting dividend policy by comparing your firm's dividend yield and payout ratio with similar companies (same market and sector). The logic is "me too": pay what comparable firms pay. |
| **Dividend Yield** | Annual dividends per share as a percentage of the current stock price. Formula: Dividends / Current Price |
| **Dividend Payout** | The percentage of net income paid out as dividends. Formula: Dividends / Net Income (the slides use PYT for the payout ratio). |
| **Cash Return/FCFE** | Dividends plus buybacks as a percentage of free cash flow to equity; used to see whether a firm and its peers return more or less cash than they could afford. Formula: (Dividends + Buybacks) / FCFE |
| **Comparable Group** | The set of similar firms used as the benchmark. The slides show yields and payouts for sector groups (for example US entertainment, global autos, European banks) and note that medians are more reliable than averages when many peers pay nothing. |
| **Market regression (dividend yield and payout against fundamentals)** | A statistical fit across all US companies (January 2014) that predicts a firm's payout ratio and yield from its beta (BETA), expected growth in earnings over five years (EGR) and debt to capital ratio (DCAP). Riskier, faster-growing firms pay less; more indebted firms pay more. It goes beyond peer averages by controlling for these characteristics. |
| **Predicted Payout / Predicted Yield** | The dividend payout ratio or yield the market regression says a firm with Disney's characteristics should have (about 26.95% and 1.40% for Disney). Comparing it with actual (21.58% and 1.09%) suggested Disney paid too little in dividends, before counting its large buybacks. |
| **DCAP** | Debt to capital ratio used in the regression: total debt divided by total debt plus market value of equity. Formula: Total Debt / (Total Debt + Market Value of Equity) |
| **Dividend clientele** | Investors pick companies for their dividend policy, and companies choose policies that fit their characteristics. When the company changes and needs a different policy, the clientele that chose it may react badly, however well-intentioned the change. |
| **The problem with changing dividends** | Because of the clientele effect, a firm that needs to cut dividends to fund new investment (the phone company entering media) faces a bad reaction. Managers are tempted to keep paying and defer investment or issue stock instead of making the right change. |
| **flexible dividends** | Damodaran's "reset" idea: fixed dividends date from a century ago when stocks competed with bonds. Since equity cannot be viewed as a bond with a fixed yield plus price appreciation, payouts should flex with the business, and the move to buybacks may already reflect this. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |

### What the project asked

1. How does your company dividend and cash return policy measure up against other companies in the sector?
2. Given how much other companies in the sector are returning to stockholders, is your company returning too much or too little?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Peer payout ratios (dividends / net income) | Five of eight peers 0.0 (Akamai, NetScout, OneSpan, Qualys, Teradata); Progress 46.05%; NetApp and Open Text blank | Peers' FY2024 filings (`sources/peer-filings/peer-facts-2025-02-05.md`); ledger `peers[].payout` |
| Software sector payout, 351 firms | 27.22% dividends; 80.36% with buybacks | Damodaran January 2025 dividend table (`04-dividends-and-valuation/lesson-28/spreadsheet-divfcfe24.md`); ledger fact `sector-software-payout` |
| SolarWinds 2024 dividends, buybacks, net income | $168.2M; $26.5M; $111.9M | FY2024 10-K cash flow and income statements; ledger `company.history` |
| Cash returned and FCFE, 2024 | $194.7M and $127.0M | Computed in lesson 26; model-output.md §5 |
| Payout regression (R-squared 19.6%) | payout = 0.649 - 0.296 x beta - 0.800 x growth + 0.300 x debt-to-capital | Lesson 28 slides, January 2014 US companies (`04-dividends-and-valuation/lesson-28/slides.md`); ledger fact `payout-regression-2014` |
| Levered beta and debt-to-capital | 1.6714; 33.03% | Computed in earlier lessons; model-output.md §1 |
| Expected growth | 8.12% | Management forecast, merger information statement (DEFM14C) (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `forecast.management_growth` |
| Ownership of the two sponsors | 66.35% combined | 2024 proxy; ledger `governance.controlling_holders` |

### Steps to complete the assignment

1. List peer payouts. Five of the eight pay no dividend, Progress pays 46.05%, and NetApp and Open Text pay dividends that the SEC data did not tag, so they are left blank. The peer norm is no dividend.
2. Add the wider benchmark: Damodaran's 351 software firms paid out 27.22% of net income as dividends and 80.36% counting buybacks.
3. Compute SolarWinds' 2024 payout: dividends of $168.2M on net income of $111.9M is 150%. With the $26.5M of buybacks it is 174%. Cash returned over FCFE is 153% ($194.7M / $127.0M). In 2022 and 2023 it paid no dividend.
4. Run the regression: 0.649 - 0.296 x 1.6714 - 0.800 x 8.12% + 0.300 x 33.03% = 18.8%. Judgment: growth uses management's 8.12% because analyst growth could not be obtained. The coefficients are ten years old, so treat 18.8% as a rough marker, not a target.
5. Compare actual with predicted: the 2024 payout was eight times the predicted 18.8%.
6. Decide whether SolarWinds is copying its sector. It is not: 2024 was a special dividend by two controlling holders (66.35%), not a payout policy. In the two years without one, it looked like its peers.
7. Answer the project questions. Against the sector: an outlier in 2024 (150% against a peer median of 0.0 among those with a recorded payout, and 27.22% for the software group; 174% against 80.36% counting buybacks). Too much or too little? In 2024, too much, and 53% above its own FCFE; over 2023-2024 it returned 115% of FCFE ($213.5M against $186.4M), not far above capacity. Given returns below the cost of capital (6.66% against 10.23%), returning cash is the right direction, but it was lumpy.

**Result for SolarWinds:** The 2024 payout was 150% of net income (174% with buybacks) against a regression-predicted 18.8% and a sector average of 27.22%, so SolarWinds diverged in 2024 because of one special dividend, not policy.
Full answers: [lesson-28.md](lesson-28.md) · Walkthrough: [Step 28](walkthrough.md#step-28-does-solarwinds-pay-out-like-its-competitors)

## Lesson 29 — First Steps

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Intrinsic valuation** | Valuing an asset from its fundamentals: its cash flows, growth and risk. Discounted cash flow models are the usual tool. |
| **Relative valuation** | Valuing an asset by what investors are currently paying for similar assets, usually through value or price multiples compared among firms in the same business. It prices an asset rather than valuing it. |
| **Contingent claim valuation** | Valuing an asset whose cash flows depend on an external event, using option pricing models. |
| **Discounted cash flow valuation** | The main tool for intrinsic value: value is the present value of expected cash flows. Formula: Value of asset = E(CF1)/(1+r) + E(CF2)/(1+r)^2 + ... + E(CFn)/(1+r)^n |
| **Cash flows from existing assets** | The base-year earnings power of what the firm already owns, after tax and after the reinvestment needed to sustain it. It is the starting point of every DCF. |
| **Value of growth** | The net effect of growth: higher future earnings (positive) minus the reinvestment needed to produce them (negative). Growth can add, destroy or leave value unchanged, and it creates value only with excess returns. Formula: Expected Cash Flow = Expected Earnings - Reinvestment needed for growth |
| **Steady state** | The point where the firm grows at a stable rate no higher than the economy. The length of the growth period before it depends on how strong and sustainable the firm's competitive advantages are. |
| **Equity valuation** | Valuing only the stockholders' claim: discount cash flows to equity (what is left after expenses, taxes, interest and principal payments) at the cost of equity. Formula: Value of Equity = sum of CF to Equity(t) / (1+ke)^t |
| **Dividend discount model** | A special case of equity valuation in which the only cash flow counted is dividends; the stock is worth the present value of expected future dividends. |
| **Firm valuation** | Valuing the whole business: discount cash flows to the firm (after operating expenses and taxes, before debt payments) at the weighted average cost of capital. Formula: Value of Firm = sum of CF to Firm(t) / (1+WACC)^t |
| **Choosing a cash flow to discount** | The rule for picking the model: discount dividends when free cash flows cannot be estimated (financial firms such as Deutsche Bank); discount FCFE when the debt ratio is stable (Tata Motors); discount FCFF when the debt ratio may change (Vale and Disney). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |

### What the project asked

1. What is the market capitalization (market value of equity) for your company, relative to its earnings and cash flows?
2. How much has that market capitalization changed over time?
3. How have earnings/cash flows changed over time?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Shares outstanding (record date) | 171.6M | Merger information statement (DEFM14C), Written Consent section (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `company.shares_basic` |
| Unaffected share price, 2025-02-05 | $15.18 | DEFM14C, Goldman Sachs fairness opinion; ledger `company.share_price` |
| Deal price | $18.50 | DEFM14C, Per Share Merger Consideration; ledger `company.deal_price` |
| Net income, 2024 | $111.9M | FY2024 10-K income statement (`sources/filings/swi-10k-fy2024.md`) |
| Debt now, and as a share of capital | $1,285.0M; 33.03% at market, 47.28% at book | FY2024 10-K note 9 and note 7 (term loan face value plus leases); model-output.md §1 |
| New debt the buyer committed | $2,225.0M first lien + $525.0M second lien = $2,750.0M | Merger closing 8-K, Item 1.01 (`sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`); ledger fact `new-debt-2025` |
| Revenue, EBIT, net income, 2022-2024 | Revenue $719.4M, $758.7M, $796.9M; net income $-929.4M, $-9.1M, $111.9M | FY2024 and FY2023 10-Ks; ledger `company.history` |
| FCFE and FCFF history | FCFE $-606.2M, $59.4M, $127.0M; FCFF $146.3M, $190.6M, $171.4M | Computed; model-output.md §5 and §8 |
| Total return and share-count history | $100 became $51 (2023) vs peers $211; 309.9M shares (Feb 2019), 155.0M after the reverse split | 2024 proxy Pay versus Performance; FY2023 10-K Item 5; ledger facts `tsr-2023`, `shares-2019-02-15`, `corporate-actions-2021` |

### Steps to complete the assignment

1. Compute market capitalization (market value of equity): 171.6M shares x $15.18 = $2,604.9M. At the $18.50 deal price it is $3,174.6M.
2. Relate it to earnings and cash: $2,604.9M / $111.9M net income = 23.28x; against FCFE of $127.0M it is 20.5x. Enterprise value (equity plus debt minus cash) is $3,630.6M, which is 4.56x revenue and 12.84x EBITDA (earnings before interest, tax, depreciation and amortization), and 23.2x after-tax operating income of $156.3M.
3. Look at the debt ratio over time: debt was $1,319.2M, $1,300.4M and $1,285.0M at the ends of 2022-2024, against invested capital of $2,422.9M, $2,356.3M and $2,348.0M. The market and book debt ratios differ by 14 points (33.03% against 47.28%).
4. Choose firm versus equity valuation. The buyer committed $2,750.0M of term debt against $1,285.0M outstanding, so the debt ratio is about to change sharply, and cost of equity depends on it (11.63% at 21% debt, 12.65% at 33%). Judgment: value the firm (cash flow before debt payments, discounted at the cost of capital of 10.23%) and subtract debt at the end.
5. Name the four inputs a discounted cash flow (DCF) needs: cash flow from existing assets (lesson 30), growth (lesson 31), risk (cost of capital 10.23%) and when the company matures (growth 2.5%, stable return on capital 10%). The hardest is growth and its reinvestment: management's 2030 cash flow exceeds after-tax operating income, and the terminal value is $5,552.5M if that cash flow is grown but $3,808.9M with consistent reinvestment.
6. Describe change over time. Market-cap history is not one series because of the July 2021 N-able spin-off and the 2-for-1 reverse split. Per share, $100 invested at the end of 2019 was worth $51 at the end of 2023. From the $15.18 unaffected price to the $18.50 deal price, value rose 21.9%; the premium to the 90-day average price was about 35%.
7. Describe earnings and cash flow change: revenue grew about 5% a year; EBIT was $-819.6M, $150.4M, $208.4M (2022 includes $906.4M of non-cash impairments; $86.8M without them); the improvement is mostly margin (EBIT margin without impairments from 12.1% to 26.2%).

**Result for SolarWinds:** Market capitalization is $2,604.9M (23.28x earnings, $3,630.6M enterprise value), and we value the whole firm because debt is set to jump from $1,285.0M to $2,750.0M of new term loans.
Full answers: [lesson-29.md](lesson-29.md) · Walkthrough: [Step 29](walkthrough.md#step-29-what-is-solarwinds-worth-on-the-stock-market-and-do-we-value-the-whole-company-or-only-the-shares)

## Lesson 30 — Cash Flows

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Modified dividends** | For a firm whose actual dividends are not meaningful (Deutsche Bank in 2013, building regulatory capital), the potential dividends estimated as FCFE after required investment in regulatory capital, instead of the dividends actually paid. |
| **Free cash flow to equity (FCFE)** | Cash left for stockholders after reinvestment and after net borrowing; the cash flow discounted in an equity valuation. For Tata Motors it was computed from net income, capital expenditure, depreciation, working capital and change in debt. Formula: FCFE = Net Income - Equity Reinvestment, where Equity Reinvestment = CapEx - Depreciation + Change in Working Capital - Change in Debt |
| **Free cash flow to the firm (FCFF)** | Cash the business generates for all capital providers (stockholders and lenders) after tax and reinvestment, but before debt payments. Formula: FCFF = EBIT (1 - t) - (CapEx - Depreciation) - Change in Working Capital |
| **After-tax Operating Income** | Operating income reduced by the tax it would pay. Formula: Operating Income x (1 - Tax rate) (Disney: 10,032 x (1 - 0.3102) = $6,920 million) |
| **Net Cap Expenditures** | Capital spending (including acquisitions) minus depreciation and amortization: the net new money put into long-lived assets. Formula: Net CapEx = CapEx - Depreciation & Amortization |
| **Reinvestment Rate** | The share of after-tax operating income plowed back into the business. Formula: Reinvestment Rate = (Net CapEx + Change in Working Capital) / After-tax Operating Income (Disney: 53.93%) |
| **Matching discount rate to cash flow** | The discount rate must fit both the riskiness and the type of cash flow: cost of equity for dividends and FCFE, cost of capital for FCFF. Mismatches cause serious valuation errors. |
| **Cost of capital** | The weighted average of the after-tax cost of debt and the cost of equity, weighted by market values; the rate used to discount FCFF. Formula: Cost of capital = Ke x E/(D+E) + Kd (1-t) x D/(D+E) (Disney: 7.81%) |
| **Levered Beta (company, with cash)** | When FCFE includes income from cash, the equity beta must be recomputed for the whole company as the value-weighted average of the operating-asset beta and cash's beta of zero (Tata Motors: 0.964). |
| **Currency choice** | A company can be valued in any currency, but cash flows and discount rates must be in the same one, so Tata Motors is valued in nominal rupees with a rupee risk-free rate. |
| **Costs of equity and capital change over time** | Discount rates should not be held constant for every year; as the firm matures, its beta moves toward 1 and its debt ratio rises, so its cost of capital falls (Disney: 7.81% in years 1-5 to 7.29% by year 10). |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Damodaran datasets** | Free spreadsheets Professor Damodaran updates each January (some monthly): equity risk premiums, industry betas, country risk premiums, tax rates, and the table that turns interest coverage into a credit rating and borrowing spread. | The market-wide inputs to a cost of capital that a single company's filings can't give you. | pages.stern.nyu.edu/~adamodar, under Data; older editions are in the archive section. |
| **FRED (Federal Reserve economic data)** | The St. Louis Fed's free database of interest rates and economic series: Treasury yields, SOFR, the fed funds rate, inflation. | The risk-free rate (10-year Treasury yield) on a specific date, and benchmark rates for floating-rate loans. | fred.stlouisfed.org (for example, series DGS10 for the 10-year Treasury yield). |

### What the project asked

1. What is the current cost of equity and capital for your firm? How might these numbers change in the future?
2. Estimate the free cash flows to the firm & equity in the most recent five years for your firm?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Operating income (EBIT) | $208.4M | FY2024 10-K income statement (`sources/filings/swi-10k-fy2024.md`); ledger `company.ebit` |
| Tax rate used | 25% marginal (reported rate unusable: $8.1M tax benefit on $103.8M pre-tax income) | Damodaran January 2025 country tax table; FY2024 10-K; ledger `market.tax_rate_marginal`, fact `tax-benefit-2024` |
| Capital spending | $20.5M | FY2024 10-K cash flow statement; ledger `company.capex` |
| Depreciation and amortization (D&A) | $74.4M, of which $52.9M is acquired technology and intangibles | FY2024 10-K cash flow and income statements; ledger `company.da`, `company.acquisition_amortization` |
| Change in working capital | $38.8M investment | FY2024 10-K cash flow statement; ledger `company.change_wc` |
| Stock-based compensation | $76.5M (treated as an expense) | FY2024 10-K cash flow statement; ledger `company.sbc` |
| Cost of equity and cost of capital | 12.65% and 10.23% | Computed in earlier lessons; model-output.md §1 |
| Risk-free rate, equity risk premium, levered beta | 4.43%, 4.92%, 1.6714 | FRED 10-year Treasury 2025-02-05; Damodaran January 2025 data weighted by revenue by region (10-K note 16); model-output.md §1 |
| Optimal-debt cost of capital schedule | 10.03% at 21% debt; 10.72% at 40%; 16.44% at 50% | Model-output.md §3 |
| Management's 2025 free cash flow | $212.0M | DEFM14C, Certain Company Financial Forecasts; ledger `forecast.years` |

### Steps to complete the assignment

1. Compute after-tax operating income: $208.4M x (1 - 25%) = $156.3M. Judgment: use the marginal 25%, not the reported rate, because the company booked a tax benefit of $8.1M on pre-tax income of $103.8M.
2. Compute net capital spending: capital spending $20.5M less D&A $74.4M = $-53.9M.
3. Add the change in working capital of $38.8M (mostly a $23.8M fall in income taxes payable).
4. Reinvestment is $-53.9M + $38.8M = $-15.1M, a rate of -9.66% of after-tax operating income.
5. Free cash flow to the firm (FCFF) = $156.3M - (-$15.1M) = $171.4M.
6. Check the judgment calls. $52.9M of the amortization is acquired technology that will never be replaced; leaving it out gives net capex of $-1.0M, reinvestment of $37.8M and a rate of 24.18%. We use the reported basis because the ledger carries it. Stock compensation is treated as an expense, not added back; adding it back would give $247.9M.
7. Pair the discount rate: a cash flow before debt payments pairs with the cost of capital, 10.23%, not the cost of equity.
8. Answer the project questions. Cost of equity 12.65% (4.43% + 1.6714 x 4.92%) and cost of capital 10.23% (33.03% debt at an after-tax 5.33%). They could change through rates, leverage (10.03% at the optimal 21% debt; the buyer's $2,750.0M of term debt pushes toward the steep part of the schedule), cost of debt (observed 7.11% against 8.85% implied by a B- synthetic rating) and beta (1.22 January 2025 software average). Last five years: three comparable years because 2020-2021 include N-able. FCFE $-606.2M, $59.4M, $127.0M for 2022-2024; FCFF $146.3M, $190.6M, $171.4M.

**Result for SolarWinds:** Base-year FCFF is $171.4M with a reinvestment rate of -9.66%, discounted at the cost of capital of 10.23% (cost of equity 12.65%).
Full answers: [lesson-30.md](lesson-30.md) · Walkthrough: [Step 30](walkthrough.md#step-30-what-cash-does-solarwinds-produce-and-what-rate-do-we-discount-it-at)

## Lesson 31 — Growth

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Historical growth** | Growth computed from past earnings. It depends on start and end dates, the earnings measure and the averaging approach, and is a poor predictor of the future. |
| **Outside estimates** | Growth forecasts from analysts or managers. They are biased and not very good, especially for longer horizons. |
| **Expected Growth Rate from Existing Fundamentals (equity)** | Growth in net income implied by how much the firm keeps and how well it invests it. Formula: Expected Growth = Retention Ratio x Return on Equity (Deutsche Bank: 0.6703 x 0.1945 = 13.04%) |
| **Return on Equity** | Net income divided by the book value of equity at the start of the year. Formula: Net Income / Book Value of Equity (beginning of year) |
| **Retention Ratio** | The share of earnings kept in the firm rather than paid as dividends. Formula: 1 - Dividends / Net Income |
| **Normalized Return on Equity / Normalized Retention Ratio** | The same measures computed on average earnings over several years (Deutsche Bank's 2003-07 average) instead of one unusual year; it cut the growth estimate from 13.04% to 5.40%. |
| **ROE and Leverage** | ROE reflects both investment quality and borrowing. Formula: ROE = ROC + D/E (ROC - i(1-t)), where ROC = EBIT(1-t) / (BV of Debt + BV of Equity - Cash) |
| **Expected growth in EBIT (operating income)** | Growth in operating income from reinvestment and return on capital. Formula: Expected Growth = Reinvestment Rate x Return on Capital (Disney: 53.93% x 12.61% = 6.8%) |
| **Return on Capital** | After-tax operating income divided by capital invested at the start of the year. Formula: EBIT(1-t) / (BV of Equity + BV of Debt - Cash) |
| **Changing growth and margins** | When a firm is in transition and margins change, the link between reinvestment and growth breaks. Instead: forecast revenue growth, forecast a target margin and a path to it, and estimate reinvestment from revenues. |
| **Sales to capital ratio** | Dollars of revenue earned per dollar of investment; used to turn a revenue forecast into reinvestment. Formula: Reinvestment = Change in Revenues / Sales-to-Capital ratio (Baidu: 2.64) |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |
| **Capital IQ** | S&P's paid database of company financials, market data, deals, ownership and credit information, standardized across companies. | Cross-checking figures and quickly assembling comparables or deal histories. Cite the filing itself when the filing has the number. | Subscription only (this course provides an NYU academic account through the final-project due date). |

### What the project asked

1. What is the historical growth rate in your company's revenues? EBIT? Net income?
2. What are analysts or managers projecting as an expected growth rate in the future?
3. Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?
4. If margins are changing, what are your estimates of revenue growth, margins and reinvestment for the future?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| ROIC and reinvestment rate, 2024 | 6.66% and -9.66% (24.18% on the alternative basis) | Computed in lessons 27 and 30; model-output.md §8 |
| Revenue, 2022-2024 | $719.4M, $758.7M, $796.9M | FY2024 10-K; ledger `company.history` |
| EBIT history (2022 ex impairments) | $86.8M, $150.4M, $208.4M | FY2024 and FY2023 10-Ks; model-output.md §8 |
| Net income, 2022-2024 | $-929.4M, $-9.1M, $111.9M | FY2024 10-K; ledger `company.history` |
| Return on equity | 7.99% | Model-output.md §8 |
| Management forecast | Revenue $832.0M (2025) to $1,273.0M (2030); EBIT margin 32.69% to 40.14%; 8.12% a year | DEFM14C, Certain Company Financial Forecasts (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `forecast.years`, `forecast.management_growth` |
| Analyst growth | Not available | Capital IQ estimates grid did not load; listed under `meta.omitted` in `inputs.yaml` |
| Peer revenue growth and EBIT margin | Growth median 4.05% (range -9.3% to 28.6%); margin median 15.92% | Peers' FY2024 filings (`sources/peer-filings/peer-facts-2025-02-05.md`); ledger `peers`, fact `peer-median-growth-margin` |
| Research and development expense | $108.6M | FY2024 10-K income statement; ledger `company.rd_expense` |
| Invested capital, 2022-2024 | $2,422.9M, $2,356.3M, $2,348.0M | FY2024 and FY2023 10-K balance sheets; ledger `company.history` |

### Steps to complete the assignment

1. Compute fundamental growth (reinvestment rate x return on capital) on the reported basis: -9.66% x 6.66% = -0.64%. On the alternative basis that leaves out acquisition amortization: 24.18% x 6.66% = 1.61%. Either way, under 2%.
2. Compute the equity version: ROE 7.99% x equity reinvestment rate of -13.5% = -1.1%. Essentially zero growth.
3. Measure actual growth: revenue grew 5.25% a year from 2022 to 2024 (5.5% in 2023, 5.0% in 2024; 3.5% a year from the 2021 recast revenue of $718.6M). EBIT rose from $86.8M to $208.4M (54.9% a year, 38.6% from 2023 alone), which mostly measures recovery from SUNBURST costs and impairment. Net income started from a negative base, so no growth rate can be computed.
4. Record the projections: management 8.12% a year in revenue to 2030 with EBIT margin 32.7% to 40.1%; analysts not available.
5. Ask where growth comes from. Not from capital: invested capital fell from $2,422.9M to $2,348.0M while revenue rose, and management's plan has free cash flow above after-tax operating income, a cumulative $163.1M of negative reinvestment over 2025-2030 while revenue rises $476.1M. Judgment: R&D of $108.6M is expensed, so it hides reinvestment; the zero-growth figure is a floor, not a forecast.
6. Test whether fundamentals are stable enough. They are not: EBIT margin was 12.1%, 19.8%, 26.2% in 2022-2024 and ROIC rose from 2.69% to 4.79% to 6.66%. Peer comparison: SolarWinds' 5.0% growth is near the peer median of 4.05%, but its 26.2% margin is far above the 15.92% median.
7. Check sales to capital: revenue over invested capital was 0.30, 0.32, 0.34, but 100.65% of invested capital is goodwill, so it says nothing about the cost of new growth. This ratio is not used in the model.
8. Choose what drives the forecast: management's revenue and margin path for 2025-2030 (free cash flow $212.0M to $419.0M), then 2.5% growth with 25.00% reinvestment (2.5% / 10% stable ROIC).

**Result for SolarWinds:** Fundamentals justify roughly zero growth (-0.64% to 1.61%), actual growth is about 5.25% a year and management plans 8.12%; we use management's plan for 2025-2030 and flag it as the main judgment.
Full answers: [lesson-31.md](lesson-31.md) · Walkthrough: [Step 31](walkthrough.md#step-31-how-fast-can-solarwinds-grow-and-has-it-earned-that-growth)

## Lesson 32 — Terminal Value

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Terminal Value** | The value at the end of the explicit forecast, standing in for all cash flows after it because a firm may live forever. Formula: Value = sum for t=1..N of CF(t)/(1+r)^t + Terminal Value/(1+r)^N |
| **Growth period** | The explicit forecast years before the firm reaches stable growth, after which terminal value takes over. |
| **Growth cap (Obey the growth cap)** | The stable growth rate cannot exceed the growth rate of the economy; it can be lower, even negative (the firm slowly disappears). The risk-free rate is a simple proxy for the nominal growth of the economy. Formula: Terminal Value = Expected Cash Flow Next Period / (r - g) |
| **Don't wait too long** | Analysts set growth periods too long. Most growth firms cannot sustain high growth, especially with excess returns, for long. |
| **Competitive advantages** | The key determinant of how long a growth period lasts. Growth creates value only with excess returns, so stronger, more sustainable advantages allow longer value-creating growth, and such firms are rare. |
| **Excess returns** | Return on capital above the cost of capital. Without it, growth does not add value. |
| **Stable growth reinvestment rate** | In stable growth, growth must still be paid for by reinvesting: the rate depends on the stable growth rate and the return on capital earned forever. Formula: Reinvestment Rate = g / ROC (Vale: 2% / 17.25% = 11.59%) |
| **Stable period payout ratio** | The dividend payout consistent with stable growth and ROE. Formula: Payout Ratio = 1 - g / ROE |
| **Be internally consistent** | In stable growth, risk and return inputs must match: betas move toward one, debt ratios toward industry averages, country risk premiums evolve, and excess returns fade toward zero (ROC toward the cost of capital, ROE toward the cost of equity). |
| **Normalized earnings** | An average or typical level of operating income and return on capital over a cycle, used instead of a peak or trough year (Vale's normalized ROC: 17.25%). |
| **Sleight of hand (capex = depreciation)** | The common shortcut that stable firms only make maintenance capex and need no working capital implies zero reinvestment and therefore zero growth in operating income, contradicting any positive stable growth rate. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |

### What the project asked

1. When (in what year) will your firm be a mature firm (where you can estimated terminal value)?
2. What will your firm's growth rate be in perpetuity after that point in time?
3. What return on and cost of capital would you give your firm, when it becomes a mature firm?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Net retention rate (subscription) and large customers | 99% (2024), 97% (2023); customers over $100,000 of annual recurring revenue (ARR) 1,148 vs 979; total ARR $729.0M, up 6.6% | FY2024 10-K MD&A (`sources/filings/swi-10k-fy2024.md`); ledger facts `net-retention-subscription`, `customers-over-100k-arr`, `total-arr-2024` |
| EBIT margin vs peers | 26.2% vs peer median 15.9% | FY2024 10-K; peers' filings (`sources/peer-filings/peer-facts-2025-02-05.md`); ledger `peers[].ebit_margin` |
| 2023 market check | 13 parties approached; three indications withdrew; Party A about $14.00 revised to $13.00 | DEFM14C, Background of the Merger; ledger fact `market-check-2023` |
| Management forecast 2025-2030, including 2030 FCFF | 2030 revenue $1,273.0M, EBIT margin 40.14%, FCFF $419.0M | DEFM14C, Certain Company Financial Forecasts; ledger `forecast.years` |
| 2030 detail | EBIT $511M, D&A $25M, capex $27M, deferred revenue change +$46M | DEFM14C forecast summary table; ledger fact `forecast-2030-detail` |
| Terminal growth and stable ROIC | 2.5%; 10% | Judgment: Goldman Sachs 2%-3% and Jefferies 2.5%-3.5% perpetuity ranges in the DEFM14C; ledger `market.terminal_growth`, `forecast.stable_roic` |
| Cost of capital | 10.23% | Model-output.md §1 |
| Terminal value under two methods | $3,808.9M (consistent reinvestment) vs $5,552.5M (grow final-year FCFF) | Model-output.md §6 |
| 2030 discount factor and shares | 0.5573; 171.6M | Model-output.md §6; ledger `company.shares_basic` |
| Goodwill | $2,363.2M | FY2024 10-K balance sheet; ledger `company.goodwill` |

### Steps to complete the assignment

1. Choose the length of the growth period: six years, 2025-2030, which is management's own forecast window (`forecast.growth_period_years` = 6). Evidence for durability: subscription retention of 99% and 97%, customers over $100,000 up from 979 to 1,148, no exodus after the 2020 SUNBURST attack, and a 26.2% EBIT margin against a 15.9% peer median. Evidence against a longer period: growth of 5.0% is near the peer median of 4.1%, and three sponsors dropped out in November 2023 doubting the subscription transition. Judgment: the moat defends but does not expand, so no more than six years.
2. Set perpetual growth at 2.5%, below the 4.43% risk-free rate and between Goldman Sachs' 2%-3% and Jefferies' 2.5%-3.5% ranges.
3. Set the stable return on capital at 10% and keep the cost of capital at 10.23%. Judgment: SolarWinds earned about 6.7% on book capital, but $2,363.2M of that capital is goodwill, so 10% gives no credit for excess returns.
4. Compute the consistent terminal reinvestment rate: growth / stable ROIC = 2.5% / 10.00% = 25.00%.
5. Check for the trap (reinvesting nothing while growing). Management's 2030 FCFF is $419.0M; EBIT of $511M is $383.3M after 25% tax, so FCFF exceeds after-tax EBIT by about $35.7M, a reinvestment rate near -9%. The gap comes from a +$46M deferred revenue change and cash taxes near 25%, not from depreciation. The forecast does not avoid the trap.
6. Compare terminal values: $3,808.9M with consistent reinvestment against $5,552.5M if the final-year FCFF is grown at g. The $1,743.6M difference, at the 2030 factor of 0.5573 over 171.6M shares, is about $5.67 a share, and would lift $13.00 to $18.67.
7. Test the stable ROIC. Value per share is $13.00 at 10%, $13.10 at 10.23%, $13.69 at 12%, $14.38 at 15%, $15.07 at 20% and $15.75 at 30%. Even 30% stays below $18.67.
8. Answer the project questions. Mature in 2030; perpetual growth 2.5%; return on capital 10% and cost of capital 10.23%.

**Result for SolarWinds:** Six-year growth period, 2.5% perpetual growth, 10% stable return, giving a terminal value of $3,808.9M (62% of enterprise value); growing management's 2030 cash flow forever instead would give $5,552.5M, a gap of about $5.67 a share.
Full answers: [lesson-32.md](lesson-32.md) · Walkthrough: [Step 32](walkthrough.md#step-32-when-does-solarwinds-stop-growing-fast-and-what-is-it-worth-after-that)

## Lesson 33 — To Value Per Share

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **From Firm Value to Equity Value per Share** | The bridge from the DCF output to a per-share figure: if you discounted FCFF, add cash and non-operating assets, subtract debt, subtract the value of equity options, then divide by shares. Formula: Value of operating assets + Cash & Near Cash + Value of minority cross holdings - Debt = Value of equity; - Value of equity options = Value of equity in common stock; / Number of shares |
| **Value of operating assets** | The present value of the cash flows from the business itself, before adding cash, cross holdings or other assets. |
| **Value of Cash** | Cash is not automatically worth its face value; the market may discount or add a premium to it depending on how well the firm will use it (return on capital versus cost of capital and the country). |
| **Cross holdings** | Stakes in other firms: minority passive (only dividends shown), minority active (share of equity income shown) or majority active (statements consolidated). They must be valued, not ignored or counted at book. |
| **Market Value Solution** | Value cross holdings with the traded market capitalizations of the subsidiaries, at the risk of importing market mistakes. |
| **Relative Value Solution** | When there are too many holdings or too little information, convert book values of holdings using the average price-to-book ratio of the subsidiaries' sector. |
| **Minority interests** | The part of a consolidated subsidiary that belongs to outside owners rather than the parent; it is subtracted from firm value. |
| **Unutilized assets** | Assets not producing cash flows in the valuation, such as vacant land. Value them at market and add them. |
| **Overfunded pension plans** | A defined benefit plan whose assets exceed liabilities can count as value, but collective bargaining may block claims, withdrawals are heavily taxed, and the asset must not be counted twice. |
| **Double counting** | If you count the income from an asset in the cash flows, you cannot also add its market value. |
| **Equity options (employee options)** | Options given to managers and employees. Options already outstanding are valued (allowing for dilution, vesting and early exercise) and subtracted from equity value; the result is divided by actual shares outstanding. |
| **Expected future option and restricted stock issues** | Future grants are treated as an operating expense: forecast their value as a percent of revenues, reduce operating income and cash flows, and discount as usual. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |

### What the project asked

1. How much cash does your firm have? Would you attach a discount or premium to it?
2. Does your firm have minority cross holdings? What is their value?
3. Does your firm have majority cross holdings? How have you incorporated their value?
4. Have managers in the firm been compensated with equity options or restricted stock? How does that affect your value per share?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Cash and short-term investments | $259.3M ($251.9M cash + $7.5M short-term investments) | FY2024 10-K balance sheet (`sources/filings/swi-10k-fy2024.md`); ledger `company.cash` |
| Revolver (undrawn) | $130.0M | FY2024 10-K note 9; ledger `debt.revolver_undrawn` |
| Debt | $1,285.0M (term loan face value plus leases) | FY2024 10-K notes 9 and 7; ledger `company.debt_total` |
| Enterprise value from the DCF | $3,444.3M | Model-output.md §6 |
| Unvested restricted stock units (RSUs) and performance stock units (PSUs) | 9,960,353 RSUs + 2,253,709 PSUs = 12.214M units; 113,430 vested options at $0.98 | FY2024 10-K note 10; ledger `company.options_value` |
| Options and RSU claim | $187.0M | Computed from note 10 at the $15.18 price; ledger `company.options_value` |
| Basic and diluted shares | 171.6M and 174.5M | DEFM14C Written Consent (record date); FY2024 10-K note 11; ledger `company.shares_basic`, `company.shares_diluted` |
| Stock-based compensation | $76.5M | FY2024 10-K cash flow statement; ledger `company.sbc` |
| Minority and cross holdings | None; no noncontrolling interest | FY2024 10-K balance sheet and equity statement |
| Equity value (market) | $2,604.9M | Computed in lesson 29; ledger `company.equity_value` |

### Steps to complete the assignment

1. Decide how to value cash. 2023-2024 after-tax returns on book capital (about 4.8% and 6.7%) are below the 10.23% cost of capital, which argues for a discount. But the company repaid $664.4M of debt in 2022 and paid a $168.2M dividend in 2024, cash was $259.3M at the end of 2024 against $289.2M in 2023 (not hoarded), and the $130.0M revolver is undrawn. Cash is 10% of the $2,604.9M equity value; a 31% discount (the lecture's example) would remove $80.4M, or $0.47 a share. Judgment: value cash at face, $259.3M, as the two banks' fairness analyses did.
2. Check for cross holdings: there is no equity-method investment, no investment securities beyond the $7.5M already counted in cash, no N-able stake after the July 2021 spin-off, and no noncontrolling interest. Value: $0.
3. Value the options claim: 12.214M units valued at the $15.18 unaffected price (no exercise price) plus 113,430 vested options at intrinsic value gives $187.0M.
4. Build the bridge from enterprise value to equity: $3,444.3M - $1,285.0M debt + $259.3M cash = $2,418.6M; less the $187.0M claim = $2,231.6M.
5. Divide by basic shares: $2,231.6M / 171.6M = $13.00.
6. Compare with the diluted shortcut: $2,418.6M / 174.5M = $13.86, which is $0.86 higher. It is higher because the diluted count adds only 2.9M shares (1.7%) while the units outstanding are 12.214M (7.1% of basic shares). No double counting: stock compensation is already expensed in EBIT and in management's cash flows, so the $187.0M covers only grants already made.
7. Answer the project questions. Cash: $259.3M, no discount or premium. Minority cross holdings: none. Majority holdings: none, no minority interest to subtract. Equity compensation: yes, mainly RSUs and PSUs; the $187.0M claim moves value per share from $13.86 to $13.00, and stock compensation is 9.6% of revenue ($76.5M).

**Result for SolarWinds:** Cash is taken at face ($259.3M), there are no cross holdings, and subtracting the $187.0M stock-unit claim and dividing by 171.6M basic shares gives $13.00 a share, against $13.86 on the diluted shortcut.
Full answers: [lesson-33.md](lesson-33.md) · Walkthrough: [Step 33](walkthrough.md#step-33-how-do-we-get-from-the-value-of-the-business-to-the-value-of-one-share)

## Lesson 34 — Value of Control

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **High Growth Phase / Transition Phase / Stable Growth Phase** | The three stages used in Disney's valuation: five years of high growth, five years in which return on capital, reinvestment rate and debt ratio move linearly to stable levels, then stable growth forever after year 10. |
| **Status quo value** | The value per share of the firm run by existing management with current investing, financing and dividend policies in place (Disney: $62.56). |
| **Optimal value** | The value per share if investing, financing and dividend policy are changed to the best feasible levels (Disney restructured: $74.91). |
| **Value of control** | The difference between the optimal value and the status quo value, which is what control of a firm is worth. Formula: Value of control = Optimal value - Status quo value (Disney: $74.91 - $62.56 = $12.35 per share). The slides' tag line: control is not always worth 20%. |
| **Ways of changing value** | The levers that move value from the status quo to the optimal: better investments (return on capital), reinvestment, optimal debt ratio and cost of capital, and dividend/cash policy. |
| **Poorly managed firms** | The value of control is greater at poorly managed firms than at well-run ones, since there is more value to gain from changing management. |
| **Expected value of control** | The probability that management changes times the value of control. The market price should embed this. |
| **Governance and price** | If governance is so weak that management cannot be changed, expected control value goes to zero and the stock converges on the status quo value; in an acquisition or activist battle, the price approaches the optimal value. |
| **Reinvestment rate = g/ROC (stable)** | Used to set the stable-phase reinvestment in the Disney inputs: 2.5% growth / 10% return on capital = 25%. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |

### What the project asked

1. What is the status quo value of your firm?
2. If you were running this firm, what would you change about the way the firm is run (in terms of investing, financing and dividend decisions)?
3. What is the value of your firm with these changes made?
4. What is the likelihood that this change will happen?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Management forecast 2025-2030 | Revenue $832.0M to $1,273.0M; EBIT margin 32.69% to 40.14%; FCFF $212.0M to $419.0M | DEFM14C, Certain Company Financial Forecasts (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger `forecast.years` |
| Cost of capital, levered beta | 10.23%; 1.6714 | Model-output.md §1 |
| Terminal growth and stable ROIC | 2.5%; 10% | Judgment, see lesson 32; ledger `market.terminal_growth`, `forecast.stable_roic` |
| DCF results | Present value of cash flows $1,321.6M; present value of terminal value $2,122.7M; enterprise value $3,444.3M | Model-output.md §6 |
| Debt, cash, options claim, basic shares | $1,285.0M; $259.3M; $187.0M; 171.6M | FY2024 10-K notes 9, 7, 10; DEFM14C; ledger `company.*` |
| Unaffected and deal prices | $15.18; $18.50 | DEFM14C, Goldman Sachs opinion and Per Share Merger Consideration |
| Banks' DCF ranges and discount rates | Goldman Sachs $14.30-$23.70 (9%-11%); Jefferies $14.70-$19.70 (10.70%-11.70%) | DEFM14C, Goldman Sachs and Jefferies opinions; ledger facts `gs-dcf-range`, `jefferies-dcf-range` |
| Optimal debt ratio and its value | 21% (vs 33.03%); cost of capital 10.03%; enterprise value $3,533.4M; $13.52 a share | Model-output.md §3 and §6 |
| Owners and board | Silver Lake 36.56%, Thoma Bravo 29.79%; three of nine directors are Silver Lake designees | 2024 proxy; ledger `governance.controlling_holders`, `governance.board` |
| Buyer's financing | $2,225M first lien, $525M second lien, $200M revolver | Merger closing 8-K Item 1.01 (`sources/deal-docs/swi-8k-2025-04-16-merger-closing.md`); ledger fact `new-debt-2025` |

### Steps to complete the assignment

1. Write the status-quo story: a mature IT-monitoring business finishing its move to subscriptions; revenue $832.0M (2025) to $1,273.0M (2030), 8.12% a year against 5.0% history; EBIT margin 32.69% to 40.14% (26.2% in 2024); free cash flow $212.0M to $419.0M; reinvestment forced to 25.00% after 2030; cost of capital 10.23%.
2. Add up the DCF: present value of 2025-2030 cash flows $1,321.6M + present value of terminal value $2,122.7M = enterprise value $3,444.3M.
3. Bridge to a share price: $3,444.3M - $1,285.0M debt + $259.3M cash = $2,418.6M; less $187.0M options claim = $2,231.6M; over 171.6M basic shares = $13.00.
4. Compare with prices and banks: $13.00 is 0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price, and below both banks' DCF ranges. Jefferies grew terminal-year cash flow at 2.5%-3.5%, which with our rates gives a terminal value of $5,552.5M against our $3,808.9M, about $5.67 a share, or $18.67.
5. Price the financing lever (the only lever the model can compute). Optimal debt is 21% against 33.03%; at the optimal cost of capital of 10.03% enterprise value is $3,533.4M and value per share is $13.52, a gain of $0.52, or $89.1M ($3,533.4M - $3,444.3M). Two other measures exist on different bases: $144.4M capitalized savings ($0.84) and $220.3M by adjusted present value ($1.28). Getting there means repaying $468.1M of debt, more than the $259.3M of cash.
6. Treat the other three levers as judgment, with no extra credit: operations (the plan already has a 40.14% margin), reinvestment and return (the DCF already assumes 10% after 2030, no excess return), and growth period (six years; retention of 97%-99% does not support more).
7. Compare with the deal premium: $18.50 is $3.32 above $15.18 (22%, about $569.7M). The financing lever explains about one-sixth of it ($0.52 / $3.32).
8. Judge likelihood of change. Silver Lake and Thoma Bravo hold 66.35%, so no other holder can force change; in 2024 they chose a special dividend over repaying debt. The buyer's two term loans of $2,750M are more than double today's $1,285.0M.
9. Answer the project questions. Status-quo value: $13.00 a share, enterprise value $3,444.3M. What I would change: financing first (repay about $468.1M), then dividends (do not pay out more than FCFE while debt is above optimum; 2024 returned $194.7M against $127.0M), then raise the bar for growth spending. Value with changes: $13.52. Value of control: $0.52 a share. Likelihood: low for the financing change under the existing owners.

**Result for SolarWinds:** The status-quo DCF is $13.00 a share (0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price); moving to the optimal 21% debt adds only $0.52, giving $13.52.
Full answers: [lesson-34.md](lesson-34.md) · Walkthrough: [Step 34](walkthrough.md#step-34-what-is-solarwinds-worth-as-it-is-run-today-and-what-would-a-better-owner-add)

## Lesson 35 — Relative Valuation

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **Relative valuation (essence)** | Value an asset by comparing the market's pricing of comparable assets, after standardizing prices into multiples and controlling for differences between firms. |
| **Price multiple** | A standardized price: market value divided by a common variable such as earnings, book value, sales or EBITDA, so that firms of different size can be compared. |
| **Four steps to deconstructing multiples** | Define the multiple, describe it (its distribution across the market), analyze it (the fundamentals that drive it) and apply it (choose comparables and control for differences). |
| **Definitional tests** | Is the multiple consistently defined (numerator and denominator belong to the same claimholders: equity value over equity earnings or book value, firm value over firm earnings) and uniformly estimated across the comparable firms? |
| **PE ratio (trailing PE, forward PE)** | Price per share divided by earnings per share. Trailing PE uses the last 12 months of EPS; forward PE uses forecast EPS. Formula: PE = Market Price per Share / Earnings per Share |
| **Enterprise Value/EBITDA** | Firm value (market equity plus debt, less cash) divided by operating earnings before interest, taxes, depreciation and amortization. Cash is netted out because it is not part of the operating business. |
| **Descriptive tests** | Look at the average, standard deviation, median and outliers of the multiple across the market, and how it changed over time. Distributions are skewed, so the median is often a more reliable benchmark, and dropping outliers can bias the estimate. |
| **Analytical tests** | Ask what fundamentals drive the multiple (growth, risk, cash flow patterns, from a DCF model) and how it responds to them. The relationship is seldom linear, so twice the growth does not mean twice the PE. |
| **PE ratio fundamentals** | From the dividend discount model. Formula: PE = Payout Ratio x (1 + g) / (r - g); with an FCFE model, replace the payout ratio with FCFE/Earnings. |
| **Comparable firm** | Damodaran defines it by similar risk, growth and cash flow characteristics, not by sector; it is impossible to find an exactly identical firm, so differences must be adjusted for. |
| **PEG ratio** | PE ratio divided by expected growth, used to adjust PE for differences in growth among comparables. |
| **Price/Book (PBV) regression** | A regression of price-to-book ratio on ROE and the Tier 1 capital ratio across European banks, used to predict a bank's PBV and judge whether it is cheap (Deutsche Bank: predicted 1.003 vs actual 0.67). Formula: PBV = 0.48 + 1.58 ROE + 3.55 Tier 1 capital ratio |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |
| **SEC structured financial data (XBRL)** | The numbers from every 10-K and 10-Q in machine-readable form, tagged line by line (revenue, operating income, debt and so on). | Pulling the same figures for many companies at once, such as a peer group, without reading each filing. | SEC's free company-facts API (data.sec.gov) or the Financial Statement Data Sets on sec.gov. |

### What the project asked

1. What multiples of earnings, book value and revenue does your company trade at?
2. Which of these multiples is the best one to price your company on?
3. What are the "comparable" firms that you would use in pricing your company?
4. Based upon the multiple and comparables, what price would you attach to your company?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Equity value, debt, cash | $2,604.9M; $1,285.0M; $259.3M | DEFM14C (price, shares); FY2024 10-K balance sheet and notes; ledger `company.*` |
| Enterprise value | $3,630.6M | Computed; model-output.md §7 |
| Revenue, standardized EBITDA, net income, book equity | $796.9M; $282.8M; $111.9M; $1,400.7M | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `company.*` |
| Peer set (8 companies) | Akamai, NetApp, NetScout, OneSpan, Open Text, Progress, Qualys, Teradata | Peers' FY2024 filings via SEC XBRL, priced 2025-02-05 (`sources/peer-filings/peer-facts-2025-02-05.md`); the set is from Jefferies' fairness opinion in the DEFM14C |
| Peer median multiples | EV/revenue 3.32x; EV/EBITDA 16.39x; P/E 26.57x; P/B 4.58x | Model-output.md §7 |
| Peer growth, EBIT margin, debt ratio | Growth median 4.1%; margin median 15.92%; debt ratio median 11.7% | Same peer file; ledger `peers[]` |
| Options and RSU claim and basic shares | $187.0M; 171.6M | FY2024 10-K note 10; DEFM14C; ledger `company.options_value`, `company.shares_basic` |
| Goodwill | $2,363.2M | FY2024 10-K balance sheet; ledger `company.goodwill` |
| Company-adjusted EBITDA (not used) | $384.7M | FY2024 10-K MD&A non-GAAP reconciliation; ledger `company.ebitda_adjusted` |

### Steps to complete the assignment

1. Compute SolarWinds' enterprise value: equity $2,604.9M + debt $1,285.0M - cash $259.3M = $3,630.6M.
2. Compute its multiples at $15.18: price/earnings 23.28x ($2,604.9M / $111.9M); price/book 1.86x (book equity $1,400.7M); EV/revenue 4.56x ($3,630.6M / $796.9M); EV/EBITDA 12.84x ($3,630.6M / $282.8M).
3. Set the comparables: the eight US-listed companies in Jefferies' fairness-opinion set that file with the SEC. Check Point, TeamViewer and Trend Micro were dropped (non-US accounting) and Informatica was dropped (acquired, no price). Datadog, Dynatrace and PagerDuty were rejected because their growth would make their multiples a price for growth SolarWinds does not have. Keep definitions consistent (debt includes leases, stock compensation stays a cost).
4. Compare with the peer medians: EV/revenue 4.56x vs 3.32x (premium); EV/EBITDA 12.84x vs 16.39x (discount, six peers); P/E 23.28x vs 26.57x (discount, seven peers); P/B 1.86x vs 4.58x (discount). The pattern reflects a 35.5% EBITDA margin against a peer median of 22.5%.
5. Choose the best multiple: EV/EBITDA. Revenue multiples ignore peer margins ranging from -18% to 31%; price/book is distorted by $2,363.2M of buyout goodwill and by peers' buybacks; price/earnings depends on debt mix and one-time items (2022 had an $891.1M impairment). Weakness: only six peers.
6. Test whether "cheap" is deserved. Growth does not explain it (5.0% vs a peer median of 4.1%); risk may (debt is 33.03% of capital against a 11.7% peer median; levered beta 1.6714). A side regression of EV/revenue on EBIT margin across the eight peers gives EV/revenue = 2.45 + 10.43 x margin, R-squared 0.42; SolarWinds' 26.2% margin predicts 5.18x against 4.56x actual, an implied $17.00 a share. This is a sanity check on eight points, not an estimate.
7. Convert to a price using the same bridge as the DCF (enterprise value - debt + cash - $187.0M claim, over 171.6M shares): at 16.39x EBITDA the value is $19.95; at 3.32x revenue it is $8.34.
8. Answer the project questions. Multiples: P/E 23.28x, P/B 1.86x, EV/revenue 4.56x, EV/EBITDA 12.84x. Best multiple: EV/EBITDA. Comparables: the eight peers above. Price: $19.95 a share, with a range of $16 to $20. The DCF ($13.00) disagrees mainly because a multiple of EBITDA does not ask how much of it must be reinvested.

**Result for SolarWinds:** SolarWinds trades at a premium on revenue (4.56x vs 3.32x) but a discount on EBITDA (12.84x vs 16.39x), so peer-median EV/EBITDA implies $19.95 a share (EV/revenue implies $8.34).
Full answers: [lesson-35.md](lesson-35.md) · Walkthrough: [Step 35](walkthrough.md#step-35-how-does-the-market-price-similar-companies-and-where-does-solarwinds-fall)

## Lesson 36 — Final Thoughts

### Key terms

| Term | Plain-language definition |
|------|---------------------------|
| **I. What are the conflicts of interest?** | Managers, inside stockholders, outside stockholders, lenders, the board, employees, customers, regulators and society want different things, so the objective of maximizing value is bent by who controls the firm. Outside stockholders want stock price plus dividends; managers want compensation and marketability; lenders want to be repaid. |
| **II. Risk and the marginal investor** | Risk is measured through the investor who sets the price at the margin (the diversified, well-informed trader), not through every holder, which is why beta and diversification drive the cost of equity. |
| **III. Risk profiles and costs of equity** | A firm's risk profile (its businesses, operating leverage and financial leverage, captured in bottom-up betas) with the risk-free rate and equity risk premium gives its cost of equity; cost of capital then blends it with the cost of debt. |
| **IV. The quality of investments: the firm view** | Investment principle: invest only in assets that earn more than the minimum acceptable hurdle rate; judge quality by comparing return on capital with cost of capital across the firm. |
| **V. The trade off on debt** | Debt has benefits (tax deductibility of interest and added discipline on managers) and costs (expected bankruptcy cost, agency costs between equity and lenders, and loss of flexibility). |
| **VI. The optimal mix of debt and equity** | Financing principle: the debt ratio that minimizes cost of capital and so maximizes firm value, balancing the trade-off in point V. |
| **VII. Getting to the optimal mix** | How quickly (an under-levered firm risks a hostile takeover, an over-levered firm risks bankruptcy) and how: recapitalizations (borrow and buy back stock, or issue equity and retire debt) or investments funded mainly by debt or by equity. |
| **VIII. The right kind of financing** | Match the type of debt to the assets and cash flows it funds (maturity, currency and so on) to lower default risk and the cost of capital. |
| **IX. Measuring potential dividends** | Dividend principle: if you cannot find investments that earn the minimum acceptable rate, return the cash to owners. Measure what could be paid (FCFE) and compare it with what is paid. |
| **X. Valuation: match up cash flows and discount rates** | Value follows from cash flows, growth, risk and the length of the growth period; cash flows to equity are discounted at the cost of equity and cash flows to the firm at the cost of capital. Ties the three principles back to first principles. |

### Key documents

| Document | What it is | When it's used | Where it's normally found |
|---|---|---|---|
| **10-K (annual report)** | The company's official yearly report to the SEC: audited financial statements, notes that explain them, risks, business description and management's discussion of results. | The main source for any valuation: earnings, debt, leases, taxes, share counts and segment data. Filed within 60–90 days of year-end. | SEC EDGAR (sec.gov/edgar, search by company name or ticker), or the company's investor-relations website. |
| **Proxy statement (DEF 14A)** | The document sent to shareholders before the annual meeting: who is on the board, how executives are paid, who owns the shares and what shareholders are voting on. | Governance questions: who controls the company, whether the board is independent, how pay is tied to performance. | SEC EDGAR (filing type DEF 14A), usually filed a month or two before the annual meeting. |
| **8-K (current report)** | A short filing a company must make within four business days of a major event: a merger, a new loan, a leadership change, a cyberattack, the close of a deal. | Pinning down when something happened and its terms, between annual reports. | SEC EDGAR (filing type 8-K), and usually as a press release on the investor-relations site. |
| **Merger information statement (DEFM14C)** | The document sent to shareholders when a merger is approved by written consent of the controlling holders, so no vote is held. It covers the background of the sale, the fairness opinions, management's forecasts and executive payouts. | Any analysis of a buyout: the deal price, how it was negotiated, the forecasts the board relied on. When there is a shareholder vote, the equivalent is a merger proxy (DEFM14A). | SEC EDGAR (filing type DEFM14C or DEFM14A). |
| **Fairness opinion** | A bank's letter to the board saying the deal price is fair to shareholders, with a summary of the valuation work behind it: comparable companies, discounted cash flow, precedent deals. | Benchmarking your own valuation, peer set and discount rate against the bankers'. | Summarized inside the merger proxy or information statement; the full letter is usually an annex to it. |

### What the project asked

1. What is the narrative that you would use to describe your company, as its run today?

### Information required and where we got it

| Information | SolarWinds value | Where we got it |
|---|---|---|
| Ownership and board | Silver Lake 36.56%, Thoma Bravo 29.79% (66.35%); 3 Silver Lake designees on the board | 2024 proxy (`sources/filings/swi-def14a-2024.md`); ledger `governance.*` |
| Sponsors' vote and consent | 111,564,519 shares, about 65% of votes, written consent 2025-02-07; no vote held | DEFM14C, Written Consent (`sources/deal-docs/swi-defm14c-2025-merger.md`); ledger fact `sponsor-voting-power-2025-02` |
| Adviser fees and conflicts | Goldman Sachs fee about $42M (contingent on closing); Jefferies $6.25M and about $39M from the sellers' firms | DEFM14C, fairness opinion fee paragraphs; ledger fact `adviser-fees-and-conflicts` |
| Change-of-control payouts | $38.96M for three executives; CEO $22.99M | DEFM14C, Golden Parachute Compensation; ledger `governance.change_of_control_payouts` |
| 2023 market check | 13 parties approached; highest indication Party A $13.00, revised from about $14.00 | DEFM14C, Background of the Merger; ledger fact `market-check-2023` |
| Returns, financing, payout | ROIC 6.66% (2.69% in 2022 ex impairments) vs cost of capital 10.23%; debt 33.03% vs optimum 21%; returned $194.7M vs FCFE $127.0M | Computed in lessons 27 to 34; model-output.md §1, §3, §5, §8 |
| Revenue, margin, retention, goodwill | $796.9M; 26.2%; 97%-99%; $2,363.2M | FY2024 10-K (`sources/filings/swi-10k-fy2024.md`); ledger `company.*` |
| DCF and multiples results | $13.00; $18.67 with the other terminal value; $19.95 at 16.39x EBITDA; $8.34 at 3.32x revenue | Model-output.md §6 and §7 |
| Banks' DCF ranges, new debt, price record | Goldman Sachs $14.30-$23.70; Jefferies $14.70-$19.70; $2,750M term debt; $15.18 was the 52-week high | DEFM14C opinions; merger closing 8-K; ledger facts `gs-dcf-range`, `jefferies-dcf-range`, `new-debt-2025`, `unaffected-price-record` |

### Steps to complete the assignment

1. Identify whose interests drove the big decisions: stockholders, and specifically the two sponsors who held 66.35%. Decisions in the ledger years: the 2021 N-able spin-off and $1.50 special dividend ($237.2M), the 2022 repayment of $664.4M of debt, the $1.00 special dividend ($168.2M) in April 2024, and the February 2025 sale at $18.50. The sharpest conflict is inside the stockholder group: the sponsors, who control, against the public holders, who do not.
2. Check the sale process: the sponsors' written consent (about 65% of votes) approved the merger the day it was signed. Michael Widmann, a Silver Lake designee, sat on the three-person committee. Goldman Sachs' $42M fee depends on closing and Jefferies earned about $39M from the sellers' firms. Managers were due $38.96M on change of control. Lenders were repaid because a change of control is an event of default. Open question: was $18.50 the best price? The 2023 check approached 13 parties and ended with no bid; the highest indication was Party A's $13.00.
3. Apply the three first principles. Investment: ROIC 6.66% (2024) against a cost of capital of 10.23%, so it did not clear the hurdle. Financing: debt 33.03% against an optimum of 21%, with a synthetic B- rating at 1.85x coverage, so it was not near optimal. Payout: with returns below cost, cash should go back, and it did, but with debt above optimum debt should be repaid first; in 2024 it returned $194.7M against FCFE of $127.0M.
4. Write the narrative: IT monitoring software customers rarely leave ($796.9M revenue, 26.2% EBIT margin, 97%-99% retention, about 5% growth); bought by two private equity firms in 2016 and listed in 2018; the buyout left $2,363.2M of goodwill, so book return is about 6.7% against 10.23%; it spun off N-able, repaid debt, paid two special dividends and agreed to sell for $18.50 cash to Turn/River Capital. Management's plan more than doubles EBIT by 2030 ($511M against $208.4M) and treats cash flow as growing forever without reinvestment. Our DCF does not accept that.
5. Compare the DCF with the prices: $13.00 is 0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price. The premium over the unaffected price is $3.32, or 22%.
6. Explain the gap. Growing management's 2030 cash flow forever ($5,552.5M of terminal value) instead of reinvesting 25% ($3,808.9M) is worth about $5.67 a share and would put the DCF at $18.67. The deal price is what the plan is worth if SolarWinds can grow without reinvesting.
7. Add the other benchmarks: Goldman Sachs $14.30-$23.70 and Jefferies $14.70-$19.70 bracket $18.50. Peer-median EV/EBITDA of 16.39x gives $19.95 and EV/revenue of 3.32x gives $8.34. The deal's enterprise value is $4,200.3M: 14.85x standardized EBITDA of $282.8M against the 16.39x median, and 5.27x revenue against 3.32x. The financing lever is worth $0.52 a share (also $0.84 and $1.28 on other bases), so the premium is not explained by better management but by price paid for the plan's cash flows and the buyer's $2,750M of term debt.
8. State the verdict: for a public holder $18.50 was a good price. It is above our $13.00, above every price in the unaffected record ($15.18 was the 52-week high), above the highest 2023 indication ($13.00) and inside both banks' ranges. The case for holding out is belief in management's 2030 cash flows, which we do not hold. What remains open is whether another buyer would have paid more.

**Result for SolarWinds:** The course-method DCF is $13.00 a share, 0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price; one assumption (no reinvestment after 2030) is worth about $5.67 a share and reproduces the deal price ($18.67), so $18.50 was a good price for a public holder.
Full answers: [lesson-36.md](lesson-36.md) · Walkthrough: [Step 36](walkthrough.md#step-36-was-1850-a-good-price-and-what-is-the-story-of-solarwinds)
