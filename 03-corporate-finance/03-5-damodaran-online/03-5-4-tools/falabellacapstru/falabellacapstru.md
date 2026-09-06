---
title: "Falabellacapstru"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/country/FalabellaCapStru.xls
---

# Falabellacapstru

Source: http://www.stern.nyu.edu/~adamodar/pc/country/FalabellaCapStru.xls

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
|  |
| References |
| Corporate Finance: Theory and Practice, Chapter 18 |
| Applied Corporate Finance: Chapter 8 |

## FAQs

| Question | Answer |
|---|---|
| Q1: What do I do excel says there are circular references? | Go into preferences, choose calculation options and make sure the iteration box has a check in it. |
| Q2: My spreadsheet has gone crazy. I get errors all over. What did I do wrong? | I am sorry to say this, but you probably just made an input error. While you might have fixed it, the iterations in the spreadsheet make it very sensitive and the errors will not go away. The only fix (Sorry, sorry…) is to copy the inputs into a fresh version of the spreadsheet. |
|  |  |
|  |  |
| Q3: I am entering the inputs for my company but the optimal numbers do not seem to change from the originals. | You probably forgot to check the iteration box (see Q1) |
|  |  |
|  |  |
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

| Inputs |
|---|
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
| Beta of the stock: |
| Cash and marketable securities = |
| Book value of debt: |
| Can you estimate the market value of the interest bearing debt? |
| If so, enter the market value of "interest bearing" debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the weighted average maturity of outstanding debt? |
| Do you have any operating leases? |
| Indirect bankruptcy costs & ratings constraints (if any) |
| Do you want to incorporate indirect bankruptcy costs into your optimal? |
| If yes, specify the magnitude of your indirect bankruptcy costs |
| General Market Data |
| Current riskfree rate in the currency of analysis = |
| Risk premium (for use in the CAPM) |
| Country Default spread (for cost of debt) |
|  |
| General Data |
| Which spread/ratio table would you like to use for your anlaysis? |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |
| Do you want the firm's current rating & cost of debt to be adjusted to the synthetic rating? |

## Marginal tax rate by country

| Country | 2016 |
|---|---|
| Afghanistan | 0.2 |
| Albania | 0.15 |
| Algeria | 0.26 |
| Angola | 0.3 |
| Argentina | 0.35 |
| Armenia | 0.2 |
| Aruba | 0.25 |
| Australia | 0.3 |
| Austria | 0.25 |
| Bahamas | 0 |
| Bahrain | 0 |
| Bangladesh | 0.25 |
| Barbados | 0.25 |
| Belarus | 0.18 |
| Belgium | 0.33990000000000004 |
| Bermuda | 0 |
| Bolivia | 0.25 |
| Bonaire, Saint Eustatius and Saba | 0 |
| Bosnia and Herzegovina | 0.1 |
| Botswana | 0.22 |
| Brazil | 0.34 |
| Bulgaria | 0.1 |
| Cambodia | 0.2 |
| Cameroon | 0.33 |
| Canada | 0.265 |
| Cayman Islands | 0 |
| Chile | 0.24 |
| China | 0.25 |
| Colombia | 0.25 |
| Costa Rica | 0.3 |
| Croatia | 0.2 |
| Curacao | 0.22 |
| Cyprus | 0.125 |
| Czech Republic | 0.19 |
| Denmark | 0.22 |
| Dominican Republic | 0.27 |
| Ecuador | 0.22 |
| Egypt | 0.225 |
| El Salvador | 0.3 |
| Estonia | 0.2 |
| Fiji | 0.2 |
| Finland | 0.2 |
| France | 0.33299999999999996 |
| Georgia | 0.15 |
| Germany | 0.29719999999999996 |
| Ghana | 0.25 |
| Gibraltar | 0.1 |
| Greece | 0.29 |
| Guatemala | 0.25 |
| Guernsey | 0 |
| Honduras | 0.3 |
| Hong Kong SAR | 0.165 |
| Hungary | 0.19 |
| Iceland | 0.2 |
| India | 0.3461 |
| Indonesia | 0.25 |
| Iraq | 0.15 |
| Ireland | 0.125 |
| Isle of Man | 0 |
| Israel | 0.25 |
| Italy | 0.314 |
| Jamaica | 0.25 |
| Japan | 0.3086 |
| Jersey | 0.2 |
| Jordan | 0.2 |
| Kazakhstan | 0.2 |
| Kenya | 0.3 |
| Korea, Republic of | 0.242 |
| Kuwait | 0.15 |
| Latvia | 0.15 |
| Lebanon | 0.15 |
| Libya | 0.2 |
| Liechtenstein | 0.125 |
| Lithuania | 0.15 |
| Luxembourg | 0.2922 |
| Macau | 0.12 |
| Macedonia | 0.1 |
| Malawi | 0.3 |
| Malaysia | 0.24 |
| Malta | 0.35 |
| Mauritius | 0.15 |
| Mexico | 0.3 |
| Moldova | 0.12 |
| Montenegro | 0.09 |
| Morocco | 0.31 |
| Mozambique | 0.32 |
| Namibia | 0.32 |
| Netherlands | 0.25 |
| New Zealand | 0.28 |
| Nigeria | 0.3 |
| Norway | 0.25 |
| Oman | 0.12 |
| Pakistan | 0.32 |
| Panama | 0.25 |
| Papua New Guinea | 0.3 |
| Paraguay | 0.1 |
| Peru | 0.28 |
| Philippines | 0.3 |
| Poland | 0.19 |
| Portugal | 0.21 |
| Qatar | 0.1 |
| Romania | 0.16 |
| Russia | 0.2 |
| Samoa | 0.27 |
| Saudi Arabia | 0.2 |
| Serbia | 0.15 |
| Sierra Leone | 0.3 |
| Singapore | 0.17 |
| Sint Maarten (Dutch part) | 0.345 |
| Slovakia | 0.22 |
| Slovenia | 0.17 |
| South Africa | 0.28 |
| Spain | 0.25 |
| Sri Lanka | 0.15 |
| St Maarten | 0.345 |
| Sudan | 0.35 |
| Suriname | 0 |
| Sweden | 0.22 |
| Switzerland | 0.17920000000000003 |
| Syria | 0.22 |
| Taiwan | 0.17 |
| Tanzania | 0.3 |
| Thailand | 0.2 |
| Trinidad and Tobago | 0.25 |
| Tunisia | 0.25 |
| Turkey | 0.2 |
| Uganda | 0.3 |
| Ukraine | 0.18 |
| United Arab Emirates | 0.55 |
| United Kingdom | 0.2 |
| United States | 0.4 |
| Uruguay | 0.25 |
| Vanuatu | 0 |
| Venezuela | 0.34 |
| Vietnam | 0.22 |
| Yemen | 0.2 |
| Zambia | 0.35 |
| Zimbabwe | 0.2575 |
| Africa average | 0.2746 |
| Americas average | 0.2786 |
| Asia average | 0.2192 |
| Europe average | 0.2048 |
| Oceania average | 0.26 |
| North America average | 0.3325 |
| Latin America average | 0.2729 |
| EU average | 0.22089999999999999 |
| OECD average | 0.2481 |
| Global average | 0.23620000000000002 |

## Operating leases

| Operating Lease Converter |
|---|
| Operating lease expenses are really financial expenses, and should be treated as such. Accounting standards allow them to |
| be treated as operating expenses. This program will convert commitments to make operating leases into debt and |
| adjust the operating income accordingly, by adding back the imputed interest expense on this debt. |
|  |
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
| Pre-tax Cost of Debt = |
|  |
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
|  |
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
|  |
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

## Optimal Capital Structure

| Falabella |
|---|
| 41471 |
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
|  |
| Assumes perpeutal growth |
|  |
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
|  |
| Pre-tax Int. cov |
| Funds/Debt |
| Likely Rating |
| Pre-tax cost of debt |
| Tax rate |
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
|  |
|  |

## Repurchase price Worksheet

| Stock price buyback effect |
|---|
| Current Stock price = |
| # Shares outstanding before buyback = |
| Expected buyback price = |
|  |
| Current Debt = |
| Debt at Optimal = |
| New Debt issued = |
| # Shares bought back = |
| Shares outstanding after buyback = |
|  |
| Enterprise value after buyback = |
|  + Cash |
|  - Debt |
| Equity value after buyback  |
| / Number of shares after buyback |
| Value per share for remaining shares |

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Enterprise Value |
|---|---|---|---|---|---|---|---|---|
| 0 | 0.6395874302541078 | 0.08383198458771876 | Aaa/AAA | 0.0472 | 0.24 | 0.035872 | 0.08383198458771876 | 17503547.715289056 |
| 0.1 | 0.6935970354755658 | 0.08802312995290391 | Aa2/AA | 0.0492 | 0.24 | 0.037392 | 0.08296001695761353 | 17822098.189451236 |
| 0.2 | 0.7611090420023883 | 0.09326206165938533 | A3/A- | 0.053700000000000005 | 0.24 | 0.040812 | 0.08277204932750827 | 17892292.33003293 |
| 0.3 | 0.84791019325116 | 0.09999783099629003 | B3/B- | 0.09620000000000001 | 0.24 | 0.07311200000000001 | 0.09193208169740301 | 12032681.229094472 |
| 0.4 | 0.9986211509958315 | 0.11169300131727652 | C2/C | 0.1462 | 0.1579719118328834 | 0.12310450649003245 | 0.11625760338637889 | 7037575.613440143 |
| 0.5 | 1.1983453811949978 | 0.12719160158073184 | C2/C | 0.1462 | 0.12637752946630673 | 0.12772360519202594 | 0.1274576033863789 | 6184628.599111881 |
| 0.6 | 1.525359134787526 | 0.152567868859512 | D2/D | 0.18120000000000003 | 0.07672596152439315 | 0.16729725577177998 | 0.1614055010068728 | 4076087.787717838 |
| 0.7 | 2.0338121797167017 | 0.19202382514601607 | D2/D | 0.18120000000000003 | 0.06576510987805129 | 0.16928336209009714 | 0.17610550100687283 | 3651308.424928799 |
| 0.8 | 3.050718269575053 | 0.27093573771902413 | D2/D | 0.18120000000000003 | 0.057544471143294876 | 0.17077294182883498 | 0.19080550100687282 | 3306708.059216421 |
| 0.9 | 6.101436539150106 | 0.5076714754380482 | D2/D | 0.18120000000000003 | 0.05115064101626207 | 0.17193150384785333 | 0.20550550100687281 | 3021543.190293773 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Debt Ratio | $ Debt | Interest Expense | Interest Coverage Ratio | Bond Rating | Pre-tax cost of debt | Tax rate | After-tax cost of debt |  |
| 0 | 0 | 0 | ∞ | Aaa/AAA | 0.0472 | 0.24 | 0.035872 |  |
| 0.1 | 1921869.3141861649 | 94555.97025795931 | 11.620047204659562 | Aa2/AA | 0.0492 | 0.24 | 0.037392 |  |
| 0.2 | 3843738.6283723298 | 206408.7643435941 | 5.323150116101029 | A3/A- | 0.053700000000000005 | 0.24 | 0.040812 |  |
| 0.3 | 5765607.942558494 | 554651.4840741272 | 1.5926454057081627 | B3/B- | 0.09620000000000001 | 0.24 | 0.07311200000000001 |  |
| 0.4 | 7687477.2567446595 | 1123909.1749360692 | 0.6582162993036809 | C2/C | 0.1462 | 0.1579719118328834 | 0.12310450649003245 |  |
| 0.5 | 9609346.570930824 | 1404886.4686700865 | 0.5265730394429446 | C2/C | 0.1462 | 0.12637752946630673 | 0.12772360519202594 |  |
| 0.6 | 11531215.885116989 | 2089456.3183831987 | 0.3196915063516381 | D2/D | 0.18120000000000003 | 0.07672596152439315 | 0.16729725577177998 |  |
| 0.7 | 13453085.199303152 | 2437699.0381137314 | 0.274021291158547 | D2/D | 0.18120000000000003 | 0.06576510987805129 | 0.16928336209009714 |  |
| 0.8 | 15374954.513489319 | 2785941.757844265 | 0.2397686297637287 | D2/D | 0.18120000000000003 | 0.057544471143294876 | 0.17077294182883498 |  |
| 0.9 | 17296823.827675484 | 3134184.4775747983 | 0.21312767090109197 | D2/D | 0.18120000000000003 | 0.05115064101626207 | 0.17193150384785333 |  |

## Input choices page

| Rating is | Yes/No | IBC | Type of firm |
|---|---|---|---|
| Aaa/AAA | Yes | High | 1 |
| Aa2/AA | No | Medium | 2 |
| A1/A+ |  | Low |  |
| A2/A |  |  |  |
| A3/A- |  |  |  |
| Baa2/BBB |  |  |  |
| Ba1/BB+ |  |  |  |
| Ba2/BB |  |  |  |
| B1/B+ |  |  |  |
| B2/B |  |  |  |
| B3/B- |  |  |  |
| Caa/CCC |  |  |  |
| Ca2/CC |  |  |  |
| C2/C |  |  |  |
| D2/D |  |  |  |
| Not rated |  |  |  |
|  |  |  |  |
| Rating is |  |  |  |
| D2/D |  |  |  |
| Caa/CCC |  |  |  |
| Ca2/CC |  |  |  |
| C2/C |  |  |  |
| B3/B- |  |  |  |
| B2/B |  |  |  |
| B1/B+ |  |  |  |
| Ba2/BB |  |  |  |
| Ba1/BB+ |  |  |  |
| Baa2/BBB |  |  |  |
| A3/A- |  |  |  |
| A2/A |  |  |  |
| A1/A+ |  |  |  |
| Aa2/AA |  |  |  |
| Aaa/AAA |  |  |  |
