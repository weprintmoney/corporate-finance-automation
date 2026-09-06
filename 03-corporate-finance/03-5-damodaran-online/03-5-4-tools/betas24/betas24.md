---
title: "Betas24"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas24.xls
---

# Betas24

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas24.xls

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

| Date updated: | 45662.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 54 | 1.2 | 0.6098 |
| Aerospace/Defense | 67 | 0.8 | 0.4341 |
| Air Transport | 24 | 0.76 | 0.5255 |
| Apparel | 37 | 0.83 | 0.4841 |
| Auto & Truck | 34 | 1.43 | 0.6646 |
| Auto Parts | 33 | 0.99 | 0.3843 |
| Bank (Money Center) | 15 | 0.53 | 0.2337 |
| Banks (Regional) | 591 | 0.48 | 0.2078 |
| Beverage (Alcoholic) | 18 | 0.51 | 0.5509 |
| Beverage (Soft) | 29 | 0.51 | 0.6427 |
| Broadcasting | 22 | 0.48 | 0.539 |
| Brokerage & Investment Banking | 30 | 0.47 | 0.399 |
| Building Materials | 39 | 1.23 | 0.3033 |
| Business & Consumer Services | 152 | 0.92 | 0.4832 |
| Cable TV | 9 | 0.5 | 0.4196 |
| Chemical (Basic) | 31 | 0.86 | 0.549 |
| Chemical (Diversified) | 4 | 0.58 | 0.2709 |
| Chemical (Specialty) | 60 | 0.79 | 0.4247 |
| Coal & Related Energy | 16 | 1.27 | 0.4805 |
| Computer Services | 63 | 1.09 | 0.5269 |
| Computers/Peripherals | 35 | 1.12 | 0.4501 |
| Construction Supplies | 46 | 1.15 | 0.4555 |
| Diversified | 21 | 1.01 | 0.5726 |
| Drugs (Biotechnology) | 535 | 1.17 | 0.6315 |
| Drugs (Pharmaceutical) | 231 | 0.98 | 0.6501 |
| Education | 29 | 0.92 | 0.5231 |
| Electrical Equipment | 101 | 1.2 | 0.6052 |
| Electronics (Consumer & Office) | 11 | 0.95 | 0.654 |
| Electronics (General) | 122 | 1.01 | 0.5014 |
| Engineering/Construction | 42 | 0.92 | 0.4576 |
| Entertainment | 96 | 0.94 | 0.6256 |
| Environmental & Waste Services | 50 | 0.82 | 0.5672 |
| Farming/Agriculture | 35 | 0.73 | 0.5104 |
| Financial Svcs. (Non-bank & Insurance) | 166 | 0.35 | 0.3957 |
| Food Processing | 77 | 0.38 | 0.4525 |
| Food Wholesalers | 14 | 0.55 | 0.3446 |
| Furn/Home Furnishings | 28 | 0.69 | 0.4093 |
| Green & Renewable Energy | 18 | 0.5 | 0.6739 |
| Healthcare Products | 218 | 0.96 | 0.5519 |
| Healthcare Support Services | 113 | 0.82 | 0.5578 |
| Heathcare Information and Technology | 116 | 1.12 | 0.5497 |
| Homebuilding | 30 | 1.38 | 0.3436 |
| Hospitals/Healthcare Facilities | 33 | 0.57 | 0.5355 |
| Hotel/Gaming | 65 | 0.95 | 0.4344 |
| Household Products | 101 | 0.83 | 0.6304 |
| Information Services | 16 | 0.8 | 0.4241 |
| Insurance (General) | 22 | 0.69 | 0.3637 |
| Insurance (Life) | 19 | 0.62 | 0.2558 |
| Insurance (Prop/Cas.) | 53 | 0.57 | 0.2914 |
| Investments & Asset Management | 231 | 0.5 | 0.2668 |
| Machinery | 109 | 0.98 | 0.4267 |
| Metals & Mining | 64 | 0.96 | 0.6103 |
| Office Equipment & Services | 14 | 0.96 | 0.3777 |
| Oil/Gas (Integrated) | 4 | 0.46 | 0.182 |
| Oil/Gas (Production and Exploration) | 147 | 0.75 | 0.4581 |
| Oil/Gas Distribution | 24 | 0.55 | 0.4258 |
| Oilfield Svcs/Equip. | 97 | 0.78 | 0.4582 |
| Packaging & Container | 22 | 0.74 | 0.2703 |
| Paper/Forest Products | 6 | 0.96 | 0.3677 |
| Power | 48 | 0.34 | 0.2644 |
| Precious Metals | 60 | 1.15 | 0.7072 |
| Publishing & Newspapers | 19 | 0.56 | 0.3281 |
| R.E.I.T. | 192 | 0.59 | 0.2572 |
| Real Estate (Development) | 15 | 0.62 | 0.478 |
| Real Estate (General/Diversified) | 11 | 0.74 | 0.4624 |
| Real Estate (Operations & Services) | 60 | 0.95 | 0.5104 |
| Recreation | 50 | 0.93 | 0.4857 |
| Reinsurance | 1 | 0.58 | 0.1814 |
| Restaurant/Dining | 62 | 0.87 | 0.4154 |
| Retail (Automotive) | 29 | 0.99 | 0.4338 |
| Retail (Building Supply) | 13 | 1.57 | 0.3394 |
| Retail (Distributors) | 66 | 0.93 | 0.4577 |
| Retail (General) | 24 | 1.03 | 0.3721 |
| Retail (Grocery and Food) | 17 | 0.47 | 0.5043 |
| Retail (REITs) | 28 | 0.69 | 0.2665 |
| Retail (Special Lines) | 98 | 1.06 | 0.5509 |
| Rubber& Tires | 3 | 0.18 | 0.4821 |
| Semiconductor | 63 | 1.46 | 0.4968 |
| Semiconductor Equip | 30 | 1.47 | 0.347 |
| Shipbuilding & Marine | 8 | 0.52 | 0.4189 |
| Shoe | 12 | 1.41 | 0.4627 |
| Software (Entertainment) | 81 | 1.18 | 0.5913 |
| Software (Internet) | 29 | 1.6 | 0.5403 |
| Software (System & Application) | 333 | 1.22 | 0.5686 |
| Steel | 27 | 0.96 | 0.3582 |
| Telecom (Wireless) | 11 | 0.59 | 0.5664 |
| Telecom. Equipment | 61 | 0.95 | 0.5385 |
| Telecom. Services | 32 | 0.52 | 0.5682 |
| Tobacco | 12 | 0.83 | 0.5533 |
| Transportation | 21 | 0.83 | 0.482 |
| Transportation (Railroads) | 4 | 0.83 | 0.2148 |
| Trucking | 24 | 0.96 | 0.3515 |
| Utility (General) | 14 | 0.25 | 0.1566 |
| Utility (Water) | 15 | 0.47 | 0.3517 |
| Total Market | 6062 | 0.82 | 0.4669 |
| Total Market (without financials) | 4935 | 0.98 | 0.5139 |

## Inputs

| Effective |
|---|
| Marginal |
