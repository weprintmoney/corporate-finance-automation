---
title: "SolarWinds (SWI) — Lesson 34: Value of Control"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 34: Value of Control

### Lesson 34 — Value of Control

- **Lesson 34, Session 34 · Part 1 — "Stories Into Numbers: Building the Full DCF Valuation"** ([transcript](../../04-dividends-and-valuation/lesson-34/session-34-part-1.md))
    - Quote: "A good valuation is a bridge between stories and numbers."
    - Question for SolarWinds: What is the status-quo story for SolarWinds (how it will grow, what margins it will earn, how much it must reinvest, how risky it is) and what intrinsic value per share does the full DCF produce from that story? How does it compare with the market price or the last transaction?
    - Sources needed: Management's 2025–2030 forecast, cost of capital, terminal assumptions, debt, cash, share count, unaffected and deal prices.
    - Where to find: `forecast.years`, `forecast.growth_period_years`, `forecast.stable_roic`, `market.terminal_growth`, `company.*`; model-output.md §1 and §6; `sources/deal-docs/swi-defm14c-2025-merger.md`.
    - Answer: $13.00 a share (model-output.md §6, course method). The story:
        - Growth. A mature IT-monitoring business finishing its move from perpetual licences to subscriptions. Management's plan takes revenue from $832.0M in 2025 to $1,273.0M in 2030 (8.12% a year from 2024's $796.9M; `forecast.years`, `forecast.management_growth`). History is 5.0% a year, so the plan is the optimistic part of the story.
        - Margins. EBIT margin rises from 32.69% to 40.14% (`forecast.years`), against 26.2% in 2024 (my arithmetic, $208.4M ÷ $796.9M).
        - Reinvestment. Free cash flow after stock compensation goes from $212.0M to $419.0M. Inside the plan reinvestment is thin; after 2030 we force it to 25.00% of after-tax EBIT (g ÷ stable ROIC, lesson 32).
        - Risk. Unlevered beta 1.22, levered 1.6714 on 33.03% debt; cost of equity 12.65%; cost of capital 10.23% (model-output.md §1).
        - Arithmetic. Present value of 2025–2030 cash flows $1,321.6M plus present value of terminal value $2,122.7M gives enterprise value $3,444.3M. Less debt $1,285.0M, plus cash $259.3M, is $2,418.6M; less the $187.0M equity claim is $2,231.6M; over 171.6M basic shares is $13.00.
        - Against prices. $13.00 is 0.86x the $15.18 unaffected price and 0.70x the $18.50 deal price (§6). It is also below the low end of both banks' DCF ranges: Goldman Sachs $14.30 to $23.70 and Jefferies $14.70 to $19.70 (`facts.gs-dcf-range`, `facts.jefferies-dcf-range`).
        - Why the gap to the banks. Jefferies applied 2.5% to 3.5% growth to terminal-year cash flow, the method that grows the plan's no-reinvestment cash flow forever. Using that method with our rates gives terminal value $5,552.5M against our $3,808.9M. That difference is about $5.67 a share, which would lift $13.00 to $18.67 (§6, "value per share with the other terminal value"). The banks used higher discount rates (Jefferies 10.70% to 11.70%, `facts.jefferies-dcf-discount-rate-range`; Goldman Sachs 9% to 11%, `facts.goldman-dcf-discount-rate-range`) that work in the other direction.

- **Lesson 34, Session 34 · Part 2 — "The Value of Control: Status Quo vs. Optimal, and the Four Levers to Restructure a Company"** ([transcript](../../04-dividends-and-valuation/lesson-34/session-34-part-2.md))
    - Quote: "The value of control in any company is the difference between two values: the status quo value and the optimal value."
    - Question for SolarWinds: What would change about SolarWinds if it were run optimally (operations, reinvestment, financing mix, growth period), what is it worth with those changes, how large is the value of control, and how likely is it that the change happens given who controls the company?
    - Sources needed: The optimal debt ratio and its value; return on capital against cost of capital; the margin plan; ownership and consent rights.
    - Where to find: model-output.md §3 and §6 (last paragraph); `governance.controlling_holders`, `governance.board`, `governance.marginal_investor`, `debt.covenants`; `sources/deal-docs/swi-defm14c-2025-merger.md`.
    - Answer: Only the financing lever can be priced from the model, and it is worth $0.52 a share. The other three are judgment calls and are not computed.
        - Financing (computed). Optimal debt is 21% against 33.03% today (model-output.md §3). At the optimal cost of capital of 10.03% the enterprise value is $3,533.4M and value per share is $13.52, against $13.00 at the status quo (§6): a gain of $0.52 (4%), or $89.1M of enterprise value ($3,533.4M − $3,444.3M). The §3 table shows a larger $144.4M "value of moving" and $10.9M a year in savings; it capitalizes the savings on the market firm value of $3,889.9M and is a different measure from the DCF difference, and the adjusted present value in §9 gives a third ($220.3M, $1.28 a share); the three are on different bases (§6, §9). To get there SolarWinds would repay $468.1M of debt (§3, "debt above optimum"), more than its $259.3M of cash.
        - Operations (judgment). The plan already assumes a 40.14% EBIT margin by 2030, up from 26.2%. The status-quo case is management's plan, so it already contains most of the operating improvement a new owner would claim. No additional credit.
        - Reinvestment and return (judgment). 2024 return on book capital was about 6.7% against a 10.23% cost of capital (lesson 33). When return is below cost, the value-adding change is to reinvest less or return cash; the DCF already assumes growth after 2030 earns 10%, no excess return. No additional credit.
        - Growth period (judgment). Extending the six years would need a stronger moat than retention of 97% to 99% shows (lesson 32).
        - Value of control, financing lever only: $0.52 a share, about $89.1M in total ($0.52 × 171.6M shares, my arithmetic).
        - The deal premium is much larger. $18.50 is $3.32 above the $15.18 unaffected price (my arithmetic), a 22% premium (`facts.premium-over-unaffected`), about $569.7M across 171.6M shares (my arithmetic). The financing lever explains about one-sixth of it (0.52 ÷ 3.32). The rest is not control value from better management as we measure it. Our status-quo value, $13.00, is below even the unaffected price.
        - Who controls: Silver Lake (36.56%) and Thoma Bravo (29.79%) together held 66.35% at the 2024 proxy (`governance.controlling_holders`); at signing the two held 111,564,519 shares, about 65% of votes (`facts.sponsor-voting-power-2025-02`). The stockholders' agreement gave each a consent right over a change of control (`governance.marginal_investor`). With governance this concentrated, the lecture's rule says the market price sits near the status-quo value, because public holders cannot force a change.

## Cumulative Project — Questions for This Lesson

- **What is the status quo value of your firm?**
  $13.00 a share, enterprise value $3,444.3M (model-output.md §6). The story and arithmetic are in Part 1 above.

- **If you were running this firm, what would you change about the way the firm is run (in terms of investing, financing and dividend decisions)?**
  Financing first. Debt is 33.03% of capital and the cost-of-capital approach puts the optimum at 21% (model-output.md §3); repay about $468.1M of term loan rather than carry it. The loan floats at SOFR plus 2.75% (`debt.rate_type`), so repaying it lowers exposure to rate rises as well. Dividends second: stop paying out more than free cash flow to equity while debt is above the optimum. In 2024 the company returned $194.7M (the $168.2M special dividend plus $26.5M of shares withheld for taxes) against FCFE of $127.0M, $67.7M more than it generated (model-output.md §5); applied to the loan, that cash would have covered part of the $468.1M. The credit agreement also limits dividends (`debt.covenants`). Investing third: return on capital is below the cost of capital (6.7% against 10.23%), so the plan's growth spending should have to clear the 10% stable return assumed in the DCF. The change is in the bar for new spending, not a stated cut.

- **What is the value of your firm with these changes made?**
  $13.52 a share with the financing change alone (model-output.md §6), against $13.00. The investing and operating changes are not priced: the margin plan is already in the status-quo case, and a higher bar for growth spending cannot be valued without a revised forecast. Value of control from the levers we can measure: $0.52 a share.

- **What is the likelihood that this change will happen?**
  Low for the financing change as run by the existing owners. In 2024 the controlling holders chose a special dividend, not debt repayment, with debt already above the optimum (`facts.special-dividend-2024-per-share`). Their control is concentrated: 66.35% of the shares (`governance.controlling_holders`), so no other holder can force a change, and three of the nine directors are Silver Lake designees (`governance.board`). What did happen is a change of control: on 2025-02-07 the two sponsors consented to sell for $18.50. The buyer's financing runs the other way. Debt commitments are a $2,225M first lien term loan, a $525M second lien and a $200M revolver (`facts.new-debt-2025`). The two term loans alone, $2,750M, are more than double today's $1,285.0M and about 65% of the deal's enterprise value of $4,200.3M (my arithmetic, 2,750 ÷ 4,200.3; deal enterprise value is $18.50 × 171.6M + $1,285.0M − $259.3M, on basic shares and before the equity claim). Sponsors borrow to raise the return on their own equity, not to lower the company's cost of capital, so the optimum in §3 is not their target.

## Notes

The status-quo value ($13.00) is below the $15.18 market price, so by the lecture's logic the market is pricing something between our status quo and a better-run company, or it is pricing the plan's cash flows more generously than we do. The financing lever is real but small ($0.52). The deal premium is not explained by control value of the kind this lesson measures. Lesson 36 returns to what does explain it.

Model note for the report: model-output.md §3 and §6 measure the financing gain on two bases ($144.4M and $89.1M of value). The per-share figure uses §6.
