---
title: "Apv"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/apv.xls
---

# Apv

Source: https://www.stern.nyu.edu/~adamodar/pc/apv.xls

Sheets: READ ME FIRST, FAQs, Inputs, Operating Lease Information, Default Spreads and Ratios, Adjusted Present Value, Country ERP, Input choices page

## READ ME FIRST

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
|  |
|  |
| READING THE OUTPUT |
| Summary |
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
| Q2: My spreadsheet has gone crazy. I get errors all over. | I am sorry to say this, but you probably just made an input error. While you might have |
| What did I do wrong? | fixed it, the iterations in the spreadsheet make it very sensitive and the errors will not |
|  | go away. The only fix (Sorry, sorry…) is to copy the inputs into a fresh version of the spreadsheet. |
| Q3: I am entering the inputs for my company but the | You probably forgot to check the iteration box (see Q1) |
| optimal numbers do not seem to change from the |  |
| originals |  |
| Q4: I am getting an optimal debt ratio of 0%. This can't | Sure. If your operating income is either negative or very low, relative to your firm value, |
| be right. Can it? | you can end up at an optimal debt ratio of 0%. For instance, if you have EBIT of 100 on a |
|  | firm value of 10000, a 10% debt ratio would probably push you into a C rating and give |
|  | you a very high cost of capital. |

## Inputs

| Inputs |
|---|
| Please enter the name of the company you are analyzing: |
| Date of analysis |
| Financial Information |
| Earnings before interest, taxes and depreciation (EBITDA) |
| Depreciation and Amortization: |
| Capital Spending: |
| Interest expense on debt: |
| Tax rate on ordinary income: |
| Cost of Bankrtupcy as a percent of market value of firm = |
| Current Rating on debt (if available): |
| Interest rate based upon rating: |
| Market Information |
| Number of shares outstanding: |
| Market price per share: |
| Beta of the stock: |
| Book value of debt: |
| Can you estimate the market value of the outstanding debt? |
| If so, enter the market value of debt: |
| Do you want me to try and estimate market value of debt? |
| If yes, enter the average maturity of outstanding debt? |
| Do you have any operating leases? |
| General Market Data |
| Current long-term (LT) government bond rate: |
| Risk premium (for use in the CAPM) |
| Country default spread (for cost of debt) |
|  |
| General Data |
| Which spread/ratio table would you like to use for your anlaysis? |
| Do you want to assume that existing debt is refinanced at the 'new' rate? |
| Do you want the firm's current rating to be adjusted to the synthetic rating? |

## Operating Lease Information

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
| Enter current Earnings before interest and taxes (EBIT) = |
| Enter current interest expenses = |
| Enter current long term government bond rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
|  |
| For large or stable firms |
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

## Adjusted Present Value

| Hormel |
|---|
| 39924 |
| Capital Structure |
| Current MV of Equity = |
| Market Value of interest-bearing debt = |
| # of Shares Outstanding = |
| Debt Value of Operating leases (if any) |
| Risk Premium = |
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
|  |
|  |
| D/(D+E) |
| D/E |
| $ Debt |
| Beta |
| Cost of Equity |
|  |
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
| Probability of Bankruptcy |
| Eff. Tax Rate |
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
|  |
| Adjusted Present Value Approach |
| Current Value of the Firm = |
|  - Tax Benefit on Current Debt = |
|  + Expected Current Bankruptcy Cost = |
| Unlevered Value of Firm = |
|  |
| Debt Ratio |
|  $ Debt |
| Unlev. Firm Value |
| Tax Benefits |
| Bond Rating |
| Prob. of Default |
| Bankruptcy Cost |
| Index variable |
| Levered Firm Value |
|  |
|  |
| Debt Ratio |
| 0 |
| 0.1 |
| 0.2 |
| 0.3 |
| 0.4 |
| 0.5 |
| 0.6 |
| 0.7 |
| 0.8 |
| 0.9 |

## Country ERP

_209 rows — showing first 20. Full data: [`apv-country-erp.csv`](apv-country-erp.csv)_

| Mature Market ERP + | 0.0433 | Updated January 1, 2025 |
|---|---|---|
| Changing this number will update all your country equity risk premiums. |  |  |
|  |  |  |
| Country | Moody's rating | Adj. Default Spread |
| Abu Dhabi | Aa2 | 0.0048889784279692525 |
| Albania | Ba3 | 0.035619699975204554 |
| Algeria | NR | 0.029799487560955448 |
| Andorra (Principality of) | Baa1 | 0.015830977766757577 |
| Angola | B3 | 0.06437154930159515 |
| Anguilla | NR | 0.06012263625836532 |
| Antigua & Barbuda | NR | 0.0601 |
| Argentina | Ca | 0.11884873749896685 |
| Armenia | Ba3 | 0.035619699975204554 |
| Aruba | Baa3 | 0.021767594429291676 |
| Australia | Aaa | 0 |
| Austria | Aa1 | 0.003957744441689394 |
| Azerbaijan | Ba1 | 0.024794104884701216 |
| Bahamas | B1 | 0.04458282709314818 |
| Bahrain | B2 | 0.05447718819737168 |
| Bangladesh | B2 | 0.05447718819737168 |
| Barbados | B3 | 0.06437154930159515 |

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
