---
title: "Betaglobal23"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal23.xls
---

# Betaglobal23

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/betaGlobal23.xls

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
| Advertising | 391 | 1.230922708614235 | 0.423917268181586 |
| Aerospace/Defense | 289 | 0.9033832599921977 | 0.35669276145019535 |
| Air Transport | 155 | 0.8104034085122015 | 0.32696418683182654 |
| Apparel | 1152 | 0.7794657334292336 | 0.32113391168320865 |
| Auto & Truck | 165 | 1.1030216126379664 | 0.42970252588994573 |
| Auto Parts | 761 | 1.2090551528976192 | 0.3175010397651392 |
| Bank (Money Center) | 607 | 0.42062215883943516 | 0.212213846149399 |
| Banks (Regional) | 881 | 0.28391223862464154 | 0.22352306057507929 |
| Beverage (Alcoholic) | 220 | 0.6865821100681192 | 0.2866903688100707 |
| Beverage (Soft) | 100 | 0.6563336098512859 | 0.37882077519542773 |
| Broadcasting | 130 | 0.6637382391378946 | 0.35327297467011515 |
| Brokerage & Investment Banking | 590 | 0.39976610514833727 | 0.3388151960688077 |
| Building Materials | 457 | 0.9404913910737808 | 0.29568948471740625 |
| Business & Consumer Services | 980 | 0.9640724752866636 | 0.3516113812858824 |
| Cable TV | 48 | 0.6075774591759452 | 0.3374969558013187 |
| Chemical (Basic) | 888 | 0.9019272865434659 | 0.29266533929194366 |
| Chemical (Diversified) | 64 | 0.8463670076042942 | 0.23217966798153808 |
| Chemical (Specialty) | 949 | 0.9409530206448732 | 0.3185147331601164 |
| Coal & Related Energy | 215 | 1.0773641639143707 | 0.4315997450411636 |
| Computer Services | 1164 | 1.0014532086275136 | 0.35144556277498573 |
| Computers/Peripherals | 338 | 1.2534021480264688 | 0.36800788475890556 |
| Construction Supplies | 793 | 0.8765233217556566 | 0.3009769204079889 |
| Diversified | 326 | 0.7447055221431189 | 0.27331421311063386 |
| Drugs (Biotechnology) | 1259 | 1.1499580759492718 | 0.5407394031199935 |
| Drugs (Pharmaceutical) | 1299 | 0.885775137044685 | 0.41674152081670857 |
| Education | 260 | 0.760048193847253 | 0.3888477402642323 |
| Electrical Equipment | 1072 | 1.1038380140290207 | 0.3780291348439767 |
| Electronics (Consumer & Office) | 127 | 1.1252477543580413 | 0.3733576257103201 |
| Electronics (General) | 1486 | 1.2783308812571208 | 0.33847288499410805 |
| Engineering/Construction | 1283 | 0.7058505143148914 | 0.3274926644590912 |
| Entertainment | 741 | 1.032645697681921 | 0.4347237209585506 |
| Environmental & Waste Services | 383 | 0.8279088564359454 | 0.37123861176203093 |
| Farming/Agriculture | 430 | 0.5739833900965212 | 0.33352048370789006 |
| Financial Svcs. (Non-bank & Insurance) | 1113 | 0.2776667061543162 | 0.35853116091176707 |
| Food Processing | 1395 | 0.6039413354218605 | 0.30647453815713643 |
| Food Wholesalers | 173 | 0.49621392699558364 | 0.33636511502487226 |
| Furn/Home Furnishings | 383 | 0.9343214300886445 | 0.2918006663540768 |
| Green & Renewable Energy | 253 | 0.6090620482792936 | 0.3681537217928212 |
| Healthcare Products | 849 | 1.0434097110903426 | 0.44060150342820786 |
| Healthcare Support Services | 463 | 0.8212109879282184 | 0.39499571685932533 |
| Heathcare Information and Technology | 443 | 1.17067702552802 | 0.44773394535161976 |
| Homebuilding | 173 | 1.0113882281398225 | 0.3304884896946101 |
| Hospitals/Healthcare Facilities | 232 | 0.5802219144187124 | 0.32407501508232067 |
| Hotel/Gaming | 650 | 0.7853696261046105 | 0.3374885116467754 |
| Household Products | 549 | 0.8467284006789493 | 0.3702339328632409 |
| Information Services | 81 | 1.0228619556904517 | 0.38166891135791475 |
| Insurance (General) | 202 | 0.629394290783981 | 0.2457207774399582 |
| Insurance (Life) | 137 | 0.7749958133235606 | 0.2408404076924146 |
| Insurance (Prop/Cas.) | 228 | 0.6647689482362986 | 0.27145201745044617 |
| Investments & Asset Management | 1374 | 0.5397928644612402 | 0.29950596570499743 |
| Machinery | 1492 | 1.03836102698098 | 0.3031773110652812 |
| Metals & Mining | 1815 | 0.9888283828600355 | 0.5013085161369282 |
| Office Equipment & Services | 137 | 0.7755481534276752 | 0.3097894010721913 |
| Oil/Gas (Integrated) | 36 | 0.9378980391506078 | 0.23196569122487862 |
| Oil/Gas (Production and Exploration) | 590 | 0.9640028763637847 | 0.45187606453427664 |
| Oil/Gas Distribution | 174 | 0.5830689215795911 | 0.2921821624974804 |
| Oilfield Svcs/Equip. | 444 | 0.8165003226031388 | 0.3600000521988543 |
| Packaging & Container | 426 | 0.6296021911543933 | 0.29386704298584165 |
| Paper/Forest Products | 266 | 0.6745272635760394 | 0.29677506048019786 |
| Power | 488 | 0.4470973992829686 | 0.2685337268300212 |
| Precious Metals | 853 | 1.0402350701665934 | 0.5052576282988133 |
| Publishing & Newspapers | 324 | 0.888119661393053 | 0.32744522580312907 |
| R.E.I.T. | 659 | 0.518676720895122 | 0.22660046672543616 |
| Real Estate (Development) | 884 | 0.41518460236100446 | 0.33952140707756057 |
| Real Estate (General/Diversified) | 336 | 0.5402762120215623 | 0.2696094336514501 |
| Real Estate (Operations & Services) | 748 | 0.5601396650240725 | 0.307843993617713 |
| Recreation | 326 | 0.9009533857969224 | 0.3418723791420405 |
| Reinsurance | 34 | 1.0857693512076685 | 0.2661683153190195 |
| Restaurant/Dining | 394 | 0.8469120945471883 | 0.32466349764175095 |
| Retail (Automotive) | 204 | 0.7151526523022773 | 0.34207120014384995 |
| Retail (Building Supply) | 120 | 0.9624856160601153 | 0.3028887069791528 |
| Retail (Distributors) | 1028 | 0.6107295837787711 | 0.33931813593052157 |
| Retail (General) | 256 | 0.9930678407425075 | 0.2865179529329477 |
| Retail (Grocery and Food) | 201 | 0.5519051683925645 | 0.28362121369770876 |
| Retail (REITs) | 123 | 0.6148047022774255 | 0.1958057068211921 |
| Retail (Special Lines) | 639 | 0.980796728945327 | 0.35768276588672027 |
| Rubber& Tires | 89 | 0.8848772364010901 | 0.2645233844582652 |
| Semiconductor | 647 | 1.6672585627718395 | 0.35205731835269655 |
| Semiconductor Equip | 367 | 1.965518756667748 | 0.35126254777679206 |
| Shipbuilding & Marine | 348 | 0.8631601762392301 | 0.2896618593847156 |
| Shoe | 85 | 0.8721798577655788 | 0.33676553384325053 |
| Software (Entertainment) | 317 | 1.3553519753448988 | 0.4660036724450452 |
| Software (Internet) | 151 | 1.298774525993413 | 0.43323221435879294 |
| Software (System & Application) | 1616 | 1.2856288444138266 | 0.45324097959801884 |
| Steel | 718 | 1.006786675768852 | 0.3217273755212449 |
| Telecom (Wireless) | 98 | 0.6530666984464208 | 0.2806116246250456 |
| Telecom. Equipment | 453 | 1.1744668677688677 | 0.39288835761797347 |
| Telecom. Services | 288 | 0.543807658930849 | 0.3328544176369092 |
| Tobacco | 56 | 0.5533516641188336 | 0.3576528642132933 |
| Transportation | 443 | 0.7460208539065312 | 0.31732087812955406 |
| Transportation (Railroads) | 49 | 0.49774817486891265 | 0.186508180093947 |
| Trucking | 106 | 0.8685544613027371 | 0.3205544589697382 |
| Utility (General) | 50 | 0.45062860002415905 | 0.23474916917581573 |
| Utility (Water) | 102 | 0.4274749642866797 | 0.25433982782510367 |
| Total Market | 47698 | 0.7862553553280948 | 0.35320733358966394 |
| Total Market (without financials) | 42566 | 0.905029349985941 | 0.3610054183867632 |

## Input Choices

| Effective |
|---|
| Marginal |
