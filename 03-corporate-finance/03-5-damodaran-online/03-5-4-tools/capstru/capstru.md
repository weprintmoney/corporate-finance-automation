---
title: "Capstru"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/capstru.xlsx
---

# Capstru

Source: https://www.stern.nyu.edu/~adamodar/pc/capstru.xlsx

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

| Disney |
|---|
| 2023-02-26 00:00:00 |
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

_251 rows — showing first 20. Full data: [`capstru-marginal-tax-rate-by-country.csv`](capstru-marginal-tax-rate-by-country.csv)_

| Country | Corporate Tax Rate |
|---|---|
| Aruba | 0.22 |
| Afghanistan | 0.2 |
| Angola | 0.25 |
| Anguilla | 0 |
| Aland Islands | 0.2 |
| Albania | 0.15 |
| Andorra | 0.1 |
| United Arab Emirates | 0.09 |
| Argentina | 0.35 |
| Armenia | 0.18 |
| American Samoa | 0.34 |
| Antigua and Barbuda | 0.25 |
| Australia | 0.3 |
| Austria | 0.23 |
| Azerbaijan | 0.2 |
| Burundi | 0.3 |
| Belgium | 0.25 |
| Benin | 0.3 |
| Bonaire, Sint Eustatius and Saba | 0.258 |
| Burkina Faso | 0.275 |

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
| Eastern Europe |
| Middle East |
| North America |
| Western Europe |
|  |
|  |
| Total |

## Country ERP 

_220 rows — showing first 20. Full data: [`capstru-country-erp.csv`](capstru-country-erp.csv)_

| Mature Market ERP + | 0.0423 | Updated January 1, 2026 |
|---|---|---|
| Changing this number will update all your country equity risk premiums. |  |  |
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.0042 |
| Albania | Ba3 | 0.0306 |
| Algeria | NR | 0.0383 |
| Andorra (Principality of) | Baa1 | 0.0136 |
| Angola | B3 | 0.0552 |
| Anguilla | NR | 0.04915183026184869 |
| Antigua & Barbuda | NR | 0.027785941866780777 |
| Argentina | Caa1 | 0.0637 |
| Armenia | Ba3 | 0.0306 |
| Aruba | Baa3 | 0.0187 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.0023 |
| Azerbaijan | Baa3 | 0.0187 |
| Bahamas | B1 | 0.0383 |
| Bahrain | B2 | 0.0467 |
| Bangladesh | B2 | 0.0467 |
| Barbados | B2 | 0.0467 |
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
| 0 | 0.861791468261517 | 0.09596441605208628 | Aaa/AAA | 0.0611 | 0.25 | 0.045825000000000005 | 0.09596441605208628 | 215350.8480313889 |
| 0.1 | 0.9336074239499766 | 0.10071145072309345 | Aaa/AAA | 0.0611 | 0.25 | 0.045825000000000005 | 0.09522280565078411 | 218191.44673472116 |
| 0.2 | 1.0233773685605514 | 0.10664524406185244 | A3/A- | 0.065972 | 0.25 | 0.049479 | 0.09521199524948196 | 218233.40818955714 |
| 0.3 | 1.1387958687741475 | 0.11427440692597116 | B1/B+ | 0.08463100000000001 | 0.25 | 0.06347325000000001 | 0.09903405984817981 | 204339.59214906534 |
| 0.4 | 1.352913619600388 | 0.12842759025558564 | C2/C | 0.21710000000000002 | 0.1451722903518528 | 0.18558309576461277 | 0.1512897924591965 | 109247.10996226399 |
| 0.5 | 1.6356273244025117 | 0.14711496614300604 | C2/C | 0.21710000000000002 | 0.10206136328774991 | 0.1949424780302295 | 0.17102872208661776 | 92914.14103350654 |
| 0.6 | 2.0527538501726337 | 0.1746870294964111 | C2/C | 0.21710000000000002 | 0.0786925253788422 | 0.20001585274025338 | 0.18988432344271647 | 81302.91487231248 |
| 0.7 | 2.7438809739402252 | 0.2203705323774489 | C2/C | 0.21710000000000002 | 0.06403136042274413 | 0.20319879165222227 | 0.20835031386979025 | 72437.62957452638 |
| 0.8 | 4.144437916633337 | 0.3129473462894636 | D2/D | 0.24710000000000001 | 0.04772599600171604 | 0.235306906387976 | 0.2508349943682735 | 57909.86206510798 |
| 0.9 | 8.29826796594114 | 0.5875155125487094 | D2/D | 0.24710000000000001 | 0.04121217621742873 | 0.2369164712566734 | 0.271976375385877 | 52654.84658739046 |
| Debt Ratio | $ Debt | Interest Expense | Interest Coverage Ratio | Bond Rating | Pre-tax cost of debt | Tax rate | After-tax cost of debt |  |
| 0 | 0 | 0 | ∞ | Aaa/AAA | 0.0611 | 0.25 | 0.045825000000000005 |  |
| 0.1 | 22808.00599631456 | 730.5385582062464 | 9.317978881028559 | Aaa/AAA | 0.0611 | 0.25 | 0.045825000000000005 |  |
| 0.2 | 45616.01199262912 | 1703.531387289088 | 3.9959010488062647 | A3/A- | 0.065972 | 0.25 | 0.049479 |  |
| 0.3 | 68424.01798894367 | 3648.087641681318 | 1.8659482791388213 | B1/B+ | 0.08463100000000001 | 0.25 | 0.06347325000000001 |  |
| 0.4 | 91232.02398525825 | 11722.52438920066 | 0.5806891614074112 | C2/C | 0.21710000000000002 | 0.1451722903518528 | 0.18558309576461277 |  |
| 0.5 | 114040.02998157279 | 16674.142491000548 | 0.4082454531509997 | C2/C | 0.21710000000000002 | 0.10206136328774991 | 0.1949424780302295 |  |
| 0.6 | 136848.03597788734 | 21625.760592800438 | 0.3147701015153689 | C2/C | 0.21710000000000002 | 0.0786925253788422 | 0.20001585274025338 |  |
| 0.7 | 159656.0419742019 | 26577.378694600324 | 0.2561254416909764 | C2/C | 0.21710000000000002 | 0.06403136042274413 | 0.20319879165222227 |  |
| 0.8 | 182464.0479705165 | 35657.41643662135 | 0.19090398400686404 | D2/D | 0.24710000000000001 | 0.04772599600171604 | 0.235306906387976 |  |
| 0.9 | 205272.05396683104 | 41293.27471831068 | 0.1648487048697148 | D2/D | 0.24710000000000001 | 0.04121217621742873 | 0.2369164712566734 |  |
| Debt Ratio | Cost of Capital | Enterprise Value |  |  |  |  |  |  |
| 0 | 0.09596441605208628 | 215350.8480313889 |  |  |  |  |  |  |
| 0.1 | 0.09522280565078411 | 218191.44673472116 |  |  |  |  |  |  |
| 0.2 | 0.09521199524948196 | 218233.40818955714 |  |  |  |  |  |  |
| 0.3 | 0.09903405984817981 | 204339.59214906534 |  |  |  |  |  |  |
| 0.4 | 0.1512897924591965 | 109247.10996226399 |  |  |  |  |  |  |
| 0.5 | 0.17102872208661776 | 92914.14103350654 |  |  |  |  |  |  |
| 0.6 | 0.18988432344271647 | 81302.91487231248 |  |  |  |  |  |  |
| 0.7 | 0.20835031386979025 | 72437.62957452638 |  |  |  |  |  |  |
| 0.8 | 0.2508349943682735 | 57909.86206510798 |  |  |  |  |  |  |
| 0.9 | 0.271976375385877 | 52654.84658739046 |  |  |  |  |  |  |

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
