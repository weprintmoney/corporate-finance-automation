---
title: "Colgate-Palmolive (CL) — Lesson 34: Value of Control"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 34: Value of Control

### Lesson 34 — Value of Control

- **Lesson 34, Session 34 · Part 1 — "Stories Into Numbers: Building the Full DCF Valuation"** ([transcript](../../04-dividends-and-valuation/lesson-34/session-34-part-1.md))
    - Quote: "A good valuation is a bridge between stories and numbers."
    - Question for Colgate-Palmolive: What is the status-quo story for Colgate-Palmolive (how it will grow, what margins it will earn, how much it must reinvest, how risky it is) and what intrinsic value per share does the full DCF produce from that story? How does it compare with the market price or the last transaction?
    - Sources needed: The valuation inputs and results; the cross-check; the market price.
    - Where to find: ledger `facts.ginzu-inputs`, `facts.ginzu-base-case-detail`, `facts.ginzu-replication-path`, `facts.ginzu-sensitivities`, `facts.price-implied-assumptions`; model-output.md §6; `professor-spreadsheet/results.md`.
    - Answer: $61.83 a share, against a price of $98.71. The price is 159.64% of the value (`facts.ginzu-base-case-detail`). The story, and the number each part becomes:

        | Part of the story | The number |
        |---|---|
        | A mature maker of branded staples whose sales grow a little slower than the economy, mostly through price | Revenue growth 2.25% next year, 3.1% a year to year 5, 3% forever |
        | Margins recover part of what they lost since 2017, but restructuring charges keep coming | Operating margin 20.5% rising to 21.3% |
        | It needs very little capital to grow | $2.20 of new sales per dollar invested; reinvestment of about 8.6% of after-tax income |
        | It is a safe business, and stays one | Cost of capital 8.34%, moving to 8.43% |
        | The brands keep earning what they earn today for ten years, and new investment after that still earns far more than it costs, but not what the old brands earn | Return on new capital 20% after year 10 |

      The arithmetic (`facts.ginzu-base-case-detail`): ten years of cash flow are worth $23,776M today and the terminal value $32,940M, so the operating business is worth $56,717M. Less debt of $8,282M and minority interests of $352M, plus cash of $1,612M and holdings of $82M, the equity is worth $49,777M. Less $439M of options, over 797.9 million shares, $61.83.
      The value under other stories, always quoted with it:

        | Case | Value per share | Price as % of value |
        |---|---|---|
        | Base case | $61.83 | 159.64% |
        | All the workbook's defaults: new investment earns only its cost, growth forever 4.82%, stable cost of capital 9.05% | $50.90 | 193.9% |
        | Return on new investment equal to the cost of capital, growth 4.82%, stable cost 8.43% | $53.82 | 183.40% |
        | Base case with growth forever at 4.82% | $79.74 | 123.78% |
        | Base case with a cost of capital of 8.67% (beta 0.80) | $60.56 | 163.00% |
        | Base case with a cost of capital of 7.84% (beta 0.63) | $63.82 | 154.66% |
        | Large-peer beta 0.41: cost of capital 6.77% for years 1 to 5, fading to 8.43% | $68.32 | 144.5% |
        | Large-peer beta 0.41: cost of capital 6.77% forever | about $91.88 | 107.4% |

      The price is above the value in every case, but in the last one by only about 7%. The base case is not the middle of a symmetric range: the cautious default is $10.93 below it and the generous growth case $17.91 above. What the price would need: holding the rest of the base case, an operating margin of 33.3%, or growth forever of 5.78%, or a cost of capital of 6.53% in every year (`facts.price-implied-assumptions`). We do not find the first two believable. The third is the uncomfortable one, because the low end of the beta range is close to it: Colgate's own regression gives 6.31% and its large peers give 6.77% (lesson 10; `facts.peer-betas-capital-iq`, `facts.ginzu-peer-beta-cases`). So the conclusion that the shares are overpriced rests on one belief: that over decades Colgate's cost of capital moves toward that of an average mature company. The professor's workbook builds that in by default, and we kept it. A reader who thinks branded staples will stay this insulated from the market forever should conclude the shares are close to fairly priced. Analysts disagree with us: their mean target price is $101.70, in a range of $88 to $112 (`facts.consensus-target-price`). A target price is a forecast of where the price will be, not an estimate of value, and lesson 35 shows the shares are priced in line with similar companies. Both things can be true.
      Cross-check. The repo model values Colgate at $60.85 on three years of analysts' forecasts as published (model-output.md §6). It is not the valuation. It lands within a dollar of the workbook because several differences offset:

        | Difference | Model cross-check | Workbook (the valuation) | Pushes the model's value |
        |---|---|---|---|
        | Margins | Consensus as published, 21.07% to 21.83% | Consensus less about 0.7 points | Up |
        | Debt subtracted | $8,084M, fair value at the end of 2025 | $8,282M, carrying value at 2026-09-30 | Up |
        | Stable cost of capital | 8.34% | 8.43% | Up |
        | Years at today's high returns before the terminal value | 3 | 10 | Down |
        | Tax rate | 25% throughout | 23.5% rising to 25% | Down |
        | Timing | Values at the end of 2025, cash flows a full year away | Values today on the last twelve months | Down |
        | Options and share count | $543.6M subtracted, 794.9 million shares | $439M subtracted, 797.9 million shares | About even |

      The agreement is a check that neither tool has a gross error. It does not make either number more certain: both rest on the same 20% return and 3% growth.

- **Lesson 34, Session 34 · Part 2 — "The Value of Control: Status Quo vs. Optimal, and the Four Levers to Restructure a Company"** ([transcript](../../04-dividends-and-valuation/lesson-34/session-34-part-2.md))
    - Quote: "The value of control in any company is the difference between two values: the status quo value and the optimal value."
    - Question for Colgate-Palmolive: What would change about Colgate-Palmolive if it were run optimally (operations, reinvestment, financing mix, growth period), what is it worth with those changes, how large is the value of control, and how likely is it that the change happens given who controls the company?
    - Sources needed: The optimal debt ratio and its value on each measure; the acquisition record; margin sensitivity; ownership and pay.
    - Where to find: ledger `facts.financing-lever-in-valuation`, `facts.capstru-detail`, `facts.cost-of-capital-grid`, `facts.buyback-above-value`, `facts.acquisitions-2018-2025`, `facts.ginzu-sensitivities`, `facts.holders-capital-iq`, `facts.executive-pay-2025`, `governance.controlling_holders`; model-output.md §3, §6 and §9.
    - Answer: Colgate is close to well run. The value of control is small: on our figures between $0.47 and $2.76 a share, set against a value of about $62.
        - Financing (computed). Colgate has 9.34% debt; the unconstrained optimum is 30% and our recommendation is 20% (lesson 19). What that is worth depends on the measure:

            | Measure | Move to 20% | Move to 30% | Basis |
            |---|---|---|---|
            | Workbook valuation, rate lowered for years 1 to 5 only | $0.47 (0.8%) | $0.79 (1.3%) | On $61.83. The stable rate stays 8.43% |
            | Workbook valuation, stable rate lowered too | $1.57 (2.5%) | $2.66 (4.3%) | On $61.83 |
            | Model DCF at the optimal cost of capital | | $2.76 (4.5%) | $63.62 against $60.85 (model-output.md §6) |
            | Model, yearly saving capitalized | $2.26 | $3.86 | On the market value of the firm (model-output.md §3) |
            | Model, adjusted present value | | $4.52 | Tax benefit less expected bankruptcy cost (model-output.md §9) |
            | `capstru.xlsx` | | $7.30 (7.40%) | $106.01 against the $98.71 price |

          The measures differ for reasons we can name. `capstru.xlsx` and the model's capitalized saving apply the saving to the firm's market value, which is about half as large again as our estimate of its worth, and `capstru.xlsx` also keeps old debt at its old interest (lesson 18). The valuation workbook is lowest because it fades every company to the same mature cost of capital. In percentage terms, each measure on its own base, the full move is worth 1% to 7%, and our recommended 20% about 1% to 3%. On the measures taken at the market price alone, the range from the move to 20% to the full move is 2% to 7% of the share price (lesson 19). We rely on the range from the valuation itself, $0.47 to $1.57 a share for 20% debt, and treat the $106.01 as a statement about the market price, not about value.
        - How the cash goes out (judgment). The usual way to hand borrowed money to shareholders is a buyback. With a share worth $61.83 and priced at $98.71, a buyback hands sellers more than the share is worth and the shareholders who stay pay the difference: $3,447M on the $9,226M of new debt, or $4.91 a share against a gain of $2.26 (`facts.buyback-above-value`). So the cash should go out as special dividends, with the regular dividend left on its existing slow rise, for as long as the price is above the estimated value. Buybacks become the better route only if the price falls to or below value. The same logic applies to the $1.2 billion or so a year Colgate already spends on buybacks from its own cash flow: while the price is above value, that money should go out as special dividends too.
        - Investing (judgment, not priced). Raise the bar for acquisitions. $2,211M written off against $3,894M spent (`facts.acquisitions-2018-2025`). The valuation assumes no further acquisitions and no further write-downs, so avoiding them protects the value; it does not add to it.
        - Operations (judgment, not priced). Margins are the largest lever in the numbers: a return to the 24.0% of 2017 would be worth $8.32 a share (`facts.ginzu-sensitivities`). But a restructuring program is already running and the base case already assumes margins recover part of the way. We give no further credit, because we cannot say what a new management would do that this one is not attempting.
        - Growth period (judgment). Nothing to change; the base case already gives the brands ten years at full strength.
      Who controls, and how likely. No one controls Colgate. The three largest holders are index-fund managers with 10.26%, 8.18% and 5.95% (`governance.controlling_holders`); directors and officers own 0.43%; the largest holder Capital IQ tags as an activist owns 0.05% (`facts.holders-capital-iq`). There is no poison pill and no staggered board, so a change is possible in principle, but the company is worth $78.5 billion in the market and no buyer or activist is in sight.

## Cumulative Project — Questions for This Lesson

- **What is the status quo value of your firm?**
  $61.83 a share; $56,717M for the operating business and $49,777M for the equity (`facts.ginzu-base-case-detail`). Beside it: $50.90 on all the workbook's defaults and $79.74 with growth forever at the riskfree rate. With the large-peer beta, $68.32 if the lower cost of capital fades to the mature rate and about $91.88 if it lasts forever (`facts.ginzu-peer-beta-cases`). The price is $98.71. The repo model's cross-check gives $60.85 (model-output.md §6).

- **If you were running this firm, what would you change about the way the firm is run (in terms of investing, financing and dividend decisions)?**
  Three things, in order of how sure we are.
    - Financing: borrow more. Move from 9.34% debt to 20% over about five years, which needs $9,226M of new debt (lesson 19). The alternative is the unconstrained 30%; it loses investment grade if operating income falls 10%.
    - Dividends: change the mix, not the amount. Pay out the borrowed money, and the cash now spent on buybacks, as special dividends while the price is above value, and leave the regular dividend on its existing slow rise. A buyback above value moves wealth from the shareholders who stay to those who sell; a dividend treats all alike. Special dividends suit both sums, because they create no expectation that they will be repeated, which was lesson 22's objection to raising the regular dividend. Buybacks become the better route only if the price falls to or below value. This is a judgment and it depends on the valuation being right: if a share is really worth $98.71 or more, buybacks do no harm, and if it is worth $79.74 the overpayment roughly equals the gain from the debt (`facts.buyback-above-value`).
    - Investing: stop buying businesses unless the price paid can be justified against the 8.34% cost of capital, given that more than half of what was spent since 2018 has been written off.
  We would not change the operating plan or the total amount returned to shareholders, which lessons 26 and 27 found about right.

- **What is the value of your firm with these changes made?**
  About $62 to $63 a share: $62.31 with the cost of capital lowered for five years, $63.41 if the lower rate lasts (`facts.financing-lever-in-valuation`). On the model's cross-check, $63.62 for the full move to 30% (model-output.md §6). The professor's `capstru.xlsx` puts the full move at $106.01, but that is $7.30 added to the market price, not to our value.
  The switch from buybacks to special dividends does not show up in this number, because it does not change what the firm is worth. It changes who gets it: it stops the transfer away from continuing shareholders that comes with buying shares above their value.

- **What is the likelihood that this change will happen?**
  Low, for both parts.
    - More debt. Nothing forces it. There is no controlling owner to demand it, the largest holders are index funds that do not campaign on capital structure, and no activist holds a meaningful stake. Management describes its approach as "prudent management of our capital structure" (`facts.capital-structure-statements`), and S&P lowered the rating in 2024 (`facts.sp-rating-action`), which makes a deliberate step down the rating scale less likely.
    - Special dividends in place of buybacks. Also unlikely. A $5 billion buyback program was authorized in March 2025 (`facts.payout-policy-2025`). And pay points the other way: 80% of the annual bonus rests on earnings per share and organic sales growth (`facts.executive-pay-2025`). A buyback raises earnings per share by shrinking the share count. A dividend does not.
  The lecture's formula is: expected value of control = probability of change × (value if changed − value as run). With a gain of $0.47 to $2.76 a share and a low probability, the expected value is cents per share. So none of the $36.88 gap between the price and our value can be explained as the market paying for a change of control.

## Notes

What this lesson establishes: the status quo value, $61.83; the value with our changes, about $62 to $63; and that the difference between the two is small beside the difference between either and the price.

The position on debt and buybacks, for the report. The case for more debt stands (lesson 19). The cash goes out as special dividends, not buybacks, while the price is above our estimate of value, and through buybacks only at or below it (lesson 22). The two fit together only through the valuation: the debt advice does not depend on $61.83, and the choice of route depends on nothing else.

Model note. Three measures of the financing gain appear in `model-output.md` ($2.76, $3.86 and $4.52 a share) and one in `capstru.xlsx` ($7.30). The table above adds the workbook valuation's own. For a per-share figure against our value, use $0.47 to $2.76; the larger figures are measured on the market value of the firm.

Confidence: moderate on the status quo value as a point estimate, for the reasons in lesson 32; moderate that the shares are worth less than the price, because that rests on the cost of capital moving toward the mature-company rate over time; high that the value of control is small; and the buyback position is only as good as the valuation.
