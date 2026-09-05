---
title: "Wacceurope"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/waccEurope.xls
---

# Wacceurope

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/waccEurope.xls

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
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | Pricing ratios (or multiples) can be used to price companies, with the end game of determining whether they are under or over priced. |
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
| Expected inflation rate in Euros = |  | 10 | 0.0885 |
| Expected inflation rate in US $ = |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Tax Rate | After-tax Cost of Debt |
| Advertising | 83 | 0.14455754809953816 | 0.041070036799999994 |
| Aerospace/Defense | 67 | 0.12744836224799488 | 0.041070036799999994 |
| Air Transport | 33 | 0.2036085512845582 | 0.038564386400000004 |
| Apparel | 109 | 0.17634028830101575 | 0.041070036799999994 |
| Auto & Truck | 31 | 0.09219392598557076 | 0.042738237199999994 |
| Auto Parts | 58 | 0.14359021470143365 | 0.041070036799999994 |
| Bank (Money Center) | 113 | 0.21704732753554598 | 0.038564386400000004 |
| Banks (Regional) | 69 | 0.1775357159868431 | 0.038564386400000004 |
| Beverage (Alcoholic) | 52 | 0.14678759741927233 | 0.038564386400000004 |
| Beverage (Soft) | 14 | 0.1729325201640237 | 0.038564386400000004 |
| Broadcasting | 18 | 0.22302049544628152 | 0.041070036799999994 |
| Brokerage & Investment Banking | 69 | 0.19043405018547374 | 0.041070036799999994 |
| Building Materials | 84 | 0.15376796630950804 | 0.038564386400000004 |
| Business & Consumer Services | 176 | 0.1721249811619091 | 0.041070036799999994 |
| Cable TV | 2 | 0 | 0.05835947119999999 |
| Chemical (Basic) | 58 | 0.0914468586346967 | 0.041070036799999994 |
| Chemical (Diversified) | 7 | 0.13553811285042505 | 0.038564386400000004 |
| Chemical (Specialty) | 92 | 0.12951939390154169 | 0.041070036799999994 |
| Coal & Related Energy | 15 | 0.07460336573934703 | 0.042738237199999994 |
| Computer Services | 210 | 0.15884217827042404 | 0.041070036799999994 |
| Computers/Peripherals | 38 | 0.10500921627756248 | 0.042738237199999994 |
| Construction Supplies | 119 | 0.1933618464803935 | 0.041070036799999994 |
| Diversified | 72 | 0.1617108826084317 | 0.038564386400000004 |
| Drugs (Biotechnology) | 199 | 0.026765069600688852 | 0.042738237199999994 |
| Drugs (Pharmaceutical) | 115 | 0.07835851187536609 | 0.042738237199999994 |
| Education | 18 | 0.15851438148394947 | 0.042738237199999994 |
| Electrical Equipment | 146 | 0.10545687908099692 | 0.042738237199999994 |
| Electronics (Consumer & Office) | 17 | 0.17297956944025167 | 0.041070036799999994 |
| Electronics (General) | 142 | 0.10366764394611248 | 0.042738237199999994 |
| Engineering/Construction | 160 | 0.16794449155515587 | 0.041070036799999994 |
| Entertainment | 199 | 0.05012509029200847 | 0.042738237199999994 |
| Environmental & Waste Services | 48 | 0.1490492995125933 | 0.041070036799999994 |
| Farming/Agriculture | 46 | 0.1741894264700056 | 0.041070036799999994 |
| Financial Svcs. (Non-bank & Insurance) | 146 | 0.14532697832867147 | 0.041070036799999994 |
| Food Processing | 173 | 0.1348913828762827 | 0.041070036799999994 |
| Food Wholesalers | 11 | 0.1590397640762279 | 0.038564386400000004 |
| Furn/Home Furnishings | 53 | 0.17838756863549707 | 0.041070036799999994 |
| Green & Renewable Energy | 60 | 0.09818755287796214 | 0.041070036799999994 |
| Healthcare Products | 163 | 0.09236129171444106 | 0.042738237199999994 |
| Healthcare Support Services | 47 | 0.1394676653251132 | 0.041070036799999994 |
| Heathcare Information and Technology | 89 | 0.08261117074523742 | 0.042738237199999994 |
| Homebuilding | 36 | 0.17571761419581275 | 0.038564386400000004 |
| Hospitals/Healthcare Facilities | 29 | 0.22432513068473298 | 0.041070036799999994 |
| Hotel/Gaming | 103 | 0.16057562124923616 | 0.041070036799999994 |
| Household Products | 65 | 0.14696121639785145 | 0.041070036799999994 |
| Information Services | 6 | 0.1953176605025154 | 0.042738237199999994 |
| Insurance (General) | 34 | 0.20553273819119847 | 0.038564386400000004 |
| Insurance (Life) | 15 | 0.1877960824133032 | 0.038564386400000004 |
| Insurance (Prop/Cas.) | 19 | 0.2004071907203176 | 0.038564386400000004 |
| Investments & Asset Management | 338 | 0.0748885761255716 | 0.041070036799999994 |
| Machinery | 210 | 0.15500618529939283 | 0.041070036799999994 |
| Metals & Mining | 118 | 0.06985830048572893 | 0.042738237199999994 |
| Office Equipment & Services | 20 | 0.12320217276741821 | 0.041070036799999994 |
| Oil/Gas (Integrated) | 12 | 0.40262751929178425 | 0.038564386400000004 |
| Oil/Gas (Production and Exploration) | 83 | 0.10574433914567677 | 0.042738237199999994 |
| Oil/Gas Distribution | 30 | 0.08371846270105068 | 0.041070036799999994 |
| Oilfield Svcs/Equip. | 58 | 0.11709108017878869 | 0.041070036799999994 |
| Packaging & Container | 42 | 0.14726512030439964 | 0.041070036799999994 |
| Paper/Forest Products | 36 | 0.10405812950846544 | 0.038564386400000004 |
| Power | 69 | 0.22279979384362356 | 0.038564386400000004 |
| Precious Metals | 39 | 0.06740197061731103 | 0.042738237199999994 |
| Publishing & Newspapers | 59 | 0.13365312936339585 | 0.041070036799999994 |
| R.E.I.T. | 138 | 0.11720965405480303 | 0.038564386400000004 |
| Real Estate (Development) | 61 | 0.1468614652350962 | 0.041070036799999994 |
| Real Estate (General/Diversified) | 45 | 0.12402792078941736 | 0.041070036799999994 |
| Real Estate (Operations & Services) | 219 | 0.13367181992224025 | 0.038564386400000004 |
| Recreation | 59 | 0.15603649727837315 | 0.041070036799999994 |
| Reinsurance | 4 | 0.2376311300578875 | 0.038564386400000004 |
| Restaurant/Dining | 38 | 0.1274008528057832 | 0.041070036799999994 |
| Retail (Automotive) | 22 | 0.12419691117262724 | 0.041070036799999994 |
| Retail (Building Supply) | 26 | 0.20468591997778962 | 0.041070036799999994 |
| Retail (Distributors) | 117 | 0.16374415204935291 | 0.041070036799999994 |
| Retail (General) | 31 | 0.13462559635968163 | 0.041070036799999994 |
| Retail (Grocery and Food) | 34 | 0.23457579804843465 | 0.041070036799999994 |
| Retail (REITs) | 28 | 0.14401491625653604 | 0.038564386400000004 |
| Retail (Special Lines) | 105 | 0.14299986432292075 | 0.041070036799999994 |
| Rubber& Tires | 10 | 0.21879053839552937 | 0.038564386400000004 |
| Semiconductor | 36 | 0.06441618535102679 | 0.042738237199999994 |
| Semiconductor Equip | 21 | 0.1381043959800509 | 0.042738237199999994 |
| Shipbuilding & Marine | 65 | 0.07833382942811873 | 0.041070036799999994 |
| Shoe | 9 | 0.09962124452238692 | 0.041070036799999994 |
| Software (Entertainment) | 51 | 0.0832403530935394 | 0.042738237199999994 |
| Software (Internet) | 23 | 0.13371623250245426 | 0.042738237199999994 |
| Software (System & Application) | 290 | 0.09399500379491245 | 0.042738237199999994 |
| Steel | 57 | 0.13952150202889507 | 0.041070036799999994 |
| Telecom (Wireless) | 11 | 0.18189755401605845 | 0.038564386400000004 |
| Telecom. Equipment | 50 | 0.08983591322985801 | 0.042738237199999994 |
| Telecom. Services | 62 | 0.18243433482798455 | 0.038564386400000004 |
| Tobacco | 5 | 0.21060670608648788 | 0.038564386400000004 |
| Transportation | 56 | 0.1817380631296963 | 0.041070036799999994 |
| Transportation (Railroads) | 8 | 0.12744508912390679 | 0.038564386400000004 |
| Trucking | 7 | 0.18560715398080577 | 0.038564386400000004 |
| Utility (General) | 18 | 0.2086498691558396 | 0.038564386400000004 |
| Utility (Water) | 12 | 0.18165312472703707 | 0.041070036799999994 |
| Grand Total | 6560 | 0.13058533800800304 | 0.041070036799999994 |
| Total Market (without financials) | 5757 | 0.12968224542822265 | 0.041070036799999994 |
