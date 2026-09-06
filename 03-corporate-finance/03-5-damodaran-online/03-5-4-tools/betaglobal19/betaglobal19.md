---
title: "Betaglobal19"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal19.xls
---

# Betaglobal19

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal19.xls

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
| Industry Name | Number of firms | Unlevered beta corrected for cash | HiLo Risk |
| Advertising | 312 | 0.9574823050721607 | 0.41189981579069157 |
| Aerospace/Defense | 238 | 1.0534298484987918 | 0.35903956803948117 |
| Air Transport | 159 | 0.6515673034236119 | 0.291836205457142 |
| Apparel | 1161 | 0.7003749710772871 | 0.3469067649311425 |
| Auto & Truck | 134 | 0.8540589604698049 | 0.33643823465249867 |
| Auto Parts | 682 | 1.1114233776958204 | 0.32334937052559676 |
| Bank (Money Center) | 595 | 0.40180142660318724 | 0.206877835903436 |
| Banks (Regional) | 862 | 0.46490532394693235 | 0.16734280713712707 |
| Beverage (Alcoholic) | 216 | 0.800587637762375 | 0.29704091584705095 |
| Beverage (Soft) | 94 | 0.7092893218236829 | 0.4070049296103608 |
| Broadcasting | 138 | 0.6852414284825481 | 0.33925682898857024 |
| Brokerage & Investment Banking | 559 | 0.43664122018957785 | 0.34227377137469683 |
| Building Materials | 426 | 0.8298498654246875 | 0.2923880749391902 |
| Business & Consumer Services | 868 | 0.8804229892151988 | 0.35829785318929797 |
| Cable TV | 61 | 0.7910340681937198 | 0.33442848538784503 |
| Chemical (Basic) | 793 | 0.9032860152963472 | 0.3022524069789313 |
| Chemical (Diversified) | 73 | 0.952334541660416 | 0.2926613538900447 |
| Chemical (Specialty) | 829 | 0.9818941076738789 | 0.337008023250152 |
| Coal & Related Energy | 224 | 1.274443681628482 | 0.44295571342273693 |
| Computer Services | 969 | 0.9806480666532279 | 0.3466197897913061 |
| Computers/Peripherals | 332 | 1.3493071035123267 | 0.3581877316252688 |
| Construction Supplies | 747 | 0.9561705566543145 | 0.30933081931222156 |
| Diversified | 319 | 0.6908015362797085 | 0.26040219624017996 |
| Drugs (Biotechnology) | 1024 | 1.4024111440166125 | 0.5222440815010535 |
| Drugs (Pharmaceutical) | 1263 | 1.1985080632950982 | 0.4549487118411232 |
| Education | 211 | 1.0234807764447162 | 0.38159618422673924 |
| Electrical Equipment | 902 | 1.146287349436663 | 0.37094890748738085 |
| Electronics (Consumer & Office) | 142 | 1.300002808253641 | 0.38721375247271694 |
| Electronics (General) | 1345 | 1.3817241330917154 | 0.3521841180649659 |
| Engineering/Construction | 1208 | 0.8099875352902434 | 0.32670768262187977 |
| Entertainment | 660 | 1.170486437164519 | 0.44143551676552706 |
| Environmental & Waste Services | 325 | 1.0108895954007615 | 0.4335448178157985 |
| Farming/Agriculture | 406 | 0.6004760571400259 | 0.34387720986795034 |
| Financial Svcs. (Non-bank & Insurance) | 1059 | 0.14956422652348697 | 0.3078967543811639 |
| Food Processing | 1262 | 0.6501170844484848 | 0.30570346529736997 |
| Food Wholesalers | 151 | 0.5184929633658631 | 0.30291991703945215 |
| Furn/Home Furnishings | 328 | 1.0058522471944715 | 0.3106262109541846 |
| Green & Renewable Energy | 213 | 0.5867303342285284 | 0.37960075010123556 |
| Healthcare Products | 739 | 1.1331289139797711 | 0.42665918437428163 |
| Healthcare Support Services | 402 | 0.8183860919317326 | 0.3842183770815967 |
| Heathcare Information and Technology | 389 | 1.225383329091867 | 0.46185033337051073 |
| Homebuilding | 167 | 0.7482870371272902 | 0.3004410971982021 |
| Hospitals/Healthcare Facilities | 206 | 0.5039735140504044 | 0.30448522546360524 |
| Hotel/Gaming | 639 | 0.6849051024844033 | 0.31019049483429584 |
| Household Products | 536 | 0.9641176499316831 | 0.4064485911442966 |
| Information Services | 215 | 1.0458294791273943 | 0.4046913892035054 |
| Insurance (General) | 216 | 0.5355173012771018 | 0.21765758320878703 |
| Insurance (Life) | 137 | 0.9778481143959333 | 0.22662634158819878 |
| Insurance (Prop/Cas.) | 223 | 0.5023697504648265 | 0.2350816643532549 |
| Investments & Asset Management | 1066 | 0.5492734103196246 | 0.30702877489597685 |
| Machinery | 1332 | 1.164533521118772 | 0.30572189833550784 |
| Metals & Mining | 1529 | 1.094059867642693 | 0.49319278795662597 |
| Office Equipment & Services | 146 | 0.9376447183289379 | 0.3306309023418529 |
| Oil/Gas (Integrated) | 49 | 1.1401792895983085 | 0.24014262969256495 |
| Oil/Gas (Production and Exploration) | 773 | 1.144320485233247 | 0.5469529226526685 |
| Oil/Gas Distribution | 160 | 0.826498511667143 | 0.3293910088798522 |
| Oilfield Svcs/Equip. | 508 | 1.0641191695035244 | 0.4192932075460661 |
| Packaging & Container | 400 | 0.607320943408075 | 0.3217584187796059 |
| Paper/Forest Products | 279 | 0.7409056418529129 | 0.32887513187994566 |
| Power | 538 | 0.5050604986216313 | 0.2538658262096573 |
| Precious Metals | 844 | 0.9983432046775572 | 0.5153991275625832 |
| Publishing & Newspapers | 352 | 0.8520217460955231 | 0.32444513180133205 |
| R.E.I.T. | 753 | 0.34523746097470087 | 0.17797586423324738 |
| Real Estate (Development) | 842 | 0.6358633022030139 | 0.30747746251601255 |
| Real Estate (General/Diversified) | 383 | 0.6422762383369989 | 0.2742448290945108 |
| Real Estate (Operations & Services) | 691 | 0.49377906135395283 | 0.2844744547806594 |
| Recreation | 315 | 0.8382133778789966 | 0.34885152123107005 |
| Reinsurance | 34 | 0.9199037070292533 | 0.25041359165822985 |
| Restaurant/Dining | 376 | 0.6672003450972904 | 0.3143830158591672 |
| Retail (Automotive) | 184 | 0.6624157829951878 | 0.32710840907535593 |
| Retail (Building Supply) | 93 | 0.9029009394098382 | 0.32156193483630624 |
| Retail (Distributors) | 982 | 0.6005287068795987 | 0.333115792771043 |
| Retail (General) | 210 | 0.8551483194122819 | 0.26504302735783664 |
| Retail (Grocery and Food) | 170 | 0.4949379666364981 | 0.24504955313005197 |
| Retail (Online) | 297 | 1.2321072795638826 | 0.4502542187632075 |
| Retail (Special Lines) | 479 | 0.748552841735843 | 0.3450477945125462 |
| Rubber& Tires | 89 | 0.7209670456185789 | 0.2752051629014338 |
| Semiconductor | 542 | 1.5295820455595976 | 0.3540806469887887 |
| Semiconductor Equip | 291 | 1.8210806223726346 | 0.3651854816509088 |
| Shipbuilding & Marine | 345 | 0.7084029347843069 | 0.2874763872091222 |
| Shoe | 78 | 0.8988600127419092 | 0.34760149597771733 |
| Software (Entertainment) | 280 | 1.1764313768041483 | 0.4843374267685716 |
| Software (Internet) | 131 | 1.2196848734436523 | 0.42480383438252456 |
| Software (System & Application) | 1375 | 1.2452889901094526 | 0.46335235413533327 |
| Steel | 695 | 0.8225064191450808 | 0.3356938162867985 |
| Telecom (Wireless) | 103 | 0.6093112277506092 | 0.30632537412017213 |
| Telecom. Equipment | 474 | 1.2655330245200576 | 0.3856177904815678 |
| Telecom. Services | 317 | 0.5867609941641149 | 0.37773193466490024 |
| Tobacco | 54 | 0.8656273334860688 | 0.37235622403297347 |
| Transportation | 265 | 0.7940858113757814 | 0.30385805225251095 |
| Transportation (Railroads) | 52 | 0.8272689994346133 | 0.20715508709224278 |
| Trucking | 208 | 0.6540174358423104 | 0.28282474993862783 |
| Utility (General) | 52 | 0.4140902432736007 | 0.17636661315204563 |
| Utility (Water) | 99 | 0.6932375070101038 | 0.2867080996663667 |
| Total Market | 44394 | 0.7943600161914623 | 0.3533752249278793 |
| Total Market (without financials) | 39677 | 0.9155482793342168 | 0.3640705318014177 |

## Input Choices

| Effective |
|---|
| Marginal |
