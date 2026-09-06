---
title: "Ctrypremjuly15"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly15.xls
---

# Ctrypremjuly15

Source: https://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly15.xls

Sheets: Explanation and FAQ, Country Lookup, ERPs by country, Regional Simple Averages, Regional Weighted Averages, Regional breakdown, Sovereign Ratings (Moody's,S&P), Regional lookup table, 10-year CDS Spreads, Equity vs Govt Bond volatility, Country GDP, Ratings worksheet, PRS Worksheet

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
| If you cannot find a country on this list, it is because that country does not have a sovereign rating or a sovereign CDS spread. Try the PRS worksheet in this spreadsheet for an alternate estimate. |
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
|  |
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
| Country Default Spread (based on rating) |
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
|  |
| To construct your own regional ERP, use the data on GDP and ERP for countries in the Regional Weighted Averages Worksheet |

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
| Andorra (Principality of) |
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
| Cayman Islands |
| Cape Verde |
| Chile |
| China |
| Colombia |
| Congo (Democratic Republic of) |
| Congo (Republic of) |
| Cook Islands |
| Costa Rica |
| Côte d'Ivoire |
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
| Ethiopia |
| Fiji |
| Finland |
| France |
| Gabon |
| Georgia |
| Germany |
| Ghana |
| Greece |
| Guatemala |
| Guernsey (States of) |
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
| Jersey (States of) |
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
| Ras Al Khaimah (Emirate of) |
| Romania |
| Russia |
| Rwanda |
| Saudi Arabia |
| Senegal |
| Serbia |
| Sharjah |
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
| Turks and Caicos Islands |
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

| Country | GDP (in billions) | Moody's rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region | GDP Weight | Weigth*Default Spread | Weight*ERP | Weight*CRP |
|---|---|---|---|---|---|---|---|---|---|---|
| Angola | 124.2 | Ba2 | 0.03 | 0.1031 | 0.045 | Africa | 0.06799146000985383 | 0.0020397438002956146 | 0.00700991952701593 | 0.0030596157004434224 |
| Botswana | 14.8 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Africa | 0.00810204193354136 | 6.886735643510156e-05 | 0.0005740296709914053 | 0.00010330103465265234 |
| Burkina Faso | 11.6 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa | 0.006350249083045929 | 0.0004127661903979854 | 0.0009880987573219467 | 0.0006191492855969781 |
| Cameroon | 29.6 | B2 | 0.055 | 0.1406 | 0.0825 | Africa | 0.01620408386708272 | 0.0008912246126895495 | 0.00227829419171183 | 0.0013368369190343244 |
| Cape Verde | 4 | B2 | 0.055 | 0.1406 | 0.0825 | Africa | 0.002189741063119286 | 0.00012043575847156074 | 0.00030787759347457164 | 0.0001806536377073411 |
| Congo (Democratic Republic of) | 32.7 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa | 0.017901133191000167 | 0.0011635736574150109 | 0.002785416324519626 | 0.0017453604861225162 |
| Congo (Republic of) | 14.1 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa | 0.007718837247495483 | 0.00027787814090983736 | 0.0008652816554442437 | 0.00041681721136475604 |
| Côte d'Ivoire | 31.1 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.01702523676575245 | 0.0007661356544588602 | 0.0021383697377785078 | 0.0011492034816882905 |
| Egypt | 272 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa | 0.14890239229211144 | 0.009678655498987243 | 0.02316921224065254 | 0.014517983248480866 |
| Ethiopia | 47.5 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.026003175124541523 | 0.0011701428806043684 | 0.003265998795642415 | 0.0017552143209065528 |
| Gabon | 19.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa | 0.010565500629550556 | 0.00038035802266382 | 0.0011843926205726172 | 0.0005705370339957299 |
| Ghana | 48.1 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa | 0.026331636284009415 | 0.001711556358460612 | 0.004097202605791866 | 0.002567334537690918 |
| Kenya | 55.2 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.03021842667104615 | 0.0013598292001970767 | 0.003795434389883396 | 0.002039743800295615 |
| Morocco | 103.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Africa | 0.056823780587945474 | 0.0014205945146986369 | 0.0054323534242075875 | 0.0021308917720479557 |
| Mozambique | 15.6 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.008539990146165216 | 0.0003842995565774347 | 0.001072622762358351 | 0.0005764493348661521 |
| Namibia | 13.1 | Baa3 | 0.022 | 0.0911 | 0.033 | Africa | 0.007171401981715662 | 0.00015777084359774456 | 0.0006533147205342968 | 0.00023665626539661687 |
| Nigeria | 521.8 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa | 0.28565172168391084 | 0.01028346198062079 | 0.032021558000766406 | 0.015425192970931183 |
| Rwanda | 7.5 | B2 | 0.055 | 0.1406 | 0.0825 | Africa | 0.004105764493348661 | 0.00022581704713417635 | 0.0005772704877648218 | 0.0003387255707012646 |
| Senegal | 14.8 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.00810204193354136 | 0.0003645918870093612 | 0.0010176164668527948 | 0.0005468878305140418 |
| South Africa | 350.6 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Africa | 0.19193080418240543 | 0.003646685279465703 | 0.01662120764219631 | 0.005470027919198555 |
| Tunisia | 47 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa | 0.025729457491651612 | 0.000926260469699458 | 0.0028842721848141455 | 0.001389390704549187 |
| Uganda | 21.5 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.011769858214266163 | 0.0005296436196419774 | 0.00147829419171183 | 0.0007944654294629661 |
| Zambia | 26.8 | B1 | 0.045 | 0.1256 | 0.0675 | Africa | 0.014671265122899218 | 0.0006602069305304647 | 0.0018427108994361417 | 0.0009903103957956973 |
| Africa | 1826.7 |  | 0.038640499260962385 | 0.11606074889144358 | 0.05796074889144357 |  | 0.9999999999999998 |  |  |  |
| Bangladesh | 150 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Asia | 0.0069911817893696755 | 0.0002516825444173083 | 0.0007837114785883406 | 0.00037752381662596243 |
| Cambodia | 15.2 | B2 | 0.055 | 0.1406 | 0.0825 | Asia | 0.0007084397546561271 | 3.896418650608699e-05 | 9.960662950465147e-05 | 5.844627975913049e-05 |
| China | 9240.3 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia | 0.4306707805887507 | 0.0025840246835325043 | 0.02889800937750517 | 0.0038760370252987567 |
| Fiji | 3.9 | B1 | 0.045 | 0.1256 | 0.0675 | Asia | 0.00018177072652361155 | 8.17968269356252e-06 | 2.2830403251365608e-05 | 1.226952404034378e-05 |
| Hong Kong | 274 | Aa1 | 0.004 | 0.0641 | 0.006 | Asia | 0.012770558735248608 | 5.108223494099443e-05 | 0.0008185928149294358 | 7.662335241149165e-05 |
| India | 1876.8 | Baa3 | 0.022 | 0.0911 | 0.033 | Asia | 0.08747366654859338 | 0.0019244206640690543 | 0.007968851022576858 | 0.002886630996103582 |
| Indonesia | 868.4 | Baa3 | 0.022 | 0.0911 | 0.033 | Asia | 0.04047428177259084 | 0.0008904341989969984 | 0.0036872070694830253 | 0.0013356512984954978 |
| Japan | 4919.6 | A1 | 0.007 | 0.0686 | 0.0105 | Asia | 0.22929211953988707 | 0.0016050448367792094 | 0.01572943940043625 | 0.0024075672551688142 |
| Korea | 1304.6 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia | 0.060804638416077854 | 0.00036482783049646714 | 0.004079991237718824 | 0.0005472417457447008 |
| Macao | 51.8 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Asia | 0.002414288111262328 | 1.207144055631164e-05 | 0.0001583773000988087 | 1.810716083446746e-05 |
| Malaysia | 313.2 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Asia | 0.014597587576203882 | 0.00017517105091444658 | 0.0011108764145491155 | 0.0002627565763716699 |
| Mauritius | 11.9 | Baa1 | 0.016 | 0.0821 | 0.024 | Asia | 0.0005546337552899943 | 8.87414008463991e-06 | 4.553543130930854e-05 | 1.3311210126959864e-05 |
| Mongolia | 11.5 | B2 | 0.055 | 0.1406 | 0.0825 | Asia | 0.0005359906038516751 | 2.9479483211842132e-05 | 7.536027890154552e-05 | 4.42192248177632e-05 |
| Pakistan | 232.3 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Asia | 0.010827010197803837 | 0.0007037556628572495 | 0.0016846827867782774 | 0.0010556334942858742 |
| Papua New Guinea | 15.3 | B1 | 0.045 | 0.1256 | 0.0675 | Asia | 0.000713100542515707 | 3.208952441320681e-05 | 8.956542813997279e-05 | 4.8134286619810226e-05 |
| Philippines | 272.1 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Asia | 0.012682003765916593 | 0.00024095807155241527 | 0.0010982615261283769 | 0.00036143710732862287 |
| Singapore | 297.9 | Aaa | 0 | 0.0581 | 0 | Asia | 0.013884487033688175 | 0 | 0.0008066886966572829 | 0 |
| Sri Lanka | 67.2 | B1 | 0.045 | 0.1256 | 0.0675 | Asia | 0.003132049441637615 | 0.00014094222487369266 | 0.0003933854098696844 | 0.00021141333731053901 |
| Taiwan | 970.9 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia | 0.04525158932866012 | 0.00027150953597196073 | 0.003036381643953094 | 0.00040726430395794113 |
| Thailand | 387.3 | Baa1 | 0.016 | 0.0821 | 0.024 | Asia | 0.018051231380152504 | 0.0002888197020824401 | 0.0014820060963105207 | 0.0004332295531236601 |
| Vietnam | 171.4 | B1 | 0.045 | 0.1256 | 0.0675 | Asia | 0.00798859039131975 | 0.0003594865676093887 | 0.0010033669531497604 | 0.0005392298514140831 |
| Asia | 21455.6 |  | 0.009981818266559778 | 0.07307272739983968 | 0.014972727399839672 |  | 0.9999999999999999 |  |  |  |
| Australia | 1560.4 | Aaa | 0 | 0.0581 | 0 | Australia & New Zealand | 0.8929838617374385 | 0 | 0.05188236236694518 | 0 |
| Cook Islands | 1.2 | B1 | 0.045 | 0.1256 | 0.0675 | Australia & New Zealand | 0.0006867345770859562 | 3.090305596886803e-05 | 8.62538628819961e-05 | 4.6354583953302045e-05 |
| New Zealand | 185.8 | Aaa | 0 | 0.0581 | 0 | Australia & New Zealand | 0.10632940368547557 | 0 | 0.006177738354126131 | 0 |
| Australia & New Zealand | 1747.4 |  | 3.090305596886803e-05 | 0.05814635458395331 | 4.6354583953302045e-05 |  |  |  |  |  |
| Aruba | 2.6 | Baa1 | 0.016 | 0.0821 | 0.024 | Caribbean | 0.013839577999329314 | 0.00022143324798926903 | 0.0011362293537449369 | 0.00033214987198390355 |
| Bahamas | 8.4 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Caribbean | 0.04471248276706394 | 0.0008495371725742148 | 0.0038721010076277367 | 0.0012743057588613222 |
| Barbados | 3.7 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Caribbean | 0.01969478407596864 | 0.0012801609649379618 | 0.0030645084022207208 | 0.0019202414474069425 |
| Bermuda | 5.557 | A1 | 0.007 | 0.0686 | 0.0105 | Caribbean | 0.029579436516258845 | 0.00020705605561381193 | 0.0020291493450153566 | 0.0003105840834207179 |
| Cayman Islands | 1.897 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Caribbean | 0.010097569024895272 | 6.0585414149371634e-05 | 0.0006775468815704727 | 9.087812122405746e-05 |
| Cuba | 60.8 | Caa2 | 0.09 | 0.1931 | 0.135 | Caribbean | 0.32363320859970085 | 0.029126988773973076 | 0.06249357258060223 | 0.043690483160959616 |
| Curacao | 1 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Caribbean | 0.0053229146151266594 | 6.387497538151992e-05 | 0.0004050738022111388 | 9.581246307227989e-05 |
| Dominican Republic | 61.2 | B1 | 0.045 | 0.1256 | 0.0675 | Caribbean | 0.32576237444575157 | 0.01465930685005882 | 0.040915754230386396 | 0.021988960275088232 |
| Jamaica | 14.4 | Caa2 | 0.09 | 0.1931 | 0.135 | Caribbean | 0.07664997045782389 | 0.00689849734120415 | 0.014801109295405792 | 0.010347746011806226 |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.0911 | 0.033 | Caribbean | 0.00798437192268999 | 0.00017565618229917974 | 0.000727376282157058 | 0.0002634842734487697 |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.0821 | 0.024 | Caribbean | 0.00798437192268999 | 0.00012774995076303983 | 0.0006555169348528482 | 0.00019162492614455975 |
| St. Vincent & the Grenadines | 0.713 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Caribbean | 0.0037952381205853076 | 0.000246690477838045 | 0.000590539051563074 | 0.0003700357167570675 |
| Trinidad and Tobago | 24.6 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Caribbean | 0.13094369953211582 | 0.0024879302911102004 | 0.01133972437948123 | 0.0037318954366653005 |
| Caribbean | 187.867 |  | 0.05640546769789266 | 0.14270820154683897 | 0.084608201546839 |  |  |  |  | 0.084608201546839 |
| Argentina | 609.9 | Caa1 | 0.075 | 0.17059999999999997 | 0.11249999999999999 | Central and South America | 0.10461765412192528 | 0.007846324059144396 | 0.01784777179320045 | 0.011769486088716592 |
| Belize | 1.6 | Caa2 | 0.09 | 0.1931 | 0.135 | Central and South America | 0.0002744519537548458 | 2.4700675837936122e-05 | 5.2996672270060725e-05 | 3.705101375690419e-05 |
| Bolivia | 30.6 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America | 0.005248893615561426 | 0.0001889601701602113 | 0.0005884009743044357 | 0.00028344025524031693 |
| Brazil | 2245.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America | 0.3852104703420357 | 0.007318998936498678 | 0.03335922673162029 | 0.010978498404748016 |
| Chile | 277.2 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Central and South America | 0.04754880098802703 | 0.0002852928059281622 | 0.0031905245462966136 | 0.0004279392088922433 |
| Colombia | 378.4 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America | 0.06490788706302103 | 0.0012332498541973995 | 0.005621023019657621 | 0.0018498747812960993 |
| Costa Rica | 49.6 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America | 0.00850801056640022 | 0.00021270026416000552 | 0.000813365810147861 | 0.0003190503962400083 |
| Ecuador | 94.5 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America | 0.01620981851864558 | 0.0010536382037119626 | 0.0025222477615012523 | 0.001580457305567944 |
| El Salvador | 24.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America | 0.00416823904765172 | 0.00015005660571546192 | 0.00046725959724175776 | 0.00022508490857319285 |
| Guatemala | 53.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America | 0.009228446945006689 | 0.00023071117362516723 | 0.0008822395279426395 | 0.00034606676043775087 |
| Honduras | 18.6 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America | 0.0031905039624000823 | 0.00020738275755600535 | 0.0004964424165494529 | 0.00031107413633400804 |
| Mexico | 1260.9 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Central and South America | 0.21628529280592818 | 0.002595423513671138 | 0.016459310782531135 | 0.0038931352705067076 |
| Nicaragua | 11.3 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America | 0.0019383169233935984 | 0.0001259906000205839 | 0.0003016021132800439 | 0.00018898590003087586 |
| Panama | 42.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America | 0.007324436515832447 | 0.0001391642938008165 | 0.0006342962022710899 | 0.00020874644070122472 |
| Paraguay | 29 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America | 0.00497444166180658 | 0.0001243610415451645 | 0.00047555662286870906 | 0.00018654156231774676 |
| Peru | 202.4 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Central and South America | 0.03471817214998799 | 0.0004166180657998559 | 0.002642052900614086 | 0.000624927098699784 |
| Suriname | 5.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America | 0.0009091220968129267 | 3.2728395485265355e-05 | 0.00010191258705272907 | 4.9092593227898035e-05 |
| Uruguay | 55.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America | 0.00955435864009057 | 0.00018153281416172083 | 0.0008274074582318433 | 0.0002722992212425812 |
| Venezuela | 438.3 | Caa3 | 0.1 | 0.2081 | 0.15000000000000002 | Central and South America | 0.07518268208171806 | 0.007518268208171807 | 0.015645516141205528 | 0.011277402312257712 |
| Central and South America | 5829.8 |  | 0.029886102439191743 | 0.1029291536587876 | 0.0448291536587876 |  | 1 |  |  |  |
| Albania | 12.9 | B1 | 0.045 | 0.1256 | 0.0675 | Eastern Europe & Russia | 0.003010993627897207 | 0.0001354947132553743 | 0.00037818079966388913 | 0.00020324206988306149 |
| Armenia | 10.4 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.002427467731017903 | 8.73888383166445e-05 | 0.00027211913264710687 | 0.00013108325747496674 |
| Azerbaijan | 73.4 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia | 0.017132320332376355 | 0.0003769110473122798 | 0.001560754382279486 | 0.0005653665709684198 |
| Belarus | 71.7 | Caa1 | 0.075 | 0.17059999999999997 | 0.11249999999999999 | Eastern Europe & Russia | 0.01673552272249843 | 0.001255164204187382 | 0.0028550801764582316 | 0.001882746306281073 |
| Bosnia and Herzegovina | 17.9 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Eastern Europe & Russia | 0.004178045421655814 | 0.0002715729524076279 | 0.0006501038676096447 | 0.00040735942861144184 |
| Bulgaria | 54.5 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Eastern Europe & Russia | 0.012720864551968818 | 0.00024169642648740755 | 0.0011016268702004996 | 0.00036254463973111126 |
| Croatia | 57.9 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia | 0.013514459771724672 | 0.0003378614942931168 | 0.0012919823541768787 | 0.0005067922414396753 |
| Czech Republic | 208.9 | A1 | 0.007 | 0.0686 | 0.0105 | Eastern Europe & Russia | 0.04875942394323461 | 0.0003413159676026423 | 0.003344896482505894 | 0.0005119739514039634 |
| Estonia | 24.9 | A1 | 0.007 | 0.0686 | 0.0105 | Eastern Europe & Russia | 0.005811917932917863 | 4.068342553042505e-05 | 0.00039869757019816537 | 6.102513829563757e-05 |
| Georgia | 16.1 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0037579067759027154 | 0.00013528464393249774 | 0.00042126134957869437 | 0.0002029269658987466 |
| Hungary | 133.4 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia | 0.03113694185747964 | 0.000778423546436991 | 0.002976691641575054 | 0.0011676353196554867 |
| Kazakhstan | 321.9 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Eastern Europe & Russia | 0.07513479448217912 | 0.0014275610951614032 | 0.006506673202156712 | 0.002141341642742105 |
| Latvia | 31 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Eastern Europe & Russia | 0.007235721121303365 | 8.682865345564038e-05 | 0.000550638377331186 | 0.00013024298018346058 |
| Lithuania | 45.9 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Eastern Europe & Russia | 0.010713535466704014 | 0.00012856242560044817 | 0.0008153000490161755 | 0.00019284363840067227 |
| Macedonia | 10.2 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0023807856592675584 | 8.570828373363209e-05 | 0.0002668860724038933 | 0.00012856242560044812 |
| Moldova | 8 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Eastern Europe & Russia | 0.0018672828700137716 | 0.00012137338655089515 | 0.0002905492145741429 | 0.00018206007982634275 |
| Montenegro | 4.4 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0010270055785075744 | 3.6972200826272676e-05 | 0.00011512732535069908 | 5.545830123940901e-05 |
| Poland | 525.9 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Eastern Europe & Russia | 0.1227505076675303 | 0.0010433793151740076 | 0.008696873468244522 | 0.0015650689727610115 |
| Romania | 189.6 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia | 0.044254604019326384 | 0.0009736012884251804 | 0.004031594426160633 | 0.0014604019326377707 |
| Russia | 2096.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia | 0.48941484023060955 | 0.012235371005765239 | 0.04678805872604627 | 0.01835305650864786 |
| Serbia | 45.5 | B1 | 0.045 | 0.1256 | 0.0675 | Eastern Europe & Russia | 0.010620171323203326 | 0.0004779077095441497 | 0.0013338935181943378 | 0.0007168615643162246 |
| Slovakia | 97.7 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Eastern Europe & Russia | 0.022804192050043186 | 0.0001938356324253671 | 0.0016156770067455597 | 0.00029075344863805063 |
| Slovenia | 48 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia | 0.01120369722008263 | 0.00024648133884181783 | 0.0010206568167495276 | 0.0003697220082627268 |
| Ukraine | 177.4 | Ca | 0.12 | 0.23809999999999998 | 0.18 | Eastern Europe & Russia | 0.041406997642555385 | 0.004968839717106646 | 0.009859006138692436 | 0.007453259575659969 |
| Eastern Europe & Russia | 4284.299999999999 |  | 0.02602821931237309 | 0.09714232896855964 | 0.039042328968559636 |  | 1.0000000000000002 |  |  |  |
| Abu Dhabi | 390 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East | 0.16198704103671704 | 0.0008099352051835852 | 0.010626349892008637 | 0.0012149028077753777 |
| Bahrain | 32.9 | Baa3 | 0.022 | 0.0911 | 0.033 | Middle East | 0.013665060641302539 | 0.0003006313341086558 | 0.0012448870244226612 | 0.0004509470011629838 |
| Israel | 290.6 | A1 | 0.007 | 0.0686 | 0.0105 | Middle East | 0.12070111314171789 | 0.0008449077919920252 | 0.008280096361521846 | 0.001267361687988038 |
| Jordan | 33.7 | B1 | 0.045 | 0.1256 | 0.0675 | Middle East | 0.013997341751121448 | 0.0006298803788004652 | 0.0017580661239408536 | 0.0009448205682006978 |
| Kuwait | 175.8 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East | 0.07301877388270477 | 0.00036509386941352385 | 0.004790031566705432 | 0.0005476408041202857 |
| Lebanon | 44.4 | B2 | 0.055 | 0.1406 | 0.0825 | Middle East | 0.018441601594949324 | 0.0010142880877222129 | 0.002592889184249875 | 0.0015214321315833194 |
| Oman | 80 | A1 | 0.007 | 0.0686 | 0.0105 | Middle East | 0.03322811098189067 | 0.0002325967768732347 | 0.0022794484133577 | 0.00034889516530985207 |
| Qatar | 203.2 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East | 0.0843994018940023 | 0.0004219970094700115 | 0.005536600764246551 | 0.0006329955142050172 |
| Ras Al Khaimah (Emirate of) | 5.2 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Middle East | 0.002159827213822894 | 1.8358531317494598e-05 | 0.00015302375809935203 | 2.75377969762419e-05 |
| Saudi Arabia | 748.5 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Middle East | 0.3108905133743146 | 0.0018653430802458876 | 0.02086075344741651 | 0.002798014620368832 |
| Sharjah | 1 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Middle East | 0.0004153513872736334 | 4.9842166472836015e-06 | 3.1608240571523504e-05 | 7.476324970925403e-06 |
| United Arab Emirates | 402.3 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East | 0.16709586310018273 | 0.0008354793155009137 | 0.010961488619371986 | 0.0012532189732513705 |
| Middle East | 2407.6000000000004 |  | 0.007343495597275294 | 0.06911524339591292 | 0.011015243395912942 |  | 1 |  |  |  |
| Canada | 1826.8 | Aaa | 0 | 0.0581 | 0 | North America | 0.09824040612631216 | 0 | 0.005707767595938737 | 0 |
| United States of America | 16768.4 | Aaa | 0 | 0.0581 | 0 | North America | 0.9017595938736879 | 0 | 0.05239223240406127 | 0 |
| North America | 18595.2 |  | 0 | 0.058100000000000006 | 0 |  |  |  |  |  |
| Andorra (Principality of) | 4.5 | Baa1 | 0.016 | 0.0821 | 0.024 | Western Europe | 0.00024201693688305853 | 3.872270990128936e-06 | 1.9869590518099106e-05 | 5.808406485193405e-06 |
| Austria | 428.3 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.023034634237114215 | 0 | 0.001338312249176336 | 0 |
| Belgium | 524.8 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Western Europe | 0.02822455299471758 | 0.00016934731796830547 | 0.0018938675059455494 | 0.00025402097695245826 |
| Cyprus | 21.9 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Western Europe | 0.0011778157594975515 | 7.655802436734085e-05 | 0.00018326813217781903 | 0.00011483703655101127 |
| Denmark | 335.9 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.018065219799782078 | 0 | 0.0010495892703673386 | 0 |
| Finland | 267.3 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.014375806050853677 | 0 | 0.0008352343315545986 | 0 |
| France | 2806.4 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe | 0.15093251814858122 | 0.0006037300725943249 | 0.009674774413324056 | 0.0009055951088914873 |
| Germany | 3730.3 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.20062128436774962 | 0 | 0.011656096621766253 | 0 |
| Greece | 242.2 | Caa2 | 0.09 | 0.1931 | 0.135 | Western Europe | 0.013025889358461504 | 0.0011723300422615353 | 0.0025152992351189164 | 0.0017584950633923032 |
| Guernsey (States of) | 0.5 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe | 2.689077076478428e-05 | 1.0756308305913713e-07 | 1.7236984060226726e-06 | 1.613446245887057e-07 |
| Iceland | 15.3 | Baa3 | 0.022 | 0.0911 | 0.033 | Western Europe | 0.000822857585402399 | 1.810286687885278e-05 | 7.496232603015855e-05 | 2.715430031827917e-05 |
| Ireland | 232.1 | Baa1 | 0.016 | 0.0821 | 0.024 | Western Europe | 0.012482695789012862 | 0.0001997231326242058 | 0.0010248293242779562 | 0.0002995846989363087 |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe | 7.529415814139598e-05 | 3.011766325655839e-07 | 4.826355536863482e-06 | 4.517649488483759e-07 |
| Italy | 2149.5 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Western Europe | 0.11560342351780761 | 0.0021964650468383447 | 0.010011256476642139 | 0.0032946975702575166 |
| Jersey (States of) | 1 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe | 5.378154152956856e-05 | 2.1512616611827426e-07 | 3.447396812045345e-06 | 3.226892491774114e-07 |
| Liechtenstein | 10.5 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.0005647061860604699 | 0 | 3.28094294101133e-05 | 0 |
| Luxembourg | 60.1 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.0032322706459270707 | 0 | 0.0001877949245283628 | 0 |
| Malta | 9.6 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Western Europe | 0.0005163027986838581 | 6.195633584206298e-06 | 3.92906429798416e-05 | 9.293450376309447e-06 |
| Netherlands | 853.54 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.045904696957147946 | 0 | 0.0026670628932102956 | 0 |
| Norway | 512.6 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.027568418188056845 | 0 | 0.0016017250967261026 | 0 |
| Portugal | 227.3 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Western Europe | 0.012224544389670935 | 0.0003056136097417734 | 0.0011686664436525414 | 0.00045842041461266014 |
| Spain | 1393 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Western Europe | 0.074917687350689 | 0.001423436059663091 | 0.006487871724569667 | 0.0021351540894946363 |
| Sweden | 579.7 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.031177159624690896 | 0 | 0.001811392974194541 | 0 |
| Switzerland | 685.4 | Aaa | 0 | 0.0581 | 0 | Western Europe | 0.03686186856436629 | 0 | 0.0021416745635896815 | 0 |
| Turkey | 822.1 | Baa3 | 0.022 | 0.0911 | 0.033 | Western Europe | 0.04421380529145831 | 0.0009727037164120828 | 0.004027877662051852 | 0.0014590555746181243 |
| United Kingdom | 2678.5 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe | 0.1440538589869494 | 0.0005762154359477975 | 0.009233852361063456 | 0.0008643231539216963 |
| Western Europe | 18593.739999999998 |  | 0.007724917095753732 | 0.0696873756436306 | 0.0115873756436306 |  | 1 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| Region | Weighted Average: TRP | Weighted Average: CRP | Weighted Average: Default Spreads | Total GDP | Weight | Weight *ERP | Weight*CRP | Weight*Default Spread |  |  |
| Africa | 0.11606074889144358 | 0.05796074889144357 | 0.038640499260962385 | 1826.7 | 0.0243793368764316 | 0.002829484095355438 | 0.001413044622834762 | 0.0009420297485565083 |  |  |
| Asia | 0.07307272739983968 | 0.014972727399839672 | 0.009981818266559778 | 21455.6 | 0.28634877116437607 | 0.020924285696573525 | 0.004287422091923274 | 0.0028582813946155146 |  |  |
| Australia & New Zealand | 0.05814635458395331 | 4.6354583953302045e-05 | 3.090305596886803e-05 | 1747.4 | 0.023320990451566527 | 0.0013560305800457766 | 1.081034809761296e-06 | 7.206898731741972e-07 |  |  |
| Caribbean | 0.14270820154683897 | 0.084608201546839 | 0.05640546769789266 | 187.867 | 0.002507293414881795 | 0.00035781133398801333 | 0.00021213758658338112 | 0.00014142505772225407 |  |  |
| Central and South America | 0.1029291536587876 | 0.0448291536587876 | 0.029886102439191743 | 5829.8 | 0.07780514486353585 | 0.00800841771110311 | 0.003487938794531677 | 0.0023252925296877855 |  |  |
| Eastern Europe & Russia | 0.09714232896855964 | 0.039042328968559636 | 0.02602821931237309 | 4284.299999999999 | 0.057178733771115056 | 0.0055544753659993494 | 0.0022323909338975646 | 0.0014882606225983764 |  |  |
| Middle East | 0.06911524339591292 | 0.011015243395912942 | 0.007343495597275294 | 2407.6000000000004 | 0.032132091456559216 | 0.0022208173218398243 | 0.0003539428082137346 | 0.00023596187214248968 |  |  |
| North America | 0.058100000000000006 | 0 | 0 | 18595.2 | 0.2481735616601636 | 0.014418883932455507 | 0 | 0 |  |  |
| Western Europe | 0.0696873756436306 | 0.0115873756436306 | 0.007724917095753732 | 18593.739999999998 | 0.24815407634137035 | 0.017293206335499262 | 0.0028754545000656434 | 0.0019169696667104285 |  |  |
| Global | 0.07296341237285982 | 0.014863412372859796 | 0.009908941581906531 | 74928.207 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| For updating industry average spreadsheets |  |  |  |  |  |  |  |  |  |  |
|  | ERP | Default Spread | Tax rate |  |  |  |  |  |  |  |
| Africa & Mid East | 0.08936778924497554 | 0.020845192829983702 | 0.2785 |  |  |  |  |  |  |  |
| Australia, NZ & Canada | 0.0575 | 0 | 0.3 |  |  |  |  |  |  |  |
| Latin America & Caribbean | 0.10417102536581037 | 0.031114016910540245 | 0.2715 |  |  |  |  |  |  |  |
| Japan | 0.0686 | 0.007 | 0.3564 |  |  |  |  |  |  |  |
| US | 0.0581 | 0 | 0.4 |  |  |  |  |  |  |  |
| Europe | 0.0696873756436306 | 0.007724917095753732 | 0.3 |  |  |  |  |  |  |  |
| Emerging Markets | 0.08534292337601247 | 0.018561948917341645 | 0.25 |  |  |  |  |  |  |  |
| Small Asia (No India, China & Japan) | 0.08107439517245202 | 0.015716263448301345 | 0.2 |  |  |  |  |  |  |  |
| India | 0.0905 | 0.022 | 0.34 |  |  |  |  |  |  |  |
| China | 0.06709999999999999 | 0.006 | 0.25 |  |  |  |  |  |  |  |
| Global | 0.07296341237285982 | 0.009908941581906531 | 0.3 |  |  |  |  |  |  |  |

## Regional breakdown

| Country | GDP (in billions) | Moody's rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|
| Abu Dhabi | 390 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East |
| Albania | 12.9 | B1 | 0.045 | 0.1256 | 0.0675 | Eastern Europe & Russia |
| Andorra (Principality of) | 4.5 | Baa1 | 0.016 | 0.0821 | 0.024 | Western Europe |
| Angola | 124.2 | Ba2 | 0.03 | 0.1031 | 0.045 | Africa |
| Argentina | 609.9 | Caa1 | 0.075 | 0.17059999999999997 | 0.11249999999999999 | Central and South America |
| Armenia | 10.4 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Aruba | 2.6 | Baa1 | 0.016 | 0.0821 | 0.024 | Caribbean |
| Australia | 1560.4 | Aaa | 0 | 0.0581 | 0 | Australia & New Zealand |
| Austria | 428.3 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Azerbaijan | 73.4 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia |
| Bahamas | 8.4 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Caribbean |
| Bahrain | 32.9 | Baa3 | 0.022 | 0.0911 | 0.033 | Middle East |
| Bangladesh | 150 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Asia |
| Barbados | 3.7 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Caribbean |
| Belarus | 71.7 | Caa1 | 0.075 | 0.17059999999999997 | 0.11249999999999999 | Eastern Europe & Russia |
| Belgium | 524.8 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Western Europe |
| Belize | 1.6 | Caa2 | 0.09 | 0.1931 | 0.135 | Central and South America |
| Bermuda | 5.557 | A1 | 0.007 | 0.0686 | 0.0105 | Caribbean |
| Bolivia | 30.6 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America |
| Bosnia and Herzegovina | 17.9 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Eastern Europe & Russia |
| Botswana | 14.8 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Africa |
| Brazil | 2245.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America |
| Bulgaria | 54.5 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Eastern Europe & Russia |
| Burkina Faso | 11.6 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa |
| Cambodia | 15.2 | B2 | 0.055 | 0.1406 | 0.0825 | Asia |
| Cameroon | 29.6 | B2 | 0.055 | 0.1406 | 0.0825 | Africa |
| Canada | 1826.8 | Aaa | 0 | 0.0581 | 0 | North America |
| Cayman Islands | 1.897 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Caribbean |
| Cape Verde | 4 | B2 | 0.055 | 0.1406 | 0.0825 | Africa |
| Chile | 277.2 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Central and South America |
| China | 9240.3 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia |
| Colombia | 378.4 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America |
| Congo (Democratic Republic of) | 32.7 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa |
| Congo (Republic of) | 14.1 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa |
| Cook Islands | 1.2 | B1 | 0.045 | 0.1256 | 0.0675 | Australia & New Zealand |
| Costa Rica | 49.6 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America |
| Côte d'Ivoire | 31.1 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Croatia | 57.9 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia |
| Cuba | 60.8 | Caa2 | 0.09 | 0.1931 | 0.135 | Caribbean |
| Curacao | 1 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Caribbean |
| Cyprus | 21.9 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Western Europe |
| Czech Republic | 208.9 | A1 | 0.007 | 0.0686 | 0.0105 | Eastern Europe & Russia |
| Denmark | 335.9 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Dominican Republic | 61.2 | B1 | 0.045 | 0.1256 | 0.0675 | Caribbean |
| Ecuador | 94.5 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America |
| Egypt | 272 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa |
| El Salvador | 24.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America |
| Estonia | 24.9 | A1 | 0.007 | 0.0686 | 0.0105 | Eastern Europe & Russia |
| Ethiopia | 47.5 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Fiji | 3.9 | B1 | 0.045 | 0.1256 | 0.0675 | Asia |
| Finland | 267.3 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| France | 2806.4 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe |
| Gabon | 19.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa |
| Georgia | 16.1 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Germany | 3730.3 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Ghana | 48.1 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Africa |
| Greece | 242.2 | Caa2 | 0.09 | 0.1931 | 0.135 | Western Europe |
| Guatemala | 53.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America |
| Guernsey (States of) | 0.5 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe |
| Honduras | 18.6 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America |
| Hong Kong | 274 | Aa1 | 0.004 | 0.0641 | 0.006 | Asia |
| Hungary | 133.4 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia |
| Iceland | 15.3 | Baa3 | 0.022 | 0.0911 | 0.033 | Western Europe |
| India | 1876.8 | Baa3 | 0.022 | 0.0911 | 0.033 | Asia |
| Indonesia | 868.4 | Baa3 | 0.022 | 0.0911 | 0.033 | Asia |
| Ireland | 232.1 | Baa1 | 0.016 | 0.0821 | 0.024 | Western Europe |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe |
| Israel | 290.6 | A1 | 0.007 | 0.0686 | 0.0105 | Middle East |
| Italy | 2149.5 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Western Europe |
| Jamaica | 14.4 | Caa2 | 0.09 | 0.1931 | 0.135 | Caribbean |
| Japan | 4919.6 | A1 | 0.007 | 0.0686 | 0.0105 | Asia |
| Jersey (States of) | 1 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe |
| Jordan | 33.7 | B1 | 0.045 | 0.1256 | 0.0675 | Middle East |
| Kazakhstan | 321.9 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Eastern Europe & Russia |
| Kenya | 55.2 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Korea | 1304.6 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia |
| Kuwait | 175.8 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East |
| Latvia | 31 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Eastern Europe & Russia |
| Lebanon | 44.4 | B2 | 0.055 | 0.1406 | 0.0825 | Middle East |
| Liechtenstein | 10.5 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Lithuania | 45.9 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Eastern Europe & Russia |
| Luxembourg | 60.1 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Macao | 51.8 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Asia |
| Macedonia | 10.2 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Malaysia | 313.2 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Asia |
| Malta | 9.6 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Western Europe |
| Mauritius | 11.9 | Baa1 | 0.016 | 0.0821 | 0.024 | Asia |
| Mexico | 1260.9 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Central and South America |
| Moldova | 8 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Eastern Europe & Russia |
| Mongolia | 11.5 | B2 | 0.055 | 0.1406 | 0.0825 | Asia |
| Montenegro | 4.4 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.0911 | 0.033 | Caribbean |
| Morocco | 103.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Africa |
| Mozambique | 15.6 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Namibia | 13.1 | Baa3 | 0.022 | 0.0911 | 0.033 | Africa |
| Netherlands | 853.54 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| New Zealand | 185.8 | Aaa | 0 | 0.0581 | 0 | Australia & New Zealand |
| Nicaragua | 11.3 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Central and South America |
| Nigeria | 521.8 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa |
| Norway | 512.6 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Oman | 80 | A1 | 0.007 | 0.0686 | 0.0105 | Middle East |
| Pakistan | 232.3 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Asia |
| Panama | 42.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America |
| Papua New Guinea | 15.3 | B1 | 0.045 | 0.1256 | 0.0675 | Asia |
| Paraguay | 29 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Central and South America |
| Peru | 202.4 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Central and South America |
| Philippines | 272.1 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Asia |
| Poland | 525.9 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Eastern Europe & Russia |
| Portugal | 227.3 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Western Europe |
| Qatar | 203.2 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East |
| Ras Al Khaimah (Emirate of) | 5.2 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Middle East |
| Romania | 189.6 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia |
| Russia | 2096.8 | Ba1 | 0.025 | 0.0956 | 0.037500000000000006 | Eastern Europe & Russia |
| Rwanda | 7.5 | B2 | 0.055 | 0.1406 | 0.0825 | Africa |
| Saudi Arabia | 748.5 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Middle East |
| Senegal | 14.8 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Serbia | 45.5 | B1 | 0.045 | 0.1256 | 0.0675 | Eastern Europe & Russia |
| Sharjah | 1 | A3 | 0.012 | 0.0761 | 0.018000000000000002 | Middle East |
| Singapore | 297.9 | Aaa | 0 | 0.0581 | 0 | Asia |
| Slovakia | 97.7 | A2 | 0.0085 | 0.07085 | 0.012750000000000001 | Eastern Europe & Russia |
| Slovenia | 48 | Baa3 | 0.022 | 0.0911 | 0.033 | Eastern Europe & Russia |
| South Africa | 350.6 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Africa |
| Spain | 1393 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Western Europe |
| Sri Lanka | 67.2 | B1 | 0.045 | 0.1256 | 0.0675 | Asia |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.0821 | 0.024 | Caribbean |
| St. Vincent & the Grenadines | 0.713 | B3 | 0.065 | 0.15560000000000002 | 0.0975 | Caribbean |
| Suriname | 5.3 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Central and South America |
| Sweden | 579.7 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Switzerland | 685.4 | Aaa | 0 | 0.0581 | 0 | Western Europe |
| Taiwan | 970.9 | Aa3 | 0.006 | 0.06709999999999999 | 0.009000000000000001 | Asia |
| Thailand | 387.3 | Baa1 | 0.016 | 0.0821 | 0.024 | Asia |
| Trinidad and Tobago | 24.6 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Caribbean |
| Tunisia | 47 | Ba3 | 0.036 | 0.11209999999999999 | 0.05399999999999999 | Africa |
| Turkey | 822.1 | Baa3 | 0.022 | 0.0911 | 0.033 | Western Europe |
| Turks and Caicos Islands | 1.5 | Baa1 | 0.016 | 0.0821 | 0.024 | Caribbean |
| Uganda | 21.5 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |
| Ukraine | 177.4 | Ca | 0.12 | 0.23809999999999998 | 0.18 | Eastern Europe & Russia |
| United Arab Emirates | 402.3 | Aa2 | 0.005 | 0.06559999999999999 | 0.0075 | Middle East |
| United Kingdom | 2678.5 | Aa1 | 0.004 | 0.0641 | 0.006 | Western Europe |
| United States of America | 16768.4 | Aaa | 0 | 0.0581 | 0 | North America |
| Uruguay | 55.7 | Baa2 | 0.019 | 0.0866 | 0.028499999999999998 | Central and South America |
| Venezuela | 438.3 | Caa3 | 0.1 | 0.2081 | 0.15000000000000002 | Central and South America |
| Vietnam | 171.4 | B1 | 0.045 | 0.1256 | 0.0675 | Asia |
| Zambia | 26.8 | B1 | 0.045 | 0.1256 | 0.0675 | Africa |

## Sovereign Ratings (Moody's,S&P)

| Country | S&P Rating | Moody's rating |
|---|---|---|
| Abu Dhabi | AA | Aa2 |
| Albania | B | B1 |
| Andorra (Principality of) | BBB+ | Baa1 |
| Angola | BB- | Ba2 |
| Argentina | CCC+ | Caa1 |
| Armenia | NA | Ba3 |
| Aruba | BBB+ | Baa1 |
| Australia | AAA | Aaa |
| Austria | AA+ | Aaa |
| Azerbaijan | BBB- | Baa3 |
| Bahamas | BBB | Baa2 |
| Bahrain | BBB | Baa3 |
| Bangladesh | BB- | Ba3 |
| Barbados | B | B3 |
| Belarus | B- | Caa1 |
| Belgium | AA | Aa3 |
| Belize | B- | Caa2 |
| Bermuda | AA- | A1 |
| Bolivia | BB | Ba3 |
| Bosnia and Herzegovina | B | B3 |
| Botswana | A- | A2 |
| Brazil | BBB+ | Baa2 |
| Bulgaria | BB+ | Baa2 |
| Burkina Faso | B- | B3 |
| Cambodia | NA | B2 |
| Cameroon | B | B2 |
| Canada | AAA | Aaa |
| Cayman Islands | NA | Aa3 |
| Cape Verde | B | B2 |
| Chile | AA+ | Aa3 |
| China | AA- | Aa3 |
| Colombia | BBB+ | Baa2 |
| Congo (Democratic Republic of) | B- | B3 |
| Congo (Republic of) | B+ | Ba3 |
| Cook Islands | B+ | B1 |
| Costa Rica | BB | Ba1 |
| Côte d'Ivoire | NA | B1 |
| Croatia | BB | Ba1 |
| Cuba | NA | Caa2 |
| Curacao | A- | A3 |
| Cyprus | B+ | B3 |
| Czech Republic | AA | A1 |
| Denmark | AAA | Aaa |
| Dominican Republic | B+ | B1 |
| Ecuador | B+ | B3 |
| Egypt | B- | B3 |
| El Salvador | B+ | Ba3 |
| Estonia | AA- | A1 |
| Ethiopia | B | B1 |
| Fiji | B | B1 |
| Finland | AA+ | Aaa |
| France | AA | Aa1 |
| Gabon | BB- | Ba3 |
| Georgia | BB- | Ba3 |
| Germany | AAA | Aaa |
| Ghana | B- | B3 |
| Greece | B | Caa2 |
| Guatemala | BB+ | Ba1 |
| Guernsey (States of) | AA+ | Aa1 |
| Honduras | B | B3 |
| Hong Kong | AAA | Aa1 |
| Hungary | BB | Ba1 |
| Iceland | BBB- | Baa3 |
| India | BBB- | Baa3 |
| Indonesia | BB+ | Baa3 |
| Ireland | A | Baa1 |
| Isle of Man | NA | Aa1 |
| Israel | A+ | A1 |
| Italy | BBB- | Baa2 |
| Jamaica | B- | Caa2 |
| Japan | AA- | A1 |
| Jersey (States of) | AA+ | Aa1 |
| Jordan | BB- | B1 |
| Kazakhstan | BBB+ | Baa2 |
| Kenya | B+ | B1 |
| Korea | AA- | Aa3 |
| Kuwait | AA | Aa2 |
| Latvia | A- | A3 |
| Lebanon | B- | B2 |
| Liechtenstein | AAA | Aaa |
| Lithuania | A- | A3 |
| Luxembourg | AAA | Aaa |
| Macao | NA | Aa2 |
| Macedonia | BB- | Ba3 |
| Malaysia | A | A3 |
| Malta | BBB+ | A3 |
| Mauritius | NA | Baa1 |
| Mexico | A | A3 |
| Moldova | NA | B3 |
| Mongolia | B+ | B2 |
| Montenegro | B+ | Ba3 |
| Montserrat | BBB- | Baa3 |
| Morocco | BBB- | Ba1 |
| Mozambique | B | B1 |
| Namibia | NA | Baa3 |
| Netherlands | AA+ | Aaa |
| New Zealand | AA+ | Aaa |
| Nicaragua | NA | B3 |
| Nigeria | BB- | Ba3 |
| Norway | AAA | Aaa |
| Oman | A | A1 |
| Pakistan | B- | B3 |
| Panama | BBB | Baa2 |
| Papua New Guinea | B+ | B1 |
| Paraguay | BB | Ba1 |
| Peru | A- | A3 |
| Philippines | BBB | Baa2 |
| Poland | A | A2 |
| Portugal | BB | Ba1 |
| Qatar | AA | Aa2 |
| Ras Al Khaimah (Emirate of) | A | A2 |
| Romania | BBB- | Baa3 |
| Russia | BBB | Ba1 |
| Rwanda | B | B2 |
| Saudi Arabia | AA- | Aa3 |
| Senegal | B+ | B1 |
| Serbia | BB- | B1 |
| Sharjah | A | A3 |
| Singapore | AAA | Aaa |
| Slovakia | A | A2 |
| Slovenia | A- | Baa3 |
| South Africa | BBB+ | Baa2 |
| Spain | BBB | Baa2 |
| Sri Lanka | B+ | B1 |
| St. Maarten | NA | Baa1 |
| St. Vincent & the Grenadines | NA | B3 |
| Suriname | BB- | Ba3 |
| Sweden | AAA | Aaa |
| Switzerland | AAA | Aaa |
| Taiwan | AA- | Aa3 |
| Thailand | A- | Baa1 |
| Trinidad and Tobago | A | Baa2 |
| Tunisia | NA | Ba3 |
| Turkey | BBB | Baa3 |
| Turks and Caicos Islands | BBB+ | Baa1 |
| Uganda | B | B1 |
| Ukraine | CCC+ | Ca |
| United Arab Emirates | NA | Aa2 |
| United Kingdom | AAA | Aa1 |
| United States of America | AA+ | Aaa |
| Uruguay | BBB- | Baa2 |
| Venezuela | CCC+ | Caa3 |
| Vietnam | BB- | B1 |
| Zambia | B+ | B1 |

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
| Congo (Democratic Republic of) | Africa |
| Congo (Republic of) | Africa |
| Cook Islands | Australia & New Zealand |
| Costa Rica | Central and South America |
| Côte d'Ivoire | Africa |
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
| Ethiopia | Africa |
| Fiji | Asia |
| Finland | Western Europe |
| France | Western Europe |
| Gabon | Africa |
| Georgia | Eastern Europe & Russia |
| Germany | Western Europe |
| Ghana | Africa |
| Greece | Western Europe |
| Guatemala | Central and South America |
| Guernsey (States of) | Western Europe |
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
| Jersey (States of) | Western Europe |
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
| Sharjah | Middle East |
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
| Turks and Caicos | Caribbean |
| Uganda | Africa |
| Ukraine | Eastern Europe & Russia |
| United Arab Emirates | Middle East |
| United Kingdom | Western Europe |
| United States of America | North America |
| Uruguay | Central and South America |
| Venezuela | Central and South America |
| Vietnam | Asia |
| Zambia | Africa |

## 10-year CDS Spreads

| Country | Moody's rating | CDS Spread | CDS Spread adj for US | Updated: July 1, 2015 |
|---|---|---|---|---|
| Abu Dhabi | Aa2 | 0.0097 | 0.0056 |  |
| Albania | B1 | NA | NA |  |
| Andorra (Principality of) | Baa1 | NA | NA |  |
| Angola | Ba2 | NA | NA |  |
| Argentina | Caa1 | NA | NA |  |
| Armenia | Ba3 | NA | NA |  |
| Aruba | Baa1 | NA | NA |  |
| Australia | Aaa | 0.0061 | 0.002 |  |
| Austria | Aaa | 0.0057 | 0.0015999999999999999 |  |
| Azerbaijan | Baa3 | NA | NA |  |
| Bahamas | Baa2 | NA | NA |  |
| Bahrain | Baa3 | 0.0321 | 0.027999999999999997 |  |
| Bangladesh | Ba3 | NA | NA |  |
| Barbados | B3 | NA | NA |  |
| Belarus | Caa1 | NA | NA |  |
| Belgium | Aa3 | 0.0085 | 0.0044 |  |
| Belize | Caa2 | NA | NA |  |
| Bermuda | A1 | NA | NA |  |
| Bolivia | Ba3 | NA | NA |  |
| Bosnia and Herzegovina | B3 | NA | NA |  |
| Botswana | A2 | NA | NA |  |
| Brazil | Baa2 | 0.0332 | 0.0291 |  |
| Bulgaria | Baa2 | 0.0226 | 0.0185 |  |
| Burkina Faso | B3 | NA | NA |  |
| Cambodia | B2 | NA | NA |  |
| Cameroon | B2 | NA | NA |  |
| Canada | Aaa | NA | NA |  |
| Cayman Islands | Aa3 | NA | NA |  |
| Cape Verde | B2 | NA | NA |  |
| Chile | Aa3 | 0.0104 | 0.006299999999999999 |  |
| China | Aa3 | 0.0152 | 0.011099999999999999 |  |
| Colombia | Baa2 | 0.0232 | 0.0191 |  |
| Congo (Democratic Republic of) | B3 | NA | NA |  |
| Congo (Republic of) | Ba3 | NA | NA |  |
| Cook Islands | B1 | NA | NA |  |
| Costa Rica | Ba1 | 0.0378 | 0.0337 |  |
| Côte d'Ivoire | B1 | NA | NA |  |
| Croatia | Ba1 | 0.0325 | 0.0284 |  |
| Cuba | Caa2 | NA | NA |  |
| Curacao | A3 | NA | NA |  |
| Cyprus | B3 | 0.0515 | 0.0474 |  |
| Czech Republic | A1 | 0.0094 | 0.0053 |  |
| Denmark | Aaa | 0.0044 | 0.0002999999999999999 |  |
| Dominican Republic | B1 | NA | NA |  |
| Ecuador | B3 | NA | NA |  |
| Egypt | B3 | 0.037 | 0.0329 |  |
| El Salvador | Ba3 | NA | NA |  |
| Estonia | A1 | 0.0088 | 0.0047 |  |
| Ethiopia | B1 | NA | NA |  |
| Fiji | B1 | NA | NA |  |
| Finland | Aaa | 0.0053 | 0.0011999999999999997 |  |
| France | Aa1 | 0.0076 | 0.0034999999999999996 |  |
| Gabon | Ba3 | NA | NA |  |
| Georgia | Ba3 | NA | NA |  |
| Germany | Aaa | 0.0041 | 0 |  |
| Ghana | B3 | NA | NA |  |
| Greece | Caa2 | NA | NA |  |
| Guatemala | Ba1 | NA | NA |  |
| Guernsey (States of) | Aa1 | NA | NA |  |
| Honduras | B3 | NA | NA |  |
| Hong Kong | Aa1 | 0.007 | 0.0029 |  |
| Hungary | Ba1 | 0.0216 | 0.0175 |  |
| Iceland | Baa3 | NA | NA |  |
| India | Baa3 | 0.0237 | 0.0196 |  |
| Indonesia | Baa3 | 0.026 | 0.0219 |  |
| Ireland | Baa1 | 0.0113 | 0.007199999999999999 |  |
| Isle of Man | Aa1 | NA | NA |  |
| Israel | A1 | 0.0106 | 0.0065 |  |
| Italy | Baa2 | 0.0203 | 0.0162 |  |
| Jamaica | Caa2 | NA | NA |  |
| Japan | A1 | 0.0084 | 0.004299999999999999 |  |
| Jersey (States of) | Aa1 | NA | NA |  |
| Jordan | B1 | NA | NA |  |
| Kazakhstan | Baa2 | 0.0288 | 0.0247 |  |
| Kenya | B1 | NA | NA |  |
| Korea | Aa3 | 0.0084 | 0.004299999999999999 |  |
| Kuwait | Aa2 | NA | NA |  |
| Latvia | A3 | 0.0143 | 0.0102 |  |
| Lebanon | B2 | 0.0403 | 0.0362 |  |
| Liechtenstein | Aaa | NA | NA |  |
| Lithuania | A3 | 0.0139 | 0.0098 |  |
| Luxembourg | Aaa | NA | NA |  |
| Macao | Aa2 | NA | NA |  |
| Macedonia | Ba3 | NA | NA |  |
| Malaysia | A3 | 0.0201 | 0.016 |  |
| Malta | A3 | NA | NA |  |
| Mauritius | Baa1 | NA | NA |  |
| Mexico | A3 | 0.0193 | 0.015200000000000002 |  |
| Moldova | B3 | NA | NA |  |
| Mongolia | B2 | NA | NA |  |
| Montenegro | Ba3 | NA | NA |  |
| Montserrat | Baa3 | NA | NA |  |
| Morocco | Ba1 | 0.0229 | 0.0188 |  |
| Mozambique | B1 | NA | NA |  |
| Namibia | Baa3 | NA | NA |  |
| Netherlands | Aaa | 0.0041 | 0 |  |
| New Zealand | Aaa | 0.0065 | 0.0023999999999999994 |  |
| Nicaragua | B3 | NA | NA |  |
| Nigeria | Ba3 | NA | NA |  |
| Norway | Aaa | 0.0031 | 0 |  |
| Oman | A1 | NA | NA |  |
| Pakistan | B3 | 0.0495 | 0.0454 |  |
| Panama | Baa2 | 0.0198 | 0.015700000000000002 |  |
| Papua New Guinea | B1 | NA | NA |  |
| Paraguay | Ba1 | NA | NA |  |
| Peru | A3 | 0.0201 | 0.016 |  |
| Philippines | Baa2 | 0.0155 | 0.0114 |  |
| Poland | A2 | 0.013 | 0.008899999999999998 |  |
| Portugal | Ba1 | 0.0271 | 0.023 |  |
| Qatar | Aa2 | 0.0101 | 0.005999999999999999 |  |
| Ras Al Khaimah (Emirate of) | A2 | NA | NA |  |
| Romania | Baa3 | 0.0173 | 0.0132 |  |
| Russia | Ba1 | 0.0359 | 0.0318 |  |
| Rwanda | B2 | NA | NA |  |
| Saudi Arabia | Aa3 | 0.0093 | 0.005199999999999999 |  |
| Senegal | B1 | NA | NA |  |
| Serbia | B1 | NA | NA |  |
| Sharjah | A3 | NA | NA |  |
| Singapore | Aaa | NA | NA |  |
| Slovakia | A2 | 0.0099 | 0.0058000000000000005 |  |
| Slovenia | Baa3 | 0.0178 | 0.0137 |  |
| South Africa | Baa2 | 0.0273 | 0.023200000000000002 |  |
| Spain | Baa2 | 0.0173 | 0.0132 |  |
| Sri Lanka | B1 | NA | NA |  |
| St. Maarten | Baa1 | NA | NA |  |
| St. Vincent & the Grenadines | B3 | NA | NA |  |
| Suriname | Ba3 | NA | NA |  |
| Sweden | Aaa | 0.0036 | 0 |  |
| Switzerland | Aaa | 0.0031 | 0 |  |
| Taiwan | Aa3 | NA | NA |  |
| Thailand | Baa1 | 0.0164 | 0.012300000000000002 |  |
| Trinidad and Tobago | Baa2 | NA | NA |  |
| Tunisia | Ba3 | 0.0333 | 0.029200000000000004 |  |
| Turkey | Baa3 | 0.0281 | 0.024 |  |
| Turks and Caicos Islands | Baa1 | NA | NA |  |
| Uganda | B1 | NA | NA |  |
| Ukraine | Ca | NA | NA |  |
| United Arab Emirates | Aa2 | NA | NA |  |
| United Kingdom | Aa1 | 0.0041 | 0 |  |
| United States of America | Aaa | 0.0041 | 0 |  |
| Uruguay | Baa2 | NA | NA |  |
| Venezuela | Caa3 | NA | NA |  |
| Vietnam | B1 | 0.029 | 0.024900000000000002 |  |
| Zambia | B1 | NA | NA |  |

## Equity vs Govt Bond volatility

| Country | Standard deviation in Equities | Standard deviation in Bond Price | Relative std deviation (stock/bond) | Standard deviation of CDS | CDS level | Coefficient of Variation in CDS | Relative std deviation (Equity/CDS) |
|---|---|---|---|---|---|---|---|
| Argentina | 0.355 |  | NA | 186 | 6296.3 | 0.029541159093435826 | 12.046672879523543 |
| Bahrain | 0.0759 |  | NA | 43.9 | 299.6 | 0.14652870493991987 | 0.664515948675683 |
| Bangladesh | 0.1624 |  | NA |  |  | NA | NA |
| Bosnia | 0.0899 |  | NA |  |  | NA | NA |
| Botswana | 0.0419 |  | NA |  |  | NA | NA |
| Brazil | 0.2225 | 0.1197 | 1.858813700918964 | 43 | 336.5 | 0.1277860326894502 | 1.8689778931545666 |
| Bulgaria | 0.1533 | 0.1749 | 0.8765008576329331 | 42.3 | 226.3 | 0.18692001767565178 | 1.0070568971082758 |
| Chile | 0.1391 | 0.0666 | 2.088588588588588 | 42.2 | 130 | 0.32461538461538464 | 0.753122493620124 |
| China | 0.1782 |  | NA | 40.2 | 143 | 0.2811188811188811 | 0.9150144035069407 |
| Colombia | 0.16 | 0.0667 | 2.39880059970015 | 52.8 | 221.9 | 0.23794502027940512 | 0.9103692627036476 |
| Costa Rica | 0.0878 |  | NA | 32.5 | 272.9 | 0.11909124221326495 | 0.856341088367111 |
| Croatia | 0.0742 |  | NA | 33.1 | 3149 | 0.010511273420133376 | 7.069598886713186 |
| Cyprus | 0.3697 |  | NA | 86 | 513.7 | 0.16741288689896824 | 2.375725561317573 |
| Czech Republic | 0.1539 | 0.0726 | 2.119834710743802 | 45 | 867 | 0.05190311418685121 | 3.0170431141868517 |
| Egypt | 0.2547 |  | NA | 38.5 | 3549 | 0.010848126232741617 | 23.48955721714183 |
| Estonia | 0.1026 |  | NA | 43.1 | 78.4 | 0.5497448979591837 | 0.7363769165206686 |
| Ghana | 0.0909 |  | NA |  |  | NA | NA |
| Greece | 0.4049 | 0.5623 | 0.7200782500444602 | 165.2 | 1357.6 | 0.12168532704773129 | 3.4491201938758187 |
| Hungary | 0.1721 |  | NA | 42.2 | 174.9 | 0.2412807318467696 | 0.9545577460647791 |
| Iceland | 0.1089 | 0.0404 | 2.6955445544554455 | 34.2 | 211.9 | 0.1613968853232657 | 0.8361310958495813 |
| India | 0.1409 | 0.0349 | 4.037249283667622 | 23.3 | 205.2 | 0.1135477582846004 | 1.354435311932669 |
| Indonesia | 0.1649 | 0.0945 | 1.7449735449735448 | 43.7 | 231.6 | 0.18868739205526772 | 1.062619657501492 |
| Ireland | 0.1607 | 0.05 | 3.214 | 65.4 | 910 | 0.07186813186813187 | 2.3079078872198138 |
| Israel | 0.0833 | 0.059 | 1.411864406779661 | 242 | 109.8 | 2.204007285974499 | 2.241802079362929 |
| Italy | 0.2074 | 0.074 | 2.8027027027027027 | 47.3 | 149 | 0.3174496644295302 | 0.9707815883195936 |
| Jamaica | 0.1004 |  | NA |  |  | NA | NA |
| Jordan | 0.0988 |  | NA |  |  | NA | NA |
| Kazakhastan | 0.2817 |  | NA | 57.4 | 338.4 | 0.16962174940898345 | 1.8303757563776246 |
| Kenya | 0.1009 |  | NA |  |  | NA | NA |
| Korea | 0.112 | 0.0659 | 1.6995447647951443 | 42.9 | 86.1 | 0.49825783972125437 | 0.7230410565044711 |
| Kuwait | 0.1047 |  | NA |  |  | NA | NA |
| Laos | 0.1418 |  | NA |  |  | NA | NA |
| Latvia | 0.1211 |  | NA | 27.3 | 130.8 | 0.20871559633027523 | 0.7889309809456598 |
| Lebanon | 0.0589 | 0.0444 | 1.3265765765765765 | 47.8 | 404.5 | 0.11817058096415327 | 0.6166025893323541 |
| Lithuania | 0.0854 |  | NA | 28.2 | 132.1 | 0.21347464042392128 | 0.6135221581544177 |
| Macedonia | 0.1364 |  | NA |  |  | NA | NA |
| Malaysia | 0.0861 |  | NA | 56.4 | 186.5 | 0.3024128686327078 | 0.5871229750156866 |
| Malta | 0.0691 |  | NA |  |  | NA | NA |
| Mauritius | 0.0542 |  | NA |  |  |  |  |
| Mexico | 0.1481 | 0.0951 | 1.5573080967402735 | 39.3 | 179.9 | 0.21845469705391882 | 0.8963984629572268 |
| Mongolia | 0.2005 |  | NA |  |  | NA | NA |
| Montenegro | 0.1326 |  | NA |  |  | NA | NA |
| Morocco | 0.0826 |  | NA | 36.6 | 211.9 | 0.17272298253893345 | 0.6509453869105182 |
| Namibia | 0.1533 |  | NA |  |  | NA | NA |
| Nigeria | 0.2407 |  | NA |  |  | NA | NA |
| Oman | 0.1768 |  | NA |  |  | NA | NA |
| Pakistan | 0.1507 |  | NA | 71.4 | 448.2 | 0.15930388219544847 | 1.1052946384979694 |
| Palestine | 0.1408 |  | NA |  |  | NA | NA |
| Panama | 0.0618 |  | NA | 35.6 | 186.1 | 0.19129500268672758 | 0.5143562386417837 |
| Peru | 0.1615 | 0.0851 | 1.8977673325499413 | 38.1 | 190.1 | 0.2004208311415045 | 1.0062252930837616 |
| Philippines | 0.1469 | 0.3036 | 0.48386034255599475 | 48.8 | 146.6 | 0.3328785811732606 | 0.7741806303535885 |
| Poland | 0.1508 | 0.1171 | 1.2877882152006832 | 31.5 | 101.8 | 0.3094302554027505 | 0.796777556990052 |
| Portugal | 0.2166 | 0.1018 | 2.1277013752455796 | 65.6 | 180.1 | 0.3642420877290394 | 0.9589015389485516 |
| Qatar | 0.2025 |  | NA | 31.9 | 118.8 | 0.2685185185185185 | 1.0226564495530015 |
| Romania | 0.1229 |  | NA | 32.7 | 151.3 | 0.21612690019828157 | 0.7847743008099024 |
| Russia | 0.2102 | 0.401 | 0.5241895261845386 | 90.5 | 395.7 | 0.228708617639626 | 1.1477819878053717 |
| Saudi Arabia | 0.1902 |  | NA | 40.9 | 112.2 | 0.36452762923351156 | 0.8862987783777659 |
| Serbia | 0.0858 |  | NA |  |  | NA | NA |
| Singapore | 0.0968 |  | NA |  |  | NA | NA |
| Slovakia | 0.1707 | 0.0791 | 2.158027812895069 | 20.1 | 86.7 | 0.23183391003460208 | 0.968136895109229 |
| Slovenia | 0.1526 | 0.1306 | 1.1684532924961717 | 13.4 | 163.9 | 0.08175716900549115 | 1.9482601540801183 |
| South Africa | 0.1379 |  | NA | 39.9 | 269.9 | 0.14783253056687662 | 1.0806448112686309 |
| Spain | 0.1938 | 0.073 | 2.6547945205479455 | 64.9 | 130 | 0.49923076923076926 | 0.8874279957330805 |
| Sri Lanka | 0.124 |  | NA |  |  | NA | NA |
| Taiwan | 0.1097 |  | NA |  |  | NA | NA |
| Tanzania | 0.1822 |  | NA |  |  | NA | NA |
| Thailand | 0.1687 | 0.0649 | 2.5993836671802772 | 42.6 | 159 | 0.2679245283018868 | 0.8975794578793514 |
| Tunisia | 0.0823 |  | NA | 42.8 | 319.2 | 0.13408521303258145 | 0.7478739980793104 |
| Turkey | 0.2506 | 0.1317 | 1.902809415337889 | 39.1 | 263.7 | 0.14827455441789913 | 1.8383824828066457 |
| UAE | 0.325 |  | NA |  |  | NA | NA |
| Ukraine | 0.2707 |  | NA | 186.7 | 2803 | 0.06660720656439528 | 4.130732005707406 |
| US | 0.1087 |  | NA | 92.1 | 32.5 | 2.8338461538461535 | 2.8722039171469134 |
| Venezuela | 0.4004 | 0.3625 | 1.104551724137931 | 401.5 | 3781 | 0.10618883893149961 | 3.8768299348219104 |
| Vietnam | 0.1675 |  | NA | 30.6 | 259 | 0.11814671814671815 | 1.5358754763166529 |
| Average |  |  | 1.8639118408712265 |  |  |  | 2.1075172406175127 |
| Median |  |  | 1.8782905167344528 |  |  |  | 0.9694592417144112 |
| High |  |  | 4.037249283667622 |  |  |  | 23.48955721714183 |
| Low |  |  | 0.48386034255599475 |  |  |  | 0.5143562386417837 |

## Country GDP

| Country | GDP (in billions) |
|---|---|
| Abu Dhabi | 390 |
| Albania | 12.9 |
| Andorra (Principality of) | 4.5 |
| Angola | 124.2 |
| Argentina | 609.9 |
| Armenia | 10.4 |
| Aruba | 2.6 |
| Australia | 1560.4 |
| Austria | 428.3 |
| Azerbaijan | 73.4 |
| Bahamas | 8.4 |
| Bahrain | 32.9 |
| Bangladesh | 150 |
| Barbados | 3.7 |
| Belarus | 71.7 |
| Belgium | 524.8 |
| Belize | 1.6 |
| Bermuda | 5.557 |
| Bolivia | 30.6 |
| Bosnia and Herzegovina | 17.9 |
| Botswana | 14.8 |
| Brazil | 2245.7 |
| Bulgaria | 54.5 |
| Burkina Faso | 11.6 |
| Cambodia | 15.2 |
| Cameroon | 29.6 |
| Canada | 1826.8 |
| Cayman Islands | 1.897 |
| Cape Verde | 4 |
| Chile | 277.2 |
| China | 9240.3 |
| Colombia | 378.4 |
| Congo (Democratic Republic of) | 32.7 |
| Congo (Republic of) | 14.1 |
| Cook Islands | 1.2 |
| Costa Rica | 49.6 |
| Côte d'Ivoire | 31.1 |
| Croatia | 57.9 |
| Cuba | 60.8 |
| Curacao | 1 |
| Cyprus | 21.9 |
| Czech Republic | 208.9 |
| Denmark | 335.9 |
| Dominican Republic | 61.2 |
| Ecuador | 94.5 |
| Egypt | 272 |
| El Salvador | 24.3 |
| Estonia | 24.9 |
| Ethiopia | 47.5 |
| Fiji | 3.9 |
| Finland | 267.3 |
| France | 2806.4 |
| Gabon | 19.3 |
| Georgia | 16.1 |
| Germany | 3730.3 |
| Ghana | 48.1 |
| Greece | 242.2 |
| Guatemala | 53.8 |
| Guernsey (States of) | 0.5 |
| Honduras | 18.6 |
| Hong Kong | 274 |
| Hungary | 133.4 |
| Iceland | 15.3 |
| India | 1876.8 |
| Indonesia | 868.4 |
| Ireland | 232.1 |
| Isle of Man | 1.4 |
| Israel | 290.6 |
| Italy | 2149.5 |
| Jamaica | 14.4 |
| Japan | 4919.6 |
| Jersey (States of) | 1 |
| Jordan | 33.7 |
| Kazakhstan | 321.9 |
| Kenya | 55.2 |
| Korea | 1304.6 |
| Kuwait | 175.8 |
| Latvia | 31 |
| Lebanon | 44.4 |
| Liechtenstein | 10.5 |
| Lithuania | 45.9 |
| Luxembourg | 60.1 |
| Macao | 51.8 |
| Macedonia | 10.2 |
| Malaysia | 313.2 |
| Malta | 9.6 |
| Mauritius | 11.9 |
| Mexico | 1260.9 |
| Moldova | 8 |
| Mongolia | 11.5 |
| Montenegro | 4.4 |
| Montserrat | 1.5 |
| Morocco | 103.8 |
| Mozambique | 15.6 |
| Namibia | 13.1 |
| Netherlands | 853.54 |
| New Zealand | 185.8 |
| Nicaragua | 11.3 |
| Nigeria | 521.8 |
| Norway | 512.6 |
| Oman | 80 |
| Pakistan | 232.3 |
| Panama | 42.7 |
| Papua New Guinea | 15.3 |
| Paraguay | 29 |
| Peru | 202.4 |
| Philippines | 272.1 |
| Poland | 525.9 |
| Portugal | 227.3 |
| Qatar | 203.2 |
| Ras Al Khaimah (Emirate of) | 5.2 |
| Romania | 189.6 |
| Russia | 2096.8 |
| Rwanda | 7.5 |
| Saudi Arabia | 748.5 |
| Senegal | 14.8 |
| Serbia | 45.5 |
| Sharjah | 1 |
| Singapore | 297.9 |
| Slovakia | 97.7 |
| Slovenia | 48 |
| South Africa | 350.6 |
| Spain | 1393 |
| Sri Lanka | 67.2 |
| St. Maarten | 1.5 |
| St. Vincent & the Grenadines | 0.713 |
| Suriname | 5.3 |
| Sweden | 579.7 |
| Switzerland | 685.4 |
| Taiwan | 970.9 |
| Thailand | 387.3 |
| Trinidad and Tobago | 24.6 |
| Tunisia | 47 |
| Turkey | 822.1 |
| Turks and Caicos Islands | 1.5 |
| Uganda | 21.5 |
| Ukraine | 177.4 |
| United Arab Emirates | 402.3 |
| United Kingdom | 2678.5 |
| United States of America | 16768.4 |
| Uruguay | 55.7 |
| Venezuela | 438.3 |
| Vietnam | 171.4 |
| Zambia | 26.8 |

## Ratings worksheet

| Country | S&P Rating | Moody's Rating | S&P local currency rating | Moody's Local Currency Rating (modified) | Rating in 1/15 | Moody's Rating in July 2015 |
|---|---|---|---|---|---|---|
| Abu Dhabi | AA | Aa2 | Abu Dhabi (Emirate of) | Abu Dhabi |  | Aa2 |
| Albania | B | B1 | Albania (Republic of) | Albania |  | B1 |
| Andorra (Principality of) | BBB+ | NA | Andorra (Principality of) |  |  |  |
| Angola | BB- | Ba2 | Angola (Republic of) | Angola |  | Ba2 |
| Argentina | CCC+ | Caa1 | Argentina (Republic of) (Unsolicited Ratings) | Argentina |  | Caa1 |
| Armenia | NA | Ba3 |  | Armenia |  | Ba3 |
| Aruba | BBB+ | NA | Aruba |  |  |  |
| Australia | AAA | Aaa | Australia (Commonwealth of) (Unsolicited Ratings) | Australia |  | Aaa |
| Austria | AA+ | Aaa | Austria (Republic of) | Austria |  | Aaa |
| Azerbaijan | BBB- | Baa3 | Azerbaijan (Republic of) | Azerbaijan |  | Baa3 |
| Bahamas | BBB | Baa2 | Bahamas | Bahamas |  | Baa2 |
| Bahrain | BBB | Baa3 | Bahrain (Kingdom of) | Bahrain | Baa4 | Baa3 |
| Bangladesh | BB- | Ba3 | Bangladesh (People's Republic of) | Bangladesh |  | Ba3 |
| Barbados | B | B3 | Barbados | Barbados |  | B3 |
| Belarus | B- | Caa1 | Belarus (Republic of) | Belarus | B3 | Caa1 |
| Belgium | AA | Aa3 | Belgium (Kingdom of) (Unsolicited Ratings) | Belgium |  | Aa3 |
| Belize | B- | Caa2 | Belize | Belize |  | Caa2 |
| Bermuda | AA- | A1 | Bermuda | Bermuda |  | A1 |
| Bolivia | BB | Ba3 | Bolivia (Plurinational State of) | Bolivia |  | Ba3 |
| Bosnia and Herzegovina | B | B3 | Bosnia and Herzegovina | Bosnia and Herzegovina |  | B3 |
| Botswana | A- | A2 | Botswana (Republic of) | Botswana |  | A2 |
| Brazil | BBB+ | Baa2 | Brazil (Federative Republic of) | Brazil |  | Baa2 |
| Bulgaria | BB+ | Baa2 | Bulgaria (Republic of) | Bulgaria |  | Baa2 |
| Burkina Faso | B- | NA | Burkina Faso |  |  |  |
| Cambodia | NA | B2 |  | Cambodia |  | B2 |
| Cameroon | B | NA | Cameroon |  |  |  |
| Canada | AAA | Aaa | Canada | Canada |  | Aaa |
| Cayman Islands | NA | Aa3 |  | Cayman Islands |  | Aa3 |
| Cape Verde | B | NA | Cape Verde |  |  |  |
| Chile | AA+ | Aa3 | Chile (Republic of) | Chile |  | Aa3 |
| China | AA- | Aa3 | China (People's Republic of ) | China |  | Aa3 |
| Colombia | BBB+ | Baa2 | Colombia (Republic of) | Colombia |  | Baa2 |
| Congo (Democratic Republic of) | B- | B3 | Congo (Democratic Republic of) | Congo (Democratic Republic of) |  | B3 |
| Congo (Republic of) | B+ | Ba3 | Congo (Republic of) | Congo (Republic of) |  | Ba3 |
| Cook Islands | B+ | NA | Cook Islands |  |  |  |
| Costa Rica | BB | Ba1 | Costa Rica (Republic of) | Costa Rica |  | Ba1 |
| Côte d'Ivoire | NA | B1 |  | Côte d'Ivoire |  | B1 |
| Croatia | BB | Ba1 | Croatia (Republic of) | Croatia |  | Ba1 |
| Cuba | NA | Caa2 |  | Cuba |  | Caa2 |
| Curacao | A- | NA | Curacao |  |  |  |
| Cyprus | B+ | B3 | Cyprus (Republic of) | Cyprus |  | B3 |
| Czech Republic | AA | A1 | Czech Republic | Czech Republic |  | A1 |
| Denmark | AAA | Aaa | Denmark (Kingdom of) | Denmark |  | Aaa |
| Dominican Republic | B+ | B1 | Dominican Republic | Dominican Republic |  | B1 |
| Ecuador | B+ | B3 | Ecuador (Republic of) | Ecuador |  | B3 |
| Egypt | B- | B3 | Egypt (Arab republic of) | Egypt | Caa1 | B3 |
| El Salvador | B+ | Ba3 | El Salvador (Republic of) | El Salvador |  | Ba3 |
| Estonia | AA- | A1 | Estonia (Republic of) | Estonia |  | A1 |
| Ethiopia | B | B1 | Ethiopia (Federal Democratic Republic of) | Ethiopia |  | B1 |
| Fiji | B | B1 | Fiji | Fiji |  | B1 |
| Finland | AA+ | Aaa | Finland (Republic of) | Finland |  | Aaa |
| France | AA | Aa1 | France (Republic of) (Unsolicited Ratings) | France |  | Aa1 |
| Gabon | BB- | Ba3 | Gabonese Republic | Gabon |  | Ba3 |
| Georgia | BB- | Ba3 | Georgia (Government of) | Georgia |  | Ba3 |
| Germany | AAA | Aaa | Germany (Federal Republic of) (Unsolicited Ratings) | Germany |  | Aaa |
| Ghana | B- | B3 | Ghana (Republic of) | Ghana | B2 | B3 |
| Greece | B | Caa2 | Greece (Hellenic Republic) | Greece | Caa1 | Caa2 |
| Guatemala | BB+ | Ba1 | Guatemala (Republic of) | Guatemala |  | Ba1 |
| Guernsey (States of) | AA+ | NA | Guernsey (States of) |  |  |  |
| Honduras | B | B3 | Honduras (Republic of) | Honduras |  | B3 |
| Hong Kong | AAA | Aa1 | Hong Kong (Special Administrative Region) | Hong Kong |  | Aa1 |
| Hungary | BB | Ba1 | Hungary | Hungary |  | Ba1 |
| Iceland | BBB- | Baa3 | Iceland (Republic of) | Iceland |  | Baa3 |
| India | BBB- | Baa3 | India (Republic of) (Unsolicited Ratings) | India |  | Baa3 |
| Indonesia | BB+ | Baa3 | Indonesia (Republic of) | Indonesia |  | Baa3 |
| Ireland | A | Baa1 | Ireland (Republic of) | Ireland |  | Baa1 |
| Isle of Man | NA | Aa1 |  | Isle of Man |  | Aa1 |
| Israel | A+ | A1 | Israel (State of) | Israel |  | A1 |
| Italy | BBB- | Baa2 | Italy (Republic of) (Unsolicited Ratings) | Italy |  | Baa2 |
| Jamaica | B- | Caa2 | Jamaica | Jamaica | Caa3 | Caa2 |
| Japan | AA- | A1 | Japan (Unsolicited Ratings) | Japan |  | A1 |
| Jersey (States of) | AA+ | NA | Jersey (States of) |  |  |  |
| Jordan | BB- | B1 | Jordan (Hashemite Kingdom of) | Jordan |  | B1 |
| Kazakhstan | BBB+ | Baa2 | Kazakhstan (Republic of) | Kazakhstan |  | Baa2 |
| Kenya | B+ | B1 | Kenya (Republic of) | Kenya |  | B1 |
| Korea | AA- | Aa3 | Korea (Republic of) | Korea |  | Aa3 |
| Kuwait | AA | Aa2 | Kuwait (State of) | Kuwait |  | Aa2 |
| Latvia | A- | A3 | Latvia (Republic of) | Latvia | Baa1 | A3 |
| Lebanon | B- | B2 | Lebanon (Republic of) | Lebanon |  | B2 |
| Liechtenstein | AAA | NA | Liechtenstein |  |  |  |
| Lithuania | A- | A3 | Lithuania (Republic of) | Lithuania | Baa1 | A3 |
| Luxembourg | AAA | Aaa | Luxembourg (Grand Duchy of) | Luxembourg |  | Aaa |
| Macao | NA | Aa2 |  | Macao |  | Aa2 |
| Macedonia | BB- | NA | Macedonia |  |  |  |
| Malaysia | A | A3 | Malaysia | Malaysia |  | A3 |
| Malta | BBB+ | A3 | Malta (Republic of) | Malta |  | A3 |
| Mauritius | NA | Baa1 |  | Mauritius |  | Baa1 |
| Mexico | A | A3 | Mexico | Mexico |  | A3 |
| Moldova | NA | B3 |  | Moldova |  | B3 |
| Mongolia | B+ | B2 | Mongolia | Mongolia |  | B2 |
| Montenegro | B+ | Ba3 | Montenegro (Republic of) | Montenegro |  | Ba3 |
| Montserrat | BBB- | NA | Montserrat |  |  |  |
| Morocco | BBB- | Ba1 | Morocco (Kingdom of) | Morocco |  | Ba1 |
| Mozambique | B | B1 | Mozambique (Republic of) | Mozambique |  | B1 |
| Namibia | NA | Baa3 |  | Namibia |  | Baa3 |
| Netherlands | AA+ | Aaa | Netherlands (State of The) (Unsolicited Ratings) | Netherlands |  | Aaa |
| New Zealand | AA+ | Aaa | New Zealand | New Zealand |  | Aaa |
| Nicaragua | NA | B3 |  | Nicaragua |  | B3 |
| Nigeria | BB- | Ba3 | Nigeria (Federal Republic of) | Nigeria |  | Ba3 |
| Norway | AAA | Aaa | Norway (Kingdom of) | Norway |  | Aaa |
| Oman | A | A1 | Oman (Sultanate of) | Oman |  | A1 |
| Pakistan | B- | B3 | Pakistan (Islamic Republic of) | Pakistan | Caa1 | B3 |
| Panama | BBB | Baa2 | Panama (Republic of) | Panama |  | Baa2 |
| Papua New Guinea | B+ | B1 | Papua New Guinea (Independent State of) | Papua New Guinea |  | B1 |
| Paraguay | BB | Ba1 | Paraguay (Republic of) | Paraguay | Ba2 | Ba1 |
| Peru | A- | A3 | Peru (Republic of) | Peru |  | A3 |
| Philippines | BBB | Baa2 | Philippines (Republic of the) | Philippines |  | Baa2 |
| Poland | A | A2 | Poland (Republic of) | Poland |  | A2 |
| Portugal | BB | Ba1 | Portugal (Republic of) (Unsolicited Ratings) | Portugal |  | Ba1 |
| Qatar | AA | Aa2 | Qatar (State of) | Qatar |  | Aa2 |
| Ras Al Khaimah (Emirate of) | A | NA | Ras Al Khaimah (Emirate of) |  |  |  |
| Romania | BBB- | Baa3 | Romania | Romania |  | Baa3 |
| Russia | BBB | Ba1 | Russian Federation | Russia | Baa2 | Ba1 |
| Rwanda | B | NA | Rwanda |  |  |  |
| Saudi Arabia | AA- | Aa3 | Saudi Arabia (Kingdom of) | Saudi Arabia |  | Aa3 |
| Senegal | B+ | B1 | Senegal (Republic of) | Senegal |  | B1 |
| Serbia | BB- | B1 | Serbia (Republic of) | Serbia |  | B1 |
| Sharjah | A | A3 | Sharjah (Emirate of) | Sharjah |  | A3 |
| Singapore | AAA | Aaa | Singapore (Republic of) (Unsolicited Ratings) | Singapore |  | Aaa |
| Slovakia | A | A2 | Slovak Republic | Slovakia |  | A2 |
| Slovenia | A- | Baa3 | Slovenia (Republic of) | Slovenia | Ba1 | Baa3 |
| South Africa | BBB+ | Baa2 | South Africa (Republic of) | South Africa |  | Baa2 |
| Spain | BBB | Baa2 | Spain (Kingdom of) | Spain |  | Baa2 |
| Sri Lanka | B+ | B1 | Sri Lanka (Democratic Socialist Republic of) | Sri Lanka |  | B1 |
| St. Maarten | NA | Baa1 |  | St. Maarten |  | Baa1 |
| St. Vincent & the Grenadines | NA | B3 |  | St. Vincent & the Grenadines |  | B3 |
| Suriname | BB- | Ba3 | Suriname (The Republic of) | Suriname |  | Ba3 |
| Sweden | AAA | Aaa | Sweden (Kingdom of) (Unsolicited Ratings) | Sweden |  | Aaa |
| Switzerland | AAA | Aaa | Swiss Confederation (Unsolicited Ratings) | Switzerland |  | Aaa |
| Taiwan | AA- | Aa3 | Taiwan (Republic of China) (Unsolicited Ratings) | Taiwan |  | Aa3 |
| Thailand | A- | Baa1 | Thailand (Kingdom of) | Thailand |  | Baa1 |
| Trinidad and Tobago | A | Baa2 | Trinidad and Tobago (Republic of) | Trinidad and Tobago | Baa1 | Baa2 |
| Tunisia | NA | Ba3 |  | Tunisia |  | Ba3 |
| Turkey | BBB | Baa3 | Turkey (Republic of) (Unsolicited Ratings) | Turkey |  | Baa3 |
| Turks and Caicos Islands | BBB+ | NA | Turks and Caicos Islands |  |  |  |
| Uganda | B | B1 | Uganda (Republic of) | Uganda |  | B1 |
| Ukraine | CCC+ | Ca | Ukraine | Ukraine | Caa3 | Ca |
| United Arab Emirates | NA | Aa2 |  | United Arab Emirates |  | Aa2 |
| United Kingdom | AAA | Aa1 | United Kingdom (Unsolicited Ratings) | United Kingdom |  | Aa1 |
| United States of America | AA+ | Aaa | United States of America (Unsolicited Ratings) | United States of America |  | Aaa |
| Uruguay | BBB- | Baa2 | Uruguay (Oriental Republic of) | Uruguay |  | Baa2 |
| Venezuela | CCC+ | Caa3 | Venezuela | Venezuela | Caa1 | Caa3 |
| Vietnam | BB- | B1 | Vietnam (Socialist Republic of) | Vietnam |  | B1 |
| Zambia | B+ | B1 | Zambia (Republic of) | Zambia |  | B1 |

## PRS Worksheet

| Country | PRS Score | ERP (based on rating) | Final ERP | PRS Score |
|---|---|---|---|---|
| Abu Dhabi | More than | 0.06559999999999999 | 0.06559999999999999 | More than |
| Albania | 0 | 0.1256 | 0.1256 | 0 |
| Andorra (Principality of) | 40.001 | 0.0821 | 0.0821 | 40.001 |
| Algeria | 50.001 |  | 0.11779999999999999 | 50.001 |
| Angola | 57.001 | 0.1031 | 0.1031 | 57.001 |
| Argentina | 60.001 | 0.17059999999999997 | 0.17059999999999997 | 60.001 |
| Armenia | 62.001 | 0.11209999999999999 | 0.11209999999999999 | 62.001 |
| Aruba | 64.001 | 0.0821 | 0.0821 | 64.001 |
| Australia | 66.001 | 0.0581 | 0.0581 | 66.001 |
| Austria | 68.001 | 0.0581 | 0.0581 | 68.001 |
| Azerbaijan | 69.001 | 0.0911 | 0.0911 | 69.001 |
| Bahamas | 72.001 | 0.0866 | 0.0866 | 72.001 |
| Bahrain | 74.001 | 0.0911 | 0.0911 | 74.001 |
| Bangladesh | 76.001 | 0.11209999999999999 | 0.11209999999999999 | 76.001 |
| Barbados | 80.001 | 0.15560000000000002 | 0.15560000000000002 | 80.001 |
| Belarus | 81.001 | 0.17059999999999997 | 0.17059999999999997 | 81.001 |
| Belgium | 83.001 | 0.06709999999999999 | 0.06709999999999999 | 83.001 |
| Belize | 85.001 | 0.1931 | 0.1931 | 85.001 |
| Bermuda |  | 0.0686 | 0.0686 |  |
| Bolivia |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Bosnia and Herzegovina |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Botswana |  | 0.07085 | 0.07085 |  |
| Brazil |  | 0.0866 | 0.0866 |  |
| Brunei |  |  | 0.06034999999999999 |  |
| Bulgaria |  | 0.0866 | 0.0866 |  |
| Burkina Faso |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Cambodia |  | 0.1406 | 0.1406 |  |
| Cameroon |  | 0.1406 | 0.1406 |  |
| Canada |  | 0.0581 | 0.0581 |  |
| Cayman Islands |  | 0.06709999999999999 | 0.06709999999999999 |  |
| Cape Verde |  | 0.1406 | 0.1406 |  |
| Chile |  | 0.06709999999999999 | 0.06709999999999999 |  |
| China |  | 0.06709999999999999 | 0.06709999999999999 |  |
| Colombia |  | 0.0866 | 0.0866 |  |
| Congo (Democratic Republic of) |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Congo (Republic of) |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Cook Islands |  | 0.1256 | 0.1256 |  |
| Costa Rica |  | 0.0956 | 0.0956 |  |
| Côte d'Ivoire |  | 0.1256 | 0.1256 |  |
| Croatia |  | 0.0956 | 0.0956 |  |
| Cuba |  | 0.1931 | 0.1931 |  |
| Curacao |  | 0.0761 | 0.0761 |  |
| Cyprus |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Czech Republic |  | 0.0686 | 0.0686 |  |
| Denmark |  | 0.0581 | 0.0581 |  |
| Dominican Republic |  | 0.1256 | 0.1256 |  |
| Ecuador |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Egypt |  | 0.15560000000000002 | 0.15560000000000002 |  |
| El Salvador |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Estonia |  | 0.0686 | 0.0686 |  |
| Ethiopia |  | 0.1256 | 0.1256 |  |
| Fiji |  | 0.1256 | 0.1256 |  |
| Finland |  | 0.0581 | 0.0581 |  |
| France |  | 0.0641 | 0.0641 |  |
| Gabon |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Gambia |  |  | 0.13185 |  |
| Georgia |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Germany |  | 0.0581 | 0.0581 |  |
| Ghana |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Greece |  | 0.1931 | 0.1931 |  |
| Guatemala |  | 0.0956 | 0.0956 |  |
| Guernsey (States of) |  | 0.0641 | 0.0641 |  |
| Guinea |  |  | 0.1495 |  |
| Guinea-Bissau |  |  | 0.1369 |  |
| Guyana |  |  | 0.11779999999999999 |  |
| Haiti |  |  | 0.14085 |  |
| Honduras |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Hong Kong |  | 0.0641 | 0.0641 |  |
| Hungary |  | 0.0956 | 0.0956 |  |
| Iceland |  | 0.0911 | 0.0911 |  |
| India |  | 0.0911 | 0.0911 |  |
| Indonesia |  | 0.0911 | 0.0911 |  |
| Iran |  |  | 0.11779999999999999 |  |
| Iraq |  |  | 0.14085 |  |
| Ireland |  | 0.0821 | 0.0821 |  |
| Isle of Man |  | 0.0641 | 0.0641 |  |
| Israel |  | 0.0686 | 0.0686 |  |
| Italy |  | 0.0866 | 0.0866 |  |
| Jamaica |  | 0.1931 | 0.1931 |  |
| Japan |  | 0.0686 | 0.0686 |  |
| Jersey (States of) |  | 0.0641 | 0.0641 |  |
| Jordan |  | 0.1256 | 0.1256 |  |
| Kazakhstan |  | 0.0866 | 0.0866 |  |
| Kenya |  | 0.1256 | 0.1256 |  |
| Korea, South |  | 0.06709999999999999 | 0.06709999999999999 |  |
| Korea, North |  |  | 0.0641 |  |
| Kuwait |  | 0.06559999999999999 | 0.06559999999999999 |  |
| Latvia |  | 0.0761 | 0.0761 |  |
| Lebanon |  | 0.1406 | 0.1406 |  |
| Liberia |  |  | 0.225 |  |
| Libya |  |  | 0.1495 |  |
| Liechtenstein |  | 0.0581 | 0.0581 |  |
| Lithuania |  | 0.0761 | 0.0761 |  |
| Luxembourg |  | 0.0581 | 0.0581 |  |
| Macao |  | 0.06559999999999999 | 0.06559999999999999 |  |
| Macedonia |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Madagascar |  |  | 0.1369 |  |
| Malawi |  |  | 0.14085 |  |
| Malaysia |  | 0.0761 | 0.0761 |  |
| Mali |  |  | 0.1369 |  |
| Malta |  | 0.0761 | 0.0761 |  |
| Mauritius |  | 0.0821 | 0.0821 |  |
| Mexico |  | 0.0761 | 0.0761 |  |
| Moldova |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Mongolia |  | 0.1406 | 0.1406 |  |
| Montenegro |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Montserrat |  | 0.0911 | 0.0911 |  |
| Morocco |  | 0.0956 | 0.0956 |  |
| Mozambique |  | 0.1256 | 0.1256 |  |
| Myanmar |  |  | 0.11779999999999999 |  |
| Namibia |  | 0.0911 | 0.0911 |  |
| Netherlands |  | 0.0581 | 0.0581 |  |
| New Zealand |  | 0.0581 | 0.0581 |  |
| Nicaragua |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Niger |  |  | 0.1495 |  |
| Nigeria |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Norway |  | 0.0581 | 0.0581 |  |
| Oman |  | 0.0686 | 0.0686 |  |
| Pakistan |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Panama |  | 0.0866 | 0.0866 |  |
| Papua New Guinea |  | 0.1256 | 0.1256 |  |
| Paraguay |  | 0.0956 | 0.0956 |  |
| Peru |  | 0.0761 | 0.0761 |  |
| Philippines |  | 0.0866 | 0.0866 |  |
| Poland |  | 0.07085 | 0.07085 |  |
| Portugal |  | 0.0956 | 0.0956 |  |
| Qatar |  | 0.06559999999999999 | 0.06559999999999999 |  |
| Ras Al Khaimah (Emirate of) |  | 0.07085 | 0.07085 |  |
| Romania |  | 0.0911 | 0.0911 |  |
| Russia |  | 0.0956 | 0.0956 |  |
| Rwanda |  | 0.1406 | 0.1406 |  |
| Saudi Arabia |  | 0.06709999999999999 | 0.06709999999999999 |  |
| Senegal |  | 0.1256 | 0.1256 |  |
| Serbia |  | 0.1256 | 0.1256 |  |
| Sharjah |  | 0.0761 | 0.0761 |  |
| Sierra Leone |  |  | 0.1369 |  |
| Singapore |  | 0.0581 | 0.0581 |  |
| Slovakia |  | 0.07085 | 0.07085 |  |
| Slovenia |  | 0.0911 | 0.0911 |  |
| Somalia |  |  | 0.225 |  |
| South Africa |  | 0.0866 | 0.0866 |  |
| Spain |  | 0.0866 | 0.0866 |  |
| Sri Lanka |  | 0.1256 | 0.1256 |  |
| St. Maarten |  | 0.0821 | 0.0821 |  |
| St. Vincent & the Grenadines |  | 0.15560000000000002 | 0.15560000000000002 |  |
| Sudan |  |  | 0.225 |  |
| Suriname |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Sweden |  | 0.0581 | 0.0581 |  |
| Switzerland |  | 0.0581 | 0.0581 |  |
| Syria |  |  | 0.25 |  |
| Taiwan |  | 0.06709999999999999 | 0.06709999999999999 |  |
| Tanzania |  |  | 0.14085 |  |
| Thailand |  | 0.0821 | 0.0821 |  |
| Togo |  |  | 0.13185 |  |
| Trinidad and Tobago |  | 0.0866 | 0.0866 |  |
| Tunisia |  | 0.11209999999999999 | 0.11209999999999999 |  |
| Turkey |  | 0.0911 | 0.0911 |  |
| Turks and Caicos Islands |  | 0.0821 | 0.0821 |  |
| Uganda |  | 0.1256 | 0.1256 |  |
| Ukraine |  | 0.0911 | 0.0911 |  |
| United Arab Emirates |  | 0.06559999999999999 | 0.06559999999999999 |  |
| United Kingdom |  | 0.0641 | 0.0641 |  |
| United States of America |  | 0.0581 | 0.0581 |  |
| Uruguay |  | 0.0866 | 0.0866 |  |
| Venezuela |  | 0.2081 | 0.2081 |  |
| Vietnam |  | 0.1256 | 0.1256 |  |
| Yemen, Republic |  |  | 0.1495 |  |
| Zambia |  | 0.1256 | 0.1256 |  |
| Zimbabwe |  |  | 0.1495 |  |
