---
title: "Dbtfund"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/dbtfund.xls
---

# Dbtfund

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/dbtfund.xls

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
| Interest Coverage Ratio | Earnings before Interest & Taxes/ Interest Expense |
| Total Debt/ EBITDA | Total Debt (including lease debt)/ EBITDA |
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
| Advertising | 52 | 2.7444609200483145 | 4.698068355002595 |
| Aerospace/Defense | 79 | 3.7068180175154835 | 4.620862256566636 |
| Air Transport | 23 | 2.461213997244209 | 5.130506126430948 |
| Apparel | 35 | 7.93123770208512 | 3.4713045625614747 |
| Auto & Truck | 33 | 3.9119829781571585 | 8.794476936637434 |
| Auto Parts | 35 | 4.235136915036808 | 2.947830238886613 |
| Bank (Money Center) | 15 | 7 | 7 |
| Banks (Regional) | 568 | 2.9999999999999996 | 7 |
| Beverage (Alcoholic) | 14 | 8.130642741802003 | 2.5741116240197894 |
| Beverage (Soft) | 27 | 9.61127494008716 | 3.2251316947778843 |
| Broadcasting | 24 | 2.415851440531456 | 3.896077028563622 |
| Brokerage & Investment Banking | 32 | -0.7610640582130501 | -473069.70969534223 |
| Building Materials | 41 | 7.313258971952832 | 2.517050019506898 |
| Business & Consumer Services | 155 | 5.526771094598775 | 2.7744679983704565 |
| Cable TV | 9 | 3.109710857352223 | 3.891057029816174 |
| Chemical (Basic) | 29 | 1.221971791465468 | 3.7481099247892518 |
| Chemical (Diversified) | 4 | 1.0580959855879393 | 6.145180466872074 |
| Chemical (Specialty) | 59 | 4.948983338652349 | 3.5201611259037136 |
| Coal & Related Energy | 16 | -2.929438543247344 | 1.5084409618718648 |
| Computer Services | 64 | 6.44944864620941 | 3.4682501998208823 |
| Computers/Peripherals | 36 | 42.454789830535084 | 1.1747026489248367 |
| Construction Supplies | 40 | 11.84974048318402 | 2.562814927467329 |
| Diversified | 20 | 11.56881639725435 | 1.4165901052969958 |
| Drugs (Biotechnology) | 496 | 1.8839366409725133 | 6.200525443723345 |
| Drugs (Pharmaceutical) | 228 | 10.49365451017941 | 2.4347443782439533 |
| Education | 32 | 5.840460875202787 | 2.5667572178760465 |
| Electrical Equipment | 112 | 4.095265890321236 | 3.882995560119734 |
| Electronics (Consumer & Office) | 8 | -10.545201668984703 | -2.1084215535297064 |
| Electronics (General) | 114 | 8.122010400969847 | 2.6873226337461054 |
| Engineering/Construction | 48 | 5.34507244782538 | 2.7837106701372316 |
| Entertainment | 92 | 3.6691397618032253 | 3.4646028104307747 |
| Environmental & Waste Services | 53 | 5.180905325998061 | 3.1525800842496152 |
| Farming/Agriculture | 35 | 5.927969070470167 | 5.919314242865338 |
| Financial Svcs. (Non-bank & Insurance) | 176 | 8.210422263640451 | 67.59006139930702 |
| Food Processing | 78 | 5.556198640728189 | 3.0058082372935044 |
| Food Wholesalers | 13 | 3.753139100582401 | 3.978483399664377 |
| Furn/Home Furnishings | 27 | 3.86561061790219 | 4.241651749354123 |
| Green & Renewable Energy | 15 | 0.5328778415792235 | 7.280862862573533 |
| Healthcare Products | 204 | 6.801400223408523 | 2.744225326781411 |
| Healthcare Support Services | 104 | 5.256713254361942 | 3.3497346332859674 |
| Heathcare Information and Technology | 115 | 5.0664097842591485 | 3.612078295098431 |
| Homebuilding | 30 | 84.5950924147911 | 1.6108619298660771 |
| Hospitals/Healthcare Facilities | 31 | 4.259640542519798 | 4.098997652248294 |
| Hotel/Gaming | 63 | 3.064127211159889 | 5.2964688047032595 |
| Household Products | 110 | 10.430896645863283 | 2.1713021469523546 |
| Information Services | 15 | 3.702866063257946 | 3.272816353120904 |
| Insurance (General) | 21 | 5.049417779158126 | 3.8390175353211324 |
| Insurance (Life) | 20 | 5.960543774296422 | 5.615639657870967 |
| Insurance (Prop/Cas.) | 57 | 16.874542716274817 | 1.3689480486735097 |
| Investments & Asset Management | 283 | 11.436458550203355 | 12.878560237517078 |
| Machinery | 105 | 7.757107648810433 | 2.303926451574374 |
| Metals & Mining | 73 | 12.74274448736937 | 1.4258754616918363 |
| Office Equipment & Services | 14 | 4.769526826682027 | 3.440152875888478 |
| Oil/Gas (Integrated) | 4 | 20.429871064158167 | 1.0084348202352316 |
| Oil/Gas (Production and Exploration) | 142 | 6.590095417903713 | 1.7436893592512848 |
| Oil/Gas Distribution | 23 | 3.1673927494475635 | 4.97363749301724 |
| Oilfield Svcs/Equip. | 97 | 4.090638238612397 | 2.753552815111632 |
| Packaging & Container | 19 | 3.7179652380287584 | 3.969217458607076 |
| Paper/Forest Products | 6 | 3.2242731887401943 | 2.2589508615833944 |
| Power | 46 | 2.4474352026471347 | 5.741858133001844 |
| Precious Metals | 56 | 21.795623312414826 | 1.228312814508863 |
| Publishing & Newspapers | 19 | 6.095721564989772 | 2.6712312498179136 |
| R.E.I.T. | 190 | 2.1216938539094734 | 11.352224398507207 |
| Real Estate (Development) | 14 | 4.103066841953906 | 7.236137976575014 |
| Real Estate (General/Diversified) | 12 | 5.384045001278445 | 9.500691521210326 |
| Real Estate (Operations & Services) | 54 | 2.2518948342249923 | 7.6886718848791284 |
| Recreation | 49 | 2.2621645974958535 | 4.776285302663746 |
| Reinsurance | 1 | 4.545197740112994 | 4.369632986142593 |
| Restaurant/Dining | 64 | 5.968117709188069 | 4.6715625405729835 |
| Retail (Automotive) | 34 | 4.3631983071820235 | 5.594771601481677 |
| Retail (Building Supply) | 14 | 7.758784510146808 | 3.0264753707175553 |
| Retail (Distributors) | 62 | 4.953732222909459 | 3.7569793007757384 |
| Retail (General) | 23 | 18.365572023422185 | 1.5783228374122342 |
| Retail (Grocery and Food) | 15 | 3.930441388505605 | 3.2687315071890968 |
| Retail (REITs) | 26 | 2.248694171082514 | 6.564277444440871 |
| Retail (Special Lines) | 94 | 13.489272967000522 | 2.8754411886105085 |
| Rubber& Tires | 3 | 0.8692569483834374 | 5.670334067640755 |
| Semiconductor | 66 | 23.060846512933892 | 1.0895886871730622 |
| Semiconductor Equip | 31 | 18.240270172395945 | 1.252959846179592 |
| Shipbuilding & Marine | 8 | 10.644990222398993 | 1.6062107469055027 |
| Shoe | 11 | 13.41581788427249 | 1.9646678206478112 |
| Software (Entertainment) | 77 | 86.01115910297268 | 0.5281936302889443 |
| Software (Internet) | 29 | 0.9465409737878505 | 11.317141700281748 |
| Software (System & Application) | 309 | 18.949263444949988 | 1.7085431505706046 |
| Steel | 19 | 4.220450964618747 | 2.200022294567489 |
| Telecom (Wireless) | 12 | 4.773828326322964 | 3.7248851593025902 |
| Telecom. Equipment | 57 | 6.996965091634613 | 2.3603013891220934 |
| Telecom. Services | 39 | 3.607771037933395 | 3.854450947286364 |
| Tobacco | 10 | 9.150846949892799 | 2.88232309185308 |
| Transportation | 19 | 4.3878156590244854 | 4.6961758966557925 |
| Transportation (Railroads) | 4 | 6.118799579470514 | 2.971645316992624 |
| Trucking | 26 | 4.060975822995257 | 2.303008467785602 |
| Utility (General) | 14 | 2.5667633793396423 | 6.77498342345563 |
| Utility (Water) | 14 | 3.0616231610739186 | 6.038753850743742 |
| Total Market | 5994 | 6.901889107221006 | 6.524437901758324 |
| Total Market (without financials) | 4822 | 6.727925091456003 | 3.006945284950977 |
