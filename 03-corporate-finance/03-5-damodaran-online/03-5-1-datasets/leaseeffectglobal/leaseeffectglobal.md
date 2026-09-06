---
title: "Leaseeffectglobal"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/leaseeffectGlobal.xls
---

# Leaseeffectglobal

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/leaseeffectGlobal.xls

Sheets: Variables & FAQ, Industry Averages

## Variables & FAQ

| End Game | To estimate what effect treating leases as debt has on key operating and financial numbers. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Lease Expenses | Operating lease expenses, as reported in income statement, aggregated across firms in group, from trailing 12-month financials |
| Lease Debt (my estimates) | PV of lease commitments over time, discounted back at pre-tax cost of debt for the firm, aggregated across firms in group, from most recent financial statements. |
| Lease Debt (Accounting) | IFRS & GAAP required companies to convert lease commitments to debt in 2019, using rules more complex than mine. Aggregated value of accounting lease debt, across all firms in the group. |
| Total Debt without leases | All interest bearing debt, aggregated across firms in group, from most recent financial statements. |
| Total Debt with lease debt | Total debt without leases + lease debt, aggregated across firms in group, from most recent financial statements. |
| Market Debt to Capital, without leases | Total debt without leases / (Total debt without leases + Market Cap), aggregated across firms in group, from most recent financial statements for all items except market cap, on last day of most recent year. |
| Market Debt to Capital, with leases | (Total debt without leases + lease debt)/ (Total debt without leases + lease debt+ Market Cap), aggregated across firms in group, from most recent financial statements for all items except market cap, on last day of most recent year. |
| Operating Income (before lease adjustment) | Earnings before interest and taxes, aggregated across firms in group, using most recent trailing 12 month statements. |
| Operating Income (after lease adjustment) | (Earnings before interest and taxes+ Operating lease expense - Depreciation on leased asset), aggregated across firms in group, using most recent trailing 12 month statements. |
| ROIC, before lease adjustment | Aggregated Operating income , across all firms in group, using trailing 12 month data (1- Effective Tax Rate)/ (BV of Equity + BV of Debt - Cash), across all firms in group, using most recent balance sheet. |
| ROIC, after lease adjustment | Aggregated Operating income after lease adjustment , across all firms in group, using trailing 12 month data (1- Effective Tax Rate)/ (BV of Equity + BV of Debt - Cash), across all firms in group, using most recent balance sheet. |

## Industry Averages

| Date updated: | 46027.0 | In 2019, accounting rules changed to require that leases be treated as debt. Since my rules are still a little different, I am reporting the difference in this column. |
|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  |
| What is this data? | Lease capitalization effect on earnings, capital and profitability measures |  |
| Home Page: | http://www.damodaran.com |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |
| Industry Name | Number of firms | Lease Debt (My Estimate) |
| Advertising | 419 | 4588.642248365184 |
| Aerospace/Defense | 319 | 13790.53315238998 |
| Air Transport | 150 | 38528.50090102223 |
| Apparel | 1207 | 14777.094985704636 |
| Auto & Truck | 165 | 10287.731068718014 |
| Auto Parts | 797 | 5800.961912820261 |
| Bank (Money Center) | 604 | 37806.74605135247 |
| Banks (Regional) | 825 | 14501.112377785612 |
| Beverage (Alcoholic) | 217 | 1188.3818805796036 |
| Beverage (Soft) | 94 | 6313.599729310052 |
| Broadcasting | 127 | 5166.5912008112355 |
| Brokerage & Investment Banking | 623 | 15149.847007533535 |
| Building Materials | 469 | 6990.446548308508 |
| Business & Consumer Services | 994 | 15749.136239398387 |
| Cable TV | 42 | 13083.520484807086 |
| Chemical (Basic) | 909 | 5228.386623359867 |
| Chemical (Diversified) | 63 | 701.0687481093046 |
| Chemical (Specialty) | 952 | 9261.159587957198 |
| Coal & Related Energy | 212 | 147.49114889636985 |
| Computer Services | 1225 | 12021.638836343598 |
| Computers/Peripherals | 343 | 19183.565661732515 |
| Construction Supplies | 804 | 6300.992894346127 |
| Diversified | 329 | 9730.61247769976 |
| Drugs (Biotechnology) | 1193 | 14464.918051084562 |
| Drugs (Pharmaceutical) | 1260 | 9952.813127885805 |
| Education | 281 | 4861.188951767865 |
| Electrical Equipment | 1158 | 6616.0196565146325 |
| Electronics (Consumer & Office) | 122 | 271.87711662552465 |
| Electronics (General) | 1481 | 6227.804358562105 |
| Engineering/Construction | 1390 | 5573.089281661902 |
| Entertainment | 733 | 22831.908634169697 |
| Environmental & Waste Services | 397 | 3170.695997266652 |
| Farming/Agriculture | 428 | 3987.120343254239 |
| Financial Svcs. (Non-bank & Insurance) | 1138 | 17356.629628572613 |
| Food Processing | 1450 | 8320.230277560651 |
| Food Wholesalers | 183 | 4982.933392870633 |
| Furn/Home Furnishings | 383 | 5540.000110959154 |
| Green & Renewable Energy | 258 | 834.6278752025682 |
| Healthcare Products | 842 | 9938.795499328407 |
| Healthcare Support Services | 478 | 36527.24727618159 |
| Heathcare Information and Technology | 430 | 7963.453797342867 |
| Homebuilding | 160 | 16267.685631812652 |
| Hospitals/Healthcare Facilities | 249 | 18414.83312451956 |
| Hotel/Gaming | 656 | 62114.37507945363 |
| Household Products | 588 | 7367.400673510681 |
| Information Services | 86 | 2207.657746131248 |
| Insurance (General) | 204 | 4401.320800937712 |
| Insurance (Life) | 143 | 2894.7987890536897 |
| Insurance (Prop/Cas.) | 248 | 7092.032481944014 |
| Investments & Asset Management | 1315 | 11581.809695286443 |
| Machinery | 1553 | 6172.822312596545 |
| Metals & Mining | 1874 | 2734.3089940232458 |
| Office Equipment & Services | 139 | 1098.7116829203023 |
| Oil/Gas (Integrated) | 34 | 15874.092802773928 |
| Oil/Gas (Production and Exploration) | 539 | 9553.009884714556 |
| Oil/Gas Distribution | 186 | 5782.962855472695 |
| Oilfield Svcs/Equip. | 431 | 13110.624757780344 |
| Packaging & Container | 438 | 5329.099923493428 |
| Paper/Forest Products | 271 | 356.84574696375057 |
| Power | 486 | 14417.611769635696 |
| Precious Metals | 777 | 207.580874029416 |
| Publishing & Newspapers | 307 | 2169.285356335691 |
| R.E.I.T. | 643 | 49887.196939799935 |
| Real Estate (Development) | 895 | 884.4321273064706 |
| Real Estate (General/Diversified) | 312 | 26873.3717984088 |
| Real Estate (Operations & Services) | 752 | 9858.261584791937 |
| Recreation | 332 | 12135.06817585665 |
| Reinsurance | 32 | 337.48737671005074 |
| Restaurant/Dining | 410 | 58107.29979979104 |
| Retail (Automotive) | 212 | 19435.056658039975 |
| Retail (Building Supply) | 121 | 22161.145848041444 |
| Retail (Distributors) | 1079 | 13216.49994785036 |
| Retail (General) | 252 | 139740.11596638744 |
| Retail (Grocery and Food) | 215 | 23327.110689095105 |
| Retail (REITs) | 113 | 2968.328261534625 |
| Retail (Special Lines) | 649 | 59459.90141218036 |
| Rubber& Tires | 91 | 1026.395443057787 |
| Semiconductor | 675 | 9650.72084714449 |
| Semiconductor Equip | 391 | 2414.087954522416 |
| Shipbuilding & Marine | 359 | 6384.178577357321 |
| Shoe | 84 | 3764.357146820439 |
| Software (Entertainment) | 298 | 36735.92210351094 |
| Software (Internet) | 150 | 6501.015515585852 |
| Software (System & Application) | 1532 | 49631.353843792574 |
| Steel | 719 | 2133.214368344634 |
| Telecom (Wireless) | 101 | 30938.740622162586 |
| Telecom. Equipment | 437 | 3472.9220821007766 |
| Telecom. Services | 283 | 48681.47335965419 |
| Tobacco | 48 | 702.8342834761715 |
| Transportation | 451 | 37230.720410537906 |
| Transportation (Railroads) | 54 | 6713.929233186238 |
| Trucking | 130 | 4345.752282258305 |
| Utility (General) | 52 | 3468.220966314897 |
| Utility (Water) | 106 | 176.593124215462 |
| Total Market | 48156 | 1337231.6948771477 |
| Total Market (without financials) | 43056 | 1226447.398044683 |
