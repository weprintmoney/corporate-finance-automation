---
title: "Colgate-Palmolive (CL) — Lesson 35: Relative Valuation"
status: active
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL) — Lesson 35: Relative Valuation

### Lesson 35 — Relative Valuation

Where the comparison companies come from. The ledger holds no agreed peer set (`meta.omitted`). This lesson uses the ten companies on Capital IQ's default comparison page for Colgate, with prices as of 2026-11-20 and Capital IQ's standardized figures (`sources/capital-iq/quick-comps.tsv`). It is Capital IQ's list, not one chosen for this project, and we say below which companies belong on it. Every median, implied price and regression is computed by `valuation-cross-checks.py`; its output is section 7 of `valuation-cross-checks-output.md`. Abbreviations: EV is enterprise value, the market value of equity plus net debt; EBITDA is operating income before depreciation and amortization; EBIT is operating income; LTM is the last twelve months and NTM the next twelve, on analysts' forecasts.

- **Lesson 35, Session 35 · Part 1 — "Pricing vs. Valuing: Defining, Describing, Analyzing, and Applying Multiples"** ([transcript](../../04-dividends-and-valuation/lesson-35/session-35-part-1.md))
    - Quote: "You're trying to attach a number to a company based on how similar companies are being priced out there."
    - Question for Colgate-Palmolive: On a consistently defined multiple and peer set, where does Colgate-Palmolive sit relative to its peers: at a premium, a discount, or in line? Which multiple fits this business best, and why?
    - Sources needed: Multiples for Colgate and each comparison company on one definition.
    - Where to find: ledger `facts.peer-multiples-capital-iq`, `facts.peer-medians-and-implied-prices`, `facts.colgate-multiples-capital-iq`; valuation-cross-checks-output.md §7.
    - Answer: At a modest premium to the companies most like it, and a large premium to the full list.

        | Company | EV ÷ revenue | EV ÷ EBITDA | EV ÷ EBIT | Price ÷ NTM earnings | Operating margin |
        |---|---|---|---|---|---|
        | Procter & Gamble | 4.74 | 16.6 | 19.1 | 23.9 | 24.9% |
        | Kimberly-Clark | 4.23 | 19.8 | 24.4 | not comparable | 17.3% |
        | Church & Dwight | 4.50 | 20.2 | 24.2 | 27.8 | 18.6% |
        | Clorox | 2.54 | 14.1 | 17.8 | 18.2 | 14.3% |
        | Reckitt Benckiser | 3.30 | 12.5 | 14.5 | 16.1 | 22.7% |
        | Henkel | 1.72 | 10.8 | 12.4 | 14.9 | 13.9% |
        | Estee Lauder | 2.75 | 16.2 | 23.2 | 28.1 | 11.9% |
        | Coty | 1.15 | 8.5 | 21.9 | 12.7 | 5.2% |
        | General Mills | 1.77 | 9.5 | 11.3 | 11.5 | 15.6% |
        | J. M. Smucker | 2.31 | 9.4 | 12.5 | 13.1 | 18.6% |
        | **Colgate** | **3.99** | **16.8** | **19.3** | **24.7** | **20.7%** |
        | Median, all ten | 2.64 | 13.3 | 18.4 | 16.1 | 16.5% |
        | Median, first six | 3.76 | 15.4 | 18.4 | 18.2 | 18.0% |

      The price ÷ NTM earnings medians leave Kimberly-Clark out, so they cover nine and five companies.
      Colgate's premium over the six household and personal care companies is 10% on EV ÷ EBITDA, 5% on EV ÷ EBIT and 6% on EV ÷ revenue. Over all ten it is 27%, 5% and 51% (`facts.peer-medians-and-implied-prices`). It ranks third of eleven on EV ÷ EBITDA and third on operating margin.
      Consistency. All eleven companies are on one source and one definition, with enterprise value in the numerator wherever an operating figure is in the denominator. Capital IQ's separate multiples page shows Colgate at 16.24 times EBITDA where the comparison page gives 16.85; we did not trace the difference and use the comparison page throughout, so that Colgate is measured the same way as the others (`facts.colgate-multiples-capital-iq`). One company's forward figures are not comparable: Kimberly-Clark's NTM revenue is 90% above its LTM revenue. The files do not say why; a pending merger would produce that pattern. It is left out of the NTM medians.
      The multiple that fits best: EV ÷ EBITDA, with EV ÷ EBIT beside it. The reasons are in the project question below.

- **Lesson 35, Session 35 · Part 2 — "Backing Out What Drives a Multiple: Why Cheap Stocks Usually Deserve to Be Cheap"** ([transcript](../../04-dividends-and-valuation/lesson-35/session-35-part-2.md))
    - Quote: "Most companies that look cheap deserve to be cheap."
    - Question for Colgate-Palmolive: If Colgate-Palmolive looks cheap or expensive against its peers, is that explained by its growth, risk and margins (a regression of the multiple on those drivers), or is there a mispricing left over?
    - Sources needed: Multiples and their drivers across the comparison companies.
    - Where to find: ledger `facts.peer-regression`, `facts.peer-multiples-capital-iq`; valuation-cross-checks-output.md §7.
    - Answer: Colgate looks a little expensive, and its margin explains most of it. The quote's point runs in reverse here: a company that looks dear may deserve to be.
      A revenue multiple should rise with the operating margin, since a company that keeps more of each dollar of sales is worth more per dollar of sales. We fitted a line through the comparison companies, leaving Colgate out, and read off the multiple it predicts at Colgate's margin of 20.66% (`facts.peer-regression`):

        | Companies in the fit | R-squared | Predicted EV ÷ revenue | Colgate's actual | Actual above predicted | Price implied |
        |---|---|---|---|---|---|
        | All ten | 0.55 | 3.63 | 3.99 | 10% | $89.08 |
        | Six household and personal care | 0.49 | 3.89 | 3.99 | 3% | $96.09 |
        | Nine, without Procter & Gamble | 0.41 | 3.48 | 3.99 | 15% | $85.03 |

      After allowing for margin, Colgate trades 3% to 15% above the line. With six to ten companies, that is inside the noise: the standard error of each prediction is about $25 a share. So the fair reading is that Colgate is priced in line with its peers once its margin is counted, or slightly above.
      Growth does not explain the rest. Colgate's expected revenue growth for the next twelve months, 2.25%, is below the nine-company median of 3.1%, and a regression of EV ÷ EBITDA on growth has an R-squared of only 0.22. Risk we could not test: the comparison page carries no betas, and the peer set is not in the ledger for the model to use.
      These regressions are rough. One company, Procter & Gamble, the largest and most profitable, moves the line, which is why the table shows the fit without it.

## Cumulative Project — Questions for This Lesson

- **What multiples of earnings, book value and revenue does your company trade at?**
  On Capital IQ's figures at the 2026-11-20 close (`facts.peer-multiples-capital-iq`, `facts.colgate-multiples-capital-iq`), and on the ledger's 2025 figures (model-output.md §7):

  | Multiple | Capital IQ, last twelve months | Ledger, 2025 |
  |---|---|---|
  | EV ÷ revenue | 3.99 | 4.18 |
  | EV ÷ EBITDA | 16.85 | 17.54 |
  | EV ÷ EBIT | 19.31 | |
  | Price ÷ earnings, as reported | 38.55 | 36.80 |
  | Price ÷ earnings, write-down added back | | 26.8 |
  | Price ÷ earnings, next twelve months | 24.71 | |
  | Price ÷ book value | 272.45 | 1,453 |

  The two columns differ because the ledger uses 2025 figures, debt at fair value with leases, and operating income with restructuring left in, where Capital IQ uses the last twelve months and its own standardized income. Against its own recent past Colgate is at the top of its range: its quarter-end EV ÷ EBITDA ran from 14.21 to 16.05 between June 2025 and September 2026, and is 16.24 now (`facts.colgate-multiples-capital-iq`).

- **Which of these multiples is the best one to price your company on?**
  EV ÷ EBITDA, checked against EV ÷ EBIT and price ÷ NTM earnings. By elimination:
    - Price to book is meaningless. Buybacks have run book equity down to $54M, about $0.07 a share, so the multiple is in the hundreds or thousands.
    - Price to trailing earnings is distorted. Colgate's last twelve months carry the $919M write-down; two of the ten comparison companies have losses and a third trades at 98.5 times depressed earnings.
    - EV to revenue ignores margins, which run from 5.2% to 24.9% across the list. It is useful only with the margin regression above.
    - EV multiples fit better than equity multiples because debt differs widely across the list (`facts.peer-leverage-capital-iq`), and an enterprise multiple is not moved by how a company is financed.
    - Between EBITDA and EBIT there is little to choose for businesses this similar. EBITDA is less affected by how each company amortizes what it has acquired. We show both.

- **What are the "comparable" firms that you would use in pricing your company?**
  Capital IQ's ten, sorted by how well each fits. This is a judgment about someone else's list, not a peer set we built.

  | Company | Belongs? | Why |
  |---|---|---|
  | Procter & Gamble | Yes | The closest: oral care, personal care and home care, sold worldwide through the same stores. Five times Colgate's size |
  | Church & Dwight | Yes | Household and personal care staples, including toothpaste. Smaller and mostly US |
  | Kimberly-Clark | Yes, for trailing figures only | Tissue and personal care staples. Its forward figures are distorted |
  | Clorox | Yes | Household cleaning staples. Mostly US, lower margin |
  | Reckitt Benckiser | Yes | Health and hygiene staples, worldwide. Listed in London; its latest figures were filed in July 2026, earlier than the others' |
  | Henkel | Partly | Laundry and home care fit; its adhesives business does not. Latest figures filed in August 2026 |
  | Estee Lauder | No | Prestige beauty: a luxury purchase that swings with the economy, not a staple |
  | Coty | No | Fragrance and cosmetics, heavily indebted, a $3.95 share with losses |
  | General Mills | Only for Hill's | Packaged food. We benchmarked Hill's pet food to food processing (lesson 10); our files do not show how much of General Mills is pet food |
  | J. M. Smucker | Only for Hill's | Same reasoning |

  We price Colgate on the first six, and show all ten beside them. A better set would weight the six household companies at about 77% and food companies at about 23%, to match Colgate's sales, and would add pet food makers. The files to do that are not in the folder. The ledger's `peers` block stays empty, so `model-output.md` section 7 shows no peer medians.
  For context only, Professor Damodaran's averages for 93 US household products firms in January 2024, two years before our date: EV ÷ EBITDA 15.95, EV ÷ EBIT 20.01, forward price ÷ earnings 31.41 (`facts.sector-multiples-2024`). Colgate at 16.85 and 19.31 is close to those.

- **Based upon the multiple and comparables, what price would you attach to your company?**
  About $89 a share, in a range of roughly $73 to $94 (`facts.peer-medians-and-implied-prices`).

  | Multiple | Median of the six | Price implied | Median of all ten | Price implied |
  |---|---|---|---|---|
  | EV ÷ EBITDA | 15.35 | $89.23 | 13.30 | $76.25 |
  | EV ÷ EBIT | 18.41 | $93.75 | 18.41 | $93.75 |
  | Price ÷ NTM earnings, Kimberly-Clark left out | 18.21 | $72.67 | 16.10 | $64.25 |
  | EV ÷ revenue, adjusted for margin (regression) | | $96.09 | | $89.08 |

  The method for the EV rows: multiply the median by Colgate's own figure, subtract net debt of $6,104M and minority interests of $352M, divide by 794.9 million shares. For EBITDA on the six: 15.35 × $5,041M, less $6,456M, over 794.9 million, is $89.23.
  Our pricing is $89.23, the EV ÷ EBITDA figure on the six household companies. The price today is $98.71, about 10% higher. That premium is roughly what Colgate's higher margin justifies. On pricing, then, Colgate is fairly priced to slightly dear.

## Notes

The one-line descriptions of what each comparison company sells are general knowledge, not drawn from files in `sources/`; the numbers are all from the Capital IQ page.

Pricing and value disagree, and both answers stand.

| | Per share |
|---|---|
| Intrinsic value, base case | $61.83 |
| Intrinsic value, range of cases | $50.90 to $79.74 |
| Pricing against the six household companies | $89.23, range $72.67 to $93.75 |
| Market price | $98.71 |
| Analysts' mean target | $101.70 |

The market is pricing Colgate about the way it prices Procter & Gamble and Church & Dwight. Our valuation says Colgate is worth a little under two-thirds of that price. If both are right, the conclusion is that the whole group of branded staples is priced above what its cash flows support on our assumptions, not that Colgate alone is out of line. That is consistent with lesson 32: the price makes sense only if high returns and growth near the riskfree rate last forever, and investors appear to believe exactly that of the whole sector. We have not valued the peers, so we cannot confirm it for them; we state it as the reading that fits both results.
What this means for an investor: the shares are not a bargain on any measure we have. A pricing-based investor sees a fairly priced stock. A value-based investor sees one priced well above value. Neither sees it as cheap.

Confidence: moderate on the multiples themselves, which are Capital IQ's standardized figures as of one date. Low to moderate on the price of $89: the peer list is not ours, two companies' latest figures are a quarter older than the rest, forward figures for one are unusable, and the regressions rest on six to ten points.

Still open from lesson 28: the comparison page carries no dividend data, so the company-by-company payout check promised there has not been done.
