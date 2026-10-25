---
title: "SolarWinds (SWI) — Lesson 19: The Cost of Capital: Follow Up"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 19: The Cost of Capital: Follow Up

### Lesson 19 — The Cost of Capital: Follow Up

Figures are quoted from model-output.md §3, §4 and §6.

- **Lesson 19, Session 19 · Part 1 — "From Lower Cost of Capital to Real Value: Financing Savings and the Buyback Premium"** ([transcript](../../02-investment-returns-and-financing/lesson-19/session-19-part-1.md))
    - Quote: "That 19.6 billion is not value creation in the traditional sense, it's a value transfer."
    - Question for SolarWinds: What are the annual financing savings from moving SolarWinds to its optimal debt ratio, what are they worth capitalized as a growing perpetuity, and who captures that value (the price at which shares are bought back, or a distribution to the owner)?
    - Sources needed: Cost of capital at the current and optimal ratios, firm value, terminal growth, shares.
    - Where to find: model-output.md §3 and §6; `company.debt_total`, `company.equity_value`, `company.shares_basic`, `market.terminal_growth`.
    - Answer: Annual savings are $10.9M (§3): the cost of capital falls from 10.31% to 10.03% on a firm value of $3,889.9M. Capitalized at growth of 2.5% (`market.terminal_growth`), the value of moving is $144.4M (§3). Per basic share (171.6M, `company.shares_basic`) that is $0.84 (arithmetic).
        - A second route gives a smaller number. The DCF at the optimal cost of capital of 10.03% gives an enterprise value of $3,533.4M and $13.52 a share, against $13.00 at the status quo (§6). That is an enterprise value gain of $89.1M and $0.52 a share (arithmetic). A third measure, the adjusted present value in §9, gives $220.3M, or $1.28 a share (arithmetic). These are three measures on different bases, not competing answers (§6 and §9): the DCF status quo prices today's debt at its observed 7.11%, so its gain is smaller; the §3 figure prices both ends at the schedule's synthetic rates (10.31% to 10.03%) and capitalizes the saving at the market firm value; the APV values tax benefits less expected bankruptcy cost. Use the DCF figure as the working number and the others as the range.
        - Who captures it? SolarWinds is over-levered, so the lecture's buyback story runs backwards. The company would reduce debt by $468.1M (§3), by retaining cash or issuing shares, not by buying shares back. Lenders are repaid at face, because the loan floats and its market value is its face value (`meta.omitted`, `company.debt_market`), so they gain nothing. The saving goes to shareholders, and the issue price decides who gets it: shares sold at a fair price leave the gain to all holders in proportion; shares sold below fair value hand it to the new buyers. The 2024 special dividend of $168.2M (`company.history`) went the other way, and Turn/River's financing, a $2.225 billion first-lien loan plus a $525.0M second-lien loan (facts.new-debt-2025), added debt. Neither move was a financing-savings play. The deal was priced at $18.50 a share (`company.deal_price`) against $15.18 unaffected (`company.share_price`).

- **Lesson 19, Session 19 · Part 2 — "Breakeven Buyback Pricing, Stress-Testing the Optimal, and Rating Constraints"** ([transcript](../../02-investment-returns-and-financing/lesson-19/session-19-part-2.md))
    - Quote: "Just because of excess debt capacity doesn't mean they can use it to do whatever they want."
    - Question for SolarWinds: How far could SolarWinds' operating income fall before the optimum shifts or a covenant or rating floor binds? Given those constraints, what debt ratio would you recommend, and how does it compare with the unconstrained optimum?
    - Sources needed: Stress test of EBIT; interest expense; covenants; EBIT history.
    - Where to find: model-output.md §4; `company.ebit`, `company.interest_expense`, `debt.covenants`, `company.history`.
    - Answer: The optimum shifts with the first dollar of lost EBIT. §4 shows it at 21% with EBIT unchanged, 19% down 10% ($187.6M), 16% down 20% ($166.7M) and 14% down 30% ($145.9M). The cost of capital at the optimum rises only from 10.03% to 10.17%.
        - Covenant: the only financial covenant is the 7.40 to 1 first-lien net leverage test, active only when more than 35% of the $130.0M revolver is drawn, that is $45.5M (`debt.covenants`, `debt.revolver_undrawn`). Net first-lien debt is $1,235.7M less $259.3M cash = $976.4M (`company.debt_face`, `company.cash`). Against standardized EBITDA of $282.8M that is 3.45 times; against the company's adjusted EBITDA of $384.7M, 2.54 times (arithmetic). The credit agreement defines its own EBITDA, which is not in the sources, so these are estimates. By these figures EBITDA would have to fall by half or more before 7.40 times is reached, and the test is off while the revolver is undrawn. The covenant does not bind.
        - Rating floor: no agency rating exists (`debt.rating_actual`). Today's rating on the actual interest is B- (coverage 1.85x, §2). The schedule's 33% row, which reprices all the debt at the schedule's synthetic rate, shows B at 2.19x, and the 21% row shows A-. If the board wanted to stay out of the B range, the schedule says to stay at or below about 20%.
        - Evidence for the size of the shock: SolarWinds' own EBIT fell to $150.4M in 2023 from $208.4M in 2024 (`company.history`), 27.8% lower (arithmetic). That falls between the 20% and 30% rows.
        - Recommendation: about 15% debt, a cushion below the 21% optimum, justified by the stress test (§4). See the project answer below.

## Cumulative Project — Questions for This Lesson

- **If you move to the optimal debt ratio (given the cost of capital) approach, what consequences do you see for the value of your firm and the value of equity in the firm?**
  Moving from 33.03% to 21% means $468.1M less debt (model-output.md §3). The cost of capital falls from 10.31% to 10.03%, an annual saving of $10.9M. The value of moving is $144.4M by the perpetuity method (§3); in the DCF the enterprise value rises from $3,444.3M to $3,533.4M and the value per share from $13.00 to $13.52 (§6). Since debt falls by $468.1M and firm value rises, equity value rises by the full gain: the $468.1M of debt retired is replaced by $468.1M of equity (about 18% of the $2,604.9M market equity value, arithmetic). Equity holders do not lose from the swap, because they are paying down a loan at 7.11%. The gain is $0.52 to $1.28 a share, on three measures with different bases (§6, §9; see the lesson answer above). It is small against the 0.86 ratio of DCF value to the unaffected price (§6), so capital structure is not what decides the valuation.

- **Bringing in reasonable constraints into the cost of capital approach, what would your recommended debt ratio be for this firm?**
  About 15%, as a cushion below the 21% optimum, not a rival optimum: the optimum is 21% (EBIT numerator, §3) and APV agrees (§9), while the §4 stress test shows it falls to 14% if operating income falls 30%. This is a judgment call.
    - The stress test supports it: SolarWinds' EBIT was 27.8% lower in 2023 than in 2024, which sits between the 16% (EBIT down 20%) and 14% (down 30%) rows of §4.
    - The cost of being cautious is small. The cost of capital is 10.22% at 10% debt, 10.05% at 20% and 10.03% at 21% (§3 schedule). So a 15% ratio would cost about 0.1 percentage points more than the optimum, interpolating between the 10% and 20% rows.
    - The risk of going the other way is large: past 40%, the rating falls to B- and the cost of debt rises to 8.85%, and at 50% the rating is C at 19.93% (§3).
    - Fifteen percent of the $3,889.9M firm value is debt of $583.5M, so $701.5M would have to be repaid (arithmetic). Cash is $259.3M (`company.cash`), so the rest would need new equity or several years of retained cash flow. The credit agreement's negative covenants on dividends and buybacks (`debt.covenants`) do not stop repayment.
    - The covenant and the rating constraint are not what bind. Earnings volatility and the experience of 2023 are.

## Notes

Moving to the optimum is worth between $0.52 and $1.28 a share depending on the measure (§6, §9). The recommendation, about 15%, is a cushion that leaves the unconstrained 21% as the ceiling. Lesson 20 asks whether the 2023 shock should be larger once a lower rating hurts customer relationships. The terminal-value choice in lesson 32, not the debt ratio, drives the valuation.
