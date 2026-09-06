---
title: "Tatachemicalscs"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/eqegs/tatachemicalscs.xls
---

# Tatachemicalscs

Source: http://www.stern.nyu.edu/~adamodar/pc/eqegs/tatachemicalscs.xls

Sheets: READ ME FIRST, FAQs, Inputs, Operating Lease Information, Default Spreads and Ratios, Optimal Capital Structure, Summary Table

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
| Lambda of the stock |
| Book value of debt: |
| Can you estimate the market value of the outstanding debt? |
| If so, enter the market value of debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the average maturity of outstanding debt? |
| Do you have any operating leases? |
| General Market Data |
| Current long-term (LT) government bond rate: |
| Mature Market Premioum |
| Country Risk Premium (for use with lambda) |
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

| Tata Chemicals |
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
| Beta |
| Lambda |
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

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Firm Value (G) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.9383696611843447 | 0.1184001686912886 | AAA | 0.08499999999999999 | 0.3399 | 0.0561085 | 0.1184001686912886 | 102600.87869344465 |
| 0.1 | 1.007193862667432 | 0.12341694106385744 | AAA | 0.08499999999999999 | 0.3399 | 0.0561085 | 0.11668609695747169 | 105374.57320550145 |
| 0.2 | 1.093224114521291 | 0.1296879065295685 | A+ | 0.09 | 0.3399 | 0.059409 | 0.11563212522365479 | 107152.03102498155 |
| 0.3 | 1.203834438333396 | 0.13775057641405417 | A- | 0.095 | 0.3399 | 0.0627095 | 0.1152382534898379 | 107831.01281674615 |
| 0.4 | 1.3513148700828685 | 0.14850080292670165 | B+ | 0.1225 | 0.3399 | 0.08086225 | 0.12144538175602099 | 98001.40163712655 |
| 0.5 | 1.5577874745321305 | 0.1635511200444082 | B- | 0.135 | 0.3399 | 0.08911350000000001 | 0.1263323100222041 | 91387.22934061837 |
| 0.6 | 1.8674963812060235 | 0.186126595720968 | CC | 0.18000000000000002 | 0.3399 | 0.11881800000000002 | 0.1457414382883872 | 71784.35375644176 |
| 0.7 | 2.458425062834004 | 0.2292009012743464 | CC | 0.18000000000000002 | 0.3057615330716323 | 0.1249629240471062 | 0.15623431721527825 | 64169.66792655178 |
| 0.8 | 3.817802071405084 | 0.32828937413051934 | C | 0.19999999999999998 | 0.23286298318017884 | 0.1534274033639642 | 0.18839979751727523 | 48021.92371107891 |
| 0.9 | 7.704114123178748 | 0.6115726162515418 | C | 0.19999999999999998 | 0.1988771421731187 | 0.16022457156537626 | 0.2053593760339928 | 42200.03045800513 |
