---
title: "Betas20"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas20.xls
---

# Betas20

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas20.xls

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

| Date updated: | 44201.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | if you are looking for a pure-play beta, i.e., a beta for a  business, the unlevered beta corrected for cash is your best bet. Since even sector betas can move over time, I have also reported the average of the this sector beta across time in the last column. This number, for obvious reasons, is less likely to be volatile over time. |
| What is this data? | Beta, Unlevered beta and other risk measures |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Do you want to use marginal or effective tax rates in unlevering betas? |  |  |  |
| If marginal tax rate, enter the marginal tax rate to use |  |  |  |
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 61 | 0.7710888722246941 | 0.7654179426038674 |
| Aerospace/Defense | 72 | 0.9103025999155656 | 0.5939983545128922 |
| Air Transport | 17 | 0.9137325131809052 | 0.654277792416702 |
| Apparel | 51 | 0.9388644583027517 | 0.6549355853398428 |
| Auto & Truck | 19 | 1.0472517867264415 | 0.7160330517933527 |
| Auto Parts | 52 | 1.091845771962285 | 0.6981220208347135 |
| Bank (Money Center) | 7 | 0.5941448338327675 | 0.34105410173881756 |
| Banks (Regional) | 598 | 0.5979069759936423 | 0.33050521986812614 |
| Beverage (Alcoholic) | 23 | 0.6748569072566616 | 0.6156343264761407 |
| Beverage (Soft) | 41 | 0.7063079859174041 | 0.7604891113952991 |
| Broadcasting | 29 | 0.6497178189669959 | 0.6274609763231741 |
| Brokerage & Investment Banking | 39 | 0.5727437184612131 | 0.6202460920435083 |
| Building Materials | 42 | 0.9684967527337779 | 0.5248142000353953 |
| Business & Consumer Services | 169 | 0.8285116002563457 | 0.6474000890351246 |
| Cable TV | 13 | 0.6982205235535328 | 0.4218908204610394 |
| Chemical (Basic) | 48 | 0.7591788658675822 | 0.6892014660514049 |
| Chemical (Diversified) | 5 | 1.0324036655167612 | 0.5311759398367519 |
| Chemical (Specialty) | 97 | 0.8166923465684208 | 0.612967400028414 |
| Coal & Related Energy | 29 | 0.5594524496194488 | 0.7276065707572446 |
| Computer Services | 116 | 0.9376812492225349 | 0.6799466162123905 |
| Computers/Peripherals | 52 | 1.1385519827896617 | 0.6473677007041652 |
| Construction Supplies | 46 | 0.8701154085863171 | 0.5214077058097009 |
| Diversified | 29 | 0.8910295956839558 | 0.6070101106392262 |
| Drugs (Biotechnology) | 547 | 0.8504659203376359 | 0.6268843356537072 |
| Drugs (Pharmaceutical) | 287 | 0.8361109611877694 | 0.6895665864028978 |
| Education | 38 | 1.0687032598564232 | 0.6972376680814039 |
| Electrical Equipment | 122 | 1.0001547798510189 | 0.7198507271578982 |
| Electronics (Consumer & Office) | 22 | 1.0100437842578767 | 0.6915080760914007 |
| Electronics (General) | 157 | 0.8572955659107067 | 0.6440954277403236 |
| Engineering/Construction | 61 | 0.9536904561931626 | 0.6438464447241811 |
| Entertainment | 118 | 0.8377594779575973 | 0.7648102947870344 |
| Environmental & Waste Services | 86 | 0.8204162405695642 | 0.70960994496677 |
| Farming/Agriculture | 32 | 0.6840937503175636 | 0.618492555475789 |
| Financial Svcs. (Non-bank & Insurance) | 235 | 0.10798894805453771 | 0.46387566776720224 |
| Food Processing | 101 | 0.5308887682515312 | 0.5417512975407125 |
| Food Wholesalers | 18 | 0.8038954894148037 | 0.6916148191358662 |
| Furn/Home Furnishings | 40 | 0.7776428982019439 | 0.6664438133366685 |
| Green & Renewable Energy | 25 | 0.6761958764160676 | 0.7945530818550454 |
| Healthcare Products | 265 | 0.8002022222608018 | 0.6221101589704446 |
| Healthcare Support Services | 129 | 0.7371571051279667 | 0.6309651954636044 |
| Heathcare Information and Technology | 139 | 0.7527762913735137 | 0.6295525024529605 |
| Homebuilding | 30 | 1.3259837174034685 | 0.5903255637328056 |
| Hospitals/Healthcare Facilities | 32 | 0.8036971111274536 | 0.6524855637002389 |
| Hotel/Gaming | 66 | 1.185661145872991 | 0.6531532913856745 |
| Household Products | 140 | 0.6829888736707932 | 0.7334142436985648 |
| Information Services | 77 | 0.9738762809653971 | 0.5867854689639354 |
| Insurance (General) | 21 | 0.557260794904117 | 0.470680847803128 |
| Insurance (Life) | 26 | 0.6409138936431259 | 0.4602913380839497 |
| Insurance (Prop/Cas.) | 55 | 0.5771327057138407 | 0.3842832774161052 |
| Investments & Asset Management | 348 | 0.7826182854438009 | 0.3588647668585568 |
| Machinery | 125 | 0.9562187966780408 | 0.5858276519757403 |
| Metals & Mining | 86 | 0.8177002612599934 | 0.786793821073182 |
| Office Equipment & Services | 22 | 0.8317441520313311 | 0.5706682538892344 |
| Oil/Gas (Integrated) | 3 | 0.9849549282165613 | 0.5036081922347394 |
| Oil/Gas (Production and Exploration) | 278 | 0.807476269260952 | 0.7658799624536865 |
| Oil/Gas Distribution | 57 | 0.5990773337393823 | 0.6544263919631939 |
| Oilfield Svcs/Equip. | 135 | 0.8315679089948197 | 0.7390340293501936 |
| Packaging & Container | 26 | 0.6800177986599872 | 0.456745151534667 |
| Paper/Forest Products | 15 | 0.9567360970451246 | 0.6175596355736828 |
| Power | 55 | 0.42904254661801955 | 0.36666160420037636 |
| Precious Metals | 93 | 0.7519210353077672 | 0.7766102895366132 |
| Publishing & Newspapers | 29 | 1.1021787350991707 | 0.5486440294344852 |
| R.E.I.T. | 238 | 0.7909575114731606 | 0.4901381999964605 |
| Real Estate (Development) | 25 | 0.5613812080555378 | 0.6851812081285757 |
| Real Estate (General/Diversified) | 11 | 0.7572797814294242 | 0.551518936088245 |
| Real Estate (Operations & Services) | 61 | 0.7538201743633561 | 0.6408490470730628 |
| Recreation | 69 | 0.7728221805426699 | 0.7368304008091368 |
| Reinsurance | 2 | 1.1258535728897527 | 0.4134600841939994 |
| Restaurant/Dining | 79 | 1.108327484346018 | 0.6957319764650596 |
| Retail (Automotive) | 30 | 0.9868233185911015 | 0.6173583563825168 |
| Retail (Building Supply) | 15 | 1.434459107150366 | 0.710667391104773 |
| Retail (Distributors) | 85 | 0.7522490597651373 | 0.6391406988267885 |
| Retail (General) | 17 | 0.8145075902919426 | 0.5433387877305249 |
| Retail (Grocery and Food) | 14 | 0.1514885766227531 | 0.4889764853912825 |
| Retail (Online) | 75 | 1.137018745081734 | 0.7481145311835655 |
| Retail (Special Lines) | 85 | 1.0336435224101186 | 0.6682550802909896 |
| Rubber& Tires | 3 | 0.5443582788933189 | 0.6340367944792071 |
| Semiconductor | 70 | 0.9609451707212839 | 0.5537144030375787 |
| Semiconductor Equip | 40 | 1.0681449570050152 | 0.5698417411837221 |
| Shipbuilding & Marine | 11 | 0.7413581059803034 | 0.5539639015042135 |
| Shoe | 11 | 0.9777184579800949 | 0.5756525665919513 |
| Software (Entertainment) | 101 | 0.9593307887724071 | 0.748928181889028 |
| Software (Internet) | 36 | 0.7484427343469626 | 0.6398388775616333 |
| Software (System & Application) | 388 | 0.893523270947977 | 0.6701733827684629 |
| Steel | 32 | 0.7823388982067156 | 0.5662329781380584 |
| Telecom (Wireless) | 16 | 0.3915247608328613 | 0.6234100586989396 |
| Telecom. Equipment | 96 | 0.8312241143236075 | 0.6388556358870728 |
| Telecom. Services | 58 | 0.41991925363355853 | 0.6187466729591025 |
| Tobacco | 15 | 0.6113882106935226 | 0.654063117065604 |
| Transportation | 21 | 0.7851895775316772 | 0.5863650895323865 |
| Transportation (Railroads) | 6 | 0.7398880209239251 | 0.5022316278338109 |
| Trucking | 35 | 0.9437673873471254 | 0.6119852488965275 |
| Utility (General) | 16 | 0.48355137178803176 | 0.2815597656010604 |
| Utility (Water) | 17 | 0.571349563878657 | 0.45013191866656144 |
| Total Market | 7582 | 0.7458330808898506 | 0.6017425581018515 |
| Total Market (without financials) | 6253 | 0.8601889077107179 | 0.6494978097075366 |

## Inputs

| Effective |
|---|
| Marginal |
