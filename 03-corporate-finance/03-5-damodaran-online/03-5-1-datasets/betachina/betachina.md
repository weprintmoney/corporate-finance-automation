---
title: "Betachina"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaChina.xls
---

# Betachina

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaChina.xls

Sheets: Explanations and FAQs, Industry Averages, Inputs

## Explanations and FAQs

| End Game | To estimate pure play betas by business, to use in estimating a bottom up beta for a project or a company. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Simple average across firms of each firm's  beta, taken as a weighted average of 2-year and 5-year weekly return regression betas, with 2-year betas weighted 2/3rds. If the company has only a 2-year beta, it is used. |
| D/E Ratio | Total debt, including lease debt/ Market Value of equity. I aggregate each number across the firms and then compute the aggregate debt to equity ratio. |
| Effective Tax Rate | Effective tax rate in the most recxent 12 months. |
| Unlevered Beta | Beta/ (1+ (1-tax rate) (D/E)). You can use either a marginal or effective tax rate as your option.  |
| Cash/Firm Value | Cash & Marketable Securities/ (Market Value of Equity + Total Debt, including lease debt. Aggregated across companies first ans then computed. |
| Unlevered Beta corrected for cash | Unlevered Beta/ (1- Cash/Firm Vaue). Cash has a beta of zero. With this calculation, I remove its effect to get a pure play beta. |
| HiLo Risk | Simple average of (High Price for year - Low Price/ (High Price + Low Price). It is a non-parametric and simple measure of price risk. |
| Standard deviation (equity) | Simple average across firms of each firm's standard deviation in stock prices in the prior 2 years, using weekly returns. |
| Standard deviation (operating income) | Simple average across firms of each firm's coefficient of variation in annual operating income over prior 10 years. (Coefficient of variation is standard deviation divided by average operating income over the period) |

## Industry Averages

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. |
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
| Advertising | 60 | 1.4000661175235607 |
| Aerospace/Defense | 68 | 1.5698718397569889 |
| Air Transport | 15 | 0.752649114900625 |
| Apparel | 128 | 1.3569666144776278 |
| Auto & Truck | 34 | 2.0305856749092435 |
| Auto Parts | 220 | 2.1525149336867315 |
| Bank (Money Center) | 21 | 0.3357112551482426 |
| Banks (Regional) | 37 | 0.121573155840596 |
| Beverage (Alcoholic) | 39 | 1.6924833590447343 |
| Beverage (Soft) | 3 | 1.4113117571774196 |
| Broadcasting | 4 | 1.642283063562469 |
| Brokerage & Investment Banking | 59 | 0.9361327195078682 |
| Building Materials | 62 | 1.6826833327285406 |
| Business & Consumer Services | 91 | 1.8944224495539 |
| Cable TV | 11 | 2.1608721974389162 |
| Chemical (Basic) | 290 | 1.5297022229560384 |
| Chemical (Diversified) | 5 | 1.3018585926127664 |
| Chemical (Specialty) | 244 | 1.655187766408501 |
| Coal & Related Energy | 29 | 1.2421053566567142 |
| Computer Services | 116 | 1.9612518126103575 |
| Computers/Peripherals | 55 | 2.0483927589357744 |
| Construction Supplies | 152 | 1.54238914743245 |
| Diversified | 7 | 1.150706501649751 |
| Drugs (Biotechnology) | 140 | 1.7406389377598261 |
| Drugs (Pharmaceutical) | 246 | 1.5012915899222663 |
| Education | 44 | 1.2402912457774085 |
| Electrical Equipment | 344 | 1.898316879261006 |
| Electronics (Consumer & Office) | 24 | 1.9456351169313135 |
| Electronics (General) | 404 | 2.1463669093133277 |
| Engineering/Construction | 135 | 0.7115956370373508 |
| Entertainment | 88 | 1.902882579455232 |
| Environmental & Waste Services | 105 | 1.1374259850194464 |
| Farming/Agriculture | 43 | 1.108697277886931 |
| Financial Svcs. (Non-bank & Insurance) | 33 | 1.3317799640433707 |
| Food Processing | 167 | 1.1246643794604212 |
| Food Wholesalers | 1 | 15 |
| Furn/Home Furnishings | 85 | 1.885067238858892 |
| Green & Renewable Energy | 32 | 0.6731445336484392 |
| Healthcare Products | 138 | 1.8161288656585155 |
| Healthcare Support Services | 57 | 1.1276024115836363 |
| Heathcare Information and Technology | 54 | 2.206184047489409 |
| Homebuilding | 2 | 1.6510170651721026 |
| Hospitals/Healthcare Facilities | 21 | 1.4054399371620574 |
| Hotel/Gaming | 28 | 1.1631988095230148 |
| Household Products | 72 | 1.5006696592436355 |
| Information Services | 2 | 2.4048662349625323 |
| Insurance (General) | 9 | 1.4628785900437173 |
| Insurance (Life) | 4 | 1.563732049493789 |
| Insurance (Prop/Cas.) | 2 | 0.8280856082443533 |
| Investments & Asset Management | 13 | 0.2081043666490333 |
| Machinery | 422 | 2.022843073735425 |
| Metals & Mining | 125 | 1.9364320711727887 |
| Office Equipment & Services | 12 | 1.3258198696440546 |
| Oil/Gas (Integrated) | 4 | 1.1226455494956387 |
| Oil/Gas (Production and Exploration) | 5 | 0.7919382592459625 |
| Oil/Gas Distribution | 14 | 0.6758952130460208 |
| Oilfield Svcs/Equip. | 51 | 1.288773283002912 |
| Packaging & Container | 57 | 1.5162207205602045 |
| Paper/Forest Products | 37 | 1.207405846621647 |
| Power | 82 | 0.5778559729560471 |
| Precious Metals | 15 | 1.525538519801077 |
| Publishing & Newspapers | 39 | 1.909588444117326 |
| R.E.I.T. | 2 | 15 |
| Real Estate (Development) | 126 | 0.5724750049031126 |
| Real Estate (General/Diversified) | 24 | 1.1293548987270041 |
| Real Estate (Operations & Services) | 71 | 1.7027542924049217 |
| Recreation | 46 | 1.6719183325105644 |
| Reinsurance | 1 | 1.206680647285657 |
| Restaurant/Dining | 21 | 1.6139374769542716 |
| Retail (Automotive) | 23 | 1.2585448125004217 |
| Retail (Building Supply) | 3 | 0.4142024099304305 |
| Retail (Distributors) | 72 | 1.2534888520914769 |
| Retail (General) | 48 | 1.0489658935952493 |
| Retail (Grocery and Food) | 22 | 1.7161544998700602 |
| Retail (REITs) | 0 | 15 |
| Retail (Special Lines) | 45 | 1.5794737129131535 |
| Rubber& Tires | 16 | 1.2521624792984578 |
| Semiconductor | 178 | 1.8588667115553779 |
| Semiconductor Equip | 65 | 1.7948202659896397 |
| Shipbuilding & Marine | 39 | 1.0255958503875637 |
| Shoe | 10 | 1.3834849459390823 |
| Software (Entertainment) | 27 | 1.6662336348831999 |
| Software (Internet) | 20 | 1.9538234767891685 |
| Software (System & Application) | 181 | 2.3204073498469575 |
| Steel | 101 | 1.3677889862815615 |
| Telecom (Wireless) | 6 | 1.7836534491874396 |
| Telecom. Equipment | 111 | 1.9278897010592793 |
| Telecom. Services | 9 | 1.666093709693449 |
| Tobacco | 2 | 1.3699523078684184 |
| Transportation | 79 | 1.1647643099763558 |
| Transportation (Railroads) | 9 | 0.9122098494505128 |
| Trucking | 9 | 1.2994544921632607 |
| Utility (General) | 3 | 0.9156224706868527 |
| Utility (Water) | 32 | 0.6588372196236818 |
| Total Market | 6307 | 1.2833333276326973 |
| Total Market (without financials) | 6129 | 1.5919827133124613 |

## Inputs

| Effective |
|---|
| Marginal |
