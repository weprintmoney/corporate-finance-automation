---
title: "Evajapan"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAJapan.xls
---

# Evajapan

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAJapan.xls

Sheets: Variables & FAQ, Industry Averages

## Variables & FAQ

| End Game | To estimate how much firms earn on their investments, relative to what they need to earn to break even, given the risk. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Average regression beta across companies in the group. |
| ROE | Aggregated Net Income , across all firms in group, using trailing 12 month data/ Aggregated Book Value of equity, across all firms in group, using most recent balance sheet. |
| Cost of Equity | Risk free Rate + Beta * Equity Risk Premium  |
| (ROE - COE) | ROE - Cost of Equity, across the sector |
| BV of Equity | Aggregated Book Value of Equity, in most recent balance sheet, across all firms in the group (in milliona of dollars) |
| Equity EVA | (ROE - Cost of Equity)* BV of Equity, defined as above, and aggregated across companies (in $ millions) |
| ROC | Aggregated Operating income , across all firms in group, using trailing 12 month data (1- Effective Tax Rate)/ (BV of Equity + BV of Debt - Cash), across all firms in group, using most recent balance sheet. |
| Cost of Capital | Cost of Equity * (Equity/ (Debt + Equity)) + Cost of Debt (1- Marginal tax rate) *(Debt/ (Debt + Equity)), with aggregated debt and market equity values across all companies in the sector, using most recent balance sheet for debt and most recent year-end for equity. |
| (ROC - Cost of Capital) | ROC- Cost of Capital, averaged across the sector |
| BV of Capital | (Book Value of Equity + BV of Debt - Cash), aggregated across all firms in the group, in most recent balance sheet. |
| EVA | (ROC - Cost of Capital)* BV of Capital, defined as above, and aggregated across companies (in $ millions) |

## Industry Averages

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | The choice of how much to return to shareholders in a business and in what form (dividends or buybacks) is one that every business has to make, and this datasets includes statistics on cash return. |
| What is this data? | Excess Returns (equity and firm) in percent and (millions of) dollar terms |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| To update this spreadsheet, enter the following |  |  |  |
| Long Term Treasury bond rate = |  |  |  |
| Risk Premium to Use for Equity = |  |  |  |
| Country Default Spread to use for debt = |  |  |  |
|  |  |  |  |
| Do you want to use the marginal tax rate? |  |  |  |
| Marginal tax rate = |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Equity EVA | ROC |
| Advertising | 87 | -2571.877361646236 | 0.25324449857358466 |
| Aerospace/Defense | 5 | -201.7652471440496 | -0.26878649754171674 |
| Air Transport | 5 | 567.6355163101559 | 0.1040060524841285 |
| Apparel | 60 | -454.7891390018932 | 0.054883632877074415 |
| Auto & Truck | 10 | -13633.70725184289 | 0.04392071537147119 |
| Auto Parts | 98 | -4885.406635770011 | 0.07597634289822501 |
| Bank (Money Center) | 7 | -21882.29420398822 | NA |
| Banks (Regional) | 76 | -9344.116920735903 | NA |
| Beverage (Alcoholic) | 7 | -195.70103911769192 | 0.04628313546848054 |
| Beverage (Soft) | 6 | -207.07850981940885 | 0.057302010131089036 |
| Broadcasting | 11 | -1151.5986800203914 | 0.02382609512451947 |
| Brokerage & Investment Banking | 39 | 287.3276671265893 | NA |
| Building Materials | 56 | -979.0231877880952 | 0.07723567444749664 |
| Business & Consumer Services | 224 | 2478.3543232825045 | 0.23301162190610428 |
| Cable TV | 1 | -55.795381705708316 | 0.07302043459084626 |
| Chemical (Basic) | 65 | -4317.511472720735 | 0.04769220210996623 |
| Chemical (Diversified) | 22 | -2167.380558616639 | 0.07186614311147375 |
| Chemical (Specialty) | 69 | -797.1140990771883 | 0.11017650948148155 |
| Coal & Related Energy | 1 | -130.74042486560916 | -0.05412624122223017 |
| Computer Services | 240 | 3124.7924480737297 | 0.15097409495174022 |
| Computers/Peripherals | 24 | -3099.216476152942 | 0.08324432401309136 |
| Construction Supplies | 51 | -2302.039668558621 | 0.06566711606215524 |
| Diversified | 16 | 1782.1254278499616 | 0.11762467948013149 |
| Drugs (Biotechnology) | 33 | -771.0123497120748 | -0.13762862211423255 |
| Drugs (Pharmaceutical) | 40 | -1154.480956740883 | 0.09320966548358155 |
| Education | 35 | 42.63360413743174 | 0.16192865177718624 |
| Electrical Equipment | 53 | -706.3369812422153 | 0.08173466645394982 |
| Electronics (Consumer & Office) | 10 | 12.795891737831578 | 0.07962724624405414 |
| Electronics (General) | 132 | -5623.491475601278 | 0.08101909901457145 |
| Engineering/Construction | 153 | 2077.6756895021754 | 0.08355223679287208 |
| Entertainment | 74 | 1878.3098544242835 | 0.1570624437039577 |
| Environmental & Waste Services | 38 | 229.6327915756401 | 0.1306807146370006 |
| Farming/Agriculture | 11 | -278.52729725437285 | 0.0418317341347663 |
| Financial Svcs. (Non-bank & Insurance) | 50 | 9278.323289798322 | NA |
| Food Processing | 118 | 1108.5864655677121 | 0.07106260713569056 |
| Food Wholesalers | 34 | 38.58933135385434 | 0.07020607770132224 |
| Furn/Home Furnishings | 19 | -141.71086136665323 | 0.06934165458575495 |
| Green & Renewable Energy | 6 | -78.7659090636546 | 0.07135116855070943 |
| Healthcare Products | 39 | 844.084858927498 | 0.12231598615147951 |
| Healthcare Support Services | 48 | -347.5964444462947 | 0.08311827831546309 |
| Heathcare Information and Technology | 35 | -36.711703697874384 | 0.21722089271468895 |
| Homebuilding | 45 | 797.0296321557045 | 0.04580530676965348 |
| Hospitals/Healthcare Facilities | 11 | -22.00724577494525 | 0.05020379450182249 |
| Hotel/Gaming | 35 | 289.0871179024615 | 0.076655453209155 |
| Household Products | 42 | -458.78248154741726 | 0.09110819728966833 |
| Information Services | 13 | 38.74992579377559 | 0.15183568495793184 |
| Insurance (General) | 6 | 97.09646071802138 | 0.909480709868891 |
| Insurance (Life) | 5 | -6134.368120562466 | 0.09147765583367765 |
| Insurance (Prop/Cas.) | 6 | 4351.028735115386 | 0.24074958806865357 |
| Investments & Asset Management | 14 | -37.320585799424755 | 0.11107198346532587 |
| Machinery | 221 | -2226.2843145731294 | 0.07662868706032985 |
| Metals & Mining | 21 | -2070.543223393718 | 0.0331424008850063 |
| Office Equipment & Services | 27 | 130.319190730973 | 0.09948153540264563 |
| Oil/Gas (Integrated) | 0 | 15 | NA |
| Oil/Gas (Production and Exploration) | 2 | 934.5596332066076 | 0.11823523206875935 |
| Oil/Gas Distribution | 3 | 9.360982767366623 | 0.04639978236831015 |
| Oilfield Svcs/Equip. | 19 | -936.7196597145429 | 0.04276944501381109 |
| Packaging & Container | 28 | -223.9848808119283 | 0.04720548030879757 |
| Paper/Forest Products | 15 | -1192.4876042240019 | 0.019663824087679548 |
| Power | 26 | -3116.078618630193 | 0.03951855103132855 |
| Precious Metals | 2 | 40.362018138165595 | 0.07089644569730241 |
| Publishing & Newspapers | 51 | -396.7322159503733 | 0.057199364125853316 |
| R.E.I.T. | 54 | -24.547074991604656 | 0.03976347290573506 |
| Real Estate (Development) | 20 | 144.78404829382532 | 0.06701612582708756 |
| Real Estate (General/Diversified) | 48 | 1485.2864947684186 | 0.04722588679058256 |
| Real Estate (Operations & Services) | 42 | 425.04235993340353 | 0.08289812300156109 |
| Recreation | 52 | 361.24344799285996 | 0.11098284571548801 |
| Reinsurance | 0 | 15 | NA |
| Restaurant/Dining | 107 | 490.7510638215349 | 0.12849751085830424 |
| Retail (Automotive) | 23 | 235.13670981319305 | 0.11444577294919196 |
| Retail (Building Supply) | 17 | -50.69098248594451 | 0.04795989040611685 |
| Retail (Distributors) | 139 | 7307.760657284322 | 0.04022014839350649 |
| Retail (General) | 42 | -1353.7077203907547 | 0.07537125989092885 |
| Retail (Grocery and Food) | 55 | -61.37203864141252 | 0.07224457849736014 |
| Retail (REITs) | 4 | 26.713259782538902 | 0.03772084015969675 |
| Retail (Special Lines) | 131 | 2602.36716251193 | 0.14962798094197408 |
| Rubber& Tires | 6 | -1884.6060015880394 | 0.0857647489032961 |
| Semiconductor | 21 | -4123.774248198328 | 0.0971950270650189 |
| Semiconductor Equip | 37 | 2205.330023717674 | 0.2406955657210107 |
| Shipbuilding & Marine | 26 | 1056.8870854518868 | 0.034193072841306585 |
| Shoe | 3 | 382.38924755658735 | 0.4324515086803739 |
| Software (Entertainment) | 76 | -625.3250701821803 | 0.18574238639775842 |
| Software (Internet) | 26 | 33.8809962713517 | 0.2291995191006783 |
| Software (System & Application) | 185 | 389.06366075255966 | 0.40745294097224044 |
| Steel | 40 | -6571.106292651399 | 0.04147697826130536 |
| Telecom (Wireless) | 8 | 15125.70315463244 | 0.0682781202992389 |
| Telecom. Equipment | 13 | -79.49801584762227 | 0.06101280354459612 |
| Telecom. Services | 20 | 735.940766403043 | 0.07005700746497007 |
| Tobacco | 1 | 1769.367552311171 | 0.35072653484036864 |
| Transportation | 31 | -178.5985219932161 | 0.05352896944580059 |
| Transportation (Railroads) | 21 | 4544.957453145324 | 0.049971584176892486 |
| Trucking | 17 | -165.9948497643432 | 0.0481188758869964 |
| Utility (General) | 0 | 15 | NA |
| Utility (Water) | 0 | 0 | 0.05329851203484457 |
| Total Market | 3965 |  | 0.05329851203484457 |
| Total Market (without financials) | 3762 |  | 0.06735445883192072 |
