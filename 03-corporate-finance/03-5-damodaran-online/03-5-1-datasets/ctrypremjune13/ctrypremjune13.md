---
title: "Ctrypremjune13"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJune13.xls
---

# Ctrypremjune13

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJune13.xls

Sheets: Explanation and FAQ, Country Lookup, ERPs by country, Regional Simple Averages, Regional Weighted Averages, Regional breakdown, Sovereign Ratings (Moody's), Regional lookup table, 10-year CDS Spreads, Equity vs Govt Bond volatility, Country GDP, Ratings lookup

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
| Country Risk Premium (simple) |
| Total Equity Risk Premium (simple) |
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

| Country | GDP | GDP Weight in region | Total Risk Premium | Weight * ERP | Country Risk Premium | Weight * CRP |
|---|---|---|---|---|---|---|
| Angola | 114.2 | 0.0823894379914869 | 0.11149999999999999 | 0.00918642233605079 | 0.05399999999999999 | 0.004449029651540292 |
| Benin | 7.6 | 0.005483009883846764 | 0.14 | 0.000767621383738547 | 0.0825 | 0.000452348315417358 |
| Botswana | 14.4 | 0.010388860832551763 | 0.07400000000000001 | 0.0007687757016088306 | 0.0165 | 0.0001714162037371041 |
| Burkina Faso | 10.4 | 0.00750306615684294 | 0.14 | 0.0010504292619580116 | 0.0825 | 0.0006190029579395426 |
| Cameroon | 25 | 0.018036216723180145 | 0.14 | 0.0025250703412452204 | 0.0825 | 0.0014879878796623621 |
| Cape Verde | 1.9 | 0.001370752470961691 | 0.125 | 0.00017134405887021136 | 0.0675 | 9.252579178991414e-05 |
| Egypt | 257.3 | 0.18562874251497005 | 0.1775 | 0.032949101796407185 | 0.12 | 0.022275449101796404 |
| Gabon | 18.7 | 0.013491090108938748 | 0.11149999999999999 | 0.0015042565471466702 | 0.05399999999999999 | 0.0007285188658826923 |
| Ghana | 40.7 | 0.029362960825337278 | 0.125 | 0.0036703701031671598 | 0.0675 | 0.0019819998557102664 |
| Kenya | 37.2 | 0.026837890484092058 | 0.125 | 0.0033547363105115072 | 0.0675 | 0.001811557607676214 |
| Morocco | 96.7 | 0.0697640862852608 | 0.09875 | 0.006889203520669505 | 0.04125 | 0.0028777685592670083 |
| Mozambique | 14.6 | 0.010533150566337204 | 0.125 | 0.0013166438207921505 | 0.0675 | 0.0007109876632277614 |
| Namibia | 12.8 | 0.009234542962268234 | 0.09125 | 0.0008426520453069763 | 0.03375 | 0.0003116658249765529 |
| Nigeria | 262.6 | 0.18945242046028424 | 0.11149999999999999 | 0.02112394488132169 | 0.05399999999999999 | 0.010230430704855348 |
| Rwanda | 7.1 | 0.00512228554938316 | 0.14 | 0.0007171199769136425 | 0.0825 | 0.00042258855782411074 |
| Senegal | 14.2 | 0.01024457109876632 | 0.125 | 0.00128057138734579 | 0.0675 | 0.0006915085491667267 |
| South Africa | 384.3 | 0.2772527234687252 | 0.083 | 0.023011976047904194 | 0.025500000000000002 | 0.007069944448452493 |
| Tunisia | 45.7 | 0.0329702041699733 | 0.10475000000000001 | 0.0034536288868047037 | 0.04725 | 0.0015578421470312386 |
| Zambia | 20.7 | 0.014933987446793159 | 0.125 | 0.0018667484308491449 | 0.0675 | 0.0010080441526585382 |
| Africa | 1386.1000000000001 | 1 |  | 0.11645061683861195 |  | 0.05895061683861193 |
| Bangladesh | 115.6 | 0.0057274506403745635 | 0.11149999999999999 | 0.0006386107464017638 | 0.05399999999999999 | 0.0003092823345802264 |
| Cambodia | 14.1 | 0.0006985904327792504 | 0.14 | 9.780266058909506e-05 | 0.0825 | 5.763371070428816e-05 |
| China | 8227.1 | 0.4076151311715015 | 0.0695 | 0.028329251616419356 | 0.012 | 0.004891381574058018 |
| Fiji | 3.9 | 0.0001932271409814948 | 0.125 | 2.415339262268685e-05 | 0.0675 | 1.3042832016250899e-05 |
| Hong Kong | 263.3 | 0.013045309287289123 | 0.062 | 0.0008088091758119256 | 0.0045000000000000005 | 5.870389179280106e-05 |
| India | 1841.7 | 0.09124780142195357 | 0.09125 | 0.008326361879753264 | 0.03375 | 0.0030796132979909333 |
| Indonesia | 878 | 0.04350087943121857 | 0.09125 | 0.003969455248098695 | 0.03375 | 0.0014681546808036267 |
| Japan | 5959.7 | 0.29527584413010627 | 0.0695 | 0.02052167116704239 | 0.012 | 0.0035433101295612754 |
| Korea | 1129.6 | 0.055966507295563205 | 0.0695 | 0.003889672257041643 | 0.012 | 0.0006715980875467585 |
| Macao | 43.6 | 0.0021601803453315826 | 0.0695 | 0.00015013253400054501 | 0.012 | 2.592216414397899e-05 |
| Malaysia | 303.5 | 0.015037035202021452 | 0.077 | 0.0011578517105556517 | 0.0195 | 0.0002932221864394183 |
| Mauritius | 10.5 | 0.0005202269180271013 | 0.083 | 4.317883419624941e-05 | 0.025500000000000002 | 1.3265786409691084e-05 |
| Mongolia | 10.3 | 0.0005103178338742042 | 0.125 | 6.378972923427553e-05 | 0.0675 | 3.4446453786508785e-05 |
| Pakistan | 231.2 | 0.011454901280749127 | 0.1775 | 0.00203324497733297 | 0.12 | 0.0013745881536898952 |
| Papua New Guinea | 15.7 | 0.0007778631060024277 | 0.125 | 9.723288825030346e-05 | 0.0675 | 5.250575965516387e-05 |
| Philippines | 250.3 | 0.012401218817350807 | 0.09875 | 0.0012246203582133922 | 0.04125 | 0.0005115502762157208 |
| Singapore | 274.7 | 0.01361012708400426 | 0.0575 | 0.000782582307330245 | 0 | 0 |
| Sri Lanka | 59.4 | 0.002942997993410459 | 0.125 | 0.0003678747491763074 | 0.0675 | 0.000198652364555206 |
| Taiwan | 44 | 0.0021799985136373773 | 0.0695 | 0.00015150989669779772 | 0.012 | 2.6159982163648528e-05 |
| Thailand | 365.6 | 0.018113805831496025 | 0.083 | 0.0015034458840141702 | 0.025500000000000002 | 0.00046190204870314865 |
| Vietnam | 141.7 | 0.007020586122327643 | 0.14 | 0.0009828820571258702 | 0.0825 | 0.0005791983550920306 |
| Asia | 20183.5 | 1 |  | 0.07516413406990861 |  | 0.017664134069908587 |
| Australia | 1520.6 | 0.9151420317766009 | 0.0575 | 0.05262066682715456 | 0 | 0 |
| Cook Islands | 1.2 | 0.0007221954742416948 | 0.125 | 9.027443428021185e-05 | 0.0675 | 4.87481945113144e-05 |
| New Zealand | 139.8 | 0.08413577274915746 | 0.0575 | 0.004837806933076554 | 0 | 0 |
| Australia & New Zealand | 1661.6 | 1 |  | 0.05754874819451132 |  | 4.87481945113144e-05 |
| Aruba | 2.6 | 0.013881473571809931 | 0.083 | 0.0011521623064602244 | 0.025500000000000002 | 0.00035397757608115327 |
| Bahamas | 8.1 | 0.04324612920448478 | 0.083 | 0.0035894287239722367 | 0.025500000000000002 | 0.0011027762947143618 |
| Barbados | 3.7 | 0.019754404698344902 | 0.09875 | 0.0019507474639615591 | 0.04125 | 0.0008148691938067273 |
| Bermuda | 5.6 | 0.029898558462359847 | 0.0695 | 0.0020779498131340097 | 0.012 | 0.00035878270154831817 |
| Cayman Islands | 4 | 0.02135611318739989 | 0.0575 | 0.0012279765082754937 | 0 | 0 |
| Cuba | 60.8 | 0.32461292044847834 | 0.1775 | 0.057618793379604905 | 0.12 | 0.0389535504538174 |
| Curacao | 1 | 0.0053390282968499726 | 0.125 | 0.0006673785371062466 | 0.0675 | 0.0003603844100373732 |
| Dominican Republic | 59 | 0.3150026695141484 | 0.125 | 0.03937533368926855 | 0.0675 | 0.02126268019220502 |
| Jamaica | 14.8 | 0.07901761879337961 | 0.2225 | 0.017581420181526964 | 0.165 | 0.013037907100907636 |
| Montserrat | 1.5 | 0.00800854244527496 | 0.09125 | 0.0007307794981313401 | 0.03375 | 0.0002702883075280299 |
| St. Maarten | 1.5 | 0.00800854244527496 | 0.083 | 0.0006647090229578217 | 0.025500000000000002 | 0.0002042178323545115 |
| St. Vincent & the Grenadines | 0.7 | 0.003737319807794981 | 0.14 | 0.0005232247730912973 | 0.0825 | 0.0003083288841430859 |
| Trinidad and Tobago | 24 | 0.12813667912439936 | 0.083 | 0.010635344367325147 | 0.025500000000000002 | 0.003267485317672184 |
| Caribbean | 187.3 | 1 |  | 0.13779524826481582 |  | 0.08029524826481578 |
| Argentina | 474.9 | 0.08635801571137619 | 0.15875 | 0.01370933499418097 | 0.10125 | 0.00874374909077684 |
| Belize | 1.4 | 0.0002545824847250509 | 0.2 | 5.091649694501018e-05 | 0.14250000000000002 | 3.627800407331975e-05 |
| Bolivia | 27 | 0.004909805062554552 | 0.11149999999999999 | 0.0005474432644748325 | 0.05399999999999999 | 0.0002651294733779458 |
| Brazil | 2252.7 | 0.4096414023858015 | 0.0875 | 0.03584362270875763 | 0.03 | 0.012289242071574044 |
| Chile | 268.3 | 0.04878891475123654 | 0.0695 | 0.00339082957521094 | 0.012 | 0.0005854669770148385 |
| Colombia | 369.8 | 0.06724614489380273 | 0.09125 | 0.006136210721559499 | 0.03375 | 0.0022695573901658425 |
| Costa Rica | 45.1 | 0.008201192900785567 | 0.09125 | 0.000748358852196683 | 0.03375 | 0.0002767902604015129 |
| Ecuador | 84.5 | 0.015365871399476285 | 0.1775 | 0.0027274421734070405 | 0.12 | 0.001843904567937154 |
| El Salvador | 23.8 | 0.004327902240325865 | 0.11149999999999999 | 0.0004825610997963339 | 0.05399999999999999 | 0.00023370672097759666 |
| Guatemala | 50.8 | 0.009237707302880416 | 0.09875 | 0.0009122235961594411 | 0.04125 | 0.0003810554262438172 |
| Honduras | 18 | 0.0032732033750363684 | 0.14 | 0.0004582484725050916 | 0.0825 | 0.0002700392784405004 |
| Mexico | 1177.3 | 0.21408568519057314 | 0.083 | 0.01776911187081757 | 0.025500000000000002 | 0.005459184972359615 |
| Nicaragua | 10.5 | 0.0019093686354378816 | 0.15875 | 0.00030311227087576374 | 0.10125 | 0.00019332357433808552 |
| Panama | 36.3 | 0.006600960139656676 | 0.0875 | 0.0005775840122199591 | 0.03 | 0.0001980288041897003 |
| Paraguay | 25.5 | 0.004637038114634855 | 0.11149999999999999 | 0.0005170297497817863 | 0.05399999999999999 | 0.00025040005819028214 |
| Peru | 197.1 | 0.03584157695664823 | 0.0875 | 0.00313613798370672 | 0.03 | 0.001075247308699447 |
| Suriname | 4.7 | 0.0008546697701483851 | 0.11149999999999999 | 9.529567937154493e-05 | 0.05399999999999999 | 4.615216758801279e-05 |
| Uruguay | 49.1 | 0.008928571428571428 | 0.09125 | 0.0008147321428571428 | 0.03375 | 0.0003013392857142857 |
| Venezuela | 382.4 | 0.06953738725632817 | 0.125 | 0.008692173407041022 | 0.0675 | 0.004693773639802152 |
| Central and South America | 5499.200000000001 | 1 |  | 0.09691236907186497 |  | 0.03941236907186499 |
| Albania | 13.1 | 0.0032841134147258643 | 0.125 | 0.00041051417684073304 | 0.0675 | 0.00022167765549399585 |
| Armenia | 9.9 | 0.0024818872370829053 | 0.10475000000000001 | 0.00025997768808443437 | 0.04725 | 0.00011726917195216727 |
| Azerbaijan | 67.2 | 0.016846749730502143 | 0.09125 | 0.0015372659129083205 | 0.03375 | 0.0005685778034044474 |
| Belarus | 63.3 | 0.015869036576499785 | 0.15875 | 0.0025192095565193407 | 0.10125 | 0.0016067399533706034 |
| Bosnia and Herzegovina | 17 | 0.004261826568728221 | 0.15875 | 0.0006765649677856051 | 0.10125 | 0.0004315099400837324 |
| Bulgaria | 51 | 0.012785479706184662 | 0.0875 | 0.0011187294742911577 | 0.03 | 0.00038356439118553983 |
| Croatia | 56.4 | 0.014139236380957156 | 0.09875 | 0.0013962495926195192 | 0.04125 | 0.0005832435007144827 |
| Czech Republic | 195.7 | 0.04906114467647722 | 0.07175000000000001 | 0.003520137130537241 | 0.014249999999999999 | 0.0006991213116398004 |
| Estonia | 21.9 | 0.005490235403244002 | 0.07175000000000001 | 0.0003939243901827572 | 0.014249999999999999 | 7.823585449622702e-05 |
| Georgia | 15.8 | 0.003960991752112111 | 0.11149999999999999 | 0.0004416505803605003 | 0.05399999999999999 | 0.00021389355461405395 |
| Hungary | 125.5 | 0.03146230790443481 | 0.09875 | 0.0031069029055629375 | 0.04125 | 0.0012978202010579358 |
| Kazakhstan | 201.7 | 0.05056531875955777 | 0.0875 | 0.004424465391461304 | 0.03 | 0.001516959562786733 |
| Latvia | 28.4 | 0.007119757326581263 | 0.0875 | 0.0006229787660758605 | 0.03 | 0.00021359271979743788 |
| Lithuania | 42.2 | 0.010579357717666524 | 0.083 | 0.0008780866905663216 | 0.025500000000000002 | 0.0002697736218004964 |
| Macedonia | 9.7 | 0.00243174810098022 | 0.11149999999999999 | 0.0002711399132592945 | 0.05399999999999999 | 0.00013131439745293186 |
| Moldova | 7.3 | 0.0018300784677480007 | 0.15875 | 0.0002905249567549951 | 0.10125 | 0.00018529544485948509 |
| Montenegro | 4.2 | 0.001052921858156384 | 0.11149999999999999 | 0.0001174007871844368 | 0.05399999999999999 | 5.685778034044472e-05 |
| Poland | 489.8 | 0.12279074431547544 | 0.07400000000000001 | 0.009086515079345185 | 0.0165 | 0.002026047281205345 |
| Romania | 169.4 | 0.04246784827897415 | 0.09125 | 0.0038751911554563913 | 0.03375 | 0.0014332898794153777 |
| Russia | 2014.8 | 0.5051016570984481 | 0.083 | 0.041923437539171195 | 0.025500000000000002 | 0.012880092256010427 |
| Serbia | 37.5 | 0.009401088019253429 | 0.11149999999999999 | 0.0010482213141467572 | 0.05399999999999999 | 0.0005076587530396851 |
| Slovakia | 91.6 | 0.022963724335029707 | 0.07400000000000001 | 0.0016993156007921986 | 0.0165 | 0.0003789014515279902 |
| Slovenia | 45.5 | 0.011406653463360826 | 0.09875 | 0.0011264070295068816 | 0.04125 | 0.0004705244553636341 |
| Uganda | 33.7 | 0.008448444433302414 | 0.125 | 0.0010560555541628018 | 0.0675 | 0.000570269999247913 |
| Ukraine | 176.3 | 0.044197648474516786 | 0.15875 | 0.00701637669532954 | 0.10125 | 0.004475011908044825 |
| Eastern Europe & Russia | 3988.9 | 1 |  | 0.0888172428489057 |  | 0.03131724284890571 |
| Bahrain | 22.9 | 0.013484072307601718 | 0.083 | 0.0011191780015309427 | 0.025500000000000002 | 0.00034384384384384385 |
| Israel | 242.9 | 0.14302537831949597 | 0.07175000000000001 | 0.010262070894423837 | 0.014249999999999999 | 0.002038111641052817 |
| Jordan | 31.2 | 0.018371312488959547 | 0.125 | 0.0022964140611199434 | 0.0675 | 0.0012400635930047694 |
| Kuwait | 176.6 | 0.10398633928045693 | 0.0665 | 0.006915091562150386 | 0.009000000000000001 | 0.0009358770535241125 |
| Lebanon | 42.9 | 0.02526055467231938 | 0.125 | 0.0031575693340399223 | 0.0675 | 0.0017050874403815581 |
| Oman | 71.8 | 0.04227757168933639 | 0.07175000000000001 | 0.003033415768709887 | 0.014249999999999999 | 0.0006024553965730435 |
| Qatar | 173 | 0.10186657245480775 | 0.0665 | 0.006774127068244716 | 0.009000000000000001 | 0.0009167991520932699 |
| Saudi Arabia | 576.8 | 0.33963375139845725 | 0.0695 | 0.023604545722192782 | 0.012 | 0.004075605016781487 |
| United Arab Emirates | 360.2 | 0.21209444738856503 | 0.0665 | 0.014104280751339576 | 0.009000000000000001 | 0.0019088500264970855 |
| Middle East | 1698.3 | 1 |  | 0.07126669316375199 |  | 0.013766693163751988 |
| Canada | 1821.4 | 0.10404313900218208 | 0.0575 | 0.00598248049262547 | 0 | 0 |
| United States of America | 15684.8 | 0.8959568609978178 | 0.0575 | 0.05151751950737452 | 0 | 0 |
| North America | 17506.2 | 1 |  | 0.057499999999999996 |  | 0 |
| Andorra | 4.5 | 0.00026060065555542683 | 0.077 | 2.0066250477767864e-05 | 0.0195 | 5.081712783330823e-06 |
| Austria | 399.6 | 0.023141338213321903 | 0.0575 | 0.0013306269472660095 | 0 | 0 |
| Belgium | 483.7 | 0.02801167490936888 | 0.0695 | 0.0019468114062011373 | 0.012 | 0.00033614009891242655 |
| Cyprus | 23 | 0.0013319589061721816 | 0.2225 | 0.00029636085662331044 | 0.165 | 0.00021977321951840997 |
| Denmark | 314.2 | 0.0181957168834478 | 0.0575 | 0.0010462537207982486 | 0 | 0 |
| Finland | 250 | 0.014477814197523713 | 0.0575 | 0.0008324743163576135 | 0 | 0 |
| France | 2612.9 | 0.15131632286683883 | 0.062 | 0.009381612017744007 | 0.0045000000000000005 | 0.0006809234529007748 |
| Germany | 3399.6 | 0.19687510858360643 | 0.0575 | 0.011320318743557371 | 0 | 0 |
| Greece | 249.1 | 0.014425694066412626 | 0.15875 | 0.0022900789330430045 | 0.10125 | 0.0014606015242242785 |
| Iceland | 13.7 | 0.0007933842180242994 | 0.09125 | 7.239630989471733e-05 | 0.03375 | 2.6776717358320108e-05 |
| Ireland | 210.3 | 0.012178737302956948 | 0.09875 | 0.0012026503086669986 | 0.04125 | 0.0005023729137469741 |
| Isle of Man | 1.4 | 8.107575950613278e-05 | 0.0575 | 4.661856171602635e-06 | 0 | 0 |
| Italy | 2013.3 | 0.11659273329549796 | 0.0875 | 0.010201864163356071 | 0.03 | 0.003497781998864939 |
| Liechtenstein | 10.5 | 0.0006080681962959959 | 0.0575 | 3.496392128701977e-05 | 0 | 0 |
| Luxembourg | 57.1 | 0.003306732762714416 | 0.0575 | 0.00019013713385607894 | 0 | 0 |
| Malta | 8.7 | 0.0005038279340738251 | 0.077 | 3.879475092368453e-05 | 0.0195 | 9.82464471443959e-06 |
| Netherlands | 772.2 | 0.044719072493311245 | 0.0575 | 0.002571346668365397 | 0 | 0 |
| Norway | 499.7 | 0.028938255018010395 | 0.0575 | 0.0016639496635355978 | 0 | 0 |
| Portugal | 212.5 | 0.012306142067895156 | 0.11149999999999999 | 0.0013721348405703097 | 0.05399999999999999 | 0.0006645316716663383 |
| Spain | 1349.4 | 0.078145449912554 | 0.09125 | 0.007130772304520552 | 0.03375 | 0.0026374089345486975 |
| Sweden | 525.7 | 0.030443947694552866 | 0.0575 | 0.00175052699243679 | 0 | 0 |
| Switzerland | 632.2 | 0.03661149654269796 | 0.0575 | 0.002105161051205133 | 0 | 0 |
| Turkey | 789.3 | 0.045709354984421864 | 0.09125 | 0.004170978642328495 | 0.03375 | 0.001542690730724238 |
| United Kingdom | 2435.2 | 0.14102549253523897 | 0.062 | 0.008743580537184817 | 0.0045000000000000005 | 0.0006346147164085754 |
| Western Europe | 17267.800000000003 | 1 |  | 0.06971852233637174 |  | 0.01221852233637174 |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Region | Total ERP | CRP |  |  |  |  |
| Africa | 0.11645061683861195 | 0.05895061683861193 |  |  |  |  |
| Asia | 0.07516413406990861 | 0.017664134069908587 |  |  |  |  |
| Australia & New Zealand | 0.05754874819451132 | 4.87481945113144e-05 |  |  |  |  |
| Caribbean | 0.13779524826481582 | 0.08029524826481578 |  |  |  |  |
| Central and South America | 0.09691236907186497 | 0.03941236907186499 |  |  |  |  |
| Eastern Europe & Russia | 0.0888172428489057 | 0.03131724284890571 |  |  |  |  |
| Middle East | 0.07126669316375199 | 0.013766693163751988 |  |  |  |  |
| North America | 0.057499999999999996 | 0 |  |  |  |  |
| Western Europe | 0.06971852233637174 | 0.01221852233637174 |  |  |  |  |

## Regional breakdown

| Country | GDP | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|
| Angola | 114.197 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Benin | 7.557 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Botswana | 14.411 | A2 | 0.011 | 0.07400000000000001 | 0.0165 | Africa |
| Burkina Faso | 10.441 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Cameroon | 24.984 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Cape Verde | 1.897 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Egypt | 257.286 | Caa1 | 0.08 | 0.1775 | 0.12 | Africa |
| Gabon | 18.661 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Ghana | 40.71 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Kenya | 37.229 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Morocco | 96.729 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Africa |
| Mozambique | 14.588 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Namibia | 12.807 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Africa |
| Nigeria | 262.606 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Rwanda | 7.103 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Senegal | 14.16 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| South Africa | 384.313 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Africa |
| Tunisia | 45.662 | Ba2 | 0.0315 | 0.10475000000000001 | 0.04725 | Africa |
| Zambia | 20.678 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Bangladesh | 115.61 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Asia |
| Cambodia | 14.062 | B2 | 0.055 | 0.14 | 0.0825 | Asia |
| China | 8227.103 | Aa3 | 0.008 | 0.0695 | 0.012 | Asia |
| Fiji | 3.882 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Hong Kong | 263.259 | Aa1 | 0.003 | 0.062 | 0.0045000000000000005 | Asia |
| India | 1841.717 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Asia |
| Indonesia | 878.043 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Asia |
| Japan | 5959.718 | Aa3 | 0.008 | 0.0695 | 0.012 | Asia |
| Korea | 1129.598 | Aa3 | 0.008 | 0.0695 | 0.012 | Asia |
| Macao | 43.582 | Aa3 | 0.008 | 0.0695 | 0.012 | Asia |
| Malaysia | 303.526 | A3 | 0.013 | 0.077 | 0.0195 | Asia |
| Mauritius | 10.492 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Asia |
| Mongolia | 10.271 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Pakistan | 231.182 | Caa1 | 0.08 | 0.1775 | 0.12 | Asia |
| Papua New Guinea | 15.654 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Philippines | 250.265 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Asia |
| Singapore | 274.701 | Aaa | 0 | 0.0575 | 0 | Asia |
| Sri Lanka | 59.421 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Taiwan | 44.02 | Aa3 | 0.008 | 0.0695 | 0.012 | Asia |
| Thailand | 365.564 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Asia |
| Vietnam | 141.669 | B2 | 0.055 | 0.14 | 0.0825 | Asia |
| Australia | 1520.608 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand |
| Cook Islands | 1.2 | B1 | 0.045 | 0.125 | 0.0675 | Australia & New Zealand |
| New Zealand | 139.768 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand |
| Aruba | 2.584 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Caribbean |
| Bahamas | 8.149 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Caribbean |
| Barbados | 3.685 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Caribbean |
| Bermuda | 5.557 | Aa3 | 0.008 | 0.0695 | 0.012 | Caribbean |
| Cayman Islands | 4 | Aaa | 0 | 0.0575 | 0 | Caribbean |
| Cuba | 60.8 | Caa1 | 0.08 | 0.1775 | 0.12 | Caribbean |
| Curacao | 1 | B1 | 0.045 | 0.125 | 0.0675 | Caribbean |
| Dominican Republic | 58.951 | B1 | 0.045 | 0.125 | 0.0675 | Caribbean |
| Jamaica | 14.84 | Caa3 | 0.11 | 0.2225 | 0.165 | Caribbean |
| Montserrat | 1.5 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Caribbean |
| St. Maarten | 1.5 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Caribbean |
| St. Vincent & the Grenadines | 0.713 | B2 | 0.055 | 0.14 | 0.0825 | Caribbean |
| Trinidad and Tobago | 23.986 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Caribbean |
| Argentina | 474.865 | B3 | 0.0675 | 0.15875 | 0.10125 | Central and South America |
| Belize | 1.448 | Caa2 | 0.095 | 0.2 | 0.14250000000000002 | Central and South America |
| Bolivia | 27.035 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Brazil | 2252.664 | Baa2 | 0.02 | 0.0875 | 0.03 | Central and South America |
| Chile | 268.314 | Aa3 | 0.008 | 0.0695 | 0.012 | Central and South America |
| Colombia | 369.813 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Central and South America |
| Costa Rica | 45.127 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Central and South America |
| Ecuador | 84.532 | Caa1 | 0.08 | 0.1775 | 0.12 | Central and South America |
| El Salvador | 23.787 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Guatemala | 50.806 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Central and South America |
| Honduras | 17.967 | B2 | 0.055 | 0.14 | 0.0825 | Central and South America |
| Mexico | 1177.271 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Central and South America |
| Nicaragua | 10.507 | B3 | 0.0675 | 0.15875 | 0.10125 | Central and South America |
| Panama | 36.253 | Baa2 | 0.02 | 0.0875 | 0.03 | Central and South America |
| Paraguay | 25.502 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Peru | 197.111 | Baa2 | 0.02 | 0.0875 | 0.03 | Central and South America |
| Suriname | 4.738 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Uruguay | 49.06 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Central and South America |
| Venezuela | 382.424 | B1 | 0.045 | 0.125 | 0.0675 | Central and South America |
| Albania | 13.119 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia |
| Armenia | 9.91 | Ba2 | 0.0315 | 0.10475000000000001 | 0.04725 | Eastern Europe & Russia |
| Azerbaijan | 67.198 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Eastern Europe & Russia |
| Belarus | 63.267 | B3 | 0.0675 | 0.15875 | 0.10125 | Eastern Europe & Russia |
| Bosnia and Herzegovina | 17.048 | B3 | 0.0675 | 0.15875 | 0.10125 | Eastern Europe & Russia |
| Bulgaria | 51.03 | Baa2 | 0.02 | 0.0875 | 0.03 | Eastern Europe & Russia |
| Croatia | 56.442 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Eastern Europe & Russia |
| Czech Republic | 195.657 | A1 | 0.0095 | 0.07175000000000001 | 0.014249999999999999 | Eastern Europe & Russia |
| Estonia | 21.854 | A1 | 0.0095 | 0.07175000000000001 | 0.014249999999999999 | Eastern Europe & Russia |
| Georgia | 15.829 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Hungary | 125.508 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Eastern Europe & Russia |
| Kazakhstan | 201.68 | Baa2 | 0.02 | 0.0875 | 0.03 | Eastern Europe & Russia |
| Latvia | 28.374 | Baa2 | 0.02 | 0.0875 | 0.03 | Eastern Europe & Russia |
| Lithuania | 42.246 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Eastern Europe & Russia |
| Macedonia | 9.663 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Moldova | 7.254 | B3 | 0.0675 | 0.15875 | 0.10125 | Eastern Europe & Russia |
| Montenegro | 4.231 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Poland | 489.795 | A2 | 0.011 | 0.07400000000000001 | 0.0165 | Eastern Europe & Russia |
| Romania | 169.396 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Eastern Europe & Russia |
| Russia | 2014.775 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Eastern Europe & Russia |
| Serbia | 37.489 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Slovakia | 91.619 | A2 | 0.011 | 0.07400000000000001 | 0.0165 | Eastern Europe & Russia |
| Slovenia | 45.469 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Eastern Europe & Russia |
| Uganda | 33.679 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia |
| Ukraine | 176.309 | B3 | 0.0675 | 0.15875 | 0.10125 | Eastern Europe & Russia |
| Bahrain | 22.945 | Baa1 | 0.017 | 0.083 | 0.025500000000000002 | Middle East |
| Israel | 242.929 | A1 | 0.0095 | 0.07175000000000001 | 0.014249999999999999 | Middle East |
| Jordan | 31.243 | B1 | 0.045 | 0.125 | 0.0675 | Middle East |
| Kuwait | 176.59 | Aa2 | 0.006 | 0.0665 | 0.009000000000000001 | Middle East |
| Lebanon | 42.945 | B1 | 0.045 | 0.125 | 0.0675 | Middle East |
| Oman | 71.782 | A1 | 0.0095 | 0.07175000000000001 | 0.014249999999999999 | Middle East |
| Qatar | 172.982 | Aa2 | 0.006 | 0.0665 | 0.009000000000000001 | Middle East |
| Saudi Arabia | 576.824 | Aa3 | 0.008 | 0.0695 | 0.012 | Middle East |
| United Arab Emirates | 360.245 | Aa2 | 0.006 | 0.0665 | 0.009000000000000001 | Middle East |
| Canada | 1821.424 | Aaa | 0 | 0.0575 | 0 | North America |
| United States of America | 15684.8 | Aaa | 0 | 0.0575 | 0 | North America |
| Andorra | 4.5 | A3 | 0.013 | 0.077 | 0.0195 | Western Europe |
| Austria | 399.649 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Belgium | 483.709 | Aa3 | 0.008 | 0.0695 | 0.012 | Western Europe |
| Cyprus | 22.981 | Caa3 | 0.11 | 0.2225 | 0.165 | Western Europe |
| Denmark | 314.242 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Finland | 250.024 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| France | 2612.878 | Aa1 | 0.003 | 0.062 | 0.0045000000000000005 | Western Europe |
| Germany | 3399.589 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Greece | 249.099 | B3 | 0.0675 | 0.15875 | 0.10125 | Western Europe |
| Iceland | 13.657 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Western Europe |
| Ireland | 210.331 | Ba1 | 0.0275 | 0.09875 | 0.04125 | Western Europe |
| Isle of Man | 1.4 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Italy | 2013.263 | Baa2 | 0.02 | 0.0875 | 0.03 | Western Europe |
| Liechtenstein | 10.5 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Luxembourg | 57.117 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Malta | 8.722 | A3 | 0.013 | 0.077 | 0.0195 | Western Europe |
| Netherlands | 772.227 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Norway | 499.667 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Portugal | 212.454 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Western Europe |
| Spain | 1349.351 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Western Europe |
| Sweden | 525.742 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Switzerland | 632.194 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Turkey | 789.257 | Baa3 | 0.0225 | 0.09125 | 0.03375 | Western Europe |
| United Kingdom | 2435.174 | Aa1 | 0.003 | 0.062 | 0.0045000000000000005 | Western Europe |

## Sovereign Ratings (Moody's)

| Country | S&P local currency | Moody's local currency |
|---|---|---|
| Albania | B+ | B1 |
| Andorra | A- | A3 |
| Angola | BB- | Ba3 |
| Argentina | B- | B3 |
| Armenia | NA | Ba2 |
| Aruba | BBB+ | Baa1 |
| Australia | AAA | Aaa |
| Austria | AA+ | Aaa |
| Azerbaijan | BBB- | Baa3 |
| Bahamas | BBB | Baa1 |
| Bahrain | BBB | Baa1 |
| Bangladesh | BB- | Ba3 |
| Barbados | NA | Ba1 |
| Belarus | B- | B3 |
| Belgium | AA | Aa3 |
| Belize | B- | Caa2 |
| Benin | B | B2 |
| Bermuda | AA- | Aa3 |
| Bolivia | BB- | Ba3 |
| Bosnia and Herzegovina | B | B3 |
| Botswana | A- | A2 |
| Brazil | A- | Baa2 |
| Bulgaria | BBB | Baa2 |
| Burkina Faso | B | B2 |
| Cambodia | B | B2 |
| Cameroon | B | B2 |
| Canada | AAA | Aaa |
| Cape Verde | B+ | B1 |
| Cayman Islands | NA | Aaa |
| Chile | AA+ | Aa3 |
| China | AA- | Aa3 |
| Colombia | BBB+ | Baa3 |
| Cook Islands | B+ | B1 |
| Costa Rica | BB | Baa3 |
| Croatia | BB+ | Ba1 |
| Cuba | NA | Caa1 |
| Curacao | A- | B1 |
| Cyprus | CCC+ | Caa3 |
| Czech Republic | AA | A1 |
| Denmark | AAA | Aaa |
| Dominican Republic | B+ | B1 |
| Ecuador | B | Caa1 |
| Egypt | CCC+ | Caa1 |
| El Salvador | BB- | Ba3 |
| Estonia | AA- | A1 |
| Fiji | B | B1 |
| Finland | AAA | Aaa |
| France | AA+ | Aa1 |
| Gabon | BB- | Ba3 |
| Georgia | BB- | Ba3 |
| Germany | AAA | Aaa |
| Ghana | B | B1 |
| Greece | B- | B3 |
| Guatemala | BB+ | Ba1 |
| Honduras | B+ | B2 |
| Hong Kong | AAA | Aa1 |
| Hungary | BB | Ba1 |
| Iceland | BBB- | Baa3 |
| India | BBB- | Baa3 |
| Indonesia | BB+ | Baa3 |
| Ireland | BBB+ | Ba1 |
| Isle of Man | AA+ | Aaa |
| Israel | A+ | A1 |
| Italy | BBB+ | Baa2 |
| Jamaica | CCC+ | Caa3 |
| Japan | AA- | Aa3 |
| Jordan | BB- | B1 |
| Kazakhstan | BBB+ | Baa2 |
| Kenya | B+ | B1 |
| Korea | AA- | Aa3 |
| Kuwait | AA | Aa2 |
| Latvia | BBB+ | Baa2 |
| Lebanon | B | B1 |
| Liechtenstein | AAA | Aaa |
| Lithuania | BBB | Baa1 |
| Luxembourg | AAA | Aaa |
| Macao | NA | Aa3 |
| Macedonia | BB- | Ba3 |
| Malaysia | A | A3 |
| Malta | BBB+ | A3 |
| Mauritius | NA | Baa1 |
| Mexico | A- | Baa1 |
| Moldova | NA | B3 |
| Mongolia | BB- | B1 |
| Montenegro | BB- | Ba3 |
| Montserrat | BBB- | Baa3 |
| Morocco | BBB | Ba1 |
| Mozambique | B+ | B1 |
| Namibia | NA | Baa3 |
| Netherlands | AAA | Aaa |
| New Zealand | AA+ | Aaa |
| Nicaragua | NA | B3 |
| Nigeria | BB- | Ba3 |
| Norway | AAA | Aaa |
| Oman | A | A1 |
| Pakistan | B- | Caa1 |
| Panama | BBB | Baa2 |
| Papua New Guinea | B+ | B1 |
| Paraguay | BB- | Ba3 |
| Peru | BBB | Baa2 |
| Philippines | BBB- | Ba1 |
| Poland | A- | A2 |
| Portugal | BB | Ba3 |
| Qatar | AA | Aa2 |
| Romania | BB+ | Baa3 |
| Russia | BBB+ | Baa1 |
| Rwanda | B | B2 |
| Saudi Arabia | AA- | Aa3 |
| Senegal | B+ | B1 |
| Serbia | BB- | Ba3 |
| Singapore | AAA | Aaa |
| Slovakia | A | A2 |
| Slovenia | A- | Ba1 |
| South Africa | A- | Baa1 |
| Spain | BBB- | Baa3 |
| Sri Lanka | B+ | B1 |
| St. Maarten | NA | Baa1 |
| St. Vincent & the Grenadines | NA | B2 |
| Suriname | BB- | Ba3 |
| Sweden | AAA | Aaa |
| Switzerland | AAA | Aaa |
| Taiwan | AA- | Aa3 |
| Thailand | A- | Baa1 |
| Trinidad and Tobago | A | Baa1 |
| Tunisia | BB- | Ba2 |
| Turkey | BBB | Baa3 |
| Uganda | B+ | B1 |
| Ukraine | B | B3 |
| United Arab Emirates | NA | Aa2 |
| United Kingdom | AAA | Aa1 |
| United States of America | AA+ | Aaa |
| Uruguay | BBB- | Baa3 |
| Venezuela | B | B1 |
| Vietnam | BB- | B2 |
| Zambia | NA | B1 |

## Regional lookup table

| Country | Region |
|---|---|
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
| Ukraine | Eastern Europe & Russia |
| United Arab Emirates | Middle East |
| United Kingdom | Western Europe |
| United States of America | North America |
| Uruguay | Central and South America |
| Venezuela | Central and South America |
| Vietnam | Asia |
| Zambia | Africa |

## 10-year CDS Spreads

| Country | Moody's local currency | 10-year CDS |
|---|---|---|
| Albania | B1 | NA |
| Andorra | A3 | NA |
| Angola | Ba3 | NA |
| Argentina | B3 | 0.284 |
| Armenia | Ba2 | NA |
| Aruba | Baa1 | NA |
| Australia | Aaa | 0.0085 |
| Austria | Aaa | 0.0076 |
| Azerbaijan | Baa3 | NA |
| Bahamas | Baa1 | NA |
| Bahrain | Baa1 | 0.0236 |
| Bangladesh | Ba3 | NA |
| Barbados | Ba1 | NA |
| Belarus | B3 | NA |
| Belgium | Aa3 | 0.0122 |
| Belize | Caa2 | NA |
| Benin | B2 | NA |
| Bermuda | Aa3 | NA |
| Bolivia | Ba3 | NA |
| Bosnia and Herzegovina | B3 | NA |
| Botswana | A2 | NA |
| Brazil | Baa2 | 0.025 |
| Bulgaria | Baa2 | 0.0176 |
| Burkina Faso | B2 | NA |
| Cambodia | B2 | NA |
| Cameroon | B2 | NA |
| Canada | Aaa | NA |
| Cape Verde | B1 | NA |
| Cayman Islands | Aaa | NA |
| Chile | Aa3 | 0.0136 |
| China | Aa3 | 0.0177 |
| Colombia | Baa3 | 0.0194 |
| Cook Islands | B1 | NA |
| Costa Rica | Baa3 | 0.0292 |
| Croatia | Ba1 | 0.0374 |
| Cuba | Caa1 | NA |
| Curacao | B1 | NA |
| Cyprus | Caa3 | NA |
| Czech Republic | A1 | 0.0094 |
| Denmark | Aaa | 0.0066 |
| Dominican Republic | B1 | NA |
| Ecuador | Caa1 | NA |
| Egypt | Caa1 | NA |
| El Salvador | Ba3 | NA |
| Estonia | A1 | 0.0094 |
| Fiji | B1 | NA |
| Finland | Aaa | 0.0052 |
| France | Aa1 | 0.0137 |
| Gabon | Ba3 | NA |
| Georgia | Ba3 | NA |
| Germany | Aaa | 0.0069 |
| Ghana | B1 | NA |
| Greece | C | NA |
| Guatemala | Ba1 | NA |
| Honduras | B2 | NA |
| Hong Kong | Aa1 | 0.0115 |
| Hungary | Ba1 | 0.0348 |
| Iceland | Baa3 | 0.02 |
| India | Baa3 | NA |
| Indonesia | Baa3 | 0.0297 |
| Ireland | Ba1 | 0.022 |
| Isle of Man | Aaa | NA |
| Israel | A1 | 0.0162 |
| Italy | Baa2 | 0.0329 |
| Jamaica | Caa3 | NA |
| Japan | Aa3 | 0.0129 |
| Jordan | B1 | NA |
| Kazakhstan | Baa2 | 0.0248 |
| Kenya | B1 | NA |
| Korea | Aa3 | 0.0129 |
| Kuwait | Aa2 | NA |
| Latvia | Baa2 | 0.0195 |
| Lebanon | B1 | 0.0564 |
| Liechtenstein | Aaa | NA |
| Lithuania | Baa1 | 0.0199 |
| Luxembourg | Aaa | NA |
| Macao | Aa3 | NA |
| Macedonia | Ba3 | NA |
| Malaysia | A3 | 0.0178 |
| Malta | A3 | NA |
| Mauritius | Baa1 | NA |
| Mexico | Baa1 | 0.0183 |
| Moldova | B3 | NA |
| Mongolia | B1 | NA |
| Montenegro | Ba3 | NA |
| Montserrat | Baa3 | NA |
| Morocco | Ba1 | 0.0323 |
| Mozambique | B1 | NA |
| Namibia | Baa3 | NA |
| Netherlands | Aaa | 0.0095 |
| New Zealand | Aaa | 0.0066 |
| Nicaragua | B3 | NA |
| Nigeria | Ba3 | NA |
| Norway | Aaa | 0.0037 |
| Oman | A1 | NA |
| Pakistan | Caa1 | NA |
| Panama | Baa2 | 0.0199 |
| Papua New Guinea | B1 | NA |
| Paraguay | Ba3 | NA |
| Peru | Baa2 | 0.0198 |
| Philippines | Ba1 | 0.0196 |
| Poland | A2 | 0.0149 |
| Portugal | Ba3 | 0.0532 |
| Qatar | Aa2 | 0.0126 |
| Romania | Baa3 | 0.0261 |
| Russia | Baa1 | 0.0246 |
| Rwanda | B2 | NA |
| Saudi Arabia | Aa3 | 0.0109 |
| Senegal | B1 | NA |
| Serbia | Ba3 | NA |
| Singapore | Aaa | NA |
| Slovakia | A2 | 0.0145 |
| Slovenia | Ba1 | 0.0367 |
| South Africa | Baa1 | 0.0291 |
| Spain | Baa3 | 0.033 |
| Sri Lanka | B1 | NA |
| St. Maarten | Baa1 | NA |
| St. Vincent & the Grenadines | B2 | NA |
| Suriname | Ba3 | NA |
| Sweden | Aaa | 0.0048 |
| Switzerland | Aaa | 0.0054 |
| Taiwan | Aa3 | NA |
| Thailand | Baa1 | 0.0173 |
| Trinidad and Tobago | Baa1 | NA |
| Tunisia | Ba2 | 0.0513 |
| Turkey | Baa3 | 0.0244 |
| Uganda | B1 | NA |
| Ukraine | B3 | 0.0843 |
| United Arab Emirates | Aa2 | 0.0291 |
| United Kingdom | Aa1 | 0.0082 |
| United States of America | Aaa | 0.005 |
| Uruguay | Baa3 | NA |
| Venezuela | B1 | 0.1008 |
| Vietnam | B2 | 0.0325 |
| Zambia | B1 | NA |

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

## Ratings lookup

| Country | S&P local currency | Moody's local currency |
|---|---|---|
| Albania | B+ | B1 |
| Andorra | A- | NA |
| Angola | BB- | Ba3 |
| Argentina | B- | B3 |
| Armenia | NA | Ba2 |
| Aruba | BBB+ | NA |
| Australia | AAA | Aaa |
| Austria | AA+ | Aaa |
| Azerbaijan | BBB- | Baa3 |
| Bahamas | BBB | Baa1 |
| Bahrain | BBB | Baa1 |
| Bangladesh | BB- | Ba3 |
| Barbados | NA | Ba1 |
| Belarus | B- | B3 |
| Belgium | AA | Aa3 |
| Belize | B- | Caa2 |
| Benin | B | NA |
| Bermuda | AA- | Aa3 |
| Bolivia | BB- | Ba3 |
| Bosnia and Herzegovina | B | B3 |
| Botswana | A- | A2 |
| Brazil | A- | Baa2 |
| Bulgaria | BBB | Baa2 |
| Burkina Faso | B | NA |
| Cambodia | B | B2 |
| Cameroon | B | NA |
| Canada | AAA | Aaa |
| Cape Verde | B+ | NA |
| Cayman Islands | NA | Aaa |
| Chile | AA+ | Aa3 |
| China | AA- | Aa3 |
| Colombia | BBB+ | Baa3 |
| Cook Islands | B+ | NA |
| Costa Rica | BB | Baa3 |
| Croatia | BB+ | Ba1 |
| Cuba | NA | Caa1 |
| Curacao | A- | NA |
| Cyprus | CCC+ | Caa3 |
| Czech Republic | AA | A1 |
| Denmark | AAA | Aaa |
| Dominican Republic | B+ | B1 |
| Ecuador | B | Caa1 |
| Egypt | CCC+ | Caa1 |
| El Salvador | BB- | Ba3 |
| Estonia | AA- | A1 |
| Fiji | B | B1 |
| Finland | AAA | Aaa |
| France | AA+ | Aa1 |
| Gabon | BB- | NA |
| Georgia | BB- | Ba3 |
| Germany | AAA | Aaa |
| Ghana | B | B1 |
| Greece | B- | C |
| Guatemala | BB+ | Ba1 |
| Honduras | B+ | B2 |
| Hong Kong | AAA | Aa1 |
| Hungary | BB | Ba1 |
| Iceland | BBB- | Baa3 |
| India | BBB- | Baa3 |
| Indonesia | BB+ | Baa3 |
| Ireland | BBB+ | Ba1 |
| Isle of Man | AA+ | Aaa |
| Israel | A+ | A1 |
| Italy | BBB+ | Baa2 |
| Jamaica | CCC+ | Caa3 |
| Japan | AA- | Aa3 |
| Jordan | BB- | B1 |
| Kazakhstan | BBB+ | Baa2 |
| Kenya | B+ | B1 |
| Korea | AA- | Aa3 |
| Kuwait | AA | Aa2 |
| Latvia | BBB+ | Baa2 |
| Lebanon | B | B1 |
| Liechtenstein | AAA | NA |
| Lithuania | BBB | Baa1 |
| Luxembourg | AAA | Aaa |
| Macao | NA | Aa3 |
| Macedonia | BB- | NA |
| Malaysia | A | A3 |
| Malta | BBB+ | A3 |
| Mauritius | NA | Baa1 |
| Mexico | A- | Baa1 |
| Moldova | NA | B3 |
| Mongolia | BB- | B1 |
| Montenegro | BB- | Ba3 |
| Montserrat | BBB- | NA |
| Morocco | BBB | Ba1 |
| Mozambique | B+ | NA |
| Namibia | NA | Baa3 |
| Netherlands | AAA | Aaa |
| New Zealand | AA+ | Aaa |
| Nicaragua | NA | B3 |
| Nigeria | BB- | Ba3 |
| Norway | AAA | Aaa |
| Oman | A | A1 |
| Pakistan | B- | Caa1 |
| Panama | BBB | Baa2 |
| Papua New Guinea | B+ | B1 |
| Paraguay | BB- | Ba3 |
| Peru | BBB | Baa2 |
| Philippines | BBB- | Ba1 |
| Poland | A- | A2 |
| Portugal | BB | Ba3 |
| Qatar | AA | Aa2 |
| Romania | BB+ | Baa3 |
| Russia | BBB+ | Baa1 |
| Rwanda | B | NA |
| Saudi Arabia | AA- | Aa3 |
| Senegal | B+ | B1 |
| Serbia | BB- | NA |
| Singapore | AAA | Aaa |
| Slovakia | A | A2 |
| Slovenia | A- | Ba1 |
| South Africa | A- | Baa1 |
| Spain | BBB- | Baa3 |
| Sri Lanka | B+ | B1 |
| St. Maarten | NA | Baa1 |
| St. Vincent & the Grenadines | NA | B2 |
| Suriname | BB- | Ba3 |
| Sweden | AAA | Aaa |
| Switzerland | AAA | Aaa |
| Taiwan | AA- | Aa3 |
| Thailand | A- | Baa1 |
| Trinidad and Tobago | A | Baa1 |
| Tunisia | BB- | Ba2 |
| Turkey | BBB | Baa3 |
| Uganda | B+ | NA |
| Ukraine | B | B3 |
| United Arab Emirates | NA | Aa2 |
| United Kingdom | AAA | Aa1 |
| United States of America | AA+ | Aaa |
| Uruguay | BBB- | Baa3 |
| Venezuela | B | B1 |
| Vietnam | BB- | B2 |
| Zambia | NA | B1 |
