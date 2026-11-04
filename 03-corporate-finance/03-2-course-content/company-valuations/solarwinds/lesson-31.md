---
title: "SolarWinds (SWI) — Lesson 31: Estimating Growth in Cash Flows"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-11-03
---

# SolarWinds (SWI) — Lesson 31: Estimating Growth in Cash Flows

### Lesson 31 — Estimating Growth in Cash Flows

- **Lesson 31, Session 31 · Part 1 — "Growth Has to Be Earned: Reinvestment, Return, and the Fundamental Growth Rate"** ([transcript](../../04-dividends-and-valuation/lesson-31/session-31-part-1.md))
    - Quote: "The growth of a company is not something that you and I can come up with or endow the company with."
    - Question for SolarWinds: What growth rate do SolarWinds' actual reinvestment rate and return on invested capital justify, and how does it compare with management's plan and analysts' numbers? If the company is growing faster than the fundamentals allow, where is the growth coming from?
    - Sources needed: Return on invested capital, reinvestment rate, management's forecast, analyst growth.
    - Where to find: model-output.md §8; lesson 30; `forecast.management_growth`, `forecast.years`; `forecast.analyst_growth` is omitted (consensus did not load from Capital IQ, `meta.omitted`).
    - Answer: The fundamentals justify roughly zero growth. Actual growth is about 5%, and management's plan is 8%.
        - Return on invested capital is 6.66% (§8). Reinvestment rate is −9.66% on the reported basis (§8), so expected growth = −9.66% × 6.66% = −0.64% (facts.fundamental-growth-2024). On the alternative basis that leaves out acquisition amortization, 24.18% × 6.66% = 1.61% (same fact). Either way, under 2%.
        - Actual: revenue grew 5.25% a year from 2022 to 2024 ($719.4M to $796.9M, `company.history`; arithmetic).
        - Management: 8.12% a year, revenue $796.9M to $1,273.0M by 2030 (`forecast.management_growth`). Analyst growth: not available (omitted).
        - Where the growth comes from: not from capital. Invested capital fell from $2,422.9M to $2,348.0M over 2022–2024 while revenue rose. Management's plan has free cash flow above after-tax operating income every year, a cumulative $163.1M of negative reinvestment over 2025–2030 (facts.plan-reinvestment) while revenue rises $476.1M. The 10-K MD&A attributes the 2024 increase to subscription revenue, partly offset by lower license revenue. Research and development of $108.6M (`company.rd_expense`) is expensed, so it does not appear as reinvestment even though it is how a software company buys growth. That is the fair argument for the plan, and the reason the zero-growth figure is a floor on the reinvestment side, not a forecast.

- **Lesson 31, Session 31 · Part 2 — "From ROE Decomposition to a Revenue-Based Growth Model"** ([transcript](../../04-dividends-and-valuation/lesson-31/session-31-part-2.md))
    - Quote: "This approach to estimating growth based on fundamentals works if you have a stable return on equity and a stable return on capital."
    - Question for SolarWinds: Are SolarWinds' margins and returns stable enough for the fundamental growth formula? If not, what revenue growth, margin path and sales-to-capital ratio should drive the forecast, and what does the company's own history say that ratio is?
    - Sources needed: Margin and return history; revenue-to-capital ratio; peers' growth and margins.
    - Where to find: `company.history`; `company.invested_capital`; `company.rd_expense`; `peers`; `forecast.sales_to_capital` is not in the ledger.
    - Answer: Not stable. A revenue-based model fits better, but the history yields no usable sales-to-capital ratio.
        - Margins: EBIT margin without the impairment was 12.1% in 2022, 19.8% in 2023 and 26.2% in 2024 (EBIT $86.8M, $150.4M, $208.4M over revenue; arithmetic). ROIC rose from 2.69% to 4.79% to 6.66% (§8). Both are moving, so one year's reinvestment rate times one year's return is a weak guide.
        - Management's path: revenue $832.0M in 2025 to $1,273.0M in 2030, EBIT margin 32.7% to 40.1% (`forecast.years`).
        - Peers (`peers`): revenue growth ranges from −9.3% to 28.6% with a median of 4.05%; EBIT margin median 15.92% (facts.peer-median-growth-margin). SolarWinds' 5.0% growth is near the peer median; its 26.2% margin is far above it. The peer rows carry no invested capital, so no peer sales-to-capital.
        - Sales to capital, own history: revenue over book invested capital was 0.30, 0.32 and 0.34 in 2022–2024 (arithmetic from `company.history`), but 100.65% of invested capital is goodwill (§8), so that ratio says nothing about what new growth costs. Incrementally, 2024 added $38.2M of revenue with $37.8M of reinvestment on the alternative basis, a ratio near 1.0; on the reported basis reinvestment was negative and the ratio is undefined. This is an estimate with a wide range, and it is not used in the model.
        - What drives the forecast here: management's revenue and margin path for 2025–2030 (§6), with the terminal reinvestment forced by growth 2.5% over a stable ROIC of 8.23%, equal to the stable cost of capital, i.e. 30.38% (§6). R&D at 13.6% of revenue (108.6 ÷ 796.9) is already inside EBIT.

## Cumulative Project — Questions for This Lesson

- **What is the historical growth rate in your company's revenues? EBIT? Net income?**
  Revenue: 5.25% a year from 2022 to 2024 (`company.history`), 5.5% in 2023 and 5.0% in 2024. From the 2021 recast revenue of $718.6M (facts.revenue-2021) the three-year rate is 3.5%. EBIT: 2022 was $-819.6M with $906.4M of non-cash impairments, $86.8M without them (§8); to 2024's $208.4M that is a 54.9% a year rise, and 38.6% from 2023 alone. A rate off a base that small mostly measures recovery from SUNBURST costs and impairment. Net income: $-929.4M, $-9.1M, $111.9M, a negative base, so no growth rate can be computed; the 2024 figure includes an $8.1M tax benefit (facts.tax-benefit-2024).

- **What are analysts or managers projecting as an expected growth rate in the future?**
  Management: 8.12% a year in revenue to 2030 (`forecast.management_growth`), with operating margin from 32.7% to 40.1%. Analysts: not available; consensus estimates did not load and the field is omitted (`meta.omitted`).

- **Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?**
  Operating income: ROIC 6.66% × reinvestment rate −9.66% = −0.64%, or 1.61% on the alternative reinvestment basis (§8; facts.fundamental-growth-2024). Net income: ROE 7.99% (§8) × equity reinvestment rate of −13.5% (net capex −$53.9M plus working capital $38.8M, less net new debt $0.0M, over net income $111.9M) = −1.1% (facts.fundamental-growth-equity-2024). Essentially zero growth.

- **If margins are changing, what are your estimates of revenue growth, margins and reinvestment for the future?**
  The valuation uses management's path for 2025–2030: revenue growth about 8.12% a year, EBIT margin 32.7% to 40.1% and free cash flow $212.0M to $419.0M (`forecast.years`), then 2.5% growth with 30.38% reinvestment (2.5% over a stable return on capital of 8.23%, equal to the stable cost of capital, §6). The plan's explicit years assume no net reinvestment, which is the main judgment in the DCF: it is the difference between terminal values of $7,490.2M and $4,769.8M (§6). The model also runs the plan at the 2022–2024 revenue rate of 5.25% instead of 8.12% (`forecast.stress_cases`; §6 stress cases): with the plan's margins, value per share is $12.65, $3.01 below the plan's $15.66; with the margin held at the plan's first-year 32.69%, $9.57, $6.09 below; with the margin held at 2024's 29.11% on the plan's basis, $7.79, $7.87 below. The margin basis matters: the plan defines EBIT as adjusted EBITDA − stock-based compensation − D&A (2025: 412 − 82 − 58 = 272, `forecast.stress_cases` source), and on that definition 2024's margin was 29.11% (adjusted EBITDA $384.7M − SBC with payroll taxes $78.3M − D&A $74.4M = $232.0M, ÷ revenue $796.9M; same source). The GAAP operating margin of 26.15% carries restructuring, cyber-incident and acquisition costs and is not the comparable floor. The growth is worth $3.01 a share; the margin expansion is worth more.

## Notes

The central finding for lessons 32 and 34: the plan's growth is paid for by operating margin, subscription pricing and expensed R&D, not by visible capital, and the fundamentals formula returns about zero. The §6 stress cases price the plan against the history: at the 5.25% revenue rate the value is $12.65 a share with the plan's margins, and $9.57 or $7.79 with the margin held at 32.69% or at 2024's 29.11% on the plan's basis, against $15.66 on the plan. The $15.18 market price sat between the history-based $12.65 and the plan-based $15.66, nearer the plan (84% of the way, my arithmetic), and it did so without having seen the plan: the forecast was published in the information statement (`sources/deal-docs/swi-defm14c-2025-merger.md`, dated 2025-03-27 in the ledger facts), after the 2025-02-05 unaffected date. The ledger has no `forecast.sales_to_capital` and no analyst growth. Return and growth figures for 2022 and 2023 are arithmetic on `company.history`; the model's §8 covers the base year only.
