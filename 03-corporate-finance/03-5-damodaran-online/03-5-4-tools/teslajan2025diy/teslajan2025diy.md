---
title: "Teslajan2025Diy"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/blog/TeslaJan2025DIY.xlsx
---

# Teslajan2025Diy

Source: https://pages.stern.nyu.edu/~adamodar/pc/blog/TeslaJan2025DIY.xlsx

Sheets: Master Inputs, Input sheet, Valuation output, Stories to Numbers, Diagnostics, Business Value, Option value, Cost of capital worksheet, Synthetic rating, R& D converter, Operating lease converter, Country equity risk premiums, Industry Average Beta (US), Industry Average Beta (Global), Trailing 12 month, Answer keys

## Master Inputs

| THE YELLOW CELLS ARE YOUR ONLY REQUIRED INPUTS. ALL THE OTHER NUMBERS WILL BE CALCULATED. | Expected Auto Revenues in 2033 (in $ mi)l | $ Revenues in 2033 |
|---|---|---|
| Your inputs | A1: $100 billion (BMW-like) | 100 |
| Growth (Autos) Lever | A2: $150 billion (Ford & Honda-like) | 150 |
| How much will Tesla have in revenues from autos in 2033? | A3: $200 billion (Daimler-like) | 200 |
| Expected auto revenues in 2033 ($ million) | A4: $300 billion (Toyota & VW -like) | 300 |
|  | A5: $500 billion (20% auto market share) | 500 |
| Growth (Software, Robotaxi and Energy) Lever | A6: Direct Input (Enter % growth rate) | 400 |
| How much will Tesla have in revenues from other businesss in 2033? |  |  |
| What percentage of other revenues in 2034 will be from software? |  Expected Other Revenues in 2033 (in $ bil) | $ Billion Revenues in 2033 |
| What percentage of other revenues in 2034 will be from robotaxis? | AA1: Energy only ($50) | 50 |
| Revenues from other businesses in 2033 (based on inputs) = | AA2: Energy + Software ($100) | 100 |
| Revenues from energy in 2033 (based on your inputs) | AA3: Energy +  Big Software ($150) | 150 |
| Revenues from software in 2033 (based on your inputs) | AA4: Energy + Software + Robotaxi ($200) | 200 |
| Revenues from robotaxis in 2033 (based on your inputs) | AA5: Energy + Software + Big Robotaxi ($300) | 300 |
| How many years before robotaxi revenues begin? | AA6: Direct Input (Enter revenues in 2033) | 120 |
| Profitability Lever |  |  |
| What operating margin will Tesla Auto have in 2033 (and beyond)? | Operating Margin in 2028  | Target Operating Margin |
| Operating margin in 2028 | B1: Auto Industry First Quartile | -0.1281 |
| What operating margin with Tesla Energy have in 2033 (and beyond)? | B2: Auto Industry Median | 0.0325 |
| What operating margin with Tesla Software have in 2033 (and beyond)? | B3: Auto Industry Third Quartile | 0.0852 |
| What operating margin with Tesla Robotaxi have in 2033 (and beyond)? | B4: Technology Median | 0.1025 |
| With your operating margin, Tesla's operating profits in 2033 ($ million) | B5: Software | 0.2124 |
|  | B6: FAANG Aggregate | 0.1987 |
| Investment Efficiency Lever | B7: Direct Input | 0.1 |
| How many dollars of revenues will Tesla generate per $ of investment? |  |  |
| Sales to Invested Capital used in valuation | Sales to Invested Capital | Sales to Capital (1st 5 years) |
| With your investment input, Tesla's return on capital in 2033 | C1: Auto Industry First Quartile | 0.75 |
|  | C2: Auto Industry Median | 1.37 |
| Risk Levers | C3: Auto Industry Third Quartile | 2.42 |
| What cost of capital do you want to give Tesla initially? | C4: Technology Median | 1.51 |
| If direct input, enter the cost of capital | C5: Software | 2.3 |
| What is the probability of failure | C6: FAANG Aggregate | 1.27 |
|  | C7: Direct Input | 3 |
| Your key inputs wrere |  |  |
| Expected Revenue Growth rate for next 5 years = | Cost of Capital | Initial cost of capital |
| Expected Pre-tax Operating Margin in year 5 = | D1: Automobile Median | 0.0975 |
| Sales to Invested Capital for first 5 years = | D2: Technology Median | 0.1011 |
| Cost of capital to start = | D3: All companies - First Quartile | 0.0687 |
|  | D4: All companies - Median | 0.0835 |
| And with these inptus, your value is | D5: All companies - Third Quartile | 0.0931 |
| Tesla's value of equity today = | D6: Direct Input | 0.0937 |
| Tesla's value per share today = |  |  |
|  | Failure Likelihood | Probability of failure |
|  | E1: No chance | 0 |
|  | E2: 10% (Marginal profitability, High Debt) | 0.1 |
|  | E3: 20% (Money loser, High Debt) | 0.2 |
|  | E4: 50% (Low Growth, Money loser, High Debt) | 0.5 |

## Input sheet

| Date of valuation | 2025-03-14 00:00:00 | Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |
|---|---|---|
| Company name | Tesla | There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |
| Numbers from your base year below ( in consistent units) |  |  |
|  | This year | Last year |
| Country of incorporation | United States |  |
| Industry (US) | Auto & Truck |  |
| Industry (Global) | Auto & Truck | Last 10K |
| Revenues (Auto) | 77070 | 82419 |
| Revenues (Energy) | 10086 | 6035 |
| Revenues (Rest) | 10534 | 8019 |
| Operating income or EBIT | 7076 | 8891 |
| Interest expense | 350 | 156 |
| Book value of equity | 72913 | 62634 |
| Book value of debt | 13623 | 9573 |
| Do you have R&D expenses to capitalize? | Yes |  If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |
| Do you have operating lease commitments? | No | If you have operating leases, please enter your lease commitments in the lease worksheet below and I will convert to debt. If it is already considered debt by accountants, enter no. |
| Cash and Marketable Securities | 36563 | 29004 |
| Cross holdings and other non-operating assets | 0 | 0 |
| Minority interests | 767 | 975 |
| Number of shares outstanding = | 3197 |  |
| Current stock price = | 220 |  |
| Effective tax rate = | 0.204 |  |
| Marginal tax rate = | 0.25 |  |
| The value drivers below: |  |  |
| Revenues (Auto) in 2033 = | 300000 | Growth Lever |
| Revenues (Energy) in 2033 = | 80000 |  |
| Revenues (Software) in 2033 = | 40000 |  |
| Revenues (Robotaxi and Rest) in 2033 = | 80000 |  |
| Target operating margin (autos) = | 0.1 | Profitability Lever |
| Target operating margin (energy) = | 0.16 |  |
| Target operating margin (software) = | 0.2181 |  |
| Target operating margin (robotaxi) = | 0.25 |  |
| Year of convergence | 5 | Speed of convergence level |
|  | Years 1-5 | Years 6-10 |
| Sales to capital ratio  (for computing reinvestment) = | 3 | 2 |
| Market numbers  |  |  |
| Riskfree rate | 0.0422 |  |
| Initial cost of capital = | 0.0937 |  |
| Other inputs |  |  |
| Do you have employee options outstanding? | Yes |  |
| Number of options outstanding = | 344.5 |  |
| Average strike price = | 40.41 |  |
| Average maturity = | 4 |  |
| Standard deviation on stock price = | 0.3 |  |
| Default assumptions.  |  |  |
| In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%) |  |  |
| Do you want to override this assumption = | Yes | Mature companies generally see their risk levels approach the average |
| If yes, enter the cost of capital after year 10 = | 0.0835 | Though some sectors, even in stable growth, may have higher risk. |
| I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time. |  |  |
| Do you want to override this assumption = | Yes | Mature companies find it difficult to generate returns that exceed the cost of capital |
| If yes, enter the return on capital you expect after year 10 | 0.15 | But there are significant exceptions among companies with long-lasting competitive advantages. |
| I will assume that your firm has no chance of failure over the foreseeable future. |  |  |
| Do you want to override this assumption = | Yes | Many young, growth companies fail, especially if they have trouble raising cash. Many distressed companies fail, because they have trouble making debt payments. |
| If yes, enter the probability of failure = | 0 | Tough to estimate but a key input. |
| What do you want to tie your proceeds in failure to? | V | B: Book value of capital, V= Estimated fair value for the company |
| Enter the distress proceeds as percentage of book or fair value | 0.5 | This can be zero, if the assets will be worth nothing if the firm fails. |
| I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year. If you override this assumption, I will leave the tax rate at your effective tax rate. |  |  |
| Do you want to override this assumption = | No |  |
| I will assume that you have no losses carried forward from prior years ( NOL) coming into the valuation. If you have a money losing company, you may want to override tis. |  |  |
| Do you want to override this assumption = | No | Check the financial statements. |
| If yes, enter the NOL that you are carrying over into year 1 | 250 | An NOL will shield your income from taxes, even after you start making money. |
| I will assume that the growth rate in perpetuity will be equal to the risk free rate. This allows for both valuation consistency and prevents "impossible" growth rates. |  |  |
| Do you want to override this assumption = | No |  |
| If yes, enter the growth rate in perpetuity | 0.01 | This can be negative, if you feel the company will decline (and disappear) after growth is done. If you let it exceed the risk free rate, you are on your own in uncharted territory. |
| I have assumed that none of the cash is trapped (in foreign countries) and that there is no additional tax liability coming due and that cash is a neutral asset. |  |  |
| Do you want to override this assumption | No |  |
| If yes, enter trapped cash (if taxes) or entire balance (if mistrust) | 140000 | Cash that is trapped in foreign markets (and subject to additoinal tax) or cash that is being discounted by the market (because of management mistrust) |
| & Average tax rate of the foreign markets where the cash is trapped | 0.15 | Additional tax rate due on trapped cash or discount being applied to cash balance because of mistrust. |

## Valuation output

| Base year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Terminal year |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.28925652004671076 | 0.22435916789952004 | 0.18324620240678624 | 0.15486734885271858 | 0.13409968599992772 | 0.11824329700055691 | 0.10574022425863738 | 0.09562845046134849 | 0.08728182480208613 | 0.08027525413475356 | 0.0422 |
| 77070 | 99363 | 121656 | 143949 | 166242 | 188535 | 210828 | 233121 | 255414 | 277707 | 300000 | 312660 |
| 10086 | 17077.4 | 22670.52 | 27145.016 | 30724.6128 | 45043 | 52034.4 | 59025.8 | 66017.2 | 73008.6 | 80000 | 83376 |
| 10534 | 12498.4 | 14069.92 | 15327.136 | 16332.908800000001 | 20356 | 24284.8 | 28213.6 | 32142.399999999998 | 36071.2 | 40000 | 41688 |
| 0 | 0 | 0 | 0 | 11428.57142857143 | 22857.142857142855 | 34285.71428571428 | 45714.28571428571 | 57142.85714285714 | 68571.42857142857 | 80000 | 83376 |
| 97690 | 128938.79999999999 | 158396.44 | 186421.152 | 224728.09302857143 | 276791.14285714284 | 321432.9142857143 | 366074.6857142857 | 410716.4571428572 | 455358.22857142857 | 500000 | 521100 |
| 0.11823537044245491 | 0.11458829635396393 | 0.11094122226547296 | 0.10729414817698196 | 0.10364707408849098 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |
| 0.12 | 0.128 | 0.136 | 0.144 | 0.152 | 0.16 | 0.16 | 0.16 | 0.16 | 0.16 | 0.16 | 0.16 |
| 0.1 | 0.12362000000000001 | 0.14724 | 0.17086 | 0.19448 | 0.2181 | 0.2181 | 0.2181 | 0.2181 | 0.2181 | 0.2181 | 0.2181 |
| 0 | 0.04999999999999999 | 0.09999999999999998 | 0.15 | 0.2 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 |
| 9112.4 | 15116.79629861892 | 18651.511076728377 | 21972.562096888378 | 27362.776425357202 | 36214.30931428571 | 43276.24745142858 | 50338.18558857143 | 57400.123725714286 | 64462.06186285714 | 71524 | 74542.3128 |
| 0.204 | 0.204 | 0.204 | 0.204 | 0.204 | 0.204 | 0.2132 | 0.22240000000000001 | 0.23160000000000003 | 0.24080000000000004 | 0.25000000000000006 | 0.25 |
| 7253.4704 | 12032.96985370066 | 14846.602817075789 | 17490.15942912315 | 21780.770034584333 | 28826.590214171425 | 34049.75149478401 | 39142.97311367314 | 44106.25507083886 | 48939.59736628114 | 53643 | 55906.734599999996 |
|  | 10416.266666666663 | 9819.213333333339 | 9341.570666666667 | 12768.980342857141 | 17354.349942857138 | 22320.885714285716 | 22320.885714285716 | 22320.885714285745 | 22320.885714285687 | 22320.885714285716 | 15728.428000800002 |
|  | 1616.703187033998 | 5027.3894837424505 | 8148.588762456482 | 9011.789691727192 | 11472.240271314287 | 11728.865780498294 | 16822.087399387427 | 21785.369356553114 | 26618.71165199545 | 31322.114285714284 | 40178.30659919999 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0.0937 | 0.0937 | 0.0937 | 0.0937 | 0.0937 | 0.09166 | 0.08962 | 0.08758 | 0.08554 | 0.0835 | 0.0835 |
|  | 0.9143275121148394 | 0.8359947994101118 | 0.7643730450855918 | 0.6988873046407531 | 0.6390118905008256 | 0.5853579782174171 | 0.5372129533391614 | 0.49395258586877416 | 0.4550293732785288 | 0.41996250417953745 |  |
|  | 1478.1962028289272 | 4202.871463017776 | 6228.561605509095 | 6298.225407640541 | 7330.897944052247 | 6865.585160055929 | 9037.043253154412 | 10760.939527775763 | 12112.295680489362 | 13154.113551626235 | 57027` |
| 40178.30659919999 |  |  |  |  |  |  |  |  |  |  |  |
| 0.0835 |  |  |  |  |  |  |  |  |  |  |  |
| 972840.353491525 |  |  |  |  |  |  |  |  |  |  |  |
| 408556.47101920727 |  |  |  |  |  |  |  |  |  |  |  |
| 77468.72979615028 |  |  |  |  |  |  |  |  |  |  |  |
| 486025.20081535756 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 243012.60040767878 |  |  |  |  |  |  |  |  |  |  |  |
| 486025.20081535756 |  |  |  |  |  |  |  |  |  |  |  |
| 13623 |  |  |  |  |  |  |  |  |  |  |  |
| 767 |  |  |  |  |  |  |  |  |  |  |  |
| 36563 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 508198.20081535756 |  |  |  |  |  |  |  |  |  |  |  |
| 37714.78120766026 |  |  |  |  |  |  |  |  |  |  |  |
| 470483.4196076973 |  |  |  |  |  |  |  |  |  |  |  |
| 3197 |  |  |  |  |  |  |  |  |  |  |  |
| 147.16403491013367 |  |  |  |  |  |  |  |  |  |  |  |
| 220 |  |  |  |  |  |  |  |  |  |  |  |
| 1.4949304708473365 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 |  |
| 60868.600000000006 | 71284.86666666667 | 81104.08 | 90445.65066666667 | 103214.63100952382 | 120568.98095238095 | 142889.86666666667 | 165210.75238095238 | 187531.63809523813 | 209852.52380952382 | 232173.40952380953 |  |
| 0.11916604620444694 | 0.16880118342603798 | 0.18305617691583195 | 0.1933775621072409 | 0.21102405561644239 | 0.23908794771647415 | 0.23829367532559348 | 0.23692751560997097 | 0.23519367461846333 | 0.2332094771979106 | 0.2310471302894782 | 0.15 |

## Stories to Numbers

| Tesla |
|---|
| An Auto Tale, with Add-on Stories |
| The news in 2024 for Tesla, ranging from price cuts on many of its lowest-priced models, in conjunction with the  Cybertruck introduction, suggests that Tesla will continue to grow in its core auto business, maintaining a dominant market share of the electric car component. In conjunection, a rise in revenues and operating profits from the energy businesss, coming from a shift to energy storage soltuions will expand the profitability of that business, and Tesla's committment to FSD will translate into software revenues (from sale as an add-on) and provide an impetus to a robotaxi business.   |
| The Assumptions |
|  |
| Revenues (a) |
| Operating margin (b) |
| Tax rate |
| Reinvestment (c ) |
| Return on capital |
| Cost of capital (d) |
| The Cash Flows |
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
| Terminal year |
| The Value |
| Terminal value |
| PV(Terminal value) |
| PV (CF over next 10 years) |
| Value of operating assets = |
| Adjustment for distress |
|  - Debt & Minority Interests |
|  + Cash & Other Non-operating assets |
| Value of equity |
|  - Value of equity options |
| Number of shares |
| Value per share |

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

## Business Value

| Tesla Business | Value |
|---|---|
| Auto  | 351402 |
| Energy | 81965 |
| Software | 54474 |
| Robotaxi | 121679 |

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
| Do not input any numbers below this line |
| VALUING WARRANTS WHEN THERE IS DILUTION |
| Stock Price= |
| Strike Price= |
| Adjusted S = |
| Adjusted K = |
| Expiration (in years) = |
|  |
| d1 =  |
| N (d1) = |
| d2 =  |
| N (d2) = |
| Value per option =  |
| Value of all options outstanding = |

## Cost of capital worksheet

| You can use this spreadsheet to compute your cost of capital. You can either use the built-in data to compute key inputs (beta, equity risk premium, default spread) or enter them directly. If you choose to use the built in ERP data, you can update the ERP numbers to reflect a more current mature market premuum (since the spreadsheet uses the start of the year numbers). |
|---|
| Estimation of Current Cost of Capital |
| Inputs |
| Equity |
| Number of Shares outstanding = |
| Current Market Price per share = |
|  |
| Approach for estimating beta |
| If direct input, enter levered beta (or regression beta) |
| Unlevered beta = |
| Riskfree Rate = |
| What approach do you want to use to input ERP? |
| Direct input for ERP (if you choose "will input" |
| Equity Risk Premium used in cost of equity = |
|  |
| Debt |
| Book Value of Straight Debt = |
| Interest Expense on Debt = |
| Average Maturity = |
| Approach for estimating pre-tax cost of debt |
| If direct input, input the pre-tax cost of debt |
| If actual rating, input the rating |
| If synethetic rating, input the type of company |
| Pre-tax Cost of Debt = |
| Tax Rate = |
|  |
| Book Value of Convertible Debt = |
| Interest Expense on Convertible = |
| Maturity of Convertible Bond = |
| Market Value of Convertible = |
|  |
| Debt value of operating leases = |
|  |
| Preferred Stock |
| Number of Preferred Shares = |
| Current Market Price per Share= |
| Annual Dividend per Share = |
|  |
| Output |
| Estimating Market Value of Straight Debt = |
| Estimated Value of Straight Debt in Convertible = |
| Value of Debt in Operating leases = |
| Estimated Value of Equity in Convertible = |
| Levered Beta for equity = |
|  |
|  |
| Market Value |
| Weight in Cost of Capital |
| Cost of Component |
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

## R& D converter

| R & D Converter |
|---|
| This spreadsheet converts R&D expenses from operating to capital expenses. It makes the appropriate adjustments to operating income, net |
| income, the book value of assets and the book value of equity. |
| Inputs |
| Over how many years do you want to amortize R&D expenses |
| Enter the current year's R&D expense = |
| Enter R& D expenses for past years: the number of years that you will need to enter will be determined by the amortization period |
| Do not input numbers in the first column (Year). It will get automatically updated  based on the input above. |
| Year |
| -1 |
| -2 |
| -3 |
| -4 |
| -5 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| Output |
| Year |
| Current |
| -1 |
| -2 |
| -3 |
| -4 |
| -5 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| Value of Research Asset = |
| Amortization of asset for current year = |
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
| Output |
| Pre-tax Cost of Debt = |
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
| Restated Financials |
| Depreciation on Operating Lease Asset = |
| Adjustment to Operating Earnings = |
| Adjustment to Total Debt outstanding = |
| Adjustment to Depreciation = |

## Country equity risk premiums

_3295 rows — showing first 20. Full data: [`teslajan2025diy-country-equity-risk-premiums.csv`](teslajan2025diy-country-equity-risk-premiums.csv)_

| Mature Market ERP + | 0.0433 | Updated January 1, 2025 |
|---|---|---|
| Changing this number will update all your country equity risk premiums. |  |  |
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.0049 |
| Albania | Ba3 | 0.0356 |
| Algeria | NR | 0.0298 |
| Andorra (Principality of) | Baa1 | 0.0158 |
| Angola | B3 | 0.0644 |
| Anguilla | NR | 0.0601 |
| Antigua & Barbuda | NR | 0.0601 |
| Argentina | Ca | 0.1188 |
| Armenia | Ba3 | 0.0356 |
| Aruba | Baa3 | 0.0218 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.004 |
| Azerbaijan | Ba1 | 0.0248 |
| Bahamas | B1 | 0.0446 |
| Bahrain | B2 | 0.0545 |
| Bangladesh | B2 | 0.0545 |
| Barbados | B3 | 0.0644 |
| Belarus | C | 0.175 |

## Industry Average Beta (US)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 54 | -0.01617666667 | 0.10900602210262404 | 0.34913076808783805 | 0.2927367453879188 | 1.1961570326525681 | 1.337294053 | 0.10370483249489999 | 0.671856667 | 0.0641 | 0.20758669213753542 | 0.09215681958311851 | 4.1947708837323034 | 2.7530320630511635 | 15.557572543531982 | 24.270404651523627 | 6.976657001320543 | 291.270179 | 0.03230773802741799 | 0.018063081232134088 | 0.007034421163821441 | 0.16148108503414008 | 0.11852693534291847 | 0.8336316717637688 | 0.8336316717637688 | 0.11395905036151344 |
| Aerospace/Defense | 67 | 0.08205536585 | 0.07586463137368067 | 0.1402535112217883 | 0.1647887633504989 | 0.800892578975626 | 0.901553128 | 0.0848372504424 | 0.427424009 | 0.0553 | 0.18562455188693347 | 0.07678815213522051 | 2.6209631630366763 | 2.604179873160579 | 17.237956269633543 | 28.387133116704323 | 6.825577021568141 | 87.41777889 | 0.3869621222644865 | 0.027915932425310697 | 0.007667472862174317 | 0.6500860604012224 | 0.11941015141390651 | 0.5150492697875694 | 0.5150492697875694 | 0.07869697574772488 |
| Air Transport | 24 | 0.02636923077 | 0.055360161881576116 | 0.08476398601412484 | 0.22111636379000343 | 0.7648537512324446 | 1.236006738 | 0.09931909175539999 | 0.652716386 | 0.0641 | 0.5165022574610012 | 0.07285140268219722 | 1.7451651543788214 | 1.0222121375517874 | 7.465027434427947 | 17.630170815052836 | 2.941323609021738 | 17.98192415 | 0.010803799258014462 | 0.08793404412682534 | 0.043650452468515705 | 0.9954533910534928 | 0.13271934387774287 | 0.14499243721351626 | 0.1449924372135163 | 0.05504600412176442 |
| Apparel | 37 | 0.0696692 | 0.08726286645130762 | 0.1525620938440485 | 0.184121853974336 | 0.8267021914205971 | 0.990568046 | 0.08869159639179999 | 0.509263882 | 0.057800000000000004 | 0.3145444021629596 | 0.07442965106162706 | 1.7344817552293235 | 1.4137613665587494 | 9.215376221494438 | 14.635935947303855 | 3.1369627319179645 | 28.05498656 | 0.2400939518060416 | 0.02001129176832979 | 0.0013152379983751258 | -0.3375347310393355 | 0.08466628867065874 | 0.628372585232684 | 0.628372585232684 | 0.09619517534929006 |
| Auto & Truck | 34 | 0.1089522222 | 0.03131636370641931 | 0.0315387610798191 | 0.06298071423761896 | 1.4333544858587057 | 1.615412645 | 0.11574736752849998 | 0.775911123 | 0.0641 | 0.1829797055595927 | 0.10336469764361451 | 1.1507770660211856 | 3.4699548342384703 | 37.443235392929616 | 106.52227906952159 | 6.854351643996245 | 27.2827678 | -0.019121501977945734 | 0.06805946406906987 | 0.029960462555513153 | 0.3134181873627815 | 0.09265899347806514 | 0.06926027501209797 | 0.06926027501209797 | 0.033115492706239175 |
| Auto Parts | 33 | 0.06489166667 | 0.05096843215474874 | 0.08659674993338977 | 0.21438279380512118 | 0.9866442740406467 | 1.225123783 | 0.09884785980389998 | 0.526237487 | 0.057800000000000004 | 0.3235618549413413 | 0.08089086934047561 | 2.4258768506874997 | 0.7458643658048555 | 6.527170609141058 | 13.574320807558516 | 1.6454719650255853 | 24.80288893 | 0.1621414135957554 | 0.03370373484438911 | 0.029796679237983886 | 0.9872478385354112 | 0.07086849223503966 | 0.32661617495316425 | 0.3266161749531642 | 0.054112154929540655 |
| Bank (Money Center) | 15 | 0.05995923077 | NA | NA | 0.18536212402520527 | 0.5250203515537631 | 0.875252876 | 0.0836984495308 | 0.304694013 | 0.0553 | 0.6468771820719891 | 0.056385063480957245 | 0 | NA | NA | NA | 1.322044786581685 | 28.04191666 | NA | NA | NA | NA | 0.11516319967991416 | 0.3124766097475993 | 0.3124766097475993 | NA |
| Banks (Regional) | 591 | 0.06543041754 | NA | NA | 0.21077505165572366 | 0.47508892999890606 | 0.519260942 | 0.0682839987886 | 0.299599934 | 0.0508 | 0.37623618749552407 | 0.056927686161007615 | 0 | NA | NA | NA | 1.1291008480787303 | 18.41235377 | NA | NA | NA | NA | 0.0680011952391968 | 0.5548297697973508 | 0.5548297697973508 | NA |
| Beverage (Alcoholic) | 18 | 0.0508625 | 0.22851540835432294 | 0.17863486195942435 | 0.21589979309432705 | 0.506207020622496 | 0.610297863 | 0.07222589746790001 | 0.630763756 | 0.057800000000000004 | 0.23351097343727722 | 0.06548305854129567 | 0.8510742188918321 | 3.300647073395304 | 11.63038120388939 | 14.398388419724839 | 2.696407349039924 | 44.43103428 | 0.16418832033027872 | 0.08652568745816556 | 0.06208213696143839 | 0.357085160613112 | 0.09490713677653632 | 0.5549730749534877 | 0.5549730749534877 | 0.2288389143557621 |
| Beverage (Soft) | 29 | 0.16750833329999998 | 0.20008555306144923 | 0.3060959745263867 | 0.19713421347462087 | 0.5128879692565596 | 0.567766101 | 0.0703842721733 | 0.476702678 | 0.057800000000000004 | 0.16479514715168567 | 0.0659291553123623 | 1.6739557556528541 | 4.00109810652223 | 16.76312416416936 | 19.86672786217797 | 7.483916113465137 | 25.66698037 | -0.10319965162205474 | 0.053396373552860144 | 0.0282972262332606 | 0.26994041473158514 | 0.30605829873016316 | 0.686947036056462 | 0.686947036056462 | 0.20137095743625985 |
| Broadcasting | 22 | 0.018948125 | 0.1251192337482472 | 0.12676646580261572 | 0.2679495890056047 | 0.4776744420077846 | 0.917523633 | 0.08552877330889999 | 0.52595168 | 0.057800000000000004 | 0.599299474915381 | 0.06025105661230134 | 1.135134525031125 | 1.2871011667112966 | 7.205645787792572 | 10.263125382797796 | 1.0157798794125992 | 45.02351959 | 0.10428461190725047 | 0.01890904431602558 | -0.02381183757029204 | 2.0277458422227252 | -0.09123594639568328 | 0.006253124370000001 | 0.006253124370000029 | 0.125125408608095 |
| Brokerage & Investment Banking | 30 | 0.22187095240000002 | NA | NA | 0.2111858517010476 | 0.47017758016751704 | 0.952267405 | 0.0870331786365 | 0.404908912 | 0.0553 | 0.6510651489165336 | 0.05737183627816109 | 0 | NA | NA | NA | 2.107553367614496 | 29.86793199 | NA | NA | NA | NA | 0.1311086874362939 | 0.3715975987050716 | 0.3715975987050716 | NA |
| Building Materials | 39 | 0.04056935484 | 0.13339807849794327 | 0.26836667409798826 | 0.2372114097961747 | 1.2345815852317845 | 1.359882717 | 0.10468292164609999 | 0.347474928 | 0.0553 | 0.159473079563649 | 0.0946029597283786 | 2.65630182786225 | 2.3330552823981074 | 13.144108813471654 | 17.28060940453545 | 4.2673351808781455 | 22.98375797 | 0.17589732311416995 | 0.03381389083562024 | 0.1442683199845523 | 1.3576339984632542 | 0.273585123195433 | 0.16632375734397675 | 0.16632375734397675 | 0.13659535563209246 |
| Business & Consumer Services | 152 | 0.05241806818 | 0.1210671049743861 | 0.2683220667135423 | 0.23839859256142706 | 0.9217421067931305 | 1.00384996 | 0.08926670326799999 | 0.453932055 | 0.057800000000000004 | 0.1436951590921071 | 0.08266869528691966 | 2.6612038226413137 | 2.932909606309558 | 16.754385344425835 | 23.770574543055467 | 5.940615291172687 | 49.9883544 | 0.1446669061418907 | 0.028368193891951846 | -0.0011791142392289103 | 0.04674507635012014 | 0.1826562013235273 | 0.41282664900021215 | 0.41282664900021215 | 0.12434265853816712 |
| Cable TV | 9 | 0.24145 | 0.18459797782132617 | 0.13752245099771512 | 0.24595154201024375 | 0.5042060471678157 | 0.960510745 | 0.08739011525849999 | 0.497327842 | 0.057800000000000004 | 0.5582149393723677 | 0.06280626498952432 | 0.8503767957069994 | 2.274010217387463 | 7.039959537560604 | 12.51512590734801 | 1.5110124996664887 | 10.74120025 | 0.014661260425027692 | 0.1274566885266333 | -0.002186709723143231 | 0.048180050259822575 | 0.15502628901756088 | 0.32245541299708064 | 0.3224554129970807 | 0.18156021868957392 |
| Chemical (Basic) | 31 | 0.08669777778 | 0.06048689379806931 | 0.08711525643483861 | 0.17651351969149562 | 0.8603685518030199 | 1.147686922 | 0.0954948437226 | 0.500216196 | 0.057800000000000004 | 0.36810087599643493 | 0.07630028106961374 | 1.5856091699425192 | 1.0328956410360037 | 7.9670583901425305 | 16.21039583896549 | 1.611224798317052 | 25.8083733 | 0.1560831126647369 | 0.06007795749756813 | 0.03746685791879284 | 0.6939562430612916 | 0.06369809057698893 | 1.2817896941827633 | 1.2817896941827633 | 0.06246565909397009 |
| Chemical (Diversified) | 4 | 0.016685000000000002 | 0.043609560927712385 | 0.05353673633217604 | 0 | 0.5804650334684516 | 0.994138662 | 0.0888462040646 | 0.469704194 | 0.057800000000000004 | 0.5307849949248137 | 0.064697501621073 | 1.3096090731277268 | 0.998346664774641 | 9.273711289711123 | 22.25938726597356 | 1.3756962474757561 | 33.22368421 | 0.19024416102117192 | 0.056483490852626696 | 0.00309597381827909 | 0.2143220982666615 | -0.013011807112258857 | 0.01960526316 | 0.019605263159999997 | 0.043824308778591406 |
| Chemical (Specialty) | 60 | 0.09194422222 | 0.1193494453676533 | 0.11308895503943045 | 0.20545318279218358 | 0.7942145818971595 | 0.921548907 | 0.0857030676731 | 0.481493551 | 0.057800000000000004 | 0.2133695725539178 | 0.0766662117273435 | 1.1344320373825643 | 2.7705093015104674 | 13.305677144877386 | 22.12973118763059 | 2.5680732923090193 | 43.85667873 | 0.2229359556819943 | 0.0881762795123409 | 0.05202727564134819 | 0.5429721462698663 | 0.07775909833844559 | 0.5923187486492923 | 0.5923187486492923 | 0.12123369916544284 |
| Coal & Related Energy | 16 | 0.0065125 | 0.10974053594215227 | 0.131360985972046 | 0.17764284602210806 | 1.2666789941187624 | 1.182062997 | 0.09698332777009999 | 0.537782229 | 0.057800000000000004 | 0.08650014794994586 | 0.0923440369829384 | 1.2410014770236968 | 1.5677608367812537 | 3.8937525141164238 | 7.979844062386776 | 1.652433883756701 | 8.92895397 | 0.10744364100382817 | 0.10056739234110565 | 0.04181843960661484 | 0.784182502395822 | 0.1133530739065558 | 0.06849833048137254 | 0.06849833048137255 | 0.11036162808862766 |
| Computer Services | 63 | 0.09341057143 | 0.06055245267476086 | 0.20511859984992606 | 0.1582832356431084 | 1.091806958703224 | 1.234460621 | 0.0992521448893 | 0.443962787 | 0.0553 | 0.20842271411909233 | 0.08721007553742005 | 4.71399880823382 | 1.384128746459615 | 14.291251634862933 | 21.79417760816968 | 4.548651300213198 | 56.19388981 | 0.13791056200710072 | 0.00991624879658428 | 0.0013792624153242633 | -0.1352497963392787 | 0.1744259991849477 | 0.553130820816213 | 0.553130820816213 | 0.0644742795490481 |
| Computers/Peripherals | 35 | 0.03547884615 | 0.22650656923300075 | 0.414087117520171 | 0.22873507397401782 | 1.118287266469026 | 1.142245646 | 0.09525923647179999 | 0.526219681 | 0.057800000000000004 | 0.045958192552513426 | 0.09287358178677504 | 3.3449300664684207 | 6.67914190608648 | 25.359132422946413 | 29.38954939369914 | 38.95577055053 | 610.1473168 | -0.07992706036776984 | 0.02581604556184513 | 0.003347027496244872 | 0.0217896969435155 | 0.00020232635 | 0.17968917860020636 | 0.1796891786002064 | 0.22950815299948338 |
| Construction Supplies | 46 | 0.03746354839 | 0.15132789353180212 | 0.18411663423273966 | 0.21734420347661088 | 1.152782179050854 | 1.293637225 | 0.1018144918425 | 0.475248388 | 0.057800000000000004 | 0.17739375240336838 | 0.0914432562522028 | 1.5644347993202348 | 2.4608867902074083 | 12.62265816468092 | 16.105371320231963 | 4.38822675872248 | 18.96755165 | 0.18587440808334135 | 0.048192358657233425 | 0.038508067346589604 | 0.4233187994008747 | 0.25625980435240003 | 0.2921633243015753 | 0.2921633243015753 | 0.15206830137916255 |
| Diversified | 21 | 0.1162011111 | 0.3284732876420425 | 0.24653408323908313 | 0.19221263304728198 | 1.0140267770157503 | 1.089996424 | 0.0929968451592 | 0.593496607 | 0.057800000000000004 | 0.13859853317033913 | 0.08611586524359992 | 0.7997477918147733 | 2.9071161346491126 | 7.856925836398023 | 8.807214412052092 | 1.806284985867228 | 13.03290856 | 0.014896509586036182 | 0.04862532897256853 | 0.030015662439102954 | 0.10870945577023988 | 0.20898799911870694 | 0.05033268272864516 | 0.05033268272864522 | 0.3300008853097672 |
| Drugs (Biotechnology) | 535 | 0.23766170890000002 | 0.014221272716606562 | 0.030814784217150146 | 0.19482954958812734 | 1.1689511933236565 | 1.251948113 | 0.1000093532929 | 0.868278117 | 0.0758 | 0.1459806038133114 | 0.09370892483901044 | 0.9333946427404237 | 6.791791099779408 | 15.186565174237344 | NA | 6.017097654153798 | 84.99430249 | 0.136456198402093 | 0.03360787117884962 | 0.24938461994507974 | NA | -0.14115598020476416 | 0.00974627798 | 0.009746277980000051 | 0.07488265801874916 |
| Drugs (Pharmaceutical) | 231 | 0.2478495652 | 0.22807562351451666 | 0.14079869875837178 | 0.1358270853295788 | 0.9833609439300397 | 1.073797133 | 0.0922954158589 | 0.800484536 | 0.0758 | 0.14449996998715745 | 0.08717355433110663 | 1.0148579813307739 | 5.483712102310231 | 15.36886270507868 | 23.36794850415672 | 5.699401006896502 | 20.88293026 | 0.25087194172001104 | 0.053594365491549195 | 0.23936246817779333 | 1.1762436887227607 | 0.104929834787929 | 1.2549442133929405 | 1.2549442133929405 | 0.2559161155722693 |
| Education | 29 | 0.04766 | 0.09240538407657353 | 0.1185554706305268 | 0.25611450384983275 | 0.9221112564153724 | 0.983172276 | 0.0883713595508 | 0.558226871 | 0.057800000000000004 | 0.16279107677962734 | 0.08104228395144251 | 1.859008910079772 | 2.4903031810109364 | 14.254583613223035 | 28.47050309824616 | 3.3561827175807553 | 33.92151127 | 0.07987259272774762 | 0.031075975498548073 | 0.008910306202179034 | 0.3044884889576344 | 0.042221737467676 | 0.7187351830354953 | 0.7187351830354953 | 0.08546563422373665 |
| Electrical Equipment | 101 | 0.1328885417 | 0.07152181433780842 | 0.12226468202114389 | 0.20188534158072283 | 1.201076911463217 | 1.269751059 | 0.10078022085470001 | 0.721156702 | 0.0641 | 0.1292534032164745 | 0.09396789169195413 | 2.087537198763825 | 3.30719628964143 | 19.605829838383833 | 41.43504205344964 | 4.069239753991878 | 55.43392358 | 0.2887273468000888 | 0.050657051700423394 | 0.10742964307899272 | 2.027078835206155 | 0.04777295470096294 | 0.8026848535774878 | 0.8026848535774878 | 0.07643265546002215 |
| Electronics (Consumer & Office) | 11 | -0.06997714286 | -0.05297232032984498 | -0.058115332425485076 | #DIV/0! | 0.9536363844925939 | 0.919635201 | 0.0856202042033 | 0.731989771 | 0.0641 | 0.11745374424986435 | 0.08121037939099668 | 2.7373984741056008 | 0.7246945892586846 | 44.48899046615133 | NA | 2.2193725635789865 | #DIV/0! | 0.1281047274892576 | 0.02072207888239267 | 0.002187211917956069 | NA | -0.30964018341180377 | #DIV/0! | #DIV/0! | -0.04868542581690992 |
| Electronics (General) | 122 | 0.1058519753 | 0.08154981683331164 | 0.13112417823624317 | 0.1922895485416306 | 1.0112705827294393 | 1.058231623 | 0.0916214292759 | 0.616085598 | 0.057800000000000004 | 0.1260319676230025 | 0.08553768606428372 | 2.1729517723710456 | 2.4557308639937196 | 17.2834812096568 | 28.931820005023166 | 3.7528619810100485 | 74.9382479 | 0.22928356263952965 | 0.03305371229631034 | 0.0472319275712025 | 0.5422676302624916 | 0.10193122279662485 | 0.22225240003320335 | 0.22225240003320335 | 0.08370023339953213 |
| Engineering/Construction | 42 | 0.08651148148000001 | 0.05567652186705069 | 0.19158078820440533 | 0.26452669039145904 | 0.9171641176368084 | 0.987915291 | 0.0885767321003 | 0.47331966 | 0.057800000000000004 | 0.15199105524120338 | 0.0817026733632642 | 3.862962070890738 | 1.4093068695496445 | 15.64699107043541 | 24.030910388290252 | 4.811546921270118 | 44.73407496 | 0.18589282923198996 | 0.02358246832645084 | 0.0385185288253212 | 0.8419758860713495 | 0.13082400113099374 | 0.082519841894834 | 0.08251984189483397 | 0.05839409008802537 |
| Entertainment | 96 | 0.1325096552 | 0.08339991531547873 | 0.09941346558875379 | 0.18832506154081263 | 0.937524322724562 | 1.040909254 | 0.0908713706982 | 0.626979123 | 0.057800000000000004 | 0.16899576961106283 | 0.08284046008408509 | 1.406969514219978 | 3.9046945294667585 | 19.61096687194483 | 45.58406244383965 | 4.0679110721849066 | 84.24318924 | 0.015271225517126164 | 0.036993536255993935 | -0.039181988163196985 | -0.7118566713135513 | -0.039027958459762736 | 0.00081707032 | 0.0008170703200000018 | 0.08256419725779691 |
| Environmental & Waste Services | 50 | 0.1963952381 | 0.14893092624522616 | 0.31722930695398477 | 0.22539063245351154 | 0.8154365927953799 | 0.920470271 | 0.0856563627343 | 0.544758219 | 0.057800000000000004 | 0.16194219947983726 | 0.07880517730111564 | 2.319389085585667 | 3.683161818039651 | 15.816653690727547 | 24.291419446245214 | 6.654633809226148 | 86.5905265 | 0.1012278675566884 | 0.08685273552228773 | 0.06417199514719471 | 0.5897643992973957 | 0.22316956149771278 | 0.3633210907300387 | 0.3633210907300387 | 0.1512014381016425 |
| Farming/Agriculture | 35 | 0.2223105263 | 0.0725286291815041 | 0.09966097926177687 | 0.23425644116474048 | 0.7317985276905549 | 0.982388156 | 0.0883374071548 | 0.695913261 | 0.0641 | 0.3478095566497602 | 0.07433375717263688 | 1.5671727482197484 | 1.1820781626784913 | 11.764311675282677 | 15.776928117367982 | 2.503453363855312 | 35.00291504 | 0.14866693371867232 | 0.0394226386992334 | 0.03360420334860541 | 0.44796406898590785 | 0.15326132462871572 | 0.3057061550448788 | 0.30570615504487875 | 0.07466480137741174 |
| Financial Svcs. (Non-bank & Insurance) | 166 | 0.1479327 | 0.1633057193708989 | NA | 0.18619370304267924 | 0.35059353202283133 | 1.073489898 | 0.0922821125834 | 0.4195847 | 0.0553 | 0.7413733708658856 | 0.05461507226348218 | 0.06810031517177884 | 19.30347905094736 | 62.82440097666481 | 79.26775330166299 | 3.797377982567915 | 30.21108272 | 12.499751151458387 | 0.026661393599936054 | 0.017918660321226597 | 0.14977712365084803 | 0.315488080050799 | 0.18129345640546582 | 0.1812934564054658 | 0.1643608663080031 |
| Food Processing | 77 | 0.1001784 | 0.1196989866600123 | 0.179008744988626 | 0.2415591084925007 | 0.38277695500353215 | 0.474240235 | 0.0663346021755 | 0.462695731 | 0.057800000000000004 | 0.2675164852672177 | 0.06018584218624499 | 1.6975230664187548 | 1.794561254105961 | 11.167310604446802 | 14.75500676313727 | 2.1753858995460424 | 27.67322876 | 0.05647943056639733 | 0.03988083049878293 | 0.043559980139493436 | 0.41589524150370255 | 0.09802418035108233 | 0.6795638505562032 | 0.6795638505562032 | 0.1213296889884875 |
| Food Wholesalers | 14 | 0.11898 | 0.02668323514122336 | 0.17303730342745285 | 0.23847853631388988 | 0.5547774624190575 | 0.724632235 | 0.0771765757755 | 0.391670258 | 0.0553 | 0.3020683236001308 | 0.06639226063111167 | 7.777325065179679 | 0.44417810691387977 | 10.770681593282227 | 16.860430568640545 | 4.514160864716116 | 29.30346327 | 0.0571128010743372 | 0.009943610292843528 | 0.014365742505631607 | 0.7230194392164317 | 0.20052924126260915 | 0.344994817550537 | 0.34499481755053707 | 0.026340675628140704 |
| Furn/Home Furnishings | 28 | -0.00282952381 | 0.0650643353627397 | 0.10653951148142196 | 0.21164392773352858 | 0.6901905810431348 | 0.866242693 | 0.0833083086069 | 0.54801472 | 0.057800000000000004 | 0.2954389234714598 | 0.07150306892833709 | 1.9591798093994046 | 1.183895108625572 | 10.17923705680146 | 17.216244074133204 | 2.3694622631620494 | 30.847498 | 0.15734604061775348 | 0.029978650800531234 | 0.011233594701056575 | 0.11503777765214553 | 0.05849960245124717 | 0.8433821399699984 | 0.8433821399699984 | 0.06858572865571802 |
| Green & Renewable Energy | 18 | 0.1573 | 0.21598234119080256 | 0.03668230812976016 | 0.057241379310344835 | 0.5005254491535094 | 1.130425266 | 0.0947474140178 | 0.719302568 | 0.0641 | 0.6379186419431446 | 0.06497421105135684 | 0.1882582558306389 | 6.383498113840869 | 11.304545504032925 | 31.905381263495403 | 0.7604581145144261 | 25.51122245 | -0.3754312702131538 | 0.49500958753350577 | 0.3815940335447929 | 1.5993934098834703 | -0.11574516676108294 | 0.00081832444 | 0.0008183244399999623 | 0.1973879701773694 |
| Healthcare Products | 218 | 0.1460585714 | 0.14812121552106344 | 0.14710425697558768 | 0.15966032970482166 | 0.9580877046258003 | 1.0145167 | 0.08972857310999999 | 0.674052859 | 0.0641 | 0.11340902578772541 | 0.0850046819630171 | 1.3345092640558633 | 5.200686146885706 | 21.19759515704529 | 33.633724884042 | 4.756612592973772 | 45.2516385 | 0.26694130053252635 | 0.047980860988146495 | 0.045760403063886256 | 0.5546286757135178 | 0.08881077313041913 | 0.3580752216461151 | 0.35807522164611516 | 0.1514690360825379 |
| Healthcare Support Services | 113 | 0.11339571429999999 | 0.03436937020226516 | 0.44602956452982473 | 0.23085871100828093 | 0.8153500076641338 | 0.941212934 | 0.08655452004219999 | 0.539967819 | 0.057800000000000004 | 0.2435768930799556 | 0.07603089728331025 | 14.649503528884146 | 0.5259930515797708 | 11.315758417060703 | 15.148910175226469 | 2.8942971689889623 | 38.82971906 | -0.06930645344028069 | 0.006333983394759203 | 0.00743260158898802 | 0.45953028085748876 | 0.11660456386084155 | 0.42183664735852133 | 0.42183664735852133 | 0.03427553986135274 |
| Heathcare Information and Technology | 116 | 0.14728 | 0.1335229870447581 | 0.12742981260508918 | 0.16510959748334217 | 1.1234093966584342 | 1.222923714 | 0.0987525968162 | 0.645438121 | 0.057800000000000004 | 0.1393804567634771 | 0.09103055756607528 | 1.2215732596318463 | 5.311889541228291 | 22.01135224050213 | 38.617519944721025 | 3.929559630568024 | 54.46738057 | 0.2310351474948779 | 0.04003716129722745 | 0.05378245546115293 | 0.38026780252615516 | 0.03933763839168482 | 0.256718261808874 | 0.256718261808874 | 0.13495449256441597 |
| Homebuilding | 30 | 0.09001090909000001 | 0.1552469366730168 | 0.21045792739664068 | 0.23178301071898474 | 1.3762359491843439 | 1.42748671 | 0.107610174543 | 0.414320248 | 0.0553 | 0.14894590395276014 | 0.09775961118761929 | 1.641118382058291 | 1.2430969824286757 | 7.647428900944848 | 7.974293672450544 | 1.7480275947698287 | 10.85248606 | 0.6317058112564676 | 0.005785892292905283 | 0.007289797351351661 | 0.513794661279955 | 0.20149423065772437 | 0.07297285112579148 | 0.07297285112579144 | 0.15587402563467992 |
| Hospitals/Healthcare Facilities | 33 | 0.01566052632 | 0.12448735406100417 | 0.21189861748431305 | 0.22234896117336775 | 0.5652613375247338 | 0.857081614 | 0.0829116338862 | 0.508099059 | 0.057800000000000004 | 0.43551540447634884 | 0.06568193290250637 | 1.9243115204339636 | 1.484022296092266 | 8.112146472634091 | 12.21014652807294 | 4.281727024179832 | 19.90376001 | 0.10773432975924571 | 0.05840345982571967 | 0.02940535781153524 | 0.3395703359082387 | 0.7610091187909209 | 0.23156761774438134 | 0.23156761774438128 | 0.12143678731352776 |
| Hotel/Gaming | 65 | 0.11904536589999999 | 0.18146969754607978 | 0.12172347058770536 | 0.14872131335374356 | 0.9507214498893468 | 1.193760779 | 0.0974898417307 | 0.450953288 | 0.057800000000000004 | 0.3017303728446324 | 0.08115420709954649 | 0.9762977965119558 | 4.28296044613172 | 15.417626243502292 | 28.231252598870075 | 14.590953327578633 | 33.74480756 | 0.02288364986375318 | 0.07779583455520896 | 0.02025023027892743 | 0.2541720868564456 | 0.4205107674642232 | 0.15158277264503262 | 0.15158277264503262 | 0.1490485912543498 |
| Household Products | 101 | 0.031504090910000004 | 0.18381524828445367 | 0.33557667664941937 | 0.2249200888022358 | 0.8289296813883512 | 0.895264979 | 0.0845649735907 | 0.566703537 | 0.057800000000000004 | 0.1321202007981977 | 0.0791196430040043 | 2.217432544077391 | 3.5277078107468967 | 15.311705988267818 | 18.971627471249754 | 7.331355612163251 | 32.1738381 | 0.06895979054658521 | 0.035264087119431374 | 0.002175810487227502 | 0.012952164540033463 | 0.2624495610799743 | 0.7387863810748427 | 0.7387863810748427 | 0.18562429495005234 |
| Information Services | 16 | 0.025249999999999998 | 0.11538316523706287 | 0.24548990546783805 | 0.23243235864253148 | 0.8031590545209226 | 0.984489325 | 0.0884283877725 | 0.396580654 | 0.0553 | 0.2612694166130669 | 0.07616090354117182 | 2.732013145091482 | 2.269212322276089 | 11.747539906963985 | 18.678481750561183 | 3.7266775487361254 | 21.27761649 | 0.16870250399329484 | 0.020095380515778288 | 0.03725775922024389 | 0.4471010416321389 | 0.159033666768628 | 0.34174987723031597 | 0.341749877230316 | 0.12244160335564143 |
| Insurance (General) | 22 | 0.1298025 | 0.164310729269812 | 0.17446771472463615 | 0.16954804866527337 | 0.6896826641236571 | 0.760364469 | 0.0787237815077 | 0.510071782 | 0.057800000000000004 | 0.14787928662976846 | 0.07349273193294403 | 1.1641427939095834 | 3.114533941571186 | 13.017606684305473 | 18.82666484490262 | 3.093612910505429 | 58.24358392 | -0.10194221183914387 | 0.00754062251864311 | 0.004719125790251846 | 0.24090411691201394 | 0.05625314862883568 | 0.8352296629100675 | 0.8352296629100675 | 0.16494256638950247 |
| Insurance (Life) | 19 | 0.03704733333 | 0.08206657647517031 | 0.06964505786786918 | 0.21271817055092468 | 0.6205348110956823 | 0.731672262 | 0.0774814089446 | 0.343126708 | 0.0553 | 0.38547717601130227 | 0.0636017601063275 | 0.9872542563059108 | 1.2376599868418128 | 11.698376152776595 | 14.398949767417532 | 1.5262221547976622 | 46.46403095 | 0.2013400271562588 | 0.001602865652273081 | -0.011900991639857614 | -0.012846672585224567 | 0.11889819319599934 | 0.41553641065353875 | 0.41553641065353875 | 0.08251450920702572 |
| Insurance (Prop/Cas.) | 53 | 0.09121866667 | 0.13631717261708118 | 0.21986027180636247 | 0.20317549016972772 | 0.5690197716125752 | 0.605663581 | 0.07202523305729999 | 0.336883546 | 0.0553 | 0.13391402267011 | 0.06793412845508758 | 1.9113389894888644 | 1.5092144680220723 | 10.216278469520937 | 10.963945562667854 | 2.332330037266932 | 16.58902576 | -0.38805051280630365 | 0.00762760479386508 | 0.006145288725294821 | 0.2265529246528915 | 0.22604897277800795 | 0.1687574507700016 | 0.1687574507700016 | 0.13702141254052255 |
| Investments & Asset Management | 231 | 0.08365945455 | 0.1448782157009349 | 0.06797686012793668 | 0.1871866203241025 | 0.49932623482699845 | 0.567136155 | 0.0703569955115 | 0.229410333 | 0.0508 | 0.25950157646332855 | 0.061986254324295234 | 0.5165450044947686 | 6.012389746607367 | 41.40436735972429 | 41.45081431631505 | 2.5278122168665753 | 56.09787202 | NA | 0.024697760708194686 | 0.054996961891315664 | 0.48858293195856894 | 0.13317232180589358 | 0.5962939888899269 | 0.5962939888899269 | 0.14125835342517715 |
| Machinery | 109 | 0.062251029410000006 | 0.1578997061601933 | 0.2475872269593568 | 0.21009485897951116 | 0.9835242099250273 | 1.067242281 | 0.0920115907673 | 0.460733301 | 0.057800000000000004 | 0.13568778466035222 | 0.08540880731803642 | 1.9682598139763747 | 3.2279049143312166 | 15.350424128173863 | 20.022926217249612 | 4.273411612510947 | 33.32676744 | 0.2544408663349021 | 0.02385872521610842 | 0.05032307501088092 | 0.35902577677855047 | 0.16564120986417863 | 0.34237039342996284 | 0.3423703934299629 | 0.15989798855104875 |
| Metals & Mining | 64 | 0.01841384615 | 0.22622928199945197 | 0.27131917252639576 | 0.3624319632132132 | 0.9615982694311441 | 1.022250551 | 0.0900634488583 | 0.723723464 | 0.0641 | 0.1435430682523116 | 0.08403629807802435 | 1.2286156999263649 | 2.886818055495662 | 8.68043322884353 | 12.272594960246712 | 3.1156411055280255 | 74.86384367 | 0.16545695284640777 | 0.13377770985457035 | 0.05852663365934226 | 0.5707814590542162 | 0.12502993777199908 | 0.6906320072824792 | 0.6906320072824792 | 0.22647118253788354 |
| Office Equipment & Services | 14 | 0.1414766667 | 0.08166045516693865 | 0.15003946621251396 | 0.21647969820311724 | 0.9638143971905709 | 1.200495591 | 0.0977814590903 | 0.498920038 | 0.057800000000000004 | 0.31743720141192583 | 0.08050288904790745 | 2.3287714864040083 | 1.2000344991840515 | 8.76539448895973 | 14.162061901038948 | 2.8565260458936685 | 14.81153835 | 0.06589980373131035 | 0.021693864949499403 | -0.002225874388038631 | -0.2215695106611476 | 0.03370770816230284 | 2.012591978443362 | 2.012591978443362 | 0.0847558576280157 |
| Oil/Gas (Integrated) | 4 | 0.0019500000000000001 | 0.13434037495005738 | 0.12903399917583033 | 0.30257394807397847 | 0.45577993390039784 | 0.483682004 | 0.0667434307732 | 0.255595298 | 0.0508 | 0.12058731670495794 | 0.06328939631503559 | 1.2679674608622964 | 1.5157081668506258 | 6.695477232545713 | 11.05501460755642 | 1.6638981685489767 | 10.82668985 | 0.03614715534637552 | 0.08382716319151502 | 0.01930391086244483 | 0.2827516366049607 | 0.14204315331349052 | 0.5237170589950078 | 0.5237170589950078 | 0.13718197508137822 |
| Oil/Gas (Production and Exploration) | 147 | 0.053528533329999996 | 0.2954045788633479 | 0.18619988925264025 | 0.23663744833137312 | 0.7545351031706402 | 0.875929343 | 0.08372774055189999 | 0.476588509 | 0.057800000000000004 | 0.21040224261825277 | 0.07523217338792226 | 0.6674241236462098 | 3.077233951149892 | 5.602267266776679 | 10.139033098061212 | 1.7398879827728644 | 19.10246638 | 0.01525015817993553 | 0.36742825347942487 | 0.17944803046179625 | 0.7439264567808016 | 0.17604362804614881 | 0.3763251022313812 | 0.37632510223138116 | 0.3006389033463689 |
| Oil/Gas Distribution | 24 | 0.1987206667 | 0.2806157892822455 | 0.12176139467315485 | 0.19723763310080308 | 0.5507758746918867 | 0.754707504 | 0.0784788349232 | 0.381741501 | 0.0553 | 0.3401007614865949 | 0.06589380248789542 | 0.48899530900155047 | 4.981084711853547 | 12.164142478812128 | 17.29980936773354 | 3.211874642531892 | 27.81791682 | 0.02868263015219864 | 0.22848825007987825 | 0.15403105351560173 | 0.647540262621836 | 0.1974651283929793 | 0.6072511720282857 | 0.6072511720282857 | 0.2845553222334854 |
| Oilfield Svcs/Equip. | 97 | 0.052465846149999995 | 0.04992682091832309 | 0.1436713162033353 | 0.19763425933334403 | 0.7777793295038246 | 0.937600524 | 0.08639810268920001 | 0.494883871 | 0.057800000000000004 | 0.27810053473826807 | 0.0744264023118656 | 3.131938639340938 | 0.607283601699653 | 7.350017313645032 | 11.6967200492003 | 1.7462429767106171 | 29.32508777 | 0.0750729312075754 | 0.0238504668214339 | 0.0020219680375014736 | -0.01485777502880382 | 0.1326556225567935 | 0.3872444431193258 | 0.3872444431193258 | 0.05185005944104041 |
| Packaging & Container | 22 | 0.040221666669999996 | 0.09790343714371146 | 0.14486486031209506 | 0.21399991291817783 | 0.7383541924466364 | 0.97636341 | 0.088076535653 | 0.339754281 | 0.0553 | 0.3460358130070013 | 0.07195073537593938 | 1.7435134987048067 | 1.540926439760242 | 9.457927000705379 | 15.428794145134688 | 2.849047681033775 | 26.09845032 | 0.10248734884452107 | 0.05627402504057689 | 0.016203867343771897 | 0.14127571050488755 | 0.20757287742616085 | 0.32348788287142144 | 0.3234878828714214 | 0.09978523098639712 |
| Paper/Forest Products | 6 | 0.04535 | 0.10131943754571975 | 0.19419479914040808 | 0.2559991616891963 | 0.9588822117328989 | 1.07174103 | 0.092206386599 | 0.606574576 | 0.057800000000000004 | 0.18411329851970282 | 0.0832112761085043 | 2.474249268999992 | 1.2326955404636546 | 7.873352437265647 | 11.956087664450166 | 3.5653256212510716 | 23.33602332 | 0.0816046383512901 | 0.05326517895041046 | 0.07868760667937034 | 0.8213447510412241 | 0.24202243428762765 | 0.1950747094631987 | 0.19507470946319871 | 0.10331066929169413 |
| Power | 48 | 0.05061857143 | 0.19751182991756608 | 0.06564911548274062 | 0.13258131129564985 | 0.3427138343438257 | 0.542348627 | 0.0692836955491 | 0.273142734 | 0.0508 | 0.4454796177988055 | 0.05539199477433261 | 0.3801204647508593 | 4.325013095388234 | 11.873306592314158 | 21.890159750197203 | 2.073412973548015 | 23.26783271 | 0.08032609640709555 | 0.3649187842429746 | 0.2357328538153427 | 1.429602507657313 | 0.11130193260347093 | 0.554637751117826 | 0.554637751117826 | 0.1967316783998681 |
| Precious Metals | 60 | 0.0447 | 0.18829183593579835 | 0.1292686842301033 | 0.4290331303194571 | 1.1452183128750493 | 1.228314776 | 0.0989860298008 | 0.709719516 | 0.0641 | 0.15894994616948027 | 0.09089372435453003 | 0.7092830047628302 | 3.0618240426997394 | 8.167722151394198 | 15.627358292343562 | 1.6107917556952125 | 28.22042495 | 0.20137848430887303 | 0.20150781992714806 | 0.030208703112695925 | 0.588083549381841 | -0.03815832614932794 | 0.01532136664 | 0.015321366640000056 | 0.18924617224540177 |
| Publishing & Newspapers | 19 | 0.01501333333 | 0.08301568593211756 | 0.15529613776373735 | 0.32131793860884256 | 0.5573432866995673 | 0.637353091 | 0.0733973888403 | 0.410004918 | 0.0553 | 0.22296848382654758 | 0.06627970220045681 | 2.2554075844500825 | 1.5926717159618449 | 11.093233553255816 | 19.22025789957895 | 2.25767800886576 | 25.08409747 | 0.10880574457669615 | 0.03492547064851126 | -0.0063874491321072166 | -0.03233708585488725 | 0.041853467616081864 | 0.7275574237232688 | 0.7275574237232688 | 0.08282770856475201 |
| R.E.I.T. | 192 | 0.07056878788 | 0.2448459776072924 | 0.030943075263370073 | 0.03502494522018959 | 0.5944283083931003 | 0.947227237 | 0.0868149393621 | 0.320770821 | 0.0553 | 0.45500220616438203 | 0.06618516692498519 | 0.14175359905867305 | 10.830765392411573 | 20.33178362353982 | 43.92180303887089 | 2.005629185642519 | 51.7842795 | 1.2938522711502523 | 0.029696867217088883 | -0.14198715050017852 | -0.6581426158989507 | 0.047340170324202686 | 2.03798541808363 | 2.03798541808363 | 0.22229031072473096 |
| Real Estate (Development) | 15 | 0.151 | 0.14741909792198638 | 0.03734709120429483 | 0.1826940517471326 | 0.6150110038893978 | 1.02618833 | 0.090233954689 | 0.49682192 | 0.057800000000000004 | 0.5208652046108243 | 0.0658137340369494 | 0.28405101940074207 | 3.958248083561817 | 14.935370005087758 | 27.384816277187706 | 1.1412158224225333 | 40.49470653 | 0.030247300573384317 | 0.020967475037198677 | -0.06168253720540396 | -1.0603866958563923 | 0.06342371782701332 | 0.0006501046214879232 | 0.0006501046214879569 | 0.13484155926361419 |
| Real Estate (General/Diversified) | 11 | 0.143496 | 0.11065093708165998 | 0.03973051125363468 | 0.14280428363041234 | 0.7367049503976224 | 0.864194343 | 0.0832196150519 | 0.26527845 | 0.0508 | 0.2954722215526159 | 0.06988802215691625 | 0.3737527636213412 | 4.097515446787149 | 14.224590455661255 | 31.136453335955135 | 0.9479464548396587 | 17.88432292 | 2.1197172021419006 | 0.021623995983935742 | 0.013348393574297183 | 1.0821106152319355 | 0.04313063815569663 | 0.5577504066930049 | 0.5577504066930049 | 0.11242361746987951 |
| Real Estate (Operations & Services) | 60 | 0.045311153849999994 | 0.01393407366548548 | 0.028763124525455864 | 0.18819227728766463 | 0.9516898093790228 | 1.075216812 | 0.09235688795960001 | 0.565339353 | 0.057800000000000004 | 0.223516479710678 | 0.0814030408812946 | 2.3061889572841 | 1.5307462963673806 | 20.833733868250523 | 90.18798277082739 | 2.8493760079491484 | 63.94075126 | 0.12366082312918376 | 0.016275392938852926 | 0.018320039500273166 | 3.6429856021044453 | -0.01905926688079955 | 0.03039534048 | 0.030395340480000033 | 0.014608008482760783 |
| Recreation | 50 | 0.0877137931 | 0.0903615757144022 | 0.07946131550975259 | 0.2198994417229918 | 0.9335936700245824 | 1.327897225 | 0.1032979498425 | 0.53062303 | 0.057800000000000004 | 0.3943031040564273 | 0.07966028713778324 | 1.293679154403314 | 1.9894583442029383 | 10.668698265051631 | 25.201245830142568 | 3.0985357561435602 | 33.91159809 | 0.16986987891583769 | 0.06780151813226594 | 0.023924166811692786 | 0.14852085535701345 | 0.017487855284722388 | 3.2895854718588247 | 3.2895854718588247 | 0.07396940064734013 |
| Reinsurance | 1 | 0.0966 | 0.05513646962007955 | 0.09890324421774312 | 0.20130576713819368 | 0.5778829574543252 | 0.537329871 | 0.06906638341429999 | 0.198658127 | 0.0508 | 0.2678036348779579 | 0.06077347337692594 | 2.238247886300918 | 0.6410632300096009 | 11.047014913731978 | 11.58721489809192 | 1.2543995720780958 | 19.35433287 | 0.04110090065377406 | 0 | -0.001979609564303022 | 0.5108018008533212 | 0.09016495101079003 | 0.312242090784044 | 0.31224209078404397 | 0.05532504882732135 |
| Restaurant/Dining | 62 | 0.08597307691999999 | 0.15960254602877869 | 0.20394892204796075 | 0.20465304109413093 | 0.8749739210888298 | 1.009040065 | 0.0894914348145 | 0.415043245 | 0.0553 | 0.18789372628014492 | 0.08046944795451591 | 1.655671489755043 | 4.469184534191943 | 18.667676815197808 | 32.10677664883862 | NA | 56.60443767 | -0.00394809126743371 | 0.06274623878463635 | 0.04146306550972133 | 0.387192687801366 | NA | 0.5512272884125671 | 0.5512272884125671 | 0.13959270726915785 |
| Retail (Automotive) | 29 | 0.103217619 | 0.06013251795404904 | 0.12115010427606814 | 0.2257835935470156 | 0.9917642043796703 | 1.353074414 | 0.1043881221262 | 0.473945116 | 0.057800000000000004 | 0.33510223813957135 | 0.08393411078987388 | 2.4663966081903905 | 1.222045850009327 | 14.419927914163718 | 21.681945615914966 | 7.777014645233271 | 123.0704727 | 0.12188531804157499 | 0.020009321980419263 | 0.02493638465561772 | 0.8289858427080858 | 0.35699248801731837 | 0.05961556234279155 | 0.05961556234279153 | 0.05586664024484593 |
| Retail (Building Supply) | 13 | 0.05149083333 | 0.12124630894860067 | 0.3628459653896072 | 0.23817452639636 | 1.574546568160133 | 1.792774397 | 0.1234271313901 | 0.521259821 | 0.057800000000000004 | 0.16797788462082947 | 0.10997594425268678 | 3.5706348388844233 | 2.5168840644209354 | 15.746684126619444 | 20.752329820525382 | NA | 42.96360355 | 0.08352757120989122 | 0.02420334999180278 | 0.0715703846430157 | 0.7168921587957251 | NA | 0.53225823359673 | 0.53225823359673 | 0.11977489830842546 |
| Retail (Distributors) | 66 | 0.07073414634 | 0.10559724307801825 | 0.17536861677582882 | 0.24372011263235407 | 0.9254645175303127 | 1.117155906 | 0.0941728507298 | 0.438886042 | 0.0553 | 0.23820734397611792 | 0.08161983567420442 | 1.880634510325728 | 1.8141684070556663 | 12.874163371741568 | 15.744115641148806 | 4.303197415415965 | 51.90215662 | 0.17020865900643473 | 0.05835726344340757 | 0.07671691227770815 | 1.0195443860624036 | 0.21635698612262233 | 0.3121855201758274 | 0.31218552017582746 | 0.10791543860104447 |
| Retail (General) | 24 | 0.1439742105 | 0.06201301531080719 | 0.11983290770437496 | 0.19835937513442456 | 1.0255755386066459 | 1.061771934 | 0.0917747247422 | 0.466898824 | 0.057800000000000004 | 0.08027535408126109 | 0.0878874128172323 | 3.5951299451019962 | 2.050871333564441 | 18.20902196898702 | 34.66223707061496 | 8.428688099762482 | 25.79221081 | 0.0069049320335358285 | 0.057537256815085584 | 0.021600848026036377 | 0.4641145450266851 | 0.25368084600002294 | 0.14172819017903793 | 0.14172819017903793 | 0.059976342513351315 |
| Retail (Grocery and Food) | 17 | 0.09281 | 0.033325604942954244 | 0.09247376187945984 | 0.21096293504573324 | 0.4663235292503023 | 0.579407306 | 0.0708883363498 | 0.271282461 | 0.0508 | 0.343215525192746 | 0.059634870269306986 | 4.893097606432322 | 0.494972467929007 | 7.73939838475208 | 16.88568810033508 | 3.497688639613604 | 21.11570182 | -0.001995689640997077 | 0.02743874200075055 | 0.0025903700967199864 | 0.14685770979269633 | 0.21090257168217028 | 0.236694556868387 | 0.23669455686838703 | 0.024582375791246495 |
| Retail (REITs) | 28 | 0.07910038462 | 0.38879345924804937 | 0.04999389101400612 | 0.03203294562858256 | 0.6859427120656839 | 0.94758859 | 0.086830585947 | 0.235572061 | 0.0508 | 0.35390072696862224 | 0.06958479615474976 | 0.13573524804042503 | 12.21753601147776 | 17.4419383365469 | 32.77459286785557 | 2.015499883545752 | 72.23515241 | -0.0547072581120654 | 0.04290017884868615 | -0.26575609756097557 | -0.748802126384674 | 0.07340315755134588 | 1.4364006576861084 | 1.4364006576861084 | 0.37279033104695275 |
| Retail (Special Lines) | 98 | 0.06785274194 | 0.05097611201807646 | 0.1767838502882247 | 0.23366272749859898 | 1.0592547675648005 | 1.223962594 | 0.0987975803202 | 0.569960812 | 0.057800000000000004 | 0.22440271815045107 | 0.08635499258148166 | 3.677187121640216 | 1.0697959500151255 | 9.895888372898733 | 19.988363782118277 | 5.871263425781446 | 24.48494405 | 0.04947974434029326 | 0.024350612794780534 | 0.007260282299794612 | 0.2384246819225872 | 0.10134724746541818 | 0.8642616405994955 | 0.8642616405994955 | 0.053157658105189375 |
| Rubber& Tires | 3 | 0.027549999999999998 | 0.040436780162376486 | 0.057556753506032426 | #DIV/0! | 0.1780746040367293 | 0.645345391 | 0.0737434554303 | 0.720368676 | 0.0641 | 0.7947160233881684 | 0.05334432260421555 | 1.5003253061530804 | 0.6157089238886442 | 5.677884532107041 | 14.149107124847289 | 0.5261558731123949 | #DIV/0! | 0.1283259382801519 | 0.06057649946503871 | 0.0064504793672771525 | 0.16171849409183106 | -0.06413687820932215 | #DIV/0! | #DIV/0! | 0.04256184664967378 |
| Semiconductor | 63 | 0.05131886364 | 0.2971116134346505 | 0.21144652173406386 | 0.14190702210640413 | 1.4601551161065303 | 1.485871504 | 0.1101382361232 | 0.560486072 | 0.057800000000000004 | 0.03747861955904781 | 0.10763510523051874 | 1.1023163547709465 | 14.645136031617927 | 34.47976073847495 | 48.853838409004744 | 11.12123958640339 | 54.21845143 | 0.203450318876862 | 0.1325155150629162 | 0.11600239559724274 | 0.5930815713362112 | 0.19084697104786927 | 0.32634631628070393 | 0.3263463162807039 | 0.3144019419558283 |
| Semiconductor Equip | 30 | 0.116725 | 0.2406234259235884 | 0.24197449544323665 | 0.12586026384945445 | 1.4745155675062604 | 1.484975954 | 0.11009945880819999 | 0.510930714 | 0.057800000000000004 | 0.07557801091410334 | 0.10505466748188336 | 1.6833471274291145 | 5.069166449025872 | 17.733051139589943 | 20.926140364357934 | 6.970205981851539 | 71.34768494 | 0.32724535175360886 | 0.04650401510953067 | 0.021214202221508948 | 0.04667986081335397 | 0.31784500493054746 | 0.20804682750970707 | 0.20804682750970704 | 0.24840614231914826 |
| Shipbuilding & Marine | 8 | -0.042679999999999996 | 0.13739293792172794 | 0.13232356550929528 | 0.2060037192913771 | 0.5248238080556044 | 0.57844977 | 0.070846875041 | 0.451893002 | 0.057800000000000004 | 0.1604635798786198 | 0.06643462803644606 | 0.9375867084126069 | 1.7491091978050035 | 7.7139416157820575 | 11.585715174691481 | 1.605174159213743 | 12.7685681 | 0.10341773076541534 | 0.10180449326206187 | 0.04677173514901479 | 0.4417924406546218 | 0.11718743679126227 | 0.15050901924356352 | 0.15050901924356352 | 0.1497942355390159 |
| Shoe | 12 | 0.0990625 | 0.12820574035012822 | 0.2912089771267716 | 0.16763413851482192 | 1.4086385456424702 | 1.424207891 | 0.1074682016803 | 0.517524117 | 0.057800000000000004 | 0.09294187987435525 | 0.10150893548196988 | 2.5356270056745536 | 2.4017041674975634 | 14.770185001070939 | 18.457142037087245 | 6.741298105170388 | 17.57809169 | 0.19568711187756468 | 0.007944000831364928 | -0.00794574220384732 | -0.08230189069000453 | 0.31672211045805776 | 0.32504532056515784 | 0.3250453205651578 | 0.1301559408326569 |
| Software (Entertainment) | 81 | 0.2806917647 | 0.32367209422672144 | 0.2529435269270178 | 0.15053173892351865 | 1.1833988427238291 | 1.182782103 | 0.0970144650599 | 0.66628958 | 0.0641 | 0.024296047356735302 | 0.09582542949919137 | 1.3970196738508474 | 7.345462856049665 | 18.27402621276981 | 22.459003609744194 | 7.7104509035941335 | 68.17906807 | 0.04974142540696422 | 0.15069195860015666 | 0.1138596997532106 | 0.47974527461100563 | 0.3345642404399427 | 0.059483802001344954 | 0.059483802001344954 | 0.33505217703126305 |
| Software (Internet) | 29 | 0.1972083333 | 0.01311510803818907 | 0.029315361747272173 | 0.12622972608967076 | 1.5986239005097629 | 1.687026441 | 0.11884824489529999 | 0.556166978 | 0.057800000000000004 | 0.10348217224030058 | 0.11103552251320417 | 1.2317197291379707 | 7.589087565794395 | 28.08006683746375 | NA | 8.719427821180213 | 50.6412608 | 0.10195017636271114 | 0.04286864312115726 | 0.024250902453430468 | 3.764390677507587 | -0.03085095614661618 | 0.00013770325 | 0.0001377032499999542 | 0.042337843902451065 |
| Software (System & Application) | 333 | 0.1555315493 | 0.28631658213930083 | 0.2685477285289906 | 0.17372113877129391 | 1.2190339285497593 | 1.241760834 | 0.0995682441122 | 0.636284864 | 0.057800000000000004 | 0.04667109757935985 | 0.09694447695549925 | 1.7141776006664302 | 11.543734848591981 | 27.978212114920282 | 37.850738061107265 | 10.733765678170464 | 203.7719298 | 0.10581055834537492 | 0.11958977395044544 | 0.21011597941116059 | 0.93539436133576 | 0.27664221670097855 | 0.23176224004903084 | 0.2317622400490309 | 0.30049989034140007 |
| Steel | 27 | 0.06051583333 | 0.07605822887692532 | 0.12494672128873931 | 0.1866940765884209 | 0.9639390334814825 | 1.05977921 | 0.09168843979300001 | 0.467902736 | 0.057800000000000004 | 0.2056982038589905 | 0.08174530955023396 | 1.855004733537124 | 0.887388116825059 | 7.517316862652473 | 11.566499852584055 | 1.4229678027129475 | 15.02257097 | 0.19146593285137128 | 0.075305799854803 | 0.049794273240634554 | 0.6084524552700056 | 0.10041297286139539 | 0.20943523814289522 | 0.20943523814289522 | 0.07647490666248957 |
| Telecom (Wireless) | 11 | 0.2806725 | 0.20147395975539462 | 0.08305425936497644 | 0.24089288108515727 | 0.58526739373043 | 0.772539146 | 0.0792509450218 | 0.667326915 | 0.0641 | 0.32254087570054973 | 0.06919542841367643 | 0.5167546319134271 | 4.15150308898799 | 9.843701954698677 | 21.967971806851832 | 3.5080037399413166 | 13.3597627 | 0.09035207528852948 | 0.11373822804120673 | -0.047718937847524664 | 0.06822127620077649 | 0.13417482253514232 | 0.3153366694762964 | 0.31533666947629646 | 0.18900872750163605 |
| Telecom. Equipment | 61 | 0.025522291670000002 | 0.17490719670287783 | 0.2177054718093945 | 0.10244037219902397 | 0.9483963215929979 | 0.999614648 | 0.08908331425839999 | 0.560934426 | 0.057800000000000004 | 0.11350800707772311 | 0.0838922168998698 | 2.669183642701123 | 5.479900052960705 | 21.766350676481835 | 29.902931442066308 | 6.911004688868769 | 46.05597165 | 0.24911288660028066 | 0.029582183569742293 | 0.26114498331874886 | 1.5162671716874174 | 0.1503452787522845 | 0.6691295820704013 | 0.6691295820704013 | 0.1841453647965715 |
| Telecom. Services | 32 | 0.105799 | 0.20346195325377506 | 0.1168586516115778 | 0.28301670118193933 | 0.5150726409519035 | 0.886038614 | 0.0841654719862 | 0.637091179 | 0.057800000000000004 | 0.5004169769643724 | 0.06374071688149177 | 0.5922678617812643 | 2.563505864854464 | 6.618966238101931 | 12.281153635423223 | 1.6220825706185245 | 25.51708033 | -0.02619425804434495 | 0.14643746938324614 | 0.0016218816990425423 | 0.038956674413500404 | 0.07746513753344163 | 1.178420807376031 | 1.178420807376031 | 0.20646024162442983 |
| Tobacco | 12 | -0.0051542857099999995 | 0.4104696070690012 | 0.5789921248582272 | 0.22089489521036715 | 0.8250398443426944 | 0.979968253 | 0.08823262535490001 | 0.683432507 | 0.0641 | 0.21850684001661214 | 0.07945790953602982 | 1.7295163968284217 | 5.537373974975528 | 12.351530214414623 | 13.422569017122045 | NA | 15.28964314 | 0.15221849660983588 | 0.02730416469399122 | -0.006025102637536636 | -0.013103944020907228 | NA | 0.744767515253524 | 0.744767515253524 | 0.41216607778207126 |
| Transportation | 21 | 0.08572428571 | 0.06834441308516317 | 0.1089542373441166 | 0.19644394413311603 | 0.8323467894508807 | 1.026899078 | 0.09026473007739999 | 0.516753402 | 0.057800000000000004 | 0.27905061935740655 | 0.07717314559231597 | 1.9438034247568625 | 1.5760401872467884 | 11.794225725241436 | 21.82202147496412 | 4.8854504792465905 | 24.83280336 | 0.07072219497785746 | 0.05613036869425785 | 0.03471645534761659 | 1.0095105897567116 | 0.1732466371886561 | 0.5978316333615453 | 0.5978316333615453 | 0.06830592734504456 |
| Transportation (Railroads) | 4 | 0.0223 | 0.38313530147727365 | 0.15062156493399784 | 0.23259321829371304 | 0.8268042765704411 | 0.991856107 | 0.08874736943309999 | 0.265599529 | 0.0508 | 0.2211382775666099 | 0.07754729739338449 | 0.47509810066637165 | 6.276096219003287 | 12.55883378642996 | 16.403978960543967 | 5.7917933026902615 | 19.92768709 | 0.01012760038233488 | 0.1988219112081627 | 0.09430927162096003 | 0.3189368237221375 | 0.31992256328814483 | 0.42724562146779754 | 0.42724562146779754 | 0.3825959685817086 |
| Trucking | 24 | 0.1022627778 | 0.0696834566171777 | 0.09299440516178187 | 0.24091420495127222 | 0.9646536256536747 | 1.104813204 | 0.0936384117332 | 0.321800942 | 0.0553 | 0.18643277958512136 | 0.08391344189113639 | 1.6281746952724945 | 1.8533738985390344 | 11.329962641638978 | 25.314404890062036 | 3.226670548989158 | 335.5151302 | 0.0704402986038363 | 0.14730258749801634 | 0.09085369367456267 | 1.6422339837953763 | 0.09323625722668266 | 0.23428414208931425 | 0.23428414208931425 | 0.07161627256450262 |
| Utility (General) | 14 | 0.02362214286 | 0.23277003858979722 | 0.060541913857707054 | 0.10640099363124654 | 0.2501807366180015 | 0.393437747 | 0.0628358544451 | 0.182144764 | 0.0508 | 0.43837816797525603 | 0.05199219589015447 | 0.2937142289822406 | 5.238603373307601 | 13.43981735863711 | 22.708466614939166 | 1.8234183995388085 | 18.71716615 | 0.060863152512305625 | 0.464392812938704 | 0.30653922157705915 | 1.5320810969483256 | 0.10812006094726512 | 0.6322813722270325 | 0.6322813722270325 | 0.23068943676986509 |
| Utility (Water) | 15 | 0.1164666667 | 0.3310642355108798 | 0.06959237321145335 | 0.16358856638156224 | 0.47321201737160523 | 0.678567197 | 0.07518195963009999 | 0.291677801 | 0.0508 | 0.36963856764413655 | 0.06147503718699213 | 0.23750271221398803 | 7.509319274948086 | 15.027217298270639 | 22.558596050932096 | 2.0547679174434674 | 23.13437709 | 0.10763973741455986 | 0.5587284748870998 | 0.4184202999074465 | 1.5664814339057058 | 0.15933623251563078 | 0.5782618108947731 | 0.37933536416241576 | 0.3306378575708055 |
| Total Market | 6062 | 0.09966282036000002 | 0.12082027487417142 | 0.08728270994558283 | 0.19324455633307253 | 0.8167518764285684 | 1.002779668 | 0.0892203596244 | 0.525326392 | 0.057800000000000004 | 0.2815127907823082 | 0.07630726667234705 | 0.8431269668834348 | 3.64615550043554 | 18.597580056961124 | 28.26574274666995 | 4.308601916726718 | 48.85612744 | -0.21701985477065053 | 0.05875142977484411 | 0.04214832041393187 | 0.4772723193371768 | 0.15933623251563078 | 0.3793353641624157 | 0.37933536416241576 | 0.12264077943971394 |
| Total Market (without financials) | 4935 | 0.10246298224008107 | 0.11934234745453784 | 0.15008472975146017 | 0.19335597694893408 | 0.9767930643706536 | 1.0857816776984806 | 0.09281434664434421 | 0.5739628547189463 | 0.057800000000000004 | 0.16170905004468053 | 0.08481551413740654 | 1.5606598104159137 | 2.987722286202415 | 15.831102273722884 | 24.411761199614997 | 5.0970317355598365 | 53.282762874549164 | 0.08252203941622305 | 0.06078159317458977 | 0.0434739032018408 | 0.5079011864198951 | 0.16407375407096406 | 0.39682647940453203 | 0.396826479404532 | 0.1213209947335242 |

## Industry Average Beta (Global)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 417 | 0.06845644351464436 | 0.07913067219612407 | 0.21482336224002138 | 0.27772030741013054 | 1.1531366444558786 | 1.254409764675642 | 0.11742679756297916 | 0.47409030355897464 | 0.0682 | 0.21907007610000434 | 0.1028746652029747 | 3.383463127892816 | 1.6457239785378095 | 12.92025260266753 | 19.470706486361774 | 2.8478508119646855 | 83.11145737364957 | 0.0035044234029197167 | 0.01726374903867861 | 0.0004019883057349198 | 0.19188668826893185 | 0.06775942528719077 | 0.8857034224859133 | 0.8857034224859133 | 0.080901122750602 |
| Aerospace/Defense | 300 | 0.09738137362637367 | 0.07974262337171378 | 0.13729203977947993 | 0.17428076979295634 | 0.9590867663115341 | 1.037195471112474 | 0.10502386140052226 | 0.40681270069304865 | 0.0657 | 0.15916292005563432 | 0.09612770442177346 | 2.5396295766760097 | 2.4742340513883314 | 17.81701844239874 | 27.493400274781134 | 5.419325740426683 | 97.71456478973904 | 0.3692140677291876 | 0.03612398833244467 | 0.02590480889773784 | 0.9898289273191564 | 0.13402938524886077 | 0.45591558195131565 | 0.45591558195131565 | 0.08261641855121409 |
| Air Transport | 151 | 0.0470309375 | 0.07844318023938146 | 0.08850245019032303 | 0.18327850297384737 | 0.8505119212104351 | 1.2946167772204054 | 0.11972261797928516 | 0.34980433042159803 | 0.0657 | 0.48039790421242834 | 0.0858102932322039 | 1.337815041270704 | 1.314093924202901 | 8.859743965106361 | 16.544135959367118 | 2.3421281268207106 | 42.00202574687905 | -0.029945450543038217 | 0.09629529883903551 | 0.03319093699540186 | 0.5393379365190375 | 0.2057306858888202 | 0.2968499633985163 | 0.2968499633985163 | 0.07803032980438115 |
| Apparel | 1194 | 0.032728793650793675 | 0.1420871608461303 | 0.18859814493129912 | 0.2519608113798398 | 0.6944286080738915 | 0.7505397384113048 | 0.08865581906328551 | 0.38575066387969126 | 0.0657 | 0.1641661410566406 | 0.08216709339198781 | 1.5685523836893338 | 2.300082542343417 | 12.737551855791756 | 15.694507480997327 | 3.187809316791018 | 50.66818776166972 | 0.2301052942513817 | 0.048569456351802064 | 0.03638036258163637 | 0.47113928552253975 | 0.14562582622166154 | 0.5234031699562627 | 0.5234031699562627 | 0.1436296327436913 |
| Auto & Truck | 162 | 0.12695689320388354 | 0.0670663972886944 | 0.07142845891959625 | 0.23279848887114113 | 1.2450163798565128 | 1.5289121782877741 | 0.1331008853802319 | 0.47910660285728646 | 0.0682 | 0.33160162018624123 | 0.1058760855053573 | 1.3255157215079496 | 1.3688004851918063 | 12.12555584215913 | 19.801842238501486 | 1.9254463546374438 | 280.71089678234097 | 0.048572616840444525 | 0.06622506150063852 | 0.042017509132913015 | 0.7704946740114171 | 0.1159786565805555 | 0.30537677843928696 | 0.3053767784392869 | 0.07007849124700442 |
| Auto Parts | 780 | 0.0755517447495962 | 0.05268548423262653 | 0.07937770430239609 | 0.2258550600098475 | 1.1857071522127585 | 1.2988008165300675 | 0.11996152662386686 | 0.36388827016804043 | 0.0657 | 0.2642591476315824 | 0.10124376933200797 | 2.0899721697370044 | 0.7374554607482262 | 7.242658481761152 | 13.350115616373527 | 1.299794235311194 | 44.145380578058656 | 0.11844074988072356 | 0.051831986762537516 | 0.03207403889156836 | 0.9097762307041399 | 0.07210859882854923 | 0.420032853223694 | 0.420032853223694 | 0.05619911634898599 |
| Bank (Money Center) | 621 | 0.13966549019607843 | NA | NA | 0.19221418038942642 | 0.3878457299023172 | 0.7970332484692695 | 0.09131059848759529 | 0.23784037636515615 | 0.0612 | 0.7260594506571556 | 0.05824204765124272 | 0 | NA | NA | NA | 0.9035318100897214 | 15.369409408303067 | NA | NA | NA | NA | 0.11993770657008117 | 0.3829230402791724 | 0.38292304027917234 | NA |
| Banks (Regional) | 849 | 0.07051658402203857 | NA | NA | 0.1906673120451636 | 0.3258114737086947 | 0.5570410856784398 | 0.07760704599223892 | 0.27469873140890805 | 0.0612 | 0.6935380678985263 | 0.055523624610549965 | 0 | NA | NA | NA | 0.7802285980334723 | 16.319062069258603 | NA | NA | NA | NA | 0.0759558097766404 | 0.3989672179876748 | 0.39896721798767487 | NA |
| Beverage (Alcoholic) | 216 | 0.08466418994413406 | 0.22475441046323 | 0.15898286131530992 | 0.249070921933466 | 0.7823142345759401 | 0.863513239856649 | 0.09510660599581466 | 0.3215969919679286 | 0.0657 | 0.19010886786225525 | 0.08636613293188058 | 0.8483484379616044 | 2.9382465622400087 | 10.864403573135078 | 12.947360370099922 | 2.3889454445917453 | 37.11917758108955 | 0.10033319989160408 | 0.049327755412571755 | 0.014771796284374744 | 0.14851681898506583 | 0.12953690994733089 | 0.5855987152395606 | 0.5855987152395606 | 0.22401121282496458 |
| Beverage (Soft) | 101 | 0.07284174603174602 | 0.17273825570109677 | 0.26466406261132963 | 0.21237668954286396 | 0.5241587026085254 | 0.5726263697379518 | 0.07849696571203704 | 0.34852094064678985 | 0.0657 | 0.15617531459487424 | 0.07391064244390748 | 1.7731795673077668 | 3.373147103839262 | 15.971324202788859 | 19.414654477752674 | 6.063945382915313 | 27.394975805455502 | -0.06627915354555267 | 0.0554615216199334 | 0.034472421066757616 | 0.32446840970412993 | 0.2634297115325893 | 0.6447133405942478 | 0.6447133405942478 | 0.17363889123785076 |
| Broadcasting | 126 | 0.015663523809523815 | 0.10026649034327256 | 0.09118766396956975 | 0.24870391104560474 | 0.6993806615357511 | 1.0043908188810557 | 0.10315071575810827 | 0.39297438939225027 | 0.0657 | 0.45516247895507844 | 0.07856272223346036 | 1.0683894088183026 | 1.195970558927447 | 7.433634052954371 | 11.248085810490112 | 0.86208534748094 | 81.55491545622783 | 0.14311964500119906 | 0.033601495740461944 | -0.009709643177491172 | 1.4386473146249832 | -0.017943670483959652 | 0.006020596913157564 | 0.006020596913157594 | 0.10006439131743146 |
| Brokerage & Investment Banking | 606 | 0.19713917721518975 | NA | NA | 0.19425314029367832 | 0.40657974968199745 | 0.9085137997254473 | 0.09767613796432303 | 0.3888889230372778 | 0.0657 | 0.6840020842845964 | 0.06447079305371727 | 0 | NA | NA | NA | 1.4657788628543078 | 101.58408036324856 | NA | NA | NA | NA | 0.08857741865491958 | 0.5211426415210836 | 0.5211426415210836 | NA |
| Building Materials | 462 | 0.047801337047353745 | 0.10550739754850814 | 0.15629327131409368 | 0.22959364703573754 | 0.9350007143209421 | 1.026465291452767 | 0.104411168141953 | 0.31754053539247207 | 0.0657 | 0.17989724912380414 | 0.09446632081759979 | 1.9021251075734757 | 1.7897276422263575 | 11.907869725109522 | 16.651118535377062 | 2.699566318943797 | 30.110179863252046 | 0.1697084197726317 | 0.04376842028037473 | 0.06658985193129285 | 0.7908258650170241 | 0.13491464933049338 | 0.35065128367847975 | 0.35065128367847975 | 0.10782324738340433 |
| Business & Consumer Services | 974 | 0.07707627421758571 | 0.09782001262025221 | 0.21417691014080062 | 0.2313474456877 | 0.9464981920403315 | 1.015539693366137 | 0.10378731649120641 | 0.3882079654892777 | 0.0657 | 0.14718679969998058 | 0.09574254870260464 | 2.798586592052117 | 2.23415846039558 | 15.979569702346412 | 22.03324091886064 | 4.726306782097976 | 50.16027132363976 | 0.11117210612160035 | 0.02553366038165102 | 0.005623853132169171 | 0.15404640571695835 | 0.15996585353877668 | 0.4692857395395101 | 0.46928573953951 | 0.09940853263234993 |
| Cable TV | 45 | 0.041268780487804885 | 0.17152961199324118 | 0.12395246866735661 | 0.25041302283655165 | 0.5924148760482556 | 1.0687515972057318 | 0.10682571620044728 | 0.38950232042602995 | 0.0657 | 0.5361764713513466 | 0.07589087731717956 | 0.8254008116150726 | 2.3017811696776587 | 7.277108228464824 | 13.502588554663282 | 1.4440953280626694 | 63.46161450340903 | 0.02333817089107924 | 0.12840740382377908 | -0.0038141169095833056 | 0.046504520896977826 | 0.11186832855618259 | 0.3866046296201087 | 0.38660462962010866 | 0.16884225115837503 |
| Chemical (Basic) | 897 | 0.07855856940509917 | 0.043643418482694665 | 0.04211770219853005 | 0.19032896528430887 | 0.9059036350600613 | 1.1492820149889402 | 0.1114240030558685 | 0.34088887374809757 | 0.0657 | 0.3553919782186683 | 0.0892853775589936 | 1.1559379942651005 | 1.1972259407228243 | 10.877089343936419 | 25.707501671760706 | 1.21261882745677 | 58.86034971850286 | 0.12904778151210078 | 0.0912596450828845 | 0.05736830214870226 | 0.9781431058356577 | 0.030176306306210342 | 1.6512525361502586 | 1.6512525361502586 | 0.044803981992907076 |
| Chemical (Diversified) | 64 | 0.06524965517241378 | 0.05433113453313254 | 0.047486814943558296 | 0.31321076583748 | 0.8411297915277633 | 1.1400490925634852 | 0.11089680318537501 | 0.28122766558418827 | 0.0612 | 0.39462038216250384 | 0.08519460818476692 | 1.1517164786342886 | 1.008635885119825 | 8.419175610610855 | 17.4638224450494 | 1.1109210276463266 | 29.17400284822903 | 0.19455144732873944 | 0.08139884706744789 | 0.037391688830966364 | 0.876094324062263 | 0.016669653664093967 | 2.91800997226874 | 2.91800997226874 | 0.05571765473258092 |
| Chemical (Specialty) | 951 | 0.08490807635829667 | 0.10567135821074822 | 0.0962744977475017 | 0.2302263226325249 | 0.9490060613608508 | 1.0488139972344594 | 0.10568727924208762 | 0.3728389893824859 | 0.0657 | 0.19388773722892033 | 0.0947216055343742 | 1.1280818260629875 | 2.2179806855203226 | 12.545314456391363 | 20.102124642214093 | 2.133892680679617 | 42.71396167385844 | 0.18536199182641627 | 0.09045717953537039 | 0.049438736103891566 | 0.628467071190249 | 0.0745476913837322 | 0.6725754191183008 | 0.6725754191183008 | 0.10690822933918473 |
| Coal & Related Energy | 216 | 0.07463082568807337 | 0.20749330061841298 | 0.24085864121433487 | 0.21027079935349902 | 1.243741763005687 | 1.196210664496575 | 0.11410362894275444 | 0.5561230830367363 | 0.0682 | 0.16049759891512955 | 0.10397564159470712 | 1.3211596897978948 | 1.6107026774646396 | 5.3519535082121825 | 7.383142622596054 | 1.5023583544911636 | 38.39765112908485 | -0.027227901279599405 | 0.11453327004675845 | 0.06904727980142891 | 0.6377768936209977 | 0.17139697152965847 | 0.7985503298587916 | 0.7985503298587916 | 0.20788174483635727 |
| Computer Services | 1182 | 0.09158469104665821 | 0.07176513248621288 | 0.20377160576210954 | 0.22494048259484503 | 1.047759546162209 | 1.09258003723948 | 0.1081863201263743 | 0.3945424528093295 | 0.0657 | 0.12910175825900239 | 0.10056210474856167 | 3.8438543424357055 | 1.5137031692330656 | 15.245954362476072 | 20.35127542737932 | 4.02096966323875 | 59.67930916295105 | 0.15935117887976563 | 0.015571470094428969 | 0.018251439665462266 | 0.3269483288175687 | 0.1444388114563661 | 0.5565590976688113 | 0.5565590976688113 | 0.07327265681195216 |
| Computers/Peripherals | 342 | 0.034963609022556415 | 0.1306287413941654 | 0.20415937267651255 | 0.19680016648684778 | 1.2452856029038846 | 1.26185646056331 | 0.117852003898165 | 0.41480392467646005 | 0.0657 | 0.061860212296684716 | 0.11360087460326858 | 2.4658781226112927 | 3.3510269146523033 | 19.044383449948704 | 25.458165307974447 | 7.576169353743152 | 92.11097730140658 | 0.0297718030280104 | 0.048325901214352485 | 0.03619219738413128 | 0.34307128387551117 | 0.2640323130303963 | 0.2542750995466337 | 0.25427509954663363 | 0.13536126174578905 |
| Construction Supplies | 804 | 0.09304889763779531 | 0.09459114752576649 | 0.0972904990816261 | 0.23089860732564285 | 0.8467977037752572 | 0.9781792891945789 | 0.10165403741301045 | 0.3521565297169424 | 0.0657 | 0.2723704493170634 | 0.08734816703328924 | 1.299415119166942 | 1.4443804605364166 | 10.268126391930863 | 14.965943010321554 | 1.6552858516841096 | 69.54793621474097 | 0.16694497876572217 | 0.05215018349353288 | 0.0319584978533755 | 0.5418601669369973 | 0.1018600199160753 | 0.44686899740976965 | 0.4468689974097697 | 0.09637021234678882 |
| Diversified | 335 | 0.1245467041198502 | 0.1912668825995744 | 0.1305216540403019 | 0.1666769275061829 | 0.6955076338659182 | 0.888561948694207 | 0.09653688727043921 | 0.29019574720420455 | 0.0612 | 0.3345993493863077 | 0.07954876727840107 | 0.8099047766125886 | 1.959813502253223 | 8.39813072448559 | 10.126118827408375 | 1.138967259074129 | 23.62475657603454 | -0.10274984833872372 | 0.050695893854381356 | 0.02793250091127634 | 0.22130686642225372 | 0.15189767624625436 | 0.15552381391113076 | 0.1555238139111308 | 0.1912738724024415 |
| Drugs (Biotechnology) | 1223 | 0.2538742105263159 | 0.0017550043440366014 | 0.019137906017770365 | 0.1725664048431158 | 1.2281686132974015 | 1.2918900121586152 | 0.11956691969425692 | 0.7005011522421916 | 0.0745 | 0.1316878042854114 | 0.1111578870078751 | 0.8098585984792431 | 6.7442010984757115 | 15.972191315595955 | NA | 4.694724914520711 | 91.22924081809997 | 0.21363002889103208 | 0.0455853842530919 | 0.1884363873554751 | NA | -0.08221073332968983 | 0.0064958693706511465 | 0.006495869370651164 | 0.04641505744888885 |
| Drugs (Pharmaceutical) | 1271 | 0.12712799270073 | 0.2041832410112752 | 0.13663932508445867 | 0.16064147614048158 | 0.9744455501369576 | 1.0459900460346432 | 0.10552603162857813 | 0.4768068841155595 | 0.0682 | 0.14274968253928402 | 0.09774245221348435 | 1.0855796526615398 | 3.9470092833666963 | 13.408666143145313 | 18.824918010965483 | 3.7441871673985103 | 73.37428620641204 | 0.1677471206005622 | 0.05146301720590947 | 0.09814312779069889 | 0.643770672798444 | 0.12357116156594297 | 0.7262903568373973 | 0.7262903568373973 | 0.21726947442920141 |
| Education | 272 | 0.07004443113772454 | 0.1343360825901661 | 0.11595776073954202 | 0.20811150771496137 | 0.7837802085517217 | 0.8626890707188635 | 0.09505954593804711 | 0.42984198755760755 | 0.0657 | 0.225580289765356 | 0.08469884942348449 | 1.113273313686314 | 2.314609992405274 | 11.187385345832285 | 16.921324079239835 | 2.0558121302891568 | 50.52627944902218 | 0.05170675416540939 | 0.05587448905212795 | 0.023931514815740806 | 0.3957936490287724 | 0.06783923072268373 | 0.6360184008010564 | 0.6360184008010564 | 0.1315115079707806 |
| Electrical Equipment | 1101 | 0.10367485714285714 | 0.0729100535207483 | 0.1059167172061984 | 0.18997957183314162 | 1.1801425031628325 | 1.215668392683982 | 0.11521466522225537 | 0.43176608961512536 | 0.0657 | 0.1466570863500688 | 0.1055229482305994 | 1.8766458092541503 | 2.1500587989364 | 17.14381216121704 | 27.80277677785591 | 2.9876405679544003 | 47.215518793463666 | 0.23318262917278393 | 0.07118995015018294 | 0.06638132905392209 | 1.3156207360980665 | 0.0911746660830686 | 0.5524360897081295 | 0.5524360897081295 | 0.07570008997986713 |
| Electronics (Consumer & Office) | 125 | 0.021197961165048542 | 0.05800555637569238 | 0.10563964900091696 | 0.21689689306216253 | 1.1198908994583037 | 1.2099501889035962 | 0.11488815578639533 | 0.45184781142729097 | 0.0682 | 0.21344316858760534 | 0.10125165684240181 | 2.0670829469847414 | 0.9558152285018218 | 10.518161345684888 | 16.11710481739536 | 1.7815824953269306 | 33.498845812540615 | 0.049128228781795555 | 0.044635348037750384 | 0.050417669449723014 | 1.00459417915495 | 0.09315471675283989 | 0.26621712484707033 | 0.2662171248470704 | 0.07343094274369003 |
| Electronics (General) | 1480 | 0.058368749999999955 | 0.05847756642278254 | 0.07756998876499577 | 0.16900845025701186 | 1.3619377589137938 | 1.376789570828448 | 0.12441468449430437 | 0.4193173808966851 | 0.0657 | 0.1489011520554098 | 0.11320477673550434 | 1.721452209725421 | 1.6413704225339114 | 13.89883400396274 | 26.487674851947386 | 2.309980011730418 | 70.86083442086094 | 0.19103082751396167 | 0.05911667968245431 | 0.03524292614835784 | 0.8048039988896056 | 0.07954209984384333 | 0.5268290378145564 | 0.5268290378145564 | 0.06168009081797421 |
| Engineering/Construction | 1327 | 0.0677850628930817 | 0.048119137923535574 | 0.07784889611248046 | 0.22533742620492453 | 0.6631340537552841 | 0.9287986474120591 | 0.09883440276722857 | 0.3703988832542879 | 0.0657 | 0.4847341107984981 | 0.07474120626677658 | 2.1204934498710473 | 0.6929373488594868 | 9.945024601486805 | 13.87488635539866 | 1.079329524157367 | 40.07337397461095 | 0.15915697069730544 | 0.10185507267633107 | 0.09247243895802869 | 1.6076085598549554 | 0.09466668705089495 | 0.6836228176176073 | 0.6836228176176073 | 0.04866593065346499 |
| Entertainment | 748 | 0.09067304904051174 | 0.09237732892705441 | 0.09652074087312353 | 0.21491862789103236 | 0.9946761025633484 | 1.0554392738374743 | 0.10606558253611978 | 0.47466301980519926 | 0.0682 | 0.15039781096904528 | 0.09778383344703964 | 1.3248974637190056 | 3.397357563023296 | 10.018113981196533 | 35.037371694133945 | 3.1483119784955673 | 75.60502347832771 | 0.025583647390353237 | 0.1437970196121046 | 0.07789571215418195 | 28.10735793704604 | 0.015830256978802845 | 1.5537993739780185 | 1.5537993739780185 | 0.09356457567164092 |
| Environmental & Waste Services | 391 | 0.0867159722222222 | 0.11387736489673332 | 0.11120965355361774 | 0.2189507683911178 | 0.8559508193936919 | 1.0297058112156112 | 0.1045962018204114 | 0.42938191566121314 | 0.0657 | 0.2558756871351501 | 0.0904038670196528 | 1.1393893248941391 | 2.7574506520977793 | 13.975562127508603 | 23.293637829550324 | 3.011918854583545 | 44.10085849980927 | 0.16827458844233123 | 0.08663158766212009 | 0.05977943230506238 | 1.000549081862317 | 0.0995503209549674 | 0.4888710248687173 | 0.48887102486871736 | 0.11487977472409466 |
| Farming/Agriculture | 429 | 0.10853714285714278 | 0.06759782258183901 | 0.07513685742168924 | 0.20940564970482062 | 0.5575241353500908 | 0.7735453815409571 | 0.08996944128598865 | 0.3723630247762325 | 0.0657 | 0.39044782434722086 | 0.0740239498943175 | 1.3429171541514722 | 1.1025697181373753 | 11.010459556981896 | 15.6992425108689 | 1.6010274631657162 | 207.49711514436956 | 0.1735387900254468 | 0.04474690472046362 | 0.029266162724058364 | 0.4317750383078226 | 0.1214179778158247 | 0.3724624770787258 | 0.3724624770787258 | 0.06898207746463805 |
| Financial Svcs. (Non-bank & Insurance) | 1117 | 0.15429169191919181 | NA | NA | 0.17474488044171121 | 0.27307489021810905 | 0.8208564761626547 | 0.09267090478888758 | 0.40822234595011475 | 0.0657 | 0.7474050998122198 | 0.06012855430558061 | 0 | NA | 46.49336057762887 | 59.411574439410536 | 2.3699459395108122 | 73.38192818687733 | NA | NA | NA | NA | 0.2007772241112249 | 0.20913029006425635 | 0.20913029006425632 | NA |
| Food Processing | 1424 | 0.0886347655502392 | 0.08446738554652544 | 0.12288224100938813 | 0.22148943024213846 | 0.5739152609745028 | 0.6812356108037589 | 0.08469855337689464 | 0.32702488022790016 | 0.0657 | 0.26551510426144387 | 0.07525468735554769 | 1.7566913458225955 | 1.301417203785907 | 10.759608452938423 | 15.155316867147562 | 2.0450972747782026 | 38.646736231744654 | 0.10267806314266137 | 0.0434206963089129 | 0.025182532696515107 | 0.3879261050043912 | 0.11468592374483505 | 0.602223215216532 | 0.602223215216532 | 0.08503758490110712 |
| Food Wholesalers | 188 | 0.10498807407407403 | 0.025910812651305338 | 0.11568187281193071 | 0.2218641335934656 | 0.44056581692882124 | 0.5985481152537028 | 0.07997709738098643 | 0.36762294661109274 | 0.0657 | 0.3692662514740203 | 0.06858647522473119 | 5.39258180680121 | 0.4160858136885029 | 10.39348774075683 | 15.92968702038703 | 2.05295409132877 | 45.13485060151118 | 0.06547689620104731 | 0.011412606456288341 | 0.009696862945077843 | 0.9289757324516321 | 0.11576016004286808 | 0.40988709749757013 | 0.40988709749757013 | 0.025783349498618283 |
| Furn/Home Furnishings | 380 | 0.05024189285714278 | 0.07361882708215475 | 0.1380676274530838 | 0.17581133155931547 | 0.951334627649579 | 0.9361040517808141 | 0.09925154135668449 | 0.35335197113155625 | 0.0657 | 0.19864980056980275 | 0.08929499854083625 | 2.53920509698485 | 1.0822094988657878 | 10.231658597772654 | 14.106460925913412 | 2.0734336899003707 | 35.63091978092736 | 0.03189906904374622 | 0.03218118579732652 | 0.015116134251715823 | -0.22974118520506204 | 0.13459586762813505 | 0.6174691986516684 | 0.6174691986516684 | 0.07639137155405705 |
| Green & Renewable Energy | 260 | 0.12277534591194965 | 0.30365434678921766 | 0.06292648559233405 | 0.2030095227155928 | 0.5963118858484414 | 0.8859790820218285 | 0.09638940558344641 | 0.3816488811114374 | 0.0657 | 0.42171118317258166 | 0.07645977972596257 | 0.2355864530183031 | 6.989131721305897 | 13.697589576827577 | 22.890412127309926 | 1.7709188169336842 | 41.036665765995295 | 0.09646008525377874 | 0.5113710987724096 | 0.27548673955186526 | 1.2755393760527536 | 0.0768891075255072 | 0.8946657617226894 | 0.8946657617226894 | 0.3027870000297326 |
| Healthcare Products | 850 | 0.13721645472061658 | 0.13832356020472056 | 0.1218233026244545 | 0.17241350822608986 | 1.0816981151098504 | 1.1457756246639703 | 0.11122378816831271 | 0.49084979637043874 | 0.0682 | 0.12459018106802841 | 0.1037204905122128 | 1.1765513584055438 | 4.388803105975948 | 19.377323312465347 | 30.31685618933484 | 3.521970817747559 | 67.93954673552811 | 0.27893792598004885 | 0.054383620154039844 | 0.04164991859697952 | 0.5380481952774577 | 0.07810632071550389 | 0.5106156827590972 | 0.5106156827590972 | 0.14275881397717696 |
| Healthcare Support Services | 480 | 0.1349915570934257 | 0.035089065418329506 | 0.23334053461573592 | 0.23951022022842386 | 0.7317595094588942 | 0.8683207919134942 | 0.09538111721826051 | 0.4113975379400226 | 0.0657 | 0.2797187430613118 | 0.08244394151540908 | 8.17248928240306 | 0.5485601445540983 | 10.837305629682863 | 15.603649398440352 | 2.3248576628802273 | 73.03451834567375 | -0.03446419428460827 | 0.007741839105446776 | 0.007160783221830502 | 0.45876009446127347 | 0.09422788546682755 | 0.4655588373735928 | 0.4655588373735928 | 0.03464149122791732 |
| Heathcare Information and Technology | 435 | 0.13021968127490038 | 0.12799840863570688 | 0.11111500595339449 | 0.17487821027373782 | 1.132253717064354 | 1.2059921327413936 | 0.11466215077953357 | 0.5267125928105998 | 0.0682 | 0.12344132624849466 | 0.10680360551782325 | 1.1152274195001748 | 5.117858045506105 | 21.5588041455903 | 38.09825603802337 | 3.667453398398297 | 146.24483142937692 | 0.2442834334317575 | 0.06663516662349238 | 0.06446813924673489 | 0.5853009440373665 | 0.043618944508061926 | 0.33030864379188873 | 0.33030864379188873 | 0.12991518646922223 |
| Homebuilding | 165 | 0.05990234848484852 | 0.12393975964590233 | 0.1361031622471103 | 0.2382270524736707 | 0.9495758670695034 | 1.0677356476037183 | 0.10676770547817231 | 0.3342135660466185 | 0.0657 | 0.25804280316384937 | 0.09189482908834183 | 1.4026520779873481 | 1.1458028565386256 | 8.314655336912486 | 9.463226781099026 | 1.4237005303027135 | 17.25137253653105 | 0.6626853866537605 | 0.00578969216892311 | 0.005496074685259385 | 0.48593342951853447 | 0.1526433322485836 | 0.17225114219829524 | 0.1722511421982953 | 0.11997238739126523 |
| Hospitals/Healthcare Facilities | 245 | 0.1010432515337423 | 0.1130258173060321 | 0.1287428129243988 | 0.19476987168278334 | 0.5880920206585584 | 0.7736783334954127 | 0.08997703284258807 | 0.3442232907867701 | 0.0657 | 0.33381945480346914 | 0.07634165216568513 | 1.4074174666695256 | 1.9890356888551743 | 11.947380885526506 | 17.878504321618458 | 3.2272819963627066 | 51.42046469635571 | 0.05343224904591918 | 0.06769506740156436 | 0.03631982036976909 | 0.5232031838541817 | 0.2537801194488341 | 0.33409824897174106 | 0.334098248971741 | 0.11056840824888346 |
| Hotel/Gaming | 660 | 0.07520172744721694 | 0.15571477839598694 | 0.10909506308719386 | 0.1747017186024152 | 0.7423154544956462 | 0.9130526779150158 | 0.09793530790894739 | 0.3703974371162 | 0.0657 | 0.29801697871686506 | 0.08339063458838678 | 0.9271596250718696 | 3.3799125612463863 | 14.079987190558994 | 23.51851005685243 | 4.516436994551129 | 53.997068577157464 | -0.016755297209510932 | 0.06716390170745104 | 0.011232514421773726 | 0.14794105203092242 | 0.14828396167408225 | 0.3099942377603527 | 0.3099942377603526 | 0.1415379940292289 |
| Household Products | 554 | 0.06572973190348526 | 0.1602174235186326 | 0.22277651316453786 | 0.2404778273409792 | 0.827584516939807 | 0.8799543472237394 | 0.09604539322647551 | 0.39284610486733684 | 0.0657 | 0.1237449627466964 | 0.09023990656210155 | 1.761434215021396 | 3.033196912289804 | 15.31120597913071 | 18.692511149399856 | 4.695640453550533 | 67.36377870567239 | 0.058834030995191605 | 0.034708927475133676 | 0.024621545246325278 | 0.23145141603777733 | 0.17827338579111895 | 0.7012348868026012 | 0.7012348868026012 | 0.16119326947087548 |
| Information Services | 85 | 0.06631736842105262 | 0.1104412456289791 | 0.21256133010877326 | 0.23667823985110378 | 0.9461858149674477 | 1.1245610499517515 | 0.11001243595224502 | 0.4122886386795369 | 0.0657 | 0.25438748341972206 | 0.09452482330413338 | 2.5968899920630952 | 1.9465266072689704 | 11.286514405100725 | 16.835615265579136 | 3.1330702066977385 | 47.863780258628985 | 0.16890946785103858 | 0.020278829661343024 | 0.0450937371200375 | 0.601521563701527 | 0.13730676677374132 | 0.37477605380667883 | 0.3747760538066789 | 0.11434607310740295 |
| Insurance (General) | 199 | 0.1022633540372671 | 0.1450249863366485 | 0.22284268214086758 | 0.2126328634371507 | 0.5339135196684894 | 0.5745120018721774 | 0.07860463530690133 | 0.3007847416073076 | 0.0657 | 0.23821384546215085 | 0.07158347866521879 | 1.8452373630409193 | 1.3098108224415517 | 7.761539710357843 | 7.937211693949075 | 1.8832308583242523 | 23.78237417655259 | 0.11397206981003143 | 0.007333216232256841 | 0.02218875172675276 | 0.0495832791702887 | 0.14580483534717362 | 0.451685279800353 | 0.451685279800353 | 0.14517319228042763 |
| Insurance (Life) | 137 | 0.06776583333333334 | 0.1323906892596889 | 0.11188409574679048 | 0.17516897912997553 | 0.8366648433165084 | 0.941598944837215 | 0.09956529975020498 | 0.291910176346379 | 0.0612 | 0.4964050638626039 | 0.07285873722270024 | 1.0049548349312696 | 1.1648377995828094 | 7.87577449768657 | 8.210704074127591 | 1.1391819987430885 | 54.92068535625781 | -1.001350550937412 | 0.006360957102223615 | 0.00780177234258859 | -0.05672677291835923 | 0.12029518289031958 | 0.4080877759483987 | 0.40808777594839873 | 0.13250955227861244 |
| Insurance (Prop/Cas.) | 240 | 0.11804827411167505 | 0.1472800687770428 | 0.2049680044948979 | 0.1757133229465237 | 0.47753753007082456 | 0.498548660992902 | 0.07426712854269471 | 0.2960167732719298 | 0.0612 | 0.14412767676679425 | 0.07015923485889122 | 1.6841376149261809 | 1.2631238543860641 | 7.966622953668649 | 8.53178848333957 | 1.702045053071061 | 17.683477325569502 | -0.2753750414904087 | 0.006988874140907462 | 0.0022022869312401535 | 0.01743328437789124 | 0.1998132179259425 | 0.2229419671107289 | 0.2229419671107289 | 0.14756512604875174 |
| Investments & Asset Management | 1291 | 0.14752180357142863 | 0.187998113367846 | 0.06286342760445107 | 0.1683613810326697 | 0.5751603220865722 | 0.7670268111942766 | 0.0895972309191932 | 0.3758031166548576 | 0.0657 | 0.38145630617884313 | 0.07416092596137233 | 0.3662145282301179 | 5.1390496197574 | 19.776535857034077 | 21.922168532184187 | 1.6370771000274509 | 46.24203162928689 | NA | 0.04041935793440722 | 0.04743447981151396 | 0.38395888903852277 | 0.10266771326817513 | 0.5343336684877689 | 0.5343336684877689 | 0.18660042820908357 |
| Machinery | 1548 | 0.06557624783362219 | 0.10246595144206258 | 0.1287927559074887 | 0.21773331936373322 | 1.1230406760043468 | 1.1576883260119293 | 0.11190400341528117 | 0.37357026284951733 | 0.0657 | 0.1350005834663423 | 0.10342953842796844 | 1.6428307320616382 | 2.0885541427672822 | 13.952773356683227 | 19.45620670699655 | 2.7643975780752923 | 79.07882170944231 | 0.2859034765943716 | 0.04118657904986903 | 0.03932809856546194 | 0.6571645295914001 | 0.11487605886746285 | 0.4463402639749103 | 0.44634026397491033 | 0.10466244081141049 |
| Metals & Mining | 1832 | 0.22555768442622956 | 0.1094090172100248 | 0.15028461661979697 | 0.3061832883365534 | 1.0067152939696256 | 1.1212472099030004 | 0.10982321568546133 | 0.6955492640839968 | 0.0745 | 0.23391739719832377 | 0.09716545042742362 | 1.451332582140876 | 1.2222894523844456 | 7.021168829829218 | 10.577326797748654 | 1.6658670310855495 | 64.70400774712483 | 0.12476590159998122 | 0.08356917836582853 | 0.04780990022511663 | 0.7129551141130064 | 0.08606105756405125 | 0.796459082151292 | 0.796459082151292 | 0.11009706683729671 |
| Office Equipment & Services | 140 | 0.050200416666666664 | 0.0735820632382038 | 0.12805012241363092 | 0.2334915098335708 | 0.7267324854020321 | 0.760108409459641 | 0.0892021901801455 | 0.3555086597763081 | 0.0657 | 0.21923460408682288 | 0.0804170802790273 | 2.1812277740154595 | 1.0044524807823128 | 8.827084955778323 | 13.16903998629038 | 1.802655892462207 | 133.87204494827162 | 0.13156634716952909 | 0.026356483004655675 | 0.007258331975358016 | 0.04364067057892862 | 0.08199196601755371 | 0.6015066536921426 | 0.6015066536921426 | 0.07557513266953912 |
| Oil/Gas (Integrated) | 36 | 0.07216314285714287 | 0.14913790374495575 | 0.16942432319584688 | 0.42409460137349425 | 0.8705119047647804 | 0.9316777107029921 | 0.09899879728114085 | 0.3037060199174906 | 0.0657 | 0.1671788898395993 | 0.09066186401633301 | 1.5340470392934398 | 1.232030082877976 | 5.755024883216643 | 8.229320828665447 | 1.7561517688182717 | 11.847866338187274 | 0.02330915199676819 | 0.08282085640915483 | 0.015681400322980307 | 0.09817507009166661 | 0.14992924499222218 | 0.7821731682452366 | 0.7821731682452366 | 0.1498611037445995 |
| Oil/Gas (Production and Exploration) | 548 | 0.15812938709677413 | 0.31594019100097365 | 0.182499556775622 | 0.3274721313844728 | 0.8938719628830606 | 1.0156805607417236 | 0.10379536001835242 | 0.5037976772748156 | 0.0682 | 0.22437288709513967 | 0.0919495036908919 | 0.6400592252236873 | 2.549433106158156 | 4.5585159475016965 | 7.869435810582128 | 1.4319196086027774 | 17.9623401139556 | 0.00595985852421627 | 0.3144250310158541 | 0.1443228919197149 | 0.5916293360157628 | 0.15066651084632068 | 0.44928168898043747 | 0.4492816889804374 | 0.3185547419618592 |
| Oil/Gas Distribution | 179 | 0.09019410447761192 | 0.17409116789879855 | 0.10213474768823065 | 0.1651901679962025 | 0.47137829737850173 | 0.672133432376452 | 0.0841788189886954 | 0.3150068945407914 | 0.0657 | 0.3869701056489716 | 0.07061615180801686 | 0.6647014298320117 | 2.910005633686923 | 11.347357731814801 | 16.22649339563943 | 2.038517779472103 | 24.232799172879478 | 0.06532928237748997 | 0.14358433840334278 | 0.1240093479658206 | 0.8398036753766988 | 0.16128448737467838 | 0.6974769859703234 | 0.6974769859703234 | 0.1753633251969385 |
| Oilfield Svcs/Equip. | 437 | 0.07497964809384165 | 0.04870039882881739 | 0.10190717522939738 | 0.23041430225670032 | 0.7691461508463383 | 0.952999839867837 | 0.10021629085645349 | 0.40800244927459106 | 0.0657 | 0.3223037966730864 | 0.08375113361521942 | 2.4092616300678835 | 0.6096048596238653 | 7.580235518358163 | 12.034566811785607 | 1.301592544900414 | 38.63384348256543 | 0.0627112568811023 | 0.041870931609964766 | 0.022181706438933448 | 0.4371964659170376 | 0.09628431334865412 | 0.512204592925453 | 0.512204592925453 | 0.04970367805212622 |
| Packaging & Container | 438 | 0.05407319402985073 | 0.08236451753518798 | 0.10687018671898328 | 0.22615723883544117 | 0.6111062559848243 | 0.7788018325751739 | 0.09026958464004242 | 0.3308379531302539 | 0.0657 | 0.32394015773860135 | 0.0769429701149191 | 1.5613159703303021 | 1.4527002195861074 | 10.066296705708428 | 17.200550439305598 | 1.9039652615763276 | 368.70254755029885 | 0.15444680287895513 | 0.06328556353999056 | 0.02940152525481447 | 0.3922916674448261 | 0.11623958944351027 | 0.5069985689113533 | 0.5069985689113533 | 0.08369156687325101 |
| Paper/Forest Products | 269 | 0.03171213636363637 | 0.06987799539209932 | 0.05272866685558862 | 0.20538045297098367 | 0.5869170186693181 | 0.8664084913107887 | 0.09527192485384603 | 0.3431638315376204 | 0.0657 | 0.4510229955123151 | 0.07446106315813819 | 0.8733283412611578 | 1.2574426720984482 | 9.390507281629812 | 17.422383534388768 | 0.8391340044508875 | 564.6642050149882 | 0.23127248565986247 | 0.100163451218125 | 0.06456055436497996 | 1.1950005445747607 | 0.03873481201204777 | 0.8928724648508355 | 0.8928724648508355 | 0.07074321381274189 |
| Power | 492 | 0.09470596153846161 | 0.14046122994065985 | 0.07050906109597382 | 0.22193021233481208 | 0.4266485225974891 | 0.7029482497612936 | 0.08593834506136985 | 0.2851559907405637 | 0.0612 | 0.49461605837835343 | 0.06606814153702262 | 0.6083593392909591 | 2.2428031241496234 | 9.52122498089377 | 15.89437334936098 | 1.3092156724559636 | 23.937128067272884 | 0.04889477797980726 | 0.18962666985428472 | 0.11282124652140116 | 1.0749431149609059 | 0.10420386209633929 | 0.5945260466001989 | 0.5945260466001989 | 0.1404434071462865 |
| Precious Metals | 823 | 0.23166027322404364 | 0.1267878215363298 | 0.10269894013168175 | 0.27555218036402884 | 1.1122272531127146 | 1.1733808838398774 | 0.112800048467257 | 0.7078952403894263 | 0.0745 | 0.15751587434249664 | 0.10380763283414328 | 0.8527895141853166 | 2.3138332837840294 | 8.191244378046427 | 16.961329808372106 | 1.6595540828753375 | 43.668297531113026 | 0.1045200496032405 | 0.18342540915819863 | 0.08691699560346858 | 1.1399813900044753 | 0.03301130425407585 | 1.5292432877623996 | 1.5292432877623996 | 0.12719775590183677 |
| Publishing & Newspapers | 321 | 0.012444810606060619 | 0.07554716472672487 | 0.10343449946067172 | 0.1818283700421587 | 0.8404531985008978 | 0.8338346370959802 | 0.09341195777818047 | 0.37553461134817656 | 0.0657 | 0.17225527053311818 | 0.08578423639878832 | 1.6459546584453943 | 1.3284966418875108 | 10.162094800454826 | 16.33410413148988 | 1.611467319885355 | 40.61420519164698 | 0.08415100551889458 | 0.0361724151369375 | 0.0026847916843477787 | 0.06237126560109434 | 0.08810239588654906 | 0.6645051008166462 | 0.6645051008166462 | 0.07660190460993758 |
| R.E.I.T. | 650 | 0.08566818548387094 | 0.31117064377034764 | 0.03460415465330588 | 0.03301692565825981 | 0.49452464538210045 | 0.7873467984882381 | 0.0907575021936784 | 0.25184912324488745 | 0.0612 | 0.45710454740859624 | 0.07019138939929383 | 0.12057399553090244 | 10.96376962247573 | 20.05881850007929 | 33.079933689832885 | 1.45614324862315 | 36.793980326828695 | 1.069664429672774 | 0.04734848211351085 | -0.06985823211671999 | -0.23265421518672788 | 0.03518749162884923 | 1.998598139485014 | 1.998598139485014 | 0.2934329893867503 |
| Real Estate (Development) | 879 | 0.05772051209103836 | 0.05513288161783046 | 0.021146449116557203 | 0.2968212668744724 | 0.4321952750030903 | 0.9372138252501093 | 0.09931490942178124 | 0.41235401305466174 | 0.0657 | 0.6742720749004402 | 0.0654769365824206 | 0.45314505601031874 | 1.8901276128687499 | 14.910613926783386 | 24.783043140230752 | 0.4900218720041644 | 53.27971578094697 | 3.245641632996061 | 0.03077430220513581 | 0.020828016741098767 | -3.670446296951757 | -0.017116229122804562 | 0.0070901179081967166 | 0.007090117908196691 | 0.0548810512167145 |
| Real Estate (General/Diversified) | 309 | 0.07175267441860465 | 0.14863328964235034 | 0.03542870514679378 | 0.2725157764203402 | 0.5277516629535361 | 0.9453524190708004 | 0.0997796231289427 | 0.3176306571722835 | 0.0657 | 0.5546362818921262 | 0.07168775961015815 | 0.26993760898108565 | 3.4523419558692625 | 13.785148217782979 | 20.446975972530712 | 0.716367272664805 | 29.2542097458327 | 1.2231403828503178 | 0.08681382014953509 | 0.071181742296746 | 1.172685699963017 | 0.028230967320701322 | 0.8970300032365812 | 0.8970300032365812 | 0.15464921545883958 |
| Real Estate (Operations & Services) | 749 | 0.07427590994371487 | 0.17510345882073594 | 0.04144747040045901 | 0.21824282806506626 | 0.5603549860848621 | 0.881998397612396 | 0.0961621085036678 | 0.35968379636045256 | 0.0657 | 0.4778542445911017 | 0.0736878356360734 | 0.26402837363555315 | 3.9947941196473966 | 16.687504936509356 | 20.40580240199837 | 0.8964444972275748 | 94.64720267040038 | 0.22078779853759253 | 0.022938933571137618 | 0.030877327544336957 | 0.2948218030859899 | -0.0004276127115410209 | 0.009063149645655473 | 0.009063149645655466 | 0.17939982235728005 |
| Recreation | 320 | 0.049946122448979606 | 0.10483252540858064 | 0.09828012461097044 | 0.24470492031754193 | 0.9484442886385445 | 1.0667202545900192 | 0.1067097265370901 | 0.3660347727883388 | 0.0657 | 0.24249789964099594 | 0.09274687533897666 | 1.2590547993679317 | 2.0170035035455416 | 11.386961680012252 | 19.432345858948352 | 2.522150411867047 | 78.6687475906874 | 0.15389722616578982 | 0.06279515739288019 | 0.03203300430426912 | 0.288810018290435 | 0.07825262786617852 | 0.5833095006590824 | 0.5833095006590824 | 0.0992410245346695 |
| Reinsurance | 33 | 0.060185000000000016 | 0.12739255796707408 | 0.20241035747384928 | 0.1319751636706322 | 1.2009096051209383 | 1.1953705432106245 | 0.11405565801732667 | 0.3140790807598063 | 0.0657 | 0.20135742519601033 | 0.10098248731421666 | 1.8532614712467494 | 0.9121997194300304 | 9.853351280211657 | 7.161561197527308 | 1.2423818744268456 | 7.533238512888166 | -0.6464235376069414 | 0.001082445077598424 | 0.005436687489382434 | 0.11098441622112191 | 0.1995703246338004 | 0.2566759305399446 | 0.25667593053994464 | 0.12734499906420016 |
| Restaurant/Dining | 401 | 0.03456134482758625 | 0.10403299523950783 | 0.14980478064662475 | 0.1896342847213431 | 0.8135516955790292 | 0.9244926369893237 | 0.09858852957209038 | 0.33700973355544106 | 0.0657 | 0.1911842056182664 | 0.08913292782953733 | 1.9164377799332746 | 2.7726225397663167 | 17.094692016883652 | 27.637934106200042 | 10.085725547891842 | 125.5940324072094 | -0.025221375907373885 | 0.04557551711955683 | 0.022728735488689106 | 0.28750586664140193 | 0.2902241259735708 | 0.6028349214565062 | 0.6028349214565062 | 0.09706697763499965 |
| Retail (Automotive) | 208 | 0.06608078571428573 | 0.05012435553065411 | 0.10287586469596494 | 0.23589453873014418 | 0.6741820924391226 | 0.9302921727911228 | 0.09891968306637311 | 0.365384427810218 | 0.0657 | 0.3717844602894967 | 0.08040882364040822 | 2.6155464304479135 | 0.8360007140361282 | 11.861639541973805 | 17.186046585303917 | 3.127673636774118 | 81.11607075357556 | 0.11613663993077378 | 0.021324501407629315 | 0.016567194986285064 | 0.6441326788747836 | 0.1840579660107366 | 0.2947680940994878 | 0.2947680940994878 | 0.04815828942347502 |
| Retail (Building Supply) | 117 | 0.04441772151898734 | 0.10656115161321383 | 0.2461376398673357 | 0.24309177240267593 | 0.8505019178694755 | 0.9765945052218301 | 0.10156354624816649 | 0.34112481595208105 | 0.0657 | 0.18478286981752373 | 0.09187481009784054 | 2.8469120837423003 | 2.107825907712949 | 14.809875799753357 | 19.779644376508973 | 19.11768176233563 | 49.09335035729035 | 0.08708499858731492 | 0.02587699148629189 | 0.05477444707113248 | 0.62906203570821 | 0.9921001879984631 | 0.5333408264813647 | 0.5333408264813647 | 0.10516457985864275 |
| Retail (Distributors) | 1038 | 0.09791606958762891 | 0.04928295149469039 | 0.0799339959563239 | 0.23116288389908993 | 0.6214126804412217 | 0.8201075345159564 | 0.0926281402208611 | 0.3676124393461729 | 0.0657 | 0.3671137302019578 | 0.07665954457984886 | 1.943673711701556 | 0.8348356353188954 | 12.084949912771686 | 16.185383594810467 | 1.5839785215995876 | 81.82789179431978 | 0.16544401430445746 | 0.031005551301192757 | 0.027911408779862108 | 0.8570172906842205 | 0.12488227375888986 | 0.4120966980240126 | 0.4120966980240126 | 0.04973450098466439 |
| Retail (General) | 253 | 0.019390829015544033 | 0.05924229691082409 | 0.10133972617718918 | 0.19124132658939955 | 1.0445584246223811 | 1.104769773812101 | 0.10888235408467095 | 0.34376130249213976 | 0.0657 | 0.12769375354781737 | 0.1012524104474077 | 2.7232353399824696 | 1.8330148893854228 | 17.201151727924977 | 31.51981023275394 | 5.601453097562185 | 89.06645505284209 | 0.015021771148685649 | 0.05110068332114653 | 0.01728319881340636 | 0.40321578384544315 | 0.1809302180720614 | 0.1870138687949028 | 0.18701386879490278 | 0.05796713097762505 |
| Retail (Grocery and Food) | 204 | 0.0600456603773585 | 0.040244062899986256 | 0.10782224576056171 | 0.24884311993825056 | 0.619685890020288 | 0.7748288746225396 | 0.09004272874094701 | 0.3076379871583256 | 0.0657 | 0.32194327930613215 | 0.07687129877863277 | 3.5709022365605043 | 0.6444372587185917 | 9.636517671162286 | 15.943768531608725 | 2.4958635803321796 | 35.53027722271778 | -0.025013504837998732 | 0.028575691029278094 | 0.01092709861017801 | 0.36041561390054655 | 0.1104058137541288 | 0.5955179671666571 | 0.5955179671666571 | 0.03845620029910794 |
| Retail (REITs) | 121 | 0.08284762376237627 | 0.5001065282249229 | 0.048001617939278346 | 0.04486548628619145 | 0.639896428640752 | 0.974888176214587 | 0.10146611486185292 | 0.20234299271343784 | 0.0612 | 0.4330431695955872 | 0.07734528342760932 | 0.10213707891072211 | 11.511604716091854 | 17.299202462732264 | 21.392580282716718 | 1.184426488337337 | 81.25625737032763 | -0.013814521510392669 | 0.03007009009884399 | -0.050879732370639634 | -0.0916375715239623 | 0.04043734976178894 | 1.562077291161109 | 1.562077291161109 | 0.4920281072585968 |
| Retail (Special Lines) | 633 | 0.05541662763466047 | 0.05890805839097781 | 0.1470399885066467 | 0.2471304524677494 | 0.9619087443665812 | 1.0598913069344804 | 0.10631979362595884 | 0.3981427469667038 | 0.0657 | 0.19321961771110194 | 0.0952696924455984 | 2.9583766512181544 | 1.194972977717833 | 11.889756633073452 | 19.433913304527746 | 3.9178839227449673 | 39.739255325161146 | 0.06693670426086686 | 0.022031853834014913 | 0.001241304877115251 | 0.06873217660316387 | 0.10914157998940444 | 0.5835206099037102 | 0.5835206099037102 | 0.06026471746132379 |
| Rubber& Tires | 92 | 0.06180455696202532 | 0.1041946189710417 | 0.10030589911486042 | 0.2380629281392605 | 0.7622642218288536 | 0.9130420368678229 | 0.0979347003051527 | 0.30447246680306844 | 0.0657 | 0.31344269736678787 | 0.08263736758096872 | 1.2921480931644265 | 0.937452678036485 | 5.726002461136792 | 8.938518104009537 | 1.0723311730859577 | 22.008550905548397 | 0.2329929488526439 | 0.06890632025380106 | 0.033505933306492264 | 0.5295842969680905 | 0.10107081994905652 | 0.39476594988021463 | 0.39476594988021463 | 0.10357233543979387 |
| Semiconductor | 665 | 0.07738432835820887 | 0.21342892802586189 | 0.15913647234971032 | 0.14728494801798722 | 1.6614076139987826 | 1.6782559728868123 | 0.141628416051837 | 0.4227354225158977 | 0.0657 | 0.055576897022523435 | 0.13648766667355014 | 1.0926794351128142 | 8.708991582214495 | 24.78669820792039 | 39.72162889779928 | 7.0911935285722025 | 137.20492507459227 | 0.15613189700892702 | 0.16674497372170724 | 0.11719594265964474 | 0.7822345638055896 | 0.15372078320054205 | 0.38497471073014505 | 0.3849747107301451 | 0.22304998196596562 |
| Semiconductor Equip | 375 | 0.09643841328413284 | 0.18648608557226617 | 0.1681612582174975 | 0.1632729299459991 | 2.0245749437343714 | 2.0188341849907365 | 0.16107543196297106 | 0.4385096135203445 | 0.0657 | 0.07008560646376134 | 0.15322970071237746 | 1.3347110524026369 | 4.788955766357449 | 19.055050981102493 | 25.045126734212634 | 4.964783270483776 | 62.22820542390951 | 0.3492796829132233 | 0.1013150204340442 | 0.07145248710624737 | 0.7925123576440898 | 0.18395242715947255 | 0.3692655405261411 | 0.36926554052614113 | 0.19464169814910937 |
| Shipbuilding & Marine | 357 | 0.09890581881533098 | 0.1456287756982192 | 0.0952899796758431 | 0.13868025690251345 | 0.7506806238343013 | 0.8366730815879405 | 0.0935740329586714 | 0.34385890924876383 | 0.0657 | 0.3036986179520979 | 0.08007658127426966 | 0.7460415988430965 | 1.5631628979033525 | 7.226344141112483 | 10.406519873864868 | 0.9509744539076272 | 26.43495318106245 | -0.0020946630263142677 | 0.10973486448820233 | 0.0479781078209702 | 0.5127862640843637 | 0.12192809569866123 | 0.45056013361274094 | 0.45056013361274094 | 0.14801483692823528 |
| Shoe | 82 | -0.01184859375 | 0.11104326222840347 | 0.1867464447049137 | 0.19010081966149922 | 0.7518116101350905 | 0.766209790964854 | 0.08955057906409317 | 0.36837870667795686 | 0.0657 | 0.10497374311291298 | 0.08530752786886568 | 2.063054907104521 | 2.119130714823717 | 14.609529294235351 | 18.74181784305706 | 4.404379392393313 | 49.04608236773148 | 0.19368218656241376 | 0.014023266602783727 | -0.0074046856870474435 | -0.050069596639942905 | 0.2080101698352004 | 0.3675676344734462 | 0.3675676344734462 | 0.11197229343951604 |
| Software (Entertainment) | 311 | 0.12961611702127657 | 0.3005706765379933 | 0.21551369284962238 | 0.16014482156025028 | 1.2571994981034138 | 1.2601011119394356 | 0.11775177349174176 | 0.5291591166446696 | 0.0682 | 0.037008983305729826 | 0.1152813567405987 | 1.2108199820984327 | 6.625998304435553 | 17.79794122383781 | 21.78929709686213 | 6.2033634949669505 | 81.08414190587361 | 0.01643653445137837 | 0.12785219724176686 | 0.09488675645353344 | 0.42153839341779437 | 0.2809801054045535 | 0.0836818043806024 | 0.08368180438060235 | 0.3105833818781535 |
| Software (Internet) | 147 | 0.13876399999999994 | 0.048592885534827684 | 0.13534242363047064 | 0.1360800774419946 | 1.3183294821552847 | 1.370302206754265 | 0.12404425600566851 | 0.49045487085788775 | 0.0682 | 0.09550212624772073 | 0.11706837042685928 | 1.4171358211200535 | 6.006606904719914 | 36.671837030076084 | 95.59569167889396 | 8.096127234595507 | 54.19840720169244 | 0.05965559742004337 | 0.07164938473559157 | 1.8867821441981214 | 48.707438751507134 | 0.03675910171257023 | 0.5031442641398015 | 0.5031442641398015 | 1.89933875321686 |
| Software (System & Application) | 1567 | 0.12663019977802442 | 0.23529299232412612 | 0.2155025330071699 | 0.18289890986131171 | 1.3062901950386756 | 1.3220217888237162 | 0.1212874441418342 | 0.5182410676502874 | 0.0682 | 0.04738292708398446 | 0.11795701740582495 | 1.7212276243824696 | 9.949708907005416 | 28.175499498690545 | 38.9169595641231 | 9.355734821455885 | 126.90444921887325 | 0.11839954050265998 | 0.09893182940943189 | 0.16827628965820413 | 0.9445904808338665 | 0.19997192333925523 | 0.29238301037888953 | 0.2923830103788896 | 0.2485555047805545 |
| Steel | 727 | 0.08867734729493887 | 0.05588964379870377 | 0.06714366561929556 | 0.22305624292718015 | 0.9368976981171875 | 1.1503164323693125 | 0.11148306828828775 | 0.3647609307279481 | 0.0657 | 0.3491864839517607 | 0.08971038023487914 | 1.4149409280658292 | 0.7378165646184713 | 6.7333764064996515 | 12.416542389663983 | 0.8866040261597283 | 40.6154948930657 | 0.14573435255963102 | 0.06920970793009786 | 0.04405337669589425 | 1.1489567343320086 | 0.05817759911574916 | 0.7626058118067116 | 0.7626058118067116 | 0.05653804644097683 |
| Telecom (Wireless) | 98 | 0.06572125 | 0.1504256110533277 | 0.09125758201669891 | 0.20573941316505037 | 0.6677029437691795 | 0.8966865208041107 | 0.09700080033791472 | 0.2979439172230527 | 0.0612 | 0.3717635077285821 | 0.07795333331787305 | 0.7327045130572793 | 2.4164834395924806 | 7.936894151214051 | 16.18033477434827 | 1.67383663047263 | 37.225399646705654 | -0.11944514701787583 | 0.14227790591002004 | 0.004436514397926499 | 0.23214748789030573 | 0.12144919744872282 | 0.5651423003823961 | 0.5651423003823961 | 0.15460199014959705 |
| Telecom. Equipment | 440 | 0.03249771739130435 | 0.10034189474527085 | 0.1150888135688252 | 0.13315894255152091 | 1.1657942786205602 | 1.194848437320267 | 0.11402584577098723 | 0.45110054710512826 | 0.0682 | 0.11717756571463833 | 0.10664062589933408 | 2.133449316551066 | 3.1249197515155034 | 19.594893307939277 | 28.77849391695484 | 1.4537205694885273 | 1214.1471266685842 | 0.23096559178353746 | 0.03140360804582742 | 0.11382499999201402 | 1.118233662094995 | 0.08701211123782261 | 0.7980208714108472 | 0.7980208714108472 | 0.10628065173262888 |
| Telecom. Services | 274 | 0.09622234741784036 | 0.15849933656994836 | 0.09443635195896061 | 0.2572917715967945 | 0.56153373714287 | 0.8550601614198708 | 0.09462393521707463 | 0.3595014226933627 | 0.0657 | 0.4439547655066988 | 0.07442689009499344 | 0.7069149298346922 | 2.1270350277373287 | 6.591251748080409 | 13.150511409746436 | 1.4442478756159476 | 31.7251055162019 | 0.002494972503375732 | 0.13961160101976128 | -0.024904116834196376 | -0.1704302189203261 | 0.07173997369320387 | 1.040007505483598 | 1.040007505483598 | 0.15940387291798466 |
| Tobacco | 54 | 0.3216951162790697 | 0.31816203573924395 | 0.21074845170305248 | 0.21340542399574022 | 0.4281823452206098 | 0.4991008376020947 | 0.0742986578270796 | 0.435071779899884 | 0.0657 | 0.21836442328743838 | 0.06880281882338521 | 0.8131276141902394 | 3.811976834989089 | 10.585718837954175 | 11.9448170729096 | 4.324858735416174 | 24.825429268205777 | 0.16015318560811023 | 0.030316812433430644 | -0.006124985589879158 | -0.01554790043416352 | 0.10474313833596573 | 1.9933810028880292 | 1.9933810028880292 | 0.31851588612350995 |
| Transportation | 446 | 0.11398623376623374 | 0.06678266624701394 | 0.08771982267279026 | 0.2196352934185786 | 0.7080179718509676 | 0.9208773980068596 | 0.0983820994261917 | 0.3542176323049625 | 0.0657 | 0.3591640175760828 | 0.08069268273767208 | 1.6123142590216617 | 1.2299670565769731 | 10.45563391803228 | 17.314661800139064 | 1.9017142768387425 | 45.61218451016317 | 0.03225227136514108 | 0.043282548485499714 | 0.010388768796590047 | 0.37753566426628327 | 0.11920419510260823 | 0.5543814785773705 | 0.5543814785773705 | 0.06730511186864416 |
| Transportation (Railroads) | 54 | 0.0011922222222222202 | 0.22968154884064834 | 0.0839752026313908 | 0.23749901561865872 | 0.61340248884171 | 0.8009430350904613 | 0.09153384730366534 | 0.21796118227542896 | 0.0612 | 0.32519926850152797 | 0.0766499687120919 | 0.46351632546624344 | 3.733593144665918 | 11.006040774056666 | 15.994348218590789 | 1.9506652485134208 | 24.631744447251233 | 0.06244499224212902 | 0.17329726449242247 | 0.11132107764862063 | 0.6724574315836479 | 0.1301223688587202 | 0.3834361301670866 | 0.38343613016708655 | 0.23157174435676822 |
| Trucking | 113 | 0.04918160493827158 | 0.0753296571799199 | 0.09425862206181831 | 0.24711593668939988 | 0.6972765725709966 | 0.851592078101013 | 0.09442590765956785 | 0.33872458859943927 | 0.0657 | 0.26028933258687587 | 0.08263598581903517 | 1.529153595252337 | 1.5853905197423346 | 10.290760835840068 | 20.328257422330534 | 2.5622334984026183 | 77.87155222990306 | 0.06700264607480963 | 0.11257750993727737 | 0.06889583971237419 | 1.1478645542405777 | 0.0917556887503292 | 0.3022195260212316 | 0.3022195260212316 | 0.07681384291412023 |
| Utility (General) | 52 | 0.04313956521739129 | 0.1497309632557981 | 0.08406795723580653 | 0.1531684021545398 | 0.4293673465124172 | 0.6529650084393694 | 0.08308430198188799 | 0.21904160884218274 | 0.0612 | 0.44426312380056915 | 0.06650487224008222 | 0.6708962381093332 | 2.408308795454755 | 10.29775989560504 | 16.129722995120197 | 1.604371431586532 | 16.75160693273575 | -0.03222569424995128 | 0.19357492852232017 | 0.11661381202132674 | 0.9968959632193806 | 0.10714233716527913 | 0.6780132743146468 | 0.6780132743146468 | 0.14938493487574075 |
| Utility (Water) | 106 | 0.06402658823529411 | 0.2619979802373128 | 0.07045633803569709 | 0.21916734957401024 | 0.4070576244109758 | 0.6674612303833111 | 0.08391203625488705 | 0.3134659052139992 | 0.0657 | 0.4948539301685357 | 0.06670023654769958 | 0.31906450065547604 | 4.449026913332253 | 11.223810658872942 | 16.829973847096994 | 1.3543250533701492 | 22.16381608993469 | 0.10812369734755466 | 0.24975989914155822 | 0.1312284591374094 | 0.7639934010248204 | 0.11510643200063127 | 0.6656255388167998 | 0.48297940904182024 | 0.26216752986427083 |
| Tiotal Market | 47810 | 0.09196669412124926 | 0.10240304523413575 | 0.06931334160955732 | 0.2154439821853485 | 0.7944602468554776 | 1.016327909542543 | 0.10383232363487921 | 0.4087040282697168 | 0.0657 | 0.37081896540542153 | 0.08354783515604486 | 0.796490186309763 | 2.4842971498154522 | 13.21342785074356 | 19.78446438728275 | 2.1526525659456675 | 74.52514474933345 | -1.2054905343567515 | 0.06435696483693416 | 0.04155856269057567 | 0.6852248542373072 | 0.11510643200063127 | 0.48297940904182024 | 0.48297940904182024 | 0.10587551679735265 |
| Total Market (without financials) | 42750 | 0.08678596665746692 | 0.09777263014633325 | 0.10997032471851471 | 0.22547870642741624 | 0.915155197428865 | 1.0480020010286757 | 0.10564091425873738 | 0.41664366643680406 | 0.0657 | 0.22771761651352895 | 0.0927724883068409 | 1.3815053414692071 | 1.8953802539663376 | 12.152627518309783 | 18.667601887208964 | 2.5328727957007104 | 77.65897060338989 | 0.12219536157105167 | 0.06476508635962093 | 0.04076020921540295 | 0.7123419882101653 | 0.1112437980672905 | 0.5354053033856725 | 0.5354053033856725 | 0.10142295103506685 |

## Trailing 12 month

| Last 10K | First X months: Last year | First X months: Current year | Trailing 12 month |
|---|---|---|---|
| 15794.34 | 7608.13 | 9444.11 | 17630.32 |
| 1221.81 | 581.41 | 756 | 1396.4 |
| 1605.23 | 908.79 | 1165.5 | 1861.94 |
| 420.49 | 182.82 | 287.56 | 525.23 |
| 5238.77 |  | 6105.55 |  |
| 10360 |  | 12594.14 |  |
|  |  |  |  |
| 3794.48 |  | 5004.25 |  |
| 0 |  | 0 |  |
| 0 |  | 0 |  |
|  |  |  |  |
|  |  |  |  |
| 0.2588313889069934 | 0.25767665556788755 | 0.16485401154521878 |  |
|  |  |  |  |
|  |  |  |  |
| 172.47 |  | NA |  |
| 139.4 | Copy into operating lease worksheet | NA |  |
| 145.18 |  | NA |  |
| 156.53 |  | NA |  |
| 151.2 |  | NA |  |
| 943.63 |  | NA |  |
| 107 |  |  |  |
|  |  | 75872 |  |
|  |  | 2404 |  |
|  |  | 24171 |  |
|  |  | 276 |  |
| 630.29 | 286.14 | 426.61 | 770.76 |
| 2369.47 | 1128.78 | 1219.73 | 2460.42 |
| 9967.54 | 4703.01 | 5876.21 | 11140.740000000002 |
| 13043 | 6020.47 | 6322.85 | 13345.380000000001 |

## Answer keys

| Yes/No | Book or Market Value | ERP choices | Cost of debt | Synthetic rating | Beta | Rating is |
|---|---|---|---|---|---|---|
| Yes | B | Will input | Direct input | 1 | Direct input | Aaa/AAA |
| No | V | Country of incorporation | Synthetic rating | 2 | Single Business(US) | Aa2/AA |
|  |  | Operating countries | Actual rating |  | Single Business(Global) | A1/A+ |
|  |  | Operating regions |  |  | Multibusiness(US) | A2/A |
|  |  |  |  |  | Multibusiness(Global) | A3/A- |
|  |  |  |  |  |  | Baa2/BBB |
|  |  |  |  |  |  | Ba1/BB+ |
|  |  |  |  |  |  | Ba2/BB |
|  |  |  |  |  |  | B1/B+ |
|  |  |  |  |  |  | B2/B |
|  |  |  |  |  |  | B3/B- |
|  |  |  |  |  |  | C2/C |
|  |  |  |  |  |  | Ca2/CC |
|  |  |  |  |  |  | Caa/CCC |
|  |  |  |  |  |  | D2/D |
