---
title: "Dbtfundchina"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundChina.xls
---

# Dbtfundchina

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundChina.xls

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
| Advertising | 60 | 3.291583736138756 | 32.72609451386279 |
| Aerospace/Defense | 68 | 4.17453019521985 | 4.541226507950503 |
| Air Transport | 15 | 1.031294178244132 | 12.848663962481707 |
| Apparel | 128 | 9.01837231450212 | 3.4463957890102463 |
| Auto & Truck | 34 | 4.826202556913136 | 1.972250509794913 |
| Auto Parts | 220 | 7.315775845140995 | 3.6629573164682263 |
| Bank (Money Center) | 21 | 1.4245954418368212 | 1629.1904674849832 |
| Banks (Regional) | 37 | NA | NA |
| Beverage (Alcoholic) | 39 | 288.87937301645877 | 0.1121643933172862 |
| Beverage (Soft) | 3 | 120.5677041150835 | 0.5364493050521605 |
| Broadcasting | 4 | -0.25529265255292655 | 4.30069142631371 |
| Brokerage & Investment Banking | 59 | -3.886075949367089 | -25046.657676411935 |
| Building Materials | 62 | 4.058846522950167 | 3.9107249282126477 |
| Business & Consumer Services | 91 | 1.7116003671575046 | 6.608379331736101 |
| Cable TV | 11 | -1.3960941599820078 | 5.493573509121571 |
| Chemical (Basic) | 290 | 2.43878461629363 | 7.084382918110669 |
| Chemical (Diversified) | 5 | 14.16099667386357 | 3.325678190635973 |
| Chemical (Specialty) | 244 | 5.5680517748230365 | 3.9643373023708257 |
| Coal & Related Energy | 29 | 12.132814228836574 | 1.5517115019968857 |
| Computer Services | 116 | 1.6090330457154012 | 8.402006509795338 |
| Computers/Peripherals | 55 | 3.4906392674200917 | 3.8030371045817604 |
| Construction Supplies | 152 | 4.9056717320210215 | 4.597119644242722 |
| Diversified | 7 | 2.3285531733636233 | 9.204670966192387 |
| Drugs (Biotechnology) | 140 | -2.7468847139493864 | 12.889590417380443 |
| Drugs (Pharmaceutical) | 246 | 9.95232000075617 | 2.165571674642756 |
| Education | 44 | 5.82063598248248 | 2.7173424042355196 |
| Electrical Equipment | 344 | 6.7726776664137605 | 3.7828622916257406 |
| Electronics (Consumer & Office) | 24 | 3.9015596358105205 | 5.402134596145826 |
| Electronics (General) | 404 | 5.714037319751984 | 4.2014217433198 |
| Engineering/Construction | 135 | 2.70442732871042 | 10.034240791894682 |
| Entertainment | 88 | 16.593522970057467 | 1.131545452393754 |
| Environmental & Waste Services | 105 | 1.9592588849395525 | 9.032181242806276 |
| Farming/Agriculture | 43 | 2.619835049595511 | 6.63105620446041 |
| Financial Svcs. (Non-bank & Insurance) | 33 | 5.256843488782023 | 74.95881097372047 |
| Food Processing | 167 | 8.726914939005816 | 2.717640556023625 |
| Food Wholesalers | 1 | 24.299999999999997 | 1.5242165242165242 |
| Furn/Home Furnishings | 85 | 13.268532009606414 | 1.858211381758827 |
| Green & Renewable Energy | 32 | 3.4045976633697728 | 7.023884644300428 |
| Healthcare Products | 138 | 9.791183996625124 | 2.3026922640161818 |
| Healthcare Support Services | 57 | 4.7441622914054244 | 5.400816151789497 |
| Heathcare Information and Technology | 54 | 16.593124204190293 | 3.522040117543374 |
| Homebuilding | 2 | -0.8036935704514364 | 131.33793103448275 |
| Hospitals/Healthcare Facilities | 21 | 5.868769112668789 | 2.77372791985236 |
| Hotel/Gaming | 28 | 4.416598214049129 | 4.926185799438676 |
| Household Products | 72 | 11.200870333746836 | 3.5511864723693587 |
| Information Services | 2 | -191.70370370370372 | -0.3959131545338442 |
| Insurance (General) | 9 | 17.257108396835697 | 3.671140310751128 |
| Insurance (Life) | 4 | 13.593963873656072 | 6.556117255752168 |
| Insurance (Prop/Cas.) | 2 | 11.267312542994725 | 1.7710418430686947 |
| Investments & Asset Management | 13 | 4.051507281057578 | 378.1454214101718 |
| Machinery | 422 | 5.005053983104864 | 4.569464510130094 |
| Metals & Mining | 125 | 9.141825858104601 | 3.838297509001077 |
| Office Equipment & Services | 12 | 6.541312011005072 | 3.1098958696735957 |
| Oil/Gas (Integrated) | 4 | 7.463472242566282 | 1.488483026358687 |
| Oil/Gas (Production and Exploration) | 5 | 7.518815308673632 | 1.7159433646112605 |
| Oil/Gas Distribution | 14 | 3.6141979749071056 | 5.019535248872194 |
| Oilfield Svcs/Equip. | 51 | 4.507516880646695 | 3.370122181729407 |
| Packaging & Container | 57 | 3.647910524249099 | 4.979665934371808 |
| Paper/Forest Products | 37 | 0.7856556105018762 | 7.88185914884423 |
| Power | 82 | 3.9827682672704916 | 6.46179490770223 |
| Precious Metals | 15 | 12.38779884366775 | 3.975422834270435 |
| Publishing & Newspapers | 39 | 24.305557579909348 | 1.7518022205233357 |
| R.E.I.T. | 2 | NA | NA |
| Real Estate (Development) | 126 | -0.7505499368675771 | -152.0184905577887 |
| Real Estate (General/Diversified) | 24 | 0.07365435540943589 | 27.614903316607514 |
| Real Estate (Operations & Services) | 71 | 3.419594731509625 | 3.02094987211551 |
| Recreation | 46 | 5.080309554204443 | 3.270525080118538 |
| Reinsurance | 1 | 7.395287958115184 | 4.968822570285092 |
| Restaurant/Dining | 21 | 7.923910129229447 | 1.2990405228464599 |
| Retail (Automotive) | 23 | 2.123146266784619 | 6.176822705130868 |
| Retail (Building Supply) | 3 | 5.891438807584413 | 2.5493073539688416 |
| Retail (Distributors) | 72 | 1.9592179940739336 | 9.24515502091024 |
| Retail (General) | 48 | 1.291867673379402 | 7.511314874982518 |
| Retail (Grocery and Food) | 22 | -0.6296203139139207 | 15.688385872227236 |
| Retail (REITs) | 0 | NA | NA |
| Retail (Special Lines) | 45 | 3.9679244542390744 | 3.694696045198089 |
| Rubber& Tires | 16 | 7.653972564741855 | 2.5580008908623304 |
| Semiconductor | 178 | -1.093901342248889 | 7.360946145544685 |
| Semiconductor Equip | 65 | 0.6889199022294262 | 6.443520772153546 |
| Shipbuilding & Marine | 39 | 8.759350988068219 | 2.4565030330951267 |
| Shoe | 10 | 24.13927440954468 | 0.882496888534107 |
| Software (Entertainment) | 27 | 17.361959528065086 | 1.7959865161576365 |
| Software (Internet) | 20 | 3.0345874547491247 | 6.941958604664777 |
| Software (System & Application) | 181 | -5.821490618485061 | -12.799838113481801 |
| Steel | 101 | 1.7869267372457251 | 6.5026360762104085 |
| Telecom (Wireless) | 6 | 34.27382399616732 | 0.37745928330204426 |
| Telecom. Equipment | 111 | 4.651174263375844 | 4.785811803708139 |
| Telecom. Services | 9 | 10.931281508921913 | 0.8996032789635228 |
| Tobacco | 2 | 20.022509848058526 | 0.8101433177674857 |
| Transportation | 79 | 4.976462154502341 | 4.042051341942548 |
| Transportation (Railroads) | 9 | 12.1167760743273 | 1.522347777362719 |
| Trucking | 9 | 0.7918903506184491 | 13.450621249269645 |
| Utility (General) | 3 | 1.56527739442451 | 12.214713430282295 |
| Utility (Water) | 32 | 2.5198258059573395 | 7.957727049572802 |
| Total Market | 6307 | 4.67903050408449 | 12.58473313768637 |
| Total Market (without financials) | 6129 | 4.282015688003224 | 4.714524265173072 |
