---
title: "SolarWinds final project — deal-analysis version (Google Doc snapshot, 2026-11-03)"
status: archived
owner: weprintmoney
created: 2026-11-03
last_updated: 2026-11-03
---

> Text of the Google Doc working draft as of 2026-11-03, saved before it was refocused on the assignment instructions. It keeps the deal analysis (the Turn/River sale, the deal-insights summary bullet and the "The deal" paragraph) and the ❓ questions for the professor. The original Word export is alongside: `final-project-deal-analysis-version-2026-11-03.docx`. Images are shown as [image]; the exhibits are in `../report-exhibits/`.

Corporate Finance Assessment and Valuation

SolarWinds Corporation

February 5, 2025


[Executive summary](#executive-summary) 3

[1. Stockholder analysis: who has the power?](#_udrjxy52nbtx) 4

[2. Risk and return: how risky is SolarWinds, and what is its hurdle rate?](#risk-and-return-how-risky-is-solarwinds-and-what-is-its-hurdle-rate) 4

[3. Investments: how good are SolarWinds' existing investments?](#investments-how-good-are-solarwinds-existing-investments) 5

[4. Capital structure choices: how is SolarWinds financed?](#capital-structure-choices-how-is-solarwinds-financed) 6

[5. Optimal financing: what is the right mix of debt and equity?](#optimal-financing-what-is-the-right-mix-of-debt-and-equity) 7

[6. Financing changes: should SolarWinds move to the optimum, and with what debt?](#financing-changes-should-solarwinds-move-to-the-optimum-and-with-what-debt) 7

[7. Dividend policy: how does SolarWinds return cash?](#dividend-policy-how-does-solarwinds-return-cash) 8

[8. Dividend assessment: should SolarWinds return more or less cash?](#dividend-assessment-should-solarwinds-return-more-or-less-cash) 9

[9. Valuation: what is SolarWinds worth?](#valuation-what-is-solarwinds-worth) 9

> [Discounted cash flow](#discounted-cash-flow) 9
>
> [Relative valuation](#relative-valuation) 11
>
> [Value with changes, and the deal](#value-with-changes-and-the-deal) 12

[Conclusion](#conclusion) 12

[Sources](#sources) 13

❓ I am basing this analysis of SolarWinds on public data from **February 5, 2025**. This was the last normal day of stock trading before Turn/River Capital announced they were buying the company on February 7. SolarWinds has since been delisted, obscuring the data required for an accurate current valuation. Is this allowed?

# Executive summary

SolarWinds was a mature, cash-generating software company run for the benefit of two private-equity owners. Silver Lake and Thoma Bravo (the sponsors) held two-thirds of the shares, chose the directors that mattered and approved the deal without a public vote.

| Value per share on management's plan (DCF) | \$16.13 |
|----|----|
| Value per share at the optimal debt ratio | \$16.35 |
| Market price on February 5, 2025 | \$15.18 |
| Deal price | \$18.50 |
| Cost of capital: 2025–2030 / after 2030 | 10.23% / 8.23% |
| Return on invested capital, FY2024 | 6.66%, on a capital base that is almost all buyout goodwill |
| Debt ratio: actual / optimal | 33% / 21% |

- **Does well:** It keeps customers: 93.5% of revenue is recurring, subscription net retention was 99% in 2024, and maintenance contracts renewed at 97%. Its loan has the right rate type and maturity for that business.

- **Does poorly:** It earns 6.66% on its capital against a 10.23% cost. It carries more debt than is optimal, 33% against 21%. In 2024 it paid out more cash than it generated, through a \$168.2M special dividend, while over-levered.

- **Should do differently:** Repay about \$468.1M of debt before returning more cash. Hold new growth spending to a return above the cost of capital.

❓ Should I remove the deal insights section? I specifically chose this company because I wanted to figure out why someone would buy it when it’s down in revenue YoY, has failed to meet its hurdle rate on new projects for almost a decade, and has become too debt-heavy to continue its endless quest for acquisitions that also failed to exceed the cost of capital. I understand this is not a normal section of this assignment, and perhaps this is a lesson better covered in the

- **Deal insights:** I used the discounted cash flow valuation as the basis for my conclusions. On management's plan it puts SolarWinds at \$16.13 a share, 6% above its market price. The \$18.50 deal price was 15% above that. Reaching it would take a return on new capital of about 12.7% forever, where this report assumes new capital earns only its cost. At the company's own growth rate the shares are worth \$13.05. Market price sat between the two. In this analysis, \$18.50 looks like a full price for public shareholders: it paid for the plan and a premium on top. No other bidder came close, and the buyer could pay more than the business is worth on its own because it funded the deal mostly with debt and specialized in finishing the subscription transition that public shareholders had discounted.

1\. Stockholder analysis: who has the power?


*Exhibit 1: ownership*

**Power lies with the sponsors, not with managers or the public float.** Silver Lake held 36.56% and Thoma Bravo 29.79% at the 2024 proxy, 66.34% together. Officers and directors as a group held 1.95%.

Their control goes beyond ownership. Each sponsor could nominate three directors while it held 20% or more, and the two jointly named a seventh. Of nine directors, three were Silver Lake designees; <span class="mark">Thoma Bravo's three seats and the joint seat were vacant,</span> so the sponsors held three seats and could have filled seven. Eight of the nine counted as independent under exchange rules, including all three designees. Each sponsor also had to consent to any change of control, so a hostile takeover was impossible. The sponsors approved the deal by written consent on February 7, 2025, with about 65% of the votes. Public shareholders never voted.

**Conflicts of interest.** The sponsors and the public shareholders wanted different things. The sponsors had owned the company since 2016 and wanted an exit, and the 2024 special dividend paid them about <span class="mark">two-thirds of \$168.2M.</span> The CEO had a conflict of his own: his \$22.99M change-of-control package was mostly \$19.94M of accelerated equity paid on closing, which tied his reward to completing a deal.

The marginal investor was the diversified institution holding the roughly 34% public float. The sponsors did not set the traded price, so market beta is the right measure of risk. Their lack of diversification belongs in a private negotiation, not in the cost of capital.

# 2. Risk and return: how risky is SolarWinds, and what is its hurdle rate?

| Input | Value | Basis |
|----|----|----|
| Risk-free rate | 4.43% | 10-year Treasury, 2025-02-05; the US was rated Aaa, so no default spread |
| Equity risk premium | 4.92% | The course dataset's implied US premium of 4.27% on the 64.82% of revenue earned in the US; 6.11%, the European premium, on the 35.18% earned abroad, which adds 0.65 points |
| Unlevered beta | 1.22 | Software industry, cash-corrected (course dataset, January 2025) |
| Levered beta | 1.6714 | Relevered at a debt-to-equity ratio of 0.4933 and a 25% marginal tax rate |
| Cost of equity | 12.65% | <span class="mark">4.43% + 1.6714 × 4.92%</span> |
| Pre-tax cost of debt | 7.11% | The term loan's effective rate, SOFR + 2.75% (FY2024 10-K) |
| After-tax cost of debt | 5.33% | 7.11% × (1 − 25%) |
| Debt ratio, market values | 33.03% | Debt \$1,285M; equity 171.6M shares × \$15.18 = \$2,604.9M |
| Cost of capital | 10.23% | <span class="mark">66.97% × 12.65% + 33.03% × 5.33%</span> |

**Beta.** A regression beta is not available for the delisted ticker, and the <span class="mark">bottom-up beta is the better measure in any case.</span> SolarWinds reports one segment, so the software industry beta applies to the whole firm.

**Debt** is the loan at face value, \$1,235.7M, plus \$49.4M of lease liabilities. Deferred revenue of \$389.3M is owed in service, not cash. Cloud purchase commitments of \$68.4M are payments for a service the company uses. Both are excluded.

**Cost of debt.** No agency rating is disclosed. Interest coverage of 1.85 times (operating income of \$208.4M against gross interest expense of \$112.4M) implies a synthetic B- rating on the course's table for smaller firms and an 8.85% cost of debt. Interest expense ran above today's rate because the loan's rate fell during 2024 from 9.11% to 7.11%. The 7.11% is a rate set by its lenders, so it is the cost of debt used.

❓ SolarWinds has no agency rating, but its only debt is a floating-rate term loan with an observed rate of 7.11%. A synthetic rating from interest coverage gives B- and 8.85%. I used the observed rate. Is that right, or should a synthetic rating take priority?

**Market or book weights.** At <span class="mark">book values</span>, debt would be 47.28% of capital and the cost of capital 9.19%. The book version leans on cheap debt because the market values equity at 1.86 times book. Market weights are the right ones.

# 3. Investments: how good are SolarWinds' existing investments?


*Exhibit 2: return on capital*

Return on invested capital rose from 2.69% in 2022 to 6.66% in 2024, but stayed below the 10.23% cost of capital every year. In 2024 the shortfall cost \$84M of economic value added. Return on equity was 7.99% against a 12.65% cost of equity.

The capital base explains much of the gap. Goodwill from the 2016 buyout and later acquisitions is 100.65% of invested capital, so the return is measured against the price the sponsors paid, not against the operating assets. A typical SolarWinds project is a small, repeated spend on product development, paid back over years of subscription renewals. The large, lumpy investments were acquisitions funded with debt, and those are what the low return reflects. Future projects are uncertain: bidders in a 2023 sale process doubted the move to subscriptions, citing its "early stage".

Capitalizing research and development does not change the headline. SolarWinds expenses its R&D, \$108.6M in 2024. Capitalizing the last three years' spend over a three-year life, the life the course uses for software, adds a \$206.2M research asset to capital and \$10.5M to operating income (R&D less \$98.1M of amortization). The adjusted return is 6.53%, because the capital base is still the goodwill. Strip the \$2,363.2M of goodwill out and the business runs on \$191.0M of capital, almost all of it the research asset, and earns 87% on it (61% on a five-year life). That says the business needs little capital, not what a new dollar earns: SolarWinds' new dollars have gone into acquisitions, and acquisitions are what the 6.66% measures. The 2016 price was too high for what the business earns, and the maintenance revenue of the legacy license base fell 4.6% in 2024 as customers converted. Section 9 uses both facts.

# 4. Capital structure choices: how is SolarWinds financed?

SolarWinds uses both ends of the debt-equity continuum and nothing in between. From most debt-like to most equity-like:

1.  Operating leases, \$49.4M.

2.  A first-lien term loan, \$1,235.7M at face, senior, secured and floating-rate.

3.  A \$130.0M revolving credit facility, undrawn at year-end.

4.  Options and restricted stock units, worth \$187.0M at the market price.

5.  Common stock: one class, one vote a share, listed in the 2018 IPO.

There is no convertible debt and no preferred stock.

The trade-off. Debt saves about \$28.1M a year in taxes. Its discipline benefit is small, because managers already answer to the sponsors. Against that, the interest is heavy: cash interest of \$104.5M took 55.5% of the \$188.3M of operating cash flow in 2024, and that cash flow is already after interest. The rate is floating, so each percentage point costs about \$12.4M a year. And the loan had to be refinanced on a sale, which limits flexibility.

On the qualitative weighing, SolarWinds has too much debt.

# 5. Optimal financing: what is the right mix of debt and equity?


*Exhibit 3: cost of capital by debt ratio*

The cost of capital is lowest, at 10.03%, with 21% debt and an A- rating. This schedule re-estimates the rating and interest rate at each debt ratio. At the actual 33% that method gives a B rating and 10.31%, slightly above the 10.23% in section 2, which uses the loan's actual 7.11% rate. Moving to the optimum saves \$10.9M a year, worth \$144.4M as a perpetuity growing at 2.5%. SolarWinds carried \$468.1M more debt than the optimum.

| Debt ratio | Levered beta | Cost of equity | Rating | Pre-tax cost of debt | Cost of capital |
|----|----|----|----|----|----|
| 0% | 1.220 | 10.43% | AAA | 4.88% | 10.43% |
| 10% | 1.322 | 10.93% | AA | 5.03% | 10.22% |
| 21% (optimum) | 1.463 | 11.63% | A- | 5.38% | 10.03% |
| 30% | 1.612 | 12.36% | B+ | 7.04% | 10.24% |
| 33% (actual) | 1.671 | 12.65% | B | 7.43% | 10.31% |
| 40% | 1.830 | 13.43% | B- | 8.85% | 10.72% |
| 50% | 2.135 | 14.93% | C | 19.93% | 16.44% |

The result holds under other assumptions. Measuring coverage on EBITDA gives an optimum of 28%, still below 33%. A 30% fall in operating income lowers the optimum to 14%. The adjusted present value approach reaches the same 21%: today's debt carries a \$321.2M tax benefit and \$361.6M of expected bankruptcy cost (a 36.8% ten-year default probability at the B rating, at a cost of 25% of firm value); at 21% debt the benefit is \$204.2M and the cost \$24.6M, and firm value is \$220.3M higher.

# 6. Financing changes: should SolarWinds move to the optimum, and with what debt?

Whether and how fast. SolarWinds should move, but gradually. It cannot be taken over against the sponsors' will, so there is no takeover pressure. There is no near-term bankruptcy threat either: it has \$259.3M of cash and an undrawn revolver, its covenant applies only when the revolver is more than 35% drawn, and the loan does not mature until 2030. The best path is to repay debt out of free cash flow to equity, with no special dividends until the ratio nears 21%. At 2024's \$127.0M, repaying \$468.1M takes about 3.7 years (468.1 ÷ 127.0); using part of the cash balance shortens that. It does not need an equity issue or a recapitalization.

The right type of debt. Debt should match the assets it funds:

| Characteristic | Right for SolarWinds | Actual |
|----|----|----|
| Rate | Floating: annual price increases give it pricing power | Floating, SOFR + 2.75% |
| Maturity | Medium term, four to six years | 5.0 years, one maturity in 2030 |
| Currency | Dollars and euros in proportion to cash flow; at most 35.18% foreign | All US dollars |
| Form | Straight debt | Straight debt, no swaps |

Rate type, maturity and form fit; the problem is size. Two mismatches remain. No debt is in euros, the currency of most of the foreign revenue; a euro tranche could be added at refinancing, once net foreign cash flow is measured, but the filings do not size it. The single 2030 maturity could also be staggered.

# 7. Dividend policy: how does SolarWinds return cash?

SolarWinds has no regular dividend. In five years it paid two special dividends:

- 2021: \$237.2M, \$1.50 a share, funded by \$238.2M of cash N-able paid SolarWinds at its spin-off.

- 2024: \$168.2M, \$1.00 a share.

Its only other cash return is shares withheld for employees' taxes on vesting stock. In 2024 the dividend was 150.3% of net income. Counting withheld shares, cash returned was 174.0%. The dividend yield was 6.59% at the \$15.18 market price.

Against the sector, this is an outlier. Most of the eight peers paid no dividend, and the wider software group paid out 27.22% of earnings. The course's dividend trade-off, the tax cost to shareholders against the signal a dividend sends and the discipline it imposes on managers, cuts against special dividends here: an irregular payment signals nothing and disciplines no one. Against the patterns the course describes, SolarWinds' payments followed no earnings trend and were not sticky. The likeliest driver of the 2024 dividend is the sponsors' preference; with their stakes unchanged from the proxy, about two-thirds of it went to them. That is an inference, not a stated reason. Either way, irregular payments that follow the owners' preference and not earnings are a weak policy for public shareholders.

# 8. Dividend assessment: should SolarWinds return more or less cash?


*Exhibit 4: free cash flow to equity vs cash returned*

Over 2022–2024, free cash flow to equity totaled −\$419.8M against \$224.6M returned. The negative total comes from 2022, when the company repaid \$664.4M of debt. Years before 2022 include <span class="mark">N-able</span> and are not comparable. The years that describe the business today:

- 2023: free cash flow to equity of \$59.4M; \$18.8M returned.

- 2024: \$194.7M returned against \$127.0M of free cash flow to equity (net income \$111.9M + depreciation \$74.4M − capital spending \$20.5M − working-capital build \$38.8M, no net borrowing), \$67.7M more than it generated. Cash fell only \$29.9M, because the cash flow charges \$76.5M of non-cash stock-based compensation; the rest of the dividend was paid by diluting shareholders.

❓ SolarWinds is delisted, so I can’t run a regression for Jensen’s alpha. Is the proxy’s total shareholder return chart an acceptable stand-in for the stock-return test?

Should shareholders trust SolarWinds with cash? No. On all the capital invested in it, SolarWinds earns 6.66% against a 10.23% cost. Its operating business needs little capital, so new cash idles or goes to acquisitions, and acquisitions are what the 6.66% reflects. Returning cash was right. Paying it out as a dividend while debt sat \$468.1M above the optimum was not. SolarWinds should have returned less to shareholders and used the cash to repay debt.

# 9. Valuation: what is SolarWinds worth?

## Discounted cash flow

Cash flows are management's 2025–2030 forecast from the merger information statement, with stock-based compensation charged as an expense:

- Free cash flow to the firm rises from \$212.0M in 2025 to \$419.0M in 2030.

- Revenue grows 8.12% a year, against 5.0% in 2024 and 5.25% a year over 2022–2024. The operating margin, on the plan's definition (adjusted EBITDA less stock-based compensation and depreciation), rises from about 29% in 2024 to 32.7% in 2025 and 40.1% in 2030. The GAAP margin was 26.2% in 2024, after restructuring, cyber-incident and acquisition costs.

- The record behind the plan: operating income went from a loss of \$819.6M in 2022 (after a \$906.4M goodwill impairment) to \$150.4M in 2023 and \$208.4M in 2024; <span class="mark">net income from −\$929.4M to −\$9.1M to \$111.9M</span>; free cash flow to the firm about \$146M, \$191M and \$171M, against the plan's \$212M for 2025.

- On SolarWinds' own fundamentals (return on invested capital times reinvestment), growth would be about zero. The plan assumes its margin expansion delivers.

❓ SolarWinds’ margins are changing, so the fundamental formula (reinvestment × return on capital) gives about zero growth. The revenue-based model needs a sales-to-capital ratio, and I can’t get a meaningful one because nearly all invested capital is buyout goodwill. So I used management’s six-year forecast from the merger documents and show stress cases at the historical growth rate. Is that acceptable as the status quo story, or would you rather I build my own revenue and margin path?

❓ Management’s forecast has free cash flow above after-tax operating income every year, so reinvestment is negative. I fixed that in the terminal value by setting reinvestment to growth ÷ return on capital, but left the forecast years as management wrote them. Should I also force positive reinvestment in the forecast years?

Two costs of capital. The plan years (2025–2030) are discounted at 10.23%. After 2030, growth is 2.5% a year and the terminal value uses a stable-period cost of capital. A mature firm's beta moves toward one and its debt toward its optimum, and at that debt ratio it pays the rate its new rating commands:

| Stable-period input | Value |
|----|----|
| Beta | 1.00: the course's rule for a mature firm, and a fit for a business with 93.5% recurring revenue |
| Cost of equity | 9.35% (4.43% + 1.00 × 4.92%) |
| Debt ratio | 21%, the optimum |
| Pre-tax cost of debt | 5.38%, the A- rate at 21% debt from the section 5 schedule, not today's 7.11% |
| After-tax cost of debt | 4.04% |
| Stable cost of capital | 8.23% |
| Return on new capital | 8.23%, equal to the cost of capital, so growth after 2030 adds no value |
| Reinvestment rate | 30.38% (2.5% ÷ 8.23%) |

❓ I set the growth period at six years because that’s how long management’s plan runs, not from a competitive-advantage analysis; I then checked it against retention and peer growth. Is it fine to let the forecast’s length set the period if the moat evidence supports it?

❓ My cost of capital, beta and debt ratio jump straight to stable values after 2030. In your Disney valuation you moved each input in linear steps over years 6–10. How much does skipping the transition matter, and should I add one?

The return on new capital is the judgment that matters. SolarWinds earns 6.66% on all its capital and 6.53% with R&D capitalized, both below its cost of capital, and its marginal dollars have gone into acquisitions. The 87% in section 3 shows how little capital the business runs on, not what the next dollar will earn. Nothing in the record earns a lasting excess return, so none is assumed, and the terminal value is then almost exactly next year's after-tax operating income capitalized at the cost of capital; how much is reinvested and how fast it grows no longer matter. The sensitivity table below prices the case that an excess return exists.

| Bridge | Status quo | At the optimal debt ratio |
|----|----|----|
| Present value of 2025–2030 cash flows | <span class="mark">\$1,321.6M</span> |  |
| Present value of terminal value | \$2,658.2M |  |
| Enterprise value | \$3,979.8M | \$4,017.7M |
| − Debt | \$1,285.0M |  |
| \+ Cash, at face value: it earns interest at market rates, so no discount; no cross holdings or minority interests | \$259.3M |  |
| − Options and restricted stock units | \$187.0M |  |
| Value per share (171.6M shares) | \$16.13 | \$16.35 |

The terminal-value method matters. Growing the 2030 cash flow at 2.5% forever gives \$24.96 a share. That method assumes SolarWinds grows without reinvesting: in 2030 capital spending barely exceeds depreciation, and customers prepay \$46M more than the year before. Matching that cash flow would need reinvestment of <span class="mark">−9.33%</span> of operating income forever, so the reinvestment-consistent value is the right one.

What it takes to reach \$18.50. The deal price requires excess returns forever, or a lower stable beta:

| Return on new capital after 2030 | 8.23% (used) | 10%     | 12%     | 15%     | 20%     |
|----------------------------------|--------------|---------|---------|---------|---------|
| Value per share                  | \$16.13      | \$17.32 | \$18.25 | \$19.18 | \$20.10 |

| Stable beta (stable cost of capital) | 0.80 (7.46%) | 1.00 (8.23%) | 1.46 (10.02%): today's business risk relevered at 21% debt |
|----|----|----|----|
| Value per share, no excess returns | \$17.74 | \$16.13 | \$13.36 |
| Value per share, 12% return | \$21.01 | \$18.25 | \$14.06 |

At a beta of 1.0 the deal price needs a return of about 12.7% in perpetuity. The stable beta moves the value more than the return does, and 1.0 is the course's rule for a mature firm rather than a SolarWinds-specific estimate, so the second table says what that choice is worth.

What if the plan is wrong. The plan carries more of the value than the terminal assumptions do. Rerunning the valuation with revenue growing at the 2022–2024 rate of 5.25% instead of 8.12%, with the same terminal assumptions:

| Case | 2030 revenue | 2030 free cash flow to the firm | Value per share |
|----|----|----|----|
| Management's plan: 8.12% growth, margin 32.7% to 40.1% | \$1,273.0M | \$419.0M | \$16.13 |
| Historical growth, plan margins | \$1,083.3M | \$345.3M | \$13.05 |
| Historical growth, margin held at 32.7% | \$1,083.3M | \$284.7M | \$9.89 |
| Historical growth, margin held at 2024's 29.1% on the plan's definition | \$1,083.3M | \$255.6M | \$8.08 |

The margin expansion matters more than the growth. The market price of \$15.18 sat between the history-based \$13.05 and the plan-based \$16.13, nearer the plan. The market had not seen the plan: it was published in the March 2025 information statement, seven weeks after the valuation date.

Against the banks. The fairness opinions valued SolarWinds at \$14.30–\$23.70 (Goldman Sachs) and \$14.70–\$19.70 (Jefferies). \$16.13 sits inside both, in the lower part of each. Their higher midpoints come mainly from growing the final-year cash flow, the method that gives \$24.96 here.

## Relative valuation

| Multiple                   | SolarWinds | Peer median | Implied value per share |
|----------------------------|------------|-------------|-------------------------|
| Enterprise value / EBITDA  | 12.84x     | 16.39x      | \$19.95                 |
| Price / earnings           | 23.28x     | 26.57x      | about \$16.24           |
| Enterprise value / revenue | 4.56x      | 3.32x       | \$8.34                  |
| Price / book               | 1.86x      | 4.58x       | not used                |

❓ For pricing, I used the fairness opinion’s peer set, narrowed to eight US filers, and excluded high-growth observability companies because their multiples price growth SolarWinds doesn’t have. You argue comparables should be defined broadly by cash flows, growth and risk. Is a curated set like this acceptable with a sample this small?

The peers are the eight US filers in Jefferies' fairness-opinion set: Akamai, NetApp, NetScout, OneSpan, OpenText, Progress, Qualys and Teradata; three foreign filers and the since-acquired Informatica are left out. The EV/EBITDA median rests on the six peers with positive EBITDA, the P/E median on the seven with profits. EV/EBITDA is the best multiple here. It is not distorted by SolarWinds' debt or one-time items. Revenue multiples ignore that peer margins range from −18% to 31%. Price to book is set aside because SolarWinds' book equity rests on buyout goodwill and buybacks have shrunk some peers' equity. The peers grew from −9.3% to 9.6%, apart from OpenText's acquisition-driven 28.6%, so the median is not adjusted for growth. EV/EBITDA gives \$19.95 and price to earnings about \$16.24, so the market's own pricing puts SolarWinds at \$16 to \$20. That brackets both the market price and the deal.

## Value with changes, and the deal


*Exhibit 5: value per share by method*

Value with changes. The financing change in section 6 raises value to \$16.35 a share, a gain of \$0.22 (\$37.9M). The gain is small because the stable period already assumes the 21% optimum, so only 2025–2030 benefits. The gain is larger on other bases: \$144.4M (\$0.84 a share) from capitalized annual savings and \$220.3M (\$1.28) from adjusted present value. Those measure the change at a constant firm value, before any forecast. The operating changes are not priced separately: the margin expansion is already in management's plan.

Likelihood of change. Under the sponsors it was low. In 2024 they chose a special dividend over repaying debt. What happened instead was the deal. The buyer's financing runs the other way: \$2,750M of new term loans, more than double the \$1,285.0M SolarWinds carried. A private-equity buyer borrows to raise the return on its own equity, not to lower the company's cost of capital.

The deal. \$18.50 was 15% above intrinsic value on management's plan and 22% above the market price, and no other buyer would pay it. Three of 13 bidders approached in 2023 made offers, all well below \$18.50, and more than 20 approached in 2024 made none. Thoma Bravo, a 30% owner with full access to the company's data, declined to bid as high. The buyer could pay it for two reasons. It funded the deal with \$1,670M of equity, \$2,750M of new debt and \$225M of the company's cash, so it needs the business to beat the cost of its debt, not the 8.23% cost of capital. And it specializes in software companies partway through a move to subscriptions, as it did with Tufin in 2022, the transition the 2023 bidders had doubted; its own name for its method is “growth engineering”. The value still rests on margin rising from about 29% toward 40%. At historical growth the shares are worth \$13.05, against a buyer carrying more than twice the debt.

# Conclusion

| Principle | What SolarWinds does | What it should do |
|----|----|----|
| Objective and governance | Runs for the sponsors; the public float had no vote on the deal | Give the minority a real voice on a change of control |
| Investment | Earns 6.66% against a 10.23% cost of capital on a capital base of buyout goodwill | Hold new spending to a return above the cost of capital |
| Financing | 33% debt against a 21% optimum; the right type of debt, too much of it | Repay about \$468.1M from free cash flow to the firm before any special dividend |
| Dividends | Pays out more than it generates, in special dividends, while over-levered | Repay debt before returning more cash |
| Valuation | Worth \$16.13 a share on management's plan, 6% above the market price | \$18.50 looks like a full price for the public shareholders: 15% above intrinsic value on the plan, with the plan priced in |

# Sources

SolarWinds Forms 10-K (FY2018, FY2020, FY2023, FY2024), 2024 proxy statement, 2018 IPO prospectus, Forms 8-K (February and April 2025) and merger information statement (March 2025, including the Goldman Sachs and Jefferies fairness opinions and management's plan); Damodaran datasets as of January–February 2025; FRED (10-year Treasury, SOFR); peer companies' fiscal-2024 Forms 10-K and February 5, 2025 closing prices.
