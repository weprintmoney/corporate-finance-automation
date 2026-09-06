---
title: "Illamgenno2024"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/inv4ed/illAmgenNo2024.xlsx
---

# Illamgenno2024

Source: https://www.stern.nyu.edu/~adamodar/pc/inv4ed/illAmgenNo2024.xlsx

Sheets: Input sheet, Valuation output, Stories to Numbers, Valuation as picture, Diagnostics, Option value, Synthetic rating, R& D converter, Operating lease converter, Cost of capital worksheet, Failure Rate worksheet, Country equity risk premiums, Industry Averages(US), Industry Average Beta (Global), Input Stat Distributioons, Trailing 12 month Worskheet, Answer keys

## Input sheet

| Input cell | Calculated cell |
|---|---|
| Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |  |
| There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
| Last 10K before LTM |  |
| 26323 |  |
| 10069 |  |
| 1406 |  |
| 3661 |  |
| 39640 |  |
| If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |  |
| If you lease or other contractual commitments that have not been converteed to debt already, say yes to this option and do the conversion. |  |
| 9305 |  |
| 3162 |  |
| 0 |  |
|  | Computed numbers: Here is what your company's numbers look like, relative to industry. |
|  | If you are not working in US dollars, you should add the inflation differential to the industry averages. |
|  |  |
|  |  |
|  | Revenue growth in the most recent year = |
| Growth Lever - Next year | Pre-tax operating margin in the most recent year = |
| Profitability Lever - Next year | Sales to capital ratio in most recent year = |
| Growth Lever - Long term | Marginal sales to capital ratio  = |
| Profitability Lever - Long term | Return on invested capital in most recent year= |
| Speed of convergence level | Standard deviation in stock prices = |
| Efficency of Growth Lever (first 5 years) | Cost of capital = |
| Efficency of Growth Lever (years 6-10) |  |
|  | Valuation Output Feedback (for you to use to fine tune your inputs, if you want) |
|  | Revenues in year 10, based on your revenue growth = |
| Do not input. Go to cost of capital sheet. | Pre-tax Operating Income in year 10, based on your operating margin = |
|  | Return on invested capital in year 10, based on your sales/capital ratio = |
|  | Check the Diagnostics worksheet for more details. |
|  |  |
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
|  | 0.09 | 0.09 | 0.09 | 0.09 | 0.09 | 0.08 | 0.07 | 0.06 | 0.05 | 0.04000000000000001 | 0.04 |
| 28190 | 30727.100000000002 | 33492.539000000004 | 36506.86751000001 | 39792.485585900016 | 43373.80928863102 | 46843.7140317215 | 50122.77401394201 | 53130.140454778535 | 55786.647477517465 | 58018.11337661817 | 60338.837911682895 |
| 0.2896062433487052 | 0.2896062433487052 | 0.33376374600922315 | 0.3558424973394821 | 0.3779212486697411 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 |
| 8164 | 8898.76 | 11178.595280000001 | 12990.694904800004 | 15038.425840296008 | 17349.523715452407 | 18737.4856126886 | 20049.109605576807 | 21252.056181911415 | 22314.65899100699 | 23207.245350647267 | 24135.535164673158 |
| 0.145 | 0.145 | 0.145 | 0.145 | 0.145 | 0.145 | 0.16599999999999998 | 0.18699999999999997 | 0.20799999999999996 | 0.22899999999999995 | 0.24999999999999994 | 0.25 |
| 6980.22 | 7608.4398 | 9557.698964400002 | 11107.044143604004 | 12857.854093453087 | 14833.842776711808 | 15627.063000982293 | 16299.926109333945 | 16831.62849607384 | 17204.60208206639 | 17405.43401298545 | 18101.65137350487 |
|  | 1843.6260000000013 | 2009.5523400000045 | 2190.4120506000036 | 2387.5491351540018 | 2313.2698287269886 | 819.7649955551278 | 751.8416102091305 | 664.1267556847324 | 557.8664747751754 | 580.181133766182 | 4525.412843376217 |
|  | 5764.813799999999 | 7548.146624399998 | 8916.632093004 | 10470.304958299084 | 12520.57294798482 | 14807.298005427165 | 15548.084499124814 | 16167.501740389109 | 16646.735607291215 | 16825.252879219268 | 13576.238530128652 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0.09261706048908777 | 0.09261706048908777 | 0.09261706048908777 | 0.09261706048908777 | 0.09261706048908777 | 0.09009364839127022 | 0.08757023629345267 | 0.08504682419563513 | 0.08252341209781758 | 0.08000000000000003 | 0.08 |
|  | 0.9152337412271143 | 0.8376528010805805 | 0.7666481069823514 | 0.7016622151581424 | 0.6421849342568912 | 0.5891098762061496 | 0.5416752468455689 | 0.49921831460787197 | 0.46116167930302676 | 0.4270015549102099 |  |
|  | 5276.152101651696 | 6322.726162895587 | 6835.919114759598 | 7346.617370421418 | 8040.523315460241 | 8723.125494924763 | 8422.012509039198 | 8071.112970256888 | 7676.836547571907 | 7184.409141184114 |  |
| 13576.238530128652 |  |  |  |  |  |  |  |  |  |  |  |
| 0.08 |  |  |  |  |  |  |  |  |  |  |  |
| 339405.9632532163 |  |  |  |  |  |  |  |  |  |  |  |
| 144926.87405492092 |  |  |  |  |  |  |  |  |  |  |  |
| 73899.43472816539 |  |  |  |  |  |  |  |  |  |  |  |
| 218826.3087830863 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  | 339412.5 |  |  |  |
| 109413.15439154315 |  |  |  |  |  |  |  |  |  |  |  |
| 218826.3087830863 |  |  |  |  |  |  |  |  |  |  |  |
| 65423 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 10944 |  | If you get Value Errors all over, it is usually because your option worksheet has gone haywire. The fix is very low tech. Go into the option value worksheet, and in cell B17 of that worksheet (adjusted S), enter any number (say 5) and then undo what you did. Voila! |  |  |  |  |  |  |  |  |  |
| 4454 |  |  |  |  |  |  |  |  |  |  |  |
| 168801.3087830863 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 168801.3087830863 |  |  |  |  |  |  |  |  |  |  |  |
| 535.5 |  |  |  |  |  |  |  |  |  |  |  |
| 315.2218651411509 |  |  |  |  |  |  |  |  |  |  |  |
| 311.29 |  |  |  |  |  |  |  |  |  |  |  |
| 0.9875266738257822 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 4 | 4 | 4 | 4 | 4 |  |
| 60711 | 62554.626000000004 | 64564.178340000006 | 66754.5903906 | 69142.139525754 | 71455.40935448099 | 72275.17435003612 | 73027.01596024525 | 73691.14271592998 | 74249.00919070515 | 74829.19032447133 |  |
| 0.11497455156396699 | 0.12532226120472403 | 0.1527896428379254 | 0.17203106163782403 | 0.19261378158742556 | 0.2145412750958699 | 0.21869671088802342 | 0.22552593274132723 | 0.2304849551190304 | 0.23346906355337646 | 0.23441974785522587 | 0.16 |

## Stories to Numbers

| Amgen | 2024-05-01 00:00:00 |
|---|---|
| The Biotech Giant is grown up |  |
| Amgen, a biotech pioneer, has scaled up, and as it has become bigger, it has found it more difficult to sustain its high revenue growth from previous years. We exepcted moderate revenue growth, driven by drugs in the pipeline and a recovery in operating margins to a ten-year norm (and close to the third quartile of drug companies). While the company will continue to invest heavily in R&D for the next five years, it will scale down that investment in years 6-10, as it approaches stable growth. In stable growth, the company will continue to earn excess returns, with it strong competitive advantages, and see its cost of capital decline to that of an average firm.  |  |
| The Assumptions |  |
|  | Link to story |
| Revenues (a) | Moderate growth driven by new drugs emerging from the pipeline, but scale will operate a growth-limiter. |
| Operating margin (b) | The company saw margins decline in 2023, but margins will improve over time to reach historical norms (10-year average) |
| Tax rate | Strong tax deferral programs will keep effective tax rates low for the near term, but increase to marginal tax rate over time. |
| Sales to Capital  (c ) | Continued large spending on R&D for next five years, before tapering down ahead of stable growth. |
| Return on capital | Strong competitive edges, primarily from patents. |
| Cost of capital (d) | Cost of capital slightly higher than median company, but decreases as company matures. |
| The Cash Flows |  |
|  | FCFF |
| 1 | 5764.813799999999 |
| 2 | 7548.146624399998 |
| 3 | 8916.632093004 |
| 4 | 10470.304958299084 |
| 5 | 12520.57294798482 |
| 6 | 14807.298005427165 |
| 7 | 15548.084499124814 |
| 8 | 16167.501740389109 |
| 9 | 16646.735607291215 |
| 10 | 16825.252879219268 |
| Terminal year | 13576.238530128652 |
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
| Value per share | 311.29 |

## Valuation as picture

| You can modify this picture and bring in relevant details to back up your cost of capital and other details that you think flesh out your company's valuation story. |
|---|
| Amgen |
| Base Year and Comparison |
|  |
| Revenue Growth |
| Revenue |
| Operating Margin |
| Operating Income |
| EBIT (1-t) |
| PV(Terminal value) |
| PV (CF over next 10 years) |
| Probability of failure = |
| Value of operating assets = |
|  - Debt |
|  - Minority interests |
|  +  Cash |
|  + Non-operating assets |
| Value of equity |
|  - Value of options |
| Value of equity in common stock |
| Number of shares |
| Estimated value /share |
|  |
| Price per share |
| % Under or Over Valued |
|  |
|  |

## Diagnostics

| Step 1: Check revenue growth rate | Your forecasts | Questions to ask |
|---|---|---|
|  | Next year | 1. If you are forecasting a revenue growth rate > industry average, is your company small? |
| Annual Revenue Growth Rate | 0.09 | 2. If your forecasted revenue growth rate is very different from your company's most recent year of growth, what is the reason? |
| Step 2: Check dollar revenues |  |  |
|  | Year 5 | 1. How big is the total market today? |
| Revenues | 43373.80928863102 | 2. How much revenues do the biggest companies in that market make today? |
|  |  | 3. How much growth is there in the total market? |
|  |  | 4. What type of market share are you forecasting for your company in year 10? |
| Step 3: Check your margins | Year 5 | 1. What are the margins of the industry that the company is in? |
| Operating Margin | 0.4 | 2. What are the unit economics of the business? (How much does it cost you to make the extra unit that you sell? |
|  |  | 3. What does the competition in this business look like? |
| Step 4: Check how much you are reinvesting |  |  |
|  | Year 5 | 1. is the growth that you are forecasting bounce-back growth or new growth? |
| Sales to Capital | 1.5 | 2. How much excess capacity do you have to service near term growth? |
|  |  | 3. Does investment efficiency in this business change as companies get bigger? |
| Reinvestment effect on cash flows |  |  |
|  |  |  |
| PV of after-tax operating income for next 10 yearas |  | 1. Is your reinvestment consitent with your revenue growth forecast? |
| Value effect of reinvestment for next 10 years |  | 2. Are you comfortable with your return on capital in year 10? |
| PV of FCFF for next ten years |  |  |
| Return on capital effects |  |  |
|  | ROC in year 10 |  |
| Return on capital | 0.23441974785522587 |  |
| Step 5: Risk Metrics |  |  |
|  | Year 1-5 | 1. How does your cost of capital compare to the industry average? |
| Cost of capital | 0.09261706048908777 | 2. What is happenign to your cost of capital over time? Why? |
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
| -4 |
| -5 |
| -6 |
| -7 |
| -8 |
| -9 |
| -10 |
| Output |
| Year |
| Current |
| -1 |
| -2 |
| -3 |
| -4 |
| -5 |
| -6 |
| -7 |
| -8 |
| -9 |
| -10 |
| Value of Research Asset = |
| Amortization of asset for current year = |
| Adjustment to Operating Income = |
| Tax Effect of R&D Expensing |
| Lookup Table for Amortizable Lives |
| Industry Name |
| Advertising |
| Aerospace/Defense |
| Air Transport |
| Aluminum |
| Apparel |
| Auto & Truck |
| Auto Parts (OEM) |
| Auto Parts (Replacement) |
| Bank |
| Bank (Canadian) |
| Bank (Foreign) |
| Bank (Midwest) |
| Beverage (Alcoholic) |
| Beverage (Soft Drink) |
| Building Materials |
| Cable TV |
| Canadian Energy |
| Cement & Aggregates |
| Chemical (Basic) |
| Chemical (Diversified) |
| Chemical (Specialty) |
| Coal/Alternate Energy |
| Computer & Peripherals |
| Computer Software & Svcs |
| Copper |
| Diversified Co. |
| Drug |
| Drugstore |
| Educational Services |
| Electric Util. (Central) |
| Electric Utility (East) |
| Electric Utility (West) |
| Electrical Equipment |
| Electronics |
| Entertainment |
| Environmental |
| Financial Services |
| Food Processing |
| Food Wholesalers |
| Foreign Electron/Entertn |
| Foreign Telecom. |
| Furn./Home Furnishings |
| Gold/Silver Mining |
| Grocery |
| Healthcare Info Systems |
| Home Appliance |
| Homebuilding |
| Hotel/Gaming |
| Household Products |
| Industrial Services |
| Insurance (Diversified) |
| Insurance (Life) |
| Insurance (Prop/Casualty) |
| Internet |
| Investment Co. (Domestic) |
| Investment Co. (Foreign) |
| Investment Co. (Income) |
| Machinery |
| Manuf. Housing/Rec Veh |
| Maritime |
| Medical Services |
| Medical Supplies |
| Metal Fabricating |
| Metals & Mining (Div.) |
| Natural Gas (Distrib.) |
| Natural Gas (Diversified) |
| Newspaper |
| Office Equip & Supplies |
| Oilfield Services/Equip. |
| Packaging & Container |
| Paper & Forest Products |
| Petroleum (Integrated) |
| Petroleum (Producing) |
| Precision Instrument |
| Publishing |
| R.E.I.T. |
| Railroad |
| Recreation |
| Restaurant |
| Retail (Special Lines) |
| Retail Building Supply |
| Retail Store |
| Securities Brokerage |
| Semiconductor |
| Semiconductor Cap Equip |
| Shoe |
| Steel (General) |
| Steel (Integrated) |
| Telecom. Equipment |
| Telecom. Services |
| Textile |
| Thrift |
| Tire & Rubber |
| Tobacco |
| Toiletries/Cosmetics |
| Trucking/Transp. Leasing |
| Utility (Foreign) |
| Water Utility |

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
| There are four ways in whch you can estimate your cost of capital. In the first, you can directly input a cost of captial. In the second, you can work through your company's cost of capital inputs in detail, entering business, geogaphical mix and debt, and I will help you estimate a cost of capital. In the third, you can look up the cost of capital for the industry or industries your firm belongs to and in the fourth, you can use a crosssectional distribution  of costs of capital for companies at the start of the year to make your estimate. |
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
| Which grouping (US, Emerging Markets, Global) |
| Which risk grouping does your company fall in? |
| Cost of capital based upon decile/group chosen |
| Region |
| Emerging |
| Europe |
| Global |
| Japan |
| US |
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

## Country equity risk premiums

_204 rows — showing first 20. Full data: [`illamgenno2024-country-equity-risk-premiums.csv`](illamgenno2024-country-equity-risk-premiums.csv)_

| Mature Market ERP + | 0.0433 | Updated March 1, 2024 |
|---|---|---|
| Changing this number will update all your country equity risk premiums. |  |  |
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.005377876270766179 |
| Albania | B1 | 0.04904110980246301 |
| Algeria | NR | 0.04904110980246301 |
| Andorra (Principality of) | Baa2 | 0.020743237044383835 |
| Angola | B3 | 0.07080870423175468 |
| Anguilla | NR | 0.1054310997313879 |
| Antigua & Barbuda | NR | 0.1054310997313879 |
| Argentina | Ca | 0.13073361124886354 |
| Armenia | Ba3 | 0.03918166997272502 |
| Aruba | Baa2 | 0.020743237044383835 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.004353518885858335 |
| Azerbaijan | Ba1 | 0.027273515373171343 |
| Bahamas | B1 | 0.04904110980246301 |
| Bahrain | B2 | 0.059924907017108855 |
| Bangladesh | B1 | 0.04904110980246301 |
| Barbados | B3 | 0.07080870423175468 |
| Belarus | C | 0.175 |

## Industry Averages(US)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 57 | 0.11568399999999998 | 0.09613021337246905 | 0.3151511149045307 | 0.20554353210253967 | 1.1806104386629273 | 1.3723256229214125 | 0.10192697865438498 | 0.5641442530150431 | 0.053524 | 0.25241808479709577 | 0.08633158509130047 | 3.283403041333076 | 2.2595129005604955 | 12.940312997421533 | 22.23859403832829 | 5.76329812534153 | 175.73470187151344 | 0.012534141364144605 | 0.01834674674697402 | -0.016886086216883787 | -0.00993406001897932 | 0.032541006196152036 | 2.828444643801165 | 2.828444643801165 | 0.10140072310597556 |
| Aerospace/Defense | 70 | 0.07588256410256408 | 0.0853938467891159 | 0.16167717664340658 | 0.15449878451886198 | 0.9308535405948443 | 1.0764050153356324 | 0.08831463070543909 | 0.36402149671230677 | 0.050855 | 0.20291777620162876 | 0.07813355986817368 | 1.9843395804666923 | 2.478314246749687 | 18.488711603269998 | 28.310279485536824 | 5.077156879683216 | 32.517250905909876 | 0.45042764203965496 | 0.028342846696895605 | 0.02282923210385782 | 0.3924774302821871 | 0.13191483651952815 | 0.5369469719720693 | 0.5369469719720693 | 0.08770115426633238 |
| Air Transport | 25 | 0.029028333333333337 | 0.06895611482307311 | 0.1092325173386668 | 0.23528767545229368 | 0.6401880468304745 | 1.2668401714816373 | 0.09707464788815531 | 0.4465099892190103 | 0.050855 | 0.6185403903760626 | 0.06062196095222791 | 1.7773199625336142 | 0.905791803102739 | 6.1674965255190735 | 13.02453750133096 | 2.2359420389310194 | 12.658954105086503 | 0.010944385248270856 | 0.11159925638117965 | 0.06720275462762036 | 1.1858967293486484 | 0.219363538879951 | 0.0786327190884794 | 0.07863271908847935 | 0.06722710910472822 |
| Apparel | 38 | 0.057186 | 0.08757781197777915 | 0.15293487788906657 | 0.321659193318978 | 0.9295756500550167 | 1.1946998769689117 | 0.09375619434056993 | 0.37035509904588476 | 0.050855 | 0.3277875013609528 | 0.07552631069684605 | 1.7730762352050577 | 1.2013803591525696 | 7.918116190218288 | 12.388401308447197 | 2.5581525508953336 | 18.68854542735665 | 0.24650261726088157 | 0.0241727298617933 | 0.005365083866607844 | -0.07285876271141715 | 0.09204171598277805 | 0.7498299827899141 | 0.7498299827899141 | 0.09604206456031172 |
| Auto & Truck | 34 | 0.2194211111111111 | 0.04819731976726051 | 0.05186632508660861 | 0.13206977576521484 | 1.3040309184380587 | 1.5223779065768546 | 0.10882938370253531 | 0.59698514250326 | 0.053524 | 0.23675434053330363 | 0.0925675842254241 | 1.048731678622114 | 2.4924481910179397 | 21.649291457975476 | 49.578165599480705 | 4.598881244319622 | 21.120152874872904 | -0.02199384121059546 | 0.06409275484587712 | 0.026576673289955756 | 0.8147103151259559 | 0.09370908108633746 | 0.35459224927693617 | 0.3545922492769362 | 0.05097954162021133 |
| Auto Parts | 39 | 0.06284695652173916 | 0.05306898539439057 | 0.10156047044070848 | 0.2795040993246159 | 1.1211038704345888 | 1.3444265903808044 | 0.100643623157517 | 0.3707196400160045 | 0.050855 | 0.2776627158727018 | 0.08328904447811177 | 2.0047909637588615 | 0.8166091584007446 | 7.05552696054855 | 14.11643631329104 | 1.9975303469056522 | 39.03342462860953 | 0.15450924675978886 | 0.03707814807523698 | 0.03169360364635347 | 0.9518332479515937 | 0.05723613672909091 | 0.4536555295436519 | 0.45365552954365196 | 0.058520548536996245 |
| Bank (Money Center) | 15 | 0.07275384615384616 | 0 | 0.00017809965864835952 | 0.15860164261163576 | 0.644005117845298 | 1.0613761697933088 | 0.08762330381049221 | 0.22510527234137442 | 0.045043 | 0.6837066086251078 | 0.05081181950491864 | 0.26645699933051714 | 5.265879881670676 | NA | NA | 1.0492601893677032 | 8.547358658097874 | NA | 0.019731137380717412 | 0.012953142452475423 | 55.728776313853096 | 0.148740347323159 | 0.2433797029883855 | 0.24337970298838552 | 0.0008120089321794556 |
| Banks (Regional) | 625 | 0.0921562422997947 | 3.6415348617892096e-08 | -0.0005337495814512601 | 0.2072412923305567 | 0.3333666067349679 | 0.4611581340936746 | 0.06001327416830903 | 0.1867735328629955 | 0.045043 | 0.5048182884466578 | 0.04677137344346035 | 0.3671924593155293 | 4.47375649038584 | NA | NA | 1.0188589222331499 | 35.96629242038575 | NA | 0.027336820130708508 | -0.10087904726752299 | NA | 0.1214259211695359 | 0.32014617865318346 | 0.3201461786531834 | -0.0017660881241903206 |
| Beverage (Alcoholic) | 19 | 0.12062222222222224 | 0.20626605729454345 | 0.16670846804136458 | 0.25595531935006144 | 0.9702633521273643 | 1.131834912668812 | 0.09086440598276535 | 0.4970414041193621 | 0.050855 | 0.19656022020066688 | 0.08050113083311888 | 0.8968231153352131 | 3.891668687686919 | 14.84352953298064 | 18.678840886226705 | 3.0993348768756093 | 35.37590107389537 | 0.17116248155736727 | 0.07663177615269445 | 0.09390305849002889 | 0.9081296859580446 | 0.0869908980857384 | 0.5463466520815233 | 0.5463466520815233 | 0.20751043151831927 |
| Beverage (Soft) | 29 | 0.2857907692307692 | 0.19303402977387185 | 0.3065163030779624 | 0.18728623048491203 | 0.7018333472111191 | 0.7641458754245853 | 0.07395071026953093 | 0.42961071148670704 | 0.050855 | 0.1461578752429545 | 0.0687168756429393 | 1.6931990505110932 | 4.164625625009446 | 18.067516918352702 | 21.46725363552388 | 7.4226028259445 | 33.67306525553318 | -0.07141616874567232 | 0.0465383125685219 | 0.02386992815326883 | 0.25676455571759477 | 0.30557353679830446 | 0.6638966866591276 | 0.6638966866591276 | 0.1939726828971502 |
| Broadcasting | 22 | 0.054847058823529415 | 0.11778498155713862 | 0.12063888924002568 | 0.2627114978288718 | 0.4997566745248037 | 1.0609243999049403 | 0.08760252239562726 | 0.38457133667076027 | 0.050855 | 0.6382079868292138 | 0.05603594331400262 | 1.1159893806472496 | 1.2533019633843616 | 7.309829643836126 | 10.673057550494407 | 0.8010135128715571 | 7.816781173533133 | 0.10922957427443249 | 0.025150013344556445 | -0.020612152442738167 | 2.1143668601085928 | -0.021565149058570276 | 0.0021958759739129407 | 0.0021958759739129086 | 0.11731512451023196 |
| Brokerage & Investment Banking | 27 | 0.12787473684210526 | 0.007705853109232633 | 0.001307446941021954 | 0.21046665127451775 | 0.550778221499521 | 1.120326193984736 | 0.09033500492329785 | 0.25213732428210645 | 0.050855 | 0.6933076588770894 | 0.054148674889421655 | 0.27949922437037333 | 5.609753546935761 | NA | NA | 1.6565413108416178 | 222.18514648652769 | NA | 0.03412584763467917 | 0.016766162791348155 | 56.43365588996486 | 0.10413110832014963 | 0.4352511082051424 | 0.43525110820514246 | 0.0057932474418426055 |
| Building Materials | 44 | 0.06407764705882352 | 0.13549668839875367 | 0.252670574449478 | 0.24749103744997217 | 1.2090471865786552 | 1.3177985305249351 | 0.09941873240414702 | 0.28715879840268466 | 0.050855 | 0.15361123144803443 | 0.09000582287201073 | 2.288218658680442 | 2.110936521592126 | 12.010468803767779 | 15.39424362371289 | 4.735200284670956 | 24.84788931563107 | 0.1835621131134187 | 0.03251273384820363 | 0.02451312577392343 | -0.00761665449252251 | 0.21354650605206582 | 0.2901940579761685 | 0.2901940579761685 | 0.13773258950466172 |
| Business & Consumer Services | 162 | 0.06692426966292138 | 0.11098788170854047 | 0.27452359974428153 | 0.24242512766060723 | 0.9296426574330118 | 1.022101721640971 | 0.08581667919548466 | 0.41290054994468384 | 0.050855 | 0.15210606535531057 | 0.07856495724643378 | 2.721892729960434 | 2.681998782938528 | 16.123377912677118 | 23.493439699858502 | 5.535512057561694 | 86.89938236196181 | 0.1348442517919118 | 0.029848449272908677 | 0.016940121240038436 | 0.2544682103316714 | 0.1399754737551486 | 0.5978300778071928 | 0.5978300778071928 | 0.11307358791595411 |
| Cable TV | 10 | 0.1623166666666667 | 0.19465081924755748 | 0.11311872163563386 | 0.2555517666975476 | 0.7356295403207628 | 1.2767983158980267 | 0.09753272253130923 | 0.3300530419558696 | 0.050855 | 0.5042600346325823 | 0.06758397653579118 | 0.7767223693225921 | 2.546585383581608 | 7.80087236104986 | 13.348955942597875 | 2.063094529414669 | 16.12065991866249 | -0.000977411923104362 | 0.14079353806475833 | 0.016512641327761278 | 0.15767366778442643 | 0.19466771140821634 | 0.21927067291667543 | 0.21927067291667546 | 0.19087795085663556 |
| Chemical (Basic) | 32 | 0.11316100000000001 | 0.07880938244885832 | 0.11808931523559212 | 0.23971308008564993 | 0.8746907847879827 | 1.096267077331708 | 0.08922828555725856 | 0.389245235426506 | 0.050855 | 0.31354657676699077 | 0.07321012044110661 | 1.6175128141587387 | 1.14999857052991 | 8.09953226998328 | 14.05606834124257 | 1.9757813391316583 | 12.407994201775024 | 0.14739172149447363 | 0.05507532358895694 | 0.030793498175279994 | 0.173667004732125 | 0.08894604157698592 | 1.3126657214952435 | 1.3126657214952435 | 0.08017253592667842 |
| Chemical (Diversified) | 4 | -0.007550000000000004 | 0.015232688891083214 | 0.015720852535763625 | 0.4429336629583849 | 0.8134608576935285 | 1.133279731139076 | 0.0909308676323975 | 0.37242278384437877 | 0.050855 | 0.4101286201966363 | 0.06928033459211429 | 1.2786447256557913 | 1.1597139266470613 | 15.396063877133198 | 73.61515917157838 | 1.9746042510627253 | 30.527729815250837 | 0.17621388838496 | 0.04511777011805717 | -0.005790335432994922 | -5.556514170837235 | -0.02360500422508987 | 0.01037037037037037 | 0.010370370370370363 | 0.014639496833568348 |
| Chemical (Specialty) | 68 | 0.07331875000000002 | 0.13090390749762712 | 0.13505275648152232 | 0.18266700211687126 | 0.9381357434291198 | 1.0873832852797658 | 0.08881963112286922 | 0.36600539277751015 | 0.050855 | 0.21148852013848732 | 0.07810173529617936 | 1.15732408251221 | 2.6791416225374163 | 12.84967814786451 | 19.995555424351952 | 2.67276074057165 | 60.901134435897625 | 0.22747765886505658 | 0.08458782491964281 | 0.09811517277754803 | 1.0348496791866486 | 0.1494327338476946 | 0.33249927210754887 | 0.3324992721075488 | 0.1304736636407548 |
| Coal & Related Energy | 18 | 0.05559999999999999 | 0.20509759118732937 | 0.29497550992564786 | 0.13126063867339174 | 1.2427250283125129 | 1.2707580825145446 | 0.09725487179566905 | 0.5569225989970031 | 0.053524 | 0.18396815851589854 | 0.08674810591202373 | 1.4739520943470472 | 1.329263856564374 | 2.752899093023886 | 4.036828154446029 | 1.7901440274639588 | 91.91242298375973 | 0.061300782894183045 | 0.09304611980325424 | 0.015940120019722653 | 0.13283664539899678 | 0.29069215958320355 | 0.15155665948302102 | 0.151556659483021 | 0.2055288408959451 |
| Computer Services | 72 | 0.10926473684210528 | 0.06978175075516928 | 0.24167411086330845 | 0.18859681218443272 | 0.8586975071173775 | 0.9973235378280684 | 0.08467688274009114 | 0.49612772702274627 | 0.050855 | 0.22566035729965525 | 0.07417563522879664 | 3.586752140343538 | 1.374220668174326 | 12.610910959671749 | 18.86294317155709 | 4.374578039057352 | 76.13219981553276 | 0.1385312172798853 | 0.012325750009423415 | 0.008234391003302918 | 0.23795588571918946 | 0.18772570752648005 | 0.5707264443402909 | 0.5707264443402909 | 0.07303438673884674 |
| Computers/Peripherals | 36 | 0.023118148148148145 | 0.21063899949335566 | 0.37798197124632166 | 0.146118607992441 | 1.1003543807483607 | 1.1329223650294353 | 0.09091442879135403 | 0.38898164531276785 | 0.050855 | 0.05741744674704877 | 0.08788432760842899 | 1.922787109314276 | 5.51173057328121 | 21.831632280697495 | 25.971419409717786 | 30.982880033408666 | 31.833390779893396 | -0.09869344487486884 | 0.0305976596426454 | 0.00900470133952177 | 0.092441186690531 | -1.234289008499134e-05 | 0.17443899392066986 | 0.17443899392066986 | 0.2148311734272625 |
| Construction Supplies | 45 | 0.05646333333333333 | 0.1516624134275202 | 0.20159249439191199 | 0.2240246415269075 | 0.9906432640326439 | 1.1279620532844743 | 0.09068625445108582 | 0.37831296869001413 | 0.050855 | 0.19808486343548007 | 0.08027788442017579 | 1.5346635011566743 | 2.1404639541029313 | 11.117699163080328 | 14.030171302852379 | 3.9177656869750295 | 33.88591584170452 | 0.19378020407952468 | 0.048387580949684664 | 0.030449081725833525 | 0.5198317789035468 | 0.27112218233648655 | 0.23711309103177794 | 0.2371130910317779 | 0.15403954967556815 |
| Diversified | 23 | 0.06940636363636364 | 0.22931748516386233 | 0.20395197737613438 | 0.17651836241260768 | 1.0923486152033832 | 1.1948544445210565 | 0.0937633044479686 | 0.5225050340018127 | 0.053524 | 0.1607420785589129 | 0.0851442652580404 | 0.9331386227471588 | 2.4285333531334716 | 8.934637168196366 | 10.510496860016763 | 1.8732585871718974 | 13.800008820068092 | 0.05002077101846478 | 0.04483024892964029 | 0.046101030377602686 | 0.25080420620828026 | 0.15867710900985088 | 0.08160540712757532 | 0.08160540712757536 | 0.23068357288812125 |
| Drugs (Biotechnology) | 572 | 0.18950851190476192 | 0.010772125793898567 | 0.015551579144381567 | 0.16414119075344816 | 1.089096469625617 | 1.1233547439492362 | 0.09047431822166487 | 0.6198094773831897 | 0.053524 | 0.14082267604024337 | 0.08338652730105696 | 0.40681193428310364 | 6.888047035213811 | 13.519816800069261 | NA | 6.135291677851848 | 30.391605386786914 | 0.09981041747914851 | 0.03823100547201804 | 0.03468871974612317 | NA | -0.11590040227481527 | 0.0008849667367975925 | 0.00088496673679761 | 0.03830299416528875 |
| Drugs (Pharmaceutical) | 245 | 0.41537666666666667 | 0.1816047184019137 | 0.1337527062215693 | 0.14924679402968208 | 0.9439976867785511 | 1.0269619624933468 | 0.08604025027469395 | 0.6530341383257241 | 0.060879 | 0.1382882750021232 | 0.08045603140384625 | 0.6429618194294369 | 5.079239809938446 | 16.617974116905632 | 27.428480363585575 | 5.1951082931130115 | 57.62587734954958 | 0.22369121415285234 | 0.05305346359441335 | 0.1297351632612678 | 0.8539263175436763 | 0.17320808107952249 | 0.6995836180254923 | 0.6995836180254923 | 0.21327300590991013 |
| Education | 31 | 0.04118187499999999 | 0.05815213773071442 | 0.05928030828162614 | 0.3215618737875887 | 1.146739430936378 | 1.2251855531141391 | 0.0951585354432504 | 0.43781301036597053 | 0.050855 | 0.16383109786985448 | 0.0858173309715238 | 1.2894168928698895 | 2.3038717172014334 | 10.79885515422891 | 31.74120806131489 | 2.71602884918073 | 34.57346986093771 | 0.09076833645533934 | 0.02924050168157691 | 0.003324528881953833 | 0.9750398020735855 | 0.016746880536467494 | 0.38078808076847676 | 0.3807880807684767 | 0.05162998984685171 |
| Electrical Equipment | 103 | 0.14907829787234042 | 0.09001062757621153 | 0.13265964322266596 | 0.21670554463683422 | 1.145843471951508 | 1.2410543592858396 | 0.09588850052714862 | 0.5442389893824032 | 0.053524 | 0.17619594793469248 | 0.08606636921867376 | 1.4659763013390332 | 2.975717978432906 | 14.654554784871266 | 28.89201617695047 | 2.9236490003601276 | 24.68870614432407 | 0.28273149237543 | 0.06163253029040514 | 0.09817923934367007 | 2.1463997544763114 | 0.23703235618633814 | 0.17177866341194353 | 0.1717786634119436 | 0.09571467640528439 |
| Electronics (Consumer & Office) | 13 | -0.06321 | -0.0007643401586021315 | 0.009542635546224023 | 0.6944234404536862 | 1.3029636093516688 | 1.29517877665579 | 0.09837822372616634 | 0.3942415498208712 | 0.050855 | 0.15486981955971799 | 0.08904933447437148 | 1.6732153737167332 | 0.8460734447976122 | 19.14394169874833 | NA | 1.9031490452094928 | 38.63288320991239 | 0.15533542696520905 | 0.015568092728386464 | -0.0022079528200980025 | NA | -0.06626800138724744 | 0 | 0 | 0.005672435482946352 |
| Electronics (General) | 129 | 0.1582396511627907 | 0.09481660558440742 | 0.15114383953059968 | 0.22613287894821063 | 0.8772051743933108 | 0.9339545990672654 | 0.08176191155709421 | 0.4294264362055603 | 0.050855 | 0.14673840734826454 | 0.07536108515272853 | 1.6768879249052682 | 2.1770119295764263 | 13.589599841576854 | 22.109356359942485 | 3.279017675641514 | 102.2602762874735 | 0.24013986599713918 | 0.04063467322550578 | 0.04116813973531535 | 0.7043164107310471 | 0.08797660106927524 | 0.2852688403156121 | 0.28526884031561206 | 0.09797018507091383 |
| Engineering/Construction | 43 | 0.08056709677419355 | 0.04476191515889162 | 0.12584190576281387 | 0.28016307022345316 | 0.8446770651898954 | 0.9606439454908486 | 0.08298962149257905 | 0.3368374054652199 | 0.050855 | 0.20763646217020956 | 0.07367746430176464 | 3.1139792067111656 | 1.1163272617563171 | 12.760394435192657 | 23.127763287334602 | 3.333138872597814 | 47.295500708894096 | 0.18924885792675486 | 0.030006983111800924 | 0.02636229257370127 | 1.2619175754407028 | 0.06411400934520678 | 0.21672148486032367 | 0.2167214848603236 | 0.0471774671389744 |
| Entertainment | 98 | 0.15469137931034482 | 0.07006793583532164 | 0.07557891173918209 | 0.19997160037162454 | 0.8657191928039559 | 0.9945594291517039 | 0.08454973374097838 | 0.6118583017241714 | 0.053524 | 0.22327359258810395 | 0.07463488276352676 | 1.105934104413193 | 3.0674272548861663 | 16.3723272692034 | 42.533399418877075 | 2.592969156186322 | 31.168325364687774 | 0.038054347095575536 | 0.043745016460205635 | -0.02257591732057464 | -0.20650613209517016 | -0.0027275543810870717 | 0.0034346522556140007 | 0.0034346522556140124 | 0.07052565436421813 |
| Environmental & Waste Services | 57 | 0.13381230769230767 | 0.13553472241576553 | 0.2994248396119106 | 0.24029481031348 | 0.7857301954805603 | 0.9069990344697701 | 0.08052195558560943 | 0.4606641855124769 | 0.050855 | 0.17996903176435833 | 0.07289474103587697 | 2.2902044972728537 | 3.3833883540504326 | 15.00034560192311 | 24.256339038064446 | 6.247640228043101 | 31.275191037772736 | 0.10180591590590521 | 0.07838174216179752 | 0.06484591372588196 | 0.7009982439901342 | 0.2101163487107984 | 0.3634221878468773 | 0.3634221878468773 | 0.13822317401919318 |
| Farming/Agriculture | 42 | 0.21383809523809522 | 0.1017867183533354 | 0.17930588293067248 | 0.20906218860773967 | 0.7692133353509856 | 0.9916245080726602 | 0.08441472737134237 | 0.5413972223878111 | 0.053524 | 0.3117833507573673 | 0.07061153986768859 | 1.8306605351728302 | 1.1055363962241 | 8.972844558455247 | 10.564710180101258 | 2.733036754860097 | 21.61187500533381 | 0.14722500458801463 | 0.033959385963758186 | 0.026989790167118995 | 0.5301203584239703 | 0.2751209698375531 | 0.17330466660689933 | 0.17330466660689936 | 0.10487455135329483 |
| Financial Svcs. (Non-bank & Insurance) | 172 | 0.20501310679611653 | 0.15180167018136817 | 0.008800023323033083 | 0.19506036249910982 | 0.3219787507277045 | 1.1435084926002885 | 0.09140139065961328 | 0.38661906483318564 | 0.050855 | 0.7797646357747897 | 0.049871016476855864 | 0.06486881783951717 | 19.18449176258731 | 62.47502878860274 | 83.07855996089174 | 3.433260809839322 | 25.58837051606901 | 13.079698706991074 | 0.025535543778949593 | 0.0283598183581379 | 0.21675896399206002 | 0.22361139419471984 | 0.278095003447611 | 0.27809500344761107 | 0.1525193861991764 |
| Food Processing | 82 | 0.07243347826086957 | 0.10787378764336854 | 0.17232732992047894 | 0.2157611897080789 | 0.49587927161435114 | 0.6057177351430681 | 0.06666301581658113 | 0.36509661152078565 | 0.050855 | 0.2520787816629353 | 0.0594732838386618 | 1.7201959394721398 | 1.8429492449644929 | 12.510605460521338 | 16.772528178110687 | 2.2978753647758015 | 31.40132716803937 | 0.06007671733337372 | 0.04125541496137907 | 0.02646915514691439 | 0.41192631497381554 | 0.10101697021572027 | 0.6870670237911619 | 0.6870670237911619 | 0.10922833001114575 |
| Food Wholesalers | 14 | 0.18654000000000004 | 0.022317777961135557 | 0.14961754390226162 | 0.2440190000210877 | 0.735070446558385 | 0.9657109707728366 | 0.08322270465555048 | 0.2730341205580487 | 0.050855 | 0.3086032140951128 | 0.06931042285276451 | 8.019146001382584 | 0.4004885022763874 | 11.256367425384894 | 18.0515417386402 | 4.102757035965513 | 26.10422435346539 | 0.05775676283002207 | 0.009305647965928221 | 0.008990082879669114 | 0.47194525861898456 | 0.21114375328629606 | 0.3816139050363045 | 0.38161390503630455 | 0.022183644509181345 |
| Furn/Home Furnishings | 31 | 0.031330476190476186 | 0.05863342094918943 | 0.1031461588962982 | 0.3449147774663963 | 0.8611874852176121 | 1.1071062452097284 | 0.0897268872796475 | 0.46652480430214993 | 0.050855 | 0.3222606162357703 | 0.07310286802099338 | 1.960874135947077 | 1.0479459257763848 | 9.365153315056007 | 16.699225224322326 | 2.2525462393242712 | 19.58001711865685 | 0.13973769506770378 | 0.03244916758319206 | 0.07215518793071732 | 0.9731455119346809 | -0.06526279080199633 | 0.008561710778602603 | 0.008561710778602571 | 0.06111385929719684 |
| Green & Renewable Energy | 17 | 0.03735 | 0.23439691972396948 | 0.041502730750869 | 0.07057255807755519 | 0.5560860191551688 | 1.1067077196296322 | 0.08970855510296308 | 0.5733620520250774 | 0.053524 | 0.5857606197878946 | 0.060675004825720386 | 0.19933188854202233 | 7.471964571566294 | 12.631994561427968 | 33.57877466889787 | 0.8544222894141614 | 39.87241810854294 | -0.2798162545898892 | 0.4431677167628508 | 0.20460875674779533 | 1.159019820796266 | 0.10675101428653834 | 0.2559530242443892 | 0.25595302424438926 | 0.21775570853782217 |
| Healthcare Products | 230 | 0.1794840000000001 | 0.13294967540797936 | 0.13081181602888342 | 0.2058016276197557 | 1.0054180718910262 | 1.062079895442844 | 0.08765567519037082 | 0.5220553450431473 | 0.053524 | 0.11239729750559911 | 0.08231537890171181 | 0.9916960692418304 | 5.16106566472784 | 21.511372797591477 | 36.992220884124826 | 4.629146961325782 | 61.89156213874568 | 0.25574201971953897 | 0.049018238448480196 | 0.020771729298397056 | 0.49512455251752285 | 0.08305797928561881 | 0.4176547855320923 | 0.41765478553209223 | 0.13835739605834813 |
| Healthcare Support Services | 119 | 0.12421877192982453 | 0.039183419890367124 | 0.45741028306204884 | 0.22529394737980976 | 0.9403062489496928 | 1.0326229061406076 | 0.08630065368246795 | 0.495257334489641 | 0.050855 | 0.2117523051840508 | 0.07610278893641609 | 12.880997802478152 | 0.6094709713815003 | 11.29245433490106 | 15.455594645482641 | 3.337712803480082 | 80.16828730486425 | -0.06525413741565193 | 0.007054822379833121 | 0.019151402871181444 | 0.6275372045055494 | 0.15620310034184115 | 0.2962592112192362 | 0.29625921121923615 | 0.03863510174300033 |
| Heathcare Information and Technology | 128 | 0.1966670689655173 | 0.14008066391084326 | 0.14281217248637942 | 0.11691985958691149 | 1.1875339477983193 | 1.2747542568245518 | 0.09743869581392939 | 0.5415316524692178 | 0.053524 | 0.13845034763183783 | 0.08950608681068283 | 1.0414718449585996 | 5.28889573407126 | 21.43557654642684 | 36.52953122117682 | 4.088727827705521 | 44.43644387862758 | 0.22945875273735597 | 0.045108188895623375 | 0.026677271844225636 | 0.31339455513224623 | 0.0517765805634577 | 0.19727330771004128 | 0.19727330771004126 | 0.14149228552648924 |
| Homebuilding | 32 | 0.11040782608695648 | 0.16243511385197026 | 0.20906182388989658 | 0.23441748751073238 | 1.3535915929813263 | 1.3695349346617718 | 0.1017986069944415 | 0.3231388378117894 | 0.050855 | 0.14104057563334713 | 0.09282033672064799 | 1.5490492448976174 | 1.322751156524132 | 7.792651325795131 | 8.106886452741305 | 2.0034988997912557 | 10.663226208304753 | 0.5851080967899663 | 0.005136223478795905 | 0.003627956840827162 | -0.04996220070411062 | 0.2288315257494398 | 0.06433100516498451 | 0.06433100516498447 | 0.16303748138534604 |
| Hospitals/Healthcare Facilities | 32 | 0.18106894736842105 | 0.11569354150132667 | 0.20156640226109454 | 0.2029553064378943 | 0.5599961069519285 | 0.879576324903561 | 0.0792605109455638 | 0.46328064944317854 | 0.050855 | 0.44365037194401546 | 0.06101793553300139 | 1.8739472690562888 | 1.5597693131250068 | 8.752615756037349 | 13.412731417361721 | 5.116820380350496 | 22.866077429053238 | 0.11173413334158254 | 0.06248242818478106 | 0.022041129079390705 | 0.3491979818825059 | 0.6196567951123925 | 0.12781126030710444 | 0.12781126030710444 | 0.11548052103864387 |
| Hotel/Gaming | 68 | 0.10244649999999998 | 0.17139569325713905 | 0.09988621756233888 | 0.1926500388336529 | 1.048189773353677 | 1.3434280675321946 | 0.10059769110648095 | 0.4079972106407317 | 0.050855 | 0.32736720549245807 | 0.080151500516448 | 0.8068226577495352 | 4.225278800410454 | 14.975440441167427 | 30.72977186409063 | 11.056315096413167 | 32.22143792065357 | 0.02991513267185368 | 0.0671217870013804 | 0.011171667233667715 | 0.2181007264159746 | 0.3586909891606898 | 0.08431271586945352 | 0.08431271586945355 | 0.13535100750457585 |
| Household Products | 93 | 0.022456341463414627 | 0.1685988615827197 | 0.3117119490495866 | 0.22132011627855985 | 0.772920133759626 | 0.8434441780824564 | 0.077598432191793 | 0.5111810512741538 | 0.053524 | 0.1420395966697854 | 0.07227827771017822 | 1.9939780230234398 | 3.4146535727357166 | 15.95498916736902 | 20.01362143547223 | 7.327476195584277 | 34.469619164706735 | 0.07496444937618411 | 0.036174629752540516 | 0.009442860706523613 | -0.0009751404704261414 | 0.26982900687477657 | 1.2222919620788795 | 1.2222919620788795 | 0.1702679338230282 |
| Information Services | 18 | 0.04717 | 0.11632760029506121 | 0.22740740434639165 | 0.25775980471928395 | 0.7723824914378383 | 0.9307433698849299 | 0.08161419501470678 | 0.3382873796265951 | 0.050855 | 0.26289829475513876 | 0.07018523190235645 | 2.1851130805639345 | 2.332933091341277 | 12.153718575448424 | 19.061250080564882 | 4.057632214426638 | 24.757228147387533 | 0.15732336315134232 | 0.019033801691390826 | -0.03625119576829269 | -0.2631403524056768 | 0.08428916780703317 | 0.6070397140714504 | 0.6070397140714504 | 0.1233982054939375 |
| Insurance (General) | 21 | 0.07763727272727272 | 0.15227330392370475 | 0.15653546538570912 | 0.20671990280364713 | 0.8946178159376359 | 1.0331486323510635 | 0.08632483708814892 | 0.40381703602170393 | 0.050855 | 0.20592429100406523 | 0.07640266607898921 | 1.187979918303592 | 2.6563933238175803 | 11.47931425966219 | 17.340883842855348 | 2.855054505130747 | 92.17728773965159 | -9.32562533189817e-05 | 0.00927886987041088 | -0.02599849839227991 | 0.3789687523388437 | 0.13524697097521135 | 0.32753059692538994 | 0.3275305969253899 | 0.1526705842911407 |
| Insurance (Life) | 23 | -0.0006250000000000012 | 0.0006561673843832166 | 0.0010816809572142688 | 0.1773493298381602 | 0.5398311188838629 | 0.7657608653274894 | 0.07402499980506452 | 0.30849684925039994 | 0.050855 | 0.47983380623416055 | 0.0568067635541461 | 0.9369712840702341 | 1.5653336469693586 | 17.24492070332478 | NA | 1.6173451473258358 | 176.3786320021675 | 0.286158812471161 | 0.001812242761727661 | -0.025614435950617652 | NA | 0.013240127450855269 | 3.812072472103254 | 3.812072472103254 | 0.0012852923105425914 |
| Insurance (Prop/Cas.) | 50 | 0.061676590909090896 | 0.0741210434078295 | 0.11118635097908262 | 0.18944213157737264 | 0.6752076172747652 | 0.7387577603373708 | 0.07278285697551906 | 0.2740417784199851 | 0.050855 | 0.1623541698682306 | 0.06715864763210716 | 1.6945936593477595 | 1.3577625752259637 | 11.773604889791214 | 15.658885816047809 | 2.2989008715036703 | 20.722521356503638 | -0.40937489754024503 | 0.007798282092746183 | -0.0013016926116446899 | 0.2866229380931067 | 0.10356883343367865 | 0.3513343235075974 | 0.3513343235075974 | 0.07491728052428294 |
| Investments & Asset Management | 334 | 0.04603686274509802 | 0.1499916403489553 | 0.061639717527291187 | 0.18978292304498715 | 0.39129392968006665 | 0.45700546948270204 | 0.059822251596204294 | 0.15150889761067693 | 0.045043 | 0.28742573556682555 | 0.05233768498325397 | 0.47398717524974837 | 5.415454683531844 | 34.84525131380541 | 34.89604066216606 | 2.0039088032674184 | 69.37883307856436 | NA | 0.029725746882996038 | 0.0613614718892364 | 0.5466968323096587 | 0.13783634813168708 | 0.4210565068467859 | 0.42105650684678597 | 0.14670723243602463 |
| Machinery | 103 | 0.04712599999999998 | 0.147792130725919 | 0.24909385325604075 | 0.21716795174857764 | 0.9376095544061418 | 1.0260564286029479 | 0.08599859571573559 | 0.3344421407862324 | 0.050855 | 0.14430985657050793 | 0.07909230901965258 | 1.8716132403381998 | 3.0699195050801884 | 15.461408447841649 | 20.31238382156512 | 4.343824750041772 | 26.951754964203868 | 0.25173396431408457 | 0.024425884717957834 | 0.06427958072207628 | 0.6676806488145169 | 0.19022656097823037 | 0.3626998107382271 | 0.3626998107382271 | 0.150614656789397 |
| Metals & Mining | 68 | -0.013133333333333325 | 0.19621084093017843 | 0.2402669710602103 | 0.352864128291061 | 0.9121243548326187 | 0.962478409539915 | 0.08307400683883609 | 0.605593652790272 | 0.053524 | 0.1365935261422664 | 0.07720990923388173 | 1.2535014116480827 | 2.937914549631262 | 10.355846578641355 | 14.873774197012049 | 3.222491992809813 | 33.132597557421676 | 0.1532155838029568 | 0.13030144622632117 | 0.05911404921719728 | 0.631496293074419 | 0.12165895420384185 | 0.9547059514867223 | 0.9547059514867223 | 0.19557867619586258 |
| Office Equipment & Services | 17 | 0.15850384615384616 | 0.07292311757505164 | 0.12926389341779917 | 0.443225574589701 | 0.8764328079953049 | 1.1394185236914496 | 0.09121325208980668 | 0.3028006279393898 | 0.050855 | 0.34456840647253745 | 0.07292631690141482 | 2.070408564827314 | 1.1711022809028628 | 9.34264860122093 | 15.610563143808655 | 2.5364199127790323 | 249.1565502380709 | 0.09126079195854167 | 0.022936760875543978 | 0.01983353016355783 | 0.1658016014045215 | 0.026638000470444 | 2.251690805097501 | 2.251690805097501 | 0.07526993149408069 |
| Oil/Gas (Integrated) | 4 | 0.0176 | 0.155957937510296 | 0.17039770081786265 | 0.2951241851606302 | 0.6440450138393521 | 0.6706515844468459 | 0.0696499728845549 | 0.26444809223182186 | 0.050855 | 0.11113222576377609 | 0.06614833837942029 | 1.3700896826288935 | 1.3474820849008362 | 6.238126514870909 | 8.538840720552136 | 1.816944677335053 | 8.018212897016301 | 0.03369649525012355 | 0.07386778595354455 | -0.0002148426775026158 | -0.01671215236463339 | 0.19851813516763073 | 0.37142296537371583 | 0.3714229653737158 | 0.15779316761156298 |
| Oil/Gas (Production and Exploration) | 166 | 0.2328005882352942 | 0.37265839691067637 | 0.28405709355869363 | 0.20342463510697406 | 0.8214204967594376 | 0.9298987386959587 | 0.0815753419800141 | 0.46310335310672146 | 0.050855 | 0.18884246603997282 | 0.07337314094030123 | 0.7985632978346455 | 2.650004308645573 | 4.668377817514971 | 6.982567340901188 | 1.9431230096211636 | 16.325943214834 | 0.009995128861736279 | 0.30047596852821296 | 0.16046402665504775 | 0.5039504893607293 | 0.31094799857184063 | 0.3127231610769736 | 0.3127231610769736 | 0.37686234244190675 |
| Oil/Gas Distribution | 24 | 0.2745153333333334 | 0.37953024273539593 | 0.20602082553480802 | 0.18244447623517368 | 0.529121571269841 | 0.790752151008787 | 0.07517459894640421 | 0.3254754733249822 | 0.050855 | 0.4125209705549901 | 0.05989756589613192 | 0.5941367718527 | 3.5771916018946355 | 7.311766844085146 | 9.292319764938465 | 2.316973847830998 | 18.41284012023769 | 0.025338522415672818 | 0.1653134380456791 | 0.13121071073961837 | 0.4028456796383902 | 0.42406084058617804 | 0.39844096378722926 | 0.39844096378722926 | 0.38210569457340066 |
| Oilfield Svcs/Equip. | 100 | 0.07737212121212124 | 0.0872091490275141 | 0.2802140695692729 | 0.2183798745548326 | 0.8529017381494012 | 0.9795500315745983 | 0.08385930145243152 | 0.43728736432048126 | 0.050855 | 0.2432269507930905 | 0.07273943920145498 | 3.553462668606814 | 0.6282383014519446 | 5.424130388035158 | 7.0794352962597635 | 1.9840962070304522 | 70.29822817770717 | 0.06341844706124501 | 0.023634819010543238 | 0.005762949509121732 | 0.15485672710250106 | 0.296469137164352 | 0.1880872531115289 | 0.18808725311152896 | 0.08846245675775162 |
| Packaging & Container | 22 | 0.03418388888888888 | 0.0975946017284918 | 0.14213647578465585 | 0.2399155168186175 | 0.8068658605326057 | 1.1327220379604754 | 0.09090521374618188 | 0.2624270896574677 | 0.050855 | 0.37988410428510205 | 0.07086102263993198 | 1.7390682733466043 | 1.3995514423034054 | 8.631115428237793 | 14.02966201208884 | 2.574898261389149 | 19.636247288161293 | 0.11122681556948795 | 0.061265537922326724 | 0.04828525693355974 | 0.6796320359442392 | 0.08543065693073756 | 0.7022179042517068 | 0.7022179042517068 | 0.09980257971460628 |
| Paper/Forest Products | 7 | 0.038425 | 0.099619899214932 | 0.18901373691463047 | 0.30911701363962674 | 1.5902925666995296 | 1.9382231536190784 | 0.12795826506647762 | 0.43036486711913036 | 0.050855 | 0.27203680189153673 | 0.10352473153234908 | 2.1382237014668712 | 1.039978868393705 | 7.063368657012814 | 10.309929699692999 | 2.420835985244048 | 19.990268135629133 | 0.12896672468828177 | 0.07590810594104122 | 0.050747159393665635 | 0.9970294005799266 | 0.1516544447144206 | 0.27578599007170435 | 0.27578599007170435 | 0.10140987860769964 |
| Power | 50 | 0.05327999999999999 | 0.16292988851641926 | 0.05783880879545163 | 0.16140322753814085 | 0.3885061927976376 | 0.6506274182981785 | 0.0687288612417162 | 0.20394370124554315 | 0.045043 | 0.48166097793207796 | 0.05189644229561903 | 0.4114319764618295 | 3.7153854274683433 | 11.691846058595218 | 22.33991040176153 | 1.7113225687107074 | 23.19158205893271 | 0.08255159354511177 | 0.33954089511344704 | 0.22702951827873996 | 1.7342755771524554 | 0.08603363410590081 | 0.7667440694022755 | 0.7667440694022755 | 0.16287010099737925 |
| Precious Metals | 61 | 0.116358 | 0.09481534785916063 | 0.04692969329686256 | 0.22878493646304626 | 0.8300839147546547 | 0.8689509398150602 | 0.07877174323149277 | 0.6360947392798966 | 0.053524 | 0.13198988940179562 | 0.07367313968463768 | 0.5050530432733019 | 3.955802095084481 | 13.009572620028603 | 40.05647773739665 | 2.0363465513114485 | 34.232639448888236 | 0.09832505200986535 | 0.254079702395255 | 0.09540597574989443 | 1.462623173547346 | -0.023341970007055318 | 0.008835121692908373 | 0.008835121692908343 | 0.0948174324372014 |
| Publishing & Newspapers | 21 | 0.014301538461538454 | 0.07799268875649687 | 0.13864542842203184 | 0.30084662624835684 | 0.8229834620810547 | 0.9611136476182338 | 0.08301122779043876 | 0.3820331725274816 | 0.050855 | 0.24514393589381342 | 0.07201162483142262 | 2.002343030060959 | 1.441750885458818 | 10.524430352410006 | 18.911615383953578 | 2.054348258457602 | 29.2414035210639 | 0.10133375540284054 | 0.03594412667278533 | -0.012909705831287229 | -0.13309544549517302 | 0.03396787791067467 | 0.8715513267926518 | 0.8715513267926518 | 0.07683361395321084 |
| R.E.I.T. | 193 | 0.08359719512195124 | 0.243406841238619 | 0.02981217511772447 | 0.03212842930885189 | 0.6600635421243216 | 1.0315825268097811 | 0.08625279623324994 | 0.23718238142541787 | 0.045043 | 0.4414651235052642 | 0.06308888005999957 | 0.13967726747915735 | 11.49492573699334 | 21.02190927560778 | 47.68030534436101 | 2.0128630891188832 | 117.17420797066069 | 1.3368628412334298 | 0.02965427926540301 | -0.1511950776822921 | -0.6651383148057987 | 0.04572271115802798 | 2.152187853630432 | 2.152187853630432 | 0.2176858060671846 |
| Real Estate (Development) | 17 | 0.5556166666666666 | 0.1260895802230371 | 0.029287042485061747 | 0.24259357814440308 | 0.4314363177605709 | 0.6685940614079962 | 0.06955532682476782 | 0.3424003701471713 | 0.050855 | 0.484795077605791 | 0.054325937012590225 | 0.26632691318970303 | 4.382629372614688 | 17.93205737756681 | 36.271131152719285 | 1.3514347597641898 | 8.022117698323951 | 0.04078481886311249 | 0.02541914029412253 | -0.05928807510108271 | -0.9727120811775142 | -0.08538037893418758 | 0 | 0 | 0.11158676233778687 |
| Real Estate (General/Diversified) | 11 | 0.09080400000000001 | 0.16131826431281968 | 0.05312220372276945 | 0.17400095021907827 | 0.5125267518181463 | 0.5635722376636395 | 0.06472432293252742 | 0.35907096541478567 | 0.050855 | 0.24171470192446345 | 0.05829880338240528 | 0.37242041233481304 | 4.778840644215548 | 18.009159397595386 | 28.438668024742345 | 1.2470691827068427 | 33.2262308257929 | 2.012999505032173 | 0.02840372875763075 | -0.051359511631743945 | -0.5941237825780336 | 0.09109205615781056 | 0.2492318197336975 | 0.24923181973369757 | 0.1643542931994576 |
| Real Estate (Operations & Services) | 60 | 0.054392666666666666 | -0.0028357035717595817 | 0.0006711915964746503 | 0.18035278243626368 | 0.8828463853207577 | 1.0801188936162607 | 0.088485469106348 | 0.4419222889349552 | 0.050855 | 0.3082714813242523 | 0.07296578210632138 | 1.44524314073108 | 1.5074220348746605 | 14.981930532197556 | NA | 2.8721502379113324 | 104.23604792269977 | 0.09693828006851661 | 0.013030956034781528 | -0.01166064844331973 | NA | -0.08269945359431624 | 0.007618846133805902 | 0.007618846133805923 | 0.00048652777182227547 |
| Recreation | 55 | 0.10951862068965518 | 0.09659043658909008 | 0.09536754171130633 | 0.2790897385078625 | 0.8488780060557483 | 1.17128693009822 | 0.09267919878451812 | 0.4429522114939097 | 0.050855 | 0.3693821811903066 | 0.07253385230484759 | 1.28318501683349 | 1.8421118883204324 | 9.98738944984403 | 21.71796210872423 | 3.4596231451635577 | 27.700115574206265 | 0.18037794033907653 | 0.07111560994338362 | 0.032100923079553575 | 0.5615834278229958 | 0.025626629604530146 | 1.9958513365724233 | 1.9958513365724233 | 0.0810090946051851 |
| Reinsurance | 1 | 0.0695 | 0.0965567194116336 | 0.30116910073399067 | 0.2295302013422819 | 0.6098509183978317 | 0.6551440260520247 | 0.06893662519839314 | 0.17094029032718663 | 0.045043 | 0.2984245857127374 | 0.05844569534382253 | 4.048441545907466 | 0.6896317635240171 | 7.283030827731133 | 7.142501442962344 | 1.3077640132466577 | 9.344609991235759 | 0.17093826610207266 | 0.0014486293737463784 | 0.04326387341207934 | 0.7560799531674074 | 0.3123460169723515 | 0.18930762489044697 | 0.18930762489044695 | 0.09655325505093537 |
| Restaurant/Dining | 64 | 0.06796 | 0.1580022591623619 | 0.19557552942837814 | 0.19967846424718289 | 1.0243276951296387 | 1.194577320424228 | 0.09375055673951449 | 0.35372310643077254 | 0.050855 | 0.20462608516509845 | 0.08237144200266251 | 1.6196890156518917 | 4.194361595858457 | 16.598910443571427 | 29.333020694460565 | NA | 94.18909813240215 | 0.00860428879008023 | 0.057944026102845256 | 0.03572268537099506 | 0.3451108324184372 | NA | 0.5307559895574028 | 0.5307559895574028 | 0.13614064338279905 |
| Retail (Automotive) | 30 | 0.17498636363636366 | 0.06175620642981021 | 0.13195481158300898 | 0.23751485780163534 | 1.0587643053346871 | 1.4944959500823904 | 0.10754681370378996 | 0.46787574959813977 | 0.050855 | 0.3651324749998421 | 0.08220458844986592 | 2.669833787404534 | 1.049476016950808 | 11.625721407059311 | 17.424466432833757 | 6.9701147308624885 | 17.88872792375451 | 0.09983369799408429 | 0.019066371040589995 | 0.021762603098834987 | 0.7134611678555867 | 0.4732854552615435 | 0.05794159749803761 | 0.05794159749803762 | 0.057130049786012285 |
| Retail (Building Supply) | 16 | 0.08905384615384616 | 0.12513815577176424 | 0.39426101011063314 | 0.24040748843756385 | 1.704153179546406 | 1.9381785697071496 | 0.12795621420652886 | 0.4521058266464563 | 0.050855 | 0.16613035370375878 | 0.11303522243500778 | 3.641816586745592 | 2.169932476442798 | 13.331901910729169 | 17.19076108032302 | NA | 27.87080707923468 | 0.08469682764457319 | 0.024278467792407967 | 0.008484963589781638 | 0.023337337560001278 | NA | 0.46644741818218693 | 0.46644741818218693 | 0.1238432505090802 |
| Retail (Distributors) | 62 | 0.05805459459459458 | 0.11953213688630857 | 0.186085879254954 | 0.23449866940082945 | 0.9093255538405173 | 1.106042693037566 | 0.08967796387972804 | 0.37735750438183585 | 0.050855 | 0.24408909195893314 | 0.07709841418627789 | 1.8156573835628624 | 1.813078112372955 | 11.632873296385332 | 13.822749735595126 | 4.030387228576006 | 28.908314358128138 | 0.17415504658831088 | 0.0625565357934217 | 0.0921510641035311 | 1.0375036244575058 | 0.2545162298582571 | 0.2522053106672775 | 0.25220531066727747 | 0.121685531334811 |
| Retail (General) | 26 | 0.18063052631578944 | 0.044133968058007046 | 0.0989299380525086 | 0.21721237165566823 | 1.171062908717729 | 1.2466770513434235 | 0.09614714436179748 | 0.38283198873816127 | 0.050855 | 0.1183525185747442 | 0.0892820006718982 | 2.411559428998697 | 1.5688483400026725 | 16.63129575259254 | 38.46582980994355 | 7.24228550393011 | 29.84401634296881 | 0.007687613623918548 | 0.05200966480677357 | 0.022820227937652104 | 0.794478336472149 | 0.1955014547502191 | 0.21744723060022958 | 0.21744723060022952 | 0.04696703491105394 |
| Retail (Grocery and Food) | 14 | 0.0659125 | 0.024225596853965255 | 0.10989245466725754 | 0.22911929074099627 | 0.364761149065977 | 0.4936080595618046 | 0.06150597073984301 | 0.25647926947712857 | 0.050855 | 0.35831710070912415 | 0.05313399174546412 | 4.75644637935626 | 0.4125213111332912 | 6.379804822101389 | 19.804920951092498 | 2.903171334143174 | 16.757683247241964 | -0.00243238992810026 | 0.026633515324994268 | 0.01326060238245387 | 1.1428223096616057 | 0.14777603490447422 | 0.3692401555065788 | 0.36924015550657874 | 0.026473632076435664 |
| Retail (REITs) | 28 | 0.04110185185185184 | 0.36745097043843167 | 0.04458562834006221 | 0.04201930358888443 | 0.7866747019034875 | 1.120867766031394 | 0.09035991723744412 | 0.20718002005434216 | 0.045043 | 0.37042376508860575 | 0.06940220471941981 | 0.13065981426778428 | 12.151988991799444 | 17.431873861346652 | 34.711010000762485 | 1.9356719923817578 | 74.0905042250849 | -0.09870898691980977 | 0.05167863850956901 | -0.2652596155473204 | -0.8180364327949872 | 0.06523063162826355 | 1.5557235045106812 | 1.5557235045106812 | 0.3500970998582947 |
| Retail (Special Lines) | 105 | 0.12071967741935487 | 0.04617263081820448 | 0.13499345989584943 | 0.24714983147031147 | 0.9730692183120843 | 1.1814057462278666 | 0.09314466432648186 | 0.4400785368755131 | 0.050855 | 0.2655200484001674 | 0.07854015509233994 | 3.1090000638677036 | 0.983570844924985 | 9.341548558904895 | 20.317569846397642 | 4.778606562878069 | 48.78837652846057 | 0.050599261894710514 | 0.02588926922351027 | 0.026622349307585433 | 0.5523015624992001 | 0.09643878418310899 | 0.8704265485497078 | 0.8704265485497078 | 0.0479816113263796 |
| Rubber& Tires | 3 | 0.0902 | 0.018445123448906007 | 0.03124092719979871 | #DIV/0! | 0.26316933125019143 | 0.674519769567508 | 0.06982790940010537 | 0.4077252655256018 | 0.050855 | 0.7017405533587942 | 0.04759209549858379 | 1.4484047693844369 | 0.6282869174808124 | 7.94758657142281 | 29.777572649378406 | 0.78946449471402 | #DIV/0! | 0.10694212196535768 | 0.05418679936728137 | 0.00706289851939911 | -0.3200268060602408 | -0.0999805523142746 | #DIV/0! | #DIV/0! | 0.021569196581060632 |
| Semiconductor | 63 | 0.06441162790697674 | 0.19711975635060902 | 0.11368358391768708 | 0.0930926705083394 | 1.460244593924559 | 1.4952411850835359 | 0.10758109451384265 | 0.4147143445700453 | 0.050855 | 0.05700810294721246 | 0.10362246070915908 | 0.5807292092301813 | 10.596722932093094 | 31.594447138361602 | 53.315004182229046 | 7.38179145503603 | 82.75051639049542 | 0.22403022878237655 | 0.1700086447636025 | 0.06898697577847278 | 0.498632244773038 | 0.12611876313091647 | 0.48873979408723345 | 0.48873979408723345 | 0.2053985135441381 |
| Semiconductor Equip | 30 | 0.09925749999999998 | 0.2418675138617241 | 0.25683632466511935 | 0.12268560712932465 | 1.5077650793777069 | 1.5279822074255314 | 0.10908718154157444 | 0.3704014298865129 | 0.050855 | 0.0721657639254397 | 0.10396731419447477 | 1.1649954029158387 | 5.244258173215728 | 18.178195157648474 | 21.529732735448246 | 8.100975890903412 | 163.51842013025154 | 0.34562808268522127 | 0.050796555474868554 | 0.026035463292282256 | 0.13881169088914808 | 0.3289066823779071 | 0.20089988720666727 | 0.2008998872066673 | 0.2500123642381983 |
| Shipbuilding & Marine | 8 | -0.006803333333333335 | 0.10650740465993001 | 0.09235139499766344 | 0.18850960892353175 | 0.686594972052408 | 0.8108361418109077 | 0.07609846252330175 | 0.4507472470693009 | 0.050855 | 0.22942151889413903 | 0.06739026117321822 | 0.8293396370887708 | 1.7047396816839095 | 8.384720595362964 | 14.228088437354392 | 1.3642629613319885 | 24.757087703228514 | 0.11299865486721869 | 0.10241614888029281 | 0.0402991976086052 | 0.5027071202632976 | 0.07817317702121597 | 0.29337528524998274 | 0.2933752852499827 | 0.11940027650657051 |
| Shoe | 13 | 0.11491250000000001 | 0.12199139215361694 | 0.24043080830071734 | 0.1746054567339842 | 1.2730955389810585 | 1.2915789442240697 | 0.09821263143430721 | 0.3627990889011926 | 0.050855 | 0.08011440800391599 | 0.09340004827272026 | 2.2253944893651223 | 2.886304484269497 | 18.953733947779405 | 23.682872304836216 | 8.710769065002456 | 19.768872194714948 | 0.19614445731942837 | 0.008576270485019038 | -0.005201249793080597 | -0.20182594713277416 | 0.29903214866474775 | 0.3226131069739849 | 0.3226131069739848 | 0.12180719617705567 |
| Software (Entertainment) | 84 | 0.17412533333333333 | 0.2680484859792075 | 0.19944873406255512 | 0.16568125122952723 | 1.1136804709373258 | 1.1083305740238332 | 0.08978320640509632 | 0.5278932207822914 | 0.053524 | 0.030561494934367585 | 0.08826612748850601 | 0.7438484984853133 | 6.025017719108312 | 17.157815859353224 | 22.22174441209462 | 6.243054731624327 | 30.818070198150206 | 0.04776324767882057 | 0.12672459193901217 | 0.08703914407040002 | 0.4679443076693403 | 0.2325593855621183 | 0.0025063968697220758 | 0.002506396869722094 | 0.2816776939314963 |
| Software (Internet) | 35 | 0.22244545454545456 | -0.03359481657046853 | -0.004810953262445776 | 0.17878408264897386 | 1.5117563379021286 | 1.6160843271745926 | 0.11313987905003126 | 0.65221602599035 | 0.060879 | 0.10698653549795539 | 0.10592036033474572 | 0.6361233556563813 | 8.382873685172553 | 19.329878727497675 | NA | 9.00211413022916 | 35.177442964143594 | 0.09669575439393442 | 0.05577807792135737 | 0.028310083379424048 | NA | -0.1454065112919735 | 0 | 0 | -0.008317507436808912 |
| Software (System & Application) | 351 | 0.15903337837837828 | 0.25298655593299035 | 0.23224389866710615 | 0.1785326176172911 | 1.2724589938133573 | 1.2939647291542515 | 0.09832237754109557 | 0.5208648982480728 | 0.053524 | 0.05841338019643433 | 0.09492392344119566 | 0.920355645703261 | 10.72155166283089 | 28.433138742544646 | 39.48199090418876 | 11.028707841031288 | 88.72457294882238 | 0.112044526586602 | 0.0867464101497983 | 0.059162106791780016 | 0.3638023142592327 | 0.24441835382299518 | 0.27220590606666156 | 0.2722059060666615 | 0.2629596189730837 |
| Steel | 29 | 0.0787332 | 0.12104448776971048 | 0.2218083633357043 | 0.19962963225553462 | 1.0774711199709137 | 1.126371725263511 | 0.0906130993621215 | 0.3810220503199221 | 0.050855 | 0.1679434941873973 | 0.08180079363377206 | 2.1668462373578015 | 0.9413469942673617 | 5.931545531851561 | 7.726201556222234 | 1.7639737558457758 | 14.541699757518971 | 0.19023869959969508 | 0.06201549106073591 | 0.042105106814159125 | 0.1569878341429413 | 0.22194709191501236 | 0.12471207785733139 | 0.1247120778573314 | 0.12145781664117886 |
| Telecom (Wireless) | 13 | 0.09297714285714287 | 0.16792801039724245 | 0.06548378425028921 | 0.2465243485527615 | 0.7473117190554889 | 1.087361359035153 | 0.08881862251561704 | 0.6030586941268392 | 0.053524 | 0.3908431811819875 | 0.0697940873655997 | 0.4844121348561745 | 3.514710160984272 | 9.00951389360519 | 23.51266092863578 | 2.532248003346641 | 67.85383293004256 | 0.0626805786291462 | 0.15310947618240378 | -0.0029960671300220164 | 0.5510450483030811 | 0.09739597751390545 | 0.1104528008925427 | 0.11045280089254272 | 0.1494776231119549 |
| Telecom. Equipment | 66 | 0.09616448979591839 | 0.19578373512751376 | 0.2818216189274289 | 0.1690647820001858 | 1.045647985265377 | 1.0805072059156025 | 0.08850333147211771 | 0.4662214509006452 | 0.050855 | 0.10245104955940504 | 0.08334368336730298 | 1.4464269754607526 | 3.606781499774281 | 13.979069158223247 | 17.645248189217565 | 5.1449679404665405 | 70.49127690111283 | 0.23092380701323104 | 0.027789568604778662 | 0.03979962341125538 | 0.36669384113949066 | 0.2455054145923156 | 0.46084832909856577 | 0.46084832909856577 | 0.2071352516666671 |
| Telecom. Services | 42 | 0.1316995652173913 | 0.2086157899836036 | 0.11796482606061286 | 0.21774220884735582 | 0.4141115560097563 | 0.7845047112872219 | 0.07488721671921221 | 0.5041671435022144 | 0.053524 | 0.555383790159887 | 0.05559084195155961 | 0.6020033791062319 | 2.3574881101650598 | 6.178012041794295 | 11.212869716340027 | 1.2986532244972615 | 77.10240124570124 | -0.03223536165247942 | 0.16715169820304818 | 0.024292121675182632 | 0.2012230524472249 | -0.0034470942023052953 | 0.0016337690728598522 | 0.0016337690728598364 | 0.20983808679246463 |
| Tobacco | 16 | 0.34968888888888894 | 0.4081835064651061 | 0.8036055993679144 | 0.21139682210925856 | 0.9870802250148996 | 1.2232908278447494 | 0.09507137808085847 | 0.4800026780389306 | 0.050855 | 0.25873063108247973 | 0.08034181011489157 | 2.1763696274457 | 4.79530494511946 | 10.84266449583115 | 11.674129778938338 | NA | 17.746085416091766 | 0.15300181101471985 | 0.027084958732519204 | 0.33428394436606595 | 1.17639869037906 | NA | 0.8798405961040541 | 0.8798405961040541 | 0.4100225199058006 |
| Transportation | 36 | 0.15364933333333336 | 0.0795021944889079 | 0.15477553498576985 | 0.21188841521511076 | 1.046594408036378 | 1.2585314504520015 | 0.09669244672079208 | 0.5311913745643302 | 0.053524 | 0.25139522991909635 | 0.08247618556062086 | 2.0684414873920227 | 1.6787844253487405 | 12.006297422349427 | 20.8867003352248 | 5.382579370274886 | 23.427810144534483 | 0.06448826405478997 | 0.08703076355477433 | 0.05614884013663418 | 0.9343605303661486 | 0.2826737687263194 | 0.4050546148197834 | 0.40505461481978333 | 0.07999971892269056 |
| Transportation (Railroads) | 4 | 0.0249 | 0.35113467269131693 | 0.142619533616312 | 0.22982533024478807 | 0.8559978059315445 | 1.0172723923008653 | 0.0855945300458398 | 0.2227735820416239 | 0.045043 | 0.21142467310039645 | 0.07464013567456193 | 0.49324628388749064 | 6.629559697290431 | 14.3196804838998 | 18.966125677741278 | 6.911381082942223 | 22.28825335650561 | 0.022557471822586217 | 0.1570320179340837 | 0.05598864744528668 | 0.22178443078565843 | 0.3167794507858253 | 0.4351952815226011 | 0.4351952815226011 | 0.34954738832459115 |
| Trucking | 22 | 0.06190722222222224 | 0.08493405229389801 | 0.12748742307030905 | 0.2556493406176706 | 1.029154942745124 | 1.1484074577647394 | 0.09162674305717802 | 0.28328548955431604 | 0.050855 | 0.16632304812803944 | 0.08273087282127708 | 1.8424099749470806 | 1.8055802361025481 | 10.57224029827716 | 20.589002549993637 | 3.5846942504030093 | 36.07946277619434 | 0.06748020749652663 | 0.14934250443095923 | 0.09098037027775313 | 1.217807517047936 | 0.12974692001389668 | 0.1736271884654995 | 0.17362718846549952 | 0.0869108373084328 |
| Utility (General) | 14 | 0.043405 | 0.2180508078273298 | 0.06473139954433985 | 0.1601620397950673 | 0.3567951929109757 | 0.5804323081687388 | 0.06549988617576198 | 0.1492727509573606 | 0.045043 | 0.4589770332002346 | 0.050942219623686315 | 0.3479906108434517 | 4.128817283340104 | 11.69639755876778 | 19.078266611364857 | 1.6473566371259394 | 17.483750732416834 | 0.13370151554071408 | 0.38606604885824003 | 0.25906870978152774 | 1.5052569708950143 | 0.11153676746474966 | 0.5888282183165542 | 0.5888282183165542 | 0.21642128320038204 |
| Utility (Water) | 13 | 0.1084909090909091 | 0.3079161579620825 | 0.06798956612265145 | 0.1491899144854105 | 0.5223114719862922 | 0.7139634340794939 | 0.07164231796765672 | 0.28198719816416 | 0.050855 | 0.33727313092901634 | 0.06034330788473936 | 0.24924739614341856 | 7.895573764246353 | 16.861059231983642 | 25.637409477526273 | 2.3031518241417506 | 34.88450544421217 | 0.11350573999309437 | 0.5390843091810553 | 0.4017509969105366 | 1.4950509635847589 | 0.15979158800682636 | 0.6058549621884045 | 0.3924497264677397 | 0.30680997617385836 |
| Grand Total | 6481 | 0.1203779994242945 | 0.1145256755435513 | 0.08406230914414912 | 0.1923185498660195 | 0.7903856717545845 | 1.000223134856211 | 0.08481026420338571 | 0.42031449597641213 | 0.050855 | 0.31703408820818413 | 0.07001459583784053 | 0.7869856634612866 | 3.2302321427131906 | 16.807342298997796 | 26.13928689562484 | 3.77976528797633 | 52.28373716861881 | -0.2621844466207268 | 0.05800732530173432 | 0.03343579357417402 | 0.468845142326734 | 0.15979158800682636 | 0.3924497264677397 | 0.3924497264677397 | 0.11629806601986115 |
| Total Market (without financials) | 5214 | 0.12709816521785855 | 0.12032430790128817 | 0.1466884216172786 | 0.1940658510661986 | 0.972267805446803 | 1.0975226422471853 | 0.08928604154337053 | 0.4700345950094993 | 0.050855 | 0.18433859162959904 | 0.07985808270107618 | 1.2846280224071296 | 2.7276225992096554 | 14.145902302173438 | 22.061341722186697 | 4.473299274966686 | 52.86583637680429 | 0.08673678051027232 | 0.062462255788532275 | 0.03707475113184182 | 0.44373494936660024 | 0.16592552471920183 | 0.4126837264965974 | 0.41268372649659746 | 0.12230591201543203 |

## Industry Average Beta (Global)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 391 | 0.060678733031674176 | 0.07893289015217175 | 0.2231841538480623 | 0.2467186246978417 | 1.230922708614235 | 1.3525261181448878 | 0.12549692417308733 | 0.38891117906224903 | 0.064355 | 0.23971065900192132 | 0.10693454331762167 | 3.226927815858111 | 1.5597581830598455 | 11.941457605101096 | 18.4681983544186 | 2.5969840766685475 | 53.67686365127595 | -0.025138144517558057 | 0.017243189100700853 | 0.0017319182249018413 | 0.2511407802749644 | 0.0753565496905051 | 0.7601358005112615 | 0.7601358005112615 | 0.08065983706407705 |
| Aerospace/Defense | 289 | 0.0930956804733728 | 0.07992361762235553 | 0.13938187028979593 | 0.1617728803446455 | 0.9033832599921977 | 0.9843030741457368 | 0.10189382705274173 | 0.3510101886001401 | 0.064355 | 0.17197348630021475 | 0.09263589013327363 | 1.8322619807727754 | 2.2616278665454344 | 17.9076320802759 | 27.40985380310172 | 4.467578985815014 | 77.14560185913516 | 0.3880533361795135 | 0.03540472169202087 | 0.021536227284770452 | 0.40167246380722416 | 0.1414338304779268 | 0.4495815637111211 | 0.4495815637111211 | 0.08359700918676129 |
| Air Transport | 155 | 0.024834959999999982 | 0.07283278618645271 | 0.07609043946784132 | 0.18079322862025005 | 0.8104034085122015 | 1.2872127648104188 | 0.12131033822434785 | 0.30061794269989933 | 0.064355 | 0.5098168184151186 | 0.08396624392546047 | 1.1974037614368915 | 1.416060675493406 | 8.42106553377959 | 18.08875694052878 | 2.4000358145682927 | 96.63158394397243 | -0.02852314543830259 | 0.09872859043606706 | 0.03460650247583549 | 0.3036030119027154 | 0.19646294458461788 | 0.2520957459568711 | 0.2520957459568711 | 0.07233687669860593 |
| Apparel | 1152 | 0.029902592592592637 | 0.14639551002807655 | 0.2131479985821288 | 0.2530654600393106 | 0.7794657334292336 | 0.8327732999954237 | 0.09218076852970666 | 0.3272366860839866 | 0.064355 | 0.14561415127969835 | 0.0857562059892889 | 1.6689116104178512 | 2.4393038474523547 | 13.192840233095483 | 16.125324871999982 | 3.6292338849372476 | 42.48821546891322 | 0.2242806816328672 | 0.05163412076682679 | 0.03426756271231745 | 0.5214723064236175 | 0.17062717492423174 | 0.42378359803405474 | 0.42378359803405474 | 0.14804138042034035 |
| Auto & Truck | 165 | 0.08132156862745096 | 0.07559460879664003 | 0.08616757062954447 | 0.218811345565262 | 1.1030216126379664 | 1.3606863499868866 | 0.12601999503415945 | 0.364637234321081 | 0.064355 | 0.3560974076196418 | 0.09825875471904111 | 1.2339366809197059 | 1.2010454020784693 | 9.842284210252915 | 15.278938923875353 | 1.6673634307963552 | 42.26406405869235 | 0.02127909970655693 | 0.06066018448661873 | 0.034611750465439184 | 0.7038213344566223 | 0.1450297214555686 | 0.2655201118429188 | 0.2655201118429188 | 0.07738371255941774 |
| Auto Parts | 761 | 0.06871993174061446 | 0.0501128648978648 | 0.06951342691934614 | 0.2407743035732297 | 1.2090551528976192 | 1.3055576462563971 | 0.12248624512503506 | 0.30389336137361084 | 0.064355 | 0.23444226966537232 | 0.10503766091012318 | 1.7302940449169677 | 0.826554824388617 | 8.553999746202306 | 15.807321844185415 | 1.4984185462279607 | 130.48897980538896 | 0.11764661032295141 | 0.053688520658493784 | 0.03847388809441341 | 1.161358931096735 | 0.07578820040942477 | 0.4165823913292757 | 0.41658239132927566 | 0.048274277955413544 |
| Bank (Money Center) | 607 | 0.12026280219780221 | 0.0028364375669561663 | 0.00038710600933369535 | 0.18590464159135886 | 0.42062215883943516 | 0.8766122259384862 | 0.09499084368265698 | 0.2128077921549118 | 0.058543 | 0.7442254790211423 | 0.05683371028896152 | 0.1591156761958457 | 6.769919336252972 | 189.89899252176042 | NA | 0.8423495689751942 | 14.729077831666997 | NA | 0.033254363502624444 | 0.050798671170112115 | 19.575019416478437 | 0.1265430638481194 | 0.3069542161513744 | 0.3069542161513744 | 0.0031046482550396875 |
| Banks (Regional) | 881 | 0.08400441828254843 | -0.00010767472807027957 | -0.0001474165996108738 | 0.19178309540764643 | 0.28391223862464154 | 0.5230836051597125 | 0.07232965909073757 | 0.18295557375623153 | 0.058543 | 0.7175653123942995 | 0.05180029726907669 | 0.17196644382490733 | 5.837120237502678 | NA | NA | 0.7449859762005425 | 28.980754193617027 | NA | 0.02958498139413369 | -0.04266256265612315 | NA | 0.09826683499231499 | 0.29089509088479176 | 0.2908950908847918 | -0.0010386505223670638 |
| Beverage (Alcoholic) | 220 | 0.08247847457627114 | 0.21689011757613919 | 0.16067497723977517 | 0.2194506824475854 | 0.6865821100681192 | 0.7455633619248502 | 0.08659061149938291 | 0.2748939825628717 | 0.064355 | 0.15736771820899165 | 0.08052718649999141 | 0.8820905961381764 | 3.645519486097814 | 13.890019429473544 | 16.682460386274567 | 3.1761893485945167 | 49.8061446842652 | 0.10799586197824754 | 0.05108051295184851 | 0.029178936196543638 | 0.39674912424489117 | 0.16528003825197396 | 0.4461456976706301 | 0.44614569767063017 | 0.2173706332558427 |
| Beverage (Soft) | 100 | 0.13106444444444448 | 0.16712851609847534 | 0.2608297340208955 | 0.20408115504017893 | 0.6563336098512859 | 0.7071161596851042 | 0.08412614583581518 | 0.3223807318866916 | 0.064355 | 0.14148944903633834 | 0.07902321116032845 | 1.7627547191775153 | 3.5378584257458034 | 17.269454444972254 | 21.06683164363447 | 6.221247733454318 | 34.11006197729769 | -0.046222997524781595 | 0.046679170313504 | 0.02269315879940046 | 0.28353809683457815 | 0.25763420811932436 | 0.631087930406666 | 0.631087930406666 | 0.16780765336144984 |
| Broadcasting | 130 | 0.04030675925925924 | 0.09912960810652863 | 0.08815285332158262 | 0.25292769638038864 | 0.6637382391378946 | 0.9819685709875663 | 0.101744185400303 | 0.31539632930060435 | 0.064355 | 0.46662626831965837 | 0.07669388081982717 | 1.048262275637724 | 1.1859945658791722 | 7.870578150057497 | 11.666819517509959 | 0.7470920120100536 | 45.3362314766247 | 0.12358975266083903 | 0.03768812298249833 | -0.0027459630890185483 | 1.5367973063044447 | -0.0035567526500278465 | 0.004708516540728868 | 0.004708516540728902 | 0.09876314296512266 |
| Brokerage & Investment Banking | 590 | 0.10416122249388747 | 0.011775589724179561 | 0.0018058244106970507 | 0.1895973460883673 | 0.39976610514833727 | 0.9286781655866341 | 0.09832827041410325 | 0.3195173390050282 | 0.064355 | 0.7123160909430237 | 0.06252159620151493 | 0.18374812093580103 | 6.822798379397698 | 189.17464263492164 | NA | 1.2584232975164993 | 115.17713682796493 | NA | 0.03214726780705562 | 0.017840380622725385 | 8.460207121086022 | 0.07664517748653683 | 0.5963023526064825 | 0.5963023526064825 | 0.01134704485330971 |
| Building Materials | 457 | 0.06034177966101692 | 0.10639298425330167 | 0.1673029038037701 | 0.2283837221122689 | 0.9404913910737808 | 1.0314797894224854 | 0.10491785450198132 | 0.2800130376053482 | 0.064355 | 0.17800859680469794 | 0.09479672349945735 | 1.843429570155149 | 1.7142682425921862 | 11.505961873812181 | 15.690307278203443 | 2.8207400308199984 | 28.790076883849167 | 0.1748929917996949 | 0.04351105995778941 | 0.051551982456434185 | 0.6799932681628228 | 0.1338814752703728 | 0.38887233845093194 | 0.38887233845093194 | 0.10786546811677492 |
| Business & Consumer Services | 980 | 0.0747518865030675 | 0.09154535040510714 | 0.21051840184826337 | 0.2471200523511016 | 0.9640724752866636 | 1.0420886881980238 | 0.10559788491349333 | 0.3330640976941999 | 0.064355 | 0.16018506974822777 | 0.09638122510357179 | 2.715334288051403 | 2.0557335896830167 | 15.444300197282384 | 21.523989925145592 | 4.425380484914039 | 215.34905421682564 | 0.10538724930811741 | 0.027100047299620268 | 0.014473205088458603 | 0.3041621919138275 | 0.13588911707732615 | 0.5437955896475363 | 0.5437955896475363 | 0.09307970415006403 |
| Cable TV | 48 | 0.041942682926829275 | 0.18608743617896145 | 0.12004314941711697 | 0.2500354333947001 | 0.6075774591759452 | 1.021143501777062 | 0.10425529846390968 | 0.3091067406758942 | 0.064355 | 0.49229680226199307 | 0.07659068730916456 | 0.7593723043146429 | 2.5412604191516603 | 7.875476369514113 | 13.842133335680826 | 1.867922154373058 | 34.87596597057485 | 0.007530629820232445 | 0.14155246221551376 | 0.014127987573296625 | 0.1802528247348732 | 0.1588258209350195 | 0.2472674887044122 | 0.24726748870441217 | 0.18267772317044453 |
| Chemical (Basic) | 888 | 0.08587208708708725 | 0.04654223591776663 | 0.04639005089702379 | 0.1989867937354632 | 0.9019272865434659 | 1.0727320656318426 | 0.10756212540700112 | 0.2887733872844873 | 0.064355 | 0.30060028166786384 | 0.08967586413830847 | 1.142331199467976 | 1.3267680881060941 | 12.70958051084601 | 26.90677406929441 | 1.4647625666630506 | 113.95451115517623 | 0.13109121704272 | 0.09340874194022346 | 0.06648192201506159 | 1.945903280402447 | 0.038401073053239365 | 1.4179036744594131 | 1.4179036744594131 | 0.04704576874190067 |
| Chemical (Diversified) | 64 | 0.08104345454545456 | 0.0662386012353452 | 0.054454418663555146 | 0.22367776062870598 | 0.8463670076042942 | 1.0926752561445323 | 0.10884048391886453 | 0.2236285736387566 | 0.058543 | 0.3577601691273466 | 0.08554293723860608 | 1.0817263319048778 | 1.0157982256985354 | 7.980261546645114 | 14.423533988163413 | 1.1205497743065969 | 82.9914539334953 | 0.1932783817991698 | 0.0725779211832236 | 0.02999193005123553 | 0.4901686958441055 | 0.029144222762520315 | 1.7073693515687172 | 1.7073693515687172 | 0.06528829722994219 |
| Chemical (Specialty) | 949 | 0.09484867187499998 | 0.11947289608979784 | 0.12380681994346789 | 0.2088836095470917 | 0.9409530206448732 | 1.0268135146120057 | 0.10461874628662957 | 0.3121796391835974 | 0.064355 | 0.17874753360855905 | 0.09450906601062783 | 1.2093762157449228 | 2.2521789021943563 | 12.46623304629337 | 18.488180723537518 | 2.4503177323688616 | 46.3496903380483 | 0.18241924623939812 | 0.08833111633006872 | 0.06737714083011986 | 0.7886187208447886 | 0.12070412277404138 | 0.517197624307738 | 0.517197624307738 | 0.11942987979894938 |
| Coal & Related Energy | 215 | 0.14781403669724769 | 0.24031355444243957 | 0.322209335583537 | 0.22559346242492312 | 1.0773641639143707 | 1.0062570197628316 | 0.10330107496679751 | 0.5042147298228631 | 0.067024 | 0.16520601635212573 | 0.0945042590589013 | 1.4921479319729078 | 1.3071148054536077 | 4.071193117211346 | 5.173591267456976 | 1.5046538096423798 | 25.295557069036455 | -0.030186938808872184 | 0.0904879921874929 | 0.05122327606808048 | 0.24945089536313977 | 0.2136253482938942 | 0.7643344174950243 | 0.7643344174950243 | 0.24079230474275254 |
| Computer Services | 1164 | 0.10303601552393266 | 0.07557906617878252 | 0.21094949668920462 | 0.23628691375717017 | 1.0014532086275136 | 1.041484274226574 | 0.10555914197792339 | 0.3289536292318077 | 0.064355 | 0.12391040167313519 | 0.0984344391074444 | 3.2861205177683654 | 1.5245898873969417 | 14.677564171647024 | 19.463101367592564 | 3.998187265866603 | 64.47124345561163 | 0.15358638268892338 | 0.015317632718716554 | 0.011342015868972452 | 0.27663520093905836 | 0.16017730806734784 | 0.5307109222033554 | 0.5307109222033554 | 0.07681953889911759 |
| Computers/Peripherals | 338 | 0.005776498054474725 | 0.11390914392035238 | 0.1574768445956785 | 0.15096534785349103 | 1.2534021480264688 | 1.2665979213694365 | 0.11998892675978089 | 0.32935741174104016 | 0.064355 | 0.07029824234814774 | 0.11493247170822773 | 1.6364958004251184 | 3.0481583211129673 | 18.661505715430856 | 26.442662992327314 | 6.798948105569134 | 54.682422056511946 | 0.020955925405337854 | 0.0568499320658307 | 0.034593624971602135 | 0.38943365679267344 | 0.28447577234191745 | 0.24867757226688195 | 0.24867757226688192 | 0.11013239847595385 |
| Construction Supplies | 793 | 0.0957569154228855 | 0.08854238001268122 | 0.09335125538795638 | 0.2261320771632339 | 0.8765233217556566 | 1.0171432230729893 | 0.10399888059897862 | 0.2848026297975704 | 0.064355 | 0.28272755951113976 | 0.08818350618189803 | 1.2315279663731877 | 1.356071618713427 | 9.961896552312256 | 14.794651131796325 | 1.6048717436646578 | 70.31254894973388 | 0.16378923364761214 | 0.052092175075610876 | 0.02785872969085414 | 0.7756509803954151 | 0.1014701174588533 | 0.401042876869769 | 0.401042876869769 | 0.08957676764777435 |
| Diversified | 326 | 0.08091493975903613 | 0.15638955743055627 | 0.11943531860178906 | 0.17383650907577258 | 0.7447055221431189 | 0.9535674979014122 | 0.09992367661548052 | 0.2713903517710711 | 0.064355 | 0.3400614823470112 | 0.08228694464495964 | 0.8544472236675219 | 1.8308485319739551 | 8.931834240315368 | 11.141035054865844 | 1.2240143580285003 | 18.17107919610741 | -0.09452790124570301 | 0.048969042848116186 | 0.03612372317675373 | 0.3708958339722381 | 0.13097599742002441 | 0.20065345310626245 | 0.20065345310626248 | 0.1623363593703387 |
| Drugs (Biotechnology) | 1259 | 0.20205506249999997 | -0.004349654165448963 | 0.0069302625462042446 | 0.16290318362799433 | 1.1499580759492718 | 1.173586127245847 | 0.1140268707564588 | 0.5327835684030323 | 0.067024 | 0.12539388617853772 | 0.10600500409450417 | 0.4224018531621072 | 6.9645349708093045 | 15.315541154043325 | NA | 5.1098850921129335 | 127.83565374797985 | 0.17156984512745305 | 0.05670880114214907 | 0.09623601001085444 | NA | -0.08826768540176394 | 0.004660050948575847 | 0.0046600509485758 | 0.01629347728461259 |
| Drugs (Pharmaceutical) | 1299 | 0.1801146291560104 | 0.18171077589188153 | 0.12868088125172028 | 0.16609341613188638 | 0.885775137044685 | 0.9463176964388144 | 0.099458964341728 | 0.41512557065255234 | 0.064355 | 0.13356717205915378 | 0.09259379196792614 | 0.7133575578287207 | 4.050186295727115 | 14.60113338333945 | 21.710340042553312 | 3.880532878413638 | 41.50646703224001 | 0.15494978149385633 | 0.050126176906218664 | 0.05709230352486827 | 0.4421980861514401 | 0.13204955368081206 | 0.6354262724578472 | 0.6354262724578472 | 0.19790654724473067 |
| Education | 260 | 0.1049271523178808 | 0.11068501831140407 | 0.09268476409209102 | 0.20115514479499427 | 0.760048193847253 | 0.831043895169313 | 0.09206991368035297 | 0.3452563908096796 | 0.064355 | 0.2238175015251615 | 0.08221979503677382 | 0.9700013526960014 | 2.2863341200289162 | 10.92084133436804 | 18.170084325962243 | 1.945981275121727 | 125.4237648269257 | 0.0347618405437226 | 0.057202129044108055 | 0.030121776656189952 | 0.5759498657784389 | 0.051181871388765295 | 0.5770804164162722 | 0.5770804164162722 | 0.1089354913518312 |
| Electrical Equipment | 1072 | 0.10648472622478389 | 0.07125667037299772 | 0.10900312865728104 | 0.1877640569768875 | 1.1038380140290207 | 1.1304437779998266 | 0.11126144616978889 | 0.3511338511809446 | 0.064355 | 0.14982261726599763 | 0.10179248713393688 | 1.665499126878828 | 1.937473915590827 | 15.546386961505645 | 24.88578876473839 | 2.8201040669778954 | 97.34873031868189 | 0.21724570207617197 | 0.06886198879542421 | 0.060263839932513816 | 1.622376012024411 | 0.10855337528235157 | 0.3938315660428019 | 0.3938315660428019 | 0.07392852706932732 |
| Electronics (Consumer & Office) | 127 | 0.030448865979381453 | 0.04675350733593803 | 0.062281608986361356 | 0.14511188845949377 | 1.1252477543580413 | 1.2272209019035967 | 0.11746485981202055 | 0.33860993934953365 | 0.064355 | 0.23240429857556588 | 0.10133494502462219 | 1.4795010697699906 | 0.9372307095413658 | 11.435556560776208 | 19.485953759181257 | 1.7221991828297822 | 40.79347758155906 | 0.06626061355356098 | 0.04199658621982048 | 0.026957624809844094 | 0.8712160994984531 | 0.07310350523512302 | 0.322409892738655 | 0.32240989273865495 | 0.047475838673722494 |
| Electronics (General) | 1486 | 0.0583861029411765 | 0.052816362664381264 | 0.06442013008104085 | 0.18363373037764957 | 1.2783308812571208 | 1.2819639249630843 | 0.12097388759013371 | 0.3253309852456644 | 0.064355 | 0.1570780939611311 | 0.10952076242670084 | 1.3596420054060334 | 1.5902472235868699 | 14.162266281966438 | 28.293547866055906 | 2.2713680154060296 | 102.0009865712753 | 0.18920480550752594 | 0.06311217680124008 | 0.03571937444832814 | 0.9658046997915959 | 0.06682404237790968 | 0.6191160197223171 | 0.6191160197223171 | 0.05340382332713351 |
| Engineering/Construction | 1283 | 0.05414898190045237 | 0.0473263475570705 | 0.07890348694080135 | 0.22601656498353057 | 0.7058505143148914 | 0.9684592416234427 | 0.10087823738806267 | 0.3057573435641939 | 0.064355 | 0.4834532657436405 | 0.07534323983630636 | 1.957133670142594 | 0.6319690641888086 | 9.128583061880741 | 12.771361202731047 | 1.0286615211721977 | 39.88158117438705 | 0.15166813159500808 | 0.03210791493621454 | 0.023003554359122564 | 1.2629972936342393 | 0.09111818582020693 | 0.663128434383875 | 0.663128434383875 | 0.04786317293842815 |
| Entertainment | 741 | 0.09607665178571427 | 0.07301455929955164 | 0.07471394705446398 | 0.22104866126785255 | 1.032645697681921 | 1.108071766625171 | 0.10982740024067346 | 0.41350767359783575 | 0.064355 | 0.18212968708614155 | 0.09857778015143688 | 1.09039647289904 | 2.9125408254770817 | 15.77637640940653 | 36.435754194976965 | 2.478243757744576 | 156.16716168811138 | 0.03998354131040744 | 0.0371914707513846 | -0.025549451493464218 | -0.3412171459861466 | 0.02266695055525666 | 0.8923656321785683 | 0.8923656321785683 | 0.07479552339549585 |
| Environmental & Waste Services | 383 | 0.08214126829268294 | 0.1059427762504348 | 0.10776035869992424 | 0.22828572809639683 | 0.8279088564359454 | 1.0018793316240373 | 0.1030204651571008 | 0.3388816224065516 | 0.064355 | 0.2593042957980481 | 0.0887690618643545 | 1.159020805834006 | 2.7759010980617136 | 14.044705041117068 | 24.861013118730188 | 3.0192593691541787 | 39.26285294619102 | 0.14714493884822613 | 0.0864903499458508 | 0.07450731664583757 | 1.3468736213993477 | 0.08068341683507488 | 0.6316740322827555 | 0.6316740322827555 | 0.10712905533260315 |
| Farming/Agriculture | 430 | 0.11069166112956813 | 0.08155918853538352 | 0.10564638698267616 | 0.21465598191652302 | 0.5739833900965212 | 0.7739207856809721 | 0.08840832236215032 | 0.3405479235070628 | 0.064355 | 0.36687002403495417 | 0.0736058475645657 | 1.4546832049254665 | 1.083445156327121 | 9.748963134960206 | 12.674165730446662 | 1.8261410113292809 | 26.811988355670827 | 0.1620209245358258 | 0.04191540951324291 | 0.027119979747894672 | 0.5982715203228036 | 0.14471013504560334 | 0.330233740156234 | 0.3302337401562341 | 0.08378458499710377 |
| Financial Svcs. (Non-bank & Insurance) | 1113 | 0.13966122830440608 | 0.12396400036662453 | 0.008761897143301427 | 0.1737059815532707 | 0.2776667061543162 | 0.9263947961157201 | 0.09818190643101765 | 0.3520861107982175 | 0.064355 | 0.7752631577651665 | 0.059324482410728234 | 0.08176786069558538 | 15.087157197700607 | 51.97883927062566 | 71.07619607266898 | 2.2543147403608255 | 50.717970657858544 | NA | 0.03870786958759963 | -0.08005263917150024 | -0.7739543954061371 | 0.18599670816271613 | 0.2395510614420021 | 0.2395510614420021 | 0.12518863431233251 |
| Food Processing | 1395 | 0.09150664953751296 | 0.07601821923013945 | 0.11622768831214836 | 0.23203358657357873 | 0.6039413354218605 | 0.7051051868903214 | 0.08399724247966961 | 0.286288168212873 | 0.064355 | 0.24367084990706836 | 0.07524046057397898 | 1.8018530156761792 | 1.4097637305734059 | 12.638629712056016 | 18.182590730645643 | 2.3207121070069805 | 49.424628991224 | 0.10209470422865594 | 0.044032327026134896 | 0.022819064923232654 | 0.59209442076174 | 0.10404779362976543 | 0.6364338642154035 | 0.6364338642154035 | 0.07643217976016078 |
| Food Wholesalers | 173 | 0.07762073770491804 | 0.0247050127681529 | 0.10682869077036927 | 0.24528806061661854 | 0.49621392699558364 | 0.669184281117407 | 0.0816947124196258 | 0.3082233050608905 | 0.064355 | 0.3657986184010768 | 0.06939129594697532 | 5.266001173030653 | 0.37040946105270617 | 9.705473761566207 | 14.908328811292225 | 2.1484244627673386 | 49.788416639124684 | 0.058735090381477895 | 0.014196921545210834 | 0.009039573725576098 | 0.48474528312897786 | 0.08914166793720849 | 0.5694556518243253 | 0.5694556518243253 | 0.024650661855536982 |
| Furn/Home Furnishings | 383 | 0.051528208955223906 | 0.07236821058761174 | 0.13128509792883244 | 0.18188020982467473 | 0.9343214300886445 | 0.9490949854867619 | 0.09963698856970143 | 0.29724029020693765 | 0.064355 | 0.21842611560401573 | 0.08837129588766914 | 2.088919277463388 | 1.0263903171402884 | 9.742334396995355 | 13.621346679027324 | 2.0500313773089878 | 37.844392452209235 | 0.0491114224711247 | 0.03588446704427892 | 0.03095329705244206 | 0.5344106441284637 | 0.11207479182881593 | 0.7004804195891057 | 0.7004804195891057 | 0.07332634459333483 |
| Green & Renewable Energy | 253 | 0.13562630434782605 | 0.2923549836232071 | 0.07173408690830194 | 0.15996917387477594 | 0.6090620482792936 | 0.865385048247372 | 0.09427118159265654 | 0.3337365434374277 | 0.064355 | 0.39204417303862843 | 0.07615448022189596 | 0.2748775497385651 | 7.400667405873423 | 13.94521369318382 | 22.78669236974085 | 2.0118013936278083 | 49.91219743572899 | 0.09720434876570103 | 0.4155888393759565 | 0.366754884688644 | 1.5213911510431768 | 0.10750114708648674 | 0.6638681430225125 | 0.6638681430225125 | 0.2914634184100197 |
| Healthcare Products | 849 | 0.15227076604554854 | 0.12429654755321932 | 0.11043987670936666 | 0.20586319075844875 | 1.0434097110903426 | 1.0980822833163133 | 0.10918707436057569 | 0.42342967151692185 | 0.064355 | 0.11702454945172519 | 0.10203374276993574 | 0.934438224672006 | 4.412915204529998 | 20.066047522071443 | 33.885138474146686 | 3.577065328687604 | 94.72577507667808 | 0.2568771678494069 | 0.05425840003523742 | 0.03468357524389041 | 0.6732921834615992 | 0.07578216042011074 | 0.5070323335024587 | 0.5070323335024587 | 0.12860324255827582 |
| Healthcare Support Services | 463 | 0.1262148689138577 | 0.03949890391586041 | 0.28931239582267737 | 0.23065813714388514 | 0.8212109879282184 | 0.9102046390281967 | 0.09714411736170742 | 0.3780579367531488 | 0.064355 | 0.2300114299920197 | 0.08585428156103399 | 8.658982223369822 | 0.6084030855050848 | 11.05672759844143 | 15.221991037238858 | 2.6222805850361985 | 57.50089542846316 | -0.02729586537091901 | 0.008735011215680625 | 0.016595145817757888 | 0.5745139054109445 | 0.12150320012763628 | 0.3688222893654052 | 0.3688222893654052 | 0.03906588789448509 |
| Heathcare Information and Technology | 443 | 0.16608049792531115 | 0.1360342036177964 | 0.12755597641996133 | 0.1406302678057966 | 1.17067702552802 | 1.2336178357798575 | 0.11787490327348887 | 0.4493294014324383 | 0.064355 | 0.12088709657117488 | 0.10943522027790771 | 0.9806808854111762 | 5.245477310988296 | 21.657557844698776 | 36.68273692947799 | 3.937298830626732 | 128.07264346669305 | 0.23898000848150244 | 0.07151953974823033 | 0.06135000646949924 | 0.7159047776805149 | 0.06025565979669429 | 0.24427342031412552 | 0.24427342031412547 | 0.13842721531237037 |
| Homebuilding | 173 | 0.0783418881118881 | 0.13284171703093914 | 0.14415922427185887 | 0.24284596243598933 | 1.0113882281398225 | 1.09470744903033 | 0.10897074748284415 | 0.2896512515831867 | 0.064355 | 0.23108292327990762 | 0.09489538645538215 | 1.3895015946994185 | 1.1836835844750713 | 8.02944931196801 | 9.165171354093467 | 1.5788152644485347 | 20.55071204788833 | 0.6093441380975978 | 0.006943514595374568 | 0.005146380776774236 | 0.2028709193735042 | 0.166100037997485 | 0.18138712820097372 | 0.1813871282009737 | 0.12789569443934784 |
| Hospitals/Healthcare Facilities | 232 | 0.11022302631578944 | 0.10856496717371635 | 0.123234764374531 | 0.20089465914726268 | 0.5802219144187124 | 0.7649492144306516 | 0.08783324464500478 | 0.2952943117870857 | 0.064355 | 0.3220849172106314 | 0.07502298357098423 | 1.3816578903093093 | 2.3100825241398093 | 12.437422816930154 | 20.5766743043298 | 4.077228390304158 | 41.97948073189126 | 0.06963885853470497 | 0.07173862767890807 | 0.024492221939418652 | 0.4077498161537452 | 0.1194972327229353 | 0.45894118236119014 | 0.4589411823611902 | 0.10768274675714398 |
| Hotel/Gaming | 650 | 0.03479338114754097 | 0.1401879193441881 | 0.08265390639495226 | 0.20563328333825087 | 0.7853696261046105 | 0.9791274828677105 | 0.10156207165182024 | 0.33832876960999625 | 0.064355 | 0.31642144634643116 | 0.08463296811355503 | 0.7580094309218132 | 3.563706751527192 | 15.089381235478525 | 28.37207756106548 | 3.9615827071660843 | 60.185329176533294 | -0.01978075305102923 | 0.06305597202590978 | 0.008460904068733094 | 0.1601647809552411 | 0.10909196658632195 | 0.27136929836694895 | 0.2713692983669489 | 0.12340733671522258 |
| Household Products | 549 | 0.060971030640668535 | 0.1497559861434353 | 0.20302883575078812 | 0.2301047953820261 | 0.8467284006789493 | 0.8982548951677175 | 0.0963781387802507 | 0.35414092089807037 | 0.064355 | 0.12115016737086057 | 0.09052442622112741 | 1.5570513358426705 | 3.196194277642087 | 16.97568549147966 | 21.055092462300728 | 5.139633379302668 | 102.10298129696187 | 0.05617026470262276 | 0.0336381206784447 | 0.016120548878256664 | 0.15524193686286272 | 0.188260624126361 | 0.832862491968048 | 0.832862491968048 | 0.15094620466716002 |
| Information Services | 81 | 0.02068361702127659 | 0.10927793514353082 | 0.2187503321074406 | 0.25722215886696137 | 1.0228619556904517 | 1.210329895898512 | 0.11638214632709462 | 0.33631953220947924 | 0.064355 | 0.2571948078093871 | 0.09881012579254235 | 2.3003858434396283 | 1.9345203801039386 | 11.380600486423958 | 16.9698411934083 | 3.3749990528836573 | 143.50472685181344 | 0.14317420782326637 | 0.01973490042030984 | -0.013947351432358696 | 0.0014962129840578925 | 0.08982080004282594 | 0.5528405809168633 | 0.5528405809168633 | 0.11380792726772192 |
| Insurance (General) | 202 | 0.08460260355029592 | 0.11829078864545531 | 0.18156705572027637 | 0.20990187857546344 | 0.629394290783981 | 0.6850762226636024 | 0.08271338587273691 | 0.2478689232245281 | 0.058543 | 0.2600645108966294 | 0.0725725672658889 | 1.8091101184233103 | 1.169134129847309 | 8.142154303147006 | 8.598038176376035 | 1.7824284117595683 | 22.77264393872935 | -0.015909868291309536 | 0.0075983583944395 | 0.004228833772045729 | 0.02016860823021111 | 0.15203983853675432 | 0.4245453994262913 | 0.4245453994262913 | 0.11840530188875235 |
| Insurance (Life) | 137 | 0.08265757009345796 | 0.1081994611376226 | 0.09641658012037313 | 0.1430098540208482 | 0.7749958133235606 | 0.8866231834549279 | 0.09563254605946088 | 0.2529088497524812 | 0.064355 | 0.5093217544162885 | 0.07140297336543747 | 1.0309138465092285 | 1.062582877725027 | 7.215679263423442 | 8.805890086056612 | 1.1248722994828504 | 45.46642003583751 | -0.9618918273783861 | 0.006879342537715868 | 0.004798682264904494 | -0.07883068102302149 | 0.07415972895423793 | 0.6190700745883686 | 0.6190700745883686 | 0.10832802165624869 |
| Insurance (Prop/Cas.) | 228 | 0.09064165803108809 | 0.09758146600419187 | 0.1331121282848552 | 0.18702298039483276 | 0.6647689482362986 | 0.7108225066540635 | 0.08436372267652548 | 0.2674377675554218 | 0.064355 | 0.18249067562498456 | 0.07773868909965642 | 1.6491131323911137 | 1.1297486196935074 | 9.24722869193527 | 10.817649285030537 | 1.5899488639029258 | 19.552938187213638 | -0.284760298271382 | 0.006965993910183879 | -0.003131181087510266 | 0.1901790615584792 | 0.12312293515838725 | 0.31767302616536414 | 0.3176730261653642 | 0.09792192081104666 |
| Investments & Asset Management | 1374 | 0.1147342226487523 | 0.17622005224472428 | 0.05577023711236661 | 0.17295984619363824 | 0.5397928644612402 | 0.7538219195489255 | 0.08711998504308613 | 0.2952473128244418 | 0.064355 | 0.4242460949211658 | 0.07054907213415151 | 0.3486627307782067 | 4.655215766873885 | 16.80944133555133 | 20.170578625395255 | 1.3814510990522955 | 56.35007269514767 | NA | 0.036008275754089686 | 0.07678811784148615 | 0.5242060967646028 | 0.10448446992594382 | 0.5604759651615945 | 0.5604759651615945 | 0.17504604457389847 |
| Machinery | 1492 | 0.06073680695333948 | 0.0991880918076997 | 0.12714981972762668 | 0.2130156548090914 | 1.03836102698098 | 1.0707088534325075 | 0.10743243750502374 | 0.2975651969773884 | 0.064355 | 0.1330768416769064 | 0.09953138282532396 | 1.4758444913873285 | 2.152051180477195 | 14.74009147266254 | 20.50788813757822 | 2.931897166989251 | 59.82145516111431 | 0.283204746618663 | 0.041859504460015566 | 0.04235351210658818 | 0.9159125105760647 | 0.11997300767360276 | 0.41450280864813255 | 0.4145028086481326 | 0.10081767143303741 |
| Metals & Mining | 1815 | 0.1980477777777777 | 0.10664862064250391 | 0.14836568932569902 | 0.3083537659419267 | 0.9888283828600355 | 1.0907339755589993 | 0.10871604783333186 | 0.5751337390211976 | 0.067024 | 0.21730036180967954 | 0.0959686600058396 | 1.4403961344658271 | 1.321840943539155 | 7.816887061757307 | 11.719208861545555 | 1.8383154452637767 | 54.204297468339085 | 0.11976332846375232 | 0.08001763962680722 | 0.048951300244026504 | 0.8486181060050277 | 0.10498912521603516 | 0.859502621972046 | 0.859502621972046 | 0.10717263648228535 |
| Office Equipment & Services | 137 | 0.0710070297029703 | 0.070961579936264 | 0.11212639112128635 | 0.2667674954461756 | 0.7755481534276752 | 0.8288759065679246 | 0.09193094561100398 | 0.2790876657137057 | 0.064355 | 0.22256683686744946 | 0.0821667979019657 | 1.94869207920148 | 1.06430544667157 | 9.433164404749508 | 14.408234304339357 | 1.8408621168699566 | 148.70651436275128 | 0.13322722592940034 | 0.024677177006253274 | 0.01610612551919599 | 0.3043774045124996 | 0.08262946816534691 | 0.5240183295713124 | 0.5240183295713124 | 0.0714975262865802 |
| Oil/Gas (Integrated) | 36 | 0.17374848484848482 | 0.18330450455077887 | 0.21955647007213325 | 0.41146504501815456 | 0.9378980391506078 | 0.9908295261548429 | 0.10231217262652544 | 0.26835269009888657 | 0.064355 | 0.1487666678846342 | 0.09424130439210901 | 1.6577440240335317 | 1.2699079204434358 | 5.329375681172025 | 6.910376636063507 | 1.995998993876314 | 14.03182681845412 | 0.032549087570827244 | 0.07551581451441237 | 0.017882863221327802 | 0.1470972992362722 | 0.2111799007567265 | 0.48938589191024884 | 0.48938589191024884 | 0.18395151105610733 |
| Oil/Gas (Production and Exploration) | 590 | 0.2666915522388059 | 0.3635981139178642 | 0.24158267687634816 | 0.3126073120713543 | 0.9640028763637847 | 1.0888559417354342 | 0.10859566586524134 | 0.48387766980457786 | 0.064355 | 0.21367468576413548 | 0.09566079357781453 | 0.7217778775968877 | 2.381052734287631 | 4.223431799917248 | 6.396844572892298 | 1.542041524916099 | 17.55048381530332 | 0.011379439275655288 | 0.27791758398609806 | 0.142306251128303 | 0.53680367572185 | 0.21873526979182864 | 0.3835460571954803 | 0.3835460571954803 | 0.3659777861602497 |
| Oil/Gas Distribution | 174 | 0.14224071428571422 | 0.20652391715940327 | 0.1263403111518606 | 0.17576164835069488 | 0.5830689215795911 | 0.8547732753174829 | 0.09359096694785066 | 0.29604834790023926 | 0.064355 | 0.4134481382681031 | 0.07476640325243068 | 0.7011935349847029 | 2.435044126632089 | 8.6538309913821 | 11.66765742791088 | 1.7319473403576051 | 379.6137201341005 | 0.04040003139702512 | 0.11718132418192699 | 0.08023052540611693 | 0.47879736709681825 | 0.1980299140664168 | 0.5813383192295897 | 0.5813383192295897 | 0.20766740281227833 |
| Oilfield Svcs/Equip. | 444 | 0.07793392441860464 | 0.06721194579633354 | 0.14553325656056446 | 0.2301869480268253 | 0.8165003226031388 | 0.9765462243377149 | 0.10139661298004753 | 0.36102582329931976 | 0.064355 | 0.29357721636773987 | 0.08573829079412765 | 2.483571853868623 | 0.6441414790034161 | 6.43827911918698 | 8.887525466584957 | 1.489958451553507 | 46.82672174092002 | 0.06444806614870531 | 0.039255162065945426 | 0.021534721834103425 | 0.41173452769247443 | 0.16710585203452488 | 0.2527854321469115 | 0.2527854321469115 | 0.06781531627866524 |
| Packaging & Container | 426 | 0.052569709677419384 | 0.08566052402410433 | 0.11004848275450956 | 0.2277855269020298 | 0.6296021911543933 | 0.8139771520457355 | 0.09097593544613165 | 0.27470203395781206 | 0.064355 | 0.33196678664683954 | 0.07672937449770714 | 1.500826460362026 | 1.3051058737303116 | 9.04903995147484 | 14.919827634507392 | 1.9534952033407125 | 30.816579837398784 | 0.1334650474318476 | 0.06792023071655107 | 0.04488394310228557 | 0.8031165370481568 | 0.0837951355806958 | 0.6620440239883706 | 0.6620440239883706 | 0.08673728826356969 |
| Paper/Forest Products | 266 | 0.030151770334928205 | 0.06546926515126182 | 0.049573756287668545 | 0.20852980162414905 | 0.6745272635760394 | 0.9112356226770696 | 0.09721020341360016 | 0.2923214250279434 | 0.064355 | 0.39221477839053925 | 0.07793289042932547 | 0.8661449398864447 | 1.310328744108613 | 10.145296025613924 | 19.409725734324393 | 1.0700113153525859 | 53.22904085321701 | 0.19301023843083528 | 0.1035625412714256 | 0.06828682180288678 | 1.5270401595610315 | 0.06468581288494171 | 0.5588183001769139 | 0.5588183001769139 | 0.06527002673893548 |
| Power | 488 | 0.10553491271820457 | 0.13542991805419816 | 0.07777329056638789 | 0.20805972007633666 | 0.4470973992829686 | 0.7365451827825267 | 0.08601254621635997 | 0.25342379632553697 | 0.064355 | 0.49590794161286095 | 0.06719173285833159 | 0.6852687404907293 | 1.9842440306784832 | 8.710860032149972 | 14.11305426861972 | 1.3054398461869157 | 19.74645453790872 | 0.051321052580214285 | 0.16145031366596396 | 0.0978459970091638 | 0.9399752179719862 | 0.12425005928175509 | 0.6306400614403218 | 0.6306400614403218 | 0.13547671716176612 |
| Precious Metals | 853 | 0.39661279569892466 | 0.11716428482873283 | 0.09093109941714525 | 0.25659862660670973 | 1.0402350701665934 | 1.0916417105034693 | 0.10877423364327239 | 0.6015926072615447 | 0.067024 | 0.15542889273887203 | 0.09964733863823465 | 0.8076654779709082 | 2.388243444540734 | 8.812981190868676 | 18.8279381793466 | 1.6763220630025488 | 250.16739966900235 | 0.10876920780761577 | 0.1859310527286239 | 0.1127933403861452 | 1.560681789819639 | 0.043236320854281265 | 0.9830800612665044 | 0.9830800612665044 | 0.11750297486073452 |
| Publishing & Newspapers | 324 | 0.021356641221374026 | 0.06755366934098846 | 0.08380137544218207 | 0.1510460073303066 | 0.888119661393053 | 0.8946248623694311 | 0.09614545367788054 | 0.30651468123456876 | 0.064355 | 0.1870421256352493 | 0.0871515069410619 | 1.4638192187131276 | 1.3350774004036638 | 11.149755418406585 | 18.762274053118684 | 1.5791572059386556 | 151.60478716541692 | 0.09368642756794865 | 0.03317992472146954 | 0.0014372747150760389 | 0.12410318055865499 | 0.07706709737549311 | 0.41359921166168145 | 0.41359921166168145 | 0.06653069570962454 |
| R.E.I.T. | 659 | 0.09313607966457031 | 0.3147747366624331 | 0.03419004504110163 | 0.031473434098282925 | 0.518676720895122 | 0.8045890535754917 | 0.09037415833418902 | 0.19507213564220016 | 0.058543 | 0.4391650242389279 | 0.069885245287652 | 0.11833306407750671 | 11.736466940021847 | 20.989918696773227 | 35.178934935581324 | 1.5208705970932974 | 63.34198505876185 | 1.0816859107397565 | 0.06469433602206726 | -0.05235482018456911 | -0.15371841024421157 | 0.02360740857350486 | 3.0371936222786355 | 3.0371936222786355 | 0.29476744207796207 |
| Real Estate (Development) | 884 | 0.10489185582822078 | 0.05008086776968071 | 0.020519444443367223 | 0.2936327237915764 | 0.41518460236100446 | 0.9838192893514592 | 0.10186281644742855 | 0.3226407984583051 | 0.064355 | 0.7133891845775145 | 0.06348069309822776 | 0.4813605407740626 | 1.6844769371768087 | 13.210589287216825 | 25.061544895916906 | 0.4749923270093885 | 85.61782512481719 | 1.9372904748389614 | 0.024175751924503067 | 0.0156418801478079 | -2.4874862323222344 | -0.03484020169433607 | 0.007953247477577668 | 0.00795324747757764 | 0.04982877978065471 |
| Real Estate (General/Diversified) | 336 | 0.043873405797101465 | 0.15167474002655607 | 0.035054354887619446 | 0.2811506132640649 | 0.5402762120215623 | 0.9412697957463101 | 0.09913539390733848 | 0.25548788218587737 | 0.064355 | 0.5473580673539544 | 0.0711790368793089 | 0.2635230813358876 | 3.345216132295702 | 13.533672644677281 | 19.755324773603927 | 0.6763235915355317 | 82.37810039802746 | 1.1297095601126692 | 0.08625186294579883 | 0.08263981951953812 | 1.101716107166683 | 0.03972777403412024 | 0.5754716568717486 | 0.5754716568717486 | 0.15726657130404778 |
| Real Estate (Operations & Services) | 748 | 0.0853380265654649 | 0.16934513350573346 | 0.03906588983308024 | 0.20979484449374175 | 0.5601396650240725 | 0.8751991180677632 | 0.09490026346814362 | 0.2896694113717817 | 0.064355 | 0.47132844724291256 | 0.072823262816387 | 0.25417193766136426 | 4.070480362190564 | 16.501271688502577 | 21.26265606980112 | 0.9182357349998902 | 66.29074531924107 | 0.19381853732242285 | 0.025089112611829608 | 0.023190835360523392 | 0.1355762381327822 | -0.028154334130633382 | 0.006595846366837411 | 0.00659584636683741 | 0.17582372303902696 |
| Recreation | 326 | 0.06745337448559668 | 0.11257736658811479 | 0.11185676111013582 | 0.24549862040910803 | 0.9009533857969224 | 0.9948681136678436 | 0.10257104608610877 | 0.31551562219003826 | 0.064355 | 0.21268298134588468 | 0.09097754107068837 | 1.217049747767757 | 2.1605517731648627 | 11.793257016689152 | 19.324996402942176 | 3.0397868598630815 | 65.70636344576498 | 0.16351049819930016 | 0.06218833328725202 | 0.030626786553431828 | 0.4828574746721958 | 0.09452247803676629 | 0.48688895447622094 | 0.48688895447622094 | 0.10633930550184406 |
| Reinsurance | 34 | 0.08025758620689655 | 0.10234972842353285 | 0.23300411586091976 | 0.1710653074295285 | 1.0857693512076685 | 1.141023579620872 | 0.11193961145369791 | 0.23429812694853552 | 0.058543 | 0.21538998013834518 | 0.09724577182947802 | 2.61483968472586 | 0.7571375575209435 | 8.518185888789777 | 7.379860497167062 | 1.3386475086303302 | 13.49980534711361 | -0.6973276816797296 | 0.0006738376188928387 | 0.018491228366908426 | 0.31393549854645547 | 0.18999090330907184 | 0.21042384692812818 | 0.2104238469281282 | 0.10227896161981584 |
| Restaurant/Dining | 394 | 0.036257622377622395 | 0.09505901095729707 | 0.1287733318373561 | 0.192004542456971 | 0.8469120945471883 | 0.9801535686910061 | 0.1016278437530935 | 0.29860207290824436 | 0.064355 | 0.21472117827075912 | 0.09012576064745531 | 1.7170453671868768 | 2.689154149655912 | 16.482868061831127 | 29.127158687564183 | 9.191184194179934 | 79.59438351118557 | -0.015570926850960377 | 0.042112293334399024 | 0.01654178029422381 | 0.2483825751653092 | 0.24646866445962629 | 0.6404025280634015 | 0.6404025280634015 | 0.08689553242317735 |
| Retail (Automotive) | 204 | 0.07397937931034479 | 0.04584363400371386 | 0.10481182756223022 | 0.22757761647084082 | 0.7151526523022773 | 0.9984182748699064 | 0.10279861141916101 | 0.3273261317518817 | 0.064355 | 0.38448853694962754 | 0.08175236352935422 | 2.9249830898771987 | 0.7630474626398553 | 11.188689690797085 | 16.606135028579907 | 3.2512101325430622 | 30.23868574486237 | 0.10706378902882019 | 0.019475688209471428 | 0.017281765587046718 | 0.8282777368984547 | 0.20769252360863635 | 0.26136084734296855 | 0.2613608473429685 | 0.0436712430670153 |
| Retail (Building Supply) | 120 | 0.053912839506172844 | 0.10876679058825121 | 0.2434078621058677 | 0.243543717914554 | 0.9624856160601153 | 1.1069063250264495 | 0.10975269543419541 | 0.30071356129427346 | 0.064355 | 0.1864372227857414 | 0.09825093917256539 | 2.830654398471692 | 1.8618827532091615 | 12.924894242121775 | 17.009576813204827 | 19.811084981805248 | 33.618358654770894 | 0.08974502663749971 | 0.026357907198269647 | 0.008459289446716362 | 0.05879493485247277 | 0.8522817280375384 | 0.4731673198122778 | 0.4731673198122778 | 0.10736791491467855 |
| Retail (Distributors) | 1028 | 0.1037008665749656 | 0.05219898471908759 | 0.08729577431256255 | 0.22076759899753468 | 0.6107295837787711 | 0.8024527976818081 | 0.09023722433140391 | 0.310820691469926 | 0.064355 | 0.36447404135218536 | 0.07486483537116838 | 1.9850579256746446 | 0.8312963718491309 | 11.837965793763221 | 15.17094325756826 | 1.6896602976560269 | 47.96349712077025 | 0.15950699645612898 | 0.027385728666768392 | 0.02785637218603638 | 0.7507573636319772 | 0.14332500695587785 | 0.36173027740438013 | 0.36173027740438013 | 0.05259131543797793 |
| Retail (General) | 256 | 0.00962261538461539 | 0.04354224163527193 | 0.08347827970872808 | 0.1937942292977833 | 0.9930678407425075 | 1.0856124994038356 | 0.10838776121178587 | 0.2972838203067488 | 0.064355 | 0.1680989294267964 | 0.0982467819204331 | 2.1335725223471855 | 1.4828729592721792 | 15.611727952528396 | 34.18498849935147 | 4.781420312674802 | 65.25379490127541 | -0.012451183702950721 | 0.04724451227655676 | 0.01900452171270064 | 0.7258827172270904 | 0.15077463621146756 | 0.2588761758041417 | 0.2588761758041417 | 0.045982485680762096 |
| Retail (Grocery and Food) | 201 | 0.05332968354430376 | 0.039152682778807624 | 0.1088812105703706 | 0.23475115944607725 | 0.5519051683925645 | 0.705680360826839 | 0.08403411112900039 | 0.25255189468537254 | 0.064355 | 0.33371729426885527 | 0.07202903288653367 | 3.4246814204206175 | 0.6274825802759753 | 9.29261974663617 | 15.848493854891704 | 2.511722796665512 | 40.906368724614 | -0.030261379667246235 | 0.02956309714105123 | 0.00988534737172546 | 0.3000843333618986 | 0.10054514265836897 | 0.5021504998959198 | 0.5021504998959198 | 0.039591001476449124 |
| Retail (REITs) | 123 | 0.05323048543689318 | 0.48374162072210686 | 0.044961316107197745 | 0.044981924599759 | 0.6148047022774255 | 0.9472021176371492 | 0.09951565574054128 | 0.17432124177759648 | 0.058543 | 0.43600243609609307 | 0.07518857572027292 | 0.09823803799271287 | 12.063494268116482 | 18.137472907035068 | 22.997222452541262 | 1.1688862348470348 | 77.55700762936728 | -0.07144270536301826 | 0.034648147310819416 | -0.032494460963517484 | -0.08525345732360949 | 0.03561672473232391 | 1.6515768649547715 | 1.6515768649547715 | 0.4749556436009854 |
| Retail (Special Lines) | 639 | 0.05191495238095237 | 0.05042217907288426 | 0.11756426158826139 | 0.25216642740714357 | 0.980796728945327 | 1.0906405392648795 | 0.10871005856687878 | 0.3381580139068764 | 0.064355 | 0.21088688811216771 | 0.09591982267037186 | 2.6894797418402403 | 1.1241172369518075 | 11.714060757610003 | 21.0652365615444 | 3.5753490889594213 | 48.403695063803546 | 0.06132524578190501 | 0.022601381462110836 | 0.010176207106635242 | 0.22248105248757089 | 0.08228908811454388 | 0.7110192463684515 | 0.7110192463684515 | 0.05164689882435198 |
| Rubber& Tires | 89 | 0.05151014285714283 | 0.08779744381418667 | 0.08670171150271351 | 0.22925931428575888 | 0.8848772364010901 | 1.044744213088216 | 0.10576810405895466 | 0.2690211904339668 | 0.064355 | 0.29805660736281797 | 0.08856791593557688 | 1.1842357353944357 | 1.0282305738273885 | 6.937882618901526 | 11.448330027422394 | 1.2500330822119678 | 30.55131207043543 | 0.22165245192765948 | 0.06427069529051858 | 0.0407420115395582 | 0.7027237598756656 | 0.09015662424350955 | 0.36944271507301674 | 0.36944271507301674 | 0.0884005633660413 |
| Semiconductor | 647 | 0.05773729910714279 | 0.16322682653942908 | 0.114165502163095 | 0.12199186980792052 | 1.6672585627718395 | 1.6822579862201206 | 0.14663273691670975 | 0.3438195665674977 | 0.064355 | 0.07373440500180067 | 0.1393645579633603 | 0.7359665502599343 | 6.3251190470549785 | 20.981056455013007 | 37.44856548929744 | 5.04988517271824 | 110.9653407444195 | 0.16662104351990092 | 0.20552519176488987 | 0.11495413779205406 | 0.9343515564878387 | 0.12679960999111167 | 0.5089241654655245 | 0.5089241654655245 | 0.16739903396879177 |
| Semiconductor Equip | 367 | 0.08230695312500004 | 0.21824208267685807 | 0.23276660818443082 | 0.15580173596694383 | 1.965518756667748 | 1.9544533519177911 | 0.16408045985793043 | 0.3351128957237849 | 0.064355 | 0.05802381238635139 | 0.15734852868163274 | 1.1814497522995537 | 5.143673155108626 | 19.317946832775053 | 23.201206714872182 | 6.020479517171844 | 53.58613842117239 | 0.3106031314736264 | 0.10522991608042923 | 0.08208706213281063 | 0.6056721166917823 | 0.2629036594867058 | 0.28643463629818017 | 0.2864346362981802 | 0.22432131540380976 |
| Shipbuilding & Marine | 348 | 0.08735046762589929 | 0.17220230906567338 | 0.11145415365810689 | 0.13252980229125183 | 0.8631601762392301 | 0.9453479455543992 | 0.09939680331003699 | 0.29862899830307615 | 0.064355 | 0.3086512244938419 | 0.08355173302327903 | 0.7506357359214945 | 1.4812037419285917 | 6.117194368361085 | 8.44645920189936 | 0.9527523070472024 | 16.820605028707856 | -0.0048828006332957315 | 0.10792273114460799 | 0.05447159926448501 | 0.1540889710328404 | 0.13643801936112443 | 0.9844363726578802 | 0.9844363726578802 | 0.17202742276129493 |
| Shoe | 85 | -0.01577904761904762 | 0.09681051066273828 | 0.15682992610629745 | 0.18937093682463682 | 0.8721798577655788 | 0.8997075382086072 | 0.09647125319917171 | 0.31722109009264277 | 0.064355 | 0.11004901871848087 | 0.09114367684506283 | 1.87883565697323 | 2.2689859800308474 | 17.311594837188313 | 23.138673472383207 | 4.847626279455051 | 37.91823660764975 | 0.1999959955890515 | 0.0155448432405021 | -0.004839285759461316 | -0.16076892920930544 | 0.18728005326541663 | 0.409713367577831 | 0.40971336757783106 | 0.09682900806840694 |
| Software (Entertainment) | 317 | 0.09019086419753085 | 0.24397492356226416 | 0.15958092016299497 | 0.16758546169524044 | 1.3553519753448988 | 1.356775411126699 | 0.1257693038532214 | 0.4382090246503033 | 0.064355 | 0.047797711791041766 | 0.12205499195264415 | 0.7038722223983201 | 5.604623076659677 | 17.539469415145657 | 22.713777633858786 | 5.1419967098307415 | 235.2071073525805 | 0.012379849093651437 | 0.10657483391064419 | 0.06939299789868697 | 0.4056523435520016 | 0.20902108693447324 | 0.027408126710642 | 0.027408126710641967 | 0.2539681337781789 |
| Software (Internet) | 151 | 0.12337151515151513 | -0.0007929462693840991 | 0.013073769344178877 | 0.19524857352132755 | 1.298774525993413 | 1.3617461374106075 | 0.12608792740801994 | 0.4698226412977677 | 0.064355 | 0.0997544457795296 | 0.11830432607700352 | 0.8787634525735459 | 6.014836641489651 | 20.43779506759383 | NA | 7.966227226370068 | 62.96786353390488 | 0.05207557992689165 | 0.059528224990848 | 0.03349517717879784 | NA | -0.10004457144069427 | 0.003742653810663614 | 0.003742653810663632 | 0.014866689098504715 |
| Software (System & Application) | 1616 | 0.14317631639722875 | 0.20245159521759293 | 0.18335837660819057 | 0.18835127456152267 | 1.2856288444138266 | 1.298989733922843 | 0.12206524194445424 | 0.4359142137619651 | 0.064355 | 0.05849855321588472 | 0.11773606072885787 | 0.9343146311452694 | 9.20213603267864 | 28.477414772492736 | 41.06942761789676 | 9.152165527378905 | 96.42955861610483 | 0.1335332117963446 | 0.07233864732673151 | 0.05885835272308939 | 0.4763010165661551 | 0.16957095297200736 | 0.3289132253967318 | 0.32891322539673173 | 0.2128494752540535 |
| Steel | 718 | 0.08987769376181497 | 0.07188270996116729 | 0.0904906469174532 | 0.20410892423422447 | 1.006786675768852 | 1.1651510574107116 | 0.11348618278002662 | 0.32684206346899697 | 0.064355 | 0.29282307986344275 | 0.09432797838111776 | 1.4569431690097083 | 0.8234515222700458 | 6.896510713908434 | 10.902342900094519 | 1.1441036709966868 | 42.97637774132422 | 0.1463639736470269 | 0.06046124169077838 | 0.038355539277544884 | 0.5365682468211627 | 0.00010149487153178553 | 0.5075703862611376 | 0.5075703862611376 | 0.07221629768650172 |
| Telecom (Wireless) | 98 | 0.0589098734177215 | 0.14601324969098128 | 0.08308394526497115 | 0.22352795591870583 | 0.6530666984464208 | 0.897027162733216 | 0.09629944113119915 | 0.29268715180378874 | 0.064355 | 0.4004265931789509 | 0.07698321179612677 | 0.7055913479848427 | 2.2521573000348893 | 7.3658215226325705 | 15.636398623682114 | 1.5396711794028626 | 33.14019231705149 | -0.13702130661688386 | 0.152332531395948 | 0.015600504167240651 | 0.3050583637784972 | 0.08181796535473856 | 0.7358141070495954 | 0.7358141070495954 | 0.14327448180824276 |
| Telecom. Equipment | 453 | 0.04597224324324329 | 0.10996963575683873 | 0.1362119863769908 | 0.1478267622747537 | 1.1744668677688677 | 1.185716234992941 | 0.11480441066304753 | 0.36121152315507643 | 0.064355 | 0.11422832700367296 | 0.10718034416385619 | 1.2621053433181886 | 2.3180551802022675 | 14.280877316972678 | 19.41242551940864 | 3.4564201757538724 | 120.3162423275964 | 0.2467526994732747 | 0.03158775202621778 | 0.02561034135214803 | 0.5362424352475735 | 0.12935477470221632 | 0.5328168427334831 | 0.5328168427334831 | 0.11666475116522716 |
| Telecom. Services | 288 | 0.08399032558139537 | 0.15465250724642488 | 0.09502129852429446 | 0.21847468285036423 | 0.543807658930849 | 0.849373944269902 | 0.09324486982770072 | 0.3013188613936473 | 0.064355 | 0.4567224046170274 | 0.07260807083852093 | 0.7033661156283555 | 2.1627790318150595 | 6.87826173239651 | 13.871231213040748 | 1.3805704498802125 | 41.987956622506964 | -0.0022673400403473644 | 0.1474304776645122 | -0.014085192899059221 | -0.0328430395021499 | 0.0779658250341491 | 0.8972629293469917 | 0.8972629293469917 | 0.15572276593304957 |
| Tobacco | 56 | 0.17277631578947372 | 0.33764511168785427 | 0.23171724996207474 | 0.2244021922465821 | 0.5533516641188336 | 0.6668153472871898 | 0.08154286376110886 | 0.31215895747055444 | 0.064355 | 0.2486214464550605 | 0.07321838380849845 | 0.8277635948646116 | 3.4660578760708205 | 9.334613473587153 | 10.23405906734787 | 3.1655940261072453 | 32.34526176009394 | 0.160557632946608 | 0.027943882680795982 | 0.12228402836106568 | 0.5479142566521387 | 0.28431447473661764 | 0.7167329555663585 | 0.7167329555663585 | 0.338803061493157 |
| Transportation | 443 | 0.06527082508250827 | 0.06435501724804757 | 0.08934491370457888 | 0.22908287037391753 | 0.7460208539065312 | 0.9408740913308127 | 0.0991100292543051 | 0.30380702193123765 | 0.064355 | 0.32986359315353947 | 0.08227058675105496 | 1.6277454450437747 | 1.2696774679411371 | 10.42705949519842 | 18.777765446190777 | 2.1765217731429574 | 28.20138997386132 | 0.03634259138927476 | 0.0529751563321938 | 0.017747701289386193 | 0.2842895547246911 | 0.1310556943227592 | 0.5045483878998465 | 0.5045483878998465 | 0.06500330200447187 |
| Transportation (Railroads) | 49 | -0.003088571428571427 | 0.21498144726244753 | 0.06911956076890328 | 0.24505070391318387 | 0.49774817486891265 | 0.6287330139602276 | 0.07910178619485059 | 0.1925517420182543 | 0.058543 | 0.2963758386366957 | 0.06861545367636401 | 0.41782902810812156 | 4.330807666885992 | 13.312399536973741 | 19.99149807548134 | 2.364619435710157 | 54.74120388067776 | 0.05750694818191757 | 0.15777752692235822 | 0.09369508542243203 | 0.5999807472548995 | 0.11847480095542914 | 0.40046902958975955 | 0.4004690295897595 | 0.21543368123934659 |
| Trucking | 106 | 0.03021282051282051 | 0.08600260208420525 | 0.11601095133243039 | 0.2576812815542906 | 0.8685544613027371 | 1.0142471138460685 | 0.10381323999753299 | 0.2911515050298223 | 0.064355 | 0.22285087362357622 | 0.09138865173191216 | 1.6608901785159862 | 1.5858226133716178 | 9.975911701096043 | 17.984157510576416 | 2.8560845316782566 | 27.978465612651178 | 0.06887580582714121 | 0.11440306207150298 | 0.0709062887717008 | 1.0534268769842425 | 0.12020693727190153 | 0.20666338943773307 | 0.2066633894377331 | 0.08756853622132452 |
| Utility (General) | 50 | 0.07822044444444445 | 0.1226477130898772 | 0.08320329489198379 | 0.20200998795914918 | 0.45062860002415905 | 0.6833212006287833 | 0.08260088896030501 | 0.18493219542658187 | 0.058543 | 0.4448745696058084 | 0.0653037312471858 | 0.8126579164565683 | 1.8774889614873251 | 9.857640046481395 | 15.28891440825529 | 1.615489714297475 | 20.357420845545533 | -0.005972675226400996 | 0.14206470240344746 | 0.0774702135312875 | 0.7842162740133911 | 0.10614481878166145 | 0.6670336160874528 | 0.6670336160874528 | 0.12236645400729415 |
| Utility (Water) | 102 | 0.0643201265822785 | 0.23268694623750147 | 0.06233778435011252 | 0.19785675095563685 | 0.4274749642866797 | 0.6700706237217016 | 0.08175152698056107 | 0.23638245507713002 | 0.058543 | 0.46441396893036424 | 0.0640891139083728 | 0.31191832028707533 | 4.586730603072258 | 12.671747297577289 | 19.57400783851767 | 1.4758103846880881 | 26.689561208834526 | 0.07351491716518994 | 0.22672810101363378 | 0.1157283775757966 | 0.9624500898653524 | 0.008643179175213485 | 0.8329098960481567 | 0.46710436060400684 | 0.23254289553331944 |
| Total Market | 47698 | 0.09241073828936881 | 0.09973011387095097 | 0.06940509121988034 | 0.2177750939884145 | 0.7862553553280948 | 1.0126713640221112 | 0.10371223443381733 | 0.34377339651496613 | 0.064355 | 0.38429196179492087 | 0.08232564875265083 | 0.7855098642027194 | 2.3247142544915254 | 12.637940500302095 | 18.943156174827294 | 2.0947026740752137 | 69.34631263922105 | -1.1741621987258182 | 0.05920970311575726 | 0.0324145842784861 | 0.5013197469909659 | 0.008643179175213485 | 0.46710436060400684 | 0.46710436060400684 | 0.10079068098279807 |
| Total Market (without financials) | 42566 | 0.09014652492930246 | 0.1040142263401258 | 0.11066121900138588 | 0.22913282338577817 | 0.905029349985941 | 1.0400974791141913 | 0.10547024841121967 | 0.3518111767981802 | 0.064355 | 0.2365927927390806 | 0.09188747169790176 | 1.1967894578056688 | 1.9179992146300602 | 11.564480426364062 | 17.591607430516678 | 2.4768948341486112 | 71.79655523413336 | 0.1157258739983058 | 0.06384133546592097 | 0.03514072812939737 | 0.519346816320147 | 0.006288025122559176 | 0.5204190303625429 | 0.5204190303625429 | 0.10518808980286382 |

## Input Stat Distributioons

| Revenue Growth Rate = Last 3 years | Pre-tax Operating Margin | Sales to Invested Capital | Cost of Capital | Beta | Debt to Capital Ratio |
|---|---|---|---|---|---|
| First Quartlie | First Quartlie | First Quartlie | First Quartlie | median(Beta) | First Quartlie |
| -0.0227 | -0.05163398692810457 | 1.39654463183875 | 0.09836891315438587 | 0.6440464534599691 | 1.203144563302701 |
| 0.00268 | -0.06331694441331505 | 0.5795037109228578 | 0.07927123819983303 | 0.5067993389789744 | 0.9259121818896379 |
| 0.09210000000000002 | -0.03366526235158943 | 0.4822614953489223 | 0.07548634270861693 | 0.7784964479395179 | 1.240713233739075 |
| -0.0119 | -0.02992366421898226 | 0.6410073787071592 | 0.0809939896693336 | 0.3133717668461348 | 0.7884320972122296 |
| 0.0434 | -0.2543810062182024 | 0.5915638270621842 | 0.085515379882285 | 0.8500670587943352 | 1.391400674129436 |
| 0.0775 | 0.0179178655506147 | 1.004318322023442 | 0.09775278367129892 | 0.833431933229425 | 1.232626377077593 |
| 0.0823 | 0 | 0.1483223367588072 | 0.06105718460287066 | 0.2622764322642789 | 0.8358118490036747 |
| 0.0444 | 0 | 0.1858490566037736 | 0.04881219951969602 | 0.2057687656370838 | 0.4418342101687323 |
| 0.0462 | 0.01880790611488573 | 0.5973506623344162 | 0.07059025425896753 | 0.3346210148305092 | 0.7149946961782315 |
| 0.0394 | -0.1572953054607621 | 1.220314307281951 | 0.06898751822706016 | 0.227864792957012 | 0.6004673207561629 |
| -0.00195 | -0.02509316770186336 | 0.6200668292242392 | 0.0736719858968715 | 0.5050759990877971 | 1.021566703669367 |
| -0.038 | 0 | 0.07491010787055533 | 0.05916207485232679 | 0.3493481690300868 | 0.9118862151101015 |
| 0.0197 | 0.01153122058362096 | 0.9046011234230639 | 0.08405588120214819 | 0.5036193196570941 | 0.9747940732489032 |
| 0.0259 | 0 | 0.9391323659919348 | 0.08255148945638 | 0.5221486638994687 | 0.9899478226686172 |
| -0.0407 | -0.009173715029277815 | 0.3379001381352765 | 0.06739569145758198 | 0.633084545543681 | 1.077758748701366 |
| 0.0449 | -0.001032702237521515 | 0.7778878089316388 | 0.08617527129200236 | 0.6177338525468948 | 1.046070122202205 |
| 0.0566 | 0.02850809957845308 | 0.9055361525391733 | 0.07950987790559788 | 0.6993101230345485 | 1.125450608340361 |
| 0.0382 | 0.00247787610619469 | 0.6829360575104048 | 0.08607563438672819 | 0.5586488007229141 | 0.9824680873781174 |
| 0.11 | -0.1298429319371728 | 0 | 0.08865915065955403 | 0.3727351568985759 | 0.9444725696960092 |
| 0.0161 | 0.005176534492123846 | 1.43595041322314 | 0.09043512842322962 | 0.5648900084166104 | 1.003765905072171 |
| -0.0421 | -0.05042424242424243 | 0.826106800547695 | 0.1024153249601094 | 0.8059414775513541 | 1.208390091947987 |
| 0.0141 | 0.01701214721701819 | 0.551623646960866 | 0.0768609955377672 | 0.4269034632197925 | 0.9057036612311372 |
| 0.0446 | 0.02756813417190775 | 0.2325669374080096 | 0.07342226115527012 | 0.3993751342500558 | 0.916923264166887 |
| -0.05300000000000001 | -12.87079134971378 | 0.001864031639602062 | 0.09107256542614203 | 0.6412542267471837 | 1.108579338558525 |
| 0.0121 | -0.2980958634274458 | 0.408505875769446 | 0.07946971827051694 | 0.4689517632669788 | 0.8547367162095574 |
| 0.00507 | -0.03421828908554572 | 0.4005450508041181 | 0.0749829152471205 | 0.2599929931506992 | 0.7681542434214266 |
| 0.0342 | -0.01394495412844037 | 0.7853844064113013 | 0.09461882571311157 | 0.5918704821430562 | 1.080245257160927 |
| -0.0438 | -0.05801324503311259 | 1.061159287996349 | 0.09109518207902552 | 0.718953127517035 | 1.179104108245023 |
| -0.0166 | -0.06284333113601406 | 0.7042062415196745 | 0.1031493045695606 | 0.7469700779027746 | 1.254871304110378 |
| -0.0192 | -0.002638888888888889 | 0.7684371388011885 | 0.07820543034194977 | 0.5249899919156651 | 0.9668772105712965 |
| -0.0281 | -0.2458333333333333 | 0.4651369619352543 | 0.08614980063257772 | 0.5179071021794708 | 1.023460922346831 |
| -0.00184 | -0.06797119384619679 | 0.3835955453420541 | 0.07579559707108771 | 0.4993375462559688 | 0.8926869790372804 |
| 0.04940000000000001 | -0.01596491228070175 | 0.4794372294372294 | 0.06887448554733712 | 0.2628207663690826 | 0.691037878605737 |
| 0.00138 | 0 | 0.09444193402620875 | 0.05015195025444996 | 0.3561613360222687 | 0.8489303381625015 |
| 0.0252 | 0.008142059553349876 | 0.9414225941422594 | 0.07125676511630759 | 0.2746399106884778 | 0.6492798789831261 |
| 0.0147 | 0.006541935483870968 | 1.34020618556701 | 0.06443677801173839 | 0.207481014179219 | 0.6544334014781269 |
| -0.014 | 0 | 1.031948881789137 | 0.08833212571343328 | 0.4736518087854164 | 0.8969749608616471 |
| 0.0213 | 0.03963133640552995 | 0.1288690834638083 | 0.06686868560646486 | 0.3395022706532055 | 0.8869557532952093 |
| 0.0186 | -0.9327389618567661 | 0.5139240506329116 | 0.08635256623146172 | 0.6345997594353269 | 1.022950940395206 |
| 0.0329 | -0.05046728971962618 | 1.019607843137255 | 0.07639012358270988 | 0.4404301273652743 | 0.7812420315124222 |
| 0.0421 | -0.8819425003288887 | 0.4816417212347989 | 0.09218717236217229 | 0.7727967597261343 | 1.151970976712207 |
| 0.0281 | 0.02492248062015504 | 0.7688191223688906 | 0.08226064164006815 | 0.6534006796804992 | 1.049749698895646 |
| 0.0609 | 0.03757700205338809 | 0.6656414762741653 | 0.06514910494885043 | 0.3335281963627414 | 0.7757983755317827 |
| 0.0573 | -0.05937136204889405 | 0.2058252427184466 | 0.0767629476293663 | 0.3614314945730799 | 0.9005309871503696 |
| -0.0165 | -0.01415525114155251 | 0.8974097491331837 | 0.07441245466869095 | 0.3073668271172179 | 0.6653142532759653 |
| 0.00825 | 0.01992347275366143 | 1.282051282051282 | 0.08700663139659845 | 0.5679741849811997 | 1.094170919644543 |
| 0.0348 | 0.03931865605134691 | 1.012345679012346 | 0.07150919627494529 | 0.1807036048591203 | 0.6600810478222483 |
| -0.0236 | 0.0001834150485030975 | 0.6518219120306374 | 0.07432040677157861 | 0.4278628859963649 | 0.8531242719845141 |
| 0.038 | 0.04937965260545906 | 0.8204419889502762 | 0.06901070313049372 | 0.3628355151361401 | 0.6637958526182828 |
| -0.029 | -0.00133054808346924 | 0.007109660285492973 | 0.06227634483954853 | 0.1314166379182863 | 0.5879115554656339 |
| 0.036 | 0.01434352836649245 | 0.8493358633776091 | 0.0907609636688385 | 0.5975616522506249 | 1.015786908217617 |
| 0.0325 | -9.61111111111111 | 0 | 0.08401048758680386 | 0.5594744857874498 | 1.044028472258659 |
|  | 0 |  |  | 1.258030612019513 | 1.258030612019513 |
| 0.0209 | 0.008777372262773723 | 0.9243662955507168 | 0.07722896469767941 | 0.3483511264209298 | 0.7859973551387082 |
| 0.154 | 0.06667398829369865 | 1.219214121148865 | 0.08162772120256655 | 0.5309154964964505 | 0.8969749608616471 |
| 0.08470000000000001 | -0.3180952380952381 | 0.06046313005210847 | 0.08238134470142476 | 0.5390729959110587 | 0.9976809475733847 |
| 0.0158 | 0.02072186836518047 | 0.3486269634987005 | 0.06636544789309094 | 0.3743267524927403 | 0.8298620595680499 |
| 0.0254 | -0.002202224952687693 | 0.7416743419458046 | 0.07525862229948913 | 0.4491816388545652 | 0.9668286408616179 |
| 0.0342 | 0.03025936599423631 | 1.013722627737226 | 0.07084668672720806 | 0.380349396492883 | 0.763735149597427 |
| 0.0338 | -0.01255278310940499 | 0.5785837651122625 | 0.07173873119214594 | 0.4104869013484358 | 0.833869060616532 |
| 0.0654 | 0.04388979634228093 | 0.3990843189622281 | 0.06077639154652098 | 0.3336496206369378 | 0.6483978432642004 |
| 0.00285 | -3.8 | 0 | 0.08616658917032927 | 0.5797345063276523 | 1.040410168765752 |
| -0.0131 | -0.03220779220779221 | 0.7086882453151618 | 0.08959226836890329 | 0.4299147852198638 | 0.9108755561319086 |
| 0.0114 | 0.1851258046809299 | 0.05777435825697698 | 0.05948160984090209 | 0.4165338302034178 | 0.7917797040265699 |
| -0.109 | -0.0729559748427673 | 0.1020055325034578 | 0.06337531121992672 | 0.428724827332739 | 0.9262277459139344 |
| -0.0602 | 0.005366795366795367 | 0.07679024885728795 | 0.06504057564192911 | 0.4327075435263816 | 0.906561620815254 |
| -0.0089 | 0.03916400791529651 | 0.06206501762525986 | 0.06369953793084188 | 0.2400072203766545 | 0.7532513259957963 |
| 0.0276 | -0.01717171717171717 | 0.5923460898502496 | 0.08003937144051153 | 0.4924882135384958 | 1.021529975355817 |
| 0.0391 | 0.07748739110499772 | 0.8234192553425865 | 0.09794090329137616 | 0.6449328899668939 | 1.048547177395812 |
| 0.0179 | -0.01884905590244753 | 1.238805970149254 | 0.07764783886670062 | 0.4306930231827682 | 0.8048729439384256 |
| 0.039 | 0.0006964084785451448 | 1.509438359356793 | 0.07149466568881499 | 0.3987987313862636 | 0.8701506337464239 |
| -0.00369 | 0.01672473867595819 | 1.293890538837104 | 0.08084781067662387 | 0.573292568191003 | 0.9935419811848315 |
| 0.00586 | 0 | 0.7239263803680981 | 0.06846876978254893 | 0.2858084566035461 | 0.7728005173009658 |
| -0.0776 | -0.00920282542885974 | 0.6920122887864822 | 0.08298676092872442 | 0.5410665658192717 | 0.928038329488805 |
| -0.00183 | 0.01449814126394052 | 2.231317522786168 | 0.06576515271101267 | 0.3296063709452022 | 0.5640582357927003 |
| 0.0135 | 0.3986254295532646 | 0.07479637862218907 | 0.06265727326477667 | 0.5703986672944151 | 0.9139362270216549 |
| 0.0007000000000000001 | -0.009647044568335218 | 1.500887614365697 | 0.08334712969165906 | 0.5911251536049448 | 0.9772468435876711 |
| 0.05019999999999999 | 0.03844705882352941 | 0.891178688112591 | 0.08322508029770886 | 0.6274517277099881 | 1.090171418590347 |
| -0.0273 | -0.1291711517761033 | 0.5772338482117424 | 0.1245526186995488 | 1.135486957720453 | 1.58973516748928 |
| 0.00831 | 0.01263736263736264 | 0.7437503169210485 | 0.1391919158417226 | 1.299608294458068 | 1.959755909254536 |
| 0.0488 | 0.06260683760683762 | 0.3166890195673854 | 0.0817372818979578 | 0.4856970967857017 | 0.8676063939372943 |
| -0.0205 | -0.03880232202871983 | 0.8096095764341992 | 0.08354653624791157 | 0.2618878745868504 | 0.8959411495857447 |
| 0.00899 | -0.2752542372881356 | 0.9122424722662439 | 0.1007463724299459 | 0.7619373205825695 | 1.308613687869716 |
| 0.0343 | -0.231549815498155 | 0.5462653288740246 | 0.09637620564520535 | 0.7425337215659807 | 1.205698786213557 |
| 0.0241 | -0.3719806763285025 | 0.7376570260005844 | 0.09744367380212228 | 0.689953200263927 | 1.157974733301631 |
| 0.0704 | -0.002836269875376021 | 0.8826742407690626 | 0.08792334520885384 | 0.6168803328960546 | 1.144180935752917 |
| 0.0177 | 0.0414738929279577 | 0.5751724137931034 | 0.06806752705099503 | 0.3560402567987587 | 0.7000595104520712 |
| -0.0375 | -0.1044444444444444 | 0.7619595594279139 | 0.09291137856426393 | 0.6528983223541794 | 1.099982499945418 |
| 0.0074 | -0.0002114164904862579 | 0.556161703055388 | 0.06330644360792485 | 0.3597801244440085 | 0.776969645728087 |
| 0.027 | -0.005756186984417965 | 0.8892865726674298 | 0.06443476105256096 | 0.2152123835857444 | 0.5277019396298577 |
| 0.00328 | -0.01719280184845445 | 0.6544117647058824 | 0.07698267131574446 | 0.4445828375427921 | 0.8979395946443616 |
| 0.0269 | 0.07293796864349011 | 0.3599557451516902 | 0.06118119399783414 | 0.1828397917521003 | 0.6028933787407033 |
| -0.009910000000000002 | 0.02324730001830496 | 0.9779571561626823 | 0.07675886351931402 | 0.5313954068444727 | 0.9499119195296295 |
| 0.0636 | 0.05547201909200119 | 0.3182633308391677 | 0.05683301936089966 | 0.4677605532147335 | 0.6102849676955249 |
| 0.00155 | 0.07207578253706755 | 0.2102032657029534 | 0.05878584302753442 | 0.4211236677680427 | 0.6038672004336629 |

## Trailing 12 month Worskheet

| If you are midway through a year, and want to compute updated trailing twelve month numbers, this worksheet may help. You will need your most recent quartely financials (or 10Q) as well as your most recent annual (or 10K). |
|---|
|  |
| Revenues |
| Technology & Content |
| Operating income or EBIT |
| Interest expenses |
| Book value of equity |
| Book value of debt |
| Do you have operating lease commitments? |
| Cash and cross holdings |
| Non-operating assets  |
| Minority interests |
| Number of shares outstanding = |
| Current stock price = |
| Effective tax rate = |
| Marginal tax rate = |
| Lease commitments |
| Year 1 |
| Year 2 |
| Year 3 |
| Year 4 |
| Year 5 |
| Beyond year 5 |
| Current year's lease expense |
|  |
|  |
|  |
|  |
| G&A |
| Marketing Costs |
| Content Costs |
| Content Costs (Cash Flows) |

## Answer keys

| Yes/No | Book or Market Value | ERP choices | Cost of debt | Synthetic rating | Beta | Rating is | Region | Cost of Capital Approach | Reinvestment lag |
|---|---|---|---|---|---|---|---|---|---|
| Yes | B | Will input | Direct input | 1 | Direct input | Aaa/AAA | First Decile | I will input | 0 |
| No | V | Country of incorporation | Synthetic rating | 2 | Single Business(US) | Aa2/AA | First Quartile | Detailed | 1 |
|  |  | Operating countries | Actual rating |  | Single Business(Global) | A1/A+ | Median | Industry Average | 2 |
|  |  | Operating regions |  |  | Multibusiness(US) | A2/A | Third Quartile | Distribution | 3 |
|  |  |  |  |  | Multibusiness(Global) | A3/A- | Ninth Decile |  |  |
|  |  |  |  |  |  | Baa2/BBB |  |  |  |
|  |  |  |  |  |  | Ba1/BB+ |  |  |  |
|  |  |  |  |  |  | Ba2/BB |  |  |  |
|  |  |  |  |  |  | B1/B+ |  |  |  |
|  |  |  |  |  |  | B2/B |  |  |  |
|  |  |  |  |  |  | B3/B- |  |  |  |
|  |  |  |  |  |  | C2/C |  |  |  |
|  |  |  |  |  |  | Ca2/CC |  |  |  |
|  |  |  |  |  |  | Caa/CCC |  |  |  |
|  |  |  |  |  |  | D2/D |  |  |  |
