---
title: "Betajapan22"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan22.xls
---

# Betajapan22

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan22.xls

Sheets: Variables & FAQ, Industry Averages, Input Choices

## Variables & FAQ

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

| Date updated: | 44931.0 | YouTube Video explaining estimation choices and process. |
|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  |
| What is this data? | Beta, Unlevered beta and other risk measures |  |
| Home Page: | http://www.damodaran.com |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash |
| Advertising | 71 | 1.5698767818675012 |
| Aerospace/Defense | 2 | 0.6263311444210655 |
| Air Transport | 6 | 0.6533911651319158 |
| Apparel | 61 | 0.8396995578145652 |
| Auto & Truck | 10 | 1.0062462339975926 |
| Auto Parts | 104 | 1.293169708993909 |
| Bank (Money Center) | 6 | -0.8138544984809313 |
| Banks (Regional) | 78 | -0.3594548407795059 |
| Beverage (Alcoholic) | 6 | 0.44670253167858837 |
| Beverage (Soft) | 7 | 0.44525068613743196 |
| Broadcasting | 11 | 0.6177313747808834 |
| Brokerage & Investment Banking | 35 | 0.15905714116075975 |
| Building Materials | 63 | 0.8287963052062822 |
| Business & Consumer Services | 205 | 1.5012329077867166 |
| Cable TV | 1 | 0.4563194042756045 |
| Chemical (Basic) | 69 | 0.8797959851133984 |
| Chemical (Diversified) | 22 | 0.815705590980323 |
| Chemical (Specialty) | 73 | 1.1939287285932805 |
| Coal & Related Energy | 1 | 0.41663375932818647 |
| Computer Services | 227 | 1.2685278011840706 |
| Computers/Peripherals | 26 | 1.2456675308104714 |
| Construction Supplies | 52 | 0.855417122961975 |
| Diversified | 15 | 0.5692875161433639 |
| Drugs (Biotechnology) | 28 | 1.6006172787410775 |
| Drugs (Pharmaceutical) | 41 | 0.8443951589959421 |
| Education | 32 | 0.8648877203733255 |
| Electrical Equipment | 57 | 1.3284968905268526 |
| Electronics (Consumer & Office) | 10 | 1.2622274808434997 |
| Electronics (General) | 139 | 1.5455621770242072 |
| Engineering/Construction | 156 | 0.8015358459785709 |
| Entertainment | 72 | 1.3431882348542379 |
| Environmental & Waste Services | 35 | 1.2262826980915613 |
| Farming/Agriculture | 11 | 0.5492470298217005 |
| Financial Svcs. (Non-bank & Insurance) | 37 | 0.08638794502637416 |
| Food Processing | 120 | 0.37090264477367385 |
| Food Wholesalers | 36 | 0.5281394302261693 |
| Furn/Home Furnishings | 21 | 1.2502483569968281 |
| Green & Renewable Energy | 9 | 1.2410230042609667 |
| Healthcare Products | 39 | 1.065929021881723 |
| Healthcare Support Services | 45 | 1.2133160252463937 |
| Heathcare Information and Technology | 35 | 1.5195322219779541 |
| Homebuilding | 51 | 0.718005961981939 |
| Hospitals/Healthcare Facilities | 9 | 1.2799468656566302 |
| Hotel/Gaming | 29 | 0.675946202990337 |
| Household Products | 43 | 0.9221904367922275 |
| Information Services | 25 | 1.5898929013959664 |
| Insurance (General) | 5 | 1.5909821163140185 |
| Insurance (Life) | 5 | -0.5060576218069279 |
| Insurance (Prop/Cas.) | 6 | 1.9287538498906691 |
| Investments & Asset Management | 13 | 1.5032501332498966 |
| Machinery | 229 | 1.1713046517222756 |
| Metals & Mining | 21 | 1.0041316852722606 |
| Office Equipment & Services | 27 | 0.8611869180714553 |
| Oil/Gas (Integrated) | 0 | NA |
| Oil/Gas (Production and Exploration) | 2 | 0.7780461794244761 |
| Oil/Gas Distribution | 3 | 0.535314232147782 |
| Oilfield Svcs/Equip. | 19 | 0.3271941567170767 |
| Packaging & Container | 31 | 0.6426055680326487 |
| Paper/Forest Products | 16 | 0.33070794781030566 |
| Power | 25 | 0.09725651614727139 |
| Precious Metals | 2 | 0.6452551297981901 |
| Publishing & Newspapers | 51 | 1.004121427527183 |
| R.E.I.T. | 61 | 0.5384142635609598 |
| Real Estate (Development) | 16 | 0.6582971674255469 |
| Real Estate (General/Diversified) | 55 | 0.4330800101480902 |
| Real Estate (Operations & Services) | 42 | 0.5174423935815009 |
| Recreation | 50 | 1.1201627965660474 |
| Reinsurance | 0 | NA |
| Restaurant/Dining | 107 | 0.5851569449409679 |
| Retail (Automotive) | 27 | 0.8012627942043925 |
| Retail (Building Supply) | 16 | 0.6243436208159576 |
| Retail (Distributors) | 145 | 0.5168013186063733 |
| Retail (General) | 28 | 0.49658663091355254 |
| Retail (Grocery and Food) | 50 | 0.45523824327270496 |
| Retail (Online) | 64 | 1.7028975138663767 |
| Retail (Special Lines) | 108 | 0.8251005358043574 |
| Rubber& Tires | 7 | 1.0261539588648372 |
| Semiconductor | 20 | 2.2428596354734283 |
| Semiconductor Equip | 35 | 2.6556906399359224 |
| Shipbuilding & Marine | 29 | 0.8158742362447601 |
| Shoe | 3 | 0.8516560298284236 |
| Software (Entertainment) | 68 | 1.5783584984544132 |
| Software (Internet) | 25 | 1.8048052538531463 |
| Software (System & Application) | 172 | 1.7756136290343063 |
| Steel | 44 | 0.7476352565745601 |
| Telecom (Wireless) | 7 | 0.8044132364823993 |
| Telecom. Equipment | 16 | 1.9907558682254234 |
| Telecom. Services | 19 | 0.9678570238164715 |
| Tobacco | 1 | 0.5974051598925538 |
| Transportation | 18 | 0.8120281053009143 |
| Transportation (Railroads) | 20 | 0.129889194451012 |
| Trucking | 35 | 0.5241743136831295 |
| Utility (General) | 0 | NA |
| Utility (Water) | 0 | NA |
| Total Market | 3974 | 0.9143839155036615 |
| Total Market (without financials) | 3789 | 0.8791369241144318 |

## Input Choices

| Effective |
|---|
| Marginal |
