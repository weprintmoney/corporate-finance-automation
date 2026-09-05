---
title: "Betaemerg"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaemerg.xls
---

# Betaemerg

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaemerg.xls

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
| Advertising | 184 | 1.2809853688611113 | 0.21246107385827917 |
| Aerospace/Defense | 151 | 1.2562692644526494 | 0.3724194665085091 |
| Air Transport | 79 | 0.5918007979154652 | 2.5267325345289247 |
| Apparel | 993 | 0.6661863294930219 | 0.24383264453975834 |
| Auto & Truck | 89 | 1.2171574349263523 | 0.4737045351278563 |
| Auto Parts | 592 | 1.466893265486387 | 0.17900659882065958 |
| Bank (Money Center) | 455 | 0.3042765346340089 | 0.22494793119089798 |
| Banks (Regional) | 104 | 0.1367004666369731 | 2.155495595141906 |
| Beverage (Alcoholic) | 132 | 0.9529745756365909 | 0.33371561462503363 |
| Beverage (Soft) | 40 | 0.5795249019159485 | 0.463960111030658 |
| Broadcasting | 63 | 0.8562247437111076 | 0.39363709153615145 |
| Brokerage & Investment Banking | 468 | 0.42415921507281446 | 0.5245528836164461 |
| Building Materials | 281 | 0.8906827154957453 | 0.3046079535527801 |
| Business & Consumer Services | 379 | 1.1108084033013805 | 0.14920350318950953 |
| Cable TV | 29 | 1.0277435831726425 | 1.1027137916366585 |
| Chemical (Basic) | 741 | 1.0605126494627473 | 0.4397603478497234 |
| Chemical (Diversified) | 29 | 0.8594128706321852 | 0.35558128439030245 |
| Chemical (Specialty) | 687 | 1.1061483277420343 | 0.5569557932419357 |
| Coal & Related Energy | 96 | 0.9674443666307335 | 0.6014228505804987 |
| Computer Services | 693 | 1.082243993454939 | 0.2210635872979819 |
| Computers/Peripherals | 244 | 1.6177756841435402 | 0.3391503610200605 |
| Construction Supplies | 580 | 0.9062103275500444 | 0.3373815445355407 |
| Diversified | 215 | 0.4303834170775743 | 0.19575577551380796 |
| Drugs (Biotechnology) | 382 | 1.4134239857758604 | 1.5218152270647998 |
| Drugs (Pharmaceutical) | 753 | 1.0503243645309164 | 0.1504895559253604 |
| Education | 182 | 0.7702012115504218 | 0.32035244347738967 |
| Electrical Equipment | 810 | 1.450411044457564 | 0.4875513007200769 |
| Electronics (Consumer & Office) | 81 | 1.2062914184062385 | 0.2924297579211149 |
| Electronics (General) | 1050 | 1.7235389543933388 | 0.3102578637306701 |
| Engineering/Construction | 999 | 0.6129492893412035 | 0.24343120817490982 |
| Entertainment | 343 | 1.2157824560972854 | 0.211448620629568 |
| Environmental & Waste Services | 223 | 0.8903722053474792 | 0.27489897017244574 |
| Farming/Agriculture | 312 | 0.4980007225357512 | 0.30326637865056383 |
| Financial Svcs. (Non-bank & Insurance) | 697 | 0.4041432228424281 | 0.3678043601456678 |
| Food Processing | 1030 | 0.6083270541935392 | 0.23471711041975632 |
| Food Wholesalers | 121 | 0.4329688910946347 | 0.30308518076706525 |
| Furn/Home Furnishings | 278 | 1.1059227309079382 | 0.2808726269074557 |
| Green & Renewable Energy | 154 | 0.5905521274856151 | 0.33140774067439527 |
| Healthcare Products | 380 | 1.433943645116322 | 0.7985964973422124 |
| Healthcare Support Services | 256 | 0.7784511725870926 | 0.26617862736526277 |
| Heathcare Information and Technology | 146 | 1.5622762899525076 | 0.700694736060963 |
| Homebuilding | 46 | 0.5058672901088846 | 1.0483665938966304 |
| Hospitals/Healthcare Facilities | 164 | 0.6460670085977334 | 0.42803066966489745 |
| Hotel/Gaming | 427 | 0.5798020247434328 | 1.2123413179021856 |
| Household Products | 339 | 0.8210138715374586 | 0.13326210055473234 |
| Information Services | 49 | 1.029130246145059 | 0.2728749108903318 |
| Insurance (General) | 140 | 0.3638389604908368 | 0.24034705589138547 |
| Insurance (Life) | 92 | 0.7043001184648876 | 0.2500459938421822 |
| Insurance (Prop/Cas.) | 158 | 0.33150653155372817 | 0.35206828061305556 |
| Investments & Asset Management | 486 | 0.41460204659548344 | 0.5346390541220288 |
| Machinery | 987 | 1.4955690434570708 | 0.35022363090811914 |
| Metals & Mining | 358 | 1.4017831440655648 | 0.5266207718109674 |
| Office Equipment & Services | 78 | 0.7791548243979408 | 0.27970020789939354 |
| Oil/Gas (Integrated) | 15 | 0.742613875689985 | 0.48803102298756396 |
| Oil/Gas (Production and Exploration) | 105 | 0.8134379731628218 | 0.6986138452365959 |
| Oil/Gas Distribution | 120 | 0.4898179652388992 | 0.3786921067018167 |
| Oilfield Svcs/Equip. | 228 | 0.7884115659170906 | 0.4956079576643336 |
| Packaging & Container | 341 | 0.6123989280219638 | 0.15635986502455912 |
| Paper/Forest Products | 197 | 0.5626142683729399 | 0.3050653906850666 |
| Power | 328 | 0.4609920141214062 | 0.19761000736577836 |
| Precious Metals | 64 | 1.4989077994705398 | 0.6577947112203587 |
| Publishing & Newspapers | 171 | 1.0076064976928458 | 0.09726986877085089 |
| R.E.I.T. | 208 | 0.3215370033228604 | 0.2660352149065346 |
| Real Estate (Development) | 786 | 0.452215520616785 | 0.5019726842746028 |
| Real Estate (General/Diversified) | 205 | 0.7193019962954033 | 0.20499022468773326 |
| Real Estate (Operations & Services) | 406 | 0.5898101464704868 | 0.14037829316248862 |
| Recreation | 158 | 0.9949165193195968 | 0.21663146123428448 |
| Reinsurance | 27 | 0.904260494375423 | 0.7007432580203984 |
| Restaurant/Dining | 184 | 0.8179701636559041 | 1.3211385446737254 |
| Retail (Automotive) | 122 | 0.5827612239859625 | 0.27899335641149814 |
| Retail (Building Supply) | 55 | 0.6639968073344463 | 0.1876179282082812 |
| Retail (Distributors) | 731 | 0.5327070760460003 | 0.35948159517059913 |
| Retail (General) | 147 | 0.8901685363181931 | 0.1735564824189049 |
| Retail (Grocery and Food) | 97 | 0.8562153656648939 | 0.164400153244494 |
| Retail (REITs) | 39 | 0.4277486522911941 | 0.14469940229785072 |
| Retail (Special Lines) | 282 | 0.8532840920548314 | 0.2738276728908849 |
| Rubber& Tires | 72 | 0.7899230792444669 | 0.3221696154204394 |
| Semiconductor | 546 | 1.9759034943373723 | 0.4596642656935485 |
| Semiconductor Equip | 300 | 2.0865952011759936 | 0.6561314867469624 |
| Shipbuilding & Marine | 252 | 0.8427506421507318 | 1.0509786198396125 |
| Shoe | 60 | 0.7888374534424963 | 0.2595916128534623 |
| Software (Entertainment) | 67 | 1.5066104807142138 | 0.4636819163261826 |
| Software (Internet) | 49 | 1.3291908498747178 | 0.49607319386883797 |
| Software (System & Application) | 548 | 1.639660103124549 | 0.5955633640643428 |
| Steel | 555 | 0.9301361977882723 | 0.5819421821169715 |
| Telecom (Wireless) | 68 | 0.6684435056475432 | 0.10821191433593155 |
| Telecom. Equipment | 296 | 1.5148775938475338 | 0.21501185820641944 |
| Telecom. Services | 142 | 0.6141251965428087 | 0.06657594749857722 |
| Tobacco | 30 | 0.2305353323131311 | 0.22764682040521927 |
| Transportation | 330 | 0.7937991068388717 | 0.2405811636538192 |
| Transportation (Railroads) | 18 | 0.8872775915809581 | 0.23783723818467467 |
| Trucking | 76 | 0.36738084292150314 | 0.5867554272791906 |
| Utility (General) | 14 | 0.5724743533012847 | 0.41473866426605877 |
| Utility (Water) | 76 | 0.4728514212827937 | 0.18823466327545008 |
| Total Market | 27360 | 0.8479005017168175 | 0.24293442627557077 |
| Total Market (without financials) | 24760 | 0.9877994206071099 | 0.24920555130812153 |

## Input Choices

| Effective |
|---|
| Marginal |
