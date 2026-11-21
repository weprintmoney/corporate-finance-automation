---
title: "Colgate-Palmolive (CL) — Lesson 28: The End Game"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 28: The End Game

### Lesson 28 — The End Game

The peer set for this project is not fixed yet (`meta.omitted`), and the Capital IQ comparison page in our files carries no dividend data for the candidates. This lesson therefore compares Colgate with industry averages from Professor Damodaran's datasets and with a market-wide regression from the lesson slides. Each source's date is given, because they differ.

- **Lesson 28, Session 28 · Part 1 — "Me-Too Corporate Finance: Benchmarking Dividend Policy Against the Peer Group"** ([transcript](../../04-dividends-and-valuation/lesson-28/session-28-part-1.md))
    - Quote: "Much of corporate finance is what I call 'me-too corporate finance.'"
    - Question for Colgate-Palmolive: How does Colgate-Palmolive's payout compare with its peers, and what would a regression of payout on growth, beta and leverage predict for a company with its characteristics? Is the company copying its sector, or diverging for a reason?
    - Sources needed: Industry payout ratios and yields; cash returned against net income and FCFE for the industry; a market regression; Colgate's beta, expected growth and debt ratio.
    - Where to find: ledger `facts.sector-dividends`, `facts.payout-regression-2014`, `facts.dividends-2021-2025`, `facts.fcfe-by-year-2018-2025`, `forecast.analyst_growth`; model-output.md §1; modules-2-4-cross-checks-output.md §11.
    - Answer: Colgate looks like its industry. Side by side (`facts.sector-dividends`, `facts.dividends-2021-2025`, `facts.fcfe-by-year-2018-2025`):

        | Measure | Colgate | Household products | Food processing | All US companies | Industry data as of |
        |---|---|---|---|---|---|
        | Dividend payout | 77.46% over 2021–2025; 85.51% in 2025; 62.3% before the write-down | 67.25% | 143.11% | 34.83% | January 2026 |
        | Dividend yield | 2.11% | 2.94% | 3.84% | 1.10% | January 2026 |
        | Dividends plus buybacks, % of net income | 136.9% over 2021–2025 | 153.90% | 100.36% | 87.16% | January 2024 |
        | Cash returned net of share issues, % of FCFE | 105.0% over 2021–2025 | 88.21% | 124.37% | 72.77% | January 2024 |

      Reading across. Colgate's payout ratio is close to the household products average: above it on reported earnings, a little below it before the write-down. Its yield is lower than the industry's, 2.11% against 2.94%, which says the market pays more for a dollar of Colgate's dividend than for the average household products company's. Counting buybacks, Colgate returns a somewhat smaller share of net income than the industry did two years ago and a somewhat larger share of FCFE. On every measure it is far above the market as a whole, as a mature, slow-growing business should be.
      The regression. The lesson slides give a regression across US companies from January 2014 (`facts.payout-regression-2014`): payout = 0.649 − 0.296 × beta − 0.800 × expected growth + 0.300 × debt to capital. With Colgate's beta of 0.7321, analysts' expected earnings growth of 5.45% and a debt ratio of 9.34%, the predicted payout is 41.67%. The matching yield regression predicts 2.12%.
      So the regression says a company with Colgate's risk, growth and debt would pay out about 42% of earnings, and Colgate pays 77%, or about 62% before write-downs. On yield it is exactly where predicted: 2.11% against 2.12%. We put more weight on the yield result and less on the payout gap, for three reasons. The regression is twelve years old and no later edition is in our files. It covers every US company, most of which are younger and reinvest more. And the growth input, 5.45%, is growth in earnings per share, which Colgate's buybacks lift above the growth of the business; a lower growth figure would raise the predicted payout.
      Copying or diverging? Neither, in the pejorative sense of the quote. Colgate's policy matches its industry because the industry's economics match its own: branded staples generate cash and need little reinvestment. Lessons 25 to 27 reached the same policy from Colgate's own cash flows and projects, without reference to peers. Where Colgate does differ from its industry is in ownership, with institutions at 87.19% against an industry average of 42.96%, and that difference argues for buybacks over dividends at the margin, which is the mix Colgate uses.

## Cumulative Project — Questions for This Lesson

- **How does your company dividend and cash return policy measure up against other companies in the sector?**
  It is typical of the sector. Payout of 77.46% over five years against 67.25% for household products; yield of 2.11% against 2.94%; dividends plus buybacks of 136.9% of net income against 153.90%; net cash returned of 105.0% of FCFE against 88.21%. The differences are small next to the gap between this industry and the market (payout 34.83%, yield 1.10%). Colgate's second business, pet food, is benchmarked against food processing, where payout is higher still (143.11% of a depressed net income); it is 23% of sales and does not change the picture.
  Limits on this comparison: the industry averages are sums across 110 and 93 companies of very different sizes, dominated by the largest; the two tables are two years apart; and company-by-company peer figures are not in our files. When the peer set is fixed in lesson 35, dividend data for those companies should be added and this answer checked.

- **Given how much other companies in the sector are returning to stockholders, is your company returning too much or too little?**
  About the right amount by this test. It is within a few points of the sector on every measure and on the regression's yield. Against the regression's payout it looks high (77% against 42%), for the reasons given: an old, market-wide regression and a growth input flattered by buybacks.
  The sector test is the weakest of the three we have applied, and it agrees with the two stronger ones. Lesson 26 compared cash returned with Colgate's own FCFE and found them about equal. Lesson 27 placed Colgate in the cell of the assessment matrix that needs no change. A me-too comparison adds only this: Colgate would not stand out to an investor screening the sector for companies that pay too little or too much.

## Notes

End of the dividend module. Conclusions for the report:

- Colgate pays a high, steady, slowly rising dividend and tops it up with flexible buybacks, about $3 billion a year in total (lesson 24).
- The trade-off supports a high payout: cash the business cannot use, an institutional shareholder base, and a poor acquisition record (lesson 25).
- It returned roughly what it generated: 105% of FCFE over five years once option proceeds are counted (lesson 26).
- No change in dividend policy is called for (lesson 27), and the sector comparison agrees (this lesson).

Confidence: moderate for this lesson taken alone, because of dated and aggregated benchmarks and no fixed peer set; high for the module's conclusion, because three independent tests agree.

Lessons 29 to 35 turn to valuation. Nothing in lessons 13 to 28 quotes a value per share from the valuation workbook; those figures are still being settled and belong to the lessons that follow.
