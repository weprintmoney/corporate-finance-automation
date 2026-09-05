---
title: "Evaindia"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAIndia.xls
---

# Evaindia

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAIndia.xls

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
| Advertising | 24 | -90.55900428443032 | 0.14820964828899713 |
| Aerospace/Defense | 23 | 947.2834086163342 | 0.24287900805315096 |
| Air Transport | 5 | NA | 0.1262852921075307 |
| Apparel | 386 | 1040.7660627749306 | 0.07360936171737938 |
| Auto & Truck | 19 | 10784.154709324459 | 0.0692631004213713 |
| Auto Parts | 120 | 633.1022435001349 | 0.09579816709720189 |
| Bank (Money Center) | 35 | 1079.7082685190046 | NA |
| Banks (Regional) | 6 | -47.25966922888652 | NA |
| Beverage (Alcoholic) | 22 | 123.95047877235913 | 0.13651311214320727 |
| Beverage (Soft) | 5 | 251.39672577463088 | 0.2163185965322036 |
| Broadcasting | 19 | -446.584048654945 | 0.03563962830990509 |
| Brokerage & Investment Banking | 186 | 380.9244786777212 | NA |
| Building Materials | 67 | -35.4651861782733 | 0.08510019646793546 |
| Business & Consumer Services | 75 | 206.45915823132785 | 0.10561712702197591 |
| Cable TV | 8 | -114.699056413748 | -0.012484745968063038 |
| Chemical (Basic) | 152 | 135.43555987167355 | 0.08954473994147216 |
| Chemical (Diversified) | 8 | 250.4190293922545 | 0.13079558505715383 |
| Chemical (Specialty) | 202 | 1335.4724825558267 | 0.13037062132863547 |
| Coal & Related Energy | 5 | 2250.7672820810308 | 0.33009633048959935 |
| Computer Services | 196 | 9900.423706993664 | 0.3345123803171721 |
| Computers/Peripherals | 12 | 33.9983963216473 | 0.5477327980151537 |
| Construction Supplies | 109 | -587.2987453517816 | 0.09379304721528987 |
| Diversified | 13 | 346.3395826839611 | 0.061414010147993865 |
| Drugs (Biotechnology) | 9 | -161.6375295503121 | 0.05798134897985626 |
| Drugs (Pharmaceutical) | 188 | 2732.9868983514602 | 0.15041471385272348 |
| Education | 40 | -2.4432011510614116 | 0.0793432692519242 |
| Electrical Equipment | 139 | 885.8161133340976 | 0.1414891546072528 |
| Electronics (Consumer & Office) | 9 | 136.73683473495728 | 0.3317637696637128 |
| Electronics (General) | 37 | 177.92280232696973 | 0.19709781551975863 |
| Engineering/Construction | 219 | 2455.73098849079 | 0.10941468316144158 |
| Entertainment | 66 | -126.23283354405156 | 0.05825835725770885 |
| Environmental & Waste Services | 20 | 17.420732515930396 | 0.15421666947555454 |
| Farming/Agriculture | 75 | 189.46090927976516 | 0.08736600559133556 |
| Financial Svcs. (Non-bank & Insurance) | 291 | 6363.051125546468 | NA |
| Food Processing | 220 | 659.8610850755402 | 0.14261061851282303 |
| Food Wholesalers | 41 | -4.497338703188995 | 0.05671398175123974 |
| Furn/Home Furnishings | 52 | 203.44932876057163 | 0.14522915474720355 |
| Green & Renewable Energy | 18 | -281.8512711252365 | 0.06996411773051332 |
| Healthcare Products | 19 | -36.78673351066808 | -0.28747285702314745 |
| Healthcare Support Services | 45 | 92.51546804961214 | 0.13240079179466085 |
| Heathcare Information and Technology | 25 | -3.175186626867936 | 0.17007446729357956 |
| Homebuilding | 1 | 0.27775638393069557 | -0.0002494076568150642 |
| Hospitals/Healthcare Facilities | 42 | 434.3738674394163 | 0.16441401776407463 |
| Hotel/Gaming | 80 | 285.54866553727123 | 0.1622025534837713 |
| Household Products | 43 | 1399.3028649196085 | 0.2719497172404126 |
| Information Services | 26 | -211.18372970940842 | 0.262243568284261 |
| Insurance (General) | 2 | NA | 0.020652861964320424 |
| Insurance (Life) | 9 | 4882.0940458284795 | 0.47035374472323943 |
| Insurance (Prop/Cas.) | 3 | -609.164197065509 | 0.0785039457843991 |
| Investments & Asset Management | 115 | 91.56482509064239 | 0.058427009173686 |
| Machinery | 187 | 1089.6011420681857 | 0.11683425891105738 |
| Metals & Mining | 51 | 2287.1586281746145 | 0.19719266792294884 |
| Office Equipment & Services | 20 | 29.263287878921602 | 0.16999333841962158 |
| Oil/Gas (Integrated) | 1 | 188.93005451339218 | 0.08609448124530268 |
| Oil/Gas (Production and Exploration) | 7 | 279.381012963354 | 0.09649343514465793 |
| Oil/Gas Distribution | 12 | 225.47336420847358 | 0.1435983896324984 |
| Oilfield Svcs/Equip. | 30 | 1524.6201941779193 | 0.09508811207846213 |
| Packaging & Container | 101 | 76.91385200268074 | 0.08867142805018938 |
| Paper/Forest Products | 55 | -151.97691558230633 | 0.042518722272099595 |
| Power | 33 | 564.7148216758465 | 0.08773878725008293 |
| Precious Metals | 1 | -10.038329049795706 | -0.4107438016528925 |
| Publishing & Newspapers | 25 | 4.012621584024702 | 0.07590642684276976 |
| R.E.I.T. | 5 | -55.596963740413756 | 0.08426331137473939 |
| Real Estate (Development) | 156 | -243.31616104459647 | 0.06661931777269842 |
| Real Estate (General/Diversified) | 16 | -326.1193290177717 | 0.057369005306506946 |
| Real Estate (Operations & Services) | 42 | -26.214777351119018 | 0.0449684735073011 |
| Recreation | 15 | 8.478545478254617 | 0.05964814890894304 |
| Reinsurance | 1 | -128.76898920235882 | 0.11647069990352801 |
| Restaurant/Dining | 19 | -760.0355019169783 | -0.04938080758628355 |
| Retail (Automotive) | 10 | -21.15699890909211 | 0.059368081865918354 |
| Retail (Building Supply) | 3 | -0.5362779896472102 | -0.3366457365430514 |
| Retail (Distributors) | 276 | 535.5726681571615 | 0.05944499742106318 |
| Retail (General) | 11 | -328.1984857369526 | -0.0019030326569487754 |
| Retail (Grocery and Food) | 13 | 45.77744710994319 | 0.1363868471091925 |
| Retail (REITs) | 1 | -77.12348451290269 | 0.037401390267529 |
| Retail (Special Lines) | 61 | 187.13934391394343 | 0.09984254517116335 |
| Rubber& Tires | 18 | 9.535884591418947 | 0.08496867300514514 |
| Semiconductor | 18 | 506.0865202468161 | 0.9349812357150846 |
| Semiconductor Equip | 2 | -33.20353427276048 | 0.054759150408537585 |
| Shipbuilding & Marine | 28 | 493.85072316732067 | 0.12308697855977173 |
| Shoe | 13 | 19.565344225914828 | 0.0861331799615263 |
| Software (Entertainment) | 4 | -239.02111808277877 | 0.02082269063546196 |
| Software (Internet) | 6 | -0.7396403513762801 | 0.01985853189415883 |
| Software (System & Application) | 82 | 358.09468012879427 | 0.22888554504236558 |
| Steel | 185 | -1350.9145100871983 | 0.0848013478110619 |
| Telecom (Wireless) | 4 | 15 | 0.11822389109847768 |
| Telecom. Equipment | 22 | -190.37611977317107 | 0.015260800720310407 |
| Telecom. Services | 11 | 15 | 0.17653558286412552 |
| Tobacco | 7 | 3646.233178733997 | 0.2589144276405504 |
| Transportation | 59 | 18.0110124658295 | 0.063880584073571 |
| Transportation (Railroads) | 3 | -47.07845836579981 | 0.10513687474885666 |
| Trucking | 24 | 31.177351734279195 | 0.12999729742134206 |
| Utility (General) | 0 | 15 | NA |
| Utility (Water) | 1 | 2.8458751992916604 | 0.06681151778700149 |
| Total Market | 5170 | 78109.26579748033 | 0.06681151778700149 |
| Total Market (without financials) | 4523 | 55698.43390985679 | 0.11171536768312097 |
