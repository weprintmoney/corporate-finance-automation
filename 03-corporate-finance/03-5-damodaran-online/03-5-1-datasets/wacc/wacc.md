---
title: "Wacc"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls
---

# Wacc

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls

Sheets: Variables & FAQ, Industry Averages

## Variables & FAQ

| End Game | To estimate the hurdle rate (required return) on both equity and overall capital invested for firms. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Average regression beta across companies in the group. |
| Cost of Equity | Risk free Rate + Beta * Equity Risk Premium, in US $ |
| D/(D+E) | Total Debt (including lease debt)/ (Total Debt (including lease debt)+ Market Cap), aggregated across all firms in group, with all numbers other than market cap coming from most recent balance sheet; market cap is as of last day of the most recent year. |
| Cost of debt | Pre-tax cost of borrowing for sector, estimated based upon the standard deviation of equity. |
| After-tax Cost of Debt | Pre-tax cost of borrowing  (1- Marginal tax rate), in US $ |
| Cost of Capital | Cost of Equity * (Equity/ (Debt + Equity)) + Cost of Debt (1- Marginal tax rate) *(Debt/ (Debt + Equity)), with aggregated debt and market equity values across all companies in the sector, using most recent balance sheet for debt and most recent year-end for equity. |
| Cost of Capital (local currency) | You can convert the $ cost of capital for a sector into any other currency, if you can estimate an expected inflation rate for the local currency. |

## Industry Averages

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | Notes on how cost of capital is estimated for firms in US dollars and how to convert that into a cost of capital in a different currency |
| What is this data? | Cost of equity and capital (updateable) |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| To update this spreadsheet, enter the following |  |  |  |
| Long Term Treasury bond rate = |  |  | Basis Spread |
| Risk Premium to Use for Equity = |  | 0.3 | 0.0055060000000000005 |
| Global Default Spread to add to cost of debt = |  | 0.45 | 0.008872 |
| Do you want to use the marginal tax rate for cost of debt? |  | 0.65 | 0.011113 |
| If yes, enter the marginal tax rate to use |  | 0.8 | 0.018394999999999998 |
|  |  | 0.9 | 0.032098 |
| These costs of capital are in US$. To convert to a different currency, please enter |  | 1 | 0.050899 |
| Expected inflation rate in local currency = |  | 10 | 0.0885 |
| Expected inflation rate in US $ = |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Tax Rate | After-tax Cost of Debt |
| Advertising | 52 | 0.050166601892135954 | 0.039684750000000005 |
| Aerospace/Defense | 79 | 0.1157525444051738 | 0.039684750000000005 |
| Air Transport | 23 | 0.0829257860360182 | 0.039684750000000005 |
| Apparel | 35 | 0.09612500297378584 | 0.039684750000000005 |
| Auto & Truck | 33 | 0.03737150993812953 | 0.039684750000000005 |
| Auto Parts | 35 | 0.14999691449019154 | 0.039684750000000005 |
| Bank (Money Center) | 15 | 0.1843478364577707 | 0.0354795 |
| Banks (Regional) | 568 | 0.17609708151159398 | 0.0354795 |
| Beverage (Alcoholic) | 14 | 0.12349880380286866 | 0.039684750000000005 |
| Beverage (Soft) | 27 | 0.0684627965508008 | 0.039684750000000005 |
| Broadcasting | 24 | 0.07728859528725333 | 0.039684750000000005 |
| Brokerage & Investment Banking | 32 | 0.15273177578181318 | 0.038003999999999996 |
| Building Materials | 41 | 0.1802113978781021 | 0.038003999999999996 |
| Business & Consumer Services | 155 | 0.10382630217002471 | 0.038003999999999996 |
| Cable TV | 9 | 0.10643042905457614 | 0.038003999999999996 |
| Chemical (Basic) | 29 | 0.07683856093152415 | 0.039684750000000005 |
| Chemical (Diversified) | 4 | 0 | 0.038003999999999996 |
| Chemical (Specialty) | 59 | 0.13675158334443216 | 0.038003999999999996 |
| Coal & Related Energy | 16 | 0.03125 | 0.039684750000000005 |
| Computer Services | 64 | 0.10526994226576537 | 0.039684750000000005 |
| Computers/Peripherals | 36 | 0.05911353077642165 | 0.039684750000000005 |
| Construction Supplies | 40 | 0.16038852383860958 | 0.038003999999999996 |
| Diversified | 20 | 0.02756045788007777 | 0.0354795 |
| Drugs (Biotechnology) | 496 | 0.010795122386082115 | 0.04514625 |
| Drugs (Pharmaceutical) | 228 | 0.029938702770438724 | 0.04514625 |
| Education | 32 | 0.15540367121320292 | 0.039684750000000005 |
| Electrical Equipment | 112 | 0.048160938724098754 | 0.04514625 |
| Electronics (Consumer & Office) | 8 | 0 | 0.04514625 |
| Electronics (General) | 114 | 0.08036356729856782 | 0.039684750000000005 |
| Engineering/Construction | 48 | 0.1363531807406391 | 0.039684750000000005 |
| Entertainment | 92 | 0.03304355681192803 | 0.039684750000000005 |
| Environmental & Waste Services | 53 | 0.04267831701608498 | 0.039684750000000005 |
| Farming/Agriculture | 35 | 0.06294399257877176 | 0.039684750000000005 |
| Financial Svcs. (Non-bank & Insurance) | 176 | 0.12056567700542625 | 0.038003999999999996 |
| Food Processing | 78 | 0.10372593278493082 | 0.038003999999999996 |
| Food Wholesalers | 13 | 0.09152840668006618 | 0.038003999999999996 |
| Furn/Home Furnishings | 27 | 0.11382525542555506 | 0.039684750000000005 |
| Green & Renewable Energy | 15 | 0 | 0.04514625 |
| Healthcare Products | 204 | 0.048453372827770576 | 0.039684750000000005 |
| Healthcare Support Services | 104 | 0.09799646168506736 | 0.039684750000000005 |
| Heathcare Information and Technology | 115 | 0.06381881317110165 | 0.039684750000000005 |
| Homebuilding | 30 | 0.16989203344780976 | 0.038003999999999996 |
| Hospitals/Healthcare Facilities | 31 | 0.11347796258733156 | 0.039684750000000005 |
| Hotel/Gaming | 63 | 0.08308178299623932 | 0.038003999999999996 |
| Household Products | 110 | 0.06500436608160612 | 0.039684750000000005 |
| Information Services | 15 | 0.18162842926123732 | 0.038003999999999996 |
| Insurance (General) | 21 | 0.12768801589234566 | 0.039684750000000005 |
| Insurance (Life) | 20 | 0.15186017647763664 | 0.038003999999999996 |
| Insurance (Prop/Cas.) | 57 | 0.1836669176395358 | 0.0354795 |
| Investments & Asset Management | 283 | 0.03534923619833761 | 0.038003999999999996 |
| Machinery | 105 | 0.13373442732400442 | 0.039684750000000005 |
| Metals & Mining | 73 | 0.02516414295193868 | 0.04514625 |
| Office Equipment & Services | 14 | 0.12297383351664745 | 0.038003999999999996 |
| Oil/Gas (Integrated) | 4 | 0.2824095529705382 | 0.0354795 |
| Oil/Gas (Production and Exploration) | 142 | 0.06664478996170788 | 0.038003999999999996 |
| Oil/Gas Distribution | 23 | 0.09166185880832112 | 0.038003999999999996 |
| Oilfield Svcs/Equip. | 97 | 0.08746367186047936 | 0.039684750000000005 |
| Packaging & Container | 19 | 0.1557025871337487 | 0.0354795 |
| Paper/Forest Products | 6 | 0.08598511133455124 | 0.039684750000000005 |
| Power | 46 | 0.12748334654668436 | 0.0354795 |
| Precious Metals | 56 | 0.05974812957530874 | 0.04514625 |
| Publishing & Newspapers | 19 | 0.10205812286876828 | 0.038003999999999996 |
| R.E.I.T. | 190 | 0.01581382585274235 | 0.0354795 |
| Real Estate (Development) | 14 | 0.04907001511578525 | 0.039684750000000005 |
| Real Estate (General/Diversified) | 12 | 0.046482967477014005 | 0.038003999999999996 |
| Real Estate (Operations & Services) | 54 | 0.08697440271481936 | 0.039684750000000005 |
| Recreation | 49 | 0.11454512843876968 | 0.039684750000000005 |
| Reinsurance | 1 | 0.3035856573705179 | 0.0354795 |
| Restaurant/Dining | 64 | 0.09916012680622868 | 0.038003999999999996 |
| Retail (Automotive) | 34 | 0.10773098945749512 | 0.038003999999999996 |
| Retail (Building Supply) | 14 | 0.11839851054454309 | 0.039684750000000005 |
| Retail (Distributors) | 62 | 0.14586482228388625 | 0.038003999999999996 |
| Retail (General) | 23 | 0.19099933477629175 | 0.038003999999999996 |
| Retail (Grocery and Food) | 15 | 0.12221523285745305 | 0.039684750000000005 |
| Retail (REITs) | 26 | 0.016032624227080367 | 0.0354795 |
| Retail (Special Lines) | 94 | 0.10067307943310284 | 0.039684750000000005 |
| Rubber& Tires | 3 | 0 | 0.039684750000000005 |
| Semiconductor | 66 | 0.05106370873021537 | 0.039684750000000005 |
| Semiconductor Equip | 31 | 0.099620953538418 | 0.039684750000000005 |
| Shipbuilding & Marine | 8 | 0.052561473759605716 | 0.039684750000000005 |
| Shoe | 11 | 0.11861173771031724 | 0.039684750000000005 |
| Software (Entertainment) | 77 | 0.05286401405640245 | 0.039684750000000005 |
| Software (Internet) | 29 | 0.03054366211647507 | 0.039684750000000005 |
| Software (System & Application) | 309 | 0.05509792802786181 | 0.039684750000000005 |
| Steel | 19 | 0.09275991753479733 | 0.038003999999999996 |
| Telecom (Wireless) | 12 | 0.04023108287054421 | 0.038003999999999996 |
| Telecom. Equipment | 57 | 0.07062863646712804 | 0.039684750000000005 |
| Telecom. Services | 39 | 0.034002984466728295 | 0.039684750000000005 |
| Tobacco | 10 | 0.1476725198349122 | 0.04514625 |
| Transportation | 19 | 0.08538457407963723 | 0.038003999999999996 |
| Transportation (Railroads) | 4 | 0.16983557424101936 | 0.0354795 |
| Trucking | 26 | 0.12598448805395965 | 0.038003999999999996 |
| Utility (General) | 14 | 0.12765942282237325 | 0.0354795 |
| Utility (Water) | 14 | 0.11191995155470791 | 0.0354795 |
| Total Market | 5994 | 0.08301735903677065 | 0.039684750000000005 |
| Total Market (without financials) | 4822 | 0.071032603531751 | 0.039684750000000005 |
