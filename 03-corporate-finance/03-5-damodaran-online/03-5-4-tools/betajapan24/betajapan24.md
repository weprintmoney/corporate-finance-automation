---
title: "Betajapan24"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan24.xls
---

# Betajapan24

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaJapan24.xls

Sheets: Variables & FAQ, Industry Averages, Input Choices

## Variables & FAQ

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

| Date updated: | 45662.0 | YouTube Video explaining estimation choices and process. | Effective |
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
| Advertising | 84 | 1.3461456253547002 | 0.2567799042607876 |
| Aerospace/Defense | 5 | 1.5544752898725067 | 3.813357198923914 |
| Air Transport | 6 | 0.76481785366215 | 5.3268360789022795 |
| Apparel | 60 | 0.6977034599410512 | 0.30873138627698565 |
| Auto & Truck | 10 | 0.8745414870997993 | 0.20721697139990247 |
| Auto Parts | 102 | 1.129362268695201 | 0.28653936947782366 |
| Bank (Money Center) | 8 | -4.892173853671835 | NA |
| Banks (Regional) | 75 | -0.9751842270739597 | NA |
| Beverage (Alcoholic) | 6 | 0.558242557297079 | 0.16896222258227828 |
| Beverage (Soft) | 6 | 0.4281429854797697 | 0.1803252723012123 |
| Broadcasting | 11 | 0.6665740783007035 | 0.13961576910193016 |
| Brokerage & Investment Banking | 38 | 0.19750976723276317 | 0.41715272469086656 |
| Building Materials | 60 | 0.7430888427013129 | 0.14810891611529 |
| Business & Consumer Services | 224 | 1.2543815261486733 | 0.30536984054983657 |
| Cable TV | 1 | 1.2962106960948927 | 0.11529688112634126 |
| Chemical (Basic) | 66 | 0.8965939087719424 | 0.23454964462226188 |
| Chemical (Diversified) | 22 | 0.721935679990443 | 0.35480774594501735 |
| Chemical (Specialty) | 70 | 1.172787582890719 | 0.25376222848771973 |
| Coal & Related Energy | 1 | 0.7994411126879304 | 0.8408669947029486 |
| Computer Services | 244 | 1.2705207106968193 | 0.2872406322436096 |
| Computers/Peripherals | 25 | 1.225014464621448 | 0.18616822763767482 |
| Construction Supplies | 51 | 0.9404085574160664 | 0.2010772299574693 |
| Diversified | 16 | 0.9679054987811316 | 0.26276872237504767 |
| Drugs (Biotechnology) | 33 | 1.5361664152960897 | NA |
| Drugs (Pharmaceutical) | 41 | 0.7638967058321121 | 0.23852721318718872 |
| Education | 39 | 0.7633349916811084 | 0.1767104581134483 |
| Electrical Equipment | 53 | 1.225328797051372 | 0.13180998919371373 |
| Electronics (Consumer & Office) | 10 | 1.1872180967869046 | 0.3182743149667726 |
| Electronics (General) | 136 | 1.3594116611877447 | 0.38234200526814904 |
| Engineering/Construction | 156 | 0.7475315815239936 | 0.23788523239492465 |
| Entertainment | 74 | 1.1093220118424645 | 0.3511771862377769 |
| Environmental & Waste Services | 38 | 0.9901349475646053 | 0.27486597782188577 |
| Farming/Agriculture | 11 | 0.6215621557764485 | 0.11235675815484693 |
| Financial Svcs. (Non-bank & Insurance) | 50 | 0.09800110098094732 | 0.13122964571655613 |
| Food Processing | 121 | 0.3878511966762396 | 0.16886835418805077 |
| Food Wholesalers | 37 | 0.512081325537758 | 0.1748023054142501 |
| Furn/Home Furnishings | 19 | 0.9995907473500512 | 0.11076869879146037 |
| Green & Renewable Energy | 8 | 0.9398940586923281 | 1.0244652345036802 |
| Healthcare Products | 40 | 0.9215857368758618 | 0.19389302786855184 |
| Healthcare Support Services | 48 | 0.30418129954874396 | 0.1416989082049606 |
| Heathcare Information and Technology | 37 | 1.6622552755883524 | 0.5942375306018273 |
| Homebuilding | 51 | 0.5256899746696521 | 0.2589916699339451 |
| Hospitals/Healthcare Facilities | 11 | 0.5182244113542644 | 0.7799107877230874 |
| Hotel/Gaming | 33 | 0.8081211322997861 | 2.45153018949177 |
| Household Products | 41 | 0.8359363133624181 | 0.2406383002911144 |
| Information Services | 14 | 1.272251255866928 | 0.3041658032633801 |
| Insurance (General) | 6 | 2.1998084171378074 | 0.8928176340923887 |
| Insurance (Life) | 5 | -1.063159162309088 | 0.27847678044758817 |
| Insurance (Prop/Cas.) | 7 | 1.4802046770891062 | 0.3088987786623572 |
| Investments & Asset Management | 14 | 2.883184594974419 | 0.3973925839462388 |
| Machinery | 226 | 1.1375918079374288 | 0.1247777866331132 |
| Metals & Mining | 20 | 0.9786680120678295 | 0.36848463465632375 |
| Office Equipment & Services | 26 | 0.7884625691399818 | 0.1226595043103676 |
| Oil/Gas (Integrated) | 0 | NA | 7 |
| Oil/Gas (Production and Exploration) | 2 | 1.0046256001777287 | 0.5041659111316387 |
| Oil/Gas Distribution | 3 | 0.7643987716196162 | 0.2716205643089409 |
| Oilfield Svcs/Equip. | 19 | 0.45533883451256013 | 0.9098972023633096 |
| Packaging & Container | 29 | 0.46133562633811215 | 0.2426817262792629 |
| Paper/Forest Products | 15 | 0.3586632853858436 | 0.3267935913658411 |
| Power | 25 | 0.1984391905538939 | 0.7346498124102008 |
| Precious Metals | 2 | 0.3312267508932802 | 0.452614831743697 |
| Publishing & Newspapers | 53 | 0.8612949253120585 | 0.20103190081206782 |
| R.E.I.T. | 53 | 0.475567673305943 | 0.2630627154754342 |
| Real Estate (Development) | 17 | 0.6447338484922672 | 0.3135580021693117 |
| Real Estate (General/Diversified) | 52 | 0.5106428165077653 | 0.17124044974683028 |
| Real Estate (Operations & Services) | 43 | 0.5630965945549646 | 0.1982229696540414 |
| Recreation | 51 | 0.9783739202251728 | 0.25855920703843055 |
| Reinsurance | 0 | NA | 7 |
| Restaurant/Dining | 109 | 0.8056665306960998 | 1.1012057154860928 |
| Retail (Automotive) | 27 | 0.7965514611970144 | 0.22075536981633445 |
| Retail (Building Supply) | 18 | 0.6084124970905785 | 0.3464270236298431 |
| Retail (Distributors) | 141 | 0.6601269309167067 | 0.3998880901673718 |
| Retail (General) | 43 | 0.8484681954448724 | 0.43674811448459294 |
| Retail (Grocery and Food) | 52 | 0.46280039434905573 | 0.12564338813071002 |
| Retail (REITs) | 4 | 0.48519439125085845 | 0.31306587312351863 |
| Retail (Special Lines) | 133 | 0.7956247674903266 | 0.12368144964559118 |
| Rubber& Tires | 6 | 0.7742945267531836 | 0.17680918046193486 |
| Semiconductor | 23 | 1.4418777795495505 | 0.6918195938489813 |
| Semiconductor Equip | 35 | 2.453297707508105 | 0.5352618412446872 |
| Shipbuilding & Marine | 29 | 0.7092852901846654 | 0.7433130592584234 |
| Shoe | 3 | -0.32327101885251625 | 0.6558082986807979 |
| Software (Entertainment) | 74 | 1.0991106807800899 | 0.08887623258796527 |
| Software (Internet) | 26 | 1.584731305092712 | 0.4172733351096784 |
| Software (System & Application) | 182 | 1.6522177535112914 | 0.2526900860184143 |
| Steel | 42 | 0.8630118058859848 | 0.5688040594685013 |
| Telecom (Wireless) | 8 | 0.6861136198066836 | 0.21216992926524145 |
| Telecom. Equipment | 15 | 1.6793757659801547 | 0.27831753136559556 |
| Telecom. Services | 20 | 0.8097073543804293 | 0.19716789129264514 |
| Tobacco | 1 | 0.6265352388461052 | 0.12100857272341775 |
| Transportation | 33 | 0.45130164239122034 | 0.1987875017646363 |
| Transportation (Railroads) | 22 | 0.3028820987877038 | 0.8912192657861224 |
| Trucking | 17 | 0.6377636684209281 | 0.18361370331345517 |
| Utility (General) | 0 | NA | 7 |
| Utility (Water) | 0 | NA | 7 |
| Total Market | 4023 | 0.842679213896826 | 0.13174129973936816 |
| Total Market (without financials) | 3820 | 0.8340994090736613 | 0.13239020723327816 |

## Input Choices

| Effective |
|---|
| Marginal |
