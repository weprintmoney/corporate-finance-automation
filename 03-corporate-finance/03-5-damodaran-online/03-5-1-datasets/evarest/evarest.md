---
title: "Evarest"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVARest.xls
---

# Evarest

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVARest.xls

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
| Advertising | 13 | -71.69144525763828 | 0.08469996431775256 |
| Aerospace/Defense | 17 | 505.1451828321395 | 0.11291639720792614 |
| Air Transport | 10 | 1091.6710483213883 | 0.10048483652919052 |
| Apparel | 10 | 1808.375175144949 | 0.32624435535578417 |
| Auto & Truck | 2 | 15 | -0.36139929172668694 |
| Auto Parts | 14 | -348.1602192856585 | 0.08852810693776876 |
| Bank (Money Center) | 14 | 29160.456577425495 | NA |
| Banks (Regional) | 8 | -485.0155616975813 | NA |
| Beverage (Alcoholic) | 12 | 112.26960394878779 | 0.10997026344189398 |
| Beverage (Soft) | 7 | 15 | -0.548299863002136 |
| Broadcasting | 11 | -259.4015416587794 | 0.085966269653636 |
| Brokerage & Investment Banking | 15 | -220.59526290844136 | NA |
| Building Materials | 7 | -361.3522999164295 | 0.06073609110692376 |
| Business & Consumer Services | 60 | 2195.4711113723706 | 0.14400765427358866 |
| Cable TV | 1 | -0.375349446538065 | 0.09352331606217616 |
| Chemical (Basic) | 16 | -225.06821594486928 | 0.13522055424496934 |
| Chemical (Diversified) | 1 | -266.88783371823337 | 0.09854547812978748 |
| Chemical (Specialty) | 45 | -534.3022446185099 | 0.10031965437237086 |
| Coal & Related Energy | 84 | -1068.286781130686 | 0.06484564875955888 |
| Computer Services | 18 | 753.7372097043624 | 0.8805813883931098 |
| Computers/Peripherals | 1 | -2.1537779048083894 | -0.9911212058641337 |
| Construction Supplies | 14 | -634.104461821031 | -0.046052494900565774 |
| Diversified | 6 | -151.11905249898396 | 0.07903946728676652 |
| Drugs (Biotechnology) | 83 | 241.3932389715961 | 0.10264298951079744 |
| Drugs (Pharmaceutical) | 124 | -3472.0682476274533 | 0.08601738354794 |
| Education | 14 | 42.52734881054776 | 0.1423513720609856 |
| Electrical Equipment | 37 | -217.7534381769406 | -0.10073715975303056 |
| Electronics (Consumer & Office) | 6 | -8.12811733087633 | -0.18426604192755533 |
| Electronics (General) | 43 | 274.8374800074459 | 0.23465469115781 |
| Engineering/Construction | 30 | 2472.3672493185813 | 0.2716858954246205 |
| Entertainment | 25 | -185.90318330052668 | 0.0642736288423882 |
| Environmental & Waste Services | 35 | 2183.746822611701 | 0.10495042772667576 |
| Farming/Agriculture | 24 | -24.17933484877781 | 0.08575341921709959 |
| Financial Svcs. (Non-bank & Insurance) | 69 | 1036.4813078749353 | NA |
| Food Processing | 51 | -300.82799504778745 | 0.10536632823931699 |
| Food Wholesalers | 4 | 1.0912604790469265 | 0.09461560705558494 |
| Furn/Home Furnishings | 6 | -153.21491538193231 | 0.05647596937006403 |
| Green & Renewable Energy | 23 | -1271.4397748270083 | 0.01802969084681335 |
| Healthcare Products | 56 | -847.0993538115241 | 0.06503151176411046 |
| Healthcare Support Services | 23 | -45.66716515390428 | 0.21295949413779214 |
| Heathcare Information and Technology | 45 | -374.30390182679133 | -0.10282950211777833 |
| Homebuilding | 3 | 4.626213419928785 | 0.1959691025892885 |
| Hospitals/Healthcare Facilities | 14 | -500.95696858467085 | 0.04832304457740605 |
| Hotel/Gaming | 28 | 494.59096826852374 | 0.1818697668458433 |
| Household Products | 32 | -106.3272294194794 | 0.038779898462628325 |
| Information Services | 3 | 483.3297277497304 | 0.30478998878070673 |
| Insurance (General) | 3 | 176.25505847574328 | 0.5820193706325949 |
| Insurance (Life) | 11 | 6853.688447152878 | 0.2022625530766283 |
| Insurance (Prop/Cas.) | 8 | 7906.707272042413 | 0.18748946413011958 |
| Investments & Asset Management | 194 | -2689.691863018221 | 0.0774217122276125 |
| Machinery | 30 | -133.86379198610692 | 0.06314544606994585 |
| Metals & Mining | 1304 | -5854.532526998106 | 0.1278342229290086 |
| Office Equipment & Services | 0 | 15 | NA |
| Oil/Gas (Integrated) | 4 | 1887.0806104174533 | 0.12514200217782764 |
| Oil/Gas (Production and Exploration) | 207 | 2200.9901797713746 | 0.09492464431196689 |
| Oil/Gas Distribution | 10 | 3509.003503694554 | 0.07012703773710215 |
| Oilfield Svcs/Equip. | 29 | -505.7873644255939 | 0.0715280128889107 |
| Packaging & Container | 8 | 851.2053302311507 | 0.11769978187054816 |
| Paper/Forest Products | 17 | -1974.5542762834268 | -0.017851932167253393 |
| Power | 17 | 1973.7547550803424 | 0.07026565339477804 |
| Precious Metals | 616 | 4290.125230619932 | 0.2192203011934386 |
| Publishing & Newspapers | 7 | -26.023966645284748 | 0.08901485482420578 |
| R.E.I.T. | 53 | -3491.546314749732 | 0.04456488168882421 |
| Real Estate (Development) | 14 | -124.83357742692948 | 0.04238292302539325 |
| Real Estate (General/Diversified) | 2 | 16.259509253771796 | 0.07275459556245517 |
| Real Estate (Operations & Services) | 31 | 181.4796375192011 | 0.08151559637058033 |
| Recreation | 14 | -118.59397154598821 | 0.10201439084076665 |
| Reinsurance | 0 | 15 | NA |
| Restaurant/Dining | 17 | 986.6990340364241 | 0.12295459373685472 |
| Retail (Automotive) | 11 | 63.48238780120809 | 0.08558372706231679 |
| Retail (Building Supply) | 9 | 134.04687270625683 | 0.13648903385089198 |
| Retail (Distributors) | 30 | 777.1963320674907 | 0.1243513639483446 |
| Retail (General) | 9 | 2558.73188120809 | 0.14614985128582805 |
| Retail (Grocery and Food) | 14 | 5522.6146789753675 | 0.14685336080439343 |
| Retail (REITs) | 16 | 240.2609205555366 | 0.049602741236112476 |
| Retail (Special Lines) | 37 | 694.8972293624104 | 0.19372377206695726 |
| Rubber& Tires | 0 | 15 | NA |
| Semiconductor | 6 | -372.7088841991381 | -0.004706797105632701 |
| Semiconductor Equip | 2 | -7.496149121244813 | -0.7309753483386924 |
| Shipbuilding & Marine | 8 | 32.197785486762086 | 0.053620130795071975 |
| Shoe | 1 | 15 | NA |
| Software (Entertainment) | 27 | 166.1152372506748 | 0.23832221337542608 |
| Software (Internet) | 23 | 270.50901006020774 | 0.09857386265224018 |
| Software (System & Application) | 200 | -802.5082990820515 | 0.0898605572399292 |
| Steel | 48 | 146.94602915946794 | 0.14055120963767306 |
| Telecom (Wireless) | 2 | 4384.368813682674 | 0.11375726988049117 |
| Telecom. Equipment | 21 | -104.37114651715734 | -0.012734232040508293 |
| Telecom. Services | 20 | 4422.524958849657 | 0.09455029596187717 |
| Tobacco | 2 | -5.381744758950554 | -0.5250332567420486 |
| Transportation | 15 | 52.05180774212291 | 0.15946232630991544 |
| Transportation (Railroads) | 3 | 3027.531097434946 | 0.10184457929419521 |
| Trucking | 4 | 96.05725757111307 | 0.11301300259186443 |
| Utility (General) | 6 | -148.42513863089113 | 0.04693104860280775 |
| Utility (Water) | 4 | 6.666893465556386 | 0.05862377450350449 |
| Total Market | 4278 | 50590.37054039366 | 0.05862377450350449 |
| Total Market (without financials) | 3956 | 16742.410094012466 | 0.11232685703370611 |
