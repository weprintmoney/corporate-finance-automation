---
title: "Betajapan"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaJapan.xls
---

# Betajapan

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/betaJapan.xls

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
| Advertising | 87 | 1.4625982075559045 | 0.2317025243328256 |
| Aerospace/Defense | 5 | 3.1718513711919214 | NA |
| Air Transport | 5 | 0.9662871978791753 | 5.179968917662647 |
| Apparel | 60 | 1.0630815166633523 | 0.2887115368273685 |
| Auto & Truck | 10 | 0.9073418651835004 | 0.21397236022216132 |
| Auto Parts | 98 | 1.3934992397433166 | 0.28095727229450235 |
| Bank (Money Center) | 7 | 5.871809733258941 | NA |
| Banks (Regional) | 76 | 99.23546381907646 | NA |
| Beverage (Alcoholic) | 7 | 0.505626808899495 | 0.1314944257423261 |
| Beverage (Soft) | 6 | 0.1392188839706905 | 0.15957837631951868 |
| Broadcasting | 11 | 0.9214309358884848 | 0.15513090662887347 |
| Brokerage & Investment Banking | 39 | 0.305303110339823 | 0.38938057389081104 |
| Building Materials | 56 | 0.9419660694280511 | 0.12257800522815776 |
| Business & Consumer Services | 224 | 1.2351703977479793 | 0.22672589565743648 |
| Cable TV | 1 | 1.36496593573125 | 0.11133290199069205 |
| Chemical (Basic) | 65 | 1.040263772942314 | 0.22672876331827993 |
| Chemical (Diversified) | 22 | 1.104882503188288 | 0.3848453937804799 |
| Chemical (Specialty) | 69 | 1.302279622359831 | 0.20892383355548141 |
| Coal & Related Energy | 1 | 0.7899936440863613 | 1.1256190947858231 |
| Computer Services | 240 | 1.446919348481557 | 0.25634939184336364 |
| Computers/Peripherals | 24 | 1.2283034928977707 | 0.1766035965883862 |
| Construction Supplies | 51 | 1.2079253898441744 | 0.21519795634150457 |
| Diversified | 16 | 1.1529435784085125 | 0.243592846709989 |
| Drugs (Biotechnology) | 33 | 1.773314064136744 | NA |
| Drugs (Pharmaceutical) | 40 | 1.0681419786655695 | 0.20950335409114548 |
| Education | 35 | 1.0404697081296432 | 0.18282023980801163 |
| Electrical Equipment | 53 | 1.406038939091871 | 0.1254234048432134 |
| Electronics (Consumer & Office) | 10 | 1.4691093980508056 | 0.26184003173427234 |
| Electronics (General) | 132 | 1.6317907770628628 | 0.3646730842018123 |
| Engineering/Construction | 153 | 0.8897298794096263 | 0.1944456559106063 |
| Entertainment | 74 | 1.1397846216690681 | 0.30181846490685676 |
| Environmental & Waste Services | 38 | 1.0527876924098578 | 0.37996801198490443 |
| Farming/Agriculture | 11 | 0.6431607537330846 | 0.11062305597623724 |
| Financial Svcs. (Non-bank & Insurance) | 50 | 0.16591693547471348 | 0.1225053027041623 |
| Food Processing | 118 | 0.47566778064838267 | 0.11670646614414643 |
| Food Wholesalers | 34 | 0.6834308497160911 | 0.1709233394611806 |
| Furn/Home Furnishings | 19 | 0.8990645660450491 | 0.10322566874748657 |
| Green & Renewable Energy | 6 | 1.529601728588263 | 0.9929664905695441 |
| Healthcare Products | 39 | 1.0610520830162378 | 0.16326326380998032 |
| Healthcare Support Services | 48 | 1.1231752838963927 | 0.11314060407086651 |
| Heathcare Information and Technology | 35 | 1.4951585866803716 | 0.49020796430047053 |
| Homebuilding | 45 | 0.5252274783299177 | 0.1804664407482996 |
| Hospitals/Healthcare Facilities | 11 | 0.9773440523018432 | 0.7003566339877033 |
| Hotel/Gaming | 35 | 0.8546959354352324 | 2.3250582120797847 |
| Household Products | 42 | 0.9549213721031866 | 0.24760851011342488 |
| Information Services | 13 | 1.2741343737591866 | 0.24950372215836075 |
| Insurance (General) | 6 | 2.1747218597829074 | 0.7834449164566614 |
| Insurance (Life) | 5 | -1.506272206263137 | 0.22208642830586212 |
| Insurance (Prop/Cas.) | 6 | 1.6550181608604664 | 0.3530960784172667 |
| Investments & Asset Management | 14 | 1.5401274045650348 | 0.3777359811397675 |
| Machinery | 221 | 1.266255080606733 | 0.1241951035232205 |
| Metals & Mining | 21 | 1.2876132885248275 | 0.38345379324987067 |
| Office Equipment & Services | 27 | 0.6790133331149948 | 0.06839043372773665 |
| Oil/Gas (Integrated) | 0 | NA | NA |
| Oil/Gas (Production and Exploration) | 2 | 0.6410229242959918 | 0.5083567657998189 |
| Oil/Gas Distribution | 3 | 0.9297715861897244 | 0.21078078599714264 |
| Oilfield Svcs/Equip. | 19 | 0.6362360803863331 | 0.6841575671192841 |
| Packaging & Container | 28 | 0.6500628399438355 | 0.1765718961237566 |
| Paper/Forest Products | 15 | 0.532979182698055 | 0.3278242090825449 |
| Power | 26 | 0.3403801374116821 | 0.6728580970265856 |
| Precious Metals | 2 | 0.5412694371956077 | 0.41999074832071054 |
| Publishing & Newspapers | 51 | 0.8281915354380376 | 0.17560693728658092 |
| R.E.I.T. | 54 | 0.3492202157192497 | 0.18933775600222527 |
| Real Estate (Development) | 20 | 0.6721376488998958 | 0.2832529710822262 |
| Real Estate (General/Diversified) | 48 | 0.5175776517490165 | 0.11720268072258394 |
| Real Estate (Operations & Services) | 42 | 0.6046095661241715 | 0.19542061799604898 |
| Recreation | 52 | 0.9538350177901406 | 0.2515275768834479 |
| Reinsurance | 0 | NA | NA |
| Restaurant/Dining | 107 | 0.5998531044498568 | 1.0139711180457125 |
| Retail (Automotive) | 23 | 0.6981535617497049 | 0.19757195712057288 |
| Retail (Building Supply) | 17 | 0.5111339446398321 | 0.3298558173052776 |
| Retail (Distributors) | 139 | 0.8071368285506627 | 0.37069776473474936 |
| Retail (General) | 42 | 0.8350093699949339 | 0.4410926904398408 |
| Retail (Grocery and Food) | 55 | 0.4443748303010394 | 0.10730814092691159 |
| Retail (REITs) | 4 | 0.2460787598060525 | 0.09653003463927379 |
| Retail (Special Lines) | 131 | 0.8864103776801079 | 0.1111000142498668 |
| Rubber& Tires | 6 | 1.5723282599621655 | 0.17221775557840238 |
| Semiconductor | 21 | 1.9900916657682015 | 0.9560463649669817 |
| Semiconductor Equip | 37 | 2.8168514950267696 | 0.4621731162310003 |
| Shipbuilding & Marine | 26 | 0.7115752320925524 | 0.7280511441546355 |
| Shoe | 3 | 1.6232735178309312 | 0.8348538180780928 |
| Software (Entertainment) | 76 | 1.202819808474296 | 0.0973284988599915 |
| Software (Internet) | 26 | 1.6448115756056694 | 0.36542975746720724 |
| Software (System & Application) | 185 | 1.8698404221888172 | 0.21563134117909508 |
| Steel | 40 | 0.7872936715342266 | 0.5607849030214328 |
| Telecom (Wireless) | 8 | 1.0135769877353136 | 0.20097965530582385 |
| Telecom. Equipment | 13 | 1.9968794881975063 | 0.2462524222542658 |
| Telecom. Services | 20 | 0.6457122637175092 | 0.1590796726568425 |
| Tobacco | 1 | 0.5039778404504659 | 0.20316486395381875 |
| Transportation | 31 | 0.5881952548838629 | 0.1854557732694076 |
| Transportation (Railroads) | 21 | 0.28014268320052765 | 0.8889261296078311 |
| Trucking | 17 | 0.5946811211454606 | 0.1412044335854013 |
| Utility (General) | 0 | NA | NA |
| Utility (Water) | 0 | NA | NA |
| Total Market | 3965 | 0.9809425497005044 | 0.10211736972559271 |
| Total Market (without financials) | 3762 | 0.961812826271152 | 0.10625301614780429 |

## Input Choices

| Effective |
|---|
| Marginal |
