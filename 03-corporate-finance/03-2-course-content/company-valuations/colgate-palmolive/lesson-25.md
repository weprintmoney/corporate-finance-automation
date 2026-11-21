---
title: "Colgate-Palmolive (CL) — Lesson 25: The Trade Off"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 25: The Trade Off

### Lesson 25 — The Trade Off

- **Lesson 25, Session 25 · Part 1 — "Three Schools of Thought on Dividends and the Ex-Dividend Day as a Tax-Preference Test"** ([transcript](../../03-financing-mix-and-dividends/lesson-25/session-25-part-1.md))
    - Quote: "The more the tax rates diverge, the more dividends will matter."
    - Question for Colgate-Palmolive: Who holds Colgate-Palmolive's shares, what are their tax preferences, and which school of thought on dividends applies? If the company has paid dividends, what does the ex-dividend price behaviour say about the marginal investor?
    - Sources needed: Ownership by type of holder; daily prices around ex-dividend dates.
    - Where to find: ledger `governance.marginal_investor`, `governance.controlling_holders`, `facts.institutional-ownership`, `facts.holders-capital-iq`, `facts.sector-dividends`. Daily prices are not in `sources/` (the price file is monthly).
    - Answer: Institutions hold 87.19% of the shares; the largest holders are BlackRock, Vanguard and State Street, mostly through index funds (`facts.institutional-ownership`, `facts.holders-capital-iq`). The three schools of thought are: dividends do not matter (what is paid out is offset by a lower share price); dividends are bad (they are taxed more heavily than capital gains); dividends are good (some investors want them and will pay for them). Which applies depends on how the investors who set the price are taxed.
      For Colgate's holders, taxes are close to neutral. Index funds, pension funds and retirement accounts pay little or no tax on dividends as they arrive, and the funds do not choose their stocks on yield. For them the first school holds: a dollar of dividend and a dollar of buyback are worth about the same. The minority of taxable individuals would prefer buybacks, which let them choose when to pay tax. So nothing about the tax position of the holders argues for a high dividend, and nothing argues strongly against one.
      The ex-dividend test (comparing the price drop on the day the dividend detaches with the dividend itself) was not run: it needs daily prices, and our price file is monthly. We leave it out and do not guess the result.
      One comparison is worth noting. Institutional holding in Colgate, 87.19%, is about twice the 42.96% average for household products companies (`facts.sector-dividends`). Colgate's shareholder base is more professional and less tax-sensitive than its industry's.

- **Lesson 25, Session 25 · Part 2 — "Bad Reasons vs. Good Reasons to Pay Dividends: Clientele, Signaling, and Wealth Transfer From Bondholders"** ([transcript](../../03-financing-mix-and-dividends/lesson-25/session-25-part-2.md))
    - Quote: "When you pay a dividend, you might be transferring wealth from the bondholders or lenders to the equity investors."
    - Question for Colgate-Palmolive: What are Colgate-Palmolive's actual reasons for its payout policy (a clientele, signalling, lender restrictions, controlling-holder preference, habit), and are they good ones? Would a change in payout signal something the company does not intend?
    - Sources needed: The company's own statements on returning cash; covenants; ownership; the dividend record.
    - Where to find: ledger `facts.capital-structure-statements`, `facts.payout-policy-2025`, `debt.covenants`, `governance.controlling_holders`, `facts.dividends-2021-2025`, `facts.executive-pay-2025`, `facts.sp-rating-action`.
    - Answer: Colgate's stated reason is brief: "we drive additional value to shareholders by returning cash through dividends and ongoing share repurchases" (`facts.capital-structure-statements`). Reading the record against the lecture's list:

        | Reason | Does it apply to Colgate? | Good reason? |
        |---|---|---|
        | The cash is not needed in the business | Yes. Capital spending is below depreciation and the business throws off more cash than it reinvests (lesson 14) | The best reason there is |
        | Clientele: holders who own it for the dividend | Yes. A dividend raised every year attracts and keeps investors who want exactly that | Good, as long as the dividend is affordable |
        | Signalling | Yes, and it binds. A steady rise says "nothing has changed". A freeze or cut would be read as bad news about the business | A reason to keep it, not to raise it faster |
        | Lender restrictions | No. Covenants exist only on bank borrowings and Colgate complies (`debt.covenants`); the 10-K mentions no covenant on the public notes, and no limit on dividends | Not a constraint |
        | A controlling holder's needs | No. There is none (`governance.controlling_holders`) | Does not apply |
        | Pay incentives | Partly. Bonuses rest on earnings per share (`facts.executive-pay-2025`), and buybacks raise earnings per share by shrinking the share count | A weak reason, and a reason for buybacks, not dividends |

      The wealth-transfer point in the quote is real but small today. Paying cash out leaves lenders with less cushion. With coverage of 15.82 times, lenders are not at risk, though S&P's 2024 action, recorded as a downgrade (`facts.sp-rating-action`), came while Colgate was returning more than its net income. Under the path in lesson 22 (borrowing to buy back shares) the transfer would become deliberate and noticeable: existing noteholders would hold lower-rated paper.
      Would a change signal something unintended? A cut or freeze in the dividend, yes. That is why the recommendation in lesson 22 leaves the regular dividend alone and runs through special dividends, which are labelled as one-off and can stop without the market reading a cut into it. Buybacks have the same flexibility, but lesson 22 sets them aside while the price is above the estimated value.

## Cumulative Project — Questions for This Lesson

- **What does the trade off on dividends look like for your firm? (What are the benefits of paying more dividends? What are the costs of paying more dividends?)**
  Benefits of paying more:
    - It moves cash that the business cannot use well out of management's hands. This is the strongest argument for Colgate. Its organic needs are small, and the money it did deploy at scale, $3,894M of acquisitions from 2018 to 2025, was followed by $2,211M of write-downs (`facts.acquisitions-2018-2025`).
    - It serves the investors who hold Colgate for income and steadiness.
    - It tells the market that management expects cash flows to hold up.
  Costs of paying more:
    - A regular dividend is a promise. Dividends paid are already 85.51% of 2025 net income, 62.3% before the write-down (`facts.dividends-2021-2025`). Raising the regular dividend faster than earnings grow builds a commitment that would be painful to break; operating income before write-downs has grown 0.7% a year for a decade (`facts.growth-and-margin-history`).
    - Taxable holders pay tax on receipt, where a buyback would let them defer it. For Colgate's mostly institutional base this cost is small.
    - Less financial slack. For Colgate this cost is also small: it has $3,641M of unused credit lines and a business that produces cash every quarter.
  On balance the benefits of returning cash are large and the costs low. The costs attach specifically to the fixed, regular dividend, not to returning cash as such.

- **Given that trade off, do you think that your company should be paying high, low or no dividends?**
  High, and it does. A mature company with a 34.56% return on existing capital, little need to reinvest, steady earnings and a poor acquisition record should return most of what it earns. The form matters more than the level. The regular dividend should stay about where it is, at roughly 60% of earnings before write-downs, and keep rising slowly with earnings. Cash beyond that should go out in a form that carries no promise and can flex with the year. Colgate has used buybacks for that part: $8,731M of dividends and $6,705M of buybacks over five years (`facts.dividends-2021-2025`). While the share price is above the estimated value, special dividends are the better route for it; buybacks become the better route only if the price falls to or below value (lesson 22). We would not change the regular dividend. Whether the total returned is right is a question about cash flow, which lesson 26 answers.

## Notes

The trade-off favours a high payout, and Colgate's policy is consistent with it. The reasons are good ones: the cash is not needed, the shareholders expect it, and management's alternative uses for it have a poor record. Confidence is high on the direction. It rests on disclosed facts about ownership, reinvestment and write-downs, not on a model.

Not done: the ex-dividend test, for lack of daily prices. It would tell us the tax position of the marginal investor more directly than the ownership table does, and we expect it would confirm a near-neutral result, but that is an expectation and not a finding.

One link back to lesson 22: the plan to move toward 20% debt leaves the regular dividend alone because of this lesson, and pays the borrowed cash out as special dividends. A dividend raised with borrowed money would have to be held or cut when the borrowing stopped, and a cut is the one signal Colgate cannot afford to send.
