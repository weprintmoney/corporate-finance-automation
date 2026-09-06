---
title: "Chapter 5 Derivations"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/CFTheory/deriv/ch5deriv.html
---

Chapter 5 Derivations

### *Discussion Issues and Derivations*

1. *A Derivation of the Capital Asset Pricing Model   
   I. Establish the Objects of Choice: Mean versus Variance*  
   Theme: Investors are risk averse. They measure reward using expected return and risk using variance.   
   Underlying assumptions: The mean-variance assumption can hold only if (a) all investors have quadratic utility function or (b) returns are normally distributed.  
   Implication: Portfolio A with higher expected return and the same variance as portfolio B will be preferred to B  
   *II. Benefits of Diversification*  
   For any desired level of risk (s) there exists a portfolio of several assets which yields a higher expected return than any individual security  
   E(Rp) = S wi E(Ri)  
   s2p = S S wi wj Covij  
   Efficient portfolios: maximize returns for any level of risk.  
   Implications: (a) Everybody should diversify (b) Investors should try to identify and hold efficient portfolios (c) This method has very heavy computational requirements.  
   *III. The Single Index Model: The Logical Limit of Diversification*  
   Assumptions: (a) Riskfree lending and borrowing (b) Markets which are frictionless - there are no transactions costs (c)Homogeneous expectations  
   Implications: (1) The risky portfolio than when combined with the riskless asset maximizes returns is the market portfolio. (2) Everybody holds some combination of the market portfolio and the risky asset. How much of each is held will be a function of the investor's risk aversion.(3) Since all investors hold the same market portfolio it must contain all assets in the economy in proportion to their value.  
   *IV. The Risk of an Individual Asset*  
   Step 1: Individuals diversify and hold portfolios  
   Step 2: The risk of a security is the risk it adds to the portfolio  
   Step 3: Everybody holds the market portfolio  
   Step 4: The risk of a security is the risk that it adds to the market portfolio.  
   Step 5: The covariance between an asset "i" and the market portfolio (Covim) is a measure of this added risk. The higher the covariance the higher the risk.  
   Step 6: This measure can be standardized by dividing by the market variance. b = Covim/ s2m.

- *Variants of the Capital Asset Pricing Model**I. No Riskless Asset*  
  Basis: If no riskless asset exists investors can use a portfolio of risky assets which is uncorrelated with the market portfolio instead as the riskless asset. This portfolio is called the zero-beta portfolio.  
  Properties of the Zero-beta portfolio  
  (1) Of all the the zero-beta portfolios this has the minimum variance  
  (2) The separation principle applies here with the two portfolios, the market portfolio and the zero-beta portfolio, i.e. all investors hold combinations of the two.  
  (3) The expected return on any security can be expressed as a linear function of its beta.  
  E(Ri) = E(Rz) + b (E(Rm) - E(Rz))  
  where E(Rz) is the expected return on a zero beta portfolio  
  *II. Riskless Lending but no Riskless Borrowing*  
  Basis:   
  (a) There is a piecewise linear relationship between expected return and beta for efficient portfolios.  
  (b) Efficient portfolios with the riskfree asset lie along the segment RfT and those containing only risky assets lies along the segment TMC.  
  *III. Existence of Non-Marketable Assets (such as Human Capital)*  
  The separation principle still holds but,  
  (a) Investors hold different portfolios of risky assets depending upon the portfolios of non-marketable assets that they possess.  
  (b) The market price of risk includes the variance of the market and the covariance between the market portfolio and the portfolio of non-marketable assets  
  *IV. Existence of Taxes*  
  Model: The model considers differential taxes on dividends and capital gains in a one-period context where investors maximize their one-period returns. The final model for expected return has a dividend component  
  E(Ri) = a + bi (E(Rm) - Rf) + c (di - Rf)  
  where di = Dividend yield on asset i  
  Rf = After-tax riskfree rate  
  *V. Existence of Heterogeneous Expectations and Information*  
  Model: To get strong conclusions we have to assume that all investors have a certain class of utility functions (Constant Absolute risk aversion) and complete markets (At least as many independent securities as states).   
  - *Testing the CAPM: Issues and Discussion   
    Issue 1: The CAPM can never be tested because the market portfolio can never be observed*  
    Central to the CAPM is the concept of a market portfolio which includes every asset in the economy. To test the CAPM therefore one has to observe and be able to measure this efficient market portfolio. If one cannot do so one cannot test the CAPM. One cannot use of an inefficient portfolio like the S&P 500 or the NYSE 2000 or even every stock in the economy to estimate betas and test for linearity (like all the studies have done) because   
    (a) The betas measured against an inefficient portfolio are meaningless measures and cannot be used to accept or reject the CAPM which is really a theory about betas measured against the efficient market portfolio  
    (b) For every inefficient portfolio there exists a set of betas which will satisfy the linearity condition.   
    *Issue 2: The CAPM is difficult to test on individual assets*  
    The noisiness in beta estimates and the fact that the CAPM yields expected returns for individual assets over the long term makes it difficult to test the CAPM by trying to relate expected returns on individual assets (such as stocks) to their betas. What most tests of the CAPM do instead is to look at portfolios of stocks, based upon betas, and then compare these betas to expected returns in the next time period.  
    - *More on Factor Analysis and the Arbitrage Pricing Model*Central to applying the arbitrage pricing model is the use of a factor analysis. In a typical factor analysis, we begin with pricing data on a large number of assets over very long time periods. In the factor analysis, we look for factors that seem to move prices on large numbers of assets in unison. To prevent factors from being double counted, we ensure that the factors that emerge are independent of each other. While all of this occurs behind the screen of the factor analysis, what emerges as output from the analysis includes:  
      (a) the number of common factors that appeared to affect asset prices over the period for which the data is available  
      (b) the betas of each asset relative to each factor, again using the same data  
      (c) the "risk premiums" associated with each factor  
      These factor betas and factor premiums are then used, in conjunction with a riskfree rate to get an expected return for an asset.- *Estimating the Macro Economic Factors in a Multi-Factor Model*Once the number of factors have been identified in an arbitrage pricing model, the time series behavior of each factor can be derived from the factor analysis. The search then begins for macro economic factors that exhibit the same time series behavior. Once macro economic factors have been matched up with the unnamed factors in the factor analysis, the betas of each asset are re-estimated against the identified macro economic factors. The beta estimation may be done by running a multiple regression of stock returns (for each stock) against changes in macro economic variables (such as interest rates, inflation rates and GNP growth) over time. The coefficients on these regressions yield the betas, and risk premiums can be estimated also from the historical data.- *Building a Regression Model*Generally, regression models begin with the cross sectional differences in returns across stocks at any point in time, and try to explain these differences using differences on measurable financial characteristics of the firms issuing these assets. As an example, Fama and French, in their much quoted study, used differences in market capitalization and price to book ratios to explain differences in returns across stocks.  
          The more difficult question is deciding which financial variables to use in explaining returns. The best place to start is to look at the empirical evidence that has been accumulated over time on market efficiency and the CAPM. This evidence suggests that  
          - Low market capitalization stocks seem to earn higher returns, on average, than high market capitalization stocks  
          - Low PE, PBV and PS ratio stocks seem to earn higher returns, on average, than high PE, PBV and PS ratio stocks  
          - High dividend yield stocks seem to earn higher returns, on average, than low dividend yield stocks  
          While the initial regression may include all of these variables, many of these variables tend to be correlated with each other. Thus, low PE stocks tend to also be low PBV ratio stocks which pay high dividends. In the interests of efficiency (and to prevent problems in the regression from independent variables being correlated with each other), it makes sense to use the measure that is most highly correlated with returns and drop the others. Thus, the use of price to book value ratios by Fama and French.- *Why not use bond betas to arrive at the cost of debt?*Given that we use stock betas to arrive at expected returns for stocks, the question may arise as to why we do not use bond betas to get expected returns for bonds. The reason lies in the absence or presence of symmetry in returns for each of these asset classes. Stocks, which have potentially unlimited upside potential as well as significant downside potential, have much more symmetric returns than bonds. Thus, they tend to fit in much more cleanly into the mean-variance framework than do bonds.   
            Corporate bonds have some upside potential, but it is limited by the fact that bonds can at best become default-free. Thus, the upside potential for a AA rated bond is fairly limited. Consequently, the risk measure that we have to use has to be a downside risk measure, which is what default risk and ratings measure. Clearly, the lower the rating of a bond, the greater the upside potential, and thus, the greater the likelihood that we can estimate bond betas and expected returns on them. For a junk bond, for instance, it may be possible to estimate a beta like a stock beta and get an expected return from it.- *Credit Scores as Alternatives to Bond Ratings*Bond ratings are a tool that we use to measure default risk and arrive at a cost of debt. Lenders (such as banks) have historically used credit scores as a measure of default risk, especially when lending to individuals and private businessess. A credit score is derived by measuring how a borrower scores on a variety of measures, which over time have been correlated with default risk.
