---
title: "Evachina"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAChina.xls
---

# Evachina

Source: https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVAChina.xls

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
| Long Term Treasury bond rate = |  |  |  |
| Risk Premium to Use for Equity = |  |  |  |
| Country Default Spread to use for debt = |  |  |  |
|  |  |  |  |
| Do you want to use the marginal tax rate? |  |  |  |
| Marginal tax rate = |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| Industry Name | Number of Firms | Equity EVA | ROC |
| Advertising | 60 | -1608.331952233802 | 0.014274686594939644 |
| Aerospace/Defense | 68 | -4182.652994699745 | 0.024925156247146592 |
| Air Transport | 15 | -3336.6891908286907 | 0.019953509765045518 |
| Apparel | 128 | -1473.8159148659186 | 0.08439951728710408 |
| Auto & Truck | 34 | -8686.8858811647 | 0.057381440829003115 |
| Auto Parts | 220 | -5907.864551326212 | -0.09969159839837219 |
| Bank (Money Center) | 21 | 10857.13776805338 | NA |
| Banks (Regional) | 37 | 8069.447044155719 | NA |
| Beverage (Alcoholic) | 39 | 11707.345480108901 | 0.43908355264303983 |
| Beverage (Soft) | 3 | 2174.6581665063754 | 0.7627660043369058 |
| Broadcasting | 4 | -473.6620681171969 | -0.001126853451333612 |
| Brokerage & Investment Banking | 59 | -22067.561869286143 | NA |
| Building Materials | 62 | -2177.5372741400174 | 0.042239449759304035 |
| Business & Consumer Services | 91 | -3392.6434384891672 | 0.021904977811127647 |
| Cable TV | 11 | -2232.833626346634 | -0.01753230940148005 |
| Chemical (Basic) | 290 | -18334.161798978905 | 0.03455183347533645 |
| Chemical (Diversified) | 5 | 730.3303485179188 | 0.12335560291287105 |
| Chemical (Specialty) | 244 | -10454.053459039156 | 0.05590109002679527 |
| Coal & Related Energy | 29 | -411.0813215103374 | 0.12469912968543048 |
| Computer Services | 116 | -4605.375197605456 | 0.024771592932946552 |
| Computers/Peripherals | 55 | -556.7294476824842 | 0.11620498217867663 |
| Construction Supplies | 152 | -13688.24325937831 | 0.05820613820343622 |
| Diversified | 7 | -326.5520772425449 | 0.03390966709591376 |
| Drugs (Biotechnology) | 140 | -9029.625345438379 | -0.018531429221789828 |
| Drugs (Pharmaceutical) | 246 | -6287.528938448983 | 0.06931746928915641 |
| Education | 44 | -158.0777512161957 | 0.10706466029415601 |
| Electrical Equipment | 344 | -9240.47672443307 | 0.08546342860162202 |
| Electronics (Consumer & Office) | 24 | -1020.8438785988124 | 0.052887005109342106 |
| Electronics (General) | 404 | -16848.672459477417 | 0.0607560593603953 |
| Engineering/Construction | 135 | -19386.589968867458 | 0.0445654179253264 |
| Entertainment | 88 | -938.2520416647574 | 0.11754031070220636 |
| Environmental & Waste Services | 105 | -4085.0744701789436 | 0.029984379591229873 |
| Farming/Agriculture | 43 | -1829.3214676212008 | 0.057941265180738645 |
| Financial Svcs. (Non-bank & Insurance) | 33 | 69.2711950362757 | NA |
| Food Processing | 167 | 2437.2964797096292 | 0.1079090116638593 |
| Food Wholesalers | 1 | 15 | NA |
| Furn/Home Furnishings | 85 | 5216.435025983955 | 0.17470220869870096 |
| Green & Renewable Energy | 32 | 83.60771421520944 | 0.051893524483664064 |
| Healthcare Products | 138 | -3962.4082060124233 | 0.06280369116760638 |
| Healthcare Support Services | 57 | -2657.8513089338417 | 0.07269390765891276 |
| Heathcare Information and Technology | 54 | 774.2849675163037 | 0.07941630940445411 |
| Homebuilding | 2 | -25.58274406751947 | -0.013149871227393056 |
| Hospitals/Healthcare Facilities | 21 | -402.06066965492454 | 0.08042891391442311 |
| Hotel/Gaming | 28 | -665.8556659122168 | 0.06918847928290058 |
| Household Products | 72 | -482.60894238701377 | 0.09814133020343956 |
| Information Services | 2 | -31.973786964482265 | -0.07381337148770098 |
| Insurance (General) | 9 | 1835.862498026195 | 0.16179644693697567 |
| Insurance (Life) | 4 | 16395.566356079 | 0.12480104467780538 |
| Insurance (Prop/Cas.) | 2 | 6310.952260564593 | 0.17125269204893245 |
| Investments & Asset Management | 13 | -1599.9568632280898 | 0.002423905386217752 |
| Machinery | 422 | -14642.636803244044 | 0.05103772742636848 |
| Metals & Mining | 125 | -1361.9755199382464 | 0.10891097131819745 |
| Office Equipment & Services | 12 | -31.477769738723975 | 0.09908335108139044 |
| Oil/Gas (Integrated) | 4 | -7784.699888821026 | 0.08011783722053195 |
| Oil/Gas (Production and Exploration) | 5 | -170.0622586043124 | 0.07108893616020348 |
| Oil/Gas Distribution | 14 | 154.1455056010669 | 0.05853167012477355 |
| Oilfield Svcs/Equip. | 51 | -1347.1069379530395 | 0.0642908403314533 |
| Packaging & Container | 57 | -1641.3705461670359 | 0.03775877475114708 |
| Paper/Forest Products | 37 | -4379.310299784644 | 0.009996101792039108 |
| Power | 82 | -2290.5252030210413 | 0.05399013299253977 |
| Precious Metals | 15 | 4442.423356760478 | 0.15394952640496198 |
| Publishing & Newspapers | 39 | -1807.7904350213937 | 0.06783196401002091 |
| R.E.I.T. | 2 | 15 | NA |
| Real Estate (Development) | 126 | -106311.21799191355 | -0.017862419931999166 |
| Real Estate (General/Diversified) | 24 | -5585.432969030587 | 0.0017785521096267624 |
| Real Estate (Operations & Services) | 71 | -4657.265316909856 | 0.06341735873002519 |
| Recreation | 46 | -978.0277007450871 | 0.05829600230380428 |
| Reinsurance | 1 | -377.3632591348795 | 0.0738851717399591 |
| Restaurant/Dining | 21 | -1698.9905472086023 | 0.06782906186744997 |
| Retail (Automotive) | 23 | -2288.9268522113275 | 0.041954125357471755 |
| Retail (Building Supply) | 3 | -228.28535736241344 | 0.16179853144912093 |
| Retail (Distributors) | 72 | -6641.555135736763 | 0.052246656531408864 |
| Retail (General) | 48 | -2705.286070644213 | 0.023315079511390998 |
| Retail (Grocery and Food) | 22 | -1850.1003288032107 | -0.013800078951548196 |
| Retail (REITs) | 0 | 15 | NA |
| Retail (Special Lines) | 45 | -1540.6273032767199 | 0.09334935030880183 |
| Rubber& Tires | 16 | 11.859779221387662 | 0.08183331359309708 |
| Semiconductor | 178 | -23153.31758022237 | -0.01112044082001606 |
| Semiconductor Equip | 65 | -7617.592170844315 | 0.007838317318622065 |
| Shipbuilding & Marine | 39 | 1921.4920637013843 | 0.09274332149772528 |
| Shoe | 10 | 28.699423523546084 | 0.1739054563061701 |
| Software (Entertainment) | 27 | 14555.104528562662 | 0.16130161343180557 |
| Software (Internet) | 20 | -469.4778307850332 | 0.041380962741839555 |
| Software (System & Application) | 181 | -11899.803438903124 | -0.026236774435775476 |
| Steel | 101 | -17056.770909134826 | 0.021266627319141442 |
| Telecom (Wireless) | 6 | -6052.5594348753 | 0.09483983806899737 |
| Telecom. Equipment | 111 | -4426.288631784566 | 0.04604202778223467 |
| Telecom. Services | 9 | -5416.978157132504 | 0.07175328324737665 |
| Tobacco | 2 | -209.892131005922 | 0.023612519150340096 |
| Transportation | 79 | -1496.382852581563 | 0.06656039695099658 |
| Transportation (Railroads) | 9 | -1883.6355949515626 | 0.05305487515119621 |
| Trucking | 9 | -182.937421669726 | 0.011448305881559989 |
| Utility (General) | 3 | -43.83763029967222 | 0.025969536850406042 |
| Utility (Water) | 32 | -524.4325179519702 | 0.03405578480657066 |
| Total Market | 6307 | -511985.7950060375 | 0.03405578480657066 |
| Total Market (without financials) | 6129 | -397419.9993580102 | 0.06188271911751499 |
