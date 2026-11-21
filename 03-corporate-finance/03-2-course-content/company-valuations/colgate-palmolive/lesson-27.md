---
title: "Colgate-Palmolive (CL) — Lesson 27: Action and Follow Up"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 27: Action and Follow Up

### Lesson 27 — Action and Follow Up

- **Lesson 27, Session 27 · Part 1 — "Companies Earn the Right to Accumulate Cash: The Dividend Assessment Matrix"** ([transcript](../../04-dividends-and-valuation/lesson-27/session-27-part-1.md))
    - Quote: "Companies earn the right to accumulate cash. They're not endowed with that right."
    - Question for Colgate-Palmolive: Has Colgate-Palmolive earned the right to hold cash? Over the current management's tenure, has return on capital beaten the cost of capital, and has the stock beaten the market? Which cell of the dividend assessment matrix does the company fall in?
    - Sources needed: Cash returned against FCFE; return on capital against cost of capital; stock returns against required returns; the acquisition record.
    - Where to find: model-output.md §5 and §8; ledger `facts.fcfe-by-year-2018-2025`, `facts.dividends-xlsx-results`, `facts.shareholder-return-2020-2025`, `facts.jensens-alpha-estimate`, `facts.acquisitions-2018-2025`, `facts.roic-variants-2025`.
    - Answer: The matrix has two questions. Does the company return more or less than its free cash flow to equity? And are its projects good or poor?

        | | Returns less than FCFE (cash builds up) | Returns about what it generates, or more |
        |---|---|---|
        | Good projects | Give management flexibility | Colgate is here. No pressure to change |
        | Poor projects | Pressure to pay out more | Pressure to cut payout and fix the business |

      On the first question, lesson 26: Colgate returned about 105% of FCFE over five years once option proceeds are counted, and holds cash of only 1.61% of firm value. It is not accumulating. On the second, the two tests the lecture uses disagree, and we report both.
        - Return on capital against cost of capital: clearly good. 34.56% against 8.34% in 2025, and above 30% in each of the last three years (model-output.md §8). Return on equity cannot be used: it is 3,948% because book equity is $54M.
        - Stock return against required return: poor. The professor's workbook shows the shares fell short of their required return in four of the five years from 2021 to 2025, by 3.03 to 25.08 points (`facts.dividends-xlsx-results`). Over five years to December 2025 the shares returned 4.0% in total against 96.2% for the S&P 500 (`facts.shareholder-return-2020-2025`). The one regression measure that looks favourable, a Jensen's alpha of about 2.1% a year, depends on a beta of 0.315 that we rejected in lesson 10 (`facts.jensens-alpha-estimate`).
      How both can be true: the high return on capital is the return on brands built long ago, and the market priced it in years ago. The share price responds to what is new, and what was new in this period was slow growth, margins that slipped, and acquisitions that were written down. We place Colgate in the good-projects column on the strength of its existing business, with that qualification attached.
      Has it earned the right to hold cash? It has not asked for it, which makes the question easy. If it did start building cash, the acquisition record ($2,211M written down against $3,894M spent, `facts.acquisitions-2018-2025`) says shareholders should be reluctant to grant it.

- **Lesson 27, Session 27 · Part 2 — "Dividend Addicts, Family Subsidies, and Control: Assessing Dividend Policy"** ([transcript](../../04-dividends-and-valuation/lesson-27/session-27-part-2.md))
    - Quote: "So BP kept putting off the bad decision year after year after year hoping that something good will happen."
    - Question for Colgate-Palmolive: Did Colgate-Palmolive ever fund dividends or buybacks with new borrowing, or pay out to serve a controlling holder's needs rather than its own capacity? What pressure did that create, and what decision was being deferred?
    - Sources needed: Net debt issued by year against acquisitions and cash returned; ownership.
    - Where to find: ledger `facts.fcfe-by-year-2018-2025`, `facts.dividends-xlsx-results`, `facts.acquisitions-2018-2025`, `governance.controlling_holders`, `facts.dividends-2021-2025`, `facts.growth-and-margin-history`.
    - Answer: No to both. There is no controlling holder (`governance.controlling_holders`). And the dividend has not depended on borrowing. FCFE before any debt flows was $17,868M over 2018 to 2025 against dividends of $13,590M, so dividends were covered 1.3 times from the business alone (`facts.dividends-xlsx-results`). Net borrowing over those eight years was $951M, and it came in the two acquisition years (lesson 26).
      Colgate is not BP in the lecture's example: a company holding a dividend it could no longer earn. But the mechanism the lecture warns about is present in a milder form. A dividend that has risen every year is a commitment that management will go a long way to keep. Dividends were 94.73% of net income in 2022 and 85.51% in 2025 (`facts.dividends-2021-2025`). Those are write-down years, and the dividend is comfortably covered by cash flow. The pressure would become real only if cash flow itself fell, and the long-run trend to watch is that operating income before write-downs grew 0.7% a year over a decade while the dividend per share grew 3.6% a year over the last four years (`facts.growth-and-margin-history`, `facts.dividends-2021-2025`). Buybacks close the gap by shrinking the share count. That works for a long time, and it does not work forever.
      The decision being deferred, as we read it, is not about the dividend. It is about growth: whether to accept being a slow-growing company that returns its cash, or to keep buying growth through acquisitions. The payout policy is sound either way.

## Cumulative Project — Questions for This Lesson

- **If your firm has returned less cash than it can over time and has a big cash balance, do you trust the firm with your cash?**
  The premise does not hold. Colgate has returned slightly more than its FCFE, and its cash balance is $1,395M, 1.61% of firm value. So the question is hypothetical, and our answer to the hypothetical is: only partly. We would trust management to run the existing brands, where returns are 34.56%. We would not trust it with a large pool of cash to spend on acquisitions, given that write-downs since 2021 equal 57% of what was spent on acquisitions since 2018. Colgate's actual practice, paying the cash out, is the one that record supports.

- **If your firm has returned more cash than it can over time, should it scale back cash return?**
  No. The excess is small and explained: $637M over five years after option proceeds, 4.1% of what was returned (`facts.fcfe-by-year-2018-2025`). It has not been funded by rising debt or a shrinking cash balance (lesson 26). Scaling back would build cash that the company has no good use for.
  Two refinements.
    - Keep the split. The regular dividend, about $1.8 billion a year, is covered 1.3 times by FCFE before debt flows over eight years. The buyback, between $1.1 billion and $1.7 billion a year, is the part that should flex, and it has.
    - Lessons 19 and 22 recommend raising debt from 9.34% to 20% and paying the proceeds out as special dividends, because the valuation puts the share price above its value and a buyback at that price would favour the sellers. That would lift cash returned well above FCFE for about five years. It is consistent with this lesson, because it is a decision to change how the company is financed, with a stated end, and not a payout the business is expected to sustain from operations.

## Notes

Colgate sits in the cell of the matrix that calls for no change: it returns what it generates and its existing business earns far more than its cost of capital. Confidence is high on the first half (lesson 26) and qualified on the second: returns on capital are excellent, shareholder returns have been poor, and the two are measuring different things.

The practical conclusion for the report: do not recommend a change in dividend policy. The recommendations that matter are elsewhere: more debt (lesson 22), and discipline on acquisitions, which is where value has been lost.

One open item carried forward: the workbook's required-return figures use year-end to year-end stock returns and the bottom-up beta. They were read from the sheet, not recomputed here.
