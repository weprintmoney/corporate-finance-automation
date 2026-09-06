---
title: "Capstruo"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/capstruo.xls
---

# Capstruo

Source: https://www.stern.nyu.edu/~adamodar/pc/capstruo.xls

Sheets: READ ME 1ST, FAQs, Inputs, Default Spreads and Ratios, Optimal Capital Structure, Summary Table

## READ ME 1ST

| PRELIMINARY STUFF AND INPUTS |
|---|
| Objective |
|  |
| Before you start |
|  |
| Inputs |
|  |
| Units |
| Income inputs |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Balance Sheet |
|  |
|  |
| Market Data |
|  |
|  |
|  |
| Tax Rate |
| Default Spreads |
|  |
|  |
|  |
| READING THE OUTPUT |
| Summary |
|  |
|  |
|  |
|  |
| Details |
|  |
| References |
| Corporate Finance: Theory and Practice, Chapter 18 |
| Applied Corporate Finance: Chapter 8 |

## FAQs

| Question | Answer |
|---|---|
| Q1: What do I do excel says there are circular references? | Go into preferences, choose calculation options and make sure the iteration box has a check in it. |
| Q2: My spreadsheet has gone crazy. I get errors all over. | I am sorry to say this, but you probably just made an input error. While you might have |
| What did I do wrong? | fixed it, the iterations in the spreadsheet make it very sensitive and the errors will not |
|  | go away. The only fix (Sorry, sorry…) is to copy the inputs into a fresh version of the spreadsheet. |
| Q3: I am entering the inputs for my company but the | You probably forgot to check the iteration box (see Q1) |
| optimal numbers do not seem to change from the |  |
| originals |  |
| Q4: I am getting an optimal debt ratio of 0%. This can't | Sure. If your operating income is either negative or very low, relative to your firm value, |
| be right. Can it? | you can end up at an optimal debt ratio of 0%. For instance, if you have EBIT of 100 on a |
|  | firm value of 10000, a 10% debt ratio would probably push you into a C rating and give |
|  | you a very high cost of capital. |
| Q5: My cost of capital at my optimal debt ratio is higher | Generally, you are right. However, I would suggest that you look at three factors: |
| than the current cost of capital. I thought it was supposed |  - If your optimal is just slightly higher or lower than your current debt ratio, it is possible that you |
| to be lower. | are closer to the optimal than the stated optimal. Let me explain. Assume that you are at a 24% debt ratio |
|  | and the optimal comes out to 30%. The true optimal is really somewhere around 30% since |
|  | I am constrained to work in 10% increments of the debt ratio. If the true optimal were |
|  | 26%, your current debt ratio of 24% is closer to the optimal. |
|  |  - Rating Differences: One of the costs of rating a company based only on the interest |
|  | coverage ratio is that the rating might be very different from the actual rating. Thus, your |
|  | current cost of capital is based upon your current rating, and the optimal is based upon |
|  | the synthetic ratings, and the two don't match, the current and the optimal cost of capital |
|  | can be mismatched. You can get around this by switching to a synthetic rating for computing |
|  | the current cost of capital (in the input sheet). |
|  |  - Existing debt at low rates: I assume in the spreadsheet that existing debt gets refinanced at |
|  | the new pre-tax cost of debt at each debt ratio. Consequently, if you have a lot of old debt on |
|  | your books at much lower rates, the interest expense that I report will be much higher than |
|  | your actual interest expense. This, in turn, can affect your interest coverage ratio and rating. |
|  | This, too, you can fix by locking in debt at current rates in the input sheet. |

## Inputs

| Inputs |
|---|
| Please enter the name of the company you are analyzing: |
| Financial Information |
| Earnings before long term interest expenses, depreciation & amortization |
| Depreciation and Amortization: |
| Capital Spending: |
| Interest expense on long term debt: |
| Tax rate on ordinary income: |
| Current Rating on long term debt (if available): |
| Interest rate based upon rating: |
| Market Information |
| Number of shares outstanding: |
| Market price per share: |
| Beta of the stock: |
| Book value of long term debt: |
| Can you estimate the market value of the long term debt? |
| If so, enter the market value of debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the average maturity of outstanding debt? |
| Do you have any operating leases? |
| General Market Data |
| Current long-term (LT) government bond rate: |
| Risk premium (for use in the CAPM) |
|  |
| General Data |
| Which spread/ratio table would you like to use for your anlaysis? |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |
| Do you want the firm's current rating to be adjusted to the synthetic rating? |

## Default Spreads and Ratios

| Inputs for synthetic rating estimation |
|---|
| Enter the type of firm = |
| Earnings before interest and taxes (EBIT) = |
| Current interest expenses = |
| Current long term government bond rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
|  |
| For large financial service firms |
| If interest coverage ratio is |
| > |
| -100000 |
| 0.05 |
| 0.1 |
| 0.2 |
| 0.3 |
| 0.4 |
| 0.5 |
| 0.6 |
| 0.75 |
| 0.9 |
| 1.2 |
| 1.5 |
| 2 |
| 2.5 |
| 3 |
|  |
| For smaller and riskier financial service firms |
| If interest coverage ratio is |
| greater than |
| -100000 |
| 0.05 |
| 0.1 |
| 0.2 |
| 0.3 |
| 0.4 |
| 0.55 |
| 0.7 |
| 1 |
| 1 |
| 1.5 |
| 2 |
| 2.5 |
| 3 |
| 3.5 |

## Optimal Capital Structure

| Summit |
|---|
| Capital Structure |
| Current MV of Equity = |
| Market Value of interest-bearing debt = |
| # of Shares Outstanding = |
| Debt Value of Operating leases (if any) |
| Risk Premium = |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Assumes perpeutal growth |
|  |
|  |
| We use the following default spreads in our analysis. Change them in the input sheet if necessary: |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
| Current beta= |
| Current  Debt= |
| Tax rate= |
|  |
|  |
| D/(D+E) |
| D/E |
| $ Debt |
| Beta |
| Cost of Equity |
| % Drop in EBITDA |
| EBITDA |
| Depreciation |
| EBIT |
| Interest |
| Taxable Income |
| Tax |
| Net Income |
| (+)Deprec'n |
| Funds from Op. |
|  |
| Pre-tax Int. cov |
| Funds/Debt |
| Likely Rating |
| Pre-tax cost of debt |
| Eff. Tax Rate |
|  |
| D/(D+E) |
| D/E |
| $ Debt |
| Cost of equity |
| Cost of debt |
| Cost of Capital |
|  |
| Value (perpetual growth) |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Firm Value (G) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.6822989876645938 | 0.10305306612163587 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.10305306612163587 | 8479.037036757003 |
| 0.1 | 0.7315761367737034 | 0.10616245423042069 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.09970620880737861 | 8764.988302017911 |
| 0.2 | 0.7931725731600904 | 0.1100491893664017 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.09635935149312136 | 9070.899843146746 |
| 0.3 | 0.8723679913711592 | 0.11504642025552014 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.0930124941788641 | 9398.937172618937 |
| 0.4 | 0.9779618823192512 | 0.12170939477434475 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.08966563686460685 | 9751.590808102788 |
| 0.5 | 1.1257933296465799 | 0.1310375591006992 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.0863187795503496 | 10131.739621271368 |
| 0.6 | 1.3475405006375727 | 0.14502980559023082 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.08297192223609234 | 10542.729604930379 |
| 0.7 | 1.7171191189558945 | 0.16835021640611694 | AAA | 0.064 | 0.35 | 0.041600000000000005 | 0.07962506492183509 | 10988.472621630064 |
| 0.8 | 2.4562763555925384 | 0.2149910380378892 | A+ | 0.0685 | 0.35 | 0.044525 | 0.07861820760757783 | 10017.034736257616 |
| 0.9 | 4.673748065502469 | 0.3549135029332058 | A+ | 0.0685 | 0.35 | 0.044525 | 0.07556385029332058 | 10424.439572433384 |
