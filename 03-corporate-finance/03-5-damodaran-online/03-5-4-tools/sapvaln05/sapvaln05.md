---
title: "Sapvaln05"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/eqegs/SAPvaln05.xls
---

# Sapvaln05

Source: https://www.stern.nyu.edu/~adamodar/pc/eqegs/SAPvaln05.xls

Sheets: Read me first, Master Inputs Start here, Earnings Normalizer, R&D converter, Operating lease converter, What-if, Terminal Value, Valuation Model, Option Value, Bottom-up Beta, Ratings estimator, Industry averages

## Read me first

| FCFF VALUATION MODEL |
|---|
| Before you start |
|  |
| What the model does |
|  |
| Inputs |
|  |
|  |
|  |
|  |
|  |
| Options |
|  |
|  |
|  |
|  |
| Other worksheets |
|  |
|  |
|  |
|  |
| Output |

## Master Inputs Start here

| An apology: I apologize for the number of inputs that are required on this sheet. Many of the inputs are required only if you choose the appropriate option, though. |
|---|
| If you have negative operating income, you will either have to normalize it to make it positive, or use the highgrowth.xls spreadsheet. |
| Master Input Sheet |
| Do you want to capitalize R&D expenses? |
| Do you want to convert operating leases to debt? |
| Do you want to normalize operating income? |
|  |
| Inputs |
| From Current Financials |
| Current EBIT = |
| Current Interest Expense = |
| Current Capital Spending |
| Current Depreciation & Amort'n = |
| Tax Rate on Income = |
| Current Revenues = |
| Current Non-cash Working Capital = |
| Chg. Working Capital = |
| Book Value of Debt = |
| Book Value of Equity = |
| Minority Interests if any = |
| Price to Book Ratio of minority interest company = |
|  |
| Cash & Marketable Securities = |
| Value of Non-operating Assets = |
| Value of Non-operating liabilities (pension fund etc.) = |
|  |
| Market Data for your firm |
| Is your stock currently traded? |
| If yes, enter the following: |
| Current Stock Price = |
| Number of shares outstanding = |
| Market Value of Debt = |
| If no, enter the following |
| Would you like to use the book value debt ratio? |
| If no, enter the debt ratio to use in valuation |
|  |
| General Market Data |
| Long Term Treasury bond rate= |
| Risk premium for equity = |
|  |
| Ratings |
| Do you want to estimate the firm's synthetic rating = |
| If yes, choose the type of firm |
| If not, what is the current rating of the firm? |
| Enter the cost of debt associated with the rating = |
| If your country has a default spread enter it here |
| Options |
| Do you have equity options (management options, warrants) outstanding? |
| If yes, enter the number of options |
| Average strike price  |
| Average maturity |
| Standard Deviation in stock price |
| Do you want to use the stock price to value the option or your estimated value? |
|  |
| Valuation Inputs |
| High Growth Period |
| Length of high growth period = |
| Beta to use for high growth period for your firm= |
| Do you want to keep the debt ratio computed from your inputs? |
| If yes, the debt ratio that will be used to compute the cost of capital is |
| If no, enter the debt ratio that you would like to use in the high growth period |
| Do you want to keep the existing ratio of working capital to revenue? |
| If yes, the working capital as a percent of revenues will be |
| If no, enter the ratio of working capital to revenues to use in analysis |
| Do you want to compute your growth rate from fundamentals? |
| If no, enter the expected growth rate in operating income for high growth period |
| If yes, the inputs to the fundamental growth calculation (based upon your inputs) are |
| Return on Capital = |
| Reinvestment Rate = |
| Do you want to change these inputs? |
| Return on Capital = |
| Reinvestment Rate = |
|  |
| Do you want me to gradually adjust your high growth inputs in the second half? |
|  |
| Stable Growth Period |
| Growth rate during stable growth period = |
| Beta to use in stable growth period = |
| Risk premium for equity in stable growth period = |
| Debt Ratio to use in stable growth period = |
| Pre-tax cost of debt in stable growth period = |
| Tax Rate to use in stable growth period = |
| To compute the reinvestment rate in stable growth, you have two options |
| Do you want to compute reinvestment needs in stable growth based on fundamentals? |
| If yes, enter the return on capital that the firm will have in stable growth |
| If no,  enter capital expenditure as % of depreciation in stable growth |

## Earnings Normalizer

| Normalizing Earnings |
|---|
| Approach used to normalize earnings = |
|  |
| If historical average, |
| Average Earnings before interest and taxes = |
|  |
| If historical average ROC, |
| Historical average pre-tax return on capital = |
|  |
| If sector margin |
| Pre-tax Operating Margin for Sector = |
|  |
|  |
| Normalized Earnings before interest and taxes = |
|  |
|  |
| Worksheet for normalization (Last 5 years of data) |
|  |
| Revenues |
| EBIT |
| Operating Margin |
|  |
|  |
| Cp Ex |
| Depreciation |
| EBIT |
| EBIT(1-t) |
| Net Cap Ex as % of EBIT(1-t) |
| Revenues |
| Non-cashh Current assets |
| Non-debt current liabilities |
| Non-cash WC |
| as % of revenues |
|  |
| Equity |
| ST Debt |
| LT Debt |
| Total Capital |
| Change in capital |

## R&D converter

| R & D Converter |
|---|
| This spreadsheet converts R&D expenses from operating to capital expenses. It makes the appropriate adjustments to operating income, net |
| income, the book value of assets and the book value of equity. |
|  |
| Inputs |
| Over how many years do you want to amortize R&D expenses |
| Enter the current year's R&D expense = |
| Enter R& D expenses for past years: the number of years that you will need to enter will be determined by the amortization period |
| Do not input numbers in the first column (Year). It will get automatically updated  based on the input above. |
| Year |
| -1 |
| -2 |
| -3 |
| -4 |
| -5 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
|  |
| Output |
| Year |
| Current |
| -1 |
| -2 |
| -3 |
| -4 |
| -5 |
| 0 |
| 0 |
| 0 |
| 0 |
| 0 |
| Value of Research Asset = |
|  |
| Amortization of asset for current year = |
|  |
| Adjustment to Operating Income = |
| Tax Effect of R&D Expensing |
|  |
|  |
| Look Up Table for Amortization Periods |
| Industry Name |
| Advertising |
| Aerospace/Defense |
| Air Transport |
| Aluminum |
| Apparel |
| Auto & Truck |
| Auto Parts (OEM) |
| Auto Parts (Replacement) |
| Bank |
| Bank (Canadian) |
| Bank (Foreign) |
| Bank (Midwest) |
| Beverage (Alcoholic) |
| Beverage (Soft Drink) |
| Building Materials |
| Cable TV |
| Canadian Energy |
| Cement & Aggregates |
| Chemical (Basic) |
| Chemical (Diversified) |
| Chemical (Specialty) |
| Coal/Alternate Energy |
| Computer & Peripherals |
| Computer Software & Svcs |
| Copper |
| Diversified Co. |
| Drug |
| Drugstore |
| Educational Services |
| Electric Util. (Central) |
| Electric Utility (East) |
| Electric Utility (West) |
| Electrical Equipment |
| Electronics |
| Entertainment |
| Environmental |
| Financial Services |
| Food Processing |
| Food Wholesalers |
| Foreign Electron/Entertn |
| Foreign Telecom. |
| Furn./Home Furnishings |
| Gold/Silver Mining |
| Grocery |
| Healthcare Info Systems |
| Home Appliance |
| Homebuilding |
| Hotel/Gaming |
| Household Products |
| Industrial Services |
| Insurance (Diversified) |
| Insurance (Life) |
| Insurance (Prop/Casualty) |
| Internet |
| Investment Co. (Domestic) |
| Investment Co. (Foreign) |
| Investment Co. (Income) |
| Machinery |
| Manuf. Housing/Rec Veh |
| Maritime |
| Medical Services |
| Medical Supplies |
| Metal Fabricating |
| Metals & Mining (Div.) |
| Natural Gas (Distrib.) |
| Natural Gas (Diversified) |
| Newspaper |
| Office Equip & Supplies |
| Oilfield Services/Equip. |
| Packaging & Container |
| Paper & Forest Products |
| Petroleum (Integrated) |
| Petroleum (Producing) |
| Precision Instrument |
| Publishing |
| R.E.I.T. |
| Railroad |
| Recreation |
| Restaurant |
| Retail (Special Lines) |
| Retail Building Supply |
| Retail Store |
| Securities Brokerage |
| Semiconductor |
| Semiconductor Cap Equip |
| Shoe |
| Steel (General) |
| Steel (Integrated) |
| Telecom. Equipment |
| Telecom. Services |
| Textile |
| Thrift |
| Tire & Rubber |
| Tobacco |
| Toiletries/Cosmetics |
| Trucking/Transp. Leasing |
| Utility (Foreign) |
| Water Utility |

## Operating lease converter

| Operating Lease Converter |
|---|
| Inputs |
| Operating lease expense in current year = |
| Operating Lease Commitments (From footnote to financials) |
| Year |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 and beyond |
|  |
| Output |
| Pre-tax Cost of Debt = |
|  |
| From the current financial statements, enter the following |
| Reported Operating Income (EBIT) = |
| Reported Debt = |
|  |
| Number of years embedded in yr 6 estimate = |
|  |
| Converting Operating Leases into debt |
| Year |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
| 6 and beyond |
| Debt Value of leases = |
|  |
| Restated Financials |
| Depreciation on Operating Lease Asset = |
| Adjustment to Operating Earnings = |
| Adjustment to Total Debt outstanding = |

## What-if

| Reinvestment rate | Value/share |
|---|---|
| 0 | 14610 |
| 0.1 | 15789 |
| 0.2 | 17022 |
| 0.3 | 18310 |
| 0.4 | 19654 |
| 0.5 | 21057 |
| 0.6 | 22520 |
| 0.7 | 24045 |
| 0.8 | 25632 |
| 0.9 | 27284 |
| 1 | 29002 |

## Terminal Value

|  |
||
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Valuation Model

| Input Summary |
|---|
| Normalized EBIT (before adjustments) |
| Adjusted EBIT = |
| Adjusted Interest Expense = |
| Adjusted Capital Spending |
| Adjusted Depreciation & Amort'n = |
| Tax Rate on Income = |
| Current Revenues = |
| Current Non-cash Working Capital = |
| Chg. Working Capital = |
| Adjusted Book Value of Debt = |
| Adjusted Book Value of Equity = |
|  |
| Length of High Growth Period = |
| Growth Rate = |
| Debt Ratio used in Cost of Capital Calculation= |
| Beta used for stock = |
| Riskfree rate = |
| Risk Premium = |
| Cost of Debt = |
| Tax Rate = |
| Return on Capital = |
| Reinvestment Rate = |
|  |
| Output from the program |
| Cost of Equity = |
| Equity/(Debt+Equity ) = |
| After-tax Cost of debt = |
| Debt/(Debt +Equity) = |
| Cost of Capital = |
|  |
| Intermediate Output |
| Expected Growth Rate |
| Working Capital as percent of revenues = |
| The FCFF for the high growth phase are shown below (upto 10 years) |
|  |
| Expected Growth Rate |
| Cumulated Growth |
| Reinvestment Rate |
| EBIT * (1 - tax rate) |
|  - (CapEx-Depreciation) |
|  -Chg. Working Capital |
| Free Cashflow to Firm |
| Cost of Capital |
| Cumulated Cost of Capital |
| Present Value |
|  |
| Growth Rate in Stable Phase = |
| Reinvestment Rate in Stable Phase = |
| FCFF in Stable Phase = |
| Cost of Equity in Stable Phase = |
| Equity/ (Equity + Debt) = |
| AT Cost of Debt in Stable Phase = |
| Debt/ (Equity + Debt)  = |
| Cost of Capital in Stable Phase = |
| Value at the end of growth phase = |
| Valuation |
| Present Value of FCFF in high growth phase = |
| Present Value of Terminal Value of Firm = |
| Value of operating assets of the firm = |
| Value of Cash, Marketable Securities & Non-operating assets = |
| Value of Firm = |
| Market Value of outstanding debt = |
| Other non-debt liabiities = |
| Value of Minority Interests in Consolidated Company = |
| Market Value of Equity = |
| Value of Equity in Options = |
| Value of Equity in Common Stock = |
| Market Value of Equity/share = |
|  |
|  |
|  |
| Year |
| EBIT |
| EBIT(1-t) |
|  - Reinvestment |
|  = FCFF |

## Option Value

| Valuing Options or Warrants |
|---|
| Enter the current stock price = |
| Enter the strike price on the option = |
| Enter the expiration of the option = |
| Enter the standard deviation in stock prices = |
| Enter the annualized dividend yield on stock = |
| Enter the treasury bond rate = |
| Enter the number of warrants (options) outstanding = |
| Enter the number of shares outstanding = |
|  |
| Do not input any numbers below this line |
| VALUING WARRANTS WHEN THERE IS DILUTION |
| Stock Price= |
| Strike Price= |
| Adjusted S = |
| Adjusted K = |
| Expiration (in years) = |
|  |
|  |
| d1 =  |
| N (d1) = |
|  |
| d2 =  |
| N (d2) = |
|  |
| Value per option =  |
| Value of all options outstanding = |

## Bottom-up Beta

| Bottom-up Beta Calculator |
|---|
| Unlevered beta for sector = |
|  |
| Output |
| Firm's Current market value D/E ratio = |
| Firm's Current tax rate = |
|  |
| Bottom-up beta for firm = |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Ratings estimator

| Inputs for synthetic rating estimation |
|---|
| Enter the type of firm = |
| Enter current Earnings before interest and taxes (EBIT) = |
| Enter current interest expenses = |
| Enter current long term government bond rate = |
| Output |
| Interest  coverage ratio = |
| Estimated Bond Rating = |
| Estimated Default Spread = |
| Estimated Cost of Debt = |
|  |
| For large manufacturing firms |
| If interest coverage ratio is |
| > |
| -100000 |
| 0.2 |
| 0.65 |
| 0.8 |
| 1.25 |
| 1.5 |
| 1.75 |
| 2 |
| 2.25 |
| 2.5 |
| 3 |
| 4.25 |
| 5.5 |
| 6.5 |
| 8.5 |
|  |
| For smaller and riskier firms |
| If interest coverage ratio is |
| greater than |
| -100000 |
| 0.5 |
| 0.8 |
| 1.25 |
| 1.5 |
| 2 |
| 2.5 |
| 3 |
| 3.5 |
| 4 |
| 4.5 |
| 6 |
| 7.5 |
| 9.5 |
| 12.5 |

## Industry averages

| Inudstry | Number of firms | Cap Ex/Depreciation | ROC | Reinvestment Rate | Unlevered Beta | MV Debt to Capital Ratio | Non-Cash Working Capital/Sales | Pre-tax Operating Margin | Std Deviation in Equity |
|---|---|---|---|---|---|---|---|---|---|
| Advertising | 31 | 0.8611390437882804 | 0.12310991129669245 | -0.12480558246084927 | 1.0567579935250728 | 0.08464594882072249 | -0.1749454416556696 | 0.158375079542009 | 0.4817181818181818 |
| Aerospace/Defense | 41 | 0.8342268386664433 | 0.11930387332491356 | 0.04335941205899112 | 0.6723504278292167 | 0.3075792258469412 | 0.10383874547802244 | 0.104470355035269 | 0.44926296296296286 |
| Air Transport | 38 | 2.63097062194607 | 0.12600790567409834 | 0.29233208470866945 | 0.8410927564733536 | 0.4448111529355957 | -0.11963555813051127 | 0.123049958275087 | 0.5014962962962963 |
| Apparel | 46 | 1.2617854849068721 | 0.1510365290094748 | 0.20250802426601125 | 0.6481485340995699 | 0.32199990987337207 | 0.2240370932710573 | 0.132393292163978 | 0.5449878787878788 |
| Auto & Truck | 20 | 0.8919124964078498 | 0.08959439951228979 | 0.08567700156913792 | 0.5950700791600342 | 0.5436812844384904 | 0.28338877911565735 | 0.150476763096417 | 0.3978866666666667 |
| Auto Parts (OEM) | 31 | 1.4825878637008485 | 0.16281187661641838 | 0.1683966859070361 | 0.5913646455757413 | 0.3905821385732376 | 0.06651316810679361 | 0.113196564391784 | 0.4630428571428572 |
| Auto Parts (Replacement) | 28 | 1.1664493698392002 | 0.12468196319697039 | 0.23898773591675726 | 0.3878887788498909 | 0.5459651738778811 | 0.17118598145897104 | 0.117876861791714 | 0.49629047619047617 |
| Bank | 178 | NA | 0.21740283977553557 | 0 | 0.7005790706041992 | 0.33130091987789717 | NA | NA | 0.288076595744681 |
| Bank (Canadian) | 7 | NA | 0.3407186352769653 | 0 | 0.9853214283839364 | 0.23393994766399692 | NA | NA | 0.27027142857142855 |
| Bank (Foreign) | 2 | NA | 0.41805469726093225 | 0 | 1.3284649022554098 | 0.16639681954441257 | NA | NA | 0.33244999999999997 |
| Bank (Midwest) | 34 | NA | 0.20262902555759607 | 0 | 0.7078014585512347 | 0.34319489812963344 | NA | NA | 0.271625 |
| Beverage (Alcoholic) | 22 | 0.9800364868386761 | 0.08516411083615924 | 0.010126677837063513 | 0.5322283423570392 | 0.20901453238313117 | 0.048369811505627906 | 0.164396732274303 | 0.3706230769230769 |
| Beverage (Soft Drink) | 15 | 1.1082670124295806 | 0.17540857229426515 | 0.021985541811991617 | 0.6974484608737607 | 0.11691169702362401 | 0.0033791986778331762 | 0.199991146204338 | 0.38111666666666666 |
| Building Materials | 42 | 1.723984384530926 | 0.17958614729308964 | 0.1860077678404426 | 0.6613706453554379 | 0.3260866781896165 | 0.0804633758706929 | 0.120194182497578 | 0.40087878787878783 |
| Cable TV | 21 | 1.0363942454851547 | 0.04735432512643961 | -0.28250420199450405 | 1.0053965338659585 | 0.31644983749357314 | -0.3062621309633262 | 0.245647876067375 | 0.71943 |
| Canadian Energy | 16 | 2.1202542262315247 | 0.09201286911945321 | 0.2680290091981773 | 0.5776124591295076 | 0.34098401995449934 | 0.025880058327767873 | 0.254848900114853 | 0.33102000000000004 |
| Cement & Aggregates | 13 | 2.0122129297756537 | 0.17975631349533222 | 0.249430747051146 | 0.6765805342776254 | 0.20102449862800717 | 0.1274717887154862 | 0.241392557022809 | 0.36504166666666654 |
| Chemical (Basic) | 14 | 1.1946723312823517 | 0.13656054590728725 | 0.07065265879310491 | 0.7438113347943459 | 0.2566032417668149 | 0.16069631907663692 | 0.191660180597478 | 0.42823000000000006 |
| Chemical (Diversified) | 34 | 1.129350405378683 | 0.15325592609080393 | 0.03391838191064993 | 0.675662601207764 | 0.21457200226402987 | 0.15420620000799953 | 0.183659088916935 | 0.3493 |
| Chemical (Specialty) | 83 | 1.1251141031492469 | 0.13198065290437402 | 0.07379351618932951 | 0.6169598357154019 | 0.2947435812526216 | 0.15418997163586765 | 0.161991193943194 | 0.45275373134328345 |
| Computer & Peripherals | 155 | 0.9470243141510394 | 0.1348587647877478 | 0.002355995351834393 | 1.118488954569798 | 0.029097574301278174 | 0.06589827641514306 | 0.122425977735458 | 0.7796376344086022 |
| Computer Software & Svcs | 418 | 0.9033080226825763 | 0.1870810192713732 | -0.027380805972245466 | 1.081244404419465 | 0.020739298100366097 | -0.02771338807019647 | 0.247777604720256 | 0.7816105263157893 |
| Copper | 2 | 3.025358324145534 | 0.07407637540453074 | 0.7501875675026796 | 0.4993837111791962 | 0.5299331963001028 | 0.2498577582703405 | 0.151670324311144 | 0.3564 |
| Diversified Co. | 93 | 1.2380137614118278 | 0.1260746405177474 | 0.061145942168008775 | 0.7233652677346728 | 0.2297792406085289 | 0.08398312282933948 | 0.140894466354978 | 0.4251277108433736 |
| Drug | 272 | 1.4586804697850932 | 0.2380714632866114 | 0.10702370364962999 | 0.875124133321295 | 0.031577106168813394 | 0.08024226026972879 | 0.28694084737167 | 0.8088784615384612 |
| Drugstore | 10 | 2.4896901765887702 | 0.14221974791068775 | 0.38472668675137645 | 0.8307109470702188 | 0.1302721908651781 | 0.094130364876607 | 0.0708338179653665 | 0.4061571428571428 |
| Educational Services | 29 | 1.2154308617234468 | 0.1186420559083625 | 0.05950034892446226 | 0.8585358529151325 | 0.04884218719595252 | 0.03618536484673347 | 0.165053153060171 | 0.5615416666666667 |
| Electric Util. (Central) | 34 | 1.4780383519046385 | 0.10748344655442985 | 0.13279724799805578 | 0.31440350441791587 | 0.5343705484657847 | 0.05786760783152782 | 0.23324282485144 | 0.23545294117647056 |
| Electric Utility (East) | 36 | 1.1538019307084855 | 0.11345489933148138 | 0.043699880190721394 | 0.34936170104292325 | 0.46632961658376837 | 0.0328510039088106 | 0.286076379615917 | 0.228258064516129 |
| Electric Utility (West) | 17 | 1.1484510493404827 | 0.11897552657964988 | 0.03757105928928484 | 0.3283563692500715 | 0.5066454645427987 | -0.025768155973901096 | 0.223155683482952 | 0.2554083333333333 |
| Electrical Equipment | 87 | 1.0395605205913798 | 0.16667140641744796 | 0.024552157933948254 | 0.8474366684826267 | 0.031112479974419658 | 0.03943799012835994 | 0.170732872529403 | 0.6461303571428573 |
| Electronics | 142 | 1.1528325218332174 | 0.07940891691060573 | 0.10268184964900517 | 0.9576815969317373 | 0.05823956931788472 | 0.17993993645297837 | 0.0930655104345899 | 0.6491715596330274 |
| Entertainment | 91 | 0.8649084159425611 | 0.06627489535970854 | -0.002402619672929756 | 0.7927663587305928 | 0.17933288993023266 | 0.07079690012062591 | 0.221683397335725 | 0.48221904761904755 |
| Environmental | 55 | 0.9850786866135612 | 0.11361938365401308 | 0.04635482171585454 | 0.3960573085347495 | 0.5593557118543276 | 0.13142156625293902 | 0.255987003163508 | 0.6487538461538462 |
| Financial Svcs. (Div.) | 185 | 1.5084617327607983 | 0.1308357478614184 | 0.2389154277186106 | 0.8146601126833273 | 0.3138468074206552 | 1.3205920668232711 | 0.943351805921563 | 0.4160294642857142 |
| Food Processing | 94 | 1.1419797438951171 | 0.14317991821982462 | 0.02786420640990128 | 0.6707538651514644 | 0.2375268507786956 | 0.016301163645403505 | 0.127582984352246 | 0.3771867647058823 |
| Food Wholesalers | 23 | 2.0641722555594777 | 0.10795551008738266 | 0.23041961425286095 | 0.5822927467362484 | 0.26512603253001793 | 0.015603955602264852 | 0.0440029050275036 | 0.36520769230769234 |
| Foreign Electron/Entertn | 13 | 1.066784629114714 | 0.08712844430967186 | 0.0681762561711579 | 0.900674331235116 | 0.16175183927932005 | 0.14391493220809926 | 0.0987912852274835 | 0.35475 |
| Foreign Telecom. | 16 | 0.8215213984481506 | 0.20050074733935327 | -0.03493989801850249 | 1.0589488237772169 | 0.05966584175118211 | 0.07415222344957638 | 0.328443134563783 | 0.39468666666666663 |
| Furn./Home Furnishings | 35 | 1.5176123991289867 | 0.18140079500580647 | 0.2382562411265776 | 0.7305803985389661 | 0.20901761719916392 | 0.15243219262033128 | 0.133685999383398 | 0.38556521739130434 |
| Gold/Silver Mining | 31 | 1.2240954221363363 | 0.07210311452688277 | 0.05550848304776803 | 0.627455165834156 | 0.1277052376349547 | 0.06939272615281239 | 0.333342665957387 | 0.5930931034482758 |
| Grocery | 27 | 1.7560696605723525 | 0.1425211634152418 | 0.18215531219247885 | 0.5781468301796608 | 0.28482373439981706 | 0.010415908629558287 | 0.0668555216380496 | 0.3911652173913043 |
| Healthcare Info Systems | 32 | 1.0072666294019004 | 0.10662959662246402 | 0.05643173171739688 | 0.8368267080689118 | 0.1336257147615611 | 0.0607935217797044 | 0.160646015834312 | 1.1107 |
| Home Appliance | 12 | 1.0526506899055919 | 0.2395414514255607 | 0.08467530475350982 | 0.8042672872187613 | 0.26553635217482663 | 0.1011153253320864 | 0.132509828371521 | 0.40756 |
| Homebuilding | 58 | 2.5323932419848343 | 0.0942627814764289 | 0.5746612989800547 | 0.5037591220819843 | 0.5297801485323589 | 0.36038688743967784 | 0.124171070058615 | 0.4168176470588235 |
| Hotel/Gaming | 54 | 2.1576760893331253 | 0.08223259761298435 | 0.20716896350216926 | 0.5515088012389686 | 0.5011810160630477 | -0.02439934573211365 | 0.247473193190768 | 0.49952580645161304 |
| Household Products | 30 | 1.0979978925184404 | 0.22580666639779934 | 0.06654891500001511 | 0.709793523384362 | 0.13683883834407132 | 0.0667553028378177 | 0.20380770477584 | 0.40691249999999995 |
| Industrial Services | 187 | 1.0430080482897384 | 0.11803004828889786 | 0.1617094406090878 | 0.820696364024951 | 0.17336776241079724 | 0.09026079237177659 | 0.100268645319891 | 0.5001902777777777 |
| Insurance (Life) | 34 | NA | 0.2959753318208331 | 0.03931730770488996 | 0.8674971995894651 | 0.18296863887424683 | NA | NA | 0.3760896551724138 |
| Insurance (Prop/Casualty | 59 | 494.05555555555554 | 7.762688948589621e-05 | 70.00718925014343 | 0.8229123512374225 | 0.07648232772344894 | -2.0352941176470587 | 0.384313725490196 | 0.3406444444444445 |
| Internet | 304 | 1.6076332986078226 | 0.01879205653988125 | -0.9339026965206807 | 2.115054202987856 | 0.012288875204505773 | -0.21000292483182187 | 0.0836231083379372 | 1.263092857142857 |
| Investment Co. | 26 | 3.23321554770318 | 0.09702574438845625 | 0.6180218453756313 | 0.5671907315667911 | 0.027103559870550162 | 0.1822866344605475 | 0.340096618357488 | 0.17307826086956526 |
| Investment Co. (Foreign) | 20 | 0.41399416909620995 | 0.06207615624815885 | -0.18671845533467202 | 1.1514188751106416 | 0.031258431296974365 | -0.053466076696165196 | 0.550884955752212 | 0.33158 |
| Machinery | 126 | 1.1936340658869897 | 0.1148835440512341 | 0.08930456306320184 | 0.6237201993896746 | 0.3056943567157691 | 0.21318322120158256 | 0.124687921969113 | 0.4263160000000002 |
| Manuf. Housing/Rec Veh | 21 | 1.4868667917448406 | 0.12724151656537094 | 0.20680272821954 | 0.6870412858402571 | 0.3327116627544294 | 0.15216658236385094 | 0.0809890665732851 | 0.417255 |
| Maritime | 16 | 1.6748806406899739 | 0.08163075261357966 | 0.2326367405633034 | 0.4184647001765631 | 0.5765472907573461 | 0.06979723140074817 | 0.18030830143088 | 0.39708333333333334 |
| Medical Services | 163 | 1.0858086382202137 | 0.13115724206402987 | 0.0924153759096865 | 0.7927973380317153 | 0.25668880005299116 | 0.0505597877211012 | 0.116131891315814 | 0.6473931034482758 |
| Medical Supplies | 194 | 1.145778087927425 | 0.18705547226066893 | 0.17188640923233556 | 0.7996663072991363 | 0.07559362088607387 | 0.13345205074492567 | 0.141756494309848 | 0.635760606060606 |
| Metal Fabricating | 42 | 1.2529401439354044 | 0.15044155283968366 | 0.12000506928630798 | 0.736100329417208 | 0.18711651144853628 | 0.17404561492665005 | 0.142132534809445 | 0.44080833333333325 |
| Metals & Mining (Div.) | 35 | 1.3352762336517532 | 0.10892038788874454 | 0.13542380054886413 | 0.7141669997060793 | 0.2819091472762061 | 0.15957289706095268 | 0.160702186187925 | 0.486488888888889 |
| Natural Gas (Distrib.) | 43 | 1.8412515774626976 | 0.11254589766843398 | 0.2140324329589915 | 0.39601236443889243 | 0.45008787043747817 | 0.0446765920566037 | 0.220295540976932 | 0.24230625 |
| Natural Gas (Diversified | 37 | 2.261287268550853 | 0.10315747362257986 | 0.38359078436266597 | 0.5713131459176695 | 0.2839798407952917 | 0.012286986346292602 | 0.139828007268603 | 0.38803030303030295 |
| Newspaper | 20 | 0.8571124036909584 | 0.1252977584226731 | -0.027238040818467018 | 0.7517350168867305 | 0.16538152027251882 | -0.028132714953897603 | 0.238856944543038 | 0.33240000000000003 |
| Office Equip & Supplies | 31 | 0.9997625750432452 | 0.12620163797604847 | 0.04984469913439807 | 0.6861872269993202 | 0.33520584175271523 | 0.19638795775553844 | 0.124597374163497 | 0.44713461538461535 |
| Oilfield Services/Equip. | 72 | 1.6698216037495912 | 0.06674562878748537 | 0.095732811730791 | 0.9808656400945769 | 0.1457969870816969 | 0.18237931926579942 | 0.166254834194588 | 0.5566127659574469 |
| Packaging & Container | 36 | 0.923053772070626 | 0.11411880017785436 | 0.026421725040684036 | 0.47206058277180124 | 0.5239653451839449 | 0.10908312753156654 | 0.164057796508128 | 0.37829642857142853 |
| Paper & Forest Products | 55 | 0.8864662594829449 | 0.11046847670321132 | 0.02308389025930324 | 0.5796454755719703 | 0.39612510620771296 | 0.11462587803038567 | 0.156412674665262 | 0.35515625 |
| Petroleum (Integrated) | 43 | 1.331416066960976 | 0.16747040383856185 | 0.08378703426740516 | 0.7150880182554125 | 0.11050376298047612 | 0.006401872782825706 | 0.1580220956375 | 0.3329941176470588 |
| Petroleum (Producing) | 96 | 1.6099809173311523 | 0.11558896574179149 | 0.22667137472329693 | 0.5984603891561204 | 0.27909892389218144 | -0.0028247412544574 | 0.372688117557639 | 0.5829093333333336 |
| Precision Instrument | 89 | 1.0999183006535946 | 0.145467319799664 | 0.03634700424678892 | 0.8583956205668815 | 0.06791934604165023 | 0.15782149205197338 | 0.170217749750835 | 0.6217515151515152 |
| Publishing | 49 | 1.1888793103448276 | 0.19361424063066834 | 0.039667978432316016 | 0.746113617813221 | 0.19973904322340044 | -0.008877962899347284 | 0.197988234283751 | 0.5112151515151515 |
| R.E.I.T. | 155 | 3.9517157607045243 | 0.06603404293958205 | 0.35158936562252424 | 0.6550168844389088 | 0.08885452409746612 | -0.2387737478411054 | 0.590421704087507 | 0.24254077669902904 |
| Railroad | 16 | 1.953395593435488 | 0.10995178125023795 | 0.17340914407040803 | 0.5802369887323932 | 0.39873261073208016 | -0.07036535859269283 | 0.256037705557212 | 0.38137692307692306 |
| Recreation | 87 | 1.7110583153347731 | 0.1041340206161053 | 0.1794946747789988 | 0.7351941623724135 | 0.20205148654137647 | 0.054989232548735625 | 0.165111106931606 | 0.6210785714285714 |
| Restaurant | 93 | 1.846001152590126 | 0.17392868969832614 | 0.1420914997113873 | 0.6812594999717587 | 0.18361078303223485 | -0.047193477071673894 | 0.164724008791323 | 0.450355 |
| Retail (Special Lines) | 205 | 1.610292280789408 | 0.1693824018330751 | 0.17869789342043335 | 1.107539601614724 | 0.1266274712687375 | 0.08708762605709411 | 0.0931661924670669 | 0.6269887218045112 |
| Retail Building Supply | 12 | 4.637127167007645 | 0.17820190877723058 | 0.3803346894486445 | 0.8408605402833401 | 0.026324974844146528 | 0.08141412647195694 | 0.100048384661138 | 0.3997583333333333 |
| Retail Store | 31 | 1.8929570302568013 | 0.13254419770807718 | 0.2523679942383079 | 0.963286846189505 | 0.16675989077350803 | 0.11028406671881195 | 0.0791163182167686 | 0.4118928571428571 |
| Securities Brokerage | 32 | 1.2502274795268427 | 0.14880055900693132 | 0.5136542751310116 | 0.8225532497548614 | 0.5349595876599984 | 1.6488599404440094 | 0.574709365842903 | 0.5478304347826087 |
| Semiconductor | 99 | 1.091921900016105 | 0.18085845524797517 | 0.035278892470598046 | 1.3236685139331046 | 0.017665546074303016 | 0.07043377185008688 | 0.260700208492088 | 0.7616942307692308 |
| Semiconductor Cap Equip | 7 | 0.9748888888888889 | 0.16923768443900522 | 0.015708392710868845 | 1.9141448131984133 | 0.00558897234972181 | 0.15853191153594695 | 0.239883220235814 | 0.6801666666666667 |
| Shoe | 26 | 1.559416767922236 | 0.14487018470739627 | 0.2741594500852522 | 0.8919871363250397 | 0.14184752059884015 | 0.22089194046555669 | 0.103378138418657 | 0.5233476190476191 |
| Steel (General) | 30 | 1.707338725586901 | 0.103414182120838 | 0.17030376447217166 | 0.5952582224595353 | 0.3904635906856864 | 0.16996460256113272 | 0.107626908555939 | 0.4412888888888889 |
| Steel (Integrated) | 19 | 1.4832878819662962 | 0.10487183532353922 | 0.19358690497984132 | 0.6665847835702408 | 0.4776080211515013 | 0.13966408531338712 | 0.125786206133368 | 0.4075875 |
| Telecom. Equipment | 116 | 1.5732128740824391 | 0.13822640313616835 | 0.2524965941902044 | 1.0904394445994552 | 0.03637444530875293 | 0.2518488750316912 | 0.173222463764207 | 0.8614542372881355 |
| Telecom. Services | 175 | 1.7278244124319289 | 0.12132152922705437 | 0.17624426773185603 | 1.0789772291374644 | 0.17338179722793354 | -0.048571190815044143 | 0.342897744332025 | 0.6735966101694918 |
| Textile | 27 | 1.3669829655882018 | 0.09855104228621162 | 0.1684285882141393 | 0.33050207700767625 | 0.6858528251639324 | 0.22549853945764425 | 0.116400625618143 | 0.4808047619047619 |
| Thrift | 133 | NA | 0.09260332041594382 | 0 | 0.2591664330700181 | 0.7672826876094434 | NA | NA | 0.31009166666666665 |
| Tire & Rubber | 10 | 1.5235607912869529 | 0.11070821504370248 | 0.15624258690001946 | 0.63263194895296 | 0.41455250769448354 | 0.1660958904109589 | 0.101005611907003 | 0.43605555555555564 |
| Tobacco | 12 | 0.7755452515885283 | 0.2606674388263065 | -0.019243661749492314 | 0.5596636443026515 | 0.23401710644017187 | 0.015838540853583678 | 0.158227780952222 | 0.4165375 |
| Toiletries/Cosmetics | 20 | 1.6621936342464232 | 0.21664388539482876 | 0.10401365393052726 | 0.8606513962877795 | 0.1360624447168728 | 0.14952707468958348 | 0.184349850954573 | 0.48913529411764706 |
| Trucking/Transp. Leasing | 51 | 1.9004454963107336 | 0.161796426154615 | 0.3555722818260182 | 0.5077274704100041 | 0.5891845690217296 | 0.23742363520844534 | 0.193987341772152 | 0.4295162162162162 |
| Utility (Foreign) | 2 | 2.155777277116189 | 0.12527192872651047 | 0.5010953862327758 | 1.0282372381803804 | 0.3164683764026305 | -0.07909949312583701 | 0.449049822848328 | 0.3797 |
| Water Utility | 15 | 2.541040177471038 | 0.06736020340561157 | 0.20894066542619177 | 0.418849309596949 | 0.4554620487660028 | 0.017587609922562 | 0.39501246882793 | 0.28818181818181815 |
