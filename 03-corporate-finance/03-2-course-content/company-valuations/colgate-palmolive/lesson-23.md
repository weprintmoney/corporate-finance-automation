---
title: "Colgate-Palmolive (CL) — Lesson 23: The Right Financing"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 23: The Right Financing

### Lesson 23 — The Right Financing

A caution on the evidence before the answers. This lesson's numbers come from `professor-spreadsheet/macro-sensitivity-output.md`. The professor's sector table uses data from 1987 to 1997. Pet food is not in it, so a neighbouring group (grain mill products) stands in for Hill's. Colgate's own regressions on nine to eleven yearly observations are not statistically significant: no coefficient is as large as 1.3 times its standard error (`facts.macro-sensitivity-own`). The professor's project checklist says that when the numbers are weak the intuitive argument should carry the conclusion. It does here; the numbers are shown as a check on the intuition, not as its source.

- **Lesson 23, Session 23 · Part 1 — "Matching Debt to Assets: The Five Questions That Design the Perfect Financing"** ([transcript](../../03-financing-mix-and-dividends/lesson-23/session-23-part-1.md))
    - Quote: "You'd like to issue debt that behaves like equity, that gives you the flexibility of equity while giving you the tax benefits of debt."
    - Question for Colgate-Palmolive: Given the life, currency, cyclicality and pricing power of Colgate-Palmolive's assets, what should its debt look like in maturity, fixed versus floating, and currency? Does the company have the pricing power that floating-rate debt requires?
    - Sources needed: What the assets are and where; sensitivity of value and income to rates, growth, inflation and currencies.
    - Where to find: ledger `facts.macro-sensitivity-sector`, `facts.macro-sensitivity-own`, `country.exposures`, `facts.segment-results-2025`, `facts.sales-drivers-2025`, `facts.growth-and-margin-history`, `facts.operating-income-stability`.
    - Answer: The idea is to make the debt payments move with the cash flows of the assets, so that when the business has a bad year the debt is lighter too. Question by question.

        | Design question | Intuition | What the numbers say | Conclusion |
        |---|---|---|---|
        | How long-lived are the assets? | Brands that have sold for generations, with cash flows that arrive steadily every year. Long-lived, but not back-loaded | Sector duration 4.78 years (5.05 for personal care, 3.83 for the pet food stand-in). Colgate's own firm value: −5.54 on interest rates, about 5.5 years, standard error 4.87 | Medium to long: an average life of five to ten years, spread across maturities |
        | Are cash flows cyclical? | Staples: people buy toothpaste in recessions | Operating income fell at most 7.4% in a year since 2016. Sector cyclicality 0.96; Colgate's own coefficients on growth are negative and insignificant | Not cyclical. Plain debt with fixed payments is fine; no need for payments that flex |
        | Do cash flows rise with inflation? | Colgate can raise prices (+2.1% in 2025 with volume −0.4%), which would suit floating-rate debt | Not confirmed. Sector inflation coefficient −0.92; Colgate's own 0.04 with a standard error of 2.62. Over ten years sales grew 3.3% a year but operating income 0.7%: prices rose and margins did not keep up | Mostly fixed rate. Pricing power shows in sales, not in profit |
        | What currencies are the cash flows in? | About one-third US, 45% emerging markets, the rest other developed markets | Sector currency coefficient 1.25; Colgate's own on firm value 1.26, standard error 0.98, and −0.44 on operating income. Signs disagree | Mixed currencies, in rough proportion to where the business is |
        | Is growth uncertain enough to want conversion features? | No: slow, predictable growth and large cash flows | | Straight debt. No convertibles |

      On the pricing-power question directly: Colgate has enough to protect sales, and the 10-K names selling price increases among its responses to currency moves. It has not had enough to make profit track inflation. Floating-rate debt pays off when a company's income rises with interest rates. There is no evidence of that here, so floating debt should stay a small share.
      The right debt for Colgate, then: straight, fixed-rate, medium to long in maturity, in a mix of currencies of which the dollar is well under half.

- **Lesson 23, Session 23 · Part 2 — "Fixing Debt/Asset Mismatches: Swaps vs. New-Project Financing"** ([transcript](../../03-financing-mix-and-dividends/lesson-23/session-23-part-2.md))
    - Quote: "There are two ways in which companies can adjust debt that doesn't match."
    - Question for Colgate-Palmolive: Where does Colgate-Palmolive's actual debt mismatch its assets (currency, maturity, rate type)? Is the better fix a swap or a different financing of future projects, and what would it cost?
    - Sources needed: The notes outstanding by maturity, currency and rate type; hedges that change their effective currency.
    - Where to find: ledger `facts.debt-profile-detail`, `facts.euro-debt-share`, `facts.debt-maturity-schedule`, `facts.debt-detail-2025`, `facts.currency-and-hedging-2025`, `debt.rate_type`, `debt.currency`, `facts.cost-of-capital-grid`.
    - Answer: Rate type matches. Maturity is close enough. Currency is the mismatch, and the fix is in how new debt is issued.
        - Rate type: 90.5% fixed, 9.5% floating (`facts.debt-profile-detail`). That is what the analysis asks for.
        - Maturity: the rated notes have a weighted average maturity of 9.6 years, twice the sector's 4.78-year duration. This overstates the gap. Maturity is when principal comes due; duration also counts the interest paid along the way and is shorter, and no duration for the notes is in our files. The schedule is well spread: 42.7% of long-term debt falls due from 2026 to 2030 and 57.3% later, out to 2078 (`facts.debt-profile-detail`). For assets as durable as these, somewhat long debt is the safe side to err on. No fix needed.
        - Currency: 64.1% of rated notes are in dollars and 35.9% in euros. The United States is 32.67% of sales and Europe 14.5%; emerging markets are about 45% and no note in the list is in an emerging-market currency. So the dollar's share of the debt is about twice its share of sales, the euro's more than twice, and nearly half the business has no matching debt. The picture improves once hedges are counted: Colgate designates $3,942M of foreign currency debt, 49.3% of its debt, as a hedge of its investments abroad, and holds $3,535M of currency contracts (`facts.currency-and-hedging-2025`). Which currencies those cover is not disclosed in our files, so we cannot say how much of the emerging-market gap they close.
      The fix. Swapping or refinancing the existing notes is the wrong tool. They carry coupons averaging 2.9% and are worth 5.9% less than face (`facts.debt-cross-checks`); they are cheap funding that Colgate should let run. The lecture's second route fits better: change the mix through new issues. The recommended path in lesson 22 adds $9,226M of debt over five years, more than the $6,869M of rated notes outstanding. If that new debt is issued outside the dollar, in euros and in other currencies where Colgate has assets and deep enough bond markets, the currency mix corrects itself without touching the old notes. For emerging-market currencies where borrowing is expensive or the market is thin, the practical choice is the one Colgate already makes: short forward contracts and local borrowing by subsidiaries. A cost for either route cannot be computed from our files; it would need quotes for swap rates and new-issue spreads by currency.

## Cumulative Project — Questions for This Lesson

- **Given its asset/project characteristics, what is the right type of debt for your firm?**
  Straight (no conversion or other special features), fixed-rate, with an average life of roughly five to ten years spread over many maturities, and in a mix of currencies that follows where the business is: no more than about a third in dollars, the rest in euros and the currencies of its larger foreign markets. The reasons are the intuitive ones in Part 1: long-lived brands, steady non-cyclical cash flows, pricing power that protects sales but not margins, and two-thirds of sales outside the United States.

- **What are the actual debt characteristics?**
  From the 21 rated notes, principal $6,869M (`facts.debt-profile-detail`), and the 10-K debt note (`facts.debt-detail-2025`):

  | Feature | Actual |
  |---|---|
  | Type | Senior notes and medium-term notes; no convertibles; commercial paper of $147M at year end |
  | Rate | 90.5% fixed, 9.5% floating; average coupon 2.9% |
  | Maturity | Weighted average 9.6 years; individual notes from 2026 to 2078 |
  | Currency | 64.1% dollars, 35.9% euros |
  | Hedges | $3,942M of foreign currency debt designated against investments abroad |

- **If there is a mismatch, what is the best way to fix it?**
  The only real mismatch is currency: too much of the debt is in dollars for a company that makes two-thirds of its sales elsewhere, and none of the notes is in an emerging-market currency. Fix it through new borrowing, not swaps: issue the debt needed to reach the 20% target in non-dollar currencies. Leave the existing notes alone. The maturity gap (9.6 years against a sector duration of 4.78) is smaller than it looks and is on the safe side.

## Notes

Colgate's debt is close to what its assets call for in type, rate and maturity, and off in currency. Confidence is moderate, and lower than for most lessons, for three stated reasons: the sector estimates are about thirty years old, the stand-in for pet food is a different industry, and Colgate's own regressions cannot tell any coefficient from zero. The conclusions rest on what the business is, which is well documented, and the regressions do not contradict them.

Two gaps in the data, both stated above: the duration of the notes (we have maturity only), and the currencies behind the $3,942M of hedging debt. Either could shrink the mismatch we describe. Neither would reverse the advice on new debt.

This closes the financing module. Summary for the report: 9.34% debt today, 30% unconstrained optimum, 20% recommended, reached over five years through special dividends funded with new fixed-rate debt issued mostly outside the dollar.
