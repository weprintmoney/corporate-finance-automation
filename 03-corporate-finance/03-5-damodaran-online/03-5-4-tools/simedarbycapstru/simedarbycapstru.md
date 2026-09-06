---
title: "Simedarbycapstru"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/country/SimeDarbycapstru.xls
---

# Simedarbycapstru

Source: http://www.stern.nyu.edu/~adamodar/pc/country/SimeDarbycapstru.xls

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

| Sime Darby |
|---|
| 41547 |
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
| 0 | 0.8042822896584647 | 0.08273298327394205 | Aaa/AAA | 0.0484 | 0.24 | 0.036784 | 0.08273298327394205 | 77532.51900921352 |
| 0.1 | 0.8721994607851796 | 0.08731265741707493 | A2/A | 0.0534 | 0.24 | 0.040584 | 0.08263979167536745 | 77665.97684428071 |
| 0.2 | 0.957095924693573 | 0.09303725009599102 | B2/B | 0.08739999999999999 | 0.24 | 0.066424 | 0.08771460007679283 | 71009.84894198767 |
| 0.3 | 1.0662485211472217 | 0.10039744068316887 | Ca2/CC | 0.1224 | 0.24 | 0.093024 | 0.0981854084782182 | 60340.03241765576 |
| 0.4 | 1.2562949781810668 | 0.11321232726977419 | C2/C | 0.1474 | 0.1569887320634386 | 0.12425986089384915 | 0.11763134071940418 | 47175.54759835299 |
| 0.5 | 1.50755397381728 | 0.130154792723729 | C2/C | 0.1474 | 0.12559098565075089 | 0.12888788871507934 | 0.1295213407194042 | 41623.084554901456 |
| 0.6 | 1.9086706141499423 | 0.15720220173145283 | D2/D | 0.1824 | 0.08457653182072682 | 0.16697324059589944 | 0.1630648250501208 | 31247.540395843553 |
| 0.7 | 2.544894152199923 | 0.20010293564193712 | D2/D | 0.1824 | 0.07249417013205155 | 0.1691770633679138 | 0.1784548250501208 | 28040.57692180197 |
| 0.8 | 3.8173412282998864 | 0.2859044034629058 | D2/D | 0.1824 | 0.0634323988655451 | 0.17082993044692457 | 0.19384482505012082 | 25430.61027364277 |
| 0.9 | 7.634682456599771 | 0.5433088069258114 | D2/D | 0.1824 | 0.0563843545471512 | 0.17211549373059962 | 0.20923482505012078 | 23265.13335461057 |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| Debt Ratio | $ Debt | Interest Expense | Interest Coverage Ratio | Bond Rating | Pre-tax cost of debt | Tax rate | After-tax cost of debt |  |
| 0 | 0 | 0 | ∞ | Aaa/AAA | 0.0484 | 0.24 | 0.036784 |  |
| 0.1 | 7952.415461110424 | 424.65898562329664 | 7.2222656386238615 | A2/A | 0.0534 | 0.24 | 0.040584 |  |
| 0.2 | 15904.830922220848 | 1390.082222602102 | 2.206344308366786 | B2/B | 0.08739999999999999 | 0.24 | 0.066424 |  |
| 0.3 | 23857.246383331272 | 2920.126957319748 | 1.0502968003881106 | Ca2/CC | 0.1224 | 0.24 | 0.093024 |  |
| 0.4 | 31809.661844441696 | 4688.744155870706 | 0.6541197169309942 | C2/C | 0.1474 | 0.1569887320634386 | 0.12425986089384915 |  |
| 0.5 | 39762.07730555212 | 5860.930194838383 | 0.5232957735447954 | C2/C | 0.1474 | 0.12559098565075089 | 0.12888788871507934 |  |
| 0.6 | 47714.492766662544 | 8703.123480639248 | 0.352402215919695 | D2/D | 0.1824 | 0.08457653182072682 | 0.16697324059589944 |  |
| 0.7 | 55666.90822777297 | 10153.64406074579 | 0.3020590422168814 | D2/D | 0.1824 | 0.07249417013205155 | 0.1691770633679138 |  |
| 0.8 | 63619.32368888339 | 11604.164640852332 | 0.2643016619397712 | D2/D | 0.1824 | 0.0634323988655451 | 0.17082993044692457 |  |
| 0.9 | 71571.73914999382 | 13054.685220958874 | 0.23493481061312993 | D2/D | 0.1824 | 0.0563843545471512 | 0.17211549373059962 |  |

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
