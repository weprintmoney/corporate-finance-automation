---
title: "Valsession21B"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valfall16/valsession21B.pdf
---

### VALUATION: PACKET 3 REAL OPTIONS, ACQUISITION VALUATION AND VALUE ENHANCEMENT

Aswath Damodaran

Updated: September 2016

# REAL OPTIONS: FACT AND FANTASY

Aswath Damodaran

### Underlying Theme: Searching for an Elusive Premium

**3**

¨ Traditional discounted cashflow models under estimate the value of investments, where there are options embedded in the investments to ¤ Delay or defer making the investment (delay) ¤ Adjust or alter production schedules as price changes (flexibility) ¤ Expand into new markets or products at later stages in the process, based upon observing favorable outcomes at the early stages (expansion) ¤ Stop production or abandon investments if the outcomes are unfavorable at early stages (abandonment) ¨ Put another way, real option advocates believe that you should be paying a premium on discounted cashflow value estimates.

# A bad investment…

![](_page_3_Diagram_2.jpeg)

# Becomes a good one…

![](_page_4_Diagram_2.jpeg)

# Three Basic Questions

**6**

¨ When is there a real option embedded in a decision or an asset? ¨ When does that real option have significant economic value? ¨ Can that value be estimated using an option pricing model?

### When is there an option embedded in an action?

**7**

¨ An option provides the holder with the right to buy or sell a specified quantity of an underlying asset at a fixed price (called a strike price or an exercise price) at or before the expiration date of the option. ¨ There has to be a clearly defined underlying asset whose value changes over time in unpredictable ways. ¨ The payoffs on this asset (real option) have to be contingent on an specified event occurring within a finite period.

# Payoff Diagram on a Call

![](_page_7_Diagram_2.jpeg)

# Payoff Diagram on Put Option

![](_page_8_Diagram_2.jpeg)

### When does the option have significant economic value?

**10**

¨ For an option to have significant economic value, there has to be a restriction on competition in the event of the contingency. In a perfectly competitive product market, no contingency, no matter how positive, will generate positive net present value. ¨ At the limit, real options are most valuable when you have exclusivity - you and only you can take advantage of the contingency. They become less valuable as the barriers to competition become less steep.

# Determinants of option value

**11**

### ¨ Variables Relating to Underlying Asset

¤ Value of Underlying Asset; as this value increases, the right to buy at a fixed price (calls) will become more valuable and the right to sell at a fixed price (puts) will become less valuable. ¤ Variance in that value; as the variance increases, both calls and puts will become more valuable because all options have limited downside and depend upon price volatility for upside. ¤ Expected dividends on the asset, which are likely to reduce the price appreciation component of the asset, reducing the value of calls and increasing the value of puts.

### ¨ Variables Relating to Option

¤ Strike Price of Options; the right to buy (sell) at a fixed price becomes more (less) valuable at a lower price. ¤ Life of the Option; both calls and puts benefit from a longer life.

#### ¨ Level of Interest Rates; as rates increase, the right to buy (sell) at a fixed price in the future becomes more (less) valuable.

### When can you use option pricing models to value real options?

**12**

¨ The notion of a replicating portfolio that drives option pricing models makes them most suited for valuing real options where ¤ The underlying asset is traded - this yield not only observable prices and volatility as inputs to option pricing models but allows for the possibility of creating replicating portfolios ¤ An active marketplace exists for the option itself. ¤ The cost of exercising the option is known with some degree of certainty. ¨ When option pricing models are used to value real assets, we have to accept the fact that ¤ The value estimates that emerge will be far more imprecise. ¤ The value can deviate much more dramatically from market price because of the difficulty of arbitrage.

# Creating a replicating portfolio

**13**

¨ The objective in creating a replicating portfolio is to use a combination of riskfree borrowing/lending and the underlying asset to create the same cashflows as the option being valued. ¤ Call = Borrowing + Buying D of the Underlying Stock ¤ Put = Selling Short D on Underlying Asset + Lending ¤ The number of shares bought or sold is called the option delta. ¨ The principles of arbitrage then apply, and the value of the option has to be equal to the value of the replicating portfolio. 

# The Binomial Option Pricing Model

![](_page_13_Diagram_2.jpeg)

# The Limiting Distributions….

**15**

¨ As the time interval is shortened, the limiting distribution, as t -> 0, can take one of two forms. ¤ If as t -> 0, price changes become smaller, the limiting distribution is the normal distribution and the price process is a continuous one. ¤ If as t->0, price changes remain large, the limiting distribution is the poisson distribution, i.e., a distribution that allows for price jumps. ¨ The Black-Scholes model applies when the limiting distribution is the normal distribution , and explicitly assumes that the price process is continuous and that there are no jumps in asset prices. 

# Black and Scholes…

**16**

¨ The version of the model presented by Black and Scholes was designed to value European options, which were dividend-protected. ¨ The value of a call option in the Black-Scholes model can be written as a function of the following variables: ¤ S = Current value of the underlying asset ¤ K = Strike price of the option ¤ t = Life to expiration of the option ¤ r = Riskless interest rate corresponding to the life of the option ¤ s<sup>2</sup> = Variance in the ln(value) of the underlying asset

# The Black Scholes Model

**17**

Value of call = S N (d1) - K e-rtN(d2)

where

d2 = d1 - s √t

¨ The replicating portfolio is embedded in the Black-Scholes model. To replicate this call, you would need to ¤ Buy N(d1) shares of stock; N(d1) is called the option delta ¤ Borrow K e-rtN(d2) 

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r + \frac{\sigma^2}{2})t}{\sigma \sqrt{t}}$$

# The Normal Distribution

| d     | N(d)   | d     | N(d)   | d    | N(d)   |
|-------|--------|-------|--------|------|--------|
| -3.00 | 0.0013 | -1.00 | 0.1587 | 1.05 | 0.8531 |
| -2.95 | 0.0016 | -0.95 | 0.1711 | 1.10 | 0.8643 |
| -2.90 | 0.0019 | -0.90 | 0.1841 | 1.15 | 0.8749 |
| -2.85 | 0.0022 | -0.85 | 0.1977 | 1.20 | 0.8849 |
| -2.80 | 0.0026 | -0.80 | 0.2119 | 1.25 | 0.8944 |
| -2.75 | 0.0030 | -0.75 | 0.2266 | 1.30 | 0.9032 |
| -2.70 | 0.0035 | -0.70 | 0.2420 | 1.35 | 0.9115 |
| -2.65 | 0.0040 | -0.65 | 0.2578 | 1.40 | 0.9192 |
| -2.60 | 0.0047 | -0.60 | 0.2743 | 1.45 | 0.9265 |
| -2.55 | 0.0054 | -0.55 | 0.2912 | 1.50 | 0.9332 |
| -2.50 | 0.0062 | -0.50 | 0.3085 | 1.55 | 0.9394 |
| -2.45 | 0.0071 | -0.45 | 0.3264 | 1.60 | 0.9452 |
| -2.40 | 0.0082 | -0.40 | 0.3446 | 1.65 | 0.9505 |
| -2.35 | 0.0094 | -0.35 | 0.3632 | 1.70 | 0.9554 |
| -2.30 | 0.0107 | -0.30 | 0.3821 | 1.75 | 0.9599 |
| -2.25 | 0.0122 | -0.25 | 0.4013 | 1.80 | 0.9641 |
| -2.20 | 0.0139 | -0.20 | 0.4207 | 1.85 | 0.9678 |
| -2.15 | 0.0158 | -0.15 | 0.4404 | 1.90 | 0.9713 |
| -2.10 | 0.0179 | -0.10 | 0.4602 | 1.95 | 0.9744 |
| -2.05 | 0.0202 | -0.05 | 0.4801 | 2.00 | 0.9772 |
| -2.00 | 0.0228 | 0.00  | 0.5000 | 2.05 | 0.9798 |
| -1.95 | 0.0256 | 0.05  | 0.5199 | 2.10 | 0.9821 |
| -1.90 | 0.0287 | 0.10  | 0.5398 | 2.15 | 0.9842 |
| -1.85 | 0.0322 | 0.15  | 0.5596 | 2.20 | 0.9861 |
| -1.80 | 0.0359 | 0.20  | 0.5793 | 2.25 | 0.9878 |
| -1.75 | 0.0401 | 0.25  | 0.5987 | 2.30 | 0.9893 |
| -1.70 | 0.0446 | 0.30  | 0.6179 | 2.35 | 0.9906 |
| -1.65 | 0.0495 | 0.35  | 0.6368 | 2.40 | 0.9918 |
| -1.60 | 0.0548 | 0.40  | 0.6554 | 2.45 | 0.9929 |
| -1.55 | 0.0606 | 0.45  | 0.6736 | 2.50 | 0.9938 |
| -1.50 | 0.0668 | 0.50  | 0.6915 | 2.55 | 0.9946 |
| -1.45 | 0.0735 | 0.55  | 0.7088 | 2.60 | 0.9953 |
| -1.40 | 0.0808 | 0.60  | 0.7257 | 2.65 | 0.9960 |
| -1.35 | 0.0885 | 0.65  | 0.7422 | 2.70 | 0.9965 |
| -1.30 | 0.0968 | 0.70  | 0.7580 | 2.75 | 0.9970 |
| -1.25 | 0.1056 | 0.75  | 0.7734 | 2.80 | 0.9974 |
| -1.20 | 0.1151 | 0.80  | 0.7881 | 2.85 | 0.9978 |
| -1.15 | 0.1251 | 0.85  | 0.8023 | 2.90 | 0.9981 |
| -1.10 | 0.1357 | 0.90  | 0.8159 | 2.95 | 0.9984 |
| -1.05 | 0.1469 | 0.95  | 0.8289 | 3.00 | 0.9987 |
| -1.00 | 0.1587 | 1.00  | 0.8413 |      |        |

![](_page_17_Figure_2.jpeg)

# Adjusting for Dividends

**19**

¨ If the dividend yield (y = dividends/ Current value of the asset) of the underlying asset is expected to remain unchanged during the life of the option, the Black-Scholes model can be modified to take dividends into account. ¨ C = S e-yt N(d1) - K e-rtN(d2)

where,

d2 = d1 - s √t

¨ The value of a put can also be derived: ¨ P = K e-rt (1-N(d2)) - S e-yt (1-N(d1))

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r - y + \frac{\sigma^2}{2}) t}{\sigma \sqrt{t}}$$

# Choice of Option Pricing Models

**20**

¨ Most practitioners who use option pricing models to value real options argue for the binomial model over the Black-Scholes and justify this choice by noting that ¤ Early exercise is the rule rather than the exception with real options ¤ Underlying asset values are generally discontinous. ¨ If you can develop a binomial tree with outcomes at each node, it looks a great deal like a decision tree from capital budgeting. The question then becomes when and why the two approaches yield different estimates of value.

# The Decision Tree Alternative

**21**

¨ Traditional decision tree analysis tends to use ¤ One cost of capital to discount cashflows in each branch to the present ¤ Probabilities to compute an expected value ¤ These values will generally be different from option pricing model values ¨ If you modified decision tree analysis to ¤ Use different discount rates at each node to reflect where you are in the decision tree (This is the Copeland solution) (or) ¤ Use the riskfree rate to discount cashflows in each branch, estimate the probabilities to estimate an expected value and adjust the expected value for the market risk in the investment ¨ Decision Trees could yield the same values as option pricing models