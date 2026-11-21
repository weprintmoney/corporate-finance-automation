---
title: "Colgate-Palmolive (CL) — Lesson 15: Time Weighting Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 15: Time Weighting Cash Flows

### Lesson 15 — Time Weighting Cash Flows

- **Lesson 15, Session 15 · Part 1 — "Sunk Costs, Non-Incremental G&A, and Time-Weighting Cash Flows"** ([transcript](../../02-investment-returns-and-financing/lesson-15/session-15-part-1.md))
    - Quote: "The first rule in capital budgeting is you have sunk cost, money were already spent, don't consider them."
    - Question for Colgate-Palmolive: For Colgate-Palmolive's typical project (an acquisition, a product line, a plant), which costs already spent are sunk, and which allocated overheads are truly incremental? What does a typical project look like in life, investment needs and cash-flow pattern?
    - Sources needed: Capital spending, R&D, advertising, acquisition history, corporate overhead.
    - Where to find: ledger `company.capex`, `company.rd_expense`, `facts.uses-of-cash-2025`, `facts.acquisitions-2018-2025`, `facts.skin-health-writedown-2025`, `facts.segment-results-2025`, `facts.restructuring-program-2025`.
    - Answer: Take the three kinds of project from lesson 14.
        - A new product line under an existing brand (a new toothpaste, a new pet food formula). Sunk: the research already done ($366M a year company-wide) and the decades of advertising behind the brand name. Neither should be charged to the new product when deciding whether to launch it. Incremental: the launch advertising, any new production line, and the sales the new product takes from Colgate's existing ones. That last item is the one most easily missed for a company that already holds a large share of its shelf.
        - A plant. Incremental: the construction cost and the working capital to run it. Not incremental: a share of corporate overhead. Colgate's Corporate line was −$1,717M in 2025 (`facts.segment-results-2025`), but that figure includes the $919M write-down and the litigation charge, and what remains is head-office cost that would be paid whether or not one more plant is built. Only overhead that rises because of the project counts.
        - An acquisition. Here the sunk-cost rule is the live one. The $2,211M written down since 2021 is gone. The question for the skin health business now is only whether its future cash flows are worth more inside Colgate than its sale price, not how to earn back what was paid. The write-down note says the unit has $51M of goodwill left (`facts.skin-health-writedown-2025`). Money spent on the current restructuring program ($13M booked in 2025, `facts.restructuring-program-2025`) is sunk in the same way.
      The typical project is small against the company, long-lived, and funded from yearly cash flow: capital spending of $564M against cash from operations of $4,198M (`facts.uses-of-cash-2025`). The exceptions are acquisitions, which are large, irregular and paid up front.

- **Lesson 15, Session 15 · Part 2 — "NPV, IRR, and Terminal Value via the Growing Perpetuity"** ([transcript](../../02-investment-returns-and-financing/lesson-15/session-15-part-2.md))
    - Quote: "If you take a project with an NPV of $3.3 billion, your value will increase by $3.3 billion."
    - Question for Colgate-Palmolive: What terminal growth rate is defensible for Colgate-Palmolive, and does any disclosed valuation of it (a fairness opinion, an analyst model, management's plan) use a growth rate above the risk-free rate or the economy's growth?
    - Sources needed: Risk-free rate, the chosen perpetual growth rate, analyst and management growth figures.
    - Where to find: ledger `market.terminal_growth`, `market.risk_free_rate`, `forecast.analyst_growth`, `forecast.years`, `facts.growth-and-margin-history`, `facts.sales-drivers-2025`. `forecast.management_growth` is not in the ledger: the 10-K gives no numeric long-term growth target.
    - Answer: 3%, the figure in the ledger (`market.terminal_growth`). The rule from the lecture is that no company can grow faster than the economy forever, and the risk-free rate, 4.82%, is the course's stand-in for the economy's long-run nominal growth. So 4.82% is the ceiling, and the professor's valuation spreadsheet uses it as its default. We chose a lower figure for two reasons. First, Colgate's own record: sales grew 3.3% a year from 2016 to 2025 (`facts.growth-and-margin-history`), and analysts expect 2.33% and 3.46% for 2027 and 2028 (the source note on `market.terminal_growth`). A company that has grown about 3% for a decade should not be assumed to speed up in perpetuity. Second, because Colgate is assumed to keep earning more than its cost of capital, each point of perpetual growth adds value, so the default would flatter the result. The alternative, 4.82%, is quoted beside the base case in the valuation lessons.
      Is any disclosed figure above the ceiling? One: analysts' long-term earnings-per-share growth of 5.45% (`forecast.analyst_growth`, the mean of two estimates). It is not a perpetual rate. It is a five-year view of earnings per share, which buybacks lift above the growth of the business. It should not be carried into a terminal value, and it is not. There is no fairness opinion, because there is no deal. Management gives no numeric long-run target in the 10-K.

## Cumulative Project — Questions for This Lesson

- **If you can identify a typical project for your firm, what pattern of cash flows do you foresee for the project?**
  For the typical project, a product line or a plant behind an existing brand: a modest outlay in the first year or two, a launch period when advertising is heavy and cash flow is low or negative, then many years of steady, slowly growing cash flow with small top-up spending. There is usually no natural end date, so a project analysis needs a terminal value, and for Colgate most of a project's worth will sit in it. That makes the growth rate after the forecast years (3% or less for a single product) and the assumption about how long the brand holds its price the two inputs that matter.
  For an acquisition the pattern is different and worse: the whole price is paid on day one, the benefits depend on growth that has to be forecast, and the 2025 write-down shows what happens when the forecast is wrong. The filing gives the cause as lower category growth and weaker performance than expected, particularly in China (`facts.skin-health-writedown-2025`).
  The discount rate should be the division's, not the company's: 8.67% for household and personal products, 7.24% for pet food (lesson 13), and higher for a project in Latin America or Africa (lesson 16).

## Notes

This lesson sets no new number. It fixes two rules for later: perpetual growth is capped by the risk-free rate, 4.82%, and we use 3%; and the money already lost on acquisitions is sunk and stays out of any forward-looking decision, while staying in invested capital when we measure how management has done (lesson 14). Those are different questions and they get different treatments.

Confidence: the description of typical projects is our reading of the filings, not something Colgate discloses project by project. No project-level cash flows are in the sources, so no net present value was computed.
