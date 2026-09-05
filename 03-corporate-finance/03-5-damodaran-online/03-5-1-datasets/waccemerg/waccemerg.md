---
title: "Waccemerg"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/waccemerg.xls
---

# Waccemerg

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/waccemerg.xls

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
| Expected inflation rate in local currency = |  | 10 | 0.0885 |
| Expected inflation rate in US $ = |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Tax Rate | After-tax Cost of Debt |
| Advertising | 184 | 0.10280547291382684 | 0.0496618057 |
| Aerospace/Defense | 151 | 0.10744341352537773 | 0.04798352079999999 |
| Air Transport | 79 | 0.13737163407443873 | 0.0454627234 |
| Apparel | 993 | 0.14501552802460532 | 0.04798352079999999 |
| Auto & Truck | 89 | 0.13909530553355096 | 0.04798352079999999 |
| Auto Parts | 592 | 0.16187762034804024 | 0.04798352079999999 |
| Bank (Money Center) | 455 | 0.21545502635732602 | 0.0454627234 |
| Banks (Regional) | 104 | 0.15297178584067106 | 0.0454627234 |
| Beverage (Alcoholic) | 132 | 0.19234185279974694 | 0.04798352079999999 |
| Beverage (Soft) | 40 | 0.16589059249798627 | 0.0454627234 |
| Broadcasting | 63 | 0.12380415408425828 | 0.04798352079999999 |
| Brokerage & Investment Banking | 468 | 0.14259194584175705 | 0.04798352079999999 |
| Building Materials | 281 | 0.14794934376253957 | 0.04798352079999999 |
| Business & Consumer Services | 379 | 0.12160144472550669 | 0.0496618057 |
| Cable TV | 29 | 0.091651954089193 | 0.04798352079999999 |
| Chemical (Basic) | 741 | 0.14555149551220847 | 0.04798352079999999 |
| Chemical (Diversified) | 29 | 0.2135787881271695 | 0.04798352079999999 |
| Chemical (Specialty) | 687 | 0.16010227503306423 | 0.04798352079999999 |
| Coal & Related Energy | 96 | 0.2021672555188101 | 0.04798352079999999 |
| Computer Services | 693 | 0.13778307209271917 | 0.0496618057 |
| Computers/Peripherals | 244 | 0.13390361064004702 | 0.04798352079999999 |
| Construction Supplies | 580 | 0.15293999112171255 | 0.04798352079999999 |
| Diversified | 215 | 0.15022444640659258 | 0.04798352079999999 |
| Drugs (Biotechnology) | 382 | 0.03273948797653944 | 0.0496618057 |
| Drugs (Pharmaceutical) | 753 | 0.139462978306192 | 0.04798352079999999 |
| Education | 182 | 0.11943679574326466 | 0.04798352079999999 |
| Electrical Equipment | 810 | 0.12957669804759694 | 0.04798352079999999 |
| Electronics (Consumer & Office) | 81 | 0.1357096829482956 | 0.04798352079999999 |
| Electronics (General) | 1050 | 0.11174962374051088 | 0.04798352079999999 |
| Engineering/Construction | 999 | 0.15915988846141668 | 0.04798352079999999 |
| Entertainment | 343 | 0.07968092664070184 | 0.0496618057 |
| Environmental & Waste Services | 223 | 0.12628847004049434 | 0.04798352079999999 |
| Farming/Agriculture | 312 | 0.16181016752651323 | 0.04798352079999999 |
| Financial Svcs. (Non-bank & Insurance) | 697 | 0.1708418267503516 | 0.04798352079999999 |
| Food Processing | 1030 | 0.1636050401218475 | 0.04798352079999999 |
| Food Wholesalers | 121 | 0.15168649917985652 | 0.04798352079999999 |
| Furn/Home Furnishings | 278 | 0.14485354471615688 | 0.04798352079999999 |
| Green & Renewable Energy | 154 | 0.13176448866017867 | 0.04798352079999999 |
| Healthcare Products | 380 | 0.08749210829554217 | 0.04798352079999999 |
| Healthcare Support Services | 256 | 0.1425811224228185 | 0.04798352079999999 |
| Heathcare Information and Technology | 146 | 0.08196068166789691 | 0.0496618057 |
| Homebuilding | 46 | 0.10931810416978548 | 0.04798352079999999 |
| Hospitals/Healthcare Facilities | 164 | 0.18453433988481516 | 0.04798352079999999 |
| Hotel/Gaming | 427 | 0.15629098848858092 | 0.04798352079999999 |
| Household Products | 339 | 0.1401154315073192 | 0.04798352079999999 |
| Information Services | 49 | 0.17982671816976264 | 0.04798352079999999 |
| Insurance (General) | 140 | 0.143771402158095 | 0.04798352079999999 |
| Insurance (Life) | 92 | 0.16197575803890557 | 0.04798352079999999 |
| Insurance (Prop/Cas.) | 158 | 0.19038821767318614 | 0.04798352079999999 |
| Investments & Asset Management | 486 | 0.08883564375578094 | 0.04798352079999999 |
| Machinery | 987 | 0.14078976337626004 | 0.04798352079999999 |
| Metals & Mining | 358 | 0.15138172717675286 | 0.04798352079999999 |
| Office Equipment & Services | 78 | 0.14157320924925473 | 0.04798352079999999 |
| Oil/Gas (Integrated) | 15 | 0.2349815529379119 | 0.04798352079999999 |
| Oil/Gas (Production and Exploration) | 105 | 0.1413254887700449 | 0.04798352079999999 |
| Oil/Gas Distribution | 120 | 0.1288169833383369 | 0.04798352079999999 |
| Oilfield Svcs/Equip. | 228 | 0.15581496825191818 | 0.04798352079999999 |
| Packaging & Container | 341 | 0.1607571386362981 | 0.04798352079999999 |
| Paper/Forest Products | 197 | 0.12410167871390171 | 0.04798352079999999 |
| Power | 328 | 0.17355310697192694 | 0.04798352079999999 |
| Precious Metals | 64 | 0.1592667382946683 | 0.0496618057 |
| Publishing & Newspapers | 171 | 0.11616385663228028 | 0.04798352079999999 |
| R.E.I.T. | 208 | 0.024724421385629067 | 0.0454627234 |
| Real Estate (Development) | 786 | 0.14196491031320685 | 0.04798352079999999 |
| Real Estate (General/Diversified) | 205 | 0.11885782458701509 | 0.04798352079999999 |
| Real Estate (Operations & Services) | 406 | 0.14093048713534612 | 0.04798352079999999 |
| Recreation | 158 | 0.11825836413828875 | 0.04798352079999999 |
| Reinsurance | 27 | 0.163855181133209 | 0.04798352079999999 |
| Restaurant/Dining | 184 | 0.12308434324095571 | 0.04798352079999999 |
| Retail (Automotive) | 122 | 0.16579436444622273 | 0.04798352079999999 |
| Retail (Building Supply) | 55 | 0.14474349347506207 | 0.04798352079999999 |
| Retail (Distributors) | 731 | 0.15445010170198256 | 0.04798352079999999 |
| Retail (General) | 147 | 0.1601073174673642 | 0.04798352079999999 |
| Retail (Grocery and Food) | 97 | 0.1752956230846009 | 0.04798352079999999 |
| Retail (REITs) | 39 | 0.05696677692732207 | 0.0454627234 |
| Retail (Special Lines) | 282 | 0.16115150277306628 | 0.04798352079999999 |
| Rubber& Tires | 72 | 0.17819752380378712 | 0.04798352079999999 |
| Semiconductor | 546 | 0.08645253427932258 | 0.04798352079999999 |
| Semiconductor Equip | 300 | 0.10727140531133218 | 0.0496618057 |
| Shipbuilding & Marine | 252 | 0.1584580751455054 | 0.04798352079999999 |
| Shoe | 60 | 0.1661322105956063 | 0.04798352079999999 |
| Software (Entertainment) | 67 | 0.10623008705570679 | 0.0496618057 |
| Software (Internet) | 49 | 0.12255800193212629 | 0.0496618057 |
| Software (System & Application) | 548 | 0.08205549974551207 | 0.0496618057 |
| Steel | 555 | 0.14331831227661535 | 0.04798352079999999 |
| Telecom (Wireless) | 68 | 0.19550391470592918 | 0.0454627234 |
| Telecom. Equipment | 296 | 0.08395715037819061 | 0.0496618057 |
| Telecom. Services | 142 | 0.15845441152762327 | 0.04798352079999999 |
| Tobacco | 30 | 0.22877164007187017 | 0.04798352079999999 |
| Transportation | 330 | 0.17184940522691664 | 0.04798352079999999 |
| Transportation (Railroads) | 18 | 0.2573475934694324 | 0.0454627234 |
| Trucking | 76 | 0.19168029695245878 | 0.0496618057 |
| Utility (General) | 14 | 0.16569261498887994 | 0.0454627234 |
| Utility (Water) | 76 | 0.17110687710389094 | 0.04798352079999999 |
| Total Market | 27360 | 0.13909503388757335 | 0.04798352079999999 |
| Total Market (without financials) | 24760 | 0.13722148680313695 | 0.04798352079999999 |
