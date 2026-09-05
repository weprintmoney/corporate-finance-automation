---
title: "Betaglobal20"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal20.xls
---

# Betaglobal20

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal20.xls

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
| Advertising | 348 | 0.9882805307734214 | 0.5359967452043048 |
| Aerospace/Defense | 255 | 1.0024811526281652 | 0.5020292111001042 |
| Air Transport | 156 | 0.9177893627711246 | 0.48768937332635137 |
| Apparel | 1188 | 0.853766109354668 | 0.4227326509920152 |
| Auto & Truck | 144 | 1.011046446440295 | 0.4736049312444391 |
| Auto Parts | 709 | 1.278855395804032 | 0.43530702802410837 |
| Bank (Money Center) | 620 | 0.47930202143470874 | 0.30591891893608925 |
| Banks (Regional) | 850 | 0.541608568531446 | 0.3114176814420221 |
| Beverage (Alcoholic) | 223 | 0.7341539604842614 | 0.3776567687722867 |
| Beverage (Soft) | 108 | 0.6509116265997663 | 0.48869210994915807 |
| Broadcasting | 146 | 0.6858768416034856 | 0.44398638400409984 |
| Brokerage & Investment Banking | 575 | 0.4170812123977514 | 0.43750739137285666 |
| Building Materials | 439 | 0.9093397804125348 | 0.40522179285963095 |
| Business & Consumer Services | 923 | 0.9130597184101551 | 0.4739725700165205 |
| Cable TV | 60 | 0.7846306814157183 | 0.40365594102168845 |
| Chemical (Basic) | 844 | 0.9311754214530038 | 0.41747329884368894 |
| Chemical (Diversified) | 73 | 1.048031632511917 | 0.4182128873292168 |
| Chemical (Specialty) | 861 | 0.9876840523287519 | 0.4373054872411437 |
| Coal & Related Energy | 222 | 0.8959412374490998 | 0.5255587832909673 |
| Computer Services | 1007 | 1.002571650346871 | 0.4542872773691189 |
| Computers/Peripherals | 337 | 1.2349266090265119 | 0.4645749364111696 |
| Construction Supplies | 753 | 0.9489007969115382 | 0.4120749664243056 |
| Diversified | 324 | 0.7325078955806549 | 0.3806203919219385 |
| Drugs (Biotechnology) | 1139 | 0.9685394778129185 | 0.5847900504884678 |
| Drugs (Pharmaceutical) | 1319 | 0.9257197914498704 | 0.5217319863211026 |
| Education | 250 | 0.9499461907192076 | 0.4523355059537646 |
| Electrical Equipment | 950 | 1.0579135270894295 | 0.458749173494078 |
| Electronics (Consumer & Office) | 142 | 1.145109372962284 | 0.4764844972745351 |
| Electronics (General) | 1387 | 1.2454565864733256 | 0.44394311771239436 |
| Engineering/Construction | 1263 | 0.7667538377017049 | 0.41721983426190745 |
| Entertainment | 725 | 1.040905952611656 | 0.5355999517924163 |
| Environmental & Waste Services | 344 | 0.8679019283602359 | 0.49662671295193833 |
| Farming/Agriculture | 410 | 0.7077344411836932 | 0.4267191942950053 |
| Financial Svcs. (Non-bank & Insurance) | 1096 | 0.16420934370708237 | 0.42320029960418626 |
| Food Processing | 1322 | 0.7073301892505268 | 0.38917139032543385 |
| Food Wholesalers | 155 | 0.5416663968973806 | 0.41921687207112235 |
| Furn/Home Furnishings | 357 | 1.0241862469995968 | 0.4409430802994445 |
| Green & Renewable Energy | 226 | 0.6934742009209247 | 0.4604341436314864 |
| Healthcare Products | 816 | 0.9284236857290972 | 0.5392649006884597 |
| Healthcare Support Services | 413 | 0.7551857751051636 | 0.48193420486225974 |
| Heathcare Information and Technology | 423 | 0.97133553640996 | 0.5625597478953913 |
| Homebuilding | 167 | 1.15829842401638 | 0.4234014267973573 |
| Hospitals/Healthcare Facilities | 216 | 0.6571476212889761 | 0.41934041160541646 |
| Hotel/Gaming | 641 | 0.8472227190304773 | 0.44977292428552396 |
| Household Products | 568 | 0.8717875265869961 | 0.5045948282989213 |
| Information Services | 244 | 1.141318939194461 | 0.5249070514135928 |
| Insurance (General) | 220 | 0.6609391585431089 | 0.3196075443932574 |
| Insurance (Life) | 133 | 0.9646892900671663 | 0.352601294667935 |
| Insurance (Prop/Cas.) | 229 | 0.654703856455113 | 0.36428880391554685 |
| Investments & Asset Management | 1234 | 0.5496927154725375 | 0.3881410084056666 |
| Machinery | 1385 | 1.0733563446039929 | 0.40751758253765713 |
| Metals & Mining | 1620 | 0.8290093911238976 | 0.6081968479412403 |
| Office Equipment & Services | 148 | 1.006404408347355 | 0.4301671248374972 |
| Oil/Gas (Integrated) | 49 | 1.0784866590681668 | 0.40169304492813324 |
| Oil/Gas (Production and Exploration) | 765 | 0.9311569725891855 | 0.6731807794663675 |
| Oil/Gas Distribution | 204 | 0.6460413399479771 | 0.47645868096594657 |
| Oilfield Svcs/Equip. | 513 | 0.9101608921339075 | 0.5345860280613323 |
| Packaging & Container | 412 | 0.7071919893044979 | 0.3977302112144236 |
| Paper/Forest Products | 287 | 0.78438278848567 | 0.41417016663406164 |
| Power | 553 | 0.5100482281134904 | 0.32238541260608494 |
| Precious Metals | 922 | 0.8668060224206355 | 0.6417101703254495 |
| Publishing & Newspapers | 349 | 0.8413789216293962 | 0.3983930405660878 |
| R.E.I.T. | 799 | 0.6576554717540797 | 0.37933572872811566 |
| Real Estate (Development) | 890 | 0.5229773863704421 | 0.3702949025056515 |
| Real Estate (General/Diversified) | 364 | 0.5974495419983722 | 0.35794336224308276 |
| Real Estate (Operations & Services) | 720 | 0.5349059557928528 | 0.3668585574469329 |
| Recreation | 331 | 0.9346070560540213 | 0.48210281282058637 |
| Reinsurance | 37 | 1.2520897822012522 | 0.3777422683286649 |
| Restaurant/Dining | 379 | 0.9039754916807023 | 0.4704657406401753 |
| Retail (Automotive) | 185 | 0.8198056108284281 | 0.4301693964599231 |
| Retail (Building Supply) | 90 | 1.056717304804078 | 0.49283140916064366 |
| Retail (Distributors) | 1022 | 0.5682992106428517 | 0.4178556837245517 |
| Retail (General) | 217 | 0.8360116928977362 | 0.37501014816166683 |
| Retail (Grocery and Food) | 171 | 0.46899598303943174 | 0.34709076231263597 |
| Retail (Online) | 356 | 1.3114219547764037 | 0.5978748497130146 |
| Retail (Special Lines) | 480 | 0.9588475188774988 | 0.4644036835372506 |
| Rubber& Tires | 92 | 0.8586946281144724 | 0.3804051901479573 |
| Semiconductor | 565 | 1.4320884315366331 | 0.485108870970558 |
| Semiconductor Equip | 308 | 1.7312795141670492 | 0.5033654196612263 |
| Shipbuilding & Marine | 353 | 0.7633616944643629 | 0.39457006405566253 |
| Shoe | 79 | 0.9862424204588389 | 0.4199569417237239 |
| Software (Entertainment) | 339 | 1.1300805915396532 | 0.5947399978553699 |
| Software (Internet) | 155 | 0.9315669326828552 | 0.5403902218320361 |
| Software (System & Application) | 1478 | 1.061330895451685 | 0.5524342727452248 |
| Steel | 718 | 0.933124990188395 | 0.4391525242205005 |
| Telecom (Wireless) | 104 | 0.6304226924540491 | 0.37587231791686065 |
| Telecom. Equipment | 482 | 1.0886826127954905 | 0.4825000480693799 |
| Telecom. Services | 315 | 0.5118078353492548 | 0.43076405490730524 |
| Tobacco | 57 | 0.5510383587069492 | 0.3976273120487636 |
| Transportation | 284 | 0.7671444445351495 | 0.39875719066464776 |
| Transportation (Railroads) | 53 | 0.6190910706898799 | 0.30641162333342614 |
| Trucking | 217 | 0.806368916596742 | 0.4239171949446186 |
| Utility (General) | 53 | 0.48803783479430257 | 0.28064501144064147 |
| Utility (Water) | 104 | 0.5889254995125772 | 0.3554404263321351 |
| Total Market | 46580 | 0.7917792561150673 | 0.45708637344498904 |
| Total Market (without financials) | 41623 | 0.894132484382979 | 0.4670907062265888 |

## Input Choices

| Effective |
|---|
| Marginal |
