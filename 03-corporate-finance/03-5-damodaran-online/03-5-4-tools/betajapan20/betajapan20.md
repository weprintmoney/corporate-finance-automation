---
title: "Betajapan20"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan20.xls
---

# Betajapan20

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan20.xls

Sheets: Sheet1, Industry Averages, Input Choices

## Sheet1

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

| Date updated: | 44201.0 | YouTube Video explaining estimation choices and process. |
|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  |
| What is this data? | Beta, Unlevered beta and other risk measures |  |
| Home Page: | http://www.damodaran.com |  |
| Data website: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |
| Companies in each industry: | https://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |
| Variable definitions: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash |
| Advertising | 63 | 1.5259732684156608 |
| Aerospace/Defense | 2 | 0.6734138349473159 |
| Air Transport | 5 | 0.8504729199818912 |
| Apparel | 65 | 0.9527498020767923 |
| Auto & Truck | 10 | 1.0330088943419098 |
| Auto Parts | 105 | 1.308464094407217 |
| Bank (Money Center) | 6 | -0.8125688813815956 |
| Banks (Regional) | 81 | -0.365474116423365 |
| Beverage (Alcoholic) | 6 | 0.6978447006659707 |
| Beverage (Soft) | 5 | 0.5460049060461644 |
| Broadcasting | 11 | 0.9695316701872663 |
| Brokerage & Investment Banking | 36 | 0.1790177213699494 |
| Building Materials | 69 | 0.9425666289955346 |
| Business & Consumer Services | 186 | 1.497235025307868 |
| Cable TV | 1 | 0.7494034957200618 |
| Chemical (Basic) | 70 | 1.0993899601078245 |
| Chemical (Diversified) | 21 | 0.8827283224572883 |
| Chemical (Specialty) | 75 | 1.1356942450490015 |
| Coal & Related Energy | 1 | 0.6935846380205499 |
| Computer Services | 198 | 1.280073315849896 |
| Computers/Peripherals | 30 | 1.299401387354585 |
| Construction Supplies | 50 | 1.0340032865890254 |
| Diversified | 14 | 0.9534576964240397 |
| Drugs (Biotechnology) | 25 | 1.4933546373285862 |
| Drugs (Pharmaceutical) | 40 | 0.9583993784367326 |
| Education | 27 | 1.0131739217486995 |
| Electrical Equipment | 59 | 1.454036391461857 |
| Electronics (Consumer & Office) | 12 | 1.4359966112666172 |
| Electronics (General) | 135 | 1.4691685115672828 |
| Engineering/Construction | 157 | 1.1961483822023606 |
| Entertainment | 67 | 1.4003848760827173 |
| Environmental & Waste Services | 34 | 1.2325861902867896 |
| Farming/Agriculture | 11 | 1.0083601085759328 |
| Financial Svcs. (Non-bank & Insurance) | 39 | 0.12628688935503551 |
| Food Processing | 118 | 0.5806493819156402 |
| Food Wholesalers | 35 | 0.6816445514043636 |
| Furn/Home Furnishings | 19 | 1.1129009377841217 |
| Green & Renewable Energy | 8 | 1.2431769208941645 |
| Healthcare Products | 36 | 0.9485796702333243 |
| Healthcare Support Services | 43 | 1.221890891853866 |
| Heathcare Information and Technology | 34 | 1.3994226813073034 |
| Homebuilding | 51 | 0.8938245612988366 |
| Hospitals/Healthcare Facilities | 9 | 0.9343908055480614 |
| Hotel/Gaming | 28 | 0.8894763391089373 |
| Household Products | 42 | 0.9141044822733023 |
| Information Services | 23 | 1.098034626877585 |
| Insurance (General) | 4 | 1.4461471639730337 |
| Insurance (Life) | 5 | -0.5011430151837266 |
| Insurance (Prop/Cas.) | 6 | 1.2065904398992788 |
| Investments & Asset Management | 10 | 1.6785477362452532 |
| Machinery | 232 | 1.2641429324370825 |
| Metals & Mining | 21 | 0.9705268252807305 |
| Office Equipment & Services | 32 | 1.312298139827242 |
| Oil/Gas (Integrated) | 0 | NA |
| Oil/Gas (Production and Exploration) | 2 | 1.0054031942687855 |
| Oil/Gas Distribution | 3 | 0.5308132405947544 |
| Oilfield Svcs/Equip. | 19 | 0.5001437544317827 |
| Packaging & Container | 31 | 0.7878586403524257 |
| Paper/Forest Products | 17 | 0.5553018652411124 |
| Power | 25 | 0.18500426522856694 |
| Precious Metals | 2 | 0.4994374005205317 |
| Publishing & Newspapers | 52 | 1.2308992902468712 |
| R.E.I.T. | 62 | 0.9898601026682766 |
| Real Estate (Development) | 14 | 1.0612692860468578 |
| Real Estate (General/Diversified) | 56 | 0.6332515760407743 |
| Real Estate (Operations & Services) | 38 | 0.7619107632726893 |
| Recreation | 51 | 1.1532171799488846 |
| Reinsurance | 0 | NA |
| Restaurant/Dining | 105 | 0.8650342262878055 |
| Retail (Automotive) | 29 | 1.0142923580241723 |
| Retail (Building Supply) | 18 | 0.8994551866241172 |
| Retail (Distributors) | 153 | 0.5944440619487497 |
| Retail (General) | 33 | 0.6830805995415415 |
| Retail (Grocery and Food) | 46 | 0.7146271666391937 |
| Retail (Online) | 0 | NA |
| Retail (Special Lines) | 110 | 0.9860518597224383 |
| Rubber& Tires | 7 | 1.1188229410877397 |
| Semiconductor | 18 | 1.6049627405152223 |
| Semiconductor Equip | 33 | 1.7454067854393485 |
| Shipbuilding & Marine | 31 | 0.44833291031736144 |
| Shoe | 3 | 1.1700678420333614 |
| Software (Entertainment) | 66 | 1.5328225226261654 |
| Software (Internet) | 23 | 1.6978227905923455 |
| Software (System & Application) | 150 | 1.5002425218082158 |
| Steel | 45 | 0.6805155424197521 |
| Telecom (Wireless) | 7 | 0.8127226929159529 |
| Telecom. Equipment | 17 | 1.9821526715656557 |
| Telecom. Services | 16 | 1.0183340350010128 |
| Tobacco | 1 | 0.5998674090585641 |
| Transportation | 16 | 0.8284154887439373 |
| Transportation (Railroads) | 21 | 0.31692558181765706 |
| Trucking | 39 | 0.6243782090184469 |
| Utility (General) | 0 | NA |
| Utility (Water) | 0 | NA |
| Total Market | 3893 | 1.0379996897638073 |
| Total Market (without financials) | 3706 | 0.9920706320246404 |

## Input Choices

| Effective |
|---|
| Marginal |
