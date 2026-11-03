---
title: "SolarWinds Corporation — Corporate Finance Assessment and Valuation"
status: draft
owner: weprintmoney
created: 2026-11-01
last_updated: 2026-11-03
---

# SolarWinds Corporation — Corporate Finance Assessment and Valuation

> Synced from the final Google Doc on 2026-11-03. Lines starting with ❓ are questions for the professor, marking where the project departs from the course guidance. The earlier version with the analysis of the Turn/River deal is in [drafts/](drafts/).

## Executive summary

*I am basing this analysis of SolarWinds on public data from **February 5, 2025**. This was the last normal day of stock trading before Turn/River Capital announced they were buying the company on February 7. SolarWinds has since been delisted, making the data required for an accurate current valuation inaccessible.*

SolarWinds was a mature, cash-generating public software company run for the benefit of two private-equity owners. Silver Lake and Thoma Bravo (the sponsors) held two-thirds of the shares, chose the directors that mattered and approved the company’s sale without a public vote.

| Value per share on management's plan (DCF) | $16.13 |
| :---- | :---- |
| Value per share at the optimal debt ratio | $16.35 |
| Market price on February 5, 2025 | $15.18 |
| Deal price | $18.50 |
| Cost of capital: 2025–2030 / after 2030 | 10.23% / 8.23% |
| Return on invested capital, FY2024 | 6.66%, on a capital base that is almost all buyout goodwill |
| Debt ratio: actual / optimal | 33% / 21% |

- **Does well:** It keeps customers: 93.5% of revenue is recurring, subscription net retention was 99% in 2024, and maintenance contracts renewed at 97%. Its loan has the right rate type and maturity for that business.

- **Does poorly:** It earns 6.66% on its capital against a 10.23% cost. It carries more debt than is optimal, 33% against 21%. In 2024 it paid out more cash than it generated, through a $168.2M special dividend, while over-levered.

- **Should do differently:** Repay about $468.1M of debt before returning more cash. Hold new growth spending to a return above the cost of capital.

## 1. Stockholder analysis: who has the power?

![Exhibit 1: ownership](report-exhibits/exhibit-5-ownership.png)

*Exhibit 1: ownership*

**Power lies with the sponsors, not with managers or the public float.** Silver Lake held 36.56% and Thoma Bravo 29.79% at the 2024 proxy, 66.34% together. Officers and directors as a group held 1.95%.

Their control goes beyond ownership. Each sponsor could nominate three directors while it held 20% or more, and the two could jointly name a seventh. Silver Lake used its three nominations. Thoma Bravo's three directors resigned in October 2022 after the Justice Department alleged that their service broke the Clayton Act's ban on interlocking directorates, because Thoma Bravo also sat on the board of Dynatrace, a competitor. Their seats and the joint seat then stayed empty, so the sponsors' designees held three of nine seats although they were entitled to seven of nine. Eight of the nine directors counted as independent under exchange rules, including all three Silver Lake designees. Each sponsor also had to consent to any change of control, so a hostile takeover was impossible. The sponsors approved the deal by written consent on February 7, 2025, with about 65% of the votes. Public shareholders never voted.

**Conflicts of interest.** The sponsors and the public shareholders wanted different things. The sponsors had owned the company since 2016 and wanted an exit, and the 2024 special dividend paid them about two-thirds of $168.2M. The CEO had a conflict of his own: his $22.99M change-of-control package was mostly $19.94M of accelerated equity paid on closing, which tied his reward to completing a deal.

The marginal investor was the diversified institution holding the roughly 34% public float. The sponsors did not set the traded price, so market beta is the right measure of risk.

## 2. Risk and return: how risky is SolarWinds, and what is its hurdle rate?

| Input | Value | Basis |
| :---- | ----: | :---- |
| Risk-free rate | 4.43% | 10-year Treasury, 2025-02-05; the US was rated Aaa, so no default spread |
| Equity risk premium | 4.92% | The course dataset's implied US premium of 4.27% on the 64.82% of revenue earned in the US; 6.11%, the European premium, on the 35.18% earned abroad, which adds 0.65 points. Europe stands in for all foreign revenue because the 10-K gives no regional split and most foreign offices are in Europe; the Western Europe premium alone would lower the cost of equity by about 0.42 points |
| Unlevered beta | 1.22 | Software industry, cash-corrected (course dataset, January 2025) |
| Levered beta | 1.6714 | Relevered at a debt-to-equity ratio of 0.4933 and a 25% marginal tax rate |
| Cost of equity | 12.65% | Risk-free + beta × ERP: 4.43% + 1.6714 × 4.92% |
| Pre-tax cost of debt | 7.11% | The term loan's effective rate, SOFR + 2.75% (FY2024 10-K) |
| After-tax cost of debt | 5.33% | Pre-tax rate × (1 − marginal tax rate): 7.11% × (1 − 25%) |
| Debt ratio, market values | 33.03% | Debt $1,285M; equity 171.6M shares × $15.18 = $2,604.9M |
| Cost of capital | 10.23% | E/V × cost of equity + D/V × after-tax cost of debt: 66.97% × 12.65% + 33.03% × 5.33% |

**Beta.** We use a bottom-up beta rather than a regression beta, for three reasons. A regression would describe a company that no longer exists: any five-year window before February 2025 includes the SUNBURST attack (December 2020), the N-able spin-off (July 2021) and two special dividends, so past returns mix different businesses and capital structures. One company's regression beta is also noisy, while the average of the 333 US software companies in the course dataset is roughly 18 times more precise, the square root of the sample size. And the bottom-up beta measures the business as it is today: SolarWinds reports one segment, so the software industry beta of 1.22 applies to the whole firm, relevered at today's debt.

**Debt** is the loan at face value, $1,235.7M, plus $49.4M of lease liabilities. Deferred revenue of $389.3M is owed in service, not cash. Cloud purchase commitments of $68.4M are payments for a service the company uses. Both are excluded.

**Cost of debt.** No agency rating is disclosed. Interest coverage of 1.85 times (operating income of $208.4M against gross interest expense of $112.4M) implies a synthetic B- rating on the course's table for smaller firms and an 8.85% cost of debt. Interest expense ran above today's rate because the loan's rate fell during 2024 from 9.11% to 7.11%. The 7.11% is a rate set by its lenders, so it is the cost of debt used. The tax rate is the 25% US marginal rate (21% federal plus state), not the effective rate, because interest saves tax at the margin; the 2024 effective rate was negative, an $8.1M tax benefit.

**Market or book weights.** We weight debt and equity at market value, because investors expect a return on what their stake is worth today. The balance sheet shows what was paid in the 2016 buyout, which isn't what the stake is worth now. SolarWinds' book equity is mostly goodwill from that buyout, and the market values the equity at 1.86 times book. Using book values would make debt look bigger: 47.28% of capital instead of 33.03%. Debt is cheaper than equity, so that would lower the cost of capital to 9.19%. But more debt also makes the stock riskier, which raises the cost of equity. Once that's included, the book version lands at about 10.15%, close to our 10.23%.

## 3. Investments: how good are SolarWinds' existing investments?

![Exhibit 2: return on capital](report-exhibits/exhibit-2-return-on-capital.png)

*Exhibit 2: return on capital*

Return on invested capital rose from 2.69% in 2022 to 6.66% in 2024, but stayed below the 10.23% cost of capital every year. In 2024 the shortfall cost $84M of economic value added. Return on equity was 7.99% against a 12.65% cost of equity.

**Why the return is low.** Much of the gap comes from what the return is measured against. Goodwill from the 2016 buyout and later acquisitions makes up all of invested capital (100.65%). So the 6.66% compares profits to the price the buyers paid, not to the assets the business actually runs on.

**How SolarWinds invests.** A typical project is small, steady spending on product development that pays back over years of subscription renewals. The big investments were acquisitions paid for with debt, and the low return reflects those. Whether future projects will pay off is less clear: bidders in a 2023 sale process doubted the move to subscriptions, calling it "early stage."

**R&D classification as expense vs investment.** SolarWinds counts its R&D ($108.6M in 2024) as an expense. Treating it as an investment spread over three years, the course's standard for software, adds $206.2M to capital and $10.5M to operating income. The return barely moves, to 6.53%, because goodwill still makes up most of the capital.

**Without goodwill, the business needs very little capital.** Take out the $2,363.2M of goodwill and the business runs on $191.0M of capital, almost all of it R&D. On that base it earns 87% (61% if R&D is spread over five years). That shows the business is cheap to run. It doesn't show what a new dollar would earn, because SolarWinds has spent its new dollars on acquisitions, and the 6.66% measures those.

**What this means for our valuation.** The 2016 price was too high for what the business earns. Maintenance revenue from older license customers also fell 4.6% in 2024 as they switched to subscriptions.

## 4. Capital structure choices: how is SolarWinds financed?

SolarWinds uses both ends of the debt-equity continuum. From most debt-like to most equity-like:

1.  Operating leases, $49.4M.

2.  A first-lien term loan, $1,235.7M at face, senior, secured and floating-rate.

3.  A $130.0M revolving credit facility, undrawn at year-end.

4.  Options and restricted stock units, worth $187.0M at the market price. The units carry no exercise price, so they are valued at the share price and subtracted from equity value; value per share then divides by basic shares, so dilution is not counted twice.

5.  Common stock: one class, one vote a share, listed in the 2018 IPO.

There is no convertible debt and no preferred stock.

**The trade-off.** Debt saves about $28.1M a year in taxes. Its discipline benefit is small, because managers already answer to the sponsors. Against that, the interest is heavy: cash interest of $104.5M took 55.5% of the $188.3M of operating cash flow in 2024, and that cash flow is already after interest. The rate is floating, so each percentage point costs about $12.4M a year. And the loan had to be refinanced on a sale, which limits flexibility.

On the qualitative weighing, SolarWinds has too much debt.

## 5. Optimal financing: what is the right mix of debt and equity?

![Exhibit 3: cost of capital by debt ratio](report-exhibits/exhibit-1-cost-of-capital-by-debt-ratio.png)

*Exhibit 3: cost of capital by debt ratio*

The cost of capital is lowest, at 10.03%, with 21% debt and an A- rating. This schedule re-estimates the rating and interest rate at each debt ratio. At the actual 33% that method gives a B rating and 10.31%, slightly above the 10.23% in section 2, which uses the loan's actual 7.11% rate. Moving to the optimum saves $10.9M a year, worth $144.4M as a perpetuity growing at 2.5%. SolarWinds carried $468.1M more debt than the optimum.

| Debt ratio | Levered beta | Cost of equity | Rating | Pre-tax cost of debt | Cost of capital |
| :---- | ----: | ----: | :---- | ----: | ----: |
| 0% | 1.220 | 10.43% | AAA | 4.88% | 10.43% |
| 10% | 1.322 | 10.93% | AA | 5.03% | 10.22% |
| 21% (optimum) | 1.463 | 11.63% | A- | 5.38% | 10.03% |
| 30% | 1.612 | 12.36% | B+ | 7.04% | 10.24% |
| 33% (actual) | 1.671 | 12.65% | B | 7.43% | 10.31% |
| 40% | 1.830 | 13.43% | B- | 8.85% | 10.72% |
| 50% | 2.135 | 14.93% | C | 19.93% | 16.44% |

The result holds under other assumptions. Three checks all put the optimum below today's 33%:

- Coverage measured on EBITDA instead of operating income: optimum of 28%.

- A 30% fall in operating income: optimum of 14%.

- Adjusted present value, which weighs debt's tax savings against the expected cost of bankruptcy: optimum of 21%. At today's debt the expected bankruptcy cost (361.6M) outweighs the tax savings (321.2M), so the debt is reducing value. At 21% debt, the tax savings are $204.2M and the bankruptcy cost is $24.6M, and the firm is worth $220.3M more.

The bankruptcy cost rests on a judgment. At the B rating, the chance of default within ten years is 36.8%, and we assume a default would cost 25% of firm value. Direct costs, like lawyers and restructuring, usually run 5–10%. Indirect costs are higher for a software company, because customers hesitate to sign multi-year contracts with a vendor that might fail.

## 6. Financing changes: should SolarWinds move to the optimum, and with what debt?

**Whether and how fast.** SolarWinds should move, but gradually. It cannot be taken over against the sponsors' will, so there is no takeover pressure. There is no near-term bankruptcy threat either: it has $259.3M of cash and an undrawn revolver, its covenant applies only when the revolver is more than 35% drawn, and the loan does not mature until 2030. The best path is to repay debt out of free cash flow to equity, with no special dividends until the ratio nears 21%. At 2024's $127.0M, repaying $468.1M takes about 3.7 years (468.1 ÷ 127.0); using part of the cash balance shortens that. It does not need an equity issue or a recapitalization.

The right type of debt. Debt should match the assets it funds:

| Characteristic | Right for SolarWinds | Actual |
| :---- | :---- | :---- |
| Rate | Floating: annual price increases give it pricing power | Floating, SOFR + 2.75% |
| Maturity | Medium term, four to six years | 5.0 years, one maturity in 2030 |
| Currency | Dollars and euros in proportion to cash flow; at most 35.18% foreign | All US dollars |
| Form | Straight debt | Straight debt, no swaps |

Rate type, maturity and form fit; the problem is size. Two mismatches remain. No debt is in euros, the currency of most of the foreign revenue; a euro tranche could be added at refinancing, once net foreign cash flow is measured, but the filings do not size it. The single 2030 maturity could also be staggered.

## 7. Dividend policy: how does SolarWinds return cash?

SolarWinds has no regular dividend. In five years it paid two special dividends:

- 2021: $237.2M, $1.50 a share, funded by $238.2M of cash N-able paid SolarWinds at its spin-off.

- 2024: $168.2M, $1.00 a share.

Its only other cash return is shares withheld for employees' taxes on vesting stock. In 2024 the dividend was 150.3% of net income. Counting withheld shares, cash returned was 174.0%. The dividend yield was 6.59% at the $15.18 market price.

Against the sector, this is an outlier. Most of the eight peers paid no dividend, and the wider software group paid out 27.22% of earnings. The course's dividend trade-off, the tax cost to shareholders against the signal a dividend sends and the discipline it imposes on managers, cuts against special dividends here: an irregular payment signals nothing and disciplines no one. Against the patterns the course describes, SolarWinds' payments followed no earnings trend and were not sticky. The likeliest driver of the 2024 dividend is the sponsors' preference; with their stakes unchanged from the proxy, about two-thirds of it went to them. That is an inference, not a stated reason. Either way, irregular payments that follow the owners' preference and not earnings are a weak policy for public shareholders.

## 8. Dividend assessment: should SolarWinds return more or less cash?

![Exhibit 4: free cash flow to equity vs cash returned](report-exhibits/exhibit-3-fcfe-vs-cash-returned.png)

*Exhibit 4: free cash flow to equity vs cash returned*

Over 2022–2024, free cash flow to equity totaled −$419.8M against $224.6M returned. The negative total comes from 2022, when the company repaid $664.4M of debt. Years before 2022 include N-able and are not comparable. The years that describe the business today:

- 2023: free cash flow to equity of $59.4M; $18.8M returned.

- 2024: SolarWinds returned $194.7M but generated only $127.0M of free cash flow to equity, so it paid out $67.7M more than it made. Free cash flow to equity = net income + depreciation − capital spending − increase in working capital − net debt repaid: $111.9M + $74.4M − $20.5M − $38.8M − $0 = $127.0M. Cash fell by only $29.9M. Two non-cash items pulled in opposite directions: $76.5M of employee pay was in stock rather than cash, while net income included a $49.0M tax benefit that brought in no cash. The stock pay is what let SolarWinds pay out more than it generated, so part of the dividend was funded by diluting the shareholders who received it.

❓ SolarWinds is delisted, so I can’t run a regression for Jensen’s alpha. Is the proxy’s total shareholder return chart an acceptable stand-in for the stock-return test?

Should shareholders trust SolarWinds with cash? No. On all the capital invested in it, SolarWinds earns 6.66% against a 10.23% cost. Its operating business needs little capital, so new cash idles or goes to acquisitions, and acquisitions are what the 6.66% reflects. Returning cash was right. Paying it out as a dividend while debt sat $468.1M above the optimum was not. SolarWinds should have returned less to shareholders and used the cash to repay debt.

## 9. Valuation: what is SolarWinds worth?

### Discounted cash flow

We value the whole firm, not just the equity, because the debt ratio is not stable: 33% today against a 21% optimum, and an equity valuation would need a forecast of every debt issue and repayment. Cash flows are management's 2025–2030 forecast from the merger information statement, with stock-based compensation charged as an expense:

- Free cash flow to the firm rises from $212.0M in 2025 to $419.0M in 2030.

- Revenue grows 8.12% a year, against 5.0% in 2024 and 5.25% a year over 2022–2024. The operating margin, on the plan's definition (adjusted EBITDA less stock-based compensation and depreciation), rises from about 29% in 2024 to 32.7% in 2025 and 40.1% in 2030. The GAAP margin was 26.2% in 2024, after restructuring, cyber-incident and acquisition costs.

- The record behind the plan: operating income went from a loss of $819.6M in 2022 (after a $906.4M goodwill impairment) to $150.4M in 2023 and $208.4M in 2024; net income from −$929.4M to −$9.1M to $111.9M; free cash flow to the firm about $146M, $191M and $171M, against the plan's $212M for 2025.

- On SolarWinds' own fundamentals (return on invested capital times reinvestment), growth would be about zero. The plan assumes its margin expansion delivers.

❓ SolarWinds’ margins are changing, so the fundamental formula (reinvestment × return on capital) gives about zero growth. The revenue-based model needs a sales-to-capital ratio, and I can’t get a meaningful one because nearly all invested capital is buyout goodwill. So I used management’s six-year forecast from the merger documents and show stress cases at the historical growth rate. Is that acceptable as the status quo story?

❓ Management’s forecast has free cash flow above after-tax operating income every year, so reinvestment is negative. I fixed that in the terminal value by setting reinvestment to growth ÷ return on capital, but left the forecast years as management wrote them. Should I also force positive reinvestment in the forecast years?

**Two costs of capital.** The plan years (2025–2030) are discounted at 10.23%. After 2030, growth is 2.5% a year, below the 4.43% risk-free rate that caps growth forever; since new capital is assumed to earn only its cost, the exact rate barely moves the value. The terminal value uses a stable-period cost of capital. A mature firm's beta moves toward one and its debt toward its optimum, and at that debt ratio it pays the rate its new rating commands:

| Stable-period input | Value |
| :---- | :---- |
| Beta | 1.00: the course's rule for a mature firm, and a fit for a business with 93.5% recurring revenue |
| Cost of equity | 9.35% (risk-free + stable beta × ERP: 4.43% + 1.00 × 4.92%) |
| Debt ratio | 21%, the optimum |
| Pre-tax cost of debt | 5.38%, the A- rate at 21% debt from the section 5 schedule, not today's 7.11% |
| After-tax cost of debt | 4.04% |
| Stable cost of capital | 8.23% |
| Return on new capital | 8.23%, equal to the cost of capital, so growth after 2030 adds no value |
| Reinvestment rate | 30.38% (growth ÷ return on new capital: 2.5% ÷ 8.23%) |

❓ I set the growth period at six years because that’s how long management’s plan runs, not from a competitive-advantage analysis; I then checked it against retention and peer growth. Is it fine to let the forecast’s length set the period if the moat evidence supports it?

❓ My cost of capital, beta and debt ratio jump straight to stable values after 2030. In the Disney valuation we moved each input in linear steps over years 6–10. Should I add a similar transition?

The return on new capital is the judgment that matters. SolarWinds earns 6.66% on all its capital and 6.53% with R&D capitalized, both below its cost of capital, and its marginal dollars have gone into acquisitions. The 87% in section 3 shows how little capital the business runs on, not what the next dollar will earn. Nothing in the record earns a lasting excess return, so none is assumed, and the terminal value is then almost exactly next year's after-tax operating income capitalized at the cost of capital; how much is reinvested and how fast it grows no longer matter. The sensitivity table below prices the case that an excess return exists.

| Bridge | Status quo | At the optimal debt ratio |
| :---- | ----: | ----: |
| Present value of 2025–2030 cash flows | $1,321.6M |  |
| Present value of terminal value | $2,658.2M |  |
| Enterprise value | $3,979.8M | $4,017.7M |
| − Debt | $1,285.0M |  |
| + Cash, at face value: it earns interest at market rates, so no discount; no cross holdings or minority interests | $259.3M |  |
| − Options and restricted stock units | $187.0M |  |
| Value per share (171.6M shares) | $16.13 | $16.35 |

**The terminal-value method.** The simplest method takes the 2030 cash flow and grows it at 2.5% a year forever. That gives $24.96 a share, but it overstates the value. In 2030, SolarWinds spends almost nothing beyond replacing worn-out equipment, and customers prepay $46M more than the year before. Both push cash flow above operating income, so the company looks like it is growing without reinvesting anything. That can't last forever. Growing 2.5% a year when new capital earns its 8.23% cost means reinvesting about 30% of operating income each year. We use that reinvestment instead, which gives $16.13 a share.

**Sensitivity.** The value depends most on two terminal judgments, the return on new capital and the stable beta:

| Return on new capital after 2030 | 8.23% (used) | 10%     | 12%     | 15%     | 20%     |
| :---- | ----: | ----: | ----: | ----: | ----: |
| Value per share                  | $16.13      | $17.32 | $18.25 | $19.18 | $20.10 |

| Stable beta (stable cost of capital) | 0.80 (7.46%) | 1.00 (8.23%) | 1.46 (10.02%): today's business risk relevered at 21% debt |
| :---- | ----: | ----: | ----: |
| Value per share, no excess returns | $17.74 | $16.13 | $13.36 |
| Value per share, 12% return | $21.01 | $18.25 | $14.06 |

**The return on new capital.** After 2030, the question is what SolarWinds will earn on each new dollar it invests. Its record says no more than that dollar costs. It earns 6.66% on its capital (6.53% with R&D capitalized), below its cost of capital, and its new dollars have mostly gone into acquisitions. The 87% in section 3 shows the business needs little capital to run. It doesn't show what a new dollar would earn. So we assume new capital earns exactly its 8.23% cost. Under that assumption, growth adds no value, because reinvesting only to earn your cost of capital creates nothing. The terminal value is then simply next year's after-tax operating income divided by the cost of capital.

**What if the plan is wrong.** The plan carries more of the value than the terminal assumptions do. Rerunning the valuation with revenue growing at the 2022–2024 rate of 5.25% instead of 8.12%, with the same terminal assumptions:

| Case | 2030 revenue | 2030 free cash flow to the firm | Value per share |
| :---- | ----: | ----: | ----: |
| Management's plan: 8.12% growth, margin 32.7% to 40.1% | $1,273.0M | $419.0M | $16.13 |
| Historical growth, plan margins | $1,083.3M | $345.3M | $13.05 |
| Historical growth, margin held at 32.7% | $1,083.3M | $284.7M | $9.89 |
| Historical growth, margin held at 2024's 29.1% on the plan's definition | $1,083.3M | $255.6M | $8.08 |

The margin expansion matters more than the growth. The market price of $15.18 sat between the history-based $13.05 and the plan-based $16.13, nearer the plan. The market had not seen the plan: it was published in the March 2025 information statement, seven weeks after the valuation date.

### Relative valuation

| Multiple                   | SolarWinds | Peer median | Implied value per share |
| :---- | ----: | ----: | :---- |
| Enterprise value / EBITDA  | 12.84x     | 16.39x      | $19.95                 |
| Price / earnings           | 23.28x     | 26.57x      | about $16.24           |
| Enterprise value / revenue | 4.56x      | 3.32x       | $8.34                  |
| Price / book               | 1.86x      | 4.58x       | not used                |

❓ For pricing, I used the fairness opinion’s peer set, narrowed to eight US filers, and excluded high-growth observability companies because their multiples price growth SolarWinds doesn’t have. You argue comparables should be defined broadly by cash flows, growth and risk. Is a curated set like this acceptable with a sample this small?

The peers are the eight US filers in Jefferies' fairness-opinion set: Akamai, NetApp, NetScout, OneSpan, OpenText, Progress, Qualys and Teradata; three foreign filers and the since-acquired Informatica are left out. The EV/EBITDA median rests on the six peers with positive EBITDA, the P/E median on the seven with profits. EV/EBITDA is the best multiple here. It is not distorted by SolarWinds' debt or one-time items. Revenue multiples ignore that peer margins range from −18% to 31%. Price to book is set aside because SolarWinds' book equity rests on buyout goodwill and buybacks have shrunk some peers' equity. The peers grew from −9.3% to 9.6%, apart from OpenText's acquisition-driven 28.6%, so the median is not adjusted for growth. EV/EBITDA gives $19.95 and price to earnings about $16.24, so the market's own pricing puts SolarWinds at $16 to $20, a range that takes in the $16.13 DCF value and sits just above the $15.18 market price.

### Value with changes

![Exhibit 5: value per share by method](report-exhibits/exhibit-4-value-per-share.png)

*Exhibit 5: value per share by method*

Value with changes. The financing change in section 6 raises value to $16.35 a share, a gain of $0.22 ($37.9M). The gain is small because the stable period already assumes the 21% optimum, so only 2025–2030 benefits. The operating changes are not priced separately: the margin expansion is already in management's plan.

Likelihood of change. Under the sponsors it was low. In 2024 they chose a special dividend over repaying debt. Control did change in 2025, when the sponsors sold the company for $18.50 a share, but the buyer added $2,750M of new term loans, more than double the $1,285.0M SolarWinds carried, so the move to the optimal debt ratio did not happen.

## Conclusion

SolarWinds is a steady business with a poor financial structure. Customers stay, and the business needs little capital to run. But it earns less than its cost of capital on the price paid for it, carries about $468M more debt than it should, and in 2024 paid out more cash than it generated. The fix is simple: use free cash flow to repay debt until it is about 21% of capital, pause special dividends until then, and only fund projects that earn more than they cost. On management's plan, the shares are worth $16.13, a little above the $15.18 market price.

| Principle | What SolarWinds does | What it should do |
| :---- | :---- | :---- |
| Objective and governance | Runs for the sponsors; the public float had no vote on the deal | Give the minority a real voice on a change of control |
| Investment | Earns 6.66% against a 10.23% cost of capital on a capital base of buyout goodwill | Hold new spending to a return above the cost of capital |
| Financing | 33% debt against a 21% optimum; the right type of debt, too much of it | Repay about $468.1M from free cash flow to the firm before any special dividend |
| Dividends | Pays out more than it generates, in special dividends, while over-levered | Repay debt before returning more cash |
| Valuation | Worth $16.13 a share on management's plan, 6% above the market price | Worth $16.35 with debt at the optimum; most of the value rests on the plan's margin expansion |

## Sources

SolarWinds Forms 10-K (FY2018, FY2020, FY2023, FY2024), 2024 proxy statement, 2018 IPO prospectus, Forms 8-K (October 2022, February and April 2025) and merger information statement (March 2025, including the Goldman Sachs and Jefferies fairness opinions and management's plan); Damodaran datasets as of January–February 2025; FRED (10-year Treasury, SOFR); peer companies' fiscal-2024 Forms 10-K and February 5, 2025 closing prices; US Department of Justice press release on interlocking directorates (October 19, 2022).
