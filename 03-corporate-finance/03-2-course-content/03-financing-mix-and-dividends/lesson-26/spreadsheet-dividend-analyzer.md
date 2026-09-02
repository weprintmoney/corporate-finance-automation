---
title: "Spreadsheet: Dividend Analyzer"
status: active
owner: weprintmoney
created: 2026-09-01
last_updated: 2026-09-01
---

## Read me first
| 0                           | 1                                                                                                                                              |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Analysis of Dividend Policy | nan                                                                                                                                            |
| Objective                   | 1. To compare how much a firm has returned to its stockholder historically (up to 10 years) with how much it could have returned.              |
| nan                         | 2. To provide an assessment of project quality (ROE compared to cost of equity) and stock price performance over the period.                   |
| nan                         | 3. To provide forecasts of how much cash the firm will have available for stock buybacks in the future                                         |
| Inputs needed               | For historical analysis:                                                                                                                       |
| nan                         | a. Net Income                                                                                                                                  |
| nan                         | b. Depreciation, amortization and other non-cash charges                                                                                       |
| nan                         | c. Capital expenditures: Please include acquisitions as part of capital expenditures                                                           |
| nan                         | d. Non-cash working capital changes                                                                                                            |
| nan                         | In entering these numbers, please make sure that you get the signs right (check the comment box on each of these inputs)                       |
| nan                         | e. Dividends: Only cash dividends should be shown here (ignore stock dividends)                                                                |
| nan                         | f. Stock Buybacks: Include the cash flow associated with stock buybacks.                                                                       |
| nan                         | For project assessment and stock price performance analysis                                                                                    |
| nan                         | a. Beta: You should really use an average beta over the historical period, but go ahead and use your current beta if you do not have this.     |
| nan                         | b. Book Value of Equity: To compute return on equity.                                                                                          |
| nan                         | c. Return on the stock: This is the total return you would have made as an investor: It includes price appreciation + dividend yield each year |
| nan                         | d. Riskfree rate: The one-year government security rate at the start of each year (use the T.Bill rate)                                        |
| nan                         | e. Return on Stock Market: This is the total return on the stock market each year                                                              |
| nan                         | (You can get the last two from the worksheet that is part of this spreadsheet that reports historical data on both)                            |
| nan                         | For forecasts                                                                                                                                  |
| nan                         | a. Expected growth rates in net income, dividends, depreciation, capital expenditures and revenues                                             |
| nan                         | b. Working capital as a percent of revenues                                                                                                    |
| nan                         | c. Debt as a percent of reinvestment, looking forward. As a default, you can use your historical average.                                      |
| Output                      | Historical Analysis                                                                                                                            |
| nan                         | 1. FCFE and Cash Returned each year for the historical period                                                                                  |
| nan                         | 2. Returns on equity, the stock and your required return each year for the historical period                                                   |
| nan                         | 3. Averages of both over the entire period                                                                                                     |
| nan                         | Forecasts                                                                                                                                      |
| nan                         | 1. Forecasted FCFE for next 5 years                                                                                                            |
| nan                         | 2. Forecasted dividends for next 5 years                                                                                                       |
| nan                         | 3. Cash available each year for stock buybacks for next 5 years.                                                                               |

## Inputs
| 0                                                                                                                                                                                                                              | 1                     | 2                           | 3                                        | 4                                            | 5                                                                               |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|:----------------------------|:-----------------------------------------|:---------------------------------------------|:--------------------------------------------------------------------------------|
| Section 1: Inputs for estimating Dividends and FCFE                                                                                                                                                                            | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| How many years of historical data do you have available?                                                                                                                                                                       | nan                   | nan                         | nan                                      | 5                                            | (number of years)                                                               |
| Current debt to capital ratio =                                                                                                                                                                                                | nan                   | nan                         | nan                                      | 0.11579296585803885                          | nan                                                                             |
| Do you want to want to change this ratio to a target debt ratio?                                                                                                                                                               | nan                   | nan                         | nan                                      | No                                           | nan                                                                             |
| If yes, enter the target debt ratio to use =                                                                                                                                                                                   | nan                   | nan                         | nan                                      | 0.4                                          | nan                                                                             |
| nan                                                                                                                                                                                                                            | nan                   | nan                         | nan                                      | Use less years, if you do not have the data. | nan                                                                             |
| Enter the following data for the years for which you have data (starting with the most recent year of data and working backwards).                                                                                             | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Year                                                                                                                                                                                                                           | Net Income            | Depreciation & Amortization | Capital Spending & operating investments | Chg in Non-Cash WC                           | Net Debt Issued                                                                 |
| 1                                                                                                                                                                                                                              | 6136                  | 2192                        | 2796                                     | -133                                         | 1881                                                                            |
| 2                                                                                                                                                                                                                              | 5682                  | 1987                        | 3784                                     | 940                                          | 4246                                                                            |
| 3                                                                                                                                                                                                                              | 4807                  | 1841                        | 3559                                     | 950                                          | 2743                                                                            |
| 4                                                                                                                                                                                                                              | 3963                  | 1713                        | 2110                                     | 308                                          | 1190                                                                            |
| 5                                                                                                                                                                                                                              | 3307                  | 1631                        | 1753                                     | -109                                         | -235                                                                            |
| 0                                                                                                                                                                                                                              | 4427                  | 1582                        | 1586                                     | 485                                          | 1005                                                                            |
| 0                                                                                                                                                                                                                              | 4687                  | 1491                        | 1566                                     | 45                                           | 4990                                                                            |
| 0                                                                                                                                                                                                                              | 3374                  | 1437                        | 1319                                     | -136                                         | 2891                                                                            |
| 0                                                                                                                                                                                                                              | 2533                  | 1339                        | 1823                                     | 270                                          | 1076                                                                            |
| 0                                                                                                                                                                                                                              | 2345                  | 1210                        | 1427                                     | 51                                           | 276                                                                             |
| Enter the dollar dividends paid and equity repurchases for each year of historical data (staring with most recent year): (Equity repurchases are in the statement of cash flows)                                               | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Year                                                                                                                                                                                                                           | Dividends (aggregate) | Equity Repurchases (in $)   | nan                                      | nan                                          | nan                                                                             |
| 1                                                                                                                                                                                                                              | 1324                  | 4087                        | nan                                      | nan                                          | nan                                                                             |
| 2                                                                                                                                                                                                                              | 1076                  | 3015                        | nan                                      | nan                                          | nan                                                                             |
| 3                                                                                                                                                                                                                              | 756                   | 4993                        | nan                                      | nan                                          | nan                                                                             |
| 4                                                                                                                                                                                                                              | 653                   | 2669                        | nan                                      | nan                                          | nan                                                                             |
| 5                                                                                                                                                                                                                              | 648                   | 648                         | nan                                      | nan                                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 664                   | 4453                        | nan                                      | nan                                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 637                   | 6923                        | nan                                      | nan                                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 519                   | 6898                        | nan                                      | nan                                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 490                   | 2420                        | nan                                      | nan                                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 430                   | 335                         | nan                                      | nan                                          | nan                                                                             |
| Section 2: Assessing Investment Quality and Stock Performance                                                                                                                                                                  | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| The following section of the dividend policy analysis looks at the quality of your firm's investments and the risk-adjusted, market-adjusted performance of your stock over the period. If                                     | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| you have a measure of excess returns (ROIC- Cost of capital) or  a Jensen's alpha computed for your stock, you can use those measures instead of the ones computed here.                                                       | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| The last set of inputs to this analysis relate to project choice and performance:                                                                                                                                              | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Enter the beta for the equity of this firm:                                                                                                                                                                                    | nan                   | nan                         | 0.9011                                   | nan                                          | nan                                                                             |
| Enter the following data relating to performance (starting with most recent year): (Make sure that you update the riskfree rate and return on the market from the attached worksheet to reflect the time period for your data) | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Year                                                                                                                                                                                                                           | BV: Equity            | Annual return on stock      | T.Bill rate                              | Return on market                             | nan                                                                             |
| 1                                                                                                                                                                                                                              | 380078                | 0.32145085858125483         | 0.00066                                  | 0.32145085858125483                          | Note: I have the numbers for the US in the Historical stock & t.bill worksheet. |
| 2                                                                                                                                                                                                                              | 330056                | 0.24733553840499822         | 0.0005                                   | 0.15890585241730293                          | Please match up the annual data for the years for your company.                 |
| 3                                                                                                                                                                                                                              | 194181                | -0.07288542291541701        | 0.0003                                   | 0.0209837473362805                           | If you are in foreign market and don't                                          |
| 4                                                                                                                                                                                                                              | 84200                 | nan                         | 0.0013                                   | 0.14821092278719414                          | have these numbers, leave them at the US levels.                                |
| 5                                                                                                                                                                                                                              | 63437                 | nan                         | 0.00135                                  | 0.2593523387766398                           | nan                                                                             |
| 0                                                                                                                                                                                                                              | 91658                 | nan                         | 0.01585                                  | -0.3655234411179819                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 79717                 | nan                         | 0.046425                                 | 0.054847352464217694                         | nan                                                                             |
| 0                                                                                                                                                                                                                              | 63054                 | nan                         | 0.046775000000000004                     | 0.15612557979315703                          | nan                                                                             |
| 0                                                                                                                                                                                                                              | 44602                 | nan                         | 0.0301                                   | 0.048344775232688535                         | nan                                                                             |
| 0                                                                                                                                                                                                                              | 37019                 | nan                         | 0.012275000000000001                     | 0.10742775944096193                          | nan                                                                             |
| Section 3: Inputs for forecasting future dividends and FCFE                                                                                                                                                                    | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Use these inputs if you want to make projection of FCFE for the future                                                                                                                                                         | nan                   | nan                         | nan                                      | nan                                          | nan                                                                             |
| Expected growth in Revenues over next 5 years =                                                                                                                                                                                | nan                   | nan                         | nan                                      | 0.05                                         | nan                                                                             |
| Expected growth in Net Income over next 5 years =                                                                                                                                                                              | nan                   | nan                         | nan                                      | 0.05                                         | nan                                                                             |
| Expected growth in capital expenditures in next 5 years =                                                                                                                                                                      | nan                   | nan                         | nan                                      | 0.05                                         | nan                                                                             |
| Expected growth in depreciation in next 5 years =                                                                                                                                                                              | nan                   | nan                         | nan                                      | 0.05                                         | nan                                                                             |
| Enter non-cash working capital as a percent of revenues                                                                                                                                                                        | nan                   | nan                         | nan                                      | 0.06                                         | nan                                                                             |
| Enter revenues from most recent year =                                                                                                                                                                                         | nan                   | nan                         | nan                                      | 42278                                        | nan                                                                             |
| Enter net income from most recent year or normalized value =                                                                                                                                                                   | nan                   | nan                         | nan                                      | 6136                                         | nan                                                                             |
| Enter capital expenditures from most recent year or normalized value =                                                                                                                                                         | nan                   | nan                         | nan                                      | 2796                                         | nan                                                                             |
| Enter depreciation in most recent year =                                                                                                                                                                                       | nan                   | nan                         | nan                                      | 2192                                         | nan                                                                             |
| Enter dividends paid in the most recent year =                                                                                                                                                                                 | nan                   | nan                         | nan                                      | 1324                                         | nan                                                                             |
| Expected growth in dividends                                                                                                                                                                                                   | nan                   | nan                         | 0.05                                     | nan                                          | nan                                                                             |

## Analysis of past dividends
| 0                                     | 1                    | 2                    |             3 |            4 |            5 | 6   | 7   | 8   | 9   | 10   | 11                |
|:--------------------------------------|:---------------------|:---------------------|--------------:|-------------:|-------------:|:----|:----|:----|:----|:-----|:------------------|
| Analysis of Past Dividends            | nan                  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| nan                                   | 1                    | 2                    |    3          |    4         |    5         | 0   | 0   | 0   | 0   | 0    | Aggregate         |
| Net Income                            | 6136                 | 5682                 | 4807          | 3963         | 3307         |     |     |     |     |      | 23895             |
| - (Cap. Exp - Depr)                   | 604                  | 1797                 | 1718          |  397         |  122         |     |     |     |     |      | 4638              |
| - ∂ Working Capital                   | -133                 | 940                  |  950          |  308         | -109         |     |     |     |     |      | 1956              |
| Free CF to Equity (pre-debt)          | 5665                 | 2945                 | 2139          | 3258         | 3294         | 0   | 0   | 0   | 0   | 0    | 17301             |
| + Net Debt Issued                     | 1881                 | 4246                 | 2743          | 1190         | -235         |     |     |     |     |      | 9825              |
| = Free CF to Equity (actual debt)     | 7546                 | 7191                 | 4882          | 4448         | 3059         |     |     |     |     |      | 27126             |
| Free CF to Equity (target debt ratio) | 5719.538486919137    | 3261.9253475534524   | 2447.94       | 3339.63      | 3295.51      | 0   | 0   | 0   | 0   | 0    | 18064.53881686791 |
| Dividends                             | 1324                 | 1076                 |  756          |  653         |  648         |     |     |     |     |      | 4457              |
| + Equity Repurchases                  | 4087                 | 3015                 | 4993          | 2669         |  648         | 0   | 0   | 0   | 0   | 0    | 15412             |
| = Cash to Stockholders                | 5411                 | 4091                 | 5749          | 3322         | 1296         |     |     |     |     |      | 19869             |
| Dividend Ratios                       | nan                  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Payout Ratio                          | 0.21577574967405475  | 0.18936994016191483  |    0.157271   |    0.164774  |    0.195948  |     |     |     |     |      | nan               |
| Cash Paid as % of FCFE                | 0.7170686456400742   | 0.5689055764149632   |    1.17759    |    0.746853  |    0.423668  |     |     |     |     |      | nan               |
| Performance Ratios                    | nan                  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| 1. Accounting Measure                 | nan                  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| ROE                                   | 0.01614405464141571  | 0.017215260440652497 |    0.0247553  |    0.0470665 |    0.0521305 |     |     |     |     |      | nan               |
| Required rate of return               | 0.28972464266756875  | 0.14323951361323167  |    0.0189381  |    0.133681  |    0.233836  |     |     |     |     |      | nan               |
| ROE - Cost of Equity                  | -0.27358058802615304 | -0.12602425317257918 |    0.00581713 |   -0.0866149 |   -0.181705  |     |     |     |     |      | nan               |
| 2. Stock Performance Measure          | nan                  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Returns on stock                      | 0.32145085858125483  | 0.24733553840499822  |   -0.0728854  |    0         |    0         |     |     |     |     |      | nan               |
| Required rate of return               | 0.28972464266756875  | 0.14323951361323167  |    0.0189381  |    0.133681  |    0.233836  |     |     |     |     |      | nan               |
| Jensen's alpha                        | 0.03172621591368607  | 0.10409602479176655  |   -0.0918235  |   -0.133681  |   -0.233836  |     |     |     |     |      | nan               |
| Index                                 | 1                    | 1                    |    1          |    1         |    1         | 0   | 0   | 0   | 0   | 0    | nan               |
| nan                                   | Aggregate            | Average              |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Net Income                            | 23895                | 4779                 |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Dividends                             | 4457                 | 891.4                |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Dividend Payout Ratio                 | 0.18652437748482947  | 0.1846276973824568   |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Stock Buybacks                        | 15412                | 3082.4               |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Dividends + Buybacks                  | 19869                | 3973.8               |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Cash Payout Ratio                     | 0.8315128688010044   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Free CF to Equity (pre-debt)          | 17301                | 3460.2               |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Free CF to Equity (actual debt)       | 27126                | 5425.2               |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Free CF to Equity (target debt ratio) | 18064.53881686791    | 3612.907763373582    |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Cash payout as % of pre-debt FCFE     | 1.1484307265475984   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Cash payout as % of actual FCFE       | 0.732470692324707    | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Cash payout as % of target FCFE       | 1.0998896900399782   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| ROE                                   | 0.0301615056118339   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Return on Stock                       | 0.0991801948141672   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Required Return                       | 0.1638839242001387   | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| ROE - Required return                 | -0.1337224185883048  | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |
| Actual - Required Return              | -0.06470372938597149 | nan                  |  nan          |  nan         |  nan         | nan | nan | nan | nan | nan  | nan               |

## Forecasted Dividends & FCFE
| 0                                     |            1 |         2 |         3 |         4 |         5 |
|:--------------------------------------|-------------:|----------:|----------:|----------:|----------:|
| FORECASTED FCFE AND DIVIDENDS         |   nan        |   nan     |   nan     |   nan     |   nan     |
| Debt Ratio used in forecasting FCFE = |     0.115793 |   nan     |   nan     |   nan     |   nan     |
| Forecasted FCFE                       |   nan        |   nan     |   nan     |   nan     |   nan     |
| nan                                   |     1        |     2     |     3     |     4     |     5     |
| Net Income                            |  6442.8      |  6764.94  |  7103.19  |  7458.35  |  7831.26  |
| - (Cap Ex - Deprec'n) (1 - DR)        |   560.764    |   588.802 |   618.242 |   649.155 |   681.612 |
| -  Change in Working Capital (1 - DR) |   112.148    |   117.755 |   123.643 |   129.825 |   136.316 |
| FCFE                                  |  5769.89     |  6058.38  |  6361.3   |  6679.37  |  7013.34  |
| Expected Dividends                    |  1390.2      |  1459.71  |  1532.7   |  1609.33  |  1689.8   |
| Cash available for stock buybacks     |  4379.69     |  4598.67  |  4828.61  |  5070.04  |  5323.54  |
| Revenues                              | 44391.9      | 46611.5   | 48942.1   | 51389.2   | 53958.6   |
| Non-cash WC                           |   126.834    |   133.176 |   139.834 |   146.826 |   154.168 |

## Historical Stock and T.Bills
| 0    | 1                     | 2                      | 3                      |
|:-----|:----------------------|:-----------------------|:-----------------------|
| Year | S&P 500               | 3-month T.Bill         | 10-year T. Bond        |
| 1928 | 0.43811155152887893   | 0.0308                 | 0.008354708589799302   |
| 1929 | -0.0829794661190966   | 0.0316                 | 0.04203804156320426    |
| 1930 | -0.25123636363636365  | 0.0455                 | 0.045409314348970366   |
| 1931 | -0.4383754889178619   | 0.0231                 | -0.02558855961942253   |
| 1932 | -0.08642364532019696  | 0.0107                 | 0.08790306990477326    |
| 1933 | 0.49982225433526023   | 0.0096                 | 0.01855272089185736    |
| 1934 | -0.011885656970912803 | 0.003225               | 0.0796344261796561     |
| 1935 | 0.4674042105263158    | 0.0017499999999999998  | 0.04472047729656613    |
| 1936 | 0.3194341027550261    | 0.0017000000000000001  | 0.0501787540454506     |
| 1937 | -0.3533672875436554   | 0.0030250000000000003  | 0.01379146059646038    |
| 1938 | 0.29282654028436017   | 0.000775               | 0.04213248532204607    |
| 1939 | -0.010975646879756443 | 0.00037500000000000006 | 0.04412261394206067    |
| 1940 | -0.10672873194221515  | 0.00025                | 0.05402481596284551    |
| 1941 | -0.1277145557655955   | 0.0008249999999999999  | -0.020221975848580105  |
| 1942 | 0.19173762945914843   | 0.0033750000000000004  | 0.022948682374484164   |
| 1943 | 0.25061310133060394   | 0.0038                 | 0.0249                 |
| 1944 | 0.1903067694944301    | 0.0038                 | 0.025776111579070303   |
| 1945 | 0.358210843373494     | 0.0038                 | 0.03804417341923723    |
| 1946 | -0.08429147465437781  | 0.0038                 | 0.031283745375695685   |
| 1947 | 0.052                 | 0.005675               | 0.009196968062832236   |
| 1948 | 0.057045751633986834  | 0.010225               | 0.019510369413175046   |
| 1949 | 0.18303223684210526   | 0.011025               | 0.04663485182797314    |
| 1950 | 0.30805539011316263   | 0.011725               | 0.00429595741710961    |
| 1951 | 0.2367846304454234    | 0.014775               | -0.0029531392208319886 |
| 1952 | 0.18150988641144306   | 0.016725               | 0.022679961918305656   |
| 1953 | -0.012082047421904465 | 0.018925               | 0.04143840258908851    |
| 1954 | 0.525633212414349     | 0.009625               | 0.032898034558095555   |
| 1955 | 0.3259733185102835    | 0.0166                 | -0.013364391288618781  |
| 1956 | 0.07439511873350935   | 0.025550000000000003   | -0.022557738173154165  |
| 1957 | -0.1045736018855796   | 0.0323                 | 0.0679701284662499     |
| 1958 | 0.43719954988747184   | 0.017775               | -0.020990181755274694  |
| 1959 | 0.12056457163557326   | 0.032549999999999996   | -0.026466312591385065  |
| 1960 | 0.00336535314743695   | 0.030449999999999998   | 0.11639503690963365    |
| 1961 | 0.2663771295818275    | 0.022675               | 0.020609208076323167   |
| 1962 | -0.08811460517120888  | 0.027775000000000005   | 0.05693544054008462    |
| 1963 | 0.22611927099841514   | 0.031100000000000003   | 0.016841620739546127   |
| 1964 | 0.16415455878432425   | 0.03505                | 0.037280648911540815   |
| 1965 | 0.12399242477876114   | 0.039025               | 0.007188550935926234   |
| 1966 | -0.0997095423563779   | 0.0484                 | 0.029079409324299622   |
| 1967 | 0.23802966513133328   | 0.043324999999999995   | -0.015806209932824666  |
| 1968 | 0.10814862651601535   | 0.0526                 | 0.032746196950768365   |
| 1969 | -0.08241371076449064  | 0.065625               | -0.050140493209926106  |
| 1970 | 0.03561144905496419   | 0.06684999999999999    | 0.16754737183412338    |
| 1971 | 0.14221150298426474   | 0.0454                 | 0.09786896619712297    |
| 1972 | 0.18755362915074925   | 0.039525000000000005   | 0.02818449050444969    |
| 1973 | -0.14308047437526472  | 0.06724999999999999    | 0.036586646024150085   |
| 1974 | -0.2590178575089697   | 0.07777500000000001    | 0.019886086932378574   |
| 1975 | 0.36995137106184356   | 0.0599                 | 0.03605253602603384    |
| 1976 | 0.23830999002106662   | 0.04970000000000001    | 0.1598456074290921     |
| 1977 | -0.06979704075935232  | 0.051275               | 0.012899606071070449   |
| 1978 | 0.0650928391167193    | 0.06932500000000001    | -0.007775806907508648  |
| 1979 | 0.18519490167516386   | 0.099375               | 0.006707203124723546   |
| 1980 | 0.3173524550676301    | 0.1122                 | -0.02989744251999403   |
| 1981 | -0.04702390247495576  | 0.143                  | 0.08199215335892354    |
| 1982 | 0.20419055079559353   | 0.1101                 | 0.32814549486295586    |
| 1983 | 0.22337155858930619   | 0.084475               | 0.032002094451429264   |
| 1984 | 0.0614614199963621    | 0.096125               | 0.13733364344102345    |
| 1985 | 0.3123514948576895    | 0.074875               | 0.2571248821260641     |
| 1986 | 0.18494578758046187   | 0.06035                | 0.24284215141767618    |
| 1987 | 0.05812721641821871   | 0.057225               | -0.04960508937926228   |
| 1988 | 0.16537192812044688   | 0.06449999999999999    | 0.08223595843484167    |
| 1989 | 0.31475183638196724   | 0.08109999999999999    | 0.17693647159446219    |
| 1990 | -0.03064451612903212  | 0.07550000000000001    | 0.06235375333553336    |
| 1991 | 0.3023484313487976    | 0.05610000000000001    | 0.15004510019517303    |
| 1992 | 0.07493727972380064   | 0.03405                | 0.09361637316207942    |
| 1993 | 0.0996705147919488    | 0.029825               | 0.14210957589263107    |
| 1994 | 0.013259206774573897  | 0.039850000000000003   | -0.08036655550998592   |
| 1995 | 0.3719519890260631    | 0.055150000000000005   | 0.23480780112538907    |
| 1996 | 0.2268096601886579    | 0.050225               | 0.01428607793401844    |
| 1997 | 0.33103653103653097   | 0.050525               | 0.09939130272977531    |
| 1998 | 0.28337953278443584   | 0.047275               | 0.14921431922606215    |
| 1999 | 0.20885350992084475   | 0.0451                 | -0.08254214796268576   |
| 2000 | -0.09031818955249278  | 0.057625               | 0.16655267125397488    |
| 2001 | -0.11849759142000185  | 0.036725               | 0.055721811892492555   |
| 2002 | -0.219660479579127    | 0.016575               | 0.15116400378109285    |
| 2003 | 0.2835580005001023    | 0.0103                 | 0.003753185881775853   |
| 2004 | 0.10742775944096193   | 0.012275000000000001   | 0.04490683702274547    |
| 2005 | 0.048344775232688535  | 0.0301                 | 0.028675329597779506   |
| 2006 | 0.15612557979315703   | 0.046775000000000004   | 0.019610012417568386   |
| 2007 | 0.054847352464217694  | 0.046425               | 0.10209921930012807    |
| 2008 | -0.3655234411179819   | 0.01585                | 0.20101279926977011    |
| 2009 | 0.2593523387766398    | 0.00135                | -0.11116695313259162   |
| 2010 | 0.14821092278719414   | 0.0013                 | 0.08462933880355772    |
| 2011 | 0.0209837473362805    | 0.0003                 | 0.16035334999461354    |
| 2012 | 0.15890585241730293   | 0.0005                 | 0.02971571978018946    |
| 2013 | 0.32145085858125483   | 0.00066                | -0.09104568794347262   |
| 2014 | 0.13524421649462237   | 0.00053                | 0.10746180452004755    |
| 2015 | 0.01359949487590461   | 0.0021                 | 0.012842996709792224   |

## Disney 2010-12 nos
| 0                            |     1 |     2 |     3 |
|:-----------------------------|------:|------:|------:|
| nan                          |  2012 |  2011 |  2010 |
| Receivables                  |  -108 |  -518 |  -686 |
| Inventories                  |    18 |  -199 |  -127 |
| Other assets                 |  -151 |  -189 |    42 |
| Accounts payable             |  -608 |  -367 |   649 |
| Income taxes                 |  -242 |   134 |  -144 |
| Chg in WC (Cash flow effect) | -1091 | -1139 |  -266 |
| Commercial Paper             |   467 |   393 |  1190 |
| Borrowings                   |  3779 |  2350 |     0 |
| Reductions of borrowings     | -3822 | -1096 | -1371 |
| Net Debt (Cash flow effect)  |   424 |  1647 |  -181 |

## Annual return worksheet
|    0 | 1           | 2         | 3                    |
|-----:|:------------|:----------|:---------------------|
|  nan | Stock price | Dividends | Returns              |
| 2009 | 32.75       | nan       | nan                  |
| 2010 | 27.21       | 0.4       | -0.15694656488549616 |
| 2011 | 33.34       | 0.6       | 0.24733553840499822  |
| 2012 | 30.16       | 0.75      | -0.07288542291541701 |

## Sheet1
| 0   |
|:----|
| Yes |
| No  |
