---
title: "Risk"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/invphiloh/risk.pdf
---

## Understanding Risk

Aswath Damodaran

#### What is Risk?

 Risk, in traditional terms, is viewed as a 'negative'. Webster' s dictionary, for instance, defines risk as "exposing to danger or hazard". The Chinese symbols for risk, reproduced below, give a much better description of risk

# 危機

 The first symbol is the symbol for "danger", while the second is the symbol for "opportunity", making risk a mix of danger and opportunity.

#### Equity Risk

- An equity investment in a business (private or public) entitles you to residual earnings and cashflows. In other words, you are not promised an interest rate but earn whatever is left over after you pay off other investors. Models that try to measure equity risk vary across investors. Broadly speaking, these risk and return models can be categorized as:
  - Theory based models that begin with an economic (and quantitative) definition of risk and derive risk measures based on that definition.
  - Alternative models that are based upon either intuitive or qualitative measures of risk.

#### I. Theory Based Models

 Most theory based models begin by defining risk in terms of variance in actual returns around expected returns. They usually measure risk through the eyes of the marginal investor in equity (rather than the average investor). The marginal investor is an investor who owns a large portion of the equity and trades frequently.

#### A. The Capital Asset Pricing Model

- The capital asset pricing model is the oldest and still the most widely used model for risk in the investment world. It is derived in four steps:
  - Uses variance as a measure of risk
  - Specifies that a portion of variance can be diversified away, and that is only the non-diversifiable portion that is rewarded.
  - Measures the non-diversifiable risk with beta, which is standardized around one.
  - Translates beta into expected return -

Expected Return = Riskfree rate + Beta \* Risk Premium

#### Step 1: The Mean-Variance Framework

 The variance on any investment measures the disparity between actual and expected returns.

![](_page_5_Figure_2.jpeg)

#### Step 2: The Importance of Diversification: Risk Types

![](_page_6_Diagram_2.jpeg)

*Figure 2.3: A Break Down of Risk*

#### The Effects of Diversification

- Firm-specific risk can be reduced, if not eliminated, by increasing the number of investments in your portfolio (i.e., by being diversified). Market-wide risk cannot. This can be justified on either economic or statistical grounds. On economic grounds, diversifying and holding a larger portfolio eliminates firm-specific risk for two reasons-
  - (a) Each investment is a much smaller percentage of the portfolio, muting the effect (positive or negative) on the overall portfolio.
  - (b) Firm-specific actions can be either positive or negative. In a large portfolio, it is argued, these effects will average out to zero. (For every firm, where something bad happens, there will be some other firm, where something good happens.)

#### The Role of the Marginal Investor

 The marginal investor in a firm is the investor who is most likely to be the buyer or seller on the next trade. Since trading is required, the largest investor may not be the marginal investor, especially if he or she is a founder/manager of the firm (Michael Dell at Dell Computers or Bill Gates at Microsoft) In all risk and return models in finance, we assume that the marginal investor is well diversified.

#### Step 3: The Market Portfolio

 Assuming diversification costs nothing (in terms of transactions costs), and that all assets can be traded, the limit of diversification is to hold a portfolio of every single asset in the economy (in proportion to market value). This portfolio is called the market portfolio. Individual investors will adjust for risk, by adjusting their allocations to this market portfolio and a riskless asset (such as a T-Bill)

| Preferred risk level | Allocation decision                                                  |
|----------------------|----------------------------------------------------------------------|
| Some risk            | 50% in T-Bills; 50% in Market Portfolio;                             |
| A little more risk   | 25% in T-Bills; 75% in Market Portfolio                              |
| Even more risk       | 100% in Market Portfolio                                             |
| A risk hog..         | Borrow money; Invest in market portfolio;                            |
|                     | Every investor holds some combination of the risk free asset and the |

#### Step 4: The Risk of an Individual Asset

 The risk of any asset is the risk that it adds to the market portfolio Statistically, this risk can be measured by how much an asset moves with the market (called the covariance) Beta is a standardized measure of this covariance Beta is a measure of the non-diversifiable risk for any asset can be measured by the covariance of its returns with returns on a market index, which is defined to be the asset's beta. The cost of equity will be the required return,

Cost of Equity = 
$$R_f + \text{Equity Beta} * (E(R_m) - R_f)$$

where,

Rf = Riskfree rate

$$E(R_m) = \text{Expected Return on the Market Index}$$

#### Using the CAPM: The basic inputs

- (a) the current risk-free rate
- (b) the expected market risk premium (the premium expected for investing in risky assets over the riskless asset)
- (c) the beta of the asset being analyzed.

#### The Riskfree Rate and Time Horizon

- On a riskfree asset, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. For an investment to be riskfree, i.e., to have an actual return be equal to the expected return, two conditions have to be met –
  - There has to be no default risk, which generally implies that the security has to be issued by the government. Note, however, that not all governments can be viewed as default free.
  - There can be no uncertainty about reinvestment rates, which implies that it is a zero coupon security with the same maturity as the cash flow being analyzed.

#### Riskfree Rate in Practice

 The riskfree rate is the rate on a zero coupon government bond matching the time horizon of the cash flow being analyzed. Theoretically, this translates into using different riskfree rates for each cash flow - the 1 year zero coupon rate for the cash flow in year 2, the 2-year zero coupon rate for the cash flow in year 2 ... Practically speaking, if there is substantial uncertainty about expected cash flows, the present value effect of using time varying riskfree rates is small enough that it may not be worth it.

#### The Bottom Line on Riskfree Rates

 Using a long term government rate (even on a coupon bond) as the riskfree rate on all of the cash flows in a long term analysis will yield a close approximation of the true value. For short term analysis, it is entirely appropriate to use a short term government security rate as the riskfree rate.

#### Measurement of the risk premium

- The risk premium is the premium that investors demand for investing in an average risk investment, relative to the riskfree rate. As a general proposition, this premium should be
  - greater than zero
  - increase with the risk aversion of the investors in that market
  - increase with the riskiness of the " average " risk investment

#### What is your risk premium?

- Assume that stocks are the only risky assets and that you are offered two investment options:
  - a riskless investment (say a Government Security), on which you can make 5%
  - a mutual fund of all stocks, on which the returns are uncertain

How much of an expected return would you demand to shift your money from the riskless asset to the mutual fund?

 Less than 5% Between 5 - 7% Between 7 - 9% Between 9 - 11% Between 11- 13% More than 13%

#### Risk Aversion and Risk Premiums

 If this were the capital market line, the risk premium would be a weighted average of the risk premiums demanded by each and every investor. The weights will be determined by the magnitude of wealth that each investor has. Thus, Warren Bufffet's risk aversion counts more towards determining the "equilibrium" premium than yours' and mine. As investors become more risk averse, you would expect the "equilibrium" premium to increase.

#### Estimating Risk Premiums in Practice

 Survey investors on their desired risk premiums and use the average premium from these surveys. Assume that the actual premium delivered over long time periods is equal to the expected premium - i.e., use historical data Estimate the implied premium in today's asset prices.

#### The Survey Approach

- Surveying all investors in a market place is impractical. However, you can survey a few investors (especially the larger investors) and use these results. In practice, this translates into surveys of money managers' expectations of expected returns on stocks over the next year. The limitations of this approach are:
  - there are no constraints on reasonability (the survey could produce negative risk premiums or risk premiums of 50%)
  - they are extremely volatile
  - they tend to be short term; even the longest surveys do not go beyond one year

#### The Historical Premium Approach

- This is the default approach used by most to arrive at the premium to use in the model In most cases, this approach does the following
  - it defines a time period for the estimation (1926-Present, 1962-Present....)
  - it calculates average returns on a stock index during the period
    - it calculates average returns on a riskless security over the period
      - it calculates the difference between the two
- and uses it as a premium looking forward The limitations of this approach are:
  - it assumes that the risk aversion of investors has not changed in a systematic way across time. (The risk aversion may change from year to year, but it reverts back to historical averages)
  - it assumes that the riskiness of the "risky" portfolio (stock index) has not changed in a systematic way across time.

### Historical Average Premiums for the United States

*What is the right premium?*

 Go back as far as you can. Otherwise, the standard error in the estimate will be large. Be consistent in your use of a riskfree rate. Use arithmetic premiums for one-year estimates of costs of equity and geometric premiums for estimates of long term costs of equity.

| " "       | Stocks - T. Bills | Arithmetic Average Stocks - T. Bonds | Stocks - T. Bills | Geometric Average Stocks - T. Bonds |
|-----------|-------------------|--------------------------------------|-------------------|-------------------------------------|
| 1928-2011 | 7.55%             | 5.79%                                | 5.62%             | 4.10%                               |
| "         | 2.22%             | 2.36%                                | "                 | "                                   |
| 1962-2011 | 5.38%             | 3.36%                                | 4.02%             | 2.35%                               |
| "         | 2.39%             | 2.68%                                | "                 | "                                   |
| 2002-2011 | 3.12%             | -1.92%                               | 1.08%             | -3.61%                              |
| "         | 6.46%             | 8.94%                                | "                 | "                                   |

#### What about historical premiums for other markets?

 Historical data for markets outside the United States is available for much shorter time periods. The problem is even greater in emerging markets. The historical premiums that emerge from this data reflects this data problem and there is much greater error associated with the estimates of the premiums.

#### One solution: Look at a country's bond rating and default spreads as a start

- Ratings agencies assign ratings to countries that reflect their assessment of the default risk of these countries. These ratings reflect the political and economic stability of these countries and thus provide a useful measure of country risk.
  - In May 2009, the local currency rating, from Moody's, for Brazil was Ba1. In May 2009, Brazil had dollar denominated 10-year Bonds, trading at an interest rate of 6%. The US treasury bond rate that day was 3.5%, yielding a default spread of 2.50% for Brazil.
- India has a rating of Ba2 from Moody's but has no dollar denominated bonds. The typical default spread for Ba2 rated sovereign bonds is 3%. Many analysts add this default spread to the US risk premium to come up with a risk premium for a country. This would yield a risk premium of 6.38% for Brazil and 6.88% for India, if we use 3.88% as the premium for the US .

#### Beyond the default spread

- While default risk spreads and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads. In fact, one simple way to adjust the default spread for the additional risk in the equity market is to multiply it by the relative volatility (standard deviation of equities/ standard deviation of government bond) Risk Premium for Brazil in early 2009
  - Standard Deviation in Bovespa (Equity) = 34%
  - Standard Deviation in Brazil \$ denominated Bond = 21.5%
  - Default spread on \$ denominated Bond = 2.5%
  - Country Risk Premium (CRP) for Brazil = 2.5% (34%/21.5%) = 3.95%
  - Total Risk Premium for Brazil = US risk premium (in '09) + CRP for Brazil = 3.88% + 3.95% = 7.83%

#### *Country Risk Premiums January 2012*

| Angola       | 10.88% |
|--------------|--------|
| Botswana     | 7.50%  |
| Egypt        | 13.50% |
| Mauritius    | 8.63%  |
| Morocco      | 9.60%  |
| Namibia      | 9.00%  |
| South Africa | 7.73%  |
| Tunisia      | 9.00%  |

| Bangladesh   | 10.88% |
|--------------|--------|
| Cambodia     | 13.50% |
| China        | 7.05%  |
| Fiji Islands | 12.00% |
| Hong Kong    | 6.38%  |
| India        | 9.00%  |
| Indonesia    | 9.60%  |
| Japan        | 7.05%  |
| Korea        | 7.28%  |
| Macao        | 7.05%  |
| Malaysia     | 7.73%  |
| Mongolia     | 12.00% |
| Pakistan     | 15.00% |
| Guinea       | 12.00% |
| Philippines  | 10.13% |
| Singapore    | 6.00%  |
| Sri Lanka    | 12.00% |
| Taiwan       | 7.05%  |
| Thailand     | 8.25%  |
| Turkey       | 10.13% |
| Vietnam      | 12.00% |

| <span></span> | <span></span> | <span></span> |
|---------------|---------------|---------------|
| Australia     | 6.00%         |               |
| New Zealand   | 6.00%         |               |

| Argentina   | 15.00% |
|-------------|--------|
| Belize      | 15.00% |
| Bolivia     | 12.00% |
| Brazil      | 8.63%  |
| Chile       | 7.05%  |
| Colombia    | 9.00%  |
| Costa Rica  | 9.00%  |
| Ecuador     | 18.75% |
| El Salvador | 10.13% |
| Guatemala   | 9.60%  |
| Honduras    | 13.50% |
| Mexico      | 8.25%  |
| Nicaragua   | 15.00% |
| Panama      | 9.00%  |
| Paraguay    | 12.00% |
| Peru        | 9.00%  |
| Uruguay     | 9.60%  |
| Venezuela   | 12.00% |

| Albania        | 12.00% |
|----------------|--------|
| Armenia        | 10.13% |
| Azerbaijan     | 9.60%  |
| Belarus        | 15.00% |
| Herzegovina    | 13.50% |
| Bulgaria       | 8.63%  |
| Croatia        | 9.00%  |
| Czech Republic | 7.28%  |
| Estonia        | 7.28%  |
| Georgia        | 10.88% |
| Hungary        | 9.60%  |
| Kazakhstan     | 8.63%  |
| Latvia         | 9.00%  |
| Lithuania      | 8.25%  |
| Moldova        | 15.00% |
| Montenegro     | 10.88% |
| Poland         | 7.50%  |
| Romania        | 9.00%  |
| Russia         | 8.25%  |
| Slovakia       | 7.28%  |
| Slovenia [1]   | 7.28%  |
| Ukraine        | 13.50% |

| Bahrain              | 8.25%  |
|----------------------|--------|
| Israel               | 7.28%  |
| Jordan               | 10.13% |
| Kuwait               | 6.75%  |
| Lebanon              | 12.00% |
| Oman                 | 7.28%  |
| Qatar                | 6.75%  |
| Saudi Arabia         | 7.05%  |
| Senegal              | 12.00% |
| United Arab Emirates | 6.75%  |

| Canada                   | 6.00% |
|--------------------------|-------|
| United States of America | 6.00% |

| Austria [1]     | 6.00%  |
|-----------------|--------|
| Belgium [1]     | 7.05%  |
| Cyprus [1]      | 9.00%  |
| Denmark         | 6.00%  |
| Finland [1]     | 6.00%  |
| France [1]      | 6.00%  |
| Germany [1]     | 6.00%  |
| Greece [1]      | 9.00%  |
| Iceland         | 9.00%  |
| Ireland [1]     | 9.60%  |
| Italy [1]       | 7.50%  |
| Malta [1]       | 7.50%  |
| Netherlands [1] | 6.00%  |
| Norway          | 6.00%  |
| Portugal [1]    | 10.13% |
| Spain [1]       | 7.28%  |
| Sweden          | 6.00%  |
| Switzerland     | 6.00%  |
| United Kingdom  | 6.00%  |

#### An Alternative Approach: Watch what I pay, not what I say…

 On January 1, 2012, the S&P 500 was at 1257.60, essentially unchanged for the year. And it was a year of macro shocks – political upheaval in the Middle East and sovereign debt problems in Europe. The treasury bond rate dropped below 2% and buybacks/dividends surged.

![](_page_26_Figure_5.jpeg)

*In the trailing 12 months, the cash returned to stockholders was 74.17. Using the average cash yield of 4.71% for 2002-2011 the cash returned would have been 59.29.*

Analysts expect earnings to grow 9.6% in 2012, 11.9% in 2013, 8.2% in 2014, 4.5% in 2015 and 2% therafter, resulting in a compounded annual growth rate of 7.18% over the next 5 years. We will assume that dividends & buybacks will grow 7.18% a year for the next 5 years.

After year 5, we will assume that earnings on the index will grow at 1.87%, the same rate as the entire economy (= riskfree rate).

> *Dividends and Buybacks last year*: S&P *Expected growth rate*: News stories, Yahoo! Finance, Bloomberg

#### Implied Premiums in the US: 1960-2011

![](_page_27_Figure_2.jpeg)

#### Firm Specific and Market Risk

 The R squared (R2) of the regression provides an estimate of the proportion of the risk (variance) of a firm that can be attributed to market risk; The balance (1 - R2) can be attributed to firm specific risk.

#### Beta Estimate: Disney – 2004-2008

![](_page_29_Figure_2.jpeg)

#### Estimating Expected Returns for Disney in May 2009

- Inputs to the expected return calculation
  - Disney's Beta = 0.95
  - Riskfree Rate = 3.50% (U.S. ten-year T.Bond rate in May 2009)
- Risk Premium = 6% (Based on updated implied premium at the start of 2009) Expected Return = Riskfree Rate + Beta (Risk Premium) = 3.50% + 0.95 (6.00%) = 9.2%

#### Use to a Potential Investor in Disney

As a potential investor in Disney, what does this expected return of 9.2% tell you?

- a) This is the return that I can expect to make in the long term on Disney, if the stock is correctly priced and the CAPM is the right model for risk,
- b) This is the return that I need to make on Disney in the long term to break even on my investment in the stock
- c) Both

Assume now that you are an active investor and that your research suggests that an investment in Disney will yield 12.5% a year for the next 5 years. Based upon the expected return of 9.2%, you would

- a) Buy the stock
- b) Sell the stock

#### Myths about beta

 Beta is a measure of overall risk: It is not. It measures only exposure to macro or market risk. Thus, volatile investments can have low betas, if the bulk of their risk is specific to the investment. Beta is a statistical measure: While betas might be estimated from regressions, they are determined by three fundamental decisions that a firm makes: the business it is in, its fixed cost structure and its financial leverage. Beta is a fact: It is not. It is an estimate and a single regression beta can have a very high standard error. Beta measures investment quality: It does not. It measures investment risk. Thus, you can have a great investment with a low beta, an average beta or a high beta.

#### Limitations of the CAPM

- 1. The model makes unrealistic assumptions
- 2. The parameters of the model cannot be estimated precisely
  - - Definition of a market index
  - - Firm may have changed during the 'estimation' period'
- 3. The model does not work well
  - - If the model is right, there should be
    - a linear relationship between returns and betas
    - the only variable that should explain returns is betas
  - - The reality is that
    - the relationship between betas and returns is weak
    - Other variables (size, price/book value) seem to explain differences in returns better.

#### B. Alternatives to the CAPM

| expected return                                                                                                                                                                                                                                                                                                   | Step 1: Defining Risk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Riskless Investment                                                                                                                                                                                                                                                                                               | Low Risk Investment High Risk Investment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| E(R)                                                                                                                                                                                                                                                                                                              | E(R) E(R)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Risk that is specific to investment (Firm Specific)                                                                                                                                                                                                                                                               | Risk that affects all investments (Market Risk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Can be diversified away in a diversified portfolio                                                                                                                                                                                                                                                                | Cannot be diversified away since most assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1. each investment is a small proportion of portfolio 2. risk averages out across investments in portfolio be rewarded and priced.                                                                                                                                                                                | are affected by it. Step 3: Measuring Market Risk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| The CAPM If there is 1. no private information 2. no transactions cost the optimal diversified portfolio includes every traded asset. Everyone will hold this market portfolio Market Risk = Risk added by any investment to the market portfolio: Beta of asset relative to Market portfolio (from a regression) | The APM Multi-Factor Models Proxy Models If there are no Since market risk affects In an efficient market, arbitrage opportunities most or all investments, differences in returns then the market risk of it must come from across long periods must any asset must be macro economic factors. be due to market risk captured by betas Market Risk = Risk differences. Looking for relative to factors that exposures of any variables correlated with affect all investments. asset to macro returns should then give Market Risk = Risk economic factors. us proxies for this risk. exposures of any Market Risk = asset to market Captured by the factors Proxy Variable(s) Betas of asset relative Betas of assets relative Equation relating to unspecified market to specified macro returns to proxy factors (from a factor economic factors (from variables (from a analysis) a regression) regression) |

#### II. Alternative models of Equity Risk

- There are many who find theory based models of equity risk lacking because
  - They look at both upside and downside volatility (it is only the latter that investors don't like)
  - They are based upon market prices rather than fundamentals
- They break risk down into diversifiable and non-diversifiable components, a break down that may have no relevance if you are only minimally diversified. The alternative models for equity risk can broadly be classified as
  - Models that are based upon accounting statements
  - Proxy models (where something else stands in for risk)
  - Market implied measures of risk
  - Risk adjusted earnings/ cash flows
  - Margin of Safety

#### a. Accounting based risk measures

*Accounting Ratio:* Pick an accounting ratio, and scale risk to this ratio. Thus, the median book debt to capital ratio for US companies at the start of 2011 was 51%. The book debt to capital ratio for 3M at that time 30.91%, yielding a relative risk measure of 0.61 for the company, obtained by dividing 3M's debt ratio (30.91%) by the market average (51%). *Compute an accounting beta*: Look at changes in accounting earnings at a firm, relative to accounting earnings for the entire market. Firms that have more stable earnings than the rest of the market or whose earnings movements have nothing to do with the rest of the market will have low accounting betas.

#### b. Proxy Models

- Look at returns on individual stocks over long periods and search for characteristics shared by companies that earn high returns. This approach was kicked off by Fama and French, who found that low price to book and small market cap stocks earned higher returns than the rest of the market. In the years since, there have been additional three additional variables that seem to be correlated with returns:
  - Earnings momentum: Companies that have reported stronger than expected earnings growth in the past earn higher returns than the rest of the market.
  - Price momentum: Returns are higher for stocks that have outperformed markets in recent time periods and lower for stocks that have lagged.
  - Liquidity: Stocks that are less liquid (lower trading volume, higher bidask spreads) earn higher returns than more liquid stocks.

#### c. Market Implied risk measures

 If you can observe the price of a risky asset, and you can estimate the expected cash flows on that asset, you can back out the market's implied "required return" for that asset. With bonds, we use promised coupons and the face value, in conjunction with the price of the bond today to compute yields to maturity. With stocks, with we can used expected dividends or cash flows together with the stock price to get an expected return on the stock.

#### d. Risk adjusted cash flows

- Risk adjusting the cash flows requires more than taking the expected cash flow across all scenarios, good and bad. You have to convert these expected cash flows into certainty equivalent cash flows. There are two practical approaches to computing certainty equivalent cash flows. .
  - In the first, you consider only those cash flows from a business that are "safe" and that you can count on, when you do valuation. If you do so, and you are correct in your assessment, you don't have to risk adjust the cash flows.
  - The second variant is an interesting twist on dividends and a throw back to Ben Graham. To the extent that companies are reluctant to cut dividends, once they initiate them, it can be argued that the dividends paid by a company reflects its view of how much of its earnings are certain.

#### e. Margin of Safety

- The "margin of safety" has a long history in value investing. While the term may have been in use prior to 1934, Graham and Dodd argued that investors should buy stocks that trade at significant discounts on value and developed screens that would yield these stocks. To put into practice the margin of safety (MOS), investors have to
  - Screen for companies that meets good company criteria: solid management, good product and sustainable competitive advantages.
  - Estimate intrinsic value. Value investors use a variety of approaches in this endeavor: some use discounted cash flow, some use relative valuation and some look at book value.
  - . The third step in the process is to compare the price to the intrinsic value and that is where the MOS comes in: with a margin of safety of 40%, you would only buy an asset if its price was more than 40% below its intrinsic value.

#### Propositions about MOS

Proposition 1: MOS comes into play at the end of the investment process, not at the beginning.

Proposition 2: MOS does not substitute for risk assessment and intrinsic valuation, but augments them.

Proposition 3: The MOS cannot and should not be a fixed number, but should be reflective of the uncertainty in the assessment of intrinsic value.

Proposition 4: Being too conservative can be damaging to your long term investment prospects.

#### Final thoughts about equity risk

- a. Explicit versus implicit: There are plenty of analysts who steer away from discounted cash flow valuation and use relative valuation (multiples and comparable firms) because they are uncomfortable with measuring risk explicitly. The danger with implicit assumptions is that you can be lulled into a false sense of complacency, even as circumstances change.
- b. Quantitative versus qualitative: Analysts who use conventional risk and return models are accused of being too number oriented and not looking at qualitative factors enough. Perhaps, but the true test of whether you can do valuation is whether you can take stories that you hear about companies and convert them into numbers for the future.
- c. Simple versus complicated: Sometimes, less is more and you get your best assessments when you keep things simple.

#### What is debt?

- General Rule: Debt generally has the following characteristics:
  - Commitment to make fixed payments in the future
  - The fixed payments are tax deductible
- Failure to make the payments can lead to either default or loss of control of the firm to the party to whom payments are due. As a consequence, debt should include
  - Any interest-bearing liability, whether short term or long term.
  - Any lease obligation, whether operating or capital.

#### Measuring Bond Risk: Default Risk

 When you buy a bond, you are promised a fixed payment (the interest rate on the bond). The best case scenario for you is that you receive that fixed payment. The worse case scenarios have a much wider range, with the worst case scenario being that you do not receive any of your promised cash flows. Since the potential for upside is limited and for downside is very large, we measure risk in bonds by looking at the downside or default risk.

#### Determinants of Default Risk

*Capacity to generate cashflows from operations*: The larger the cashflows that you generate from operations, the lower your default risk should be. *Volatility in these cashflows*: The more predictable your cashflows are, the lower your default risk should be. *Fixed Commitments*: The larger your commitments (interest and principal payments), relative to your operating cashflows, the greater is your default risk.

#### Measuring Default Risk

*Credit Risk Scores*: For as long as institutions and individuals have been lending money, they have been using both qualitative and quantitative factors to measure the credit risk of borrowers. *Bond Ratings*: Publicly traded companies that desire to access the bond market (where individual investors may lack the resources and the incentives to measure default risk on their own) have been rated by ratings agencies.

#### The Ratings Process

![](_page_47_Diagram_1.jpeg)

#### Ratings and Financial Ratios

|                        | AAA   | AA   | A    | BBB  | BB   | B    | CCC   |
|------------------------|-------|------|------|------|------|------|-------|
| EBIT interest cov. (x) | 17.5  | 10.8 | 6.8  | 3.9  | 2.3  | 1.0  | 0.2   |
| EBITDA interest cov.   | 21.8  | 14.6 | 9.6  | 6.1  | 3.8  | 2.0  | 1.4   |
| Funds flow/total debt  | 105.8 | 55.8 | 46.1 | 30.5 | 19.2 | 9.4  | 5.8   |
| Free oper. cash        | 55.4  | 24.6 | 15.6 | 6.6  | 1.9  | –4.5 | -14.0 |
| Return on capital (%)  | 28.2  | 22.9 | 19.9 | 14.0 | 11.7 | 7.2  | 0.5   |
| Oper.income/sales      | 29.2  | 21.3 | 18.3 | 15.3 | 15.4 | 11.2 | 13.6  |
| Long-term              | 15.2  | 26.4 | 32.5 | 41.0 | 55.8 | 70.7 | 80.3  |
| Total Debt/ Capital    | 26.9  | 35.6 | 40.1 | 47.4 | 61.3 | 74.6 | 89.4  |
| Number of firms        | 10    | 34   | 150  | 234  | 276  | 240  | 23    |

#### From Ratings to Default Spreads

| <i>Interest Coverage Ratio: Small market cap(&lt;\$5 billion)</i> | <i>Interest Coverage Ratio: Large market cap (&gt;US \$ 5 billion)</i> | <i>Rating</i> | <i>Typical Default</i> |
|-------------------------------------------------------------------|------------------------------------------------------------------------|---------------|------------------------|
| > 12.5                                                            | >8.5                                                                   | AAA           | 1.25%                  |
| 9.50–12.50                                                        | 6.5-8.5                                                                | AA            | 1.75%                  |
| 7.50–9.50                                                         | 5.5-6.5                                                                | A+            | 2.25%                  |
| 6.00–7.50                                                         | 4.25- 5.5                                                              | A             | 2.50%                  |
| 4.50–6.00                                                         | 3- 4.25                                                                | A-            | 3.00%                  |
| 4.00-4.50                                                         | 2.5-3.0                                                                | BBB           | 3.50%                  |
| 3.50–4.00                                                         | 2.25-2.5                                                               | BB+           | 4.25%                  |
| 3.00–3.50                                                         | 2.0-2.25                                                               | BB            | 5.00%                  |
| 2.50–3.00                                                         | 1.75-2.0                                                               | B+            | 6.00%                  |
| 2.00–2.50                                                         | 1.5-1.75                                                               | B             | 7.25%                  |
| 1.50–2.00                                                         | 1.25-1.5                                                               | B-            | 8.50%                  |
| 1.25–1.50                                                         | 0.8-1.25                                                               | CCC           | 10.00%                 |
| 0.80–1.25                                                         | 0.65-0.8                                                               | CC            | 12.00%                 |
| 0.50–0.80                                                         | 0.2-0.65                                                               | C             | 15.00%                 |
| < 0.65                                                            | <0.2                                                                   | D             | 20.00%                 |

#### Updated Default Spreads – January 2012

| Ra#ng       | 1	  year | 5	  year | 10	  year | 30	  year |
|-------------|-----------|-----------|------------|------------|
| Aaa/AAA     | 0.35%     | 0.70%     | 0.65%      | 0.85%      |
| Aa1/AA+     | 0.45%     | 0.75%     | 0.80%      | 1.10%      |
| Aa2/AA      | 0.50%     | 0.80%     | 0.95%      | 1.15%      |
| Aa3/AA-­‐   | 0.60%     | 0.85%     | 1.05%      | 1.20%      |
| A1/A+       | 0.65%     | 0.90%     | 1.15%      | 1.30%      |
| A2/A        | 0.80%     | 1.05%     | 1.20%      | 1.40%      |
| A3/A-­‐     | 0.95%     | 1.25%     | 1.45%      | 1.65%      |
| Baa1/BBB+   | 1.20%     | 1.70%     | 2.00%      | 2.20%      |
| Baa2/BBB    | 1.30%     | 2.05%     | 2.30%      | 2.50%      |
| Baa3/BBB-­‐ | 2.00%     | 2.80%     | 3.10%      | 3.25%      |
| Ba1/BB+     | 4.00%     | 4.00%     | 3.75%      | 3.75%      |
| Ba2/BB      | 4.50%     | 5.50%     | 4.50%      | 4.75%      |
| Ba3/BB-­‐   | 4.75%     | 5.75%     | 4.75%      | 5.25%      |
| B1/B+       | 5.75%     | 6.75%     | 5.50%      | 5.50%      |
| B2/B        | 6.25%     | 7.75%     | 6.50%      | 6.00%      |
| B3/B-­‐     | 6.50%     | 9.00%     | 6.75%      | 6.25%      |
| Caa/CCC     | 7.25%     | 9.25%     | 8.75%      | 8.25%      |
| CC          | 8.00%     | 9.50%     | 9.50%      | 9.50%      |
| C           | 9.00%     | 10.00%    | 10.50%     | 10.50%     |
| D           | 10.00%    | 12.00%    | 12.00%     | 12.00%     |

#### Estimating the Cost of Debt

- If the firm has bonds outstanding, and the bonds are traded, the yield to maturity on a long-term, straight (no special features) bond can be used as the interest rate. If the firm is rated, use the rating and a typical default spread on bonds with that rating to estimate the cost of debt. If the firm is not rated,
  - and it has recently borrowed long term from a bank, use the interest rate on the borrowing or
  - estimate a synthetic rating for the company, and use the synthetic rating to arrive at a default spread and a cost of debt

#### Estimating Synthetic Ratings

 The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

 For a firm, which has earnings before interest and taxes of \$ 3,500 million and interest expenses of \$ 700 million

Interest Coverage Ratio = 3,500/700= 5.00

- Based upon the relationship between interest coverage ratios and ratings, we would estimate a rating of A for the firm.

### Interest Coverage Ratios, Ratings and Default Spreads

| <i>Interest Coverage Ratio: Small market cap(&lt;\$ billion)</i> | <i>Interest Coverage Ratio: Large market cap (&gt;US \$ 5 billion)</i> | <i>Rating</i> | <i>Typical Default</i> |
|------------------------------------------------------------------|------------------------------------------------------------------------|---------------|------------------------|
| > 12.5                                                           | >8.5                                                                   | AAA           | 1.25%                  |
| 9.50–12.50                                                       | 6.5-8.5                                                                | AA            | 1.75%                  |
| 7.50–9.50                                                        | 5.5-6.5                                                                | A+            | 2.25%                  |
| 6.00–7.50                                                        | 4.25- 5.5                                                              | A             | 2.50%                  |
| 4.50–6.00                                                        | 3- 4.25                                                                | A-            | 3.00%                  |
| 4.00-4.50                                                        | 2.5-3.0                                                                | BBB           | 3.50%                  |
| 3.50–4.00                                                        | 2.25-2.5                                                               | BB+           | 4.25%                  |
| 3.00–3.50                                                        | 2.0-2.25                                                               | BB            | 5.00%                  |
| 2.50–3.00                                                        | 1.75-2.0                                                               | B+            | 6.00%                  |
| 2.00–2.50                                                        | 1.5-1.75                                                               | B             | 7.25%                  |
| 1.50–2.00                                                        | 1.25-1.5                                                               | B-            | 8.50%                  |
| 1.25–1.50                                                        | 0.8-1.25                                                               | CCC           | 10.00%                 |
| 0.80–1.25                                                        | 0.65-0.8                                                               | CC            | 12.00%                 |
| 0.50–0.80                                                        | 0.2-0.65                                                               | C             | 15.00%                 |
| < 0.65                                                           | <0.2                                                                   | D             | 20.00%                 |

#### In closing…

- Higher risk investments should earn higher expected returns. The way we measure risk is different for equity investments (stocks) and bonds.
  - With stocks, we make the assumption that the risk that matters is risk that cannot be diversified. This non-diversifiable risk is measured with one beta (in the CAPM) or multiple betas (with more complex risk and return models).
  - With bonds, we measure risk as default risk.