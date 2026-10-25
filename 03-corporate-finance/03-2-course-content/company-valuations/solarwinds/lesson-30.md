---
title: "SolarWinds (SWI) — Lesson 30: Cash Flows and Discount Rates in Valuation"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 30: Cash Flows and Discount Rates in Valuation

### Lesson 30 — Cash Flows and Discount Rates in Valuation

- **Lesson 30, Session 30 · Part 1 — "Three Cash Flow Definitions and Matching Discount Rates"** ([transcript](../../04-dividends-and-valuation/lesson-30/session-30-part-1.md))
    - Quote: "So free cash flow to equity is after debt payments, free cash flow to the firm is before debt payments."
    - Question for SolarWinds: What is SolarWinds' base-year free cash flow to the firm (after-tax operating income minus net capital spending minus the change in working capital), what reinvestment rate does it imply, and which discount rate pairs with it?
    - Sources needed: EBIT, tax rate, capital spending, depreciation and amortization, change in working capital.
    - Where to find: `company.ebit`, `company.capex`, `company.da`, `company.change_wc`, `market.tax_rate_marginal`; model-output.md §1, §5, §8; `sources/filings/swi-10k-fy2024.md` income statement and cash flow statement.
    - Answer: $171.4M, with a negative reinvestment rate on the reported figures, paired with the cost of capital of 10.23%.
        - After-tax operating income: $208.4M × (1 − 25%) = $156.3M (§8). The reported tax rate cannot be used. The company booked a tax benefit of $8.1M on pre-tax income of $103.8M (facts.tax-benefit-2024), so the marginal 25% is used.
        - Net capital spending: capital spending $20.5M less depreciation and amortization $74.4M is $-53.9M (§5 net capex for 2024).
        - Change in working capital: $38.8M of investment, mostly a $23.8M fall in income taxes payable (`company.change_wc` note).
        - Free cash flow to the firm = after-tax operating income 156.3 − reinvestment (−15.1) = $171.4M (model-output.md §8, "By year").
        - Reinvestment is −53.9 + 38.8 = $-15.1M, a rate of −9.66% of after-tax operating income (model-output.md §8). That is judgment territory: $52.9M of the $74.4M of amortization is acquired technology and intangibles from the 2016 buyout (`company.acquisition_amortization`), which will never be replaced by spending. Leave it out and net capex is $-1.0M, reinvestment is $37.8M and the rate is 24.18% (model-output.md §8, note under "By year"). The reported basis is used here because it is what the ledger and model carry.
        - Stock-based compensation of $76.5M is treated as an expense (`modeling_choices.sbc_treatment`), so it is not added back. Adding it back would give $247.9M (171.4 + 76.5), which is the sort of number a company-adjusted figure shows.
        - Discount rate: a cash flow before debt payments pairs with the cost of capital, 10.23% (§1), not the cost of equity.

## Cumulative Project — Questions for This Lesson

- **What is the current cost of equity and capital for your firm? How might these numbers change in the future?**
  Cost of equity 12.65% and cost of capital 10.23% (model-output.md §1): risk-free 4.43% plus levered beta 1.6714 times a 4.92% premium; 33.03% debt at an after-tax 5.33%. They can change four ways. (1) Rates: the 4.43% Treasury and the 4.92% premium are 2025-02-05 values, and the premium rests on a judgment about international revenue (`country.exposures`). (2) Leverage: at the optimal 21% debt the cost of capital would be 10.03% and cost of equity 11.63% (§3); the model's schedule shows cost of capital rising steeply past 40% debt, 10.72% at 40% and 16.44% at 50% (§3), because interest coverage fails. The buyer's $2,750.0M of term debt (facts.new-debt-2025) moves the company into that range, though that schedule is a synthetic rating on current EBIT, not the sponsors' actual loan pricing. (3) Cost of debt: observed 7.11% against 8.85% implied by the synthetic B- rating (§2). (4) Beta: 1.22 is the January 2025 software industry average (`beta.unlevered_bottom_up`). The DCF holds 10.23% for every year (§6).

- **Estimate the free cash flows to the firm & equity in the most recent five years for your firm?**
  Three comparable years (2020 and 2021 include N-able). FCFE from §5: $-606.2M, $59.4M, $127.0M for 2022–2024. FCFF from the §8 "By year" table, with the 2022 impairments added back to operating income ($86.8M): $146.3M, $190.6M, $171.4M. Management's own 2025 figure, after stock compensation, is $212.0M (`forecast.years`).

## Notes

The base-year FCFF of $171.4M is the starting point the plan's $212.0M for 2025 grows from. The negative reinvestment rate carries into lesson 31, where it is the reason fundamental growth comes out near zero. The model prints FCFE history (§5) but not FCFF history; the FCFF rows here are arithmetic on `company.history` and are listed as facts to add.
