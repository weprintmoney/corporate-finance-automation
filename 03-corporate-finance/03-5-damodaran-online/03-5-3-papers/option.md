---
title: "Option"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/option.pdf
---

---

# **VALUATION: PACKET 3 REAL OPTIONS, ACQUISITION VALUATION AND VALUE ENHANCEMENT**

Updated: January 2025

**1**

Aswath Damodaran

# **REAL OPTIONS: FACT AND FANTASY**

# UNDERLYING THEME: SEARCHING FOR AN ELUSIVE PREMIUM

- ▪ Traditional discounted cashflow models underestimate the value of investments, where there are options embedded in the investments to
  - ▪ Delay or defer making the investment (delay)
  - ▪ Adjust or alter production schedules as price changes (flexibility)
  - ▪ Expand into new markets or products at later stages in the process, based upon observing favorable outcomes at the early stages (expansion)
  - ▪ Stop production or abandon investments if the outcomes are unfavorable at early stages (abandonment)
- ▪ Put another way, real option advocates believe that you should be paying a premium on discounted cashflow value estimates.

# A BAD INVESTMENT...

![](_page_3_Diagram_32.jpeg)

# BECOMES A GOOD ONE...

![](_page_4_Diagram_35.jpeg)

# THREE BASIC QUESTIONS

- ■ When is there a real option embedded in a decision or an asset?
- ■ When does that real option have significant economic value?
- ■ Can that value be estimated using an option pricing model?

# WHEN IS THERE AN OPTION EMBEDDED IN AN ACTION?

- ▪ An option provides the holder with the right to buy or sell a specified quantity of an underlying asset at a fixed price (called a strike price or an exercise price) at or before the expiration date of the option.
- ▪ There has to be a clearly defined underlying asset whose value changes over time in unpredictable ways.
- ▪ The payoffs on this asset (real option) have to be contingent on a specified event occurring within a finite period.

# PAYOFF DIAGRAM ON A CALL

![](_page_7_Diagram_24.jpeg)

# PAYOFF DIAGRAM ON PUT OPTION

![](_page_8_Diagram_24.jpeg)

# WHEN DOES THE OPTION HAVE SIGNIFICANT ECONOMIC VALUE?

- ■ For an option to have significant economic value, there has to be a **restriction on competition** in the event of the contingency. In a perfectly competitive product market, no contingency, no matter how positive, will generate positive net present value.
- ■ At the limit, real options are most valuable **when you have exclusivity** - you and only you can take advantage of the contingency. They become less valuable as the barriers to competition become less steep.

# DETERMINANTS OF OPTION VALUE

- ▪ Variables Relating to Underlying Asset
  - ▪ **Value of Underlying Asset**; as this value increases, the right to buy at a fixed price (calls) will become more valuable and the right to sell at a fixed price (puts) will become less valuable.
  - ▪ **Variance in that value**; as the variance increases, both calls and puts will become more valuable because all options have limited downside and depend upon price volatility for upside.
  - ▪ **Expected dividends on the asset**, which are likely to reduce the price appreciation component of the asset, reducing the value of calls and increasing the value of puts.
- ▪ Variables Relating to Option
  - ▪ **Strike Price of Options**; the right to buy (sell) at a fixed price becomes more (less) valuable at a lower price.
  - ▪ **Life of the Option**; both calls and puts benefit from a longer life.
- ▪ **Level of Interest Rates**; as rates increase, the right to buy (sell) at a fixed price in the future becomes more (less) valuable.

# WHEN CAN YOU USE OPTION PRICING MODELS TO VALUE REAL OPTIONS?

- ▪ The notion of a replicating portfolio that drives option pricing models makes them most suited for valuing real options where
  - ▪ The **underlying asset is traded** - this yield not only observable prices and volatility as inputs to option pricing models but allows for the possibility of creating replicating portfolios
  - ▪ An **active marketplace exists for the option** itself.
  - ▪ The **cost of exercising the option is known** with some degree of certainty.
- ▪ When option pricing models are used to value real assets, we have to accept the fact that
  - ▪ The value estimates that emerge will be **far more imprecise**.
  - ▪ The value can **deviate much more dramatically from market price** because of the difficulty of arbitrage.

# CREATING A REPLICATING PORTFOLIO

- ■ The objective in creating a replicating portfolio is to use a **combination of riskfree borrowing/lending and the underlying asset to create the same cashflows as the option** being valued.
  - ■ Call = Borrowing + Buying D of the Underlying Stock
  - ■ Put = Selling Short D on Underlying Asset + Lending
  - ■ The number of shares bought or sold is called the option delta.
- ■ The **principles of arbitrage** then apply, and the value of the option has to be equal to the value of the **replicating portfolio**.

# THE BINOMIAL OPTION PRICING MODEL

![](_page_13_Diagram_102.jpeg)

# THE LIMITING DISTRIBUTIONS....

- ▪ As the time interval is shortened, the limiting distribution, as  $t \rightarrow 0$ , can take one of two forms.
  - ▪ If as  $t \rightarrow 0$ , **price changes become smaller**, the limiting distribution is the normal distribution and the price process is a continuous one.
  - ▪ If as  $t \rightarrow 0$ , **price changes remain large**, the limiting distribution is the Poisson distribution, i.e., a distribution that allows for price jumps.
- ▪ The Black-Scholes model applies when the limiting distribution is the normal distribution and explicitly **assumes that the price process is continuous** and that there are no jumps in asset prices.

# BLACK AND SCHOLES...

- ■ The version of the model presented by Black and Scholes was designed to value European options, which were dividend-protected.
- ■ The value of a call option in the Black-Scholes model can be written as a function of the following variables:
  - ■  $S$  = Current value of the underlying asset
  - ■  $K$  = Strike price of the option
  - ■  $t$  = Life to expiration of the option
  - ■  $r$  = Riskless interest rate corresponding to the life of the option
  - ■  $\sigma^2$  = Variance in the  $\ln(\text{value})$  of the underlying asset

# THE BLACK SCHOLES MODEL

- ▪ Value of call =  $S N(d_1) - K e^{-rt} N(d_2)$

- ▪ where

- ▪ 
  $$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r + \frac{\sigma^2}{2})t}{\sigma \sqrt{t}}$$

- ▪ 
  $$d_2 = d_1 - \sigma \sqrt{t}$$

- ▪ The replicating portfolio is embedded in the Black-Scholes model. To replicate this call, you would need to
  - ▪ Buy  $N(d_1)$  shares of stock;  $N(d_1)$  is called the option delta
  - ▪ Borrow  $K e^{-rt} N(d_2)$

# THE NORMAL DISTRIBUTION

![](_page_17_Figure_326.jpeg)

| $d$   | $N(d)$ | $d$   | $N(d)$ | $d$  | $N(d)$ |
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

# ADJUSTING FOR DIVIDENDS

- ▪ If the dividend yield ( $y = \text{dividends} / \text{Current value of the asset}$ ) of the underlying asset is expected to remain unchanged during the life of the option, the Black-Scholes model can be modified to take dividends into account.

- ▪ 
  $$C = S e^{-yt} N(d_1) - K e^{-rt} N(d_2)$$

- - ▪ where,

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r - y + \frac{\sigma^2}{2})t}{\sigma \sqrt{t}}$$

- - ▪ 
    $$d_2 = d_1 - \sigma \sqrt{t}$$

- ▪ The value of a put can also be derived:

- - ▪ 
    $$P = K e^{-rt} (1 - N(d_2)) - S e^{-yt} (1 - N(d_1))$$

# DIVIDEND YIELD = COST OF DELAY

- ▪ Options have time premiums, and when they are traded, you very seldom get early exercise, with one exception being calls before big ex-dividend dates. The trade off that drives early exercise is:
  - ▪ **Loss of the time premium** of the option from **exercising early** (against)
  - ▪ **Dividends you will receive**, if you exercise early
  - ▪ If the dividend exceeds the time premium, you will see early exercise.
- ▪ Put differently, the dividends foregone become the cost of delaying exercise and leaving the option live.
- ▪ Thus, having a cost of delay in an option will require that you use a dividend-adjusted version of the option pricing model.

# CHOICE OF OPTION PRICING MODELS

- ■ Most practitioners who use option pricing models to value real options argue for the binomial model over the Black-Scholes and justify this choice by noting that
  - ■ Early exercise is the rule rather than the exception with real options
  - ■ Underlying asset values are generally discontinuous.
- ■ If you can develop a binomial tree with outcomes at each node, it looks a great deal like a decision tree from capital budgeting. The question then becomes when and why the two approaches yield different estimates of value.

# THE DECISION TREE ALTERNATIVE

- ▪ Traditional decision tree analysis tends to use
  - ▪ One cost of capital to discount cashflows in each branch to the present
  - ▪ Probabilities to compute an expected value
  - ▪ These values will generally be different from option pricing model values
- ▪ If you modified decision tree analysis to
  - ▪ Use **different discount rates at each node** to reflect where you are in the decision tree (This is the Copeland solution) (or)
  - ▪ Use the **riskfree rate to discount cashflows in each branch**, estimate the probabilities to estimate an expected value and adjust the expected value for the market risk in the investment
- ▪ Decision Trees could yield the same values as option pricing models

# A DECISION TREE VALUATION OF A PHARMACEUTICAL COMPANY WITH ONE DRUG IN THE FDA PIPELINE...

![](_page_22_Diagram_154.jpeg)

# KEY TESTS FOR REAL OPTIONS

- ▪ Is there an option embedded in this asset/ decision?
  - ▪ Can you identify **the underlying asset**?
  - ▪ Can you specify **the contingency under which you will get payoff**?
- ▪ Is there exclusivity?
  - ▪ **If yes**, there is option value.
  - ▪ **If no**, there is none.
  - ▪ If in between, you have to scale value.
- ▪ Can you use an option pricing model to value the real option?
  - ▪ Is the underlying asset traded?
  - ▪ Can the option be bought and sold?
  - ▪ Is the cost of exercising the option known and clear?

# I. OPTIONS IN PROJECTS/INVESTMENTS/ACQUISITIONS

- ▪ One of the limitations of traditional investment analysis is that **it is static** and does not do a good job of capturing the options embedded in investment.
  - ▪ The first of these options is the **option to delay taking a investment**, when a firm has exclusive rights to it, until a later date.
  - ▪ The second of these options is taking one investment may allow us to take **advantage of other opportunities (investments) in the future**
  - ▪ The last option that is embedded in projects is the **option to abandon an investment**, if the cash flows do not measure up.
- ▪ These **options all add value** to projects and may make a “bad” investment (from traditional analysis) into a good one.

## A. THE OPTION TO DELAY

- ▪ When a firm has **exclusive rights to a project or product** for a specific period, it can delay taking this project or product until a later date.
- ▪ A traditional investment analysis **just answers the question of whether the project is a “good” one if taken today.**
- ▪ Thus, the fact that a project **does not pass muster today** (because its NPV is negative, or its IRR is less than its hurdle rate) does not mean that the rights to this project are not valuable.

# VALUING THE OPTION TO DELAY A PROJECT

![](_page_26_Diagram_39.jpeg)

# EXAMPLE 1: VALUING PRODUCT PATENTS AS OPTIONS

- ▪ A product patent provides the firm with the right to develop the product and market it.
  - ▪ It will do so only if the present value of the expected cash flows from the product sales exceed the cost of development.
  - ▪ If this does not occur, the firm can shelve the patent and not incur any further costs.
- ▪ If  $I$  is the present value of the costs of developing the product, and  $V$  is the present value of the expected cashflows from development, the payoffs from owning a product patent can be written as:
- ▪ Payoff from owning a product patent  $= V - I$  if  $V > I$   
   $= 0$  if  $V \leq I$

# PAYOFF ON PRODUCT OPTION

![](_page_28_Diagram_27.jpeg)

# OBTAINING INPUTS FOR PATENT VALUATION

| Input                                    | Estimation Process                                                                                                                                                                                       |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Value of the Underlying Asset         | <ul> <li>• Present Value of Cash Inflows from taking project now</li> <li>• This will be noisy, but that adds value.</li> </ul>                                                                          |
| 2. Variance in value of underlying asset | <ul> <li>• Variance in cash flows of similar assets or firms</li> <li>• Variance in present value from capital budgeting simulation.</li> </ul>                                                          |
| 3. Exercise Price on Option              | <ul> <li>• Option is exercised when investment is made.</li> <li>• Cost of making investment on the project; assumed to be constant in present value dollars.</li> </ul>                                 |
| 4. Expiration of the Option              | <ul> <li>• Life of the patent</li> </ul>                                                                                                                                                                 |
| 5. Dividend Yield                        | <ul> <li>• Cost of delay = Cash flow next year as % of Value of Underlying asset</li> <li>• If cash flows not available, use <math>1/n</math> (one less year or protection from competition).</li> </ul> |

![](_page_29_Picture_5.jpeg)

# VALUING A PRODUCT PATENT: AVONEX

- ▪ Biogen, a bio-technology firm, has a patent on Avonex, a drug to treat multiple sclerosis, for the next 17 years, and it plans to produce and sell the drug by itself.
- ▪ The key inputs on the drug are as follows:
  - ▪ PV of Cash Flows from Introducing the Drug Now =  $S = \$ 3.422$  billion
  - ▪ PV of Cost of Developing Drug for Commercial Use =  $K = \$ 2.875$  billion
  - ▪ Patent Life =  $t = 17$  years      Riskless Rate =  $r = 6.7\%$  (17-year T.Bond rate)
  - ▪ Variance in Expected Present Values =  $s_2 = 0.224$  (Industry average firm variance for bio-tech firms)
  - ▪ Expected Cost of Delay =  $y = 1/17 = 5.89\%$  (since no cash flows are available)
- ▪ The output from the option pricing model
  - ▪  $d_1 = 1.1362$        $N(d_1) = 0.8720$
  - ▪  $d_2 = -0.8512$        $N(d_2) = 0.2076$
  - ▪ Call Value =  $3,422 \exp^{(-0.0589)(17)} (0.8720) - 2,875 \exp^{(-0.067)(17)} (0.2076) = \$ 907$  million

# THE OPTIMAL TIME TO EXERCISE

![](_page_31_Figure_10.jpeg)

# VALUING A FIRM WITH PATENTS

- ▪ The value of a firm with a substantial number of patents can be derived using the option pricing model.
- ▪ Value of Firm = Value of commercial products (using DCF value
  - + Value of existing patents (using option pricing)
  - + (Value of New patents that will be obtained in the future – Cost of obtaining these patents)
- ▪ The last input **measures the efficiency of the firm in converting its R&D into commercial products**. If we assume that a firm earns its cost of capital from research, this term will become zero.
- ▪ If we use this approach, we should be **careful not to double count** and allow for a high growth rate in cash flows (in the DCF valuation).

# VALUE OF BIOGEN'S EXISTING PRODUCTS

- ▪ Biogen had two commercial products (a drug to treat Hepatitis B and Intron) at the time of this valuation that it had licensed to other pharmaceutical firms.
- ▪ The license fees on these products were expected to generate \$ 50 million in after-tax cash flows each year for the next 12 years.
- ▪ To value these cash flows, which were guaranteed contractually, the pre-tax cost of debt of the guarantors was used:
  - ▪  $\text{Present Value of License Fees} = \$ 50 \text{ million} (1 - 1.07^{-12}) / .07$   
     $= \$ 397.13 \text{ million}$

# VALUE OF BIOGEN'S FUTURE R&D

- ▪ Biogen continued to fund research into new products, spending about \$ 100 million on R&D in the most recent year. These R&D expenses were expected **to grow 20% a year for the next 10 years**, and 5% thereafter.
- ▪ It was assumed that every dollar invested in research would create **\$ 1.25 in value in patents (valued using the option pricing model described above) for the next 10 years**, and break even after that (i.e., generate \$ 1 in patent value for every \$ 1 invested in R&D).
- ▪ There was a significant amount of risk associated with this component and the cost of capital was estimated to be 15%.

# VALUE OF FUTURE R&D

| ▪ Yr | Value of Patents<br>PV (at 15%) | R&D Cost  | Excess Value |                  |
|------|---------------------------------|-----------|--------------|------------------|
| ▪ 1  | \$ 150.00                       | \$ 120.00 | \$ 30.00     | \$ 26.09         |
| ▪ 2  | \$ 180.00                       | \$ 144.00 | \$ 36.00     | \$ 27.22         |
| ▪ 3  | \$ 216.00                       | \$ 172.80 | \$ 43.20     | \$ 28.40         |
| ▪ 4  | \$ 259.20                       | \$ 207.36 | \$ 51.84     | \$ 29.64         |
| ▪ 5  | \$ 311.04                       | \$ 248.83 | \$ 62.21     | \$ 30.93         |
| ▪ 6  | \$ 373.25                       | \$ 298.60 | \$ 74.65     | \$ 32.27         |
| ▪ 7  | \$ 447.90                       | \$ 358.32 | \$ 89.58     | \$ 33.68         |
| ▪ 8  | \$ 537.48                       | \$ 429.98 | \$ 107.50    | \$ 35.14         |
| ▪ 9  | \$ 644.97                       | \$ 515.98 | \$ 128.99    | \$ 36.67         |
| ▪ 10 | \$ 773.97                       | \$ 619.17 | \$ 154.79    | \$ 38.26         |
| ▪    |                                 |           |              | <b>\$ 318.30</b> |

# VALUE OF BIOGEN

- ■ The value of Biogen as a firm is the sum of all three components – the present value of cash flows from existing products, the value of Avonex (as an option) and the value created by new research:

$$\begin{aligned}\text{Value} &= \text{Existing products} + \text{Existing Patents} + \text{Value: Future R\&D} \\ &= \$ 397.13 \text{ million} + \$ 907 \text{ million} + \$ 318.30 \text{ million} \\ &= \$ 1622.43 \text{ million}\end{aligned}$$

- ■ Since Biogen had no debt outstanding, this value was divided by the number of shares outstanding (35.50 million) to arrive at a value per share:
  - ■ Value per share =  $\$ 1,622.43 \text{ million} / 35.5 = \$ 45.70$

# THE REAL OPTIONS TEST: PATENTS AND TECHNOLOGY

- ▪ **The Option Test:**
  - ▪ **Underlying Asset:** Product that would be generated by the patent
  - ▪ **Contingency:**
    - ▪ If PV of CFs from development > Cost of development: PV - Cost
    - ▪ If PV of CFs from development < Cost of development: 0
- ▪ **The Exclusivity Test:**
  - ▪ Patents restrict competitors from developing similar products
  - ▪ Patents do not restrict competitors from developing other products to treat the same disease.
- ▪ **The Pricing Test**
  - ▪ **Underlying Asset:** Patents are not traded. Not only do you therefore have to estimate the present values and volatilities yourself, you cannot construct replicating positions or do arbitrage.
  - ▪ **Option:** Patents are bought and sold, though not as frequently as oil reserves or mines.
  - ▪ **Cost of Exercising the Option:** This is the cost of converting the patent for commercial production. Here, experience does help and drug firms can make fairly precise estimates of the cost.
- ▪ **Conclusion:** Option exists but option pricing models are stretched.

# EXAMPLE 2: VALUING NATURAL RESOURCE OPTIONS

- ▪ In a natural resource investment, the underlying asset is the resource, and the value of the asset is based upon two variables
  - - **the quantity of the resource** that is available in the investment and the **price of the resource**.
- ▪ In most such investments, there is a cost associated with developing the resource, and the **difference between the value of the asset extracted and the cost of the development** is the profit to the owner of the resource.
- ▪ Defining the cost of development as  $X$ , and the estimated value of the resource as  $V$ , the potential payoffs on a natural resource option can be written as follows:
  - ▪ Payoff on natural resource investment  $= V - X$  if  $V > X$   
     $= 0$  if  $V \leq X$

# PAYOFF DIAGRAM ON NATURAL RESOURCE FIRMS

![](_page_39_Diagram_27.jpeg)

# ESTIMATING INPUTS FOR NATURAL RESOURCE OPTIONS

| Input                                          | Estimation Process                                                                                                                                                                |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Value of Available Reserves of the Resource | <ul> <li>• Expert estimates (Geologists for oil..); The present value of the after-tax cash flows from the resource are then estimated.</li> </ul>                                |
| 2. Cost of Developing Reserve (Strike Price)   | <ul> <li>• Past costs and the specifics of the investment</li> </ul>                                                                                                              |
| 3. Time to Expiration                          | <ul> <li>• Relinquishment Period: if asset has to be relinquished at a point in time.</li> <li>• Time to exhaust inventory - based upon inventory and capacity output.</li> </ul> |
| 4. Variance in value of underlying asset       | <ul> <li>• based upon variability of the price of the resources and variability of available reserves.</li> </ul>                                                                 |
| 5. Net Production Revenue (Dividend Yield)     | <ul> <li>• Net production revenue every year as percent of market value.</li> </ul>                                                                                               |
| 6. Development Lag                             | <ul> <li>• Calculate present value of reserve based upon the lag.</li> </ul>                                                                                                      |

![](_page_40_Picture_5.jpeg)

# VALUING GULF OIL

- ■ Gulf Oil was the target of a takeover in early 1984 at \$70 per share (It had 165.30 million shares outstanding, and total debt of \$9.9 billion).
  - ■ It had **estimated reserves of 3038 million barrels of oil** and the **average cost of developing these reserves was estimated to be \$10 a barrel in present value dollars** (The development lag is approximately two years).
  - ■ The average relinquishment life of the **reserves is 12 years**.
  - ■ The **price of oil was \$22.38 per barrel**, and the production cost, taxes and royalties were estimated at \$7 per barrel.
  - ■ The **treasury bond rate** at the time of the analysis was 9.00%.
  - ■ Gulf was expected to have **net production revenues each year of approximately 5% of the value** of the developed reserves. The variance in oil prices is 0.03.

# VALUING UNDEVELOPED RESERVES

- ▪ Inputs for valuing undeveloped reserves
  - ▪ Value of underlying asset = Value of estimated reserves discounted back for period of development lag =  $3038 * (\$ 22.38 - \$7) / 1.052 = \$42,380.44$
  - ▪ Exercise price = Estimated development cost of reserves =  $3038 * \$10 = \$30,380$  million
  - ▪ Time to expiration = Average length of relinquishment option = 12 years
  - ▪ Variance in value of asset = **Variance in oil prices** = 0.03
  - ▪ Riskless interest rate = 9%
  - ▪ Cost of delay = Expected CF next year/ Value of developed reserves = 5%
- ▪ Based upon these inputs, the Black-Scholes model provides the following value for the call:
  - ▪  $d1 = 1.6548$   $N(d1) = 0.9510$
  - ▪  $d2 = 1.0548$   $N(d2) = 0.8542$
  - ▪ Call Value =  $42,380.44 \exp^{(-0.05)(12)} (0.9510) - 30,380 (\exp^{(-0.09)(12)} (0.8542))$
  - ▪  $= \$ 13,306$  million

# VALUING GULF OIL

- ▪ In addition, Gulf Oil had free cashflows to the firm from its oil and gas production of \$915 million from already developed reserves and these cashflows are likely to continue for ten years (the remaining lifetime of developed reserves).
- ▪ The present value of these developed reserves, discounted at the weighted average cost of capital of 12.5%, yields:
  - ▪  $\text{Value of already developed reserves} = 915 (1 - 1.125^{-10}) / .125 = \$5065.83$
- ▪ Adding the value of the developed and undeveloped reserves
   

  | ▪ Value of undeveloped reserves | = \$ 13,306 million            |
  |---------------------------------|--------------------------------|
  | ▪ Value of production in place  | = \$ 5,066 million             |
  | ▪ Total value of firm           | = \$ 18,372 million            |
  | ▪ Less Outstanding Debt         | = \$ 9,900 million             |
  | ▪ Value of Equity               | = \$ 8,472 million             |
  | ▪ Value per share               | = $\$ 8,472 / 165.3 = \$51.25$ |

## **B. THE OPTION TO EXPAND/TAKE OTHER PROJECTS**

- ▪ Taking a project today may **allow access to other valuable projects** in the future.
- ▪ Thus, even though a project may have a negative NPV, it may be a project worth taking **if the option it provides the firm (to take other projects in the future) provides a more-than-compensating value.**
- ▪ These are the options that firms **often call “strategic options”** and use as a rationale for taking on “negative NPV” or even “negative return” projects.

# THE OPTION TO EXPAND

![](_page_45_Diagram_39.jpeg)

# THE OPTION TO EXPAND: VALUING A YOUNG, START-UP COMPANY

- ▪ You have complete a DCF valuation of a small anti-virus software company, Secure Mail, and estimated a value of \$1.15 million.
- ▪ Assume that there is the possibility that the company could use the customer base that it develops for the anti-virus software and the technology on which the software is based to create a database software program sometime in the next 5 years.
  - ▪ It will **cost Secure Mail about \$500 million** to develop a new database program, if they decided to do it today.
  - ▪ Based upon the information you have now on the potential for a database program, the company can **expect to generate about \$ 40 million a year in after-tax cashflows for ten years**. The cost of capital for private companies that provide database software **is 12%**.
  - ▪ The **annualized standard deviation** in firm value at publicly traded database companies is **50%**.
  - ▪ The **five-year treasury bond rate is 3%**.

# VALUING THE EXPANSION OPTION

| S | = Value of entering the database software market                 |                 |
|---|------------------------------------------------------------------|-----------------|
|   | = PV of \$40 million for 10 years @12%                           | = \$226 million |
| K | = Exercise price                                                 |                 |
|   | = Cost of entering the database software market = \$ 500 million |                 |
| t | = Period over which you have the right to enter the market       |                 |
|   | = 5 years                                                        |                 |
| s | = Standard deviation of stock prices of database firms = 50%     |                 |
| r | = Riskless rate = 3%                                             |                 |

▪ Call Value= \$ 56 Million

| DCF valuation of the firm | = \$ 115 million |
|---------------------------|------------------|
|---------------------------|------------------|

| Value of Option to Expand to Database market | = \$ 56 million |
|----------------------------------------------|-----------------|
|----------------------------------------------|-----------------|

| Value of the company with option to expand | = \$ 171 million |
|--------------------------------------------|------------------|
|--------------------------------------------|------------------|

# A NOTE OF CAUTION: OPPORTUNITIES ARE NOT OPTIONS...

![](_page_48_Diagram_88.jpeg)

# THE REAL OPTIONS TEST FOR EXPANSION OPTIONS

- ▪ The Options Test
  - ▪ Underlying Asset: Expansion Project
  - ▪ Contingency
  - ▪ If PV of CF from expansion > Expansion Cost: PV - Expansion Cost
  - ▪ If PV of CF from expansion < Expansion Cost: 0
- ▪ The Exclusivity Test
  - ▪ Barriers may range from strong (exclusive licenses granted by the government) to weaker (brand name, knowledge of the market) to weakest (first mover).
- ▪ The Pricing Test
  - ▪ Underlying Asset: As with patents, there is no trading in the underlying asset and you have to estimate value and volatility.
  - ▪ Option: Licenses are sometimes bought and sold, but more diffuse expansion options are not.
  - ▪ Cost of Exercising the Option: Not known with any precision and may itself evolve over time as the market evolves.
- ▪ Using option pricing models to value expansion options will not only yield extremely noisy estimates, but may attach inappropriate premiums to discounted cashflow estimates.

# C. THE OPTION TO ABANDON

- ▪ A firm may sometimes have the **option to abandon a project**, if the cash flows do not measure up to expectations.
- ▪ If abandoning the project **allows the firm to save itself from further losses**, this option can make a project more valuable.

PV of Cash Flows  
from Project

![](_page_50_Figure_48.jpeg)

# VALUING THE OPTION TO ABANDON

- ▪ Airbus is considering a **joint venture with Lear Aircraft** to produce a small commercial airplane (capable of carrying 40-50 passengers on short haul flights)
  - ▪ Airbus will have to **invest \$ 500 million for a 50% share of the venture**
  - ▪ Its share of the **present value of expected cash flows is 480 million.**
- ▪ Lear Aircraft, which is eager to enter into the deal, offers to buy Airbus's 50% share of the investment anytime over the next five years **for \$ 400 million**, if Airbus decides to get out of the venture.
- ▪ A simulation of the cash flows on this time share investment yields a **variance** in the present value of the cash flows from being in the partnership **is 0.16**.
- ▪ The project has a **life of 30 years**.

# PROJECT WITH OPTION TO ABANDON

- ▪ Value of the Underlying Asset (S)  
  = PV of Cash Flows from Project = \$ 480 million
- ▪ Strike Price (K)  
  = Salvage Value from Abandonment = \$ 400 million
- ▪ Variance in Underlying Asset's Value = 0.16
- ▪ Time to expiration = Life of the Project = 5 years
- ▪ Dividend Yield =  $1 / \text{Life of the Project}$  =  $1 / 30$  = **0.033**
- ▪ The five-year riskless rate is 6%.

# SHOULD AIRBUS ENTER INTO THE JOINT VENTURE?

- ■  $\text{Value of Put} = \text{Ke-rt} (1-N(d2)) - \text{Se-yt} (1-N(d1))$   
   $= 400 \exp^{(-0.06)(5)} (1-0.4624) - 480 \exp^{(-0.033)(5)} (1-0.7882)$   
   $= \$ 73.23 \text{ million}$
- ■ The value of this abandonment option has to be added on to the net present value of the project of -\$ 20 million, yielding a total net present value with the abandonment option of \$ 53.23 million.
- ■ While this is what Lear Aircraft wants from the deal, it has to have a large enough net present value of the cost of the put option.

# IMPLICATIONS FOR INVESTMENT ANALYSIS/ VALUATION

- ▪ Having a option to abandon a project can **make otherwise unacceptable projects acceptable.**
- ▪ Other things remaining equal, you would attach more value to companies with
  - ▪ **More cost flexibility**, that is, making more of the costs of the projects into variable costs as opposed to fixed costs.
  - ▪ **Fewer long-term contracts/obligations** with employees and customers, since these add to the cost of abandoning a project.
- ▪ These actions will undoubtedly cost the firm some value, but this has to be **weighed off against the increase in the value of the abandonment option.**

## D. OPTIONS IN CAPITAL STRUCTURE

- ▪ The most direct applications of option pricing in capital structure decisions is in the **design of securities**. In fact, most complex financial instruments can be broken down into some combination of a simple bond/common stock and a variety of options.
  - ▪ If these securities are **to be issued to the public**, and traded, the options must be priced.
  - ▪ If these are **non-traded instruments** (bank loans, for instance), they still have to be priced into the interest rate on the instrument.
- ▪ The other application of option pricing is in valuing flexibility. Often, firms preserve debt capacity or hold back on issuing debt because they want to maintain flexibility.

# THE VALUE OF FLEXIBILITY

- ▪ Firms **maintain excess debt capacity or larger cash balances** than are warranted by current needs, to meet **unexpected future requirements**.
- ▪ While **maintaining this financing flexibility has value** to firms, it also has a cost; the excess debt capacity implies that the firm is **giving up some value and has a higher cost of capital**.
- ▪ The **value of flexibility can be analyzed using the option pricing framework**; a firm maintains large cash balances and excess debt capacity in order to have the option to take projects that might arise in the future.

# THE VALUE OF FLEXIBILITY

![](_page_57_Figure_59.jpeg)

# DISNEY'S OPTIMAL DEBT RATIO

| Debt Ratio  | Cost of Equity | Cost of Debt | Cost of Capital |
|-------------|----------------|--------------|-----------------|
| 0.00%       | 13.00%         | 4.61%        | 13.00%          |
| 10.00%      | 13.43%         | 4.61%        | 12.55%          |
| Current:18% | 13.85%         | 4.80%        | 12.22%          |
| 20.00%      | 13.96%         | 4.99%        | 12.17%          |
| 30.00%      | 14.65%         | 5.28%        | 11.84%          |
| 40.00%      | 15.56%         | 5.76%        | 11.64%          |
| 50.00%      | 16.85%         | 6.56%        | 11.70%          |
| 60.00%      | 18.77%         | 7.68%        | 12.11%          |
| 70.00%      | 21.97%         | 7.68%        | 11.97%          |
| 80.00%      | 28.95%         | 7.97%        | 12.17%          |
| 90.00%      | 52.14%         | 9.42%        | 13.69%          |

# INPUTS TO OPTION VALUATION MODEL- DISNEY

| Model input    | Estimated as                                            | In general...                                              | For Disney                                                                    |
|----------------|---------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------|
| S              | Expected annual reinvestment needs (as % of firm value) | Measures magnitude of reinvestment needs                   | Average of Reinvestment/ Value over last 5 years = 5.3%                       |
| s <sup>2</sup> | Variance in annual reinvestment needs                   | Measures how much volatility there is in investment needs. | Variance over last 5 years in $\ln(\text{Reinvestment}/\text{Value}) = 0.375$ |
| K              | (Internal + Normal access to external funds)/ Value     | Measures the capital constraint                            | Average over last 5 years = 4.8%                                              |
| T              | 1 year                                                  | Measures an annual value for flexibility                   | T = 1                                                                         |

# VALUING FLEXIBILITY AT DISNEY

- ▪ The value of an option with these characteristics is 1.6092%. You can consider this the value of the option to take a project, but the overall value of flexibility will still depend upon the quality of the projects taken.
- ▪ **Disney earns 18.69% on its projects has a cost of capital of 12.22%.** The excess return (annually) is 6.47%. Assuming that they can continue to generate these excess returns in perpetuity:
  - ▪ Value of Flexibility (annual)  
    **= 1.6092%(.0647/.1222) = 0.85 % of value**
- ▪ Disney's cost of capital at its optimal debt ratio is 11.64%. The **cost it incurs to maintain flexibility is therefore 0.58% annually (12.22%-11.64%).** It therefore pays to maintain flexibility.

# DETERMINANTS OF THE VALUE OF FLEXIBILITY

- ▪ **Capital Constraints (External and Internal):** The greater the capacity to raise funds, either internally or externally, the less the value of flexibility.
  - ▪ 1.1: Firms with significant internal operating cash flows should have a lower value of flexibility than firms with small or negative operating cash flows.
  - ▪ 1.2: Firms with easy access to financial markets should have a lower value for flexibility than firms without that access.
- ▪ **Unpredictability of reinvestment needs:** The more unpredictable the reinvestment needs of a firm, the greater the value of flexibility.
- ▪ **Capacity to earn excess returns:** The greater the capacity to earn excess returns, the greater the value of flexibility.
  - ▪ 1.3: Firms that do not have the capacity to earn or sustain excess returns get no value from flexibility.

# E. VALUING EQUITY AS AN OPTION

- ■ The **equity in a firm is a residual claim**, i.e., equity holders lay claim to all cashflows left over after other financial claim-holders (debt, preferred stock etc.) have been satisfied.
- ■ If a firm is liquidated, the same principle applies, with **equity investors receiving whatever is left over in the firm** after all outstanding debts and other financial claims are paid off.
- ■ The **principle of limited liability**, **however, protects equity investors** in publicly traded firms if the value of the firm is less than the value of the outstanding debt, and they cannot lose more than their investment in the firm.

# PAYOFF DIAGRAM FOR LIQUIDATION OPTION

![](_page_63_Figure_26.jpeg)

# **APPLICATION TO VALUATION: A SIMPLE EXAMPLE**

- ■ Assume that you have a firm whose assets are **currently valued at \$100 million** and that the **standard deviation in this asset value is 40%**.
- ■ Further, assume that the **face value of debt is \$80 million** (It is zero coupon debt with 10 years left to maturity).
- ■ If the ten-year treasury bond rate is 10%,
  - ■ how much is the **equity worth**?
  - ■ What should the **interest rate on debt** be?

# MODEL PARAMETERS

- ▪ Value of the underlying asset =  $S$ 
  - ▪ Value of the firm =  $\$ 100$  million
- ▪ Exercise price =  $K$ 
  - ▪ Face Value of outstanding debt =  $\$ 80$  million
- ▪ Life of the option =  $t$ 
  - ▪ Life of zero-coupon debt = 10 years
- ▪ Variance in the value of the underlying asset =  $\sigma^2$ 
  - ▪ Variance in firm value = 0.16
- ▪ Riskless rate =  $r$ 
  - ▪ Treasury bond rate corresponding to option life = 10%

# VALUING EQUITY AS A CALL OPTION

- ▪ Based upon these inputs, the Black-Scholes model provides the following value for the call:

- ▪  $d_1 = 1.5994$                        $N(d_1) = 0.9451$

- ▪  $d_2 = 0.3345$                        $N(d_2) = 0.6310$

- ▪ Value of the call =  $100 (0.9451) - 80 \exp^{(-0.10)(10)}$   
   $(0.6310) = \$75.94$  million

- ▪ Value of the outstanding debt =  $\$100 - \$75.94 =$   
   $\$24.06$  million

- ▪ Interest rate on debt =  $(\$ 80 / \$24.06) 1/10 - 1 =$   
   $12.77\%$

# I. THE EFFECT OF CATASTROPHIC DROPS IN VALUE

- ■ Assume now that a catastrophe wipes out half the value of this firm (the value drops to \$ 50 million), while the face value of the debt remains at \$ 80 million. What will happen to the equity value of this firm?
  - a. It will drop in value to \$ 25.94 million [ \$ 50 million - market value of debt from previous page]
  - b. It will be worth nothing since debt outstanding > Firm Value
  - c. It will be worth more than \$ 25.94 million

# VALUING EQUITY IN THE TROUBLED FIRM

- ▪ Value of the underlying asset =  $S$ 
  - ▪ Value of the firm =  $\$ 50 \text{ million}$
- ▪ Exercise price =  $K$ 
  - ▪ Face Value of outstanding debt =  $\$ 80 \text{ million}$
- ▪ Life of the option =  $t$ 
  - ▪ Life of zero-coupon debt = 10 years
- ▪ Variance in the value of the underlying asset =  $\sigma^2$ 
  - ▪ Variance in firm value = 0.16
- ▪ Riskless rate =  $r$ 
  - ▪ Treasury bond rate corresponding to option life = 10%

# THE VALUE OF EQUITY AS AN OPTION

- ▪ Based upon these inputs, the Black-Scholes model provides the following value for the call:
  - ▪  $d1 = 1.0515$
  - ▪  $d2 = -0.2135$
  $$N(d1) = 0.8534$$
  $$N(d2) = 0.4155$$
- ▪ Value of the call =  $50 (0.8534) - 80 \exp^{(-0.10)(10)} (0.4155) = \$30.44$  million
- ▪ Value of the bond =  $\$50 - \$30.44 = \$19.56$  million
- ▪ The **equity in this firm drops by \$45.50 million**, less than the overall drop in value of \$50 million, because of the option characteristics of equity.
- ▪ This might explain why stock in firms, which are in Chapter 11 and essentially bankrupt, still has value.

# EQUITY VALUE PERSISTS ..

Value of Equity as Firm Value Changes

![](_page_70_Figure_69.jpeg)

# II. THE CONFLICT BETWEEN STOCKHOLDERS AND BONDHOLDERS

- ▪ Consider again the firm described in the earlier example , with a value of assets of \$100 million, a face value of zero-coupon ten-year debt of \$80 million, a standard deviation in the value of the firm of 40%. The equity and debt in this firm were valued as follows:
  - ▪ Value of Equity = \$75.94 million
  - ▪ Value of Debt = \$24.06 million
  - ▪ Value of Firm == \$100 million
- ▪ Now assume that the stockholders have the opportunity to take a project with a **negative net present value of -\$2 million**, but assume that this project is a **very risky project that will push up the standard deviation in firm value to 50%**. Would you invest in this project?
  - ▪ Yes
  - ▪ No

# VALUING EQUITY AFTER THE PROJECT

- ▪ Value of the underlying asset = S
  - ▪ Value of the firm =  $\$ 100 \text{ million} - \$ 2 \text{ million} = \$ 98 \text{ million}$  (The value of the firm is lowered because of the negative net present value project)
- ▪ Exercise price = K
  - ▪ Face Value of outstanding debt =  $\$ 80 \text{ million}$
- ▪ Life of the option = t
- ▪ Life of zero-coupon debt = 10 years
- ▪ Variance in the value of the underlying asset =  $\sigma^2$ 
  - ▪ Variance in firm value = 0.25
- ▪ Riskless rate = r
  - ▪ Treasury bond rate corresponding to option life = 10%

# OPTION VALUATION

- ▪ Option Pricing Results for Equity and Debt Value
  - ▪ Value of Equity = \$77.71
  - ▪ Value of Debt = \$20.29
  - ▪ Value of Firm = \$98.00
- ▪ The value of equity rises from \$75.94 million to \$77.71 million , even though the firm value declines by \$2 million. The increase in equity value comes at the expense of bondholders, who find their wealth decline from \$24.06 million to \$20.19 million.

# EFFECTS OF AN ACQUISITION

- ■ Assume that you are the manager of a firm and that you buy another firm, with a fair market value of \$ 150 million, for exactly \$ 150 million. In an efficient market, the stock price of your firm will
  - ■ Increase
  - ■ Decrease
  - ■ Remain Unchanged

# EFFECTS ON EQUITY OF A CONGLOMERATE MERGER

- ▪ You are provided information on two firms, which operate in unrelated businesses and hope to merge.

|                                  | Firm A        | Firm B         |
|----------------------------------|---------------|----------------|
| Value of the firm                | \$100 million | \$ 150 million |
| Face Value of Debt (10 yr zeros) | \$ 80 million | \$ 50 million  |
| Maturity of debt                 | 10 years      | 10 years       |
| Std. Dev. in value               | 40 %          | 50 %           |
| Correlation between cashflows    | 0.4           |                |

- ▪ The ten-year bond rate is 10%.

- ▪ The variance in the value of the firm after the acquisition can be calculated as follows:

- - ▪ Variance in combined firm value

$$= w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho^{1/2} \sigma_1 \sigma_2$$

$$= (0.4)^2 (0.16) + (0.6)^2 (0.25) + 2 (0.4) (0.6) (0.4) (0.4) (0.5)$$

$$= 0.154$$

# VALUING THE COMBINED FIRM

- The values of equity and debt in the individual firms and the combined firm can then be estimated using the option pricing model:

|                                                                                                                                                                                                                                                                                            | <i>Firm A</i> | <i>Firm B</i> | <i>Combined firm</i> |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------|----------------------|
| Value of equity in the firm                                                                                                                                                                                                                                                                | \$75.94       | \$134.47      | \$ 207.43            |
| Value of debt in the firm                                                                                                                                                                                                                                                                  | \$24.06       | \$ 15.53      | \$ 42.57             |
| Value of the firm                                                                                                                                                                                                                                                                          | \$100.00      | \$150.00      | \$ 250.00            |
| <ul><li>The combined value of the equity prior to the merger is \$ 210.41 million and it declines to \$207.43 million after.</li><li>The wealth of the bondholders increases by an equal amount.</li></ul>                                                                                 |               |               |                      |
| <ul><li>There is a <b>transfer of wealth from stockholders to bondholders, as a consequence of the merger</b>. Thus, conglomerate mergers that are not followed by increases in leverage are likely to see this redistribution of wealth occur across claim holders in the firm.</li></ul> |               |               |                      |

# OBTAINING OPTION PRICING INPUTS - SOME REAL WORLD PROBLEMS

- ■ The examples that have been used to illustrate the use of option pricing theory to value equity have made some simplifying assumptions. Among them are the following:
  1. 1) There were **only two claim holders** in the firm - debt and equity.
  2. 2) There **is only one issue of debt** outstanding, and it can be retired at face value.
  3. 3) The debt has a **zero coupon** and no special features (convertibility, put clauses etc.)
  4. 4) The **value of the firm and the variance in that value can be estimated.**

# REAL WORLD APPROACHES TO VALUING EQUITY IN TROUBLED FIRMS: GETTING INPUTS

| Input                  | Estimation Process                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value of the Firm      | <ul> <li>• Cumulate market values of equity and debt (or)</li> <li>• Value the <u>assets in place</u> using FCFF and WACC (or)</li> <li>• Use cumulated market value of assets, if traded.</li> </ul>                                                                                                                                                                                                                                                                                                                                                                                        |
| Variance in Firm Value | <ul> <li>• If stocks and bonds are traded,<br/> <math display="block">\sigma^2_{\text{firm}} = w_e^2 \sigma_e^2 + w_d^2 \sigma_d^2 + 2 w_e w_d \rho_{\text{ed}} \sigma_e \sigma_d</math><br/>           where <math>\sigma_e^2</math> = variance in the stock price<br/> <math>w_e</math> = MV weight of Equity<br/> <math>\sigma_d^2</math> = the variance in the bond price      <math>w_d</math> = MV weight of debt</li> <li>• If not traded, use variances of similarly rated bonds.</li> <li>• Use average firm value variance from the industry in which company operates.</li> </ul> |
| Value of the Debt      | <ul> <li>• If the debt is short term, you can use only the face or book value of the debt.</li> <li>• If the debt is long term and coupon bearing, add the cumulated nominal value of these coupons to the face value of the debt.</li> </ul>                                                                                                                                                                                                                                                                                                                                                |
| Maturity of the Debt   | <ul> <li>• Face value weighted duration of bonds outstanding (or)</li> <li>• If not available, use weighted maturity</li> </ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

![](_page_78_Picture_5.jpeg)

# VALUING EQUITY AS AN OPTION - EUROTUNNEL IN EARLY 1998

- ▪ Eurotunnel has been a financial disaster since its opening
  - ▪ In 1997, Eurotunnel had earnings before interest and taxes of -£56 million and net income of -£685 million
  - ▪ At the end of 1997, its book value of equity was -£117 million

- ▪ It had £8,865 million in face value of debt outstanding

- - ▪ The weighted average duration of this debt was 10.93 years

| Debt Type  | Face Value | Duration    |
|------------|------------|-------------|
| Short term | 935        | 0.50        |
| 10 year    | 2435       | 6.7         |
| 20 year    | 3555       | 12.6        |
| Longer     | 1940       | 18.2        |
| Total      | £8,865 mil | 10.93 years |

# THE BASIC DCF VALUATION

- ▪ The value of the firm estimated using projected cashflows to the firm, discounted at the weighted average cost of capital was £2,312 million.
- ▪ This was based upon the following assumptions –
  - ▪ Revenues will grow 5% a year in perpetuity.
  - ▪ The COGS which is **currently 85% of revenues will drop to 65% of revenues in yr 5** and stay at that level.
  - ▪ Capital spending and depreciation **will grow 5% a year in perpetuity.**
  - ▪ There are no working capital requirements.
  - ▪ The debt ratio, which is **currently 95.35%, will drop to 70%** after year 5. The cost of debt is 10% in high growth period and 8% after that.
  - ▪ The beta for the stock **will be 1.10 for the next five years**, and drop to 0.8 after the next 5 years.
  - ▪ The long term bond rate is 6%.

# OTHER INPUTS

- ▪ The stock has been traded on the London Exchange, and the **annualized std deviation based upon  $\ln$  (prices) is 41%.**
- ▪ There are Eurotunnel bonds, that have been traded; the annualized std deviation in  $\ln(\text{price})$  for the bonds is 17%.
  - ▪ The correlation between stock price and bond price changes has been 0.5. The proportion of debt in the capital structure during the period (1992-1996) was 85%.
  - ▪ Annualized variance in firm value
  - ▪  $= (0.15)^2 (0.41)^2 + (0.85)^2 (0.17)^2 + 2 (0.15) (0.85)(0.5)(0.41)(0.17) = 0.0335$
- ▪ The 15-year bond rate is 6%. (I used a bond with a duration of roughly 11 years to match the life of my option)

# VALUING EUROTUNNEL EQUITY AND DEBT

- ▪ Inputs to Model
  - ▪ Value of the underlying asset =  $S$  = Value of the firm = £2,312 million
  - ▪ Exercise price =  $K$  = Face Value of outstanding debt = £8,865 million
  - ▪ Life of the option =  $t$  = Weighted average duration of debt = 10.93 years
  - ▪ Variance in the value of the underlying asset =  $s^2$  = Variance in firm value = 0.0335
  - ▪ Riskless rate =  $r$  = Treasury bond rate corresponding to option life = 6%
- ▪ Based upon these inputs, the Black-Scholes model provides the following value for the call:
  - ▪  $d_1 = -0.8337$                        $N(d_1) = 0.2023$
  - ▪  $d_2 = -1.4392$                        $N(d_2) = 0.0751$
- ▪ Value of the call =  $2312 (0.2023) - 8,865 \exp^{(-0.06)(10.93)} (0.0751) = \$122 \text{ million}$
- ▪ Appropriate interest rate on debt =  $(8865/2190)(1/10.93) - 1 = 13.65\%$

# IN CLOSING...

- ▪ There are **real options everywhere**.
- ▪ **Most of them have no significant economic value** because there is no exclusivity associated with using them.
- ▪ When options have significant economic value, the inputs needed to value them in a binomial model can be used in more traditional approaches (decision trees) to yield equivalent value.
- ▪ The real value from real options lies in
  - ▪ Recognizing that **building in flexibility and escape hatches** into large decisions has value
  - ▪ Insights we get on understanding how and why companies behave the way they do **in investment analysis and capital structure choices**.