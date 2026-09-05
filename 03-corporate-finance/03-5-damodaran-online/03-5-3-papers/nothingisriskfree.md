---
title: "Nothingisriskfree"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/papers/nothingisriskfree.pdf
---

# **Into the Abyss: What if nothing is risk free?**

*July 2010*

*Aswath Damodaran*

*Stern School of Business*

*adamodar@stern.nyu.edu*

# **Into the Abyss: What if nothing is risk free?**

In corporate finance and investment analysis, we assume that there is an investment with a guaranteed return that offers both firms and investors a "risk free" choice. This assumption, innocuous though it may seem, is a critical component of both risk and return models and corporate financial theory. But what if there is no risk free investment? During the banking crisis of 2008, this question came to the fore, as investors began questioning the credit worthiness of US treasuries, UK gilts and Germans bonds. In effect, the fear that governments can default, hitherto restricted to risky, emerging markets, had seeped into developed markets as well. In this paper, we examine why governments may default, even on local currency bonds, and the consequences. We also look at how best to estimate a risk free rate, when no default free entity exists, and the effects on both investors and firms. In particular, we argue that the absence of a riskfree investment will make investors collectively more risk averse, thus reducing the prices of all risky assets, and induce firms to borrow less money and pay out lower dividends.

If there is a constant in any financial analysis, it is that there is at least one entity that is incapable of default and that investing in its financial obligations yields a guaranteed return; this guaranteed return represents a risk free rate and it is the base on which we build expected returns for risky assets. That "default free" entity is usually the government, with the implicit assumptions being both that the cost of default is so catastrophic that governments will find a way to fulfill their obligations and that they have more powers to do so, including the right to print money, than other entities. When governments default or are perceived as capable of default, their obligations are no longer guaranteed, and this has profound implications both for financial analysis and decisionmaking.

In this paper, we begin by first defining a risk free rate and then examining why the risk free investment is so central to financial theory and investing practice. We then look at the history of sovereign defaults and the circumstances that precipitated these defaults. We move on to ways of estimating the default risk in sovereign investments, from sovereign ratings to market prices. In the final section, we look at ways of dealing with the possibility that governments can default and the consequences for corporate finance and investing.

# **What is a risk free investment?**

To understand what makes an investment risk free, let us go back to how risk is measured in finance. Investors who invest in an asset have a return that they expect to make over the time horizon that they will hold the asset. The actual returns that they make over this holding period may by very different from the expected returns, and this is where the risk comes in. Risk in finance is viewed in terms of the variance in actual returns around the expected return. For an investment to be risk free in this environment, then, the actual returns should always be equal to the expected return.

To illustrate, consider an investor with a 1-year time horizon buying a 1-year default-free one-year bond with a 5% expected return. At the end of the 1-year holding period, the actual return that this investor would have on this investment will always be 5%, which is equal to the expected return. The return distribution for this investment is shown in Figure 1.

This investment is risk free because there is no variance around the expected return.

There are two basic conditions that have to be met for the actual returns on an investment to be equal to always equal to the expected return. The first is that there can be no default risk. Essentially, this rules out any security issued by a private firm, since even the largest and safest firms have some measure of default risk. The only securities that have a chance of being risk free are government securities, not because governments are better run than corporations, but because they control the printing of currency. At least in nominal terms, they should be able to fulfill their promises. Even this assumption, straightforward though it might seem, does not always hold up, especially when governments refuse to honor claims made by previous regimes and when they borrow in currencies other than their own.

There is a second condition that riskless securities need to fulfill that is often forgotten. For an investment to have an actual return equal to its expected return, there can be no reinvestment risk. To illustrate this point, assume that you are trying to estimate the expected return over a five-year period, and that you need a risk free rate over this time horizon. A six-month treasury bill rate, even if default free, will not be risk

|                 |  | Probability = 1 |  |
|-----------------|--|-----------------|--|
|                 |  |                 |  |
| Expected Return |  | Returns         |  |

*Figure 2.1: Returns on a Riskfree Investment*

free, because there is the reinvestment risk of not knowing what the treasury bill rate will be in six months. Even a 5-year treasury bond is not risk free, since the coupons on the bond will be reinvested at rates that cannot be predicted today. The risk free rate for a five-year time horizon has to be the expected return on a default-free (government) fiveyear zero coupon bond. This clearly has painful implications for anyone doing corporate finance or valuation, where expected returns often have to be estimated for periods ranging from one to ten years. A purist's view of risk free rates would then require different risk free rates for each period, and different expected returns.

# **The importance of having a risk free investment**

When investors are faced with an array of risky investment choices, why does it matter if there is no investment that is truly risk free? As we will argue in this section, the existence of a risk free asset is central to modern portfolio theory and the pricing of derivative securities. It affects how companies make investment, financing and dividend decisions and how investors make asset allocation and investment choices. Finally, the absence of a risk free investment is unsettling to investors and can have far reaching effects on not only capital markets but also the real economy.

# **Risk Theory and Models**

The initial forays by Harry Markowitz into portfolio theory were focused on how to create an optimal portfolio from a set of risky assets. Markowitz noted that if an investor can specify the maximum amount of risk he is willing to take on (in terms of variance), the task of portfolio optimization becomes the maximization of expected returns subject to this level of risk. Alternatively, if an investor specifies her desired level of return, the optimum portfolio is the one that minimizes the variance subject to this level of return. These optimization algorithms can be written as follows.

|            | Return Maximization                                                                      | Risk Minimization                                                    |
|------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
|            | Maximize Expected Return                                                                 | Minimize return variance                                             |
|            | $E(R_p) = \sum_{i=1}^{i=n} w_i E(R_i)$                                                   | $\sigma_p^2 = \sum_{i=1}^{i=n} \sum_{j=1}^{j=n} w_i w_j \sigma_{ij}$ |
| subject to | $\sigma_p^2 = \sum_{i=1}^{i=n} \sum_{j=1}^{j=n} w_i w_j \sigma_{ij} \leq \hat{\sigma}^2$ | $E(R_p) = \sum_{i=1}^{i=n} w_i E(R_i) = E(\hat{R})$                  |

where,

The portfolios that emerge from this process are called **efficient portfolios**, because they maximize expected returns given the standard deviation, and the entire set of portfolios is referred to as the **Efficient Frontier**. Graphically, these portfolios are shown on the expected return/standard deviation dimensions in figure 2 -

## $$\hat{\sigma}$$ = Investor's desired level of variance

$$E(\hat{\mathbf{R}}) = \text{Investor's desired expected returns}$$

*Figure 2: Markowitz Portfolios*

![](_page_5_Figure_6.jpeg)

The Markowitz approach to portfolio optimization, while intuitively appealing, suffers from two major problems. The first is that it requires a very large number of inputs, since the we need to assess how each pair of assets in the portfolio moves together (covariance) to estimate the variances of portfolios. While this may be manageable for small numbers of assets, it becomes less so when the entire universe of stocks or all investments is considered.1 The second problem is that the Markowitz approach will not be able to generate a solution for an investor who wants to bear either no risk or less risk than the least risky efficient portfolio. It is also worth noting that the Markowitz portfolios that emerge from this search will be customized, requiring different portfolios (with different assets and different weights) for investors with different risk preferences.

<sup>1</sup> To assess the variance of a portfolio with 100 assets, you will need to estimate 49,500 covariances [100\*99/2].

Now let us considering adding a riskless asset to the mix of risky assets. By itself, the addition of one asset to the investment universe may seem trivial, but the riskless asset has some special characteristics that simpligyoptimal portfolio choice for all investors.

(1) The riskless asset, by definition, has an expected return that will always be equal to the actual return. The expected return is known when the investment is made, and the actual return should be equal to this expected return.

(2) While risky assets' returns vary, the absence of variance in the riskless asset's returns make it uncorrelated with returns on any of these risky assets. To examine what happens to the variance of a portfolio that combines a riskless asset with a risky portfolio, assume that the variance of the risky portfolio is  $\sigma_r^2$  and that  $w_r$  is the proportion of the overall portfolio invested to these risky assets. The balance is invested in a riskless asset, which has no variance, and is uncorrelated with the risky asset. The variance of the overall portfolio can be written as:

$$\sigma^2_{\text{portfolio}} = w_r^2 \sigma^2_r$$

$$\mathbf{\sigma}_{\text{portfolio}} = \mathbf{w}_r \mathbf{\sigma}_r$$

Note that the the standard deviation of the overall portfolio is directly related to the proportion of the portfolio invested in the risky portfolio. In practical terms, having a riskless asset gives investors an alternate (and more efficient) way of fine tuning risk in their portfolios.

The significance of this result can be illustrated by returning to figure 2 and adding the riskless asset to the choices available to the investor. The effect of this addition is explored in figure 3.

*Figure 3: Introducing a Riskless Asset*

![](_page_7_Figure_2.jpeg)

Consider investor A, whose desired risk level is  $\sigma_A$ . This investor, instead of choosing portfolio A, the Markowitz portfolio containing only risky assets, will choose to invest in a combination of the riskless asset and a much riskier portfolio, since he will be able to make a much higher return for the same level of risk. The expected return increases as the slope of the line drawn from the riskless rate increases, and the slope is maximized when the line is tangential to the efficient frontier; the risky portfolio at the point of tangency is labeled as risky portfolio M. Thus, investor A's expected return is maximized by holding a combination of the riskless asset and risky portfolio M. Investor B, whose desired risk level is  $\sigma_B$ , which happens to be equal to the standard deviation of the risky portfolio M, will choose to invest her entire portfolio in that portfolio. Investor C, whose desired risk level is  $\sigma_C$ , which exceeds the standard deviation of the risky portfolio M, will borrow money at the riskless rate and invest in the portfolio M. The central role that the risky portfolio M plays in this process raises the question of how this portfolio is constructed and what assets it contains. If all investors in this universe are assumed to have the same information and hold the same risky portfolio, portfolio M has to include all traded assets, in proportion to their market values. In other words, any asset that is not in this portfolio will be held by no investors and have no value. The fact that this portfolio includes all traded assets in the market is the reason it is called the **market portfolio**, which should not be a surprising result, given the benefits of diversification and the absence of transactions costs in the capital asset pricing model. If diversification reduces exposure to

firm-specific risk, and there are no costs associated with adding more assets to the portfolio, the logical limit to diversification is to hold a small proportion of every traded asset in the economy. If this seems abstract, consider M to be an extremely well diversified mutual fund that holds stocks and real assets, and treasury bills as the riskless asset. In the CAPM, all investors will hold combinations of treasury bills and the same mutual fund2.

Thus, introducing the riskless asset vastly simplifies the investment decision. Rather than have investor-specific risky portfolios, all investors choose to hold the riskless asset and the market portfolio and are set apart only by what proportions of their wealth they invest in each. Having access to a riskless investment therefore allows investors to have their cake and eat it too. They can diversify to the fullest extent possible across risky assets and then use the riskless asset to adjust the overall risk in their portfolios, investing in the riskless asset to reduce portfolio risk or borrowing at the riskless rate to augment portfolio risk.

## **Pricing of Derivative Assets**

In the last four decades, we have seen an explosion in the derivatives markets. As options and futures contracts proliferate, the models to value them have also become more advanced. The presence of a riskfree rate/asset is central to deriving most of these models, because they are based upon arbitrage, i.e., creating investment positions that have no risk, require no capital but still generate a sure or riskless profit.

To illustrate this concept with options, consider a standard call option, where you get the right to buy an underlying asset at a fixed price any time during the life of the option. You can create an alternate investment (called a replicating portfolio), by borrowing money at the riskfree rate and buying the underlying asset, to generate exactly the same cash flows as the call option. Since this replicating portfolio and the option have identical cash flows, they should trade at the same price to prevent riskless profits or arbitrage. The net effect is that the cost of putting together the replicating portfolio yields the value for the option. With a put option, the process is similar, with the replicating

<sup>2</sup> The significance of introducing the riskless asset into the choice mix, and the implications for portfolio choice were first noted in Sharpe (1964) and Lintner (1965). Hence, the model is sometimes called the Sharpe-Lintner model.

portfolio created by selling the underlying asset and lending the proceeds at the riskfree rate.

In futures and forward contracts, there is a similar arbitrage argument that comes into play. Consider an investor who is looking at buying a futures contract at gold, where he will take delivery of 100 ounces of gold in three months at the specified futures price. She can accomplish the same objective by borrowing money risklessly today and buying 100 ounces of gold. Consequently, the futures price of gold can be written as a function of the current spot price of gold, the risk free rate and any storage costs associated with storing the gold for the next three months.

## **Corporate Finance**

Corporate finance provides a framework for examining how firms invest their resources, the mix of debt and equity that they use to fund these assets and the choices they make in how much cash they return to the owners in the form of dividends and stock buybacks. Having access to riskfree investments plays a role in each of these decisions.

## *Investment Policy*

If we begin with the fundamental premise that firms should invest in an asset/project only if they believe that they can generate returns on this asset that exceed a "hurdle rate" that reflects its risk, having a riskfree asset (and rate) puts a baseline on the hurdle rate. If the cash flows on an investment are guaranteed (and known) at the time of the investment, the investment has to generate returns that exceed the risk free rate. For riskier investments, the hurdle rate will be comprised of two components – a base of a risk free rate and a risk premium, reflecting the perceived risk in the investment.

In capital budgeting, the net present value becomes the measure that captures the difference between what an investment is expected to generate in cash flows (and returns) and what it needs to generate, given its risk. A positive (negative) net present value is an indication that an asset earns higher (lower) returns than what other assets with similar risk can generate. Investing in the risk free asset and earning the riskfree rate thus comprises a zero net present value investment. In most corporate financial analysis, it is taken as a given that a risk free asset exists and that any firm should therefore be able to generate at least a zero net present value on its investments. Put another way, there is no excuse for a firm to invest in risky assets expecting to generate negative net present values, when it can invest in the risk free asset.

#### *Financing Policy*

When firms borrow money, one concern that both firms and lenders have is their capacity to repay that money. If a firm has accumulated cash that is invested in a riskless (and liquid) investment, it is reasonable to assume that this cash can be used to cover at least some of its debt obligations, when they come due. This is why it is common practice in many parts of the world to compute debt ratios and to measure financial leverage using net debt, which is the difference between debt owed and cash and marketable securities.

Net Debt = Gross debt – Cash and marketable securities

Thus, a firm that has \$ 10 billion in debt outstanding, with a cash balance of \$ 10 billion, has net debt of zero and is treated on par with another firm that has no debt and no cash on its balance sheet, a parity made possible by the assumption that cash is riskless and

To the extent that firms have at least of some of their investments in riskless assets, it also affects measures of default risk and cost of debt. Ratings agencies, for instance, weigh in the presence of cash and other riskless assets on the balance sheet, when assigning bond ratings, and the cost of debt for a company will be lower, if a larger portion of its assets is invested in riskless assets.

## *Dividend Policy*

When a firm has a cash surplus from operations, after meeting its reinvestment needs and debt obligations, it can pay the cash out as a dividend, use it buy back stock or retain it as a cash balance. Miller and Modigliani (1961) made an argument that dividend policy is irrelevant in value determination, i.e., that firm value is unaffected by whether a company pays out cash or retains it, that is at least implicitly based upon the existence of a riskless asset. Their argument can be summarized as follows. A firm that pays too little in dividends, relative to cash available for payouts, can always invest the cash in the risk free asset and thus leave investors unaffected in terms of overall returns, by substituting price appreciation for dividends. While any zero net present value investment will accomplish the same purpose, the presence of a riskless asset that delivers the riskless rate makes it far simpler for firms to accomplish.

#### **Portfolio Management**

As we noted in our earlier discussion of efficient portfolios, the riskfree asset plays an outsized role in portfolio management. It is not only a key driver of investors' asset allocation decisions but is also a part of active equity investors' tool kits for managing risk and for timing markets.

### *Asset Allocation*

The first step in portfolio management is asset allocation, where the decision is made about how much money to invest in different risky asset classes – stocks, corporate bonds, real assets – and how much to invest in the riskless asset. The presence of a riskless investment allows for more separation between investment decisions and risk profiles. In the absence of a riskless asset, risk seeking investors will have to see out much riskier stocks to hold, whereas risk averse investors will screen for safer and more secure companies. In the process, both groups will have to give up on some diversification; the former may never be able to hold mature, stable companies whereas the latter will have to avoid technology and high growth companies. With a riskless asset, both groups of investors can hold a much wider array of assets (and in some cases, even the same well diversified portfolio) and use the proportion invested in the riskless asset to alter the overall risk exposure of the portfolio.

In the context of financial planning, this asset allocation decision sometimes takes the form of allocation mixes that are tied to age, with the proportion invested in treasury bills or money market accounts increasing as investors age (and presumably have a greater need for liquidity and are more risk averse).3 Implicit in this mechanism is the assumption that treasuries (and by extension, money market funds) are riskless.

# *Risk buffer and Market Timing*

Equity money managers use investments in riskless assets as a way of both adjusting overall portfolio risk exposure and as a market timing mechanism.

<sup>3</sup> In one of its simplest variants, called the 120 rule, subtracting your age from 120 yields the percent of your portfolio that should be invested in stocks. Thus, the proportion invested in stocks will drop from 75%, for a 45-year old, to 50%, for a 70-year old.

 Risk buffer: Holdings of treasury bills and other liquid, riskless investments at mutual funds usually increase in the midst of a crisis and decrease when money managers become less concerned about risk. In effect, rather than changing the mix or the types of companies that they invest in, mutual fund managers use cash holdings to adjust overall risk exposure. Market Timing: A more controversial use of riskless investments is as a markettiming device, where bearish equity mutual fund mangers sell stocks and buy treasury bills and bullish managers do the reverse. The controversy stems from the empirical finding that mutual funds do not seem to be good market timers and there are investors who use mutual fund cash holdings as a contrarian indicator: a move by mutual fund managers into (away from) cash is considered a bullish (bearish) sign.

The degree to which equity mutual fund managers use treasury bills (cash) as a investment tool is measured in table 1, which lists equity mutual fund cash holdings as a percent of overall portfolio value over time and returns on the S&P 500 each year from 1985 to 2009.

*Table 1: Cash as % of mutual fund assets and Stock Returns: 1985-2009*

|      | Cash as % of fund value at the end of year | Change in cash holdings over prior year | Return on S&P 500 in following year |
|------|--------------------------------------------|-----------------------------------------|-------------------------------------|
| 1984 | 9.10%                                      |                                         |                                     |
| 1985 | 9.40%                                      | 0.30%                                   | 12.46%                              |
| 1986 | 9.50%                                      | 0.10%                                   | 0.09%                               |
| 1987 | 9.30%                                      | -0.20%                                  | 10.09%                              |
| 1988 | 9.40%                                      | 0.10%                                   | 23.37%                              |
| 1989 | 10.40%                                     | 1.00%                                   | -10.61%                             |
| 1990 | 11.40%                                     | 1.00%                                   | 24.62%                              |
| 1991 | 7.60%                                      | -3.80%                                  | 4.09%                               |
| 1992 | 8.30%                                      | 0.70%                                   | 6.98%                               |
| 1993 | 7.80%                                      | -0.50%                                  | -2.66%                              |
| 1994 | 8.30%                                      | 0.50%                                   | 31.68%                              |
| 1995 | 7.80%                                      | -0.50%                                  | 18.79%                              |
| 1996 | 6.20%                                      | -1.60%                                  | 26.81%                              |
| 1997 | 6.10%                                      | -0.10%                                  | 23.61%                              |
| 1998 | 4.80%                                      | -1.30%                                  | 16.38%                              |

| 1999 | 4.30% | -0.50% | -14.79% |
|------|-------|--------|---------|
| 2000 | 5.80% | 1.50%  | -15.52% |
| 2001 | 5.00% | -0.80% | -23.62% |
| 2002 | 4.60% | -0.40% | 27.33%  |
| 2003 | 4.30% | -0.30% | 9.52%   |
| 2004 | 4.20% | -0.10% | 1.82%   |
| 2005 | 3.90% | -0.30% | 10.94%  |
| 2006 | 3.90% | 0.00%  | 0.84%   |
| 2007 | 4.20% | 0.30%  | -38.16% |
| 2008 | 5.20% | 1.00%  | 25.79%  |
| 2009 | 3.60% | -1.60% | ?       |

Cash as a percent of overall fund value has ranged from a low of 3.60% at the end of 2009 to a high of 11.40% at the end of 1990. Note also that cash holdings increase during market dips and decrease in the course of market upturns, a finding that runs counter to market timing, with cash holdings increasing (decreasing) prior to market downturns (upturns). Thus, cash holdings in 1999 decreased to 4.30% from 4.80% at the end of 1998, as the S&P 500 increased by 16.38% during the year. When the market dropped by almost 15% in 2000, cash holdings increased from 4.30% to 5.80% during the year.

# **A History of Sovereign Default**

If a prerequisite for an investment to be riskfree is that the entity issuing it has no default risk, the only entities that have a chance at issuing riskfree investments are governments, since any private business or entity will have at least a residue of default risk. Governments, when issuing debt in the local currency, have the unique power to print money to pay their obligations and thus can avoid default. As we will see in this section, though, that power does not give governments immunity from default.

# **Sovereign Defaults over time**

In this section, we will examine the history of sovereign default, by first looking at governments that default on foreign currency debt (which is understandable) and then looking at governments that default on local currency debt (which is more difficult to explain).

#### *Foreign Currency Defaults*

Through time, many governments have been dependent on debt borrowed from other countries (or banks in those countries), usually denominated in a foreign currency. A large proportion of sovereign defaults have occurred with this type of sovereign borrowing, as the borrowing country finds its short of the foreign currency to meet its obligations, without the recourse of being able to print money in that currency.

Starting with the most recent history from 2000-2010, sovereign defaults have mostly been on foreign currency debt, starting with a relatively small default by Ukraine in January 2000, followed by the largest sovereign default of the last decade with Argentina in November 2001. Table 2 lists the sovereign defaults, with details of each:

*Table 2: Sovereign Defaults: 2000-2010*

| Default Date                            |           |         |
|-----------------------------------------|-----------|---------|
| Country \$ Value of Defaulted           |           |         |
| Debt (millions)                         |           |         |
| January 2000 Ukraine \$1,064 m          |           |         |
| Defaulted                               |           | on DM   |
| and                                     | US dollar |         |
| denominated                             |           | bonds.  |
| Offered                                 | exchange  | for     |
| longer                                  | term,     | lower   |
| coupon                                  | bonds     | to      |
| September 2000 Peru \$4,870 m           |           |         |
| November 2001 Argentina \$82,268 m      |           |         |
| Debt                                    |           | was     |
| January 2002 Moldova \$145 m            |           |         |
| bond                                    | but       | bought  |
| May 2003 Uruguay \$5,744 m              |           |         |
| Contagion                               |           | effect  |
| from                                    | Argentina | led     |
| April 2005 Dominican Republic \$1,622 m |           |         |
| Defaulted                               |           | on debt |
| and                                     | exchanged | for     |
| new                                     | bonds     | with    |
| December 2006 Belize \$242 m            |           |         |
| and                                     | exchanged | for     |

Going back further in time, sovereign defaults have occurred have occurred frequently over the last two centuries, though the defaults have been bunched up in eight periods. A survey article on sovereign default, Hatchondo, Martinez and Sapriza (2007) summarizes defaults over time for most countries in Europe and Latin America and their findings are captured in table 3:4

*Table 3: Defaults over time: 1820-2003*

|                    | 1824- 34 | 1867- 82 | 1890- 1900 Europe | 1911- 1921 | 1931- 40 | 1976- 89 | 1998- 2003 |
|--------------------|----------|----------|-------------------|------------|----------|----------|------------|
| Austria            |          | 1868     |                   | 1914       | 1932     |          |            |
| Bulgaria           |          |          |                   | 1915       | 1932     |          |            |
| Germany            |          |          |                   |            | 1932     |          |            |
| Greece             | 1824     |          | 1893              |            |          |          |            |
| Hungary            |          |          |                   |            | 1931     |          |            |
| Italy              |          |          |                   |            | 1940     |          |            |
| Moldova            |          |          |                   |            |          |          | 2002       |
| Poland             |          |          |                   |            | 1936     | 1981     |            |
| Portugal           | 1834     |          | 1892              |            |          |          |            |
| Romania            |          |          |                   | 1915       | 1933     | 1981     |            |
| Russia Serbia     |          |          |                   | 1917       |          |          | 1998       |
| Yugoslavia         |          |          | 1895              |            | 1933     | 1983     |            |
| Spain              | 1831     | 1867     |                   |            |          |          |            |
| Turkey             |          | 1976     |                   | 1915       | 1940     | 1978     |            |
| Ukraine            |          |          |                   |            |          |          | 1998       |
|                    |          |          | Latin             | America    |          |          |            |
| Argentina          | 1830     |          | 1890              | 1915       | 1930     | 1982     | 2001       |
| Bolivia            |          | 1874     |                   |            | 1931     | 1980     |            |
| Brazil             | 1826     |          | 1898              | 1914       | 1931     | 1983     |            |
| Chile              | 1826     | 1880     |                   |            | 1931     | 1983     |            |
| Columbia           | 1826     | 1879     | 1900              |            | 1932     |          |            |
| Costa Rica         | 1827     | 1874     | 1895              |            | 1937     | 1983     |            |
| Cuba               |          |          |                   |            | 1933     | 1982     |            |
| Dominica Dominican |          |          |                   |            |          |          | 2003       |
| Republic           |          | 1869     | 1899              |            | 1931     | 1982     |            |
| Ecuador            | 1832     | 1868     |                   | 1911, '14  | 1931     | 1982     | 1999       |

<sup>4</sup> J.C. Hatchondo, L. Martinez, and H. Sapriza, 2007, *The Economics of Sovereign Default*, Economic Quarterly, v93, pg 163-187.

| El Salvador | 1827 |      |      | 1921 | 1931 |      |      |
|-------------|------|------|------|------|------|------|------|
| Guatemala   | 1828 | 1876 | 1894 | 1933 |      |      |      |
| Honduras    | 1827 | 1873 |      | 1914 |      | 1981 |      |
| Mexico      | 1827 | 1867 |      | 1914 |      | 1982 |      |
| Nicaragua   | 1828 |      | 1894 | 1911 | 1932 | 1980 |      |
| Panama      |      |      |      |      | 1932 | 1982 |      |
| Paraguay    | 1827 | 1874 | 1892 | 1920 | 1932 | 1986 |      |
| Peru        | 1826 | 1876 |      |      | 1931 | 1983 |      |
| Uruguay     |      | 1876 | 1892 |      |      | 1983 | 2003 |
| Venezuela   | 1832 | 1878 | 1892 |      |      | 1982 |      |

While table 3 does not list defaults in Asia and Africa, there have been defaults in those regions over the last 50 years as well. Thus, most of the countries in Africa as well as Pakistan, Philippines and Vietnam defaulted in the 1980s.

In a study of sovereign defaults between 1975 and 2004, Standard and Poor's notes the following facts about the phenomenon:5

- 1. Countries have been more likely to default on bank debt owed than on sovereign bonds issued. Figure 4 summarizes default rates on each:

*Figure 4*

![](_page_17_Figure_7.jpeg)

<sup>5</sup> S&P Ratings Report, "Sovereign Defaults set to fall again in 2005, September 28, 2004.

Note that while bank loans were the only recourse available to governments that wanted to borrow prior to the 1960s, sovereign bond markets have expanded access in the last few decades. Defaults since then have been more likely on foreign currency debt than on foreign currency bonds.

- 2. In dollar value terms, Latin American countries have accounted for much of sovereign defaulted debt in the last 50 years. Figure 5 summarizes the statistics:

*Figure 5*

![](_page_18_Figure_4.jpeg)

In fact, the 1990s represent the only decade in the last 5 decades, where Latin American countries did not account for 60% or more of defaulted sovereign debt.

Since Latin America has been at the epicenter of sovereign default for most of the last two centuries, we may be able to learn more about why default occurs by looking at its history, especially in the nineteenth century, when the region was a prime destination for British, French and Spanish capital. Lacking significant domestic savings and

possessing the allure of natural resources, the newly independent countries of Latin American countries borrowed heavily, usually in foreign currency or gold and for very long maturities (exceeding 20 years). Brazil and Argentina also issued domestic debt, with gold clauses, where the lender could choose to be paid in gold. The primary trigger for default was military conflicts between countries or coups within, with weak institutional structures exacerbating the problems. Of the 77 government defaults between 1820 and 1914, 58 were in Latin America and as figure 6 indicates, these countries collectively spent 38% of the period between 1820 and 1940 in default.

Figure 6

### Latin America: Periods in Default, 1825–1940

![](_page_19_Figure_49.jpeg)

Sources: Taylor (2003); default data from Tomz (2001); issue dates from Marichal (1989).

The percentage of years that each country spent in default during the entire period is in parentheses next to the country; for instance, Honduras spent 79% of the 115 years in default.

#### **Consequences of Default**

What happens when a government defaults? In the eighteenth century, government defaults were followed often by shows of military force. When Turkey defaulted in the 1880s, the British and the French governments intervened and appointed commissioners to oversee the Ottoman Empire to ensure discipline. When Egypt defaulted around the same point in time, the British used military force to take over the government. A default by Venezuela in the early part of the 20th century led to a European blockade of that country and a reaction from President Theodore Roosevelt and the United States government, who viewed the blockade as the a threat to the US power in the hemisphere.

In the twentieth century, the consequences of sovereign default have been both economic and political. Besides the obvious implication that lenders to that government lose some or a great deal of what is owed to them, there are other consequences as well:

- a. Reputation loss: A government that defaults is tagged with the "deadbeat" label for years after the event, making it more difficult for it to raise financing in future rounds.
- b. Capital Market turmoil: Defaulting on sovereign debt has repercussions for all capital markets. Investors withdraw from equity and bond markets, making it more difficult for private enterprises in the defaulting country to raise funds for projects.
- c. Real Output: The uncertainty created by sovereign default also has ripple effects on real investment and consumption. In general, sovereign defaults are followed by economic recessions, as consumers hold back on spending and firms are reluctant to commit resources to long-term investments.
- d. Political Instability: Default can also strike a blow to the national psyche, which in turn can put the leadership class at risk. The wave of defaults that swept through Europe in the 1930s, with Germany, Austria, Hungary and Italy all falling victim, allowed for the rise of the Nazis and set the stage for the Second World War. In Latin America, defaults and coups have gone hand in hand for much of the last two centuries.

In short, sovereign default has serious and painful effects on the defaulting entity that may last for long periods.

It is also worth emphasizing is that default has seldom involved total repudiation of the debt. Most defaults are followed by negotiations for either a debt exchange or restructuring, where the defaulting government is given more time, lower principal and/or lower interest payments. Credit agencies usually define the duration of a default episode as lasting from when the default occurs to when the debt is restructured. Defaulting governments can mitigate the reputation loss and return to markets sooner, if they can minimize losses to lenders.

Researchers who have examined the aftermath of default have come to the following conclusions about the short and long term effects of defaulting on debt:

- a. Default has a negative impact on real GDP growth of between 0.5% and 2%, but the bulk of the decline is in the first year after the default and seems to be short lived.
- b. Default does affect a country's sovereign rating and borrowing costs. One study of credit ratings in 1995 found that the ratings for countries that had defaulted at least once since 1970 were one to two notches lower than otherwise similar countries that had not defaulted. In the same vein, defaulting countries have borrowing costs that are about 0.5 to 1% higher than countries that have not defaulted. Here again, though, the effects of default dissipate over time.
- c. Sovereign default can cause trade retaliation. One study indicates a drop of 8% in bilateral trade after default, with the effects lasting for up to 15 years, and another one that uses industry level data finds that export oriented industries are particularly hurt by sovereign default.
- d. Sovereign default can make banking systems more fragile. A study of 149 countries between 1975 and 2000 indicates that the probability of a banking crisis is 14% in countries that have defaulted, an 11 percentage-point increase over nondefaulting countries.
- e. Sovereign default also increases the likelihood of political change. While none of the studies focus on defaults per se, there are several that have examined the after effects of sharp devaluations, which often accompany default. A study of

devaluations between 1971 and 2003 finds a 45% increase in the probability of change in the top leader (prime minister or president) in the country and a 64% increase in the probability of change in the finance executive (minister of finance or head of central bank).

In summary, default is costly and countries do not (and should not) take the possibility of default lightly. Default is particularly expensive when it leads to banking crises and currency devaluations; the former have a longstanding impact on the capacity of firms to fund their investments whereas the latter create political and institutional instability that lasts for long periods.

## **The special case of local currency debt**

While defaulting on foreign currency debt draws more headlines, some of the countries listed in tables 2 and 3 also defaulted contemporaneously on domestic currency debt. <sup>6</sup> A survey of defaults by S&P since 1975 notes that 23 issuers have defaulted on local currency debt, including Argentina (2002-2004), Madagascar (2002), Dominica (2003-2004), Mongolia (1997-2000), Ukraine (1998-2000), and Russia (1998-1999). Russia's default on \$39 billion worth of ruble debt stands out as the largest local currency default since Brazil defaulted on \$62 billion of local currency debt in 1990. Figure 7 summarizes the percentage of countries that defaulted in local currency debt between 1975 and 2004 and compares it to sovereign defaults in foreign currency. 7

<sup>6</sup> In 1992, Kuwait defaulted on its local currency debt, while meeting its foreign currency obligations.

<sup>7</sup> S&P Ratings Report, "Sovereign Defaults set to fall again in 2005, September 28, 2004.

*Figure 7: Defaults on Foreign and Local Currency Debt*

![](_page_23_Figure_2.jpeg)

While it is easy to see how countries can default on foreign currency debt, it is more difficult to explain why they default on local currency debt. As some have argued, countries should be able to print more of the local currency to meet their obligations and thus should never default. There are three reasons why local currency default occurs and will continue to do so.

The first two reasons for default in the local currency can be traced to a loss of power in printing currency.

- a. Gold Standard: In the decades prior to 1971, when some countries followed the gold standard, currency had to be backed up with gold reserves. As a consequence, the extent of these reserves put a limit on how much currency could be printed.
- b. Shared Currency: The crisis in Greece has brought home one of the costs of a shared currency. When the Euro was adopted as the common currency for the Euro zone, the countries involved accepted a trade off. In return for a common market and the convenience of a common currency, they gave up the power to control how much of the currency they could print. Thus, the Greek government cannot print more Euros to pay off outstanding debt.

The third reason for local currency default is more intriguing. In the last section, we noted that default has negative consequences: reputation loss, economic recessions and political instability. The alternative of printing more currency to pay debt obligations also has costs. It debases and devalues the currency and causes inflation to increase exponentially, which in turn can cause the real economy to shrink. Investors abandon financial assets (and markets) and move to real assets (real estate, gold) and firms shift from real investments to financial speculation. Countries therefore have to trade off between which action – default or currency debasement – has lower long-term costs and pick one; many choose default as the less costly option.

An intriguing explanation for why some countries choose to default in local currency debt whereas other prefer to print money (and debase their currencies) is based on whether companies in the country have foreign currency debt funding local currency assets. If they do, the cost of printing more local currency, pushing up inflation and devaluing the local currency, can be catastrophic for corporations, as the local currency devaluation lays waste to assets while liabilities remain relatively unchanged.

# **Measuring Sovereign Default Risk**

If governments can default, we need measures of sovereign default risk not only to set interest rates on sovereign bonds and loans but to price all other assets. In this section, we will first look at why governments default and then at how ratings agencies, markets and services measure this default risk.

# **Factors determining sovereign default risk**

Governments default for the same reason that individuals and firms default. In good times, they borrow far more than they can afford, given their assets and earning power, and then find themselves unable to meet their debt obligations during downturns. To determine a country's default risk, we would look at the following variables:

- a. Degree of indebtedness: The most logical place to start assessing default risk is by looking at how much a sovereign entity owes not only to foreign banks/ investors but also to its own citizens. Since larger countries can borrow more money, in absolute terms, the

debt owed is usually scaled to the GDP of the country. Table 4 lists the 20 countries that owe the most, relative to GDP, in 2010. 8

*Table 4: Debt as % of Gross Domestic Product*

| Ranking | Country               | Debt as % of GDP |
|---------|-----------------------|------------------|
| 1       | Zimbabwe              | 304.30%          |
| 2       | Japan                 | 192.10%          |
| 3       | Saint Kitts and Nevis | 185.00%          |
| 4       | Lebanon               | 156.00%          |
| 5       | Jamaica               | 131.70%          |
| 6       | Singapore             | 117.60%          |
| 7       | Italy                 | 115.20%          |
| 8       | Greece                | 113.40%          |
| 9       | Sudan                 | 104.50%          |
| 10      | Belgium               | 99.00%           |
| 11      | Iceland               | 95.10%           |
| 12      | Nicaragua             | 87.00%           |
| 13      | Sri Lanka             | 82.90%           |
| 14      | Egypt                 | 79.80%           |
| 15      | France                | 79.70%           |
| 16      | Hungary               | 78.00%           |
| 17      | Israel                | 78.00%           |
| 18      | Germany               | 77.20%           |
| 19      | Portugal              | 75.20%           |
| 20      | Canada                | 72.30%           |

The list suggests that this statistic (debt as percent of GDP) is an incomplete measure of default risk. The list includes some countries with high default risk (Zimbabwe, Sudan, Nicaragua, Sri Lanka) but is also includes some countries that were viewed as credit worthy by ratings agencies and markets (Japan, Germany and Canada). However, the list did also include Portugal, Greece and Italy, countries that entered 2009 with high credit ratings, but that have seen a surge in default risk in recent months. As a final note, it is worth looking at how this statistic has changed in the United States over its lifetime. Figure 8 shows public debt as a percent of GDP for the US from 1790 to 2010:9

<sup>8</sup> The World Factbook, 2010, Central Intelligence Agency.

<sup>9</sup> The statistic varies depending upon the data source you use, with some reporting higher numbers and others lower. This data was obtained from usgovernmentspending.com.

*Figure 8*

![](_page_26_Figure_2.jpeg)

At 94% of GDP, federal debt in the United States is approaching levels not seen since the Second World War. If there is a link between debt levels and default risk, it is not surprising that questions about default risk in the US government have risen to the surface.

In addition to traditional debt obligations, governments also make commitments to their citizens to pay pensions and cover health care. Since these obligations also compete for the limited revenues that the government has, countries that have larger commitments on these counts should have higher default risk than countries that do not. 10

- b. Revenues/Inflows to government: Government revenues usually come from tax receipts, which in turn are a function of both the tax code and the tax base. Holding all else constant, access to a larger tax base should increase potential tax revenues, which, in turn, can be used to meet debt obligations.

<sup>10</sup> Since pension and health care costs increase as people age, countries with aging populations (and fewer working age people) face more default risk.

- c. Stability of revenues: The essence of debt is that it gives rise to fixed obligations that have be covered in both good and bad times. Countries with more stable revenue streams should therefore face less default risk, other things remaining equal, than countries with volatile revenues. But what is it that drives revenue stability? Since revenues come from taxing income and consumption in the nation's economy, countries with more diversified economies should have more stable tax revenues than countries that are dependent on one or a few sectors for their prosperity. To illustrate, Peru, with its reliance on copper and silver production and Jamaica, an economy dependent upon tourism, face more default risk than Brazil or India, which are larger, more diversified economies. The other factor that determines revenue stability is type of tax system used by the country. Generally, income tax based systems generate more volatile revenues than sales tax (or value added tax systems).
- d. Political risk: Ultimately, the decision to default is as much a political decision as it is an economic decision. Given that sovereign default often exposes the political leadership to pressure, it is entirely possible that autocracies (where there is less worry about political backlash) are more likely to default than democracies. Since the alternative to default is printing more money, the independence and power of the central bank will also affect assessments of default risk.
- e. Implicit backing from other entities: When Greece, Portugal and Spain entered the European Union, investors, analysts and ratings agencies reduced their assessments of default risk in these countries. Implicitly, they were assuming that the stronger European Union countries – Germany, France and the Scandinavian countries – would step in to protect the weaker countries from defaulting. The danger, of course, is that the backing is implicit and not explicit, and lenders may very well find themselves disappointed by lack of backing, and no legal recourse.

In summary, a full assessment of default risk in a sovereign entity requires the assessor to go beyond the numbers and understand how the country's economy works, the strength of its tax system and the trustworthiness of its governing institutions.

#### **Sovereign Ratings**

Since few of us have the resources or the time to dedicate to understanding small and unfamiliar countries, it is no surprises that third parties have stepped into the breach, with their assessments of sovereign default risk. Of these third party assessors, bond ratings agencies came in with the biggest advantages:

- (1) They have been assessing default risk in corporations for a hundred years and presumable can transfer some of their skills to assessing sovereign risk.
- (2) Bond investors who are familiar with the ratings measures, from investing in corporate bonds, find it easy to extend their use to assessing sovereign bonds. Thus, a AAA rated country is viewed as close to riskless whereas a C rated country is very risky.

In spite of these advantages, there are critiques that have been leveled at ratings agencies by both the sovereigns they rate and the investors that use these ratings. In this section, we will begin by looking at how ratings agencies come up with sovereign ratings (and change them) and then evaluate how well sovereign ratings measure default risk.

# *The evolution of sovereign ratings*

Moody's, Standard and Poor's and Fitch's have been rating corporate bond offerings since the early part of the twentieth century. Moody's has been rating corporate bonds since 1919 and starting rating government bonds in the 1920s, when that market was an active one. By 1929, Moody's provided ratings for almost fifty central governments. With the great depression and the Second World War, investments in government bonds abated and with it, the interest in government bond ratings. In the 1970s, the business picked up again slowly. As recently as the early 1980s, only about fifteen, more mature governments had ratings, with most of them commanding the highest level (Aaa). The decade from 1985 to 1994 added 35 companies to the sovereign rating list, with many of them having speculative or lower ratings. Table 5 summarizes the growth of sovereign ratings from 1975 to 1994:

*Table 5: Sovereign Ratings – 1975-1995*

|          | Number of newly rated sovereigns | Median rating |  |
|----------|----------------------------------|---------------|--|
| Pre-1975 | 3                                | AAA/Aaa       |  |

| 1975- 79  | 9  | AAA/Aaa   |
|-----------|----|-----------|
| 1980-84   | 3  | AAA/Aaa   |
| 1985-1989 | 19 | A/A2      |
| 1990-94   | 15 | BBB-/Baa3 |

Since 1994, the number of countries with sovereign ratings has surged, just as the market for sovereign bonds has expanded. In 2010, Moody's and S&P had ratings available for almost a hundred countries, with Fitch a more recent entrant into the business.

In addition to more countries being rated, the ratings themselves have become richer. Moody's and S&P now provide two ratings for each country – a local currency rating (for domestic currency debt/ bonds) and a foreign currency rating (for government borrowings in a foreign currency). As an illustration, table 6 summarizes the local and foreign currency ratings, from Moody's, for Latin American countries in 2010:

*Table 6: Local and Foreign Currency Ratings – Latin America in January 2010*

|            | Foreign Currency Rating | Local Currency Rating |
|------------|-------------------------|-----------------------|
| Argentina  | B3                      | B3                    |
| Bolivia    | B2                      | B2                    |
| Brazil     | Baa3                    | Baa3                  |
| Chile      | A1                      | A1                    |
| Colombia   | Ba1                     | Baa3                  |
| Costa Rica | Ba1                     | Ba1                   |
| Ecuador    | Caa3                    | Caa3                  |
| Guatemala  | Ba2                     | Ba1                   |
| Honduras   | B2                      | B2                    |
| Mexico     | Baa1                    | Baa1                  |
| Nicaragua  | Caa1                    | B3                    |
| Panama     | Ba1                     | Ba1                   |
| Paraguay   | B3                      | B3                    |
| Peru       | Baa3                    | Baa3                  |
| Uruguay    | Ba3                     | Ba3                   |
| Venezuela  | B2                      | B1                    |

For the most part, local currency ratings are at least as high or higher than the foreign currency rating, for the obvious reason that governments have more power to print more of their own currency . There are, however, notable exceptions, where the local currency

rating is lower than the foreign currency rating. In March 2010, for instance, India was assigned a local currency rating of Ba2 and a foreign currency rating of Baa3.

Do the ratings agencies agree on sovereign risk? For the most part, there is consensus in the ratings, but there can be significant differences on individual countries. These differences can come from very different assessments of political and economic risk in these countries by the ratings teams at the different agencies.

Do sovereign ratings change over time? Yes, but far less than corporate ratings do. The best measure of sovereign ratings changes is a ratings transition matrix. Using Fitch ratings to illustrate our point, table 7 summarizes the annual probability of ratings transitions, by rating, from 1995 to 2008.

*Table 7: Annual Ratings Transitions – 1995 to 2008*

**Fitch Sovereign Transition Rates Across the Major Rating Categories:  
1995–2008**

(%, Average Annual)

|          | AAA   | AA    | A     | BBB   | BB    | B     | CCC to C | D     | Total  |
|----------|-------|-------|-------|-------|-------|-------|----------|-------|--------|
| AAA      | 99.42 | 0.58  | 0.00  | 0.00  | 0.00  | 0.00  | 0.00     | 0.00  | 100.00 |
| AA       | 4.12  | 94.12 | 1.18  | 0.00  | 0.00  | 0.59  | 0.00     | 0.00  | 100.00 |
| A        | 0.00  | 3.55  | 92.91 | 3.55  | 0.00  | 0.00  | 0.00     | 0.00  | 100.00 |
| BBB      | 0.00  | 0.00  | 8.11  | 87.84 | 3.38  | 0.68  | 0.00     | 0.00  | 100.00 |
| BB       | 0.00  | 0.00  | 0.00  | 9.04  | 83.51 | 5.85  | 0.00     | 1.60  | 100.00 |
| B        | 0.00  | 0.00  | 0.00  | 0.00  | 12.12 | 84.09 | 3.03     | 0.76  | 100.00 |
| CCC to C | 0.00  | 0.00  | 0.00  | 0.00  | 0.00  | 23.08 | 53.85    | 23.08 | 100.00 |

Source: Fitch.

This table provides evidence on how little sovereign ratings change on an annual basis, especially for higher rated countries. A AAA rated sovereign has a 99.42% chance of remaining AAA rated the next year; a BBB rated sovereign has an 8.11% chance of being upgraded, an 87.84% chance of remaining unchanged and a 4.06% chance of being downgraded. The ratings transition tables at Moody's and S&P tell the same story of ratings stickiness. As we will see later in this paper, one of the critiques of sovereign ratings is that they do not change quickly enough to alert investors to imminent danger.

As the number of rated countries around the globe increases, we are opening a window on how ratings agencies assess risk at the broader regional level. Figure 9 summarizes S&P's ratings around the globe, classified by continent.

*Figure .9: S&P Sovereign Ratings Map*

![](_page_31_Figure_2.jpeg)

One of the criticisms that rated countries have mounted against the ratings agencies is that they have regional biases, leading them to under rate entire continents such as Latin America and over rate others (Europe and North America). The defense that ratings agencies would offer is that past default history is a good predictor of future default and that Latin America has a great deal of history to live down.

# *What goes into a sovereign rating?*

The ratings agencies started with a template that they developed and fine tuned with corporations and have modified it to estimate sovereign ratings. While each agency has its own system for estimating sovereign ratings, the processes share a great deal in common.

 Ratings Measure: A sovereign rating is focused on the credit worthiness of the sovereign to private creditors (bondholders and private banks) and not to official creditors (which may include the World Bank, the IMF and other entities). Ratings agencies also vary on whether their rating captures only the probability of default or also incorporates the expected severity, if it does occur. S&P's ratings are designed to capture the probability that default will occur and not necessarily the severity of the default, whereas Moody's focus on both the probability of default and severity (captured in the expected recovery rate). Default at all of the agencies is defined as either a failure to pay interest or principal on a debt instrument on the due date (outright default) or a rescheduling, exchange or other restructuring of the debt (restructuring default).

 Determinants of ratings: In a publication that explains its process for sovereign ratings, Standard and Poor's lists out the variables that it considers when rating a country. These variables encompass both political, economic and institutional variables and are summarized in table 8:

*Table 8: Factors considered while assigning sovereign ratings*

While Moody's and Fitch have their own set of variables that they use to estimate sovereign ratings, they parallel S&P in their focus on economic, political and institutional detail.

 Rating process: The analyst with primary responsibility for the sovereign rating prepares a ratings recommendation with a draft report, which is then assessed by a ratings committee composed of 5-10 analysts, who debate each analytical category and vote on a score. Following closing arguments, the ratings are decided by a vote of the committee. Local versus Foreign Currency Ratings: As we noted earlier, the ratings agencies usually assign two ratings for each sovereign – a local currency rating and a foreign currency rating. There are two approaches used by ratings agencies to differentiate between these ratings. In the first, called the notch-up approach, the foreign currency rating is viewed as the primary measure of sovereign credit risk and the local currency rating is notched up, based upon domestic debt market factors. In the notch down approach, it is the local currency rating that is the anchor, with the foreign currency rating notched down, reflecting foreign exchange constraints. The differential between foreign and local currency ratings is primarily a function of monetary policy independence. Countries that maintain floating rate exchange regimes and fund borrowing from deep domestic markets will have the largest differences between local and foreign currency ratings, whereas countries that have given up monetary policy independence, either through dollarization or joining a monetary union, will see local currency ratings converge on foreign currency ratings. Ratings Review and Updates: Sovereign ratings are reviewed and updated by the ratings agencies and these reviews can be both at regular periods and also triggered by news items. Thus, news of a political coup or an economic disaster can lead to a ratings review not just for the country in question but for surrounding countries (that may face a contagion effect).

# *Do sovereign ratings measure default risk?*

The sales pitch from ratings agencies for sovereign ratings is that they are effective measures of default risk in bonds (or loans) issued by that sovereign. But do they work as advertised? Each of the ratings agencies goes to great pains to argue that notwithstanding errors on some countries, there is a high correlation between sovereign

ratings and sovereign defaults. In table 9, we summarize Fitch's estimates of cumulative default rates for bonds in each ratings class from 1995 to 2008:

*Table 9: Fitch Sovereign Ratings and Default Probabilities*

---

**Fitch Sovereign Ratings Average Cumulative Default Rates: 1995–2008**

(%)

|                   | One-Year | Two-Year | Three-Year | Four-Year | Five-Year |
|-------------------|----------|----------|------------|-----------|-----------|
| AAA               | 0.00     | 0.00     | 0.00       | 0.00      | 0.00      |
| AA                | 0.00     | 0.00     | 0.00       | 0.00      | 0.00      |
| A                 | 0.00     | 0.00     | 0.00       | 0.00      | 0.00      |
| BBB               | 0.00     | 0.75     | 1.68       | 2.83      | 4.21      |
| BB                | 1.60     | 3.05     | 4.20       | 5.69      | 6.36      |
| B                 | 0.75     | 3.51     | 5.26       | 7.50      | 7.94      |
| CCC to C          | 21.43    | 15.38    | 16.67      | 18.18     | 25.00     |
| Investment Grade  | 0.00     | 0.18     | 0.39       | 0.66      | 1.00      |
| Speculative Grade | 2.09     | 3.78     | 5.20       | 7.01      | 7.73      |
| All               | 0.72     | 1.39     | 1.97       | 2.69      | 3.10      |

Source: Fitch.

---

Standard and Poor's provide their estimates of default rate for different ratings classes for both sovereign and corporate ratings from 1975-2007 in table 10:

*Table 10: S&P Sovereign Ratings and Default Probabilities*

| Sovereign And Corporate Default Rate Comparison |           |                |            |                |           |                |
|-------------------------------------------------|-----------|----------------|------------|----------------|-----------|----------------|
| (% of rated issuers)                            | One-year  |                | Three-year |                | Five-year |                |
|                                                 | Sovereign | Private sector | Sovereign  | Private sector | Sovereign | Private sector |
| AAA                                             | 0.0       | 0.0            | 0.0        | 0.1            | 0.0       | 0.3            |
| AA                                              | 0.0       | 0.0            | 0.0        | 0.1            | 0.0       | 0.3            |
| A                                               | 0.0       | 0.1            | 0.0        | 0.3            | 0.0       | 0.6            |
| BBB                                             | 0.0       | 0.2            | 1.8        | 1.1            | 4.7       | 2.4            |
| BB                                              | 0.9       | 1.0            | 4.5        | 5.2            | 7.8       | 9.3            |
| B                                               | 1.7       | 4.6            | 7.3        | 14.7           | 14.3      | 21.1           |
| CCC/CC                                          | 38.9      | 25.6           | 52.9       | 39             | 52.9      | 44.5           |

Note: Implied senior debt ratings through 1995; issuer credit ratings thereafter. Sovereign foreign currency ratings cover 1975-2007; private sector local currency ratings cover 1981-2007.

Moody's lists default rates for sovereign rating categories from 1985-2007 in table 11:

*Table 11: Moody's Sovereign Ratings and Default Probabilities*

| Issuer-Weighted Cumulative Default Rates (1983-2007) |         |         |         |         |         |         |         |         |         |         |
|------------------------------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|                                                      | Year1   | Year2   | Year 3  | Year 4  | Year 5  | Year 6  | Year 7  | Year 8  | Year 9  | Year 10 |
| <b>Sovereign</b>                                     |         |         |         |         |         |         |         |         |         |         |
| Aaa                                                  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  |
| Aa                                                   | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  |
| A                                                    | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  | 0.000%  |
| Baa                                                  | 0.000%  | 0.517%  | 1.087%  | 1.725%  | 2.444%  | 3.198%  | 3.198%  | 3.198%  | 3.198%  | 3.198%  |
| Ba                                                   | 0.892%  | 1.951%  | 3.700%  | 5.864%  | 8.134%  | 9.799%  | 12.014% | 14.494% | 16.490% | 18.420% |
| B                                                    | 2.801%  | 5.769%  | 6.900%  | 8.720%  | 10.514% | 12.681% | 14.496% | 16.072% | 18.079% | 20.832% |
| Caa-C                                                | 22.535% | 26.786% | 32.418% | 32.418% | 32.418% | 32.418% | 32.418% | 32.418% | 32.418% | 32.418% |
| Investment Grade                                     | 0.000%  | 0.106%  | 0.220%  | 0.344%  | 0.479%  | 0.616%  | 0.616%  | 0.616%  | 0.616%  | 0.616%  |
| Speculative Grade                                    | 2.650%  | 4.637%  | 6.363%  | 8.247%  | 10.231% | 12.005% | 13.989% | 16.055% | 17.965% | 20.051% |
| All Sovereign                                        | 0.775%  | 1.429%  | 2.006%  | 2.629%  | 3.279%  | 3.862%  | 4.390%  | 4.914%  | 5.368%  | 5.817%  |

In summary, all of the ratings agencies seem to have, on average, delivered the goods. Sovereign bonds with investment grade ratings have defaulted far less frequently than sovereign bonds with speculative ratings.

Notwithstanding this overall track record of success, ratings agencies have been criticized for failing investors on the following counts:

- 1. Ratings are upward biased: Ratings agencies have been accused of being far too optimistic in their assessments of both corporate and sovereign ratings. While the conflict of interest of having issuers pay for the rating is offered as the rationale for the upward bias in corporate ratings, that argument does not hold up when it comes to sovereign ratings, since the issuing government does not pay ratings agencies.
- 2. There is herd behavior: When one ratings agency lowers or raises a sovereign rating, other ratings agencies seem to follow suit. This herd behavior reduces the value of having three separate ratings agencies, since their assessments of sovereign risk are no longer independent.
- 3. Too little, too late: To price sovereign bonds (or set interest rates on sovereign loans), investors (banks) need assessments of default risk that are updated and timely. It has long been argued that ratings agencies take too long to change ratings, and that these changes happen too late to protect investors from a crisis.

- 4. Vicious Cycle: Once a market is in crisis, there is the perception that ratings agencies sometimes over react and lower ratings too much, thus creating a feedback effect that makes the crisis worse.
- 5. Ratings failures: At the other end of the spectrum, it can be argued that when a ratings agency changes the rating for a sovereign multiple times in a short time period, it is admitting to failure in its initial rating assessment. In a paper on the topic, Bhatia (2004) looks at sovereigns where S&P and Moody changed ratings multiple times during the course of a year between 1997 and 2002. His findings are reproduced in table 12:

*Table 12: Ratings Failures*

| Failure         | Failed rating<br>(& date) 2/ | Corrected rating<br>(& date) 2/ | Notches<br>adjusted 3/ | Key factor                |
|-----------------|------------------------------|---------------------------------|------------------------|---------------------------|
| <b>S&amp;P</b>  |                              |                                 |                        |                           |
| 1997: Thailand  | A (Sept. 3, 1997)            | BBB- (Jan. 8, 1998)             | ↓↓ (0.97)              | Evaporation of reserves   |
| 1997: Indonesia | BBB (Oct. 10, 1997)          | B- (Mar. 11, 1998)              | 7↓ (1.40)              | Collapse of asset quality |
| 1997: Korea     | AA- (Oct. 24, 1997)          | B+ (Dec. 22, 1997)              | 10↓ (5.26)             | Evaporation of reserves   |
| 1997: Malaysia  | A+ (Dec. 23, 1997)           | BBB- (Sept. 15, 1998)           | 5↓ (0.57)              | Collapse of asset quality |
| 1998: Korea     | B+ (Feb. 18, 1998)           | BBB- (Jan. 25, 1999)            | 4↑ (0.36)              | Reserves replenishment    |
| 1998: Romania   | BB- (May 20, 1998)           | B- (Oct. 19, 1998)              | 3↓ (0.61)              | Evaporation of reserves   |
| 1998: Russia    | BB- (June 9, 1998)           | B- (Aug. 13, 1998)              | 3↓ (1.43)              | Evaporation of reserves   |
| 2000: Argentina | BB (Nov. 14, 2000)           | B- (July 12, 2001)              | 4↓ (0.50)              | Fiscal slippage           |
| 2000: Uruguay   | BBB- (Feb. 14, 2002)         | B (July 26, 2002)               | 5↓ (0.94)              | Evaporation of reserves   |
| <b>Moody's</b>  |                              |                                 |                        |                           |
| 1997: Thailand  | A2 (Apr. 8, 1997)            | BaI (Dec. 21, 1997)             | 5↓ (0.68)              | Evaporation of reserves   |
| 1997: Korea     | A1 (Nov. 27, 1997)           | BaI (Dec. 21, 1997)             | 6↓ (7.83)              | Evaporation of reserves   |
| 1997: Indonesia | Baa3 (Dec. 21, 1997)         | B3 (Mar. 20, 1998)              | 6↓ (2.05)              | Collapse of asset quality |
| 1997: Malaysia  | A1 (Dec. 21, 1997)           | Baa2 (Sept. 14, 1998)           | 4↓ (0.46)              | Collapse of asset quality |
| 1998: Russia    | Ba2 (Mar. 11, 1998)          | B3 (Aug. 21, 1998)              | 4↓ (0.75)              | Evaporation of reserves   |
| 1998: Moldova   | Ba2 (July 14, 1998)          | B2 (July 14, 1998)              | 3↓ (90.00)             | Evaporation of reserves   |
| 1998: Romania   | Ba3 (Sept. 14, 1998)         | B3 (Nov. 6, 1998)               | 3↓ (1.76)              | Evaporation of reserves   |
| 2002: Uruguay   | Baa3 (May 3, 2002)           | B3 (July 31, 2002)              | 6↓ (2.07)              | Evaporation of reserves   |

Why do ratings agencies sometimes fail? Bhatia provides some possible answers:

- a. Information problems: The data that the agencies use to rate sovereigns generally come from the governments. Not only are there wide variations in the quantity and quality of information across governments, but there is also the potential for governments holding back bad news and revealing only good news. This, in turn, may explain the upward bias in sovereign ratings.
- b. Limited resources: To the extent that the sovereign rating business generates only limited revenues for the agencies and it is required to at least break even in terms of costs, the agencies cannot afford to hire too many analysts. These analysts are then spread thin globally, being asked to assess the ratings of dozens of lowprofile countries. In 2003, it was estimated that each analyst at the agencies was called up to rate between four and five sovereign governments. It has been argued by some that it is this overload that leads analysts to use common information (rather than do their own research) and to herd behavior.

- c. Revenue Bias: Since ratings agencies offer sovereign ratings gratis to most users, the revenues from ratings either have to come from the issuers or from other business that stems from the sovereign ratings business. When it comes from the issuing sovereigns or sub-sovereigns, it can be argued that agencies will hold back on assigning harsh ratings. In particular, ratings agencies generate significant revenues from rating sub-sovereign issuers. Thus, a sovereign ratings downgrade will be followed by a series of sub-sovereign ratings downgrades. Indirectly, therefore, these sub-sovereign entities will fight a sovereign downgrade, again explaining the upward bias in ratings.
- d. Other Incentive problems: While it is possible that some of the analysts who work for S&P and Moody's may seek work with the governments that they rate, it is uncommon and thus should not pose a problem with conflict of interest. However, the ratings agencies have created other businesses, including market indices, ratings evaluation services and risk management services, which may be lucrative enough to influence sovereign ratings.

## **Market Interest Rates**

The growth of the sovereign ratings business reflected the growth in sovereign bonds in the 1980s and 1990s. As more countries have shifted from bank loans to bonds, the market prices commanded by these bonds (and the resulting interest rates) have yielded an alternate measure of sovereign default risk, continuously updated in real time. In this section, we will examine the information in sovereign bond markets that can be used to estimate sovereign default risk.

# *The Sovereign Default Spread*

When a government issues bonds, denominated in a foreign currency, the interest rate on the bond can be compared to a rate on a riskless investment in that currency to get a market measure of the default spread for that country. To illustrate, the Brazilian government had a 10-year dollar denominated bond outstanding in June 2010, with a market interest rate of 5.55%. At the same time, the 10-year US treasury bond rate was 3.25%. If we assume that the US treasury is default free, the difference between the two rates can be attributed (2.30%) can be viewed as the market's assessment of the default spread for Brazil. Table 13 summarizes interest rates and default spreads for Latin American countries in June 2010, using dollar denominated bonds issued by these countries, as well as the sovereign foreign currency ratings (from Moody's) at the time.

*Table 13: Default Spreads on Dollar Denominated Bonds- Latin America*

| Country   | Moody’s Rating | Interest rate on \$ denominated bond (10 Year) | 10-year US Treasury Bond Rate | Default Spread |
|-----------|----------------|------------------------------------------------|-------------------------------|----------------|
| Mexico    | Baa1           | 4.60%                                          | 3.02%                         | 1.58%          |
| Brazil    | Baa3           | 4.64%                                          | 3.02%                         | 1.62%          |
| Colombia  | Ba1            | 5.26%                                          | 3.02%                         | 2.24%          |
| Peru      | Baa3           | 6.19%                                          | 3.02%                         | 3.17%          |
| Argentina | B3             | 8.92%                                          | 3.02%                         | 5.90%          |
| Venezuela | B2             | 14.24%                                         | 3.02%                         | 11.22%         |

While there is a strong correlation between sovereign ratings and market default spreads, there are advantages to using the default spreads. The first is that the market differentiation for risk is more granular than the ratings agencies; thus, Peru and Mexico have the same Moody's rating (Baa3) but the market sees more default risk in Peru. The second is that the market-based spreads are more dynamic than ratings, with changes occurring in real time. In figure 9, we graph the shifts in the default spreads for Brazil and Venezuela between 2006 and the end of 2009:

*Figure 9: Default Spreads for \$ Denominated Bonds: Brazil vs Venezuela*

![](_page_40_Figure_2.jpeg)

In December 2005, the default spreads for Brazil and Venezuela were similar; the Brazilian default spread was 3.18% and the Venezuelan default spread was 3.09%. Between 2006 and 2009, the spreads diverged, with Brazilian default spreads dropping to 1.32% by December 2009 and Venezuelan default spreads widening to 10.26%.

To use market-based default spreads as a measure of country default risk, there has to be a default free security in the currency in which the bonds are issued. Local currency bonds issued by governments cannot be compared to each other, since the differences in rates can be due to differences in expected inflation. Even with dollardenominated bonds, it is only the assumption that the US treasury bond rate is default free that allows us to back out default spreads from the interest rates.

# *The spread as a predictor of default*

Are market default spreads better predictors of default risk than ratings? One advantage that market spreads have over ratings is that they can adjust quickly to information. As a consequence, they provide earlier signals of imminent danger (and default) than ratings agencies do. However, market-based default measures carry their own costs. They tend to be far more volatile than ratings and can be affected by variables that have nothing to do with default. Liquidity and investor demand can sometimes cause shifts in spreads that have little or nothing to do with default risk.

Studies of the efficacy of default spreads as measures of country default risk reveal some consensus. First, default spreads are for the most part correlated with both sovereign ratings and ultimate default risk. In other words, sovereign bonds with low ratings tend trade at much higher interest rates and also are more likely to default. Second, the sovereign bond market leads ratings agencies, with default spreads usually climbing ahead of a rating downgrade and dropping before an upgrade. Third, notwithstanding the lead-lag relationship, a change in sovereign ratings is still an informational event that creates a price impact at the time that it occurs. In summary, it would be a mistake to conclude that sovereign ratings are useless, since sovereign bond markets seems to draw on ratings (and changes in these ratings) when pricing bonds.

## **Credit Default Swaps**

The last decade has seen the evolution of the Credit Default Swap (CDS) market, where investors try to put a price on the default risk in an entity and trade at that price. In conjunction with CDS contracts on companies, we have seen the development of a market for sovereign CDS contracts. The prices of these contracts represent market assessments of default risk in countries, updated constantly.

# *How does a CDS work?*

The CDS market allows investors to buy protection against default in a security. The buyer of a CDS on a specific bond makes payments of the "spread" each period to the seller of the CDS; the payment is specified as a percentage (spread) of the notional or face value of the bond being insured. In return, the seller agrees to make the buyer whole if the issuer of the bond (reference entity) fails to pay, restructures or goes bankrupt (credit event), by doing one of the following:

- a. Physical settlement: The buyer of the CDS can deliver the "defaulted" bond to the seller and get par value for the bond.

- b. Cash settlement: The seller of the CDS can pay the buyer the difference between par value of the defaulted bond and the market price, which will reflects the expected recovery from the issuer.

In effect, the buyer of the CDS is protected from losses arising from credit events over the life of the CDS.

Assume, for instance, that you own 5-year Colombian government bonds, with a par value of \$ 10 million, and that you are worried about default over the life of the bond. Assume also that the price of a 5-year CDS on the Colombian government is 250 basis points (2.5%). If you buy the CDS, you will be obligated to pay \$250,000 each year for the next 5 years and the seller of the CDS would receive this payment. If the Colombian government fails to fulfill its obligations on the bond or restructures the bond any time over the next 5 years, the seller of the CDS can fulfill his obligations by either buying the bonds from you for \$ 10 million or by paying you the difference between \$ 10 million and the market price of the bond after the credit event happens.

There are two points worth emphasizing about a CDS that may undercut the protection against default that it is designed to offer. The first is that the protection against failure is triggered by a credit event; if there is no credit event, and the market price of the bond collapses, you as the buyer will not be compensated. The second is that the guarantee is only as good as the credit standing of the seller of the CDS. If the seller defaults, the insurance guarantee will fail. On the other side of the transaction, the buyer may default on the spread payments that he has contractually agreed to make.

# *Market Background*

J.P. Morgan is credited with creating the first CDS, when it extended a \$4.8 billon credit line to Exxon and then sold the credit risk in the transaction to investors. Over the last decade and a half, the CDS market has surged in size. By the end of 2007, the notional value of the securities on which CDS had been sold amounted to more than \$ 60 trillion, though the market crisis caused a pullback to about \$39 trillion by December 2008.

You can categorize the CDS market based upon the reference entity, i.e., the issuer of the bond underlying the CDS. While our focus is on sovereign CDS, they represent a small proportion of the overall market. Corporate CDS represent the bulk of the market, followed by bank CDS and then sovereign CDS. Figure 10 provides a breakdown of the CDS market in 2008, categorized by reference entity.

*Figure 10: CDS Market broken down by Issuer - 2008*

![](_page_43_Figure_3.jpeg)

While the notional value of the securities underlying the CDS market is huge, the market itself is a fair narrow one, insofar that a few investors account for the bulk of the trading in the market. While the market was initially dominated by banks buying protection against default risk, the market has attracted investors, portfolio managers and speculators, but the number of players in the market remains small, especially given the size of the market. The narrowness of the market does make it vulnerable, since the failure of one or more of the big players can throw the market into tumult and cause spreads to shift dramatically. The failure of Lehman Brothers in 2008, during the banking crisis, threw the CDS market into turmoil for several weeks.

# *CDS and default risk*

If we assume away counter party risk and liquidity, the prices that investors set for credit default swaps should provide us with updated measures of default risk in the reference entity. In contrast to ratings, that get updated infrequently, CDS prices should reflect adjust to reflect current information on default risk.

To illustrate this point, let us consider the evolution of sovereign risk in Greece during 2009 and 2010. In figure 11, we graph out the CDS spreads for Greece on a month-by-month basis from 2006 to 2010 and ratings actions taken by one agency (Fitch) during that period:

*Figure 11: Greece CDS Prices and Ratings*

![](_page_44_Figure_3.jpeg)

While ratings stayed stagnant for the bulk of the period, before moving late in 2009 and 2010, when Greece was downgraded, the CDS spread and default spreads for Greece changed each month. The changes in both market-based measures reflect market reassessments of default risk in Greece, using updated information.

While it is easy to show that CDS spreads are more timely and dynamic than sovereign ratings and that they reflect fundamental changes in the issuing entities, the fundamental question remains: Are changes in CDS spreads better predictors of future default risk than sovereign ratings or default spreads? The findings are significant. First, changes in CDS spreads lead changes in the sovereign bond yields and in sovereign ratings. 11 Second, it is not clear that the CDS market is quicker or better at assessing

<sup>11</sup> Ismailescu, I., 2007, The Reaction of Emerging Markets Credit Default Swap Spreads to Sovereign Credit Rating Changes and Country Fundamentals, Working Paper, Pace University. This study finds that

default risks than the government bond market, from which we can extract default spreads. Third, there seems to be clustering in the CDS market, where CDS prices across groups of companies move together in the same direction. A study suggests six clusters of emerging market countries, captured in table 14:

*Table 14: Clusters of Emerging Markets: CDS Market*

|                      | Cluster 1 | Cluster 2 | Cluster 3 | Cluster 4 | Cluster 5   | Cluster 6 |
|----------------------|-----------|-----------|-----------|-----------|-------------|-----------|
| Countries in Cluster | Brazil    | Chile     | Croatia   | Colombia  | Pakistan    | Israel    |
|                      | Bulgaria  | China     | Hungary   | Panama    | Philippines | Qatar     |
|                      | Mexico    | Japan     | Malaysia  | Peru      | Ukraine     |           |
|                      | Poland    | Korea     | Romania   |           |             |           |
|                      | Russia    | Thailand  | S. Africa |           |             |           |
|                      | Slovak    | Venezuela |           |           |             |           |
|                      | Turkey    |           |           |           |             |           |
|                      |           |           |           |           |             |           |
| Ave. Corr. Internal  | 0.516     | 0.596     | 0.402     | 0.588     | 0.517       | 0.466     |
| Ave. Corr. External  | 0.210     | 0.220     | 0.278     | 0.245     | 0.218       | 0.102     |
| Ave. CDS Spread      | 287.30    | 114.83    | 96.10     | 243.63    | 262.37      | 30.12     |

The correlation within the cluster, and without, are provided towards the bottom. Thus, the correlation between countries in cluster 1 is 0.516, whereas the correlation between countries in cluster 1 and the rest of the market is only 0.210.

There are inherent limitations with using CDS prices as predictors of country default risk. The first is that the exposure to counterparty and liquidity risk, endemic to the CDS market, can cause changes in CDS prices that have little to do with default risk. Thus, a significant portion of the surge in CDS prices in the last quarter of 2008 can be traced to the failure of Lehman and the subsequent surge in concerns about counterparty risk. The second and related problem is that the narrowness of the CDS market can make individual CDS susceptible to illiquidity problems, with a concurrent effect on prices. Notwithstanding these limitations, it is undeniable that changes in CDS prices supply important information about shifts in default risk in entities. In summary, the evidence, at least as of now, is that changes in CDS prices provide information, albeit noisy, of changes in default risk. However, there is little to indicate that it is superior to market default spreads (obtained from government bonds) in assessing this risk.

CDS prices provide more advance warning of ratings downgrades.

#### **Fundamental Analysis**

Sovereign ratings, market default spreads and CDS prices all provide useful information about default risk, but they also have limitations. When they fail badly in a specific country, as they inevitably will, investors are spurred to develop their own measures of default risk, based upon intrinsic or fundamental data that is available about countries. In this section, we will examine whether we can develop measures from sovereign default risk from macro economic and financial fundamentals, and whether these measures can add value to the process of estimating default risk.

## **Variations**

Fundamental analyses can range from statistical models that yield default risk scores to country risk scores that incorporate richer information about sovereign risk to synthetic ratings models, where analysts use either raw data to come up with "better" sovereign ratings or modify existing ratings.

- a. Statistical Models: The statistical models for default risk take two forms. In the first, called logit or probit models, researchers begin with a sample of countries that have defaulted over time versus those that have not and try to find variables from prior periods that could have predicted the defaults. In the second, the objective becomes explaining differences in market default spreads (rather than actual default) using data available to investors at the time.
- b. Country risk scores: One of the limitations of ratings is that they are so closely focused on default risk in government bonds that they miss other risks that investors may be exposed to in a country.
- c. Synthetic ratings models: In this approach, we stay within the comfortable confines of sovereign ratings, with improvements made to the actual ratings to reflect some the weaknesses that we mentioned earlier – the lag in ratings changes, the regional biases and the ratings bubbles that sometimes come from weighing recent history too much.

In general, fundamental approaches to assessing sovereign risk are more time and resource intensive than the first three approaches. The investment may be well worth making for investors who want to take advantage of systematic market mistakes in assessing sovereign risk.

# **Dealing with Sovereign Default Risk**

So, what if there is sovereign default risk? From a measurement standpoint, it does complicate financial analysis, since we cannot use government bond rates as risk free rates, and in the first part of this section, we will consider alternative solutions. The more significant effect of potential sovereign default is that it may change the way investors and managers think about and react to risk, altering risk premiums for all assets and altering the investment, financing and dividend policies of companies. We will consider these changes in the second part of the section.

## **The Measurement Problem**

When there is no default free entity, the measurement question that every analyst confronts is estimating a riskfree rate for both corporate financial analysis and valuation. There are several approaches that can be used to get around this problem, though none is perfect and some require that riskfree rate be available in another currency.

## *a. Pricing of derivatives*

Assume you are working in a currency, where there is no default free entity (or riskfree rate) but that there are other currencies where a riskfree rate is available. If you have forward or futures contracts on currencies, you can back out a riskfree rate in one currency, if you know the riskfree rate in the other. For instance, let us take the case of Colombian Peso, a currency in which you cannot find a default free entity or riskfree rate and assume that you can obtain a riskfree rate in US dollars. The forward rate between the Colombian peso and the US dollar can be written as follows;

$$\text{Forward Rate}^t_{\text{Peso}, $} = \text{Spot Rate}_{\text{Peso}, $} \frac{(1 + \text{Riskfree Rate}_{\text{Peso}})}{(1 + \text{Riskfree Rate}_{\text{US}})^t}$$

For example, if the current spot rate is 2000 pesos per US dollar, the ten-year forward rate is 2400 Pesos per dollar, and the current ten-year US treasury bond rate is 3%, the ten-year Colombian Peso risk free rate can be estimated as follows:

$$2400 = 2000 \frac{(1 + \text{Riskfree Rate}_{\text{Pesos}})^{10}}{(1.03)^{10}}$$

Solving for the Peso rate yields a ten-year risk free rate of 4.90%. The biggest limitation of this approach, however, is that forward rates are difficult to come by for periods beyond a year<sup>12</sup> for many of the emerging markets, where we would be most interested in using them and there has to be at least one sovereign that is viewed as not having default risk, with futures and forward contracts against other currencies.

### *b. Adjusted Government Bond Rates*

As we noted in earlier sections, governments can default on local currency debt just as they can on foreign currency debt. When a government has local currency bonds outstanding, but the government is not considered default free, the interest rate on these bonds includes a default spread. There is a simple way to get to a riskfree rate. If we can estimate how much of the current market interest rate on the bond can be attributed to default risk, we can strip this default spread from the rate to arrive at an estimate of the riskfree rate in that currency. Using the Indian rupee bond as the illustration, we used the ten-year government bond rate in June 2010 of 8% and the local currency rating for India of Baa2 the measure of default risk to arrive at a default spread of 3%. Subtracting this from the market interest rate yields a riskfree rupee rate of 5%.

Riskfree rate in Indian rupees = Market interest rate on rupee bond – Default Spread<sub>India</sub>  

$$= 8\% - 3\% = 8.10\%$$

How did we go from a rating to a default spread? Earlier in this paper, we introduced two measures – a default spread estimated from dollar-denominated or Euro-denominated bonds and the CDS spread. The former implicitly assumes that there is a riskfree rate available in US dollars or Euros, whereas the latter does not. But what about countries that have only local currency bonds (where there is no default free rate) outstanding and no CDS market? In table 15, we have estimated the typical default spreads for bonds in

<sup>12</sup> In cases where only a one-year forward rate exists, an approximation for the long term rate can be obtained by first backing out the one-year local currency borrowing rate, taking the spread over the oneyear treasury bill rate, and then adding this spread on to the long term treasury bond rate. For instance, with a one-year forward rate of 39.95 on the Thai bond, we obtain a one-year Thai baht riskless rate of 9.04% (given a one-year T.Bill rate of 4%). Adding the spread of 5.04% to the ten-year treasury bond rate of 5% provides a ten-year Thai Baht rate of 10.04%.

different sovereign ratings classes, using market-traded bonds issued in dollars or Euros by governments and CDS spreads within each ratings class.. We were able to get default spreads for almost 50 countries, categorized by rating class, and we averaged the spreads across multiple countries in the same ratings class. 13 An alternative approach to estimating default spread is to assume that sovereign ratings are comparable to corporate ratings, i.e., a Ba1 rated country bond and a Ba1 rated corporate bond have equal default risk. In this case, we can use the default spreads on corporate bonds for different ratings classes. Table 2.15 also summarizes the typical default spreads for corporate bonds in different ratings classes in January 2010.

*Table 15: Default Spreads by Sovereign Ratings Class – January 2010*

| Moody’s Rating | Sovereign Bonds/ CDS | Corporate Bonds |
|----------------|----------------------|-----------------|
| Aaa            | 0.25%                | 0.50%           |
| Aa1            | 0.35%                | 0.55%           |
| Aa2            | 0.60%                | 0.65%           |
| Aa3            | 0.70%                | 0.70%           |
| A1             | 0.80%                | 0.85%           |
| A2             | 0.90%                | 0.90%           |
| A3             | 1.00%                | 1.05%           |
| Baa1           | 1.50%                | 1.65%           |
| Baa2           | 1.75%                | 1.80%           |
| Baa3           | 2.00%                | 2.25%           |
| Ba1            | 3.00%                | 3.50%           |
| Ba2            | 3.55%                | 3.85%           |
| Ba3            | 3.75%                | 4.00%           |
| B1             | 4.00%                | 4.25%           |
| B2             | 5.00%                | 5.25%           |
| B3             | 5.25%                | 5.50%           |
| Caa1           | 7.00%                | 7.25%           |
| Caa2           | 8.00%                | 8.50%           |
| Caa3           | 10.00%               | 10.50%          |

<sup>13</sup> For instance, Turkey, Indonesia and Vietnam all share a Ba3 rating, and the CDS spreads as of September 2008 were 2.95%, 3.15% and 3.65% respectively. The average spread across the three countries is 3.25%.

Note that the corporate bond spreads, at least in January 2010, were very similar to the sovereign spreads.

If, in fact, we reach the point where no entity is default free, we may have to make this adjustment not only for emerging market currencies, but also for developed market currencies. Getting a risk free US dollar rate may then require subtracting out the default spread for whatever rating the United States may have from the treasury bond rate.

#### *c. Build up Approach*

Since the risk free rate in any currency can be written as the sum of expected inflation in that currency and the expected real rate, we can try to estimate the two components separately. To estimate expected inflation, we can start with the current inflation rate and extrapolate from that to expected inflation in the future. For the real rate, we can use the expected real growth rate in the economy in the long term. Thus, if expected inflation in a currency is 6% and the real rate is 2%, the risk free rate in that currency is 8%. Needless to say, both expected inflation and real rates will be difficult to estimate, and this approach should be reserved for the most dire circumstances, where there is no local currency government bond and no futures or forward contracts in that currency.

## **Changes in investment/ corporate financial behavior**

If the only problem with not having a default free entity is that risk free rates become more difficult to estimate, we should consider ourselves lucky, since there are solutions to that problem. The bigger concern is that the loss of a safe haven will have real and potentially damaging effects on both investor behavior and on decision making at firms.

## **Investor Behavior**

In an earlier section, we noted how much of portfolio theory and management is built on the premise that a risk free investment exists. Put another way, not having this investment is more than just a measurement problem and can change the way investors construct portfolios and price risk. Here are some of the potential consequences:

- a. Less diversified portfolios, tailored to investor risk aversion: While there are several assumptions in the capital asset pricing model that can be critiqued, the

key conclusion remains viable. If investors can lend and borrow at the risk free rate, they will be better off holding the most diversified portfolio of risky assets that they can get and use the proportion invested in the riskless asset as the risk tuning device. Investors who want to bear less risk will invest more in the riskless asset and investors who want to bear a great deal of risk will borrow at the riskless rate; both groups will invest in the same diversified portfolio. If there is no riskless asset, this conclusion breaks down. Without a riskless asset available for adjusting risk, investors have to tailor portfolios to their specific risk needs. In practical terms, this would require investors who want to bear more (less) risk holding stocks in the riskiest (safest) sectors and avoiding safe (risky) companies. So what? Both groups will give up some diversification when they do so, resulting in less efficient risk bearing overall. While direct evidence for this proposition is difficult to come by, there is evidence that investors in emerging markets, where governments have historically been exposed to more default risk, are less likely to invest in mutual funds with diversified portfolios and more likely to hold idiosyncratic portfolios.

- b. Higher risk premiums: Building on the theme of less efficient risk bearing, the absence of a riskless investment will make risky investments seem even riskier to all investors. Investors may not consciously think about the riskless asset but having one provides psychological solace that in times of crisis, they will have a safe haven for their savings. Not having a riskless investment can therefore be unsettling for investors and can have significant consequences for the pricing of all risky assets. Investors may invest less in risky assets, demand higher risk premiums (and pay lower prices) and be quicker to flee these assets in the face of danger. Put another way, not having a safe haven that they can return to will make investors less willing to take risk. As a consequence, we can expect to see lower prices for all risky assets, higher volatility in prices in these markets and abrupt, painful market corrections. In emerging markets, where the absence of a riskless asset is a very real phenomenon, we have witnessed all of these phenomena play out.

- c. Search for a constant can lead to strange consequences: Even in the absence of default free entities, investors will continue to look for safety. Not only will this open the door for investment scams that claim to be risk free, when they are not, but also open the door to the irrational pricing of anything perceived as close to risk free.

#### **Corporate Finance**

A great deal of corporate financial theory is also built around the assumption that firms can invest excess cash in a riskless investment and that cash is therefore a neutral asset. We would hypothesize that in the absence of a risk free asset, we can see the following:

- a. Cash as a "value added" investment: In most developed markets with a riskfree asset, cash is viewed as a neutral asset. In most US companies, for instance, cash is invested in treasury bills or money market funds, earning what is perceived to be a fair, riskless rate of return and there is little or no differentiation across companies. When there is no riskfree asset, any cash held by the company has to be invested in "risky" assets and the quality of the investment will be judged by the returns earned, relative to the required return (given the risk). Companies that find better cash investments will therefore be viewed as more valuable than companies that do not. Following up on this proposition, it is also possible that some companies may generate more excess returns on their cash investments than on their operating investments. As a result, managers will spend more of their time and resources researching cash investments and less on their operating investments.
- b. Decreased debt capacity: As we noted earlier in this paper, lenders often are more comfortable lending to firms with substantial cash balances that are invested in liquid, riskfree assets. When there are no riskfree assets, lenders will be less inclined to lend to companies with large cash balances, since they have no way of knowing whether these investments are good and/or liquid.
- c. Greater pressure to return cash to stockhoders: When there is a riskfree investment, companies are less likely to be penalized when they hold back from

paying dividends and invest in the riskfree investment instead. Investors will receive less in dividends but they will get an equivalent capital gain. When nothing is riskfree, this trust breaks down and we should expect to see stockholders, at least in poorly managed companies, demand their cash back. If companies refuse, and stockholders do not have much power to force the issue, they will fall back on the only remaining mechanism under their control and discount the market values of companies that hold on to cash.

## **Conclusion**

Having an investment that is risk free is critical not only for financial modeling but also for investor behavior and corporate financial analysis. From a measurement standpoint the return on the investment (the risk free rate) provides the basis for computing expected returns on risky assets and the presence of a riskless asset also changes investment, financing and dividend policy at firms.

In this paper, we begin by establishing the centrality of the riskfree rate to portfolio theory and corporate finance and argue that the only entity that is capable of issuing riskfree investments is the government. We then explore what happens when governments default, by first noting the history of such defaults and why they occur. Accepting the proposition that governments sometimes default, we then examine different measures of sovereign or government default risk, ranging from sovereign ratings to credit default swaps to fundamental analysis, with the intent of isolating the best predictor of future default risk.

In the last section, we consider the consequences of assuming not only that some sovereigns have default risk, but that all of them do. In other words, how would corporate finance and portfolio theory change if nothing was riskfree? We present ways of estimating the risk free rate when confronted with market rates that have default risk embedded in them. We also argue that investors will become more risk averse in the absence of a riskfree rate and charge higher risk premiums for risky assets and that there will be significant shifts in investment policy (towards financial from real investments), financing policy (towards equity from debt) and dividend policy (towards less dividends) as a consequence.