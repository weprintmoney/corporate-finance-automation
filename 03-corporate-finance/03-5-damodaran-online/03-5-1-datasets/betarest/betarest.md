---
title: "Betarest"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaRest.xls
---

# Betarest

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/betaRest.xls

Sheets: Explanations & FAQ, Industry Averages, Input Choices

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
| Advertising | 13 | 0.515368198921896 |
| Aerospace/Defense | 17 | 1.2381757961060393 |
| Air Transport | 10 | 0.6991837310519168 |
| Apparel | 10 | 0.7984679532874505 |
| Auto & Truck | 2 | 5.357698333106964 |
| Auto Parts | 14 | 0.7910966334104541 |
| Bank (Money Center) | 14 | 0.3898903721501957 |
| Banks (Regional) | 8 | 0.19820036884964723 |
| Beverage (Alcoholic) | 12 | 0.2510247728455301 |
| Beverage (Soft) | 7 | 0.9074321679101244 |
| Broadcasting | 11 | 0.447132849448459 |
| Brokerage & Investment Banking | 15 | 1.1140167686498674 |
| Building Materials | 7 | 0.2564680728541053 |
| Business & Consumer Services | 60 | 0.4250220019215906 |
| Cable TV | 1 | 0.15792383519029668 |
| Chemical (Basic) | 16 | 0.881279660818725 |
| Chemical (Diversified) | 1 | 0.6071616805736153 |
| Chemical (Specialty) | 45 | 0.6325447521309655 |
| Coal & Related Energy | 84 | 1.467363907342948 |
| Computer Services | 18 | 0.5255179804687785 |
| Computers/Peripherals | 1 | NA |
| Construction Supplies | 14 | 0.571964978407795 |
| Diversified | 6 | 0.6247390662486646 |
| Drugs (Biotechnology) | 83 | 0.8796342942959642 |
| Drugs (Pharmaceutical) | 124 | 0.5460050850846703 |
| Education | 14 | 0.3998637732185591 |
| Electrical Equipment | 37 | 0.7278717348602222 |
| Electronics (Consumer & Office) | 6 | 0.7438285307682257 |
| Electronics (General) | 43 | 0.9858573489493806 |
| Engineering/Construction | 30 | 0.7517363182730534 |
| Entertainment | 25 | 0.932372617980317 |
| Environmental & Waste Services | 35 | 0.4465384275522495 |
| Farming/Agriculture | 24 | 0.2816259223424171 |
| Financial Svcs. (Non-bank & Insurance) | 69 | 0.39706295854981566 |
| Food Processing | 51 | 0.7817220413273633 |
| Food Wholesalers | 4 | 0.5598495941588604 |
| Furn/Home Furnishings | 6 | 0.7918114187211652 |
| Green & Renewable Energy | 23 | 0.6038541144559506 |
| Healthcare Products | 56 | 0.6564530126914156 |
| Healthcare Support Services | 23 | 0.6147627396081814 |
| Heathcare Information and Technology | 45 | 1.0459593151346065 |
| Homebuilding | 3 | 0.7423619919667225 |
| Hospitals/Healthcare Facilities | 14 | 0.5045022860254643 |
| Hotel/Gaming | 28 | 0.8021635431444687 |
| Household Products | 32 | 0.6462657722562013 |
| Information Services | 3 | 0.5487190388138448 |
| Insurance (General) | 3 | 0.499194510589648 |
| Insurance (Life) | 11 | 0.7445455401044998 |
| Insurance (Prop/Cas.) | 8 | 0.4079739101593961 |
| Investments & Asset Management | 194 | 0.4353386124754953 |
| Machinery | 30 | 0.6752422775768261 |
| Metals & Mining | 1304 | 1.1092978535124964 |
| Office Equipment & Services | 0 | 15 |
| Oil/Gas (Integrated) | 4 | 1.2456331855617062 |
| Oil/Gas (Production and Exploration) | 207 | 0.8371339613142424 |
| Oil/Gas Distribution | 10 | 0.4498669299378857 |
| Oilfield Svcs/Equip. | 29 | 0.9504718626842806 |
| Packaging & Container | 8 | 0.639575303751004 |
| Paper/Forest Products | 17 | 0.7447043552574795 |
| Power | 17 | 0.27143255996576987 |
| Precious Metals | 616 | 1.4556762717793619 |
| Publishing & Newspapers | 7 | 0.20860903439448242 |
| R.E.I.T. | 53 | 0.4201932802013747 |
| Real Estate (Development) | 14 | 0.3070782016828816 |
| Real Estate (General/Diversified) | 2 | 0.2541203658161623 |
| Real Estate (Operations & Services) | 31 | 0.6085869319910119 |
| Recreation | 14 | 0.7262652671680923 |
| Reinsurance | 0 | 15 |
| Restaurant/Dining | 17 | 0.2967040432816547 |
| Retail (Automotive) | 11 | 0.3804698211932919 |
| Retail (Building Supply) | 9 | 0.6718986955679003 |
| Retail (Distributors) | 30 | 0.6918045218936425 |
| Retail (General) | 9 | 0.6273878224494949 |
| Retail (Grocery and Food) | 14 | 0.4676577774762029 |
| Retail (REITs) | 16 | 0.368334698971578 |
| Retail (Special Lines) | 37 | 0.8733723195160265 |
| Rubber& Tires | 0 | 15 |
| Semiconductor | 6 | 0.789737980170876 |
| Semiconductor Equip | 2 | -0.23113179370399814 |
| Shipbuilding & Marine | 8 | 0.3576469027292039 |
| Shoe | 1 | 15 |
| Software (Entertainment) | 27 | 1.2489381936711776 |
| Software (Internet) | 23 | 1.468205062379181 |
| Software (System & Application) | 200 | 1.1609232143887496 |
| Steel | 48 | 0.9604795897524777 |
| Telecom (Wireless) | 2 | 0.17830660067368603 |
| Telecom. Equipment | 21 | 1.0634341091108512 |
| Telecom. Services | 20 | 0.4569614789209599 |
| Tobacco | 2 | 10.79152281384688 |
| Transportation | 15 | 0.6136599948570018 |
| Transportation (Railroads) | 3 | 0.6201485816142025 |
| Trucking | 4 | 0.8239636890385263 |
| Utility (General) | 6 | 0.15202783190367394 |
| Utility (Water) | 4 | 0.4620150676491281 |
| Total Market | 4278 | 0.7548617422056766 |
| Total Market (without financials) | 3956 | 0.9257487464390752 |

## Input Choices

| Effective |
|---|
| Marginal |
