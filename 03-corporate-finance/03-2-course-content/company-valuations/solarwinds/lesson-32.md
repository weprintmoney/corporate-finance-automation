---
title: "SolarWinds (SWI) — Lesson 32: Terminal Value"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 32: Terminal Value

### Lesson 32 — Terminal Value

- **Lesson 32, Session 32 · Part 1 — "Capping the Growth Rate: How Long Should the Growth Period Last?"** ([transcript](../../04-dividends-and-valuation/lesson-32/session-32-part-1.md))
    - Quote: "The bigger your competitive advantages and the more sustainable they are, the longer your growth period can be."
    - Question for SolarWinds: How durable are SolarWinds' competitive advantages (switching costs, brand, network, cost position), and how long a growth period do they justify before the company is treated as mature? What evidence (retention, share, margins versus peers) supports the choice?
    - Sources needed: Retention and customer-count disclosures; revenue and margin history; peer growth and margins; the buyers' 2023 market check.
    - Where to find: `sources/filings/swi-10k-fy2024.md` MD&A (net retention rate, Total ARR, customers above $100,000); `company.history`; `peers`; `sources/deal-docs/swi-defm14c-2025-merger.md` Background of the Merger.
    - Answer: Six years, 2025 to 2030 (`forecast.growth_period_years` = 6), which is management's own forecast window. The moat is real but it defends, it does not expand. For:
        - Retention. Subscription net retention was 99% in 2024 and 97% in 2023 (`facts.net-retention-subscription`, `facts.net-retention-subscription`). Customers kept what they bought and bought almost nothing more.
        - Stickiness. Customers with more than $100,000 of annual recurring revenue rose from 979 to 1,148 (`facts.customers-over-100k-arr`). Total ARR was $729.0M, up 6.6% (`facts.total-arr-2024`). There was no exodus after the 2020 SUNBURST attack: revenue went 719.4, 758.7, 796.9 ($M, `company.history`), about 5.0% in 2024.
        - Margins. GAAP EBIT margin is 26.2% ($208.4M ÷ $796.9M, `company.ebit`, `company.revenue`) against a peer median of 15.9% (median of `peers[].ebit_margin`, my arithmetic). Customers pay for software they do not leave, which is what a switching-cost moat looks like.
        - Against a longer period. Growth is 5.0%, close to the peer median of 4.1% (`peers[].growth`), so there is no share gain. In the 2023 market check, three sponsors that had signed on dropped out in November 2023, citing the early stage of the subscription transition and doubt that it would succeed (deal document, Background of the Merger). The only price indication, from "Party A", was about $14.00 a share (`facts.market-check-2023`).
        - Against a shorter one. Management's plan has revenue growing 8.12% a year (`forecast.management_growth`) and EBIT margin rising from 26.2% to 40.14% by 2030 (`forecast.years`). A shorter period would cut the margin ramp. We did not cut it because the plan is the status-quo story and the course asks us to value that first.
        - Judgment call. Six years, with the plan's growth treated as optimistic against a 5.0% history. A shorter period is arguable; a longer one has no support in the retention data.

- **Lesson 32, Session 32 · Part 2 — "Valuing a Mature Company and Avoiding the Terminal Value Inconsistency Trap"** ([transcript](../../04-dividends-and-valuation/lesson-32/session-32-part-2.md))
    - Quote: "If your net CapEx is zero, and your change in working capital is zero, you're reinvesting nothing, right?"
    - Question for SolarWinds: In SolarWinds' terminal year, what reinvestment rate is consistent with the perpetual growth rate and the stable return on capital? Does the forecast avoid the trap of capital spending that exactly offsets depreciation while growth continues?
    - Sources needed: Terminal growth rate, stable ROIC, management's 2030 cash flow and EBIT, capex and D&A history.
    - Where to find: `market.terminal_growth`, `forecast.stable_roic`, `forecast.years`, `company.capex`, `company.da`, `company.acquisition_amortization`; model-output.md §5 and §6.
    - Answer: The consistent reinvestment rate is 25.00% (g ÷ stable ROIC = 2.5% ÷ 10.00%, model-output.md §6). The forecast does not avoid the trap.
        - Management's 2030 unlevered free cash flow (FCFF) after stock compensation is $419.0M (`forecast.years`). EBIT in 2030 is $511M (1,273.0 × 40.14%), or $383.3M after 25% tax. FCFF above after-tax EBIT means net reinvestment of about −$35.7M, a reinvestment rate near −9% (my arithmetic: 419.0 − 383.3 = 35.7). The gap comes from a forecast +$46M change in deferred revenue and cash taxes near 25% of EBIT (`facts.forecast-2030-detail`). It does not come from depreciation running ahead of capital spending: in 2030 D&A is $25M and capex $27M.
        - The model's terminal value, with consistent reinvestment, is $3,808.9M. Growing the final-year FCFF at g instead gives $5,552.5M (model-output.md §6). The difference is $1,743.6M at 2030.
        - Discounted at the 2030 factor of 0.5573 and divided by 171.6M shares, that difference is about $5.67 a share. The status-quo DCF is $13.00 (§6); with the plan's terminal cash flow it would be $18.67 (§6, "value per share with the other terminal value"), nearly the $18.50 deal price. The deal price is what the plan is worth if cash flow can grow forever with no reinvestment.
        - The 10% stable return is not what separates $13.00 from the deal price. The model's sensitivity (§6) gives value per share of $13.00 at 10% (ledger), $13.10 at 10.23%, $13.69 at 12%, $14.38 at 15%, $15.07 at 20% and $15.75 at 30%. Even a 30% return on new capital stays below $18.67. The final-year-FCFF terminal value implies terminal reinvestment of −9.33%, so no positive return on capital reaches it; only negative reinvestment forever does.
        - The capex and D&A trap shows up in the history too. 2024 capex was $20.5M against D&A of $74.4M, net capex of −$53.9M (model-output.md §5). Of that D&A, $52.9M is amortization of intangibles acquired in the 2016 buyout (`company.acquisition_amortization`), a non-cash charge. The gap is not hidden shrinkage of the operating base, but it means the base-year cash flow flatters a company that reinvests little. The terminal year must not copy it.

## Cumulative Project — Questions for This Lesson

- **When (in what year) will your firm be a mature firm (where you can estimated terminal value)?**
  2030, the last year of management's forecast (`forecast.growth_period_years` = 6). SolarWinds already grows near 5.0%, so "mature" here means the point where we stop trusting the plan's margin ramp, not a sudden change in the business.

- **What will your firm's growth rate be in perpetuity after that point in time?**
  2.5% (`market.terminal_growth`). It sits below the 4.43% risk-free rate (`market.risk_free_rate`), the cap the lecture sets, and between Goldman Sachs' 2%–3% and Jefferies' 2.5%–3.5% perpetuity ranges (`facts.gs-dcf-range`, `facts.jefferies-dcf-range`).

- **What return on and cost of capital would you give your firm, when it becomes a mature firm?**
  Return on capital 10% (`forecast.stable_roic`). Cost of capital 10.23%, the current rate, held into the terminal year (model-output.md §1 and §6; the ledger has no separate stable-period rate). A 10% return against a 10.23% cost means growth after 2030 adds no value. That is a judgment: SolarWinds earned about 6.7% on book invested capital in 2024 (EBIT × (1 − 25%) = $156.3M ÷ $2,348.0M, my arithmetic), but $2,363.2M of that capital is goodwill from the 2016 buyout (`company.goodwill`), so book capital overstates what the business needs. 10% is above the book return and below the cost of capital, so it gives no credit for excess returns. We did not lower the cost of capital for maturity: the debt ratio and beta have no stated path to change.

## Notes

Lesson 32 sets the terminal value, which is 62% of the DCF enterprise value ($2,122.7M of $3,444.3M, model-output.md §6). The six-year period and 2.5% growth are inputs; the large judgment is the terminal reinvestment rate. The ledger's `terminal_method: consistent_reinvestment` replaces the shortcut of growing the final-year cash flow, which assumes no reinvestment in perpetuity. Lesson 34 uses the $13.00 this produces, and lesson 36 uses the $5.67 gap to explain the deal price.

Ledger gap: `forecast.wacc_stable` is listed as an input for these questions but is not in the ledger; the model uses the current cost of capital in the terminal year.
