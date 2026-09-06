---
title: "Embraercapstr"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/country/Embraercapstr.xls
---

# Embraercapstr

Source: https://www.stern.nyu.edu/~adamodar/pc/country/Embraercapstr.xls

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
| Country Default Spread (to use for cost of debt) |
| Risk premium (for use in the CAPM) |
|  |
| General Data |
| Which spread/ratio table would you like to use for your anlaysis? |
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
| 2.5 |
| 3 |
| 4.25 |
| 5.5 |
| 6.5 |
| 8.5 |
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
| 4.5 |
| 6 |
| 7.5 |
| 9.5 |
| 12.5 |

## Optimal Capital Structure

| Embraer |
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
| Beta |
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

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Firm Value (G) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.8657673827831354 | 0.1742640108462852 | AAA | 0.10669999999999999 | 0.33 | 0.07148899999999998 | 0.1742640108462852 | 9265.440886505967 |
| 0.1 | 0.9302189546125467 | 0.1834403316537309 | AA | 0.10969999999999999 | 0.33 | 0.07349899999999998 | 0.1724461984883578 | 9424.254222188323 |
| 0.2 | 1.0107834193993106 | 0.194910732663038 | A- | 0.1172 | 0.33 | 0.078524 | 0.1716333861304304 | 9496.939018929377 |
| 0.3 | 1.1143663026965784 | 0.20965839110357568 | BB | 0.12469999999999999 | 0.33 | 0.08354899999999998 | 0.17182557377250296 | 9479.657481221702 |
| 0.4 | 1.2524768137596025 | 0.22932193569095927 | B- | 0.1472 | 0.33 | 0.09862399999999999 | 0.17704276141457556 | 9032.209121594584 |
| 0.5 | 1.445831529247836 | 0.2568508981132963 | CCC | 0.1547 | 0.33 | 0.10364899999999999 | 0.18024994905664815 | 8776.41705697179 |
| 0.6 | 1.7594953161162379 | 0.3015089173405214 | CCC | 0.1547 | 0.3118028767649774 | 0.106464094964458 | 0.18448202391488333 | 8459.05576357993 |
| 0.7 | 2.3784370255151583 | 0.3896310146818547 | CC | 0.16469999999999999 | 0.2511995685743177 | 0.12332743105580987 | 0.2032185061436233 | 7279.348010885782 |
| 0.8 | 3.6305399688516733 | 0.5678997204073487 | C | 0.1797 | 0.20164104092811486 | 0.14346510494521775 | 0.22835202803764393 | 6109.234441578469 |
| 0.9 | 7.262465660442654 | 1.0849967336974793 | C | 0.1797 | 0.17905863952914391 | 0.14752316247661285 | 0.2412705195986995 | 5634.054136547211 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Debt Ratio | Cost of Capital | Bond Rating |  |  |  |  |  |  |
| 0 | 0.1742640108462852 | AAA |  |  |  |  |  |  |
| 0.1 | 0.1724461984883578 | AA |  |  |  |  |  |  |
| 0.2 | 0.1716333861304304 | A- |  |  |  |  |  |  |
| 0.3 | 0.17182557377250296 | BB |  |  |  |  |  |  |
| 0.4 | 0.17704276141457556 | B- |  |  |  |  |  |  |
| 0.5 | 0.18024994905664815 | CCC |  |  |  |  |  |  |
| 0.6 | 0.18448202391488333 | CCC |  |  |  |  |  |  |
| 0.7 | 0.2032185061436233 | CC |  |  |  |  |  |  |
| 0.8 | 0.22835202803764393 | C |  |  |  |  |  |  |
| 0.9 | 0.2412705195986995 | C |  |  |  |  |  |  |
