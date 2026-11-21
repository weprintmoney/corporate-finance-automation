---
title: "Colgate-Palmolive (CL) — Lesson 19: The Cost of Capital: Follow Up"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 19: The Cost of Capital: Follow Up

### Lesson 19 — The Cost of Capital: Follow Up

- **Lesson 19, Session 19 · Part 1 — "From Lower Cost of Capital to Real Value: Financing Savings and the Buyback Premium"** ([transcript](../../02-investment-returns-and-financing/lesson-19/session-19-part-1.md))
    - Quote: "That 19.6 billion is not value creation in the traditional sense, it's a value transfer."
    - Question for Colgate-Palmolive: What are the annual financing savings from moving Colgate-Palmolive to its optimal debt ratio, what are they worth capitalized as a growing perpetuity, and who captures that value (the price at which shares are bought back, or a distribution to the owner)?
    - Sources needed: Firm value, cost of capital now and at the optimum, perpetual growth rate, shares outstanding.
    - Where to find: model-output.md §3 and §6; ledger `facts.capstru-detail`, `facts.cost-of-capital-grid`, `company.shares_basic`, `market.terminal_growth`.
    - Answer: The formula is: yearly saving = (cost of capital now − cost of capital at the optimum) × firm value. Value of the saving = yearly saving ÷ (cost of capital at the optimum − growth). In the model, (8.32% − 8.14%) × $86,550.6M is $157.5M a year, worth $3,064.4M at 3% growth, or $3.86 a share (model-output.md §3 and §6). The workbook gives more: enterprise value up $5,806M, from $85,154M to $90,960M, and value per share up $7.30, from $98.71 to $106.01 (`facts.capstru-detail`).

        | Measure | Gain $M | Per share | What it assumes |
        |---|---|---|---|
        | Model, savings capitalized | 3,064.4 | $3.86 | All debt repriced at the BBB rate; savings grow 3% a year |
        | Workbook (`capstru.xlsx`) | 5,806 | $7.30 | Old debt keeps its old interest (A− rating, 8.09%); savings grow at the 4.27% the workbook backs out of today's price |
        | Model, adjusted present value (lesson 21) | 3,596.7 | $4.52 | Tax savings less expected bankruptcy cost |

      The three agree on direction and order of size: 4% to 7% of today's value. The workbook is highest for two reasons, both identified: a larger fall in the cost of capital (0.25 points against the model's 0.19, lesson 18) and a higher growth rate on the savings (4.27% against 3%). Our view is that the model's $3.86 is the better central figure and $7.30 the upper end, because the workbook's advantage from old cheap coupons fades as the notes mature.
      Who captures it. No value is created in the operating sense; the business sells the same toothpaste. The gain is the government taking less in tax, net of a higher risk of distress. It goes to shareholders, and how it is split depends on the buyback price. If Colgate borrowed $17,881M and bought shares at today's $98.71, the holders who stay would keep all of the gain. If the market priced the gain in first, sellers and stayers would share it. With no controlling owner, the cash can go out either as buybacks or as dividends. Which is better depends on the share price against its value: a buyback above value pays the sellers at the expense of the holders who stay. The valuation in lessons 29 to 34 puts value below the price, so lesson 22 uses dividends. Lenders are on the other side: existing notes would be worth less at a lower rating, which is a transfer from them to shareholders. The fair value of debt is already 5.9% below carrying value because of rates (`facts.debt-cross-checks`), and a downgrade would widen that.

- **Lesson 19, Session 19 · Part 2 — "Breakeven Buyback Pricing, Stress-Testing the Optimal, and Rating Constraints"** ([transcript](../../02-investment-returns-and-financing/lesson-19/session-19-part-2.md))
    - Quote: "Just because of excess debt capacity doesn't mean they can use it to do whatever they want."
    - Question for Colgate-Palmolive: How far could Colgate-Palmolive's operating income fall before the optimum shifts or a covenant or rating floor binds? Given those constraints, what debt ratio would you recommend, and how does it compare with the unconstrained optimum?
    - Sources needed: The stress test; the grid; covenants; operating income history.
    - Where to find: model-output.md §4; ledger `facts.cost-of-capital-grid`, `facts.operating-income-stability`, `debt.covenants`, `debt.rating_actual`, `facts.debt-to-ebitda-at-targets`.
    - Answer: Not far. The optimum shifts with the first 10% (model-output.md §4):

        | Operating income | Optimal debt ratio | Cost of capital there |
        |---|---|---|
        | $4,225.0M | 30% | 8.14% |
        | Down 10% | 27% | 8.17% |
        | Down 20% | 21% | 8.21% |
        | Down 30% | 21% | 8.24% |

      And a company that had already borrowed to 30% would be badly placed if income then fell (`facts.cost-of-capital-grid`): with operating income 10% lower, coverage would be 2.13 times and the synthetic rating BB; 20% lower, 1.58 times and B. Is a fall of that size plausible? Since 2016 the largest one-year fall in operating income before write-downs was 7.4%, in 2022, and a 15.9% fall would take it back to its ten-year low. In 2015 it fell 21.6% in a single year (`facts.operating-income-stability`; the cause is not in our files). So a 10% fall is ordinary and a 20% fall has happened.
      Covenants: the 10-K says only that bank agreements contain financial covenants and that Colgate complies (`debt.covenants`); the ratios are not disclosed, so no covenant floor can be tested. The rating is the constraint we can test.

## Cumulative Project — Questions for This Lesson

- **If you move to the optimal debt ratio (given the cost of capital) approach, what consequences do you see for the value of your firm and the value of equity in the firm?**
  Firm value rises by between $3,064.4M (model) and $5,806M (workbook), or 4% to 7%. Per share, $3.86 to $7.30 on a price of $98.71; the workbook's figure is $106.01. Debt rises from $8,084M to $25,965M and the $17,881M raised buys back shares, so the equity is smaller in total but each remaining share is worth more. The cost of equity rises from 8.76% to 9.65% and the beta from 0.73 to 0.90, because the shares carry more risk. The rating falls from A+ to A− (workbook) or BBB (model). These figures hold the business itself constant; they are not a forecast of where the share price would go, and they are not the valuation, which is settled in lessons 29 to 35.

- **Bringing in reasonable constraints into the cost of capital approach, what would your recommended debt ratio be for this firm?**
  20%, against the unconstrained 30%. This is a judgment; here is what it rests on and what it gives up.

  | Debt ratio | Debt $M | Debt ÷ EBITDA | Synthetic rating | If operating income fell 10% | If it fell 20% | Share of the 30% gain captured |
  |---|---|---|---|---|---|---|
  | 9.34% (today) | 8,084 | 1.67x | AAA | | | |
  | 20% (recommended) | 17,310 | 3.57x | A− | | A− | 56.9% |
  | 25% | 21,638 | 4.46x | A− | BBB | BB+ | 91.8% |
  | 30% (unconstrained) | 25,965 | 5.35x | BBB | BB | B | 100% |

  Sources: `facts.cost-of-capital-grid`, `facts.debt-to-ebitda-at-targets`. Blank cells were not computed. Four reasons for stopping at 20%.
    - The constraint we chose is an investment-grade rating with room to spare: the synthetic rating should stay at A− or better even if operating income falls 20%. At 20% debt it does (coverage 3.29 times). At 25% a 20% fall gives BB+, below investment grade. Colgate depends on commercial paper (an average daily balance of $1,611M in 2025, `facts.financing-types-2025`), a market that closes to weaker credits.
    - The table is more generous than the agencies. At today's debt the table says AAA and S&P says A+. If that two-step gap persists, a synthetic A− at 20% is an actual BBB, and a synthetic BBB at 30% is not investment grade. This is inference from one data point, but it points the same way as everything else.
    - The cost of stopping short is small. The cost of capital at 20% is 8.22% against 8.14% at 30%; the capitalized gain is $1,798.5M ($2.26 a share) against $3,159.1M on the same grid. Going from 20% to 30% buys the rest of the gain by standing one point from the cliff.
    - The percentages flatter Colgate's capacity. Debt ratios here are on market value, and Colgate's market value is high for its earnings: operating income is only 4.88% of firm value (`facts.debt-trade-off-sizes`). Thirty percent of market value is 5.35 times EBITDA. Twenty percent is already 3.57 times, against 1.67 today.
  The alternative we considered is 25% to 26%, which captures about nine-tenths of the gain and is still A− on today's income. It loses on the stress test. A reader who thinks a 20% fall in income is too severe a test for a toothpaste company would choose it, and would not be wrong.
  Reaching 20% means $9,226M of new debt, taking the total to $17,310M.

## Notes

Moving to the optimum is worth roughly $3 to $7 a share on a $98.71 price, with $3.86 our central figure for the full move and $2.26 for the recommended move to 20%. The gain is real but modest, 2% to 7% of value, and it is a one-time transfer from taxes to shareholders, not an improvement in the business.

The recommendation is 20%, not 30%. Confidence that Colgate should have more debt than 9.34%: high. Confidence that 20% is the right stopping point: moderate; it depends on how much weight is put on keeping a single-A rating through a bad year, which is a preference as much as a calculation. Lesson 20 checks the answer against the drivers of debt capacity, lesson 21 against a second method and the industry, and lesson 22 asks how to get there.
