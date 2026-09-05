---
title: "Ch8 2A"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/acf3E/ch8-2A.xls
---

# Ch8 2A

Source: http://www.stern.nyu.edu/~adamodar/pc/acf3E/ch8-2A.xls

Sheets: READ ME FIRST, FAQs, Inputs, Operating Lease Information, Default Spreads and Ratios, Optimal Capital Structure, Levered Betas (wo tax adj), Summary Table

## READ ME FIRST

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
|  |
|  |
| READING THE OUTPUT |
| Summary |
|  |
|  |
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
| Earnings before interest, taxes and depreciation (EBITDA) |
| Depreciation and Amortization: |
| Capital Spending: |
| Interest expense on debt: |
| Tax rate on ordinary income: |
| Current Rating on debt (if available): |
| Interest rate based upon rating: |
| Market Information |
| Number of shares outstanding: |
| Market price per share: |
| Beta of the stock: |
| Book value of debt: |
| Can you estimate the market value of the outstanding debt? |
| If so, enter the market value of debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the average maturity of outstanding debt? |
| Do you have any operating leases? |
| General Market Data |
| Current long-term (LT) government bond rate: |
| Risk premium (for use in the CAPM) |
| Country default spread (for cost of debt)  |
|  |
| General Data |
| Which spread/ratio table would you like to use for your analysis? |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |
| Do you want the firm's current rating to be adjusted to the synthetic rating? |

## Operating Lease Information

| Operating Lease Converter |
|---|
| Operating lease expenses are really financial expenses, and should be treated as such. Accounting standards allow them to |
| be treated as operating expenses. This program will convert commitments to make operating leases into debt and |
| adjust the operating income accordingly, by adding back the imputed interest expense on this debt. |
|  |
| Inputs |
| Operating lease expense in current year = |
| Operating Lease Commitments (From footnote to financials) |
| Year |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 and beyond |
|  |
| Pre-tax Cost of Debt = |
|  |
| From the current financial statements, enter the following |
| Reported Operating Income (EBIT) = |
| Reported Interest Expenses = |
| Output |
| Number of years embedded in yr 6 estimate = |
|  |
| Converting Operating Leases into debt |
| Year |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 and beyond |
| Debt Value of leases = |
|  |
| Restated Financials |
| Operating Income with Operating leases reclassified as debt = |
| Interest expenses with Operating leases classified as debt = |

## Default Spreads and Ratios

| Inputs for synthetic rating estimation |
|---|
| Enter the type of firm = |
| Enter current Earnings before interest and taxes (EBIT) = |
| Enter current interest expenses = |
| Enter current long term government bond rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
|  |
| For large or stable firms |
| If interest coverage ratio is |
| > |
| -100000 |
| 0.2 |
| 0.65 |
| 0.8 |
| 1.25 |
| 1.5 |
| 1.75 |
| 2 |
| 2.25 |
| 2.5 |
| 3 |
| 4.25 |
| 5.5 |
| 6.5 |
| 8.5 |
|  |
|  |
| For smaller and riskier firms |
| If interest coverage ratio is |
| greater than |
| -100000 |
| 0.5 |
| 0.8 |
| 1.25 |
| 1.5 |
| 2 |
| 2.5 |
| 3 |
| 3.5 |
| 4 |
| 4.5 |
| 6 |
| 7.5 |
| 9.5 |
| 12.5 |

## Optimal Capital Structure

| Disney |
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
| Assumes constant saving |
| Assumes perpeutal growth |
|  |
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
| Beta of debt |
| Beta of equtiy |
| Cost of Equity |
|  |
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
|  Value (no growth) |
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

## Levered Betas (wo tax adj)

| Debt to Capital Ratio | D/E Ratio | Levered Beta | Cost of Equity |
|---|---|---|---|
| 0 | 0 | 0.7332980261744674 | 0.07899788157046805 |
| 0.1 | 0.11111111111111112 | 0.7838141124220419 | 0.08202884674532251 |
| 0.2 | 0.25 | 0.8469592202315098 | 0.08581755321389059 |
| 0.3 | 0.4285714285714286 | 0.9281457874151117 | 0.0906887472449067 |
| 0.4 | 0.6666666666666667 | 1.0363945436599138 | 0.09718367261959483 |
| 0.5 | 1 | 1.1879428024026373 | 0.10627656814415824 |
| 0.6 | 1.4999999999999998 | 1.4152651905167217 | 0.11991591143100332 |
| 0.7 | 2.333333333333333 | 1.7941358373735299 | 0.1426481502424118 |
| 0.8 | 4.000000000000001 | 2.5518771310871466 | 0.1881126278652288 |
| 0.9 | 9.000000000000002 | 4.8251010122279965 | 0.3245060607336798 |

## Summary Table

| Debt Ratio | Beta of Equity | Beta of Debt | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | Cost of capital | Firm Value (G) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0.7332980261744674 | 0.052083333333333315 | 0.07899788157046805 | AAA | 0.0475 | 0.38 | 0.02945 | 0.07899788157046805 | 58499.82122694249 |
| 0.1 | 0.780226149459079 | 0.052083333333333315 | 0.08181356896754474 | AAA | 0.0475 | 0.38 | 0.02945 | 0.07657721207079027 | 60542.62412144043 |
| 0.2 | 0.8388863035648432 | 0.052083333333333315 | 0.08533317821389058 | AAA | 0.0475 | 0.38 | 0.02945 | 0.07415654257111247 | 62732.170529858384 |
| 0.3 | 0.9087707874151116 | 0.07291666666666667 | 0.08952624724490671 | AA | 0.052500000000000005 | 0.38 | 0.03255 | 0.07243337307143469 | 64389.16139414142 |
| 0.4 | 0.9933389881043583 | 0.10416666666666666 | 0.09460033928626149 | A | 0.060000000000000005 | 0.38 | 0.037200000000000004 | 0.07164020357175689 | 65181.45055057158 |
| 0.5 | 1.1104428024026374 | 0.12499999999999999 | 0.10162656814415824 | A- | 0.065 | 0.38 | 0.0403 | 0.07096328407207912 | 65873.1014056617 |
| 0.6 | 1.2796401905167216 | 0 | 0.1117784114310033 | BBB | 0.07 | 0.38 | 0.0434 | 0.07075136457240133 | 66092.64042096879 |
| 0.7 | 1.2817747262624188 | 0.3541666666666667 | 0.11190648357574513 | B- | 0.12000000000000001 | 0.38 | 0.07440000000000001 | 0.08565194507272356 | 53530.38366085591 |
| 0.8 | 1.5185437977538132 | 0.41666666666666663 | 0.1261126278652288 | CCC | 0.135 | 0.38 | 0.08370000000000001 | 0.09218252557304576 | 49405.95287345922 |
| 0.9 | 2.5992963740494637 | 0.41666666666666663 | 0.19095778244296782 | CCC | 0.135 | 0.3451907287825658 | 0.08839925161435364 | 0.09865510469721506 | 45896.58145380988 |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Debt Ratio | $ Debt | Interest Expense | Interest coverage ratio | Bond Rating | Interest rate on debt | Tax Rate | After-tax cost of debt |  |  |
| 0 | 0 | 0 | 7 | AAA | 0.0475 | 0.38 | 0.02945 |  |  |
| 0.1 | 6187.549157957317 | 293.9085850029726 | 23.23583021998989 | AAA | 0.0475 | 0.38 | 0.02945 |  |  |
| 0.2 | 12375.098315914634 | 587.8171700059452 | 11.617915109994945 | AAA | 0.0475 | 0.38 | 0.02945 |  |  |
| 0.3 | 18562.64747387195 | 974.5389923782775 | 7.007631336187427 | AA | 0.052500000000000005 | 0.38 | 0.03255 |  |  |
| 0.4 | 24750.19663182927 | 1485.0117979097563 | 4.598758064372999 | A | 0.060000000000000005 | 0.38 | 0.037200000000000004 |  |  |
| 0.5 | 30937.745789786586 | 2010.9534763361282 | 3.3960059552292914 | A- | 0.065 | 0.38 | 0.0403 |  |  |
| 0.6 | 37125.2949477439 | 2598.7706463420736 | 2.627861751070285 | BBB | 0.07 | 0.38 | 0.0434 |  |  |
| 0.7 | 43312.84410570122 | 5197.541292684146 | 1.3139308755351427 | B- | 0.12000000000000001 | 0.38 | 0.07440000000000001 |  |  |
| 0.8 | 49500.39326365854 | 6682.553090593903 | 1.021946236527333 | CCC | 0.135 | 0.38 | 0.08370000000000001 |  |  |
| 0.9 | 55687.94242161586 | 7517.872226918142 | 0.9083966546909626 | CCC | 0.135 | 0.3451907287825658 | 0.08839925161435364 |  |  |
