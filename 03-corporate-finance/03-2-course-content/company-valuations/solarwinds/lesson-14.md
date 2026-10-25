---
title: "SolarWinds (SWI) — Lesson 14: From Hurdle Rates to Cash Flows"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 14: From Hurdle Rates to Cash Flows

### Lesson 14 — From Hurdle Rates to Cash Flows

- **Lesson 14, Session 14 · Part 1 — "Show Me the Money: From Accounting Earnings to Cash Flows"** ([transcript](../../02-investment-returns-and-financing/lesson-14/session-14-part-1.md))
    - Quote: "It's not show me the accounting income, it's not show me the earnings, it's show me the money."
    - Question for SolarWinds: Starting from SolarWinds' operating income, what are the adjustments (depreciation, capital spending, working capital, expensed R&D) that get to free cash flow to the firm? How much of the gap between operating income and EBITDA is non-cash amortization versus real reinvestment?
    - Sources needed: EBIT, tax rate, depreciation and amortization, capital spending, working capital change, R&D expense, acquisition amortization, stock compensation.
    - Where to find: `inputs.yaml` fields `company.ebit`, `company.da`, `company.capex`, `company.change_wc`, `company.rd_expense`, `company.acquisition_amortization`, `company.sbc`; model-output.md §8.
    - Answer: Free cash flow to the firm (FCFF) = after-tax operating income + depreciation and amortization − capital spending − increase in working capital. With 2024 figures: after-tax EBIT $156.3M (208.4 × (1 − 0.25); model-output.md §8) + $74.4M − $20.5M − $38.8M = $171.4M (arithmetic). Notes on each step. Depreciation and amortization of $74.4M is added back because it is an expense that takes no cash. Capital spending of $20.5M is property and equipment $5.6M, capitalized software $14.4M and intangibles $0.5M (`company.capex` source). Working capital took $38.8M, mostly a $23.8M drop in income taxes payable and an $8.2M drop in accrued liabilities (`company.change_wc` note), so it is a one-off weight on 2024, not a trend. Stock-based compensation of $76.5M (`company.sbc`) is not added back: the ledger expenses it (`modeling_choices.sbc_treatment`), because it is paid in shares that dilute owners. Management's own 2025 FCFF is $212.0M (`forecast.years`), after subtracting stock compensation too. Expensed research and development is $108.6M (`company.rd_expense`), 13.6% of revenue. The lesson treats R&D as capital spending: it creates software that earns for years. We did not capitalize it. Doing so needs several years of R&D history and a life, the ledger has one year, and it changes operating income and invested capital but not cash flow, so FCFF stays at $171.4M. EBIT-to-EBITDA gap: standardized EBITDA of $282.8M less EBIT of $208.4M is $74.4M, which is all depreciation and amortization. Of it, $52.9M is amortization of acquired technologies and intangibles from the 2016 buyout and later deals (`company.acquisition_amortization`): non-cash, and no reinvestment in the business. The remaining $21.5M (74.4 − 52.9) is depreciation and amortization of equipment and capitalized software, and that is close to the $20.5M the company spends on capital each year. So about 71% of the gap (52.9 ÷ 74.4) is old acquisition cost wearing off, and the rest is replacing assets at roughly the pace they wear out (arithmetic).

- **Lesson 14, Session 14 · Part 2 — "Return on Invested Capital vs. Cost of Capital, and the Country Risk Premium"** ([transcript](../../02-investment-returns-and-financing/lesson-14/session-14-part-2.md))
    - Quote: "It looks like Disney is generating a 4.8% excess return over and above its cost of capital."
    - Question for SolarWinds: What return on invested capital did SolarWinds earn in the base year, does it clear the cost of capital, and does the answer flip if acquisition goodwill is excluded from invested capital?
    - Sources needed: EBIT, marginal tax rate, invested capital, goodwill, cost of capital.
    - Where to find: model-output.md §8 (and §1); `company.invested_capital`, `company.goodwill`.
    - Answer: Return on invested capital (ROIC) = after-tax operating income ÷ invested capital = $156.3M ÷ $2,348.0M = 6.66% (model-output.md §8). The cost of capital is 10.23%, so SolarWinds earned 3.58 points below its hurdle rate (−3.58%). Economic value added is −$84.0M: the capital base, valued at what it cost, earned $84.0M less than the capital charge (model-output.md §8). It does not clear the cost of capital. Goodwill: it is 100.65% of invested capital (model-output.md §8; $2,363.2M of goodwill against $2,348.0M). Excluding it, invested capital is −$15.2M (2,348.0 − 2,363.2; arithmetic). Return on a negative base has no meaning, so the answer does not flip to a number, it breaks. What it says: the operating assets SolarWinds uses to earn $156.3M are nearly all paid for by customers in advance (deferred revenue of $389.3M, `company.deferred_revenue`) and by suppliers, so the business earns a very high return on its tangible capital and a poor return on the price the 2016 buyers paid. Both views are correct and they answer different questions: the 6.66% judges the investment decision to buy the company; the ex-goodwill view describes the operating business. The 2022 impairment already wrote off $891.1M of goodwill (`company.history` note, 2022).

## Cumulative Project — Questions for This Lesson

- **What return on capital did your firm generate last year?**
  6.66%: after-tax operating income of $156.3M (taxed at the 25% marginal rate) on invested capital of $2,348.0M (model-output.md §8).

- **If you have returns on capital over time for your firm, is there a trend in those returns?**
  Rising from a low base. Invested capital barely moved (2022: $2,422.9M; 2023: $2,356.3M; 2024: $2,348.0M; `company.history`), so the movement comes from operating income: −$819.6M in 2022 as reported, $86.8M once the $906.4M of non-cash impairments (goodwill $891.1M plus indefinite-lived intangibles) is taken out, then $150.4M in 2023 and $208.4M in 2024. The model's §8 "By year" table gives ROIC of 2.69% in 2022, 4.79% in 2023 and 6.66% in 2024. Years before 2022 include N-able and are not comparable (`company.history` note).

- **How do the returns on capital (equity) compare to the costs of capital (equity)?**
  Return on equity is 7.99% ($111.9M net income ÷ $1,400.7M book equity) against a cost of equity of 12.65%, a shortfall of 4.66 points (model-output.md §8). Return on capital is 6.66% against a 10.23% cost of capital, a shortfall of 3.58 points. Both are below the hurdle. 2024 net income also includes interest costs of $112.4M, which is why the equity gap is the wider one.

- **Is there a typical project for this firm? If yes, what does it look like in terms of life (long term or short term), investment needs and cash flow patterns?**
  Two kinds. (1) Product development: a small, repeated investment. The company spent $108.6M on R&D (expensed) and $14.4M on capitalized software in 2024; capitalized internal-use software is amortized over three years and equipment over 3 to 5 (10-K note 2; `company.depreciation_life_change`). Cash pattern: money out first in salaries, then paid back over years of renewals (net retention 99% and 97% maintenance renewals, facts.net-retention-subscription, facts.maintenance-renewal-rate), with customers often paying a year ahead. Short to medium life; low capital needs (capital spending of $20.5M on $796.9M of revenue). (2) Acquisitions: large, lumpy, long-lived, and funded with debt. They created the $2,363.2M of goodwill and $52.9M a year of amortization. The firm's returns on capital are set by these, not by the product projects.

- **Are the projects in the future likely to look like the projects in the past? Why or why not?**
  Mostly the first kind. The credit agreement restricts new debt, investments and acquisitions (`debt.covenants`), the debt is 33% of firm value against an estimated 21% optimum (model-output.md §3), and management's forecast is organic: revenue from $832.0M in 2025 to $1,273.0M in 2030, operating margin from 32.69% to 40.14% (`forecast.years`). That plan assumes growth with little reinvestment: 2030 FCFF of $419.0M exceeds after-tax EBIT of $383.3M (511.0 × 0.75; arithmetic), so cash flow is larger than the profit. The reason is a forecast $46M rise in deferred revenue and cash taxes near 25% of EBIT (`facts.forecast-2030-detail`), not depreciation running ahead of capital spending: in 2030 D&A is $25M and capex $27M. That cannot hold if the company grows forever. The terminal value in the DCF corrects this by reinvesting 25.00% of operating income (model-output.md §6). The honest difference from the past: the history is dominated by acquisition goodwill, the forecast has none, and a returns-on-capital figure built on the forecast would be far higher than 6.66% because it would carry no goodwill.

## Skipped

- None.

## Notes

SolarWinds earned 6.66% on a capital base that is 100.65% goodwill, against a cost of capital of 10.23%. Value was destroyed on the price paid in 2016, but the operating business generates $171.4M of free cash flow on almost no tangible capital. That tension shapes later lessons: the DCF in model-output.md §6 values the cash flows and not the accounting capital, and the stable ROIC of 10% in the terminal value (`forecast.stable_roic`) is set equal to the cost of capital, so growth after 2030 adds no value.

Ledger and model observations: the ROIC section of the model (§8) gives one year only. The trend figures above for 2022 and 2023 come from `company.history` and are listed in the run report as derived facts.
