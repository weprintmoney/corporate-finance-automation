---
title: "Colgate-Palmolive (CL) — Lesson 32: Terminal Value"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 32: Terminal Value

### Lesson 32 — Terminal Value

This is the lesson the valuation turns on. Two assumptions about the years after the forecast, the return Colgate earns on new investment and the rate it grows at forever, move the value per share more than everything in lessons 30 and 31 combined.

- **Lesson 32, Session 32 · Part 1 — "Capping the Growth Rate: How Long Should the Growth Period Last?"** ([transcript](../../04-dividends-and-valuation/lesson-32/session-32-part-1.md))
    - Quote: "The bigger your competitive advantages and the more sustainable they are, the longer your growth period can be."
    - Question for Colgate-Palmolive: How durable are Colgate-Palmolive's competitive advantages (switching costs, brand, network, cost position), and how long a growth period do they justify before the company is treated as mature? What evidence (retention, share, margins versus peers) supports the choice?
    - Sources needed: Returns and margins against the industry and peers; margin history; acquisition record; growth against the economy.
    - Where to find: model-output.md §8; ledger `facts.industry-averages-2026`, `facts.peer-medians-and-implied-prices`, `facts.growth-and-margin-history`, `facts.acquisitions-2018-2025`, `facts.sales-drivers-2025`, `facts.ginzu-replication-path`.
    - Answer: Colgate has no high-growth period left to size. Its sales grow about 3% a year, below the 4.82% riskfree rate that the course uses as a ceiling for growth forever. In the lecture's terms it is mature already. What its advantages buy is not faster growth but a high return on the capital it uses, and the question becomes how long that lasts.
      The advantage is brand: shoppers reach for a toothpaste they know, and stores must stock it. Evidence that it is real:
        - Return on invested capital of 34.56% against a cost of capital of 8.34% (model-output.md §8).
        - Gross profit of 60.1% of sales (`facts.growth-and-margin-history`).
        - An operating margin of 20.7% on Capital IQ's figures against a median of 16.5% for the ten companies on its comparison list and 18.0% for the six household and personal care companies (`facts.peer-multiples-capital-iq`, `facts.peer-medians-and-implied-prices`).
      Evidence on how durable and how wide it is:
        - The whole industry earns about the same: 34.42% after tax for US household products (`facts.industry-averages-2026`). The advantage belongs to branded staples as a category at least as much as to Colgate.
        - It does not travel. Colgate spent $3,894M buying businesses from 2018 to 2025 and wrote off $2,211M (`facts.acquisitions-2018-2025`). New money put to work outside the core has earned poorly.
        - It is being used up at the edges. The margin before write-downs fell from 24.0% in 2017 to 20.7% in 2025, and 2025 growth was all price, with volume down 0.4% (`facts.growth-and-margin-history`, `facts.sales-drivers-2025`).
      Market share and customer retention figures are not in our ledger, so the judgment rests on returns and margins.
      What we did with this. The workbook has a fixed ten-year forecast. Over those ten years Colgate's revenue grows 2.98% a year, almost the same as the 3% assumed afterwards, so the ten years are not a growth period in the usual sense. They are a period in which Colgate keeps earning what it earns today: the workbook's return on capital is 42.70% in the base year and 43.87% in year 10 (`facts.ginzu-replication-path`). After year 10 the existing business keeps its profits, and only new investment earns less, 20%. That is a generous treatment of the brand: ten more years at full strength, then a permanent advantage of more than twice the cost of capital on everything new.

- **Lesson 32, Session 32 · Part 2 — "Valuing a Mature Company and Avoiding the Terminal Value Inconsistency Trap"** ([transcript](../../04-dividends-and-valuation/lesson-32/session-32-part-2.md))
    - Quote: "If your net CapEx is zero, and your change in working capital is zero, you're reinvesting nothing, right?"
    - Question for Colgate-Palmolive: In Colgate-Palmolive's terminal year, what reinvestment rate is consistent with the perpetual growth rate and the stable return on capital? Does the forecast avoid the trap of capital spending that exactly offsets depreciation while growth continues?
    - Sources needed: Terminal-year cash flow; growth; stable return; recent reinvestment.
    - Where to find: ledger `facts.ginzu-replication-path`, `facts.ginzu-base-case-detail`, `facts.fcff-fcfe-2021-2025`; model-output.md §6.
    - Answer: 15%. The rule is: reinvestment rate = growth ÷ return on capital, so 3% ÷ 20% = 15%. In the terminal year after-tax operating income is $4,700M, reinvestment is $705M and the cash flow is $3,995M. The terminal value is that cash flow divided by the stable cost of capital less growth: $3,995M ÷ (8.43% − 3%) = $73,570M (`facts.ginzu-base-case-detail`, `facts.ginzu-replication-path`).
      The trap is real for Colgate, and the forecast avoids it. Colgate's actual reinvestment was negative in each of the last three years and −1.09% of after-tax income over five (`facts.fcff-fcfe-2021-2025`). Projecting that forever alongside 3% growth would be the exact error the quote describes: growth with nothing paid for it. The workbook instead charges $307M to $389M a year in years 1 to 10 and $705M in the terminal year. The repo model's cross-check shows the size of the trap: growing the final year's cash flow with no adjustment gives $64.93 a share against $60.85 with consistent reinvestment (model-output.md §6).

## Cumulative Project — Questions for This Lesson

- **When (in what year) will your firm be a mature firm (where you can estimated terminal value)?**
  It is mature now, by the test of growth. The terminal value is taken after year 10, which ends on 2036-09-30, because that is how the workbook is built, and we use that window for a different purpose: ten years in which Colgate keeps today's returns on everything it does.
  The choice of year matters little. The repo model's cross-check puts the terminal value after only three years and gives $60.85 a share (model-output.md §6) against the workbook's $61.83. When growth is about 3% before and after, moving the date changes almost nothing. What matters is what is assumed after it.
  One consequence should be stated plainly. The terminal value is 58.1% of the value of the operating business in the base case, and 85.4% in the three-year cross-check (`facts.ginzu-replication-path`). Most of Colgate's value lies beyond any year an analyst forecasts.

- **What will your firm's growth rate be in perpetuity after that point in time?**
  3%. A judgment; the reasons, and the alternative.
    - Evidence for about 3%: sales grew 3.3% a year from 2016 to 2025; analysts' revenue growth runs from 2.33% to 3.46% for 2027 and 2028 and 3.07% a year for 2027 to 2030 (`facts.growth-history-and-consensus`, `market.terminal_growth`).
    - The ceiling: no company can grow faster than the economy forever, and the course uses the riskfree rate, 4.82%, as the stand-in for the economy's long-run growth in dollars. 3% is under it.
    - The alternative is the workbook's default, growth equal to the riskfree rate. It gives $79.74 a share, $17.91 more (`facts.ginzu-base-case-detail`). We do not use it as the base because it would have Colgate growing faster forever than it has grown in the past nine years, in categories where volume is flat. It is quoted beside the base case every time.
  Why the choice is so sensitive here, when it often is not. If a company's new investments earn only their cost, growth adds no value and the growth rate hardly matters: with return equal to cost, value runs only from $50.79 to $53.82 across growth of 2% to 4.82%. At a 20% return each point of growth is worth much more: $56.20 to $79.74 over the same range (`facts.ginzu-sensitivities`). The two assumptions multiply each other.

- **What return on and cost of capital would you give your firm, when it becomes a mature firm?**
  Return on capital 20%; cost of capital 8.43%.
    - Return. A judgment. 20% is under half of the workbook's base-year return of 42.70% and well under the 34.42% the US household products industry earns (`forecast.stable_roic`, `facts.industry-averages-2026`). It is far above the 8.43% cost. The course's default is that the return on new investment falls to the cost of capital, on the argument that competition wears every advantage away in the end. We do not accept the default for a brand that has held for generations, and we do not accept today's return for new money either, given the acquisition record. The value at each choice, with growth at 3% (`facts.ginzu-sensitivities`):

      | Stable return on new investment | Value per share |
      |---|---|
      | 8.43%, equal to the cost of capital (the default) | $51.84 |
      | 10% | $54.55 |
      | 15% | $59.41 |
      | 20% (base case) | $61.83 |
      | 25% | $63.29 |
      | 34.56%, today's return | $64.90 |

    - Cost. 8.43% is the riskfree rate plus the mature-market premium of 3.61%, the cost of capital of an average-risk mature company (`facts.ginzu-inputs`). The workbook's own default, 9.05%, uses a premium from January with a riskfree rate from November; we replaced it so both come from the same date. Holding today's 8.34% forever would add $0.81 a share.
  The two defaults together, with the default 9.05% cost, give $50.90 a share. That is the all-defaults result, and it is quoted beside the base case throughout.

## Notes

The finding to carry forward. The value of Colgate rests on two assumptions about the distant future, not on the next five years:

| | Growth 3% | Growth 4.82% |
|---|---|---|
| Return on new investment equal to the cost of capital | $51.84 | $53.82 |
| Return on new investment 20% | $61.83 | $79.74 |

All four are below the $98.71 price. Changing every near-term input in lesson 31 within its plausible range moves value by a few dollars; these two assumptions move it by about $28 ($79.74 less $51.84). And no pair we tried reaches the price: even today's 34.56% return kept forever, with growth at the 4.82% ceiling, gives $87.70 (`facts.ginzu-sensitivities`). Holding the rest of the base case, growth forever would have to be 5.78%, above the riskfree rate, which the course treats as impossible (`facts.price-implied-assumptions`).

Confidence: low on the point estimate, and we say so. Nobody can observe what a new Colgate investment will earn in 2040. Moderate on the conclusion that the shares are worth less than $98.71. It holds in every cell of the table, but every cell uses the mature-company cost of capital of 8.43%. With the large-peer beta of 0.41 and its cost of capital of 6.77% held forever, a share is worth about $91.88 (`facts.ginzu-peer-beta-cases`). The conclusion rests on the cost of capital moving toward the mature-company rate over time, which is the workbook's default.

The grid figures other than the four cases read from the workbook come from the replication described in lesson 31.
