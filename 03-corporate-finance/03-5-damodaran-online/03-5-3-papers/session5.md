---
title: "Session5"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/FoundationsOnline/slides/session5.pdf
---

#### SESSION 5: THE MEASUREMENT OF RISK

![](_page_0_Picture_3.jpeg)

![](_page_0_Picture_4.jpeg)

# We are risk averse… So what?

¨ If we (human beings) were risk neutral, we would accept the risk free rate as our expected return on every investment, settling for expected cash flows as equivalent to guaranteed cash flows. ¨ Since we are risk averse, we demand a risk premium for investing in risky assets. Put differently, we pay less for an expected cash flow, with uncertainty associated with it, than a guaranteed cash flow of equivalent amount. ¨ The essence of risk measurement then becomes coming up with a measure of risk that reflects what we are averse to and converting it into a risk premium.

**1**

# The Mean-Variance Framework

¨ The variance on any investment measures the disparity between actual and expected returns. ¨ Thus, a risk free investment in this framework has actual returns that always equal to the expected return. The greater the variance in an investment, the riskier it is viewed as being. ¨ In the mean variance world, it is assumed that investors pick investments on only two dimensions, the expected return being the positive and the risk being the negative. This is a strong assumption and can hold only if ¤ Returns are normally distributed ¤ Our utility functions (which determine how we view risk) lead us to here.

#### The Importance of Diversification: Risk Types

![](_page_3_Diagram_2.jpeg)

# The Effects of Diversification

- ¨ Firm-specific risk can be reduced, if not eliminated, by increasing the number of investments in your portfolio (i.e., by being diversified). Market-wide risk cannot. This can be justified on either economic or statistical grounds. ¨ On economic grounds, diversifying and holding a larger portfolio eliminates firm-specific risk for two reasons-
  - (a) Each investment is a much smaller percentage of the portfolio, muting the effect (positive or negative) on the overall portfolio.
  - (b) Firm-specific actions can be either positive or negative. In a large portfolio, it is argued, these effects will average out to zero. (For every firm, where something bad happens, there will be some other firm, where something good happens.)

#### A Statistical Proof that Diversification works… An example with two stocks..

|                             |             | Stock 1 | Stock 2 |
|-----------------------------|-------------|---------|---------|
| Average Monthly Return      |             | 1.50%   | 2.50%   |
| ( s 1, ( s 2 )              |             |         |         |
|                             |             | 10%     | 15%     |
| Correlation between Stock 1 | and Stock 2 |         |         |
| ( r 12)                     |             |         |         |

If you put half your money in stock 1 (w1) and half in stock 2 (w2), your portfolio's standard deviation is only 9.81%, lower than the standard deviations of either of the stocks:

Variance of portfolio

$$= w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

$$= (0.5)^2(.10)^2 + (0.5)^2(.15)^2 + 2(.5)(.5)(.10)(.15)(.20) = .009625$$

Standard deviation = 
$$\sqrt{.009625} = .0981$$

# The Magic of Correlation

¨ The less correlated assets are with each other, the more you will benefit from diversification. ¨ The mechanical challenge: As you go from two to three to four to n assets, the number of correlations you have to calculate will increase exponentially. ¨ The marginal benefit: The benefit of adding an asset to a portfolio will decrease as you increase the number of assets in your portfolio.

**6**

# The Role of the Marginal Investor

¨ The marginal investor in a firm is the investor who is most likely to be the buyer or seller on the next trade and to influence the stock price. ¤ Generally speaking, the marginal investor in a stock has to own a lot of stock and also trade a lot. ¤ Since trading is required, the largest investor may not be the marginal investor, especially if he or she is a founder/manager of the firm. ¨ In all risk and return models in finance, we assume that the marginal investor is well diversified.

# The Market Portfolio

- □ Assuming diversification costs nothing (in terms of transactions costs), and that all assets can be traded, the limit of diversification is to hold a portfolio of every single asset in the economy (in proportion to market value). This portfolio is called the market portfolio.
- □ Individual investors will adjust for risk, by adjusting their allocations to this market portfolio and a riskless asset (such as a T-Bill)

*Preferred risk level*

*Allocation decision*

| No risk        | 100% in T-Bills                          |
|----------------|------------------------------------------|
| Some risk      | 50% in T-Bills; 50% in Market Portfolio; |
| Even more risk | 100% in Market Portfolio                 |
| A risk hog..   | Borrow money; Invest in market portfolio |

- □ Every investor holds some combination of the risk free asset and the market portfolio.

# The Risk of an Individual Asset

¨ The risk of any asset is the risk that it adds to the market portfolio Statistically, this risk can be measured by how much an asset moves with the market (called the covariance) ¨ Beta is a standardized measure of this covariance, obtained by dividing the covariance of any asset with the market by the variance of the market. It is a measure of the non- diversifiable risk for any asset can be measured by the covariance of its returns with returns on a market index, which is defined to be the asset's beta. ¨ The required return on an investment will be a linear function of its beta:

Expected Return = Riskfree Rate+ Beta \* (Expected Return on the Market Portfolio - Riskfree Rate)

# Alternatives to the CAPM

¨ Modified versions: There are modified versions of the CAPM that try to selectively ease assumptions about transactions costs or taxes or even distributional assumptions. ¨ Extended versions: In extended versions, you allow for more than one market risk factor. ¤ The arbitrage pricing model allows for many market risk factors but those factors remain unnamed (statistical) ¤ Multifactor models are built around macro economic variables as stand ins for market risk factors. ¨ Proxy models: In proxy models, we look for the characteristics shared by stocks that have earned higher returns in the past and use them as proxies for risk.

#### Risk and Cost of Equity: The role of the marginal investor

¨ Not all risk counts: While the notion that the cost of equity should be higher for riskier investments and lower for safer investments is intuitive, what risk should be built into the cost of equity is the question. ¨ Risk through whose eyes? While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment ¨ The diversification effect: Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (i.e, market or non-diversifiable risk). In effect, it is primarily economic, macro, continuous risk that should be incorporated into the cost of equity.

**11**

Key Event

Risk Measure used

| Risk was considered to be either fated and thus impossible to change or divine providence in which case it could be altered only through prayer or sacrifice.                        | Pre-1494  | None or gut feeling         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------|
| Luca Pacioli posits his puzzle with two gamblers in a coin tossing game                                                                                                              | 1494      |                             |
| Pascal and Fermal solve the Pacioli puzzle and lay foundations for probability estimation and theory                                                                                 | 1654      | Computed Probabilities      |
| Graunt generates life table using data on births and deaths in London                                                                                                                | 1662      |                             |
| Bernoulli states the "law of large numbers", providing the basis for sampling from large populations.                                                                                | 1711      | Sample-based probabilities  |
| de Moivre derives the normal distribution as an approximation to the binomial and Gauss & Laplace refine it.                                                                         | 1738      |                             |
| Bayes published his treatise on how to update prior beliefs as new information is acquired.                                                                                          | 1763      |                             |
| Insurance business develops and with it come actuarial measures of risk, based upon historical data.                                                                                 | 1800s     | Expected loss               |
| Bachelier examines stock and option prices on Paris exchanges and defends his thesis that prices follow a random walk.                                                               | 1900      | Price variance              |
| Standard Statistics Bureau, Moody's and Fitch start rating corporate bonds using accounting information.                                                                             | 1909-1915 | Bond & Stock Ratings        |
| Markowitz lays statistical basis for diversification and generates efficient portfolios for different risk levels.                                                                   | 1952      | Variance added to portfolio |
| Sharpe and Lintner introduce a riskless asset and show that combinations of it and a market portfolio (including all traded assets) are optimal for all investors. The CAPM is born. | 1964      | Market beta                 |
| Risk and return models based upon alternatives to normal distribution - Power law, asymmetric and jump process distributions                                                         | 1960-     |                             |
| Using the "no arbitrage" argument, Ross derives the arbitrage pricing model; multiple market risk factors are derived from the historical data.                                      | 1976      | Factor betas                |
| Macroeconomic variables examined as potential market risk factors, leading the multi-factor model.                                                                                   | 1986      | Macro economic betas        |
| Fama and French, examining the link between stock returns and firm-specific factors conclude that market cap and book to price at better proxies for risk than beta or betas.        | 1992      | Proxies                     |