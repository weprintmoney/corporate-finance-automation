---
title: "Betas22"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas22.xls
---

# Betas22

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betas22.xls

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

| Date updated: | 44931.0 | YouTube Video explaining estimation choices and process. | Notes |
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
| Advertising | 58 | 1.3458926691301203 | 0.6867454020094217 |
| Aerospace/Defense | 77 | 1.2292962090923658 | 0.47207385668758833 |
| Air Transport | 21 | 0.6939980034393283 | 0.44026952881288556 |
| Apparel | 39 | 1.0163797426008965 | 0.5219832711715527 |
| Auto & Truck | 31 | 1.2255318343171395 | 0.6906352624443269 |
| Auto Parts | 37 | 1.202436458457679 | 0.5099287640392465 |
| Bank (Money Center) | 7 | 0.7393414305916117 | 0.22354726306204947 |
| Banks (Regional) | 557 | 0.4129806383970706 | 0.1756514255721121 |
| Beverage (Alcoholic) | 23 | 0.8807822917633785 | 0.5870582585990226 |
| Beverage (Soft) | 31 | 1.2014134916712005 | 0.6105213214406137 |
| Broadcasting | 26 | 0.7021599591713337 | 0.558392045026283 |
| Brokerage & Investment Banking | 30 | 0.6937505627531657 | 0.35452868010802446 |
| Building Materials | 45 | 1.0983592603350816 | 0.4207823750753867 |
| Business & Consumer Services | 164 | 1.0198687734730703 | 0.5384231377505506 |
| Cable TV | 10 | 0.7059202442851957 | 0.4067510262609936 |
| Chemical (Basic) | 38 | 0.9589900308465779 | 0.5269623558081643 |
| Chemical (Diversified) | 4 | 1.0902565654988166 | 0.4489238033488614 |
| Chemical (Specialty) | 76 | 1.1152530501630955 | 0.48818195945349135 |
| Coal & Related Energy | 19 | 1.4289145880963197 | 0.5502255669727574 |
| Computer Services | 80 | 0.9932217950326541 | 0.6052685974116296 |
| Computers/Peripherals | 42 | 1.227042372213005 | 0.4600212953010714 |
| Construction Supplies | 49 | 1.0760610533922743 | 0.4573409539780639 |
| Diversified | 23 | 0.9394964138236339 | 0.5643234779391457 |
| Drugs (Biotechnology) | 598 | 1.1994489579084946 | 0.6539990607514994 |
| Drugs (Pharmaceutical) | 281 | 1.1808060946282533 | 0.6919122536259916 |
| Education | 33 | 0.9937160802737702 | 0.5483166862101779 |
| Electrical Equipment | 110 | 1.4326548798323873 | 0.5944028755049212 |
| Electronics (Consumer & Office) | 16 | 1.6130596990178139 | 0.59618023652288 |
| Electronics (General) | 138 | 1.1161632606240839 | 0.5030761314415528 |
| Engineering/Construction | 43 | 1.0176246718468016 | 0.42193835857454437 |
| Entertainment | 110 | 1.2462224080092748 | 0.688274441827099 |
| Environmental & Waste Services | 62 | 0.8591109527629267 | 0.6156615678292375 |
| Farming/Agriculture | 39 | 0.9310497068082925 | 0.5890289174435183 |
| Financial Svcs. (Non-bank & Insurance) | 223 | 0.10617474510192053 | 0.33784250120258325 |
| Food Processing | 92 | 0.7686726756486479 | 0.4866088668527545 |
| Food Wholesalers | 14 | 0.8457047174503761 | 0.4792931471704661 |
| Furn/Home Furnishings | 32 | 0.9519122322245162 | 0.5483600453060752 |
| Green & Renewable Energy | 19 | 0.8771923185242169 | 0.6770603046757789 |
| Healthcare Products | 254 | 1.0971029719882097 | 0.5938554268008396 |
| Healthcare Support Services | 131 | 1.0725471879998554 | 0.5635984031690817 |
| Heathcare Information and Technology | 138 | 1.370736187816319 | 0.6172879220079127 |
| Homebuilding | 32 | 1.3331558308257836 | 0.41272083246912217 |
| Hospitals/Healthcare Facilities | 34 | 0.7230794758104835 | 0.6027909329624173 |
| Hotel/Gaming | 69 | 1.0609649277632753 | 0.4849956687865248 |
| Household Products | 127 | 1.0578798468783357 | 0.657658600910968 |
| Information Services | 73 | 1.3334436182933442 | 0.4768121512169421 |
| Insurance (General) | 21 | 1.0269385936275734 | 0.45212247290893337 |
| Insurance (Life) | 27 | 0.6674646710271233 | 0.37737813626902367 |
| Insurance (Prop/Cas.) | 51 | 0.7295385474975669 | 0.3527091878622686 |
| Investments & Asset Management | 600 | 0.5377530864305458 | 0.14993616815022495 |
| Machinery | 116 | 1.0938250803149925 | 0.4224065663042139 |
| Metals & Mining | 68 | 1.2191906966167014 | 0.6658049675950692 |
| Office Equipment & Services | 16 | 0.8448370751926576 | 0.4441949474746268 |
| Oil/Gas (Integrated) | 4 | 0.946268369906833 | 0.34410896982169686 |
| Oil/Gas (Production and Exploration) | 174 | 1.1361280842130776 | 0.5789642939989437 |
| Oil/Gas Distribution | 23 | 0.656489918658282 | 0.42358629907014234 |
| Oilfield Svcs/Equip. | 101 | 1.1869387038702228 | 0.5323266583847177 |
| Packaging & Container | 25 | 0.6704997219078969 | 0.3688793813718014 |
| Paper/Forest Products | 7 | 1.1258403034857074 | 0.6011566734952618 |
| Power | 48 | 0.4640263901945677 | 0.2556313254305959 |
| Precious Metals | 74 | 1.1872086171220402 | 0.6947327970793664 |
| Publishing & Newspapers | 20 | 0.9141555268995404 | 0.4606505763247093 |
| R.E.I.T. | 223 | 0.6855568332302365 | 0.3082774695650108 |
| Real Estate (Development) | 18 | 0.8838048274406524 | 0.5935560500176223 |
| Real Estate (General/Diversified) | 12 | 0.6649391588559308 | 0.5264619483249621 |
| Real Estate (Operations & Services) | 60 | 0.8050206047433183 | 0.5368798902000679 |
| Recreation | 57 | 1.0754929270701692 | 0.5939259548412263 |
| Reinsurance | 1 | 0.8316073808059627 | 0.20758239974021755 |
| Restaurant/Dining | 70 | 1.1660017105464549 | 0.4749197130090601 |
| Retail (Automotive) | 30 | 1.0827260845919955 | 0.4958162101500319 |
| Retail (Building Supply) | 15 | 1.5670419621739333 | 0.4708175159353282 |
| Retail (Distributors) | 69 | 1.00607436454125 | 0.46193491376213663 |
| Retail (General) | 15 | 1.2201002971574864 | 0.34600452314885843 |
| Retail (Grocery and Food) | 13 | 0.4731749077028324 | 0.44427105868248346 |
| Retail (Online) | 63 | 1.355989844350516 | 0.7024869327703446 |
| Retail (Special Lines) | 78 | 1.187876333197214 | 0.5087813282201621 |
| Rubber& Tires | 3 | 0.267665547396446 | 0.4502618640265363 |
| Semiconductor | 68 | 1.534267220206094 | 0.4893379233506794 |
| Semiconductor Equip | 30 | 1.6892473610771204 | 0.4351337345019169 |
| Shipbuilding & Marine | 8 | 0.7803339556376949 | 0.4893232382847557 |
| Shoe | 13 | 1.2886673829152329 | 0.5084634578495381 |
| Software (Entertainment) | 91 | 1.3578802103729628 | 0.6871552157284953 |
| Software (Internet) | 33 | 1.416511407810549 | 0.6605497248979673 |
| Software (System & Application) | 390 | 1.4129709426977197 | 0.6164066436646158 |
| Steel | 28 | 1.2125474928571525 | 0.39412504778160207 |
| Telecom (Wireless) | 16 | 0.7113584236080368 | 0.572471775665538 |
| Telecom. Equipment | 79 | 1.1784895771242725 | 0.5273300494301266 |
| Telecom. Services | 49 | 0.47390612503545576 | 0.5554026212509242 |
| Tobacco | 15 | 1.7442504521558875 | 0.6063488165394005 |
| Transportation | 18 | 0.9245938189921151 | 0.4789286178644412 |
| Transportation (Railroads) | 4 | 0.9323815338876874 | 0.22719138715983178 |
| Trucking | 35 | 1.232855746839977 | 0.4458153014104363 |
| Utility (General) | 15 | 0.4094617819876518 | 0.15608401947167233 |
| Utility (Water) | 16 | 0.8725208753424394 | 0.3655131913452527 |
| Total Market | 7165 | 0.884737434318496 | 0.4832448489852054 |
| Total Market (without financials) | 5649 | 1.1212181402625263 | 0.5575213805701925 |

## Inputs

| Effective |
|---|
| Marginal |
