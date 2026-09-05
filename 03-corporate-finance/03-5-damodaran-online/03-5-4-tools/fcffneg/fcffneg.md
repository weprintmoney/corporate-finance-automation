---
title: "Fcffneg"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/fcffneg.xls
---

# Fcffneg

Source: https://pages.stern.nyu.edu/~adamodar/pc/fcffneg.xls

Sheets: Valuation, Summary, Option Valuation

## Valuation

| A General FCFF Valuation Model |
|---|
| An n-stage Model |
| This model is designed to value a firm, with changing margins, revenue growth, |
| and other parameters. |
|  |
| Assumptions |
| 1. The firm is expected to grow at a higher growth rate in the first period. |
| 2. The growth rate will drop at the end of the first period to the stable growth rate. |
| 3. The free cashflow to equity is the correct measure of expected cashflows to stockholders. |
|  |
| The user has to define the following inputs: |
| 1. Length of high growth period |
| 2. Expected growth rate in earnings during the high growth period. |
| 3. Capital Spending, Depreciation and Working Capital needs during the high growth period. |
| 4. Expected growth rate in earnings during the stable growth period. |
| 5. Inputs for the cost of capital. (Cost of equity, Cost of debt, Weights on debt and equity) |
|  |
|  |
|  |
| Inputs to the model |
| Current EBIT = |
| Current Net Income = |
| Current Dividends = |
| Current Interest Expense = |
| Current Capital Spending |
| Current Depreciation = |
| Tax Rate on Income = |
| Current Revenues = |
| Current Working Capital = |
| Chg. Working Capital = |
| Cash and Non-operating assets = |
| Book Value of Debt = |
| Book Value of Equity = |
| NOL carried forward = |
|  |
| Weights on Debt and Equity |
| Is the firm publicly traded ? |
|  |
| If yes, enter the market price per share = |
|       & Number of shares outstanding  = |
|       & Market Value of Debt = |
|  |
| If no, do you want to use the book value debt ratio ? |
| If no, enter the debt to capital ratio to be used = |
|  |
| Enter length of extraordinary growth period = |
|  |
| Costs of Components |
| Do you want to enter cost of equity directly? |
| If yes, enter the cost of equity = |
| If no, enter the inputs to the cost of equity |
| Beta of the stock = |
| Riskfree rate= |
| Risk Premium= |
|  |
| Enter the cost of debt for cost of capital calculation |
|  |
| Earnings Inputs |
| Please enter year-specific inputs for each of the following variables: |
| Year |
|  |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 |
| 7 |
| 8 |
| 9 |
| 10 |
| Compounded Avg |
| Enter growth rate in stable growth period |
| Enter EBITDA as % of Revenue in stable phase |
| Enter Working Capital as % of Revenue in stable phase |
|  |
| Will the beta change in the stable period? |
| If yes, enter the beta for stable period = |
|  |
| Do you want to change the debt ratio in the stable growth period? |
| If yes, enter the debt ratio for the stable growth period = |
|  |
| Will the cost of debt change in the stable period? |
| If yes, enter the new cost of debt  = |
|  |
| Capital Spending and Depreciation in Stable growth period |
| Do you want to compute the reinvestment rate in stable growth from fundamentals? |
| If yes, enter the return on capital in stable growth = |
| If no, enter capital expenditures as % of depreciation in steady state: |
|  |
| Output from the program |
| Cost of Equity = |
| Equity/(Debt+Equity ) = |
| After-tax Cost of debt = |
| Debt/(Debt +Equity) = |
| Cost of Capital = |
|  |
|  |
| Revenues |
|  - Operating Expenses |
| EBITDA |
|  - Depreciation |
| EBIT |
|  - EBIT*t |
| EBIT (1-t) |
|  + Depreciation |
|  - Capital Spending |
|  -  Chg. Working Capital |
| Free CF to Firm |
| Present Value |
| NOL |
| Index |
|  |
| Cost of Capital Computation |
| Tax Rate |
| Beta |
| Cost of Equity |
| Cost of Debt |
| Debt Ratio |
| Cost of Capital |
| Cum. WACC |
|  |
| Growth Rate in Stable Phase = |
| FCFF in Stable Phase = |
| Cost of Equity in Stable Phase = |
| Equity/ (Equity + Debt) = |
| AT Cost of Debt in Stable Phase = |
| Debt/ (Equity + Debt)  = |
| Cost of Capital in Stable Phase = |
| Value at the end of growth phase = |
|  |
| Present Value of FCFF in high growth phase = |
| Present Value of Terminal Value of Firm = |
| Value of the firm = |
|  + Cash and Marketable Securities = |
| Market Value of Debt = |
| Market Value of Equity = |
| Value of Options Outstanding (See option worksheet) = |
| Value of Equity in Common Stock = |
| Value of Equity per Share = |

## Summary

| Year | Revenues | EBITDA | Depreciation | EBIT | NOL at beginning of year | Taxes | EBIT (1-t) | Capital Expenditures | Depreciation | Change in working capital | FCFF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3789 | 0 | 1519.1000000000001 | -1519.1000000000001 | 2075 | 0 | -1519.1000000000001 | 3431.2000000000003 | 1519.1000000000001 | 0 | -3431.2000000000003 |
| 2 | 4925.7 | 369.4274999999998 | 1671.0100000000002 | -1301.5825000000004 | 3594.1000000000004 | 0 | -1301.5825000000004 | 1715.6000000000001 | 1671.0100000000002 | 34.10099999999999 | -1380.2735000000002 |
| 3 | 6157.125 | 923.5687500000004 | 1838.1110000000003 | -914.54225 | 4895.682500000001 | 0 | -914.54225 | 857.8000000000001 | 1838.1110000000003 | 36.942750000000004 | 28.826000000000292 |
| 4 | 7388.549999999999 | 1662.42375 | 2021.9221000000005 | -359.4983500000005 | 5810.224750000001 | 0 | -359.4983500000005 | 428.90000000000003 | 2021.9221000000005 | 36.942749999999975 | 1196.581 |
| 5 | 8127.405 | 2438.2215000000006 | 1010.9610500000002 | 1427.2604500000002 | 6169.723100000002 | 0 | 1427.2604500000002 | 450.345 | 1010.9610500000002 | 22.165650000000014 | 1965.7108500000006 |
| 6 | 8940.1455 | 2735.684523000001 | 505.4805250000001 | 2230.203998000001 | 4742.462650000001 | 0 | 2230.203998000001 | 472.8622500000001 | 505.4805250000001 | 24.382215000000024 | 2238.4400580000006 |
| 7 | 9834.160050000002 | 3068.2579356000015 | 530.7545512500002 | 2537.5033843500014 | 2512.2586520000004 | 8.835656322500334 | 2528.667728027501 | 496.5053625000001 | 530.7545512500002 | 26.82043650000005 | 2536.096480277501 |
| 8 | 10620.892854000003 | 3313.7185704480016 | 557.2922788125002 | 2756.4262916355015 | 0 | 964.7492020724254 | 1791.6770895630762 | 521.3306306250001 | 557.2922788125002 | 23.601984120000033 | 1804.0367536305762 |
| 9 | 11258.146425240004 | 3580.090563226322 | 585.1568927531252 | 2994.933670473197 | 0 | 1048.2267846656189 | 1946.706885807578 | 547.3971621562501 | 585.1568927531252 | 19.11760713720001 | 1965.3490092672535 |
| 10 | 11821.053746502004 | 3830.0214138666506 | 614.4147373907815 | 3215.606676475869 | 0 | 1125.462336766554 | 2090.144339709315 | 574.7670202640627 | 614.4147373907815 | 16.887219637860017 | 2112.904837198173 |
| Term. Year | 12412.106433827104 | 4095.9951231629457 | 645.1354742603206 | 3450.859648902625 | 0 | 1207.8008771159186 | 2243.0587717867065 | 1873.5476557442935 | 645.1354742603206 | 17.731580619753004 | 996.9150096829808 |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | 0.4166666666666667 |  |  |  |  |

## Option Valuation

| Valuing Options or Warrants when there is dilution |
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
|  |
| VALUING WARRANTS WHEN THERE IS DILUTION |
| Stock Price= |
| Strike Price= |
| Adjusted S (DO NOT ENTER)= |
| Adjusted K (DO NOT ENTER)= |
| Expiration (in years) = |
|  |
|  |
| d1 =  |
| N (d1) = |
|  |
| d2 =  |
| N (d2) = |
|  |
| Value of the call =  |
| Number of Options = |
| Value of Options = |
