---
title: "Dbtfundemerg"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundemerg.xls
---

# Dbtfundemerg

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundemerg.xls

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
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| Industry Name | Number of firms | Interest Coverage Ratio | Debt to EBITDA |
| Advertising | 184 | 3.0501487759659467 | 12.389531965597957 |
| Aerospace/Defense | 151 | 6.947480783146409 | 4.581690454035391 |
| Air Transport | 79 | 2.1605981238559133 | 6.578849955344707 |
| Apparel | 993 | 4.297149604079356 | 3.663234227350841 |
| Auto & Truck | 89 | 6.714305885706758 | 4.136557145212959 |
| Auto Parts | 592 | 5.343956687872142 | 3.1689534142983966 |
| Bank (Money Center) | 455 | 1.853494936942686 | 1024.9474337643042 |
| Banks (Regional) | 104 | -7.4561403508771935 | -12600.42737911597 |
| Beverage (Alcoholic) | 132 | 31.45151008059889 | 0.4365128220938935 |
| Beverage (Soft) | 40 | 17.568729700154297 | 0.9331174642544181 |
| Broadcasting | 63 | 2.1538128137117 | 4.602400513891122 |
| Brokerage & Investment Banking | 468 | 5.110665040093901 | 655.6762588724713 |
| Building Materials | 281 | 3.749288421038394 | 3.6715089757245214 |
| Business & Consumer Services | 379 | 5.016971844040289 | 4.0996842148258406 |
| Cable TV | 29 | 0.44735913678418804 | 4.627847891224388 |
| Chemical (Basic) | 741 | 1.7823071243423052 | 6.14833286276969 |
| Chemical (Diversified) | 29 | 4.811158393050749 | 3.0802030524689936 |
| Chemical (Specialty) | 687 | 5.517069614722758 | 3.258183977837081 |
| Coal & Related Energy | 96 | 10.679894040868874 | 1.4226282877883398 |
| Computer Services | 693 | 9.872239050531729 | 2.0571234688143054 |
| Computers/Peripherals | 244 | 8.593351584418047 | 1.4713612555740256 |
| Construction Supplies | 580 | 4.2782436642947514 | 4.1722729200799265 |
| Diversified | 215 | 2.2225898612187303 | 6.713263220122706 |
| Drugs (Biotechnology) | 382 | -1.4546291289261424 | 21.453076838162666 |
| Drugs (Pharmaceutical) | 753 | 8.839474324442998 | 2.2373156959138876 |
| Education | 182 | 3.463045973277899 | 2.841190632693566 |
| Electrical Equipment | 810 | 5.531047067295773 | 4.243896715430774 |
| Electronics (Consumer & Office) | 81 | 4.195727987545396 | 2.982724948940243 |
| Electronics (General) | 1050 | 5.531177469610503 | 3.8569322948489764 |
| Engineering/Construction | 999 | 2.763774122021882 | 9.004666907502562 |
| Entertainment | 343 | 7.568142198248889 | 1.8874098050408037 |
| Environmental & Waste Services | 223 | 2.074707188001126 | 8.099147585768657 |
| Farming/Agriculture | 312 | 3.6877246296794812 | 4.938999959882826 |
| Financial Svcs. (Non-bank & Insurance) | 697 | 3.2715025877775448 | 58.08814279457421 |
| Food Processing | 1030 | 4.618838706302984 | 3.6485832895380903 |
| Food Wholesalers | 121 | 1.7315907596535727 | 5.366995282292641 |
| Furn/Home Furnishings | 278 | 10.968065632825065 | 2.086262930497792 |
| Green & Renewable Energy | 154 | 2.560037322974261 | 6.88349634229725 |
| Healthcare Products | 380 | 7.062846420053628 | 2.61113360279499 |
| Healthcare Support Services | 256 | 2.7803772045948136 | 6.267544195615575 |
| Heathcare Information and Technology | 146 | 14.440460180254433 | 2.665648495581529 |
| Homebuilding | 46 | 2.714622591215713 | 8.34136775383436 |
| Hospitals/Healthcare Facilities | 164 | 3.9405086878574846 | 3.8654377890312936 |
| Hotel/Gaming | 427 | 2.3499914692092303 | 5.077071667976187 |
| Household Products | 339 | 9.833884625628814 | 3.064798331149575 |
| Information Services | 49 | 5.407670819066333 | 2.0740186344963436 |
| Insurance (General) | 140 | 6.2524298983405755 | 3.094200437223744 |
| Insurance (Life) | 92 | 8.239765993380338 | 5.1540336937342905 |
| Insurance (Prop/Cas.) | 158 | 10.224282901238208 | 1.5152204332062928 |
| Investments & Asset Management | 486 | 4.810283137971949 | 23.77511771373152 |
| Machinery | 987 | 5.739039441041236 | 4.052412772577878 |
| Metals & Mining | 358 | 7.413697781314009 | 2.9551073024044716 |
| Office Equipment & Services | 78 | 5.82253201416993 | 2.994269174404229 |
| Oil/Gas (Integrated) | 15 | 21.76883573614733 | 0.8918617833026196 |
| Oil/Gas (Production and Exploration) | 105 | 8.548472664549324 | 1.363245519229024 |
| Oil/Gas Distribution | 120 | 3.5720153117934412 | 3.9035604374740576 |
| Oilfield Svcs/Equip. | 228 | 3.768998418040327 | 3.585406999060529 |
| Packaging & Container | 341 | 2.9719119823002442 | 4.719913503604626 |
| Paper/Forest Products | 197 | 1.1754959125155304 | 6.226731757948347 |
| Power | 328 | 3.166358584024765 | 5.332164033837684 |
| Precious Metals | 64 | 12.938317872695986 | 2.6703274798942496 |
| Publishing & Newspapers | 171 | 9.002955857338055 | 2.163502217215703 |
| R.E.I.T. | 208 | 2.547960197412336 | 9.754595786796601 |
| Real Estate (Development) | 786 | 0.617373121756207 | 32.220180064512626 |
| Real Estate (General/Diversified) | 205 | 1.6002576846530068 | 10.629095087319005 |
| Real Estate (Operations & Services) | 406 | 2.9268115505929657 | 7.049595945357457 |
| Recreation | 158 | 3.314426960443332 | 4.3848668140506915 |
| Reinsurance | 27 | 12.329528504091689 | 2.191908397092787 |
| Restaurant/Dining | 184 | 3.881900499922288 | 2.2499960081129844 |
| Retail (Automotive) | 122 | 2.5003742406934686 | 4.456600789764062 |
| Retail (Building Supply) | 55 | 2.2643368259647327 | 3.025965253831141 |
| Retail (Distributors) | 731 | 1.9270345034674223 | 8.354498402424495 |
| Retail (General) | 147 | 2.8058624314004796 | 5.192157658404788 |
| Retail (Grocery and Food) | 97 | 2.932781173910323 | 4.375171834303863 |
| Retail (REITs) | 39 | 2.973094922485957 | 8.030523848198722 |
| Retail (Special Lines) | 282 | 3.746065975709254 | 3.4948074886165528 |
| Rubber& Tires | 72 | 5.441819842314751 | 2.6140450436599085 |
| Semiconductor | 546 | 18.421197879848904 | 1.6215403291923558 |
| Semiconductor Equip | 300 | 3.6058721783464605 | 6.401879398491317 |
| Shipbuilding & Marine | 252 | 6.631379573862578 | 2.307690071335952 |
| Shoe | 60 | 7.749781106307997 | 1.7834311353696417 |
| Software (Entertainment) | 67 | 16.46612029932116 | 1.856181078404119 |
| Software (Internet) | 49 | 3.7369761313909513 | 6.927241515400793 |
| Software (System & Application) | 548 | 0.2817687159597717 | 11.829836899200942 |
| Steel | 555 | 2.977584806055528 | 4.238909836431961 |
| Telecom (Wireless) | 68 | 4.109039173717456 | 1.8389361181046588 |
| Telecom. Equipment | 296 | 4.636780860428284 | 4.52312882396005 |
| Telecom. Services | 142 | 4.157423055676534 | 1.9684072290960464 |
| Tobacco | 30 | 45.86169635446592 | 0.696587105342618 |
| Transportation | 330 | 3.3145776406404295 | 4.656895938098181 |
| Transportation (Railroads) | 18 | 6.069063993543274 | 2.8657018976942488 |
| Trucking | 76 | 1.1450778153892334 | 5.980056945019665 |
| Utility (General) | 14 | 3.1749765621257637 | 4.1866747014232075 |
| Utility (Water) | 76 | 3.505343832831339 | 5.4993021954995065 |
| Total Market | 27360 | 4.513338705646066 | 7.945187513091572 |
| Total Market (without financials) | 24760 | 4.3643052225901195 | 3.891201119479393 |
