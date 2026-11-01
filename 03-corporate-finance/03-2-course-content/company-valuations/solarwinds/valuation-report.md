---
title: "SolarWinds (SWI) — Valuation Report"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-11-01
---

# SolarWinds (SWI) — Valuation Report

Valued as of 2025-02-05, the last undisturbed trading day before Turn/River's $18.50 cash offer was announced. Every number cites the ledger (`inputs.yaml` field) or the model (`model-output.md` section). The working for each step is in `lesson-01.md` … `lesson-36.md`; the plain-language version is `walkthrough.md`.

## 1. Company and story

SolarWinds sold IT monitoring software to network and systems engineers, a business it was moving from perpetual licenses to subscriptions. In FY2024 revenue was $796.9M, operating income $208.4M and net income $111.9M (`company.revenue`, `company.ebit`, `company.net_income`). Revenue grew from $758.7M in 2023 (`company.history`). A company growing about 5% a year at a 26% operating margin is a mature business. Management's own plan in the deal document called for 8.12% annual revenue growth to 2030 (`forecast.management_growth`). The plan carried the EBIT margin from 32.69% in 2025 to 40.14% in 2030 (`forecast.years`); on the plan's own definition of EBIT (adjusted EBITDA less stock-based compensation less D&A), 2024's margin was about 29.1%, so the GAAP 26% is not the like-for-like starting point (section 6).

Two private-equity firms controlled it:
- **Silver Lake** held 36.56% (`governance.controlling_holders`).
- **Thoma Bravo** held 29.79%.

Each had to consent to any change of control (`governance.marginal_investor`). They took it private in 2016 and re-listed it in 2018. They took cash out through special dividends, including $168.2M in 2024 (`company.history`). In February 2025 they consented to the sale by written consent, so public stockholders never voted.

The question this report answers is what SolarWinds was worth to a diversified investor on 2025-02-05. The answer is set against the two prices that matter: the $15.18 market price (`company.share_price`) and the $18.50 deal price (`company.deal_price`).

## 2. Cost of capital

| Input | Value | Source |
|---|---|---|
| Risk-free rate | 4.43% | `market.risk_free_rate`: 10-year Treasury on 2025-02-05; the US was rated Aaa, so the default spread was 0 |
| Equity risk premium | 4.92% | `country.weighted_erp`: 4.27% implied premium on US revenue, plus an EMEA country premium on the 35.18% of revenue earned abroad |
| Unlevered beta | 1.22 | `beta.unlevered_bottom_up`: software industry, cash-corrected, January 2025 |
| Levered beta | 1.6714 | model §1, at a debt-to-equity ratio of 0.4933 |
| Cost of equity | 12.65% | model §1 |
| Pre-tax cost of debt | 7.11% | `debt.kd_pretax_observed`: the term loan's rate, SOFR plus 2.75% |
| After-tax cost of debt | 5.33% | model §1, at the 25% marginal tax rate |
| Debt ratio | 33.03% | model §1: debt $1,285.0M and equity $2,604.9M at market |
| **Cost of capital** | **10.23%** | model §1 |

**Debt** is the loan at face value, $1,235.7M, plus leases of $49.4M (`company.debt_total`):
- **Deferred revenue** of $389.3M is a service obligation, not debt.
- **Cloud purchase commitments** of $68.4M were checked and ruled out (`company.off_balance_sheet_debt`).
- **No interest is capitalized** and depreciation lives did not change, so operating income is not flattered by either.

**Credit:**
- No agency rating is disclosed (`debt.rating_actual`).
- Interest coverage of 1.85x earns a synthetic B- on Damodaran's January 2025 small-firm table, which implies an 8.85% cost of debt (model §2). That is above the 7.11% the loan actually paid. Secured lenders likely priced the loan on adjusted EBITDA of $384.7M (`company.ebitda_adjusted`), which adds back stock-based compensation and gives 3.42x coverage and a BB rating (model §2). The course measures coverage on operating income after those costs.

**Cross-check against the deal:**
- Goldman Sachs used 9% to 11% and Jefferies 10.70% to 11.70% (`facts.goldman-dcf-discount-rate-range`, `facts.jefferies-dcf-discount-rate-range`).
- 10.23% sits inside Goldman's range. Their per-share DCF ranges were $14.30 to $23.70 (Goldman) and $14.70 to $19.70 (Jefferies, with stock-based compensation charged) (`facts.gs-dcf-range`, `facts.jefferies-dcf-range`). Both contain this report's $16.13, in the lower part of each range. Section 6 explains the remaining gap to their midpoints.

## 3. Investment returns

SolarWinds earned a return on invested capital of 6.66% against its 10.23% cost of capital. That destroyed $84.0M of value in FY2024 on an economic-value-added basis (model §8). Return on equity was 7.99% against a 12.65% cost of equity.

The book measure is distorted. Invested capital of $2,348.0M is all goodwill from the 2016 buyout (goodwill is 100.65% of it, model §8). Capitalizing R&D does not change that verdict: with a 3-year amortizable life (`modeling_choices.rd_amortizable_life`, `company.rd_history`), the research asset is $206.2M, adjusted operating income $218.9M and the adjusted return 6.53%, against 6.66% unadjusted (model §8, R&D capitalized), because the research asset is small next to the goodwill. Strip out the goodwill and the operating assets earn far more than the capital tied up in them: on operating capital of $191.0M (adjusted invested capital less goodwill) the adjusted after-tax operating income of $166.8M is a return of 87.35%, or 60.56% on a 5-year R&D life (model §8). That figure is after-tax operating income over about three years of R&D: it shows how little capital the business runs on, not what a new dollar earns. What fails the test is the price Silver Lake and Thoma Bravo paid in 2016; the business is capital-light. For a new owner the relevant question is not past returns but whether new investment earns its cost, and the record does not show that it does. SolarWinds' marginal dollars have been acquisitions, which is where the goodwill came from, and on all its capital it earns 6.66%, or 6.53% with R&D capitalized, against a 10.23% cost of capital. Section 6 uses this when it sets the stable-period return on capital equal to the stable cost of capital. Management's forecast reinvests little. In 2030, capital spending is $27M against depreciation and amortization of $25M, and the cash flow is lifted by $46M of new deferred revenue (`facts.forecast-2030-detail`).

## 4. Financing mix and the path to the optimum

At the actual 33% debt ratio, the cost of capital is 10.31% on the model's iterated rating. The minimum is 10.03% at 21% debt, under the chosen numerator, EBIT (model §3):
- **Moving to the optimum** saves $10.9M a year, worth $144.4M in perpetuity.
- **Debt above the optimum:** SolarWinds carried $468.1M more debt than the optimum.

The answer depends on how coverage is measured:

| Coverage numerator | Optimal debt ratio | Value of moving |
|---|---|---|
| EBIT (chosen) | 21% | $144.4M |
| EBIT + acquisition amortization | 26% | $44.3M |
| EBITDA | 28% | $28.0M |

All three say SolarWinds was over-levered. Even the most generous one puts the optimum below 33%. The stress test in model §4 points the same way: if operating income falls 30%, the optimum drops to 14%. The adjusted-present-value approach (model §9) reaches the same 21% optimum, with a 25% bankruptcy cost and Altman's default rates by rating. It values moving from 33% at $220.3M; a 10% bankruptcy cost would push the optimum to 40%.

The path to the optimum is to pay down debt, not to issue equity. The term loan is floating-rate debt maturing in February 2030 (`debt.maturity_years`, `debt.covenants`). Cutting it by the $468.1M excess would take about two years of forecast free cash flow ($212.0M in 2025, `forecast.years`) with no further dividends. The loan's type fits the business: dollar debt for a company that reports in dollars, repayable as subscription cash comes in. Its size is the problem.

## 5. Dividend policy

Over 2022–2024, free cash flow to equity totaled −$419.8M against $224.6M returned (model §5), with the $906.4M of non-cash impairments in 2022 added back. The negative total is 2022's $664.4M loan repayment, funded from cash left by the N-able spin-off.

The years that describe the business are 2023 and 2024:

| Year | FCFE | Cash returned | Of which |
|---|---|---|---|
| 2023 | $59.4M | $18.8M | shares withheld for employees' taxes |
| 2024 | $127.0M | $194.7M | $168.2M special dividend + $26.5M of withheld shares |

The 2024 dividend paid out more than the year generated and ran the cash balance down from $289.2M to $259.3M (model §5). That is the pattern of a controlling owner harvesting cash ahead of an exit. The lesson 26 judgment: return of cash was appropriate for a mature company whose projects did not earn their cost of capital. But it should have gone to debt reduction first, given the over-leverage in section 4.

## 6. Discounted cash flow

Cash flows are management's 2025–2030 forecast (`forecast.years`) with stock-based compensation charged as an expense: free cash flow to the firm rises from $212.0M to $419.0M. They are discounted at 10.23% (model §6). The terminal value is capitalized at the stable-period cost of capital of 8.23% and discounted back to today at 10.23%.

The forecast is the main judgment, so model §6 also reruns it with revenue growing at the 2022–2024 rate of 5.25% instead of the plan's 8.12% (`forecast.stress_cases`), with the same terminal method:

| Case | Revenue growth | Margin | 2030 FCFF | Enterprise value | Value per share | vs. plan |
|---|---|---|---|---|---|---|
| Plan (management forecast) | 8.12% | plan, 32.69% to 40.14% | $419.0M | $3,979.8M | $16.13 | |
| Revenue at the 2022–2024 rate, plan margins | 5.25% | plan | $345.3M | $3,451.5M | $13.05 | −$3.08 |
| Same, margin held at the plan's first year | 5.25% | 32.69% | $284.7M | $2,910.7M | $9.89 | −$6.23 |
| Same, margin held at 2024 on the plan's basis | 5.25% | 29.11% | $255.6M | $2,599.4M | $8.08 | −$8.04 |

The plan carries the value, and the margin expansion carries more of it than the growth. The third case is on the plan's own margin definition: the plan's EBIT is adjusted EBITDA less stock-based compensation less D&A (2025: 272 = 412 − 82 − 58), and on that basis 2024's margin was 29.11%, from adjusted EBITDA of $384.7M less $78.3M of stock-based compensation with payroll taxes less $74.4M of D&A, $232.0M on $796.9M of revenue (`forecast.stress_cases`, `company.ebitda_adjusted`, `facts.sbc-with-payroll-taxes-2024`); the GAAP 26.15% is not comparable. The $15.18 market price sat between the history-based $13.05 and the plan-based $16.13, nearer the plan (about 69% of the way, my arithmetic). The market had not seen the plan: it was published in the information statement on 2025-03-27.

| Bridge | Status quo | At the optimal mix |
|---|---|---|
| Present value of 2025–2030 cash flows | $1,321.6M | |
| Present value of terminal value | $2,658.2M | |
| Enterprise value | $3,979.8M | $4,017.7M |
| Less debt, plus cash | debt $1,285.0M, cash $259.3M | |
| − Options and restricted stock | $187.0M | |
| **Value per share** | **$16.13** | **$16.35** |

**The terminal value is the whole argument.** The model shows two methods (model §6):
- **Final-year cash flow grown at 2.5% forever:** $7,490.2M.
- **Operating income less the reinvestment needed to grow at 2.5%** (lesson 32's consistent-reinvestment method, at a stable return on capital equal to the stable cost of capital): $4,769.8M.

In management's 2030 forecast, free cash flow of $419.0M is larger than after-tax operating income. Capital spending ($27M) barely exceeds depreciation ($25M), and customers prepay $46M more in deferred revenue than the year before (`facts.forecast-2030-detail`). Deferred revenue can grow that fast only while the business grows fast, not forever. Growing that cash flow forever assumes SolarWinds grows without ever reinvesting, which no company can do. The course method costs $2,720.4M of terminal value. That is the difference between $24.96 a share, above the deal price, and $16.13 (model §6). Matching the final-year cash flow would need reinvestment of −9.33% of operating income forever: the company would have to shrink its capital while growing.

**The stable-period cost of capital.** Lesson 32 says a firm in stable growth looks like the average firm: beta moves toward one, debt moves toward its optimum, and excess returns fade. So the terminal value does not use today's 10.23%, which rests on a beta of 1.6714 and 33% debt. It uses a beta of 1.00 and the 21% optimum from section 4. Cost of equity is 4.43% + 1.00 × 4.92% = 9.35%. The cost of debt moves with the debt ratio: section 4's schedule assigns an A- rating and 5.38% pre-tax at 21% debt, the 4.43% risk-free rate plus the A- spread (model §3), which is 4.04% after tax. Holding today's 7.11% at the optimum would contradict that schedule. The stable cost of capital is 79% × 9.35% + 21% × 4.04% = 8.23% (model §6).

**The stable return on capital** is set equal to the stable cost of capital, 8.23% (`forecast.stable_roic`), so growth after 2030 adds no value, and terminal reinvestment is 2.5% ÷ 8.23% = 30.38% of operating income. That is a judgment, and section 3 holds the evidence. The record shows no excess returns on new capital: the book return is 6.66%, and capitalizing R&D leaves it at 6.53% (model §8). The capital base is the 2016 buyout goodwill, and that is the point rather than a distortion to strip out: SolarWinds' marginal dollars have been acquisitions, which is where the goodwill came from. The 87.35% return on operating capital excluding goodwill (60.56% on a 5-year R&D life) is after-tax operating income over about three years of R&D; it measures how little capital the business runs on, not what a new dollar earns. The case for a spread is real but unproven: SolarWinds keeps about 99% of its subscription revenue each year (`facts.net-retention-subscription`) and raises prices every year, while the license base is shrinking (maintenance revenue fell 4.6% in 2024, `facts.maintenance-decline-2024`) and the observability rivals grow faster. So the spread stays in the sensitivity, not the base case: $17.32 at the 10% course convention, $18.25 at 12%, $19.18 at 15%, $20.10 at 20% and $21.03 at 30% (model §6). Twelve percent is the upside case, and the deal price needs about 12.7% forever. Even at 30% the value stays below the $24.96 of the no-reinvestment method.

**The stable beta** of 1.00 is the largest single assumption. Model §6 rebuilds the stable cost of capital at 21% debt and the 5.38% cost of debt for three betas, keeping the return on new capital equal to each row's cost of capital: 0.80 gives a 7.46% stable cost of capital and $17.74 a share; 1.00 gives 8.23% and $16.13; 1.46, today's 1.22 unlevered beta relevered at 21%, gives 10.02% and $13.36 ($14.06 at a 12% return). The stable beta moves value more than the stable return does. A beta of 1.00 is the course's rule for mature firms (betas move toward one, and mature-firm betas run about 0.8 to 1.2) and fits a business with 93.5% recurring revenue (`facts.recurring-revenue-share`), but it is a judgment, and the table says what it is worth.

Against the prices, $16.13 is 1.06 times the $15.18 market price and 0.87 times the $18.50 deal price (model §6). Other per-share shortcuts:
- **Diluted shares:** dividing by them instead of subtracting options gives $16.93.
- **Optimal debt ratio:** moving to it adds $0.22 a share ($16.35) in the DCF, because the terminal value already assumes the 21% optimum and only the 2025–2030 years gain. The other two measures give more: annual savings capitalized give $0.84 a share and adjusted present value $1.28 (model §6 reconciliation, §9). They differ in basis. The DCF prices today's debt at its actual 7.11% rate, while the other two price both ends on the synthetic ratings.

## 7. Relative valuation

SolarWinds traded at these multiples against the medians of the eight fairness-opinion peers (model §7, `peers`):

| Multiple | SolarWinds | Peer median |
|---|---|---|
| Enterprise value / revenue | 4.56x | 3.32x |
| Enterprise value / EBITDA | 12.84x | 16.39x |
| Price / earnings | 23.28x | 26.57x |
| Price / book | 1.86x | 4.58x |

The multiples disagree, and for a reason:
- **Revenue multiple:** SolarWinds looks expensive on revenue because its margins are higher than the peers'.
- **EBITDA multiple:** it looks cheap on EBITDA. That is what slower growth predicts: the peers that set the median, such as Qualys growing 9.6% (`peers`), earn higher multiples.
- **Implied values:** after the same subtraction for options and restricted stock as the DCF, the peer-median revenue multiple implies $8.34 a share and the EBITDA multiple $19.95 (model §7).
- **Price to book** is set aside. SolarWinds' book equity rests on buyout goodwill, and two peers' book equity has been shrunk by buybacks. NetApp's and Teradata's price-to-book ratios are above 20x, so the 4.58x median says little.
- **Fiscal years differ:** NetApp's ends in April 2024, NetScout's in March 2024 and Open Text's in June 2024, against SolarWinds' December 2024. Each peer's latest year ended by the valuation date is used; trailing-twelve-month figures would align them better.

Read together, the multiples span $8.34 to $19.95 and bracket both prices. They do not overturn the DCF. The market was not mispricing SolarWinds against its peers at $15.18.

## 8. Final narrative

On the rates of 2025-02-05, SolarWinds as run was worth about $16.13 a share to a diversified investor, on management's plan. That is 6% above the $15.18 it traded at (1.06 times) and 87% of the $18.50 Turn/River paid. The market price was 6% below intrinsic value on the plan (my arithmetic from the 1.06 times); it sat between the history-based $13.05 and the plan-based $16.13 (model §6), nearer the plan, and it did so without having seen the plan, which was published in the information statement on 2025-03-27. Three things could close the $2.37 gap to the deal price ($18.50 − $16.13), and only one is in this model:
- **Financing:** moving to the optimal debt ratio is worth $0.22 a share (model §6).
- **Terminal value:** the deal price is reached only if SolarWinds earns a stable return on capital of about 12.7% forever ($18.25 at 12%, $19.18 at 15%), against the 8.23% assumed here, equal to the stable cost of capital because the record shows no excess returns on new capital; or if its stable beta is nearer 0.8 than 1.0 ($17.74 at 0.80, model §6).
- **Control:** a private-equity buyer can cut costs and lever up in ways a public company with a diffuse float cannot. The lesson 34 answer sizes the operating levers as judgment calls, not model outputs.

For the public stockholders, $18.50 was a full price: 21.9% above the unaffected $15.18, and 15% above the $16.13 intrinsic value on management's plan with consistent reinvestment. It paid for the plan in full and a premium on top, which a public holder could not have earned alone, and the plan itself is the bet: at historical growth the shares are worth $13.05 with the plan's margins, and $9.89 or $8.08 with margins held. For Silver Lake and Thoma Bravo, it was an exit at a price inside both advisers' DCF ranges. Our reading, not stated in the deal document, is this: $16.13 sits inside both ranges, in the lower part of each, and the remaining gap to their midpoints is mainly because the advisers grew the final-year cash flow at 2% to 3.5% (`facts.gs-perpetuity-growth-range`, `facts.jefferies-perpetuity-growth-range`), which gives $24.96 here. That method assumes no reinvestment.

The board's process is the governance weakness. The two sponsors' consent rights meant the 34% public float had no vote. The CEO's $22.99M golden parachute (`governance.change_of_control_payouts`) was mostly $19.94M of accelerated equity that paid on closing. That tied management's reward to getting a deal done rather than to long-run value.

## What would change the answer

| If | Then |
|---|---|
| Stable return on capital were 10%, the course convention, or 12% (a lasting spread over the 8.23% stable cost of capital) | $17.32 at 10%; $18.25 at 12% (model §6). The deal price needs about 12.7% forever |
| Stable return on capital were 15% (a lasting competitive advantage) | $19.18; $20.10 at 20%, $21.03 at 30% (model §6). Value rises slowly |
| Stable beta were 0.80 instead of 1.00 | $17.74 (model §6); at 1.46, today's unlevered beta relevered at 21%, $13.36. The stable beta moves value more than the stable return does |
| Revenue grew at the 2022–2024 rate of 5.25% instead of the plan's 8.12% | $13.05 with the plan's margins; $9.89 with the margin held at 32.69%; $8.08 with it held at 2024's 29.11% on the plan's basis (model §6, `forecast.stress_cases`) |
| International revenue carried only the Western European premium | The cost of capital falls by roughly three-tenths of a point; value rises |
| Operating income fell 30% | The optimal debt ratio falls to 14% (model §4), and the over-leverage is worse |
| The cloud purchase commitments counted as debt | Debt rises by about 5%; value per share falls by the commitments' present value spread over 171.6M shares |
