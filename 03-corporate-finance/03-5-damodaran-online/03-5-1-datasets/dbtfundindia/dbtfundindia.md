---
title: "Dbtfundindia"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundIndia.xls
---

# Dbtfundindia

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundIndia.xls

Sheets: Variables & FAQ, Industry Averages

## Variables & FAQ

| End Game | To estimate how much debt companies have used in funding, and some of the fundamentals driving that debt choice. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Total Debt | I use all interest bearing debt, short term as well as long term, and add on the PV of lease commitments as debt. (See lease debt for details) |
| Capital (Market) | Market capital = Total Debt (including lease debt), as of last balance sheet + Market capitalization (as of year end).  |
| Capital (Book) | Book Capital = Total Debt (including lease debt), as of last balance sheet + Book Value of Equity, as of last balance sheet |
| Market Debt to Capital | Total debt aggregated across all firms in group, based upon last balance sheet/ (Aggregated total debt, from last balance sheet + Aggregated Market Capitalization, as of end of most recent year) |
| Book Debt to Capital | Total debt aggregated across all firms in group, based upon last balance sheet/ (Aggregated Total debt + Aggregated Book Value of Equity, based upon last balance sheet) |
| Market Debt to Capital | Total debt aggregated across all firms in group, based upon last balance sheet/ Market Capitalization, as of end of most recent year |
| Book Debt to Capital | Total debt aggregated across all firms in group, based upon last balance sheet/ Book Value of Equity, based upon last balance sheet) |
| Effective Tax Rate | Effective tax rate = Accrual taxes in  income statement/ Accrual taxable income in income statement, all from trailing 12 month data, and based upon aggregated numbers across all firms in group |
| Institutional Holdings | Simple average across all firms in group of percent of outstanding shares held by institutional investors, as of the most recent filings with institutional authorities. |
| Net PP&E/ Total Assets | Net property, plant and equipment, aggregated across all firms in group as reported on the most recent balance sheet. |
| EBITDA/EV | Aggregated EBITDA across firms in group, based upon TTM/ Aggregated Market Cap end of most recent year + Aggregated Total Debt in most recent balance sheet - Aggregated Cash & Marketable Securities in most recent balance sheet. |
| Standard deviation (equity) | Simple average across firms of each firm's standard deviation in stock prices in the prior 2 years, using weekly returns. |
| Capital Spending/ Total Assets | Aggregated Capital Expenditures across firms in group, based upon TTM/ Aggregated Total Book value of Assets  in most recent balance sheet |

## Industry Averages

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | The choice of whether to use debt or equity is fundamental to every business, and this dataset provides debt startistics that you can use to compare firms and industries. |
| What is this data? | Debt to capital & debt to equity ratios, with key drivers. |  |  |
| Home Page: | damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Industry Name | Number of firms | Interest Coverage Ratio | Debt to EBITDA |
| Advertising | 24 | 18.066368010618884 | 0.8462697138981826 |
| Aerospace/Defense | 23 | 84.82233545647557 | 1.6589663140006083 |
| Air Transport | 5 | 1.4683343104185336 | 7.989206472583382 |
| Apparel | 386 | 3.0751268019734135 | 4.812517379861829 |
| Auto & Truck | 19 | 6.236186974373721 | 5.345479871759672 |
| Auto Parts | 120 | 4.326470460069529 | 2.4927743311126225 |
| Bank (Money Center) | 35 | NA | NA |
| Banks (Regional) | 6 | NA | NA |
| Beverage (Alcoholic) | 22 | 9.22171729251375 | 1.6613967025452048 |
| Beverage (Soft) | 5 | 17.640462342088693 | 0.46803158187102933 |
| Broadcasting | 19 | 4.121971527791882 | 2.1305631366519324 |
| Brokerage & Investment Banking | 186 | 3.065531308683549 | 100.1748495199771 |
| Building Materials | 67 | 5.8031549427436255 | 2.182892621281644 |
| Business & Consumer Services | 75 | 12.190689240259626 | 3.9612812659386893 |
| Cable TV | 8 | -0.3043153289806326 | 0.9006126528387114 |
| Chemical (Basic) | 152 | 4.945962368262235 | 1.871908397314781 |
| Chemical (Diversified) | 8 | 11.151687495322905 | 1.0649126530762913 |
| Chemical (Specialty) | 202 | 5.182451261316296 | 2.119699337287771 |
| Coal & Related Energy | 5 | 33.419143581213476 | 0.2832907499620057 |
| Computer Services | 196 | 32.67740198096867 | 0.4835659041469408 |
| Computers/Peripherals | 12 | 10.059546313799624 | 1.0118752950939294 |
| Construction Supplies | 109 | 2.9090247963225657 | 4.420181714721196 |
| Diversified | 13 | 3.2245154749529106 | 5.376948080010314 |
| Drugs (Biotechnology) | 9 | 1.759757477037238 | 5.039101468671104 |
| Drugs (Pharmaceutical) | 188 | 13.682562817354329 | 1.0248316107068367 |
| Education | 40 | 1.3505459387483352 | 6.023076147179123 |
| Electrical Equipment | 139 | 7.92430728071853 | 1.339274077046909 |
| Electronics (Consumer & Office) | 9 | 8.322732012513036 | 1.2427833489751734 |
| Electronics (General) | 37 | 7.174030940378936 | 2.0090099362852665 |
| Engineering/Construction | 219 | 3.4160163568333504 | 3.4051719384580426 |
| Entertainment | 66 | 1.1001454096120125 | 7.758708020314597 |
| Environmental & Waste Services | 20 | 6.243655828707373 | 1.6197464360930014 |
| Farming/Agriculture | 75 | 4.828141594745359 | 1.9318447729559671 |
| Financial Svcs. (Non-bank & Insurance) | 291 | 2.158774362376865 | 93.23138697282643 |
| Food Processing | 220 | 5.519639303646496 | 1.8698644713578294 |
| Food Wholesalers | 41 | 4.907048940832726 | 3.601933542913158 |
| Furn/Home Furnishings | 52 | 7.379861754754278 | 1.5378248212025152 |
| Green & Renewable Energy | 18 | 1.6773246614968227 | 8.581097375383901 |
| Healthcare Products | 19 | 10.220761862330141 | 1.2564866633820047 |
| Healthcare Support Services | 45 | 8.5803112666617 | 2.5008960797850843 |
| Heathcare Information and Technology | 25 | 9.902169021690218 | 0.5103095954870724 |
| Homebuilding | 1 | -0.14285714285714285 | NA |
| Hospitals/Healthcare Facilities | 42 | 6.115455601227853 | 2.2246982106561344 |
| Hotel/Gaming | 80 | 4.0962461875834935 | 2.789014384769065 |
| Household Products | 43 | 24.910254287186266 | 0.7027578959752404 |
| Information Services | 26 | 6.2163873089060635 | 1.9313796850700993 |
| Insurance (General) | 2 | 4.117394108793807 | 5.285536159600998 |
| Insurance (Life) | 9 | 125.0947505373911 | 0.10951521682625007 |
| Insurance (Prop/Cas.) | 3 | 25.088368269625978 | 0.1570465689576637 |
| Investments & Asset Management | 115 | 12.001331693744437 | 2.903145605741429 |
| Machinery | 187 | 7.388236760354683 | 2.4080920478408587 |
| Metals & Mining | 51 | 6.719821038260123 | 1.8592514475972672 |
| Office Equipment & Services | 20 | 16.724033686028935 | 0.6514326165940135 |
| Oil/Gas (Integrated) | 1 | 7.663186514410006 | 1.975789484180402 |
| Oil/Gas (Production and Exploration) | 7 | 4.074422961597891 | 4.05324704452771 |
| Oil/Gas Distribution | 12 | 5.471029183884299 | 1.508918798329551 |
| Oilfield Svcs/Equip. | 30 | 5.26804359829222 | 2.567456527611327 |
| Packaging & Container | 101 | 3.0167465517884833 | 3.047193712863085 |
| Paper/Forest Products | 55 | 2.039075850043593 | 2.662419133651561 |
| Power | 33 | 2.857717591452981 | 3.8425484993292383 |
| Precious Metals | 1 | -6.371794871794871 | -3.4871099050203527 |
| Publishing & Newspapers | 25 | 6.367336529633785 | 1.607513810511755 |
| R.E.I.T. | 5 | 1.936561640938888 | 2.2575833144411703 |
| Real Estate (Development) | 156 | 1.721604731971279 | 7.376193853799899 |
| Real Estate (General/Diversified) | 16 | 3.211700489988977 | 2.712668467350794 |
| Real Estate (Operations & Services) | 42 | 1.2213860917927286 | 14.456521061911612 |
| Recreation | 15 | 5.742635350318472 | 1.0043483370701713 |
| Reinsurance | 1 | 153.24968632371395 | 0 |
| Restaurant/Dining | 19 | -1.8265475040892338 | 69.68699581175589 |
| Retail (Automotive) | 10 | 1.661708294263064 | 5.259689263615965 |
| Retail (Building Supply) | 3 | -2.0095795635976583 | -1.0137497202541892 |
| Retail (Distributors) | 276 | 1.6491463446069792 | 7.083786726183325 |
| Retail (General) | 11 | -0.03569983000080955 | 6.998472170663075 |
| Retail (Grocery and Food) | 13 | 26.27604260696876 | 0.4191647995055243 |
| Retail (REITs) | 1 | 2.563894523326572 | 3.4442116291251965 |
| Retail (Special Lines) | 61 | 2.584966849439676 | 4.172411582862583 |
| Rubber& Tires | 18 | 4.817257734343959 | 1.5717440176702369 |
| Semiconductor | 18 | 12.295297573367911 | 1.1492884717514231 |
| Semiconductor Equip | 2 | 3.8616600790513833 | 3.2697030268418046 |
| Shipbuilding & Marine | 28 | 4.862693312710436 | 2.911396765905161 |
| Shoe | 13 | 3.6906886203260605 | 2.016274689358914 |
| Software (Entertainment) | 4 | 23.22770700636942 | 0.3853240561783275 |
| Software (Internet) | 6 | 2.0096818810511756 | 4.284767114205205 |
| Software (System & Application) | 82 | 27.684753025652896 | 0.4473234179123146 |
| Steel | 185 | 3.193072815116542 | 3.1207481593596955 |
| Telecom (Wireless) | 4 | 1.3708952124984612 | 4.79312785590377 |
| Telecom. Equipment | 22 | 0.5113687993061008 | 7.244853740704078 |
| Telecom. Services | 11 | 1.9859005954394382 | 3.8224320739760915 |
| Tobacco | 7 | 343.1795827992075 | 0.2839043227014883 |
| Transportation | 59 | 1.7434568103142818 | 4.55555466318134 |
| Transportation (Railroads) | 3 | 19.47378253829867 | 0.4876905990972311 |
| Trucking | 24 | 3.529752371565847 | 2.4987901701323247 |
| Utility (General) | 0 | NA | NA |
| Utility (Water) | 1 | 12.627551020408163 | 0.5441767068273093 |
| Total Market | 5170 | 4.546458898524127 | 6.1359127135683265 |
| Total Market (without financials) | 4523 | 4.476317124668068 | 2.8458879075973185 |
