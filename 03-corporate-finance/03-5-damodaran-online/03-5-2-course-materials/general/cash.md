---
title: "DISCOUNTED CASHFLOW MODELS: WHAT THEY ARE AND HOW TO CHOOSE THE RIGHT ONE.."
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/cash.htm
---

DISCOUNTED CASHFLOW MODELS: WHAT THEY ARE AND HOW TO CHOOSE THE
RIGHT ONE.. 

**Valuing a Company with Cash**

**Basic Proposition:** Cash is different from other assets, insofar as

- its value is known with certainty

- it has no risk associated with it

The easiest way to value cash (and marketable securities) is to
separate them from other assets, and value them separately.

**Steps involved:**

*Step 1*: Estimate the cash flows for the firm, as if it had no cash,
i.e., take out any interest or other income that accrued from
cash from the reported income. Thus, if the firm is being valued,

Adjusted EBIT = EBIT - Pre-tax Interest Income on Cash and Marketable
Securities

If equity is being valued,

Net Income = Net Income - Interest Income (1 - tax rate)

*Step 2*: Estimate the discount rate for the firm, as if it had no cash.
Since cash has no risk, this will mean that the risk parameteris
for the firm have to be re-estimated. Since the reported beta
for the firm reflects the cash holdings that the firm had during
the regression period, the beta has to be adjusted by doing the
following:

Step 2a: Estimate the cash balance as a percentage of firm value
during the period of the regression.

Step 2b: Estimate the unlevered beta for the firm, using the average
debt/equity ratio during the period of the regression.

Step 2c: Note that this unlevered beta was a weighted average
of the beta of cash (zero) and the beta of all other assets.

Unlevered Beta = Beta of all other Assets (1 - Cash Balance as
% of Firm Value) + 0 (Cash Balance as % of Firm Value)

Step 2d: Solve for the beta of all other assets

Unlevered Beta without cash = Unlevered Beta/ (1 - Cash Balance
as % of Firm Value)

Step 2e: Calculate the new beta for the firm, using the firmís
current debt/equity ratio

New Beta for Stock = Unlevered Beta without Cash (1 + (1- tax
rate) (Current Debt/Equity Ratio))

Step 2f: Calculate the new cost of capital for the firm, using
this new beta for cost of equity

Step 3: Value the assets of the firm using the cash flows adjusted
(in step 1) and the re-estimated discount rates (in step 2)

Step 4: Add the current cash balance

Value of the Firm = Value of the Assets from step 3 + Current
Cash Balance

Step 5: Subtract out the total debt outstanding to get value of
equity

Value of Equity = Value of Firm - Value of Debt

Alternatively, the firm value can be compared to the sum of the
values of equity and debt.

---

**The Standard Practice (and what could be wrong with it)**

---

---

The standard practice on Wall Street in valuations is to do a
status quo valuation of the firm (using reported net income and
cost of capital) and compare it to the sum of value of equity
and net debt, which is the difference between debt and cash.

---

Status Quo Valuation of Firm ***Compared to*** Value of Equity + Value of Debt - Cash Balance

In other words, they do the same thing that we do, except that
they do not adjust the income and cost of capital for the existence
of cash. This could result in the double counting of cash, since
the interest income from cash is counted in the status quo valuation
and cash is counted again as an asset.

**An Example: Valuing Chrysler in March 1996**

**Step 1:** Estimate the operating earnings without the interest income from
cash

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | *1995* | *Next Year* |  |
| EBIT = |  | $ 4,444 |  |  |
| Less Interest Income from Cash = | | $ 800 |  |  |
| EBIT without interest income = | | $3,644 | $ 3,826 |  |
| EBIT (1-t) = |  | $ 2,332 | $ 2,449 |  |

**Step 2:** Estimate the discount rate, without the cash effects

*2a: Estimate the cash balance as a percent of firm value for period
of the regression*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1991 | 1992 | 1993 | 1994 | 1995 | Average |
| Cash | $ 3,035 | $ 3,649 | $ 5,095 | $ 8,371 | $ 8,125 |  |
|  |  |  |  |  |  |  |
| MV of Equity | $ 3,435 | $ 9,468 | $ 18,834 | $ 17,399 | $ 20,854 |  |
| Debt | $ 19,438 | $ 15,551 | $ 11,451 | $ 13,106 | $ 14,193 |  |
| Firm Value | $ 22,873 | $ 25,019 | $ 30,285 | $ 30,505 | $ 35,047 |  |
|  |  |  |  |  |  |  |
| Cash as % of Value | 13.27% | 14.58% | 16.82% | 27.44% | 23.18% | 19.06% |

*2b: Estimate the unlevered beta for Chrysler, using the average
debt equity ratio during the period of the regression*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1991 | 1992 | 1993 | 1994 | 1995 | Average |
| MV of Equity | $ 3,435 | $ 9,468 | $ 18,834 | $ 17,399 | $ 20,854 |  |
| Debt | $ 19,438 | $ 15,551 | $ 11,451 | $ 13,106 | $ 14,193 |  |
| Debt/Equity Ratio | 5.66 | 1.64 | 0.61 | 0.75 | 0.68 | 1.87 |

---

Unlevered Beta for Chrysler = Beta for the Stock / ( 1 + (1- tax
rate) (Debt/Equity))

---

= 1.20 / (1 + 0.64 \* 1.87) = 0.55

*2c & d: Estimate the unlevered beta without cash*

Beta of other assets (1 - Cash/Firm Value) + 0 (Cash/Firm Value)
= Unlevered Beta for the Firm

Beta of other assets (1 - 0.1906) + 0 (0.1906) = 0.55

Unlevered Beta of other assets = 0.55/0.8094 = 0.68

*2e: Estimate the new levered beta*

Levered Beta without Cash = 0.68 ( 1 + (1 - tax rate) ( Current
Debt Equity Ratio)

= 0.68 ( 1 + 0.64 (0.68)) = 0.98

*2f: Estimate the cost of capital*

Cost of Equity = 6.5% + 0.98 (5.5%) = 11.87% Current Proportion
of Equity = 20854/(20854+14193) = 59.50%

Cost of Debt = 7.5% (based upon bond rating) Current Proportion
of Debt = 14193/(20854+14193) = 40.50%

Cost of Capital = 11.87% (0.595) + 7.5% (1-0.36) (0.405) = 9.00%

**Step 3:** Value Chryslerís non-cash assets.

Model Used: Stable Growth FCFF Model

Reasons: Firm is in stable growth; Cyclical Firm in a Mature Industry

Estimated Free Cash Flow to Firm Next Year

|  |  |  |  |
| --- | --- | --- | --- |
| EBIT (1-t) = |  | $ 2,449 |  |
| - (Net Capital Expenditure) = | | $ 1,000 |  |
| - Change in Working Capital = | |  | $ 195 |
| Free Cashflow to | Firm | $ 1,254 |  |

Value of Chryslerís non-cash assets = Expected Free Cash Flow
to Firm Next Year / (WACC - Stable Growth Rate)

= $ 1,254 / (.09 - .05) = $ 31,344 million

**Step 4:** Value all of Chryslerís assets by adding back the cash

Value of non-cash assets = $ 31,344 million

+ Cash & Marketable Securities = $ 8,125 million

Value of Chrysler = $ 39,469 million

**Step 5:** Subtract out the value of the outstanding debt, and estimate
the value of equity.

Value of Chrysler = $ 39,469 million

- Value of Debt = $ 14,193 million

- Value of Preferred Stock = $ 683 million

Value of Equity = $ 24, 413 million

/ Number of Shares = 382.56 million

Value per Share = $ 63.82
