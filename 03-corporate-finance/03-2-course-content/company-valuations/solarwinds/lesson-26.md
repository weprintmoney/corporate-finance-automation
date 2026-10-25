---
title: "SolarWinds (SWI) — Lesson 26: Assessing Dividend Policy and Free Cash Flow to Equity"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 26: Assessing Dividend Policy and Free Cash Flow to Equity

### Lesson 26 — Assessing Dividend Policy and Free Cash Flow to Equity

- **Lesson 26, Session 26 · Part 1 — "FCFE as the Potential Dividend: Computing It and Reading the Payout Gap"** ([transcript](../../03-financing-mix-and-dividends/lesson-26/session-26-part-1.md))
    - Quote: "If you're already in a hole, you need to stop digging."
    - Question for SolarWinds: What was SolarWinds' free cash flow to equity in each of the last five years, and did the cash it returned (dividends plus buybacks) fall short of, match, or exceed it? If it paid out more than it earned, where did the money come from?
    - Sources needed: Net income, capital spending, depreciation, working capital change, debt issued and repaid, dividends and buybacks, by year.
    - Where to find: `company.history` in `inputs.yaml`; model-output.md §5; `sources/filings/swi-10k-fy2024.md` (2022–2024 flows) and `swi-10k-fy2023.md` (2021 flows).
    - Answer: Three years can be built on a comparable basis (2022–2024). Years before 2022 include N-able, spun off in July 2021 (`company.history` note), so 2020 and 2021 are not built.
        - Model-output.md §5: FCFE was $-606.2M in 2022, $59.4M in 2023 and $127.0M in 2024 (total $-419.8M). Cash returned was $11.1M, $18.8M and $194.7M (total $224.6M).
        - 2022 and 2023: returned less than FCFE in 2023 (gap $-40.6M), and 2022's FCFE was negative, so any payout at all exceeded it.
        - 2024: returned $194.7M against FCFE of $127.0M, $67.7M more (153% of FCFE: 194.7 ÷ 127.0). The $194.7M is the $1.00 special dividend of $168.2M (`company.history` 2024 dividends) plus $26.5M of buybacks.
        - Where the money came from in 2024: not new debt. Net new debt was $0.0M (a $10.0M revolver draw, repaid). It came from the cash pile built in 2023: cash went from $289.2M to $259.3M (`company.history`), a fall of $29.9M. The rest came from the year's cash flow.
        - The 2022 number needs a caution. Net income of $-929.4M includes $906.4M of non-cash impairments (goodwill $891.1M plus indefinite-lived intangibles; `company.history` 2022 impairment), which are write-downs, not cash. §5 adds them back (the "Impairments added back" column), which is why 2022 FCFE is $-606.2M and not a much larger negative number. The rest of the shortfall is $664.4M of term loan repaid (`company.history` 2022 debt_repaid); before that repayment, FCFE would have been about $58.2M (arithmetic: −606.2 + 664.4).
        - The buybacks are not discretionary repurchases. The ledger notes say they are shares withheld to cover employees' taxes on vesting stock.

- **Lesson 26, Session 26 · Part 2 — "Cash Accumulation and What Happens When Payout Falls Short of Capacity"** ([transcript](../../03-financing-mix-and-dividends/lesson-26/session-26-part-2.md))
    - Quote: "The point I'm trying to make is when you hold back cash, your cash balance balloons out."
    - Question for SolarWinds: Where did the gap between SolarWinds' free cash flow to equity and the cash it returned show up: the cash balance, debt paydown, or acquisitions? Did any shareholder act as an activist to force the cash out?
    - Sources needed: Year-end cash, debt, controlling holders, any activist filing.
    - Where to find: `company.history` (cash, debt_total), `governance.controlling_holders`, `sources/filings/swi-10k-fy2023.md` cash flow statement, `swi-def14a-2024.md`.
    - Answer: Both the cash balance and debt paydown, in different years; no acquisitions in the ledger years.
        - 2021: the N-able separation put $505.6M of net cash into SolarWinds (facts.spin-distribution-2021). Year-end cash was $732.1M (facts.cash-end-2021). The $237.2M special dividend (facts.special-dividend-2021, paid 2021-08-24) came out of it.
        - 2022: the balloon was deflated by debt paydown. $664.4M of the term loan was repaid; cash fell to $148.9M and debt fell to $1,319.2M (`company.history`).
        - 2023: a smaller balloon. Cash rose to $289.2M while only $18.8M was returned.
        - 2024: the $168.2M special dividend took it back to $259.3M. Over 2022–2024 the cash balance rose by $110.4M (§5), and debt fell from $1,319.2M to $1,285.0M.
        - Activist: none appears in the compiled filings. The 2024 proxy shows no activist campaign. Silver Lake (36.56%) and Thoma Bravo (29.79%) held 66.35% between them (`governance.controlling_holders`; 36.56% + 29.79%). Silver Lake had three designees on the board (`governance.board`). Holders who sit on the board and hold two-thirds of the stock do not need to campaign. Each special dividend went out pro rata, so about 66% of the 2024 payout, $111.6M (168.2 × 0.6635), went to the two sponsors.

## Cumulative Project — Questions for This Lesson

- **How much has your company returned to its stockholders, in the form of dividends and stock buybacks in the last five years?**
  Over 2022–2024, $224.6M: $168.2M of dividends and $56.4M of buybacks, all of them tax-withholding repurchases (model-output.md §5; `company.history`). Adding the two earlier years from the 10-Ks: 2021 had the $237.2M special dividend (facts.special-dividend-2021) and $14.2M of tax-withholding repurchases (facts.withholding-buyback-2020-2021); 2020 had no dividend and $12.1M of repurchases (facts.withholding-buyback-2020-2021, consolidated with N-able). The five-year total is $488.1M (224.6 + 237.2 + 14.2 + 12.1), with the caveat that 2020 includes N-able.

- **How much cash could your company have returned in the last five years? (Estimate FCFE)**
  Model-output.md §5 gives $-419.8M for 2022–2024: $-606.2M, $59.4M and $127.0M, with the 2022 non-cash impairments added back. The whole shortfall is debt repayment: $664.4M in 2022, $9.3M in 2023 and $0.0M net in 2024 (`company.history`), $673.7M in all. Before debt repayment, FCFE for the three years was about $253.9M (arithmetic: −419.8 + 673.7). The company returned $224.6M (§5). So it paid out about what it could have, and used the rest of its cash to repay debt. 2020 and 2021 are not built because N-able was consolidated.

- **If there is a difference, where is it showing up (cash balances, debt ratios)?**
  In 2022 it showed up as debt: $664.4M of repayment, funded by the cash left from the N-able separation. In 2023 it showed up as cash, up to $289.2M. In 2024 the dividend drew cash back down to $259.3M. Debt as a share of total capital at the analysis date is 33.03% (§1), against a book weight of 47.28% (§1). See also the Part 2 answer above.

## Notes

The multi-year FCFE total is dominated by two non-recurring items, the 2022 goodwill impairment and the 2022 term loan prepayment, so the useful reading is year by year: 2023 returned less than FCFE and cash built; 2024 returned more and cash was drawn down, with debt flat. The model's §5 adds back the 2022 impairment, so this lesson uses the §5 figures as printed. Lesson 27 uses this pattern with the returns on capital in §8; lesson 30 uses the same cash flow building blocks for the firm.
