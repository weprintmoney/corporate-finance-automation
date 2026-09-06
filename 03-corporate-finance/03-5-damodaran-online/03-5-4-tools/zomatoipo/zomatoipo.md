---
title: "Zomatoipo"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/littlebook2/ZomatoIPO.xlsx
---

# Zomatoipo

Source: https://pages.stern.nyu.edu/~adamodar/pc/littlebook2/ZomatoIPO.xlsx

Sheets: Input sheet, Valuation output, Stories to Numbers, Diagnostics, Summary Sheet, Option value, Cost of capital worksheet, R& D converter, Operating lease converter, Country equity risk premiums, Synthetic rating, Industry Average Beta (US), Industry Average Beta (Global), Trailing 12 month, Answer keys

## Input sheet

| Date of valuation | 2021-07-01 00:00:00 | Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |
|---|---|---|
| Company name | Zomato | There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |
| Numbers from your base year below ( in consistent units) |  |  |
|  | This year | Last year |
| Country of incorporation | India |  |
| Industry (US) | Restaurant/Dining |  |
| Industry (Global) | Restaurant/Dining | Last 10K |
| Gross Order Value | 94828.7 | 112209 |
| Revenues | 19937.89 | 26047 |
| Operating income or EBIT | -4804.56 | 22762.08 |
| Interest expense | 100.82 | 126.36 |
| Book value of equity | 80987.17 | 7097.81 |
| Book value of debt | 1534.63 | 3260.76 |
| Do you have R&D expenses to capitalize? | No |  If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |
| Do you have operating lease commitments? | No | If you have operating leases, please enter your lease commitments in the lease worksheet below and I will convert to debt |
| Cash and Marketable Securities | 15332.029999999999 | 4710.16 |
| Cross holdings and other non-operating assets | 30627.67 | 104.76 |
| Minority interests | 57.09 | 65 |
| Offer Proceeds (staying in firm) | 90000 |  |
| Number of shares outstanding = | 6660.97 |  |
| Current stock price = | 70 |  |
| Effective tax rate = | 0.25 |  |
| Marginal tax rate = | 0.25 |  |
| The value drivers below: |  |  |
| Indian food delivery market in 2020 | 225000 |  |
| Growth rate for next year | 0.5 |  |
| Growth rate in years 2-5 | 0.3 |  |
| Market Share for Zomato in year 5 | 0.4 |  |
| Revenues as percent of GOV in future | 0.22 |  |
| Operating Margin for next year | -0.1 |  |
| Target pre-tax operating margin (EBIT as % of sales in year 10) = | 0.35 | Profitability Lever |
| Year of convergence | 8 | Speed of convergence level |
| Sales to capital ratio (next year) | 2.5 | Efficency of Growth Lever |
| Sales to capital ratio  (for years 2-5) = | 2.5 |  |
| Sales to capital ratio (for years 6-10) | 3 |  |
| Market numbers  |  |  |
| Riskfree rate | 0.0425 |  |
| Initial cost of capital = | 0.10254512690972693 |  |
| Other inputs |  |  |
| Do you have employee options outstanding? | Yes |  |
| Number of options outstanding = | 1075.1799999999998 |  |
| Average strike price = | 2 |  |
| Average maturity = | 5 |  |
| Standard deviation on stock price = | 0.5 |  |
| Default assumptions.  |  |  |
| In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%) |  |  |
| Do you want to override this assumption = | No | Mature companies generally see their risk levels approach the average |
| If yes, enter the cost of capital after year 10 = | 0.075 | Though some sectors, even in stable growth, may have higher risk. If you change your risk free rate after year 10 (see cell B57 & 58), you should incorporate the change into your stable cost of capital estimate. |
| I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time. |  |  |
| Do you want to override this assumption = | Yes | Mature companies find it difficult to generate returns that exceed the cost of capital |
| If yes, enter the return on capital you expect after year 10 | 0.12 | But there are significant exceptions among companies with long-lasting competitive advantages. |
| I will assume that your firm has no chance of failure over the foreseeable future. |  |  |
| Do you want to override this assumption = | Yes | Many young, growth companies fail, especially if they have trouble raising cash. Many distressed companies fail, because they have trouble making debt payments. |
| If yes, enter the probability of failure = | 0.1 | Tough to estimate but a key input. |
| What do you want to tie your proceeds in failure to? | V | B: Book value of capital, V= Estimated fair value for the company |
| Enter the distress proceeds as percentage of book or fair value | 0.5 | This can be zero, if the assets will be worth nothing if the firm fails. |
| I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year. If you override this assumption, I will leave the tax rate at your effective tax rate. |  |  |
| Do you want to override this assumption = | No |  |
| I will assume that you have no losses carried forward from prior years ( NOL) coming into the valuation. If you have a money losing company, you may want to override tis. |  |  |
| Do you want to override this assumption = | No | Check the financial statements. |
| If yes, enter the NOL that you are carrying over into year 1 | 731.4000000000001 | An NOL will shield your income from taxes, even after you start making money. |
| I will asssume that today's risk free rate will prevail in perpetuity. If you override this assumption, I will change the riskfree rate after year 10. |  |  |
| Do you want to override this assumption = | No | If yes, you will be asked to enter a normal risk free rate and your growth in perpetuity will be adjusted accordingly. |
| If yes, enter the riskfree rate after year 10 | 0.02 | Enter your estimate of what the riskfree rate (in your currency of choice) will be after year 10 |
| I will assume that the growth rate in perpetuity will be equal to the risk free rate. This allows for both valuation consistency and prevents "impossible" growth rates. |  |  |
| Do you want to override this assumption = | No | This is an option to let you use a negative growth rate in perpetuity or to even liquidate the firm. |
| If yes, enter the growth rate in perpetuity | -0.05 | This can be negative, if you feel the company will decline (and disappear) after growth is done. If you let it exceed the risk free rate, you are on your own in uncharted territory. |
| I have assumed that none of the cash is trapped (in foreign countries) and that there is no additional tax liability coming due and that cash is a neutral asset. |  |  |
| Do you want to override this assumption | No |  |
| If yes, enter trapped cash (if taxes) or entire balance (if mistrust) | 140000 | Cash that is trapped in foreign markets (and subject to additoinal tax) or cash that is being discounted by the market (because of management mistrust) |
| & Average tax rate of the foreign markets where the cash is trapped | 0.15 | Additional tax rate due on trapped cash or discount being applied to cash balance because of mistrust. |

## Valuation output

| Base year | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Terminal year |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.5 | 0.3 | 0.3 | 0.3 | 0.3 | 0.2485 | 0.19699999999999998 | 0.14549999999999996 | 0.09399999999999997 | 0.04249999999999998 | 0.0425 |
| 225000 | 337500 | 438750 | 570375 | 741487.5 | 963933.75 | 1203471.286875 | 1440555.1303893751 | 1650155.9018610292 | 1805270.5566359658 | 1881994.5552929942 | 1961979.3238929466 |
| 0.4214608888888889 | 0.4171687111111111 | 0.41287653333333335 | 0.40858435555555556 | 0.4042921777777778 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 |
| 94828.7 | 140794.44 | 181149.579 | 233046.3018 | 299777.59617000003 | 385573.5 | 481388.51475000003 | 576222.0521557501 | 660062.3607444117 | 722108.2226543864 | 752797.8221171978 | 784791.7295571787 |
| 0.2102516432261541 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 | 0.22 |
| 19937.89 | 30974.7768 | 39852.90738 | 51270.186396 | 65951.0711574 | 84826.17 | 105905.473245 | 126768.85147426503 | 145213.71936377056 | 158863.80898396502 | 165615.5208657835 | 172654.18050257931 |
| -0.24097635206132648 | -0.1 | 0.012500000000000011 | 0.06874999999999998 | 0.125 | 0.18125 | 0.20225591198466836 | 0.2761279559923342 | 0.35 | 0.35 | 0.35 | 0.35 |
| -4804.56 | -3097.47768 | 498.1613422500004 | 3524.825314724999 | 8243.883894675 | 15374.743312499999 | 21420.00807533537 | 35004.4238410846 | 50824.80177731969 | 55602.333144387754 | 57965.43230302422 | 60428.963175902754 |
| 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 |
| -4804.56 | -3097.47768 | 498.1613422500004 | 3293.448070481249 | 6182.91292100625 | 11531.057484375 | 16065.006056501526 | 26253.31788081345 | 38118.60133298977 | 41701.749858290816 | 43474.07422726817 | 45321.722381927066 |
|  | 4414.75472 | 3551.252231999999 | 4566.9116064 | 5872.353904560002 | 6291.699614199999 | 7026.434415000001 | 6954.45940975501 | 6148.289296501845 | 4550.029873398152 | 2250.5706272728276 | 16051.44334359917 |
|  | -7512.2324 | -3053.0908897499985 | -1273.463535918751 | 310.5590164462483 | 5239.357870175001 | 9038.571641501527 | 19298.85847105844 | 31970.312036487925 | 37151.71998489266 | 41223.50359999534 | 29270.279038327895 |
| 0 | 3097.47768 | 2599.3163377499995 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0.10254512690972693 | 0.10254512690972693 | 0.10254512690972693 | 0.10254512690972693 | 0.10254512690972693 | 0.09997610152778155 | 0.09740707614583617 | 0.09483805076389079 | 0.09226902538194541 | 0.08970000000000003 | 0.0897 |
|  | 0.906992353957297 | 0.8226351301369988 | 0.7461237731309239 | 0.676728557335517 | 0.6137876272078662 | 0.5580008750693426 | 0.5084720949942089 | 0.46442676580288517 | 0.4251944850678926 | 0.3901940764135932 |  |
|  | -6813.537347950275 | -2511.5798214095757 | -950.1614183643463 | 210.16415516720667 | 3215.8530352275734 | 5043.530885334796 | 9812.93099777582 | 14847.868620815138 | 15796.70644836297 | 16085.166913732617 |  |
| 29270.279038327895 |  |  |  |  |  |  |  |  |  |  |  |
| 0.0897 |  |  |  |  |  |  |  |  |  |  |  |
| 620133.0304730487 |  |  |  |  |  |  |  |  |  |  |  |
| 241972.2350789939 |  |  |  |  |  |  |  |  |  |  |  |
| 54736.94246869192 |  |  |  |  |  |  |  |  |  |  |  |
| 296709.1775476858 |  |  |  |  |  |  |  |  |  |  |  |
| 0.1 |  |  |  |  |  |  |  |  |  |  |  |
| 148354.5887738429 |  |  |  |  |  |  |  |  |  |  |  |
| 281873.71867030155 |  | 14835.458877384255 |  |  |  |  |  |  |  |  |  |
| 1534.63 |  |  |  |  |  |  |  |  |  |  |  |
| 57.09 |  |  |  |  |  |  |  |  |  |  |  |
| 15332.029999999999 |  |  |  |  |  |  |  |  |  |  |  |
| 90000 |  |  |  |  |  |  |  |  |  |  |  |
| 30627.67 |  |  |  |  |  |  |  |  |  |  |  |
| 416241.6986703015 |  |  |  |  |  |  |  |  |  |  |  |
| 73244.5257747911 |  |  |  |  |  |  |  |  |  |  |  |
| 342997.17289551045 |  |  |  |  |  |  |  |  |  |  |  |
| 7946.684285714286 |  |  |  |  |  |  |  |  |  |  |  |
| 43.16230022024591 |  |  |  |  |  |  |  |  |  |  |  |
| 70 |  |  |  |  |  |  |  |  |  |  |  |
| 1.621785670430175 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 2.5 | 2.5 | 2.5 | 2.5 | 3 | 3 | 3 | 3 | 3 | 3 |  |
| 67189.77 | 71604.52472 | 75155.776952 | 79722.6885584 | 85595.04246296 | 91886.74207716 | 98913.17649216 | 105867.63590191501 | 112015.92519841685 | 116565.955071815 | 118816.52569908783 |  |
| -0.07150731428311186 | -0.04325812778050375 | 0.006628383904116417 | 0.04131130209022829 | 0.07223447460385121 | 0.12549207016929637 | 0.16241522743711362 | 0.24798247034756504 | 0.3402962682803294 | 0.35775239719520874 | 0.3658924881995765 | 0.12 |

## Stories to Numbers

| Zomato | 2021-07-01 00:00:00 |
|---|---|
| The Story |  |
| Zomato will benefit as the Indian food delivery market grows, driven by overall economic growth and more digital access, and it will be one of a few (two or three) players who will dominate the market; there will be a near term COVID bouncecback effect. While Amazon Food remains the wild card, economies of scales will allow the company to generate high operating margins, and the company will continue to reinvest (acquisitions and technology) as it grows. The risk of failure is low, given the company's post-IPO cash balance and access to capital and its operating risk reflects its exposure to Indian country risk. |  |
| The Assumptions |  |
|  | Link to story |
| Indian Food Delivery | Indian food market rebounds in 2021 and grows to about $25 billion in year 10 |
| Market Share | Zomato is one of two or three lead players in Indian food delivery market |
| Revenues  as % of GOV |  |
| Revenues (a) | COVID rebound in 2021 + Growth in food delivery market in India long term |
| Operating margin (b) | Margins improve as growth wanes |
| Tax rate | Indian corporate tax rate over time |
| Reinvestment (c ) | Acquisitions & technology investments needed to sustain growth |
| Return on capital | Newworking benefits allow for high ROIC, near and long term. |
| Cost of capital (d) | Cost of capital reflects Indian country risk |
| The Cash Flows |  |
|  | FCFF |
| 1 | -7512.2324 |
| 2 | -3053.0908897499985 |
| 3 | -1273.463535918751 |
| 4 | 310.5590164462483 |
| 5 | 5239.357870175001 |
| 6 | 9038.571641501527 |
| 7 | 19298.85847105844 |
| 8 | 31970.312036487925 |
| 9 | 37151.71998489266 |
| 10 | 41223.50359999534 |
| Terminal year | 29270.279038327895 |
| The Value |  |
| Terminal value |  |
| PV(Terminal value) |  |
| PV (CF over next 10 years) |  |
| Value of operating assets = |  |
| Adjustment for distress | 0.1 |
|  - Debt & Minority Interests |  |
|  + Cash & Other Non-operating assets | 90000 |
| Value of equity |  |
|  - Value of equity options |  |
| Number of shares |  |
| Value per share | 70 |

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

## Summary Sheet

| Year | Revenues | Revenue Growth Rate | Pre-Tax Operating Margin | Pre-Tax Operating Income | NOL | Taxes | After-Tax Operating Income |
|---|---|---|---|---|---|---|---|
| Traling 12 month | 19937.89 |  | -0.24097635206132648 | -4804.56 | 0 | 0 | -4804.56 |
| 1 | 30974.7768 | 140794.44 | -0.1 | -3097.47768 | 3097.47768 | 0 | -3097.47768 |
| 2 | 39852.90738 | 0.28662452153650375 | 0.012500000000000011 | 498.1613422500004 | 2599.3163377499995 | 0 | 498.1613422500004 |
| 3 | 51270.186396 | 0.28648547286990933 | 0.06874999999999998 | 3524.825314724999 | 0 | 231.37724424374983 | 3293.448070481249 |
| 4 | 65951.0711574 | 0.28634350279142695 | 0.125 | 8243.883894675 | 0 | 2060.97097366875 | 6182.91292100625 |
| 5 | 84826.17 | 0.2861985182553344 | 0.18125 | 15374.743312499999 | 0 | 3843.685828124999 | 11531.057484375 |
| 6 | 105905.473245 | 0.24849999999999994 | 0.20225591198466836 | 21420.00807533537 | 0 | 5355.002018833842 | 16065.006056501526 |
| 7 | 126768.85147426503 | 0.19700000000000029 | 0.2761279559923342 | 35004.4238410846 | 0 | 8751.10596027115 | 26253.31788081345 |
| 8 | 145213.71936377056 | 0.14549999999999974 | 0.35 | 50824.80177731969 | 0 | 12706.200444329923 | 38118.60133298977 |
| 9 | 158863.80898396502 | 0.09400000000000008 | 0.35 | 55602.333144387754 | 0 | 13900.583286096939 | 41701.749858290816 |
| 10 | 165615.5208657835 | 0.04249999999999976 | 0.35 | 57965.43230302422 | 0 | 14491.358075756056 | 43474.07422726817 |
| Year | After-Tax Operating Income | Change in Revenues | Sales to Capital | Reinvestment | FCFF | Capital Invested | Implied ROC |
| Traling 12 month | -4804.56 |  |  |  |  | 67189.77 | -0.07150731428311186 |
| 1 | -3097.47768 | 11036.8868 | 2.5 | 4414.75472 | -7512.2324 | 71604.52472 | -0.04325812778050375 |
| 2 | 498.1613422500004 | 8878.130579999997 | 2.5 | 3551.252231999999 | -3053.0908897499985 | 75155.776952 | 0.006628383904116417 |
| 3 | 3293.448070481249 | 11417.279016 | 2.5 | 4566.9116064 | -1273.463535918751 | 79722.6885584 | 0.04131130209022829 |
| 4 | 6182.91292100625 | 14680.884761400004 | 2.5 | 5872.353904560002 | 310.5590164462483 | 85595.04246296 | 0.07223447460385121 |
| 5 | 11531.057484375 | 18875.098842599997 | 3 | 6291.699614199999 | 5239.357870175001 | 91886.74207716 | 0.12549207016929637 |
| 6 | 16065.006056501526 | 21079.303245000003 | 3 | 7026.434415000001 | 9038.571641501527 | 98913.17649216 | 0.16241522743711362 |
| 7 | 26253.31788081345 | 20863.37822926503 | 3 | 6954.45940975501 | 19298.85847105844 | 105867.63590191501 | 0.24798247034756504 |
| 8 | 38118.60133298977 | 18444.867889505535 | 3 | 6148.289296501845 | 31970.312036487925 | 112015.92519841685 | 0.3402962682803294 |
| 9 | 41701.749858290816 | 13650.089620194456 | 3 | 4550.029873398152 | 37151.71998489266 | 116565.955071815 | 0.35775239719520874 |
| 10 | 43474.07422726817 | 6751.711881818483 | 3 | 2250.5706272728276 | 41223.50359999534 | 118816.52569908783 | 0.3658924881995765 |
| Year | Beta | Cost of Equity | Pre-Tax Cost of Debt | Tax Savings | After-Tax Cost of Debt | Debt Ratio | Cost of Capital |
| 1 |  |  |  |  |  |  | 0.10254512690972693 |
| 2 |  |  |  |  |  |  | 0.10254512690972693 |
| 3 |  |  |  |  |  |  | 0.10254512690972693 |
| 4 |  |  |  |  |  |  | 0.10254512690972693 |
| 5 |  |  |  |  |  |  | 0.10254512690972693 |
| 6 |  |  |  |  |  |  | 0.09997610152778155 |
| 7 |  |  |  |  |  |  | 0.09740707614583617 |
| 8 |  |  |  |  |  |  | 0.09483805076389079 |
| 9 |  |  |  |  |  |  | 0.09226902538194541 |
| 10 |  |  |  |  |  |  | 0.08970000000000003 |
| Year | Cost of Capital | Cumulated Cost of Capital | FCFF | Terminal Value | Present Value |  |  |
| 1 | 0.10254512690972693 | 1.1025451269097268 | -7512.2324 |  | -6813.537347950275 |  |  |
| 2 | 0.10254512690972693 | 1.2156057568723857 | -3053.0908897499985 |  | -2511.5798214095757 |  |  |
| 3 | 0.10254512690972693 | 1.340260203483059 | -1273.463535918751 |  | -950.1614183643464 |  |  |
| 4 | 0.10254512690972693 | 1.4776973561412856 | 310.5590164462483 |  | 210.16415516720673 |  |  |
| 5 | 0.10254512690972693 | 1.6292280190609616 | 5239.357870175001 |  | 3215.853035227574 |  |  |
| 6 | 0.09997610152778155 | 1.7921118849065067 | 9038.571641501527 |  | 5043.530885334798 |  |  |
| 7 | 0.09740707614583617 | 1.9666762637414528 | 19298.85847105844 |  | 9812.930997775822 |  |  |
| 8 | 0.09483805076389079 | 2.153192007078304 | 31970.312036487925 |  | 14847.868620815143 |  |  |
| 9 | 0.09226902538194541 | 2.351864935031614 | 37151.71998489266 |  | 15796.706448362973 |  |  |
| 10 | 0.08970000000000003 | 2.56282721970395 | 41223.50359999534 | 620133.0304730487 | 16085.16691373262 |  |  |
| Value of operating assets = |  |  |  |  | 54736.94246869194 |  |  |

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

| Mature Market ERP + | 0.0472 | Updated January 1, 2021 |
|---|---|---|
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.0043848898169671765 |
| Albania | B1 | 0.0397829094303022 |
| Algeria | NR | 0.07956581886060442 |
| Andorra (Principality of) | Caa1 | 0.06625169887090407 |
| Angola | Caa1 | 0.06625169887090407 |
| Argentina | Ca | 0.10603460830120626 |
| Armenia | Ba3 | 0.03181038249036188 |
| Aruba | Baa1 | 0.014111372683694367 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.0035079118535737406 |
| Azerbaijan | Ba2 | 0.02654851471000126 |
| Bahamas | Ba2 | 0.02654851471000126 |
| Bahrain | B2 | 0.04863241433363595 |
| Bangladesh | Ba3 | 0.03181038249036188 |
| Barbados | Caa1 | 0.06625169887090407 |
| Belarus | B3 | 0.0574819192369697 |
| Belgium | Aa3 | 0.005341593049760015 |
| Belize | Caa3 | 0.08833559849453876 |
| Benin | B2 | 0.04863241433363595 |
| Bermuda | A2 | 0.0074941753235439005 |
| Bolivia | B2 | 0.04863241433363595 |
| Bosnia and Herzegovina | B3 | 0.0574819192369697 |
| Botswana | A2 | 0.0074941753235439005 |
| Brazil | Ba2 | 0.02654851471000126 |
| British Virgin Islands | NR | 0.0302 |
| Brunei | NR | 0.007494175323543901 |
| Bulgaria | Baa1 | 0.014111372683694367 |
| Burkina Faso | B2 | 0.04863241433363595 |
| Cambodia | B2 | 0.04863241433363595 |
| Cameroon | B2 | 0.04863241433363595 |
| Canada | Aaa | 0 |
| Cape Verde | B2 | 0.04863241433363595 |
| Cayman Islands | Aa3 | 0.005341593049760015 |
| Chile | A1 | 0.0062185710131534505 |
| China | A1 | 0.0062185710131534505 |
| Colombia | Baa2 | 0.016822031843274077 |
| Congo (Democratic Republic of) | Caa1 | 0.06625169887090407 |
| Congo (Republic of) | Caa2 | 0.0795658188606044 |
| Cook Islands | B1 | 0.0397829094303022 |
| Costa Rica | B2 | 0.04863241433363595 |
| Croatia | Ba1 | 0.02208389962363469 |
| Cuba | Caa2 | 0.0795658188606044 |
| Curaçao | A3 | 0.010603460830120627 |
| Cyprus | Ba2 | 0.02654851471000126 |
| Czech Republic | Aa3 | 0.005341593049760015 |
| Denmark | Aaa | 0 |
| Dominican Republic | Ba3 | 0.03181038249036188 |
| Ecuador | Caa3 | 0.08833559849453876 |
| Egypt | B2 | 0.04863241433363595 |
| El Salvador | B3 | 0.0574819192369697 |
| Estonia | A1 | 0.0062185710131534505 |
| Ethiopia | B2 | 0.04863241433363595 |
| Fiji | Ba3 | 0.03181038249036188 |
| Finland | Aa1 | 0.0035079118535737406 |
| France | Aa2 | 0.0043848898169671765 |
| Gabon | Caa1 | 0.06625169887090407 |
| Gambia | NR | 0.05748191923696969 |
| Georgia | Ba2 | 0.02654851471000126 |
| Germany | Aaa | 0 |
| Ghana | B3 | 0.0574819192369697 |
| Greece | Ba3 | 0.03181038249036188 |
| Guatemala | Ba1 | 0.02208389962363469 |
| Guernsey | Aaa | 0 |
| Guinea | NR | 0.10603460830120626 |
| Guinea-Bissau | NR | 0.06625169887090408 |
| Guyana | NR | 0.04863241433363596 |
| Haiti | NR | 0.10603460830120626 |
| Honduras | B1 | 0.0397829094303022 |
| Hong Kong | Aa3 | 0.005341593049760015 |
| Hungary | Baa3 | 0.019452965733454383 |
| Iceland | A2 | 0.0074941753235439005 |
| India | Baa3 | 0.019452965733454383 |
| Indonesia | Baa2 | 0.016822031843274077 |
| Iran | NR | 0.07956581886060442 |
| Iraq | Caa1 | 0.06625169887090407 |
| Ireland | A2 | 0.0074941753235439005 |
| Isle of Man | Aa3 | 0.005341593049760015 |
| Israel | A1 | 0.0062185710131534505 |
| Italy | Baa3 | 0.019452965733454383 |
| Ivory Coast | Ba3 | 0.03181038249036188 |
| Jamaica | B2 | 0.04863241433363595 |
| Japan | A1 | 0.0062185710131534505 |
| Jersey | Aaa | 0 |
| Jordan | B1 | 0.0397829094303022 |
| Kazakhstan | Baa3 | 0.019452965733454383 |
| Kenya | B2 | 0.04863241433363595 |
| Korea, D.P.R. | NR | 0.10603460830120626 |
| Kuwait | A1 | 0.0062185710131534505 |
| Kyrgyzstan | B2 | 0.04863241433363595 |
| Laos | Caa2 | 0.010603460830120627 |
| Latvia | A3 | 0.010603460830120627 |
| Lebanon | C | 0.175 |
| Liberia | NR | 0.10603460830120626 |
| Libya | NR | 0.07956581886060442 |
| Liechtenstein | Aaa | 0 |
| Lithuania | A3 | 0.010603460830120627 |
| Luxembourg | Aaa | 0 |
| Macao | Aa3 | 0.005341593049760015 |
| Macedonia | Ba3 | 0.03181038249036188 |
| Madagascar | NR | 0.05748191923696969 |
| Malawi | NR | 0.07956581886060442 |
| Malaysia | A3 | 0.010603460830120627 |
| Mali | Caa1 | 0.06625169887090407 |
| Malta | A2 | 0.0074941753235439005 |
| Mauritius | Baa1 | 0.014111372683694367 |
| Mexico | Baa1 | 0.014111372683694367 |
| Moldova | B3 | 0.0574819192369697 |
| Mongolia | B3 | 0.0574819192369697 |
| Montenegro | B1 | 0.0397829094303022 |
| Montserrat | Baa3 | 0.019452965733454383 |
| Morocco | Ba1 | 0.02208389962363469 |
| Mozambique | Caa2 | 0.0795658188606044 |
| Myanmar | NR | 0.05748191923696969 |
| Namibia | Ba3 | 0.03181038249036188 |
| Netherlands | Aaa | 0 |
| New Zealand | Aaa | 0 |
| Nicaragua | B3 | 0.0574819192369697 |
| Niger | B3 | 0.0574819192369697 |
| Nigeria | B2 | 0.04863241433363595 |
| Norway | Aaa | 0 |
| Oman | Ba3 | 0.03181038249036188 |
| Pakistan | B3 | 0.0574819192369697 |
| Panama | Baa1 | 0.014111372683694367 |
| Papua New Guinea | B2 | 0.04863241433363595 |
| Paraguay | Ba1 | 0.02208389962363469 |
| Peru | A3 | 0.010603460830120627 |
| Philippines | Baa2 | 0.016822031843274077 |
| Poland | A2 | 0.0074941753235439005 |
| Portugal | Baa3 | 0.019452965733454383 |
| Qatar | Aa3 | 0.005341593049760015 |
| Ras Al Khaimah (Emirate of) | Aaa | 0 |
| Romania | Baa3 | 0.019452965733454383 |
| Russia | Baa3 | 0.019452965733454383 |
| Rwanda | B2 | 0.04863241433363595 |
| Saint Lucia | NR | 0.0302 |
| Saudi Arabia | A1 | 0.0062185710131534505 |
| Senegal | Ba3 | 0.03181038249036188 |
| Serbia | Ba3 | 0.03181038249036188 |
| Sharjah | Baa2 | 0.016822031843274077 |
| Sierra Leone | NR | 0.07956581886060442 |
| Singapore | Aaa | 0 |
| Slovakia | A2 | 0.0074941753235439005 |
| Slovenia | A3 | 0.010603460830120627 |
| Solomon Islands | B3 | 0.0574819192369697 |
| Somalia | NR | 0.10603460830120626 |
| South Africa | Ba2 | 0.02654851471000126 |
| South Korea | Aa2 | 0.0043848898169671765 |
| Spain | Baa1 | 0.014111372683694367 |
| Sri Lanka | Caa1 | 0.06625169887090407 |
| St. Maarten | Baa3 | 0.019452965733454383 |
| St. Vincent & the Grenadines | B3 | 0.0574819192369697 |
| Sudan | NR | 0.175 |
| Suriname | Caa3 | 0.08833559849453876 |
| Swaziland | B3 | 0.0574819192369697 |
| Sweden | Aaa | 0 |
| Switzerland | Aaa | 0 |
| Syria | NR | 0.175 |
| Taiwan | Aa3 | 0.005341593049760015 |
| Tajikistan | B3 | 0.0574819192369697 |
| Tanzania | B2 | 0.04863241433363595 |
| Thailand | Baa1 | 0.014111372683694367 |
| Togo | B3 | 0.0574819192369697 |
| Trinidad and Tobago | Ba1 | 0.02208389962363469 |
| Tunisia | B2 | 0.04863241433363595 |
| Turkey | B2 | 0.04863241433363595 |
| Turks and Caicos Islands | Baa1 | 0.014111372683694367 |
| Uganda | B2 | 0.04863241433363595 |
| Ukraine | B3 | 0.0574819192369697 |
| United Arab Emirates | Aa2 | 0.0043848898169671765 |
| United Kingdom | Aa3 | 0.005341593049760015 |
| United States | Aaa | 0 |
| Uruguay | B1 | 0.0397829094303022 |
| Venezuela | C | 0.175 |
| Vietnam | Ba3 | 0.03181038249036188 |
| Yemen | NR | 0.175 |
| Zambia | Ca | 0.10603460830120626 |
| Zimbabwe | NR | 0.10603460830120626 |
|  | ERP | Default Spread |
| Africa | 0.09664194736704565 | 0.04511442352024405 |
| Asia | 0.057467692442688456 | 0.00936900849357519 |
| Australia & New Zealand | 0.04723268292122549 | 2.9822270937258018e-05 |
| Caribbean | 0.10031257462365305 | 0.048463770410045445 |
| Central and South America | 0.08710043172107099 | 0.036408051688206385 |
| Eastern Europe & Russia | 0.06798054108360041 | 0.0189616748803517 |
| Middle East | 0.06250178543397211 | 0.01396246032866099 |
| North America | 0.0472 | 0 |
| Western Europe | 0.055597475094507666 | 0.007662466146445361 |
| Global | 0.057630323227580695 | 0.009517391170547215 |

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

## Industry Average Beta (US)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 61 | 0.08314599999999998 | 0.09978982911471537 | 0.5151189951700217 | 0.21473754602683312 | 0.7744094010040972 | 1.0763167747709843 | 0.060102151769190454 | 0.5773635026347075 | 0.029980000000000003 | 0.4366235123495564 | 0.0434158193811354 | 5.16893366314677 | 1.8279748463952663 | 8.860314159035372 | 16.081323674363535 | 5.729581759423581 | 45.375202628511474 | -0.005745858907579926 | 0.01749996930714576 | -0.01911835966362643 | -0.31670613154939664 | 0.02933270644878155 | 9.128474462304553 | 9.128474462304553 | 0.10312282984536096 |
| Aerospace/Defense | 72 | 0.052835581395348837 | 0.07555824105542643 | 0.1911487501301388 | 0.2462174246147118 | 0.9124112469458897 | 1.0654116800938749 | 0.0595874313004309 | 0.34892933167879187 | 0.0258 | 0.24839853323369193 | 0.04946433874116383 | 2.605987875982208 | 2.011767585240377 | 12.152653123863544 | 20.31000758159399 | 4.436924916352297 | 107.38396177092393 | 0.43564008525480985 | 0.027682925662515925 | -0.013339522457738126 | 0.36932242726066256 | 0.08543188803755926 | 1.205515919077203 | 1.205515919077203 | 0.0789221212923313 |
| Air Transport | 17 | -0.06822916666666667 | -0.1899061389769127 | -0.16065422687831812 | 0.8875778816199377 | 0.9196221669289372 | 1.6081637004838845 | 0.08520532666283935 | 0.4615078958344 | 0.029980000000000003 | 0.6173848737990707 | 0.04611256173113587 | 0.8832377145018504 | 1.972801574870317 | 34.42544764696492 | NA | 3.224149710847368 | 13.467519539284243 | 0.017044401390725925 | 0.11832919205455525 | 0.01799000360057866 | NA | -0.4702685391404543 | 0.0008642533936651585 | 0.0008642533936651375 | -0.1935180472021863 |
| Apparel | 51 | -0.03555310344827586 | 0.054872250559461794 | 0.07542256068257507 | 0.3140990793511618 | 0.9413632904562012 | 1.0982186127658942 | 0.06113591852255021 | 0.4784359487657423 | 0.029980000000000003 | 0.2825836395818197 | 0.05004436414297434 | 1.3391307059586217 | 2.0258437620692398 | 14.688666444402248 | 33.97625454492586 | 4.111694101411789 | 22.761750232250616 | 0.24962264547366317 | 0.025172142610807156 | 0.001553138806358238 | -1.4672262647921706 | -0.08188096631907989 | 0.003245269154063234 | 0.0032452691540632017 | 0.05913857501245369 |
| Auto & Truck | 19 | 0.12191666666666669 | 0.019333508605592183 | 0.011709090822045768 | 0.28480567682019586 | 1.0499991719428035 | 1.2828255283085925 | 0.06984936493616556 | 0.4523696418680257 | 0.029980000000000003 | 0.2788406990461426 | 0.05647505942434049 | 0.7427041662869365 | 3.5828402796043126 | 45.72989527510934 | 177.7600106028954 | 7.578761704122104 | 261.55986156714147 | -0.06939140210297645 | 0.10244391023130034 | 0.046115116875564834 | 1.8440271694624273 | 0.044885246411493 | 0.6457993434631338 | 0.6457993434631338 | 0.01733279303568889 |
| Auto Parts | 52 | 0.040210357142857145 | 0.04009886276210231 | 0.06458653900492817 | 0.32645234056176436 | 1.0938111386841938 | 1.2034979086361026 | 0.06610510128762404 | 0.43164927127684694 | 0.029980000000000003 | 0.19595454549627142 | 0.05744004981982678 | 1.8223436646890339 | 1.5973947047834025 | 10.069787934462136 | 23.28239703812532 | 4.775601035002602 | 55.56467095160826 | 0.13841228389990334 | 0.03711280345065762 | 0.02087451364490318 | 0.3006946507706782 | -0.1431069277976672 | 0.004182244008432757 | 0.004182244008432812 | 0.03850709823598535 |
| Bank (Money Center) | 7 | -0.007768333333333333 | 0 | -0.00013307855085708446 | 0.14043540086905243 | 0.5984792904660569 | 0.8277079354664856 | 0.04836781455401812 | 0.21588164482905958 | 0.019200000000000002 | 0.6837368986713982 | 0.024880211407118772 | 0.14283525600359426 | 5.316984564676387 | NA | NA | 1.0031245608712027 | 14.862679952459837 | NA | 0.010567244136700984 | 0.010567244136700984 | NA | 0.0741320864778279 | 0.4695006870349304 | 0.4695006870349304 | -0.0011112733946249372 |
| Banks (Regional) | 598 | 0.08824597189695547 | 0 | -0.0008105591329961938 | 0.18951592738394935 | 0.6001085940658732 | 0.6448746960107257 | 0.03973808565170625 | 0.1948333710409514 | 0.019200000000000002 | 0.37983637553849753 | 0.029967901866471358 | 0.23930540909038422 | 4.472711399045109 | NA | NA | 1.0754982433128295 | 15.385193908763318 | NA | 0.043659040048152624 | 0.020083498513917483 | NA | 0.08216376124038208 | 0.4435224690419324 | 0.4435224690419324 | -0.004052542383221588 |
| Beverage (Alcoholic) | 23 | 0.1439 | 0.2387432428677387 | 0.14430150625179838 | 0.18356492728273902 | 0.6760305928323548 | 0.778263875057117 | 0.04603405490269592 | 0.37007991589511724 | 0.0258 | 0.18966662702601325 | 0.040875112234379216 | 0.6393400430448049 | 5.299531951321307 | 17.606214861939037 | 22.212937620161576 | 3.450923356617885 | 32.3896191058676 | 0.1525471369424097 | 0.06379224476796506 | 0.04490660248504295 | 0.24109615176253643 | 0.10103219726606896 | 0.415798340970307 | 0.415798340970307 | 0.23840844026504482 |
| Beverage (Soft) | 41 | 0.27075 | 0.19977131401368578 | 0.2673628021205749 | 0.18600628389948448 | 0.7074545270732899 | 0.7912608446043524 | 0.04664751186532544 | 0.4969504572395075 | 0.029980000000000003 | 0.1776358852166161 | 0.042248872204295476 | 1.3749583854286462 | 5.075068917147974 | 20.73500011735879 | 25.222526693198947 | 8.496343773435537 | 116.71720199086498 | -0.09544501723027882 | 0.05416471074329389 | 0.07406171182308426 | 0.3700889850351279 | 0.2885724626678179 | 0.7419292283670309 | 0.7419292283670309 | 0.2011283037932287 |
| Broadcasting | 29 | 0.05798299999999999 | 0.1929505932007099 | 0.16921739618580592 | 0.2316077026030292 | 0.653360936474274 | 1.1290399914200455 | 0.06259068759502615 | 0.45557616657732153 | 0.029980000000000003 | 0.5489775443996067 | 0.04024439876702893 | 0.9799459986927346 | 2.0808035893696673 | 7.843594381434588 | 10.931193344849747 | 1.5827116637449947 | 12.419936016946153 | 0.15711742011636806 | 0.027447171351973422 | -0.010518597030448126 | 1.1105642514742904 | 0.002385020644630917 | 0.0016973796349178008 | 0.0016973796349177839 | 0.19029743526881368 |
| Brokerage & Investment Banking | 39 | 0.09514347826086957 | 0.004212077281518308 | -2.8929962113133283e-05 | 0.22176459343610108 | 0.5769420165866951 | 1.1318381741280126 | 0.06272276181884219 | 0.3590279319865953 | 0.0258 | 0.6863989735519761 | 0.03259756075592175 | 0.21596489089219734 | 4.9306724537536955 | NA | NA | 1.5165540056877012 | 82.1983554242335 | NA | 0.052392768488402484 | 0.027448227056769928 | NA | 0.12076092974514126 | 0.20841894732278166 | 0.20841894732278166 | -0.0001497195846546239 |
| Building Materials | 42 | 0.07473275862068965 | 0.10803949730457793 | 0.2416569439389175 | 0.26259827271827774 | 0.9703551760346607 | 1.0884900729483686 | 0.060676731443163004 | 0.3399320710459472 | 0.0258 | 0.20816381881187787 | 0.051966588676434354 | 2.5924572788089524 | 1.9953151010184944 | 13.271107257463079 | 18.167058935351683 | 4.976990611230132 | 25.63409712027883 | 0.15453419984060132 | 0.024433610353444768 | 0.004527888246303807 | -0.024613641395462703 | 0.20538521259637507 | 0.21488040227325825 | 0.21488040227325822 | 0.10983107146900138 |
| Business & Consumer Services | 169 | 0.07533364864864864 | 0.08879414946761108 | 0.18329932580841857 | 0.23839807268309032 | 0.8300209186877809 | 0.9267932361238046 | 0.05304464074504357 | 0.4564535314466953 | 0.029980000000000003 | 0.1981885854997205 | 0.04686923489653813 | 2.157163239010289 | 2.9656653719133295 | 17.396962450101594 | 31.207264566605247 | 5.849457813011957 | 44.22061660781585 | 0.1383677881159181 | 0.03136518992428987 | 0.003445090302082048 | -0.11507975896192031 | 0.06809072735062517 | 0.6586916494255654 | 0.6586916494255654 | 0.09175394666398484 |
| Cable TV | 13 | 0.06698749999999999 | 0.1815182558471984 | 0.1108695566443063 | 0.2232749536475076 | 0.7005089695981953 | 0.9429659094015693 | 0.05380799092375407 | 0.32015889451441987 | 0.0258 | 0.34194704307327883 | 0.04184873814290468 | 0.7569964588490863 | 3.8522973077997342 | 11.11066035269977 | 20.197523407169026 | 3.1267555932444693 | 63.6766581402262 | -0.013478658831321332 | 0.10944094488998773 | -0.0174479403422238 | -0.1500927287320319 | 0.11465857561738993 | 0.2620469354048315 | 0.2620469354048315 | 0.1807427802346405 |
| Chemical (Basic) | 48 | 0.22507260869565218 | 0.07212579984954545 | 0.09526127058726884 | 0.0911707592257123 | 0.7617748033516681 | 0.9934776101041584 | 0.056192143196916275 | 0.48059008560792 | 0.029980000000000003 | 0.35532754282219436 | 0.04400201243452398 | 1.3495744099697256 | 1.5174120796495583 | 10.009800017612704 | 20.702463001148864 | 2.9613466941521587 | 45.863876676003365 | 0.15781685360764552 | 0.06329380354930282 | 0.031644256342847926 | 0.18240181383069348 | -0.018172614575978987 | 0.0043914837186071155 | 0.004391483718607092 | 0.0727597699601162 |
| Chemical (Diversified) | 5 | 0.28994 | 0.05812700689721961 | 0.05925802837332307 | 0.0570409982174688 | 1.0360679957510837 | 1.3627228737800379 | 0.0736205196424178 | 0.3616124741436054 | 0.0258 | 0.36748841144372296 | 0.05348710857049536 | 1.031930960947973 | 1.7193508613762196 | 13.381341293177154 | 29.250566929834815 | 2.1784653458416967 | 17.186064480100946 | 0.17676019324724168 | 0.05074313834085399 | 0.023919844159355344 | -0.6879074942117647 | 0.13253487594391739 | 0.5184435712212837 | 0.5184435712212837 | 0.05815571575313176 |
| Chemical (Specialty) | 97 | 0.05935418181818182 | 0.1206548383139212 | 0.11841392418279365 | 0.18168903732029262 | 0.8182123963069228 | 0.9265920088277176 | 0.05303514281666827 | 0.38541268779569865 | 0.0258 | 0.20225162151176118 | 0.04611790622444179 | 1.039150967937543 | 3.27348697881494 | 15.557856524721306 | 26.532549641016292 | 3.0972111715996866 | 58.86459210562928 | 0.21288350405516016 | 0.06371648495796166 | 0.023084996958236067 | 0.10485662262283377 | 0.02499996726894384 | 1.6368906543614743 | 1.6368906543614743 | 0.12183987826365998 |
| Coal & Related Energy | 29 | -0.14184545454545455 | -0.08702143368658297 | -0.07496374233834217 | 0 | 0.5621765173293861 | 0.8276705451096317 | 0.04836604972917462 | 0.4227402783807622 | 0.029980000000000003 | 0.48620323960370054 | 0.03549107204403906 | 0.8701923475250947 | 1.0829349201864724 | 5.785229553794515 | NA | 1.3578938055185275 | 37.68038023665884 | 0.07745527015549279 | 0.11286931613161091 | -0.07187800396364986 | NA | -0.4166384657129265 | 0.022375830881551706 | 0.022375830881551706 | -0.08614617509743197 |
| Computer Services | 116 | 0.09404 | 0.07578777390338884 | 0.2298022219858635 | 0.12935124662396041 | 0.9401944658459049 | 1.1172533064231442 | 0.06203435606317241 | 0.4589086089029444 | 0.029980000000000003 | 0.28441649812649367 | 0.05061533057625046 | 3.029833578595018 | 1.4323282243264928 | 10.70329441764578 | 17.955357866981824 | 4.000981993951046 | 27.860284729188052 | 0.12085695378067635 | 0.018050529500291616 | -0.0013398434376508724 | -0.16577062867375225 | 0.13499616893510502 | 0.755715755184985 | 0.755715755184985 | 0.08021523074969895 |
| Computers/Peripherals | 52 | 0.04061 | 0.15552039250702068 | 0.27816937415419485 | 0.14173391130511429 | 1.1394194094100192 | 1.1840744332992201 | 0.06518831325172318 | 0.42866445573502415 | 0.029980000000000003 | 0.08554834353119962 | 0.061483820752963034 | 1.8063509746701698 | 5.140639765434694 | 24.76341804425069 | 32.891802691131986 | 22.895969862404975 | 27.254643581045862 | -0.09083115851266192 | 0.0271589677736691 | 0.0017043799815278755 | -0.0024432574778906627 | 0.5053070007659138 | 0.2683230097870919 | 0.2683230097870919 | 0.15976104070516475 |
| Construction Supplies | 46 | 0.03502444444444444 | 0.09411044708774612 | 0.09932761824016942 | 0.22986853036142532 | 0.8722151255893847 | 1.0210954372727519 | 0.05749570463927389 | 0.3339082351055017 | 0.0258 | 0.258047889146616 | 0.047519133366299336 | 1.206776267166916 | 2.265331047669523 | 15.233753921075373 | 23.470484102110117 | 3.820222366541409 | 108.39709320846305 | 0.1723074882003061 | 0.052131428478764265 | 0.01963238854994992 | -0.08257774157481017 | 0.1320365231919894 | 0.4984597631107452 | 0.49845976311074525 | 0.09247820870969517 |
| Diversified | 29 | 0.005076363636363639 | 0.18064192537411194 | 0.13444721876605892 | 0.20759642859229738 | 0.8929236712420557 | 1.0248022870265143 | 0.05767066794765148 | 0.2993738242593451 | 0.0258 | 0.22921378752881652 | 0.04876876819237129 | 0.7927492409564074 | 2.797346566325185 | 11.373562877617585 | 15.120913165750846 | 1.8571825941414872 | 27.98364258478868 | 0.01483491445574776 | 0.050773905367239976 | 0.02969539203929677 | 0.2048576773074839 | 0.10620755186982106 | 0.1432137587176341 | 0.1432137587176341 | 0.18142791563042543 |
| Drugs (Biotechnology) | 547 | 0.32639857142857154 | 0.09544135407770715 | 0.06219168731196901 | 0.11951101190106696 | 0.8514961827629022 | 0.88621166971942 | 0.05112919081075662 | 0.501020020931708 | 0.029980000000000003 | 0.1341972536842995 | 0.04720475439663493 | 0.48336474338597796 | 8.734440588362972 | 14.395456267958144 | 57.62803183258693 | 7.180632724004509 | 480.18431697399177 | 0.13136172945902347 | 0.035629635456688805 | 0.37648897569690665 | 7.215486710009989 | -0.011878403785774745 | 0.0012584434526538685 | 0.0012584434526539123 | 0.1291522149779662 |
| Drugs (Pharmaceutical) | 287 | 0.32655375 | 0.24020052440609022 | 0.2031087214884036 | 0.16298183314653755 | 0.8372785027179765 | 0.9082184036647888 | 0.05216790865297803 | 0.5545237555574154 | 0.029980000000000003 | 0.1538384177716649 | 0.04750929543564714 | 0.8148626332310698 | 5.554598329200359 | 14.320361585486834 | 22.26771629288338 | 5.042337225154573 | 34.542058049164375 | 0.2622562276521094 | 0.05005383316952787 | 0.0973906129719695 | 0.48917071797569545 | 0.18978925035861566 | 0.6085526782221004 | 0.6085526782221004 | 0.2537697988195733 |
| Education | 38 | 0.010088888888888892 | 0.09261346896693554 | 0.09889168096460405 | 0.16654618048728848 | 1.0706243737868801 | 1.1476809803615506 | 0.06347054227306519 | 0.5572674495767506 | 0.029980000000000003 | 0.19570414695886867 | 0.055332157478351775 | 1.1668784652111823 | 2.8063477998163817 | 14.427941847430578 | 31.20589851999431 | 2.917435064171115 | 26.631329737537396 | 0.07471452593540345 | 0.03875434754966314 | 0.026957645691001734 | 0.614076239086715 | -0.05662813099300916 | 0.0005875310487758168 | 0.0005875310487758467 | 0.08824983359548152 |
| Electrical Equipment | 122 | 0.042116111111111104 | 0.1260196090138315 | 0.22121527249320072 | 0.17212659415707204 | 1.0013558595552174 | 1.0590362036719883 | 0.059286508813317845 | 0.5511942445541246 | 0.029980000000000003 | 0.133074214836378 | 0.054309385623975644 | 1.803380336617907 | 3.655558696261214 | 15.957574454786183 | 22.8282656767188 | 6.275090002935122 | 106.0185982870089 | 0.20995663482744578 | 0.03786673679915287 | 0.04492046104295457 | 0.36521953697919074 | 0.17667213707166918 | 0.4354706417572364 | 0.4354706417572364 | 0.12836155649720854 |
| Electronics (Consumer & Office) | 22 | 0.016941666666666667 | 0.019904348412680198 | 0.04660749238558445 | 0.11280558789289871 | 1.0108246814095976 | 0.9553526613630773 | 0.05439264561633725 | 0.549089075674876 | 0.029980000000000003 | 0.08678348362284845 | 0.05157155359876793 | 1.8201553312722258 | 1.316628884965371 | 18.961147120687322 | 59.51841853000027 | 4.263036545767564 | 14.621502322457888 | 0.13255100340049722 | 0.016756066198075428 | 0.009743146441601932 | -1.1244550392272765 | -0.04885721052787399 | 0 | 0 | 0.025820612218617388 |
| Electronics (General) | 157 | 0.02877239130434783 | 0.07467215532888848 | 0.110846132849151 | 0.1984947191787583 | 0.8582111004966717 | 0.8852671542153301 | 0.05108460967896358 | 0.4386506757631673 | 0.029980000000000003 | 0.11881317128022098 | 0.047615358978129796 | 1.489769744874309 | 2.543668038136409 | 17.51783625412998 | 32.12076712538554 | 4.141084396122947 | 69.76193685004223 | 0.2051509990360154 | 0.04194668977772201 | 0.04245064113775834 | 0.5996447700371407 | 0.06668520372973948 | 0.4148041192349626 | 0.4148041192349625 | 0.07903472733366322 |
| Engineering/Construction | 61 | 0.03570034482758622 | 0.04103267783010694 | 0.1485004333970936 | 0.21894983014970723 | 0.9556328465645647 | 1.0564199824615637 | 0.0591630231721858 | 0.42042611788262696 | 0.029980000000000003 | 0.22018691156817488 | 0.050954978455299976 | 3.796458327447753 | 0.8994726401457801 | 10.853099629722484 | 19.79548685881852 | 2.3182244883002365 | 34.52489960977317 | 0.1793938318792594 | 0.016956216288295495 | 0.10319245357384162 | 2.8375145355622444 | 0.02536909816371401 | 0.5278823677154549 | 0.5278823677154549 | 0.04313202473857852 |
| Entertainment | 118 | 0.06353703703703703 | 0.07440800483281292 | 0.07964578595907326 | 0.06731279068796499 | 0.8387564304949311 | 0.8828171901910933 | 0.0509689713770196 | 0.6806217937013402 | 0.040925 | 0.13191242879076623 | 0.04818644735794123 | 1.0663038710804666 | 6.808995645078939 | 36.256779848569074 | 89.24147491629141 | 5.489121597160912 | 1157.131952527469 | 0.006512986859852944 | 0.05181286318160206 | 0.0028005982797696055 | 0.16681230416370763 | -0.028668030644176556 | 0.0011191861766307 | 0.0011191861766306488 | 0.07506239521522044 |
| Environmental & Waste Services | 86 | 0.07879172413793104 | 0.11917242531350217 | 0.19189575392252223 | 0.20676852622066183 | 0.8219353591662187 | 0.9544076549916705 | 0.054348041315606846 | 0.5043075835957249 | 0.029980000000000003 | 0.20126685325298424 | 0.047814387649734336 | 1.6302770377529443 | 3.340836896990688 | 14.978449052948609 | 27.418717580911146 | 4.680760599570829 | 549.5790790368981 | 0.09556030288716413 | 0.0748874492373683 | 0.028259328543857452 | 0.22495391418471472 | 0.06210179286154515 | 0.9476265002446901 | 0.9476265002446901 | 0.1209624712478881 |
| Farming/Agriculture | 32 | -0.007699374999999998 | 0.06554866344228205 | 0.09124579364966134 | 0.21868498381957277 | 0.6861115455181382 | 0.8746992284349784 | 0.05058580358213098 | 0.45299255806954924 | 0.029980000000000003 | 0.310601084517407 | 0.04167142710343383 | 1.4758582162441996 | 1.3516162158425524 | 14.707892115448548 | 20.129193995151144 | 3.2090475248642476 | 23.819322781968737 | 0.1299961971544714 | 0.03061530342509149 | 0.013450482592225456 | 0.38726473158402225 | 0.14029208346160055 | 0.38932196061718255 | 0.3893219606171825 | 0.06613173568128106 |
| Financial Svcs. (Non-bank & Insurance) | 235 | 0.09082781690140847 | 0.12316551032467732 | 0.003986998716634871 | 0.1921273875658431 | 0.10910525070369609 | 0.7971007195992842 | 0.046923153965086215 | 0.27738631258663876 | 0.0258 | 0.8995871097130348 | 0.021654513135349877 | 0.03741104570867409 | 31.486334617180493 | NA | NA | 2.2299287385592383 | 21.864515213007955 | NA | 0.06990675981640994 | 0.1319795854325862 | 1.2262482887311255 | 0.6428251670643044 | 0.23859654799119204 | 0.238596547991192 | 0.12232122312899665 |
| Food Processing | 101 | 0.06848840909090909 | 0.1279885383691914 | 0.1753093853314738 | 0.2502009007866638 | 0.532117428178121 | 0.6363265081541909 | 0.03933461118487781 | 0.3255716456670335 | 0.0258 | 0.24819053775449415 | 0.03424655347060719 | 1.4801162017099179 | 2.1935894352175414 | 12.883089542134233 | 16.826468443447887 | 2.5667103507314697 | 375.1949183186845 | 0.052654172141950666 | 0.03213035755249827 | 0.020938027507652963 | 0.15123913232404507 | 0.10117860572097045 | 0.6097629836433757 | 0.6097629836433757 | 0.1295280562972138 |
| Food Wholesalers | 18 | 0.12012500000000001 | 0.01558491306059144 | 0.08885997750640885 | 0.038720173535791755 | 0.8066761959870339 | 1.0346238620519972 | 0.05813424628885426 | 0.5803291952709172 | 0.029980000000000003 | 0.3590472455959706 | 0.04511919787280942 | 5.816600387634345 | 0.5436161544559327 | 15.871954547377648 | 35.36101597589498 | 5.017410786298054 | 8.635295744239595 | 0.05381609459391457 | 0.010154823902139759 | 0.026125454156993962 | 0.8755572432669068 | -0.05025675254223573 | 0.001994219653179191 | 0.001994219653179141 | 0.015356701695384856 |
| Furn/Home Furnishings | 40 | 0.050844444444444435 | 0.07979264517520307 | 0.14594063278054276 | 0.18916536786093302 | 0.7794883146985623 | 0.8832454494140802 | 0.05098918521234458 | 0.4052293488753811 | 0.029980000000000003 | 0.2540581733269667 | 0.04359513070439593 | 1.878711078869517 | 1.310844897084742 | 9.733423917830745 | 15.816425327036262 | 2.6811847780363887 | 125.49843153837293 | 0.10604425927478943 | 0.02742211302108916 | 0.013722507350154173 | -0.268315983961284 | 0.13370153727916076 | 0.27174160213987486 | 0.27174160213987486 | 0.08158213940561013 |
| Green & Renewable Energy | 25 | -0.0008999999999999986 | 0.26119284560598877 | 0.06893357173637996 | 0.4303428154631656 | 0.6787637152198226 | 0.9818502419420978 | 0.055643331419667014 | 0.5604169570489518 | 0.029980000000000003 | 0.39047333707738796 | 0.04246175928540003 | 0.27102832816880995 | 13.152748324967906 | 22.940439620941806 | 50.76278937521196 | 1.6801621931847164 | 40.67259807376087 | -1.5824581888131781 | 0.3568714923853575 | 0.2581980339400441 | 1.1011353779451551 | -0.20588897193795236 | 0.001453488372093023 | 0.0014534883720930258 | 0.25882529218209455 |
| Healthcare Products | 265 | 0.1390005633802817 | 0.14236329164930261 | 0.1321841382355416 | 0.13641522537328338 | 0.8008924234779894 | 0.833584082448911 | 0.048645168691588594 | 0.4618945988808825 | 0.029980000000000003 | 0.09655711279842244 | 0.046061322687575186 | 0.963176898461064 | 7.418860964552465 | 28.528876115334604 | 49.24884508873965 | 5.774542888763149 | 317.981478965745 | 0.25162848288718354 | 0.05153195425594519 | 0.11832959057934007 | 1.1346429444683592 | 0.10549129143429795 | 0.30107203248356434 | 0.3010720324835643 | 0.1409061346196625 |
| Healthcare Support Services | 129 | 0.17543859649122812 | 0.04968880162522246 | 0.3527178244976464 | 0.24053692123715872 | 0.7388082452571512 | 0.8507744932523916 | 0.04945655608151288 | 0.4449160731789303 | 0.029980000000000003 | 0.24072345229636458 | 0.04281953220576919 | 7.715434060244526 | 0.6820844203953057 | 10.360969964204955 | 13.628443805969216 | 2.908873188852539 | 104.17605537136028 | -0.05331303854529308 | 0.007409175498195439 | 0.006846234519744327 | 0.19571731702201534 | 0.16598318123555375 | 0.25627274193952404 | 0.2562727419395241 | 0.04844772409047084 |
| Heathcare Information and Technology | 139 | 0.1502389285714286 | 0.13140034808253312 | 0.16352219103562232 | 0.1642744803976314 | 0.7535044118211223 | 0.7909028907872078 | 0.0466306164451562 | 0.4244860262497535 | 0.029980000000000003 | 0.10793771659912331 | 0.04395967428531497 | 1.244529189662103 | 7.33387458565224 | 29.316679172039294 | 50.48768796980264 | 7.119657387892159 | 162.96068906351726 | 0.230695661728999 | 0.03824160897783545 | 0.0007246922376176022 | 0.1028322873125889 | 0.14110113703375673 | 0.1055403844498929 | 0.10554038444989289 | 0.13688108658432346 |
| Homebuilding | 30 | 0.13522173913043478 | 0.11811793417275933 | 0.13576565262352838 | 0.2030435174635442 | 1.3290311296483035 | 1.4589538372780313 | 0.07816262111952307 | 0.36557254084354074 | 0.0258 | 0.2465771383242102 | 0.06353353950314977 | 1.3657613592279838 | 1.209195427123592 | 9.544930988811277 | 10.22676909904947 | 1.7506787743935 | 17.34211171965205 | 0.6609636749904222 | 0.007353378642970425 | 0.0063110106495485605 | -0.10147826243566957 | 0.17701980078050125 | 0.07582219186699346 | 0.07582219186699346 | 0.11820899341778766 |
| Hospitals/Healthcare Facilities | 32 | 0.04236545454545456 | 0.10195066535222672 | 0.13175970132459572 | 0.2031542536465011 | 0.8077248329160305 | 1.2831022322021963 | 0.06986242535994366 | 0.49211448705692795 | 0.029980000000000003 | 0.49850202834771307 | 0.04594578090392208 | 1.512408642599691 | 1.535517811612603 | 8.965463247068126 | 16.183161799511307 | 5.779901782873066 | 44.60670222235663 | 0.03372627120613141 | 0.05918657412478547 | 0.013927684229044475 | -0.26096085143205294 | 0.706385377665926 | 0.10911348102850074 | 0.10911348102850071 | 0.09485783762237918 |
| Hotel/Gaming | 66 | -0.0037959459459459503 | -0.10338054015318786 | -0.052366069049734905 | 0.233404223072424 | 1.1898252960272824 | 1.56468392285972 | 0.08315308115897879 | 0.43694205263736113 | 0.029980000000000003 | 0.36401274176782844 | 0.060850864558541794 | 0.3818038451098195 | 8.078257152585952 | 38.324760402618416 | NA | 6.096573931589885 | 64.17173094138856 | 0.15669943941554873 | 0.18514010951751525 | 0.12996342799426844 | NA | -0.30404227686734225 | 0.005007636426932952 | 0.0050076364269329154 | -0.14013203795027143 |
| Household Products | 140 | 0.14176819999999998 | 0.1819667744413215 | 0.34990818070240404 | 0.2023689287495646 | 0.6837848719774786 | 0.7300042258200384 | 0.04375619945870582 | 0.5465668265331682 | 0.029980000000000003 | 0.1292850892914983 | 0.04092863119781059 | 2.017031766019237 | 4.093420857302042 | 17.59977177709689 | 22.32691974834668 | 9.058770037102697 | 36.29200380102163 | 0.08852960286923306 | 0.036469456611976016 | 0.012704344447733367 | -0.025748375486340506 | 0.31596573813617485 | 0.608526708455038 | 0.608526708455038 | 0.1827156850383734 |
| Information Services | 77 | 0.12192054054054054 | 0.2339520762233811 | 0.24335217141940213 | 0.2034638500005031 | 0.9746191270150343 | 1.0099196260149268 | 0.056968206347904546 | 0.4237334323941007 | 0.029980000000000003 | 0.08564753071541022 | 0.0539634506136396 | 1.1415497263439134 | 10.543643178813669 | 31.702639169289323 | 44.480181369409 | 8.383058579954936 | 71.12999032730562 | 0.06790317038418667 | 0.030739337558518105 | -0.0014683566513378913 | -0.07075273655204885 | 0.14346907619602076 | 0.32413898792734774 | 0.32413898792734774 | 0.23610747495742426 |
| Insurance (General) | 21 | 0.05512214285714286 | 0.12831289999334866 | 0.09255951163135816 | 0.19299294104911144 | 0.5587852752875939 | 0.6823375793703895 | 0.04150633374628239 | 0.3012204051735581 | 0.0258 | 0.2898373665216235 | 0.03493504424036056 | 0.8193859351037079 | 1.9727436127834244 | 9.98611664048919 | 15.008167570981826 | 1.4487601146501508 | 50.36284753835904 | -0.15439187837672572 | 0.007750870874152129 | -0.03165018074533069 | -0.44470666364534434 | 0.014880081144398424 | 1.9278781887477539 | 1.9278781887477539 | 0.12922179742688972 |
| Insurance (Life) | 26 | 0.03345050000000001 | 0.08477946992051422 | 0.043331979597565747 | 0.13003550125681396 | 0.6444797320249215 | 0.9764166324940539 | 0.05538686505371934 | 0.306764746756935 | 0.0258 | 0.5453413565246409 | 0.0354530760404619 | 0.6020940907392548 | 1.3106236214950624 | 12.509114846235827 | 15.004458995361144 | 0.5908804164790717 | 28.98599964627679 | 0.01346441993151282 | 0.0016236942865729218 | -0.0038606362671102083 | 0.0263748191236712 | 0.05605803505335443 | 0.37954798472289947 | 0.3795479847228995 | 0.08479024195083217 |
| Insurance (Prop/Cas.) | 55 | 0.030855111111111107 | 0.10847421675224501 | 0.10737324263625311 | 0.19459729772239065 | 0.5781962611665361 | 0.6432174198310505 | 0.03965986221602558 | 0.22934083377302145 | 0.019200000000000002 | 0.20036030011663622 | 0.034521850286273026 | 1.105706601852552 | 1.4442166689309721 | 9.685827820945773 | 12.331872133525609 | 1.543246884950685 | 22.123312520281296 | -0.5280457269678629 | 0.010637588426180641 | 0.0036507669157428164 | 0.1346544089460229 | 0.09193652734031799 | 0.38393406234625005 | 0.38393406234625005 | 0.10894128541349707 |
| Investments & Asset Management | 348 | 0.006503220338983045 | 0.16949131848115098 | 0.07235458316488017 | 0.18522401728308402 | 0.7849330909198695 | 0.9292368077719284 | 0.053159977326835015 | 0.28854952848131826 | 0.0258 | 0.3113902411235565 | 0.042471202970230125 | 0.45307081218054784 | 5.871516322365792 | 26.171674354963887 | 30.597103347514032 | 2.050155422152945 | 625.4061996670526 | NA | 0.029159132551968562 | 0.05307040842219577 | 0.4622776970878483 | 0.12346905522546975 | 0.5269656225294622 | 0.5269656225294622 | 0.16744692784157078 |
| Machinery | 125 | 0.0343967105263158 | 0.1307484370934618 | 0.21421867033781458 | 0.21031036635138367 | 0.9576485509506472 | 1.0479358847691829 | 0.05876257376110543 | 0.34280553440309797 | 0.0258 | 0.16424258943543665 | 0.05220460141411764 | 1.7786859034556404 | 3.0635239041521163 | 16.702375922383748 | 23.08223261612077 | 4.546716372640119 | 46.08685518800034 | 0.23307038550191156 | 0.024372114670142813 | 0.03994013246202416 | 0.2062480656024749 | 0.1264807435923593 | 0.4537441140915281 | 0.45374411409152815 | 0.13211554307149764 |
| Metals & Mining | 86 | 0.04019916666666667 | 0.11465099887537564 | 0.10749615366753695 | 0.5198387393463733 | 0.8191457243801408 | 0.9037228265597004 | 0.05195571741361786 | 0.6784026451141769 | 0.040925 | 0.1926188206516461 | 0.047702603820969684 | 0.9709846969015278 | 2.9961886099567443 | 13.901198791089055 | 25.92017493804576 | 3.2865078885347216 | 44.41973275025248 | 0.14295395247247653 | 0.08976040924551146 | 0.010325301873605076 | -0.07460881121158068 | 0.026737409474055483 | 1.9735534728963189 | 1.9735534728963189 | 0.11262436965250604 |
| Office Equipment & Services | 22 | 0.007835714285714284 | 0.07500593571755922 | 0.12839147542241577 | 0.23999728394642578 | 0.8343091510750356 | 1.0002964815877964 | 0.05651399393094399 | 0.3111157261368244 | 0.0258 | 0.3235071731023251 | 0.04432424561183153 | 1.972113714604361 | 1.1194240858943512 | 8.820468860712234 | 14.773431283161203 | 2.6021235267337746 | 33.03445829991035 | 0.06659256682513652 | 0.028121497236440328 | 0.0036925574384203833 | -0.10660481631796878 | 0.06362765577478811 | 0.9177120986604297 | 0.9177120986604297 | 0.07510806548165637 |
| Oil/Gas (Integrated) | 3 | -0.012399999999999996 | -0.042742659174976 | -0.023337328566244785 | 0.2562741312741313 | 0.987813337225918 | 1.2606140135050163 | 0.06880098143743676 | 0.2638843975896713 | 0.0258 | 0.30601073208560187 | 0.05351054886765906 | 0.6449724865989008 | 1.5354222004654785 | 10.77335432691406 | NA | 1.049004784404624 | 52.49632530120481 | 0.05386450545774042 | 0.11103398463515529 | -0.06725011803477571 | NA | -0.06188553889817617 | 0.04477710843373494 | 0.04477710843373495 | -0.03958005482758781 |
| Oil/Gas (Production and Exploration) | 278 | -0.011709734513274346 | -0.21398495731025832 | -0.06328679112816 | 0.28594713349681666 | 0.8107940246397045 | 1.1833905955492112 | 0.06515603610992277 | 0.5627627424695174 | 0.029980000000000003 | 0.4188642149162133 | 0.04703151508681482 | 0.3078386836810865 | 2.9075110392871673 | 6.394146587731367 | NA | 1.2088683318955453 | 26.13436075156192 | 0.012895675227694475 | 0.38822244842950576 | -0.2284716491229808 | NA | -0.37085636682963297 | 0.01677259585794925 | 0.016772595857949213 | -0.2069884578842894 |
| Oil/Gas Distribution | 57 | 0.10740717948717951 | 0.17432125042370422 | 0.09010014455324526 | 0.08740134915689066 | 0.6025495506569715 | 1.1569354576468236 | 0.06390735360093007 | 0.40777804780152754 | 0.029980000000000003 | 0.5646366505264954 | 0.04018021847112112 | 0.5432274546686021 | 2.4248652088923657 | 9.123331216657595 | 13.945658781175549 | 1.24018893184319 | 37.082779959348315 | 0.06972807174314526 | 0.1348128654934345 | 0.05014869756525568 | 0.3647710066766695 | 0.012807842501367015 | 0.04659291493241009 | 0.046592914932410134 | 0.17376178369902853 |
| Oilfield Svcs/Equip. | 135 | -0.06856603448275864 | 0.004740181743221958 | 0.012932644090616056 | 0.043658438018919055 | 0.8351469957210687 | 1.207736156526019 | 0.0663051465880281 | 0.5026747446872831 | 0.029980000000000003 | 0.43642107631601756 | 0.046919432972396126 | 1.8801409219692327 | 0.7342577025313457 | 11.347598966546137 | 95.77501672860984 | 1.3032352417280142 | 31.776149931718642 | 0.1140675782923368 | 0.041399140362135954 | -0.0007939312059139853 | -0.39825324699839454 | -0.26630862548974504 | 0.0030415759862292557 | 0.003041575986229228 | 0.0069636398233456145 |
| Packaging & Container | 26 | 0.025224210526315786 | 0.09664098627318571 | 0.12248725976415933 | 0.2538264440660422 | 0.6823428815077008 | 0.9216211012020442 | 0.05280051597673649 | 0.2921549503587486 | 0.0258 | 0.35530389787857364 | 0.040732080452847166 | 1.4717693406459775 | 1.7169827985643689 | 10.335189534200357 | 17.47859094945766 | 3.757301185065967 | 24.2523172589606 | 0.07230605776069157 | 0.05339046494887028 | 0.02177664819877731 | 0.22765881308245103 | 0.09759076798351683 | 0.6494473136450327 | 0.6494473136450327 | 0.09860750132462508 |
| Paper/Forest Products | 15 | 0.005061000000000002 | 0.05843192301468415 | 0.08377338690804254 | 0.21086814763291745 | 0.9591878655692225 | 1.1387183512788366 | 0.06304750618036109 | 0.35669571939417954 | 0.0258 | 0.2728558537476297 | 0.05098359220434256 | 1.4821096503747624 | 0.9436908604996481 | 7.709041538464629 | 15.645062769895638 | 1.6062131835036193 | 20.046811587596142 | 0.15400195670021366 | 0.038510324637052895 | -0.00289659923127514 | -0.2791132324214473 | 0.04694524584126205 | 1.1751668769654215 | 1.1751668769654215 | 0.06008455650218768 |
| Power | 55 | 0.010116808510638295 | 0.1982046382980983 | 0.0680220903268518 | 0.11022539636200014 | 0.43089894553631297 | 0.6665369158849023 | 0.040760542429767385 | 0.1985988098435171 | 0.019200000000000002 | 0.43846095917670846 | 0.029034104703269403 | 0.3849902115303567 | 4.365478434899049 | 11.886012377389731 | 22.25721320987319 | 1.9013502632090518 | 21.953539691815568 | 0.025709267919529984 | 0.35107335678984564 | 0.2055474505651342 | 1.195335560604849 | 0.07686818607537643 | 0.8758861241284948 | 0.8758861241284948 | 0.19611736910155966 |
| Precious Metals | 93 | 0.03165090909090909 | 0.2147910388307706 | 0.09874387536842302 | 0.1813211341779995 | 0.7526808918216534 | 0.7572224109852259 | 0.04504089779850266 | 0.6776341202099045 | 0.040925 | 0.112623488142298 | 0.043332889643497734 | 0.4613182701513254 | 4.816617002312094 | 10.29895210389425 | 21.447009085372958 | 2.191621022332762 | 86.45417020156775 | 0.11992866477531236 | 0.12997655288825916 | -0.08186463339316354 | -0.4422377448205774 | 0.08269916319904205 | 0.3190804543851265 | 0.31908045438512644 | 0.21639308705395235 |
| Publishing & Newspapers | 29 | 0.0030811764705882326 | 0.05643398968627482 | 0.10481911231511697 | 0.237931513509759 | 1.1058928086855666 | 1.4081707476360148 | 0.0757656592884199 | 0.37469457859611055 | 0.0258 | 0.3506570567572469 | 0.0558021712060362 | 2.094067922011159 | 1.1672414575150774 | 9.768589159561946 | 21.764632043006802 | 2.072828870620205 | 48.93628356371428 | 0.11595179418705917 | 0.026935334536692845 | 0.0056288048002505545 | -0.04911954742944402 | -0.1418445799382198 | 0.005425539675000019 | 0.005425539675000035 | 0.053133700414144995 |
| R.E.I.T. | 238 | 0.06808419354838717 | 0.23233180736213863 | 0.020493526397506158 | 0.024742221389100028 | 0.7943417624156209 | 1.2058791394920116 | 0.06621749538402295 | 0.32404663855566707 | 0.0258 | 0.43415228137378137 | 0.04564584276358535 | 0.10894301479869328 | 12.853445702702684 | 22.717249672863435 | 61.429724826063385 | 2.114754374861165 | 62.99942866144742 | 0.8965016806343281 | 0.03238381958370286 | -0.15306880511760745 | -0.7512579172000803 | 0.02169137698390085 | 4.304926425494218 | 4.304926425494218 | 0.19052205895653385 |
| Real Estate (Development) | 25 | -0.19924799999999998 | -0.03638448971503492 | -0.014133381657184096 | 0.2731707317073171 | 0.5641158479680449 | 0.8485468366232567 | 0.04935141068861772 | 0.6069587345461144 | 0.029980000000000003 | 0.4863856806938416 | 0.03599233638389006 | 0.21705428819872297 | 5.997432276524977 | 47.57435572158438 | NA | 1.1875663171101498 | 15.95559210526316 | -0.03412921704306389 | 0.33826843447784827 | 0.21690308145710785 | NA | -0.0012987379920889072 | 0 | 0 | -0.06702066747459626 |
| Real Estate (General/Diversified) | 11 | 0.0920425 | 0.06930375331379937 | 0.01955925775268762 | 0.18499999999999997 | 0.7588663923539402 | 0.7807684737144263 | 0.04615227195932092 | 0.20993179354391503 | 0.019200000000000002 | 0.22611863374459878 | 0.038885662050234415 | 0.33115359281110035 | 6.814457271939483 | 25.25416971536394 | 78.40128595993298 | 1.1866321450440618 | 52.41307348791471 | 3.010076740616716 | 0.02573043114273755 | -0.029910701827821965 | 4.974439892029881 | 0.020017463435931023 | 0.6761177753544164 | 0.6761177753544164 | 0.06374284169135565 |
| Real Estate (Operations & Services) | 61 | 0.020951249999999998 | 0.04131406998869502 | 0.07971133246877254 | 0.10487936387860981 | 0.7558814991893474 | 0.9208927333748228 | 0.052766137015291634 | 0.3472166107627512 | 0.0258 | 0.2897237856755935 | 0.04293518982315841 | 2.0466694347095413 | 1.5620549062342843 | 14.823666944541676 | 32.30807833647381 | 3.211968885514006 | 56.828067786122666 | 0.1400779672113061 | 0.012178573466827854 | -0.00635764617637838 | -0.9367776963655569 | 0.04713329207977078 | 0.3908101824522527 | 0.39081018245225274 | 0.040708392406484474 |
| Recreation | 69 | 0.0262240625 | 0.06810673440156714 | 0.08652013993123524 | 0.22557740263103085 | 0.7742194870853449 | 0.8666049795890294 | 0.05020375503660218 | 0.5639985763918559 | 0.029980000000000003 | 0.19678085259101566 | 0.04463124498852453 | 1.4245720046350399 | 3.733091040487094 | 22.593235934486472 | 52.057461234948995 | 10.37050813778886 | 155.3943058020587 | 0.1566398569548586 | 0.045603247079010326 | 0.11377842440533756 | 2.0677973858941097 | -0.07192026554404488 | 0.00708309369429064 | 0.00708309369429061 | 0.06442441565709045 |
| Reinsurance | 2 | 0.0911 | 0.04269278060776392 | 0.037434277758313074 | 0.2514450867052023 | 1.1287984344732374 | 1.162552284097433 | 0.06417246780939884 | 0.252283349677488 | 0.0258 | 0.2780784531256095 | 0.051564816813875966 | 1.017237317675182 | 0.8074970701511205 | 12.924039416278688 | 19.184172065966298 | 0.7490214221242512 | 15.20057915057915 | -0.07602757772703317 | 0.002920252942209731 | -0.009823467416125062 | -0.17142292109247392 | 0.02419370688469173 | 0.36149471974004876 | 0.36149471974004876 | 0.0420918383850227 |
| Restaurant/Dining | 79 | 0.008368936170212764 | 0.11362052797567285 | 0.07240115751477365 | 0.18690061517325515 | 1.1109354329268502 | 1.34479999809822 | 0.07277455991023599 | 0.5362551868675114 | 0.029980000000000003 | 0.25205862631121706 | 0.05994750816913005 | 1.1412993265905524 | 5.268088509378254 | 23.53164279824024 | 80.2485509634631 | NA | 58.9131827767466 | 0.028449815137323243 | 0.05822284197322754 | 0.0247138581382442 | 0.4871532110779687 | NA | 1.143323840028764 | 1.143323840028764 | 0.06552930130985031 |
| Retail (Automotive) | 30 | 0.03197875 | 0.06428963721055747 | 0.10101677694275035 | 0.2318203274186281 | 0.9899549283696469 | 1.2983003362585088 | 0.07057977587140161 | 0.42818769334060935 | 0.029980000000000003 | 0.3320585102931527 | 0.054410393959889156 | 2.0854857642689666 | 1.2354713774059443 | 11.562920284920681 | 19.837016676554224 | 5.987888841341951 | 17.52087132977596 | 0.10951001226456983 | 0.01810229596642221 | 0.01720355931450485 | -0.23160788717362138 | 0.3627555764295495 | 0.03723462603920915 | 0.03723462603920913 | 0.05482476268008062 |
| Retail (Building Supply) | 15 | 0.06416916666666667 | 0.1278852016756044 | 0.37473666366176334 | 0.23936075728833486 | 1.4364527693272269 | 1.5448319293271313 | 0.0822160670642406 | 0.406039068096387 | 0.029980000000000003 | 0.15314560322006773 | 0.0729766906640184 | 3.4633208322498397 | 2.0622277256162804 | 12.587836152496534 | 16.492777890733734 | 40.06705255976665 | 140.10936326540158 | 0.0445947753850694 | 0.020684112057608384 | 0.002022778450870283 | -0.26454073195651945 | 0.002686575363030675 | 0.4550551200615562 | 0.45505512006155624 | 0.12505116505894562 |
| Retail (Distributors) | 85 | 0.04672270833333332 | 0.0769952413191337 | 0.11673794881176164 | 0.25020494886257216 | 0.7544930962556359 | 0.9709642518894183 | 0.05512951268918054 | 0.4197426052172029 | 0.029980000000000003 | 0.31383121292981025 | 0.04469647248115972 | 1.6830973049227915 | 1.4939726023257278 | 13.87615007968248 | 18.778751898007332 | 3.3874229957444038 | 138.4448999428416 | 0.1553712869000455 | 0.03681838430677834 | 0.050780477336164566 | 0.6311387798933072 | 0.09671544926260549 | 0.5236595814721173 | 0.5236595814721173 | 0.07900741664313288 |
| Retail (General) | 17 | 0.024121428571428565 | 0.04629571086718491 | 0.14673499048151145 | 0.24420249386604162 | 0.8158161595249539 | 0.8989781986771581 | 0.05173177097756186 | 0.3891086642216753 | 0.0258 | 0.17589407943441762 | 0.04594524783601932 | 4.097280581112848 | 0.9340125081690106 | 12.294282269885292 | 22.811510729590694 | 5.434608571329924 | 22.701744745699372 | 0.0005801414846466877 | 0.020052800278028426 | 0.00022870350403747554 | -0.4279977871242316 | 0.2064061291768292 | 0.36119871746793664 | 0.36119871746793664 | 0.04092206326636516 |
| Retail (Grocery and Food) | 14 | 0.06278571428571429 | 0.03477944470880662 | 0.09627991103939768 | 0.2343460786276352 | 0.1522248643717008 | 0.24210864998201992 | 0.02072752827915134 | 0.377189287326462 | 0.0258 | 0.48543831871077164 | 0.019808337094888814 | 4.113426821923807 | 0.38776793300135814 | 5.746899396042721 | 14.309495478867953 | 2.505680111477363 | 14.413462025265975 | -0.0019838027348915957 | 0.022882199540951748 | 0.0011046969695747576 | -0.14716520493103935 | 0.30626515873294846 | 0.1284866271514254 | 0.12848662715142534 | 0.027066363205398937 |
| Retail (Online) | 75 | 0.09283413793103451 | 0.05737275938209128 | 0.11041784163396202 | 0.16129555163492154 | 1.1376905330729945 | 1.1641204247505164 | 0.06424648404822438 | 0.5286592105592185 | 0.029980000000000003 | 0.06668899619263163 | 0.061421465875416595 | 1.800799944356819 | 4.706890357997243 | 33.186332533470555 | 83.83424800114123 | 18.62437568372255 | 131.27291479009298 | -0.03697726524193984 | 0.0772451057530893 | 0.035451473830388706 | 0.5536864691944209 | 0.2705462908122298 | 0.05660671732423871 | 0.05660671732423872 | 0.06285293595552784 |
| Retail (Special Lines) | 85 | 0.05570571428571428 | 0.028917338857007716 | 0.05289633441365744 | 0.24552721852134185 | 1.0368527310405244 | 1.28200255415871 | 0.06981052055629111 | 0.4900945730473005 | 0.029980000000000003 | 0.32550445482921975 | 0.054210680316990945 | 2.294482687456437 | 1.1005434739152702 | 11.399676175611779 | 43.75303051493489 | 5.513442421186035 | 55.99188411017896 | 0.047494439458487206 | 0.017848599906423814 | 0.0005042581574495583 | -1.7933947942274442 | -0.006403584007527591 | 0.003196087125085441 | 0.003196087125085456 | 0.025064988173618206 |
| Rubber& Tires | 3 | -0.042133333333333335 | -0.004966495834843661 | 0.00010380134134452082 | 0.15903459134450276 | 0.5479963985646816 | 1.0939555482653982 | 0.06093470187812679 | 0.43827239010407376 | 0.029980000000000003 | 0.6362340824801757 | 0.036090205126205394 | 1.0683496657652694 | 0.7406329645505939 | 9.84116819817675 | NA | 1.044917656279905 | 24.89280216470498 | 0.13627166748967 | 0.05625081658236745 | -0.0053268306017885516 | NA | -0.2568636111000834 | 0.0006758488148622678 | 0.0006758488148622677 | 8.471147091679e-05 |
| Semiconductor | 70 | 0.03770520833333332 | 0.24090189851762 | 0.17390673660088912 | 0.10767179368946722 | 0.9617032705158021 | 1.0019932071355018 | 0.05659407937679568 | 0.3725527386379852 | 0.0258 | 0.08851229034889581 | 0.05325184826739939 | 0.7480023912643442 | 7.159084587076163 | 18.04337796507661 | 29.301109086416297 | 6.874724790334205 | 726.5221969353058 | 0.17435415119284708 | 0.1276133683661259 | 0.1606080271258418 | 0.7983281840348446 | 0.22132843436176297 | 0.4210188979419662 | 0.42101889794196623 | 0.24792674895127 |
| Semiconductor Equip | 40 | 0.08492499999999997 | 0.22214383974230267 | 0.27892537443467325 | 0.1283245337282424 | 1.0688501095696221 | 1.0703806513615421 | 0.05982196674426479 | 0.3590552168142753 | 0.0258 | 0.07435767191806535 | 0.05677419696050618 | 1.2955167484418966 | 5.143851768897692 | 18.692654437299094 | 22.85639158051403 | 7.8717905246460385 | 55.871007175483264 | 0.27818447663763024 | 0.03711723123413067 | 0.011627942992143444 | 0.2859438641860631 | 0.32234700585446124 | 0.2330874998121391 | 0.23308749981213905 | 0.231831627226387 |
| Shipbuilding & Marine | 11 | 0.031014285714285713 | 0.05111343454462016 | 0.03741410931236756 | 0.2439167399589563 | 0.7441157519970447 | 1.035148855900927 | 0.05815902599852375 | 0.2983019628501746 | 0.0258 | 0.38330558536377457 | 0.04308552388871395 | 0.6761789407498047 | 1.7395230517207627 | 10.668320496769473 | 30.64396086181471 | 1.1313888455192476 | 49.987186364820744 | 0.08572365754692728 | 0.09728489447564256 | 0.07100749228457118 | 1.2447679087535939 | -0.05697051984097218 | 0.00156783103168156 | 0.0015678310316815658 | 0.05663204602476245 |
| Shoe | 11 | -0.0011125000000000006 | 0.09215506564777627 | 0.20895913003172306 | 0.13438008307011218 | 0.978275005705732 | 0.9832092184040022 | 0.0557074751086689 | 0.3150494707159971 | 0.0258 | 0.06429307080561467 | 0.05333676616265818 | 2.5047178788505673 | 5.0458322546184595 | 35.83292533805466 | 56.48797169319823 | 14.870008712382473 | 46.18128726931203 | 0.2038273827804307 | 0.007617912077544867 | -0.02125462424902995 | -0.30661254345367106 | 0.23700994672881648 | 0.4827492555440928 | 0.48274925554409287 | 0.08934535082223198 |
| Software (Entertainment) | 101 | -0.004129047619047612 | 0.20610436169824337 | 0.14733514240062395 | 0.12015444977232942 | 0.9595450250239156 | 0.95869522130184 | 0.05455041444544685 | 0.6261407642744445 | 0.029980000000000003 | 0.025492110851799844 | 0.05371771427622788 | 0.6796224176385661 | 8.162760263426316 | 25.09006052547303 | 38.04280251527433 | 6.23326053224863 | 157.38488806622505 | 0.05405821769479559 | 0.14038188523708567 | 0.09936505726465815 | 0.6779602325217717 | 0.17714237086811832 | 0.00263078250845753 | 0.0026307825084574965 | 0.21793855131962409 |
| Software (Internet) | 36 | 0.19335999999999998 | 0.05059438968915846 | 0.06657754301766602 | 0.05971398081317674 | 0.7489829463811578 | 0.7731297817248773 | 0.045791725697414215 | 0.3272513071218806 | 0.0258 | 0.08114570483472933 | 0.043604222044956245 | 1.005696970573685 | 15.670513651651863 | 19.20812597236386 | 95.4389335203651 | 15.18744917520298 | 67.88862020182876 | 0.10575986297138683 | 0.07898986325218318 | 0.06950194591862519 | 2.172385347684909 | -0.11228566914958794 | 0.0017811704834605599 | 0.0017811704834606035 | 0.06778427722305094 |
| Software (System & Application) | 388 | 0.18927503401360543 | 0.23304335184880492 | 0.22277139598413231 | 0.14135251695865048 | 0.8940094147780339 | 0.9116872129500534 | 0.052331636451242516 | 0.4797059001928455 | 0.029980000000000003 | 0.06149896085335673 | 0.05045922454759551 | 0.9183098124080067 | 11.823495715635733 | 30.423805681689416 | 43.93497908448027 | 14.073826222631265 | 148.99150403292035 | 0.13148461542558323 | 0.06803683883367444 | 0.05598702822445494 | 0.3368903374513123 | 0.28087977508472173 | 0.29353987792074177 | 0.29353987792074177 | 0.2490378107929511 |
| Steel | 32 | 0.004723181818181818 | 0.03553259633998463 | 0.058100247248397074 | 0.2452883447769849 | 0.7848408528683425 | 0.952674326623155 | 0.05426622821661291 | 0.39319155229808395 | 0.0258 | 0.3344020408467834 | 0.04241761878922857 | 1.7027174008564028 | 0.9348148107342041 | 9.73900318919887 | 23.061200217062375 | 1.5528479464148082 | 35.72607944310593 | 0.21691105123338691 | 0.06958239712924102 | 0.05573441180672951 | 0.2849257135685403 | -0.028409504493084305 | 0.0064673007856719126 | 0.006467300785671926 | 0.03630202797164876 |
| Telecom (Wireless) | 16 | 0.06527428571428572 | 0.12481677647749129 | 0.10222796915324003 | 0.22645519947678222 | 0.3928540426155399 | 0.5310142821993883 | 0.03436387411981112 | 0.3977891384408794 | 0.0258 | 0.35304680875165795 | 0.028881101621496843 | 0.837351433012571 | 3.670171538931945 | 10.14115826322539 | 29.546652439145003 | 2.355593966908743 | 24.683121593527087 | 0.10992374328413039 | 0.15333720134670512 | 0.03515227197167915 | 1.6819529435066813 | 0.08910396354573871 | 0.03035906170520749 | 0.030359061705207524 | 0.1265185910881838 |
| Telecom. Equipment | 96 | 0.3164748275862069 | 0.1868731479566305 | 0.21798778520816608 | 0.17902419010153528 | 0.8321899032421213 | 0.8693736521919523 | 0.05033443638346015 | 0.4310848014202543 | 0.029980000000000003 | 0.12890225671719946 | 0.04666729139220242 | 1.202507645635238 | 3.564182895581489 | 13.922166632416614 | 18.523992372505774 | 4.839981523865038 | 50.67812474449751 | 0.16836471254894772 | 0.02948276994734827 | 0.03347339345026165 | 0.11714492463095033 | 0.17100403472629144 | 0.6470705916056715 | 0.6470705916056715 | 0.188558332583883 |
| Telecom. Services | 58 | 0.07790958333333332 | 0.19456609726786683 | 0.13777796302969947 | 0.16707497661242765 | 0.4218094129832811 | 0.6590463448973455 | 0.04040698747915471 | 0.43529745323644603 | 0.029980000000000003 | 0.4539679483934028 | 0.031998780410253905 | 0.7518885560052747 | 2.506385123412646 | 6.761231193397334 | 13.116222031782481 | 1.7288217901555876 | 22.27268322910477 | 0.01184630346198197 | 0.1262725136691345 | -0.023647204248838035 | -0.021878837569718146 | 0.11268328342687449 | 0.5191915938459982 | 0.5191915938459982 | 0.19073146201563007 |
| Tobacco | 15 | 0.5282333333333333 | 0.4279906353325778 | 0.45326065003003474 | 0.3466611044689678 | 0.6127084551791008 | 0.721841145813917 | 0.04337090208241688 | 0.24488233552075422 | 0.019200000000000002 | 0.2326199241662911 | 0.03654236698609617 | 1.156729762888958 | 4.815429210466744 | 10.48285471378874 | 11.203681381675812 | NA | 54.618361961531335 | 0.13100960465577405 | 0.01754340460060597 | 0.01238721827891767 | 0.006870486775321647 | -0.002310808677456026 | 1.6495295056583579 | 1.6495295056583579 | 0.4291556052120133 |
| Transportation | 21 | 0.09416076923076921 | 0.06276779961127353 | 0.133171237007476 | 0.22365897901010617 | 0.7869478459766643 | 0.907385385057 | 0.05212859017469039 | 0.2867619467746414 | 0.0258 | 0.24066478106211525 | 0.044115754919745676 | 2.4515741849278605 | 1.5567317897080666 | 12.959492073346206 | 25.626980651208445 | 6.7749292258814835 | 48.60592887164585 | 0.07969313674377931 | 0.058812779442184736 | 0.022628756627930156 | 0.6834097279228616 | 0.22767914053607058 | 0.5544234835637599 | 0.5544234835637599 | 0.060731915901517 |
| Transportation (Railroads) | 6 | -0.0147 | 0.391250230607379 | 0.12967763596876056 | 0.23115977314390468 | 0.7411339573627611 | 0.8448084966784221 | 0.04917496104322151 | 0.16833997765542183 | 0.019200000000000002 | 0.1839447211506495 | 0.04270765575817958 | 0.39701712586492816 | 8.099944429036343 | 15.458052399785434 | 20.934853811173205 | 5.8229959384546 | 28.550848056184293 | 0.016536008612455824 | 0.16356660291394318 | 0.044470443723626116 | 0.12829844070642524 | 0.2147462635210425 | 0.41027528063719787 | 0.41027528063719787 | 0.38690910749986346 |
| Trucking | 35 | 0.030642105263157887 | -0.02882246905058946 | -0.04035655435213481 | 0.21675277856229133 | 0.9459911344624463 | 1.1117887824981547 | 0.06177643053391291 | 0.38783760729396827 | 0.0258 | 0.25237767229324226 | 0.05093871987314971 | 0.8363612764475106 | 2.7292351713007115 | 10.06408212794103 | NA | 4.8117257666698885 | 46.7383416220156 | 0.06072380004133968 | -0.008012577696492773 | -0.08670771031573203 | NA | -0.17695648613703024 | 0.0027100744882994714 | 0.0027100744882995187 | -0.05073213664972472 |
| Utility (General) | 16 | 0.022684999999999997 | 0.20403341154138444 | 0.06785090533886397 | 0.117171773264289 | 0.48558485606254603 | 0.7397784589518577 | 0.04421754326252768 | 0.18444652874211906 | 0.019200000000000002 | 0.4275674762006704 | 0.031304345632403356 | 0.3730703446726419 | 4.136621754888119 | 12.15184429138481 | 20.529474325741415 | 1.8404346419169308 | 18.73085205950922 | 0.09013450236117515 | 0.3114652228597598 | 0.1989684170004613 | 1.1039575205276062 | 0.07485712426664354 | 1.0089818624326357 | 1.0089818624326357 | 0.20149672072710154 |
| Utility (Water) | 17 | 0.12739090909090908 | 0.3046286436581441 | 0.08050168864973231 | 0.18748481661181424 | 0.5729021415532374 | 0.7339677478881326 | 0.04394327770031986 | 0.35960926569887885 | 0.0258 | 0.288051163370102 | 0.03671052104735977 | 0.29873574208480336 | 9.786175412560377 | 20.924855016692508 | 32.162808766564744 | 3.507385026927302 | 62.39214919438848 | 0.16949223860701113 | 0.4727682208153895 | 0.9662024548757527 | 3.945375740335322 | 0.08246567667915546 | 0.6636643303963654 | 0.7130556748510612 | 0.3020891365798054 |
| Total Market | 7582 | 0.08860444816988013 | 0.09620170484014086 | 0.06050609668535474 | 0.17760057899121492 | 0.7481510729858899 | 0.9415331238919882 | 0.05374036344770183 | 0.4120539592527792 | 0.029980000000000003 | 0.32580752942081304 | 0.043361776507015795 | 0.6674701198606623 | 3.6462526886648874 | 20.01732271472191 | 36.46096474546584 | 3.8138539866725387 | 103.24608265487092 | -0.36101539217904444 | 0.05596708595971746 | 0.025664988528031712 | 0.3315979365036908 | 0.08246567667915546 | 0.7130556748510612 | 0.7130556748510612 | 0.09607036759767228 |
| Total Market (without financials) | 6253 | 0.09404120434190034 | 0.09930087339393491 | 0.10584436361002644 | 0.1774336097509946 | 0.8617766222327651 | 0.9783060090968476 | 0.05547604362937121 | 0.44772960581474536 | 0.029980000000000003 | 0.20066342541531326 | 0.04873563001679652 | 1.1137481600322767 | 3.196959116613741 | 16.520979574563068 | 30.624257438474952 | 4.750107542777902 | 87.07726236585047 | 0.08281119286219245 | 0.059114865494029625 | 0.025390218706648097 | 0.29398897453501566 | 0.07775091279087382 | 0.8396750904099498 | 0.8396750904099498 | 0.09929752116915765 |

## Industry Average Beta (Global)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 348 | 0.04968401960784313 | 0.046369827884157076 | 0.09341621106422812 | 0.24988852578843032 | 0.9882805307734214 | 1.1319137589948762 | 0.07449823251810488 | 0.37243852902684466 | 0.0353 | 0.2904840631480306 | 0.06043237762279403 | 2.140102536817457 | 1.7076898417157673 | 12.740599099038405 | 29.56873357908132 | 2.5099680285363823 | 69.02658656640058 | -0.0288297647585567 | 0.019024834754616627 | 0.01183698856558044 | -0.10606811432482084 | -0.03953923793915843 | 0.009018629222583481 | 0.009018629222583452 | 0.04960223639015808 |
| Aerospace/Defense | 255 | 0.07838546583850929 | 0.05474920636018071 | 0.11423386323796658 | 0.21356462870588366 | 1.0024811526281652 | 1.1325267666463197 | 0.07453354175882801 | 0.32562776491531553 | 0.0353 | 0.2305578462994164 | 0.06336130065531168 | 2.1134795842234686 | 1.927150626049155 | 14.013550352444684 | 26.8606911293056 | 4.6248530905303005 | 76.24782689697476 | 0.3935976502080867 | 0.0329534251364801 | -0.0019643446180409485 | 0.6651113997790041 | -0.0017517061044385349 | 0.010312764937080448 | 0.010312764937080443 | 0.059330014314364084 |
| Air Transport | 156 | -0.02624438461538462 | -0.14640343076642073 | -0.0923608918368996 | 0.31438683636038384 | 0.9177893627711246 | 1.5558940900594647 | 0.09891949958742516 | 0.3275500638650721 | 0.0353 | 0.5524382470902457 | 0.05867802513163615 | 0.6457204126429056 | 2.4945852060044076 | 24.887778926888874 | NA | 2.617410455499562 | 140.70446974608913 | -0.07419854689493033 | 0.12671727568986016 | 0.00438217474096354 | NA | -0.35472999202518024 | 0.020935579476952265 | 0.020935579476952237 | -0.1514746483878396 |
| Apparel | 1188 | -0.01944730011587482 | 0.07895253308908266 | 0.08754180087411942 | 0.2763037037545783 | 0.853766109354668 | 0.91974417018327 | 0.062277264202556346 | 0.31184050864198964 | 0.0353 | 0.18044958371276787 | 0.05574478099678334 | 1.2319624652352226 | 2.9035711339165524 | 21.19404750665937 | 35.17179023969078 | 3.653226466265027 | 95.19271431887735 | 0.246851039877393 | 0.04339849561843164 | 0.013140272307589266 | 0.24783335547374252 | 0.02441369180501603 | 1.7153366570976118 | 1.7153366570976118 | 0.08031671736285691 |
| Auto & Truck | 144 | 0.008959387755102043 | 0.026116229675050597 | 0.02019757288299452 | 0.26403304486438145 | 1.011046446440295 | 1.3908100918793502 | 0.08941066129225057 | 0.30826068857209266 | 0.0353 | 0.4290926897160074 | 0.062234268326302335 | 0.86286711983275 | 1.5268667169799859 | 19.792878287323244 | 53.778443636415865 | 1.7637423999800206 | 156.27256481915006 | 0.006223342593151992 | 0.0676093691509492 | 0.03313328814176482 | 1.0701501300192282 | 0.019102539299651326 | 1.2162737004645183 | 1.2162737004645183 | 0.027080488974336604 |
| Auto Parts | 709 | 0.018493838951310862 | 0.026240731097590102 | 0.034016619949833765 | 0.2418073034474979 | 1.278855395804032 | 1.401797850820661 | 0.09004355620727007 | 0.29937810300029793 | 0.0353 | 0.2558158342305505 | 0.07367967059215941 | 1.3814967701299383 | 1.04696516719464 | 11.243398611826539 | 36.171282728865734 | 1.716766846150272 | 78.98671854669723 | 0.12313890091459503 | 0.058200234040694396 | 0.03451237260217902 | 1.751281828042802 | -0.01611439426467019 | 0.007115183504964928 | 0.007115183504964984 | 0.02793480988410377 |
| Bank (Money Center) | 620 | 0.08453200723327309 | 0.0019535025732567456 | 0.00021134270243845115 | 0.2018385257924417 | 0.47930202143470874 | 0.9958221306579454 | 0.06665935472589765 | 0.2118167315121493 | 0.028699999999999996 | 0.7541779427187429 | 0.03237543248417907 | 0.12240599459485685 | 7.748113541961514 | NA | NA | 0.8058746736395114 | 71.41434508725857 | NA | 0.03324992323751933 | 0.040850262075864806 | 19.65584487166099 | 0.07703361938496033 | 0.3738557717796145 | 0.3738557717796145 | 0.0021574186564773325 |
| Banks (Regional) | 850 | 0.07097401273885348 | -0.00019084141059655401 | -0.0003110157139963043 | 0.19244130955102906 | 0.541608568531446 | 0.6931500735198498 | 0.04922544423474334 | 0.19259738563288453 | 0.028699999999999996 | 0.6612471414454477 | 0.0306941556073081 | 0.18061916348465945 | 4.941278280033928 | NA | NA | 0.8144171915543502 | 17.678497838941823 | NA | 0.041003001672158 | 0.026572613835878743 | NA | 0.07261939551182298 | 0.5439957310470919 | 0.5439957310470919 | -0.0021088300151206594 |
| Beverage (Alcoholic) | 223 | 0.07340137724550898 | 0.20272296899195852 | 0.11494548796982305 | 0.25178165969865146 | 0.7341539604842614 | 0.8033392748865462 | 0.055572342233465064 | 0.2427781243058273 | 0.028699999999999996 | 0.15014863898939057 | 0.05041148543079364 | 0.6778647021794201 | 5.863688719779713 | 22.588944420379654 | 28.795988823563306 | 4.951925797052342 | 163.76681633353238 | 0.10258976751752767 | 0.05018873726338192 | 0.03932907608495289 | 0.24686269813777073 | 0.09136431138078918 | 0.7296473786156777 | 0.7296473786156777 | 0.20305434892882004 |
| Beverage (Soft) | 108 | 0.06391868852459016 | 0.15004359982735904 | 0.19808135464622645 | 0.2209494347835911 | 0.6509116265997663 | 0.7186800053771338 | 0.05069596830972291 | 0.3120224363107186 | 0.0353 | 0.1756759595905583 | 0.046370851076178755 | 1.472125004619433 | 3.7948323266530735 | 19.29162173874707 | 25.141934749095892 | 5.901723247731475 | 82.18337119152622 | -0.05544838627339804 | 0.05351758246088692 | 0.04951250000863443 | 0.3627109540711113 | 0.19343727734061583 | 0.7848384602492934 | 0.7848384602492934 | 0.15082503605065087 |
| Broadcasting | 146 | 0.01324925619834711 | 0.14787517294448518 | 0.12962343724148687 | 0.2393224724540934 | 0.6858768416034856 | 0.9757206090412675 | 0.065501507080777 | 0.31231753614001356 | 0.0353 | 0.43511625190134506 | 0.04834687607326708 | 0.995529273803742 | 1.7970064129869014 | 8.13610921821012 | 11.773187414350323 | 1.34689473750717 | 26.64149731131128 | 0.1464019876048404 | 0.036197823486362586 | -0.00029642709176272533 | 0.807528153649082 | 0.019465284070952146 | 1.2773396025035546 | 1.2773396025035546 | 0.14665719487319243 |
| Brokerage & Investment Banking | 575 | 0.08358816793893126 | 0.01029113883419104 | 0.0014969793363148565 | 0.22230716721406613 | 0.4170812123977514 | 0.8570174992053535 | 0.05866420795422836 | 0.2964112853784567 | 0.0353 | 0.6616527976140522 | 0.037102201773892396 | 0.194276808342641 | 6.61930348825638 | NA | NA | 1.5977468994922899 | 44.201549360580934 | -2.0402288547815743 | 0.03718988366449679 | 0.017440904949260462 | -10.226284298674983 | 0.10248729057098893 | 0.5159419054543647 | 0.5159419054543647 | 0.008893746736187667 |
| Building Materials | 439 | 0.019863768115942038 | 0.08616365100742433 | 0.12205115913914638 | 0.255759149127762 | 0.9093397804125348 | 0.9907325966620614 | 0.06636619756773474 | 0.2750731041076881 | 0.0353 | 0.19903276640502102 | 0.05834714998042795 | 1.6645875685228881 | 1.8097196742726982 | 13.579397096941168 | 20.467603763788127 | 2.901620952819778 | 66.9216376653281 | 0.17070952099764924 | 0.04142767872948287 | 0.03125984820507061 | 0.35428453901100215 | 0.08686694096597235 | 0.4147229633724553 | 0.4147229633724553 | 0.08780408479172233 |
| Business & Consumer Services | 923 | 0.07367932604735887 | 0.07607390108257078 | 0.1619707701951342 | 0.25588898098952817 | 0.9130597184101551 | 0.9890051291924944 | 0.06626669544148768 | 0.3224137009951675 | 0.0353 | 0.1775471204967655 | 0.05913097272527232 | 2.4526219940928735 | 2.174791451270585 | 17.284995888960246 | 27.39959945364704 | 4.543316314256659 | 90.74911140013413 | 0.08914302881057155 | 0.02693561349959557 | 0.008770263616906693 | -0.006118581388095989 | 0.08881233838203681 | 0.7064783204199622 | 0.7064783204199622 | 0.07815625262729903 |
| Cable TV | 60 | 0.018461395348837208 | 0.18120573700866768 | 0.11273736665557826 | 0.22910601629864716 | 0.7846306814157183 | 1.054606414897804 | 0.07004532949811351 | 0.306428085448991 | 0.0353 | 0.3447516621771386 | 0.05488686799150743 | 0.7302350532656041 | 3.6661791915588653 | 10.395373883711642 | 19.343111840923548 | 2.746955359539827 | 41.39629383405336 | -0.0006552823118284271 | 0.11704535160235692 | -0.021053584023977966 | -0.15896999663209133 | 0.10469353726580118 | 0.3291022889389591 | 0.3291022889389591 | 0.1807178082970915 |
| Chemical (Basic) | 844 | 0.05610441471571906 | 0.06486937609306058 | 0.05830047024143202 | 0.2247168074718624 | 0.9311754214530038 | 1.0691111060471685 | 0.0708807997083169 | 0.2852257675158434 | 0.0353 | 0.2579781877722254 | 0.059322167053668426 | 1.0424667501964167 | 1.7591172468941758 | 13.320041688164443 | 26.300440571081324 | 1.897601298466219 | 47.06232557681493 | 0.12169372266725441 | 0.08990592248278358 | 0.057049136183993265 | 1.0408000196656972 | 0.039737528173163325 | 1.3594998306259558 | 1.3594998306259558 | 0.06599402993231032 |
| Chemical (Diversified) | 73 | 0.03337515624999999 | 0.03808585836370672 | 0.03124793891189071 | 0.2481112941009404 | 1.048031632511917 | 1.3270222093432342 | 0.0857364792581703 | 0.2488744564697533 | 0.028699999999999996 | 0.3488442840966249 | 0.06322353805579323 | 0.973325018010135 | 1.367885345365418 | 12.956374740690297 | 35.2411715061052 | 1.4535072618966636 | 129.62251426929518 | 0.19363001707459326 | 0.06774511564868557 | 0.029530869367977258 | 0.7117590255112627 | -0.029490179506814138 | 0.03332697362393155 | 0.033326973623931555 | 0.03919076713616907 |
| Chemical (Specialty) | 861 | 0.05370258680555558 | 0.09707254715826102 | 0.0883085478318408 | 0.21582117341015417 | 0.9876840523287519 | 1.0808109733679223 | 0.07155471206599233 | 0.3026924868560246 | 0.0353 | 0.17796850390004934 | 0.06346095329684198 | 1.0615571011396603 | 2.751613936157158 | 15.88532911777755 | 27.731356607432527 | 2.87126621477407 | 61.435271843483626 | 0.17884070358888488 | 0.07586319591814532 | 0.03470968604900245 | 0.3499944351879806 | 0.053334231251365743 | 0.8960947865816967 | 0.8960947865816967 | 0.0979601059535959 |
| Coal & Related Energy | 222 | 0.06571418181818181 | 0.1218290816170572 | 0.10531492718469361 | 0.23719120869784457 | 0.8959412374490998 | 1.013679986125723 | 0.06768796720084165 | 0.4086933250594344 | 0.03948 | 0.35535304618159413 | 0.05399831404124503 | 0.9248649637974896 | 1.2333180933827743 | 5.593105806168129 | 9.533506106452775 | 0.9587625887972162 | 22.51091611623879 | -0.017644460636817693 | 0.0802902955025262 | 0.023395224056865994 | 0.4451615494105017 | 0.07603348212189433 | 0.9830412357576869 | 0.9830412357576869 | 0.12240118268833063 |
| Computer Services | 1007 | 0.06153784090909088 | 0.06918678973224604 | 0.19175452489110154 | 0.22243146519854123 | 1.002571650346871 | 1.0511211184102125 | 0.06984457642042824 | 0.3102109593989236 | 0.0353 | 0.15546475930731418 | 0.0630401223231261 | 3.2119052522719165 | 1.441639137513786 | 14.007509742166441 | 20.0668993666045 | 3.8685276547508676 | 60.29821893758642 | 0.1318102043200423 | 0.016630968016223786 | 0.010223152944133935 | 0.09832211840671143 | 0.14318370184159132 | 0.5151446707783542 | 0.5151446707783542 | 0.07113654947074603 |
| Computers/Peripherals | 337 | 0.005844453441295554 | 0.10061552016867199 | 0.15095340226442908 | 0.1888157572805608 | 1.2349266090265119 | 1.2663921417568875 | 0.08224418736519672 | 0.315119307274991 | 0.0353 | 0.09644246918321457 | 0.07682719929482333 | 1.6523591911652566 | 2.8016692606470146 | 18.05147968168148 | 27.536708740206596 | 6.205039303815056 | 57.748484821262934 | 0.01619834397593741 | 0.04477641851626084 | 0.02922467877265536 | 0.3594151459299558 | 0.19085449785345163 | 0.3457079127846273 | 0.3457079127846273 | 0.10381742632021614 |
| Construction Supplies | 753 | 0.037298051724137936 | 0.09324757838923538 | 0.09452958824826624 | 0.2224910969144936 | 0.9489007969115382 | 1.0957343284461016 | 0.07241429731849545 | 0.28733443270571196 | 0.0353 | 0.2890991212203247 | 0.05901796808577563 | 1.1582545079632034 | 1.5904793753246216 | 10.895685858664661 | 16.464972101413746 | 1.7597374934063412 | 49.37807314022342 | 0.10099063374463307 | 0.05062254660421008 | 0.01831827888424495 | 0.048594004039031094 | 0.07986349375190804 | 0.5933919598594313 | 0.5933919598594313 | 0.09441246292122955 |
| Diversified | 324 | 0.056422099236641224 | 0.12433811979973126 | 0.08553469199412174 | 0.20381517830430806 | 0.7325078955806549 | 0.9892341689916919 | 0.06627988813392145 | 0.23451037040077102 | 0.028699999999999996 | 0.4032320075676552 | 0.04810251257084021 | 0.7944869430218806 | 1.8159464762698883 | 10.243369841838692 | 14.178655182290706 | 1.0856816986322737 | 38.0459008777764 | -0.20773026042628404 | 0.05339680185868785 | 0.029322671623944405 | 0.34756508034898165 | 0.07738529790374182 | 0.33957022768072453 | 0.33957022768072453 | 0.12451555409757133 |
| Drugs (Biotechnology) | 1139 | 0.24874885441527453 | 0.062090736562745635 | 0.04852037122246915 | 0.13519785478395316 | 0.9685394778129185 | 0.984680107510535 | 0.06601757419260681 | 0.45626529096284685 | 0.03948 | 0.09871996498167057 | 0.062379378397587615 | 0.48980970593293854 | 10.37014698527021 | 18.612858580057853 | 106.33980521815054 | 7.299971546270757 | 547.8497415618034 | 0.18818201472731777 | 0.053017714675160095 | 0.3156280800304832 | 15.404114494332054 | -0.043762485981236963 | 0.003091109414749929 | 0.003091109414749882 | 0.10026016955868507 |
| Drugs (Pharmaceutical) | 1319 | 0.16983117021276595 | 0.16853669271730168 | 0.12495543650621611 | 0.16971692757229118 | 0.9257197914498704 | 0.9965706750432711 | 0.06670247088249241 | 0.3991727855676368 | 0.0353 | 0.15009921470735643 | 0.06060448601761264 | 0.7559634978870898 | 4.3834692879439086 | 15.066080670816556 | 24.385692717357813 | 3.8974323376359465 | 78.51376847141269 | 0.17082126261777686 | 0.047018021944881555 | 0.05087616987461571 | 0.4404253624219358 | 0.10897933255853319 | 0.822389446061133 | 0.822389446061133 | 0.18088395166223137 |
| Education | 250 | 0.12704097744360907 | 0.07213175311904294 | 0.07552684045457071 | 0.19574051846959023 | 0.9499461907192076 | 0.9773862759048871 | 0.0655974494921215 | 0.32663572682842823 | 0.0353 | 0.12578498956409234 | 0.06062625821654605 | 1.0923545764525615 | 4.8768075279836705 | 23.878787288397817 | 58.552180606140766 | 4.844654822242692 | 58.53170309792169 | 0.02188975227689002 | 0.0650310856305665 | 0.06565300888450676 | 1.3104919746550734 | -0.002804382309882154 | 0.006523303783484505 | 0.006523303783484535 | 0.07755255557740942 |
| Electrical Equipment | 950 | 0.06300889067524111 | 0.05685260976177123 | 0.08167627551538968 | 0.2078502324152131 | 1.0579135270894295 | 1.0879948514578053 | 0.07196850344396959 | 0.3230302979044234 | 0.0353 | 0.13585721813792845 | 0.06573369053698057 | 1.5372083965326797 | 2.3402953125293577 | 20.354938143376994 | 36.590130464451114 | 3.3101473810447177 | 71.44147918013634 | 0.23327615141193275 | 0.04824715614055023 | 0.03468479048195641 | 0.5482085851898714 | 0.06625010510672431 | 0.6674717895267412 | 0.6674717895267412 | 0.05988437784885174 |
| Electronics (Consumer & Office) | 142 | 0.0081176923076923 | 0.04827881513525814 | 0.07205652394224428 | 0.09751673124555285 | 1.145109372962284 | 1.2232666801248744 | 0.07976016077519277 | 0.3439496510355762 | 0.0353 | 0.23944913896642778 | 0.06690556104084287 | 1.5664643247494714 | 1.0773828965113874 | 11.497667691691621 | 21.323618694899746 | 2.0661965403358313 | 46.43510074669959 | -0.008452810899136451 | 0.055181827278201354 | 0.037719846921732664 | 0.7548371951620465 | 0.12116348626652564 | 0.23661088651545462 | 0.2366108865154546 | 0.05095746016028555 |
| Electronics (General) | 1387 | 0.05039032673267329 | 0.06134223585479155 | 0.08688164708607479 | 0.20994618893740422 | 1.2454565864733256 | 1.244315303120397 | 0.08097256145973487 | 0.3103629442568496 | 0.0353 | 0.12690751313957163 | 0.07400578932479272 | 1.515813832063237 | 1.891331273241231 | 16.689991322975818 | 29.746316242580836 | 2.96479951936241 | 85.41306832360665 | 0.17577548317404054 | 0.05975750426334641 | 0.04469113693593514 | 1.0368999529833396 | 0.06810745928181276 | 0.5983527524045724 | 0.5983527524045724 | 0.06482095539421755 |
| Engineering/Construction | 1263 | 0.03729562814070351 | 0.04930461983145388 | 0.08890641253739132 | 0.25896414975609133 | 0.7667538377017049 | 1.0397204401367581 | 0.06918789735187726 | 0.29240085762704454 | 0.0353 | 0.4991075736001216 | 0.047670477773117385 | 2.015523697242366 | 0.6027654755237734 | 8.22080735946927 | 11.639582527367274 | 0.994800110401009 | 52.359156800334404 | 0.16221290140247865 | 0.03516834977135432 | 0.02883407934974276 | 1.2978074837439155 | 0.07889668580581656 | 0.6295132519264252 | 0.6295132519264252 | 0.05206550041952085 |
| Entertainment | 725 | 0.08470911917098442 | 0.07710094843144275 | 0.08751487006100385 | 0.15404275789668376 | 1.040905952611656 | 1.0712915032145511 | 0.07100639058515815 | 0.39451893814144784 | 0.0353 | 0.1153220291715905 | 0.0658249394568288 | 1.159469426853421 | 5.434874897447202 | 26.537136907432146 | 58.66240487326016 | 4.6180858715348405 | 128.442461189475 | 0.017942437602176023 | 0.04265567157659175 | 0.00934943868941965 | 0.15875638267781322 | -0.01271993149832526 | 0.0021256264085103057 | 0.0021256264085103282 | 0.08042779146316989 |
| Environmental & Waste Services | 344 | 0.09849937500000001 | 0.10326787383667504 | 0.11623827276818133 | 0.21080225234559513 | 0.8679019283602359 | 1.0140033069350232 | 0.06770659047945733 | 0.3524691931160971 | 0.0353 | 0.24776005942461762 | 0.057392220161991594 | 1.2571207546733698 | 2.7959298193754965 | 14.656568648465615 | 26.1570797077737 | 3.144748395514224 | 86.82227240923604 | 0.11383407503502893 | 0.09873079754629571 | 0.06589114536590492 | 1.0994698185737106 | 0.05782772265833795 | 0.9362763471053946 | 0.9362763471053946 | 0.10445466044930429 |
| Farming/Agriculture | 410 | 0.06194767361111108 | 0.06761446389584813 | 0.07418344230902338 | 0.19350964755693048 | 0.7077344411836932 | 0.8936053186618897 | 0.06077166635492484 | 0.3071716621493304 | 0.0353 | 0.31685744471309574 | 0.049778121025404146 | 1.2219439380942514 | 1.446836688910868 | 14.10566169306754 | 20.684220239893335 | 2.301113053186465 | 50.26083158717105 | 0.1549072897604784 | 0.0580168189215617 | 0.036775287398929934 | 0.5379964376059525 | 0.09451890837834413 | 0.40754280163089707 | 0.40754280163089707 | 0.06879024848332839 |
| Financial Svcs. (Non-bank & Insurance) | 1096 | 0.0898048948106592 | 0.09170347877158057 | 0.005192044272108589 | 0.18413512117724837 | 0.16420934370708237 | 0.8046943673782855 | 0.055650395560989246 | 0.29683347769977464 | 0.0353 | 0.8572075347797116 | 0.030299095142382437 | 0.06621205658399419 | 17.207044491329235 | 113.75739635310738 | 154.76750093060386 | 1.4189051169891547 | 67.24273883378044 | NA | 0.05911366686335692 | 0.08108812194805326 | 1.1718657109301276 | 0.1395851811891469 | 0.279793470613296 | 0.27979347061329607 | 0.09136336041634084 |
| Food Processing | 1322 | 0.07059465314834579 | 0.09415928915164211 | 0.1396656518417869 | 0.21667817241269927 | 0.7073301892505268 | 0.7845502233355475 | 0.05449009286412754 | 0.2694701238423807 | 0.0353 | 0.1892237742349077 | 0.04911349178553133 | 1.7218024356757367 | 1.869758031832264 | 14.141587050804027 | 19.484294866563495 | 3.034811606521128 | 72.32340694019413 | 0.09335284871599672 | 0.0468262254153033 | 0.03140010313574586 | 0.44803841684065737 | 0.13027600894669486 | 0.47239492007148565 | 0.47239492007148565 | 0.0948071219870837 |
| Food Wholesalers | 155 | 0.04761357142857144 | 0.018836296708560765 | 0.0769413243038743 | 0.24769059632810453 | 0.5416663968973806 | 0.755278734108514 | 0.0528040550846504 | 0.3009347792549209 | 0.0353 | 0.4407228023955713 | 0.041024440224668335 | 4.774107292619259 | 0.4467977917156276 | 12.840125372920806 | 23.741133675188834 | 2.0698104807238042 | 43.341589180279904 | 0.04303058874505076 | 0.01326533283554843 | 0.016426556508702735 | 0.6853471845092919 | 0.015973162534866574 | 3.0430782041658815 | 3.0430782041658815 | 0.018561170869412665 |
| Furn/Home Furnishings | 357 | 0.047406903765690386 | 0.07159892354838619 | 0.1494832105705743 | 0.18096652473002495 | 1.0241862469995968 | 1.0122029505682673 | 0.0676028899527322 | 0.2809329378925945 | 0.0353 | 0.1493232870393652 | 0.061401974670029814 | 2.3687307251840988 | 1.677304280258096 | 15.593919289334458 | 22.641560665659384 | 3.6072382991315286 | 40.27418076728882 | 0.0415641769750507 | 0.034304214057021505 | 0.01546938021201274 | -0.06369336810865801 | 0.11898775988900899 | 0.5873283917301526 | 0.5873283917301526 | 0.07403676661408572 |
| Green & Renewable Energy | 226 | 0.12060146551724132 | 0.3436615440206193 | 0.0723040735009171 | 0.16204325520177662 | 0.6934742009209247 | 0.9463745341990184 | 0.06381117316986346 | 0.3114915975858737 | 0.0353 | 0.3572698659748869 | 0.05032957220861245 | 0.2354352941964785 | 8.97167183322528 | 15.684857834720361 | 25.873765615835435 | 2.121699539751118 | 194.2438753961279 | 0.06857081034183446 | 0.2723030606131439 | 0.16008202027903226 | 0.6927352463949107 | 0.0725009138274475 | 1.0712287482913938 | 1.0712287482913938 | 0.34260304920099577 |
| Healthcare Products | 816 | 0.12113916666666663 | 0.144705854680734 | 0.13144364062566824 | 0.1635127416209039 | 0.9284236857290972 | 0.9577619553752513 | 0.06446708862961448 | 0.383156666118089 | 0.0353 | 0.08867851486125819 | 0.06106263366066997 | 0.9649960298700515 | 6.506148500542282 | 27.02181813357982 | 42.652328601369675 | 5.478751101874931 | 421.868988690934 | 0.2502067956749908 | 0.05250165758823701 | 0.07861055196196585 | 0.7836379385948444 | 0.1055608332907397 | 0.3716695215235935 | 0.37166952152359345 | 0.14678848552962961 |
| Healthcare Support Services | 413 | 0.12889150442477879 | 0.0501541588809329 | 0.265545550294607 | 0.24082720013969547 | 0.7551857751051636 | 0.87059608465776 | 0.05944633447628697 | 0.3320149092308395 | 0.0353 | 0.24769890907542982 | 0.05118056627790848 | 6.243759438961222 | 0.7284689392198032 | 10.847079800290684 | 14.31169370730497 | 2.6446384411468586 | 86.37521626570474 | -0.01685083027939961 | 0.009905460656722284 | 0.008352145523242422 | 0.21963153396471125 | 0.14369234144227325 | 0.2927052140139472 | 0.2927052140139472 | 0.049236607147722204 |
| Heathcare Information and Technology | 423 | 0.15792810256410247 | 0.1287998312727684 | 0.14923014613029265 | 0.17031472234355802 | 0.97133553640996 | 0.9972417693955472 | 0.06674112591718352 | 0.40100567320191943 | 0.03948 | 0.07736911846113322 | 0.06383380721689734 | 1.1849469547433327 | 8.660472994566351 | 36.65710465359902 | 61.78365814061515 | 8.084343788382578 | 117.84884991076231 | 0.2206925931375152 | 0.05528084345393012 | 0.02783484087912103 | 0.40648092120088497 | 0.12878899822363232 | 0.14170023353348848 | 0.14170023353348848 | 0.13464518789154892 |
| Homebuilding | 167 | 0.06433782945736434 | 0.10443997100670073 | 0.09504263018098238 | 0.22592952506397226 | 1.15829842401638 | 1.3074955260239107 | 0.08461174229897726 | 0.2833287411588534 | 0.0353 | 0.2901351779264224 | 0.06762849620687786 | 1.2643564168022239 | 1.2128871862586506 | 9.926169001878376 | 12.77400128588857 | 1.5682864771736835 | 174.93405380702026 | 0.6080582917578619 | 0.010310107698711827 | 0.012154285274957153 | 0.17365130991782143 | 0.13346953779498932 | 0.21559760760017976 | 0.21559760760017976 | 0.09415453994673514 |
| Hospitals/Healthcare Facilities | 216 | 0.057736644295302016 | 0.09263246658822868 | 0.08537235413834134 | 0.21652669275093028 | 0.6571476212889761 | 0.8602387781690174 | 0.0588497536225354 | 0.2717488781489348 | 0.0353 | 0.3402545081953642 | 0.04769837362997949 | 1.156761339311659 | 2.664429820044965 | 15.137243581830917 | 27.531995484459397 | 4.6133226053635505 | 80.43798290986813 | 0.039870889157123175 | 0.07075277058407965 | 0.02409181370053029 | 0.15271446938321112 | 0.06710617664030664 | 0.6126621759157449 | 0.6126621759157449 | 0.08672812648807358 |
| Hotel/Gaming | 641 | -0.009498008474576271 | -0.057502661812593864 | -0.030280355968965215 | 0.20950361172276596 | 0.8472227190304773 | 1.090026993734096 | 0.07208555483908394 | 0.31461340725880804 | 0.0353 | 0.35181874999791884 | 0.05589856946769923 | 0.45578215616842904 | 5.260045195437387 | 30.70040958152282 | NA | 2.916215199759927 | 125.16336052023325 | 0.006466674795165275 | 0.13807782806300675 | 0.0579999347287853 | NA | -0.14748529661620288 | 0.013777250879214746 | 0.013777250879214775 | -0.07149583521919455 |
| Household Products | 568 | 0.0594598761609907 | 0.15820258326561418 | 0.22372859735810136 | 0.23560669219940256 | 0.8717875265869961 | 0.9088701906140632 | 0.06165092297937004 | 0.35238610342639226 | 0.0353 | 0.10628214020009465 | 0.057869955718704486 | 1.588285814432605 | 3.8447764903630572 | 18.642932971149786 | 23.869352920980948 | 6.1323586699133354 | 73.08995461654715 | 0.056268596375048836 | 0.03602199173681105 | 0.03138496946508878 | 0.19934316355132445 | 0.16796405774858486 | 0.6542020837371743 | 0.6542020837371743 | 0.15887069513763688 |
| Information Services | 244 | 0.15574862595419844 | 0.20182645524700482 | 0.21092627951971957 | 0.20715442478367135 | 1.141318939194461 | 1.1784026677580446 | 0.07717599366286337 | 0.3854074301545758 | 0.0353 | 0.08747410021429676 | 0.07270607731839915 | 1.2043786540585535 | 9.665671234659511 | 32.31057446719368 | 46.24812821916358 | 8.324239310226748 | 62.48286092529231 | 0.04484478679684489 | 0.030687127151268905 | 0.003451626292730319 | -0.0035999337262954813 | 0.13120933947351837 | 0.3455620858146772 | 0.3455620858146772 | 0.20264065412192425 |
| Insurance (General) | 220 | 0.05634541666666665 | 0.08441147836787613 | 0.10302496663851407 | 0.23030529198316071 | 0.6609391585431089 | 0.7537223938093799 | 0.052714409883420285 | 0.23272027545347965 | 0.028699999999999996 | 0.3212164501575006 | 0.04259168465121018 | 1.449513575954447 | 1.0440686718821062 | 9.334371645143012 | 12.245819694385553 | 1.2333989119701083 | 72.14469593691938 | -0.03141636931151894 | 0.007046341742634903 | -0.003724885894737316 | -0.15000429057772613 | 0.07198488151241526 | 0.462744909587967 | 0.462744909587967 | 0.08449602170434296 |
| Insurance (Life) | 133 | 0.09316283018867924 | 0.09678556538135037 | 0.10700627475871892 | 0.1610078319937726 | 0.9646892900671663 | 1.0009130721259367 | 0.06695259295445395 | 0.23853805321034321 | 0.028699999999999996 | 0.4924450783300975 | 0.044422293520296856 | 1.2996375403888412 | 0.9106872155117317 | 8.593636720133048 | 9.210219926577075 | 0.9498938541546095 | 52.06885257075531 | -1.0439527494357963 | 0.0056241715500413535 | 0.004368158362390044 | 0.6324134646084827 | 0.07891140288038069 | 0.4564103111000501 | 0.45641031110005015 | 0.09679334132803674 |
| Insurance (Prop/Cas.) | 229 | 0.043124891304347816 | 0.08339901141603052 | 0.09446806914861561 | 0.19801392597572173 | 0.654703856455113 | 0.7229195692595527 | 0.05094016718935024 | 0.24512185999972827 | 0.028699999999999996 | 0.24163976840889187 | 0.04375392680871412 | 1.334310392036499 | 1.037640063894711 | 9.568707734556885 | 11.604261411844687 | 1.2187240683339138 | 26.18470472273216 | -0.39684602981822165 | 0.008615413571998494 | 0.0005928121885339603 | 0.13845036464541077 | 0.07402299799580685 | 0.46016618765259676 | 0.46016618765259676 | 0.08339273377303792 |
| Investments & Asset Management | 1234 | 0.09609849794238684 | 0.17100771031174963 | 0.046153342880509034 | 0.21142347839020378 | 0.5496927154725375 | 0.7845243327653025 | 0.05448860156728143 | 0.30369873311812645 | 0.0353 | 0.4481458066827532 | 0.041755662613995166 | 0.29173714122735234 | 5.789814236623464 | 18.3054304679237 | 23.235396857603682 | 1.5435732528554318 | 198.8736159724429 | NA | 0.02431330863216957 | 0.06223805446028311 | 0.5792688751272149 | 0.07243692555462167 | 0.6726533423773673 | 0.6726533423773673 | 0.1701751324389026 |
| Machinery | 1385 | 0.03574917903066273 | 0.07818033856902394 | 0.0954793856056466 | 0.23825619324132302 | 1.0733563446039929 | 1.1119310657993697 | 0.07334722939004369 | 0.2733722514093022 | 0.0353 | 0.14536554264149013 | 0.06647563746863933 | 1.4056883069110573 | 2.2171526556283028 | 17.093035579406454 | 27.39778004012002 | 3.054559899632621 | 87.49748799842052 | 0.2630743779833235 | 0.042522639050687386 | 0.034695606907674835 | 0.48139571916221713 | 0.07474191627607292 | 0.5622432371085997 | 0.5622432371085997 | 0.080082959671066 |
| Metals & Mining | 1620 | 0.15564490683229823 | 0.08099218223657793 | 0.0865142067301867 | 0.3130462030210996 | 0.8290093911238976 | 0.9682334837445484 | 0.06507024866368599 | 0.5380452152659055 | 0.03948 | 0.2672545975700434 | 0.05547410548725259 | 1.1012033100705725 | 1.6387589778053513 | 10.199381830776048 | 19.251610285711003 | 1.9822301557157571 | 175.1044987455909 | 0.10385805243346732 | 0.0805289049519866 | 0.04114956166567166 | 0.8851443011547651 | 0.03613573760842866 | 1.7998077354931796 | 1.7998077354931796 | 0.08157623220081785 |
| Office Equipment & Services | 148 | 0.03173081081081082 | 0.06681498530028931 | 0.106868494381812 | 0.2623483628670444 | 1.006404408347355 | 1.04061227843863 | 0.06923926723806509 | 0.2931484770507266 | 0.0353 | 0.2016683934441601 | 0.060534622661886826 | 1.9088819783660118 | 1.1585597192864 | 10.517703746078713 | 16.80864058668698 | 2.1382695836214745 | 35.76073792081617 | 0.12522881738234767 | 0.02306010936166831 | 0.0035955351939908277 | 0.01649843021718488 | 0.06871744748105728 | 0.5825875048926391 | 0.5825875048926391 | 0.06661131960335742 |
| Oil/Gas (Integrated) | 49 | 0.007351463414634147 | 0.06252556689950099 | 0.04590053350214165 | 0.4513652944515794 | 1.0784866590681668 | 1.2711173449593738 | 0.08251635906965993 | 0.24704063022857292 | 0.028699999999999996 | 0.2596922609263629 | 0.06659315433874728 | 0.8538369977565511 | 1.660873383545431 | 9.646050314224087 | 26.37762169078243 | 1.5892205099596308 | 45.520538800951364 | 0.01876130226756612 | 0.11179618510887376 | 0.003423742949072911 | -0.17524038955800547 | -0.01428484689581434 | 0.014475627028430147 | 0.014475627028430194 | 0.06295332949919145 |
| Oil/Gas (Production and Exploration) | 765 | 0.06673129834254139 | -0.07497951056488074 | -0.021942125991481487 | 0.4103022773236194 | 0.9311569725891855 | 1.312032788531789 | 0.08487308861943105 | 0.5071143236628101 | 0.03948 | 0.40389839932705973 | 0.06237222681467201 | 0.31875987970857345 | 2.7822729517139697 | 6.10771814744925 | NA | 1.048950330651544 | 52.885257417390406 | -0.0005090366417228736 | 0.3225934817169848 | -0.1377980207724487 | NA | -0.21044027879950497 | 0.008332941087518118 | 0.008332941087518142 | -0.07116728076745936 |
| Oil/Gas Distribution | 204 | 0.09682361842105262 | 0.16791450682916975 | 0.08068303310224383 | 0.10935148833870346 | 0.6460413399479771 | 1.1410741205323776 | 0.07502586934266495 | 0.3131478445564459 | 0.0353 | 0.5240843743366759 | 0.04937206534363353 | 0.535137661141986 | 2.3767141676513144 | 9.220482403857291 | 14.139492936348553 | 1.1875477581713811 | 26.720608206799174 | 0.04750895217518948 | 0.1359248532525583 | 0.05775551358070285 | 0.42130021006085205 | 0.05245003509824698 | 2.0187121806587864 | 2.0187121806587864 | 0.16756757531796393 |
| Oilfield Svcs/Equip. | 513 | -0.022513019943019998 | 0.012732821776313276 | 0.021184430469070606 | 0.1475596772093498 | 0.9101608921339075 | 1.2272852849455207 | 0.07999163241286199 | 0.37623190538611695 | 0.0353 | 0.38264705229440676 | 0.05936101668866732 | 1.6461650636765661 | 0.8462725394271224 | 12.814444848422259 | 54.87171029545358 | 1.4077579768604562 | 35.051665639752855 | 0.06959284734924201 | 0.049458459419800815 | 0.01852825198188469 | 0.9028446789713837 | -0.12478769836405747 | 0.005297750006321492 | 0.005297750006321489 | 0.013848175464534504 |
| Packaging & Container | 412 | 0.02806399361022365 | 0.08804801221910473 | 0.10178597731007138 | 0.23864860403676158 | 0.7071919893044979 | 0.8828357360378839 | 0.060151338395782114 | 0.2867769605043152 | 0.0353 | 0.3039520233345641 | 0.049794103779296744 | 1.3541364004470926 | 1.6641896493621446 | 10.826582116570467 | 18.627664835468295 | 2.722140474835705 | 35.86775850819938 | 0.11429810826297121 | 0.06043937002078969 | 0.02395867605134147 | 0.28169823761335094 | 0.10064848137749706 | 0.5327549018222129 | 0.5327549018222129 | 0.08925267708413802 |
| Paper/Forest Products | 287 | 0.03252789473684211 | 0.07026270783658912 | 0.05384093266919172 | 0.22556317729487382 | 0.78438278848567 | 1.0127509460670638 | 0.06763445449346288 | 0.2943852876274353 | 0.0353 | 0.3515123723957232 | 0.053026182227726995 | 0.8704559426076012 | 1.5672227102312852 | 10.991859737512723 | 21.675130000386094 | 1.4651092432023394 | 159.36105337962837 | 0.18689597808612965 | 0.07356133913464612 | 0.026641147244268252 | 0.17012378409593912 | 0.049568531155455606 | 0.5965708023624549 | 0.5965708023624549 | 0.07066603412132974 |
| Power | 553 | 0.06416361233480179 | 0.13383292253248166 | 0.06148511546223197 | 0.1969090398801272 | 0.5100482281134904 | 0.8230453544536388 | 0.05670741241652959 | 0.2241267021692613 | 0.028699999999999996 | 0.4835085700319804 | 0.03953960783439091 | 0.5544837874271533 | 2.4391340190746416 | 10.024515704542777 | 18.186634474714506 | 1.3490838922280772 | 25.262992128402374 | 0.021055139607578925 | 0.17478004662950275 | 0.08634167069869854 | 0.8524751009953019 | 0.07313350812780546 | 0.8159127219374034 | 0.8159127219374034 | 0.13381221841430968 |
| Precious Metals | 922 | 0.35804587677725125 | 0.19254638587743905 | 0.14340915346960495 | 0.2774940635145083 | 0.8668060224206355 | 0.8941949739133607 | 0.06080563049740957 | 0.5477937365981371 | 0.03948 | 0.12607061524508933 | 0.05681653504048707 | 0.7735602487226662 | 3.517191568537293 | 9.826234640496189 | 16.60011252595551 | 2.5262624612889852 | 63.02873161414072 | 0.1272947072260593 | 0.13901228111964897 | 0.08187156661836856 | 0.781629126487647 | 0.0785698251482008 | 0.45147786660172823 | 0.4514778666017283 | 0.1929942938695585 |
| Publishing & Newspapers | 349 | -0.0028980303030302934 | 0.05311093360708903 | 0.06744803896370061 | 0.17117068641900787 | 0.8413789216293962 | 0.8921015757879442 | 0.06068505076538559 | 0.29133936354608264 | 0.0353 | 0.26366196503726563 | 0.0515599894353257 | 1.4459996435778888 | 1.195613888304771 | 11.159749707403003 | 21.710068056077088 | 1.4320864259085992 | 42.53671620701574 | 0.13099245685414607 | 0.03202400619258669 | 0.014607083829178549 | 0.4075214286624949 | -0.007561701114108308 | 0.005351799022608235 | 0.0053517990226081835 | 0.05292024349792354 |
| R.E.I.T. | 799 | 0.08601998198198194 | 0.3319219992416578 | 0.028770244081453056 | 0.03281903238390018 | 0.6576554717540797 | 0.9730814698066932 | 0.06534949266086552 | 0.23991832658607432 | 0.028699999999999996 | 0.41473145740192324 | 0.04703959539077486 | 0.09712516379373877 | 13.479584121122995 | 23.079362984011247 | 38.37480306230855 | 1.6184680498795514 | 44.44678943888325 | 0.6330253938573194 | 0.0539671559585923 | -0.014477526167262103 | -0.009996460952430954 | 0.007957506785963003 | 8.233638011708138 | 8.233638011708138 | 0.3034907362040781 |
| Real Estate (Development) | 890 | 0.06888012698412697 | 0.17309142985975756 | 0.08284031813191539 | 0.35866183116359035 | 0.5229773863704421 | 0.9438599147641852 | 0.06366633109041707 | 0.26438414331101134 | 0.0353 | 0.6374976971549685 | 0.03970265170973006 | 0.5710305709197759 | 1.8547413109907804 | 9.483678422826525 | 10.169019132006383 | 0.6802799716905636 | 62.6265842492542 | 1.9282397527828392 | 0.030484546501111057 | 0.034722096325413634 | 1.037173197114842 | 0.10436126084927606 | 0.6921286289282714 | 0.6921286289282714 | 0.17305495372407725 |
| Real Estate (General/Diversified) | 364 | 0.05410121311475408 | 0.16292815008764083 | 0.038877756570155166 | 0.31953806046087424 | 0.5974495419983722 | 0.9921666342329557 | 0.06644879813181824 | 0.2440071950568731 | 0.028699999999999996 | 0.530888644106923 | 0.04242709135731382 | 0.284060436055407 | 3.348591030148532 | 13.556066545288195 | 19.50397400995738 | 0.7347476840364257 | 99.04468488174223 | 0.9891589717371361 | 0.10068085437466272 | 0.08866378119584013 | 1.365704367203274 | 0.039049595073957596 | 0.8398643508300876 | 0.8398643508300876 | 0.1613931973567631 |
| Real Estate (Operations & Services) | 720 | 0.08042713665943607 | 0.23224845502814612 | 0.046013002742450404 | 0.23848763936015505 | 0.5349059557928528 | 0.8122367121362232 | 0.05608483461904645 | 0.2502594665830582 | 0.0353 | 0.4505632001805107 | 0.042564007621353206 | 0.22343757031692119 | 6.459546711372596 | 20.781192619274044 | 24.12613150820831 | 1.0773780504882806 | 58.529352569681656 | 0.2153538872214986 | 0.03245264403436725 | 0.058415095055054524 | 0.3631696307983389 | 0.05084537870279203 | 0.4888921912408715 | 0.48889219124087147 | 0.24067439829514758 |
| Recreation | 331 | 0.00428597345132745 | 0.08047959213278184 | 0.06670987773491634 | 0.24965599001655334 | 0.9346070560540213 | 1.011760959183012 | 0.06757743124894149 | 0.33210412200889905 | 0.0353 | 0.2003215277363509 | 0.05926382317327645 | 0.9469442025791535 | 3.3730539906020716 | 20.530262823460074 | 39.2574982166704 | 3.7015014835215094 | 71.57119852318591 | 0.34595963119417467 | 0.06910313753947105 | 0.06927601925298026 | 1.4473768355146879 | 0.02792097787371199 | 1.9260136266613193 | 1.9260136266613193 | 0.07975210556387026 |
| Reinsurance | 37 | 0.042927096774193554 | 0.03797897697445781 | 0.05177097304394431 | 0.1375841522124885 | 1.2520897822012522 | 1.2696688592443122 | 0.08243292629247238 | 0.28791202923342046 | 0.0353 | 0.23724363082006256 | 0.06906263057378698 | 1.534486780269337 | 0.6681798002192456 | 11.422737106280737 | 13.94519406019538 | 0.9052509628902821 | 188.4398961922008 | -0.4117942650256345 | 0.0016419803986456364 | -7.55666654806784e-05 | 0.25394574631979033 | 0.033419604200959754 | 0.9349143594359081 | 0.9349143594359081 | 0.03781185855620412 |
| Restaurant/Dining | 379 | -0.0052900396825396835 | 0.060159209417432434 | 0.05416078268419203 | 0.2091900398213581 | 0.9039754916807023 | 1.098013369120579 | 0.07254557006134535 | 0.31963507648362244 | 0.0353 | 0.26738881524164293 | 0.06012015619062337 | 1.4588560793159122 | 3.3652569110653676 | 22.801882704261608 | 80.66185047469637 | 16.00917100117888 | 127.2499841457048 | -0.0035887537620460535 | 0.04873834821918264 | 0.006965113453039727 | 0.34964872209516107 | 0.051712395508900395 | 4.595024282344413 | 4.595024282344413 | 0.04026638071788824 |
| Retail (Automotive) | 185 | 0.035018931297709915 | 0.04896505854141559 | 0.08395232222708361 | 0.236612639000007 | 0.8198056108284281 | 1.0700510989492495 | 0.07093494329947678 | 0.304837461835144 | 0.0353 | 0.3459779923356545 | 0.055414774216004 | 2.2807705591323653 | 0.9584243623480845 | 11.88931397167438 | 19.810087509167047 | 3.3757801421974696 | 43.313102504874884 | 0.11513950156342101 | 0.023019766495647943 | 0.015418598616611984 | 0.0039266418788244835 | 0.13992124464706138 | 0.3641534771044252 | 0.36415347710442525 | 0.04449359451236929 |
| Retail (Building Supply) | 90 | 0.028206250000000002 | 0.11623659269182686 | 0.24982671398153575 | 0.24939746537409957 | 1.056717304804078 | 1.144396017309487 | 0.07521721059702645 | 0.28186126519449634 | 0.0353 | 0.17020372300281458 | 0.06685321232295671 | 2.7781158448277607 | 1.8438475036111974 | 12.32962170710272 | 16.215827826771573 | 10.725438237273437 | 46.21141166352574 | 0.05315621125268974 | 0.02077152599390211 | 0.0005123140800056243 | -0.25475018889805434 | 0.5515778855152732 | 0.4342473472327862 | 0.43424734723278613 | 0.11364826473151755 |
| Retail (Distributors) | 1022 | 0.06620903713892705 | 0.036528182814979986 | 0.052280262972447665 | 0.23158351463796487 | 0.5682992106428517 | 0.8305862333635267 | 0.057141767041739136 | 0.29102214535003457 | 0.0353 | 0.46284679439490467 | 0.04276312726419868 | 1.675329296928518 | 0.8082701612334082 | 13.452513353995348 | 21.203287593586882 | 1.3981699880791132 | 66.68019881687596 | 0.1531002463269937 | 0.030185904977333783 | 0.024509913421407365 | 0.42864874122544977 | 0.05730397944045916 | 0.7554637145830954 | 0.7554637145830954 | 0.036833456488232046 |
| Retail (General) | 217 | -0.011407988826815652 | 0.043138262543505806 | 0.0866373320384371 | 0.26860119219565864 | 0.8360116928977362 | 0.9926297249656834 | 0.06647547215802337 | 0.2572793768540807 | 0.0353 | 0.26948287835953866 | 0.05558853575978981 | 2.713833167458637 | 0.9645012637757063 | 12.760976623828352 | 24.542236626760943 | 3.3377367920575516 | 61.885892413707744 | -0.018599070726929373 | 0.024105534937314807 | 0.0018030789783290541 | -0.15302365996144848 | 0.09988944229296311 | 0.5581437059719203 | 0.5581437059719203 | 0.038765642590881264 |
| Retail (Grocery and Food) | 171 | 0.037350583941605835 | 0.04309429895098543 | 0.11086978401287294 | 0.2533277378926875 | 0.46899598303943174 | 0.6209083788726557 | 0.045064322623064965 | 0.21914600518311636 | 0.028699999999999996 | 0.37545613633961356 | 0.036104575319381035 | 3.3962154280606267 | 0.6354420392317874 | 9.046225745213576 | 15.416222137347557 | 2.2766364814256095 | 53.40403630226628 | -0.03313668225107744 | 0.02646375324837432 | 0.004593110317627414 | 0.24827958855405888 | 0.11408848077040329 | 0.4707300526294422 | 0.47073005262944223 | 0.04111384301504433 |
| Retail (Online) | 356 | 0.13381464864864856 | 0.0475017946768988 | 0.08668534222796066 | 0.14081453314852424 | 1.3114219547764037 | 1.311385754427996 | 0.08483581945505257 | 0.3983872847144697 | 0.0353 | 0.05737693177263693 | 0.08146436761467006 | 1.7599439509309411 | 5.063373506843167 | 36.22568845459988 | 91.76872979263466 | 8.839980484615392 | 110.83377838843676 | -0.029669413385307424 | 0.06358444118758247 | 0.03987692127301868 | 0.9819980950066997 | 0.14894789455396087 | 0.050312735130040975 | 0.050312735130040975 | 0.053846064430240315 |
| Retail (Special Lines) | 480 | 0.015052514124293804 | 0.03469280758405615 | 0.0639307330803434 | 0.2742014187130554 | 0.9588475188774988 | 1.0890217337097654 | 0.07202765186168249 | 0.320353573893323 | 0.0353 | 0.2528564569561445 | 0.0604085077948655 | 2.236088756499614 | 1.3044020396015177 | 14.286604286405765 | 38.133243189816746 | 4.053750466850901 | 38.35879244242442 | 0.06055278117437554 | 0.017110484458779003 | -0.006444298860516757 | -1.0135662397922771 | 0.022919820972104276 | 2.0173268130575543 | 2.0173268130575543 | 0.03317893941801664 |
| Rubber& Tires | 92 | 0.003056212121212122 | 0.056216340825908664 | 0.04422351706839217 | 0.2995235621339244 | 0.8586946281144724 | 1.0440216408610408 | 0.06943564651359595 | 0.25607853647573625 | 0.0353 | 0.34330448992494217 | 0.05455012294741398 | 0.9994159450853716 | 1.1802286452530013 | 8.394919525830648 | 20.156345820775165 | 1.3309983571384347 | 30.654901894650372 | 0.19354105745315298 | 0.05471680145457201 | 0.011382795561056465 | -0.1249399737415639 | 0.02650083131980971 | 1.1037913523011518 | 1.1037913523011518 | 0.05390033807179412 |
| Semiconductor | 565 | 0.045546287703016206 | 0.1819255442909072 | 0.13957824407992553 | 0.12092342441406735 | 1.4320884315366331 | 1.4604657403163814 | 0.09342282664222357 | 0.3240033562622677 | 0.0353 | 0.08494679491689297 | 0.0877019389152905 | 0.7982182901690509 | 5.955689073720818 | 17.813177456921434 | 31.938803435592277 | 5.311810939169272 | 254.64890293126535 | 0.16627383510342844 | 0.15668921634728375 | 0.14784538643129233 | 1.0165541100549904 | 0.16885649393948046 | 0.4442119526050973 | 0.4442119526050974 | 0.191549362181733 |
| Semiconductor Equip | 308 | 0.07149727699530514 | 0.18844245302525117 | 0.18607449770217854 | 0.16105200100995765 | 1.7312795141670492 | 1.725312705976888 | 0.10867801186426874 | 0.3370362624649953 | 0.0353 | 0.059052605831114234 | 0.1038001543125777 | 1.0826223177464123 | 5.57531562280028 | 22.85963102263472 | 29.164732876275398 | 6.6997819372687974 | 84.83288877889781 | 0.29828142612368935 | 0.05957357751597131 | 0.036570509984575755 | 0.38196691385749265 | 0.2138047091400965 | 0.31507257362441277 | 0.31507257362441277 | 0.19694364226538294 |
| Shipbuilding & Marine | 353 | 0.015926799999999998 | 0.08175857670457888 | 0.04967320087955309 | 0.19102891193397079 | 0.7633616944643629 | 1.02883186828969 | 0.06856071561348615 | 0.2629035504109872 | 0.0353 | 0.40193307768280934 | 0.0514847473251173 | 0.6839294871606224 | 1.9276378810897623 | 11.541776817028166 | 22.599930441373402 | 1.2412284068863078 | 915.7718578708901 | -0.0006801338277724659 | 0.094533054043487 | 0.03221660940280553 | 0.4271857123197109 | 0.05681468224311345 | 0.6179283552913896 | 0.6179283552913896 | 0.0835311038342106 |
| Shoe | 79 | -0.05895081967213116 | 0.06258032148626948 | 0.09454294865663851 | 0.18568679154226103 | 0.9862424204588389 | 1.0070690763979555 | 0.06730717880052224 | 0.2935206920243487 | 0.0353 | 0.09130352046550465 | 0.06354263706647913 | 1.7204343077244941 | 3.7349267766834107 | 33.74668593003162 | 60.068377128714154 | 7.744121034560733 | 108.91796356952068 | 0.19765000133103522 | 0.016273876099341878 | -0.01445307353723201 | -0.3975997882656982 | 0.09950648639896924 | 0.6538213143299318 | 0.6538213143299318 | 0.06157539954163352 |
| Software (Entertainment) | 339 | 0.08143351145038165 | 0.19779940546390076 | 0.13999901760611586 | 0.1392684760367291 | 1.1300805915396532 | 1.1310278949888313 | 0.07444720675135669 | 0.42350712300861326 | 0.03948 | 0.04067089682365539 | 0.0726054930785368 | 0.7264761045966572 | 7.991226951252645 | 25.76099250146309 | 38.87610772016263 | 5.951365040640641 | 122.10940688102315 | 0.015369657864021155 | 0.10826051026723006 | 0.07120572983792296 | 0.5113295441982466 | 0.1841635095401823 | 0.03723349362250475 | 0.03723349362250472 | 0.210463976208952 |
| Software (Internet) | 155 | 0.23828485714285713 | 0.036440699845695444 | 0.05509440812375373 | 0.12492018675446852 | 0.9315669326828552 | 0.9466092053447701 | 0.06382469022785876 | 0.3476714612128289 | 0.0353 | 0.07087500540286507 | 0.06114925940025879 | 1.2628020819928294 | 11.15136637631543 | 44.20754435861171 | 185.24787691360976 | 12.485508913370875 | 118.92128965027622 | 0.019769669327639496 | 0.10426588483661711 | 0.09533660835921416 | 4.147346101449111 | -0.056416708432936453 | 0.003173308092368274 | 0.0031733080923682655 | 0.047170308121622366 |
| Software (System & Application) | 1478 | 0.1436631781914894 | 0.19819486778469864 | 0.19306860147523508 | 0.15879470254168898 | 1.061330895451685 | 1.0751764312841539 | 0.07123016244196725 | 0.4058604376773745 | 0.03948 | 0.059969594038213246 | 0.06870746432134729 | 0.9757205468594601 | 10.192194994552144 | 30.91577752733774 | 44.66091268297033 | 11.121994295690284 | 187.92052246866453 | 0.13524265747327346 | 0.05649354007628566 | 0.05987275775319205 | 0.43792853888115507 | 0.20372488699604252 | 0.33252734321217636 | 0.33252734321217636 | 0.21440565747924 |
| Steel | 718 | 0.057176514598540125 | 0.044113221112797744 | 0.04542911010162443 | 0.2527171290774104 | 0.933124990188395 | 1.1722376504299339 | 0.07682088866476419 | 0.30402847090654683 | 0.0353 | 0.362697328656645 | 0.058415892999781505 | 1.144437849412679 | 0.9879917832686349 | 8.957097034404189 | 21.06345212237107 | 1.1867896318072497 | 59.31361962828615 | 0.14070318472506455 | 0.06216644784683507 | 0.03214990202153909 | 0.5037063575631194 | 0.02435911906315282 | 1.540478737936398 | 1.540478737936398 | 0.04524112420959029 |
| Telecom (Wireless) | 104 | 0.01129712328767123 | 0.14172166323860358 | 0.08578950586300499 | 0.3241602059438072 | 0.6304226924540491 | 0.8717996947672737 | 0.05951566241859496 | 0.2676900794831759 | 0.0353 | 0.40088578105945444 | 0.046110221328987955 | 0.7361487419806113 | 2.287420896022666 | 6.947353548550464 | 16.013579042440426 | 1.5538168437458335 | 46.652160068964285 | -0.06548012195076866 | 0.11574632183757574 | -0.04382283871948101 | -0.22911111777139614 | 0.08186453993691088 | 0.7755475319989686 | 0.7755475319989686 | 0.14067588103968898 |
| Telecom. Equipment | 482 | 0.08731657657657661 | 0.10811698860678298 | 0.12493117439397157 | 0.19453377106949057 | 1.0886826127954905 | 1.1027535028105426 | 0.07281860176188726 | 0.3426767022619919 | 0.0353 | 0.12662594500512964 | 0.0668997895706438 | 1.2140094925293565 | 2.5246877752794 | 15.546740875831969 | 22.163962406463337 | 3.6820040182671403 | 105.5138767138832 | 0.21751505575496946 | 0.03546076567204579 | 0.026551918368723348 | 0.28776759230536864 | 0.10415871121882829 | 0.6154918338247359 | 0.6154918338247359 | 0.11182273432588506 |
| Telecom. Services | 315 | 0.09989497652582165 | 0.15080547353352663 | 0.10274122736190537 | 0.220952576674282 | 0.5118078353492548 | 0.7840792147688006 | 0.05446296277068291 | 0.29193877430611376 | 0.0353 | 0.4501077790112539 | 0.04168581951695137 | 0.7902500769274025 | 2.159989726666743 | 6.794752492665894 | 14.388148270140736 | 1.4762161132156635 | 58.99880453145874 | 0.02265523762169849 | 0.13982079153583804 | -0.03323194279245312 | -0.22878766696941064 | 0.08778869289656513 | 0.6561752492070673 | 0.6561752492070673 | 0.14947113889296235 |
| Tobacco | 57 | 0.11853499999999999 | 0.32805054543644013 | 0.18583126680255094 | 0.288308515737265 | 0.5510383587069492 | 0.6502328263914867 | 0.046753410800149636 | 0.24629626930957138 | 0.028699999999999996 | 0.23956091766014292 | 0.040631977556552366 | 0.6785216007409167 | 3.8743720796808714 | 10.3540966009104 | 11.76634269212936 | 3.580947108277556 | 39.88743088552784 | 0.17485574794503045 | 0.02727838669696254 | -3.4168863424045765e-06 | -0.08736596130282775 | 0.19351367033332903 | 1.0588700078017717 | 1.0588700078017717 | 0.32910685241754273 |
| Transportation | 284 | 0.05639654639175257 | 0.05887231818228832 | 0.07766280127519899 | 0.2301324338638986 | 0.7671444445351495 | 0.9459671796945618 | 0.06378770955040676 | 0.2601839385224362 | 0.0353 | 0.31488860718429634 | 0.05191275649328724 | 1.5498880823873908 | 1.5288367575956143 | 13.19502000406185 | 25.126450081239827 | 2.9408871100133194 | 37.6671734602049 | 0.03961774248317611 | 0.04665036367911691 | 0.006800700489646501 | 0.21493585493956563 | 0.08264062501201731 | 0.7953594433568918 | 0.7953594433568918 | 0.0603245992298799 |
| Transportation (Railroads) | 53 | 0.017566 | 0.15267045457435474 | 0.052393215951068925 | 0.23922631739933373 | 0.6190910706898799 | 0.7815028778778556 | 0.054314565765764475 | 0.1728152690932219 | 0.028699999999999996 | 0.29206131008352504 | 0.044643283827672214 | 0.39891599725424676 | 4.831798753577469 | 17.086253630460416 | 31.01307190617256 | 2.4811895472515757 | 56.82889139903317 | 0.07990820110822126 | 0.1950041401195689 | 0.12715356895785646 | 1.1209397415275466 | 0.05655501193180012 | 0.7807991454567925 | 0.7807991454567925 | 0.156215101707636 |
| Trucking | 217 | 0.025366875 | 0.014466648377545644 | 0.004464628518474443 | 0.2760325610508961 | 0.806368916596742 | 1.0539104624207907 | 0.07000524263543755 | 0.29382378116453434 | 0.0353 | 0.3543539417654877 | 0.05443878132773132 | 0.9951000602262386 | 1.7437963135244796 | 10.053075459267033 | 68.18175003586217 | 2.675536384079602 | 35.79482789017418 | 0.05945265168327072 | 0.02421394770416182 | -0.02784022212094745 | -7.267791381409006 | -0.05758056844094958 | 0.004669969402644484 | 0.004669969402644525 | 0.007277836771987419 |
| Utility (General) | 53 | 0.0257616 | 0.11862805381356314 | 0.0665065284593002 | 0.2332520414392328 | 0.48803783479430257 | 0.7631648274815779 | 0.05325829406293889 | 0.1772973830165321 | 0.028699999999999996 | 0.4637390551336899 | 0.038391931044941666 | 0.6959111245848756 | 2.378705519069597 | 10.758421798603603 | 19.002956607631102 | 1.6685151193349903 | 37.33345084474906 | -0.012827272751673835 | 0.15369567376360188 | 0.10161823774842545 | 1.0796981588532988 | 0.05485150855276108 | 1.222793064848565 | 1.222793064848565 | 0.11793061223035635 |
| Utility (Water) | 104 | 0.08443684931506854 | 0.26786051215746653 | 0.07271210049744356 | 0.2653577150730401 | 0.5889254995125772 | 0.8279781995936756 | 0.05699154429659571 | 0.27389365083788414 | 0.0353 | 0.40893948453987256 | 0.04434900253101957 | 0.3246181507178537 | 5.010386869035395 | 12.783878973416556 | 18.44458533192589 | 1.7051069929463623 | 31.573496920080274 | 0.05292179439868498 | 0.2708939990886701 | 0.27534918016672044 | 1.7257929849519456 | 0.06299110689663923 | 0.568294114097338 | 0.753211581809748 | 0.2679357207017367 |
| Total Market | 46580 | 0.06617008784625207 | 0.08003749365632534 | 0.04943236315795192 | 0.2211610464746955 | 0.7917792561150673 | 1.0126516437334008 | 0.06762873467904389 | 0.3235676087993788 | 0.0353 | 0.38684090102653307 | 0.051554479908185194 | 0.6905705567846341 | 2.6638950424577574 | 15.836063112747448 | 27.989069142863478 | 2.2098733643239052 | 93.22244318877755 | -1.373882440248397 | 0.05877471074010732 | 0.02722663424910209 | 0.4793177223221601 | 0.06299110689663923 | 0.753211581809748 | 0.753211581809748 | 0.08093822246446525 |
| Total Market (without financials) | 41623 | 0.06414068617439965 | 0.08306242773852437 | 0.07723521333629764 | 0.22888604684744512 | 0.894132484382979 | 1.0368162847389348 | 0.06902061800096264 | 0.33075842494807123 | 0.0353 | 0.2482491205787853 | 0.05835968165603505 | 1.0351331591251673 | 2.305157992728423 | 14.331251277047636 | 26.063060552182353 | 2.7117825747567825 | 93.93077202465864 | 0.11581483197696948 | 0.06370060695985874 | 0.027532999205641173 | 0.46138853290161297 | 0.05537010105114484 | 0.9572515334251787 | 0.9572515334251787 | 0.08411142918389601 |

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
