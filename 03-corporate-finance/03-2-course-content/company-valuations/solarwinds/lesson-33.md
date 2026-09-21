---
title: "SolarWinds (SWI) — Lesson 33: Firm-to-Equity Bridge"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-21
---

# SolarWinds (SWI) — Lesson 33: Firm-to-Equity Bridge

### Lesson 33 — Firm-to-Equity Bridge

- **Lesson 33, Session 33 · Part 1 — "From Firm Value to Equity Value: Discounting Cash, Premiuming Cash, and Valuing Cross-Holdings"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-1.md))
    - Quote: "A dollar in cash is valued at about 69 cents. That's a 31% discount."
    - Question for SWI: Given SWI's ROIC-vs-WACC track record and the fact the market ultimately accepted a going-private sale at $18.50/share, does SWI's cash sit closer to the "neutral" (ROIC≈WACC) bucket or the "discounted" (bad-projects, market doesn't trust the cash) bucket — and would that partly explain why a going-private discount was acceptable to public shareholders rather than a fight for a higher price?
    - Sources needed: SWI's ROIC vs. WACC track record 2021–2024, cash balance size, and any market commentary on cash-balance discounting ahead of the deal.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024 balance sheet (cash position); REPO-SWI-VAL (WACC built at Step 12; ROIC not yet computed there); DEAL-DOCS (fairness opinion may discuss treatment of cash in its own DCF); NEWS-WEB (pre-deal market commentary on SWI's cash use).
    - Answer: Theoretically the discounted bucket, practically irrelevant — and cash discounting is not why shareholders took $18.50. SWI held $251.85M of cash plus $7.47M of short-term investments at 2024 year-end (`swi-10k-fy2024.md`), which is 7.6% of the $3,422.9M equity value at $18.50 and 5.9% of the $4,370.2M enterprise value; with ROIC at 6.7% against a 10.33% WACC the theory says haircut it, but even Damodaran's full 31% discount is worth only $80.4M, or **$0.43 per share**. Management behaved as if it agreed the cash was untrusted by paying $168.2M of it out as the April 2024 special dividend instead of reinvesting. Neither fairness opinion applied any discount — Goldman explicitly "added the amount of SolarWinds' cash and cash-equivalents and short-term investments" and Jefferies subtracted "net debt" at face (`swi-defm14c-2025-merger-information-statement.md`). The real reason the float didn't fight is governance mechanics: thirteen Thoma Bravo and Silver Lake vehicles holding 111,564,519 shares — ~65% of voting power — signed a written consent under DGCL §228 on 2025-02-07, the same day the agreement was signed, leaving minority holders with appraisal rights and no vote.

- **Lesson 33, Session 33 · Part 2 — "Cross-Holding Shortcuts, Other Assets, and Equity Options as a Second Claim on Equity"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-2.md))
    - Quote: "You have to net out the value of that second claim if you want the value per share as a common stockholder."
    - Question for SWI: How large was SWI's outstanding equity option/RSU overhang in FY2024, and using the lecture's prescribed method (value equity first, subtract options valued as options via an option-pricing model, then divide by actual — not diluted — shares), how much does per-share intrinsic value change versus a naive diluted-share-count treasury-stock-method treatment?
    - Sources needed: SWI's FY2024 outstanding stock options/RSUs, exercise prices, remaining contractual life, and the diluted share count used in reported EPS.
    - Where to find: SEC-EDGAR — SWI 10-K FY2024, Item 8 stock-based-compensation footnote, plus DEF 14A proxy (equity grant detail); REPO-SWI-VAL (no equity-bridge or options work exists there yet).
    - Answer: The overhang is 7.2% of shares, and the naive diluted treatment overstates value by $1.00/share (5.1%). At 2024 year-end SWI had 12,214,062 units outstanding under the 2018 Plan — 9,960,353 RSUs (weighted-average grant fair value $10.86, 1.3 years remaining, $141.9M intrinsic) and 2,253,709 PSUs ($10.05, 0.7 years, $32.1M intrinsic) — plus just 113,430 fully-exercisable options at a $0.98 weighted-average exercise price with 2.6 years left and $1.5M of intrinsic value, against 171,566,604 shares outstanding: 12,327,492 units, or 7.19% (`swi-10k-fy2024.md` Note 10; the merger agreement's Capitalization Date schedule in `swi-defm14c-2025-merger-information-statement.md` confirms 113,430 options at $0.98, 9,869,552 time-vesting RSUs, 1,068,068 earned PSUs and 2,371,282 unearned PSUs at maximum). Applying the lecture's method to my $3,408.8M DCF equity value: the options are so deep in the money that option value collapses to intrinsic value, 113,430 × ($18.50 − $0.98) = **$2.0M**, leaving $3,406.8M over 183,780,666 real-plus-restricted shares = **$18.54/share**. The naive route — dividing by the 174,491K diluted count behind the reported $0.64 diluted EPS — gives $19.54, because the treasury-stock method drops unvested service-condition RSUs entirely. Here the option-pricing refinement is worth $0.01/share and the share-count definition is worth a dollar; that is the practical lesson.

## Cumulative Project — Questions for This Lesson

- **How much cash does your firm have? Would you attach a discount or premium to it?**
  $251.85M of cash plus $7.47M of short-term investments at FY2024 year-end (established above). As established above, theory says discount it (ROIC 6.7% against a 10.33% WACC puts SWI in the "market doesn't trust the cash" bucket), but the discount is immaterial in dollar terms — even Damodaran's full 31% haircut is worth only $0.43/share — and neither fairness opinion actually applied one; both added cash back at face value. Management's own behavior (paying $168.2M of it out as a special dividend rather than reinvesting) is the more informative signal than any formal discount.

- **Does your firm have minority cross holdings? What is their value?**
  None are disclosed anywhere in the compiled sources — no equity-method investment or minority-stake line appears on SWI's balance sheet in any of the FY2018, FY2020, FY2023, or FY2024 10-Ks reviewed across this project. This question doesn't apply to SWI.

- **Does your firm have majority cross holdings? How have you incorporated their value?**
  Also none currently. SWI's one historical majority holding — N-able, Inc. — was fully separated via a spin-off completed in 2021 (established in Lessons 8, 16, 26), not retained as a consolidated majority stake, and SWI shows no non-controlling-interest line in any reviewed balance sheet. This question doesn't apply post-separation.

- **Have managers in the firm been compensated with equity options or restricted stock? How does that affect your value per share?**
  Yes, extensively — as established above, 12,327,492 RSU/PSU/option units were outstanding at FY2024 year-end against 171,566,604 shares (a 7.19% overhang), and the golden-parachute disclosure (established in Lesson 2 Part 2) shows RSU acceleration is 88.4% of the executive change-of-control payout, scaling one-for-one with deal price. Applying the lecture's prescribed method (value equity, subtract options at their option/intrinsic value, divide by actual-plus-restricted rather than diluted shares) — established above — gives $18.54/share on a $3,408.8M DCF equity value, versus $19.54/share using the naive diluted-share treasury-stock-method count. The $1.00/share (5.1%) difference is entirely a share-count-definition effect, since the options themselves are so deep in the money that their option value collapses to intrinsic value regardless of method.

## Notes

Lesson 33 covers the firm-to-equity bridge: how to treat cash (trust it at face, discount it, or premium it) and how to net out options as a second claim on equity rather than diluting naively. For SWI, both bridge steps turn out to be small relative to the questions this project keeps returning to — a full cash discount is worth only $0.43/share, and the options-versus-diluted-shares refinement is worth about $1.00/share — but Part 1's answer surfaces the real reason the float accepted the price: not cash discounting, but a same-day written consent under DGCL §228 that left minority holders with appraisal rights and no vote at all. That governance-mechanics point connects directly back to Lesson 2 Part 3's minority-protection finding and forward to Lesson 34's "value of control" analysis, which treats the deal premium as governance-discount recapture rather than an operating story. This lesson's equity-value and share-count outputs feed straight into Lesson 34's completed per-share DCF.
