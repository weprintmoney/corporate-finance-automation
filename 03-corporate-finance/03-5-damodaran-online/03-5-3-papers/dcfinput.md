---
title: "Dcfinput"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/dcfinput.pdf
---

![]()Aswath Damodaran

#### The Key Inputs in DCF Valuation

- <sup>l</sup> Discount Rate
  - Cost of Equity, in valuing equity
- Cost of Capital, in valuing the firm <sup>l</sup> Cash Flows
  - Cash Flows to Equity
- Cash Flows to Firm <sup>l</sup> Growth (to get future cash flows)
  - Growth in Equity Earnings
  - Growth in Firm Earnings (Operating Income)

# I. Estimating Discount Rates

DCF Valuation

# Estimating Inputs: Discount Rates

- <sup>l</sup> **Critical ingredient** in discounted cashflow valuation. Errors in estimating the discount rate or mismatching cashflows and discount rates can lead to serious errors in valuation. <sup>l</sup> At an intuitive level, the discount rate used should be consistent with both the **riskiness** and the **type of cashflow** being discounted.
  - Equity versus Firm: If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital.
  - Currency: The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated.
  - Nominal versus Real: If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

# I. Cost of Equity

- <sup>l</sup> The cost of equity is the rate of return that investors require to make an equity investment in a firm. There are two approaches to estimating the cost of equity;
  - a dividend-growth model.
- a risk and return model <sup>l</sup> The dividend growth model (which specifies the cost of equity to be the sum of the dividend yield and the expected growth in earnings) is based upon the premise that the current price is equal to the value. It cannot be used in valuation, if the objective is to find out if an asset is correctly valued. <sup>l</sup> A risk and return model, on the other hand, tries to answer two questions:
  - How do you measure risk?
  - How do you translate this risk measure into a risk premium?

# What is Risk?

<sup>l</sup> Risk, in traditional terms, is viewed as a 'negative'. Webster's dictionary, for instance, defines risk as "exposing to danger or hazard". The Chinese symbols for risk are reproduced below:

![](_page_5_Picture_2.jpeg)

<sup>l</sup> The first symbol is the symbol for "danger", while the second is the symbol for "opportunity", making risk a mix of danger and opportunity.

#### Risk and Return Models

**The risk in an investment can be measured by the variance in actual returns around an expected return**

![](_page_6_Figure_3.jpeg)

*Risk that is specific to investment (Firm Specific) Risk that affects all investments (Market Risk)*

Can be diversified away in a diversified portfolio Cannot be diversified away since most assets

1. each investment is a small proportion of portfolio are affected by it.

2. risk averages out across investments in portfolio

**The marginal investor is assumed to hold a "diversified" portfolio. Thus, only market risk will be rewarded and priced.**

| <b>The CAPM</b>                                                                                                                                                                                                                                                                   | <b>The APM</b>                                                                                                                                                                                                                      | <b>Multi-Factor Models</b>                                                                                                                                                           | <b>Proxy Models</b>                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <p>If there is</p> <ol> <li>no private information</li> <li>no transactions cost</li> </ol> the optimal diversified portfolio includes every traded asset. Everyone will hold this market portfolio<br><b>Market Risk = Risk added by any investment to the market portfolio:</b> | <p>If there are no arbitrage opportunities then the market risk of any asset must be captured by betas relative to factors that affect all investments.<br/> <b>Market Risk = Risk exposures of any asset to market factors</b></p> | <p>Since market risk affects most or all investments, it must come from macro economic factors.<br/> <b>Market Risk = Risk exposures of any asset to macro economic factors.</b></p> | <p>In an efficient market, differences in returns across long periods must be due to market risk differences. Looking for variables correlated with returns should then give us proxies for this risk.<br/> <b>Market Risk = Captured by the Proxy Variable(s)</b></p> |
| <p>Beta of asset relative to Market portfolio (from a regression)</p>                                                                                                                                                                                                             | <p>Betas of asset relative to unspecified market factors (from a factor analysis)</p>                                                                                                                                               | <p>Betas of assets relative to specified macro economic factors (from a regression)</p>                                                                                              | <p>Equation relating returns to proxy variables (from a regression)</p>                                                                                                                                                                                                |

**Step 1: Defining Risk**

**Step 2: Differentiating between Rewarded and Unrewarded Risk**

**Step 3: Measuring Market Risk**

# Comparing Risk Models

| Model  | Expected Return                        | Inputs Needed                   |
|--------|----------------------------------------|---------------------------------|
| CAPM   | E(R) = R f + b (R m - R f )            | Riskfree Rate                   |
| APM    | E(R) = R f + S j=1 b j (R j - R f )    | Riskfree Rate; # of Factors;    |
| Multi  | E(R) = R f + S j=1,,N b j (R j - R f ) | Riskfree Rate; Macro factors    |
| factor |                                        | Betas relative to macro factors |
| Proxy  | E(R) = a + S j=1..N b j Y j            | Proxies                         |

#### Beta's Properties

- Betas are standardized around one.

- If

 $\beta = 1$  ... Average risk investment

 $\beta > 1$  ... Above Average risk investment

 $\beta < 1$  ... Below Average risk investment

 $\beta = 0$  ... Riskless investment

- The average beta across all investments is one.

# Limitations of the CAPM

- <sup>l</sup> 1. The model makes unrealistic assumptions <sup>l</sup> 2. The parameters of the model cannot be estimated precisely
  - - Definition of a market index
- - Firm may have changed during the 'estimation' period' <sup>l</sup> 3. The model does not work well
  - - If the model is right, there should be <sup>l</sup> \* a linear relationship between returns and betas <sup>l</sup> \* the only variable that should explain returns is betas
  - - The reality is that <sup>l</sup> \* the relationship between betas and returns is weak <sup>l</sup> \* Other variables (size, price/book value) seem to explain differences in returns better.

#### Inputs required to use the CAPM -

- (a) the current risk-free rate
- (b) the expected return on the market index and
- (c) the beta of the asset being analyzed.

# Riskfree Rate in Valuation

<sup>l</sup> The correct risk free rate to use in a risk and return model is <sup>o</sup> a short-term Government Security rate (eg. T.Bill), since it has no default risk or price risk <sup>o</sup> a long-term Government Security rate, since it has no default risk <sup>o</sup> other: specify ->

# The Riskfree Rate

- <sup>l</sup> On a riskfree asset, the actual return is equal to the expected return. <sup>l</sup> Therefore, there is no variance around the expected return. <sup>l</sup> For an investment to be riskfree, i.e., to have an actual return be equal to the expected return, two conditions have to be met –
  - There has to be no default risk, which generally implies that the security has to be issued by the government. Note, however, that not all governments can be viewed as default free.
  - There can be no uncertainty about reinvestment rates, which implies that it is a zero coupon security with the same maturity as the cash flow being analyzed.

# Riskfree Rate in Practice

<sup>l</sup> The riskfree rate is the rate on a zero coupon government bond matching the time horizon of the cash flow being analyzed. <sup>l</sup> Theoretically, this translates into using different riskfree rates for each cash flow - the 1 year zero coupon rate for the cash flow in year 2, the 2-year zero coupon rate for the cash flow in year 2 ... <sup>l</sup> Practically speaking, if there is substantial uncertainty about expected cash flows, the present value effect of using time varying riskfree rates is small enough that it may not be worth it.

# The Bottom Line on Riskfree Rates

- <sup>l</sup> Using a long term government rate (even on a coupon bond) as the riskfree rate on all of the cash flows in a long term analysis will yield a close approximation of the true value. <sup>l</sup> For short term analysis, it is entirely appropriate to use a short term government security rate as the riskfree rate. <sup>l</sup> If the analysis is being done in real terms (rather than nominal terms) use a real riskfree rate, which can be obtained in one of two ways –
  - from an inflation-indexed government bond, if one exists
  - set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done.

# Riskfree Rate in Valuation

<sup>l</sup> You are valuing a Brazilian company in nominal U.S. dollars. The correct riskfree rate to use in this valuation is: <sup>o</sup> the U.S. treasury bond rate <sup>o</sup> the Brazilian C-Bond rate (the rate on dollar denominated Brazilian long term debt) <sup>o</sup> the local riskless Brazilian Real rate (in nominal terms) <sup>o</sup> the real riskless Brazilian Real rate

# Measurement of the risk premium

- <sup>l</sup> The risk premium is the premium that investors demand for investing in an average risk investment, relative to the riskfree rate. <sup>l</sup> As a general proposition, this premium should be
  - greater than zero
  - increase with the risk aversion of the investors in that market
  - increase with the riskiness of the "average" risk investment

# Risk Aversion and Risk Premiums

<sup>l</sup> If this were the capital market line, the risk premium would be a weighted average of the risk premiums demanded by each and every investor. <sup>l</sup> The weights will be determined by the magnitude of wealth that each investor has. Thus, Warren Bufffet's risk aversion counts more towards determining the "equilibrium" premium than yours' and mine. <sup>l</sup> As investors become more risk averse, you would expect the "equilibrium" premium to increase.

# Estimating Risk Premiums in Practice

<sup>l</sup> Survey investors on their desired risk premiums and use the average premium from these surveys. <sup>l</sup> Assume that the actual premium delivered over long time periods is equal to the expected premium - i.e., use historical data <sup>l</sup> Estimate the implied premium in today's asset prices.

#### The Survey Approach

- <sup>l</sup> Surveying all investors in a market place is impractical. <sup>l</sup> However, you can survey a few investors (especially the larger investors) and use these results. In practice, this translates into surveys of money managers' expectations of expected returns on stocks over the next year. <sup>l</sup> The limitations of this approach are:
  - there are no constraints on reasonability (the survey could produce negative risk premiums or risk premiums of 50%)
  - they are extremely volatile
  - they tend to be short term; even the longest surveys do not go beyond one year

# The Historical Premium Approach

- <sup>l</sup> This is the default approach used by most to arrive at the premium to use in the model <sup>l</sup> In most cases, this approach does the following
  - it defines a time period for the estimation (1926-Present, 1962-Present....)
  - it calculates average returns on a stock index during the period
    - it calculates average returns on a riskless security over the period
      - it calculates the difference between the two
- and uses it as a premium looking forward <sup>l</sup> The limitations of this approach are:
  - it assumes that the risk aversion of investors has not changed in a systematic way across time. (The risk aversion may change from year to year, but it reverts back to historical averages)
  - it assumes that the riskiness of the "risky" portfolio (stock index) has not changed in a systematic way across time.

# Historical Average Premiums for the United States

Historical period Stocks - T.Bills Stocks - T.Bonds

| Arith  | Geom  | Arith | Geom  |
|--------|-------|-------|-------|
| 8.76%  | 6.95% | 7.57% | 5.91% |
| 5.74%  | 4.63% | 5.16% | 4.46% |
| 10.34% | 9.72% | 9.22% | 8.02% |

|           | Arith  | Geom  | Arith | Geom  |
|-----------|--------|-------|-------|-------|
| 1926-1996 | 8.76%  | 6.95% | 7.57% | 5.91% |
| 1962-1996 | 5.74%  | 4.63% | 5.16% | 4.46% |
| 1981-1996 | 10.34% | 9.72% | 9.22% | 8.02% |

What is the right premium?

# What about historical premiums for other markets?

<sup>l</sup> Historical data for markets outside the United States tends to be sketch and unreliable. <sup>l</sup> Ibbotson, for instance, estimates the following premiums for major markets from 1970-1990

| Country     | Period  | Stocks | Bonds | Risk Premium |
|-------------|---------|--------|-------|--------------|
| Australia   | 1970-90 | 9.60%  | 7.35% | 2.25%        |
| Canada      | 1970-90 | 10.50% | 7.41% | 3.09%        |
| France      | 1970-90 | 11.90% | 7.68% | 4.22%        |
| Germany     | 1970-90 | 7.40%  | 6.81% | 0.59%        |
| Italy       | 1970-90 | 9.40%  | 9.06% | 0.34%        |
| Japan       | 1970-90 | 13.70% | 6.96% | 6.74%        |
| Netherlands | 1970-90 | 11.20% | 6.87% | 4.33%        |
| Switzerland | 1970-90 | 5.30%  | 4.10% | 1.20%        |
| UK          | 1970-90 | 14.70% | 8.45% | 6.25%        |

# Risk Premiums for Latin America

| Country   | Rating | Risk Premium         |
|-----------|--------|----------------------|
| Argentina | BBB    | 5.5% + 1.75% = 7.25% |
| Brazil    | BB     | 5.5% + 2% = 7.5%     |
| Chile     | AA     | 5.5% + 0.75% = 6.25% |
| Columbia  | A+     | 5.5% + 1.25% = 6.75% |
| Mexico    | BBB+   | 5.5% + 1.5% = 7%     |
| Paraguay  | BBB-   | 5.5% + 1.75% = 7.25% |
| Peru      | B      | 5.5% + 2.5% = 8%     |
| Uruguay   | BBB    | 5.5% + 1.75% = 7.25% |

# Risk Premiums for Asia

| Country     | Rating | Risk Premium         |
|-------------|--------|----------------------|
| China       | BBB+   | 5.5% + 1.5% = 7.00%  |
| Indonesia   | BBB    | 5.5% + 1.75% = 7.25% |
| India       | BB+    | 5.5% + 2.00% = 7.50% |
| Japan       | AAA    | 5.5% + 0.00% = 5.50% |
| Korea       | AA-    | 5.5% + 1.00% = 6.50% |
| Malaysia    | A+     | 5.5% + 1.25% = 6.75% |
| Pakistan    | B+     | 5.5% + 2.75% = 8.25% |
| Phillipines | BB+    | 5.5% + 2.00% = 7.50% |
| Singapore   | AAA    | 5.5% + 0.00% = 7.50% |
| Taiwan      | AA+    | 5.5% + 0.50% = 6.00% |
| Thailand    | A      | 5.5% + 1.35% = 6.85% |

# Implied Equity Premiums

- <sup>l</sup> If we use a basic discounted cash flow model, we can estimate the implied risk premium from the current level of stock prices. <sup>l</sup> For instance, if stock prices are determined by the simple Gordon Growth Model:
  - Value = Expected Dividends next year/ (Required Returns on Stocks Expected Growth Rate)
- Plugging in the current level of the index, the dividends on the index and expected growth rate will yield a "implied" expected return on stocks. Subtracting out the riskfree rate will yield the implied premium. <sup>l</sup> The problems with this approach are:
  - the discounted cash flow model used to value the stock index has to be the right one.
  - the inputs on dividends and expected growth have to be correct
  - it implicitly assumes that the market is currently correctly valued

# Implied Risk Premiums in the US

Implied Risk Premium: U.S. Equities

![](_page_26_Figure_2.jpeg)

# Historical and Implied Premiums

<sup>l</sup> Assume that you use the historical risk premium of 5.5% in doing your discounted cash flow valuations and that the implied premium in the market is only 2.5%. As you value stocks, you will find <sup>o</sup> more under valued than over valued stocks <sup>o</sup> more over valued than under valued stocks <sup>o</sup> about as many under and over valued stocks

# Estimating Beta

<sup>l</sup> The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm) -

$$R_j = a + b R_m$$

– where a is the intercept and b is the slope of the regression.

<sup>l</sup> The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.

# Beta Estimation in Practice

10

DG28 Equity BETA

## HISTORICAL BETA

Number of points may be insufficient for an accurate beta.

**DIS**

**US**

THE WALT DISNEY CO.

Market

**SPX**

S&P 500 INDEX

\* Identifies latest observation

Period M (D-W-M-Q-Y)  
 Range 1/31/92 To 12/31/96  
I (T=Trade, B=Bid, A=Ask)

| <b>ADJ BETA</b>              | 1.27 |
|------------------------------|------|
| <b>RAW BETA</b>              | 1.40 |
| Alpha (Intercept)            | -.06 |
| R <sup>2</sup> (Correlation) | .32  |
| Std Dev of Error             | 5.09 |
| Std Error of Beta            | .27  |
| Number of Points             | 59   |

![](_page_29_Figure_32.jpeg)

$$\text{Adj beta} = (0.67) * \text{Raw Beta} + (0.33) * 1.0$$

Bloomberg-all rights reserved. Frankfurt:69-920410 Hong Kong:2-521-3000 London:171-330-7500 New York:212-318-2000  
 Princeton:609-279-3000 Singapore:226-3000 Sydney:2-9777-8600 Tokyo:3-3201-8900 Sao Paulo:11-3048-4500  
 G261-4-0 08-Aug-97 14:34:21

# Estimating Expected Returns: September 30, 1997

<sup>l</sup> Disney's Beta = 140 <sup>l</sup> Riskfree Rate = 7.00% (Long term Government Bond rate) <sup>l</sup> Risk Premium = 5.50% (Approximate historical premium) <sup>l</sup> Expected Return = 7.00% + 1.40 (5.50%) = 14.70%

# The Implications of an Expected Return

<sup>l</sup> Which of the following statements best describes what the expected return of 14.70% that emerges from the capital asset pricing model is telling you as an investor? <sup>o</sup> This stock is a good investment since it will make a higher return than the market (which is expected to make 12.50%) <sup>o</sup> If the CAPM is the right model for risk and the beta is correctly measured, this stock can be expected to make 14.70% over the long term. <sup>o</sup> This stock is correctly valued <sup>o</sup> None of the above

# How investors use this expected return

- <sup>l</sup> If the stock is correctly valued, the CAPM is the right model for risk and the beta is correctly estimated, an investment in Disney stock can be expected to earn a return of 14.70% over the long term. <sup>l</sup> Investors in stock in Disney
  - need to make 14.70% over time to break even
  - will decide to invest or not invest in Disney based upon whether they think they can make more or less than this hurdle rate

#### How managers use this expected return

- <sup>l</sup> Managers at Disney
  - need to make at least 14.70% as a return for their equity investors to break even.
- this is the hurdle rate for projects, when the investment is analyzed from an equity standpoint <sup>l</sup> In other words, Disney's cost of equity is 14.70%.

# Beta Estimation and Index Choice

![](_page_34_Figure_12.jpeg)

#### A Few Questions

<sup>l</sup> The R squared for Nestle is very high and the standard error is very low, at least relative to U.S. firms. This implies that this beta estimate is a better one than those for U.S. firms. <sup>o</sup> True <sup>o</sup> False <sup>l</sup> The beta for Nestle is 0.97. This is the appropriate measure of risk to what kind of investor (What has to be in his or her portfolio for this beta to be an adequate measure of risk?) <sup>l</sup> If you were an investor in primarily U.S. stocks, would this be an appropriate measure of risk?

# Nestle: To a U.S. Investor

## HISTORICAL BETA

Number of points may be insufficient for an accurate beta.

**NESN**

**SW**

NESTLE SA-REGISTERED

Market

**SPX**

S&P 500 INDEX

\* Identifies latest observation

Period [ ] (D-W-M-Q-Y)  
 Range 1/31/92 To 11/28/97  
[ ] (T=Trade, B=Bid, A=Ask)

| <b>ADJ BETA</b>   | .86  |
|-------------------|------|
| <b>RAW BETA</b>   | .79  |
| Alpha (Intercept) | .35  |
| R2 (Correlation)  | .19  |
| Std Dev of Error  | 4.83 |
| Std Error of Beta | .20  |
| Number of Points  | 70   |

$$\text{Adj beta} = (0.67) * \text{Raw Beta} + (0.33) * 1.0$$

Bloomberg-all rights reserved. Frankfurt: 69-920410 Hong Kong: 2-521-3000 London: 171-330-7500 New York: 212-318-2000  
 Princeton: 609-279-3000 Singapore: 226-3000 Sydney: 2-9777-9600 Tokyo: 3-3201-8900 Sao Paulo: 11-3048-4500  
 6261-4-0 29-Dec-97 11:39:28

![](_page_36_Figure_25.jpeg)

# Nestle: To a Global Investor

## HISTORICAL BETA

Number of points may be insufficient for an accurate beta.

**NESN SW**

Market **NFT**

Period **I** (D-W-M-O-Y)  
 Range **1/31/92 To 11/28/97**  
**I** (T=Trade, B=Bid, A=Ask)

| <b>ADJ BETA</b>   | .76  |
|-------------------|------|
| <b>RAW BETA</b>   | .63  |
| Alpha (Intercept) | .41  |
| R2 (Correlation)  | .17  |
| Std Dev of Error  | 4.91 |
| Std Error of Beta | .17  |
| Number of Points  | 70   |

NESTLE SA-REGISTERED

MS MULTINATIONAL INDEX  
 \* Identifies latest observation

![](_page_37_Figure_21.jpeg)

$$\text{Adj beta} = (0.67) * \text{Raw Beta} + (0.33) * 1.0$$

Bloomberg-all rights reserved. Frankfurt: 69-920410 Hong Kong: 2-521-3000 London: 171-330-7500 New York: 212-318-2000  
 Princeton: 609-279-3000 Singapore: 226-3000 Sydney: 2-9777-9600 Tokyo: 3-3201-6900 Sao Paulo: 11-3048-4500  
 6261-4-0 29-Dec-97 11:33:37

# Telebras: The Index Effect Again

## HISTORICAL BETA

**TEL3 BZ**

Market **IBDV**

Period **(D-W-M-Q-Y)**  
 Range **12/29/95 To 12/26/97**  
**(T=Trade, B=Bid, A=Ask)**

| <b>ADJ BETA</b>   | 1.09 |
|-------------------|------|
| <b>RAW BETA</b>   | 1.13 |
| Alpha (Intercept) | .19  |
| R2 (Correlation)  | .02  |
| Std Dev of Error  | 2.62 |
| Std Error of Beta | .05  |
| Number of Points  | 104  |

TELECOMUNIC BRASILEIRAS S.A.

BRAZIL BOVESPA STOCK IDX

\* Identifies latest observation

![](_page_38_Figure_19.jpeg)

$$\text{Adj beta} = (0.67) * \text{Raw Beta} + (0.33) * 1.0$$

Bloomberg-all rights reserved. Frankfurt: 69-920410 Hong Kong: 2-521-3000 London: 171-330-7500 New York: 212-319-2000  
 Princeton: 609-279-3000 Singapore: 226-3000 Sydney: 2-9777-8600 Tokyo: 3-3201-8900 Sao Paulo: 11-3048-4500  
 6261-4-0 29-Dec-97 11:44:10

# Brahma: The Contrast

## HISTORICAL BETA

**BRH3**

**BZ**

CIA CERVEJARIA BRAHMA

Market

**IBOV**

BRAZIL BOVESPA STOCK IDX

\*Identifies latest observation

Period  (D-W-M-Q-Y)  
 Range  To   
 (T=Trade, B=Bid, A=Ask)

| <b>ADJ BETA</b>   | .48  |
|-------------------|------|
| <b>RAW BETA</b>   | .23  |
| Alpha (Intercept) | .39  |
| R2 (Correlation)  | .07  |
| Std Dev of Error  | 4.05 |
| Std Error of Beta | .08  |
| Number of Points  | 103  |

$$\text{Adj beta} = (0.67) * \text{Raw Beta} + (0.33) * 1.0$$

Bloomberg-all rights reserved. Frankfurt:69-920410 Hong Kong:2-521-3000 London:171-330-7500 New York:212-318-2000  
 Princeton:609-273-3000 Singapore:226-3000 Sydney:2-9777-8600 Tokyo:3-3201-8900 Sao Paulo:11-3048-4500  
 6261-4-0 29-Dec-97 11:45:31

#### Beta Differences

Beta = 1 Average Stock

Beta > 1 Above-average Risk

Beta < 1 Below-average Risk

**Government bonds:** Beta = 0

**CVRD:** Beta=0.64

**Petrobras:** Beta = 1.04

Low Risk

High Risk

**Eletrobras:** Beta = 1.22

**Minupar:** Beta = 1.72

#### **BETA AS A MEASURE OF RISK**

**Telebras:** Beta = 1.11

**Brahma**: Beta = 0.84

**Brahma:** Beta=0.50 169 stocks

9 stocks

# The Problem with Regression Betas

- <sup>l</sup> When analysts use the CAPM, they generally assume that the regression is the only way to estimate betas. <sup>l</sup> Regression betas are not necessarily good estimates of the "true" beta because of
  - the market index may be narrowly defined and dominated by a few stocks
  - even if the market index is well defined, the standard error on the beta estimate is usually large leading to a wide range for the true beta
  - even if the market index is well defined and the standard error on the beta is low, the regression estimate is a beta for the period of the analysis. To the extent that the company has changed over the time period (in terms of business or financial leverage), this may not be the right beta for the next period or periods.

# Solutions to the Regression Beta Problem

- <sup>l</sup> Modify the regression beta by
- changing the index used to estimate the beta adjusting the regression beta estimate, by bringing in information about the fundamentals of the company <sup>l</sup> Estimate the beta for the firm using
  - the standard deviation in stock prices instead of a regression against an index.
- accounting earnings or revenues, which are less noisy than market prices. <sup>l</sup> Estimate the beta for the firm from the bottom up without employing the regression technique. This will require
  - understanding the business mix of the firm
- estimating the financial leverage of the firm <sup>l</sup> Use an alternative measure of market risk that does not need a regression.

# Modified Regression Betas

- <sup>l</sup> *Adjusted Betas*: When one or a few stocks dominate an index, the betas might be better estimated relative to an equally weighted index. While this approach may eliminate some of the more egregious problems associated with indices dominated by a few stocks, it will still leave us with beta estimates with large standard errors. <sup>l</sup> *Enhanced Betas*: Adjust the beta to reflect the differences between firms on other financial variables that are correlated with market risk
  - Barra, which is one of the most respected beta estimation services in the world, employs this technique. They adjust regression betas for differences in a number of accounting variables.
  - The variables to adjust for, and the extent of the adjustment, are obtained by looking at variables that are correlated with returns over time.

# Adjusted Beta Calculation: Brahma

<sup>l</sup> Consider the earlier regression done for Brahma against the Bovespa. Given the problems with the Bovespa, we could consider running the regression against alternative market indices:

| Index   | Beta | R squared | Notes           |
|---------|------|-----------|-----------------|
| Bovespa | 0.23 | 0.07      |                 |
| I-Senn  | 0.26 | 0.08      | Market Cap Wtd. |
| S&P     | 0.51 | 0.06      | Could use ADR   |
| MSCI    | 0.39 | 0.04      | Could use ADR   |

<sup>l</sup> For many large non-US companies, with ADRs listed in the US, the betas can be estimated relative to the U.S. or Global indices.

# Betas and Fundamentals

<sup>l</sup> The earliest studies in the 1970s combined industry and companyfundamental factors to predict betas. <sup>l</sup> Income statement and balance sheet variables are important predictors of beta <sup>l</sup> The following is a regression relating the betas of NYSE and AMEX stocks in 1996 to four variables - dividend yield, standard deviation in operating income, market capitalization and book debt/equity ratio yielded the following.

BETA = 0. 7997 + 2.28 Std Dev in Operating Income- 3.23 Dividend Yield + 0.21 Debt/Equity Ratio - .000005 Market Capitalization where,

Market Cap: measured as market value of equity (in millions)

# Using the Fundamentals to Estimate Betas

- <sup>l</sup> To use these fundamentals to estimate a beta for Disney, for instance, you would estimate the independent variables for Disney
  - Standard Deviation in Operating Income = 20.60%
  - Dividend Yield = 0.62%
  - Debt/Equity Ratio (Book) = 77%
- Market Capitalization of Equity = \$ 54,471(in mils) <sup>l</sup> The estimated beta for Disney is:

BETA = 
$$0.7997 + 2.28 (0.206) - 3.23 (0.0062) + 0.21 (0.77) - .000005$$
  
 $(54,471) = 1.14$ 

<sup>l</sup> Alternatively, the regression beta could have been adjusted for differences on these fundamentals.

# Other Measures of Market Risk

#### <sup>l</sup> *Relative Standard Deviation*

= Standard Deviation of Firm j / Average Standard Deviation across all stocks

- This approach steers clear of the index definition problems that betas have, but is based on the implicit assumption that total risk (which is what standard deviation measures) and market risk are highly correlated.

#### <sup>l</sup> *Accounting Betas*

- If the noise in market data is what makes the betas unreliable, estimates of betas can be obtained using accounting earnings.
- This approach can be used for non-traded firms as well, but suffers from a serious data limitation problem.

#### Relative Volatility

| Government bonds: | Rel Vol = 0              |
|-------------------|--------------------------|
| Bradesco:         | Rel Vol=0.70             |
| Acesita:          | Rel Vol = 1.01           |
| Celesc:           | Rel Vol = 1.25           |
| Serrano:          | Rel Vol = 2.20           |
| Usimanas:         | Rel Vol = 1.11           |
| Telebras:         | Rel Vol= 0.84            |
| Brahma:           | Rel Vol=0.50 86 stocks   |
| Sifco:            | Rel Vol = 1.50 83 stocks |

High Risk

#### **RELATIVE VOLATILITY AS A MEASURE OF RISK**

# Estimating Cost of Equity from Relative Standard Deviation: Brazil

- <sup>l</sup> The analysis is done in real terms <sup>l</sup> The riskfree rate has to be a real riskfree rate.
  - We will use the expected real growth rate in the Brazilian economy of approximately 5%
- This assumption is largely self correcting since the expected real growth rate in the valuation is also assumed to be 5% <sup>l</sup> The risk premium used, based upon the country rating, is 7.5%.
- Should this be adjusted as we go into the future? <sup>l</sup> Estimated Cost of Equity
  - *Company Beta Cost of Equity* Telebras 0.87 5%+0.87 (7.5%) = 11.53% CVRD 0.85 5%+0.85 (7.5%) = 11.38% Aracruz 0.72 5%+0.72 (7.5%) = 10.40%

# Accounting Betas

<sup>l</sup> An accounting beta is estimated by regressing the changes in earnings of a firm against changes in earnings on a market index.

$$\Delta \text{ Earnings}_{\text{Firm}} = a + b \Delta \text{ Earnings}_{\text{Market Index}}$$

<sup>l</sup> The slope of the regression is the accounting beta for this firm. <sup>l</sup> The key limitation of this approach is that accounting data is not measured very often. Thus, the regression's power is limited by the absence of data.

# Estimating an Accounting Beta

| Year | Change in Disney EPS | Change in S&P 500 Earnings |
|------|----------------------|----------------------------|
| 1980 | -7.69%               | -2.10%                     |
| 1981 | -4.17%               | 6.70%                      |
| 1982 | -17.39%              | -45.50%                    |
| 1983 | 11.76%               | 37.00%                     |
| 1984 | 68.42%               | 41.80%                     |
| 1985 | -10.83%              | -11.80%                    |
| 1986 | 43.75%               | 7.00%                      |
| 1987 | 54.35%               | 41.50%                     |
| 1988 | 33.80%               | 41.80%                     |
| 1989 | 34.74%               | 2.60%                      |
| 1990 | 17.19%               | -18.00%                    |
| 1991 | -20.00%              | -47.40%                    |
| 1992 | 26.67%               | 64.50%                     |
| 1993 | 7.24%                | 20.00%                     |
| 1994 | 25.15%               | 25.30%                     |
| 1995 | 24.02%               | 15.50%                     |
| 1996 | -11.86%              | 24.00%                     |

#### The Accounting Beta

<sup>l</sup> Regressing Disney EPS against S&P 500 earnings, we get:

$$\text{Earnings}_{\text{Disney}} = 0.10 + 0.54 \Delta \text{Earnings}_{\text{S\&P 500}}$$

<sup>l</sup> The accounting beta for Disney is 0.54.

# Accounting Betas: The Effects of Smoothing

<sup>l</sup> Accountants tend to smooth out earnings, relative to value and market prices. As a consequence, we would expect accounting betas for most firms to be <sup>o</sup> closer to zero <sup>o</sup> less than one <sup>o</sup> close to one <sup>o</sup> greater than one

# Alternative Measures of Market Risk

#### <sup>l</sup> *Proxy Variables for Risk*

- Use variables such as market capitalization as proxies for market risk
- Regression can be used to make relationship between return and these variables explicit.

#### <sup>l</sup> *Qualitative Risk Measures*

- Divide firms into risk classes
- Assign a different cost of equity for each risk class

# Using Proxy Variables for Risk

<sup>l</sup> Fama and French, in much quoted study on the efficacy (or the lack) of the CAPM, looked at returns on stocks between 1963 and 1990. While they found no relationship with differences in betas, they did find a strong relationship between size, book/market ratios and returns. <sup>l</sup> A regression off monthly returns on stocks on the NYSE, using data from 1963 to 1990:

$$R_t = 1.77\% - 0.0011 \ln(MV) + 0.0035 \ln(BV/MV)$$

MV = Market Value of Equity

BV/MV = Book Value of Equity / Market Value of Equity

<sup>l</sup> To get the cost of equity for Disney, you would plug in the values into this regression. Since Disney has a market value of \$ 54,471 million and a book/market ratio of 0.30 its monthly return would have been:

$$R_t = .0177 - .0011 \ln(54,471) + 0.0035 (.3) = 0.675\%$$
 a month or 8.41% a year

#### Korea: Proxies for Risk and Returns

![](_page_56_Figure_1.jpeg)

#### Bottom-up Betas

- <sup>l</sup> The other approach to estimate betas is to build them up from the base, by understanding the business that a firm is in, and estimating a beta based upon this understanding. <sup>l</sup> To use this approach, we need to
  - deconstruct betas, and understand the fundamental determinants of betas (i.e., why are betas high for some firms and low for others?)
  - come up with a way of linking the fundamental characteristics of an asset with a beta that can be used in valuation.

#### Determinant 1: Product or Service Type

- <sup>l</sup> The beta value for a firm depends upon the sensitivity of the demand for its products and services and of its costs to macroeconomic factors that affect the overall market.
  - Cyclical companies have higher betas than non-cyclical firms
  - Firms which sell more discretionary products will have higher betas than firms that sell less discretionary products

#### Determinant 2: Operating Leverage Effects

<sup>l</sup> Operating leverage refers to the proportion of the total costs of the firm that are fixed. <sup>l</sup> Other things remaining equal, higher operating leverage results in greater earnings variability which in turn results in higher betas.

# Measures of Operating Leverage

Fixed Costs Measure = Fixed Costs / Variable Costs

<sup>l</sup> This measures the relationship between fixed and variable costs. The higher the proportion, the higher the operating leverage.

EBIT Variability Measure = % Change in EBIT / % Change in Revenues

<sup>l</sup> This measures how quickly the earnings before interest and taxes changes as revenue changes. The higher this number, the greater the operating leverage.

#### The Effects of Firm Actions on Beta

<sup>l</sup> When Robert Goizueta became CEO of Coca Cola, he proceeded to move most of the bottling plants and equipment to Coca Cola Bottling, which trades as an independent company (with Coca Cola as a primary but not the only investor). Which of the following consequences would you predict for Coca Cola's beta? <sup>o</sup> Coke's beta should go up <sup>o</sup> Coke'e beta should go down <sup>o</sup> Coke's beta should be unchanged <sup>l</sup> Would your answer have been any different if Coca Cola had owned 100% of the bottling plants?

#### Determinant 3: Financial Leverage

<sup>l</sup> As firms borrow, they create fixed costs (interest payments) that make their earnings to equity investors more volatile. <sup>l</sup> This increased earnings volatility increases the equity beta

#### Equity Betas and Leverage

<sup>l</sup> The beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_L = \beta_u (1 + ((1-t)D/E))$$

where

### $\beta_L = \text{Levered or Equity Beta}$

### $\beta_u$ = Unlevered Beta

t = Corporate marginal tax rate

D = Market Value of Debt

E = Market Value of Equity

# Betas and Leverage: Hansol Paper, a Korean Paper Company

- Current Beta = 1.03
- Current Debt/Equity Ratio = 950/346=2.74
- Current Unlevered Beta = 1.03/(1+2.74(1-.3)) = 0.35

| Debt Ratio | D/E Ratio | Beta | Cost of Equity |
|------------|-----------|------|----------------|
| 0.00%      | 0.00%     | 0.35 | 14.29%         |
| 10.00%     | 11.11%    | 0.38 | 14.47%         |
| 20.00%     | 25.00%    | 0.41 | 14.69%         |
| 30.00%     | 42.86%    | 0.46 | 14.98%         |
| 40.00%     | 66.67%    | 0.52 | 15.36%         |
| 50.00%     | 100.00%   | 0.60 | 15.90%         |
| 60.00%     | 150.00%   | 0.74 | 16.82%         |
| 70.00%     | 233.33%   | 1.00 | 18.50%         |
| 80.00%     | 400.00%   | 1.50 | 21.76%         |
| 90.00%     | 900.00%   | 3.00 | 31.51%         |

# Bottom-up versus Top-down Beta

- <sup>l</sup> The top-down beta for a firm comes from a regression <sup>l</sup> The bottom up beta can be estimated by doing the following:
  - Find out the businesses that a firm operates in
  - Find the unlevered betas of other firms in these businesses
  - Take a weighted (by sales or operating income) average of these unlevered betas
- Lever up using the firm's debt/equity ratio <sup>l</sup> The bottom up beta will give you a better estimate of the true beta when
  - the standard error of the beta from the regression is high (and) the beta for a firm is very different from the average for the business
  - the firm has reorganized or restructured itself substantially during the period of the regression
  - when a firm is not traded

#### Decomposing Disney's Beta

| Business         | Beta | Unlevered D/E Ratio | Levered Beta | Riskfree Rate | Risk Premium | Cost of Equity |
|------------------|------|---------------------|--------------|---------------|--------------|----------------|
| Creative Content | 1.25 | 22.23%              | 1.43         | 7.00%         | 5.50%        | 14.85%         |
| Retailing        | 1.5  | 22.23%              | 1.71         | 7.00%         | 5.50%        | 16.42%         |
| Broadcasting     | 0.9  | 22.23%              | 1.03         | 7.00%         | 5.50%        | 12.65%         |
| Theme Parks      | 1.1  | 22.23%              | 1.26         | 7.00%         | 5.50%        | 13.91%         |
| Real Estate      | 0.7  | 22.23%              | 0.80         | 7.00%         | 5.50%        | 11.40%         |
| Disney           | 1.09 | 22.23%              | 1.25         | 7.00%         | 5.50%        | 13.85%         |

# Choosing among Alternative Beta Estimates: Disney

| Approach            | Beta  | Comments                           |
|---------------------|-------|------------------------------------|
| Regression          | 1.40  | Company has changed significantly  |
| Modified Regression | 1.15  | Used MSCI as market index          |
| Enhanced Beta       | 1.14  | Fundamental regression has low R 2 |
| Accounting Beta     | 0.54  | Only 16 observations               |
| Proxy Variable      | 0.25* | Uses market cap and book/market    |
| Bottom-up Beta      | 1.25  | Reflects current business and      |

\* Estimated from expected return on 8.41%.

#### Which beta would you choose?

<sup>l</sup> Given the alternative estimates of beta for Disney, which one would you choose to use in your valuation? <sup>o</sup> Regression <sup>o</sup> Modified Regression <sup>o</sup> Enhanced Beta <sup>o</sup> Accounting Beta <sup>o</sup> Proxy Variable <sup>o</sup> Bottom-up Beta Why?

# Estimating a Bottom-up Beta for Hansol Paper

<sup>l</sup> Hansol paper, like most Korean firms in 1996, had an extraordinary amount of debt on its balance sheet. The beta does not reflect this risk adequately, since it is estimated using the Korean index. <sup>l</sup> To estimate a bottom up beta, we looked at paper and pulp firms:

| Comparable Firms (# of firms) | Beta | Average D/E Ratio | Unlevered Beta |
|-------------------------------|------|-------------------|----------------|
| Asian Paper & Pulp (5)        | 0.92 | 65.00%            | 0.65           |
| U.S. Paper and Pulp (45)      | 0.85 | 35.00%            | 0.69           |
| Global Paper & Pulp (187)     | 0.80 | 50.00%            | 0.61           |

Unlevered Beta for Paper and Pulp is 0.61

<sup>l</sup> Using the current debt equity ratio of 274%, the beta can be estimated:

Beta for Hansol Paper = 0.61 (1 + (1-.3) (2.74)) = 1.78

# Estimating Betas: More Examples

| Company       | Approach Used          | Beta |
|---------------|------------------------|------|
| ABN Amro      | Comparable Firms       | 0.99 |
| Nestle        | Bottom-up Firms        | 0.85 |
| Titan Watches | Regression against BSE | 0.94 |
| Brahma        | Bottom-up Beta         | 0.80 |
| Amazon.com    | Bottom-up Beta         | 1.80 |

# Measuring Cost of Capital

- <sup>l</sup> It will depend upon:
  - (a) the components of financing: Debt, Equity or Preferred stock
- (b) the cost of each component <sup>l</sup> In summary, the cost of capital is the cost of each component weighted by its relative market value.

$$\text{WACC} = k_e (E/(D+E)) + k_d (D/(D+E))$$

#### The Cost of Debt

- <sup>l</sup> The cost of debt is the market interest rate that the firm has to pay on its borrowing. It will depend upon three components-
  - (a) The general level of interest rates
  - (b) The default premium
  - (c) The firm's tax rate

#### What the cost of debt is and is not..

- The cost of debt is
  - the rate at which the company can borrow at today
  - corrected for the tax benefit it gets for interest payments. Cost of debt = kd= Interest Rate on Debt (1 - Tax rate)
- The cost of debt is not
  - the interest rate at which the company obtained the debt it has on its books.

# Estimating the Cost of Debt

- <sup>l</sup> If the firm has bonds outstanding, and the bonds are traded, the yield to maturity on a long-term, straight (no special features) bond can be used as the interest rate. <sup>l</sup> If the firm is rated, use the rating and a typical default spread on bonds with that rating to estimate the cost of debt. <sup>l</sup> If the firm is not rated,
  - and it has recently borrowed long term from a bank, use the interest rate on the borrowing or
- estimate a synthetic rating for the company, and use the synthetic rating to arrive at a default spread and a cost of debt <sup>l</sup> The cost of debt has to be estimated in the same currency as the cost of equity and the cash flows in the valuation.

# Estimating Synthetic Ratings

<sup>l</sup> The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

<sup>l</sup> For Hansol Paper, for instance

Interest Coverage Ratio = 109,569/85,401 = 1.28

- Based upon the relationship between interest coverage ratios and ratings, we would estimate a rating of B- for Hansol Paper.

<sup>l</sup> For Brahma,

Interest Coverage Ratio = 413/257 = 1.61

- Based upon the relationship between interest coverage ratios and ratings, we would estimate a rating of B for Brahma

# Interest Coverage Ratios, Ratings and Default Spreads

| If Interest Coverage Ratio is | Estimated Bond Rating | Default Spread |
|-------------------------------|-----------------------|----------------|
| > 8.50                        | AAA                   | 0.20%          |
| 6.50 - 8.50                   | AA                    | 0.50%          |
| 5.50 - 6.50                   | A+                    | 0.80%          |
| 4.25 - 5.50                   | A                     | 1.00%          |
| 3.00 - 4.25                   | A–                    | 1.25%          |
| 2.50 - 3.00                   | BBB                   | 1.50%          |
| 2.00 - 2.50                   | BB                    | 2.00%          |
| 1.75 - 2.00                   | B+                    | 2.50%          |
| 1.50 - 1.75                   | B                     | 3.25%          |
| 1.25 - 1.50                   | B –                   | 4.25%          |
| 0.80 - 1.25                   | CCC                   | 5.00%          |
| 0.65 - 0.80                   | CC                    | 6.00%          |
| 0.20 - 0.65                   | C                     | 7.50%          |
| < 0.20                        | D                     | 10.00%         |

# Examples of Cost of Debt calculation

| Company       | Approach Used               | Cost of Debt           |
|---------------|-----------------------------|------------------------|
| Disney        | Rating & Default spread     | 7% + 0.50% = 7.50%     |
| Hansol Paper  | Synthetic Rating based upon | 12% + 4.25% = 16.25%   |
|               | Interest coverage ratio     | (in nominal WN)        |
| Nestle        | Rating & Default spread     | 4.25%+0.25%= 4.50%     |
| ABN Amro      | YTM on 10-year straight     | 5.40% (in NLG)         |
| Titan Watches | Recent Borrowing            | 13.5% (in nominal Rs.) |
| Brahma        | Synthetic Rating based upon | 5% + 3.25% = 8.25%     |
|               | interest coverage ratio     | (in real BR)           |

#### Calculate the weights of each component

- <sup>l</sup> Use target/average debt weights rather than project-specific weights. <sup>l</sup> Use market value weights for debt and equity.
  - The cost of capital is a measure of how much it would cost you to go out and raise the financing to acquire the business you are valuing today. Since you have to pay market prices for debt and equity, the cost of capital is better estimated using market value weights. – Book values are often misleading and outdated.

# Estimating Market Value Weights

- ● Market Value of Equity should include the following
  - – Market Value of Shares outstanding
  - – Market Value of Warrants outstanding
  - – Market Value of Conversion Option in Convertible Bonds
- ● Market Value of Debt is more difficult to estimate because few firms have only publicly traded debt. There are two solutions:
  - – Assume book value of debt is equal to market value
  - – Estimate the market value of debt from the book value
  - – For Disney, with book value of \$12,342 million, interest expenses of \$479 million, and a current cost of borrowing of 7.5% (from its rating)

Estimated MV of Disney Debt =

$$479 \left[ \frac{(1 - \frac{1}{(1.075)^3})}{.075} \right] + \frac{12,342}{(1.075)^3} = \$11,180$$

# Estimating Cost of Capital: Disney

#### <sup>l</sup> Equity

– Cost of Equity = 13.85%

– Market Value of Equity = \$54.88 Billion

– Equity/(Debt+Equity ) = 82%

#### <sup>l</sup> Debt

– After-tax Cost of debt = 7.50% (1-.36) = 4.80%

– Market Value of Debt = \$ 11.18 Billion

– Debt/(Debt +Equity) = 18%

<sup>l</sup> Cost of Capital = 13.85%(.82)+4.80%(.18) = 12.22%

#### Book Value and Market Value

<sup>l</sup> If you use book value weights for debt and equity to calculate cost of capital in the United States, and value a firm on the basis of this cost of capital, you will generally end up <sup>o</sup> over valuing the firm <sup>o</sup> under valuing the firm <sup>o</sup> neither

# Estimating Cost of Capital: Hansol Paper

#### <sup>l</sup> Equity

– Cost of Equity = 23.57% (with beta of 1.78)

– Market Value of Equity = 23000\*15.062= 346,426 Million

– Equity/(Debt+Equity ) = 26.72%

#### <sup>l</sup> Debt

– After-tax Cost of debt = 16.25% (1-.3) = 11.38%

– Market Value of Debt = 949,862 Million

– Debt/(Debt +Equity) = 73.28%

<sup>l</sup> Cost of Capital = 23.57%(.267)+11.38%(.733) = 14.63%

#### Firm Value , WACC and Optimal Debt ratios

#### <sup>l</sup> Objective:

- A firm should pick a debt ratio that minimizes its cost of capital.

#### <sup>l</sup> Why?:

- Because if operating cash flows are held constant, minimizing the Cost of Capital maximizes Firm Value.

# Mechanics of Cost of Capital Estimation

- 1. Estimate the Cost of Equity at different levels of debt: Equity will become riskier -> Cost of Equity will increase.
- 2. Estimate the Cost of Debt at different levels of debt: Default risk will go up and bond ratings will go down as debt goes up -> Cost of Debt will increase.
- 3. Estimate the Cost of Capital at different levels of debt
- 4. Calculate the effect on Firm Value and Stock Price.

# Disney: Debt Ratios, Cost of Capital and Firm Value

| Debt Beta Ratio | Cost of Equity | Cov Ratio | Rating | Rate   | AT Rate | WACC   | Firm Value |
|-----------------|----------------|-----------|--------|--------|---------|--------|------------|
| 0% 1.09         | 13.00%         | ¥         | AAA    | 7.20%  | 4.61%   | 13.00% | \$53,842   |
| 10%1.17         | 13.43%         | 12.44     | AAA    | 7.20%  | 4.61%   | 12.55% | \$58,341   |
| 20%1.27         | 13.96%         | 5.74      | A+     | 7.80%  | 4.99%   | 12.17% | \$62,650   |
| 30%1.39         | 14.65%         | 3.62      | A-     | 8.25%  | 5.28%   | 11.84% | \$66,930   |
| 40%1.56         | 15.56%         | 2.49      | BB     | 9.00%  | 5.76%   | 11.64% | \$69,739   |
| 50%1.79         | 16.85%         | 1.75      | B      | 10.25% | 6.56%   | 11.70% | \$68,858   |
| 60%2.14         | 18.77%         | 1.24      | CCC    | 12.00% | 7.68%   | 12.11% | \$63,325   |
| 70%2.72         | 21.97%         | 1.07      | CCC    | 12.00% | 7.68%   | 11.97% | \$65,216   |
| 80%3.99         | 28.95%         | 0.93      | CCC    | 12.00% | 7.97%   | 12.17% | \$62,692   |
| 90%8.21         | 52.14%         | 0.77      | CC     | 13.00% | 9.42%   | 13.69% | \$48,160   |

l Firm Value = Current Firm Value + Firm Value (WACC(old) - WACC(new))/(WACC(new)-g)

# Hansol Paper: Debt Ratios, Cost of Capital and Firm Value

| Debt Ratio | Beta | Cost of Equity | Ratio | Int. Cov. Rating | Interest Rate | AT Cost | WACC   | Firm Value   |
|------------|------|----------------|-------|------------------|---------------|---------|--------|--------------|
| 0.00%      | 0.35 | 14.29%         | ¥     | AAA              | 12.30%        | 8.61%   | 14.29% | 988,162 WN   |
| 10.00%     | 0.38 | 14.47%         | 6.87  | AAA              | 12.30%        | 8.61%   | 13.89% | 1,043,287 WN |
| 20.00%     | 0.41 | 14.69%         | 3.25  | A+               | 13.00%        | 9.10%   | 13.58% | 1,089,131 WN |
| 30.00%     | 0.46 | 14.98%         | 2.13  | A                | 13.25%        | 9.28%   | 13.27% | 1,138,299 WN |
| 40.00%     | 0.52 | 15.36%         | 1.51  | BBB              | 14.00%        | 9.80%   | 13.14% | 1,160,668 WN |
| 50.00%     | 0.60 | 15.90%         | 1.13  | B+               | 15.00%        | 10.50%  | 13.20% | 1,150,140 WN |
| 60.00%     | 0.74 | 16.82%         | 0.88  | B                | 16.00%        | 11.77%  | 13.79% | 1,056,435 WN |
| 70.00%     | 0.99 | 18.43%         | 0.75  | B                | 16.00%        | 12.38%  | 14.19% | 1,001,068 WN |
| 80.00%     | 1.50 | 21.76%         | 0.62  | B-               | 17.00%        | 13.83%  | 15.42% | 861,120 WN   |
| 90.00%     | 3.00 | 31.51%         | 0.55  | B-               | 17.00%        | 14.18%  | 15.92% | 813,775 WN   |

l Firm Value = Current Firm Value + Firm Value (WACC(old) - WACC(new))/(WACC(new)-g)

# II. Estimating Cash Flows

DCF Valuation

# Steps in Cash Flow Estimation

- <sup>l</sup> Estimate the current earnings of the firm
  - If looking at cash flows to equity, look at earnings after interest expenses i.e. net income
- If looking at cash flows to the firm, look at operating earnings after taxes <sup>l</sup> Consider how much the firm invested to create future growth
  - If the investment is not expensed, it will be categorized as capital expenditures. To the extent that depreciation provides a cash flow, it will cover some of these expenditures.
- Increasing working capital needs are also investments for future growth <sup>l</sup> If looking at cash flows to equity, consider the cash flows from net debt issues (debt issued - debt repaid)

# Earnings Checks

- <sup>l</sup> When estimating cash flows, we invariably start with accounting earnings. To the extent that we start with accounting earnings in a base year, it is worth considering the following questions:
  - Are basic accounting standards being adhered to in the calculation of the earnings?
  - Are the base year earnings skewed by extraordinary items profits or losses? (Look at earnings prior to extraordinary items)
  - Are the base year earnings affected by any accounting rule changes made during the period? (Changes in inventory or depreciation methods can have a material effect on earnings)
  - Are the base year earnings abnormally low or high? (If so, it may be necessary to normalize the earnings.)
  - How much of the accounting expenses are operating expenses and how much are really expenses to create future growth?

# Three Ways to Think About Earnings

Revenues Revenues \* Capital Invested \*

- Operating Expenses *Operating Margin Pre-tax ROC*

= Operating Income = Operating Income = Operating Income

Capital Invested = Book Value of Debt + Book Value of Equity

Pre-tax ROC = EBIT / (Book Value of Debt + Book Value of Equity)

*The equity shortcuts would be as follows:*

Revenues Revenues \* Equity Invested \*

- Operating Expenses *Net Margin Return on Equity*

- Interest Expenses = Net Income = Net Income

= Taxable Income

- Taxes

= Net Income

# Dividends and Cash Flows to Equity

- <sup>l</sup> In the strictest sense, the only cash flow that an investor will receive from an equity investment in a publicly traded firm is the dividend that will be paid on the stock. <sup>l</sup> Actual dividends, however, are set by the managers of the firm and may be much lower than the potential dividends (that could have been paid out)
  - managers are conservative and try to smooth out dividends
- managers like to hold on to cash to meet unforeseen future contingencies and investment opportunities <sup>l</sup> When actual dividends are less than potential dividends, using a model that focuses only on dividends will under state the true value of the equity in a firm.

# Measuring Potential Dividends

- <sup>l</sup> Some analysts assume that the earnings of a firm represent its potential dividends. This cannot be true for several reasons:
  - Earnings are not cash flows, since there are both non-cash revenues and expenses in the earnings calculation
  - Even if earnings were cash flows, a firm that paid its earnings out as dividends would not be investing in new assets and thus could not grow
- Valuation models, where earnings are discounted back to the present, will over estimate the value of the equity in the firm <sup>l</sup> The potential dividends of a firm are the cash flows left over after the firm has made any "investments" it needs to make to create future growth and net debt repayments (debt repayments - new debt issues)
  - The common categorization of capital expenditures into discretionary and non-discretionary loses its basis when there is future growth built into the valuation.

# Measuring Investment Expenditures

- <sup>l</sup> Accounting rules categorize expenses into operating and capital expenses. In theory, operating expenses are expenses that create earnings only in the current period, whereas capital expenses are those that will create earnings over future periods as well. Operating expenses are netted against revenues to arrive at operating income.
- There are anomalies in the way in which this principle is applied. Research and development expenses are treated as operating expenses, when they are in fact designed to create products in future periods. <sup>l</sup> Capital expenditures, while not shown as operating expenses in the period in which they are made, are depreciated or amortized over their estimated life. This depreciation and amortization expense is a noncash charge when it does occur. <sup>l</sup> The net cash flow from capital expenditures can be then be written as: **Net Capital Expenditures = Capital Expenditures - Depreciation**

# The Working Capital Effect

<sup>l</sup> In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) <sup>l</sup> A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilties (accounts payable <sup>l</sup> Any investment in this measure of working capital ties up cash. Therefore, any increases (decreases) in working capital will reduce (increase) cash flows in that period. <sup>l</sup> When forecasting future growth, it is important to forecast the effects of such growth on working capital needs, and building these effects into the cash flows.

# Estimating Cash Flows: FCFE

<sup>l</sup> Cash flows to Equity for a Levered Firm

Net Income

+ Depreciation & Amortization

= Cash flows from Operations to Equity Investors

- Preferred Dividends

- Capital Expenditures

- Working Capital Needs (Changes in Non-cash Working Capital)

- Principal Repayments

+ Proceeds from New Debt Issues

= Free Cash flow to Equity

# Estimating FCFE when Leverage is Stable

#### Net Income

- ## - (1- δ) (Capital Expenditures - Depreciation)
- - (1-  $\delta$ ) Working Capital Needs
  = Free Cash flow to Equity

## $$\delta = \text{Debt/Capital Ratio}$$

## For this firm,

- – Proceeds from new debt issues = Principal Repayments + d (Capital Expenditures - Depreciation + Working Capital Needs)

# Estimating FCFE: Disney

<sup>l</sup> Net Income=\$ 1533 Million <sup>l</sup> Capital spending = \$ 1,746 Million <sup>l</sup> Depreciation per Share = \$ 1,134 Million <sup>l</sup> Non-cash Working capital Change = \$ 477 Million <sup>l</sup> Debt to Capital Ratio = 23.83% <sup>l</sup> Estimating FCFE (1997):

| Net Income                  | \$1,533 Mil    |
|-----------------------------|----------------|
| - (Cap. Exp - Depr)*(1-DR)  | \$465.90       |
| Chg. Working Capital*(1-DR) | \$363.33       |
| = Free CF to Equity         | \$ 704 Million |
| Dividends Paid              | \$ 345 Million |

#### FCFE and Leverage: Is this a free lunch?

![](_page_98_Figure_1.jpeg)

#### FCFE and Leverage: The Other Shoe Drops

![](_page_99_Figure_1.jpeg)

# Leverage, FCFE and Value

<sup>l</sup> In a discounted cash flow model, increasing the debt/equity ratio will generally increase the expected free cash flows to equity investors over future time periods and also the cost of equity applied in discounting these cash flows. Which of the following statements relating leverage to value would you subscribe to? <sup>o</sup> Increasing leverage will increase value because the cash flow effects will dominate the discount rate effects <sup>o</sup> Increasing leverage will decrease value because the risk effect will be greater than the cash flow effects <sup>o</sup> Increasing leverage will not affect value because the risk effect will exactly offset the cash flow effect <sup>o</sup> Any of the above, depending upon what company you are looking at and where it is in terms of current leverage

#### Estimating FCFE: Brahma

- <sup>l</sup> Net Income (1996) = 325 Million BR <sup>l</sup> Capital spending (1996) = 396 Million <sup>l</sup> Depreciation (1996) = 183 Million BR <sup>l</sup> Non-cash Working capital Change (1996) = 12 Million BR <sup>l</sup> Debt Ratio = 43.48% <sup>l</sup> Estimating FCFE (1996): Earnings per Share 325.00 Million BR
  - (Cap Ex-Depr) (1-DR) = (396-183)(1-.4348) = 120.39 Million BR
  - Change in Non-cash WC (1-DR) = 12 (1-.4348) = 6.78 Million BR **Free Cashflow to Equity 197.83 Million Br Dividends Paid 232.00 Million BR**

#### Cashflow to Firm

| Claimholder              | Cash flows to claimholder         |
|--------------------------|-----------------------------------|
| Equity Investors         | Free Cash flow to Equity          |
| Debt Holders             | Interest Expenses (1 - tax rate)  |
| Preferred Stockholders   | Preferred Dividends               |
| Firm =                   | Free Cash flow to Firm =          |
| Equity Investors         | Free Cash flow to Equity          |
| + Debt Holders           | + Interest Expenses (1- tax rate) |
| + Preferred Stockholders | + Principal Repayments            |

# A Simpler Approach

EBIT ( 1 - tax rate)

- (Capital Expenditures Depreciation)
- Change in Working Capital = Cash flow to the firm <sup>l</sup> The calculation starts with after-tax operating income, where the entire operating income is assumed to be taxed at the marginal tax rate <sup>l</sup> Where are the tax savings from interest payments in this cash flow?

# Estimating FCFF: Disney

- <sup>l</sup> EBIT = \$5,559 Million Tax Rate = 36% <sup>l</sup> Capital spending = \$ 1,746 Million <sup>l</sup> Depreciation = \$ 1,134 Million <sup>l</sup> Non-cash Working capital Change = \$ 477 Million <sup>l</sup> Estimating FCFF EBIT (1-t) \$ 3,558
  - Net Capital Expenditures \$ 612
  - Change in WC \$ 477 = FCFF \$ 2,469 Million

# Estimating FCFF: Hansol Paper

- <sup>l</sup> EBIT (1995) = 109,569 Million WN <sup>l</sup> Capital spending (1995) =326,385 Million WN <sup>l</sup> Depreciation (1995) = 45,000 Million WN <sup>l</sup> Non-cash Working capital Change (1995) = 37,000 WN <sup>l</sup> Estimating FCFF (1995) Current EBIT \* (1 - tax rate) = 109,569 (1-.3) =76,698 Million WN
  - (Capital Spending Depreciation) =282,385
  - Change in Working Capital = 37,000 Current FCFF = **- 242,687 Million WN**

#### Negative FCFF and Implications for Value

<sup>l</sup> A firm which has a negative FCFF is a bad investment and not worth much. <sup>o</sup> True <sup>o</sup> False <sup>l</sup> If true, explain why. <sup>l</sup> If false, explain under what conditions it can be a valuable firm.

# III. Estimating Growth

DCF Valuation

# Ways of Estimating Growth in Earnings

- <sup>l</sup> Look at the past
- The historical growth in earnings per share is usually a good starting point for growth estimation <sup>l</sup> Look at what others are estimating
- Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are. <sup>l</sup> Look at fundamentals
  - Ultimately, all growth in earnings can be traced to two fundamentals how much the firm is investing in new projects, and what returns these projects are making for the firm.

# I. Historical Growth in EPS

- <sup>l</sup> Historical growth rates can be estimated in a number of different ways
  - Arithmetic versus Geometric Averages
- Simple versus Regression Models <sup>l</sup> Historical growth rates can be sensitive to
- the period used in the estimation <sup>l</sup> In using historical growth rates, the following factors have to be considered
  - how to deal with negative earnings
  - the effect of changing size

# Disney: Arithmetic versus Geometric Growth Rates

| Year | EPS  | Growth Rate |
|------|------|-------------|
| 1990 | 1.50 |             |
| 1991 | 1.20 | -20.00%     |
| 1992 | 1.52 | 26.67%      |
| 1993 | 1.63 | 7.24%       |
| 1994 | 2.04 | 25.15%      |
| 1995 | 2.53 | 24.02%      |
| 1996 | 2.23 | -11.86%     |

Arithmetic Average = 8.54%

Geometric Average = (2.23/1.50) (1/6) – 1 = 6.83% (6 years of growth)

<sup>l</sup> The arithmetic average will be higher than the geometric average rate <sup>l</sup> The difference will increase with the standard deviation in earnings

# Disney: The Effects of Altering Estimation Periods

| Year | EPS  | Growth Rate |
|------|------|-------------|
| 1991 | 1.20 |             |
| 1992 | 1.52 | 26.67%      |
| 1993 | 1.63 | 7.24%       |
| 1994 | 2.04 | 25.15%      |
| 1995 | 2.53 | 24.02%      |
| 1996 | 2.23 | -11.86%     |

Taking out 1990 from our sample, changes the growth rates materially:

Arithmetic Average from 1991 to 1996 = 14.24%

Geometric Average = (2.23/1.20)(1/5) = 13.19% (5 years of growth)

# Disney: Linear and Log-Linear Models for Growth

| Year | Year Number | EPS     | ln(EPS) |
|------|-------------|---------|---------|
| 1990 | 1           | \$ 1.50 | 0.4055  |
| 1991 | 2           | \$ 1.20 | 0.1823  |
| 1992 | 3           | \$ 1.52 | 0.4187  |
| 1993 | 4           | \$ 1.63 | 0.4886  |
| 1994 | 5           | \$ 2.04 | 0.7129  |
| 1995 | 6           | \$ 2.53 | 0.9282  |
| 1996 | 7           | \$ 2.23 | 0.8020  |

<sup>l</sup> EPS = 1.04 + 0.19 ( t): EPS grows by \$0.19 a year

Growth Rate = \$0.19/\$1.81 = 10.5% (\$1.81: Average EPS from 90-96)

<sup>l</sup> ln(EPS) = 0.1375 + 0.1063 (t): Growth rate approximately 10.63%

# A Test

<sup>l</sup> You are trying to estimate the growth rate in earnings per share at Time Warner from 1996 to 1997. In 1996, the earnings per share was a deficit of \$0.05. In 1997, the expected earnings per share is \$ 0.25. What is the growth rate? <sup>o</sup> -600% <sup>o</sup> +600% <sup>o</sup> +120% <sup>o</sup> Cannot be estimated

# Dealing with Negative Earnings

- <sup>l</sup> When the earnings in the starting period are negative, the growth rate cannot be estimated. (0.30/-0.05 = -600%) <sup>l</sup> There are three solutions:
  - Use the higher of the two numbers as the denominator (0.30/0.25 = 120%)
  - Use the absolute value of earnings in the starting period as the denominator (0.30/0.05=600%)
- Use a linear regression model and divide the coefficient by the average earnings. <sup>l</sup> When earnings are negative, the growth rate is meaningless. Thus, while the growth rate can be estimated, it does not tell you much about the future.

# The Effect of Size on Growth: Callaway Golf

| Year | Net Profit | Growth Rate |
|------|------------|-------------|
| 1990 | 1.80       |             |
| 1991 | 6.40       | 255.56%     |
| 1992 | 19.30      | 201.56%     |
| 1993 | 41.20      | 113.47%     |
| 1994 | 78.00      | 89.32%      |
| 1995 | 97.70      | 25.26%      |
| 1996 | 122.30     | 25.18%      |

Geometric Average Growth Rate = 102%

# Extrapolation and its Dangers

| Year |             | Net Profit |
|------|-------------|------------|
| 1996 | \$          | 122.30     |
| 1997 | \$          | 247.05     |
| 1998 | \$          | 499.03     |
| 1999 | \$ 1,008.05 |            |
| 2000 | \$ 2,036.25 |            |
| 2001 | \$ 4,113.23 |            |

<sup>l</sup> If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

#### Propositions about Historical Growth

<sup>l</sup> Proposition 1: And in today already walks tomorrow. <sup>l</sup> Proposition 2: You cannot plan the future by the past *Burke* <sup>l</sup> Proposition 3: Past growth carries the most information for firms whose size and business mix have not changed during the estimation period, and are not expected to change during the forecasting period. <sup>l</sup> Proposition 4: Past growth carries the least information for firms in transition (from small to large, from one business to another..)

*Coleridge*

# II. Analyst Forecasts of Growth

- <sup>l</sup> While the job of an analyst is to find under and over valued stocks in the sectors that they follow, a significant proportion of an analyst's time (outside of selling) is spent forecasting earnings per share.
  - Most of this time, in turn, is spent forecasting earnings per share in the next earnings report
- While many analysts forecast expected growth in earnings per share over the next 5 years, the analysis and information (generally) that goes into this estimate is far more limited. <sup>l</sup> Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

# How good are analysts at forecasting growth?

<sup>l</sup> Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| Study             | Time Period          | Analyst Forecast Error | Time Series Model |
|-------------------|----------------------|------------------------|-------------------|
| Collins & Hopwood | Value Line Forecasts | 31.7%                  | 34.1%             |
| Brown & Rozeff    | Value Line Forecasts | 28.4%                  | 32.2%             |
| Fried & Givoly    | Earnings Forecaster  | 16.4%                  | 19.8%             |

- <sup>l</sup> The advantage that analysts have over time series models
  - tends to decrease with the forecast period (next quarter versus 5 years)
  - tends to be greater for larger firms than for smaller firms
- tends to be greater at the industry level than at the company level <sup>l</sup> Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

# Are some analysts more equal than others?

- <sup>l</sup> A study of All-America Analysts (chosen by Institutional Investor) found that
  - There is no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%)
  - However, in the calendar year following being chosen as All-America analysts, these analysts become slightly better forecasters than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts)
  - Earnings revisions made by All-America analysts tend to have a much greater impact on the stock price than revisions from other analysts
  - The recommendations made by the All America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (2.4% for buys; 13.8% for the sells).

# The Five Deadly Sins of an Analyst

<sup>l</sup> **Tunnel Vision**: Becoming so focused on the sector and valuations within the sector that they lose sight of the bigger picture. <sup>l</sup> **Lemmingitis**:Strong urge felt by analysts to change recommendations & revise earnings estimates when other analysts do the same. <sup>l</sup> **Stockholm Syndrome**(shortly to be renamed the Bre-X syndrome): Refers to analysts who start identifying with the managers of the firms that they are supposed to follow. <sup>l</sup> **Factophobia** (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a "story" coupled with a refusal to face the facts. <sup>l</sup> **Dr. Jekyll/Mr.Hyde**: Analyst who thinks his primary job is to bring in investment banking business to the firm.

# Propositions about Analyst Growth Rates

- <sup>l</sup> **Proposition 1**: There if far less private information and far more public information in most analyst forecasts than is generally claimed. <sup>l</sup> **Proposition 2**: The biggest source of private information for analysts remains the company itself which might explain
  - why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources)
  - why there is such a high correlation across analysts forecasts and revisions
- why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team. <sup>l</sup> **Proposition 3**: There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

#### III. Fundamental Growth Rates

| Investment in Existing                                                  | Current Return on Current Investment on   |   |                                                          |
|-------------------------------------------------------------------------|-------------------------------------------|---|----------------------------------------------------------|
| X Projects Projects \$ 1000 Investment                                  | = Earnings \$120 Next Period’s Investment |   | Return on Next                                           |
| in Existing Return on X Projects Investment \$1000 Investment Change in | + in New Projects \$100 Investment        | X | = Investment on Period’s New Projects Earnings Return on |
| in Existing ROI from X Projects                                         | + in New current to next Projects         | X | Change in Earnings Investment on New Projects            |
| \$1000                                                                  | \$100                                     |   | = \$ 12                                                  |

#### Growth Rate Derivations

In the special case where ROI on existing projects remains unchanged and is equal to the ROI on new projects

Investment in New Projects Current Earnings Return on Investment Change in Earnings Current Earnings X = 100 <sup>120</sup> X 12% = \$12 \$120

| Reinvestment Rate | $\times$ | Return on Investment | $=$ | Growth Rate in Earnings |
|-------------------|----------|----------------------|-----|-------------------------|
| 83.33%            | $\times$ | 12%                  | $=$ | 10%                     |

in the more general case where ROI can change from period to period, this can be expanded as follows:

Investment in Existing Projects\*(Change in ROI) + New Projects (ROI) Investment in Existing Projects\* Current ROI Change in Earnings Current Earnings =

For instance, if the ROI increases from 12% to 13%, the expected growth rate can be written as follows:

\$1,000 \* (.13 - .12) + 100 (13%) \$ 1000 \* .12 \$23 \$120 = = 19.17%

# Expected Long Term Growth in EPS

l When looking at growth in earnings per share, these inputs can be cast as follows:

Reinvestment Rate = Retained Earnings/ Current Earnings = Retention Ratio

Return on Investment = ROE = Net Income/Book Value of Equity

l In the special case where the current ROE is expected to remain unchanged

$$g_{\text{EPS}} = \text{Retained Earnings}_{t-1} / \text{NI}_{t-1} * \text{ROE}$$

= Retention Ratio \* ROE

= b \* ROE

<sup>l</sup> Proposition 1: The expected growth rate in earnings for a company cannot exceed its return on equity in the long term.

# Estimating Expected Growth in EPS: ABN Amro

<sup>l</sup> Current Return on Equity = 15.79% <sup>l</sup> Current Retention Ratio = 1 - DPS/EPS = 1 - 1.13/2.45 = 53.88% <sup>l</sup> If ABN Amro can maintain its current ROE and retention ratio, its expected growth in EPS will be:

Expected Growth Rate = 0.5388 (15.79%) = 8.51%

# Expected ROE changes and Growth

<sup>l</sup> Assume now that ABN Amro's ROE next year is expected to increase to 17%, while its retention ratio remains at 53.88%. What is the new expected long term growth rate in earnings per share? <sup>l</sup> Will the expected growth rate in earnings per share next year be greater than, less than or equal to this estimate? <sup>o</sup> greater than <sup>o</sup> less than <sup>o</sup> equal to

# Changes in ROE and Expected Growth

<sup>l</sup> When the ROE is expected to change,

$$g_{\text{EPS}} = b * \text{ROE}_{t+1} + \{(\text{ROE}_{t+1} - \text{ROE}_t) \text{BV of Equity}_t / \text{ROE}_t (\text{BV of Equity}_t)\}$$

- <sup>l</sup> Proposition 2: Small changes in ROE translate into large changes in the expected growth rate.
- Corollary: The larger the existing asset base, the bigger the effect on earnings growth of changes in ROE. <sup>l</sup> Proposition 3: No firm can, in the long term, sustain growth in earnings per share from improvement in ROE.
  - Corollary: The higher the existing ROE of the company (relative to the business in which it operates) and the more competitive the business in which it operates, the smaller the scope for improvement in ROE.

#### Changes in ROE: ABN Amro

<sup>l</sup> Assume now that ABN's expansion into Asia will push up the ROE to 17%, while the retention ratio will remain 53.88%. The expected growth rate in that year will be:

$$\begin{aligned} g_{EPS} &= b * ROE_{t+1} + (ROE_{t+1} - ROE_t)(BV \text{ of Equity}_t) / ROE_t (BV \text{ of Equity}_t) \\ &= (.5388)(.17) + (.17 - .1579)(25,066) / ((.1579)(25,066)) \\ &= 16.83\% \end{aligned}$$

<sup>l</sup> Note that 1.21% improvement in ROE translates into amost a doubling of the growth rate from 8.51% to 16.83%.

# ROE and Leverage

<sup>l</sup> ROE = ROC + D/E (ROC - i (1-t))

where,

$$\begin{aligned} \text{ROC} &= (\text{Net Income} + \text{Interest (1 - tax rate)}) / \text{BV of Capital} \\ &= \text{EBIT (1- t)} / \text{BV of Capital} \end{aligned}$$

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / BV of Debt

t = Tax rate on ordinary income

<sup>l</sup> Note that BV of Assets = BV of Debt + BV of Equity.

#### Decomposing ROE: Brahma

- <sup>l</sup> Real Return on Capital = 687 (1-.32) / (1326+542+478) = 19.91%
- This is assumed to be real because both the book value and income are inflation adjusted. <sup>l</sup> Debt/Equity Ratio = (542+478)/1326 = 0.77 <sup>l</sup> After-tax Cost of Debt = 8.25% (1-.32) = 5.61% (Real BR) <sup>l</sup> Return on Equity = ROC + D/E (ROC - i(1-t)) 19.91% + 0.77 (19.91% - 5.61%) = 30.92%

# Decomposing ROE: Titan Watches

<sup>l</sup> Return on Capital = 713 (1-.25)/(1925+2378+1303) = 9.54% <sup>l</sup> Debt/Equity Ratio = (2378 + 1303)/1925 = 1.91 <sup>l</sup> After-tax Cost of Debt = 13.5% (1-.25) = 10.125% <sup>l</sup> Return on Equity = ROC + D/E (ROC - i(1-t)) 9.54% + 1.91 (9.54% - 10.125%) = 8.42%

# Expected Growth in EBIT And Fundamentals

<sup>l</sup> When looking at growth in operating income, the definitions are Reinvestment Rate = (Net Capital Expenditures + Change in WC)/EBIT(1-t) Return on Investment = ROC = EBIT(1-t)/(BV of Debt + BV of Equity) <sup>l</sup> Reinvestment Rate and Return on Capital gEBIT = (Net Capital Expenditures + Change in WC)/EBIT(1-t) \* ROC = Reinvestment Rate \* ROC <sup>l</sup> Proposition 4: No firm can expect its operating income to grow over time without reinvesting some of the operating income in net capital expenditures and/or working capital. <sup>l</sup> Proposition 5: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.

# No Net Capital Expenditures and Long Term Growth

<sup>l</sup> You are looking at a valuation, where the terminal value is based upon the assumption that operating income will grow 3% a year forever, but there are no net cap ex or working capital investments being made after the terminal year. When you confront the analyst, he contends that this is still feasible because the company is becoming more efficient with its existing assets and can be expected to increase its return on capital over time. Is this a reasonable explanation? <sup>o</sup> Yes <sup>o</sup> No <sup>l</sup> Explain.

# Estimating Growth in EBIT: Disney

<sup>l</sup> Reinvestment Rate = 50% <sup>l</sup> Return on Capital =18.69% <sup>l</sup> Expected Growth in EBIT =.5(18.69%) = 9.35%

# Estimating Growth in EBIT: Hansol Paper

<sup>l</sup> Net Capital Expenditures = (150,000-45000) = 105,000 Million WN (I normalized capital expenditures to account for lumpy investments) <sup>l</sup> Change in Working Capital = 1000 Million WN <sup>l</sup> Reinvestment Rate = (105,000+1,000)/(109,569\*.7) = 138.20% <sup>l</sup> Return on Capital = 6.76% <sup>l</sup> Expected Growth in EBIT = 6.76% (1.382) = 9.35%

# A Profit Margin View of Growth

<sup>l</sup> The relationship between growth and return on investment can also be framed in terms of profit margins: <sup>l</sup> In the case of growth in EPS

Growth in EPS = Retention Ratio \* ROE = Retention Ratio\*Net Income/Sales \* Sales/BV of Equity = Retention Ratio \* Net Margin \* Equity Turnover Ratio

Growth in EBIT = Reinvestment Rate \* ROC = Reinvestment Rate \* EBIT(1-t)/ BV of Capital = Reinvestment Rate \* AT Operating Margin \* Capital Turnover Ratio

# IV. Growth Patterns

#### Discounted Cashflow Valuation

# Stable Growth and Terminal Value

<sup>l</sup> When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

g = Expected growth rate

<sup>l</sup> This "constant" growth rate is called a stable growth rate and cannot be higher than the growth rate of the economy in which the firm operates. <sup>l</sup> While companies can maintain high growth rates for extended periods, they will all approach "stable growth" at some point in time. <sup>l</sup> When they do approach stable growth, the valuation formula above can be used to estimate the "terminal value" of all cash flows beyond.

#### Growth Patterns

- <sup>l</sup> A key assumption in all discounted cash flow models is the period of high growth, and the pattern of growth during that period. In general, we can make one of three assumptions:
  - there is no high growth, in which case the firm is already in stable growth
  - there will be high growth for a period, at the end of which the growth rate will drop to the stable growth rate (2-stage)
  - there will be high growth for a period, at the end of which the growth rate will decline gradually to a stable growth rate(3-stage)

![](_page_140_Figure_2.jpeg)

# Determinants of Growth Patterns

#### <sup>l</sup> Size of the firm

- Success usually makes a firm larger. As firms become larger, it becomes much more difficult for them to maintain high growth rates

#### <sup>l</sup> Current growth rate

- While past growth is not always a reliable indicator of future growth, there is a correlation between current growth and future growth. Thus, a firm growing at 30% currently probably has higher growth and a longer expected growth period than one growing 10% a year now.

#### <sup>l</sup> Barriers to entry and differential advantages

- Ultimately, high growth comes from high project returns, which, in turn, comes from barriers to entry and differential advantages.
- The question of how long growth will last and how high it will be can therefore be framed as a question about what the barriers to entry are, how long they will stay up and how strong they will remain.

# Stable Growth and Fundamentals

<sup>l</sup> The growth rate of a firm is driven by its fundamentals - how much it reinvests and how high project returns are. As growth rates approach "stability", the firm should be given the characteristics of a stable growth firm.

| Model | High Growth Firms usually  | Stable growth firms usually |
|-------|----------------------------|-----------------------------|
| DDM   | 1. Pay no or low dividends | 1. Pay high dividends       |
|       | 2. Have high risk          | 2. Have average risk        |
|       | 3. Earn high ROC           | 3. Earn ROC closer to WACC  |
| FCFE/ | 1. Have high net cap ex    | 1. Have lower net cap ex    |
| FCFF  | 2. Have high risk          | 2. Have average risk        |
|       | 3. Earn high ROC           | 3. Earn ROC closer to WACC  |
|       | 4. Have low leverage       | 4. Have leverage closer to  |

# The Dividend Discount Model: Estimating Stable Growth Inputs

<sup>l</sup> Consider the example of ABN Amro. Based upon its current return on equity of 15.79% and its retention ratio of 53.88%, we estimated a growth in earnings per share of 8.51%. <sup>l</sup> Let us assume that ABN Amro will be in stable growth in 5 years. At that point, let us assume that its return on equity will be closer to the average for European banks of 15%, and that it will grow at a nominal rate of 5% (Real Growth + Inflation Rate in NV) <sup>l</sup> The expected payout ratio in stable growth can then be estimated as follows:

Stable Growth Payout Ratio = 1 - g/ ROE = 1 - .05/.15 = 66.67%

g = b (ROE)

b = g/ROE

Payout = 1- b

# The FCFE/FCFF Models: Estimating Stable Growth Inputs

<sup>l</sup> To estimate the net capital expenditures in stable growth, consider the growth in operating income that we assumed for Disney. The reinvestment rate was assumed to be 50%, and the return on capital was assumed to be 18.69%, giving us an expected growth rate of 9.35%. <sup>l</sup> In stable growth (which will occur 10 years from now), assume that Disney will have a return on capital of 16%, and that its operating income is expected to grow 5% a year forever.

Reinvestment Rate = Growth in Operating Income/ROC = 5/16

<sup>l</sup> This reinvestment rate includes both net cap ex and working capital.

Estimated EBIT (1-t) in year 11 = \$ 9,098 Million

Reinvestment = \$9,098(5/16) = \$2,843 Million

Net Capital Expenditures = Reinvestment - Change in Working Capital<sup>11</sup> = \$ 2,843m -105m = 2,738m