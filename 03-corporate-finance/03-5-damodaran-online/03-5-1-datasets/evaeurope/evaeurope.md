---
title: "Evaeurope"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAEurope.xls
---

# Evaeurope

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAEurope.xls

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
| Advertising | 83 | 132.78946905051555 | 0.5089609803619859 |
| Aerospace/Defense | 67 | 19180.9228563516 | 0.19764578092921203 |
| Air Transport | 33 | 11738.865413297324 | 0.13170531730204219 |
| Apparel | 109 | 17327.99624545513 | 0.21590250316259607 |
| Auto & Truck | 31 | -40488.092529752445 | 0.03672504931457592 |
| Auto Parts | 58 | -4653.127344597248 | 0.09165239472576614 |
| Bank (Money Center) | 113 | 60944.90182730304 | NA |
| Banks (Regional) | 69 | 1388.337216641009 | NA |
| Beverage (Alcoholic) | 52 | 5035.363863166118 | 0.10762103084869144 |
| Beverage (Soft) | 14 | 2388.8944235658623 | 0.17582849934494985 |
| Broadcasting | 18 | -587.8664248933433 | 0.15451257422513381 |
| Brokerage & Investment Banking | 69 | 3337.427331208146 | NA |
| Building Materials | 84 | 6888.770576953702 | 0.2196881443702467 |
| Business & Consumer Services | 176 | 5367.904447416121 | 0.2905655881061073 |
| Cable TV | 2 | -2378.259706777829 | -0.03894735401458487 |
| Chemical (Basic) | 58 | -1717.9149925813188 | 0.01863596516966062 |
| Chemical (Diversified) | 7 | -5355.308181769032 | 0.04512955865450766 |
| Chemical (Specialty) | 92 | 566.773880594108 | 0.10724746854801773 |
| Coal & Related Energy | 15 | -511.1217558589362 | 0.014664154105397266 |
| Computer Services | 210 | 8114.622488669735 | 0.3531538219536814 |
| Computers/Peripherals | 38 | -70.71842562849412 | 0.14939117548553962 |
| Construction Supplies | 119 | 21655.9709641345 | 0.10753020545514828 |
| Diversified | 72 | -6477.46487923094 | 0.06630654150731158 |
| Drugs (Biotechnology) | 199 | -3905.849774883969 | 0.033713487541740424 |
| Drugs (Pharmaceutical) | 115 | 40928.767965194136 | 0.18531129259274276 |
| Education | 18 | 315.33295051300166 | 0.1665576919229589 |
| Electrical Equipment | 146 | 9660.109251398739 | 0.28293873839610273 |
| Electronics (Consumer & Office) | 17 | -304.8919325296959 | 0.09559904242806065 |
| Electronics (General) | 142 | -513.0906086527942 | 0.12487702363576184 |
| Engineering/Construction | 160 | 12107.643523486377 | 0.16493876895728063 |
| Entertainment | 199 | -9588.111741856881 | 0.07410942241496286 |
| Environmental & Waste Services | 48 | -915.7970235786895 | 0.11646920290256818 |
| Farming/Agriculture | 46 | 582.8528435286174 | 0.05831123705283598 |
| Financial Svcs. (Non-bank & Insurance) | 146 | 17364.810432452792 | NA |
| Food Processing | 173 | 15629.762747507668 | 0.1474400022875708 |
| Food Wholesalers | 11 | -312.15538392964254 | 0.06107557552589179 |
| Furn/Home Furnishings | 53 | -1686.5665340864919 | 0.05812089864724443 |
| Green & Renewable Energy | 60 | -3347.6689727795147 | 0.05513518211053032 |
| Healthcare Products | 163 | -4987.887089421063 | 0.14216240419818352 |
| Healthcare Support Services | 47 | -594.8454954933787 | 0.12627917296894572 |
| Heathcare Information and Technology | 89 | -1722.1679211285582 | 0.1373221410509644 |
| Homebuilding | 36 | -2642.798189591817 | 0.08717950781193934 |
| Hospitals/Healthcare Facilities | 29 | -908.8674850951899 | 0.04834912106613593 |
| Hotel/Gaming | 103 | 5799.986141969503 | 0.20544454906208173 |
| Household Products | 65 | 11252.556211690806 | 0.25347801708087264 |
| Information Services | 6 | 190.89352288378868 | 0.2500282493389675 |
| Insurance (General) | 34 | 29387.67902352139 | 0.24556405806665307 |
| Insurance (Life) | 15 | 417.18002934593136 | 0.14702993544760404 |
| Insurance (Prop/Cas.) | 19 | 9283.349782443009 | 0.1695600383424429 |
| Investments & Asset Management | 338 | 10078.939717720421 | 0.07548400421667939 |
| Machinery | 210 | 6554.140914119838 | 0.18343718799038822 |
| Metals & Mining | 118 | -8750.13147345787 | 0.12199299050379689 |
| Office Equipment & Services | 20 | 2.1270731509403205 | 0.1525809129123385 |
| Oil/Gas (Integrated) | 12 | 83487.04007515956 | 0.17042975983835443 |
| Oil/Gas (Production and Exploration) | 83 | -5805.662355879081 | 0.35598919262036666 |
| Oil/Gas Distribution | 30 | 1305.7792899363067 | 0.08932040339225365 |
| Oilfield Svcs/Equip. | 58 | -3012.9170677464 | 0.11372536605883717 |
| Packaging & Container | 42 | -363.5198147856741 | 0.09609461533686932 |
| Paper/Forest Products | 36 | -2526.222341536569 | 0.04252745115632007 |
| Power | 69 | 10117.112361158903 | 0.10065075463923492 |
| Precious Metals | 39 | -72.68231403493796 | 0.1517881328561717 |
| Publishing & Newspapers | 59 | -185.98264598778937 | 0.12867078618315317 |
| R.E.I.T. | 138 | -1199.5525730370305 | 0.04019503442940416 |
| Real Estate (Development) | 61 | -554.0705369876507 | 0.03712229825108549 |
| Real Estate (General/Diversified) | 45 | -27.734162002043753 | 0.01639484941111548 |
| Real Estate (Operations & Services) | 219 | -585.0993094437388 | 0.03297858561701157 |
| Recreation | 59 | 551.3043576125391 | 0.13318706444375294 |
| Reinsurance | 4 | 8713.911846902305 | 0.2364619332833937 |
| Restaurant/Dining | 38 | 1190.0728274897808 | 0.18014488427560363 |
| Retail (Automotive) | 22 | -224.6298044541454 | 0.08674150831729856 |
| Retail (Building Supply) | 26 | -940.058359991513 | 0.09551114942956646 |
| Retail (Distributors) | 117 | 3770.3552274305375 | 0.10220846273039408 |
| Retail (General) | 31 | 9648.900975631546 | 0.06446843608910052 |
| Retail (Grocery and Food) | 34 | 1449.9766375035133 | 0.10036750868108366 |
| Retail (REITs) | 28 | 277.7221034092229 | 0.05492721632279415 |
| Retail (Special Lines) | 105 | 4901.247710260996 | 0.2114346552961282 |
| Rubber& Tires | 10 | -939.5664597351665 | 0.08538486676799882 |
| Semiconductor | 36 | -1852.5805937086354 | 0.09518969932873782 |
| Semiconductor Equip | 21 | 8233.677259155937 | 0.32701957294659717 |
| Shipbuilding & Marine | 65 | 3118.1896255534366 | 0.09770143621958068 |
| Shoe | 9 | -465.130720883327 | 0.13145552857657716 |
| Software (Entertainment) | 51 | 436.5939278774596 | 0.23375338340182578 |
| Software (Internet) | 23 | 115.81449326236954 | 0.19177028103667848 |
| Software (System & Application) | 290 | 5129.292812072486 | 0.23184579015259307 |
| Steel | 57 | -7370.898060205646 | 0.020526101860812947 |
| Telecom (Wireless) | 11 | -8871.84793697619 | 0.06282995755833184 |
| Telecom. Equipment | 50 | 522.5298503444772 | 0.08347514127911092 |
| Telecom. Services | 62 | 4658.646809756341 | 0.09897652669181198 |
| Tobacco | 5 | 3531.7853484890065 | 0.1291009658666117 |
| Transportation | 56 | -963.0483528511943 | 0.08185603692375731 |
| Transportation (Railroads) | 8 | -572.2160482448567 | 0.013510514893708442 |
| Trucking | 7 | 26.75428056965034 | 0.08647951719775196 |
| Utility (General) | 18 | 7188.6864431210115 | 0.1253877324593472 |
| Utility (Water) | 12 | 276.9840296172057 | 0.08098877180569838 |
| Grand Total | 6560 | 348553.2824591466 | 0.08098877180569838 |
| Total Market (without financials) | 5757 | 201471.63944489762 | 0.13009897846450405 |
