---
title: "Ctryprem"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pc/ctryprem.xls
---

# Ctryprem

Source: https://www.stern.nyu.edu/~adamodar/pc/ctryprem.xls

Sheets: Explanation and FAQ, Country Lookup, ERPs by country, Regional Simple Averages, Regional Weighted Averages, Regional breakdown, Sovereign Ratings (Moody's), Regional lookup table, Rating  CDS, 10-year CDS Spreads, Equity vs Govt Bond volatility, Country GDP, Ratings worksheet, PRS Worksheet

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
| Angola | 124.2 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Africa | 0.06799146000985383 | 0.0020397438002956146 | 0.006969124651010018 | 0.0030596157004434224 |
| Botswana | 14.8 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Africa | 0.00810204193354136 | 6.886735643510156e-05 | 0.0005691684458312805 | 0.00010330103465265234 |
| Burkina Faso | 11.6 | B3 | 0.065 | 0.155 | 0.0975 | Africa | 0.006350249083045929 | 0.0004127661903979854 | 0.000984288607872119 | 0.0006191492855969781 |
| Cameroon | 29.6 | B2 | 0.055 | 0.14 | 0.0825 | Africa | 0.01620408386708272 | 0.0008912246126895495 | 0.002268571741391581 | 0.0013368369190343244 |
| Cape Verde | 4 | B2 | 0.055 | 0.14 | 0.0825 | Africa | 0.002189741063119286 | 0.00012043575847156074 | 0.0003065637488367001 | 0.0001806536377073411 |
| Congo (Democratic Republic of) | 32.7 | B3 | 0.065 | 0.155 | 0.0975 | Africa | 0.017901133191000167 | 0.0011635736574150109 | 0.002774675644605026 | 0.0017453604861225162 |
| Congo (Republic of) | 14.1 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa | 0.007718837247495483 | 0.00027787814090983736 | 0.0008606503530957463 | 0.00041681721136475604 |
| Côte d'Ivoire | 31.1 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.01702523676575245 | 0.0007661356544588602 | 0.0021281545957190563 | 0.0011492034816882905 |
| Egypt | 272 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Africa | 0.14890239229211144 | 0.011167679421908357 | 0.02531340668965894 | 0.016751519132862536 |
| Ethiopia | 47.5 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.026003175124541523 | 0.0011701428806043684 | 0.0032503968905676904 | 0.0017552143209065528 |
| Gabon | 19.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa | 0.010565500629550556 | 0.00038035802266382 | 0.001178053320194887 | 0.0005705370339957299 |
| Ghana | 48.1 | B2 | 0.055 | 0.14 | 0.0825 | Africa | 0.026331636284009415 | 0.001448239995620518 | 0.0036864290797613184 | 0.002172359993430777 |
| Kenya | 55.2 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.03021842667104615 | 0.0013598292001970767 | 0.0037773033338807686 | 0.002039743800295615 |
| Morocco | 103.8 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Africa | 0.056823780587945474 | 0.0014205945146986369 | 0.00539825915585482 | 0.0021308917720479557 |
| Mozambique | 15.6 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.008539990146165216 | 0.0003842995565774347 | 0.001067498768270652 | 0.0005764493348661521 |
| Namibia | 13.1 | Baa3 | 0.022 | 0.0905 | 0.033 | Africa | 0.007171401981715662 | 0.00015777084359774456 | 0.0006490118793452674 | 0.00023665626539661687 |
| Nigeria | 521.8 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa | 0.28565172168391084 | 0.01028346198062079 | 0.031850166967756055 | 0.015425192970931183 |
| Rwanda | 7.5 | B2 | 0.055 | 0.14 | 0.0825 | Africa | 0.004105764493348661 | 0.00022581704713417635 | 0.0005748070290688126 | 0.0003387255707012646 |
| Senegal | 14.8 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.00810204193354136 | 0.0003645918870093612 | 0.00101275524169267 | 0.0005468878305140418 |
| South Africa | 350.6 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Africa | 0.19193080418240543 | 0.003646685279465703 | 0.016506049159686866 | 0.005470027919198555 |
| Tunisia | 47 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa | 0.025729457491651612 | 0.000926260469699458 | 0.0028688345103191543 | 0.001389390704549187 |
| Uganda | 21.5 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.011769858214266163 | 0.0005296436196419774 | 0.0014712322767832704 | 0.0007944654294629661 |
| Zambia | 26.8 | B1 | 0.045 | 0.125 | 0.0675 | Africa | 0.014671265122899218 | 0.0006602069305304647 | 0.0018339081403624022 | 0.0009903103957956973 |
| Africa | 1826.7 |  | 0.03986620682104341 | 0.11729931023156509 | 0.059799310231565116 |  | 0.9999999999999998 |  |  |  |
| Bangladesh | 150 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Asia | 0.0069911817893696755 | 0.0002516825444173083 | 0.0007795167695147187 | 0.00037752381662596243 |
| Cambodia | 15.2 | B2 | 0.055 | 0.14 | 0.0825 | Asia | 0.0007084397546561271 | 3.896418650608699e-05 | 9.91815656518578e-05 | 5.844627975913049e-05 |
| China | 9240.3 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia | 0.4306707805887507 | 0.0025840246835325043 | 0.028639606909151922 | 0.0038760370252987567 |
| Fiji | 3.9 | B1 | 0.045 | 0.125 | 0.0675 | Asia | 0.00018177072652361155 | 8.17968269356252e-06 | 2.2721340815451444e-05 | 1.226952404034378e-05 |
| Hong Kong | 274 | Aa1 | 0.004 | 0.0635 | 0.006 | Asia | 0.012770558735248608 | 5.108223494099443e-05 | 0.0008109304796882867 | 7.662335241149165e-05 |
| India | 1876.8 | Baa3 | 0.022 | 0.0905 | 0.033 | Asia | 0.08747366654859338 | 0.0019244206640690543 | 0.007916366822647701 | 0.002886630996103582 |
| Indonesia | 868.4 | Baa3 | 0.022 | 0.0905 | 0.033 | Asia | 0.04047428177259084 | 0.0008904341989969984 | 0.003662922500419471 | 0.0013356512984954978 |
| Japan | 4919.6 | A1 | 0.007 | 0.068 | 0.0105 | Asia | 0.22929211953988707 | 0.0016050448367792094 | 0.015591864128712322 | 0.0024075672551688142 |
| Korea | 1304.6 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia | 0.060804638416077854 | 0.00036482783049646714 | 0.004043508454669178 | 0.0005472417457447008 |
| Macao | 51.8 | Aa2 | 0.005 | 0.065 | 0.0075 | Asia | 0.002414288111262328 | 1.207144055631164e-05 | 0.00015692872723205132 | 1.810716083446746e-05 |
| Malaysia | 313.2 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Asia | 0.014597587576203882 | 0.00017517105091444658 | 0.0011021178620033933 | 0.0002627565763716699 |
| Mauritius | 11.9 | Baa1 | 0.016 | 0.0815 | 0.024 | Asia | 0.0005546337552899943 | 8.87414008463991e-06 | 4.520265105613454e-05 | 1.3311210126959864e-05 |
| Mongolia | 11.5 | B2 | 0.055 | 0.14 | 0.0825 | Asia | 0.0005359906038516751 | 2.9479483211842132e-05 | 7.503868453923452e-05 | 4.42192248177632e-05 |
| Pakistan | 232.3 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Asia | 0.010827010197803837 | 0.0008120257648352877 | 0.0018405917336266522 | 0.0012180386472529317 |
| Papua New Guinea | 15.3 | B1 | 0.045 | 0.125 | 0.0675 | Asia | 0.000713100542515707 | 3.208952441320681e-05 | 8.913756781446337e-05 | 4.8134286619810226e-05 |
| Philippines | 272.1 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Asia | 0.012682003765916593 | 0.00024095807155241527 | 0.0010906523238688268 | 0.00036143710732862287 |
| Singapore | 297.9 | Aaa | 0 | 0.0575 | 0 | Asia | 0.013884487033688175 | 0 | 0.0007983580044370701 | 0 |
| Sri Lanka | 67.2 | B1 | 0.045 | 0.125 | 0.0675 | Asia | 0.003132049441637615 | 0.00014094222487369266 | 0.00039150618020470187 | 0.00021141333731053901 |
| Taiwan | 970.9 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia | 0.04525158932866012 | 0.00027150953597196073 | 0.003009230690355898 | 0.00040726430395794113 |
| Thailand | 387.3 | Baa1 | 0.016 | 0.0815 | 0.024 | Asia | 0.018051231380152504 | 0.0002888197020824401 | 0.0014711753574824292 | 0.0004332295531236601 |
| Vietnam | 171.4 | B1 | 0.045 | 0.125 | 0.0675 | Asia | 0.00798859039131975 | 0.0003594865676093887 | 0.0009985737989149687 | 0.0005392298514140831 |
| Asia | 21455.6 |  | 0.010090088368537817 | 0.07263513255280672 | 0.015135132552806728 |  | 0.9999999999999999 |  |  |  |
| Australia | 1560.4 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand | 0.8929838617374385 | 0 | 0.051346572049902714 | 0 |
| Cook Islands | 1.2 | B1 | 0.045 | 0.125 | 0.0675 | Australia & New Zealand | 0.0006867345770859562 | 3.090305596886803e-05 | 8.584182213574453e-05 | 4.6354583953302045e-05 |
| New Zealand | 185.8 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand | 0.10632940368547557 | 0 | 0.006113940711914846 | 0 |
| Australia & New Zealand | 1747.4 |  | 3.090305596886803e-05 | 0.0575463545839533 | 4.6354583953302045e-05 |  |  |  |  |  |
| Aruba | 2.6 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean | 0.013839577999329314 | 0.0008995725699564055 | 0.002145134589896044 | 0.0013493588549346083 |
| Bahamas | 8.4 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Caribbean | 0.04471248276706394 | 0.0008495371725742148 | 0.0038452735179674985 | 0.0012743057588613222 |
| Barbados | 3.7 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean | 0.01969478407596864 | 0.0012801609649379618 | 0.0030526915317751393 | 0.0019202414474069425 |
| Bermuda | 5.557 | A1 | 0.007 | 0.068 | 0.0105 | Caribbean | 0.029579436516258845 | 0.00020705605561381193 | 0.0020114016831056015 | 0.0003105840834207179 |
| Cayman Islands | 1.897 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Caribbean | 0.010097569024895272 | 6.0585414149371634e-05 | 0.0006714883401555356 | 9.087812122405746e-05 |
| Cuba | 60.8 | Caa2 | 0.09 | 0.1925 | 0.135 | Caribbean | 0.32363320859970085 | 0.029126988773973076 | 0.06229939265544242 | 0.043690483160959616 |
| Curacao | 1 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Caribbean | 0.0053229146151266594 | 6.387497538151992e-05 | 0.00040188005344206286 | 9.581246307227989e-05 |
| Dominican Republic | 61.2 | B1 | 0.045 | 0.125 | 0.0675 | Caribbean | 0.32576237444575157 | 0.01465930685005882 | 0.040720296805718946 | 0.021988960275088232 |
| Jamaica | 14.4 | Caa3 | 0.1 | 0.20750000000000002 | 0.15000000000000002 | Caribbean | 0.07664997045782389 | 0.007664997045782389 | 0.015904868869998458 | 0.011497495568673586 |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.0905 | 0.033 | Caribbean | 0.00798437192268999 | 0.00017565618229917974 | 0.000722585659003444 | 0.0002634842734487697 |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.0815 | 0.024 | Caribbean | 0.00798437192268999 | 0.00012774995076303983 | 0.0006507263116992341 | 0.00019162492614455975 |
| St. Vincent & the Grenadines | 0.713 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean | 0.0037952381205853076 | 0.000246690477838045 | 0.0005882619086907227 | 0.0003700357167570675 |
| Trinidad and Tobago | 24.6 | Baa1 | 0.016 | 0.0815 | 0.024 | Caribbean | 0.13094369953211582 | 0.002095099192513853 | 0.01067191151186744 | 0.0031426487887707797 |
| Caribbean | 187.867 |  | 0.05745727562584169 | 0.14368591343876252 | 0.08618591343876254 |  |  |  |  | 0.08618591343876254 |
| Argentina | 609.9 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Central and South America | 0.10461765412192528 | 0.007846324059144396 | 0.017785001200727298 | 0.011769486088716592 |
| Belize | 1.6 | Caa2 | 0.09 | 0.1925 | 0.135 | Central and South America | 0.0002744519537548458 | 2.4700675837936122e-05 | 5.2832001097807824e-05 | 3.705101375690419e-05 |
| Bolivia | 30.6 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America | 0.005248893615561426 | 0.0001889601701602113 | 0.0005852516381350989 | 0.00028344025524031693 |
| Brazil | 2245.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America | 0.3852104703420357 | 0.007318998936498678 | 0.03312810044941507 | 0.010978498404748016 |
| Chile | 277.2 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Central and South America | 0.04754880098802703 | 0.0002852928059281622 | 0.003161995265703798 | 0.0004279392088922433 |
| Colombia | 378.4 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America | 0.06490788706302103 | 0.0012332498541973995 | 0.005582078287419808 | 0.0018498747812960993 |
| Costa Rica | 49.6 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Central and South America | 0.00850801056640022 | 0.00021270026416000552 | 0.000808261003808021 | 0.0003190503962400083 |
| Ecuador | 94.5 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America | 0.01620981851864558 | 0.0010536382037119626 | 0.0025125218703900645 | 0.001580457305567944 |
| El Salvador | 24.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America | 0.00416823904765172 | 0.00015005660571546192 | 0.00046475865381316676 | 0.00022508490857319285 |
| Guatemala | 53.8 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Central and South America | 0.009228446945006689 | 0.00023071117362516723 | 0.0008767024597756355 | 0.00034606676043775087 |
| Honduras | 18.6 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America | 0.0031905039624000823 | 0.00020738275755600535 | 0.0004945281141720127 | 0.00031107413633400804 |
| Mexico | 1260.9 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Central and South America | 0.21628529280592818 | 0.002595423513671138 | 0.01632953960684758 | 0.0038931352705067076 |
| Nicaragua | 11.3 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America | 0.0019383169233935984 | 0.0001259906000205839 | 0.00030043912312600776 | 0.00018898590003087586 |
| Panama | 42.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America | 0.007324436515832447 | 0.0001391642938008165 | 0.0006299015403615904 | 0.00020874644070122472 |
| Paraguay | 29 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Central and South America | 0.00497444166180658 | 0.0001492332498541974 | 0.0005098802703351745 | 0.00022384987478129607 |
| Peru | 202.4 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Central and South America | 0.03471817214998799 | 0.0004166180657998559 | 0.002621221997324094 | 0.000624927098699784 |
| Suriname | 5.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America | 0.0009091220968129267 | 3.2728395485265355e-05 | 0.0001013671137946413 | 4.9092593227898035e-05 |
| Uruguay | 55.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America | 0.00955435864009057 | 0.00018153281416172083 | 0.0008216748430477889 | 0.0002722992212425812 |
| Venezuela | 438.3 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Central and South America | 0.07518268208171806 | 0.005638701156128855 | 0.012781055953892069 | 0.008458051734193282 |
| Central and South America | 5829.8 |  | 0.028031407595457827 | 0.09954711139318673 | 0.04204711139318672 |  | 1 |  |  |  |
| Albania | 12.9 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia | 0.003010993627897207 | 0.0001354947132553743 | 0.00037637420348715086 | 0.00020324206988306149 |
| Armenia | 10.4 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Eastern Europe & Russia | 0.002427467731017903 | 7.282403193053708e-05 | 0.0002488154424293351 | 0.00010923604789580563 |
| Azerbaijan | 73.4 | Baa3 | 0.022 | 0.0905 | 0.033 | Eastern Europe & Russia | 0.017132320332376355 | 0.0003769110473122798 | 0.00155047499008006 | 0.0005653665709684198 |
| Belarus | 71.7 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia | 0.01673552272249843 | 0.001087808976962398 | 0.0025940060219872565 | 0.0016317134654435968 |
| Bosnia and Herzegovina | 17.9 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia | 0.004178045421655814 | 0.0002715729524076279 | 0.0006475970403566512 | 0.00040735942861144184 |
| Bulgaria | 54.5 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia | 0.012720864551968818 | 0.00024169642648740755 | 0.0010939943514693183 | 0.00036254463973111126 |
| Croatia | 57.9 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia | 0.013514459771724672 | 0.0003378614942931168 | 0.0012838736783138437 | 0.0005067922414396753 |
| Czech Republic | 208.9 | A1 | 0.007 | 0.068 | 0.0105 | Eastern Europe & Russia | 0.04875942394323461 | 0.0003413159676026423 | 0.0033156408281399537 | 0.0005119739514039634 |
| Estonia | 24.9 | A1 | 0.007 | 0.068 | 0.0105 | Eastern Europe & Russia | 0.005811917932917863 | 4.068342553042505e-05 | 0.0003952104194384147 | 6.102513829563757e-05 |
| Georgia | 16.1 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0037579067759027154 | 0.00013528464393249774 | 0.0004190066055131527 | 0.0002029269658987466 |
| Hungary | 133.4 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia | 0.03113694185747964 | 0.000778423546436991 | 0.002958009476460566 | 0.0011676353196554867 |
| Kazakhstan | 321.9 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia | 0.07513479448217912 | 0.0014275610951614032 | 0.006461592325467404 | 0.002141341642742105 |
| Latvia | 31 | Baa1 | 0.016 | 0.0815 | 0.024 | Eastern Europe & Russia | 0.007235721121303365 | 0.00011577153794085384 | 0.0005897112713862242 | 0.00017365730691128075 |
| Lithuania | 45.9 | Baa1 | 0.016 | 0.0815 | 0.024 | Eastern Europe & Russia | 0.010713535466704014 | 0.00017141656746726423 | 0.0008731531405363771 | 0.00025712485120089635 |
| Macedonia | 10.2 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0023807856592675584 | 8.570828373363209e-05 | 0.0002654576010083327 | 0.00012856242560044812 |
| Moldova | 8 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia | 0.0018672828700137716 | 0.00012137338655089515 | 0.0002894288448521346 | 0.00018206007982634275 |
| Montenegro | 4.4 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia | 0.0010270055785075744 | 3.6972200826272676e-05 | 0.00011451112200359454 | 5.545830123940901e-05 |
| Poland | 525.9 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Eastern Europe & Russia | 0.1227505076675303 | 0.0010433793151740076 | 0.008623223163644004 | 0.0015650689727610115 |
| Romania | 189.6 | Baa3 | 0.022 | 0.0905 | 0.033 | Eastern Europe & Russia | 0.044254604019326384 | 0.0009736012884251804 | 0.0040050416637490375 | 0.0014604019326377707 |
| Russia | 2096.8 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia | 0.48941484023060955 | 0.009298881964381582 | 0.04208967625983242 | 0.013948322946572372 |
| Serbia | 45.5 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia | 0.010620171323203326 | 0.0004779077095441497 | 0.0013275214154004158 | 0.0007168615643162246 |
| Slovakia | 97.7 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Eastern Europe & Russia | 0.022804192050043186 | 0.0001938356324253671 | 0.001601994491515534 | 0.00029075344863805063 |
| Slovenia | 48 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia | 0.01120369722008263 | 0.00028009243050206576 | 0.0010643512359078497 | 0.0004201386457530987 |
| Ukraine | 177.4 | Caa3 | 0.1 | 0.20750000000000002 | 0.15000000000000002 | Eastern Europe & Russia | 0.041406997642555385 | 0.0041406997642555385 | 0.008591952010830243 | 0.006211049646383309 |
| Eastern Europe & Russia | 4284.299999999999 |  | 0.02218707840253951 | 0.09078061760380927 | 0.033280617603809265 |  | 1.0000000000000002 |  |  |  |
| Abu Dhabi | 390 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East | 0.16198704103671704 | 0.0008099352051835852 | 0.010529157667386609 | 0.0012149028077753777 |
| Bahrain | 32.9 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Middle East | 0.013665060641302539 | 0.00025963615218474825 | 0.0011751952151520181 | 0.0003894542282771223 |
| Israel | 290.6 | A1 | 0.007 | 0.068 | 0.0105 | Middle East | 0.12070111314171789 | 0.0008449077919920252 | 0.008207675693636817 | 0.001267361687988038 |
| Jordan | 33.7 | B1 | 0.045 | 0.125 | 0.0675 | Middle East | 0.013997341751121448 | 0.0006298803788004652 | 0.001749667718890181 | 0.0009448205682006978 |
| Kuwait | 175.8 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East | 0.07301877388270477 | 0.00036509386941352385 | 0.00474622030237581 | 0.0005476408041202857 |
| Lebanon | 44.4 | B2 | 0.055 | 0.14 | 0.0825 | Middle East | 0.018441601594949324 | 0.0010142880877222129 | 0.002581824223292906 | 0.0015214321315833194 |
| Oman | 80 | A1 | 0.007 | 0.068 | 0.0105 | Middle East | 0.03322811098189067 | 0.0002325967768732347 | 0.002259511546768566 | 0.00034889516530985207 |
| Qatar | 203.2 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East | 0.0843994018940023 | 0.0004219970094700115 | 0.00548596112311015 | 0.0006329955142050172 |
| Ras Al Khaimah (Emirate of) | 5.2 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Middle East | 0.002159827213822894 | 1.8358531317494598e-05 | 0.00015172786177105831 | 2.75377969762419e-05 |
| Saudi Arabia | 748.5 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Middle East | 0.3108905133743146 | 0.0018653430802458876 | 0.020674219139391922 | 0.002798014620368832 |
| Sharjah | 1 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Middle East | 0.0004153513872736334 | 4.9842166472836015e-06 | 3.1359029739159326e-05 | 7.476324970925403e-06 |
| United Arab Emirates | 402.3 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East | 0.16709586310018273 | 0.0008354793155009137 | 0.010861231101511878 | 0.0012532189732513705 |
| Middle East | 2407.6000000000004 |  | 0.007302500415351387 | 0.06845375062302708 | 0.010953750623027081 |  | 1 |  |  |  |
| Canada | 1826.8 | Aaa | 0 | 0.0575 | 0 | North America | 0.09824040612631216 | 0 | 0.00564882335226295 | 0 |
| United States of America | 16768.4 | Aaa | 0 | 0.0575 | 0 | North America | 0.9017595938736879 | 0 | 0.05185117664773706 | 0 |
| North America | 18595.2 |  | 0 | 0.05750000000000001 | 0 |  |  |  |  |  |
| Andorra (Principality of) | 4.5 | Baa1 | 0.016 | 0.0815 | 0.024 | Western Europe | 0.00024201693688305853 | 3.872270990128936e-06 | 1.972438035596927e-05 | 5.808406485193405e-06 |
| Austria | 428.3 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.023034634237114215 | 0 | 0.0013244914686340674 | 0 |
| Belgium | 524.8 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Western Europe | 0.02822455299471758 | 0.00016934731796830547 | 0.001876932774148719 | 0.00025402097695245826 |
| Cyprus | 21.9 | B3 | 0.065 | 0.155 | 0.0975 | Western Europe | 0.0011778157594975515 | 7.655802436734085e-05 | 0.00018256144272212047 | 0.00011483703655101127 |
| Denmark | 335.9 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.018065219799782078 | 0 | 0.0010387501384874695 | 0 |
| Finland | 267.3 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.014375806050853677 | 0 | 0.0008266088479240865 | 0 |
| France | 2806.4 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe | 0.15093251814858122 | 0.0006037300725943249 | 0.009584214902434907 | 0.0009055951088914873 |
| Germany | 3730.3 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.20062128436774962 | 0 | 0.011535723851145603 | 0 |
| Greece | 242.2 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Western Europe | 0.013025889358461504 | 0.0009769417018846128 | 0.0022144011909384555 | 0.0014654125528269191 |
| Guernsey (States of) | 0.5 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe | 2.689077076478428e-05 | 1.0756308305913713e-07 | 1.7075639435638018e-06 | 1.613446245887057e-07 |
| Iceland | 15.3 | Baa3 | 0.022 | 0.0905 | 0.033 | Western Europe | 0.000822857585402399 | 1.810286687885278e-05 | 7.446861147891711e-05 | 2.715430031827917e-05 |
| Ireland | 232.1 | Baa1 | 0.016 | 0.0815 | 0.024 | Western Europe | 0.012482695789012862 | 0.0001997231326242058 | 0.0010173397068045484 | 0.0002995846989363087 |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe | 7.529415814139598e-05 | 3.011766325655839e-07 | 4.781179041978645e-06 | 4.517649488483759e-07 |
| Italy | 2149.5 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Western Europe | 0.11560342351780761 | 0.0021964650468383447 | 0.009941894422531454 | 0.0032946975702575166 |
| Jersey (States of) | 1 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe | 5.378154152956856e-05 | 2.1512616611827426e-07 | 3.4151278871276036e-06 | 3.226892491774114e-07 |
| Liechtenstein | 10.5 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.0005647061860604699 | 0 | 3.2470605698477017e-05 | 0 |
| Luxembourg | 60.1 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.0032322706459270707 | 0 | 0.00018585556214080658 | 0 |
| Malta | 9.6 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Western Europe | 0.0005163027986838581 | 6.195633584206298e-06 | 3.8980861300631297e-05 | 9.293450376309447e-06 |
| Netherlands | 853.54 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.045904696957147946 | 0 | 0.002639520075036007 | 0 |
| Norway | 512.6 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.027568418188056845 | 0 | 0.0015851840458132687 | 0 |
| Portugal | 227.3 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Western Europe | 0.012224544389670935 | 0.0003056136097417734 | 0.001161331717018739 | 0.00045842041461266014 |
| Spain | 1393 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Western Europe | 0.074917687350689 | 0.001423436059663091 | 0.006442921112159254 | 0.0021351540894946363 |
| Sweden | 579.7 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.031177159624690896 | 0 | 0.0017926866784197266 | 0 |
| Switzerland | 685.4 | Aaa | 0 | 0.0575 | 0 | Western Europe | 0.03686186856436629 | 0 | 0.0021195574424510617 | 0 |
| Turkey | 822.1 | Baa3 | 0.022 | 0.0905 | 0.033 | Western Europe | 0.04421380529145831 | 0.0009727037164120828 | 0.004001349378876977 | 0.0014590555746181243 |
| United Kingdom | 2678.5 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe | 0.1440538589869494 | 0.0005762154359477975 | 0.009147420045671286 | 0.0008643231539216963 |
| Western Europe | 18593.739999999998 |  | 0.0075295287553768095 | 0.0687942931330652 | 0.011294293133065215 |  | 1 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| Region | Weighted Average: TRP | Weighted Average: CRP | Weighted Average: Default Spreads | Total GDP | Weight | Weight *ERP | Weight*CRP | Weight*Default Spread |  |  |
| Africa | 0.11729931023156509 | 0.059799310231565116 | 0.03986620682104341 | 1826.7 | 0.0243793368764316 | 0.002859679399508385 | 0.0014578675291135688 | 0.0009719116860757125 |  |  |
| Asia | 0.07263513255280672 | 0.015135132552806728 | 0.010090088368537817 | 21455.6 | 0.28634877116437607 | 0.020798980949857774 | 0.004333926607906153 | 0.002889284405270768 |  |  |
| Australia & New Zealand | 0.0575463545839533 | 4.6354583953302045e-05 | 3.090305596886803e-05 | 1747.4 | 0.023320990451566527 | 0.0013420379857748367 | 1.081034809761296e-06 | 7.206898731741972e-07 |  |  |
| Caribbean | 0.14368591343876252 | 0.08618591343876254 | 0.05745727562584169 | 187.867 | 0.002507293414881795 | 0.0003602627445762849 | 0.0002160933732205817 | 0.00014406224881372115 |  |  |
| Central and South America | 0.09954711139318673 | 0.04204711139318672 | 0.028031407595457827 | 5829.8 | 0.07780514486353585 | 0.007745277422693433 | 0.003271481593040121 | 0.002180987728693415 |  |  |
| Eastern Europe & Russia | 0.09078061760380927 | 0.033280617603809265 | 0.02218707840253951 | 4284.299999999999 | 0.057178733771115056 | 0.0051907207655456115 | 0.0019029435737064951 | 0.0012686290491376634 |  |  |
| Middle East | 0.06845375062302708 | 0.010953750623027081 | 0.007302500415351387 | 2407.6000000000004 | 0.032132091456559216 | 0.0021995621755636035 | 0.00035196691681144864 | 0.0002346446112076324 |  |  |
| North America | 0.05750000000000001 | 0 | 0 | 18595.2 | 0.2481735616601636 | 0.01426997979545941 | 0 | 0 |  |  |
| Western Europe | 0.0687942931330652 | 0.011294293133065215 | 0.0075295287553768095 | 18593.739999999998 | 0.24815407634137035 | 0.01707158426999327 | 0.0028027248803644805 | 0.00186848325357632 |  |  |
| Global | 0.07183808550897261 | 0.014338085508972608 | 0.009558723672648407 | 74928.207 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| For updating industry average spreadsheets |  |  |  |  |  |  |  |  |  |  |
|  | ERP | Default Spread | Tax rate |  |  |  |  |  |  |  |
| Africa & Mid East | 0.08952599012823842 | 0.02135066008549229 | 0.2785 |  |  |  |  |  |  |  |
| Australia, NZ & Canada | 0.0575 | 0 | 0.3 |  |  |  |  |  |  |  |
| Latin America & Caribbean | 0.10092509131861234 | 0.028950060879074892 | 0.2715 |  |  |  |  |  |  |  |
| Japan | 0.068 | 0.007 | 0.3564 |  |  |  |  |  |  |  |
| US | 0.0575 | 0 | 0.4 |  |  |  |  |  |  |  |
| Europe | 0.0687942931330652 | 0.0075295287553768095 | 0.3 |  |  |  |  |  |  |  |
| Emerging Markets | 0.08365152248144625 | 0.017434348320964164 | 0.25 |  |  |  |  |  |  |  |
| Small Asia (No India, China & Japan) | 0.0811174223550905 | 0.015744948236726994 | 0.2 |  |  |  |  |  |  |  |
| India | 0.0905 | 0.022 | 0.34 |  |  |  |  |  |  |  |
| China | 0.0665 | 0.006 | 0.25 |  |  |  |  |  |  |  |
| Global | 0.07183808550897261 | 0.009558723672648407 | 0.3 |  |  |  |  |  |  |  |

## Regional breakdown

| Country | GDP (in billions) | Moody's rating | Adj. Default Spread | Total Risk Premium | Country Risk Premium | Region |
|---|---|---|---|---|---|---|
| Abu Dhabi | 390 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East |
| Albania | 12.9 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia |
| Andorra (Principality of) | 4.5 | Baa1 | 0.016 | 0.0815 | 0.024 | Western Europe |
| Angola | 124.2 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Africa |
| Argentina | 609.9 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Central and South America |
| Armenia | 10.4 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Eastern Europe & Russia |
| Aruba | 2.6 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean |
| Australia | 1560.4 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand |
| Austria | 428.3 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Azerbaijan | 73.4 | Baa3 | 0.022 | 0.0905 | 0.033 | Eastern Europe & Russia |
| Bahamas | 8.4 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Caribbean |
| Bahrain | 32.9 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Middle East |
| Bangladesh | 150 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Asia |
| Barbados | 3.7 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean |
| Belarus | 71.7 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia |
| Belgium | 524.8 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Western Europe |
| Belize | 1.6 | Caa2 | 0.09 | 0.1925 | 0.135 | Central and South America |
| Bermuda | 5.557 | A1 | 0.007 | 0.068 | 0.0105 | Caribbean |
| Bolivia | 30.6 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Bosnia and Herzegovina | 17.9 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia |
| Botswana | 14.8 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Africa |
| Brazil | 2245.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America |
| Bulgaria | 54.5 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia |
| Burkina Faso | 11.6 | B3 | 0.065 | 0.155 | 0.0975 | Africa |
| Cambodia | 15.2 | B2 | 0.055 | 0.14 | 0.0825 | Asia |
| Cameroon | 29.6 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Canada | 1826.8 | Aaa | 0 | 0.0575 | 0 | North America |
| Cayman Islands | 1.897 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Caribbean |
| Cape Verde | 4 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Chile | 277.2 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Central and South America |
| China | 9240.3 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia |
| Colombia | 378.4 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America |
| Congo (Democratic Republic of) | 32.7 | B3 | 0.065 | 0.155 | 0.0975 | Africa |
| Congo (Republic of) | 14.1 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Cook Islands | 1.2 | B1 | 0.045 | 0.125 | 0.0675 | Australia & New Zealand |
| Costa Rica | 49.6 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Central and South America |
| Côte d'Ivoire | 31.1 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Croatia | 57.9 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia |
| Cuba | 60.8 | Caa2 | 0.09 | 0.1925 | 0.135 | Caribbean |
| Curacao | 1 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Caribbean |
| Cyprus | 21.9 | B3 | 0.065 | 0.155 | 0.0975 | Western Europe |
| Czech Republic | 208.9 | A1 | 0.007 | 0.068 | 0.0105 | Eastern Europe & Russia |
| Denmark | 335.9 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Dominican Republic | 61.2 | B1 | 0.045 | 0.125 | 0.0675 | Caribbean |
| Ecuador | 94.5 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America |
| Egypt | 272 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Africa |
| El Salvador | 24.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Estonia | 24.9 | A1 | 0.007 | 0.068 | 0.0105 | Eastern Europe & Russia |
| Ethiopia | 47.5 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Fiji | 3.9 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Finland | 267.3 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| France | 2806.4 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe |
| Gabon | 19.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Georgia | 16.1 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Germany | 3730.3 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Ghana | 48.1 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Greece | 242.2 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Western Europe |
| Guatemala | 53.8 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Central and South America |
| Guernsey (States of) | 0.5 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe |
| Honduras | 18.6 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America |
| Hong Kong | 274 | Aa1 | 0.004 | 0.0635 | 0.006 | Asia |
| Hungary | 133.4 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia |
| Iceland | 15.3 | Baa3 | 0.022 | 0.0905 | 0.033 | Western Europe |
| India | 1876.8 | Baa3 | 0.022 | 0.0905 | 0.033 | Asia |
| Indonesia | 868.4 | Baa3 | 0.022 | 0.0905 | 0.033 | Asia |
| Ireland | 232.1 | Baa1 | 0.016 | 0.0815 | 0.024 | Western Europe |
| Isle of Man | 1.4 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe |
| Israel | 290.6 | A1 | 0.007 | 0.068 | 0.0105 | Middle East |
| Italy | 2149.5 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Western Europe |
| Jamaica | 14.4 | Caa3 | 0.1 | 0.20750000000000002 | 0.15000000000000002 | Caribbean |
| Japan | 4919.6 | A1 | 0.007 | 0.068 | 0.0105 | Asia |
| Jersey (States of) | 1 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe |
| Jordan | 33.7 | B1 | 0.045 | 0.125 | 0.0675 | Middle East |
| Kazakhstan | 321.9 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia |
| Kenya | 55.2 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Korea | 1304.6 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia |
| Kuwait | 175.8 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East |
| Latvia | 31 | Baa1 | 0.016 | 0.0815 | 0.024 | Eastern Europe & Russia |
| Lebanon | 44.4 | B2 | 0.055 | 0.14 | 0.0825 | Middle East |
| Liechtenstein | 10.5 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Lithuania | 45.9 | Baa1 | 0.016 | 0.0815 | 0.024 | Eastern Europe & Russia |
| Luxembourg | 60.1 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Macao | 51.8 | Aa2 | 0.005 | 0.065 | 0.0075 | Asia |
| Macedonia | 10.2 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Malaysia | 313.2 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Asia |
| Malta | 9.6 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Western Europe |
| Mauritius | 11.9 | Baa1 | 0.016 | 0.0815 | 0.024 | Asia |
| Mexico | 1260.9 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Central and South America |
| Moldova | 8 | B3 | 0.065 | 0.155 | 0.0975 | Eastern Europe & Russia |
| Mongolia | 11.5 | B2 | 0.055 | 0.14 | 0.0825 | Asia |
| Montenegro | 4.4 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Eastern Europe & Russia |
| Montserrat | 1.5 | Baa3 | 0.022 | 0.0905 | 0.033 | Caribbean |
| Morocco | 103.8 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Africa |
| Mozambique | 15.6 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Namibia | 13.1 | Baa3 | 0.022 | 0.0905 | 0.033 | Africa |
| Netherlands | 853.54 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| New Zealand | 185.8 | Aaa | 0 | 0.0575 | 0 | Australia & New Zealand |
| Nicaragua | 11.3 | B3 | 0.065 | 0.155 | 0.0975 | Central and South America |
| Nigeria | 521.8 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Norway | 512.6 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Oman | 80 | A1 | 0.007 | 0.068 | 0.0105 | Middle East |
| Pakistan | 232.3 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Asia |
| Panama | 42.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America |
| Papua New Guinea | 15.3 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Paraguay | 29 | Ba2 | 0.03 | 0.10250000000000001 | 0.045 | Central and South America |
| Peru | 202.4 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Central and South America |
| Philippines | 272.1 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Asia |
| Poland | 525.9 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Eastern Europe & Russia |
| Portugal | 227.3 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Western Europe |
| Qatar | 203.2 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East |
| Ras Al Khaimah (Emirate of) | 5.2 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Middle East |
| Romania | 189.6 | Baa3 | 0.022 | 0.0905 | 0.033 | Eastern Europe & Russia |
| Russia | 2096.8 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Eastern Europe & Russia |
| Rwanda | 7.5 | B2 | 0.055 | 0.14 | 0.0825 | Africa |
| Saudi Arabia | 748.5 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Middle East |
| Senegal | 14.8 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Serbia | 45.5 | B1 | 0.045 | 0.125 | 0.0675 | Eastern Europe & Russia |
| Sharjah | 1 | A3 | 0.012 | 0.07550000000000001 | 0.018000000000000002 | Middle East |
| Singapore | 297.9 | Aaa | 0 | 0.0575 | 0 | Asia |
| Slovakia | 97.7 | A2 | 0.0085 | 0.07025 | 0.012750000000000001 | Eastern Europe & Russia |
| Slovenia | 48 | Ba1 | 0.025 | 0.095 | 0.037500000000000006 | Eastern Europe & Russia |
| South Africa | 350.6 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Africa |
| Spain | 1393 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Western Europe |
| Sri Lanka | 67.2 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| St. Maarten | 1.5 | Baa1 | 0.016 | 0.0815 | 0.024 | Caribbean |
| St. Vincent & the Grenadines | 0.713 | B3 | 0.065 | 0.155 | 0.0975 | Caribbean |
| Suriname | 5.3 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Central and South America |
| Sweden | 579.7 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Switzerland | 685.4 | Aaa | 0 | 0.0575 | 0 | Western Europe |
| Taiwan | 970.9 | Aa3 | 0.006 | 0.0665 | 0.009000000000000001 | Asia |
| Thailand | 387.3 | Baa1 | 0.016 | 0.0815 | 0.024 | Asia |
| Trinidad and Tobago | 24.6 | Baa1 | 0.016 | 0.0815 | 0.024 | Caribbean |
| Tunisia | 47 | Ba3 | 0.036 | 0.11149999999999999 | 0.05399999999999999 | Africa |
| Turkey | 822.1 | Baa3 | 0.022 | 0.0905 | 0.033 | Western Europe |
| Turks and Caicos Islands | 1.5 | Baa1 | 0.016 | 0.0815 | 0.024 | Caribbean |
| Uganda | 21.5 | B1 | 0.045 | 0.125 | 0.0675 | Africa |
| Ukraine | 177.4 | Caa3 | 0.1 | 0.20750000000000002 | 0.15000000000000002 | Eastern Europe & Russia |
| United Arab Emirates | 402.3 | Aa2 | 0.005 | 0.065 | 0.0075 | Middle East |
| United Kingdom | 2678.5 | Aa1 | 0.004 | 0.0635 | 0.006 | Western Europe |
| United States of America | 16768.4 | Aaa | 0 | 0.0575 | 0 | North America |
| Uruguay | 55.7 | Baa2 | 0.019 | 0.086 | 0.028499999999999998 | Central and South America |
| Venezuela | 438.3 | Caa1 | 0.075 | 0.16999999999999998 | 0.11249999999999999 | Central and South America |
| Vietnam | 171.4 | B1 | 0.045 | 0.125 | 0.0675 | Asia |
| Zambia | 26.8 | B1 | 0.045 | 0.125 | 0.0675 | Africa |

## Sovereign Ratings (Moody's)

| Country | S&P Rating | Moody's rating |
|---|---|---|
| Abu Dhabi | AA | Aa2 |
| Albania | B | B1 |
| Andorra (Principality of) | BBB+ | Baa1 |
| Angola | BB- | Ba2 |
| Argentina | CCC+ | Caa1 |
| Armenia | NA | Ba2 |
| Aruba | BBB+ | B3 |
| Australia | AAA | Aaa |
| Austria | AA+ | Aaa |
| Azerbaijan | BBB- | Baa3 |
| Bahamas | BBB | Baa2 |
| Bahrain | BBB | Baa2 |
| Bangladesh | BB- | Ba3 |
| Barbados | B | B3 |
| Belarus | B- | B3 |
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
| Egypt | B- | Caa1 |
| El Salvador | B+ | Ba3 |
| Estonia | AA- | A1 |
| Ethiopia | B | B1 |
| Fiji | B | B1 |
| Finland | AA+ | Aaa |
| France | AA | Aa1 |
| Gabon | BB- | Ba3 |
| Georgia | BB- | Ba3 |
| Germany | AAA | Aaa |
| Ghana | B- | B2 |
| Greece | B | Caa1 |
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
| Jamaica | B- | Caa3 |
| Japan | AA- | A1 |
| Jersey (States of) | AA+ | Aa1 |
| Jordan | BB- | B1 |
| Kazakhstan | BBB+ | Baa2 |
| Kenya | B+ | B1 |
| Korea | AA- | Aa3 |
| Kuwait | AA | Aa2 |
| Latvia | A- | Baa1 |
| Lebanon | B- | B2 |
| Liechtenstein | AAA | Aaa |
| Lithuania | A- | Baa1 |
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
| Pakistan | B- | Caa1 |
| Panama | BBB | Baa2 |
| Papua New Guinea | B+ | B1 |
| Paraguay | BB | Ba2 |
| Peru | A- | A3 |
| Philippines | BBB | Baa2 |
| Poland | A | A2 |
| Portugal | BB | Ba1 |
| Qatar | AA | Aa2 |
| Ras Al Khaimah (Emirate of) | A | A2 |
| Romania | BBB- | Baa3 |
| Russia | BBB | Baa2 |
| Rwanda | B | B2 |
| Saudi Arabia | AA- | Aa3 |
| Senegal | B+ | B1 |
| Serbia | BB- | B1 |
| Sharjah | A | A3 |
| Singapore | AAA | Aaa |
| Slovakia | A | A2 |
| Slovenia | A- | Ba1 |
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
| Trinidad and Tobago | A | Baa1 |
| Tunisia | NA | Ba3 |
| Turkey | BBB | Baa3 |
| Turks and Caicos Islands | BBB+ | Baa1 |
| Uganda | B | B1 |
| Ukraine | CCC+ | Caa3 |
| United Arab Emirates | NA | Aa2 |
| United Kingdom | AAA | Aa1 |
| United States of America | AA+ | Aaa |
| Uruguay | BBB- | Baa2 |
| Venezuela | CCC+ | Caa1 |
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

## 10-year CDS Spreads

| Country | Moody's rating | CDS Spread adj for US | Updated: January 5, 2015 |
|---|---|---|---|
| Abu Dhabi | Aa2 | 0.011179999999999999 |  |
| Albania | B1 | NA |  |
| Andorra (Principality of) | Baa1 | NA |  |
| Angola | Ba2 | NA |  |
| Argentina | Caa1 | 0.83165 |  |
| Armenia | Ba2 | NA |  |
| Aruba | B3 | NA |  |
| Australia | Aaa | 0.00662 |  |
| Austria | Aaa | 0.005 |  |
| Azerbaijan | Baa3 | NA |  |
| Bahamas | Baa2 | NA |  |
| Bahrain | Baa2 | 0.02865 |  |
| Bangladesh | Ba3 | NA |  |
| Barbados | B3 | NA |  |
| Belarus | B3 | NA |  |
| Belgium | Aa3 | 0.0089 |  |
| Belize | Caa2 | NA |  |
| Bermuda | A1 | NA |  |
| Bolivia | Ba3 | NA |  |
| Bosnia and Herzegovina | B3 | NA |  |
| Botswana | A2 | NA |  |
| Brazil | Baa2 | 0.0286 |  |
| Bulgaria | Baa2 | 0.02682 |  |
| Burkina Faso | B3 | NA |  |
| Cambodia | B2 | NA |  |
| Cameroon | B2 | NA |  |
| Canada | Aaa | NA |  |
| Cayman Islands | Aa3 | NA |  |
| Cape Verde | B2 | NA |  |
| Chile | Aa3 | 0.01455 |  |
| China | Aa3 | 0.014740000000000001 |  |
| Colombia | Baa2 | 0.02263 |  |
| Congo (Democratic Republic of) | B3 | NA |  |
| Congo (Republic of) | Ba3 | NA |  |
| Cook Islands | B1 | NA |  |
| Costa Rica | Ba1 | 0.03274 |  |
| Côte d'Ivoire | B1 | NA |  |
| Croatia | Ba1 | 0.033389999999999996 |  |
| Cuba | Caa2 | NA |  |
| Curacao | A3 | NA |  |
| Cyprus | B3 | 0.060360000000000004 |  |
| Czech Republic | A1 | 0.00943 |  |
| Denmark | Aaa | 0.0048 |  |
| Dominican Republic | B1 | NA |  |
| Ecuador | B3 | NA |  |
| Egypt | Caa1 | 0.03254 |  |
| El Salvador | Ba3 | NA |  |
| Estonia | A1 | 0.00885 |  |
| Ethiopia | B1 | NA |  |
| Fiji | B1 | NA |  |
| Finland | Aaa | 0.005 |  |
| France | Aa1 | 0.00911 |  |
| Gabon | Ba3 | NA |  |
| Georgia | Ba3 | NA |  |
| Germany | Aaa | 0.0043 |  |
| Ghana | B2 | NA |  |
| Greece | Caa1 | 0.10453 |  |
| Guatemala | Ba1 | NA |  |
| Guernsey (States of) | Aa1 | NA |  |
| Honduras | B3 | NA |  |
| Hong Kong | Aa1 | 0.00805 |  |
| Hungary | Ba1 | 0.02326 |  |
| Iceland | Baa3 | 0.01958 |  |
| India | Baa3 | 0.02334 |  |
| Indonesia | Baa3 | 0.02507 |  |
| Ireland | Baa1 | 0.0095 |  |
| Isle of Man | Aa1 | NA |  |
| Israel | A1 | 0.0011300000000000001 |  |
| Italy | Baa2 | 0.0203 |  |
| Jamaica | Caa3 | NA |  |
| Japan | A1 | 0.01241 |  |
| Jersey (States of) | Aa1 | NA |  |
| Jordan | B1 | NA |  |
| Kazakhstan | Baa2 | 0.03847 |  |
| Kenya | B1 | NA |  |
| Korea | Aa3 | 0.00855 |  |
| Kuwait | Aa2 | NA |  |
| Latvia | Baa1 | 0.016059999999999998 |  |
| Lebanon | B2 | 0.04378 |  |
| Liechtenstein | Aaa | NA |  |
| Lithuania | Baa1 | 0.01574 |  |
| Luxembourg | Aaa | NA |  |
| Macao | Aa2 | NA |  |
| Macedonia | Ba3 | NA |  |
| Malaysia | A3 | 0.01841 |  |
| Malta | A3 | NA |  |
| Mauritius | Baa1 | NA |  |
| Mexico | A3 | 0.01738 |  |
| Moldova | B3 | NA |  |
| Mongolia | B2 | NA |  |
| Montenegro | Ba3 | NA |  |
| Montserrat | Baa3 | NA |  |
| Morocco | Ba1 | 0.02242 |  |
| Mozambique | B1 | NA |  |
| Namibia | Baa3 | NA |  |
| Netherlands | Aaa | 0.0047 |  |
| New Zealand | Aaa | 0.0069900000000000006 |  |
| Nicaragua | B3 | NA |  |
| Nigeria | Ba3 | NA |  |
| Norway | Aaa | 0.003 |  |
| Oman | A1 | NA |  |
| Pakistan | Caa1 | 0.10103999999999999 |  |
| Panama | Baa2 | 0.01775 |  |
| Papua New Guinea | B1 | NA |  |
| Paraguay | Ba2 | NA |  |
| Peru | A3 | 0.01923 |  |
| Philippines | Baa2 | 0.01671 |  |
| Poland | A2 | 0.0115 |  |
| Portugal | Ba1 | 0.02781 |  |
| Qatar | Aa2 | 0.0126 |  |
| Ras Al Khaimah (Emirate of) | A2 | NA |  |
| Romania | Baa3 | 0.01924 |  |
| Russia | Baa2 | 0.05315 |  |
| Rwanda | B2 | NA |  |
| Saudi Arabia | Aa3 | 0.0108 |  |
| Senegal | B1 | NA |  |
| Serbia | B1 | NA |  |
| Sharjah | A3 | NA |  |
| Singapore | Aaa | NA |  |
| Slovakia | A2 | 0.01014 |  |
| Slovenia | Ba1 | 0.018330000000000003 |  |
| South Africa | Baa2 | 0.02645 |  |
| Spain | Baa2 | 0.0148 |  |
| Sri Lanka | B1 | NA |  |
| St. Maarten | Baa1 | NA |  |
| St. Vincent & the Grenadines | B3 | NA |  |
| Suriname | Ba3 | NA |  |
| Sweden | Aaa | 0.0034 |  |
| Switzerland | Aaa | 0.00405 |  |
| Taiwan | Aa3 | NA |  |
| Thailand | Baa1 | 0.01596 |  |
| Trinidad and Tobago | Baa1 | NA |  |
| Tunisia | Ba3 | 0.03067 |  |
| Turkey | Baa3 | 0.02462 |  |
| Turks and Caicos Islands | Baa1 | NA |  |
| Uganda | B1 | NA |  |
| Ukraine | Caa3 | 0.15434 |  |
| United Arab Emirates | Aa2 | 0.012320000000000001 |  |
| United Kingdom | Aa1 | 0.0046 |  |
| United States of America | Aaa | 0 |  |
| Uruguay | Baa2 | NA |  |
| Venezuela | Caa1 | 0.17753 |  |
| Vietnam | B1 | 0.028360000000000003 |  |
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

| Country | S&P Rating | Moody's Rating | S&P local currency rating | Moody's Local Currency Rating |
|---|---|---|---|---|
| Abu Dhabi | AA | Aa2 | Abu Dhabi (Emirate of) | Abu Dhabi |
| Albania | B | B1 | Albania (Republic of) | Albania |
| Andorra (Principality of) | BBB+ | NA | Andorra (Principality of) |  |
| Angola | BB- | Ba2 | Angola (Republic of) | Angola |
| Argentina | CCC+ | Caa1 | Argentina (Republic of) (Unsolicited Ratings) | Argentina |
| Armenia | NA | Ba2 |  | Armenia |
| Aruba | BBB+ | NA | Aruba |  |
| Australia | AAA | Aaa | Australia (Commonwealth of) (Unsolicited Ratings) | Australia |
| Austria | AA+ | Aaa | Austria (Republic of) | Austria |
| Azerbaijan | BBB- | Baa3 | Azerbaijan (Republic of) | Azerbaijan |
| Bahamas | BBB | Baa2 | Bahamas | Bahamas |
| Bahrain | BBB | Baa2 | Bahrain (Kingdom of) | Bahrain |
| Bangladesh | BB- | Ba3 | Bangladesh (People's Republic of) | Bangladesh |
| Barbados | B | B3 | Barbados | Barbados |
| Belarus | B- | B3 | Belarus (Republic of) | Belarus |
| Belgium | AA | Aa3 | Belgium (Kingdom of) (Unsolicited Ratings) | Belgium |
| Belize | B- | Caa2 | Belize | Belize |
| Bermuda | AA- | A1 | Bermuda | Bermuda |
| Bolivia | BB | Ba3 | Bolivia (Plurinational State of) | Bolivia |
| Bosnia and Herzegovina | B | B3 | Bosnia and Herzegovina | Bosnia and Herzegovina |
| Botswana | A- | A2 | Botswana (Republic of) | Botswana |
| Brazil | BBB+ | Baa2 | Brazil (Federative Republic of) | Brazil |
| Bulgaria | BB+ | Baa2 | Bulgaria (Republic of) | Bulgaria |
| Burkina Faso | B- | NA | Burkina Faso |  |
| Cambodia | NA | B2 |  | Cambodia |
| Cameroon | B | NA | Cameroon |  |
| Canada | AAA | Aaa | Canada | Canada |
| Cayman Islands | NA | Aa3 |  | Cayman Islands |
| Cape Verde | B | NA | Cape Verde |  |
| Chile | AA+ | Aa3 | Chile (Republic of) | Chile |
| China | AA- | Aa3 | China (People's Republic of ) | China |
| Colombia | BBB+ | Baa2 | Colombia (Republic of) | Colombia |
| Congo (Democratic Republic of) | B- | B3 | Congo (Democratic Republic of) | Congo (Democratic Republic of) |
| Congo (Republic of) | B+ | Ba3 | Congo (Republic of) | Congo (Republic of) |
| Cook Islands | B+ | NA | Cook Islands |  |
| Costa Rica | BB | Ba1 | Costa Rica (Republic of) | Costa Rica |
| Côte d'Ivoire | NA | B1 |  | Côte d'Ivoire |
| Croatia | BB | Ba1 | Croatia (Republic of) | Croatia |
| Cuba | NA | Caa2 |  | Cuba |
| Curacao | A- | NA | Curacao |  |
| Cyprus | B+ | B3 | Cyprus (Republic of) | Cyprus |
| Czech Republic | AA | A1 | Czech Republic | Czech Republic |
| Denmark | AAA | Aaa | Denmark (Kingdom of) | Denmark |
| Dominican Republic | B+ | B1 | Dominican Republic | Dominican Republic |
| Ecuador | B+ | B3 | Ecuador (Republic of) | Ecuador |
| Egypt | B- | Caa1 | Egypt (Arab republic of) | Egypt |
| El Salvador | B+ | Ba3 | El Salvador (Republic of) | El Salvador |
| Estonia | AA- | A1 | Estonia (Republic of) | Estonia |
| Ethiopia | B | B1 | Ethiopia (Federal Democratic Republic of) | Ethiopia |
| Fiji | B | B1 | Fiji | Fiji |
| Finland | AA+ | Aaa | Finland (Republic of) | Finland |
| France | AA | Aa1 | France (Republic of) (Unsolicited Ratings) | France |
| Gabon | BB- | Ba3 | Gabonese Republic | Gabon |
| Georgia | BB- | Ba3 | Georgia (Government of) | Georgia |
| Germany | AAA | Aaa | Germany (Federal Republic of) (Unsolicited Ratings) | Germany |
| Ghana | B- | B2 | Ghana (Republic of) | Ghana |
| Greece | B | Caa1 | Greece (Hellenic Republic) | Greece |
| Guatemala | BB+ | Ba1 | Guatemala (Republic of) | Guatemala |
| Guernsey (States of) | AA+ | NA | Guernsey (States of) |  |
| Honduras | B | B3 | Honduras (Republic of) | Honduras |
| Hong Kong | AAA | Aa1 | Hong Kong (Special Administrative Region) | Hong Kong |
| Hungary | BB | Ba1 | Hungary | Hungary |
| Iceland | BBB- | Baa3 | Iceland (Republic of) | Iceland |
| India | BBB- | Baa3 | India (Republic of) (Unsolicited Ratings) | India |
| Indonesia | BB+ | Baa3 | Indonesia (Republic of) | Indonesia |
| Ireland | A | Baa1 | Ireland (Republic of) | Ireland |
| Isle of Man | NA | Aa1 |  | Isle of Man |
| Israel | A+ | A1 | Israel (State of) | Israel |
| Italy | BBB- | Baa2 | Italy (Republic of) (Unsolicited Ratings) | Italy |
| Jamaica | B- | Caa3 | Jamaica | Jamaica |
| Japan | AA- | A1 | Japan (Unsolicited Ratings) | Japan |
| Jersey (States of) | AA+ | NA | Jersey (States of) |  |
| Jordan | BB- | B1 | Jordan (Hashemite Kingdom of) | Jordan |
| Kazakhstan | BBB+ | Baa2 | Kazakhstan (Republic of) | Kazakhstan |
| Kenya | B+ | B1 | Kenya (Republic of) | Kenya |
| Korea | AA- | Aa3 | Korea (Republic of) | Korea |
| Kuwait | AA | Aa2 | Kuwait (State of) | Kuwait |
| Latvia | A- | Baa1 | Latvia (Republic of) | Latvia |
| Lebanon | B- | B2 | Lebanon (Republic of) | Lebanon |
| Liechtenstein | AAA | NA | Liechtenstein |  |
| Lithuania | A- | Baa1 | Lithuania (Republic of) | Lithuania |
| Luxembourg | AAA | Aaa | Luxembourg (Grand Duchy of) | Luxembourg |
| Macao | NA | Aa2 |  | Macao |
| Macedonia | BB- | NA | Macedonia |  |
| Malaysia | A | A3 | Malaysia | Malaysia |
| Malta | BBB+ | A3 | Malta (Republic of) | Malta |
| Mauritius | NA | Baa1 |  | Mauritius |
| Mexico | A | A3 | Mexico | Mexico |
| Moldova | NA | B3 |  | Moldova |
| Mongolia | B+ | B2 | Mongolia | Mongolia |
| Montenegro | B+ | Ba3 | Montenegro (Republic of) | Montenegro |
| Montserrat | BBB- | NA | Montserrat |  |
| Morocco | BBB- | Ba1 | Morocco (Kingdom of) | Morocco |
| Mozambique | B | B1 | Mozambique (Republic of) | Mozambique |
| Namibia | NA | Baa3 |  | Namibia |
| Netherlands | AA+ | Aaa | Netherlands (State of The) (Unsolicited Ratings) | Netherlands |
| New Zealand | AA+ | Aaa | New Zealand | New Zealand |
| Nicaragua | NA | B3 |  | Nicaragua |
| Nigeria | BB- | Ba3 | Nigeria (Federal Republic of) | Nigeria |
| Norway | AAA | Aaa | Norway (Kingdom of) | Norway |
| Oman | A | A1 | Oman (Sultanate of) | Oman |
| Pakistan | B- | Caa1 | Pakistan (Islamic Republic of) | Pakistan |
| Panama | BBB | Baa2 | Panama (Republic of) | Panama |
| Papua New Guinea | B+ | B1 | Papua New Guinea (Independent State of) | Papua New Guinea |
| Paraguay | BB | Ba2 | Paraguay (Republic of) | Paraguay |
| Peru | A- | A3 | Peru (Republic of) | Peru |
| Philippines | BBB | Baa2 | Philippines (Republic of the) | Philippines |
| Poland | A | A2 | Poland (Republic of) | Poland |
| Portugal | BB | Ba1 | Portugal (Republic of) (Unsolicited Ratings) | Portugal |
| Qatar | AA | Aa2 | Qatar (State of) | Qatar |
| Ras Al Khaimah (Emirate of) | A | NA | Ras Al Khaimah (Emirate of) |  |
| Romania | BBB- | Baa3 | Romania | Romania |
| Russia | BBB | Baa2 | Russian Federation | Russia |
| Rwanda | B | NA | Rwanda |  |
| Saudi Arabia | AA- | Aa3 | Saudi Arabia (Kingdom of) | Saudi Arabia |
| Senegal | B+ | B1 | Senegal (Republic of) | Senegal |
| Serbia | BB- | B1 | Serbia (Republic of) | Serbia |
| Sharjah | A | A3 | Sharjah (Emirate of) | Sharjah |
| Singapore | AAA | Aaa | Singapore (Republic of) (Unsolicited Ratings) | Singapore |
| Slovakia | A | A2 | Slovak Republic | Slovakia |
| Slovenia | A- | Ba1 | Slovenia (Republic of) | Slovenia |
| South Africa | BBB+ | Baa2 | South Africa (Republic of) | South Africa |
| Spain | BBB | Baa2 | Spain (Kingdom of) | Spain |
| Sri Lanka | B+ | B1 | Sri Lanka (Democratic Socialist Republic of) | Sri Lanka |
| St. Maarten | NA | Baa1 |  | St. Maarten |
| St. Vincent & the Grenadines | NA | B3 |  | St. Vincent & the Grenadines |
| Suriname | BB- | Ba3 | Suriname (The Republic of) | Suriname |
| Sweden | AAA | Aaa | Sweden (Kingdom of) (Unsolicited Ratings) | Sweden |
| Switzerland | AAA | Aaa | Swiss Confederation (Unsolicited Ratings) | Switzerland |
| Taiwan | AA- | Aa3 | Taiwan (Republic of China) (Unsolicited Ratings) | Taiwan |
| Thailand | A- | Baa1 | Thailand (Kingdom of) | Thailand |
| Trinidad and Tobago | A | Baa1 | Trinidad and Tobago (Republic of) | Trinidad and Tobago |
| Tunisia | NA | Ba3 |  | Tunisia |
| Turkey | BBB | Baa3 | Turkey (Republic of) (Unsolicited Ratings) | Turkey |
| Turks and Caicos Islands | BBB+ | NA | Turks and Caicos Islands |  |
| Uganda | B | B1 | Uganda (Republic of) | Uganda |
| Ukraine | CCC+ | Caa3 | Ukraine | Ukraine |
| United Arab Emirates | NA | Aa2 |  | United Arab Emirates |
| United Kingdom | AAA | Aa1 | United Kingdom (Unsolicited Ratings) | United Kingdom |
| United States of America | AA+ | Aaa | United States of America (Unsolicited Ratings) | United States of America |
| Uruguay | BBB- | Baa2 | Uruguay (Oriental Republic of) | Uruguay |
| Venezuela | CCC+ | Caa1 | Venezuela | Venezuela |
| Vietnam | BB- | B1 | Vietnam (Socialist Republic of) | Vietnam |
| Zambia | B+ | B1 | Zambia (Republic of) | Zambia |

## PRS Worksheet

| Country | PRS Score (1/15) | Country ERP (if available) | Group ERP |
|---|---|---|---|
| Somalia | 37.25 |  | 0.2375 |
| Syria | 41.5 |  |  |
| Guinea | 47.75 |  |  |
| Liberia | 50 |  |  |
| Sudan | 50 |  |  |
| Ukraine | 54.25 | 0.2075 | 0.1775 |
| Zimbabwe | 54.5 |  |  |
| Venezuela | 54.75 | 0.17 |  |
| Congo, Dem. Republic | 55.25 | 0.155 |  |
| Korea, D.P.R. | 55.75 |  |  |
| Niger | 55.75 |  | 0.14 |
| Mozambique | 56 | 0.125 |  |
| Uganda | 58 | 0.125 |  |
| Lebanon | 58.5 | 0.14 |  |
| Pakistan | 58.5 | 0.17 |  |
| Egypt | 59 | 0.17 | 0.15 |
| Belarus | 59.25 | 0.155 |  |
| Ethiopia | 59.25 | 0.125 |  |
| Libya | 59.25 |  |  |
| Yemen, Republic | 59.5 |  |  |
| Togo | 60.25 |  | 0.14 |
| Mali | 60.5 |  |  |
| Haiti | 61 |  |  |
| Malawi | 61 |  |  |
| Ghana | 61.25 | 0.14 |  |
| Iran | 61.25 |  |  |
| Sierra Leone | 61.5 |  | 0.1135 |
| Turkey | 61.5 | 0.0905 |  |
| Guyana | 61.75 |  |  |
| Iraq | 61.75 |  |  |
| Cote d'Ivoire | 62.25 | 0.125 |  |
| Sri Lanka | 62.25 | 0.125 |  |
| Tanzania | 62.25 |  |  |
| Guinea-Bissau | 62.5 |  | 0.11825 |
| Nigeria | 62.5 | 0.1115 |  |
| Gambia | 62.75 |  |  |
| Myanmar | 62.75 |  |  |
| Senegal | 62.75 | 0.125 |  |
| Armenia | 63 | 0.1025 | 0.12650000000000003 |
| Burkina Faso | 63 | 0.155 |  |
| Serbia  | 63 | 0.125 |  |
| Kenya | 63.25 | 0.125 |  |
| Cameroon | 63.5 | 0.14 |  |
| Madagascar | 63.5 |  |  |
| Tunisia | 63.5 | 0.1115 |  |
| Argentina | 63.75 | 0.17 | 0.13875 |
| Moldova | 63.75 | 0.155 |  |
| Bangladesh | 64 | 0.1115 |  |
| Greece | 64.25 | 0.17 |  |
| Mongolia | 64.25 | 0.14 |  |
| Russia | 64.25 | 0.086 |  |
| Honduras | 64.75 | 0.155 | 0.15050000000000002 |
| Nicaragua | 64.75 | 0.155 |  |
| Papua New Guinea | 64.75 | 0.125 |  |
| Jordan | 65 | 0.125 |  |
| Cuba | 65.5 | 0.1925 |  |
| Angola | 65.75 | 0.1025 | 0.11364285714285714 |
| Albania | 66.25 | 0.125 |  |
| El Salvador | 66.75 | 0.1115 |  |
| Guatemala | 66.75 | 0.095 |  |
| Ecuador | 67 | 0.155 |  |
| Thailand | 67 | 0.0815 |  |
| Zambia | 67 | 0.125 |  |
| Indonesia | 67.25 | 0.0905 | 0.08937499999999998 |
| Morocco | 67.25 | 0.095 |  |
| South Africa | 67.25 | 0.086 |  |
| Brazil | 67.5 | 0.086 |  |
| Algeria | 68.25 |  |  |
| Colombia | 68.5 | 0.086 | 0.11099999999999999 |
| Croatia | 68.5 | 0.095 |  |
| Jamaica | 68.5 | 0.2075 |  |
| Congo, Republic | 68.75 | 0.1115 |  |
| India | 68.75 | 0.0905 |  |
| Mexico | 68.75 | 0.0755 |  |
| Latvia | 69 | 0.0815 | 0.0986 |
| Bulgaria | 69.25 | 0.086 |  |
| Cyprus | 69.25 | 0.155 |  |
| Estonia | 69.5 | 0.068 |  |
| Paraguay | 69.5 | 0.1025 |  |
| Slovenia | 70 | 0.095 | 0.09559999999999999 |
| Vietnam | 70 | 0.125 |  |
| Bahrain | 70.5 | 0.086 |  |
| Kazakhstan | 70.5 | 0.086 |  |
| Spain | 70.5 | 0.086 |  |
| France | 70.75 | 0.0635 | 0.08835714285714284 |
| Gabon | 71.25 | 0.1115 |  |
| Dominican Republic | 71.5 | 0.125 |  |
| Peru | 71.5 | 0.0755 |  |
| Romania | 71.5 | 0.0905 |  |
| China, Peoples' Rep. | 71.75 | 0.0665 |  |
| Panama | 71.75 | 0.086 |  |
| Suriname | 72 | 0.1115 | 0.0893 |
| Uruguay | 72 | 0.086 |  |
| Hungary | 72.25 | 0.095 |  |
| Israel | 72.25 | 0.068 |  |
| Philippines | 72.25 | 0.086 |  |
| Italy | 72.5 | 0.086 | 0.09156 |
| Portugal | 73.25 | 0.095 |  |
| Costa Rica | 73.5 | 0.095 |  |
| Bolivia | 73.75 | 0.1115 |  |
| Slovakia | 74.25 | 0.0703 |  |
| Poland | 75.25 | 0.0703 | 0.07988333333333335 |
| Azerbaijan | 75.75 | 0.0905 |  |
| Bahamas | 75.75 | 0.086 |  |
| Chile | 75.75 | 0.0665 |  |
| Malta | 75.75 | 0.0755 |  |
| Namibia | 75.75 | 0.0905 |  |
| Belgium | 76 | 0.0665 | 0.07100000000000001 |
| Lithuania | 76 | 0.0815 |  |
| Trinidad & Tobago | 76.75 | 0.0815 |  |
| United States | 77.25 | 0.0575 |  |
| Czech Republic | 78.25 | 0.068 |  |
| Australia | 78.5 | 0.0575 | 0.06875 |
| Ireland | 78.5 | 0.0815 |  |
| Japan | 78.75 | 0.068 |  |
| Malaysia | 78.75 | 0.0755 |  |
| Saudi Arabia | 78.75 | 0.0665 |  |
| United Kingdom | 78.75 | 0.0635 |  |
| Finland | 79 | 0.0575 | 0.0664 |
| Austria | 79.5 | 0.0575 |  |
| Botswana | 79.5 | 0.0703 |  |
| Iceland | 79.75 | 0.0905 |  |
| Hong Kong | 81 | 0.0635 |  |
| Netherlands | 81 | 0.0575 |  |
| Oman | 81 | 0.068 |  |
| Denmark | 81.25 | 0.0575 | 0.0608 |
| Korea, Republic | 81.5 | 0.0665 |  |
| Kuwait | 81.5 | 0.065 |  |
| Canada | 82 | 0.0575 |  |
| Sweden | 82 | 0.0575 |  |
| Qatar | 82.25 | 0.065 | 0.0623 |
| United Arab Emirates | 82.75 | 0.065 |  |
| New Zealand | 83 | 0.0575 |  |
| Taiwan | 83 | 0.0665 |  |
| Germany | 84.5 | 0.0575 |  |
| Brunei | 87 |  | 0.0575 |
| Singapore | 87 | 0.0575 |  |
| Luxembourg | 87.5 | 0.0575 |  |
| Switzerland | 89.5 | 0.0575 |  |
| Norway | 90 | 0.0575 |  |
