---
title: "SolarWinds (SWI) — Valuation Report"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Valuation Report

Valued as of 2025-02-05, the last undisturbed trading day before Turn/River's $18.50 cash offer was announced. Every number cites the ledger (`inputs.yaml` field) or the model (`model-output.md` section). The working for each step is in `lesson-01.md` … `lesson-36.md`; the plain-language version is `walkthrough.md`.

## 1. Company and story

SolarWinds sold IT monitoring software to network and systems engineers, a business it was moving from perpetual licenses to subscriptions. In FY2024 revenue was $796.9M, operating income $208.4M and net income $111.9M (`company.revenue`, `company.ebit`, `company.net_income`). Revenue grew from $758.7M in 2023 (`company.history`). A company growing about 5% a year at a 26% operating margin is a mature business. Management's own plan in the deal document called for 8.12% annual revenue growth to 2030 (`forecast.management_growth`). The plan carried the EBIT margin from 32.69% in 2025 to 40.14% in 2030 (`forecast.years`).

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
- 10.23% sits inside Goldman's range. Their per-share DCF ranges were $14.30 to $23.70 (Goldman) and $14.70 to $19.70 (Jefferies, with stock-based compensation charged) (`facts.gs-dcf-range`, `facts.jefferies-dcf-range`). Both contain this report's $15.63, near their low ends. Section 6 explains the remaining gap to their midpoints.

## 3. Investment returns

SolarWinds earned a return on invested capital of 6.66% against its 10.23% cost of capital. That destroyed $84.0M of value in FY2024 on an economic-value-added basis (model §8). Return on equity was 7.99% against a 12.65% cost of equity.

The book measure is distorted. Invested capital of $2,348.0M is all goodwill from the 2016 buyout (goodwill is 100.65% of it, model §8). Strip out the goodwill and the operating assets earn far more than the capital tied up in them. What fails the test is the price Silver Lake and Thoma Bravo paid in 2016. For a new owner the relevant question is not past returns but whether new investment earns its cost. Management's forecast reinvests little. In 2030, capital spending is $27M against depreciation and amortization of $25M, and the cash flow is lifted by $46M of new deferred revenue (`facts.forecast-2030-detail`).

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

Cash flows are management's 2025–2030 forecast (`forecast.years`) with stock-based compensation charged as an expense: free cash flow to the firm rises from $212.0M to $419.0M. They are discounted at 10.23% (model §6). The terminal value is capitalized at the stable-period cost of capital of 8.51% and discounted back to today at 10.23%.

| Bridge | Status quo | At the optimal mix |
|---|---|---|
| Present value of 2025–2030 cash flows | $1,321.6M | |
| Present value of terminal value | $2,574.0M | |
| Enterprise value | $3,895.6M | $3,932.6M |
| Less debt, plus cash | debt $1,285.0M, cash $259.3M | |
| − Options and restricted stock | $187.0M | |
| **Value per share** | **$15.63** | **$15.85** |

**The terminal value is the whole argument.** The model shows two methods (model §6):
- **Final-year cash flow grown at 2.5% forever:** $7,150.4M.
- **Operating income less the reinvestment needed to grow at 2.5%** (lesson 32's consistent-reinvestment method, at a stable return on capital of 8.51%): $4,618.8M.

In management's 2030 forecast, free cash flow of $419.0M is larger than after-tax operating income. Capital spending ($27M) barely exceeds depreciation ($25M), and customers prepay $46M more in deferred revenue than the year before (`facts.forecast-2030-detail`). Deferred revenue can grow that fast only while the business grows fast, not forever. Growing that cash flow forever assumes SolarWinds grows without ever reinvesting, which no company can do. The course method costs $2,531.6M of terminal value. That is the difference between $23.86 a share, above the deal price, and $15.63 (model §6). Matching the final-year cash flow would need reinvestment of −9.33% of operating income forever: the company would have to shrink its capital while growing.

**The stable-period cost of capital.** Lesson 32 says a firm in stable growth looks like the average firm: beta moves toward one, debt moves toward its optimum, and excess returns fade. So the terminal value does not use today's 10.23%, which rests on a beta of 1.6714 and 33% debt. It uses a beta of 1.00 and the 21% optimum from section 4. Cost of equity is 4.43% + 1.00 × 4.92% = 9.35%. The after-tax cost of debt stays at 5.33%, and the stable cost of capital is 79% × 9.35% + 21% × 5.33% = 8.51% (model §6). The stable return on capital is set equal to it, 8.51%, so growth after 2030 adds no value, and that sets terminal reinvestment at 2.5% ÷ 8.51% = 29.38% of operating income. The sensitivity shows what a lasting advantage would be worth: $16.56 at a 10% return on capital, $18.33 at 15%, $19.22 at 20% and $20.10 at 30% (model §6). Even at 30% the value stays below the $23.86 of the no-reinvestment method.

Against the prices, $15.63 is 1.03 times the $15.18 market price and 0.85 times the $18.50 deal price (model §6). Other per-share shortcuts:
- **Diluted shares:** dividing by them instead of subtracting options gives $16.45.
- **Optimal debt ratio:** moving to it adds $0.22 a share ($15.85) in the DCF, because the terminal value already assumes the 21% optimum and only the 2025–2030 years gain. The other two measures give more: annual savings capitalized give $0.84 a share and adjusted present value $1.28 (model §6 reconciliation, §9). They differ in basis. The DCF prices today's debt at its actual 7.11% rate, while the other two price both ends on the synthetic ratings.

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

On the rates of 2025-02-05, SolarWinds as run was worth about $15.63 a share to a diversified investor. That is close to the $15.18 it traded at (1.03 times) and 85% of the $18.50 Turn/River paid. Three things could close the $2.87 gap to the deal price ($18.50 − $15.63), and only one is in this model:
- **Financing:** moving to the optimal debt ratio is worth $0.22 a share (model §6).
- **Terminal value:** the deal price is reached only if SolarWinds earns a stable return on capital of about 16% or more forever ($18.33 at 15%, $19.22 at 20%). That is a lasting competitive advantage, the opposite of the ledger's judgment that growth after 2030 adds no value.
- **Control:** a private-equity buyer can cut costs and lever up in ways a public company with a diffuse float cannot. The lesson 34 answer sizes the operating levers as judgment calls, not model outputs.

For the public stockholders, $18.50 was still a full price: 21.9% above the unaffected $15.18, and above the $15.63 intrinsic value on a consistent-reinvestment basis, but not a windfall over it. For Silver Lake and Thoma Bravo, it was an exit at a price inside both advisers' DCF ranges. Our reading, not stated in the deal document, is this: $15.63 sits inside both ranges near their low ends, and the remaining gap to their midpoints is mainly because the advisers grew the final-year cash flow at 2% to 3.5% (`facts.gs-perpetuity-growth-range`, `facts.jefferies-perpetuity-growth-range`), which gives $23.86 here. That method assumes no reinvestment.

The board's process is the governance weakness. The two sponsors' consent rights meant the 34% public float had no vote. The CEO's $22.99M golden parachute (`governance.change_of_control_payouts`) was mostly $19.94M of accelerated equity that paid on closing. That tied management's reward to getting a deal done rather than to long-run value.

## What would change the answer

| If | Then |
|---|---|
| Stable return on capital were higher than 8.51% (lasting competitive advantage) | Value rises, but slowly: $16.56 at 10%, $18.33 at 15%, $19.22 at 20%, $20.10 at 30% (model §6). The deal price needs about 16% or more forever |
| International revenue carried only the Western European premium | The cost of capital falls by roughly three-tenths of a point; value rises |
| Operating income fell 30% | The optimal debt ratio falls to 14% (model §4), and the over-leverage is worse |
| The cloud purchase commitments counted as debt | Debt rises by about 5%; value per share falls by the commitments' present value spread over 171.6M shares |
