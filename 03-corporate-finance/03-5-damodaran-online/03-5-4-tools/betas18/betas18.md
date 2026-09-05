---
title: "Betas18"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas18.xls
---

# Betas18

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas18.xls

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

| Date updated: | 43470.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | http://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | http://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 48 | 0.8679813153566758 | 0.6668159774546396 |
| Aerospace/Defense | 85 | 1.09222603297197 | 0.5107850207868528 |
| Air Transport | 18 | 0.6344901276087225 | 0.41340581347068883 |
| Apparel | 50 | 0.7631729241326889 | 0.5379623288697442 |
| Auto & Truck | 14 | 0.3418710955309782 | 0.48777558323221165 |
| Auto Parts | 52 | 0.9678850643412212 | 0.5603734143197332 |
| Bank (Money Center) | 10 | 0.4282334507505517 | 0.17304533402607078 |
| Banks (Regional) | 633 | 0.4043516578768579 | 0.20146464548080123 |
| Beverage (Alcoholic) | 31 | 1.0479649012287298 | 0.5693641956642026 |
| Beverage (Soft) | 37 | 1.0445632745746374 | 0.6395938095091317 |
| Broadcasting | 24 | 0.5086546647315182 | 0.42219346886199566 |
| Brokerage & Investment Banking | 38 | 0.4576710177663197 | 0.3703764707836142 |
| Building Materials | 42 | 0.9149343033203543 | 0.37071216329788187 |
| Business & Consumer Services | 168 | 1.0001911265533716 | 0.5494578479468898 |
| Cable TV | 14 | 0.761515774451065 | 0.2818127809114058 |
| Chemical (Basic) | 39 | 1.1226945412373202 | 0.5417565435736025 |
| Chemical (Diversified) | 6 | 1.4913554180375088 | 0.3575407761041985 |
| Chemical (Specialty) | 89 | 0.9890237899947718 | 0.47527181169450805 |
| Coal & Related Energy | 23 | 0.967284291647994 | 0.5706516188580665 |
| Computer Services | 119 | 1.0462592460215911 | 0.6067225342558576 |
| Computers/Peripherals | 57 | 1.4982789281613096 | 0.5360097837448855 |
| Construction Supplies | 48 | 1.149597054125011 | 0.4206364965462961 |
| Diversified | 23 | 1.1438090814341535 | 0.5054728075118394 |
| Drugs (Biotechnology) | 481 | 1.4307835597315306 | 0.6040888493203511 |
| Drugs (Pharmaceutical) | 237 | 1.3790871702678402 | 0.6490594004420682 |
| Education | 35 | 1.1083755117525074 | 0.538963612720728 |
| Electrical Equipment | 116 | 1.1823979253907428 | 0.6492524151589845 |
| Electronics (Consumer & Office) | 19 | 1.2240277060430294 | 0.5769822720834676 |
| Electronics (General) | 160 | 0.9606603035174501 | 0.515860084830092 |
| Engineering/Construction | 52 | 0.810158783963093 | 0.43092685932052205 |
| Entertainment | 120 | 1.2140124334135816 | 0.6943994428653351 |
| Environmental & Waste Services | 91 | 0.9601751957992237 | 0.6328889073191557 |
| Farming/Agriculture | 33 | 0.49587806644422544 | 0.5496511083059528 |
| Financial Svcs. (Non-bank & Insurance) | 259 | 0.07561533503134525 | 0.30644051349838164 |
| Food Processing | 83 | 0.6114219919250382 | 0.44014468324502815 |
| Food Wholesalers | 18 | 1.234429635135682 | 0.5031675380315522 |
| Furn/Home Furnishings | 30 | 0.6678086467719215 | 0.4822289030875486 |
| Green & Renewable Energy | 21 | 0.7987630939198215 | 0.7243660856666055 |
| Healthcare Products | 248 | 1.0412420580286896 | 0.5501235117620845 |
| Healthcare Support Services | 111 | 1.0266507370055664 | 0.5388818381502589 |
| Heathcare Information and Technology | 119 | 1.1770734443491222 | 0.5598137927247793 |
| Homebuilding | 31 | 0.7246149165867888 | 0.4156884280057186 |
| Hospitals/Healthcare Facilities | 34 | 0.5521951118294665 | 0.48377662083637035 |
| Hotel/Gaming | 70 | 0.7117119465176714 | 0.4489551265315968 |
| Household Products | 141 | 0.9972506674830345 | 0.6116996384730774 |
| Information Services | 71 | 1.04761476043476 | 0.42093635312350025 |
| Insurance (General) | 20 | 0.6717916195533868 | 0.3298290759177526 |
| Insurance (Life) | 23 | 0.7033562806382644 | 0.2660350491771033 |
| Insurance (Prop/Cas.) | 50 | 0.6511506597940658 | 0.22611624199146937 |
| Investments & Asset Management | 172 | 0.866684474117967 | 0.36859497245459294 |
| Machinery | 127 | 1.0121653053546547 | 0.4302904730594393 |
| Metals & Mining | 94 | 1.1094422701693822 | 0.683007434840342 |
| Office Equipment & Services | 24 | 1.3336679465607404 | 0.470576227506701 |
| Oil/Gas (Integrated) | 5 | 1.055607164642918 | 0.37932506830420437 |
| Oil/Gas (Production and Exploration) | 301 | 1.0743174544514105 | 0.6041420352516472 |
| Oil/Gas Distribution | 20 | 0.6231608561764338 | 0.40905439867235804 |
| Oilfield Svcs/Equip. | 134 | 1.0668864769579942 | 0.5599036547753962 |
| Packaging & Container | 27 | 0.7370550227480763 | 0.3961191555127831 |
| Paper/Forest Products | 20 | 1.1728745712683208 | 0.5161034102987132 |
| Power | 51 | 0.3460165075906414 | 0.2332299776282963 |
| Precious Metals | 91 | 1.1490747541483908 | 0.6986558814957184 |
| Publishing & Newspapers | 33 | 0.8978859113758451 | 0.436409397801752 |
| R.E.I.T. | 238 | 0.409468579532681 | 0.19972988830406255 |
| Real Estate (Development) | 18 | 0.8710375930164825 | 0.5286767447862721 |
| Real Estate (General/Diversified) | 11 | 1.32735715457991 | 0.4906723114408076 |
| Real Estate (Operations & Services) | 59 | 0.9528770584096617 | 0.5450714626242869 |
| Recreation | 72 | 0.8092329672801789 | 0.5168030746992182 |
| Reinsurance | 2 | 0.8820173563179452 | 0.10492021861913658 |
| Restaurant/Dining | 78 | 0.6510688399498351 | 0.44101040954903176 |
| Retail (Automotive) | 24 | 0.7609980014069839 | 0.45770036396352504 |
| Retail (Building Supply) | 17 | 0.9672791777625668 | 0.4176248307740727 |
| Retail (Distributors) | 88 | 0.9870211814795625 | 0.5219909171095275 |
| Retail (General) | 19 | 0.7514861871220232 | 0.4057797297571276 |
| Retail (Grocery and Food) | 12 | 0.2812326219094314 | 0.3711118690469338 |
| Retail (Online) | 79 | 1.34449825920508 | 0.5959567813699645 |
| Retail (Special Lines) | 91 | 0.8000650410909912 | 0.5122991736141596 |
| Rubber& Tires | 4 | 0.23902988074589715 | 0.3702502050279505 |
| Semiconductor | 72 | 1.2637967280679967 | 0.44607512433866636 |
| Semiconductor Equip | 41 | 1.3908894934763405 | 0.43733704196451284 |
| Shipbuilding & Marine | 9 | 0.7785073448794292 | 0.500595763640584 |
| Shoe | 10 | 0.7412820035926789 | 0.3571631421110512 |
| Software (Entertainment) | 92 | 1.2697947323690497 | 0.6844153476383252 |
| Software (Internet) | 44 | 1.3051434552841432 | 0.6444097660995498 |
| Software (System & Application) | 355 | 1.1619596463607587 | 0.5631042690577909 |
| Steel | 37 | 1.2948714024708063 | 0.48994504399399974 |
| Telecom (Wireless) | 21 | 0.7062658331251642 | 0.6198770989208389 |
| Telecom. Equipment | 98 | 1.0228587017593667 | 0.4932346439397782 |
| Telecom. Services | 67 | 0.7408260327170008 | 0.628825580142901 |
| Tobacco | 17 | 1.1252643536813445 | 0.622492723511322 |
| Transportation | 19 | 0.8992975404508528 | 0.41304950768216236 |
| Transportation (Railroads) | 10 | 2.080151823033132 | 0.3941431487334624 |
| Trucking | 28 | 0.71085656044871 | 0.4151070861999311 |
| Utility (General) | 18 | 0.1745698394445703 | 0.1259272568957579 |
| Utility (Water) | 19 | 0.32295708453677063 | 0.37577090332673935 |
| Total Market  | 7209 | 0.8020173970839132 | 0.4863542387124373 |
| Total Market (without financials) | 6004 | 0.9985589472694634 | 0.5323131577367258 |

## Inputs

| Effective |
|---|
| Marginal |
