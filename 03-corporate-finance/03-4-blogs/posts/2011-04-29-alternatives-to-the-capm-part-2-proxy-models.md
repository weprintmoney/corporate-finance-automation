---
title: "Alternatives to the CAPM: Part 2: Proxy Models"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-2-proxy.html
published: 2011-04-29
updated_source: 2011-04-30
fetched: 2026-08-27
---

# Alternatives to the CAPM: Part 2: Proxy Models

_Source: [https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-2-proxy.html](https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-2-proxy.html) — published 2011-04-29_

The conventional models for risk and return in finance (CAPM, arbitrage pricing model and even multi-factor models) start by making assumptions about how investors behave and how markets work to derive models that measure risk and link those measures to expected returns. While these models have the advantage of a foundation in economic theory, they seem to fall short in explaining differences in returns across investments. The reasons for the failure of these models run the gamut: the assumptions made about markets are unrealistic (no transactions costs, perfect information) and investors don't behave rationally (and behavioral finance research provides ample evidence of this).

With proxy models, we essentially give up on building risk and return models from economic theory. Instead, we start with how investments are priced by markets and relate returns earned to observable variables. Rather than talk in abstractions, consider the [work done by Fama and French in the early 1990s](http://www.bengrahaminvesting.ca/Research/Papers/French/The_Cross-Section_of_Expected_Stock_Returns.pdf). Examining returns earned by individual stocks from 1962 to 1990, they concluded that CAPM betas did not explain much of the variation in these returns. They then took a different tack and  looking for company-specific variables that did a better job of explaining return differences and pinpointed two variables - the market capitalization of a firm and its price to book ratio (the ratio of market cap to accounting book value for equity). Specifically, they concluded that small market cap stocks earned much higher annual returns than large market cap stocks and that low price to book ratio stocks earned much higher annual returns than stocks that traded at high price to book ratios. Rather than view this as evidence of market inefficiency (which is what prior studies that had found the same phenomena had), they argued if these stocks earned higher returns over long time periods, they must be riskier than stocks that earned lower returns. In effect, market capitalization and price to book ratios were better proxies for risk, according to their reasoning, than betas. In fact, they regressed returns on stocks against the market capitalization of a company and its price to book ratio to arrive at the following regression for US stocks;

Expected Monthly Return = 1.77% - 0.11 (ln(Market Capitalization in millions) + 0.35 (ln (Book/Price))

In a pure proxy model, you could plug the market capitalization and book to market ratio for any company into this regression to get expected monthly returns.

In the two decades since the Fama-French paper brought proxy models to the fore, researchers have probed the data (which has become more detailed and voluminous over time) to find better and additional proxies for risk. Some of the proxies are highlighted below:

a. Earnings Momentum: Equity research analysts will find vindication in research that seems to indicate that companies that have reported stronger than expected earnings growth in the past earn higher returns than the rest of the market.

b. Price Momentum: Chartists will smile when they read this, but researchers have concluded that price momentum carries over into future periods. Thus, the expected returns will be higher for stocks that have outperformed markets in recent time periods and lower for stocks that have lagged.

c. Liquidity: In a nod to real world costs, there seems to be clear evidence that stocks that are less liquid (lower trading volume, higher bid-ask spreads) earn higher returns than more liquid stocks. In fact, I have a [paper on liquidity](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1729408), where I explore the estimation of a liquidity beta and liquidity risk premium to adjust expected returns for less liquid companies.

While the use of pure proxy models by practitioners is rare, they have adapted the findings for these models into their day-to-day use. IMany analysts have melded the CAPM with proxy models to create composite or melded models. For instance, many analysts who value small companies derive expected returns for these companies by adding a "small cap premium" to the CAPM expected return:

Expected return = Riskfree rate + Market Beta * Equity Risk Premium + Small Cap Premium

The threshold for small capitalization varies across time but is generally set at the bottom decile of publicly traded companies and the small cap premium itself is estimated by looking at the historical premium earned by small cap stocks over the market. (In my 2011 paper on equity risk premiums, I estimate that companies in the bottom market cap decile earned 4.82% more than the overall market between 1928 and 2010.) Thus, the expected return (cost of equity) for a small cap company, with a beta of 1.20 would be:

Expected return = 3.5% + 1.2 (5%) + 4.82% = 14.32%

(I have used a riskfree rate of 3.5% and a mature market premium of 5% in my estimation)

Using the Fama-French findings, the CAPM has been expanded to include market capitalization and price to book ratios as additional variables, with the expected return stated as:

Expected return = Riskfree rate + Market Beta * Equity Risk Premium + Size beta * Small cap risk premium + Book to Market beta * Book to Market premium

The size factor and the book to market betas are estimated by regressing a stock's returns against the size premium and book to market premiums over time; this is analogous to the way we get the market beta, by regressing stock returns against overall market returns.

While the use of proxy and melded models offers a way of adjusting expected returns to reflect market reality, there are three dangers in using these models.

a. Data mining: As the amount of data that we have on companies increases and becomes more accessible, it is inevitable that we will find more variables that are related to returns. It is also likely that most of these variables are not proxies for risk and that the correlation is a function of the time period that we look at. In effect, proxy models are statistical models and not economic models. Thus, there is no easy way to separate the variables that matter from those that do not.

b. Standard error: Since proxy models come from looking at historical data, they carry all of the burden of the noise in the data . Stock returns are extremely volatile over time, and any historical premia that we compute (for market capitalization or any other variable) are going to have significant standard errors. For instance, the small cap premium of 4.82% between 1928 and 2010 has a standard error of 2.02%; put simply, the true premium may be less than 1% or higher than 7%. The standard errors on the size and book to market betas in the three factor Fama-French model are so large that using them in practice creates almost as much noise as it adds in precision.

c. Pricing error or Risk proxy: For decades, value investors have argued that you should invest in stocks with low PE ratios that trade at low multiples of book value and have high dividend yields, pointing to the fact that you will earn higher returns by doing so. (In fact, a scan of Ben Graham's screens from security analysis for cheap companies unearths most of the proxies that you see in use today.)  Proxy models incorporate all of these variables into the expected return and thus render these assets to be fairly priced. Using the circular logic of these models, markets are always efficient because any inefficiency that exists is just another risk proxy that needs to get built into the model.

I have never used the Fama-French model or added a small cap premium to a CAPM model in intrinsic valuation. If I believe that small cap stocks are riskier than large stocks, I have an obligation to think of fundamental or economic reasons why and build those into my risk and return model or into the parameters of the model. Adding a small cap premium strikes me as not only a sloppy (and high error) way of adjusting expected returns but an abdication of the mission in intrinsic valuation, which is to build up your numbers from fundamentals. I do think that it makes sense to adjust your expected returns for liquidity, and I think our capacity to do so is improving as we get access to more data on liquidity and better models for incorporating that data.

**The series on alternatives to the CAPM**

[Alternatives to the CAPM: Part 1: Relative Risk Measures](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-1-relative.html)

[Alternatives to the CAPM: Part 2: Proxy Models](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-2-proxy.html)

[Alternatives to the CAPM: Part 3: Connecting cost of equity to cost of debt](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-3-connecting.html)

[Alternatives to the CAPM: Part 4: Market-implied costs of equity](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-4-market.html)

[Alternatives to the CAPM: Part 5: Risk adjusting the cash flows](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-5-risk-adjusting.html)

[Alternatives to the CAPM: Wrapping up](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-wrapping-up.html)
