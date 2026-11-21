---
title: "Colgate-Palmolive (CL) — Lesson 14: Earnings and Cash Flows"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 14: Earnings and Cash Flows

### Lesson 14 — Earnings and Cash Flows

- **Lesson 14, Session 14 · Part 1 — "Show Me the Money: From Accounting Earnings to Cash Flows"** ([transcript](../../02-investment-returns-and-financing/lesson-14/session-14-part-1.md))
    - Quote: "It's not show me the accounting income, it's not show me the earnings, it's show me the money."
    - Question for Colgate-Palmolive: Starting from Colgate-Palmolive's operating income, what are the adjustments (depreciation, capital spending, working capital, expensed R&D) that get to free cash flow to the firm? How much of the gap between operating income and EBITDA is non-cash amortization versus real reinvestment?
    - Sources needed: Operating income, tax rate, depreciation and amortization, capital spending, working capital change, R&D, stock-based compensation.
    - Where to find: ledger `company.ebit`, `company.da`, `company.capex`, `company.change_wc`, `company.rd_expense`, `company.acquisition_amortization`, `company.sbc`, `facts.cash-flow-bridge-2025`, `facts.uses-of-cash-2025`; model-output.md §8; modules-2-4-cross-checks-output.md §2.
    - Answer: For 2025 (`facts.cash-flow-bridge-2025`; model-output.md §8):

        | Step | $M |
        |---|---|
        | Operating income, before the $919M write-down | 4,225 |
        | Less taxes at the 25% marginal rate | 1,056.2 |
        | After-tax operating income | 3,168.8 |
        | Plus depreciation and amortization | 630 |
        | Less capital spending | 564 |
        | Less change in working capital (negative: it released cash) | −344 |
        | Free cash flow to the firm | 3,578.8 |

      Colgate's cash flow is larger than its after-tax earnings, 112.9% of them. Two things drive that. Capital spending is slightly below depreciation and amortization (0.90 times), and working capital shrank by $344M, most of it from higher accounts payable and other working capital at year end. Neither can go on forever: a company cannot spend less than it wears out indefinitely, and payables can only be stretched so far. The model shows the same pattern in all three years, with reinvestment between −$328M and −$410M (model-output.md §8).
      The gap between operating income and EBITDA is $630M. Of that, $78M (12.4%) is amortization of intangibles from past acquisitions, a charge that needs no replacement spending. The other $552M is depreciation of plant and software that does have to be replaced; capital spending is 1.02 times that figure. So the depreciation is real, and EBITDA overstates what Colgate can spend.
      Other adjustments the lecture lists, each checked and left alone. Research and development is $366M, 1.8% of sales, too small for capitalizing it to change anything. Stock-based compensation of $155M (0.8% of sales) is treated as an expense, which it is. The largest long-lived spending that accountants expense is advertising, $2,703M or 13.3% of sales (`facts.uses-of-cash-2025`). It builds the brands, which are Colgate's main asset, and none of it is on the balance sheet. We do not capitalize it, because the course does not and there is no agreed life for it, but it is the reason invested capital looks small and returns look high (Part 2).

- **Lesson 14, Session 14 · Part 2 — "Return on Invested Capital vs. Cost of Capital, and the Country Risk Premium"** ([transcript](../../02-investment-returns-and-financing/lesson-14/session-14-part-2.md))
    - Quote: "It looks like Disney is generating a 4.8% excess return over and above its cost of capital."
    - Question for Colgate-Palmolive: What return on invested capital did Colgate-Palmolive earn in the base year, does it clear the cost of capital, and does the answer flip if acquisition goodwill is excluded from invested capital?
    - Sources needed: After-tax operating income, invested capital, goodwill, write-downs, cost of capital.
    - Where to find: model-output.md §8; ledger `company.invested_capital`, `company.goodwill`, `facts.writedowns-2021-2025`, `facts.roic-variants-2025`, `facts.acquisitions-2018-2025`.
    - Answer: 34.56%, against a cost of capital of 8.34%: an excess return of 26.22 points, or $2,403.8M a year of economic value added (model-output.md §8). It does not flip under any definition (`facts.roic-variants-2025`):

        | Definition | Invested capital $M | Return |
        |---|---|---|
        | Chosen: write-down out of income, $2,211M of write-downs since 2021 added back to capital | 9,169 | 34.56% |
        | Write-downs not added back | 6,958 | 45.54% |
        | Reported operating income ($3,306M), same capital | 9,169 | 27.04% |
        | Goodwill taken out | 6,047 | 52.40% |

      The chosen definition, with its reason and the alternative. Operating income leaves out the $919M write-down because it is a non-cash charge about a past purchase, not a cost of running the business in 2025. But a write-down is also an admission that capital was spent and lost. Colgate wrote down $571M in 2021, $721M in 2022 and $919M in 2025. If those amounts simply vanish from invested capital, each failed acquisition makes the return look better. So the $2,211M is added back to invested capital: money spent on deals that failed still counts as money invested. The alternative, not adding it back, gives 45.54%; the professor's valuation workbook, which does not make the adjustment, shows about 42%.
      Taking goodwill out raises the return to 52.40%, and the lecture's point about goodwill cuts the other way here: for a company that grows by acquisition, goodwill is capital and belongs in. It stays in. Goodwill is 34.05% of invested capital (model-output.md §8).
      How far is the conclusion from flipping? Invested capital would have to be $37,995M, 4.1 times the ledger figure, for the return to fall to 8.34%. No reasonable adjustment for expensed advertising gets there.

## Cumulative Project — Questions for This Lesson

- **What return on capital did your firm generate last year?**
  34.56% in 2025: after-tax operating income of $3,168.8M on invested capital of $9,169.0M (model-output.md §8). Return on equity is not usable. Net income of $2,132M on book equity of $54M is 3,948% (model-output.md §8), a number that measures how little book equity is left after years of buybacks, not how good the projects are.

- **If you have returns on capital over time for your firm, is there a trend in those returns?**
  No clear trend in three years: 30.95% in 2023, 37.53% in 2024, 34.56% in 2025 (model-output.md §8). Capital IQ's own measure, on a different definition, rises from 26.3% in 2021 to 29.5% in 2025 with a dip to 23.6% in 2022 (`facts.ciq-return-on-capital`). Both say the same thing: returns are high and steady, in the high twenties to mid thirties. The longer record points to flat profits, not rising ones: operating income before write-downs grew 0.7% a year from 2016 to 2025 while sales grew 3.3% (`facts.growth-and-margin-history`).

- **How do the returns on capital (equity) compare to the costs of capital (equity)?**
  Return on capital 34.56% against a cost of capital of 8.34%, a spread of 26.22 points (model-output.md §8). The comparison on equity (3,948% against 8.76%) is meaningless for the reason above. For context, the US household products industry averages a 34.42% after-tax return on capital (`facts.industry-averages-2026`), so Colgate is typical of its industry, not exceptional within it. The excess return belongs to branded staples as a category.

- **Is there a typical project for this firm? If yes, what does it look like in terms of life (long term or short term), investment needs and cash flow patterns?**
  There are three kinds, with very different records.
    - Brand support: advertising of $2,703M a year, expensed as spent. No end date, no up-front outlay, cash flows that continue as long as the spending does. This is where the 34.56% comes from.
    - Plant and capacity: capital spending of $564M, 2.8% of sales, on assets depreciated over 3 to 15 years for equipment and up to 40 for buildings (`facts.depreciation-lives`). Medium to long life, modest outlay, steady cash flows.
    - Acquisitions: $3,894M from 2018 to 2025, in lumps. Long-lived on paper, but $2,211M was written down over the same years, 57% of what was spent (`facts.acquisitions-2018-2025`). The filings in our folder tie only the 2025 write-down to a named deal (skin health, primarily Filorga), so the 57% compares totals and does not prove that those particular purchases failed.

- **Are the projects in the future likely to look like the projects in the past? Why or why not?**
  The first two kinds, yes: Colgate expects capital spending of about 3.0% of sales in 2026 (`facts.uses-of-cash-2025`), and the brands are the same brands. The risk is the third kind. Organic growth is slow (sales up 1.4% in 2025, volume down 0.4%, `facts.sales-drivers-2025`), which is the usual reason a mature company reaches for acquisitions, and Colgate bought again in 2025 (Prime100, $293M). If future growth has to come from purchases in categories outside toothpaste and pet food, the marginal return will be far below 34.56%. The average return describes the existing brands; it is not what a new dollar earns.

## Notes

Colgate earns far more than its cost of capital on what it has: 34.56% against 8.34%, on the conservative definition. That finding is high-confidence in direction, because no definition brings it near 8.34%. The level is less certain: 27% to 52% depending on how write-downs and goodwill are treated.

The more important distinction for later lessons is between average and marginal returns. Existing brands earn about 35%. The $3,894M spent on acquisitions since 2018 did much worse. Lesson 22 uses this when it asks whether Colgate has good projects for borrowed money, and lesson 27 when it asks whether management should be trusted with cash. The valuation (lessons 29 to 35) has to decide how long the excess return lasts; the stable return on capital of 20% in the ledger is that judgment.
