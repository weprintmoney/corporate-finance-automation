---
title: "Hurdlerate"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/hurdlerate.pdf
---

# **FROM RISK MODELS TO HURDLE RATES: ESTIMATION CHALLENGES**

*"The price of purity is  
purists..."*

# INPUTS REQUIRED TO USE THE CAPM -

- ▪ The capital asset pricing model yields the following expected return:
  - ▪  $\text{Expected Return} = \text{Riskfree Rate} + \text{Beta} * (\text{Expected Return on the Market Portfolio} - \text{Riskfree Rate})$
- ▪ To use the model, we need three inputs:
  - ▪ The **current risk-free rate**
  - ▪ The **expected equity risk premium**, the premium expected for investing in risky assets, i.e. the market portfolio, over the riskless asset.
  - ▪ The **beta of the asset** being analyzed.

# THE RISKFREE RATE AND TIME HORIZON

- ▪ On a riskfree asset, **the actual return is always equal to the expected return**. Therefore, there is no variance around the expected return.
- ▪ For an investment to be riskfree, i.e., to have an actual return be equal to the expected return, two conditions have to be met –
  - ▪ There **can be no default risk**, which generally implies that the security has to be issued by the government. Note, however, that not all governments can be viewed as default free.
  - ▪ There **can be no uncertainty about reinvestment rates**, which implies that it is a zero-coupon security with the same maturity as the cash flow being analyzed.

# RISKFREE RATE IN PRACTICE

- ▪ **Definition:** The riskfree rate is the **rate on a zero coupon default-free bond** matching the time horizon of the cash flow being analyzed.
- ▪ **Implication:** Theoretically, this translates into **using different riskfree rates for each cash flow** - the 1 year zero coupon rate for the cash flow in year 1, the 2-year zero coupon rate for the cash flow in year 2 ...
- ▪ **A Practical Solution:** Practically speaking, if there is substantial uncertainty about expected cash flows, the present value effect of using time varying riskfree rates is small enough that it may not be worth it.
- ▪ **In corporate finance, almost everything we do is long term.** So, using a **long-term default free rate as the riskfree rate makes sense.**

# THE BOTTOM LINE ON RISKFREE RATES

- ▪ **Currency Matching:** The riskfree rate that you use in an analysis should be in the same currency that your cashflows are estimated in.
  - ▪ In other words, if your cashflows are in U.S. dollars, your riskfree rate has to be in U.S. dollars as well.
  - ▪ If your cash flows are in Euros, your riskfree rate should be a Euro riskfree rate.
- ▪ **Just use the government bond rate?** The conventional practice of estimating riskfree rates is to use the government bond rate, with the government being the one that is in control of issuing that currency.
- ▪ **If the government is default-free**, using a long term government rate (even on a coupon bond) as the risk free rate on all of the cash flows in a long term analysis will yield a close approximation of the true value. With US dollars in November 2013, for instance, the ten-year treasury bond rate of 2.75% was used as the riskfree rate.

# WHAT IS THE EURO RISKFREE RATE? AN EXERCISE IN NOVEMBER 2013

Rate on 10-year Euro Government Bonds: November 2013

![](_page_5_Figure_89.jpeg)

# WHEN THE GOVERNMENT IS DEFAULT FREE: RISK FREE RATES – IN NOVEMBER 2013

![](_page_6_Figure_7.jpeg)

# WHAT IF THERE IS NO DEFAULT-FREE ENTITY? RISK FREE RATES IN NOVEMBER 2013

- ▪ **Adjust the local currency government borrowing rate for default risk** to get a riskless local currency rate.
  - ▪ In November 2013, the Indian government rupee bond rate was 8.82%. the local currency rating from Moody's was Baa3 and the default spread for a Baa3 rated country bond was 2.25%.

$$\text{Riskfree rate in Rupees} = 8.82\% - 2.25\% = 6.57\%$$

- ▪ In November 2013, the Chinese Renmimbi government bond rate was 4.30% and the local currency rating was Aa3, with a default spread of 0.8%.

$$\text{Riskfree rate in Chinese Renmimbi} = 4.30\% - 0.80\% = 3.50\%$$

- ▪ **Do the analysis in an alternate currency**, where getting the riskfree rate is easier. With Vale in 2013, we could choose to do the analysis in US dollars (rather than estimate a riskfree rate in R\$). The riskfree rate is then the US treasury bond rate.
- ▪ **Do your analysis in real terms**, in which case the riskfree rate has to be a real riskfree rate. The inflation-indexed treasury rate is a measure of a real riskfree rate.

# THREE PATHS TO ESTIMATING SOVEREIGN DEFAULT SPREADS

- ▪ **Sovereign dollar or euro denominated bonds:** The difference between the interest rate on a sovereign US \$ bond, issued by the country, and the US treasury bond rate can be used as the default spread. For example, in November 2013, the 10-year Brazil US \$ bond, denominated in US dollars had a yield of 4.25% and the US 10-year T.Bond rate traded at 2.75%.

$$\text{Default spread} = 4.25\% - 2.75\% = 1.50\%$$

- ▪ **Sovereign CDS spreads:** Obtain the default spreads for sovereigns in the CDS market. The CDS spread for Brazil in November 2013 was 2.50%.
- ▪ **Ratings-based spread:** If you know the sovereign rating for a country, you can estimate the default spread based on the rating. In November 2013, Brazil's rating was Baa2, yielding a default spread of 2%.

# RISK FREE RATES IN CURRENCIES: SOVEREIGNS WITH DEFAULT RISK IN NOVEMBER 2013

Figure 4.2: Risk free rates in Currencies where Governments not Aaa rated

![](_page_9_Figure_6.jpeg)

# RISK FREE RATES IN JANUARY 2025

Government-bond Based Riskfree Rates in January 2025

![](_page_10_Figure_8.jpeg)

# MEASUREMENT OF THE EQUITY RISK PREMIUM

- ▪ The equity risk premium is **the premium that investors demand for investing in an average risk equity**, relative to the riskfree rate. In short, it is the price of risk in equity markets, rising with fear.
- ▪ As a general proposition, this premium should be
  - ▪ Greater than zero
  - ▪ Increase with the **risk aversion** of the investors in that market
  - ▪ Increase with the **riskiness of the “average” risk investment**
- ▪ If so, it also follows that equity risk **premiums should change over time**, as economic circumstances change and investor composition also changes.

# WHAT IS YOUR RISK PREMIUM?

- ▪ Assume that stocks are the only risky assets and that you are offered two investment options:
  - ▪ a **riskless investment** (say a Government Security), on which you can make 3%
  - ▪ **An index fund of all stocks**, on which the returns are uncertain
- ▪ How much of an expected return would you demand to shift your money from the riskless asset to the mutual fund?
  - a. Less than 3%
  - b. Between 3% - 5%
  - c. Between 5% - 7%
  - d. Between 7% - 9%
  - e. Between 9% - 11%
  - f. More than 11%

# RISK AVERSION AND RISK PREMIUMS

- ▪ If this were the entire market, the risk premium would be a **weighted average of the risk premiums demanded** by each and every investor.
- ▪ The weights will be determined by the **wealth that each investor brings to the market**. Thus, Warren Buffett's risk aversion counts more towards determining the “equilibrium” premium than yours’ and mine.
- ▪ As investors become more risk averse, or the market becomes “more risky”, you would expect the “equilibrium” premium to increase.

# RISK PREMIUMS DO CHANGE..

- ■ Go back to the previous question. Assume now that you are making the same choice but that you are making it in the aftermath of a stock market crash (it has dropped 25% in the last month). Would you change your answer?
  - a. I would demand a larger premium
  - b. I would demand a smaller premium
  - c. I would demand the same premium
- ■ If your equity risk premium rises, what should happen to stock prices, all else held constant?

# ESTIMATING RISK PREMIUMS IN PRACTICE

- ▪ **Survey Premiums:** Survey investors on their desired risk premiums and use the average premium from these surveys.
- ▪ **Historical Premiums:** Assume that the actual premium delivered over long time periods is equal to the expected premium - i.e., use historical data.
- ▪ **Implied Premiums:** Estimate a forward-looking premium, based upon today's asset prices.

# 1. THE SURVEY APPROACH

- ▪ Surveying all investors in a marketplace is impractical.
- ▪ However, you can survey a few individuals and use these results. In practice, this translates into surveys of the following:

| <i>Group Surveyed</i>   | <i>Survey done by</i>             | <i>Estimated ERP</i> | <i>Notes</i>                |
|-------------------------|-----------------------------------|----------------------|-----------------------------|
| Individual Investors    | Securities Industries Association | 8.3% (2004)          | One year premium            |
| Institutional Investors | Merrill Lynch                     | 4.8% (2013)          | Monthly updates             |
| CFOs                    | Campbell Harvey & Graham          | 4.48% (2012)         | 5-8% response rate          |
| Analysts                | Pablo Fernandez                   | 5.0% (2011)          | Lowest standard deviation   |
| Academics               | Pablo Fernandez                   | 5.7% (2011)          | Higher for emerging markets |

- ▪ The limitations of this approach are:
  - ▪ There are **no constraints on reasonability** (the survey could produce negative risk premiums or risk premiums of 50%)
  - ▪ The survey results are **more reflective of the past than the future**.
  - ▪ They **tend to be short term**; even the longest surveys do not go beyond one year.

## 2. THE HISTORICAL PREMIUM APPROACH

- ▪ This is the default approach used by most to arrive at the premium to use in the model
- ▪ In most cases, this approach does the following
  - ▪ Defines a **time period** for the estimation (1928-Present, last 50 years...)
  - ▪ Calculates **average returns on a stock index** during the period
  - ▪ Calculates **average returns on a riskless security** over the period
  - ▪ Calculates the difference between the two averages and uses it as a premium looking forward.
- ▪ The limitations of this approach are:
  - ▪ it assumes that the risk aversion of investors **has not changed in a systematic way across time**. (The risk aversion may change from year to year, but it reverts back to historical averages)
  - ▪ it assumes that **the riskiness of the “risky” portfolio (stock index) has not changed** in a systematic way across time.

# HISTORICAL ERP: A HISTORICAL SNAPSHOT

|           |  | <i>Arithmetic Average</i> |                   | <i>Geometric Average</i> |                   |
|-----------|--|---------------------------|-------------------|--------------------------|-------------------|
|           |  | Stocks - T. Bills         | Stocks - T. Bonds | Stocks - T. Bills        | Stocks - T. Bonds |
| 1928-2024 |  | 8.44%                     | 7.00%             | 6.63%                    | 5.44%             |
| Std Error |  | 2.01%                     | 2.12%             |                          |                   |
| 1975-2024 |  | 9.25%                     | 7.03%             | 8.02%                    | 6.22%             |
| Std Error |  | 2.30%                     | 2.67%             |                          |                   |
| 2015-2024 |  | 12.34%                    | 13.54%            | 11.22%                   | 12.71%            |
| Std Error |  | 5.04%                     | 3.84%             |                          |                   |

Historical premium for the US

- ▪ If you are going to use a historical risk premium, make it
  - ▪ Long term (because of the standard error)
  - ▪ Consistent with your choice of risk free rate
  - ▪ A “compounded” average
- ▪ No matter which estimate you use, recognize that it is backward looking, is noisy and may reflect selection bias.

### 3. A FORWARD-LOOKING ERP

- ▪ If you know **the price paid for an asset and have estimates of the expected cash flows on the asset**, you can estimate the **IRR** of these cash flows. If you paid the price, this is your expected return.
  - ▪ In the **bond market**, that is exactly what we do when we compute the yield to maturity on a bond.
  - ▪ If you assume that **stocks are correctly priced in the aggregate and you can estimate the expected cashflows from buying stocks**, **you can estimate the expected rate of return on stocks** by finding that discount rate that makes the present value equal to the price paid.
- ▪ Subtracting out the riskfree rate should yield **an implied equity risk premium**. This implied equity premium is a forward-looking number and can be updated as often as you want.

# IMPLIED ERP IN NOVEMBER 2013: WATCH WHAT I PAY, NOT WHAT I SAY.

- If you can observe what investors are willing to pay for stocks, you can back out an expected return from that price and an implied equity risk premium.

![](_page_20_Figure_189.jpeg)

# THE BOTTOM LINE ON EQUITY RISK PREMIUMS IN NOVEMBER 2013

- ■ **Mature Markets:** In November 2013, the number that we chose to use as the equity risk premium for all mature markets was 5.5%. This was set equal to the implied premium at that point in time and it was much higher than the historical risk premium of 4.20% prevailing then.

|           | Arithmetic Average |                   | Geometric Average |                   |
|-----------|--------------------|-------------------|-------------------|-------------------|
|           | Stocks - T. Bills  | Stocks - T. Bonds | Stocks - T. Bills | Stocks - T. Bonds |
| 1928-2012 | 7.65%              | 5.88%             | 5.74%             | 4.20%             |
|           | 2.20%              | 2.33%             |                   |                   |
| 1962-2012 | 5.93%              | 3.91%             | 4.60%             | 2.93%             |
|           | 2.38%              | 2.66%             |                   |                   |
| 2002-2012 | 7.06%              | 3.08%             | 5.38%             | 1.71%             |
|           | 5.82%              | 8.11%             |                   |                   |

- ■ **For emerging markets**, we will use the melded default spread approach (where default spreads are scaled up to reflect additional equity risk) to come up with the additional risk premium that we will add to the mature market premium. Thus, markets in countries with lower sovereign ratings will have higher risk premiums than 5.5%.

- - ■ Emerging Market ERP = 5.5% + Country Default Spread\*  $\left( \frac{\sigma_{\text{Equity}}}{\sigma_{\text{Country Bond}}} \right)$

# WHAT ABOUT EQUITY RISK PREMIUMS FOR OTHER MARKETS?

- ▪ Historical data for markets outside the United States is available **for much shorter time periods**. The problem is even greater in emerging markets.
- ▪ The historical premiums that emerge from this data reflects this data problem and there is **much greater error associated with the estimates of the premiums**.
- ▪ You could **try to compute implied equity risk premiums** but getting the inputs, especially for long term growth are difficult to do.

# ONE SOLUTION: BOND DEFAULT SPREADS AS CRP — NOVEMBER 2013

- ■ In November 2013, the equity risk premium for the US was 5.50% Using the default spread on the sovereign bond or based upon the sovereign rating and adding that spread to the mature market premium (4.20% for the US) gives you a total ERP for a country.

| Country | Rating | Default Spread (Country Risk Premium) | US ERP | Total ERP for country |
|---------|--------|---------------------------------------|--------|-----------------------|
| India   | Baa3   | 2.25%                                 | 5.50%  | 7.75%                 |
| China   | Aa3    | 0.80%                                 | 5.50%  | 6.30%                 |
| Brazil  | Baa2   | 2.00%                                 | 5.50%  | 7.50%                 |

- ■ If you prefer CDS spreads:

| Country | Sovereign CDS Spread | US ERP | Total ERP for country |
|---------|----------------------|--------|-----------------------|
| India   | 4.20%                | 5.50%  | 9.70%                 |
| China   | 1.20%                | 5.50%  | 6.70%                 |
| Brazil  | 2.59%                | 5.50%  | 8.09%                 |

# BEYOND THE DEFAULT SPREAD? EQUITIES ARE RISKIER THAN BONDS

- ■ While default risk spreads and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads. One approach to scaling up the premium is to look at the relative volatility of equities to bonds and to scale up the default spread to reflect this:

$$\text{Country Risk Premium} = \text{Country Default Spread} * \left( \frac{\sigma_{\text{Equity}}}{\sigma_{\text{Country Bond}}} \right)$$

- ■ Brazil: The annualized standard deviation in the Brazilian equity index over the previous year is 21 percent, whereas the annualized standard deviation in the Brazilian C-bond is 14 percent.
  - ■ Brazil's Equity Risk Premium =  $5.50\% + 2.00\% (21\%/14\%) = 8.50\%$
- ■ Using the same approach for China and India:
  - ■ China's Equity Risk Premium =  $5.50\% + 0.80\% (18\%/10\%) = 6.94\%$
  - ■ India's Equity Risk Premium =  $5.50\% + 2.25\% (24\%/17\%) = 9.10\%$

# A TEMPLATE FOR ESTIMATING THE ERP

## ERP Estimation Procedure - January 1, 2025

*Step 1: Mature Market Premium*

*Step 2: Assess country risk*

*Step 3: Convert country risk measure into an additional country risk premium for equity*

*Step 4: Estimate an ERP for country*

![](_page_25_Diagram_19.jpeg)

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

# ESTIMATING ERP FOR DISNEY: NOVEMBER 2013

- ■ **Incorporation:** The conventional practice on equity risk premiums is to estimate an ERP based upon where a company is incorporated. Thus, the cost of equity for Disney would be computed based on the US equity risk premium, because it is a US company, and the Brazilian ERP would be used for Vale, because it is a Brazilian company.
- ■ **Operations:** The more sensible practice on equity risk premium is to estimate an ERP based upon where a company operates. For Disney in 2013:

| <i>Region/ Country</i> | <i>Proportion of Disney's Revenues</i> | <i>ERP</i>   |
|------------------------|----------------------------------------|--------------|
| US& Canada             | 82.01%                                 | 5.50%        |
| Europe                 | 11.64%                                 | 6.72%        |
| Asia-Pacific           | 6.02%                                  | 7.27%        |
| Latin America          | 0.33%                                  | 9.44%        |
| <b>Disney</b>          | <b>100.00%</b>                         | <b>5.76%</b> |

# ERP FOR COMPANIES: NOVEMBER 2013

In November 2013,  
the mature market  
premium used was  
5.5%

| <i>Company</i>  | <i>Region/ Country</i> | <i>Weight</i> | <i>ERP</i> |
|-----------------|------------------------|---------------|------------|
| Bookscape       | United States          | 100%          | 5.50%      |
| Vale            | US & Canada            | 4.90%         | 5.50%      |
|                 | Brazil                 | 16.90%        | 8.50%      |
|                 | Rest of Latin America  | 1.70%         | 10.09%     |
|                 | China                  | 37.00%        | 6.94%      |
|                 | Japan                  | 10.30%        | 6.70%      |
|                 | Rest of Asia           | 8.50%         | 8.61%      |
|                 | Europe                 | 17.20%        | 6.72%      |
|                 | Rest of World          | 3.50%         | 10.06%     |
|                 | Company                | 100.00%       | 7.38%      |
|                 | Tata Motors            | India         | 23.90%     |
| China           |                        | 23.60%        | 6.94%      |
| UK              |                        | 11.90%        | 5.95%      |
| United States   |                        | 10.00%        | 5.50%      |
| Mainland Europe |                        | 11.70%        | 6.85%      |
| Rest of World   |                        | 18.90%        | 6.98%      |
| Company         |                        | 100.00%       | 7.19%      |
| Baidu           | China                  | 100%          | 6.94%      |
| Deutsche Bank   | Germany                | 35.93%        | 5.50%      |
|                 | North America          | 24.72%        | 5.50%      |
|                 | Rest of Europe         | 28.67%        | 7.02%      |
|                 | Asia-Pacific           | 10.68%        | 7.27%      |
|                 | South America          | 0.00%         | 9.44%      |
|                 | Company                | 100.00%       | 6.12%      |

# THE ANATOMY OF A CRISIS: IMPLIED ERP FROM SEPTEMBER 12, 2008 TO JANUARY 1, 2009

Implied Equity Risk Premium - 9/12- 12/31/08

![](_page_29_Figure_8.jpeg)

# AND IN 2020.. COVID EFFECTS

![](_page_30_Figure_6.jpeg)

# AN UPDATED IMPLIED ERP

![](_page_31_Diagram_25.jpeg)

# IMPLIED PREMIUMS IN THE US: 1960-2023

*Implied Equity Risk Premium for US Equity Market: 1960-2024*

![](_page_32_Figure_8.jpeg)

# A TEMPLATE FOR ESTIMATING THE ERP

## ERP Estimation Procedure - January 1, 2025

*Step 1: Mature Market Premium*

*Step 2: Assess country risk*

*Step 3: Convert country risk measure into an additional country risk premium for equity*

*Step 4: Estimate an ERP for country*

![](_page_33_Diagram_15.jpeg)

*Blue: Moody's Rating Red: Added Country Risk Green #: Total ERP*

| Andorra     | Baal | 1.87% | 6.20% | Jersey                | Aaz  | 0.58%        | 4.91%        |
|-------------|------|-------|-------|-----------------------|------|--------------|--------------|
| Austria     | Aal  | 0.47% | 4.80% | Liechtenstein         | Aaa  | 0.00%        | 4.33%        |
| Belgium     | Aa3  | 1.07% | 5.03% | Luxembourg            | Aaa  | 0.00%        | 4.37%        |
| Cyprus      | A3   | 1.40% | 5.73% | Malta                 | A2   | 0.99%        | 5.32%        |
| Denmark     | Aaa  | 0.00% | 4.33% | Netherlands           | Aaa  | 0.00%        | 4.33%        |
| Finland     | Aal  | 0.47% | 4.80% | Norway                | Aaa  | 0.00%        | 4.33%        |
| France      | Aa3  | 0.70% | 5.03% | Portugal              | A3   | 1.40%        | 5.37%        |
| Germany     | Aaa  | 0.00% | 4.33% | Spain                 | Baal | 1.87%        | 6.20%        |
| Greece      | Bal  | 2.93% | 7.26% | Sweden                | Aaa  | 0.00%        | 4.33%        |
| Guernsey    | A1   | 0.82% | 5.15% | Switzerland           | Aaa  | 0.00%        | 4.37%        |
| Iceland     | A1   | 0.82% | 5.15% | Turkey                | B1   | 5.26%        | 5.39%        |
| Ireland     | Aa3  | 0.70% | 5.03% | United Kingdom        | Aa3  | 0.70%        | 5.30%        |
| Isle of Man | Aa3  | 0.70% | 5.03% | <b>Western Europe</b> |      | <b>0.98%</b> | <b>5.31%</b> |
| Italy       | Baa3 | 2.57% | 6.90% |                       |      |              |              |

| Canada               | Aaa        | 0.003%        | 4.33%        |
|----------------------|------------|---------------|--------------|
| United States        | Aaa        | 0.003%        | 4.33%        |
| <b>North America</b> | <b>Aaa</b> | <b>0.003%</b> | <b>4.33%</b> |

| Caribbean | 7.09% | 11.42% |
|-----------|-------|--------|
|-----------|-------|--------|

| Argentina            | Ca   | <b>14.03%</b> | <b>18.36%</b> |
|----------------------|------|---------------|---------------|
| Belize               | Caal | <b>8.76%</b>  | <b>13.09%</b> |
| Bolivia              | Caa3 | <b>11.69%</b> | <b>16.02%</b> |
| Brazil               | Bal  | <b>2.93%</b>  | <b>7.26%</b>  |
| Chile                | A2   | <b>0.99%</b>  | <b>5.32%</b>  |
| Colombia             | Baa2 | <b>2.23%</b>  | <b>6.56%</b>  |
| Costa Rica           | Ba3  | <b>4.20%</b>  | <b>8.53%</b>  |
| Ecuador              | Caa3 | <b>11.69%</b> | <b>16.02%</b> |
| El Salvador          | B3   | <b>7.60%</b>  | <b>11.93%</b> |
| Guatemala            | Bal  | <b>2.93%</b>  | <b>7.26%</b>  |
| Honduras             | B1   | <b>5.26%</b>  | <b>9.59%</b>  |
| Mexico               | Baa2 | <b>2.23%</b>  | <b>6.56%</b>  |
| Nicaragua            | B2   | <b>6.43%</b>  | <b>10.76%</b> |
| Panama               | Baa3 | <b>2.57%</b>  | <b>6.90%</b>  |
| Paraguay             | Baa3 | <b>2.57%</b>  | <b>6.90%</b>  |
| Peru                 | Baal | <b>1.87%</b>  | <b>6.20%</b>  |
| Suriname             | Caal | <b>8.76%</b>  | <b>13.09%</b> |
| Uruguay              | Baal | <b>1.87%</b>  | <b>6.20%</b>  |
| Venezuela            | C    | <b>20.65%</b> | <b>24.98%</b> |
| <b>Latin America</b> |      | <b>4.22%</b>  | <b>8.55%</b>  |

Aswath Damodaran

| Albania                | Ba3   | 4.20%  | 8.53%  |
|------------------------|-------|--------|--------|
| Armenia                | Ba3   | 4.20%  | 8.53%  |
| Azerbaijan             | Ba1   | 2.93%  | 2.06%  |
| Belarus                | C     | 4.06%  | 24.98% |
| Bosnia and Herzegovina | B3    | 7.60%  | 11.19% |
| Bulgaria               | Baa1  | 1.87%  | 6.20%  |
| Croatia                | A3    | 1.40%  | 5.73%  |
| Czech Republic         | Aa3   | 0.70%  | 5.03%  |
| Estonia                | A1    | 0.82%  | 5.15%  |
| Georgia                | Ba2   | 3.52%  | 7.85%  |
| Hungary                | Baa2  | 2.23%  | 6.56%  |
| Kazakhstan             | Baa1  | 1.87%  | 6.20%  |
| Kyrgyzstan             | B3    | 7.60%  | 11.19% |
| Latvia                 | A3    | 1.40%  | 5.73%  |
| Lithuania              | A2    | 0.99%  | 5.32%  |
| Macedonia              | Ba3   | 4.20%  | 8.53%  |
| Moldova                | B3    | 7.60%  | 11.19% |
| Montenegro             | B1    | 5.26%  | 9.59%  |
| Poland                 | A2    | 0.99%  | 5.32%  |
| Romania                | Baa3  | 2.57%  | 6.90%  |
| Serbia                 | Ba2   | 3.52%  | 7.85%  |
| Slovakia               | A3    | 1.40%  | 5.73%  |
| Slovenia               | A3    | 1.40%  | 5.73%  |
| Tajikistan             | B3    | 7.60%  | 11.19% |
| Ukraine                | Ca    | 14.03% | 18.36% |
| Uzbekistan             | Ba3   | 8.53%  | 8.53%  |
| Eastern Europe         | 2.98% | 7.31%  | 7.31%  |

| Abu Dhabi                   | Aa2  | 0.08%        | 4.91%        |
|-----------------------------|------|--------------|--------------|
| Bahrain                     | B2   | 6.43%        | 10.76%       |
| Iraq                        | Caa1 | 2.86%        | 13.09%       |
| Israel                      | Baa1 | 1.87%        | 6.20%        |
| Jordan                      | Ba3  | 4.20%        | 8.53%        |
| Kuwait                      | A1   | 0.80%        | 5.15%        |
| Lebanon                     | C    | 20.65%       | 24.98%       |
| Oman                        | Ba1  | 2.93%        | 7.26%        |
| Qatar                       | Aa2  | 0.58%        | 4.91%        |
| Ras Al Khaimah (Emirate of) | A3   | 1.08%        | 5.73%        |
| Saudi Arabia                | Aa3  | 0.70%        | 5.03%        |
| Sharjah                     | Ba1  | 2.93%        | 7.26%        |
| United Arab Emirates        | Aa2  | 0.58%        | 4.91%        |
| <b>Middle East</b>          |      | <b>1.84%</b> | <b>6.17%</b> |

| Country         | PPS   | CPP    | EPP    |
|-----------------|-------|--------|--------|
| Algeria         | 69.25 | 3.52%  | 7.85%  |
| Brunei          | 81.75 | 0.70%  | 5.03%  |
| Gambia          | 67.5  | 5.26%  | 9.59%  |
| Guinea          | 57.75 | 10.52% | 14.85% |
| Guinea-Bissau   | 63.25 | 7.60%  | 11.93% |
| Guyana          | 75.75 | 1.87%  | 6.20%  |
| Haiti           | 54.75 | 14.03% | 18.36% |
| Iran            | 63.75 | 7.60%  | 11.93% |
| Korea, D.P.R.   | 51    | 14.03% | 18.36% |
| Liberia         | 58.25 | 10.52% | 14.85% |
| Libya           | 74.5  | 1.87%  | 6.20%  |
| Madagascar      | 64.5  | 6.43%  | 10.76% |
| Malawi          | 57.75 | 10.52% | 14.85% |
| Myanmar         | 56    | 11.69% | 16.02% |
| Russia          | 69.25 | 3.52%  | 7.85%  |
| Sierra Leone    | 59.5  | 10.52% | 14.85% |
| Somalia         | 55.5  | 11.69% | 16.02% |
| Sudan           | 43.5  | 20.65% | 24.98% |
| Syria           | 46.5  | 20.65% | 24.98% |
| Yemen, Republic | 51.5  | 14.03% | 18.36% |
| Zimbabwe        | 57.75 | 10.52% | 14.85% |

| Bangladesh       | B2   | 6.43%        | 10.76%       |
|------------------|------|--------------|--------------|
| Cambodia         | B2   | 6.43%        | 10.76%       |
| China            | A1   | 8.22%        | 5.15%        |
| Fiji             | B1   | 5.26%        | 9.59%        |
| Hong Kong        | Aa3  | 6.07%        | 5.03%        |
| India            | Baa3 | 2.57%        | 6.90%        |
| Indonesia        | Baa2 | 2.23%        | 6.56%        |
| Japan            | A1   | 8.22%        | 5.15%        |
| Korea            | Aa2  | 5.08%        | 4.91%        |
| Laos             | Caa3 | 1.69%        | 16.02%       |
| Macao            | Aa3  | 0.70%        | 5.03%        |
| Malaysia         | A3   | 1.40%        | 5.73%        |
| Maldives         | Caa2 | 1.02%        | 14.85%       |
| Mongolia         | B2   | 6.43%        | 10.76%       |
| Nepal            | Ba3  | 4.20%        | 8.53%        |
| Pakistan         | Caa2 | 1.02%        | 14.85%       |
| Papua New Guinea | B2   | 6.43%        | 10.76%       |
| Philippines      | Baa2 | 2.23%        | 6.56%        |
| Singapore        | Aaa  | 0.00%        | 4.33%        |
| Solomon Islands  | Caa1 | 8.76%        | 13.09%       |
| Sri Lanka        | Ca   | 1.40%        | 18.36%       |
| Taiwan           | Aa3  | 5.03%        | 8.03%        |
| Thailand         | Baa1 | 1.87%        | 6.20%        |
| Vietnam          | Ba2  | 3.52%        | 7.85%        |
| <b>Asia</b>      |      | <b>1.26%</b> | <b>5.54%</b> |

| Australia                 | <i>Aaa</i> | <i>0.000%</i>        | <i>4.33%</i>        |
|---------------------------|------------|----------------------|---------------------|
| Cook Islands              | <i>B1</i>  | <i>5.000%</i>        | <i>9.59%</i>        |
| New Zealand               | <i>Aaa</i> | <i>0.000%</i>        | <i>4.33%</i>        |
| <b>Australia &amp; NZ</b> |            | <b><i>0.000%</i></b> | <b><i>4.33%</i></b> |

# **APPLICATION TEST: ESTIMATING AN EQUITY RISK PREMIUM FOR YOUR COMPANY!**

- ▪ For your company, **get the geographical breakdown of revenues in the most recent year**. Based upon this revenue breakdown and the most recent country risk premiums, estimate the equity risk premium that you would use for your company.
  
- ▪ This computation was **based entirely on revenues**. With your company, what concerns would you have about your estimate being too high or too low?

# ESTIMATING BETA

- ▪ The standard procedure for estimating betas is to regress stock returns ( $R_j$ ) against market returns ( $R_m$ ):

$$R_j = a + b R_m$$

- ▪ where  $a$  is the intercept and  $b$  is the slope of the regression.
- ▪ The slope of the regression corresponds to the beta of the stock and measures the riskiness of the stock.
- ▪ The  $R$  squared ( $R^2$ ) of the regression provides an estimate of the proportion of the risk (variance) of a firm that can be attributed to market risk. The balance ( $1 - R^2$ ) can be attributed to firm specific risk.
- ▪

# ESTIMATING PERFORMANCE

- The intercept of the regression provides a simple measure of performance during the period of the regression, relative to the capital asset pricing model.

- $$R_j = R_f + b (R_m - R_f)$$

- $$R_j = R_f (1-b) + b R_m$$

- $$R_j = a + b R_m$$

..... Capital Asset Pricing Model

..... Regression Equation

- If

- $$a > R_f (1-b) \dots \text{ regression period}$$

Stock did better than expected during

- $$a = R_f (1-b) \dots \text{ period}$$

Stock did as well as expected during regression

- $$a < R_f (1-b) \dots \text{ regression period}$$

Stock did worse than expected during

- The difference between the intercept and  $R_f (1-b)$  is Jensen's alpha. If it is positive, your stock did perform better than expected during the period of the regression.

# SETTING UP FOR THE ESTIMATION

- ▪ **Decide on an estimation period**
  - ▪ Services use periods ranging from 2 to 5 years for the regression
  - ▪ Longer estimation period provides more data, but firms change.
  - ▪ Shorter periods can be affected more easily by significant firm-specific event that occurred during the period
- ▪ **Decide on a return interval** - daily, weekly, monthly
  - ▪ Shorter intervals yield more observations, but suffer from more noise.
  - ▪ Noise is created by stocks not trading and biases all betas towards one.
- ▪ **Estimate returns** (including dividends) on stock
  - ▪  $\text{Return} = (\text{Price}_{\text{End}} - \text{Price}_{\text{Beginning}} + \text{Dividends}_{\text{Period}}) / \text{Price}_{\text{Beginning}}$
  - ▪ Included dividends only in ex-dividend month
- ▪ **Choose a market index**, and estimate returns (inclusive of dividends) on the index for each interval for the period.

# CHOOSING THE PARAMETERS: DISNEY

- ▪ Period used: 5 years
- ▪ Return Interval: Monthly
- ▪ Market Index: S&P 500 Index.
- ▪ For instance, to calculate returns on Disney in December 2009,
  - ▪ Price for Disney at end of November 2009 = \$ 30.22
  - ▪ Price for Disney at end of December 2009 = \$ 32.25
  - ▪ Dividends during month = \$0.35 (It was an ex-dividend month)
  - ▪ Disney Return =  $(\$32.25 - \$30.22 + \$ 0.35) / \$30.22 = 7.88\%$
- ▪ To estimate returns on the index in the same month
  - ▪ Index level at end of November 2009 = 1095.63
  - ▪ Index level at end of December 2009 = 1115.10
  - ▪ Dividends on index in December 2009 = 1.683
  - ▪ S&P 500 Return =  $(1115.1 - 1095.63 + 1.683) / 1095.63 = 1.78\%$

# DISNEY'S HISTORICAL BETA

![](_page_40_Figure_13.jpeg)

$$\text{Return on Disney} = .0071 + 1.2517 \text{ Return on Market} \\ (.0053) (0.10)$$

$$R^2 = 0.73386$$

# ANALYZING DISNEY'S PERFORMANCE

- ■ Intercept = 0.712%

- - ■ This is an intercept based on monthly returns. Thus, it has to be compared to a monthly riskfree rate.

- - ■ Between 2008 and 2013

- - - ■ Average Annualized T.Bill rate = 0.50%
    - ■ Monthly Riskfree Rate =  $0.5\%/12 = 0.042\%$
    - ■ Riskfree Rate (1-Beta) =  $0.042\% (1-1.252) = -.0105\%$

- ■ The Comparison is then between

- - ■ Intercept                      versus                      Riskfree Rate (1 - Beta)
  - ■ 0.712%                                  versus                      0.0105%
  - ■ Jensen's Alpha =  $0.712\% - (-0.0105)\% = 0.723\%$

- ■ Disney did 0.723% better than expected, per month, between October 2008 and September 2013

- - ■ Annualized, Disney's annual excess return =  $(1.00723)12 - 1 = 9.02\%$

# MORE ON JENSEN'S ALPHA

- ■ If you did this analysis on every stock listed on an exchange, what would the average Jensen's alpha be across all stocks?
  - a. Depend upon whether the market went up or down during the period
  - b. Should be zero
  - c. Should be greater than zero, because stocks tend to go up more often than down.
- ■ Disney has a positive Jensen's alpha of 9.02% a year between 2008 and 2013. This can be viewed as a sign that management in the firm did a good job, managing the firm during the period.
  - a. True
  - b. False
- ■ Disney has had a positive Jensen's alpha between 2008 and 2013. If you were an investor in early 2014, looking at the stock, you would view this as a sign that the stock will be a:
  - a. Good investment for the future
  - b. Bad investment for the future
  - c. No information about the future

# ESTIMATING DISNEY'S BETA

- ▪ The **slope of the regression** of 1.25 is the beta.
- ▪ The regression parameters are **always estimated with error**.  
  The error is captured in the standard error of the beta estimate, which in the case of Disney is 0.10.
- ▪ Assume that I asked you what Disney's true beta is, after this regression.
  - ▪ What is your best point estimate?
- ▪ What range would you give me, with 67% confidence?
- ▪ What range would you give me, with 95% confidence?

# THE DIRTY SECRET OF “STANDARD ERROR”

*Distribution of Standard Errors: Beta Estimates for U.S. stocks*

![](_page_44_Figure_66.jpeg)

# BREAKING DOWN DISNEY'S RISK

- ▪ The R Squared = 73%. This implies that
  - ▪ 73% of the risk at Disney comes from market sources
  - ▪ 27%, therefore, comes from firm-specific sources
- ▪ If investors diversify, the firm-specific risk is diversifiable and will not be rewarded. It is only the market risk that will be rewarded with a higher expected return.
- ▪ The R-squared for companies, globally, has increased significantly since 2008.
  - a. Why might this be happening?
  - b. What are the implications for investors?

# THE RELEVANCE OF R SQUARED

- ■ You are a diversified investor trying to decide whether you should invest in Disney or Amgen. Both companies have betas of 1.25, but Disney has an R Squared of 73% while Amgen's R squared is only 25%. Which one would you invest in?
  - a. Amgen, because it has the lower R squared
  - b. Disney, because it has the higher R squared
  - c. You would be indifferent
- ■ Would your answer be different if you were an undiversified investor?

# BETA ESTIMATION: USING A SERVICE (BLOOMBERG)

![](_page_47_Figure_6.jpeg)

# ESTIMATING EXPECTED RETURNS FOR DISNEY IN NOVEMBER 2013

- ▪ Inputs to the expected return calculation
  - ▪ Disney's Beta = 1.25
  - ▪ Riskfree Rate = 2.75% (U.S. ten-year T.Bond rate in November 2013)
  - ▪ Risk Premium = 5.76% (Based on Disney's operating exposure)
- ▪ Expected Return = Riskfree Rate + Beta (Risk Premium)
  $$= 2.75\% + 1.25 (5.76\%) = 9.95\%$$

# USE TO A POTENTIAL INVESTOR IN DISNEY

- ▪ As a potential investor in Disney, what does this expected return of 9.95% tell you?
  - a. This is the return that I can expect to make in the long term on Disney, if the stock is correctly priced and the CAPM is the right model for risk,
  - b. This is the return that I need to make on Disney in the long term to break even on my investment in the stock
  - c. Both
- ▪ Assume now that you are an active investor and that your research suggests that an investment in Disney will yield 12.5% a year for the next 5 years. Based upon the expected return of 9.95%, you would
  - a. Buy the stock
  - b. Sell the stock

# HOW MANAGERS USE THIS EXPECTED RETURN

- ▪ Managers at Disney

- - ▪ need to make at least 9.95% as a return for their equity investors to break even.

- - ▪ this is the hurdle rate for projects, when the investment is analyzed from an equity standpoint

- - ▪ In other words, Disney's cost of equity is 9.95% and it should try to deliver a return on equity that exceeds this value.

- - ▪ What is the cost of not delivering this cost of equity?

# APPLICATION TEST: ANALYZING THE RISK REGRESSION

- ▪ Using your Bloomberg risk and return print out, answer the following questions:
  - ▪ How well or badly did your stock do, relative to the market, during the period of the regression?
  - ▪ Intercept - (Riskfree Rate/n) (1 - Beta) = Jensen's Alpha
    - ▪ where n is the number of return periods in a year (12 if monthly; 52 if weekly)
  - ▪ What proportion of the risk in your stock is attributable to the market? What proportion is firm-specific?
  - ▪ What is the historical estimate of beta for your stock? What is the range on this estimate with 67% probability? With 95% probability?
  - ▪ Based upon this beta, what is your estimate of the required return on this stock?
  - ▪ Riskless Rate + Beta \* Risk Premium

# A QUICK TEST

- ■ You are advising a very risky software firm on the right cost of equity to use in project analysis. You estimate a beta of 3.0 for the firm and come up with a cost of equity of 20%. The CFO of the firm is concerned about the high cost of equity and wants to know whether there is anything he can do to lower his beta.
- ■ How do you bring your beta down?
  
- ■ Should you focus your attention on bringing your beta down?
  - ■ Yes
  - ■ No

# REGRESSION DIAGNOSTICS FOR TATA MOTORS

![](_page_53_Figure_55.jpeg)

Beta = 1.83  
67% range  
1.67-1.99

69% market risk  
31% firm specific

Jensen's  $\alpha$   
 $= 2.28\% - 4\%/12 (1-1.83) = 2.56\%$   
 Annualized =  $(1+.0256)^{12}-1 = 35.42\%$   
 Average monthly riskfree rate (2008-13) = 4%  
 Aswath Damodaran

rmany 49 69 9204 1  
 Copyright  
 ST GHT-5:00 G627-

Expected Return (in Rupees)  
 $= \text{Riskfree Rate} + \text{Beta} * \text{Risk premium}$   
 $= 6.57\% + 1.83 (7.19\%) = 19.73\%$ 

# A BETTER BETA? FOR VALE.

![](_page_54_Figure_7.jpeg)

![](_page_54_Figure_8.jpeg)

# DEUTSCHE BANK AND BAIDU: INDEX EFFECTS ON RISK PARAMETERS

- ▪ For Deutsche Bank, a widely held European stock, we tried both the DAX (German index) and the FTSE European index.

|                       | <i>DAX</i> | <i>FTSE Euro 100</i> |
|-----------------------|------------|----------------------|
| Intercept             | -0.90%     | -0.15%               |
| Beta                  | 1.58       | 1.98                 |
| Std Error of beta     | 0.21       | 0.29                 |
| <i>R</i> <sup>2</sup> | 51%        | 29%                  |

- ▪ For Baidu, a NASDAQ listed stock, we ran regressions against both the S&P 500 and the NASDAQ.

|                       | <i>S&amp;P 500</i> | <i>NASDAQ</i> |
|-----------------------|--------------------|---------------|
| Intercept             | 2.84%              | 2.15%         |
| Beta                  | 1.63               | 1.65          |
| Std Error of beta     | 0.28               | 0.23          |
| <i>R</i> <sup>2</sup> | 37%                | 47%           |

# BETA: EXPLORING FUNDAMENTALS

| Beta > 2             |  | Bulgari: 2.45                                     |
|----------------------|--|---------------------------------------------------|
| Beta between 1 and 2 |  | Qwest Communications: 1.85                        |
| Beta < 1             |  | Microsoft: 1.25<br>GE: 1.15                       |
| Beta < 0             |  | Exxon Mobil: 0.70<br>Altria (Philip Morris): 0.60 |
| Beta < 0             |  | Harmony Gold Mining: -0.15                        |

# DETERMINANT 1: PRODUCT/ SERVICE TYPE

- ▪ Betas measure a company's exposure to macroeconomic risks. Consequently, you would expect the beta to be a function of the **sensitivity of the demand for its products and services to macroeconomic factors.**
  - ▪ To the extent that **cyclical companies are more likely to move with the macroeconomy, they are likely to have higher betas.**
  - ▪ Firms which sell more discretionary products will have higher betas than firms that sell less discretionary product

# A SIMPLE TEST

- ▪ Phone service is close to being non-discretionary in the United States and Western Europe. However, in much of Asia and Latin America, there are large segments of the population for which phone service is a luxury.
- ▪ Given our discussion of discretionary and non-discretionary products, which of the following conclusions would you be willing to draw:
  - a. Emerging market telecom companies should have higher betas than developed market telecom companies.
  - b. Developed market telecom companies should have higher betas than emerging market telecom companies
  - c. The two groups of companies should have similar betas

# DETERMINANT 2: OPERATING LEVERAGE EFFECTS

- ▪ Operating leverage refers to the proportion of the total costs of the firm that are fixed.
- ▪ When a company has higher fixed costs, small changes in revenues will translate into larger changes in earnings, and by extension, into more variable earnings.
  - ▪ Other things remaining equal, sectors with **higher operating leverage should have higher betas** than sectors with less operating leverage.
  - ▪ Within sectors, companies with **more flexible cost structures (where costs adjust more quickly to revenues) should have lower betas** than companies with more rigid cost structures.

# MEASURES OF OPERATING LEVERAGE

- ▪ Fixed Costs Measure = Fixed Costs / Variable Costs
  - ▪ This measures the **relationship between fixed and variable costs**. The higher the proportion, the higher the operating leverage.
  - ▪ The problem with this measure is that companies **do not break costs down into fixed and variable**.
- ▪ EBIT Variability Measure = % Change in EBIT / % Change in Revenues
  - ▪ This measures **how quickly the earnings before interest and taxes changes as revenue changes**. The higher this number, the greater the operating leverage.
  - ▪ There is **noise in this number** on a year-to-year basis.

# DISNEY'S OPERATING LEVERAGE: 1987- 2013

| Year                  | Net Sales | % Change in Sales | EBIT    | % Change in EBIT |                           |
|-----------------------|-----------|-------------------|---------|------------------|---------------------------|
| 1987                  | \$2,877   |                   | \$756   |                  |                           |
| 1988                  | \$3,438   | 19.50%            | \$848   | 12.17%           |                           |
| 1989                  | \$4,594   | 33.62%            | \$1,177 | 38.80%           |                           |
| 1990                  | \$5,844   | 27.21%            | \$1,368 | 16.23%           |                           |
| 1991                  | \$6,182   | 5.78%             | \$1,124 | -17.84%          |                           |
| 1992                  | \$7,504   | 21.38%            | \$1,287 | 14.50%           |                           |
| 1993                  | \$8,529   | 13.66%            | \$1,560 | 21.21%           |                           |
| 1994                  | \$10,055  | 17.89%            | \$1,804 | 15.64%           |                           |
| 1995                  | \$12,112  | 20.46%            | \$2,262 | 25.39%           |                           |
| 1996                  | \$18,739  | 54.71%            | \$3,024 | 33.69%           |                           |
| 1997                  | \$22,473  | 19.93%            | \$3,945 | 30.46%           |                           |
| 1998                  | \$22,976  | 2.24%             | \$3,843 | -2.59%           |                           |
| 1999                  | \$23,435  | 2.00%             | \$3,580 | -6.84%           |                           |
| 2000                  | \$25,418  | 8.46%             | \$2,525 | -29.47%          |                           |
| 2001                  | \$25,172  | -0.97%            | \$2,832 | 12.16%           |                           |
| 2002                  | \$25,329  | 0.62%             | \$2,384 | -15.82%          |                           |
| 2003                  | \$27,061  | 6.84%             | \$2,713 | 13.80%           |                           |
| 2004                  | \$30,752  | 13.64%            | \$4,048 | 49.21%           |                           |
| 2005                  | \$31,944  | 3.88%             | \$4,107 | 1.46%            |                           |
| 2006                  | \$33,747  | 5.64%             | \$5,355 | 30.39%           |                           |
| 2007                  | \$35,510  | 5.22%             | \$6,829 | 27.53%           |                           |
| 2008                  | \$37,843  | 6.57%             | \$7,404 | 8.42%            |                           |
| 2009                  | \$36,149  | -4.48%            | \$5,697 | -23.06%          |                           |
| 2010                  | \$38,063  | 5.29%             | \$6,726 | 18.06%           |                           |
| 2011                  | \$40,893  | 7.44%             | \$7,781 | 15.69%           |                           |
| 2012                  | \$42,278  | 3.39%             | \$8,863 | 13.91%           |                           |
| 2013                  | \$45,041  | 6.54%             | \$9,450 | 6.62%            |                           |
| <b>Average: 87-13</b> |           | <b>11.79%</b>     |         | <b>11.91%</b>    | <b>11.91/11.79 = 1.01</b> |
| <b>Average: 96-13</b> |           | <b>8.16%</b>      |         | <b>10.20%</b>    | <b>10.20/8.16 = 1.25</b>  |

![](_page_61_Picture_365.jpeg)

# DETERMINANT 3: FINANCIAL LEVERAGE

- ▪ As firms borrow, they create fixed costs (interest payments) that make their earnings to equity investors more volatile. This increased earnings volatility which increases the equity beta.
- ▪ The beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_{\text{Levered}} = \beta_{\text{unlevered}} (1 + ((1-t)D/E))$$

where

- ▪  $\beta_L$  = Levered or Equity Beta       $D/E$  = Market value Debt to equity ratio
- ▪  $\beta_u$  = Unlevered or Asset Beta       $t$  = Marginal tax rate
- ▪ Earlier, we estimated the beta for Disney from a regression. Was that beta a levered or unlevered beta?
  - a. Levered
  - b. Unlevered

# EFFECTS OF LEVERAGE ON BETAS: DISNEY

- ▪ The regression beta for Disney is 1.25. This beta is a levered beta (because it is based on stock prices, which reflect leverage) and the leverage implicit in the beta estimate is the average market debt equity ratio during the period of the regression (2008 to 2013)
  - ▪ The average debt equity ratio during this period was 19.44%.
  - ▪ The unlevered beta for Disney can then be estimated (using a marginal tax rate of 36.1%)
    - ▪ Disney's Unlevered Beta  
       $= \text{Regression Beta} / (1 + (1 - \text{tax rate}) (\text{Average Debt/Equity}))$   
       $= 1.25 / (1 + (1 - 0.361)(0.1944)) = 1.11$

# DISNEY : BETA AND FINANCIAL LEVERAGE

| <i>Debt to Capital</i> | <i>Debt/Equity Ratio</i> | <i>Beta</i> | <i>Effect of Leverage</i> |
|------------------------|--------------------------|-------------|---------------------------|
| 0.00%                  | 0.00%                    | 1.11        | 0.00                      |
| 10.00%                 | 11.11%                   | 1.1908      | 0.08                      |
| 20.00%                 | 25.00%                   | 1.29        | 0.18                      |
| 30.00%                 | 42.86%                   | 1.42        | 0.30                      |
| 40.00%                 | 66.67%                   | 1.59        | 0.47                      |
| 50.00%                 | 100.00%                  | 1.82        | 0.71                      |
| 60.00%                 | 150.00%                  | 2.18        | 1.07                      |
| 70.00%                 | 233.33%                  | 2.77        | 1.66                      |
| 80.00%                 | 400.00%                  | 3.95        | 2.84                      |
| 90.00%                 | 900.00%                  | 7.51        | 6.39                      |

# BETAS ARE WEIGHTED AVERAGES

- ▪ The beta of a portfolio is always the market-value weighted average of the betas of the individual investments in that portfolio.
- ▪ Thus,
  - ▪ the beta of a mutual fund is the **weighted average of the betas of the stocks** and other investment in that portfolio
  - ▪ the beta of a firm after a merger is the market-value weighted average of the **betas of the companies involved in the merger**.
  - ▪ The beta of a company is a **weighted average of the businesses that it invests in...**

# THE DISNEY/CAP CITIES MERGER (1996): PRE-MERGER

## Disney: The Acquirer

Equity Beta  
1.15

Debt = \$3,186 million

Market value of equity = \$31,100 million

Debt + Equity = Firm value = \$31,100

+ \$3186 = \$34,286 million

D/E Ratio =  $\frac{3186}{31100} = 0.10$ 

+

## Capital Cities: The Target

Equity Beta  
0.95

Debt = \$ 615 million

Market value of equity = \$18,500 million

Debt + Equity = Firm value = \$18,500 +

\$615 = \$19,115 million

D/E Ratio =  $\frac{615}{18500} = 0.03$ 

# DISNEY CAP CITIES BETA ESTIMATION: STEP 1

- ▪ Calculate the unlevered betas for both firms
  - ▪ Disney's unlevered beta =  $1.15/(1+0.64*0.10) = 1.08$
  - ▪ Cap Cities unlevered beta =  $0.95/(1+0.64*0.03) = 0.93$
- ▪ Calculate the unlevered beta for the combined firm
  - ▪ Unlevered Beta for combined firm  
     $= 1.08 (34286/53401) + 0.93 (19115/53401)$   
     $= 1.026$
- ▪ The weights used are the firm values (and not just the equity values) of the two firms, since these are unlevered betas and thus reflects the risks of the entire businesses and not just the equity]

# DISNEY CAP CITIES BETA ESTIMATION: STEP 2

- ■ If Disney had **used all equity** to buy Cap Cities equity, while assuming Cap Cities debt, the consolidated numbers would have looked as follows:
  - ■  $\text{Debt} = \$ 3,186 + \$615 = \$ 3,801 \text{ million}$
  - ■  $\text{Equity} = \$ 31,100 + \$18,500 = \$ 49,600 \text{ m (Disney issues $18.5 billion in equity)}$
  - ■  $\text{D/E Ratio} = 3,801/49600 = 7.66\%$
  - ■  $\text{New Beta} = 1.026 (1 + 0.64 (.0766)) = 1.08$
- ■ Since Disney **borrowed \$ 10 billion** to buy Cap Cities/ABC, funded the rest with new equity and assumed Cap Cities debt:
  - ■ The market value of Cap Cities equity is \$18.5 billion. If \$ 10 billion comes from debt, the balance (\$8.5 billion) has to come from new equity.
  - ■  $\text{Debt} = \$ 3,186 + \$615 \text{ million} + \$ 10,000 = \$ 13,801 \text{ million}$
  - ■  $\text{Equity} = \$ 31,100 + \$8,500 = \$39,600 \text{ million}$
  - ■  $\text{D/E Ratio} = 13,801/39600 = 34.82\%$
  - ■  $\text{New Beta} = 1.026 (1 + 0.64 (.3482)) = 1.25$

# FIRM BETAS VERSUS DIVISIONAL BETAS

- ▪ **Firm Betas as weighted averages: The beta of a firm is the weighted average of the betas of its individual projects.**
  - ▪ Since betas measure exposure to macro risk, if the projects are all in the same line of business, they may all share the same unlevered beta.
  - ▪ If the projects vary in their macroeconomic risk exposure, the project betas will also vary.
- ▪ **Firm Betas and Business betas: At a broader level of aggregation, the beta of a multi-business firm is the weighted average of the betas of the different businesses that they operate in.**

# BOTTOM-UP VERSUS TOP-DOWN BETA

- ▪ The **top-down beta** for a firm comes from a regression
- ▪ The **bottom-up beta** can be estimated by doing the following:
  - ▪ Find out the businesses that a firm operates in
  - ▪ Find the unlevered betas of other firms in these businesses
  - ▪ Take a weighted (by sales or operating income) average of these unlevered betas
  - ▪ Lever up using the firm's debt/equity ratio
- ▪ The bottom-up beta is a better estimate than the top down beta for the following reasons
  - ▪ The **standard error** of the beta estimate will **be much lower**
  - ▪ The betas can reflect the **current (and even expected future) mix of businesses** that the firm is in rather than the historical mix

# DISNEY'S BUSINESSES: THE FINANCIAL BREAKDOWN (FROM 2013 ANNUAL REPORT)

| <i>Business</i>      | <i>Revenues</i> | <i>Operating Income</i> | <i>D&amp;A</i> | <i>EBITDA</i> | <i>S, G &amp; A Costs</i> | <i>Cap Ex</i> | <i>Identifiable Assets</i> |
|----------------------|-----------------|-------------------------|----------------|---------------|---------------------------|---------------|----------------------------|
| Media Networks       | \$20,356        | \$6,818                 | \$251          | \$7,069       | \$2,768                   | \$263         | \$28,627                   |
| Parks & Resorts      | \$14,087        | \$2,220                 | \$1,370        | \$3,590       | \$1,960                   | \$2,110       | \$22,056                   |
| Studio Entertainment | \$5,979         | \$661                   | \$161          | \$822         | \$2,145                   | \$78          | \$14,750                   |
| Consumer Products    | \$3,555         | \$1,112                 | \$146          | \$1,258       | \$731                     | \$45          | \$7,506                    |
| Interactive          | \$1,064         | -\$87                   | \$44           | -\$43         | \$449                     | \$13          | \$2,311                    |

# UNLEVERED BETAS FOR BUSINESSES

Unlevered Beta  
(1 - Cash/ Firm Value)

| Business             | Comparable firms                               | Sample size | Median Beta | Median D/E | Median Tax rate | Company Unlevered Beta | Median Cash/ Firm Value | Business Unlevered Beta |
|----------------------|------------------------------------------------|-------------|-------------|------------|-----------------|------------------------|-------------------------|-------------------------|
| Media Networks       | US firms in broadcasting business              | 26          | 1.43        | 71.09%     | 40.00%          | 1.0024                 | 2.80%                   | 1.0313                  |
| Parks & Resorts      | Global firms in amusement park business        | 20          | 0.87        | 46.76%     | 35.67%          | 0.6677                 | 4.95%                   | 0.7024                  |
| Studio Entertainment | US movie firms                                 | 10          | 1.24        | 27.06%     | 40.00%          | 1.0668                 | 2.96%                   | 1.0993                  |
| Consumer Products    | Global firms in toys/games production & retail | 44          | 0.74        | 29.53%     | 25.00%          | 0.6034                 | 10.64%                  | 0.6752                  |
| Interactive          | Global computer gaming firms                   | 33          | 1.03        | 3.26%      | 34.55%          | 1.0085                 | 17.25%                  | 1.2187                  |

# A CLOSER LOOK AT THE PROCESS... STUDIO ENTERTAINMENT BETAS

| Company Name                                           | Levered Beta | Market Capitalization | + Total Debt including Leases | =Firm Value  | -Cash      | = Enterprise Value | Cash/Firm Value | Pre-tax cost of debt | Marginal tax rate | Gross D/E ratio | Revenue (Sales) | EV/Sales |             |
|--------------------------------------------------------|--------------|-----------------------|-------------------------------|--------------|------------|--------------------|-----------------|----------------------|-------------------|-----------------|-----------------|----------|-------------|
| SFX Entertainment Inc.<br>(NasdaqGS:SFXE)              | 1.12         | \$738.8               | \$98.9                        | \$837.7      | \$143.6    | \$694.1            | 17.14%          | 8.46%                | 40.00%            | 13.39%          | 62.0            | 11.20    |             |
| Mass Hysteria Entertainment Company, Inc. (OTCPK:MHYS) | 1.19         | \$0.2                 | \$1.1                         | \$1.4        | \$-        | \$1.4              | 0.00%           | 10.00%               | 40.00%            | 477.94%         | 0               | 12.45    |             |
| Medient Studios, Inc.<br>(OTCPK:MDNT)                  | 0.93         | \$3.2                 | \$3.2                         | \$6.4        | \$0.1      | \$6.3              | 0.81%           | 4.84%                | 40.00%            | 99.07%          | 5.22            | 1.21     |             |
| POW! Entertainment, Inc.<br>(OTCPK:POWN)               | 0.94         | \$4.0                 | \$0.3                         | \$4.3        | \$0.4      | \$3.9              | 9.85%           | 4.00%                | 40.00%            | 8.65%           | 2.03            | 1.92     |             |
| MGM Holdings Inc. (OTCPK:MGMB)                         | 1.29         | \$3,631.7             | \$142.2                       | \$3,773.9    | \$140.7    | \$3,633.2          | 3.73%           | 10.00%               | 40.00%            | 3.91%           | 1,892.6         | 1.92     |             |
| Lions Gate Entertainment Corp.<br>(NYSE:LGF)           | 1.20         | \$4,719.6             | \$1,283.2                     | \$6,002.8    | \$67.2     | \$5,935.6          | 1.12%           | 6.34%                | 40.00%            | 27.19%          | 2,597.8         | 2.28     |             |
| DreamWorks Animation SKG Inc.<br>(NasdaqGS:DWA)        | 1.32         | \$2,730.0             | \$348.3                       | \$3,078.3    | \$156.4    | \$2,921.9          | 5.08%           | 3.00%                | 40.00%            | 12.76%          | 767.3           | 3.81     |             |
| Twenty-First Century Fox, Inc.<br>(NasdaqGS:FOXA)      | 1.28         | \$77,743.5            | \$20,943.0                    | \$98,686.5   | \$6,681.0  | \$92,005.5         | 6.77%           | 6.15%                | 40.00%            | 26.94%          | 28,733.0        | 3.20     |             |
| Independent Film Development Corporation (OTCPK:IFLM)  | 1.61         | \$1.3                 | \$1.0                         | \$2.3        | \$-        | \$2.2              | 2.20%           | 10.00%               | 40.00%            | 72.35%          | 1               | 3.37     |             |
| Odyssey Pictures Corp.<br>(OTCPK:OPIX)                 | 2.60         | \$0.3                 | \$1.6                         | \$1.9        | \$0.0      | \$1.9              | 0.10%           | 3.00%                | 40.00%            | 551.12%         | 0.669           | 2.90     |             |
| <b>Average</b>                                         | <b>1.35</b>  |                       |                               |              |            |                    |                 | <b>4.68%</b>         | <b>6.58%</b>      | <b>40.00%</b>   | <b>129.33%</b>  |          | <b>4.43</b> |
| <b>Aggregate</b>                                       | <b>1.35</b>  |                       | \$22,822.82                   | \$112,395.45 | \$7,189.43 | \$105,206.02       | 6.40%           | 6.58%                | 40.00%            | 25.48%          | 34,061.4        | 3.09     |             |
| <b>Median</b>                                          | <b>1.24</b>  |                       |                               |              |            |                    | 2.96%           | 6.24%                | 40.00%            | 27.06%          |                 | 3.05     |             |

# BACKING INTO A PURE PLAY BETA: THE MEDIAN MOVIE COMPANY

|                | Value | Beta   |        | Value | Beta |
|----------------|-------|--------|--------|-------|------|
| Movie Business | 97.04 | 1.0993 | Debt   | 21.3  | 0    |
| Cash Business  | 2.96  | 0      | Equity | 78.7  | 1.24 |
| Movie Company  | 100   | 1.0668 |        |       |      |

1. 1. Start with the median regression beta (equity beta) of 1.24
2. 2. Unlever the beta, using the median gross D/E ratio of 27.06%

$$\text{Gross D/E ratio} = 21.30/78.70 = 27.06\%$$

$$\text{Unlevered beta} = 1.24/(1 + (1 - .4)(.2706)) = 1.0668$$

1. 3. Take out the cash effect, using the median cash/value of 2.96%

$$(.0296)(0) + (1 - .0296)(\text{Beta of movie business}) = 1.0668$$

$$\text{Beta of movie business} = 1.0668/(1 - .0296) = 1.0993$$

**Alternatively, you could have used the net debt to equity ratio**

$$\text{Net D/E ratio} = (21.30 - 2.96)/78.70 = 23.30\%$$

$$\text{Unlevered beta for movies} = 1.24/(1 + (1 - .4)(.233)) = 1.0879$$

# DISNEY'S UNLEVERED BETA: OPERATIONS & ENTIRE COMPANY

## *Disney Operations: Unlevered Beta*

| Business             | Revenues | EV/Sales | Value of Business | Proportion of Disney | Unlevered beta | Value        | Proportion |
|----------------------|----------|----------|-------------------|----------------------|----------------|--------------|------------|
| Media Networks       | \$20,356 | 3.27     | \$66,580          | 49.27%               | 1.03           | \$66,579.81  | 49.27%     |
| Parks & Resorts      | \$14,087 | 3.24     | \$45,683          | 33.81%               | 0.70           | \$45,682.80  | 33.81%     |
| Studio Entertainment | \$5,979  | 3.05     | \$18,234          | 13.49%               | 1.10           | \$18,234.27  | 13.49%     |
| Consumer Products    | \$3,555  | 0.83     | \$2,952           | 2.18%                | 0.68           | \$2,951.50   | 2.18%      |
| Interactive          | \$1,064  | 1.58     | \$1,684           | 1.25%                | 1.22           | \$1,683.72   | 1.25%      |
| Disney Operations    | \$45,041 |          | \$135,132         | 100.00%              | 0.9239         | \$135,132.11 |            |

## *Disney – The Company: Unlevered Beta*

Disney has \$3.93 billion in cash, invested in close to riskless assets (with a beta of zero).  
 You can compute an unlevered beta for Disney as a company (inclusive of cash):

$$\begin{aligned}
 \beta_{\text{Disney}} &= \beta_{\text{Operating Assets}} \frac{\text{Value}_{\text{Operating Assets}}}{(\text{Value}_{\text{Operating Assets}} + \text{Value}_{\text{Cash}})} + \beta_{\text{Cash}} \frac{\text{Value}_{\text{Cash}}}{(\text{Value}_{\text{Operating Assets}} + \text{Value}_{\text{Cash}})} \\
 &= 0.9239 \left( \frac{135,132}{(135,132 + 3,931)} \right) + 0.00 \left( \frac{3,931}{(135,132 + 3,931)} \right) = 0.8978
 \end{aligned}$$

# THE LEVERED BETA: DISNEY AND ITS DIVISIONS

- To estimate the debt ratios for division, we allocate Disney's total debt (\$15,961 million) to its divisions based on identifiable assets.

| Business             | Identifiable assets (2013) | Proportion of debt | Value of business | Allocated debt | Estimated equity | D/E ratio |
|----------------------|----------------------------|--------------------|-------------------|----------------|------------------|-----------|
| Media Networks       | \$28,627                   | 38.04%             | \$66,580          | \$6,072        | \$60,508         | 10.03%    |
| Parks & Resorts      | \$22,056                   | 29.31%             | \$45,683          | \$4,678        | \$41,005         | 11.41%    |
| Studio Entertainment | \$14,750                   | 19.60%             | \$18,234          | \$3,129        | \$15,106         | 20.71%    |
| Consumer Products    | \$7,506                    | 9.97%              | \$2,952           | \$1,592        | \$1,359          | 117.11%   |
| Interactive          | \$2,311                    | 3.07%              | \$1,684           | \$490          | \$1,194          | 41.07%    |
| Disney               | \$75,250                   | 100.00%            |                   | \$15,961       | \$121,878        | 13.10%    |

- We use the allocated debt to compute D/E ratios and levered betas.

| Business             | Unlevered beta | Value of business | D/E ratio | Levered beta | Cost of Equity |
|----------------------|----------------|-------------------|-----------|--------------|----------------|
| Media Networks       | 1.0313         | \$66,580          | 10.03%    | 1.0975       | 9.07%          |
| Parks & Resorts      | 0.7024         | \$45,683          | 11.41%    | 0.7537       | 7.09%          |
| Studio Entertainment | 1.0993         | \$18,234          | 20.71%    | 1.2448       | 9.92%          |
| Consumer Products    | 0.6752         | \$2,952           | 117.11%   | 1.1805       | 9.55%          |
| Interactive          | 1.2187         | \$1,684           | 41.07%    | 1.5385       | 11.61%         |
| Disney Operations    | 0.9239         | \$135,132         | 13.10%    | 1.0012       | 8.52%          |

# DISCUSSION ISSUE

- ▪ Assume now that you are the CFO of Disney. The head of the movie business has come to you with a new big budget movie that he would like you to fund. He claims that his analysis of the movie indicates that it will generate a return on equity of 9.5%. Would you fund it?
  - a. Yes. It is higher than the cost of equity for Disney as a company
  - b. No. It is lower than the cost of equity for the movie business.
- ▪ What are the broader implications of your choice?

# ESTIMATING BOTTOM UP BETAS & COSTS OF EQUITY: VALE

| Business        | Sample                                                  | Sample size | Unlevered beta of business | Revenues | Peer Group EV/Sales | Value of Business | Proportion of Vale |
|-----------------|---------------------------------------------------------|-------------|----------------------------|----------|---------------------|-------------------|--------------------|
| Metals & Mining | Global firms in metals & mining, Market cap>\$1 billion | 48          | 0.86                       | \$9,013  | 1.97                | \$17,739          | 16.65%             |
| Iron Ore        | Global firms in iron ore                                | 78          | 0.83                       | \$32,717 | 2.48                | \$81,188          | 76.20%             |
| Fertilizers     | Global specialty chemical firms                         | 693         | 0.99                       | \$3,777  | 1.52                | \$5,741           | 5.39%              |
| Logistics       | Global transportation firms                             | 223         | 0.75                       | \$1,644  | 1.14                | \$1,874           | 1.76%              |
| Vale Operations |                                                         |             | 0.8440                     | \$47,151 |                     | \$106,543         | 100.00%            |

| Business        | Unlevered beta | D/E ratio | Levered beta | Risk free rate | ERP   | Cost of Equity |
|-----------------|----------------|-----------|--------------|----------------|-------|----------------|
| Metals & Mining | 0.86           | 54.99%    | 1.1657       | 2.75%          | 7.38% | 11.35%         |
| Iron Ore        | 0.83           | 54.99%    | 1.1358       | 2.75%          | 7.38% | 11.13%         |
| Fertilizers     | 0.99           | 54.99%    | 1.3493       | 2.75%          | 7.38% | 12.70%         |
| Logistics       | 0.75           | 54.99%    | 1.0222       | 2.75%          | 7.38% | 10.29%         |
| Vale Operations | 0.84           | 54.99%    | 1.1503       | 2.75%          | 7.38% | 11.23%         |

# VALE: COST OF EQUITY CALCULATION – IN NOMINAL \$R

- ▪ To convert a discount rate in one currency to another, all you need are expected inflation rates in the two currencies.

$$(1 + \text{\$ Cost of Equity}) \frac{(1 + \text{Inflation Rate}_{\text{Brazil}})}{(1 + \text{Inflation Rate}_{\text{US}})} - 1$$

- ▪ **Inflation Differential:** If we use 2% as the inflation rate in US dollars and 9% as the inflation ratio in Brazil, we can convert Vale's US dollar cost of equity of 11.23% to a \$R cost of equity:

$$\begin{aligned}\text{Cost of Equity}_{\text{Nominal R\$}} &= (1 + \text{Cost of Equity}_{\text{US \$}}) \frac{(1 + \text{Expected Inflation}_{\text{R\$}})}{(1 + \text{Expected Inflation}_{\text{US \$}})} - 1 \\ &= (1.1123) \frac{(1.09)}{(1.02)} - 1 = 18.87\%\end{aligned}$$

- ▪ **Riskfree Rate:** Alternatively, you can compute a cost of equity, starting with the \$R riskfree rate of 10.18%.
  - ▪ Cost of Equity in \$R =  $10.18\% + 1.15 (7.38\%) = 18.67\%$

# BOTTOM UP BETAS & COSTS OF EQUITY: TATA MOTORS & BAIDU

- ▪ **Tata Motors:** We estimated an unlevered beta of 0.8601 across 76 publicly traded automotive companies (globally) and estimated a levered beta based on Tata Motor's D/E ratio of 41.41% and a marginal tax rate of 32.45% for India:
  - ▪ Levered Beta for Tata Motors =  $0.8601 (1 + (1 - .3245) (.4141)) = 1.1007$
  - ▪ Cost of equity for Tata Motors (Rs) =  $6.57\% + 1.1007 (7.19\%) = 14.49\%$
- ▪ **Baidu:** To estimate its beta, we looked at 42 global companies that derive all or most of their revenues from online advertising and estimated an unlevered beta of 1.30 for the business. Incorporating Baidu's current market debt to equity ratio of 5.23% and the marginal tax rate for China of 25%, we estimate Baidu's current levered beta to be 1.3560.
  - ▪ Levered Beta for Baidu =  $1.30 (1 + (1 - .25) (.0523)) = 1.356$
  - ▪ Cost of Equity for Baidu (Renmimbi) =  $3.50\% + 1.356 (6.94\%) = 12.91\%$

# BOTTOM UP BETAS AND COSTS OF EQUITY: DEUTSCHE BANK

- ■ We break **Deutsche Bank** down into two businesses – commercial and investment banking.

| <i>Company</i> | <i>Largest holder</i>  | <i># of institutional investors in top ten holdings</i> |
|----------------|------------------------|---------------------------------------------------------|
| Disney         | Laurene Jobs (7.3%)    | 8                                                       |
| Deutsche Bank  | Blackrock (4.69%)      | 10                                                      |
| Vale Preferred | Aberdeen (7.40%)       | 8                                                       |
| Tata Motors    | Tata Sons (26.07%)     | 7                                                       |
| Baidu (A)      | Capital Group (12.46%) | 10                                                      |

- ■ We do not unlever or relever betas, because estimating debt and equity for banks is an exercise in futility. Using a riskfree rate of 1.75% (Euro risk free rate) and Deutsche's ERP of 6.12%:

| <i>Business</i>    | <i>Beta</i> | <i>Cost of Equity</i>             |
|--------------------|-------------|-----------------------------------|
| Commercial banking | 1.0665      | $1.75\%+1.0665 (6.12\%) = 8.28\%$ |
| Investment Banking | 1.2550      | $1.75\%+1.2550 (6.12\%) = 9.44\%$ |
| Deutsche Bank      | 1.1516      | $1.75\%+1.1516 (6.12\%) = 8.80\%$ |

# ESTIMATING BETAS FOR NON-TRADED ASSETS

- ▪ The regression beta approach of estimating betas from regressions do not work for **assets that are not traded**. There are no stock prices or historical returns that can be used to compute regression betas.
- ▪ There are two ways in which betas can be estimated for non-traded assets
  - ▪ Using **comparable firms**
  - ▪ Using **accounting earnings**

# USING COMPARABLE FIRMS TO ESTIMATE BETA FOR BOOKSCAPE

| <i>Company Name</i>     | <i>Industry</i> | <i>Market Capitalization</i> | <i>Levered Beta</i> | <i>Marginal tax rate</i> | <i>Gross D/E ratio</i> | <i>Cash/Firm Value</i> | <i>R<sup>2</sup></i> |
|-------------------------|-----------------|------------------------------|---------------------|--------------------------|------------------------|------------------------|----------------------|
| Red Giant Entertainment | Publishing      | \$2.13                       | 0.69                | 40.00%                   | 0.00%                  | 0.05%                  | 0.1300               |
| CTM Media Holdings      | Publishing      | \$25.20                      | 1.04                | 40.00%                   | 17.83%                 | 33.68%                 | 0.1800               |
| Books-A-Million         | Book Stores     | \$38.60                      | 1.42                | 40.00%                   | 556.55%                | 4.14%                  | 0.1900               |
| Dex Media               | Publishing      | \$90.50                      | 4.92                | 40.00%                   | 3190.39%               | 7.86%                  | 0.2200               |
| Martha Stewart Living   | Publishing      | \$187.70                     | 1.11                | 40.00%                   | 19.89%                 | 15.86%                 | 0.3500               |
| Barnes & Noble          | Book Stores     | \$939.30                     | 0.11                | 40.00%                   | 164.54%                | 3.22%                  | 0.2600               |
| Scholastic Corporation  | Publishing      | \$953.80                     | 1.08                | 40.00%                   | 21.41%                 | 1.36%                  | 0.2750               |
| John Wiley              | Publishing      | \$2,931.40                   | 0.81                | 40.00%                   | 29.58%                 | 5.00%                  | 0.3150               |
| Washington Post         | Publishing      | \$4,833.20                   | 0.68                | 40.00%                   | 21.04%                 | 16.04%                 | 0.2680               |
| News Corporation        | Publishing      | \$10,280.40                  | 0.49                | 40.00%                   | 8.73%                  | 24.05%                 | 0.2300               |
| Thomson Reuters         | Publishing      | \$31,653.80                  | 0.62                | 40.00%                   | 26.38%                 | 1.68%                  | 0.2680               |
| <b>Average</b>          |                 |                              | <b>1.1796</b>       | <b>40.00%</b>            | <b>368.76%</b>         | <b>10.27%</b>          | <b>0.2442</b>        |
| <b>Median</b>           |                 |                              | <b>0.8130</b>       | <b>40.00%</b>            | <b>21.41%</b>          | <b>5.00%</b>           | <b>0.2600</b>        |

Unlevered beta for book company =  $0.8130 / (1 + (1 - .4) \cdot (.2141)) = 0.7205$ 

Unlevered beta for book business =  $0.7205 / (1 - .05) = 0.7584$ 

# ESTIMATING BOOKSCAPE LEVERED BETA AND COST OF EQUITY

- ▪ Because the debt/equity ratios used in computing levered betas are market debt equity ratios, and the only debt equity ratio we can compute for Bookscape is a book value debt equity ratio, we have assumed that Bookscape is **close to the book industry median market debt to equity ratio of 21.41 percent.**
- ▪ Using a **marginal tax rate of 40 percent** for Bookscape, we get a levered beta of 0.8558.
  - ▪ Levered beta for Bookscape =  $0.7584[1 + (1 - 0.40)(0.2141)] = 0.8558$
- ▪ Using a riskfree rate of 2.75% (US treasury bond rate) and an equity risk premium of 5.5%:
  - ▪ Cost of Equity =  $2.75\% + 0.8558(5.5\%) = 7.46\%$

# IS BETA AN ADEQUATE MEASURE OF RISK FOR A PRIVATE FIRM?

## Private Owner versus Publicly Traded Company Perceptions of Risk in an Investment

![](_page_85_Diagram_103.jpeg)

# TOTAL RISK VERSUS MARKET RISK

- ▪ **Adjust the beta to reflect total risk rather than market risk.**

This adjustment is a relatively simple one, since the R squared of the regression measures the proportion of the risk that is market risk.

- - ▪ Total Beta = Market Beta / Correlation of the sector with the market

- - ▪ In the Bookscape example, where the market beta is 0.8558 and the median R-squared of the comparable publicly traded firms is 26.00%; the correlation with the market is 50.99%.

$$\frac{\text{Market Beta}}{\sqrt{R \text{ squared}}} = \frac{0.8558}{.5099} = 1.6783$$

- - - ▪ Total Cost of Equity =  $2.75 + 1.6783 (5.5\%) = 11.98\%$

- - - ▪ Note that the **market beta and the correlation come from publicly traded companies** in this space.

# **APPLICATION TEST: ESTIMATING A BOTTOM-UP BETA**

- ▪ Based upon the business or businesses that your firm is in right now, and its current financial leverage, estimate the bottom-up unlevered beta for your firm.
  
- ▪ Data Source: You can get a listing of unlevered betas by industry on my web site by going to updated data.

# FROM COST OF EQUITY TO COST OF CAPITAL

- ▪ The cost of capital is a composite cost to the firm of raising financing to fund its projects.
- ▪ In addition to equity, firms can raise capital from debt.
- ▪ To get to a cost of capital, you need to
  - ▪ Estimate a cost of debt
  - ▪ Estimate weights for debt and equity

# WHAT IS DEBT?

- ■ **General Rule:** Debt generally has the following characteristics:
  - ■ **Contractual commitment** to make fixed payments in the future
  - ■ The fixed payments are **tax deductible**
  - ■ Failure to make the payments can **lead to either default or loss of control** of the firm to the party to whom payments are due.
- ■ As a consequence, debt should include
  - ■ Any **interest-bearing liability**, whether short term or long term.
  - ■ Any **lease obligation**, whether operating or capital.

# ESTIMATING THE COST OF DEBT

- ▪ If the firm has bonds outstanding, and the bonds are traded, **the yield to maturity on a long-term, straight (no special features) bond** can be used as the interest rate.
- ▪ If the **firm is rated**, use the **rating and a typical default spread** on bonds with that rating to estimate the cost of debt.
- ▪ If the firm is not rated,
  - ▪ and it has **recently borrowed long term from a bank**, use the interest rate on the borrowing or
  - ▪ estimate a **synthetic rating for the company**, and use the synthetic rating to arrive at a default spread and a cost of debt
- ▪ The cost of debt has to be estimated in the same currency as the cost of equity and the cash flows in the valuation.

# THE EASY ROUTE: OUTSOURCING THE MEASUREMENT OF DEFAULT RISK

- ▪ For those firms that have bond ratings from global ratings agencies, I used those ratings:

| Company       | S&P Rating | Risk-Free Rate | Default Spread | Cost of Debt |
|---------------|------------|----------------|----------------|--------------|
| Disney        | A          | 2.75% (US \$)  | 1.00%          | 3.75%        |
| Deutsche Bank | A          | 1.75% (Euros)  | 1.00%          | 2.75%        |
| Vale          | A-         | 2.75% (US \$)  | 1.30%          | 4.05%        |

- ▪ If you want to estimate Vale's cost of debt in \$R terms, we can again use the differential inflation approach we used for the cost of equity:

$$\begin{aligned}
 \text{Cost of debt}_{\text{R$}} &= (1 + \text{Cost of debt}_{\text{US $}}) \frac{(1 + \text{Expected Inflation}_{\text{R$}})}{(1 + \text{Expected Inflation}_{\text{US $}})} - 1 \\
 &= (1.0405) = 11.19\% \frac{(1.09)}{(1.02)} - 1 = 11.19\%\%
 \end{aligned}$$

# A MORE GENERAL ROUTE: ESTIMATING SYNTHETIC RATINGS

- The **rating for a firm can be estimated using the financial characteristics of the firm**. In its simplest form, we can use just the interest coverage ratio:

$$\text{Interest Coverage Ratio} = \frac{\text{EBIT}}{\text{Interest Expenses}}$$

- For the non-financial service companies, we obtain the following:

| Company     | Operating income | Interest Expense | Interest coverage ratio |
|-------------|------------------|------------------|-------------------------|
| Disney      | \$10,023         | \$444            | 22.57                   |
| Vale        | \$15,667         | \$1,342          | 11.67                   |
| Tata Motors | Rs 166,605       | Rs 36,972        | 4.51                    |
| Baidu       | CY 11,193        | CY 472           | 23.72                   |
| Bookscape   | \$2,536          | \$492            | 5.16                    |

# INTEREST COVERAGE RATIOS, RATINGS AND DEFAULT SPREADS- NOVEMBER 2013

| <i>Large cap (&gt;\$ billion)</i> | <i>Small cap or risky (&lt;\$ billion)</i> | <i>Rating is (S&amp;P/ Moody's)</i> | <i>Spread (11/13)</i> |
|-----------------------------------|--------------------------------------------|-------------------------------------|-----------------------|
| >8.50                             | >12.5                                      | Aaa/AAA                             | 0.40%                 |
| 6.5-8.5                           | 9.5-12.5                                   | Aa2/AA                              | 0.70%                 |
| 5.5-6.5                           | 7.5-9.5                                    | A1/A+                               | 0.85%                 |
| 4.25-5.5                          | 6-7.5                                      | A2/A                                | 1.00%                 |
| 3-4.25                            | 4.5-6                                      | A3/A-                               | 1.30%                 |
| 2.5-3                             | 4-4.5                                      | Baa2/BBB                            | 2.00%                 |
| 2.25-2.5                          | 3.5-4                                      | Ba1/BB+                             | 3.00%                 |
| 2-2.25                            | 3-3.5                                      | Ba2/BB                              | 4.00%                 |
| 1.75-2.25                         | 2.5-3                                      | B1/B+                               | 5.50%                 |
| 1.5-1.75                          | 2-2.5                                      | B2/B                                | 6.50%                 |
| 1.25-1.5                          | 1.5-2                                      | B3/B-                               | 7.25%                 |
| 0.8-1.25                          | 1.25-1.5                                   | Caa/CCC                             | 8.75%                 |
| 0.65-0.8                          | 0.8-1.25                                   | Ca2/CC                              | 9.50%                 |
| 0.2-0.65                          | 0.5-0.8                                    | C2/C                                | 10.50%                |
| <0.2                              | <0.5                                       | D2/D                                | 12.00%                |

| Disney: Large cap, developed     | 22.57 | → | AAA |
|----------------------------------|-------|---|-----|
| Vale: Large cap, emerging        | 11.67 | → | AA  |
| Tata Motors: Large cap, Emerging | 4.51  | → | A-  |
| Baidu: Small cap, Emerging       | 23.72 | → | AAA |
| Bookscape: Small cap, private    | 5.16  | → | A-  |

# SYNTHETIC VERSUS ACTUAL RATINGS: RATED FIRMS

- ▪ **Disney's synthetic rating is AAA**, whereas its **actual rating is A**. The difference can be attributed to any of the following:
  - ▪ Synthetic ratings reflect only the interest coverage ratio whereas actual ratings incorporate all of the other ratios and qualitative factors
  - ▪ Synthetic ratings do not allow for sector-wide biases in ratings
  - ▪ Synthetic rating was based on 2013 operating income whereas actual rating reflects normalized earnings
- ▪ **Vale's synthetic rating is AA**, **but the actual rating for dollar debt is A-**. The biggest factor behind the difference is the presence of country risk, since Vale is probably being rated lower for being a Brazil-based corporation.
- ▪ **Deutsche Bank had an A rating**. We will not try to estimate a synthetic rating for the bank. Defining interest expenses on debt for a bank is difficult...

# ESTIMATING COST OF DEBT

- ▪ For Bookscape, we will use the synthetic rating (A-) to estimate the cost of debt:
  - ▪ Default Spread based upon A- rating = 1.30%
  - ▪ Pre-tax cost of debt = Riskfree Rate + Default Spread =  $2.75\% + 1.30\% = 4.05\%$
  - ▪ After-tax cost of debt = Pre-tax cost of debt (1- tax rate) =  $4.05\% (1-.40) = 2.43\%$
- ▪ For the three publicly traded firms that are rated in our sample, we will use the actual bond ratings to estimate the costs of debt.

| Company       | S&P Rating | Risk-Free Rate | Default Spread | Cost of Debt | Tax Rate | After-Tax Cost of Debt |
|---------------|------------|----------------|----------------|--------------|----------|------------------------|
| Disney        | A          | 2.75% (US \$)  | 1.00%          | 3.75%        | 36.1%    | 2.40%                  |
| Deutsche Bank | A          | 1.75% (Euros)  | 1.00%          | 2.75%        | 29.48%   | 1.94%                  |
| Vale          | A-         | 2.75% (US \$)  | 1.30%          | 4.05%        | 34%      | 2.67%                  |

- ▪ For Tata Motors, we have a rating of AA- from CRISIL, an Indian bond-rating firm, that measures only company risk. Using that rating:
  - ▪  $\text{Cost of debt}_{TMT} = \text{Risk free rate}_{Rupees} + \text{Default spread}_{India} + \text{Default spread}_{TMT}$
  - ▪  $= 6.57\% + 2.25\% + 0.70\% = 9.62\%$
  - ▪ After-tax cost of debt =  $9.62\% (1-.3245) = 6.50\%$

# DEFAULT SPREADS – JANUARY 2024

*Corporate Bond Default Spreads on January 1, 2025*

![](_page_96_Figure_257.jpeg)

# BUT SOME YEARS ARE VOLATILE: 2020 AS A CASE STUDY..

Corporate Bond Default Spreads: 2/14 - 11/1

![](_page_97_Figure_8.jpeg)

# APPLICATION TEST: ESTIMATING A COST OF DEBT

- ▪ Based upon your firm's current earnings before interest and taxes, its interest expenses, estimate
  - ▪ An interest coverage ratio for your firm
  - ▪ A synthetic rating for your firm (use the tables from prior pages)
  - ▪ A pre-tax cost of debt for your firm
  - ▪ An after-tax cost of debt for your firm

# COSTS OF HYBRIDS

- ▪ **Preferred stock** shares some of the characteristics of debt - the preferred dividend is pre-specified at the time of the issue and is paid out before common dividend -- and some of the characteristics of equity - the payments of preferred dividend are not tax deductible. If preferred stock is viewed as perpetual, the cost of preferred stock can be written as follows:
  - ▪  $k_{ps} = \text{Preferred Dividend per share} / \text{Market Price per preferred share}$
- ▪ **Convertible debt** is part debt (the bond part) and part equity (the conversion option). It is best to break it up into its component parts and eliminate it from the mix altogether.

# WEIGHTS FOR COST OF CAPITAL CALCULATION

- ■ The weights used in the cost of capital computation should be market values.
- ■ There are **three specious arguments** used against market value
  - ■ **Book value is more reliable than market value because it is not as volatile:** While it is true that book value does not change as much as market value, this is more a reflection of weakness than strength
  - ■ **Using book value rather than market value is a more conservative approach** to estimating debt ratios: For most companies, using book values will yield a lower cost of capital than using market value weights.
  - ■ **Since accounting returns are computed based upon book value, consistency requires the use of book value in computing cost of capital:** While it may seem consistent to use book values for both accounting return and cost of capital calculations, it does not make economic sense.

# DISNEY: FROM BOOK VALUE TO MARKET VALUE FOR INTEREST BEARING DEBT...

- In Disney's 2013 financial statements, the debt due over time was footnoted.

| Time due | Amount due | Weight | Weight *Maturity |
|----------|------------|--------|------------------|
| 0.5      | \$1,452    | 11.96% | 0.06             |
| 2        | \$1,300    | 10.71% | 0.21             |
| 3        | \$1,500    | 12.36% | 0.37             |
| 4        | \$2,650    | 21.83% | 0.87             |
| 6        | \$500      | 4.12%  | 0.25             |
| 8        | \$1,362    | 11.22% | 0.9              |
| 9        | \$1,400    | 11.53% | 1.04             |
| 19       | \$500      | 4.12%  | 0.78             |
| 26       | \$25       | 0.21%  | 0.05             |
| 28       | \$950      | 7.83%  | 2.19             |
| 29       | \$500      | 4.12%  | 1.19             |
|          | \$12,139   |        | 7.92             |

*The debt in this table does not add up to the book value of debt, because Disney does not break down the maturity of all of its debt.*

- Disney's total debt due, in book value terms, on the balance sheet is \$14,288 million and the total interest expense for the year was \$349 million. Using 3.75% as the pre-tax cost of debt:

$$\text{Estimated MV of Disney Debt} = 349 \left[ \frac{1}{(1.0375)^{7.92}} + \frac{14,288}{(1.0375)^{7.92}} \right] = \$13,028 \text{ million}$$

PV of annuity of \$349 million for 7.92 years

PV of face value of \$14,288 million in 7.92 years

# OPERATING LEASES AT DISNEY

- ▪ The “debt value” of operating leases is the present value of the lease payments, at a rate that reflects their risk, usually the pre-tax cost of debt.
- ▪ The pre-tax cost of debt at Disney is 3.75%.

| Year                 | Commitment | Present Value @3.75% |
|----------------------|------------|----------------------|
| 1                    | \$507.00   | \$488.67             |
| 2                    | \$422.00   | \$392.05             |
| 3                    | \$342.00   | \$306.24             |
| 4                    | \$272.00   | \$234.76             |
| 5                    | \$217.00   | \$180.52             |
| 6-10                 | \$356.80   | \$1,330.69           |
| Debt value of leases |            | \$2,932.93           |

Disney reported \$1,784 million in commitments after year 5. Given that their average commitment over the first 5 years, we assumed 5 years @ \$356.8 million each.

- ▪ Debt outstanding at Disney =  $\$13,028 + \$2,933 = \$15,961$  million

# ACCOUNTING COMES TO ITS SENSES ON OPERATING LEASES

- ■ In 2019, **both IFRS and GAAP made a major shift on operating leases**, requiring companies to capitalize leases and show the resulting debt (and counter asset) on the balance sheets.
- ■ That said, the accounting rules for capitalizing leases are far more complex than the simple calculations that I have used, for two reasons:
  - ■ Accounting has to balance its desire to **do the right thing with maintaining some connection to its legacy rules**.
  - ■ Companies have **lobbied to modify rules** in their sectors to cushion the impact.

# **APPLICATION TEST: ESTIMATING MARKET VALUE**

- ■ Estimate the
  - ■ Market value of equity at your firm and Book Value of equity
  - ■ Market value of debt and book value of debt (If you cannot find the average maturity of your debt, use 3 years): Remember to capitalize the value of operating leases and add them on to both the book value and the market value of debt.
- ■ Estimate the
  - ■ Weights for equity and debt based upon market value
  - ■ Weights for equity and debt based upon book value

# CURRENT COST OF CAPITAL: DISNEY

- ■ **Equity**

- ▪  $\text{Cost of Equity} = \text{Riskfree rate} + \text{Beta} * \text{Risk Premium}$   
   $= 2.75\% + 1.0013 (5.76\%) = 8.52\%$

- ▪ Market Value of Equity = \$121,878 million

- ▪  $\text{Equity}/(\text{Debt} + \text{Equity}) = 88.42\%$

- ■ **Debt**

- ▪  $\text{After-tax Cost of debt} = (\text{Riskfree rate} + \text{Default Spread}) (1-t)$

- ▪  $= (2.75\% + 1\%) (1 - .361) = 2.40\%$

- ▪ Market Value of Debt = \$13,028 + \$2933 = \$ 15,961 million

- ▪  $\text{Debt}/(\text{Debt} + \text{Equity}) = 11.58\%$

- ▪  $\text{Cost of Capital} = 8.52\% (.8842) + 2.40\% (.1158) = 7.81\%$

![](_page_105_Picture_97.jpeg)

$$121,878 / (121,878 + 15,961)$$

# DIVISIONAL COSTS OF CAPITAL: DISNEY AND VALE

## ■ Disney

|                   | Cost of equity | Cost of debt | Marginal tax rate | After-tax cost of debt | Debt ratio | Cost of capital |
|-------------------|----------------|--------------|-------------------|------------------------|------------|-----------------|
| Media Networks    | 9.07%          | 3.75%        | 36.10%            | 2.40%                  | 9.12%      | 8.46%           |
| Parks & Resorts   | 7.09%          | 3.75%        | 36.10%            | 2.40%                  | 10.24%     | 6.61%           |
| Studio            |                |              |                   |                        |            |                 |
| Entertainment     | 9.92%          | 3.75%        | 36.10%            | 2.40%                  | 17.16%     | 8.63%           |
| Consumer Products | 9.55%          | 3.75%        | 36.10%            | 2.40%                  | 53.94%     | 5.69%           |
| Interactive       | 11.65%         | 3.75%        | 36.10%            | 2.40%                  | 29.11%     | 8.96%           |
| Disney Operations | 8.52%          | 3.75%        | 36.10%            | 2.40%                  | 11.58%     | 7.81%           |

## ■ Vale

| <i>Business</i> | <i>Cost of equity</i> | <i>After-tax cost of debt</i> | <i>Debt ratio</i> | <i>Cost of capital (in US\$)</i> | <i>Cost of capital (in \$R)</i> |
|-----------------|-----------------------|-------------------------------|-------------------|----------------------------------|---------------------------------|
| Metals & Mining | 11.35%                | 2.67%                         | 35.48%            | 8.27%                            | 15.70%                          |
| Iron Ore        | 11.13%                | 2.67%                         | 35.48%            | 8.13%                            | 15.55%                          |
| Fertilizers     | 12.70%                | 2.67%                         | 35.48%            | 9.14%                            | 16.63%                          |
| Logistics       | 10.29%                | 2.67%                         | 35.48%            | 7.59%                            | 14.97%                          |
| Vale Operations | 11.23%                | 2.67%                         | 35.48%            | 8.20%                            | 15.62%                          |

# COSTS OF CAPITAL: TATA MOTORS, BAIDU AND BOOKSCAPE

- ▪ To estimate the costs of capital for Tata Motors in Indian rupees:
  - ▪ Cost of capital =  $14.49\% (1-.2928) + 6.50\% (.2928) = 12.15\%$
- ▪ For Baidu, we follow the same path to estimate a cost of equity in Chinese RMB:
  - ▪ Cost of capital =  $12.91\% (1-.0523) + 3.45\% (.0523) = 12.42\%$
- ▪ For Bookscape, the cost of capital is different depending on whether you look at market or total beta:

|             | Cost of equity | Pre-tax Cost of debt | After-tax cost of debt | D/(D+E) | Cost of capital |
|-------------|----------------|----------------------|------------------------|---------|-----------------|
| Market Beta | 7.46%          | 4.05%                | 2.43%                  | 17.63%  | 6.57%           |
| Total Beta  | 11.98%         | 4.05%                | 2.43%                  | 17.63%  | 10.30%          |

# APPLICATION TEST: ESTIMATING COST OF CAPITAL

- ▪ Using the bottom-up unlevered beta that you computed for your firm, and the values of debt and equity you have estimated for your firm, estimate a bottom-up levered beta and cost of equity for your firm.
- ▪ Based upon the costs of equity and debt that you have estimated, and the weights for each, estimate the cost of capital for your firm.
- ▪ How different would your cost of capital have been, if you used book value weights?

# CHOOSING A HURDLE RATE

- ▪ Either the cost of equity or the cost of capital can be used as a hurdle rate, **depending upon whether the returns measured are to equity investors or to all claimholders on the firm (capital)**
- ▪ If **returns are measured to equity investors**, the appropriate hurdle rate is the cost of equity.
- ▪ If **returns are measured to capital** (or the firm), the appropriate hurdle rate is the cost of capital.

# BACK TO FIRST PRINCIPLES

![](_page_110_Diagram_6.jpeg)