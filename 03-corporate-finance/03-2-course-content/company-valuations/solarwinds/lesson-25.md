---
title: "SolarWinds (SWI) — Lesson 25: Three Schools of Thought on Dividends"
status: active
owner: weprintmoney
created: 2026-10-25
last_updated: 2026-10-25
---

# SolarWinds (SWI) — Lesson 25: Three Schools of Thought on Dividends

### Lesson 25 — Three Schools of Thought on Dividends

- **Lesson 25, Session 25 · Part 1 — "Three Schools of Thought on Dividends and the Ex-Dividend Day as a Tax-Preference Test"** ([transcript](../../03-financing-mix-and-dividends/lesson-25/session-25-part-1.md))
    - Quote: "The more the tax rates diverge, the more dividends will matter."
    - Question for SolarWinds: Who holds SolarWinds' shares, what are their tax preferences, and which school of thought on dividends applies? If the company has paid dividends, what does the ex-dividend price behaviour say about the marginal investor?
    - Sources needed: Ownership; the sponsors' tax status; prices on the days around the 2021 and 2024 ex-dividend dates.
    - Where to find: `governance.controlling_holders`, `governance.marginal_investor`; `sources/filings/swi-def14a-2024.md` (beneficial ownership); `sources/filings/swi-10k-fy2024.md` Item 5 (holders of record); `company.history`.
    - Answer: The ex-dividend test cannot be run, and the sponsors' tax status is not in the files, so the answer is a reasoned lean, not a measurement.
        - Holders: Silver Lake 36.56% and Thoma Bravo 29.79% (`governance.controlling_holders`), together about 66%. They are separate holders and each had to consent to a change of control. The rest, about 34%, is public float held by diversified institutions, which set the traded price (`governance.marginal_investor`). There were 33 holders of record on 2025-02-13 (facts.holders-of-record), and 39 a year earlier; most shares sit with brokers, so these counts understate the true number.
        - Tax preferences: the filings say nothing about the sponsors' funds or their investors, and a fund's investors may be taxable, tax-exempt or foreign. No source says they were largely tax-exempt, so no such assumption is used. For the float, nothing in the files shows a preference either way.
        - Schools: for the controlling holders, who could extract cash without selling, the neutral school is the closest fit (the same total return whether it arrives as dividend or gain). The bad-for-taxes school would only matter if the dividend was taxed more heavily than a sale for them or for the float; unknown. The clientele school (investors who want dividends) has no support: there was no regular dividend to attract anyone.
        - Ex-dividend behaviour: the record dates are 2021-08-09 and 2024-04-03, and the test needs the price just before and just after each ex-date. The ticker is delisted and no price history was obtainable (`meta.omitted`), so the test is not run. The 2021 date would be unreadable anyway: it fell weeks after the N-able spin-off and the 2:1 reverse split.

- **Lesson 25, Session 25 · Part 2 — "Bad Reasons vs. Good Reasons to Pay Dividends: Clientele, Signaling, and Wealth Transfer From Bondholders"** ([transcript](../../03-financing-mix-and-dividends/lesson-25/session-25-part-2.md))
    - Quote: "When you pay a dividend, you might be transferring wealth from the bondholders or lenders to the equity investors."
    - Question for SolarWinds: What are SolarWinds' actual reasons for its payout policy (a clientele, signalling, lender restrictions, controlling-holder preference, habit), and are they good ones? Would a change in payout signal something the company does not intend?
    - Sources needed: Stated reasons; covenants on dividends; who benefited.
    - Where to find: `debt.covenants`; `sources/filings/swi-10k-fy2023.md` and `swi-10k-fy2024.md` Item 5 and note 9; `company.history`; `governance.*`.
    - Answer: The filings state a process, not a reason. Item 5 says any dividend "will be made at the discretion of our board of directors and will depend on a number of factors, including our financial condition, results of operations, our level of indebtedness and restrictions imposed by our credit agreement". Against the lecture's list:
        - Clientele: not a reason. No regular dividend, 33 holders of record.
        - Signalling: avoided. Both payments were called special and one-time; the 2021 one was tied to the N-able separation, so it was labelled as a result of the spin-off.
        - Lender restrictions: the credit agreement restricts dividends and buybacks "subject to certain exceptions" (note 9). The one financial test springs only when the revolver is more than 35% drawn, and the revolver was undrawn (`debt.covenants`, `debt.revolver_undrawn`). In practice the restriction did not stop $168.2M in 2024. Lenders did not lose protection, but the debt stayed at about $1.24 billion, so the transfer of value to equity was real: in the lecture's terms, cash left that could have repaid debt. The lenders cut the margin to SOFR plus 2.75% in the same year (`debt.covenants`, amendments 7 and 8), which is consistent with lenders who were not alarmed.
        - Controlling-holder preference: the strongest candidate, and the files give no direct statement of it. The board declared the 2024 dividend on 2024-03-15; the sponsors held about two-thirds of the shares and took about two-thirds of the cash (66.35% × $168.2M = $111.6M, assuming their stake was unchanged from the proxy date). Inference, not a disclosed motive.
        - Habit: no, with two payments in five years.
        - Were they good reasons? The 2024 payment is hard to defend on the lecture's tests: debt was $468.1M above the optimum (model-output.md §3), the return on invested capital was below the cost of capital (lesson 22), and cash returned of $194.7M exceeded free cash flow to equity of $127.0M (model-output.md §5). Cash going out is right when investments earn less than the cost of capital, but here debt reduction was available and was worth more (lesson 22).
        - Signal: a regular dividend would signal that the subscription transition was done and growth had slowed, which is how bidders in 2023 read the company ("the relative early stage of the Company's ongoing transition to a subscription-first business model" was the stated reason three bidders withdrew). Another special dividend would signal little; a regular one would signal something the company did not intend.

## Cumulative Project — Questions for This Lesson

- **What does the trade off on dividends look like for your firm? (What are the benefits of paying more dividends? What are the costs of paying more dividends?)**
  Benefits: the return on invested capital is 6.66% against a 10.23% cost of capital (lesson 22), so cash kept inside is not earning its cost; the controlling holders can use cash directly. Costs: debt is $468.1M above the optimum, so a dollar paid out is a dollar not repaying 7.11% debt; the credit agreement restricts payments and the 2024 payout already exceeded free cash flow to equity by $67.7M (model-output.md §5); a regular dividend would send the wrong signal during the subscription transition. Tax costs to the holders are unknown.

- **Given that trade off, do you think that your company should be paying high, low or no dividends?**
  No regular dividend, and no special dividend until debt is near the 21% optimum. The cash should repay debt first (lesson 22's path). Once the ratio is near optimum and projects still earn less than 10.23%, return the excess, by special dividend rather than a regular one, so the payout carries no growth signal.

## Notes

Lesson 25 shows the 2024 special dividend was inconsistent with lesson 22: it paid out cash while debt sat above the optimum. Two points could not be settled from the files: the sponsors' tax position and ex-dividend price behaviour. Lesson 26 tests what the company could afford to pay; lesson 27 sets the full policy.
