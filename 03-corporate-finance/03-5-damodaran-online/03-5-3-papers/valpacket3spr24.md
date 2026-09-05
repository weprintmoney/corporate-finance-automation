---
title: "Valpacket3Spr24"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket3spr24.pdf
---

### VALUATION: PACKET 3 REAL OPTIONS, ACQUISITION VALUATION AND VALUE ENHANCEMENT

Aswath Damodaran Updated: January 2024

### REAL OPTIONS: FACT AND FANTASY

Aswath Damodaran

### Underlying Theme: Searching for an Elusive Premium

**3**

¨ Traditional discounted cashflow models underestimate the value of investments, where there are options embedded in the investments to ¤ Delay or defer making the investment (delay) ¤ Adjust or alter production schedules as price changes (flexibility) ¤ Expand into new markets or products at later stages in the process, based upon observing favorable outcomes at the early stages (expansion) ¤ Stop production or abandon investments if the outcomes are unfavorable at early stages (abandonment) ¨ Put another way, real option advocates believe that you should be paying a premium on discounted cashflow value estimates.

# A bad investment…

![](_page_3_Diagram_2.jpeg)

# Becomes a good one…

![](_page_4_Diagram_2.jpeg)

# Three Basic Questions

- 1. When is there a real option embedded in a decision or an asset?
- 2. When does that real option have significant economic value?
- 3. Can that value be estimated using an option pricing model?

### When is there an option embedded in an action?

**7**

¨ An option provides the holder with the *right* to buy or sell a specified quantity of an underlying asset at a *fixed price* (called a strike price or an exercise price) at or before the expiration date of the option. ¨ There has to be a *clearly defined underlying asset*  whose value changes over time in unpredictable ways. ¨ The payoffs on this asset (real option) have to be *contingent on a specified event* occurring within a finite period.

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

### ¨ Level of Interest Rates; as rates increase, the right to buy (sell) at a fixed price in the future becomes more (less) valuable.

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

¨ The version of the model presented by Black and Scholes was designed to value European options, which were dividend-protected. ¨ The value of a call option in the Black-Scholes model can be written as a function of the following variables: ¤ S = Current value of the underlying asset ¤ K = Strike price of the option ¤ t = Life to expiration of the option ¤ r = Riskless interest rate corresponding to the life of the option ¤ <sup>2</sup> = Variance in the ln(value) of the underlying asset

# The Black Scholes Model

**17**

Value of call = S N (d1) - K e-rtN(d2)

where

d2 = d1 - √t

¨ The replicating portfolio is embedded in the Black-Scholes model. To replicate this call, you would need to ¤ Buy N(d1) shares of stock; N(d1) is called the option delta ¤ Borrow K e-rtN(d2)

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r + \frac{\sigma^2}{2}) t}{\sigma \sqrt{t}}$$

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

¨ If the dividend yield (y = dividends/ Current value of the asset) of the underlying asset is expected to remain unchanged during the life of the option, the Black-Scholes model can be modified to take dividends into account.

□ 
$$C = S e^{-yt} N(d1) - K e^{-rt} N(d2)$$

where,

d2 = d1 - √t

¨ The value of a put can also be derived: ¨ P = K e-rt (1-N(d2)) - S e-yt (1-N(d1))

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r - y + \frac{\sigma^2}{2}) t}{\sigma \sqrt{t}}$$

# Dividend Yield = Cost of Delay

¨ Options have time premiums, and when they are traded, you very seldom get early exercise, with one exception being calls before big ex-dividend dates. The trade off that drives early exercise is: ¤ Loss of the time premium of the option from exercising early (against) ¤ Dividends you will receive, if you exercise early ¤ If the dividend exceeds the time premium, you will see early exercise. ¨ Put differently, the dividends foregone become the cost of delaying exercise and leaving the option live. ¨ Thus, having a cost of delay in an option will require that you use an dividend-adjusted version of the option pricing model.

# Choice of Option Pricing Models

**21**

¨ Most practitioners who use option pricing models to value real options argue for the binomial model over the Black-Scholes and justify this choice by noting that ¤ Early exercise is the rule rather than the exception with real options ¤ Underlying asset values are generally discontinous. ¨ If you can develop a binomial tree with outcomes at each node, it looks a great deal like a decision tree from capital budgeting. The question then becomes when and why the two approaches yield different estimates of value.

# The Decision Tree Alternative

**22**

¨ Traditional decision tree analysis tends to use ¤ One cost of capital to discount cashflows in each branch to the present ¤ Probabilities to compute an expected value ¤ These values will generally be different from option pricing model values ¨ If you modified decision tree analysis to ¤ Use different discount rates at each node to reflect where you are in the decision tree (This is the Copeland solution) (or) ¤ Use the riskfree rate to discount cashflows in each branch, estimate the probabilities to estimate an expected value and adjust the expected value for the market risk in the investment ¨ Decision Trees could yield the same values as option pricing models

### A decision tree valuation of a pharmaceutical company with one drug in the FDA pipeline…

![](_page_22_Diagram_2.jpeg)

# Key Tests for Real Options

**24**

¨ Is there an option embedded in this asset/ decision? ¤ Can you identify the underlying asset? ¤ Can you specify the contingency under which you will get payoff? ¨ Is there exclusivity? ¤ If yes, there is option value. ¤ If no, there is none. ¤ If in between, you have to scale value. ¨ Can you use an option pricing model to value the real option? ¤ Is the underlying asset traded? ¤ Can the option be bought and sold? ¤ Is the cost of exercising the option known and clear?

### I. Options in Projects/Investments/Acquisitions

**25**

¨ One of the limitations of traditional investment analysis is that it is static and does not do a good job of capturing the options embedded in investment. ¤ The first of these options is the option to delay taking a investment, when a firm has exclusive rights to it, until a later date. ¤ The second of these options is taking one investment may allow us to take advantage of other opportunities (investments) in the future ¤ The last option that is embedded in projects is the option to abandon a investment, if the cash flows do not measure up. ¨ These options all add value to projects and may make a "bad" investment (from traditional analysis) into a good one.

# A. The Option to Delay

**26**

¨ When a firm has exclusive rights to a project or product for a specific period, it can delay taking this project or product until a later date. ¨ A traditional investment analysis just answers the question of whether the project is a "good" one if taken today. ¨ Thus, the fact that a project does not pass muster today (because its NPV is negative, or its IRR is less than its hurdle rate) does not mean that the rights to this project are not valuable.

# Valuing the Option to Delay a Project

![](_page_26_Diagram_2.jpeg)

### Example 1: Valuing product patents as options

**28**

¨ A product patent provides the firm with the right to develop the product and market it. ¨ It will do so only if the present value of the expected cash flows from the product sales exceed the cost of development. ¨ If this does not occur, the firm can shelve the patent and not incur any further costs. ¨ If I is the present value of the costs of developing the product, and V is the present value of the expected cashflows from development, the payoffs from owning a product patent can be written as:

| Payoff from owning a product patent | $= V - I$ | if $V > I$    |
|-------------------------------------|-----------|---------------|
|                                     | $= 0$     | if $V \leq I$ |

# Payoff on Product Option

![](_page_28_Diagram_2.jpeg)

# Obtaining Inputs for Patent Valuation

| Input                                    | Estimation Process                                     |
|------------------------------------------|--------------------------------------------------------|
| 1. Value of the Underlying Asset         | Present Value of Cash Inflows from taking project      |
| 2. Variance in value of underlying asset | Variance in cash flows of similar assets or firms      |
| 3. Exercise Price on Option              | Option is exercised when investment is made.           |
| 4. Expiration of the Option              | Life of the patent                                     |
| 5. Dividend Yield                        | Cost of delay = Cash flow next year as % of Value      |
|                                          | If cash flows not available, use 1/n (one less year or |

# Valuing a Product Patent: Avonex

31

- ❑ Biogen, a bio-technology firm, has a patent on Avonex, a drug to treat multiple sclerosis, for the next 17 years, and it plans to produce and sell the drug by itself.
- ❑ The key inputs on the drug are as follows:
  - ❑ PV of Cash Flows from Introducing the Drug Now =  $S = \$ 3.422$  billion
  - ❑ PV of Cost of Developing Drug for Commercial Use =  $K = \$ 2.875$  billion
  - ❑ Patent Life =  $t = 17$  years Riskless Rate =  $r = 6.7\%$  (17-year T.Bond rate)
  - ❑ Variance in Expected Present Values =  $\sigma^2 = 0.224$  (Industry average firm variance for bio-tech firms)
  - ❑ Expected Cost of Delay =  $y = 1/17 = 5.89\%$  (since no cash flows are available)
- ❑ The output from the option pricing model
  - ❑  $d1 = 1.1362$   $N(d1) = 0.8720$
  - ❑  $d2 = -0.8512$   $N(d2) = 0.2076$

Call Value= 3,422  $\exp^{(-0.0589)(17}(0.8720) - 2,875 \exp^{(-0.067)(17}(0.2076)$ = \$ 907 million

# The Optimal Time to Exercise

![](_page_31_Figure_2.jpeg)

# Valuing a firm with patents

**33**

¨ The value of a firm with a substantial number of patents can be derived using the option pricing model.

Value of Firm = Value of commercial products (using DCF value

+ Value of existing patents (using option pricing) + (Value of New patents that will be obtained in the future – Cost of obtaining these patents)

¨ The last input measures the efficiency of the firm in converting its R&D into commercial products. If we assume that a firm earns its cost of capital from research, this term will become zero. ¨ If we use this approach, we should be careful not to double count and allow for a high growth rate in cash flows (in the DCF valuation).

# Value of Biogen's existing products

**34**

¨ Biogen had two commercial products (a drug to treat Hepatitis B and Intron) at the time of this valuation that it had licensed to other pharmaceutical firms. ¨ The license fees on these products were expected to generate \$ 50 million in after-tax cash flows each year for the next 12 years. ¨ To value these cash flows, which were guaranteed contractually, the pre-tax cost of debt of the guarantors was used:

Present Value of License Fees = \$ 50 million (1 – (1.07)-12)/.07 = \$ 397.13 million

# Value of Biogen's Future R&D

**35**

¨ Biogen continued to fund research into new products, spending about \$ 100 million on R&D in the most recent year. These R&D expenses were expected to grow 20% a year for the next 10 years, and 5% thereafter. ¨ It was assumed that every dollar invested in research would create \$ 1.25 in value in patents (valued using the option pricing model described above) for the next 10 years, and break even after that (i.e., generate \$ 1 in patent value for every \$ 1 invested in R&D). ¨ There was a significant amount of risk associated with this component and the cost of capital was estimated to be 15%.

# Value of Future R&D

| Yr | Value of Patents | R&D Cost  | Excess Value | PV (at 15%) |
|----|------------------|-----------|--------------|-------------|
| 1  | \$ 150.00        | \$ 120.00 | \$ 30.00     | \$ 26.09    |
| 2  | \$ 180.00        | \$ 144.00 | \$ 36.00     | \$ 27.22    |
| 3  | \$ 216.00        | \$ 172.80 | \$ 43.20     | \$ 28.40    |
| 4  | \$ 259.20        | \$ 207.36 | \$ 51.84     | \$ 29.64    |
| 5  | \$ 311.04        | \$ 248.83 | \$ 62.21     | \$ 30.93    |
| 6  | \$ 373.25        | \$ 298.60 | \$ 74.65     | \$ 32.27    |
| 7  | \$ 447.90        | \$ 358.32 | \$ 89.58     | \$ 33.68    |
| 8  | \$ 537.48        | \$ 429.98 | \$ 107.50    | \$ 35.14    |
| 9  | \$ 644.97        | \$ 515.98 | \$ 128.99    | \$ 36.67    |
| 10 | \$ 773.97        | \$ 619.17 | \$ 154.79    | \$ 38.26    |
|    |                  |           |              | \$ 318.30   |

# Value of Biogen

**37**

¨ The value of Biogen as a firm is the sum of all three components – the present value of cash flows from existing products, the value of Avonex (as an option) and the value created by new research:

Value = Existing products + Existing Patents + Value: Future R&D = \$ 397.13 million + \$ 907 million + \$ 318.30 million = \$1622.43 million

¨ Since Biogen had no debt outstanding, this value was divided by the number of shares outstanding (35.50 million) to arrive at a value per share: ¤Value per share = \$ 1,622.43 million / 35.5 = \$ 45.70

### The Real Options Test: Patents and Technology

**38**

### ¨ The Option Test:

¤ Underlying Asset: Product that would be generated by the patent ¤ Contingency: <sup>n</sup> If PV of CFs from development > Cost of development: PV - Cost <sup>n</sup> If PV of CFs from development < Cost of development: 0

### ¨ The Exclusivity Test:

¤ Patents restrict competitors from developing similar products ¤ Patents do not restrict competitors from developing other products to treat the same disease.

### ¨ The Pricing Test

¤ Underlying Asset: Patents are not traded. Not only do you therefore have to estimate the present values and volatilities yourself, you cannot construct replicating positions or do arbitrage. ¤ Option: Patents are bought and sold, though not as frequently as oil reserves or mines. ¤ Cost of Exercising the Option: This is the cost of converting the patent for commercial production. Here, experience does help and drug firms can make fairly precise estimates of the cost.

### ¨ **Conclusion: Option exists but option pricing models are stretched.**

### Example 2: Valuing Natural Resource Options

**39**

¨ In a natural resource investment, the underlying asset is the resource and the value of the asset is based upon two variables - the quantity of the resource that is available in the investment and the price of the resource. ¨ In most such investments, there is a cost associated with developing the resource, and the difference between the value of the asset extracted and the cost of the development is the profit to the owner of the resource. ¨ Defining the cost of development as X, and the estimated value of the resource as V, the potential payoffs on a natural resource option can be written as follows:

Payoff on natural resource investment = V - X if V > X = 0 if V≤ X

# Payoff Diagram on Natural Resource Firms

![](_page_39_Diagram_2.jpeg)

### Estimating Inputs for Natural Resource Options

| Input                                                 |               |         | Estimation    | Process         |                     |
|-------------------------------------------------------|---------------|---------|---------------|-----------------|---------------------|
| 1. Value of Available Reserves of the Resource Expert | estimates     |         |               | (Geologists for | oil..); The         |
| present                                               | value         | of      | the           | after-tax       | cash flows from     |
| the                                                   | resource      | are     | then          | estimated.      |                     |
| 2. Cost of Developing Reserve (Strike Price) Past     | costs and     |         | the specifics | of              | the investment      |
| 3. Time to Expiration                                 | Relinqushment |         | Period:       | if asset        | has to be           |
|                                                       | relinquished  | at      | a point       | in time.        |                     |
| Time                                                  | to exhaust    |         | inventory     | based           | upon                |
| inventory                                             | and           |         | capacity      | output.         |                     |
| 4. Variance in value of underlying asset based        | upon          |         | variability   | of the          | price of the        |
| resources                                             | and           |         | variability   | of              | available reserves. |
| 5. Net Production Revenue (Dividend Yield) Net        | production    |         | revenue       | every           | year as percent     |
| of                                                    | market        | value.  |               |                 |                     |
| 6. Development Lag Calculate                          |               | present | value         | of reserve      | based upon          |
| the                                                   | lag.          |         |               |                 |                     |

# Valuing Gulf Oil

**42**

¨ Gulf Oil was the target of a takeover in early 1984 at \$70 per share (It had 165.30 million shares outstanding, and total debt of \$9.9 billion). ¤ It had estimated reserves of 3038 million barrels of oil and the average cost of developing these reserves was estimated to be \$10 a barrel in present value dollars (The development lag is approximately two years). ¤ The average relinquishment life of the reserves is 12 years. ¤ The price of oil was \$22.38 per barrel, and the production cost, taxes and royalties were estimated at \$7 per barrel. ¤ The bond rate at the time of the analysis was 9.00%. ¤ Gulf was expected to have net production revenues each year of approximately 5% of the value of the developed reserves. The variance in oil prices is 0.03.

# Valuing Undeveloped Reserves

**43**

¨ Inputs for valuing undeveloped reserves ¤ Value of underlying asset = Value of estimated reserves discounted back for period of development lag= 3038 \* (\$ 22.38 - \$7) / 1.052 = \$42,380.44 ¤ Exercise price = Estimated development cost of reserves = 3038 \* \$10 = \$30,380 million ¤ Time to expiration = Average length of relinquishment option = 12 years ¤ Variance in value of asset = Variance in oil prices = 0.03 ¤ Riskless interest rate = 9% ¤ Cost of delay = Expected CF next year/ Value of developed reserves = 5% ¨ Based upon these inputs, the Black-Scholes model provides the following value for the call:

| $d1 = 1.6548$ | $N(d1) = 0.9510$ |
|---------------|------------------|
|               |                  |

| $d2 = 1.0548$ | $N(d2) = 0.8542$ |
|---------------|------------------|
|               |                  |

Call Value= 
$$42,380.44 \exp^{(-0.05)(12)}(0.9510) - 30,380 (\exp^{(-0.09)(12)}(0.8542))$$
  
 $= \$ 13,306 \text{ million}$ 

# Valuing Gulf Oil

**44**

¨ In addition, Gulf Oil had free cashflows to the firm from its oil and gas production of \$915 million from already developed reserves and these cashflows are likely to continue for ten years (the remaining lifetime of developed reserves). ¨ The present value of these developed reserves, discounted at the weighted average cost of capital of 12.5%, yields: ¤ Value of already developed reserves = 915 (1 - 1.125-10)/.125 = \$5065.83 ¨ Adding the value of the developed and undeveloped reserves Value of undeveloped reserves = \$ 13,306 million Value of production in place = \$ 5,066 million Total value of firm = \$ 18,372 million Less Outstanding Debt = \$ 9,900 million Value of Equity = \$ 8,472 million Value per share = \$ 8,472/165.3 = \$51.25

### B. The Option to Expand/Take Other Projects

**45**

¨ Taking a project today may allow a firm to consider and take other valuable projects in the future. ¨ Thus, even though a project may have a negative NPV, it may be a project worth taking if the option it provides the firm (to take other projects in the future) provides a more-than-compensating value. ¨ These are the options that firms often call "strategic options" and use as a rationale for taking on "negative NPV" or even "negative return" projects.

# The Option to Expand

![](_page_45_Figure_2.jpeg)

### The option to expand: Valuing a young, start-up company

**47**

¨ You have complete a DCF valuation of a small anti-virus software company, Secure Mail, and estimated a value of \$115 million. ¨ Assume that there is the possibility that the company could use the customer base that it develops for the anti-virus software and the technology on which the software is based to create a database software program sometime in the next 5 years. ¤ It will cost Secure Mail about \$500 million to develop a new database program, if they decided to do it today. ¤ Based upon the information you have now on the potential for a database program, the company can expect to generate about \$ 40 million a year in after-tax cashflows for ten years. The cost of capital for private companies that provide database software is 12%. ¤ The annualized standard deviation in firm value at publicly traded database companies is 50%. ¤ The five-year treasury bond rate is 3%.

# Valuing the Expansion Option

48

| S                                                                                       | = Value of entering the database software market                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------|-------------------------------|----------------------------|----------------------------------------------------|--------------------------|-----------------------|------------------|--------------------------------------|-----------------------------------|
|                                                                                         | = PV of \$40 million for 10 years @12%                           | = \$226 million        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| K                                                                                       | = Exercise price                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | = Cost of entering the database software market = \$ 500 million |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| t                                                                                       | = Period over which you have the right to enter the market       |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | = 5 years                                                        |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| σ                                                                                       | = Standard deviation of stock prices of database firms = 50%     |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| r                                                                                       | = Riskless rate = 3%                                             |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | <input type="checkbox"/> Call Value= \$ 56 Million               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | DCF valuation of the firm                                        | = \$ 115 million       |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Value of Option to Expand to Database market                     | = \$ 56 million        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Value of the company with option to expand                       | = \$ 171 million       |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Debt Ratio                                                                              | Cost of Equity                                                   | Cost of Debt           | Cost of Capital               |                            |                                                    |                          |                       |                  |                                      |                                   |
| 0.00%                                                                                   | 13.00%                                                           | 4.61%                  | 13.00%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 10.00%                                                                                  | 13.43%                                                           | 4.61%                  | 12.55%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| Current:18%                                                                             | 13.85%                                                           | 4.80%                  | 12.22%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 20.00%                                                                                  | 13.96%                                                           | 4.99%                  | 12.17%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 30.00%                                                                                  | 14.65%                                                           | 5.28%                  | 11.84%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 40.00%                                                                                  | 15.56%                                                           | 5.76%                  | 11.64%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 50.00%                                                                                  | 16.85%                                                           | 6.56%                  | 11.70%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 60.00%                                                                                  | 18.77%                                                           | 7.68%                  | 12.11%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 70.00%                                                                                  | 21.97%                                                           | 7.68%                  | 11.97%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 80.00%                                                                                  | 28.95%                                                           | 7.97%                  | 12.17%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
| 90.00%                                                                                  | 52.14%                                                           | 9.42%                  | 13.69%                        |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Estimated as                                                     | In general…            | For Disney                    |                            |                                                    |                          |                       |                  |                                      |                                   |
| S                                                                                       | Expected annual reinvestment                                     |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| s 2                                                                                     | Variance in annual                                               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| K                                                                                       | (Internal + Normal access to                                     |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| T                                                                                       | 1 year                                                           | Measures an annual     |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| $d1 = 1.5994$                                                                           | $N(d1) = 0.9451$                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| $d1 = 1.0515$                                                                           | $N(d1) = 0.8534$                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| $d2 = -0.2135$                                                                          | $N(d2) = 0.4155$                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Firm A                                                           | Firm B                 |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of the firm                                                                       | \$100 million                                                    | \$ 150 million         |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Face Value of Debt (10 yr                                                               | zeros) \$ 80 million                                             | \$ 50 million          |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Maturity of debt                                                                        | 10 years                                                         | 10 years               |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Std. Dev. in value                                                                      | 40 %                                                             | 50 %                   |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Correlation between cashflows                                                           |                                                                  | 0.4                    |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Firm A                                                           | Firm B                 | Combined firm                 |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of equity in the firm                                                             | \$75.94                                                          | \$134.47               | \$ 207.43                     |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of debt in the firm                                                               | \$24.06                                                          | \$ 15.53               | \$ 42.57                      |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of the firm                                                                       | \$100.00                                                         | \$150.00               | \$ 250.00                     |                            |                                                    |                          |                       |                  |                                      |                                   |
| Input                                                                                   | Estimation Process                                               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of the Firm                                                                       | Cumulate market values of equity and debt (or)                   |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | Value the assets in place using FCFF and WACC (or)               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Variance in Firm Value                                                                  | If stocks and bonds are traded,                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | σ 2firm = we2 σ e2 + wd2 σ d 2 + 2 we wd ρ ed σ e σ d            |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | where σ e2 = variance in the stock price                         |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | we = MV weight of Equity                                         |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | σ d 2 = the variance in the bond price wd = MV weight of         |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Value of the Debt                                                                       | If the debt is short term, you can use only the face or book     |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Maturity of the Debt                                                                    | Face value weighted duration of bonds outstanding (or)           |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Debt Type                                                                               | Face Value                                                       | Duration               |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Short term                                                                              | 935                                                              | 0.50                   |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| 10 year                                                                                 | 2435                                                             | 6.7                    |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| 20 year                                                                                 | 3555                                                             | 12.6                   |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Longer                                                                                  | 1940                                                             | 18.2                   |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Total                                                                                   | £8,865 mil                                                       | 10.93 years            |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| ■ $d1 = -0.8337$                                                                        | $N(d1) = 0.2023$                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| ■ $d2 = -1.4392$                                                                        | $N(d2) = 0.0751$                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| <b>Test</b>                                                                             | <b>Passed/Failed</b>                                             | <b>Rationalization</b> |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Risk transference                                                                       |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Debt subsidies                                                                          |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Control premium                                                                         |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| The value of synergy                                                                    |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Comparables and Exit Multiples                                                          |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Bias                                                                                    |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| A successful acquisition strategy                                                       |                                                                  |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Revenues                                                                                | 100                                                              |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Operating Expenses                                                                      | 80                                                               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| = Operating Income                                                                      | 20                                                               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Taxes                                                                                   | 8                                                                |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| = After-tax OI                                                                          | 12                                                               |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Free Cashflow to Equity                                                                 | P&G \$5,864.74                                                   | Gillette \$1,547.50    | Piglet: No Synergy \$7,412.24 | Piglet: Synergy \$7,569.73 | Annual operating expenses reduced by \$250 million |                          |                       |                  |                                      |                                   |
| Growth rate for first 5 years                                                           | 12%                                                              | 10%                    | 11.58%                        | 12.50%                     | Slighly higher growth rate                         |                          |                       |                  |                                      |                                   |
| Growth rate after five years                                                            | 4%                                                               | 4%                     | 4.00%                         | 4.00%                      |                                                    |                          |                       |                  |                                      |                                   |
| Beta                                                                                    | 0.90                                                             | 0.80                   | 0.88                          | 0.88                       |                                                    |                          |                       |                  |                                      |                                   |
| Cost of Equity                                                                          | 7.90%                                                            | 7.50%                  | 7.81%                         | 7.81%                      | Value of synergy                                   |                          |                       |                  |                                      |                                   |
| Value of Equity                                                                         | \$221,292                                                        | \$59,878               | \$281,170                     | \$298,355                  | \$17,185                                           |                          |                       |                  |                                      |                                   |
| This                                                                                    | Or this                                                          |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Sole Bidder                                                                             | Bidding War                                                      |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Public target                                                                           | Private target                                                   |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Pay with cash                                                                           | Pay with stock                                                   |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Small target                                                                            | Large target                                                     |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Cost synergies                                                                          | Growth synergies                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| Sub Group                                                                               | count                                                            | Median Value           |                               | % with ROE>COE             | Median Value                                       |                          | % with ROC>WACC       | % with ROIC<WACC | % with ROIC greater than WACC by >5% | % with ROIC less than WACC by >5% |
|                                                                                         |                                                                  | ROE                    | Cost of Equity                |                            | ROIC                                               | Cost of Capital          |                       |                  |                                      |                                   |
| Africa and Middle East                                                                  | 1,836                                                            | 8.14%                  | 13.93%                        | 33.22%                     | 5.81%                                              | 11.70%                   | 29.96%                | 70.04%           | 20.00%                               | 47.01%                            |
| Australia & NZ                                                                          | 1,747                                                            | -9.04%                 | 10.51%                        | 22.36%                     | -5.36%                                             | 10.43%                   | 25.72%                | 74.28%           | 18.88%                               | 41.88%                            |
| Canada                                                                                  | 2,722                                                            | -12.09%                | 10.54%                        | 17.13%                     | -7.99%                                             | 10.44%                   | 19.96%                | 80.04%           | 14.54%                               | 41.19%                            |
| China                                                                                   | 6,955                                                            | 7.15%                  | 12.14%                        | 27.96%                     | 4.64%                                              | 11.00%                   | 27.25%                | 72.75%           | 17.32%                               | 43.20%                            |
| EU & Environs                                                                           | 5,243                                                            | 8.46%                  | 12.11%                        | 36.99%                     | 6.66%                                              | 10.66%                   | 37.74%                | 62.26%           | 27.09%                               | 50.17%                            |
| Eastern Europe & Russia                                                                 | 287                                                              | 7.85%                  | 13.31%                        | 32.87%                     | 4.96%                                              | 11.61%                   | 28.83%                | 71.17%           | 20.27%                               | 43.94%                            |
| India                                                                                   | 3,574                                                            | 8.37%                  | 14.31%                        | 34.00%                     | 6.29%                                              | 12.85%                   | 29.63%                | 70.37%           | 19.71%                               | 42.87%                            |
| Japan                                                                                   | 3,787                                                            | 7.06%                  | 12.51%                        | 23.75%                     | 5.93%                                              | 10.79%                   | 30.83%                | 69.17%           | 19.87%                               | 50.36%                            |
| Latin America & Caribbean                                                               | 821                                                              | 10.13%                 | 16.17%                        | 32.21%                     | 9.30%                                              | 12.50%                   | 40.90%                | 59.10%           | 26.45%                               | 52.00%                            |
| Small Asia                                                                              | 8,792                                                            | 7.09%                  | 13.31%                        | 27.71%                     | 4.77%                                              | 11.35%                   | 24.71%                | 75.29%           | 15.10%                               | 41.29%                            |
| UK                                                                                      | 1,052                                                            | 5.76%                  | 12.32%                        | 33.22%                     | 6.56%                                              | 10.95%                   | 41.53%                | 58.47%           | 31.36%                               | 52.28%                            |
| United States                                                                           | 5,593                                                            | 3.51%                  | 11.37%                        | 35.20%                     | 7.44%                                              | 10.10%                   | 46.89%                | 53.11%           | 37.53%                               | 51.67%                            |
| Global                                                                                  | 42,409                                                           | 6.64%                  | 12.31%                        | 29.49%                     | 5.19%                                              | 10.86%                   | 30.64%                | 69.36%           | 20.86%                               | 51.68%                            |
| Year                                                                                    | 1                                                                | 2                      | 3                             | 4                          | 5                                                  | 6                        | 7                     | 8                | 9                                    | 10                                |
| EBIT                                                                                    | 2,483                                                            | 2,767                  | 3,083                         | 3,436                      | 3,829                                              | 4,206                    | 4,552                 | 4,854            | 5,097                                | 5,271                             |
| EBIT(1-t)                                                                               | 1,576                                                            | 1,756                  | 1,957                         | 2,181                      | 2,430                                              | 2,669                    | 2,889                 | 3,080            | 3,235                                | 3,345                             |
| - Reinvestm                                                                             | 905                                                              | 1,008                  | 1,124                         | 1,252                      | 1,395                                              | 1,501                    | 1,591                 | 1,660            | 1,705                                | 1,724                             |
| = FCFF                                                                                  | 671                                                              | 748                    | 833                           | 929                        | 1,035                                              | 1,168                    | 1,298                 | 1,420            | 1,530                                | 1,621                             |
| Debt Ratio                                                                              | Beta                                                             | Cost of Equity         | Bond Rating                   | Interest rate on debt      | Tax Rate                                           | Cost of Debt (after-tax) | WACC                  | Firm Value (G)   |                                      |                                   |
| 0%                                                                                      | 1.25                                                             | 8.72%                  | AAA                           | 3.76%                      | 36.54%                                             | 2.39%                    | 8.72%                 | \$39,088         |                                      |                                   |
| 10%                                                                                     | 1.34                                                             | 9.09%                  | AAA                           | 3.76%                      | 36.54%                                             | 2.39%                    | 8.42%                 | \$41,480         |                                      |                                   |
| 20%                                                                                     | 1.45                                                             | 9.56%                  | A                             | 4.26%                      | 36.54%                                             | 2.70%                    | 8.19%                 | \$43,567         |                                      |                                   |
| 30%                                                                                     | 1.59                                                             | 10.16%                 | A-                            | 4.41%                      | 36.54%                                             | 2.80%                    | 7.95%                 | \$45,900         |                                      |                                   |
| 40%                                                                                     | 1.78                                                             | 10.96%                 | CCC                           | 11.41%                     | 36.54%                                             | 7.24%                    | 9.47%                 | \$34,043         |                                      |                                   |
| 50%                                                                                     | 2.22                                                             | 12.85%                 | C                             | 15.41%                     | 22.08%                                             | 12.01%                   | 12.43%                | \$22,444         |                                      |                                   |
| 60%                                                                                     | 2.78                                                             | 15.21%                 | C                             | 15.41%                     | 18.40%                                             | 12.58%                   | 13.63%                | \$19,650         |                                      |                                   |
| 70%                                                                                     | 3.70                                                             | 19.15%                 | C                             | 15.41%                     | 15.77%                                             | 12.98%                   | 14.83%                | \$17,444         |                                      |                                   |
| 80%                                                                                     | 5.55                                                             | 27.01%                 | C                             | 15.41%                     | 13.80%                                             | 13.28%                   | 16.03%                | \$15,658         |                                      |                                   |
| 90%                                                                                     | 11.11                                                            | 50.62%                 | C                             | 15.41%                     | 12.26%                                             | 13.52%                   | 17.23%                | \$14,181         |                                      |                                   |
|                                                                                         |                                                                  | Value of Equity        | Value per s hare              |                            |                                                    |                          |                       |                  |                                      |                                   |
| Status Quo                                                                              |                                                                  | \$ 955 million         | \$ 5.13 per share             |                            |                                                    |                          |                       |                  |                                      |                                   |
| Optimally mana                                                                          | ged                                                              | \$2,323 million        | \$12.47 per share             |                            |                                                    |                          |                       |                  |                                      |                                   |
| Capital Invested in Assets in Place =                                                   | \$ 100                                                           |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| EVA from Assets in Place = $(.15 - .10) \cdot (100) / .10$ =                            | \$ 50                                                            |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| + PV of EVA from New Investments in Year 1 = $[(.15 - .10) \cdot (10) / .10]$ =         | \$ 5                                                             |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| + PV of EVA from New Investments in Year 2 = $[(.15 - .10) \cdot (10) / .10] / 1.1 =$   | \$ 4.55                                                          |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| + PV of EVA from New Investments in Year 3 = $[(.15 - .10) \cdot (10) / .10] / 1.1^2 =$ | \$ 4.13                                                          |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| + PV of EVA from New Investments in Year 4 = $[(.15 - .10) \cdot (10) / .10] / 1.1^3 =$ | \$ 3.76                                                          |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| + PV of EVA from New Investments in Year 5 = $[(.15 - .10) \cdot (10) / .10] / 1.1^4 =$ | \$ 3.42                                                          |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
| <b>Value of Firm =</b>                                                                  | <b>\$ 170.85</b>                                                 |                        |                               |                            |                                                    |                          |                       |                  |                                      |                                   |
|                                                                                         | <i>Base<br/>Year</i>                                             | <i>I</i>               | <i>2</i>                      | <i>3</i>                   | <i>4</i>                                           | <i>5</i>                 | <i>Term.<br/>Year</i> |                  |                                      |                                   |
| EBIT (1-t) : Assets in Place                                                            | \$ 15.00                                                         | \$ 15.00               | \$ 15.00                      | \$ 15.00                   | \$ 15.00                                           | \$ 15.00                 |                       |                  |                                      |                                   |
| EBIT(1-t) : Investments- Yr 1                                                           |                                                                  | \$ 1.50                | \$ 1.50                       | \$ 1.50                    | \$ 1.50                                            | \$ 1.50                  |                       |                  |                                      |                                   |
| EBIT(1-t) : Investments- Yr 2                                                           |                                                                  |                        | \$ 1.50                       | \$ 1.50                    | \$ 1.50                                            | \$ 1.50                  |                       |                  |                                      |                                   |
| EBIT(1-t): Investments - Yr 3                                                           |                                                                  |                        |                               | \$ 1.50                    | \$ 1.50                                            | \$ 1.50                  |                       |                  |                                      |                                   |
| EBIT(1-t): Investments - Yr 4                                                           |                                                                  |                        |                               |                            | \$ 1.50                                            | \$ 1.50                  |                       |                  |                                      |                                   |
| EBIT(1-t): Investments- Yr 5                                                            |                                                                  |                        |                               |                            |                                                    | \$ 1.50                  |                       |                  |                                      |                                   |
| Total EBIT(1-t)                                                                         |                                                                  | \$ 16.50               | \$ 18.00                      | \$ 19.50                   | \$ 21.00                                           | \$ 22.50                 | \$ 23.63              |                  |                                      |                                   |
| - Net Capital Expenditures                                                              | \$10.00                                                          | \$ 10.00               | \$ 10.00                      | \$ 10.00                   | \$ 10.00                                           | \$ 11.25                 | \$ 11.81              |                  |                                      |                                   |
| FCFF                                                                                    |                                                                  | \$ 6.50                | \$ 8.00                       | \$ 9.50                    | \$ 11.00                                           | \$ 11.25                 | \$ 11.81              |                  |                                      |                                   |
| Year                                                                                    |                                                                  | 0                      | 1                             | 2                          | 3                                                  | 4                        | 5                     | Term Year        |                                      |                                   |
| FCFF                                                                                    |                                                                  |                        | \$ 6.50                       | \$ 8.00                    | \$ 9.50                                            | \$ 11.00                 | \$ 11.25              | \$ 11.81         |                                      |                                   |
| PV of FCFF                                                                              |                                                                  | (\$10)                 | \$ 5.91                       | \$ 6.61                    | \$ 7.14                                            | \$ 7.51                  | \$ 6.99               |                  |                                      |                                   |
| Terminal Value                                                                          |                                                                  |                        |                               |                            |                                                    |                          | \$ 236.25             |                  |                                      |                                   |
| PV of Terminal                                                                          | Value                                                            |                        |                               |                            |                                                    |                          | \$ 146.69             |                  |                                      |                                   |
| Value of Firm                                                                           |                                                                  | \$170.85               |                               |                            |                                                    |                          |                       |                  |                                      |                                   |