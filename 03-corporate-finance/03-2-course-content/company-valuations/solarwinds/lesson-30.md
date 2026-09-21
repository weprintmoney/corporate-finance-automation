---
title: "SolarWinds (SWI) — Lesson 30: DCF Cash Flows & Discount Rates"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Lesson 30: DCF Cash Flows & Discount Rates

### Lesson 30 — DCF Cash Flows & Discount Rates

- **Lesson 30, Session 30 · Part 1 — "Three Cash Flow Definitions and Matching Discount Rates: Deutsche Bank, Tata Motors, and Disney"** ([transcript](../../04-dividends-and-valuation/lesson-30/session-30-part-1.md))
    - Quote: "So free cash flow to equity is after debt payments, free cash flow to the firm is before debt payments."
    - Question for SWI: Building SWI's FY2024 free cash flow to the firm (after-tax operating income minus net CapEx minus change in working capital) — what number results, what reinvestment rate does it imply relative to SWI's ~48% adjusted EBITDA margin, and how does that base-year cash flow pair with the cost of capital REPO-SWI-VAL already computed at Step 12 for a firm-value DCF?
    - Sources needed: SWI FY2024 operating income, effective tax rate, CapEx, depreciation, and change in working capital.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 8 (income statement + cash flow statement); REPO-SWI-VAL (WACC/cost of capital already computed at Step 12 — reusable as the discount rate; base-year FCFF itself is not yet built there).
    - Answer: FY2024 FCFF is **$153.8M**, on a 1.6% reinvestment rate. EBIT of $208.419M × (1 − 0.25 marginal) = $156.314M; the reported effective rate is unusable (a −$8.102M tax *benefit* on $103.801M of pre-tax income, i.e. −7.8%), though cash taxes paid were $61.5M. Total capitalized spend was $20.478M ($5.611M PP&E + $14.401M capitalized software development + $0.466M intangibles) against $74.352M of reported D&A, which naively gives net capex of −$53.874M — but $52.915M of that D&A is amortization of 2016-LBO purchase intangibles ($45.846M acquired intangibles + $7.069M acquired technologies) that never has to be replaced, so real D&A is $21.437M and real net capex is −$0.959M. Non-cash working capital moved from −$308.336M to −$304.815M, a $3.521M investment, giving FCFF = $156.314M + $0.959M − $3.521M = $153.8M and a reinvestment rate of $2.562M ÷ $156.314M = 1.6% — the 48.3% adjusted EBITDA margin is real but almost nothing is being plowed back. Discounted as a no-growth perpetuity at the Step 12 WACC of 10.33%, that base year is worth $153.8M ÷ 0.1033 = $1.49B, only 34% of the $4.37B enterprise value Turn/River paid — so the deal price is overwhelmingly a bet on management's forecast growth, not on the base year. (All figures from `swi-10k-fy2024.md`; WACC from `valuation-report.md`.)

## Notes

Lesson 30 puts the three cash-flow definitions (FCFF, FCFE, dividends) and their matching discount rates into practice by building SWI's actual base-year FCFF. The key move is separating real D&A from acquisition-amortization noise — of the $74.4M reported, $52.9M is 2016-LBO purchase-accounting amortization that will never recur as cash spend, so real net capex is nearly zero and FCFF lands at $153.8M on a 1.6% reinvestment rate. Capitalized as a no-growth perpetuity at the 10.33% WACC, that base year is worth only 34% of what Turn/River actually paid — the single clearest number in this project showing the deal price is a bet on management's forecast growth, not on where SWI's cash flows already sit. This base-year build feeds directly into Lesson 34's full DCF, and the same D&A-versus-real-depreciation distinction was first raised (in less precise form) back in Lesson 14's ROIC/FCFF discussion.
