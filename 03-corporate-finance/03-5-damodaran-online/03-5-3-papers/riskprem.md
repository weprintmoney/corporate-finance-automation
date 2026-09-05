---
title: "Riskprem"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/papers/riskprem.pdf
---

# **Estimating Equity Risk Premiums**

Aswath Damodaran

Stern School of Business

44 West Fourth Street

New York, NY 10012

Adamodar@stern.nyu.edu

# **Estimating Equity Risk Premiums**

Equity risk premiums are a central component of every risk and return model in finance.

Given their importance, it is surprising how haphazard the estimation of equity risk premiums remains in practice. The standard approach to estimating equity risk premiums remains the use of historical returns, with the difference in annual returns on stocks and bonds over a long time period comprising the expected risk premium, looking forward.

We note the limitations of this approach, even in markets like the United States, which have long periods of historical data available, and its complete failure in emerging markets, where the historical data tends to limited and noisy. We suggest ways in which equity risk premiums can be estimated for these markets, using a base equity premium and a country risk premium. Finally, we suggest an alternative approach to estimating equity risk premiums that requires no historical data and provides updated estimates for most markets.

# **Equity Risk Premiums**

The notion that risk matters, and that riskier investments should have a higher expected return than safer investments, to be considered good investments, is intuitive. Thus, the expected return on any investment can be written as the sum of the riskfree rate and an extra return to compensate for the risk. The disagreement, in both theoretical and practical terms, remains on how to measure this risk, and how to convert the risk measure into an expected return that compensates for risk. This paper looks at the estimation of an appropriate risk premium to use in risk and return models, in general, and in the capital asset pricing model, in particular.

# *Risk and Return Models*

While there are several competing risk and return models in finance, they all share some common views about risk. First, they all define risk in terms of variance in actual returns around an expected return; thus, an investment is riskless when actual returns are always equal to the expected return. Second, they all argue that risk has to be measured from the perspective of the marginal investor in an asset, and that this marginal investor is well diversified. Therefore, the argument goes, it is only the risk that an investment adds on to a diversified portfolio that should be measured and compensated.

In fact, it is this view of risk that leads risk models to break the risk in any investment into two components. There is a firm-specific component that measures risk that relates only to that investment or to a few investments like it, and a market component that contains risk that affects a large subset or all investments. It is the latter risk that is not diversifiable and should be rewarded.

While all risk and return models agree on this fairly crucial distinction, they part ways when it comes to how measure this market risk. The following table summarizes four models, and the way each model attempts to measure risk:

|                               | Assumptions                                                                                                                                                             | Measure of Market Risk                                                           |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| The CAPM                      | There are no transactions costs or private information. Therefore, the diversified portfolio includes all traded investments, held in proportion to their market value. | Beta measured against this market portfolio.                                     |
| Arbitrage pricing model (APM) | Investments with the same exposure to market risk have to trade at the same price (no arbitrage).                                                                       | Betas measured against multiple (unspecified) market risk factors.               |
| Multi-Factor Model            | Same no arbitrage assumption                                                                                                                                            | Betas measured against multiple macro economic factors.                          |
| Proxy Model                   | Over very long periods, higher returns on investments must be compensation for higher market risk.                                                                      | Proxies for market risk, for example, market capitalization and Price/BV ratios. |

In the first three models, the expected return on any investment can be written as:

$$\text{Expected Return} = \text{Riskfree Rate} + \sum_{j=1}^{j=k} \beta_j(\text{Risk Premium}_j)$$

where  $\beta_j = \text{Beta of investment relative to factor } j$ 

Risk Premium<sup>j</sup> = Risk Premium for factor j

Note that in the special case of a single-factor model, like the CAPM, each investment's expected return will be determined by its beta relative to the single factor.

Assuming that the riskfree rate is known, these models all require two inputs. The first is the beta or betas of the investment being analyzed, and the second is the appropriate risk premium(s) for the factor or factors in the model. While we examine the issue of beta estimation in a companion piece<sup>1</sup> , we will concentrate on the measurement of the risk premium in this paper.

# *What we would like to measure*

We would like to measure how much market risk (or non-diversifiable risk) there is in any investment through its beta or betas. As far as the risk premium is concerned, we would like to know what investors, on average, require as a premium over the riskfree rate for an investment with average risk, for each factor.

Without any loss of generality, let us consider the estimation of the beta and the risk premium in the capital asset pricing model. Here, the beta should measure the risk added on by the investment being analyzed to a portfolio, diversified not only within asset classes but across asset classes. The risk premium should measure what investors,

 1 See "Estimating Risk Parameters, Aswath Damodaran". http://www.stern.nyu.edu/~adamodar.

on average, demand as extra return for investing in this portfolio relative to the riskfree asset.

#### *What we do in practice…*

In practice, however, we compromise on both counts. We estimate the beta of an asset relative to the local stock market index, rather than a portfolio that is diversified across asset classes. This beta estimate is often noisy and a historical measure of risk. We estimate the risk premium by looking at the historical premium earned by stocks over default-free securities over long time periods. These approaches might yield reasonable estimates in markets like the United States, with a large and diverisified stock market and a long history of returns on both stocks and government bonds. We will argue, however, that they yield meaningless estimates for both the beta and the risk premium in other countries, where the equity markets represent a small proportion of the overall economy, and the historical returns can be reliably estimated only for short periods.

### *The Historical Premium Approach: An Examination*

The historical premium approach, which remains the standard approach when it comes to estimating risk premiums, is simple. The actual returns earned on stocks over a long time period is estimated, and compared to the actual returns earned on a default-free (usually government security). The difference, on an annual basis, between the two returns is computed and represents the historical risk premium

While users of risk and return models may have developed a consensus that historical premium is, in fact, the best estimate of the risk premium looking forward, there are surprisingly large differences in the actual premiums we observe being used in practice. For instance, the risk premium estimated in the US markets by different investment banks, consultants and corporations range from 4% at the lower end to 12% at the upper end. Given that we almost all use the same database of historical returns, provided by Ibbotson Associates<sup>2</sup> , summarizing data from 1926, these differences may seem surprising. There are, however, three reasons for the divergence in risk premiums:

- a. Time Period Used: While there are many who use all the data going back to 1926, there are almost as many using data over shorter time periods, such as fifty, twenty or even ten years to come up with historical risk premiums. The rationale presented by those who use shorter periods is that the risk aversion of the average investor is likely to change over time, and that using a shorter time period provides a more updated estimate. This has to be offset against a cost associated with using shorter time periods, which is the greater noise in the risk premium estimate. In fact, given the annual standard deviation in stock prices<sup>3</sup> between 1926 and 1997 of 20%, the standard error<sup>4</sup> associated with the risk premium estimate can be estimated as follows for different estimation periods:

| Estimation Period | Standard Error of Risk Premium Estimate |   |            |
|-------------------|-----------------------------------------|---|------------|
| 5 years           | 20%/                                    | Ö | 5 = 8.94%  |
| 10 years          | 20%/                                    | Ö | 10 = 6.32% |
| 25 years          | 20% /                                   | Ö | 25 = 4.00% |
| 50 years          | 20% /                                   | Ö | 50 = 2.83% |

 2 See "Stocks, Bonds, Bills and Inflation", an annual edition that reports on annual returns on stocks, treasury bonds and bills, as well as inflation rates from 1926 to the present. (http://www.ibbotson.com)

<sup>3</sup> For the historical data on stock returns, bond returns and bill returns check under "updated data" in www.stern.nyu.edu/~adamodar

<sup>4</sup> These estimates of the standard error are probably understated, because they are based upon the assumption that annual returns are uncorrelated over time. There is substantial empirical evidence that returns are correlated over time, which would make this standard error estimate much larger.

Note that to get reasonable standard errors, we need very long time periods of historical returns. Conversely, the standard errors from ten-year and twenty-year estimates are likely to almost as large or larger than the actual risk premium estimated. This cost of using shorter time periods seems, in our view, to overwhelm any advantages associated with getting a more updated premium.

- b. Choice of Riskfree Security: The Ibbotson database reports returns on both treasury bills and treasury bonds, and the risk premium for stocks can be estimated relative to each. Given that the yield curve in the United States has been upward sloping for most of the last seven decades, the risk premium is larger when estimated relative to shorter term government securities (such as treasury bills). The riskfree rate chosen in computing the premium has to be consistent with the riskfree rate used to compute expected returns. Thus, if the treasury bill rate is used as the riskfree rate, the premium has to be the premium earned by stocks over that rate. If the treasury bond rate is used as the riskfree rate, the premium has to be estimated relative to that rate. I have argued in a companion piece<sup>5</sup> that the riskfree rate used has to match up the duration of the cashflows being discounted. For the most part, in corporate finance and valuation, the riskfree rate will be a long term default-free (government) bond rate and not a treasury bill rate. Thus, the risk premium used should be the premium earned by stocks over treasury bonds.
- c. Arthmetic and Geometric Averages: The final sticking point when it comes to estimating historical premiums relates to how the average returns on stocks, treasury

bonds and bills are computed. The arithmetic average return measures the simple mean of the series of annual returns, whereas the geometric average looks at the compounded return<sup>6</sup> . Conventional wisdom argues for the use of the arithmetic average. In fact, if annual returns are uncorrelated over time, and our objective were to estimate the risk premium for the next year, the arithmetic average is the best unbiased estimate of the premium. In reality, however, there are strong arguments that can be made for the use of geometric averages. First, empirical studies seem to indicate that returns on stocks are negatively correlated<sup>7</sup> over time. Consequently, the arithmetic average return is likely to over state the premium. Second, while asset pricing models may be single period models, the use of these models to get expected returns over long periods (such as five or ten years) suggests that the single period may be much longer than a year. In this context, the argument for geometric average premiums becomes even stronger.

In summary, the risk premium estimates vary across users because of differences in time periods used, the choice of treasury bills or bonds as the riskfree rate and the use of arithmetic as opposed to geometric averages. The effect of these choices is summarized in the table below, which uses returns from 1926 to 1997.

| <span></span>     | <span></span>           | <span></span>    | <span></span> |
|-------------------|-------------------------|------------------|---------------|
| Historical period | Stocks - Treasury Bills | Stocks - T.Bonds |               |
|                   | Arithmetic              | Arithmetic       | Geometric     |

 5 "The Right Riskfree Rate to Use in Asset Pricing Models: A Note", September 1998., www.stern.nyu.edu/~adamodar.

$$\text{Geometric Average} = \left( \frac{\text{Value}_N}{\text{Value}_0} \right)^{1/N} - 1$$

<sup>6</sup> The compounded return is computed by taking the value of the investment at the start of the period (Value<sup>0</sup> ) and the value at the end (ValueN), and then computing the following:

<sup>7</sup> In other words, good years are more likely to be followed by poor years, and vice versa. The evidence on negative serial correlation in stock returns over time is extensive, and can be found in Fama and French (1988). While they find that the one-year correlations are low, the five-year serial correlations are strongly negative for all size classes.

| 1926-1997 | 9.05%  | 7.13%  | 7.73% | 6.10% |
|-----------|--------|--------|-------|-------|
| 1962-1997 | 6.21%  | 5.64%  | 5.55% | 5.48% |
| 1981-1997 | 11.56% | 12.02% | 9.56% | 9.07% |

Note that the premiums can range from 5 to 12%, depending upon the choices made. In fact, these differences are exacerbated by the fact that many risk premiums that are in use today were estimated using historical data three, four or even ten years ago.

![](_page_9_Picture_2.jpeg)

There is a dataset on the web that summarizes historical returns on stocks, T.Bonds and T.Bills in the United States going back to 1926.

### *The Historical Risk Premium Approach: Some Caveats*

Given how widely the historical risk premium approach is used, it is surprising how flawed it is and how little attention these flaws have received. Consider first the underlying assumption that investors' risk premiums have not changed over time and that the average risk investment (in the market portfolio) has remained stable over the period examined. We would be hard pressed to find anyone who would be willing to sustain this argument with fervor.

The obvious fix for this problem, which is to use a more recent time period, runs directly into a second problem, which is the large noise associated with risk premium estimates. While these standard errors may be tolerable for very long time periods, they clearly are unacceptably high when shorter periods are used.

Finally, even if there is a sufficiently long time period of history available, and investors' risk aversion has not changed in a systematic way over that period, there is a

final problem. Markets that exhibit this characteristic, and let us assume that the US market is one such example, represent "survivor markets". In other words, assume that one had invested in the ten largest equity markets in the world in 1926, of which the United States was one. In the period extending from 1926 to 1997, investments in none of the other equity markets would have earned as large a premium as the US equity market, and some of them (like Austria) would have resulted in investors earning little or even negative returns over the period. Thus, the survivor bias will result in historical premiums that are larger than expected premiums for markets like the United States, even assuming that investors are rational and factor risk into prices.

# *Historical Risk Premiums: Other Markets*

If it is difficult to estimate a reliable historical premium for the US market, it becomes doubly so when looking at markets with short and volatile histories. This is clearly true for emerging markets, but it is also true for the European equity markets. While the economies of Germany, Italy and France may be mature, their equity markets do not share the same characteristic. They tend to be dominated by a few large companies, many businesses remain private, and trading, until recently, tended to be thin except on a few stocks.

There are some practitioners who still use historical premiums for these markets. To capture some of the danger in this practice, I have summarized historical risk premiums<sup>8</sup> for major non-US markets below for 1970-1996:

|           |                | <i>Equity</i>    | <i>Bonds</i>  | <i>Risk Premium</i>  |                      |
|-----------|----------------|------------------|---------------|----------------------|----------------------|
|           | <i>Country</i> | <i>Beginning</i> | <i>Ending</i> | <i>Annual Return</i> | <i>Annual Return</i> |
| Australia | 100            | 898.36           | 8.47%         | 6.99%                | 1.48%                |

 8 This data is also from Ibbotson Associcates, and can be obtained from their web site: http://www.ibbotson.com.

| Canada      | 100 | 1020.7   | 8.98%  | 8.30%  | 0.68%  |
|-------------|-----|----------|--------|--------|--------|
| France      | 100 | 1894.26  | 11.51% | 9.17%  | 2.34%  |
| Germany     | 100 | 1800.74  | 11.30% | 12.10% | -0.80% |
| Hong Kong   | 100 | 14993.06 | 20.39% | 12.66% | 7.73%  |
| Italy       | 100 | 423.64   | 5.49%  | 7.84%  | -2.35% |
| Japan       | 100 | 5169.43  | 15.73% | 12.69% | 3.04%  |
| Mexico      | 100 | 2073.65  | 11.88% | 10.71% | 1.17%  |
| Netherlands | 100 | 4870.32  | 15.48% | 10.83% | 4.65%  |
| Singapore   | 100 | 4875.91  | 15.48% | 6.45%  | 9.03%  |
| Spain       | 100 | 844.8    | 8.22%  | 7.91%  | 0.31%  |
| Switzerland | 100 | 3046.09  | 13.49% | 10.11% | 3.38%  |
| UK          | 100 | 2361.53  | 12.42% | 7.81%  | 4.61%  |

Note that a couple of the countries have negative historical risk premiums, and a few others have risk premiums under 1%. Before we attempt to come up with rationale for why this might be so, it is worth noting that the standard errors on each and every one of these estimates is larger than 5%, largely because the estimation period includes only 26 years.

If the standard errors on these estimates make them close to useless, consider how much more noise there is in estimates of historical risk premiums for emerging market equity markets, which often have a reliable history of ten years or less, and very large standard deviations in annual stock returns. Historical risk premiums for emerging markets may provide for interesting anecdotes, but they clearly should not be used in risk and return models.

# *A Modified Historical Risk Premium*

While historical risk premiums for markets outside the United States cannot be used in risk models, we still need to estimate a risk premium for use in these markets. To approach this estimation question, let us start with the basic proposition that the risk premium in any equity market can be written as:

Equity Risk Premium = Base Premium for Mature Equity Market + Country Premium

The country premium could reflect the extra risk in a specific market. This boils down our estimation to answering two questions:

- a. What should the base premium for a mature equity market be?
- b. Should there be a country premium, and if so, how do we estimate the premium?

To answer the first question, we will make the argument that the US equity market is a mature market, and that there is sufficient historical data in the United States to make a reasonable estimate of the risk premium. In fact, reverting back to our discussion of historical premiums in the US market, we will use the geometric average premium earned by stocks over treasury bonds of 6.10% between 1926 and 1998. We chose the long time period to reduce standard error, the treasury bond to be consistent with our choice of a riskfree rate and geometric averages to reflect our desire for a risk premium that we can use for longer term expected returns.

On the issue of country premiums, there are some who argue that country risk is diversifiable, and that there should be no country risk premium. While this might be true if equity markets across countries were uncorrelated, the last few months have brought clear evidence of cross-market correlation. In other words, a significant portion of country risk seems to be systematic and non-diversifiable even in a global portfolio. To estimate the country risk premium, however, we need to

- a. measure country risk (and)
- b. convert the country risk measure into a country risk premium, and

c. evaluate how individual companies in that country are exposed to country risk

#### *a. Measuring Country Risk*

While there are several measures of country risk, one of the simplest and most easily accessible is the rating assigned to a country's debt by a ratings agency (S&P, Moody's and IBCA all rate countries). These ratings measure default risk (rather than equity risk) but they are affected by many of the factors that drive equity risk – the stability of a country's currency, its budget and trade balances and its political stability, for instance<sup>9</sup> . The other advantage of ratings is that they come with default spreads over the US treasury bond. For instance, the following table summarizes the ratings and default spreads for Latin American countries as on June 1998:

| Country   | Rating | a Corporate Spread | b Country Bond Spread c |
|-----------|--------|--------------------|-------------------------|
| Argentina | BB     | 1.75%              | 2.58%                   |
| Brazil    | BB-    | 2%                 | 2.87%                   |
| Chile     | A-     | 0.75%              | NA                      |
| Columbia  | BBB-   | 1.50%              | NA                      |
| Paraguay  | BB-    | 2%                 | NA                      |
| Peru      | BB     | 1.75%              | 2.04%                   |
| Uruguay   | BBB-   | 1.50%              | 1.68%                   |
| Venezuela | B+     | 2.25%              | 2.60%                   |

<sup>a</sup>Ratings are foreign currency ratings

<sup>b</sup>Corporate bond spreads are estimated looking at US corporate bond yields relative to treasury bond.

<sup>c</sup>Country bond spreads based upon par Brady bond, blended yield over T. Bond.

While a reasonable argument can be made that the country bond spreads are far more likely to reflect the market's current view of risk in the market, we would make a counter argument for using the corporate bond spreads, instead. The corporate bond market is a

 9 The process by which country ratings are obtained in explained on the S&P web site at http://www.ratings.standardpoor.com/criteria/index.htm.

far deeper market, in terms of the number of market participants, than the country bond markets, and thus less volatile on a period by period basis.

While ratings provide a convenient measure of country risk, there are costs associated with using them as the only measure. First, ratings agencies often lag markets when it comes to responding to changes in the underlying default risk. Second, the ratings agency focus on default risk may obscure other risks that could still affect equity markets. What are the alternatives? There are numerical country risk scores that have been developed by some services as much more comprehensive measures of risk. The Economist, for instance, has a score that runs from 0 to 100, where 0 is no risk, and 100 is most risky, that it uses to rank emerging markets. Alternatively, country risk can be estimated from the bottom-up by looking at economic fundamentals in each country. This, of course, requires significantly more information than the other approaches.

### *b. Estimating Country Risk Premium*

The country risk measure is an intermediate step towards estimating the risk premium to use in risk models. The default spreads that come with country ratings provide an important first step, but still only measure the premium for default risk. Intuitively, we would expect the country equity risk premium to be larger than the country default risk spread. To address the issue of how much higher, we look at the volatility of the equity market in a country relative to the volatility of the country bond, used to estimate the spread. This yields the following estimate for the country equity risk premium:

$$\text{Country Equity Risk Premium} = \text{Country Default Spread} \left( * \frac{\sigma_{\text{Equity}}}{\sigma_{\text{Country Bond}}} \right)$$

To illustrate, consider the case of Brazil. In June 1998, Brazil was rated BB- by Standard and Poor's, resulting in a default spread of 2.00% (based upon US corporates with the same rating). The annualized standard deviation in the Brazilian equity index over the previous year was 34.9%, while the annualized standard deviation in the Brazilian par Brady bond was 10.9%. The resulting country equity risk premium for Brazil is as follows:

Brazil's Equity Risk Premium = 2.00% (34.9%/10.9%) = 6.29%

Note that this country risk premium will increase if the country rating drops or if the relative volatility of the equity market increases. It is also worth noting that this premium will not stay constant as we extend the time horizon. Thus, to estimate the equity risk premium to use for a ten-year cash flows, we would use the standard deviations in equity and bond prices over ten years, and the resulting relative volatility will generally be smaller<sup>10</sup>. Thus, the equity risk premium will converge on the country bond spread as we look at longer term expected returns.

# *c. Estimating Asset Exposure to Country Risk Premiums*

Once country risk premiums have been estimated, the final question that we have to address relates to the exposure of individual companies within that country to country risk. There are three alternative views of country risk:

- 1. Assume that all companies in a country are equally exposed to country risk. Thus, for Brazil, where we have estimated a country risk premium of 6.29%, each company in

 <sup>10</sup> Jeremy Siegel reports on the standard deviation in equity markets in his book "Stocks for the very long run", and notes that they tend to decrease with time horizon.

the market will have an additional country risk premium of 6.29% added to its expected returns. For instance, the cost of equity for Aracruz Celulose, a paper and pulp manufacturer listed in Brazil, with a beta of 0.72, in US dollar terms would be (assuming a US treasury bond rate of 5%):

Expected Cost of Equity = 5.00% + 0.72 (6.10%) + 6.29% = 15.68%

Note that the riskfree rate that we use is the US treasury bond rate, and that the 6.10% is the equity risk premium for a mature equity market (estimated from historical data in the US market). It is also worth noting that analysts estimating cost of equity for Brazilian companies, in US dollar terms, often use the Brazilian C-Bond rate, a dollar denominated Brazilian bond, as the riskfree rate. This is dangerous, since it is often also accompanied with a higher risk premium, and ends up double counting risk. It also seems inconsistent to use a rate that clearly incorporates default risk as a riskfree rate.

- 2. Assume that a company's exposure to country risk is proportional to its exposure to all other market risk, which is measured by the beta. For Aracruz, this would lead to a cost of equity estimate of:

Expected Cost of Equity = 5.00% + 0.72 (6.10% + 6.29%) = 13.92%

- 3. The most general, and our preferred approach, is to allow for each company to have an exposure to country risk that is different from its exposure to all other market risk. We will measure this exposure with  $\lambda$ , and estimate the cost of equity for any firm as follows:

Expected Return = 
$$R_f + \text{Beta (Mature Equity Risk Premium)} + \lambda (\text{County Risk Premium})$$

How can we best estimate  $\lambda$ ? I consider this question in far more detail in my companion piece on beta estimation, but I would argue that commodity companies which get most of their revenues in US dollars by selling into a global market should be less exposed than manufacturing companies that service the local markets. Using this rationale, Aracruz, which derives 80% or more of its revenues in the global paper market in US dollars, should be less exposed than the typical Brazilian firm to country risk. Using a  $\lambda$  of 0.25, for instance, we get a cost of equity in US dollar terms for Aracruz of:

Expected Return = 5% + 0.72 (5.5%) + 0.25 (6.29%) =10.53%

![](_page_17_Picture_2.jpeg)

There is a data set on the website that contains the updated ratings for countries and the risk premiums associated with each.

# *An Alternative Approach: Implied Equity Premiums*

There is an alternative to estimating risk premiums that does not require historical data or corrections for country risk, but does assume that the market, overall, is correctly priced. Consider, for instance, a very simple valuation model for stocks:

Value = 
$$\frac{\text{Expected Dividends Next Period}}{(\text{Required Return on Equity} - \text{Expected Growth Rate})}$$

This is essentially the present value of dividends growing at a constant rate. Three of the four inputs in this model can be obtained externally - the current level of the market (value), the expected dividends next period and the expected growth rate in earnings and dividends in the long term. The only "unknown" is then the required return on equity; when we solve for it, we get an implied expected return on stocks. Subtracting out the riskfree rate will yield an implied equity risk premium.

To illustrate, assume that the current level of the S&P 500 Index is 900, the expected dividend yield on the index is 2% and the expected growth rate in earnings and dividends in the long term is 7%. Solving for the required return on equity yields the following:

$$900 = (.02 * 900) / (r - .07)$$

Solving for r,

$$r = (18+63)/900 = 9\%$$

If the current riskfree rate is 6%, this will yield a premium of 3%.

This approach can be generalized to allow for high growth for a period, and extended to cover cash flow based, rather than dividend, models. To illustrate this, consider the S&P 500 Index, as of December 31, 1997. The index was at 985, and the dividend yield on the index was roughly 2%. With stock buybacks in 1997, though, the cash yield on the index was closer to 3%. In addition, the consensus estimate of growth in earnings for companies in the index was approximately 10% for the next 5 years. Since this is not a growth rate that can be sustained forever, we employ a two-stage valuation model, where we allow growth to continue at 10% for 5 years, and then lower the growth rate to a more sustainable nominal growth rate of 5% forever. The following table summarizes the expected cash flows for the next 5 years of high growth, and the first year of stable growth thereafter:

|  | Year | Cash Flow on Index |
|--|------|--------------------|
|  |      |                    |

| 1 | 32.01 |
|---|-------|
| 2 | 35.21 |
| 3 | 38.73 |
| 4 | 42.61 |
| 5 | 46.87 |
| 6 | 49.21 |

<sup>a</sup>Cash flow in the first year = 3% of 985 (1.10)

If we assume that these are reasonable estimates of the cash flows and that the index is correctly priced, then

| Level of Index = 970 | $= \frac{32.01}{(1+r)} + \frac{35.21}{(1+r)^2} + \frac{38.73}{(1+r)^3} + \frac{42.61}{(1+r)^4} + \frac{46.87}{(1+r)^5} + \frac{(49.21/(r-.05))}{(1+r)^6}$ |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

Note that the last term in the equation is the terminal value of the index, based upon the stable growth rate of 5%, discounted back to the present. Solving for r in this equation yields us the required return on equity of 8.95%. The treasury bond rate on December 31, 1997, was approximately 6%, yielding an implied equity premium of 2.95%.

The advantage of this approach is that it is market-driven and current, and does not require any historical data. Thus, it can be used to estimate implied equity premiums in any market, It is, however, bounded by whether the model used for the valuation is the right one and the availability and reliability of the inputs to that model. For instance, the equity risk premium for the Argentine market on September 30, 1998, was estimated from the following inputs. The index (Merval) was at 687.50 and the current dividend yield on the index was 5.60%. Earnings in companies in the index are expected to grow 11% (in US dollar terms) over the next 5 years, and 6% thereafter. These inputs yield a required return on equity of 10.59%, which when compared to the treasury bond rate of 5.14% on that day results in an implied equity premium of 5.45%. For simplicity, we

have used nominal dollar expected growth rates<sup>11</sup> and treasury bond rates, but this analysis could have been done entirely in the local currency.

The implied equity premiums change over time much more than historical risk premiums. In fact, the contrast between these premiums and the historical premiums is best illustrated by graphing out the implied premiums in the S&P 500 going back to 1960:

Implied Risk Premium: U.S. Equities

![](_page_20_Figure_3.jpeg)

In terms of mechanics, we used smooothed historical growth rates in earnings and dividends as our projected growth rates and a two-stage dividend discount model.

Looking at these numbers, we would draw the following conclusions:

 <sup>11</sup> The input that is most difficult to estimate for emerging markets is a long term expected growth rate. For Argentine stocks, I used the average consensus estimate of growth in earnings for the largest Argentine companies which have ADRs listed on them. This estimate may be biased, as a consequence.

a. The implied equity premium has seldom been as high as the historical risk premium.

Even in 1978, when the implied equity premium peaked, the estimate of 6.50% is well below what many practitioners use as the risk premium in their risk and return models. In fact, the average implied equity risk premium has been between about 4% over time. We would argue that this is because of the survivor bias that pushes up historical risk premiums.

b. The implied equity premium did increase during the seventies, as inflation increased.

This does have interesting implications for risk premium estimation. Instead of assuming that the risk premium is a constant, and unaffected by the level of inflation and interest rates, which is what we do with historical risk premiums, it may be more realistic to increase the risk premium as expected inflation and interest rates increases. In fact, an interesting avenue of research would be to estimate the fundamentals that determine risk premiums

c. Finally, the risk premium has been on a downward trend since the early eighties, and

the risk premium at the end of 1997 is at a historical low. Part of the decline can be attributed to a decline in inflation uncertainty and lower interest rates, and part of it, arguably, may reflect other changes in investor risk aversion and characteristics over the period. There is, however, the very real possibility that the risk premium is low because investors have over priced equity.

As a final point, there is a strong tendency towards mean reversion in financial markets. Given this tendency, it is possible that we can end up with a far better estimate of the implied equity premium by looking at not just the current premium, but also at historical data. There are two ways in which we can do this:

- a. We can use the average implied equity premium over longer periods, say ten to fifteen years. Note that we do not need as many years of data here, as we did with the traditional estimate, because the standard errors tend to be smaller.
- b. A more rigorous approach would require relating implied equity risk premiums to fundamental macroeconomic data over the period. For instance, given that implied equity premiums tend to be higher during periods with higher inflation rates (and interest rates), we ran a regression of implied equity premiums against treasury bond rates, and a term structure variable between 1960 and 1997:

| Implied Equity Premium = $2.04\% + 0.2855$ (T.Bond Rate) - .2089 (T.Bond – T.Bill) | (5.61) | (1.79) |
|------------------------------------------------------------------------------------|--------|--------|
|------------------------------------------------------------------------------------|--------|--------|

The regression has significant explanatory power, with an R-squared of 50%, and the t statistics (in brackets under the coefficients) indicate the statistical significance of the independent variables used. Substituting the current treasury bond rate and bond-bill spread into this equation should yield an updated estimate<sup>12</sup> of the implied equity premium.

 <sup>12</sup> On September 30, 1998, for instance, I substituted in the treasury bond rate of 5%, and a spread of 0.8% between the T.Bond and T.Bill rate into the regression equation to get: .0204 +0.2855 (.05) - .2088 (.008) = .0363 or 3.63%

![](_page_23_Picture_0.jpeg)

histimpl.xls: This data set on the web shows the inputs used to calculate the premium in each year for the U.S. market.

![](_page_23_Picture_2.jpeg)

implprem.xls: This spreadsheet allows you to estimate the implied equity premium in a market.

### *Closing Thoughts*

The risk premium is a fundamental and critical component in portfolio management, corporate finance and in valuation. Given its importance, it is surprising that more attention has not been paid in practical terms to estimation issues. In this paper, we considered the conventional approach to estimating risk premiums, which is to use historical returns on equity and government securities, and evaluated some of its weaknesses. We also examined how to extend this approach to emerging markets, where historical data tends to be both limited and volatile.

The alternative to historical premiums is to estimate the equity premium implied by equity prices. This approach does require that we start with a valuation model for equities, and estimate the expected growth and cash flows, collectively, on equity investments. It has the advantage of not requiring historical data and reflecting current market perceptions.