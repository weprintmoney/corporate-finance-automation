---
title: "SolarWinds (SWI) — Lesson 33: To Value Per Share"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 33: To Value Per Share

### Lesson 33 — To Value Per Share

- **Lesson 33, Session 33 · Part 1 — "From Firm Value to Equity Value: Discounting Cash, Premiuming Cash, and Valuing Cross-Holdings"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-1.md))
    - Quote: "A dollar in cash is valued at about 69 cents. That's a 31% discount."
    - Question for SolarWinds: Should SolarWinds' cash be valued at face, at a discount, or at a premium, judged by its record of returns versus the cost of capital and how it has used cash? Does it hold stakes in other companies, and how are they valued?
    - Sources needed: Cash and investments; return on capital against cost of capital; how cash was used (debt repaid, dividends); any equity stakes or minority interests.
    - Where to find: `company.cash`, `company.history`, `company.invested_capital`, `debt.revolver_undrawn`; `sources/filings/swi-10k-fy2024.md` balance sheet and notes; model-output.md §1 and §5.
    - Answer: At face value, $259.3M (`company.cash`: cash $251.9M plus short-term investments $7.5M at 2024-12-31).
        - The case for a discount is the return record. 2024 after-tax return on book invested capital was about 6.7% and 2023's about 4.8% (EBIT × (1 − 25%) ÷ `company.invested_capital`, `company.history`, my arithmetic), both below the 10.23% cost of capital (model-output.md §1). A market that expects a firm to earn less than its cost of capital discounts the cash it holds.
        - The case against is how this cash was used. In 2022 the company repaid $664.4M of debt (`company.history`). In 2024 it paid a $168.2M special dividend (`facts.special-dividend-2024-per-share`). Cash ended 2024 at $259.3M, near 2023's $289.2M, so it was not hoarded. A $130.0M revolver is undrawn (`debt.revolver_undrawn`), so no cash needs to sit idle as a liquidity reserve.
        - It is 10% of the $2,604.9M equity value (259.3 ÷ 2,604.9, `company.equity_value`, my arithmetic). A 31% discount, the lecture's example, would remove $80.4M, or $0.47 a share on 171.6M shares (my arithmetic). Small either way.
        - Judgment call: face value. The record argues for a discount; the use of cash (repaying debt, paying it out) argues against, and a discount would also mean marking down what SolarWinds' two advisers counted at face in their fairness analyses (deal document, Goldman Sachs and Jefferies discounted cash flow sections).
        - Stakes in other companies: none (see the project question below).

- **Lesson 33, Session 33 · Part 2 — "Cross-Holding Shortcuts, Other Assets, and Equity Options as a Second Claim on Equity"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-2.md))
    - Quote: "You have to net out the value of that second claim if you want the value per share as a common stockholder."
    - Question for SolarWinds: How large are SolarWinds' outstanding options and restricted stock units, and how much does valuing them as a claim and dividing by basic shares change value per share compared with the diluted-share shortcut?
    - Sources needed: Count of unvested restricted and performance stock units and vested options; share price; basic and diluted share counts.
    - Where to find: `company.options_value`, `company.shares_basic`, `company.shares_diluted`, `company.sbc`; `sources/filings/swi-10k-fy2024.md` note 10; model-output.md §6.
    - Answer: The claim is $187.0M (`company.options_value`): 9,960,353 unvested restricted stock units plus 2,253,709 performance stock units, 12.214M units in all, valued at the $15.18 unaffected price because they carry no exercise price, plus 113,430 vested options at $0.98 valued at intrinsic value. The model subtracts it from equity value and divides by basic shares:
        - Equity value before option claims $2,418.6M − $187.0M = $2,231.6M; ÷ 171.6M basic shares = $13.00 (model-output.md §6).
        - The shortcut, $2,418.6M ÷ 174.5M diluted shares, gives $13.86 (§6). The shortcut is $0.86 higher.
        - Why it is higher: the diluted count adds only 2.9M shares to the basic count (174.5 − 171.6, `company.shares_diluted`, my arithmetic), which is 1.7%. The units outstanding are 12.214M, 7.1% of basic shares. The diluted count is also a weighted average over 2024, not a year-end count, and uses the treasury-stock method, which assumes unvested units are partly offset by the compensation expense still to come.
        - No double counting: stock compensation of $76.5M is expensed in EBIT (`company.sbc`, `modeling_choices.sbc_treatment: expense`), and management's forecast cash flows are after stock compensation (`forecast.years`). Future grants are therefore paid for in the cash flows; the $187.0M covers only grants already made.
        - Circularity: the units are valued at $15.18, not at the $13.00 the DCF produces. At $13.00 the claim would be smaller and value per share slightly higher. We keep the course method.

## Cumulative Project — Questions for This Lesson

- **How much cash does your firm have? Would you attach a discount or premium to it?**
  $259.3M at 2024-12-31 (`company.cash`). No discount or premium; face value (see Part 1 above). The cash is added in the bridge from enterprise value to equity value (model-output.md §6).

- **Does your firm have minority cross holdings? What is their value?**
  No. The FY2024 balance sheet has no equity-method investment and no investment securities beyond the $7.5M of short-term investments already counted in cash (`sources/filings/swi-10k-fy2024.md`). SolarWinds' July 2021 spin-off of N-able was a distribution of N-able shares to SolarWinds shareholders, one N-able share for every two SolarWinds shares (`facts.corporate-actions-2021`); no N-able stake appears on the 2024 balance sheet. Value: $0. The ledger has no `company.cross_holdings` field because there is nothing to put in it.

- **Does your firm have majority cross holdings? How have you incorporated their value?**
  No consolidated subsidiary has outside owners: the 10-K's balance sheet and equity statement show no noncontrolling interest. There is no minority interest to subtract from equity, and nothing to add. The statements are consolidated, so the cash flows in the DCF already include every subsidiary.

- **Have managers in the firm been compensated with equity options or restricted stock? How does that affect your value per share?**
  Yes, mainly restricted and performance stock units. The $187.0M claim lowers equity value, and value per share falls from $13.86 (diluted-share shortcut) to $13.00 (course method), model-output.md §6. Stock compensation was $76.5M in 2024 (`company.sbc`), 9.6% of revenue (76.5 ÷ 796.9, my arithmetic), and is treated as an operating cost. The deal accelerates equity for executives: $19.94M of the CEO's $22.99M change-of-control payout is accelerated equity (`governance.change_of_control_payouts`).

## Notes

Lesson 33 turns the DCF's enterprise value of $3,444.3M into $13.00 a share: less debt of $1,285.0M, plus cash of $259.3M, less the $187.0M equity claim, over 171.6M basic shares (model-output.md §6). Cash is at face; there are no cross holdings or minority interests; the stock-unit claim is the one adjustment that moves the answer ($0.86 against the shortcut). Debt includes leases and excludes deferred revenue and cloud purchase commitments (lesson 12). Lesson 34 uses this bridge for both the status-quo and the optimal value.
