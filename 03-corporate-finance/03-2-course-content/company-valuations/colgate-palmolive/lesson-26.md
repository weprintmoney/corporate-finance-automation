---
title: "Colgate-Palmolive (CL) — Lesson 26: Assessments"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 26: Assessments

### Lesson 26 — Assessments

Three sources appear in this lesson. The professor's `dividends.xlsx`, filled in for 2018 to 2025 (`professor-spreadsheet/results.md`; ledger `facts.dividends-xlsx-results`). The repo model's section 5, for 2023 to 2025. And a year-by-year table built from the same rows that went into the workbook (modules-2-4-cross-checks-output.md §10; ledger `facts.fcfe-by-year-2018-2025`). The workbook counts acquisitions as capital spending; the model's section 5 does not. Each figure below says which it is.

- **Lesson 26, Session 26 · Part 1 — "FCFE as the Potential Dividend: Computing It and Reading the Payout Gap"** ([transcript](../../03-financing-mix-and-dividends/lesson-26/session-26-part-1.md))
    - Quote: "If you're already in a hole, you need to stop digging."
    - Question for Colgate-Palmolive: What was Colgate-Palmolive's free cash flow to equity in each of the last five years, and did the cash it returned (dividends plus buybacks) fall short of, match, or exceed it? If it paid out more than it earned, where did the money come from?
    - Sources needed: Net income, depreciation and write-downs, capital spending and acquisitions, working capital changes, debt issued and repaid, dividends, buybacks, proceeds from option exercises.
    - Where to find: ledger `facts.fcfe-by-year-2018-2025`, `facts.dividends-xlsx-results`, `facts.option-proceeds-2018-2025`; model-output.md §5; `professor-spreadsheet/inputs.md`.
    - Answer: Free cash flow to equity (FCFE) is the cash left for shareholders after the business has paid for its reinvestment and settled with its lenders: net income, plus depreciation and non-cash write-downs, less capital spending and acquisitions, less the increase in working capital, plus new debt net of repayments. On the workbook's definition, in $ millions (`facts.fcfe-by-year-2018-2025`):

        | Year | FCFE | Dividends plus buybacks | Excess over FCFE | Returned ÷ FCFE | Option proceeds | Excess net of option proceeds |
        |---|---|---|---|---|---|---|
        | 2021 | 2,409 | 2,999 | 590 | 124.49% | 424 | 166 |
        | 2022 | 2,518 | 2,999 | 481 | 119.10% | 418 | 63 |
        | 2023 | 2,314 | 2,877 | 563 | 124.33% | 380 | 183 |
        | 2024 | 2,885 | 3,528 | 643 | 122.29% | 638 | 5 |
        | 2025 | 2,712 | 3,033 | 321 | 111.84% | 101 | 220 |
        | Five years | 12,838 | 15,436 | 2,598 | 120.24% | 1,961 | 637 |

      On the face of it Colgate returned more than its FCFE in every one of the five years, by 12% to 24%, and $2,598M more in total. Read alone, that would put Colgate in the "hole" the quote describes. It is not, and the reason is one line the formula leaves out.
      When employees exercise stock options they pay the company cash. Colgate received $1,961M that way over the five years (`facts.option-proceeds-2018-2025`). The FCFE formula starts from net income and never sees that cash. But the buybacks in the same table are largely the other side of the same programme: the company buys shares in the market and reissues them to employees who exercise. Counting the buyback and not the proceeds overstates what shareholders were paid. Net of option proceeds, the five-year excess is $637M, 4.1% of the cash returned. Over the full eight years in the workbook the gross excess is $5,392M, option proceeds are $3,662M, and the net excess is $1,730M, 7% of the $24,211M returned (`facts.dividends-xlsx-results`).
      So the finding is that Colgate returned roughly what it generated: about 105% of FCFE over five years on the net basis. It did not pay out more than it could afford, and it did not hold cash back.

- **Lesson 26, Session 26 · Part 2 — "Cash Accumulation and What Happens When Payout Falls Short of Capacity"** ([transcript](../../03-financing-mix-and-dividends/lesson-26/session-26-part-2.md))
    - Quote: "The point I'm trying to make is when you hold back cash, your cash balance balloons out."
    - Question for Colgate-Palmolive: Where did the gap between Colgate-Palmolive's free cash flow to equity and the cash it returned show up: the cash balance, debt paydown, or acquisitions? Did any shareholder act as an activist to force the cash out?
    - Sources needed: Cash balances and debt over the period; acquisitions; ownership.
    - Where to find: ledger `facts.fcfe-by-year-2018-2025`, `facts.debt-ratio-history`, `facts.acquisitions-2018-2025`, `facts.holders-capital-iq`, `company.cash`.
    - Answer: The quote describes the opposite of Colgate. Cash has not ballooned: cash and equivalents were $1,535M at the end of 2017, $888M at the end of 2020 and $1,288M at the end of 2025 (`facts.fcfe-by-year-2018-2025`). With marketable securities the 2025 figure is $1,395M, 1.61% of firm value (`facts.debt-trade-off-sizes`). There is no hoard for anyone to force out, and no activist has tried: the largest holder Capital IQ tags as an activist owns 0.05% (`facts.holders-capital-iq`).
      Where the small remaining gap went:
        - Not into the cash balance in any lasting way. It fell $247M over eight years and rose $400M over the last five.
        - Not into debt paydown. Net debt issued was positive: $951M over eight years and $294M over the last five. The two years of heavy borrowing, 2019 ($1,433M) and 2022 ($1,647M), are the two years of large acquisitions ($1,711M and $809M, `facts.acquisitions-2018-2025`). Colgate borrowed to buy businesses, not to pay dividends.
        - Into acquisitions, in the sense that they are the swing item in FCFE. The $3,894M spent on them is inside the workbook's capital spending. If acquisitions are treated as a separate decision and left out, eight-year FCFE is $22,713M and cash returned is 106.60% of it before counting any option proceeds.
      The net excess that is left ($1,730M over eight years) is not traced line by line. Other items the formula does not count, such as stock-based compensation expense, which is not a cash cost ($155M in 2025, `company.sbc`), are large enough to cover it. We state that as the likely explanation, not a reconciliation.

## Cumulative Project — Questions for This Lesson

- **How much has your company returned to its stockholders, in the form of dividends and stock buybacks in the last five years?**
  $15,436M from 2021 to 2025: $8,731M in dividends and $6,705M in buybacks (`facts.fcfe-by-year-2018-2025`). That is 136.9% of net income over the period (`facts.dividends-2021-2025`). Net of the $1,961M employees paid to exercise options, buybacks were $4,744M and the total returned was $13,475M. Over the workbook's eight years the total is $24,211M: $13,590M of dividends and $10,621M of buybacks, or $6,959M of buybacks net of option proceeds.

- **How much cash could your company have returned in the last five years? (Estimate FCFE)**
  $12,838M on the workbook's definition: $12,544M before debt flows plus $294M of net new debt (`facts.fcfe-by-year-2018-2025`). Year by year it ran between $2,314M and $2,885M, which is steady. Two cross-checks:
    - The repo model, which leaves acquisitions out, gives $8,204.0M for 2023 to 2025 against $9,438.0M returned, 115.04% (model-output.md §5). The two sources agree for 2023 and 2024 to the dollar and differ in 2025 by exactly the $293M Prime100 acquisition ($3,005M against $2,712M).
    - The workbook's eight-year total is $18,819M: net income of $18,734M, almost unchanged by the adjustments, because depreciation plus write-downs roughly paid for capital spending plus acquisitions over the period.
  Adding the $1,961M of option proceeds, which is cash that did arrive, the amount Colgate could have returned over five years is about $14,799M, against $15,436M actually returned.

- **If there is a difference, where is it showing up (cash balances, debt ratios)?**
  The difference is small once option proceeds are counted (4.1% of cash returned over five years, 7.1% over eight), and it does not show up as a trend in either place. The cash balance is about where it was. The debt ratio has moved between 10% and 12% for six years with no direction (`facts.debt-ratio-history`). What the pattern shows is a company that pays out its free cash flow as it arrives, borrows when it buys a business, and keeps neither a cash pile nor a rising debt load.

## Notes

The headline, and the correction that produced it. `dividends.xlsx` taken alone shows cash returned of $24,211M against FCFE of $18,819M, 128.65%, and an excess in every year. That reading is incomplete, and it is not our finding. Option exercise proceeds of $3,662M explain two-thirds of the gap. Colgate returned roughly what it generated: within 7% over eight years and 4% over five.

Confidence: high on the amounts returned and on option proceeds, all disclosed. Moderate on FCFE itself, which depends on choices: whether acquisitions count as reinvestment (we follow the workbook and count them) and how working capital is measured. The conclusion does not depend on those choices: on every version, the net figure is between about 100% and 107% of FCFE.

What this means for the plan in lesson 22. Colgate is not over-distributing today, so borrowing an extra $1,845M a year for special dividends would be new: for those five years it would return well over its FCFE, by design, until debt reaches 20%. That should be described to shareholders as a change in capital structure with an end date, not as a higher sustainable payout.

Not read from the workbook: its 2018 to 2020 yearly performance rows and its forecast sheet (noted in `professor-spreadsheet/results.md`). The 2018 to 2020 FCFE figures in our table are computed from the input rows, not read from the sheet.
