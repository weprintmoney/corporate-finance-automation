---
title: "Ctryprem13"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/ctryprem13.xls
---

# Ctryprem13

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/ctryprem13.xls

Sheets: Explanation and FAQ, Country Lookup, ERPs by country, Regional Simple Averages, Regional Weighted Averages, Regional breakdown, Sovereign Ratings (Moody's), Regional lookup table, Rating  CDS, 10-year CDS Spreads, Equity vs Govt Bond volatility, Country GDP, Ratings look up

## Explanation and FAQ

| Country Risk Premiums |
|---|
| To estimate the equity risk premium for a country, I start with a mature market premium and add an additional country risk premium, based upon the risk of the country in question. |
| Use the look up table in the next worksheet, to look up the statistics for an individual country or region. |
|  |
| Step 1: Estimating mature market risk premium |
| To estimate the mature market risk premium, I compute the implied equity risk premium for the S&P 500. To see the latest estimate for this number, go to my website and you can download the excel spreadsheet containing the implied premium |
| Link to site: |
| Historical monthly ERP: |
|  |
| Step 2: Estimate the default spread for the country in question. I offer two choices, one based upon the local currency sovereign rating for the country from Moody's and the other is the CDS spread for the country (if one exists) |
| Moody's ratings: |
| Ratings to spreads: |
| CDS spreads: |
|  |
| Step 3: Convert the default spread into a country risk premium |
| With sovereign ratings default spreads, you have two choices: |
| Choice 1: Use the default spread as the measure of the additional country risk premium. To make this choice, go into the ERP worksheet and set cell E5 to 1.00. |
| Choice 2: Scale the default spread up to reflect the higher risk of equity in the market, relative to the default spread. You can see the relative ratios for individual countries in the worksheet "Equity vs Govt Bond" in this spreadsheet. Set cell E5 in the ERP worksheet to that number. |
|  |
| With CDS spreads, I compute the base number in two steps |
| Substep 1: Since the base equity premium is computed for the US, and the US has a CDS spread, I subtracted out the US CDS spread from the CDS for other markets. |
| Any country that has a CDS spread lower than the US will have a negative country risk premium and end up with a total equity risk premium lower than the US. |
| Substep 2: I apply the scaling factor that you chose for the default spreads to this number to get a country risk premium. The default scaling is set at 1.5, but you can change it to 1, if you would |
| prefer not to scale the default spread. |
| Step 4: Compute a total equity risk premium |
| Add the mature market premium from step 1 to the country risk premium from step 3 to get a total equity risk premium. |
|  |
| Step 5: Compute regional averages and regional weighted averages |
| For the regional averages, I use a simple average of the total and country risk premiums by region |
| For the weighted averages, I use the World Bank GDP estimates from the most recent year.  |
|  |
| If you are interested in a fuller explanation of these concepts, try these references: |
| My paper on equity risk premiums: |
| Campbell Harvey's country risk premium page: |
| Watch my lectures on country risk premiums: |
|  |

## Country Lookup

| To look up the equity risk premium for a country, use this worksheet |
|---|
| Country |
|  |
| Moody's sovereign rating |
| S&P sovereign rating |
| CDS spread |
| Excess CDS spread (over US CDS) |
|  |
| Country Risk Premium (Rating) |
| Equity Risk Premium (Rating) |
|  |
| Country Risk Premium (CDS) |
| Equity Risk Premium (CDS) |
|  |
| To look up the equity risk premium for a region, use this worksheet |
| Region |
|  |
| Country Risk Premium (simple average)) |
| Total Equity Risk Premium (simple average) |
|  |
| Country Risk Premium (GDP weighted) |
| Total Equity Risk Premium (GDP weighted) |

## ERPs by country

| Estimating Country Risk Premiums |
|---|
|  |
| Enter the current risk premium for a mature equity market |
| Do you want to adjust the country default spread for the additional volatility of the equity market to get to a country premium? |
| If yes, enter the multiplier to use on the default spread (See worksheet for volatility numbers for selected emerging markets) |
|  |
| Country |
| Abu Dhabi |
| Albania |
| Andorra |
| Angola |
| Argentina |
| Armenia |
| Aruba |
| Australia |
| Austria |
| Azerbaijan |
| Bahamas |
| Bahrain |
| Bangladesh |
| Barbados |
| Belarus |
| Belgium |
| Belize |
| Benin |
| Bermuda |
| Bolivia |
| Bosnia and Herzegovina |
| Botswana |
| Brazil |
| Bulgaria |
| Burkina Faso |
| Cambodia |
| Cameroon |
| Canada |
| Cape Verde |
| Cayman Islands |
| Chile |
| China |
| Colombia |
| Cook Islands |
| Costa Rica |
| Croatia |
| Cuba |
| Curacao |
| Cyprus |
| Czech Republic |
| Democratic Republic of Congo |
| Denmark |
| Dominican Republic |
| Ecuador |
| Egypt |
| El Salvador |
| Estonia |
| Fiji |
| Finland |
| France |
| Gabon |
| Georgia |
| Germany |
| Ghana |
| Greece |
| Guatemala |
| Honduras |
| Hong Kong |
| Hungary |
| Iceland |
| India |
| Indonesia |
| Ireland |
| Isle of Man |
| Israel |
| Italy |
| Jamaica |
| Japan |
| Jordan |
| Kazakhstan |
| Kenya |
| Korea |
| Kuwait |
| Latvia |
| Lebanon |
| Liechtenstein |
| Lithuania |
| Luxembourg |
| Macao |
| Macedonia |
| Malaysia |
| Malta |
| Mauritius |
| Mexico |
| Moldova |
| Mongolia |
| Montenegro |
| Montserrat |
| Morocco |
| Mozambique |
| Namibia |
| Netherlands |
| New Zealand |
| Nicaragua |
| Nigeria |
| Norway |
| Oman |
| Pakistan |
| Panama |
| Papua New Guinea |
| Paraguay |
| Peru |
| Philippines |
| Poland |
| Portugal |
| Qatar |
| Ras Al Kaminah |
| Republic of the Congo |
| Romania |
| Russia |
| Rwanda |
| Saudi Arabia |
| Senegal |
| Serbia |
| Singapore |
| Slovakia |
| Slovenia |
| South Africa |
| Spain |
| Sri Lanka |
| St. Maarten |
| St. Vincent & the Grenadines |
| Suriname |
| Sweden |
| Switzerland |
| Taiwan |
| Thailand |
| Trinidad and Tobago |
| Tunisia |
| Turkey |
| Uganda |
| Ukraine |
| United Arab Emirates |
| United Kingdom |
| United States of America |
| Uruguay |
| Venezuela |
| Vietnam |
| Zambia |
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
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

## Regional Simple Averages

|  |
||
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
|  |
|  |
|  |

## Regional Weighted Averages

| Country | GDP | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region | Weight | Weight * TRP | Weight * CRP |
|---|---|---|---|---|---|---|---|---|---|
| Angola | 114.197 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa | 0.08931800548123489 | 0.009289072570048428 | 0.004823172295986684 |
| Benin | 7.557 | B2 | 0.055 | 0.1325 | 0.0825 | Africa | 0.005910629591159944 | 0.0007831584208286926 | 0.00048762694127069535 |
| Botswana | 14.411 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Africa | 0.011271414984544917 | 0.0007072812902801935 | 0.0001437105410529477 |
| Burkina Faso | 10.441 | B2 | 0.055 | 0.1325 | 0.0825 | Africa | 0.008166320439499929 | 0.0010820374582337406 | 0.0006737214362587441 |
| Cameroon | 24.984 | B2 | 0.055 | 0.1325 | 0.0825 | Africa | 0.019540977862318384 | 0.002589179566757186 | 0.0016121306736412667 |
| Cape Verde | 1.897 | B2 | 0.055 | 0.1325 | 0.0825 | Africa | 0.0014837189803401365 | 0.0001965927648950681 | 0.00012240681587806127 |
| Democratic Republic of Congo | 17.9 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Africa | 0.01400030034163861 | 0.0020650443003916953 | 0.0013650292833097646 |
| Egypt | 84.532 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Africa | 0.06611583175862541 | 0.010743822660776628 | 0.0074380310728453585 |
| Gabon | 18.661 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa | 0.014595508641079225 | 0.0015179328986722393 | 0.000788157466618278 |
| Ghana | 40.71 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.03184090653117921 | 0.003741306517413557 | 0.0021492611908545964 |
| Kenya | 37.229 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.029118278291556637 | 0.003421397699257905 | 0.001965483784680073 |
| Morocco | 96.729 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Africa | 0.07565558948303694 | 0.006619864079765733 | 0.0028370846056138856 |
| Mozambique | 14.588 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.011409853708593522 | 0.001340657810759739 | 0.0007701651253300628 |
| Namibia | 12.807 | Baa3 | 0.022 | 0.083 | 0.033 | Africa | 0.010016862931584675 | 0.0008313996233215281 | 0.0003305564767422943 |
| Nigeria | 262.606 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa | 0.205394573827729 | 0.021361035678083815 | 0.011091306986697365 |
| Republic of the Congo | 13.7 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa | 0.010715313669298824 | 0.0011143926216070775 | 0.0005786269381421364 |
| Rwanda | 7.103 | B2 | 0.055 | 0.1325 | 0.0825 | Africa | 0.00555553817467369 | 0.0007361088081442639 | 0.00045833189941057946 |
| Senegal | 14.16 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.01107509792388842 | 0.0013013240060568893 | 0.0007475691098624684 |
| South Africa | 384.313 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Africa | 0.30058644833498094 | 0.022243397176788592 | 0.007214074760039543 |
| Tunisia | 45.662 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa | 0.03571406224580459 | 0.0037142624735636773 | 0.0019285593612734476 |
| Uganda | 33.679 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.02634168241374563 | 0.0030951476836151115 | 0.00177806356292783 |
| Zambia | 20.678 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa | 0.016173084383486212 | 0.00190033741505963 | 0.0010916831958853194 |
| Africa | 1278.5440000000003 |  | 0.03359650234954759 | 0.10039475352432138 | 0.05039475352432139 |  | 0.9999999999999998 |  |  |
| Bangladesh | 115.61 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Asia | 0.005727991785700078 | 0.0005957111457128081 | 0.00030931155642780416 |
| Cambodia | 14.062 | B2 | 0.055 | 0.1325 | 0.0825 | Asia | 0.0006967132643414453 | 9.23145075252415e-05 | 5.747884430816924e-05 |
| China | 8227.103 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia | 0.40761853130445863 | 0.02404949334696306 | 0.003668566781740128 |
| Fiji | 3.882 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia | 0.00019233685764283109 | 2.2599580773032654e-05 | 1.2982737890891098e-05 |
| Hong Kong | 263.259 | Aa1 | 0.004 | 0.056 | 0.006 | Asia | 0.01304338196965329 | 0.0007304293903005843 | 7.826029181791974e-05 |
| India | 1841.717 | Baa3 | 0.022 | 0.083 | 0.033 | Asia | 0.09124937157325656 | 0.007573697840580295 | 0.0030112292619174667 |
| Indonesia | 878.043 | Baa3 | 0.022 | 0.083 | 0.033 | Asia | 0.043503356902443155 | 0.003610778622902782 | 0.0014356107777806241 |
| Japan | 5959.718 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia | 0.2952790913336986 | 0.01742146638868822 | 0.002657511822003288 |
| Korea | 1129.598 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia | 0.055966854641840987 | 0.0033020444238686182 | 0.0005037016917765689 |
| Macao | 43.582 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia | 0.0021593057521354622 | 0.00012739903937599229 | 1.9433751769219164e-05 |
| Malaysia | 303.526 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Asia | 0.015038443341807818 | 0.0010226141472429316 | 0.00027069198015254077 |
| Mauritius | 10.492 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Asia | 0.0005198347012850551 | 3.8467767895094086e-05 | 1.2476032830841324e-05 |
| Mongolia | 10.271 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia | 0.0005088850759529929 | 5.979399642447666e-05 | 3.434974262682702e-05 |
| Pakistan | 231.182 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Asia | 0.011454100830392833 | 0.001861291384938835 | 0.0012885863434191935 |
| Papua New Guinea | 15.654 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia | 0.0007755902033850793 | 9.113184889774682e-05 | 5.2352338728492856e-05 |
| Philippines | 250.265 | Baa3 | 0.022 | 0.083 | 0.033 | Asia | 0.012399583636780814 | 0.0010291654418528077 | 0.0004091862600137669 |
| Singapore | 274.701 | Aaa | 0 | 0.05 | 0 | Asia | 0.01361028519612142 | 0.000680514259806071 | 0 |
| Sri Lanka | 59.421 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia | 0.002944061931477245 | 0.0003459272769485763 | 0.00019872418037471406 |
| Taiwan | 44.02 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia | 0.002181006819535658 | 0.00012867940235260385 | 1.9629061375820927e-05 |
| Thailand | 365.564 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Asia | 0.018112166673710434 | 0.0013403003338545722 | 0.0004346920001690504 |
| Vietnam | 141.669 | B2 | 0.055 | 0.1325 | 0.0825 | Asia | 0.007019106204379763 | 0.0009300315720803187 | 0.0005790762618613305 |
| Asia | 20183.338999999996 |  | 0.010035901145989772 | 0.06505385171898466 | 0.015053851718984658 |  |  |  |  |
| Australia | 1520.608 | Aaa | 0 | 0.05 | 0 | Australia & New Zealand | 0.9151600649022373 | 0.04575800324511187 | 0 |
| Cook Islands | 1.2 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Australia & New Zealand | 0.0007222059057184263 | 8.48591939219151e-05 | 4.874889863599378e-05 |
| New Zealand | 139.768 | Aaa | 0 | 0.05 | 0 | Australia & New Zealand | 0.08411772919204417 | 0.0042058864596022085 | 0 |
| Australia & New Zealand | 1661.576 |  | 3.249926575732918e-05 | 0.05004874889863599 | 4.874889863599378e-05 |  |  |  |  |
| Aruba | 2.584 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean | 0.013740880182077298 | 0.0010168251334737202 | 0.00032978112436985515 |
| Bahamas | 8.149 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean | 0.043333758747580456 | 0.003206698147320954 | 0.0010400102099419309 |
| Barbados | 3.685 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Caribbean | 0.01959564375810946 | 0.001714618828834578 | 0.0007348366409291048 |
| Bermuda | 5.557 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Caribbean | 0.029550337140790847 | 0.00174346989130666 | 0.00026595303426711766 |
| Cayman Islands | 4 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Caribbean | 0.02127071235615681 | 0.001254972029013252 | 0.00019143641120541132 |
| Cuba | 60.8 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Caribbean | 0.32331482781358345 | 0.052538659519707306 | 0.03637291812902813 |
| Curacao | 1 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Caribbean | 0.005317678089039202 | 0.0006248271754621063 | 0.0003589432710101462 |
| Dominican Republic | 58.951 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Caribbean | 0.31348244102695 | 0.03683418682066663 | 0.021160064769319125 |
| Jamaica | 14.84 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Caribbean | 0.07891434284134176 | 0.01578286856826835 | 0.011837151426201266 |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.083 | 0.033 | Caribbean | 0.007976517133558804 | 0.0006620509220853808 | 0.00026322506540744055 |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean | 0.007976517133558804 | 0.0005902622678833515 | 0.0001914364112054113 |
| St. Vincent & the Grenadines | 1.5 | B2 | 0.055 | 0.1325 | 0.0825 | Caribbean | 0.007976517133558804 | 0.0010568885201965416 | 0.0006580626635186013 |
| Trinidad and Tobago | 23.986 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean | 0.1275498266436943 | 0.009438687171633379 | 0.003061195839448663 |
| Caribbean | 188.052 |  | 0.05097667666390147 | 0.12646501499585222 | 0.0764650149958522 |  |  |  |  |
| Argentina | 474.865 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Central and South America | 0.09192370679809363 | 0.013558746752718813 | 0.00896256141281413 |
| Belize | 1.448 | Caa2 | 0.09 | 0.185 | 0.135 | Central and South America | 0.0002803018277692388 | 5.1855838137309173e-05 | 3.784074674884724e-05 |
| Bolivia | 27.035 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America | 0.005233397730484372 | 0.0005442733639703746 | 0.00028260347744615605 |
| Brazil | 2252.664 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America | 0.43606756667815233 | 0.034231303984234955 | 0.01242792565032734 |
| Chile | 268.314 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Central and South America | 0.05193985125419581 | 0.0030644512239975533 | 0.00046745866128776236 |
| Colombia | 369.813 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America | 0.07158788662487948 | 0.005941794589864997 | 0.002362400258621023 |
| Costa Rica | 45.127 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America | 0.008735621948717154 | 0.0007250566217435238 | 0.0002882755243076661 |
| Ecuador | 84.532 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Central and South America | 0.016363587089081002 | 0.0026590829019756622 | 0.0018409035475216125 |
| El Salvador | 23.787 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America | 0.004604654404106963 | 0.0004788840580271241 | 0.00024865133782177594 |
| Guatemala | 50.806 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Central and South America | 0.00983495487682593 | 0.0008605585517222689 | 0.0003688108078809724 |
| Honduras | 17.967 | B2 | 0.055 | 0.1325 | 0.0825 | Central and South America | 0.0034780268919405474 | 0.00046083856318212255 | 0.0002869372185850952 |
| Mexico | 1177.271 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Central and South America | 0.227894484171077 | 0.0168641918286597 | 0.005469467620105848 |
| Nicaragua | 10.507 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Central and South America | 0.002033930458820022 | 0.0003000047426759533 | 0.00019830821973495217 |
| Panama | 36.253 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America | 0.007017805360578877 | 0.0005508977208054419 | 0.00020000745277649797 |
| Paraguay | 25.502 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America | 0.004936641720836413 | 0.0005134107389669869 | 0.0002665786529251663 |
| Peru | 197.111 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America | 0.038156473462308306 | 0.002995283166791202 | 0.0010874594936757867 |
| Suriname | 4.738 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America | 0.000917175455780838 | 9.538624740120714e-05 | 4.9527474612165245e-05 |
| Uruguay | 49.06 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America | 0.009496966623176005 | 0.0007882482297236084 | 0.0003133998985648082 |
| Venezuela | 49.06 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Central and South America | 0.009496966623176005 | 0.0015432570762661006 | 0.0010684087451073004 |
| Central and South America | 5165.860000000001 |  | 0.024151684133909942 | 0.0862275262008649 | 0.03622752620086491 |  |  |  |  |
| Albania | 13.119 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Eastern Europe & Russia | 0.0033169311396094516 | 0.0003897394089041106 | 0.000223892851923638 |
| Armenia | 9.91 | Ba2 | 0.03 | 0.095 | 0.045 | Eastern Europe & Russia | 0.0025055863704192137 | 0.0002380307051898253 | 0.00011275138666886462 |
| Azerbaijan | 67.198 | Baa3 | 0.022 | 0.083 | 0.033 | Eastern Europe & Russia | 0.016989948831425863 | 0.0014101657530083468 | 0.0005606683114370535 |
| Belarus | 63.267 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia | 0.015996057810021433 | 0.0023594185269781615 | 0.0015596156364770897 |
| Bosnia and Herzegovina | 17.048 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia | 0.004310316492725202 | 0.0006357716826769673 | 0.0004202558580407072 |
| Bulgaria | 51.03 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia | 0.012902126385720735 | 0.0010128169212790777 | 0.0003677106019930409 |
| Croatia | 56.442 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia | 0.014270464774894173 | 0.0012486656678032404 | 0.0005351424290585316 |
| Czech Republic | 195.657 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Eastern Europe & Russia | 0.04946877017932514 | 0.002992860595849171 | 0.000519422086882914 |
| Estonia | 21.854 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Eastern Europe & Russia | 0.005525437390428002 | 0.00033428896212089415 | 5.801709259949402e-05 |
| Georgia | 15.829 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia | 0.004002111670773536 | 0.0004162196137604477 | 0.0002161140302217709 |
| Hungary | 125.508 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia | 0.03173270778794901 | 0.0027766119314455388 | 0.001189976542048088 |
| Kazakhstan | 201.68 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia | 0.05099159023069092 | 0.004002839833109237 | 0.0014532603215746912 |
| Latvia | 28.374 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia | 0.007173916011531258 | 0.0005631524069052038 | 0.00020445660632864086 |
| Lithuania | 42.246 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Eastern Europe & Russia | 0.010681231261829476 | 0.0007904111133753813 | 0.0002563495502839074 |
| Macedonia | 9.663 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia | 0.002443136336766989 | 0.00025408617902376683 | 0.0001319293621854174 |
| Moldova | 7.254 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia | 0.0018340588830495434 | 0.0002705236852498077 | 0.00017882074109733047 |
| Montenegro | 4.231 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia | 0.0010697412647067298 | 0.0001112530915294999 | 5.77660282941634e-05 |
| Poland | 489.795 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Eastern Europe & Russia | 0.12383689972749534 | 0.007770765457900333 | 0.0015789204715255657 |
| Romania | 169.396 | Baa3 | 0.022 | 0.083 | 0.033 | Eastern Europe & Russia | 0.04282909271478639 | 0.0035548146953272705 | 0.001413360059587951 |
| Russia | 2014.775 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Eastern Europe & Russia | 0.5094039131646187 | 0.037695889574181796 | 0.012225693915950851 |
| Serbia | 37.489 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Eastern Europe & Russia | 0.009478499237199385 | 0.0011137236603709277 | 0.0006397986985109585 |
| Slovakia | 91.619 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Eastern Europe & Russia | 0.023164411470377188 | 0.0014535668197661685 | 0.00029534624624730915 |
| Slovenia | 45.469 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia | 0.011496115709040487 | 0.0010059101245410427 | 0.00043110433908901834 |
| Ukraine | 176.309 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Eastern Europe & Russia | 0.04457693515461566 | 0.007243751962625044 | 0.005014905204894261 |
| Eastern Europe & Russia | 3955.1620000000007 |  | 0.019763518915280838 | 0.07964527837292125 | 0.029645278372921257 |  |  |  |  |
| Abu Dhabi | 15 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East | 0.008727602789341852 | 0.0005018371603871565 | 6.545702092006388e-05 |
| Bahrain | 22.945 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Middle East | 0.013350323066763252 | 0.0010480003607409153 | 0.00038048420740275263 |
| Israel | 242.929 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Middle East | 0.14134585453413512 | 0.008551424199315176 | 0.0014841314726084188 |
| Jordan | 31.243 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Middle East | 0.018178432929827164 | 0.0021359658692546917 | 0.0012270442227633337 |
| Kuwait | 176.59 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East | 0.10274715843799184 | 0.005907961610184531 | 0.0007706036882849388 |
| Lebanon | 42.945 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Middle East | 0.024987126785885723 | 0.0029359873973415726 | 0.0016866310580472864 |
| Oman | 71.782 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Middle East | 0.041765652228302454 | 0.0025268219598122985 | 0.0004385393483971758 |
| Qatar | 172.982 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East | 0.10064787904706214 | 0.005787253045206073 | 0.0007548590928529661 |
| Ras Al Kaminah | 5.2 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Middle East | 0.003025568966971842 | 0.0001898544526774831 | 3.857600432889099e-05 |
| Saudi Arabia | 576.824 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Middle East | 0.3356193834239549 | 0.01980154362201334 | 0.0030205744508155948 |
| United Arab Emirates | 360.245 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East | 0.2096050177897637 | 0.012052288522911413 | 0.0015720376334232278 |
| Middle East | 1718.685 |  | 0.0076259587998964325 | 0.06143893819984465 | 0.011438938199844649 |  |  |  |  |
| Canada | 1821.424 | Aaa | 0 | 0.05 | 0 | North America | 0.10404436730616495 | 0.005202218365308248 | 0 |
| United States of America | 15684.8 | Aaa | 0 | 0.05 | 0 | North America | 0.8959556326938352 | 0.04479778163469176 | 0 |
| North America | 17506.224 |  | 0 | 0.05000000000000001 | 0 |  |  |  |  |
| Andorra | 4.5 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Western Europe | 0.00026060175725502264 | 1.772091949334154e-05 | 4.690831630590408e-06 |
| Austria | 399.649 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.02314427370782501 | 0.0011572136853912505 | 0 |
| Belgium | 483.709 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Western Europe | 0.028012314533348834 | 0.0016527265574675814 | 0.0002521108308001395 |
| Cyprus | 22.981 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Western Europe | 0.0013308642185505947 | 0.0002661728437101189 | 0.00019962963278258924 |
| Denmark | 314.242 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.018198226089629517 | 0.0009099113044814758 | 0 |
| Finland | 250.024 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.014479265279095507 | 0.0007239632639547753 | 0 |
| France | 2612.878 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe | 0.15131568850955313 | 0.008473678556534974 | 0.0009078941310573188 |
| Germany | 3399.589 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.19687530385441002 | 0.009843765192720502 | 0 |
| Greece | 249.099 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Western Europe | 0.014425697140104195 | 0.0028851394280208394 | 0.0021638545710156295 |
| Iceland | 13.657 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe | 0.0007908973775181875 | 6.564448233400958e-05 | 2.609961345810019e-05 |
| Ireland | 210.331 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Western Europe | 0.01218058404560137 | 0.00106580110399012 | 0.00045677190171005143 |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe | 8.107610225711815e-05 | 4.540261726398616e-06 | 4.864566135427089e-07 |
| Italy | 2013.263 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Western Europe | 0.11659108347033748 | 0.009152400052421492 | 0.003322845878904618 |
| Liechtenstein | 10.5 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.0006080707669283862 | 3.040353834641931e-05 | 0 |
| Luxembourg | 57.117 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.003307731237585584 | 0.00016538656187927922 | 0 |
| Malta | 8.722 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Western Europe | 0.000505104117061846 | 3.434707996020553e-05 | 9.09187410711323e-06 |
| Netherlands | 772.227 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.04472082515550541 | 0.0022360412577752706 | 0 |
| Norway | 499.667 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.028936466276076753 | 0.0014468233138038378 | 0 |
| Portugal | 212.454 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Western Europe | 0.01230353016352413 | 0.0012795671370065096 | 0.0006643906288303029 |
| Spain | 1349.351 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe | 0.07814294261196046 | 0.006485864236792718 | 0.0025787171061946953 |
| Sweden | 525.742 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.03044650868061558 | 0.001522325434030779 | 0 |
| Switzerland | 632.194 | Aaa | 0 | 0.05 | 0 | Western Europe | 0.0366113038502404 | 0.00183056519251202 | 0 |
| Turkey | 789.257 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe | 0.04570705802796164 | 0.0037936858163208163 | 0.0015083329149227342 |
| United Kingdom | 2435.174 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe | 0.1410245830270539 | 0.007897376649515018 | 0.0008461474981623234 |
| Western Europe | 17267.727 |  | 0.008627375913459833 | 0.06294106387018976 | 0.01294106387018975 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Region | Weighted Average: TRP | Weighted Average: CRP | Weighted Average: Default Spreads |  |  |  |  |  |  |
| Africa | 0.10039475352432138 | 0.05039475352432139 | 0.03359650234954759 |  |  |  |  |  |  |
| Asia | 0.06505385171898466 | 0.015053851718984658 | 0.010035901145989772 |  |  |  |  |  |  |
| Australia & New Zealand | 0.05004874889863599 | 4.874889863599378e-05 | 3.249926575732918e-05 |  |  |  |  |  |  |
| Caribbean | 0.12646501499585222 | 0.0764650149958522 | 0.05097667666390147 |  |  |  |  |  |  |
| Central and South America | 0.0862275262008649 | 0.03622752620086491 | 0.024151684133909942 |  |  |  |  |  |  |
| Eastern Europe & Russia | 0.07964527837292125 | 0.029645278372921257 | 0.019763518915280838 |  |  |  |  |  |  |
| Middle East | 0.06143893819984465 | 0.011438938199844649 | 0.0076259587998964325 |  |  |  |  |  |  |
| North America | 0.05000000000000001 | 0 | 0 |  |  |  |  |  |  |
| Western Europe | 0.06294106387018976 | 0.01294106387018975 | 0.008627375913459833 |  |  |  |  |  |  |
| Global | 0.0635 | 0.0135 | 0.009 |  |  |  |  |  |  |

## Regional breakdown

| Country | GDP | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|
| Abu Dhabi | 15 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East |
| Albania | 13.119 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Eastern Europe & Russia |
| Andorra | 4.5 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Western Europe |
| Angola | 114.197 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa |
| Argentina | 474.865 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Central and South America |
| Armenia | 9.91 | Ba2 | 0.03 | 0.095 | 0.045 | Eastern Europe & Russia |
| Aruba | 2.584 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean |
| Australia | 1520.608 | Aaa | 0 | 0.05 | 0 | Australia & New Zealand |
| Austria | 399.649 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Azerbaijan | 67.198 | Baa3 | 0.022 | 0.083 | 0.033 | Eastern Europe & Russia |
| Bahamas | 8.149 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean |
| Bahrain | 22.945 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Middle East |
| Bangladesh | 115.61 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Asia |
| Barbados | 3.685 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Caribbean |
| Belarus | 63.267 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia |
| Belgium | 483.709 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Western Europe |
| Belize | 1.448 | Caa2 | 0.09 | 0.185 | 0.135 | Central and South America |
| Benin | 7.557 | B2 | 0.055 | 0.1325 | 0.0825 | Africa |
| Bermuda | 5.557 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Caribbean |
| Bolivia | 27.035 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America |
| Bosnia and Herzegovina | 17.048 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia |
| Botswana | 14.411 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Africa |
| Brazil | 2252.664 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America |
| Bulgaria | 51.03 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia |
| Burkina Faso | 10.441 | B2 | 0.055 | 0.1325 | 0.0825 | Africa |
| Cambodia | 14.062 | B2 | 0.055 | 0.1325 | 0.0825 | Asia |
| Cameroon | 24.984 | B2 | 0.055 | 0.1325 | 0.0825 | Africa |
| Canada | 1821.424 | Aaa | 0 | 0.05 | 0 | North America |
| Cape Verde | 1.897 | B2 | 0.055 | 0.1325 | 0.0825 | Africa |
| Cayman Islands | 4 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Caribbean |
| Chile | 268.314 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Central and South America |
| China | 8227.103 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia |
| Colombia | 369.813 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America |
| Cook Islands | 1.2 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Australia & New Zealand |
| Costa Rica | 45.127 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America |
| Croatia | 56.442 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia |
| Cuba | 60.8 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Caribbean |
| Curacao | 1 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Caribbean |
| Cyprus | 22.981 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Western Europe |
| Czech Republic | 195.657 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Eastern Europe & Russia |
| Democratic Republic of Congo | 17.9 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Africa |
| Denmark | 314.242 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Dominican Republic | 58.951 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Caribbean |
| Ecuador | 84.532 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Central and South America |
| Egypt | 84.532 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Africa |
| El Salvador | 23.787 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America |
| Estonia | 21.854 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Eastern Europe & Russia |
| Fiji | 3.882 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia |
| Finland | 250.024 | Aaa | 0 | 0.05 | 0 | Western Europe |
| France | 2612.878 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe |
| Gabon | 18.661 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa |
| Georgia | 15.829 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia |
| Germany | 3399.589 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Ghana | 40.71 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |
| Greece | 249.099 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Western Europe |
| Guatemala | 50.806 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Central and South America |
| Honduras | 17.967 | B2 | 0.055 | 0.1325 | 0.0825 | Central and South America |
| Hong Kong | 263.259 | Aa1 | 0.004 | 0.056 | 0.006 | Asia |
| Hungary | 125.508 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia |
| Iceland | 13.657 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe |
| India | 1841.717 | Baa3 | 0.022 | 0.083 | 0.033 | Asia |
| Indonesia | 878.043 | Baa3 | 0.022 | 0.083 | 0.033 | Asia |
| Ireland | 210.331 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Western Europe |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe |
| Israel | 242.929 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Middle East |
| Italy | 2013.263 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Western Europe |
| Jamaica | 14.84 | Caa3 | 0.1 | 0.2 | 0.15000000000000002 | Caribbean |
| Japan | 5959.718 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia |
| Jordan | 31.243 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Middle East |
| Kazakhstan | 201.68 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia |
| Kenya | 37.229 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |
| Korea | 1129.598 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia |
| Kuwait | 176.59 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East |
| Latvia | 28.374 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Eastern Europe & Russia |
| Lebanon | 42.945 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Middle East |
| Liechtenstein | 10.5 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Lithuania | 42.246 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Eastern Europe & Russia |
| Luxembourg | 57.117 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Macao | 43.582 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia |
| Macedonia | 9.663 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia |
| Malaysia | 303.526 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Asia |
| Malta | 8.722 | A3 | 0.012 | 0.068 | 0.018000000000000002 | Western Europe |
| Mauritius | 10.492 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Asia |
| Mexico | 1177.271 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Central and South America |
| Moldova | 7.254 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Eastern Europe & Russia |
| Mongolia | 10.271 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia |
| Montenegro | 4.231 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Eastern Europe & Russia |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.083 | 0.033 | Caribbean |
| Morocco | 96.729 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Africa |
| Mozambique | 14.588 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |
| Namibia | 12.807 | Baa3 | 0.022 | 0.083 | 0.033 | Africa |
| Netherlands | 772.227 | Aaa | 0 | 0.05 | 0 | Western Europe |
| New Zealand | 139.768 | Aaa | 0 | 0.05 | 0 | Australia & New Zealand |
| Nicaragua | 10.507 | B3 | 0.065 | 0.14750000000000002 | 0.0975 | Central and South America |
| Nigeria | 262.606 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa |
| Norway | 499.667 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Oman | 71.782 | A1 | 0.007 | 0.060500000000000005 | 0.0105 | Middle East |
| Pakistan | 231.182 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Asia |
| Panama | 36.253 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America |
| Papua New Guinea | 15.654 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia |
| Paraguay | 25.502 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America |
| Peru | 197.111 | Baa2 | 0.019 | 0.0785 | 0.028499999999999998 | Central and South America |
| Philippines | 250.265 | Baa3 | 0.022 | 0.083 | 0.033 | Asia |
| Poland | 489.795 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Eastern Europe & Russia |
| Portugal | 212.454 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Western Europe |
| Qatar | 172.982 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East |
| Ras Al Kaminah | 5.2 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Middle East |
| Republic of the Congo | 13.7 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa |
| Romania | 169.396 | Baa3 | 0.022 | 0.083 | 0.033 | Eastern Europe & Russia |
| Russia | 2014.775 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Eastern Europe & Russia |
| Rwanda | 7.103 | B2 | 0.055 | 0.1325 | 0.0825 | Africa |
| Saudi Arabia | 576.824 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Middle East |
| Senegal | 14.16 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |
| Serbia | 37.489 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Eastern Europe & Russia |
| Singapore | 274.701 | Aaa | 0 | 0.05 | 0 | Asia |
| Slovakia | 91.619 | A2 | 0.0085 | 0.06275 | 0.012750000000000001 | Eastern Europe & Russia |
| Slovenia | 45.469 | Ba1 | 0.025 | 0.08750000000000001 | 0.037500000000000006 | Eastern Europe & Russia |
| South Africa | 384.313 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Africa |
| Spain | 1349.351 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe |
| Sri Lanka | 59.421 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Asia |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean |
| St. Vincent & the Grenadines | 1.5 | B2 | 0.055 | 0.1325 | 0.0825 | Caribbean |
| Suriname | 4.738 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Central and South America |
| Sweden | 525.742 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Switzerland | 632.194 | Aaa | 0 | 0.05 | 0 | Western Europe |
| Taiwan | 44.02 | Aa3 | 0.006 | 0.059000000000000004 | 0.009000000000000001 | Asia |
| Thailand | 365.564 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Asia |
| Trinidad and Tobago | 23.986 | Baa1 | 0.016 | 0.07400000000000001 | 0.024 | Caribbean |
| Tunisia | 45.662 | Ba3 | 0.036 | 0.104 | 0.05399999999999999 | Africa |
| Turkey | 789.257 | Baa3 | 0.022 | 0.083 | 0.033 | Western Europe |
| Uganda | 33.679 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |
| Ukraine | 176.309 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Eastern Europe & Russia |
| United Arab Emirates | 360.245 | Aa2 | 0.005 | 0.0575 | 0.0075 | Middle East |
| United Kingdom | 2435.174 | Aa1 | 0.004 | 0.056 | 0.006 | Western Europe |
| United States of America | 15684.8 | Aaa | 0 | 0.05 | 0 | North America |
| Uruguay | 49.06 | Baa3 | 0.022 | 0.083 | 0.033 | Central and South America |
| Venezuela | 49.06 | Caa1 | 0.075 | 0.16249999999999998 | 0.11249999999999999 | Central and South America |
| Vietnam | 141.669 | B2 | 0.055 | 0.1325 | 0.0825 | Asia |
| Zambia | 20.678 | B1 | 0.045 | 0.11750000000000001 | 0.0675 | Africa |

## Sovereign Ratings (Moody's)

| S&P Rating | Moody's rating |
|---|---|
| AA | Aa2 |
| B | B1 |
| A- | A3 |
| BB- | Ba3 |
| CCC+ | B3 |
| NA | Ba2 |
| BBB+ | Baa1 |
| AAA | Aaa |
| AA+ | Aaa |
| BBB- | Baa3 |
| BBB | Baa1 |
| BBB | Baa2 |
| BB- | Ba3 |
| BB- | Ba1 |
| B- | B3 |
| AA | Aa3 |
| B- | Caa2 |
| B | B2 |
| AA- | Aa3 |
| BB- | Ba3 |
| B | B3 |
| A- | A2 |
| A- | Baa2 |
| BBB | Baa2 |
| B | B2 |
| B | B2 |
| B | B2 |
| AAA | Aaa |
| B | B2 |
| NA | Aa3 |
| AA+ | Aa3 |
| AA- | Aa3 |
| BBB+ | Baa3 |
| B+ | B1 |
| BB | Baa3 |
| BB+ | Ba1 |
| NA | Caa1 |
| A- | B1 |
| B- | Caa3 |
| AA | A1 |
| B- | B3 |
| AAA | Aaa |
| B+ | B1 |
| B | Caa1 |
| B- | Caa1 |
| BB- | Ba3 |
| AA- | A1 |
| NA | B1 |
| AAA | Aaa |
| AA | Aa1 |
| BB- | Ba3 |
| BB= | Ba3 |
| AAA | Aaa |
| B | B1 |
| B- | Caa3 |
| BB+ | Ba1 |
| B | B2 |
| AAA | Aa1 |
| BB | Ba1 |
| BBB- | Baa3 |
| BBB- | Baa3 |
| BB+ | Baa3 |
| BBB+ | Ba1 |
| AA+ | Aa1 |
| A+ | A1 |
| BBB | Baa2 |
| B- | Caa3 |
| AA- | Aa3 |
| BB- | B1 |
| BBB+ | Baa2 |
| B+ | B1 |
| AA- | Aa3 |
| AA | Aa2 |
| BBB+ | Baa2 |
| B- | B1 |
| AAA | Aaa |
| BBB | Baa1 |
| AAA | Aaa |
| NA | Aa3 |
| BB- | Ba3 |
| A | A3 |
| BBB+ | A3 |
| NA | Baa1 |
| A | Baa1 |
| NA | B3 |
| BB- | B1 |
| BB- | Ba3 |
| BBB- | Baa3 |
| BBB- | Ba1 |
| B+ | B1 |
| NA | Baa3 |
| AA+ | Aaa |
| AA+ | Aaa |
| NA | B3 |
| BB- | Ba3 |
| AAA | Aaa |
| A | A1 |
| B- | Caa1 |
| BBB | Baa2 |
| B+ | B1 |
| BB- | Ba3 |
| A- | Baa2 |
| BBB- | Baa3 |
| A | A2 |
| BB | Ba3 |
| AA | Aa2 |
| A | A2 |
| NA | Ba3 |
| BB+ | Baa3 |
| BBB+ | Baa1 |
| B | B2 |
| AAA | Aa3 |
| B+ | B1 |
| BB- | B1 |
| AAA | Aaa |
| A | A2 |
| A- | Ba1 |
| A- | Baa1 |
| BBB- | Baa3 |
| B+ | B1 |
| NA | Baa1 |
| NA | B2 |
| BB- | Ba3 |
| AAA | Aaa |
| AAA | Aaa |
| AA- | Aa3 |
| A- | Baa1 |
| A | Baa1 |
| NA | Ba3 |
| BBB | Baa3 |
| B+ | B1 |
| B+ | Caa1 |
| NA | Aa2 |
| AAA | Aa1 |
| AA+ | Aaa |
| BBB- | Baa3 |
| B- | Caa1 |
| BB- | B2 |
| B+ | B1 |

## Regional lookup table

| Country | Region |
|---|---|
| Abu Dhabi | Middle East |
| Albania | Eastern Europe & Russia |
| Andorra | Western Europe |
| Angola | Africa |
| Argentina | Central and South America |
| Armenia | Eastern Europe & Russia |
| Aruba | Caribbean |
| Australia | Australia & New Zealand |
| Austria | Western Europe |
| Azerbaijan | Eastern Europe & Russia |
| Bahamas | Caribbean |
| Bahrain | Middle East |
| Bangladesh | Asia |
| Barbados | Caribbean |
| Belarus | Eastern Europe & Russia |
| Belgium | Western Europe |
| Belize | Central and South America |
| Benin | Africa |
| Bermuda | Caribbean |
| Bolivia | Central and South America |
| Bosnia and Herzegovina | Eastern Europe & Russia |
| Botswana | Africa |
| Brazil | Central and South America |
| Bulgaria | Eastern Europe & Russia |
| Burkina Faso | Africa |
| Cambodia | Asia |
| Cameroon | Africa |
| Canada | North America |
| Cape Verde | Africa |
| Cayman Islands | Caribbean |
| Chile | Central and South America |
| China | Asia |
| Colombia | Central and South America |
| Cook Islands | Australia & New Zealand |
| Costa Rica | Central and South America |
| Croatia | Eastern Europe & Russia |
| Cuba | Caribbean |
| Curacao | Caribbean |
| Cyprus | Western Europe |
| Czech Republic | Eastern Europe & Russia |
| Democratic Republic of Congo | Africa |
| Denmark | Western Europe |
| Dominican Republic | Caribbean |
| Ecuador | Central and South America |
| Egypt | Africa |
| El Salvador | Central and South America |
| Estonia | Eastern Europe & Russia |
| Fiji | Asia |
| Finland | Western Europe |
| France | Western Europe |
| Gabon | Africa |
| Georgia | Eastern Europe & Russia |
| Germany | Western Europe |
| Ghana | Africa |
| Greece | Western Europe |
| Guatemala | Central and South America |
| Honduras | Central and South America |
| Hong Kong | Asia |
| Hungary | Eastern Europe & Russia |
| Iceland | Western Europe |
| India | Asia |
| Indonesia | Asia |
| Ireland | Western Europe |
| Isle of Man | Western Europe |
| Israel | Middle East |
| Italy | Western Europe |
| Jamaica | Caribbean |
| Japan | Asia |
| Jordan | Middle East |
| Kazakhstan | Eastern Europe & Russia |
| Kenya | Africa |
| Korea | Asia |
| Kuwait | Middle East |
| Latvia | Eastern Europe & Russia |
| Lebanon | Middle East |
| Liechtenstein | Western Europe |
| Lithuania | Eastern Europe & Russia |
| Luxembourg | Western Europe |
| Macao | Asia |
| Macedonia | Eastern Europe & Russia |
| Malaysia | Asia |
| Malta | Western Europe |
| Mauritius | Asia |
| Mexico | Central and South America |
| Moldova | Eastern Europe & Russia |
| Mongolia | Asia |
| Montenegro | Eastern Europe & Russia |
| Montserrat | Caribbean |
| Morocco | Africa |
| Mozambique | Africa |
| Namibia | Africa |
| Netherlands | Western Europe |
| New Zealand | Australia & New Zealand |
| Nicaragua | Central and South America |
| Nigeria | Africa |
| Norway | Western Europe |
| Oman | Middle East |
| Pakistan | Asia |
| Panama | Central and South America |
| Papua New Guinea | Asia |
| Paraguay | Central and South America |
| Peru | Central and South America |
| Philippines | Asia |
| Poland | Eastern Europe & Russia |
| Portugal | Western Europe |
| Qatar | Middle East |
| Ras Al Kaminah | Middle East |
| Republic of the Congo | Africa |
| Romania | Eastern Europe & Russia |
| Russia | Eastern Europe & Russia |
| Rwanda | Africa |
| Saudi Arabia | Middle East |
| Senegal | Africa |
| Serbia | Eastern Europe & Russia |
| Singapore | Asia |
| Slovakia | Eastern Europe & Russia |
| Slovenia | Eastern Europe & Russia |
| South Africa | Africa |
| Spain | Western Europe |
| Sri Lanka | Asia |
| St. Maarten | Caribbean |
| St. Vincent & the Grenadines | Caribbean |
| Suriname | Central and South America |
| Sweden | Western Europe |
| Switzerland | Western Europe |
| Taiwan | Asia |
| Thailand | Asia |
| Trinidad and Tobago | Caribbean |
| Tunisia | Africa |
| Turkey | Western Europe |
| Turkmenistan | Eastern Europe & Russia |
| Uganda | Africa |
| Ukraine | Eastern Europe & Russia |
| United Arab Emirates | Middle East |
| United Kingdom | Western Europe |
| United States of America | North America |
| Uruguay | Central and South America |
| Venezuela | Central and South America |
| Vietnam | Asia |
| Zambia | Africa |

## Rating  CDS

|  |
||
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
|  |
|  |
|  |
|  |

## 10-year CDS Spreads

| Country | Moody's local currency | 10-year CDS | Updated: January 2, 2014 |
|---|---|---|---|
| Abu Dhabi | Aa2 | 0.01 |  |
| Albania | B1 | NA |  |
| Andorra | A3 | NA |  |
| Angola | Ba3 | NA |  |
| Argentina | B3 | 0.1473 |  |
| Armenia | Ba2 | NA |  |
| Aruba | Baa1 | NA |  |
| Australia | Aaa | 0.007 |  |
| Austria | Aaa | 0.0074 |  |
| Azerbaijan | Baa3 | NA |  |
| Bahamas | Baa1 | NA |  |
| Bahrain | Baa1 | 0.0297 |  |
| Bangladesh | Ba3 | NA |  |
| Barbados | Ba1 | NA |  |
| Belarus | B3 | NA |  |
| Belgium | Aa3 | 0.0097 |  |
| Belize | Caa2 | NA |  |
| Benin | B2 | NA |  |
| Bermuda | Aa3 | NA |  |
| Bolivia | Ba3 | NA |  |
| Bosnia and Herzegovina | B3 | NA |  |
| Botswana | A2 | NA |  |
| Brazil | Baa2 | 0.0253 |  |
| Bulgaria | Baa2 | 0.0189 |  |
| Burkina Faso | B2 | NA |  |
| Cambodia | B2 | NA |  |
| Cameroon | B2 | NA |  |
| Canada | Aaa | NA |  |
| Cape Verde | B1 | NA |  |
| Cayman Islands | Aaa | NA |  |
| Chile | Aa3 | 0.0108 |  |
| China | Aa3 | 0.0133 |  |
| Colombia | Baa3 | 0.0174 |  |
| Cook Islands | B1 | NA |  |
| Costa Rica | Baa3 | 0.0343 |  |
| Croatia | Ba1 | 0.0397 |  |
| Cuba | Caa1 | NA |  |
| Curacao | B1 | NA |  |
| Cyprus | Caa3 | NA |  |
| Czech Republic | A1 | 0.0107 |  |
| Democratic Republic of Congo | B3 | NA |  |
| Denmark | Aaa | 0.0054 |  |
| Dominican Republic | B1 | NA |  |
| Ecuador | Caa1 | NA |  |
| Egypt | Caa1 | NA |  |
| El Salvador | Ba3 | NA |  |
| Estonia | A1 | 0.0089 |  |
| Fiji | B1 | NA |  |
| Finland | Aaa | 0.0048 |  |
| France | Aa1 | 0.0106 |  |
| Gabon | Ba3 | NA |  |
| Georgia | Ba3 | NA |  |
| Germany | Aaa | 0.0056 |  |
| Ghana | B1 | NA |  |
| Greece | C | NA |  |
| Guatemala | Ba1 | NA |  |
| Honduras | B2 | NA |  |
| Hong Kong | Aa1 | 0.0091 |  |
| Hungary | Ba1 | 0.0308 |  |
| Iceland | Baa3 | 0.0219 |  |
| India | Baa3 | 0.0351 |  |
| Indonesia | Baa3 | 0.0319 |  |
| Ireland | Ba1 | 0.0169 |  |
| Isle of Man | Aaa | NA |  |
| Israel | A1 | 0.0153 |  |
| Italy | Baa2 | 0.0211 |  |
| Jamaica | Caa3 | NA |  |
| Japan | Aa3 | 0.0079 |  |
| Jordan | B1 | NA |  |
| Kazakhstan | Baa2 | 0.0226 |  |
| Kenya | B1 | NA |  |
| Korea | Aa3 | 0.0097 |  |
| Kuwait | Aa2 | NA |  |
| Latvia | Baa2 | 0.0169 |  |
| Lebanon | B1 | 0.0438 |  |
| Liechtenstein | Aaa | NA |  |
| Lithuania | Baa1 | 0.0177 |  |
| Luxembourg | Aaa | NA |  |
| Macao | Aa3 | NA |  |
| Macedonia | Ba3 | NA |  |
| Malaysia | A3 | 0.0165 |  |
| Malta | A3 | NA |  |
| Mauritius | Baa1 | NA |  |
| Mexico | Baa1 | 0.0149 |  |
| Moldova | B3 | NA |  |
| Mongolia | B1 | NA |  |
| Montenegro | Ba3 | NA |  |
| Montserrat | Baa3 | NA |  |
| Morocco | Ba1 | 0.0254 |  |
| Mozambique | B1 | NA |  |
| Namibia | Baa3 | NA |  |
| Netherlands | Aaa | 0.0074 |  |
| New Zealand | Aaa | 0.008 |  |
| Nicaragua | B3 | NA |  |
| Nigeria | Ba3 | NA |  |
| Norway | Aaa | 0.0029 |  |
| Oman | A1 | NA |  |
| Pakistan | Caa1 | NA |  |
| Panama | Baa2 | 0.0164 |  |
| Papua New Guinea | B1 | NA |  |
| Paraguay | Ba3 | NA |  |
| Peru | Baa2 | 0.0188 |  |
| Philippines | Ba1 | 0.0181 |  |
| Poland | A2 | 0.0128 |  |
| Portugal | Ba3 | 0.0403 |  |
| Qatar | Aa2 | 0.0103 |  |
| Ras Al Kaminah | A2 | NA |  |
| Republic of the Congo | Ba3 | NA |  |
| Romania | Baa3 | 0.0261 |  |
| Russia | Baa1 | 0.0221 |  |
| Rwanda | B2 | NA |  |
| Saudi Arabia | Aa3 | 0.0109 |  |
| Senegal | B1 | 0.009 |  |
| Serbia | Ba3 | NA |  |
| Singapore | Aaa | NA |  |
| Slovakia | A2 | 0.013 |  |
| Slovenia | Ba1 | 0.0275 |  |
| South Africa | Baa1 | 0.0275 |  |
| Spain | Baa3 | 0.0196 |  |
| Sri Lanka | B1 | NA |  |
| St. Maarten | Baa1 | NA |  |
| St. Vincent & the Grenadines | B2 | NA |  |
| Suriname | Ba3 | NA |  |
| Sweden | Aaa | 0.0039 |  |
| Switzerland | Aaa | 0.0056 |  |
| Taiwan | Aa3 | NA |  |
| Thailand | Baa1 | 0.0186 |  |
| Trinidad and Tobago | Baa1 | NA |  |
| Tunisia | Ba2 | 0.0457 |  |
| Turkey | Baa3 | 0.0289 |  |
| Uganda | B1 | NA |  |
| Ukraine | B3 | NA |  |
| United Arab Emirates | Aa2 | 0.0288 |  |
| United Kingdom | Aa1 | 0.0057 |  |
| United States of America | Aaa | 0.0046 |  |
| Uruguay | Baa3 | NA |  |
| Venezuela | B1 | 0.108 |  |
| Vietnam | B2 | 0.0335 |  |
| Zambia | B1 | NA |  |

## Equity vs Govt Bond volatility

| Country | Std deviation in Equities (weekly over 2 years) | Std deviation in Bond Price | Relative Standard Deviation |
|---|---|---|---|
| Argentina | 0.2985 | 0.1827 | 1.6338259441707716 |
| Bangladesh | 0.3607 | NA | NA |
| Bosnia | 0.1421 | NA | NA |
| Brazil | 0.218 | 0.1258 | 1.7329093799682036 |
| Bulgaria | 0.1662 | NA | NA |
| Chile | 0.1566 | 0.085 | 1.8423529411764703 |
| China | 0.22 | 0.112 | 1.9642857142857142 |
| Colombia | 0.1781 | 0.1452 | 1.2265840220385675 |
| Croatia | 0.15 | 0.0908 | 1.6519823788546253 |
| Czech Republic | 0.2145 | 0.109 | 1.9678899082568808 |
| Egypt | 0.2629 | 0.1635 | 1.6079510703363915 |
| Estonia | 0.2158 | NA | NA |
| Greece | 0.329 | 0.3917 | 0.8399285167219812 |
| Hungary | 0.2708 | 0.1824 | 1.4846491228070173 |
| Iceland | 0.1431 | 0.1241 | 1.153102336825141 |
| India | 0.1987 | 0.0801 | 2.4806491885143567 |
| Indonesia | 0.2058 | 0.2043 | 1.0073421439060206 |
| Ireland | 0.2256 | 0.2486 | 0.9074818986323412 |
| Israel | 0.1858 | 0.092 | 2.019565217391304 |
| Italy | 0.2996 | 0.153 | 1.9581699346405228 |
| Kenya | 0.2841 | NA | NA |
| Korea | 0.1992 | 0.0655 | 3.041221374045801 |
| Lativia | 0.1524 | NA | NA |
| Lithuania | 0.1943 | NA | NA |
| Macedonia | 0.1687 | NA | NA |
| Malaysia | 0.1095 | 0.0864 | 1.267361111111111 |
| Mexico | 0.1802 | 0.1106 | 1.6292947558770343 |
| Morocco | 0.1136 | 0.0835 | 1.3604790419161676 |
| Namibia | 0.1951 | NA | NA |
| Nigeria | 0.144 | NA | NA |
| Pakistan | 0.1666 | 0.0754 | 2.2095490716180373 |
| Peru | 0.2651 | 0.1224 | 2.1658496732026147 |
| Philippines | 0.1835 | 0.1224 | 1.4991830065359477 |
| Poland | 0.1868 | 0.1167 | 1.6006855184233075 |
| Portugal | 0.2046 | 0.2969 | 0.6891209161333782 |
| Romania | 0.2373 | 0.1697 | 1.3983500294637596 |
| Russia | 0.2441 | 0.1255 | 1.9450199203187253 |
| Serbia | 0.1445 | NA | NA |
| Slovakia | 0.1706 | 0.1044 | 1.6340996168582376 |
| Slovenia | 0.1576 | 0.1263 | 1.2478226444972287 |
| South Africa | 0.1633 | 0.1018 | 1.6041257367387034 |
| Spain | 0.2914 | 0.3083 | 0.9451832630554654 |
| Sri Lanka | 0.1928 | NA | NA |
| Thailand | 0.1777 | 0.0988 | 1.798582995951417 |
| Tunisia | 0.17 | NA | NA |
| Turkey | 0.2452 | 0.1197 | 2.048454469507101 |
| Ukraine | 0.3783 | NA | NA |
| Venezuela | 0.1438 | 0.2087 | 0.6890273119310015 |
| Vietnam | 0.2542 | 0.1265 | 2.009486166007905 |
| US | 0.1955 |  |  |
|  |  |  |  |
| Average |  |  | 1.607473324049121 |
| Median |  |  | 1.6292947558770343 |

## Country GDP

| Country | GDP (in billions) |
|---|---|
| Abu Dhabi | 15 |
| Albania | 13.119 |
| Andorra | 4.5 |
| Angola | 114.197 |
| Argentina | 474.865 |
| Armenia | 9.91 |
| Aruba | 2.584 |
| Australia | 1520.608 |
| Austria | 399.649 |
| Azerbaijan | 67.198 |
| Bahamas | 8.149 |
| Bahrain | 22.945 |
| Bangladesh | 115.61 |
| Barbados | 3.685 |
| Belarus | 63.267 |
| Belgium | 483.709 |
| Belize | 1.448 |
| Benin | 7.557 |
| Bermuda | 5.557 |
| Bolivia | 27.035 |
| Bosnia and Herzegovina | 17.048 |
| Botswana | 14.411 |
| Brazil | 2252.664 |
| Bulgaria | 51.03 |
| Burkina Faso | 10.441 |
| Cambodia | 14.062 |
| Cameroon | 24.984 |
| Canada | 1821.424 |
| Cape Verde | 1.897 |
| Cayman Islands | 4 |
| Chile | 268.314 |
| China | 8227.103 |
| Colombia | 369.813 |
| Cook Islands | 1.2 |
| Costa Rica | 45.127 |
| Croatia | 56.442 |
| Cuba | 60.8 |
| Curacao | 1 |
| Cyprus | 22.981 |
| Czech Republic | 195.657 |
| Democratic Republic of Congo | 17.9 |
| Denmark | 314.242 |
| Dominican Republic | 58.951 |
| Ecuador | 84.532 |
| Egypt, Arab Rep. | 257.286 |
| El Salvador | 23.787 |
| Estonia | 21.854 |
| Fiji | 3.882 |
| Finland | 250.024 |
| France | 2612.878 |
| Gabon | 18.661 |
| Georgia | 15.829 |
| Germany | 3399.589 |
| Ghana | 40.71 |
| Greece | 249.099 |
| Guatemala | 50.806 |
| Honduras | 17.967 |
| Hong Kong | 263.259 |
| Hungary | 125.508 |
| Iceland | 13.657 |
| India | 1841.717 |
| Indonesia | 878.043 |
| Ireland | 210.331 |
| Isle of Man | 1.4 |
| Israel | 242.929 |
| Italy | 2013.263 |
| Jamaica | 14.84 |
| Japan | 5959.718 |
| Jordan | 31.243 |
| Kazakhstan | 201.68 |
| Kenya | 37.229 |
| Korea | 1129.598 |
| Kuwait | 176.59 |
| Latvia | 28.374 |
| Lebanon | 42.945 |
| Liechtenstein | 10.5 |
| Lithuania | 42.246 |
| Luxembourg | 57.117 |
| Macao | 43.582 |
| Macedonia | 9.663 |
| Malaysia | 303.526 |
| Malta | 8.722 |
| Mauritius | 10.492 |
| Mexico | 1177.271 |
| Moldova | 7.254 |
| Mongolia | 10.271 |
| Montenegro | 4.231 |
| Montserrat | 1.5 |
| Morocco | 96.729 |
| Mozambique | 14.588 |
| Namibia | 12.807 |
| Netherlands | 772.227 |
| New Zealand | 139.768 |
| Nicaragua | 10.507 |
| Nigeria | 262.606 |
| Norway | 499.667 |
| Oman | 71.782 |
| Pakistan | 231.182 |
| Panama | 36.253 |
| Papua New Guinea | 15.654 |
| Paraguay | 25.502 |
| Peru | 197.111 |
| Philippines | 250.265 |
| Poland | 489.795 |
| Portugal | 212.454 |
| Qatar | 172.982 |
| Ras Al Kaminah | 5.2 |
| Republic of the Congo | 13.7 |
| Romania | 169.396 |
| Russia | 2014.775 |
| Rwanda | 7.103 |
| Saudi Arabia | 576.824 |
| Senegal | 14.16 |
| Serbia | 37.489 |
| Singapore | 274.701 |
| Slovakia | 91.619 |
| Slovenia | 45.469 |
| South Africa | 384.313 |
| Spain | 1349.351 |
| Sri Lanka | 59.421 |
| St. Maarten | 1.5 |
| St. Vincent and the Grenadines | 0.713 |
| Suriname | 4.738 |
| Sweden | 525.742 |
| Switzerland | 632.194 |
| Taiwan | 44.02 |
| Thailand | 365.564 |
| Trinidad and Tobago | 23.986 |
| Tunisia | 45.662 |
| Turkey | 789.257 |
| Turkmenistan | 33.679 |
| Ukraine | 176.309 |
| United Arab Emirates | 360.245 |
| United Kingdom | 2435.174 |
| United States | 15684.8 |
| Uruguay | 49.06 |
| Venezuela, RB | 382.424 |
| Vietnam | 141.669 |
| Zambia | 20.678 |

## Ratings look up

| S&P Rating | Moody's rating |
|---|---|
| AA | Aa2 |
| B | B1 |
| A- | NA |
| BB- | Ba3 |
| CCC+ | B3 |
| NA | Ba2 |
| BBB+ | NA |
| AAA | Aaa |
| AA+ | Aaa |
| BBB- | Baa3 |
| BBB | Baa1 |
| BBB | Baa2 |
| BB- | Ba3 |
| BB- | Ba1 |
| B- | B3 |
| AA | Aa3 |
| B- | Caa2 |
| B | NA |
| AA- | Aa3 |
| BB- | Ba3 |
| B | B3 |
| A- | A2 |
| A- | Baa2 |
| BBB | Baa2 |
| B | NA |
| B | B2 |
| B | Na |
| AAA | Aaa |
| B | NA |
| NA | Aa3 |
| AA+ | Aa3 |
| AA- | Aa3 |
| BBB+ | Baa3 |
| B+ | NA |
| BB | Baa3 |
| BB+ | Ba1 |
| NA | Caa1 |
| A- | NA |
| B- | Caa3 |
| AA | A1 |
| B- | B3 |
| AAA | Aaa |
| B+ | B1 |
| B | Caa1 |
| B- | Caa1 |
| BB- | Ba3 |
| AA- | A1 |
| NA | B1 |
| AAA | Aaa |
| AA | Aa1 |
| BB- | NA |
| BB= | Ba3 |
| AAA | Aaa |
| B | B1 |
| B- | Caa3 |
| BB+ | Ba1 |
| B | B2 |
| AAA | Aa1 |
| BB | Ba1 |
| BBB- | Baa3 |
| BBB- | Baa3 |
| BB+ | Baa3 |
| BBB+ | Ba1 |
| AA+ | Aa1 |
| A+ | A1 |
| BBB | Baa2 |
| B- | Caa3 |
| AA- | Aa3 |
| BB- | B1 |
| BBB+ | Baa2 |
| B+ | B1 |
| AA- | Aa3 |
| AA | Aa2 |
| BBB+ | Baa2 |
| B- | B1 |
| AAA | NA |
| BBB | Baa1 |
| AAA | Aaa |
| NA | Aa3 |
| BB- | NA |
| A | A3 |
| BBB+ | A3 |
| NA | Baa1 |
| A | Baa1 |
| NA | B3 |
| BB- | B1 |
| BB- | Ba3 |
| BBB- | NA |
| BBB- | Ba1 |
| B+ | B1 |
| NA | Baa3 |
| AA+ | Aaa |
| AA+ | Aaa |
| NA | B3 |
| BB- | Ba3 |
| AAA | Aaa |
| A | A1 |
| B- | Caa1 |
| BBB | Baa2 |
| B+ | B1 |
| BB- | Ba3 |
| A- | Baa2 |
| BBB- | Baa3 |
| A | A2 |
| BB | Ba3 |
| AA | Aa2 |
| A | A2 |
| NA | Ba3 |
| BB+ | Baa3 |
| BBB+ | Baa1 |
| B | NA |
| AAA | Aa3 |
| B+ | B1 |
| BB- | B1 |
| AAA | Aaa |
| A | A2 |
| A- | Ba1 |
| A- | Baa1 |
| BBB- | Baa3 |
| B+ | B1 |
| NA | Baa1 |
| NA | B2 |
| BB- | Ba3 |
| AAA | Aaa |
| AAA | Aaa |
| AA- | Aa3 |
| A- | Baa1 |
| A | Baa1 |
| NA | Ba3 |
| BBB | Baa3 |
| B+ | NA |
| B+ | Caa1 |
| NA | Aa2 |
| AAA | Aa1 |
| AA+ | Aaa |
| BBB- | Baa3 |
| B- | Caa1 |
| BB- | B2 |
| B+ | B1 |
