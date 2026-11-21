---
title: "Colgate-Palmolive (CL) — Corporate Finance Final Project"
status: draft
owner: weprintmoney
created: 2026-11-21
last_updated: 2026-11-21
---

# Colgate-Palmolive (CL): Corporate Finance Assessment and Valuation

Prices and market data are as of 2026-11-20. Company figures come from the 2025 annual report (10-K), the 10-Q for the quarter to 2026-09-30 and the 2026 proxy statement. Amounts are in US dollars.

## Verdict

Colgate-Palmolive is an excellent business priced as if it were better than any business can be for long. It sells toothpaste, soap, cleaners and Hill's pet food worldwide: $20,382 million of sales in 2025, growing about 3% a year, mostly through price, two-thirds of it outside the United States.

| | |
|---|---|
| Value per share, base case | $61.83 |
| Value per share, the spreadsheet's defaults / its default growth | $50.90 / $79.74 |
| Market price, 2026-11-20 | $98.71 |
| Price implied by six comparable companies' multiples | $89.23 |
| Cost of capital | 8.34% |
| Return on invested capital, 2025 | 34.56% |
| Debt ratio: actual / unconstrained optimum / recommended | 9.34% / 30% / 20% |
| Cash returned, 2021–2025, as a share of free cash flow to equity | About 105%, once employee option cash is counted |

- **Does well:** its existing brands earn about four times what their capital costs, and it pays out the cash it cannot use.
- **Does poorly:** it has written off $2,211 million of the $3,894 million it spent buying businesses since 2018, and it borrows far less than it safely could.
- **Should change:** borrow up to 20% of value over about five years, pay the borrowed cash, and the money now spent on buybacks, out as special dividends while the price is above value, and stop buying businesses that cannot clear the cost of capital.

I am confident about the direction of every finding and less confident about the size of each. The shares look overpriced in my base case and in most of the cases I tested. The exception is the beta: if the low betas of Colgate and its large peers last forever, the price is close to fair (sections 2 and 9).

## 1. Stockholder analysis: who has the power?

**Nobody controls Colgate. Power sits with management, checked by a board that shareholders could replace but have no reason to organize against.**

The three largest holders are Vanguard (10.26%), BlackRock (8.18%) and State Street (5.95%). All three mainly run index funds, which hold every large company and cannot sell when they disagree. Institutions own 87.19% of the shares across 2,356 holders. Directors and officers own 0.43%. The largest holder that Capital IQ tags as an activist, meaning an investor who buys a stake to force change, owns 0.05%.

The formal rights are strong: annual elections for every director, one vote per share, a special-meeting right at 15%, and no poison pill (a device that makes a hostile takeover ruinously expensive). Nine of ten board nominees are independent. The tenth, Noel Wallace, is both chief executive and chairman; a proposal to split the roles is on the 2026 ballot, and the board opposes it. His change-of-control payment, about $45.3 million, is 0.06% of the equity's value, too small to sway a sale.

**The conflict that matters is quiet and sits in the pay plan.** Eighty percent of the annual bonus rests on earnings per share before special items and on organic sales growth, meaning growth with currency moves and acquisitions stripped out. Nothing in it measures the return on money spent buying companies, which is where value was lost, and the pay committee took the $919 million 2025 write-down out of its cash flow measure. That loss cost shareholders, not management's bonus. The plan also rewards buybacks, because they lift earnings per share. That matters in section 8.

Because the marginal investor, the one whose trades set the price, is a diversified institution, risk should be measured as exposure to the market. That is what a beta does.

## 2. Risk and return: how risky is Colgate, and what is its hurdle rate?

**Money costs Colgate 8.34% a year.** That is the cost of capital: the blended return that shareholders and lenders require, and the hurdle any new investment has to clear.

| Input | Value | Basis |
|---|---|---|
| Riskfree rate | 4.82% | 10-year Treasury yield of 5.04% on 2026-11-19, less the 0.22% default spread Damodaran assigns the US |
| Equity risk premium | 5.38% | The extra return investors want for owning stocks. A mature-market premium of 3.61%, plus country risk premiums weighted by where Colgate sells: 33% United States, 45% emerging markets, 22% other developed markets |
| Unlevered beta | 0.68 | Household Products (0.74) for the 77% of sales in oral, personal and home care; Food Processing (0.47) for the 23% in Hill's |
| Levered beta | 0.73 | Adjusted for Colgate's debt |
| Cost of equity | 8.76% | 4.82% + 0.73 × 5.38% |
| Cost of debt, before / after tax | 5.74% / 4.30% | Riskfree rate plus the spread for S&P's A+ rating; 25% marginal tax rate |
| Debt ratio, market values | 9.34% | Debt of $8,084 million, including leases, against $78.5 billion of equity |
| **Cost of capital** | **8.34%** | 90.66% × 8.76% + 9.34% × 4.30% |

*Sources: FRED; Damodaran's January 2026 industry betas, country risk and ratings spread tables and his November 2026 implied premium; Colgate 10-K (note 14 for the sales split, note 7 for debt); S&P rating via S&P Capital IQ.*

**The beta is the weakest input, and the evidence pulls two ways.** A beta measures how much a stock moves with the market. I have three readings.

| Reading | Beta | What it rests on |
|---|---|---|
| Colgate's own regression | 0.315 | Sixty monthly returns against the S&P 500; standard error 0.158, R-squared 0.064 |
| Six large household peers | about 0.41 | Median of S&P Capital IQ's five-year betas, which run from 0.28 to 0.58 |
| Industry average (used) | 0.73 | Damodaran's averages for 110 household products companies and 78 food processors, adjusted for Colgate's debt |

All three come from the same recent years; Damodaran's table is built from two and five years of weekly returns. So the gap is not about the period. It is about which companies are averaged. The industry tables include many small companies, and the two readings closest to Colgate, its own history and its six largest peers, agree on 0.3 to 0.4.

I kept 0.73 for the base case for three reasons. It is the course's method, and an average over 188 companies is far more precise than one regression with a standard error of 0.158 or a median of six. A beta near 0.3 gives a cost of equity of 6.51%, less than a point above the 5.74% at which Colgate borrows, and shareholders are paid after lenders. And from December 2020 to 2026-11-20 the index returned 100.0% and Colgate 33.0%, most of it in 2026, so the low figures record a market driven by other sectors as much as they record safety.

But the peer evidence says 0.73 is probably too high for the world's largest toothpaste maker. The honest range is 0.41 to 0.80, a cost of capital of 6.77% to 8.67%. Section 9 shows what each end does to value, and the low end matters.

[Exhibit: Colgate's total return against the S&P 500, 2021–2026]

**The two businesses deserve different hurdle rates:** 8.67% for Oral, Personal and Home Care and 7.24% for Hill's. One company rate of 8.34% sets the bar too low for the riskier business, and the purchase that failed worst, the Filorga skin care brand, sat at its riskiest end.

| Judgment call | Choice and reason | Alternative, and what it changes | Confidence |
|---|---|---|---|
| Beta | Industry average 0.73: the course's method and the most precise estimate | Large-peer median 0.41: cost of capital 6.77%, value $68.32 if it fades to the mature rate and about $91.88 if it lasts forever | Low. This is the input most likely to be wrong |
| Hill's comparison industry | Food Processing: Hill's makes packaged food, and the dataset has no pet food industry | Household Products for the whole company: cost of capital 8.67% | Moderate |
| Date of the risk premium | Damodaran's published start-of-November premium, 3.61% | The S&P 500 fell 8.8% after that date. A premium recomputed for 2026-11-20 would be near 3.96%, a cost of capital near 8.57% | Moderate. If anything, 8.34% is low, which would lower value further |
| US country risk | US sales priced at the mature premium, with nothing added | The other two readings of Damodaran's tables give 5.23% or 5.45%, about 0.1 point of cost of equity | High that it does not matter |
| Cost of debt | S&P's actual A+ rating, 5.74% | The rating implied by interest coverage, AAA, at 5.44%. Debt is so small that this moves the cost of capital by hundredths | High |

## 3. Investments: how good are Colgate's existing investments?

**The existing business is excellent. The acquisitions are not.**

Return on invested capital (ROIC), after-tax operating income divided by the capital tied up in the business, was 34.56% in 2025 against a cost of capital of 8.34%, after 30.95% in 2023 and 37.53% in 2024. The excess is worth about $2.4 billion a year. Invested capital would have to be 4.1 times larger for the return to fall to the cost of capital.

Colgate makes three kinds of investment, with very different records.

- **Brand support.** Advertising was $2,703 million in 2025, 13.3% of sales. Because it is expensed, it never appears as capital, which is part of why the return looks so high. It is also the real source of that return.
- **Plant and equipment.** Capital spending was $564 million, slightly below depreciation. Modest, steady and well rewarded.
- **Acquisitions.** Colgate spent $3,894 million buying businesses from 2018 to 2025 and wrote down $2,211 million over the same years: $571 million in 2021, $721 million in 2022 and $919 million in 2025. A write-down admits that a purchase is worth less than was paid. The filings tie only the 2025 charge to a named deal, Filorga, so the 57% ratio compares totals rather than proving which deals failed. It still shows that money put to work outside the core has earned poorly.

**Why the returns are high, and whether they last.** The advantage is brand. Shoppers reach for a toothpaste they know, and stores must stock it. Colgate held 41.3% of the world toothpaste market in 2025, by its own count from retail data, and 41.4% so far in 2026. But the whole US household products industry earns 34.42% after tax, so the advantage belongs to branded staples as a category as much as to Colgate. It is also fraying at the edges. The operating margin before write-downs fell from 24.0% in 2017 to 20.7% in 2025. Sales grew 3.3% a year over 2016–2025 while operating income grew 0.7%. In 2025 prices rose 2.1% and the number of units sold fell 0.4%. The average return describes brands built decades ago, not what a new dollar earns. How long the excess lasts is the decision that matters most in section 9.

**Judgment call: operating income.** I build on $4,225 million: the reported $3,306 million plus the $919 million write-down, which was a non-cash charge about a past purchase. I did not strip out restructuring and litigation charges, because Colgate books charges like those most years. And I added the $2,211 million of write-downs back to invested capital, so that money lost on failed deals still counts as money invested. The alternatives: on reported income the return is 27.04%; without adding the write-downs back it is 45.54%. Either way the return is more than three times the cost of capital. Confidence: high on the direction, moderate on the level.

## 4. Capital structure choices: how is Colgate financed?

**Almost entirely with equity, by choice.** Debt is $8,084 million at market value, including $566 million of leases: 9.34% of the firm's value. It has sat between 10% and 12% for six years with no trend. Interest is covered 15.82 times by operating income, and debt is 1.67 times EBITDA (operating income before depreciation and amortization). S&P rates Colgate A+, after a downgrade in April 2024. Management describes its approach as "prudent management of our capital structure".

The debt itself is plain. It is senior notes, no convertibles, 90.5% fixed-rate, with an average coupon of 2.9% and a weighted average maturity of 9.6 years. Because the coupons were set when rates were lower, the notes are worth 5.9% less than face value. Of the rated notes, 64.1% are in dollars and 35.9% in euros. Colgate also borrows short term through commercial paper, with an average daily balance of $1,611 million in 2025, and holds $3,641 million of unused credit lines.

Book equity is only $54 million after years of buybacks, so book-value debt ratios (99.37%) mean nothing; I use market values.

How Colgate compares: the US household products and food processing industries, weighted by Colgate's sales, carry about 19% debt to capital. Colgate carries half that. The course's trade-off points to more debt: a 25% tax rate, steady cash flows, and small, predictable investment needs. The only argument for so little debt is caution, and section 5 prices it.

## 5. Optimal financing: what is the right mix of debt and equity?

**The unconstrained optimum is 30%, and I recommend 20%.**

The optimum is the debt ratio that makes the cost of capital lowest. More debt saves tax but raises the risk borne by shareholders and lenders. The professor's capital structure spreadsheet and a model that re-rates the company at each step from its interest coverage both put the minimum at 30%.

| Debt ratio | Debt $M | Debt ÷ EBITDA | Cost of capital | Synthetic rating | Rating if operating income falls 20% | Share of the full gain captured |
|---|---|---|---|---|---|---|
| 9.34% (today) | 8,084 | 1.67x | 8.34% | AAA (S&P: A+) | | 0% |
| 20% (recommended) | 17,310 | 3.57x | 8.22% | A− | A− | 56.9% |
| 25% | 21,638 | 4.46x | | A− | BB+ | 91.8% |
| 30% (optimum) | 25,965 | 5.35x | 8.14% | BBB | B | 100% |
| 40% | 34,619 | | 10.56% | CCC | | |

*Model on a one-point grid; blank cells were not computed. Sources: Colgate 10-K; Damodaran's ratings spread table, January 2026.*

[Exhibit: cost of capital by debt ratio, 0% to 50%]

**Which tool I rely on.** The professor's spreadsheet rates Colgate A− at 30% (cost of capital 8.09%) because it keeps existing debt at today's low interest. The model reprices all debt and rates it BBB (8.14%). I rely on the model, because the spreadsheet's better rating depends on 2.9% coupons that disappear as the notes mature. The adjusted present value (APV) approach, which adds the tax benefit of debt and subtracts the expected cost of bankruptcy, also gives 30%, and the industry carries about 19%. All point well above 9.34%.

**Why stop at 20%.** The curve is flat from 20% to 30% (8.22% to 8.14%) and falls off a cliff just past 30%. Four reasons favour staying well short.

- The constraint I chose is a single-A rating that survives a bad year. At 20% the rating stays A− if operating income falls 20%; at 25% it drops below investment grade; at 30% a mere 10% fall gives BB. Operating income fell 7.4% in 2022 and 21.6% in 2015.
- The rating table is more generous than S&P. Today the table says AAA and S&P says A+. If that two-step gap holds, A− in the table is BBB in practice.
- Colgate depends on commercial paper, a market that closes to weaker credits.
- Stopping at 20% still captures 56.9% of the gain.

The alternative is 25%, which captures about nine-tenths of the gain and is still A− on today's income. A reader who thinks a 20% fall in income is too harsh a test for a toothpaste company would choose it and would not be wrong.

**What the move is worth.** On the market's value of the firm, moving to 20% is worth $2.26 a share and the full move to 30% $3.86. In my own valuation, which starts from a lower value, the move to 20% is worth $0.47 to $1.57 a share. The professor's spreadsheet puts the full move at $7.30, from $98.71 to $106.01. That figure is the market price plus a gain, not an estimate of value. In every version the gain is real and modest: a one-time transfer from the tax authorities to shareholders.

**Judgment call: bankruptcy cost in the APV.** I used 15% of firm value, within a range of 10% to 25%, because a maker of staples loses little in distress beyond supplier terms and short-term funding. At 25% the APV optimum moves from 30% to 26%. Across every cost anyone would defend it stays between 26% and 34%. Confidence: high that Colgate should borrow more; moderate that 20% is the right stopping point, which is a preference about risk as much as a calculation.

## 6. Financing changes: should Colgate move to the optimum, and with what debt?

**Yes, slowly, and the cash should go out rather than into acquisitions.**

Colgate is under-borrowed but not under threat. No buyer could debt-finance a $78.5 billion purchase of a business that cannot carry even 40% debt. The realistic threat is an activist with a simple case: a 33.0% total return since December 2020 against 100.0% for the S&P 500, an idle balance sheet and $2.2 billion of write-offs. That case was stronger a year ago, when the figures were 4.0% and 96.2%; Colgate's shares returned 27.9% in 2026 to date while the index returned 2.0%. None is visible in the register.

Nor does Colgate have projects big enough to absorb new borrowing. Large sums could only go into acquisitions, where the record says the money would likely earn less than it costs.

**The path.** Borrow $9,226 million over about five years, about $1,845 million a year, taking debt to $17,310 million. Pay it out as special dividends while the share price is above my estimate of value (section 8). Leave the regular dividend on its slow rise; one raised with borrowed money would have to be cut when the borrowing stops. Going gradually lets Colgate stop if S&P reacts more harshly than the rating table suggests.

**The right kind of debt.** The debt should match the assets: long-lived brands, cash flows steady through recessions, and pricing power that protects sales but not margins. That calls for straight, fixed-rate debt with an average life of five to ten years, spread over many maturities. Regressions of Colgate's own history on macroeconomic variables are too noisy to use (no coefficient reaches 1.3 times its standard error), so this rests on what the business is.

The existing debt fits on rate type and maturity but not on currency. Two-thirds of the notes are in dollars and the rest in euros, while two-thirds of sales are outside the US and 45% are in emerging markets. Colgate designates $3,942 million of foreign currency debt as a hedge of its investments abroad, but the filings do not say which currencies. The fix is the new borrowing, not swaps: leave the cheap 2.9% notes alone and raise the new $9.2 billion mostly outside the dollar, where Colgate's foreign markets have deep enough bond markets.

## 7. Dividend policy: how does Colgate return cash?

**About $3 billion a year: a steady, rising dividend plus flexible buybacks.**

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | Five years |
|---|---|---|---|---|---|---|
| Dividends | 1,679 | 1,691 | 1,749 | 1,789 | 1,823 | 8,731 |
| Buybacks | 1,320 | 1,308 | 1,128 | 1,739 | 1,210 | 6,705 |
| Total returned | 2,999 | 2,999 | 2,877 | 3,528 | 3,033 | 15,436 |
| Free cash flow to equity | 2,409 | 2,518 | 2,314 | 2,885 | 2,712 | 12,838 |
| Cash from employee option exercises | 424 | 418 | 380 | 638 | 101 | 1,961 |
| Returned above FCFE, net of option cash | 166 | 63 | 183 | 5 | 220 | 637 |

*Sources: Colgate 10-K cash flow statements, 2021–2025. FCFE as defined in the professor's dividend spreadsheet, which counts acquisitions as capital spending.*

The dividend per share rose every year, from $1.79 in 2021 to $2.06 in 2025. The payout ratio, dividends over net income, was 77.46%, inflated by write-down years; before write-downs it is a little over 60%. The yield is 2.11%. Buybacks are the flexible part, between $1,128 million and $1,739 million a year.

Free cash flow to equity (FCFE) is the cash left for shareholders after reinvestment and debt flows. On its face Colgate returned 120% of FCFE over five years, more than it generated. But employees exercising options paid Colgate $1,961 million, cash the FCFE formula never sees, and much of the buyback is the other side of that program: shares bought in the market and reissued to employees. Net of option cash, Colgate returned about 105% of FCFE over five years and within 7% over eight. Even that overstates it a little: the dividends paid include about $630 million over 2022–2025 that went to the outside owners of partly owned subsidiaries, not to Colgate's shareholders.

[Exhibit: cash returned against FCFE, 2018–2025, with and without option proceeds]

The balance sheet agrees. Cash at the end of 2025, $1,288 million, was lower than at the end of 2017, and the two years of heavy borrowing, 2019 and 2022, were the two years of large acquisitions. Colgate borrows to buy businesses, not to pay dividends.

## 8. Dividend assessment: should Colgate return more or less?

**The amount is right. The form is wrong while the shares trade above their value.**

Colgate sits in the cell of the course's dividend matrix that calls for no change: it returns about what it generates, and its existing business earns far more than its cost of capital. Against the household products sector it is typical: payout 77.46% against 67.25%, yield 2.11% against 2.94%. Against the six comparable companies in section 9, over five years, Colgate paid 77.5% of net income in dividends against a median of 69.6%, and returned 119.5% including buybacks net of shares issued, against 94.6%. Colgate's net income carries the write-downs; before them its figures are 64.8% and 99.9%, in line with the group. I would not cut the payout: cash held back would be at risk of going into acquisitions. One caution: the stock missed its required return in four of the five years from 2021 to 2025. The high return on capital comes from brands the market priced in long ago, and what was new in these years was slow growth and write-downs.

**The form.** A buyback pays the shareholders who sell; a dividend pays everyone the same per share. When the price is above the value, a buyback pays sellers more than their shares are worth, and the shareholders who stay make up the difference. My valuation (section 9) puts a share at $61.83 against a price of $98.71. Borrowing $9,226 million to buy back shares would overpay by $3,447 million, or $4.91 for each remaining share. That is more than twice the $2.26 a share the extra debt is worth on the market's own value. The buyback would undo the gain from the borrowing.

So my recommendation is to pay out both the borrowed money and the cash now spent on buybacks as special dividends, for as long as the price stays above value. Special dividends suit money that will not recur, because they create no expectation of being repeated. Buybacks become the better route once the price falls to or below value.

**Judgment call: dividends rather than buybacks.** This depends entirely on the valuation. If a share is worth $98.71 or more, buybacks do no harm. If it is worth $79.74, the default-growth case, the overpayment on the borrowed money roughly equals the gain from the debt. The recommendation also runs against a pay plan that rewards earnings per share, which buybacks raise and dividends do not. With a $5 billion buyback program authorized in March 2025, I rate the chance of adoption as low. Confidence that the shares are above value: moderate (section 9). Confidence in the recommendation: only as good as that.

## 9. Valuation: what is Colgate worth?

**$61.83 a share in the professor's valuation spreadsheet, against a price of $98.71.** The price is 159.64% of that value. The value rests on two long-run assumptions, not on the next five years.

**The story and its numbers.** Revenue grows 2.25% next year, 3.1% by year five and 3% forever. The operating margin recovers from 20.5% to 21.3%. That is the analysts' consensus less about 0.7 points for the restructuring charges Colgate books most years, which consensus leaves out and my operating income keeps in. Colgate needs little capital to grow, $2.20 of new sales for each dollar invested. The cost of capital moves from 8.34% to 8.43%, the rate for an average mature company. For ten years the brands keep earning today's returns. After that, new investment earns 20%, under half of today's return but far above its cost. Ten years of cash flow are worth $23,776 million today and the value of everything after year 10 (the terminal value) another $32,940 million today: $56,717 million for the operating business. Subtracting debt and minority interests (the outside owners' share of subsidiaries Colgate does not wholly own), adding cash and small investments, and subtracting $439 million for employee options leaves $49,338 million, or $61.83 over 797.9 million shares.

**The two assumptions that carry the value.** The terminal value is 58.1% of the operating value. Its size depends on how long the excess returns last (the return on new investment) and how fast the company grows forever. The spreadsheet's defaults assume new investment earns only its cost and growth equals the riskfree rate, 4.82%. I replaced both, and the four combinations are:

| | Growth forever 3% | Growth forever 4.82% |
|---|---|---|
| New investment earns its cost (8.43%) | $51.84 | $53.82 |
| New investment earns 20% | **$61.83** | $79.74 |

*With the spreadsheet's default stable cost of capital of 9.05% as well, the first cell becomes $50.90, the all-defaults result.*

[Exhibit: value per share by return on new investment and growth forever]

I chose 3% growth because sales grew 3.3% a year over 2016–2025, analysts expect 2.3% to 3.5%, and management told analysts in October 2026 that its categories are growing 1.5% to 3% a year; the 4.82% default would have Colgate growing faster forever than it has in a decade, with flat volumes. I chose a 20% return because the default, that competition erases every advantage, does not fit a brand that has held for generations, while today's 34.56% does not fit new money given the acquisition record. The two assumptions multiply each other. When new investment earns only its cost, growth adds no value, and value barely moves between 2% and 4.82% growth ($50.79 to $53.82). At 20% each point of growth is worth much more ($56.20 to $79.74).

| Case | Value per share | Price as % of value |
|---|---|---|
| Base case | $61.83 | 159.64% |
| All the spreadsheet's defaults | $50.90 | 193.9% |
| The spreadsheet's default growth, 4.82% | $79.74 | 123.78% |
| Beta 0.63 / 0.80 (cost of capital 7.84% / 8.67%) | $63.82 / $60.56 | 154.66% / 163.00% |
| Peer-median beta 0.41 (cost of capital 6.77%) for years 1–5, then the mature rate | $68.32 | 144.5% |
| Peer-median beta 0.41 held forever | about $91.88 | 107.4% |
| Today's 34.56% return kept forever, with growth at 4.82% | $87.70 | |
| Margin held at the trailing 19.17% / back to 2017's 24.0% | $54.73 / $70.15 | |
| With the move to 20% debt | $62.31 to $63.41 | |

*Sources: the professor's valuation spreadsheet, filled from the 10-K, 10-Q, S&P Capital IQ consensus and Damodaran's datasets.*

Everything near-term moves value by a few dollars. Revenue growth a point higher or lower in years 1–5 moves it about $3.50. Using consensus margins as published gives $64.27. The spreadsheet's global sales-to-capital default of 1.79 gives $61.19. The two long-run assumptions move it by about $28.

**What the price requires.** Holding the rest of the base case, the price needs an operating margin of 33.3% (the best in ten years was 26.0%, in 2016), or growth forever of 5.78% (above the riskfree rate, which the course treats as impossible), or a cost of capital of 6.53% in every year. That last one is the uncomfortable point, because the low end of my beta range is close to it. Colgate's own regression gives 6.31% and its large peers give 6.77%. At 6.77% for five years, fading to the mature rate, a share is worth $68.32. At 6.77% forever it is worth about $91.88, within 7% of the price. So the conclusion that the shares are overpriced rests on one belief: that over decades Colgate's cost of capital moves toward that of an average mature company. The professor's spreadsheet builds that in by default, and I kept it. A reader who thinks branded staples will stay this insulated from the market forever should conclude the shares are close to fairly priced.

**The bridge leans high.** Three items in the step from operating value to equity value probably flatter it. Minority interests are subtracted at their book value of $352 million, but those outside owners earned $129 million in 2025; valued on earnings their claim is about $2,117 million, which alone takes the value to $59.62. The pension and retiree-benefit shortfall of $1,283 million is not subtracted (−$1.21 after tax). Debt at fair value instead of carrying value adds $0.91. Together these would put the base case near $59. I keep $61.83 as the spreadsheet's own result; none of the three changes the conclusion.

A separate model on three years of analysts' forecasts gives $60.85, which rules out a gross error but rests on the same two assumptions.

**Relative valuation.** On multiples, Colgate is priced in line with its sector. I used the six household and personal care companies on S&P Capital IQ's default comparison list: Procter & Gamble, Kimberly-Clark, Church & Dwight, Clorox, Reckitt Benckiser and Henkel. Their median enterprise value (equity plus net debt) is 15.35 times EBITDA, which gives Colgate $89.23 a share, within $72.67 to $93.75 across the other earnings multiples. Colgate trades at 16.85 times, a 10% premium, about what its higher operating margin (20.7% against a median of 18.0%) justifies. The list is Capital IQ's, not one built for Colgate; it has no pet food companies, and Kimberly-Clark's forward figures are unusable.

Pricing and value disagree, and both answers stand. The market prices Colgate much as it prices Procter & Gamble and Church & Dwight; my cash flows say it is worth under two-thirds of that. If both are right, it is the sector's price that the cash flows do not support, not Colgate's alone. I have not valued the peers, so this is the reading that fits both results, not a finding about them. Analysts' mean target of $101.70 is a forecast of the price, not an estimate of value.

**Value of control.** Run my way, with 20% debt and dividends in place of buybacks, Colgate is worth $62.31 to $63.41. The switch to dividends changes who gets the value, not its size. The gain from control is $0.47 to $2.76 a share across measures and the chance of change is low, so none of the $36.88 gap between price and value is the market paying for control.

| Judgment call | Choice and reason | Alternative, and what it changes | Confidence |
|---|---|---|---|
| Return on new investment after year 10 | 20%: the brand is durable, the acquisitions were not | Equal to the cost of capital (default): $51.84 | Low on the number; nobody can observe a 2040 return |
| Growth forever | 3%: matches history and consensus | 4.82% (default): $79.74 | Moderate |
| Forecast margins | Consensus less about 0.7 points for recurring charges | Consensus as published: $64.27 | Moderate; the margin path is the most optimistic near-term input |
| Sales to capital | 2.2: Colgate's own ratio and the US household products average | Global default 1.79: $61.19 | High |
| Comparable companies | Capital IQ's six household and personal care companies | All ten on the list: $76.25 on EV ÷ EBITDA | Low to moderate |

**How confident I am.** I am confident in the description of the business, which comes from audited filings. I am only moderately confident that the shares are worth less than $98.71. That holds under every growth and return assumption I tested, but it comes close to failing if the low betas of Colgate and its large peers last forever, and I cannot rule that out. I am not confident in $61.83 as a point. The direction of every finding in this report is firmer than its size.

## Sources

Colgate-Palmolive Form 10-K for 2025 (filed 2026-02-23) and 2024; Form 10-Q for the quarter to 2026-09-30 (filed 2026-10-30); 2026 proxy statement (filed 2026-03-25); S&P Capital IQ (ownership, credit ratings, consensus estimates, comparable companies, multiples, betas, cash flow statements and earnings call transcripts); FRED (10-year Treasury yield); Damodaran Online datasets (implied equity risk premium, country risk premiums, industry betas and averages, ratings spreads); Professor Damodaran's capital structure, dividend and valuation spreadsheets.
