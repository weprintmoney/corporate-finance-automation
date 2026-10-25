---
title: "SolarWinds (SWI) — Lesson 27: Assessing Dividend Policy: Trust, Projects, and the Cash Matrix"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 27: Assessing Dividend Policy: Trust, Projects, and the Cash Matrix

### Lesson 27 — Assessing Dividend Policy: Trust, Projects, and the Cash Matrix

- **Lesson 27, Session 27 · Part 1 — "Companies Earn the Right to Accumulate Cash: The Dividend Assessment Matrix"** ([transcript](../../04-dividends-and-valuation/lesson-27/session-27-part-1.md))
    - Quote: "Companies earn the right to accumulate cash. They're not endowed with that right."
    - Question for SolarWinds: Has SolarWinds earned the right to hold cash? Over the current management's tenure, has return on capital beaten the cost of capital, and has the stock beaten the market? Which cell of the dividend assessment matrix does the company fall in?
    - Sources needed: Return on invested capital against the cost of capital; the stock's return against a benchmark; cash returned against free cash flow to equity.
    - Where to find: model-output.md §1, §5 and §8; `company.history`; `sources/filings/swi-def14a-2024.md` Pay versus Performance table. `beta.jensens_alpha` is omitted (`meta.omitted`: no price history for a delisted ticker).
    - Answer: No. Both tests fail, and the matrix cell is "bad projects".
        - Return on capital: model-output.md §8 gives ROIC of 6.66% against a cost of capital of 10.23%, a gap of −3.58 points and economic value added of $-84.0M a year. Return on equity is 7.99% against a cost of equity of 12.65% (−4.66 points).
        - Trend over management's tenure (arithmetic, ledger rows, 25% tax, year-end invested capital): 2022 ROIC was 2.69% on operating income of $86.8M, which is reported EBIT of $-819.6M plus the $906.4M of non-cash impairments, giving $65.1M after tax on $2,422.9M of capital. 2023 was 4.79% ($112.8M on $2,356.3M). 2024 was 6.66% (all three from the §8 "By year" table). The trend is up, the level has not once reached the cost of capital. Goodwill is 100.65% of invested capital (§8), almost all of it from the 2016 buyout, so part of the low ROIC measures the price the sponsors paid, not the quality of the operations.
        - Stock: no price history for the delisted ticker, so no Jensen's alpha. The proxy's table gives $100 invested at the end of 2019 worth $81, $57, $38 and $51 at the ends of 2020–2023, against $142, $190, $135 and $211 for the peer index (facts.tsr-2023). Sudhakar Ramakrishna was CEO for all of 2021–2023 (same fact). The stock lost about half while the index doubled.
        - Matrix: the axes are good or bad projects (ROIC against cost of capital) and cash surplus or deficit (cash returned against FCFE). SolarWinds has bad projects. In 2023 it returned $18.8M against FCFE of $59.4M, a surplus (§5); in 2024 it returned $194.7M against $127.0M, a deficit. Both are in the bad-projects row, where the lecture's advice is to deal with the investment problem first.

- **Lesson 27, Session 27 · Part 2 — "Dividend Addicts, Family Subsidies, and Control: Assessing Dividend Policy"** ([transcript](../../04-dividends-and-valuation/lesson-27/session-27-part-2.md))
    - Quote: "So BP kept putting off the bad decision year after year after year hoping that something good will happen."
    - Question for SolarWinds: Did SolarWinds ever fund dividends or buybacks with new borrowing, or pay out to serve a controlling holder's needs rather than its own capacity? What pressure did that create, and what decision was being deferred?
    - Sources needed: Debt issued and repaid in each payout year; the source of cash for each dividend; who received it.
    - Where to find: `company.history`; `governance.controlling_holders`; `sources/filings/swi-10k-fy2023.md` (2021 cash flow statement); `swi-10k-fy2024.md` note 9.
    - Answer: No borrowing-funded payout. The controlling holders did take most of each dividend.
        - 2024: the $168.2M dividend was paid with net new debt of $0.0M ($10.0M drawn on the revolver, $10.0M repaid; `company.history`). Cash fell by $29.9M and debt fell by $15.4M ($1,300.4M to $1,285.0M).
        - 2021: the $237.2M dividend (facts.special-dividend-2021) came from the $505.6M of net cash that N-able sent to SolarWinds at separation (facts.spin-distribution-2021). That cash did originate in debt placed on N-able, so it is a distant relative of the BP pattern, but SolarWinds itself did not borrow to pay.
        - Whose needs: Silver Lake and Thoma Bravo held 36.56% and 29.79% (`governance.controlling_holders`), so $111.6M of the 2024 dividend (66.35% × $168.2M) went to them. Nothing in the filings says the sponsors needed the cash. That motive would be an inference, and the ledger does not support it.
        - What was deferred: the exit. The sponsors had held the company since 2016. Dividends in 2021 and 2024, a $664.4M debt paydown in 2022 and then a sale in February 2025 are the sequence of a holder returning capital while waiting for a buyer. The credit agreement allowed it: restricted payments are limited "subject to certain exceptions" and the only financial test springs when the revolver is more than 35% drawn (`debt.covenants`).

## Cumulative Project — Questions for This Lesson

- **If your firm has returned less cash than it can over time and has a big cash balance, do you trust the firm with your cash?**
  No. ROIC of 6.66% against 10.23% (model-output.md §8) means each dollar kept in the business is expected to earn less than investors require, and the stock's index fell to 51 against the peers' 211 (facts.tsr-2023). The premise only partly holds. Over 2022–2024 SolarWinds returned $224.6M against FCFE of $-419.8M (§5, impairments added back) after $673.7M of debt repayment (lesson 26), and cash ended at $259.3M, 6.7% of firm value ($3,889.9M, §1; 259.3 ÷ 3,889.9). That is not a big hoard. The cash that was big, $732.1M at the end of 2021 (facts.cash-end-2021), was paid out or used to repay debt within two years.

- **If your firm has returned more cash than it can over time, should it scale back cash return?**
  Not on the 2024 evidence alone. It returned 153% of FCFE in 2024 ($194.7M against $127.0M, §5), but the special dividend was a single payment, debt did not rise, and cash was drawn from $289.2M to $259.3M, which still leaves cash above 2022's $148.9M (`company.history`). Over the two years 2023–2024 it returned $213.5M against FCFE of $186.4M (arithmetic from §5), 115%, which is close to even. The matrix says the real problem is returns below the cost of capital, which scaling back dividends would not fix.

## Notes

Established for later lessons: SolarWinds sits in the bad-projects row of the matrix (ROIC 6.66% against 10.23%, §8), so the stable ROIC for the terminal value in lesson 32 is set near the cost of capital (`forecast.stable_roic` 10%), not above it. The Jensen's alpha field is omitted; the proxy's total-return index stands in for it and is through 2023 only. The §8 "By year" table adds back the 2022 impairment for ROIC.
