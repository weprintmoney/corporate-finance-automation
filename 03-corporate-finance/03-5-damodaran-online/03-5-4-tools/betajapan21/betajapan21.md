---
title: "Betajapan21"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan21.xls
---

# Betajapan21

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan21.xls

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

| Date updated: | 44566.0 | YouTube Video explaining estimation choices and process. |
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
| Advertising | 69 | 1.885150176176757 |
| Aerospace/Defense | 2 | 0.6931531399736915 |
| Air Transport | 5 | 0.7821802635364595 |
| Apparel | 62 | 1.00229832951656 |
| Auto & Truck | 10 | 1.0266723425107784 |
| Auto Parts | 104 | 1.4317459872729916 |
| Bank (Money Center) | 6 | -0.5161475363064791 |
| Banks (Regional) | 80 | -0.2247689749368617 |
| Beverage (Alcoholic) | 6 | 0.6989681366937839 |
| Beverage (Soft) | 6 | 0.5673098642777151 |
| Broadcasting | 11 | 0.985853460514174 |
| Brokerage & Investment Banking | 36 | 0.1694912300909122 |
| Building Materials | 67 | 0.9996730959155506 |
| Business & Consumer Services | 195 | 1.6482928141035131 |
| Cable TV | 1 | 0.7943422113392794 |
| Chemical (Basic) | 69 | 1.064576381331768 |
| Chemical (Diversified) | 22 | 0.8223804161320092 |
| Chemical (Specialty) | 74 | 1.190512835311452 |
| Coal & Related Energy | 1 | 0.9667269758529798 |
| Computer Services | 214 | 1.3890533423212303 |
| Computers/Peripherals | 30 | 1.3475622739723032 |
| Construction Supplies | 52 | 1.0249083049908256 |
| Diversified | 15 | 0.8940946985412888 |
| Drugs (Biotechnology) | 27 | 1.6139441273380608 |
| Drugs (Pharmaceutical) | 40 | 1.0285937440451067 |
| Education | 30 | 1.0542917873139652 |
| Electrical Equipment | 57 | 1.4316977400857904 |
| Electronics (Consumer & Office) | 10 | 1.4106599002936482 |
| Electronics (General) | 138 | 1.6318522880108695 |
| Engineering/Construction | 156 | 1.2433936544854858 |
| Entertainment | 68 | 1.6269888263063272 |
| Environmental & Waste Services | 33 | 1.3833174315901795 |
| Farming/Agriculture | 11 | 1.0050714509057164 |
| Financial Svcs. (Non-bank & Insurance) | 38 | 0.07853774639889495 |
| Food Processing | 119 | 0.6237278419255253 |
| Food Wholesalers | 36 | 0.6506762296529691 |
| Furn/Home Furnishings | 21 | 1.4355148918328315 |
| Green & Renewable Energy | 9 | 1.192520627337631 |
| Healthcare Products | 38 | 1.0013725996248466 |
| Healthcare Support Services | 43 | 1.3820751860727707 |
| Heathcare Information and Technology | 35 | 1.4953179974732176 |
| Homebuilding | 53 | 0.9172396552287964 |
| Hospitals/Healthcare Facilities | 9 | 1.1185223604268344 |
| Hotel/Gaming | 30 | 0.9089701633102697 |
| Household Products | 44 | 1.0801561937481756 |
| Information Services | 27 | 1.3828052124938064 |
| Insurance (General) | 4 | 1.9554606986591518 |
| Insurance (Life) | 5 | -0.34625252767115183 |
| Insurance (Prop/Cas.) | 6 | 1.3739336862526024 |
| Investments & Asset Management | 13 | 1.8742187924538984 |
| Machinery | 230 | 1.3228057808052214 |
| Metals & Mining | 21 | 0.9230293330634413 |
| Office Equipment & Services | 27 | 1.4491422779879368 |
| Oil/Gas (Integrated) | 0 | 15 |
| Oil/Gas (Production and Exploration) | 2 | 1.1281173296794889 |
| Oil/Gas Distribution | 3 | 0.5550161223974406 |
| Oilfield Svcs/Equip. | 19 | 0.4732988033510975 |
| Packaging & Container | 32 | 0.771965184572384 |
| Paper/Forest Products | 17 | 0.47360858068725437 |
| Power | 25 | 0.11886943825197321 |
| Precious Metals | 2 | 0.5612501700422874 |
| Publishing & Newspapers | 52 | 1.2545405907684613 |
| R.E.I.T. | 61 | 1.0436981976115853 |
| Real Estate (Development) | 14 | 1.0296761530993752 |
| Real Estate (General/Diversified) | 55 | 0.5563755811461145 |
| Real Estate (Operations & Services) | 41 | 0.6180023274278179 |
| Recreation | 50 | 1.3101587466539242 |
| Reinsurance | 0 | 15 |
| Restaurant/Dining | 106 | 0.8894824478183152 |
| Retail (Automotive) | 29 | 1.0516918567381235 |
| Retail (Building Supply) | 16 | 0.709008842168274 |
| Retail (Distributors) | 146 | 0.571872290387089 |
| Retail (General) | 30 | 0.5637232854647073 |
| Retail (Grocery and Food) | 49 | 0.6245893691743468 |
| Retail (Online) | 61 | 2.120471992709449 |
| Retail (Special Lines) | 109 | 1.0563962675408582 |
| Rubber& Tires | 7 | 1.297625192924618 |
| Semiconductor | 19 | 1.6363585095994853 |
| Semiconductor Equip | 35 | 1.8935096078473084 |
| Shipbuilding & Marine | 31 | 0.6262694089241081 |
| Shoe | 3 | 1.324044483239514 |
| Software (Entertainment) | 69 | 1.6420446191402505 |
| Software (Internet) | 24 | 1.7242024675907397 |
| Software (System & Application) | 161 | 1.8059039332151303 |
| Steel | 44 | 0.7211623409103513 |
| Telecom (Wireless) | 7 | 0.6367616160748032 |
| Telecom. Equipment | 17 | 2.7168461655391933 |
| Telecom. Services | 18 | 0.8707795641748884 |
| Tobacco | 1 | 0.6411701128892761 |
| Transportation | 17 | 0.8070356974174927 |
| Transportation (Railroads) | 21 | 0.2783647415113698 |
| Trucking | 39 | 0.6077313966520939 |
| Utility (General) | 0 | 15 |
| Utility (Water) | 0 | 15 |
| Total Market | 3947 | 0.9777426078392244 |
| Total Market (without financials) | 3759 | 0.9852855164969687 |

## Input Choices

| Effective |
|---|
| Marginal |
