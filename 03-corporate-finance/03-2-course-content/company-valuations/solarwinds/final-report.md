---
title: "SolarWinds Corporation — Corporate Finance Assessment and Valuation"
status: draft
owner: weprintmoney
created: 2026-11-01
last_updated: 2026-11-03
---

# SolarWinds Corporation — Corporate Finance Assessment and Valuation

> Shortened in the repo on 2026-11-03 to fit the 7–9 page limit, from the Google Doc version of the same day; port back to the Google Doc before submitting. The earlier version with the analysis of the Turn/River deal is in [drafts/](drafts/).

## Executive summary

*I am basing this analysis of SolarWinds on public data from **February 5, 2025**. This was the last normal day of stock trading before Turn/River Capital announced they were buying the company on February 7. SolarWinds has since been delisted, making the data required for an accurate current valuation inaccessible.*

A 2025 date is a requirement, not a preference. After February 7 the stock traded on the $18.50 offer, so any later price, beta or debt ratio would measure the deal, not the business. February 5 is the last date where the market price reflects SolarWinds as an independent company, and it lets us compare our value with the deal price without hindsight in the inputs. The one exception is disclosed in section 9: management's plan was published seven weeks after this date.

SolarWinds was a mature, cash-generating public software company run for the benefit of two private-equity owners. Silver Lake and Thoma Bravo (the sponsors) held two-thirds of the shares, chose the directors that mattered and approved the company's sale without a public vote.

| Value per share on management's plan (DCF) | $15.32 |
| :---- | :---- |
| Value per share at the optimal debt ratio | $16.08 |
| Market price on February 5, 2025 | $15.18 |
| Deal price | $18.50 |
| Cost of capital: years 1–5 / after year 10 | 10.67% / 8.66% |
| Return on invested capital, FY2024 | 6.66%, on a capital base that is almost all buyout goodwill |
| Debt ratio: actual / optimal | 33% / 21% |

- **Does well:** It keeps customers: 93.5% of revenue is recurring, subscription net retention was 99% in 2024, and maintenance contracts renewed at 97%. Its loan has the right rate type and maturity for that business.
- **Does poorly:** It earns 6.66% on its capital against a 10.67% cost. It carries more debt than is optimal, 33% against 21%. In 2024 it paid out more cash than it generated, through a $168.2M special dividend, while over-levered.
- **Should do differently:** Repay about $468.1M of debt before returning more cash. Hold new growth spending to a return above the cost of capital.

## 1. Stockholder analysis: who has the power?

**Power lies with the sponsors, not with managers or the public float.** Silver Lake held 36.56% and Thoma Bravo 29.79% at the 2024 proxy, 66.34% together. Officers and directors as a group held 1.95%.

Their control goes beyond ownership. Each sponsor could nominate three directors, and the two could jointly name a seventh. Thoma Bravo's three directors resigned in October 2022 after the Justice Department alleged an illegal interlock with Dynatrace, a competitor, so the sponsors' designees held three of nine seats although they were entitled to seven. Eight of the nine directors counted as independent, including all three Silver Lake designees. Each sponsor also had to consent to any change of control, so a hostile takeover was impossible. The sponsors approved the deal by written consent on February 7, 2025, with about 65% of the votes. Public shareholders never voted.

**Conflicts of interest.** The sponsors and the public shareholders wanted different things. The sponsors had owned the company since 2016 and wanted an exit, and the 2024 special dividend paid them about two-thirds of $168.2M. The CEO had a conflict of his own: his $22.99M change-of-control package was mostly $19.94M of accelerated equity paid on closing, which tied his reward to completing a deal.

The marginal investor was the diversified institution holding the roughly 34% public float. The sponsors did not set the traded price, so market beta is the right measure of risk.

## 2. Risk and return: how risky is SolarWinds, and what is its hurdle rate?

| Input | Value | Basis |
| :---- | ----: | :---- |
| Risk-free rate | 4.43% | 10-year Treasury, 2025-02-05; the US was rated Aaa, so no default spread |
| Equity risk premium | 4.92% | Weighted by revenue: the US premium of 4.27% on the 64.82% earned in the US, the European premium of 6.11% on the 35.18% earned abroad |
| Unlevered beta | 1.22 | Software industry, cash-corrected (course dataset, January 2025) |
| Levered beta | 1.6714 | Relevered at a debt-to-equity ratio of 0.4933 and a 25% marginal tax rate |
| Cost of equity | 12.65% | Risk-free + beta × ERP: 4.43% + 1.6714 × 4.92% |
| Pre-tax cost of debt | 8.85% | Risk-free + default spread for a synthetic B- rating (interest coverage 1.85x) |
| After-tax cost of debt | 6.64% | Pre-tax rate × (1 − marginal tax rate): 8.85% × (1 − 25%) |
| Debt ratio, market values | 33.03% | Debt $1,285M; equity 171.6M shares × $15.18 = $2,604.9M |
| Cost of capital | 10.67% | E/V × cost of equity + D/V × after-tax cost of debt: 66.97% × 12.65% + 33.03% × 6.64% |

**Beta.** We use a bottom-up beta rather than a regression beta, for three reasons. A regression would describe a company that no longer exists: any five-year window before February 2025 includes the SUNBURST attack (December 2020), the N-able spin-off (July 2021) and two special dividends, so past returns mix different businesses and capital structures. One company's regression beta is also noisy, while the average of the 333 US software companies in the course dataset is far more precise. And the bottom-up beta measures the business as it is today: SolarWinds reports one segment, so the software industry beta of 1.22 applies to the whole firm, relevered at today's debt.

**Debt** is the loan at face value, $1,235.7M, plus $49.4M of lease liabilities. Deferred revenue of $389.3M is owed in service, not cash. Cloud purchase commitments of $68.4M are payments for a service the company uses. Both are excluded.

**Cost of debt.** No agency rating is disclosed, so we estimate one from interest coverage, the course's method: 2024 operating income of $208.4M covered interest expense of $112.4M 1.85 times, which maps to a B- rating and a 4.42% default spread over the 4.43% Treasury, 8.85%. The term loan's own rate is lower, 7.11%, because its spread was reset in July 2024 and it floats on SOFR. Using it instead would lower the cost of capital to 10.23% and raise the value to $16.13 a share, a 3% difference that does not change any conclusion. We prefer the synthetic rate because it reflects what a new lender would charge on 2024 earnings, not the terms of one loan. The tax rate is the 25% US marginal rate, not the effective rate, because interest saves tax at the margin.

**Market or book weights.** We weight debt and equity at market value, because investors expect a return on what their stake is worth today. The balance sheet shows what was paid in the 2016 buyout, which isn't what the stake is worth now. SolarWinds' book equity is mostly goodwill from that buyout, and the market values the equity at 1.86 times book. Using book values would make debt look bigger: 47.28% of capital instead of 33.03%. Debt is cheaper than equity, so that would lower the cost of capital to 9.81%. But more debt also makes the stock riskier, which raises the cost of equity. Once that's included, the book version lands at about 10.8%, close to our 10.67%.

## 3. Investments: how good are SolarWinds' existing investments?

![Exhibit 1: return on capital](report-exhibits/exhibit-2-return-on-capital.png)

*Exhibit 1: return on capital*

Return on invested capital rose from 2.69% in 2022 to 6.66% in 2024, but stayed below the 10.67% cost of capital every year. In 2024 the shortfall cost $94.1M of economic value added. Return on equity was 7.99% against a 12.65% cost of equity.

**Why the return is low.** Much of the gap comes from what the return is measured against. Goodwill from the 2016 buyout and later acquisitions makes up all of invested capital (100.65%). So the 6.66% compares profits to the price the buyers paid, not to the assets the business actually runs on.

**How SolarWinds invests.** A typical project is small, steady spending on product development that pays back over years of subscription renewals. The big investments were acquisitions paid for with debt, and the low return reflects those. Whether future projects will pay off is less clear: bidders in a 2023 sale process doubted the move to subscriptions, calling it "early stage."

**R&D classification as expense vs investment.** SolarWinds counts its R&D ($108.6M in 2024) as an expense. Treating it as an investment spread over three years, the course's standard for software, adds $206.2M to capital and $10.5M to operating income. The return barely moves, to 6.53%, because goodwill still makes up most of the capital.

**Without goodwill, the business needs very little capital.** Take out the $2,363.2M of goodwill and the business runs on $191.0M of capital, almost all of it R&D. On that base it earns 87% (61% if R&D is spread over five years). That shows the business is cheap to run. It doesn't show what a new dollar would earn, because SolarWinds has spent its new dollars on acquisitions, and the 6.66% measures those.

**What this means for our valuation.** The 2016 price was too high for what the business earns. Maintenance revenue from older license customers also fell 4.6% in 2024 as they switched to subscriptions.

## 4. Capital structure choices: how is SolarWinds financed?

SolarWinds uses both ends of the debt-equity continuum. From most debt-like to most equity-like:

1. Operating leases, $49.4M.
2. A first-lien term loan, $1,235.7M at face, senior, secured and floating-rate.
3. A $130.0M revolving credit facility, undrawn at year-end.
4. Options and restricted stock units, worth $187.0M at the market price.
5. Common stock: one class, one vote a share, listed in the 2018 IPO.

There is no convertible debt and no preferred stock.

**The trade-off.** Debt saves about $28.1M a year in taxes. Its discipline benefit is small, because managers already answer to the sponsors. Against that, the interest is heavy: cash interest of $104.5M took 55.5% of the $188.3M of operating cash flow in 2024, and that cash flow is already after interest. The rate is floating, so each percentage point costs about $12.4M a year. And the loan had to be refinanced on a sale, which limits flexibility.

On the qualitative weighing, SolarWinds has too much debt.

## 5. Optimal financing: what is the right mix of debt and equity?

![Exhibit 2: cost of capital by debt ratio](report-exhibits/exhibit-1-cost-of-capital-by-debt-ratio.png)

*Exhibit 2: cost of capital by debt ratio*

The cost of capital is lowest, at 10.03%, with 21% debt and an A- rating. This schedule re-estimates the rating and interest rate at each debt ratio. At the actual 33% the schedule gives a B rating and 10.31%, below the 10.67% in section 2, because the schedule prices interest at each ratio's own rate while section 2 uses 2024's actual interest expense. Moving to the optimum saves $10.9M a year, worth $144.4M as a perpetuity growing at 2.5%. SolarWinds carried $468.1M more debt than the optimum.

**Against the sector.** Software companies carry little debt. Across the 333 US software companies in the course dataset, debt is about 4.7% of capital, and the median for the eight peers is 11.7%. At 33%, SolarWinds sits with Open Text (45%) and Progress (38%), the two peers that grew through debt-funded acquisitions. Its debt comes from the 2016 buyout, not from what a software business needs. The 21% optimum is itself above the sector, because it counts debt's tax savings but not the flexibility software companies value, so 21% is better read as a ceiling. Both comparisons point the same way: SolarWinds has too much debt.

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
- Adjusted present value, which weighs debt's tax savings against the expected cost of bankruptcy: optimum of 21%. At today's debt the expected bankruptcy cost ($361.6M) outweighs the tax savings ($321.2M), so the debt is reducing value. At 21% debt, the tax savings are $204.2M and the bankruptcy cost is $24.6M, and the firm is worth $220.3M more.

The bankruptcy cost rests on a judgment: we assume a default would cost 25% of firm value, above the usual 5–10% in direct costs, because software customers hesitate to sign multi-year contracts with a vendor that might fail.

## 6. Financing changes: should SolarWinds move to the optimum, and with what debt?

**Whether and how fast.** SolarWinds should move, but gradually. It cannot be taken over against the sponsors' will, so there is no takeover pressure. There is no near-term bankruptcy threat either: it has $259.3M of cash and an undrawn revolver, its covenant applies only when the revolver is more than 35% drawn, and the loan does not mature until 2030. The best path is to repay debt out of free cash flow to equity, with no special dividends until the ratio nears 21%. At 2024's $127.0M, repaying $468.1M takes about 3.7 years; using part of the cash balance shortens that. It does not need an equity issue or a recapitalization.

**The right type of debt.** Debt should match the assets it funds:

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

**Against the sector, this is an outlier.** Most of the eight peers paid no dividend, and the wider software group paid out 27.22% of earnings. An irregular special dividend gets none of a dividend's usual benefits: it signals nothing about future earnings and does not discipline managers. The likeliest driver was the sponsors' preference: about two-thirds of the 2024 dividend went to them. That is an inference, not a stated reason. Either way, payments that follow the owners' preference and not earnings are a weak policy for public shareholders.

## 8. Dividend assessment: should SolarWinds return more or less cash?

Over 2022–2024, free cash flow to equity totaled −$419.8M against $224.6M returned. The negative total comes from 2022, when the company repaid $664.4M of debt. Years before 2022 include N-able and are not comparable. The years that describe the business today:

- 2023: free cash flow to equity of $59.4M; $18.8M returned.
- 2024: SolarWinds returned $194.7M but generated only $127.0M of free cash flow to equity, so it paid out $67.7M more than it made. Cash fell by only $29.9M. Two non-cash items pulled in opposite directions: $76.5M of employee pay was in stock rather than cash, while net income included a $49.0M tax benefit that brought in no cash. The stock pay is what let SolarWinds pay out more than it generated, so part of the dividend was funded by diluting the shareholders who received it.

**Should shareholders trust SolarWinds with cash?** No. On all the capital invested in it, SolarWinds earns 6.66% against a 10.67% cost. Its operating business needs little capital, so new cash idles or goes to acquisitions, and acquisitions are what the 6.66% reflects. Returning cash was right. Paying it out as a dividend while debt sat $468.1M above the optimum was not. SolarWinds should have returned less to shareholders and used the cash to repay debt.

## 9. Valuation: what is SolarWinds worth?

### Discounted cash flow

We value the whole firm, not just the equity, because the debt ratio is not stable: 33% today against a 21% optimum, and an equity valuation would need a forecast of every debt issue and repayment. The valuation runs in the course's spreadsheet (fcffsimpleginzu), with its default assumptions kept wherever we had no better information. The inputs are management's 2025–2030 forecast from the merger information statement, with stock-based compensation charged as an expense:

- Free cash flow to the firm rises from $156.0M in 2025 to $322.2M in 2030 and $430.7M in 2034, after reinvesting at the spreadsheet's default sales-to-capital ratio for software, 1.54. The plan's own cash flows are higher because customer prepayments fund its growth; the default is the conservative side.
- Revenue grows 8.12% a year to 2030 (4.4% in 2025, then 8.9%), against 5.25% a year over 2022–2024, and fades to the 4.43% risk-free rate by year 10. The operating margin, on the plan's definition, rises from 32.7% in 2025 to 40.1% in 2030 and stays there.
- On SolarWinds' own fundamentals (return on invested capital times reinvestment), growth would be about zero. The plan assumes its margin expansion delivers.

**Cost of capital and terminal value.** The 10.67% from section 2 is entered directly, because the spreadsheet's built-in betas and risk premiums are 2026 data and the valuation date is February 2025. The spreadsheet then applies its defaults: the cost of capital fades to a mature-company 8.66% (risk-free plus the 4.23% mature-market premium) over years 6–10; growth after year 10 equals the 4.43% risk-free rate; and the return on new capital equals the cost of capital, so growth after year 10 adds no value. Taxes are 25% throughout: the reported −7.8% effective rate came from a one-off valuation-allowance release, and cash taxes were $61.5M on $103.8M of pre-tax income. Restricted stock units (12.2M) are counted as shares, as the spreadsheet suggests; the 0.1M options are valued separately.

| Bridge | Status quo | At the optimal debt ratio |
| :---- | ----: | ----: |
| Present value of cash flows, years 1–10 (2025–2034) | $1,642.7M |  |
| Present value of terminal value | $2,200.5M |  |
| Enterprise value | $3,843.2M | $3,982.3M |
| − Debt | $1,285.0M |  |
| + Cash, at face value: it earns interest at market rates, so no discount; no cross holdings or minority interests | $259.3M |  |
| − Options (restricted units are counted as shares) | $1.6M |  |
| Value per share (183.8M shares, including 12.2M restricted units) | $15.32 | $16.08 |

**Why this terminal value.** The spreadsheet's terminal cash flow reinvests 51% of after-tax operating income (growth ÷ return on capital, 4.43% ÷ 8.66%), so the company pays for the growth it is credited with. Capitalizing the year-10 cash flow without that reinvestment would assume growth for free and overstate the value.

**Sensitivity.** The terminal value is 57% of the total, and the two defaults behind it pull in opposite directions. Growth in perpetuity at 2.5% instead of the risk-free rate takes the value to $14.52. Reinvesting almost nothing, as the plan itself assumes, takes it to $16.94. We keep the defaults: the first is the spreadsheet's rule that growth cannot outrun the economy forever, and the second is the sign of a plan that expects growth without paying for it.

**What if the plan is wrong.** The plan carries more of the value than the terminal assumptions do. With revenue growing at the 2022–2024 rate of 5.25% instead of 8.12%, the value falls to $12.65 a share, and to $7.77 if margins also stay at 2024's 29.1%. The margin expansion matters more than the growth. The market price of $15.18 sat between the history-based $12.65 and the plan-based $15.32, nearer the plan, though the market had not seen the plan: it was published in March 2025, seven weeks after the valuation date.

### Relative valuation

| Multiple | SolarWinds | Peer median | Implied value per share |
| :---- | ----: | ----: | :---- |
| Enterprise value / EBITDA | 12.84x | 16.39x | $19.95 |
| Price / earnings | 23.28x | 26.57x | about $16.24 |
| Enterprise value / revenue | 4.56x | 3.32x | $8.34 |
| Price / book | 1.86x | 4.58x | not used |

The peers are the eight US filers in Jefferies' fairness-opinion set. EV/EBITDA is the best multiple here: it is not distorted by SolarWinds' debt or one-time items, while revenue multiples ignore that peer margins range from −18% to 31%, and book equity rests on buyout goodwill. EV/EBITDA gives $19.95 and price to earnings about $16.24, a range above both the $15.32 DCF value and the $15.18 market price.

### Value with changes

The financing change in section 6 raises value to $16.08 a share, a gain of $0.76 ($139.1M). The gain is modest because the spreadsheet already moves the cost of capital to a mature-company level after year 5, so only the first five years benefit. The operating changes are not priced separately: the margin expansion is already in management's plan.

**Likelihood of change.** Under the sponsors it was low. In 2024 they chose a special dividend over repaying debt. Control did change in 2025, when the sponsors sold the company for $18.50 a share, but the buyer added $2,750M of new term loans, more than double the $1,285.0M SolarWinds carried, so the move to the optimal debt ratio did not happen.

## Conclusion

SolarWinds is a steady business with a poor financial structure. Customers stay, and the business needs little capital to run. But it earns less than its cost of capital on the price paid for it, carries about $468M more debt than it should, and in 2024 paid out more cash than it generated. The fix is simple: use free cash flow to repay debt until it is about 21% of capital, pause special dividends until then, and only fund projects that earn more than they cost. On management's plan, the shares are worth $15.32, in line with the $15.18 market price.

| Principle | What SolarWinds does | What it should do |
| :---- | :---- | :---- |
| Objective and governance | Runs for the sponsors; the public float had no vote on the deal | Give the minority a real voice on a change of control |
| Investment | Earns 6.66% against a 10.67% cost of capital on a capital base of buyout goodwill | Hold new spending to a return above the cost of capital |
| Financing | 33% debt against a 21% optimum; the right type of debt, too much of it | Repay about $468.1M from free cash flow to equity before any special dividend |
| Dividends | Pays out more than it generates, in special dividends, while over-levered | Repay debt before returning more cash |
| Valuation | Worth $15.32 a share on management's plan, 1% above the market price | Worth $16.08 with debt at the optimum; most of the value rests on the plan's margin expansion |

## Sources

SolarWinds Forms 10-K (FY2018, FY2020, FY2023, FY2024), 2024 proxy statement, 2018 IPO prospectus, Forms 8-K (October 2022, February and April 2025) and merger information statement (March 2025, including the Goldman Sachs and Jefferies fairness opinions and management's plan); Damodaran datasets as of January–February 2025; FRED (10-year Treasury, SOFR); peer companies' fiscal-2024 Forms 10-K and February 5, 2025 closing prices; US Department of Justice press release on interlocking directorates (October 19, 2022); Damodaran, fcffsimpleginzu.xlsx (February 2026 edition, pages.stern.nyu.edu/~adamodar/pc/).
