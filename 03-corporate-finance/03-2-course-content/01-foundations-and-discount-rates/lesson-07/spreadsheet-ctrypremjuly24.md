## Explanation and FAQ
| Country Risk Premiums | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| To estimate the equity risk premium for a country, I start with a mature market premium and add an additional country risk premium, based upon the risk of the country in question. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Use the look up table in the next worksheet, to look up the statistics for an individual country or region. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Step 1: Estimating mature market risk premium | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| To estimate the mature market risk premium, I compute the implied equity risk premium for the S&P 500. To see the latest estimate for this number, go to my website and you can download the excel spreadsheet containing the implied premium | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Link to site: | http://www.damodaran.com | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Historical monthly ERP: | https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xls | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Step 2: Estimate the default spread for the country in question. I offer two choices, one based upon the local currency sovereign rating for the country from Moody's and the other is the CDS spread for the country (if one exists) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Moody's ratings: | http://www.moodys.com | NaN | (You will have to register, but it is free. Look under sovereign ratings) | NaN | NaN | NaN | NaN | NaN |
| Ratings to spreads: | Based upon my estimates of typical spreads for each ratings class. I compute these by averaging CDS spreads and sovereign US$ bond spreads by ratings class, at the start of every year. | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| CDS spreads: | Bloomberg | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| If you cannot find a country on this list, it is because that country does not have a sovereign rating or a sovereign CDS spread. Try the PRS worksheet in this spreadsheet for an alternate estimate. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Step 3: Convert the default spread into a country risk premium | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| With sovereign ratings default spreads, you have two choices: | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Choice 1: Use the default spread as the measure of the additional country risk premium. To make this choice, go into the ERP worksheet and set cell E5 to 1.00. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Choice 2: Scale the default spread up to reflect the higher risk of equity in the market, relative to the default spread. I used the ratio of the S&P Emerging Market Equity Index std deviation to the iShares Emerging Market Bond Index standard deviation | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| With CDS spreads, I compute the base number in two steps | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Substep 1: Since the base equity premium is computed for the US, and the US has a CDS spread, I subtracted out the US CDS spread from the CDS for other markets. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For simplicity (and since it does not make a big difference), I assume that any country that has a CDS spread lower than the US will have a zero country risk premium and end up with a total equity risk premium equal to the US. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Substep 2: I apply the scaling factor that you chose for the default spreads to this number to get a country risk premium. The default scaling is set at the my most recent year's estimate, but you can change it to 1, if you would | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| prefer not to scale the default spread. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Step 4: Compute a total equity risk premium | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Add the mature market premium from step 1 to the country risk premium from step 3 to get a total equity risk premium. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Step 5: Compute regional averages and regional weighted averages | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For the regional averages, I use a simple average of the total and country risk premiums by region | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For the weighted averages, I use the World Bank GDP estimates from the most recent year. | NaN | NaN | NaN | NaN | NaN | NaN | NaN | https://data.worldbank.org/indicator/NY.GDP.MKTP.CD |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| If you are interested in a fuller explanation of these concepts, try these references: | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| My paper on equity risk premiums: | NaN | NaN | NaN | https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4398884 | NaN | NaN | NaN | NaN |
| My paper on country risk premiums: | NaN | NaN | NaN | https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4509578 | NaN | NaN | NaN | NaN |
| Watch my lectures on country risk premiums: | NaN | NaN | NaN | https://www.youtube.com/watch?v=aIRPvY2SQ94 | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | https://www.youtube.com/watch?v=D3IGn6tH03c | NaN | NaN | NaN | NaN |

## Summary of Most Recent Update
| Unnamed: 0 | Update Notes |
| --- | --- |
| Mature Marlet Premium | The implied equity risk premium for the S&P 500, which is my base premium dropped to 5% in this update. You can review the calcualtion in this spreadsheet. (https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPJuly24.xlsx) |
| Sovereign Ratings | The ratings (Moody's and S&P)  have been updated to reflect the most recent ratings. (See Ratings Worksheet) |
| Default Spreads | The default spreads have dropped as some of the market fears from the start of 2023 have subsdied. The change in default spredas is computed by looking at percentage changes in sovereign CDS spreads over the period>. (See Default Spreads for Ratings worksheet) |
| Relative Equity Market Volatility | The biggest change in this update is in this measure. For the last few years, I have used the coefficient of variation in emerging market bond yields and the standard deviation of returns in emerging market equities. In this iteration, I have replaced the former with an emerging market sovereign bond ETF returns, thus creating more consistency in the calcuatlions. Whiel this change does not create a substantive shift in the numbers in this iteration, I think it is a more solid basis for computing this value in future ones. |
| Bottom Line | The combination of a lower base mature market premium and lower sovereign default spreads has led to lower equity risk premiums across the board, a climb down from historically high numbers at the start of the year. |

## Country Lookup
| To look up the equity risk premium for a country, use this worksheet | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 |
| --- | --- | --- | --- |
| Country | Angola | NaN | If you cannot find a country on this list, it is because that country does not have a sovereign rating |
| NaN | NaN | NaN | or a sovereign CDS spread. Try the PRS worksheet in this spreadsheet for an alternate estimate. |
| Moody's sovereign rating | B3 | Local currency | NaN |
| S&P sovereign rating | B- | Local currency | NaN |
| CDS spread | 0.0678 | NaN | NaN |
| Excess CDS spread (over US CDS) | 0.0632 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| Country Default Spread (based on rating) | 0.061153 | NaN | NaN |
| Country Risk Premium (Rating) | 0.079379 | NaN | NaN |
| Equity Risk Premium (Rating) | 0.120579 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| Country Risk Premium (CDS) | 0.082037 | NaN | NaN |
| Equity Risk Premium (CDS) | 0.123237 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| To look up the equity risk premium for a region, use this worksheet | NaN | NaN | NaN |
| Region | Asia | NaN | NaN |
| NaN | NaN | NaN | NaN |
| Country Risk Premium (simple average)) | 0.047269 | NaN | NaN |
| Total Equity Risk Premium (simple average) | 0.088369 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| Country Risk Premium (GDP weighted) | 0.014022 | NaN | NaN |
| Total Equity Risk Premium (GDP weighted) | 0.055122 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| To construct your own regional ERP, use the data on GDP and ERP for countries in the Regional Weighted Averages Worksheet | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN |
| For countries not on the list above, try this frontier market list | NaN | NaN | NaN |
| Country | Zimbabwe | NaN | NaN |
| NaN | NaN | NaN | NaN |
| PRS Score | 58 | NaN | NaN |
| ERP based on PRS Score | 0.151154 | NaN | NaN |

## ERPs by country
| Country and Equity Risk Premiums | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 | Unnamed: 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Date of update: | 2024-07-01 00:00:00 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Enter the current risk premium for a mature equity market | NaN | NaN | NaN | 0.0412 | Implied ERP for S&P 500 | NaN | NaN | NaN | NaN | NaN |
| Do you want to adjust the country default spread for the additional volatility of the equity market to get to a country premium? | NaN | NaN | NaN | Yes | NaN | NaN | NaN | NaN | NaN | NaN |
| If yes, enter the multiplier to use on the default spread (See worksheet for volatility numbers for selected emerging markets) | NaN | NaN | NaN | 1.298047 | See "Relative Equity Volatilty" worksheet | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Country | Africa | Moody's rating | Rating-based Default Spread | Total Equity Risk Premium | Country Risk Premium | Sovereign CDS, net of US | Total Equity Risk Premium2 | Country Risk Premium3 | Has to be sorted in ascending order | NaN |
| Abu Dhabi | Middle East | Aa2 | 0.004645 | 0.047229 | 0.006029 | 0.0027 | 0.044705 | 0.003505 | Rating | Default spread in basis points |
| Albania | Eastern Europe & Russia | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | A1 | 66.350422 |
| Andorra (Principality of) | Western Europe | Baa1 | 0.015039 | 0.060722 | 0.019522 | NaN | NaN | NaN | A2 | 79.620506 |
| Angola | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | 0.0632 | 0.123237 | 0.082037 | A3 | 112.795717 |
| Argentina | Central and South America | Ca | 0.112906 | 0.187758 | 0.146558 | NaN | NaN | NaN | Aa1 | 37.598572 |
| Armenia | Eastern Europe & Russia | Ba3 | 0.033839 | 0.085124 | 0.043924 | NaN | NaN | NaN | Aa2 | 46.445295 |
| Aruba | Caribbean | Baa3 | 0.020679 | 0.068043 | 0.026843 | NaN | NaN | NaN | Aa3 | 56.397858 |
| Australia | Australia & New Zealand | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | Aaa | 0 |
| Austria | Western Europe | Aa1 | 0.00376 | 0.04608 | 0.00488 | 0 | 0.0412 | 0 | B1 | 423.536857 |
| Azerbaijan | Eastern Europe & Russia | Ba1 | 0.023554 | 0.071775 | 0.030575 | NaN | NaN | NaN | B2 | 517.533288 |
| Bahamas | Caribbean | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | B3 | 611.529718 |
| Bahrain | Middle East | B2 | 0.051753 | 0.108378 | 0.067178 | 0.0194 | 0.066382 | 0.025182 | Ba1 | 235.543996 |
| Bangladesh | Asia | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | Ba2 | 283.095132 |
| Barbados | Caribbean | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | Ba3 | 338.38715 |
| Belarus | Eastern Europe & Russia | C | 0.175 | 0.268358 | 0.227158 | NaN | NaN | NaN | Baa1 | 150.394289 |
| Belgium | Western Europe | Aa3 | 0.00564 | 0.048521 | 0.007321 | 0 | 0.0412 | 0 | Baa2 | 179.146138 |
| Belize | Central and South America | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | Baa3 | 206.792147 |
| Benin | Africa | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | C | 1750 |
| Bermuda | Caribbean | A2 | 0.007962 | 0.051535 | 0.010335 | NaN | NaN | NaN | Ca | 1129.063006 |
| Bolivia | Central and South America | Caa3 | 0.094107 | 0.163355 | 0.122155 | NaN | NaN | NaN | Caa1 | 705.526149 |
| Bosnia and Herzegovina | Eastern Europe & Russia | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | Caa2 | 847.073715 |
| Botswana | Africa | A3 | 0.01128 | 0.055841 | 0.014641 | NaN | NaN | NaN | Caa3 | 941.070145 |
| Brazil | Central and South America | Ba2 | 0.02831 | 0.077947 | 0.036747 | 0.0211 | 0.068589 | 0.027389 | NR | NaN |
| Bulgaria | Eastern Europe & Russia | Baa1 | 0.015039 | 0.060722 | 0.019522 | 0.0081 | 0.051714 | 0.010514 | NaN | NaN |
| Burkina Faso | Africa | Caa1 | 0.070553 | 0.132781 | 0.091581 | NaN | NaN | NaN | NaN | NaN |
| Cambodia | Asia | B2 | 0.051753 | 0.108378 | 0.067178 | NaN | NaN | NaN | NaN | NaN |
| Cameroon | Africa | Caa1 | 0.070553 | 0.132781 | 0.091581 | 0.07 | 0.132063 | 0.090863 | NaN | NaN |
| Canada | North America | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Cape Verde | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Cayman Islands | Caribbean | Aa3 | 0.00564 | 0.048521 | 0.007321 | NaN | NaN | NaN | NaN | NaN |
| Chile | Central and South America | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0057 | 0.048599 | 0.007399 | NaN | NaN |
| China | Asia | A1 | 0.006635 | 0.049813 | 0.008613 | 0.0059 | 0.048858 | 0.007658 | NaN | NaN |
| Colombia | Central and South America | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0264 | 0.075468 | 0.034268 | NaN | NaN |
| Congo (Democratic Republic of) | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Congo (Republic of) | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | NaN | NaN |
| Cook Islands | Australia & New Zealand | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Costa Rica | Central and South America | B1 | 0.042354 | 0.096177 | 0.054977 | 0.0183 | 0.064954 | 0.023754 | NaN | NaN |
| Côte d'Ivoire | Africa | Ba2 | 0.02831 | 0.077947 | 0.036747 | NaN | NaN | NaN | NaN | NaN |
| Croatia | Eastern Europe & Russia | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0078 | 0.051325 | 0.010125 | NaN | NaN |
| Cuba | Caribbean | Ca | 0.112906 | 0.187758 | 0.146558 | NaN | NaN | NaN | NaN | NaN |
| Curacao | Caribbean | Baa3 | 0.020679 | 0.068043 | 0.026843 | NaN | NaN | NaN | NaN | NaN |
| Cyprus | Western Europe | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0047 | 0.047301 | 0.006101 | NaN | NaN |
| Czech Republic | Eastern Europe & Russia | Aa3 | 0.00564 | 0.048521 | 0.007321 | 0 | 0.0412 | 0 | NaN | NaN |
| Denmark | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Dominican Republic | Caribbean | Ba3 | 0.033839 | 0.085124 | 0.043924 | NaN | NaN | NaN | NaN | NaN |
| Ecuador | Central and South America | Caa3 | 0.094107 | 0.163355 | 0.122155 | 0.2151 | 0.32041 | 0.27921 | NaN | NaN |
| Egypt | Africa | Caa1 | 0.070553 | 0.132781 | 0.091581 | 0.0624 | 0.122198 | 0.080998 | NaN | NaN |
| El Salvador | Central and South America | Caa1 | 0.070553 | 0.132781 | 0.091581 | 0.0704 | 0.132582 | 0.091382 | NaN | NaN |
| Estonia | Eastern Europe & Russia | A1 | 0.006635 | 0.049813 | 0.008613 | 0.0031 | 0.045224 | 0.004024 | NaN | NaN |
| Ethiopia | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | 0.3113 | 0.445282 | 0.404082 | NaN | NaN |
| Fiji | Asia | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Finland | Western Europe | Aa1 | 0.00376 | 0.04608 | 0.00488 | 0 | 0.0412 | 0 | NaN | NaN |
| France | Western Europe | Aa2 | 0.004645 | 0.047229 | 0.006029 | 0.0005 | 0.041849 | 0.000649 | NaN | NaN |
| Gabon | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | NaN | NaN |
| Georgia | Eastern Europe & Russia | Ba2 | 0.02831 | 0.077947 | 0.036747 | NaN | NaN | NaN | NaN | NaN |
| Germany | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Ghana | Africa | Caa3 | 0.094107 | 0.163355 | 0.122155 | NaN | NaN | NaN | NaN | NaN |
| Greece | Western Europe | Ba1 | 0.023554 | 0.071775 | 0.030575 | 0.0085 | 0.052233 | 0.011033 | NaN | NaN |
| Guatemala | Central and South America | Ba1 | 0.023554 | 0.071775 | 0.030575 | NaN | NaN | NaN | NaN | NaN |
| Guernsey (States of) | Western Europe | A1 | 0.006635 | 0.049813 | 0.008613 | NaN | NaN | NaN | NaN | NaN |
| Honduras | Central and South America | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Hong Kong | Asia | Aa3 | 0.00564 | 0.048521 | 0.007321 | 0.0007 | 0.042109 | 0.000909 | NaN | NaN |
| Hungary | Eastern Europe & Russia | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0121 | 0.056906 | 0.015706 | NaN | NaN |
| Iceland | Western Europe | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0014 | 0.043017 | 0.001817 | NaN | NaN |
| India | Asia | Baa3 | 0.020679 | 0.068043 | 0.026843 | 0.0037 | 0.046003 | 0.004803 | NaN | NaN |
| Indonesia | Asia | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0082 | 0.051844 | 0.010644 | NaN | NaN |
| Iraq | Middle East | Caa1 | 0.070553 | 0.132781 | 0.091581 | 0.0349 | 0.086502 | 0.045302 | NaN | NaN |
| Ireland | Western Europe | Aa3 | 0.00564 | 0.048521 | 0.007321 | 0 | 0.0412 | 0 | NaN | NaN |
| Isle of Man | Western Europe | Aa3 | 0.00564 | 0.048521 | 0.007321 | NaN | NaN | NaN | NaN | NaN |
| Israel | Middle East | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0127 | 0.057685 | 0.016485 | NaN | NaN |
| Italy | Western Europe | Baa3 | 0.020679 | 0.068043 | 0.026843 | 0.0083 | 0.051974 | 0.010774 | NaN | NaN |
| Jamaica | Caribbean | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Japan | Asia | A1 | 0.006635 | 0.049813 | 0.008613 | 0 | 0.0412 | 0 | NaN | NaN |
| Jersey (States of) | Western Europe | Aa3 | 0.00564 | 0.048521 | 0.007321 | NaN | NaN | NaN | NaN | NaN |
| Jordan | Middle East | Ba3 | 0.033839 | 0.085124 | 0.043924 | NaN | NaN | NaN | NaN | NaN |
| Kazakhstan | Eastern Europe & Russia | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0091 | 0.053012 | 0.011812 | NaN | NaN |
| Kenya | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | 0.0496 | 0.105583 | 0.064383 | NaN | NaN |
| Korea | Asia | Aa2 | 0.004645 | 0.047229 | 0.006029 | 0 | 0.0412 | 0 | NaN | NaN |
| Kuwait | Middle East | A1 | 0.006635 | 0.049813 | 0.008613 | 0.0037 | 0.046003 | 0.004803 | NaN | NaN |
| Kyrgyzstan | Eastern Europe & Russia | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Laos | Asia | Caa3 | 0.094107 | 0.163355 | 0.122155 | NaN | NaN | NaN | NaN | NaN |
| Latvia | Eastern Europe & Russia | A3 | 0.01128 | 0.055841 | 0.014641 | 0.004 | 0.046392 | 0.005192 | NaN | NaN |
| Lebanon | Middle East | C | 0.175 | 0.268358 | 0.227158 | NaN | NaN | NaN | NaN | NaN |
| Liechtenstein | Western Europe | Aaa | 0 | 0.0412 | 0 | NaN | NaN | NaN | NaN | NaN |
| Lithuania | Eastern Europe & Russia | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0041 | 0.046522 | 0.005322 | NaN | NaN |
| Luxembourg | Western Europe | Aaa | 0 | 0.0412 | 0 | NaN | NaN | NaN | NaN | NaN |
| Macao | Asia | Aa3 | 0.00564 | 0.048521 | 0.007321 | NaN | NaN | NaN | NaN | NaN |
| Macedonia | Eastern Europe & Russia | Ba3 | 0.033839 | 0.085124 | 0.043924 | NaN | NaN | NaN | NaN | NaN |
| Malaysia | Asia | A3 | 0.01128 | 0.055841 | 0.014641 | 0.0035 | 0.045743 | 0.004543 | NaN | NaN |
| Maldives | Asia | Caa1 | 0.070553 | 0.132781 | 0.091581 | NaN | NaN | NaN | NaN | NaN |
| Mali | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | NaN | NaN |
| Malta | Western Europe | A2 | 0.007962 | 0.051535 | 0.010335 | NaN | NaN | NaN | NaN | NaN |
| Mauritius | Africa | Baa3 | 0.020679 | 0.068043 | 0.026843 | NaN | NaN | NaN | NaN | NaN |
| Mexico | Central and South America | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.013 | 0.058075 | 0.016875 | NaN | NaN |
| Moldova | Eastern Europe & Russia | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Mongolia | Asia | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Montenegro | Eastern Europe & Russia | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Montserrat | Caribbean | Baa3 | 0.020679 | 0.068043 | 0.026843 | NaN | NaN | NaN | NaN | NaN |
| Morocco | Africa | Ba1 | 0.023554 | 0.071775 | 0.030575 | 0.0089 | 0.052753 | 0.011553 | NaN | NaN |
| Mozambique | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | NaN | NaN |
| Namibia | Africa | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Netherlands | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| New Zealand | Australia & New Zealand | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Nicaragua | Central and South America | B2 | 0.051753 | 0.108378 | 0.067178 | 0.0578 | 0.116227 | 0.075027 | NaN | NaN |
| Niger | Africa | Caa3 | 0.094107 | 0.163355 | 0.122155 | NaN | NaN | NaN | NaN | NaN |
| Nigeria | Africa | Caa1 | 0.070553 | 0.132781 | 0.091581 | 0.0588 | 0.117525 | 0.076325 | NaN | NaN |
| Norway | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Oman | Middle East | Ba1 | 0.023554 | 0.071775 | 0.030575 | 0.0103 | 0.05457 | 0.01337 | NaN | NaN |
| Pakistan | Asia | Caa3 | 0.094107 | 0.163355 | 0.122155 | 0.1632 | 0.253041 | 0.211841 | NaN | NaN |
| Panama | Central and South America | Baa3 | 0.020679 | 0.068043 | 0.026843 | 0.0215 | 0.069108 | 0.027908 | NaN | NaN |
| Papua New Guinea | Asia | B2 | 0.051753 | 0.108378 | 0.067178 | NaN | NaN | NaN | NaN | NaN |
| Paraguay | Central and South America | Ba1 | 0.023554 | 0.071775 | 0.030575 | NaN | NaN | NaN | NaN | NaN |
| Peru | Central and South America | Baa1 | 0.015039 | 0.060722 | 0.019522 | 0.0082 | 0.051844 | 0.010644 | NaN | NaN |
| Philippines | Asia | Baa2 | 0.017915 | 0.064454 | 0.023254 | 0.0076 | 0.051065 | 0.009865 | NaN | NaN |
| Poland | Eastern Europe & Russia | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0055 | 0.048339 | 0.007139 | NaN | NaN |
| Portugal | Western Europe | A3 | 0.01128 | 0.055841 | 0.014641 | 0.002 | 0.043796 | 0.002596 | NaN | NaN |
| Qatar | Middle East | Aa2 | 0.004645 | 0.047229 | 0.006029 | 0.0025 | 0.044445 | 0.003245 | NaN | NaN |
| Ras Al Khaimah (Emirate of) | Middle East | A3 | 0.01128 | 0.055841 | 0.014641 | NaN | NaN | NaN | NaN | NaN |
| Romania | Eastern Europe & Russia | Baa3 | 0.020679 | 0.068043 | 0.026843 | 0.0152 | 0.06093 | 0.01973 | NaN | NaN |
| Rwanda | Africa | B2 | 0.051753 | 0.108378 | 0.067178 | NaN | NaN | NaN | NaN | NaN |
| Saudi Arabia | Middle East | A1 | 0.006635 | 0.049813 | 0.008613 | 0.0036 | 0.045873 | 0.004673 | NaN | NaN |
| Senegal | Africa | Ba3 | 0.033839 | 0.085124 | 0.043924 | 0.049 | 0.104804 | 0.063604 | NaN | NaN |
| Serbia | Eastern Europe & Russia | Ba2 | 0.02831 | 0.077947 | 0.036747 | 0.0187 | 0.065473 | 0.024273 | NaN | NaN |
| Sharjah | Middle East | Ba1 | 0.023554 | 0.071775 | 0.030575 | NaN | NaN | NaN | NaN | NaN |
| Singapore | Asia | Aaa | 0 | 0.0412 | 0 | NaN | NaN | NaN | NaN | NaN |
| Slovakia | Eastern Europe & Russia | A2 | 0.007962 | 0.051535 | 0.010335 | 0.0002 | 0.04146 | 0.00026 | NaN | NaN |
| Slovenia | Eastern Europe & Russia | A3 | 0.01128 | 0.055841 | 0.014641 | 0.0015 | 0.043147 | 0.001947 | NaN | NaN |
| Solomon Islands | Asia | Caa1 | 0.070553 | 0.132781 | 0.091581 | NaN | NaN | NaN | NaN | NaN |
| South Africa | Africa | Ba2 | 0.02831 | 0.077947 | 0.036747 | 0.0271 | 0.076377 | 0.035177 | NaN | NaN |
| Spain | Western Europe | Baa1 | 0.015039 | 0.060722 | 0.019522 | 0.0022 | 0.044056 | 0.002856 | NaN | NaN |
| Sri Lanka | Asia | Ca | 0.112906 | 0.187758 | 0.146558 | NaN | NaN | NaN | NaN | NaN |
| St. Maarten | Caribbean | Ba2 | 0.02831 | 0.077947 | 0.036747 | NaN | NaN | NaN | NaN | NaN |
| St. Vincent & the Grenadines | Caribbean | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Suriname | Central and South America | Caa3 | 0.094107 | 0.163355 | 0.122155 | NaN | NaN | NaN | NaN | NaN |
| Swaziland | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Sweden | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Switzerland | Western Europe | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Taiwan | Asia | Aa3 | 0.00564 | 0.048521 | 0.007321 | NaN | NaN | NaN | NaN | NaN |
| Tajikistan | Eastern Europe & Russia | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Tanzania | Africa | B1 | 0.042354 | 0.096177 | 0.054977 | NaN | NaN | NaN | NaN | NaN |
| Thailand | Asia | Baa1 | 0.015039 | 0.060722 | 0.019522 | 0.0023 | 0.044186 | 0.002986 | NaN | NaN |
| Togo | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Trinidad and Tobago | Caribbean | Ba2 | 0.02831 | 0.077947 | 0.036747 | NaN | NaN | NaN | NaN | NaN |
| Tunisia | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | 0.0743 | 0.137645 | 0.096445 | NaN | NaN |
| Turkey | Western Europe | B3 | 0.061153 | 0.120579 | 0.079379 | 0.0331 | 0.084165 | 0.042965 | NaN | NaN |
| Turks and Caicos Islands | Caribbean | Baa1 | 0.015039 | 0.060722 | 0.019522 | NaN | NaN | NaN | NaN | NaN |
| Uganda | Africa | B3 | 0.061153 | 0.120579 | 0.079379 | NaN | NaN | NaN | NaN | NaN |
| Ukraine | Eastern Europe & Russia | Ca | 0.112906 | 0.187758 | 0.146558 | NaN | NaN | NaN | NaN | NaN |
| United Arab Emirates | Middle East | Aa2 | 0.004645 | 0.047229 | 0.006029 | NaN | NaN | NaN | NaN | NaN |
| United Kingdom | Western Europe | Aa3 | 0.00564 | 0.048521 | 0.007321 | 0 | 0.0412 | 0 | NaN | NaN |
| United States | North America | Aaa | 0 | 0.0412 | 0 | 0 | 0.0412 | 0 | NaN | NaN |
| Uruguay | Central and South America | Baa1 | 0.015039 | 0.060722 | 0.019522 | 0.0062 | 0.049248 | 0.008048 | NaN | NaN |
| Uzbekistan | Eastern Europe & Russia | Ba3 | 0.033839 | 0.085124 | 0.043924 | NaN | NaN | NaN | NaN | NaN |
| Venezuela | Central and South America | C | 0.175 | 0.268358 | 0.227158 | 0.0983 | 0.168798 | 0.127598 | NaN | NaN |
| Vietnam | Asia | Ba2 | 0.02831 | 0.077947 | 0.036747 | 0.013 | 0.058075 | 0.016875 | NaN | NaN |
| Zambia | Africa | Caa2 | 0.084707 | 0.151154 | 0.109954 | NaN | NaN | NaN | NaN | NaN |
| Frontier Markets (no sovereign ratings) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Country | PRS Composite Risk Score | ERP | CRP | Default Spread | NaN | NaN | NaN | NaN | NaN | NaN |
| Algeria | 69.25 | 0.077947 | 0.036747 | 0.02831 | NaN | NaN | NaN | NaN | NaN | NaN |
| Brunei | 81.75 | 0.048521 | 0.007321 | 0.00564 | NaN | NaN | NaN | NaN | NaN | NaN |
| Gambia | 66.75 | 0.096177 | 0.054977 | 0.042354 | NaN | NaN | NaN | NaN | NaN | NaN |
| Guinea | 59 | 0.151154 | 0.109954 | 0.084707 | NaN | NaN | NaN | NaN | NaN | NaN |
| Guinea-Bissau | 63 | 0.120579 | 0.079379 | 0.061153 | NaN | NaN | NaN | NaN | NaN | NaN |
| Guyana | 74.5 | 0.060722 | 0.019522 | 0.015039 | NaN | NaN | NaN | NaN | NaN | NaN |
| Haiti | 55 | 0.187758 | 0.146558 | 0.112906 | NaN | NaN | NaN | NaN | NaN | NaN |
| Iran | 63.25 | 0.120579 | 0.079379 | 0.061153 | NaN | NaN | NaN | NaN | NaN | NaN |
| Korea, D.P.R. | 49.25 | 0.268358 | 0.227158 | 0.175 | NaN | NaN | NaN | NaN | NaN | NaN |
| Liberia | 61.5 | 0.132781 | 0.091581 | 0.070553 | NaN | NaN | NaN | NaN | NaN | NaN |
| Libya | 74.75 | 0.060722 | 0.019522 | 0.015039 | NaN | NaN | NaN | NaN | NaN | NaN |
| Madagascar | 63.25 | 0.120579 | 0.079379 | 0.061153 | NaN | NaN | NaN | NaN | NaN | NaN |
| Malawi | 52.25 | 0.187758 | 0.146558 | 0.112906 | NaN | NaN | NaN | NaN | NaN | NaN |
| Myanmar | 58 | 0.151154 | 0.109954 | 0.084707 | NaN | NaN | NaN | NaN | NaN | NaN |
| Russia | 71.25 | 0.077947 | 0.036747 | 0.02831 | NaN | NaN | NaN | NaN | NaN | NaN |
| Sierra Leone | 58 | 0.151154 | 0.109954 | 0.084707 | NaN | NaN | NaN | NaN | NaN | NaN |
| Somalia | 54.25 | 0.187758 | 0.146558 | 0.112906 | NaN | NaN | NaN | NaN | NaN | NaN |
| Sudan | 43.5 | 0.268358 | 0.227158 | 0.175 | NaN | NaN | NaN | NaN | NaN | NaN |
| Syria | 44.25 | 0.268358 | 0.227158 | 0.175 | NaN | NaN | NaN | NaN | NaN | NaN |
| Yemen, Republic | 51.5 | 0.187758 | 0.146558 | 0.112906 | NaN | NaN | NaN | NaN | NaN | NaN |
| Zimbabwe | 58 | 0.151154 | 0.109954 | 0.084707 | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Rating | Default spread in basis points | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | A1 | 66.350422 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | A2 | 79.620506 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | A3 | 112.795717 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Aa1 | 37.598572 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Aa2 | 46.445295 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Aa3 | 56.397858 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Aaa | 0 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | B1 | 423.536857 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | B2 | 517.533288 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | B3 | 611.529718 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Ba1 | 235.543996 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Ba2 | 283.095132 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Ba3 | 338.38715 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Baa1 | 150.394289 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Baa2 | 179.146138 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Baa3 | 206.792147 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | C | 1750 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Ca | 1129.063006 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Caa1 | 705.526149 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Caa2 | 847.073715 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | Caa3 | 941.070145 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NR | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Relative Equity Volatility
| Year | Std Dev (BMI) | Std Dev (JPM Sov Bond) | REL VOL | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Estimation note: Those of you who have followed my attempts to estimate the relative equity market volatility know that I have struggled with getting a proxy for returns on emerging market sovereign bonds, and have used the coefficient of varation in yields to make that estimate. I have finally replaced that estimate with a return on an emerging market governemnt bond ETF from iShares. The standard deviations are now computed consistently for emerigng equities and emerigng government bonds. (Using the old yield coefficient of variation approach would have yielded a ratio of 1.49 in this computation.) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2019-2020 | 0.217772 | 0.19276 | 1.129759 | NaN | NaN | NaN | NaN | NaN | NaN |
| 2020-2021 | 0.143766 | 0.074054 | 1.941371 | NaN | NaN | NaN | NaN | NaN | NaN |
| 2021-2022 | 0.178779 | 0.107213 | 1.667510 | NaN | NaN | NaN | NaN | NaN | NaN |
| 2022-2023 | 0.135737 | 0.140694 | 0.964766 | NaN | NaN | NaN | NaN | NaN | NaN |
| 2023-2024 | 0.111958 | 0.092354 | 1.212265 | NaN | NaN | NaN | NaN | NaN | NaN |
| Average Relative Volatility | 0.157603 | 0.121415 | 1.298047 | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Index: | iShares JP Morgan USD Emerging Markets Bond ETF | NaN | NaN | NaN | NaN | Index: | S&P Emerging BMI Index | NaN | NaN |
| Source: | Yahoo! | NaN | NaN | NaN | NaN | Source: | S&P | NaN | NaN |
| NaN | https://finance.yahoo.com/quote/EMB/ | NaN | NaN | NaN | NaN | NaN | https://www.spglobal.com/spdji/en/indices/equity/sp-emerging-bmi/#overview | NaN | NaN |
| Period | Five years | (July 1, 2019 - June 30, 2024) | NaN | NaN | NaN | Period | Five years | (July 1, 2019 - June 30, 2024) | NaN |
| Interval | Daily | NaN | NaN | NaN | NaN | Interval | Daily | NaN | NaN |
| Date | Adj Close | Return | NaN | NaN | NaN | Effective date | S&P Emerging BMI (USD) | Return | NaN |
| 2019-07-01 00:00:00 | 91.064468 | NaN | NaN | NaN | NaN | 2019-07-01 00:00:00 | 281.63 | NaN | NaN |
| 2019-07-02 00:00:00 | 91.224991 | 0.001763 | NaN | NaN | NaN | 2019-07-02 00:00:00 | 281.95 | 0.001136 | NaN |
| 2019-07-03 00:00:00 | 91.473907 | 0.002729 | NaN | NaN | NaN | 2019-07-03 00:00:00 | 281.64 | -0.001099 | NaN |
| 2019-07-05 00:00:00 | 91.000237 | -0.005178 | NaN | NaN | NaN | 2019-07-04 00:00:00 | 282.85 | 0.004296 | NaN |
| 2019-07-08 00:00:00 | 90.871796 | -0.001411 | NaN | NaN | NaN | 2019-07-05 00:00:00 | 281.57 | -0.004525 | NaN |
| 2019-07-09 00:00:00 | 90.655029 | -0.002385 | NaN | NaN | NaN | 2019-07-08 00:00:00 | 278.7 | -0.010193 | NaN |
| 2019-07-10 00:00:00 | 90.799522 | 0.001594 | NaN | NaN | NaN | 2019-07-09 00:00:00 | 277.64 | -0.003803 | NaN |
| 2019-07-11 00:00:00 | 90.534569 | -0.002918 | NaN | NaN | NaN | 2019-07-10 00:00:00 | 279.33 | 0.006087 | NaN |
| 2019-07-12 00:00:00 | 90.719254 | 0.00204 | NaN | NaN | NaN | 2019-07-11 00:00:00 | 280.61 | 0.004582 | NaN |
| 2019-07-15 00:00:00 | 90.903908 | 0.002035 | NaN | NaN | NaN | 2019-07-12 00:00:00 | 279.48 | -0.004027 | NaN |
| 2019-07-16 00:00:00 | 90.855698 | -0.00053 | NaN | NaN | NaN | 2019-07-15 00:00:00 | 281.27 | 0.006405 | NaN |
| 2019-07-17 00:00:00 | 90.960106 | 0.001149 | NaN | NaN | NaN | 2019-07-16 00:00:00 | 281.73 | 0.001635 | NaN |
| 2019-07-18 00:00:00 | 91.12867 | 0.001853 | NaN | NaN | NaN | 2019-07-17 00:00:00 | 280.62 | -0.00394 | NaN |
| 2019-07-19 00:00:00 | 90.992249 | -0.001497 | NaN | NaN | NaN | 2019-07-18 00:00:00 | 279.81 | -0.002886 | NaN |
| 2019-07-22 00:00:00 | 91.313332 | 0.003529 | NaN | NaN | NaN | 2019-07-19 00:00:00 | 280.6 | 0.002823 | NaN |
| 2019-07-23 00:00:00 | 91.594337 | 0.003077 | NaN | NaN | NaN | 2019-07-22 00:00:00 | 279.47 | -0.004027 | NaN |
| 2019-07-24 00:00:00 | 91.803047 | 0.002279 | NaN | NaN | NaN | 2019-07-23 00:00:00 | 279.62 | 0.000537 | NaN |
| 2019-07-25 00:00:00 | 91.66658 | -0.001487 | NaN | NaN | NaN | 2019-07-24 00:00:00 | 279.79 | 0.000608 | NaN |
| 2019-07-26 00:00:00 | 91.618446 | -0.000525 | NaN | NaN | NaN | 2019-07-25 00:00:00 | 279.55 | -0.000858 | NaN |
| 2019-07-29 00:00:00 | 91.610382 | -0.000088 | NaN | NaN | NaN | 2019-07-26 00:00:00 | 278.28 | -0.004543 | NaN |
| 2019-07-30 00:00:00 | 91.457832 | -0.001665 | NaN | NaN | NaN | 2019-07-29 00:00:00 | 277.91 | -0.00133 | NaN |
| 2019-07-31 00:00:00 | 91.265144 | -0.002107 | NaN | NaN | NaN | 2019-07-30 00:00:00 | 276.75 | -0.004174 | NaN |
| 2019-08-01 00:00:00 | 91.658409 | 0.004309 | NaN | NaN | NaN | 2019-07-31 00:00:00 | 275.61 | -0.004119 | NaN |
| 2019-08-02 00:00:00 | 91.601974 | -0.000616 | NaN | NaN | NaN | 2019-08-01 00:00:00 | 272.25 | -0.012191 | NaN |
| 2019-08-05 00:00:00 | 90.699501 | -0.009852 | NaN | NaN | NaN | 2019-08-02 00:00:00 | 266.96 | -0.019431 | NaN |
| 2019-08-06 00:00:00 | 91.336082 | 0.007019 | NaN | NaN | NaN | 2019-08-05 00:00:00 | 259.26 | -0.028843 | NaN |
| 2019-08-07 00:00:00 | 91.795364 | 0.005028 | NaN | NaN | NaN | 2019-08-06 00:00:00 | 259.7 | 0.001697 | NaN |
| 2019-08-08 00:00:00 | 92.254684 | 0.005004 | NaN | NaN | NaN | 2019-08-07 00:00:00 | 259.92 | 0.000847 | NaN |
| 2019-08-09 00:00:00 | 92.206337 | -0.000524 | NaN | NaN | NaN | 2019-08-08 00:00:00 | 263.26 | 0.01285 | NaN |
| 2019-08-12 00:00:00 | 91.239403 | -0.010487 | NaN | NaN | NaN | 2019-08-09 00:00:00 | 262.2 | -0.004026 | NaN |
| 2019-08-13 00:00:00 | 91.110435 | -0.001414 | NaN | NaN | NaN | 2019-08-12 00:00:00 | 260.67 | -0.005835 | NaN |
| 2019-08-14 00:00:00 | 90.989609 | -0.001326 | NaN | NaN | NaN | 2019-08-13 00:00:00 | 259.14 | -0.005869 | NaN |
| 2019-08-15 00:00:00 | 91.352196 | 0.003985 | NaN | NaN | NaN | 2019-08-14 00:00:00 | 257.42 | -0.006637 | NaN |
| 2019-08-16 00:00:00 | 91.875961 | 0.005733 | NaN | NaN | NaN | 2019-08-15 00:00:00 | 256.93 | -0.001904 | NaN |
| 2019-08-19 00:00:00 | 91.505287 | -0.004035 | NaN | NaN | NaN | 2019-08-16 00:00:00 | 258.93 | 0.007784 | NaN |
| 2019-08-20 00:00:00 | 91.529495 | 0.000265 | NaN | NaN | NaN | 2019-08-19 00:00:00 | 260.91 | 0.007647 | NaN |
| 2019-08-21 00:00:00 | 91.795364 | 0.002905 | NaN | NaN | NaN | 2019-08-20 00:00:00 | 260.98 | 0.000268 | NaN |
| 2019-08-22 00:00:00 | 91.843719 | 0.000527 | NaN | NaN | NaN | 2019-08-21 00:00:00 | 261.77 | 0.003027 | NaN |
| 2019-08-23 00:00:00 | 91.884003 | 0.000439 | NaN | NaN | NaN | 2019-08-22 00:00:00 | 259.97 | -0.006876 | NaN |
| 2019-08-26 00:00:00 | 91.803467 | -0.000876 | NaN | NaN | NaN | 2019-08-23 00:00:00 | 259.38 | -0.002269 | NaN |
| 2019-08-27 00:00:00 | 92.061279 | 0.002808 | NaN | NaN | NaN | 2019-08-26 00:00:00 | 256.7 | -0.010332 | NaN |
| 2019-08-28 00:00:00 | 92.166046 | 0.001138 | NaN | NaN | NaN | 2019-08-27 00:00:00 | 257.5 | 0.003116 | NaN |
| 2019-08-29 00:00:00 | 92.37558 | 0.002273 | NaN | NaN | NaN | 2019-08-28 00:00:00 | 257.56 | 0.000233 | NaN |
| 2019-08-30 00:00:00 | 92.68174 | 0.003314 | NaN | NaN | NaN | 2019-08-29 00:00:00 | 259.07 | 0.005863 | NaN |
| 2019-09-03 00:00:00 | 92.89444 | 0.002295 | NaN | NaN | NaN | 2019-08-30 00:00:00 | 262.46 | 0.013085 | NaN |
| 2019-09-04 00:00:00 | 93.4767 | 0.006268 | NaN | NaN | NaN | 2019-09-02 00:00:00 | 262.46 | 0 | NaN |
| 2019-09-05 00:00:00 | 92.975304 | -0.005364 | NaN | NaN | NaN | 2019-09-03 00:00:00 | 259.61 | -0.010859 | NaN |
| 2019-09-06 00:00:00 | 93.306839 | 0.003566 | NaN | NaN | NaN | 2019-09-04 00:00:00 | 263.96 | 0.016756 | NaN |
| 2019-09-09 00:00:00 | 92.538612 | -0.008233 | NaN | NaN | NaN | 2019-09-05 00:00:00 | 266.69 | 0.010342 | NaN |
| 2019-09-10 00:00:00 | 91.851227 | -0.007428 | NaN | NaN | NaN | 2019-09-06 00:00:00 | 267.9 | 0.004537 | NaN |
| 2019-09-11 00:00:00 | 91.948265 | 0.001056 | NaN | NaN | NaN | 2019-09-09 00:00:00 | 268.11 | 0.000784 | NaN |
| 2019-09-12 00:00:00 | 92.126167 | 0.001935 | NaN | NaN | NaN | 2019-09-10 00:00:00 | 267.36 | -0.002797 | NaN |
| 2019-09-13 00:00:00 | 91.066811 | -0.011499 | NaN | NaN | NaN | 2019-09-11 00:00:00 | 269.79 | 0.009089 | NaN |
| 2019-09-16 00:00:00 | 91.454948 | 0.004262 | NaN | NaN | NaN | 2019-09-12 00:00:00 | 271.57 | 0.006598 | NaN |
| 2019-09-17 00:00:00 | 91.746094 | 0.003183 | NaN | NaN | NaN | 2019-09-13 00:00:00 | 272.89 | 0.004861 | NaN |
| 2019-09-18 00:00:00 | 91.754181 | 0.000088 | NaN | NaN | NaN | 2019-09-16 00:00:00 | 272.42 | -0.001722 | NaN |
| 2019-09-19 00:00:00 | 92.158531 | 0.004407 | NaN | NaN | NaN | 2019-09-17 00:00:00 | 270.17 | -0.008259 | NaN |
| 2019-09-20 00:00:00 | 92.570969 | 0.004475 | NaN | NaN | NaN | 2019-09-18 00:00:00 | 270.78 | 0.002258 | NaN |
| 2019-09-23 00:00:00 | 92.360695 | -0.002271 | NaN | NaN | NaN | 2019-09-19 00:00:00 | 269.13 | -0.006094 | NaN |
| 2019-09-24 00:00:00 | 91.770348 | -0.006392 | NaN | NaN | NaN | 2019-09-20 00:00:00 | 270.74 | 0.005982 | NaN |
| 2019-09-25 00:00:00 | 91.503494 | -0.002908 | NaN | NaN | NaN | 2019-09-23 00:00:00 | 269.63 | -0.0041 | NaN |
| 2019-09-26 00:00:00 | 91.689499 | 0.002033 | NaN | NaN | NaN | 2019-09-24 00:00:00 | 268.47 | -0.004302 | NaN |
| 2019-09-27 00:00:00 | 91.568161 | -0.001323 | NaN | NaN | NaN | 2019-09-25 00:00:00 | 267.12 | -0.005028 | NaN |
| 2019-09-30 00:00:00 | 91.66523 | 0.00106 | NaN | NaN | NaN | 2019-09-26 00:00:00 | 267.94 | 0.00307 | NaN |
| 2019-10-01 00:00:00 | 91.227005 | -0.004781 | NaN | NaN | NaN | 2019-09-27 00:00:00 | 266.29 | -0.006158 | NaN |
| 2019-10-02 00:00:00 | 91.210732 | -0.000178 | NaN | NaN | NaN | 2019-09-30 00:00:00 | 265.49 | -0.003004 | NaN |
| 2019-10-03 00:00:00 | 91.648987 | 0.004805 | NaN | NaN | NaN | 2019-10-01 00:00:00 | 264.6 | -0.003352 | NaN |
| 2019-10-04 00:00:00 | 92.452423 | 0.008766 | NaN | NaN | NaN | 2019-10-02 00:00:00 | 263.05 | -0.005858 | NaN |
| 2019-10-07 00:00:00 | 91.933029 | -0.005618 | NaN | NaN | NaN | 2019-10-03 00:00:00 | 263.95 | 0.003421 | NaN |
| 2019-10-08 00:00:00 | 91.843735 | -0.000971 | NaN | NaN | NaN | 2019-10-04 00:00:00 | 264.87 | 0.003486 | NaN |
| 2019-10-09 00:00:00 | 91.851906 | 0.000089 | NaN | NaN | NaN | 2019-10-07 00:00:00 | 264.13 | -0.002794 | NaN |
| 2019-10-10 00:00:00 | 91.697693 | -0.001679 | NaN | NaN | NaN | 2019-10-08 00:00:00 | 263.49 | -0.002423 | NaN |
| 2019-10-11 00:00:00 | 91.632759 | -0.000708 | NaN | NaN | NaN | 2019-10-09 00:00:00 | 263.48 | -0.000038 | NaN |
| 2019-10-14 00:00:00 | 91.673355 | 0.000443 | NaN | NaN | NaN | 2019-10-10 00:00:00 | 264.78 | 0.004934 | NaN |
| 2019-10-15 00:00:00 | 91.868118 | 0.002125 | NaN | NaN | NaN | 2019-10-11 00:00:00 | 268.27 | 0.013181 | NaN |
| 2019-10-16 00:00:00 | 91.722054 | -0.00159 | NaN | NaN | NaN | 2019-10-14 00:00:00 | 269.52 | 0.004659 | NaN |
| 2019-10-17 00:00:00 | 91.851906 | 0.001416 | NaN | NaN | NaN | 2019-10-15 00:00:00 | 269.86 | 0.001262 | NaN |
| 2019-10-18 00:00:00 | 91.933029 | 0.000883 | NaN | NaN | NaN | 2019-10-16 00:00:00 | 270.82 | 0.003557 | NaN |
| 2019-10-21 00:00:00 | 91.600288 | -0.003619 | NaN | NaN | NaN | 2019-10-17 00:00:00 | 272.41 | 0.005871 | NaN |
| 2019-10-22 00:00:00 | 91.933029 | 0.003633 | NaN | NaN | NaN | 2019-10-18 00:00:00 | 271.68 | -0.00268 | NaN |
| 2019-10-23 00:00:00 | 92.095337 | 0.001766 | NaN | NaN | NaN | 2019-10-21 00:00:00 | 272.54 | 0.003165 | NaN |
| 2019-10-24 00:00:00 | 92.095337 | 0 | NaN | NaN | NaN | 2019-10-22 00:00:00 | 273.53 | 0.003632 | NaN |
| 2019-10-25 00:00:00 | 92.070992 | -0.000264 | NaN | NaN | NaN | 2019-10-23 00:00:00 | 272.89 | -0.00234 | NaN |
| 2019-10-28 00:00:00 | 91.924934 | -0.001586 | NaN | NaN | NaN | 2019-10-24 00:00:00 | 274.54 | 0.006046 | NaN |
| 2019-10-29 00:00:00 | 91.681488 | -0.002648 | NaN | NaN | NaN | 2019-10-25 00:00:00 | 274.25 | -0.001056 | NaN |
| 2019-10-30 00:00:00 | 91.778831 | 0.001062 | NaN | NaN | NaN | 2019-10-28 00:00:00 | 276.13 | 0.006855 | NaN |
| 2019-10-31 00:00:00 | 92.192726 | 0.00451 | NaN | NaN | NaN | 2019-10-29 00:00:00 | 276.03 | -0.000362 | NaN |
| 2019-11-01 00:00:00 | 92.522591 | 0.003578 | NaN | NaN | NaN | 2019-10-30 00:00:00 | 275.8 | -0.000833 | NaN |
| 2019-11-04 00:00:00 | 92.32711 | -0.002113 | NaN | NaN | NaN | 2019-10-31 00:00:00 | 275.7 | -0.000363 | NaN |
| 2019-11-05 00:00:00 | 91.659286 | -0.007233 | NaN | NaN | NaN | 2019-11-01 00:00:00 | 277.63 | 0.007 | NaN |
| 2019-11-06 00:00:00 | 91.699982 | 0.000444 | NaN | NaN | NaN | 2019-11-04 00:00:00 | 280.93 | 0.011886 | NaN |
| 2019-11-07 00:00:00 | 91.382355 | -0.003464 | NaN | NaN | NaN | 2019-11-05 00:00:00 | 282.23 | 0.004627 | NaN |
| 2019-11-08 00:00:00 | 91.512634 | 0.001426 | NaN | NaN | NaN | 2019-11-06 00:00:00 | 281.51 | -0.002551 | NaN |
| 2019-11-11 00:00:00 | 91.439354 | -0.000801 | NaN | NaN | NaN | 2019-11-07 00:00:00 | 282.97 | 0.005186 | NaN |
| 2019-11-12 00:00:00 | 91.252052 | -0.002048 | NaN | NaN | NaN | 2019-11-08 00:00:00 | 280.78 | -0.007739 | NaN |
| 2019-11-13 00:00:00 | 91.113579 | -0.001517 | NaN | NaN | NaN | 2019-11-11 00:00:00 | 277.89 | -0.010293 | NaN |
| 2019-11-14 00:00:00 | 91.594116 | 0.005274 | NaN | NaN | NaN | 2019-11-12 00:00:00 | 278.21 | 0.001152 | NaN |
| 2019-11-15 00:00:00 | 91.667412 | 0.0008 | NaN | NaN | NaN | 2019-11-13 00:00:00 | 275.4 | -0.0101 | NaN |
| 2019-11-18 00:00:00 | 91.235748 | -0.004709 | NaN | NaN | NaN | 2019-11-14 00:00:00 | 274.89 | -0.001852 | NaN |
| 2019-11-19 00:00:00 | 91.032135 | -0.002232 | NaN | NaN | NaN | 2019-11-15 00:00:00 | 276.23 | 0.004875 | NaN |
| 2019-11-20 00:00:00 | 91.186867 | 0.0017 | NaN | NaN | NaN | 2019-11-18 00:00:00 | 277.09 | 0.003113 | NaN |
| 2019-11-21 00:00:00 | 91.195038 | 0.00009 | NaN | NaN | NaN | 2019-11-19 00:00:00 | 278.66 | 0.005666 | NaN |
| 2019-11-22 00:00:00 | 91.439354 | 0.002679 | NaN | NaN | NaN | 2019-11-20 00:00:00 | 277.68 | -0.003517 | NaN |
| 2019-11-25 00:00:00 | 91.431236 | -0.000089 | NaN | NaN | NaN | 2019-11-21 00:00:00 | 276.3 | -0.00497 | NaN |
| 2019-11-26 00:00:00 | 91.675545 | 0.002672 | NaN | NaN | NaN | 2019-11-22 00:00:00 | 277.19 | 0.003221 | NaN |
| 2019-11-27 00:00:00 | 91.54525 | -0.001421 | NaN | NaN | NaN | 2019-11-25 00:00:00 | 278.32 | 0.004077 | NaN |
| 2019-11-29 00:00:00 | 91.317169 | -0.002491 | NaN | NaN | NaN | 2019-11-26 00:00:00 | 277.04 | -0.004599 | NaN |
| 2019-12-02 00:00:00 | 90.947708 | -0.004046 | NaN | NaN | NaN | 2019-11-27 00:00:00 | 278.33 | 0.004656 | NaN |
| 2019-12-03 00:00:00 | 91.127556 | 0.001977 | NaN | NaN | NaN | 2019-11-28 00:00:00 | 277.95 | -0.001365 | NaN |
| 2019-12-04 00:00:00 | 91.34008 | 0.002332 | NaN | NaN | NaN | 2019-11-29 00:00:00 | 275.92 | -0.007303 | NaN |
| 2019-12-05 00:00:00 | 91.609833 | 0.002953 | NaN | NaN | NaN | 2019-12-02 00:00:00 | 275.92 | 0 | NaN |
| 2019-12-06 00:00:00 | 91.797836 | 0.002052 | NaN | NaN | NaN | 2019-12-03 00:00:00 | 275.33 | -0.002138 | NaN |
| 2019-12-09 00:00:00 | 92.043045 | 0.002671 | NaN | NaN | NaN | 2019-12-04 00:00:00 | 275.61 | 0.001017 | NaN |
| 2019-12-10 00:00:00 | 92.043045 | 0 | NaN | NaN | NaN | 2019-12-05 00:00:00 | 277.2 | 0.005769 | NaN |
| 2019-12-11 00:00:00 | 92.656143 | 0.006661 | NaN | NaN | NaN | 2019-12-06 00:00:00 | 278.57 | 0.004942 | NaN |
| 2019-12-12 00:00:00 | 92.664322 | 0.000088 | NaN | NaN | NaN | 2019-12-09 00:00:00 | 278.99 | 0.001508 | NaN |
| 2019-12-13 00:00:00 | 93.007652 | 0.003705 | NaN | NaN | NaN | 2019-12-10 00:00:00 | 278.4 | -0.002115 | NaN |
| 2019-12-16 00:00:00 | 93.064857 | 0.000615 | NaN | NaN | NaN | 2019-12-11 00:00:00 | 280.7 | 0.008261 | NaN |
| 2019-12-17 00:00:00 | 93.408195 | 0.003689 | NaN | NaN | NaN | 2019-12-12 00:00:00 | 283.26 | 0.00912 | NaN |
| 2019-12-18 00:00:00 | 93.588036 | 0.001925 | NaN | NaN | NaN | 2019-12-13 00:00:00 | 286.54 | 0.011579 | NaN |
| 2019-12-19 00:00:00 | 93.268814 | -0.003411 | NaN | NaN | NaN | 2019-12-16 00:00:00 | 287.16 | 0.002164 | NaN |
| 2019-12-20 00:00:00 | 93.498596 | 0.002464 | NaN | NaN | NaN | 2019-12-17 00:00:00 | 290.24 | 0.010726 | NaN |
| 2019-12-23 00:00:00 | 93.60527 | 0.001141 | NaN | NaN | NaN | 2019-12-18 00:00:00 | 292.02 | 0.006133 | NaN |
| 2019-12-24 00:00:00 | 93.769386 | 0.001753 | NaN | NaN | NaN | 2019-12-19 00:00:00 | 291.46 | -0.001918 | NaN |
| 2019-12-26 00:00:00 | 93.900688 | 0.0014 | NaN | NaN | NaN | 2019-12-20 00:00:00 | 291.4 | -0.000206 | NaN |
| 2019-12-27 00:00:00 | 94.155083 | 0.002709 | NaN | NaN | NaN | 2019-12-23 00:00:00 | 292.49 | 0.003741 | NaN |
| 2019-12-30 00:00:00 | 93.99913 | -0.001656 | NaN | NaN | NaN | 2019-12-24 00:00:00 | 292.07 | -0.001436 | NaN |
| 2019-12-31 00:00:00 | 94.007385 | 0.000088 | NaN | NaN | NaN | 2019-12-25 00:00:00 | 292.12 | 0.000171 | NaN |
| 2020-01-02 00:00:00 | 94.122223 | 0.001222 | NaN | NaN | NaN | 2019-12-26 00:00:00 | 292.59 | 0.001609 | NaN |
| 2020-01-03 00:00:00 | 93.88427 | -0.002528 | NaN | NaN | NaN | 2019-12-27 00:00:00 | 294.52 | 0.006596 | NaN |
| 2020-01-06 00:00:00 | 93.695526 | -0.00201 | NaN | NaN | NaN | 2019-12-30 00:00:00 | 294.86 | 0.001154 | NaN |
| 2020-01-07 00:00:00 | 93.843231 | 0.001576 | NaN | NaN | NaN | 2019-12-31 00:00:00 | 294.06 | -0.002713 | NaN |
| 2020-01-08 00:00:00 | 94.089417 | 0.002623 | NaN | NaN | NaN | 2020-01-01 00:00:00 | 294.1 | 0.000136 | NaN |
| 2020-01-09 00:00:00 | 94.023766 | -0.000698 | NaN | NaN | NaN | 2020-01-02 00:00:00 | 298.23 | 0.014043 | NaN |
| 2020-01-10 00:00:00 | 94.040207 | 0.000175 | NaN | NaN | NaN | 2020-01-03 00:00:00 | 297.17 | -0.003554 | NaN |
| 2020-01-13 00:00:00 | 94.130432 | 0.000959 | NaN | NaN | NaN | 2020-01-06 00:00:00 | 294.22 | -0.009927 | NaN |
| 2020-01-14 00:00:00 | 94.10582 | -0.000261 | NaN | NaN | NaN | 2020-01-07 00:00:00 | 294.75 | 0.001801 | NaN |
| 2020-01-15 00:00:00 | 94.458672 | 0.00375 | NaN | NaN | NaN | 2020-01-08 00:00:00 | 293.61 | -0.003868 | NaN |
| 2020-01-16 00:00:00 | 94.65564 | 0.002085 | NaN | NaN | NaN | 2020-01-09 00:00:00 | 297.82 | 0.014339 | NaN |
| 2020-01-17 00:00:00 | 94.540764 | -0.001214 | NaN | NaN | NaN | 2020-01-10 00:00:00 | 298.82 | 0.003358 | NaN |
| 2020-01-21 00:00:00 | 94.458672 | -0.000868 | NaN | NaN | NaN | 2020-01-13 00:00:00 | 301.32 | 0.008366 | NaN |
| 2020-01-22 00:00:00 | 94.532524 | 0.000782 | NaN | NaN | NaN | 2020-01-14 00:00:00 | 301.23 | -0.000299 | NaN |
| 2020-01-23 00:00:00 | 94.310959 | -0.002344 | NaN | NaN | NaN | 2020-01-15 00:00:00 | 300.07 | -0.003851 | NaN |
| 2020-01-24 00:00:00 | 94.187889 | -0.001305 | NaN | NaN | NaN | 2020-01-16 00:00:00 | 300.6 | 0.001766 | NaN |
| 2020-01-27 00:00:00 | 94.072998 | -0.00122 | NaN | NaN | NaN | 2020-01-17 00:00:00 | 302.11 | 0.005023 | NaN |
| 2020-01-28 00:00:00 | 94.516121 | 0.00471 | NaN | NaN | NaN | 2020-01-20 00:00:00 | 301.43 | -0.002251 | NaN |
| 2020-01-29 00:00:00 | 94.951035 | 0.004601 | NaN | NaN | NaN | 2020-01-21 00:00:00 | 296.95 | -0.014862 | NaN |
| 2020-01-30 00:00:00 | 94.885399 | -0.000691 | NaN | NaN | NaN | 2020-01-22 00:00:00 | 298.18 | 0.004142 | NaN |
| 2020-01-31 00:00:00 | 95.172615 | 0.003027 | NaN | NaN | NaN | 2020-01-23 00:00:00 | 295.55 | -0.00882 | NaN |
| 2020-02-03 00:00:00 | 95.148735 | -0.000251 | NaN | NaN | NaN | 2020-01-24 00:00:00 | 294.84 | -0.002402 | NaN |
| 2020-02-04 00:00:00 | 95.033417 | -0.001212 | NaN | NaN | NaN | 2020-01-27 00:00:00 | 290.14 | -0.015941 | NaN |
| 2020-02-05 00:00:00 | 95.066376 | 0.000347 | NaN | NaN | NaN | 2020-01-28 00:00:00 | 291.15 | 0.003481 | NaN |
| 2020-02-06 00:00:00 | 95.296951 | 0.002425 | NaN | NaN | NaN | 2020-01-29 00:00:00 | 289.81 | -0.004602 | NaN |
| 2020-02-07 00:00:00 | 95.296951 | 0 | NaN | NaN | NaN | 2020-01-30 00:00:00 | 283.4 | -0.022118 | NaN |
| 2020-02-10 00:00:00 | 95.313408 | 0.000173 | NaN | NaN | NaN | 2020-01-31 00:00:00 | 281.29 | -0.007445 | NaN |
| 2020-02-11 00:00:00 | 95.27224 | -0.000432 | NaN | NaN | NaN | 2020-02-03 00:00:00 | 279.9 | -0.004942 | NaN |
| 2020-02-12 00:00:00 | 95.412262 | 0.00147 | NaN | NaN | NaN | 2020-02-04 00:00:00 | 285.89 | 0.021401 | NaN |
| 2020-02-13 00:00:00 | 95.436966 | 0.000259 | NaN | NaN | NaN | 2020-02-05 00:00:00 | 287.12 | 0.004302 | NaN |
| 2020-02-14 00:00:00 | 95.81575 | 0.003969 | NaN | NaN | NaN | 2020-02-06 00:00:00 | 289.37 | 0.007836 | NaN |
| 2020-02-18 00:00:00 | 95.898117 | 0.00086 | NaN | NaN | NaN | 2020-02-07 00:00:00 | 286.84 | -0.008743 | NaN |
| 2020-02-19 00:00:00 | 96.087502 | 0.001975 | NaN | NaN | NaN | 2020-02-10 00:00:00 | 285.51 | -0.004637 | NaN |
| 2020-02-20 00:00:00 | 96.145164 | 0.0006 | NaN | NaN | NaN | 2020-02-11 00:00:00 | 288.64 | 0.010963 | NaN |
| 2020-02-21 00:00:00 | 96.359283 | 0.002227 | NaN | NaN | NaN | 2020-02-12 00:00:00 | 291.18 | 0.0088 | NaN |
| 2020-02-24 00:00:00 | 95.939285 | -0.004359 | NaN | NaN | NaN | 2020-02-13 00:00:00 | 290.33 | -0.002919 | NaN |
| 2020-02-25 00:00:00 | 95.346359 | -0.00618 | NaN | NaN | NaN | 2020-02-14 00:00:00 | 290.05 | -0.000964 | NaN |
| 2020-02-26 00:00:00 | 95.296951 | -0.000518 | NaN | NaN | NaN | 2020-02-17 00:00:00 | 290.75 | 0.002413 | NaN |
| 2020-02-27 00:00:00 | 94.111076 | -0.012444 | NaN | NaN | NaN | 2020-02-18 00:00:00 | 288.17 | -0.008874 | NaN |
| 2020-02-28 00:00:00 | 93.979332 | -0.0014 | NaN | NaN | NaN | 2020-02-19 00:00:00 | 290.33 | 0.007496 | NaN |
| 2020-03-02 00:00:00 | 94.737251 | 0.008065 | NaN | NaN | NaN | 2020-02-20 00:00:00 | 288.73 | -0.005511 | NaN |
| 2020-03-03 00:00:00 | 95.836555 | 0.011604 | NaN | NaN | NaN | 2020-02-21 00:00:00 | 286.59 | -0.007412 | NaN |
| 2020-03-04 00:00:00 | 96.547386 | 0.007417 | NaN | NaN | NaN | 2020-02-24 00:00:00 | 280.14 | -0.022506 | NaN |
| 2020-03-05 00:00:00 | 95.696053 | -0.008818 | NaN | NaN | NaN | 2020-02-25 00:00:00 | 279.68 | -0.001642 | NaN |
| 2020-03-06 00:00:00 | 95.299316 | -0.004146 | NaN | NaN | NaN | 2020-02-26 00:00:00 | 276.6 | -0.011013 | NaN |
| 2020-03-09 00:00:00 | 87.579483 | -0.081006 | NaN | NaN | NaN | 2020-02-27 00:00:00 | 273.07 | -0.012762 | NaN |
| 2020-03-10 00:00:00 | 88.596123 | 0.011608 | NaN | NaN | NaN | 2020-02-28 00:00:00 | 266.59 | -0.02373 | NaN |
| 2020-03-11 00:00:00 | 84.587395 | -0.045247 | NaN | NaN | NaN | 2020-03-02 00:00:00 | 268.94 | 0.008815 | NaN |
| 2020-03-12 00:00:00 | 80.421707 | -0.049247 | NaN | NaN | NaN | 2020-03-03 00:00:00 | 272.01 | 0.011415 | NaN |
| 2020-03-13 00:00:00 | 82.702911 | 0.028366 | NaN | NaN | NaN | 2020-03-04 00:00:00 | 273.49 | 0.005441 | NaN |
| 2020-03-16 00:00:00 | 78.884346 | -0.046172 | NaN | NaN | NaN | 2020-03-05 00:00:00 | 273.31 | -0.000658 | NaN |
| 2020-03-17 00:00:00 | 78.115692 | -0.009744 | NaN | NaN | NaN | 2020-03-06 00:00:00 | 266.81 | -0.023783 | NaN |
| 2020-03-18 00:00:00 | 70.916565 | -0.09216 | NaN | NaN | NaN | 2020-03-09 00:00:00 | 249.58 | -0.064578 | NaN |
| 2020-03-19 00:00:00 | 72.71843 | 0.025408 | NaN | NaN | NaN | 2020-03-10 00:00:00 | 253.81 | 0.016948 | NaN |
| 2020-03-20 00:00:00 | 75.28891 | 0.035348 | NaN | NaN | NaN | 2020-03-11 00:00:00 | 249.68 | -0.016272 | NaN |
| 2020-03-23 00:00:00 | 75.503838 | 0.002855 | NaN | NaN | NaN | 2020-03-12 00:00:00 | 232.06 | -0.07057 | NaN |
| 2020-03-24 00:00:00 | 77.859444 | 0.031198 | NaN | NaN | NaN | 2020-03-13 00:00:00 | 234.96 | 0.012497 | NaN |
| 2020-03-25 00:00:00 | 80.983749 | 0.040128 | NaN | NaN | NaN | 2020-03-16 00:00:00 | 218.98 | -0.068012 | NaN |
| 2020-03-26 00:00:00 | 82.322716 | 0.016534 | NaN | NaN | NaN | 2020-03-17 00:00:00 | 217.76 | -0.005571 | NaN |
| 2020-03-27 00:00:00 | 80.628342 | -0.020582 | NaN | NaN | NaN | 2020-03-18 00:00:00 | 207.3 | -0.048035 | NaN |
| 2020-03-30 00:00:00 | 80.520882 | -0.001333 | NaN | NaN | NaN | 2020-03-19 00:00:00 | 203.35 | -0.019055 | NaN |
| 2020-03-31 00:00:00 | 79.909241 | -0.007596 | NaN | NaN | NaN | 2020-03-20 00:00:00 | 211.43 | 0.039734 | NaN |
| 2020-04-01 00:00:00 | 77.899689 | -0.025148 | NaN | NaN | NaN | 2020-03-23 00:00:00 | 199.71 | -0.055432 | NaN |
| 2020-04-02 00:00:00 | 79.49337 | 0.020458 | NaN | NaN | NaN | 2020-03-24 00:00:00 | 209.4 | 0.04852 | NaN |
| 2020-04-03 00:00:00 | 79.35228 | -0.001775 | NaN | NaN | NaN | 2020-03-25 00:00:00 | 217.72 | 0.039733 | NaN |
| 2020-04-06 00:00:00 | 80.954254 | 0.020188 | NaN | NaN | NaN | 2020-03-26 00:00:00 | 222.85 | 0.023562 | NaN |
| 2020-04-07 00:00:00 | 81.41909 | 0.005742 | NaN | NaN | NaN | 2020-03-27 00:00:00 | 219.58 | -0.014674 | NaN |
| 2020-04-08 00:00:00 | 81.767715 | 0.004282 | NaN | NaN | NaN | 2020-03-30 00:00:00 | 216.78 | -0.012752 | NaN |
| 2020-04-09 00:00:00 | 84.125031 | 0.028829 | NaN | NaN | NaN | 2020-03-31 00:00:00 | 220.78 | 0.018452 | NaN |
| 2020-04-13 00:00:00 | 83.959053 | -0.001973 | NaN | NaN | NaN | 2020-04-01 00:00:00 | 216.35 | -0.020065 | NaN |
| 2020-04-14 00:00:00 | 84.515144 | 0.006623 | NaN | NaN | NaN | 2020-04-02 00:00:00 | 218.73 | 0.011001 | NaN |
| 2020-04-15 00:00:00 | 82.83847 | -0.019839 | NaN | NaN | NaN | 2020-04-03 00:00:00 | 216.77 | -0.008961 | NaN |
| 2020-04-16 00:00:00 | 82.298958 | -0.006513 | NaN | NaN | NaN | 2020-04-06 00:00:00 | 221.78 | 0.023112 | NaN |
| 2020-04-17 00:00:00 | 82.87999 | 0.00706 | NaN | NaN | NaN | 2020-04-07 00:00:00 | 228.48 | 0.03021 | NaN |
| 2020-04-20 00:00:00 | 82.357056 | -0.00631 | NaN | NaN | NaN | 2020-04-08 00:00:00 | 227.95 | -0.00232 | NaN |
| 2020-04-21 00:00:00 | 81.203316 | -0.014009 | NaN | NaN | NaN | 2020-04-09 00:00:00 | 231.52 | 0.015661 | NaN |
| 2020-04-22 00:00:00 | 81.269691 | 0.000817 | NaN | NaN | NaN | 2020-04-10 00:00:00 | 231.6 | 0.000346 | NaN |
| 2020-04-23 00:00:00 | 81.659843 | 0.004801 | NaN | NaN | NaN | 2020-04-13 00:00:00 | 230.69 | -0.003929 | NaN |
| 2020-04-24 00:00:00 | 81.302864 | -0.004372 | NaN | NaN | NaN | 2020-04-14 00:00:00 | 233.98 | 0.014262 | NaN |
| 2020-04-27 00:00:00 | 81.161789 | -0.001735 | NaN | NaN | NaN | 2020-04-15 00:00:00 | 231.54 | -0.010428 | NaN |
| 2020-04-28 00:00:00 | 81.958626 | 0.009818 | NaN | NaN | NaN | 2020-04-16 00:00:00 | 230.99 | -0.002375 | NaN |
| 2020-04-29 00:00:00 | 83.270096 | 0.016002 | NaN | NaN | NaN | 2020-04-17 00:00:00 | 234.23 | 0.014027 | NaN |
| 2020-04-30 00:00:00 | 83.41951 | 0.001794 | NaN | NaN | NaN | 2020-04-20 00:00:00 | 234.47 | 0.001025 | NaN |
| 2020-05-01 00:00:00 | 83.060417 | -0.004305 | NaN | NaN | NaN | 2020-04-21 00:00:00 | 228.79 | -0.024225 | NaN |
| 2020-05-04 00:00:00 | 83.060417 | 0 | NaN | NaN | NaN | 2020-04-22 00:00:00 | 231.59 | 0.012238 | NaN |
| 2020-05-05 00:00:00 | 83.968559 | 0.010934 | NaN | NaN | NaN | 2020-04-23 00:00:00 | 232.52 | 0.004016 | NaN |
| 2020-05-06 00:00:00 | 83.593658 | -0.004465 | NaN | NaN | NaN | 2020-04-24 00:00:00 | 229.45 | -0.013203 | NaN |
| 2020-05-07 00:00:00 | 84.260201 | 0.007974 | NaN | NaN | NaN | 2020-04-27 00:00:00 | 233.3 | 0.016779 | NaN |
| 2020-05-08 00:00:00 | 84.693451 | 0.005142 | NaN | NaN | NaN | 2020-04-28 00:00:00 | 235.31 | 0.008616 | NaN |
| 2020-05-11 00:00:00 | 85.160019 | 0.005509 | NaN | NaN | NaN | 2020-04-29 00:00:00 | 239.9 | 0.019506 | NaN |
| 2020-05-12 00:00:00 | 85.001732 | -0.001859 | NaN | NaN | NaN | 2020-04-30 00:00:00 | 241.39 | 0.006211 | NaN |
| 2020-05-13 00:00:00 | 84.493492 | -0.005979 | NaN | NaN | NaN | 2020-05-01 00:00:00 | 239.2 | -0.009072 | NaN |
| 2020-05-14 00:00:00 | 84.885094 | 0.004635 | NaN | NaN | NaN | 2020-05-04 00:00:00 | 232.15 | -0.029473 | NaN |
| 2020-05-15 00:00:00 | 85.118385 | 0.002748 | NaN | NaN | NaN | 2020-05-05 00:00:00 | 234.39 | 0.009649 | NaN |
| 2020-05-18 00:00:00 | 86.601448 | 0.017424 | NaN | NaN | NaN | 2020-05-06 00:00:00 | 234.83 | 0.001877 | NaN |
| 2020-05-19 00:00:00 | 86.668106 | 0.00077 | NaN | NaN | NaN | 2020-05-07 00:00:00 | 234.54 | -0.001235 | NaN |
| 2020-05-20 00:00:00 | 88.334473 | 0.019227 | NaN | NaN | NaN | 2020-05-08 00:00:00 | 238.3 | 0.016031 | NaN |
| 2020-05-21 00:00:00 | 88.309486 | -0.000283 | NaN | NaN | NaN | 2020-05-11 00:00:00 | 239.36 | 0.004448 | NaN |
| 2020-05-22 00:00:00 | 87.909554 | -0.004529 | NaN | NaN | NaN | 2020-05-12 00:00:00 | 237.97 | -0.005807 | NaN |
| 2020-05-26 00:00:00 | 88.451126 | 0.006161 | NaN | NaN | NaN | 2020-05-13 00:00:00 | 237.79 | -0.000756 | NaN |
| 2020-05-27 00:00:00 | 88.601097 | 0.001696 | NaN | NaN | NaN | 2020-05-14 00:00:00 | 235.7 | -0.008789 | NaN |
| 2020-05-28 00:00:00 | 88.351151 | -0.002821 | NaN | NaN | NaN | 2020-05-15 00:00:00 | 235.82 | 0.000509 | NaN |
| 2020-05-29 00:00:00 | 88.651093 | 0.003395 | NaN | NaN | NaN | 2020-05-18 00:00:00 | 238.72 | 0.012298 | NaN |
| 2020-06-01 00:00:00 | 89.083214 | 0.004874 | NaN | NaN | NaN | 2020-05-19 00:00:00 | 241.44 | 0.011394 | NaN |
| 2020-06-02 00:00:00 | 89.944107 | 0.009664 | NaN | NaN | NaN | 2020-05-20 00:00:00 | 243.25 | 0.007497 | NaN |
| 2020-06-03 00:00:00 | 90.345329 | 0.004461 | NaN | NaN | NaN | 2020-05-21 00:00:00 | 242.92 | -0.001357 | NaN |
| 2020-06-04 00:00:00 | 89.919037 | -0.004718 | NaN | NaN | NaN | 2020-05-22 00:00:00 | 236.81 | -0.025152 | NaN |
| 2020-06-05 00:00:00 | 90.654602 | 0.00818 | NaN | NaN | NaN | 2020-05-25 00:00:00 | 238.6 | 0.007559 | NaN |
| 2020-06-08 00:00:00 | 91.298187 | 0.007099 | NaN | NaN | NaN | 2020-05-26 00:00:00 | 242.35 | 0.015717 | NaN |
| 2020-06-09 00:00:00 | 91.055779 | -0.002655 | NaN | NaN | NaN | 2020-05-27 00:00:00 | 242.7 | 0.001444 | NaN |
| 2020-06-10 00:00:00 | 91.064148 | 0.000092 | NaN | NaN | NaN | 2020-05-28 00:00:00 | 242.42 | -0.001154 | NaN |
| 2020-06-11 00:00:00 | 88.974541 | -0.022947 | NaN | NaN | NaN | 2020-05-29 00:00:00 | 243.9 | 0.006105 | NaN |
| 2020-06-12 00:00:00 | 90.010986 | 0.011649 | NaN | NaN | NaN | 2020-06-01 00:00:00 | 249.33 | 0.022263 | NaN |
| 2020-06-15 00:00:00 | 90.487427 | 0.005293 | NaN | NaN | NaN | 2020-06-02 00:00:00 | 253.66 | 0.017367 | NaN |
| 2020-06-16 00:00:00 | 90.913689 | 0.004711 | NaN | NaN | NaN | 2020-06-03 00:00:00 | 258.21 | 0.017937 | NaN |
| 2020-06-17 00:00:00 | 90.7883 | -0.001379 | NaN | NaN | NaN | 2020-06-04 00:00:00 | 258.38 | 0.000658 | NaN |
| 2020-06-18 00:00:00 | 90.688011 | -0.001105 | NaN | NaN | NaN | 2020-06-05 00:00:00 | 261.85 | 0.01343 | NaN |
| 2020-06-19 00:00:00 | 90.888611 | 0.002212 | NaN | NaN | NaN | 2020-06-08 00:00:00 | 263.39 | 0.005881 | NaN |
| 2020-06-22 00:00:00 | 91.047432 | 0.001747 | NaN | NaN | NaN | 2020-06-09 00:00:00 | 263.62 | 0.000873 | NaN |
| 2020-06-23 00:00:00 | 91.231323 | 0.00202 | NaN | NaN | NaN | 2020-06-10 00:00:00 | 264.12 | 0.001897 | NaN |
| 2020-06-24 00:00:00 | 90.947128 | -0.003115 | NaN | NaN | NaN | 2020-06-11 00:00:00 | 259.01 | -0.019347 | NaN |
| 2020-06-25 00:00:00 | 91.005623 | 0.000643 | NaN | NaN | NaN | 2020-06-12 00:00:00 | 258.13 | -0.003398 | NaN |
| 2020-06-26 00:00:00 | 90.821747 | -0.00202 | NaN | NaN | NaN | 2020-06-15 00:00:00 | 254.1 | -0.015612 | NaN |
| 2020-06-29 00:00:00 | 90.938774 | 0.001289 | NaN | NaN | NaN | 2020-06-16 00:00:00 | 259.01 | 0.019323 | NaN |
| 2020-06-30 00:00:00 | 91.289818 | 0.00386 | NaN | NaN | NaN | 2020-06-17 00:00:00 | 260.51 | 0.005791 | NaN |
| 2020-07-01 00:00:00 | 91.49939 | 0.002296 | NaN | NaN | NaN | 2020-06-18 00:00:00 | 260.85 | 0.001305 | NaN |
| 2020-07-02 00:00:00 | 91.985657 | 0.005314 | NaN | NaN | NaN | 2020-06-19 00:00:00 | 262.5 | 0.006325 | NaN |
| 2020-07-06 00:00:00 | 92.555771 | 0.006198 | NaN | NaN | NaN | 2020-06-22 00:00:00 | 262.77 | 0.001029 | NaN |
| 2020-07-07 00:00:00 | 92.035965 | -0.005616 | NaN | NaN | NaN | 2020-06-23 00:00:00 | 266.4 | 0.013814 | NaN |
| 2020-07-08 00:00:00 | 92.429977 | 0.004281 | NaN | NaN | NaN | 2020-06-24 00:00:00 | 264.46 | -0.007282 | NaN |
| 2020-07-09 00:00:00 | 92.027588 | -0.004353 | NaN | NaN | NaN | 2020-06-25 00:00:00 | 263.75 | -0.002685 | NaN |
| 2020-07-10 00:00:00 | 92.019203 | -0.000091 | NaN | NaN | NaN | 2020-06-26 00:00:00 | 261.81 | -0.007355 | NaN |
| 2020-07-13 00:00:00 | 91.834747 | -0.002005 | NaN | NaN | NaN | 2020-06-29 00:00:00 | 261.11 | -0.002674 | NaN |
| 2020-07-14 00:00:00 | 92.052742 | 0.002374 | NaN | NaN | NaN | 2020-06-30 00:00:00 | 261.23 | 0.00046 | NaN |
| 2020-07-15 00:00:00 | 92.429977 | 0.004098 | NaN | NaN | NaN | 2020-07-01 00:00:00 | 262.85 | 0.006201 | NaN |
| 2020-07-16 00:00:00 | 92.597649 | 0.001814 | NaN | NaN | NaN | 2020-07-02 00:00:00 | 269.22 | 0.024234 | NaN |
| 2020-07-17 00:00:00 | 92.807266 | 0.002264 | NaN | NaN | NaN | 2020-07-03 00:00:00 | 271.7 | 0.009212 | NaN |
| 2020-07-20 00:00:00 | 93.42765 | 0.006685 | NaN | NaN | NaN | 2020-07-06 00:00:00 | 278.94 | 0.026647 | NaN |
| 2020-07-21 00:00:00 | 93.930672 | 0.005384 | NaN | NaN | NaN | 2020-07-07 00:00:00 | 277.2 | -0.006238 | NaN |
| 2020-07-22 00:00:00 | 94.198967 | 0.002856 | NaN | NaN | NaN | 2020-07-08 00:00:00 | 281.73 | 0.016342 | NaN |
| 2020-07-23 00:00:00 | 94.157043 | -0.000445 | NaN | NaN | NaN | 2020-07-09 00:00:00 | 284.11 | 0.008448 | NaN |
| 2020-07-24 00:00:00 | 94.224098 | 0.000712 | NaN | NaN | NaN | 2020-07-10 00:00:00 | 281.41 | -0.009503 | NaN |
| 2020-07-27 00:00:00 | 94.383415 | 0.001691 | NaN | NaN | NaN | 2020-07-13 00:00:00 | 281.77 | 0.001279 | NaN |
| 2020-07-28 00:00:00 | 94.064812 | -0.003376 | NaN | NaN | NaN | 2020-07-14 00:00:00 | 278.27 | -0.012421 | NaN |
| 2020-07-29 00:00:00 | 94.618118 | 0.005882 | NaN | NaN | NaN | 2020-07-15 00:00:00 | 279.57 | 0.004672 | NaN |
| 2020-07-30 00:00:00 | 94.592972 | -0.000266 | NaN | NaN | NaN | 2020-07-16 00:00:00 | 274.64 | -0.017634 | NaN |
| 2020-07-31 00:00:00 | 94.810959 | 0.002304 | NaN | NaN | NaN | 2020-07-17 00:00:00 | 276.79 | 0.007828 | NaN |
| 2020-08-03 00:00:00 | 95.162437 | 0.003707 | NaN | NaN | NaN | 2020-07-20 00:00:00 | 279.71 | 0.01055 | NaN |
| 2020-08-04 00:00:00 | 95.65007 | 0.005124 | NaN | NaN | NaN | 2020-07-21 00:00:00 | 284.6 | 0.017482 | NaN |
| 2020-08-05 00:00:00 | 95.952782 | 0.003165 | NaN | NaN | NaN | 2020-07-22 00:00:00 | 282.72 | -0.006606 | NaN |
| 2020-08-06 00:00:00 | 96.196625 | 0.002541 | NaN | NaN | NaN | 2020-07-23 00:00:00 | 282.9 | 0.000637 | NaN |
| 2020-08-07 00:00:00 | 95.994827 | -0.002098 | NaN | NaN | NaN | 2020-07-24 00:00:00 | 278.11 | -0.016932 | NaN |
| 2020-08-10 00:00:00 | 96.137749 | 0.001489 | NaN | NaN | NaN | 2020-07-27 00:00:00 | 280.46 | 0.00845 | NaN |
| 2020-08-11 00:00:00 | 96.036858 | -0.001049 | NaN | NaN | NaN | 2020-07-28 00:00:00 | 282 | 0.005491 | NaN |
| 2020-08-12 00:00:00 | 95.927544 | -0.001138 | NaN | NaN | NaN | 2020-07-29 00:00:00 | 283.33 | 0.004716 | NaN |
| 2020-08-13 00:00:00 | 95.708954 | -0.002279 | NaN | NaN | NaN | 2020-07-30 00:00:00 | 281.89 | -0.005082 | NaN |
| 2020-08-14 00:00:00 | 95.280128 | -0.004481 | NaN | NaN | NaN | 2020-07-31 00:00:00 | 281.56 | -0.001171 | NaN |
| 2020-08-17 00:00:00 | 95.389435 | 0.001147 | NaN | NaN | NaN | 2020-08-03 00:00:00 | 281.21 | -0.001243 | NaN |
| 2020-08-18 00:00:00 | 95.263321 | -0.001322 | NaN | NaN | NaN | 2020-08-04 00:00:00 | 284 | 0.009921 | NaN |
| 2020-08-19 00:00:00 | 95.044716 | -0.002295 | NaN | NaN | NaN | 2020-08-05 00:00:00 | 287.34 | 0.011761 | NaN |
| 2020-08-20 00:00:00 | 95.263321 | 0.0023 | NaN | NaN | NaN | 2020-08-06 00:00:00 | 287.59 | 0.00087 | NaN |
| 2020-08-21 00:00:00 | 95.565987 | 0.003177 | NaN | NaN | NaN | 2020-08-07 00:00:00 | 283.29 | -0.014952 | NaN |
| 2020-08-24 00:00:00 | 95.759399 | 0.002024 | NaN | NaN | NaN | 2020-08-10 00:00:00 | 282.4 | -0.003142 | NaN |
| 2020-08-25 00:00:00 | 95.288551 | -0.004917 | NaN | NaN | NaN | 2020-08-11 00:00:00 | 283.31 | 0.003222 | NaN |
| 2020-08-26 00:00:00 | 95.069946 | -0.002294 | NaN | NaN | NaN | 2020-08-12 00:00:00 | 283.63 | 0.00113 | NaN |
| 2020-08-27 00:00:00 | 94.624298 | -0.004688 | NaN | NaN | NaN | 2020-08-13 00:00:00 | 284.13 | 0.001763 | NaN |
| 2020-08-28 00:00:00 | 95.507172 | 0.00933 | NaN | NaN | NaN | 2020-08-14 00:00:00 | 283.91 | -0.000774 | NaN |
| 2020-08-31 00:00:00 | 95.498726 | -0.000088 | NaN | NaN | NaN | 2020-08-17 00:00:00 | 285.83 | 0.006763 | NaN |
| 2020-09-01 00:00:00 | 96.142143 | 0.006737 | NaN | NaN | NaN | 2020-08-18 00:00:00 | 288.17 | 0.008187 | NaN |
| 2020-09-02 00:00:00 | 96.538513 | 0.004123 | NaN | NaN | NaN | 2020-08-19 00:00:00 | 286.83 | -0.00465 | NaN |
| 2020-09-03 00:00:00 | 96.0494 | -0.005067 | NaN | NaN | NaN | 2020-08-20 00:00:00 | 282.97 | -0.013457 | NaN |
| 2020-09-04 00:00:00 | 95.6362 | -0.004302 | NaN | NaN | NaN | 2020-08-21 00:00:00 | 285.62 | 0.009365 | NaN |
| 2020-09-08 00:00:00 | 95.256729 | -0.003968 | NaN | NaN | NaN | 2020-08-24 00:00:00 | 289.79 | 0.0146 | NaN |
| 2020-09-09 00:00:00 | 95.737396 | 0.005046 | NaN | NaN | NaN | 2020-08-25 00:00:00 | 290.89 | 0.003796 | NaN |
| 2020-09-10 00:00:00 | 95.467567 | -0.002818 | NaN | NaN | NaN | 2020-08-26 00:00:00 | 291.85 | 0.0033 | NaN |
| 2020-09-11 00:00:00 | 95.501244 | 0.000353 | NaN | NaN | NaN | 2020-08-27 00:00:00 | 291.77 | -0.000274 | NaN |
| 2020-09-14 00:00:00 | 95.594009 | 0.000971 | NaN | NaN | NaN | 2020-08-28 00:00:00 | 293.3 | 0.005244 | NaN |
| 2020-09-15 00:00:00 | 95.754242 | 0.001676 | NaN | NaN | NaN | 2020-08-31 00:00:00 | 288.68 | -0.015752 | NaN |
| 2020-09-16 00:00:00 | 95.526558 | -0.002378 | NaN | NaN | NaN | 2020-09-01 00:00:00 | 293.31 | 0.016039 | NaN |
| 2020-09-17 00:00:00 | 95.130196 | -0.004149 | NaN | NaN | NaN | 2020-09-02 00:00:00 | 293.01 | -0.001023 | NaN |
| 2020-09-18 00:00:00 | 94.691704 | -0.004609 | NaN | NaN | NaN | 2020-09-03 00:00:00 | 289.95 | -0.010443 | NaN |
| 2020-09-21 00:00:00 | 93.764114 | -0.009796 | NaN | NaN | NaN | 2020-09-04 00:00:00 | 287.88 | -0.007139 | NaN |
| 2020-09-22 00:00:00 | 93.570168 | -0.002068 | NaN | NaN | NaN | 2020-09-07 00:00:00 | 286.14 | -0.006044 | NaN |
| 2020-09-23 00:00:00 | 92.364273 | -0.012888 | NaN | NaN | NaN | 2020-09-08 00:00:00 | 283.75 | -0.008353 | NaN |
| 2020-09-24 00:00:00 | 92.608833 | 0.002648 | NaN | NaN | NaN | 2020-09-09 00:00:00 | 283.7 | -0.000176 | NaN |
| 2020-09-25 00:00:00 | 93.055748 | 0.004826 | NaN | NaN | NaN | 2020-09-10 00:00:00 | 283.08 | -0.002185 | NaN |
| 2020-09-28 00:00:00 | 93.266571 | 0.002266 | NaN | NaN | NaN | 2020-09-11 00:00:00 | 284.65 | 0.005546 | NaN |
| 2020-09-29 00:00:00 | 93.055748 | -0.00226 | NaN | NaN | NaN | 2020-09-14 00:00:00 | 287.67 | 0.01061 | NaN |
| 2020-09-30 00:00:00 | 93.511108 | 0.004893 | NaN | NaN | NaN | 2020-09-15 00:00:00 | 289.66 | 0.006918 | NaN |
| 2020-10-01 00:00:00 | 93.68541 | 0.001864 | NaN | NaN | NaN | 2020-09-16 00:00:00 | 290.88 | 0.004212 | NaN |
| 2020-10-02 00:00:00 | 93.355431 | -0.003522 | NaN | NaN | NaN | 2020-09-17 00:00:00 | 288.68 | -0.007563 | NaN |
| 2020-10-05 00:00:00 | 93.719292 | 0.003898 | NaN | NaN | NaN | 2020-09-18 00:00:00 | 288.88 | 0.000693 | NaN |
| 2020-10-06 00:00:00 | 93.786934 | 0.000722 | NaN | NaN | NaN | 2020-09-21 00:00:00 | 283.63 | -0.018174 | NaN |
| 2020-10-07 00:00:00 | 93.990005 | 0.002165 | NaN | NaN | NaN | 2020-09-22 00:00:00 | 282.42 | -0.004266 | NaN |
| 2020-10-08 00:00:00 | 94.90374 | 0.009722 | NaN | NaN | NaN | 2020-09-23 00:00:00 | 280.78 | -0.005807 | NaN |
| 2020-10-09 00:00:00 | 95.132195 | 0.002407 | NaN | NaN | NaN | 2020-09-24 00:00:00 | 275.86 | -0.017523 | NaN |
| 2020-10-12 00:00:00 | 95.377556 | 0.002579 | NaN | NaN | NaN | 2020-09-25 00:00:00 | 276.19 | 0.001196 | NaN |
| 2020-10-13 00:00:00 | 95.140663 | -0.002484 | NaN | NaN | NaN | 2020-09-28 00:00:00 | 278.96 | 0.010029 | NaN |
| 2020-10-14 00:00:00 | 95.106827 | -0.000356 | NaN | NaN | NaN | 2020-09-29 00:00:00 | 278.41 | -0.001972 | NaN |
| 2020-10-15 00:00:00 | 94.726089 | -0.004003 | NaN | NaN | NaN | 2020-09-30 00:00:00 | 281.88 | 0.012464 | NaN |
| 2020-10-16 00:00:00 | 94.869934 | 0.001519 | NaN | NaN | NaN | 2020-10-01 00:00:00 | 283.05 | 0.004151 | NaN |
| 2020-10-19 00:00:00 | 94.319992 | -0.005797 | NaN | NaN | NaN | 2020-10-02 00:00:00 | 282.19 | -0.003038 | NaN |
| 2020-10-20 00:00:00 | 94.37075 | 0.000538 | NaN | NaN | NaN | 2020-10-05 00:00:00 | 284.37 | 0.007725 | NaN |
| 2020-10-21 00:00:00 | 93.888481 | -0.00511 | NaN | NaN | NaN | 2020-10-06 00:00:00 | 287.22 | 0.010022 | NaN |
| 2020-10-22 00:00:00 | 93.448502 | -0.004686 | NaN | NaN | NaN | 2020-10-07 00:00:00 | 288.2 | 0.003412 | NaN |
| 2020-10-23 00:00:00 | 93.888481 | 0.004708 | NaN | NaN | NaN | 2020-10-08 00:00:00 | 290.51 | 0.008015 | NaN |
| 2020-10-26 00:00:00 | 93.550041 | -0.003605 | NaN | NaN | NaN | 2020-10-09 00:00:00 | 292.33 | 0.006265 | NaN |
| 2020-10-27 00:00:00 | 94.108459 | 0.005969 | NaN | NaN | NaN | 2020-10-12 00:00:00 | 295.73 | 0.011631 | NaN |
| 2020-10-28 00:00:00 | 93.304688 | -0.008541 | NaN | NaN | NaN | 2020-10-13 00:00:00 | 295.32 | -0.001386 | NaN |
| 2020-10-29 00:00:00 | 93.338516 | 0.000363 | NaN | NaN | NaN | 2020-10-14 00:00:00 | 295.6 | 0.000948 | NaN |
| 2020-10-30 00:00:00 | 93.084724 | -0.002719 | NaN | NaN | NaN | 2020-10-15 00:00:00 | 291.56 | -0.013667 | NaN |
| 2020-11-02 00:00:00 | 93.234138 | 0.001605 | NaN | NaN | NaN | 2020-10-16 00:00:00 | 292.97 | 0.004836 | NaN |
| 2020-11-03 00:00:00 | 93.989876 | 0.008106 | NaN | NaN | NaN | 2020-10-19 00:00:00 | 293.43 | 0.00157 | NaN |
| 2020-11-04 00:00:00 | 95.806999 | 0.019333 | NaN | NaN | NaN | 2020-10-20 00:00:00 | 295.18 | 0.005964 | NaN |
| 2020-11-05 00:00:00 | 96.17215 | 0.003811 | NaN | NaN | NaN | 2020-10-21 00:00:00 | 295.88 | 0.002371 | NaN |
| 2020-11-06 00:00:00 | 95.747574 | -0.004415 | NaN | NaN | NaN | 2020-10-22 00:00:00 | 295.66 | -0.000744 | NaN |
| 2020-11-09 00:00:00 | 96.206116 | 0.004789 | NaN | NaN | NaN | 2020-10-23 00:00:00 | 295.77 | 0.000372 | NaN |
| 2020-11-10 00:00:00 | 96.104187 | -0.001059 | NaN | NaN | NaN | 2020-10-26 00:00:00 | 293.83 | -0.006559 | NaN |
| 2020-11-11 00:00:00 | 96.46933 | 0.003799 | NaN | NaN | NaN | 2020-10-27 00:00:00 | 294.45 | 0.00211 | NaN |
| 2020-11-12 00:00:00 | 96.282516 | -0.001937 | NaN | NaN | NaN | 2020-10-28 00:00:00 | 290.74 | -0.0126 | NaN |
| 2020-11-13 00:00:00 | 96.656143 | 0.003881 | NaN | NaN | NaN | 2020-10-29 00:00:00 | 290.9 | 0.00055 | NaN |
| 2020-11-16 00:00:00 | 96.868408 | 0.002196 | NaN | NaN | NaN | 2020-10-30 00:00:00 | 287.35 | -0.012204 | NaN |
| 2020-11-17 00:00:00 | 96.698586 | -0.001753 | NaN | NaN | NaN | 2020-11-02 00:00:00 | 289.59 | 0.007795 | NaN |
| 2020-11-18 00:00:00 | 96.613678 | -0.000878 | NaN | NaN | NaN | 2020-11-03 00:00:00 | 291.27 | 0.005801 | NaN |
| 2020-11-19 00:00:00 | 96.83448 | 0.002285 | NaN | NaN | NaN | 2020-11-04 00:00:00 | 295.15 | 0.013321 | NaN |
| 2020-11-20 00:00:00 | 96.902405 | 0.000701 | NaN | NaN | NaN | 2020-11-05 00:00:00 | 302.67 | 0.025479 | NaN |
| 2020-11-23 00:00:00 | 96.825981 | -0.000789 | NaN | NaN | NaN | 2020-11-06 00:00:00 | 305.09 | 0.007996 | NaN |
| 2020-11-24 00:00:00 | 96.961807 | 0.001403 | NaN | NaN | NaN | 2020-11-09 00:00:00 | 309.39 | 0.014094 | NaN |
| 2020-11-25 00:00:00 | 96.885414 | -0.000788 | NaN | NaN | NaN | 2020-11-10 00:00:00 | 306.37 | -0.009761 | NaN |
| 2020-11-27 00:00:00 | 97.199577 | 0.003243 | NaN | NaN | NaN | 2020-11-11 00:00:00 | 305.26 | -0.003623 | NaN |
| 2020-11-30 00:00:00 | 97.012772 | -0.001922 | NaN | NaN | NaN | 2020-11-12 00:00:00 | 306.38 | 0.003669 | NaN |
| 2020-12-01 00:00:00 | 97.256477 | 0.002512 | NaN | NaN | NaN | 2020-11-13 00:00:00 | 307.75 | 0.004472 | NaN |
| 2020-12-02 00:00:00 | 97.307594 | 0.000526 | NaN | NaN | NaN | 2020-11-16 00:00:00 | 310.62 | 0.009326 | NaN |
| 2020-12-03 00:00:00 | 97.716591 | 0.004203 | NaN | NaN | NaN | 2020-11-17 00:00:00 | 310.72 | 0.000322 | NaN |
| 2020-12-04 00:00:00 | 97.801804 | 0.000872 | NaN | NaN | NaN | 2020-11-18 00:00:00 | 312.36 | 0.005278 | NaN |
| 2020-12-07 00:00:00 | 97.78476 | -0.000174 | NaN | NaN | NaN | 2020-11-19 00:00:00 | 311.08 | -0.004098 | NaN |
| 2020-12-08 00:00:00 | 97.622833 | -0.001656 | NaN | NaN | NaN | 2020-11-20 00:00:00 | 313.57 | 0.008004 | NaN |
| 2020-12-09 00:00:00 | 97.384277 | -0.002444 | NaN | NaN | NaN | 2020-11-23 00:00:00 | 315.65 | 0.006633 | NaN |
| 2020-12-10 00:00:00 | 97.869957 | 0.004987 | NaN | NaN | NaN | 2020-11-24 00:00:00 | 317.08 | 0.00453 | NaN |
| 2020-12-11 00:00:00 | 97.921089 | 0.000522 | NaN | NaN | NaN | 2020-11-25 00:00:00 | 314.9 | -0.006875 | NaN |
| 2020-12-14 00:00:00 | 97.921089 | 0 | NaN | NaN | NaN | 2020-11-26 00:00:00 | 317.53 | 0.008352 | NaN |
| 2020-12-15 00:00:00 | 98.25341 | 0.003394 | NaN | NaN | NaN | 2020-11-27 00:00:00 | 318.28 | 0.002362 | NaN |
| 2020-12-16 00:00:00 | 98.321571 | 0.000694 | NaN | NaN | NaN | 2020-11-30 00:00:00 | 312.62 | -0.017783 | NaN |
| 2020-12-17 00:00:00 | 98.642189 | 0.003261 | NaN | NaN | NaN | 2020-12-01 00:00:00 | 317.3 | 0.01497 | NaN |
| 2020-12-18 00:00:00 | 98.513931 | -0.0013 | NaN | NaN | NaN | 2020-12-02 00:00:00 | 317.47 | 0.000536 | NaN |
| 2020-12-21 00:00:00 | 98.231766 | -0.002864 | NaN | NaN | NaN | 2020-12-03 00:00:00 | 319.78 | 0.007276 | NaN |
| 2020-12-22 00:00:00 | 98.351486 | 0.001219 | NaN | NaN | NaN | 2020-12-04 00:00:00 | 321.8 | 0.006317 | NaN |
| 2020-12-23 00:00:00 | 98.496834 | 0.001478 | NaN | NaN | NaN | 2020-12-07 00:00:00 | 322.02 | 0.000684 | NaN |
| 2020-12-24 00:00:00 | 98.744797 | 0.002517 | NaN | NaN | NaN | 2020-12-08 00:00:00 | 323.22 | 0.003726 | NaN |
| 2020-12-28 00:00:00 | 98.770447 | 0.00026 | NaN | NaN | NaN | 2020-12-09 00:00:00 | 322.69 | -0.00164 | NaN |
| 2020-12-29 00:00:00 | 98.915794 | 0.001472 | NaN | NaN | NaN | 2020-12-10 00:00:00 | 322.68 | -0.000031 | NaN |
| 2020-12-30 00:00:00 | 99.044052 | 0.001297 | NaN | NaN | NaN | 2020-12-11 00:00:00 | 323.02 | 0.001054 | NaN |
| 2020-12-31 00:00:00 | 99.103882 | 0.000604 | NaN | NaN | NaN | 2020-12-14 00:00:00 | 321.62 | -0.004334 | NaN |
| 2021-01-04 00:00:00 | 98.556694 | -0.005521 | NaN | NaN | NaN | 2020-12-15 00:00:00 | 321.77 | 0.000466 | NaN |
| 2021-01-05 00:00:00 | 98.625114 | 0.000694 | NaN | NaN | NaN | 2020-12-16 00:00:00 | 325.44 | 0.011406 | NaN |
| 2021-01-06 00:00:00 | 97.915436 | -0.007196 | NaN | NaN | NaN | 2020-12-17 00:00:00 | 328.17 | 0.008389 | NaN |
| 2021-01-07 00:00:00 | 97.881248 | -0.000349 | NaN | NaN | NaN | 2020-12-18 00:00:00 | 327.2 | -0.002956 | NaN |
| 2021-01-08 00:00:00 | 97.932526 | 0.000524 | NaN | NaN | NaN | 2020-12-21 00:00:00 | 323.8 | -0.010391 | NaN |
| 2021-01-11 00:00:00 | 97.163025 | -0.007857 | NaN | NaN | NaN | 2020-12-22 00:00:00 | 322.21 | -0.00491 | NaN |
| 2021-01-12 00:00:00 | 96.701324 | -0.004752 | NaN | NaN | NaN | 2020-12-23 00:00:00 | 324.62 | 0.00748 | NaN |
| 2021-01-13 00:00:00 | 97.154457 | 0.004686 | NaN | NaN | NaN | 2020-12-24 00:00:00 | 322.79 | -0.005637 | NaN |
| 2021-01-14 00:00:00 | 96.872314 | -0.002904 | NaN | NaN | NaN | 2020-12-25 00:00:00 | 323.16 | 0.001146 | NaN |
| 2021-01-15 00:00:00 | 96.983475 | 0.001148 | NaN | NaN | NaN | 2020-12-28 00:00:00 | 322.53 | -0.001949 | NaN |
| 2021-01-19 00:00:00 | 97.120277 | 0.001411 | NaN | NaN | NaN | 2020-12-29 00:00:00 | 325.84 | 0.010263 | NaN |
| 2021-01-20 00:00:00 | 97.231453 | 0.001145 | NaN | NaN | NaN | 2020-12-30 00:00:00 | 330.6 | 0.014608 | NaN |
| 2021-01-21 00:00:00 | 97.29985 | 0.000703 | NaN | NaN | NaN | 2020-12-31 00:00:00 | 331.34 | 0.002238 | NaN |
| 2021-01-22 00:00:00 | 97.34259 | 0.000439 | NaN | NaN | NaN | 2021-01-01 00:00:00 | 331.57 | 0.000694 | NaN |
| 2021-01-25 00:00:00 | 97.727325 | 0.003952 | NaN | NaN | NaN | 2021-01-04 00:00:00 | 334.34 | 0.008354 | NaN |
| 2021-01-26 00:00:00 | 97.599091 | -0.001312 | NaN | NaN | NaN | 2021-01-05 00:00:00 | 337.8 | 0.010349 | NaN |
| 2021-01-27 00:00:00 | 97.145935 | -0.004643 | NaN | NaN | NaN | 2021-01-06 00:00:00 | 336.87 | -0.002753 | NaN |
| 2021-01-28 00:00:00 | 97.351128 | 0.002112 | NaN | NaN | NaN | 2021-01-07 00:00:00 | 337.98 | 0.003295 | NaN |
| 2021-01-29 00:00:00 | 97.34259 | -0.000088 | NaN | NaN | NaN | 2021-01-08 00:00:00 | 343.78 | 0.017161 | NaN |
| 2021-02-01 00:00:00 | 97.824615 | 0.004952 | NaN | NaN | NaN | 2021-01-11 00:00:00 | 342.48 | -0.003781 | NaN |
| 2021-02-02 00:00:00 | 97.824615 | 0 | NaN | NaN | NaN | 2021-01-12 00:00:00 | 344.33 | 0.005402 | NaN |
| 2021-02-03 00:00:00 | 97.575851 | -0.002543 | NaN | NaN | NaN | 2021-01-13 00:00:00 | 346.61 | 0.006622 | NaN |
| 2021-02-04 00:00:00 | 97.858925 | 0.002901 | NaN | NaN | NaN | 2021-01-14 00:00:00 | 348.89 | 0.006578 | NaN |
| 2021-02-05 00:00:00 | 97.970436 | 0.00114 | NaN | NaN | NaN | 2021-01-15 00:00:00 | 346.19 | -0.007739 | NaN |
| 2021-02-08 00:00:00 | 97.970436 | 0 | NaN | NaN | NaN | 2021-01-18 00:00:00 | 347.78 | 0.004593 | NaN |
| 2021-02-09 00:00:00 | 97.618759 | -0.00359 | NaN | NaN | NaN | 2021-01-19 00:00:00 | 352.56 | 0.013744 | NaN |
| 2021-02-10 00:00:00 | 97.816032 | 0.002021 | NaN | NaN | NaN | 2021-01-20 00:00:00 | 357.12 | 0.012934 | NaN |
| 2021-02-11 00:00:00 | 97.876106 | 0.000614 | NaN | NaN | NaN | 2021-01-21 00:00:00 | 357.52 | 0.00112 | NaN |
| 2021-02-12 00:00:00 | 97.335724 | -0.005521 | NaN | NaN | NaN | 2021-01-22 00:00:00 | 354.69 | -0.007916 | NaN |
| 2021-02-16 00:00:00 | 96.143478 | -0.012249 | NaN | NaN | NaN | 2021-01-25 00:00:00 | 357.84 | 0.008881 | NaN |
| 2021-02-17 00:00:00 | 96.675262 | 0.005531 | NaN | NaN | NaN | 2021-01-26 00:00:00 | 353.68 | -0.011625 | NaN |
| 2021-02-18 00:00:00 | 96.572334 | -0.001065 | NaN | NaN | NaN | 2021-01-27 00:00:00 | 349.28 | -0.012441 | NaN |
| 2021-02-19 00:00:00 | 96.057663 | -0.005329 | NaN | NaN | NaN | 2021-01-28 00:00:00 | 344.95 | -0.012397 | NaN |
| 2021-02-22 00:00:00 | 95.405823 | -0.006786 | NaN | NaN | NaN | 2021-01-29 00:00:00 | 340.73 | -0.012234 | NaN |
| 2021-02-23 00:00:00 | 95.517319 | 0.001169 | NaN | NaN | NaN | 2021-02-01 00:00:00 | 347.93 | 0.021131 | NaN |
| 2021-02-24 00:00:00 | 95.663132 | 0.001527 | NaN | NaN | NaN | 2021-02-02 00:00:00 | 353.35 | 0.015578 | NaN |
| 2021-02-25 00:00:00 | 93.956245 | -0.017843 | NaN | NaN | NaN | 2021-02-03 00:00:00 | 355.98 | 0.007443 | NaN |
| 2021-02-26 00:00:00 | 94.376518 | 0.004473 | NaN | NaN | NaN | 2021-02-04 00:00:00 | 355.5 | -0.001348 | NaN |
| 2021-03-01 00:00:00 | 94.902321 | 0.005571 | NaN | NaN | NaN | 2021-02-05 00:00:00 | 357.29 | 0.005035 | NaN |
| 2021-03-02 00:00:00 | 94.842064 | -0.000635 | NaN | NaN | NaN | 2021-02-08 00:00:00 | 359.51 | 0.006213 | NaN |
| 2021-03-03 00:00:00 | 94.274147 | -0.005988 | NaN | NaN | NaN | 2021-02-09 00:00:00 | 362.25 | 0.007621 | NaN |
| 2021-03-04 00:00:00 | 93.465302 | -0.00858 | NaN | NaN | NaN | 2021-02-10 00:00:00 | 365.49 | 0.008944 | NaN |
| 2021-03-05 00:00:00 | 93.448074 | -0.000184 | NaN | NaN | NaN | 2021-02-11 00:00:00 | 367.04 | 0.004241 | NaN |
| 2021-03-08 00:00:00 | 91.830368 | -0.017311 | NaN | NaN | NaN | 2021-02-12 00:00:00 | 367.4 | 0.000981 | NaN |
| 2021-03-09 00:00:00 | 92.914581 | 0.011807 | NaN | NaN | NaN | 2021-02-15 00:00:00 | 368.84 | 0.003919 | NaN |
| 2021-03-10 00:00:00 | 93.818108 | 0.009724 | NaN | NaN | NaN | 2021-02-16 00:00:00 | 369.97 | 0.003064 | NaN |
| 2021-03-11 00:00:00 | 94.515053 | 0.007429 | NaN | NaN | NaN | 2021-02-17 00:00:00 | 371.45 | 0.004 | NaN |
| 2021-03-12 00:00:00 | 93.327606 | -0.012564 | NaN | NaN | NaN | 2021-02-18 00:00:00 | 367.1 | -0.011711 | NaN |
| 2021-03-15 00:00:00 | 93.938545 | 0.006546 | NaN | NaN | NaN | 2021-02-19 00:00:00 | 368.17 | 0.002915 | NaN |
| 2021-03-16 00:00:00 | 94.265549 | 0.003481 | NaN | NaN | NaN | 2021-02-22 00:00:00 | 360.27 | -0.021457 | NaN |
| 2021-03-17 00:00:00 | 95.057198 | 0.008398 | NaN | NaN | NaN | 2021-02-23 00:00:00 | 360.55 | 0.000777 | NaN |
| 2021-03-18 00:00:00 | 93.766449 | -0.013579 | NaN | NaN | NaN | 2021-02-24 00:00:00 | 355.64 | -0.013618 | NaN |
| 2021-03-19 00:00:00 | 94.041817 | 0.002937 | NaN | NaN | NaN | 2021-02-25 00:00:00 | 355.86 | 0.000619 | NaN |
| 2021-03-22 00:00:00 | 94.248329 | 0.002196 | NaN | NaN | NaN | 2021-02-26 00:00:00 | 345.68 | -0.028607 | NaN |
| 2021-03-23 00:00:00 | 93.912743 | -0.003561 | NaN | NaN | NaN | 2021-03-01 00:00:00 | 352.43 | 0.019527 | NaN |
| 2021-03-24 00:00:00 | 94.119263 | 0.002199 | NaN | NaN | NaN | 2021-03-02 00:00:00 | 350.92 | -0.004285 | NaN |
| 2021-03-25 00:00:00 | 93.981575 | -0.001463 | NaN | NaN | NaN | 2021-03-03 00:00:00 | 355.27 | 0.012396 | NaN |
| 2021-03-26 00:00:00 | 94.016006 | 0.000366 | NaN | NaN | NaN | 2021-03-04 00:00:00 | 347.71 | -0.02128 | NaN |
| 2021-03-29 00:00:00 | 93.52552 | -0.005217 | NaN | NaN | NaN | 2021-03-05 00:00:00 | 345.69 | -0.005809 | NaN |
| 2021-03-30 00:00:00 | 93.568535 | 0.00046 | NaN | NaN | NaN | 2021-03-08 00:00:00 | 337.39 | -0.02401 | NaN |
| 2021-03-31 00:00:00 | 93.689018 | 0.001288 | NaN | NaN | NaN | 2021-03-09 00:00:00 | 340.26 | 0.008506 | NaN |
| 2021-04-01 00:00:00 | 94.42968 | 0.007906 | NaN | NaN | NaN | 2021-03-10 00:00:00 | 342.84 | 0.007582 | NaN |
| 2021-04-05 00:00:00 | 94.317459 | -0.001188 | NaN | NaN | NaN | 2021-03-11 00:00:00 | 351.1 | 0.024093 | NaN |
| 2021-04-06 00:00:00 | 94.636818 | 0.003386 | NaN | NaN | NaN | 2021-03-12 00:00:00 | 348.12 | -0.008488 | NaN |
| 2021-04-07 00:00:00 | 94.30883 | -0.003466 | NaN | NaN | NaN | 2021-03-15 00:00:00 | 346.23 | -0.005429 | NaN |
| 2021-04-08 00:00:00 | 94.852631 | 0.005766 | NaN | NaN | NaN | 2021-03-16 00:00:00 | 348.11 | 0.00543 | NaN |
| 2021-04-09 00:00:00 | 94.593689 | -0.00273 | NaN | NaN | NaN | 2021-03-17 00:00:00 | 346.81 | -0.003734 | NaN |
| 2021-04-12 00:00:00 | 94.749046 | 0.001642 | NaN | NaN | NaN | 2021-03-18 00:00:00 | 347.35 | 0.001557 | NaN |
| 2021-04-13 00:00:00 | 95.249741 | 0.005284 | NaN | NaN | NaN | 2021-03-19 00:00:00 | 345.31 | -0.005873 | NaN |
| 2021-04-14 00:00:00 | 95.163399 | -0.000906 | NaN | NaN | NaN | 2021-03-22 00:00:00 | 345.15 | -0.000463 | NaN |
| 2021-04-15 00:00:00 | 96.320168 | 0.012156 | NaN | NaN | NaN | 2021-03-23 00:00:00 | 341.91 | -0.009387 | NaN |
| 2021-04-16 00:00:00 | 96.009384 | -0.003227 | NaN | NaN | NaN | 2021-03-24 00:00:00 | 335.12 | -0.019859 | NaN |
| 2021-04-19 00:00:00 | 95.940353 | -0.000719 | NaN | NaN | NaN | 2021-03-25 00:00:00 | 332.33 | -0.008325 | NaN |
| 2021-04-20 00:00:00 | 95.698624 | -0.00252 | NaN | NaN | NaN | 2021-03-26 00:00:00 | 337 | 0.014052 | NaN |
| 2021-04-21 00:00:00 | 95.879906 | 0.001894 | NaN | NaN | NaN | 2021-03-29 00:00:00 | 337.71 | 0.002107 | NaN |
| 2021-04-22 00:00:00 | 96.026657 | 0.001531 | NaN | NaN | NaN | 2021-03-30 00:00:00 | 340.1 | 0.007077 | NaN |
| 2021-04-23 00:00:00 | 96.190681 | 0.001708 | NaN | NaN | NaN | 2021-03-31 00:00:00 | 339.62 | -0.001411 | NaN |
| 2021-04-26 00:00:00 | 95.750427 | -0.004577 | NaN | NaN | NaN | 2021-04-01 00:00:00 | 344.11 | 0.013221 | NaN |
| 2021-04-27 00:00:00 | 95.232506 | -0.005409 | NaN | NaN | NaN | 2021-04-02 00:00:00 | 344.2 | 0.000262 | NaN |
| 2021-04-28 00:00:00 | 95.55188 | 0.003354 | NaN | NaN | NaN | 2021-04-05 00:00:00 | 343.95 | -0.000726 | NaN |
| 2021-04-29 00:00:00 | 95.664078 | 0.001174 | NaN | NaN | NaN | 2021-04-06 00:00:00 | 345.97 | 0.005873 | NaN |
| 2021-04-30 00:00:00 | 95.940353 | 0.002888 | NaN | NaN | NaN | 2021-04-07 00:00:00 | 344.33 | -0.00474 | NaN |
| 2021-05-03 00:00:00 | 95.808716 | -0.001372 | NaN | NaN | NaN | 2021-04-08 00:00:00 | 345.8 | 0.004269 | NaN |
| 2021-05-04 00:00:00 | 95.895317 | 0.000904 | NaN | NaN | NaN | 2021-04-09 00:00:00 | 342.87 | -0.008473 | NaN |
| 2021-05-05 00:00:00 | 96.025177 | 0.001354 | NaN | NaN | NaN | 2021-04-12 00:00:00 | 340.05 | -0.008225 | NaN |
| 2021-05-06 00:00:00 | 96.207062 | 0.001894 | NaN | NaN | NaN | 2021-04-13 00:00:00 | 339.76 | -0.000853 | NaN |
| 2021-05-07 00:00:00 | 96.64003 | 0.0045 | NaN | NaN | NaN | 2021-04-14 00:00:00 | 342.53 | 0.008153 | NaN |
| 2021-05-10 00:00:00 | 96.423538 | -0.00224 | NaN | NaN | NaN | 2021-04-15 00:00:00 | 343.64 | 0.003241 | NaN |
| 2021-05-11 00:00:00 | 96.198395 | -0.002335 | NaN | NaN | NaN | 2021-04-16 00:00:00 | 346.25 | 0.007595 | NaN |
| 2021-05-12 00:00:00 | 95.323792 | -0.009092 | NaN | NaN | NaN | 2021-04-19 00:00:00 | 346.6 | 0.001011 | NaN |
| 2021-05-13 00:00:00 | 95.817352 | 0.005178 | NaN | NaN | NaN | 2021-04-20 00:00:00 | 346.06 | -0.001558 | NaN |
| 2021-05-14 00:00:00 | 96.319641 | 0.005242 | NaN | NaN | NaN | 2021-04-21 00:00:00 | 344.58 | -0.004277 | NaN |
| 2021-05-17 00:00:00 | 96.267685 | -0.000539 | NaN | NaN | NaN | 2021-04-22 00:00:00 | 345.69 | 0.003221 | NaN |
| 2021-05-18 00:00:00 | 96.259018 | -0.00009 | NaN | NaN | NaN | 2021-04-23 00:00:00 | 348.69 | 0.008678 | NaN |
| 2021-05-19 00:00:00 | 95.808716 | -0.004678 | NaN | NaN | NaN | 2021-04-26 00:00:00 | 350.67 | 0.005678 | NaN |
| 2021-05-20 00:00:00 | 96.475502 | 0.00696 | NaN | NaN | NaN | 2021-04-27 00:00:00 | 351.2 | 0.001511 | NaN |
| 2021-05-21 00:00:00 | 96.285004 | -0.001975 | NaN | NaN | NaN | 2021-04-28 00:00:00 | 353.08 | 0.005353 | NaN |
| 2021-05-24 00:00:00 | 96.388878 | 0.001079 | NaN | NaN | NaN | 2021-04-29 00:00:00 | 353.02 | -0.00017 | NaN |
| 2021-05-25 00:00:00 | 96.856514 | 0.004852 | NaN | NaN | NaN | 2021-04-30 00:00:00 | 349 | -0.011387 | NaN |
| 2021-05-26 00:00:00 | 96.847855 | -0.000089 | NaN | NaN | NaN | 2021-05-03 00:00:00 | 347.17 | -0.005244 | NaN |
| 2021-05-27 00:00:00 | 96.666016 | -0.001878 | NaN | NaN | NaN | 2021-05-04 00:00:00 | 344.99 | -0.006279 | NaN |
| 2021-05-28 00:00:00 | 96.865181 | 0.00206 | NaN | NaN | NaN | 2021-05-05 00:00:00 | 344.66 | -0.000957 | NaN |
| 2021-06-01 00:00:00 | 96.993744 | 0.001327 | NaN | NaN | NaN | 2021-05-06 00:00:00 | 346.65 | 0.005774 | NaN |
| 2021-06-02 00:00:00 | 97.141411 | 0.001522 | NaN | NaN | NaN | 2021-05-07 00:00:00 | 348.66 | 0.005798 | NaN |
| 2021-06-03 00:00:00 | 96.66362 | -0.004919 | NaN | NaN | NaN | 2021-05-10 00:00:00 | 347.55 | -0.003184 | NaN |
| 2021-06-04 00:00:00 | 97.30648 | 0.00665 | NaN | NaN | NaN | 2021-05-11 00:00:00 | 343.59 | -0.011394 | NaN |
| 2021-06-07 00:00:00 | 97.089317 | -0.002232 | NaN | NaN | NaN | 2021-05-12 00:00:00 | 340.16 | -0.009983 | NaN |
| 2021-06-08 00:00:00 | 97.471542 | 0.003937 | NaN | NaN | NaN | 2021-05-13 00:00:00 | 335.04 | -0.015052 | NaN |
| 2021-06-09 00:00:00 | 97.819023 | 0.003565 | NaN | NaN | NaN | 2021-05-14 00:00:00 | 338.29 | 0.0097 | NaN |
| 2021-06-10 00:00:00 | 97.966736 | 0.00151 | NaN | NaN | NaN | 2021-05-17 00:00:00 | 339.63 | 0.003961 | NaN |
| 2021-06-11 00:00:00 | 98.079643 | 0.001153 | NaN | NaN | NaN | 2021-05-18 00:00:00 | 345.37 | 0.016901 | NaN |
| 2021-06-14 00:00:00 | 97.488907 | -0.006023 | NaN | NaN | NaN | 2021-05-19 00:00:00 | 343.94 | -0.00414 | NaN |
| 2021-06-15 00:00:00 | 97.706078 | 0.002228 | NaN | NaN | NaN | 2021-05-20 00:00:00 | 344.45 | 0.001483 | NaN |
| 2021-06-16 00:00:00 | 96.872139 | -0.008535 | NaN | NaN | NaN | 2021-05-21 00:00:00 | 344.78 | 0.000958 | NaN |
| 2021-06-17 00:00:00 | 97.254372 | 0.003946 | NaN | NaN | NaN | 2021-05-24 00:00:00 | 344.65 | -0.000377 | NaN |
| 2021-06-18 00:00:00 | 97.532364 | 0.002858 | NaN | NaN | NaN | 2021-05-25 00:00:00 | 348.92 | 0.012389 | NaN |
| 2021-06-21 00:00:00 | 97.471542 | -0.000624 | NaN | NaN | NaN | 2021-05-26 00:00:00 | 350.79 | 0.005359 | NaN |
| 2021-06-22 00:00:00 | 97.428116 | -0.000446 | NaN | NaN | NaN | 2021-05-27 00:00:00 | 352.03 | 0.003535 | NaN |
| 2021-06-23 00:00:00 | 97.541046 | 0.001159 | NaN | NaN | NaN | 2021-05-28 00:00:00 | 353.55 | 0.004318 | NaN |
| 2021-06-24 00:00:00 | 97.57579 | 0.000356 | NaN | NaN | NaN | 2021-05-31 00:00:00 | 357.07 | 0.009956 | NaN |
| 2021-06-25 00:00:00 | 97.410728 | -0.001692 | NaN | NaN | NaN | 2021-06-01 00:00:00 | 360.55 | 0.009746 | NaN |
| 2021-06-28 00:00:00 | 97.593155 | 0.001873 | NaN | NaN | NaN | 2021-06-02 00:00:00 | 360.82 | 0.000749 | NaN |
| 2021-06-29 00:00:00 | 97.567123 | -0.000267 | NaN | NaN | NaN | 2021-06-03 00:00:00 | 359.36 | -0.004046 | NaN |
| 2021-06-30 00:00:00 | 97.697418 | 0.001335 | NaN | NaN | NaN | 2021-06-04 00:00:00 | 359.35 | -0.000028 | NaN |
| 2021-07-01 00:00:00 | 97.597191 | -0.001026 | NaN | NaN | NaN | 2021-06-07 00:00:00 | 359 | -0.000974 | NaN |
| 2021-07-02 00:00:00 | 97.710487 | 0.001161 | NaN | NaN | NaN | 2021-06-08 00:00:00 | 358.41 | -0.001643 | NaN |
| 2021-07-06 00:00:00 | 97.823776 | 0.001159 | NaN | NaN | NaN | 2021-06-09 00:00:00 | 357.69 | -0.002009 | NaN |
| 2021-07-07 00:00:00 | 97.963219 | 0.001425 | NaN | NaN | NaN | 2021-06-10 00:00:00 | 359.54 | 0.005172 | NaN |
| 2021-07-08 00:00:00 | 97.762764 | -0.002046 | NaN | NaN | NaN | 2021-06-11 00:00:00 | 359.7 | 0.000445 | NaN |
| 2021-07-09 00:00:00 | 97.736641 | -0.000267 | NaN | NaN | NaN | 2021-06-14 00:00:00 | 360.42 | 0.002002 | NaN |
| 2021-07-12 00:00:00 | 97.797623 | 0.000624 | NaN | NaN | NaN | 2021-06-15 00:00:00 | 358.56 | -0.005161 | NaN |
| 2021-07-13 00:00:00 | 97.449028 | -0.003564 | NaN | NaN | NaN | 2021-06-16 00:00:00 | 355.87 | -0.007502 | NaN |
| 2021-07-14 00:00:00 | 97.867355 | 0.004293 | NaN | NaN | NaN | 2021-06-17 00:00:00 | 354.57 | -0.003653 | NaN |
| 2021-07-15 00:00:00 | 98.172371 | 0.003117 | NaN | NaN | NaN | 2021-06-18 00:00:00 | 354.09 | -0.001354 | NaN |
| 2021-07-16 00:00:00 | 98.041641 | -0.001332 | NaN | NaN | NaN | 2021-06-21 00:00:00 | 351.85 | -0.006326 | NaN |
| 2021-07-19 00:00:00 | 98.059067 | 0.000178 | NaN | NaN | NaN | 2021-06-22 00:00:00 | 350.98 | -0.002473 | NaN |
| 2021-07-20 00:00:00 | 98.329239 | 0.002755 | NaN | NaN | NaN | 2021-06-23 00:00:00 | 354.53 | 0.010115 | NaN |
| 2021-07-21 00:00:00 | 97.954506 | -0.003811 | NaN | NaN | NaN | 2021-06-24 00:00:00 | 356.13 | 0.004513 | NaN |
| 2021-07-22 00:00:00 | 98.172371 | 0.002224 | NaN | NaN | NaN | 2021-06-25 00:00:00 | 359.35 | 0.009042 | NaN |
| 2021-07-23 00:00:00 | 98.181084 | 0.000089 | NaN | NaN | NaN | 2021-06-28 00:00:00 | 359.43 | 0.000223 | NaN |
| 2021-07-26 00:00:00 | 97.910904 | -0.002752 | NaN | NaN | NaN | 2021-06-29 00:00:00 | 358.53 | -0.002504 | NaN |
| 2021-07-27 00:00:00 | 97.649483 | -0.00267 | NaN | NaN | NaN | 2021-06-30 00:00:00 | 357.51 | -0.002845 | NaN |
| 2021-07-28 00:00:00 | 97.893501 | 0.002499 | NaN | NaN | NaN | 2021-07-01 00:00:00 | 355.92 | -0.004447 | NaN |
| 2021-07-29 00:00:00 | 97.980652 | 0.00089 | NaN | NaN | NaN | 2021-07-02 00:00:00 | 353.12 | -0.007867 | NaN |
| 2021-07-30 00:00:00 | 98.242088 | 0.002668 | NaN | NaN | NaN | 2021-07-05 00:00:00 | 353.41 | 0.000821 | NaN |
| 2021-08-02 00:00:00 | 98.373222 | 0.001335 | NaN | NaN | NaN | 2021-07-06 00:00:00 | 350.16 | -0.009196 | NaN |
| 2021-08-03 00:00:00 | 98.416924 | 0.000444 | NaN | NaN | NaN | 2021-07-07 00:00:00 | 349.27 | -0.002542 | NaN |
| 2021-08-04 00:00:00 | 98.460655 | 0.000444 | NaN | NaN | NaN | 2021-07-08 00:00:00 | 343.35 | -0.01695 | NaN |
| 2021-08-05 00:00:00 | 98.399437 | -0.000622 | NaN | NaN | NaN | 2021-07-09 00:00:00 | 345.29 | 0.00565 | NaN |
| 2021-08-06 00:00:00 | 97.874924 | -0.00533 | NaN | NaN | NaN | 2021-07-12 00:00:00 | 347.23 | 0.005618 | NaN |
| 2021-08-09 00:00:00 | 97.551483 | -0.003305 | NaN | NaN | NaN | 2021-07-13 00:00:00 | 349.69 | 0.007085 | NaN |
| 2021-08-10 00:00:00 | 97.533997 | -0.000179 | NaN | NaN | NaN | 2021-07-14 00:00:00 | 349.57 | -0.000343 | NaN |
| 2021-08-11 00:00:00 | 97.595184 | 0.000627 | NaN | NaN | NaN | 2021-07-15 00:00:00 | 351.76 | 0.006265 | NaN |
| 2021-08-12 00:00:00 | 97.726311 | 0.001344 | NaN | NaN | NaN | 2021-07-16 00:00:00 | 349.79 | -0.0056 | NaN |
| 2021-08-13 00:00:00 | 98.189636 | 0.004741 | NaN | NaN | NaN | 2021-07-19 00:00:00 | 344.53 | -0.015038 | NaN |
| 2021-08-16 00:00:00 | 98.207108 | 0.000178 | NaN | NaN | NaN | 2021-07-20 00:00:00 | 342.95 | -0.004586 | NaN |
| 2021-08-17 00:00:00 | 98.11972 | -0.00089 | NaN | NaN | NaN | 2021-07-21 00:00:00 | 343.74 | 0.002304 | NaN |
| 2021-08-18 00:00:00 | 98.041031 | -0.000802 | NaN | NaN | NaN | 2021-07-22 00:00:00 | 347.03 | 0.009571 | NaN |
| 2021-08-19 00:00:00 | 98.137184 | 0.000981 | NaN | NaN | NaN | 2021-07-23 00:00:00 | 342.79 | -0.012218 | NaN |
| 2021-08-20 00:00:00 | 97.997307 | -0.001425 | NaN | NaN | NaN | 2021-07-26 00:00:00 | 334.85 | -0.023163 | NaN |
| 2021-08-23 00:00:00 | 98.364479 | 0.003747 | NaN | NaN | NaN | 2021-07-27 00:00:00 | 327.16 | -0.022966 | NaN |
| 2021-08-24 00:00:00 | 98.425636 | 0.000622 | NaN | NaN | NaN | 2021-07-28 00:00:00 | 331.47 | 0.013174 | NaN |
| 2021-08-25 00:00:00 | 98.355736 | -0.00071 | NaN | NaN | NaN | 2021-07-29 00:00:00 | 338.17 | 0.020213 | NaN |
| 2021-08-26 00:00:00 | 98.19841 | -0.0016 | NaN | NaN | NaN | 2021-07-30 00:00:00 | 334.62 | -0.010498 | NaN |
| 2021-08-27 00:00:00 | 98.827805 | 0.006409 | NaN | NaN | NaN | 2021-08-02 00:00:00 | 338.84 | 0.012611 | NaN |
| 2021-08-30 00:00:00 | 99.090073 | 0.002654 | NaN | NaN | NaN | 2021-08-03 00:00:00 | 338.05 | -0.002331 | NaN |
| 2021-08-31 00:00:00 | 99.125031 | 0.000353 | NaN | NaN | NaN | 2021-08-04 00:00:00 | 340.17 | 0.006271 | NaN |
| 2021-09-01 00:00:00 | 99.298637 | 0.001751 | NaN | NaN | NaN | 2021-08-05 00:00:00 | 339.06 | -0.003263 | NaN |
| 2021-09-02 00:00:00 | 99.570488 | 0.002738 | NaN | NaN | NaN | 2021-08-06 00:00:00 | 336.9 | -0.006371 | NaN |
| 2021-09-03 00:00:00 | 99.24604 | -0.003258 | NaN | NaN | NaN | 2021-08-09 00:00:00 | 337.54 | 0.0019 | NaN |
| 2021-09-07 00:00:00 | 98.974213 | -0.002739 | NaN | NaN | NaN | 2021-08-10 00:00:00 | 339.36 | 0.005392 | NaN |
| 2021-09-08 00:00:00 | 99.149559 | 0.001772 | NaN | NaN | NaN | 2021-08-11 00:00:00 | 339.28 | -0.000236 | NaN |
| 2021-09-09 00:00:00 | 99.316177 | 0.00168 | NaN | NaN | NaN | 2021-08-12 00:00:00 | 338.21 | -0.003154 | NaN |
| 2021-09-10 00:00:00 | 99.000496 | -0.003179 | NaN | NaN | NaN | 2021-08-13 00:00:00 | 336.45 | -0.005204 | NaN |
| 2021-09-13 00:00:00 | 99.13205 | 0.001329 | NaN | NaN | NaN | 2021-08-16 00:00:00 | 333.54 | -0.008649 | NaN |
| 2021-09-14 00:00:00 | 99.324951 | 0.001946 | NaN | NaN | NaN | 2021-08-17 00:00:00 | 329.49 | -0.012142 | NaN |
| 2021-09-15 00:00:00 | 99.307426 | -0.000176 | NaN | NaN | NaN | 2021-08-18 00:00:00 | 330.87 | 0.004188 | NaN |
| 2021-09-16 00:00:00 | 98.974213 | -0.003355 | NaN | NaN | NaN | 2021-08-19 00:00:00 | 323.88 | -0.021126 | NaN |
| 2021-09-17 00:00:00 | 98.64975 | -0.003278 | NaN | NaN | NaN | 2021-08-20 00:00:00 | 321.23 | -0.008182 | NaN |
| 2021-09-20 00:00:00 | 98.193771 | -0.004622 | NaN | NaN | NaN | 2021-08-23 00:00:00 | 326.25 | 0.015627 | NaN |
| 2021-09-21 00:00:00 | 98.377922 | 0.001875 | NaN | NaN | NaN | 2021-08-24 00:00:00 | 333.81 | 0.023172 | NaN |
| 2021-09-22 00:00:00 | 98.439316 | 0.000624 | NaN | NaN | NaN | 2021-08-25 00:00:00 | 335.47 | 0.004973 | NaN |
| 2021-09-23 00:00:00 | 97.685181 | -0.007661 | NaN | NaN | NaN | 2021-08-26 00:00:00 | 333.09 | -0.007095 | NaN |
| 2021-09-24 00:00:00 | 97.281822 | -0.004129 | NaN | NaN | NaN | 2021-08-27 00:00:00 | 335.25 | 0.006485 | NaN |
| 2021-09-27 00:00:00 | 96.992432 | -0.002975 | NaN | NaN | NaN | 2021-08-30 00:00:00 | 338.88 | 0.010828 | NaN |
| 2021-09-28 00:00:00 | 96.44001 | -0.005696 | NaN | NaN | NaN | 2021-08-31 00:00:00 | 343.62 | 0.013987 | NaN |
| 2021-09-29 00:00:00 | 96.527672 | 0.000909 | NaN | NaN | NaN | 2021-09-01 00:00:00 | 345.15 | 0.004453 | NaN |
| 2021-09-30 00:00:00 | 96.510124 | -0.000182 | NaN | NaN | NaN | 2021-09-02 00:00:00 | 345.18 | 0.000087 | NaN |
| 2021-10-01 00:00:00 | 96.488167 | -0.000228 | NaN | NaN | NaN | 2021-09-03 00:00:00 | 346.12 | 0.002723 | NaN |
| 2021-10-04 00:00:00 | 96.02195 | -0.004832 | NaN | NaN | NaN | 2021-09-06 00:00:00 | 347.97 | 0.005345 | NaN |
| 2021-10-05 00:00:00 | 96.083527 | 0.000641 | NaN | NaN | NaN | 2021-09-07 00:00:00 | 348.89 | 0.002644 | NaN |
| 2021-10-06 00:00:00 | 95.881233 | -0.002105 | NaN | NaN | NaN | 2021-09-08 00:00:00 | 345.54 | -0.009602 | NaN |
| 2021-10-07 00:00:00 | 95.986763 | 0.001101 | NaN | NaN | NaN | 2021-09-09 00:00:00 | 343.68 | -0.005383 | NaN |
| 2021-10-08 00:00:00 | 95.74926 | -0.002474 | NaN | NaN | NaN | 2021-09-10 00:00:00 | 345.63 | 0.005674 | NaN |
| 2021-10-11 00:00:00 | 95.485397 | -0.002756 | NaN | NaN | NaN | 2021-09-13 00:00:00 | 344.47 | -0.003356 | NaN |
| 2021-10-12 00:00:00 | 95.793251 | 0.003224 | NaN | NaN | NaN | 2021-09-14 00:00:00 | 342.42 | -0.005951 | NaN |
| 2021-10-13 00:00:00 | 96.400185 | 0.006336 | NaN | NaN | NaN | 2021-09-15 00:00:00 | 340.71 | -0.004994 | NaN |
| 2021-10-14 00:00:00 | 96.813622 | 0.004289 | NaN | NaN | NaN | 2021-09-16 00:00:00 | 337.88 | -0.008306 | NaN |
| 2021-10-15 00:00:00 | 96.699265 | -0.001181 | NaN | NaN | NaN | 2021-09-17 00:00:00 | 337.68 | -0.000592 | NaN |
| 2021-10-18 00:00:00 | 96.382614 | -0.003275 | NaN | NaN | NaN | 2021-09-20 00:00:00 | 331.06 | -0.019604 | NaN |
| 2021-10-19 00:00:00 | 96.312233 | -0.00073 | NaN | NaN | NaN | 2021-09-21 00:00:00 | 332.2 | 0.003443 | NaN |
| 2021-10-20 00:00:00 | 96.365013 | 0.000548 | NaN | NaN | NaN | 2021-09-22 00:00:00 | 333.07 | 0.002619 | NaN |
| 2021-10-21 00:00:00 | 95.951591 | -0.00429 | NaN | NaN | NaN | 2021-09-23 00:00:00 | 336.36 | 0.009878 | NaN |
| 2021-10-22 00:00:00 | 96.329826 | 0.003942 | NaN | NaN | NaN | 2021-09-24 00:00:00 | 334.03 | -0.006927 | NaN |
| 2021-10-25 00:00:00 | 96.400185 | 0.00073 | NaN | NaN | NaN | 2021-09-27 00:00:00 | 334.7 | 0.002006 | NaN |
| 2021-10-26 00:00:00 | 96.602539 | 0.002099 | NaN | NaN | NaN | 2021-09-28 00:00:00 | 332.91 | -0.005348 | NaN |
| 2021-10-27 00:00:00 | 97.174301 | 0.005919 | NaN | NaN | NaN | 2021-09-29 00:00:00 | 330.45 | -0.007389 | NaN |
| 2021-10-28 00:00:00 | 96.989548 | -0.001901 | NaN | NaN | NaN | 2021-09-30 00:00:00 | 331.89 | 0.004358 | NaN |
| 2021-10-29 00:00:00 | 96.66407 | -0.003356 | NaN | NaN | NaN | 2021-10-01 00:00:00 | 330.75 | -0.003435 | NaN |
| 2021-11-01 00:00:00 | 96.397568 | -0.002757 | NaN | NaN | NaN | 2021-10-04 00:00:00 | 328.07 | -0.008103 | NaN |
| 2021-11-02 00:00:00 | 96.521133 | 0.001282 | NaN | NaN | NaN | 2021-10-05 00:00:00 | 329.39 | 0.004024 | NaN |
| 2021-11-03 00:00:00 | 96.371078 | -0.001555 | NaN | NaN | NaN | 2021-10-06 00:00:00 | 327.22 | -0.006588 | NaN |
| 2021-11-04 00:00:00 | 97.068268 | 0.007234 | NaN | NaN | NaN | 2021-10-07 00:00:00 | 333.88 | 0.020353 | NaN |
| 2021-11-05 00:00:00 | 97.800774 | 0.007546 | NaN | NaN | NaN | 2021-10-08 00:00:00 | 334.74 | 0.002576 | NaN |
| 2021-11-08 00:00:00 | 97.712524 | -0.000902 | NaN | NaN | NaN | 2021-10-11 00:00:00 | 335.98 | 0.003704 | NaN |
| 2021-11-09 00:00:00 | 97.889023 | 0.001806 | NaN | NaN | NaN | 2021-10-12 00:00:00 | 333.96 | -0.006012 | NaN |
| 2021-11-10 00:00:00 | 96.459328 | -0.014605 | NaN | NaN | NaN | 2021-10-13 00:00:00 | 335.39 | 0.004282 | NaN |
| 2021-11-11 00:00:00 | 96.459328 | 0 | NaN | NaN | NaN | 2021-10-14 00:00:00 | 336.43 | 0.003101 | NaN |
| 2021-11-12 00:00:00 | 96.706444 | 0.002562 | NaN | NaN | NaN | 2021-10-15 00:00:00 | 340.73 | 0.012781 | NaN |
| 2021-11-15 00:00:00 | 96.450523 | -0.002646 | NaN | NaN | NaN | 2021-10-18 00:00:00 | 340.99 | 0.000763 | NaN |
| 2021-11-16 00:00:00 | 96.229889 | -0.002288 | NaN | NaN | NaN | 2021-10-19 00:00:00 | 343.88 | 0.008475 | NaN |
| 2021-11-17 00:00:00 | 96.3358 | 0.001101 | NaN | NaN | NaN | 2021-10-20 00:00:00 | 344.52 | 0.001861 | NaN |
| 2021-11-18 00:00:00 | 96.582893 | 0.002565 | NaN | NaN | NaN | 2021-10-21 00:00:00 | 342.55 | -0.005718 | NaN |
| 2021-11-19 00:00:00 | 96.556435 | -0.000274 | NaN | NaN | NaN | 2021-10-22 00:00:00 | 342.18 | -0.00108 | NaN |
| 2021-11-22 00:00:00 | 95.559189 | -0.010328 | NaN | NaN | NaN | 2021-10-25 00:00:00 | 342.85 | 0.001958 | NaN |
| 2021-11-23 00:00:00 | 94.959045 | -0.00628 | NaN | NaN | NaN | 2021-10-26 00:00:00 | 342.14 | -0.002071 | NaN |
| 2021-11-24 00:00:00 | 95.109093 | 0.00158 | NaN | NaN | NaN | 2021-10-27 00:00:00 | 339.39 | -0.008038 | NaN |
| 2021-11-26 00:00:00 | 94.050079 | -0.011135 | NaN | NaN | NaN | 2021-10-28 00:00:00 | 337.29 | -0.006188 | NaN |
| 2021-11-29 00:00:00 | 94.861977 | 0.008633 | NaN | NaN | NaN | 2021-10-29 00:00:00 | 334.9 | -0.007086 | NaN |
| 2021-11-30 00:00:00 | 94.844322 | -0.000186 | NaN | NaN | NaN | 2021-11-01 00:00:00 | 335.97 | 0.003195 | NaN |
| 2021-12-01 00:00:00 | 95.505791 | 0.006974 | NaN | NaN | NaN | 2021-11-02 00:00:00 | 334.32 | -0.004911 | NaN |
| 2021-12-02 00:00:00 | 96.072464 | 0.005933 | NaN | NaN | NaN | 2021-11-03 00:00:00 | 335.12 | 0.002393 | NaN |
| 2021-12-03 00:00:00 | 96.196411 | 0.00129 | NaN | NaN | NaN | 2021-11-04 00:00:00 | 336.3 | 0.003521 | NaN |
| 2021-12-06 00:00:00 | 96.284958 | 0.00092 | NaN | NaN | NaN | 2021-11-05 00:00:00 | 335.24 | -0.003152 | NaN |
| 2021-12-07 00:00:00 | 96.798553 | 0.005334 | NaN | NaN | NaN | 2021-11-08 00:00:00 | 337.32 | 0.006205 | NaN |
| 2021-12-08 00:00:00 | 96.656891 | -0.001463 | NaN | NaN | NaN | 2021-11-09 00:00:00 | 338.32 | 0.002965 | NaN |
| 2021-12-09 00:00:00 | 96.594887 | -0.000641 | NaN | NaN | NaN | 2021-11-10 00:00:00 | 338.97 | 0.001921 | NaN |
| 2021-12-10 00:00:00 | 96.612579 | 0.000183 | NaN | NaN | NaN | 2021-11-11 00:00:00 | 341.22 | 0.006638 | NaN |
| 2021-12-13 00:00:00 | 97.011063 | 0.004125 | NaN | NaN | NaN | 2021-11-12 00:00:00 | 341.98 | 0.002227 | NaN |
| 2021-12-14 00:00:00 | 96.76313 | -0.002556 | NaN | NaN | NaN | 2021-11-15 00:00:00 | 342.06 | 0.000234 | NaN |
| 2021-12-15 00:00:00 | 96.453239 | -0.003203 | NaN | NaN | NaN | 2021-11-16 00:00:00 | 342.54 | 0.001403 | NaN |
| 2021-12-16 00:00:00 | 96.549179 | 0.000995 | NaN | NaN | NaN | 2021-11-17 00:00:00 | 341.62 | -0.002686 | NaN |
| 2021-12-17 00:00:00 | 96.380371 | -0.001748 | NaN | NaN | NaN | 2021-11-18 00:00:00 | 337.38 | -0.012411 | NaN |
| 2021-12-20 00:00:00 | 95.865051 | -0.005347 | NaN | NaN | NaN | 2021-11-19 00:00:00 | 337.02 | -0.001067 | NaN |
| 2021-12-21 00:00:00 | 96.149361 | 0.002966 | NaN | NaN | NaN | 2021-11-22 00:00:00 | 333.63 | -0.010059 | NaN |
| 2021-12-22 00:00:00 | 96.255959 | 0.001109 | NaN | NaN | NaN | 2021-11-23 00:00:00 | 332.5 | -0.003387 | NaN |
| 2021-12-23 00:00:00 | 96.398155 | 0.001477 | NaN | NaN | NaN | 2021-11-24 00:00:00 | 332.53 | 0.00009 | NaN |
| 2021-12-27 00:00:00 | 96.753517 | 0.003686 | NaN | NaN | NaN | 2021-11-25 00:00:00 | 333.41 | 0.002646 | NaN |
| 2021-12-28 00:00:00 | 96.664673 | -0.000918 | NaN | NaN | NaN | 2021-11-26 00:00:00 | 325.05 | -0.025074 | NaN |
| 2021-12-29 00:00:00 | 96.566917 | -0.001011 | NaN | NaN | NaN | 2021-11-29 00:00:00 | 323.91 | -0.003507 | NaN |
| 2021-12-30 00:00:00 | 97.020042 | 0.004692 | NaN | NaN | NaN | 2021-11-30 00:00:00 | 322.84 | -0.003303 | NaN |
| 2021-12-31 00:00:00 | 96.89566 | -0.001282 | NaN | NaN | NaN | 2021-12-01 00:00:00 | 324.96 | 0.006567 | NaN |
| 2022-01-03 00:00:00 | 95.936119 | -0.009903 | NaN | NaN | NaN | 2021-12-02 00:00:00 | 326.52 | 0.004801 | NaN |
| 2022-01-04 00:00:00 | 95.882843 | -0.000555 | NaN | NaN | NaN | 2021-12-03 00:00:00 | 323.44 | -0.009433 | NaN |
| 2022-01-05 00:00:00 | 94.96772 | -0.009544 | NaN | NaN | NaN | 2021-12-06 00:00:00 | 322.01 | -0.004421 | NaN |
| 2022-01-06 00:00:00 | 94.878876 | -0.000936 | NaN | NaN | NaN | 2021-12-07 00:00:00 | 326.63 | 0.014347 | NaN |
| 2022-01-07 00:00:00 | 94.692307 | -0.001966 | NaN | NaN | NaN | 2021-12-08 00:00:00 | 328.96 | 0.007133 | NaN |
| 2022-01-10 00:00:00 | 94.372429 | -0.003378 | NaN | NaN | NaN | 2021-12-09 00:00:00 | 329.87 | 0.002766 | NaN |
| 2022-01-11 00:00:00 | 94.567917 | 0.002071 | NaN | NaN | NaN | 2021-12-10 00:00:00 | 328.36 | -0.004578 | NaN |
| 2022-01-12 00:00:00 | 94.372429 | -0.002067 | NaN | NaN | NaN | 2021-12-13 00:00:00 | 326.16 | -0.0067 | NaN |
| 2022-01-13 00:00:00 | 94.052589 | -0.003389 | NaN | NaN | NaN | 2021-12-14 00:00:00 | 324.17 | -0.006101 | NaN |
| 2022-01-14 00:00:00 | 93.226311 | -0.008785 | NaN | NaN | NaN | 2021-12-15 00:00:00 | 321.59 | -0.007959 | NaN |
| 2022-01-18 00:00:00 | 92.36451 | -0.009244 | NaN | NaN | NaN | 2021-12-16 00:00:00 | 323.85 | 0.007028 | NaN |
| 2022-01-19 00:00:00 | 92.986427 | 0.006733 | NaN | NaN | NaN | 2021-12-17 00:00:00 | 321.5 | -0.007256 | NaN |
| 2022-01-20 00:00:00 | 93.315163 | 0.003535 | NaN | NaN | NaN | 2021-12-20 00:00:00 | 314.64 | -0.021337 | NaN |
| 2022-01-21 00:00:00 | 93.812721 | 0.005332 | NaN | NaN | NaN | 2021-12-21 00:00:00 | 319.6 | 0.015764 | NaN |
| 2022-01-24 00:00:00 | 93.1819 | -0.006724 | NaN | NaN | NaN | 2021-12-22 00:00:00 | 320.72 | 0.003504 | NaN |
| 2022-01-25 00:00:00 | 93.324066 | 0.001526 | NaN | NaN | NaN | 2021-12-23 00:00:00 | 323.51 | 0.008699 | NaN |
| 2022-01-26 00:00:00 | 92.835373 | -0.005237 | NaN | NaN | NaN | 2021-12-24 00:00:00 | 323.61 | 0.000309 | NaN |
| 2022-01-27 00:00:00 | 93.359612 | 0.005647 | NaN | NaN | NaN | 2021-12-27 00:00:00 | 324.19 | 0.001792 | NaN |
| 2022-01-28 00:00:00 | 93.652779 | 0.00314 | NaN | NaN | NaN | 2021-12-28 00:00:00 | 324.95 | 0.002344 | NaN |
| 2022-01-31 00:00:00 | 93.626137 | -0.000284 | NaN | NaN | NaN | 2021-12-29 00:00:00 | 322.9 | -0.006309 | NaN |
| 2022-02-01 00:00:00 | 93.869537 | 0.0026 | NaN | NaN | NaN | 2021-12-30 00:00:00 | 325.86 | 0.009167 | NaN |
| 2022-02-02 00:00:00 | 94.297539 | 0.00456 | NaN | NaN | NaN | 2021-12-31 00:00:00 | 327.39 | 0.004695 | NaN |
| 2022-02-03 00:00:00 | 93.486153 | -0.008605 | NaN | NaN | NaN | 2022-01-03 00:00:00 | 328.07 | 0.002077 | NaN |
| 2022-02-04 00:00:00 | 93.040337 | -0.004769 | NaN | NaN | NaN | 2022-01-04 00:00:00 | 327.93 | -0.000427 | NaN |
| 2022-02-07 00:00:00 | 92.933357 | -0.00115 | NaN | NaN | NaN | 2022-01-05 00:00:00 | 325.46 | -0.007532 | NaN |
| 2022-02-08 00:00:00 | 92.692596 | -0.002591 | NaN | NaN | NaN | 2022-01-06 00:00:00 | 324.43 | -0.003165 | NaN |
| 2022-02-09 00:00:00 | 93.022507 | 0.003559 | NaN | NaN | NaN | 2022-01-07 00:00:00 | 325.81 | 0.004254 | NaN |
| 2022-02-10 00:00:00 | 91.800995 | -0.013131 | NaN | NaN | NaN | 2022-01-10 00:00:00 | 328.12 | 0.00709 | NaN |
| 2022-02-11 00:00:00 | 91.266029 | -0.005827 | NaN | NaN | NaN | 2022-01-11 00:00:00 | 330.92 | 0.008533 | NaN |
| 2022-02-14 00:00:00 | 91.613762 | 0.00381 | NaN | NaN | NaN | 2022-01-12 00:00:00 | 336.3 | 0.016258 | NaN |
| 2022-02-15 00:00:00 | 91.961487 | 0.003796 | NaN | NaN | NaN | 2022-01-13 00:00:00 | 334.62 | -0.004996 | NaN |
| 2022-02-16 00:00:00 | 92.228958 | 0.002909 | NaN | NaN | NaN | 2022-01-14 00:00:00 | 333.92 | -0.002092 | NaN |
| 2022-02-17 00:00:00 | 91.800995 | -0.00464 | NaN | NaN | NaN | 2022-01-17 00:00:00 | 334.06 | 0.000419 | NaN |
| 2022-02-18 00:00:00 | 91.836662 | 0.000389 | NaN | NaN | NaN | 2022-01-18 00:00:00 | 330.6 | -0.010357 | NaN |
| 2022-02-22 00:00:00 | 90.677544 | -0.012622 | NaN | NaN | NaN | 2022-01-19 00:00:00 | 330.67 | 0.000212 | NaN |
| 2022-02-23 00:00:00 | 89.15287 | -0.016814 | NaN | NaN | NaN | 2022-01-20 00:00:00 | 334.27 | 0.010887 | NaN |
| 2022-02-24 00:00:00 | 88.252365 | -0.010101 | NaN | NaN | NaN | 2022-01-21 00:00:00 | 330.67 | -0.01077 | NaN |
| 2022-02-25 00:00:00 | 89.313362 | 0.012022 | NaN | NaN | NaN | 2022-01-24 00:00:00 | 325.07 | -0.016935 | NaN |
| 2022-02-28 00:00:00 | 88.448502 | -0.009683 | NaN | NaN | NaN | 2022-01-25 00:00:00 | 322.73 | -0.007198 | NaN |
| 2022-03-01 00:00:00 | 87.084793 | -0.015418 | NaN | NaN | NaN | 2022-01-26 00:00:00 | 322.88 | 0.000465 | NaN |
| 2022-03-02 00:00:00 | 86.896881 | -0.002158 | NaN | NaN | NaN | 2022-01-27 00:00:00 | 319.26 | -0.011212 | NaN |
| 2022-03-03 00:00:00 | 86.521042 | -0.004325 | NaN | NaN | NaN | 2022-01-28 00:00:00 | 318.61 | -0.002036 | NaN |
| 2022-03-04 00:00:00 | 84.659821 | -0.021512 | NaN | NaN | NaN | 2022-01-31 00:00:00 | 324.16 | 0.017419 | NaN |
| 2022-03-07 00:00:00 | 83.99765 | -0.007822 | NaN | NaN | NaN | 2022-02-01 00:00:00 | 325.96 | 0.005553 | NaN |
| 2022-03-08 00:00:00 | 84.731377 | 0.008735 | NaN | NaN | NaN | 2022-02-02 00:00:00 | 325.51 | -0.001381 | NaN |
| 2022-03-09 00:00:00 | 85.554619 | 0.009716 | NaN | NaN | NaN | 2022-02-03 00:00:00 | 324.19 | -0.004055 | NaN |
| 2022-03-10 00:00:00 | 85.679901 | 0.001464 | NaN | NaN | NaN | 2022-02-04 00:00:00 | 325.6 | 0.004349 | NaN |
| 2022-03-11 00:00:00 | 85.017769 | -0.007728 | NaN | NaN | NaN | 2022-02-07 00:00:00 | 325.87 | 0.000829 | NaN |
| 2022-03-14 00:00:00 | 84.838768 | -0.002105 | NaN | NaN | NaN | 2022-02-08 00:00:00 | 327.07 | 0.003682 | NaN |
| 2022-03-15 00:00:00 | 85.348808 | 0.006012 | NaN | NaN | NaN | 2022-02-09 00:00:00 | 331.92 | 0.014829 | NaN |
| 2022-03-16 00:00:00 | 87.093735 | 0.020445 | NaN | NaN | NaN | 2022-02-10 00:00:00 | 333.71 | 0.005393 | NaN |
| 2022-03-17 00:00:00 | 87.648537 | 0.00637 | NaN | NaN | NaN | 2022-02-11 00:00:00 | 330.42 | -0.009859 | NaN |
| 2022-03-18 00:00:00 | 87.290604 | -0.004084 | NaN | NaN | NaN | 2022-02-14 00:00:00 | 325.08 | -0.016161 | NaN |
| 2022-03-21 00:00:00 | 85.760437 | -0.01753 | NaN | NaN | NaN | 2022-02-15 00:00:00 | 329.02 | 0.01212 | NaN |
| 2022-03-22 00:00:00 | 85.608322 | -0.001774 | NaN | NaN | NaN | 2022-02-16 00:00:00 | 332.03 | 0.009148 | NaN |
| 2022-03-23 00:00:00 | 85.679901 | 0.000836 | NaN | NaN | NaN | 2022-02-17 00:00:00 | 331.18 | -0.00256 | NaN |
| 2022-03-24 00:00:00 | 86.019951 | 0.003969 | NaN | NaN | NaN | 2022-02-18 00:00:00 | 328.52 | -0.008032 | NaN |
| 2022-03-25 00:00:00 | 85.823097 | -0.002288 | NaN | NaN | NaN | 2022-02-21 00:00:00 | 325.37 | -0.009588 | NaN |
| 2022-03-28 00:00:00 | 86.655266 | 0.009696 | NaN | NaN | NaN | 2022-02-22 00:00:00 | 321.67 | -0.011372 | NaN |
| 2022-03-29 00:00:00 | 87.505363 | 0.00981 | NaN | NaN | NaN | 2022-02-23 00:00:00 | 321.9 | 0.000715 | NaN |
| 2022-03-30 00:00:00 | 87.567986 | 0.000716 | NaN | NaN | NaN | 2022-02-24 00:00:00 | 308.29 | -0.04228 | NaN |
| 2022-03-31 00:00:00 | 87.478523 | -0.001022 | NaN | NaN | NaN | 2022-02-25 00:00:00 | 313.45 | 0.016737 | NaN |
| 2022-04-01 00:00:00 | 87.795631 | 0.003625 | NaN | NaN | NaN | 2022-02-28 00:00:00 | 312.85 | -0.001914 | NaN |
| 2022-04-04 00:00:00 | 88.137001 | 0.003888 | NaN | NaN | NaN | 2022-03-01 00:00:00 | 314.65 | 0.005754 | NaN |
| 2022-04-05 00:00:00 | 86.717606 | -0.016104 | NaN | NaN | NaN | 2022-03-02 00:00:00 | 312.51 | -0.006801 | NaN |
| 2022-04-06 00:00:00 | 86.457077 | -0.003004 | NaN | NaN | NaN | 2022-03-03 00:00:00 | 312.6 | 0.000288 | NaN |
| 2022-04-07 00:00:00 | 86.205559 | -0.002909 | NaN | NaN | NaN | 2022-03-04 00:00:00 | 305.89 | -0.021465 | NaN |
| 2022-04-08 00:00:00 | 85.459908 | -0.00865 | NaN | NaN | NaN | 2022-03-07 00:00:00 | 296.24 | -0.031547 | NaN |
| 2022-04-11 00:00:00 | 84.444809 | -0.011878 | NaN | NaN | NaN | 2022-03-08 00:00:00 | 288.91 | -0.024743 | NaN |
| 2022-04-12 00:00:00 | 84.759209 | 0.003723 | NaN | NaN | NaN | 2022-03-09 00:00:00 | 292.6 | 0.012772 | NaN |
| 2022-04-13 00:00:00 | 84.974823 | 0.002544 | NaN | NaN | NaN | 2022-03-10 00:00:00 | 294.03 | 0.004887 | NaN |
| 2022-04-14 00:00:00 | 84.184265 | -0.009303 | NaN | NaN | NaN | 2022-03-11 00:00:00 | 290.22 | -0.012958 | NaN |
| 2022-04-18 00:00:00 | 84.139359 | -0.000533 | NaN | NaN | NaN | 2022-03-14 00:00:00 | 282.39 | -0.02698 | NaN |
| 2022-04-19 00:00:00 | 83.806984 | -0.00395 | NaN | NaN | NaN | 2022-03-15 00:00:00 | 275.45 | -0.024576 | NaN |
| 2022-04-20 00:00:00 | 84.381905 | 0.00686 | NaN | NaN | NaN | 2022-03-16 00:00:00 | 290.45 | 0.054456 | NaN |
| 2022-04-21 00:00:00 | 83.618309 | -0.009049 | NaN | NaN | NaN | 2022-03-17 00:00:00 | 298.56 | 0.027922 | NaN |
| 2022-04-22 00:00:00 | 82.728928 | -0.010636 | NaN | NaN | NaN | 2022-03-18 00:00:00 | 300.37 | 0.006062 | NaN |
| 2022-04-25 00:00:00 | 83.699142 | 0.011728 | NaN | NaN | NaN | 2022-03-21 00:00:00 | 298.5 | -0.006226 | NaN |
| 2022-04-26 00:00:00 | 83.124229 | -0.006869 | NaN | NaN | NaN | 2022-03-22 00:00:00 | 302.64 | 0.013869 | NaN |
| 2022-04-27 00:00:00 | 82.899635 | -0.002702 | NaN | NaN | NaN | 2022-03-23 00:00:00 | 304.24 | 0.005287 | NaN |
| 2022-04-28 00:00:00 | 83.052361 | 0.001842 | NaN | NaN | NaN | 2022-03-24 00:00:00 | 303.88 | -0.001183 | NaN |
| 2022-04-29 00:00:00 | 81.641937 | -0.016982 | NaN | NaN | NaN | 2022-03-25 00:00:00 | 301.17 | -0.008918 | NaN |
| 2022-05-02 00:00:00 | 81.194565 | -0.00548 | NaN | NaN | NaN | 2022-03-28 00:00:00 | 301.21 | 0.000133 | NaN |
| 2022-05-03 00:00:00 | 81.537315 | 0.004221 | NaN | NaN | NaN | 2022-03-29 00:00:00 | 304.05 | 0.009429 | NaN |
| 2022-05-04 00:00:00 | 82.935364 | 0.017146 | NaN | NaN | NaN | 2022-03-30 00:00:00 | 307.36 | 0.010886 | NaN |
| 2022-05-05 00:00:00 | 81.690643 | -0.015008 | NaN | NaN | NaN | 2022-03-31 00:00:00 | 304.87 | -0.008101 | NaN |
| 2022-05-06 00:00:00 | 80.59024 | -0.01347 | NaN | NaN | NaN | 2022-04-01 00:00:00 | 307.12 | 0.00738 | NaN |
| 2022-05-09 00:00:00 | 79.877701 | -0.008842 | NaN | NaN | NaN | 2022-04-04 00:00:00 | 311.65 | 0.01475 | NaN |
| 2022-05-10 00:00:00 | 80.274574 | 0.004969 | NaN | NaN | NaN | 2022-04-05 00:00:00 | 309.92 | -0.005551 | NaN |
| 2022-05-11 00:00:00 | 80.626328 | 0.004382 | NaN | NaN | NaN | 2022-04-06 00:00:00 | 307.1 | -0.009099 | NaN |
| 2022-05-12 00:00:00 | 80.680443 | 0.000671 | NaN | NaN | NaN | 2022-04-07 00:00:00 | 302.59 | -0.014686 | NaN |
| 2022-05-13 00:00:00 | 80.545166 | -0.001677 | NaN | NaN | NaN | 2022-04-08 00:00:00 | 303.61 | 0.003371 | NaN |
| 2022-05-16 00:00:00 | 80.112206 | -0.005375 | NaN | NaN | NaN | 2022-04-11 00:00:00 | 299.58 | -0.013274 | NaN |
| 2022-05-17 00:00:00 | 80.400833 | 0.003603 | NaN | NaN | NaN | 2022-04-12 00:00:00 | 299.17 | -0.001369 | NaN |
| 2022-05-18 00:00:00 | 79.886719 | -0.006394 | NaN | NaN | NaN | 2022-04-13 00:00:00 | 300.61 | 0.004813 | NaN |
| 2022-05-19 00:00:00 | 80.319679 | 0.00542 | NaN | NaN | NaN | 2022-04-14 00:00:00 | 299.93 | -0.002262 | NaN |
| 2022-05-20 00:00:00 | 80.842796 | 0.006513 | NaN | NaN | NaN | 2022-04-15 00:00:00 | 299.17 | -0.002534 | NaN |
| 2022-05-23 00:00:00 | 80.896919 | 0.000669 | NaN | NaN | NaN | 2022-04-18 00:00:00 | 297.59 | -0.005281 | NaN |
| 2022-05-24 00:00:00 | 81.600433 | 0.008696 | NaN | NaN | NaN | 2022-04-19 00:00:00 | 294.92 | -0.008972 | NaN |
| 2022-05-25 00:00:00 | 82.322021 | 0.008843 | NaN | NaN | NaN | 2022-04-20 00:00:00 | 294.34 | -0.001967 | NaN |
| 2022-05-26 00:00:00 | 82.592598 | 0.003287 | NaN | NaN | NaN | 2022-04-21 00:00:00 | 291.91 | -0.008256 | NaN |
| 2022-05-27 00:00:00 | 82.727913 | 0.001638 | NaN | NaN | NaN | 2022-04-22 00:00:00 | 288.94 | -0.010174 | NaN |
| 2022-05-31 00:00:00 | 82.30397 | -0.005125 | NaN | NaN | NaN | 2022-04-25 00:00:00 | 281.29 | -0.026476 | NaN |
| 2022-06-01 00:00:00 | 82.154587 | -0.001815 | NaN | NaN | NaN | 2022-04-26 00:00:00 | 281.32 | 0.000107 | NaN |
| 2022-06-02 00:00:00 | 82.951248 | 0.009697 | NaN | NaN | NaN | 2022-04-27 00:00:00 | 281.36 | 0.000142 | NaN |
| 2022-06-03 00:00:00 | 82.389961 | -0.006766 | NaN | NaN | NaN | 2022-04-28 00:00:00 | 283.63 | 0.008068 | NaN |
| 2022-06-06 00:00:00 | 81.303642 | -0.013185 | NaN | NaN | NaN | 2022-04-29 00:00:00 | 287.7 | 0.01435 | NaN |
| 2022-06-07 00:00:00 | 81.783432 | 0.005901 | NaN | NaN | NaN | 2022-05-02 00:00:00 | 287.11 | -0.002051 | NaN |
| 2022-06-08 00:00:00 | 80.977737 | -0.009852 | NaN | NaN | NaN | 2022-05-03 00:00:00 | 286.72 | -0.001358 | NaN |
| 2022-06-09 00:00:00 | 80.307823 | -0.008273 | NaN | NaN | NaN | 2022-05-04 00:00:00 | 285.45 | -0.004429 | NaN |
| 2022-06-10 00:00:00 | 78.958954 | -0.016796 | NaN | NaN | NaN | 2022-05-05 00:00:00 | 283.43 | -0.007077 | NaN |
| 2022-06-13 00:00:00 | 76.867752 | -0.026485 | NaN | NaN | NaN | 2022-05-06 00:00:00 | 276.92 | -0.022969 | NaN |
| 2022-06-14 00:00:00 | 76.831535 | -0.000471 | NaN | NaN | NaN | 2022-05-09 00:00:00 | 271.36 | -0.020078 | NaN |
| 2022-06-15 00:00:00 | 79.130966 | 0.029928 | NaN | NaN | NaN | 2022-05-10 00:00:00 | 269.69 | -0.006154 | NaN |
| 2022-06-16 00:00:00 | 77.374702 | -0.022194 | NaN | NaN | NaN | 2022-05-11 00:00:00 | 270.1 | 0.00152 | NaN |
| 2022-06-17 00:00:00 | 77.79113 | 0.005382 | NaN | NaN | NaN | 2022-05-12 00:00:00 | 264.84 | -0.019474 | NaN |
| 2022-06-21 00:00:00 | 77.564804 | -0.002909 | NaN | NaN | NaN | 2022-05-13 00:00:00 | 269.28 | 0.016765 | NaN |
| 2022-06-22 00:00:00 | 77.682495 | 0.001517 | NaN | NaN | NaN | 2022-05-16 00:00:00 | 269.9 | 0.002302 | NaN |
| 2022-06-23 00:00:00 | 78.198509 | 0.006643 | NaN | NaN | NaN | 2022-05-17 00:00:00 | 275.8 | 0.02186 | NaN |
| 2022-06-24 00:00:00 | 78.298103 | 0.001274 | NaN | NaN | NaN | 2022-05-18 00:00:00 | 275.46 | -0.001233 | NaN |
| 2022-06-27 00:00:00 | 77.229858 | -0.013643 | NaN | NaN | NaN | 2022-05-19 00:00:00 | 272.17 | -0.011944 | NaN |
| 2022-06-28 00:00:00 | 76.641418 | -0.007619 | NaN | NaN | NaN | 2022-05-20 00:00:00 | 276.56 | 0.01613 | NaN |
| 2022-06-29 00:00:00 | 76.922066 | 0.003662 | NaN | NaN | NaN | 2022-05-23 00:00:00 | 276.66 | 0.000362 | NaN |
| 2022-06-30 00:00:00 | 77.23893 | 0.004119 | NaN | NaN | NaN | 2022-05-24 00:00:00 | 272.01 | -0.016808 | NaN |
| 2022-07-01 00:00:00 | 78.321709 | 0.014019 | NaN | NaN | NaN | 2022-05-25 00:00:00 | 272.47 | 0.001691 | NaN |
| 2022-07-05 00:00:00 | 77.703476 | -0.007894 | NaN | NaN | NaN | 2022-05-26 00:00:00 | 274.97 | 0.009175 | NaN |
| 2022-07-06 00:00:00 | 77.07618 | -0.008073 | NaN | NaN | NaN | 2022-05-27 00:00:00 | 278.9 | 0.014292 | NaN |
| 2022-07-07 00:00:00 | 77.303436 | 0.002948 | NaN | NaN | NaN | 2022-05-30 00:00:00 | 283.68 | 0.017139 | NaN |
| 2022-07-08 00:00:00 | 76.939804 | -0.004704 | NaN | NaN | NaN | 2022-05-31 00:00:00 | 286.8 | 0.010998 | NaN |
| 2022-07-11 00:00:00 | 76.294319 | -0.008389 | NaN | NaN | NaN | 2022-06-01 00:00:00 | 284.32 | -0.008647 | NaN |
| 2022-07-12 00:00:00 | 76.076134 | -0.00286 | NaN | NaN | NaN | 2022-06-02 00:00:00 | 284.52 | 0.000703 | NaN |
| 2022-07-13 00:00:00 | 75.767021 | -0.004063 | NaN | NaN | NaN | 2022-06-03 00:00:00 | 283.41 | -0.003901 | NaN |
| 2022-07-14 00:00:00 | 74.43969 | -0.017519 | NaN | NaN | NaN | 2022-06-06 00:00:00 | 286.03 | 0.009245 | NaN |
| 2022-07-15 00:00:00 | 75.185196 | 0.010015 | NaN | NaN | NaN | 2022-06-07 00:00:00 | 284.61 | -0.004965 | NaN |
| 2022-07-18 00:00:00 | 75.22155 | 0.000484 | NaN | NaN | NaN | 2022-06-08 00:00:00 | 287.78 | 0.011138 | NaN |
| 2022-07-19 00:00:00 | 76.321602 | 0.014624 | NaN | NaN | NaN | 2022-06-09 00:00:00 | 284.72 | -0.010633 | NaN |
| 2022-07-20 00:00:00 | 76.921631 | 0.007862 | NaN | NaN | NaN | 2022-06-10 00:00:00 | 281.85 | -0.01008 | NaN |
| 2022-07-21 00:00:00 | 77.348923 | 0.005555 | NaN | NaN | NaN | 2022-06-13 00:00:00 | 272.14 | -0.034451 | NaN |
| 2022-07-22 00:00:00 | 78.194427 | 0.010931 | NaN | NaN | NaN | 2022-06-14 00:00:00 | 273.59 | 0.005328 | NaN |
| 2022-07-25 00:00:00 | 78.248947 | 0.000697 | NaN | NaN | NaN | 2022-06-15 00:00:00 | 274.91 | 0.004825 | NaN |
| 2022-07-26 00:00:00 | 77.521652 | -0.009295 | NaN | NaN | NaN | 2022-06-16 00:00:00 | 270.71 | -0.015278 | NaN |
| 2022-07-27 00:00:00 | 78.694427 | 0.015128 | NaN | NaN | NaN | 2022-06-17 00:00:00 | 269.87 | -0.003103 | NaN |
| 2022-07-28 00:00:00 | 79.712662 | 0.012939 | NaN | NaN | NaN | 2022-06-20 00:00:00 | 268.97 | -0.003335 | NaN |
| 2022-07-29 00:00:00 | 80.021782 | 0.003878 | NaN | NaN | NaN | 2022-06-21 00:00:00 | 273.79 | 0.01792 | NaN |
| 2022-08-01 00:00:00 | 80.383194 | 0.004516 | NaN | NaN | NaN | 2022-06-22 00:00:00 | 268.32 | -0.019979 | NaN |
| 2022-08-02 00:00:00 | 79.214935 | -0.014534 | NaN | NaN | NaN | 2022-06-23 00:00:00 | 269.44 | 0.004174 | NaN |
| 2022-08-03 00:00:00 | 80.739166 | 0.019242 | NaN | NaN | NaN | 2022-06-24 00:00:00 | 273.15 | 0.013769 | NaN |
| 2022-08-04 00:00:00 | 80.912582 | 0.002148 | NaN | NaN | NaN | 2022-06-27 00:00:00 | 276.75 | 0.01318 | NaN |
| 2022-08-05 00:00:00 | 80.748283 | -0.002031 | NaN | NaN | NaN | 2022-06-28 00:00:00 | 276.66 | -0.000325 | NaN |
| 2022-08-08 00:00:00 | 81.943947 | 0.014807 | NaN | NaN | NaN | 2022-06-29 00:00:00 | 273.39 | -0.01182 | NaN |
| 2022-08-09 00:00:00 | 80.57486 | -0.016708 | NaN | NaN | NaN | 2022-06-30 00:00:00 | 270.16 | -0.011815 | NaN |
| 2022-08-10 00:00:00 | 82.016983 | 0.017898 | NaN | NaN | NaN | 2022-07-01 00:00:00 | 268.42 | -0.006441 | NaN |
| 2022-08-11 00:00:00 | 81.679276 | -0.004118 | NaN | NaN | NaN | 2022-07-04 00:00:00 | 268.43 | 0.000037 | NaN |
| 2022-08-12 00:00:00 | 82.299927 | 0.007599 | NaN | NaN | NaN | 2022-07-05 00:00:00 | 267.56 | -0.003241 | NaN |
| 2022-08-15 00:00:00 | 82.144753 | -0.001885 | NaN | NaN | NaN | 2022-07-06 00:00:00 | 264.97 | -0.00968 | NaN |
| 2022-08-16 00:00:00 | 81.432831 | -0.008667 | NaN | NaN | NaN | 2022-07-07 00:00:00 | 268.51 | 0.01336 | NaN |
| 2022-08-17 00:00:00 | 80.538353 | -0.010984 | NaN | NaN | NaN | 2022-07-08 00:00:00 | 269.23 | 0.002681 | NaN |
| 2022-08-18 00:00:00 | 80.447083 | -0.001133 | NaN | NaN | NaN | 2022-07-11 00:00:00 | 264.19 | -0.01872 | NaN |
| 2022-08-19 00:00:00 | 79.224052 | -0.015203 | NaN | NaN | NaN | 2022-07-12 00:00:00 | 261.17 | -0.011431 | NaN |
| 2022-08-22 00:00:00 | 78.6399 | -0.007373 | NaN | NaN | NaN | 2022-07-13 00:00:00 | 261.8 | 0.002412 | NaN |
| 2022-08-23 00:00:00 | 79.470482 | 0.010562 | NaN | NaN | NaN | 2022-07-14 00:00:00 | 259.8 | -0.007639 | NaN |
| 2022-08-24 00:00:00 | 79.397469 | -0.000919 | NaN | NaN | NaN | 2022-07-15 00:00:00 | 259.3 | -0.001925 | NaN |
| 2022-08-25 00:00:00 | 80.237167 | 0.010576 | NaN | NaN | NaN | 2022-07-18 00:00:00 | 263.72 | 0.017046 | NaN |
| 2022-08-26 00:00:00 | 78.986732 | -0.015584 | NaN | NaN | NaN | 2022-07-19 00:00:00 | 264.4 | 0.002578 | NaN |
| 2022-08-29 00:00:00 | 78.512131 | -0.006009 | NaN | NaN | NaN | 2022-07-20 00:00:00 | 265.78 | 0.005219 | NaN |
| 2022-08-30 00:00:00 | 78.484726 | -0.000349 | NaN | NaN | NaN | 2022-07-21 00:00:00 | 266.7 | 0.003462 | NaN |
| 2022-08-31 00:00:00 | 77.854965 | -0.008024 | NaN | NaN | NaN | 2022-07-22 00:00:00 | 266.48 | -0.000825 | NaN |
| 2022-09-01 00:00:00 | 77.664436 | -0.002447 | NaN | NaN | NaN | 2022-07-25 00:00:00 | 265.98 | -0.001876 | NaN |
| 2022-09-02 00:00:00 | 77.939255 | 0.003539 | NaN | NaN | NaN | 2022-07-26 00:00:00 | 265.78 | -0.000752 | NaN |
| 2022-09-06 00:00:00 | 77.224709 | -0.009168 | NaN | NaN | NaN | 2022-07-27 00:00:00 | 266.66 | 0.003311 | NaN |
| 2022-09-07 00:00:00 | 78.39727 | 0.015184 | NaN | NaN | NaN | 2022-07-28 00:00:00 | 268.45 | 0.006713 | NaN |
| 2022-09-08 00:00:00 | 78.424751 | 0.000351 | NaN | NaN | NaN | 2022-07-29 00:00:00 | 267.32 | -0.004209 | NaN |
| 2022-09-09 00:00:00 | 78.901138 | 0.006074 | NaN | NaN | NaN | 2022-08-01 00:00:00 | 268.36 | 0.00389 | NaN |
| 2022-09-12 00:00:00 | 78.873634 | -0.000349 | NaN | NaN | NaN | 2022-08-02 00:00:00 | 265.89 | -0.009204 | NaN |
| 2022-09-13 00:00:00 | 77.664436 | -0.015331 | NaN | NaN | NaN | 2022-08-03 00:00:00 | 265.88 | -0.000038 | NaN |
| 2022-09-14 00:00:00 | 77.609482 | -0.000708 | NaN | NaN | NaN | 2022-08-04 00:00:00 | 267.97 | 0.007861 | NaN |
| 2022-09-15 00:00:00 | 77.554489 | -0.000709 | NaN | NaN | NaN | 2022-08-05 00:00:00 | 269.67 | 0.006344 | NaN |
| 2022-09-16 00:00:00 | 77.133102 | -0.005433 | NaN | NaN | NaN | 2022-08-08 00:00:00 | 269.98 | 0.00115 | NaN |
| 2022-09-19 00:00:00 | 77.407928 | 0.003563 | NaN | NaN | NaN | 2022-08-09 00:00:00 | 269.94 | -0.000148 | NaN |
| 2022-09-20 00:00:00 | 76.69339 | -0.009231 | NaN | NaN | NaN | 2022-08-10 00:00:00 | 269.96 | 0.000074 | NaN |
| 2022-09-21 00:00:00 | 76.473549 | -0.002866 | NaN | NaN | NaN | 2022-08-11 00:00:00 | 273.68 | 0.01378 | NaN |
| 2022-09-22 00:00:00 | 75.960548 | -0.006708 | NaN | NaN | NaN | 2022-08-12 00:00:00 | 274.43 | 0.00274 | NaN |
| 2022-09-23 00:00:00 | 75.044479 | -0.01206 | NaN | NaN | NaN | 2022-08-15 00:00:00 | 274.16 | -0.000984 | NaN |
| 2022-09-26 00:00:00 | 73.276443 | -0.02356 | NaN | NaN | NaN | 2022-08-16 00:00:00 | 274.03 | -0.000474 | NaN |
| 2022-09-27 00:00:00 | 72.103882 | -0.016002 | NaN | NaN | NaN | 2022-08-17 00:00:00 | 274.42 | 0.001423 | NaN |
| 2022-09-28 00:00:00 | 73.835236 | 0.024012 | NaN | NaN | NaN | 2022-08-18 00:00:00 | 273.38 | -0.00379 | NaN |
| 2022-09-29 00:00:00 | 72.900848 | -0.012655 | NaN | NaN | NaN | 2022-08-19 00:00:00 | 271.13 | -0.00823 | NaN |
| 2022-09-30 00:00:00 | 72.735977 | -0.002262 | NaN | NaN | NaN | 2022-08-22 00:00:00 | 269.26 | -0.006897 | NaN |
| 2022-10-03 00:00:00 | 73.841316 | 0.015197 | NaN | NaN | NaN | 2022-08-23 00:00:00 | 269.58 | 0.001188 | NaN |
| 2022-10-04 00:00:00 | 75.231094 | 0.018821 | NaN | NaN | NaN | 2022-08-24 00:00:00 | 268.7 | -0.003264 | NaN |
| 2022-10-05 00:00:00 | 74.16346 | -0.014191 | NaN | NaN | NaN | 2022-08-25 00:00:00 | 273.05 | 0.016189 | NaN |
| 2022-10-06 00:00:00 | 73.878151 | -0.003847 | NaN | NaN | NaN | 2022-08-26 00:00:00 | 273.3 | 0.000916 | NaN |
| 2022-10-07 00:00:00 | 72.884148 | -0.013455 | NaN | NaN | NaN | 2022-08-29 00:00:00 | 270.16 | -0.011489 | NaN |
| 2022-10-10 00:00:00 | 72.67247 | -0.002904 | NaN | NaN | NaN | 2022-08-30 00:00:00 | 270.04 | -0.000444 | NaN |
| 2022-10-11 00:00:00 | 72.617249 | -0.00076 | NaN | NaN | NaN | 2022-08-31 00:00:00 | 270.04 | 0 | NaN |
| 2022-10-12 00:00:00 | 72.359535 | -0.003549 | NaN | NaN | NaN | 2022-09-01 00:00:00 | 266.43 | -0.013368 | NaN |
| 2022-10-13 00:00:00 | 72.138634 | -0.003053 | NaN | NaN | NaN | 2022-09-02 00:00:00 | 265.78 | -0.00244 | NaN |
| 2022-10-14 00:00:00 | 71.604851 | -0.007399 | NaN | NaN | NaN | 2022-09-05 00:00:00 | 265.18 | -0.002258 | NaN |
| 2022-10-17 00:00:00 | 72.000603 | 0.005527 | NaN | NaN | NaN | 2022-09-06 00:00:00 | 264.02 | -0.004374 | NaN |
| 2022-10-18 00:00:00 | 72.764496 | 0.01061 | NaN | NaN | NaN | 2022-09-07 00:00:00 | 262.8 | -0.004621 | NaN |
| 2022-10-19 00:00:00 | 71.678459 | -0.014925 | NaN | NaN | NaN | 2022-09-08 00:00:00 | 263.1 | 0.001142 | NaN |
| 2022-10-20 00:00:00 | 70.951355 | -0.010144 | NaN | NaN | NaN | 2022-09-09 00:00:00 | 266.71 | 0.013721 | NaN |
| 2022-10-21 00:00:00 | 71.733681 | 0.011026 | NaN | NaN | NaN | 2022-09-12 00:00:00 | 269.52 | 0.010536 | NaN |
| 2022-10-24 00:00:00 | 71.68766 | -0.000642 | NaN | NaN | NaN | 2022-09-13 00:00:00 | 267.82 | -0.006308 | NaN |
| 2022-10-25 00:00:00 | 72.930161 | 0.017332 | NaN | NaN | NaN | 2022-09-14 00:00:00 | 264.52 | -0.012322 | NaN |
| 2022-10-26 00:00:00 | 73.40876 | 0.006562 | NaN | NaN | NaN | 2022-09-15 00:00:00 | 263.36 | -0.004385 | NaN |
| 2022-10-27 00:00:00 | 73.574425 | 0.002257 | NaN | NaN | NaN | 2022-09-16 00:00:00 | 258.71 | -0.017656 | NaN |
| 2022-10-28 00:00:00 | 73.758507 | 0.002502 | NaN | NaN | NaN | 2022-09-19 00:00:00 | 257.75 | -0.003711 | NaN |
| 2022-10-31 00:00:00 | 72.617249 | -0.015473 | NaN | NaN | NaN | 2022-09-20 00:00:00 | 259.27 | 0.005897 | NaN |
| 2022-11-01 00:00:00 | 74.015617 | 0.019257 | NaN | NaN | NaN | 2022-09-21 00:00:00 | 255.58 | -0.014232 | NaN |
| 2022-11-02 00:00:00 | 73.451447 | -0.007622 | NaN | NaN | NaN | 2022-09-22 00:00:00 | 253.71 | -0.007317 | NaN |
| 2022-11-03 00:00:00 | 73.192497 | -0.003525 | NaN | NaN | NaN | 2022-09-23 00:00:00 | 249.03 | -0.018446 | NaN |
| 2022-11-04 00:00:00 | 74.367058 | 0.016048 | NaN | NaN | NaN | 2022-09-26 00:00:00 | 244.28 | -0.019074 | NaN |
| 2022-11-07 00:00:00 | 74.339302 | -0.000373 | NaN | NaN | NaN | 2022-09-27 00:00:00 | 245.01 | 0.002988 | NaN |
| 2022-11-08 00:00:00 | 74.857224 | 0.006967 | NaN | NaN | NaN | 2022-09-28 00:00:00 | 241.76 | -0.013265 | NaN |
| 2022-11-09 00:00:00 | 73.849129 | -0.013467 | NaN | NaN | NaN | 2022-09-29 00:00:00 | 240.73 | -0.00426 | NaN |
| 2022-11-10 00:00:00 | 77.24334 | 0.045961 | NaN | NaN | NaN | 2022-09-30 00:00:00 | 241.86 | 0.004694 | NaN |
| 2022-11-11 00:00:00 | 77.224838 | -0.00024 | NaN | NaN | NaN | 2022-10-03 00:00:00 | 242.13 | 0.001116 | NaN |
| 2022-11-14 00:00:00 | 76.568199 | -0.008503 | NaN | NaN | NaN | 2022-10-04 00:00:00 | 247.15 | 0.020733 | NaN |
| 2022-11-15 00:00:00 | 78.010956 | 0.018843 | NaN | NaN | NaN | 2022-10-05 00:00:00 | 249.7 | 0.010318 | NaN |
| 2022-11-16 00:00:00 | 78.010956 | 0 | NaN | NaN | NaN | 2022-10-06 00:00:00 | 249.86 | 0.000641 | NaN |
| 2022-11-17 00:00:00 | 77.308052 | -0.00901 | NaN | NaN | NaN | 2022-10-07 00:00:00 | 246.52 | -0.013367 | NaN |
| 2022-11-18 00:00:00 | 77.308052 | 0 | NaN | NaN | NaN | 2022-10-10 00:00:00 | 242.76 | -0.015252 | NaN |
| 2022-11-21 00:00:00 | 77.317322 | 0.00012 | NaN | NaN | NaN | 2022-10-11 00:00:00 | 238.05 | -0.019402 | NaN |
| 2022-11-22 00:00:00 | 78.121941 | 0.010407 | NaN | NaN | NaN | 2022-10-12 00:00:00 | 238.2 | 0.00063 | NaN |
| 2022-11-23 00:00:00 | 78.630592 | 0.006511 | NaN | NaN | NaN | 2022-10-13 00:00:00 | 235.74 | -0.010327 | NaN |
| 2022-11-25 00:00:00 | 78.99131 | 0.004588 | NaN | NaN | NaN | 2022-10-14 00:00:00 | 237.27 | 0.00649 | NaN |
| 2022-11-28 00:00:00 | 78.676842 | -0.003981 | NaN | NaN | NaN | 2022-10-17 00:00:00 | 238.83 | 0.006575 | NaN |
| 2022-11-29 00:00:00 | 79.037521 | 0.004584 | NaN | NaN | NaN | 2022-10-18 00:00:00 | 241.48 | 0.011096 | NaN |
| 2022-11-30 00:00:00 | 79.934647 | 0.011351 | NaN | NaN | NaN | 2022-10-19 00:00:00 | 237.94 | -0.01466 | NaN |
| 2022-12-01 00:00:00 | 81.521439 | 0.019851 | NaN | NaN | NaN | 2022-10-20 00:00:00 | 238.47 | 0.002227 | NaN |
| 2022-12-02 00:00:00 | 81.177895 | -0.004214 | NaN | NaN | NaN | 2022-10-21 00:00:00 | 238.58 | 0.000461 | NaN |
| 2022-12-05 00:00:00 | 79.933708 | -0.015327 | NaN | NaN | NaN | 2022-10-24 00:00:00 | 232.55 | -0.025275 | NaN |
| 2022-12-06 00:00:00 | 79.497314 | -0.005459 | NaN | NaN | NaN | 2022-10-25 00:00:00 | 232.64 | 0.000387 | NaN |
| 2022-12-07 00:00:00 | 80.648643 | 0.014483 | NaN | NaN | NaN | 2022-10-26 00:00:00 | 235.08 | 0.010488 | NaN |
| 2022-12-08 00:00:00 | 80.500092 | -0.001842 | NaN | NaN | NaN | 2022-10-27 00:00:00 | 236.08 | 0.004254 | NaN |
| 2022-12-09 00:00:00 | 79.942993 | -0.00692 | NaN | NaN | NaN | 2022-10-28 00:00:00 | 232.7 | -0.014317 | NaN |
| 2022-12-12 00:00:00 | 80.240112 | 0.003717 | NaN | NaN | NaN | 2022-10-31 00:00:00 | 233.14 | 0.001891 | NaN |
| 2022-12-13 00:00:00 | 81.010765 | 0.009604 | NaN | NaN | NaN | 2022-11-01 00:00:00 | 237.78 | 0.019902 | NaN |
| 2022-12-14 00:00:00 | 80.890053 | -0.00149 | NaN | NaN | NaN | 2022-11-02 00:00:00 | 239.09 | 0.005509 | NaN |
| 2022-12-15 00:00:00 | 80.461266 | -0.005301 | NaN | NaN | NaN | 2022-11-03 00:00:00 | 237.17 | -0.00803 | NaN |
| 2022-12-16 00:00:00 | 80.041824 | -0.005213 | NaN | NaN | NaN | 2022-11-04 00:00:00 | 243.36 | 0.026099 | NaN |
| 2022-12-19 00:00:00 | 79.603722 | -0.005473 | NaN | NaN | NaN | 2022-11-07 00:00:00 | 245.9 | 0.010437 | NaN |
| 2022-12-20 00:00:00 | 79.202904 | -0.005035 | NaN | NaN | NaN | 2022-11-08 00:00:00 | 245.9 | 0 | NaN |
| 2022-12-21 00:00:00 | 80.237572 | 0.013064 | NaN | NaN | NaN | 2022-11-09 00:00:00 | 244.96 | -0.003823 | NaN |
| 2022-12-22 00:00:00 | 79.827461 | -0.005111 | NaN | NaN | NaN | 2022-11-10 00:00:00 | 243.72 | -0.005062 | NaN |
| 2022-12-23 00:00:00 | 79.398636 | -0.005372 | NaN | NaN | NaN | 2022-11-11 00:00:00 | 252.99 | 0.038035 | NaN |
| 2022-12-27 00:00:00 | 78.923256 | -0.005987 | NaN | NaN | NaN | 2022-11-14 00:00:00 | 254.5 | 0.005969 | NaN |
| 2022-12-28 00:00:00 | 78.634315 | -0.003661 | NaN | NaN | NaN | 2022-11-15 00:00:00 | 259.58 | 0.019961 | NaN |
| 2022-12-29 00:00:00 | 79.240189 | 0.007705 | NaN | NaN | NaN | 2022-11-16 00:00:00 | 257.61 | -0.007589 | NaN |
| 2022-12-30 00:00:00 | 78.848686 | -0.004941 | NaN | NaN | NaN | 2022-11-17 00:00:00 | 255.93 | -0.006521 | NaN |
| 2023-01-03 00:00:00 | 79.193588 | 0.004374 | NaN | NaN | NaN | 2022-11-18 00:00:00 | 255.38 | -0.002149 | NaN |
| 2023-01-04 00:00:00 | 80.162987 | 0.012241 | NaN | NaN | NaN | 2022-11-21 00:00:00 | 252.71 | -0.010455 | NaN |
| 2023-01-05 00:00:00 | 79.435944 | -0.00907 | NaN | NaN | NaN | 2022-11-22 00:00:00 | 252.28 | -0.001702 | NaN |
| 2023-01-06 00:00:00 | 80.843445 | 0.017719 | NaN | NaN | NaN | 2022-11-23 00:00:00 | 253.28 | 0.003964 | NaN |
| 2023-01-09 00:00:00 | 80.684998 | -0.00196 | NaN | NaN | NaN | 2022-11-24 00:00:00 | 256.19 | 0.011489 | NaN |
| 2023-01-10 00:00:00 | 80.181618 | -0.006239 | NaN | NaN | NaN | 2022-11-25 00:00:00 | 254.73 | -0.005699 | NaN |
| 2023-01-11 00:00:00 | 81.095116 | 0.011393 | NaN | NaN | NaN | 2022-11-28 00:00:00 | 253.35 | -0.005418 | NaN |
| 2023-01-12 00:00:00 | 82.055229 | 0.011839 | NaN | NaN | NaN | 2022-11-29 00:00:00 | 258.19 | 0.019104 | NaN |
| 2023-01-13 00:00:00 | 81.859459 | -0.002386 | NaN | NaN | NaN | 2022-11-30 00:00:00 | 263.56 | 0.020799 | NaN |
| 2023-01-17 00:00:00 | 81.943367 | 0.001025 | NaN | NaN | NaN | 2022-12-01 00:00:00 | 264.58 | 0.00387 | NaN |
| 2023-01-18 00:00:00 | 82.912766 | 0.01183 | NaN | NaN | NaN | 2022-12-02 00:00:00 | 264.84 | 0.000983 | NaN |
| 2023-01-19 00:00:00 | 82.679733 | -0.002811 | NaN | NaN | NaN | 2022-12-05 00:00:00 | 266.39 | 0.005853 | NaN |
| 2023-01-20 00:00:00 | 82.493332 | -0.002254 | NaN | NaN | NaN | 2022-12-06 00:00:00 | 264.55 | -0.006907 | NaN |
| 2023-01-23 00:00:00 | 82.446716 | -0.000565 | NaN | NaN | NaN | 2022-12-07 00:00:00 | 261.37 | -0.01202 | NaN |
| 2023-01-24 00:00:00 | 82.810234 | 0.004409 | NaN | NaN | NaN | 2022-12-08 00:00:00 | 264.12 | 0.010521 | NaN |
| 2023-01-25 00:00:00 | 82.754311 | -0.000675 | NaN | NaN | NaN | 2022-12-09 00:00:00 | 265 | 0.003332 | NaN |
| 2023-01-26 00:00:00 | 82.754311 | 0 | NaN | NaN | NaN | 2022-12-12 00:00:00 | 261.68 | -0.012528 | NaN |
| 2023-01-27 00:00:00 | 82.595856 | -0.001915 | NaN | NaN | NaN | 2022-12-13 00:00:00 | 262.49 | 0.003095 | NaN |
| 2023-01-30 00:00:00 | 81.542542 | -0.012753 | NaN | NaN | NaN | 2022-12-14 00:00:00 | 264.1 | 0.006134 | NaN |
| 2023-01-31 00:00:00 | 81.943367 | 0.004916 | NaN | NaN | NaN | 2022-12-15 00:00:00 | 260.86 | -0.012268 | NaN |
| 2023-02-01 00:00:00 | 83.49807 | 0.018973 | NaN | NaN | NaN | 2022-12-16 00:00:00 | 259.95 | -0.003488 | NaN |
| 2023-02-02 00:00:00 | 83.769363 | 0.003249 | NaN | NaN | NaN | 2022-12-19 00:00:00 | 259.83 | -0.000462 | NaN |
| 2023-02-03 00:00:00 | 82.618752 | -0.013735 | NaN | NaN | NaN | 2022-12-20 00:00:00 | 258.15 | -0.006466 | NaN |
| 2023-02-06 00:00:00 | 81.449432 | -0.014153 | NaN | NaN | NaN | 2022-12-21 00:00:00 | 258.75 | 0.002324 | NaN |
| 2023-02-07 00:00:00 | 81.524277 | 0.000919 | NaN | NaN | NaN | 2022-12-22 00:00:00 | 260.16 | 0.005449 | NaN |
| 2023-02-08 00:00:00 | 81.477516 | -0.000574 | NaN | NaN | NaN | 2022-12-23 00:00:00 | 258.07 | -0.008034 | NaN |
| 2023-02-09 00:00:00 | 80.94429 | -0.006544 | NaN | NaN | NaN | 2022-12-26 00:00:00 | 258.76 | 0.002674 | NaN |
| 2023-02-10 00:00:00 | 80.317551 | -0.007743 | NaN | NaN | NaN | 2022-12-27 00:00:00 | 259.57 | 0.00313 | NaN |
| 2023-02-13 00:00:00 | 80.542068 | 0.002795 | NaN | NaN | NaN | 2022-12-28 00:00:00 | 259.97 | 0.001541 | NaN |
| 2023-02-14 00:00:00 | 80.588829 | 0.000581 | NaN | NaN | NaN | 2022-12-29 00:00:00 | 260.64 | 0.002577 | NaN |
| 2023-02-15 00:00:00 | 80.354965 | -0.002902 | NaN | NaN | NaN | 2022-12-30 00:00:00 | 260.42 | -0.000844 | NaN |
| 2023-02-16 00:00:00 | 79.831123 | -0.006519 | NaN | NaN | NaN | 2023-01-02 00:00:00 | 260.49 | 0.000269 | NaN |
| 2023-02-17 00:00:00 | 79.859177 | 0.000351 | NaN | NaN | NaN | 2023-01-03 00:00:00 | 262.48 | 0.007639 | NaN |
| 2023-02-21 00:00:00 | 78.652443 | -0.015111 | NaN | NaN | NaN | 2023-01-04 00:00:00 | 265.35 | 0.010934 | NaN |
| 2023-02-22 00:00:00 | 78.961151 | 0.003925 | NaN | NaN | NaN | 2023-01-05 00:00:00 | 267.16 | 0.006821 | NaN |
| 2023-02-23 00:00:00 | 80.224007 | 0.015993 | NaN | NaN | NaN | 2023-01-06 00:00:00 | 268.1 | 0.003518 | NaN |
| 2023-02-24 00:00:00 | 79.672089 | -0.00688 | NaN | NaN | NaN | 2023-01-09 00:00:00 | 272.96 | 0.018128 | NaN |
| 2023-02-27 00:00:00 | 80.074348 | 0.005049 | NaN | NaN | NaN | 2023-01-10 00:00:00 | 273.58 | 0.002271 | NaN |
| 2023-02-28 00:00:00 | 79.737564 | -0.004206 | NaN | NaN | NaN | 2023-01-11 00:00:00 | 274.13 | 0.00201 | NaN |
| 2023-03-01 00:00:00 | 79.210434 | -0.006611 | NaN | NaN | NaN | 2023-01-12 00:00:00 | 274.59 | 0.001678 | NaN |
| 2023-03-02 00:00:00 | 78.919174 | -0.003677 | NaN | NaN | NaN | 2023-01-13 00:00:00 | 277.44 | 0.010379 | NaN |
| 2023-03-03 00:00:00 | 80.131271 | 0.015359 | NaN | NaN | NaN | 2023-01-16 00:00:00 | 277.59 | 0.000541 | NaN |
| 2023-03-06 00:00:00 | 79.811798 | -0.003987 | NaN | NaN | NaN | 2023-01-17 00:00:00 | 276.54 | -0.003783 | NaN |
| 2023-03-07 00:00:00 | 79.482925 | -0.004121 | NaN | NaN | NaN | 2023-01-18 00:00:00 | 277.35 | 0.002929 | NaN |
| 2023-03-08 00:00:00 | 79.107086 | -0.004729 | NaN | NaN | NaN | 2023-01-19 00:00:00 | 277.03 | -0.001154 | NaN |
| 2023-03-09 00:00:00 | 79.125877 | 0.000238 | NaN | NaN | NaN | 2023-01-20 00:00:00 | 279.04 | 0.007256 | NaN |
| 2023-03-10 00:00:00 | 79.868172 | 0.009381 | NaN | NaN | NaN | 2023-01-23 00:00:00 | 279.8 | 0.002724 | NaN |
| 2023-03-13 00:00:00 | 79.736633 | -0.001647 | NaN | NaN | NaN | 2023-01-24 00:00:00 | 279.85 | 0.000179 | NaN |
| 2023-03-14 00:00:00 | 79.520515 | -0.00271 | NaN | NaN | NaN | 2023-01-25 00:00:00 | 279.63 | -0.000786 | NaN |
| 2023-03-15 00:00:00 | 79.811798 | 0.003663 | NaN | NaN | NaN | 2023-01-26 00:00:00 | 281.96 | 0.008332 | NaN |
| 2023-03-16 00:00:00 | 79.473541 | -0.004238 | NaN | NaN | NaN | 2023-01-27 00:00:00 | 280.89 | -0.003795 | NaN |
| 2023-03-17 00:00:00 | 79.116478 | -0.004493 | NaN | NaN | NaN | 2023-01-30 00:00:00 | 279.37 | -0.005411 | NaN |
| 2023-03-20 00:00:00 | 79.125877 | 0.000119 | NaN | NaN | NaN | 2023-01-31 00:00:00 | 277.65 | -0.006157 | NaN |
| 2023-03-21 00:00:00 | 79.689644 | 0.007125 | NaN | NaN | NaN | 2023-02-01 00:00:00 | 280.16 | 0.00904 | NaN |
| 2023-03-22 00:00:00 | 80.384979 | 0.008726 | NaN | NaN | NaN | 2023-02-02 00:00:00 | 280.39 | 0.000821 | NaN |
| 2023-03-23 00:00:00 | 80.676262 | 0.003624 | NaN | NaN | NaN | 2023-02-03 00:00:00 | 278.47 | -0.006848 | NaN |
| 2023-03-24 00:00:00 | 80.23465 | -0.005474 | NaN | NaN | NaN | 2023-02-06 00:00:00 | 273.5 | -0.017848 | NaN |
| 2023-03-27 00:00:00 | 79.896362 | -0.004216 | NaN | NaN | NaN | 2023-02-07 00:00:00 | 273.51 | 0.000037 | NaN |
| 2023-03-28 00:00:00 | 79.614487 | -0.003528 | NaN | NaN | NaN | 2023-02-08 00:00:00 | 274.32 | 0.002962 | NaN |
| 2023-03-29 00:00:00 | 79.999725 | 0.004839 | NaN | NaN | NaN | 2023-02-09 00:00:00 | 275.18 | 0.003135 | NaN |
| 2023-03-30 00:00:00 | 80.554115 | 0.00693 | NaN | NaN | NaN | 2023-02-10 00:00:00 | 272.36 | -0.010248 | NaN |
| 2023-03-31 00:00:00 | 81.070908 | 0.006415 | NaN | NaN | NaN | 2023-02-13 00:00:00 | 273.02 | 0.002423 | NaN |
| 2023-04-03 00:00:00 | 81.374733 | 0.003748 | NaN | NaN | NaN | 2023-02-14 00:00:00 | 273 | -0.000073 | NaN |
| 2023-04-04 00:00:00 | 81.487961 | 0.001391 | NaN | NaN | NaN | 2023-02-15 00:00:00 | 271.49 | -0.005531 | NaN |
| 2023-04-05 00:00:00 | 81.318123 | -0.002084 | NaN | NaN | NaN | 2023-02-16 00:00:00 | 272.37 | 0.003241 | NaN |
| 2023-04-06 00:00:00 | 81.2332 | -0.001044 | NaN | NaN | NaN | 2023-02-17 00:00:00 | 269.87 | -0.009179 | NaN |
| 2023-04-10 00:00:00 | 80.808594 | -0.005227 | NaN | NaN | NaN | 2023-02-20 00:00:00 | 271.38 | 0.005595 | NaN |
| 2023-04-11 00:00:00 | 80.893509 | 0.001051 | NaN | NaN | NaN | 2023-02-21 00:00:00 | 268.9 | -0.009138 | NaN |
| 2023-04-12 00:00:00 | 81.12941 | 0.002916 | NaN | NaN | NaN | 2023-02-22 00:00:00 | 266.1 | -0.010413 | NaN |
| 2023-04-13 00:00:00 | 81.214317 | 0.001047 | NaN | NaN | NaN | 2023-02-23 00:00:00 | 266.82 | 0.002706 | NaN |
| 2023-04-14 00:00:00 | 81.044479 | -0.002091 | NaN | NaN | NaN | 2023-02-24 00:00:00 | 263.04 | -0.014167 | NaN |
| 2023-04-17 00:00:00 | 80.52552 | -0.006403 | NaN | NaN | NaN | 2023-02-27 00:00:00 | 262.44 | -0.002281 | NaN |
| 2023-04-18 00:00:00 | 80.50663 | -0.000235 | NaN | NaN | NaN | 2023-02-28 00:00:00 | 261.96 | -0.001829 | NaN |
| 2023-04-19 00:00:00 | 80.119781 | -0.004805 | NaN | NaN | NaN | 2023-03-01 00:00:00 | 266.91 | 0.018896 | NaN |
| 2023-04-20 00:00:00 | 80.025414 | -0.001178 | NaN | NaN | NaN | 2023-03-02 00:00:00 | 266.11 | -0.002997 | NaN |
| 2023-04-21 00:00:00 | 80.034859 | 0.000118 | NaN | NaN | NaN | 2023-03-03 00:00:00 | 268.01 | 0.00714 | NaN |
| 2023-04-24 00:00:00 | 80.251869 | 0.002711 | NaN | NaN | NaN | 2023-03-06 00:00:00 | 269.11 | 0.004104 | NaN |
| 2023-04-25 00:00:00 | 80.742531 | 0.006114 | NaN | NaN | NaN | 2023-03-07 00:00:00 | 267.35 | -0.00654 | NaN |
| 2023-04-26 00:00:00 | 80.52552 | -0.002688 | NaN | NaN | NaN | 2023-03-08 00:00:00 | 266.03 | -0.004937 | NaN |
| 2023-04-27 00:00:00 | 80.54438 | 0.000234 | NaN | NaN | NaN | 2023-03-09 00:00:00 | 263.09 | -0.011051 | NaN |
| 2023-04-28 00:00:00 | 81.28981 | 0.009255 | NaN | NaN | NaN | 2023-03-10 00:00:00 | 260.03 | -0.011631 | NaN |
| 2023-05-01 00:00:00 | 80.484482 | -0.009907 | NaN | NaN | NaN | 2023-03-13 00:00:00 | 260.31 | 0.001077 | NaN |
| 2023-05-02 00:00:00 | 80.825569 | 0.004238 | NaN | NaN | NaN | 2023-03-14 00:00:00 | 257.08 | -0.012408 | NaN |
| 2023-05-03 00:00:00 | 81.081367 | 0.003165 | NaN | NaN | NaN | 2023-03-15 00:00:00 | 256.34 | -0.002878 | NaN |
| 2023-05-04 00:00:00 | 80.673973 | -0.005025 | NaN | NaN | NaN | 2023-03-16 00:00:00 | 255.29 | -0.004096 | NaN |
| 2023-05-05 00:00:00 | 80.901375 | 0.002819 | NaN | NaN | NaN | 2023-03-17 00:00:00 | 257.3 | 0.007873 | NaN |
| 2023-05-08 00:00:00 | 80.579231 | -0.003982 | NaN | NaN | NaN | 2023-03-20 00:00:00 | 255.27 | -0.00789 | NaN |
| 2023-05-09 00:00:00 | 80.541344 | -0.00047 | NaN | NaN | NaN | 2023-03-21 00:00:00 | 257.87 | 0.010185 | NaN |
| 2023-05-10 00:00:00 | 80.986633 | 0.005529 | NaN | NaN | NaN | 2023-03-22 00:00:00 | 259.75 | 0.00729 | NaN |
| 2023-05-11 00:00:00 | 81.242439 | 0.003159 | NaN | NaN | NaN | 2023-03-23 00:00:00 | 263.1 | 0.012897 | NaN |
| 2023-05-12 00:00:00 | 80.730835 | -0.006297 | NaN | NaN | NaN | 2023-03-24 00:00:00 | 262.02 | -0.004105 | NaN |
| 2023-05-15 00:00:00 | 80.380272 | -0.004342 | NaN | NaN | NaN | 2023-03-27 00:00:00 | 260.29 | -0.006603 | NaN |
| 2023-05-16 00:00:00 | 80.067627 | -0.00389 | NaN | NaN | NaN | 2023-03-28 00:00:00 | 261.61 | 0.005071 | NaN |
| 2023-05-17 00:00:00 | 80.07708 | 0.000118 | NaN | NaN | NaN | 2023-03-29 00:00:00 | 264.2 | 0.0099 | NaN |
| 2023-05-18 00:00:00 | 79.754967 | -0.004023 | NaN | NaN | NaN | 2023-03-30 00:00:00 | 265.65 | 0.005488 | NaN |
| 2023-05-19 00:00:00 | 79.745483 | -0.000119 | NaN | NaN | NaN | 2023-03-31 00:00:00 | 266.8 | 0.004329 | NaN |
| 2023-05-22 00:00:00 | 79.736031 | -0.000119 | NaN | NaN | NaN | 2023-04-03 00:00:00 | 267.08 | 0.001049 | NaN |
| 2023-05-23 00:00:00 | 79.830757 | 0.001188 | NaN | NaN | NaN | 2023-04-04 00:00:00 | 266.65 | -0.00161 | NaN |
| 2023-05-24 00:00:00 | 79.698135 | -0.001661 | NaN | NaN | NaN | 2023-04-05 00:00:00 | 266.48 | -0.000638 | NaN |
| 2023-05-25 00:00:00 | 79.489685 | -0.002615 | NaN | NaN | NaN | 2023-04-06 00:00:00 | 266.43 | -0.000188 | NaN |
| 2023-05-26 00:00:00 | 79.821281 | 0.004172 | NaN | NaN | NaN | 2023-04-07 00:00:00 | 266.53 | 0.000375 | NaN |
| 2023-05-30 00:00:00 | 80.42765 | 0.007597 | NaN | NaN | NaN | 2023-04-10 00:00:00 | 266.7 | 0.000638 | NaN |
| 2023-05-31 00:00:00 | 80.323418 | -0.001296 | NaN | NaN | NaN | 2023-04-11 00:00:00 | 268.79 | 0.007837 | NaN |
| 2023-06-01 00:00:00 | 80.859062 | 0.006669 | NaN | NaN | NaN | 2023-04-12 00:00:00 | 268.49 | -0.001116 | NaN |
| 2023-06-02 00:00:00 | 80.735382 | -0.00153 | NaN | NaN | NaN | 2023-04-13 00:00:00 | 269.14 | 0.002421 | NaN |
| 2023-06-05 00:00:00 | 81.00177 | 0.0033 | NaN | NaN | NaN | 2023-04-14 00:00:00 | 269.76 | 0.002304 | NaN |
| 2023-06-06 00:00:00 | 81.144493 | 0.001762 | NaN | NaN | NaN | 2023-04-17 00:00:00 | 270.72 | 0.003559 | NaN |
| 2023-06-07 00:00:00 | 80.668777 | -0.005863 | NaN | NaN | NaN | 2023-04-18 00:00:00 | 270.08 | -0.002364 | NaN |
| 2023-06-08 00:00:00 | 81.125458 | 0.005661 | NaN | NaN | NaN | 2023-04-19 00:00:00 | 267.46 | -0.009701 | NaN |
| 2023-06-09 00:00:00 | 81.030327 | -0.001173 | NaN | NaN | NaN | 2023-04-20 00:00:00 | 267.21 | -0.000935 | NaN |
| 2023-06-12 00:00:00 | 81.477478 | 0.005518 | NaN | NaN | NaN | 2023-04-21 00:00:00 | 264.67 | -0.009506 | NaN |
| 2023-06-13 00:00:00 | 81.35379 | -0.001518 | NaN | NaN | NaN | 2023-04-24 00:00:00 | 264.33 | -0.001285 | NaN |
| 2023-06-14 00:00:00 | 81.525055 | 0.002105 | NaN | NaN | NaN | 2023-04-25 00:00:00 | 261.2 | -0.011841 | NaN |
| 2023-06-15 00:00:00 | 81.943665 | 0.005135 | NaN | NaN | NaN | 2023-04-26 00:00:00 | 262.14 | 0.003599 | NaN |
| 2023-06-16 00:00:00 | 81.620186 | -0.003948 | NaN | NaN | NaN | 2023-04-27 00:00:00 | 263.25 | 0.004234 | NaN |
| 2023-06-20 00:00:00 | 81.658234 | 0.000466 | NaN | NaN | NaN | 2023-04-28 00:00:00 | 264.77 | 0.005774 | NaN |
| 2023-06-21 00:00:00 | 82.086357 | 0.005243 | NaN | NaN | NaN | 2023-05-01 00:00:00 | 264.69 | -0.000302 | NaN |
| 2023-06-22 00:00:00 | 81.772415 | -0.003825 | NaN | NaN | NaN | 2023-05-02 00:00:00 | 263.9 | -0.002985 | NaN |
| 2023-06-23 00:00:00 | 81.867538 | 0.001163 | NaN | NaN | NaN | 2023-05-03 00:00:00 | 263.07 | -0.003145 | NaN |
| 2023-06-26 00:00:00 | 82.12442 | 0.003138 | NaN | NaN | NaN | 2023-05-04 00:00:00 | 264.75 | 0.006386 | NaN |
| 2023-06-27 00:00:00 | 82.12442 | 0 | NaN | NaN | NaN | 2023-05-05 00:00:00 | 265.84 | 0.004117 | NaN |
| 2023-06-28 00:00:00 | 82.181503 | 0.000695 | NaN | NaN | NaN | 2023-05-08 00:00:00 | 267.91 | 0.007787 | NaN |
| 2023-06-29 00:00:00 | 81.743851 | -0.005325 | NaN | NaN | NaN | 2023-05-09 00:00:00 | 265.78 | -0.00795 | NaN |
| 2023-06-30 00:00:00 | 82.333733 | 0.007216 | NaN | NaN | NaN | 2023-05-10 00:00:00 | 265.53 | -0.000941 | NaN |
| 2023-07-03 00:00:00 | 82.492294 | 0.001926 | NaN | NaN | NaN | 2023-05-11 00:00:00 | 265.05 | -0.001808 | NaN |
| 2023-07-05 00:00:00 | 82.071991 | -0.005095 | NaN | NaN | NaN | 2023-05-12 00:00:00 | 264.03 | -0.003848 | NaN |
| 2023-07-06 00:00:00 | 80.897079 | -0.014316 | NaN | NaN | NaN | 2023-05-15 00:00:00 | 265.19 | 0.004393 | NaN |
| 2023-07-07 00:00:00 | 80.801552 | -0.001181 | NaN | NaN | NaN | 2023-05-16 00:00:00 | 265.34 | 0.000566 | NaN |
| 2023-07-10 00:00:00 | 81.145424 | 0.004256 | NaN | NaN | NaN | 2023-05-17 00:00:00 | 264.23 | -0.004183 | NaN |
| 2023-07-11 00:00:00 | 81.66127 | 0.006357 | NaN | NaN | NaN | 2023-05-18 00:00:00 | 264.45 | 0.000833 | NaN |
| 2023-07-12 00:00:00 | 82.635574 | 0.011931 | NaN | NaN | NaN | 2023-05-19 00:00:00 | 263.67 | -0.00295 | NaN |
| 2023-07-13 00:00:00 | 83.533478 | 0.010866 | NaN | NaN | NaN | 2023-05-22 00:00:00 | 264.95 | 0.004855 | NaN |
| 2023-07-14 00:00:00 | 83.046303 | -0.005832 | NaN | NaN | NaN | 2023-05-23 00:00:00 | 263.52 | -0.005397 | NaN |
| 2023-07-17 00:00:00 | 83.170502 | 0.001496 | NaN | NaN | NaN | 2023-05-24 00:00:00 | 261.59 | -0.007324 | NaN |
| 2023-07-18 00:00:00 | 83.581245 | 0.004939 | NaN | NaN | NaN | 2023-05-25 00:00:00 | 259.92 | -0.006384 | NaN |
| 2023-07-19 00:00:00 | 83.352013 | -0.002743 | NaN | NaN | NaN | 2023-05-26 00:00:00 | 261.86 | 0.007464 | NaN |
| 2023-07-20 00:00:00 | 82.845726 | -0.006074 | NaN | NaN | NaN | 2023-05-29 00:00:00 | 261.94 | 0.000306 | NaN |
| 2023-07-21 00:00:00 | 83.10363 | 0.003113 | NaN | NaN | NaN | 2023-05-30 00:00:00 | 261.22 | -0.002749 | NaN |
| 2023-07-24 00:00:00 | 83.266022 | 0.001954 | NaN | NaN | NaN | 2023-05-31 00:00:00 | 258.61 | -0.009992 | NaN |
| 2023-07-25 00:00:00 | 83.16095 | -0.001262 | NaN | NaN | NaN | 2023-06-01 00:00:00 | 259.74 | 0.00437 | NaN |
| 2023-07-26 00:00:00 | 83.428391 | 0.003216 | NaN | NaN | NaN | 2023-06-02 00:00:00 | 264.87 | 0.019751 | NaN |
| 2023-07-27 00:00:00 | 82.635574 | -0.009503 | NaN | NaN | NaN | 2023-06-05 00:00:00 | 265.62 | 0.002832 | NaN |
| 2023-07-28 00:00:00 | 83.638542 | 0.012137 | NaN | NaN | NaN | 2023-06-06 00:00:00 | 265.96 | 0.00128 | NaN |
| 2023-07-31 00:00:00 | 83.753189 | 0.001371 | NaN | NaN | NaN | 2023-06-07 00:00:00 | 267.9 | 0.007294 | NaN |
| 2023-08-01 00:00:00 | 82.916916 | -0.009985 | NaN | NaN | NaN | 2023-06-08 00:00:00 | 267.49 | -0.00153 | NaN |
| 2023-08-02 00:00:00 | 82.322319 | -0.007171 | NaN | NaN | NaN | 2023-06-09 00:00:00 | 269.1 | 0.006019 | NaN |
| 2023-08-03 00:00:00 | 81.622231 | -0.008504 | NaN | NaN | NaN | 2023-06-12 00:00:00 | 269.38 | 0.001041 | NaN |
| 2023-08-04 00:00:00 | 82.705925 | 0.013277 | NaN | NaN | NaN | 2023-06-13 00:00:00 | 271.41 | 0.007536 | NaN |
| 2023-08-07 00:00:00 | 82.437401 | -0.003247 | NaN | NaN | NaN | 2023-06-14 00:00:00 | 272.49 | 0.003979 | NaN |
| 2023-08-08 00:00:00 | 82.648376 | 0.002559 | NaN | NaN | NaN | 2023-06-15 00:00:00 | 274.97 | 0.009101 | NaN |
| 2023-08-09 00:00:00 | 82.821007 | 0.002089 | NaN | NaN | NaN | 2023-06-16 00:00:00 | 276.52 | 0.005637 | NaN |
| 2023-08-10 00:00:00 | 82.504532 | -0.003821 | NaN | NaN | NaN | 2023-06-19 00:00:00 | 275.3 | -0.004412 | NaN |
| 2023-08-11 00:00:00 | 82.312729 | -0.002325 | NaN | NaN | NaN | 2023-06-20 00:00:00 | 272.67 | -0.009553 | NaN |
| 2023-08-14 00:00:00 | 81.650993 | -0.008039 | NaN | NaN | NaN | 2023-06-21 00:00:00 | 271.08 | -0.005831 | NaN |
| 2023-08-15 00:00:00 | 80.96051 | -0.008457 | NaN | NaN | NaN | 2023-06-22 00:00:00 | 270 | -0.003984 | NaN |
| 2023-08-16 00:00:00 | 80.80706 | -0.001895 | NaN | NaN | NaN | 2023-06-23 00:00:00 | 267.77 | -0.008259 | NaN |
| 2023-08-17 00:00:00 | 80.739929 | -0.000831 | NaN | NaN | NaN | 2023-06-26 00:00:00 | 266.78 | -0.003697 | NaN |
| 2023-08-18 00:00:00 | 80.720757 | -0.000237 | NaN | NaN | NaN | 2023-06-27 00:00:00 | 268.27 | 0.005585 | NaN |
| 2023-08-21 00:00:00 | 80.317978 | -0.00499 | NaN | NaN | NaN | 2023-06-28 00:00:00 | 267.87 | -0.001491 | NaN |
| 2023-08-22 00:00:00 | 80.538551 | 0.002746 | NaN | NaN | NaN | 2023-06-29 00:00:00 | 267.24 | -0.002352 | NaN |
| 2023-08-23 00:00:00 | 81.833214 | 0.016075 | NaN | NaN | NaN | 2023-06-30 00:00:00 | 268.13 | 0.00333 | NaN |
| 2023-08-24 00:00:00 | 81.276985 | -0.006797 | NaN | NaN | NaN | 2023-07-03 00:00:00 | 271.83 | 0.013799 | NaN |
| 2023-08-25 00:00:00 | 81.401657 | 0.001534 | NaN | NaN | NaN | 2023-07-04 00:00:00 | 272.62 | 0.002906 | NaN |
| 2023-08-28 00:00:00 | 81.660583 | 0.003181 | NaN | NaN | NaN | 2023-07-05 00:00:00 | 270.79 | -0.006713 | NaN |
| 2023-08-29 00:00:00 | 82.504532 | 0.010335 | NaN | NaN | NaN | 2023-07-06 00:00:00 | 266.88 | -0.014439 | NaN |
| 2023-08-30 00:00:00 | 82.283943 | -0.002674 | NaN | NaN | NaN | 2023-07-07 00:00:00 | 266.27 | -0.002286 | NaN |
| 2023-08-31 00:00:00 | 82.207222 | -0.000932 | NaN | NaN | NaN | 2023-07-10 00:00:00 | 266.65 | 0.001427 | NaN |
| 2023-09-01 00:00:00 | 82.004021 | -0.002472 | NaN | NaN | NaN | 2023-07-11 00:00:00 | 269.35 | 0.010126 | NaN |
| 2023-09-05 00:00:00 | 81.204704 | -0.009747 | NaN | NaN | NaN | 2023-07-12 00:00:00 | 271.79 | 0.009059 | NaN |
| 2023-09-06 00:00:00 | 81.079491 | -0.001542 | NaN | NaN | NaN | 2023-07-13 00:00:00 | 275.27 | 0.012804 | NaN |
| 2023-09-07 00:00:00 | 81.512863 | 0.005345 | NaN | NaN | NaN | 2023-07-14 00:00:00 | 276.8 | 0.005558 | NaN |
| 2023-09-08 00:00:00 | 81.580292 | 0.000827 | NaN | NaN | NaN | 2023-07-17 00:00:00 | 277.06 | 0.000939 | NaN |
| 2023-09-11 00:00:00 | 81.455086 | -0.001535 | NaN | NaN | NaN | 2023-07-18 00:00:00 | 275.45 | -0.005811 | NaN |
| 2023-09-12 00:00:00 | 81.512863 | 0.000709 | NaN | NaN | NaN | 2023-07-19 00:00:00 | 274.85 | -0.002178 | NaN |
| 2023-09-13 00:00:00 | 81.56102 | 0.000591 | NaN | NaN | NaN | 2023-07-20 00:00:00 | 274.93 | 0.000291 | NaN |
| 2023-09-14 00:00:00 | 81.589928 | 0.000354 | NaN | NaN | NaN | 2023-07-21 00:00:00 | 274.46 | -0.00171 | NaN |
| 2023-09-15 00:00:00 | 81.320259 | -0.003305 | NaN | NaN | NaN | 2023-07-24 00:00:00 | 273.87 | -0.00215 | NaN |
| 2023-09-18 00:00:00 | 81.368416 | 0.000592 | NaN | NaN | NaN | 2023-07-25 00:00:00 | 278.67 | 0.017527 | NaN |
| 2023-09-19 00:00:00 | 81.272102 | -0.001184 | NaN | NaN | NaN | 2023-07-26 00:00:00 | 278.96 | 0.001041 | NaN |
| 2023-09-20 00:00:00 | 81.204704 | -0.000829 | NaN | NaN | NaN | 2023-07-27 00:00:00 | 279.7 | 0.002653 | NaN |
| 2023-09-21 00:00:00 | 80.386093 | -0.010081 | NaN | NaN | NaN | 2023-07-28 00:00:00 | 281.96 | 0.00808 | NaN |
| 2023-09-22 00:00:00 | 80.713531 | 0.004073 | NaN | NaN | NaN | 2023-07-31 00:00:00 | 283.04 | 0.00383 | NaN |
| 2023-09-25 00:00:00 | 80.251274 | -0.005727 | NaN | NaN | NaN | 2023-08-01 00:00:00 | 281.66 | -0.004876 | NaN |
| 2023-09-26 00:00:00 | 79.721588 | -0.0066 | NaN | NaN | NaN | 2023-08-02 00:00:00 | 276.19 | -0.019421 | NaN |
| 2023-09-27 00:00:00 | 79.374886 | -0.004349 | NaN | NaN | NaN | 2023-08-03 00:00:00 | 275.31 | -0.003186 | NaN |
| 2023-09-28 00:00:00 | 79.557869 | 0.002305 | NaN | NaN | NaN | 2023-08-04 00:00:00 | 276.54 | 0.004468 | NaN |
| 2023-09-29 00:00:00 | 79.471199 | -0.001089 | NaN | NaN | NaN | 2023-08-07 00:00:00 | 276.24 | -0.001085 | NaN |
| 2023-10-02 00:00:00 | 78.603622 | -0.010917 | NaN | NaN | NaN | 2023-08-08 00:00:00 | 273.3 | -0.010643 | NaN |
| 2023-10-03 00:00:00 | 77.723503 | -0.011197 | NaN | NaN | NaN | 2023-08-09 00:00:00 | 274.14 | 0.003074 | NaN |
| 2023-10-04 00:00:00 | 78.091026 | 0.004729 | NaN | NaN | NaN | 2023-08-10 00:00:00 | 274.06 | -0.000292 | NaN |
| 2023-10-05 00:00:00 | 78.062004 | -0.000372 | NaN | NaN | NaN | 2023-08-11 00:00:00 | 271.55 | -0.009159 | NaN |
| 2023-10-06 00:00:00 | 78.091026 | 0.000372 | NaN | NaN | NaN | 2023-08-14 00:00:00 | 268.61 | -0.010827 | NaN |
| 2023-10-09 00:00:00 | 78.477898 | 0.004954 | NaN | NaN | NaN | 2023-08-15 00:00:00 | 267.47 | -0.004244 | NaN |
| 2023-10-10 00:00:00 | 78.603622 | 0.001602 | NaN | NaN | NaN | 2023-08-16 00:00:00 | 266.51 | -0.003589 | NaN |
| 2023-10-11 00:00:00 | 79.241982 | 0.008121 | NaN | NaN | NaN | 2023-08-17 00:00:00 | 266.16 | -0.001313 | NaN |
| 2023-10-12 00:00:00 | 78.410194 | -0.010497 | NaN | NaN | NaN | 2023-08-18 00:00:00 | 263.7 | -0.009243 | NaN |
| 2023-10-13 00:00:00 | 78.63266 | 0.002837 | NaN | NaN | NaN | 2023-08-21 00:00:00 | 262.63 | -0.004058 | NaN |
| 2023-10-16 00:00:00 | 78.545601 | -0.001107 | NaN | NaN | NaN | 2023-08-22 00:00:00 | 264.44 | 0.006892 | NaN |
| 2023-10-17 00:00:00 | 78.168396 | -0.004802 | NaN | NaN | NaN | 2023-08-23 00:00:00 | 265.56 | 0.004235 | NaN |
| 2023-10-18 00:00:00 | 77.665459 | -0.006434 | NaN | NaN | NaN | 2023-08-24 00:00:00 | 267.78 | 0.00836 | NaN |
| 2023-10-19 00:00:00 | 77.09481 | -0.007348 | NaN | NaN | NaN | 2023-08-25 00:00:00 | 265.19 | -0.009672 | NaN |
| 2023-10-20 00:00:00 | 77.520378 | 0.00552 | NaN | NaN | NaN | 2023-08-28 00:00:00 | 266.92 | 0.006524 | NaN |
| 2023-10-23 00:00:00 | 77.965286 | 0.005739 | NaN | NaN | NaN | 2023-08-29 00:00:00 | 269.68 | 0.01034 | NaN |
| 2023-10-24 00:00:00 | 78.584274 | 0.007939 | NaN | NaN | NaN | 2023-08-30 00:00:00 | 269.99 | 0.00115 | NaN |
| 2023-10-25 00:00:00 | 77.994293 | -0.007508 | NaN | NaN | NaN | 2023-08-31 00:00:00 | 267.94 | -0.007593 | NaN |
| 2023-10-26 00:00:00 | 78.303802 | 0.003968 | NaN | NaN | NaN | 2023-09-01 00:00:00 | 269.08 | 0.004255 | NaN |
| 2023-10-27 00:00:00 | 78.342484 | 0.000494 | NaN | NaN | NaN | 2023-09-04 00:00:00 | 271.71 | 0.009774 | NaN |
| 2023-10-30 00:00:00 | 78.545601 | 0.002593 | NaN | NaN | NaN | 2023-09-05 00:00:00 | 269.5 | -0.008134 | NaN |
| 2023-10-31 00:00:00 | 78.526268 | -0.000246 | NaN | NaN | NaN | 2023-09-06 00:00:00 | 268.59 | -0.003377 | NaN |
| 2023-11-01 00:00:00 | 79.558014 | 0.013139 | NaN | NaN | NaN | 2023-09-07 00:00:00 | 266.77 | -0.006776 | NaN |
| 2023-11-02 00:00:00 | 80.354652 | 0.010013 | NaN | NaN | NaN | 2023-09-08 00:00:00 | 267.02 | 0.000937 | NaN |
| 2023-11-03 00:00:00 | 81.141594 | 0.009793 | NaN | NaN | NaN | 2023-09-11 00:00:00 | 268.09 | 0.004007 | NaN |
| 2023-11-06 00:00:00 | 80.471245 | -0.008261 | NaN | NaN | NaN | 2023-09-12 00:00:00 | 267.32 | -0.002872 | NaN |
| 2023-11-07 00:00:00 | 80.743263 | 0.00338 | NaN | NaN | NaN | 2023-09-13 00:00:00 | 267.22 | -0.000374 | NaN |
| 2023-11-08 00:00:00 | 80.898712 | 0.001925 | NaN | NaN | NaN | 2023-09-14 00:00:00 | 268.83 | 0.006025 | NaN |
| 2023-11-09 00:00:00 | 80.072922 | -0.010208 | NaN | NaN | NaN | 2023-09-15 00:00:00 | 269.11 | 0.001042 | NaN |
| 2023-11-10 00:00:00 | 80.422668 | 0.004368 | NaN | NaN | NaN | 2023-09-18 00:00:00 | 267.07 | -0.007581 | NaN |
| 2023-11-13 00:00:00 | 79.995186 | -0.005315 | NaN | NaN | NaN | 2023-09-19 00:00:00 | 266.76 | -0.001161 | NaN |
| 2023-11-14 00:00:00 | 81.384476 | 0.017367 | NaN | NaN | NaN | 2023-09-20 00:00:00 | 265.62 | -0.004274 | NaN |
| 2023-11-15 00:00:00 | 80.879288 | -0.006207 | NaN | NaN | NaN | 2023-09-21 00:00:00 | 262.12 | -0.013177 | NaN |
| 2023-11-16 00:00:00 | 81.549637 | 0.008288 | NaN | NaN | NaN | 2023-09-22 00:00:00 | 264.29 | 0.008279 | NaN |
| 2023-11-17 00:00:00 | 81.811951 | 0.003217 | NaN | NaN | NaN | 2023-09-25 00:00:00 | 262.67 | -0.00613 | NaN |
| 2023-11-20 00:00:00 | 82.326851 | 0.006294 | NaN | NaN | NaN | 2023-09-26 00:00:00 | 260.52 | -0.008185 | NaN |
| 2023-11-21 00:00:00 | 82.326851 | 0 | NaN | NaN | NaN | 2023-09-27 00:00:00 | 260.96 | 0.001689 | NaN |
| 2023-11-22 00:00:00 | 82.734894 | 0.004956 | NaN | NaN | NaN | 2023-09-28 00:00:00 | 260.06 | -0.003449 | NaN |
| 2023-11-24 00:00:00 | 82.569733 | -0.001996 | NaN | NaN | NaN | 2023-09-29 00:00:00 | 262.4 | 0.008998 | NaN |
| 2023-11-27 00:00:00 | 82.929192 | 0.004353 | NaN | NaN | NaN | 2023-10-02 00:00:00 | 262 | -0.001524 | NaN |
| 2023-11-28 00:00:00 | 83.356667 | 0.005155 | NaN | NaN | NaN | 2023-10-03 00:00:00 | 258.64 | -0.012824 | NaN |
| 2023-11-29 00:00:00 | 84.017303 | 0.007925 | NaN | NaN | NaN | 2023-10-04 00:00:00 | 256.56 | -0.008042 | NaN |
| 2023-11-30 00:00:00 | 83.424675 | -0.007054 | NaN | NaN | NaN | 2023-10-05 00:00:00 | 257.05 | 0.00191 | NaN |
| 2023-12-01 00:00:00 | 84.704254 | 0.015338 | NaN | NaN | NaN | 2023-10-06 00:00:00 | 258.93 | 0.007314 | NaN |
| 2023-12-04 00:00:00 | 84.119072 | -0.006909 | NaN | NaN | NaN | 2023-10-09 00:00:00 | 258.01 | -0.003553 | NaN |
| 2023-12-05 00:00:00 | 84.606728 | 0.005797 | NaN | NaN | NaN | 2023-10-10 00:00:00 | 260.68 | 0.010348 | NaN |
| 2023-12-06 00:00:00 | 85.074867 | 0.005533 | NaN | NaN | NaN | 2023-10-11 00:00:00 | 263.04 | 0.009053 | NaN |
| 2023-12-07 00:00:00 | 84.987099 | -0.001032 | NaN | NaN | NaN | 2023-10-12 00:00:00 | 264.26 | 0.004638 | NaN |
| 2023-12-08 00:00:00 | 84.694489 | -0.003443 | NaN | NaN | NaN | 2023-10-13 00:00:00 | 261.7 | -0.009687 | NaN |
| 2023-12-11 00:00:00 | 84.557961 | -0.001612 | NaN | NaN | NaN | 2023-10-16 00:00:00 | 260.54 | -0.004433 | NaN |
| 2023-12-12 00:00:00 | 84.733513 | 0.002076 | NaN | NaN | NaN | 2023-10-17 00:00:00 | 261.52 | 0.003761 | NaN |
| 2023-12-13 00:00:00 | 86.137932 | 0.016575 | NaN | NaN | NaN | 2023-10-18 00:00:00 | 258.59 | -0.011204 | NaN |
| 2023-12-14 00:00:00 | 87.033043 | 0.010392 | NaN | NaN | NaN | 2023-10-19 00:00:00 | 256.02 | -0.009939 | NaN |
| 2023-12-15 00:00:00 | 86.915527 | -0.00135 | NaN | NaN | NaN | 2023-10-20 00:00:00 | 254.71 | -0.005117 | NaN |
| 2023-12-18 00:00:00 | 86.935104 | 0.000225 | NaN | NaN | NaN | 2023-10-23 00:00:00 | 252.58 | -0.008362 | NaN |
| 2023-12-19 00:00:00 | 87.150574 | 0.002479 | NaN | NaN | NaN | 2023-10-24 00:00:00 | 252.8 | 0.000871 | NaN |
| 2023-12-20 00:00:00 | 87.160362 | 0.000112 | NaN | NaN | NaN | 2023-10-25 00:00:00 | 253.1 | 0.001187 | NaN |
| 2023-12-21 00:00:00 | 87.317062 | 0.001798 | NaN | NaN | NaN | 2023-10-26 00:00:00 | 251.36 | -0.006875 | NaN |
| 2023-12-22 00:00:00 | 87.199532 | -0.001346 | NaN | NaN | NaN | 2023-10-27 00:00:00 | 253.85 | 0.009906 | NaN |
| 2023-12-26 00:00:00 | 87.512917 | 0.003594 | NaN | NaN | NaN | 2023-10-30 00:00:00 | 254.42 | 0.002245 | NaN |
| 2023-12-27 00:00:00 | 87.826309 | 0.003581 | NaN | NaN | NaN | 2023-10-31 00:00:00 | 252.89 | -0.006014 | NaN |
| 2023-12-28 00:00:00 | 87.581474 | -0.002788 | NaN | NaN | NaN | 2023-11-01 00:00:00 | 252.89 | 0 | NaN |
| 2023-12-29 00:00:00 | 87.219124 | -0.004137 | NaN | NaN | NaN | 2023-11-02 00:00:00 | 256.15 | 0.012891 | NaN |
| 2024-01-02 00:00:00 | 86.3573 | -0.009881 | NaN | NaN | NaN | 2023-11-03 00:00:00 | 260.38 | 0.016514 | NaN |
| 2024-01-03 00:00:00 | 86.024338 | -0.003856 | NaN | NaN | NaN | 2023-11-06 00:00:00 | 264.01 | 0.013941 | NaN |
| 2024-01-04 00:00:00 | 85.632607 | -0.004554 | NaN | NaN | NaN | 2023-11-07 00:00:00 | 262.93 | -0.004091 | NaN |
| 2024-01-05 00:00:00 | 85.368179 | -0.003088 | NaN | NaN | NaN | 2023-11-08 00:00:00 | 262.82 | -0.000418 | NaN |
| 2024-01-08 00:00:00 | 85.475906 | 0.001262 | NaN | NaN | NaN | 2023-11-09 00:00:00 | 262.14 | -0.002587 | NaN |
| 2024-01-09 00:00:00 | 85.142944 | -0.003895 | NaN | NaN | NaN | 2023-11-10 00:00:00 | 260.39 | -0.006676 | NaN |
| 2024-01-10 00:00:00 | 85.750114 | 0.007131 | NaN | NaN | NaN | 2023-11-13 00:00:00 | 261.82 | 0.005492 | NaN |
| 2024-01-11 00:00:00 | 86.523796 | 0.009023 | NaN | NaN | NaN | 2023-11-14 00:00:00 | 263.62 | 0.006875 | NaN |
| 2024-01-12 00:00:00 | 86.680481 | 0.001811 | NaN | NaN | NaN | 2023-11-15 00:00:00 | 268.76 | 0.019498 | NaN |
| 2024-01-16 00:00:00 | 85.877434 | -0.009264 | NaN | NaN | NaN | 2023-11-16 00:00:00 | 268.39 | -0.001377 | NaN |
| 2024-01-17 00:00:00 | 85.55426 | -0.003763 | NaN | NaN | NaN | 2023-11-17 00:00:00 | 267.7 | -0.002571 | NaN |
| 2024-01-18 00:00:00 | 85.642395 | 0.00103 | NaN | NaN | NaN | 2023-11-20 00:00:00 | 269.95 | 0.008405 | NaN |
| 2024-01-19 00:00:00 | 85.681572 | 0.000457 | NaN | NaN | NaN | 2023-11-21 00:00:00 | 270.63 | 0.002519 | NaN |
| 2024-01-22 00:00:00 | 85.740334 | 0.000686 | NaN | NaN | NaN | 2023-11-22 00:00:00 | 269.36 | -0.004693 | NaN |
| 2024-01-23 00:00:00 | 85.299622 | -0.00514 | NaN | NaN | NaN | 2023-11-23 00:00:00 | 270.63 | 0.004715 | NaN |
| 2024-01-24 00:00:00 | 85.064598 | -0.002755 | NaN | NaN | NaN | 2023-11-24 00:00:00 | 269.23 | -0.005173 | NaN |
| 2024-01-25 00:00:00 | 85.671791 | 0.007138 | NaN | NaN | NaN | 2023-11-27 00:00:00 | 268.42 | -0.003009 | NaN |
| 2024-01-26 00:00:00 | 85.799095 | 0.001486 | NaN | NaN | NaN | 2023-11-28 00:00:00 | 270.3 | 0.007004 | NaN |
| 2024-01-29 00:00:00 | 86.122269 | 0.003767 | NaN | NaN | NaN | 2023-11-29 00:00:00 | 269.84 | -0.001702 | NaN |
| 2024-01-30 00:00:00 | 86.318138 | 0.002274 | NaN | NaN | NaN | 2023-11-30 00:00:00 | 270.67 | 0.003076 | NaN |
| 2024-01-31 00:00:00 | 86.161453 | -0.001815 | NaN | NaN | NaN | 2023-12-01 00:00:00 | 270.45 | -0.000813 | NaN |
| 2024-02-01 00:00:00 | 86.88623 | 0.008412 | NaN | NaN | NaN | 2023-12-04 00:00:00 | 270 | -0.001664 | NaN |
| 2024-02-02 00:00:00 | 86.187996 | -0.008036 | NaN | NaN | NaN | 2023-12-05 00:00:00 | 268.32 | -0.006222 | NaN |
| 2024-02-05 00:00:00 | 85.460258 | -0.008444 | NaN | NaN | NaN | 2023-12-06 00:00:00 | 269.23 | 0.003391 | NaN |
| 2024-02-06 00:00:00 | 86.237175 | 0.009091 | NaN | NaN | NaN | 2023-12-07 00:00:00 | 268.43 | -0.002971 | NaN |
| 2024-02-07 00:00:00 | 86.119156 | -0.001369 | NaN | NaN | NaN | 2023-12-08 00:00:00 | 268.78 | 0.001304 | NaN |
| 2024-02-08 00:00:00 | 86.010979 | -0.001256 | NaN | NaN | NaN | 2023-12-11 00:00:00 | 268.4 | -0.001414 | NaN |
| 2024-02-09 00:00:00 | 86.040474 | 0.000343 | NaN | NaN | NaN | 2023-12-12 00:00:00 | 268.92 | 0.001937 | NaN |
| 2024-02-12 00:00:00 | 86.119156 | 0.000914 | NaN | NaN | NaN | 2023-12-13 00:00:00 | 268.64 | -0.001041 | NaN |
| 2024-02-13 00:00:00 | 85.057045 | -0.012333 | NaN | NaN | NaN | 2023-12-14 00:00:00 | 273.18 | 0.0169 | NaN |
| 2024-02-14 00:00:00 | 85.637276 | 0.006822 | NaN | NaN | NaN | 2023-12-15 00:00:00 | 275.06 | 0.006882 | NaN |
| 2024-02-15 00:00:00 | 86.335518 | 0.008153 | NaN | NaN | NaN | 2023-12-18 00:00:00 | 274.09 | -0.003527 | NaN |
| 2024-02-16 00:00:00 | 85.745453 | -0.006835 | NaN | NaN | NaN | 2023-12-19 00:00:00 | 274.46 | 0.00135 | NaN |
| 2024-02-20 00:00:00 | 85.735619 | -0.000115 | NaN | NaN | NaN | 2023-12-20 00:00:00 | 272.72 | -0.00634 | NaN |
| 2024-02-21 00:00:00 | 85.666779 | -0.000803 | NaN | NaN | NaN | 2023-12-21 00:00:00 | 273.62 | 0.0033 | NaN |
| 2024-02-22 00:00:00 | 86.207672 | 0.006314 | NaN | NaN | NaN | 2023-12-22 00:00:00 | 272.38 | -0.004532 | NaN |
| 2024-02-23 00:00:00 | 86.689545 | 0.00559 | NaN | NaN | NaN | 2023-12-25 00:00:00 | 272.5 | 0.000441 | NaN |
| 2024-02-26 00:00:00 | 86.443695 | -0.002836 | NaN | NaN | NaN | 2023-12-26 00:00:00 | 273.88 | 0.005064 | NaN |
| 2024-02-27 00:00:00 | 86.365013 | -0.00091 | NaN | NaN | NaN | 2023-12-27 00:00:00 | 276.49 | 0.00953 | NaN |
| 2024-02-28 00:00:00 | 86.542038 | 0.00205 | NaN | NaN | NaN | 2023-12-28 00:00:00 | 279.58 | 0.011176 | NaN |
| 2024-02-29 00:00:00 | 86.837074 | 0.003409 | NaN | NaN | NaN | 2023-12-29 00:00:00 | 280.09 | 0.001824 | NaN |
| 2024-03-01 00:00:00 | 87.346741 | 0.005869 | NaN | NaN | NaN | 2024-01-01 00:00:00 | 280.45 | 0.001285 | NaN |
| 2024-03-04 00:00:00 | 87.267715 | -0.000905 | NaN | NaN | NaN | 2024-01-02 00:00:00 | 278.12 | -0.008308 | NaN |
| 2024-03-05 00:00:00 | 87.455399 | 0.002151 | NaN | NaN | NaN | 2024-01-03 00:00:00 | 275.66 | -0.008845 | NaN |
| 2024-03-06 00:00:00 | 87.781357 | 0.003727 | NaN | NaN | NaN | 2024-01-04 00:00:00 | 276.35 | 0.002503 | NaN |
| 2024-03-07 00:00:00 | 88.018417 | 0.002701 | NaN | NaN | NaN | 2024-01-05 00:00:00 | 276.12 | -0.000832 | NaN |
| 2024-03-08 00:00:00 | 88.117195 | 0.001122 | NaN | NaN | NaN | 2024-01-08 00:00:00 | 274.74 | -0.004998 | NaN |
| 2024-03-11 00:00:00 | 87.978905 | -0.001569 | NaN | NaN | NaN | 2024-01-09 00:00:00 | 273.95 | -0.002875 | NaN |
| 2024-03-12 00:00:00 | 87.860367 | -0.001347 | NaN | NaN | NaN | 2024-01-10 00:00:00 | 273.37 | -0.002117 | NaN |
| 2024-03-13 00:00:00 | 87.949272 | 0.001012 | NaN | NaN | NaN | 2024-01-11 00:00:00 | 274.96 | 0.005816 | NaN |
| 2024-03-14 00:00:00 | 87.504776 | -0.005054 | NaN | NaN | NaN | 2024-01-12 00:00:00 | 275.6 | 0.002328 | NaN |
| 2024-03-15 00:00:00 | 87.228203 | -0.003161 | NaN | NaN | NaN | 2024-01-15 00:00:00 | 275.55 | -0.000181 | NaN |
| 2024-03-18 00:00:00 | 87.277603 | 0.000566 | NaN | NaN | NaN | 2024-01-16 00:00:00 | 271.96 | -0.013028 | NaN |
| 2024-03-19 00:00:00 | 87.682571 | 0.00464 | NaN | NaN | NaN | 2024-01-17 00:00:00 | 266.71 | -0.019304 | NaN |
| 2024-03-20 00:00:00 | 88.097427 | 0.004731 | NaN | NaN | NaN | 2024-01-18 00:00:00 | 267.09 | 0.001425 | NaN |
| 2024-03-21 00:00:00 | 88.403633 | 0.003476 | NaN | NaN | NaN | 2024-01-19 00:00:00 | 269.14 | 0.007675 | NaN |
| 2024-03-22 00:00:00 | 88.690086 | 0.00324 | NaN | NaN | NaN | 2024-01-22 00:00:00 | 267.35 | -0.006651 | NaN |
| 2024-03-25 00:00:00 | 88.620941 | -0.00078 | NaN | NaN | NaN | 2024-01-23 00:00:00 | 268.06 | 0.002656 | NaN |
| 2024-03-26 00:00:00 | 88.611061 | -0.000111 | NaN | NaN | NaN | 2024-01-24 00:00:00 | 271.92 | 0.0144 | NaN |
| 2024-03-27 00:00:00 | 88.976532 | 0.004124 | NaN | NaN | NaN | 2024-01-25 00:00:00 | 273.65 | 0.006362 | NaN |
| 2024-03-28 00:00:00 | 88.571556 | -0.004551 | NaN | NaN | NaN | 2024-01-26 00:00:00 | 272.8 | -0.003106 | NaN |
| 2024-04-01 00:00:00 | 88.190697 | -0.0043 | NaN | NaN | NaN | 2024-01-29 00:00:00 | 273.84 | 0.003812 | NaN |
| 2024-04-02 00:00:00 | 88.23037 | 0.00045 | NaN | NaN | NaN | 2024-01-30 00:00:00 | 271.08 | -0.010079 | NaN |
| 2024-04-03 00:00:00 | 88.418816 | 0.002136 | NaN | NaN | NaN | 2024-01-31 00:00:00 | 270.26 | -0.003025 | NaN |
| 2024-04-04 00:00:00 | 88.379143 | -0.000449 | NaN | NaN | NaN | 2024-02-01 00:00:00 | 271.18 | 0.003404 | NaN |
| 2024-04-05 00:00:00 | 88.517998 | 0.001571 | NaN | NaN | NaN | 2024-02-02 00:00:00 | 271.36 | 0.000664 | NaN |
| 2024-04-08 00:00:00 | 88.547752 | 0.000336 | NaN | NaN | NaN | 2024-02-05 00:00:00 | 269.99 | -0.005049 | NaN |
| 2024-04-09 00:00:00 | 89.142822 | 0.00672 | NaN | NaN | NaN | 2024-02-06 00:00:00 | 275.04 | 0.018704 | NaN |
| 2024-04-10 00:00:00 | 87.734474 | -0.015799 | NaN | NaN | NaN | 2024-02-07 00:00:00 | 275.66 | 0.002254 | NaN |
| 2024-04-11 00:00:00 | 87.476601 | -0.002939 | NaN | NaN | NaN | 2024-02-08 00:00:00 | 274.5 | -0.004208 | NaN |
| 2024-04-12 00:00:00 | 87.228653 | -0.002834 | NaN | NaN | NaN | 2024-02-09 00:00:00 | 273.78 | -0.002623 | NaN |
| 2024-04-15 00:00:00 | 86.217018 | -0.011598 | NaN | NaN | NaN | 2024-02-12 00:00:00 | 273.49 | -0.001059 | NaN |
| 2024-04-16 00:00:00 | 85.949242 | -0.003106 | NaN | NaN | NaN | 2024-02-13 00:00:00 | 273.26 | -0.000841 | NaN |
| 2024-04-17 00:00:00 | 86.623657 | 0.007847 | NaN | NaN | NaN | 2024-02-14 00:00:00 | 274.52 | 0.004611 | NaN |
| 2024-04-18 00:00:00 | 86.55423 | -0.000801 | NaN | NaN | NaN | 2024-02-15 00:00:00 | 277.24 | 0.009908 | NaN |
| 2024-04-19 00:00:00 | 86.802177 | 0.002865 | NaN | NaN | NaN | 2024-02-16 00:00:00 | 279.36 | 0.007647 | NaN |
| 2024-04-22 00:00:00 | 87.268326 | 0.00537 | NaN | NaN | NaN | 2024-02-19 00:00:00 | 279.29 | -0.000251 | NaN |
| 2024-04-23 00:00:00 | 87.387344 | 0.001364 | NaN | NaN | NaN | 2024-02-20 00:00:00 | 280.32 | 0.003688 | NaN |
| 2024-04-24 00:00:00 | 86.762512 | -0.00715 | NaN | NaN | NaN | 2024-02-21 00:00:00 | 280.67 | 0.001249 | NaN |
| 2024-04-25 00:00:00 | 86.514565 | -0.002858 | NaN | NaN | NaN | 2024-02-22 00:00:00 | 282.97 | 0.008195 | NaN |
| 2024-04-26 00:00:00 | 86.891441 | 0.004356 | NaN | NaN | NaN | 2024-02-23 00:00:00 | 282.69 | -0.00099 | NaN |
| 2024-04-29 00:00:00 | 87.317917 | 0.004908 | NaN | NaN | NaN | 2024-02-26 00:00:00 | 282.06 | -0.002229 | NaN |
| 2024-04-30 00:00:00 | 86.435219 | -0.010109 | NaN | NaN | NaN | 2024-02-27 00:00:00 | 283.41 | 0.004786 | NaN |
| 2024-05-01 00:00:00 | 86.794746 | 0.004159 | NaN | NaN | NaN | 2024-02-28 00:00:00 | 280.09 | -0.011714 | NaN |
| 2024-05-02 00:00:00 | 87.501854 | 0.008147 | NaN | NaN | NaN | 2024-02-29 00:00:00 | 281.25 | 0.004142 | NaN |
| 2024-05-03 00:00:00 | 88.218918 | 0.008195 | NaN | NaN | NaN | 2024-03-01 00:00:00 | 282.53 | 0.004551 | NaN |
| 2024-05-06 00:00:00 | 88.467896 | 0.002822 | NaN | NaN | NaN | 2024-03-04 00:00:00 | 283.43 | 0.003186 | NaN |
| 2024-05-07 00:00:00 | 88.537613 | 0.000788 | NaN | NaN | NaN | 2024-03-05 00:00:00 | 281.72 | -0.006033 | NaN |
| 2024-05-08 00:00:00 | 88.208954 | -0.003712 | NaN | NaN | NaN | 2024-03-06 00:00:00 | 283.2 | 0.005253 | NaN |
| 2024-05-09 00:00:00 | 88.507736 | 0.003387 | NaN | NaN | NaN | 2024-03-07 00:00:00 | 283.71 | 0.001801 | NaN |
| 2024-05-10 00:00:00 | 88.298592 | -0.002363 | NaN | NaN | NaN | 2024-03-08 00:00:00 | 284.6 | 0.003137 | NaN |
| 2024-05-13 00:00:00 | 88.388222 | 0.001015 | NaN | NaN | NaN | 2024-03-11 00:00:00 | 285.17 | 0.002003 | NaN |
| 2024-05-14 00:00:00 | 88.587402 | 0.002253 | NaN | NaN | NaN | 2024-03-12 00:00:00 | 287.26 | 0.007329 | NaN |
| 2024-05-15 00:00:00 | 89.513611 | 0.010455 | NaN | NaN | NaN | 2024-03-13 00:00:00 | 285.71 | -0.005396 | NaN |
| 2024-05-16 00:00:00 | 89.214844 | -0.003338 | NaN | NaN | NaN | 2024-03-14 00:00:00 | 286.34 | 0.002205 | NaN |
| 2024-05-17 00:00:00 | 89.04554 | -0.001898 | NaN | NaN | NaN | 2024-03-15 00:00:00 | 283.88 | -0.008591 | NaN |
| 2024-05-20 00:00:00 | 89.055489 | 0.000112 | NaN | NaN | NaN | 2024-03-18 00:00:00 | 284.82 | 0.003311 | NaN |
| 2024-05-21 00:00:00 | 89.125206 | 0.000783 | NaN | NaN | NaN | 2024-03-19 00:00:00 | 282.51 | -0.00811 | NaN |
| 2024-05-22 00:00:00 | 88.836388 | -0.003241 | NaN | NaN | NaN | 2024-03-20 00:00:00 | 283.09 | 0.002053 | NaN |
| 2024-05-23 00:00:00 | 88.228874 | -0.006839 | NaN | NaN | NaN | 2024-03-21 00:00:00 | 286.22 | 0.011057 | NaN |
| 2024-05-24 00:00:00 | 88.577454 | 0.003951 | NaN | NaN | NaN | 2024-03-22 00:00:00 | 284.14 | -0.007267 | NaN |
| 2024-05-28 00:00:00 | 88.049614 | -0.005959 | NaN | NaN | NaN | 2024-03-25 00:00:00 | 283.47 | -0.002358 | NaN |
| 2024-05-29 00:00:00 | 87.730911 | -0.00362 | NaN | NaN | NaN | 2024-03-26 00:00:00 | 283.75 | 0.000988 | NaN |
| 2024-05-30 00:00:00 | 88.258759 | 0.006017 | NaN | NaN | NaN | 2024-03-27 00:00:00 | 283.13 | -0.002185 | NaN |
| 2024-05-31 00:00:00 | 88.687004 | 0.004852 | NaN | NaN | NaN | 2024-03-28 00:00:00 | 284.14 | 0.003567 | NaN |
| 2024-06-03 00:00:00 | 89.089996 | 0.004544 | NaN | NaN | NaN | 2024-03-29 00:00:00 | 284.68 | 0.0019 | NaN |
| 2024-06-04 00:00:00 | 89.150002 | 0.000674 | NaN | NaN | NaN | 2024-04-01 00:00:00 | 284.88 | 0.000703 | NaN |
| 2024-06-05 00:00:00 | 89.389999 | 0.002692 | NaN | NaN | NaN | 2024-04-02 00:00:00 | 287.31 | 0.00853 | NaN |
| 2024-06-06 00:00:00 | 89.18 | -0.002349 | NaN | NaN | NaN | 2024-04-03 00:00:00 | 286.38 | -0.003237 | NaN |
| 2024-06-07 00:00:00 | 88.480003 | -0.007849 | NaN | NaN | NaN | 2024-04-04 00:00:00 | 287.41 | 0.003597 | NaN |
| 2024-06-10 00:00:00 | 88.459999 | -0.000226 | NaN | NaN | NaN | 2024-04-05 00:00:00 | 287.29 | -0.000418 | NaN |
| 2024-06-11 00:00:00 | 88.800003 | 0.003844 | NaN | NaN | NaN | 2024-04-08 00:00:00 | 288.21 | 0.003202 | NaN |
| 2024-06-12 00:00:00 | 89.150002 | 0.003941 | NaN | NaN | NaN | 2024-04-09 00:00:00 | 290.18 | 0.006835 | NaN |
| 2024-06-13 00:00:00 | 89.389999 | 0.002692 | NaN | NaN | NaN | 2024-04-10 00:00:00 | 290.59 | 0.001413 | NaN |
| 2024-06-14 00:00:00 | 89.279999 | -0.001231 | NaN | NaN | NaN | 2024-04-11 00:00:00 | 289.87 | -0.002478 | NaN |
| 2024-06-17 00:00:00 | 89.010002 | -0.003024 | NaN | NaN | NaN | 2024-04-12 00:00:00 | 286.72 | -0.010867 | NaN |
| 2024-06-18 00:00:00 | 89.599998 | 0.006628 | NaN | NaN | NaN | 2024-04-15 00:00:00 | 283.89 | -0.00987 | NaN |
| 2024-06-20 00:00:00 | 89.269997 | -0.003683 | NaN | NaN | NaN | 2024-04-16 00:00:00 | 278.69 | -0.018317 | NaN |
| 2024-06-21 00:00:00 | 89.379997 | 0.001232 | NaN | NaN | NaN | 2024-04-17 00:00:00 | 280.21 | 0.005454 | NaN |
| 2024-06-24 00:00:00 | 89.419998 | 0.000448 | NaN | NaN | NaN | 2024-04-18 00:00:00 | 281.02 | 0.002891 | NaN |
| 2024-06-25 00:00:00 | 89.410004 | -0.000112 | NaN | NaN | NaN | 2024-04-19 00:00:00 | 277.82 | -0.011387 | NaN |
| 2024-06-26 00:00:00 | 89.110001 | -0.003355 | NaN | NaN | NaN | 2024-04-22 00:00:00 | 279.23 | 0.005075 | NaN |
| 2024-06-27 00:00:00 | 89.190002 | 0.000898 | NaN | NaN | NaN | 2024-04-23 00:00:00 | 281.38 | 0.0077 | NaN |
| 2024-06-28 00:00:00 | 88.480003 | -0.007961 | NaN | NaN | NaN | 2024-04-24 00:00:00 | 284.66 | 0.011657 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-04-25 00:00:00 | 283.96 | -0.002459 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-04-26 00:00:00 | 287.24 | 0.011551 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-04-29 00:00:00 | 290.11 | 0.009992 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-04-30 00:00:00 | 288.71 | -0.004826 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-01 00:00:00 | 288.62 | -0.000312 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-02 00:00:00 | 290.66 | 0.007068 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-03 00:00:00 | 292.85 | 0.007535 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-06 00:00:00 | 294.23 | 0.004712 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-07 00:00:00 | 293.47 | -0.002583 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-08 00:00:00 | 292.92 | -0.001874 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-09 00:00:00 | 292.31 | -0.002082 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-10 00:00:00 | 294.28 | 0.006739 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-13 00:00:00 | 295.85 | 0.005335 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-14 00:00:00 | 296.77 | 0.00311 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-15 00:00:00 | 298.22 | 0.004886 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-16 00:00:00 | 301.06 | 0.009523 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-17 00:00:00 | 302.56 | 0.004982 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-20 00:00:00 | 302.94 | 0.001256 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-21 00:00:00 | 301.33 | -0.005315 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-22 00:00:00 | 301.77 | 0.00146 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-23 00:00:00 | 300.47 | -0.004308 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-24 00:00:00 | 299.11 | -0.004526 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-27 00:00:00 | 300.54 | 0.004781 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-28 00:00:00 | 299.63 | -0.003028 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-29 00:00:00 | 296.22 | -0.011381 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-30 00:00:00 | 293.13 | -0.010431 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-05-31 00:00:00 | 291.24 | -0.006448 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-03 00:00:00 | 295.94 | 0.016138 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-04 00:00:00 | 290.33 | -0.018957 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-05 00:00:00 | 292.82 | 0.008576 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-06 00:00:00 | 295.66 | 0.009699 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-07 00:00:00 | 295.47 | -0.000643 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-10 00:00:00 | 295.45 | -0.000068 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-11 00:00:00 | 294.31 | -0.003859 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-12 00:00:00 | 294.97 | 0.002243 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-13 00:00:00 | 296.44 | 0.004984 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-14 00:00:00 | 297.02 | 0.001957 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-17 00:00:00 | 296.55 | -0.001582 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-18 00:00:00 | 298.47 | 0.006474 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-19 00:00:00 | 301.07 | 0.008711 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-20 00:00:00 | 301.24 | 0.000565 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-21 00:00:00 | 299.6 | -0.005444 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-24 00:00:00 | 298.68 | -0.003071 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-25 00:00:00 | 298.75 | 0.000234 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-26 00:00:00 | 298.88 | 0.000435 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-27 00:00:00 | 297.45 | -0.004785 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | 2024-06-28 00:00:00 | 298.63 | 0.003967 | NaN |

## Regional Simple Averages
| Unnamed: 0 | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 |
| --- | --- | --- | --- | --- |
| NaN | NaN | NaN | NaN | NaN |
| NaN | Values | NaN | NaN | NaN |
| Row Labels | Average of Adj. Default Spread | Average of Country Risk Premium | Average of Equity Risk Premium | Average of Corporate Tax Rate |
| Africa | 0.060541 | 0.078585 | 0.119685 | 0.268193 |
| Asia | 0.036416 | 0.047269 | 0.088369 | 0.245087 |
| Australia & New Zealand | 0.014118 | 0.018326 | 0.059426 | 0.292467 |
| Caribbean | 0.03579 | 0.046457 | 0.087557 | 0.177586 |
| Central and South America | 0.054311 | 0.070499 | 0.111599 | 0.2837 |
| Eastern Europe & Russia | 0.036893 | 0.04797 | 0.089251 | 0.161111 |
| Middle East | 0.032669 | 0.042406 | 0.083506 | 0.134615 |
| North America | 0 | 0 | 0.0411 | 0.2575 |
| Western Europe | 0.008753 | 0.011362 | 0.052462 | 0.195162 |
| Grand Total | 0.037436 | 0.048608 | 0.089739 | 0.217362 |

## Regional Weighted Averages
| Country | GDP (in billions) | Moody's rating | Adj. Default Spread | Equity Risk Premium | Country Risk Premium | Corporate Tax Rate | Region | GDP Weight | Weight\*Default Spread | Weight\*ERP | Weight\*CRP | Weight \* Tax Rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Angola | 84722.957642 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.25 | Africa | 0.036064 | 0.002205 | 0.004345 | 0.002863 | 0.009016 |
| Benin | 19673.284686 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.3 | Africa | 0.008374 | 0.000355 | 0.000805 | 0.000460 | 0.002512 |
| Botswana | 19395.765126 | A3 | 0.01128 | 0.055741 | 0.014641 | 0.22 | Africa | 0.008256 | 0.000093 | 0.00046 | 0.000121 | 0.001816 |
| Burkina Faso | 20324.617839 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.28 | Africa | 0.008652 | 0.00061 | 0.001148 | 0.000792 | 0.002422 |
| Cameroon | 47945.51009 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.33 | Africa | 0.020409 | 0.00144 | 0.002708 | 0.001869 | 0.006735 |
| Cape Verde | 1936 | B3 | 0.061153 | 0.120479 | 0.079379 | 0 | Africa | 0.000824 | 0.00005 | 0.000099 | 0.000065 | 0.000000 |
| Congo (Democratic Republic of) | 66383.287003 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.3 | Africa | 0.028257 | 0.001728 | 0.003404 | 0.002243 | 0.008477 |
| Congo (Republic of) | 15321.055818 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.28 | Africa | 0.006522 | 0.000552 | 0.000985 | 0.000717 | 0.001826 |
| Côte d'Ivoire | 78788.828907 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.25 | Africa | 0.033538 | 0.000949 | 0.002611 | 0.001232 | 0.008384 |
| Egypt | 395926.075163 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.225 | Africa | 0.168533 | 0.01189 | 0.022361 | 0.015434 | 0.037920 |
| Ethiopia | 163697.927594 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.3 | Africa | 0.069681 | 0.005902 | 0.010526 | 0.007662 | 0.020904 |
| Gabon | 20516.134389 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.3 | Africa | 0.008733 | 0.00074 | 0.001319 | 0.000960 | 0.002620 |
| Ghana | 76370.394412 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.25 | Africa | 0.032508 | 0.003059 | 0.005307 | 0.003971 | 0.008127 |
| Kenya | 107440.575838 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.3 | Africa | 0.045734 | 0.002797 | 0.00551 | 0.003630 | 0.013720 |
| Mali | 20904.898296 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.2686 | Africa | 0.008899 | 0.000754 | 0.001344 | 0.000978 | 0.002390 |
| Mauritius | 14397.127281 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.15 | Africa | 0.006128 | 0.000127 | 0.000416 | 0.000165 | 0.000919 |
| Morocco | 141109.373209 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.32 | Africa | 0.060066 | 0.001415 | 0.004305 | 0.001836 | 0.019221 |
| Mozambique | 20624.597847 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.32 | Africa | 0.008779 | 0.000744 | 0.001326 | 0.000965 | 0.002809 |
| Namibia | 12351.024844 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.32 | Africa | 0.005257 | 0.000223 | 0.000505 | 0.000289 | 0.001682 |
| Niger | 16819.170421 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.2686 | Africa | 0.007159 | 0.000674 | 0.001169 | 0.000875 | 0.001923 |
| Nigeria | 362814.951696 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.3 | Africa | 0.154439 | 0.010896 | 0.020491 | 0.014144 | 0.046332 |
| Rwanda | 14097.768648 | B2 | 0.051753 | 0.108278 | 0.067178 | 0.3 | Africa | 0.006001 | 0.000311 | 0.00065 | 0.000403 | 0.001800 |
| Senegal | 31013.986429 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.3 | Africa | 0.013202 | 0.000447 | 0.001122 | 0.000580 | 0.003960 |
| South Africa | 377781.600986 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.27 | Africa | 0.160809 | 0.004552 | 0.012519 | 0.005909 | 0.043419 |
| Swaziland | 4597.855845 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.275 | Africa | 0.001957 | 0.00012 | 0.000236 | 0.000155 | 0.000538 |
| Tanzania | 79158.286334 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.3 | Africa | 0.033695 | 0.001427 | 0.003237 | 0.001852 | 0.010109 |
| Togo | 9171.261835 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.2686 | Africa | 0.003904 | 0.000239 | 0.00047 | 0.000310 | 0.001049 |
| Tunisia | 48529.595417 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.15 | Africa | 0.020657 | 0.00175 | 0.00312 | 0.002271 | 0.003099 |
| Uganda | 49272.882214 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.3 | Africa | 0.020974 | 0.001283 | 0.002527 | 0.001665 | 0.006292 |
| Zambia | 28162.630954 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.35 | Africa | 0.011988 | 0.001015 | 0.001811 | 0.001318 | 0.004196 |
| Africa | 2349249.426763 | NaN | 0.058347 | 0.116837 | 0.075737 | 0.274219 | NaN | 1.0 | NaN | NaN | NaN | NaN |
| Bangladesh | 437415.331041 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.3 | Asia | 0.013208 | 0.000559 | 0.001269 | 0.000726 | 0.003962 |
| Cambodia | 31772.759999 | B2 | 0.051753 | 0.108278 | 0.067178 | 0.2 | Asia | 0.000959 | 0.00005 | 0.000104 | 0.000064 | 0.000192 |
| China | 17794781.986104 | A1 | 0.006635 | 0.049713 | 0.008613 | 0.25 | Asia | 0.537322 | 0.003565 | 0.026712 | 0.004628 | 0.134331 |
| Fiji | 5494.797541 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.2 | Asia | 0.000166 | 0.000007 | 0.000016 | 0.000009 | 0.000033 |
| Hong Kong | 382054.574299 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.165 | Asia | 0.011536 | 0.000065 | 0.000559 | 0.000084 | 0.001903 |
| India | 3549918.918778 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.3 | Asia | 0.107192 | 0.002217 | 0.007283 | 0.002877 | 0.032157 |
| Indonesia | 1371171.152331 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.22 | Asia | 0.041403 | 0.000742 | 0.002664 | 0.000963 | 0.009109 |
| Japan | 4212945.159781 | A1 | 0.006635 | 0.049713 | 0.008613 | 0.3062 | Asia | 0.127212 | 0.000844 | 0.006324 | 0.001096 | 0.038952 |
| Korea | 1712792.854202 | Aa2 | 0.004645 | 0.047129 | 0.006029 | 0.25 | Asia | 0.051719 | 0.00024 | 0.002437 | 0.000312 | 0.012930 |
| Laos | 15843.155731 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.2686 | Asia | 0.000478 | 0.000045 | 0.000078 | 0.000058 | 0.000128 |
| Macao | 47061.843716 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.2686 | Asia | 0.001421 | 0.000008 | 0.000069 | 0.000010 | 0.000382 |
| Malaysia | 399648.828547 | A3 | 0.01128 | 0.055741 | 0.014641 | 0.24 | Asia | 0.012068 | 0.000136 | 0.000673 | 0.000177 | 0.002896 |
| Maldives | 6600 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.2686 | Asia | 0.000199 | 0.000014 | 0.000026 | 0.000018 | 0.000054 |
| Mongolia | 19872.18037 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.25 | Asia | 0.0006 | 0.000037 | 0.000072 | 0.000048 | 0.000150 |
| Pakistan | 338368.455318 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.29 | Asia | 0.010217 | 0.000962 | 0.001668 | 0.001248 | 0.002963 |
| Papua New Guinea | 30932.49625 | B2 | 0.051753 | 0.108278 | 0.067178 | 0.3 | Asia | 0.000934 | 0.000048 | 0.000101 | 0.000063 | 0.000280 |
| Philippines | 437146.37273 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.25 | Asia | 0.0132 | 0.000236 | 0.000849 | 0.000307 | 0.003300 |
| Singapore | 501427.50008 | Aaa | 0 | 0.0411 | 0 | 0.17 | Asia | 0.015141 | 0 | 0.000622 | 0.000000 | 0.002574 |
| Solomon Islands | 1631.286701 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.3 | Asia | 0.000049 | 0.000003 | 0.000007 | 0.000005 | 0.000015 |
| Sri Lanka | 84356.860421 | Ca | 0.112906 | 0.187658 | 0.146558 | 0.24 | Asia | 0.002547 | 0.000288 | 0.000478 | 0.000373 | 0.000611 |
| Taiwan | 791610 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.2 | Asia | 0.023903 | 0.000135 | 0.001157 | 0.000175 | 0.004781 |
| Thailand | 514944.993834 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.2 | Asia | 0.015549 | 0.000234 | 0.000943 | 0.000304 | 0.003110 |
| Vietnam | 429716.96905 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.2 | Asia | 0.012976 | 0.000367 | 0.00101 | 0.000477 | 0.002595 |
| Asia | 33117508.476822 | NaN | 0.010802 | 0.055122 | 0.014022 | 0.257408 | NaN | 1.0 | NaN | NaN | NaN | NaN |
| Australia | 1723827.215335 | Aaa | 0 | 0.0411 | 0 | 0.3 | Australia & New Zealand | 0.871189 | 0 | 0.035806 | 0.000000 | 0.261357 |
| Cook Islands | 1414 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.2974 | Australia & New Zealand | 0.000715 | 0.00003 | 0.000069 | 0.000039 | 0.000213 |
| New Zealand | 253465.703232 | Aaa | 0 | 0.0411 | 0 | 0.28 | Australia & New Zealand | 0.128097 | 0 | 0.005265 | 0.000000 | 0.035867 |
| Australia & New Zealand | 1978706.918567 | NaN | 0.00003 | 0.041139 | 0.000039 | 0.297436 | NaN | 1 | NaN | NaN | NaN | NaN |
| Aruba | 3544.707788 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.25 | Caribbean | 0.010053 | 0.000208 | 0.000683 | 0.000270 | 0.002513 |
| Bahamas | 11210 | B1 | 0.042354 | 0.096077 | 0.054977 | 0 | Caribbean | 0.031791 | 0.001346 | 0.003054 | 0.001748 | 0.000000 |
| Barbados | 6393.56419 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.055 | Caribbean | 0.018132 | 0.001109 | 0.002185 | 0.001439 | 0.000997 |
| Bermuda | 7827.98 | A2 | 0.007962 | 0.051435 | 0.010335 | 0 | Caribbean | 0.0222 | 0.000177 | 0.001142 | 0.000229 | 0.000000 |
| Cayman Islands | 6600.844002 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0 | Caribbean | 0.01872 | 0.000106 | 0.000906 | 0.000137 | 0.000000 |
| Cuba | 107351 | Ca | 0.112906 | 0.187658 | 0.146558 | 0.2853 | Caribbean | 0.304446 | 0.034374 | 0.057132 | 0.044619 | 0.086859 |
| Curacao | 3073.840325 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.22 | Caribbean | 0.008717 | 0.00018 | 0.000592 | 0.000234 | 0.001918 |
| Dominican Republic | 121444.279314 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.27 | Caribbean | 0.344415 | 0.011655 | 0.029284 | 0.015128 | 0.092992 |
| Jamaica | 19423.355367 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.25 | Caribbean | 0.055084 | 0.002333 | 0.005292 | 0.003028 | 0.013771 |
| Montserrat | 16199 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.2853 | Caribbean | 0.04594 | 0.00095 | 0.003121 | 0.001233 | 0.013107 |
| St. Maarten | 11900 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.2853 | Caribbean | 0.033748 | 0.000955 | 0.002627 | 0.001240 | 0.009628 |
| St. Vincent & the Grenadines | 8100 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.2853 | Caribbean | 0.022972 | 0.001405 | 0.002768 | 0.001823 | 0.006554 |
| Trinidad and Tobago | 28139.94479 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.3 | Caribbean | 0.079805 | 0.002259 | 0.006213 | 0.002933 | 0.023941 |
| Turks and Caicos Islands | 1402.054391 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0 | Caribbean | 0.003976 | 0.00006 | 0.000241 | 0.000078 | 0.000000 |
| Caribbean | 352610.570167 | NaN | 0.057117 | 0.11524 | 0.07414 | 0.25228 | NaN | 1.0 | NaN | NaN | 0.074140 | NaN |
| Argentina | 640591.410664 | Ca | 0.112906 | 0.187658 | 0.146558 | 0.35 | Central and South America | 0.101386 | 0.011447 | 0.019026 | 0.014859 | 0.035485 |
| Belize | 3281.5 | Caa2 | 0.084707 | 0.151054 | 0.109954 | 0.2853 | Central and South America | 0.000519 | 0.000044 | 0.000078 | 0.000057 | 0.000148 |
| Bolivia | 45849.832906 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.25 | Central and South America | 0.007257 | 0.000683 | 0.001185 | 0.000886 | 0.001814 |
| Brazil | 2173665.655937 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.34 | Central and South America | 0.344024 | 0.009739 | 0.026781 | 0.012642 | 0.116968 |
| Chile | 335533.331669 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.27 | Central and South America | 0.053105 | 0.000423 | 0.002731 | 0.000549 | 0.014338 |
| Colombia | 363540.156235 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.35 | Central and South America | 0.057537 | 0.001031 | 0.003703 | 0.001338 | 0.020138 |
| Costa Rica | 86497.941439 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.3 | Central and South America | 0.01369 | 0.00058 | 0.001315 | 0.000753 | 0.004107 |
| Ecuador | 118844.826 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.25 | Central and South America | 0.018809 | 0.00177 | 0.003071 | 0.002298 | 0.004702 |
| El Salvador | 34015.62 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.3 | Central and South America | 0.005384 | 0.00038 | 0.000714 | 0.000493 | 0.001615 |
| Guatemala | 102050.473864 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.25 | Central and South America | 0.016151 | 0.00038 | 0.001158 | 0.000494 | 0.004038 |
| Honduras | 34400.509852 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.25 | Central and South America | 0.005445 | 0.000231 | 0.000523 | 0.000299 | 0.001361 |
| Mexico | 1788886.821047 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.3 | Central and South America | 0.283126 | 0.005072 | 0.01822 | 0.006584 | 0.084938 |
| Nicaragua | 17829.215284 | B2 | 0.051753 | 0.108278 | 0.067178 | 0.3 | Central and South America | 0.002822 | 0.000146 | 0.000306 | 0.000190 | 0.000847 |
| Panama | 83382.4 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.25 | Central and South America | 0.013197 | 0.000273 | 0.000897 | 0.000354 | 0.003299 |
| Paraguay | 42956.263544 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.1 | Central and South America | 0.006799 | 0.00016 | 0.000487 | 0.000208 | 0.000680 |
| Peru | 267603.248655 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.295 | Central and South America | 0.042353 | 0.000637 | 0.002568 | 0.000827 | 0.012494 |
| Suriname | 3782.437296 | Caa3 | 0.094107 | 0.163255 | 0.122155 | 0.36 | Central and South America | 0.000599 | 0.000056 | 0.000098 | 0.000073 | 0.000216 |
| Uruguay | 77240.831587 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.25 | Central and South America | 0.012225 | 0.000184 | 0.000741 | 0.000239 | 0.003056 |
| Venezuela | 98400 | C | 0.175 | 0.268258 | 0.227158 | 0.34 | Central and South America | 0.015574 | 0.002725 | 0.004178 | 0.003538 | 0.005295 |
| Central and South America | 6318352.475979 | NaN | 0.035961 | 0.087779 | 0.046679 | 0.31554 | NaN | 1.0 | NaN | NaN | NaN | NaN |
| Albania | 22977.677861 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.15 | Eastern Europe & Russia | 0.004424 | 0.000187 | 0.000425 | 0.000243 | 0.000664 |
| Armenia | 24212.134631 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.18 | Eastern Europe & Russia | 0.004661 | 0.000158 | 0.000396 | 0.000205 | 0.000839 |
| Azerbaijan | 72356.176471 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.2 | Eastern Europe & Russia | 0.01393 | 0.000328 | 0.000998 | 0.000426 | 0.002786 |
| Belarus | 71857.382746 | C | 0.175 | 0.268258 | 0.227158 | 0.18 | Eastern Europe & Russia | 0.013834 | 0.002421 | 0.003711 | 0.003142 | 0.002490 |
| Bosnia and Herzegovina | 27054.889363 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.1 | Eastern Europe & Russia | 0.005208 | 0.000319 | 0.000628 | 0.000413 | 0.000521 |
| Bulgaria | 101584.384673 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.1 | Eastern Europe & Russia | 0.019557 | 0.000294 | 0.001186 | 0.000382 | 0.001956 |
| Croatia | 82688.842717 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.18 | Eastern Europe & Russia | 0.015919 | 0.000285 | 0.001024 | 0.000370 | 0.002865 |
| Czech Republic | 330858.339872 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.19 | Eastern Europe & Russia | 0.063695 | 0.000359 | 0.003084 | 0.000466 | 0.012102 |
| Estonia | 40744.848828 | A1 | 0.006635 | 0.049713 | 0.008613 | 0.2 | Eastern Europe & Russia | 0.007844 | 0.000052 | 0.00039 | 0.000068 | 0.001569 |
| Georgia | 30535.530479 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.15 | Eastern Europe & Russia | 0.005879 | 0.000166 | 0.000458 | 0.000216 | 0.000882 |
| Hungary | 212388.906459 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.09 | Eastern Europe & Russia | 0.040888 | 0.000732 | 0.002631 | 0.000951 | 0.003680 |
| Kazakhstan | 261421.121086 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.2 | Eastern Europe & Russia | 0.050328 | 0.000902 | 0.003239 | 0.001170 | 0.010066 |
| Kyrgyzstan | 13987.627909 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.1 | Eastern Europe & Russia | 0.002693 | 0.000165 | 0.000324 | 0.000214 | 0.000269 |
| Latvia | 43627.078481 | A3 | 0.01128 | 0.055741 | 0.014641 | 0.2 | Eastern Europe & Russia | 0.008399 | 0.000095 | 0.000468 | 0.000123 | 0.001680 |
| Lithuania | 77836.396963 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.15 | Eastern Europe & Russia | 0.014985 | 0.000119 | 0.000771 | 0.000155 | 0.002248 |
| Macedonia | 14761.237042 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.1 | Eastern Europe & Russia | 0.002842 | 0.000096 | 0.000242 | 0.000125 | 0.000284 |
| Moldova | 16539.436547 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.12 | Eastern Europe & Russia | 0.003184 | 0.000195 | 0.000384 | 0.000253 | 0.000382 |
| Montenegro | 7404.541965 | B1 | 0.042354 | 0.096077 | 0.054977 | 0.15 | Eastern Europe & Russia | 0.001425 | 0.00006 | 0.000137 | 0.000078 | 0.000214 |
| Poland | 811229.100688 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.19 | Eastern Europe & Russia | 0.156174 | 0.001243 | 0.008033 | 0.001614 | 0.029673 |
| Romania | 351002.57963 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.16 | Eastern Europe & Russia | 0.067573 | 0.001397 | 0.004591 | 0.001814 | 0.010812 |
| Russia | 2021421.476035 | NR | 0.02831 | 0.077947 | 0.036747 | 0.2 | Eastern Europe & Russia | 0.389154 | 0.011017 | 0.030333 | 0.014300 | 0.077831 |
| Serbia | 75187.125427 | Ba2 | 0.02831 | 0.077847 | 0.036747 | 0.15 | Eastern Europe & Russia | 0.014475 | 0.00041 | 0.001127 | 0.000532 | 0.002171 |
| Slovakia | 132793.622283 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.21 | Eastern Europe & Russia | 0.025565 | 0.000204 | 0.001315 | 0.000264 | 0.005369 |
| Slovenia | 68216.781411 | A3 | 0.01128 | 0.055741 | 0.014641 | 0.19 | Eastern Europe & Russia | 0.013133 | 0.000148 | 0.000732 | 0.000192 | 0.002495 |
| Tajikistan | 12060.602009 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.18 | Eastern Europe & Russia | 0.002322 | 0.000142 | 0.00028 | 0.000184 | 0.000418 |
| Ukraine | 178757.021387 | Ca | 0.112906 | 0.187658 | 0.146558 | 0.18 | Eastern Europe & Russia | 0.034413 | 0.003885 | 0.006458 | 0.005044 | 0.006194 |
| Uzbekistan | 90889.149307 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.15 | Eastern Europe & Russia | 0.017498 | 0.000592 | 0.001488 | 0.000769 | 0.002625 |
| Eastern Europe & Russia | 5194394.012266 | NaN | 0.025972 | 0.074852 | 0.033713 | 0.183083 | NaN | 1.0 | NaN | NaN | NaN | NaN |
| Abu Dhabi | 310000 | Aa2 | 0.004645 | 0.047129 | 0.006029 | 0.15 | Middle East | 0.098562 | 0.000458 | 0.004645 | 0.000594 | 0.014784 |
| Bahrain | 43205 | B2 | 0.051753 | 0.108278 | 0.067178 | 0 | Middle East | 0.013737 | 0.000711 | 0.001487 | 0.000923 | 0.000000 |
| Iraq | 250842.782139 | Caa1 | 0.070553 | 0.132681 | 0.091581 | 0.15 | Middle East | 0.079754 | 0.005627 | 0.010582 | 0.007304 | 0.011963 |
| Israel | 509901.495702 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.23 | Middle East | 0.16212 | 0.001291 | 0.008339 | 0.001676 | 0.037287 |
| Jordan | 50813.642349 | Ba3 | 0.033839 | 0.085024 | 0.043924 | 0.2 | Middle East | 0.016156 | 0.000547 | 0.001374 | 0.000710 | 0.003231 |
| Kuwait | 11000 | A1 | 0.006635 | 0.049713 | 0.008613 | 0.15 | Middle East | 0.003497 | 0.000023 | 0.000174 | 0.000030 | 0.000525 |
| Lebanon | 17937.256175 | C | 0.175 | 0.268258 | 0.227158 | 0.17 | Middle East | 0.005703 | 0.000998 | 0.00153 | 0.001295 | 0.000970 |
| Oman | 108192.457737 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.15 | Middle East | 0.034399 | 0.00081 | 0.002466 | 0.001052 | 0.005160 |
| Qatar | 235770.403735 | Aa2 | 0.004645 | 0.047129 | 0.006029 | 0.1 | Middle East | 0.074962 | 0.000348 | 0.003533 | 0.000452 | 0.007496 |
| Ras Al Khaimah (Emirate of) | 11000 | A3 | 0.01128 | 0.055741 | 0.014641 | 0 | Middle East | 0.003497 | 0.000039 | 0.000195 | 0.000051 | 0.000000 |
| Saudi Arabia | 1067582.933333 | A1 | 0.006635 | 0.049713 | 0.008613 | 0.2 | Middle East | 0.33943 | 0.002252 | 0.016874 | 0.002923 | 0.067886 |
| Sharjah | 24800 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0 | Middle East | 0.007885 | 0.000186 | 0.000565 | 0.000241 | 0.000000 |
| United Arab Emirates | 504173.451327 | Aa2 | 0.004645 | 0.047129 | 0.006029 | 0.25 | Middle East | 0.160298 | 0.000745 | 0.007555 | 0.000966 | 0.040075 |
| Middle East | 3145219.422498 | NaN | 0.014034 | 0.059317 | 0.018217 | 0.189377 | NaN | 1.0 | NaN | NaN | NaN | NaN |
| Canada | 2140085.567791 | Aaa | 0 | 0.0411 | 0 | 0.265 | North America | 0.072543 | 0 | 0.002982 | 0.000000 | 0.019224 |
| United States | 27360935 | Aaa | 0 | 0.0411 | 0 | 0.25 | North America | 0.927457 | 0 | 0.038118 | 0.000000 | 0.231864 |
| North America | 29501020.567791 | NaN | 0 | 0.0411 | 0 | 0.251088 | NaN | NaN | NaN | NaN | NaN | NaN |
| Andorra (Principality of) | 3352 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.1898 | Western Europe | 0.000153 | 0.000002 | 0.000009 | 0.000003 | 0.000029 |
| Austria | 516034.144116 | Aa1 | 0.00376 | 0.04598 | 0.00488 | 0.24 | Western Europe | 0.023493 | 0.000088 | 0.00108 | 0.000115 | 0.005638 |
| Belgium | 632216.577075 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.25 | Western Europe | 0.028783 | 0.000162 | 0.001394 | 0.000211 | 0.007196 |
| Cyprus | 32229.622669 | Baa2 | 0.017915 | 0.064354 | 0.023254 | 0.125 | Western Europe | 0.001467 | 0.000026 | 0.000094 | 0.000034 | 0.000183 |
| Denmark | 404198.757538 | Aaa | 0 | 0.0411 | 0 | 0.22 | Western Europe | 0.018402 | 0 | 0.000756 | 0.000000 | 0.004048 |
| Finland | 300187.202696 | Aa1 | 0.00376 | 0.04598 | 0.00488 | 0.2 | Western Europe | 0.013667 | 0.000051 | 0.000628 | 0.000067 | 0.002733 |
| France | 3030904.089608 | Aa2 | 0.004645 | 0.047129 | 0.006029 | 0.25 | Western Europe | 0.137988 | 0.000641 | 0.006503 | 0.000832 | 0.034497 |
| Germany | 4456081.016706 | Aaa | 0 | 0.0411 | 0 | 0.3 | Western Europe | 0.202872 | 0 | 0.008338 | 0.000000 | 0.060862 |
| Greece | 238206.312633 | Ba1 | 0.023554 | 0.071675 | 0.030575 | 0.22 | Western Europe | 0.010845 | 0.000255 | 0.000777 | 0.000332 | 0.002386 |
| Guernsey (States of) | 3446 | A1 | 0.006635 | 0.049713 | 0.008613 | 0 | Western Europe | 0.000157 | 0.000001 | 0.000008 | 0.000001 | 0.000000 |
| Iceland | 31020.032583 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.2 | Western Europe | 0.001412 | 0.000011 | 0.000073 | 0.000015 | 0.000282 |
| Ireland | 545629.450404 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.125 | Western Europe | 0.024841 | 0.00014 | 0.001203 | 0.000182 | 0.003105 |
| Isle of Man | 0 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0 | Western Europe | 0 | 0 | 0 | 0.000000 | 0.000000 |
| Italy | 2254851.212732 | Baa3 | 0.020679 | 0.067943 | 0.026843 | 0.24 | Western Europe | 0.102657 | 0.002123 | 0.006975 | 0.002756 | 0.024638 |
| Jersey (States of) | 4890 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0 | Western Europe | 0.000223 | 0.000001 | 0.000011 | 0.000002 | 0.000000 |
| Liechtenstein | 7364.654515 | Aaa | 0 | 0.0411 | 0 | 0.125 | Western Europe | 0.000335 | 0 | 0.000014 | 0.000000 | 0.000042 |
| Luxembourg | 85755.006124 | Aaa | 0 | 0.0411 | 0 | 0.2494 | Western Europe | 0.003904 | 0 | 0.00016 | 0.000000 | 0.000974 |
| Malta | 20956.999452 | A2 | 0.007962 | 0.051435 | 0.010335 | 0.35 | Western Europe | 0.000954 | 0.000008 | 0.000049 | 0.000010 | 0.000334 |
| Netherlands | 1118124.749886 | Aaa | 0 | 0.0411 | 0 | 0.258 | Western Europe | 0.050905 | 0 | 0.002092 | 0.000000 | 0.013133 |
| Norway | 485513.316504 | Aaa | 0 | 0.0411 | 0 | 0.22 | Western Europe | 0.022104 | 0 | 0.000908 | 0.000000 | 0.004863 |
| Portugal | 287080.013574 | A3 | 0.01128 | 0.055741 | 0.014641 | 0.21 | Western Europe | 0.01307 | 0.000147 | 0.000729 | 0.000191 | 0.002745 |
| Spain | 1580694.712516 | Baa1 | 0.015039 | 0.060622 | 0.019522 | 0.25 | Western Europe | 0.071964 | 0.001082 | 0.004363 | 0.001405 | 0.017991 |
| Sweden | 593267.701033 | Aaa | 0 | 0.0411 | 0 | 0.206 | Western Europe | 0.02701 | 0 | 0.00111 | 0.000000 | 0.005564 |
| Switzerland | 884940.40223 | Aaa | 0 | 0.0411 | 0 | 0.146 | Western Europe | 0.040289 | 0 | 0.001656 | 0.000000 | 0.005882 |
| Turkey | 1108022.37326 | B3 | 0.061153 | 0.120479 | 0.079379 | 0.25 | Western Europe | 0.050445 | 0.003085 | 0.006078 | 0.004004 | 0.012611 |
| United Kingdom | 3340032.380668 | Aa3 | 0.00564 | 0.048421 | 0.007321 | 0.25 | Western Europe | 0.152062 | 0.000858 | 0.007363 | 0.001113 | 0.038015 |
| Western Europe | 21964998.728522 | NaN | 0.008683 | 0.052371 | 0.011271 | 0.247752 | NaN | 1 | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Region | Weighted Average: ERP | Weighted Average: CRP | Weighted Average: Default Spreads | Tax Rate | Total GDP | Weight | Weight \*ERP | Weight\*CRP | Weight\*Default Spread | Weight\* Tax Rate | NaN | NaN |
| Africa | 0.116837 | 0.075737 | 0.058347 | 0.274219 | 2349249.426763 | 0.022606 | 0.002641 | 0.001712 | 0.001319 | 0.006199 | NaN | NaN |
| Asia | 0.055122 | 0.014022 | 0.010802 | 0.257408 | 33117508.476822 | 0.318676 | 0.017566 | 0.004468 | 0.003442 | 0.08203 | NaN | NaN |
| Australia & New Zealand | 0.041139 | 0.000039 | 0.00003 | 0.297436 | 1978706.918567 | 0.01904 | 0.000783 | 0.000001 | 0.000001 | 0.005663 | NaN | NaN |
| Caribbean | 0.11524 | 0.07414 | 0.057117 | 0.25228 | 352610.570167 | 0.003393 | 0.000391 | 0.000252 | 0.000194 | 0.000856 | NaN | NaN |
| Central and South America | 0.087779 | 0.046679 | 0.035961 | 0.31554 | 6318352.475979 | 0.060799 | 0.005337 | 0.002838 | 0.002186 | 0.019184 | NaN | NaN |
| Eastern Europe & Russia | 0.074852 | 0.033713 | 0.025972 | 0.183083 | 5194394.012266 | 0.049984 | 0.003741 | 0.001685 | 0.001298 | 0.009151 | NaN | NaN |
| Middle East | 0.059317 | 0.018217 | 0.014034 | 0.189377 | 3145219.422498 | 0.030265 | 0.001795 | 0.000551 | 0.000425 | 0.005732 | NaN | NaN |
| North America | 0.0411 | 0 | 0 | 0.251088 | 29501020.567791 | 0.283876 | 0.011667 | 0 | 0 | 0.071278 | NaN | NaN |
| Western Europe | 0.052371 | 0.011271 | 0.008683 | 0.247752 | 21964998.728522 | 0.21136 | 0.011069 | 0.002382 | 0.001835 | 0.052365 | NaN | NaN |
| Global | 0.054992 | 0.01389 | 0.0107 | 0.252458 | 103922060.599376 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For updating industry average spreadsheets | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | ERP | Default Spread | Tax rate | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Africa & Mid East | 0.083911 | 0.032981 | 0.225653 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Australia, NZ & Canada | 0.041119 | 0.000015 | 0.280583 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Latin America & Caribbean | 0.089231 | 0.037002 | 0.312196 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Japan | 0.049713 | 0.006635 | 0.3062 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| US | 0.0411 | 0 | 0.25 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Europe | 0.052371 | 0.008683 | 0.247752 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Emerging Markets | 0.066167 | 0.019308 | 0.248749 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Small Asia (No India, China & Japan) | 0.064848 | 0.018218 | 0.227656 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| India | 0.067943 | 0.020679 | 0.3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| China | 0.049713 | 0.006635 | 0.25 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Global | 0.054992 | 0.0107 | 0.252458 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| For other regional groupings | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | ERP | Default Spread | Tax rate | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| EMEA | 0.058682 | 0.013545 | 0.24333 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Regional breakdown
| Country | GDP (in millions) in 2023 | Moody's rating | Sovereign CDS | Adj. Default Spread | Equity Risk Premium | Country Risk Premium | Corporate Tax Rate | Region |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | 3.100000e+05 | Aa2 | 0.0073 | 0.004645 | 0.047229 | 0.006029 | 0.1500 | Middle East |
| Albania | 2.297768e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.1500 | Eastern Europe & Russia |
| Andorra (Principality of) | 3.352000e+03 | Baa1 | NaN | 0.015039 | 0.060722 | 0.019522 | 0.1898 | Western Europe |
| Angola | 8.472296e+04 | B3 | 0.0678 | 0.061153 | 0.120579 | 0.079379 | 0.2500 | Africa |
| Argentina | 6.405914e+05 | Ca | NaN | 0.112906 | 0.187758 | 0.146558 | 0.3500 | Central and South America |
| Armenia | 2.421213e+04 | Ba3 | NaN | 0.033839 | 0.085124 | 0.043924 | 0.1800 | Eastern Europe & Russia |
| Aruba | 3.544708e+03 | Baa3 | NaN | 0.020679 | 0.068043 | 0.026843 | 0.2500 | Caribbean |
| Australia | 1.723827e+06 | Aaa | 0.0019 | 0.000000 | 0.041200 | 0.000000 | 0.3000 | Australia & New Zealand |
| Austria | 5.160341e+05 | Aa1 | 0.0023 | 0.003760 | 0.046080 | 0.004880 | 0.2400 | Western Europe |
| Azerbaijan | 7.235618e+04 | Ba1 | NaN | 0.023554 | 0.071775 | 0.030575 | 0.2000 | Eastern Europe & Russia |
| Bahamas | 1.121000e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.0000 | Caribbean |
| Bahrain | 4.320500e+04 | B2 | 0.0240 | 0.051753 | 0.108378 | 0.067178 | 0.0000 | Middle East |
| Bangladesh | 4.374153e+05 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.3000 | Asia |
| Barbados | 6.393564e+03 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.0550 | Caribbean |
| Belarus | 7.185738e+04 | C | NaN | 0.175000 | 0.268358 | 0.227158 | 0.1800 | Eastern Europe & Russia |
| Belgium | 6.322166e+05 | Aa3 | 0.0028 | 0.005640 | 0.048521 | 0.007321 | 0.2500 | Western Europe |
| Belize | 3.281500e+03 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.2853 | Central and South America |
| Benin | 1.967328e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.3000 | Africa |
| Bermuda | 7.827980e+03 | A2 | NaN | 0.007962 | 0.051535 | 0.010335 | 0.0000 | Caribbean |
| Bolivia | 4.584983e+04 | Caa3 | NaN | 0.094107 | 0.163355 | 0.122155 | 0.2500 | Central and South America |
| Bosnia and Herzegovina | 2.705489e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.1000 | Eastern Europe & Russia |
| Botswana | 1.939577e+04 | A3 | NaN | 0.011280 | 0.055841 | 0.014641 | 0.2200 | Africa |
| Brazil | 2.173666e+06 | Ba2 | 0.0257 | 0.028310 | 0.077947 | 0.036747 | 0.3400 | Central and South America |
| Bulgaria | 1.015844e+05 | Baa1 | 0.0127 | 0.015039 | 0.060722 | 0.019522 | 0.1000 | Eastern Europe & Russia |
| Burkina Faso | 2.032462e+04 | Caa1 | NaN | 0.070553 | 0.132781 | 0.091581 | 0.2800 | Africa |
| Cambodia | 3.177276e+04 | B2 | NaN | 0.051753 | 0.108378 | 0.067178 | 0.2000 | Asia |
| Cameroon | 4.794551e+04 | Caa1 | 0.0746 | 0.070553 | 0.132781 | 0.091581 | 0.3300 | Africa |
| Canada | 2.140086e+06 | Aaa | 0.0038 | 0.000000 | 0.041200 | 0.000000 | 0.2650 | North America |
| Cape Verde | 1.936000e+03 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.0000 | Africa |
| Cayman Islands | 6.600844e+03 | Aa3 | NaN | 0.005640 | 0.048521 | 0.007321 | 0.0000 | Caribbean |
| Chile | 3.355333e+05 | A2 | 0.0103 | 0.007962 | 0.051535 | 0.010335 | 0.2700 | Central and South America |
| China | 1.779478e+07 | A1 | 0.0105 | 0.006635 | 0.049813 | 0.008613 | 0.2500 | Asia |
| Colombia | 3.635402e+05 | Baa2 | 0.0310 | 0.017915 | 0.064454 | 0.023254 | 0.3500 | Central and South America |
| Congo (Democratic Republic of) | 6.638329e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.3000 | Africa |
| Congo (Republic of) | 1.532106e+04 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.2800 | Africa |
| Cook Islands | 1.414000e+03 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.2974 | Australia & New Zealand |
| Costa Rica | 8.649794e+04 | B1 | 0.0229 | 0.042354 | 0.096177 | 0.054977 | 0.3000 | Central and South America |
| Côte d'Ivoire | 7.878883e+04 | Ba2 | NaN | 0.028310 | 0.077947 | 0.036747 | 0.2500 | Africa |
| Croatia | 8.268884e+04 | Baa2 | 0.0124 | 0.017915 | 0.064454 | 0.023254 | 0.1800 | Eastern Europe & Russia |
| Cuba | 1.073510e+05 | Ca | NaN | 0.112906 | 0.187758 | 0.146558 | 0.2853 | Caribbean |
| Curacao | 3.073840e+03 | Baa3 | NaN | 0.020679 | 0.068043 | 0.026843 | 0.2200 | Caribbean |
| Cyprus | 3.222962e+04 | Baa2 | 0.0093 | 0.017915 | 0.064454 | 0.023254 | 0.1250 | Western Europe |
| Czech Republic | 3.308583e+05 | Aa3 | 0.0046 | 0.005640 | 0.048521 | 0.007321 | 0.1900 | Eastern Europe & Russia |
| Denmark | 4.041988e+05 | Aaa | 0.0017 | 0.000000 | 0.041200 | 0.000000 | 0.2200 | Western Europe |
| Dominican Republic | 1.214443e+05 | Ba3 | NaN | 0.033839 | 0.085124 | 0.043924 | 0.2700 | Caribbean |
| Ecuador | 1.188448e+05 | Caa3 | 0.2197 | 0.094107 | 0.163355 | 0.122155 | 0.2500 | Central and South America |
| Egypt | 3.959261e+05 | Caa1 | 0.0670 | 0.070553 | 0.132781 | 0.091581 | 0.2250 | Africa |
| El Salvador | 3.401562e+04 | Caa1 | 0.0750 | 0.070553 | 0.132781 | 0.091581 | 0.3000 | Central and South America |
| Estonia | 4.074485e+04 | A1 | 0.0077 | 0.006635 | 0.049813 | 0.008613 | 0.2000 | Eastern Europe & Russia |
| Ethiopia | 1.636979e+05 | Caa2 | 0.3159 | 0.084707 | 0.151154 | 0.109954 | 0.3000 | Africa |
| Fiji | 5.494798e+03 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.2000 | Asia |
| Finland | 3.001872e+05 | Aa1 | 0.0029 | 0.003760 | 0.046080 | 0.004880 | 0.2000 | Western Europe |
| France | 3.030904e+06 | Aa2 | 0.0051 | 0.004645 | 0.047229 | 0.006029 | 0.2500 | Western Europe |
| Gabon | 2.051613e+04 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.3000 | Africa |
| Georgia | 3.053553e+04 | Ba2 | NaN | 0.028310 | 0.077947 | 0.036747 | 0.1500 | Eastern Europe & Russia |
| Germany | 4.456081e+06 | Aaa | 0.0020 | 0.000000 | 0.041200 | 0.000000 | 0.3000 | Western Europe |
| Ghana | 7.637039e+04 | Caa3 | NaN | 0.094107 | 0.163355 | 0.122155 | 0.2500 | Africa |
| Greece | 2.382063e+05 | Ba1 | 0.0131 | 0.023554 | 0.071775 | 0.030575 | 0.2200 | Western Europe |
| Guatemala | 1.020505e+05 | Ba1 | NaN | 0.023554 | 0.071775 | 0.030575 | 0.2500 | Central and South America |
| Guernsey (States of) | 3.446000e+03 | A1 | NaN | 0.006635 | 0.049813 | 0.008613 | 0.0000 | Western Europe |
| Honduras | 3.440051e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.2500 | Central and South America |
| Hong Kong | 3.820546e+05 | Aa3 | 0.0053 | 0.005640 | 0.048521 | 0.007321 | 0.1650 | Asia |
| Hungary | 2.123889e+05 | Baa2 | 0.0167 | 0.017915 | 0.064454 | 0.023254 | 0.0900 | Eastern Europe & Russia |
| Iceland | 3.102003e+04 | A2 | 0.0060 | 0.007962 | 0.051535 | 0.010335 | 0.2000 | Western Europe |
| India | 3.549919e+06 | Baa3 | 0.0083 | 0.020679 | 0.068043 | 0.026843 | 0.3000 | Asia |
| Indonesia | 1.371171e+06 | Baa2 | 0.0128 | 0.017915 | 0.064454 | 0.023254 | 0.2200 | Asia |
| Iraq | 2.508428e+05 | Caa1 | 0.0395 | 0.070553 | 0.132781 | 0.091581 | 0.1500 | Middle East |
| Ireland | 5.456295e+05 | Aa3 | 0.0031 | 0.005640 | 0.048521 | 0.007321 | 0.1250 | Western Europe |
| Isle of Man | 0.000000e+00 | Aa3 | NaN | 0.005640 | 0.048521 | 0.007321 | 0.0000 | Western Europe |
| Israel | 5.099015e+05 | A2 | 0.0173 | 0.007962 | 0.051535 | 0.010335 | 0.2300 | Middle East |
| Italy | 2.254851e+06 | Baa3 | 0.0129 | 0.020679 | 0.068043 | 0.026843 | 0.2400 | Western Europe |
| Jamaica | 1.942336e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.2500 | Caribbean |
| Japan | 4.212945e+06 | A1 | 0.0035 | 0.006635 | 0.049813 | 0.008613 | 0.3062 | Asia |
| Jersey (States of) | 4.890000e+03 | Aa3 | NaN | 0.005640 | 0.048521 | 0.007321 | 0.0000 | Western Europe |
| Jordan | 5.081364e+04 | Ba3 | NaN | 0.033839 | 0.085124 | 0.043924 | 0.2000 | Middle East |
| Kazakhstan | 2.614211e+05 | Baa2 | 0.0137 | 0.017915 | 0.064454 | 0.023254 | 0.2000 | Eastern Europe & Russia |
| Kenya | 1.074406e+05 | B3 | 0.0542 | 0.061153 | 0.120579 | 0.079379 | 0.3000 | Africa |
| Korea | 1.712793e+06 | Aa2 | 0.0045 | 0.004645 | 0.047229 | 0.006029 | 0.2500 | Asia |
| Kuwait | 1.100000e+04 | A1 | 0.0083 | 0.006635 | 0.049813 | 0.008613 | 0.1500 | Middle East |
| Kyrgyzstan | 1.398763e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.1000 | Eastern Europe & Russia |
| Laos | 1.584316e+04 | Caa3 | NaN | 0.094107 | 0.163355 | 0.122155 | 0.2686 | Asia |
| Latvia | 4.362708e+04 | A3 | 0.0086 | 0.011280 | 0.055841 | 0.014641 | 0.2000 | Eastern Europe & Russia |
| Lebanon | 1.793726e+04 | C | NaN | 0.175000 | 0.268358 | 0.227158 | 0.1700 | Middle East |
| Liechtenstein | 7.364655e+03 | Aaa | NaN | 0.000000 | 0.041200 | 0.000000 | 0.1250 | Western Europe |
| Lithuania | 7.783640e+04 | A2 | 0.0087 | 0.007962 | 0.051535 | 0.010335 | 0.1500 | Eastern Europe & Russia |
| Luxembourg | 8.575501e+04 | Aaa | NaN | 0.000000 | 0.041200 | 0.000000 | 0.2494 | Western Europe |
| Macao | 4.706184e+04 | Aa3 | NaN | 0.005640 | 0.048521 | 0.007321 | 0.2686 | Asia |
| Macedonia | 1.476124e+04 | Ba3 | NaN | 0.033839 | 0.085124 | 0.043924 | 0.1000 | Eastern Europe & Russia |
| Malaysia | 3.996488e+05 | A3 | 0.0081 | 0.011280 | 0.055841 | 0.014641 | 0.2400 | Asia |
| Maldives | 6.600000e+03 | Caa1 | NaN | 0.070553 | 0.132781 | 0.091581 | 0.2686 | Asia |
| Mali | 2.090490e+04 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.2686 | Africa |
| Malta | 2.095700e+04 | A2 | NaN | 0.007962 | 0.051535 | 0.010335 | 0.3500 | Western Europe |
| Mauritius | 1.439713e+04 | Baa3 | NaN | 0.020679 | 0.068043 | 0.026843 | 0.1500 | Africa |
| Mexico | 1.788887e+06 | Baa2 | 0.0176 | 0.017915 | 0.064454 | 0.023254 | 0.3000 | Central and South America |
| Moldova | 1.653944e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.1200 | Eastern Europe & Russia |
| Mongolia | 1.987218e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.2500 | Asia |
| Montenegro | 7.404542e+03 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.1500 | Eastern Europe & Russia |
| Montserrat | 1.619900e+04 | Baa3 | NaN | 0.020679 | 0.068043 | 0.026843 | 0.2853 | Caribbean |
| Morocco | 1.411094e+05 | Ba1 | 0.0135 | 0.023554 | 0.071775 | 0.030575 | 0.3200 | Africa |
| Mozambique | 2.062460e+04 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.3200 | Africa |
| Namibia | 1.235102e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.3200 | Africa |
| Netherlands | 1.118125e+06 | Aaa | 0.0019 | 0.000000 | 0.041200 | 0.000000 | 0.2580 | Western Europe |
| New Zealand | 2.534657e+05 | Aaa | 0.0021 | 0.000000 | 0.041200 | 0.000000 | 0.2800 | Australia & New Zealand |
| Nicaragua | 1.782922e+04 | B2 | 0.0624 | 0.051753 | 0.108378 | 0.067178 | 0.3000 | Central and South America |
| Niger | 1.681917e+04 | Caa3 | NaN | 0.094107 | 0.163355 | 0.122155 | 0.2686 | Africa |
| Nigeria | 3.628150e+05 | Caa1 | 0.0634 | 0.070553 | 0.132781 | 0.091581 | 0.3000 | Africa |
| Norway | 4.855133e+05 | Aaa | 0.0017 | 0.000000 | 0.041200 | 0.000000 | 0.2200 | Western Europe |
| Oman | 1.081925e+05 | Ba1 | 0.0149 | 0.023554 | 0.071775 | 0.030575 | 0.1500 | Middle East |
| Pakistan | 3.383685e+05 | Caa3 | 0.1678 | 0.094107 | 0.163355 | 0.122155 | 0.2900 | Asia |
| Panama | 8.338240e+04 | Baa3 | 0.0261 | 0.020679 | 0.068043 | 0.026843 | 0.2500 | Central and South America |
| Papua New Guinea | 3.093250e+04 | B2 | NaN | 0.051753 | 0.108378 | 0.067178 | 0.3000 | Asia |
| Paraguay | 4.295626e+04 | Ba1 | NaN | 0.023554 | 0.071775 | 0.030575 | 0.1000 | Central and South America |
| Peru | 2.676032e+05 | Baa1 | 0.0128 | 0.015039 | 0.060722 | 0.019522 | 0.2950 | Central and South America |
| Philippines | 4.371464e+05 | Baa2 | 0.0122 | 0.017915 | 0.064454 | 0.023254 | 0.2500 | Asia |
| Poland | 8.112291e+05 | A2 | 0.0101 | 0.007962 | 0.051535 | 0.010335 | 0.1900 | Eastern Europe & Russia |
| Portugal | 2.870800e+05 | A3 | 0.0066 | 0.011280 | 0.055841 | 0.014641 | 0.2100 | Western Europe |
| Qatar | 2.357704e+05 | Aa2 | 0.0071 | 0.004645 | 0.047229 | 0.006029 | 0.1000 | Middle East |
| Ras Al Khaimah (Emirate of) | 1.100000e+04 | A3 | NaN | 0.011280 | 0.055841 | 0.014641 | 0.0000 | Middle East |
| Romania | 3.510026e+05 | Baa3 | 0.0198 | 0.020679 | 0.068043 | 0.026843 | 0.1600 | Eastern Europe & Russia |
| Russia | 2.021421e+06 | NaN | NaN | 0.028310 | 0.077947 | 0.036747 | 0.2000 | Eastern Europe & Russia |
| Rwanda | 1.409777e+04 | B2 | NaN | 0.051753 | 0.108378 | 0.067178 | 0.3000 | Africa |
| Saudi Arabia | 1.067583e+06 | A1 | 0.0082 | 0.006635 | 0.049813 | 0.008613 | 0.2000 | Middle East |
| Senegal | 3.101399e+04 | Ba3 | 0.0536 | 0.033839 | 0.085124 | 0.043924 | 0.3000 | Africa |
| Serbia | 7.518713e+04 | Ba2 | 0.0233 | 0.028310 | 0.077947 | 0.036747 | 0.1500 | Eastern Europe & Russia |
| Sharjah | 2.480000e+04 | Ba1 | NaN | 0.023554 | 0.071775 | 0.030575 | 0.0000 | Middle East |
| Singapore | 5.014275e+05 | Aaa | NaN | 0.000000 | 0.041200 | 0.000000 | 0.1700 | Asia |
| Slovakia | 1.327936e+05 | A2 | 0.0048 | 0.007962 | 0.051535 | 0.010335 | 0.2100 | Eastern Europe & Russia |
| Slovenia | 6.821678e+04 | A3 | 0.0061 | 0.011280 | 0.055841 | 0.014641 | 0.1900 | Eastern Europe & Russia |
| Solomon Islands | 1.631287e+03 | Caa1 | NaN | 0.070553 | 0.132781 | 0.091581 | 0.3000 | Asia |
| South Africa | 3.777816e+05 | Ba2 | 0.0317 | 0.028310 | 0.077947 | 0.036747 | 0.2700 | Africa |
| Spain | 1.580695e+06 | Baa1 | 0.0068 | 0.015039 | 0.060722 | 0.019522 | 0.2500 | Western Europe |
| Sri Lanka | 8.435686e+04 | Ca | NaN | 0.112906 | 0.187758 | 0.146558 | 0.2400 | Asia |
| St. Maarten | 1.190000e+04 | Ba2 | NaN | 0.028310 | 0.077947 | 0.036747 | 0.2853 | Caribbean |
| St. Vincent & the Grenadines | 8.100000e+03 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.2853 | Caribbean |
| Suriname | 3.782437e+03 | Caa3 | NaN | 0.094107 | 0.163355 | 0.122155 | 0.3600 | Central and South America |
| Swaziland | 4.597856e+03 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.2750 | Africa |
| Sweden | 5.932677e+05 | Aaa | 0.0020 | 0.000000 | 0.041200 | 0.000000 | 0.2060 | Western Europe |
| Switzerland | 8.849404e+05 | Aaa | 0.0008 | 0.000000 | 0.041200 | 0.000000 | 0.1460 | Western Europe |
| Taiwan | 7.916100e+05 | Aa3 | NaN | 0.005640 | 0.048521 | 0.007321 | 0.2000 | Asia |
| Tajikistan | 1.206060e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.1800 | Eastern Europe & Russia |
| Tanzania | 7.915829e+04 | B1 | NaN | 0.042354 | 0.096177 | 0.054977 | 0.3000 | Africa |
| Thailand | 5.149450e+05 | Baa1 | 0.0069 | 0.015039 | 0.060722 | 0.019522 | 0.2000 | Asia |
| Togo | 9.171262e+03 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.2686 | Africa |
| Trinidad and Tobago | 2.813994e+04 | Ba2 | NaN | 0.028310 | 0.077947 | 0.036747 | 0.3000 | Caribbean |
| Tunisia | 4.852960e+04 | Caa2 | 0.0789 | 0.084707 | 0.151154 | 0.109954 | 0.1500 | Africa |
| Turkey | 1.108022e+06 | B3 | 0.0377 | 0.061153 | 0.120579 | 0.079379 | 0.2500 | Western Europe |
| Turks and Caicos Islands | 1.402054e+03 | Baa1 | NaN | 0.015039 | 0.060722 | 0.019522 | 0.0000 | Caribbean |
| Uganda | 4.927288e+04 | B3 | NaN | 0.061153 | 0.120579 | 0.079379 | 0.3000 | Africa |
| Ukraine | 1.787570e+05 | Ca | NaN | 0.112906 | 0.187758 | 0.146558 | 0.1800 | Eastern Europe & Russia |
| United Arab Emirates | 5.041735e+05 | Aa2 | NaN | 0.004645 | 0.047229 | 0.006029 | 0.2500 | Middle East |
| United Kingdom | 3.340032e+06 | Aa3 | 0.0042 | 0.005640 | 0.048521 | 0.007321 | 0.2500 | Western Europe |
| United States | 2.736094e+07 | Aaa | 0.0046 | 0.000000 | 0.041200 | 0.000000 | 0.2500 | North America |
| Uruguay | 7.724083e+04 | Baa1 | 0.0108 | 0.015039 | 0.060722 | 0.019522 | 0.2500 | Central and South America |
| Uzbekistan | 9.088915e+04 | Ba3 | NaN | 0.033839 | 0.085124 | 0.043924 | 0.1500 | Eastern Europe & Russia |
| Venezuela | 9.840000e+04 | C | 0.1029 | 0.175000 | 0.268358 | 0.227158 | 0.3400 | Central and South America |
| Vietnam | 4.297170e+05 | Ba2 | 0.0176 | 0.028310 | 0.077947 | 0.036747 | 0.2000 | Asia |
| Zambia | 2.816263e+04 | Caa2 | NaN | 0.084707 | 0.151154 | 0.109954 | 0.3500 | Africa |

## Sovereign Ratings (Moody's,S&P)
| Country | S&P Rating | Moody's rating | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | AA | Aa2 | NaN | NaN | GOVERNMENT BOND RATINGS | NaN |
| Albania | BB- | B1 | NaN | NaN | In local currency | NaN |
| Andorra (Principality of) | BBB+ | Baa1 | NaN | NaN | S&P: These are the S&P sovereign local currency ratings | NaN |
| Angola | B- | B3 | NaN | NaN | Moody's: These are the Moody's local currency rating | NaN |
| Argentina | CCC | Ca | NaN | NaN | In red: These are countries where S&P has a rating and Moody's does not. The following lookup table is used to estimate the | NaN |
| Armenia | BB- | Ba3 | NaN | NaN | Moody's equivalent rating for these countries. | NaN |
| Aruba | BBB | Baa3 | NaN | NaN | S&P | Moody's |
| Australia | AAA | Aaa | NaN | NaN | A | A2 |
| Austria | AA+ | Aa1 | NaN | NaN | A- | A3 |
| Azerbaijan | BB+ | Ba1 | NaN | NaN | A+ | A1 |
| Bahamas | B+ | B1 | NaN | NaN | AA | Aa2 |
| Bahrain | B+ | B2 | NaN | NaN | AA- | Aa3 |
| Bangladesh | BB- | B1 | NaN | NaN | AA+ | Aa1 |
| Barbados | B- | B3 | NaN | NaN | AAA | Aaa |
| Belarus | NR | C | NaN | NaN | B | B2 |
| Belgium | AA | Aa3 | NaN | NaN | B- | B3 |
| Belize | B- | Caa2 | NaN | NaN | B+ | B1 |
| Benin | B+ | B1 | NaN | NaN | BB | Ba2 |
| Bermuda | A+ | A2 | NaN | NaN | BB- | Ba3 |
| Bolivia | CCC+ | Caa3 | NaN | NaN | BB+ | Ba1 |
| Bosnia and Herzegovina | B+ | B3 | NaN | NaN | BBB | Baa2 |
| Botswana | BBB+ | A3 | NaN | NaN | BBB- | Baa3 |
| Brazil | BB | Ba2 | NaN | NaN | BBB+ | Baa1 |
| Bulgaria | BBB | Baa1 | NaN | NaN | C | C2 |
| Burkina Faso | CCC+ | Caa1 | NaN | NaN | C- | C3 |
| Cambodia | NR | B2 | NaN | NaN | C+ | C1 |
| Cameroon | B- | Caa1 | NaN | NaN | CC | Ca2 |
| Canada | AAA | Aaa | NaN | NaN | CC- | Ca3 |
| Cape Verde | B- | B3 | NaN | NaN | CC+ | Ca1 |
| Cayman Islands | NR | Aa3 | NaN | NaN | CCC | Caa2 |
| Chile | A | A2 | NaN | NaN | CCC- | Caa3 |
| China | A+ | A1 | NaN | NaN | CCC+ | Caa1 |
| Colombia | BB+ | Baa2 | NaN | NaN | NaN | NaN |
| Congo (Democratic Republic of) | B- | B3 | NaN | NaN | NaN | NaN |
| Congo (Republic of) | B- | Caa2 | NaN | NaN | NaN | NaN |
| Cook Islands | B+ | B1 | NaN | NaN | NaN | NaN |
| Costa Rica | BB- | B1 | NaN | NaN | NaN | NaN |
| Côte d'Ivoire | BB- | Ba2 | NaN | NaN | NaN | NaN |
| Croatia | BBB+ | Baa2 | NaN | NaN | NaN | NaN |
| Cuba | NR | Ca | NaN | NaN | NaN | NaN |
| Curacao | BBB- | Baa3 | NaN | NaN | NaN | NaN |
| Cyprus | BBB | Baa2 | NaN | NaN | NaN | NaN |
| Czech Republic | AA- | Aa3 | NaN | NaN | NaN | NaN |
| Denmark | AAA | Aaa | NaN | NaN | NaN | NaN |
| Dominican Republic | BB | Ba3 | NaN | NaN | NaN | NaN |
| Ecuador | B- | Caa3 | NaN | NaN | NaN | NaN |
| Egypt | B- | Caa1 | NaN | NaN | NaN | NaN |
| El Salvador | B- | Caa1 | NaN | NaN | NaN | NaN |
| Estonia | AA- | A1 | NaN | NaN | NaN | NaN |
| Ethiopia | SD | Caa2 | NaN | NaN | NaN | NaN |
| Fiji | B+ | B1 | NaN | NaN | NaN | NaN |
| Finland | AA+ | Aa1 | NaN | NaN | NaN | NaN |
| France | AA | Aa2 | NaN | NaN | NaN | NaN |
| Gabon | NR | Caa2 | NaN | NaN | NaN | NaN |
| Georgia | BB | Ba2 | NaN | NaN | NaN | NaN |
| Germany | AAA | Aaa | NaN | NaN | NaN | NaN |
| Ghana | SD | Caa3 | NaN | NaN | NaN | NaN |
| Greece | BBB- | Ba1 | NaN | NaN | NaN | NaN |
| Guatemala | BB | Ba1 | NaN | NaN | NaN | NaN |
| Guernsey (States of) | A+ | A1 | NaN | NaN | NaN | NaN |
| Honduras | BB- | B1 | NaN | NaN | NaN | NaN |
| Hong Kong | AA+ | Aa3 | NaN | NaN | NaN | NaN |
| Hungary | BBB- | Baa2 | NaN | NaN | NaN | NaN |
| Iceland | A+ | A2 | NaN | NaN | NaN | NaN |
| India | BBB- | Baa3 | NaN | NaN | NaN | NaN |
| Indonesia | BBB | Baa2 | NaN | NaN | NaN | NaN |
| Iraq | B- | Caa1 | NaN | NaN | NaN | NaN |
| Ireland | AA | Aa3 | NaN | NaN | NaN | NaN |
| Isle of Man | NR | Aa3 | NaN | NaN | NaN | NaN |
| Israel | AA- | A2 | NaN | NaN | NaN | NaN |
| Italy | BBB | Baa3 | NaN | NaN | NaN | NaN |
| Jamaica | BB- | B1 | NaN | NaN | NaN | NaN |
| Japan | A+ | A1 | NaN | NaN | NaN | NaN |
| Jersey (States of) | AA- | Aa3 | NaN | NaN | NaN | NaN |
| Jordan | B+ | Ba3 | NaN | NaN | NaN | NaN |
| Kazakhstan | BBB- | Baa2 | NaN | NaN | NaN | NaN |
| Kenya | B | B3 | NaN | NaN | NaN | NaN |
| Korea | AA | Aa2 | NaN | NaN | NaN | NaN |
| Kuwait | A+ | A1 | NaN | NaN | NaN | NaN |
| Kyrgyzstan | NR | B3 | NaN | NaN | NaN | NaN |
| Laos | NR | Caa3 | NaN | NaN | NaN | NaN |
| Latvia | A+ | A3 | NaN | NaN | NaN | NaN |
| Lebanon | NR | C | NaN | NaN | NaN | NaN |
| Liechtenstein | AAA | Aaa | NaN | NaN | NaN | NaN |
| Lithuania | A+ | A2 | NaN | NaN | NaN | NaN |
| Luxembourg | AAA | Aaa | NaN | NaN | NaN | NaN |
| Macao | NR | Aa3 | NaN | NaN | NaN | NaN |
| Macedonia | BB- | Ba3 | NaN | NaN | NaN | NaN |
| Malaysia | A- | A3 | NaN | NaN | NaN | NaN |
| Maldives | NR | Caa1 | NaN | NaN | NaN | NaN |
| Mali | NR | Caa2 | NaN | NaN | NaN | NaN |
| Malta | A- | A2 | NaN | NaN | NaN | NaN |
| Mauritius | BBB- | Baa3 | NaN | NaN | NaN | NaN |
| Mexico | BBB | Baa2 | NaN | NaN | NaN | NaN |
| Moldova | NR | B3 | NaN | NaN | NaN | NaN |
| Mongolia | B | B3 | NaN | NaN | NaN | NaN |
| Montenegro | B | B1 | NaN | NaN | NaN | NaN |
| Montserrat | BBB- | Baa3 | NaN | NaN | NaN | NaN |
| Morocco | BB+ | Ba1 | NaN | NaN | NaN | NaN |
| Mozambique | CCC+ | Caa2 | NaN | NaN | NaN | NaN |
| Namibia | NR | B1 | NaN | NaN | NaN | NaN |
| Netherlands | AAA | Aaa | NaN | NaN | NaN | NaN |
| New Zealand | AA+ | Aaa | NaN | NaN | NaN | NaN |
| Nicaragua | B | B2 | NaN | NaN | NaN | NaN |
| Niger | NR | Caa3 | NaN | NaN | NaN | NaN |
| Nigeria | B- | Caa1 | NaN | NaN | NaN | NaN |
| Norway | AAA | Aaa | NaN | NaN | NaN | NaN |
| Oman | BB+ | Ba1 | NaN | NaN | NaN | NaN |
| Pakistan | CCC+ | Caa3 | NaN | NaN | NaN | NaN |
| Panama | BBB | Baa3 | NaN | NaN | NaN | NaN |
| Papua New Guinea | B- | B2 | NaN | NaN | NaN | NaN |
| Paraguay | BB+ | Ba1 | NaN | NaN | NaN | NaN |
| Peru | BBB | Baa1 | NaN | NaN | NaN | NaN |
| Philippines | BBB+ | Baa2 | NaN | NaN | NaN | NaN |
| Poland | A- | A2 | NaN | NaN | NaN | NaN |
| Portugal | A- | A3 | NaN | NaN | NaN | NaN |
| Qatar | AA | Aa2 | NaN | NaN | NaN | NaN |
| Ras Al Khaimah (Emirate of) | A- | A3 | NaN | NaN | NaN | NaN |
| Romania | BBB- | Baa3 | NaN | NaN | NaN | NaN |
| Russia | NR | NaN | NaN | NaN | NaN | NaN |
| Rwanda | B+ | B2 | NaN | NaN | NaN | NaN |
| Saudi Arabia | A | A1 | NaN | NaN | NaN | NaN |
| Senegal | B+ | Ba3 | NaN | NaN | NaN | NaN |
| Serbia | BB+ | Ba2 | NaN | NaN | NaN | NaN |
| Sharjah | BBB- | Ba1 | NaN | NaN | NaN | NaN |
| Singapore | AAA | Aaa | NaN | NaN | NaN | NaN |
| Slovakia | A+ | A2 | NaN | NaN | NaN | NaN |
| Slovenia | AA- | A3 | NaN | NaN | NaN | NaN |
| Solomon Islands | NR | Caa1 | NaN | NaN | NaN | NaN |
| South Africa | BB- | Ba2 | NaN | NaN | NaN | NaN |
| Spain | A | Baa1 | NaN | NaN | NaN | NaN |
| Sri Lanka | NR | Ca | NaN | NaN | NaN | NaN |
| St. Maarten | NaN | Ba2 | NaN | NaN | NaN | NaN |
| St. Vincent & the Grenadines | NR | B3 | NaN | NaN | NaN | NaN |
| Suriname | CCC+ | Caa3 | NaN | NaN | NaN | NaN |
| Swaziland | NR | B3 | NaN | NaN | NaN | NaN |
| Sweden | AAA | Aaa | NaN | NaN | NaN | NaN |
| Switzerland | AAA | Aaa | NaN | NaN | NaN | NaN |
| Taiwan | AA+ | Aa3 | NaN | NaN | NaN | NaN |
| Tajikistan | B- | B3 | NaN | NaN | NaN | NaN |
| Tanzania | NR | B1 | NaN | NaN | NaN | NaN |
| Thailand | BBB+ | Baa1 | NaN | NaN | NaN | NaN |
| Togo | B | B3 | NaN | NaN | NaN | NaN |
| Trinidad and Tobago | BBB- | Ba2 | NaN | NaN | NaN | NaN |
| Tunisia | NR | Caa2 | NaN | NaN | NaN | NaN |
| Turkey | B | B3 | NaN | NaN | NaN | NaN |
| Turks and Caicos Islands | BBB+ | Baa1 | NaN | NaN | NaN | NaN |
| Uganda | B- | B3 | NaN | NaN | NaN | NaN |
| Ukraine | CC | Ca | NaN | NaN | NaN | NaN |
| United Arab Emirates | NR | Aa2 | NaN | NaN | NaN | NaN |
| United Kingdom | AA | Aa3 | NaN | NaN | NaN | NaN |
| United States | AA+ | Aaa | NaN | NaN | NaN | NaN |
| Uruguay | BBB+ | Baa1 | NaN | NaN | NaN | NaN |
| Uzbekistan | BB- | Ba3 | NaN | NaN | NaN | NaN |
| Venezuela | NR | C | NaN | NaN | NaN | NaN |
| Vietnam | BB+ | Ba2 | NaN | NaN | NaN | NaN |
| Zambia | NR | Caa2 | NaN | NaN | NaN | NaN |

## Regional lookup table
| Country | Region |
| --- | --- |
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
| Iraq | Middle East |
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
| Kyrgyzstan | Eastern Europe & Russia |
| Laos | Asia |
| Latvia | Eastern Europe & Russia |
| Lebanon | Middle East |
| Liechtenstein | Western Europe |
| Lithuania | Eastern Europe & Russia |
| Luxembourg | Western Europe |
| Macao | Asia |
| Macedonia | Eastern Europe & Russia |
| Malaysia | Asia |
| Maldives | Asia |
| Mali | Africa |
| Malta | Western Europe |
| Mauritius | Africa |
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
| Niger | Africa |
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
| Solomon Islands | Asia |
| South Africa | Africa |
| Spain | Western Europe |
| Sri Lanka | Asia |
| St. Maarten | Caribbean |
| St. Vincent & the Grenadines | Caribbean |
| Suriname | Central and South America |
| Swaziland | Africa |
| Sweden | Western Europe |
| Switzerland | Western Europe |
| Taiwan | Asia |
| Tajikistan | Eastern Europe & Russia |
| Tanzania | Africa |
| Thailand | Asia |
| Togo | Africa |
| Trinidad and Tobago | Caribbean |
| Tunisia | Africa |
| Turkey | Western Europe |
| Turkmenistan | Eastern Europe & Russia |
| Turks and Caicos | Caribbean |
| Uganda | Africa |
| Ukraine | Eastern Europe & Russia |
| United Arab Emirates | Middle East |
| United Kingdom | Western Europe |
| United States | North America |
| Uruguay | Central and South America |
| Uzbekistan | Eastern Europe & Russia |
| Venezuela | Central and South America |
| Vietnam | Asia |
| Zambia | Africa |

## Default Spreads for Ratings
| Rating | Default Spread (12/31/23) | Updated Default Spread (7/1/24) | Unnamed: 3 | Country | Moody's rating | 2023-12-31 00:00:00 | 2024-07-01 00:00:00 | CDS % Change | Unnamed: 9 | Country.1 | 2024-07-01 00:00:00.1 | Unnamed: 12 | Country.2 | 2023-12-31 00:00:00.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | 76.826804 | 66.350422 | NaN | Abu Dhabi | Aa2 | 0.0075 | 0.0073 | -0.026667 | NaN | Abu Dhabi | 0.0073 | NaN | Abu Dhabi | 0.0075 |
| A2 | 92.192165 | 79.620506 | NaN | Algeria | NaN | 0.0170 | 0.0145 | -0.147059 | NaN | Algeria | 0.0145 | NaN | Algeria | 0.0170 |
| A3 | 130.605567 | 112.795717 | NaN | Angola | B3 | 0.0782 | 0.0678 | -0.132992 | NaN | Angola | 0.0678 | NaN | Angola | 0.0782 |
| Aa1 | 43.535189 | 37.598572 | NaN | Australia | Aaa | 0.0026 | 0.0019 | -0.269231 | NaN | Argentina | 0.2380 | NaN | Argentina | NaN |
| Aa2 | 53.778763 | 46.445295 | NaN | Austria | Aa1 | 0.0027 | 0.0023 | -0.148148 | NaN | Australia | 0.0019 | NaN | Australia | 0.0026 |
| Aa3 | 65.302783 | 56.397858 | NaN | Bahrain | B2 | 0.0274 | 0.0240 | -0.124088 | NaN | Austria | 0.0023 | NaN | Austria | 0.0027 |
| Aaa | 0.000000 | 0.000000 | NaN | Belgium | Aa3 | 0.0033 | 0.0028 | -0.151515 | NaN | Bahrain | 0.0240 | NaN | Bahrain | 0.0274 |
| B1 | 490.411098 | 423.536857 | NaN | Brazil | Ba2 | 0.0239 | 0.0257 | 0.075314 | NaN | Belgium | 0.0028 | NaN | Belgium | 0.0033 |
| B2 | 599.249070 | 517.533288 | NaN | Bulgaria | Baa1 | 0.0147 | 0.0127 | -0.136054 | NaN | Brazil | 0.0257 | NaN | Brazil | 0.0239 |
| B3 | 708.087042 | 611.529718 | NaN | Cameroon | Caa1 | 0.0914 | 0.0746 | -0.183807 | NaN | Bulgaria | 0.0127 | NaN | Bulgaria | 0.0147 |
| Ba1 | 272.735154 | 235.543996 | NaN | Canada | Aaa | 0.0044 | 0.0038 | -0.136364 | NaN | Cameroon | 0.0746 | NaN | Cameroon | 0.0914 |
| Ba2 | 327.794363 | 283.095132 | NaN | Chile | A2 | 0.0115 | 0.0103 | -0.104348 | NaN | Canada | 0.0038 | NaN | Canada | 0.0044 |
| Ba3 | 391.816700 | 338.387150 | NaN | China | A1 | 0.0099 | 0.0105 | 0.060606 | NaN | Chile | 0.0103 | NaN | Chile | 0.0115 |
| Baa1 | 174.140755 | 150.394289 | NaN | Colombia | Baa2 | 0.0274 | 0.0310 | 0.131387 | NaN | China | 0.0105 | NaN | China | 0.0099 |
| Baa2 | 207.432370 | 179.146138 | NaN | Costa Rica | B1 | 0.0311 | 0.0229 | -0.263666 | NaN | Colombia | 0.0310 | NaN | Colombia | 0.0274 |
| Baa3 | 239.443539 | 206.792147 | NaN | Croatia | Baa2 | 0.0134 | 0.0124 | -0.074627 | NaN | Costa Rica | 0.0229 | NaN | Costa Rica | 0.0311 |
| Ca | 1307.336112 | 1129.063006 | NaN | Cyprus | Baa2 | 0.0111 | 0.0093 | -0.162162 | NaN | Croatia | 0.0124 | NaN | Croatia | 0.0134 |
| Caa1 | 816.925014 | 705.526149 | NaN | Czech Republic | Aa3 | 0.0056 | 0.0046 | -0.178571 | NaN | Cyprus | 0.0093 | NaN | Cyprus | 0.0111 |
| Caa2 | 980.822196 | 847.073715 | NaN | Denmark | Aaa | 0.0024 | 0.0017 | -0.291667 | NaN | Czech Republic | 0.0046 | NaN | Czech Republic | 0.0056 |
| Caa3 | 1089.660168 | 941.070145 | NaN | Dubai | NR | 0.0110 | 0.0095 | -0.136364 | NaN | Denmark | 0.0017 | NaN | Denmark | 0.0024 |
| NR | NaN | NaN | NaN | Ecuador | Caa3 | NaN | 0.2197 | NaN | NaN | Dubai | 0.0095 | NaN | Dubai | 0.0110 |
| NaN | NaN | NaN | NaN | Egypt | Caa1 | 0.1013 | 0.0670 | -0.338598 | NaN | Ecuador | 0.2197 | NaN | Ecuador | NaN |
| NaN | NaN | NaN | NaN | El Salvador | Caa1 | 0.0840 | 0.0750 | -0.107143 | NaN | Egypt | 0.0670 | NaN | Egypt | 0.1013 |
| NaN | NaN | NaN | NaN | Estonia | A1 | 0.0060 | 0.0077 | 0.283333 | NaN | El Salvador | 0.0750 | NaN | El Salvador | 0.0840 |
| NaN | NaN | NaN | NaN | Finland | Aa1 | 0.0034 | 0.0029 | -0.147059 | NaN | Estonia | 0.0077 | NaN | Estonia | 0.0060 |
| NaN | NaN | NaN | NaN | France | Aa2 | 0.0043 | 0.0051 | 0.186047 | NaN | Ethiopia | 0.3159 | NaN | Ethiopia | 0.3231 |
| NaN | NaN | NaN | NaN | Germany | Aaa | 0.0029 | 0.0020 | -0.310345 | NaN | Finland | 0.0029 | NaN | Finland | 0.0034 |
| NaN | NaN | NaN | NaN | Greece | Ba1 | 0.0128 | 0.0131 | 0.023438 | NaN | France | 0.0051 | NaN | France | 0.0043 |
| NaN | NaN | NaN | NaN | Guatemala | Ba1 | 0.0268 | 0.0215 | -0.197761 | NaN | Gabon | 0.0894 | NaN | Gabon | 0.0685 |
| NaN | NaN | NaN | NaN | Hong Kong | Aa3 | 0.0060 | 0.0053 | -0.116667 | NaN | Germany | 0.0020 | NaN | Germany | 0.0029 |
| NaN | NaN | NaN | NaN | Hungary | Baa2 | 0.0195 | 0.0167 | -0.143590 | NaN | Greece | 0.0131 | NaN | Greece | 0.0128 |
| NaN | NaN | NaN | NaN | Iceland | A2 | 0.0088 | 0.0060 | -0.318182 | NaN | Guatemala | 0.0215 | NaN | Guatemala | 0.0268 |
| NaN | NaN | NaN | NaN | India | Baa3 | 0.0099 | 0.0083 | -0.161616 | NaN | Hong Kong | 0.0053 | NaN | Hong Kong | 0.0060 |
| NaN | NaN | NaN | NaN | Indonesia | Baa2 | 0.0132 | 0.0128 | -0.030303 | NaN | Hungary | 0.0167 | NaN | Hungary | 0.0195 |
| NaN | NaN | NaN | NaN | Iraq | Caa1 | 0.0514 | 0.0395 | -0.231518 | NaN | Iceland | 0.0060 | NaN | Iceland | 0.0088 |
| NaN | NaN | NaN | NaN | Ireland | Aa3 | 0.0041 | 0.0031 | -0.243902 | NaN | India | 0.0083 | NaN | India | 0.0099 |
| NaN | NaN | NaN | NaN | Israel | A2 | 0.0157 | 0.0173 | 0.101911 | NaN | Indonesia | 0.0128 | NaN | Indonesia | 0.0132 |
| NaN | NaN | NaN | NaN | Italy | Baa3 | 0.0134 | 0.0129 | -0.037313 | NaN | Iraq | 0.0395 | NaN | Iraq | 0.0514 |
| NaN | NaN | NaN | NaN | Japan | A1 | 0.0043 | 0.0035 | -0.186047 | NaN | Ireland | 0.0031 | NaN | Ireland | 0.0041 |
| NaN | NaN | NaN | NaN | Kazakhstan | Baa2 | 0.0176 | 0.0137 | -0.221591 | NaN | Israel | 0.0173 | NaN | Israel | 0.0157 |
| NaN | NaN | NaN | NaN | Kenya | B3 | 0.0704 | 0.0542 | -0.230114 | NaN | Italy | 0.0129 | NaN | Italy | 0.0134 |
| NaN | NaN | NaN | NaN | Korea | Aa2 | 0.0037 | 0.0045 | 0.216216 | NaN | Japan | 0.0035 | NaN | Japan | 0.0043 |
| NaN | NaN | NaN | NaN | Kuwait | A1 | 0.0083 | 0.0083 | 0.000000 | NaN | Kazakhstan | 0.0137 | NaN | Kazakhstan | 0.0176 |
| NaN | NaN | NaN | NaN | Latvia | A3 | 0.0094 | 0.0086 | -0.085106 | NaN | Kenya | 0.0542 | NaN | Kenya | 0.0704 |
| NaN | NaN | NaN | NaN | Lithuania | A2 | 0.0090 | 0.0087 | -0.033333 | NaN | Korea | 0.0045 | NaN | Korea | 0.0037 |
| NaN | NaN | NaN | NaN | Malaysia | A3 | 0.0086 | 0.0081 | -0.058140 | NaN | Kuwait | 0.0083 | NaN | Kuwait | 0.0083 |
| NaN | NaN | NaN | NaN | Mexico | Baa2 | 0.0168 | 0.0176 | 0.047619 | NaN | Latvia | 0.0086 | NaN | Latvia | 0.0094 |
| NaN | NaN | NaN | NaN | Morocco | Ba1 | 0.0190 | 0.0135 | -0.289474 | NaN | Lebanon | NaN | NaN | Lebanon | NaN |
| NaN | NaN | NaN | NaN | Namibia | B1 | 0.0210 | 0.0159 | -0.242857 | NaN | Lithuania | 0.0087 | NaN | Lithuania | 0.0090 |
| NaN | NaN | NaN | NaN | Netherlands | Aaa | 0.0024 | 0.0019 | -0.208333 | NaN | Malaysia | 0.0081 | NaN | Malaysia | 0.0086 |
| NaN | NaN | NaN | NaN | New Zealand | Aaa | 0.0029 | 0.0021 | -0.275862 | NaN | Mexico | 0.0176 | NaN | Mexico | 0.0168 |
| NaN | NaN | NaN | NaN | Nicaragua | B2 | 0.0489 | 0.0624 | 0.276074 | NaN | Mongolia | 0.0331 | NaN | Mongolia | 0.0402 |
| NaN | NaN | NaN | NaN | Nigeria | Caa1 | 0.0644 | 0.0634 | -0.015528 | NaN | Morocco | 0.0135 | NaN | Morocco | 0.0190 |
| NaN | NaN | NaN | NaN | Norway | Aaa | 0.0024 | 0.0017 | -0.291667 | NaN | Namibia | 0.0159 | NaN | Namibia | 0.0210 |
| NaN | NaN | NaN | NaN | Oman | Ba1 | 0.0192 | 0.0149 | -0.223958 | NaN | Netherlands | 0.0019 | NaN | Netherlands | 0.0024 |
| NaN | NaN | NaN | NaN | Pakistan | Caa3 | NaN | 0.1678 | NaN | NaN | New Zealand | 0.0021 | NaN | New Zealand | 0.0029 |
| NaN | NaN | NaN | NaN | Panama | Baa3 | 0.0231 | 0.0261 | 0.129870 | NaN | Nicaragua | 0.0624 | NaN | Nicaragua | 0.0489 |
| NaN | NaN | NaN | NaN | Peru | Baa1 | 0.0137 | 0.0128 | -0.065693 | NaN | Nigeria | 0.0634 | NaN | Nigeria | 0.0644 |
| NaN | NaN | NaN | NaN | Philippines | Baa2 | 0.0118 | 0.0122 | 0.033898 | NaN | Norway | 0.0017 | NaN | Norway | 0.0024 |
| NaN | NaN | NaN | NaN | Poland | A2 | 0.0106 | 0.0101 | -0.047170 | NaN | Oman | 0.0149 | NaN | Oman | 0.0192 |
| NaN | NaN | NaN | NaN | Portugal | A3 | 0.0075 | 0.0066 | -0.120000 | NaN | Pakistan | 0.1678 | NaN | Pakistan | NaN |
| NaN | NaN | NaN | NaN | Qatar | Aa2 | 0.0083 | 0.0071 | -0.144578 | NaN | Panama | 0.0261 | NaN | Panama | 0.0231 |
| NaN | NaN | NaN | NaN | Romania | Baa3 | 0.0231 | 0.0198 | -0.142857 | NaN | Peru | 0.0128 | NaN | Peru | 0.0137 |
| NaN | NaN | NaN | NaN | Russia | NaN | NaN | NaN | NaN | NaN | Philippines | 0.0122 | NaN | Philippines | 0.0118 |
| NaN | NaN | NaN | NaN | Rwanda | B2 | 0.0553 | NaN | NaN | NaN | Poland | 0.0101 | NaN | Poland | 0.0106 |
| NaN | NaN | NaN | NaN | Saudi Arabia | A1 | 0.0085 | 0.0082 | -0.035294 | NaN | Portugal | 0.0066 | NaN | Portugal | 0.0075 |
| NaN | NaN | NaN | NaN | Senegal | Ba3 | 0.0689 | 0.0536 | -0.222061 | NaN | Qatar | 0.0071 | NaN | Qatar | 0.0083 |
| NaN | NaN | NaN | NaN | Serbia | Ba2 | 0.0286 | 0.0233 | -0.185315 | NaN | Romania | 0.0198 | NaN | Romania | 0.0231 |
| NaN | NaN | NaN | NaN | Slovakia | A2 | 0.0060 | 0.0048 | -0.200000 | NaN | Russia | NaN | NaN | Russia | NaN |
| NaN | NaN | NaN | NaN | Slovenia | A3 | 0.0076 | 0.0061 | -0.197368 | NaN | Rwanda | NaN | NaN | Rwanda | 0.0553 |
| NaN | NaN | NaN | NaN | South Africa | Ba2 | 0.0316 | 0.0317 | 0.003165 | NaN | Saudi Arabia | 0.0082 | NaN | Saudi Arabia | 0.0085 |
| NaN | NaN | NaN | NaN | Spain | Baa1 | 0.0078 | 0.0068 | -0.128205 | NaN | Senegal | 0.0536 | NaN | Senegal | 0.0689 |
| NaN | NaN | NaN | NaN | Sweden | Aaa | 0.0028 | 0.0020 | -0.285714 | NaN | Serbia | 0.0233 | NaN | Serbia | 0.0286 |
| NaN | NaN | NaN | NaN | Switzerland | Aaa | 0.0022 | 0.0008 | -0.636364 | NaN | Slovakia | 0.0048 | NaN | Slovakia | 0.0060 |
| NaN | NaN | NaN | NaN | Thailand | Baa1 | 0.0065 | 0.0069 | 0.061538 | NaN | Slovenia | 0.0061 | NaN | Slovenia | 0.0076 |
| NaN | NaN | NaN | NaN | Tunisia | Caa2 | 0.0978 | 0.0789 | -0.193252 | NaN | South Africa | 0.0317 | NaN | South Africa | 0.0316 |
| NaN | NaN | NaN | NaN | Turkey | B3 | 0.0386 | 0.0377 | -0.023316 | NaN | Spain | 0.0068 | NaN | Spain | 0.0078 |
| NaN | NaN | NaN | NaN | United Kingdom | Aa3 | 0.0051 | 0.0042 | -0.176471 | NaN | Sri Lanka | NaN | NaN | Sri Lanka | 0.5936 |
| NaN | NaN | NaN | NaN | United States | Aaa | 0.0058 | 0.0046 | -0.206897 | NaN | Sweden | 0.0020 | NaN | Sweden | 0.0028 |
| NaN | NaN | NaN | NaN | Uruguay | Baa1 | 0.0114 | 0.0108 | -0.052632 | NaN | Switzerland | 0.0008 | NaN | Switzerland | 0.0022 |
| NaN | NaN | NaN | NaN | Vietnam | Ba2 | 0.0184 | 0.0176 | -0.043478 | NaN | Thailand | 0.0069 | NaN | Thailand | 0.0065 |
| NaN | NaN | NaN | NaN | Average | NaN | NaN | NaN | -0.115449 | NaN | Tunisia | 0.0789 | NaN | Tunisia | 0.0978 |
| NaN | NaN | NaN | NaN | Median | NaN | NaN | NaN | -0.136364 | NaN | Turkey | 0.0377 | NaN | Turkey | 0.0386 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Ukraine | NaN | NaN | Ukraine | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | United Kingdom | 0.0042 | NaN | United Kingdom | 0.0051 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | United States | 0.0046 | NaN | United States | 0.0058 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Uruguay | 0.0108 | NaN | Uruguay | 0.0114 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Venezuela | 0.1029 | NaN | Venezuela | 0.1125 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Vietnam | 0.0176 | NaN | Vietnam | 0.0184 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Zambia | NaN | NaN | Zambia | NaN |

## 10-year CDS Spreads
| Country | Moody's rating | CDS Spread (7/1/24) | CDS Spread adj for US | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | Aa2 | 0.0073 | 0.0027 | NaN | NaN | NaN | NaN | NaN | NaN |
| Albania | B1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Andorra (Principality of) | Baa1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Angola | B3 | 0.0678 | 0.0632 | NaN | NaN | NaN | NaN | NaN | NaN |
| Argentina | Ca | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Armenia | Ba3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Aruba | Baa3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Australia | Aaa | 0.0019 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Austria | Aa1 | 0.0023 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Azerbaijan | Ba1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Bahamas | B1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Bahrain | B2 | 0.0240 | 0.0194 | NaN | NaN | NaN | NaN | NaN | NaN |
| Bangladesh | B1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Barbados | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Belarus | C | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Belgium | Aa3 | 0.0028 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Belize | Caa2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Benin | B1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Bermuda | A2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Bolivia | Caa3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Bosnia and Herzegovina | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Botswana | A3 | NaN | NaN | NaN | NaN | NaN | Country | 2024-07-01 00:00:00 | CDS Spread net of US |
| Brazil | Ba2 | 0.0257 | 0.0211 | NaN | NaN | NaN | Abu Dhabi | 0.0073 | 0.0027 |
| Bulgaria | Baa1 | 0.0127 | 0.0081 | NaN | NaN | NaN | Algeria | 0.0145 | 0.0099 |
| Burkina Faso | Caa1 | NaN | NaN | NaN | NaN | NaN | Angola | 0.0678 | 0.0632 |
| Cambodia | B2 | NaN | NaN | NaN | NaN | NaN | Argentina | 0.238 | 0.2334 |
| Cameroon | Caa1 | 0.0746 | 0.0700 | NaN | NaN | NaN | Australia | 0.0019 | 0 |
| Canada | Aaa | 0.0038 | 0.0000 | NaN | NaN | NaN | Austria | 0.0023 | 0 |
| Cape Verde | B3 | NaN | NaN | NaN | NaN | NaN | Bahrain | 0.024 | 0.0194 |
| Cayman Islands | Aa3 | NaN | NaN | NaN | NaN | NaN | Belgium | 0.0028 | 0 |
| Chile | A2 | 0.0103 | 0.0057 | NaN | NaN | NaN | Brazil | 0.0257 | 0.0211 |
| China | A1 | 0.0105 | 0.0059 | NaN | NaN | NaN | Bulgaria | 0.0127 | 0.0081 |
| Colombia | Baa2 | 0.0310 | 0.0264 | NaN | NaN | NaN | Cameroon | 0.0746 | 0.07 |
| Congo (Democratic Republic of) | B3 | NaN | NaN | NaN | NaN | NaN | Canada | 0.0038 | 0 |
| Congo (Republic of) | Caa2 | NaN | NaN | NaN | NaN | NaN | Chile | 0.0103 | 0.0057 |
| Cook Islands | B1 | NaN | NaN | NaN | NaN | NaN | China | 0.0105 | 0.0059 |
| Costa Rica | B1 | 0.0229 | 0.0183 | NaN | NaN | NaN | Colombia | 0.031 | 0.0264 |
| Côte d'Ivoire | Ba2 | NaN | NaN | NaN | NaN | NaN | Costa Rica | 0.0229 | 0.0183 |
| Croatia | Baa2 | 0.0124 | 0.0078 | NaN | NaN | NaN | Croatia | 0.0124 | 0.0078 |
| Cuba | Ca | NaN | NaN | NaN | NaN | NaN | Cyprus | 0.0093 | 0.0047 |
| Curacao | Baa3 | NaN | NaN | NaN | NaN | NaN | Czech Republic | 0.0046 | 0 |
| Cyprus | Baa2 | 0.0093 | 0.0047 | NaN | NaN | NaN | Denmark | 0.0017 | 0 |
| Czech Republic | Aa3 | 0.0046 | 0.0000 | NaN | NaN | NaN | Dubai | 0.0095 | 0.0049 |
| Denmark | Aaa | 0.0017 | 0.0000 | NaN | NaN | NaN | Ecuador | 0.2197 | 0.2151 |
| Dominican Republic | Ba3 | NaN | NaN | NaN | NaN | NaN | Egypt | 0.067 | 0.0624 |
| Ecuador | Caa3 | 0.2197 | 0.2151 | NaN | NaN | NaN | El Salvador | 0.075 | 0.0704 |
| Egypt | Caa1 | 0.0670 | 0.0624 | NaN | NaN | NaN | Estonia | 0.0077 | 0.0031 |
| El Salvador | Caa1 | 0.0750 | 0.0704 | NaN | NaN | NaN | Ethiopia | 0.3159 | 0.3113 |
| Estonia | A1 | 0.0077 | 0.0031 | NaN | NaN | NaN | Finland | 0.0029 | 0 |
| Ethiopia | Caa2 | 0.3159 | 0.3113 | NaN | NaN | NaN | France | 0.0051 | 0.0005 |
| Fiji | B1 | NaN | NaN | NaN | NaN | NaN | Gabon | 0.0894 | 0.0848 |
| Finland | Aa1 | 0.0029 | 0.0000 | NaN | NaN | NaN | Germany | 0.002 | 0 |
| France | Aa2 | 0.0051 | 0.0005 | NaN | NaN | NaN | Greece | 0.0131 | 0.0085 |
| Gabon | Caa2 | NaN | NaN | NaN | NaN | NaN | Guatemala | 0.0215 | 0.0169 |
| Georgia | Ba2 | NaN | NaN | NaN | NaN | NaN | Hong Kong | 0.0053 | 0.0007 |
| Germany | Aaa | 0.0020 | 0.0000 | NaN | NaN | NaN | Hungary | 0.0167 | 0.0121 |
| Ghana | Caa3 | NaN | NaN | NaN | NaN | NaN | Iceland | 0.006 | 0.0014 |
| Greece | Ba1 | 0.0131 | 0.0085 | NaN | NaN | NaN | India | 0.0083 | 0.0037 |
| Guatemala | Ba1 | NaN | NaN | NaN | NaN | NaN | Indonesia | 0.0128 | 0.0082 |
| Guernsey (States of) | A1 | NaN | NaN | NaN | NaN | NaN | Iraq | 0.0395 | 0.0349 |
| Honduras | B1 | NaN | NaN | NaN | NaN | NaN | Ireland | 0.0031 | 0 |
| Hong Kong | Aa3 | 0.0053 | 0.0007 | NaN | NaN | NaN | Israel | 0.0173 | 0.0127 |
| Hungary | Baa2 | 0.0167 | 0.0121 | NaN | NaN | NaN | Italy | 0.0129 | 0.0083 |
| Iceland | A2 | 0.0060 | 0.0014 | NaN | NaN | NaN | Japan | 0.0035 | 0 |
| India | Baa3 | 0.0083 | 0.0037 | NaN | NaN | NaN | Kazakhstan | 0.0137 | 0.0091 |
| Indonesia | Baa2 | 0.0128 | 0.0082 | NaN | NaN | NaN | Kenya | 0.0542 | 0.0496 |
| Iraq | Caa1 | 0.0395 | 0.0349 | NaN | NaN | NaN | Korea | 0.0045 | 0 |
| Ireland | Aa3 | 0.0031 | 0.0000 | NaN | NaN | NaN | Kuwait | 0.0083 | 0.0037 |
| Isle of Man | Aa3 | NaN | NaN | NaN | NaN | NaN | Latvia | 0.0086 | 0.004 |
| Israel | A2 | 0.0173 | 0.0127 | NaN | NaN | NaN | Lebanon | NaN | NaN |
| Italy | Baa3 | 0.0129 | 0.0083 | NaN | NaN | NaN | Lithuania | 0.0087 | 0.0041 |
| Jamaica | B1 | NaN | NaN | NaN | NaN | NaN | Malaysia | 0.0081 | 0.0035 |
| Japan | A1 | 0.0035 | 0.0000 | NaN | NaN | NaN | Mexico | 0.0176 | 0.013 |
| Jersey (States of) | Aa3 | NaN | NaN | NaN | NaN | NaN | Mongolia | 0.0331 | 0.0285 |
| Jordan | Ba3 | NaN | NaN | NaN | NaN | NaN | Morocco | 0.0135 | 0.0089 |
| Kazakhstan | Baa2 | 0.0137 | 0.0091 | NaN | NaN | NaN | Namibia | 0.0159 | 0.0113 |
| Kenya | B3 | 0.0542 | 0.0496 | NaN | NaN | NaN | Netherlands | 0.0019 | 0 |
| Korea | Aa2 | 0.0045 | 0.0000 | NaN | NaN | NaN | New Zealand | 0.0021 | 0 |
| Kuwait | A1 | 0.0083 | 0.0037 | NaN | NaN | NaN | Nicaragua | 0.0624 | 0.0578 |
| Kyrgyzstan | B3 | NaN | NaN | NaN | NaN | NaN | Nigeria | 0.0634 | 0.0588 |
| Laos | Caa3 | NaN | NaN | NaN | NaN | NaN | Norway | 0.0017 | 0 |
| Latvia | A3 | 0.0086 | 0.0040 | NaN | NaN | NaN | Oman | 0.0149 | 0.0103 |
| Lebanon | C | NaN | NaN | NaN | NaN | NaN | Pakistan | 0.1678 | 0.1632 |
| Liechtenstein | Aaa | NaN | NaN | NaN | NaN | NaN | Panama | 0.0261 | 0.0215 |
| Lithuania | A2 | 0.0087 | 0.0041 | NaN | NaN | NaN | Peru | 0.0128 | 0.0082 |
| Luxembourg | Aaa | NaN | NaN | NaN | NaN | NaN | Philippines | 0.0122 | 0.0076 |
| Macao | Aa3 | NaN | NaN | NaN | NaN | NaN | Poland | 0.0101 | 0.0055 |
| Macedonia | Ba3 | NaN | NaN | NaN | NaN | NaN | Portugal | 0.0066 | 0.002 |
| Malaysia | A3 | 0.0081 | 0.0035 | NaN | NaN | NaN | Qatar | 0.0071 | 0.0025 |
| Maldives | Caa1 | NaN | NaN | NaN | NaN | NaN | Romania | 0.0198 | 0.0152 |
| Mali | Caa2 | NaN | NaN | NaN | NaN | NaN | Russia | NaN | NaN |
| Malta | A2 | NaN | NaN | NaN | NaN | NaN | Rwanda | NaN | NaN |
| Mauritius | Baa3 | NaN | NaN | NaN | NaN | NaN | Saudi Arabia | 0.0082 | 0.0036 |
| Mexico | Baa2 | 0.0176 | 0.0130 | NaN | NaN | NaN | Senegal | 0.0536 | 0.049 |
| Moldova | B3 | NaN | NaN | NaN | NaN | NaN | Serbia | 0.0233 | 0.0187 |
| Mongolia | B3 | NaN | NaN | NaN | NaN | NaN | Slovakia | 0.0048 | 0.0002 |
| Montenegro | B1 | NaN | NaN | NaN | NaN | NaN | Slovenia | 0.0061 | 0.0015 |
| Montserrat | Baa3 | NaN | NaN | NaN | NaN | NaN | South Africa | 0.0317 | 0.0271 |
| Morocco | Ba1 | 0.0135 | 0.0089 | NaN | NaN | NaN | Spain | 0.0068 | 0.0022 |
| Mozambique | Caa2 | NaN | NaN | NaN | NaN | NaN | Sri Lanka | NaN | NaN |
| Namibia | B1 | NaN | NaN | NaN | NaN | NaN | Sweden | 0.002 | 0 |
| Netherlands | Aaa | 0.0019 | 0.0000 | NaN | NaN | NaN | Switzerland | 0.0008 | 0 |
| New Zealand | Aaa | 0.0021 | 0.0000 | NaN | NaN | NaN | Thailand | 0.0069 | 0.0023 |
| Nicaragua | B2 | 0.0624 | 0.0578 | NaN | NaN | NaN | Tunisia | 0.0789 | 0.0743 |
| Niger | Caa3 | NaN | NaN | NaN | NaN | NaN | Turkey | 0.0377 | 0.0331 |
| Nigeria | Caa1 | 0.0634 | 0.0588 | NaN | NaN | NaN | Ukraine | NaN | NaN |
| Norway | Aaa | 0.0017 | 0.0000 | NaN | NaN | NaN | United Kingdom | 0.0042 | 0 |
| Oman | Ba1 | 0.0149 | 0.0103 | NaN | NaN | NaN | United States | 0.0046 | 0 |
| Pakistan | Caa3 | 0.1678 | 0.1632 | NaN | NaN | NaN | Uruguay | 0.0108 | 0.0062 |
| Panama | Baa3 | 0.0261 | 0.0215 | NaN | NaN | NaN | Venezuela | 0.1029 | 0.0983 |
| Papua New Guinea | B2 | NaN | NaN | NaN | NaN | NaN | Vietnam | 0.0176 | 0.013 |
| Paraguay | Ba1 | NaN | NaN | NaN | NaN | NaN | Zambia | NaN | NaN |
| Peru | Baa1 | 0.0128 | 0.0082 | NaN | NaN | NaN | NaN | NaN | NaN |
| Philippines | Baa2 | 0.0122 | 0.0076 | NaN | NaN | NaN | NaN | NaN | NaN |
| Poland | A2 | 0.0101 | 0.0055 | NaN | NaN | NaN | NaN | NaN | NaN |
| Portugal | A3 | 0.0066 | 0.0020 | NaN | NaN | NaN | NaN | NaN | NaN |
| Qatar | Aa2 | 0.0071 | 0.0025 | NaN | NaN | NaN | NaN | NaN | NaN |
| Ras Al Khaimah (Emirate of) | A3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Romania | Baa3 | 0.0198 | 0.0152 | NaN | NaN | NaN | NaN | NaN | NaN |
| Russia | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Rwanda | B2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Saudi Arabia | A1 | 0.0082 | 0.0036 | NaN | NaN | NaN | NaN | NaN | NaN |
| Senegal | Ba3 | 0.0536 | 0.0490 | NaN | NaN | NaN | NaN | NaN | NaN |
| Serbia | Ba2 | 0.0233 | 0.0187 | NaN | NaN | NaN | NaN | NaN | NaN |
| Sharjah | Ba1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Singapore | Aaa | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Slovakia | A2 | 0.0048 | 0.0002 | NaN | NaN | NaN | NaN | NaN | NaN |
| Slovenia | A3 | 0.0061 | 0.0015 | NaN | NaN | NaN | NaN | NaN | NaN |
| Solomon Islands | Caa1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| South Africa | Ba2 | 0.0317 | 0.0271 | NaN | NaN | NaN | NaN | NaN | NaN |
| Spain | Baa1 | 0.0068 | 0.0022 | NaN | NaN | NaN | NaN | NaN | NaN |
| Sri Lanka | Ca | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| St. Maarten | Ba2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| St. Vincent & the Grenadines | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Suriname | Caa3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Swaziland | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Sweden | Aaa | 0.0020 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Switzerland | Aaa | 0.0008 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Taiwan | Aa3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Tajikistan | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Tanzania | B1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Thailand | Baa1 | 0.0069 | 0.0023 | NaN | NaN | NaN | NaN | NaN | NaN |
| Togo | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Trinidad and Tobago | Ba2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Tunisia | Caa2 | 0.0789 | 0.0743 | NaN | NaN | NaN | NaN | NaN | NaN |
| Turkey | B3 | 0.0377 | 0.0331 | NaN | NaN | NaN | NaN | NaN | NaN |
| Turks and Caicos Islands | Baa1 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Uganda | B3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Ukraine | Ca | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| United Arab Emirates | Aa2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| United Kingdom | Aa3 | 0.0042 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| United States | Aaa | 0.0046 | 0.0000 | NaN | NaN | NaN | NaN | NaN | NaN |
| Uruguay | Baa1 | 0.0108 | 0.0062 | NaN | NaN | NaN | NaN | NaN | NaN |
| Uzbekistan | Ba3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Venezuela | C | 0.1029 | 0.0983 | NaN | NaN | NaN | NaN | NaN | NaN |
| Vietnam | Ba2 | 0.0176 | 0.0130 | NaN | NaN | NaN | NaN | NaN | NaN |
| Zambia | Caa2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Equity vs Govt Bond vol Risky
| Date: | 2024-02-01 00:00:00 | Unnamed: 2 | Just Risky markets | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Country | sEquity | sBond | sEquity/ sBond | s (CDS) | CDS | CV(CDS) | sEquity/ sCDS |
| Argentina | 0.5652 | 0.48055 | 1.176152 | NaN | NaN | NaN | NaN |
| Bahrain | 0.0511 | NaN | NaN | 0.0029 | 0.0269 | 0.107807 | 0.473997 |
| Brazil | 0.1621 | 0.1332 | 1.216967 | 0.0021 | 0.0231 | 0.090909 | 1.7831 |
| Colombia | 0.1744 | NaN | NaN | 0.0023 | 0.0275 | 0.083636 | 2.085217 |
| Costa Rica | 0.0714 | 0.0492 | 1.45122 | 0.0045 | 0.0242 | 0.18595 | 0.383973 |
| Egypt | 0.2733 | NaN | NaN | 0.0065 | 0.0633 | 0.102686 | 2.661522 |
| Hungary | 0.1441 | 0.1226 | 1.175367 | 0.0027 | 0.0175 | 0.154286 | 0.933981 |
| Jamaica | 0.1124 | 0.0908 | 1.237885 | 0.0038 | 0.0156 | 0.24359 | 0.461432 |
| Kenya | 0.1767 | NaN | NaN | 0.0072 | 0.0457 | 0.157549 | 1.121554 |
| Lebanon | 0.31 | 0.1646 | 1.883354 | NaN | NaN | NaN | NaN |
| Mexico | 0.1414 | 0.0801 | 1.765293 | 0.0025 | 0.0158 | 0.158228 | 0.893648 |
| Mongolia | 0.1545 | NaN | NaN | 0.005 | 0.0365 | 0.136986 | 1.12785 |
| Morocco | 0.099 | NaN | NaN | 0.0045 | 0.0153 | 0.294118 | 0.3366 |
| Nigeria | 0.1674 | NaN | NaN | 0.0049 | 0.0694 | 0.070605 | 2.370931 |
| Oman | 0.0733 | NaN | NaN | 0.0041 | 0.0168 | 0.244048 | 0.300351 |
| Panama | 0.0794 | 0.089 | 0.892135 | 0.0026 | 0.0268 | 0.097015 | 0.818431 |
| Romania | 0.1109 | 0.0803 | 1.381071 | NaN | NaN | NaN | NaN |
| Serbia | 0.0712 | NaN | NaN | 0.0032 | 0.0263 | 0.121673 | 0.585175 |
| Singapore | 0.1162 | 0.0599 | 1.9399 | NaN | NaN | NaN | NaN |
| South Africa | 0.1729 | NaN | NaN | 0.0027 | 0.0347 | 0.07781 | 2.222085 |
| Taiwan | 0.1398 | 0.1373 | 1.018208 | NaN | NaN | NaN | NaN |
| Tunisia | 0.0539 | NaN | NaN | 0.004 | 0.0816 | 0.04902 | 1.09956 |
| Turkey | 0.3189 | 0.148 | 2.15473 | 0.0036 | 0.0414 | 0.086957 | 3.66735 |
| Venezuela | 0.3081 | 0.6973 | 0.441847 | 0.0123 | 0.1065 | 0.115493 | 2.667695 |
| Vietnam | 0.1596 | NaN | NaN | 0.0024 | 0.018 | 0.133333 | 1.197 |
| Average | NaN | NaN | 1.364164 | NaN | NaN | NaN | 1.359573 |
| Median | NaN | NaN | 1.237885 | NaN | NaN | NaN | 1.110557 |
| High | NaN | NaN | 2.15473 | NaN | NaN | NaN | 3.66735 |
| Low | NaN | NaN | 0.441847 | NaN | NaN | NaN | 0.300351 |

## Country GDP
| Country | GDP (in millions) in 2023 | Unnamed: 2 | Unnamed: 3 | Country Name | GDP in 2023 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Country.1 | GDP (in millions) in 2022 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | 3.100000e+05 | NaN | NaN | Afghanistan | 1.450216e+04 | NaN | NaN | NaN | Abu Dhabi | 2.995000e+05 |
| Albania | 2.297768e+04 | Source: | World Bank | Albania | 2.297768e+04 | NaN | NaN | NaN | Albania | 2.297768e+04 |
| Andorra (Principality of) | 3.352000e+03 | Year | 2022 | Algeria | 2.398995e+05 | NaN | NaN | NaN | Andorra (Principality of) | 3.330000e+03 |
| Angola | 8.472296e+04 | NaN | NaN | American Samoa | 8.710000e+02 | NaN | NaN | NaN | Angola | 8.472296e+04 |
| Argentina | 6.405914e+05 | NaN | NaN | Andorra | 3.727674e+03 | NaN | NaN | NaN | Argentina | 6.405914e+05 |
| Armenia | 2.421213e+04 | NaN | NaN | Angola | 8.472296e+04 | NaN | NaN | NaN | Armenia | 2.421213e+04 |
| Aruba | 3.544708e+03 | NaN | NaN | Antigua and Barbuda | 2.033085e+03 | NaN | NaN | NaN | Aruba | 3.544708e+03 |
| Australia | 1.723827e+06 | NaN | NaN | Argentina | 6.405914e+05 | NaN | NaN | NaN | Australia | 1.723827e+06 |
| Austria | 5.160341e+05 | NaN | NaN | Armenia | 2.421213e+04 | NaN | NaN | NaN | Austria | 5.160341e+05 |
| Azerbaijan | 7.235618e+04 | NaN | NaN | Aruba | 3.544708e+03 | NaN | NaN | NaN | Azerbaijan | 7.235618e+04 |
| Bahamas | 1.121000e+04 | NaN | NaN | Australia | 1.723827e+06 | NaN | NaN | NaN | Bahamas | 1.121000e+04 |
| Bahrain | 4.320500e+04 | NaN | NaN | Austria | 5.160341e+05 | NaN | NaN | NaN | Bahrain | 4.320500e+04 |
| Bangladesh | 4.374153e+05 | NaN | NaN | Azerbaijan | 7.235618e+04 | NaN | NaN | NaN | Bangladesh | 4.374153e+05 |
| Barbados | 6.393564e+03 | NaN | NaN | Bahamas, The | 1.433850e+04 | NaN | NaN | NaN | Barbados | 6.393564e+03 |
| Belarus | 7.185738e+04 | NaN | NaN | Bahrain | 4.320500e+04 | NaN | NaN | NaN | Belarus | 7.185738e+04 |
| Belgium | 6.322166e+05 | NaN | NaN | Bangladesh | 4.374153e+05 | NaN | NaN | NaN | Belgium | 6.322166e+05 |
| Belize | 3.281500e+03 | NaN | NaN | Barbados | 6.393564e+03 | NaN | NaN | NaN | Belize | 3.281500e+03 |
| Benin | 1.967328e+04 | NaN | NaN | Belarus | 7.185738e+04 | NaN | NaN | NaN | Benin | 1.967328e+04 |
| Bermuda | 7.827980e+03 | NaN | NaN | Belgium | 6.322166e+05 | NaN | NaN | NaN | Bermuda | 7.827980e+03 |
| Bolivia | 4.584983e+04 | NaN | NaN | Belize | 3.281500e+03 | NaN | NaN | NaN | Bolivia | 4.584983e+04 |
| Bosnia and Herzegovina | 2.705489e+04 | NaN | NaN | Benin | 1.967328e+04 | NaN | NaN | NaN | Bosnia and Herzegovina | 2.705489e+04 |
| Botswana | 1.939577e+04 | NaN | NaN | Bermuda | 7.827980e+03 | NaN | NaN | NaN | Botswana | 1.939577e+04 |
| Brazil | 2.173666e+06 | NaN | NaN | Bhutan | 2.898228e+03 | NaN | NaN | NaN | Brazil | 2.173666e+06 |
| Bulgaria | 1.015844e+05 | NaN | NaN | Bolivia | 4.584983e+04 | NaN | NaN | NaN | Bulgaria | 1.015844e+05 |
| Burkina Faso | 2.032462e+04 | NaN | NaN | Bosnia and Herzegovina | 2.705489e+04 | NaN | NaN | NaN | Burkina Faso | 2.032462e+04 |
| Cambodia | 3.177276e+04 | NaN | NaN | Botswana | 1.939577e+04 | NaN | NaN | NaN | Cambodia | 3.177276e+04 |
| Cameroon | 4.794551e+04 | NaN | NaN | Brazil | 2.173666e+06 | NaN | NaN | NaN | Cameroon | 4.794551e+04 |
| Canada | 2.140086e+06 | NaN | NaN | British Virgin Islands | 0.000000e+00 | NaN | NaN | NaN | Canada | 2.140086e+06 |
| Cape Verde | 1.936000e+03 | NaN | NaN | Brunei Darussalam | 1.512829e+04 | NaN | NaN | NaN | Cape Verde | 1.936000e+03 |
| Cayman Islands | 6.600844e+03 | NaN | NaN | Bulgaria | 1.015844e+05 | NaN | NaN | NaN | Cayman Islands | 6.600844e+03 |
| Chile | 3.355333e+05 | NaN | NaN | Burkina Faso | 2.032462e+04 | NaN | NaN | NaN | Chile | 3.355333e+05 |
| China | 1.779478e+07 | NaN | NaN | Burundi | 2.642162e+03 | NaN | NaN | NaN | China | 1.779478e+07 |
| Colombia | 3.635402e+05 | NaN | NaN | Cabo Verde | 2.587252e+03 | NaN | NaN | NaN | Colombia | 3.635402e+05 |
| Congo (Democratic Republic of) | 6.638329e+04 | NaN | NaN | Cambodia | 3.177276e+04 | NaN | NaN | NaN | Congo (Democratic Republic of) | 0.000000e+00 |
| Congo (Republic of) | 1.532106e+04 | NaN | NaN | Cameroon | 4.794551e+04 | NaN | NaN | NaN | Congo (Republic of) | 1.461600e+04 |
| Cook Islands | 1.414000e+03 | NaN | NaN | Canada | 2.140086e+06 | NaN | NaN | NaN | Cook Islands | 1.414000e+03 |
| Costa Rica | 8.649794e+04 | NaN | NaN | Cayman Islands | 6.600844e+03 | NaN | NaN | NaN | Costa Rica | 8.649794e+04 |
| Côte d'Ivoire | 7.878883e+04 | NaN | NaN | Central African Republic | 2.555492e+03 | NaN | NaN | NaN | Côte d'Ivoire | 7.001900e+04 |
| Croatia | 8.268884e+04 | NaN | NaN | Chad | 1.314933e+04 | NaN | NaN | NaN | Croatia | 8.268884e+04 |
| Cuba | 1.073510e+05 | NaN | NaN | Channel Islands | 1.122832e+04 | NaN | NaN | NaN | Cuba | 0.000000e+00 |
| Curacao | 3.073840e+03 | NaN | NaN | Chile | 3.355333e+05 | NaN | NaN | NaN | Curacao | 3.073840e+03 |
| Cyprus | 3.222962e+04 | NaN | NaN | China | 1.779478e+07 | NaN | NaN | NaN | Cyprus | 3.222962e+04 |
| Czech Republic | 3.308583e+05 | NaN | NaN | Colombia | 3.635402e+05 | NaN | NaN | NaN | Czech Republic | 0.000000e+00 |
| Denmark | 4.041988e+05 | NaN | NaN | Comoros | 1.352381e+03 | NaN | NaN | NaN | Denmark | 4.041988e+05 |
| Dominican Republic | 1.214443e+05 | NaN | NaN | Congo, Dem. Rep. | 6.638329e+04 | NaN | NaN | NaN | Dominican Republic | 1.214443e+05 |
| Ecuador | 1.188448e+05 | NaN | NaN | Congo, Rep. | 1.532106e+04 | NaN | NaN | NaN | Ecuador | 1.188448e+05 |
| Egypt | 3.959261e+05 | NaN | NaN | Costa Rica | 8.649794e+04 | NaN | NaN | NaN | Egypt | 0.000000e+00 |
| El Salvador | 3.401562e+04 | NaN | NaN | Cote d'Ivoire | 7.878883e+04 | NaN | NaN | NaN | El Salvador | 3.401562e+04 |
| Estonia | 4.074485e+04 | NaN | NaN | Croatia | 8.268884e+04 | NaN | NaN | NaN | Estonia | 4.074485e+04 |
| Ethiopia | 1.636979e+05 | NaN | NaN | Cuba | 0.000000e+00 | NaN | NaN | NaN | Ethiopia | 1.636979e+05 |
| Fiji | 5.494798e+03 | NaN | NaN | Curacao | 3.073840e+03 | NaN | NaN | NaN | Fiji | 5.494798e+03 |
| Finland | 3.001872e+05 | NaN | NaN | Cyprus | 3.222962e+04 | NaN | NaN | NaN | Finland | 3.001872e+05 |
| France | 3.030904e+06 | NaN | NaN | Czechia | 3.308583e+05 | NaN | NaN | NaN | France | 3.030904e+06 |
| Gabon | 2.051613e+04 | NaN | NaN | Denmark | 4.041988e+05 | NaN | NaN | NaN | Gabon | 2.051613e+04 |
| Georgia | 3.053553e+04 | NaN | NaN | Djibouti | 4.098531e+03 | NaN | NaN | NaN | Georgia | 3.053553e+04 |
| Germany | 4.456081e+06 | NaN | NaN | Dominica | 6.539926e+02 | NaN | NaN | NaN | Germany | 4.456081e+06 |
| Ghana | 7.637039e+04 | NaN | NaN | Dominican Republic | 1.214443e+05 | NaN | NaN | NaN | Ghana | 7.637039e+04 |
| Greece | 2.382063e+05 | NaN | NaN | Ecuador | 1.188448e+05 | NaN | NaN | NaN | Greece | 2.382063e+05 |
| Guatemala | 1.020505e+05 | NaN | NaN | Egypt, Arab Rep. | 3.959261e+05 | NaN | NaN | NaN | Guatemala | 1.020505e+05 |
| Guernsey (States of) | 3.446000e+03 | NaN | NaN | El Salvador | 3.401562e+04 | NaN | NaN | NaN | Guernsey (States of) | 3.446000e+03 |
| Honduras | 3.440051e+04 | NaN | NaN | Equatorial Guinea | 1.211692e+04 | NaN | NaN | NaN | Honduras | 3.440051e+04 |
| Hong Kong | 3.820546e+05 | NaN | NaN | Eritrea | 0.000000e+00 | NaN | NaN | NaN | Hong Kong | 0.000000e+00 |
| Hungary | 2.123889e+05 | NaN | NaN | Estonia | 4.074485e+04 | NaN | NaN | NaN | Hungary | 2.123889e+05 |
| Iceland | 3.102003e+04 | NaN | NaN | Eswatini | 4.597856e+03 | NaN | NaN | NaN | Iceland | 3.102003e+04 |
| India | 3.549919e+06 | NaN | NaN | Ethiopia | 1.636979e+05 | NaN | NaN | NaN | India | 3.549919e+06 |
| Indonesia | 1.371171e+06 | NaN | NaN | Faroe Islands | 3.555930e+03 | NaN | NaN | NaN | Indonesia | 1.371171e+06 |
| Iraq | 2.508428e+05 | NaN | NaN | Fiji | 5.494798e+03 | NaN | NaN | NaN | Iraq | 2.508428e+05 |
| Ireland | 5.456295e+05 | NaN | NaN | Finland | 3.001872e+05 | NaN | NaN | NaN | Ireland | 5.456295e+05 |
| Isle of Man | 0.000000e+00 | NaN | NaN | France | 3.030904e+06 | NaN | NaN | NaN | Isle of Man | 0.000000e+00 |
| Israel | 5.099015e+05 | NaN | NaN | French Polynesia | 5.814661e+03 | NaN | NaN | NaN | Israel | 5.099015e+05 |
| Italy | 2.254851e+06 | NaN | NaN | Gabon | 2.051613e+04 | NaN | NaN | NaN | Italy | 2.254851e+06 |
| Jamaica | 1.942336e+04 | NaN | NaN | Gambia, The | 2.339904e+03 | NaN | NaN | NaN | Jamaica | 1.942336e+04 |
| Japan | 4.212945e+06 | NaN | NaN | Georgia | 3.053553e+04 | NaN | NaN | NaN | Japan | 4.212945e+06 |
| Jersey (States of) | 4.890000e+03 | NaN | NaN | Germany | 4.456081e+06 | NaN | NaN | NaN | Jersey (States of) | 4.890000e+03 |
| Jordan | 5.081364e+04 | NaN | NaN | Ghana | 7.637039e+04 | NaN | NaN | NaN | Jordan | 5.081364e+04 |
| Kazakhstan | 2.614211e+05 | NaN | NaN | Gibraltar | 0.000000e+00 | NaN | NaN | NaN | Kazakhstan | 2.614211e+05 |
| Kenya | 1.074406e+05 | NaN | NaN | Greece | 2.382063e+05 | NaN | NaN | NaN | Kenya | 1.074406e+05 |
| Korea | 1.712793e+06 | NaN | NaN | Greenland | 0.000000e+00 | NaN | NaN | NaN | Korea | 0.000000e+00 |
| Kuwait | 1.100000e+04 | NaN | NaN | Grenada | 1.320334e+03 | NaN | NaN | NaN | Kuwait | 1.617722e+05 |
| Kyrgyzstan | 1.398763e+04 | NaN | NaN | Guam | 6.910000e+03 | NaN | NaN | NaN | Kyrgyzstan | 0.000000e+00 |
| Laos | 1.584316e+04 | NaN | NaN | Guatemala | 1.020505e+05 | NaN | NaN | NaN | Laos | 0.000000e+00 |
| Latvia | 4.362708e+04 | NaN | NaN | Guinea | 2.361230e+04 | NaN | NaN | NaN | Latvia | 4.362708e+04 |
| Lebanon | 1.793726e+04 | NaN | NaN | Guinea-Bissau | 1.966461e+03 | NaN | NaN | NaN | Lebanon | 1.793726e+04 |
| Liechtenstein | 7.364655e+03 | NaN | NaN | Guyana | 1.678630e+04 | NaN | NaN | NaN | Liechtenstein | 7.364655e+03 |
| Lithuania | 7.783640e+04 | NaN | NaN | Haiti | 1.985083e+04 | NaN | NaN | NaN | Lithuania | 7.783640e+04 |
| Luxembourg | 8.575501e+04 | NaN | NaN | Honduras | 3.440051e+04 | NaN | NaN | NaN | Luxembourg | 8.575501e+04 |
| Macao | 4.706184e+04 | NaN | NaN | Hong Kong SAR, China | 3.820546e+05 | NaN | NaN | NaN | Macao | 0.000000e+00 |
| Macedonia | 1.476124e+04 | NaN | NaN | Hungary | 2.123889e+05 | NaN | NaN | NaN | Macedonia | 0.000000e+00 |
| Malaysia | 3.996488e+05 | NaN | NaN | Iceland | 3.102003e+04 | NaN | NaN | NaN | Malaysia | 3.996488e+05 |
| Maldives | 6.600000e+03 | NaN | NaN | India | 3.549919e+06 | NaN | NaN | NaN | Maldives | 6.600000e+03 |
| Mali | 2.090490e+04 | NaN | NaN | Indonesia | 1.371171e+06 | NaN | NaN | NaN | Mali | 2.090490e+04 |
| Malta | 2.095700e+04 | NaN | NaN | Iran, Islamic Rep. | 4.015045e+05 | NaN | NaN | NaN | Malta | 2.095700e+04 |
| Mauritius | 1.439713e+04 | NaN | NaN | Iraq | 2.508428e+05 | NaN | NaN | NaN | Mauritius | 1.439713e+04 |
| Mexico | 1.788887e+06 | NaN | NaN | Ireland | 5.456295e+05 | NaN | NaN | NaN | Mexico | 1.788887e+06 |
| Moldova | 1.653944e+04 | NaN | NaN | Isle of Man | 0.000000e+00 | NaN | NaN | NaN | Moldova | 1.653944e+04 |
| Mongolia | 1.987218e+04 | NaN | NaN | Israel | 5.099015e+05 | NaN | NaN | NaN | Mongolia | 1.987218e+04 |
| Montenegro | 7.404542e+03 | NaN | NaN | Italy | 2.254851e+06 | NaN | NaN | NaN | Montenegro | 7.404542e+03 |
| Montserrat | 1.619900e+04 | NaN | NaN | Jamaica | 1.942336e+04 | NaN | NaN | NaN | Montserrat | 1.619900e+04 |
| Morocco | 1.411094e+05 | NaN | NaN | Japan | 4.212945e+06 | NaN | NaN | NaN | Morocco | 1.411094e+05 |
| Mozambique | 2.062460e+04 | NaN | NaN | Jordan | 5.081364e+04 | NaN | NaN | NaN | Mozambique | 2.062460e+04 |
| Namibia | 1.235102e+04 | NaN | NaN | Kazakhstan | 2.614211e+05 | NaN | NaN | NaN | Namibia | 1.235102e+04 |
| Netherlands | 1.118125e+06 | NaN | NaN | Kenya | 1.074406e+05 | NaN | NaN | NaN | Netherlands | 1.118125e+06 |
| New Zealand | 2.534657e+05 | NaN | NaN | Kiribati | 2.790344e+02 | NaN | NaN | NaN | New Zealand | 2.534657e+05 |
| Nicaragua | 1.782922e+04 | NaN | NaN | Korea, Dem. People's Rep. | 0.000000e+00 | NaN | NaN | NaN | Nicaragua | 1.782922e+04 |
| Niger | 1.681917e+04 | NaN | NaN | Korea, Rep. | 1.712793e+06 | NaN | NaN | NaN | Niger | 1.681917e+04 |
| Nigeria | 3.628150e+05 | NaN | NaN | Kosovo | 1.043835e+04 | NaN | NaN | NaN | Nigeria | 3.628150e+05 |
| Norway | 4.855133e+05 | NaN | NaN | Kuwait | 1.617722e+05 | NaN | NaN | NaN | Norway | 4.855133e+05 |
| Oman | 1.081925e+05 | NaN | NaN | Kyrgyz Republic | 1.398763e+04 | NaN | NaN | NaN | Oman | 1.081925e+05 |
| Pakistan | 3.383685e+05 | NaN | NaN | Lao PDR | 1.584316e+04 | NaN | NaN | NaN | Pakistan | 3.383685e+05 |
| Panama | 8.338240e+04 | NaN | NaN | Latvia | 4.362708e+04 | NaN | NaN | NaN | Panama | 8.338240e+04 |
| Papua New Guinea | 3.093250e+04 | NaN | NaN | Lebanon | 1.793726e+04 | NaN | NaN | NaN | Papua New Guinea | 3.093250e+04 |
| Paraguay | 4.295626e+04 | NaN | NaN | Lesotho | 2.046039e+03 | NaN | NaN | NaN | Paraguay | 4.295626e+04 |
| Peru | 2.676032e+05 | NaN | NaN | Liberia | 4.332000e+03 | NaN | NaN | NaN | Peru | 2.676032e+05 |
| Philippines | 4.371464e+05 | NaN | NaN | Libya | 5.049172e+04 | NaN | NaN | NaN | Philippines | 4.371464e+05 |
| Poland | 8.112291e+05 | NaN | NaN | Liechtenstein | 7.364655e+03 | NaN | NaN | NaN | Poland | 8.112291e+05 |
| Portugal | 2.870800e+05 | NaN | NaN | Lithuania | 7.783640e+04 | NaN | NaN | NaN | Portugal | 2.870800e+05 |
| Qatar | 2.357704e+05 | NaN | NaN | Luxembourg | 8.575501e+04 | NaN | NaN | NaN | Qatar | 2.357704e+05 |
| Ras Al Khaimah (Emirate of) | 1.100000e+04 | NaN | NaN | Macao SAR, China | 4.706184e+04 | NaN | NaN | NaN | Ras Al Khaimah (Emirate of) | 1.100000e+04 |
| Romania | 3.510026e+05 | NaN | NaN | Madagascar | 1.603170e+04 | NaN | NaN | NaN | Romania | 3.510026e+05 |
| Russia | 2.021421e+06 | NaN | NaN | Malawi | 1.408434e+04 | NaN | NaN | NaN | Russia | 0.000000e+00 |
| Rwanda | 1.409777e+04 | NaN | NaN | Malaysia | 3.996488e+05 | NaN | NaN | NaN | Rwanda | 1.409777e+04 |
| Saudi Arabia | 1.067583e+06 | NaN | NaN | Maldives | 6.600000e+03 | NaN | NaN | NaN | Saudi Arabia | 1.067583e+06 |
| Senegal | 3.101399e+04 | NaN | NaN | Mali | 2.090490e+04 | NaN | NaN | NaN | Senegal | 3.101399e+04 |
| Serbia | 7.518713e+04 | NaN | NaN | Malta | 2.095700e+04 | NaN | NaN | NaN | Serbia | 7.518713e+04 |
| Sharjah | 2.480000e+04 | NaN | NaN | Marshall Islands | 2.840000e+02 | NaN | NaN | NaN | Sharjah | 2.480000e+04 |
| Singapore | 5.014275e+05 | NaN | NaN | Mauritania | 1.045258e+04 | NaN | NaN | NaN | Singapore | 5.014275e+05 |
| Slovakia | 1.327936e+05 | NaN | NaN | Mauritius | 1.439713e+04 | NaN | NaN | NaN | Slovakia | 0.000000e+00 |
| Slovenia | 6.821678e+04 | NaN | NaN | Mexico | 1.788887e+06 | NaN | NaN | NaN | Slovenia | 6.821678e+04 |
| Solomon Islands | 1.631287e+03 | NaN | NaN | Micronesia, Fed. Sts. | 4.600000e+02 | NaN | NaN | NaN | Solomon Islands | 1.631287e+03 |
| South Africa | 3.777816e+05 | NaN | NaN | Moldova | 1.653944e+04 | NaN | NaN | NaN | South Africa | 3.777816e+05 |
| Spain | 1.580695e+06 | NaN | NaN | Monaco | 8.784003e+03 | NaN | NaN | NaN | Spain | 1.580695e+06 |
| Sri Lanka | 8.435686e+04 | NaN | NaN | Mongolia | 1.987218e+04 | NaN | NaN | NaN | Sri Lanka | 8.435686e+04 |
| St. Maarten | 1.190000e+04 | NaN | NaN | Montenegro | 7.404542e+03 | NaN | NaN | NaN | St. Maarten | 1.190000e+04 |
| St. Vincent & the Grenadines | 8.100000e+03 | NaN | NaN | Morocco | 1.411094e+05 | NaN | NaN | NaN | St. Vincent & the Grenadines | 8.100000e+03 |
| Suriname | 3.782437e+03 | NaN | NaN | Mozambique | 2.062460e+04 | NaN | NaN | NaN | Suriname | 3.782437e+03 |
| Swaziland | 4.597856e+03 | NaN | NaN | Myanmar | 6.481503e+04 | NaN | NaN | NaN | Swaziland | 0.000000e+00 |
| Sweden | 5.932677e+05 | NaN | NaN | Namibia | 1.235102e+04 | NaN | NaN | NaN | Sweden | 5.932677e+05 |
| Switzerland | 8.849404e+05 | NaN | NaN | Nauru | 1.541278e+02 | NaN | NaN | NaN | Switzerland | 8.849404e+05 |
| Taiwan | 7.916100e+05 | NaN | NaN | Nepal | 4.090807e+04 | NaN | NaN | NaN | Taiwan | 7.616900e+05 |
| Tajikistan | 1.206060e+04 | NaN | NaN | Netherlands | 1.118125e+06 | NaN | NaN | NaN | Tajikistan | 1.206060e+04 |
| Tanzania | 7.915829e+04 | NaN | NaN | New Caledonia | 9.623319e+03 | NaN | NaN | NaN | Tanzania | 7.915829e+04 |
| Thailand | 5.149450e+05 | NaN | NaN | New Zealand | 2.534657e+05 | NaN | NaN | NaN | Thailand | 5.149450e+05 |
| Togo | 9.171262e+03 | NaN | NaN | Nicaragua | 1.782922e+04 | NaN | NaN | NaN | Togo | 9.171262e+03 |
| Trinidad and Tobago | 2.813994e+04 | NaN | NaN | Niger | 1.681917e+04 | NaN | NaN | NaN | Trinidad and Tobago | 2.813994e+04 |
| Tunisia | 4.852960e+04 | NaN | NaN | Nigeria | 3.628150e+05 | NaN | NaN | NaN | Tunisia | 4.852960e+04 |
| Turkey | 1.108022e+06 | NaN | NaN | North Macedonia | 1.476124e+04 | NaN | NaN | NaN | Turkey | 0.000000e+00 |
| Turks and Caicos Islands | 1.402054e+03 | NaN | NaN | Northern Mariana Islands | 0.000000e+00 | NaN | NaN | NaN | Turks and Caicos Islands | 1.402054e+03 |
| Uganda | 4.927288e+04 | NaN | NaN | Norway | 4.855133e+05 | NaN | NaN | NaN | Uganda | 4.927288e+04 |
| Ukraine | 1.787570e+05 | NaN | NaN | Oman | 1.081925e+05 | NaN | NaN | NaN | Ukraine | 1.787570e+05 |
| United Arab Emirates | 5.041735e+05 | NaN | NaN | Pakistan | 3.383685e+05 | NaN | NaN | NaN | United Arab Emirates | 5.041735e+05 |
| United Kingdom | 3.340032e+06 | NaN | NaN | Palau | 2.630207e+02 | NaN | NaN | NaN | United Kingdom | 3.340032e+06 |
| United States of America | 2.736094e+07 | NaN | NaN | Panama | 8.338240e+04 | NaN | NaN | NaN | United States of America | 0.000000e+00 |
| Uruguay | 7.724083e+04 | NaN | NaN | Papua New Guinea | 3.093250e+04 | NaN | NaN | NaN | Uruguay | 7.724083e+04 |
| Uzbekistan | 9.088915e+04 | NaN | NaN | Paraguay | 4.295626e+04 | NaN | NaN | NaN | Uzbekistan | 9.088915e+04 |
| Venezuela | 9.840000e+04 | NaN | NaN | Peru | 2.676032e+05 | NaN | NaN | NaN | Venezuela | 9.840000e+04 |
| Vietnam | 4.297170e+05 | NaN | NaN | Philippines | 4.371464e+05 | NaN | NaN | NaN | Vietnam | 4.088020e+05 |
| Zambia | 2.816263e+04 | NaN | NaN | Poland | 8.112291e+05 | NaN | NaN | NaN | Zambia | 2.816263e+04 |
| NaN | NaN | NaN | NaN | Portugal | 2.870800e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Puerto Rico | 1.179023e+05 | NaN | NaN | NaN | NaN | NaN |
| Algeria | 2.398995e+05 | NaN | NaN | Qatar | 2.357704e+05 | NaN | NaN | NaN | Algeria | 2.398995e+05 |
| Brunei | 1.401000e+04 | NaN | NaN | Romania | 3.510026e+05 | NaN | NaN | NaN | Brunei | 1.401000e+04 |
| Gambia | 2.339904e+03 | NaN | NaN | Russian Federation | 2.021421e+06 | NaN | NaN | NaN | Gambia | 2.038000e+03 |
| Guinea | 2.361230e+04 | NaN | NaN | Rwanda | 1.409777e+04 | NaN | NaN | NaN | Guinea | 2.361230e+04 |
| Guinea-Bissau | 1.966461e+03 | NaN | NaN | Samoa | 9.341003e+02 | NaN | NaN | NaN | Guinea-Bissau | 1.966461e+03 |
| Guyana | 1.678630e+04 | NaN | NaN | San Marino | 0.000000e+00 | NaN | NaN | NaN | Guyana | 1.678630e+04 |
| Haiti | 1.985083e+04 | NaN | NaN | Sao Tome and Principe | 6.032407e+02 | NaN | NaN | NaN | Haiti | 1.985083e+04 |
| Iran | 4.015045e+05 | NaN | NaN | Saudi Arabia | 1.067583e+06 | NaN | NaN | NaN | Iran | 0.000000e+00 |
| Korea, D.P.R. | 2.850000e+04 | NaN | NaN | Senegal | 3.101399e+04 | NaN | NaN | NaN | Korea, D.P.R. | 2.850000e+04 |
| Liberia | 4.332000e+03 | NaN | NaN | Serbia | 7.518713e+04 | NaN | NaN | NaN | Liberia | 4.332000e+03 |
| Libya | 5.049172e+04 | NaN | NaN | Seychelles | 2.141450e+03 | NaN | NaN | NaN | Libya | 5.049172e+04 |
| Madagascar | 1.603170e+04 | NaN | NaN | Sierra Leone | 3.809832e+03 | NaN | NaN | NaN | Madagascar | 1.603170e+04 |
| Malawi | 1.408434e+04 | NaN | NaN | Singapore | 5.014275e+05 | NaN | NaN | NaN | Malawi | 1.408434e+04 |
| Myanmar | 6.481503e+04 | NaN | NaN | Sint Maarten (Dutch part) | 1.623166e+03 | NaN | NaN | NaN | Myanmar | 6.481503e+04 |
| Sierra Leone | 3.809832e+03 | NaN | NaN | Slovak Republic | 1.327936e+05 | NaN | NaN | NaN | Sierra Leone | 3.809832e+03 |
| Somalia | 1.167980e+04 | NaN | NaN | Slovenia | 6.821678e+04 | NaN | NaN | NaN | Somalia | 1.167980e+04 |
| Sudan | 1.093270e+05 | NaN | NaN | Solomon Islands | 1.631287e+03 | NaN | NaN | NaN | Sudan | 1.093270e+05 |
| Syria | 8.980000e+03 | NaN | NaN | Somalia | 1.167980e+04 | NaN | NaN | NaN | Syria | 0.000000e+00 |
| Yemen, Republic | 2.161000e+04 | NaN | NaN | South Africa | 3.777816e+05 | NaN | NaN | NaN | Yemen, Republic | 2.161000e+04 |
| Zimbabwe | 2.653827e+04 | NaN | NaN | South Sudan | 0.000000e+00 | NaN | NaN | NaN | Zimbabwe | 2.653827e+04 |
| NaN | NaN | NaN | NaN | Spain | 1.580695e+06 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Sri Lanka | 8.435686e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | St. Kitts and Nevis | 1.077033e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | St. Lucia | 2.519926e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | St. Martin (French part) | 0.000000e+00 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | St. Vincent and the Grenadines | 1.065963e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Sudan | 1.093270e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Suriname | 3.782437e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Sweden | 5.932677e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Switzerland | 8.849404e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Syrian Arab Republic | 0.000000e+00 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tajikistan | 1.206060e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tanzania | 7.915829e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Thailand | 5.149450e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Timor-Leste | 2.243143e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Togo | 9.171262e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tonga | 5.002749e+02 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Trinidad and Tobago | 2.813994e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tunisia | 4.852960e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turkiye | 1.108022e+06 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turkmenistan | 5.988733e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turks and Caicos Islands | 1.402054e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tuvalu | 6.228031e+01 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uganda | 4.927288e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Ukraine | 1.787570e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United Arab Emirates | 5.041735e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United Kingdom | 3.340032e+06 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United States | 2.736094e+07 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uruguay | 7.724083e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uzbekistan | 9.088915e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Vanuatu | 1.126313e+03 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Venezuela, RB | 0.000000e+00 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Viet Nam | 4.297170e+05 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Virgin Islands (U.S.) | 0.000000e+00 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | West Bank and Gaza | 1.739630e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Yemen, Rep. | 0.000000e+00 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Zambia | 2.816263e+04 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Zimbabwe | 2.653827e+04 | NaN | NaN | NaN | NaN | NaN |

## Ratings worksheet
| Country | S&P Rating | Moody's Rating | Unnamed: 3 | Country.1 | Moody's | S&P | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 | Country.2 | FC | LC | Unnamed: 13 | Sovereign | LT FC rating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | AA | Aa2 | NaN | Abu Dhabi | Aa2 | AA | NaN | NaN | NaN | Abu Dhabi | Aa2 | Aa2 | NaN | Abu Dhabi | AA |
| Albania | BB- | B1 | NaN | Albania | B1 | BB- | NaN | NaN | NaN | Albania | B1 | B1 | NaN | Albania | BB- |
| Andorra (Principality of) | BBB+ | Baa1 | NaN | Andorra | Baa1 | BBB+ | NaN | NaN | NaN | Andorra | Baa1 | Baa1 | NaN | Andorra | BBB+ |
| Angola | B- | B3 | NaN | Angola | B3 | B- | NaN | NaN | NaN | Angola | B3 | B3 | NaN | Angola | B- |
| Argentina | CCC | Ca | NaN | Argentina | Ca | CCC | NaN | NaN | NaN | Argentina | Ca | Ca | NaN | Argentina | CCC |
| Armenia | BB- | Ba3 | NaN | Armenia | Ba3 | BB- | NaN | NaN | NaN | Armenia | Ba3 | Ba3 | NaN | Armenia | BB- |
| Aruba | BBB | Baa3 | NaN | Aruba | Baa3 | BBB | NaN | NaN | NaN | Aruba | Baa3 | Baa3 | NaN | Aruba | BBB |
| Australia | AAA | Aaa | NaN | Australia | Aaa | AAA | NaN | NaN | NaN | Australia | Aaa | Aaa | NaN | Australia | AAA |
| Austria | AA+ | Aa1 | NaN | Austria | Aa1 | AA+ | NaN | NaN | NaN | Austria | Aa1 | Aa1 | NaN | Austria | AA+ |
| Azerbaijan | BB+ | Ba1 | NaN | Azerbaijan | Ba1 | BB+ | NaN | NaN | NaN | Azerbaijan | Ba1 | Ba1 | NaN | Azerbaijan | BB+ |
| Bahamas | B+ | B1 | NaN | Bahamas | B1 | B+ | NaN | NaN | NaN | Bahamas | B1 | B1 | NaN | Bahamas | B+ |
| Bahrain | B+ | B2 | NaN | Bahrain | B2 | B+ | NaN | NaN | NaN | Bahamas-Offshore Banks | - | - | NaN | Bahrain | B+ |
| Bangladesh | BB- | B1 | NaN | Bangladesh | B1 | BB- | NaN | NaN | NaN | Bahrain | B2 | B2 | NaN | Bangladesh | BB- |
| Barbados | B- | B3 | NaN | Barbados | B3 | B- | NaN | NaN | NaN | Bahrain-Offshore Banks [1] | - | - | NaN | Barbados | B- |
| Belarus | NR | C | NaN | Belarus | C | NR | NaN | NaN | NaN | Bangladesh | B1 | B1 | NaN | Belgium | AA |
| Belgium | AA | Aa3 | NaN | Belgium | Aa3 | AA | NaN | NaN | NaN | Barbados | B3 | B3 | NaN | Belize | B- |
| Belize | B- | Caa2 | NaN | Belize | Caa2 | B- | NaN | NaN | NaN | Belarus | C | C | NaN | Benin | B+ |
| Benin | B+ | B1 | NaN | Benin | B1 | B+ | NaN | NaN | NaN | Belgium | Aa3 | Aa3 | NaN | Bermuda | A+ |
| Bermuda | A+ | A2 | NaN | Bermuda | A2 | A+ | NaN | NaN | NaN | Belize | Caa2 | Caa2 | NaN | Bolivia | CCC+ |
| Bolivia | CCC+ | Caa3 | NaN | Bolivia | Caa3 | CCC+ | NaN | NaN | NaN | Benin | B1 | B1 | NaN | Bosnia | B+ |
| Bosnia and Herzegovina | B+ | B3 | NaN | Bosnia and Herzegovina | B3 | B+ | NaN | NaN | NaN | Bermuda | A2 | A2 | NaN | Botswana | BBB+ |
| Botswana | BBB+ | A3 | NaN | Botswana | A3 | BBB+ | NaN | NaN | NaN | Bolivia | Caa3 | Caa3 | NaN | Brazil | BB |
| Brazil | BB | Ba2 | NaN | Brazil | Ba2 | BB | NaN | NaN | NaN | Bosnia and Herzegovina | B3 | B3 | NaN | Bulgaria | BBB |
| Bulgaria | BBB | Baa1 | NaN | Bulgaria | Baa1 | BBB | NaN | NaN | NaN | Botswana | A3 | A3 | NaN | Burkina Faso | CCC+ |
| Burkina Faso | CCC+ | NR | NaN | Burkina Faso | NR | CCC+ | NaN | NaN | NaN | Brazil | Ba2 | Ba2 | NaN | Cameroon | B- |
| Cambodia | NR | B2 | NaN | Cambodia | B2 | NR | NaN | NaN | NaN | Bulgaria | Baa1 | Baa1 | NaN | Canada | AAA |
| Cameroon | B- | Caa1 | NaN | Cameroon | Caa1 | B- | NaN | NaN | NaN | Cambodia | B2 | B2 | NaN | Cape Verde | B- |
| Canada | AAA | Aaa | NaN | Canada | Aaa | AAA | NaN | NaN | NaN | Cameroon | Caa1 | Caa1 | NaN | Chile | A |
| Cape Verde | B- | NR | NaN | Cape Verde | NR | B- | NaN | NaN | NaN | Canada | Aaa | Aaa | NaN | China | A+ |
| Cayman Islands | NR | Aa3 | NaN | Cayman Islands | Aa3 | NR | NaN | NaN | NaN | Cayman Islands | Aa3 | Aa3 | NaN | Colombia | BB+ |
| Chile | A | A2 | NaN | Chile | A2 | A | NaN | NaN | NaN | Cayman Islands-Offshore Banks | - | - | NaN | Congo, D.R. | B- |
| China | A+ | A1 | NaN | China | A1 | A+ | NaN | NaN | NaN | Chile | A2 | A2 | NaN | Congo | B- |
| Colombia | BB+ | Baa2 | NaN | Colombia | Baa2 | BB+ | NaN | NaN | NaN | China | A1 | A1 | NaN | Cook Islands | B+ |
| Congo (Democratic Republic of) | B- | B3 | NaN | Congo (Democratic Republic of) | B3 | B- | NaN | NaN | NaN | Colombia | Baa2 | Baa2 | NaN | Costa Rica | BB- |
| Congo (Republic of) | B- | Caa2 | NaN | Congo (Republic of) | Caa2 | B- | NaN | NaN | NaN | Costa Rica | B1 | B1 | NaN | Cote d'Ivoire | BB- |
| Cook Islands | B+ | NR | NaN | Cook Islands | NR | B+ | NaN | NaN | NaN | Cote d'Ivoire | Ba2 | Ba2 | NaN | Croatia | BBB+ |
| Costa Rica | BB- | B1 | NaN | Costa Rica | B1 | BB- | NaN | NaN | NaN | Croatia | Baa2 | Baa2 | NaN | Curacao | BBB- |
| Côte d'Ivoire | BB- | Ba2 | NaN | Cote d'Ivoire | Ba2 | BB- | NaN | NaN | NaN | Cuba | CA | WR | NaN | Cyprus | BBB |
| Croatia | BBB+ | Baa2 | NaN | Croatia | Baa2 | BBB+ | NaN | NaN | NaN | Cyprus | Baa2 | Baa2 | NaN | Czech Rep. | AA- |
| Cuba | NR | Ca | NaN | Cuba | Ca | NR | NaN | NaN | NaN | Czech Republic | Aa3 | Aa3 | NaN | Denmark | AAA |
| Curacao | BBB- | NR | NaN | Curacao | NR | BBB- | NaN | NaN | NaN | Democratic Republic of the Congo | B3 | B3 | NaN | Dominican Rep. | BB |
| Cyprus | BBB | Baa2 | NaN | Cyprus | Baa2 | BBB | NaN | NaN | NaN | Denmark | Aaa | Aaa | NaN | Ecuador | B- |
| Czech Republic | AA- | Aa3 | NaN | Czech Republic | Aa3 | AA- | NaN | NaN | NaN | Dominican Republic | Ba3 | Ba3 | NaN | Egypt | B- |
| Denmark | AAA | Aaa | NaN | Denmark | Aaa | AAA | NaN | NaN | NaN | Ecuador | Caa3 | Caa3 | NaN | El Salvador | B- |
| Dominican Republic | BB | Ba3 | NaN | Dominican Republic | Ba3 | BB | NaN | NaN | NaN | Egypt | Caa1 | Caa1 | NaN | Estonia | AA- |
| Ecuador | B- | Caa3 | NaN | Ecuador | Caa3 | B- | NaN | NaN | NaN | El Salvador | Caa1 | Caa1 | NaN | Ethiopia | SD |
| Egypt | B- | Caa1 | NaN | Egypt | Caa1 | B- | NaN | NaN | NaN | Estonia | A1 | A1 | NaN | Falkland Islands | A+ |
| El Salvador | B- | Caa1 | NaN | El Salvador | Caa1 | B- | NaN | NaN | NaN | eSwatini | B3 | B3 | NaN | Fiji | B+ |
| Estonia | AA- | A1 | NaN | Estonia | A1 | AA- | NaN | NaN | NaN | Ethiopia | Caa3 | Caa2 | NaN | Finland | AA+ |
| Ethiopia | SD | Caa2 | NaN | Ethiopia | Caa2 | SD | NaN | NaN | NaN | Fiji | B1 | B1 | NaN | France | AA |
| Fiji | B+ | B1 | NaN | Fiji | B1 | B+ | NaN | NaN | NaN | Finland | Aa1 | Aa1 | NaN | Georgia | BB |
| Finland | AA+ | Aa1 | NaN | Finland | Aa1 | AA+ | NaN | NaN | NaN | France | Aa2 | Aa2 | NaN | Germany | AAA |
| France | AA | Aa2 | NaN | France | Aa2 | AA | NaN | NaN | NaN | Gabon | Caa2 | Caa2 | NaN | Ghana | SD |
| Gabon | NR | Caa2 | NaN | Gabon | Caa2 | NR | NaN | NaN | NaN | Georgia | Ba2 | Ba2 | NaN | Greece | BBB- |
| Georgia | BB | Ba2 | NaN | Georgia | Ba2 | BB | NaN | NaN | NaN | Germany | Aaa | Aaa | NaN | Guatemala | BB |
| Germany | AAA | Aaa | NaN | Germany | Aaa | AAA | NaN | NaN | NaN | Ghana | Ca | Caa3 | NaN | Guernsey | A+ |
| Ghana | SD | Caa3 | NaN | Ghana | Caa3 | SD | NaN | NaN | NaN | Greece | Ba1 | Ba1 | NaN | Honduras | BB- |
| Greece | BBB- | Ba1 | NaN | Greece | Ba1 | BBB- | NaN | NaN | NaN | Guatemala | Ba1 | Ba1 | NaN | Hong Kong | AA+ |
| Guatemala | BB | Ba1 | NaN | Guatemala | Ba1 | BB | NaN | NaN | NaN | Guernsey (Channel Islands) | - | - | NaN | Hungary | BBB- |
| Guernsey (States of) | A+ | NR | NaN | Guernsey (Channel Islands) | NR | A+ | NaN | NaN | NaN | Honduras | B1 | B1 | NaN | Iceland | A+ |
| Honduras | BB- | B1 | NaN | Honduras | B1 | BB- | NaN | NaN | NaN | Hong Kong SAR, China | Aa3 | Aa3 | NaN | India | BBB- |
| Hong Kong | AA+ | Aa3 | NaN | Hong Kong | Aa3 | AA+ | NaN | NaN | NaN | Hungary | Baa2 | Baa2 | NaN | Indonesia | BBB |
| Hungary | BBB- | Baa2 | NaN | Hungary | Baa2 | BBB- | NaN | NaN | NaN | Iceland | A2 | A2 | NaN | Iraq | B- |
| Iceland | A+ | A2 | NaN | Iceland | A2 | A+ | NaN | NaN | NaN | India | Baa3 | Baa3 | NaN | Ireland\* | AA |
| India | BBB- | Baa3 | NaN | India | Baa3 | BBB- | NaN | NaN | NaN | Indonesia | Baa2 | Baa2 | NaN | Israel | AA- |
| Indonesia | BBB | Baa2 | NaN | Indonesia | Baa2 | BBB | NaN | NaN | NaN | Iraq | Caa1 | Caa1 | NaN | Italy | BBB |
| Iraq | B- | Caa1 | NaN | Iraq | Caa1 | B- | NaN | NaN | NaN | Ireland | Aa3 | Aa3 | NaN | Jamaica | BB- |
| Ireland | AA | Aa3 | NaN | Ireland | Aa3 | AA | NaN | NaN | NaN | Isle of Man | Aa3 | Aa3 | NaN | Japan | A+ |
| Isle of Man | NR | Aa3 | NaN | Isle of Man | Aa3 | NR | NaN | NaN | NaN | Israel | A2 | A2 | NaN | Jersey | AA- |
| Israel | AA- | A2 | NaN | Israel | A2 | AA- | NaN | NaN | NaN | Italy | Baa3 | Baa3 | NaN | Jordan | B+ |
| Italy | BBB | Baa3 | NaN | Italy | Baa3 | BBB | NaN | NaN | NaN | Jamaica | B1 | B1 | NaN | Kazakhstan | BBB- |
| Jamaica | BB- | B1 | NaN | Jamaica | B1 | BB- | NaN | NaN | NaN | Japan | A1 | A1 | NaN | Kenya | B |
| Japan | A+ | A1 | NaN | Japan | A1 | A+ | NaN | NaN | NaN | Jersey (Channel Islands) | - | - | NaN | Korea | AA |
| Jersey (States of) | AA- | NR | NaN | Jersey (Channel Islands) | NR | AA- | NaN | NaN | NaN | Jordan | Ba3 | Ba3 | NaN | Kuwait | A+ |
| Jordan | B+ | Ba3 | NaN | Jordan | Ba3 | B+ | NaN | NaN | NaN | Kazakhstan | Baa2 | Baa2 | NaN | Latvia | A+ |
| Kazakhstan | BBB- | Baa2 | NaN | Kazakhstan | Baa2 | BBB- | NaN | NaN | NaN | Kenya | B3 | B3 | NaN | Lebanon | SD |
| Kenya | B | B3 | NaN | Kenya | B3 | B | NaN | NaN | NaN | Korea | Aa2 | Aa2 | NaN | Liechtenstein | AAA |
| Korea | AA | Aa2 | NaN | Korea | Aa2 | AA | NaN | NaN | NaN | Kuwait | A1 | A1 | NaN | Lithuania | A+ |
| Kuwait | A+ | A1 | NaN | Kuwait | A1 | A+ | NaN | NaN | NaN | Kyrgyz Republic | B3 | B3 | NaN | Luxembourg | AAA |
| Kyrgyzstan | NR | B3 | NaN | Kyrgyz Republic | B3 | NR | NaN | NaN | NaN | Laos | Caa3 | Caa3 | NaN | Madagascar | B- |
| Laos | NR | Caa3 | NaN | Laos | Caa3 | NR | NaN | NaN | NaN | Latvia | A3 | A3 | NaN | Malaysia | A- |
| Latvia | A+ | A3 | NaN | Latvia | A3 | A+ | NaN | NaN | NaN | Lebanon | C | C | NaN | Malta | A- |
| Lebanon | NR | C | NaN | Lebanon | C | NR | NaN | NaN | NaN | Liechtenstein | - | - | NaN | Mauritius | BBB- |
| Liechtenstein | AAA | NR | NaN | Liechtenstein | NR | AAA | NaN | NaN | NaN | Lithuania | A2 | A2 | NaN | Mexico | BBB |
| Lithuania | A+ | A2 | NaN | Lithuania | A2 | A+ | NaN | NaN | NaN | Luxembourg | Aaa | Aaa | NaN | Mongolia | B |
| Luxembourg | AAA | Aaa | NaN | Luxembourg | Aaa | AAA | NaN | NaN | NaN | Macao SAR, China | Aa3 | Aa3 | NaN | Montenegro | B |
| Macao | NR | Aa3 | NaN | Macao | Aa3 | NR | NaN | NaN | NaN | Malaysia | A3 | A3 | NaN | Montserrat | BBB- |
| Macedonia | BB- | NR | NaN | Macedonia | NR | BB- | NaN | NaN | NaN | Maldives | Caa1 | Caa1 | NaN | Morocco | BB+ |
| Malaysia | A- | A3 | NaN | Malaysia | A3 | A- | NaN | NaN | NaN | Mali | Caa2 | Caa2 | NaN | Mozambique | CCC+ |
| Maldives | NR | Caa1 | NaN | Maldives | Caa1 | NR | NaN | NaN | NaN | Malta | A2 | A2 | NaN | Netherlands | AAA |
| Mali | NR | Caa2 | NaN | Mali | Caa2 | NR | NaN | NaN | NaN | Mauritius | Baa3 | Baa3 | NaN | New Zealand | AA+ |
| Malta | A- | A2 | NaN | Malta | A2 | A- | NaN | NaN | NaN | Mexico | Baa2 | Baa2 | NaN | Nicaragua | B |
| Mauritius | BBB- | Baa3 | NaN | Mauritius | Baa3 | BBB- | NaN | NaN | NaN | Moldova | B3 | B3 | NaN | Nigeria | B- |
| Mexico | BBB | Baa2 | NaN | Mexico | Baa2 | BBB | NaN | NaN | NaN | Mongolia | B3 | B3 | NaN | North Macedonia | BB- |
| Moldova | NR | B3 | NaN | Moldova | B3 | NR | NaN | NaN | NaN | Montenegro | B1 | - | NaN | Norway | AAA |
| Mongolia | B | B3 | NaN | Mongolia | B3 | B | NaN | NaN | NaN | Morocco | Ba1 | Ba1 | NaN | Oman | BB+ |
| Montenegro | B | B1 | NaN | Montenegro | B1 | B | NaN | NaN | NaN | Mozambique | Caa2 | Caa2 | NaN | Pakistan | CCC+ |
| Montserrat | BBB- | NR | NaN | Montserrat | NR | BBB- | NaN | NaN | NaN | Namibia | B1 | B1 | NaN | Panama | BBB |
| Morocco | BB+ | Ba1 | NaN | Morocco | Ba1 | BB+ | NaN | NaN | NaN | Netherlands | Aaa | Aaa | NaN | Papua New Guinea | B- |
| Mozambique | CCC+ | Caa2 | NaN | Mozambique | Caa2 | CCC+ | NaN | NaN | NaN | New Zealand | Aaa | Aaa | NaN | Paraguay | BB+ |
| Namibia | NR | B1 | NaN | Namibia | B1 | NR | NaN | NaN | NaN | Nicaragua | B2 | B2 | NaN | Peru | BBB |
| Netherlands | AAA | Aaa | NaN | Netherlands | Aaa | AAA | NaN | NaN | NaN | Niger | Caa3 | Caa3 | NaN | Philippines | BBB+ |
| New Zealand | AA+ | Aaa | NaN | New Zealand | Aaa | AA+ | NaN | NaN | NaN | Nigeria | Caa1 | Caa1 | NaN | Poland | A- |
| Nicaragua | B | B2 | NaN | Nicaragua | B2 | B | NaN | NaN | NaN | Norway | Aaa | Aaa | NaN | Portugal | A- |
| Niger | NR | Caa3 | NaN | Niger | Caa3 | NR | NaN | NaN | NaN | Oman | Ba1 | Ba1 | NaN | Qatar | AA |
| Nigeria | B- | Caa1 | NaN | Nigeria | Caa1 | B- | NaN | NaN | NaN | Pakistan | Caa3 | Caa3 | NaN | Ras Al Khaimah | A- |
| Norway | AAA | Aaa | NaN | Norway | Aaa | AAA | NaN | NaN | NaN | Panama | Baa3 | - | NaN | Romania | BBB- |
| Oman | BB+ | Ba1 | NaN | Oman | Ba1 | BB+ | NaN | NaN | NaN | Panama-Offshore Banks | - | - | NaN | Rwanda | B+ |
| Pakistan | CCC+ | Caa3 | NaN | Pakistan | Caa3 | CCC+ | NaN | NaN | NaN | Papua New Guinea | B2 | B2 | NaN | Saudi Arabia | A |
| Panama | BBB | Baa3 | NaN | Panama | Baa3 | BBB | NaN | NaN | NaN | Paraguay | Ba1 | Ba1 | NaN | Senegal | B+ |
| Papua New Guinea | B- | B2 | NaN | Papua New Guinea | B2 | B- | NaN | NaN | NaN | Peru | Baa1 | Baa1 | NaN | Serbia | BB+ |
| Paraguay | BB+ | Ba1 | NaN | Paraguay | Ba1 | BB+ | NaN | NaN | NaN | Philippines | Baa2 | Baa2 | NaN | Sharjah | BBB- |
| Peru | BBB | Baa1 | NaN | Peru | Baa1 | BBB | NaN | NaN | NaN | Poland | A2 | A2 | NaN | Singapore | AAA |
| Philippines | BBB+ | Baa2 | NaN | Philippines | Baa2 | BBB+ | NaN | NaN | NaN | Portugal | A3 | A3 | NaN | Slovakia | A+ |
| Poland | A- | A2 | NaN | Poland | A2 | A- | NaN | NaN | NaN | Qatar | Aa2 | Aa2 | NaN | Slovenia | AA- |
| Portugal | A- | A3 | NaN | Portugal | A3 | A- | NaN | NaN | NaN | Republic of the Congo | Caa2 | Caa2 | NaN | Vietnam | BB+ |
| Qatar | AA | Aa2 | NaN | Qatar | Aa2 | AA | NaN | NaN | NaN | Romania | Baa3 | Baa3 | NaN | South Africa | BB- |
| Ras Al Khaimah (Emirate of) | A- | A3 | NaN | Ras Al Khaimah (Emirate of) | NR | A- | NaN | NaN | NaN | Russia | WR | WR | NaN | Spain | A |
| Romania | BBB- | Baa3 | NaN | Romania | Baa3 | BBB- | NaN | NaN | NaN | Rwanda | B2 | B2 | NaN | Sri Lanka | SD |
| Russia | NR | NR | NaN | Russia | NR | NR | NaN | NaN | NaN | Saudi Arabia | A1 | A1 | NaN | St. Helena | BBB- |
| Rwanda | B+ | B2 | NaN | Rwanda | B2 | B+ | NaN | NaN | NaN | Senegal | Ba3 | Ba3 | NaN | Suriname | CCC+ |
| Saudi Arabia | A | A1 | NaN | Saudi Arabia | A1 | A | NaN | NaN | NaN | Serbia | Ba2 | Ba2 | NaN | Sweden | AAA |
| Senegal | B+ | Ba3 | NaN | Senegal | Ba3 | B+ | NaN | NaN | NaN | Sharjah | Ba1 | Ba1 | NaN | Switzerland | AAA |
| Serbia | BB+ | Ba2 | NaN | Serbia | Ba2 | BB+ | NaN | NaN | NaN | Singapore | Aaa | Aaa | NaN | Taiwan | AA+ |
| Sharjah | BBB- | Ba1 | NaN | Sharjah | Ba1 | BBB- | NaN | NaN | NaN | Slovakia | A2 | A2 | NaN | Tajikistan | B- |
| Singapore | AAA | Aaa | NaN | Singapore | Aaa | AAA | NaN | NaN | NaN | Slovenia | A3 | A3 | NaN | Thailand | BBB+ |
| Slovakia | A+ | A2 | NaN | Slovakia | A2 | A+ | NaN | NaN | NaN | Solomon Islands | Caa1 | Caa1 | NaN | Togo | B |
| Slovenia | AA- | A3 | NaN | Slovenia | A3 | AA- | NaN | NaN | NaN | South Africa | Ba2 | Ba2 | NaN | Trinidad and Tobago | BBB- |
| Solomon Islands | NR | Caa1 | NaN | Solomon Islands | Caa1 | NR | NaN | NaN | NaN | Spain | Baa1 | Baa1 | NaN | Turkiye | B |
| South Africa | BB- | Ba2 | NaN | South Africa | Ba2 | BB- | NaN | NaN | NaN | Sri Lanka | Ca | - | NaN | Turks and Caicos | BBB+ |
| Spain | A | Baa1 | NaN | Spain | Baa1 | A | NaN | NaN | NaN | Sint Maarten | WR | WR | NaN | Uganda | B- |
| Sri Lanka | NR | Ca | NaN | Sri Lanka | Ca | NR | NaN | NaN | NaN | St. Vincent & the Grenadines | B3 | B3 | NaN | Ukraine | CC |
| St. Maarten | NaN | Ba2 | NaN | Sint Maarten | WR | NR | NaN | NaN | NaN | Suriname | Caa3 | Caa3 | NaN | U.K. | AA |
| St. Vincent & the Grenadines | NR | B3 | NaN | St. Vincent & the Grenadines | B3 | NR | NaN | NaN | NaN | Sweden | Aaa | Aaa | NaN | U.S. | AA+ |
| Suriname | CCC+ | Caa3 | NaN | Suriname | Caa3 | CCC+ | NaN | NaN | NaN | Switzerland | Aaa | Aaa | NaN | Uruguay | BBB+ |
| Swaziland | NR | B3 | NaN | eSwatini | B3 | NR | NaN | NaN | NaN | Taiwan, China | Aa3 | Aa3 | NaN | Uzbekistan | BB- |
| Sweden | AAA | Aaa | NaN | Sweden | Aaa | AAA | NaN | NaN | NaN | Tajikistan | B3 | B3 | NaN | Zambia | SD |
| Switzerland | AAA | Aaa | NaN | Switzerland | Aaa | AAA | NaN | NaN | NaN | Tanzania | B1 | B1 | NaN | NaN | NaN |
| Taiwan | AA+ | Aa3 | NaN | Taiwan | Aa3 | AA+ | NaN | NaN | NaN | Thailand | Baa1 | Baa1 | NaN | NaN | NaN |
| Tajikistan | B- | B3 | NaN | Tajikistan | B3 | B- | NaN | NaN | NaN | Togo | B3 | B3 | NaN | NaN | NaN |
| Tanzania | NR | B1 | NaN | Tanzania | B1 | NR | NaN | NaN | NaN | Trinidad and Tobago | Ba2 | Ba2 | NaN | NaN | NaN |
| Thailand | BBB+ | Baa1 | NaN | Thailand | Baa1 | BBB+ | NaN | NaN | NaN | Tunisia | Caa2 | Caa2 | NaN | NaN | NaN |
| Togo | B | B3 | NaN | Togo | B3 | B | NaN | NaN | NaN | Turkiye | B3 | B3 | NaN | NaN | NaN |
| Trinidad and Tobago | BBB- | Ba2 | NaN | Trinidad and Tobago | Ba2 | BBB- | NaN | NaN | NaN | Uganda | B3 | B3 | NaN | NaN | NaN |
| Tunisia | NR | Caa2 | NaN | Tunisia | Caa2 | NR | NaN | NaN | NaN | Ukraine | Ca | Ca | NaN | NaN | NaN |
| Turkey | B | B3 | NaN | Turkey | B3 | B | NaN | NaN | NaN | United Arab Emirates | Aa2 | Aa2 | NaN | NaN | NaN |
| Turks and Caicos Islands | BBB+ | Baa1 | NaN | Turks and Caicos Islands | NR | BBB+ | NaN | NaN | NaN | United Kingdom | Aa3 | Aa3 | NaN | NaN | NaN |
| Uganda | B- | B3 | NaN | Uganda | B3 | B- | NaN | NaN | NaN | United States of America | Aaa | Aaa | NaN | NaN | NaN |
| Ukraine | CC | Ca | NaN | Ukraine | Ca | CC | NaN | NaN | NaN | Uzbekistan | Ba3 | Ba3 | NaN | NaN | NaN |
| United Arab Emirates | NR | Aa2 | NaN | United Arab Emirates | Aa2 | NR | NaN | NaN | NaN | Uruguay | Baa1 | Baa1 | NaN | NaN | NaN |
| United Kingdom | AA | Aa3 | NaN | United Kingdom | Aa3 | AA | NaN | NaN | NaN | Venezuela [2] | C | WR | NaN | NaN | NaN |
| United States | AA+ | Aaa | NaN | United States of America | Aaa | AA+ | NaN | NaN | NaN | Vietnam | Ba2 | Ba2 | NaN | NaN | NaN |
| Uruguay | BBB+ | Baa1 | NaN | Uruguay | Baa1 | BBB+ | NaN | NaN | NaN | Zambia | Caa2 | Caa2 | NaN | NaN | NaN |
| Uzbekistan | BB- | Ba3 | NaN | Uzbekistan | Ba3 | BB- | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Venezuela | NR | C | NaN | Venezuela | C | NR | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Vietnam | BB+ | Ba2 | NaN | Vietnam | Ba2 | BB+ | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Zambia | NR | Caa2 | NaN | Zambia | Caa2 | NR | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Country Tax Rates
| Country | Tax Rate | Looked up for 2023 | Unnamed: 3 | Country.1 | 2023 | Unnamed: 6 | Region | Average Tax Rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | 0.1500 | 0.1500 | NaN | Afghanistan | 0.2000 | NaN | Europe average | 0.1952 |
| Albania | 0.1500 | 0.1500 | NaN | Albania | 0.1500 | NaN | Africa average | 0.2686 |
| Andorra (Principality of) | 0.1898 | 0.1898 | NaN | Algeria | 0.2600 | NaN | Latin America average | 0.2853 |
| Angola | 0.2500 | 0.2500 | NaN | Andorra | 0.1000 | NaN | North America average | 0.2575 |
| Argentina | 0.3500 | 0.3500 | NaN | Angola | 0.2500 | NaN | Oceania average | 0.2974 |
| Armenia | 0.1800 | 0.1800 | NaN | Anguilla | 0.0000 | NaN | OECD average | 0.2281 |
| Aruba | 0.2500 | 0.2500 | NaN | Antigua and Barbuda | 0.2500 | NaN | NaN | NaN |
| Australia | 0.3000 | 0.3000 | NaN | Argentina | 0.3500 | NaN | NaN | NaN |
| Austria | 0.2400 | 0.2400 | NaN | Armenia | 0.1800 | NaN | NaN | NaN |
| Azerbaijan | 0.2000 | 0.2000 | NaN | Aruba | 0.2500 | NaN | NaN | NaN |
| Bahamas | 0.0000 | 0.0000 | NaN | Australia | 0.3000 | NaN | NaN | NaN |
| Bahrain | 0.0000 | 0.0000 | NaN | Austria | 0.2400 | NaN | NaN | NaN |
| Bangladesh | 0.3000 | 0.3000 | NaN | Azerbaijan | 0.2000 | NaN | NaN | NaN |
| Barbados | 0.0550 | 0.0550 | NaN | Bahamas | 0.0000 | NaN | NaN | NaN |
| Belarus | 0.1800 | 0.1800 | NaN | Bahrain | 0.0000 | NaN | NaN | NaN |
| Belgium | 0.2500 | 0.2500 | NaN | Bangladesh | 0.3000 | NaN | NaN | NaN |
| Belize | 0.2853 | 0.2853 | NaN | Barbados | 0.0550 | NaN | NaN | NaN |
| Benin | 0.3000 | 0.3000 | NaN | Belarus | 0.1800 | NaN | NaN | NaN |
| Bermuda | 0.0000 | 0.0000 | NaN | Belgium | 0.2500 | NaN | NaN | NaN |
| Bolivia | 0.2500 | 0.2500 | NaN | Benin | 0.3000 | NaN | NaN | NaN |
| Bosnia and Herzegovina | 0.1000 | 0.1000 | NaN | Bermuda | 0.0000 | NaN | NaN | NaN |
| Botswana | 0.2200 | 0.2200 | NaN | Bolivia | 0.2500 | NaN | NaN | NaN |
| Brazil | 0.3400 | 0.3400 | NaN | Bonaire, Saint Eustatius and Saba | 0.2500 | NaN | NaN | NaN |
| Bulgaria | 0.1000 | 0.1000 | NaN | Bosnia and Herzegovina | 0.1000 | NaN | NaN | NaN |
| Burkina Faso | 0.2800 | 0.2800 | NaN | Botswana | 0.2200 | NaN | NaN | NaN |
| Cambodia | 0.2000 | 0.2000 | NaN | Brazil | 0.3400 | NaN | NaN | NaN |
| Cameroon | 0.3300 | 0.3300 | NaN | Brunei Darussalam | 0.1850 | NaN | NaN | NaN |
| Canada | 0.2650 | 0.2650 | NaN | Bulgaria | 0.1000 | NaN | NaN | NaN |
| Cape Verde | 0.0000 | 0.0000 | NaN | Burkina Faso | 0.2800 | NaN | NaN | NaN |
| Cayman Islands | 0.0000 | 0.0000 | NaN | Burundi | 0.3000 | NaN | NaN | NaN |
| Chile | 0.2700 | 0.2700 | NaN | Cambodia | 0.2000 | NaN | NaN | NaN |
| China | 0.2500 | 0.2500 | NaN | Cameroon | 0.3300 | NaN | NaN | NaN |
| Colombia | 0.3500 | 0.3500 | NaN | Canada | 0.2650 | NaN | NaN | NaN |
| Congo (Democratic Republic of) | 0.3000 | 0.3000 | NaN | Cayman Islands | 0.0000 | NaN | NaN | NaN |
| Congo (Republic of) | 0.2800 | 0.2800 | NaN | Chile | 0.2700 | NaN | NaN | NaN |
| Cook Islands | 0.2974 | 0.2974 | NaN | China | 0.2500 | NaN | NaN | NaN |
| Costa Rica | 0.3000 | 0.3000 | NaN | Colombia | 0.3500 | NaN | NaN | NaN |
| Côte d'Ivoire | 0.2500 | 0.2500 | NaN | Congo | 0.2800 | NaN | NaN | NaN |
| Croatia | 0.1800 | 0.1800 | NaN | Congo (Democratic Republic of the) | 0.3000 | NaN | NaN | NaN |
| Cuba | 0.2853 | 0.2853 | NaN | Costa Rica | 0.3000 | NaN | NaN | NaN |
| Curacao | 0.2200 | 0.2200 | NaN | Croatia | 0.1800 | NaN | NaN | NaN |
| Cyprus | 0.1250 | 0.1250 | NaN | Curacao | 0.2200 | NaN | NaN | NaN |
| Czech Republic | 0.1900 | 0.1900 | NaN | Cyprus | 0.1250 | NaN | NaN | NaN |
| Denmark | 0.2200 | 0.2200 | NaN | Czech Republic | 0.1900 | NaN | NaN | NaN |
| Dominican Republic | 0.2700 | 0.2700 | NaN | Denmark | 0.2200 | NaN | NaN | NaN |
| Ecuador | 0.2500 | 0.2500 | NaN | Djibouti | 0.2500 | NaN | NaN | NaN |
| Egypt | 0.2250 | 0.2250 | NaN | Dominica | 0.2500 | NaN | NaN | NaN |
| El Salvador | 0.3000 | 0.3000 | NaN | Dominican Republic | 0.2700 | NaN | NaN | NaN |
| Estonia | 0.2000 | 0.2000 | NaN | Ecuador | 0.2500 | NaN | NaN | NaN |
| Ethiopia | 0.3000 | 0.3000 | NaN | Egypt | 0.2250 | NaN | NaN | NaN |
| Fiji | 0.2000 | 0.2000 | NaN | El Salvador | 0.3000 | NaN | NaN | NaN |
| Finland | 0.2000 | 0.2000 | NaN | Estonia | 0.2000 | NaN | NaN | NaN |
| France | 0.2500 | 0.2500 | NaN | Ethiopia | 0.3000 | NaN | NaN | NaN |
| Gabon | 0.3000 | 0.3000 | NaN | Fiji | 0.2000 | NaN | NaN | NaN |
| Georgia | 0.1500 | 0.1500 | NaN | Finland | 0.2000 | NaN | NaN | NaN |
| Germany | 0.3000 | 0.3000 | NaN | France | 0.2500 | NaN | NaN | NaN |
| Ghana | 0.2500 | 0.2500 | NaN | Gabon | 0.3000 | NaN | NaN | NaN |
| Greece | 0.2200 | 0.2200 | NaN | Gambia | 0.2700 | NaN | NaN | NaN |
| Guatemala | 0.2500 | 0.2500 | NaN | Georgia | 0.1500 | NaN | NaN | NaN |
| Guernsey (States of) | 0.0000 | 0.0000 | NaN | Germany | 0.3000 | NaN | NaN | NaN |
| Honduras | 0.2500 | 0.2500 | NaN | Ghana | 0.2500 | NaN | NaN | NaN |
| Hong Kong | 0.1650 | 0.1650 | NaN | Gibraltar | 0.1000 | NaN | NaN | NaN |
| Hungary | 0.0900 | 0.0900 | NaN | Greece | 0.2200 | NaN | NaN | NaN |
| Iceland | 0.2000 | 0.2000 | NaN | Grenada | 0.2800 | NaN | NaN | NaN |
| India | 0.3000 | 0.3000 | NaN | Guatemala | 0.2500 | NaN | NaN | NaN |
| Indonesia | 0.2200 | 0.2200 | NaN | Guernsey | 0.0000 | NaN | NaN | NaN |
| Iraq | 0.1500 | 0.1500 | NaN | Honduras | 0.2500 | NaN | NaN | NaN |
| Ireland | 0.1250 | 0.1250 | NaN | Hong Kong SAR | 0.1650 | NaN | NaN | NaN |
| Isle of Man | 0.0000 | 0.0000 | NaN | Hungary | 0.0900 | NaN | NaN | NaN |
| Israel | 0.2300 | 0.2300 | NaN | Iceland | 0.2000 | NaN | NaN | NaN |
| Italy | 0.2400 | 0.2400 | NaN | India | 0.3000 | NaN | NaN | NaN |
| Jamaica | 0.2500 | 0.2500 | NaN | Indonesia | 0.2200 | NaN | NaN | NaN |
| Japan | 0.3062 | 0.3062 | NaN | Iraq | 0.1500 | NaN | NaN | NaN |
| Jersey (States of) | 0.0000 | 0.0000 | NaN | Ireland | 0.1250 | NaN | NaN | NaN |
| Jordan | 0.2000 | 0.2000 | NaN | Isle of Man | 0.0000 | NaN | NaN | NaN |
| Kazakhstan | 0.2000 | 0.2000 | NaN | Israel | 0.2300 | NaN | NaN | NaN |
| Kenya | 0.3000 | 0.3000 | NaN | Italy | 0.2400 | NaN | NaN | NaN |
| Korea | 0.2500 | 0.2500 | NaN | Ivory Coast | 0.2500 | NaN | NaN | NaN |
| Kuwait | 0.1500 | 0.1500 | NaN | Jamaica | 0.2500 | NaN | NaN | NaN |
| Kyrgyzstan | 0.1000 | 0.1000 | NaN | Japan | 0.3062 | NaN | NaN | NaN |
| Laos | 0.2686 | 0.2686 | NaN | Jersey | 0.0000 | NaN | NaN | NaN |
| Latvia | 0.2000 | 0.2000 | NaN | Jordan | 0.2000 | NaN | NaN | NaN |
| Lebanon | 0.1700 | 0.1700 | NaN | Kazakhstan | 0.2000 | NaN | NaN | NaN |
| Liechtenstein | 0.1250 | 0.1250 | NaN | Kenya | 0.3000 | NaN | NaN | NaN |
| Lithuania | 0.1500 | 0.1500 | NaN | Korea, Republic of | 0.2400 | NaN | NaN | NaN |
| Luxembourg | 0.2494 | 0.2494 | NaN | Kuwait | 0.1500 | NaN | NaN | NaN |
| Macao | 0.2686 | 0.2686 | NaN | Kyrgyzstan | 0.1000 | NaN | NaN | NaN |
| Macedonia | 0.1000 | 0.1000 | NaN | Latvia | 0.2000 | NaN | NaN | NaN |
| Malaysia | 0.2400 | 0.2400 | NaN | Lebanon | 0.1700 | NaN | NaN | NaN |
| Maldives | 0.2686 | 0.2686 | NaN | Libya | 0.2400 | NaN | NaN | NaN |
| Mali | 0.2686 | 0.2686 | NaN | Liechtenstein | 0.1250 | NaN | NaN | NaN |
| Malta | 0.3500 | 0.3500 | NaN | Lithuania | 0.1500 | NaN | NaN | NaN |
| Mauritius | 0.1500 | 0.1500 | NaN | Luxembourg | 0.2494 | NaN | NaN | NaN |
| Mexico | 0.3000 | 0.3000 | NaN | Macau | 0.1200 | NaN | NaN | NaN |
| Moldova | 0.1200 | 0.1200 | NaN | Macedonia | 0.1000 | NaN | NaN | NaN |
| Mongolia | 0.2500 | 0.2500 | NaN | Madagascar | 0.2000 | NaN | NaN | NaN |
| Montenegro | 0.1500 | 0.1500 | NaN | Malawi | 0.3000 | NaN | NaN | NaN |
| Montserrat | 0.2853 | 0.2853 | NaN | Malaysia | 0.2400 | NaN | NaN | NaN |
| Morocco | 0.3200 | 0.3200 | NaN | Malta | 0.3500 | NaN | NaN | NaN |
| Mozambique | 0.3200 | 0.3200 | NaN | Mauritania | 0.2500 | NaN | NaN | NaN |
| Namibia | 0.3200 | 0.3200 | NaN | Mauritius | 0.1500 | NaN | NaN | NaN |
| Netherlands | 0.2580 | 0.2580 | NaN | Mexico | 0.3000 | NaN | NaN | NaN |
| New Zealand | 0.2800 | 0.2800 | NaN | Moldova | 0.1200 | NaN | NaN | NaN |
| Nicaragua | 0.3000 | 0.3000 | NaN | Monaco | 0.3300 | NaN | NaN | NaN |
| Niger | 0.2686 | 0.2686 | NaN | Mongolia | 0.2500 | NaN | NaN | NaN |
| Nigeria | 0.3000 | 0.3000 | NaN | Montenegro | 0.1500 | NaN | NaN | NaN |
| Norway | 0.2200 | 0.2200 | NaN | Morocco | 0.3200 | NaN | NaN | NaN |
| Oman | 0.1500 | 0.1500 | NaN | Mozambique | 0.3200 | NaN | NaN | NaN |
| Pakistan | 0.2900 | 0.2900 | NaN | Myanmar | 0.2200 | NaN | NaN | NaN |
| Panama | 0.2500 | 0.2500 | NaN | Namibia | 0.3200 | NaN | NaN | NaN |
| Papua New Guinea | 0.3000 | 0.3000 | NaN | Netherlands | 0.2580 | NaN | NaN | NaN |
| Paraguay | 0.1000 | 0.1000 | NaN | New Zealand | 0.2800 | NaN | NaN | NaN |
| Peru | 0.2950 | 0.2950 | NaN | Nicaragua | 0.3000 | NaN | NaN | NaN |
| Philippines | 0.2500 | 0.2500 | NaN | Nigeria | 0.3000 | NaN | NaN | NaN |
| Poland | 0.1900 | 0.1900 | NaN | Norway | 0.2200 | NaN | NaN | NaN |
| Portugal | 0.2100 | 0.2100 | NaN | Oman | 0.1500 | NaN | NaN | NaN |
| Qatar | 0.1000 | 0.1000 | NaN | Pakistan | 0.2900 | NaN | NaN | NaN |
| Ras Al Khaimah (Emirate of) | 0.0000 | 0.0000 | NaN | Palestinian Territory | 0.1500 | NaN | NaN | NaN |
| Romania | 0.1600 | 0.1600 | NaN | Panama | 0.2500 | NaN | NaN | NaN |
| Russia | 0.2000 | 0.2000 | NaN | Papua New Guinea | 0.3000 | NaN | NaN | NaN |
| Rwanda | 0.3000 | 0.3000 | NaN | Paraguay | 0.1000 | NaN | NaN | NaN |
| Saudi Arabia | 0.2000 | 0.2000 | NaN | Peru | 0.2950 | NaN | NaN | NaN |
| Senegal | 0.3000 | 0.3000 | NaN | Philippines | 0.2500 | NaN | NaN | NaN |
| Serbia | 0.1500 | 0.1500 | NaN | Poland | 0.1900 | NaN | NaN | NaN |
| Sharjah | 0.0000 | 0.0000 | NaN | Portugal | 0.2100 | NaN | NaN | NaN |
| Singapore | 0.1700 | 0.1700 | NaN | Qatar | 0.1000 | NaN | NaN | NaN |
| Slovakia | 0.2100 | 0.2100 | NaN | Romania | 0.1600 | NaN | NaN | NaN |
| Slovenia | 0.1900 | 0.1900 | NaN | Russia | 0.2000 | NaN | NaN | NaN |
| Solomon Islands | 0.3000 | 0.3000 | NaN | Rwanda | 0.3000 | NaN | NaN | NaN |
| South Africa | 0.2700 | 0.2700 | NaN | Saint Kitts and Nevis | 0.3300 | NaN | NaN | NaN |
| Spain | 0.2500 | 0.2500 | NaN | Saint Lucia | 0.3000 | NaN | NaN | NaN |
| Sri Lanka | 0.2400 | 0.2400 | NaN | Saint Vincent and the Grenadines | 0.3000 | NaN | NaN | NaN |
| St. Maarten | 0.2853 | 0.2853 | NaN | Samoa | 0.2700 | NaN | NaN | NaN |
| St. Vincent & the Grenadines | 0.2853 | 0.2853 | NaN | Saudi Arabia | 0.2000 | NaN | NaN | NaN |
| Suriname | 0.3600 | 0.3600 | NaN | Senegal | 0.3000 | NaN | NaN | NaN |
| Swaziland | 0.2750 | 0.2750 | NaN | Serbia | 0.1500 | NaN | NaN | NaN |
| Sweden | 0.2060 | 0.2060 | NaN | Sierra Leone | 0.2500 | NaN | NaN | NaN |
| Switzerland | 0.1460 | 0.1460 | NaN | Singapore | 0.1700 | NaN | NaN | NaN |
| Taiwan | 0.2000 | 0.2000 | NaN | Sint Maarten (Dutch part) | 0.3500 | NaN | NaN | NaN |
| Tajikistan | 0.1800 | 0.1800 | NaN | Slovakia | 0.2100 | NaN | NaN | NaN |
| Tanzania | 0.3000 | 0.3000 | NaN | Slovenia | 0.1900 | NaN | NaN | NaN |
| Thailand | 0.2000 | 0.2000 | NaN | Solomon Islands | 0.3000 | NaN | NaN | NaN |
| Togo | 0.2686 | 0.2686 | NaN | South Africa | 0.2700 | NaN | NaN | NaN |
| Trinidad and Tobago | 0.3000 | 0.3000 | NaN | Spain | 0.2500 | NaN | NaN | NaN |
| Tunisia | 0.1500 | 0.1500 | NaN | Sri Lanka | 0.2400 | NaN | NaN | NaN |
| Turkey | 0.2500 | 0.2500 | NaN | St Maarten | 0.3500 | NaN | NaN | NaN |
| Turks and Caicos Islands | 0.0000 | 0.0000 | NaN | Sudan | 0.3500 | NaN | NaN | NaN |
| Uganda | 0.3000 | 0.3000 | NaN | Suriname | 0.3600 | NaN | NaN | NaN |
| Ukraine | 0.1800 | 0.1800 | NaN | Swaziland | 0.2750 | NaN | NaN | NaN |
| United Arab Emirates | 0.2500 | 0.2500 | NaN | Sweden | 0.2060 | NaN | NaN | NaN |
| United Kingdom | 0.2500 | 0.2500 | NaN | Switzerland | 0.1460 | NaN | NaN | NaN |
| United States | 0.2500 | 0.2500 | NaN | Syria | 0.2800 | NaN | NaN | NaN |
| Uruguay | 0.2500 | 0.2500 | NaN | Taiwan | 0.2000 | NaN | NaN | NaN |
| Uzbekistan | 0.1500 | 0.1500 | NaN | Tajikistan | 0.1800 | NaN | NaN | NaN |
| Venezuela | 0.3400 | 0.3400 | NaN | Tanzania | 0.3000 | NaN | NaN | NaN |
| Vietnam | 0.2000 | 0.2000 | NaN | Thailand | 0.2000 | NaN | NaN | NaN |
| Zambia | 0.3500 | 0.3500 | NaN | Trinidad and Tobago | 0.3000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Tunisia | 0.1500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turkey | 0.2500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turkmenistan | 0.2000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Turks and Caicos Islands | 0.0000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uganda | 0.3000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Ukraine | 0.1800 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United Arab Emirates | 0.2500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United Kingdom | 0.2500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | United States | 0.2500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uruguay | 0.2500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Uzbekistan | 0.1500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Vanuatu | 0.0000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Venezuela | 0.3400 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Vietnam | 0.2000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Yemen | 0.2000 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Zambia | 0.3500 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Zimbabwe | 0.2472 | NaN | NaN | NaN |

## PRS Worksheet
| Country | PRS Score | Total Equity Risk Premium | Rating-based Default Spread | Final ERP | Tax Rate | CRP | Unnamed: 7 | PRS Score.1 | Unnamed: 9 | Unnamed: 10 | Unnamed: 11 | Unnamed: 12 | Country.1 | PRS Score in June 2024 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Abu Dhabi | NaN | 0.047229 | 0.004645 | 0.047229 | 0.1500 | 0.006029 | NaN | More than | Less than | ERP | Default Spread | Rating | Albania | 70.75 |
| Albania | 70.75 | 0.096177 | 0.042354 | 0.096177 | 0.1500 | 0.054977 | NaN | 0 | 50 | 0.268358 | 0.175 | Below Ca | Algeria | 69.25 |
| Andorra (Principality of) | NaN | 0.060722 | 0.015039 | 0.060722 | 0.1898 | 0.019522 | NaN | 50.001 | 55 | 0.187758 | 0.112906 | Ca | Angola | 64.75 |
| Angola | 64.75 | 0.120579 | 0.061153 | 0.120579 | 0.2500 | 0.079379 | NaN | 55.001 | 57 | 0.163355 | 0.094107 | Caa3 | Argentina | 59.25 |
| Argentina | 59.25 | 0.187758 | 0.112906 | 0.187758 | 0.3500 | 0.146558 | NaN | 57.001 | 60 | 0.151154 | 0.084707 | Caa2 | Armenia | 65.00 |
| Armenia | 65.00 | 0.085124 | 0.033839 | 0.085124 | 0.1800 | 0.043924 | NaN | 60.001 | 62 | 0.132781 | 0.070553 | Caa1 | Australia | 79.50 |
| Aruba | NaN | 0.068043 | 0.020679 | 0.068043 | 0.2500 | 0.026843 | NaN | 62.001 | 64 | 0.120579 | 0.061153 | B3 | Austria | 77.25 |
| Australia | 79.50 | 0.041200 | 0.000000 | 0.041200 | 0.3000 | 0.000000 | NaN | 64.001 | 66 | 0.108378 | 0.051753 | B2 | Azerbaijan | 72.75 |
| Austria | 77.25 | 0.046080 | 0.003760 | 0.046080 | 0.2400 | 0.004880 | NaN | 66.001 | 68 | 0.096177 | 0.042354 | B1 | Bahamas | 76.75 |
| Azerbaijan | 72.75 | 0.071775 | 0.023554 | 0.071775 | 0.2000 | 0.030575 | NaN | 68.001 | 69 | 0.085124 | 0.033839 | Ba3 | Bahrain | 72.50 |
| Bahamas | 76.75 | 0.096177 | 0.042354 | 0.096177 | 0.0000 | 0.054977 | NaN | 69.001 | 72 | 0.077947 | 0.02831 | Ba2 | Bangladesh | 65.00 |
| Bahrain | 72.50 | 0.108378 | 0.051753 | 0.108378 | 0.0000 | 0.067178 | NaN | 72.001 | 74 | 0.064454 | 0.017915 | Baa2 | Belarus | 61.50 |
| Bangladesh | 65.00 | 0.096177 | 0.042354 | 0.096177 | 0.3000 | 0.054977 | NaN | 74.001 | 76 | 0.060722 | 0.015039 | Baa1 | Belgium | 74.50 |
| Barbados | NaN | 0.120579 | 0.061153 | 0.120579 | 0.0550 | 0.079379 | NaN | 76.001 | 80 | 0.051535 | 0.007962 | A2 | Bolivia | 64.25 |
| Belarus | 61.50 | 0.268358 | 0.175000 | 0.268358 | 0.1800 | 0.227158 | NaN | 80.001 | 82.5 | 0.048521 | 0.00564 | Aa3 | Botswana | 79.25 |
| Belgium | 74.50 | 0.048521 | 0.005640 | 0.048521 | 0.2500 | 0.007321 | NaN | 82.501 | 85 | 0.04608 | 0.00376 | Aa1 | Brazil | 69.50 |
| Belize | NaN | 0.151154 | 0.084707 | 0.151154 | 0.2853 | 0.109954 | NaN | 85.001 | 90.0001 | 0.0412 | 0 | Aaa | Brunei | 81.75 |
| Benin | NaN | 0.096177 | 0.042354 | 0.096177 | 0.3000 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Bulgaria | 70.75 |
| Bermuda | NaN | 0.051535 | 0.007962 | 0.051535 | 0.0000 | 0.010335 | NaN | Rating | Updated Default Spread (7/124) | NaN | NaN | NaN | Burkina Faso | 59.50 |
| Bolivia | 64.25 | 0.163355 | 0.094107 | 0.163355 | 0.2500 | 0.122155 | NaN | Aaa | 0 | NaN | NaN | NaN | Cameroon | 61.00 |
| Bosnia and Herzegovina | NaN | 0.120579 | 0.061153 | 0.120579 | 0.1000 | 0.079379 | NaN | Aa1 | 0.00376 | NaN | NaN | NaN | Canada | 81.75 |
| Botswana | 79.25 | 0.055841 | 0.011280 | 0.055841 | 0.2200 | 0.014641 | NaN | Aa2 | 0.004645 | NaN | NaN | NaN | Chile | 72.75 |
| Brazil | 69.50 | 0.077947 | 0.028310 | 0.077947 | 0.3400 | 0.036747 | NaN | Aa3 | 0.00564 | NaN | NaN | NaN | China, Peoples' Rep. | 71.00 |
| Bulgaria | 70.75 | 0.060722 | 0.015039 | 0.060722 | 0.1000 | 0.019522 | NaN | A1 | 0.006635 | NaN | NaN | NaN | Colombia | 64.00 |
| Burkina Faso | 59.50 | 0.132781 | 0.070553 | 0.132781 | 0.2800 | 0.091581 | NaN | A2 | 0.007962 | NaN | NaN | NaN | Congo, Dem. Republic | 56.75 |
| Cambodia | NaN | 0.108378 | 0.051753 | 0.108378 | 0.2000 | 0.067178 | NaN | A3 | 0.01128 | NaN | NaN | NaN | Congo, Republic | 66.75 |
| Cameroon | 61.00 | 0.132781 | 0.070553 | 0.132781 | 0.3300 | 0.091581 | NaN | Baa1 | 0.015039 | NaN | NaN | NaN | Costa Rica | 75.75 |
| Canada | 81.75 | 0.041200 | 0.000000 | 0.041200 | 0.2650 | 0.000000 | NaN | Baa2 | 0.017915 | NaN | NaN | NaN | Cote d'Ivoire | 66.00 |
| Cape Verde | NaN | 0.120579 | 0.061153 | 0.120579 | 0.0000 | 0.079379 | NaN | Baa3 | 0.020679 | NaN | NaN | NaN | Croatia | 76.00 |
| Cayman Islands | NaN | 0.048521 | 0.005640 | 0.048521 | 0.0000 | 0.007321 | NaN | Ba1 | 0.023554 | NaN | NaN | NaN | Cuba | 60.75 |
| Chile | 72.75 | 0.051535 | 0.007962 | 0.051535 | 0.2700 | 0.010335 | NaN | Ba2 | 0.02831 | NaN | NaN | NaN | Cyprus | 71.25 |
| China | NaN | 0.049813 | 0.006635 | 0.049813 | 0.2500 | 0.008613 | NaN | Ba3 | 0.033839 | NaN | NaN | NaN | Czech Republic | 79.50 |
| Colombia | 64.00 | 0.064454 | 0.017915 | 0.064454 | 0.3500 | 0.023254 | NaN | B1 | 0.042354 | NaN | NaN | NaN | Denmark | 86.25 |
| Congo (Democratic Republic of) | NaN | 0.120579 | 0.061153 | 0.120579 | 0.3000 | 0.079379 | NaN | B2 | 0.051753 | NaN | NaN | NaN | Dominican Republic | 71.75 |
| Congo (Republic of) | NaN | 0.151154 | 0.084707 | 0.151154 | 0.2800 | 0.109954 | NaN | B3 | 0.061153 | NaN | NaN | NaN | Ecuador | 66.25 |
| Cook Islands | NaN | 0.096177 | 0.042354 | 0.096177 | 0.2974 | 0.054977 | NaN | Caa1 | 0.070553 | NaN | NaN | NaN | Egypt | 56.25 |
| Costa Rica | 75.75 | 0.096177 | 0.042354 | 0.096177 | 0.3000 | 0.054977 | NaN | Caa2 | 0.084707 | NaN | NaN | NaN | El Salvador | 69.75 |
| Côte d'Ivoire | NaN | 0.077947 | 0.028310 | 0.077947 | 0.2500 | 0.036747 | NaN | Caa3 | 0.094107 | NaN | NaN | NaN | Estonia | 71.50 |
| Croatia | 76.00 | 0.064454 | 0.017915 | 0.064454 | 0.1800 | 0.023254 | NaN | Ca | 0.112906 | NaN | NaN | NaN | Ethiopia | 59.75 |
| Cuba | 60.75 | 0.187758 | 0.112906 | 0.187758 | 0.2853 | 0.146558 | NaN | C | 0.175 | NaN | NaN | NaN | Finland | 77.25 |
| Curacao | NaN | 0.068043 | 0.020679 | 0.068043 | 0.2200 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | France | 71.25 |
| Cyprus | 71.25 | 0.064454 | 0.017915 | 0.064454 | 0.1250 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Gabon | 68.75 |
| Czech Republic | 79.50 | 0.048521 | 0.005640 | 0.048521 | 0.1900 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Gambia | 66.75 |
| Denmark | 86.25 | 0.041200 | 0.000000 | 0.041200 | 0.2200 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Germany | 79.75 |
| Dominican Republic | 71.75 | 0.085124 | 0.033839 | 0.085124 | 0.2700 | 0.043924 | NaN | NaN | NaN | NaN | NaN | NaN | Ghana | 61.25 |
| Ecuador | 66.25 | 0.163355 | 0.094107 | 0.163355 | 0.2500 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | Greece | 69.00 |
| Egypt | 56.25 | 0.132781 | 0.070553 | 0.132781 | 0.2250 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | Guatemala | 72.75 |
| El Salvador | 69.75 | 0.132781 | 0.070553 | 0.132781 | 0.3000 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | Guinea | 59.00 |
| Estonia | 71.50 | 0.049813 | 0.006635 | 0.049813 | 0.2000 | 0.008613 | NaN | NaN | NaN | NaN | NaN | NaN | Guinea-Bissau | 63.00 |
| Ethiopia | 59.75 | 0.151154 | 0.084707 | 0.151154 | 0.3000 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | Guyana | 74.50 |
| Fiji | NaN | 0.096177 | 0.042354 | 0.096177 | 0.2000 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Haiti | 55.00 |
| Finland | 77.25 | 0.046080 | 0.003760 | 0.046080 | 0.2000 | 0.004880 | NaN | NaN | NaN | NaN | NaN | NaN | Honduras | 66.75 |
| France | 71.25 | 0.047229 | 0.004645 | 0.047229 | 0.2500 | 0.006029 | NaN | NaN | NaN | NaN | NaN | NaN | Hong Kong | 78.00 |
| Gabon | 68.75 | 0.151154 | 0.084707 | 0.151154 | 0.3000 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | Hungary | 72.75 |
| Georgia | NaN | 0.077947 | 0.028310 | 0.077947 | 0.1500 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | Iceland | 82.00 |
| Germany | 79.75 | 0.041200 | 0.000000 | 0.041200 | 0.3000 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | India | 72.00 |
| Ghana | 61.25 | 0.163355 | 0.094107 | 0.163355 | 0.2500 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | Indonesia | 68.75 |
| Greece | 69.00 | 0.071775 | 0.023554 | 0.071775 | 0.2200 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Iran | 63.25 |
| Guatemala | 72.75 | 0.071775 | 0.023554 | 0.071775 | 0.2500 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Iraq | 61.00 |
| Guernsey (States of) | NaN | 0.049813 | 0.006635 | 0.049813 | 0.0000 | 0.008613 | NaN | NaN | NaN | NaN | NaN | NaN | Ireland | 83.00 |
| Honduras | 66.75 | 0.096177 | 0.042354 | 0.096177 | 0.2500 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Israel | 71.50 |
| Hong Kong | 78.00 | 0.048521 | 0.005640 | 0.048521 | 0.1650 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Italy | 76.75 |
| Hungary | 72.75 | 0.064454 | 0.017915 | 0.064454 | 0.0900 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Jamaica | 74.50 |
| Iceland | 82.00 | 0.051535 | 0.007962 | 0.051535 | 0.2000 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | Japan | 78.25 |
| India | 72.00 | 0.068043 | 0.020679 | 0.068043 | 0.3000 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Jordan | 63.50 |
| Indonesia | 68.75 | 0.064454 | 0.017915 | 0.064454 | 0.2200 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Kazakhstan | 75.50 |
| Iraq | 61.00 | 0.132781 | 0.070553 | 0.132781 | 0.1500 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | Kenya | 61.50 |
| Ireland | 83.00 | 0.048521 | 0.005640 | 0.048521 | 0.1250 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Korea, D.P.R. | 49.25 |
| Isle of Man | NaN | 0.048521 | 0.005640 | 0.048521 | 0.0000 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Korea, Republic | 80.50 |
| Israel | 71.50 | 0.051535 | 0.007962 | 0.051535 | 0.2300 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | Kuwait | 79.75 |
| Italy | 76.75 | 0.068043 | 0.020679 | 0.068043 | 0.2400 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Latvia | 72.25 |
| Jamaica | 74.50 | 0.096177 | 0.042354 | 0.096177 | 0.2500 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Lebanon | 34.25 |
| Japan | 78.25 | 0.049813 | 0.006635 | 0.049813 | 0.3062 | 0.008613 | NaN | NaN | NaN | NaN | NaN | NaN | Liberia | 61.50 |
| Jersey (States of) | NaN | 0.048521 | 0.005640 | 0.048521 | 0.0000 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Libya | 74.75 |
| Jordan | 63.50 | 0.085124 | 0.033839 | 0.085124 | 0.2000 | 0.043924 | NaN | NaN | NaN | NaN | NaN | NaN | Lithuania | 70.75 |
| Kazakhstan | 75.50 | 0.064454 | 0.017915 | 0.064454 | 0.2000 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Luxembourg | 84.25 |
| Kenya | 61.50 | 0.120579 | 0.061153 | 0.120579 | 0.3000 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Madagascar | 63.25 |
| Korea | NaN | 0.047229 | 0.004645 | 0.047229 | 0.2500 | 0.006029 | NaN | NaN | NaN | NaN | NaN | NaN | Malawi | 52.25 |
| Kuwait | 79.75 | 0.049813 | 0.006635 | 0.049813 | 0.1500 | 0.008613 | NaN | NaN | NaN | NaN | NaN | NaN | Malaysia | 74.75 |
| Kyrgyzstan | NaN | 0.120579 | 0.061153 | 0.120579 | 0.1000 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Mali | 59.50 |
| Laos | NaN | 0.163355 | 0.094107 | 0.163355 | 0.2686 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | Malta | 76.25 |
| Latvia | 72.25 | 0.055841 | 0.011280 | 0.055841 | 0.2000 | 0.014641 | NaN | NaN | NaN | NaN | NaN | NaN | Mexico | 68.75 |
| Lebanon | 34.25 | 0.268358 | 0.175000 | 0.268358 | 0.1700 | 0.227158 | NaN | NaN | NaN | NaN | NaN | NaN | Moldova | 64.25 |
| Liechtenstein | NaN | 0.041200 | 0.000000 | 0.041200 | 0.1250 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Mongolia | 69.75 |
| Lithuania | 70.75 | 0.051535 | 0.007962 | 0.051535 | 0.1500 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | Morocco | 67.00 |
| Luxembourg | 84.25 | 0.041200 | 0.000000 | 0.041200 | 0.2494 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Mozambique | 59.50 |
| Macao | NaN | 0.048521 | 0.005640 | 0.048521 | 0.2686 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Myanmar | 58.00 |
| Macedonia | NaN | 0.085124 | 0.033839 | 0.085124 | 0.1000 | 0.043924 | NaN | NaN | NaN | NaN | NaN | NaN | Namibia | 71.25 |
| Malaysia | 74.75 | 0.055841 | 0.011280 | 0.055841 | 0.2400 | 0.014641 | NaN | NaN | NaN | NaN | NaN | NaN | Netherlands | 81.25 |
| Maldives | NaN | 0.132781 | 0.070553 | 0.132781 | 0.2686 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | New Zealand | 77.25 |
| Mali | 59.50 | 0.151154 | 0.084707 | 0.151154 | 0.2686 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | Nicaragua | 64.00 |
| Malta | 76.25 | 0.051535 | 0.007962 | 0.051535 | 0.3500 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | Niger | 48.00 |
| Mauritius | NaN | 0.068043 | 0.020679 | 0.068043 | 0.1500 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Nigeria | 54.25 |
| Mexico | 68.75 | 0.064454 | 0.017915 | 0.064454 | 0.3000 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Norway | 87.00 |
| Moldova | 64.25 | 0.120579 | 0.061153 | 0.120579 | 0.1200 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Oman | 79.00 |
| Mongolia | 69.75 | 0.120579 | 0.061153 | 0.120579 | 0.2500 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Pakistan | 54.25 |
| Montenegro | NaN | 0.096177 | 0.042354 | 0.096177 | 0.1500 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Panama | 71.50 |
| Montserrat | NaN | 0.068043 | 0.020679 | 0.068043 | 0.2853 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Papua New Guinea | 69.00 |
| Morocco | 67.00 | 0.071775 | 0.023554 | 0.071775 | 0.3200 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Paraguay | 71.00 |
| Mozambique | 59.50 | 0.151154 | 0.084707 | 0.151154 | 0.3200 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | Peru | 70.00 |
| Namibia | 71.25 | 0.096177 | 0.042354 | 0.096177 | 0.3200 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Philippines | 71.75 |
| Netherlands | 81.25 | 0.041200 | 0.000000 | 0.041200 | 0.2580 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Poland | 76.00 |
| New Zealand | 77.25 | 0.041200 | 0.000000 | 0.041200 | 0.2800 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Portugal | 77.25 |
| Nicaragua | 64.00 | 0.108378 | 0.051753 | 0.108378 | 0.3000 | 0.067178 | NaN | NaN | NaN | NaN | NaN | NaN | Qatar | 80.75 |
| Niger | 48.00 | 0.163355 | 0.094107 | 0.163355 | 0.2686 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | Romania | 68.00 |
| Nigeria | 54.25 | 0.132781 | 0.070553 | 0.132781 | 0.3000 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | Russia | 71.25 |
| Norway | 87.00 | 0.041200 | 0.000000 | 0.041200 | 0.2200 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Saudi Arabia | 81.50 |
| Oman | 79.00 | 0.071775 | 0.023554 | 0.071775 | 0.1500 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Senegal | 63.50 |
| Pakistan | 54.25 | 0.163355 | 0.094107 | 0.163355 | 0.2900 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | Serbia | 66.50 |
| Panama | 71.50 | 0.068043 | 0.020679 | 0.068043 | 0.2500 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Sierra Leone | 58.00 |
| Papua New Guinea | 69.00 | 0.108378 | 0.051753 | 0.108378 | 0.3000 | 0.067178 | NaN | NaN | NaN | NaN | NaN | NaN | Singapore | 86.50 |
| Paraguay | 71.00 | 0.071775 | 0.023554 | 0.071775 | 0.1000 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Slovakia | 67.25 |
| Peru | 70.00 | 0.060722 | 0.015039 | 0.060722 | 0.2950 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | Slovenia | 75.25 |
| Philippines | 71.75 | 0.064454 | 0.017915 | 0.064454 | 0.2500 | 0.023254 | NaN | NaN | NaN | NaN | NaN | NaN | Somalia | 54.25 |
| Poland | 76.00 | 0.051535 | 0.007962 | 0.051535 | 0.1900 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | South Africa | 66.75 |
| Portugal | 77.25 | 0.055841 | 0.011280 | 0.055841 | 0.2100 | 0.014641 | NaN | NaN | NaN | NaN | NaN | NaN | Spain | 73.25 |
| Qatar | 80.75 | 0.047229 | 0.004645 | 0.047229 | 0.1000 | 0.006029 | NaN | NaN | NaN | NaN | NaN | NaN | Sri Lanka | 56.25 |
| Ras Al Khaimah (Emirate of) | NaN | 0.055841 | 0.011280 | 0.055841 | 0.0000 | 0.014641 | NaN | NaN | NaN | NaN | NaN | NaN | Sudan | 43.50 |
| Romania | 68.00 | 0.068043 | 0.020679 | 0.068043 | 0.1600 | 0.026843 | NaN | NaN | NaN | NaN | NaN | NaN | Suriname | 63.50 |
| Rwanda | NaN | 0.108378 | 0.051753 | 0.108378 | 0.3000 | 0.067178 | NaN | NaN | NaN | NaN | NaN | NaN | Sweden | 79.25 |
| Saudi Arabia | 81.50 | 0.049813 | 0.006635 | 0.049813 | 0.2000 | 0.008613 | NaN | NaN | NaN | NaN | NaN | NaN | Switzerland | 86.00 |
| Senegal | 63.50 | 0.085124 | 0.033839 | 0.085124 | 0.3000 | 0.043924 | NaN | NaN | NaN | NaN | NaN | NaN | Syria | 44.25 |
| Serbia | NaN | 0.077947 | 0.028310 | 0.077947 | 0.1500 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | Taiwan | 86.25 |
| Sharjah | NaN | 0.071775 | 0.023554 | 0.071775 | 0.0000 | 0.030575 | NaN | NaN | NaN | NaN | NaN | NaN | Tanzania | 66.25 |
| Singapore | 86.50 | 0.041200 | 0.000000 | 0.041200 | 0.1700 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Thailand | 71.25 |
| Slovakia | 67.25 | 0.051535 | 0.007962 | 0.051535 | 0.2100 | 0.010335 | NaN | NaN | NaN | NaN | NaN | NaN | Togo | 63.75 |
| Slovenia | 75.25 | 0.055841 | 0.011280 | 0.055841 | 0.1900 | 0.014641 | NaN | NaN | NaN | NaN | NaN | NaN | Trinidad & Tobago | 77.50 |
| Solomon Islands | NaN | 0.132781 | 0.070553 | 0.132781 | 0.3000 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | Tunisia | 61.50 |
| South Africa | 66.75 | 0.077947 | 0.028310 | 0.077947 | 0.2700 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | Turkey | 58.50 |
| Spain | 73.25 | 0.060722 | 0.015039 | 0.060722 | 0.2500 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | Uganda | 61.50 |
| Sri Lanka | 56.25 | 0.187758 | 0.112906 | 0.187758 | 0.2400 | 0.146558 | NaN | NaN | NaN | NaN | NaN | NaN | Ukraine | 60.75 |
| St. Maarten | NaN | 0.077947 | 0.028310 | 0.077947 | 0.2853 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | United Arab Emirates | 81.00 |
| St. Vincent & the Grenadines | NaN | 0.120579 | 0.061153 | 0.120579 | 0.2853 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | United Kingdom | 77.50 |
| Suriname | 63.50 | 0.163355 | 0.094107 | 0.163355 | 0.3600 | 0.122155 | NaN | NaN | NaN | NaN | NaN | NaN | United States | 71.25 |
| Swaziland | NaN | 0.120579 | 0.061153 | 0.120579 | 0.2750 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Uruguay | 73.75 |
| Sweden | 79.25 | 0.041200 | 0.000000 | 0.041200 | 0.2060 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Uzbekistan | 75.00 |
| Switzerland | 86.00 | 0.041200 | 0.000000 | 0.041200 | 0.1460 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | Venezuela | 53.00 |
| Taiwan | 86.25 | 0.048521 | 0.005640 | 0.048521 | 0.2000 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | Vietnam | 70.50 |
| Tajikistan | NaN | 0.120579 | 0.061153 | 0.120579 | 0.1800 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | Yemen, Republic | 51.50 |
| Tanzania | 66.25 | 0.096177 | 0.042354 | 0.096177 | 0.3000 | 0.054977 | NaN | NaN | NaN | NaN | NaN | NaN | Zambia | 65.50 |
| Thailand | 71.25 | 0.060722 | 0.015039 | 0.060722 | 0.2000 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | Zimbabwe | 58.00 |
| Togo | 63.75 | 0.120579 | 0.061153 | 0.120579 | 0.2686 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Trinidad and Tobago | NaN | 0.077947 | 0.028310 | 0.077947 | 0.3000 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Tunisia | 61.50 | 0.151154 | 0.084707 | 0.151154 | 0.1500 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Turkey | 58.50 | 0.120579 | 0.061153 | 0.120579 | 0.2500 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Turks and Caicos Islands | NaN | 0.060722 | 0.015039 | 0.060722 | 0.0000 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Uganda | 61.50 | 0.120579 | 0.061153 | 0.120579 | 0.3000 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Ukraine | 60.75 | 0.187758 | 0.112906 | 0.187758 | 0.1800 | 0.146558 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| United Arab Emirates | 81.00 | 0.047229 | 0.004645 | 0.047229 | 0.2500 | 0.006029 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| United Kingdom | 77.50 | 0.048521 | 0.005640 | 0.048521 | 0.2500 | 0.007321 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| United States | 71.25 | 0.041200 | 0.000000 | 0.041200 | 0.2500 | 0.000000 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Uruguay | 73.75 | 0.060722 | 0.015039 | 0.060722 | 0.2500 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Uzbekistan | 75.00 | 0.085124 | 0.033839 | 0.085124 | 0.1500 | 0.043924 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Venezuela | 53.00 | 0.268358 | 0.175000 | 0.268358 | 0.3400 | 0.227158 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Vietnam | 70.50 | 0.077947 | 0.028310 | 0.077947 | 0.2000 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Zambia | 65.50 | 0.151154 | 0.084707 | 0.151154 | 0.3500 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Row Labels | Average of Corporate Tax Rate | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Africa | 0.268573 | NaN | NaN | NaN | NaN |
| Algeria | 69.25 | NaN | 0.028310 | 0.077947 | 0.2600 | 0.036747 | NaN | NaN | Asia | 0.245583 | NaN | NaN | NaN | NaN |
| Brunei | 81.75 | NaN | 0.005640 | 0.048521 | 0.1850 | 0.007321 | NaN | NaN | Australia & New Zealand | 0.292467 | NaN | NaN | NaN | NaN |
| Gambia | 66.75 | NaN | 0.042354 | 0.096177 | 0.3100 | 0.054977 | NaN | NaN | Caribbean | 0.186386 | NaN | NaN | NaN | NaN |
| Guinea | 59.00 | NaN | 0.084707 | 0.151154 | 0.2915 | 0.109954 | NaN | NaN | Central and South America | 0.285321 | NaN | NaN | NaN | NaN |
| Guinea-Bissau | 63.00 | NaN | 0.061153 | 0.120579 | 0.2915 | 0.079379 | NaN | NaN | Eastern Europe & Russia | 0.161111 | NaN | NaN | NaN | NaN |
| Guyana | 74.50 | NaN | 0.015039 | 0.060722 | 0.1864 | 0.019522 | NaN | NaN | Middle East | 0.134615 | NaN | NaN | NaN | NaN |
| Haiti | 55.00 | NaN | 0.112906 | 0.187758 | 0.1864 | 0.146558 | NaN | NaN | North America | 0.2575 | NaN | NaN | NaN | NaN |
| Iran | 63.25 | NaN | 0.061153 | 0.120579 | 0.2023 | 0.079379 | NaN | NaN | Western Europe | 0.195162 | NaN | NaN | NaN | NaN |
| Korea, D.P.R. | 49.25 | NaN | 0.175000 | 0.268358 | 0.2310 | 0.227158 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Liberia | 61.50 | NaN | 0.070553 | 0.132781 | 0.2915 | 0.091581 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Libya | 74.75 | NaN | 0.015039 | 0.060722 | 0.2000 | 0.019522 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Madagascar | 63.25 | NaN | 0.061153 | 0.120579 | 0.2000 | 0.079379 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Malawi | 52.25 | NaN | 0.112906 | 0.187758 | 0.3000 | 0.146558 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Myanmar | 58.00 | NaN | 0.084707 | 0.151154 | 0.2500 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Russia | 71.25 | NaN | 0.028310 | 0.077947 | 0.2500 | 0.036747 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Sierra Leone | 58.00 | NaN | 0.084707 | 0.151154 | 0.3000 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Somalia | 54.25 | NaN | 0.112906 | 0.187758 | 0.2915 | 0.146558 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Sudan | 43.50 | NaN | 0.175000 | 0.268358 | 0.3500 | 0.227158 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Syria | 44.25 | NaN | 0.175000 | 0.268358 | 0.2800 | 0.227158 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Yemen, Republic | 51.50 | NaN | 0.112906 | 0.187758 | 0.2000 | 0.146558 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Zimbabwe | 58.00 | NaN | 0.084707 | 0.151154 | 0.2500 | 0.109954 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Data Update Sequence
| Updating Sequence |
| --- |
| 1. Relative Risk Worksheet |
| 2. Sovereign Ratings |
| 3. CDS Worksheet |
| 4. Default Spreads |
| 5. PRS Worksheet |
| 6. Country GDP |
| 7. Country tax rates |
| 8. Regional Weighted averages |