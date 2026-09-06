---
title: "Betaglobal18"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal18.xls
---

# Betaglobal18

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal18.xls

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
| Advertising | 303 | 0.9136923477867658 | 0.4396413093987327 |
| Aerospace/Defense | 234 | 1.0569406646334956 | 0.3964095441635619 |
| Air Transport | 162 | 0.5942202018191366 | 0.31951440226938216 |
| Apparel | 1148 | 0.7487595079985668 | 0.3728350752675562 |
| Auto & Truck | 133 | 0.8016912770661271 | 0.3387828649930809 |
| Auto Parts | 681 | 1.0858928225770144 | 0.3654528695584084 |
| Bank (Money Center) | 617 | 0.38392646777645967 | 0.24160672334377578 |
| Banks (Regional) | 872 | 0.46600710739863394 | 0.2064289854536609 |
| Beverage (Alcoholic) | 220 | 0.7959728564953452 | 0.31935807259471616 |
| Beverage (Soft) | 97 | 0.6755843630131199 | 0.3988238323583305 |
| Broadcasting | 135 | 0.6103725894232909 | 0.3630042306001429 |
| Brokerage & Investment Banking | 553 | 0.42119202782012716 | 0.3710111751586773 |
| Building Materials | 416 | 0.813578860866948 | 0.3324980025700573 |
| Business & Consumer Services | 850 | 0.9215650049807711 | 0.3940826993926521 |
| Cable TV | 60 | 0.7164810703734728 | 0.3453842753257326 |
| Chemical (Basic) | 785 | 0.9505393595920643 | 0.3476262403962364 |
| Chemical (Diversified) | 71 | 0.9586996619107844 | 0.31630808202119265 |
| Chemical (Specialty) | 811 | 1.0359122277535977 | 0.35850008747526585 |
| Coal & Related Energy | 232 | 1.2312048013040942 | 0.4420654500955494 |
| Computer Services | 998 | 1.0136316505590375 | 0.38460794608149756 |
| Computers/Peripherals | 340 | 1.3484800037867355 | 0.3961376819921831 |
| Construction Supplies | 746 | 0.9193152152402437 | 0.34710912725935 |
| Diversified | 336 | 0.6642527747713601 | 0.2812808690465901 |
| Drugs (Biotechnology) | 975 | 1.3757142379570484 | 0.5258009876053589 |
| Drugs (Pharmaceutical) | 1175 | 1.1894809072126773 | 0.4431166298149914 |
| Education | 189 | 1.055947299838236 | 0.40892070234129313 |
| Electrical Equipment | 907 | 1.1134884498203954 | 0.414647121527547 |
| Electronics (Consumer & Office) | 150 | 1.2953016455479365 | 0.4135004181674389 |
| Electronics (General) | 1318 | 1.3615550970838504 | 0.39372892120858827 |
| Engineering/Construction | 1183 | 0.8773101056579604 | 0.3623661053995461 |
| Entertainment | 634 | 1.2378822052461393 | 0.4860598596750665 |
| Environmental & Waste Services | 321 | 0.9771897129310338 | 0.46850943935431305 |
| Farming/Agriculture | 407 | 0.5926769477587667 | 0.3563462904537921 |
| Financial Svcs. (Non-bank & Insurance) | 1048 | 0.13365425687307278 | 0.3239008603453932 |
| Food Processing | 1234 | 0.6620661234829931 | 0.332803571977052 |
| Food Wholesalers | 156 | 0.6042265406643416 | 0.3606381815919669 |
| Furn/Home Furnishings | 317 | 0.9706642807777182 | 0.3529020644473325 |
| Green & Renewable Energy | 189 | 0.6472431587685039 | 0.3894756645346032 |
| Healthcare Products | 707 | 1.1262537574933937 | 0.4491939668757043 |
| Healthcare Support Services | 362 | 0.9456248673748303 | 0.40124805652575385 |
| Heathcare Information and Technology | 357 | 1.2296091130792568 | 0.46959202900523545 |
| Homebuilding | 164 | 0.735745762953485 | 0.3399243604630141 |
| Hospitals/Healthcare Facilities | 203 | 0.5554015373025118 | 0.30593771108845413 |
| Hotel/Gaming | 646 | 0.7211671254033455 | 0.331201747306258 |
| Household Products | 544 | 0.9411486452330633 | 0.4255859065107073 |
| Information Services | 214 | 1.121984378642264 | 0.41759507819172187 |
| Insurance (General) | 216 | 0.579223094723065 | 0.24946840503440512 |
| Insurance (Life) | 130 | 0.9385294245362802 | 0.24739132787577917 |
| Insurance (Prop/Cas.) | 220 | 0.5229158767738623 | 0.22859304325772872 |
| Investments & Asset Management | 1018 | 0.5720149493570743 | 0.34813366889105585 |
| Machinery | 1314 | 1.1228221725865228 | 0.3529747861918658 |
| Metals & Mining | 1549 | 1.2422178123867944 | 0.518958555985446 |
| Office Equipment & Services | 156 | 0.8601726997590272 | 0.3530710891118689 |
| Oil/Gas (Integrated) | 49 | 1.1077893646523318 | 0.2622532437051895 |
| Oil/Gas (Production and Exploration) | 852 | 1.1639456881074064 | 0.5389597026797283 |
| Oil/Gas Distribution | 143 | 0.7522591829556261 | 0.3247024309992246 |
| Oilfield Svcs/Equip. | 517 | 1.0665139611521441 | 0.4390884415576891 |
| Packaging & Container | 402 | 0.6127406964143424 | 0.3496588168111514 |
| Paper/Forest Products | 292 | 0.770175186453703 | 0.3674170265311532 |
| Power | 529 | 0.48622628511227367 | 0.24811523787721512 |
| Precious Metals | 871 | 1.1521424888333422 | 0.5224072969180611 |
| Publishing & Newspapers | 353 | 0.8996044049853278 | 0.3682913791867615 |
| R.E.I.T. | 727 | 0.33943979658911216 | 0.16870874804154834 |
| Real Estate (Development) | 811 | 0.6584662981000482 | 0.3391315294979229 |
| Real Estate (General/Diversified) | 399 | 0.6765302640453436 | 0.3455127699593655 |
| Real Estate (Operations & Services) | 645 | 0.5392993202872123 | 0.299713879173631 |
| Recreation | 325 | 0.8263127803415073 | 0.3751666895830149 |
| Reinsurance | 36 | 0.9014529507271523 | 0.269757026604619 |
| Restaurant/Dining | 373 | 0.6446886017377874 | 0.3293338900258362 |
| Retail (Automotive) | 173 | 0.6410092207352402 | 0.3347629270375267 |
| Retail (Building Supply) | 90 | 0.7611057126463388 | 0.33265678389844633 |
| Retail (Distributors) | 983 | 0.6226134969144431 | 0.3662964603235334 |
| Retail (General) | 215 | 0.7688929763603288 | 0.2992390771246902 |
| Retail (Grocery and Food) | 165 | 0.5132265169888095 | 0.2634000461059036 |
| Retail (Online) | 291 | 1.2393918031061377 | 0.48517465917276936 |
| Retail (Special Lines) | 466 | 0.7997457847643465 | 0.372404051984964 |
| Rubber& Tires | 93 | 0.7018089125915598 | 0.29400535701361025 |
| Semiconductor | 530 | 1.588943348994372 | 0.4013011461708741 |
| Semiconductor Equip | 284 | 1.7258020742872078 | 0.411428936927422 |
| Shipbuilding & Marine | 341 | 0.6650715617459226 | 0.3327480092135479 |
| Shoe | 82 | 0.9372203303016206 | 0.3561591058041951 |
| Software (Entertainment) | 262 | 1.2472757421221403 | 0.5365609814574471 |
| Software (Internet) | 131 | 1.0647910764908508 | 0.4765639472267213 |
| Software (System & Application) | 1272 | 1.1783224420185525 | 0.4687089205384593 |
| Steel | 701 | 0.8905646323022122 | 0.3780478984782474 |
| Telecom (Wireless) | 107 | 0.6909977140967478 | 0.3810110956312416 |
| Telecom. Equipment | 493 | 1.2825820889812123 | 0.4201814115113441 |
| Telecom. Services | 317 | 0.6624444332388177 | 0.39713272595556204 |
| Tobacco | 52 | 0.7735243623520475 | 0.37714227045113535 |
| Transportation | 261 | 0.8028984149534666 | 0.3265991027232545 |
| Transportation (Railroads) | 51 | 0.9074939521739978 | 0.21149931113025147 |
| Trucking | 205 | 0.566435316531778 | 0.3100691204366062 |
| Utility (General) | 54 | 0.3833796602312747 | 0.1609721265449521 |
| Utility (Water) | 102 | 0.6515150081173146 | 0.3169009526985267 |
| Total Market  | 43848 | 0.7863963567312631 | 0.37962560881885765 |
| Total Market (without financials) | 39174 | 0.9186410921737417 | 0.3900901719969053 |

## Input Choices

| Effective |
|---|
| Marginal |
