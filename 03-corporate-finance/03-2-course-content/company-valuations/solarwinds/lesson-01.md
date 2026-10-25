---
title: "SolarWinds (SWI) — Lesson 01: Valuation: The Big Picture / What is Corporate Finance?"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 01: Valuation: The Big Picture / What is Corporate Finance?

### Lesson 01 — Valuation: The Big Picture / What is Corporate Finance?

- **Lesson 01, Session 1 · Part 1 — "The Financial Balance Sheet and the Singular Objective of Maximizing Firm Value"** ([transcript](../../01-foundations-and-discount-rates/lesson-01/session-1-part-1.md))
    - Quote: "You want to make your business the most valuable business you can."
    - Question for SolarWinds: Split SolarWinds' balance sheet into assets in place and growth assets. In the base year, how did capital allocation (R&D, capital spending, acquisitions) divide between defending the existing business and funding growth, and does that split match what management says the strategy is?
    - Sources needed: FY2024 R&D, capital spending and acquisition cash; revenue by type; any segment split; management's stated strategy.
    - Where to find: `sources/filings/swi-10k-fy2024.md` (income statement, cash flow statement, Item 1, Note 16); ledger `company.rd_expense`, `company.capex`, `company.history`, `governance.objectives`.
    - Answer: No filing splits SolarWinds into legacy and growth. It reports one segment, and the chief executive allocates resources at the consolidated level (10-K FY2024, Note 16). So the split is a proxy by revenue type, and it is a judgment. Assets in place: the perpetual-license base, which is maintenance revenue of $440.6M plus license revenue of $51.8M, $492.4M or 61.8% of the $796.9M revenue (`facts.maintenance-revenue`, `facts.license-revenue`, `company.revenue`). Growth assets: the subscription products, $304.5M or 38.2% of revenue, up from $234.2M (`facts.subscription-revenue`, `facts.revenue-subscription-2023`). Much of that subscription growth is existing customers converting rather than new buyers (lesson 3). Where the money went in FY2024: R&D $108.6M, 13.6% of revenue (`company.rd_expense`); capital spending $20.5M including capitalized software, 2.6% of revenue (`company.capex`); acquisitions $0 (`facts.acquisitions-cash-2024`). R&D plus capital spending is $129.1M. The special dividend was $168.2M (`company.history`, 2024 `dividends`), 1.30 times that. R&D rose $8.4M, but $13.3M of the rise came from moving the product-management team out of sales and marketing (`facts.rd-reorg-increase-2024`), so underlying R&D fell. Capital spending ran $53.9M below depreciation and amortization of $74.4M (`company.da`; model-output.md §5, net capex −$53.9M). Does it match the strategy? Management says it intends to "extend our leadership in observability and IT infrastructure management and grow our market share in adjacent areas" through a "subscription-first approach" (`governance.objectives`). The subscription push is paid for out of R&D and the existing sales team, with no acquisitions. The largest discretionary use of cash in the year was the payout to shareholders, not growth.

- **Lesson 01, Session 1 · Part 2 — "Companies Age Like Human Beings — Placing the Company on the Corporate Life Cycle"** ([transcript](../../01-foundations-and-discount-rates/lesson-01/session-1-part-2.md))
    - Quote: "The third theme is that companies, just like human beings, age."
    - Question for SolarWinds: Where does SolarWinds sit on the corporate life cycle, judged by revenue growth, margins, reinvestment, and how it uses cash? Does management's behaviour (acquisitions, payouts, any sale of the business) agree with that placement, or is the company refusing to act its age?
    - Sources needed: revenue, margin and reinvestment history; payout history; the sale process; management's forecast.
    - Where to find: ledger `company.history`, `company.capex`, `company.rd_expense`, `forecast.management_growth`; model-output.md §5; `sources/deal-docs/swi-defm14c-2025-merger.md` (Background of the Merger).
    - Answer: Mature, with a plan that assumes it is younger than it is. Revenue grew 5.0% in 2024 ($758.7M to $796.9M; `company.history`) and 5.5% in 2023 ($719.4M to $758.7M). The GAAP operating margin was 26.2% ($208.4M ÷ $796.9M; `company.ebit`), and the company's own adjusted EBITDA margin was 48.3% (`company.ebitda_adjusted` note). Reinvestment was light: capital spending was below depreciation in all three years on file (model-output.md §5). Cash went out, not in: a $1.50 a share special dividend of $237.2M in 2021 (`facts.special-dividend-2021`) and a $1.00 a share dividend of $168.2M in 2024 (`company.history`). Free cash flow to equity was $127.0M in 2024 against $194.7M returned (model-output.md §5). Those are the habits of a mature firm. The sale agrees with the placement. In 2023 the board and its two banks approached 13 buyers; three submitted indications in October 2023, and all three withdrew by 2023-11-23, citing the early stage of the subscription transition (`facts.market-check-2023`). Turn/River then offered $18.50 a share (`company.deal_price`), a 21.9% premium to the $15.18 unaffected price (arithmetic, $18.50 ÷ $15.18 − 1). The one place it refuses to act its age is the forecast: management's 2025–2030 plan grows revenue 8.12% a year (`forecast.management_growth`), against the 5.0% just reported. The DCF in lesson 32 tests that.

## Module 1 Step — Questions for This Lesson

- **Pick a company**
  - Which company, and why is it a good subject (data available, decisions to judge)? SolarWinds Corporation (NYSE: SWI), type `delisted`, FY2024 base year, valued as of 2025-02-05 (`meta`). Data: four annual reports, the 2024 proxy and a 2025 merger information statement with management's forecast, two fairness opinions and the full sale chronology (`sources/README.md`). Decisions to judge: two special dividends, 33.03% debt in its capital (model-output.md §1), a control group of two private equity firms, and a sale at $18.50 a share. Limits: no price history survives, so no regression beta (`meta.omitted`).
  - Where does it sit on the corporate life cycle, judged by growth, margins, reinvestment and cash use? Mature: 5.0% growth, 26.2% GAAP operating margin, capital spending below depreciation, cash paid out. See Part 2 above.

## Notes

This lesson fixes the frame. SolarWinds is a mature, cash-paying software company whose management plan assumes faster growth than it has delivered. No filing splits legacy from growth, so every later split (lesson 3's recurring revenue, lesson 28's peers) is a proxy and says so. Lesson 13 tests whether the 2016 buyout goodwill ($2,363.2M, `company.goodwill`) earns its keep, and lessons 22–26 take "mature, pays out cash" as the starting point for dividend policy. The pattern, not a single figure, is what carries forward: the dividend was larger than reinvestment.
