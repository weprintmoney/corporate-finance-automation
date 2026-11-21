---
title: "Colgate-Palmolive (CL) — Lesson 33: To Value Per Share"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 33: To Value Per Share

### Lesson 33 — To Value Per Share

The discounted cash flows give the value of the operating business: $56,717M in the base case. This lesson walks from there to a value per share (`facts.ginzu-base-case-detail`):

| Step | $M | Source of the balance |
|---|---|---|
| Value of operating assets | 56,717 | Lessons 30 to 32 |
| − Debt, with operating leases | 8,282 | 10-Q, 2026-09-30, carrying value; leases carried forward from year end |
| − Minority interests | 352 | 10-Q, book value |
| + Cash and marketable securities | 1,612 | 10-Q |
| + Non-operating assets (cross holdings) | 82 | 10-K, book value |
| Value of equity | 49,777 | |
| − Value of employee options | 439 | Option pricing model in the workbook |
| Value of equity in common stock | 49,338 | |
| ÷ Shares, including restricted and performance units (millions) | 797.9 | 10-Q cover and 10-K Item 12 |
| **Value per share** | **$61.83** | |

- **Lesson 33, Session 33 · Part 1 — "From Firm Value to Equity Value: Discounting Cash, Premiuming Cash, and Valuing Cross-Holdings"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-1.md))
    - Quote: "A dollar in cash is valued at about 69 cents. That's a 31% discount."
    - Question for Colgate-Palmolive: Should Colgate-Palmolive's cash be valued at face, at a discount, or at a premium, judged by its record of returns versus the cost of capital and how it has used cash? Does it hold stakes in other companies, and how are they valued?
    - Sources needed: Cash and where it is held; returns against cost; record on uses of cash; equity-method investments; noncontrolling interests.
    - Where to find: ledger `facts.balances-2026-q3`, `facts.geographic-risk-notes`, `facts.acquisitions-2018-2025`, `facts.fcfe-by-year-2018-2025`, `facts.equity-method-investments`, `facts.minority-interest-estimate`, `facts.ginzu-sensitivities`; model-output.md §8.
    - Answer: At face value. The lecture's discount applies to companies that sit on large cash balances and have a record of wasting them. Colgate's record is mixed, but the balance is too small and too short-lived for a discount to matter.
        - The case for a discount: Colgate's acquisitions have been poor, with write-downs equal to 57% of what it spent on them (`facts.acquisitions-2018-2025`). And almost all the cash sits abroad, $1,234M of $1,288M at the end of 2025 (`facts.geographic-risk-notes`), so some tax could fall due if it were brought home.
        - The case against: the cash is $1,612M, under 3% of the value of the operating business, and Colgate does not let it build up. It returned about what it generated in every recent year, and the balance was lower at the end of 2025 than at the end of 2017 (lesson 26). The existing business earns 34.56% against a cost of 8.34% (model-output.md §8). Cash that is paid out within the year is worth what it says.
        - A premium, for companies with a record of investing cash unusually well, is not warranted either, given the acquisitions.
      What a discount would be worth: 10% off the cash is $0.20 a share (`facts.ginzu-sensitivities`). The choice does not move the answer.
      Stakes in other companies: yes, small ones, both ways round. They are answered in the project questions below.

- **Lesson 33, Session 33 · Part 2 — "Cross-Holding Shortcuts, Other Assets, and Equity Options as a Second Claim on Equity"** ([transcript](../../04-dividends-and-valuation/lesson-33/session-33-part-2.md))
    - Quote: "You have to net out the value of that second claim if you want the value per share as a common stockholder."
    - Question for Colgate-Palmolive: How large are Colgate-Palmolive's outstanding options and restricted stock units, and how much does valuing them as a claim and dividing by basic shares change value per share compared with the diluted-share shortcut?
    - Sources needed: Options outstanding, strike, life, volatility; restricted and performance units; basic and diluted shares.
    - Where to find: ledger `facts.ginzu-inputs`, `company.options_value`, `company.shares_diluted`, `facts.option-remaining-life`, `facts.ginzu-sensitivities`; model-output.md §6.
    - Answer: 12.619 million options at an average exercise price of $79, with four years left on average, and 2.988 million restricted and performance units (`facts.ginzu-inputs`). Together they are about 2% of the 794.9 million shares. Three treatments:

        | Treatment | What it does | Value per share |
        |---|---|---|
        | Course method in the workbook (base case) | Options valued with an option pricing model at $439M and subtracted; units added to the share count (797.9 million) | $61.83 |
        | Course method with the ledger's simpler figure | Options at today's price less the exercise price, units at today's price, $543.6M in all, subtracted; 794.9 million shares | $61.94 |
        | Diluted-share shortcut | Nothing subtracted; divide by 811.1 million diluted shares | $61.37 |

      The shortcut is $0.47 lower here (`facts.ginzu-sensitivities`). The repo model's cross-check shows the same gap on its own figures: $60.85 against $60.31 (model-output.md §6). The shortcut is wrong in principle, because it counts each option as a full share and ignores the cash employees pay to exercise. For Colgate the error is under 1% of value because the grants are small.
      Future grants are a separate matter, and they are already counted: stock-based pay of $155M a year is left in operating expenses (`company.sbc`), so the cash flows are after the cost of the shares Colgate will keep handing to employees.

## Cumulative Project — Questions for This Lesson

- **How much cash does your firm have? Would you attach a discount or premium to it?**
  $1,612M at 2026-09-30: $1,527M of cash and $85M of marketable securities (`facts.balances-2026-q3`). At the end of 2025 it was $1,395M. Neither a discount nor a premium, for the reasons in Part 1: it is small, it is paid out as it arrives, and a 10% discount would change the value by $0.20 a share.

- **Does your firm have minority cross holdings? What is their value?**
  Yes, small ones. Colgate holds stakes of between 20% and 50% in other consumer products companies, carried at $82M at the end of 2025, and they earned it $20M that year (`facts.equity-method-investments`). The valuation adds them at the $82M book figure, about $0.10 a share. The filings we hold do not name them or give a market value, so we cannot value them properly. Their income is not in the operating income we discounted, so adding them is right; the amount is probably low, since stakes earning $20M a year are likely worth more than $82M. Even at several times book the effect is well under a dollar a share.

- **Does your firm have majority cross holdings? How have you incorporated their value?**
  Yes. Colgate consolidates subsidiaries it controls but does not wholly own. All of their sales and operating income are inside the figures we discounted, so the part that belongs to outside shareholders must come back out. The workbook subtracts it at book value: $352M (`facts.balances-2026-q3`).
  We think book value understates this claim, and we flag it as the largest unsettled item in the bridge. Those outside shareholders earned $129M in 2025, $160M in 2024 and $155M in 2023, on a book value of $311M (`facts.minority-interest-estimate`). A claim that earns 41% of its book value in a year is worth much more than book. A rough estimate: their share of 2025 earnings is 4.22%; the same share of the base-case equity value is $2,117M, which is $1,765M more than the workbook subtracts, or $2.21 a share. On that estimate the base case would be $59.62. It is an estimate, resting on the assumption that those subsidiaries deserve the same multiple of earnings as the whole company; the filings we hold do not name them. We leave the base case at $61.83, with book value as the professor's workbook takes it, and quote $59.62 beside it.

- **Have managers in the firm been compensated with equity options or restricted stock? How does that affect your value per share?**
  Yes: 12.619 million options and 2.988 million restricted and performance units (`facts.ginzu-inputs`). The options are valued at $439M and subtracted; the units are counted as shares. Compared with ignoring both and dividing by 794.9 million shares, the effect is a reduction of under a dollar a share. Compared with the diluted-share shortcut, the course method gives $0.47 more.

## Notes

Other items in the bridge, each a choice with its alternative (`facts.ginzu-sensitivities`):

| Item | Base case | Alternative | Effect on $61.83 |
|---|---|---|---|
| Debt | Carrying value, $8,282M with leases | Fair value, $7,554M: the notes carry old, low coupons and trade below face | +$0.91 |
| Pension and retiree-benefit shortfall, $1,283M | Not subtracted, as it was not counted as debt in the cost of capital (lesson 12) | Subtract it after tax, $962M | −$1.21 |
| Minority interests | Book value, $352M | Estimate of $2,117M | −$2.21 |
| Cash | Face value | 10% discount | −$0.20 |

The alternatives lean down more than up. Taking the debt, pension and minority interest alternatives together would put the base case near $59, not $62. None of them changes the conclusion, and all of them are small beside the two assumptions in lesson 32.

How the value per share connects to the debt recommendation. Lessons 19 and 22 recommend moving to 20% debt and paying the borrowed cash out as special dividends, not buybacks. The reason is the number this lesson arrives at. A buyback at $98.71 pays $98.71 for a share worth $61.83, and the difference comes out of the pockets of the shareholders who stay. On the $9,226M that the move to 20% debt requires, the overpayment would be $3,447M, or $4.91 for each share left, more than twice the $2.26 a share the extra debt is worth (`facts.buyback-above-value`). So the position, set out in full in lesson 34, is this: the case for more debt stands, and the cash should go out as special dividends, with the regular dividend left on its existing slow rise, for as long as the price is above the estimated value. Buybacks become the better route only if the price falls to or below value. A dividend pays every holder the same amount per share and moves nothing between them. That is a judgment, and it depends on our valuation being right.

Confidence: high on the amounts, which are read from filings. Moderate on the bridge as a whole, because two items, cross holdings and minority interests, are at book value for want of better information, and we have shown the one that matters.
