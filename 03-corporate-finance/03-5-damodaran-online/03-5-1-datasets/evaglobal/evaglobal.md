---
title: "Evaglobal"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/EVAGlobal.xls
---

# Evaglobal

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/EVAGlobal.xls

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

| Date updated: | 45662.0 | YouTube Video explaining estimation choices and process. | Notes |
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
| Advertising | 419 | -6456.264328938017 | 0.1793365767118328 |
| Aerospace/Defense | 319 | 25831.51770724513 | 0.1546266528982992 |
| Air Transport | 150 | 18088.128804672182 | 0.09013467295800828 |
| Apparel | 1207 | 20096.12578695431 | 0.16066581496248522 |
| Auto & Truck | 165 | -74729.39531196521 | 0.043290711847986524 |
| Auto Parts | 797 | -25478.02373179681 | 0.12916441167961604 |
| Bank (Money Center) | 604 | 325568.651680279 | NA |
| Banks (Regional) | 825 | 23301.71962152689 | NA |
| Beverage (Alcoholic) | 217 | 19718.854346578173 | 0.15417973283933217 |
| Beverage (Soft) | 94 | 23695.468506208643 | 0.25367508689543017 |
| Broadcasting | 127 | -4460.529882737323 | 0.09505074643010343 |
| Brokerage & Investment Banking | 623 | 25390.025161320962 | NA |
| Building Materials | 469 | 6190.655720628256 | 0.14189101363837847 |
| Business & Consumer Services | 994 | 15644.718545951435 | 0.22092321087225542 |
| Cable TV | 42 | -3327.2071942181983 | 0.11149964694609382 |
| Chemical (Basic) | 909 | -69017.30289105498 | 0.031507248495430164 |
| Chemical (Diversified) | 63 | -7985.502559674412 | 0.06387008533010807 |
| Chemical (Specialty) | 952 | -19943.900764376507 | 0.09511963803857178 |
| Coal & Related Energy | 212 | 646.5622998864785 | 0.1415339475997465 |
| Computer Services | 1225 | 25180.78039221342 | 0.20955305758952805 |
| Computers/Peripherals | 343 | 95145.26174187456 | 0.19910185025773558 |
| Construction Supplies | 804 | 21505.24288372003 | 0.09292383137761633 |
| Diversified | 329 | 8716.600622282807 | 0.08984867749422655 |
| Drugs (Biotechnology) | 1193 | -48962.799986416954 | 0.02994251473785985 |
| Drugs (Pharmaceutical) | 1260 | 75937.45114406984 | 0.1473728320717214 |
| Education | 281 | 1945.2501733167492 | 0.14361683059114613 |
| Electrical Equipment | 1158 | -12637.653839458004 | 0.11449613160913091 |
| Electronics (Consumer & Office) | 122 | -1559.964023561359 | 0.08067930496038599 |
| Electronics (General) | 1481 | -30498.30583400139 | 0.08238339577137488 |
| Engineering/Construction | 1390 | 6340.931915981 | 0.07191370425530605 |
| Entertainment | 733 | -16198.806351527732 | 0.11040823320939556 |
| Environmental & Waste Services | 397 | 0.48743647508888244 | 0.10410726284517295 |
| Farming/Agriculture | 428 | 4468.775226382263 | 0.06778885085649826 |
| Financial Svcs. (Non-bank & Insurance) | 1138 | 147606.94790461936 | NA |
| Food Processing | 1450 | 21445.590701644476 | 0.11973510077420262 |
| Food Wholesalers | 183 | 841.3964148715254 | 0.10674987618913893 |
| Furn/Home Furnishings | 383 | 4999.310932625482 | 0.12607849884713523 |
| Green & Renewable Energy | 258 | -7157.664762078848 | 0.0548972040319626 |
| Healthcare Products | 842 | -8530.812996520694 | 0.1370039723966101 |
| Healthcare Support Services | 478 | -3100.763194598909 | 0.20715330775726026 |
| Heathcare Information and Technology | 430 | -9328.982213073943 | 0.12540078363727983 |
| Homebuilding | 160 | 4198.30099640836 | 0.10363608542706 |
| Hospitals/Healthcare Facilities | 249 | 9399.197094007466 | 0.13209802635759535 |
| Hotel/Gaming | 656 | 24549.049559789622 | 0.11804602744851275 |
| Household Products | 588 | 26261.664844141087 | 0.23080676138017858 |
| Information Services | 86 | 1611.1413546211752 | 0.22813484005297627 |
| Insurance (General) | 204 | 46665.05474749558 | 0.25623976617078165 |
| Insurance (Life) | 143 | 51961.073231367845 | 0.14482008583497807 |
| Insurance (Prop/Cas.) | 248 | 73205.53302902935 | 0.18054615244201797 |
| Investments & Asset Management | 1315 | 24091.152570038914 | 0.08295566505053059 |
| Machinery | 1553 | -4544.692034050925 | 0.11835120000818343 |
| Metals & Mining | 1874 | -12040.167370047238 | 0.13657806342663706 |
| Office Equipment & Services | 139 | 114.8881783934264 | 0.12615897165864376 |
| Oil/Gas (Integrated) | 34 | 83591.01617144648 | 0.1387668708403002 |
| Oil/Gas (Production and Exploration) | 539 | 20195.46623376038 | 0.14869475920730077 |
| Oil/Gas Distribution | 186 | 14130.932322032284 | 0.09191073674979025 |
| Oilfield Svcs/Equip. | 431 | -6480.760507450275 | 0.09059300961038078 |
| Packaging & Container | 438 | 524.2623410366892 | 0.09283256980080849 |
| Paper/Forest Products | 271 | -12013.150355147225 | 0.02912813212669578 |
| Power | 486 | 37175.724052640115 | 0.07017650626025004 |
| Precious Metals | 777 | 13317.270445290413 | 0.2153013873373777 |
| Publishing & Newspapers | 307 | -1334.2729098413652 | 0.09322190614455993 |
| R.E.I.T. | 643 | -18354.08292414511 | 0.03662333496456642 |
| Real Estate (Development) | 895 | -118491.78523321853 | 0.012077386763519887 |
| Real Estate (General/Diversified) | 312 | -24075.276930816348 | 0.03590291574504025 |
| Real Estate (Operations & Services) | 752 | -20134.962859948722 | 0.04194610209003494 |
| Recreation | 332 | -5493.369608277693 | 0.09530290658247441 |
| Reinsurance | 32 | 9094.759937506451 | 0.17454384807953413 |
| Restaurant/Dining | 410 | 19080.070188990136 | 0.14183906093505005 |
| Retail (Automotive) | 212 | 4201.802425447943 | 0.10474129181968908 |
| Retail (Building Supply) | 121 | 21465.61334791973 | 0.23141477875102603 |
| Retail (Distributors) | 1079 | 17021.977975720558 | 0.07256195383239139 |
| Retail (General) | 252 | 80650.65995916237 | 0.11723450186313795 |
| Retail (Grocery and Food) | 215 | 5075.5833894169555 | 0.10077396955084775 |
| Retail (REITs) | 113 | -3765.803807314182 | 0.0508836109745845 |
| Retail (Special Lines) | 649 | 18389.462903835854 | 0.17001609417625824 |
| Rubber& Tires | 91 | -4203.043976787668 | 0.08276265626723926 |
| Semiconductor | 675 | 96683.35599444895 | 0.2053635878609724 |
| Semiconductor Equip | 391 | 8289.762818811156 | 0.17156324390987804 |
| Shipbuilding & Marine | 359 | 11962.398353383138 | 0.08841408706345948 |
| Shoe | 84 | 2451.9242001310186 | 0.1529177894508127 |
| Software (Entertainment) | 298 | 144409.24466304985 | 0.22833611523325711 |
| Software (Internet) | 150 | -2952.9677742633785 | 0.05780212413228354 |
| Software (System & Application) | 1532 | 90302.87979317024 | 0.2372451641796658 |
| Steel | 719 | -44233.12037860295 | 0.050947063518873376 |
| Telecom (Wireless) | 101 | 30793.218076852594 | 0.09293603514650267 |
| Telecom. Equipment | 437 | 4754.805734200189 | 0.12728086404035685 |
| Telecom. Services | 283 | 42178.361846081934 | 0.0987270863692802 |
| Tobacco | 48 | 27158.89658041577 | 0.24167133409961422 |
| Transportation | 451 | 16640.460553387893 | 0.086620383576458 |
| Transportation (Railroads) | 54 | 13062.76839699459 | 0.0778672810557345 |
| Trucking | 130 | -981.4755752290274 | 0.08435475076105046 |
| Utility (General) | 52 | 14991.460649685687 | 0.0799133728230514 |
| Utility (Water) | 106 | 3590.4626951790706 | 0.06738830206060704 |
| Total Market | 48156 | 1063723.8462395763 | 0.06738830206060704 |
| Total Market (without financials) | 43056 | 554236.8344674952 | 0.10623042736930534 |
