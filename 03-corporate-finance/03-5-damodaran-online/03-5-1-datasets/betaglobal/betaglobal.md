---
title: "Betaglobal"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls
---

# Betaglobal

Source: http://www.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls

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

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Notes |
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
| Advertising | 419 | 1.0861161361977183 | 0.4367319648294255 |
| Aerospace/Defense | 319 | 1.1666842994270814 | 0.4403743803301015 |
| Air Transport | 150 | 0.6840621552018372 | 0.3091008884506873 |
| Apparel | 1207 | 0.7052666591336804 | 0.35698558254195356 |
| Auto & Truck | 165 | 1.1453823854743228 | 0.4437730703979481 |
| Auto Parts | 797 | 1.3534718796622696 | 0.3401959393157561 |
| Bank (Money Center) | 604 | 0.36276505097143535 | 0.24885897307915883 |
| Banks (Regional) | 825 | 0.30036338266393103 | 0.2085037724595426 |
| Beverage (Alcoholic) | 217 | 0.7250443439894131 | 0.26407058149339885 |
| Beverage (Soft) | 94 | 0.5420226574467705 | 0.3841127699055224 |
| Broadcasting | 127 | 0.6557707626756251 | 0.3819823295460835 |
| Brokerage & Investment Banking | 623 | 0.4895737616143335 | 0.3692407247148386 |
| Building Materials | 469 | 0.9027205933766406 | 0.3168658235846766 |
| Business & Consumer Services | 994 | 0.9083303812347316 | 0.3703976452139277 |
| Cable TV | 42 | 0.5908296327587623 | 0.36092660242803 |
| Chemical (Basic) | 909 | 1.0021472613339761 | 0.3163278013158262 |
| Chemical (Diversified) | 63 | 0.9100571271749189 | 0.27585948544245925 |
| Chemical (Specialty) | 952 | 1.0428068761505285 | 0.34823175094829023 |
| Coal & Related Energy | 212 | 1.1330048763544707 | 0.4597620590660238 |
| Computer Services | 1225 | 1.0715769620770927 | 0.3663404487013347 |
| Computers/Peripherals | 343 | 1.468198255805328 | 0.37379935353108434 |
| Construction Supplies | 804 | 0.916676263756567 | 0.32966131619321154 |
| Diversified | 329 | 0.6525743978395595 | 0.28705648780665155 |
| Drugs (Biotechnology) | 1193 | 1.1808092261100824 | 0.5503856607464563 |
| Drugs (Pharmaceutical) | 1260 | 0.9987543035477139 | 0.41994351962215043 |
| Education | 281 | 0.7445772281882472 | 0.3740687957740938 |
| Electrical Equipment | 1158 | 1.3406410283101367 | 0.4109007742807771 |
| Electronics (Consumer & Office) | 122 | 1.1925872612470574 | 0.3898922981224419 |
| Electronics (General) | 1481 | 1.568504800835242 | 0.38940300772621733 |
| Engineering/Construction | 1390 | 0.7593173946857013 | 0.36127859197148243 |
| Entertainment | 733 | 0.9820773204991382 | 0.4294451781371229 |
| Environmental & Waste Services | 397 | 0.9079972563351502 | 0.4000870560323378 |
| Farming/Agriculture | 428 | 0.4926714956404097 | 0.33867073094144384 |
| Financial Svcs. (Non-bank & Insurance) | 1138 | 0.29511483099160984 | 0.36988223561578165 |
| Food Processing | 1450 | 0.5602253462264254 | 0.31198031848835595 |
| Food Wholesalers | 183 | 0.49887742197895796 | 0.3342729988932386 |
| Furn/Home Furnishings | 383 | 0.9383844270287286 | 0.32072625054734893 |
| Green & Renewable Energy | 258 | 0.5668002134281666 | 0.3627740018794838 |
| Healthcare Products | 842 | 1.1165102988785227 | 0.4226386742572651 |
| Healthcare Support Services | 478 | 0.7786715730650319 | 0.3930327399818113 |
| Heathcare Information and Technology | 430 | 1.2072494398821825 | 0.44922521399631615 |
| Homebuilding | 160 | 0.8223996026589195 | 0.31941662381436653 |
| Hospitals/Healthcare Facilities | 249 | 0.5838514857400334 | 0.3211521258092209 |
| Hotel/Gaming | 656 | 0.6562244487273435 | 0.33396483203511357 |
| Household Products | 588 | 0.7741444240060512 | 0.38720574164019406 |
| Information Services | 86 | 0.8737359462659163 | 0.35213732899248407 |
| Insurance (General) | 204 | 0.4730782196000951 | 0.30344791767045226 |
| Insurance (Life) | 143 | 0.7948484337173086 | 0.27197369976404934 |
| Insurance (Prop/Cas.) | 248 | 0.4123714259312061 | 0.2731161612742246 |
| Investments & Asset Management | 1315 | 0.5657130541049615 | 0.31967499146105743 |
| Machinery | 1553 | 1.329621716102589 | 0.3476117951484502 |
| Metals & Mining | 1874 | 1.1256104046768172 | 0.5369725988921057 |
| Office Equipment & Services | 139 | 0.7113013935053746 | 0.3073276571499566 |
| Oil/Gas (Integrated) | 34 | 0.6324676188577144 | 0.21436586122799883 |
| Oil/Gas (Production and Exploration) | 539 | 0.7463854591601625 | 0.4668950575338259 |
| Oil/Gas Distribution | 186 | 0.4611542527144429 | 0.3470959069593989 |
| Oilfield Svcs/Equip. | 431 | 0.7996508694362168 | 0.37153982370439825 |
| Packaging & Container | 438 | 0.5755524439641465 | 0.3190892683345648 |
| Paper/Forest Products | 271 | 0.6106540110372702 | 0.3058225168054844 |
| Power | 486 | 0.45529282820391004 | 0.26090179924789364 |
| Precious Metals | 777 | 1.3739381911113473 | 0.5774476192724218 |
| Publishing & Newspapers | 307 | 0.7787889630268272 | 0.31300237622202753 |
| R.E.I.T. | 643 | 0.3617107801017127 | 0.20507496140988338 |
| Real Estate (Development) | 895 | 0.4459430094478332 | 0.3517775631363108 |
| Real Estate (General/Diversified) | 312 | 0.5976415577929464 | 0.29199793865189955 |
| Real Estate (Operations & Services) | 752 | 0.5141243820700275 | 0.2986530056239502 |
| Recreation | 332 | 0.8899705656165486 | 0.3564674999139533 |
| Reinsurance | 32 | 0.9526677446916421 | 0.2533000659866368 |
| Restaurant/Dining | 410 | 0.6606263564759781 | 0.32411063646678384 |
| Retail (Automotive) | 212 | 0.6298056345182907 | 0.3492448330267457 |
| Retail (Building Supply) | 121 | 0.8046541261441439 | 0.30392105528642754 |
| Retail (Distributors) | 1079 | 0.6427870354354531 | 0.3515543473083488 |
| Retail (General) | 252 | 0.9372779491064982 | 0.31928519528088883 |
| Retail (Grocery and Food) | 215 | 0.6905168684866784 | 0.2967224894348833 |
| Retail (REITs) | 113 | 0.4073102020389581 | 0.1697504486086578 |
| Retail (Special Lines) | 649 | 0.9036386392039154 | 0.35469955420908994 |
| Rubber& Tires | 91 | 0.7807467415051133 | 0.2608595596123324 |
| Semiconductor | 675 | 1.8688970322549403 | 0.3833764930860169 |
| Semiconductor Equip | 391 | 2.117251565837131 | 0.3931431829987285 |
| Shipbuilding & Marine | 359 | 0.7871248113700747 | 0.3160614274568845 |
| Shoe | 84 | 0.8938187049899886 | 0.3540141632687013 |
| Software (Entertainment) | 298 | 1.2346330983114904 | 0.47175858576562024 |
| Software (Internet) | 150 | 1.3370400063421872 | 0.44721132362344007 |
| Software (System & Application) | 1532 | 1.3309502549413545 | 0.44582899699155365 |
| Steel | 719 | 0.929347814691143 | 0.3241430832805526 |
| Telecom (Wireless) | 101 | 0.6028420822440717 | 0.31192575831134417 |
| Telecom. Equipment | 437 | 1.2979321307103502 | 0.40513421304888086 |
| Telecom. Services | 283 | 0.49625571682046693 | 0.34455219956026784 |
| Tobacco | 48 | 0.3743139650447623 | 0.38628412838573833 |
| Transportation | 451 | 0.7474630967654462 | 0.32565768890856284 |
| Transportation (Railroads) | 54 | 0.5543601703442842 | 0.20850138596404777 |
| Trucking | 130 | 0.6772463794887177 | 0.37075515525660424 |
| Utility (General) | 52 | 0.3343806185124047 | 0.17953117113055364 |
| Utility (Water) | 106 | 0.44533853048776256 | 0.24683946382128158 |
| Total Market | 48156 | 0.8323164345801076 | 0.3690846372105525 |
| Total Market (without financials) | 43056 | 0.9553636779709899 | 0.37652009861171487 |

## Input Choices

| Effective |
|---|
| Marginal |
