---
title: "Disneytaxreform"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/blog/DisneyTaxReform.xlsx
---

# Disneytaxreform

Source: https://www.stern.nyu.edu/~adamodar/pc/blog/DisneyTaxReform.xlsx

Sheets: READ ME 1ST, FAQs, Inputs, Marginal tax rate by country, Operating leases, Default Spreads and Ratios, Optimal Capital Structure, Repurchase price Worksheet, Summary Table, Input choices page

## READ ME 1ST

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
| Details |
| References |
| Corporate Finance: Theory and Practice, Chapter 18 |
| Applied Corporate Finance: Chapter 8 |

## FAQs

| Question | Answer |
|---|---|
| Q1: What do I do excel says there are circular references? | Go into preferences, choose calculation options and make sure the iteration box has a check in it. |
| Q2: My spreadsheet has gone crazy. I get errors all over. What did I do wrong? | I am sorry to say this, but you probably just made an input error. While you might have fixed it, the iterations in the spreadsheet make it very sensitive and the errors will not go away. The only fix (Sorry, sorry…) is to copy the inputs into a fresh version of the spreadsheet. |
| Q3: I am entering the inputs for my company but the optimal numbers do not seem to change from the originals. | You probably forgot to check the iteration box (see Q1) |
| Q4: I am getting an optimal debt ratio of 0%. This can't be right. Can it? | Sure. If your operating income is either negative or very low, relative to your firm value, |
|  | you can end up at an optimal debt ratio of 0%. For instance, if you have EBIT of 100 on a |
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
| Q6: I am getting an optimal debt ratio at a mix where my cost  | Not necessarily. If you chose to build in indirect bankruptcy costs (an option on the input page), |
| of capital is not minimized? Is something wrong? | your operating income also changes as your debt ratio changes. Since the objective ultimately is to  |
|  | maximize firm value, it is possible that the net effect (lower cost of capital is good but it could be offset |
|  | by lower operating income) is resulting in an optimal at a higher debt ratio. |

## Inputs

| In December 2017, Congress passed a major tax reform that not only lowered the tax rate for US companies but alao imposed limits on interst tax deductions for tax purposes. Starting in 2018, interest will be deductible, for tax purposes, only if it is less than 30% of taxable income. However, Congress in its wisdom has defined EBITDA as taxable income until 2022 and EBIT thereafter. I have added an option to the spreadsheet to allow you to incorporate this limit.  If you are working with a company outside the US, just set the option to constrain interest expenses to no and you should be ready to go. |
|---|
| Inputs |
| Please enter the name of the company you are analyzing: |
| Please enter the date that you are doing this analysis |
| Financial Information |
| Earnings before interest expenses, depreciation & amortization (EBITDA) |
| Depreciation and Amortization: |
| Capital Spending: |
| Interest expense on debt: |
| Marginal tax rate to use for pre-tax cost of debt |
| Current Bond Rating on debt (if available): |
| Enter the current pre-tax cost of debt for your company |
| Market Information & information on debt |
| Number of shares outstanding: |
| Market price per share: |
| Unlevered Beta |
| Beta of the stock: |
| Cash and marketable securities = |
| Book value of debt: |
| Can you estimate the market value of the interest bearing debt? |
| If so, enter the market value of "interest bearing" debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the weighted average maturity of outstanding debt? |
| Do you have any operating leases? |
| Interest deduction constraints |
| Are there any restrictions on interest deductions for tax purposes? |
| If yes, what earnings or operating measure is the restriction tied to? |
| Enter the maximum percentage of that measure that is deductible |
| Indirect bankruptcy costs & ratings constraints (if any) |
| Do you want to incorporate indirect bankruptcy costs into your optimal? |
| If yes, specify the magnitude of your indirect bankruptcy costs |
| General Market Data |
| Current riskfree rate in the currency of analysis = |
| Risk premium (for use in the CAPM) |
| Country Default spread (for cost of debt) |
| General Data |
| Which spread/ratio table would you like to use for your anlaysis? |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |
| Do you want the firm's current rating & cost of debt to be adjusted to the synthetic rating? |

## Marginal tax rate by country

| Country | 2017 |
|---|---|
| Afghanistan | 0.2 |
| Albania | 0.15 |
| Algeria | 0.26 |
| Andorra | 0.1 |
| Angola | 0.3 |
| Anguilla | 0 |
| Antigua and Barbuda | 0.25 |
| Argentina | 0.35 |
| Armenia | 0.2 |
| Aruba | 0.25 |
| Australia | 0.3 |
| Austria | 0.25 |
| Azerbaijan | 0.2 |
| Bahamas | 0 |
| Bahrain | 0 |
| Bangladesh | 0.25 |
| Barbados | 0.25 |
| Belarus | 0.18 |
| Belgium | 0.33990000000000004 |
| Benin | 0.3 |
| Bermuda | 0 |
| Bolivia | 0.25 |
| Bonaire, Saint Eustatius and Saba | 0.25 |
| Bosnia and Herzegovina | 0.1 |
| Botswana | 0.22 |
| Brazil | 0.34 |
| Brunei Darussalam | 0.185 |
| Bulgaria | 0.1 |
| Burkina Faso | 0.275 |
| Burundi | 0.3 |
| Cambodia | 0.2 |
| Cameroon | 0.33 |
| Canada | 0.265 |
| Cayman Islands | 0 |
| Chile | 0.255 |
| China | 0.25 |
| Colombia | 0.34 |
| Congo (Democratic Republic of the) | 0.35 |
| Costa Rica | 0.3 |
| Croatia | 0.2 |
| Curacao | 0.22 |
| Cyprus | 0.125 |
| Czech Republic | 0.19 |
| Denmark | 0.22 |
| Djibouti | 0.25 |
| Dominica | 0.25 |
| Dominican Republic | 0.27 |
| Ecuador | 0.22 |
| Egypt | 0.225 |
| El Salvador | 0.3 |
| Estonia | 0.2 |
| Ethiopia | 0.3 |
| Fiji | 0.2 |
| Finland | 0.2 |
| France | 0.3333 |
| Gabon | 0.3 |
| Gambia | 0.31 |
| Georgia | 0.15 |
| Germany | 0.2979 |
| Ghana | 0.25 |
| Gibraltar | 0.1 |
| Greece | 0.29 |
| Grenada | 0.3 |
| Guatemala | 0.25 |
| Guernsey | 0 |
| Honduras | 0.25 |
| Hong Kong SAR | 0.165 |
| Hungary | 0.09 |
| Iceland | 0.2 |
| India | 0.3 |
| Indonesia | 0.25 |
| Iraq | 0.15 |
| Ireland | 0.125 |
| Isle of Man | 0 |
| Israel | 0.24 |
| Italy | 0.24 |
| Ivory Coast | 0.25 |
| Jamaica | 0.25 |
| Japan | 0.3086 |
| Jersey | 0.2 |
| Jordan | 0.2 |
| Kazakhstan | 0.2 |
| Kenya | 0.3 |
| Korea, Republic of | 0.22 |
| Kuwait | 0.15 |
| Kyrgyzstan | 0.1 |
| Latvia | 0.15 |
| Lebanon | 0.15 |
| Libya | 0.2 |
| Liechtenstein | 0.125 |
| Lithuania | 0.15 |
| Luxembourg | 0.2708 |
| Macau | 0.12 |
| Macedonia | 0.1 |
| Madagascar | 0.2 |
| Malawi | 0.3 |
| Malaysia | 0.24 |
| Malta | 0.35 |
| Mauritius | 0.15 |
| Mexico | 0.3 |
| Moldova | 0.12 |
| Monaco | 0.3333 |
| Mongolia | 0.25 |
| Montenegro | 0.09 |
| Morocco | 0.31 |
| Mozambique | 0.32 |
| Myanmar | 0.25 |
| Namibia | 0.32 |
| Netherlands | 0.25 |
| New Zealand | 0.28 |
| Nicaragua | 0.3 |
| Nigeria | 0.3 |
| Norway | 0.24 |
| Oman | 0.15 |
| Pakistan | 0.31 |
| Palestinian Territory | 0.15 |
| Panama | 0.25 |
| Papua New Guinea | 0.3 |
| Paraguay | 0.1 |
| Peru | 0.295 |
| Philippines | 0.3 |
| Poland | 0.19 |
| Portugal | 0.21 |
| Qatar | 0.1 |
| Romania | 0.16 |
| Russia | 0.2 |
| Rwanda | 0.3 |
| Saint Kitts and Nevis | 0.33 |
| Saint Lucia | 0.3 |
| Saint Vincent and the Grenadines | 0.325 |
| Samoa | 0.27 |
| Saudi Arabia | 0.2 |
| Senegal | 0.3 |
| Serbia | 0.15 |
| Sierra Leone | 0.3 |
| Singapore | 0.17 |
| Sint Maarten (Dutch part) | 0.345 |
| Slovakia | 0.21 |
| Slovenia | 0.19 |
| Solomon Islands | 0.3 |
| South Africa | 0.28 |
| Spain | 0.25 |
| Sri Lanka | 0.28 |
| St Maarten | 0.345 |
| Sudan | 0.35 |
| Suriname | 0.36 |
| Swaziland | 0.275 |
| Sweden | 0.22 |
| Switzerland | 0.1777 |
| Syria | 0.28 |
| Taiwan | 0.17 |
| Tanzania | 0.3 |
| Thailand | 0.2 |
| Trinidad and Tobago | 0.25 |
| Tunisia | 0.25 |
| Turkey | 0.2 |
| Turkmenistan | 0.2 |
| Turks and Caicos Islands | 0 |
| Uganda | 0.3 |
| Ukraine | 0.18 |
| United Arab Emirates | 0.55 |
| United Kingdom | 0.19 |
| United States | 0.24 |
| Uruguay | 0.25 |
| Uzbekistan | 0.075 |
| Vanuatu | 0 |
| Venezuela | 0.34 |
| Vietnam | 0.2 |
| Yemen | 0.2 |
| Zambia | 0.35 |
| Zimbabwe | 0.25 |
| Africa average | 0.2821 |
| Americas average | 0.2566 |
| Asia average | 0.21280000000000002 |
| EU average | 0.2151 |
| Europe average | 0.1954 |
| Global average | 0.2425 |
| Latin America average | 0.2798 |
| North America average | 0.2375 |
| Oceania average | 0.2867 |
| OECD average | 0.2407 |
| South America average | 0.2798 |

## Operating leases

| Operating Lease Converter |
|---|
| Operating lease expenses are really financial expenses, and should be treated as such. Accounting standards allow them to |
| be treated as operating expenses. This program will convert commitments to make operating leases into debt and |
| adjust the operating income accordingly, by adding back the imputed interest expense on this debt. |
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
| Pre-tax Cost of Debt = |
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
| Restated Financials |
| Operating Income with Operating leases reclassified as debt = |
| Interest expenses with Operating leases classified as debt = |
| Depreciation with operating leases classified as debt = |

## Default Spreads and Ratios

| Inputs for synthetic rating estimation |
|---|
| Enter the type of firm = |
| Earnings before interest and taxes (EBIT) = |
| Current interest expenses = |
| Current long term government bond rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
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

## Optimal Capital Structure

| Disney |
|---|
| 2018-01-01 00:00:00 |
| Capital Structure |
| Current MV of Equity = |
| Market Value of interest-bearing debt = |
| # of Shares Outstanding = |
| Debt Value of Operating leases = |
| Equity Risk Premium = |
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
| Assumes perpeutal growth |
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
| Enterprise value = |
|  |
| D/(D+E) |
| D/E |
| $ Debt |
| Beta |
| Cost of Equity |
| % Drop in EBITDA |
| EBITDA |
| Depreciation |
| EBIT |
| Interest |
| Taxable Income |
| Tax |
| Net Income |
| (+)Deprec'n |
| Funds from Op. |
| Pre-tax Int. cov |
| Funds/Debt |
| Likely Rating |
| Pre-tax cost of debt |
| Tax rate for debt (deduction constraint) |
| Tax rate for debt tax benefits (Interest limits) |
| Tax rate to use in after-tax cost of debt |
|  |
| D/(D+E) |
| D/E |
| $ Debt |
| Cost of equity |
| Cost of debt |
| Cost of Capital |
|  |
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

## Repurchase price Worksheet

| Stock price buyback effect |
|---|
| Current Stock price = |
| # Shares outstanding before buyback = |
| Expected buyback price = |
| Current Debt = |
| Debt at Optimal = |
| New Debt issued = |
| # Shares bought back = |
| Shares outstanding after buyback = |
| Enterprise value after buyback = |
|  + Cash |
|  - Debt |
| Equity value after buyback  |
| / Number of shares after buyback |
| Value per share for remaining shares |

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Enterprise Value |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.92 | 0.072236 | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 | 0.072236 | 184639.60459558028 |
| 0.1 | 0.9976888888888891 | 0.07618259555555557 | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 | 0.07091273600000002 | 188955.77927601401 |
| 0.2 | 1.0948 | 0.08111584 | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 | 0.069589472 | 193478.57562375738 |
| 0.3 | 1.2196571428571428 | 0.08745858285714285 | Aa2/AA | 0.03269999999999999 | 0.24 | 0.024851999999999996 | 0.06867660799999999 | 196726.98208695522 |
| 0.4 | 1.3861333333333334 | 0.09591557333333334 | A2/A | 0.035399999999999994 | 0.24 | 0.026903999999999997 | 0.068310944 | 198058.99421453226 |
| 0.5 | 1.6192 | 0.10775536 | A3/A- | 0.03674999999999999 | 0.24 | 0.027929999999999993 | 0.06784267999999999 | 199791.31943919227 |
| 0.6 | 1.9687999999999999 | 0.12551504 | A3/A- | 0.03674999999999999 | 0.24 | 0.027929999999999993 | 0.06696401599999999 | 203125.04930875302 |
| 0.7 | 2.7340334250392666 | 0.16438889799199474 | C2/C | 0.16501875 | 0.15495337342891324 | 0.1394485380084775 | 0.14693064600353267 | 80650.39178957461 |
| 0.8 | 4.1010501375589 | 0.2338333469879921 | C2/C | 0.16501875 | 0.13558420175029912 | 0.14264481450741784 | 0.16088252100353267 | 72973.71927534499 |
| 0.9 | 8.2021002751178 | 0.44216669397598424 | C2/C | 0.16501875 | 0.12051929044471033 | 0.14513080733992695 | 0.17483439600353268 | 66631.43506792089 |
| Debt Ratio | $ Debt | Interest Expense | Interest Coverage Ratio | Bond Rating | Pre-tax cost of debt | Tax rate | After-tax cost of debt |  |
| 0 | 0 | 0 | ∞ | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 |  |
| 0.1 | 19439.93474935094 | 600.693983754944 | 24.13585274280709 | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 |  |
| 0.2 | 38879.86949870188 | 1201.387967509888 | 12.067926371403543 | Aaa/AAA | 0.030899999999999997 | 0.24 | 0.023483999999999998 |  |
| 0.3 | 58319.804248052824 | 1907.057598911327 | 7.602424564248104 | Aa2/AA | 0.03269999999999999 | 0.24 | 0.024851999999999996 |  |
| 0.4 | 77759.73899740377 | 2752.6947605080927 | 5.2669339671803606 | A2/A | 0.035399999999999994 | 0.24 | 0.026903999999999997 |  |
| 0.5 | 97199.6737467547 | 3572.0880101932344 | 4.058763808178172 | A3/A- | 0.03674999999999999 | 0.24 | 0.027929999999999993 |  |
| 0.6 | 116639.60849610565 | 4286.505612231881 | 3.3823031734818105 | A3/A- | 0.03674999999999999 | 0.24 | 0.027929999999999993 |  |
| 0.7 | 136079.5432454566 | 22455.67612693619 | 0.6456390559538052 | C2/C | 0.16501875 | 0.15495337342891324 | 0.1394485380084775 |  |
| 0.8 | 155519.47799480753 | 25663.629859355642 | 0.5649341739595797 | C2/C | 0.16501875 | 0.13558420175029912 | 0.14264481450741784 |  |
| 0.9 | 174959.41274415847 | 28871.5835917751 | 0.502163710186293 | C2/C | 0.16501875 | 0.12051929044471033 | 0.14513080733992695 |  |

## Input choices page

| Rating is | Yes/No | IBC | Type of firm | Earnings/Operating Measure |
|---|---|---|---|---|
| Aaa/AAA | Yes | High | 1 |  |
| Aa2/AA | No | Medium | 2 | EBITDA |
| A1/A+ |  | Low |  | EBIT |
| A2/A |  |  |  |  |
| A3/A- |  |  |  |  |
| Baa2/BBB |  |  |  |  |
| Ba1/BB+ |  |  |  |  |
| Ba2/BB |  |  |  |  |
| B1/B+ |  |  |  |  |
| B2/B |  |  |  |  |
| B3/B- |  |  |  |  |
| Caa/CCC |  |  |  |  |
| Ca2/CC |  |  |  |  |
| C2/C |  |  |  |  |
| D2/D |  |  |  |  |
| Not rated |  |  |  |  |
| Rating is |  |  |  |  |
| D2/D |  |  |  |  |
| Caa/CCC |  |  |  |  |
| Ca2/CC |  |  |  |  |
| C2/C |  |  |  |  |
| B3/B- |  |  |  |  |
| B2/B |  |  |  |  |
| B1/B+ |  |  |  |  |
| Ba2/BB |  |  |  |  |
| Ba1/BB+ |  |  |  |  |
| Baa2/BBB |  |  |  |  |
| A3/A- |  |  |  |  |
| A2/A |  |  |  |  |
| A1/A+ |  |  |  |  |
| Aa2/AA |  |  |  |  |
| Aaa/AAA |  |  |  |  |
