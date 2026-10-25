---
title: "SolarWinds (SWI) — Lesson 29: Intrinsic Valuation Foundations"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 29: Intrinsic Valuation Foundations

### Lesson 29 — Intrinsic Valuation Foundations

- **Lesson 29, Session 29 · Part 1 — "Three Ways to Value a Company and the Four Questions Behind Every DCF"** ([transcript](../../04-dividends-and-valuation/lesson-29/session-29-part-1.md))
    - Quote: "When you have shifting, unstable, or unpredictable debt ratios, you should be valuing the entire firm."
    - Question for SolarWinds: Given how SolarWinds' debt ratio has moved over the years in the ledger, should it be valued as a firm (cash flows before debt payments) or as equity (cash flows after them)? What four inputs will the DCF need, and which is the hardest to estimate here?
    - Sources needed: Debt and equity over time; the debt the buyer committed to.
    - Where to find: `company.history` (debt_total, invested_capital); model-output.md §1; `sources/deal-docs/swi-defm14c-2025-merger.md` (Debt Commitment Letter).
    - Answer: Value the firm.
        - Debt ratio: debt was $1,319.2M, $1,300.4M and $1,285.0M at the ends of 2022–2024 (`company.history`), against book invested capital of $2,422.9M, $2,356.3M and $2,348.0M. Book debt-to-capital, with leases, was 47.28% in 2024 (§1) and market debt-to-capital was 33.03% (§1) because equity is worth more than its book value. The two measures differ by 14 points.
        - The ratio is about to change sharply. The buyer committed $2,225.0M of first lien term debt and $525.0M of second lien (facts.new-debt-2025), $2,750.0M against the $1,285.0M outstanding. Cost of equity depends on the debt ratio (§3 schedule: 11.63% at 21% debt, 12.65% at 33%), so an equity model would need a debt forecast nobody can make. A firm model discounts cash flow before debt at the cost of capital and subtracts debt at the end.
        - Four questions (the lecture): cash flows from existing assets; the value of growth; how risky the cash flows are; when the company becomes mature. In inputs: base-year free cash flow to the firm (lesson 30), the growth path (lesson 31), the cost of capital 10.23% (§1) and the terminal assumptions (g 2.5%, stable ROIC 10%; `market.terminal_growth`, `forecast.stable_roic`).
        - Hardest: the growth and its reinvestment. Management's 2030 free cash flow exceeds after-tax operating income, which assumes no reinvestment. §6 shows the effect: terminal value of $5,552.5M if that cash flow is grown, $3,808.9M with consistent reinvestment.

## Cumulative Project — Questions for This Lesson

- **What is the market capitalization (market value of equity) for your company, relative to its earnings and cash flows?**
  Market value of equity is $2,604.9M (`company.equity_value`: 171.6M shares × $15.18 on 2025-02-05). Against FY2024 net income of $111.9M that is 23.28x (§7). Against FCFE of $127.0M (§5) it is 20.5x (arithmetic). Enterprise value is $3,630.6M (§7), which is 4.56x revenue and 12.84x EBITDA (§7), and 23.2x after-tax operating income of $156.3M (§8; 3,630.6 ÷ 156.3). At the $18.50 deal price equity is worth $3,174.6M (18.50 × 171.6).

- **How much has that market capitalization changed over time?**
  The ledger holds one market capitalization, at the analysis date, so the long history comes from two other measures. Per-share return: $100 invested at the end of 2019 was worth $51 at the end of 2023, with the spin-off treated as a dividend, while the peer index went to $211 (facts.tsr-2023). Share count: 309.9M shares in February 2019 (facts.shares-2019-02-15), which is 155.0M after the 2-for-1 reverse split of July 2021 (facts.corporate-actions-2021), against 171.6M at the record date (`company.shares_basic`). The July 2021 spin-off of N-able removed value, so market capitalization before and after is not one continuous series. From the unaffected price to the deal price, per-share value rose 21.9% (18.50 ÷ 15.18 − 1), and the information statement puts the premium to the 90-day average price at about 35% (facts.premium-90day-vwap).

- **How have earnings/cash flows changed over time?**
  On the comparable 2022–2024 years (`company.history`): revenue $719.4M, $758.7M, $796.9M. EBIT $-819.6M, $150.4M, $208.4M, where 2022 includes $906.4M of non-cash impairments (without them $86.8M, §8). Net income $-929.4M, $-9.1M, $111.9M. FCFE $-606.2M, $59.4M, $127.0M (§5). Free cash flow to the firm $146.3M, $190.6M and $171.4M (§8 "By year"). Revenue grew about 5% a year; the improvement is mostly margin (EBIT margin without the impairments from 12.1% to 26.2%; arithmetic on `company.history`).

## Notes

This lesson fixes the method: free cash flow to the firm at the cost of capital, then debt, cash and options to get to a share price (model-output.md §6). The change in the debt ratio after the deal is why lesson 34 keeps the status quo cost of capital for the main value and treats the optimal ratio as a separate lever.
