---
title: "Betas"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/datasets/betas.xls
---

# Betas

Source: http://www.stern.nyu.edu/~adamodar/pc/datasets/betas.xls

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
| Advertising | 52 | 1.0080098903421257 | 0.6233257531660213 |
| Aerospace/Defense | 79 | 0.8693772823914925 | 0.5213050748745736 |
| Air Transport | 23 | 0.7579038179118688 | 0.5151727607461237 |
| Apparel | 35 | 0.794563498700363 | 0.5786453528011011 |
| Auto & Truck | 33 | 1.3081652064358895 | 0.7242202227236834 |
| Auto Parts | 35 | 1.1283051051783621 | 0.5242640346289048 |
| Bank (Money Center) | 15 | 0.4438913800649 | 0.23102417672707903 |
| Banks (Regional) | 568 | 0.3744392448485997 | 0.1917165677227987 |
| Beverage (Alcoholic) | 14 | 0.6280466376925842 | 0.582970879014547 |
| Beverage (Soft) | 27 | 0.5754648330410659 | 0.6187363130886608 |
| Broadcasting | 24 | 0.315292569835984 | 0.5720694045435653 |
| Brokerage & Investment Banking | 32 | 0.6794030848916329 | 0.42206737565162095 |
| Building Materials | 41 | 0.9605275604881124 | 0.40986010917831023 |
| Business & Consumer Services | 155 | 0.8060249314889546 | 0.5301773694386264 |
| Cable TV | 9 | 0.36287690746362616 | 0.4440901519592926 |
| Chemical (Basic) | 29 | 0.6367830669050106 | 0.535444966705913 |
| Chemical (Diversified) | 4 | 0.40614323179001943 | 0.42303926014131843 |
| Chemical (Specialty) | 59 | 0.8244706586041288 | 0.4094843058839141 |
| Coal & Related Energy | 16 | 1.1824381999346527 | 0.6619189868384981 |
| Computer Services | 64 | 0.9617009989891427 | 0.5715390929381887 |
| Computers/Peripherals | 36 | 1.3245870396777912 | 0.5570782029943967 |
| Construction Supplies | 40 | 1.0468296973758173 | 0.4302290616017562 |
| Diversified | 20 | 0.8430962646682882 | 0.5557774635262347 |
| Drugs (Biotechnology) | 496 | 1.079453865168337 | 0.6431233872977022 |
| Drugs (Pharmaceutical) | 228 | 0.915135973481584 | 0.6840671510230288 |
| Education | 32 | 0.719599829329938 | 0.5006386723025373 |
| Electrical Equipment | 112 | 1.1898070318069807 | 0.6770752062132696 |
| Electronics (Consumer & Office) | 8 | 0.9273766123201671 | 0.6313586941286815 |
| Electronics (General) | 114 | 0.9374545595854545 | 0.533205169727335 |
| Engineering/Construction | 48 | 1.137436783693752 | 0.48191035503115626 |
| Entertainment | 92 | 0.7628468307830948 | 0.6108354156893298 |
| Environmental & Waste Services | 53 | 0.8247690956344971 | 0.6039647123055116 |
| Farming/Agriculture | 35 | 0.8457836746022086 | 0.5709210427107252 |
| Financial Svcs. (Non-bank & Insurance) | 176 | 0.32770838684759396 | 0.4483550193131286 |
| Food Processing | 78 | 0.46942377677075875 | 0.48589638792481726 |
| Food Wholesalers | 13 | 0.6477598141678518 | 0.5105259187106911 |
| Furn/Home Furnishings | 27 | 0.6521303704400933 | 0.47189994716908745 |
| Green & Renewable Energy | 15 | 0.4722841676536161 | 0.730979638575004 |
| Healthcare Products | 204 | 0.8569477958661521 | 0.5589658747106533 |
| Healthcare Support Services | 104 | 0.7448750574739688 | 0.5230194559374083 |
| Heathcare Information and Technology | 115 | 1.016325032628335 | 0.5788051740319831 |
| Homebuilding | 30 | 0.8532230798743929 | 0.36815060194677524 |
| Hospitals/Healthcare Facilities | 31 | 0.5648588718287879 | 0.5197979912329719 |
| Hotel/Gaming | 63 | 0.8756884427797555 | 0.4804349731732187 |
| Household Products | 110 | 0.7410769287097494 | 0.6273286444390683 |
| Information Services | 15 | 0.7563563575971642 | 0.4394703659399052 |
| Insurance (General) | 21 | 0.5780724262046252 | 0.4200868926838418 |
| Insurance (Life) | 20 | 0.5317480065275768 | 0.23176202865660195 |
| Insurance (Prop/Cas.) | 57 | 0.4570234949231456 | 0.2677137310292105 |
| Investments & Asset Management | 283 | 0.588064033338367 | 0.24979176761115496 |
| Machinery | 105 | 0.8940302510086939 | 0.43866071672945106 |
| Metals & Mining | 73 | 1.0104492960544031 | 0.7046547159245414 |
| Office Equipment & Services | 14 | 1.0381901897861687 | 0.4264799643054135 |
| Oil/Gas (Integrated) | 4 | 0.2780040123588666 | 0.15721649319411557 |
| Oil/Gas (Production and Exploration) | 142 | 0.5785405692885324 | 0.5045189633960516 |
| Oil/Gas Distribution | 23 | 0.46925629740907565 | 0.4564611173153585 |
| Oilfield Svcs/Equip. | 97 | 0.7870575641420728 | 0.4765813226700708 |
| Packaging & Container | 19 | 0.7489917958635104 | 0.38154365295589976 |
| Paper/Forest Products | 6 | 0.7696751455408247 | 0.46710221978809086 |
| Power | 46 | 0.31457840775745605 | 0.22344962815356856 |
| Precious Metals | 56 | 0.8308962073401722 | 0.7326706104991456 |
| Publishing & Newspapers | 19 | 0.511884073790114 | 0.3069368107166666 |
| R.E.I.T. | 190 | 0.40054184967311207 | 0.25934541449375126 |
| Real Estate (Development) | 14 | 0.564103618717777 | 0.6069532024375857 |
| Real Estate (General/Diversified) | 12 | 0.6269536358598106 | 0.46251713640767406 |
| Real Estate (Operations & Services) | 54 | 0.8575864326620388 | 0.4308207605315895 |
| Recreation | 49 | 0.7364987182992697 | 0.5364508541827235 |
| Reinsurance | 1 | 0.5777016987693434 | 0.1879557391260007 |
| Restaurant/Dining | 64 | 0.7830073823550779 | 0.49137844689177756 |
| Retail (Automotive) | 34 | 0.713248607812822 | 0.4825372615960231 |
| Retail (Building Supply) | 14 | 1.3176570660974836 | 0.3865195809285255 |
| Retail (Distributors) | 62 | 0.8016320288830955 | 0.43297246786029253 |
| Retail (General) | 23 | 0.7809280399984467 | 0.3806084813467897 |
| Retail (Grocery and Food) | 15 | 0.8483611176919518 | 0.4157715510638451 |
| Retail (REITs) | 26 | 0.442715972660596 | 0.2004571607943027 |
| Retail (Special Lines) | 94 | 1.0018775790318082 | 0.5308677688475226 |
| Rubber& Tires | 3 | 0.15435790814828812 | 0.36277061657452014 |
| Semiconductor | 66 | 1.5046492754744247 | 0.5440400597664541 |
| Semiconductor Equip | 31 | 1.3916911563373942 | 0.47598492942989046 |
| Shipbuilding & Marine | 8 | 0.6607667999490512 | 0.5290585304325847 |
| Shoe | 11 | 1.0001868235248257 | 0.4536428192746412 |
| Software (Entertainment) | 77 | 1.0206917427212765 | 0.6091442626711892 |
| Software (Internet) | 29 | 1.5905250877083126 | 0.5617970760653243 |
| Software (System & Application) | 309 | 1.2481994174665423 | 0.574139770333485 |
| Steel | 19 | 0.9449429751018495 | 0.3648257910016504 |
| Telecom (Wireless) | 12 | 0.39242083985345116 | 0.5029827095145988 |
| Telecom. Equipment | 57 | 0.8872512120358865 | 0.5619381481246962 |
| Telecom. Services | 39 | 0.38150035836387236 | 0.5334807660091442 |
| Tobacco | 10 | 0.6902977739311797 | 0.563964922337651 |
| Transportation | 19 | 0.7115266417564335 | 0.44453815008849273 |
| Transportation (Railroads) | 4 | 0.8137222539977831 | 0.23929433617664572 |
| Trucking | 26 | 0.8688507380232171 | 0.43293535347074813 |
| Utility (General) | 14 | 0.14911053505258812 | 0.1300880797936857 |
| Utility (Water) | 14 | 0.28247289345133525 | 0.2490832022451339 |
| Total Market | 5994 | 0.7557168656692986 | 0.48072519724238 |
| Total Market (without financials) | 4822 | 0.9009675279492425 | 0.5344840318356062 |

## Inputs

| Effective |
|---|
| Marginal |
