---
title: "Betaglobal24"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal24.xls
---

# Betaglobal24

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal24.xls

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
| Advertising | 417 | 1.1534040974143316 | 0.42645981634762253 |
| Aerospace/Defense | 300 | 0.9592458275374192 | 0.3932733721745295 |
| Air Transport | 151 | 0.8509770865553573 | 0.3154871567160049 |
| Apparel | 1194 | 0.6945475539459525 | 0.3553991621759483 |
| Auto & Truck | 162 | 1.2454670699337789 | 0.4691776531589818 |
| Auto Parts | 780 | 1.1860429548696714 | 0.33648262296904313 |
| Bank (Money Center) | 621 | 0.38819075839525424 | 0.2145522965269891 |
| Banks (Regional) | 849 | 0.3260855684590195 | 0.20509278043746246 |
| Beverage (Alcoholic) | 216 | 0.7824704804320017 | 0.2937891901018008 |
| Beverage (Soft) | 101 | 0.5242439335980796 | 0.3932183209470126 |
| Broadcasting | 126 | 0.6997404590000051 | 0.36742463568719264 |
| Brokerage & Investment Banking | 606 | 0.40691610406824463 | 0.37072992131056787 |
| Building Materials | 462 | 0.9351769457144394 | 0.3056472652331514 |
| Business & Consumer Services | 974 | 0.9466428968969911 | 0.36020766248783903 |
| Cable TV | 45 | 0.5927824115414603 | 0.36130182671877753 |
| Chemical (Basic) | 897 | 0.9062574215064294 | 0.3382858718888727 |
| Chemical (Diversified) | 64 | 0.8414985656125796 | 0.25201032856137706 |
| Chemical (Specialty) | 951 | 0.9491995613739216 | 0.3509259830898305 |
| Coal & Related Energy | 216 | 1.2439498362512165 | 0.44265789598056415 |
| Computer Services | 1182 | 1.0478993848891942 | 0.3670076330333622 |
| Computers/Peripherals | 342 | 1.245363862313229 | 0.38550884901981475 |
| Construction Supplies | 804 | 0.8470454307375338 | 0.3260802452769085 |
| Diversified | 335 | 0.6957618910800656 | 0.25959979429842384 |
| Drugs (Biotechnology) | 1223 | 1.2283359269224818 | 0.5447442095224443 |
| Drugs (Pharmaceutical) | 1271 | 0.9745898681934191 | 0.42917448528109664 |
| Education | 272 | 0.7839677242385173 | 0.3869159200355736 |
| Electrical Equipment | 1101 | 1.1803222542231724 | 0.4167651773484566 |
| Electronics (Consumer & Office) | 125 | 1.120143588816069 | 0.41446538460572574 |
| Electronics (General) | 1480 | 1.362148498261915 | 0.3904437178780335 |
| Engineering/Construction | 1327 | 0.6635004693508927 | 0.3396104609742587 |
| Entertainment | 748 | 0.994831621963418 | 0.44782018019901776 |
| Environmental & Waste Services | 391 | 0.8561850090099775 | 0.39875270342990776 |
| Farming/Agriculture | 429 | 0.5577657009461505 | 0.33132271826396403 |
| Financial Svcs. (Non-bank & Insurance) | 1117 | 0.27332662724701895 | 0.36047318630458536 |
| Food Processing | 1424 | 0.5740786269842967 | 0.3124627608427594 |
| Food Wholesalers | 188 | 0.4407452827505263 | 0.33061017715979474 |
| Furn/Home Furnishings | 380 | 0.9515336189750979 | 0.3283244630702815 |
| Green & Renewable Energy | 260 | 0.5965934185310744 | 0.36059010237896605 |
| Healthcare Products | 850 | 1.0818372740131788 | 0.4315590510693509 |
| Healthcare Support Services | 480 | 0.7319797982129079 | 0.3950869651284412 |
| Heathcare Information and Technology | 435 | 1.1323979933703863 | 0.4554881481215059 |
| Homebuilding | 165 | 0.9498380268759352 | 0.3131728393220037 |
| Hospitals/Healthcare Facilities | 245 | 0.5883064625026934 | 0.3270501506545979 |
| Hotel/Gaming | 660 | 0.7425547325217814 | 0.3309288550615528 |
| Household Products | 554 | 0.827690238857905 | 0.3921296524074759 |
| Information Services | 85 | 0.9464430837097791 | 0.3654096265340622 |
| Insurance (General) | 199 | 0.5340488689542506 | 0.262737890833354 |
| Insurance (Life) | 137 | 0.8371398745434203 | 0.2638833041811696 |
| Insurance (Prop/Cas.) | 240 | 0.47760896326633245 | 0.29774136909912535 |
| Investments & Asset Management | 1291 | 0.5754031766639106 | 0.32604090359550036 |
| Machinery | 1548 | 1.1231976529603653 | 0.35026580007417235 |
| Metals & Mining | 1832 | 1.0069656077464937 | 0.5126780544824836 |
| Office Equipment & Services | 140 | 0.726901174263479 | 0.3078617872976938 |
| Oil/Gas (Integrated) | 36 | 0.8706638685596864 | 0.21252159476033355 |
| Oil/Gas (Production and Exploration) | 548 | 0.8940846039112385 | 0.4358159478473538 |
| Oil/Gas Distribution | 179 | 0.4715805206967589 | 0.315095048011025 |
| Oilfield Svcs/Equip. | 437 | 0.7694160775676291 | 0.3649575634591566 |
| Packaging & Container | 438 | 0.6113219057945549 | 0.3056406119903724 |
| Paper/Forest Products | 269 | 0.5872158590167443 | 0.3068414492143556 |
| Power | 492 | 0.42688976183478017 | 0.278644103786351 |
| Precious Metals | 823 | 1.1124097240530046 | 0.5174986674396027 |
| Publishing & Newspapers | 321 | 0.8406045732070051 | 0.3113590633550173 |
| R.E.I.T. | 650 | 0.4947802819320964 | 0.20886245828828479 |
| Real Estate (Development) | 879 | 0.43254668731756957 | 0.36538749566568085 |
| Real Estate (General/Diversified) | 309 | 0.5280921954877321 | 0.2867749882186602 |
| Real Estate (Operations & Services) | 749 | 0.5606596115492618 | 0.3054686189080664 |
| Recreation | 320 | 0.948689330043453 | 0.3406131843836307 |
| Reinsurance | 33 | 1.2011644079794304 | 0.2569404451098205 |
| Restaurant/Dining | 401 | 0.8137151461005107 | 0.32405295107468723 |
| Retail (Automotive) | 208 | 0.6744587900196068 | 0.34851313530166683 |
| Retail (Building Supply) | 117 | 0.850666789927349 | 0.2957367052271311 |
| Retail (Distributors) | 1038 | 0.6216641879998483 | 0.353892006295582 |
| Retail (General) | 253 | 1.0446962648672686 | 0.3180061258411659 |
| Retail (Grocery and Food) | 204 | 0.6199030998093494 | 0.2999395642888886 |
| Retail (REITs) | 121 | 0.6402076564701218 | 0.1807372554004395 |
| Retail (Special Lines) | 633 | 0.9621041645905499 | 0.3622289677109371 |
| Rubber& Tires | 92 | 0.7625237446734922 | 0.2777300835370454 |
| Semiconductor | 665 | 1.6615012677812717 | 0.40605620225004946 |
| Semiconductor Equip | 375 | 2.024719400785088 | 0.42049425794356066 |
| Shipbuilding & Marine | 357 | 0.7509275957778898 | 0.286442804607982 |
| Shoe | 82 | 0.7518926855457816 | 0.36833689482143356 |
| Software (Entertainment) | 311 | 1.257246465898575 | 0.45145413719770283 |
| Software (Internet) | 147 | 1.3184585053516902 | 0.43378524790668044 |
| Software (System & Application) | 1567 | 1.3063528424956525 | 0.46156822211430343 |
| Steel | 727 | 0.9372565803503431 | 0.325205536272085 |
| Telecom (Wireless) | 98 | 0.6679769651309979 | 0.2826622194349522 |
| Telecom. Equipment | 440 | 1.165935060463378 | 0.41988252733764636 |
| Telecom. Services | 274 | 0.5618146048803229 | 0.3313613112045757 |
| Tobacco | 54 | 0.4282813171571885 | 0.39604984981077457 |
| Transportation | 446 | 0.7082977055004389 | 0.3375699386015879 |
| Transportation (Railroads) | 54 | 0.6136198657999822 | 0.21529291287822042 |
| Trucking | 113 | 0.6974708715491826 | 0.34244575147149237 |
| Utility (General) | 52 | 0.42958227538616095 | 0.19732611741503459 |
| Utility (Water) | 106 | 0.40728791294174177 | 0.30294746896586655 |
| Tiotal Market | 47810 | 0.7947853744554728 | 0.3676949062719027 |
| Total Market (without financials) | 42750 | 0.9153763453587291 | 0.3757662749154231 |

## Input Choices

| Effective |
|---|
| Marginal |
