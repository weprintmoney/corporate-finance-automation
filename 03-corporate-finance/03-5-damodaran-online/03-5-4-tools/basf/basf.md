---
title: "Basf"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/blog/BASF.xlsx
---

# Basf

Source: https://www.stern.nyu.edu/~adamodar/pc/blog/BASF.xlsx

Sheets: Input sheet, Valuation output, Stories to Numbers, Diagnostics, Option value, Synthetic rating, R& D converter, Operating lease converter, Cost of capital worksheet, Failure Rate worksheet, Summary Sheet, Country equity risk premiums, Industry Averages(US), Input Stat Distributioons, Industry Average Beta (Global), Trailing 12 month, Answer keys

## Input sheet

| Input cell | Calculated cell |
|---|---|
| Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |  |
| There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |  |
|  |  |
| Last year | Updated on January 2023 with updated Industry averages and risk premiums |
|  |  |
|  |  |
| Last 10K |  |
| 78598 |  |
| 7467 |  |
| 506 |  |
| 42081 |  |
| 19136 |  |
|  If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |  |
| If you have operating leases, please enter your lease commitments in the lease worksheet below and I will convert to debt |  |
| 4386 |  |
| 12958 |  |
| 0 |  |
|  |  |
|  | Computed numbers: Here is what your company's numbers look like, relative to industry. |
|  | If you are not working in US dollars, you should add the inflation differential to the industry averages. |
|  |  |
|  |  |
|  | Revenue growth in the most recent year = |
|  | Pre-tax operating margin in the most recent year = |
| Growth Lever | Sales to capital ratio in most recent year = |
| Profitability Lever | Marginal Sales to capital in most recent year |
| Speed of convergence level | Return on invested capital in most recent year= |
| Efficency of Growth Lever | Standard deviation in stock prices = |
|  | Cost of capital = |
|  |  |
|  | Valuation Output Feedback (for you to use to fine tune your inputs, if you want) |
| Do not input. Go to cost of capital sheet. | Revenues in year 10, based on your revenue growth = |
|  | Pre-tax Operating Income in year 10, based on your operating margin = |
|  | Return on invested capital in year 10, based on your sales/capital ratio = |
|  | Check the Diagnostics worksheet for more details. |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
| Mature companies generally see their risk levels approach the average |  |
| Though some sectors, even in stable growth, may have higher risk. If you change your risk free rate after year 10 (see cell B57 & 58), you should incorporate the change into your stable cost of capital estimate. |  |
|  |  |
| Mature companies find it difficult to generate returns that exceed the cost of capital |  |
| But there are significant exceptions among companies with long-lasting competitive advantages. |  |
|  |  |
| Many young, growth companies fail, especially if they have trouble raising cash. Many distressed companies fail, because they have trouble making debt payments. |  |
| Tough to estimate but a key input. Use the failure rate worksheet, if necessary. |  |
| B: Book value of capital, V= Estimated fair value for the company |  |
| This can be zero, if the assets will be worth nothing if the firm fails. |  |
|  |  |
|  |  |
|  |  |
| Check the financial statements. |  |
| An NOL will shield your income from taxes, even after you start making money. |  |
|  |  |
| If yes, you will be asked to enter a normal risk free rate and your growth in perpetuity will be adjusted accordingly. |  |
| Enter your estimate of what the riskfree rate (in your currency of choice) will be after year 10 |  |
|  |  |
| This is an option to let you use a negative growth rate in perpetuity or to even liquidate the firm. |  |
| This can be negative, if you feel the company will decline (and disappear) after growth is done. If you let it exceed the risk free rate, you are on your own in uncharted territory. |  |
|  |  |
|  |  |
| Cash that is trapped in foreign markets (and subject to additoinal tax) or cash that is being discounted by the market (because of management mistrust) |  |
| Additional tax rate due on trapped cash or discount being applied to cash balance because of mistrust. |  |

## Valuation output

| Base year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Terminal year |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.03 | 0.03 | 0.03 | 0.03 | 0.03 | 0.02896 | 0.02792 | 0.02688 | 0.02584 | 0.0248 | 0.0248 |
| 87327 | 89946.81 | 92645.2143 | 95424.57072900001 | 98287.30785087001 | 101235.92708639611 | 104167.71953481816 | 107076.08226423027 | 109954.28735549278 | 112795.50614075872 | 115592.83469304953 | 118459.53699343716 |
| 0.07974242406892103 | 0.08 | 0.079 | 0.0785 | 0.078 | 0.0775 | 0.077 | 0.0765 | 0.076 | 0.0755 | 0.075 | 0.075 |
| 6963.666666666666 | 7195.7448 | 7318.971929700001 | 7490.8288022265015 | 7666.410012367861 | 7845.784349195699 | 8020.914404180998 | 8191.3202932136155 | 8356.525839017451 | 8516.060713627283 | 8669.462601978714 | 8884.465274507786 |
| 0.27 | 0.27 | 0.27 | 0.27 | 0.27 | 0.27 | 0.276 | 0.28200000000000003 | 0.28800000000000003 | 0.29400000000000004 | 0.30000000000000004 | 0.3 |
| 5083.4766666666665 | 5252.893704 | 5342.849508681001 | 5468.305025625346 | 5596.479309028538 | 5727.42257491286 | 5807.142028627042 | 5881.367970527375 | 5949.846397380425 | 6012.338863820862 | 6068.623821385099 | 6219.1256921554495 |
|  | 1885.7858000000065 | 1942.3593740000047 | 2000.6301552199993 | 2060.649059876601 | 2048.8896225749118 | 2032.5157117391936 | 2011.4399797652823 | 1985.5920181967397 | 1954.919232023374 | 2003.4012289775537 | 1947.4029945133234 |
|  | 3367.1079039999936 | 3400.490134680996 | 3467.674870405347 | 3535.8302491519376 | 3678.5329523379482 | 3774.6263168878486 | 3869.927990762093 | 3964.254379183685 | 4057.4196317974875 | 4065.2225924075456 | 4271.722697642126 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0.08830897897546104 | 0.08830897897546104 | 0.08830897897546104 | 0.08830897897546104 | 0.08830897897546104 | 0.08648718318036883 | 0.08466538738527661 | 0.0828435915901844 | 0.08102179579509218 | 0.07919999999999996 | 0.07919999999999999 |
|  | 0.9188567027549516 | 0.8442976401977014 | 0.7757885458158463 | 0.7128385052434072 | 0.6549964385247254 | 0.6028570319692292 | 0.5558000089064264 | 0.5132781993844738 | 0.4748083723945245 | 0.43996328057313244 |  |
|  | 3093.88966648957 | 2871.0257962267287 | 2690.1824450739177 | 2520.475949599891 | 2409.4259827772 | 2275.5600181919517 | 2150.9060117328004 | 2034.765349649417 | 1926.4968114953558 | 1788.5486680156378 |  |
| 4271.722697642126 |  |  |  |  |  |  |  |  |  |  |  |
| 0.07919999999999999 |  |  |  |  |  |  |  |  |  |  |  |
| 78524.31429489204 |  |  |  |  |  |  |  |  |  |  |  |
| 34547.81492193642 |  |  |  |  |  |  |  |  |  |  |  |
| 23761.27669925247 |  |  |  |  |  |  |  |  |  |  |  |
| 58309.09162118889 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 29154.545810594445 |  |  |  |  |  |  |  |  |  |  |  |
| 58309.09162118889 |  |  |  |  |  |  |  |  |  |  |  |
| 20949 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 4687 |  |  |  |  |  |  |  |  |  |  |  |
| 8121 |  |  |  |  |  |  |  |  |  |  |  |
| 50168.09162118889 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 50168.09162118889 |  |  |  |  |  |  |  |  |  |  |  |
| 901.8 |  |  |  |  |  |  |  |  |  |  |  |
| 55.63106189974373 |  |  |  |  |  |  |  |  |  |  |  |
| 49.81 |  |  |  |  |  |  |  |  |  |  |  |
| 0.8953630993017133 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 | 1.4309177108025737 |  |
| 61028.666666666664 | 62914.45246666667 | 64856.811840666676 | 66857.44199588668 | 68918.09105576327 | 70966.98067833818 | 72999.49639007737 | 75010.93636984266 | 76996.5283880394 | 78951.44762006277 | 80954.84884904033 |  |
| 0.08329653823886042 | 0.08607256214019642 | 0.08492245103001968 | 0.08431350339975541 | 0.08370764932006904 | 0.08310477680350527 | 0.0818287881648543 | 0.08056724034231576 | 0.07931971903462995 | 0.07808584347492238 | 0.07686526345392772 | 0.07919999999999996 |

## Stories to Numbers

| BASF | 2023-04-01 00:00:00 |
|---|---|
| Chemical Reaction |  |
| BASF has been a longstanding leader in the chemical business, with a reputation for superior engineering and products tailored to different markets. Over the last two decades, BASF has fought industry-wide trends, increased competition from lower cost producers and disruptors, pushing down margins, and pressures from envirnomentalists to clean up the business. The company will continue to face these headwinds in the future, but will be able grow at rates close to that of the economy while its margis continue to drop.  |  |
| The Assumptions |  |
|  | Link to story |
| Revenues (a) | Slow growth as lower-cost and disruptive new entrants eat into market shaare. |
| Operating margin (b) | Margins continue to remain under pressure, but BASF's engineering expertise and efficiencies will restrict margin drop. |
| Tax rate | Move to German corporate tax rate over time |
| Reinvestment (c ) | Maintined at BASF's current level |
| Return on capital | Earn cost of capital |
| Cost of capital (d) | Based on median company |
| The Cash Flows |  |
|  | FCFF |
| 1 | 3367.1079039999936 |
| 2 | 3400.490134680996 |
| 3 | 3467.674870405347 |
| 4 | 3535.8302491519376 |
| 5 | 3678.5329523379482 |
| 6 | 3774.6263168878486 |
| 7 | 3869.927990762093 |
| 8 | 3964.254379183685 |
| 9 | 4057.4196317974875 |
| 10 | 4065.2225924075456 |
| Terminal year | 4271.722697642126 |
| The Value |  |
| Terminal value |  |
| PV(Terminal value) |  |
| PV (CF over next 10 years) |  |
| Value of operating assets = |  |
| Adjustment for distress | 0 |
|  - Debt & Minority Interests |  |
|  + Cash & Other Non-operating assets |  |
| Value of equity |  |
|  - Value of equity options |  |
| Number of shares |  |
| Value per share | 49.81 |

## Diagnostics

| Step 1: Check revenue growth rate | Your forecasts | Questions to ask |
|---|---|---|
|  | Next year | 1. If you are forecasting a revenue growth rate > industry average, is your company small? |
| Annual Revenue Growth Rate | 0.03 | 2. If your forecasted revenue growth rate is very different from your company's most recent year of growth, what is the reason? |
| Step 2: Check dollar revenues |  |  |
|  | Year 5 | 1. How big is the total market today? |
| Revenues | 101235.92708639611 | 2. How much revenues do the biggest companies in that market make today? |
|  |  | 3. How much growth is there in the total market? |
|  |  | 4. What type of market share are you forecasting for your company in year 10? |
| Step 3: Check your margins | Year 5 | 1. What are the margins of the industry that the company is in? |
| Operating Margin | 0.0775 | 2. What are the unit economics of the business? (How much does it cost you to make the extra unit that you sell? |
|  |  | 3. What does the competition in this business look like? |
| Step 4: Check how much you are reinvesting |  |  |
|  | Year 5 | 1. is the growth that you are forecasting bounce-back growth or new growth? |
| Sales to Capital | 1.4309177108025737 | 2. How much excess capacity do you have to service near term growth? |
|  |  | 3. Does investment efficiency in this business change as companies get bigger? |
| Reinvestment effect on cash flows |  |  |
|  |  |  |
| PV of after-tax operating income for next 10 yearas |  | 1. Is your reinvestment consitent with your revenue growth forecast? |
| Value effect of reinvestment for next 10 years |  | 2. Are you comfortable with your return on capital in year 10? |
| PV of FCFF for next ten years |  |  |
| Return on capital effects |  |  |
|  | ROC in year 10 |  |
| Return on capital | 0.07686526345392772 |  |
| Step 5: Risk Metrics |  |  |
|  | Year 1-5 | 1. How does your cost of capital compare to the industry average? |
| Cost of capital | 0.08830897897546104 | 2. What is happenign to your cost of capital over time? Why? |
|  |  | 3. Is your failure rate consistent with your company's characteristics? |
| Failure Rate |  |  |
| Step 6: Price versus Value |  |  |
| Your calculated value as a percent of current price |  |  |
|  |  |  |
| Inputs |  |  |
| Revenue growth rate (input cell B25, B27) |  |  |
| Operating margin (B26, B28) |   |  |
| Sales to Capital (B30-B32) |   |  |
| Return on capital in perpetuity (B48, B49) | T |  |

## Option value

| Note: This worksheet is the most finicky of all of the worksheets in this spreadsheet. If you start to get errors, here is a quick fix. Go into cell B12 and replace the contents with a number (say 5), and then undo your action. The spreadsheet will fix itself magically. |
|---|
| Valuing Options or Warrants |
| Enter the current stock price = |
| Enter the strike price on the option = |
| Enter the expiration of the option = |
| Enter the standard deviation in stock prices = |
| Enter the annualized dividend yield on stock = |
| Enter the treasury bond rate = |
| Enter the number of warrants (options) outstanding = |
| Enter the number of shares outstanding = |
| Do not input any numbers below this line |
| Dilution-adjusted Black-Scholes |
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

## Synthetic rating

| If you have negative operating income, this spreadsheet will offer you a D rating. Do not use that rating as your cost of debt for a going concern. Insread give your company a low, but going concern rating like BB and use that cost of debt. |
|---|
| Inputs for synthetic rating estimation |
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
| 0 |
| 0 |
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
| 0 |
| 0 |
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

## Cost of capital worksheet

| You can use this spreadsheet to compute your cost of capital. You can either use the built-in data to compute key inputs (beta, equity risk premium, default spread) or enter them directly. If you choose to use the built in ERP data, you can update the ERP numbers to reflect a more current mature market premuum (since the spreadsheet uses the start of the year numbers). |
|---|
| Estimation of Current Cost of Capital |
| There are four ways in whch you can estimate your cost of capital. In the first, you can directly input a cost of captial. In the second, you can work through your company's cost of capital inputs in detail, entering business, geogaphical mix and debt, and I will help you estimate a cost of capital. In the third, you can look up the cost of capital for the industry your firm belongs to and in the fourth, you can use a crosssectoinal distribution  of costs of capital for companies at the start of the year to make your estimate. |
|  |
|  |
|  |
|  |
|  |
|  |
| Which approach will you be using? |
| If direct input, enter cost of capital to use |
| Cost of capital based upon approach = |
|  |
| Approach 1: Detailed Cost of Capital |
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
| Approach 2: industry average cost of capital, adjusted for riskfre rate differences |
| Industry  |
| Cost of capital, adjusted for riskfree rate difference |
| Approach 3: Uae histogram of costs of capital of all publicly traded firms |
| What risk  decile does your company fall in? |
| Which grouping (US, Emerging Markets, Global) |
| Cost of capital based upon decile/group chosen |
| Decile/Quartile |
| First Decile (lowest Risk) |
| First Quartile  |
| Median |
| Third Quartile |
| Ninth Decile (Highest Risk) |
| These costs of capital are all in US dollars and reflect the US dollar  riskfree rate at the start of the year. Once you make your choice, though, I will adjust the rate by the difference in riskfree rates, effectively converting currency and bringing it up to date.  |

## Failure Rate worksheet

| Estimating the likelihood of failure |
|---|
| Approach 1: Using a corporate bond rating |
| Default Probabilities over time (1 - 10 year time horizons) |
| Rating |
| AAA |
| AA |
| A |
| BBB |
| BB |
| B |
| CCC/C |
| Thus, if you use the 10-year likelihood of failure, the chance of failure for a BB rated firm is 11.78%. |
| Approach 2: Using corporate age (for young companies) |
|  |
|  |
| Failure Rate given age |
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
| Source; Bureau of Labor Statistics |
| Thus, if you are valuing a technology firm that is 6 years old, the chance of failure is 11.70%. |
| Factors to consider |
| 1. The likelihood of failure decreases for larger firms.  |
| 2. The likelihood of failure decreases with access to capital, and is thus lower for publicly traded firms or firms with multiple high profile VCs |
| 3. The likelihood of failure decreases as revenue growth increases, since hope for future growth will sustain the firm. |
| 4. The likelihood of failure decreases with better unit economics, higher gross margins on the additional units sold |

## Summary Sheet

| Year | Revenues | Revenue Growth Rate | Pre-Tax Operating Margin | Pre-Tax Operating Income | NOL | Taxes | After-Tax Operating Income |
|---|---|---|---|---|---|---|---|
| Traling 12 month | 87327 |  | 0.07974242406892103 | 6963.666666666667 | 0 | 1880.1900000000005 | 5083.4766666666665 |
| 1 | 89946.81 | 0.03 | 0.08 | 7195.7448 | 0 | 1942.8510960000003 | 5252.893704 |
| 2 | 92645.2143 | 0.030000000000000027 | 0.079 | 7318.971929700001 | 0 | 1976.1224210190003 | 5342.849508681001 |
| 3 | 95424.57072900001 | 0.030000000000000027 | 0.0785 | 7490.8288022265015 | 0 | 2022.523776601155 | 5468.305025625346 |
| 4 | 98287.30785087001 | 0.030000000000000027 | 0.078 | 7666.410012367861 | 0 | 2069.9307033393225 | 5596.479309028538 |
| 5 | 101235.92708639611 | 0.030000000000000027 | 0.0775 | 7845.784349195699 | 0 | 2118.361774282839 | 5727.42257491286 |
| 6 | 104167.71953481816 | 0.028960000000000097 | 0.077 | 8020.914404180998 | 0 | 2213.7723755539555 | 5807.142028627042 |
| 7 | 107076.08226423027 | 0.027919999999999945 | 0.0765 | 8191.3202932136155 | 0 | 2309.95232268624 | 5881.367970527375 |
| 8 | 109954.28735549278 | 0.026880000000000015 | 0.076 | 8356.525839017451 | 0 | 2406.6794416370267 | 5949.846397380425 |
| 9 | 112795.50614075872 | 0.025840000000000085 | 0.0755 | 8516.060713627283 | 0 | 2503.7218498064212 | 6012.338863820862 |
| 10 | 115592.83469304953 | 0.024799999999999933 | 0.075 | 8669.462601978714 | 0 | 2600.8387805936145 | 6068.623821385099 |
| Year | After-Tax Operating Income | Change in Revenues | Sales to Capital | Reinvestment | FCFF | Capital Invested | Implied ROC |
| Traling 12 month | 5083.4766666666665 |  |  |  |  | 61028.666666666664 | 0.08329653823886042 |
| 1 | 5252.893704 | 2619.8099999999977 | 1.4309177108025737 | 1830.8599999999983 | 3422.0337040000018 | 62859.526666666665 | 0.08356559431087031 |
| 2 | 5342.849508681001 | 2698.4043000000092 | 1.4309177108025737 | 1885.7858000000065 | 3457.0637086809943 | 64745.31246666667 | 0.08252102438198443 |
| 3 | 5468.305025625346 | 2779.3564290000068 | 1.4309177108025737 | 1942.3593740000047 | 3525.9456516253417 | 66687.67184066668 | 0.08199873941754149 |
| 4 | 5596.479309028538 | 2862.737121869999 | 1.4309177108025737 | 2000.6301552199993 | 3595.849153808539 | 68688.30199588668 | 0.08147645445309853 |
| 5 | 5727.42257491286 | 2948.619235526101 | 1.4309177108025737 | 2060.649059876601 | 3666.773515036259 | 70748.95105576327 | 0.08095416948865561 |
| 6 | 5807.142028627042 | 2931.792448422042 | 1.4309177108025737 | 2048.8896225749118 | 3758.2524060521305 | 72797.84067833818 | 0.07977080054182188 |
| 7 | 5881.367970527375 | 2908.3627294121106 | 1.4309177108025737 | 2032.5157117391936 | 3848.8522587881816 | 74830.35639007737 | 0.07859601710125297 |
| 8 | 5949.846397380425 | 2878.2050912625127 | 1.4309177108025737 | 2011.4399797652823 | 3938.4064176151423 | 76841.79636984266 | 0.07742981916694885 |
| 9 | 6012.338863820862 | 2841.218785265941 | 1.4309177108025737 | 1985.5920181967397 | 4026.746845624122 | 78827.3883880394 | 0.07627220673890958 |
| 10 | 6068.623821385099 | 2797.328552290812 | 1.4309177108025737 | 1954.919232023374 | 4113.704589361725 | 80782.30762006277 | 0.07512317981713511 |
| Year | Beta | Cost of Equity | Pre-Tax Cost of Debt | Tax Savings | After-Tax Cost of Debt | Debt Ratio | Cost of Capital |
| 1 |  |  |  |  |  |  | 0.08830897897546104 |
| 2 |  |  |  |  |  |  | 0.08830897897546104 |
| 3 |  |  |  |  |  |  | 0.08830897897546104 |
| 4 |  |  |  |  |  |  | 0.08830897897546104 |
| 5 |  |  |  |  |  |  | 0.08830897897546104 |
| 6 |  |  |  |  |  |  | 0.08648718318036883 |
| 7 |  |  |  |  |  |  | 0.08466538738527661 |
| 8 |  |  |  |  |  |  | 0.0828435915901844 |
| 9 |  |  |  |  |  |  | 0.08102179579509218 |
| 10 |  |  |  |  |  |  | 0.07919999999999996 |
| Year | Cost of Capital | Cumulated Cost of Capital | FCFF | Terminal Value | Present Value |  |  |
| 1 | 0.08830897897546104 | 1.088308978975461 | 3422.0337040000018 |  | 3144.3586059737554 |  |  |
| 2 | 0.08830897897546104 | 1.1844164337186103 | 3457.0637086809943 |  | 2918.7907312524776 |  |  |
| 3 | 0.08830897897546104 | 1.2890110396620575 | 3525.9456516253417 |  | 2735.388249700131 |  |  |
| 4 | 0.08830897897546104 | 1.4028422884627112 | 3595.849153808539 |  | 2563.25973588165 |  |  |
| 5 | 0.08830897897546104 | 1.5267258586204524 | 3666.773515036259 |  | 2401.723593225539 |  |  |
| 6 | 0.08648718318036883 | 1.6587680776211653 | 3758.2524060521305 |  | 2265.6888909038025 |  |  |
| 7 | 0.08466538738527661 | 1.7992083194952917 | 3848.8522587881816 |  | 2139.1921197139914 |  |  |
| 8 | 0.0828435915901844 | 1.9482611987012217 | 3938.4064176151423 |  | 2021.498154477757 |  |  |
| 9 | 0.08102179579509218 | 2.106112819697894 | 4026.746845624122 |  | 1911.9331158155758 |  |  |
| 10 | 0.07919999999999996 | 2.272916955017967 | 4113.704589361725 | 78524.31429489204 | 36357.693888380774 |  |  |
| Value of operating assets = |  |  |  |  | 58459.52708532546 |  |  |

## Country equity risk premiums

| Mature Market ERP + | 0.0544 | Updated January 1, 2023 |
|---|---|---|
| Changing this number will update all your country equity risk premiums. |  |  |
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.006039908256880735 |
| Albania | B1 | 0.05507821100917431 |
| Algeria | NR | 0.036814678899082576 |
| Andorra (Principality of) | Baa2 | 0.023296788990825688 |
| Angola | B3 | 0.07952545871559634 |
| Argentina | Ca | 0.14682729357798166 |
| Armenia | Ba3 | 0.04400504587155964 |
| Aruba | Baa2 | 0.023296788990825688 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.004889449541284403 |
| Azerbaijan | Ba1 | 0.030630963302752296 |
| Bahamas | B1 | 0.05507821100917431 |
| Bahrain | B2 | 0.06730183486238533 |
| Bangladesh | Ba3 | 0.04400504587155964 |
| Barbados | Caa1 | 0.09174908256880734 |
| Belarus | Ca | 0.14682729357798166 |
| Belgium | Aa3 | 0.007334174311926606 |
| Belize | Caa2 | 0.11015642201834862 |
| Benin | B1 | 0.05507821100917431 |
| Bermuda | A2 | 0.010354128440366973 |
| Bolivia | B2 | 0.06730183486238533 |
| Bosnia and Herzegovina | B3 | 0.07952545871559634 |
| Botswana | A3 | 0.014668348623853212 |
| Brazil | Ba2 | 0.03681467889908257 |
| Brunei | NR | 0.01035412844036697 |
| Bulgaria | Baa1 | 0.019557798165137613 |
| Burkina Faso | Caa1 | 0.09174908256880734 |
| Cambodia | B2 | 0.06730183486238533 |
| Cameroon | B2 | 0.06730183486238533 |
| Canada | Aaa | 0 |
| Cape Verde | B3 | 0.07952545871559634 |
| Cayman Islands | Aa3 | 0.007334174311926606 |
| Chile | A2 | 0.010354128440366973 |
| China | A1 | 0.008628440366972478 |
| Colombia | Baa2 | 0.023296788990825688 |
| Congo (Democratic Republic of) | B3 | 0.07952545871559634 |
| Congo (Republic of) | Caa2 | 0.11015642201834862 |
| Cook Islands | B1 | 0.05507821100917431 |
| Costa Rica | B2 | 0.06730183486238533 |
| Côte d'Ivoire | Ba3 | 0.04400504587155964 |
| Croatia | Baa2 | 0.023296788990825688 |
| Cuba | Ca | 0.14682729357798166 |
| Curacao | Baa2 | 0.023296788990825688 |
| Cyprus | Ba1 | 0.030630963302752296 |
| Czech Republic | Aa3 | 0.007334174311926606 |
| Denmark | Aaa | 0 |
| Dominican Republic | Ba3 | 0.04400504587155964 |
| Ecuador | Caa3 | 0.12238004587155965 |
| Egypt | B2 | 0.06730183486238533 |
| El Salvador | Caa3 | 0.12238004587155965 |
| Estonia | A1 | 0.008628440366972478 |
| Ethiopia | Caa2 | 0.11015642201834862 |
| Fiji | B1 | 0.05507821100917431 |
| Finland | Aa1 | 0.004889449541284403 |
| France | Aa2 | 0.006039908256880735 |
| Gabon | Caa1 | 0.09174908256880734 |
| Gambia | NR | 0.06730183486238533 |
| Georgia | Ba2 | 0.03681467889908257 |
| Germany | Aaa | 0 |
| Ghana | Ca | 0.14682729357798166 |
| Greece | Ba3 | 0.04400504587155964 |
| Guatemala | Ba1 | 0.030630963302752296 |
| Guernsey (States of) | Aaa | 0 |
| Guinea | NR | 0.11015642201834863 |
| Guinea-Bissau | NR | 0.07952545871559634 |
| Guyana | NR | 0.01955779816513761 |
| Haiti | NR | 0.14682729357798163 |
| Honduras | B1 | 0.05507821100917431 |
| Hong Kong | Aa3 | 0.007334174311926606 |
| Hungary | Baa2 | 0.023296788990825688 |
| Iceland | A2 | 0.010354128440366973 |
| India | Baa3 | 0.026891972477064225 |
| Indonesia | Baa2 | 0.023296788990825688 |
| Iran | NR | 0.0550782110091743 |
| Iraq | Caa1 | 0.09174908256880734 |
| Ireland | A1 | 0.008628440366972478 |
| Isle of Man | Aa3 | 0.007334174311926606 |
| Israel | A1 | 0.008628440366972478 |
| Italy | Baa3 | 0.026891972477064225 |
| Jamaica | B2 | 0.06730183486238533 |
| Japan | A1 | 0.008628440366972478 |
| Jersey (States of) | Aaa | 0 |
| Jordan | B1 | 0.05507821100917431 |
| Kazakhstan | Baa2 | 0.023296788990825688 |
| Kenya | B2 | 0.06730183486238533 |
| Korea | Aa2 | 0.006039908256880735 |
| Korea, D.P.R. | NR | 0.14682729357798163 |
| Kuwait | A1 | 0.008628440366972478 |
| Kyrgyzstan | B3 | 0.07952545871559634 |
| Laos | Caa3 | 0.12238004587155965 |
| Latvia | A3 | 0.014668348623853212 |
| Lebanon | C | 0.175 |
| Liberia | NR | 0.11015642201834863 |
| Libya | NR | 0.036814678899082576 |
| Liechtenstein | Aaa | 0 |
| Lithuania | A2 | 0.010354128440366973 |
| Luxembourg | Aaa | 0 |
| Macao | Aa3 | 0.007334174311926606 |
| Macedonia | Ba3 | 0.04400504587155964 |
| Madagascar | NR | 0.07952545871559634 |
| Malawi | NR | 0.14682729357798163 |
| Malaysia | A3 | 0.014668348623853212 |
| Maldives | Caa1 | 0.09174908256880734 |
| Mali | Caa2 | 0.11015642201834862 |
| Malta | A2 | 0.010354128440366973 |
| Mauritius | Baa3 | 0.026891972477064225 |
| Mexico | Baa2 | 0.023296788990825688 |
| Moldova | B3 | 0.07952545871559634 |
| Mongolia | B3 | 0.07952545871559634 |
| Montenegro | B1 | 0.05507821100917431 |
| Montserrat | Baa3 | 0.026891972477064225 |
| Morocco | Ba1 | 0.030630963302752296 |
| Mozambique | Caa2 | 0.11015642201834862 |
| Myanmar | NR | 0.12238004587155965 |
| Namibia | B1 | 0.05507821100917431 |
| Netherlands | Aaa | 0 |
| New Zealand | Aaa | 0 |
| Nicaragua | B3 | 0.07952545871559634 |
| Niger | B3 | 0.07952545871559634 |
| Nigeria | B3 | 0.07952545871559634 |
| Norway | Aaa | 0 |
| Oman | Ba3 | 0.04400504587155964 |
| Pakistan | Caa1 | 0.09174908256880734 |
| Panama | Baa2 | 0.023296788990825688 |
| Papua New Guinea | B2 | 0.06730183486238533 |
| Paraguay | Ba1 | 0.030630963302752296 |
| Peru | Baa1 | 0.019557798165137613 |
| Philippines | Baa2 | 0.023296788990825688 |
| Poland | A2 | 0.010354128440366973 |
| Portugal | Baa2 | 0.023296788990825688 |
| Qatar | Aa3 | 0.007334174311926606 |
| Ras Al Khaimah (Emirate of) | A3 | 0.014668348623853212 |
| Romania | Baa3 | 0.026891972477064225 |
| Russia | Caa1 | 0.09174908256880734 |
| Rwanda | B2 | 0.06730183486238533 |
| Saudi Arabia | A1 | 0.008628440366972478 |
| Senegal | Ba3 | 0.04400504587155964 |
| Serbia | Ba2 | 0.03681467889908257 |
| Sharjah | Ba1 | 0.030630963302752296 |
| Sierra Leone | NR | 0.14682729357798163 |
| Singapore | Aaa | 0 |
| Slovakia | A2 | 0.010354128440366973 |
| Slovenia | A3 | 0.014668348623853212 |
| Solomon Islands | Caa1 | 0.09174908256880734 |
| Somalia | NR | 0.14682729357798163 |
| South Africa | Ba2 | 0.03681467889908257 |
| Spain | Baa1 | 0.019557798165137613 |
| Sri Lanka | Ca | 0.14682729357798166 |
| St. Maarten | Ba2 | 0.03681467889908257 |
| St. Vincent & the Grenadines | B3 | 0.07952545871559634 |
| Sudan | NR | 0.17499999999999996 |
| Suriname | Caa3 | 0.12238004587155965 |
| Swaziland | B3 | 0.07952545871559634 |
| Sweden | Aaa | 0 |
| Switzerland | Aaa | 0 |
| Syria | NR | 0.17499999999999996 |
| Taiwan | Aa3 | 0.007334174311926606 |
| Tajikistan | B3 | 0.07952545871559634 |
| Tanzania | B2 | 0.06730183486238533 |
| Thailand | Baa1 | 0.019557798165137613 |
| Togo | B3 | 0.07952545871559634 |
| Trinidad and Tobago | Ba2 | 0.03681467889908257 |
| Tunisia | Caa1 | 0.09174908256880734 |
| Turkey | B3 | 0.07952545871559634 |
| Turks and Caicos Islands | Baa1 | 0.019557798165137613 |
| Uganda | B2 | 0.06730183486238533 |
| Ukraine | Caa3 | 0.12238004587155965 |
| United Arab Emirates | Aa2 | 0.006039908256880735 |
| United Kingdom | Aa3 | 0.007334174311926606 |
| United States | Aaa | 0 |
| Uruguay | Baa2 | 0.023296788990825688 |
| Uzbekistan | B1 | 0.05507821100917431 |
| Venezuela | C | 0.175 |
| Vietnam | Ba2 | 0.03681467889908257 |
| Yemen, Republic | NR | 0.17499999999999996 |
| Zambia | Ca | 0.14682729357798166 |
| Zimbabwe | NR | 0.09174908256880734 |
| Region | Weighted Average: ERP | Weighted Average: Default Spreads |
| Africa | 0.1507584248080814 | 0.06830904895845899 |
| Asia | 0.07368154663395052 | 0.013668800788686953 |
| Australia & New Zealand | 0.054400016642806436 | 1.179818248697996e-08 |
| Caribbean | 0.16630442097799 | 0.07932969625103738 |
| Central and South America | 0.12005674061025501 | 0.04654444609001751 |
| Eastern Europe & Russia | 0.1323209821291211 | 0.05523863838321001 |
| Middle East | 0.07946247554970726 | 0.017766934990427034 |
| North America | 0.0544 | 0 |
| Western Europe | 0.06946878889206058 | 0.010682352271974054 |
| Global | 0.07483302726688038 | 0.01448509212061963 |

## Industry Averages(US)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 58 | 0.1816695238095238 | 0.10617104930138777 | 0.3662007137757841 | 0.2471286786756691 | 1.3458926691301203 | 1.6317380595347237 | 0.1357252407363626 | 0.5272211445533301 | 0.058800000000000005 | 0.3102922425013758 | 0.10729463931854823 | 3.512608304846977 | 1.962344118097263 | 10.360206985338735 | 17.03323375019978 | 4.586086438436397 | 13.993381837579332 | 0.03141449120879309 | 0.035092407254195046 | 0.017750375959909692 | 0.5552666934840239 | 0.13567415534535524 | 0.676333683553441 | 0.676333683553441 | 0.11135468081206297 |
| Aerospace/Defense | 77 | 0.03992255813953487 | 0.08635403832710994 | 0.15249479884885908 | 0.1651470921779243 | 1.2292962090923658 | 1.414182280259186 | 0.12280242744739564 | 0.3755554495377183 | 0.055 | 0.2067088360715109 | 0.10594482009093814 | 1.8653814845726677 | 2.545107584189468 | 14.590340622882026 | 23.97611514164623 | 4.9344353649769275 | 53.68599931349899 | 0.46912992617043536 | 0.0291314970360018 | 0.006276938395963106 | 0.32747182434374533 | 0.09872588082604772 | 0.7069683668685915 | 0.7069683668685915 | 0.08921531385841867 |
| Air Transport | 21 | 0.022412499999999995 | 0.02112454674491141 | 0.03075109258968068 | 0.3599305643296216 | 0.6939980034393283 | 1.4159650876966507 | 0.12290832620918106 | 0.37727498727802966 | 0.055 | 0.6507579595971008 | 0.06976852046117993 | 1.601522515617954 | 1.0151710556389202 | 9.393728081856844 | 47.45014363707215 | 2.735341481815569 | 71.79390747675272 | 0.010475454736403853 | 0.0916526424186832 | 0.04028620680068708 | 2.099340473681085 | -0.11368810625736339 | 0 | 0 | 0.02138359154860849 |
| Apparel | 39 | 0.05835695652173913 | 0.10161425283086532 | 0.20566758390991585 | 0.20508511458335257 | 1.0163797426008965 | 1.3246974025641622 | 0.11748702571231125 | 0.38508746928890447 | 0.055 | 0.3402490695982089 | 0.09154744864476262 | 2.1037931987292 | 1.1592906024030611 | 7.021999822290446 | 10.381787550219668 | 2.420558868970722 | 13.804567941679538 | 0.26207135646756324 | 0.022325046445097148 | 0.015269741052495196 | 1.1025108153914758 | 0.13522490180674987 | 0.543158964702381 | 0.543158964702381 | 0.11113035634210841 |
| Auto & Truck | 31 | 0.280595 | 0.06432595910665025 | 0.06461347054513161 | 0.10579107985442861 | 1.2255318343171395 | 1.5405976750533805 | 0.1303115018981708 | 0.5261412487524837 | 0.058800000000000005 | 0.3341810706289511 | 0.10150124989331025 | 0.9452866486358166 | 1.8115110523190732 | 12.745223056693563 | 27.01546905986054 | 2.9173208877532226 | 10.303473979252582 | -0.002638232462945013 | 0.08322654687306077 | 0.04634395309466842 | 0.8908302745493875 | 0.15677154224933043 | 0.10549811796720597 | 0.10549811796720598 | 0.0702992355351022 |
| Auto Parts | 37 | 0.07074333333333332 | 0.05064354320086486 | 0.10259465039163591 | 0.2155946221992605 | 1.202436458457679 | 1.4739918130238336 | 0.12635511369361574 | 0.39519394771296495 | 0.055 | 0.29901008239034443 | 0.10090782663624806 | 1.9747050886050657 | 0.8227724278495656 | 7.179627117821992 | 14.540547974540397 | 1.8900634744418994 | 31.628193367611757 | 0.16055172230589412 | 0.03613112947785673 | 0.036695997763959105 | 1.6270607086056388 | 0.07033878015608527 | 0.3713952123895747 | 0.37139521238957474 | 0.0567775618858974 |
| Bank (Money Center) | 7 | 0.0194 | 0 | 0.00026445657070231255 | 0.17163347967737153 | 0.7393414305916117 | 1.0801015876287672 | 0.10295803430514877 | 0.19594323414619666 | 0.0473 | 0.683929164378137 | 0.05680441904312722 | 0.31756087167554575 | 4.494934562083074 | NA | NA | 0.9875553994107819 | 9.516543910327655 | NA | 0.013070339707981026 | 0.013070339707981026 | -128.48607336966558 | 0.11345074325185552 | 0.2836234354829657 | 0.28362343548296565 | 0.0009943950271997593 |
| Banks (Regional) | 557 | 0.11019711409395982 | 2.692633514771359e-08 | -0.0003681163159071202 | 0.2105476592348194 | 0.4129806383970706 | 0.5048742347564779 | 0.0687895295445348 | 0.16758082918349013 | 0.0473 | 0.3925396989484301 | 0.055712254146514525 | 0.46900063005241044 | 4.343621303282799 | NA | NA | 1.236699810286065 | 24.60127993387343 | NA | 0.029363729443897247 | -0.043451691210799066 | NA | 0.11799058812595946 | 0.2910721262501414 | 0.29107212625014145 | -0.0009670777155914957 |
| Beverage (Alcoholic) | 23 | 0.12543749999999998 | 0.20062785390172486 | 0.14657661188814805 | 0.34926041014564846 | 0.8807822917633785 | 1.0129742331996445 | 0.09897066945205889 | 0.4987467644298934 | 0.055 | 0.18639448485009497 | 0.08821185500433976 | 0.8020000732465785 | 4.071342816847094 | 15.905118508516384 | 20.15187932703732 | 3.1924325323981106 | 111.50158955717302 | 0.15335977242937937 | 0.07876355015613064 | 0.056799689637347855 | 0.5682188940381574 | 0.052846235851230244 | 0.7900316485210999 | 0.7900316485210999 | 0.20171280627414753 |
| Beverage (Soft) | 31 | 0.15048545454545456 | 0.19036999167153545 | 0.2871936673456856 | 0.18187508793156812 | 1.2014134916712005 | 1.3034433070435496 | 0.11622453243838685 | 0.41717146856964005 | 0.055 | 0.1324643982229776 | 0.10629307611688682 | 1.6029900764895542 | 4.666857342578456 | 20.008347527759813 | 24.137168786878842 | 8.227273676625366 | 39.5525944806275 | -0.09057656493088537 | 0.0466213190425338 | 0.056771639556521265 | 0.29140445421199807 | 0.31944669288621974 | 0.5651658752736757 | 0.5651658752736757 | 0.1914400730665588 |
| Broadcasting | 26 | 0.19544111111111115 | 0.1457512346683704 | 0.13517156563045288 | 0.21951773068864888 | 0.7021599591713337 | 1.322058642547223 | 0.11733028336730504 | 0.468984145587513 | 0.055 | 0.5948662688389924 | 0.07207268906838304 | 1.088218556042584 | 1.327352847501104 | 6.551963052409365 | 8.98424931771724 | 0.8817652483888191 | 6.93318863344397 | 0.10620894391959061 | 0.024926670267360996 | 0.0254680025404599 | 2.1013859237709163 | 0.20758583832448124 | 0.14361734100768372 | 0.14361734100768375 | 0.1474621069628176 |
| Brokerage & Investment Banking | 30 | 0.1422875 | 0.004089649281098402 | 0.0005645094247926231 | 0.20823984488924394 | 0.6937505627531657 | 1.2048082896180194 | 0.11036561240331036 | 0.2799624925624301 | 0.055 | 0.6678715351103847 | 0.06420526224741713 | 0.26390729940029073 | 4.458461423368311 | NA | NA | 1.6222402453644245 | 15.398825088840153 | NA | 0.03805697985708237 | 0.025052525387016997 | -106.71129131280301 | 0.13433666755237328 | 0.2868814096660765 | 0.28688140966607656 | 0.0026196985508719333 |
| Building Materials | 45 | 0.10597500000000004 | 0.13807573680826582 | 0.3459620341330455 | 0.22045577488665988 | 1.0983592603350816 | 1.277280094823728 | 0.11467043763252945 | 0.2918991384716212 | 0.055 | 0.22436251520240177 | 0.09819764357803407 | 2.9646568034688325 | 1.3599831051822802 | 7.849544737270424 | 9.7338715959223 | 3.189256369070784 | 15.731797108797148 | 0.1821289295553649 | 0.024582389713126325 | 0.0467874260762279 | 0.7299170025386822 | 0.32728776839603557 | 0.1295396387669115 | 0.12953963876691144 | 0.13998849891511717 |
| Business & Consumer Services | 164 | 0.0846428 | 0.09028385981048767 | 0.23990816674375973 | 0.22537233164821857 | 1.0198687734730703 | 1.1709200204529924 | 0.10835264921490775 | 0.4578249370970681 | 0.055 | 0.21552515508878373 | 0.09389034033599651 | 2.8046731724829046 | 2.0548295737776865 | 13.17826726900874 | 21.791313120550598 | 3.9002335521700227 | 33.71993975794946 | 0.13038697382193254 | 0.02842130096609692 | 0.05718756127720386 | 1.0203838316554499 | 0.12850428149482823 | 0.28225571869971045 | 0.28225571869971045 | 0.09423121049915897 |
| Cable TV | 10 | 0.20048888888888888 | 0.1989566188928557 | 0.12126078877676111 | 0.29816727963168077 | 0.7059202442851957 | 1.2551641961018303 | 0.11335675324844872 | 0.25406917505650006 | 0.055 | 0.5175278387670518 | 0.07603950107926996 | 0.7954872209511412 | 2.4271351695921024 | 7.388341366320442 | 12.434965607445452 | 2.0421096097889047 | 11.031811598705742 | 0.005934431800706669 | 0.11049608575165179 | -0.004865584877609428 | 0.015184488206219843 | 0.12137565446376083 | 0.2905065908357078 | 0.29050659083570785 | 0.19527628887738516 |
| Chemical (Basic) | 38 | 0.2702 | 0.1305339104740846 | 0.25379383032265024 | 0.2096660776140613 | 0.9589900308465779 | 1.2471014770997904 | 0.11287782773972756 | 0.4657900442175986 | 0.055 | 0.3256937459356132 | 0.08954909220994486 | 2.140539561734049 | 0.8879906828603437 | 4.918862714929454 | 6.658556646699511 | 1.9406925746228572 | 9.950772082530245 | 0.13501869928478144 | 0.046946155965922734 | 0.052585156771289575 | 0.5855153966288552 | 0.34777022369023014 | 0.27395285947542003 | 0.27395285947542003 | 0.13148514278842838 |
| Chemical (Diversified) | 4 | 0.017524999999999995 | 0.13516371228768437 | 0.20349837596065587 | 0.17552757581131406 | 1.0902565654988166 | 1.4125912305600932 | 0.12270791909526954 | 0.3949317614003628 | 0.055 | 0.36805699288839216 | 0.09272676234611871 | 1.696073044152786 | 0.910381123993981 | 5.015717861470585 | 6.7070116425908575 | 1.8892572990056375 | 4.913635036652967 | 0.14468858429825437 | 0.03796293491355908 | 0.0004090535190393897 | 0.23180043531608446 | 0.43436231081579907 | 0.14606681893025975 | 0.14606681893025975 | 0.13629282750850893 |
| Chemical (Specialty) | 76 | 0.09482244897959184 | 0.14620994370453144 | 0.17826252008578738 | 0.21518437900478904 | 1.1152530501630955 | 1.2772947079305697 | 0.11467130565107583 | 0.4232046909214356 | 0.055 | 0.21509733288408953 | 0.0988785786286619 | 1.300382837279803 | 2.478483344687263 | 10.530080416847145 | 16.533152933135522 | 2.8296016487864555 | 34.72552764602949 | 0.22710714698009443 | 0.0592701889883797 | 0.06215548918095831 | 0.9187162005119015 | 0.11428570397103884 | 0.4046247565327966 | 0.4046247565327966 | 0.1529991140262301 |
| Coal & Related Energy | 19 | -0.03714899999999999 | 0.22154519636476394 | 0.417859281998402 | 0.057877792248144 | 1.4289145880963197 | 1.45217888188087 | 0.12505942558372368 | 0.6195673940499934 | 0.058800000000000005 | 0.1783669702738898 | 0.11061893812724044 | 1.914464970928417 | 1.4317347621068663 | 3.8137225981171055 | 5.313497891800048 | 2.45757981722153 | 70.10021734645936 | 0.07193329766827207 | 0.06654469909067097 | 0.01340816712569722 | 0.16330024899958975 | 0.7408390302523333 | 0.20433717791215913 | 0.2043371779121591 | 0.2233108579995417 |
| Computer Services | 80 | 0.10479307692307695 | 0.06572484141188979 | 0.28393181700102466 | 0.20902109276047354 | 0.9932217950326541 | 1.1713869322889647 | 0.10838038377796451 | 0.47775300169020696 | 0.055 | 0.24564199162920453 | 0.09189034260791246 | 4.362127057694285 | 1.1705516509622818 | 10.563161623441127 | 16.723392422877364 | 4.03272970946335 | 16.826618008820372 | 0.15591437376823686 | 0.01229709556092224 | -0.002207438701758182 | 0.3065729494563137 | 0.12149230128546304 | 0.9358278527691721 | 0.9358278527691721 | 0.06954770331174166 |
| Computers/Peripherals | 42 | 0.16357148148148148 | 0.21409567860908393 | 0.42627570781813673 | 0.16701412664987517 | 1.227042372213005 | 1.2910863648381774 | 0.11549053007138774 | 0.48725444355956743 | 0.055 | 0.08694726327018577 | 0.10903551915795263 | 2.12396319511638 | 3.667515447858306 | 14.733525349856887 | 17.080897524012034 | 25.561397089337795 | 60.37198607537146 | -0.08761785669500524 | 0.030428476782541368 | 0.01816023975440227 | 0.0627499738738938 | 0.9626017835927464 | 0.16947356652480433 | 0.1694735665248044 | 0.22026534167026365 |
| Construction Supplies | 49 | 0.05016781250000001 | 0.1113211314713254 | 0.1454747413376444 | 0.21149094625947643 | 1.0760610533922743 | 1.264396002860222 | 0.11390512256989718 | 0.3511164528388211 | 0.055 | 0.23151570788836295 | 0.09708432043641166 | 1.4171828125823143 | 2.149130072951404 | 12.934160671927692 | 18.74940900566638 | 3.6559134287335295 | 23.67017657790564 | 0.20313324960220644 | 0.05343245722428593 | 0.06039717544139717 | 1.1390269734410299 | 0.18776605314361972 | 0.3215565201312873 | 0.3215565201312873 | 0.11439331049245301 |
| Diversified | 23 | 0.07692 | 0.0344185411414363 | 0.028451413775521742 | 0.15969215649818055 | 0.9394964138236339 | 1.0382284747790869 | 0.10047077140187777 | 0.5784443873074648 | 0.058800000000000005 | 0.17516637526737888 | 0.09059650770438482 | 0.8091355852203166 | 2.497073337847707 | 30.95510954380436 | 69.44109385976469 | 1.8458984878571658 | 14.458344682654587 | 0.07613974462511099 | 0.04250139388832482 | 0.0276219002205922 | 1.7018968838721764 | 0.008249600127117764 | 1.5067793894620867 | 1.5067793894620867 | 0.03623278335047383 |
| Drugs (Biotechnology) | 598 | 0.27230353658536566 | 0.12018971566330637 | 0.06493048690162403 | 0.1425123298573789 | 1.1994489579084946 | 1.2417422800706084 | 0.11255949143619413 | 0.5841409330821086 | 0.058800000000000005 | 0.13285422647907655 | 0.10346435865628759 | 0.4588572593717011 | 6.184837468966433 | 11.029260692823163 | 40.682421818847885 | 5.800972165849432 | 113.80317420122032 | 0.12996962084632474 | 0.03558353907764804 | -0.00020551912434212563 | 0.40999126936273844 | 0.006775907836833162 | 0.0005691925454312509 | 0.0005691925454311964 | 0.142616457040632 |
| Drugs (Pharmaceutical) | 281 | 0.4234563380281691 | 0.27387480126192115 | 0.19583591126440983 | 0.12152173885442238 | 1.1808060946282533 | 1.2680061555196915 | 0.11411956563786968 | 0.6488355395045173 | 0.058800000000000005 | 0.11983897594961615 | 0.10572849259539045 | 0.7538683006298992 | 4.8507972602124285 | 12.336746475080462 | 17.37496592242517 | 5.2822318741793906 | 17.765653282813773 | 0.19448863395055158 | 0.04544449745943131 | 0.027328938551878745 | 0.23314422056482276 | 0.24540189875584534 | 0.5136008017948664 | 0.5136008017948664 | 0.26627225481310235 |
| Education | 33 | 0.041291875000000006 | 0.052763116719378576 | 0.06774187060273272 | 0.28828758577666874 | 0.9937160802737702 | 1.1008288893194806 | 0.10418923602557716 | 0.41812601855058806 | 0.055 | 0.23436430724796883 | 0.08943852557572636 | 1.2400892015686051 | 1.8499312364405511 | 9.650215665864085 | 30.359718234591035 | 1.81380698120419 | 18.213402559297673 | 0.07957505660234288 | 0.03209320302203601 | 0.092404200428599 | 3.5636046330701983 | 0.03190071456829195 | 0.17439258095206728 | 0.17439258095206722 | 0.058289255738509536 |
| Electrical Equipment | 110 | 0.138975 | 0.09966773470320654 | 0.1840328456371863 | 0.20103829040431295 | 1.4326548798323873 | 1.5896686619511227 | 0.1332263185198967 | 0.5855485943663449 | 0.058800000000000005 | 0.18379271640117503 | 0.11684555033628852 | 1.784175397261031 | 2.7669115666624866 | 12.687782652021538 | 22.71778994473753 | 3.131143964049657 | 50.35024785167854 | 0.25546598517273594 | 0.052685242562635834 | 0.14996801054437855 | 2.7928575511304214 | 0.13203099340958588 | 0.3446045463329263 | 0.34460454633292636 | 0.10772663000105302 |
| Electronics (Consumer & Office) | 16 | -0.004729999999999997 | 0.018532970035645514 | 0.05463891445559998 | 0.10064883323847465 | 1.6130596990178139 | 1.538919124088938 | 0.13021179597088292 | 0.3956471324501661 | 0.055 | 0.14129490331068803 | 0.11764194761083187 | 2.2252934810205893 | 0.7762903101485829 | 10.434016718178196 | 27.82775567194643 | 1.8651208939219588 | 78.60622134012917 | 0.13681325152347834 | 0.01371020423662633 | 0.024097951690066212 | 4.482980469573045 | 0.012750302661478806 | 0 | 0 | 0.025394437421319454 |
| Electronics (General) | 138 | 0.106349294117647 | 0.0973606008204959 | 0.17474664762348024 | 0.1899944205243292 | 1.1161632606240839 | 1.2012527647557136 | 0.11015441422648939 | 0.449375866701406 | 0.055 | 0.15835752834031197 | 0.0992428814978455 | 1.8293533131914423 | 1.9376194589256814 | 11.91629375511652 | 19.249574240444776 | 3.0614854022412756 | 58.252171064461706 | 0.22422007253520718 | 0.04529483333663775 | 0.13580448309031176 | 2.234127969038666 | 0.12417520019293474 | 0.10608878216021826 | 0.10608878216021822 | 0.10170714884999767 |
| Engineering/Construction | 43 | 0.12138344827586202 | 0.04422234908722617 | 0.1383462171293748 | 0.22883380517568075 | 1.0176246718468016 | 1.1967640138319908 | 0.10988778242162026 | 0.3516684814395371 | 0.055 | 0.24007634301961103 | 0.09340947462486192 | 3.398853205223256 | 1.083075588028985 | 13.169580718377542 | 22.98728031850993 | 2.8181860701948733 | 29.062594674781394 | 0.2001452260073408 | 0.031165438708910063 | 0.0792501681739788 | 3.007830882148567 | 0.07495788208319021 | 0.16885746296448992 | 0.1688574629644899 | 0.04693760148613017 |
| Entertainment | 110 | 0.28593124999999997 | 0.07512458188433216 | 0.11234825527684747 | 0.21094506563113774 | 1.2462224080092748 | 1.4497950169593838 | 0.1249178240073874 | 0.578095571351251 | 0.058800000000000005 | 0.24970269532215986 | 0.1047373955226708 | 1.4645754612679325 | 3.0598123732084623 | 17.462187520735604 | 39.95907149942788 | 2.224931360853785 | 47.736718632185095 | 0.04191818235094667 | 0.044160033252208485 | -0.004979303346952369 | 0.04050024890613391 | 0.011812232323271436 | 0.504205300396235 | 0.504205300396235 | 0.07927768866245001 |
| Environmental & Waste Services | 62 | 0.10134039999999998 | 0.1259444829111092 | 0.28322287490094245 | 0.22114200170438975 | 0.8591109527629267 | 1.0153454106826958 | 0.09911151739455212 | 0.48087346767746236 | 0.055 | 0.20341883913216277 | 0.08734139469572688 | 2.3308722386849454 | 3.0346407791089263 | 14.022412125338205 | 23.388429760710196 | 5.292040895164843 | 76.98730729392803 | 0.10044659986151996 | 0.0791397272675094 | 0.09628471466477503 | 1.1007779432771518 | 0.16473874687290124 | 0.46259054584477655 | 0.46259054584477655 | 0.1284742274005583 |
| Farming/Agriculture | 39 | 0.17570944444444442 | 0.07621590723204641 | 0.15172833554504575 | 0.20033571011302 | 0.9310497068082925 | 1.1403135761675725 | 0.10653462642435381 | 0.5442670958617369 | 0.058800000000000005 | 0.25298812315410507 | 0.09073940746542884 | 2.051776568615021 | 1.2248382413417702 | 12.60893108246012 | 15.581328911598986 | 3.4691348828249016 | 22.12057113620223 | 0.1482856605674927 | 0.029070036355784076 | 0.03335753597775123 | 1.4678368468897955 | 0.23648187908031001 | 0.21028238912969796 | 0.210282389129698 | 0.07911455499645086 |
| Financial Svcs. (Non-bank & Insurance) | 223 | 0.1044040579710145 | 0.1588822815855376 | 0.006537565294637276 | 0.2088068946745798 | 0.10617474510192053 | 0.8857250736377152 | 0.09141206937408028 | 0.2714530650370676 | 0.055 | 0.9094527962519532 | 0.04579203511603851 | 0.04716792489213012 | 23.486787015859328 | 91.88027150796391 | 90.63053658376812 | 1.6875081521756248 | 32.69630059854332 | NA | 0.025335116701238395 | 0.036372628687447776 | 0.2184817075557922 | 0.48075065014765694 | 0.1364873346721653 | 0.13648733467216534 | 0.16180683625994385 |
| Food Processing | 92 | 0.2521022448979591 | 0.11768965472306084 | 0.1859935447135467 | 0.19895740390789407 | 0.7686726756486479 | 0.9175202331173958 | 0.09330070184717332 | 0.3422878341543323 | 0.055 | 0.22395116431995885 | 0.08164388656482782 | 1.6859815207716935 | 2.099541082262578 | 13.24274225046033 | 17.401340165255593 | 2.6065242636797277 | 52.47444886536464 | 0.06761507012216998 | 0.03702154235562431 | 0.03712651759254365 | 0.5754372131132566 | 0.11538895815608002 | 0.5377905934476894 | 0.5377905934476894 | 0.11955369864953631 |
| Food Wholesalers | 14 | 0.09836 | 0.02102412449953486 | 0.15535644943181512 | 0.22254279669167149 | 0.8457047174503761 | 1.1237058272854066 | 0.10554812614075315 | 0.32418308733551454 | 0.055 | 0.31580170522329504 | 0.08524266826284077 | 8.411641325622437 | 0.41461800975807755 | 12.015914836847594 | 19.708268616623734 | 4.536016224851112 | 25.137922065338433 | 0.06342789548322521 | 0.008295079189244195 | 0.009034874257437216 | 1.2945984195977063 | 0.1898419988361979 | 0.43594516376534403 | 0.435945163765344 | 0.0209727955809301 |
| Furn/Home Furnishings | 32 | 0.14448380952380954 | 0.0765936312548692 | 0.15236680821065973 | 0.32782325118771566 | 0.9519122322245162 | 1.2708955631991046 | 0.11429119645402681 | 0.41911842205905825 | 0.055 | 0.3587120935375829 | 0.08809043595951298 | 2.1902364409373862 | 0.8793552411057327 | 6.283919020064695 | 10.046127129844884 | 1.822770795533889 | 14.03013265423464 | 0.15842212845958345 | 0.038007682752639126 | 0.03800411098909126 | 1.506522341669401 | 0.05446456547577848 | 0.6801970152211083 | 0.6801970152211083 | 0.07956088078382309 |
| Green & Renewable Energy | 19 | -0.14713666666666667 | 0.260956619525612 | 0.046816390058494056 | 0.1404424588963212 | 0.8771923185242169 | 1.60070111091836 | 0.13388164598855057 | 0.6759835919999633 | 0.0701 | 0.5477495182317988 | 0.08934596981927857 | 0.20539294157771462 | 7.785269341085777 | 12.701231489743156 | 31.282179206839263 | 1.0789864566845957 | 34.62057492244528 | -0.6111278234342038 | 0.4595700708746041 | 0.26912402409773456 | 1.5839659027786925 | 0.18266048315237854 | 0.5684766460827907 | 0.5684766460827907 | 0.24440548669537576 |
| Healthcare Products | 254 | 0.19900759398496237 | 0.15015238491328653 | 0.15878607397399988 | 0.15498161973077781 | 1.0971029719882097 | 1.1623831948690986 | 0.10784556177522446 | 0.5094012253760996 | 0.058800000000000005 | 0.11192266952101866 | 0.10071098833122433 | 1.0339137994093208 | 5.15284829263527 | 19.089978627201564 | 32.02458868945606 | 4.701218047051161 | 62.958973741822945 | 0.2449164318011062 | 0.04857766527009542 | 0.125937345585974 | 1.293067295649264 | 0.07091922967824961 | 0.4613141074361804 | 0.4613141074361804 | 0.15917088171556376 |
| Healthcare Support Services | 131 | 0.20156749999999996 | 0.04071525759889633 | 0.3378630108253928 | 0.22031799938817112 | 1.0725471879998554 | 1.1603652760592904 | 0.10772569739792186 | 0.47792508451312243 | 0.055 | 0.19097410804999704 | 0.09503056038035224 | 9.025276930735776 | 0.6887289455148623 | 12.16043752366125 | 16.77624757149482 | 3.6006610530276073 | 45.90801455210623 | -0.07140259802805697 | 0.007325658993960622 | 0.008021346789135277 | 0.3034022713232111 | 0.12337379962692853 | 0.33042108015587673 | 0.3304210801558767 | 0.04013336124322542 |
| Heathcare Information and Technology | 138 | 0.2045203508771929 | 0.1693154514439247 | 0.19103562594036017 | 0.15820736589386364 | 1.370736187816319 | 1.4715094541215377 | 0.12620766157481933 | 0.5387173762249065 | 0.058800000000000005 | 0.12440570020083286 | 0.11599300044475092 | 1.1333037378180726 | 5.332529419023302 | 19.362951181106027 | 30.48594494927957 | 4.326155333149176 | 48.341137501288586 | 0.22486925050519696 | 0.04913593435626128 | 0.14769419579728138 | 1.2967985907886859 | -0.0028789813310332304 | 0.0004328283318266802 | 0.00043282833182667346 | 0.17588409101918592 |
| Homebuilding | 32 | 0.15822272727272732 | 0.18763159239110155 | 0.28173702467387046 | 0.23124619223292053 | 1.3331558308257836 | 1.5022071383659328 | 0.12803110401893641 | 0.3333038712963018 | 0.055 | 0.2443462078673053 | 0.10682647033737112 | 1.8239578402915135 | 0.8528638431421254 | 4.389062015208314 | 4.536403127639891 | 1.2863359814095505 | 5.0845371401835715 | 0.6325462143933341 | 0.005094344658519622 | 0.013602387991019798 | 0.6995946775077 | 0.3074751070897314 | 0.05448602499635796 | 0.05448602499635791 | 0.18794668320617053 |
| Hospitals/Healthcare Facilities | 34 | 0.01596736842105263 | 0.11615164232145252 | 0.20452836690892628 | 0.24113534072653886 | 0.7230794758104835 | 1.174001444953803 | 0.1085356858302559 | 0.5119442326502478 | 0.058800000000000005 | 0.46591874206509154 | 0.07851389214412163 | 1.946046908415305 | 1.5690399443104104 | 8.704398867518197 | 13.48218533002113 | 5.326270915466297 | 105.59442613995225 | 0.10445838743236993 | 0.06032948905550597 | 0.03632154631162509 | 0.6344228696504937 | 0.49037665345444303 | 0.13557220326973293 | 0.13557220326973296 | 0.11620573950103597 |
| Hotel/Gaming | 69 | 0.07584189189189189 | 0.0724911355698957 | 0.02338560835877878 | 0.23845423964291163 | 1.0609649277632753 | 1.4599765370156599 | 0.1255226062987302 | 0.38051359185436157 | 0.055 | 0.3996777803163692 | 0.09184071807177843 | 0.6478703943188595 | 4.20490472712404 | 15.187616716813173 | 82.57716395932685 | 6.773130036537119 | 17.546856842427747 | 0.07508768954208403 | 0.08078588826260018 | 0.04549090287993243 | 2.5582638357878977 | 0.025319429359336565 | 0.49425325285811983 | 0.49425325285811983 | 0.03954292109035511 |
| Household Products | 127 | 0.11551042553191491 | 0.16990919421137413 | 0.34916245427993664 | 0.2015988668185506 | 1.0578798468783357 | 1.1550009836175177 | 0.10740705842688056 | 0.568275249431107 | 0.058800000000000005 | 0.13437882331900164 | 0.09889993040768906 | 2.1854467010901835 | 3.6464203371631907 | 16.847339181418562 | 21.18720479743272 | 9.167328405354654 | 124.19393691012411 | 0.08557124926849248 | 0.03728403629130116 | 0.021526585003622836 | 0.300869727003317 | 0.3317897030303111 | 0.6369459063855155 | 0.6369459063855155 | 0.17128481786522984 |
| Information Services | 73 | 0.11055135135135132 | 0.24023393261357548 | 0.3288577979075361 | 0.19105010155621463 | 1.3334436182933442 | 1.4047128789332648 | 0.12223994500863593 | 0.4510937058049509 | 0.055 | 0.11550414899232817 | 0.11288527033347798 | 1.5141875230145225 | 6.256562003407964 | 18.38253671001275 | 24.56414806734132 | 5.972964532086621 | 60.49602307155901 | 0.03065770092615278 | 0.029758877206398943 | 0.025448641162149385 | 0.2179440739830361 | 0.17742326258322197 | 0.2807286179718941 | 0.2807286179718941 | 0.24732602294106956 |
| Insurance (General) | 21 | 0.06900909090909091 | 0.2182179716474952 | 0.1930656056607453 | 0.20378651559004954 | 1.0269385936275734 | 1.2277613538599423 | 0.11172902441928058 | 0.4376102850667002 | 0.055 | 0.2336517107244612 | 0.09526147979352459 | 0.984152498699773 | 2.160106830480198 | 7.434275477712832 | 9.807334195718845 | 2.593260482621046 | 213.16752918372785 | 0.024139638910329986 | 0.009147240996291205 | 0.009565126042509914 | 0.6790818991643168 | 0.17429837416489147 | 0.16850456388146776 | 0.16850456388146773 | 0.21860829295850032 |
| Insurance (Life) | 27 | 0.08287000000000001 | 0.08340736731278155 | 0.04828414139506578 | 0.1454871451402842 | 0.6674646710271233 | 0.9393536603143791 | 0.09459760742267412 | 0.28891454530535254 | 0.055 | 0.4802581428121806 | 0.06897698455838734 | 0.6495091917970076 | 1.3252068248279174 | 10.66670958998455 | 12.247740216996728 | 1.7297667448322556 | 16.589451562329984 | 0.16252107176106828 | 0.0015332374828122921 | 0.0023115111588852626 | 0.006787533027391526 | 0.055791645738122134 | 0.38242287811508857 | 0.38242287811508857 | 0.08391171025722444 |
| Insurance (Prop/Cas.) | 51 | 0.03817636363636363 | 0.0640953790830861 | 0.0707619000900866 | 0.19872018013981518 | 0.7295385474975669 | 0.8033013628246957 | 0.08651610095178693 | 0.2766718330726164 | 0.055 | 0.17672400294711046 | 0.07851649439377913 | 1.2235917495745048 | 1.3918409007316568 | 14.615123157002838 | 21.016328286322402 | 2.1991436416927073 | 20.230973091308005 | -0.5111507631245079 | 0.009401377739052872 | 0.005775129413466673 | 0.4890913390928211 | 0.05709867338201454 | 0.7331941199432807 | 0.7331941199432807 | 0.0649235951089916 |
| Investments & Asset Management | 600 | 0.10789090909090909 | 0.18362934886099308 | 0.09161885851815564 | 0.18201474107993432 | 0.5377530864305458 | 0.6236129544790963 | 0.07584260949605831 | 0.09906426739982557 | 0.0473 | 0.277179353742124 | 0.06465354158382644 | 0.5246132339352295 | 5.164961395127254 | 18.342065712597037 | 22.4431383974077 | 2.128488760779847 | 413.138812929384 | NA | 0.028393720405116826 | 0.0744774085036554 | 0.5986414301068331 | 0.17165541003222293 | 0.42685509300941743 | 0.4268550930094175 | 0.1819226240213684 |
| Machinery | 116 | 0.08504565217391302 | 0.13797099354120126 | 0.2744089522575868 | 0.20984581189172136 | 1.0938250803149925 | 1.224816899432044 | 0.11155412382626342 | 0.32362033573649224 | 0.055 | 0.17247652623442106 | 0.09942831276875491 | 2.1608500691718713 | 2.6683702336166513 | 14.083078687600038 | 18.88916743626743 | 4.057385286241111 | 43.77318575878879 | 0.25954733960836424 | 0.024915916926800095 | 0.10792630698907046 | 1.4023558792324888 | 0.15486472220663997 | 0.3670721468884211 | 0.36707214688842105 | 0.14150866099187387 |
| Metals & Mining | 68 | 0.05883076923076924 | 0.2289052263190132 | 0.3472496988991556 | 0.38407016996119214 | 1.2191906966167014 | 1.2900534643158847 | 0.11542917578036356 | 0.7005623950119386 | 0.0701 | 0.1772589847747572 | 0.10428770839268217 | 1.5847983484975299 | 2.060190198107211 | 6.579397137458955 | 8.854388912836441 | 2.753388524420772 | 17.597890904343 | 0.12050846757809916 | 0.08493077162378138 | 0.023387475892735522 | 0.302541338551599 | 0.21097592151322797 | 0.6250115940632788 | 0.6250115940632788 | 0.22858605943486224 |
| Office Equipment & Services | 16 | 0.1579192857142857 | 0.05943763982424308 | 0.12191063223697689 | 0.2422852760736197 | 0.8448370751926576 | 1.1770946700328646 | 0.10871942339995216 | 0.35220934553840333 | 0.055 | 0.4004847294400365 | 0.08169894962414706 | 2.3804211822459824 | 0.9328859417265536 | 8.44876451690469 | 14.906166393314605 | 2.022459919957329 | 23.352946188547765 | 0.10580064791999493 | 0.023993627737332053 | 0.05735121351327445 | 2.0750554367424625 | 0.07960246716669528 | 0.8295817217255299 | 0.8295817217255299 | 0.06343388016300913 |
| Oil/Gas (Integrated) | 4 | 0.12122499999999999 | 0.17323216393519394 | 0.2237117966538663 | 0.23128677128184674 | 0.946268369906833 | 0.9774858927490678 | 0.09686266202929464 | 0.3054894443464334 | 0.055 | 0.10316970884560783 | 0.09112511987960312 | 1.4955904353767258 | 1.3937972898489077 | 5.732077549878968 | 7.9816868353676975 | 2.2503250646526936 | 6.712316071134506 | 0.0316106162674479 | 0.04806097343178481 | -0.012355711407971395 | -0.10405303090005764 | 0.32415954257527113 | 0.26356755294941536 | 0.26356755294941536 | 0.17441627220965225 |
| Oil/Gas (Production and Exploration) | 174 | 0.2956583720930232 | 0.35545174432146454 | 0.39824340316559603 | 0.20955223008563117 | 1.1361280842130776 | 1.2574315521617736 | 0.11349143419840936 | 0.569768773700139 | 0.058800000000000005 | 0.16724493485833186 | 0.10188606830617017 | 1.1700439551307493 | 2.1191896091279183 | 4.276247542882828 | 5.869301418718809 | 2.4310528245139333 | 20.684944931020116 | -0.03604427736204131 | 0.1885674246152993 | 0.1078629574354029 | 0.4423312916881501 | 0.4700009949859578 | 0.2314686425395253 | 0.23146864253952526 | 0.3567926320359328 |
| Oil/Gas Distribution | 23 | 0.21857272727272728 | 0.10554569736383697 | 0.07175104303163517 | 0.16732223134836754 | 0.656489918658282 | 0.9912553313271651 | 0.09768056668083361 | 0.33549336269635954 | 0.055 | 0.41660661946754163 | 0.07417121906129383 | 0.7120378923813613 | 2.59927331485073 | 11.36460340092179 | 19.40704029518387 | 2.7164260652684495 | 17.52691395432573 | 0.035242294739286945 | 0.07999241280532651 | 0.048183145588975365 | 0.671107517805467 | 0.04093205044691008 | 3.1496776117177885 | 3.1496776117177885 | 0.10823727370000472 |
| Oilfield Svcs/Equip. | 101 | 0.07721338461538461 | 0.07261549102618922 | 0.2808940923374969 | 0.2108326327763118 | 1.1869387038702228 | 1.3751593545688363 | 0.12048446566138887 | 0.4689810733878538 | 0.055 | 0.24587596268608092 | 0.10100261513897765 | 4.098572921606003 | 0.5763594222166393 | 5.898896320620514 | 7.783349750591038 | 2.066860808545039 | 35.47003067427473 | 0.052452832524179795 | 0.01895340439535063 | 0.0028621639869896368 | 0.23846989683692524 | 0.3082104600084224 | 0.17578397726915398 | 0.17578397726915396 | 0.07374653437423348 |
| Packaging & Container | 25 | 0.05901842105263158 | 0.09432619009012708 | 0.1604004979040459 | 0.20377136598084747 | 0.6704997219078969 | 0.9524219969120523 | 0.0953738666165759 | 0.24431384085324004 | 0.0473 | 0.38258512094774455 | 0.0724574514874404 | 1.951780905409734 | 1.2479568457109567 | 8.241799574031862 | 12.954725986412068 | 2.4964229215467095 | 13.232355624196757 | 0.1039753447723231 | 0.05749572425290096 | 0.04428884655379667 | 0.8693917506302825 | 0.19745548981610928 | 0.2864117389608509 | 0.2864117389608509 | 0.09630291291898281 |
| Paper/Forest Products | 7 | 0.06995 | 0.18473924668549113 | 0.4283275094215141 | 0.25797346881174144 | 1.1258403034857074 | 1.3830066711394122 | 0.1209505962656811 | 0.42843597130920175 | 0.055 | 0.30490399792922035 | 0.09664956582693224 | 2.640287423267194 | 0.7744608337917074 | 3.4314540119535057 | 4.160086734865813 | 2.849340156959341 | 12.831132860096082 | 0.07955855971818733 | 0.04840885650461677 | 0.03594806278218337 | 0.37226163421064296 | 0.46826521479713606 | 0.07884048737755833 | 0.07884048737755833 | 0.18593819979693185 |
| Power | 48 | 0.06412690476190475 | 0.15573872218414844 | 0.06042080967715359 | 0.13472676053727245 | 0.4640263901945677 | 0.7250009747102386 | 0.08186505789778817 | 0.1717812350329328 | 0.0473 | 0.43552496662165086 | 0.061661029480277525 | 0.43922516402299394 | 3.7530377133084176 | 12.972637040869596 | 23.94821694902156 | 1.9823980732078421 | 19.07432291850709 | 0.06578724389324328 | 0.2922190210011655 | 0.1839600884056081 | 1.4569117844566188 | 0.09389804277904026 | 0.6055689151540586 | 0.6055689151540586 | 0.1568331369296484 |
| Precious Metals | 74 | 0.03738571428571432 | 0.10026540707071753 | 0.05282254269046003 | 0.4461255940505129 | 1.1872086171220402 | 1.2336190389708566 | 0.11207697091486889 | 0.7254331454586879 | 0.0701 | 0.14034933783922693 | 0.10372590869683809 | 0.5174437684326845 | 3.553152355335159 | 10.884098925641386 | 33.92461158130266 | 1.6758914035578867 | 14.432357858158962 | 0.10747723875647383 | 0.23691578941503644 | 0.06299898965364086 | 1.164825671754932 | 0.03660707162608941 | 1.6036342196424935 | 1.6036342196424935 | 0.10498432937504064 |
| Publishing & Newspapers | 20 | 0.033178571428571425 | 0.07728787314175316 | 0.15253143934703767 | 0.1529815223903639 | 0.9141555268995404 | 1.114895776688169 | 0.10502480913527724 | 0.30919744401282184 | 0.055 | 0.29664827548349576 | 0.08610612198600814 | 2.1495360876073235 | 1.1585137067311873 | 8.396094672232355 | 14.858834219149905 | 1.5796672211897118 | 19.59895929655136 | 0.09878380480674955 | 0.0345280622858652 | 0.06112699934515906 | 1.2037354739181043 | 0.051457490948492286 | 0.5237275948847004 | 0.5237275948847004 | 0.07844877654611533 |
| R.E.I.T. | 223 | 0.09572032432432433 | 0.2546204677399553 | 0.03291953537764929 | 0.042830130197032544 | 0.6855568332302365 | 1.063376043005491 | 0.10196453695452617 | 0.21541532639566627 | 0.0473 | 0.4360730525810025 | 0.07297024161006857 | 0.14684116326248878 | 11.06237876186524 | 19.889516018721697 | 43.36149682247148 | 1.9278379217128667 | 41.48255152493677 | 1.1802755385535975 | 0.030609471497529343 | -0.06957944332379132 | -0.3090305179736722 | 0.08852962680905438 | 1.0779848431093604 | 1.0779848431093604 | 0.23203055634695816 |
| Real Estate (Development) | 18 | 0.10161666666666665 | 0.18643282544436918 | 0.06124687047515737 | 0.22962895460275518 | 0.8838048274406524 | 1.5166924498761216 | 0.12889153152264163 | 0.5125063500210518 | 0.058800000000000005 | 0.529536988685742 | 0.08399127925408982 | 0.37533699252084596 | 2.8074579856808244 | 10.539631090506099 | 15.458491482757813 | 0.9422782431952952 | 10.7244443912679 | 0.06897932766415636 | 0.016656707603486576 | -0.04235974257333449 | -0.5256687632821045 | 0.10514161885746096 | 0 | 0 | 0.17482898999177635 |
| Real Estate (General/Diversified) | 12 | 0.08742 | 0.18574177746675996 | 0.06512491651609979 | 0.22877349119949147 | 0.6649391588559308 | 0.7898029768416497 | 0.08571429682439399 | 0.28661749273612586 | 0.055 | 0.2847886041613258 | 0.07305137179675997 | 0.38625209859805604 | 4.015643823790661 | 14.89079423992054 | 21.390967318368396 | 0.9660094293418295 | 17.526867681340555 | 2.0459245976207137 | 0.018100944716585025 | -0.0003393981805458408 | 0.6677825293193983 | 0.0668111597878718 | 0.3319988956377692 | 0.3319988956377692 | 0.18604180906971937 |
| Real Estate (Operations & Services) | 60 | 0.16003758620689656 | 0.011685762595962912 | 0.010758116120213667 | 0.2022882818442118 | 0.8050206047433183 | 1.3454843302112593 | 0.11872176921454881 | 0.44434220453063733 | 0.055 | 0.5221196650429506 | 0.07827223502196382 | 1.5689215564881624 | 0.9973110120329112 | 8.797146265973787 | 159.94211887150664 | 1.6465144649718912 | 39.80017732507439 | 0.15137872576266614 | 0.011949056366529672 | -0.0009733550346680991 | NA | -0.03576685675209117 | 0.003350886733222865 | 0.003350886733222813 | 0.007128360349921379 |
| Recreation | 57 | 0.07788692307692306 | 0.09187261806584006 | 0.12254941456919057 | 0.20045837235862293 | 1.0754929270701692 | 1.417980944163648 | 0.12302806808332069 | 0.42131153923229786 | 0.055 | 0.34236718555089074 | 0.09502994107384506 | 1.5859899092296037 | 1.7662464800785203 | 9.662279737002965 | 20.26156769140154 | 3.243990223876226 | 18.79714703297693 | 0.18853137911199377 | 0.0631651853574229 | 0.08463375238729509 | 2.4253997212904026 | 0.03952343386952121 | 1.3633798616766255 | 1.3633798616766255 | 0.08515525051509744 |
| Reinsurance | 1 | 0.056299999999999996 | 0.04648442310060338 | 0.052526535195568026 | 0.06482982171799027 | 0.8316073808059627 | 0.8292482034163514 | 0.08805734328293127 | 0.1936761567443839 | 0.0473 | 0.31081382917101813 | 0.07171402382037845 | 1.2102032753146545 | 0.6321626547848161 | 12.075250898524033 | 13.620688310926171 | 2.537189420251136 | 16.516000000000002 | -0.17934983376431474 | 0.001416081763329639 | -0.0035894594261790392 | 0.059152910542786076 | 0.0446255335661622 | 0.34956521739130436 | 0.3495652173913044 | 0.04641194632415979 |
| Restaurant/Dining | 70 | 0.06276761904761904 | 0.15419795499898792 | 0.18384754911547566 | 0.2130288291961474 | 1.1660017105464549 | 1.4103978688180479 | 0.12257763340779204 | 0.41147053391609606 | 0.055 | 0.2353304096491526 | 0.10343876812214023 | 1.5701942239956401 | 4.066538376447473 | 16.789677683444 | 31.709447042133828 | NA | 32.060305059956086 | 0.01691510380042419 | 0.055110462367772506 | 0.041202702185160214 | 0.4504151924701673 | NA | 0.6185939707977715 | 0.6185939707977715 | 0.12802472049949576 |
| Retail (Automotive) | 30 | 0.17119444444444448 | 0.06192772057800811 | 0.15601912407155186 | 0.23558902670157125 | 1.0827260845919955 | 1.5201925121768585 | 0.12909943522330541 | 0.3571089596648453 | 0.055 | 0.3650261649894974 | 0.09703209278724896 | 3.231310954211314 | 0.9056056510991908 | 9.751030600499705 | 15.107260975672965 | 6.065222452224933 | 10.001651614901713 | 0.08138642919835998 | 0.017778313148109137 | 0.05125989446153653 | 1.339063563687063 | 0.4325408025161122 | 0.06700715204320706 | 0.06700715204320706 | 0.057364970955562075 |
| Retail (Building Supply) | 15 | 0.13023333333333334 | 0.13849542000702966 | 0.5028484728676212 | 0.24916304003227943 | 1.5670419621739333 | 1.7891723510222548 | 0.14507683765072193 | 0.3754618371665436 | 0.055 | 0.17500957285412982 | 0.126906147142674 | 4.203817602520786 | 1.956348655854606 | 11.469128120171815 | 14.161032414237553 | NA | 14.307930590731086 | 0.10000462572456546 | 0.022444677911148944 | 0.006313216921601308 | 0.41726625965420955 | 0.004772696062798849 | 0.41155081198269666 | 0.4115508119826967 | 0.13811055980818 |
| Retail (Distributors) | 69 | 0.07326928571428572 | 0.11662138900914724 | 0.21342632081347138 | 0.23456802565441692 | 1.00607436454125 | 1.2752456934388758 | 0.11454959419026922 | 0.3708301077624006 | 0.055 | 0.2834997671745757 | 0.093769176303337 | 2.072928089871825 | 1.449137151741598 | 9.433702866546723 | 11.189698840895451 | 3.3546996530954596 | 27.139280463174906 | 0.17141068041195093 | 0.060647545579341045 | 0.07949364519590488 | 1.3260349839685297 | 0.2737443605173803 | 0.2164578249331 | 0.21645782493309995 | 0.11913571399654554 |
| Retail (General) | 15 | 0.04318153846153847 | 0.04349013269604322 | 0.17887258680308168 | 0.2540702378569475 | 1.2201002971574864 | 1.3632136186935628 | 0.11977488895039763 | 0.3152808031931311 | 0.055 | 0.1664557837084525 | 0.10670396701953999 | 5.511747523381161 | 0.8131344998544168 | 11.895592388704946 | 19.72897984645551 | 5.447198664759489 | 18.550527865353317 | 0.02616537964536512 | 0.028461865484092286 | 0.012638682392051338 | 0.9847020872176538 | 0.18290105640630752 | 0.4059765447938354 | 0.4059765447938354 | 0.041215232930581755 |
| Retail (Grocery and Food) | 13 | 0.049611111111111106 | 0.033229364367785945 | 0.12766332763145424 | 0.22297163025907965 | 0.4731749077028324 | 0.6675697330631398 | 0.07845364214395051 | 0.28264661461127033 | 0.055 | 0.39692761226145523 | 0.06368648930032259 | 5.234475855272969 | 0.37471973967659333 | 5.89476304542662 | 12.820375172626665 | 2.7461328553855116 | 16.752102075844263 | -0.0058215488757404205 | 0.021644450260973638 | 0.0023337952710874967 | 0.4241060659995174 | 0.2797516700679757 | 0.19815214989312624 | 0.19815214989312624 | 0.029192633781895124 |
| Retail (Online) | 63 | 0.2071252173913043 | 0.023028824906177303 | 0.050939512756182574 | 0.00440357025290346 | 1.355989844350516 | 1.4871300694613425 | 0.12713552612600376 | 0.5941038876075868 | 0.058800000000000005 | 0.16089394698680773 | 0.11377561258746482 | 1.3427580150233107 | 1.866225598378875 | 16.070943107400783 | 98.64073830484081 | 6.1619844288535095 | 205.21167470141248 | -0.00428482546646858 | 0.11698649326936973 | 0.08251654433099144 | 7.0941697703296684 | 0.02542424244032552 | 0.13918756106739016 | 0.13918756106739016 | 0.03868918333877249 |
| Retail (Special Lines) | 78 | 0.13322980769230772 | 0.05426945441732903 | 0.1571584353124657 | 0.20574028224664132 | 1.187876333197214 | 1.4752073825450458 | 0.12642731852317574 | 0.3858590522578964 | 0.055 | 0.28139429989154335 | 0.10245890661070772 | 3.2211003615831286 | 0.9674550191478091 | 8.399902375045642 | 16.588661331446687 | 4.418236641665773 | 19.96836293696793 | 0.0780756893625751 | 0.025391764038313232 | 0.016007996870033885 | 0.8898670773460154 | 0.2416499492873876 | 0.32402204137758905 | 0.32402204137758905 | 0.05740600747813129 |
| Rubber& Tires | 3 | 0.12423333333333333 | 0.055477892133474836 | 0.09617454430217655 | 0 | 0.267665547396446 | 0.8380149796297053 | 0.0885780897900045 | 0.39785998397496214 | 0.055 | 0.7676223370968542 | 0.05224799089507148 | 1.5914803168514429 | 0.5499465414761432 | 4.811274774025906 | 9.42230539891849 | 0.5493720735234542 | 7.086078039072091 | 0.1333243103767247 | 0.052902454698591055 | 0.00856348039454338 | 1.0500968085452227 | 0.1980977052337177 | 0 | 0 | 0.06043087261829703 |
| Semiconductor | 68 | 0.08879891304347824 | 0.2543854003508068 | 0.1851707902340006 | 0.1021277550583995 | 1.534267220206094 | 1.607746258634069 | 0.1343001277628637 | 0.38404265117692143 | 0.055 | 0.10124985178257215 | 0.12487881611852436 | 0.722010058861165 | 4.975798282606991 | 12.655041430895425 | 19.336945230156992 | 3.793246267198556 | 29.657290214296978 | 0.2033162539524809 | 0.16832492397226165 | 0.09421140516616199 | 0.685618469941525 | 0.22766391058991867 | 0.3284419880341456 | 0.3284419880341456 | 0.2772817593589296 |
| Semiconductor Equip | 30 | 0.1569692307692308 | 0.27299636853201725 | 0.3816616626750827 | 0.13503787754453553 | 1.6892473610771204 | 1.757142721715889 | 0.1431742776699238 | 0.4156872302967652 | 0.055 | 0.10544019640189742 | 0.13242736181428552 | 1.5108753291051042 | 3.6641302435732546 | 11.777235010380455 | 13.34229484427565 | 6.397780511346916 | 20.068843491664495 | 0.3428701992540078 | 0.04492499775711765 | 0.15241894968668626 | 1.0589803717525832 | 0.4651593371329801 | 0.14247023533039754 | 0.1424702353303975 | 0.2826196149157691 |
| Shipbuilding & Marine | 8 | 0.15536666666666668 | 0.25504298331125996 | 0.2879125341055872 | 0.15555189720939572 | 0.7803339556376949 | 0.9437386318475969 | 0.09485807473174726 | 0.4116087861322939 | 0.055 | 0.28067166925935105 | 0.07981180691100771 | 1.1661301455364754 | 1.072671629219107 | 3.281536209212122 | 4.063874880059042 | 1.0608776649134781 | 10.015502901810539 | 0.09395861575323011 | 0.051803655272075054 | 0.0015116725465492238 | 0.00598353316552729 | 0.352900093688783 | 0.12371482357484191 | 0.12371482357484187 | 0.2633054493508078 |
| Shoe | 13 | 0.11900000000000001 | 0.12855202477384006 | 0.3342396344576759 | 0.14205695165101007 | 1.2886673829152329 | 1.3276925338648697 | 0.11766493651157327 | 0.39374185918980237 | 0.055 | 0.08268717900795376 | 0.11134640097735939 | 2.9142709053503486 | 3.219725310841145 | 20.228666883751565 | 25.052228696194703 | 9.044190384706098 | 13.494158283376812 | 0.24978584094939296 | 0.008455204799205937 | 0.022399777105094363 | 0.48818130917890407 | 0.3628330262085087 | 0.26914232272981153 | 0.26914232272981153 | 0.12841863962857086 |
| Software (Entertainment) | 91 | 0.3037975862068965 | 0.2591428002892296 | 0.21872362118463728 | 0.15916868395647554 | 1.3578802103729628 | 1.363575730964357 | 0.11979639841928282 | 0.5870954387158441 | 0.058800000000000005 | 0.04582462828641865 | 0.11632763909909853 | 0.7813974373898928 | 3.5922880547988676 | 10.654085080406665 | 13.78633819467794 | 3.7956325817017307 | 105.43298269537888 | 0.06682436208311335 | 0.13448757972934877 | 0.14039023756413552 | 0.6717978389947261 | 0.22766341753018665 | 0.0006551477297013915 | 0.000655147729701433 | 0.2897011182972217 |
| Software (Internet) | 33 | 0.25943 | -0.05853173284373935 | -0.010250823148619595 | 0.19106183121096207 | 1.416511407810549 | 1.5513058877107246 | 0.13094756973001703 | 0.5524383754678915 | 0.058800000000000005 | 0.15006072569661108 | 0.11791516039134364 | 0.6650697398715891 | 6.33261280809359 | 14.835872625839691 | NA | 5.209346954450719 | 28.69825303664946 | 0.11330412713427597 | 0.064780861262625 | 0.11033018097918079 | NA | -0.15730842666696312 | 0 | 0 | -0.01670941277525544 |
| Software (System & Application) | 390 | 0.201011923076923 | 0.21806980176649746 | 0.2247072128366467 | 0.17780321331389323 | 1.4129709426977197 | 1.4697712402478267 | 0.1261044116707209 | 0.5211121018357716 | 0.058800000000000005 | 0.08562961432885291 | 0.11908240552609259 | 0.959207166594295 | 7.587550224240557 | 21.32786903325158 | 31.832828872759528 | 8.387814032453386 | 103.73573705984646 | 0.1302699211493067 | 0.08172221219660308 | 0.21305367709810255 | 1.3763945807748532 | 0.19683264162210642 | 0.34011176822892464 | 0.34011176822892464 | 0.241698966742379 |
| Steel | 28 | 0.1520936 | 0.19837279405275304 | 0.4863153885196634 | 0.2062644831235786 | 1.2125474928571525 | 1.3424843767995962 | 0.11854357198189602 | 0.3829895701117335 | 0.055 | 0.22236540864885215 | 0.10135615526221226 | 2.8748481776829053 | 0.6763276916009028 | 2.9604690976503054 | 3.3903648016728862 | 1.5077570630625767 | 12.795287192941224 | 0.1944023890324635 | 0.04052838514931539 | 0.0512979629176749 | 0.4870278990667957 | 0.537480679412654 | 0.052465192388391764 | 0.05246519238839176 | 0.19890523188577286 |
| Telecom (Wireless) | 16 | 0.1849777777777778 | 0.14045963573882486 | 0.061518831942779746 | 0.04744637161955524 | 0.7113584236080368 | 1.0309737102652559 | 0.10003983838975619 | 0.5192104768899954 | 0.058800000000000005 | 0.3945063077306901 | 0.07797121929156196 | 0.5214575852257843 | 3.1769575920264543 | 8.74089286190526 | 25.66249204105151 | 2.1879318941731314 | 30.24621768547484 | 0.0614378777867187 | 0.17161754624729897 | 0.010400480070954753 | 0.6218677824615795 | 0.02970805422426054 | 0.0627732949625411 | 0.06277329496254114 | 0.1227109614976522 |
| Telecom. Equipment | 79 | 0.03511584905660377 | 0.18340619780161901 | 0.25986621816079664 | 0.184466328861244 | 1.1784895771242725 | 1.2331194872073334 | 0.11204729754011561 | 0.4134875394830146 | 0.055 | 0.10457107348559717 | 0.10464394813646649 | 1.4179419448565018 | 3.5614434610706187 | 14.699355157441362 | 19.00053687930832 | 5.2013339028049375 | 36.72724784657824 | 0.23107855060632893 | 0.02460198485112462 | 0.03515367465928802 | 0.4993733539051406 | 0.2012914047129525 | 0.5106530444713658 | 0.5106530444713658 | 0.1908294296044563 |
| Telecom. Services | 49 | 0.1681304347826087 | 0.1998345514022523 | 0.12376739217567063 | 0.22104818421663627 | 0.47390612503545576 | 0.8822681652856597 | 0.09120672901796818 | 0.5537169562159238 | 0.058800000000000005 | 0.5406894051251091 | 0.06573661972785325 | 0.6617294326445012 | 2.1752246611284507 | 5.984354115234283 | 10.877670675991812 | 1.287295882965915 | 145.85411391978104 | 0.0036739098538658686 | 0.1517084798090702 | 0.05761750673143343 | 0.36159994195800516 | 0.15757991803815463 | 0.519086211396578 | 0.519086211396578 | 0.20007496687469906 |
| Tobacco | 15 | 0.05765 | 0.43764657386660305 | 0.7088019113767647 | 0.2521525784260651 | 1.7442504521558875 | 2.0004565028386407 | 0.15762711626861525 | 0.44059235658259677 | 0.055 | 0.19390853485149315 | 0.1350606001627262 | 1.7836862713219102 | 5.046509870925673 | 10.761389721102821 | 11.467667597500895 | NA | 13.55073144227022 | 0.11365806683826973 | 0.022929900257818856 | 0.021105974212593085 | 0.0789063998419489 | NA | 1.0717329039722374 | 1.0717329039722374 | 0.44061190099685843 |
| Transportation | 18 | 0.14991818181818178 | 0.09352031095902198 | 0.24195399230782733 | 0.22166954631975314 | 0.9245938189921151 | 1.058265749430396 | 0.10166098551616552 | 0.28046286808958065 | 0.055 | 0.22785975576835596 | 0.08789575311072637 | 3.0857818119673657 | 1.082541670530705 | 7.653711343450065 | 11.54418795470029 | 4.252470295167995 | 23.851971943925097 | 0.07219291492622648 | 0.04730328909936803 | 0.023385069645266855 | 0.5047978775727006 | 0.36781742659330763 | 0.3344890410678481 | 0.33448904106784805 | 0.09377321952538265 |
| Transportation (Railroads) | 4 | 0.03783333333333333 | 0.4006313001564678 | 0.16937779933759034 | 0.2228821337940716 | 0.9323815338876874 | 1.1078308621714459 | 0.10460515321298389 | 0.1634126909210618 | 0.0473 | 0.21538599902572655 | 0.08971548610040381 | 0.5093378532028319 | 6.3236145780689155 | 12.476631341363998 | 15.865279366688831 | 6.753225613529635 | 17.861577963998506 | 0.013241792225468774 | 0.14796776026105116 | 0.055810927929796944 | 0.18857241896280746 | 0.335553285922049 | 0.3587947092321935 | 0.3587947092321935 | 0.39858198723850696 |
| Trucking | 35 | 0.14159818181818185 | 0.08928908640688692 | 0.13529236520773816 | 0.24436980579597808 | 1.232855746839977 | 1.5451244708853058 | 0.13058039357058715 | 0.4117132456701876 | 0.055 | 0.30513857374628695 | 0.10332224468426371 | 1.6609808041341676 | 1.451337489537834 | 6.338373479316901 | 11.6361932152168 | 3.5261511856041166 | 10.280924299605571 | 0.05441910923110437 | 0.12294170091825792 | 0.11041328797291604 | 1.9266562984152134 | 0.0405361647492955 | 0.3559574467046484 | 0.35595744670464846 | 0.09502037930535086 |
| Utility (General) | 15 | 0.040473333333333326 | 0.18191380915780603 | 0.058204550746344036 | 0.16649618768328447 | 0.4094617819876518 | 0.6351394196016483 | 0.07652728152433791 | 0.1497076220101746 | 0.0473 | 0.42586480270208965 | 0.0590445597525051 | 0.3722954582545888 | 4.283399946079026 | 13.745257053013487 | 23.7623070921024 | 1.9179993201105874 | 20.529372149088115 | 0.08922966654204853 | 0.32903516939936395 | 0.1997163970348629 | 1.5034787791370685 | 0.11241118642718625 | 0.5928100944369493 | 0.5928100944369493 | 0.1801395242781695 |
| Utility (Water) | 16 | 0.1435181818181818 | 0.29510813036713346 | 0.06906780182799742 | 0.18061405935116764 | 0.8725208753424394 | 1.1524153536245123 | 0.10725347200529603 | 0.27961318235637356 | 0.055 | 0.30263279217508 | 0.08727865697908357 | 0.2568642966131626 | 9.182944577217532 | 20.002976875109358 | 31.139459378884858 | 3.0872029616902905 | 35.13145376761002 | 0.11821847966647889 | 0.5055711743187792 | 0.4092139943577809 | 1.7868875303324088 | 0.16474700015176275 | 0.4538886548416308 | 0.34685422173962976 | 0.2936978061206455 |

## Input Stat Distributioons

| Revenue Growth Rate = Last 3 years | Pre-tax Operating Margin | Sales to Invested Capital | Cost of Capital | Beta | Debt to Capital Ratio |
|---|---|---|---|---|---|
| First Quartlie | First Quartlie | First Quartlie | First Quartlie | median(Beta) | First Quartlie |
| -0.0783 | 0.0405 | 1.15 | 0.1141 | 1.23 | 0.0102 |
| -0.0601 | 0.0561 | 0.62 | 0.1011 | 1.04 | 0.0103 |
| -0.188 | 0.0717 | 0.31 | 0.0856 | 1.24 | 0.1688 |
| -0.0379 | 0.0392 | 0.74 | 0.0975 | 0.86 | 0.0632 |
| -0.0589 | 0.0447 | 0.65 | 0.1006 | 1.35 | 0.0133 |
| -0.0144 | 0.0292 | 0.92 | 0.1225 | 1.32 | 0.0624 |
| 0.0248 | 0.001 | 0.12 | 0.0726 | 0.83 | 0.2576 |
| 0.0341 | 0.0009 | 0.22 | 0.0578 | 0.52 | 0.0875 |
| 0.0008 | 0.0722 | 0.58 | 0.0871 | 0.79 | 0.0014 |
| -0.0128 | 0.0667 | 1.02 | 0.0861 | 0.7 | 0.0007 |
| -0.0344 | 0.0721 | 0.56 | 0.0883 | 1.02 | 0.0228 |
| -0.024 | 0.0071 | 0.08 | 0.0706 | 0.97 | 0.0157 |
| -0.0056 | 0.0515 | 0.88 | 0.1035 | 1.04 | 0.0492 |
| -0.0164 | 0.0467 | 0.91 | 0.0982 | 1.03 | 0.0122 |
| -0.0441 | 0.0698 | 0.35 | 0.075 | 1.01 | 0.0664 |
| 0.0356 | 0.0491 | 0.81 | 0.1059 | 1.08 | 0.027 |
| 0.0444 | 0.0648 | 0.9 | 0.1016 | 1.16 | 0.0808 |
| 0.0371 | 0.0603 | 0.8 | 0.1067 | 1.05 | 0.02 |
| 0.0257 | 0.1413 | 0.57 | 0.1194 | 1.06 | 0.0005 |
| 0.0013 | 0.0381 | 1.31 | 0.1083 | 1.02 | 0.0099 |
| -0.0245 | 0.035 | 0.86 | 0.1175 | 1.21 | 0.02 |
| -0.0178 | 0.0423 | 0.63 | 0.101 | 1.07 | 0.047 |
| -0.006 | 0.0642 | 0.31 | 0.0863 | 0.97 | 0.0589 |
| -0.0689 | 0.0869 | 0.12 | 0.1126 | 1.17 | 0.0023 |
| -0.0039 | 0.0652 | 0.46 | 0.098 | 0.97 | 0.0057 |
| -0.0304 | 0.079 | 0.43 | 0.0902 | 0.78 | 0.0134 |
| 0.0062 | 0.0411 | 0.8 | 0.1116 | 1.05 | 0.0162 |
| -0.0581 | 0.0264 | 1.01 | 0.1059 | 1.18 | 0.0286 |
| -0.0126 | 0.0471 | 0.74 | 0.1229 | 1.23 | 0.017 |
| -0.0653 | 0.0341 | 0.7 | 0.0887 | 0.95 | 0.0516 |
| -0.0944 | 0.0529 | 0.42 | 0.1044 | 1.15 | 0.0009 |
| -0.0231 | 0.0553 | 0.42 | 0.0923 | 0.97 | 0.0281 |
| 0.0359 | 0.049 | 0.52 | 0.0829 | 0.74 | 0.0141 |
| -0.0271 | 0.0285 | 0.09 | 0.0484 | 0.81 | 0.0302 |
| 0.0102 | 0.0349 | 0.94 | 0.0858 | 0.68 | 0.0391 |
| -0.0406 | 0.0124 | 1.23 | 0.0717 | 0.61 | 0.0213 |
| -0.005 | 0.0503 | 1.05 | 0.1128 | 0.98 | 0.0292 |
| 0.0116 | 0.1752 | 0.13 | 0.0871 | 0.93 | 0.0877 |
| 0.0138 | 0.089 | 0.6 | 0.1025 | 1.1 | 0.0064 |
| 0.0176 | 0.0368 | 1.13 | 0.0935 | 0.88 | 0.0185 |
| 0.0456 | 0.0821 | 0.57 | 0.1139 | 1.28 | 0.0047 |
| -0.0126 | 0.0626 | 0.61 | 0.0983 | 1.09 | 0.1344 |
| 0.036 | 0.075 | 0.63 | 0.0731 | 0.72 | 0.0447 |
| -0.178 | 0.0694 | 0.16 | 0.0895 | 0.91 | 0.0342 |
| -0.0232 | 0.0485 | 0.78 | 0.0959 | 0.9 | 0.0032 |
| 0.0086 | 0.0723 | 1.1 | 0.1184 | 1.26 | 0.0079 |
| -0.0175 | 0.0635 | 0.83 | 0.0799 | 0.61 | 0 |
| -0.0178 | 0.0576 | 0.49 | 0.0864 | 0.89 | 0.0056 |
| 0.0036 | 0.072 | 0.68 | 0.0799 | 0.76 | 0.0001 |
| -0.0313 | 0.1856 | 0.06 | 0.0726 | 0.52 | 0 |
| -0.0072 | 0.0512 | 0.81 | 0.1088 | 1.06 | 0.0184 |
| 0.0115 | 0.0474 | 0.09 | 0.1049 | 1.13 | 0 |
| -0.0309 | 0.0343 | 0.94 | 0.0945 | 0.89 | 0.031 |
| 0.106 | 0.1189 | 1 | 0.1034 | 1.08 | 0.1014 |
| 0.0227 | 0.2321 | 0.34 | 0.1085 | 1.14 | 0 |
| 0.0085 | 0.0391 | 0.28 | 0.0793 | 0.9 | 0.103 |
| -0.0754 | 0.0288 | 0.62 | 0.0936 | 1.09 | 0.0448 |
| 0.0197 | 0.0419 | 0.92 | 0.0835 | 0.84 | 0.0619 |
| 0.014 | 0.045 | 0.69 | 0.0892 | 0.97 | 0.1041 |
| 0.0301 | 0.0659 | 0.36 | 0.0691 | 0.64 | 0.1411 |
| 0.0083 | 0.1119 | 0.1 | 0.1042 | 1.12 | 0 |
| -0.0567 | 0.0401 | 0.73 | 0.0979 | 0.79 | 0.0128 |
| -0.025 | 0.3438 | 0.06 | 0.0673 | 0.81 | 0.2442 |
| -0.13 | 0.0978 | 0.11 | 0.075 | 0.96 | 0.0959 |
| -0.105 | 0.1047 | 0.07 | 0.0746 | 0.91 | 0.1588 |
| -0.0397 | 0.1671 | 0.06 | 0.0719 | 0.81 | 0.0183 |
| -0.028 | 0.0679 | 0.52 | 0.0976 | 1.07 | 0.0276 |
| 0.0386 | 0.0354 | 0.7 | 0.1164 | 1.02 | 0.0001 |
| -0.092 | 0.03 | 0.99 | 0.0888 | 0.87 | 0.0974 |
| 0.0038 | 0.0267 | 1.55 | 0.0835 | 0.93 | 0.0964 |
| 0.0032 | 0.0472 | 1.24 | 0.0928 | 1.09 | 0.1793 |
| -0.0269 | 0.0274 | 0.68 | 0.0796 | 0.77 | 0.0217 |
| -0.153 | 0.0365 | 0.51 | 0.0864 | 0.79 | 0.1906 |
| 0.004 | 0.0232 | 1.85 | 0.0742 | 0.57 | 0.1311 |
| -0.0098 | 0.0242 | 1.56 | 0.1272 | 1.49 | 0.0118 |
| -0.0524 | 0.0329 | 1.32 | 0.0957 | 1.01 | 0.093 |
| 0.0372 | 0.0286 | 0.91 | 0.1009 | 1.06 | 0.1129 |
| 0.0234 | 0.0677 | 0.7 | 0.1488 | 1.7 | 0.0049 |
| 0.0552 | 0.0969 | 0.78 | 0.1673 | 2.07 | 0.01 |
| 0.0037 | 0.1051 | 0.34 | 0.1084 | 1.04 | 0.0852 |
| -0.106 | 0.0632 | 0.86 | 0.1047 | 1.03 | 0.031 |
| -0.0312 | 0.0592 | 1.04 | 0.1256 | 1.39 | 0.0009 |
| 0.037 | 0.0469 | 0.71 | 0.1135 | 1.3 | 0.017 |
| 0.0068 | 0.0557 | 0.78 | 0.1169 | 1.22 | 0.0022 |
| 0.027 | 0.0371 | 0.95 | 0.1074 | 1.18 | 0.0527 |
| -0.0328 | 0.0922 | 0.55 | 0.078 | 0.72 | 0.0553 |
| -0.0545 | 0.0449 | 0.81 | 0.1087 | 1.05 | 0.0159 |
| -0.0138 | 0.07 | 0.48 | 0.0707 | 0.81 | 0.0488 |
| 0.0307 | 0.1858 | 1.09 | 0.085 | 0.59 | 0.0009 |
| 0.0177 | 0.0399 | 0.45 | 0.0931 | 0.94 | 0.0852 |
| -0.079 | 0.0433 | 0.26 | 0.0746 | 0.54 | 0.1624 |
| -0.0614 | 0.0427 | 0.64 | 0.0875 | 1.05 | 0.1033 |
| 0.0141 | 0.0849 | 0.32 | 0.0641 | 0.63 | 0.3489 |
| 0.0064 | 0.1301 | 0.2 | 0.0692 | 0.69 | 0.0668 |

## Industry Average Beta (Global)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 362 | 0.07349679425837323 | 0.090308890940185 | 0.21338723126336392 | 0.2507210528737477 | 1.1743473424289956 | 1.2935834925393561 | 0.14202796270464063 | 0.39695739619251297 | 0.0695 | 0.26559116619465917 | 0.11821144332952692 | 2.711138672455651 | 1.5118171161470773 | 10.549458319666552 | 15.504367980070299 | 2.335462071149348 | 39.759159058984224 | -0.02605962957448102 | 0.02148474848240947 | 0.007215982887477486 | 0.27774109940881886 | 0.10200864604262225 | 0.44451143385934094 | 0.444511433859341 | 0.0922245028320596 |
| Aerospace/Defense | 278 | 0.07371420118343196 | 0.0802440409532544 | 0.12143702063274998 | 0.16363578286229677 | 1.0573692747052328 | 1.1580552633554024 | 0.13121281001576113 | 0.36229340257411924 | 0.0695 | 0.18855316790308613 | 0.11634379756383052 | 1.692127515385807 | 2.262635626066735 | 15.266315053274221 | 24.54544846983273 | 4.357323379752499 | 69.87388551014537 | 0.4234310138456182 | 0.03391517043933751 | 0.009353075996040757 | 0.41378426559560244 | 0.08035518193987151 | 0.7295149346220662 | 0.7295149346220662 | 0.07998193024724214 |
| Air Transport | 155 | -0.024202561983471073 | 0.012353378911390047 | 0.009035525266594758 | 0.1308370077254517 | 0.7616142271729274 | 1.2354206917515256 | 0.13738657120177172 | 0.3086331186196793 | 0.0695 | 0.5237682228114381 | 0.09284939582121066 | 0.805422779862451 | 1.9367510184926524 | 10.980475195113629 | 106.6657342055652 | 2.938289478805663 | 75.85609215490307 | -0.035817592352555154 | 0.09669306549087575 | 0.03255914751008839 | 9.554712598518389 | -0.09324294682762552 | 0.004419175188995642 | 0.004419175188995594 | 0.012274593703366197 |
| Apparel | 1146 | 0.04618989323843408 | 0.14743627276755109 | 0.20093422274465472 | 0.23781863623580107 | 0.8419360205243345 | 0.9023788899541185 | 0.11080983541833865 | 0.34781354412233134 | 0.0695 | 0.15361852401854517 | 0.10182999002758587 | 1.5806190152148958 | 2.3572313228368644 | 12.584665934703455 | 15.486602949046972 | 3.630902383785467 | 73.56324390422597 | 0.21493944316933722 | 0.03660958407879034 | 0.01666673769185636 | 0.4898760232758958 | 0.1530772260165763 | 0.4288308576857397 | 0.4288308576857397 | 0.14943657631895677 |
| Auto & Truck | 154 | 0.0820659595959596 | 0.06584576381061448 | 0.053357693453791086 | 0.21365745874896358 | 1.033835592637108 | 1.3526231349119202 | 0.14673932616597124 | 0.33896789399772925 | 0.0695 | 0.42427592940792425 | 0.10669405268100901 | 0.9247133687947062 | 1.082392518093318 | 9.203088454113926 | 15.835554573844876 | 1.292431960902446 | 27.78183817535008 | 0.007971307435025709 | 0.06042326507167017 | 0.027560794421056058 | 0.501947218801582 | 0.11518174528970851 | 0.22505595545281412 | 0.2250559554528141 | 0.0651703237606505 |
| Auto Parts | 746 | 0.05157986111111109 | 0.03647900956143489 | 0.04222860068434426 | 0.2574675742296212 | 1.2875467841381958 | 1.413010159958089 | 0.1515582107646555 | 0.31499751482799093 | 0.0695 | 0.26055904721279227 | 0.12570974732398635 | 1.4689858860581844 | 0.8305830591776443 | 9.466619658163935 | 21.860840601324096 | 1.3917099071259258 | 39.30186873531657 | 0.13142619927912766 | 0.05141194612231626 | 0.03166860853225206 | 2.064763431650533 | 0.05251207918833817 | 0.5185241338593111 | 0.5185241338593111 | 0.03494348846379794 |
| Bank (Money Center) | 596 | 0.10534848197343455 | 4.176476620020245e-05 | 4.1684616383614826e-05 | 0.18677332609619868 | 0.4376114721606776 | 0.875215474102932 | 0.10864219483341397 | 0.21675380851065218 | 0.0618 | 0.7502559737795642 | 0.06206011074309724 | 0.14023331329651406 | 6.68904522191274 | NA | NA | 0.8128519039802712 | 13.739133910974902 | NA | 0.03240448410896908 | 0.03436084105993763 | 84.18982259677921 | 0.01033504286307702 | 0.3348340047059705 | 0.3348340047059706 | 0.00037602747649597004 |
| Banks (Regional) | 800 | 0.09005879699248125 | 0.00010047331251049651 | -3.6680349455871644e-05 | 0.19825798888305474 | 0.3577565862282306 | 0.563870289429285 | 0.08379684909645693 | 0.17830180346656344 | 0.0618 | 0.6591944805456077 | 0.05924652898061072 | 0.19352947870025708 | 5.504574764357144 | NA | NA | 0.8918841732556868 | 20.711981486924902 | NA | 0.03158023938571787 | -0.013115480793971833 | NA | 0.09043693980666588 | 0.2752450001964576 | 0.2752450001964576 | -0.0002540984845925507 |
| Beverage (Alcoholic) | 220 | 0.09132939759036145 | 0.21975004183319735 | 0.13930925191772361 | 0.23813766776644182 | 0.810718193165097 | 0.8721564431804729 | 0.10839808416580174 | 0.2857195762521225 | 0.0695 | 0.14071582488908002 | 0.10051184388279663 | 0.7656233265353857 | 4.332294815544168 | 16.172276414424015 | 19.503078091482607 | 3.5736745890053765 | 69.35161011944025 | 0.08687148075729637 | 0.045801360272714885 | 0.009414363227832468 | 0.01649576290788247 | 0.14498308042811484 | 0.41804095988813733 | 0.4180409598881374 | 0.21965850488954478 |
| Beverage (Soft) | 100 | 0.09017305084745762 | 0.16549489068571271 | 0.22610954818560502 | 0.19967869658810308 | 0.7947183264713243 | 0.8559001919036798 | 0.10710083531391365 | 0.31052361417890234 | 0.0695 | 0.1332849773199536 | 0.0998039512605015 | 1.5704645257815757 | 3.9033785429845778 | 18.728439522644482 | 23.26588194335533 | 6.611053706122415 | 44.95759960527995 | -0.06490524601098407 | 0.045824689476554596 | 0.04190415783690828 | 0.25833730543349975 | 0.24708930327847395 | 0.5469157277907805 | 0.5469157277907805 | 0.16620550043419383 |
| Broadcasting | 135 | 0.04427754545454546 | 0.1308431874962574 | 0.1088653110194383 | 0.23766054151835447 | 0.7444295667373665 | 1.0569743272387224 | 0.12314655131365004 | 0.3471662204267433 | 0.0695 | 0.44641195523530475 | 0.09154406630981221 | 0.9915056500674314 | 1.2237022060163452 | 6.469753703932454 | 9.086302445486572 | 0.8121902879750735 | 22.857740397461747 | 0.1137871279794641 | 0.03567095665871962 | 0.017539067116144117 | 1.3085560327270698 | 0.2978111577675327 | 0.10093323840372377 | 0.10093323840372381 | 0.13150372291132204 |
| Brokerage & Investment Banking | 592 | 0.10401919621749414 | 0.007269050174820512 | 0.0011237028657450701 | 0.2023495810574502 | 0.4509503326169772 | 0.9914624277631093 | 0.11791870173549612 | 0.349876137221484 | 0.0695 | 0.7057778831848922 | 0.07164483235522795 | 0.19322010265558867 | 5.3692439869910435 | 197.28291344916556 | NA | 1.2161813550455391 | 60.9495955459226 | NA | 0.028564235872633317 | -0.005022949212196832 | -39.91358492584554 | 0.09203278286129259 | 0.5223993223618727 | 0.5223993223618727 | 0.006873375407273932 |
| Building Materials | 454 | 0.07662574712643681 | 0.1074016270100931 | 0.16368297461942438 | 0.2164151373942824 | 0.9975517318295956 | 1.1065292223300869 | 0.12710103194194095 | 0.29868072216447483 | 0.0695 | 0.2017709367688076 | 0.11201932390615539 | 1.851184271800939 | 1.4390645957182182 | 9.6623300164161 | 13.03055848596199 | 2.4062797893398473 | 42.279983498124 | 0.17342708024407452 | 0.03830683646294482 | 0.040279969081317146 | 0.8692682599636523 | 0.15118080309483573 | 0.3029680271893628 | 0.3029680271893628 | 0.10756044602739526 |
| Business & Consumer Services | 961 | 0.07703052459016402 | 0.08521041542643595 | 0.1949198693955836 | 0.24146672103341693 | 0.9967488441793113 | 1.094243034645496 | 0.12612059416471058 | 0.35508042862954164 | 0.0695 | 0.18870553380788824 | 0.11220049568260584 | 2.6318315409345043 | 1.796327021989877 | 13.458680230874046 | 20.23265239150099 | 3.557244153469614 | 43.8099528747089 | 0.09763990251606934 | 0.026116173242196936 | 0.04355539782995434 | 0.8672778013318297 | 0.10173941306387643 | 0.5467143801782037 | 0.5467143801782037 | 0.08831909150481168 |
| Cable TV | 54 | 0.042067906976744174 | 0.19268732296056873 | 0.12652466179683763 | 0.2839068189404157 | 0.6054329946472208 | 1.023983376282326 | 0.12051387342732961 | 0.26282180998895055 | 0.0695 | 0.49450981804764355 | 0.08680831989906676 | 0.7691956873494492 | 2.4944078285796922 | 7.497175384132114 | 12.940344181786392 | 1.929850102641772 | 29.82018487985743 | 0.01544906558148442 | 0.11558223276503958 | 0.001154135785663474 | 0.061135959638478815 | 0.10901267306081759 | 0.35370332420360845 | 0.3537033242036085 | 0.1895508363242917 |
| Chemical (Basic) | 879 | 0.1238678778625954 | 0.10020419212665564 | 0.10745139617308558 | 0.18832514749498638 | 0.9877865839791308 | 1.1399114789559386 | 0.1297649360206839 | 0.3264943738808307 | 0.0695 | 0.27051844186953267 | 0.10882394490616107 | 1.2655741833436442 | 1.2364855715506904 | 8.30586737128921 | 11.916917872618122 | 1.5633404186346405 | 32.46118220402441 | 0.1304677165424474 | 0.07741641993492572 | 0.06290271963579111 | 1.1979557665164933 | 0.13015440695282732 | 0.4641633324157964 | 0.4641633324157963 | 0.10069812557358715 |
| Chemical (Diversified) | 68 | 0.07925883333333332 | 0.10208853535516443 | 0.08886057802387214 | 0.22109460004677506 | 0.9419506953199124 | 1.1958248741877604 | 0.1342268249601833 | 0.2492126497097023 | 0.0618 | 0.34287939688821434 | 0.10416559904158584 | 1.1466338195851349 | 0.9429672385801698 | 6.171064177804876 | 9.16206219781443 | 1.1245367981194994 | 13.50879548773655 | 0.1721723279126885 | 0.05447492443625545 | 0.01968897467248543 | 0.8023891759844538 | 0.13650087385165174 | 0.29292289982848024 | 0.2929228998284803 | 0.09917956328860605 |
| Chemical (Specialty) | 922 | 0.12358691813804168 | 0.1547255582981597 | 0.1715000996753188 | 0.2172107878596366 | 1.0212013193407876 | 1.1068628177675968 | 0.1271276528578542 | 0.3414918749663052 | 0.0695 | 0.17459079391537816 | 0.11407292254822643 | 1.3054375504666331 | 2.0157117635380177 | 9.479471948077077 | 12.823605641607234 | 2.4990688320644274 | 33.689947719856896 | 0.1844776588281513 | 0.06744484988879569 | 0.04983810727029268 | 0.7573810351674554 | 0.1590104705266318 | 0.3380528302598103 | 0.33805283025981026 | 0.15610820572687148 |
| Coal & Related Energy | 212 | 0.19073247787610623 | 0.29123799344815227 | 0.38609852291856595 | 0.23084834706391377 | 1.3528350871710502 | 1.211961212621946 | 0.13551450476723126 | 0.5872695030181825 | 0.0733 | 0.19555045254951162 | 0.11981226986085283 | 1.4608803604303342 | 1.0881834921399869 | 3.008895759072722 | 3.6010760403633757 | 1.4159269251330795 | 19.361296059901157 | -0.008295758638766266 | 0.05858210343417448 | 0.03608471636427277 | 0.14301394578319884 | 0.3143846294124089 | 0.4089572366189599 | 0.4089572366189599 | 0.2920798340532986 |
| Computer Services | 1105 | 0.0936456639566397 | 0.0731762669272857 | 0.2025293235529626 | 0.23035511343444337 | 1.0374271307252976 | 1.088247192028082 | 0.12564212592384094 | 0.33786373564723465 | 0.0695 | 0.14049829938709574 | 0.11534531804067875 | 3.2818741479491207 | 1.3095675699093319 | 12.706719019755342 | 17.227484749698625 | 3.578599453181751 | 49.676816960710156 | 0.1651626702816448 | 0.013489169924479476 | 0.009891542576939902 | 0.6566015328288205 | 0.13814920572691777 | 0.5219473538547462 | 0.5219473538547462 | 0.07406757612376824 |
| Computers/Peripherals | 333 | 0.04330487999999997 | 0.1371709696494902 | 0.20720316942953626 | 0.1870417925316183 | 1.2200041411476166 | 1.2620051937696362 | 0.13950801446281696 | 0.3292446932773343 | 0.0695 | 0.105922132128553 | 0.1302765125000989 | 1.7356503868390247 | 2.0056137769058395 | 11.199448015099572 | 14.50983570747668 | 5.202182203957226 | 34.15914079600229 | 0.032155484356610434 | 0.043997628967966884 | 0.03202733454190231 | 0.4842047957807719 | 0.27940376674380923 | 0.22650677990976426 | 0.2265067799097642 | 0.1386901932166646 |
| Construction Supplies | 790 | 0.08988834162520723 | 0.0792381372224037 | 0.07145774048181253 | 0.2208663656991046 | 0.9372739963088855 | 1.1168579550772775 | 0.12792526481516675 | 0.30150511958275444 | 0.0695 | 0.31133232518566467 | 0.1043975961893531 | 1.06716272205561 | 1.3587154692875165 | 10.009606294953084 | 16.066971457506867 | 1.416933142554405 | 42.499008672488294 | 0.18043639079001042 | 0.05809013759002801 | 0.03862360995787296 | 1.075371172802579 | 0.08092246027245968 | 0.5144602635037274 | 0.5144602635037274 | 0.07872801398395676 |
| Diversified | 314 | 0.0981704081632652 | 0.09340396121502545 | 0.0629528070306068 | 0.1715193352239163 | 0.7347087450687306 | 0.9639252546213195 | 0.1157212353187813 | 0.27349373371508195 | 0.0695 | 0.35858198888340026 | 0.09299901155182635 | 0.7840641464318554 | 1.8829530097500131 | 13.155686802482316 | 19.330338827982725 | 1.2135055453841528 | 19.426843095216764 | -0.11650945036047462 | 0.04246304386697994 | 0.007631232936130878 | 0.49580074819389314 | 0.05811285313673751 | 0.3984014016641982 | 0.39840140166419813 | 0.09286448437938341 |
| Drugs (Biotechnology) | 1267 | 0.26030372043010735 | 0.08228334754243002 | 0.04652691339292144 | 0.14795873564922327 | 1.2526532845890637 | 1.268267613064147 | 0.14000775552251893 | 0.5169419464088241 | 0.0733 | 0.1139572454338612 | 0.1303452220496197 | 0.4598326164690035 | 6.5588146508950045 | 12.966365172864815 | 61.86420434741448 | 5.076921463063109 | 126.61097345829106 | 0.18476756001476305 | 0.05548950053184296 | 0.028951510522702298 | 1.8806559490214771 | -0.010637065540967156 | 0.002231814578747779 | 0.0022318145787477706 | 0.1031871099641556 |
| Drugs (Pharmaceutical) | 1352 | 0.17139170469798656 | 0.21497248584763778 | 0.13957128286220502 | 0.14063075584878457 | 0.995463542798184 | 1.0635869533243638 | 0.12367423887528423 | 0.44281720798926644 | 0.0695 | 0.13152916490130936 | 0.11429359345066391 | 0.7148776728319557 | 3.9802709254480027 | 12.690853000619033 | 17.54056349391283 | 3.8038786986767983 | 128.87688628734568 | 0.14897338338600832 | 0.046616068018540166 | 0.02011806323193172 | 0.22118800607153283 | 0.16122384369938733 | 0.5040583954113961 | 0.5040583954113961 | 0.2169338084689572 |
| Education | 251 | 0.0724626666666667 | 0.0852324095366155 | 0.06260319152041387 | 0.2024249848906487 | 0.7917217099759216 | 0.8787672588238772 | 0.1089256272541454 | 0.34117555150021905 | 0.0695 | 0.24741750017757028 | 0.0949289032540725 | 0.8514149741093573 | 2.369614694624465 | 10.001464516545653 | 21.79913089310736 | 1.85553442914771 | 179.0535768204242 | 0.007382867995886809 | 0.07271230216929873 | 0.09407008697754254 | 1.947534990521329 | 0.03679776661145092 | 0.7182624548207336 | 0.7182624548207336 | 0.08480802638312034 |
| Electrical Equipment | 1045 | 0.12176879483500726 | 0.06658191558606737 | 0.09606962883100381 | 0.181138022713572 | 1.102323689949516 | 1.1360186851537797 | 0.12945429107527162 | 0.37245108102966507 | 0.0695 | 0.14301741508197188 | 0.11842765679971393 | 1.5879625149016394 | 2.027701783318698 | 16.767282753897025 | 27.675072347786415 | 2.833909558497774 | 40.84984806066813 | 0.22452763237582904 | 0.06781703353333478 | 0.06501200066309834 | 2.0550213941805726 | 0.09006775516814414 | 0.44354143830219317 | 0.44354143830219317 | 0.06835482579698489 |
| Electronics (Consumer & Office) | 134 | 0.028733333333333326 | 0.051856753090923656 | 0.06019721929032275 | 0.21975619593622803 | 1.0955088212486108 | 1.2725160060597946 | 0.1403467772835716 | 0.34632531120576865 | 0.0695 | 0.30715094709946367 | 0.11331981990584189 | 1.288634554510691 | 0.8036832244377874 | 7.497978347029389 | 14.970393372901015 | 1.2983108781883297 | 52.42531022117699 | 0.055377331814515686 | 0.0511236327188187 | 0.035786919353448146 | 1.6572731380834365 | 0.07850910404817528 | 0.3031069299296089 | 0.30310692992960897 | 0.05323691462491336 |
| Electronics (General) | 1457 | 0.07440767161410021 | 0.0697190397043466 | 0.08720693418717892 | 0.19110084825797172 | 1.2905124151341338 | 1.2955238162109064 | 0.14218280053363033 | 0.33176265991369114 | 0.0695 | 0.16342124700338245 | 0.1275029231310428 | 1.4384315985614258 | 1.3776033874896974 | 11.273965737803852 | 18.870401996910637 | 2.1250670536108807 | 84.52801117120472 | 0.2007449918521005 | 0.06175666226333611 | 0.0496516040521283 | 1.611553978564818 | 0.09562351801783527 | 0.3931343954665542 | 0.39313439546655427 | 0.0693254658143617 |
| Engineering/Construction | 1269 | 0.07889437054631836 | 0.0482719503946705 | 0.07301466577699338 | 0.224693023501524 | 0.7301374520654016 | 1.0295667164846354 | 0.1209594239754739 | 0.3227938598626329 | 0.0695 | 0.5103847042756305 | 0.0859444435826939 | 1.7980446299653665 | 0.5971624651351077 | 8.560221877663977 | 11.84183341894872 | 0.9243848864915459 | 30.799850738194948 | 0.15956663775102348 | 0.03191355274753511 | 0.025650645849841693 | 1.7330707134271515 | 0.09144919076728208 | 0.5913151617245603 | 0.5913151617245603 | 0.048306809979186786 |
| Entertainment | 752 | 0.10592681498829039 | 0.07987034968184331 | 0.09651262642338801 | 0.22879350569990112 | 1.101640081025748 | 1.2013486787553214 | 0.13466762456467463 | 0.42673745588286965 | 0.0695 | 0.20884276813170335 | 0.11747709245060305 | 1.2759768911988971 | 2.8990443634193923 | 16.73425520177774 | 33.75328948872721 | 2.2420184466493 | 214.52307445927008 | 0.04123618732506771 | 0.03776934359367372 | 0.018753776279506335 | 0.5072249381554339 | 0.053343812988993114 | 0.36913257422099616 | 0.3691325742209961 | 0.08253259073781696 |
| Environmental & Waste Services | 370 | 0.08376195238095238 | 0.1067977168535225 | 0.10618091123311392 | 0.218534161701805 | 0.89640526150774 | 1.0880867288276126 | 0.1256293209604435 | 0.38236707668331305 | 0.0695 | 0.27226072626110814 | 0.10567942414999154 | 1.1302069098777168 | 2.639850911564028 | 13.452443116927057 | 23.2348784088586 | 2.8428385265315317 | 42.62499718035013 | 0.13276798839253917 | 0.08456206819063641 | 0.0877448543218802 | 1.6514979421321525 | 0.09137172503715554 | 0.5584930444752979 | 0.5584930444752979 | 0.1076269103567748 |
| Farming/Agriculture | 426 | 0.1273559602649007 | 0.07427672829076559 | 0.10276535855905174 | 0.20630778097962557 | 0.659688782675045 | 0.8419168951866424 | 0.10598496823589405 | 0.34158621718358206 | 0.0695 | 0.31714825367380384 | 0.08897611131893379 | 1.5664988491796712 | 1.1363326568143441 | 10.531883443049173 | 14.629414005607046 | 2.1504493343657427 | 41.53747750861123 | 0.16352430082262925 | 0.042599519305417305 | 0.03452772940859547 | 1.3044537684733635 | 0.14362550060321239 | 0.32007015569173347 | 0.32007015569173347 | 0.07508390847390328 |
| Financial Svcs. (Non-bank & Insurance) | 1089 | 0.104697216066482 | 0.10651653844559901 | 0.005932745272563773 | 0.21700378492815886 | 0.15539901285715607 | 0.8817936764299235 | 0.1091671353791079 | 0.3312368784924336 | 0.0695 | 0.8719326375242562 | 0.05963021357840285 | 0.06471123820155421 | 16.5350973338144 | 63.3049703556233 | 74.38331473590492 | 1.2380098214278055 | 153.15694290299754 | NA | 0.04450338862807543 | 0.04185213273841836 | 0.4927886333641313 | 0.14209285342615216 | 0.22864298056819313 | 0.2286429805681931 | 0.1082415050730236 |
| Food Processing | 1397 | 0.0970760041194644 | 0.08321397200060052 | 0.1178757677853427 | 0.20488868426604323 | 0.6918080464880533 | 0.7960380934460616 | 0.10232383985699571 | 0.2917088789119689 | 0.0695 | 0.22476528833524 | 0.09109243306132322 | 1.6660267682211776 | 1.5542804803457522 | 13.042858477382078 | 18.28801310021742 | 2.4990667838755436 | 45.07197667390273 | 0.1081163125722616 | 0.04512229739322791 | 0.03329507276418465 | 0.79410782944646 | 0.11636452300326208 | 0.5155970149821228 | 0.5155970149821228 | 0.08344531465268795 |
| Food Wholesalers | 169 | 0.06287545454545455 | 0.02579436264604726 | 0.11488938343353311 | 0.23204263164290403 | 0.4847061410486548 | 0.6883974795696614 | 0.09373411886965897 | 0.31458186609200384 | 0.0695 | 0.4046727554679931 | 0.0769888537805454 | 5.369586205673487 | 0.4439028726022793 | 10.933264747622454 | 17.07657313824943 | 2.1616053317977144 | 45.479220835055926 | 0.05772507668534418 | 0.01189684837156351 | 0.005754462363766735 | 0.8507253470246667 | 0.1313375950156184 | 0.41004672915186663 | 0.4100467291518666 | 0.025686424038396192 |
| Furn/Home Furnishings | 362 | 0.09034418326693233 | 0.07587488118654037 | 0.1464127947186541 | 0.19416481758070114 | 1.0884231491124254 | 1.0821054084407624 | 0.12515201159357284 | 0.30125928200266844 | 0.0695 | 0.2042984087234449 | 0.11027956517121806 | 2.2818130755137274 | 1.0212678274664981 | 9.567276667618454 | 12.90366304775915 | 2.202709437099178 | 53.50768839525915 | 0.07338773485684795 | 0.0321538805708603 | 0.01910342536170239 | 0.8037173550256184 | 0.1353404441072435 | 0.5263838236002145 | 0.5263838236002145 | 0.07565572484687222 |
| Green & Renewable Energy | 248 | 0.1574820472440945 | 0.32890130702989834 | 0.06735338001368155 | 0.16194245636985027 | 0.7390903503257963 | 1.0336423067859184 | 0.12128465608151628 | 0.36974872492744715 | 0.0695 | 0.3839114729907757 | 0.09482152074005634 | 0.2293780785175985 | 7.524653979293316 | 14.030011705053287 | 22.59081317615253 | 1.9232200976937126 | 47.369779187704324 | 0.11304862660232423 | 0.385725295761713 | 0.24846525569738823 | 1.171130427953877 | 0.19282714525293054 | 0.3581348798742606 | 0.3581348798742606 | 0.32759318005707233 |
| Healthcare Products | 896 | 0.15152649797570858 | 0.15096971096104425 | 0.1352276726043494 | 0.18304340165470476 | 1.0775359783236322 | 1.1305011645147018 | 0.1290139929282732 | 0.43161496413982586 | 0.0695 | 0.11619162184556213 | 0.12010678468633545 | 0.9505702873128594 | 4.401980924665958 | 17.54319683749446 | 27.465650956358477 | 3.6045967641993903 | 55.29930642282753 | 0.24351064396568506 | 0.05653557319057285 | 0.10326654607578553 | 1.1082463831838485 | 0.07899234119529851 | 0.4789213443003872 | 0.47892134430038724 | 0.15422910964795478 |
| Healthcare Support Services | 460 | 0.14661127906976745 | 0.04230337105560238 | 0.24286107738383947 | 0.22635668993878802 | 0.920550044362433 | 1.0131363720531945 | 0.11964828248984492 | 0.38241271592555787 | 0.0695 | 0.21480632072052405 | 0.105193120444886 | 6.779006368941454 | 0.6858729021916748 | 11.670725837391533 | 15.975037197614578 | 2.827594063962792 | 41.59070570653649 | -0.03479074548612292 | 0.011193000384593066 | 0.01147731795337012 | 0.4668476016186193 | 0.10886237618760991 | 0.3753962472913868 | 0.37539624729138676 | 0.04182576089978843 |
| Heathcare Information and Technology | 447 | 0.20462864035087733 | 0.16006819885448872 | 0.16356639499180595 | 0.16972013476926534 | 1.2736117177372563 | 1.337779775787863 | 0.14555482610787146 | 0.45081477143098153 | 0.0695 | 0.10660654390272724 | 0.13561904545992257 | 1.0682277315056228 | 5.501359471663744 | 20.992704781338507 | 33.022761124162685 | 4.358930717477145 | 52.05237625764335 | 0.22881100885747016 | 0.07346369761166127 | 0.14879751394370175 | 1.4410021525209946 | 0.035050016747700995 | 0.35753705040317413 | 0.3575370504031741 | 0.16553367467046465 |
| Homebuilding | 171 | 0.07586536231884063 | 0.15495719798118576 | 0.17576561641927174 | 0.23537488242222698 | 0.9748955450608979 | 1.1397794466928413 | 0.12975439984608872 | 0.28509702105698664 | 0.0695 | 0.3153283743379511 | 0.10534796795444518 | 1.458885787217353 | 0.8544329496635298 | 5.03247083177265 | 5.629197243987296 | 1.1140152455630299 | 26.850355328605822 | 0.6166186684020648 | 0.006977927556165745 | 0.011182492565286405 | 0.7494600232935346 | 0.19431222567463893 | 0.16051300014034145 | 0.16051300014034142 | 0.14965402333568886 |
| Hospitals/Healthcare Facilities | 231 | 0.09018398692810456 | 0.11144592137589428 | 0.11635149727764249 | 0.21457189962085135 | 0.5707105333941709 | 0.7679402317477074 | 0.10008163049346705 | 0.31837828004373 | 0.0695 | 0.3398300472954005 | 0.0838624665060913 | 1.2424263296458609 | 2.3120736886481557 | 13.54146808270113 | 20.52622097197481 | 3.747968761278704 | 51.88238462148476 | 0.06402119507078356 | 0.06556376780458541 | 0.031508810674146785 | 0.567080322048612 | 0.15650807269310177 | 0.3177225637253474 | 0.31772256372534735 | 0.11084921823155379 |
| Hotel/Gaming | 650 | -0.0146983857442348 | 0.05797334423480763 | 0.021470742209970764 | 0.23239039501910805 | 0.7452374087131339 | 0.9705863973229032 | 0.11625279450636768 | 0.3499130792336531 | 0.0695 | 0.36056008478203067 | 0.09321356593771186 | 0.5631848527599266 | 3.89209590661724 | 16.45504646818514 | 74.0075291325496 | 3.1356479827955788 | 71.88670834443072 | 0.0074461963202217115 | 0.07436948211096218 | 0.01642156681135556 | 1.1479792696025544 | 0.022693214706000397 | 0.7620518976487767 | 0.7620518976487767 | 0.04168134383158712 |
| Household Products | 589 | 0.06879519553072619 | 0.14889539541413527 | 0.22892705098975522 | 0.21653101556185894 | 0.959250721543237 | 1.0240740179746777 | 0.12052110663437927 | 0.3789198008021104 | 0.0695 | 0.12288598649272289 | 0.11214436749935422 | 1.748546760596642 | 3.3530050782266416 | 17.791187993381833 | 22.186521995295013 | 5.242697635135145 | 74.72639864948364 | 0.06515419884833379 | 0.03436560599592606 | 0.026033477826032644 | 0.3541731509536776 | 0.19391815619878336 | 0.5998251790640028 | 0.5998251790640028 | 0.14841624764038996 |
| Information Services | 242 | 0.1099322137404581 | 0.20798720231291662 | 0.28674950161733914 | 0.19823094621386078 | 1.341638572668401 | 1.4107202256089806 | 0.15137547400359663 | 0.40765639840290036 | 0.0695 | 0.12308124671080803 | 0.13918783061052845 | 1.5812475805660275 | 5.475478442552351 | 18.24986278020042 | 24.82607377205625 | 5.258790303928886 | 54.49701097519528 | 0.029592502219401365 | 0.031231663406059016 | 0.025610685683135626 | 0.3652033807370103 | 0.14456373910874776 | 0.3060685793667489 | 0.3060685793667489 | 0.2143630738787314 |
| Insurance (General) | 206 | 0.06315289940828402 | 0.1040683015707577 | 0.11101717127867118 | 0.20597412821067834 | 0.6092906981965142 | 0.6906668147572236 | 0.09391521181762644 | 0.2527216619310413 | 0.0695 | 0.2918827858410955 | 0.08178431168834083 | 1.24965626436614 | 1.188008263499676 | 8.902201507197136 | 11.079319418780047 | 1.752157445449415 | 38.508132037411606 | 0.045398911100244445 | 0.008617396095773422 | 0.00675556803339109 | 0.4004151183998587 | 0.1109472421073442 | 0.3914994014939252 | 0.39149940149392526 | 0.10471297824825589 |
| Insurance (Life) | 142 | 0.10457288288288295 | 0.05656509696153738 | 0.039384734913749324 | 0.1574938581031083 | 0.7962762006298993 | 0.903786502197535 | 0.11092216287536329 | 0.23901505811759377 | 0.0618 | 0.4961765106368041 | 0.07898416265317341 | 0.8020176042590659 | 1.1271766774918102 | 11.129244835533825 | 16.271411386726815 | 1.2578747095304454 | 27.359392745137853 | -1.0607068814046108 | 0.006328163981822423 | 0.012637845656328256 | 0.24419652289647661 | 0.07018317898422892 | 0.45904302814741293 | 0.45904302814741293 | 0.05668933698504374 |
| Insurance (Prop/Cas.) | 235 | 0.06473863636363632 | 0.06378859935826829 | 0.06719791507014804 | 0.194916252646702 | 0.690694218235931 | 0.7457504789241671 | 0.09831088821814854 | 0.26692529380793906 | 0.0695 | 0.20181381932143566 | 0.08903622371755246 | 1.2439988186908715 | 1.1056855730020798 | 12.606428708454226 | 16.619567458404536 | 1.5933275666493296 | 20.31627414303407 | -0.4145486361178712 | 0.0068210247518077595 | 0.0027305540715448855 | 0.3442610375274731 | 0.0678709377123708 | 0.5494780979743276 | 0.5494780979743276 | 0.0641586747375173 |
| Investments & Asset Management | 1660 | 0.11960795744680854 | 0.2024143572291584 | 0.06259987647621855 | 0.16368981033632454 | 0.565197064061528 | 0.7921833492421216 | 0.1020162312695213 | 0.26550357638295474 | 0.0695 | 0.4325801594605201 | 0.08053348675084236 | 0.32929523205310735 | 4.638788774194115 | 12.5106314005126 | 15.16699627760411 | 1.4294350080625697 | 237.99123963506088 | NA | 0.038934740984049025 | 0.13382356189944222 | 0.9237689689292294 | 0.12311740738383642 | 0.47729614764336215 | 0.47729614764336215 | 0.20171069068869443 |
| Machinery | 1463 | 0.07435719478098793 | 0.09683834272379684 | 0.11441000402524393 | 0.22190417208531613 | 1.0629501446657796 | 1.1021402522422057 | 0.126750792128928 | 0.31622845943757366 | 0.0695 | 0.1471827018151237 | 0.11580092277095988 | 1.4166874133694627 | 1.9747841954393592 | 13.995107287843217 | 19.532098995488457 | 2.7467697368619257 | 38.91396414579239 | 0.28268996472541225 | 0.04058108687403752 | 0.052782923233098585 | 1.3529004573697616 | 0.10790104842911155 | 0.39724065432609074 | 0.3972406543260907 | 0.09625064801402965 |
| Metals & Mining | 1783 | 0.1499844536082474 | 0.16457676118489492 | 0.24562183011742217 | 0.26996966231622316 | 1.109674282355319 | 1.1980661936405959 | 0.13440568225251953 | 0.6169041114227474 | 0.0733 | 0.21009308863775686 | 0.11776866430269403 | 1.5541907800285226 | 1.1859212203390777 | 5.300524863110458 | 6.819439358368835 | 1.8251328688458563 | 76.7017355197327 | 0.10964360197616566 | 0.06302804437898227 | 0.03664201281241859 | 0.5713278427856452 | 0.2395479215961703 | 0.4721881026343019 | 0.4721881026343019 | 0.1652124790886806 |
| Office Equipment & Services | 144 | 0.06078017241379313 | 0.06875132589967149 | 0.10525106285728021 | 0.24108157389181584 | 0.8344943817237243 | 0.9252414781010465 | 0.1126342699524635 | 0.33105972711523934 | 0.0695 | 0.251315539118487 | 0.0974849893715909 | 1.8244325968890227 | 0.9905845551087058 | 8.527111891592835 | 13.29859632399348 | 1.7846844806000841 | 38.12834128674367 | 0.12932312282789618 | 0.023926107503514194 | 0.028513177071206312 | 1.093383155296316 | 0.057369127188005534 | 0.6348889054105977 | 0.6348889054105977 | 0.06994258414465422 |
| Oil/Gas (Integrated) | 36 | 0.14567833333333333 | 0.20335295617346388 | 0.27004010102815007 | 0.4199113849890901 | 1.0257376245751695 | 1.084261071514385 | 0.12532403350684793 | 0.290654684170079 | 0.0695 | 0.16268470683281316 | 0.11345298193785319 | 1.7857895827693153 | 1.1058383997115753 | 4.344885485844961 | 5.428064564430289 | 2.0049151503678555 | 9.000796473446796 | 0.03181770713774633 | 0.057508156555064825 | 0.010887406636895138 | 0.25434157304490956 | 0.27383892566202067 | 0.3730334426019616 | 0.3730334426019616 | 0.20370003311353505 |
| Oil/Gas (Production and Exploration) | 616 | 0.30223883792048944 | 0.3936986684738406 | 0.31379162613860156 | 0.2858017870579106 | 1.1719532510287904 | 1.3064445801888949 | 0.1430542774990738 | 0.5761526246802835 | 0.0733 | 0.20768151674921126 | 0.12481207563597795 | 0.8612173109220987 | 2.0731720837297396 | 3.747210169472445 | 5.162435727811072 | 1.730060677123998 | 15.176434666764806 | -0.034048080229958685 | 0.19112684090849405 | 0.10412878403283038 | 0.3997910899166188 | 0.3455460999098248 | 0.23995987250134324 | 0.2399598725013432 | 0.39485854644800417 |
| Oil/Gas Distribution | 166 | 0.1644844915254237 | 0.10430118720988638 | 0.0678584280776384 | 0.15515930094367683 | 0.640895646239336 | 0.9598833157432468 | 0.1153986885963111 | 0.3169291940181764 | 0.0695 | 0.4226618808458241 | 0.08875224986851327 | 0.730092630826344 | 2.1330247885411833 | 11.70001206424556 | 18.500278519062103 | 1.8164371624196047 | 40.13651377973176 | 0.03914602540752784 | 0.08237881928404911 | 0.04908036915449947 | 0.7280760838784098 | 0.08474579001092297 | 1.105935409235271 | 1.105935409235271 | 0.1052863696769992 |
| Oilfield Svcs/Equip. | 455 | 0.07271242074927951 | 0.06418335019399797 | 0.14865827167185494 | 0.22426511994986614 | 0.9186144133116347 | 1.1458047060134187 | 0.1302352155398708 | 0.38678554871410087 | 0.0695 | 0.3178052007067643 | 0.10548427143575564 | 2.613156854484068 | 0.6101380910433795 | 6.716267645644465 | 9.173729012533544 | 1.5357699086396315 | 28.410647467275698 | 0.06927071634289768 | 0.03082502336735689 | 0.017349901508777407 | 0.8724978379751093 | 0.16953802063524387 | 0.2379445180748172 | 0.2379445180748172 | 0.06475503420502594 |
| Packaging & Container | 414 | 0.07722906752411571 | 0.0857266219408809 | 0.11313229318848557 | 0.21261531513898216 | 0.6454232908587869 | 0.8357668353157656 | 0.10549419345819809 | 0.2944983294261341 | 0.0695 | 0.3286070606384269 | 0.08803206569661348 | 1.5638858386300616 | 1.2245297647229045 | 8.80602419200883 | 14.003272248254996 | 1.940650938180684 | 125.25944123508474 | 0.133953568149121 | 0.06156585766040262 | 0.044226653802734196 | 0.9928604400872373 | 0.12941444561462065 | 0.3914902411225463 | 0.39149024112254627 | 0.08663675761346684 |
| Paper/Forest Products | 268 | 0.09014720379146919 | 0.13562433135317445 | 0.10812075767476295 | 0.20345272338936696 | 0.752359681166661 | 0.9932645149292465 | 0.11806250829135387 | 0.3119027435891214 | 0.0695 | 0.3803895840218627 | 0.09306780929206306 | 0.9505751229073717 | 1.1570645686768584 | 6.042835916020339 | 8.335186022408996 | 1.0735483341618237 | 22.787221865495614 | 0.1982744747226807 | 0.08171337157562483 | 0.05544250852297262 | 0.7654706757504107 | 0.1507533967166234 | 0.227065803635393 | 0.22706580363539297 | 0.13522755335680517 |
| Power | 485 | 0.13698196428571432 | 0.008895202035659498 | 0.00563795095811195 | 0.19309502380562807 | 0.4433046474349577 | 0.7285185003020899 | 0.09693577632410677 | 0.25944771221610685 | 0.0695 | 0.4901853479170663 | 0.07508261435078543 | 0.7289648755018722 | 1.7852315254855147 | 11.802718510592392 | 185.00972997805684 | 1.4577656930951783 | 35.26387209099931 | -0.06430049295731272 | 0.12634435319825676 | 0.06880299151465613 | NA | 0.025145559391345728 | 2.356379147694775 | 2.356379147694775 | 0.00906508790580155 |
| Precious Metals | 930 | 0.22946125628140696 | 0.16469671534866936 | 0.1313128227330175 | 0.2792709866638391 | 1.1011319908908235 | 1.1408458156282186 | 0.12983949608713186 | 0.6291256354607682 | 0.0733 | 0.15433126027989771 | 0.11832289524433443 | 0.8276052758766798 | 2.2398890646875773 | 6.96818464128658 | 12.579527614682526 | 1.5934497426010152 | 627.2258029164234 | 0.11475012262399167 | 0.1744908004226363 | 0.11013130656603419 | 1.0172987135360556 | 0.07853502773368998 | 0.7362517184310616 | 0.7362517184310616 | 0.1654542987145614 |
| Publishing & Newspapers | 327 | 0.01678699248120301 | 0.06804740546774375 | 0.06981604588824067 | 0.16412591831025117 | 0.8690395285125317 | 0.8891333269114582 | 0.10975283948753436 | 0.31440209547156556 | 0.0695 | 0.22992110847420524 | 0.09655571515981545 | 1.2217649449167178 | 1.160223297152856 | 9.646828087669416 | 16.151701374998392 | 1.3219210745300178 | 33.167267570476426 | 0.11020902121217334 | 0.03244988786153133 | 0.025056726303420367 | 0.6145780113129105 | 0.029633954369228457 | 0.8964870051888695 | 0.8964870051888695 | 0.06659800858756872 |
| R.E.I.T. | 792 | 0.09401075971731436 | 0.3380360095549865 | 0.035771025211289796 | 0.044876200270087915 | 0.5091699845154034 | 0.7926064302783233 | 0.1020499931362102 | 0.188502700447128 | 0.0618 | 0.4393257428399891 | 0.07766914836745716 | 0.11475356271315791 | 11.531042195662517 | 20.236307238218217 | 31.551898219621943 | 1.391744101394269 | 29.010844155919504 | 0.8890614473750629 | 0.051005426695245375 | 0.02588346131024639 | 0.09464086024167101 | 0.09251907543804368 | 0.700883928299942 | 0.700883928299942 | 0.32145434499735054 |
| Real Estate (Development) | 869 | 0.07365129807692308 | 0.104902718722365 | 0.04648881319983875 | 0.32537487639676393 | 0.5012546023244221 | 1.0176524508975406 | 0.12000866558162374 | 0.32556181158049086 | 0.0695 | 0.6695039083900662 | 0.0747138368802717 | 0.5289327050081074 | 1.5312131208338273 | 10.217278961542926 | 12.510382289782783 | 0.4758144097001887 | 93.42863689228729 | 1.8806993528177163 | 0.02276963315121998 | 0.017039267244275656 | 0.1627838126945403 | 0.045763966797147754 | 1.0751257428507728 | 1.0751257428507728 | 0.10454275297579443 |
| Real Estate (General/Diversified) | 342 | 0.049859999999999995 | 0.14757079111695964 | 0.030628603680595022 | 0.2669365744455201 | 0.5297027575571283 | 0.9342277663512191 | 0.11335137575482727 | 0.26803347575607533 | 0.0695 | 0.5549975323855354 | 0.07949817697804118 | 0.23569371461739638 | 3.4160312457346205 | 13.346468325691228 | 20.678663385063345 | 0.6426846173012669 | 44.690395758888215 | 1.1832741086452718 | 0.09111187537645547 | 0.07170612677804328 | 0.9313423813623101 | 0.04032974827255095 | 0.5449814663364241 | 0.5449814663364241 | 0.15380910896269037 |
| Real Estate (Operations & Services) | 730 | 0.09982331250000012 | 0.1442484586934426 | 0.03214955502598619 | 0.22618473161019664 | 0.5521553535566948 | 0.9011880677232457 | 0.110714807804315 | 0.29972973723472146 | 0.0695 | 0.4971049352614197 | 0.08170353620567418 | 0.25341437544914164 | 3.720335983846671 | 16.148892324279235 | 23.69469503174183 | 0.8197490370417182 | 23.760402106394217 | 0.21232391694041827 | 0.023909758518659972 | 0.0771748720242712 | 0.8899927087212333 | 0.06526558844500861 | 0.5321152690956676 | 0.5321152690956676 | 0.14816464671686094 |
| Recreation | 323 | 0.05107673913043481 | 0.10008498258676168 | 0.08731459038120859 | 0.23260571570121216 | 0.9858976233637634 | 1.1091960963190381 | 0.12731384848625923 | 0.33179399049670577 | 0.0695 | 0.24702270915957644 | 0.10879715009294032 | 1.0486354163424807 | 2.0974276344108858 | 12.274712507193845 | 20.530732767244604 | 2.5725258921040592 | 47.175784717711394 | 0.31389391948549566 | 0.06850083656836245 | 0.06105344162327375 | 1.3640377199332356 | 0.0752427025591887 | 0.5684787631638673 | 0.5684787631638673 | 0.09680897325302346 |
| Reinsurance | 34 | 0.031153928571428572 | 0.016007690019154888 | 0.022689180850825514 | 0.1797815920356975 | 1.0895323174584777 | 1.1599096579998216 | 0.13136079070838574 | 0.28323303408098666 | 0.0695 | 0.2601501525257125 | 0.11080725310758553 | 1.573369170807917 | 0.6961979092565854 | 17.766280415975285 | 37.82912656295559 | 1.3931599445632008 | 15.643852704032815 | -0.5262438372366781 | 0.0007592445164573144 | 0.016224944864916987 | 2.894211893464081 | 0.01983346830319306 | 1.15165212446575 | 1.15165212446575 | 0.015999325835102884 |
| Restaurant/Dining | 382 | -0.0028214814814814916 | 0.10371730864332976 | 0.1298363222896256 | 0.20821250637663763 | 0.8289252878100836 | 0.9953207368095935 | 0.11822659479740556 | 0.31360962157417 | 0.0695 | 0.24614511902439928 | 0.1020124632613438 | 1.6243248607297194 | 2.868461691832777 | 16.545467724021872 | 30.621314288660123 | 14.381817822236322 | 55.54456171028163 | -0.0077442229665044505 | 0.045756035907612375 | 0.02472354131779093 | 0.37280426770845015 | 0.36850752125706215 | 0.6213721003208682 | 0.6213721003208682 | 0.09194255405962456 |
| Retail (Automotive) | 193 | 0.08818880597014925 | 0.050574673529283576 | 0.12384134362101419 | 0.23668024474890867 | 0.7185689332312892 | 0.9831339521946365 | 0.11725408938513199 | 0.3042116382969305 | 0.0695 | 0.36886129425022746 | 0.09331508751902975 | 3.174007342761481 | 0.716728345244149 | 9.632044946300764 | 14.248870595972095 | 3.131419321340359 | 24.10470482847775 | 0.0962362664274681 | 0.017901244840279967 | 0.0331790510863578 | 1.269679651746447 | 0.2126705193456336 | 0.2565658841379044 | 0.2565658841379044 | 0.04834333888362152 |
| Retail (Building Supply) | 98 | 0.04973098591549296 | 0.12456492607372097 | 0.29843243697346 | 0.24858851652914152 | 0.9343776592100076 | 1.0792224241204762 | 0.124921949444814 | 0.27792365922032364 | 0.0695 | 0.1938870167017119 | 0.1108520340792542 | 3.010113682204317 | 1.7330803063087947 | 11.182812043204136 | 13.9844036785419 | 16.942098977439436 | 20.808375889952647 | 0.10268186081306206 | 0.023713589272572867 | 0.0055379604041460315 | 0.4152885052448525 | 0.6206917097421666 | 0.4052393345949006 | 0.4052393345949006 | 0.12376877725925094 |
| Retail (Distributors) | 1006 | 0.07350015193370167 | 0.05478305696045563 | 0.08965288670125256 | 0.2289235703963501 | 0.5976015996949612 | 0.828851939037752 | 0.10494238473521261 | 0.3263950009608495 | 0.0695 | 0.4090616310320472 | 0.08343063747365659 | 1.961608220217619 | 0.7338344343338278 | 10.202912254657335 | 12.808650887242223 | 1.5112950518177228 | 51.298192963003395 | 0.16339131497172923 | 0.02512781315946815 | 0.03550961521616087 | 1.262069454218156 | 0.1490470679743058 | 0.3097477147444369 | 0.30974771474443696 | 0.05521002060274814 |
| Retail (General) | 189 | -0.02896084848484848 | 0.047344064491521044 | 0.116496913492536 | 0.2542058798952405 | 0.7347606574412107 | 0.8905370562593125 | 0.10986485708949313 | 0.27275967897216363 | 0.0695 | 0.2673153785851877 | 0.09449141411423916 | 3.094463195580101 | 0.8645649495119073 | 11.278125345956994 | 18.60676665621412 | 3.3512422579158496 | 36.6803578577689 | 0.0051208978463735495 | 0.030384482805711776 | 0.012404123717395098 | 0.7924199763424997 | 0.12667539417897708 | 0.4656995364488768 | 0.46569953644887674 | 0.04611346599102132 |
| Retail (Grocery and Food) | 181 | 0.04653013605442181 | 0.045257568991636785 | 0.109306157945409 | 0.23438924127155367 | 0.5285453639501723 | 0.7054027356915712 | 0.09509113830818738 | 0.2395250060619005 | 0.0618 | 0.3667013079664705 | 0.07729248420354712 | 3.1264014495235903 | 0.6481472332531077 | 9.039827811087216 | 14.284968868266562 | 2.3047587413431696 | 35.31701889554453 | -0.029975171328978954 | 0.027134911493777378 | 0.007842661483642958 | 0.2602099264724294 | 0.14692867887469693 | 0.33680698768837153 | 0.3368069876883715 | 0.04435850622262196 |
| Retail (Online) | 342 | 0.165509806451613 | 0.001796702508674976 | 0.01927410279592016 | 0.040840600088228 | 1.490503406647991 | 1.59201027229133 | 0.16584241972884814 | 0.463507362871258 | 0.0695 | 0.17038387188172086 | 0.14650588299606426 | 1.3082127267773387 | 2.0433500802590556 | 16.99833982445618 | NA | 4.242583801017513 | 90.30258828421724 | -0.022871400697795554 | 0.09495224294932071 | 0.06433562988524151 | NA | -0.0012913862822285392 | 0.0038494175802843227 | 0.0038494175802843422 | 0.014596961257935463 |
| Retail (Special Lines) | 495 | 0.027746815642458116 | 0.05641111965341764 | 0.12108557504627562 | 0.2303949764378388 | 0.9561788887224327 | 1.0901256163386903 | 0.12579202418382748 | 0.3179110026698966 | 0.0695 | 0.23738748343322327 | 0.1083588395201397 | 2.517458578419333 | 1.1055168146420087 | 10.562927567967403 | 18.29261382753738 | 3.3664874019124715 | 29.906383975982227 | 0.08366894760629288 | 0.02245102870529796 | 0.006820813718851705 | 0.6221607841938781 | 0.12040782319843941 | 0.525527360937459 | 0.525527360937459 | 0.058366703266215236 |
| Rubber& Tires | 89 | 0.05632847222222228 | 0.07506181514407724 | 0.06727892421800931 | 0.21697853221406468 | 0.9300642456688291 | 1.1594988998620432 | 0.13132801220899104 | 0.2773476779488968 | 0.0695 | 0.3385984307682709 | 0.10458765411300318 | 1.0936166560589926 | 0.9747736810052285 | 7.111957993106612 | 12.765153148732912 | 1.1120791343085825 | 60.49035251341204 | 0.24507414707859465 | 0.062484383129195534 | 0.0220363021122004 | 1.2578311950085885 | 0.06908005021114555 | 0.45219331797462237 | 0.45219331797462237 | 0.07357856242634954 |
| Semiconductor | 624 | 0.0881332808988765 | 0.22958951515279774 | 0.18215285247984078 | 0.12833630069414675 | 1.6715997850986177 | 1.6915425349552258 | 0.173785094289427 | 0.3734495183367034 | 0.0695 | 0.10404370853456175 | 0.16115098932344296 | 0.8349677090419115 | 3.7548796165230502 | 10.50343169900737 | 15.99695109228836 | 3.261468298173543 | 74.13312031594663 | 0.16627221479469054 | 0.18860060299516715 | 0.12206170568941127 | 0.8761502378982206 | 0.22004463854331047 | 0.32598202249818786 | 0.32598202249818786 | 0.24193399820083566 |
| Semiconductor Equip | 342 | 0.10496736842105271 | 0.243701326742863 | 0.2638646798167927 | 0.16461321416951447 | 1.9829052012920763 | 1.9625184452168636 | 0.1954089719283057 | 0.33267871506038227 | 0.0695 | 0.06620462453544781 | 0.18593809439548178 | 1.2343126023017275 | 4.144186999373605 | 14.386690785614098 | 16.622260371440802 | 5.367884030333931 | 28.744369420890074 | 0.2930989808104489 | 0.08251851194368172 | 0.11219404476537231 | 0.8957706537744446 | 0.303218181012323 | 0.24045618885891673 | 0.24045618885891673 | 0.24894160017681496 |
| Shipbuilding & Marine | 349 | 0.1134618587360595 | 0.3319202975644092 | 0.32699317521985316 | 0.09290437076591629 | 1.0486074968125012 | 1.095060022552661 | 0.12618578979970235 | 0.33913461678437984 | 0.0695 | 0.3334209359136372 | 0.10156884204183424 | 1.1192465562494063 | 1.0044824108835042 | 2.5752079359512443 | 2.9370669871985133 | 0.9029836098617678 | 17.544139036158338 | 0.0326299198511205 | 0.06850006802327047 | 0.03711561558510823 | 0.10442336279857994 | 0.5220397735363365 | 0.31311541565817647 | 0.31311541565817647 | 0.33302425887017123 |
| Shoe | 85 | 0.0027776190476190526 | 0.09940805273593413 | 0.17156391646728414 | 0.16296001845602212 | 0.979181546711328 | 1.0205314602380813 | 0.12023841052699888 | 0.352542931120207 | 0.0695 | 0.11028060105470616 | 0.1127521155300474 | 2.0177263229114235 | 2.4223029557587625 | 17.7124727617004 | 23.47411167886975 | 5.25688738442242 | 44.47942818320377 | 0.23433778345356734 | 0.018699871340976237 | 0.01390321544847365 | 0.5573454463625495 | 0.21068525458903517 | 0.30772156513652943 | 0.3077215651365295 | 0.0993085614798471 |
| Software (Entertainment) | 320 | 0.14282 | 0.229534639629829 | 0.15976086690423852 | 0.15681674531735063 | 1.4648921606853302 | 1.4800451918455317 | 0.15690760630927342 | 0.47746935346140246 | 0.0695 | 0.0672828948060113 | 0.14987296056339064 | 0.6884770819828501 | 3.851107829519534 | 12.118199448898602 | 16.402238187938835 | 3.5083472685377823 | 127.3905077202935 | 0.03163679719751255 | 0.11085585663611436 | 0.12181383405728993 | 0.6400453768028459 | 0.18663687839130547 | 0.027321544447000384 | 0.027321544447000412 | 0.25356431486459097 |
| Software (Internet) | 152 | 0.27269325301204816 | -0.02010271295519131 | 0.00551203420754335 | 0.20940716004868964 | 1.2628480564068731 | 1.3494055466433648 | 0.1464825626221405 | 0.4324304510301731 | 0.0695 | 0.14289541246400556 | 0.1330320728550001 | 0.8701272630451327 | 4.1806294495066085 | 15.88141959009356 | NA | 4.608321834532484 | 69.66940045110383 | 0.05014284936774209 | 0.06899492579820862 | 0.10911160059070062 | NA | -0.14640466217181433 | 0.004152920486276557 | 0.004152920486276579 | 0.0046187908283204715 |
| Software (System & Application) | 1648 | 0.16911827995255052 | 0.17725169673656516 | 0.173054641209129 | 0.18564555974970864 | 1.3178605209622307 | 1.3540948759786284 | 0.14685677110309453 | 0.4454074927960674 | 0.0695 | 0.08207902347015307 | 0.13910010466338735 | 0.9464783178759009 | 6.718013801362313 | 21.774817579847788 | 33.846686642289974 | 6.765091742203532 | 81.17018650247125 | 0.1404197930489799 | 0.07171756785190525 | 0.17698341089820932 | 1.4772666888447972 | 0.13415189960739474 | 0.42167938062996485 | 0.4216793806299648 | 0.19688448580761525 |
| Steel | 710 | 0.17691252873563204 | 0.11983144761390822 | 0.15474452778417921 | 0.2080865325449755 | 1.0387463631868152 | 1.2339858111510127 | 0.1372720677298508 | 0.36054916600984277 | 0.0695 | 0.32124888739024365 | 0.10999234538941745 | 1.5324538849846425 | 0.6825263094067728 | 4.2421310055380514 | 5.496146871010761 | 1.0334392437356485 | 34.010112280980266 | 0.1414384207393182 | 0.04698646040049268 | 0.031233063526508904 | 0.6906094052657653 | 0.19513585801447908 | 0.34425266167339813 | 0.3442526616733981 | 0.11976279919759207 |
| Telecom (Wireless) | 99 | 0.03986386666666666 | 0.1461290784707081 | 0.07185380499516585 | 0.26856038903020835 | 0.5994486949624184 | 0.8356105248266873 | 0.10548171988116964 | 0.27376891988486907 | 0.0695 | 0.4099713522947748 | 0.08370102020712183 | 0.5987566952531977 | 2.1639337464462898 | 6.767435125348608 | 14.969037905540716 | 1.4016862038068374 | 24.327805212795383 | -0.06568226483759157 | 0.17045118193113834 | 0.010045620758875377 | 0.23431849746915523 | 0.05965610107384498 | 0.9456620401040134 | 0.9456620401040134 | 0.14331345320592245 |
| Telecom. Equipment | 461 | 0.04452939890710383 | 0.1080388305879011 | 0.12105446393642671 | 0.16798552646066092 | 1.1754366702843682 | 1.1987978378632358 | 0.1344640674614862 | 0.35575957529107116 | 0.0695 | 0.12271568825108702 | 0.12438791697109762 | 1.2296782460866211 | 2.2056685736550157 | 13.982133050228981 | 19.267327671178666 | 3.278906654561631 | 48.3299995603607 | 0.24547671050793304 | 0.030967972014556554 | 0.03506719178754258 | 0.8097902080671712 | 0.12699399947863158 | 0.481182189709579 | 0.48118218970957893 | 0.1076245089719039 |
| Telecom. Services | 295 | 0.09371924882629107 | 0.14564770212095915 | 0.08300284823336357 | 0.20636862175772658 | 0.5328634384133827 | 0.83120448295402 | 0.1051301177397308 | 0.3323458822442584 | 0.0695 | 0.45523285018801557 | 0.08110485457071243 | 0.6630252862487998 | 2.093834198101839 | 6.814314301939763 | 14.316491404336567 | 1.340689090628011 | 38.64289325311667 | 0.008498171222058069 | 0.15451691162113007 | 0.0018398303676254975 | 0.06304137212091086 | 0.0979275807590621 | 0.6396927455260507 | 0.6396927455260507 | 0.145102802727752 |
| Tobacco | 56 | 0.09822864864864865 | 0.3347455940886112 | 0.20013728578995296 | 0.26807548682122645 | 0.7752611377217213 | 0.8928613188910068 | 0.11005033324750234 | 0.28815132980992253 | 0.0695 | 0.21150591899864943 | 0.09784729128820867 | 0.7348318283964261 | 3.7714885665907185 | 10.1574324151006 | 11.217270381251886 | 3.4958341314126 | 12.602231253306266 | 0.14326577092025009 | 0.02711402687189442 | 0.012922319142159418 | 0.054294763263544675 | 0.22341989038959192 | 0.9118074888631233 | 0.9118074888631233 | 0.3353339430515232 |
| Transportation | 302 | 0.10729344497607662 | 0.07881680701739548 | 0.1272026410977261 | 0.23989417549818295 | 0.8308679841758 | 1.0148110401540846 | 0.11978192100429595 | 0.3108429730265392 | 0.0695 | 0.3114596720976668 | 0.0987809518489558 | 1.946084293103231 | 0.98900039785159 | 7.892759281839684 | 12.289046954707567 | 1.9154341025484678 | 27.907558356540434 | 0.046289247811254666 | 0.04140717087920493 | 0.02130435789572665 | 0.5637129375151047 | 0.18047586417013964 | 0.3759045643575265 | 0.3759045643575265 | 0.07901879530087233 |
| Transportation (Railroads) | 50 | 0.005131860465116275 | 0.22937544917128982 | 0.063106474006416 | 0.23455439053515723 | 0.5377120552489277 | 0.6726147258124854 | 0.09247465511983632 | 0.1904649831765268 | 0.0618 | 0.28093173916735564 | 0.07957406875741202 | 0.35264141209829214 | 4.951455019190415 | 14.391882936833516 | 21.521720661372516 | 2.5233071875662696 | 47.9261460652161 | 0.05654029435972825 | 0.15530197652565753 | 0.0810738480621294 | 0.4977785042793617 | 0.10779442786699867 | 0.42288213474408926 | 0.4228821347440892 | 0.22782025938466396 |
| Trucking | 220 | 0.06741228758169934 | 0.08182596046987545 | 0.09325941401187661 | 0.25137746140461076 | 0.8010306050790537 | 1.0796626585301576 | 0.12495708015070657 | 0.31796488514967647 | 0.0695 | 0.3702800613864154 | 0.09807373677368159 | 1.2683662093737476 | 1.4582532006532531 | 7.181217894930429 | 13.577420148175593 | 2.309362540030248 | 20.393774092471542 | 0.06163128475096366 | 0.09057248620729061 | 0.06533309945749276 | 1.2953650987044991 | 0.048007666832446935 | 0.47214545338387454 | 0.4721454533838745 | 0.08797114269009386 |
| Utility (General) | 51 | 0.07792022222222221 | 0.11456119771994193 | 0.07671442300374834 | 0.18951235707131556 | 0.4455522909876226 | 0.6809328539400714 | 0.0931384417444177 | 0.1837333836003369 | 0.0618 | 0.4464746906686224 | 0.0723396407381269 | 0.7959257267099653 | 2.0587197648578983 | 11.022432960755802 | 17.92087009693338 | 1.607781228867751 | 19.959924071772317 | 0.02188278733810659 | 0.1391916397622712 | 0.07441384804679939 | 1.1281129759412232 | 0.12706804579670924 | 0.5680817786729803 | 0.5680817786729803 | 0.11417047367535862 |
| Utility (Water) | 104 | 0.07992173333333334 | 0.23308027198201 | 0.06008372259938548 | 0.195506447122988 | 0.48577767777887526 | 0.7403783627900649 | 0.09788219335064718 | 0.2917020473638641 | 0.0695 | 0.4525850505503244 | 0.07727697206634727 | 0.2960000594907215 | 4.753546236463749 | 12.93134872040161 | 20.069056769362522 | 1.5000124500603853 | 27.005335813319128 | 0.04297943947729448 | 0.21460584021765075 | 0.11132379540777157 | 0.9907467875890142 | 0.05007048841854516 | 0.8066063741040713 | 0.41572668892840536 | 0.23300787604616452 |

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

| Yes/No | Book or Market Value | ERP choices | Cost of debt | Synthetic rating | Beta | Rating is | Region | Cost of Capital Approach |
|---|---|---|---|---|---|---|---|---|
| Yes | B | Will input | Direct input | 1 | Direct input | Aaa/AAA | US | I will input |
| No | V | Country of incorporation | Synthetic rating | 2 | Single Business(US) | Aa2/AA | Emerging Markets | Detailed |
|  |  | Operating countries | Actual rating |  | Single Business(Global) | A1/A+ | Europe | Industry Average |
|  |  | Operating regions |  |  | Multibusiness(US) | A2/A | Japan | Distribution |
|  |  |  |  |  | Multibusiness(Global) | A3/A- | Global |  |
|  |  |  |  |  |  | Baa2/BBB |  |  |
|  |  |  |  |  |  | Ba1/BB+ |  |  |
|  |  |  |  |  |  | Ba2/BB |  |  |
|  |  |  |  |  |  | B1/B+ |  |  |
|  |  |  |  |  |  | B2/B |  |  |
|  |  |  |  |  |  | B3/B- |  |  |
|  |  |  |  |  |  | C2/C |  |  |
|  |  |  |  |  |  | Ca2/CC |  |  |
|  |  |  |  |  |  | Caa/CCC |  |  |
|  |  |  |  |  |  | D2/D |  |  |
