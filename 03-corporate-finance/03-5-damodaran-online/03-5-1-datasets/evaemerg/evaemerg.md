---
title: "Evaemerg"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAemerg.xls
---

# Evaemerg

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAemerg.xls

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
| Advertising | 184 | -2679.6841376249904 | 0.03426961138238492 |
| Aerospace/Defense | 151 | -1706.677682219125 | 0.08072773261441124 |
| Air Transport | 79 | 2273.01599157738 | 0.06699836149108619 |
| Apparel | 993 | -138.7834316910694 | 0.07744230974355491 |
| Auto & Truck | 89 | -3105.0721920126703 | 0.060681341275769914 |
| Auto Parts | 592 | -13007.989190423848 | 0.5379728654594347 |
| Bank (Money Center) | 455 | 158866.8180794778 | NA |
| Banks (Regional) | 104 | 5645.108473849105 | NA |
| Beverage (Alcoholic) | 132 | 16816.383364099027 | 0.33214240954639807 |
| Beverage (Soft) | 40 | 3437.1269049685775 | 0.3543828058610117 |
| Broadcasting | 63 | -1068.3484098292731 | 0.030044824389812992 |
| Brokerage & Investment Banking | 468 | -6603.801876202359 | NA |
| Building Materials | 281 | -2932.5564223382994 | 0.04975850589967081 |
| Business & Consumer Services | 379 | -2706.7116013053383 | 0.06646151562126845 |
| Cable TV | 29 | -2732.7097692007633 | 0.00953524627779983 |
| Chemical (Basic) | 741 | -58731.35468228033 | 0.02732060037148034 |
| Chemical (Diversified) | 29 | 199.67754585635248 | 0.08978112614107306 |
| Chemical (Specialty) | 687 | -8494.965400490184 | 0.07260761357952508 |
| Coal & Related Energy | 96 | 3223.310309080776 | 0.14019244691116908 |
| Computer Services | 693 | 5833.42216341474 | 0.1573115056872155 |
| Computers/Peripherals | 244 | -15299.808897801298 | 0.08768506130561739 |
| Construction Supplies | 580 | -13274.14424946301 | 0.06947166229595193 |
| Diversified | 215 | -9810.123239520262 | 0.07441297359828482 |
| Drugs (Biotechnology) | 382 | -14025.688470752719 | -0.013733675488230734 |
| Drugs (Pharmaceutical) | 753 | -5554.195509115561 | 0.08559354848770255 |
| Education | 182 | 245.57028068756674 | 0.12963739170536112 |
| Electrical Equipment | 810 | -17296.8547241397 | 0.07730534283489136 |
| Electronics (Consumer & Office) | 81 | -2190.8167275845426 | 0.05991418019555462 |
| Electronics (General) | 1050 | -33977.08076409193 | 0.06320501365606697 |
| Engineering/Construction | 999 | -20378.572755231206 | 0.049470786527283005 |
| Entertainment | 343 | -2126.1184511974743 | 0.09836628932679271 |
| Environmental & Waste Services | 223 | -5009.104157170884 | 0.04133586746102994 |
| Farming/Agriculture | 312 | 573.8073385552665 | 0.07472726685764691 |
| Financial Svcs. (Non-bank & Insurance) | 697 | 22759.705515884994 | NA |
| Food Processing | 1030 | 10709.692357898246 | 0.1053634951267247 |
| Food Wholesalers | 121 | -474.6685501981133 | 0.07587335289451681 |
| Furn/Home Furnishings | 278 | 6744.346140262247 | 0.1521171374817693 |
| Green & Renewable Energy | 154 | -1928.6405388281248 | 0.05726395990806106 |
| Healthcare Products | 380 | -6353.19815173894 | 0.05038436540574592 |
| Healthcare Support Services | 256 | -5200.906244452149 | 0.06644057134943862 |
| Heathcare Information and Technology | 146 | 427.9843994030888 | 0.09060647572291868 |
| Homebuilding | 46 | 109.04029876308326 | 0.07863416628201475 |
| Hospitals/Healthcare Facilities | 164 | 1870.9525563455065 | 0.10933172660322525 |
| Hotel/Gaming | 427 | -2244.4778281807526 | 0.06695377185013884 |
| Household Products | 339 | -1383.7104749559014 | 0.1097651435515938 |
| Information Services | 49 | 21.470483313281928 | 0.2701841598090224 |
| Insurance (General) | 140 | 9515.450966642979 | 0.1951843753699382 |
| Insurance (Life) | 92 | 39145.43163680998 | 0.15123243862043984 |
| Insurance (Prop/Cas.) | 158 | 15214.650899356433 | 0.14730607318121905 |
| Investments & Asset Management | 486 | -996.8783433842193 | 0.025241519019779092 |
| Machinery | 987 | -15279.483573614525 | 0.057980818764572305 |
| Metals & Mining | 358 | -3143.1193484195237 | 0.12644414658533148 |
| Office Equipment & Services | 78 | -137.46274277183514 | 0.07371213118212984 |
| Oil/Gas (Integrated) | 15 | 57021.74457824827 | 0.19958348858011887 |
| Oil/Gas (Production and Exploration) | 105 | 13600.593790567902 | 0.16216453288198135 |
| Oil/Gas Distribution | 120 | 1384.8581356462685 | 0.07680587669203304 |
| Oilfield Svcs/Equip. | 228 | -2075.8739300261695 | 0.07810266275804666 |
| Packaging & Container | 341 | -1424.8644224015068 | 0.04430350186861644 |
| Paper/Forest Products | 197 | -6157.813722643121 | 0.026707095711559978 |
| Power | 328 | 6146.50351902395 | 0.06587938366246265 |
| Precious Metals | 64 | 4708.469294072323 | 0.17940362549549757 |
| Publishing & Newspapers | 171 | -1761.9673992626797 | 0.05812187795128821 |
| R.E.I.T. | 208 | -1081.214131200248 | 0.05823518732713834 |
| Real Estate (Development) | 786 | -125964.78399606152 | 0.01100490923423036 |
| Real Estate (General/Diversified) | 205 | -29402.292337342333 | 0.026660292351730296 |
| Real Estate (Operations & Services) | 406 | -18694.20272002782 | 0.04606276442284258 |
| Recreation | 158 | -1548.927138207782 | 0.06448651066732741 |
| Reinsurance | 27 | -448.00227779194057 | 0.09565367233710624 |
| Restaurant/Dining | 184 | -1187.3021230681777 | 0.07418406204946486 |
| Retail (Automotive) | 122 | -3356.4989332880727 | 0.0960418083253458 |
| Retail (Building Supply) | 55 | -345.06005681768954 | 0.13872094360784257 |
| Retail (Distributors) | 731 | -4158.593090590437 | 0.052200724041405897 |
| Retail (General) | 147 | -1914.7715628987958 | 0.07163361758812302 |
| Retail (Grocery and Food) | 97 | -2018.756858429614 | 0.0963590155912503 |
| Retail (REITs) | 39 | -3143.2852880005407 | 0.04965490036720698 |
| Retail (Special Lines) | 282 | -816.9432499035516 | 0.11772009136798137 |
| Rubber& Tires | 72 | -398.3363029164873 | 0.0833370293492223 |
| Semiconductor | 546 | 11426.648874208435 | 0.1621374535723031 |
| Semiconductor Equip | 300 | -15294.734586721564 | 0.03107532218540255 |
| Shipbuilding & Marine | 252 | 5550.264637678425 | 0.09951963329541148 |
| Shoe | 60 | 316.32798922896455 | 0.09629500750478395 |
| Software (Entertainment) | 67 | 9788.623391431449 | 0.1440459613012111 |
| Software (Internet) | 49 | -247.23503504438605 | 0.051014534368396536 |
| Software (System & Application) | 548 | -13417.85772947116 | 0.007113099885598981 |
| Steel | 555 | -29296.475877728444 | 0.0521993364182723 |
| Telecom (Wireless) | 68 | 9979.359299667081 | 0.10925270165168942 |
| Telecom. Equipment | 296 | -5874.281767095951 | 0.05079892801332364 |
| Telecom. Services | 142 | 6204.500886133093 | 0.09281367095060807 |
| Tobacco | 30 | 4779.206037845377 | 0.15963140719159966 |
| Transportation | 330 | -1943.741125457541 | 0.07493451244938176 |
| Transportation (Railroads) | 18 | -3126.071807613421 | 0.06782296124647945 |
| Trucking | 76 | -381.3380672261674 | 0.08902663205458909 |
| Utility (General) | 14 | 253.7640282799918 | 0.06391134874745308 |
| Utility (Water) | 76 | 408.4455985418129 | 0.05308601084243995 |
| Total Market | 27360 | -342324.92161107203 | 0.05308601084243995 |
| Total Market (without financials) | 24760 | -413626.0780918144 | 0.08124234161770888 |
