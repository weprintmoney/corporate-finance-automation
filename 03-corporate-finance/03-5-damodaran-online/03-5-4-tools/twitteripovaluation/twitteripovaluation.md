---
title: "Twitteripovaluation"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/blog/TwitterIPOvaluation.xls
---

# Twitteripovaluation

Source: https://www.stern.nyu.edu/~adamodar/pc/blog/TwitterIPOvaluation.xls

Sheets: Input sheet, Valuation output, Option value, Diagnostics, R& D converter, Operating lease converter, Cost of capital worksheet, Synthetic rating, Industry Averages(US), Country tax rates, Country equity risk premiums, Traiing 12 month, Answer keys, Global industry averages

## Input sheet

| Date of valuation | 40086.0 | Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |
|---|---|---|
| Company name | Twitter | There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |
| Numbers from your base year below ( in consistent units) |  |  |
|  | This year | Last year |
| Country of incorporation | United States of America | See page 215. In 2013, Twitter derived about 75% of their revenues from US, 25% from rest of the world. See cost of capital worksheet for adjustment to equity risk premium. |
| Industry (US) | Advertising | See page 77. Do get some revenues from data service (about 12.6% of revenues in 2013).  |
| Industry (Global) | Advertising |  |
| Revenues | 448.209 | 316.933 |
| Operating income or EBIT | -92.873 | -77.063 |
| Interest expense | 2.75 | 2.486 |
| Book value of equity | 716.9 | -248.172 |
| Book value of debt | 80.13 | 65.73 |
| Do you have R&D expenses to capitalize? | Yes | See page 175 & R&D worksheet |
| Do you have operating lease commitments? | Yes | See page 214 & Operating lease worksheet |
| Cash and cross holdings | 375.11 | 424.83000000000004 |
| Non-operating assets  | 0 | 0 |
| Minority interests | 0 | 0 |
| Number of shares outstanding = | 574.4369999999999 | Pg 17: Shares include RSUs, warrant exercise, MoBus acquisition but not options |
| Number of shares that will be sold on offering date = | 50 | Not decided by company & bankers yet. Update when offering details set. News reports suggest that the company would like to raise $1 billion from offering. |
| Current stock price = | 20 | TBA before offering. |
| Effective tax rate = | 0.3 | No taxes until 2017 |
| Marginal tax rate = | 0.355 | Page 211: Federal + State  |
| The value drivers below: |  |  |
| Compounded annual revenue growth rate over next 5 years = | 0.55 |  |
| Target pre-tax operating margin (EBIT as % of sales in year 10) = | 0.25 |  |
| Sales to capital ratio  (for computing reinvestment) = | 1.5 |  |
| Market numbers  |  |  |
| Riskfree rate | 0.027 | 10-year bond rate (10/4/13) |
| Initial cost of capital = | 0.1121984400485641 | See cost of capital worksheet |
| Other inputs |  |  |
| Do you have employee options outstanding? | Yes |  |
| Number of options outstanding = | 44.157 | Page 207 |
| Average strike price = | 1.82 | Page 207 |
| Average maturity = | 3.465 | Page 207; Halved expected life to reflect early exercise of employee options |
| Standard deviation on stock price = | 0.536 | Page 207; 53.6% estimated |
|  |  |  |
| Default assumptions.  |  |  |
| In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%) |  |  |
| Do you want to override this assumption = | Yes |  |
| If yes, enter the cost of capital after year 10 = | 0.08 | Mature advertising companies' cost of capital |
| I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time. |  |  |
| Do you want to override this assumption = | Yes |  |
| If yes, enter the return on capital you expect after year 10 | 0.12 | At the top 10% of mature company excess returns |
| I will assume that your firm has no chance of failure over the foreseeable future. |  |  |
| Do you want to override this assumption = | No | Company has deep-pocketed VCs and access to capital. I am going to assume that they |
| If yes, enter the probability of failure = | 0.2 | will not go under or be forced to sell themselves at below value. |
| What do you want to tie your proceeds in failure to? | V |  |
| Enter the distress proceeds as percentage of book or fair value | 0.5 |  |
| I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year. If you override this assumption, I will leave the tax rate at your effective tax rate. |  |  |
| Do you want to override this assumption = | No |  |
| I will assume that you have no losses carried forward from prior years ( NOL) coming into the valuation. If you have a money losing company, you may want to override tis. |  |  |
| Do you want to override this assumption = | Yes |  |
| If yes, enter the NOL that you are carrying over into year 1 | 468.02000000000004 | Page 212: Dec 2012 loss carryforward (298.6 m + 106.6 m) + Op loss for first 6 months 2013 |
| I will assume that the proceeds of the IPO will be retained by the company (for use in future investments) |  |  |
| Do you want to override this assumption ? | No | Page 16 |
| If yes, specify the perecentage of the proceeds that be withdrawn by owners | 1 |  |

## Valuation output

| Base year | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 | 7.0 | 8.0 | 9.0 | 10.0 | Terminal year |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.55 | 0.55 | 0.55 | 0.55 | 0.55 | 0.4454 | 0.34080000000000005 | 0.23620000000000008 | 0.13160000000000005 | 0.027000000000000024 | 0.027000000000000024 |
| 448.209 | 694.7239500000001 | 1076.8221225000002 | 1669.0742898750004 | 2587.0651493062505 | 4009.9509814246885 | 5795.983148551245 | 7771.254205577509 | 9606.824448934918 | 10871.082546414755 | 11164.601775167954 | 11466.04602309749 |
| -0.011755650310511572 | 0.014419914720539606 | 0.04059547975159075 | 0.0667710447826419 | 0.09294660981369307 | 0.11912217484474422 | 0.14529773987579536 | 0.17147330490684654 | 0.19764886993789768 | 0.22382443496894885 | 0.25 | 0.25 |
| -5.2689882700240815 | 10.017860113316422 | 43.71411067001373 | 111.44583415479988 | 240.4589349951717 | 477.6740819281254 | 842.1432518426922 | 1332.5626419016057 | 1898.7779960237533 | 2433.213908452084 | 2791.1504437919884 | 2866.5115057743724 |
| 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.311 | 0.322 | 0.333 | 0.34400000000000003 | 0.35500000000000004 | 0.355 |
| -5.2689882700240815 | 10.017860113316422 | 43.71411067001373 | 111.44583415479988 | 240.4589349951717 | 353.0868353696973 | 580.2367005196149 | 903.4774712092888 | 1266.4849233478435 | 1596.188323944567 | 1800.2920362458326 | 1848.8999212244703 |
|  | 164.34330000000003 | 254.7321150000001 | 394.83477825000017 | 611.9939062875001 | 948.5905547456254 | 1190.6881114177042 | 1316.8473713508429 | 1223.7134955716058 | 842.8387316532244 | 195.67948583546604 | 416.00248227550617 |
|  | -154.3254398866836 | -211.01800432998638 | -283.38894409520026 | -371.53497129232835 | -595.5037193759281 | -610.4514108980893 | -413.3699001415541 | 42.771427776237715 | 753.3495922913426 | 1604.6125504103666 | 1432.897438948964 |
| 468.02000000000004 | 458.0021398866836 | 414.2880292166699 | 302.84219506187003 | 62.38326006669834 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | 0.1121984400485641 | 0.1121984400485641 | 0.1121984400485641 | 0.1121984400485641 | 0.1121984400485641 | 0.10575875203885128 | 0.09931906402913847 | 0.09287937601942566 | 0.08643968800971284 | 0.08000000000000003 | 0.08 |
|  | 0.8991201246032453 | 0.8084169984665553 | 0.7268639923926308 | 0.6535380434096746 | 0.5876092070234678 | 0.5314081448055514 | 0.48339755235197673 | 0.44231555920896476 | 0.4071238966051196 | 0.37696657093066627 |  |
|  | -138.7571087403656 | -170.59054168285016 | -205.98521930496932 | -242.8122381966579 | -349.92346832201474 | -324.39885175928504 | -199.8219979444083 | 18.91846799501243 | 306.70662151952956 | 604.8852908005067 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
| 1432.897438948964 |  |  |  |  |  |  |  |  |  |  |  |
| 0.08 |  |  |  |  |  |  |  |  |  |  |  |
| 27035.80073488611 |  |  |  |  |  |  |  |  |  |  |  |
| 10191.593095394805 |  |  |  |  |  |  |  |  |  |  |  |
| -701.7790456355024 |  |  |  |  |  |  |  |  |  |  |  |
| 9489.814049759301 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 4744.907024879651 |  |  |  |  |  |  |  |  |  |  |  |
| 9489.814049759301 |  |  |  |  |  |  |  |  |  |  |  |
| 204.4619296201446 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 375.11 |  |  |  |  |  |  |  |  |  |  |  |
| 1000 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 10660.462120139156 |  |  |  |  |  |  |  |  |  |  |  |
| 804.8339550163705 |  |  |  |  |  |  |  |  |  |  |  |
| 9855.628165122786 |  |  |  |  |  |  |  |  |  |  |  |
| 574.4369999999999 |  |  |  |  |  |  |  |  |  |  |  |
| 17.15702185813725 |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  |  |  |  |  |  |  |  |  |  |  |
| 1.165703474960276 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 |  |
| 836.8185962868113 | 1001.1618962868113 | 1255.8940112868113 | 1650.7287895368115 | 2262.722695824312 | 3211.3132505699373 | 4402.001361987642 | 5718.848733338485 | 6942.56222891009 | 7785.400960563315 | 7981.080446398781 |  |
| -0.006296452174227481 | 0.01000623390729457 | 0.03480716547507339 | 0.0675131098828604 | 0.10626973222963687 | 0.10995091659371199 | 0.13181202203390957 | 0.1579824040356925 | 0.18242327279026327 | 0.20502326495835024 | 0.22556996491097386 | 0.12 |

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

| Estimation of Current Cost of Capital | Your inputs | Operating Regions ERP calculator |
|---|---|---|
| Inputs | Computed number | Country |
| Equity |  | Argentina |
| Number of Shares outstanding = |  | Bolivia |
| Current Market Price per share = |  | Brazil |
|  |  | Canada |
| Approach for estimating beta |  |  |
| If direct input, enter levered beta (or regression beta) |  | Chile |
| Unlevered beta = |  | Ecuador |
| Riskfree Rate = |  | Paraguay |
| What approach do you want to use to input ERP? |  | Peru |
| Direct input for ERP (if you choose "will input" |  |  |
| Equity Risk Premium used in cost of equity = |  |  |
|  |  | Total |
| Debt |  | Operating Regions ERP calculator |
| Book Value of Straight Debt = |  | Region |
| Interest Expense on Debt = |  | Africa |
| Average Maturity = |  | Australia & New Zealand |
| Approach for estimating pre-tax cost of debt |  | Caribbean |
| If direct input, input the pre-tax cost of debt |  | Central and South America |
| If actual rating, input the rating |  | Eastern Europe & Russia |
| If synethetic rating, input the type of company |  | Middle East |
| Pre-tax Cost of Debt = |  | North America |
| Tax Rate = |  | Western Europe |
|  |  | Asia without Japan |
| Book Value of Convertible Debt = |  | Japan |
| Interest Expense on Convertible = |  | Rest of the World |
| Maturity of Convertible Bond = |  | Total |
| Market Value of Convertible = |  |  |
|  |  | Multi Business (US Industry Averages) |
| Debt value of operating leases = |  | Business |
|  |  | Advertising |
| Preferred Stock |  | Information Services |
| Number of Preferred Shares = |  |  |
| Current Market Price per Share= |  |  |
| Annual Dividend per Share = |  |  |
|  |  |  |
| Output |  |  |
| Estimating Market Value of Straight Debt = | 70.69679418787786 |  |
| Estimated Value of Straight Debt in Convertible = | 0 |  |
| Value of Debt in Operating leases = | 124.33192962014459 |  |
| Estimated Value of Equity in Convertible = | 0 |  |
| Levered Beta for equity = | 1.401 |  |
|  |  | Company |
|  | Debt  |  |
| Market Value | 195.02872380802245 | Multi Business (Global Industry Averages) |
| Weight in Cost of Capital | 0.016692278700331714 | Business |
| Cost of Component | 0.0516 | Advertising |
|  |  | Information Services |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  | Company |
|  |  |  |
|  |  |  |
|  | 0.017088800732377174 |  |

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
| Estimated Company Default Spread = |
| Estimated County Default Spread (if any) = |
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
|  |

## Industry Averages(US)

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

| Country | Tax Rate |
|---|---|
| Afghanistan | 0.2 |
| Albania | 0.1 |
| Angola | 0.35 |
| Argentina | 0.35 |
| Armenia | 0.2 |
| Aruba | 0.28 |
| Australia | 0.3 |
| Austria | 0.25 |
| Bahamas | 0 |
| Bahrain | 0 |
| Bangladesh | 0.275 |
| Barbados | 0.25 |
| Belarus | 0.18 |
| Belgium | 0.33990000000000004 |
| Bermuda | 0 |
| Bolivia | 0.25 |
| Bonaire | 0 |
| Bosnia and Herzegovina | 0.1 |
| Botswana | 0.22 |
| Brazil | 0.34 |
| Bulgaria | 0.1 |
| Cambodia | 0.2 |
| Canada | 0.26 |
| Cayman Islands | 0 |
| Chile | 0.185 |
| China | 0.25 |
| Colombia | 0.33 |
| Costa Rica | 0.3 |
| Croatia | 0.2 |
| Curacao | 0.275 |
| Cyprus | 0.1 |
| Czech Republic | 0.19 |
| Denmark | 0.25 |
| Dominican Republic | 0.29 |
| Ecuador | 0.23 |
| Egypt | 0.25 |
| Estonia | 0.21 |
| El Salvador | 0.3 |
| Fiji | 0.28 |
| Finland | 0.245 |
| France | 0.3333 |
| Georgia | 0 |
| Germany | 0.2948 |
| Gibraltar | 0.1 |
| Greece | 0.2 |
| Guatemala | 0.31 |
| Guernsey | 0 |
| Honduras | 0.35 |
| Hong Kong | 0.165 |
| Hungary | 0.19 |
| Iceland | 0.2 |
| India | 0.3245 |
| Indonesia | 0.25 |
| Ireland | 0.125 |
| Isle of Man | 0 |
| Israel | 0.25 |
| Italy | 0.314 |
| Jamaica | 0.3333 |
| Japan | 0.3801 |
| Jersey | 0 |
| Jordan | 0.14 |
| Kazakhstan | 0.2 |
| Kenya | 0.3 |
| Korea, Republic of | 0.242 |
| Kuwait | 0.15 |
| Latvia | 0.15 |
| Libya | 0.2 |
| Liechtenstein | 0.125 |
| Lithuania | 0.15 |
| Luxembourg | 0.28800000000000003 |
| Macau | 0.12 |
| Macedonia | 0.1 |
| Malawi | 0.3 |
| Malaysia | 0.25 |
| Malta | 0.35 |
| Mauritius | 0.15 |
| Mexico | 0.3 |
| Montenegro | 0.09 |
| Mozambique | 0.32 |
| Namibia | 0.34 |
| Netherlands | 0.25 |
| New Zealand | 0.28 |
| Nigeria | 0.3 |
| Norway | 0.28 |
| Oman | 0.12 |
| Pakistan | 0.35 |
| Panama | 0.25 |
| Papua New Guinea | 0.3 |
| Paraguay | 0.1 |
| Peru | 0.3 |
| Philippines | 0.3 |
| Poland | 0.19 |
| Portugal | 0.25 |
| Qatar | 0.1 |
| Romania | 0.16 |
| Russia | 0.2 |
| Saba | 0 |
| Samoa | 0.27 |
| Saudi Arabia | 0.2 |
| Serbia | 0.1 |
| Singapore | 0.17 |
| Slovak Republic | 0.19 |
| Slovenia | 0.18 |
| South Africa | 0.3455 |
| Spain | 0.3 |
| Sri Lanka | 0.28 |
| St Eustatius | 0 |
| St Maarten | 0.345 |
| Sudan | 0.35 |
| Sweden | 0.263 |
| Switzerland | 0.21170000000000003 |
| Syria | 0.28 |
| Taiwan | 0.17 |
| Tanzania | 0.3 |
| Thailand | 0.23 |
| Trinidad and Tobago | 0.25 |
| Tunisia | 0.3 |
| Turkey | 0.2 |
| Uganda | 0.3 |
| Ukraine | 0.21 |
| United Arab Emirates | 0.55 |
| United Kingdom | 0.24 |
| United States | 0.4 |
| Uruguay | 0.25 |
| Vanuatu | 0 |
| Venezuela | 0.34 |
| Vietnam | 0.25 |
| Yemen | 0.2 |
| Zambia | 0.35 |
| Zimbabwe | 0.2575 |
| Africa average | 0.2902 |
| North America average | 0.33 |
| Asia average | 0.2289 |
| Europe average | 0.205 |
| Latin America average | 0.28300000000000003 |
| Oceania average | 0.28600000000000003 |
| EU average | 0.226 |
| OECD average | 0.2525 |
| Global average | 0.2443 |

## Country equity risk premiums

| Country | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|
| Albania | B1 | 0.04 | 0.118 | 0.06 | Eastern Europe & Russia |
| Angola | Ba3 | 0.0325 | 0.1068 | 0.0488 | Africa |
| Argentina | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Armenia | Ba2 | 0.0275 | 0.0993 | 0.0413 | Eastern Europe & Russia |
| Australia | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| Austria | Aaa | 0 | 0.058 | 0 | Western Europe |
| Azerbaijan | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Bahamas | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Bahrain | Baa1 | 0.015 | 0.0805 | 0.0225 | Middle East |
| Bangladesh | Ba3 | 0.0325 | 0.1068 | 0.0488 | Asia |
| Barbados | Baa3 | 0.02 | 0.088 | 0.03 | Caribbean |
| Belarus | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Belgium | Aa3 | 0.007 | 0.0685 | 0.0105 | Western Europe |
| Belize | Caa3 | 0.1 | 0.208 | 0.15 | Central and South America |
| Bermuda | Aa2 | 0.005 | 0.0655 | 0.0075 | Caribbean |
| Bolivia | Ba3 | 0.0325 | 0.1068 | 0.0488 | Central and South America |
| Bosnia and Herzegovina | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Botswana | A2 | 0.01 | 0.073 | 0.015 | Africa |
| Brazil | Baa2 | 0.0175 | 0.0843 | 0.0263 | Central and South America |
| Bulgaria | Baa2 | 0.0175 | 0.0843 | 0.0263 | Eastern Europe & Russia |
| Cambodia | B2 | 0.05 | 0.133 | 0.075 | Asia |
| Canada | Aaa | 0 | 0.058 | 0 | North America |
| Cayman Islands | Aa3 | 0.007 | 0.0685 | 0.0105 | Caribbean |
| Chile | Aa3 | 0.007 | 0.0685 | 0.0105 | Central and South America |
| China | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Colombia | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Costa Rica | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Croatia | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Cuba | Caa1 | 0.07 | 0.163 | 0.105 | Caribbean |
| Cyprus | B3 | 0.06 | 0.148 | 0.09 | Western Europe |
| Czech Republic | A1 | 0.0085 | 0.0708 | 0.0128 | Eastern Europe & Russia |
| Denmark | Aaa | 0 | 0.058 | 0 | Western Europe |
| Dominican Republic | B1 | 0.04 | 0.118 | 0.06 | Caribbean |
| Ecuador | Caa1 | 0.07 | 0.163 | 0.105 | Central and South America |
| Egypt | B2 | 0.05 | 0.133 | 0.075 | Africa |
| El Salvador | Ba3 | 0.0325 | 0.1068 | 0.0488 | Central and South America |
| Estonia | A1 | 0.0085 | 0.0708 | 0.0128 | Eastern Europe & Russia |
| Fiji Islands | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Finland | Aaa | 0 | 0.058 | 0 | Western Europe |
| France | Aa1 | 0.0025 | 0.0618 | 0.0038 | Western Europe |
| Georgia | Ba3 | 0.0325 | 0.1068 | 0.0488 | Eastern Europe & Russia |
| Germany | Aaa | 0 | 0.058 | 0 | Western Europe |
| Greece | Caa1 | 0.07 | 0.163 | 0.105 | Western Europe |
| Guatemala | Ba1 | 0.024 | 0.094 | 0.036 | Central and South America |
| Honduras | B2 | 0.05 | 0.133 | 0.075 | Central and South America |
| Hong Kong | Aa1 | 0.0025 | 0.0618 | 0.0038 | Asia |
| Hungary | Ba1 | 0.024 | 0.094 | 0.036 | Eastern Europe & Russia |
| Iceland | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| India | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Indonesia | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Ireland | Ba1 | 0.024 | 0.094 | 0.036 | Western Europe |
| Isle of Man | Aaa | 0 | 0.058 | 0 | Financial Center |
| Israel | A1 | 0.0085 | 0.0708 | 0.0128 | Middle East |
| Italy | Baa2 | 0.0175 | 0.0843 | 0.0263 | Western Europe |
| Jamaica | B3 | 0.06 | 0.148 | 0.09 | Caribbean |
| Japan | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Jordan | Ba2 | 0.0275 | 0.0993 | 0.0413 | Middle East |
| Kazakhstan | Baa2 | 0.0175 | 0.0843 | 0.0263 | Eastern Europe & Russia |
| Kenya | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Korea | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Kuwait | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Latvia | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Lebanon | B1 | 0.04 | 0.118 | 0.06 | Middle East |
| Lithuania | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Luxembourg | Aaa | 0 | 0.058 | 0 | Western Europe |
| Macao | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Malaysia | A3 | 0.0115 | 0.0753 | 0.0173 | Asia |
| Malta | A3 | 0.0115 | 0.0753 | 0.0173 | Western Europe |
| Mauritius | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Mexico | Baa1 | 0.015 | 0.0805 | 0.0225 | Central and South America |
| Moldova | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Mongolia | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Montenegro | Ba3 | 0.0325 | 0.1068 | 0.0488 | Eastern Europe & Russia |
| Morocco | Ba1 | 0.024 | 0.094 | 0.036 | Africa |
| Namibia | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Netherlands | Aaa | 0 | 0.058 | 0 | Western Europe |
| New Zealand | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| Nicaragua | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Nigeria | Ba3 | 0.0325 | 0.1068 | 0.0488 | Africa |
| Norway | Aaa | 0 | 0.058 | 0 | Western Europe |
| Oman | A1 | 0.0085 | 0.0708 | 0.0128 | Middle East |
| Pakistan | Caa1 | 0.07 | 0.163 | 0.105 | Asia |
| Panama | Baa2 | 0.0175 | 0.0843 | 0.0263 | Central and South America |
| Papua New Guinea | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Paraguay | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Peru | Baa2 | 0.0175 | 0.0843 | 0.0263 | Central and South America |
| Philippines | Ba1 | 0.024 | 0.094 | 0.036 | Asia |
| Poland | A2 | 0.01 | 0.073 | 0.015 | Eastern Europe & Russia |
| Portugal | Ba3 | 0.0325 | 0.1068 | 0.0488 | Western Europe |
| Qatar | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Romania | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Russia | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Saudi Arabia | Aa3 | 0.007 | 0.0685 | 0.0105 | Middle East |
| Senegal | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Singapore | Aaa | 0 | 0.058 | 0 | Asia |
| Slovakia | A2 | 0.01 | 0.073 | 0.015 | Eastern Europe & Russia |
| Slovenia | Baa2 | 0.0175 | 0.0843 | 0.0263 | Western Europe |
| South Africa | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Spain | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| Sri Lanka | B1 | 0.04 | 0.118 | 0.06 | Asia |
| St. Maarten | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| St. Vincent & the Grenadines | B2 | 0.05 | 0.133 | 0.075 | Caribbean |
| Suriname | Ba3 | 0.0325 | 0.1068 | 0.0488 | Caribbean |
| Sweden | Aaa | 0 | 0.058 | 0 | Western Europe |
| Switzerland | Aaa | 0 | 0.058 | 0 | Western Europe |
| Taiwan | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Thailand | Baa1 | 0.015 | 0.0805 | 0.0225 | Asia |
| Trinidad and Tobago | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Tunisia | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Turkey | Ba1 | 0.024 | 0.094 | 0.036 | Western Europe |
| Ukraine | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| United Arab Emirates | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| United Kingdom | Aaa | 0 | 0.058 | 0 | Western Europe |
| United States of America | Aaa | 0 | 0.058 | 0 | North America |
| Uruguay | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Venezuela | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Vietnam | B2 | 0.05 | 0.133 | 0.075 | Asia |
| Zambia | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Row Labels | Default Spread (Weighted average) | Total ERP (Weighted Average) | Country Risk Premium (Weighted Average) |  |  |
| Africa | 0.0286 | 0.1009 | 0.0429 |  |  |
| Australia & New Zealand | 0 | 0.058 | 0 |  |  |
| Caribbean | 0.0452 | 0.1257 | 0.0677 |  |  |
| Central and South America | 0.0226 | 0.0918 | 0.0338 |  |  |
| Eastern Europe & Russia | 0.0179 | 0.0848 | 0.0268 |  |  |
| Middle East | 0.0077 | 0.0696 | 0.0116 |  |  |
| North America | 0 | 0.058 | 0 |  |  |
| Western Europe | 0.007 | 0.0685 | 0.0105 |  |  |
| Asia without Japan | 0.0118 | 0.0758 | 0.0178 |  |  |
| Japan | 0.007 | 0.0685 | 0.0105 |  |  |
| Rest of the World | 0.01 | 0.0723 | 0.0148 |  |  |

## Traiing 12 month

| Last 10K | First X months: Last year | First X months: Current year | Trailing 12 month |
|---|---|---|---|
| 316.933 | 122.359 | 253.635 | 448.209 |
| 119.004 | 46.3 | 111.8 | 184.50400000000002 |
| -77.063 | -47.01 | -62.82 | -92.873 |
| 2.486 | 0.89 | 2.75 | 4.346 |
| -248.172 |  | -164.375 |  |
| 65.73 |  | 80.13 |  |
|  |  |  |  |
| 424.83000000000004 |  | 375.11 |  |
| 0 |  | 0 |  |
| 0 |  | 0 |  |
|  |  |  |  |
|  |  |  |  |
| 0 | 0 | 0 |  |
|  |  |  |  |
|  |  |  |  |
| 26.91 |  | NA |  |
| 29.26 |  | NA |  |
| 29.26 |  | NA |  |
| 28.07 |  | NA |  |
| 22.02 |  | NA |  |
| 24.57 |  | NA |  |

## Answer keys

| Yes/No | Book or Market Value | ERP choices | Cost of debt | Synthetic rating | Beta |
|---|---|---|---|---|---|
| Yes | B | Will input | Direct input | 1 | Direct input |
| No | V | Country of incorporation | Synthetic rating | 2 | Single Business(US) |
|  |  | Operating countries | Actual rating |  | Single Business(Global) |
|  |  | Operating regions |  |  | Multibusiness(US) |
|  |  |  |  |  | Multibusiness(Global) |

## Global industry averages

| Industry Name | Number of firms | Unlevered beta corrected for cash | Market D/E Ratio | Market Debt to Capital | Effective tax rate | Dividend Payout | Net Margin | Pre-tax Operating Margin | ROE | ROIC | Sales/Capital | EV/Sales | Revenue Growth rate: Last 5 years | Expected Earnings growth: Next 5 years |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 255 | 0.9813128063078118 | 0.32285400930218305 | 0.24405868450479382 | 0.13915961767489343 | 0.34691743497599337 | 0.03862336823924635 | 0.08101419761211583 | 0.09424647962939244 | 0.42521222963308486 | 4.528507631543998 | 0.938341047980359 | 0.06819351851851856 | 0.21095999999999995 |
| Aerospace/Defense | 210 | 0.8920435222041221 | 0.2626743606424056 | 0.20803016900475105 | 0.13311977094505284 | 0.33178759766626276 | 0.05350132695823634 | 0.08910379922853265 | 0.16426310461110014 | 0.35497158656567274 | 4.861408152664427 | 0.9945361918433846 | 0.05451112781954886 | 0.12243676470588234 |
| Air Transport | 160 | 0.6018867893188159 | 1.0091679601276586 | 0.5022815315368347 | 0.16149706853436283 | 0.5120941110594878 | 0.016590868234295456 | 0.04840920628927394 | 0.06349880036012388 | 0.06941957804332193 | 1.667055672659041 | 0.7918412240373706 | 0.09503787037037036 | 0.21781746031746033 |
| Apparel | 1166 | 0.9960919023007525 | 0.17841250953933321 | 0.15140072605736213 | 0.13417496890087285 | 0.37804651987997434 | 0.06476104647537112 | 0.11698748618783013 | 0.1291916419237209 | 0.15045425471198526 | 1.5453554145186614 | 1.551760944825506 | 0.08054699270072996 | 0.14168521739130435 |
| Auto & Truck | 130 | 0.774914490976416 | 0.9390556238794814 | 0.4842850366513502 | 0.12660546185393126 | 0.16299350807323257 | 0.05807048414388008 | 0.0598165420528631 | 0.18614886657796392 | 0.0782582418738199 | 1.4864379768030893 | 0.7799558782657275 | 0.07885977011494252 | 0.16778125 |
| Auto Parts | 624 | 1.1883348847461743 | 0.36995263266137757 | 0.27004775482103965 | 0.16547177435032676 | 0.12540066844086628 | 0.04196974003613371 | 0.06599810034752202 | 0.13903094059836443 | 0.1433463602260584 | 2.496943580923715 | 0.5645053076137062 | 0.07608838383838384 | 0.15868089887640452 |
| Bank | 568 | 0.3064199355538831 | 3.6711701448508722 | 0.7859208787112323 | 0.18931380774478773 | 0.3202396384425511 | 0.20419909161883287 | 0.002528915374310298 | 0.08973531018635007 | 0.0001588267406032971 | 0.09090439796727583 | 11.36126107792408 | 0.09332915000000006 | 0.15269697368421048 |
| Banks (Regional) | 944 | 0.4411297738164468 | 1.4234191720500726 | 0.5873598709074924 | 0.18854689553676668 | 0.15949533615369282 | 0.1867717681187097 | 5.1830082891675855e-06 | 0.07167359321869533 | 1.2956023920285343e-06 | 0.22976523508766486 | 3.9193947291704645 | 0.040468153846153855 | 0.0768179775280899 |
| Beverage  | 99 | 0.7399561748472607 | 0.2128585567830011 | 0.17550155011280905 | 0.12824592966020384 | 0.3071296400090619 | 0.10115919047989652 | 0.14767959369907338 | 0.2128840943496653 | 0.18974582117364186 | 1.6024849083771933 | 2.2290604470483215 | 0.09190892857142857 | 0.14055 |
| Beverage (Alcoholic) | 209 | 0.6759306135245668 | 0.24361704323360311 | 0.19589394062995458 | 0.18596275952026767 | 0.33047162943952946 | 0.11692981713292433 | 0.18888084812283265 | 0.17269482194047803 | 0.14323312476484668 | 0.8935211562130586 | 2.905605308839391 | 0.09464894736842108 | 0.17422692307692308 |
| Biotechnology | 666 | 1.0534174232761304 | 0.13066268585950153 | 0.11556292384423655 | 0.029118060456114103 | 0.34780460975473915 | 0.08075456553854306 | 0.17159921646461276 | 0.07246948017732503 | 0.1145416572343344 | 0.8041379103641797 | 6.5236163504747005 | 0.18820254019292598 | 0.21890392156862745 |
| Broadcasting | 144 | 1.0280865480180033 | 0.4012362070014312 | 0.28634444713647156 | 0.17522339928121536 | 0.3173705650696116 | 0.08486258559090847 | 0.15894673538630358 | 0.13118372308279064 | 0.15032039838526717 | 1.1240793053518594 | 2.061614739336022 | 0.06869979591836736 | 0.05902399999999999 |
| Brokerage & Investment Banking | 525 | 0.27696203234691474 | 4.15345997508518 | 0.805955609467313 | 0.11360196721685252 | 0.3686600299816155 | 0.05019149739852615 | 0.0017985000474503177 | 0.041313180507171005 | 0.00015844142217180348 | 0.16834549391105746 | 6.083050794228997 | 0.05540231833910039 | 0.1690995918367347 |
| Building Materials | 420 | 0.8063758617128962 | 0.4477057753681698 | 0.3092519094595119 | 0.1608212257362318 | 0.36745843434736003 | 0.024556354504291184 | 0.06135572935106442 | 0.05131200502168298 | 0.07577157650697185 | 1.710682754255188 | 0.8888461716509403 | 0.01835483754512635 | 0.19073254237288131 |
| Business & Consumer Services | 709 | 0.82720134885165 | 0.2513232436309617 | 0.20084598037330278 | 0.1810984403199698 | 0.4068852764079592 | 0.04200859974524471 | 0.07854881818833337 | 0.12282915308368489 | 0.19569178986420643 | 3.234507089102376 | 1.0903961369382813 | 0.07637868965517246 | 0.15232718390804598 |
| Cable TV | 65 | 0.7554662883883042 | 0.5679703128061739 | 0.3622328230116077 | 0.14420905205944332 | 0.1590659174718642 | 0.09792108748685711 | 0.18408274350797957 | 0.2604030918814729 | 0.15332607716990518 | 1.0753176281434917 | 2.384572260037296 | 0.11667955555555555 | 0.05508066666666669 |
| Chemical (Basic) | 760 | 0.8552198047682432 | 0.4012822363293399 | 0.2863678892986606 | 0.13560934631730118 | 0.5781832192444376 | 0.03794786414692396 | 0.06686475346208993 | 0.08025228605821776 | 0.07988246125553582 | 1.316241942330472 | 1.060639255502786 | 0.0675595444191344 | 0.15996428571428578 |
| Chemical (Diversified) | 86 | 1.1120778099220623 | 0.4299073469067151 | 0.3006539884117132 | 0.20085321260663414 | 0.43493653823900535 | 0.03427503465720716 | 0.07962326301360768 | 0.09839017803856302 | 0.10520439986310327 | 1.7837911632234948 | 0.9623092765388879 | 0.07140233333333333 | 0.15671923076923072 |
| Chemical (Specialty) | 693 | 0.9876099368823831 | 0.20552205402128948 | 0.17048386077693437 | 0.16989302087685376 | 0.3049445934740809 | 0.079956873833185 | 0.12654674583283432 | 0.14694662312815943 | 0.1564395004319842 | 1.483864254694512 | 1.520622105749295 | 0.10949838164251209 | 0.15120170542635658 |
| Coal & Related Energy | 322 | 1.0757548208715932 | 0.2594770096065892 | 0.2060196475421489 | 0.06364950759288046 | 0.5514263850791699 | 0.08199958265714641 | 0.1567735152759357 | 0.10916985740378013 | 0.15358305657666582 | 0.9416384808059706 | 1.8090612687790892 | 0.15299490384615386 | 0.14795106382978723 |
| Computer Services | 938 | 0.9704560223755896 | 0.15815125276710823 | 0.13655492094771385 | 0.17314043826913458 | 0.2136432258993181 | 0.05444020734001125 | 0.08163227160201876 | 0.20432417520941148 | 0.28099025926948523 | 4.564667466092893 | 0.8959115373260229 | 0.09198083333333329 | 0.1471932835820895 |
| Computer Software | 1068 | 1.1209826591692842 | 0.07331932040043931 | 0.0683108176726801 | 0.11678616137799916 | 0.27503439810353125 | 0.14493953007243082 | 0.2249776516435234 | 0.16622455321494858 | 0.40080070456084116 | 1.965204241631464 | 3.2233775926743333 | 0.10538717728055086 | 0.19642245989304818 |
| Computers/Peripherals | 371 | 1.0399414870001082 | 0.16055733591747715 | 0.13834502695254497 | 0.12319420695893937 | 0.16876877870603219 | 0.050163651565618285 | 0.0996074548557677 | 0.17060782502642483 | 0.322028305271602 | 3.2790118216026256 | 0.9004708096851026 | 0.0021116044776119335 | 0.48319133333333314 |
| Construction | 466 | 0.745936812668947 | 0.48570393012533347 | 0.32691838547156543 | 0.14870416263118147 | 0.5094710027819449 | 0.05166408219303167 | 0.10845816846244229 | 0.07250781824152525 | 0.07891369144732974 | 0.8481856918583441 | 1.704600813353684 | 0.10746176245210724 | 0.18758888888888892 |
| Diversified | 365 | 0.6652974154239539 | 0.7908106036987248 | 0.44159365712118936 | 0.13263854043735607 | 0.2591790361756495 | 0.06179527022629034 | 0.09247910759284636 | 0.11533935395760675 | 0.0761540215267343 | 0.8837451818788739 | 1.4581180395235493 | 0.07647413654618479 | 0.13981737704918026 |
| Educational Services | 145 | 1.1031024607727393 | 0.20255881501219714 | 0.16843984051635982 | 0.14290141158144692 | NA | -0.01403993632183039 | 0.11075388321943491 | -0.025651076399905947 | 0.210148719249623 | 2.636793368629789 | 0.9651169580921649 | 0.15142337837837835 | 0.20398800000000006 |
| Electrical Equipment | 847 | 0.9649881723518031 | 0.2989050814689806 | 0.23012080384729697 | 0.13879982555845974 | 0.5069573429594733 | 0.032981334006264594 | 0.06861201190814321 | 0.0724166677165645 | 0.11046869484965495 | 2.098204123657942 | 1.0090025938388396 | 0.08431475982532753 | 0.20522314814814824 |
| Electronics | 1188 | 1.0126468071010164 | 0.3179539137357722 | 0.24124812743605287 | 0.12331604344824043 | 0.30540175710219 | 0.027825870237122782 | 0.0447780232075419 | 0.06199002218455373 | 0.06470274757966053 | 1.85020901395551 | 0.7421495734157086 | 0.02239268068331144 | 0.18274247311827962 |
| Electronics (Consumer & Office) | 208 | 0.961132779028457 | 0.5773025717640676 | 0.36600623247472924 | 0.12165777718118474 | NA | -0.052058401906441995 | 0.02322734936995355 | -0.13505139326274726 | 0.03569915742497714 | 2.4504434877885344 | 0.48953442238428213 | -0.013428731343283587 | 0.16821447368421052 |
| Engineering | 1141 | 0.806942599122774 | 0.8303561809829381 | 0.45365824947635064 | 0.1701593567499837 | 0.5922575545390728 | 0.017919433055986027 | 0.045211626841720524 | 0.0683046907346598 | 0.07925136959030997 | 2.2757879236704506 | 0.5633370919844753 | 0.08597636932707366 | 0.15760811518324608 |
| Entertainment | 356 | 0.9749569507953403 | 0.2871090769613308 | 0.2230650704749529 | 0.08794906626109351 | 0.2842705597771966 | 0.07879851198635245 | 0.1646308088586504 | 0.10390540803739289 | 0.21134795712387125 | 1.6925843357862418 | 1.9410773455684867 | 0.039765176470588234 | 0.20993333333333333 |
| Environmental & Waste Services | 307 | 0.8642548975521049 | 0.4091267219831157 | 0.29034061706482767 | 0.11246000869189886 | 0.6260129409795656 | 0.02971095459344241 | 0.08924937006429307 | 0.06760253214319623 | 0.13279400819461726 | 2.0421733652725154 | 1.306039278482039 | 0.12012215827338124 | 0.1479106382978723 |
| Farming/Agriculture | 331 | 0.7364460527692519 | 0.4289996636302488 | 0.3002097722965257 | 0.13556247840510444 | 0.28833943451517013 | 0.03837710652601635 | 0.048427677043770774 | 0.10863252097695207 | 0.07781068454938152 | 1.8238082439210621 | 0.7131189562685084 | 0.17258940540540546 | 0.22128653846153845 |
| Financial Svcs. | 520 | 0.17637371978368482 | 6.564552881776035 | 0.8678044802344992 | 0.17109463744167927 | 0.16509892038891955 | 0.21775914751861072 | 0.06432171983044993 | 0.14391791597558273 | 0.003762917933293578 | 0.08848854731021995 | 11.593068386017858 | 0.10600400696864103 | 0.1659487804878049 |
| Financial Svcs. (Non-bank & Insurance) | 149 | 0.1712216080391581 | 6.793527249204209 | 0.8716883937113187 | 0.1366889243277749 | 0.0800710423629135 | 0.13696964400690392 | 0.03314693419019023 | 0.06420316741239397 | 0.0021662602878458276 | 0.08676388304658694 | 11.239090965913565 | 0.1380515384615385 | 0.21864374999999997 |
| Food Processing | 1223 | 0.6895062630447725 | 0.2767559084451933 | 0.21676493260346127 | 0.15803628956335183 | 0.43332226955868974 | 0.04787408330032496 | 0.08049109827138382 | 0.1230230107915221 | 0.1362759095119226 | 2.125113847303741 | 1.1950356983691612 | 0.10361433427762043 | 0.2044492753623189 |
| Food Wholesalers | 115 | 0.5596366684399202 | 0.7098218909270163 | 0.415143761285084 | 0.18448459039776946 | 0.5415691781591184 | 0.010561017435403872 | 0.0299220781491584 | 0.10561856099836123 | 0.13976801342217993 | 5.50670520231214 | 0.3007281622312399 | 0.034304347826086955 | 0.11568461538461539 |
| Furn/Home Furnishings | 323 | 0.9372271288827345 | 0.2696951016677955 | 0.21240934245831156 | 0.1493135680037737 | 0.3024187066913847 | 0.04146175466983158 | 0.06109955933261131 | 0.12017637612584803 | 0.13604092310535362 | 2.625233806454642 | 0.7174563457332872 | 0.036747342995169095 | 0.2507333333333333 |
| Healthcare Equipment | 448 | 0.9213329275809832 | 0.1732580779708313 | 0.14767260607357924 | 0.08870461208860465 | 0.37019450550011695 | 0.09983466635472753 | 0.1820503607501299 | 0.13265633975637964 | 0.2436272710836722 | 1.49556011533465 | 2.5549842928891935 | 0.08267011952191237 | 0.15746168224299065 |
| Healthcare Facilities | 170 | 0.5371622038050927 | 0.8065445018743441 | 0.4464570349844856 | 0.16538599719658786 | 0.15049190096829418 | 0.04238883709621235 | 0.10370358638437478 | 0.26494571578328074 | 0.14161279452863604 | 1.6436800020524898 | 1.2813569227885169 | 0.1771103636363637 | 0.15739272727272718 |
| Healthcare Products | 155 | 0.7780646767860703 | 0.1941930031261014 | 0.1626144204644913 | 0.1349318259326525 | 0.2273499018398571 | 0.079536939530066 | 0.12139873573304395 | 0.1203120696789787 | 0.14312109514949417 | 1.3195166182224962 | 2.4877221996201886 | 0.14200838709677424 | 0.18056976744186048 |
| Healthcare Services | 328 | 0.8065360700509082 | 0.3197141486524402 | 0.24226015079015423 | 0.17340626474002085 | 0.16771109345716306 | 0.024750826294600434 | 0.047694670670050274 | 0.13813834432361616 | 0.30865733350331936 | 7.185047217418871 | 0.4608995141895921 | 0.1316736559139785 | 0.16521136363636357 |
| Heathcare Information and Technology | 266 | 0.9576996000657071 | 0.20133005407188312 | 0.1675892927089263 | 0.0816133146561142 | 0.14885221977589477 | 0.06269419832011934 | 0.12095557165169515 | 0.07836447808815242 | 0.1638924079003069 | 1.5388007968032071 | 2.332882287501829 | 0.12098006493506491 | 0.21924999999999994 |
| Heavy Construction | 334 | 0.9877796840713766 | 0.601318658250976 | 0.3755146767026122 | 0.17815265118590995 | 0.3136729592806846 | 0.04742283815998131 | 0.08316778222699493 | 0.15655875310546627 | 0.11920762668622706 | 1.5703830740544145 | 0.9931079555787211 | 0.09792696261682243 | 0.10969181818181817 |
| Homebuilding | 155 | 0.9995325077493526 | 0.5809414068902092 | 0.36746548882728675 | 0.19215422200751384 | 0.1451478351646075 | 0.041558624569370366 | 0.06605229541232203 | 0.07734825438611916 | 0.059392944408518944 | 1.2431620321775052 | 0.9852842770417638 | 0.013634513274336237 | 0.10354644067796606 |
| Hotel/Gaming | 618 | 0.8376390265636493 | 0.30366043825575595 | 0.23292908900575454 | 0.12186971587012083 | 0.3652028900912334 | 0.05729780746490251 | 0.11797914928322414 | 0.08021211075012151 | 0.10345451818433932 | 0.9501762402867041 | 2.2367214764519407 | 0.10034530555555561 | 0.1485308411214953 |
| Household Products | 456 | 0.8244388238017719 | 0.1425007187182826 | 0.12472702763648798 | 0.13978245053109692 | 0.43815672817780654 | 0.08682774594203696 | 0.1434108368888912 | 0.16859297245233154 | 0.220788362053318 | 2.135204047737053 | 2.0869523901656093 | 0.11761748953974895 | 0.160625 |
| Information Services | 171 | 0.9808332115529819 | 0.1212529539627874 | 0.10814058820023549 | 0.16193277237551737 | 0.31170390799523884 | 0.10402596047114963 | 0.22044992698719107 | 0.15349634135996265 | 0.42965822082651955 | 2.3628885968790043 | 3.0490106738873206 | 0.06263203883495146 | 0.14572340425531918 |
| Insurance (General) | 220 | 0.713771885072913 | 0.5751071307174891 | 0.3651225491281458 | 0.13645540744885346 | 0.21451491169699607 | 0.05889647408407331 | 0.07960773713283348 | 0.11516650867187996 | 0.10663154685357988 | 1.5594996148538192 | 0.6744109294578173 | 0.0598093396226415 | 0.15554666666666667 |
| Insurance (Life) | 117 | 0.9357010004854667 | 0.6134886257443981 | 0.3802249460924209 | 0.17281213692012987 | 0.3475894223446705 | 0.0366796496420723 | 0.06604670563694326 | 0.07682586041143762 | 0.0895438042903116 | 1.503432371008983 | 0.773069991737285 | 0.050657123287671225 | 0.12514037037037035 |
| Insurance (Prop/Cas.) | 220 | 0.6523391105660923 | 0.3918364132313591 | 0.2815247607451593 | 0.1195513555814225 | 0.31865051217906476 | 0.04423168622080606 | 0.07640592344147122 | 0.07354002692472876 | 0.07580065191454939 | 1.229438069499061 | 0.9109089922510611 | 0.08422740740740739 | 0.19509999999999997 |
| Internet software and services | 715 | 1.2164394795752738 | 0.04718963077356905 | 0.04506311883427419 | 0.07767714338308349 | 0.042940942548123404 | 0.18744630180525673 | 0.21155268706139005 | 0.19320752389597776 | 0.2400085201563208 | 1.254942286471069 | 4.3368570412952305 | 0.09164672535211274 | 0.2377296296296296 |
| Investment Co. | 448 | 0.577961585582578 | 0.9577693426539983 | 0.48921459836306536 | 0.05970845760587014 | 0.38861216341403965 | 0.14528890362817856 | 0.11325887895843466 | 0.08105595809381362 | 0.03206156870108404 | 0.29110754924812615 | 3.623487692955142 | 0.08469912408759121 | 0.10659629629629631 |
| Machinery | 1249 | 1.0616242962155311 | 0.25234116505139575 | 0.20149554457953137 | 0.17476985347537002 | 0.32017373668819665 | 0.053200575959943326 | 0.08920435272049397 | 0.10869640226810397 | 0.12833536035812584 | 1.8302297186091707 | 1.1322649397767812 | 0.03893315000000003 | 0.15817253218884117 |
| Metals & Mining | 1700 | 1.077588444010954 | 0.2700246732765312 | 0.21261372236170473 | 0.04261176323606318 | 0.4589838723812469 | 0.07443025143426593 | 0.15438431988927054 | 0.1076293826341149 | 0.12829366758384567 | 1.003452417769306 | 1.5796570538682242 | 0.2044447004608295 | 0.10672523809523808 |
| Office Equipment & Services | 162 | 0.8111925401445732 | 0.3217251844940814 | 0.24341306972767457 | 0.17479460512890282 | 0.41760302581836367 | 0.04245485662783156 | 0.07347821488154434 | 0.12397797311852346 | 0.152120842672437 | 2.595291262275346 | 0.721047691528013 | 0.025301403508771938 | 0.145785 |
| Oil/Gas (Integrated) | 55 | 1.1217380663582095 | 0.22110974966000363 | 0.181072790321728 | 0.25527163074658776 | 0.27548640759930776 | 0.07678921788354612 | 0.10778228702832933 | 0.16801912796082355 | 0.1265273232069136 | 1.692896955771231 | 0.7351457642335234 | 0.1400488372093023 | 0.08799885714285716 |
| Oil/Gas (Production and Exploration) | 1219 | 1.0496976595872094 | 0.30674442351287806 | 0.23473941651747562 | 0.06406328753559688 | 0.44131061681687545 | 0.07343483965636712 | 0.17881029142643576 | 0.07135065351546953 | 0.0865604323942608 | 0.6771502798741666 | 2.2053830839453354 | 0.21471744466800793 | 0.18546942708333336 |
| Oil/Gas Distribution | 198 | 0.7013757412483823 | 0.6184501640559521 | 0.3821249351948358 | 0.08919672515398057 | 1.1526548022092855 | 0.05031534592199196 | 0.1037924698671696 | 0.11001829826166515 | 0.08705628137459863 | 0.7314817011393656 | 2.230725966326768 | 0.16368935779816518 | 0.1739738461538462 |
| Oilfield Svcs/Equip. | 570 | 1.1201859459063455 | 0.3667376161622173 | 0.268330667002502 | 0.1421863007111455 | 0.2659192963041813 | 0.023551684219607235 | 0.042447162980928335 | 0.11205608582901963 | 0.1101238512495032 | 3.2779380568371916 | 0.52178517197565 | 0.15375774509803913 | 0.26788618421052623 |
| Packaging & Container | 399 | 0.6490052273076146 | 0.6306037930500681 | 0.38673023804913065 | 0.1716807898350111 | 0.4318290181623616 | 0.02797930537762138 | 0.07511267763526766 | 0.07734029546083633 | 0.1105266130122913 | 1.7407730165352109 | 0.8946689739267623 | 0.09612577405857746 | 0.16012682926829266 |
| Paper/Forest Products | 318 | 0.6406801567005922 | 0.9194742886464661 | 0.4790240192770914 | 0.11752427845115958 | 0.8078583259387617 | 0.019528918368241877 | 0.05175175131635336 | 0.034678800358791326 | 0.03977068415370108 | 1.0229310528463218 | 1.0610294672543215 | 0.06174920000000002 | 0.13857394736842102 |
| Pharma & Drugs | 823 | 0.8785475193240015 | 0.14738193988584264 | 0.12845063597611292 | 0.12527630917514948 | 0.4483047079124804 | 0.1254816537386081 | 0.21124547312139913 | 0.1375646661561575 | 0.18458485885143924 | 1.1313130641911926 | 2.7768781329496357 | 0.13718281779661015 | 0.18461901840490796 |
| Power | 719 | 0.46571159919936733 | 1.0583687750729447 | 0.5141784056821588 | 0.15121433315735014 | 0.9376739198353625 | 0.036183440206134725 | 0.104906410179654 | 0.052288425233671075 | 0.051415934522440754 | 0.638823905588249 | 1.8008799264794775 | 0.1396811335012595 | 0.11643202072538869 |
| Precious Metals | 1237 | 1.1564456467576896 | 0.1465523720712881 | 0.1278200417539898 | 0.03516389475832645 | 0.6188837589679226 | 0.06980955840987062 | 0.1862807238392009 | 0.04966858814854403 | 0.08786888458148148 | 0.5849436015273151 | 3.0160871637482276 | 0.40883678414096913 | 0.18469026315789464 |
| Publshing & Newspapers | 401 | 0.7481954904573297 | 0.3977324251161451 | 0.28455548284436155 | 0.15266991732439025 | 17.31520979218116 | 0.001574471423788836 | 0.07953033621999005 | 0.0025763947429641824 | 0.10443540215658349 | 1.790902713226729 | 1.1827907209052237 | 0.014528235294117649 | -0.04046393442622949 |
| R.E.I.T. | 48 | 0.14150887038897503 | 5.606041602190603 | 0.8486234177410578 | 0.029900643410690386 | 0.5573909002576996 | 0.6188933974237911 | 0.02670916771867391 | 0.10893496307020913 | 0.0006949098245919868 | 0.021027730843958935 | 47.02769443264511 | 0.02020526315789473 | 0.049420000000000006 |
| Railroad | 56 | 0.46247723844838884 | 0.6538313066569706 | 0.3953434089832386 | 0.21559827941420054 | 0.24665614310999281 | 0.09068783309888309 | 0.1799760520378999 | 0.11677176289259959 | 0.0727314001115381 | 0.5951064810221759 | 2.267057557243025 | 0.038290222222222225 | 0.1727025 |
| Real Estate | 415 | 0.6860087566419517 | 0.7708545115861325 | 0.4353008711572176 | 0.12959918552261648 | 0.2243769535027542 | 0.13080000184855392 | 0.15391785644426387 | 0.08509954824983386 | 0.04323068065845561 | 0.3149407091897547 | 3.243399722069833 | 0.05647551020408164 | 0.18537355555555554 |
| Real Estate (Development) | 611 | 0.8420947066045065 | 0.6459256045476897 | 0.3924391252939977 | 0.17320779751389026 | 0.3250775123098458 | 0.1974114073549542 | 0.24177438014744446 | 0.1295688476320063 | 0.07282999542687132 | 0.35775391566685766 | 3.1001233183999117 | 0.12444557894736849 | 0.19952306818181811 |
| Real Estate (Operations & Services) | 439 | 0.5588500819945951 | 0.8583817828518217 | 0.46189743720720966 | 0.13512592888789257 | 0.2235699523302163 | 0.2299387992412225 | 0.29362023765571643 | 0.0875917987647817 | 0.04577482262465286 | 0.17507772378329567 | 6.03304918824143 | 0.10175546558704462 | 0.15898363636363635 |
| Recreation | 292 | 0.8596253249977058 | 0.3183772226437757 | 0.24149174999043574 | 0.153036616419371 | 0.2825342368455445 | 0.05971617330479959 | 0.11005988402328172 | 0.09654364129858874 | 0.10465064712137845 | 1.3056284765850021 | 1.3113308009175424 | 0.019278839779005533 | 0.16353269230769235 |
| Reinsurance | 35 | 0.8585258660935746 | 0.4278877990568591 | 0.29966486116029933 | 0.11474449308985862 | 0.24173847558688022 | 0.08864108516509793 | 0.122955951055032 | 0.14392365263547266 | 0.15666046180161236 | 1.250042691737536 | 0.7324744474182655 | 0.060190370370370366 | 0.1529625 |
| Restaurant | 298 | 0.6222293474649695 | 0.2325521987457202 | 0.1886753347909905 | 0.20902208001557498 | 0.4097852374522096 | 0.06141535712587169 | 0.113733718545026 | 0.19631804747123466 | 0.18978398040723612 | 2.1986622118295704 | 1.55335949537561 | 0.06483358695652176 | 0.1553426315789473 |
| Retail (Automotive) | 138 | 0.7445897859163982 | 0.5159921077748085 | 0.3403659591158346 | 0.19418999899345732 | 0.16707367227571 | 0.028178681734171714 | 0.05115970360431199 | 0.17681722990321677 | 0.1295642364407921 | 3.1065697173456903 | 0.6312873322383906 | 0.06016524390243902 | 0.15756428571428574 |
| Retail (Building Supply) | 51 | 0.6764338986376054 | 0.187950862762666 | 0.15821434089081146 | 0.23149991805645453 | 0.3816953680226249 | 0.039104905237575156 | 0.07432923013573411 | 0.13278473782715688 | 0.12752847877683246 | 2.716956495956818 | 0.9504415424845695 | 0.05101032258064517 | 0.13614375 |
| Retail (Distributors) | 842 | 0.6118186242746338 | 0.9772598677646445 | 0.4942495843348441 | 0.1916185872887992 | 0.3047397064815131 | 0.02595679518855173 | 0.03521367330950831 | 0.11505537452001545 | 0.059033005064178926 | 2.0578082248880514 | 0.5741604830253084 | 0.06287957952468001 | 0.16590471698113202 |
| Retail (General) | 226 | 0.7761450930136155 | 0.3206671606864917 | 0.24280694654344762 | 0.22208440799120893 | 0.35735866476787975 | 0.028222240632174427 | 0.05104524273965269 | 0.13345534276401574 | 0.12281433543393164 | 3.283096065155698 | 0.6505170819121026 | 0.07691030303030305 | 0.15608163636363634 |
| Retail (Grocery and Food) | 170 | 0.5388332021038814 | 0.3810813211543843 | 0.27592967576728605 | 0.23429834976182382 | 0.39982567386956547 | 0.021535981280594186 | 0.041442453248080095 | 0.12109185720802973 | 0.12940696233612775 | 3.955631284806601 | 0.4823152517987793 | 0.05926491379310343 | 0.13191666666666665 |
| Retail (Internet) | 108 | 1.080958590409468 | 0.04996752444284026 | 0.04758959042028967 | 0.11104019915513458 | 0.21173029441121505 | 0.028320932710000336 | 0.050165908775816434 | 0.14072969077098335 | 0.44105144417936853 | 7.823558897659857 | 2.1112097622148145 | 0.1255171428571428 | 0.31942941176470596 |
| Retail (Special Lines) | 536 | 1.0097732353365025 | 0.13846521421926775 | 0.12162445763810525 | 0.20099906012997903 | 0.316254926716001 | 0.03533204868502171 | 0.06620384166426531 | 0.1363485235554303 | 0.185265572472415 | 3.9357251813910565 | 0.7939385138959401 | 0.050006084507042255 | 0.12166972067039108 |
| Rubber& Tires | 91 | 0.8354025515158929 | 0.5166199001809073 | 0.3406390092331528 | 0.16863410770069473 | 0.16286086037556274 | 0.047101283845691753 | 0.08101466684471552 | 0.1586886627463394 | 0.11743574953244992 | 1.7690917032377307 | 0.7803403458809475 | 0.10448872727272727 | 0.3567 |
| Semiconductor | 564 | 1.1951111769105758 | 0.1387672783500226 | 0.12185745146373068 | 0.08186553411285777 | 0.3844159488711002 | 0.07210802799028206 | 0.11304414245383274 | 0.10198236053112676 | 0.12923674209955568 | 1.3033747048715254 | 1.6611199188872057 | 0.057029520958083786 | 0.17728076923076921 |
| Semiconductor Equip | 264 | 1.4884850652482655 | 0.22441067373727866 | 0.18328055982418723 | 0.07822033017876333 | NA | -0.013725178529108734 | 0.07821014477251784 | -0.016594550237347485 | 0.07966313543084196 | 1.2070717291954853 | 1.5211266147931457 | 0.008660337837837847 | 0.12938728813559328 |
| Shipbuilding & Marine | 351 | 0.679437375871176 | 0.9070826659041583 | 0.47563888137701965 | 0.11282263784898455 | 4.971445839144591 | 0.003518758842311116 | 0.05053346367914989 | 0.005369301272204654 | 0.029658550158644766 | 0.824826004694854 | 1.2362135865826847 | 0.08502009174311928 | 0.01872323943661971 |
| Shoe | 95 | 1.0625745588883744 | 0.07416603846271236 | 0.06904522746674688 | 0.16816489888712244 | 0.1813012156668971 | 0.07160552734656898 | 0.0981483462603726 | 0.16285188850096152 | 0.18162099718869681 | 2.1224223114715013 | 1.2745583314977604 | 0.08984879999999996 | 0.14722916666666666 |
| Steel | 725 | 0.861760758573123 | 0.8101773973469961 | 0.4475679557895241 | 0.12676501987562283 | 4.114254266931165 | 0.003252065398094963 | 0.03862452889565955 | 0.007175465171233853 | 0.03969900046956261 | 1.3566779998527492 | 0.7463011380699954 | 0.08348893719806764 | 0.17150891089108913 |
| Telecom (Wireless) | 117 | 0.7949809663324604 | 0.31987181735428366 | 0.24235066856376614 | 0.1475658917157882 | 1.1137504908395501 | 0.049038949478821835 | 0.168605471400268 | 0.06287594568565473 | 0.12458700319836691 | 0.9567925072795207 | 1.8716334698373602 | 0.08432202702702703 | 0.11641874999999997 |
| Telecom. Equipment | 550 | 1.1840291680545039 | 0.15229622542804117 | 0.1321675989795662 | 0.09090255701780887 | 0.4605326670805373 | 0.05895306715569181 | 0.07462199940806577 | 0.09431720712469435 | 0.11819701789794725 | 1.9256100372650315 | 1.3674961737803535 | 0.035465621118012464 | 0.18691704545454543 |
| Telecom. Services | 325 | 0.6299698495531795 | 0.6553911705211956 | 0.39591317278492394 | 0.11920703995126393 | 1.0339697949541493 | 0.055795320953155154 | 0.14711522732832852 | 0.09014240064515872 | 0.12331212771077386 | 0.9834016635045989 | 1.558557206914213 | 0.07878063829787237 | 0.08790970873786409 |
| Thrift | 295 | 0.016637483459917994 | 54.32464544466445 | 0.9819248728670084 | 0.1811327397904755 | 0.0915776417414007 | 0.3906671476315644 | 0.0059168972719338825 | -0.12111315907996777 | -2.4656018583649233e-05 | 0.008952674053599006 | 112.28359791108633 | 0.07267438775510202 | 0.08289375000000002 |
| Tobacco | 48 | 0.4922590174039195 | 0.15475655890102114 | 0.13401660956860253 | 0.19698487088734332 | 0.6368136208619423 | 0.1671479066045681 | 0.2810221752780475 | 0.4421782859544788 | 0.4751702492315706 | 2.4389838058440465 | 3.333950094908089 | 0.06184035714285715 | 0.09459411764705883 |
| Tranportation | 223 | 0.7471454506660183 | 0.4874970823222164 | 0.32772977380309004 | 0.19613021401302577 | 0.42975743412378825 | 0.05007352034596984 | 0.08456568737942022 | 0.13013099081182752 | 0.10366702098750585 | 1.5974978209037471 | 1.137379149181088 | 0.11172653061224488 | 0.14340619047619044 |
| Trucking | 185 | 0.5514281925875475 | 0.7754613022351555 | 0.4367660963710757 | 0.2199122599369534 | 0.21812551194103877 | 0.029465857176536724 | 0.061624276467070395 | 0.10184953838667171 | 0.07811057921674786 | 1.719017269098458 | 0.7865143490187407 | 0.030354491525423716 | 0.13647162790697673 |
| Utility (General) | 61 | 0.4092429627233454 | 1.071545652846446 | 0.5172686642817013 | 0.23562575538381228 | 0.9100127833583915 | 0.037059941957485985 | 0.10480085437795794 | 0.07058431686340684 | 0.08116224139252551 | 1.001731149253729 | 1.237676867421589 | 0.084894 | 0.05629189189189191 |
| Utility (Water) | 97 | 0.5298693339709419 | 0.631753986496177 | 0.3871625206522253 | 0.14778558636229275 | 0.5481269725587617 | 0.16275558535976425 | 0.27530904590779515 | 0.12471742167885883 | 0.08805538150684483 | 0.35872089990485506 | 4.031291294376952 | 0.17203677419354835 | 0.12973076923076923 |
| Grand Total | 40943 | 0.6355910813297938 | 0.9895575604643776 | 0.4973756880064367 | 0.13402898988096504 | 0.3749472513808136 | 0.05736021964346198 | 0.08633127960618246 | 0.10486543314268132 | 0.05107573107841359 | 0.7708271921128489 | 1.7597823349023778 | 0.0893572594828718 | 0.1607019743935307 |
