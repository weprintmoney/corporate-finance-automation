---
title: "Valsession4"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valfall16/valsession4.pdf
---

## Why do risk free rates vary across currencies? January 2016 Risk free rates

![](_page_0_Figure_2.jpeg)

# Risk free Rate: Don't have or trust the government bond rate?

1. 1. Build up approach: The risk free rate in any currency can be written as the sum of two variables:

Risk free rate = Expected Inflation in currency + Expected real interest rate

The expected real interest rate can be computed in one of two ways: from the US TIPs rate or set equal to real growth in the economy. Thus, if the expected inflation rate in a country is expected to be 15% and the TIPs rate is 1%, the risk free rate is 16%.

1. 2. US \$ Rate & Differential Inflation: Alternatively, you can scale up the US \$ risk free rate by the differential inflation between the US \$ and the currency in question:

$$\text{Risk free rate}_{\text{Currency}} = \frac{(1 + \text{Risk free rate}_{\text{US \$}}) \frac{(1 + \text{Expected Inflation}_{\text{Foreign currency}})}{(1 + \text{Expected Inflation}_{\text{US \$}})} - 1$$

Thus, if the US \$ risk free rate is 2.00%, the inflation rate in the foreign currency is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

$$\text{Risk free rate} = \frac{(1.02) \frac{(1.15)}{(1.015)} - 1}{(1.015)} = 15.57\%$$

# One more test on riskfree rates…

- ¨ On January 1, 2016, the 10-year treasury bond rate in the United States was 2.27%, a historic low. Assume that you were valuing a company in US dollars then, but were wary about the risk free rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate
  - c. Something else…

# Some perspective on risk free rates

![](_page_3_Figure_2.jpeg)

# Negative Interest Rates?

¨ In 2016, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates? ¨ How negative can rates get? (Is there a bound?) ¨ Would you use these negative interest rates as risk free rates? ¤ If no, why not and what would you do instead? ¤ If yes, what else would you have to do in your valuation to be internally consistent?

44

# Discount Rates: II

## The Equity Risk Premium

# The ubiquitous historical risk premium

¨ The historical premium is the premium that stocks have historically earned over riskless securities. ¨ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to ¤ How far back you go in history… ¤ Whether you use T.bill rates or T.Bond rates ¤ Whether you use geometric or arithmetic averages. ¨ For instance, looking at the US:

|           | <i>Arithmetic Average</i> | <i>Geometric Average</i> |                   |                   |
|-----------|---------------------------|--------------------------|-------------------|-------------------|
|           | Stocks - T. Bills         | Stocks - T. Bonds        | Stocks - T. Bills | Stocks - T. Bonds |
| 1928-2015 | 7.92%                     | 6.18%                    | 6.05%             | 4.54%             |
| Std Error | <i><b>2.15%</b></i>       | <i><b>2.29%</b></i>      |                   |                   |
| 1966-2015 | 6.05%                     | 3.89%                    | 4.69%             | 2.90%             |
| Std Error | <i><b>2.42%</b></i>       | <i><b>2.74%</b></i>      |                   |                   |
| 2006-2015 | 7.87%                     | 3.88%                    | 6.11%             | 2.53%             |
| Std Error | <i><b>6.06%</b></i>       | <i><b>8.66%</b></i>      |                   |                   |

# The perils of trusting the past.....

46

- □ Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 80 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

Standard Error in Premium =  $20\%/\sqrt{80} = 2.26\%$ 

- □ Survivorship Bias: Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

## Risk Premium for a Mature Market? Broadening the sample to 1900-2015

| Country       | Geometric	ERP | Arithmetic	ERP | Standard	Error |
|---------------|---------------|----------------|----------------|
| Australia     | 5.00%         | 6.60%          | 1.70%          |
| Austria       | 2.60%         | 21.50%         | 14.30%         |
| Belgium       | 2.40%         | 4.50%          | 2.00%          |
| Canada        | 3.30%         | 4.90%          | 1.70%          |
| Denmark       | 2.30%         | 3.80%          | 1.70%          |
| Finland       | 5.20%         | 8.80%          | 2.80%          |
| France        | 3.00%         | 5.40%          | 2.10%          |
| Germany       | 5.10%         | 9.10%          | 2.70%          |
| Ireland       | 2.80%         | 4.80%          | 1.80%          |
| Italy         | 3.10%         | 6.50%          | 2.70%          |
| Japan         | 5.10%         | 9.10%          | 3.00%          |
| Netherlands   | 3.30%         | 5.60%          | 2.10%          |
| New Zealand   | 4.00%         | 5.50%          | 1.70%          |
| Norway        | 2.30%         | 5.20%          | 2.60%          |
| South Africa  | 5.40%         | 7.20%          | 1.80%          |
| Spain         | 1.80%         | 3.80%          | 1.90%          |
| Sweden        | 3.10%         | 5.40%          | 2.00%          |
| Switzerland   | 2.10%         | 3.60%          | 1.60%          |
| U.K.          | 3.60%         | 5.00%          | 1.60%          |
| U.S.          | 4.30%         | 6.40%          | 1.90%          |
| Europe        | 3.20%         | 4.50%          | 1.50%          |
| World-ex U.S. | 2.80%         | 3.90%          | 1.40%          |
| World         | 3.20%         | 4.40%          | 1.40%          |

# The simplest way of estimating an additional country risk premium: The country default spread

- ❑ Default spread for country: In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - ❑ The default spread on a dollar denominated bond issued by the country. (In January 2016, that spread was 4.83% for the Brazilian \$ bond)
  - ❑ The sovereign CDS spread for the country. In January 2016, the ten year CDS spread for Brazil, adjusted for the US CDS, was 5.19%.
  - ❑ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Baa3 and the default spread for a Baa3 rated sovereign was about 2.44% in January 2016.
- ❑ Add the default spread to a "mature" market premium: This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 6.00%.
  - ❑ Country Risk Premium for Brazil = 2.44%
  - ❑ Total ERP for Brazil = 6.00% + 2.44% = 8.44%

## An equity volatility based approach to estimating the country total ERP

- ❑ This approach draws on the standard deviation of two equity markets, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ❑  $\text{Total equity risk premium} = \text{Risk Premium}_{\text{US}}^* \sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$
- ❑ The country equity risk premium is based upon the volatility of the market in question relative to U.S market.
  - ❑ Assume that the equity risk premium for the US is 6.00%.
  - ❑ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ❑  $\text{Total Equity Risk Premium for Brazil} = 6.00\% (30\%/18\%) = 10.0\%$
  - ❑  $\text{Country equity risk premium for Brazil} = 10.00\% - 6.00\% = 4.00\%$

— 49 —

## A melded approach to estimating the additional country risk premium

- ❑ Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
- ❑ Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. Using this approach for Brazil in January 2016, you would get:
  - ❑ Country Equity risk premium = Default spread on country bond\*  $\sigma_{\text{Country}}$   
     $\text{Equity} / \sigma_{\text{Country}} \text{ Bond}$ 
    - ■ Standard Deviation in Bovespa (Equity) = 30%
    - ■ Standard Deviation in Brazil government bond = 20%
    - ■ Default spread for Brazil= 2.44%
  - ❑ Brazil Country Risk Premium =  $2.44\% (30\%/20\%) = 3.66\%$
  - ❑ Brazil Total ERP = Mature Market Premium + CRP =  $6.00\% + 3.66\% = 9.66\%$

# A Template for Country Risk

![](_page_12_Diagram_3.jpeg)

*Black #: Total ERP*

*Red #: Country risk premium*

| <i>Strong frontier (not rated)</i> |      |       |      |                 |      |       |       |
|------------------------------------|------|-------|------|-----------------|------|-------|-------|
| Algeria                            | 63.0 | 12.1% | 6.7% | Malawi          | 57.0 | 17.1% | 11.7% |
| Brunei                             | 72.8 | 8.4%  | 2.8% | Mali            | 62.5 | 12.1% | 6.7%  |
| Gambia                             | 62.0 | 14.2% | 6.2% | Myanmar         | 63.3 | 12.1% | 6.7%  |
| Guinea                             | 53.8 | 17.1% | 6.7% | Niger           | 51.0 | 17.1% | 11.7% |
| Guinea-Bissau                      | 62.3 | 12.1% | 6.7% | Siria Leone     | 56.5 | 17.1% | 11.7% |
| Guyana                             | 63.5 | 12.1% | 6.7% | Somalia         | 42.5 | 20.9% | 11.9% |
| Haiti                              | 57.0 | 17.1% | 6.7% | Sudan           | 62.5 | 20.9% | 11.9% |
| Iran                               | 67.8 | 10.4% | 4.8% | Syria           | 63.0 | 12.1% | 6.7%  |
| Iraq                               | 56.0 | 17.1% | 6.7% | Tanzania        | 63.0 | 12.1% | 6.7%  |
| Korea, D.P.R.                      | 56.0 | 17.1% | 6.7% | Togo            | 50.3 | 17.1% | 6.7%  |
| Liberia                            | 50.5 | 17.1% | 6.7% | Yemen, Republic | 50.3 | 17.1% | 6.7%  |
| Libya                              | 52.8 | 17.1% | 6.7% | Zimbabwe        | 62.5 | 17.1% | 6.7%  |
| Madagascar                         | 61.3 | 14.2% | 6.2% |                 |      |       |       |

| <span></span> | Bangladesh       | 11.37%       | <b>5.37%</b>        |
|---------------|------------------|--------------|---------------------|
| <span></span> | Cambodia         | 14.20%       | <b>8.20%</b>        |
| <span></span> | China            | 6.90%        | <b>0.90%</b>        |
| <span></span> | Fiji             | 12.71%       | <b>6.71%</b>        |
| <span></span> | Hong Kong        | 6.59%        | <b>0.59%</b>        |
| <span></span> | India            | 9.28%        | <b>3.28%</b>        |
| <span></span> | Indonesia        | 9.28%        | <b>3.28%</b>        |
| <span></span> | Japan            | 7.05%        | <b>1.05%</b>        |
| <span></span> | Korea            | 6.74%        | <b>0.74%</b>        |
| <span></span> | Macao            | 6.74%        | <b>0.74%</b>        |
| <span></span> | Malaysia         | 7.79%        | <b>1.79%</b>        |
| <span></span> | Mauritius        | 8.38%        | <b>2.38%</b>        |
| <span></span> | Mongolia         | 14.20%       | <b>8.20%</b>        |
| <span></span> | Pakistan         | 15.70%       | <b>9.70%</b>        |
| <span></span> | Papua New Guinea | 12.71%       | <b>6.71%</b>        |
| <span></span> | Philippines      | 8.84%        | <b>2.84%</b>        |
| <span></span> | Singapore        | 6.00%        | <b>0.00%</b>        |
| <span></span> | Sri Lanka        | 12.71%       | <b>6.71%</b>        |
| <span></span> | Taiwan           | 6.90%        | <b>0.90%</b>        |
| <span></span> | Thailand         | 8.38%        | <b>2.38%</b>        |
| <span></span> | Vietnam          | 12.71%       | <b>6.71%</b>        |
| <span></span> | <b>Asia</b>      | <b>7.49%</b> | <b><b>1.49%</b></b> |

| <b>Australia</b>          | 6.00%        | <b>0.09%</b> |
|---------------------------|--------------|--------------|
| Cook Islands              | 12.71%       | <b>6.71%</b> |
| New Zealand               | 6.00%        | <b>0.00%</b> |
| <b>Australia &amp; NZ</b> | <b>6.00%</b> | <b>0.00%</b> |

| Andorra     | 9.28%  | <b>3.28%</b>  | Jersey (States of)    | 6.59%        | <b>0.59%</b> |
|-------------|--------|---------------|-----------------------|--------------|--------------|
| Austria     | 6.00%  | <b>0.00%</b>  | Liechtenstein         | 6.00%        | <b>0.00%</b> |
| Belgium     | 6.90%  | <b>0.90%</b>  | Luxembourg            | 6.00%        | <b>0.00%</b> |
| Cyprus      | 12.71% | <b>6.71%</b>  | Malta                 | 7.79%        | <b>1.79%</b> |
| Denmark     | 6.00%  | <b>0.00%</b>  | Netherlands           | 6.00%        | <b>0.00%</b> |
| Finland     | 6.00%  | <b>0.00%</b>  | Norway                | 6.00%        | <b>0.00%</b> |
| France      | 6.74%  | <b>0.74%</b>  | Portugal              | 9.72%        | <b>3.72%</b> |
| Germany     | 6.00%  | <b>0.00%</b>  | Spain                 | 8.84%        | <b>2.84%</b> |
| Greece      | 20.90% | <b>14.90%</b> | Sweden                | 6.00%        | <b>0.00%</b> |
| Guernsey    | 6.59%  | <b>0.59%</b>  | Switzerland           | 6.00%        | <b>0.00%</b> |
| Iceland     | 8.84%  | <b>2.84%</b>  | Turkey                | 9.28%        | <b>3.28%</b> |
| Ireland     | 8.38%  | <b>2.38%</b>  | United Kingdom        | 6.59%        | <b>0.59%</b> |
| Isle of Man | 6.59%  | <b>0.59%</b>  | <b>Western Europe</b> | <b>7.16%</b> | <b>1.16%</b> |
| Italy       | 8.84%  | <b>2.84%</b>  |                       |              |              |

| Canada               | 6.00%         | <b>0.00%</b>  |
|----------------------|---------------|---------------|
| US                   | 6.00%         | <b>0.00%</b>  |
| <b>North America</b> | <b>6.00%</b>  | <b>0.00%</b>  |
| <b>Caribbean</b>     | <b>14.61%</b> | <b>8.61%</b>  |
| Argentina            | 17.17%        | <b>11.17%</b> |
| Belize               | 19.42%        | <b>13.42%</b> |
| Bolivia              | 11.37%        | <b>5.37%</b>  |
| Brazil               | 9.28%         | <b>3.28%</b>  |
| Chile                | 6.90%         | <b>0.90%</b>  |
| Colombia             | 8.84%         | <b>2.84%</b>  |
| Costa Rica           | 9.72%         | <b>3.72%</b>  |
| Ecuador              | 15.70%        | <b>9.70%</b>  |
| El Salvador          | 11.37%        | <b>5.37%</b>  |
| Guatemala            | 9.72%         | <b>3.72%</b>  |
| Honduras             | 15.70%        | <b>9.70%</b>  |
| Mexico               | 7.79%         | <b>1.79%</b>  |
| Nicaragua            | 14.20%        | <b>8.20%</b>  |
| Panama               | 8.84%         | <b>2.84%</b>  |
| Paraguay             | 9.72%         | <b>3.72%</b>  |
| Peru                 | 7.79%         | <b>1.79%</b>  |
| Suriname             | 11.37%        | <b>5.37%</b>  |
| Uruguay              | 8.84%         | <b>2.84%</b>  |
| Venezuela            | 20.90%        | <b>14.90%</b> |
| <b>Latin America</b> | <b>10.42%</b> | <b>4.42%</b>  |

| <i>Country</i>   | <i>ERP</i>    | <i>CRP</i>          |
|------------------|---------------|---------------------|
| Angola           | 10.48%        | <b>4.48%</b>        |
| Botswana         | 7.26%         | <b>1.26%</b>        |
| Burkina Faso     | 15.70%        | <b>9.70%</b>        |
| Cameroon         | 14.20%        | <b>8.20%</b>        |
| Cape Verde       | 14.20%        | <b>8.20%</b>        |
| Congo (DR        | 15.70%        | <b>9.70%</b>        |
| Congo (Republic) | 11.37%        | <b>5.37%</b>        |
| Côte d'Ivoire    | 11.37%        | <b>5.37%</b>        |
| Egypt            | 15.70%        | <b>9.70%</b>        |
| Ethiopia         | 12.71%        | <b>6.71%</b>        |
| Gabon            | 11.37%        | <b>5.37%</b>        |
| Ghana            | 15.70%        | <b>9.70%</b>        |
| Kenya            | 12.71%        | <b>6.71%</b>        |
| Morocco          | 9.72%         | <b>3.72%</b>        |
| Mozambique       | 14.20%        | <b>8.20%</b>        |
| Namibia          | 9.28%         | <b>3.28%</b>        |
| Nigeria          | 11.37%        | <b>5.37%</b>        |
| Rwanda           | 12.71%        | <b>6.71%</b>        |
| Senegal          | 12.71%        | <b>6.71%</b>        |
| South Africa     | 8.84%         | <b>2.84%</b>        |
| Tunisia          | 11.37%        | <b>5.37%</b>        |
| Uganda           | 12.71%        | <b>6.71%</b>        |
| Zambia           | 14.20%        | <b>8.20%</b>        |
| <b>Africa</b>    | <b>11.76%</b> | <b><b>5.76%</b></b> |

| Albania                            | 11.71%       | 6.71%        |
|------------------------------------|--------------|--------------|
| Armenia                            | 11.37%       | 5.37%        |
| Azerbaijan                         | 9.28%        | 3.28%        |
| Belarus                            | 17.17%       | 11.17%       |
| Bosnia                             | 15.70%       | 9.70%        |
| Bulgaria                           | 8.84%        | 2.84%        |
| Croatia                            | 9.72%        | 3.72%        |
| Czech Republic                     | 7.05%        | 1.05%        |
| Estonia                            | 7.05%        | 1.05%        |
| Georgia                            | 11.37%       | 5.37%        |
| Hungary                            | 9.72%        | 3.72%        |
| Kazakhstan                         | 8.84%        | 2.84%        |
| Latvia                             | 7.79%        | 1.79%        |
| Lithuania                          | 7.79%        | 1.79%        |
| Macedonia                          | 11.37%       | 5.37%        |
| Moldova                            | 15.70%       | 9.70%        |
| Montenegro                         | 11.37%       | 5.37%        |
| Poland                             | 7.26%        | 1.26%        |
| Romania                            | 9.28%        | 3.28%        |
| Russia                             | 9.72%        | 3.72%        |
| Serbia                             | 12.71%       | 6.71%        |
| Slovakia                           | 7.26%        | 1.26%        |
| Slovenia                           | 9.28%        | 3.28%        |
| Ukraine                            | 20.90%       | 14.90%       |
| <b>Eastern Europe &amp; Russia</b> | <b>9.65%</b> | <b>3.65%</b> |

| <span> </span> | <span> </span> Abu Dhabi            | <span> </span> 6.74%        | <span> </span> 0.74%        |
|----------------|-------------------------------------|-----------------------------|-----------------------------|
| <span> </span> | <span> </span> Bahrain              | <span> </span> 9.28%        | <span> </span> 3.28%        |
| <span> </span> | <span> </span> Israel               | <span> </span> 7.05%        | <span> </span> 1.05%        |
| <span> </span> | <span> </span> Jordan               | <span> </span> 12.71%       | <span> </span> 6.71%        |
| <span> </span> | <span> </span> Kuwait               | <span> </span> 6.74%        | <span> </span> 0.74%        |
| <span> </span> | <span> </span> Lebanon              | <span> </span> 14.20%       | <span> </span> 8.20%        |
| <span> </span> | <span> </span> Oman                 | <span> </span> 7.05%        | <span> </span> 1.05%        |
| <span> </span> | <span> </span> Qatar                | <span> </span> 6.74%        | <span> </span> 0.74%        |
| <span> </span> | <span> </span> Ras Al Khaimah       | <span> </span> 7.26%        | <span> </span> 1.26%        |
| <span> </span> | <span> </span> Saudi Arabia         | <span> </span> 6.90%        | <span> </span> 0.90%        |
| <span> </span> | <span> </span> Sharjah              | <span> </span> 7.79%        | <span> </span> 1.79%        |
| <span> </span> | <span> </span> United Arab Emirates | <span> </span> 6.74%        | <span> </span> 0.74%        |
| <span> </span> | <span> </span> Middle East          | <span> </span> <b>7.11%</b> | <span> </span> <b>1.11%</b> |

## From Country Equity Risk Premiums to Corporate Equity Risk premiums

¨ Approach 1: Assume that every company in the country is equally exposed to country risk. In this case, ¤ E(Return) = Riskfree Rate + CRP + Beta (Mature ERP) ¤ Implicitly, this is what you are assuming when you use the local Government' s dollar borrowing rate as your riskfree rate. ¨ Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk. ¤ E(Return) = Riskfree Rate + Beta (Mature ERP+ CRP) ¨ Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales) ¤ E(Return)=Riskfree Rate+ b (Mature ERP) + l (CRP)

Mature ERP = Mature market Equity Risk Premium

CRP = Additional country risk premium

## Approaches 1 & 2: Estimating country risk premium exposure

¨ Location based CRP: The standard approach in valuation is to attach a country risk premium to a company based upon its country of incorporation. Thus, if you are an Indian company, you are assumed to be exposed to the Indian country risk premium. A developed market company is assumed to be unexposed to emerging market risk. ¨ Operation-based CRP: There is a more reasonable modified version. The country risk premium for a company can be computed as a weighted average of the country risk premiums of the countries that it does business in, with the weights based upon revenues or operating income. If a company is exposed to risk in dozens of countries, you can take a weighted average of the risk premiums by region.

## Operation based CRP: Single versus Multiple Emerging Markets

¨ Single emerging market: Embraer, in 2004, reported that it derived 3% of its revenues in Brazil and the balance from mature markets. The mature market ERP in 2004 was 5% and Brazil's CRP was 7.89%.

| <span> </span>              | Revenues | Total ERP    | CRP          |
|-----------------------------|----------|--------------|--------------|
| US and other mature markets | 97%      | 5.00%        | 0.00%        |
| Brazil                      | 3%       | 12.89%       | 8%           |
| <b>Embraer</b>              |          | <b>5.24%</b> | <b>0.24%</b> |

¨ Multiple emerging markets: Ambev, the Brazilian-based beverage company, reported revenues from the following countries during 2011. 

|           | Revenues | %      | Total ERP    | CRP          |
|-----------|----------|--------|--------------|--------------|
| Argentina | 19       | 9.31%  | 15.00%       | 9.00%        |
| Bolivia   | 4        | 1.96%  | 10.88%       | 4.88%        |
| Brazil    | 130      | 63.73% | 8.63%        | 2.63%        |
| Canada    | 23       | 11.27% | 6.00%        | 0.00%        |
| Chile     | 7        | 3.43%  | 7.05%        | 1.05%        |
| Ecuador   | 6        | 2.94%  | 12.75%       | 6.75%        |
| Paraguay  | 3        | 1.47%  | 12.00%       | 6.00%        |
| Peru      | 12       | 5.88%  | 9.00%        | 3.00%        |
| Ambev     | 204      |        | <b>9.11%</b> | <b>3.11%</b> |

### Extending to a multinational: Regional breakdown Coca Cola's revenue breakdown and ERP in 2012

Things to watch out for

- 1. Aggregation across regions. For instance, the Pacific region often includes Australia & NZ with Asia
- 2. Obscure aggregations including Eurasia and Oceania

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