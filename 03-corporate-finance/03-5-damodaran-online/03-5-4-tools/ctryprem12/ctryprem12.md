---
title: "Ctryprem12"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pc/archives/ctryprem12.xls
---

# Ctryprem12

Source: https://pages.stern.nyu.edu/~adamodar/pc/archives/ctryprem12.xls

Sheets: Explanation and FAQ, ERPs by country, Regional breakdown, Regional Simple Averages, Regional Weighted Averages, Sovereign Ratings (Moody's), Regional lookup table, 10-year CDS Spreads, Equity vs Govt Bond volatility, Country GDP

## Explanation and FAQ

| Country Risk Premiums |
|---|
| To estimate the equity risk premium for a country, I start with a mature market premium and add an additional country risk premium, based upon the risk of the country in question. |
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
| Substep 2: I apply the scaling factor that you chose for the default spreads to this number to get a country risk premium. |
|  |
| Step 4: Compute a total equtiy risk premium |
| Add the mature market premium from step 1 to the country risk premium from step 3 to get a total equity risk premium. |
|  |
| If you are interested in a fuller explanation of these concepts, try these references: |
| My paper on equity risk premiums: |
| Campbell Harvey's country risk premium page: |
| Watch my lectures on country risk premiums: |
|  |

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
| Angola |
| Argentina |
| Armenia |
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
| Bermuda |
| Bolivia |
| Bosnia and Herzegovina |
| Botswana |
| Brazil |
| Bulgaria |
| Cambodia |
| Canada |
| Cayman Islands |
| Chile |
| China |
| Colombia |
| Costa Rica |
| Croatia |
| Cuba |
| Cyprus |
| Czech Republic |
| Denmark |
| Dominican Republic |
| Ecuador |
| Egypt |
| El Salvador |
| Estonia |
| Fiji Islands |
| Finland |
| France |
| Georgia |
| Germany |
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
| Lithuania |
| Luxembourg |
| Macao |
| Malaysia |
| Malta |
| Mauritius |
| Mexico |
| Moldova |
| Mongolia |
| Montenegro |
| Morocco |
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
| Saudi Arabia |
| Senegal |
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

## Regional breakdown

| Country | GDP | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|
| Albania | 13 | B1 | 0.04 | 0.118 | 0.06 | Eastern Europe & Russia |
| Angola | 101 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Africa |
| Argentina | 446 | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Armenia | 10.2 | Ba2 | 0.0275 | 0.09925 | 0.04125 | Eastern Europe & Russia |
| Australia | 1371.8 | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| Austria | 418.5 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Azerbaijan | 63.4 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Bahamas | 7.8 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Bahrain | 22.9 | Baa1 | 0.015 | 0.0805 | 0.0225 | Middle East |
| Bangladesh | 110.6 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Asia |
| Barbados | 3.7 | Baa3 | 0.02 | 0.088 | 0.03 | Caribbean |
| Belarus | 55.1 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Belgium | 511.5 | Aa3 | 0.007 | 0.0685 | 0.0105 | Western Europe |
| Belize | 1.5 | Caa3 | 0.1 | 0.20800000000000002 | 0.15000000000000002 | Central and South America |
| Bermuda | 7.3 | Aa2 | 0.005 | 0.0655 | 0.0075 | Caribbean |
| Bolivia | 24.4 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Central and South America |
| Bosnia and Herzegovina | 18.1 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Botswana | 17.6 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Africa |
| Brazil | 2476.7 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Bulgaria | 53.5 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Eastern Europe & Russia |
| Cambodia | 12.9 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Asia |
| Canada | 1736 | Aaa | 0 | 0.058 | 0 | North America |
| Cayman Islands | 3 | Aa3 | 0.007 | 0.0685 | 0.0105 | Caribbean |
| Chile | 248.6 | Aa3 | 0.007 | 0.0685 | 0.0105 | Central and South America |
| China | 7298.1 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Colombia | 331.7 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Costa Rica | 41 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Croatia | 63.9 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Cuba | 60.8 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Caribbean |
| Cyprus | 24.7 | B3 | 0.06 | 0.148 | 0.09 | Western Europe |
| Czech Republic | 215.2 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Eastern Europe & Russia |
| Denmark | 332.7 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Dominican Republic | 55.6 | B1 | 0.04 | 0.118 | 0.06 | Caribbean |
| Ecuador | 67 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Central and South America |
| Egypt | 229.5 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Africa |
| El Salvador | 23.1 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Central and South America |
| Estonia | 22.2 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Eastern Europe & Russia |
| Fiji Islands | 3.8 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Finland | 266.1 | Aaa | 0 | 0.058 | 0 | Western Europe |
| France | 2773 | Aa1 | 0.0025 | 0.06175 | 0.00375 | Western Europe |
| Georgia | 14.4 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Eastern Europe & Russia |
| Germany | 3570.6 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Greece | 298.7 | Caa3 | 0.1 | 0.20800000000000002 | 0.15000000000000002 | Western Europe |
| Guatemala | 46.9 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Central and South America |
| Honduras | 17.3 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Central and South America |
| Hong Kong | 243.7 | Aa1 | 0.0025 | 0.06175 | 0.00375 | Asia |
| Hungary | 140 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Eastern Europe & Russia |
| Iceland | 14.1 | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| India | 1848 | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Indonesia | 846.8 | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Ireland | 217.3 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Western Europe |
| Isle of Man | 3 | Aaa | 0 | 0.058 | 0 | Financial Center |
| Israel | 242.9 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Middle East |
| Italy | 2194.8 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Western Europe |
| Jamaica | 15.1 | B3 | 0.06 | 0.148 | 0.09 | Caribbean |
| Japan | 5867.2 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Jordan | 28.8 | Ba2 | 0.0275 | 0.09925 | 0.04125 | Middle East |
| Kazakhstan | 186.2 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Eastern Europe & Russia |
| Kenya | 33.6 | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Korea | 1116.2 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Kuwait | 176.6 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Latvia | 28.3 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Lebanon | 42.2 | B1 | 0.04 | 0.118 | 0.06 | Middle East |
| Lithuania | 42.7 | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Luxembourg | 59.5 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Macao | 36.4 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Malaysia | 278.7 | A3 | 0.0115 | 0.07525000000000001 | 0.01725 | Asia |
| Malta | 8.9 | A3 | 0.0115 | 0.07525000000000001 | 0.01725 | Western Europe |
| Mauritius | 11.3 | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Mexico | 1155.3 | Baa1 | 0.015 | 0.0805 | 0.0225 | Central and South America |
| Moldova | 7 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Mongolia | 8.6 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Montenegro | 4.6 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Eastern Europe & Russia |
| Morocco | 100.2 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Africa |
| Namibia | 12.3 | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Netherlands | 836.3 | Aaa | 0 | 0.058 | 0 | Western Europe |
| New Zealand | 142.5 | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| Nicaragua | 7.3 | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Nigeria | 235.9 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Africa |
| Norway | 485.8 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Oman | 71.8 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Middle East |
| Pakistan | 211.1 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Asia |
| Panama | 30.7 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Papua New Guinea | 12.9 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Paraguay | 23.9 | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Peru | 176.7 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Philippines | 224.8 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Asia |
| Poland | 514.5 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Eastern Europe & Russia |
| Portugal | 237.5 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Western Europe |
| Qatar | 173 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Romania | 179.8 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Russia | 1857.8 | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Saudi Arabia | 576.8 | Aa3 | 0.007 | 0.0685 | 0.0105 | Middle East |
| Senegal | 14.3 | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Singapore | 239.7 | Aaa | 0 | 0.058 | 0 | Asia |
| Slovakia | 96 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Eastern Europe & Russia |
| Slovenia | 49.5 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Western Europe |
| South Africa | 408.2 | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Spain | 1490.8 | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| Sri Lanka | 59.2 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| St. Maarten | 1 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| St. Vincent & the Grenadines | 0.7 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Caribbean |
| Suriname | 0.5 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Caribbean |
| Sweden | 538.1 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Switzerland | 635.7 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Taiwan | 393.2 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Thailand | 345.6 | Baa1 | 0.015 | 0.0805 | 0.0225 | Asia |
| Trinidad and Tobago | 22.5 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Tunisia | 45.9 | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Turkey | 773.1 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Western Europe |
| Ukraine | 165.2 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| United Arab Emirates | 360.2 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| United Kingdom | 2431.6 | Aaa | 0 | 0.058 | 0 | Western Europe |
| United States of America | 15094 | Aaa | 0 | 0.058 | 0 | North America |
| Uruguay | 46.7 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Venezuela | 316.5 | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Vietnam | 124 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Asia |
| Zambia | 19.2 | B1 | 0.04 | 0.118 | 0.06 | Africa |

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
|  |

## Regional Weighted Averages

| Country | GDP | Weight in region | Country Risk Premium | Total Risk Premium | Default Spread * Weight | CRP * Weight | TRP * Weight | Long-Term Rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Angola | 101 | 0.08218063466232708 | 0.04875 | 0.10675000000000001 | 0.0026708706265256305 | 0.004006305939788446 | 0.008772782750203417 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Africa |
| Botswana | 17.6 | 0.014320585842148086 | 0.015 | 0.07300000000000001 | 0.00014320585842148085 | 0.00021480878763222128 | 0.0010454027664768104 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Africa |
| Egypt | 229.5 | 0.18673718470301054 | 0.07500000000000001 | 0.133 | 0.009336859235150527 | 0.014005288852725792 | 0.024836045565500404 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Africa |
| Kenya | 33.6 | 0.027339300244100893 | 0.06 | 0.118 | 0.0010935720097640358 | 0.0016403580146460534 | 0.0032260374288039053 | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Mauritius | 11.3 | 0.00919446704637917 | 0.0225 | 0.0805 | 0.00013791700569568753 | 0.0002068755085435313 | 0.0007401545972335232 | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Morocco | 100.2 | 0.08152969894222944 | 0.036000000000000004 | 0.094 | 0.001956712774613507 | 0.0029350691619202604 | 0.007663791700569568 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Africa |
| Namibia | 12.3 | 0.010008136696501219 | 0.03 | 0.088 | 0.00020016273393002438 | 0.00030024410089503654 | 0.0008807160292921072 | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Nigeria | 235.9 | 0.19194467046379168 | 0.04875 | 0.10675000000000001 | 0.00623820179007323 | 0.009357302685109845 | 0.020490093572009763 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Africa |
| Senegal | 14.3 | 0.01163547599674532 | 0.06 | 0.118 | 0.00046541903986981276 | 0.0006981285598047191 | 0.0013729861676159477 | B1 | 0.04 | 0.118 | 0.06 | Africa |
| South Africa | 408.2 | 0.3321399511798209 | 0.0225 | 0.0805 | 0.004982099267697313 | 0.0074731489015459705 | 0.026737266069975583 | Baa1 | 0.015 | 0.0805 | 0.0225 | Africa |
| Tunisia | 45.9 | 0.03734743694060211 | 0.03 | 0.088 | 0.0007469487388120421 | 0.0011204231082180631 | 0.0032865744507729854 | Baa3 | 0.02 | 0.088 | 0.03 | Africa |
| Zambia | 19.2 | 0.015622457282343365 | 0.06 | 0.118 | 0.0006248982912937346 | 0.0009373474369406019 | 0.001843449959316517 | B1 | 0.04 | 0.118 | 0.06 | Africa |
| Africa | 1229.0000000000002 | 1 |  |  | 0.02859686737184703 | 0.042895301057770535 | 0.10089530105777053 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bangladesh | 110.6 | 0.005736068251951352 | 0.04875 | 0.10675000000000001 | 0.00018642221818841894 | 0.0002796333272826284 | 0.0006123252858958069 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Asia |
| Cambodia | 12.9 | 0.0006690350854445972 | 0.07500000000000001 | 0.133 | 3.345175427222986e-05 | 5.0177631408344796e-05 | 8.898166636413143e-05 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Asia |
| China | 7298.1 | 0.378502709851412 | 0.0105 | 0.0685 | 0.002649518968959884 | 0.003974278453439826 | 0.025927435624821724 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Fiji Islands | 3.8 | 0.00019708010268910614 | 0.06 | 0.118 | 7.883204107564245e-06 | 1.1824806161346368e-05 | 2.3255452117314524e-05 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Hong Kong | 243.7 | 0.012639058164561885 | 0.00375 | 0.06175 | 3.1597645411404716e-05 | 4.739646811710707e-05 | 0.0007804618416616964 | Aa1 | 0.0025 | 0.06175 | 0.00375 | Asia |
| India | 1848 | 0.09584316572880741 | 0.03 | 0.088 | 0.0019168633145761483 | 0.0028752949718642224 | 0.008434198584135051 | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Indonesia | 846.8 | 0.043917744988719754 | 0.03 | 0.088 | 0.0008783548997743951 | 0.0013175323496615926 | 0.0038647615590073382 | Baa3 | 0.02 | 0.088 | 0.03 | Asia |
| Japan | 5867.2 | 0.30429167855197986 | 0.0105 | 0.0685 | 0.002130041749863859 | 0.0031950626247957887 | 0.020843979980810622 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Korea | 1116.2 | 0.05788968700567902 | 0.0105 | 0.0685 | 0.0004052278090397532 | 0.0006078417135596298 | 0.0039654435598890135 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Macao | 36.4 | 0.001887819931021964 | 0.0105 | 0.0685 | 1.3214739517153747e-05 | 1.9822109275730623e-05 | 0.00012931566527500454 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Malaysia | 278.7 | 0.014454269636698389 | 0.01725 | 0.07525000000000001 | 0.00016622410082203147 | 0.00024933615123304726 | 0.001087683790161554 | A3 | 0.0115 | 0.07525000000000001 | 0.01725 | Asia |
| Mongolia | 8.6 | 0.0004460233902963981 | 0.06 | 0.118 | 1.7840935611855923e-05 | 2.6761403417783886e-05 | 5.2630760054974974e-05 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Pakistan | 211.1 | 0.010948318336229028 | 0.10500000000000001 | 0.163 | 0.000766382283536032 | 0.001149573425304048 | 0.0017845758888053315 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Asia |
| Papua New Guinea | 12.9 | 0.0006690350854445972 | 0.06 | 0.118 | 2.6761403417783886e-05 | 4.014210512667583e-05 | 7.894614008246246e-05 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Philippines | 224.8 | 0.011658843969608174 | 0.036000000000000004 | 0.094 | 0.00027981225527059616 | 0.0004197183829058943 | 0.0010959313331431683 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Asia |
| Singapore | 239.7 | 0.012431605424889141 | 0 | 0.058 | 0 | 0 | 0.0007210331146435702 | Aaa | 0 | 0.058 | 0 | Asia |
| Sri Lanka | 59.2 | 0.003070300547156601 | 0.06 | 0.118 | 0.00012281202188626404 | 0.00018421803282939607 | 0.0003622954645644789 | B1 | 0.04 | 0.118 | 0.06 | Asia |
| Taiwan | 393.2 | 0.020392604309830666 | 0.0105 | 0.0685 | 0.00014274823016881467 | 0.000214122345253222 | 0.0013968933952234008 | Aa3 | 0.007 | 0.0685 | 0.0105 | Asia |
| Thailand | 345.6 | 0.017923916707725022 | 0.0225 | 0.0805 | 0.0002688587506158753 | 0.000403288125923813 | 0.0014428752949718644 | Baa1 | 0.015 | 0.0805 | 0.0225 | Asia |
| Vietnam | 124 | 0.006431034929855042 | 0.07500000000000001 | 0.133 | 0.00032155174649275216 | 0.00048232761973912824 | 0.0008553276456707207 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Asia |
| Asia | 19281.5 | 0.9999999999999999 |  |  | 0.010365568031532815 | 0.015548352047299223 | 0.07354835204729923 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Australia | 1371.8 | 0.9058971141781681 | 0 | 0.058 | 0 | 0 | 0.05254203262233375 | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| New Zealand | 142.5 | 0.09410288582183188 | 0 | 0.058 | 0 | 0 | 0.005457967377666249 | Aaa | 0 | 0.058 | 0 | Australia & New Zealand |
| Australia & New Zealand | 1514.3 | 1 |  |  | 0 | 0 | 0.057999999999999996 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bahamas | 7.8 | 0.04382022471910113 | 0.0225 | 0.0805 | 0.000657303370786517 | 0.0009859550561797754 | 0.003527528089887641 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Barbados | 3.7 | 0.02078651685393259 | 0.03 | 0.088 | 0.0004157303370786518 | 0.0006235955056179776 | 0.0018292134831460677 | Baa3 | 0.02 | 0.088 | 0.03 | Caribbean |
| Bermuda | 7.3 | 0.04101123595505619 | 0.0075 | 0.0655 | 0.00020505617977528093 | 0.0003075842696629214 | 0.0026862359550561803 | Aa2 | 0.005 | 0.0655 | 0.0075 | Caribbean |
| Cayman Islands | 3 | 0.016853932584269666 | 0.0105 | 0.0685 | 0.00011797752808988767 | 0.00017696629213483152 | 0.0011544943820224723 | Aa3 | 0.007 | 0.0685 | 0.0105 | Caribbean |
| Cuba | 60.8 | 0.3415730337078652 | 0.10500000000000001 | 0.163 | 0.023910112359550564 | 0.03586516853932585 | 0.05567640449438203 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Caribbean |
| Dominican Republic | 55.6 | 0.3123595505617978 | 0.06 | 0.118 | 0.012494382022471913 | 0.018741573033707867 | 0.03685842696629214 | B1 | 0.04 | 0.118 | 0.06 | Caribbean |
| Jamaica | 15.1 | 0.08483146067415731 | 0.09 | 0.148 | 0.005089887640449439 | 0.007634831460674158 | 0.012555056179775282 | B3 | 0.06 | 0.148 | 0.09 | Caribbean |
| St. Vincent & the Grenadines | 0.7 | 0.003932584269662922 | 0.07500000000000001 | 0.133 | 0.0001966292134831461 | 0.0002949438202247192 | 0.0005230337078651686 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Caribbean |
| St. Maarten | 1 | 0.005617977528089888 | 0.0225 | 0.0805 | 8.426966292134832e-05 | 0.00012640449438202248 | 0.00045224719101123604 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Suriname | 0.5 | 0.002808988764044944 | 0.0488 | 0.1068 | 9.129213483146069e-05 | 0.0001370786516853933 | 0.00030000000000000003 | Ba3 | 0.0325 | 0.1068 | 0.0488 | Caribbean |
| Trinidad and Tobago | 22.5 | 0.1264044943820225 | 0.0225 | 0.0805 | 0.0018960674157303375 | 0.002844101123595506 | 0.010175561797752811 | Baa1 | 0.015 | 0.0805 | 0.0225 | Caribbean |
| Caribbean | 177.99999999999997 | 1 |  |  | 0.04515870786516854 | 0.06773820224719102 | 0.12573820224719104 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Argentina | 446 | 0.08136755879079781 | 0.09 | 0.148 | 0.004882053527447868 | 0.007323080291171803 | 0.012042398701038076 | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Belize | 1.5 | 0.0002736577089376608 | 0.15000000000000002 | 0.20800000000000002 | 2.7365770893766082e-05 | 4.1048656340649125e-05 | 5.692080345903345e-05 | Caa3 | 0.1 | 0.20800000000000002 | 0.15000000000000002 | Central and South America |
| Bolivia | 24.4 | 0.0044514987320526155 | 0.04875 | 0.10675000000000001 | 0.00014467370879171 | 0.000217010563187565 | 0.0004751974896466168 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Central and South America |
| Brazil | 2476.7 | 0.451845365150603 | 0.026250000000000002 | 0.08425 | 0.007907293890135553 | 0.011860940835203329 | 0.0380679720139383 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Chile | 248.6 | 0.04535420429460165 | 0.0105 | 0.0685 | 0.00031747943006221155 | 0.00047621914509331735 | 0.0031067629941802133 | Aa3 | 0.007 | 0.0685 | 0.0105 | Central and South America |
| Colombia | 331.7 | 0.06051484136974806 | 0.03 | 0.088 | 0.0012102968273949612 | 0.0018154452410924417 | 0.0053253060405378284 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Costa Rica | 41 | 0.007479977377629395 | 0.03 | 0.088 | 0.00014959954755258792 | 0.00022439932132888184 | 0.0006582380092313867 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Ecuador | 67 | 0.012223377665882183 | 0.10500000000000001 | 0.163 | 0.0008556364366117529 | 0.0012834546549176293 | 0.001992410559538796 | Caa1 | 0.07 | 0.163 | 0.10500000000000001 | Central and South America |
| El Salvador | 23.1 | 0.004214328717639977 | 0.04875 | 0.10675000000000001 | 0.00013696568332329924 | 0.00020544852498494888 | 0.0004498795906080676 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Central and South America |
| Guatemala | 46.9 | 0.008556364366117527 | 0.036000000000000004 | 0.094 | 0.00020535274478682066 | 0.00030802911718023104 | 0.0008042982504150476 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Central and South America |
| Honduras | 17.3 | 0.0031561855764143548 | 0.07500000000000001 | 0.133 | 0.00015780927882071775 | 0.00023671391823107665 | 0.0004197726816631092 | B2 | 0.05 | 0.133 | 0.07500000000000001 | Central and South America |
| Mexico | 1155.3 | 0.21077116742378635 | 0.0225 | 0.0805 | 0.003161567511356795 | 0.004742351267035192 | 0.0169670789776148 | Baa1 | 0.015 | 0.0805 | 0.0225 | Central and South America |
| Nicaragua | 7.3 | 0.0013318008501632826 | 0.09 | 0.148 | 7.990805100979695e-05 | 0.00011986207651469543 | 0.00019710652582416582 | B3 | 0.06 | 0.148 | 0.09 | Central and South America |
| Panama | 30.7 | 0.005600861109590791 | 0.026250000000000002 | 0.08425 | 9.801506941783884e-05 | 0.00014702260412675827 | 0.00047187254848302416 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Paraguay | 23.9 | 0.004360279495740062 | 0.06 | 0.118 | 0.00017441117982960248 | 0.0002616167697444037 | 0.0005145129804973273 | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Peru | 176.7 | 0.03223687811285644 | 0.026250000000000002 | 0.08425 | 0.0005641453669749878 | 0.0008462180504624817 | 0.0027159569810081556 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Central and South America |
| Uruguay | 46.7 | 0.008519876671592506 | 0.03 | 0.088 | 0.00017039753343185013 | 0.0002555963001477752 | 0.0007497491471001405 | Baa3 | 0.02 | 0.088 | 0.03 | Central and South America |
| Venezuela | 316.5 | 0.05774177658584643 | 0.06 | 0.118 | 0.0023096710634338572 | 0.0034645065951507854 | 0.006813529637129878 | B1 | 0.04 | 0.118 | 0.06 | Central and South America |
| Central and South America | 5481.299999999999 | 1 |  |  | 0.02255264262127598 | 0.033828963931913966 | 0.09182896393191398 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Albania | 13 | 0.003465650075977713 | 0.06 | 0.118 | 0.00013862600303910853 | 0.00020793900455866278 | 0.0004089467089653701 | B1 | 0.04 | 0.118 | 0.06 | Eastern Europe & Russia |
| Armenia | 10.2 | 0.0027192023673055904 | 0.04125 | 0.09925 | 7.477806510090373e-05 | 0.00011216709765135561 | 0.00026988083495507986 | Ba2 | 0.0275 | 0.09925 | 0.04125 | Eastern Europe & Russia |
| Azerbaijan | 63.4 | 0.016901708832075923 | 0.03 | 0.088 | 0.0003380341766415185 | 0.0005070512649622777 | 0.0014873503772226812 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Belarus | 55.1 | 0.014689024552797846 | 0.09 | 0.148 | 0.0008813414731678707 | 0.001322012209751806 | 0.002173975633814081 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Bosnia and Herzegovina | 18.1 | 0.004825251259630509 | 0.09 | 0.148 | 0.0002895150755778305 | 0.0004342726133667458 | 0.0007141371864253153 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Bulgaria | 53.5 | 0.014262483004985204 | 0.026250000000000002 | 0.08425 | 0.0002495934525872411 | 0.0003743901788808617 | 0.0012016141931700036 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Eastern Europe & Russia |
| Croatia | 63.9 | 0.017035003065767374 | 0.03 | 0.088 | 0.0003407000613153475 | 0.0005110500919730212 | 0.0014990802697875288 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Czech Republic | 215.2 | 0.0573698381808003 | 0.012750000000000001 | 0.07075000000000001 | 0.00048764362453680254 | 0.0007314654368052038 | 0.004058916051291621 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Eastern Europe & Russia |
| Estonia | 22.2 | 0.005918263975900402 | 0.012750000000000001 | 0.07075000000000001 | 5.0305243795153424e-05 | 7.545786569273013e-05 | 0.0004187171762949535 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Eastern Europe & Russia |
| Georgia | 14.4 | 0.003838873930313775 | 0.04875 | 0.10675000000000001 | 0.0001247634027351977 | 0.00018714510410279653 | 0.0004097997920609955 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Eastern Europe & Russia |
| Hungary | 140 | 0.037322385433606144 | 0.036000000000000004 | 0.094 | 0.0008957372504065475 | 0.0013436058756098213 | 0.0035083042307589773 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Eastern Europe & Russia |
| Kazakhstan | 186.2 | 0.049638772626696165 | 0.026250000000000002 | 0.08425 | 0.0008686785209671829 | 0.0013030177814507744 | 0.004182066593799152 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Eastern Europe & Russia |
| Latvia | 28.3 | 0.007544453626936099 | 0.03 | 0.088 | 0.000150889072538722 | 0.00022633360880808297 | 0.0006639119191703766 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Lithuania | 42.7 | 0.011383327557249875 | 0.0225 | 0.0805 | 0.00017074991335874813 | 0.00025612487003812216 | 0.000916357868358615 | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Moldova | 7 | 0.0018661192716803072 | 0.09 | 0.148 | 0.00011196715630081843 | 0.00016795073445122764 | 0.00027618565220868547 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Montenegro | 4.6 | 0.0012263069499613445 | 0.04875 | 0.10675000000000001 | 3.98549758737437e-05 | 5.978246381061555e-05 | 0.00013090826690837355 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Eastern Europe & Russia |
| Poland | 514.5 | 0.1371597664685026 | 0.015 | 0.07300000000000001 | 0.001371597664685026 | 0.002057396497027539 | 0.01001266295220069 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Eastern Europe & Russia |
| Romania | 179.8 | 0.047932606435445606 | 0.03 | 0.088 | 0.0009586521287089122 | 0.0014379781930633682 | 0.004218069366319213 | Baa3 | 0.02 | 0.088 | 0.03 | Eastern Europe & Russia |
| Russia | 1857.8 | 0.4952680547039535 | 0.0225 | 0.0805 | 0.0074290208205593025 | 0.011143531230838954 | 0.03986907840366826 | Baa1 | 0.015 | 0.0805 | 0.0225 | Eastern Europe & Russia |
| Slovakia | 96 | 0.025592492868758497 | 0.015 | 0.07300000000000001 | 0.000255924928687585 | 0.00038388739303137743 | 0.0018682519794193705 | A2 | 0.01 | 0.07300000000000001 | 0.015 | Eastern Europe & Russia |
| Ukraine | 165.2 | 0.04404041481165524 | 0.09 | 0.148 | 0.0026424248886993146 | 0.003963637333048972 | 0.006517981392124976 | B3 | 0.06 | 0.148 | 0.09 | Eastern Europe & Russia |
| Eastern Europe & Russia | 3751.1 | 1 |  |  | 0.017870797899282878 | 0.026806196848924317 | 0.08480619684892432 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Isle of Man | 3 | 1 | 0 | 0.058 | 0 | 0 | 0.058 | Aaa | 0 | 0.058 | 0 | Financial Center |
| Financial Centers | 3 |  |  |  | 0 | 0 | 0.058 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bahrain | 22.9 | 0.013508730533270409 | 0.0225 | 0.0805 | 0.00020263095799905612 | 0.00030394643699858416 | 0.001087452807928268 | Baa1 | 0.015 | 0.0805 | 0.0225 | Middle East |
| Israel | 242.9 | 0.14328692779613025 | 0.012750000000000001 | 0.07075000000000001 | 0.0012179388862671072 | 0.001826908329400661 | 0.010137550141576216 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Middle East |
| Jordan | 28.8 | 0.016989145823501653 | 0.04125 | 0.09925 | 0.0004672015101462955 | 0.0007008022652194432 | 0.0016861727229825392 | Ba2 | 0.0275 | 0.09925 | 0.04125 | Middle East |
| Kuwait | 176.6 | 0.10417649834827748 | 0.0075 | 0.0655 | 0.0005208824917413874 | 0.0007813237376120811 | 0.006823560641812176 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Lebanon | 42.2 | 0.024893817838603116 | 0.06 | 0.118 | 0.0009957527135441247 | 0.001493629070316187 | 0.0029374705049551677 | B1 | 0.04 | 0.118 | 0.06 | Middle East |
| Oman | 71.8 | 0.04235488437942425 | 0.012750000000000001 | 0.07075000000000001 | 0.00036001651722510617 | 0.0005400247758376593 | 0.0029966080698442662 | A1 | 0.0085 | 0.07075000000000001 | 0.012750000000000001 | Middle East |
| Qatar | 173 | 0.10205285512033978 | 0.0075 | 0.0655 | 0.0005102642756016989 | 0.0007653964134025483 | 0.006684462010382255 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Saudi Arabia | 576.8 | 0.3402548371873525 | 0.0105 | 0.0685 | 0.0023817838603114676 | 0.0035726757904672017 | 0.02330745634733365 | Aa3 | 0.007 | 0.0685 | 0.0105 | Middle East |
| United Arab Emirates | 360.2 | 0.2124823029731005 | 0.0075 | 0.0655 | 0.0010624115148655025 | 0.0015936172722982537 | 0.013917590844738084 | Aa2 | 0.005 | 0.0655 | 0.0075 | Middle East |
| Middle East | 1695.2 | 1 |  |  | 0.007718882727701747 | 0.011578324091552619 | 0.06957832409155262 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Canada | 1736 | 0.10314913844325609 | 0 | 0.058 | 0 | 0 | 0.005982650029708853 | Aaa | 0 | 0.058 | 0 | North America |
| United States of America | 15094 | 0.8968508615567439 | 0 | 0.058 | 0 | 0 | 0.05201734997029115 | Aaa | 0 | 0.058 | 0 | North America |
| North America | 16830 |  |  |  | 0 | 0 | 0.058 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Belgium | 511.5 | 0.026772675644978094 | 0.0105 | 0.0685 | 0.00018740872951484666 | 0.00028111309427227 | 0.0018339282816809996 | Aa3 | 0.007 | 0.0685 | 0.0105 | Western Europe |
| Cyprus | 24.7 | 0.0012928349724945433 | 0.09 | 0.148 | 7.75700983496726e-05 | 0.00011635514752450889 | 0.0001913395759291924 | B3 | 0.06 | 0.148 | 0.09 | Western Europe |
| Finland | 266.1 | 0.013928072315012066 | 0 | 0.058 | 0 | 0 | 0.0008078281942706999 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Germany | 3570.6 | 0.1868905486959116 | 0 | 0.058 | 0 | 0 | 0.010839651824362874 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Portugal | 237.5 | 0.012431105504755225 | 0.04875 | 0.10675000000000001 | 0.0004040109289045448 | 0.0006060163933568172 | 0.0013270205126326203 | Ba3 | 0.0325 | 0.10675000000000001 | 0.04875 | Western Europe |
| Ireland | 217.3 | 0.011373807268140254 | 0.036 | 0.094 | 0.0002729713744353661 | 0.00040945706165304915 | 0.0010691378832051839 | Ba1 | 0.024 | 0.094 | 0.036 | Western Europe |
| Italy | 2194.8 | 0.11487911731299694 | 0.026250000000000002 | 0.08425 | 0.0020103845529774464 | 0.00301557682946617 | 0.009678565633619993 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Western Europe |
| Luxembourg | 42.7 | 0.002234981916012834 | 0 | 0.058 | 0 | 0 | 0.00012962895112874438 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Malta | 8.9 | 0.0004658393220729327 | 0.0173 | 0.0753 | 5.357152203838726e-06 | 8.059020271861735e-06 | 3.507770095209183e-05 | A3 | 0.0115 | 0.0753 | 0.0173 | Western Europe |
| Netherlands | 836.3 | 0.04377319382579703 | 0 | 0.058 | 0 | 0 | 0.002538845241896228 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Austria | 1371.8 | 0.07180206539546619 | 0 | 0.058 | 0 | 0 | 0.004164519792937039 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Denmark | 332.7 | 0.01741401600602974 | 0 | 0.058 | 0 | 0 | 0.001010012928349725 | Aaa | 0 | 0.058 | 0 | Western Europe |
| France | 2773 | 0.1451429707986789 | 0.00375 | 0.06175 | 0.0003628574269966973 | 0.0005442861404950459 | 0.008962578446818423 | Aa1 | 0.0025 | 0.06175 | 0.00375 | Western Europe |
| Greece | 298.7 | 0.015634405112717412 | 0.15000000000000002 | 0.20800000000000002 | 0.0015634405112717412 | 0.0023451607669076123 | 0.003251956263445222 | Caa3 | 0.1 | 0.20800000000000002 | 0.15000000000000002 | Western Europe |
| Iceland | 14.1 | 0.0007380151057559944 | 0.03 | 0.088 | 1.4760302115119889e-05 | 2.214045317267983e-05 | 6.49453293065275e-05 | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| Norway | 485.8 | 0.025427499175621426 | 0 | 0.058 | 0 | 0 | 0.0014747949521860429 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Slovenia | 49.5 | 0.0025909040946752995 | 0.026250000000000002 | 0.08425 | 4.534082165681775e-05 | 6.801123248522662e-05 | 0.000218283669976394 | Baa2 | 0.0175 | 0.08425 | 0.026250000000000002 | Western Europe |
| Spain | 1490.8 | 0.07803070352205932 | 0.03 | 0.088 | 0.0015606140704411864 | 0.0023409211056617794 | 0.00686670190994122 | Baa3 | 0.02 | 0.088 | 0.03 | Western Europe |
| Sweden | 538.1 | 0.028164959461510684 | 0 | 0.058 | 0 | 0 | 0.0016335676487676198 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Switzerland | 635.7 | 0.033273489555254304 | 0 | 0.058 | 0 | 0 | 0.0019298623942047496 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Turkey | 773.1 | 0.04046521122411059 | 0.036000000000000004 | 0.094 | 0.0009711650693786543 | 0.0014567476040679814 | 0.0038037298550663958 | Ba1 | 0.024 | 0.094 | 0.036000000000000004 | Western Europe |
| United Kingdom | 2431.6 | 0.12727358376994866 | 0 | 0.058 | 0 | 0 | 0.0073818678586570225 | Aaa | 0 | 0.058 | 0 | Western Europe |
| Western Europe | 19105.3 | 1.0000000000000002 |  |  | 0.007475881038245932 | 0.011213844849335002 | 0.06921384484933502 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| Row Labels | Default Spread (Weighted average) | Country Risk Premium (Weighted Average) |  |  |  |  |  |  |  |  |  |  |
| Africa | 0.02859686737184703 | 0.042895301057770535 |  |  |  |  |  |  |  |  |  |  |
| Asia | 0.010365568031532815 | 0.015548352047299223 |  |  |  |  |  |  |  |  |  |  |
| Australia & New Zealand | 0 | 0 |  |  |  |  |  |  |  |  |  |  |
| Caribbean | 0.04515870786516854 | 0.06773820224719102 |  |  |  |  |  |  |  |  |  |  |
| Central and South America | 0.02255264262127598 | 0.033828963931913966 |  |  |  |  |  |  |  |  |  |  |
| Eastern Europe & Russia | 0.017870797899282878 | 0.026806196848924317 |  |  |  |  |  |  |  |  |  |  |
| Financial Center | 0 | 0 |  |  |  |  |  |  |  |  |  |  |
| Middle East | 0.007718882727701747 | 0.011578324091552619 |  |  |  |  |  |  |  |  |  |  |
| North America | 0 | 0 |  |  |  |  |  |  |  |  |  |  |
| Western Europe | 0.007475881038245932 | 0.011213844849335002 |  |  |  |  |  |  |  |  |  |  |
| Grand Total | 0.0233 | 0.093 |  |  |  |  |  |  |  |  |  |  |

## Sovereign Ratings (Moody's)

| Foreign Currency | Local Currency |
|---|---|
| B1 | B1 |
| Ba3 | Ba3 |
| B3 | B3 |
| Ba2 | Ba2 |
| Aaa | Aaa |
| Aaa | Aaa |
| Baa3 | Baa3 |
| Baa1 | Baa1 |
| Baa1 | Baa1 |
| Ba3 | Ba3 |
| Baa3 | Baa3 |
| B3 | B3 |
| Aa3 | Aa3 |
| Ca | Caa3 |
| Aa2 | Aa2 |
| Ba3 | Ba3 |
| B3 | B3 |
| A2 | A2 |
| Baa2 | Baa2 |
| Baa2 | Baa2 |
| B2 | B2 |
| Aaa | Aaa |
| Aa3 | Aa3 |
| Aa3 | Aa3 |
| Aa3 | Aa3 |
| Baa3 | Baa3 |
| Baa3 | Baa3 |
| Baa3 | Baa3 |
| Caa1 | Caa1 |
| B3 | B3 |
| A1 | A1 |
| Aaa | Aaa |
| B1 | B1 |
| Caa1 | Caa1 |
| B2 | B2 |
| Ba3 | Ba3 |
| A1 | A1 |
| B1 | B1 |
| Aaa | Aaa |
| Aa1 | Aa1 |
| Ba3 | Ba3 |
| Aaa | Aaa |
| Caa3 | Caa3 |
| Ba1 | Ba1 |
| B2 | B2 |
| Aa1 | Aa1 |
| Ba1 | Ba1 |
| Baa3 | Baa3 |
| Baa3 | Baa3 |
| Baa3 | Baa3 |
| Ba1 | Ba1 |
| Aaa | Aaa |
| A1 | A1 |
| Baa2 | Baa2 |
| B3 | B3 |
| Aa3 | Aa3 |
| Ba2 | Ba2 |
| Baa2 | Baa2 |
| B1 | B1 |
| Aa3 | Aa3 |
| Aa2 | Aa2 |
| Baa3 | Baa3 |
| B1 | B1 |
| Baa1 | Baa1 |
| Aaa | Aaa |
| Aa3 | Aa3 |
| A3 | A3 |
| A3 | A3 |
| Baa1 | Baa1 |
| Baa1 | Baa1 |
| B3 | B3 |
| B1 | B1 |
| Ba3 | Ba3 |
| Ba1 | Ba1 |
| Baa3 | Baa3 |
| Aaa | Aaa |
| Aaa | Aaa |
| B3 | B3 |
| Ba3 | Ba3 |
| Aaa | Aaa |
| A1 | A1 |
| Caa1 | Caa1 |
| Baa2 | Baa2 |
| B1 | B1 |
| B1 | B1 |
| Baa2 | Baa2 |
| Ba1 | Ba1 |
| A2 | A2 |
| Ba3 | Ba3 |
| Aa2 | Aa2 |
| Baa3 | Baa3 |
| Baa1 | Baa1 |
| Aa3 | Aa3 |
| B1 | B1 |
| Aaa | Aaa |
| A2 | A2 |
| Baa2 | Baa2 |
| Baa1 | Baa1 |
| Baa3 | Baa3 |
| B1 | B1 |
| Baa1 | Baa1 |
| B2 | B2 |
| Ba3 | Ba3 |
| Aaa | Aaa |
| Aaa | Aaa |
| Aa3 | Aa3 |
| Baa1 | Baa1 |
| Baa1 | Baa1 |
| Baa3 | Baa3 |
| Ba1 | Ba1 |
| B3 | B3 |
| Aa2 | Aa2 |
| Aaa | Aaa |
| Aaa | Aaa |
| Baa3 | Baa3 |
| B2 | B1 |
| B2 | B2 |
| B1 | B1 |

## Regional lookup table

| Country | Region |
|---|---|
| Albania | Eastern Europe & Russia |
| Angola | Africa |
| Argentina | Central and South America |
| Armenia | Eastern Europe & Russia |
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
| Bermuda | Caribbean |
| Bolivia | Central and South America |
| Bosnia and Herzegovina | Eastern Europe & Russia |
| Botswana | Africa |
| Brazil | Central and South America |
| Bulgaria | Eastern Europe & Russia |
| Cambodia | Asia |
| Canada | North America |
| Cayman Islands | Caribbean |
| Chile | Central and South America |
| China | Asia |
| Colombia | Central and South America |
| Costa Rica | Central and South America |
| Croatia | Eastern Europe & Russia |
| Cuba | Caribbean |
| Cyprus | Western Europe |
| Czech Republic | Eastern Europe & Russia |
| Denmark | Western Europe |
| Dominican Republic | Caribbean |
| Ecuador | Central and South America |
| Egypt | Africa |
| El Salvador | Central and South America |
| Estonia | Eastern Europe & Russia |
| Fiji Islands | Asia |
| Finland | Western Europe |
| France | Western Europe |
| Georgia | Eastern Europe & Russia |
| Germany | Western Europe |
| Greece | Western Europe |
| Guatemala | Central and South America |
| Honduras | Central and South America |
| Hong Kong | Asia |
| Hungary | Eastern Europe & Russia |
| Iceland | Western Europe |
| India | Asia |
| Indonesia | Asia |
| Ireland | Western Europe |
| Isle of Man | Financial Center |
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
| Lithuania | Eastern Europe & Russia |
| Luxembourg | Western Europe |
| Macao | Asia |
| Malaysia | Asia |
| Malta | Western Europe |
| Mauritius | Africa |
| Mexico | Central and South America |
| Moldova | Eastern Europe & Russia |
| Mongolia | Asia |
| Montenegro | Eastern Europe & Russia |
| Morocco | Africa |
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
| Saudi Arabia | Middle East |
| Senegal | Africa |
| Singapore | Asia |
| Slovakia | Eastern Europe & Russia |
| Slovenia | Eastern Europe & Russia |
| South Africa | Africa |
| Spain | Western Europe |
| Sri Lanka | Asia |
| St. Maarten | Africa |
| St. Vincent & the Grenadines | Caribbean |
| Suriname | Caribbean |
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

| Local Currency | 10-year CDS |
|---|---|
| B1 | NA |
| Ba3 | NA |
| B3 | 0.1307 |
| Ba2 | NA |
| Aaa | 0.0086 |
| Aaa | 0.0079 |
| Baa3 | NA |
| Baa1 | NA |
| Baa1 | 0.0252 |
| Ba3 | NA |
| Baa3 | NA |
| B3 | NA |
| Aa3 | 0.0124 |
| Caa3 | NA |
| Aa2 | NA |
| Ba3 | NA |
| B3 | NA |
| A2 | NA |
| Baa2 | 0.0144 |
| Baa2 | 0.0141 |
| B2 | NA |
| Aaa | NA |
| Aa3 | NA |
| Aa3 | 0.0099 |
| Aa3 | 0.0102 |
| Baa3 | 0.0135 |
| Baa3 | 0.0391 |
| Baa3 | 0.0299 |
| Caa1 | NA |
| B3 | 0.0655 |
| A1 | 0.0089 |
| Aaa | 0.0069 |
| B1 | NA |
| Caa1 | NA |
| B2 | 0.0576 |
| Ba3 | NA |
| A1 | 0.0095 |
| B1 | NA |
| Aaa | 0.006 |
| Aa1 | 0.0144 |
| Ba3 | NA |
| Aaa | 0.0082 |
| C | NA |
| Ba1 | NA |
| B2 | NA |
| Aa1 | 0.0103 |
| Ba1 | 0.0316 |
| Baa3 | 0.0216 |
| Baa3 | NA |
| Baa3 | 0.0181 |
| Ba1 | 0.0254 |
| Aaa | NA |
| A1 | 0.0161 |
| Baa2 | 0.0303 |
| B3 | NA |
| Aa3 | 0.0132 |
| Ba2 | NA |
| Baa2 | 0.0197 |
| B1 | NA |
| Aa3 | 0.0113 |
| Aa2 | NA |
| Baa3 | 0.017 |
| B1 | 0.0472 |
| Baa1 | 0.0158 |
| Aaa | NA |
| Aa3 | NA |
| A3 | 0.0114 |
| A3 | NA |
| Baa1 | NA |
| Baa1 | 0.0136 |
| B3 | NA |
| B1 | NA |
| Ba3 | NA |
| Ba1 | 0.0279 |
| Baa3 | NA |
| Aaa | 0.0083 |
| Aaa | 0.0072 |
| B3 | NA |
| Ba3 | NA |
| Aaa | 0.0041 |
| A1 | NA |
| Caa1 | 0.079 |
| Baa2 | 0.0136 |
| B1 | NA |
| B1 | NA |
| Baa2 | 0.0138 |
| Ba1 | 0.0159 |
| A2 | 0.013 |
| Ba3 | 0.0493 |
| Aa2 | 0.0128 |
| Baa3 | 0.0281 |
| Baa1 | 0.0182 |
| Aa3 | 0.0078 |
| B1 | NA |
| Aaa | NA |
| A2 | 0.0142 |
| Baa2 | 0.0259 |
| Baa1 | 0.0203 |
| Baa3 | 0.0314 |
| B1 | NA |
| Baa1 | NA |
| B2 | NA |
| Ba3 | NA |
| Aaa | 0.0041 |
| Aaa | 0.0076 |
| Aa3 | NA |
| Baa1 | 0.0143 |
| Baa1 | NA |
| Baa3 | 0.0421 |
| Ba1 | 0.0179 |
| B3 | 0.0651 |
| Aa2 | NA |
| Aaa | 0.0074 |
| Aaa | 0.0067 |
| Baa3 | NA |
| B1 | 0.0655 |
| B2 | 0.0274 |
| B1 | NA |

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
| Albania | 13 |
| Angola | 101 |
| Argentina | 446 |
| Armenia | 10.2 |
| Australia | 1371.8 |
| Austria | 418.5 |
| Azerbaijan | 63.4 |
| Bahamas | 7.8 |
| Bahrain | 22.9 |
| Bangladesh | 110.6 |
| Barbados | 3.7 |
| Belarus | 55.1 |
| Belgium | 511.5 |
| Belize | 1.5 |
| Bermuda | 7.3 |
| Bolivia | 24.4 |
| Bosnia and Herzegovina | 18.1 |
| Botswana | 17.6 |
| Brazil | 2476.7 |
| Bulgaria | 53.5 |
| Cambodia | 12.9 |
| Canada | 1736 |
| Cayman Islands | 3 |
| Chile | 248.6 |
| China | 7298.1 |
| Colombia | 331.7 |
| Costa Rica | 41 |
| Croatia | 63.9 |
| Cuba | 60.8 |
| Cyprus | 24.7 |
| Czech Republic | 215.2 |
| Denmark | 332.7 |
| Dominican Republic | 55.6 |
| Ecuador | 67 |
| Egypt | 229.5 |
| El Salvador | 23.1 |
| Estonia | 22.2 |
| Fiji Islands | 3.8 |
| Finland | 266.1 |
| France | 2773 |
| Georgia | 14.4 |
| Germany | 3570.6 |
| Greece | 298.7 |
| Guatemala | 46.9 |
| Honduras | 17.3 |
| Hong Kong | 243.7 |
| Hungary | 140 |
| Iceland | 14.1 |
| India | 1848 |
| Indonesia | 846.8 |
| Ireland | 217.3 |
| Isle of Man | 3 |
| Israel | 242.9 |
| Italy | 2194.8 |
| Jamaica | 15.1 |
| Japan | 5867.2 |
| Jordan | 28.8 |
| Kazakhstan | 186.2 |
| Kenya | 33.6 |
| Korea | 1116.2 |
| Kuwait | 176.6 |
| Latvia | 28.3 |
| Lebanon | 42.2 |
| Lithuania | 42.7 |
| Luxembourg | 59.5 |
| Macao | 36.4 |
| Malaysia | 278.7 |
| Malta | 8.9 |
| Mauritius | 11.3 |
| Mexico | 1155.3 |
| Moldova | 7 |
| Mongolia | 8.6 |
| Montenegro | 4.6 |
| Morocco | 100.2 |
| Namibia | 12.3 |
| Netherlands | 836.3 |
| New Zealand | 142.5 |
| Nicaragua | 7.3 |
| Nigeria | 235.9 |
| Norway | 485.8 |
| Oman | 71.8 |
| Pakistan | 211.1 |
| Panama | 30.7 |
| Papua New Guinea | 12.9 |
| Paraguay | 23.9 |
| Peru | 176.7 |
| Philippines | 224.8 |
| Poland | 514.5 |
| Portugal | 237.5 |
| Qatar | 173 |
| Romania | 179.8 |
| Russia | 1857.8 |
| Saudi Arabia | 576.8 |
| Senegal | 14.3 |
| Singapore | 239.7 |
| Slovakia | 96 |
| Slovenia | 49.5 |
| South Africa | 408.2 |
| Spain | 1490.8 |
| Sri Lanka | 59.2 |
| St. Maarten | 1 |
| St. Vincent & the Grenadines | 0.7 |
| Suriname | 0.5 |
| Sweden | 538.1 |
| Switzerland | 635.7 |
| Taiwan | 393.2 |
| Thailand | 345.6 |
| Trinidad and Tobago | 22.5 |
| Tunisia | 45.9 |
| Turkey | 773.1 |
| Turkmenistan | 24.1 |
| Ukraine | 165.2 |
| United Arab Emirates | 360.2 |
| United Kingdom | 2431.6 |
| United States of America | 15094 |
| Uruguay | 46.7 |
| Venezuela | 316.5 |
| Vietnam | 124 |
| Zambia | 19.2 |
