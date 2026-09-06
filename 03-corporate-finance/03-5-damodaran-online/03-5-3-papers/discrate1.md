---
title: "Discrate1"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/discrate1.pdf
---

![](_page_0_Picture_4.jpeg)

# DISCOUNT RATES I

The Riskfree Rate

# THE RISK FREE RATE: LAYING THE FOUNDATIONS

- ▪ On a riskfree investment, the actual return is equal to the expected return. Therefore, there is no variance around the expected return.
- ▪ For an investment to be riskfree, then, it has to have
  - ▪ No default risk
  - ▪ No reinvestment risk
- ▪ It follows then that if asked to estimate a risk free rate:
  - ▪ Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
  - ▪ Currencies matter: A risk free rate is currency-specific and can be very different for different currencies.
  - ▪ Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

# TEST 1: A RISKFREE RATE IN US DOLLARS!

- ▪ In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be
  - a. A three-month Treasury bill rate (4.36%)
  - b. A ten-year Treasury bond rate (4.58%)
  - c. A thirty-year Treasury bond rate (4.80%)
  - d. A TIPs (inflation-indexed treasury) rate (2.26%)
  - e. The highest of these numbers
  - f. The lowest of these numbers
  - g. Other (Specify)
- ▪ What are we implicitly assuming about the US treasury when we use any of the treasury numbers?

# TEST 2: A RISKFREE RATE IN EUROS?

Ten-year Euro Government Bond Rates on 1/1/25

![](_page_3_Figure_62.jpeg)

# TEST 3: A RISKFREE RATE IN INDIAN RUPEES

- ▪ The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 6.82% on January 1, 2025.
- ▪ In January 2025, the Indian government had a local currency sovereign rating of Baa3. The typical default spread (over a default free rate) for Baa3 rated country bonds in early 2025 was 2.18%. The riskfree rate in Indian Rupees is
  - a. The yield to maturity on the 10-year bond (6.82%)
  - b. The yield to maturity on the 10-year bond + Default spread (4.64%)
  - c. The yield to maturity on the 10-year bond – Default spread (9.00%)
  - d. None of the above

# SOVEREIGN DEFAULT SPREAD: THREE PATHS TO THE SAME DESTINATION...

- ▪ **Sovereign dollar or euro denominated bonds:** Find sovereign bonds denominated in US dollars, issued by an emerging sovereign.
  - ▪ Default spread = Emerging Govt Bond Rate (in US \$) – US Treasury Bond rate with same maturity.
- ▪ **Sovereign CDS spreads:** Obtain the traded value for a sovereign Credit Default Swap (CDS) for the emerging government.
  - ▪ Default spread = Sovereign CDS spread (with perhaps an adjustment for CDS market frictions).
- ▪ **Sovereign-rating based spread:** For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries with the same sovereign rating.

# APPROACH 1: DEFAULT SPREAD FROM GOVERNMENT BONDS

| Country    | \$ Bond Rate | Riskfree Rate | Default Spread |
|------------|--------------|---------------|----------------|
| \$ Bonds   |              |               |                |
| Peru       | 6.15%        | 4.58%         | 1.57%          |
| Brazil     | 7.75%        | 4.58%         | 3.17%          |
| Colombia   | 6.95%        | 4.58%         | 2.37%          |
| Poland     | 5.35%        | 4.58%         | 0.77%          |
| Turkey     | 13.55%       | 4.58%         | 8.97%          |
| Mexico     | 5.46%        | 4.58%         | 0.88%          |
| Euro Bonds |              |               |                |
| Bulgaria   | 2.86%        | 2.43%         | 0.43%          |

# APPROACH 2: CDS SPREADS – JANUARY 2025

| Country        | CDS Spread   | CDS Spread net of US | Country    | CDS Spread | CDS Spread net of US | Country      | CDS Spread | CDS Spread net of US | Country        | CDS Spread | CDS Spread net of US |
|----------------|--------------|----------------------|------------|------------|----------------------|--------------|------------|----------------------|----------------|------------|----------------------|
| Abu Dhabi      | 0.76%        | 0.35%                | Estonia    | 0.81%      | 0.40%                | Lithuania    | 0.96%      | 0.55%                | Serbia         | 1.26%      | 0.85%                |
| Algeria        | 1.47%        | 1.06%                | Ethiopia   | 32.97%     | 32.56%               | Malaysia     | 0.85%      | 0.44%                | Slovakia       | 0.55%      | 0.14%                |
| Angola         | 6.74%        | 6.33%                | Finland    | 0.33%      | 0.00%                | Mexico       | 2.22%      | 1.81%                | Slovenia       | 0.72%      | 0.31%                |
| Argentina      | 10.84%       | 10.43%               | France     | 0.69%      | 0.28%                | Mongolia     | 2.89%      | 2.48%                | South Africa   | 3.00%      | 2.59%                |
| Australia      | 0.18%        | 0.00%                | Gabon      | 9.61%      | 9.20%                | Morocco      | 1.51%      | 1.10%                | Spain          | 0.67%      | 0.26%                |
| Austria        | 0.26%        | 0.00%                | Germany    | 0.28%      | 0.00%                | Namibia      | 3.44%      | 3.03%                | Sri Lanka      | NA         | NA                   |
| Bahrain        | 2.51%        | 2.10%                | Greece     | 1.17%      | 0.76%                | Netherlands  | 0.25%      | 0.00%                | Sweden         | 0.20%      | 0.00%                |
| Belgium        | 0.43%        | 0.02%                | Guatemala  | 2.33%      | 1.92%                | New Zealand  | 0.20%      | 0.00%                | Switzerland    | 0.14%      | 0.00%                |
| <b>Brazil</b>  | <b>3.23%</b> | <b>2.82%</b>         | Hong Kong  | 0.64%      | 0.23%                | Nicaragua    | 6.57%      | 6.16%                | Thailand       | 0.70%      | 0.29%                |
| Bulgaria       | 1.43%        | 1.02%                | Hungary    | 1.79%      | 1.38%                | Nigeria      | 6.44%      | 6.03%                | Tunisia        | 10.24%     | 9.83%                |
| Cameroon       | 7.07%        | 6.66%                | Iceland    | 0.31%      | 0.00%                | Norway       | 0.19%      | 0.00%                | Turkey         | 3.62%      | 3.21%                |
| Canada         | 0.38%        | 0.00%                | India      | 0.95%      | 0.54%                | Oman         | 1.63%      | 1.22%                | Ukraine        | NA         | NA                   |
| Chile          | 1.17%        | 0.76%                | Indonesia  | 1.31%      | 0.90%                | Pakistan     | 16.49%     | 16.08%               | United Kingdom | 0.39%      | 0.00%                |
| China          | 0.97%        | 0.56%                | Iraq       | 4.15%      | 3.74%                | Panama       | 3.08%      | 2.67%                | United States  | 0.41%      | 0.00%                |
| Colombia       | 3.37%        | 2.96%                | Ireland    | 0.31%      | 0.00%                | Peru         | 1.47%      | 1.06%                | Uruguay        | 1.27%      | 0.86%                |
| Costa Rica     | 2.45%        | 2.04%                | Israel     | 1.44%      | 1.03%                | Philippines  | 1.21%      | 0.80%                | Venezuela      | 10.08%     | 9.67%                |
| Croatia        | 1.26%        | 0.85%                | Italy      | 1.18%      | 0.77%                | Poland       | 1.05%      | 0.64%                | Vietnam        | 1.65%      | 1.24%                |
| Cyprus         | 0.99%        | 0.58%                | Japan      | 0.33%      | 0.00%                | Portugal     | 0.58%      | 0.17%                | Zambia         | NA         | NA                   |
| Czech Republic | 0.50%        | 0.09%                | Kazakhstan | 1.36%      | 0.95%                | Qatar        | 0.77%      | 0.36%                |                |            |                      |
| Denmark        | 0.18%        | 0.00%                | Kenya      | 5.92%      | 5.51%                | Romania      | 2.39%      | 1.98%                |                |            |                      |
| Dubai          | 1.00%        | 0.59%                | Korea      | 0.48%      | 0.07%                | Russia       | NA         | NA                   |                |            |                      |
| Ecuador        | 19.08%       | 18.67%               | Kuwait     | 0.94%      | 0.53%                | Rwanda       | 4.55%      | 4.14%                |                |            |                      |
| Egypt          | 6.35%        | 5.94%                | Latvia     | 0.85%      | 0.44%                | Saudi Arabia | 1.05%      | 0.64%                |                |            |                      |
| El Salvador    | 4.20%        | 3.79%                | Lebanon    | NA         | NA                   | Senegal      | 6.23%      | 5.82%                |                |            |                      |

# APPROACH 3: TYPICAL DEFAULT SPREADS: JANUARY 2024

| S&P Sovereign Rating | Moody's Sovereign Rating | Default Spread |
|----------------------|--------------------------|----------------|
| AAA                  | Aaa                      | 0.00%          |
| AA+                  | Aa1                      | 0.38%          |
| AA                   | Aa2                      | 0.46%          |
| AA-                  | Aa3                      | 0.56%          |
| A+                   | A1                       | 0.66%          |
| A                    | A2                       | 0.80%          |
| A-                   | A3                       | 1.13%          |
| BBB+                 | Baa1                     | 1.50%          |
| BBB                  | Baa2                     | 1.79%          |
| BBB-                 | Baa3                     | 2.07%          |
| BB+                  | Ba1                      | 2.36%          |
| BB                   | Ba2                      | 2.83%          |
| BB                   | Ba3                      | 3.38%          |
| B+                   | B1                       | 4.24%          |
| B                    | B2                       | 5.18%          |
| B-                   | B3                       | 6.12%          |
| CCC+                 | Caa1                     | 7.06%          |
| CCC                  | Caa2                     | 8.47%          |
| CCC-                 | Caa3                     | 9.41%          |
| CC+                  | Ca1                      | 10.50%         |
| CC                   | Ca2                      | 11.29%         |
| CC-                  | Ca3                      | 13.00%         |
| C+                   | C1                       | 14.50%         |
| C                    | C2                       | 16.00%         |
| C-                   | C3                       | 18.00%         |

# GETTING TO A RISK FREE RATE IN BRAZILIAN REAIS ON JANUARY 1, 2024

- ▪ The Brazilian government bond rate in nominal reais on January 1, 2025, was 12.30%. To get to a riskfree rate in nominal reais, we can use one of three approaches.
  - ▪ **Approach 1: Government Bond spread**
    - ▪ Default Spread = Brazil \$ Bond Rate – US T.Bond Rate = 5.75% - 3.88% = 3.17%
    - ▪ Riskfree rate in \$R = 12.30% - 3.17% = 9.17%
  - ▪ **Approach 2: The CDS Spread**
    - ▪ The CDS spread for Brazil, adjusted for the US CDS spread was 2.82%.
    - ▪ Riskfree rate in \$R = 12.30% - 2.82% = 9.48%
  - ▪ **Approach 3: The Rating based spread**
    - ▪ Brazil has a Ba2 local currency rating from Moody's. The default spread for that rating is 2.83%
    - ▪ Riskfree rate in \$R = 12.30% - 2.83% = 9.47%

# TEST 4: A REAL RISKFREE RATE

- ▪ In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms.
- ▪ To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination.
- ▪ In January 2025, the yield on a 10-year indexed treasury bond was 2.23%. Which of the following statements would you subscribe to?
  - a. This (2.23%) is the real riskfree rate to use, if you are valuing US companies in real terms.
  - b. This (2.23%) is the real riskfree rate to use, anywhere in the world
  - c. Explain.

# WHY DO RISK FREE RATES VARY ACROSS CURRENCIES? JANUARY 2025 RISK FREE RATES

Government-bond Based Riskfree Rates in January 2025

![](_page_11_Figure_12.jpeg)

# OR ACROSS TIME...

![](_page_12_Figure_10.jpeg)

# RISK FREE RATE: DON'T HAVE OR DON'T TRUST THE GOVERNMENT BOND RATE?

- ■ You can scale up the riskfree rate in a base currency (\$, Euros) by the differential inflation between the base currency and the currency in question. In US \$:

- - ■ Risk free rate<sub>Currency</sub> =  $(1 + \text{Riskfree rate}_{US \$}) \frac{(1 + \text{Expected Inflation}_{\text{Foreign Currency}})}{(1 + \text{Expected Inflation}_{US \$})} - 1$

- ■ Thus, if the US \$ risk free rate is 2.00%, the inflation rate in Egyptian pounds is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

- - ■ Risk free rate =  $(1.02) \frac{(1.15)}{(1.015)} - 1 = 15.57\%$

# ONE MORE TEST ON RISKFREE RATES...

- ■ On January 1, 2022, the 10-year treasury bond rate in the United States was 1.51%, low by historic standards. Assume that you are valuing a company in US dollars then but are wary about the riskfree rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate.
  - c. Something else...

# SOME PERSPECTIVE ON RISK FREE RATES

![](_page_15_Figure_10.jpeg)

# NEGATIVE INTEREST RATES?

- ■ In 2022, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates?
  - ■ How negative can rates get? (Is there a lower bound?)
  - ■ Would you use these negative interest rates as risk free rates?
    - a. If no, why not and what would you do instead?
    - b. If yes, what else would you have to do in your valuation to be internally consistent?

![](_page_17_Picture_12.jpeg)

# DISCOUNT RATES: II

The price of risk

# THE DRIVERS OF EQUITY RISK PREMIUMS

## Risk Aversion

Thesis: As investors become more (less) risk averse, equity risk premiums should rise (fall).  
Implication: Markets with aging investors should have higher risk premiums that markets with younger investors.

## Economic Uncertainty

Thesis: As uncertainty about the economy increases (decreases), equity risk premiums should increase (decrease).  
Implication: Equity risk premiums should rise during economic crises, and be higher in younger & growing economies.

## Inflation and Interest Rates

Thesis: As inflation rises (falls), uncertainty about inflation will increase (decrease), pushing up (down) equity risk premiums.  
Implication: Equity risk premiums should rise during periods of high and volatile inflation.

## Information

Thesis: As corporate disclosures becomes more (less) informative, equity risk premiums should fall (rise).  
Implication: Markets with better disclosure rules and requirements should have lower equity risk premiums that markets without.

Equity Risk Premium

## Liquidity and Fund Flows

Thesis: As liquidity increases and funds flow into equity markets, equity risk premiums should decrease.  
Implication: Events or actions (crises, regulation) that stymie fund flows and liquidity will increase equity risk premiums

## Catastrophic Risk

Thesis: As the likelihood of catastrophic events (low probability events with large consequences) increases, equity risk premiums should rise.  
Implication: As investor worries about large consequence events (pandemics, nuclear war) increases, equity risk premiums will go up.

## Government Policy

Thesis: Governments that are more capricious, with changing economic rules/policies, will give rise to higher equity risk premiums.  
Implication: Equity risk premiums should be higher in countries/markets where there is less continuity in economic policy and regulation.

## Central Banks & Monetary Policy

Thesis: Central banks that are less predictable in policy responses and more inconsistent in their actions will push up equity risk premiums.  
Implication: As monetary policy becomes more unpredictable, for political reasons or because of inflation, equity risk premiums will rise.

# LOOKING BACK: HISTORICAL EQUITY RISK RISK PREMIUMS

- ▪ The **historical premium** is the premium that stocks have historically earned over riskless securities.
- ▪ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to
  - ▪ How far back you go in history...
  - ▪ Whether you use T.bill rates or T.Bond rates
  - ▪ Whether you use geometric or arithmetic averages.
- ▪ For instance, looking at the US:

|           | <i>Arithmetic Average</i> |                   | <i>Geometric Average</i> |                   |
|-----------|---------------------------|-------------------|--------------------------|-------------------|
|           | Stocks - T. Bills         | Stocks - T. Bonds | Stocks - T. Bills        | Stocks - T. Bonds |
| 1928-2024 | 8.44%                     | 7.00%             | 6.63%                    | 5.44%             |
| Std Error | 2.01%                     | 2.12%             |                          |                   |
| 1975-2024 | 9.25%                     | 7.03%             | 8.02%                    | 6.22%             |
| Std Error | 2.30%                     | 2.67%             |                          |                   |
| 2015-2024 | 12.34%                    | 13.54%            | 11.22%                   | 12.71%            |
| Std Error | 5.04%                     | 3.84%             |                          |                   |

# THE PERILS OF TRUSTING THE PAST.....

- ▪ **Noisy estimates:** Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 90 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

$$\text{Standard Error in Premium} = 20\% / \sqrt{90} = 2.1\%$$

- ▪ **Survivorship Bias:** Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

# THE SIMPLEST WAY OF ESTIMATING AN ADDITIONAL COUNTRY RISK PREMIUM: THE COUNTRY DEFAULT SPREAD

- ▪ **Estimate default spread for country:** In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - ▪ The default spread on a dollar denominated bond issued by the country. (In January 2025, that spread was % for the Brazilian \$ bond) was 1.817%.
  - ▪ The sovereign CDS spread for the country. In January 2025, the ten-year CDS spread for Brazil, adjusted for the US CDS, was 3.17%.
  - ▪ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Ba2 and the default spread for a Ba2 rated sovereign was about 2.83% in January 2025.
- ▪ **Add the default spread to a “mature” market premium:** This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 4.33%.
  - ▪ Country Risk Premium for Brazil = 2.83%
  - ▪ Total ERP for Brazil = 4.33% + 2.83% = 7.16%

# AN EQUITY VOLATILITY BASED APPROACH TO ESTIMATING THE COUNTRY TOTAL ERP

- ▪ This approach draws on the **standard deviation of two equity markets**, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ▪ Equity risk premium = Risk Premium<sub>US</sub> × (  $\sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$  )
- ▪ The country equity risk premium is based upon the **volatility of the market in question relative to U.S market**.
  - ▪ Assume that the equity risk premium for the US is 4.33%.
  - ▪ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ▪ Total Equity Risk Premium for Brazil = 4.33% (30%/18%) = 7.22%
  - ▪ Country equity risk premium for Brazil = 7.22% - 4.33% = 2.89%

# A MELDED APPROACH TO ESTIMATING THE ADDITIONAL COUNTRY RISK PREMIUM

- ▪ **Country ratings measure default risk.** While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
- ▪ Another is to **multiply the bond default spread by the relative volatility of stock and bond prices in that market.** Using this approach for Brazil in January 2025, you would get:
  - ▪ Country Equity risk premium = Default spread on country bond\*  
     $\sigma_{\text{Country Equity}} / \sigma_{\text{Country Bond}}$ 
    - ▪ Standard Deviation in Bovespa (Equity) = 30%
    - ▪ Standard Deviation in Brazil government bond = 20%
    - ▪ Default spread for Brazil= 2.83%
  - ▪ Brazil Country Risk Premium =  $2.83\% (30\%/20\%) = 4.25\%$
  - ▪ Brazil Total ERP = Mature Market Premium + CRP =  $4.33\% + 4.25\% = 8.58\%$

# A TEMPLATE FOR ESTIMATING THE ERP

## ERP Estimation Procedure - January 1, 2025

*Step 1: Mature Market Premium*

*Step 2: Assess country risk*

*Step 3: Convert country risk measure into an additional country risk premium for equity*

*Step 4: Estimate an ERP for country*

![](_page_24_Diagram_19.jpeg)

*Blue: Moody's Rating Red: Added Country Risk Green #: Total ERP*

| Andorra     | Baal | 2.03% | 4.46% | Jersey                | Aaz  | 0.66%        | 4.99%        |
|-------------|------|-------|-------|-----------------------|------|--------------|--------------|
| Austria     | Aal  | 2.03% | 4.86% | Lichtenstein          | Aaa  | 0.00%        | 4.33%        |
| Belgium     | Aa3  | 0.80% | 4.36% | Luxembourg            | Aaa  | 0.00%        | 4.33%        |
| Cyprus      | A3   | 1.60% | 5.93% | Malta                 | A2   | 1.13%        | 5.46%        |
| Denmark     | Aa   | 0.00% | 4.33% | Netherlands           | Aaa  | 0.00%        | 4.36%        |
| Finland     | Aal  | 0.53% | 4.86% | Norway                | Aaa  | 0.00%        | 4.33%        |
| France      | Aa3  | 0.80% | 5.13% | Portugal              | A3   | 1.60%        | 5.93%        |
| Germany     | Aa   | 0.00% | 4.33% | Spain                 | Baal | 2.13%        | 4.66%        |
| Greece      | Bal  | 2.34% | 7.67% | Sweden                | Aaa  | 0.00%        | 4.33%        |
| Guernsey    | A1   | 0.94% | 5.27% | Switzerland           | Aaa  | 0.00%        | 4.33%        |
| Iceland     | Aa   | 0.94% | 5.27% | Turkey                | B1   | 0.61%        | 10.34%       |
| Ireland     | Aa3  | 0.80% | 5.13% | United Kingdom        | Aa3  | 0.80%        | 5.13%        |
| Isle of Man | Aa3  | 0.80% | 5.13% | <b>Western Europe</b> |      | <b>1.12%</b> | <b>5.45%</b> |
| Italy       | Baa3 | 2.93% | 7.26% |                       |      |              |              |

| Canada               | <b>Aaa</b>    | <b>0.003%</b> | <b>4.33%</b> |
|----------------------|---------------|---------------|--------------|
| United States        | <b>Aaa</b>    | <b>0.003%</b> | <b>4.33%</b> |
| <b>North America</b> | <b>0.003%</b> | <b>4.33%</b>  |              |

| Caribbean |  | <b>8.10%</b> | <b>12.43%</b> |
|-----------|--|--------------|---------------|
|-----------|--|--------------|---------------|

| Argentina            | Ca   | 16.02%       | 2.03.5%      |
|----------------------|------|--------------|--------------|
| Belize               | Caal | 10.01%       | 1.34.4%      |
| Bolivia              | Caa3 | 13.35%       | 1.76.8%      |
| Brazil               | Ba1  | 3.34%        | 1.67%        |
| Chile                | A2   | 1.13%        | 5.46%        |
| Colombia             | Baa2 | 2.54%        | 6.87%        |
| Costa Rica           | Baa3 | 4.80%        | 7.07%        |
| Ecuador              | Caa3 | 13.35%       | 17.68%       |
| El Salvador          | B3   | 8.67%        | 13.00%       |
| Guatemala            | Ba1  | 3.34%        | 7.67%        |
| Honduras             | B1   | 6.01%        | 10.34%       |
| Mexico               | Baa2 | 2.54%        | 6.87%        |
| Nicaragua            | B2   | 7.34%        | 11.67%       |
| Panama               | Baa3 | 2.93%        | 7.26%        |
| Paraguay             | Baa3 | 2.93%        | 7.26%        |
| Peru                 | Baa1 | 2.13%        | 6.46%        |
| Suriname             | Caal | 10.01%       | 1.34.4%      |
| Uruguay              | Baa1 | 2.13%        | 6.46%        |
| Venezuela            | C    | 23.58%       | 27.91%       |
| <b>Latin America</b> |      | <b>4.82%</b> | <b>9.15%</b> |

Aswath Damodaran

| <i>Country</i> | <i>Rating</i> | <i>CRP</i>   | <i>ERP</i>    |
|----------------|---------------|--------------|---------------|
| Angola         | B3            | 8.67%        | 13.00%        |
| Benin          | B1            | 6.01%        | 13.00%        |
| Botswana       | A3            | 1.60%        | 5.93%         |
| Burkina Faso   | Caa1          | 10.01%       | 14.34%        |
| Cameroon       | Caa1          | 10.01%       | 14.34%        |
| Cape Verde     | B2            | 7.34%        | 11.67%        |
| Congo (DR)     | B3            | 8.67%        | 13.00%        |
| Congo (Rep)    | Caa2          | 11.02%       | 16.35%        |
| Côte d'Ivoire  | Ba2           | 4.02%        | 8.35%         |
| Egypt          | Caa1          | 10.01%       | 14.34%        |
| Ethiopia       | Caa2          | 12.02%       | 16.35%        |
| Gabon          | Caa2          | 12.02%       | 16.35%        |
| Ghana          | Caa2          | 12.02%       | 16.35%        |
| Kenya          | Caa1          | 10.01%       | 14.34%        |
| Mali           | Caa2          | 12.02%       | 16.35%        |
| Mauritius      | Baa3          | 2.93%        | 7.26%         |
| Morocco        | Ba1           | 3.34%        | 7.67%         |
| Mozambique     | Caa2          | 12.02%       | 16.35%        |
| Namibia        | B1            | 6.01%        | 10.34%        |
| Niger          | Caa3          | 13.35%       | 17.68%        |
| Nigeria        | Caa1          | 10.01%       | 14.34%        |
| Rwanda         | B2            | 7.34%        | 11.67%        |
| Senegal        | B1            | 6.01%        | 10.34%        |
| South Africa   | Ba2           | 4.02%        | 8.35%         |
| Swaziland      | B2            | 7.34%        | 11.67%        |
| Tanzania       | B1            | 6.01%        | 10.34%        |
| Togo           | B3            | 8.67%        | 13.00%        |
| Tunisia        | Caa2          | 12.02%       | 16.35%        |
| Uganda         | B3            | 8.67%        | 13.00%        |
| Zambia         | Caa2          | 12.02%       | 16.35%        |
| <b>Africa</b>  |               | <b>8.31%</b> | <b>12.64%</b> |

| Albania                | Ba3  | 4.80%        | 9.13%        |
|------------------------|------|--------------|--------------|
| Armenia                | Ba3  | 4.80%        | 9.13%        |
| Azerbaijan             | Ba1  | 3.34%        | 7.67%        |
| Belarus                | C    | 23.58%       | 27.91%       |
| Bosnia and Herzegovina | Ba3  | 8.67%        | 13.00%       |
| Bulgaria               | Baa1 | 2.13%        | 6.46%        |
| Croatia                | A3   | 1.60%        | 5.93%        |
| Czech Republic         | Aa3  | 0.80%        | 5.13%        |
| Estonia                | A1   | 0.94%        | 5.27%        |
| Georgia                | Ba2  | 4.02%        | 8.35%        |
| Hungary                | Baa2 | 2.54%        | 6.87%        |
| Kazakhstan             | Baa1 | 2.13%        | 6.46%        |
| Kyrgyzstan             | B3   | 8.67%        | 13.00%       |
| Latvia                 | A3   | 1.60%        | 5.93%        |
| Lithuania              | A2   | 1.13%        | 5.46%        |
| Macedonia              | Ba3  | 4.80%        | 9.13%        |
| Moldova                | B3   | 8.67%        | 13.00%       |
| Montenegro             | B1   | 6.01%        | 10.34%       |
| Poland                 | A2   | 1.13%        | 5.46%        |
| Romania                | Baa3 | 2.93%        | 7.26%        |
| Serbia                 | Ba2  | 4.02%        | 8.35%        |
| Slovakia               | A3   | 1.60%        | 5.93%        |
| Slovenia               | A3   | 1.60%        | 5.93%        |
| Tajikistan             | B3   | 8.67%        | 13.00%       |
| Ukraine                | Ca   | 16.02%       | 20.35%       |
| Uzbekistan             | Ba3  | 4.80%        | 9.13%        |
| <b>Eastern Europe</b>  |      | <b>3.40%</b> | <b>7.73%</b> |

| <span> </span> | Abu Dhabi                | Aa2  | C6.66%       | 4.99%        |
|----------------|--------------------------|------|--------------|--------------|
|                | Bahain                   | B2   | 7.34%        | 11.67%       |
|                | Iraq                     | Caa1 | 10.01%       | 14.34%       |
|                | Israel                   | Baa1 | 2.13%        | 6.46%        |
|                | Jordan                   | Ba3  | 4.80%        | 9.13%        |
|                | Kuwait                   | A1   | 0.94%        | 5.27%        |
|                | Lebanon                  | C    | 23.58%       | 27.91%       |
|                | Oman                     | Ba1  | 3.34%        | 7.67%        |
|                | Qatar                    | Aa2  | 0.66%        | 4.99%        |
|                | Ras Al Khaimah (Emirate) | C    | 1.60%        | 5.93%        |
|                | Saudi Arabia             | Aa3  | 0.80%        | 5.13%        |
|                | Sharjah                  | Ba1  | 3.64%        | 7.67%        |
|                | United Arab Emirates     | Aa2  | 0.66%        | 4.99%        |
|                | <b>Middle East</b>       |      | <b>2.10%</b> | <b>6.43%</b> |

| Country         | <i>PRS</i> | <i>CRP</i> | <i>ERP</i> |
|-----------------|------------|------------|------------|
| Algeria         | 69.25      | 3.52%      | 7.85%      |
| Brunei          | 81.75      | 0.70%      | 5.03%      |
| Gambia          | 67.5       | 5.26%      | 9.59%      |
| Guinea          | 57.75      | 10.52%     | 14.85%     |
| Guinea-Bissau   | 63.25      | 7.60%      | 11.93%     |
| Guyana          | 57.75      | 1.87%      | 6.20%      |
| Haiti           | 54.75      | 14.03%     | 18.36%     |
| Iran            | 63.75      | 7.60%      | 11.93%     |
| Korea, D.P.R.   | 51         | 14.03%     | 18.36%     |
| Liberia         | 58.25      | 10.52%     | 14.85%     |
| Libya           | 74.5       | 1.87%      | 6.20%      |
| Madagascar      | 64.5       | 6.43%      | 10.76%     |
| Malawi          | 57.75      | 10.52%     | 14.85%     |
| Myanmar         | 56         | 11.69%     | 16.02%     |
| Russia          | 69.25      | 3.52%      | 7.85%      |
| Sierra Leone    | 59.5       | 10.52%     | 14.85%     |
| Somalia         | 55.5       | 11.69%     | 16.02%     |
| Sudan           | 43.5       | 20.65%     | 24.98%     |
| Syria           | 46.5       | 20.65%     | 24.98%     |
| Yemen, Republic | 51.5       | 14.03%     | 18.36%     |
| Zimbabwe        | 57.75      | 10.52%     | 14.85%     |

| Bangladesh       | B2   | 7,043        | 11,674       |
|------------------|------|--------------|--------------|
| Cambodia         | B2   | 7,344        | 11,673       |
| China            | A1   | 0,94%        | 5,27%        |
| Fiji             | B1   | 6,01%        | 10,34%       |
| Hong Kong        | Aa3  | 0,80%        | 5,13%        |
| India            | Baa3 | 2,93%        | 7,26%        |
| Indonesia        | Baa2 | 2,54%        | 6,87%        |
| Japan            | A1   | 0,94%        | 5,27%        |
| Korea            | Aa2  | 0,66%        | 4,99%        |
| Laos             | Caa3 | 13,35%       | 17,68%       |
| Macao            | Aa3  | 0,80%        | 5,13%        |
| Malaysia         | A3   | 1,60%        | 5,93%        |
| Maldives         | Caa2 | 12,02%       | 11,67%       |
| Mongolia         | B2   | 7,34%        | 11,67%       |
| Nepal            | Ba3  | 4,80%        | 9,13%        |
| Pakistan         | Caa2 | 12,02%       | 11,67%       |
| Papua New Guinea | B2   | 7,34%        | 11,67%       |
| Philippines      | Baa2 | 2,54%        | 6,87%        |
| Singapore        | Aaa  | 0,00%        | 4,33%        |
| Solomon Islands  | Caa1 | 10,01%       | 13,78%       |
| Sri Lanka        | Ca   | 1,60,2%      | 20,35%       |
| Taiwan           | Aa3  | 0,80%        | 5,13%        |
| Thailand         | Baa1 | 2,13%        | 6,46%        |
| Vietnam          | Ba2  | 4,02%        | 8,35%        |
| Asia             |      | <b>1,44%</b> | <b>5,27%</b> |

| <b>Australia</b>          | <b>Australia</b> | <b>Australia</b> | <b>Australia</b> |
|---------------------------|------------------|------------------|------------------|
| Cook Islands              |                  | <b>B1.0%</b>     | <b>1.0%</b>      |
| New Zealand               | <b>Aua</b>       | <b>0.00%</b>     | <b>4.3%</b>      |
| <b>Australia &amp; NZ</b> |                  | <b>0.00%</b>     | <b>4.3%</b>      |

# FROM COUNTRY EQUITY RISK PREMIUMS TO CORPORATE EQUITY RISK PREMIUMS

- ▪ **Approach 1:** Assume that every company in the country is equally exposed to country risk. In this case,
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \text{CRP} + \text{Beta (Mature ERP)}$
- ▪ **Approach 2:** Assume that a company's exposure to country risk is similar to its exposure to other market risk.
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (Mature ERP} + \text{CRP})$
- ▪ **Approach 3:** Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \beta (\text{Mature ERP}) + \lambda (\text{CRP})$
  - ▪  $\text{Mature ERP} = \text{Mature market Equity Risk Premium}$
  - ▪  $\text{CRP} = \text{Additional country risk premium}$

# ESTIMATING COUNTRY RISK PREMIUM EXPOSURE\_ VARIANTS

![](_page_27_Diagram_10.jpeg)

# OPERATION BASED CRP: SINGLE VERSUS MULTIPLE EMERGING MARKETS

- Single emerging market: Embraer, in 2004, reported that it derived 3% of its revenues in Brazil and the balance from mature markets. The mature market ERP in 2004 was 5% and Brazil's CRP was 7.89%.

|                             | Revenues | Total ERP    | CRP          |
|-----------------------------|----------|--------------|--------------|
| US and other mature markets | 97%      | 5.00%        | 0.00%        |
| Brazil                      | 3%       | 12.89%       | 8%           |
| <b>Embraer</b>              |          | <b>5.24%</b> | <b>0.24%</b> |

- Multiple emerging markets: Ambev, the Brazilian-based beverage company, reported revenues from the following countries during 2011.

|              | Revenues   | %      | Total ERP    | CRP          |
|--------------|------------|--------|--------------|--------------|
| Argentina    | 19         | 9.31%  | 15.00%       | 9.00%        |
| Bolivia      | 4          | 1.96%  | 10.88%       | 4.88%        |
| Brazil       | 130        | 63.73% | 8.63%        | 2.63%        |
| Canada       | 23         | 11.27% | 6.00%        | 0.00%        |
| Chile        | 7          | 3.43%  | 7.05%        | 1.05%        |
| Ecuador      | 6          | 2.94%  | 12.75%       | 6.75%        |
| Paraguay     | 3          | 1.47%  | 12.00%       | 6.00%        |
| Peru         | 12         | 5.88%  | 9.00%        | 3.00%        |
| <b>Ambev</b> | <b>204</b> |        | <b>9.11%</b> | <b>3.11%</b> |

# EXTENDING TO A MULTINATIONAL: REGIONAL BREAKDOWN COCA COLA'S REVENUE BREAKDOWN AND ERP IN 2012

| <i>Region</i>           | <i>Revenues</i> | <i>Total ERP</i> | <i>CRP</i> |
|-------------------------|-----------------|------------------|------------|
| Western Europe          | 19%             | 6.67%            | 0.67%      |
| Eastern Europe & Russia | 5%              | 8.60%            | 2.60%      |
| Asia                    | 15%             | 7.63%            | 1.63%      |
| Latin America           | 15%             | 9.42%            | 3.42%      |
| Australia               | 4%              | 6.00%            | 0.00%      |
| Africa                  | 4%              | 9.82%            | 3.82%      |
| North America           | 40%             | 6.00%            | 0.00%      |
| Coca Cola               | 100%            | 7.14%            | 1.14%      |

Things to watch out for

1. 1. Aggregation across regions. For instance, the Pacific region often includes Australia & NZ with Asia
2. 2. Obscure aggregations including Eurasia and Oceania

# TWO PROBLEMS WITH THESE APPROACHES..

- ▪ **Focus just on revenues:** To the extent that revenues are the only variable that you consider, when weighting risk exposure across markets, you may be missing other exposures to country risk. For instance, an emerging market company that gets the bulk of its revenues outside the country (in a developed market) may still have all of its production facilities in the emerging market.
- ▪ **Exposure not adjusted or based upon beta:** To the extent that the country risk premium is multiplied by a beta, we are assuming that beta in addition to measuring exposure to all other macro economic risk also measures exposure to country risk.

# A PRODUCTION-BASED ERP: ROYAL DUTCH SHELL IN 2015

| Country                  | Oil & Gas Production | % of Total     | ERP          |
|--------------------------|----------------------|----------------|--------------|
| Denmark                  | 17396                | 3.83%          | 6.20%        |
| Italy                    | 11179                | 2.46%          | 9.14%        |
| Norway                   | 14337                | 3.16%          | 6.20%        |
| UK                       | 20762                | 4.57%          | 6.81%        |
| Rest of Europe           | 874                  | 0.19%          | 7.40%        |
| Brunei                   | 823                  | 0.18%          | 9.04%        |
| Iraq                     | 20009                | 4.40%          | 11.37%       |
| Malaysia                 | 22980                | 5.06%          | 8.05%        |
| Oman                     | 78404                | 17.26%         | 7.29%        |
| Russia                   | 22016                | 4.85%          | 10.06%       |
| Rest of Asia & ME        | 24480                | 5.39%          | 7.74%        |
| Oceania                  | 7858                 | 1.73%          | 6.20%        |
| Gabon                    | 12472                | 2.75%          | 11.76%       |
| Nigeria                  | 67832                | 14.93%         | 11.76%       |
| Rest of Africa           | 6159                 | 1.36%          | 12.17%       |
| USA                      | 104263               | 22.95%         | 6.20%        |
| Canada                   | 8599                 | 1.89%          | 6.20%        |
| Brazil                   | 13307                | 2.93%          | 9.60%        |
| Rest of Latin America    | 576                  | 0.13%          | 10.78%       |
| <b>Royal Dutch Shell</b> | <b>454326</b>        | <b>100.00%</b> | <b>8.26%</b> |

# ESTIMATE A LAMBDA FOR COUNTRY RISK

- ■ Country risk exposure is affected by **where you get your revenues and where your production happens**, but there are a host of other variables that also affect this exposure, including:
  - ■ Use of risk management products: Companies can use both options/futures markets and insurance to hedge some or a significant portion of country risk.
  - ■ Government “national” interests: There are sectors that are viewed as vital to the national interests, and governments often play a key role in these companies, either officially or unofficially. These sectors are more exposed to country risk.
- ■ It is conceivable that there is a **richer measure of country risk that incorporates all the variables that drive country risk in one measure**. That way my rationale when I devised “lambda” as my measure of country risk exposure.

# A REVENUE-BASED LAMBDA

- ▪ The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:
  - ▪  $\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{average firm}}$
- ▪ Consider two firms – Tata Motors and Tata Consulting Services, both Indian companies. In 2008-09, Tata Motors got about 91.37% of its revenues in India and TCS got 7.62%. The average Indian firm gets about 80% of its revenues in India:
  - ▪  $\lambda_{\text{Tata Motors}} = 91\%/80\% = 1.14$
  - ▪  $\lambda_{\text{TCS}} = 7.62\%/80\% = 0.09$
- ▪ There are two implications
  - ▪ A company's risk exposure is determined by where it does business and not by where it is incorporated.
  - ▪ Firms might be able to actively manage their country risk exposures

# A PRICE/RETURN BASED LAMBDA

$$\text{Return}_{\text{Embraer}} = 0.0195 + 0.2681 \text{ Return}_{\text{C Bond}}$$

$$\text{Return}_{\text{Embratel}} = -0.0308 + 2.0030 \text{ Return}_{\text{C Bond}}$$

![](_page_34_Figure_144.jpeg)

![](_page_34_Figure_145.jpeg)

# ESTIMATING A US DOLLAR COST OF EQUITY FOR EMBRAER - SEPTEMBER 2004

- ▪ Assume that the beta for Embraer is 1.07, and that the US \$ riskfree rate used is 4%. Also assume that the risk premium for the US is 5% and the country risk premium for Brazil is 7.89%. Finally, assume that Embraer gets 3% of its revenues in Brazil & the rest in the US.
- ▪ There are five estimates of \$ cost of equity for Embraer:
  - ▪ **Approach 1:** Constant exposure to CRP, Location CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + 7.89\% = 17.24\%$
  - ▪ **Approach 2:** Constant exposure to CRP, Operation CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + (0.03 * 7.89\% + 0.97 * 0\%) = 9.59\%$
  - ▪ **Approach 3:** Beta exposure to CRP, Location CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\% + 7.89\%) = 17.79\%$
  - ▪ **Approach 4:** Beta exposure to CRP, Operation CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\% + (0.03 * 7.89\% + 0.97 * 0\%)) = 9.60\%$
  - ▪ Approach 5: Lambda exposure to CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + 0.27(7.89\%) = 11.48\%$

# VALUING EMERGING MARKET COMPANIES WITH SIGNIFICANT EXPOSURE IN DEVELOPED MARKETS

- ■ The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk.
- ■ Thus, in 2004, Embraer would have been valued with a cost of equity of 17-18% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
  - ■ Emerging market companies with substantial exposure in developed markets will be significantly over valued by analysts
  - ■ Emerging market companies with substantial exposure in developed markets will be significantly under valued by analysts
- ■ Can you construct an investment strategy to take advantage of the mis-valuation? What would need to happen for you to make money of this strategy?

# IMPLIED EQUITY PREMIUMS

- ▪ **For a start:** If you know the price paid for an asset and have estimates of the expected cash flows on the asset, you can estimate the IRR of these cash flows. If you paid the price, this is your expected return.
- ▪ **Stock Price & Risk:** If you assume that stocks are correctly priced in the aggregate and you can estimate the expected cashflows from buying stocks, you can estimate the expected rate of return on stocks by finding that discount rate that makes the present value equal to the price paid.
- ▪ **Implied ERP:** Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward-looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

# A FORWARD-LOOKING NUMBER

## Implied Equity Risk Premium: Generic Version

Analyst estimates of growth in earnings for the near term, scaling down to a growth rate = riskfree rate, in perpetuity.

Growth rate in perpetuity = Riskfree Rate

Base year Cash flows from owning Equities = Dividends + Buybacks

Cash payout as a percent of earnings, adjusted for changing growth over time.

CFs continue in perpetuity

![](_page_38_Figure_19.jpeg)

Solve for  $r$ 

 $E(\text{Return on Stocks}) = \text{Discount rate that makes the present value of the expected cash flows equal to stock (index) price today}$   
 $ERP = E(\text{Return on Stocks}) - \text{Riskfree Rate}$ 

The implied equity risk premium is a number backed out from what investors are paying for stocks and their expected cash flows from holding stocks. It is an internal rate of return for equity investors, analogous to a yield to maturity for a bondholder.

# EQUITY RISK PREMIUM: JANUARY 2020

![](_page_39_Diagram_21.jpeg)

# AND IN 2020.. COVID EFFECTS

![](_page_40_Figure_10.jpeg)

# AN UPDATED ESTIMATE: ERP IN 2025

![](_page_41_Diagram_20.jpeg)

# IMPLIED PREMIUMS IN THE US: 1960-2023

*Implied Equity Risk Premium for US Equity Market: 1960-2024*

![](_page_42_Figure_11.jpeg)

# IMPLIED PREMIUM VERSUS RISK FREE RATE

![](_page_43_Figure_10.jpeg)

# EQUITY RISK PREMIUMS AND BOND DEFAULT SPREADS

*Equity Risk Premiums and Bond Default Spreads*

![](_page_44_Figure_12.jpeg)

# EQUITY RISK PREMIUMS AND CAP RATES (REAL ESTATE)

![](_page_45_Figure_10.jpeg)

# WHY IMPLIED PREMIUMS MATTER?

- ■ In many investment banks, it is **common practice (especially in corporate finance departments) to use historical risk premiums** (and arithmetic averages at that) as risk premiums to compute cost of equity. Often, the defense they offer is that as long as **everyone uses the same premium, there is no cost to being wrong**.
- ■ If all analysts in a group used the arithmetic average premium (for stocks over T.Bills) for 1928-2024 of 8.44% to value stocks in January 2025, given the implied premium of 4.33%, what are they likely to find?
  - a. The values they obtain will be too low (most stocks will look overvalued)
  - b. The values they obtain will be too high (most stocks will look under valued)
  - c. There should be no systematic bias as long as they use the same premium to value all stocks.

# WHICH EQUITY RISK PREMIUM SHOULD YOU USE?

| If you assume this                                                                 | Premium to use                                 |
|------------------------------------------------------------------------------------|------------------------------------------------|
| Premiums revert back to historical norms and your time period yields these norms   | Historical risk premium                        |
| Market is correct in the aggregate or that your valuation should be market neutral | Current implied equity risk premium            |
| Marker makes mistakes even in the aggregate but is correct over time               | Average implied equity risk premium over time. |

| Predictor                           | Correlation with implied premium next year | Correlation with actual return- next 5 years | Correlation with actual return – next 10 years |
|-------------------------------------|--------------------------------------------|----------------------------------------------|------------------------------------------------|
| <b>Current implied premium</b>      | 0.763                                      | 0.427                                        | 0.500                                          |
| <b>Average implied premium:</b>     | 0.718                                      | 0.326                                        | 0.450                                          |
| <b>Last 5 years</b>                 |                                            |                                              |                                                |
| <b>Historical Premium</b>           | -0.497                                     | -0.437                                       | -0.454                                         |
| <b>Default Spread based premium</b> | 0.047                                      | 0.143                                        | 0.160                                          |

# AN ERP FOR THE SENSEX

- ▪ Inputs for the computation
  - ▪ Sensex on 9/5/07 = 15446
  - ▪ Dividend yield on index = 3.05%
  - ▪ Expected growth rate - next 5 years = 14%
  - ▪ Growth rate beyond year 5 = 6.76% (set equal to riskfree rate)
- ▪ Solving for the expected return:

$$15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$$

- ▪ Expected return on stocks = 11.18%
- ▪ Implied equity risk premium for India = 11.18% - 6.76% = 4.42%

# THE EVOLUTION OF EMERGING MARKET RISK

| Start of year | PBV (Developed) | PBV (Emerging) | ROE (Developed) | ROE (Emerging) | US T.Bond Rate | Growth Rate (Developed) | Growth Rate (Emerging) | Cost of Equity (Developed) | Cost of Equity (Emerging) | Differential |
|---------------|-----------------|----------------|-----------------|----------------|----------------|-------------------------|------------------------|----------------------------|---------------------------|--------------|
| 2004          | 2.00            | 1.19           | 10.81%          | 11.65%         | 4.25%          | 3.75%                   | 4.75%                  | 7.28%                      | 10.55%                    | 3.27%        |
| 2005          | 2.09            | 1.27           | 11.12%          | 11.93%         | 4.22%          | 3.72%                   | 4.72%                  | 7.26%                      | 10.40%                    | 3.14%        |
| 2006          | 2.03            | 1.44           | 11.32%          | 12.18%         | 4.39%          | 3.89%                   | 4.89%                  | 7.55%                      | 9.95%                     | 2.40%        |
| 2007          | 1.67            | 1.67           | 10.87%          | 12.88%         | 4.70%          | 4.20%                   | 5.20%                  | 8.19%                      | 9.80%                     | 1.60%        |
| 2008          | 0.87            | 0.83           | 9.42%           | 11.12%         | 4.02%          | 3.52%                   | 4.52%                  | 10.30%                     | 12.47%                    | 2.17%        |
| 2009          | 1.20            | 1.34           | 8.48%           | 11.02%         | 2.21%          | 1.71%                   | 2.71%                  | 7.35%                      | 8.91%                     | 1.56%        |
| 2010          | 1.39            | 1.43           | 9.14%           | 11.22%         | 3.84%          | 3.34%                   | 4.34%                  | 7.51%                      | 9.15%                     | 1.64%        |
| 2011          | 1.12            | 1.08           | 9.21%           | 10.04%         | 3.29%          | 2.79%                   | 3.79%                  | 8.52%                      | 9.58%                     | 1.05%        |
| 2012          | 1.17            | 1.18           | 9.10%           | 9.33%          | 1.88%          | 1.38%                   | 2.38%                  | 7.98%                      | 8.27%                     | 0.29%        |
| 2013          | 1.56            | 1.63           | 8.67%           | 10.48%         | 1.76%          | 1.26%                   | 2.26%                  | 6.01%                      | 7.30%                     | 1.29%        |
| 2014          | 1.95            | 1.50           | 9.27%           | 9.64%          | 3.04%          | 2.54%                   | 3.54%                  | 5.99%                      | 7.61%                     | 1.62%        |
| 2015          | 1.88            | 1.56           | 9.69%           | 9.75%          | 2.17%          | 1.67%                   | 2.67%                  | 5.94%                      | 7.21%                     | 1.27%        |
| 2016          | 1.99            | 1.59           | 9.24%           | 10.16%         | 2.27%          | 1.77%                   | 2.77%                  | 5.52%                      | 7.42%                     | 1.89%        |
| 2017          | 1.76            | 1.48           | 8.71%           | 9.53%          | 2.68%          | 2.18%                   | 3.18%                  | 5.89%                      | 7.47%                     | 1.58%        |
| 2018          | 1.98            | 1.66           | 11.23%          | 11.36%         | 2.68%          | 2.18%                   | 3.18%                  | 6.75%                      | 8.11%                     | 1.36%        |
| 2019          | 1.64            | 1.31           | 12.09%          | 11.35%         | 2.68%          | 2.18%                   | 3.18%                  | 8.22%                      | 9.42%                     | 1.19%        |
| 2020          | 2.26            | 1.64           | 10.41%          | 9.10%          | 1.92%          | 1.42%                   | 2.42%                  | 5.40%                      | 6.49%                     | 1.10%        |
| 2021          | 2.21            | 1.77           | 6.30%           | 7.31%          | 0.93%          | 0.43%                   | 1.43%                  | 3.09%                      | 4.75%                     | 1.67%        |
| 2022          | 2.31            | 1.67           | 13.22%          | 11.99%         | 1.51%          | 1.01%                   | 2.01%                  | 6.30%                      | 7.99%                     | 1.69%        |
| 2023          | 2.28            | 1.44           | 12.90%          | 10.93%         | 3.88%          | 3.38%                   | 4.38%                  | 7.56%                      | 8.93%                     | 1.37%        |