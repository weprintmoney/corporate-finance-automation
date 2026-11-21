---
title: "Colgate-Palmolive (CL) — Lesson 31: Growth"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 31: Growth

### Lesson 31 — Growth

- **Lesson 31, Session 31 · Part 1 — "Growth Has to Be Earned: Reinvestment, Return, and the Fundamental Growth Rate"** ([transcript](../../04-dividends-and-valuation/lesson-31/session-31-part-1.md))
    - Quote: "The growth of a company is not something that you and I can come up with or endow the company with."
    - Question for Colgate-Palmolive: What growth rate do Colgate-Palmolive's actual reinvestment rate and return on invested capital justify, and how does it compare with management's plan and analysts' numbers? If the company is growing faster than the fundamentals allow, where is the growth coming from?
    - Sources needed: Reinvestment by year; return on capital; consensus and guidance; what drove sales growth.
    - Where to find: ledger `facts.fundamental-growth`, `facts.fcff-fcfe-2021-2025`, `facts.growth-history-and-consensus`, `facts.sales-drivers-2025`, `facts.growth-and-margin-history`; model-output.md §8.
    - Answer: The formula is: expected growth in operating income = reinvestment rate × return on invested capital. For Colgate it gives growth of about zero (`facts.fundamental-growth`):

        | Basis | Reinvestment rate | Return on capital | Growth the formula gives |
        |---|---|---|---|
        | 2025 | −12.94% | 34.56% | −4.47% |
        | 2021–2025, acquisitions left out | −1.09% | 34.56% | −0.38% |
        | 2021–2025, acquisitions counted | 6.26% | 34.56% | 2.16% |

      Against that, sales grew 3.3% a year from 2016 to 2025, analysts expect revenue to grow 3.07% to 3.57% a year, and management guides to 4.0% to 5.0% for 2026 (`facts.growth-history-and-consensus`). So Colgate grows faster than its own reinvestment explains. Where the growth comes from:
        - Price, not volume. In 2025 selling prices rose 2.1% and volume fell 0.4% (`facts.sales-drivers-2025`). A price rise needs no new factory. That is why sales can grow with no net reinvestment.
        - Acquisitions. They are the only reinvestment of any size, and counting them the formula gives 2.16%.
        - It has not reached profit. Sales grew 3.3% a year from 2016 while operating income before write-downs grew 0.7% a year, and the margin fell from 24.0% in 2017 to 20.7% in 2025 (`facts.growth-and-margin-history`). Growth bought with price in a category where volume is flat has cost margin.
      The formula's lesson for the valuation is a limit, not a forecast. Price-led growth of about 3% a year with no reinvestment is not something to project forever. To grow 3% a year for good, Colgate would need to reinvest 8.68% of after-tax operating income if new investments earned today's 34.56%, and 15.00% if they earned 20% (`facts.fundamental-growth`). The valuation charges for that reinvestment: about 8.6% of after-tax income in years 1 to 10 and 15% after (`facts.ginzu-replication-path`).

- **Lesson 31, Session 31 · Part 2 — "From ROE Decomposition to a Revenue-Based Growth Model"** ([transcript](../../04-dividends-and-valuation/lesson-31/session-31-part-2.md))
    - Quote: "This approach to estimating growth based on fundamentals works if you have a stable return on equity and a stable return on capital."
    - Question for Colgate-Palmolive: Are Colgate-Palmolive's margins and returns stable enough for the fundamental growth formula? If not, what revenue growth, margin path and sales-to-capital ratio should drive the forecast, and what does the company's own history say that ratio is?
    - Sources needed: Margin and return history; consensus; sales to capital for the company and the industry.
    - Where to find: ledger `facts.ginzu-inputs`, `facts.valuation-input-evidence`, `facts.ginzu-replication-path`, `facts.ginzu-sensitivities`, `forecast.sales_to_capital`; model-output.md §8.
    - Answer: No. The return on capital is high but the formula's other half, the reinvestment rate, swings from 30.47% to −12.94% within four years, and the equity version is unusable on book equity of $54M. So the forecast is built the other way: revenue growth, then a margin, then the reinvestment needed to support the revenue, from a sales-to-capital ratio. The inputs, each with its reason and the alternative (`facts.ginzu-inputs`):

        | Input | Choice | Why | Alternative, and what it is worth |
        |---|---|---|---|
        | Revenue growth, next year | 2.25% | Analysts' revenue for the next twelve months, $21,764M, against $21,285M for the last twelve | One point higher or lower in years 1 to 5: $65.44 or $58.41 a share |
        | Revenue growth, years 2 to 5 | 3.1% a year | Consensus revenue grows 3.07% a year from 2027 to 2030; sales grew 3.3% a year from 2016 to 2025 | Same row |
        | Operating margin | 20.5% next year, rising to 21.3% by year 5 | Consensus margins less about 0.7 points. See below | Consensus as published, 21.2% rising to 22%: $64.27. Margin held at 20.5%: $59.37 |
        | Sales to capital | 2.2 | Colgate's own ratio is 2.22 (sales of $20,382M on invested capital of $9,169M) and the US household products average is 2.21 | The workbook's global default, 1.79: $61.19 |
        | Tax rate | 23.5%, rising to 25% by year 10 | Colgate paid 23.1% in 2025 before the write-down and 23.8% in the first nine months of 2026 | 25% from year 1: $61.36 |

      Why the margin sits below consensus. Analysts forecast operating income on the company's adjusted basis, which leaves out restructuring and similar charges. Our operating income keeps them in. The gap between the two has been $52M, $85M, $122M and $327M in 2023, 2024, 2025 and the first nine months of 2026: $586M over 3.75 years, about $156M a year, or roughly 0.7% of sales (`facts.valuation-input-evidence`). A productivity program expanded in April 2026 is expected to cost $350M to $550M in total, of which $346M is booked, so the charges continue. Using the analysts' margin with our definition of income would count a cost as if it had gone away.
      The company's own history on sales to capital: 2.22 in 2025, which matches the industry almost exactly. This input matters little. Colgate needs so little capital that even the lower default costs only $0.65 a share (`facts.ginzu-sensitivities`).

## Cumulative Project — Questions for This Lesson

- **What is the historical growth rate in your company's revenues? EBIT? Net income?**
  Growth a year (`facts.growth-history-and-consensus`):

  | Measure | 2016 to 2025 | 2020 to 2025 |
  |---|---|---|
  | Net sales | 3.3% | 4.4% |
  | Operating income (EBIT) before write-downs | 0.7% | 1.7% |
  | Net income as reported | −1.5% | −4.6% |
  | Net income with the 2025 write-down added back | 2.0% | 1.7% |
  | Diluted earnings per share as reported | −0.4% | −3.5% |

  The further down the income statement, the slower the growth. Reported net income is distorted by the 2025 write-down; without it, profit grew about 2% a year. Earnings per share did a little better than net income because the share count fell 1.1% a year.

- **What are analysts or managers projecting as an expected growth rate in the future?**
  Analysts (Capital IQ consensus, 2026-11-20, `facts.growth-history-and-consensus`): revenue growth of 3.57% a year from 2025 to 2028 and 3.07% a year from 2027 to 2030; operating income growth of about 4.4% a year; normalized earnings per share growth of 5.58% a year to 2030, and a long-term figure of 5.45% from two analysts. Management: Colgate does not publish a long-range growth plan in the filings we hold. Its guidance for 2026, as Capital IQ records it, is revenue 4.0% to 5.0% above 2025 and earnings per share 4.9% to 7.0% higher.
  The three layers fit together. Revenue grows about 3%, margins are expected to widen a little, so operating income grows about 4%, and buybacks shrink the share count about 1% a year, so earnings per share grow 5% to 6%. Only the first of those three is growth in the business. The valuation uses revenue growth and its own margin path; it does not use the 5.45% earnings per share figure, because part of that is buybacks.

- **Assuming that your company continues to earn its current ROIC/ROE and maintaining its existing reinvestment rate, what would the expected growth rate be in earnings?**
  Between −4.47% and 2.16%, depending on the years and on whether acquisitions count (`facts.fundamental-growth`). On the 2025 figures alone, a 34.56% return and a reinvestment rate of −12.94% give −4.47%: taken literally, a company slowly liquidating. That is not a forecast; it reflects three years in which working capital released cash. Over 2021 to 2025 with acquisitions counted, 6.26% reinvested at 34.56% gives 2.16%, which is close to what profit actually grew. The equity version (retention times return on equity) cannot be computed: Colgate retained 14.49% of 2025 earnings, but return on equity is meaningless on book equity of $54M.

- **If margins are changing, what are your estimates of revenue growth, margins and reinvestment for the future?**
  Margins have changed: down from 24.0% in 2017 to 20.7% in 2025 before write-downs, and 19.17% over the last twelve months on our definition ($4,080M on $21,285M). Our estimates (`facts.ginzu-replication-path`):

  | | Year 1 | Year 5 | Year 10 | After year 10 |
  |---|---|---|---|---|
  | Revenue growth | 2.25% | 3.10% | 3.00% | 3.00% |
  | Revenue $M | 21,764 | 24,591 | 28,563 | |
  | Operating margin | 20.50% | 21.30% | 21.30% | 21.30% |
  | Operating income $M | 4,462 | 5,238 | 6,084 | |
  | Reinvestment $M | 307 | 344 | 389 | 15% of after-tax income |
  | Free cash flow to the firm $M | 3,106 | 3,663 | 4,173 | |

  The margin path is the most optimistic thing in the forecast. It assumes a recovery of more than a point from the trailing 19.17% within a year, then a slow rise. That follows analysts, less the charges they leave out. If the margin simply stayed where it has been for the last twelve months, the value would be $54.73 a share, $7.10 lower (`facts.ginzu-sensitivities`). If it climbed back to the 24.0% of 2017, $70.15. Neither reaches the $98.71 price.

## Notes

What this lesson establishes: the revenue, margin and reinvestment inputs to the valuation, and that none of them, within any range the evidence supports, closes the gap to the market price. A margin of 33.3% from year 5 on, or revenue growth of 13.4% a year in years 2 to 5, would be needed (`facts.price-implied-assumptions`). The highest margin in the ten years of sales data we hold was 26.0%, in 2016 (`facts.valuation-arithmetic`).

The year-by-year figures above come from a replication of the workbook's valuation sheet, built from the formulas in the professor's original file. The replication reproduces all six results read from the filled workbook to the cent, so we treat its year-by-year path as the workbook's. It is labelled a replication because the filled workbook itself is not in the folder.

Cross-check. The repo model's section 6 uses analysts' revenue and margins for 2026 to 2028 as published (`forecast.years`), the same 2.2144 sales-to-capital ratio and no deduction for restructuring. It is not the valuation. Its value, $60.85, is compared with the workbook's in lesson 34.

Confidence: high on history; moderate on the forecast. Revenue growth is the firm part: history, analysts and management are within a point of each other. The margin is the soft part, and we have said which way it leans.
