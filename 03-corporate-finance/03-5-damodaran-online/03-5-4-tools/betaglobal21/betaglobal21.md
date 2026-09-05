---
title: "Betaglobal21"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal21.xls
---

# Betaglobal21

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal21.xls

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

| Date updated: | 44566.0 | YouTube Video explaining estimation choices and process. | Notes |
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
| Advertising | 348 | 1.184662795054903 | 0.4293477350634977 |
| Aerospace/Defense | 272 | 1.1116864156748973 | 0.3777052926698575 |
| Air Transport | 151 | 0.9395465907074113 | 0.2992456125256538 |
| Apparel | 1170 | 0.9033441002082254 | 0.4083952175164582 |
| Auto & Truck | 152 | 1.110597323255731 | 0.3584614893163646 |
| Auto Parts | 728 | 1.4360496102184261 | 0.33547033129682113 |
| Bank (Money Center) | 610 | 0.5906038703913513 | 0.23927707042560545 |
| Banks (Regional) | 816 | 0.6667696019082262 | 0.21029391238268733 |
| Beverage (Alcoholic) | 219 | 0.860183204946771 | 0.3161624992237729 |
| Beverage (Soft) | 100 | 0.815904339020854 | 0.43906226571544954 |
| Broadcasting | 139 | 0.8122030100021643 | 0.38203847320225454 |
| Brokerage & Investment Banking | 599 | 0.45383438531295534 | 0.40046949067575627 |
| Building Materials | 449 | 1.0533687030919148 | 0.3287832682096286 |
| Business & Consumer Services | 948 | 1.0366605291428443 | 0.38205084520174243 |
| Cable TV | 54 | 0.7152089497839219 | 0.27814070668790825 |
| Chemical (Basic) | 854 | 1.0219877158206196 | 0.3692738403246024 |
| Chemical (Diversified) | 71 | 1.1476290063670667 | 0.2970985687227409 |
| Chemical (Specialty) | 898 | 1.0394823310715897 | 0.3718788550532679 |
| Coal & Related Energy | 206 | 1.0910424717421947 | 0.5196165187847982 |
| Computer Services | 1040 | 1.0872547993735642 | 0.3770639672342174 |
| Computers/Peripherals | 336 | 1.3273913361115275 | 0.364696084510823 |
| Construction Supplies | 784 | 1.021934901271395 | 0.3269368391853319 |
| Diversified | 318 | 0.81945247458655 | 0.3113112492473067 |
| Drugs (Biotechnology) | 1223 | 1.1008038836104794 | 0.5081299616049616 |
| Drugs (Pharmaceutical) | 1371 | 1.019509536200177 | 0.45476924124097123 |
| Education | 244 | 0.997308360259894 | 0.38809205082338677 |
| Electrical Equipment | 999 | 1.0807004988556506 | 0.397283247845176 |
| Electronics (Consumer & Office) | 138 | 1.186826440486317 | 0.3798770135254992 |
| Electronics (General) | 1425 | 1.3115844334733844 | 0.3605663049540746 |
| Engineering/Construction | 1267 | 0.8447598199922111 | 0.348718227836435 |
| Entertainment | 734 | 1.1070010153253311 | 0.45552715590093257 |
| Environmental & Waste Services | 353 | 0.895971848614013 | 0.4120649957163222 |
| Farming/Agriculture | 417 | 0.7676258651642635 | 0.36452133743233606 |
| Financial Svcs. (Non-bank & Insurance) | 1102 | 0.19582219262776895 | 0.36077871317707705 |
| Food Processing | 1377 | 0.7685452855225647 | 0.32738158348503454 |
| Food Wholesalers | 160 | 0.60329665941671 | 0.34485169376100905 |
| Furn/Home Furnishings | 359 | 1.1457281960478736 | 0.35516130325411455 |
| Green & Renewable Energy | 239 | 0.7593531227780699 | 0.3790968815066562 |
| Healthcare Products | 852 | 1.0051575839883573 | 0.4368823320732141 |
| Healthcare Support Services | 445 | 0.8532963298167002 | 0.40569179316898285 |
| Heathcare Information and Technology | 455 | 1.0306863148100875 | 0.44356423993054794 |
| Homebuilding | 168 | 1.368027254719254 | 0.29939423594008685 |
| Hospitals/Healthcare Facilities | 223 | 0.7366530660619384 | 0.3383414914426642 |
| Hotel/Gaming | 654 | 0.9495187874820774 | 0.35793222379699274 |
| Household Products | 575 | 0.9975160854368706 | 0.41516500204679246 |
| Information Services | 266 | 1.2268646174350117 | 0.4175651154926289 |
| Insurance (General) | 215 | 0.717758918299041 | 0.2713195117129375 |
| Insurance (Life) | 142 | 0.9967275050869701 | 0.26285517349957144 |
| Insurance (Prop/Cas.) | 231 | 0.8183094083793329 | 0.3009167522751331 |
| Investments & Asset Management | 1706 | 0.7191399175751529 | 0.2475957682973719 |
| Machinery | 1421 | 1.1250479153986082 | 0.3397047837842136 |
| Metals & Mining | 1706 | 1.0120404370223572 | 0.48364631838282895 |
| Office Equipment & Services | 145 | 1.0516179146449982 | 0.3577647259514885 |
| Oil/Gas (Integrated) | 46 | 1.148950367811506 | 0.29165587115616853 |
| Oil/Gas (Production and Exploration) | 642 | 1.208765724406964 | 0.5409028134446774 |
| Oil/Gas Distribution | 165 | 0.7452690177486584 | 0.3153761181867277 |
| Oilfield Svcs/Equip. | 457 | 1.05969409099153 | 0.39636543072135894 |
| Packaging & Container | 414 | 0.803195222596622 | 0.3265617860134949 |
| Paper/Forest Products | 272 | 0.8946464363764315 | 0.3468931018323947 |
| Power | 541 | 0.5392416959764251 | 0.2912952440280204 |
| Precious Metals | 947 | 0.9881729384346463 | 0.4748298398482442 |
| Publishing & Newspapers | 337 | 0.940295378352039 | 0.3595185089638034 |
| R.E.I.T. | 812 | 0.7667584661175046 | 0.19695583859169807 |
| Real Estate (Development) | 893 | 0.51619803539889 | 0.3490367454315253 |
| Real Estate (General/Diversified) | 344 | 0.6141206252318322 | 0.29576434774311994 |
| Real Estate (Operations & Services) | 739 | 0.6255020165547774 | 0.3097272027781396 |
| Recreation | 324 | 1.02369261923284 | 0.35760427161835157 |
| Reinsurance | 38 | 1.4408384721850078 | 0.27092852629046865 |
| Restaurant/Dining | 385 | 1.0103617059741818 | 0.32301093264838665 |
| Retail (Automotive) | 196 | 0.88667994236322 | 0.34903434715548365 |
| Retail (Building Supply) | 98 | 1.1054564123787107 | 0.30854214066264335 |
| Retail (Distributors) | 1002 | 0.6464878292043778 | 0.38328979607358626 |
| Retail (General) | 204 | 0.8681220065830827 | 0.27439356463984166 |
| Retail (Grocery and Food) | 184 | 0.5346639484687146 | 0.2629763598505409 |
| Retail (Online) | 353 | 1.404881197430484 | 0.471229685101749 |
| Retail (Special Lines) | 479 | 1.0862145397901581 | 0.3440292421458869 |
| Rubber& Tires | 90 | 1.0977626001146414 | 0.3094606191017025 |
| Semiconductor | 581 | 1.5530936635261203 | 0.4092863272315615 |
| Semiconductor Equip | 324 | 1.9337186879458486 | 0.35740268703234396 |
| Shipbuilding & Marine | 348 | 0.9860170394495534 | 0.36361319457741026 |
| Shoe | 84 | 1.1294736492366366 | 0.3785168561696509 |
| Software (Entertainment) | 317 | 1.2797793146309626 | 0.5138560178095222 |
| Software (Internet) | 151 | 1.108445828620835 | 0.46605249002314547 |
| Software (System & Application) | 1603 | 1.2008396816037168 | 0.44699646940608506 |
| Steel | 709 | 1.0675797577799606 | 0.41679596772108607 |
| Telecom (Wireless) | 101 | 0.7175934990852277 | 0.3249742351551542 |
| Telecom. Equipment | 465 | 1.1673203453641146 | 0.3928726697220049 |
| Telecom. Services | 296 | 0.5764380668363102 | 0.3571632354459364 |
| Tobacco | 55 | 0.7289287160132258 | 0.41881033719487387 |
| Transportation | 295 | 0.8529379525593787 | 0.3470226355598786 |
| Transportation (Railroads) | 51 | 0.6675122176931948 | 0.1990941205821509 |
| Trucking | 232 | 0.9208091270401624 | 0.33065902771294364 |
| Utility (General) | 54 | 0.5216509034031074 | 0.1784442218699003 |
| Utility (Water) | 104 | 0.5144648130784433 | 0.2953786620017125 |
| Total Market | 47606 | 0.8922652634995092 | 0.3730800892079746 |
| Total Market (without financials) | 42185 | 0.9928066848363145 | 0.3844556888559662 |

## Input Choices

| Effective |
|---|
| Marginal |
