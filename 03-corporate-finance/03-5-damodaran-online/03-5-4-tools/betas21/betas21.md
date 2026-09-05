---
title: "Betas21"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas21.xls
---

# Betas21

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas21.xls

Sheets: Explanations & FAQ, Industry Averages, Inputs

## Explanations & FAQ

| End Game | To estimate pure play betas by business, to use in estimating a bottom up beta for a project or a company. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Simple average across firms of each firm's  beta, taken as a weighted average of 2-year and 5-year weekly return regression betas, with 2-year betas weighted 2/3rds. If the company has only a 2-year beta, it is used. |
| D/E Ratio | Total debt, including lease debt/ Market Value of equity. I aggregate each number across the firms and then compute the aggregate debt to equity ratio. |
| Effective Tax Rate | Effective tax rate in the most recxent 12 months. |
| Unlevered Beta | Beta/ (1+ (1-tax rate) (D/E)). You can use either a marginal or effective tax rate as your option.  |
| Cash/Firm Value | Cash & Marketable Securities/ (Market Value of Equity + Total Debt, including lease debt. Aggregated across companies first ans then computed. |
| Unlevered Beta corrected for cash | Unlevered Beta/ (1- Cash/Firm Vaue). Cash has a beta of zero. With this calculation, I remove its effect to get a pure play beta. |
| HiLo Risk | Simple average of (High Price for year - Low Price/ (High Price + Low Price). It is a non-parametric and simple measure of price risk. |
| Standard deviation (equity) | Simple average across firms of each firm's standard deviation in stock prices in the prior 2 years, using weekly returns. |
| Standard deviation (operating income) | Simple average across firms of each firm's coefficient of variation in annual operating income over prior 10 years. (Coefficient of variation is standard deviation divided by average operating income over the period) |

## Industry Averages

| Date updated: | 44566.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 49 | 1.1018246898142943 | 0.6674472450289618 |
| Aerospace/Defense | 73 | 1.1104126718043248 | 0.4764780183920944 |
| Air Transport | 21 | 0.914138227895993 | 0.40198517329938127 |
| Apparel | 39 | 1.098346042881063 | 0.4895537395731435 |
| Auto & Truck | 26 | 1.0207658043192696 | 0.5955187086769643 |
| Auto Parts | 38 | 1.212594354633614 | 0.47586592101058767 |
| Bank (Money Center) | 7 | 1.0325147457583626 | 0.23805163793632148 |
| Banks (Regional) | 563 | 0.8412738920935885 | 0.20781748108618892 |
| Beverage (Alcoholic) | 21 | 0.7205248116424126 | 0.5568082819015002 |
| Beverage (Soft) | 32 | 1.1155473334942059 | 0.7179128426779466 |
| Broadcasting | 28 | 0.8112721237191215 | 0.5395030202552843 |
| Brokerage & Investment Banking | 31 | 0.6700703117819938 | 0.43933437348183185 |
| Building Materials | 44 | 1.0871499229138373 | 0.3600431703478159 |
| Business & Consumer Services | 160 | 0.9861131480384713 | 0.5195941296143437 |
| Cable TV | 11 | 0.6641386109632104 | 0.35614072065750196 |
| Chemical (Basic) | 35 | 0.9371284252203465 | 0.5277032853206369 |
| Chemical (Diversified) | 4 | 1.2079101125783385 | 0.37810473921221055 |
| Chemical (Specialty) | 81 | 0.997722954089115 | 0.48651286496753743 |
| Coal & Related Energy | 18 | 0.819710873327334 | 0.6619787643786641 |
| Computer Services | 83 | 1.0576213168025859 | 0.6098021344241484 |
| Computers/Peripherals | 46 | 1.2487708944175273 | 0.5469695860233573 |
| Construction Supplies | 48 | 0.9796485993062782 | 0.4089972387345105 |
| Diversified | 22 | 0.7021414621539441 | 0.5903861849967659 |
| Drugs (Biotechnology) | 581 | 0.9722328956942816 | 0.5861657240908675 |
| Drugs (Pharmaceutical) | 298 | 1.009823573553889 | 0.6576745356041518 |
| Education | 35 | 1.1033169078612295 | 0.5553905386228393 |
| Electrical Equipment | 104 | 1.194327330306878 | 0.630487987364063 |
| Electronics (Consumer & Office) | 16 | 1.0571596798644427 | 0.6272257368882509 |
| Electronics (General) | 137 | 1.051017267647953 | 0.5047318729041381 |
| Engineering/Construction | 48 | 0.9739625248634707 | 0.44923194970855257 |
| Entertainment | 108 | 0.9642484762875171 | 0.7100365714214518 |
| Environmental & Waste Services | 58 | 1.086182979964372 | 0.6177812988504343 |
| Farming/Agriculture | 36 | 0.8478652069247063 | 0.5642031165943422 |
| Financial Svcs. (Non-bank & Insurance) | 223 | 0.15175874715602064 | 0.34058795346988685 |
| Food Processing | 92 | 0.632413845750539 | 0.46683132899069646 |
| Food Wholesalers | 15 | 1.083475210571128 | 0.47134528499207506 |
| Furn/Home Furnishings | 32 | 0.9930686395536672 | 0.5168483348033172 |
| Green & Renewable Energy | 20 | 1.0952567764169068 | 0.7017467308735823 |
| Healthcare Products | 244 | 0.9123800188457021 | 0.5192486681989812 |
| Healthcare Support Services | 131 | 0.9498469507729029 | 0.5515302625823566 |
| Heathcare Information and Technology | 142 | 0.9088883028884132 | 0.5359635025679124 |
| Homebuilding | 29 | 1.5855573182596445 | 0.3840555672080827 |
| Hospitals/Healthcare Facilities | 31 | 0.9635819983948228 | 0.513963095137634 |
| Hotel/Gaming | 66 | 1.437433727843527 | 0.4651605873737294 |
| Household Products | 118 | 0.9200717469168898 | 0.6420880448825892 |
| Information Services | 79 | 1.2038667851126352 | 0.48452567406310687 |
| Insurance (General) | 23 | 0.8109091333395879 | 0.42670289082149376 |
| Insurance (Life) | 24 | 0.8829882032543376 | 0.3053267592089763 |
| Insurance (Prop/Cas.) | 52 | 0.7847772659651794 | 0.2997735379153266 |
| Investments & Asset Management | 687 | 0.9651176049094974 | 0.14692275554444698 |
| Machinery | 111 | 1.1782642967693542 | 0.4395207674370492 |
| Metals & Mining | 74 | 1.1279972137776122 | 0.6911871427223195 |
| Office Equipment & Services | 18 | 1.111467824035779 | 0.43882734692456504 |
| Oil/Gas (Integrated) | 4 | 1.250926196365303 | 0.36409774385768773 |
| Oil/Gas (Production and Exploration) | 183 | 1.1279889221313977 | 0.6708266994898238 |
| Oil/Gas Distribution | 21 | 0.8645108713214169 | 0.4074180030414814 |
| Oilfield Svcs/Equip. | 100 | 1.1791731857829815 | 0.5518340786738065 |
| Packaging & Container | 26 | 0.7782958213072473 | 0.3512298122961101 |
| Paper/Forest Products | 11 | 0.9984958405826988 | 0.4605276893807168 |
| Power | 50 | 0.5574641631069509 | 0.23815154632540472 |
| Precious Metals | 76 | 0.9873774941222514 | 0.748974645921416 |
| Publishing & Newspapers | 21 | 1.4642640113348089 | 0.453649959637092 |
| R.E.I.T. | 238 | 0.9882216516797577 | 0.25159601052840963 |
| Real Estate (Development) | 19 | 0.7424411801966027 | 0.6845099775987435 |
| Real Estate (General/Diversified) | 10 | 0.8332663411468256 | 0.5514989443861749 |
| Real Estate (Operations & Services) | 51 | 0.8711247503573315 | 0.5357935251013637 |
| Recreation | 60 | 1.073632586741868 | 0.5374849432368253 |
| Reinsurance | 2 | 1.2950268765575916 | 0.1555859364708569 |
| Restaurant/Dining | 70 | 1.332165894153193 | 0.4678402871178342 |
| Retail (Automotive) | 32 | 1.1214912603915739 | 0.4984016493848443 |
| Retail (Building Supply) | 16 | 1.4189632481805372 | 0.4446716429344519 |
| Retail (Distributors) | 68 | 1.064511615250408 | 0.5123429633527051 |
| Retail (General) | 16 | 1.0383563104796276 | 0.3913758636279854 |
| Retail (Grocery and Food) | 15 | 0.21200696239163366 | 0.4080484472453502 |
| Retail (Online) | 60 | 1.0650034437346438 | 0.5581885922530956 |
| Retail (Special Lines) | 76 | 1.2289647113509314 | 0.47965111991063697 |
| Rubber& Tires | 2 | 0.5892129358333806 | 0.5601984467997072 |
| Semiconductor | 67 | 1.135821074309048 | 0.45878518181136346 |
| Semiconductor Equip | 34 | 1.3414180698068143 | 0.42864259882115985 |
| Shipbuilding & Marine | 8 | 0.8023174759642652 | 0.5240402350738513 |
| Shoe | 12 | 1.1884916532310223 | 0.45068730168330445 |
| Software (Entertainment) | 88 | 1.2075498828617475 | 0.6990944265293993 |
| Software (Internet) | 36 | 0.9750638036621639 | 0.6075214153522857 |
| Software (System & Application) | 375 | 1.122454939608095 | 0.5566372736661396 |
| Steel | 28 | 0.9825569980735249 | 0.44237106776765395 |
| Telecom (Wireless) | 17 | 0.6272301130782924 | 0.6037424017973926 |
| Telecom. Equipment | 82 | 1.0568634798545709 | 0.550187702398038 |
| Telecom. Services | 42 | 0.509153351164839 | 0.597585530436032 |
| Tobacco | 16 | 0.8622490848413021 | 0.6631958280621588 |
| Transportation | 17 | 0.715814769679072 | 0.47307010176658615 |
| Transportation (Railroads) | 4 | 0.647608223077268 | 0.35371684110317164 |
| Trucking | 34 | 1.2784881792172302 | 0.4574419743294526 |
| Utility (General) | 16 | 0.5962187862572423 | 0.1395428307557692 |
| Utility (Water) | 14 | 0.6141799524382789 | 0.3151878356416157 |
| Total Market | 7229 | 0.9093805676301691 | 0.4658854037077978 |
| Total Market (without financials) | 5619 | 1.0402068170288452 | 0.5385266658025143 |

## Inputs

| Effective |
|---|
| Marginal |
