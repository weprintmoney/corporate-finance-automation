---
title: "Ill11Airbnbipo"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/inv4ed/ill11AirbnbIPO.xlsx
---

# Ill11Airbnbipo

Source: https://www.stern.nyu.edu/~adamodar/pc/inv4ed/ill11AirbnbIPO.xlsx

Sheets: Input sheet, Valuation output, Stories to Numbers, Share Count, Diagnostics, Summary Sheet, Option value, Cost of capital worksheet, R& D converter, Operating lease converter, Country equity risk premiums, Synthetic rating, Industry Average Beta (US), Industry Average Beta (Global), Trailing 12 month, Answer keys

## Input sheet

| Date of valuation | 2020-11-01 00:00:00 | Important: Before you run this spreadsheet, go into preferences in Excel and check under Calculation options |
|---|---|---|
| Company name | Airbnb | There should be a check against the iteration box. If there is not, you will get circular reasoning errors. |
| Numbers from your base year below ( in consistent units) |  |  |
|  | This year | Last year |
| Country of incorporation | United States |  |
| Industry (US) | Hotel/Gaming |  |
| Industry (Global) | Hotel/Gaming | Last 10K |
| Gross Bookings | 26491803 | 38000000 |
| Revenues | 3625731 | 4805239 |
| Operating income or EBIT | -817906 | -501543 |
| Interest expense | 110715 | 9968 |
| Book value of equity | 1855218 | 2423817 |
| Book value of debt | 2192381 | 381374 |
| Do you have R&D expenses to capitalize? | No |  If you want to capitalize R&D, you have to input the numbers into the R&D worksheet.  |
| Do you have operating lease commitments? | No | If you have operating leases, please enter your lease commitments in the lease worksheet below and I will convert to debt |
| Cash and Marketable Securities | 4495211 | 3074272 |
| Cross holdings and other non-operating assets | 0 | 0 |
| Minority interests | 0 | 0 |
| Expected IPO Proceeds held in company | 3000000 |  |
| Number of shares outstanding = | 671064 | Counted RSUs |
| Current stock price = | 50 | Rumored price |
| Effective tax rate = | 0.25 |  |
| Marginal tax rate = | 0.25 |  |
| The value drivers below: |  |  |
| Gross Bookings growth rate for next year  | 0.4 | Recovery from COVID |
| Revenues as % of Gross Bookings next year | 0.1265 |  |
| Operating Margin for next year | -0.1 |  |
| Compounded Gross Bookng growth rate - years 2-5 = | 0.25 | Growth Lever |
| Target Revenues as % of Gross Bookings | 0.14 |  |
| Target pre-tax operating margin (EBIT as % of sales in year 10) = | 0.25 | Profitability Lever |
| Year of convergence | 10 | Speed of convergence level |
| Sales to capital ratio  (for computing reinvestment) = | 2 | Efficency of Growth Lever |
| Market numbers  |  |  |
| Riskfree rate | 0.009 |  |
| Initial cost of capital = | 0.06503197511526536 |  |
| Other inputs |  |  |
| Do you have employee options outstanding? | Yes |  |
| Number of options outstanding = | 44839 |  |
| Average strike price = | 11.43 |  |
| Average maturity = | 5 |  |
| Standard deviation on stock price = | 0.4 |  |
| Default assumptions.  |  |  |
| In stable growth, I will assume that your firm will have a cost of capital similar to that of typical mature companies (riskfree rate + 4.5%) |  |  |
| Do you want to override this assumption = | No | Mature companies generally see their risk levels approach the average |
| If yes, enter the cost of capital after year 10 = | 0.075 | Though some sectors, even in stable growth, may have higher risk. If you change your risk free rate after year 10 (see cell B57 & 58), you should incorporate it into your stable cost of capital estimate. |
| I will assume that your firm will earn a return on capital equal to its cost of capital after year 10. I am assuming that whatever competitive advantages you have today will fade over time. |  |  |
| Do you want to override this assumption = | Yes | Mature companies find it difficult to generate returns that exceed the cost of capital |
| If yes, enter the return on capital you expect after year 10 | 0.1 | But there are significant exceptions among companies with long-lasting competitive advantages. |
| I will assume that your firm has no chance of failure over the foreseeable future. |  |  |
| Do you want to override this assumption = | Yes | Many young, growth companies fail, especially if they have trouble raising cash. Many distressed companies fail, because they have trouble making debt payments. |
| If yes, enter the probability of failure = | 0.1 | Tough to estimate but a key input. |
| What do you want to tie your proceeds in failure to? | V | B: Book value of capital, V= Estimated fair value for the company |
| Enter the distress proceeds as percentage of book or fair value | 0.5 | This can be zero, if the assets will be worth nothing if the firm fails. |
| I will assume that your effective tax rate will adjust to your marginal tax rate by your terminal year. If you override this assumption, I will leave the tax rate at your effective tax rate. |  |  |
| Do you want to override this assumption = | No |  |
| I will assume that you have no losses carried forward from prior years ( NOL) coming into the valuation. If you have a money losing company, you may want to override tis. |  |  |
| Do you want to override this assumption = | Yes | Check the financial statements. |
| If yes, enter the NOL that you are carrying over into year 1 | 167600 | An NOL will shield your income from taxes, even after you start making money. |
| I will asssume that today's risk free rate will prevail in perpetuity. If you override this assumption, I will change the riskfree rate after year 10. |  |  |
| Do you want to override this assumption = | Yes | If yes, you will be asked to enter a normal risk free rate and your growth in perpetuity will be adjusted accordingly. |
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
|  | 0.4 | 0.25 | 0.25 | 0.25 | 0.25 | 0.20400000000000001 | 0.158 | 0.11199999999999999 | 0.066 | 0.020000000000000018 | 0.02 |
| 26491803 | 37088524.199999996 | 46360655.24999999 | 57950819.06249999 | 72438523.82812499 | 90548154.78515624 | 109019978.36132811 | 126245134.94241795 | 140384590.05596876 | 149649972.9996627 | 152642972.45965594 | 155695831.90884906 |
| 0.1368623721080819 | 0.1265 | 0.1292 | 0.13055 | 0.13190000000000002 | 0.13325 | 0.1346 | 0.13595000000000002 | 0.1373 | 0.13865000000000002 | 0.14 | 0.14 |
| 3625731 | 4691698.311299999 | 5989796.658299999 | 7565479.428609374 | 9554641.292929687 | 12065541.625122068 | 14674089.087434763 | 17163026.09542172 | 19274804.214684512 | 20748968.756403238 | 21370016.144351833 | 21797416.46723887 |
| -0.22558375124905847 | -0.1 | -0.02999999999999997 | 0.005000000000000032 | 0.040000000000000036 | 0.07500000000000001 | 0.0597664995003766 | 0.10732487462528245 | 0.1548832497501883 | 0.20244162487509415 | 0.25 | 0.25 |
| -817906 | -469169.83112999995 | -179693.8997489998 | 37827.397143047114 | 382185.6517171878 | 904915.6218841553 | 877018.9381126515 | 1842019.623881587 | 2985344.3150689634 | 4200454.949528833 | 5342504.036087958 | 5449354.116809717 |
| 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 |
| -817906 | -469169.83112999995 | -179693.8997489998 | 37827.397143047114 | 382185.6517171878 | 777799.3869178077 | 657764.2035844886 | 1381514.7179111904 | 2239008.2363017225 | 3150341.212146625 | 4006878.0270659686 | 4087015.587607288 |
|  | 532983.6556499996 | 649049.1735 | 787841.3851546873 | 994580.9321601563 | 1255450.166096191 | 1304273.7311563473 | 1244468.5039934786 | 1055889.059631396 | 737082.2708593626 | 310523.6939742975 | 817403.1175214575 |
|  | -1002153.4867799996 | -828743.0732489999 | -750013.9880116403 | -612395.2804429685 | -477650.7791783832 | -646509.5275718587 | 137046.21391771175 | 1183119.1766703264 | 2413258.9412872624 | 3696354.333091671 | 3269612.4700858304 |
| 167600 | 636769.83113 | 816463.7308789997 | 778636.3337359526 | 396450.68201876484 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 0.06503197511526536 | 0.06503197511526536 | 0.06503197511526536 | 0.06503197511526536 | 0.06503197511526536 | 0.06626558009221228 | 0.06749918506915921 | 0.06873279004610613 | 0.06996639502305306 | 0.07119999999999999 | 0.0712 |
|  | 0.9389389458394176 | 0.8816063440140368 | 0.8277745312938827 | 0.7772297458057962 | 0.7297712782019328 | 0.6844179272286188 | 0.641141404884799 | 0.599908050783339 | 0.5606793386912059 | 0.523412377418975 |  |
|  | -940960.9384465095 | -730625.150934008 | -620842.4773901913 | -475971.82815135765 | -348575.8196551578 | -442482.7107942851 | 87866.0021253444 | 709762.7191206843 | 1353064.4272915819 | 1934717.6092664413 |  |
| 3269612.4700858304 |  |  |  |  |  |  |  |  |  |  |  |
| 0.0712 |  |  |  |  |  |  |  |  |  |  |  |
| 63859618.55636388 |  |  |  |  |  |  |  |  |  |  |  |
| 33424914.769655306 |  |  |  |  |  |  |  |  |  |  |  |
| 525951.8324325425 |  |  |  |  |  |  |  |  |  |  |  |
| 33950866.60208785 |  |  |  |  |  |  |  |  |  |  |  |
| 0.1 |  |  |  |  |  |  |  |  |  |  |  |
| 16975433.301043924 |  |  |  |  |  |  |  |  |  |  |  |
| 32253323.271983456 |  |  |  |  |  |  |  |  |  |  |  |
| 2192381 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 4495211 |  |  |  |  |  |  |  |  |  |  |  |
| 3000000 |  |  |  |  |  |  |  |  |  |  |  |
| 0 |  |  |  |  |  |  |  |  |  |  |  |
| 37556153.27198346 |  |  |  |  |  |  |  |  |  |  |  |
| 1876546.1674490059 |  |  |  |  |  |  |  |  |  |  |  |
| 35679607.104534455 |  |  |  |  |  |  |  |  |  |  |  |
| 671064 |  |  |  |  |  |  |  |  |  |  |  |
| 53.16870984665316 |  |  |  |  |  |  |  |  |  |  |  |
| 50 |  |  |  |  |  |  |  |  |  |  |  |
| 0.9404027320619174 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | After year 10 |
|  | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |  |
| -447612 | 85371.65564999962 | 734420.8291499997 | 1522262.214304687 | 2516843.1464648433 | 3772293.312561034 | 5076567.043717382 | 6321035.54771086 | 7376924.607342256 | 8114006.878201619 | 8424530.572175916 |  |
| 1.8272655782239975 | -5.495615934326817 | -0.2446742965568842 | 0.024849462062175188 | 0.15185119988665388 | 0.20618740974565278 | 0.12956870221944952 | 0.2185582896162482 | 0.30351513069189245 | 0.3882596181437874 | 0.47562033192682196 | 0.1 |

## Stories to Numbers

| Airbnb | 2020-11-01 00:00:00 |
|---|---|
| The Story |  |
| Airbnb has brought the sharing economy to housing, connecting home owners (hosts) who own units or houses that they want to rent with renters (guests) online, collecting a percentage of the transaction revenues from both sides of the transaction. Its low capital intensity model and extended reach has allowed it to expand   not only to expand to almost every part of the world (220 countries) but also provide an unmatched range of offerings. The growth in gross bookings has started to slow down, as the company gets bigger, and the COVID shut downs made 2020 a regressive year. That said, as its competitors in the hotel business have been damaged far more by the crisis, Airbnb will be able to recover quickly from the crisis, and continue on its growth path. Economies of scale will allow for only mild improvements in revenues as a % of gross billings, but the brokerage-based business will generate high margins, in steady state, and require relatively little reinvestment. |  |
| The Assumptions |  |
|  | Link to story |
| Gross Bookings & Growth Rate | Growth continues, as hotels scale back growth plans after COVID shock. |
| Revenues as % of Gross Bookings | Mild economies of scale allow slight increase in percent over time |
| Operating margin (b) | Higher margins than the hotel business, but lower than ad driven businesses. |
| Tax rate | Global/US marginal tax rate, after NOLs are used up. |
| Reinvestment (c ) | Low capital intensity business |
| Return on capital | Networking benefits allow for high value growth |
| Cost of capital (d) | Cost of capital moves up over time. |
| The Cash Flows |  |
|  | FCFF |
| 1 | -1002153.4867799996 |
| 2 | -828743.0732489999 |
| 3 | -750013.9880116403 |
| 4 | -612395.2804429685 |
| 5 | -477650.7791783832 |
| 6 | -646509.5275718587 |
| 7 | 137046.21391771175 |
| 8 | 1183119.1766703264 |
| 9 | 2413258.9412872624 |
| 10 | 3696354.333091671 |
| Terminal year | 3269612.4700858304 |
| The Value |  |
| Terminal value |  |
| PV(Terminal value) |  |
| PV (CF over next 10 years) |  |
| Value of operating assets = |  |
| Adjustment for distress | 0.1 |
|  - Debt & Minority Interests |  |
|  + IPO Proceeds |  |
|  + Cash & Other Non-operating assets |  |
| Value of equity |  |
|  - Value of equity options |  |
| Number of shares |  |
| Value per share | Not yet listed |

## Share Count

| In millions |
|---|
| 24460092 |
| 13788876 |
| 0 |
| 9200000 |
| 37509412 |
| 84958380 |
|  |
| 7934794 |
| 6408714 |
| 181782 |
| 14525290 |

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
| Traling 12 month | 3625731 |  | -0.22558375124905847 | -817906 | 167600 | 0 | -817906 |
| 1 | 4691698.311299999 | 0.4 | -0.1 | -469169.83112999995 | 636769.83113 | 0 | -469169.83112999995 |
| 2 | 5989796.658299999 | 0.27667984189723316 | -0.02999999999999997 | -179693.8997489998 | 816463.7308789997 | 0 | -179693.8997489998 |
| 3 | 7565479.428609374 | 0.2630611455108358 | 0.005000000000000032 | 37827.397143047114 | 778636.3337359526 | 0 | 37827.397143047114 |
| 4 | 9554641.292929687 | 0.2629260819609345 | 0.040000000000000036 | 382185.6517171878 | 396450.68201876484 | 0 | 382185.6517171878 |
| 5 | 12065541.625122068 | 0.26279378316906743 | 0.07500000000000001 | 904915.6218841553 | 0 | 127116.23496634758 | 777799.3869178077 |
| 6 | 14674089.087434763 | 0.216198123827392 | 0.0597664995003766 | 877018.9381126515 | 0 | 219254.73452816287 | 657764.2035844886 |
| 7 | 17163026.09542172 | 0.16961441307578018 | 0.10732487462528245 | 1842019.623881587 | 0 | 460504.9059703967 | 1381514.7179111904 |
| 8 | 19274804.214684512 | 0.12304229496138297 | 0.1548832497501883 | 2985344.3150689634 | 0 | 746336.078767241 | 2239008.2363017225 |
| 9 | 20748968.756403238 | 0.07648142753095422 | 0.20244162487509415 | 4200454.949528833 | 0 | 1050113.737382208 | 3150341.212146625 |
| 10 | 21370016.144351833 | 0.02993148214929664 | 0.25 | 5342504.036087958 | 0 | 1335626.0090219895 | 4006878.0270659686 |
| Year | After-Tax Operating Income | Change in Revenues | Sales to Capital | Reinvestment | FCFF | Capital Invested | Implied ROC |
| Traling 12 month | -817906 |  |  |  |  | -447612 | 1.8272655782239975 |
| 1 | -469169.83112999995 | 1065967.3112999992 | 2 | 532983.6556499996 | -1002153.4867799996 | 85371.65564999962 | -5.495615934326817 |
| 2 | -179693.8997489998 | 1298098.347 | 2 | 649049.1735 | -828743.0732489999 | 734420.8291499997 | -0.2446742965568842 |
| 3 | 37827.397143047114 | 1575682.7703093747 | 2 | 787841.3851546873 | -750013.9880116403 | 1522262.214304687 | 0.024849462062175188 |
| 4 | 382185.6517171878 | 1989161.8643203126 | 2 | 994580.9321601563 | -612395.2804429685 | 2516843.1464648433 | 0.15185119988665388 |
| 5 | 777799.3869178077 | 2510900.332192382 | 2 | 1255450.166096191 | -477650.7791783832 | 3772293.312561034 | 0.20618740974565278 |
| 6 | 657764.2035844886 | 2608547.4623126946 | 2 | 1304273.7311563473 | -646509.5275718587 | 5076567.043717382 | 0.12956870221944952 |
| 7 | 1381514.7179111904 | 2488937.007986957 | 2 | 1244468.5039934786 | 137046.21391771175 | 6321035.54771086 | 0.2185582896162482 |
| 8 | 2239008.2363017225 | 2111778.119262792 | 2 | 1055889.059631396 | 1183119.1766703264 | 7376924.607342256 | 0.30351513069189245 |
| 9 | 3150341.212146625 | 1474164.541718725 | 2 | 737082.2708593626 | 2413258.9412872624 | 8114006.878201619 | 0.3882596181437874 |
| 10 | 4006878.0270659686 | 621047.387948595 | 2 | 310523.6939742975 | 3696354.333091671 | 8424530.572175916 | 0.47562033192682196 |
| Year | Beta | Cost of Equity | Pre-Tax Cost of Debt | Tax Savings | After-Tax Cost of Debt | Debt Ratio | Cost of Capital |
| 1 |  |  |  |  |  |  | 0.06503197511526536 |
| 2 |  |  |  |  |  |  | 0.06503197511526536 |
| 3 |  |  |  |  |  |  | 0.06503197511526536 |
| 4 |  |  |  |  |  |  | 0.06503197511526536 |
| 5 |  |  |  |  |  |  | 0.06503197511526536 |
| 6 |  |  |  |  |  |  | 0.06626558009221228 |
| 7 |  |  |  |  |  |  | 0.06749918506915921 |
| 8 |  |  |  |  |  |  | 0.06873279004610613 |
| 9 |  |  |  |  |  |  | 0.06996639502305306 |
| 10 |  |  |  |  |  |  | 0.07119999999999999 |
| Year | Cost of Capital | Cumulated Cost of Capital | FCFF | Terminal Value | Present Value |  |  |
| 1 | 0.06503197511526536 | 1.0650319751152653 | -1002153.4867799996 |  | -940960.9384465095 |  |  |
| 2 | 0.06503197511526536 | 1.134293108017923 | -828743.0732489999 |  | -730625.1509340078 |  |  |
| 3 | 0.06503197511526536 | 1.2080584291919616 | -750013.9880116403 |  | -620842.4773901912 |  |  |
| 4 | 0.06503197511526536 | 1.2866208548969598 | -612395.2804429685 |  | -475971.82815135753 |  |  |
| 5 | 0.06503197511526536 | 1.3702923503154 | -477650.7791783832 |  | -348575.8196551578 |  |  |
| 6 | 0.06626558009221228 | 1.461095567804971 | -646509.5275718587 |  | -442482.71079428506 |  |  |
| 7 | 0.06749918506915921 | 1.5597183279399671 | 137046.21391771175 |  | 87866.00212534438 |  |  |
| 8 | 0.06873279004610613 | 1.6669221203053286 | 1183119.1766703264 |  | 709762.7191206842 |  |  |
| 9 | 0.06996639502305306 | 1.7835506518472766 | 2413258.9412872624 |  | 1353064.4272915816 |  |  |
| 10 | 0.07119999999999999 | 1.9105394582588024 | 3696354.333091671 | 63859618.55636388 | 35359632.37892174 |  |  |
| Value of operating assets = |  |  |  |  | 33950866.60208784 |  |  |

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

## Country equity risk premiums

| Mature Market ERP + | 0.0512 | Updated Nov 5, 2020 |
|---|---|---|
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.005822960436436361 |
| Albania | B1 | 0.052830131959668084 |
| Algeria | NA | 0.14080977055382476 |
| Andorra (Principality of) | Baa2 | 0.022338993674328587 |
| Angola | B3 | 0.07633371772128394 |
| Argentina | Ca | 0.14080977055382476 |
| Armenia | Ba3 | 0.04224293116614743 |
| Aruba | Baa1 | 0.018739345404531565 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.0046583683491490885 |
| Azerbaijan | Ba2 | 0.035255378642423785 |
| Bahamas | Ba2 | 0.035255378642423785 |
| Bahrain | B2 | 0.06458192484047601 |
| Bangladesh | Ba3 | 0.04224293116614743 |
| Barbados | Caa1 | 0.08797963859415668 |
| Belarus | B3 | 0.07633371772128394 |
| Belgium | Aa3 | 0.00709342453165884 |
| Belize | Caa1 | 0.08797963859415668 |
| Benin | B2 | 0.06458192484047601 |
| Bermuda | A2 | 0.009951968745909418 |
| Bolivia | B1 | 0.052830131959668084 |
| Bosnia and Herzegovina | B3 | 0.07633371772128394 |
| Botswana | A2 | 0.009951968745909418 |
| Brazil | Ba2 | 0.035255378642423785 |
| Brunei | NA | 0.009951968745909416 |
| Bulgaria | Baa2 | 0.022338993674328587 |
| Burkina Faso | B2 | 0.06458192484047601 |
| Cambodia | B2 | 0.06458192484047601 |
| Cameroon | B2 | 0.06458192484047601 |
| Canada | Aaa | 0 |
| Cape Verde | B2 | 0.06458192484047601 |
| Cayman Islands | Aa3 | 0.00709342453165884 |
| Chile | A1 | 0.008258016618946113 |
| China | A1 | 0.008258016618946113 |
| Colombia | Baa2 | 0.022338993674328587 |
| Congo (Democratic Republic of) | Caa1 | 0.08797963859415668 |
| Congo (Republic of) | Caa2 | 0.10566026391933617 |
| Cook Islands | B1 | 0.052830131959668084 |
| Costa Rica | B2 | 0.06458192484047601 |
| Côte d'Ivoire | Ba3 | 0.04224293116614743 |
| Croatia | Ba2 | 0.035255378642423785 |
| Cuba | Caa2 | 0.10566026391933617 |
| Curacao | Baa2 | 0.022338993674328587 |
| Cyprus | Ba2 | 0.035255378642423785 |
| Czech Republic | Aa3 | 0.00709342453165884 |
| Denmark | Aaa | 0 |
| Dominican Republic | Ba3 | 0.04224293116614743 |
| Ecuador | Caa3 | 0.1173061847922089 |
| Egypt | B2 | 0.06458192484047601 |
| El Salvador | B3 | 0.07633371772128394 |
| Estonia | A1 | 0.008258016618946113 |
| Ethiopia | B2 | 0.06458192484047601 |
| Fiji | Ba3 | 0.04224293116614743 |
| Finland | Aa1 | 0.0046583683491490885 |
| France | Aa2 | 0.005822960436436361 |
| Gabon | Caa1 | 0.08797963859415668 |
| Gambia | NA | 0.07633371772128394 |
| Georgia | Ba2 | 0.035255378642423785 |
| Germany | Aaa | 0 |
| Ghana | B3 | 0.07633371772128394 |
| Greece | B1 | 0.052830131959668084 |
| Guatemala | Ba1 | 0.029326546198052226 |
| Guernsey (States of) | Aa3 | 0.00709342453165884 |
| Guinea | NA | 0.14080977055382476 |
| Guinea-Bissau | NA | 0.08797963859415668 |
| Guyana | NA | 0.06458192484047602 |
| Haiti | NA | 0.14080977055382476 |
| Honduras | B1 | 0.052830131959668084 |
| Hong Kong | Aa3 | 0.00709342453165884 |
| Hungary | Baa3 | 0.02583276993619041 |
| Iceland | A2 | 0.009951968745909418 |
| India | Baa3 | 0.02583276993619041 |
| Indonesia | Baa2 | 0.022338993674328587 |
| Iran | NA | 0.10566026391933614 |
| Iraq | Caa1 | 0.08797963859415668 |
| Ireland | A2 | 0.009951968745909418 |
| Isle of Man | Aa2 | 0.005822960436436361 |
| Israel | A1 | 0.008258016618946113 |
| Italy | Baa3 | 0.02583276993619041 |
| Jamaica | B2 | 0.06458192484047601 |
| Japan | A1 | 0.008258016618946113 |
| Jersey (States of) | Aa3 | 0.00709342453165884 |
| Jordan | B1 | 0.052830131959668084 |
| Kazakhstan | Baa3 | 0.02583276993619041 |
| Kenya | B2 | 0.06458192484047601 |
| Korea | Aa2 | 0.005822960436436361 |
| Korea, D.P.R. | NA | 0.14080977055382476 |
| Kuwait | Aa2 | 0.005822960436436361 |
| Kyrgyzstan | B2 | 0.06458192484047601 |
| Laos | B3 | 0.014080977055382476 |
| Latvia | A3 | 0.014080977055382476 |
| Lebanon | Ca | 0.14080977055382476 |
| Liberia | NA | 0.14080977055382476 |
| Libya | NA | 0.10566026391933614 |
| Liechtenstein | Aaa | 0 |
| Lithuania | A3 | 0.014080977055382476 |
| Luxembourg | Aaa | 0 |
| Macao | Aa3 | 0.00709342453165884 |
| Macedonia | Ba3 | 0.04224293116614743 |
| Madagascar | NA | 0.07633371772128394 |
| Malawi | NA | 0.10566026391933614 |
| Malaysia | A3 | 0.014080977055382476 |
| Maldives | B3 | 0.07633371772128394 |
| Mali | B3 | 0.07633371772128394 |
| Malta | A2 | 0.009951968745909418 |
| Mauritius | Baa1 | 0.018739345404531565 |
| Mexico | Baa1 | 0.018739345404531565 |
| Moldova | B3 | 0.07633371772128394 |
| Mongolia | B3 | 0.07633371772128394 |
| Montenegro | B1 | 0.052830131959668084 |
| Montserrat | Baa3 | 0.02583276993619041 |
| Morocco | Ba1 | 0.029326546198052226 |
| Mozambique | Caa2 | 0.10566026391933617 |
| Myanmar | NA | 0.07633371772128394 |
| Namibia | Ba2 | 0.035255378642423785 |
| Netherlands | Aaa | 0 |
| New Zealand | Aaa | 0 |
| Nicaragua | B3 | 0.07633371772128394 |
| Niger | B3 | 0.07633371772128394 |
| Nigeria | B2 | 0.06458192484047601 |
| Norway | Aaa | 0 |
| Oman | Ba3 | 0.04224293116614743 |
| Pakistan | B3 | 0.07633371772128394 |
| Panama | Baa1 | 0.018739345404531565 |
| Papua New Guinea | B2 | 0.06458192484047601 |
| Paraguay | Ba1 | 0.029326546198052226 |
| Peru | A3 | 0.014080977055382476 |
| Philippines | Baa2 | 0.022338993674328587 |
| Poland | A2 | 0.009951968745909418 |
| Portugal | Baa3 | 0.02583276993619041 |
| Qatar | Aa3 | 0.00709342453165884 |
| Ras Al Khaimah (Emirate of) | A2 | 0.009951968745909418 |
| Romania | Baa3 | 0.02583276993619041 |
| Russia | Baa3 | 0.02583276993619041 |
| Rwanda | B2 | 0.06458192484047601 |
| Saudi Arabia | A1 | 0.008258016618946113 |
| Senegal | Ba3 | 0.04224293116614743 |
| Serbia | Ba3 | 0.04224293116614743 |
| Sharjah | Baa2 | 0.022338993674328587 |
| Sierra Leone | NA | 0.10566026391933614 |
| Singapore | Aaa | 0 |
| Slovakia | A2 | 0.009951968745909418 |
| Slovenia | Baa1 | 0.018739345404531565 |
| Solomon Islands | B3 | 0.07633371772128394 |
| Somalia | NA | 0.14080977055382476 |
| South Africa | Ba1 | 0.029326546198052226 |
| Spain | Baa1 | 0.018739345404531565 |
| Sri Lanka | B2 | 0.06458192484047601 |
| St. Maarten | Baa3 | 0.02583276993619041 |
| St. Vincent & the Grenadines | B3 | 0.07633371772128394 |
| Sudan | NA | 0.175 |
| Suriname | B3 | 0.07633371772128394 |
| Swaziland | B2 | 0.06458192484047601 |
| Sweden | Aaa | 0 |
| Switzerland | Aaa | 0 |
| Syria | NA | 0.14080977055382476 |
| Taiwan | Aa3 | 0.00709342453165884 |
| Tajikistan | B3 | 0.07633371772128394 |
| Tanzania | B1 | 0.052830131959668084 |
| Thailand | Baa1 | 0.018739345404531565 |
| Togo | B3 | 0.07633371772128394 |
| Trinidad and Tobago | Ba1 | 0.029326546198052226 |
| Tunisia | B2 | 0.06458192484047601 |
| Turkey | B1 | 0.052830131959668084 |
| Turks and Caicos Islands | Baa1 | 0.018739345404531565 |
| Uganda | B2 | 0.06458192484047601 |
| Ukraine | B3 | 0.07633371772128394 |
| United Arab Emirates | Aa2 | 0.005822960436436361 |
| United Kingdom | Aa2 | 0.005822960436436361 |
| United States | Aaa | 0 |
| Uruguay | Baa2 | 0.022338993674328587 |
| Uzbekistan | B1 | 0.052830131959668084 |
| Venezuela | C | 0.175 |
| Vietnam | Ba3 | 0.04224293116614743 |
| Yemen, Republic | NA | 0.175 |
| Zambia | Ca | 0.14080977055382476 |
| Zimbabwe | NA | 0.14080977055382476 |
|  | ERP | Default Spread |
| Africa | 0.12313055515219112 | 0.05744970535370115 |
| Asia | 0.06674863942594794 | 0.012418432636612842 |
| Australia & New Zealand | 0.05124839909207507 | 3.865552786595667e-05 |
| Caribbean | 0.13256240608476522 | 0.06498276353558158 |
| Central and South America | 0.10587565534475424 | 0.04366851170452789 |
| Eastern Europe & Russia | 0.08306283221816863 | 0.025448299666187734 |
| Middle East | 0.07593784488854033 | 0.019757694027597285 |
| North America | 0.0512 | 0 |
| Western Europe | 0.06328033357625057 | 0.009648356015904839 |
| Global | 0.0665 | 0.0122 |

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
| Advertising | 47 | 0.1898457895 | 0.12071573564591596 | 0.6351383510510417 | 0.24144885196197266 | 0.9349531429448596 | 1.43961175 | 0.094059811 | 0.623767663 | 0.036699999999999997 | 0.45970469962445887 | 0.06347344569467485 | 5.4319282449461905 | 1.93894991479811 | 9.201469364039408 | 15.117650173548792 | 5.982433780654601 | 23.77126452 | 0.0005227717768599065 | 0.02210287557289297 | 0.06896339125992407 | 0.6538330245845457 | 0.26083948775097743 | 1.0133491837919004 | 1.0133491837919004 | 0.12197803738754506 |
| Aerospace/Defense | 77 | 0.035260652170000004 | 0.11366722933042273 | 0.3393297331685048 | 0.19063413766601667 | 1.078522159887352 | 1.231583809 | 0.083242358068 | 0.387395563 | 0.0327 | 0.1953611792611965 | 0.07177126575273358 | 3.1504976789852264 | 2.2661718542019984 | 14.936671749190387 | 19.76659509155769 | 6.090570809542459 | 44.2645417 | 0.3747362548063014 | 0.02790574912863036 | 0.05830230096348875 | 1.0436645952766965 | 0.3142031220748654 | 0.4414412190504289 | 0.4414412190504289 | 0.1174744598100627 |
| Air Transport | 18 | 0.048416666670000004 | 0.11601029095344825 | 0.1369202672601922 | 0.23040082281052784 | 0.8436729976274394 | 1.435347861 | 0.09383808877199999 | 0.317396332 | 0.0327 | 0.5084252294109713 | 0.05859756571191287 | 1.5045218215644707 | 1.3392880167270775 | 6.536975693554191 | 12.003101378380897 | 2.3429187022059925 | 10.54942247 | 0.011618339509923973 | 0.10770214013909912 | 0.05429788414349164 | 0.6132926108693023 | 0.28202838198907293 | 0.15077745202490286 | 0.1507774520249029 | 0.11161527073883153 |
| Apparel | 51 | -0.02563724138 | 0.10576092104574154 | 0.163390661472867 | 0.15606759311520496 | 0.8296410009433827 | 1.055096737 | 0.074065030324 | 0.511019097 | 0.036699999999999997 | 0.2946233609166361 | 0.06035325017278096 | 1.7157058953504207 | 1.8913544786258933 | 10.93015671950725 | 17.564880152844786 | 3.725980658527597 | 54.57223938 | 0.23726047261779315 | 0.025156324353064113 | 0.017864726984155543 | 0.30488096740163095 | 0.16723276272008264 | 0.43054190753528176 | 0.43054190753528176 | 0.10713753881254759 |
| Auto & Truck | 13 | 0.1431333333 | 0.03407544543157772 | 0.028910253439599635 | 0.055439944954436375 | 0.5257350397759242 | 1.095074098 | 0.076143853096 | 0.350188777 | 0.0327 | 0.622538399061633 | 0.04400913492821854 | 0.8744482281868747 | 1.2597451537682027 | 14.386948758692284 | 36.554840874704155 | 1.818661185303154 | 16.76369679 | -0.055392899600342695 | 0.0945006104051779 | 0.05088091481404537 | 1.183687005947487 | 0.12428655448818722 | 0.5157642089093701 | 0.5157642089093701 | 0.035105100632012685 |
| Auto Parts | 46 | 0.04981034483 | 0.07242123193622181 | 0.17000160011143192 | 0.18517556494840495 | 0.9469935769993065 | 1.210970022 | 0.08217044114399999 | 0.50433022 | 0.036699999999999997 | 0.3371503989341491 | 0.06374670886236783 | 2.463110123937496 | 0.7545924613037654 | 6.382276976663343 | 10.183962727885138 | 1.9477213256191348 | 17.58040276 | 0.12619914456709705 | 0.04308241013389483 | 0.06190016521557384 | 1.029993482121285 | 0.12564211594683783 | 0.2630586705311351 | 0.2630586705311351 | 0.07436575450503331 |
| Bank (Money Center) | 7 | 0.02112 | 0 | -0.0002554348246373364 | 0.17744006670223925 | 0.5595414670761663 | 1.000862659 | 0.07124485826799999 | 0.177446458 | 0.0272 | 0.6399615057205409 | 0.038706106212663224 | 0.20423762853931487 | 7.278485635137438 | NA | NA | 1.2709212566104355 | 10.22652485 | NA | 0.014998598415935187 | 0.014998598415935187 | NA | 0.12802702006738365 | 0.2740108625315865 | 0.27401086253158646 | -0.0015508563813298008 |
| Banks (Regional) | 611 | 0.1013484055 | 0 | -0.000626012605615589 | 0.203301708617835 | 0.4313155820626237 | 0.566982758 | 0.048683103416 | 0.182632184 | 0.0272 | 0.38620076872686804 | 0.03776014713475929 | 0.25786954727934724 | 5.954467571095584 | NA | NA | 1.3739071963617933 | 15.40696154 | NA | 0.03506784069134694 | 0.00615837401653653 | NA | 0.12047930242644632 | 0.2976935629764687 | 0.29769356297646876 | -0.002941260441722288 |
| Beverage (Alcoholic) | 21 | 0.10773300000000001 | 0.221133258195691 | 0.1494764364798027 | 0.1838907832285259 | 0.9188825577761112 | 1.126335082 | 0.07776942426399999 | 0.424625152 | 0.036699999999999997 | 0.23826667554395717 | 0.06579785232999658 | 0.7239147586111915 | 4.618313532921969 | 16.32460672049884 | 20.874451468155083 | 2.9935529576291624 | 38.69106302 | 0.16610862361619405 | 0.0725224443619711 | 0.05493541661993844 | 0.4161276992332601 | 0.06884488878269722 | 0.6700355094236548 | 0.6700355094236548 | 0.22111324377239883 |
| Beverage (Soft) | 34 | 0.3074641667 | 0.20400857139373657 | 0.2620710602824583 | 0.09755790166273977 | 1.0907131928183842 | 1.218896909 | 0.08258263926799998 | 0.570769263 | 0.036699999999999997 | 0.1613435249427651 | 0.07369944567347367 | 1.329991859263124 | 4.881424317033564 | 19.920651630593337 | 23.730552017434444 | 8.048258113465169 | 39.86898263 | -0.07691789994992607 | 0.047022848434798425 | 0.08760125134470258 | 0.48511616851522715 | 0.4024944229151887 | 0.5743870023879232 | 0.5743870023879232 | 0.20527988770688685 |
| Broadcasting | 27 | 0.095402 | 0.21993025537047728 | 0.21471018773708805 | 0.07243893056637535 | 0.729937390293151 | 1.213678059 | 0.08231125906799999 | 0.326515482 | 0.0327 | 0.49610010489701606 | 0.05364348988275905 | 1.1344896657679504 | 2.7168068208307714 | 9.058433744996371 | 12.443566410441985 | 2.079228762269691 | 8.55694295 | 0.21619790077739137 | 0.027555214498372154 | 0.2952512950003833 | 1.6626603200268615 | 0.9339469470840174 | 0.3814731942701595 | 0.38147319427015947 | 0.21830773214182347 |
| Brokerage & Investment Banking | 39 | 0.0665925 | 0.005464034785645316 | 0.00039982986736765945 | 0.19962886196952606 | 0.5676743238719565 | 1.460916203 | 0.09516764255599999 | 0.273615777 | 0.0327 | 0.7285467284386993 | 0.043701176433561764 | 0.19811926589991763 | 6.168384767683812 | NA | NA | 1.2734532848331903 | 18.04954541 | NA | 0.07803345497620802 | 0.07435787534278397 | -71.68644330080181 | 0.1405687926327982 | 0.22212173378697717 | 0.2221217337869772 | 0.0023068951960916614 |
| Building Materials | 42 | 0.12306896549999999 | 0.09014496582530461 | 0.18653741318760034 | 0.24825877329412097 | 1.0185312839204805 | 1.231648593 | 0.083245726836 | 0.307784494 | 0.0327 | 0.24284915276104327 | 0.06898544807436474 | 2.4160680603788003 | 1.604296335903156 | 12.27972857387538 | 17.35524868850979 | 3.9876546398431696 | 25.41755701 | 0.15914948522476616 | 0.028101837152804374 | 0.018273444427528804 | 0.3010247125458703 | 0.14051425963604217 | 0.2674558400744551 | 0.2674558400744551 | 0.09221389289512476 |
| Business & Consumer Services | 165 | 0.09569410256 | 0.10186274115821865 | 0.2193703432956895 | 0.20236902734388063 | 0.8948866171646999 | 1.065922206 | 0.074627954712 | 0.437972967 | 0.036699999999999997 | 0.23257179257409594 | 0.0636731360990937 | 2.277474841250099 | 2.3914383071189884 | 13.995354841319832 | 22.566579621152737 | 5.002667825248062 | 47.53833193 | 0.14662963143092647 | 0.03475301358749025 | 0.01142438648740118 | 0.21646275829927772 | 0.10236449926592565 | 0.7382262195567035 | 0.7382262195567035 | 0.10504163763794887 |
| Cable TV | 14 | 0.03778571429 | 0.17946618863973934 | 0.12146173570716183 | 0.21218716705726146 | 0.776608279328833 | 1.114565004 | 0.07715738020799999 | 0.250274606 | 0.0327 | 0.3756708306867774 | 0.05738493021423833 | 0.7923672310322167 | 3.4385723692403647 | 10.120034944574694 | 18.551735617790538 | 2.611236732355121 | 80.57198359 | 0.014944040070023307 | 0.11188728331600299 | 0.16575228492078842 | 1.244027802678063 | 0.11755699477898732 | 0.23150560041677523 | 0.23150560041677526 | 0.1793052087689119 |
| Chemical (Basic) | 43 | 0.06782176471 | 0.08298043612018542 | 0.11681580455954943 | 0.25877611940298506 | 0.9929566124984756 | 1.366827709 | 0.09027504086799999 | 0.519583729 | 0.036699999999999997 | 0.3792157705365071 | 0.06647923576904406 | 1.5021790996996895 | 1.2999513253428894 | 8.241577309387305 | 15.401535422513211 | 2.115439610368818 | 16.11017453 | 0.16089409055217407 | 0.0551761568883812 | 0.05923325878053168 | 0.7571945023344184 | 0.09157341750878087 | 0.9086238425205609 | 0.9086238425205609 | 0.08332602517857328 |
| Chemical (Diversified) | 6 | -0.047995 | 0.10748918518028831 | 0.11784519554019143 | 0.23099703849950642 | 1.2147165368811397 | 1.852864301 | 0.115548943652 | 0.359186077 | 0.0327 | 0.44027836028539163 | 0.07547307099418755 | 1.2364889093567428 | 1.351878547612063 | 7.939290839514981 | 12.525383754048809 | 1.8923261761731993 | 10.48037633 | 0.19996777245701958 | 0.056617182238492075 | 0.004695528221824662 | 0.06579985416702698 | 0.10065057105681653 | 0.6272144019917648 | 0.6272144019917648 | 0.10814244321961418 |
| Chemical (Specialty) | 94 | 0.06782188679 | 0.12568248019756356 | 0.12929574120608997 | 0.254286908586703 | 0.9648570942816654 | 1.135190386 | 0.078229900072 | 0.483612329 | 0.036699999999999997 | 0.22194966217538845 | 0.06697596463038277 | 1.1250368699909405 | 2.0907907037401423 | 10.564246843917338 | 16.377615637130713 | 2.6117664773403653 | 25.33832554 | 0.163264963981507 | 0.05125536334491153 | 0.04701321361067778 | 0.6110310002670083 | 0.056845590271146884 | 0.6399421245365046 | 0.6399421245365046 | 0.1289481350888777 |
| Coal & Related Energy | 22 | -0.1168714286 | 0.0663011688752996 | 0.12696818066119872 | 0.02652705882352941 | 1.0486643640232785 | 1.395904275 | 0.09178702229999999 | 0.54709193 | 0.036699999999999997 | 0.4434894880377394 | 0.06328749092990321 | 1.8584999265102529 | 0.6166176095776303 | 2.2516026127492084 | 6.32520134300031 | 0.8579985561272154 | 10.29573167 | 0.05935908420160712 | 0.0792542434536538 | -0.008490585456733328 | 0.12652077511135348 | 0.11588977849579879 | 0.16812163662765867 | 0.16812163662765867 | 0.06898656495290788 |
| Computer Services | 106 | 0.1582766038 | 0.07645941200790693 | 0.2489135369885101 | 0.24760645767124959 | 0.9528662646292019 | 1.203022395 | 0.08175716454 | 0.455214363 | 0.036699999999999997 | 0.3086528933207223 | 0.06501825004368351 | 3.3657491912923905 | 1.281841587578139 | 10.361520723010797 | 15.919852718087524 | 3.807609005563655 | 29.1332048 | 0.1277046643289384 | 0.014625222241111725 | 0.1091026251261477 | 1.7986021688326541 | 0.17286940934309591 | 0.5213557255687444 | 0.5213557255687444 | 0.08108864392176096 |
| Computers/Peripherals | 48 | -0.01920681818 | 0.15505305501311756 | 0.22641153931591998 | 0.15801633058493908 | 1.6400833392351297 | 1.748007023 | 0.110096365196 | 0.504058887 | 0.036699999999999997 | 0.13413065168401633 | 0.0990210141718216 | 1.519805777338354 | 3.2265807729785143 | 15.129052029671968 | 20.79859220267702 | 11.026904564318405 | 28.91867687 | -0.08128668918956372 | 0.035109154999138754 | 0.0067355542549207515 | 0.0930639604432245 | 0.3999289442064997 | 0.2684404223780329 | 0.2684404223780329 | 0.15857313757823294 |
| Construction Supplies | 44 | 0.04333 | 0.11925932256903239 | 0.1598085392980638 | 0.2214681899383392 | 1.10359654774166 | 1.363622994 | 0.09010839568799998 | 0.29907074300000003 | 0.0327 | 0.2864146483685801 | 0.07132435047320401 | 1.5686120506936665 | 1.681907440072824 | 10.498742039443274 | 13.977919645053262 | 3.4080444907877325 | 39.58093682 | 0.15084214838812915 | 0.05165879247732081 | 0.0440329040780348 | 0.6508524962212954 | 0.24777437380856945 | 0.28546259658334305 | 0.28546259658334305 | 0.12089188261342128 |
| Diversified | 23 | 0.15158 | 0.1371612819516662 | 0.11554605698734828 | 0.17898424204919666 | 1.2484828302966493 | 1.401852102 | 0.09209630930399999 | 0.381569554 | 0.0327 | 0.237569073486817 | 0.07604345595835757 | 0.9071645882513742 | 2.446239739101519 | 12.92071310980912 | 17.84345276157449 | 1.9308435435694835 | 22.7751588 | 0.055528961897387395 | 0.05697482300181776 | 0.02797024611944477 | 0.28604175363623613 | 0.0786002077612884 | 0.18222631995737143 | 0.18222631995737149 | 0.13653176793162755 |
| Drugs (Biotechnology) | 503 | 0.3189407746 | 0.11254811389226776 | 0.086418583640002 | 0.14877682505820505 | 1.3891731337867141 | 1.433451664 | 0.09373948652799999 | 0.67447286 | 0.0442 | 0.12726538790327405 | 0.08602854202215388 | 0.4284180215573512 | 7.328041163687847 | 13.294180666265783 | 45.76830410893881 | 7.078617595453064 | 77.55560882 | 0.13136289662695042 | 0.04044147279993307 | 0.09589662876354435 | 1.640623271998407 | -0.00936740316703145 | 0.00102280404 | 0.0010228040399999916 | 0.20239160409629856 |
| Drugs (Pharmaceutical) | 267 | 0.3172055 | 0.24854001055085334 | 0.18292849705273642 | 0.13193476060329154 | 1.2856575366949226 | 1.361590902 | 0.09000272690399999 | 0.771366513 | 0.0692 | 0.1299095603885961 | 0.08505281840229462 | 0.7621997076047174 | 5.436403122818616 | 14.565500802857626 | 21.076432719529286 | 6.331943932678352 | 58.18354141 | 0.20669911076277772 | 0.05157159019825897 | 0.09470331126973242 | 0.43560733665315665 | 0.21508119987036403 | 0.6139409023483351 | 0.6139409023483351 | 0.2433667420433816 |
| Education | 35 | 0.027605 | 0.0875006247872748 | 0.10845001844440375 | 0.2847935591589552 | 1.3560146590000444 | 1.605603462 | 0.10269138002399998 | 0.376440693 | 0.0327 | 0.251943852044854 | 0.0829978411403515 | 1.3113086120747015 | 2.587341838374077 | 14.460654860875968 | 29.26647642678048 | 2.509803073480382 | 22.19564 | 0.12305143724874627 | 0.051996522612539064 | 0.05797133356976079 | 1.2131835974606873 | 0.12899887000370264 | 0.045584872520508544 | 0.04558487252050858 | 0.08842733932256398 |
| Electrical Equipment | 113 | 0.091217 | 0.1360982361867331 | 0.2559534760369159 | 0.18088445965228547 | 1.307118859086069 | 1.444743618 | 0.09432666813599999 | 0.536716612 | 0.036699999999999997 | 0.1735259964182832 | 0.08273484211029712 | 1.8975642180059884 | 2.560486794780635 | 12.81842815211587 | 17.78804247734955 | 4.846657584590342 | 29.84977452 | 0.19732322536089533 | 0.04442737552356094 | 0.05537203113614843 | 0.5375387636170006 | 0.20081954767808216 | 0.3679557447450575 | 0.36795574474505743 | 0.1403360019990691 |
| Electronics (Consumer & Office) | 20 | 0.05860727273 | -0.012668277255638224 | -0.02117144435931501 | 0.6277621534752913 | 1.25079435757328 | 1.275416899 | 0.085521678748 | 0.62170468 | 0.036699999999999997 | 0.17127786855295413 | 0.07558813122889214 | 1.8749195431109225 | 0.9142382869638073 | 15.64684012583527 | NA | 2.7553905177046634 | 64.23576854 | 0.17304741659483183 | 0.01717341635491727 | 0.0019784114124921067 | NA | -0.10111486815765601 | 0 | 0 | -0.01198304451530292 |
| Electronics (General) | 153 | 0.07855029126 | 0.08872079979524458 | 0.1397383808063948 | 0.1867957542534177 | 1.070921529276746 | 1.150958137 | 0.079049823124 | 0.427785929 | 0.036699999999999997 | 0.1542462170454968 | 0.07110231407318465 | 1.627631788533011 | 1.9925549912148577 | 13.073702001964598 | 21.688493110016587 | 3.2726750466864374 | 125.8236254 | 0.21143898800512861 | 0.053726607109567726 | 0.06666307512603098 | 1.060238841503128 | 0.11291067555483596 | 0.24669518991119313 | 0.2466951899111931 | 0.09184476186125819 |
| Engineering/Construction | 54 | 0.08433 | 0.03892484333747958 | 0.14554412172740805 | 0.24507619982565917 | 1.3250378765861548 | 1.597299211 | 0.102259558972 | 0.331927324 | 0.0327 | 0.2819782616209147 | 0.08034010316520696 | 3.917899694611343 | 0.7025277725419653 | 9.752651467029542 | 16.42695327484433 | 1.8660388333226876 | 18.70761785 | 0.17737417740748043 | 0.017773701630329135 | 0.02803218348160961 | 1.1865210072059746 | 0.03426025132040608 | 0.3686194552529183 | 0.3686194552529183 | 0.04102125035188866 |
| Entertainment | 107 | 0.08047741935 | 0.13523407286877287 | 0.18572742748682836 | 0.20408022173353516 | 1.2017030374551592 | 1.333187022 | 0.08852572514399999 | 0.555724404 | 0.036699999999999997 | 0.16712343782827419 | 0.07833107424791706 | 1.4063408522226708 | 4.718798201591803 | 21.849891013216887 | 34.912738681218364 | 3.702056655635448 | 47.68399889 | 0.024932947594587626 | 0.05278912044800546 | 0.08193563407338543 | 0.8321186399534515 | 0.17660188702061802 | 0.22139221107422516 | 0.22139221107422513 | 0.13458629680602266 |
| Environmental & Waste Services | 82 | 0.2102567742 | 0.12098570228045176 | 0.20001472749670868 | 0.2096599203546552 | 1.0485101305295534 | 1.268505796 | 0.08516230139199998 | 0.443353143 | 0.036699999999999997 | 0.24062580151519003 | 0.07129327954737741 | 1.6940501698643553 | 3.0813954191663675 | 13.929669795994238 | 24.91308273591856 | 4.289587757208971 | 735.0487844 | 0.09952122116662528 | 0.08394199979430425 | 0.05695458786778772 | 0.5379944148395556 | 0.10682193684871732 | 0.534611174213424 | 0.534611174213424 | 0.12316680912607017 |
| Farming/Agriculture | 31 | 0.000246875 | 0.040177230964001755 | 0.0627302710066847 | 0.2117583696313249 | 0.6274511480684076 | 0.893625083 | 0.06566850431599999 | 0.468760477 | 0.036699999999999997 | 0.38419618211811823 | 0.05101391558518683 | 1.5868509739597294 | 1.0776847266333611 | 13.915667730510025 | 23.761199476447878 | 2.5461588360650547 | 73.1893748 | 0.11506109817037004 | 0.03550218355062078 | 0.028937445065539625 | 1.3305711242328333 | 0.09141449473694817 | 0.5624443229406016 | 0.5624443229406016 | 0.04197581730835711 |
| Financial Svcs. (Non-bank & Insurance) | 232 | 0.1086845139 | 0.07509737358742584 | 0.002345884993164995 | 0.19830498513712722 | 0.09826313785398752 | 0.732438335 | 0.057286793419999996 | 0.257033041 | 0.0327 | 0.8981891558985402 | 0.02786050584236785 | 0.0370254505549912 | 30.15473009489712 | NA | NA | 2.2239361985195094 | 83.00451884 | NA | 0.0824341728675169 | 0.08367426049308425 | 2.0292353240346226 | 0.0007486425 | 0.1595928649518031 | 0.15959286495180314 | 0.07396540731342861 |
| Food Processing | 88 | 0.04236439024 | 0.12004431390715754 | 0.15554861201386966 | 0.14815869059912903 | 0.6968082479529737 | 0.875321839 | 0.064716735628 | 0.31529092 | 0.0327 | 0.2720778405670454 | 0.05378145498969217 | 1.3649666080470375 | 2.2986527569163315 | 14.264116364395472 | 18.841047218224077 | 2.5811498621211344 | 42.25438254 | 0.06525935163973232 | 0.0360661770072577 | 0.027729446920432877 | 0.27868647415448605 | 0.01903131144932094 | 3.038219783903659 | 3.038219783903659 | 0.12180748502457767 |
| Food Wholesalers | 17 | 0.2285625 | 0.027151757154997038 | 0.1682460733021894 | 0.19166311149527035 | 0.6577661732913673 | 0.868022899 | 0.064337190748 | 0.31580572 | 0.0327 | 0.305332219751679 | 0.0521812461737359 | 6.7800696012153585 | 0.5992841892038884 | 13.94967568886934 | 22.22235985513416 | 5.927960692140531 | 47.9826274 | 0.07242845921195541 | 0.01180322055990941 | 0.024337815325241683 | 1.1387689133832049 | 0.15512943196531642 | 0.5063937813923589 | 0.5063937813923589 | 0.02691039614039567 |
| Furn/Home Furnishings | 35 | 0.09712578947 | 0.07087350288585113 | 0.13357129635123577 | 0.2202996557389461 | 0.8183273103323906 | 1.076595269 | 0.075182953988 | 0.433843108 | 0.036699999999999997 | 0.32592530570754086 | 0.059650020765065176 | 1.961542046803804 | 1.1086979198562685 | 9.269384331070532 | 14.802796990466904 | 2.2052316905231346 | 14.7932714 | 0.13274710857810398 | 0.0326307823410646 | 0.04854662639890566 | 0.865415610635755 | 0.16974611949398843 | 0.24219630345218773 | 0.24219630345218768 | 0.07413115309847168 |
| Green & Renewable Energy | 22 | 0.19482500000000003 | 0.118190587573924 | 0.013934693236192324 | 0.32661085743277524 | 0.593772952019942 | 1.072331851 | 0.074961256252 | 0.53761195 | 0.036699999999999997 | 0.5297110411170959 | 0.04983374756605573 | 0.16453086906868888 | 9.938159384425457 | 17.151860051688853 | 123.23432118819223 | 1.6825439325313793 | 26.23468169 | 0.030934979594630235 | 0.3825861551686214 | 0.411498719633534 | 8.134951976755696 | -0.05800124556197328 | 0.0011632870900000001 | 0.0011632870900000203 | 0.08591268253669673 |
| Healthcare Products | 242 | 0.1340120155 | 0.1500104583843345 | 0.1586866014350913 | 0.12496352847400585 | 0.9818186838686335 | 1.042968711 | 0.073434372972 | 0.530856842 | 0.036699999999999997 | 0.11697038611330325 | 0.06806433588924553 | 1.0264217479098237 | 5.942336567546656 | 22.669654496072873 | 37.55351626774253 | 5.127991127770734 | 84.42618676 | 0.24303971757809348 | 0.05123709451888709 | 0.0621507712020643 | 0.7086517958565463 | 0.09776035078043047 | 0.30272133887505437 | 0.30272133887505437 | 0.15991068180452703 |
| Healthcare Support Services | 128 | 0.1843985 | 0.043691496620801726 | 0.37910420233851516 | 0.23595209607333076 | 0.9462382149452834 | 1.170318746 | 0.080056574792 | 0.499545328 | 0.036699999999999997 | 0.2852357743382601 | 0.06507269037899566 | 9.694448826655973 | 0.6901012499818027 | 11.737714226239843 | 16.046214219531635 | 2.8615418748663886 | 51.6405258 | -0.05178659356950737 | 0.007576138692821359 | 0.05148864085227041 | 1.6786603679322858 | 0.1315678916416916 | 0.38373267364622876 | 0.38373267364622876 | 0.0426264731940707 |
| Heathcare Information and Technology | 129 | 0.18170462959999997 | 0.12578013953083214 | 0.1439641863344189 | 0.13298058658392328 | 1.152697351786613 | 1.24491958 | 0.08393581815999998 | 0.538640137 | 0.036699999999999997 | 0.12790809380910645 | 0.07672041793894226 | 1.1438019674160267 | 5.413405022152209 | 23.491669028543857 | 40.45647472316115 | 5.283239127004696 | 99.81072772 | 0.22143774980472095 | 0.039920463554901024 | 0.0453198338075943 | 0.5910561999286313 | 0.11171734048189148 | 0.08538467878608615 | 0.08538467878608613 | 0.1307145691844556 |
| Homebuilding | 32 | 0.33644208329999997 | 0.10151698776146403 | 0.11252353720970053 | 0.2355983033666141 | 0.6640558389827699 | 0.827682488 | 0.06223948937599999 | 0.365506773 | 0.0327 | 0.3065323008442438 | 0.05067878017240892 | 1.3313979261343396 | 1.210953223606872 | 10.945436440125327 | 11.886668964457572 | 1.6277557320484664 | 16.26090276 | 0.7308043000334522 | 0.008195267297855701 | 0.01289309121295359 | 0.5609762042058851 | 0.15256525064812138 | 0.0726119556033862 | 0.07261195560338618 | 0.1018462596219259 |
| Hospitals/Healthcare Facilities | 36 | 0.05201772727 | 0.1075954629038785 | 0.15312474607463705 | 0.21482140966831925 | 0.6255623897598616 | 1.221736566 | 0.08273030143199998 | 0.426320967 | 0.036699999999999997 | 0.5655590702886582 | 0.051508442479112945 | 1.5913107594973508 | 1.627320272233575 | 9.373577975453287 | 15.59932414454162 | 6.3156550716093856 | 38.93764172 | 0.12274546166515576 | 0.06364463708380307 | 0.035350795993136404 | 0.5529386430192991 | 0.6212679203496074 | 0.2361699324021091 | 0.23616993240210915 | 0.10402460977654683 |
| Hotel/Gaming | 65 | 0.08350583333 | 0.19220154117336016 | 0.11639471697186574 | 0.17418415792562492 | 0.9144446236425152 | 1.261610395 | 0.08480374053999999 | 0.341033572 | 0.0327 | 0.3606549844459781 | 0.06306391230812314 | 0.7157650309414949 | 3.7845532404462703 | 12.736817291644046 | 20.314011943981434 | 3.852763633697383 | 134.2044691 | 0.0785060862971907 | 0.09573192042452483 | 0.04938809203250443 | 0.39808496936567744 | 0.16228307265904782 | 0.5430469991211841 | 0.5430469991211841 | 0.1858825524772738 |
| Household Products | 127 | 0.1741696 | 0.17430411560653158 | 0.28181193709251784 | 0.26920402215990097 | 0.9370572448948898 | 1.030008074 | 0.072760419848 | 0.509069047 | 0.036699999999999997 | 0.1465588652085015 | 0.066130768047847 | 1.7127013022354711 | 3.7365604572841393 | 16.57244278503747 | 21.317561664518713 | 8.199877667784119 | 33.22769382 | 0.08782020325430086 | 0.04109947305412022 | 0.05171244878808545 | 0.33265404406284493 | 0.10594857822391075 | 1.5258011818149912 | 1.5258011818149912 | 0.1749222292532958 |
| Information Services | 69 | 0.1312132432 | 0.2828270164293798 | 0.4152425174889749 | 0.18860677589539004 | 1.0315158970762186 | 1.093128707 | 0.076042692764 | 0.377976491 | 0.0327 | 0.10623812096255494 | 0.07056954988842642 | 1.585927407203242 | 9.174590890633901 | 26.351968846960887 | 32.25026688975913 | 6.5807969408446185 | 46.22702228 | 0.07181814496079711 | 0.03194053779730438 | 0.17097483708044892 | 0.8052422686897442 | 0.3052322126480062 | 0.24912613563255923 | 0.24912613563255925 | 0.28551627216842007 |
| Insurance (General) | 19 | 0.07798733333 | 0.12184459792485751 | 0.09611654351059767 | 0.21421520201272912 | 0.5926992839184214 | 0.74262553 | 0.05781652756 | 0.310019925 | 0.0327 | 0.29285597584143325 | 0.048066904769164226 | 0.9322995722817314 | 1.953117401966289 | 10.26574583037824 | 15.893054840677188 | 1.4793399136497154 | 67.57180218 | -0.0966732072159007 | 0.007534014199420231 | 0.03829014255765234 | 0.49361489957045834 | 0.07418462371642658 | 0.4204687945510782 | 0.4204687945510782 | 0.12287563299214903 |
| Insurance (Life) | 24 | 0.014992499999999999 | 0.13288366881121244 | 0.0819953593234341 | 0.19822321078110688 | 0.7324805743770343 | 1.076150112 | 0.075159805824 | 0.251282053 | 0.0327 | 0.493669765664082 | 0.050162933098419626 | 0.724038092672334 | 1.3606605288519424 | 9.532889253806566 | 10.232648185928694 | 0.7118424879597719 | 21.05216021 | 0.07031057257475563 | 0.0016041142887078725 | 0.0023015906407028216 | 0.09742255454647125 | 0.10438837499049042 | 0.2606808520806203 | 0.2606808520806203 | 0.13288356412127889 |
| Insurance (Prop/Cas.) | 51 | 0.07050186047000001 | 0.10673463482062251 | 0.10477677716285738 | 0.19780847040766927 | 0.5890715247484962 | 0.678285561 | 0.054470849172 | 0.217098126 | 0.0272 | 0.20860498140688016 | 0.047363500313958314 | 1.1355926290868585 | 1.4850608721263454 | 11.395957871571646 | 13.802894375299504 | 1.5328683423671587 | 29.59684252 | -0.5185441757101492 | 0.011976317751197786 | 0.006263434113376614 | 0.136032387690382 | 0.10583960453220007 | 0.3581733150381589 | 0.35817331503815897 | 0.10732782331776244 |
| Investments & Asset Management | 192 | 0.00895366667 | 0.17457953142195481 | 0.0731412529419428 | 0.1726171032554374 | 0.8601828401441228 | 1.027293808 | 0.072619278016 | 0.278758959 | 0.0327 | 0.3523533852993269 | 0.05567309634353541 | 0.4602146090745082 | 4.581743063288606 | 21.975408868218786 | 25.786322273380826 | 1.675882119358177 | 79.93659958 | NA | 0.03473861237259223 | 0.08280537442066276 | 0.6077890734442968 | 0.13313772511327338 | 0.49328344198734814 | 0.4932834419873482 | 0.17173593796093942 |
| Machinery | 120 | 0.035001298699999996 | 0.13839680166911014 | 0.24494098740934434 | 0.2233086569001573 | 1.0985210616277283 | 1.247017093 | 0.08404488883599999 | 0.353916965 | 0.0327 | 0.19263261139184595 | 0.07257941721976893 | 1.981008439093965 | 2.5816308002306547 | 13.87795568779971 | 18.347794164383654 | 4.089599356931275 | 36.09832278 | 0.2339615698751946 | 0.029005513878121617 | 0.08775301157953666 | 0.8946096811654389 | 0.20029882474439942 | 0.28001782383061485 | 0.2800178238306148 | 0.14096295305230103 |
| Metals & Mining | 92 | 0.148425 | 0.11276434818093449 | 0.11256543469121104 | 0.5329213392163382 | 1.0865722025981523 | 1.310283238 | 0.087334728376 | 0.732549534 | 0.0442 | 0.2764615286738967 | 0.07235473553839117 | 1.0109166329980455 | 2.038996912289164 | 9.584154343099652 | 17.434811294215052 | 1.8593553534009992 | 727.0962734 | 0.1621869456304491 | 0.10654890548234387 | 0.0281304925145326 | 0.3841120890325428 | 0.03270105050441654 | 2.0297984137434244 | 2.0297984137434244 | 0.11357641211121652 |
| Office Equipment & Services | 22 | 0.03738571429 | 0.0884924080813151 | 0.17477407471504222 | 0.2293967824341585 | 1.2442326298508288 | 1.645279013 | 0.10475450867599999 | 0.312796215 | 0.0327 | 0.35434326269795696 | 0.0763257228070921 | 2.248795676311931 | 1.2036249853181076 | 8.768055090955707 | 13.286035861692795 | 2.962264177996996 | 34.53464251 | 0.09548721295018195 | 0.03269770360145564 | 0.011919327393650385 | 0.21576991687748737 | 0.18221074572422905 | 0.3857250685086812 | 0.38572506850868127 | 0.0915673558037395 |
| Oil/Gas (Integrated) | 4 | -0.064775 | 0.07326393281743389 | 0.05358960256609772 | 0.3025111476179301 | 1.1174661727895663 | 1.300645569 | 0.086833569588 | 0.286224034 | 0.0327 | 0.2114757701987885 | 0.07365681684439289 | 0.959938994292494 | 1.606634040866202 | 9.172700433113917 | 21.74284343864046 | 1.4051456468410979 | 22.67209961 | 0.04324280095418474 | 0.1047713695761727 | 0.07122796945163014 | 1.3708934908742227 | 0.07848339873321292 | 0.890735640885839 | 0.890735640885839 | 0.07396108347801882 |
| Oil/Gas (Production and Exploration) | 269 | -0.037269344260000004 | 0.19870188081212364 | 0.0903142441594144 | 0.1936683038156571 | 1.076710639640376 | 1.478219605 | 0.09606741946 | 0.593651187 | 0.036699999999999997 | 0.3605677847336668 | 0.07135323111502202 | 0.4639438212066786 | 2.7115380336077504 | 4.894664624801636 | 13.285415282519601 | 1.1898848517843408 | 8.66001991 | 0.019785935554210408 | 0.45558724957631713 | 0.14258632808904345 | 0.7917085008304896 | 0.06362302677498229 | 0.2735996060680697 | 0.27359960606806966 | 0.20215616901160954 |
| Oil/Gas Distribution | 24 | 0.14938125 | 0.20903704289538394 | 0.07989379401380041 | 0.2234178923222237 | 0.6175192303191579 | 1.016075276 | 0.07203591435199999 | 0.326576943 | 0.0327 | 0.47282550027992126 | 0.0495715425047591 | 0.4042508424364071 | 4.436002661542646 | 12.869405786649018 | 20.67591232285663 | 1.5812911033280106 | 69.40697454 | 0.03745578151139793 | 0.300161613259615 | 0.20671722360266995 | 1.2559575677291117 | 0.03909935560641327 | 3.032142830158742 | 3.032142830158742 | 0.20904224767195717 |
| Oilfield Svcs/Equip. | 136 | 0.014886176470000002 | 0.04161182049085188 | 0.11592020109400107 | 0.20955223924223979 | 1.218654717118134 | 1.57914625 | 0.10131560499999999 | 0.534969891 | 0.036699999999999997 | 0.32728837071266015 | 0.07716479811564851 | 2.7909667710487684 | 0.7359715572468865 | 8.58291478087301 | 16.776791422903727 | 1.4661594347331335 | 25.43844596 | 0.0797976420423779 | 0.04003519681227283 | 0.01578349675123281 | 0.4360151085948563 | -0.08397066758835191 | 0.0031552795500000004 | 0.0031552795499999453 | 0.043734938415947625 |
| Packaging & Container | 24 | 0.055162105260000004 | 0.1013759277141194 | 0.1683409525775269 | 0.21709585535545384 | 0.6781735167393964 | 0.990356914 | 0.070698559528 | 0.331374104 | 0.0327 | 0.3973659158609094 | 0.05235076075759806 | 1.8518718237499854 | 1.5935927869773734 | 9.508993154383969 | 15.3214613013831 | 3.0974794478800813 | 20.60885717 | 0.10270961797152713 | 0.05302333039833002 | 0.1197680134037853 | 1.4806864026858981 | 0.15955254796758586 | 0.44972735986269075 | 0.44972735986269075 | 0.10349705087700282 |
| Paper/Forest Products | 15 | 0.1888481818 | 0.054035235163300374 | 0.09368534615215812 | 0.1961863801841673 | 1.2543747470505289 | 1.53666498 | 0.09910657896 | 0.373667154 | 0.0327 | 0.282876350128918 | 0.07800921411694349 | 1.908685055680806 | 0.7704737674950188 | 7.534351489580418 | 14.02899107203157 | 1.586392401575888 | 24.91748737 | 0.14024186746162487 | 0.04696531395876408 | 0.017666454528937506 | 0.39260598022411836 | 0.020450710425276956 | 1.7943198804185352 | 1.7943198804185352 | 0.05478924974294794 |
| Power | 52 | 0.03495446809 | 0.18321598727450708 | 0.06475986797197382 | 0.17046992035484634 | 0.37843539998307546 | 0.575828777 | 0.049143096404 | 0.184872237 | 0.0272 | 0.42033403831590493 | 0.03706139461880331 | 0.41247133623789856 | 4.1142560306250875 | 12.030275988961662 | 22.72587674540601 | 2.011009859307937 | 23.73691461 | 0.054338330303454044 | 0.34133879527338834 | 0.213116592784226 | 1.3995031229174981 | 0.057139424893253 | 0.9758729506708916 | 0.9758729506708916 | 0.18102210711788563 |
| Precious Metals | 83 | 0.140799 | 0.1450962701883178 | 0.08066446091795432 | 0.2717823481612487 | 1.3320479668619645 | 1.435073122 | 0.09382380234399999 | 0.826426419 | 0.0692 | 0.15519528905286836 | 0.0873174257210276 | 0.5682202560611633 | 5.054711480554213 | 13.650576846691388 | 34.171544765682704 | 1.7442576293034027 | 76.84467499 | 0.13966764986487296 | 0.15148399101193907 | -0.059104712113229596 | -0.17945715230240655 | 0.12900248686310087 | 0.20770337879514766 | 0.20770337879514766 | 0.14449504009038322 |
| Publishing & Newspapers | 31 | 0.0012955555599999998 | 0.054338625261254166 | 0.1047435402947904 | 0.2594746119571072 | 0.7567842313849863 | 1.067508815 | 0.07471045838 | 0.38178201 | 0.0327 | 0.4032274250011199 | 0.05447430522493173 | 2.1390230752115724 | 1.070844067568611 | 9.178702626584746 | 19.766329521415628 | 1.593737161069688 | 28.04954629 | 0.13476517640728497 | 0.032210776999170465 | 0.0018968285798983064 | -0.05131981301917006 | -0.03785045763517283 | 0.008040098839999999 | 0.00804009884000001 | 0.05329070737291027 |
| R.E.I.T. | 234 | 0.1067300549 | 0.27150867267835244 | 0.029249315554869825 | 0.02176745713501317 | 0.4256203375693727 | 0.683839332 | 0.054759645264 | 0.19856503 | 0.0272 | 0.4576296748291695 | 0.039035651974590066 | 0.12706799643010336 | 13.484933572995926 | 22.64478165733915 | 51.00547877737253 | 2.2606213141803617 | 48.00087018 | 0.8925047423906567 | 0.03694322880511876 | -0.09787529720285586 | -0.4363936917306951 | 0.05487961603138039 | 1.9243541298465447 | 1.9243541298465447 | 0.23468770829351063 |
| Real Estate (Development) | 20 | -0.025032000000000002 | 0.102755704077572 | 0.020832070614822694 | 0.22528938032472745 | 0.8910740523856756 | 1.236150137 | 0.083479807124 | 0.472235676 | 0.036699999999999997 | 0.4118468434683045 | 0.060434996433102794 | 0.2806887892019545 | 5.366379525383176 | 26.10598173800079 | 68.3350747251621 | 1.5804934348879036 | 48.48671318 | 0.043182666426087354 | 0.03348616710209873 | -0.050122720160957424 | -2.0989368533678903 | 0.033674599509687986 | 0.00046824830538708524 | 0.0004682483053870534 | 0.07587647277787528 |
| Real Estate (General/Diversified) | 12 | 0.02414 | 0.299109748335076 | 0.07412021651272707 | 0.16333180533272215 | 1.501720441937595 | 1.632605338 | 0.10409547757599999 | 0.213498317 | 0.0272 | 0.31238614415155214 | 0.07795017005311067 | 0.2692394619462248 | 6.574292781538342 | 7.675301517588212 | 13.483161886405156 | 0.8838693626073806 | 110.2108117 | 3.4567172653105116 | 0.031953140565959555 | -0.05903978361718297 | 1.3357043750568918 | 0.057098055848105546 | 0.22051996285979572 | 0.2205199628597957 | 0.2945828015156671 |
| Real Estate (Operations & Services) | 57 | 0.03481428571 | 0.05747727315112594 | 0.11469429646037563 | 0.22267816036377994 | 0.6750476077656148 | 0.932613374 | 0.06769589544799999 | 0.391522075 | 0.0327 | 0.37028678480269855 | 0.05171028337550662 | 2.1055907749253833 | 1.3894468679956034 | 12.603884514272561 | 22.98175236680557 | 2.57858277200766 | 32.45852129 | 0.11582206639824974 | 0.012829842363725547 | 0.006379010577416985 | 0.5546662089055828 | 0.11916788901395671 | 0.19232682447345148 | 0.1923268244734515 | 0.057678552033207646 |
| Recreation | 63 | 0.054745161290000004 | 0.09576695680839103 | 0.1408052894258343 | 0.23577664654300043 | 0.7540286170435926 | 0.901774873 | 0.066092293396 | 0.475304332 | 0.036699999999999997 | 0.25195474716110067 | 0.056375080739722826 | 1.6290242703556785 | 2.352410713544046 | 13.310151722367038 | 23.238601870015504 | 6.036733459546793 | 30.51047008 | 0.1867224278728972 | 0.050718173640098174 | 0.04006154803146333 | 0.7392255124980526 | 0.042683431451047166 | 2.6494802576973244 | 2.6494802576973244 | 0.09404506501896871 |
| Reinsurance | 2 | 0.06634999999999999 | 0.06609682681923669 | 0.058995489477871824 | 0.21025686291817458 | 0.7698542925210008 | 0.819046342 | 0.061790409783999994 | 0.148715632 | 0.0272 | 0.2248770959017597 | 0.052482654633590295 | 1.0942237870545661 | 1.1239309680384182 | 14.91480658007074 | 17.188588797649412 | 1.0566302378586874 | 57.39914263 | -0.04075274005652441 | 0.002403437421015142 | -0.0006507203419039086 | 0.1227912526794533 | 0.05002212595490963 | 0.18263298801070887 | 0.18263298801070893 | 0.06538820500448059 |
| Restaurant/Dining | 77 | 0.0791726 | 0.1569187442405256 | 0.19077089336457886 | 0.20490675379032897 | 0.7518963813261236 | 0.97298048 | 0.06979498496 | 0.387566962 | 0.0327 | 0.2940589701868822 | 0.056482939802286754 | 1.5300293281964508 | 4.258470299411251 | 16.879168682463227 | 31.838053804254987 | NA | 38.000133 | 0.0039339512290593875 | 0.06314859645492248 | 0.022158304385445044 | 0.2650301797617754 | NA | 0.5391255107548875 | 0.5391255107548875 | 0.13344885578837354 |
| Retail (Automotive) | 26 | 0.04696666667 | 0.056303707754557966 | 0.09475351502727314 | 0.23494271919905155 | 0.8685186932111402 | 1.332582621 | 0.088494296292 | 0.373701271 | 0.0327 | 0.42153567826618143 | 0.06152895559134145 | 2.2598364984984833 | 1.18936815417058 | 13.90485967314048 | 23.64263496311718 | 6.452961756457515 | 16.61929873 | 0.127478905148987 | 0.02138998743395444 | 0.017016494605353705 | 0.4932611247415884 | 0.34600909753608394 | 0.044208925686026294 | 0.0442089256860263 | 0.048778544423902975 |
| Retail (Building Supply) | 17 | 0.06341230769 | 0.1119544632683398 | 0.28826035423221785 | 0.2515119609149778 | 1.1509711433254448 | 1.358857744 | 0.08986060268799999 | 0.472945897 | 0.036699999999999997 | 0.2045413250822068 | 0.0771103959143985 | 3.0986362163184866 | 2.0295173393333292 | 13.600439116913867 | 18.56937689594026 | 43.04793644962896 | 238.7962998 | 0.07735270607152567 | 0.024169079582853737 | 0.007431396560799115 | 0.2575768436109511 | 0.9480653088518696 | 0.5370743605814186 | 0.5370743605814186 | 0.10931247942899779 |
| Retail (Distributors) | 80 | 0.07226270833 | 0.08350760093148743 | 0.13573769935994287 | 0.23218173288081073 | 0.8937149652220674 | 1.278978137 | 0.08570686312399999 | 0.428307926 | 0.036699999999999997 | 0.37834142231364737 | 0.06369425427680787 | 1.7866917867315544 | 1.3953306758767088 | 12.660195060649688 | 16.14070182313383 | 2.956128105673472 | 897.3225023 | 0.17093500459243968 | 0.07326203174019082 | 0.0924329630617315 | 1.3758605042610925 | 0.16471300547663828 | 0.2890791707999951 | 0.2890791707999951 | 0.08629209597953708 |
| Retail (General) | 18 | 0.01506866667 | 0.04179940261770267 | 0.1381824512217662 | 0.24941902418791229 | 0.9457267947342817 | 1.143699672 | 0.07867238294399999 | 0.404021995 | 0.036699999999999997 | 0.24302062060903565 | 0.06624251419842112 | 4.203397390938218 | 0.8785429822551506 | 12.205636964736465 | 22.574290160507264 | 4.842996302353804 | 18.63648416 | 0.019978328292947316 | 0.02449000536802195 | 0.004875101274221735 | 0.1701453684969305 | 0.18142615744208562 | 0.4444149715432356 | 0.4444149715432356 | 0.038899797234579085 |
| Retail (Grocery and Food) | 13 | 0.05568571429 | 0.02290627550761849 | 0.07127224812519929 | 0.24142139204661636 | 0.3451030636472698 | 0.587786853 | 0.049764916356 | 0.371813722 | 0.0327 | 0.4915054219647012 | 0.037359360617090456 | 4.261853746628345 | 0.486547810972035 | 8.928120898548636 | 25.37183824736728 | 2.6881570995530675 | 395.1439443 | -0.0012327194357372032 | 0.027878366880402124 | 0.006465848516541525 | 0.42706984260082675 | 0.1811190524612434 | 0.341948403816704 | 0.341948403816704 | 0.019174109321536053 |
| Retail (Online) | 70 | 0.1827114815 | 0.06707356575789979 | 0.09994827380025592 | 0.14316009662969226 | 1.1594182467938388 | 1.230127378 | 0.08316662365599999 | 0.559671851 | 0.036699999999999997 | 0.11400951566390057 | 0.0768229490922264 | 1.6500240060316411 | 3.4182355837731984 | 22.820140106083365 | 53.476057410543014 | 13.501193807576541 | 243.8237416 | -0.009887075782535622 | 0.05264802989789804 | -0.0021090758895346896 | 0.21882481173886528 | 0.22405166121112985 | 0.03596044988530687 | 0.03596044988530689 | 0.06240055411774528 |
| Retail (Special Lines) | 89 | 0.07652935484000001 | 0.05761866255503746 | 0.12044980067386891 | 0.22329696913985822 | 0.6903463796794427 | 1.030321235 | 0.07277670421999999 | 0.44947683 | 0.036699999999999997 | 0.4137311525080397 | 0.05405466448010647 | 2.447715535321885 | 1.1873922100308532 | 9.71576074752445 | 21.287033195134274 | 4.568684554463224 | 23.79334505 | 0.08001765097712936 | 0.023882968594784424 | 0.005480938197570402 | 0.2721079284168382 | 0.19919010666178474 | 0.40090750973302247 | 0.40090750973302247 | 0.05584028742935463 |
| Rubber& Tires | 4 | -0.06165 | 0.055145703338559476 | 0.06117086317970651 | 0.4196990768870706 | 0.45318132931651134 | 0.982988968 | 0.07031542633599999 | 0.575891864 | 0.036699999999999997 | 0.6403267674575432 | 0.042915570962138994 | 1.289556108176702 | 0.7428261381555464 | 5.925522703892459 | 12.436737340065022 | 0.8002199749857016 | 21.54909803 | 0.19267145755298817 | 0.05437409351942636 | 0.0030245839790713084 | 0.7734565244622541 | 0.03699469429004548 | 0.7642676779022851 | 0.7642676779022851 | 0.05972174435101638 |
| Semiconductor | 72 | 0.08347660377 | 0.24617957465863774 | 0.17003312768423534 | 0.1408216497210554 | 1.236890276724555 | 1.286598287 | 0.08610311092399998 | 0.436946034 | 0.036699999999999997 | 0.10554597607024396 | 0.07992042703017539 | 0.7128324957137516 | 5.375629898781796 | 13.709577784362965 | 21.65685013854544 | 5.012930763054209 | 97.09367421 | 0.16943441337652326 | 0.14119219281651646 | 0.15698757665339383 | 0.709626696681383 | 0.20294259200072243 | 0.4391416786137753 | 0.4391416786137753 | 0.2537060155019029 |
| Semiconductor Equip | 39 | 0.05314 | 0.19221135954697058 | 0.22138163141196174 | 0.13519564881894938 | 1.2534843105487556 | 1.278467646 | 0.085680317592 | 0.410637031 | 0.036699999999999997 | 0.10852016843933716 | 0.079369292731273 | 1.2285708695769344 | 3.9985726938741943 | 15.708967947601568 | 20.42651240026049 | 5.85095884793239 | 39.72517569 | 0.29004782930000955 | 0.043370906496172555 | 0.11987807265746403 | 0.6903534536289743 | 0.276490636903009 | 0.2919601268040588 | 0.2919601268040588 | 0.19905055440135097 |
| Shipbuilding & Marine | 10 | 0.09778333333000001 | 0.07410946307919881 | 0.06018300644180341 | 0.22817869415807562 | 1.5713945020074378 | 2.173548476 | 0.132224520752 | 0.340543042 | 0.0327 | 0.3577993037545925 | 0.0936897072122311 | 0.7565243915071949 | 1.9791727901491225 | 11.321333330237872 | 23.308228605044718 | 1.3401041855140357 | 25.12694874 | 0.1676229160836365 | 0.12979602606644547 | 0.10470331427657618 | 1.737388807262514 | 0.026936158989395224 | 0.3210577516102164 | 0.32105775161021644 | 0.08364417702794547 |
| Shoe | 11 | 0.0311875 | 0.12473296080179175 | 0.30569969295317156 | 0.15299403610573822 | 0.8336099690951179 | 0.868160264 | 0.064344333728 | 0.375639371 | 0.0327 | 0.08089793385564906 | 0.06112303190189624 | 2.905372550737599 | 3.550348413120501 | 22.079756449155596 | 29.027036966787655 | 12.2113828279578 | 23.09003215 | 0.20764209631388533 | 0.006473322297211257 | -0.008387989603074127 | -0.039956064632188266 | 0.40157200665824816 | 0.2678039825261973 | 0.2678039825261973 | 0.12231477891551373 |
| Software (Entertainment) | 86 | 0.1353454545 | 0.22643820352253305 | 0.17012255734797888 | 0.1877400702926945 | 1.2858744552797758 | 1.288330028 | 0.08619316145599999 | 0.61373099 | 0.036699999999999997 | 0.03659924861463499 | 0.0840459508291083 | 0.7086307349472726 | 6.758744980787946 | 20.596038085418968 | 30.272888882104755 | 5.124484179579928 | 33.97959704 | 0.0669344748310702 | 0.1670723750766019 | 0.12730332043466652 | 0.8560605747676094 | 0.1849199916121045 | 0 | 0 | 0.24566561317284355 |
| Software (Internet) | 30 | 0.3091916667 | 0.09150843077964844 | 0.11121374692689719 | 0.15348344512161763 | 1.5032034061311 | 1.672830078 | 0.106187164056 | 0.447814043 | 0.036699999999999997 | 0.16953539459377637 | 0.09285114303316566 | 1.021077148260791 | 7.636860721738546 | 20.229301923991574 | 58.7595716623212 | 9.386473004673128 | 66.75089323 | 0.09700797811338645 | 0.07808137870985823 | 0.0953222661192251 | 1.5671392920193457 | 0.061366180331456945 | 0.02577724461962498 | 0.02577724461962494 | 0.10993710069848815 |
| Software (System & Application) | 363 | 0.150381338 | 0.22250902833301692 | 0.20028865277858346 | 0.11241556425915916 | 1.149160826869191 | 1.196459765 | 0.08141590777999999 | 0.49502169 | 0.036699999999999997 | 0.08818850894893775 | 0.07666334897697707 | 0.8530194380908113 | 8.765955116906257 | 24.004777377399346 | 35.62444446646148 | 9.91714784915406 | 110.9020732 | 0.13079407113965075 | 0.06515503033020768 | 0.07179937754038616 | 0.4437891506278773 | 0.27914517334435085 | 0.30545961369835267 | 0.3054596136983527 | 0.24057639176907591 |
| Steel | 32 | 0.02289666667 | 0.07750525745579923 | 0.16313788752054129 | 0.1827549310502955 | 1.2855689138232198 | 1.618693392 | 0.10337205638399999 | 0.393878678 | 0.0327 | 0.31959969404403477 | 0.07817256128740083 | 2.2895436673207517 | 0.7014389748884815 | 6.241793307617861 | 8.901586027310056 | 1.4350254465111474 | 14.33817861 | 0.19611343149809785 | 0.05029856783209536 | 0.03322607467770345 | 0.3627147822011634 | 0.184094357942311 | 0.19658827139255067 | 0.19658827139255064 | 0.07851074621566341 |
| Telecom (Wireless) | 18 | 0.0348 | 0.10389000484403538 | 0.05654557535713607 | 0.2525495264443951 | 0.5969080740252654 | 1.142928674 | 0.078632291048 | 0.418491407 | 0.036699999999999997 | 0.5674579887524711 | 0.04963105045931475 | 0.5912180638940506 | 2.4272617034561526 | 6.638899467965102 | 23.870715920618657 | 1.5424136960872281 | 25.6624154 | 0.018494693781414002 | 0.22941027202147374 | 0.033783769370586504 | 1.2392358431543535 | 0.011470180235511362 | 0.1380436777390347 | 0.1380436777390347 | 0.10163146768717307 |
| Telecom. Equipment | 91 | 0.04860807018 | 0.1928205158482047 | 0.2069648259414282 | 0.21979842497473365 | 0.8359786583228734 | 0.894386107 | 0.06570807756399999 | 0.462957187 | 0.036699999999999997 | 0.1469216936530858 | 0.06009815513940997 | 1.0627313871139463 | 3.5022588908180445 | 13.422672645434622 | 17.719960257577117 | 4.999700634600171 | 57.03896354 | 0.18133550969091605 | 0.03166688941593326 | 0.09546868951763805 | 0.6254976691080412 | 0.1757842000608209 | 0.5330595771603518 | 0.5330595771603518 | 0.20318277210670793 |
| Telecom. Services | 67 | 0.10081481480000001 | 0.18292315287117344 | 0.13050207292121768 | 0.18207107946393622 | 0.6665842243194448 | 1.048161411 | 0.073704393372 | 0.544733461 | 0.036699999999999997 | 0.4419401278861309 | 0.05329586635947437 | 0.7556542449680854 | 2.8472602055791407 | 7.931675264412484 | 15.74000688834273 | 2.126308795623589 | 742.0913845 | 0.022549136522870033 | 0.12304058983405936 | -0.02786334942071912 | -0.24935916276364284 | 0.05667739052721064 | 1.7055711191264795 | 1.7055711191264795 | 0.1802234531847927 |
| Tobacco | 17 | 0.03837 | 0.3933715035185512 | 0.5411116801528135 | 0.298915636368754 | 1.426322641272642 | 1.680268449 | 0.10657395934799999 | 0.384851723 | 0.0327 | 0.22214880396163994 | 0.08834688116254458 | 1.553720379106205 | 5.189219949987208 | 12.300311067813483 | 13.163776578702118 | 89.12103701130795 | 24.29860494 | 0.1627749352319938 | 0.02553100757038003 | 0.026509600798475124 | 0.19178992522283614 | -0.00053628983 | 1.4369285357353423 | 1.4369285357353423 | 0.3935174495277971 |
| Transportation | 18 | 0.1435 | 0.05038626377492284 | 0.10453314775070761 | 0.21534808131620617 | 0.9572701695111526 | 1.305169817 | 0.08706883048399999 | 0.279851295 | 0.0327 | 0.35163076925845144 | 0.0650764952585409 | 2.4470701521069755 | 1.3480978064133249 | 12.389069049324025 | 27.532251778605968 | 4.927059241027607 | 58.53407718 | 0.07387083106874129 | 0.07061253093526207 | 0.035895131628456665 | 1.2256040443853642 | 0.21613849696997897 | 0.5998119155153555 | 0.5998119155153555 | 0.04896366334685121 |
| Transportation (Railroads) | 8 | 0.0007825 | 0.38691546827113293 | 0.1543815423746539 | 0.23383391169079815 | 1.8919831806779572 | 2.240425339 | 0.135702117628 | 0.182467472 | 0.0272 | 0.207837719130492 | 0.11173798848928078 | 0.4604085247156745 | 6.3241558799110305 | 12.558258346485765 | 16.55136853584359 | 4.907535770724011 | 20.48236864 | 0.026112811471797132 | 0.16296060925984768 | 0.05937270015682497 | 0.19132085312215535 | 0.2343664303444664 | 0.33856323545498584 | 0.3385632354549859 | 0.3820830005842498 |
| Trucking | 33 | 0.1298442857 | -0.046153607953230216 | 0.0032657923162551002 | 0.26635964891836844 | 1.041066799245524 | 1.372174672 | 0.090553082944 | 0.41853845 | 0.036699999999999997 | 0.3665900406710521 | 0.06744761545414059 | 1.1447242494385363 | 1.9341385570122458 | 9.075523539656658 | NA | 2.811558098597223 | 18.35838149 | 0.0549794297117603 | 0.19435131842924358 | 0.17408014826640636 | NA | -0.32070878705424627 | 0.00137250444 | 0.001372504440000033 | -0.0038289694564948734 |
| Utility (General) | 16 | 0.022726875 | 0.17451490320755897 | 0.0662603132854595 | 0.1442873012882563 | 0.18968841681761509 | 0.283927739 | 0.033964242428 | 0.131125922 | 0.0272 | 0.4010014411514521 | 0.02852496166624433 | 0.4429406176759636 | 4.260403797139058 | 14.125543702097886 | 24.65085900512438 | 2.108218890204647 | 23.72114147 | 0.04183619965168178 | 0.2757063007677103 | 0.26668633284411014 | 1.8550903109476926 | 0.11067375706070938 | 0.7543125579541884 | 0.7543125579541884 | 0.17282983105186767 |
| Utility (Water) | 17 | 0.07540818182 | 0.3025555044003161 | 0.07866652449173686 | 0.22258682397112353 | 0.5653212571240506 | 0.684512515 | 0.054794650779999995 | 0.178805219 | 0.0272 | 0.26337867376499546 | 0.04573583327295343 | 0.2903987700128157 | 8.829237382289845 | 19.018674576688706 | 29.100436380042847 | 3.343326442496564 | 48.12908562 | 0.07229104304760796 | 0.4482032661338867 | 0.3220991266357607 | 1.330458293647536 | 0.13629141248388368 | 0.6660128872086671 | 0.4596915950129533 | 0.3010281333628679 |
| Total Market | 7053 | 0.1014813299804416 | 0.10701158229050306 | 0.07314724979946134 | 0.18570906112791405 | 0.8294537733183968 | 1.1288402320474928 | 0.07789969206646963 | 0.4235641798373163 | 0.036699999999999997 | 0.36710501618937685 | 0.05940688991987342 | 0.7285783919119885 | 3.1581204968108927 | 17.540124294539215 | 28.988607481375357 | 3.2138465226851753 | 70.85149132528615 | -0.23201585849682022 | 0.06149438640029521 | 0.051788077362204275 | 0.6564752998258252 | 0.13629141248388368 | 0.4596915950129533 | 0.4596915950129533 | 0.10813945390506652 |
| Total Market (without financials) | 5878 | 0.10525823607500417 | 0.11153854582174225 | 0.12958913708813033 | 0.18427976475068122 | 1.0124816766847793 | 1.209528030748208 | 0.08209545759890681 | 0.4640609420800599 | 0.036699999999999997 | 0.24014798950007543 | 0.06899047192043022 | 1.2166794125498879 | 2.6248237541350905 | 13.754137505494382 | 22.973319856359776 | 3.885234521085315 | 76.83276051822784 | 0.08906331706100881 | 0.06484993058959562 | 0.05388129715990954 | 0.6682229379634154 | 0.13296367535500786 | 0.5241777361391418 | 0.5241777361391418 | 0.11292179742067442 |

## Industry Average Beta (Global)

| Industry Name | Number of firms | Annual Average Revenue growth - Last 5 years | Pre-tax Operating Margin (Unadjusted) | After-tax ROC | Average effective tax rate | Unlevered Beta | Equity (Levered) Beta | Cost of equity | Std deviation in stock prices | Pre-tax cost of debt | Market Debt/Capital | Cost of capital | Sales/Capital | EV/Sales | EV/EBITDA | EV/EBIT | Price/Book | Trailing PE | Non-cash WC as % of Revenues | Cap Ex as % of Revenues | Net Cap Ex as % of Revenues | Reinvestment Rate | ROE | Dividend Payout Ratio | Equity Reinvestment Rate | Pre-tax Operating Margin (Lease & R&D adjusted) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Advertising | 312 | 0.09085329787234041 | 0.08733141440563327 | 0.20101704822718988 | 0.26806873155806155 | 0.9574823050721607 | 1.1839688309132617 | 0.09236927375043956 | 0.4638520381367773 | 0.045 | 0.3305111645602955 | 0.07289083830066653 | 2.6407069240408267 | 1.707967390757498 | 11.101104372538035 | 18.32173867206054 | 2.202408324270789 | 66.32112107425783 | -0.024289824659392716 | 0.0206011994908111 | 0.030900017458118132 | 0.5424528488372896 | 0.07327405263667701 | 0.7846135511240362 | 0.7846135511240362 | 0.09088243039651404 |
| Aerospace/Defense | 238 | 0.08042547169811319 | 0.09601268590373963 | 0.21648845397482577 | 0.2049196714191956 | 1.0534298484987918 | 1.1848692174836355 | 0.09242491764048867 | 0.37020092658230375 | 0.040999999999999995 | 0.19762076353428135 | 0.08017995616632703 | 2.486424862330909 | 1.999406300395454 | 14.688269155539079 | 20.69337920046813 | 5.189962170204231 | 43.88795356419518 | 0.3333730601585305 | 0.03279607899943966 | 0.048135674000098 | 1.0478815222052293 | 0.220348132128799 | 0.4533968263542013 | 0.4533968263542013 | 0.09799745112347118 |
| Air Transport | 159 | 0.07137528455284552 | 0.08461019493488975 | 0.06644385547900927 | 0.22115600561855384 | 0.6515673034236119 | 1.0957907429349243 | 0.08691986791337832 | 0.306060468343657 | 0.040999999999999995 | 0.5158209102865132 | 0.05779823491437407 | 1.013441077693368 | 1.6360056019638631 | 8.158733896030586 | 20.90783742415074 | 2.003085602246734 | 21.684201294387496 | -0.02923255515634731 | 0.11222623801373716 | 0.04402017230061476 | 0.7186666014004244 | 0.11740561510541049 | 0.4361871973859124 | 0.4361871973859124 | 0.07811252943779379 |
| Apparel | 1161 | 0.008996209386281578 | 0.11537537434511372 | 0.15089152980915196 | 0.25121952050757196 | 0.7003749710772871 | 0.8023763005645276 | 0.06878685537488781 | 0.36299252466639387 | 0.040999999999999995 | 0.2166112339276341 | 0.06048547777326917 | 1.484601906926226 | 2.304326825763532 | 12.577531505262368 | 19.054421182813527 | 3.010658486444328 | 31.981182900709925 | 0.22849175610882147 | 0.04321716806074623 | 0.028151921020307943 | 0.5736013961191143 | 0.11860540439725262 | 0.5315949486697571 | 0.5315949486697571 | 0.11903078219108083 |
| Auto & Truck | 134 | 0.049735151515151524 | 0.04786241623441968 | 0.045965789058890594 | 0.22322622509907264 | 0.8540589604698049 | 1.3742955230193734 | 0.10413146332259728 | 0.33624173982581934 | 0.040999999999999995 | 0.5344225731023865 | 0.06476137359723605 | 1.0556727665465442 | 0.9044047894333606 | 9.808593209386176 | 18.37048728828633 | 1.0299668702548082 | 35.27597818343606 | 0.04630579274915943 | 0.06997238059029952 | 0.041323432321642976 | 1.3203177960638248 | 0.08545789243174735 | 0.45196954382654797 | 0.45196954382654797 | 0.05007733231457238 |
| Auto Parts | 682 | 0.05277552529182879 | 0.05339478498504968 | 0.07458792880825303 | 0.2603309630322867 | 1.1114233776958204 | 1.2611579815235474 | 0.09713956325815523 | 0.34674471803551216 | 0.040999999999999995 | 0.2810527989707697 | 0.07839992852869912 | 1.6247038288899671 | 0.7517595669409293 | 7.077359923526803 | 13.60840186643905 | 1.2909493102437013 | 36.51564969578792 | 0.11537537943209154 | 0.06176659502882899 | 0.05167164227997376 | 1.4317790147158365 | 0.06958721648962074 | 0.4831216324449794 | 0.4831216324449794 | 0.055306825380002235 |
| Bank (Money Center) | 595 | 0.1639120729366602 | 0.0011539329983969104 | 0.0001778792318531151 | 0.1957188919927861 | 0.40180142660318724 | 0.8073309901405032 | 0.0690930551906831 | 0.2253658833963936 | 0.0355 | 0.7114000988787192 | 0.038704493604272874 | 0.13895886488968295 | 7.61751942131696 | NA | NA | 0.9431413155409092 | 14.37763466966554 | NA | 0.036181719580776546 | 0.03358067198591322 | 32.40042683437395 | 0.10935713254419538 | 0.35448740653823124 | 0.3544874065382313 | 0.0016166635557404924 |
| Banks (Regional) | 862 | 0.08365839874411302 | -0.000209994926522575 | -0.00020132545711330538 | 0.18276600406971277 | 0.46490532394693235 | 0.6334948395777614 | 0.05834998108590565 | 0.19975964450888795 | 0.0355 | 0.6095460159046984 | 0.03886067307538763 | 0.21360857037803951 | 4.904337290260387 | NA | NA | 0.7205189715950423 | 14.931548772881358 | NA | 0.03320348637519771 | 0.017820906589753917 | NA | 0.10913620473429567 | 0.2578294478567224 | 0.25782944785672246 | -0.00115916151880788 |
| Beverage (Alcoholic) | 216 | 0.09264556886227546 | 0.21599540019495095 | 0.13242693358909424 | 0.24569440630159284 | 0.800587637762375 | 0.9006272110687749 | 0.07485876164405028 | 0.2917167617441984 | 0.040999999999999995 | 0.1838170375545991 | 0.06669806425866086 | 0.7432235512172697 | 4.269202300129242 | 15.539924680030659 | 19.67997758498457 | 3.641199819476549 | 32.85828364717207 | 0.08696993404927753 | 0.04920553400027366 | 0.014099787924149926 | 0.13517675215987654 | 0.15402255270124898 | 0.45163856248188194 | 0.45163856248188194 | 0.21631758054525274 |
| Beverage (Soft) | 94 | 0.0990201724137931 | 0.1603347644781908 | 0.20208102763036997 | 0.12975927843384175 | 0.7092893218236829 | 0.7924822235276967 | 0.06817540141401165 | 0.34377050760977057 | 0.040999999999999995 | 0.17028713728204806 | 0.06175346453718815 | 1.400232547157348 | 3.6439942262724343 | 17.583050539406774 | 22.49035130142908 | 5.781070411883392 | 72.47550585083277 | -0.044189406869957155 | 0.04707495663444236 | 0.055712076030163475 | 0.40874945035325844 | 0.2679170128825707 | 0.5858253200873939 | 0.5858253200873939 | 0.16170375255959873 |
| Broadcasting | 138 | 0.03516723214285713 | 0.17158735402363495 | 0.16262290740326762 | 0.13014759922291116 | 0.6852414284825481 | 0.9695097818266267 | 0.07911570451688553 | 0.3368717256126117 | 0.040999999999999995 | 0.40211387744780647 | 0.05955177685527828 | 1.1437078690348939 | 2.027893845172074 | 8.455448495351028 | 11.712233065918928 | 1.5622066799670382 | 46.47096233339704 | 0.16958953400285606 | 0.038138867378366643 | 0.14727304591720897 | 1.1222532909403695 | 0.3175833296554515 | 0.4224887564277229 | 0.4224887564277229 | 0.17147866311637552 |
| Brokerage & Investment Banking | 559 | 0.11284615803814707 | 0.009752373545304524 | 0.0014884701262390925 | 0.21262233884574178 | 0.43664122018957785 | 1.0001476218422998 | 0.08100912302985412 | 0.3629329760787471 | 0.040999999999999995 | 0.6855781099521207 | 0.046355807537639376 | 0.17511624841374854 | 7.153782692255459 | NA | NA | 1.4133318216789377 | 60.35596171892798 | NA | 0.05333707120147936 | 0.0482581594468474 | -18.767926998976655 | 0.0900057069464733 | 0.49319033863537054 | 0.49319033863537054 | 0.00990280673436056 |
| Building Materials | 426 | 0.0494075892857143 | 0.08009452761953856 | 0.1072885072738148 | 0.26585590727377045 | 0.8298498654246875 | 0.9647841871293006 | 0.07882366276459077 | 0.31420147626245704 | 0.040999999999999995 | 0.24378593551406627 | 0.06703401335044473 | 1.6006234809146507 | 1.4012821515210603 | 10.754693906466306 | 16.898736863445198 | 2.1453240250192938 | 29.192231305064055 | 0.17224369036565237 | 0.04242888509292137 | 0.031719170748827255 | 0.6698488977906575 | 0.10164853725861189 | 0.3844602377313122 | 0.3844602377313122 | 0.08248730047960598 |
| Business & Consumer Services | 868 | 0.10366239382239385 | 0.08567888014380201 | 0.18809663617793554 | 0.25266819414141234 | 0.8804229892151988 | 0.9992953354386666 | 0.0809564517301096 | 0.4149079603063023 | 0.045 | 0.20832888880820874 | 0.07105636049662292 | 2.542024695938046 | 1.9284260780297844 | 9.732643134514143 | 21.450093482916284 | 4.216896497420578 | 44.55571665019673 | 0.0946007281708728 | 0.028565562352046856 | 0.020387219936289704 | 0.43247408100907514 | 0.1418096442078267 | 0.5162767054320477 | 0.5162767054320477 | 0.08938491311614345 |
| Cable TV | 61 | 0.01556829268292683 | 0.1669331962096465 | 0.10831585003759851 | 0.23734087986037772 | 0.7910340681937198 | 1.1721899981702821 | 0.09164134188692342 | 0.3068879197961914 | 0.040999999999999995 | 0.41619597386865637 | 0.06617916230562572 | 0.7562192194566615 | 3.375389321956226 | 9.657980497348204 | 19.368327197128558 | 2.4220436988638507 | 39.46643340531077 | 0.011150740604818861 | 0.12725033659975662 | 0.10909324247745934 | 0.8716142223756729 | 0.1912080527133254 | 0.16584647686376827 | 0.1658464768637683 | 0.1672198046065474 |
| Chemical (Basic) | 793 | 0.06471770462633454 | 0.07917835071480134 | 0.07837260035028747 | 0.20563261523045673 | 0.9032860152963472 | 1.0649064177508965 | 0.08501121661700539 | 0.32191200321671976 | 0.040999999999999995 | 0.2791299419640967 | 0.0697851760784557 | 1.1706903648937874 | 1.3077381882601595 | 9.603856649466877 | 16.075722931095974 | 1.4917296707810825 | 36.37960472257273 | 0.12241694529122148 | 0.09058954938057395 | 0.06705860120170659 | 1.1742348800341575 | 0.0813212721837475 | 0.7102958953708323 | 0.7102958953708323 | 0.08002534207076183 |
| Chemical (Diversified) | 73 | 0.027063166666666666 | 0.08424619096709755 | 0.07548342560633892 | 0.2429801805657398 | 0.952334541660416 | 1.2175499913522376 | 0.09444458946556829 | 0.29936460025667866 | 0.040999999999999995 | 0.3276589032943011 | 0.07348045203025398 | 1.0793672526640117 | 1.2115414477871753 | 8.186919230239145 | 14.189437765610572 | 1.2984772327771008 | 19.54068185733641 | 0.18889026147159815 | 0.07755512065542802 | 0.06040856327827764 | 1.0920311545047259 | 0.12515300589968698 | 0.4096704104720058 | 0.4096704104720058 | 0.0859623682501244 |
| Chemical (Specialty) | 829 | 0.07546540590405901 | 0.10675773701418523 | 0.10756701934270041 | 0.22760867897224124 | 0.9818941076738789 | 1.1171285033176517 | 0.08823854150503087 | 0.3668006600454801 | 0.040999999999999995 | 0.21066783686827228 | 0.07606709315227292 | 1.171838114964683 | 2.0316601646493138 | 11.481870953121406 | 18.606931547678943 | 2.2783076134842237 | 30.03738382848273 | 0.17680899241553863 | 0.06960696633090567 | 0.0593287989804666 | 0.9236682486665296 | 0.10946237425852257 | 0.47581410665300855 | 0.4758141066530086 | 0.10887679365984387 |
| Coal & Related Energy | 224 | 0.08882982905982909 | 0.16641491839770972 | 0.14758520712864295 | 0.23404373774737955 | 1.274443681628482 | 1.4514847197730736 | 0.10890175568197594 | 0.5546261867925966 | 0.045 | 0.3438653868366696 | 0.08295135054608485 | 0.9807312966972421 | 1.1361507622690643 | 4.527535167571364 | 6.6603073231065375 | 0.9386256236549986 | 17.124322673132458 | -0.022057356968695225 | 0.07828954383900277 | 0.04013618504892986 | 0.33170493761286285 | 0.13055700046708615 | 0.5676684393102985 | 0.5676684393102985 | 0.1670850077987654 |
| Computer Services | 969 | 0.08667462318840577 | 0.07038640630543012 | 0.19831455784437527 | 0.25277327217813444 | 0.9806480666532279 | 1.0800873480285833 | 0.08594939810816644 | 0.39386989062740535 | 0.040999999999999995 | 0.19369657155730127 | 0.07520187302655107 | 3.2769627391792717 | 1.2333339697800174 | 11.794518133165653 | 16.763363655911782 | 3.367008999663801 | 37.80366922086294 | 0.13777218034762756 | 0.016751680137606587 | 0.050639057320800325 | 1.0428839488379344 | 0.1639244216752615 | 0.38371498972436646 | 0.38371498972436646 | 0.07299764161014673 |
| Computers/Peripherals | 332 | 0.03274297188755021 | 0.09993315583286366 | 0.13576268598222516 | 0.1969208953928453 | 1.3493071035123267 | 1.412451969374694 | 0.10648953170735609 | 0.37669919995679946 | 0.040999999999999995 | 0.1464155972763212 | 0.09535806165857637 | 1.5084245104738574 | 1.8377894383671138 | 11.76248456899996 | 18.13798437609278 | 3.812266865451468 | 43.67024971163001 | 0.02709030427270788 | 0.03994109530159869 | 0.020393218711625423 | 0.27844096595003437 | 0.18176452704413582 | 0.34054348452454497 | 0.34054348452454497 | 0.10253727723052218 |
| Construction Supplies | 747 | 0.05042479094076656 | 0.10392836988703523 | 0.11455445938932513 | 0.22704798014607 | 0.9561705566543145 | 1.1491804584012537 | 0.09021935232919748 | 0.3508027682094552 | 0.040999999999999995 | 0.3145677337872806 | 0.07142193199760755 | 1.2825879679904035 | 1.349782912014281 | 8.546023539126065 | 12.496060353878304 | 1.6169804973852047 | 36.03037263185481 | 0.11294840568977452 | 0.04893246164932106 | 0.02449348313062799 | 0.5612173844154965 | 0.12030031453592592 | 0.49327052496328266 | 0.4932705249632827 | 0.10544191540629884 |
| Diversified | 319 | 0.07494141176470591 | 0.11308567291672636 | 0.08734920088627118 | 0.1777456237552578 | 0.6908015362797085 | 0.9303629854722547 | 0.07669643250218534 | 0.2661570545510833 | 0.040999999999999995 | 0.4043350519746439 | 0.058002635168448044 | 0.9021169380292329 | 1.589490177287569 | 9.692307220167429 | 13.77809679257577 | 1.084465772257338 | 27.049435153536695 | -0.1368982467059007 | 0.051088482150126575 | 0.03423622675233194 | 0.5244267278870122 | 0.08241590080620301 | 0.307071838455619 | 0.30707183845561903 | 0.11385563127182309 |
| Drugs (Biotechnology) | 1024 | 0.2299758760107817 | 0.08973037371774621 | 0.07184077342926558 | 0.15183511621953374 | 1.4024111440166125 | 1.427847606081326 | 0.10744098205582595 | 0.6207464670122816 | 0.045 | 0.1094857889215384 | 0.09933837872553063 | 0.4405627067328998 | 7.925212159030943 | 16.0344913193369 | 64.00739472507772 | 6.752642207534174 | 156.2796498503833 | 0.18433726670979367 | 0.054874241788084414 | 0.09746336116443423 | 2.4823054178663537 | -0.020665181213161445 | 0.0022905271565332817 | 0.0022905271565333285 | 0.16484565005932 |
| Drugs (Pharmaceutical) | 1263 | 0.13438102272727265 | 0.18088857741957615 | 0.11951921973153175 | 0.15696550883752958 | 1.1985080632950982 | 1.2967923468416491 | 0.09934176703481391 | 0.5202975828031183 | 0.045 | 0.15454303389746984 | 0.08915633530288002 | 0.7135341361093954 | 4.132788743714877 | 14.498860315614147 | 22.150954034762684 | 3.6640204781539727 | 66.87535838970628 | 0.17686956645803012 | 0.049778433116527736 | 0.06222583260366488 | 0.4697350786571191 | 0.11025315237399004 | 0.7447133187486655 | 0.7447133187486655 | 0.1857060763014871 |
| Education | 211 | 0.06375852173913045 | 0.11433782887841556 | 0.11174300443283466 | 0.19026769380572517 | 1.0234807764447162 | 1.1366672397453836 | 0.08944603541626471 | 0.39389953814831746 | 0.040999999999999995 | 0.2145360483508689 | 0.07679204807831994 | 1.1377612814406424 | 3.1831112714873613 | 15.171288794059196 | 27.656340661115447 | 2.7660222783087045 | 57.39009605998628 | 0.030782614320438047 | 0.06833903506411985 | 0.08498967600454851 | 1.221991579648548 | 0.117598775427412 | 0.34153641320785494 | 0.3415364132078549 | 0.11321578675859927 |
| Electrical Equipment | 902 | 0.07894681444991787 | 0.07073455540802188 | 0.11584011996292115 | 0.20165042855861437 | 1.146287349436663 | 1.2804607867153421 | 0.09833247661900814 | 0.38217637423395207 | 0.040999999999999995 | 0.22416958430026196 | 0.08311820425864873 | 1.324302803739664 | 1.702037386547068 | 10.360901926891788 | 16.587100652391737 | 2.2775284895534886 | 53.30971170247794 | 0.237902446800546 | 0.047404077762603095 | 0.036554952268916016 | 0.8273874559386403 | 0.06696460990026057 | 0.6713272885755581 | 0.6713272885755581 | 0.0999179737594785 |
| Electronics (Consumer & Office) | 142 | 0.014216372549019614 | 0.04824459216964682 | 0.09405811287108841 | 0.11195830875702079 | 1.300002808253641 | 1.4512658895581136 | 0.10888823197469141 | 0.4085541195810068 | 0.045 | 0.27964914687256404 | 0.08778780002419129 | 1.841169830789388 | 0.7751313992577439 | 7.9389132940333775 | 14.717521795552267 | 1.634007982340785 | 56.46579370665613 | 0.02413584131373336 | 0.04396453671413224 | 0.036851128852855505 | 1.2171862671751041 | 0.13133087797579038 | 0.23699262136696117 | 0.2369926213669612 | 0.0564019137644148 |
| Electronics (General) | 1345 | 0.06116192231075692 | 0.060548354049097475 | 0.08611583516623587 | 0.21000135507359874 | 1.3817241330917154 | 1.3992918291192586 | 0.10567623503957017 | 0.3966702302649589 | 0.040999999999999995 | 0.15060360451192606 | 0.0943488507356082 | 1.553937801461869 | 1.4573693138125619 | 13.09257985239928 | 23.095397724536703 | 2.3731560391858024 | 54.11106548589247 | 0.17294007917473425 | 0.06445782875737087 | 0.050271659260413236 | 1.3896695159616808 | 0.07904845940592937 | 0.4878630469644681 | 0.48786304696446803 | 0.06368923959300582 |
| Engineering/Construction | 1208 | 0.046789758269720115 | 0.05285936305691498 | 0.09509737554785434 | 0.25038055688867705 | 0.8099875352902434 | 1.1004589935444633 | 0.08720836580104782 | 0.36528624125554293 | 0.040999999999999995 | 0.4760161493914744 | 0.06019665527662238 | 2.074389687962078 | 0.6407837444773156 | 8.215070546657708 | 11.61718250867424 | 1.110943022343258 | 52.5617563033992 | 0.15407814820617333 | 0.033673238704949024 | 0.03523969278509402 | 1.5687799543147374 | 0.09572335213142939 | 0.5293871745718931 | 0.5293871745718931 | 0.055431283339838974 |
| Entertainment | 660 | 0.13369196185286109 | 0.11769786115800492 | 0.12776641397737543 | 0.22573674649490091 | 1.170486437164519 | 1.259567582347123 | 0.0970412765890522 | 0.4801171749550194 | 0.045 | 0.16332628298773633 | 0.08665269985907244 | 1.2337902044429534 | 3.9049242005015166 | 19.033568038085082 | 32.63384744905579 | 3.250237868547838 | 52.252289754181774 | 0.05107553473834756 | 0.04601277068178903 | 0.05186487678565838 | 0.7228508719784478 | 0.09106903049529329 | 0.3758570631038926 | 0.37585706310389266 | 0.11413684515633774 |
| Environmental & Waste Services | 325 | 0.11699615384615386 | 0.10428205249110145 | 0.12530926577306817 | 0.22232756419999217 | 1.0108895954007615 | 1.2165784087388196 | 0.09438454566005905 | 0.4382407138678574 | 0.045 | 0.27007088423566467 | 0.07792384796988487 | 1.3546072679077885 | 2.4761615532168073 | 13.458279246366613 | 22.782829741013174 | 2.946484117711662 | 139.85974331268054 | 0.11578888566052492 | 0.0956867935617069 | 0.07426740361354325 | 1.2674716863718152 | 0.07720525929067341 | 0.6924364739221655 | 0.6924364739221655 | 0.10680689168821217 |
| Farming/Agriculture | 406 | 0.08357417910447767 | 0.047032114142262424 | 0.05383688102317684 | 0.19905884239659155 | 0.6004760571400259 | 0.8165201752326893 | 0.06966094682938019 | 0.38163047797118665 | 0.040999999999999995 | 0.369670221928746 | 0.05517063312581203 | 1.2797283591998483 | 1.2035865141777065 | 13.81388001387652 | 23.864291149688935 | 1.8348674645740137 | 79.74600304129041 | 0.15693256264053676 | 0.04937023805345629 | 0.03410734699939085 | 1.1279388683051466 | 0.06746814419122583 | 0.5443572652120209 | 0.5443572652120209 | 0.04792849369620472 |
| Financial Svcs. (Non-bank & Insurance) | 1059 | 0.13239517391304345 | 0.06774228095402572 | 0.003925050211504958 | 0.18190212777423673 | 0.14956422652348697 | 0.7891624202339724 | 0.0679702375704595 | 0.34529993937082754 | 0.040999999999999995 | 0.8627882099436442 | 0.035609435207111746 | 0.06988695052239982 | 15.973567311016513 | 152.5233407294965 | NA | 1.3513574663896395 | 69.44781591646621 | NA | 0.06892277801392457 | 0.06955802731868602 | 1.9510578436951003 | 0.20622625054362026 | 0.21148798294263862 | 0.2114879829426386 | 0.06645532093601864 |
| Food Processing | 1262 | 0.06398863839285716 | 0.08528946373931369 | 0.11936370398267163 | 0.21384248464496677 | 0.6501170844484848 | 0.7499572266099076 | 0.06554735660449229 | 0.32018900857587657 | 0.040999999999999995 | 0.2154218756983916 | 0.0579894186970813 | 1.6576475109940005 | 1.7329544653534938 | 13.717702115248796 | 20.0804217641832 | 2.747629409766204 | 41.67674372775768 | 0.10504668502667278 | 0.04608102687827592 | 0.03769290844065906 | 0.6230466215302776 | 0.07940821183188783 | 0.7452932121178012 | 0.7452932121178012 | 0.0856699631547964 |
| Food Wholesalers | 151 | 0.1559560396039604 | 0.0241586881177102 | 0.10673155089282349 | 0.26080951403938457 | 0.5184929633658631 | 0.7564156779994284 | 0.06594648890036468 | 0.3419801301460577 | 0.040999999999999995 | 0.42733054467883297 | 0.05078331026146652 | 5.208436779129817 | 0.48139534295222036 | 11.42728675780776 | 19.273881451187073 | 2.0735287535668636 | 51.75355987272999 | 0.048434790391602804 | 0.015009878205822403 | 0.01723546203934762 | 0.9845680768103174 | 0.09126999795593271 | 0.5452096350989162 | 0.5452096350989162 | 0.024825535666774243 |
| Furn/Home Furnishings | 328 | 0.06491182608695654 | 0.07427039909509768 | 0.1555536176846134 | 0.18576809374079462 | 1.0058522471944715 | 1.0262217610131108 | 0.08262050483061024 | 0.34400720365518467 | 0.040999999999999995 | 0.19345939891845115 | 0.07253014529699417 | 2.4084220959076457 | 1.1888969242664889 | 10.925249857094558 | 15.276255125764791 | 2.7210955585919785 | 28.37167500637877 | 0.04772416831404232 | 0.034835143203373393 | 0.02633918169354584 | 0.5442313129834635 | 0.1426138875345963 | 0.4921006256161733 | 0.4921006256161733 | 0.07711994429690737 |
| Green & Renewable Energy | 213 | 0.23736264150943395 | 0.35647891232232615 | 0.07110563159403839 | 0.1670100441852725 | 0.5867303342285284 | 0.8869688582861294 | 0.07401467544208279 | 0.38025489613951263 | 0.040999999999999995 | 0.4351853252877875 | 0.05506162539799184 | 0.23075931442160308 | 6.7575144931383075 | 11.569542801526575 | 19.232600522563455 | 1.7201786345229257 | 105.76953384548527 | 0.04847419776191747 | 0.2876724673838901 | 0.13757437621807073 | 0.699007139605091 | 0.1043101228470741 | 0.7784050899643815 | 0.7784050899643815 | 0.3486054877138123 |
| Healthcare Products | 739 | 0.11377816176470593 | 0.14871035922653414 | 0.14019710672728616 | 0.1527831295407561 | 1.1331289139797711 | 1.195919409632218 | 0.09310781951527107 | 0.4835661602874414 | 0.045 | 0.11060423596136852 | 0.08650775290512387 | 0.9675679144032145 | 5.173027909166 | 21.34791534773662 | 33.228231724713375 | 4.561239377591697 | 52.186073830216436 | 0.24355953159634902 | 0.053561132939922394 | 0.0642847141763407 | 0.7305603348220906 | 0.09694961173940185 | 0.3800613869848959 | 0.3800613869848959 | 0.15653695961206693 |
| Healthcare Support Services | 402 | 0.18364475336322875 | 0.04500502486244765 | 0.2722803124319694 | 0.23625082881169265 | 0.8183860919317326 | 1.0101052155748032 | 0.08162450232252283 | 0.3981792118313983 | 0.040999999999999995 | 0.29354555166461066 | 0.06660627089926761 | 7.265839638260834 | 0.7223881734452577 | 11.553106130105933 | 16.133584067510697 | 2.5486191100303244 | 36.1817771985606 | -0.012459361581455488 | 0.010041260282993932 | 0.04640308430329437 | 1.5730923352962158 | 0.12273180258406703 | 0.3905260270099705 | 0.3905260270099705 | 0.04411393080878575 |
| Heathcare Information and Technology | 389 | 0.17155423076923074 | 0.12304597355065522 | 0.13077224191903541 | 0.15757461687726282 | 1.225383329091867 | 1.295587118792645 | 0.09926728394138547 | 0.537553858180008 | 0.045 | 0.10755509414364806 | 0.09218668644437839 | 1.0975590157336705 | 5.709289187654166 | 24.814820542026666 | 42.35291241428911 | 5.532510441690977 | 770.4221620088854 | 0.20890982862970453 | 0.056204539819045385 | 0.06402239409028629 | 0.852209206790172 | 0.1018447730736845 | 0.1526881312090691 | 0.1526881312090691 | 0.12884348872191762 |
| Homebuilding | 167 | 0.11342669291338581 | 0.10694586777644409 | 0.10539983401041551 | 0.23867718585367972 | 0.7482870371272902 | 0.8856999147572187 | 0.07393625473199611 | 0.3229008226926812 | 0.040999999999999995 | 0.30137369606398984 | 0.06083455927348311 | 1.3530564092282296 | 1.1540190932813916 | 9.286781987938015 | 11.47000595509807 | 1.5844122484643632 | 16.176649935621874 | 0.5954045841693287 | 0.012065167258743518 | 0.012576183073203217 | 0.6200163210126075 | 0.14765497101637146 | 0.2181782960456158 | 0.21817829604561578 | 0.09990940093033994 |
| Hospitals/Healthcare Facilities | 206 | 0.07814309352517985 | 0.10338966407130139 | 0.09522532460359966 | 0.2167633128608968 | 0.5039735140504044 | 0.7800582660432619 | 0.06740760084147358 | 0.31468967198399317 | 0.040999999999999995 | 0.44480755032156744 | 0.0509743634435696 | 1.216662210452611 | 2.218070093012389 | 12.002033654347525 | 22.92088245826187 | 3.423003194555971 | 39.72259180834589 | 0.07558586592422534 | 0.06923805471260874 | 0.05698406172530164 | 0.9592907281259507 | 0.12874142029551164 | 0.39649563044065905 | 0.39649563044065905 | 0.09353716903320555 |
| Hotel/Gaming | 639 | 0.13215739224137918 | 0.1432728014853443 | 0.08802262264648508 | 0.18608642329791938 | 0.6849051024844033 | 0.8959503270691579 | 0.07456973021287396 | 0.34668398329402567 | 0.040999999999999995 | 0.3466426355339266 | 0.05928045700709946 | 0.7665763910842833 | 3.0255533069397207 | 12.388248799990457 | 22.43471949792487 | 2.375532095346927 | 53.14713225923438 | 0.0012774029579377944 | 0.0860295281252565 | 0.05460079075323021 | 0.5735012675568913 | 0.11443960088095181 | 0.5295443807244008 | 0.5295443807244008 | 0.13360622867128247 |
| Household Products | 536 | 0.07904667785234899 | 0.16390003516815946 | 0.2283602986688878 | 0.24375406963667737 | 0.9641176499316831 | 1.0309988968253856 | 0.08291573182380882 | 0.4058252173909233 | 0.045 | 0.1257012406888027 | 0.07669594244336612 | 1.5955418553932443 | 3.4038102627840923 | 16.097075198703642 | 20.520865985113677 | 5.964047051031478 | 73.76822386751435 | 0.06709801018873927 | 0.03821049866067796 | 0.03472456845993887 | 0.3025769020103188 | 0.16302209669156703 | 0.7439324776380757 | 0.7439324776380757 | 0.16530851382117287 |
| Information Services | 215 | 0.14939829268292687 | 0.25329954682361056 | 0.3682643371559208 | 0.1948184067460695 | 1.0458294791273943 | 1.1024635466817168 | 0.08733224718493009 | 0.4125850801465365 | 0.045 | 0.1080505394465429 | 0.08150862055191473 | 1.6504961588511904 | 8.124142927653272 | 25.296941911617193 | 31.211612588222373 | 6.277700229092158 | 39.067948897993524 | 0.06869316164268364 | 0.03257343265556052 | 0.14105276792267565 | 0.7866434969689869 | 0.27329962763586685 | 0.2639853768628828 | 0.2639853768628828 | 0.255921843055534 |
| Insurance (General) | 216 | 0.06473521978021983 | 0.09533369672453942 | 0.13442843031225699 | 0.24163191786201185 | 0.5355173012771018 | 0.6139594110120449 | 0.057142691600544374 | 0.2682809916831763 | 0.040999999999999995 | 0.29763459747756726 | 0.04920189233019071 | 1.663311433601559 | 1.079049452728 | 9.051042205755335 | 11.05289144928991 | 1.3289349091090603 | 28.437897170088362 | -0.010624191690262528 | 0.007281347315751534 | 0.022365132665681485 | 0.3587494126173865 | 0.09621087701289938 | 0.4978569881906221 | 0.4978569881906221 | 0.0953806092263949 |
| Insurance (Life) | 137 | 0.10359295238095237 | 0.09208420912334492 | 0.11582969840439336 | 0.1666158228494693 | 0.9778481143959333 | 0.991516406340754 | 0.08047571391185859 | 0.2589046978482647 | 0.040999999999999995 | 0.44928512091235506 | 0.05800574569481418 | 1.4884238388859743 | 0.8872115316497294 | 8.848306312332586 | 9.520480497014868 | 1.0292727525843677 | 24.899585711654137 | -1.0044102300193347 | 0.006926955927710461 | 0.0046127268550345876 | 0.06294185694985728 | 0.11231423959720833 | 0.2903368487723541 | 0.2903368487723541 | 0.09247021274593563 |
| Insurance (Prop/Cas.) | 223 | 0.0588560451977401 | 0.0872356394478015 | 0.09629764245758336 | 0.18045735376321356 | 0.5023697504648265 | 0.5554564620295073 | 0.05352720935342355 | 0.24733885542106424 | 0.0355 | 0.22827737821330524 | 0.04732931660559255 | 1.3256871108060282 | 1.1122383340104949 | 10.561377706227253 | 12.532749511124193 | 1.2952974769035155 | 42.814355124517895 | -0.377190498019406 | 0.008584844164901307 | 0.0013950980996996396 | 0.1163659876199962 | 0.09585622920660336 | 0.3663809997712803 | 0.36638099977128036 | 0.08727885846058635 |
| Investments & Asset Management | 1066 | 0.10670904365904363 | 0.1876954988569685 | 0.0527043341865464 | 0.16797360953270513 | 0.5492734103196246 | 0.8122627940060927 | 0.06939784066957652 | 0.3710678154909745 | 0.040999999999999995 | 0.4776565900519865 | 0.0508003574411292 | 0.3119073724447553 | 4.8772914157786165 | 20.144524246716315 | 24.683910064511462 | 1.3553497259263956 | 119.48178666794966 | NA | 0.02603788992469188 | 0.1436112547400981 | 1.1990457022408318 | 0.10247498353682159 | 0.48832724110764086 | 0.4883272411076409 | 0.1826429844900817 |
| Machinery | 1332 | 0.05507222680412374 | 0.09018753774635012 | 0.12219377289173415 | 0.23770177268803105 | 1.164533521118772 | 1.2519781633114297 | 0.09657225049264635 | 0.35086529691748397 | 0.040999999999999995 | 0.18057072971435076 | 0.08463485489032041 | 1.5022194598697762 | 1.764647124143704 | 12.211193729829086 | 17.970811515180685 | 2.5404367781412125 | 37.29680705608225 | 0.2525747281572983 | 0.04317702706189114 | 0.050964659542782745 | 0.9644955297084434 | 0.10330478381311581 | 0.4450182292544439 | 0.4450182292544439 | 0.09806614525318494 |
| Metals & Mining | 1529 | 0.11404895878524951 | 0.08965279354741407 | 0.10096648806580472 | 0.3133014220474483 | 1.094059867642693 | 1.334635891521627 | 0.10168049809603655 | 0.712858057047975 | 0.0525 | 0.3123821200115582 | 0.0821025740833163 | 1.1621302506502944 | 1.259531190625973 | 7.570504325227937 | 13.196515705796992 | 1.4410783825453035 | 155.3781782004618 | 0.09457040080219034 | 0.0789149577711148 | 0.045677057636889985 | 0.7683877805591145 | 0.0755974481155654 | 0.7672154620647981 | 0.7672154620647981 | 0.09079267230897888 |
| Office Equipment & Services | 146 | 0.031321192660550466 | 0.07238159733438726 | 0.13161293408359542 | 0.26840993310420147 | 0.9376447183289379 | 1.0445634208998078 | 0.08375401941160812 | 0.36388417310049775 | 0.040999999999999995 | 0.2524791057965059 | 0.07029915048358107 | 2.0861794362128547 | 1.0639312845321147 | 9.290283743579279 | 14.132162810733927 | 2.0260981588328133 | 28.860055286740963 | 0.13644124446470532 | 0.02606512204907037 | 0.009428415127349205 | 0.34865185377658825 | 0.09189047940229653 | 0.4720322109333745 | 0.47203221093337455 | 0.07535073394497097 |
| Oil/Gas (Integrated) | 49 | 0.007507804878048779 | 0.13109959541353317 | 0.1369516653438469 | 0.3957474172433126 | 1.1401792895983085 | 1.2957860981562233 | 0.0992795808660546 | 0.2881574692678422 | 0.040999999999999995 | 0.20730831057029125 | 0.08501333174748898 | 1.3818883044795371 | 1.4220944873741248 | 6.7663076637140005 | 11.008172308021313 | 1.742280207304061 | 23.56117359113449 | 0.02750663313729373 | 0.09029945070758316 | 0.03441979549233193 | 0.3993015293496522 | 0.14151899193172254 | 0.6350895531801765 | 0.6350895531801765 | 0.12918851521834027 |
| Oil/Gas (Production and Exploration) | 773 | -0.009602061068702315 | 0.21981338598940317 | 0.09098173754986873 | 0.27002127840639994 | 1.144320485233247 | 1.5514780345232326 | 0.11508134253353577 | 0.6368728119152843 | 0.045 | 0.3620777687240042 | 0.08551901700451739 | 0.4321181518475273 | 2.7746029803914656 | 5.136003662537055 | 12.256217476708347 | 1.1115091134834114 | 21.494267836297507 | 0.030222768100608772 | 0.35122904141823136 | 0.11107250385867352 | 0.6612900541482126 | 0.062227442417112096 | 0.5666799105612945 | 0.5666799105612945 | 0.22310557289136723 |
| Oil/Gas Distribution | 160 | 0.16266342592592586 | 0.13764106149209218 | 0.07242633745048382 | 0.17466296152727728 | 0.826498511667143 | 1.284519579311278 | 0.09858331000143698 | 0.33564192954750244 | 0.040999999999999995 | 0.44484075792465516 | 0.06828061967033529 | 0.5886667859021754 | 2.856233209737333 | 12.796943816486792 | 20.580210713925556 | 1.571090493924707 | 25.88813288146477 | 0.032992409412551355 | 0.17096661654853032 | 0.10593171124848665 | 0.9224233050424607 | 0.07202420966002927 | 1.2474336829679866 | 1.2474336829679866 | 0.13694775348672555 |
| Oilfield Svcs/Equip. | 508 | -0.009004062500000003 | 0.040123058864194136 | 0.08219064924164957 | 0.2593161951561427 | 1.0641191695035244 | 1.4085665192825956 | 0.1062494108916644 | 0.449673037548957 | 0.045 | 0.35827861367981534 | 0.08016156470148644 | 2.2417445395943716 | 0.7388990750329275 | 9.450976485239003 | 17.8272796202009 | 1.4267561678950909 | 32.97171433975635 | 0.057375218269329356 | 0.04243797157106362 | 0.022712263078881748 | 0.6999826723464472 | 0.000145022841711534 | 0.0063520856311457645 | 0.006352085631145754 | 0.040881253051559124 |
| Packaging & Container | 400 | 0.058877880794702006 | 0.08946354069501929 | 0.11674190130975308 | 0.22958340808282582 | 0.607320943408075 | 0.8168992822654855 | 0.06968437564400701 | 0.35407118177715896 | 0.040999999999999995 | 0.35422384567092174 | 0.05579122913088302 | 1.5509105252362714 | 1.4305643992275618 | 9.328720681047674 | 15.57817874342177 | 2.2439903531804557 | 31.035755025785154 | 0.1382971796612512 | 0.05950939965786715 | 0.08497730598816264 | 1.2423257835779116 | 0.09919779496675742 | 0.5244236987817754 | 0.5244236987817754 | 0.09139948472674 |
| Paper/Forest Products | 279 | 0.06515040540540537 | 0.07672692223216482 | 0.06506386072885632 | 0.21911751388685427 | 0.7409056418529129 | 1.0267113824102914 | 0.082650763432956 | 0.3534610963372517 | 0.040999999999999995 | 0.3973125153426118 | 0.06191591187330308 | 0.9801927467530284 | 1.3040643317926544 | 9.42369828821916 | 16.72555332449765 | 1.2683112873626812 | 31.859042795805642 | 0.1879279234724347 | 0.0688009493654385 | 0.06815858382770143 | 1.2322155873874094 | 0.054321572075995236 | 0.7254843093551767 | 0.7254843093551767 | 0.07716748319110982 |
| Power | 538 | 0.0697159027777778 | 0.126201945434601 | 0.0616863296449616 | 0.19465700965260932 | 0.5050604986216313 | 0.8247373670536474 | 0.07016876928391541 | 0.2659716679633612 | 0.040999999999999995 | 0.4863461556020854 | 0.05085802103745978 | 0.6027979981993015 | 2.254221495716043 | 9.680692124812317 | 17.844814136467285 | 1.3300226422708623 | 29.29091828575206 | 0.014584068958973522 | 0.15902933532528227 | 0.0823772076297145 | 0.9117514185300404 | 0.07856767530460744 | 0.689656884501097 | 0.689656884501097 | 0.12440659769151537 |
| Precious Metals | 844 | 0.18559461883408074 | 0.09711169949128218 | 0.06805188461060296 | 0.3432123205165655 | 0.9983432046775572 | 1.0764491693911828 | 0.0857245586683751 | 0.8136897019026077 | 0.0775 | 0.16000992472075454 | 0.08122154997936135 | 0.716402693063831 | 3.13654165331937 | 10.99996267026761 | 29.81071229235866 | 2.0400298983499816 | 75.40682593044642 | 0.12299808581222174 | 0.1740760619960503 | 0.07510725977184714 | 1.6889508049167774 | 0.03559673192516782 | 1.001241683727843 | 1.001241683727843 | 0.0987733826897146 |
| Publishing & Newspapers | 352 | 0.009615296442687755 | 0.059456658645740054 | 0.0724248633313697 | 0.24197154470385415 | 0.8520217460955231 | 0.9566188459570709 | 0.07831904468014698 | 0.37946234248709476 | 0.040999999999999995 | 0.28480111968184063 | 0.06468958957169693 | 1.4619259113046699 | 1.2177476981960762 | 10.07250134540489 | 19.765394967884895 | 1.4382062980195205 | 88.4911857942591 | 0.12508062081341545 | 0.035417281465972124 | 0.018512873041220596 | 0.3761088971505667 | 0.027924217771103692 | 1.265445655862366 | 1.265445655862366 | 0.05835447554896081 |
| R.E.I.T. | 753 | 0.1128328278688525 | 0.35993627620012686 | 0.03482662447168492 | 0.03373109962535656 | 0.34523746097470087 | 0.532484960284419 | 0.05210757054557709 | 0.18536628816240472 | 0.0355 | 0.43483135318088056 | 0.040918894321451106 | 0.10824190098808936 | 13.77670810237405 | 23.05837781358625 | 36.573947320283125 | 1.6749590563587815 | 65.47539513006475 | 0.6689286402087816 | 0.06295289124536624 | 0.016511084651054345 | 0.05611043269263187 | 0.06114146614640298 | 1.1869396388310514 | 1.1869396388310514 | 0.3310957003865064 |
| Real Estate (Development) | 842 | 0.1209779900332226 | 0.20383784791336962 | 0.09106983784768014 | 0.3544566186959404 | 0.6358633022030139 | 1.0752365872116536 | 0.08564962108968019 | 0.33036699251442664 | 0.040999999999999995 | 0.6001679432737542 | 0.05252838021405884 | 0.5458397967979985 | 2.1019458364157995 | 9.452238945778639 | 10.108021135618332 | 0.8555204820770472 | 48.490655277372944 | 1.6131076344036095 | 0.029086903150392654 | 0.048785443080569 | 1.3377306187540148 | 0.12825494782302443 | 0.5702031961402876 | 0.5702031961402876 | 0.2032969220209528 |
| Real Estate (General/Diversified) | 383 | 0.08630114197530867 | 0.1983216445475487 | 0.048869941498554975 | 0.22669290964855524 | 0.6422762383369989 | 1.0120709473405611 | 0.08174598454564667 | 0.29901471534648544 | 0.040999999999999995 | 0.4948716044440605 | 0.05636749170286255 | 0.2893815969135539 | 3.4326594185486994 | 12.78582341652988 | 16.872006066024284 | 0.7250611724739213 | 39.257621050359035 | 0.8431647010014772 | 0.08667462877031676 | 0.10273835713129928 | 1.3072468423110726 | 0.07655841688936918 | 0.4085743630190399 | 0.40857436301903993 | 0.19868673568450781 |
| Real Estate (Operations & Services) | 691 | 0.07880383771929825 | 0.22999468418293015 | 0.04119789607976516 | 0.20495001126935083 | 0.49377906135395283 | 0.7158961856606553 | 0.06344238427382849 | 0.3157066314750875 | 0.040999999999999995 | 0.41955717848392365 | 0.04960564685976392 | 0.20713835833671432 | 5.635139127263615 | 17.0155832186791 | 23.004922082382002 | 1.0099484780001227 | 429.93353824487235 | 0.21015044461719662 | 0.04660383646625189 | 0.045701351243339704 | 0.36886203189040634 | 0.08114350771634278 | 0.3020546686828527 | 0.3020546686828527 | 0.23217400356367204 |
| Recreation | 315 | 0.0387552073732719 | 0.1104227483742922 | 0.10089221673315414 | 0.2532398879894154 | 0.8382133778789966 | 0.924366597869494 | 0.07632585574833473 | 0.3772396888897552 | 0.040999999999999995 | 0.21958671036274224 | 0.06625498212671692 | 1.0737637509041547 | 2.5141389427594936 | 13.358837559477944 | 21.67858307860609 | 2.969366073040996 | 40.72937177995035 | 0.22900194588191186 | 0.06190022953004165 | 0.039203645168466826 | 0.9536450983436876 | 0.07682173177094892 | 0.6619626591152274 | 0.6619626591152274 | 0.11028814442769304 |
| Reinsurance | 34 | 0.04681259259259259 | 0.05898881747132159 | 0.07631975469681297 | 0.17681743015310628 | 0.9199037070292533 | 0.949214676475434 | 0.07786146700618182 | 0.23606953816563966 | 0.0355 | 0.1910988807366684 | 0.06802274743653618 | 1.4907288480712617 | 0.8789939988860236 | 13.21909695507575 | 14.84405900776726 | 1.1149384137828904 | 19.609752169849994 | -0.4551412428352204 | 0.0043772630848483395 | 0.006865454056624295 | 0.2782356068307982 | 0.06116585315106086 | 0.590328811202473 | 0.590328811202473 | 0.058945730557045016 |
| Restaurant/Dining | 376 | 0.06697100000000003 | 0.10978382925321947 | 0.15300838609033485 | 0.22431969233325166 | 0.6672003450972904 | 0.8472048185802411 | 0.0715572577882589 | 0.3439977746341815 | 0.040999999999999995 | 0.29336266270734834 | 0.05950173690151308 | 1.8252517838077875 | 2.7801187999595762 | 14.986211549385093 | 27.460190614322606 | 13.250707227107672 | 75.36506179399919 | -0.015110628531521036 | 0.04861207102955728 | 0.023043884785558254 | 0.3287168199114364 | 0.4210425338512923 | 0.5285015521464069 | 0.5285015521464069 | 0.10074955293383793 |
| Retail (Automotive) | 184 | 0.08157343283582094 | 0.042859370377592326 | 0.0787349372126706 | 0.25018240554327875 | 0.6624157829951878 | 0.9767463958647935 | 0.07956292726444424 | 0.3444876882887662 | 0.040999999999999995 | 0.4219321226075757 | 0.058846090733879704 | 2.507400153306824 | 0.8559103880170308 | 12.086402963062389 | 21.27106018242833 | 3.0878339469672453 | 42.52363873873882 | 0.11143248741714006 | 0.02509053146064916 | 0.01809641975747521 | 0.770435363242412 | 0.1486211832570094 | 0.34166447620701973 | 0.3416644762070198 | 0.03883069293886377 |
| Retail (Building Supply) | 93 | 0.04141716417910447 | 0.09776041323422738 | 0.19060188954944826 | 0.2570222890233324 | 0.9029009394098382 | 1.082609955508654 | 0.08610529525043481 | 0.3634296826759884 | 0.040999999999999995 | 0.23069613644942932 | 0.07326883271298106 | 2.4865199894921326 | 1.7905120643841668 | 12.881318467086654 | 18.866127646235903 | 9.456109751030388 | 65.76651349148034 | 0.08014561173952703 | 0.024212187947907117 | 0.006497742442476979 | 0.26619837402300656 | 0.32904708372706254 | 0.5440265190804204 | 0.5440265190804204 | 0.09487827370464562 |
| Retail (Distributors) | 982 | 0.11517992907801416 | 0.04100691894968588 | 0.06791945881345267 | 0.23332191516922982 | 0.6005287068795987 | 0.9203938950562521 | 0.07608034271447638 | 0.36068173383469204 | 0.040999999999999995 | 0.47796963135924625 | 0.0542766382336497 | 1.9436816791671818 | 0.719184061178718 | 10.900637897546464 | 16.714995419812407 | 1.2847610358944161 | 114.37493779063372 | 0.13943033141052072 | 0.029956588457576802 | 0.02604783108607248 | 0.4695896471720429 | 0.1043686316337913 | 0.4046631994442323 | 0.40466319944423224 | 0.04218549541734958 |
| Retail (General) | 210 | 0.01561876404494382 | 0.04294808336736141 | 0.08367937158790612 | 0.2800489268408578 | 0.8551483194122819 | 1.1193938285891893 | 0.0883785386068119 | 0.2910392391283711 | 0.040999999999999995 | 0.3347355923577821 | 0.06899214648454072 | 2.763780581803851 | 0.9094444894868662 | 11.217753573611496 | 23.188277470998234 | 2.8528467164366766 | 36.01020384673554 | -0.004254171222038816 | 0.02870333463086686 | 0.007427207476215547 | 0.3289139520593158 | 0.11465693170088317 | 0.501988995258101 | 0.501988995258101 | 0.039129380731371524 |
| Retail (Grocery and Food) | 170 | 0.03248 | 0.036910918471386604 | 0.07756011016212236 | 0.26876073798896255 | 0.4949379666364981 | 0.7274610930329879 | 0.06415709554943864 | 0.29305447069022006 | 0.040999999999999995 | 0.43750246258540504 | 0.049415845771971306 | 3.026424650453173 | 0.7399373017909439 | 9.473404286633446 | 22.479328564728206 | 2.0717852531761336 | 243.1887660437081 | -0.03820720752959261 | 0.028581724683385892 | 0.007610135638298967 | 0.296593981741393 | 0.1017700033457872 | 0.5679769023298241 | 0.5679769023298241 | 0.03287639630668076 |
| Retail (Online) | 297 | 0.14430561728395058 | 0.050639662415794956 | 0.06686415514039022 | 0.13546589330930398 | 1.2321072795638826 | 1.282051089712587 | 0.09843075734423787 | 0.5187074756031715 | 0.045 | 0.10634727454780772 | 0.09151863569350752 | 1.587283682541945 | 3.578333219391361 | 23.725096910077898 | 63.810673173102856 | 7.512614037527899 | 82.73704712984416 | -0.004972920252591196 | 0.046700126250884766 | 0.005068906232141111 | 0.6625460649536722 | 0.16747876029961914 | 0.08959758902091389 | 0.08959758902091386 | 0.04780449647866815 |
| Retail (Special Lines) | 479 | 0.029680197740113008 | 0.05626341260666564 | 0.11989000735119668 | 0.2509046847983885 | 0.748552841735843 | 0.9567851805062828 | 0.07832932415528827 | 0.37507504044786244 | 0.040999999999999995 | 0.3253377415040795 | 0.06275660236050462 | 2.4591436938081537 | 1.1857438577780184 | 10.29764620728669 | 19.6956220410897 | 3.3461198794239664 | 28.581629029155028 | 0.07487012091632082 | 0.02198362309279438 | 0.003329513136469143 | 0.24333099408788406 | 0.14114030912142378 | 0.41430433051917875 | 0.4143043305191787 | 0.05987847830067084 |
| Rubber& Tires | 89 | 0.0063561194029850745 | 0.08569383227484277 | 0.08599125815957376 | 0.2561248202475349 | 0.7209670456185789 | 0.9364511019160889 | 0.0770726780984143 | 0.2862477093982976 | 0.040999999999999995 | 0.35424042552467483 | 0.0605616458952639 | 1.1678428156501655 | 1.043216446962713 | 6.634632745887462 | 11.795304350729205 | 1.2277445503629398 | 44.01719576692855 | 0.21234864710302026 | 0.058071429630415256 | 0.033782704527025954 | 0.6429207027771159 | 0.09745646591324209 | 0.4136245833677129 | 0.4136245833677129 | 0.08836048880540348 |
| Semiconductor | 542 | 0.043406957547169826 | 0.18187629290875904 | 0.1260648970443346 | 0.1451641929608596 | 1.5295820455595976 | 1.57034826289507 | 0.11624752264691532 | 0.3889493573214599 | 0.040999999999999995 | 0.10841279417245589 | 0.1069473828500129 | 0.7361435168660809 | 4.387620962914453 | 13.108867850310487 | 23.712066408904356 | 3.857020918526425 | 80.32097894335163 | 0.1700620827553624 | 0.17068958073516569 | 0.13986113180716034 | 0.9074994427557961 | 0.14547154357130868 | 0.48633449157894226 | 0.48633449157894226 | 0.18901706841910554 |
| Semiconductor Equip | 291 | 0.06262726829268292 | 0.1634106860111322 | 0.15099371054832447 | 0.16155488872985746 | 1.8210806223726346 | 1.839451129460635 | 0.13287807980066724 | 0.40995730198456787 | 0.045 | 0.09321671248402026 | 0.12360832282236296 | 1.0283405675450321 | 3.911260744783514 | 17.31417456392754 | 23.373141318046773 | 4.644987236333362 | 52.13270616115902 | 0.2904897861439973 | 0.06880117093464573 | 0.08228468273326425 | 0.6267239752190069 | 0.17323358260661803 | 0.3960216291599213 | 0.39602162915992123 | 0.170244977960772 |
| Shipbuilding & Marine | 345 | 0.03930311111111112 | 0.08089995760331258 | 0.04443013664865158 | 0.18467404184339148 | 0.7084029347843069 | 1.1297396255010554 | 0.08901790885596522 | 0.3389846278458122 | 0.040999999999999995 | 0.50259887512205 | 0.05958827753208293 | 0.6255452813585394 | 1.908054068503784 | 9.57596344443177 | 23.089808022646356 | 1.0590838998195835 | 25.969467892042044 | 0.013369342467696848 | 0.09407555978425022 | 0.04423451008717181 | 0.6754344460913858 | 0.05179674291659871 | 0.7631816320989928 | 0.7631816320989928 | 0.08154996927167069 |
| Shoe | 78 | -0.0037266666666666603 | 0.09743259183501832 | 0.1666051271003659 | 0.1793813245624553 | 0.8988600127419092 | 0.9539283957019175 | 0.07815277485437849 | 0.3437471419635265 | 0.040999999999999995 | 0.1159320539013652 | 0.07262400130541671 | 2.0124005403939473 | 2.667870191216001 | 18.835231994219235 | 26.782249690015323 | 5.989226816024242 | 27.965089370181143 | 0.1999630671828922 | 0.016877469846058098 | -0.0028218596857034588 | 0.04681424212802953 | 0.20801497698435187 | 0.3684182782665939 | 0.3684182782665939 | 0.09931630400796236 |
| Software (Entertainment) | 280 | 0.16813954954954952 | 0.22152733438817873 | 0.1632044764292634 | 0.1887383657517643 | 1.1764313768041483 | 1.1759313200409354 | 0.0918725555785298 | 0.5526188609554241 | 0.045 | 0.0476869807627836 | 0.08908584498983237 | 0.7595667060351502 | 6.855608951896273 | 21.15804946995614 | 30.97616362379615 | 5.33176455673168 | 90.61250752622789 | 0.03100059405168348 | 0.13486206462781464 | 0.08930381783109186 | 0.5793670687275562 | 0.18697195922189153 | 0.036247965449341515 | 0.0362479654493415 | 0.2383516440097337 |
| Software (Internet) | 131 | 0.2900737878787879 | 0.051277844728875914 | 0.0835007108303296 | 0.1569426017871457 | 1.2196848734436523 | 1.2944385564062693 | 0.09919630278590744 | 0.46674359296639434 | 0.045 | 0.1299869351436194 | 0.09064819258571577 | 1.461809963891432 | 5.037068593233759 | 19.627893573004663 | 53.9033860487918 | 8.029028470360421 | 62.065347734334885 | 0.035723168197722484 | 0.076812175635507 | 0.08206669183328832 | 2.456454570075412 | 0.0042824888935468096 | 5.803143759353975 | 5.803143759353975 | 0.06153472290970952 |
| Software (System & Application) | 1375 | 0.15156401685393273 | 0.19629064166420293 | 0.18191681674427446 | 0.14000164258253717 | 1.2452889901094526 | 1.2831242640847385 | 0.09849707952043683 | 0.504537549814611 | 0.045 | 0.08515673223863196 | 0.09295660543582641 | 0.9309100954491047 | 7.705237994379286 | 24.34655998293438 | 35.570596024469424 | 8.13277003583819 | 99.43629159468472 | 0.13720975600607932 | 0.05616536288382423 | 0.0827021788378448 | 0.5905118828251199 | 0.21168965087614794 | 0.32638991879574897 | 0.32638991879574897 | 0.21244027032201226 |
| Steel | 695 | 0.06407765384615384 | 0.07430408276185518 | 0.06443625342101163 | 0.19888850182977028 | 0.8225064191450808 | 1.1256603947387225 | 0.08876581239485304 | 0.370890992025568 | 0.040999999999999995 | 0.4141297697998501 | 0.0646208821190887 | 0.9865672386485591 | 0.7640304666682991 | 5.921980608746653 | 9.882412528955612 | 0.9015334281031374 | 47.72656760188993 | 0.13906021617318653 | 0.04934112957025643 | 0.02700179171947085 | 0.6220865680657679 | 0.05214540713781894 | 0.6095483637729363 | 0.6095483637729363 | 0.07539179277058176 |
| Telecom (Wireless) | 103 | 0.029157532467532467 | 0.13784183145869994 | 0.08456589383776851 | 0.2809778450687086 | 0.6093112277506092 | 0.9014014728143106 | 0.0749066110199244 | 0.33974261079606466 | 0.040999999999999995 | 0.43202911990747817 | 0.05570567686547616 | 0.6844711528315655 | 2.316880469042968 | 6.8064154892871835 | 15.957201155124588 | 1.5640367088775415 | 30.64234275468978 | -0.051883744553480576 | 0.125597277276007 | 0.006307734184949675 | 0.22934433405412136 | 0.06277205672114532 | 0.8999438484823243 | 0.8999438484823243 | 0.1436479999429968 |
| Telecom. Equipment | 474 | 0.05527755351681961 | 0.1075402091486058 | 0.11142995126152834 | 0.23913534322905447 | 1.2655330245200576 | 1.3191415628341474 | 0.10072294858315031 | 0.42660275234298123 | 0.045 | 0.14825911651420848 | 0.09074689677415897 | 1.1119310900535786 | 2.3701774171262455 | 14.179658491510805 | 20.88364889815574 | 3.6375476347734943 | 119.53687553542441 | 0.21134425082069544 | 0.03714131173876199 | 0.04319709880912463 | 0.6986601283682178 | 0.07690114754425859 | 0.8177494366552884 | 0.8177494366552884 | 0.11021431125517735 |
| Telecom. Services | 317 | 0.09876712195121952 | 0.15019014449663254 | 0.10623786129360184 | 0.2336256315576936 | 0.5867609941641149 | 0.8889998653185776 | 0.07414019167668809 | 0.39022571850768173 | 0.040999999999999995 | 0.43302255769699727 | 0.055226982423826614 | 0.811916366030058 | 2.3534719990026405 | 7.060908160552654 | 15.543384706497056 | 1.7350585960468268 | 92.73517010260679 | 0.015055436602075471 | 0.12945239018155277 | -0.03324755601803491 | -0.30530240917215573 | 0.07756116991482688 | 1.0079398260340624 | 1.0079398260340624 | 0.1509908869918967 |
| Tobacco | 54 | 0.025825945945945953 | 0.3197264984417853 | 0.1932211280841413 | 0.27132917495764514 | 0.8656273334860688 | 1.0379120997158167 | 0.08334296776243746 | 0.2952645817358551 | 0.040999999999999995 | 0.24468976398994705 | 0.07040378093085063 | 0.732388591701498 | 4.028812201315229 | 11.102369090883284 | 12.541540128045591 | 3.4963032267230565 | 18.325082486391867 | 0.19320407975465875 | 0.03541312755819003 | 0.02327332631423177 | 0.1969942866444816 | 0.20837838031254807 | 0.9466430856109735 | 0.9466430856109735 | 0.3211158432655085 |
| Transportation | 265 | 0.11458125000000002 | 0.06907406816079477 | 0.10190940887978868 | 0.23197501883469585 | 0.7940858113757814 | 1.0876685300485347 | 0.08641791515699944 | 0.32744211394315736 | 0.040999999999999995 | 0.3895039010951231 | 0.06462325741790152 | 1.7767152393090468 | 1.304862901073636 | 10.46762157330528 | 18.459982848266705 | 1.8563730182897182 | 85.83340167762594 | 0.030977580576123147 | 0.052178692515681364 | 0.041030965791588214 | 0.9800468322082901 | 0.12400914875672217 | 0.607651397209029 | 0.607651397209029 | 0.07051849058010347 |
| Transportation (Railroads) | 52 | 0.07036511627906976 | 0.23181237931035845 | 0.09483851349711833 | 0.2488039189456572 | 0.8272689994346133 | 1.0441121159152091 | 0.08372612876355992 | 0.19145465803549994 | 0.0355 | 0.282282923340747 | 0.06753730790367564 | 0.520776127171807 | 3.710754437656867 | 10.91335560229394 | 15.821866749016179 | 2.478123211167372 | 24.17838006148093 | 0.1002426203533136 | 0.17065120187116398 | 0.11875510638389936 | 0.7183144141858554 | 0.15299034465361688 | 0.285747814557666 | 0.28574781455766596 | 0.23458508945828258 |
| Trucking | 208 | 0.06086605263157895 | 0.01890581297560357 | 0.04261842864519406 | 0.26864041811728145 | 0.6540174358423104 | 0.9413278111374566 | 0.07737405872829481 | 0.32563675681766896 | 0.040999999999999995 | 0.42740494417367786 | 0.05732404029139984 | 1.197206345153875 | 1.4673176364466112 | 8.844169223519375 | 46.03614074470831 | 1.9990651194023896 | 21.05308896631561 | 0.08028333995599489 | 0.10601418757672627 | 0.08377038731810268 | 14.602381293277528 | -0.03889648586467887 | 0.0033624174974592204 | 0.003362417497459247 | 0.04095205556654147 |
| Utility (General) | 52 | 0.01719816326530612 | 0.09476367570429613 | 0.05870449551521407 | 0.18512744182950677 | 0.4140902432736007 | 0.6544081596819752 | 0.05964242426834607 | 0.2012628625899196 | 0.0355 | 0.460421552298167 | 0.04432607577808091 | 0.7621732927588523 | 2.277348496098419 | 12.583122081418617 | 24.103653316433622 | 1.71822357180121 | 419.587195202067 | -0.018934940114175066 | 0.13084440814504567 | 0.09130080732920821 | 1.1766118784543311 | 0.12235563989080055 | 0.5893450720871619 | 0.5893450720871619 | 0.09445387281223759 |
| Utility (Water) | 99 | 0.11742507042253518 | 0.2803010488634021 | 0.0766819746735097 | 0.23313559748284818 | 0.6932375070101038 | 0.9487372092204914 | 0.07783195952982637 | 0.26753958736892625 | 0.040999999999999995 | 0.3806300066120747 | 0.05980191215078146 | 0.33506870152733104 | 4.980897552759019 | 12.470501405024097 | 17.82691355637673 | 1.8607104377364327 | 30.35238295385851 | 0.02509196234379651 | 0.25788681671946634 | 0.1760347889451142 | 1.177599749568401 | 0.10686793981989083 | 0.623891068582905 | 0.4853444956844384 | 0.27798498043394454 |
| Total Market | 44394 | 0.08378872121063807 | 0.09282239733856404 | 0.06146184491361945 | 0.22437492147765753 | 0.7943600161914623 | 1.0770240808772962 | 0.0857600881982169 | 0.3921961404993382 | 0.040999999999999995 | 0.4149176337569176 | 0.06281635120936517 | 0.752071691603797 | 2.2831743272090628 | 14.080259448228322 | 23.080331977115605 | 1.9010573233512178 | 65.24422428128095 | -1.1743124969509713 | 0.058716791740073784 | 0.03966794214177256 | 0.6912962348187386 | 0.10686793981989083 | 0.48534449568443844 | 0.4853444956844384 | 0.09415445823482713 |
| Total Market (without financials) | 39677 | 0.08044297689403777 | 0.09783887772629433 | 0.09779475676812337 | 0.2358120603451241 | 0.9155482793342168 | 1.1123314545476997 | 0.08794208389104784 | 0.40305931103252063 | 0.045 | 0.2848642889180314 | 0.072414962197429 | 1.1313438759338263 | 1.889207924411506 | 11.186529601930104 | 18.662684597675376 | 2.261506936776664 | 66.0653066160258 | 0.10920996537161921 | 0.06324178758123294 | 0.040995832280716904 | 0.6936200572238138 | 0.1040967822270143 | 0.5472340835895629 | 0.5472340835895629 | 0.09937447531099419 |

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
