---
title: "Betas19"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas19.xls
---

# Betas19

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas19.xls

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

| Date updated: | 43835.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | http://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | http://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry  Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 47 | 0.9349531429448596 | 0.656935125 |
| Aerospace/Defense | 77 | 1.078522159887352 | 0.48190203 |
| Air Transport | 18 | 0.8436729976274394 | 0.411024935 |
| Apparel | 51 | 0.8296410009433827 | 0.503074903 |
| Auto & Truck | 13 | 0.5257350397759242 | 0.501485235 |
| Auto Parts | 46 | 0.9469935769993065 | 0.574559174 |
| Bank (Money Center) | 7 | 0.5595414670761663 | 0.174004317 |
| Banks (Regional) | 611 | 0.4313155820626237 | 0.158177698 |
| Beverage (Alcoholic) | 21 | 0.9188825577761112 | 0.55276714 |
| Beverage (Soft) | 34 | 1.0907131928183842 | 0.667617471 |
| Broadcasting | 27 | 0.729937390293151 | 0.431276704 |
| Brokerage & Investment Banking | 39 | 0.5676743238719565 | 0.44006909 |
| Building Materials | 42 | 1.0185312839204805 | 0.358841504 |
| Business & Consumer Services | 165 | 0.8948866171646999 | 0.533056042 |
| Cable TV | 14 | 0.776608279328833 | 0.329430057 |
| Chemical (Basic) | 43 | 0.9929566124984756 | 0.530539804 |
| Chemical (Diversified) | 6 | 1.2147165368811397 | 0.505580699 |
| Chemical (Specialty) | 94 | 0.9648570942816654 | 0.481796649 |
| Coal & Related Energy | 22 | 1.0486643640232785 | 0.656960001 |
| Computer Services | 106 | 0.9528662646292019 | 0.572968939 |
| Computers/Peripherals | 48 | 1.6400833392351297 | 0.534849567 |
| Construction Supplies | 44 | 1.10359654774166 | 0.359127101 |
| Diversified | 23 | 1.2484828302966493 | 0.495433105 |
| Drugs (Biotechnology) | 503 | 1.3891731337867141 | 0.593777525 |
| Drugs (Pharmaceutical) | 267 | 1.2856575366949226 | 0.677678734 |
| Education | 35 | 1.3560146590000444 | 0.603740849 |
| Electrical Equipment | 113 | 1.307118859086069 | 0.636362108 |
| Electronics (Consumer & Office) | 20 | 1.25079435757328 | 0.547980471 |
| Electronics (General) | 153 | 1.070921529276746 | 0.505306626 |
| Engineering/Construction | 54 | 1.3250378765861548 | 0.510519097 |
| Entertainment | 107 | 1.2017030374551592 | 0.684468641 |
| Environmental & Waste Services | 82 | 1.0485101305295534 | 0.624148603 |
| Farming/Agriculture | 31 | 0.6274511480684076 | 0.495635474 |
| Financial Svcs. (Non-bank & Insurance) | 232 | 0.09826313785398752 | 0.274951219 |
| Food Processing | 88 | 0.6968082479529737 | 0.509360267 |
| Food Wholesalers | 17 | 0.6577661732913673 | 0.478716284 |
| Furn/Home Furnishings | 35 | 0.8183273103323906 | 0.469426486 |
| Green & Renewable Energy | 22 | 0.593772952019942 | 0.697853491 |
| Healthcare Products | 242 | 0.9818186838686335 | 0.532314784 |
| Healthcare Support Services | 128 | 0.9462382149452834 | 0.541445431 |
| Heathcare Information and Technology | 129 | 1.152697351786613 | 0.549248771 |
| Homebuilding | 32 | 0.6640558389827699 | 0.399038442 |
| Hospitals/Healthcare Facilities | 36 | 0.6255623897598616 | 0.490515962 |
| Hotel/Gaming | 65 | 0.9144446236425152 | 0.399915959 |
| Household Products | 127 | 0.9370572448948898 | 0.609275797 |
| Information Services | 69 | 1.0315158970762186 | 0.455634292 |
| Insurance (General) | 19 | 0.5926992839184214 | 0.279153277 |
| Insurance (Life) | 24 | 0.7324805743770343 | 0.22356712 |
| Insurance (Prop/Cas.) | 51 | 0.5890715247484962 | 0.225372596 |
| Investments & Asset Management | 192 | 0.8601828401441228 | 0.31484158 |
| Machinery | 120 | 1.0985210616277283 | 0.427411585 |
| Metals & Mining | 92 | 1.0865722025981523 | 0.660875541 |
| Office Equipment & Services | 22 | 1.2442326298508288 | 0.434347081 |
| Oil/Gas (Integrated) | 4 | 1.1174661727895663 | 0.359008858 |
| Oil/Gas (Production and Exploration) | 269 | 1.076710639640376 | 0.640473802 |
| Oil/Gas Distribution | 24 | 0.6175192303191579 | 0.442214107 |
| Oilfield Svcs/Equip. | 136 | 1.218654717118134 | 0.586225409 |
| Packaging & Container | 24 | 0.6781735167393964 | 0.388008151 |
| Paper/Forest Products | 15 | 1.2543747470505289 | 0.471598233 |
| Power | 52 | 0.37843539998307546 | 0.22253056 |
| Precious Metals | 83 | 1.3320479668619645 | 0.722350068 |
| Publishing & Newspapers | 31 | 0.7567842313849863 | 0.460772934 |
| R.E.I.T. | 234 | 0.4256203375693727 | 0.203343189 |
| Real Estate (Development) | 20 | 0.8910740523856756 | 0.67073037 |
| Real Estate (General/Diversified) | 12 | 1.501720441937595 | 0.498988845 |
| Real Estate (Operations & Services) | 57 | 0.6750476077656148 | 0.522620932 |
| Recreation | 63 | 0.7540286170435926 | 0.542894636 |
| Reinsurance | 2 | 0.7698542925210008 | 0.128729091 |
| Restaurant/Dining | 77 | 0.7518963813261236 | 0.474197137 |
| Retail (Automotive) | 26 | 0.8685186932111402 | 0.465456381 |
| Retail (Building Supply) | 17 | 1.1509711433254448 | 0.504164038 |
| Retail (Distributors) | 80 | 0.8937149652220674 | 0.466163484 |
| Retail (General) | 18 | 0.9457267947342817 | 0.407656672 |
| Retail (Grocery and Food) | 13 | 0.3451030636472698 | 0.398430316 |
| Retail (Online) | 70 | 1.1594182467938388 | 0.639262804 |
| Retail (Special Lines) | 89 | 0.6903463796794427 | 0.531341807 |
| Rubber& Tires | 4 | 0.45318132931651134 | 0.391751329 |
| Semiconductor | 72 | 1.236890276724555 | 0.427647391 |
| Semiconductor Equip | 39 | 1.2534843105487556 | 0.410622827 |
| Shipbuilding & Marine | 10 | 1.5713945020074378 | 0.531927481 |
| Shoe | 11 | 0.8336099690951179 | 0.359813441 |
| Software (Entertainment) | 86 | 1.2858744552797758 | 0.6359555 |
| Software (Internet) | 30 | 1.5032034061311 | 0.567142419 |
| Software (System & Application) | 363 | 1.149160826869191 | 0.581777235 |
| Steel | 32 | 1.2855689138232198 | 0.402795086 |
| Telecom (Wireless) | 18 | 0.5969080740252654 | 0.480394259 |
| Telecom. Equipment | 91 | 0.8359786583228734 | 0.49029901 |
| Telecom. Services | 67 | 0.6665842243194448 | 0.593275941 |
| Tobacco | 17 | 1.426322641272642 | 0.583686042 |
| Transportation | 18 | 0.9572701695111526 | 0.415928495 |
| Transportation (Railroads) | 8 | 1.8919831806779572 | 0.463163024 |
| Trucking | 33 | 1.041066799245524 | 0.434347824 |
| Utility (General) | 16 | 0.18968841681761509 | 0.135567971 |
| Utility (Water) | 17 | 0.5653212571240506 | 0.363909339 |
| Total Market | 7053 | 0.8294537733223437 | 0.480648949 |
| Total Market (without financials) | 5878 | 1.0124816766890556 | 0.532253818881082 |

## Inputs

| Effective |
|---|
| Marginal |
