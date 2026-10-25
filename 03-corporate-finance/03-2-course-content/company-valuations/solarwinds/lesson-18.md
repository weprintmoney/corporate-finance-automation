---
title: "SolarWinds (SWI) — Lesson 18: The Cost of Capital: Approach"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 18: The Cost of Capital: Approach

### Lesson 18 — The Cost of Capital: Approach

All figures below are quoted from model-output.md §1 to §3. The model uses Damodaran's small-firm ratings table (January 2025), because SolarWinds' market value of $2.6 billion is under his $5 billion line (`modeling_choices.firm_size_table`).

- **Lesson 18, Session 18 · Part 1 — "The Cost of Capital Approach to the Optimal Debt Ratio"** ([transcript](../../02-investment-returns-and-financing/lesson-18/session-18-part-1.md))
    - Quote: "The optimal debt ratio for this company, if I stay true to the notion of minimizing cost of capital, is 40% debt."
    - Question for SolarWinds: Where does SolarWinds' cost of capital bottom out as the debt ratio is varied from 0% to 70%, and does its current ratio sit below, at, or above that point? How steep is the curve on each side of the minimum?
    - Sources needed: EBIT, interest, unlevered beta, risk-free rate, equity risk premium, tax rate, ratings table.
    - Where to find: model-output.md §3 (schedule under EBIT); `company.ebit`, `beta.unlevered_bottom_up`, `market.risk_free_rate`, `country.weighted_erp`, `market.tax_rate_marginal`, `modeling_choices.firm_size_table`.
    - Answer: The cost of capital bottoms out at 21% debt, at 10.03% (§3), with an A- synthetic rating. SolarWinds' current ratio, 33%, is above that point. At 33% the same method gives 10.31% (§3).
        - The left side is shallow. At 0% debt the cost is 10.43%, at 10% it is 10.22% and at 20% it is 10.05% (§3 schedule). Each added slice of debt cuts the cost a little, because the tax shield on cheap A- debt (pre-tax 5.03% to 5.38%) outweighs the higher cost of equity (10.43% at 0% rising to 11.63% at 21%).
        - The right side is steeper and then falls off a cliff. At 30% the rating drops to B+ and the pre-tax cost of debt jumps to 7.04%; WACC is 10.24%. At 33% it is 10.31%, at 40% 10.72% (rating B-, debt at 8.85%), and at 50% 16.44% (rating C, debt at 19.93%, coverage 0.54x). The curve is a gentle bowl to the left of the minimum and a wall to the right of 40%.
        - Reading: the current position costs only about 0.28 percentage points more than the optimum (10.31% − 10.03%, arithmetic). The loss from being over-levered is small today but the slope steepens quickly.

- **Lesson 18, Session 18 · Part 2 — "The Iterative Rating Loop and the Kink in the Cost of Capital Curve"** ([transcript](../../02-investment-returns-and-financing/lesson-18/session-18-part-2.md))
    - Quote: "My advice to companies is if you're going to make a mistake, be under-levered rather than over-levered."
    - Question for SolarWinds: Which coverage numerator (operating income, operating income plus acquisition amortization, or EBITDA) does SolarWinds' optimum depend on, and how far does the optimum move between them? Which one is defensible for this company, and where is the kink in the curve?
    - Sources needed: EBIT, EBITDA, acquisition amortization, stock compensation; model-output.md §2 and §3.
    - Where to find: `modeling_choices.coverage_numerator`, `company.ebit`, `company.ebitda_standardized`, `company.acquisition_amortization`, `company.sbc`.
    - Answer: The optimum is 21% on EBIT, 26% on EBIT plus acquisition amortization and 28% on EBITDA (§3). Using EBIT ($208.4M, coverage 1.85x, B-) the optimum is the lowest and the most cautious. The model's choice is EBIT (`modeling_choices.coverage_numerator`).
        - Why EBIT is defensible: stock compensation of $76.5M is a real cost and is expensed (`modeling_choices.sbc_treatment`, `company.sbc`), and the non-acquisition depreciation, $74.4M less $52.9M = $21.5M (arithmetic), roughly equals capex of $20.5M (`company.capex`). So EBITDA ($282.8M, `company.ebitda_standardized`) credits SolarWinds with cash that equipment and software replacement consume. The case for adding back acquisition amortization ($52.9M, `company.acquisition_amortization`) is stronger, since it is a non-cash charge on the 2016 buyout and nothing replaces it. That gives 26%. The company's own adjusted EBITDA of $384.7M is shown at 3.42x and a BB rating but is not used, because it adds back stock compensation (§2).
        - The optimum moves 7 percentage points across the three numerators (21% to 28%) but the cost of capital at the optimum barely moves, 10.03% to 9.90% (§3). The savings from moving change a lot: $10.9M a year on EBIT, $3.3M on EBIT plus amortization and $2.1M on EBITDA (§3).
        - The kink: the rating is a step function of coverage. In the EBIT schedule the A- rating and 5.38% cost of debt hold from 20% to 21%; at 30% it is B+ at 7.04%. The cost of capital rises as soon as the rating steps down. The second kink is the distress cliff between 40% (B-, 8.85%) and 50% (C, 19.93%). Given "better under-levered than over-levered", the low end of the 21% to 28% range is the better guide.

## Cumulative Project — Questions for This Lesson

- **What is your firm's current debt ratio (and cost of capital)?**
  Debt of $1,285.0M (`company.debt_total`) against equity of $2,604.9M (`company.equity_value`), so the debt ratio is 33.03% of the firm's $3,889.9M value (model-output.md §1). Debt to equity is 0.4933. The levered beta is 1.6714, the cost of equity 12.65%, the after-tax cost of debt 5.33% (7.11% pre-tax, 25% tax), and the cost of capital is **10.23%** (§1). At book weights the debt ratio is 47.28% and the cost of capital 9.19% (§1), for comparison only. The §3 table shows 10.31% at the current ratio because it prices debt from the synthetic B rating (7.43%) and not from the observed rate of 7.11%.

- **Based upon the cost of capital approach, what is the optimal debt ratio for your firm?**
  21%, with a cost of capital of 10.03% and an A- rating (model-output.md §3, EBIT numerator). That is $468.1M less debt than the company carries (§3). The alternatives are 26% (EBIT plus acquisition amortization) and 28% (EBITDA). Lesson 19 puts constraints on it.

## Notes

The optimum is 21% against 33.03% today. The cost of capital curve is flat near the bottom, so the gain from moving is modest (lesson 19). The result depends on the coverage numerator but only by 7 points, and all three put SolarWinds above its optimum. Lessons 19 and 20 test it against a fall in operating income. A gap between the §1 rate (10.23%) and the §3 current-ratio rate (10.31%) is a method difference (observed versus synthetic cost of debt), not an error.
