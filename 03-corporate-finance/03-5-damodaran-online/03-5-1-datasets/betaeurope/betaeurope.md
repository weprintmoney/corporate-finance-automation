---
title: "Betaeurope"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaEurope.xls
---

# Betaeurope

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaEurope.xls

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

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Effective |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | Marginal |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | Standard deviation in operating income (last 10 years) |
| Advertising | 83 | 0.7240219104468779 | 0.46398642978475796 |
| Aerospace/Defense | 67 | 1.2427384879420882 | 0.3269558302643142 |
| Air Transport | 33 | 0.8246634039360115 | 1.5301960019054994 |
| Apparel | 109 | 0.7751456992602103 | 0.3738616046655462 |
| Auto & Truck | 31 | 0.8543957866401695 | 0.4273327474287181 |
| Auto Parts | 58 | 0.8043436237961346 | 0.24659485414540994 |
| Bank (Money Center) | 113 | 0.468376236580968 | 1.73675133607513 |
| Banks (Regional) | 69 | 0.17521548796877018 | NA |
| Beverage (Alcoholic) | 52 | 0.43204454977003287 | 0.11567419358157041 |
| Beverage (Soft) | 14 | 0.3599348013993773 | 0.3221939799046711 |
| Broadcasting | 18 | 0.8604245044796446 | 0.16607214702028053 |
| Brokerage & Investment Banking | 69 | 0.5745411027069562 | 0.6681926174786463 |
| Building Materials | 84 | 0.9373865794848548 | 0.2295248903403694 |
| Business & Consumer Services | 176 | 0.7146968116202744 | 0.21367736848770405 |
| Cable TV | 2 | 0.7565066700519174 | 0.5120758036570735 |
| Chemical (Basic) | 58 | 0.5020063295368162 | 0.4371769671799277 |
| Chemical (Diversified) | 7 | 1.0402992339392618 | 0.31895174197587384 |
| Chemical (Specialty) | 92 | 1.0126812485384102 | 0.23406512916061714 |
| Coal & Related Energy | 15 | 0.6997388287808479 | 1.5699466132871167 |
| Computer Services | 210 | 0.90442786686994 | 0.27916437175013525 |
| Computers/Peripherals | 38 | 1.1787978692657777 | 0.42032930737704716 |
| Construction Supplies | 119 | 0.8586497924588679 | 0.4318262364142823 |
| Diversified | 72 | 0.850115955823646 | 0.3390878592842986 |
| Drugs (Biotechnology) | 199 | 1.1419597046001697 | NA |
| Drugs (Pharmaceutical) | 115 | 1.0863233568429813 | 0.19259564073749133 |
| Education | 18 | 0.48389455211024646 | 0.23251585295340402 |
| Electrical Equipment | 146 | 1.0548204701514463 | 0.252958885447378 |
| Electronics (Consumer & Office) | 17 | 1.2819692999668768 | 0.24689960381942677 |
| Electronics (General) | 142 | 1.0414185446614295 | 0.18094698676373483 |
| Engineering/Construction | 160 | 0.7980766366937397 | 0.24315378401699592 |
| Entertainment | 199 | 0.7251316013752445 | 0.3714096582191131 |
| Environmental & Waste Services | 48 | 0.8025107909201695 | 0.30395589948454127 |
| Farming/Agriculture | 46 | 0.3019541799447252 | 0.3285317924905113 |
| Financial Svcs. (Non-bank & Insurance) | 146 | 0.41167230182039505 | 0.3527153764322084 |
| Food Processing | 173 | 0.381745154513015 | 0.13371650340555655 |
| Food Wholesalers | 11 | 0.37481330991031797 | 0.4747580025432125 |
| Furn/Home Furnishings | 53 | 0.3970408846882334 | 0.236749727203321 |
| Green & Renewable Energy | 60 | 0.460309863074919 | 0.4833104978153327 |
| Healthcare Products | 163 | 1.1286753995766274 | 0.19184191789822808 |
| Healthcare Support Services | 47 | 0.6396873395765236 | 0.2549673252622008 |
| Heathcare Information and Technology | 89 | 1.0817589035988804 | 0.3579311617166524 |
| Homebuilding | 36 | 1.4153822691367681 | 0.221659242841188 |
| Hospitals/Healthcare Facilities | 29 | 0.30312243422128216 | 0.2348835206420151 |
| Hotel/Gaming | 103 | 0.7730179718588945 | 0.8638930047086435 |
| Household Products | 65 | 0.7113193564134902 | 0.1398573164366598 |
| Information Services | 6 | 0.4435471274074488 | 0.2793220446653852 |
| Insurance (General) | 34 | 0.7221234429168222 | 0.21441778463795924 |
| Insurance (Life) | 15 | 0.649179321289093 | 0.3021885150292 |
| Insurance (Prop/Cas.) | 19 | 0.5149482196764558 | 0.3828579743425443 |
| Investments & Asset Management | 338 | 0.585354004073402 | 0.37619527934567687 |
| Machinery | 210 | 1.0843768780451168 | 0.17035910881822186 |
| Metals & Mining | 118 | 0.9588916873764738 | 0.548679851437121 |
| Office Equipment & Services | 20 | 0.5471382685366363 | 0.14405643911739224 |
| Oil/Gas (Integrated) | 12 | 0.40597584964829553 | 0.6375127044127864 |
| Oil/Gas (Production and Exploration) | 83 | 0.652297401315061 | 1.1449945471946357 |
| Oil/Gas Distribution | 30 | 0.4760247747904137 | 0.6477902588789396 |
| Oilfield Svcs/Equip. | 58 | 0.8103494900227602 | 0.7545704267195701 |
| Packaging & Container | 42 | 0.5433154015974925 | 0.24695339123844767 |
| Paper/Forest Products | 36 | 0.5509332556866804 | 0.3187104199288833 |
| Power | 69 | 0.4529303561672471 | 0.3188889896739052 |
| Precious Metals | 39 | 0.9530019712650923 | 0.6922546497003557 |
| Publishing & Newspapers | 59 | 0.5115086264349705 | 0.3348608560987762 |
| R.E.I.T. | 138 | 0.39845717055578816 | 0.14926113367633193 |
| Real Estate (Development) | 61 | 0.397570588405823 | 0.43280736224648164 |
| Real Estate (General/Diversified) | 45 | 0.3523071023884126 | 0.22370902475013993 |
| Real Estate (Operations & Services) | 219 | 0.3353502289498914 | 0.18880954210254752 |
| Recreation | 59 | 0.892761152950186 | 0.5191490979803722 |
| Reinsurance | 4 | 1.1389589350670695 | 0.39877720788860793 |
| Restaurant/Dining | 38 | 0.5891309004797586 | 0.7309700287971506 |
| Retail (Automotive) | 22 | 0.8741235522186201 | 0.5542788115004955 |
| Retail (Building Supply) | 26 | 0.8785310278204373 | 0.26518980990591806 |
| Retail (Distributors) | 117 | 0.6445635074030105 | 0.2978334588200174 |
| Retail (General) | 31 | 0.885906253188005 | 0.17804529260066312 |
| Retail (Grocery and Food) | 34 | 0.7497311664910142 | 0.23108781571044495 |
| Retail (REITs) | 28 | 0.35562677961201383 | 0.23043439126343312 |
| Retail (Special Lines) | 105 | 1.0600352874163959 | 0.27053437343992076 |
| Rubber& Tires | 10 | 0.6452571463400784 | 0.21991858045552387 |
| Semiconductor | 36 | 1.2164813554937137 | 0.7267957196552551 |
| Semiconductor Equip | 21 | 1.692910038974996 | 0.576837619961483 |
| Shipbuilding & Marine | 65 | 0.7401647849691244 | 1.1654138835334633 |
| Shoe | 9 | 1.1010944523697896 | 0.7879515681942035 |
| Software (Entertainment) | 51 | 1.024362473773237 | 0.15919503009555708 |
| Software (Internet) | 23 | 0.6310730550667838 | 0.6514172121443459 |
| Software (System & Application) | 290 | 0.9635892470727443 | 0.15461728967159102 |
| Steel | 57 | 0.8548645417962621 | 0.9139155015876377 |
| Telecom (Wireless) | 11 | 0.3730641076834413 | 0.3899167284713512 |
| Telecom. Equipment | 50 | 0.7601467911453165 | 0.47901844238629276 |
| Telecom. Services | 62 | 0.4469355205498445 | 0.11878951729448037 |
| Tobacco | 5 | 0.1530521341610707 | 0.22740092113512364 |
| Transportation | 56 | 0.5351793941288769 | 0.3074895627070131 |
| Transportation (Railroads) | 8 | 0.6010648228525083 | 0.9666302722783294 |
| Trucking | 7 | 0.6536316312369804 | 0.4430094691350216 |
| Utility (General) | 18 | 0.4114974821209365 | 0.4104682774416153 |
| Utility (Water) | 12 | 0.46425779608450773 | 0.1470440994174432 |
| Grand Total | 6560 | 0.692144134724092 | 0.2912502035459162 |
| Total Market (without financials) | 5757 | 0.7858018464880012 | 0.3063469814215047 |

## Input Choices

| Effective |
|---|
| Marginal |
