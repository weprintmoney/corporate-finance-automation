---
title: "Session4Slides"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valspr19/session4slides.pdf
---

27

# Discount Rates I

## The Riskfree Rate

# The Risk Free Rate: Laying the Foundations

- ¨ On a riskfree investment, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. ¨ For an investment to be riskfree, then, it has to have ¤ No default risk ¤ No reinvestment risk ¤ It follows then that if asked to estimate a risk free rate:
- 1. Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
- 2. Currencies matter: A risk free rate is currency-specific and can be very different for different currencies.
- 3. Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

# Test 1: A riskfree rate in US dollars!

- ¨ In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be
  - a. A three-month Treasury bill rate (2.3%)
  - b. A ten-year Treasury bond rate (2.7%)
  - c. A thirty-year Treasury bond rate (3.2%)
  - d. A TIPs (inflation-indexed treasury) rate (0.88%)
  - e. None of the above

What are we implicitly assuming about the US treasury when we use any of the treasury numbers?

# Test 2: A Riskfree Rate in Euros?

![](_page_3_Figure_2.jpeg)

# Test 3: A Riskfree Rate in Indian Rupees

- ¨ The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 7.43% on January 1, 2019. ¨ In January 2019, the Indian government had a local currency sovereign rating of Baa2. The typical default spread (over a default free rate) for Baa2 rated country bonds in early 2018 was 2.15%. The riskfree rate in Indian Rupees is
  - a. The yield to maturity on the 10-year bond (7.43%)
  - b. The yield to maturity on the 10-year bond + Default spread (9.58%)
  - c. The yield to maturity on the 10-year bond Default spread (5.28%)
  - d. None of the above

# Sovereign Default Spread: Three paths to the same destination…

¨ Sovereign dollar or euro denominated bonds: Find sovereign bonds denominated in US dollars, issued by an emerging sovereign. ¤ Default spread = Emerging Govt Bond Rate (in US \$) – US Treasury Bond rate with same maturity. ¨ CDS spreads: Obtain the traded value for a sovereign Credit Default Swap (CDS) for the emerging government. ¤ Default spread = Sovereign CDS spread (with perhaps an adjustment for CDS market frictions). ¨ Sovereign-rating based spread: For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries with the same sovereign rating.

### Local Currency Government Bond Rates – January 2019

| Currency          | Govt Bond Rate | Currency           | Govt Bond Rate |
|-------------------|----------------|--------------------|----------------|
| Australian \$     | 2.19%          | Mexican Peso       | 8.62%          |
| Brazilian Reai    | 9.18%          | Nigerian Naira     | 15.53%         |
| British Pound     | 1.20%          | Norwegian Krone    | 1.68%          |
| Bulgarian Lev     | 0.85%          | NZ \$              | 2.32%          |
| Canadian \$       | 1.86%          | Pakistani Rupee    | 13.15%         |
| Chilean Peso      | 4.45%          | Peruvian Sol       | 5.43%          |
| Chinese Yuan      | 3.19%          | Phillipine Peso    | 6.93%          |
| Colombian Peso    | 6.77%          | Polish Zloty       | 2.72%          |
| Croatian Kuna     | 2.09%          | Qatari Dinar       | 3.89%          |
| Czech Koruna      | 1.73%          | Romanian Leu       | 4.72%          |
| Danish Krone      | 0.14%          | Russian Ruble      | 8.68%          |
| Euro              | 0.15%          | Singapore \$       | 2.05%          |
| HK \$             | 1.92%          | South African Rand | 8.85%          |
| Hungarian Forint  | 2.84%          | Swedish Krona      | 0.40%          |
| Iceland Krona     | 5.44%          | Swiss Franc        | -0.24%         |
| Indian Rupee      | 7.43%          | Taiwanese \$       | 0.84%          |
| Indonesian Rupiah | 8.08%          | Thai Baht          | 2.40%          |
| Israeli Shekel    | 2.22%          | Turkish Lira       | 16.34%         |
| Japanese Yen      | 0.00%          | US \$              | 2.68%          |
| Kenyan Shilling   | 12.25%         | Venezuelan Bolivar | 20.43%         |
| Korean Won        | 1.95%          | Vietnamese Dong    | 5.17%          |
| Malyasian Ringgit | 4.08%          |                    |                |

### Approach 1: Default spread from Government Bonds

| Country  | \$ Bond Rate | Riskfree Rate \$ Bonds | Default Spread |
|----------|--------------|------------------------|----------------|
| Peru     | 3.66%        | 2.68%                  | 0.98%          |
| Brazil   | 3.98%        | 2.68%                  | 1.30%          |
| Colombia | 3.88%        | 2.68%                  | 1.20%          |
| Poland   | 3.22%        | 2.68%                  | 0.54%          |
| Turkey   | 6.31%        | 2.68%                  | 3.63%          |
| Mexico   | 3.90%        | 2.68%                  | 1.22%          |
| Russia   | 4.72%        | 2.68%                  | 2.04%          |
| Bulgaria | 1.46%        | 0.15%                  | 1.31%          |

# Approach 2: CDS Spreads – January 2019

| Country        | 1/1/19       | Net of US    | Country     | 1/1/19 | Net of US | Country        | 1/1/19 | Net of US |
|----------------|--------------|--------------|-------------|--------|-----------|----------------|--------|-----------|
| Abu Dhabi      | 1.12%        | 0.82%        | Guatamela   | 2.55%  | 2.25%     | Peru           | 1.61%  | 1.31%     |
| Algeria        | 1.24%        | 0.94%        | Hong Kong   | 0.67%  | 0.37%     | Philippines    | 1.44%  | 1.14%     |
| Angola         | 5.79%        | 5.49%        | Hungary     | 1.40%  | 1.10%     | Poland         | 1.09%  | 0.79%     |
| Argentina      | 8.20%        | 7.90%        | Iceland     | 0.80%  | 0.50%     | Portugal       | 1.36%  | 1.06%     |
| Australia      | 0.42%        | 0.12%        | India       | 1.85%  | 1.55%     | Qatar          | 1.29%  | 0.99%     |
| Austria        | 0.30%        | 0.00%        | Indonesia   | 2.18%  | 1.88%     | Romania        | 1.52%  | 1.22%     |
| Bahrain        | 3.72%        | 3.42%        | Iraq        | 6.10%  | 5.80%     | Russia         | 2.05%  | 1.75%     |
| Belgium        | 0.49%        | 0.19%        | Ireland     | 0.68%  | 0.38%     | Rwanda         | 4.36%  | 4.06%     |
| <b>Brazil</b>  | <b>2.87%</b> | <b>2.57%</b> | Israel      | 1.11%  | 0.81%     | Saudi Arabia   | 1.50%  | 1.20%     |
| Bulgaria       | 1.30%        | 1.00%        | Italy       | 2.44%  | 2.14%     | Senegal        | 4.41%  | 4.11%     |
| Cameroon       | 6.02%        | 5.72%        | Japan       | 0.44%  | 0.14%     | Serbia         | 1.65%  | 1.35%     |
| Canada         | 0.53%        | 0.23%        | Kazakhstan  | 1.32%  | 1.02%     | Slovakia       | 0.87%  | 0.57%     |
| Chile          | 1.11%        | 0.81%        | Kenya       | 5.90%  | 5.60%     | Slovenia       | 1.39%  | 1.09%     |
| China          | 1.14%        | 0.84%        | Korea       | 0.64%  | 0.34%     | South Africa   | 2.92%  | 2.62%     |
| Colombia       | 2.37%        | 2.07%        | Kuwait      | 1.17%  | 0.87%     | Spain          | 1.20%  | 0.90%     |
| Costa Rica     | 4.43%        | 4.13%        | Latvia      | 1.13%  | 0.83%     | Sweden         | 0.26%  | -0.04%    |
| Croatia        | 1.51%        | 1.21%        | Lebanon     | 7.92%  | 7.62%     | Switzerland    | 0.26%  | -0.04%    |
| Cyprus         | 1.57%        | 1.27%        | Lithuania   | 1.14%  | 0.84%     | Thailand       | 0.84%  | 0.54%     |
| Czech Republic | 0.75%        | 0.45%        | Malaysia    | 1.77%  | 1.47%     | Tunisia        | 3.71%  | 3.41%     |
| Denmark        | 0.26%        | -0.04%       | Mexico      | 2.35%  | 2.05%     | Turkey         | 4.19%  | 3.89%     |
| Dubai          | 1.71%        | 1.41%        | Morocco     | 1.65%  | 1.35%     | Ukraine        | 7.63%  | 7.33%     |
| Egypt          | 4.58%        | 4.28%        | Netherlands | 0.30%  | 0.00%     | United Kingdom | 0.61%  | 0.31%     |
| El Salvador    | 5.38%        | 5.08%        | New Zealand | 0.39%  | 0.09%     | United States  | 0.30%  | 0.00%     |
| Estonia        | 0.87%        | 0.57%        | Nigeria     | 4.51%  | 4.21%     | Uruguay        | 2.39%  | 2.09%     |
| Finland        | 0.28%        | -0.02%       | Norway      | 0.26%  | -0.04%    | Venezuela      | NA     | NA        |
| France         | 0.61%        | 0.31%        | Oman        | 4.23%  | 3.93%     | Vietnam        | 2.44%  | 2.14%     |
| Germany        | 0.29%        | -0.01%       | Pakistan    | 5.09%  | 4.79%     |                |        |           |
| Greece         | 5.10%        | 4.80%        | Panama      | 1.42%  | 1.12%     |                |        |           |

### Approach 3: Typical Default Spreads: January 2019

| S&P Sovereign Rating | Moody's Sovereign Rating | Default Spread |
|----------------------|--------------------------|----------------|
| AAA                  | Aaa                      | 0.00%          |
| AA+                  | Aa1                      | 0.45%          |
| AA                   | Aa2                      | 0.56%          |
| AA-                  | Aa3                      | 0.68%          |
| A+                   | A1                       | 0.79%          |
| A                    | A2                       | 0.96%          |
| A-                   | A3                       | 1.35%          |
| BBB+                 | Baa1                     | 1.80%          |
| BBB                  | Baa2                     | 2.15%          |
| BBB-                 | Baa3                     | 2.48%          |
| BB+                  | Ba1                      | 2.82%          |
| BB                   | Ba2                      | 3.39%          |
| BB                   | Ba3                      | 4.06%          |
| B+                   | B1                       | 5.08%          |
| B                    | B2                       | 6.21%          |
| B-                   | B3                       | 7.34%          |
| CCC+                 | Caa1                     | 8.46%          |
| CCC                  | Caa2                     | 10.16%         |
| CCC-                 | Caa3                     | 11.28%         |
| CC+                  | Ca1                      | 13.54%         |
| CC                   | Ca2                      | 15.41%         |
| CC-                  | Ca3                      | 17.06%         |
| C+                   | C1                       | 19.81%         |
| C                    | C2                       | 22.02%         |
| C-                   | C3                       | 27.52%         |

# Getting to a risk free rate in a currency: Example

- □ The Brazilian government bond rate in nominal reals on January 1, 2019 was 9.18%. To get to a riskfree rate in nominal reals, we can use one of three approaches.
  - □ Approach 1: Government Bond spread
    - ❑ The 2023 Brazil bond, denominated in US dollars, has a spread of 1.30% over the US treasury bond rate.
    - ❑ Riskfree rate in  $\$R = 9.18\% - 1.30\% = 7.88\%$
  - □ Approach 2: The CDS Spread
    - ❑ The CDS spread for Brazil, adjusted for the US CDS spread was 2.57%.
    - ❑ Riskfree rate in  $\$R = 9.18\% - 2.57\% = 6.61\%$
  - □ Approach 3: The Rating based spread
    - ❑ Brazil has a Ba2 local currency rating from Moody's. The default spread for that rating is 3.39%
    - ❑ Riskfree rate in  $\$R = 9.18\% - 3.39\% = 5.79\%$

# Test 4: A Real Riskfree Rate

- ¨ In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms. ¨ To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination. ¨ In January 2019, the yield on a 10-year indexed treasury bond was 0.88%. Which of the following statements would you subscribe to?
  - a. This (0.88%) is the real riskfree rate to use, if you are valuing US companies in real terms.
  - b. This (0.88%) is the real riskfree rate to use, anywhere in the world

Explain.

### No default free entity: Choices with riskfree rates….

¨ Estimate a range for the riskfree rate in local terms: ¤ Approach 1: Subtract default spread from local government bond rate: Government bond rate in local currency terms - Default spread for Government in local currency ¤ Approach 2: Use forward rates and the riskless rate in an index currency (say Euros or dollars) to estimate the riskless rate in the local currency. ¨ Do the analysis in real terms (rather than nominal terms) using a real riskfree rate, which can be obtained in one of two ways – ¤ from an inflation-indexed government bond, if one exists ¤ set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done. ¨ Do the analysis in a currency where you can get a riskfree rate, say US dollars or Euros.

# Risk free Rate: Don't have or trust the government bond rate?

1. 1. Build up approach: The risk free rate in any currency can be written as the sum of two variables:

Risk free rate = Expected Inflation in currency + Expected real interest rate

The expected real interest rate can be computed in one of two ways: from the US TIPs rate or set equal to real growth in the economy. Thus, if the expected inflation rate in a country is expected to be 15% and the TIPs rate is 1%, the risk free rate is 16%.

1. 2. US \$ rate & Differential Inflation: Alternatively, you can scale up the US \$ risk free rate by the differential inflation between the US \$ and the currency in question:

$$\text{Risk free rate}_{\text{Currency}} = \frac{(1 + \text{Risk free rate}_{\text{US \$}}) \frac{(1 + \text{Expected Inflation}_{\text{Foreign currency}})}{(1 + \text{Expected Inflation}_{\text{US \$}})} - 1$$

Thus, if the US \$ risk free rate is 2.00%, the inflation rate in the foreign currency is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

$$\text{Risk free rate} = (1.02) \frac{(1.15)}{(1.015)} - 1 = 15.57\%$$

### Why do risk free rates vary across currencies? January 2019 Risk free rates

![](_page_14_Figure_2.jpeg)

# One more test on riskfree rates…

- ¨ On January 1, 2019, the 10-year treasury bond rate in the United States was 2.68%, low by historic standards. Assume that you were valuing a company in US dollars then, but were wary about the risk free rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate.
  - c. Something else…

# Some perspective on risk free rates

![](_page_16_Figure_2.jpeg)

| Period      | T.Bond rate | Inflation rate | Real GDP growth | Intrinsic Riskfree Rate | T.Bond - Intrinsic Rate | Smoothed Intrinsic Riskfree Rate | T.Bond Rate - Smoothed Intrinsic Rate |
|-------------|-------------|----------------|-----------------|-------------------------|-------------------------|----------------------------------|---------------------------------------|
| 1954-2017   | 5.82%       | 3.57%          | 3.03%           | 6.60%                   | -0.77%                  | 6.85%                            | -1.02%                                |
| 1954-1980   | 5.83%       | 4.49%          | 3.50%           | 7.98%                   | -2.15%                  | 7.10%                            | -1.27%                                |
| 1981-2008   | 6.88%       | 3.26%          | 3.04%           | 6.30%                   | 0.58%                   | 7.59%                            | -0.71%                                |
| 2009-2018   | 2.55%       | 1.86%          | 1.72%           | 3.58%                   | -1.03%                  | 3.77%                            | -1.22%                                |
| End of 2011 | 2.68%       | 2.54%          | 3.00%           | 5.54%                   | -2.86%                  | 3.58%                            | -0.90%                                |

# Negative Interest Rates?

¨ In 2017, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates? ¨ How negative can rates get? (Is there a bound?) ¨ Would you use these negative interest rates as risk free rates? ¤ If no, why not and what would you do instead? ¤ If yes, what else would you have to do in your valuation to be internally consistent?

45

# Discount Rates: II

## The Equity Risk Premium

### II. The Equity Risk Premium The ubiquitous historical risk premium

¨ The historical premium is the premium that stocks have historically earned over riskless securities. ¨ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to ¤ How far back you go in history… ¤ Whether you use T.bill rates or T.Bond rates ¤ Whether you use geometric or arithmetic averages. ¨ For instance, looking at the US:

|           | Stocks - T. Bills | Arithmetic Average Stocks - T. Bonds | Stocks - T. Bills | Geometric Average Stocks - T. Bonds |
|-----------|-------------------|--------------------------------------|-------------------|-------------------------------------|
| 1928-2018 | 7.93%             | 6.26%                                | 6.11%             | 4.66%                               |
| Std Error | 2.09%             | 2.22%                                |                   |                                     |
| 1969-2018 | 6.34%             | 4.00%                                | 5.01%             | 3.04%                               |
| Std Error | 2.38%             | 2.71%                                |                   |                                     |
| 2009-2018 | 13.00%            | 11.21%                               | 12.48%            | 11.00%                              |
| Std Error | 3.71%             | 5.50%                                |                   |                                     |

# The perils of trusting the past.....

47

- □ Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 80 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

Standard Error in Premium =  $20\%/\sqrt{80} = 2.26\%$ 

- □ Survivorship Bias: Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

### Risk Premium for a Mature Market? Broadening the sample to 1900-2017

| <i>Country</i> | <i>Geometric Mean</i> | <i>Standard Error</i> |
|----------------|-----------------------|-----------------------|
| Australia      | 5.00%                 | 1.70%                 |
| Austria        | 2.90%                 | 14.10%                |
| Belgium        | 2.20%                 | 1.90%                 |
| Canada         | 3.50%                 | 1.70%                 |
| Denmark        | 2.20%                 | 1.70%                 |
| Finland        | 5.20%                 | 2.70%                 |
| France         | 3.10%                 | 2.10%                 |
| Germany        | 5.10%                 | 2.60%                 |
| Ireland        | 2.70%                 | 1.80%                 |
| Italy          | 3.20%                 | 2.70%                 |
| Japan          | 5.10%                 | 3.00%                 |
| Netherlands    | 3.30%                 | 2.00%                 |
| New Zealand    | 4.00%                 | 1.60%                 |
| Norway         | 2.40%                 | 2.50%                 |
| Portugal       | 5.30%                 | 2.90%                 |
| South Africa   | 5.30%                 | 1.80%                 |
| Spain          | 1.80%                 | 1.90%                 |
| Sweden         | 3.10%                 | 2.00%                 |
| Switzerland    | 2.20%                 | 1.60%                 |
| U.K.           | 3.70%                 | 1.60%                 |
| U.S.           | 4.40%                 | 1.90%                 |
| Europe         | 3.00%                 | 1.40%                 |
| World-ex U.S.  | 2.80%                 | 1.30%                 |
| World          | 3.20%                 | 1.40%                 |

# The simplest way of estimating an additional country risk premium: The country default spread

- ❑ Default spread for country: In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - ❑ The default spread on a dollar denominated bond issued by the country. (In January 2019, that spread was % for the Brazilian \$ bond) was 1.30%.
  - ❑ The sovereign CDS spread for the country. In January 2019, the ten year CDS spread for Brazil, adjusted for the US CDS, was 2.57%.
  - ❑ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Ba2 and the default spread for a Ba2 rated sovereign was about 3.39% in January 2019.
- ❑ Add the default spread to a “mature” market premium: This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 5.96%.
  - ❑ Country Risk Premium for Brazil = 3.39%
  - ❑ Total ERP for Brazil = 5.96% + 3.39% = 9.35%

### An equity volatility based approach to estimating the country total ERP

- ❑ This approach draws on the standard deviation of two equity markets, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ❑  $\text{Total equity risk premium} = \text{Risk Premium}_{\text{US}}^* \sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$
- ❑ The country equity risk premium is based upon the volatility of the market in question relative to U.S market.
  - ❑ Assume that the equity risk premium for the US is 5.69%.
  - ❑ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ❑  $\text{Total Equity Risk Premium for Brazil} = 5.96\% (30\%/18\%) = 9.93\%$
  - ❑  $\text{Country equity risk premium for Brazil} = 9.93\% - 5.96\% = 3.97\%$