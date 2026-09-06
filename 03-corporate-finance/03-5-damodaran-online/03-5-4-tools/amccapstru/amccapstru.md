---
title: "Amccapstru"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/blog/AMCcapstru.xlsx
---

# Amccapstru

Source: https://pages.stern.nyu.edu/~adamodar/pc/blog/AMCcapstru.xlsx

Sheets: READ ME 1ST, FAQs, Inputs, Optimal CS Worksheet, Marginal tax rate by country, Operating leases, Default Spreads and Ratios, ERP Calculator, Country ERP , Repurchase price Worksheet, Summary Table, Input choices page

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

| In December 2017, Congress passed a major tax reform that not only lowered the tax rate for US companies but alao imposed limits on interst tax deductions for tax purposes. Starting in 2018, interest will be deductible, for tax purposes, only if it is less than 30% of taxable income. However, Congress in its wisdom has defined EBITDA as taxable income until 2022 and EBIT thereafter. I have added an option to the spreadsheet to allow you to incorporate this limit.  If you are working with a company outside the US, just set the option to constrain interest expenses to no and you should be ready to go. | Input Cell |
|---|---|
|  | Calculated/Output Cell |
| Important: This spreadsheet includes circular references, by design. Please go into calculation options and check the iteration box. |  |
| Inputs |  |
| Please enter the name of the company you are analyzing: |  |
| Country of incorporatiion |  |
| Please enter the date that you are doing this analysis |  |
| Financial Information |  |
| Earnings before interest expenses, depreciation & amortization (EBITDA) |  |
| Depreciation and Amortization: |  |
| Capital Spending: |  |
| Interest expense on debt: |  |
| Marginal tax rate to use for pre-tax cost of debt |  |
| Current Bond Rating on debt (if available): |  |
| Enter the current pre-tax cost of debt for your company |  |
| Market Information & information on debt |  |
| Number of shares outstanding: |  |
| Market price per share: |  |
| Beta of the stock: |  |
| Cash and marketable securities = |  |
| Book value of debt: |  |
| Can you estimate the market value of the interest bearing debt? |  |
| If so, enter the market value of "interest bearing" debt: |  |
| Do you want me to try and estimate market value of debt? |  |
| If yes, enter the weighted average maturity of outstanding debt? |  |
| Do you have any operating leases? |  |
| Interest deduction constraints |  |
| Are there any restrictions on interest deductions for tax purposes? |  |
| If yes, what earnings or operating measure is the restriction tied to? |  |
| Enter the maximum percentage of that measure that is deductible |  |
| Indirect bankruptcy costs & ratings constraints (if any) |  |
| Do you want to incorporate indirect bankruptcy costs into your optimal? |  |
| If yes, specify the magnitude of your indirect bankruptcy costs |  |
| General Market Data |  |
| Current riskfree rate in the currency of analysis = |  |
| Risk premium (for use in the CAPM) |  |
| Country Default spread (for cost of debt) |  |
| General Data |  |
| Which spread/ratio table would you like to use for your anlaysis? |  |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |  |
| Do you want the firm's current rating & cost of debt to be adjusted to the synthetic rating? |  |

## Optimal CS Worksheet

| AMC |
|---|
| 2024-04-01 00:00:00 |
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
| D/(D+E) |
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

## Marginal tax rate by country

| Country | 2023 |
|---|---|
| Abu Dhabi | 0.15 |
| Albania | 0.15 |
| Algeria | 0.26 |
| Andorra (Principality of) | 0.1898 |
| Angola | 0.25 |
| Anguilla | 0.2724561140242252 |
| Antigua & Barbuda | 0.2724561140242252 |
| Argentina | 0.35 |
| Armenia | 0.18 |
| Aruba | 0.25 |
| Australia | 0.3 |
| Austria | 0.24 |
| Azerbaijan | 0.2 |
| Bahamas | 0 |
| Bahrain | 0 |
| Bangladesh | 0.3 |
| Barbados | 0.055 |
| Belarus | 0.18 |
| Belgium | 0.25 |
| Belize | 0.2853 |
| Benin | 0.3 |
| Bermuda | 0 |
| Bolivia | 0.25 |
| Bosnia and Herzegovina | 0.1 |
| Botswana | 0.22 |
| Brazil | 0.34 |
| British Virgin Islands | 0.34 |
| Brunei | 0.185 |
| Bulgaria | 0.1 |
| Burkina Faso | 0.28 |
| Cambodia | 0.2 |
| Cameroon | 0.33 |
| Canada | 0.265 |
| Cape Verde | 0 |
| Cayman Islands | 0 |
| Channel Islands | 0.24707349543413576 |
| Chile | 0.27 |
| China | 0.25 |
| Colombia | 0.35 |
| Congo (Democratic Republic of) | 0.3 |
| Congo (Republic of) | 0.28 |
| Cook Islands | 0.2974 |
| Costa Rica | 0.3 |
| Croatia | 0.18 |
| Cuba | 0.2853 |
| Curaçao | 0.22 |
| Cyprus | 0.125 |
| Czech Republic | 0.19 |
| Denmark | 0.22 |
| Dominican Republic | 0.27 |
| Ecuador | 0.25 |
| Egypt | 0.225 |
| El Salvador | 0.3 |
| Estonia | 0.2 |
| Ethiopia | 0.3 |
| Falkland Islands | 0.31595749426030023 |
| Fiji | 0.2 |
| Finland | 0.2 |
| France | 0.25 |
| French Guiana | 0.31595749426030023 |
| Gabon | 0.3 |
| Gambia | 0.31 |
| Georgia | 0.15 |
| Germany | 0.3 |
| Ghana | 0.25 |
| Gibraltar | 0.24707349543413576 |
| Greece | 0.22 |
| Greenland | 0 |
| Guatemala | 0.25 |
| Guernsey (States of) | 0 |
| Guinea | 0.2915 |
| Guinea-Bissau | 0.2915 |
| Guyana | 0.1864 |
| Haiti | 0.1864 |
| Honduras | 0.25 |
| Hong Kong | 0.165 |
| Hungary | 0.09 |
| Iceland | 0.2 |
| India | 0.3 |
| Indonesia | 0.22 |
| Iran | 0.2023 |
| Iraq | 0.15 |
| Ireland | 0.125 |
| Isle of Man | 0 |
| Israel | 0.23 |
| Italy | 0.24 |
| Ivory Coast | 0.25 |
| Jamaica | 0.25 |
| Japan | 0.3062 |
| Jersey (States of) | 0 |
| Jordan | 0.2 |
| Kazakhstan | 0.2 |
| Kenya | 0.3 |
| Korea, D.P.R. | 0.231 |
| Kuwait | 0.15 |
| Kyrgyzstan | 0.1 |
| Laos | 0.2686 |
| Latvia | 0.2 |
| Lebanon | 0.17 |
| Liberia | 0.2915 |
| Libya | 0.2 |
| Liechtenstein | 0.125 |
| Lithuania | 0.15 |
| Luxembourg | 0.2494 |
| Macau | 0.2686 |
| Macedonia | 0.1 |
| Madagascar | 0.2 |
| Malawi | 0.3 |
| Malaysia | 0.24 |
| Maldives | 0.2686 |
| Mali | 0.2686 |
| Malta | 0.35 |
| Martinique | 0 |
| Mauritius | 0.15 |
| Mexico | 0.3 |
| Monaco | 0.24707349543413576 |
| Moldova | 0.12 |
| Mongolia | 0.25 |
| Montenegro | 0.15 |
| Montserrat | 0.2853 |
| Morocco | 0.32 |
| Mozambique | 0.32 |
| Myanmar | 0.25 |
| Namibia | 0.32 |
| Netherlands | 0.258 |
| Netherlands Antilles | 0.2724561140242252 |
| New Zealand | 0.28 |
| Nicaragua | 0.3 |
| Niger | 0.2686 |
| Nigeria | 0.3 |
| Norway | 0.22 |
| Oman | 0.15 |
| Pakistan | 0.29 |
| Palestinian Authority | 0.18760152153615242 |
| Panama | 0.25 |
| Papua New Guinea | 0.3 |
| Paraguay | 0.1 |
| Peru | 0.295 |
| Philippines | 0.25 |
| Poland | 0.19 |
| Portugal | 0.21 |
| Qatar | 0.1 |
| Ras Al Khaimah (Emirate of) | 0 |
| Reunion | 0.2576437502455447 |
| Romania | 0.16 |
| Russia | 0.25 |
| Rwanda | 0.3 |
| Saint Lucia | 0.2724561140242252 |
| Saudi Arabia | 0.2 |
| Senegal | 0.3 |
| Serbia | 0.15 |
| Sharjah | 0 |
| Sierra Leone | 0.3 |
| Singapore | 0.17 |
| Slovakia | 0.21 |
| Slovenia | 0.19 |
| Solomon Islands | 0.3 |
| Somalia | 0.2915 |
| South Africa | 0.27 |
| South Korea | 0.25 |
| Spain | 0.25 |
| Sri Lanka | 0.24 |
| St. Maarten | 0.2853 |
| St. Vincent & the Grenadines | 0.2853 |
| Sudan | 0.35 |
| Suriname | 0.36 |
| Swaziland | 0.275 |
| Sweden | 0.20600000000000002 |
| Switzerland | 0.146 |
| Syria | 0.28 |
| Taiwan | 0.2 |
| Tajikistan | 0.18 |
| Tanzania | 0.3 |
| Thailand | 0.2 |
| Togo | 0.2686 |
| Trinidad &' Tobago | 0.3 |
| Tunisia | 0.15 |
| Turkey | 0.25 |
| Turks & Caicos Islands | 0 |
| Uganda | 0.3 |
| Ukraine | 0.18 |
| United Arab Emirates | 0.25 |
| United Kingdom | 0.25 |
| United States | 0.25 |
| Uruguay | 0.25 |
| Uzbekistan | 0.15 |
| Venezuela | 0.34 |
| Vietnam | 0.2 |
| Yemen | 0.2 |
| Zambia | 0.35 |
| Zimbabwe | 0.25 |

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
| Current riskfree rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
| For large non-financial service firms |
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
| For smaller and riskier non-financial service firms |
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
| For infrastructure companies/Utilities |
| greater than |
| -100000 |
| 0.2 |
| 0.5 |
| 0.75 |
| 1 |
| 1.2 |
| 1.4 |
| 1.6 |
| 1.8 |
| 2 |
| 2.25 |
| 3 |
| 3.5 |
| 4 |
| 4.5 |

## ERP Calculator

| If you are a multinational company and have a breakdown by country, you can use this table (for up to 10 countries) |
|---|
| Country |
| China |
| India |
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
| Total |
| If you are a multinational company and have a breakdown only by region, you can use this table instead |
| Region |
| Africa |
| Asia |
| Australia & New Zealand |
| Caribbean |
| Central and South America |
| Eastern Europe & Russia |
| Middle East |
| North America |
| Western Europe |
|  |
|  |
| Total |

## Country ERP 

_204 rows — showing first 20. Full data: [`amccapstru-country-erp.csv`](amccapstru-country-erp.csv)_

| Mature Market ERP + | 0.046 | Updated January 1, 2024 |
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

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | Cost of Capital | Enterprise Value |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.04995985917007311 | 0.047123294014728104 | Aaa/AAA | 0.0509 | 0.25 | 0.038175 | 0.047123294014728104 | 14765.30916491979 |
| 0.1 | 0.0541231807675792 | 0.047300235182622115 | Aaa/AAA | 0.0509 | 0.25 | 0.038175 | 0.046387711664359906 | 14948.3109391343 |
| 0.2 | 0.05932733276446182 | 0.047521411642489624 | Aaa/AAA | 0.0509 | 0.25 | 0.038175 | 0.04565212931399171 | 15135.905902680013 |
| 0.3 | 0.06601838533188233 | 0.047805781376604996 | Aa2/AA | 0.052 | 0.25 | 0.039 | 0.0451640469636235 | 15263.00158704872 |
| 0.4 | 0.07493978875510966 | 0.048184941022092156 | A1/A+ | 0.0542 | 0.25 | 0.04065 | 0.04517096461325529 | 15261.185335030186 |
| 0.5 | 0.08742975354762794 | 0.04871576452577418 | A2/A | 0.0557 | 0.25 | 0.041775 | 0.04524538226288709 | 15241.674034541371 |
| 0.6 | 0.10616470073640535 | 0.04951199978129722 | A2/A | 0.0557 | 0.25 | 0.041775 | 0.044869799912518896 | 15340.659449025014 |
| 0.7 | 0.13738961271770106 | 0.050839058540502295 | A3/A- | 0.0571 | 0.25 | 0.042825 | 0.04522921756215069 | 15245.907957622423 |
| 0.8 | 0.1998394366802925 | 0.053493176058912434 | A3/A- | 0.0571 | 0.25 | 0.042825 | 0.04495863521178249 | 15317.130834594693 |
| 0.9 | 0.3871889085680667 | 0.061455528614142836 | Baa2/BBB | 0.059699999999999996 | 0.25 | 0.044774999999999995 | 0.046443052861414286 | 14934.385228914152 |
| Debt Ratio | $ Debt | Interest Expense | Interest Coverage Ratio | Bond Rating | Pre-tax cost of debt | Tax rate | After-tax cost of debt |  |
| 0 | 0 | 0 | ∞ | Aaa/AAA | 0.0509 | 0.25 | 0.038175 |  |
| 0.1 | 1113.1094742149871 | 45.45217312671787 | 36.7086158307923 | Aaa/AAA | 0.0509 | 0.25 | 0.038175 |  |
| 0.2 | 2226.2189484299743 | 90.90434625343573 | 18.35430791539615 | Aaa/AAA | 0.0509 | 0.25 | 0.038175 |  |
| 0.3 | 3339.3284226449614 | 136.3565193801536 | 12.236205276930765 | Aa2/AA | 0.052 | 0.25 | 0.039 |  |
| 0.4 | 4452.4378968599485 | 181.80869250687147 | 9.177153957698074 | A1/A+ | 0.0542 | 0.25 | 0.04065 |  |
| 0.5 | 5565.547371074936 | 227.26086563358933 | 7.34172316615846 | A2/A | 0.0557 | 0.25 | 0.041775 |  |
| 0.6 | 6678.656845289923 | 272.7130387603072 | 6.118102638465383 | A2/A | 0.0557 | 0.25 | 0.041775 |  |
| 0.7 | 7791.766319504909 | 318.165211887025 | 5.2440879758274725 | A3/A- | 0.0571 | 0.25 | 0.042825 |  |
| 0.8 | 8904.875793719897 | 363.61738501374293 | 4.588576978849037 | A3/A- | 0.0571 | 0.25 | 0.042825 |  |
| 0.9 | 10017.985267934884 | 409.0695581404608 | 4.078735092310255 | Baa2/BBB | 0.059699999999999996 | 0.25 | 0.044774999999999995 |  |
| Debt Ratio | Cost of Capital | Enterprise Value |  |  |  |  |  |  |
| 0 | 0.047123294014728104 | 14765.30916491979 |  |  |  |  |  |  |
| 0.1 | 0.046387711664359906 | 14948.3109391343 |  |  |  |  |  |  |
| 0.2 | 0.04565212931399171 | 15135.905902680013 |  |  |  |  |  |  |
| 0.3 | 0.0451640469636235 | 15263.00158704872 |  |  |  |  |  |  |
| 0.4 | 0.04517096461325529 | 15261.185335030186 |  |  |  |  |  |  |
| 0.5 | 0.04524538226288709 | 15241.674034541371 |  |  |  |  |  |  |
| 0.6 | 0.044869799912518896 | 15340.659449025014 |  |  |  |  |  |  |
| 0.7 | 0.04522921756215069 | 15245.907957622423 |  |  |  |  |  |  |
| 0.8 | 0.04495863521178249 | 15317.130834594693 |  |  |  |  |  |  |
| 0.9 | 0.046443052861414286 | 14934.385228914152 |  |  |  |  |  |  |

## Input choices page

| Rating is | Yes/No | IBC | Type of firm | Earnings/Operating Measure |
|---|---|---|---|---|
| Aaa/AAA | Yes | High | 1 |  |
| Aa2/AA | No | Medium | 2 | EBITDA |
| A1/A+ |  | Low | 3 | EBIT |
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
