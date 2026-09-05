---
title: "Dbtfundeurope"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundEurope.xls
---

# Dbtfundeurope

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/dbtfundEurope.xls

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
| Advertising | 83 | 5.128692032873093 | 3.691773147847165 |
| Aerospace/Defense | 67 | 8.243552785942251 | 2.221251992021115 |
| Air Transport | 33 | 4.5806061972832035 | 4.108667661042873 |
| Apparel | 109 | 11.275614856671556 | 2.364778996465167 |
| Auto & Truck | 31 | 6.5136741432015945 | 6.554579302966255 |
| Auto Parts | 58 | 2.9936173546713256 | 3.4533337604551644 |
| Bank (Money Center) | 113 | 0.4733441033925686 | 540131.0188110939 |
| Banks (Regional) | 69 | NA | NA |
| Beverage (Alcoholic) | 52 | 4.823710836817218 | 3.865667547969374 |
| Beverage (Soft) | 14 | 7.442030951905394 | 3.5612397409224674 |
| Broadcasting | 18 | 5.934463354239993 | 2.2170109020470004 |
| Brokerage & Investment Banking | 69 | 1.8444788449542824 | 98.23080456437708 |
| Building Materials | 84 | 8.66288906673045 | 2.5984488769853793 |
| Business & Consumer Services | 176 | 4.993933126491675 | 3.605987962379859 |
| Cable TV | 2 | -0.5691859161246917 | 7.518460543436191 |
| Chemical (Basic) | 58 | 0.5301115967810436 | 7.818099933237305 |
| Chemical (Diversified) | 7 | 3.2419631969424114 | 4.1493784088097865 |
| Chemical (Specialty) | 92 | 7.0392890357704525 | 2.7956124969513487 |
| Coal & Related Energy | 15 | 3.462027103331452 | 1.3381358339328997 |
| Computer Services | 210 | 8.613498679202474 | 1.9369422458039702 |
| Computers/Peripherals | 38 | 9.366271485573966 | 1.5454262769773448 |
| Construction Supplies | 119 | 6.155380265289025 | 3.422712379725836 |
| Diversified | 72 | 3.7729924297851247 | 2.954660761365129 |
| Drugs (Biotechnology) | 199 | 1.214439285652183 | 833.2479712124555 |
| Drugs (Pharmaceutical) | 115 | 11.440959462433662 | 2.078905224454144 |
| Education | 18 | 5.687046520342005 | 2.0620083649264322 |
| Electrical Equipment | 146 | 0.4070053838847087 | 2.46590542612387 |
| Electronics (Consumer & Office) | 17 | 3.3936721468810354 | 1.1339045653026332 |
| Electronics (General) | 142 | 8.381355942175654 | 2.237182294380151 |
| Engineering/Construction | 160 | 3.544793134107001 | 4.533816514387811 |
| Entertainment | 199 | 4.17276511409185 | 3.6925504405513996 |
| Environmental & Waste Services | 48 | 2.8113263645624333 | 5.214748209694693 |
| Farming/Agriculture | 46 | 4.977053907954018 | 6.010908794041599 |
| Financial Svcs. (Non-bank & Insurance) | 146 | 5.22278801036452 | 77.43263599749415 |
| Food Processing | 173 | 5.289676225900568 | 3.6941772202297924 |
| Food Wholesalers | 11 | 1.0869668643484054 | 7.123597624210428 |
| Furn/Home Furnishings | 53 | 1.451889358005658 | 6.993460966520409 |
| Green & Renewable Energy | 60 | 1.943451703456184 | 6.611828091521623 |
| Healthcare Products | 163 | 4.739960983214147 | 3.107056076414712 |
| Healthcare Support Services | 47 | 4.020227275310915 | 5.206256250417843 |
| Heathcare Information and Technology | 89 | 5.396675214084178 | 3.4039571830455273 |
| Homebuilding | 36 | 6.222065522192058 | 2.418386551661135 |
| Hospitals/Healthcare Facilities | 29 | 1.3771052105125747 | 9.028963099017556 |
| Hotel/Gaming | 103 | 3.5516831289971433 | 3.835943920140503 |
| Household Products | 65 | 11.53468959132408 | 2.136402389217406 |
| Information Services | 6 | 3.7869077513721745 | 4.258931118142182 |
| Insurance (General) | 34 | 8.602052744699812 | 3.1790613367968663 |
| Insurance (Life) | 15 | 2.482582194037761 | 6.847698548281573 |
| Insurance (Prop/Cas.) | 19 | 14.058358539314527 | 1.8705886186345035 |
| Investments & Asset Management | 338 | 14.89216576155241 | 10.034130668460856 |
| Machinery | 210 | 10.645658454396761 | 1.8716347979975874 |
| Metals & Mining | 118 | 4.260210310159249 | 2.2173277463342496 |
| Office Equipment & Services | 20 | 4.458146680981821 | 2.3609420085046433 |
| Oil/Gas (Integrated) | 12 | 17.10504007270008 | 0.9855933906347605 |
| Oil/Gas (Production and Exploration) | 83 | 7.214282220821482 | 1.5495011745754363 |
| Oil/Gas Distribution | 30 | 2.510583118417138 | 3.6977333528334593 |
| Oilfield Svcs/Equip. | 58 | 5.698131934621164 | 2.38943495419272 |
| Packaging & Container | 42 | 2.9957070655626294 | 4.418452732564647 |
| Paper/Forest Products | 36 | 3.7038498927326358 | 3.191531808211261 |
| Power | 69 | 4.0028755843611865 | 3.9452755796225163 |
| Precious Metals | 39 | 7.659966201191854 | 0.8797738236841395 |
| Publishing & Newspapers | 59 | 2.79160114797729 | 4.17947952610731 |
| R.E.I.T. | 138 | 2.787446993038459 | 10.160975469940453 |
| Real Estate (Development) | 61 | 1.3166226247205675 | 15.525986657180571 |
| Real Estate (General/Diversified) | 45 | 0.7086258118595649 | 20.590367934528395 |
| Real Estate (Operations & Services) | 219 | 1.629150749957925 | 19.243966035579263 |
| Recreation | 59 | 4.284760302076923 | 3.1109827431525905 |
| Reinsurance | 4 | 23.755489906450027 | 3.492055525471187 |
| Restaurant/Dining | 38 | 3.5193598816024134 | 3.9147550496049033 |
| Retail (Automotive) | 22 | 2.033572221789072 | 4.01576653913353 |
| Retail (Building Supply) | 26 | 4.375438296989205 | 4.666954357960189 |
| Retail (Distributors) | 117 | 3.4907410690973655 | 4.827464505498518 |
| Retail (General) | 31 | 2.510426992707507 | 7.058586334446199 |
| Retail (Grocery and Food) | 34 | 2.8981609011593736 | 4.155266963907776 |
| Retail (REITs) | 28 | 2.723824716314639 | 11.166056534868721 |
| Retail (Special Lines) | 105 | 4.784684716076048 | 2.870051262644293 |
| Rubber& Tires | 10 | 5.119057064361612 | 2.2154625583347443 |
| Semiconductor | 36 | 5.549578710877466 | 2.125365332937408 |
| Semiconductor Equip | 21 | 41.75286278944744 | 0.6008347505831565 |
| Shipbuilding & Marine | 65 | 4.864965719437083 | 2.300824388978351 |
| Shoe | 9 | 4.147125938467577 | 3.312458684748247 |
| Software (Entertainment) | 51 | 3.211884996791546 | 1.9783579659014328 |
| Software (Internet) | 23 | 4.748817207670135 | 3.6085159866143894 |
| Software (System & Application) | 290 | 10.35968816557486 | 2.0580726899689665 |
| Steel | 57 | 1.3562810021209701 | 3.4777862148685434 |
| Telecom (Wireless) | 11 | 1.9985489462315438 | 4.952040159353056 |
| Telecom. Equipment | 50 | 4.582122934824575 | 2.334211648195407 |
| Telecom. Services | 62 | 3.203069268758721 | 4.120245451707647 |
| Tobacco | 5 | 6.39673390970221 | 3.035553866286903 |
| Transportation | 56 | 2.8959212458499657 | 7.308027783442291 |
| Transportation (Railroads) | 8 | -0.9114909081333034 | 15.957059713819696 |
| Trucking | 7 | 3.269552050729646 | 4.404433149795285 |
| Utility (General) | 18 | 4.544640781061527 | 4.297077699300838 |
| Utility (Water) | 12 | 1.9680163212815702 | 11.457757669930798 |
| Grand Total | 6560 | 4.706249083206302 | 7.3829105402614825 |
| Total Market (without financials) | 5757 | 4.539915052287148 | 3.1279454899406853 |
