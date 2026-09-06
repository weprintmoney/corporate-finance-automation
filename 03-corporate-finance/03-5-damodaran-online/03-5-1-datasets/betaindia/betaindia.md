---
title: "Betaindia"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaIndia.xls
---

# Betaindia

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaIndia.xls

Sheets: Explanation & FAQs, Industry Averages, Input Choices

## Explanation & FAQs

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

| Date updated: | 46027.0 |
|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |
| What is this data? | Beta, Unlevered beta and other risk measures |
| Home Page: | http://www.damodaran.com |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |
| If marginal tax rate, enter the marginal tax rate to use |  |
| Industry Name | Number of firms |
| Advertising | 24 |
| Aerospace/Defense | 23 |
| Air Transport | 5 |
| Apparel | 386 |
| Auto & Truck | 19 |
| Auto Parts | 120 |
| Bank (Money Center) | 35 |
| Banks (Regional) | 6 |
| Beverage (Alcoholic) | 22 |
| Beverage (Soft) | 5 |
| Broadcasting | 19 |
| Brokerage & Investment Banking | 186 |
| Building Materials | 67 |
| Business & Consumer Services | 75 |
| Cable TV | 8 |
| Chemical (Basic) | 152 |
| Chemical (Diversified) | 8 |
| Chemical (Specialty) | 202 |
| Coal & Related Energy | 5 |
| Computer Services | 196 |
| Computers/Peripherals | 12 |
| Construction Supplies | 109 |
| Diversified | 13 |
| Drugs (Biotechnology) | 9 |
| Drugs (Pharmaceutical) | 188 |
| Education | 40 |
| Electrical Equipment | 139 |
| Electronics (Consumer & Office) | 9 |
| Electronics (General) | 37 |
| Engineering/Construction | 219 |
| Entertainment | 66 |
| Environmental & Waste Services | 20 |
| Farming/Agriculture | 75 |
| Financial Svcs. (Non-bank & Insurance) | 291 |
| Food Processing | 220 |
| Food Wholesalers | 41 |
| Furn/Home Furnishings | 52 |
| Green & Renewable Energy | 18 |
| Healthcare Products | 19 |
| Healthcare Support Services | 45 |
| Heathcare Information and Technology | 25 |
| Homebuilding | 1 |
| Hospitals/Healthcare Facilities | 42 |
| Hotel/Gaming | 80 |
| Household Products | 43 |
| Information Services | 26 |
| Insurance (General) | 2 |
| Insurance (Life) | 9 |
| Insurance (Prop/Cas.) | 3 |
| Investments & Asset Management | 115 |
| Machinery | 187 |
| Metals & Mining | 51 |
| Office Equipment & Services | 20 |
| Oil/Gas (Integrated) | 1 |
| Oil/Gas (Production and Exploration) | 7 |
| Oil/Gas Distribution | 12 |
| Oilfield Svcs/Equip. | 30 |
| Packaging & Container | 101 |
| Paper/Forest Products | 55 |
| Power | 33 |
| Precious Metals | 1 |
| Publishing & Newspapers | 25 |
| R.E.I.T. | 5 |
| Real Estate (Development) | 156 |
| Real Estate (General/Diversified) | 16 |
| Real Estate (Operations & Services) | 42 |
| Recreation | 15 |
| Reinsurance | 1 |
| Restaurant/Dining | 19 |
| Retail (Automotive) | 10 |
| Retail (Building Supply) | 3 |
| Retail (Distributors) | 276 |
| Retail (General) | 11 |
| Retail (Grocery and Food) | 13 |
| Retail (REITs) | 1 |
| Retail (Special Lines) | 61 |
| Rubber& Tires | 18 |
| Semiconductor | 18 |
| Semiconductor Equip | 2 |
| Shipbuilding & Marine | 28 |
| Shoe | 13 |
| Software (Entertainment) | 4 |
| Software (Internet) | 6 |
| Software (System & Application) | 82 |
| Steel | 185 |
| Telecom (Wireless) | 4 |
| Telecom. Equipment | 22 |
| Telecom. Services | 11 |
| Tobacco | 7 |
| Transportation | 59 |
| Transportation (Railroads) | 3 |
| Trucking | 24 |
| Utility (General) | 0 |
| Utility (Water) | 1 |
| Total Market | 5170 |
| Total Market (without financials) | 4523 |

## Input Choices

| Effective |
|---|
| Marginal |
