---
title: "Eva"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pc/datasets/EVA.xls
---

# Eva

Source: http://www.stern.nyu.edu/~adamodar/pc/datasets/EVA.xls

Sheets: Variables & FAQ, Industry Averages

## Variables & FAQ

| End Game | To estimate how much firms earn on their investments, relative to what they need to earn to break even, given the risk. |
|---|---|
|  |  |
| Variable | Explanation |
| Number of firms | Number of firms in the indusry grouping. |
| Beta | Average regression beta across companies in the group. |
| ROE | Aggregated Net Income , across all firms in group, using trailing 12 month data/ Aggregated Book Value of equity, across all firms in group, using most recent balance sheet. |
| Cost of Equity | Risk free Rate + Beta * Equity Risk Premium  |
| (ROE - COE) | ROE - Cost of Equity, across the sector |
| BV of Equity | Aggregated Book Value of Equity, in most recent balance sheet, across all firms in the group (in milliona of dollars) |
| Equity EVA | (ROE - Cost of Equity)* BV of Equity, defined as above, and aggregated across companies (in $ millions) |
| ROC | Aggregated Operating income , across all firms in group, using trailing 12 month data (1- Effective Tax Rate)/ (BV of Equity + BV of Debt - Cash), across all firms in group, using most recent balance sheet. |
| Cost of Capital | Cost of Equity * (Equity/ (Debt + Equity)) + Cost of Debt (1- Marginal tax rate) *(Debt/ (Debt + Equity)), with aggregated debt and market equity values across all companies in the sector, using most recent balance sheet for debt and most recent year-end for equity. |
| (ROC - Cost of Capital) | ROC- Cost of Capital, averaged across the sector |
| BV of Capital | (Book Value of Equity + BV of Debt - Cash), aggregated across all firms in the group, in most recent balance sheet. |
| EVA | (ROC - Cost of Capital)* BV of Capital, defined as above, and aggregated across companies (in $ millions) |

## Industry Averages

| Date updated: | 46027.0 | YouTube Video explaining estimation choices and process. | Notes |
|---|---|---|---|
| Created by: | Aswath Damodaran, adamodar@stern.nyu.edu |  | The choice of how much to return to shareholders in a business and in what form (dividends or buybacks) is one that every business has to make, and this datasets includes statistics on cash return. |
| What is this data? | Excess Returns (equity and firm) in percent and (millions of) dollar terms |  |  |
| Home Page: | http://www.damodaran.com |  |  |
| Data website: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html |  |  |
| Companies in each industry: | https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xls |  |  |
| Variable definitions: | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm |  |  |
| To update this spreadsheet, enter the following |  |  |  |
| Long Term Treasury bond rate = |  |  | Standard Deviation |
| Risk Premium to Use for Equity = |  |  | 0 |
| Country Default Spread to use for debt = |  |  | 0.30001 |
|  |  |  | 0.45001 |
| Do you want to use the marginal tax rate? |  |  | 0.650001 |
| Marginal tax rate = |  |  | 0.800001 |
|  |  |  | 0.900001 |
|  |  |  | 1.000001 |
|  |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Equity EVA (US $ millions) | ROC |
| Advertising | 52 | -886.6355596654305 | 0.2772269074749548 |
| Aerospace/Defense | 79 | 11617.548176746232 | 0.16012360749257398 |
| Air Transport | 23 | 2147.3041490800497 | 0.07929312533704834 |
| Apparel | 35 | 536.1763970212049 | 0.15768515602445898 |
| Auto & Truck | 33 | -14806.218478145884 | 0.022474128513756082 |
| Auto Parts | 35 | -2257.9586495749195 | 0.08975948273328078 |
| Bank (Money Center) | 15 | 61645.89084681365 | NA |
| Banks (Regional) | 568 | 20820.94627032028 | NA |
| Beverage (Alcoholic) | 14 | -1892.5219698780286 | 0.15744765776572892 |
| Beverage (Soft) | 27 | 19003.0201062394 | 0.2902563541349132 |
| Broadcasting | 24 | -761.9473944653162 | 0.14567294791803095 |
| Brokerage & Investment Banking | 32 | 24884.652819706367 | NA |
| Building Materials | 41 | 4110.229452006594 | 0.20164568716545334 |
| Business & Consumer Services | 155 | 10716.214954192234 | 0.28297691435712685 |
| Cable TV | 9 | 5372.40004536118 | 0.12062120565621212 |
| Chemical (Basic) | 29 | -8684.375750059584 | 0.037245953068641535 |
| Chemical (Diversified) | 4 | -984.3732271027602 | 0.040542644509719825 |
| Chemical (Specialty) | 59 | -8264.066024197677 | 0.10949443918503624 |
| Coal & Related Energy | 16 | -822.3594938600377 | -0.04759627013362316 |
| Computer Services | 64 | 7879.218949953631 | 0.26348563236851774 |
| Computers/Peripherals | 36 | -11614.982019988467 | 0.4476035274383902 |
| Construction Supplies | 40 | 13000.10479317505 | 0.16706062867511484 |
| Diversified | 20 | 22982.439107042657 | 0.14821356557111473 |
| Drugs (Biotechnology) | 496 | -28319.886825488833 | 0.03525374326558564 |
| Drugs (Pharmaceutical) | 228 | 47072.29778657818 | 0.16949548287090127 |
| Education | 32 | 1306.8814433485102 | 0.15944153901851482 |
| Electrical Equipment | 112 | -6638.282927571321 | 0.15595603913111394 |
| Electronics (Consumer & Office) | 8 | -303.40580913251847 | -0.0834551474050309 |
| Electronics (General) | 114 | 3822.3377732351605 | 0.17911725405258233 |
| Engineering/Construction | 48 | 6377.488025603699 | 0.2531760347582192 |
| Entertainment | 92 | -2892.5169397839427 | 0.12420599801084616 |
| Environmental & Waste Services | 53 | 3803.247043637874 | 0.31754796538384716 |
| Farming/Agriculture | 35 | 2206.0365465838104 | 0.07277942934792668 |
| Financial Svcs. (Non-bank & Insurance) | 176 | 92502.12137255528 | NA |
| Food Processing | 78 | -3626.5109802345087 | 0.15949707214923414 |
| Food Wholesalers | 13 | 1551.940161554171 | 0.17837019301943033 |
| Furn/Home Furnishings | 27 | -860.1517485537859 | 0.1058742891265975 |
| Green & Renewable Energy | 15 | -1432.1772674316098 | 0.036367416094179386 |
| Healthcare Products | 204 | 7939.630916507429 | 0.16980778635574598 |
| Healthcare Support Services | 104 | 7031.964164270245 | 0.3119296654846798 |
| Heathcare Information and Technology | 115 | -4464.035255789326 | 0.13716783348113318 |
| Homebuilding | 30 | 7003.740283407164 | 0.1490812879349228 |
| Hospitals/Healthcare Facilities | 31 | 9022.036744169436 | 0.22163970318779982 |
| Hotel/Gaming | 63 | 19719.28945978685 | 0.14575119045322596 |
| Household Products | 110 | 17919.552524218467 | 0.34419837512001855 |
| Information Services | 15 | 1218.6910441588275 | 0.2217430042193927 |
| Insurance (General) | 21 | 4479.953033913128 | 0.4450609958826383 |
| Insurance (Life) | 20 | 8840.485570855959 | 0.1076576568830416 |
| Insurance (Prop/Cas.) | 57 | 32800.38021217528 | 0.18488979223477825 |
| Investments & Asset Management | 283 | 20909.55691122696 | 0.14253207300518655 |
| Machinery | 105 | 10356.399880467226 | 0.24408325788322105 |
| Metals & Mining | 73 | 3313.678395688581 | 0.2704361776786952 |
| Office Equipment & Services | 14 | 149.38538580138862 | 0.18260160203320722 |
| Oil/Gas (Integrated) | 4 | 21092.18684868391 | 0.0844906040235468 |
| Oil/Gas (Production and Exploration) | 142 | 14646.286384943787 | 0.13731095270967508 |
| Oil/Gas Distribution | 23 | 8751.05675844565 | 0.12351055159122301 |
| Oilfield Svcs/Equip. | 97 | 801.763754486174 | 0.11937951003115008 |
| Packaging & Container | 19 | 1533.5043153039421 | 0.14816927195835602 |
| Paper/Forest Products | 6 | -65.3622158456021 | 0.1041420566237548 |
| Power | 46 | 25356.155558258517 | 0.06921872420290816 |
| Precious Metals | 56 | 6990.938981143874 | 0.25451637862422194 |
| Publishing & Newspapers | 19 | 1048.4898702401185 | 0.17632773244458913 |
| R.E.I.T. | 190 | -9836.105903492275 | 0.03203080280639824 |
| Real Estate (Development) | 14 | -136.34595561847902 | 0.07043355884782262 |
| Real Estate (General/Diversified) | 12 | 69.43757767728866 | 0.05194923071492735 |
| Real Estate (Operations & Services) | 54 | -1995.9938661094334 | 0.059426974075348735 |
| Recreation | 49 | -4342.9551037601295 | 0.08024512691065157 |
| Reinsurance | 1 | 138.98908009224343 | 0.10144338115914428 |
| Restaurant/Dining | 64 | NA | 0.18360436293768279 |
| Retail (Automotive) | 34 | 7263.202705824671 | 0.12190476293616061 |
| Retail (Building Supply) | 14 | 15 | 0.3494656524485739 |
| Retail (Distributors) | 62 | 7896.747943040039 | 0.1611399066695283 |
| Retail (General) | 23 | 78806.4371770517 | 0.13590825384807578 |
| Retail (Grocery and Food) | 15 | 1121.275770780533 | 0.06763219560214334 |
| Retail (REITs) | 26 | -339.9894526261094 | 0.051639531083079775 |
| Retail (Special Lines) | 94 | 11117.832272260513 | 0.21539093465658196 |
| Rubber& Tires | 3 | -2039.6310371810628 | 0.03168147259457092 |
| Semiconductor | 66 | 101837.77717764139 | 0.27226966835133587 |
| Semiconductor Equip | 31 | 14058.263947254238 | 0.28404463068412095 |
| Shipbuilding & Marine | 8 | 203.13865538299717 | 0.11992332943837858 |
| Shoe | 11 | 2152.2485978175696 | 0.20929696659653424 |
| Software (Entertainment) | 77 | 141504.41046465852 | 0.2701916640773067 |
| Software (Internet) | 29 | -2987.378958085182 | 0.034347801967415575 |
| Software (System & Application) | 309 | 109368.66663367552 | 0.2931842949283384 |
| Steel | 19 | -2838.429618509076 | 0.06720259161412713 |
| Telecom (Wireless) | 12 | 7089.410114704903 | 0.10372019614469251 |
| Telecom. Equipment | 57 | 11970.381255100778 | 0.2547374909112715 |
| Telecom. Services | 39 | 27064.14763503447 | 0.12036566743047672 |
| Tobacco | 10 | 15 | 0.6307780350577148 |
| Transportation | 19 | 19683.634718027966 | 0.1300079849084052 |
| Transportation (Railroads) | 4 | 9069.694785039555 | 0.14236959522310544 |
| Trucking | 26 | -360.4085595157525 | 0.0929945748076969 |
| Utility (General) | 14 | 8882.207501557179 | 0.05994651585116697 |
| Utility (Water) | 14 | 2454.1558546803185 | 0.08955910414193033 |
| Total Market | 5994 | 1181273.8063180286 | 0.08955910414193033 |
| Total Market (without financials) | 4822 | 904382.8066935824 | 0.150709519195417 |
