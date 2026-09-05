---
title: "Betas23"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas23.xls
---

# Betas23

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas23.xls

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

| Date updated: | 45296.0 | YouTube Video explaining estimation choices and process. | Notes |
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
| Advertising | 57 | 1.1806104386629273 | 0.6203609804405511 |
| Aerospace/Defense | 70 | 0.9308535405948443 | 0.45844858400171823 |
| Air Transport | 25 | 0.6401880468304745 | 0.5220808406082641 |
| Apparel | 38 | 0.9295756500550167 | 0.4816041103429658 |
| Auto & Truck | 34 | 1.3040309184380587 | 0.7080593887098494 |
| Auto Parts | 39 | 1.1211038704345888 | 0.46516746954780275 |
| Bank (Money Center) | 15 | 0.644005117845298 | 0.310854706702379 |
| Banks (Regional) | 625 | 0.3333666067349679 | 0.23976240279666577 |
| Beverage (Alcoholic) | 19 | 0.9702633521273643 | 0.5269516786093021 |
| Beverage (Soft) | 29 | 0.7018333472111191 | 0.5618727576114821 |
| Broadcasting | 22 | 0.4997566745248037 | 0.5134328785449971 |
| Brokerage & Investment Banking | 27 | 0.550778221499521 | 0.32719370904363526 |
| Building Materials | 44 | 1.2090471865786552 | 0.3866043888390603 |
| Business & Consumer Services | 162 | 0.9296426574330118 | 0.4878307797023972 |
| Cable TV | 10 | 0.7356295403207628 | 0.41988100180216054 |
| Chemical (Basic) | 32 | 0.8746907847879827 | 0.4855275753494475 |
| Chemical (Diversified) | 4 | 0.8134608576935285 | 0.30122649893216696 |
| Chemical (Specialty) | 68 | 0.9381357434291198 | 0.4443482849456503 |
| Coal & Related Energy | 18 | 1.2427250283125129 | 0.5083741836491087 |
| Computer Services | 72 | 0.8586975071173775 | 0.575034920163967 |
| Computers/Peripherals | 36 | 1.1003543807483607 | 0.4389754758121167 |
| Construction Supplies | 45 | 0.9906432640326439 | 0.39771637369431545 |
| Diversified | 23 | 1.0923486152033832 | 0.5455257525139773 |
| Drugs (Biotechnology) | 572 | 1.089096469625617 | 0.6316706799599465 |
| Drugs (Pharmaceutical) | 245 | 0.9439976867785511 | 0.6616183587531324 |
| Education | 31 | 1.146739430936378 | 0.5404452903915143 |
| Electrical Equipment | 103 | 1.145843471951508 | 0.6199712415827232 |
| Electronics (Consumer & Office) | 13 | 1.3029636093516688 | 0.5283160489145928 |
| Electronics (General) | 129 | 0.8772051743933108 | 0.4869862189730259 |
| Engineering/Construction | 43 | 0.8446770651898954 | 0.4220680013423488 |
| Entertainment | 98 | 0.8657191928039559 | 0.6154437383552309 |
| Environmental & Waste Services | 57 | 0.7857301954805603 | 0.5505244740754728 |
| Farming/Agriculture | 42 | 0.7692133353509856 | 0.5790413601334238 |
| Financial Svcs. (Non-bank & Insurance) | 172 | 0.3219787507277045 | 0.41891965274480025 |
| Food Processing | 82 | 0.49587927161435114 | 0.4721851942459518 |
| Food Wholesalers | 14 | 0.735070446558385 | 0.4094434324519284 |
| Furn/Home Furnishings | 31 | 0.8611874852176121 | 0.4512480385385554 |
| Green & Renewable Energy | 17 | 0.5560860191551688 | 0.6005433175917523 |
| Healthcare Products | 230 | 1.0054180718910262 | 0.5729588590417255 |
| Healthcare Support Services | 119 | 0.9403062489496928 | 0.5222889598422624 |
| Heathcare Information and Technology | 128 | 1.1875339477983193 | 0.5607393583553072 |
| Homebuilding | 32 | 1.3535915929813263 | 0.4784755508502002 |
| Hospitals/Healthcare Facilities | 32 | 0.5599961069519285 | 0.5809408482779341 |
| Hotel/Gaming | 68 | 1.048189773353677 | 0.45543221641404846 |
| Household Products | 93 | 0.772920133759626 | 0.5665073661903348 |
| Information Services | 18 | 0.7723824914378383 | 0.4433144319691126 |
| Insurance (General) | 21 | 0.8946178159376359 | 0.4100110121652309 |
| Insurance (Life) | 23 | 0.5398311188838629 | 0.31323609058654894 |
| Insurance (Prop/Cas.) | 50 | 0.6752076172747652 | 0.29542222759979686 |
| Investments & Asset Management | 334 | 0.39129392968006665 | 0.23127931567629015 |
| Machinery | 103 | 0.9376095544061418 | 0.43145089570820533 |
| Metals & Mining | 68 | 0.9121243548326187 | 0.6448036956583449 |
| Office Equipment & Services | 17 | 0.8764328079953049 | 0.43862141616358896 |
| Oil/Gas (Integrated) | 4 | 0.6440450138393521 | 0.1559122229892095 |
| Oil/Gas (Production and Exploration) | 166 | 0.8214204967594376 | 0.5028065151873572 |
| Oil/Gas Distribution | 24 | 0.529121571269841 | 0.35814240603030073 |
| Oilfield Svcs/Equip. | 100 | 0.8529017381494012 | 0.47764888389529203 |
| Packaging & Container | 22 | 0.8068658605326057 | 0.28511922568861303 |
| Paper/Forest Products | 7 | 1.5902925666995296 | 0.44887720297805234 |
| Power | 50 | 0.3885061927976376 | 0.2731850789071314 |
| Precious Metals | 61 | 0.8300839147546547 | 0.6277710399382218 |
| Publishing & Newspapers | 21 | 0.8229834620810547 | 0.3761107560880043 |
| R.E.I.T. | 193 | 0.6600635421243216 | 0.2785202217982606 |
| Real Estate (Development) | 17 | 0.4314363177605709 | 0.5888176551236093 |
| Real Estate (General/Diversified) | 11 | 0.5125267518181463 | 0.34765379629256593 |
| Real Estate (Operations & Services) | 60 | 0.8828463853207577 | 0.4821337106090897 |
| Recreation | 55 | 0.8488780060557483 | 0.508398195758929 |
| Reinsurance | 1 | 0.6098509183978317 | 0.17019306608141013 |
| Restaurant/Dining | 64 | 1.0243276951296387 | 0.4028461029765301 |
| Retail (Automotive) | 30 | 1.0587643053346871 | 0.497412548478118 |
| Retail (Building Supply) | 16 | 1.704153179546406 | 0.40867290849107046 |
| Retail (Distributors) | 62 | 0.9093255538405173 | 0.43779976150526184 |
| Retail (General) | 26 | 1.171062908717729 | 0.41851033405292054 |
| Retail (Grocery and Food) | 14 | 0.364761149065977 | 0.37864030098436763 |
| Retail (REITs) | 28 | 0.7866747019034875 | 0.23396716194282416 |
| Retail (Special Lines) | 105 | 0.9730692183120843 | 0.5097966651901066 |
| Rubber& Tires | 3 | 0.26316933125019143 | 0.3449361948988834 |
| Semiconductor | 63 | 1.460244593924559 | 0.45354710772446294 |
| Semiconductor Equip | 30 | 1.5077650793777069 | 0.37660583764014344 |
| Shipbuilding & Marine | 8 | 0.686594972052408 | 0.3448217898647169 |
| Shoe | 13 | 1.2730955389810585 | 0.46725927842402937 |
| Software (Entertainment) | 84 | 1.1136804709373258 | 0.610172951451298 |
| Software (Internet) | 35 | 1.5117563379021286 | 0.5394406814483563 |
| Software (System & Application) | 351 | 1.2724589938133573 | 0.5847613852327183 |
| Steel | 29 | 1.0774711199709137 | 0.3620295896390823 |
| Telecom (Wireless) | 13 | 0.7473117190554889 | 0.6312614197086591 |
| Telecom. Equipment | 66 | 1.045647985265377 | 0.564690125662547 |
| Telecom. Services | 42 | 0.4141115560097563 | 0.5661747746150435 |
| Tobacco | 16 | 0.9870802250148996 | 0.5791550827639212 |
| Transportation | 36 | 1.046594408036378 | 0.6204218561309859 |
| Transportation (Railroads) | 4 | 0.8559978059315445 | 0.18679691462453912 |
| Trucking | 22 | 1.029154942745124 | 0.34295428248124715 |
| Utility (General) | 14 | 0.3567951929109757 | 0.15052959253451076 |
| Utility (Water) | 13 | 0.5223114719862922 | 0.2951453785165835 |
| Total Market | 6481 | 0.7903856717545845 | 0.472160922709717 |
| Total Market (without financials) | 5214 | 0.972267805446803 | 0.5210661954664575 |

## Inputs

| Effective |
|---|
| Marginal |
