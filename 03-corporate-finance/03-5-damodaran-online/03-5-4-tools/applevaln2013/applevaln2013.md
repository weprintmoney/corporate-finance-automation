---
title: "Applevaln2013"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/webcasts/valuation/applevaln2013.xls
---

# Applevaln2013

Source: https://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/webcasts/valuation/applevaln2013.xls

Sheets: Input sheet, Valuation output, Option value, Diagnostics, R& D converter, Operating lease converter, Cost of capital worksheet, Synthetic rating, Industry Averages, Country tax rates, Country equity risk premiums, Traiing 12 month, Answer keys

## Input sheet

| Date of valuation | 39903.0 | Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |
|---|---|---|
| Company name | Apple | There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |
| Numbers from your base year below ( in consistent units) |  |  |
|  | This year | Last year |
| Industry | Computers/Peripherals |  |
| Revenues | 169104 | 156508 |
| Operating income or EBIT | 52285 | 55241 |
| Book value of equity | 135490 | 118210 |
| Book value of debt | 0 | 0 |
| Do you have R&D expenses to capitalize? | No |  If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |
| Do you have operating lease commitments? | Yes | If you have operating leases, please enter your lease commitments in the lease worksheet below and I will convert to debt |
| Cash and cross holdings | 144687 | 121251 |
| Non-operating assets  | 0 | 0 |
| Minority interests | 0 | 0 |
| Number of shares outstanding = | 939.629 |  |
| Current stock price = | 418 |  |
| Effective tax rate = | 0.2601 |  |
| Marginal tax rate = | 0.38 |  |
| The value drivers below: |  |  |
| Compounded annual revenue growth rate over next 5 years = | 0.05 |  |
| Target pre-tax operating margin (EBIT as % of sales in year 10) = | 0.25 |  |
| Sales to capital ratio  (for computing reinvestment) = | 2.66 |  |
| Market numbers  |  |  |
| Riskfree rate | 0.0175 |  |
| Initial cost of capital = | 0.11707270010102377 |  |
| Other inputs |  |  |
| Do you have employee options outstanding? | Yes |  |
| Number of options outstanding = | 5.215 |  |
| Average strike price = | 133.78 |  |
| Average maturity = | 1.5 |  |
| Standard deviation on stock price = | 0.4 |  |
|  |  |  |
| Default assumptions.  |  |  |
| In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%) |  |  |
| Do you want to override this assumption = | Yes | Mature companies generally see their risk levels approach the average |
| If yes, enter the cost of capital after year 10 = | 0.08 | Though some sectors, even in stable growth, may have higher risk. |
| I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time. |  |  |
| Do you want to override this assumption = | Yes | Mature companies find it difficult to generate returns that exceed the cost of capital |
| If yes, enter the return on capital you expect after year 10 | 0.12 | But there are significant exceptions among companies with long-lasting competitive advantages. |
| I will assume that your firm has no chance of failure over the foreseeable future. |  |  |
| Do you want to override this assumption = | No | Many young, growth companies fail, especially if they have trouble raising cash. Many distressed companies fail, because they have trouble making debt payments. |
| If yes, enter the probability of failure = | 0.2 | Tough to estimate but a key input. |
| What do you want to tie your proceeds in failure to? | V | B: Book value of capital, V= Estimated fair value for the company |
| Enter the distress proceeds as percentage of book or fair value | 0.5 | This can be zero, if the assets will be worth nothing if the firm fails. |
| I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year. If you override this assumption, I will leave the tax rate at your effective tax rate. |  |  |
| Do you want to override this assumption = | No |  |
| I will assume that you have no losses carried forward from prior years ( NOL) coming into the valuation. If you have a money losing company, you may want to override tis. |  |  |
| Do you want to override this assumption = | No | Check the financial statements. |
| If yes, enter the NOL that you are carrying over into year 1 | 250 | An NOL will shield your income from taxes, even after you start making money. |
| I have assumed that none of the cash is trapped (in foreign countries) and that there is no additional tax liability coming due |  |  |
| Do you want to override this assumption | Yes |  |
| If yes, enter the amount of trapped cash | 100000 |  |
| & Average tax rate of the foreign markets where the cash is trapped | 0.2 |  |

## Valuation output

| Base year | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 | 7.0 | 8.0 | 9.0 | 10.0 | Terminal year |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.043500000000000004 | 0.037000000000000005 | 0.0305 | 0.024 | 0.0175 | 0.0175 |
| 169104 | 177559.2 | 186437.16000000003 | 195759.01800000004 | 205546.96890000004 | 215824.31734500005 | 225212.67514950756 | 233545.5441300393 | 240668.6832260055 | 246444.73162342963 | 250757.51442683965 | 255145.77092930936 |
| 0.30920792685681747 | 0.30328713417113573 | 0.297366341485454 | 0.29144554879977225 | 0.28552475611409045 | 0.27960396342840876 | 0.27368317074272697 | 0.2677623780570452 | 0.2618415853713635 | 0.25592079268568174 | 0.25 | 0.25 |
| 52288.29726319526 | 53851.42091371953 | 55440.13618613823 | 57053.0944335145 | 58688.748165163044 | 60345.33453389268 | 61636.91902636898 | 62534.71028088593 | 63017.06956513575 | 63070.33107027821 | 62689.37860670991 | 63786.44273232734 |
| 0.2601 | 0.2601 | 0.2601 | 0.2601 | 0.2601 | 0.2601 | 0.28408 | 0.30806 | 0.33204 | 0.35602 | 0.38 | 0.38 |
| 38688.11114503817 | 39844.66633406108 | 41020.156764123676 | 42213.58457135738 | 43423.80476740414 | 44649.513021627194 | 44127.10306935808 | 43270.267431756205 | 42092.881786728074 | 40616.031802637764 | 38867.41473616015 | 39547.594494042954 |
|  | 3178.6466165413576 | 3337.5789473684285 | 3504.4578947368445 | 3679.6807894736826 | 3863.6648289473724 | 3529.4578212434253 | 3132.6575114781035 | 2677.8718405887894 | 2171.4467659489233 | 1621.346918575197 | 5767.357530381265 |
|  | 36666.019717519725 | 37682.57781675525 | 38709.12667662054 | 39744.12397793045 | 40785.84819267982 | 40597.645248114655 | 40137.609920278104 | 39415.00994613928 | 38444.58503668884 | 37246.06781758495 | 33780.23696366169 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | 0.11707270010102377 | 0.11707270010102377 | 0.11707270010102377 | 0.11707270010102377 | 0.11707270010102377 | 0.10965816008081902 | 0.10224362006061427 | 0.09482908004040952 | 0.08741454002020477 | 0.08000000000000002 | 0.08 |
|  | 0.8951968837028816 | 0.8013774605913506 | 0.7173906053911059 | 0.6422058343438417 | 0.5749006616004161 | 0.5180880763843027 | 0.47003046055808617 | 0.4293185750425424 | 0.3948067266367115 | 0.36556178392288097 |  |
|  | 32823.30658891207 | 30197.96851932728 | 27769.563820701813 | 25523.90829951191 | 23447.811109905764 | 21033.15593232805 | 18865.899276529126 | 16921.595905364153 | 15178.18077524182 | 13615.738995508962 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
| 33780.23696366169 |  |  |  |  |  |  |  |  |  |  |  |
| 0.08 |  |  |  |  |  |  |  |  |  |  |  |
| 540483.7914185871 |  |  |  |  |  |  |  |  |  |  |  |
| 197580.218972381 |  |  |  |  |  |  |  |  |  |  |  |
| 225377.12922333094 |  |  |  |  |  |  |  |  |  |  |  |
| 422957.34819571197 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 211478.67409785598 |  |  |  |  |  |  |  |  |  |  |  |
| 422957.34819571197 |  |  |  |  |  |  |  |  |  |  |  |
| 3877.621894437937 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 144687 |  |  |  |  |  |  |  |  |  |  |  |
| 18000 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 545766.726301274 |  |  |  |  |  |  |  |  |  |  |  |
| 1498.2217709075587 |  |  |  |  |  |  |  |  |  |  |  |
| 544268.5045303665 |  |  |  |  |  |  |  |  |  |  |  |
| 939.629 |  |  |  |  |  |  |  |  |  |  |  |
| 579.2376613858943 |  |  |  |  |  |  |  |  |  |  |  |
| 418 |  |  |  |  |  |  |  |  |  |  |  |
| 0.7216381597147634 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 | 2.66 |  |
| -5319.378105562063 | -2140.7314890207053 | 1196.8474583477232 | 4701.305353084568 | 8380.986142558251 | 12244.650971505624 | 15774.108792749048 | 18906.766304227152 | 21584.63814481594 | 23756.084910764865 | 25377.43182934006 |  |
| -7.27305154423691 | -18.61264083721604 | 34.2735045122233 | 8.979119925418305 | 5.181228560550901 | 3.64645044807978 | 2.7974387427606797 | 2.2886128032418687 | 1.9501314548021584 | 1.709710668033223 | 1.5315739984068708 | 0.12 |

## Option value

| Valuing Options or Warrants |
|---|
| Enter the current stock price = |
| Enter the strike price on the option = |
| Enter the expiration of the option = |
| Enter the standard deviation in stock prices = |
| Enter the annualized dividend yield on stock = |
| Enter the treasury bond rate = |
| Enter the number of warrants (options) outstanding = |
| Enter the number of shares outstanding = |
|  |
| Do not input any numbers below this line |
| VALUING WARRANTS WHEN THERE IS DILUTION |
| Stock Price= |
| Strike Price= |
| Adjusted S = |
| Adjusted K = |
| Expiration (in years) = |
|  |
|  |
| d1 =  |
| N (d1) = |
|  |
| d2 =  |
| N (d2) = |
|  |
| Value per option =  |
| Value of all options outstanding = |

## Diagnostics

| VALUATION DIAGNOSTICS |
|---|
| Invested capital at start of valuation |
| Invested capital at end of valuation |
| Change in invested capital over 10 years |
| Change in EBIT*(1–t) (after-tax operating income) over 10 years |
| Marginal ROIC over 10 years |
| ROIC at end of valuation |
| Average WACC over the 10 years (compounded) |
| Your calculated value as a percent of current price |
|  |
| Inputs |
| Revenue growth rate (input cell B3) |
| Last period EBIT as % of revenue (Input cell B14) |
| Sales to Capital Ratio or reinvestment (Input cell B15) |
| Return on capital in perpetuity (B30 & B31) |

## R& D converter

| R & D Converter |
|---|
| This spreadsheet converts R&D expenses from operating to capital expenses. It makes the appropriate adjustments to operating income, net |
| income, the book value of assets and the book value of equity. |
|  |
| Inputs |
| Over how many years do you want to amortize R&D expenses |
| Enter the current year's R&D expense = |
| Enter R& D expenses for past years: the number of years that you will need to enter will be determined by the amortization period |
| Do not input numbers in the first column (Year). It will get automatically updated  based on the input above. |
| Year |
| -1 |
| -2 |
| -3 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
|  |
| Output |
| Year |
| Current |
| -1 |
| -2 |
| -3 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| Value of Research Asset = |
|  |
| Amortization of asset for current year = |
|  |
| Adjustment to Operating Income = |
| Tax Effect of R&D Expensing |

## Operating lease converter

| Operating Lease Converter |
|---|
| The yellow cells are input cells. Please enter them. |
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
| Output |
| Pre-tax Cost of Debt = |
|  |
|  |
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
| Depreciation on Operating Lease Asset = |
| Adjustment to Operating Earnings = |
| Adjustment to Total Debt outstanding = |

## Cost of capital worksheet

| Estimation of Current Cost of Capital | If you are a multinational company and have a breakdown by country, you can use this table (for up to 10 countries) |
|---|---|
| Inputs | Country |
| Equity | Argentina |
| Number of Shares outstanding = | Bolivia |
| Current Market Price per share = | Brazil |
|  | Canada |
| Unlevered beta = | Chile |
| Riskfree Rate = | Ecuador |
| Equity Risk Premium = | Paraguay |
|  | Peru |
| Debt |  |
| Book Value of Straight Debt = |  |
| Interest Expense on Debt = | Total |
| Average Maturity = | If you are a multinational company and have a breakdown only by region, you can use this table instead |
| Pre-tax Cost of Debt = | Region |
| Tax Rate = | Africa |
|  | Australia & New Zealand |
| Book Value of Convertible Debt = | Caribbean |
| Interest Expense on Convertible = | Central and South America |
| Maturity of Convertible Bond = | Eastern Europe & Russia |
| Market Value of Convertible = | Middle East |
|  | North America |
| Debt value of operating leases = | Western Europe |
|  | Asia (w/o Japan) |
| Preferred Stock | Japan |
| Number of Preferred Shares = | Total |
| Current Market Price per Share= |  |
| Annual Dividend per Share = | If you are a multi-business company, you can input the following |
|  | Business |
| Output | Computers/Peripherals |
| Estimating Market Value of Straight Debt = | Entertainment Tech |
| Estimated Value of Straight Debt in Convertible = | Entertainment |
| Value of Debt in Operating leases = |  |
| Estimated Value of Equity in Convertible = |  |
| Levered Beta for equity = |  |
|  |  |
|  |  |
| Market Value |  |
| Weight in Cost of Capital |  |
| Cost of Component |  |
|  |  |
|  | Company |

## Synthetic rating

| Inputs for synthetic rating estimation |
|---|
| Please read the special cases worksheet (see below) before you use this spreadsheet. |
| Before you use this spreadsheet, make sure that the iteration box (under calculation options in excel) is checked. |
| Enter the type of firm = |
| Enter current Earnings before interest and taxes (EBIT) = |
| Enter current interest expenses = |
| Enter long term risk free rate  = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
|  |
|  If you want to update the spreads listed below, please visit http://www.bondsonline.com |
| For large manufacturing firms |
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

## Industry Averages

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 32 | 0.0867 | 0.1177 | 0.1149 | 0.1602 | 1.44 | 1.68 | 0.1151 | 0.974 | 0.0476 | 0.29 | 0.09 | 1.4 | 1.22 | 7.77 | 10.4 | 2.04 | 31.25 |
| Aerospace/Defense | 66 | 0.1256 | 0.1024 | 0.194 | 0.2008 | 0.92 | 0.98 | 0.0745 | 0.4498 | 0.0276 | 0.2103 | 0.0623 | 2.71 | 0.94 | 7.42 | 9.15 | 3.11 | 15.79 |
| Air Transport | 36 | 0.1321 | 0.0838 | 0.1797 | 0.2135 | 0.82 | 1.03 | 0.0773 | 0.6494 | 0.0326 | 0.3714 | 0.0559 | 2.74 | 0.78 | 6 | 9.32 | 3.68 | 14.6 |
| Apparel | 54 | 0.0769 | 0.1037 | 0.1386 | 0.1857 | 1.29 | 1.36 | 0.0968 | 0.7488 | 0.0376 | 0.1211 | 0.0878 | 1.89 | 1.52 | 11.73 | 14.68 | 3.38 | 21.64 |
| Auto Parts | 54 | 0.201 | 0.0672 | 0.1765 | 0.1877 | 1.66 | 1.76 | 0.1194 | 0.5743 | 0.0326 | 0.1959 | 0.0998 | 3.4 | 0.6 | 6.4 | 8.92 | 2.27 | 15.39 |
| Automotive | 12 | 0.4235 | 0.058 | 0.0577 | 0.1624 | 1.11 | 1.73 | 0.1179 | 0.5923 | 0.0326 | 0.5084 | 0.0679 | 1.41 | 0.81 | 7.46 | 13.95 | 1.26 | 15.84 |
| Bank | 416 | 0 | NA | NA | 0.1639 | 0.45 | 0.77 | 0.0624 | 0.5034 | 0.0326 | 0.5618 | 0.0383 | NA | NA | 4.87 | 4.87 | 0.98 | 16.58 |
| Bank (Midwest) | 68 | 0 | NA | NA | 0.2099 | 0.76 | 0.89 | 0.0695 | 0.3637 | 0.0276 | 0.3327 | 0.0519 | NA | NA | 4.79 | 4.79 | 1.32 | 16.43 |
| Beverage | 35 | 0.0262 | 0.2074 | 0.1456 | 0.1882 | 0.84 | 0.95 | 0.0726 | 0.4717 | 0.0276 | 0.1822 | 0.0624 | 0.93 | 3.23 | 12.74 | 15.58 | 4.54 | 19.92 |
| Biotechnology | 214 | 0.2093 | 0.1854 | 0.1457 | 0.0298 | 1.3 | 1.23 | 0.0889 | 0.7999 | 0.0376 | 0.1373 | 0.0798 | 0.99 | 5.7 | 22.46 | 30.77 | 4.56 | 31.24 |
| Building Materials | 43 | 0.0128 | 0.043 | 0.0298 | 0.0948 | 1.05 | 1.57 | 0.1087 | 0.7976 | 0.0376 | 0.3948 | 0.0747 | 0.88 | 1.54 | 14.45 | 35.82 | 1.67 | 29.27 |
| Cable TV | 20 | 0.0908 | 0.1919 | 0.1052 | 0.2123 | 0.96 | 1.4 | 0.099 | 0.4045 | 0.0276 | 0.398 | 0.0662 | 0.8 | 2.37 | 7.08 | 12.35 | 4.09 | 22.28 |
| Chemical (Basic) | 18 | 0.1873 | 0.1484 | 0.1775 | 0.2189 | 1.24 | 1.37 | 0.0973 | 0.3924 | 0.0276 | 0.1983 | 0.0813 | 1.56 | 1.44 | 7.44 | 9.69 | 2.77 | 31.77 |
| Chemical (Diversified) | 33 | 0.157 | 0.1502 | 0.1812 | 0.1975 | 1.47 | 1.55 | 0.1075 | 0.4902 | 0.0276 | 0.143 | 0.0945 | 1.63 | 1.67 | 8.53 | 11.11 | 3.18 | 19.75 |
| Chemical (Specialty) | 70 | 0.254 | 0.1116 | 0.1248 | 0.1535 | 1.05 | 1.18 | 0.0859 | 0.629 | 0.0326 | 0.1703 | 0.0746 | 1.58 | 1.7 | 10.86 | 15.23 | 3.6 | 17.57 |
| Coal | 20 | 0.0708 | 0.1419 | 0.101 | 0.1127 | 0.99 | 1.47 | 0.1028 | 0.5654 | 0.0326 | 0.4061 | 0.069 | 0.9 | 1.32 | 5.99 | 9.34 | 1.33 | 29.76 |
| Computer Software | 191 | 0.1481 | 0.2999 | 0.4331 | 0.1243 | 1.11 | 0.98 | 0.0742 | 0.6839 | 0.0376 | 0.0615 | 0.071 | 1.87 | 3.33 | 9.7 | 11.11 | 3.94 | 77.29 |
| Computers/Peripherals | 81 | 0.0389 | 0.1694 | 0.3466 | 0.1001 | 1.39 | 1.37 | 0.0968 | 0.8183 | 0.0426 | 0.0884 | 0.0905 | 2.66 | 1.38 | 6.92 | 8.14 | 3.57 | 46.69 |
| Diversified Co. | 113 | 0.1736 | 0.1491 | 0.0921 | 0.1718 | 0.86 | 1.22 | 0.0882 | 0.6046 | 0.0326 | 0.4404 | 0.058 | 0.84 | 1.92 | 10.09 | 12.87 | 2.38 | 16.19 |
| Drug | 223 | 0.2019 | 0.2524 | 0.1694 | 0.0514 | 1.03 | 1.08 | 0.08 | 0.8068 | 0.0426 | 0.1289 | 0.073 | 0.9 | 3.05 | 8.93 | 12.1 | 3.04 | 28.46 |
| E-Commerce | 64 | 0.1567 | 0.0824 | 0.0546 | 0.1052 | 1.09 | 1.05 | 0.0786 | 0.806 | 0.0426 | 0.0631 | 0.0753 | 1.17 | 5.07 | 32.19 | 61.51 | 5.15 | 237.12 |
| Educational Services | 33 | 0.1029 | 0.1869 | 0.4233 | 0.2172 | 1.09 | 0.91 | 0.0701 | 0.8308 | 0.0426 | 0.1983 | 0.0613 | 3.42 | 0.54 | 2.41 | 2.91 | 1.67 | 13.29 |
| Electric Util. (Central) | 20 | 0.0405 | 0.1755 | 0.0647 | 0.3012 | 0.36 | 0.57 | 0.0508 | 0.1729 | 0.0226 | 0.4595 | 0.0337 | 0.54 | 2.27 | 7.98 | 12.94 | 1.49 | 15.66 |
| Electric Utility (East) | 17 | 0.015 | 0.2051 | 0.0669 | 0.3349 | 0.3 | 0.43 | 0.0424 | 0.1321 | 0.0226 | 0.4044 | 0.0307 | 0.49 | 2.78 | 8.96 | 13.54 | 1.79 | 17.08 |
| Electric Utility (West) | 15 | 0.0283 | 0.1644 | 0.0617 | 0.2909 | 0.38 | 0.58 | 0.0514 | 0.1419 | 0.0226 | 0.4487 | 0.0344 | 0.54 | 2.26 | 7.87 | 13.74 | 1.44 | 16.05 |
| Electrical Equipment | 64 | 0.0911 | 0.1377 | 0.1598 | 0.1615 | 1.45 | 1.43 | 0.1003 | 0.6779 | 0.0376 | 0.1094 | 0.0918 | 1.58 | 1.49 | 8.57 | 10.8 | 2.34 | 22.95 |
| Electronics | 123 | 0.0354 | 0.0639 | 0.146 | 0.1131 | 1.17 | 1.22 | 0.0881 | 0.7424 | 0.0376 | 0.1834 | 0.0761 | 3.03 | 0.59 | 6.63 | 9.28 | 1.9 | 15.11 |
| Engineering & Const | 30 | 0.0858 | 0.0483 | 0.1316 | 0.25 | 1.4 | 1.28 | 0.0919 | 0.4603 | 0.0276 | 0.1168 | 0.0831 | 3.96 | 0.5 | 7.98 | 10.42 | 1.89 | 44.34 |
| Entertainment | 76 | 0.1073 | 0.1912 | 0.1041 | 0.1256 | 1.31 | 1.6 | 0.1105 | 0.7099 | 0.0376 | 0.253 | 0.0883 | 0.79 | 2.34 | 9.53 | 12.22 | 2.38 | 27.83 |
| Entertainment Tech | 42 | 0.0607 | 0.173 | 0.1951 | 0.1101 | 1.33 | 1.11 | 0.082 | 0.5325 | 0.0326 | 0.1035 | 0.0756 | 1.34 | 1.79 | 7.97 | 10.37 | 1.97 | 20.13 |
| Environmental | 84 | 0.2011 | 0.1465 | 0.089 | 0.076 | 0.49 | 0.66 | 0.0562 | 0.7924 | 0.0376 | 0.3011 | 0.046 | 0.9 | 1.87 | 8.44 | 12.78 | 2.29 | 16.99 |
| Financial Svcs. (Div.) | 256 | 0.0586 | 0.6183 | 0.0733 | 0.1623 | 0.56 | 1.34 | 0.0953 | 0.5515 | 0.0326 | 0.6715 | 0.0444 | 0.15 | 8.15 | 12.56 | 13.19 | 1.98 | 22.15 |
| Food Processing | 119 | 0.1461 | 0.0973 | 0.1356 | 0.2163 | 0.77 | 0.87 | 0.0683 | 0.5226 | 0.0326 | 0.1903 | 0.059 | 1.84 | 1.22 | 10.1 | 12.53 | 2.93 | 24.85 |
| Foreign Electronics | 10 | -0.0459 | 0.0341 | 0.0544 | 0.2312 | 1.12 | 1.1 | 0.0813 | 0.3124 | 0.0276 | 0.3137 | 0.061 | 2.3 | 0.39 | 4.44 | 11.52 | 0.9 | 31.52 |
| Funeral Services | 6 | 0.0891 | 0.1437 | 0.0828 | 0.2866 | 0.85 | 1.12 | 0.0826 | 0.2675 | 0.0276 | 0.331 | 0.0607 | 0.85 | 1.84 | 9.73 | 12.8 | 2.09 | 17.8 |
| Furn/Home Furnishings | 32 | 0.0278 | 0.0848 | 0.1406 | 0.1669 | 1.47 | 1.63 | 0.112 | 0.556 | 0.0326 | 0.1807 | 0.0953 | 2 | 0.95 | 8.34 | 11.22 | 2.18 | 21.64 |
| Healthcare Information | 20 | 0.2068 | 0.1653 | 0.1168 | 0.2031 | 0.98 | 0.97 | 0.0736 | 0.4441 | 0.0276 | 0.1041 | 0.0677 | 1.07 | 3.6 | 14.37 | 21.77 | 3.89 | 54.59 |
| Heavy Truck & Equip | 23 | 0.271 | 0.1112 | 0.1521 | 0.2274 | 1.45 | 1.8 | 0.1222 | 0.5526 | 0.0326 | 0.3211 | 0.0892 | 1.85 | 1.12 | 7.96 | 10.05 | 3.23 | 16.08 |
| Homebuilding | 22 | 0.1134 | 0.0944 | 0.0768 | 0.0712 | 1.25 | 1.55 | 0.1073 | 0.6675 | 0.0376 | 0.3314 | 0.0792 | 0.88 | 2.19 | 21.15 | 23.16 | 2.54 | 49.55 |
| Hotel/Gaming | 57 | 0.1427 | 0.1555 | 0.1021 | 0.1752 | 1.29 | 1.65 | 0.1133 | 0.5566 | 0.0326 | 0.3091 | 0.0843 | 0.82 | 2.43 | 10.68 | 15.66 | 3.07 | 35.36 |
| Household Products | 27 | 0.1301 | 0.1656 | 0.1481 | 0.2466 | 0.88 | 0.98 | 0.0742 | 0.5086 | 0.0326 | 0.1533 | 0.0658 | 1.23 | 2.24 | 11.12 | 13.5 | 3.75 | 18.49 |
| Human Resources | 25 | 0.1617 | 0.0305 | 0.1219 | 0.2661 | 1.46 | 1.38 | 0.0976 | 0.5164 | 0.0326 | 0.0975 | 0.09 | 6.81 | 0.34 | 8.69 | 11.06 | 2.21 | 30.55 |
| Industrial Services | 136 | 0.0841 | 0.079 | 0.0995 | 0.2019 | 0.83 | 0.97 | 0.0738 | 0.5724 | 0.0326 | 0.2677 | 0.0592 | 1.85 | 0.99 | 8.87 | 12.52 | 2.29 | 34.78 |
| Information Services | 28 | 0.0856 | 0.2035 | 0.1271 | 0.1833 | 1.05 | 1.25 | 0.09 | 0.4875 | 0.0276 | 0.2215 | 0.0737 | 0.79 | 3.16 | 10.89 | 15.55 | 3.9 | 31.49 |
| Insurance (Life) | 32 | 0 | NA | NA | 0.2109 | 1.41 | 1.44 | 0.1011 | 0.422 | 0.0276 | 0.3584 | 0.0708 | NA | NA | 1.37 | 1.37 | 0.72 | 20.4 |
| Insurance (Prop/Cas.) | 62 | 0.0217 | NA | NA | 0.1073 | 0.9 | 0.85 | 0.0669 | 0.2857 | 0.0276 | 0.1768 | 0.058 | NA | NA | 291.86 | 295.89 | 1.11 | 16.65 |
| Internet | 194 | 0.1168 | 0.1312 | 0.2154 | 0.0843 | 1.31 | 1.17 | 0.0856 | 0.9781 | 0.0476 | 0.0224 | 0.0843 | 2.4 | 4.15 | 23.16 | 31.64 | 5.25 | 181.13 |
| Investment Companies | 31 | 0.4277 | 0.269 | 0.0587 | 0.0226 | 1.21 | 1.27 | 0.0911 | 0.241 | 0.0226 | 0.0702 | 0.0857 | 0.26 | 4.89 | 15.67 | 18.19 | 1.31 | 64.45 |
| IT Services | 63 | 0.0633 | 0.1119 | 0.2177 | 0.1627 | 1.11 | 1.05 | 0.0783 | 0.5611 | 0.0326 | 0.0541 | 0.0751 | 2.98 | 1.79 | 12.22 | 16.02 | 4.36 | 39.49 |
| Machinery | 94 | 0.1769 | 0.1195 | 0.1343 | 0.2273 | 1.18 | 1.26 | 0.0907 | 0.4507 | 0.0276 | 0.1481 | 0.0797 | 1.53 | 1.55 | 9.93 | 12.94 | 2.76 | 21.3 |
| Maritime | 51 | 0.0035 | 0.1218 | 0.0354 | 0.0792 | 0.6 | 1.51 | 0.1053 | 0.6252 | 0.0326 | 0.6444 | 0.05 | 0.36 | 2.64 | 10.36 | 21.66 | 0.85 | 22.57 |
| Med Supp Invasive | 87 | 0.0709 | 0.2119 | 0.1491 | 0.126 | 0.82 | 0.87 | 0.0678 | 0.5549 | 0.0326 | 0.1415 | 0.061 | 0.92 | 2.71 | 10.16 | 12.81 | 2.82 | 46.69 |
| Med Supp Non-Invasive | 143 | 0.0896 | 0.0643 | 0.1994 | 0.1061 | 1.1 | 1.07 | 0.0794 | 0.6773 | 0.0376 | 0.1142 | 0.0729 | 4.21 | 0.78 | 9.78 | 12.07 | 3.11 | 35.61 |
| Medical Services | 118 | 0.0457 | 0.1005 | 0.1444 | 0.1772 | 0.66 | 0.84 | 0.0662 | 0.7416 | 0.0376 | 0.3344 | 0.0516 | 2.19 | 0.74 | 6.02 | 7.32 | 2.03 | 29.94 |
| Metal Fabricating | 25 | 0.1943 | 0.1466 | 0.1439 | 0.233 | 1.56 | 1.63 | 0.1119 | 0.6059 | 0.0326 | 0.1909 | 0.0942 | 1.38 | 1.28 | 6.9 | 8.75 | 1.9 | 63.26 |
| Metals & Mining (Div.) | 77 | 0.2171 | 0.3497 | 0.2519 | 0.1124 | 1.54 | 1.62 | 0.1114 | 0.9305 | 0.0476 | 0.1336 | 0.1003 | 0.99 | 2.18 | 5.27 | 6.24 | 2.35 | 36.66 |
| Natural Gas (Div.) | 31 | 0.1177 | 0.2813 | 0.0736 | 0.2202 | 1.01 | 1.28 | 0.0916 | 0.4457 | 0.0276 | 0.2912 | 0.0697 | 0.43 | 2.89 | 5.41 | 10.26 | 1.35 | 53.21 |
| Natural Gas Utility | 27 | 0.0045 | 0.0726 | 0.0704 | 0.288 | 0.32 | 0.46 | 0.044 | 0.2844 | 0.0276 | 0.3982 | 0.0331 | 1.4 | 1.03 | 9.89 | 14.2 | 1.99 | 23.01 |
| Newspaper | 14 | -0.0665 | 0.123 | 0.1099 | 0.1835 | 1.5 | 1.86 | 0.1256 | 0.5439 | 0.0326 | 0.2821 | 0.0957 | 1.22 | 1.57 | 8.72 | 12.77 | 2.7 | 115.92 |
| Office Equip/Supplies | 22 | 0.1217 | 0.0659 | 0.1089 | 0.2266 | 1.05 | 1.43 | 0.1003 | 0.5192 | 0.0326 | 0.4191 | 0.0665 | 2.34 | 0.46 | 4.76 | 6.94 | 1.11 | 21.17 |
| Oil/Gas Distribution | 12 | 0.0828 | 0.1929 | 0.0762 | 0.1811 | 0.72 | 1.02 | 0.0765 | 0.3563 | 0.0276 | 0.3481 | 0.0556 | 0.56 | 3.42 | 12.02 | 17.73 | 3.56 | 37.3 |
| Oilfield Svcs/Equip. | 81 | 0.2677 | 0.1651 | 0.095 | 0.182 | 1.45 | 1.66 | 0.1139 | 0.5958 | 0.0326 | 0.217 | 0.0934 | 0.79 | 2 | 7.98 | 12.13 | 1.79 | 14.61 |
| Packaging & Container | 27 | 0.105 | 0.0963 | 0.1111 | 0.2309 | 0.88 | 1.2 | 0.0872 | 0.3652 | 0.0276 | 0.3597 | 0.0618 | 1.56 | 1.08 | 7.57 | 11.2 | 2.49 | 17.22 |
| Paper/Forest Products | 32 | 0.0615 | 0.104 | 0.1116 | 0.1143 | 1.07 | 1.37 | 0.0973 | 0.5228 | 0.0326 | 0.3007 | 0.0739 | 1.32 | 1.18 | 7.22 | 11.38 | 1.92 | 29.45 |
| Petroleum (Integrated) | 26 | 0.2494 | 0.1199 | 0.1465 | 0.3034 | 1.1 | 1.17 | 0.0855 | 0.4725 | 0.0276 | 0.1699 | 0.0738 | 2.03 | 0.7 | 4.39 | 5.81 | 1.49 | 11.29 |
| Petroleum (Producing) | 176 | 0.3294 | 0.2176 | 0.1499 | 0.1171 | 1.21 | 1.45 | 0.1018 | 0.7126 | 0.0376 | 0.2195 | 0.0844 | 1.07 | 1.26 | 4.06 | 5.77 | 1.47 | 24.25 |
| Pharmacy Services | 18 | 0.1676 | 0.0548 | 0.1153 | 0.2318 | 1.07 | 1.17 | 0.0853 | 0.4223 | 0.0276 | 0.1588 | 0.0744 | 3.34 | 0.66 | 9.57 | 11.98 | 2.58 | 19.67 |
| Pipeline MLPs | 53 | 0.2021 | 0.0899 | 0.095 | 0.043 | 0.52 | 0.74 | 0.0605 | 0.2488 | 0.0226 | 0.3073 | 0.0461 | 1.1 | 1.7 | 13.43 | 18.87 | 2.96 | 130.5 |
| Power | 101 | 0.0817 | 0.0697 | 0.0262 | 0.0619 | 0.58 | 1.35 | 0.0961 | 0.8463 | 0.0426 | 0.6204 | 0.0523 | 0.61 | 1.51 | 8.92 | 21.7 | 0.82 | 304.86 |
| Precious Metals | 83 | 0.2817 | 0.3911 | 0.1191 | 0.1113 | 1 | 1.03 | 0.0775 | 0.7777 | 0.0376 | 0.1201 | 0.0709 | 0.43 | 3.64 | 7.17 | 9.3 | 1.61 | 24.6 |
| Precision Instrument | 82 | 0.105 | 0.0702 | 0.0578 | 0.1413 | 1.21 | 1.27 | 0.0912 | 0.6011 | 0.0326 | 0.175 | 0.0786 | 1.23 | 1.89 | 14.89 | 26.86 | 2.57 | 23.56 |
| Property Management | 31 | 0.1432 | 0.1368 | 0.0472 | 0.165 | 0.73 | 1.3 | 0.093 | 0.5063 | 0.0326 | 0.5296 | 0.0541 | 0.4 | 3.12 | 15.96 | 22.79 | 1.66 | 44.26 |
| Public/Private Equity | 12 | -0.0837 | 0.3825 | 0.0883 | 0.1917 | 1.94 | 2.02 | 0.1348 | 0.42 | 0.0276 | 0.2232 | 0.1084 | 0.28 | 4 | 10.3 | 10.45 | 1.12 | 8.65 |
| Publishing | 29 | 0.0627 | 0.1007 | 0.112 | 0.2269 | 0.96 | 1.17 | 0.0856 | 0.6572 | 0.0376 | 0.2655 | 0.0688 | 1.66 | 1.32 | 8.76 | 13.14 | 3.37 | 14.22 |
| R.E.I.T. | 127 | 0.0001 | 1.6163 | 0.1458 | 0.0004 | 1.12 | 1.43 | 0.1004 | 0.3476 | 0.0276 | 0.2701 | 0.0778 | 0.09 | 13.11 | 7.25 | 8.11 | 1.29 | 16.85 |
| Railroad | 12 | 0.4426 | 0.2808 | 0.1237 | 0.286 | 1.15 | 1.32 | 0.094 | 0.3573 | 0.0276 | 0.19 | 0.0793 | 0.67 | 3.32 | 9.13 | 11.81 | 2.99 | 17.5 |
| Recreation | 51 | 0.0539 | 0.1154 | 0.0909 | 0.2031 | 1.18 | 1.45 | 0.1014 | 0.523 | 0.0326 | 0.2741 | 0.079 | 0.96 | 1.7 | 9.89 | 14.69 | 2.01 | 24.73 |
| Reinsurance | 11 | 0 | NA | NA | 0.0358 | 0.91 | 0.82 | 0.0649 | 0.2074 | 0.0226 | 0.159 | 0.0567 | NA | NA | 28.62 | 28.62 | 0.82 | 8.25 |
| Restaurant | 65 | 0.0661 | 0.1678 | 0.2141 | 0.1923 | 1.08 | 1.16 | 0.0848 | 0.5092 | 0.0326 | 0.1162 | 0.0772 | 1.83 | 2.46 | 11.5 | 14.65 | 6.65 | 19.52 |
| Retail (Hardlines) | 79 | 0.0837 | 0.0822 | 0.1489 | 0.2255 | 1.65 | 1.79 | 0.1214 | 0.6349 | 0.0326 | 0.2064 | 0.1003 | 2.61 | 0.87 | 7.65 | 10.61 | 2.76 | 22.74 |
| Retail (Softlines) | 42 | 0.0979 | 0.0937 | 0.3003 | 0.2557 | 1.51 | 1.43 | 0.1005 | 0.4254 | 0.0276 | 0.0529 | 0.096 | 5.17 | 1.14 | 9.02 | 12.12 | 4.94 | 18.19 |
| Retail Automotive | 19 | 0.223 | 0.0678 | 0.0957 | 0.3269 | 1.1 | 1.39 | 0.0982 | 0.642 | 0.0326 | 0.3071 | 0.074 | 2.17 | 0.93 | 11.03 | 13.74 | 3.46 | 15.97 |
| Retail Building Supply | 10 | 0.0508 | 0.0835 | 0.1354 | 0.2556 | 1.04 | 1.11 | 0.0822 | 0.3182 | 0.0276 | 0.1049 | 0.0753 | 2.55 | 1.31 | 12.23 | 15.74 | 4.32 | 25.76 |
| Retail Store | 38 | 0.1635 | 0.0524 | 0.1285 | 0.2483 | 1.14 | 1.29 | 0.0926 | 0.6315 | 0.0326 | 0.2037 | 0.0777 | 3.61 | 0.61 | 8.39 | 11.67 | 2.9 | 20.34 |
| Retail/Wholesale Food | 30 | 0.0891 | 0.0334 | 0.1126 | 0.3118 | 0.58 | 0.68 | 0.0569 | 0.2993 | 0.0276 | 0.2584 | 0.0465 | 4.99 | 0.43 | 8.27 | 12.98 | 3.18 | 14.89 |
| Securities Brokerage | 27 | 0.0186 | 0.3282 | 0.0709 | 0.3041 | 0.66 | 1.07 | 0.0795 | 0.4056 | 0.0276 | 0.7257 | 0.0338 | 0.3 | 3.23 | 8.79 | 9.85 | 0.93 | 20.01 |
| Semiconductor | 142 | 0.0694 | 0.2038 | 0.2288 | 0.1171 | 1.6 | 1.49 | 0.1041 | 0.5365 | 0.0326 | 0.0914 | 0.0964 | 1.41 | 2.16 | 6.98 | 10.58 | 2.72 | 50.55 |
| Semiconductor Equip | 10 | -0.0575 | 0.118 | 0.1135 | 0.1521 | 2.01 | 1.79 | 0.1216 | 0.4044 | 0.0276 | 0.1452 | 0.1063 | 1.21 | 1.44 | 8.07 | 12.22 | 1.64 | 25.21 |
| Shoe | 17 | 0.1334 | 0.0837 | 0.1766 | 0.1989 | 1.37 | 1.26 | 0.0909 | 0.4732 | 0.0276 | 0.019 | 0.0894 | 3.24 | 1.42 | 14.09 | 16.98 | 3.66 | 13.75 |
| Steel | 33 | 0.2686 | 0.0819 | 0.0759 | 0.2424 | 1.27 | 1.65 | 0.1132 | 0.4566 | 0.0276 | 0.3598 | 0.0784 | 1.26 | 0.73 | 5.63 | 8.89 | 0.88 | 23.48 |
| Telecom. Equipment | 105 | 0.0106 | 0.149 | 0.2625 | 0.1401 | 1.37 | 1.07 | 0.0796 | 0.6486 | 0.0326 | 0.1175 | 0.0725 | 2.29 | 1.27 | 6.74 | 8.51 | 2.08 | 24.8 |
| Telecom. Services | 76 | 0.1934 | 0.2013 | 0.1366 | 0.1622 | 1 | 1.15 | 0.0843 | 0.6404 | 0.0326 | 0.2414 | 0.0686 | 0.9 | 1.91 | 5.39 | 9.47 | 2.02 | 18.25 |
| Telecom. Utility | 23 | 0.0046 | 0.1469 | 0.0749 | 0.2694 | 0.53 | 0.92 | 0.0708 | 0.4385 | 0.0276 | 0.5198 | 0.0426 | 0.72 | 1.77 | 5.08 | 12.05 | 1.77 | 16.7 |
| Thrift | 170 | 0 | NA | NA | 0.1584 | 0.78 | 0.68 | 0.0568 | 0.4173 | 0.0276 | 0.1632 | 0.0503 | NA | NA | 4.08 | 4.08 | 0.99 | 29.69 |
| Tobacco | 11 | 0.1351 | 0.2235 | 0.3197 | 0.3282 | 0.79 | 0.86 | 0.0675 | 0.3644 | 0.0276 | 0.1587 | 0.0594 | 2.1 | 2.3 | 9.48 | 10.3 | 11.46 | 19.42 |
| Toiletries/Cosmetics | 14 | 0.0953 | 0.1107 | 0.2144 | 0.2733 | 1.09 | 1.17 | 0.0852 | 0.401 | 0.0276 | 0.171 | 0.0735 | 2.83 | 1.37 | 10.1 | 12.39 | 6.04 | 20.39 |
| Trucking | 34 | 0.1505 | 0.0747 | 0.1197 | 0.2594 | 0.87 | 1.09 | 0.0808 | 0.4832 | 0.0276 | 0.2974 | 0.0617 | 2.44 | 0.82 | 6.19 | 10.96 | 3.07 | 16.7 |
| Water Utility | 11 | 0.0416 | 0.2621 | 0.0589 | 0.3145 | 0.33 | 0.49 | 0.0461 | 0.3724 | 0.0276 | 0.4226 | 0.0336 | 0.32 | 4.36 | 11.2 | 16.62 | 2 | 20.46 |
| Wireless Networking | 58 | 0.0659 | 0.1593 | 0.1227 | 0.1006 | 1.17 | 1.35 | 0.0962 | 0.6291 | 0.0326 | 0.2043 | 0.0805 | 0.94 | 2.68 | 10.48 | 16.83 | 3.51 | 29.68 |
| Total Market | 6177 | 0.1224 | 0.1713 | 0.1288 | 0.1493 | 0.96 | 1.17 | 0.0853 | 0.5915 | 0.0326 | 0.3003 | 0.0656 | 1.04 | 1.64 | 7.37 | 9.59 | 2.11 | 33.45 |

## Country tax rates

| Tax rate |
|---|
| 0.2 |
| 0.1 |
| 0.35 |
| 0.35 |
| 0.2 |
| 0.28 |
| 0.3 |
| 0.25 |
| 0 |
| 0 |
| 0.275 |
| 0.25 |
| 0.24 |
| 0.33990000000000004 |
| 0 |
| 0.25 |
| 0.1 |
| 0.22 |
| 0.34 |
| 0.1 |
| 0.2 |
| 0.28 |
| 0 |
| 0.2 |
| 0.25 |
| 0.33 |
| 0.3 |
| 0.2 |
| 0.345 |
| 0.1 |
| 0.19 |
| 0.25 |
| 0.29 |
| 0.24 |
| 0.2 |
| 0.21 |
| 0.28 |
| 0.26 |
| 0.3333 |
| 0.2937 |
| 0.1 |
| 0.2 |
| 0.31 |
| 0 |
| 0.35 |
| 0.165 |
| 0.19 |
| 0.2 |
| 0.32439999999999997 |
| 0.25 |
| 0.125 |
| 0 |
| 0.24 |
| 0.314 |
| 0.3333 |
| 0.4069 |
| 0 |
| 0.14 |
| 0.2 |
| 0.22 |
| 0.15 |
| 0.15 |
| 0.2 |
| 0.125 |
| 0.15 |
| 0.28800000000000003 |
| 0.12 |
| 0.1 |
| 0.25 |
| 0.35 |
| 0.15 |
| 0.3 |
| 0.09 |
| 0.32 |
| 0.34 |
| 0.25 |
| 0 |
| 0.28 |
| 0.3 |
| 0.28 |
| 0.12 |
| 0.35 |
| 0.25 |
| 0.3 |
| 0.1 |
| 0.3 |
| 0.3 |
| 0.19 |
| 0.25 |
| 0.1 |
| 0.16 |
| 0.2 |
| 0 |
| 0.27 |
| 0.2 |
| 0.1 |
| 0.17 |
| 0.19 |
| 0.2 |
| 0.3455 |
| 0.3 |
| 0.28 |
| 0 |
| 0.345 |
| 0.35 |
| 0.263 |
| 0.21170000000000003 |
| 0.28 |
| 0.17 |
| 0.3 |
| 0.3 |
| 0 |
| 0.3 |
| 0.2 |
| 0.25 |
| 0.55 |
| 0.26 |
| 0.4 |
| 0.25 |
| 0 |
| 0.34 |
| 0.25 |
| 0.2 |
| 0.35 |
| 0.2575 |

## Country equity risk premiums

| Country | Long-Term Rating | Adj. Default Spread | Total Equity Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|
| Albania | B1 | 0.04 | 0.12 | 0.06 | Eastern Europe & Russia |
| Angola | Ba3 | 0.0325 | 0.10875 | 0.04875 | Africa |
| Argentina | B3 | 0.06 | 0.15 | 0.09 | Central and South America |
| Armenia | Ba2 | 0.0275 | 0.10125 | 0.04125 | Eastern Europe & Russia |
| Australia | Aaa | 0 | 0.06 | 0 | Australia & New Zealand |
| Austria [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| Azerbaijan | Baa3 | 0.02 | 0.09 | 0.03 | Eastern Europe & Russia |
| Bahamas | A3 | 0.0115 | 0.07725 | 0.01725 | Caribbean |
| Bahrain | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Middle East |
| Bangladesh | Ba3 | 0.0325 | 0.10875 | 0.04875 | Asia (w/o Japan) |
| Barbados | Baa3 | 0.02 | 0.09 | 0.03 | Caribbean |
| Belarus | B3 | 0.06 | 0.15 | 0.09 | Eastern Europe & Russia |
| Belgium [1] | Aa3 | 0.007 | 0.0705 | 0.0105 | Western Europe |
| Belize | Ca | 0.02 | 0.09 | 0.03 | Central and South America |
| Bermuda | Aa2 | 0.005 | 0.0675 | 0.0075 | Caribbean |
| Bolivia | Ba3 | 0.0325 | 0.10875 | 0.04875 | Central and South America |
| Bosnia and Herzegovina | B3 | 0.06 | 0.15 | 0.09 | Eastern Europe & Russia |
| Botswana | A2 | 0.01 | 0.075 | 0.015 | Africa |
| Brazil | Baa2 | 0.0175 | 0.08625 | 0.026250000000000002 | Central and South America |
| Bulgaria | Baa2 | 0.0175 | 0.08625 | 0.026250000000000002 | Eastern Europe & Russia |
| Cambodia | B2 | 0.05 | 0.135 | 0.07500000000000001 | Asia (w/o Japan) |
| Canada | Aaa | 0 | 0.06 | 0 | North America |
| Cayman Islands | Aa3 | 0.007 | 0.0705 | 0.0105 | Caribbean |
| Chile | Aa3 | 0.007 | 0.0705 | 0.0105 | Central and South America |
| China | Aa3 | 0.007 | 0.0705 | 0.0105 | Asia (w/o Japan) |
| Colombia | Baa3 | 0.02 | 0.09 | 0.03 | Central and South America |
| Costa Rica | Baa3 | 0.02 | 0.09 | 0.03 | Central and South America |
| Croatia | Baa3 | 0.02 | 0.09 | 0.03 | Eastern Europe & Russia |
| Cuba | Caa1 | 0.07 | 0.165 | 0.10500000000000001 | Caribbean |
| Cyprus [1] | Ba3 | 0.0325 | 0.10875 | 0.04875 | Western Europe |
| Czech Republic | A1 | 0.0085 | 0.07275 | 0.012750000000000001 | Eastern Europe & Russia |
| Denmark | Aaa | 0 | 0.06 | 0 | Western Europe |
| Dominican Republic | B1 | 0.04 | 0.12 | 0.06 | Caribbean |
| Ecuador | Caa2 | 0.085 | 0.1875 | 0.1275 | Central and South America |
| Egypt | B2 | 0.05 | 0.135 | 0.07500000000000001 | Africa |
| El Salvador | Ba2 | 0.0275 | 0.10125 | 0.04125 | Central and South America |
| Estonia | A1 | 0.0085 | 0.07275 | 0.012750000000000001 | Eastern Europe & Russia |
| Fiji Islands | B1 | 0.04 | 0.12 | 0.06 | Asia (w/o Japan) |
| Finland [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| France [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| Georgia | Ba3 | 0.0325 | 0.10875 | 0.04875 | Eastern Europe & Russia |
| Germany [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| Greece [1] | Caa1 | 0.07 | 0.165 | 0.10500000000000001 | Western Europe |
| Guatemala | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Central and South America |
| Honduras | B2 | 0.05 | 0.135 | 0.07500000000000001 | Central and South America |
| Hong Kong | Aa1 | 0.0025 | 0.06375 | 0.00375 | Asia (w/o Japan) |
| Hungary | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Eastern Europe & Russia |
| Iceland | Baa3 | 0.02 | 0.09 | 0.03 | Western Europe |
| India | Baa3 | 0.02 | 0.09 | 0.03 | Asia (w/o Japan) |
| Indonesia | Baa3 | 0.02 | 0.09 | 0.03 | Asia (w/o Japan) |
| Ireland [1] | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Western Europe |
| Isle of Man | Aaa | 0 | 0.06 | 0 | Western Europe |
| Israel | A1 | 0.0085 | 0.07275 | 0.012750000000000001 | Middle East |
| Italy [1] | A3 | 0.0115 | 0.07725 | 0.01725 | Western Europe |
| Jamaica | B3 | 0.06 | 0.15 | 0.09 | Caribbean |
| Japan | Aa3 | 0.007 | 0.0705 | 0.0105 | Japan |
| Jordan | Ba2 | 0.0275 | 0.10125 | 0.04125 | Middle East |
| Kazakhstan | Baa2 | 0.0175 | 0.08625 | 0.026250000000000002 | Eastern Europe & Russia |
| Korea | A1 | 0.0085 | 0.07275 | 0.012750000000000001 | Asia (w/o Japan) |
| Kuwait | Aa2 | 0.005 | 0.0675 | 0.0075 | Middle East |
| Latvia | Baa3 | 0.02 | 0.09 | 0.03 | Eastern Europe & Russia |
| Lebanon | B1 | 0.04 | 0.12 | 0.06 | Middle East |
| Lithuania | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Eastern Europe & Russia |
| Luxembourg [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| Macao | Aa3 | 0.007 | 0.0705 | 0.0105 | Asia (w/o Japan) |
| Malaysia | A3 | 0.0115 | 0.07725 | 0.01725 | Asia (w/o Japan) |
| Malta [1] | A3 | 0.0115 | 0.07725 | 0.01725 | Western Europe |
| Mauritius | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Africa |
| Mexico | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Central and South America |
| Moldova | B3 | 0.06 | 0.15 | 0.09 | Eastern Europe & Russia |
| Mongolia | B1 | 0.04 | 0.12 | 0.06 | Asia (w/o Japan) |
| Montenegro | Ba3 | 0.0325 | 0.10875 | 0.04875 | Eastern Europe & Russia |
| Morocco | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Africa |
| Namibia | Baa3 | 0.02 | 0.09 | 0.03 | Africa |
| Netherlands [1] | Aaa | 0 | 0.06 | 0 | Western Europe |
| New Zealand | Aaa | 0 | 0.06 | 0 | Australia & New Zealand |
| Nicaragua | B3 | 0.06 | 0.15 | 0.09 | Central and South America |
| Norway | Aaa | 0 | 0.06 | 0 | Western Europe |
| Oman | A1 | 0.0085 | 0.07275 | 0.012750000000000001 | Middle East |
| Pakistan | B3 | 0.06 | 0.15 | 0.09 | Asia (w/o Japan) |
| Panama | Baa3 | 0.02 | 0.09 | 0.03 | Central and South America |
| Papua New Guinea | B1 | 0.04 | 0.12 | 0.06 | Asia (w/o Japan) |
| Paraguay | B1 | 0.04 | 0.12 | 0.06 | Central and South America |
| Peru | Baa3 | 0.02 | 0.09 | 0.03 | Central and South America |
| Philippines | Ba2 | 0.0275 | 0.10125 | 0.04125 | Asia (w/o Japan) |
| Poland | A2 | 0.01 | 0.075 | 0.015 | Eastern Europe & Russia |
| Portugal [1] | Ba3 | 0.0325 | 0.10875 | 0.04875 | Western Europe |
| Qatar | Aa2 | 0.005 | 0.0675 | 0.0075 | Middle East |
| Romania | Baa3 | 0.02 | 0.09 | 0.03 | Eastern Europe & Russia |
| Russia | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Eastern Europe & Russia |
| Saudi Arabia | Aa3 | 0.007 | 0.0705 | 0.0105 | Middle East |
| Senegal | B1 | 0.04 | 0.12 | 0.06 | Africa |
| Singapore | Aaa | 0 | 0.06 | 0 | Asia (w/o Japan) |
| Slovakia | A2 | 0.01 | 0.075 | 0.015 | Eastern Europe & Russia |
| Slovenia [1] | A2 | 0.01 | 0.075 | 0.015 | Eastern Europe & Russia |
| South Africa | A3 | 0.0115 | 0.07725 | 0.01725 | Africa |
| Spain | Baa3 | 0.02 | 0.09 | 0.03 | Western Europe |
| Sri Lanka | B1 | 0.04 | 0.12 | 0.06 | Asia (w/o Japan) |
| St. Vincent & the Grenadines | B1 | 0.04 | 0.12 | 0.06 | Caribbean |
| Suriname | Ba3 | 0.0325 | 0.10875 | 0.04875 | Caribbean |
| Sweden | Aaa | 0 | 0.06 | 0 | Western Europe |
| Switzerland | Aaa | 0 | 0.06 | 0 | Western Europe |
| Taiwan | Aa3 | 0.007 | 0.0705 | 0.0105 | Asia (w/o Japan) |
| Thailand | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Asia (w/o Japan) |
| Trinidad and Tobago | Baa1 | 0.015 | 0.08249999999999999 | 0.0225 | Caribbean |
| Tunisia | Baa3 | 0.02 | 0.09 | 0.03 | Africa |
| Turkey | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Western Europe |
| Ukraine | B2 | 0.05 | 0.135 | 0.07500000000000001 | Eastern Europe & Russia |
| United Arab Emirates | Aa2 | 0.005 | 0.0675 | 0.0075 | Middle East |
| United Kingdom | Aaa | 0 | 0.06 | 0 | Western Europe |
| United States of America | Aaa | 0 | 0.06 | 0 | North America |
| Uruguay | Ba1 | 0.024 | 0.096 | 0.036000000000000004 | Central and South America |
| Venezuela | B1 | 0.04 | 0.12 | 0.06 | Central and South America |
| Vietnam | B1 | 0.04 | 0.12 | 0.06 | Asia (w/o Japan) |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | Values |  |  |  |  |
| Row Labels | Count of Country | Average of Total Equity Risk Premium | Average of Country Risk Premium |  |  |
| Africa | 9 | 0.09716666666666667 | 0.03716666666666667 |  |  |
| Australia & New Zealand | 2 | 0.06 | 0 |  |  |
| Caribbean | 10 | 0.10515000000000001 | 0.04515000000000001 |  |  |
| Central and South America | 18 | 0.10854166666666666 | 0.04854166666666667 |  |  |
| Eastern Europe & Russia | 22 | 0.09944318181818183 | 0.03944318181818182 |  |  |
| Middle East | 9 | 0.08025 | 0.020250000000000004 |  |  |
| North America | 2 | 0.06 | 0 |  |  |
| Western Europe | 22 | 0.07725000000000003 | 0.01725 |  |  |
| Asia (w/o Japan) | 19 | 0.09698684210526316 | 0.03698684210526316 |  |  |
| Japan | 1 | 0.0705 | 0.0105 |  |  |
| Grand Total | 114 | 0.09335526315789466 | 0.03335526315789474 |  |  |

## Traiing 12 month

| Last 10K | First X months: Last year | First X months: Current year | Trailing 12 month | Growth rate | Just last quarter |
|---|---|---|---|---|---|
| 156508 | 85519 | 98115 | 169104 | 0.14728890655877636 | 43603 |
| 3381 | 1599 | 2129 | 3911 | 0.3314571607254535 | 1119 |
| 55241 | 32724 | 29768 | 52285 | -0.09033125534775699 | 12558 |
| 118210 |  | 135490 |  |  |  |
| 0 |  | 0 |  |  |  |
| Yes |  | Yes |  |  |  |
| 121251 |  | 144687 |  |  |  |
| 0 |  | 0 |  |  |  |
| 0 |  | 0 |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| 0.25160052364471064 | 0.22306525037936267 | 0.26006475455407657 |  |  |  |
|  |  |  |  |  |  |
| 0.35295959311984054 | 0.3826518083700698 | 0.3033990725169444 |  |  | 0.2880077058917964 |
|  |  |  |  |  |  |
| 516 |  | NA |  |  |  |
| 556 |  | NA |  |  |  |
| 542 |  | NA |  |  |  |
| 513 |  | NA |  |  |  |
| 486 |  | NA |  |  |  |
| 1801 |  | NA |  |  |  |

## Answer keys

| Yes/No | Book or Market Value |
|---|---|
| Yes | B |
| No | V |
