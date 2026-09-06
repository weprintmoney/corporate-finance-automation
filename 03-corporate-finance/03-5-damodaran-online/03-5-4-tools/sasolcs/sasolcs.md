---
title: "Sasolcs"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/eqegs/sasolcs.xls
---

# Sasolcs

Source: http://www.stern.nyu.edu/~adamodar/pc/eqegs/sasolcs.xls

Sheets: READ ME 1ST, FAQs, Inputs, Marginal tax rate by country, Operating leases, Default Spreads and Ratios, Optimal Capital Structure, Summary Table, Input choices page

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

| Country | Tax Rate |
|---|---|
| Afghanistan | 0.2 |
| Albania | 0.1 |
| Angola | 0.35 |
| Argentina | 0.35 |
| Armenia | 0.2 |
| Aruba | 0.28 |
| Australia | 0.3 |
| Austria | 0.25 |
| Bahamas | 0 |
| Bahrain | 0 |
| Bangladesh | 0.275 |
| Barbados | 0.25 |
| Belarus | 0.18 |
| Belgium | 0.33990000000000004 |
| Bermuda | 0 |
| Bolivia | 0.25 |
| Bonaire | 0 |
| Bosnia and Herzegovina | 0.1 |
| Botswana | 0.22 |
| Brazil | 0.34 |
| Bulgaria | 0.1 |
| Cambodia | 0.2 |
| Canada | 0.26 |
| Cayman Islands | 0 |
| Chile | 0.185 |
| China | 0.25 |
| Colombia | 0.33 |
| Costa Rica | 0.3 |
| Croatia | 0.2 |
| Curacao | 0.275 |
| Cyprus | 0.1 |
| Czech Republic | 0.19 |
| Denmark | 0.25 |
| Dominican Republic | 0.29 |
| Ecuador | 0.23 |
| Egypt | 0.25 |
| Estonia | 0.21 |
| El Salvador | 0.3 |
| Fiji | 0.28 |
| Finland | 0.245 |
| France | 0.3333 |
| Georgia | 0 |
| Germany | 0.2948 |
| Gibraltar | 0.1 |
| Greece | 0.2 |
| Guatemala | 0.31 |
| Guernsey | 0 |
| Honduras | 0.35 |
| Hong Kong | 0.165 |
| Hungary | 0.19 |
| Iceland | 0.2 |
| India | 0.3245 |
| Indonesia | 0.25 |
| Ireland | 0.125 |
| Isle of Man | 0 |
| Israel | 0.25 |
| Italy | 0.314 |
| Jamaica | 0.3333 |
| Japan | 0.3801 |
| Jersey | 0 |
| Jordan | 0.14 |
| Kazakhstan | 0.2 |
| Kenya | 0.3 |
| Korea, Republic of | 0.242 |
| Kuwait | 0.15 |
| Latvia | 0.15 |
| Libya | 0.2 |
| Liechtenstein | 0.125 |
| Lithuania | 0.15 |
| Luxembourg | 0.28800000000000003 |
| Macau | 0.12 |
| Macedonia | 0.1 |
| Malawi | 0.3 |
| Malaysia | 0.25 |
| Malta | 0.35 |
| Mauritius | 0.15 |
| Mexico | 0.3 |
| Montenegro | 0.09 |
| Mozambique | 0.32 |
| Namibia | 0.34 |
| Netherlands | 0.25 |
| New Zealand | 0.28 |
| Nigeria | 0.3 |
| Norway | 0.28 |
| Oman | 0.12 |
| Pakistan | 0.35 |
| Panama | 0.25 |
| Papua New Guinea | 0.3 |
| Paraguay | 0.1 |
| Peru | 0.3 |
| Philippines | 0.3 |
| Poland | 0.19 |
| Portugal | 0.25 |
| Qatar | 0.1 |
| Romania | 0.16 |
| Russia | 0.2 |
| Saba | 0 |
| Samoa | 0.27 |
| Saudi Arabia | 0.2 |
| Serbia | 0.1 |
| Singapore | 0.17 |
| Slovak Republic | 0.19 |
| Slovenia | 0.18 |
| South Africa | 0.3455 |
| Spain | 0.3 |
| Sri Lanka | 0.28 |
| St Eustatius | 0 |
| St Maarten | 0.345 |
| Sudan | 0.35 |
| Sweden | 0.263 |
| Switzerland | 0.21170000000000003 |
| Syria | 0.28 |
| Taiwan | 0.17 |
| Tanzania | 0.3 |
| Thailand | 0.23 |
| Trinidad and Tobago | 0.25 |
| Tunisia | 0.3 |
| Turkey | 0.2 |
| Uganda | 0.3 |
| Ukraine | 0.21 |
| United Arab Emirates | 0.55 |
| United Kingdom | 0.24 |
| United States | 0.4 |
| Uruguay | 0.25 |
| Vanuatu | 0 |
| Venezuela | 0.34 |
| Vietnam | 0.25 |
| Yemen | 0.2 |
| Zambia | 0.35 |
| Zimbabwe | 0.2575 |
| Africa average | 0.2902 |
| North America average | 0.33 |
| Asia average | 0.2289 |
| Europe average | 0.205 |
| Latin America average | 0.28300000000000003 |
| Oceania average | 0.28600000000000003 |
| EU average | 0.226 |
| OECD average | 0.2525 |
| Global average | 0.2443 |

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

| Sasol |
|---|
| 39994 |
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
|  |
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
| Eff. Tax Rate |
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

## Summary Table

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC | Firm Value (G) |
|---|---|---|---|---|---|---|---|---|
| 0 | 1.1132079034957088 | 0.14912455702175414 | Aaa/AAA | 0.0804 | 0.3455 | 0.0526218 | 0.14912455702175414 | 306160.1056620709 |
| 0.1 | 1.1941628560332578 | 0.15564952619628059 | Aaa/AAA | 0.0804 | 0.3455 | 0.0526218 | 0.14534675357665253 | 319617.42259134055 |
| 0.2 | 1.2953565467051942 | 0.16380573766443865 | Aa2/AA | 0.0834 | 0.3455 | 0.05458530000000001 | 0.14196165013155093 | 332722.03031907504 |
| 0.3 | 1.425462720426255 | 0.17429229526635617 | A3/A- | 0.08940000000000001 | 0.3455 | 0.05851230000000001 | 0.1395582966864493 | 342697.8989550629 |
| 0.4 | 1.5989376187210032 | 0.18827437206891287 | Baa2/BBB | 0.0964 | 0.3455 | 0.0630938 | 0.13820214324134772 | 348595.59306819877 |
| 0.5 | 1.8418024763336502 | 0.20784927959249222 | B2/B | 0.14140000000000003 | 0.3455 | 0.09254630000000003 | 0.15019778979624612 | 302541.2834376995 |
| 0.6 | 2.2060997627526207 | 0.23721164087786126 | C2/C | 0.1639 | 0.3455 | 0.10727255000000001 | 0.15924818635114452 | 275118.46596448345 |
| 0.7 | 2.8346678894881805 | 0.28787423189274736 | C2/C | 0.1639 | 0.3372589584491852 | 0.10862325671017854 | 0.1623985492649492 | 266703.5609171529 |
| 0.8 | 4.252001834232271 | 0.40211134783912106 | C2/C | 0.1639 | 0.29510158864303704 | 0.11553284962140623 | 0.1728485492649492 | 242136.89849932573 |
| 0.9 | 8.619001131992514 | 0.7540914912385966 | Ca2/CC | 0.1714 | 0.2508344373322638 | 0.12840697744125 | 0.19097542882098464 | 208778.1898521285 |

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
