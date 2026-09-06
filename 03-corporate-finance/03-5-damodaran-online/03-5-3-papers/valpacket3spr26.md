---
title: "Valpacket3Spr26"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket3spr26.pdf
---

---

# **VALUATION: PACKET 3 REAL OPTIONS, ACQUISITION VALUATION AND VALUE ENHANCEMENT**

Updated: January 2026

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

- ▪ Interest rate on debt =  $(\$ 80 / \$24.06)^{1/10} - 1 = 12.77\%$

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

# **ACQUIRERS ANONYMOUS: SEVEN STEPS BACK TO SOBRIETY...**

Aswath Damodaran

# GREAT FOR TARGET COMPANIES BUT NOT FOR ACQUIRING COMPANY STOCKHOLDERS . . .

*Cumulative Returns: Target and Bidder firms in Public Acquisitions*

![](_page_85_Figure_13.jpeg)

# AND THE LONG-TERM FOLLOW UP IS NOT POSITIVE EITHER..

- ▪ Managers often argue that the market is unable to see the long term benefits of mergers that they can see at the time of the deal. If they are right, mergers should create long term benefits to acquiring firms.
- ▪ The evidence does not support this hypothesis:
  - ▪ McKinsey and Co. has examined acquisition programs at companies on
    - 1. Did the return on capital invested in acquisitions exceed the cost of capital?
    - 2. Did the acquisitions help the parent companies outperform the competition?
    - 3. Half of all programs failed one test, and a quarter failed both.
  - ▪ **Synergy is elusive.** KPMG in a more recent study of global acquisitions concludes that most mergers (>80%) fail - the merged companies do worse than their peer group.
  - ▪ **Regret is common:** A large number of acquisitions that are reversed within fairly short time periods. About 20% of the acquisitions made between 1982 and 1986 were divested by 1988. In studies that have tracked acquisitions for longer time periods (ten years or more) the divestiture rate of acquisitions rises to almost 50%.

# THE DISEASE IS SPREADING: INDIAN FIRMS ACQUIRING US TARGETS — 1999 - 2005

![](_page_87_Figure_12.jpeg)

# **GROWING THROUGH ACQUISITIONS IS A “LOSER’S GAME”**

- ▪ Firms that grow through acquisitions have generally had far more trouble creating value than firms that grow through internal investments.
- ▪ In general, acquiring firms tend to
  - ▪ Pay too much for target firms
  - ▪ Over estimate the value of “synergy” and “control”
  - ▪ Have a difficult time delivering the promised benefits
- ▪ Worse still, there seems to be very little learning built into the process. The same mistakes are made over and over again, often by the same firms with the same advisors.
- ▪ **Conclusion: There is something structurally wrong with the process for acquisitions which is feeding into the mistakes.**

# THE SEVEN SINS IN ACQUISITIONS...

1. 1. **Risk Transference:** Attributing acquiring company risk characteristics to the target firm.
2. 2. **Debt subsidies:** Subsiding target firm stockholders for the strengths of the acquiring firm.
3. 3. **Auto-pilot Control:** The “20% control premium” and other myth...
4. 4. **Elusive Synergy:** Misidentifying and mis-valuing synergy.
5. 5. **Its all relative:** Transaction multiples, exit multiples...
6. 6. **Verdict first, trial afterwards:** Price first, valuation to follow
7. 7. **It's not my fault:** Holding no one responsible for delivering results.

# TESTING SHEET

| Test                              | Passed/Failed | Rationalization |
|-----------------------------------|---------------|-----------------|
| Risk transference                 |               |                 |
| Debt subsidies                    |               |                 |
| Control premium                   |               |                 |
| The value of synergy              |               |                 |
| Comparables and Exit Multiples    |               |                 |
| Bias                              |               |                 |
| A successful acquisition strategy |               |                 |

# LET'S START WITH A TARGET FIRM

- The target firm has the following income statement:

|                                                                  | Next Year |
|------------------------------------------------------------------|-----------|
| Revenues                                                         | \$ 100.00 |
| Operating Expenses<br>(includes depreciation of \$20<br>million) | \$ 80.00  |
| Pre-tax Operating Income                                         | \$ 20.00  |
| Taxes                                                            | \$ 8.00   |
| After-tax Operating Income                                       | \$ 12.00  |

- Assume that this firm will generate this operating income forever (with no growth) and that the cost of equity for this firm is 20%. The firm has no debt outstanding. What is the value of this firm?

# TEST 1: RISK TRANSFERENCE...

- ■ Assume that as an acquiring firm, you are in a much safer business and have a cost of equity of 10%. What is the value of the target firm to you?
  - a. \$60 million
  - b. \$90 million
  - c. \$120 million
  - d. Other

# LESSON 1: DON'T TRANSFER YOUR RISK CHARACTERISTICS TO THE TARGET FIRM

- ■ Let's start with a basic capital budgeting principle, which is often ignored: **The discount rate used for an investment should reflect the risk of the investment and not the risk characteristics of the investor who raised the funds.**
  - ■ Risky businesses **cannot become safe** just because the buyer of these businesses is in a safe business.
  - ■ The right cost of equity to use in valuation is the **one that reflects the risk in equity in the target firm.**

## TEST 2: CHEAP DEBT?

- ■ Assume as an acquirer that you have both **excess debt capacity** (because you have not chosen to borrow as much as you could have, given your assets) and **access to cheap debt**.
- ■ You **plan to borrow money at 4%** (in after-tax terms) and that you plan to **fund half the acquisition with debt**. How much would you be willing to pay for the target firm?

## **LESSON 2: RENDER UNTO THE TARGET FIRM THAT WHICH IS THE TARGET FIRM'S BUT NOT A PENNY MORE..**

- ▪ As an acquiring firm, it is entirely possible that you can borrow much more than the target firm can on its own and at a much lower rate.
- ▪ If you build these characteristics into the valuation of the target firm, you are essentially transferring wealth from your firm's stockholder to the target firm's stockholders.
- ▪ When valuing a target firm, use a cost of capital that reflects the debt capacity and the cost of debt that would apply to the firm.

# TEST 3: CONTROL PREMIUMS

- ■ Assume that you are now told that it is conventional to pay a 20% premium for control in acquisitions.
- ■ That premium is justified by pointing to historical studies that show that this is what acquirers pay for control, i.e., pay roughly a 20% premium over the market price.
  - a. How much would you be willing to pay for the target firm?
  - b. Assuming that you are paying a control premium, how would you justify it?

# LESSON 3: BEWARE OF RULES OF THUMB...

- ▪ Valuation is cluttered with rules of thumb. After painstakingly valuing a target firm, using your best estimates, you will be often be told that
  - ▪ It is common practice to add arbitrary premiums for brand name, quality of management, control etc...
  - ▪ These premiums will be often be backed up by data, studies and services. What they will not reveal is the enormous sampling bias in the studies and the standard errors in the estimates.
  - ▪ If you have done your valuation right, those premiums should already be incorporated in your estimated value. Paying a premium will be double counting.

# TEST 4: SYNERGY....

1. 1. Assume that you are told that the combined firm will be less risky than the two individual firms and that it should have a lower cost of capital (and a higher value). Is this likely?
   1. a. Yes
   2. b. No
2. 2. Assume now that you are told that there are potential growth and cost savings synergies in the acquisition. Would that constitute value added?
   1. a. Yes
   2. b. No
3. 3. Should you pay this as a premium?
   1. a. Yes
   2. b. No

# THE VALUE OF SYNERGY

![](_page_99_Diagram_133.jpeg)

# VALUING SYNERGY

- ▪ (1) the firms involved in the **merger are valued independently**, by discounting expected cash flows to each firm at the weighted average cost of capital for that firm.
- ▪ (2) the **value of the combined firm, with no synergy**, is obtained by adding the values obtained for each firm in the first step.
- ▪ (3) The **effects of synergy are built into expected growth rates and cashflows**, and the combined firm is re-valued with synergy.
  - ▪ Value of Synergy = Value of the combined firm, with synergy - Value of the combined firm, without synergy

# SYNERGY - EXAMPLE 1

## HIGHER GROWTH AND COST SAVINGS

|                               | P&G        | Gillette   | Piglet: No Synergy | Piglet: Synergy |                                                    |
|-------------------------------|------------|------------|--------------------|-----------------|----------------------------------------------------|
| Free Cashflow to Equity       | \$5,864.74 | \$1,547.50 | \$7,412.24         | \$7,569.73      | Annual operating expenses reduced by \$250 million |
| Growth rate for first 5 years | 12%        | 10%        | 11.58%             | 12.50%          | Slightly higher growth rate                        |
| Growth rate after five years  | 4%         | 4%         | 4.00%              | 4.00%           |                                                    |
| Beta                          | 0.90       | 0.80       | 0.88               | 0.88            |                                                    |
| Cost of Equity                | 7.90%      | 7.50%      | 7.81%              | 7.81%           | Value of synergy                                   |
| Value of Equity               | \$221,292  | \$59,878   | \$281,170          | \$298,355       | <b>\$17,185</b>                                    |

## **SYNERGY: EXAMPLE 2**

### **TAX BENEFITS?**

- ▪ Assume that you are Best Buy, the electronics retailer, and that you would like to enter the hardware component of the market. You have been approached by investment bankers for Zenith, which while still a recognized brand name, is on its last legs financially. The firm has net operating losses of \$ 2 billion. If your tax rate is 36%, estimate the tax benefits from this acquisition.
- ▪ If Best Buy had only \$500 million in taxable income, how would you compute the tax benefits?
- ▪ If the market value of Zenith is \$800 million, would you pay this tax benefit as a premium on the market value?

# LESSON 4: DON'T PAY FOR BUZZ WORDS

1. 1. You have to value synergy, before you decide how much to pay (not after): Synergy will be the buzzword that explains away the premium that you are paying.
2. 2. To value synergy, you need specifics: Before you value synergy, you need to be specific about what synergies you see in a merger and where they will show up in a valuation.
3. 3. Don't mistake control for synergy: If the benefits can be generated by just one of the two entities in the merger, it is not synergy.
4. 4. Negotiate for your fair share: As the acquiring firm, you should negotiate for your share of the synergy, not pay it all off as a premium.

# TEST 5: COMPARABLES AND EXIT MULTIPLES

- ▪ Now assume that you are told that an analysis of other acquisitions reveals that acquirers have been willing to pay 5 times EBIT.. Given that your target firm has EBIT of \$ 20 million, would you be willing to pay \$ 100 million for the acquisition?
- ▪ What if I estimate the terminal value using an exit multiple of 5 times EBIT?
- ▪ As an additional input, your investment banker tells you that the acquisition is accretive. (Your PE ratio is 20 whereas the PE ratio of the target is only 10... Therefore, you will get a jump in earnings per share after the acquisition...)

# BIASED SAMPLES = POOR RESULTS

- ▪ **Biased samples yield biased results.** Basing what you pay on what other acquirers have paid is a recipe for disaster. After all, we know that acquirer, on average, pay too much for acquisitions. By matching their prices, we risk replicating their mistakes.
- ▪ Even when **we use the pricing metrics of other firms in the sector**, we may be basing the prices we pay on firms that are not truly comparable.
- ▪ When **we use exit multiples**, we are assuming that what the market is paying for comparable companies today is what it will continue to pay in the future.

# LESSON 5: IF YOU ARE GOING TO PRICE A TARGET FIRM, DO IT RIGHT..

- ▪ **Pick your game:** If you are acquiring other companies not for the cash flows but because you think that you can sell them to someone else at a higher price, it is perfectly okay to play the pricing game. If you are acquiring a firm for its cash flows, you have to play the value game.
- ▪ **Don't get distracted:** If you are playing the pricing game, dispense with the DCF and do an honest pricing. If you are playing the value game, stop looking at what other people are paying.
- ▪ **To do an honest pricing**, you have to be unbiased in your choice of multiple and comparable firms, and control for differences between your firm & the peer group.

# **TEST 6: THE CEO REALLY WANTS TO DO THIS... OR THERE ARE COMPETITIVE PRESSURES...**

1. 1. Now assume that you know that the CEO of the acquiring firm really, really wants to do this acquisition and that the investment bankers on both sides have produced fairness opinions that indicate that the firm is worth \$ 150 million. Would you be willing to go along?
   1. a) Yes
   2. b) No
2. 2. Now assume that you are told that your competitors are all doing acquisitions and that if you don't do them, you will be at a disadvantage? Would you be willing to go along?
   1. a) Yes
   2. b) No

# CEO EGOS AND OVERCONFIDENCE: THE DIRTY SECRET IN MERGERS

- ■ **The Deal Rules:** The premiums paid on acquisitions often have nothing to do with synergy, control or strategic considerations (though they may be provided as the reasons). They are just what you have to pay to get the deals done, because management really, really wants it done.
- ■ **The Ego Problem:** They may just reflect the egos of the CEOs of the acquiring firms. There is evidence that “over confident” CEOs are more likely to make acquisitions and that they leave a trail across the firms that they run.

# DEFENSIVE MERGERS: SIGNS OF A DEEPER ROT?

- ■ **Me-tooism:** Pre-emptive or defensive acquisitions, where you over pay, either because everyone else is overpaying or because you are afraid that you will be left behind if you don't acquire are dangerous.
- ■ **Weak businesses?** If the only way you can stay competitive in a business is by making bad investments, it may be best to think about shrinking or even getting out of the business.
- ■ **There is no glory in survival**, for the sake of survival. Corporate sustainability, as a corporate objective, is not just a joke, but an expensive one.

# LESSON 6: DON'T LET EGOS OR INVESTMENT BANKERS GET THE BETTER OF COMMON SENSE...

- ■ If you **define your objective in a bidding war as winning the auction** at any cost, you will win. But beware the winner's curse!
- ■ The **premiums paid on acquisitions often have nothing to do with synergy, control or strategic considerations**. They may just **reflect** the egos of the CEOs of the acquiring firms. There is evidence that “overconfident” CEOs are more likely to make acquisitions and that they leave a trail across the firms that they run.
- ■ Pre-emptive or defensive acquisitions, where you over pay, either because everyone else is overpaying or because you are afraid that you will be left behind if you don't acquire are dangerous. If the only way you can stay competitive in a business is by making bad investments, it may be best to think about getting out of the business.

# TEST 7: WHEN DEALS FALL APART..

- ■ When deals fall apart, as many do, there seems to be little or no accountability in the system, and the larger the deal, the less accountability there is for mistakes.
- ■ Breaking it down:
  - ■ The **managers** who initiate these bad deals seem to face few consequences and often move up the ranks.
  - ■ The **boards** that okay these deals protect themselves by claiming that the did due diligence and listened to experts.
  - ■ The **bankers** keep their fees, arguing that their missed forecasts were just mistakes.

# TO ILLUSTRATE: A BAD DEAL IS MADE, AND JUSTIFIED BY ACCOUNTANTS & BANKERS!

![](_page_112_Figure_9.jpeg)

# THE CEO STEPS IN... AND DIGS A HOLE...

- ■ Leo Apotheker was the CEO of HP at the time of the deal, brought in to replace Mark Hurd, the previous CEO who was forced to resign because of a “sex” scandal.
- ■ In the face of almost universal feeling that HP had paid too much for Autonomy, Mr. Apotheker addressing a conference at the time of the deal: “We have a pretty rigorous process inside H.P. that we follow for all our acquisitions, which is a D.C.F.-based model,” he said, in a reference to discounted cash flow, a standard valuation methodology. “And we try to take a very conservative view.”
- ■ Apotheker added, “Just to make sure everybody understands, Autonomy will be, on Day 1, accretive to H.P..... “Just take it from us. We did that analysis at great length, in great detail, and we feel that we paid a very fair price for Autonomy. And it will give a great return to our shareholders.

# A YEAR LATER... HP ADMITS A MISTAKE...AND EXPLAINS IT...

![](_page_114_Figure_6.jpeg)

# A MEASURED ASSESSMENT: IS IT HOPELESS?

- ▪ The odds seem to be clearly weighted against success in acquisitions. If you were to create a strategy to grow, based upon acquisitions, which of the following offers your best chance of success?

| <b>This</b>    | <b>Or this</b>   |
|----------------|------------------|
| Sole Bidder    | Bidding War      |
| Public target  | Private target   |
| Pay with cash  | Pay with stock   |
| Small target   | Large target     |
| Cost synergies | Growth synergies |

# BETTER TO LOSE A BIDDING WAR THAN TO WIN ONE...

![](_page_116_Figure_17.jpeg)

(a) Market-adjusted CARs

Aswath Damodaram Malmendier, Moretti & Peters (2011)

# BETTER OFF BUYING SMALL RATHER THAN LARGE TARGETS... WITH CASH RATHER THAN STOCK

![](_page_117_Figure_10.jpeg)

# AND FOCUSING ON PRIVATE FIRMS AND SUBSIDIARIES, RATHER THAN PUBLIC FIRMS...

![](_page_118_Figure_10.jpeg)

# GROWTH VS COST SYNERGIES

## Top-line trouble: 70 percent of mergers failed to achieve expected revenue synergies

Mergers achieving stated percentage of expected revenue synergies, percent  $N = 77$ 

![](_page_119_Figure_21.jpeg)

Typical sources of estimation error

- • Ignoring or underestimating customer losses (typically 2% to 5%) that result from the integration
- • Assuming growth or share targets out of line with overall market growth and competitive dynamics (no “outside view” calibration)

Source: McKinsey (2002) Postmerger Management Practice client survey; client case studies

## timation is better, but there arging in the errors

1 percentage of errent  $N = 92$ 

![](_page_119_Figure_27.jpeg)

timation error

e-time costs

from noncomparable situations

management estimates against precedent

timates in bottom-up analysis (e.g., location-of overlaps)

Postmerger Management Practice client survey; client case studies

# THE BOTTOM LINE: FOR ACQUISITIONS TO CREATE VALUE, YOU HAVE TO STAY DISCIPLINED..

- ▪ If you have a successful acquisition strategy, stay focused on that strategy. Don't let size or hubris drive you to “expand” the strategy.
- ▪ Realistic plans for delivering synergy and control have to be put in place before the merger is completed. By realistic, we have to mean that the magnitude of the benefits have to be reachable and not pipe dreams and that the time frame should reflect the reality that it takes a while for two organizations to work as one.
- ▪ The best thing to do in a bidding war is to drop out.
- ▪ Someone (preferably the person pushing hardest for the merger) should be held to account for delivering the benefits.
- ▪ The compensation for investment bankers and others involved in the deal should be tied to how well the deal works rather than for getting the deal done.

# **VALUE ENHANCEMENT AND THE EXPECTED VALUE OF CONTROL: BACK TO BASICS**

Aswath Damodaran

# PRICE ENHANCEMENT VERSUS VALUE ENHANCEMENT

*The market gives...*

![](_page_122_Figure_16.jpeg)

*And takes away....*

![](_page_122_Figure_18.jpeg)

# THE PATHS TO VALUE CREATION

- ▪ Using the DCF framework, there are four basic ways in which the value of a firm can be enhanced:
  - ▪ The **cash flows from existing assets** to the firm can be increased, by either
    - ▪ increasing after-tax earnings from assets in place or
    - ▪ reducing reinvestment needs (net capital expenditures or working capital)
  - ▪ The **value from growth** in these cash flows can be increased by either
    - ▪ Reinvesting more and increasing growth in good businesses
    - ▪ Reinvesting less or even divesting in bad businesses
  - ▪ The **length of the high growth period** can be extended to allow for more years of high growth.
  - ▪ The cost of capital can be reduced by
    - ▪ Reducing the operating risk in investments/assets
    - ▪ Changing the financial mix
    - ▪ Changing the financing composition

# VALUE CREATION 1: INCREASE CASH FLOWS FROM ASSETS IN PLACE

![](_page_124_Diagram_18.jpeg)

# DIVEST, ABANDON OR HOLD ON: THE MATH!

- ■ The conventional wisdom, when you are put in charge of a troubled firm, is to sell or abandon the worst-performing assets, usually ones that earn less than the cost of capital.
- ■ Every asset/business that a company owns has three values:
  - ■ Continuation value: the value of the expected cash flows from continuing to own and operate the asset
  - ■ Abandonment value: the salvage value of the asset or assets in the business
  - ■ Divestiture value: the value that the best buyer will pay for the asset or business.
- ■ For value enhancement, you pick the highest of the three values, and ironically, the ones that you may most benefit from divesting are your best-regarded, rather than your worst performing, assets.

# VALUE CREATION 2: INCREASE VALUE FROM EXPECTED GROWTH

Are you in a business where you can find more investments that generate returns that exceed the cost of capital?

![](_page_126_Diagram_13.jpeg)

| Region                    | # firms | ROE     | COE    | % of firms with ROE>COE | ROIC    | WACC  | % of firms with ROIC>WACC | % of firms with ROIC-WACC>5% | % of firms with ROIC-WACC<5% |
|---------------------------|---------|---------|--------|-------------------------|---------|-------|---------------------------|------------------------------|------------------------------|
| Africa and Middle East    | 2,423   | 7.55%   | 10.98% | 32.03%                  | 4.77%   | 9.33% | 25.05%                    | 16.59%                       | 83.41%                       |
| Australia & NZ            | 1,798   | -12.08% | 8.51%  | 18.19%                  | -11.59% | 8.36% | 19.24%                    | 13.68%                       | 86.32%                       |
| Canada                    | 2,791   | -20.66% | 8.64%  | 11.64%                  | -18.59% | 8.41% | 12.54%                    | 8.10%                        | 91.90%                       |
| China                     | 7,504   | 4.34%   | 10.07% | 23.87%                  | 3.36%   | 8.94% | 25.49%                    | 15.27%                       | 84.73%                       |
| EU & Environs             | 5,925   | 6.73%   | 9.83%  | 33.96%                  | 5.48%   | 8.59% | 33.59%                    | 24.76%                       | 75.24%                       |
| Eastern Europe & Russia   | 325     | 10.17%  | 10.38% | 34.46%                  | 4.32%   | 9.17% | 26.46%                    | 16.31%                       | 83.69%                       |
| India                     | 4,446   | 8.32%   | 11.12% | 34.14%                  | 5.61%   | 9.90% | 29.94%                    | 19.50%                       | 80.50%                       |
| Japan                     | 4,020   | 7.14%   | 10.05% | 33.23%                  | 7.15%   | 8.62% | 41.32%                    | 26.87%                       | 73.13%                       |
| Latin America & Caribbean | 984     | 9.28%   | 12.30% | 35.37%                  | 7.37%   | 9.76% | 35.98%                    | 24.19%                       | 75.81%                       |
| Small Asia                | 9,876   | 5.19%   | 10.86% | 25.65%                  | 3.81%   | 9.37% | 23.78%                    | 14.14%                       | 85.86%                       |
| UK                        | 1,125   | 1.47%   | 9.71%  | 29.16%                  | 4.76%   | 8.74% | 37.16%                    | 28.80%                       | 71.20%                       |
| United States             | 6,481   | 2.64%   | 8.80%  | 26.68%                  | 0.05%   | 7.91% | 23.59%                    | 17.74%                       | 82.26%                       |
| Global                    | 47,698  | 4.93%   | 9.92%  | 27.54%                  | 3.73%   | 8.68% | 27.12%                    | 18.02%                       | 81.98%                       |

# VALUE CREATING GROWTH... EVALUATING THE ALTERNATIVES..

## Modes of organic growth vary in value creation intensity—consumer goods industry

![](_page_127_Figure_12.jpeg)

# VALUE CREATION 3: BUILDING COMPETITIVE ADVANTAGES: INCREASE LENGTH OF THE GROWTH PERIOD

- ▪ Value comes from earning returns that exceed your cost of capital, and those excess returns, in turn, come from competitive advantages.
- ▪ Stronger competitive advantages (moats) increase how long you can add value from growth.

|                |         | Type of competitive advantage (moat) |                    |                  |                 |                  |
|----------------|---------|--------------------------------------|--------------------|------------------|-----------------|------------------|
|                |         | Brand Name                           | Switching Costs    | Network Benefits | Cost Advantages | Legal Protection |
| Moat Width     | Wide    | Top brand                            | Infinite           | Global           | Permanent       | Full             |
|                | Narrow  | Name brand                           | High               | Local            | Temporary       | Partial          |
|                | No Moat | Generic                              | None               | None             | None            | None             |
| Place in story |         | Margins                              | Customer Retention | Market Share     | Profit margins  | Pricing Power    |

# MEASURING THE MOAT

- ■ The only financial measure of the moat is the difference between the return you earn on existing assets and the cost of capital. Unfortunately, there are three problems;
  - ■ The return on equity (and capital) is an accounting number, and may not be reflective of the true return.
  - ■ It can be volatile, shifting over time.
  - ■ It is for past investments, not future ones.
- ■ The truth is that moat reading remains subjective, with a multitude of factors going into it.

# VALUE CREATION 4: REDUCE COST OF CAPITAL

## Change financing mix

The pluses (tax benefits) and minuses (bankruptcy cost) of debt can cause the cost of capital to change with debt mix.

## Match debt to assets

Mismatching debt to assets can increase default risk, and reducing that mismatch can lower the cost of debt & capital.

$$\text{Cost of Capital} = \text{Cost of equity} \times (\text{Equity}/(\text{Debt} + \text{Equity})) + \text{Cost of debt} (1 - \text{marginal tax rate}) \times (\text{Debt}/(\text{Debt} + \text{Equity}))$$

## Less Discretionary

Making your products/services less discretionary can reduce your market risk (unlevered beta) and lower your cost of equity.

## Lower operating leverage

Making your cost structure more flexible will make earnings less volatile, and reduce market risk (unlevered beta) and cost of equity.

# MYTH: BORROWING MONEY ALWAYS LOWERS YOUR COST OF CAPITAL

![](_page_131_Diagram_11.jpeg)

*The trade off: As you use more debt, you replace more expensive equity with cheaper debt but you also increase the costs of equity and debt. The net effect will determine whether the cost of capital will increase, decrease or be unchanged as debt ratio changes.*

# Changing Value

## 2.1: Increase value from growth (by growing less)

If you are in a bad business, where you earn less than your cost of capital, reinvest & grow less.

### Current Cashflows

These are the cash flows from existing investments, net of any reinvestment needed to sustain future growth. They can be computed before debt cashflows (to the firm) or after debt cashflows (to equity investors).

### 1. Increase current cash flows

Increase cash flows from existing assets, by redeploying poorly utilized assets, cutting costs, reducing taxes paid or managing working capital better.

### Growth from new investments

Growth created by making new investments; function of amount and quality of investments

### Efficiency Growth

Growth generated by using existing assets better

### 2.2: Increase value from growth (by growing more)

If you are in a good business, where you earn more than your cost of capital, reinvest & grow more.

### Expected Growth during high growth period

### Length of the high growth period

Since value creating growth requires excess returns, this is a function of

- - Magnitude of competitive advantages
- - Sustainability of competitive advantages

### Cost of financing (debt or capital) to apply to discounting cashflows

Determined by

- - Operating risk of the company
- - Default risk of the company
- - Mix of debt and equity used in financing

### Terminal Value of firm (equity)

Stable growth firm, with no or very limited excess returns

### 3. Develop & grow competitive advantages

If you have no competitive advantages, develop some, and if you do, build on them.

### 4. Reduce your cost of capital

Reduce your overall cost of capital by

1. Changing mix of debt and equity
2. Matching debt to your assets
3. Reducing fixed costs
4. Making your products/services less discretionary

**Current Cashflow to Firm** EBIT(1-t) : 1414 - Nt CpX 831 - Chg WC - 19 = FCFF 602 Reinvestment Rate = 812/1414 =57.42%

**Expected Growth in EBIT (1-t)** .5742\*.1993=.1144 **11.44%**

Stable Growth g = 3.41%; Beta = 1.00; Debt Ratio= 20% Cost of capital = 6.62% ROC= 6.62%; Tax rate=35% Reinvestment Rate=51.54%

Terminal Value10= 1717/(.0662-.0341) = 53546

**Cost of Equity 8.77%**

**Cost of Debt** (3.41%+..35%)(1-.3654) = 2.39%

**Weights** E = 98.6% D = 1.4%

Cost of Capital (WACC) = 8.77% (0.986) + 2.39% (0.014) = 8.68%

Op. Assets 31,615 + Cash: 3,018 - Debt 558 - Pension Lian 305 - Minor. Int. 55 =Equity 34,656 -Options 180 Value/Share106.12

> **Riskfree Rate**: Euro riskfree rate = 3.41%

+ **Beta**  1.26 **X** Unlevered Beta for Sectors: 1.25

**Risk Premium** 4.25%

> Mature risk premium 4%

Country Equity Prem 0.25%

# SAP: Status Quo

Reinvestment Rate 57.42%

Return on Capital 19.93%

Avg Reinvestment rate = 36.94%

> On May 5, 2005, SAP was trading at 122 Euros/share

First 5 years Growth decreases gradually to 3.41%

> Debt ratio increases to 20% Beta decreases to 1.00

| Year        | 1     | 2     | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    |
|-------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| EBIT        | 2,483 | 2,767 | 3,083 | 3,436 | 3,829 | 4,206 | 4,552 | 4,854 | 5,097 | 5,271 |
| EBIT(1-t)   | 1,576 | 1,756 | 1,957 | 2,181 | 2,430 | 2,669 | 2,889 | 3,080 | 3,235 | 3,345 |
| - Reinvestm | 905   | 1,008 | 1,124 | 1,252 | 1,395 | 1,501 | 1,591 | 1,660 | 1,705 | 1,724 |
| = FCFF      | 671   | 748   | 833   | 929   | 1,035 | 1,168 | 1,298 | 1,420 | 1,530 | 1,621 |

# SAP : OPTIMAL CAPITAL STRUCTURE

| Debt Ratio | Beta  | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC   | Firm Value (G) |
|------------|-------|----------------|-------------|-----------------------|----------|--------------------------|--------|----------------|
| 0%         | 1.25  | 8.72%          | AAA         | 3.76%                 | 36.54%   | 2.39%                    | 8.72%  | \$39,088       |
| 10%        | 1.34  | 9.09%          | AAA         | 3.76%                 | 36.54%   | 2.39%                    | 8.42%  | \$41,480       |
| 20%        | 1.45  | 9.56%          | A           | 4.26%                 | 36.54%   | 2.70%                    | 8.19%  | \$43,567       |
| 30%        | 1.59  | 10.16%         | A-          | 4.41%                 | 36.54%   | 2.80%                    | 7.95%  | \$45,900       |
| 40%        | 1.78  | 10.96%         | CCC         | 11.41%                | 36.54%   | 7.24%                    | 9.47%  | \$34,043       |
| 50%        | 2.22  | 12.85%         | C           | 15.41%                | 22.08%   | 12.01%                   | 12.43% | \$22,444       |
| 60%        | 2.78  | 15.21%         | C           | 15.41%                | 18.40%   | 12.58%                   | 13.63% | \$19,650       |
| 70%        | 3.70  | 19.15%         | C           | 15.41%                | 15.77%   | 12.98%                   | 14.83% | \$17,444       |
| 80%        | 5.55  | 27.01%         | C           | 15.41%                | 13.80%   | 13.28%                   | 16.03% | \$15,658       |
| 90%        | 11.11 | 50.62%         | C           | 15.41%                | 12.26%   | 13.52%                   | 17.23% | \$14,181       |

**Current Cashflow to Firm**

EBIT(1-t) : 1414

- Nt CpX 831

- Chg WC - 19

= FCFF 602

Reinvestment Rate = 812/1414

=57.42%

**Expected Growth** 

**in EBIT (1-t)**

.70\*.1993=.1144

**13.99%**

Stable Growth

g = 3.41%; Beta = 1.00;

Debt Ratio= 30%

Cost of capital = 6.27%

ROC= 6.27%; Tax rate=35%

Reinvestment Rate=54.38%

Terminal Value10= 1898/(.0627-.0341) = 66367

**Cost of Equity 10.57%**

**Cost of Debt** (3.41%+1.00%)(1-.3654) = 2.80%

**Weights** E = 70% D = 30%

Cost of Capital (WACC) = 10.57% (0.70) + 2.80% (0.30) = 8.24%

Op. Assets 38045

+ Cash: 3,018

- Debt 558

- Pension Lian 305

- Minor. Int. 55

=Equity 40157

-Options 180

Value/Share 126.51

**Riskfree Rate**:

Euro riskfree rate = 3.41%

+

**Beta**  1.59 **X**

**Risk Premium**

4.50%

Unlevered Beta for Sectors: 1.25

Mature risk premium 4%

Country Equity Prem 0.5%

# SAP: Restructured

Reinvestment Rate

70%

Return on Capital 19.93%

Term Yr

6402

4161

2263

1898

Avg Reinvestment rate = 36.94%

> On May 5, 2005, SAP was trading at 122 Euros/share

First 5 years gradually to 3.41% Year 1 2 3 4 5 6 7 8 9 10 EBIT 2,543 2,898 3,304 3,766 4,293 4,802 5,271 5,673 5,987 6,191 EBIT(1-t) 1,614 1,839 2,097 2,390 2,724 3,047 3,345 3,600 3,799 3,929 - Reinvest 1,130 1,288 1,468 1,673 1,907 2,011 2,074 2,089 2,052 1,965 = FCFF 484 552 629 717 817 1,036 1,271 1,512 1,747 1,963

Growth decreases

Reinvest more in Reinvest more in emerging markets emerging markets

Use more debt financing. Use more debt financing.

![](_page_136_Diagram_1.jpeg)

### Blockbuster: Status Quo

**Current Cashflow to Firm** EBIT(1-t) : 249 - Nt CpX 39 - Chg WC 4 = FCFF 206 Reinvestment Rate = 43/249 =17.32%

**Expected Growth in EBIT (1-t)** .1732\*.0620=.0107 **1.07%**

Stable Growth g = 3%; Beta = 1.00; Cost of capital = 6.76% ROC= 6.76%; Tax rate=35% Reinvestment Rate=44.37%

Terminal Value5= 156/(.0676-.03) = 4145

**Cost of Equity 8.50%**

**Cost of Debt** (4.10%+2%)(1-.35) = 3.97%

**Weights** E = 48.6% D = 51.4%

*Discount at* Cost of Capital (WACC) = 8.50% (.486) + 3.97% (0.514) = 6.17%

Op. Assets 3,840 + Cash: 330 - Debt 1847 =Equity 2323 -Options 0 Value/Share \$ 12.47

> **Riskfree Rate**: Riskfree rate = 4.10%

+ **Beta**  1.10 **X** **Risk Premium** 4%

Unlevered Beta for Sectors: 0.80

Firm's D/E Ratio: 21.35%

Mature risk premium 4%

Country Equity Prem 0%

# Blockbuster: Restructured

Reinvestment Rate 17.32%

Return on Capital 6.20%

> Term Yr 280 124 156

1 2 3 4 5

EBIT (1-t) \$252 \$255 \$258 \$264 \$272 - Reinvestment \$44 \$44 \$59 \$89 \$121 FCFF \$208 \$211 \$200 \$176 \$151

Aswath Damodaran **<sup>138</sup>**

# THE EXPECTED VALUE OF CONTROL

## The Value of Control

![](_page_138_Diagram_12.jpeg)

# WHY THE PROBABILITY OF MANAGEMENT CHANGING SHIFTS OVER TIME....

- ▪ **Corporate governance rules can change over time**, as new laws are passed. If the change gives stockholders more power, the likelihood of management changing will increase.
- ▪ **Activist investing ebbs and flows** with market movements (activist investors are more visible in down markets) and often in response to scandals.
- ▪ **Events such as hostile acquisitions** can make investors reassess the likelihood of change by reminding them of the power that they do possess.

# ESTIMATING THE PROBABILITY OF CHANGE

- ▪ You can estimate **the probability of management changes** by using historical data (on companies where change has occurred) and statistical techniques such as probits or logits.
- ▪ Empirically, the following seem to be related to the probability of management change:
  - ▪ **Stock price and earnings performance**, with forced turnover more likely in firms that have performed poorly relative to their peer group and to expectations.
  - ▪ **Structure of the board**, with forced CEO changes more likely to occur when the board is small, is composed of outsiders and when the CEO is not also the chairman of the board of directors.
  - ▪ **Ownership structure**, since forced CEO changes are more common in companies with high institutional and low insider holdings. They also seem to occur more frequently in firms that are more dependent upon equity markets for new capital.
  - ▪ **Industry structure**, with CEOs more likely to be replaced in competitive industries.

# MANIFESTATIONS OF THE VALUE OF CONTROL

1. 1. **Hostile acquisitions:** In hostile acquisitions which are motivated by control, the control premium should reflect the change in value that will come from changing management.
2. 2. **Valuing publicly traded firms:** The market price for every publicly traded firm should incorporate an expected value of control, as a function of the value of control and the probability of control changing.  
   Market value = Status quo value + (Optimal value – Status quo value)\*  
   Probability of management changing
3. 3. **Voting and non-voting shares:** The premium (if any) that you would pay for a voting share should increase with the expected value of control.
4. 4. **Minority Discounts in private companies:** The minority discount (attached to buying less than a controlling stake) in a private business should be increase with the expected value of control.

# 1. HOSTILE ACQUISITION: EXAMPLE

- ▪ In a hostile acquisition, you can **ensure management change after you take over the firm**. Consequently, you would be willing to pay up to the optimal value.
- ▪ As an example, Blockbuster was **trading at \$9.50 per share** in July 2005. The **optimal value per share that we estimated as \$ 12.47 per share**. Assuming that this is a reasonable estimate, you would be willing to pay up to \$2.97 as a premium in acquiring the shares.
- ▪ Issues to ponder:
  - ▪ Would you automatically pay \$2.97 as a premium per share? Why or why not?
  - ▪ What would your premium per share be if change will take three years to implement?

## 2. MARKET PRICES OF PUBLICLY TRADED COMPANIES: AN EXAMPLE

- **The market price per share at the time of the valuation (May 2005) was roughly \$9.50.**
  - Expected value per share = Status Quo Value + Probability of control changing \* (Optimal Value – Status Quo Value)
  - $\$ 9.50 = \$ 5.13 + \text{Probability of control changing}$  ( $\$12.47 - \$5.13$ )
- **The market is attaching a probability of 59.5% that management policies can be changed.** This was after Icahn's successful challenge of management. Prior to his arriving, the market price per share was \$8.20, yielding a probability of only 41.8% of management changing.

|                   | Value of Equity | Value per share   |
|-------------------|-----------------|-------------------|
| Status Quo        | \$ 955 million  | \$ 5.13 per share |
| Optimally managed | \$2,323 million | \$12.47 per share |

# VALUE OF STOCK IN A PUBLICLY TRADED FIRM

- ▪ When a firm is badly managed, the market still assesses the probability that it will be run better in the future and attaches a value of control to the stock price today:

$$\text{Value per share} = \frac{\text{Status Quo Value} + \text{Probability of control change (Optimal - Status Quo Value)}}{\text{Number of shares outstanding}}$$

- ▪ With voting shares and non-voting shares, a disproportionate share of the value of control will go to the voting shares. In the extreme scenario where non-voting shares are completely unprotected:

$$\text{Value per non- voting share} = \frac{\text{Status Quo Value}}{\# \text{ Voting Shares} + \# \text{ Non- voting shares}}$$

$$\text{Value per voting share} = \text{Value of non- voting share} + \frac{\text{Probability of control change (Optimal - Status Quo Value)}}{\# \text{ Voting Shares}}$$

### 3. VOTING AND NON-VOTING SHARES: AN EXAMPLE

- ▪ To value **voting and non-voting shares**, we will consider Embraer, the Brazilian aerospace company. As is typical of most Brazilian companies, the company has common (voting) shares and preferred (non-voting shares).
  - ▪ Status Quo Value = **12.5 billion \$R** for the equity;
  - ▪ Optimal Value = **14.7 billion \$R**, assuming that the firm would be more aggressive both in its use of debt and in its reinvestment policy.
- ▪ There are 242.5 million voting shares and 476.7 non-voting shares in the company and the probability of management change is relatively low. Assuming a probability of 20% that management will change, we estimated the value per non-voting and voting share:
  - ▪ **Value per non-voting share** = Status Quo Value/ (# voting shares + # non-voting shares) = 12,500/(242.5+476.7) = 17.38 \$R/ share
  - ▪ **Value per voting share** = Status Quo value/sh + Probability of management change \* (Optimal value – Status Quo Value) = 17.38 + 0.2\* (14,700-12,500)/242.5 = 19.19 \$R/share
- ▪ With our assumptions, **the voting shares should trade at a premium of 10.4% over the non-voting shares**.

## 4. MINORITY DISCOUNT: AN EXAMPLE

- ▪ Assume that you are valuing Kristin Kandy, a privately owned candy business for sale in a private transaction. You have estimated a **value of \$ 1.6 million for the equity in this firm**, assuming that the existing management of the firm continues into the future and a **value of \$ 2 million for the equity with new and more creative management in place**.
  - ▪ Value of 51% of the firm = 51% of optimal value =  $0.51 \times \$ 2$  million = \$1.02 million
  - ▪ Value of 49% of the firm = 49% of status quo value =  $0.49 \times \$1.6$  million = \$784,000
- ▪ Note that a **2% difference in ownership translates into a large difference in value** because one stake ensures control and the other does not.

# ALTERNATIVE APPROACHES TO VALUE ENHANCEMENT

- ▪ Maximize a variable that is correlated with the value of the firm. There are several choices for such a variable. It could be
  - ▪ an **accounting variable**, such as earnings or return on investment
  - ▪ a **marketing variable**, such as market share
  - ▪ a **cash flow variable**, such as cash flow return on investment (CFROI)
  - ▪ a **risk-adjusted cash flow variable**, such as Economic Value Added (EVA)
- ▪ The advantages of using these variables are that they
  - ▪ Are **often simpler and easier** to use than DCF value.
- ▪ The disadvantage is that the
  - ▪ **Simplicity comes at a cost**; these variables are not perfectly correlated with DCF value.

# ECONOMIC VALUE ADDED (EVA) AND CFROI

- ■ The **Economic Value Added (EVA)** is a measure of surplus value created on an investment.
  - ■ Define **the return on capital (ROC)** to be the “true” cash flow return on capital earned on an investment.
  - ■ Define **the cost of capital** as the weighted average of the costs of the different financing instruments used to finance the investment.
  - ■  $EVA = (\text{Return on Capital} - \text{Cost of Capital})$  (Capital Invested in Project)
- ■ The **CFROI** is a measure of the **cash flow return** made on capital
  - ■ It is computed as an IRR, based upon a base value of capital invested and the cash flow on that capital.

## THE BOTTOM LINE...

- ■ The value of a firm is not going to change just because you use a different metric for value. All approaches that are discounted cash flow approaches should yield the same value for a business, if they make consistent assumptions.
- ■ If there are differences in value from using different approaches, they must be attributable to differences in assumptions, either explicit or implicit, behind the valuation.

# A SIMPLE ILLUSTRATION

- ▪ Assume that you have a firm with a **book value value of capital of \$ 100 million**, on which it expects to generate a **return on capital of 15% in perpetuity with a cost of capital of 10%**.
- ▪ This firm is expected to make **additional investments of \$ 10 million at the beginning of each year for the next 5 years**. These investments are also expected to generate 15% as return on capital in perpetuity, with a cost of capital of 10%.
- ▪ After year 5, assume that
  - ▪ The earnings will grow 5% a year in perpetuity.
  - ▪ The firm will keep reinvesting back into the business but the return on capital on these new investments will be equal to the cost of capital (10%).

# FIRM VALUE USING EVA APPROACH

$$\begin{aligned}
 \text{Capital Invested in Assets in Place} &= \$ 100 \\
 \text{EVA from Assets in Place} &= (.15 - .10) (100) / .10 = \$ 50 \\
 &+ \text{PV of EVA from Investments in Year 1} = [(.15 - .10)(10) / .10] = \$ 5 \\
 &+ \text{PV of EVA from Investments in Year 2} = [(.15 - .10)(10) / .10] / 1.1 = \$ 4.55 \\
 &+ \text{PV of EVA from Investments in Year 3} = [(.15 - .10)(10) / .10] / 1.12 = \$ 4.13 \\
 &+ \text{PV of EVA from Investments in Year 4} = [(.15 - .10)(10) / .10] / 1.13 = \$ 3.76 \\
 &+ \text{PV of EVA from Investments in Year 5} = [(.15 - .10)(10) / .10] / 1.14 = \$ 3.42 \\
 \text{Value of Firm} &= \$ 170.85
 \end{aligned}$$

![](_page_151_Figure_72.jpeg)

# FIRM VALUE USING DCF VALUATION: ESTIMATING FCFF

|                               | Base<br>Year | 1        | 2        | 3        | 4        | 5        | Term.<br>Year |
|-------------------------------|--------------|----------|----------|----------|----------|----------|---------------|
| EBIT (1-t) : Assets in Place  | \$ 15.00     | \$ 15.00 | \$ 15.00 | \$ 15.00 | \$ 15.00 | \$ 15.00 |               |
| EBIT(1-t) : Investments- Yr 1 |              | \$ 1.50  | \$ 1.50  | \$ 1.50  | \$ 1.50  | \$ 1.50  |               |
| EBIT(1-t) : Investments- Yr 2 |              |          | \$ 1.50  | \$ 1.50  | \$ 1.50  | \$ 1.50  |               |
| EBIT(1-t): Investments - Yr 3 |              |          |          | \$ 1.50  | \$ 1.50  | \$ 1.50  |               |
| EBIT(1-t): Investments - Yr 4 |              |          |          |          | \$ 1.50  | \$ 1.50  |               |
| EBIT(1-t): Investments- Yr 5  |              |          |          |          |          | \$ 1.50  |               |
| Total EBIT(1-t)               |              | \$ 16.50 | \$ 18.00 | \$ 19.50 | \$ 21.00 | \$ 22.50 | \$ 23.63      |
| - Net Capital Expenditures    | \$10.00      | \$ 10.00 | \$ 10.00 | \$ 10.00 | \$ 10.00 | \$ 11.25 | \$ 11.81      |
| FCFF                          |              | \$ 6.50  | \$ 8.00  | \$ 9.50  | \$ 11.00 | \$ 11.25 | \$ 11.81      |

After year 5, the reinvestment rate is 50% = g/ ROC

# FIRM VALUE: PRESENT VALUE OF FCFF

| Year                 | 0              |          | 1    |      | 2    |      | 3    |      | 4    |       | 5         |       | Term Year |
|----------------------|----------------|----------|------|------|------|------|------|------|------|-------|-----------|-------|-----------|
|                      | FCFF           |          | \$   | 6.50 | \$   | 8.00 | \$   | 9.50 | \$   | 11.00 | \$        | 11.25 |           |
| PV of FCFF           | (\$10)         | \$       | 5.91 | \$   | 6.61 | \$   | 7.14 | \$   | 7.51 | \$    | 6.99      |       |           |
|                      | Terminal Value |          |      |      |      |      |      |      |      |       | \$ 236.25 |       |           |
| PV of Terminal Value |                |          |      |      |      |      |      |      |      |       | \$ 146.69 |       |           |
|                      | Value of Firm  | \$170.85 |      |      |      |      |      |      |      |       |           |       |           |

# IMPLICATIONS

- ■ **Growth, by itself, does not create value.** It is growth, with investment in excess return projects, that creates value.
  - ■ The growth of 5% a year after year 5 creates no additional value.
- ■ The “market value added” (MVA), which is defined to be the excess of market value over capital invested is a **function of the excess value created.**
  - ■ In the example above, the market value of \$ 170.85 million exceeds the book value of \$ 100 million, because the return on capital is 5% higher than the cost of capital.

# YEAR-BY-YEAR EVA CHANGES

- ▪ Firms are often evaluated based upon **year-to-year changes in EVA rather than the present value of EVA over time**.
  - ▪ The advantage of this comparison is that **it is simple** and does not require the making of forecasts about future earnings potential.
  - ▪ Another advantage is that it can be broken down by any unit - person, division etc., as long as one is willing to assign capital and allocate earnings across these same units.
- ▪ While it is simpler than DCF valuation, using year-by-year EVA changes comes at a cost. In particular, it is entirely possible that **a firm which focuses on increasing EVA on a year-to-year basis may end up being less valuable**.

# **GAMING THE SYSTEM: DELIVERING HIGH CURRENT EVA WHILE DESTROYING VALUE...**

- ▪ **The Growth trade off game:** Managers may give up valuable growth opportunities in the future to deliver higher EVA in the current year.
- ▪ **The Risk game:** Managers may be able to deliver a higher dollar EVA but in riskier businesses. The value of the business is the present value of EVA over time and the risk effect may dominate the increased EVA.
- ▪ **The Capital Invested game:** The key to delivering positive EVA is to make investments that do not show up as part of capital invested. That way, your operating income will increase while capital invested will decrease.

# **DELIVERING A HIGH EVA MAY NOT TRANSLATE INTO HIGHER STOCK PRICES...**

- ▪ The relationship **between EVA and Market Value Changes is more complicated** than the one between EVA and Firm Value.
- ▪ The market value of a firm reflects not only the Expected EVA of Assets in Place but also the Expected EVA from Future Projects
- ▪ To the extent that the **actual economic value added is smaller than the expected EVA** the market value can decrease even though the EVA is higher.

# WHEN FOCUSING ON YEAR-TO-YEAR EVA CHANGES HAS LEAST SIDE EFFECTS

**1. Most or all of the assets of the firm are already in place; i.e., very little or none of the value of the firm is expected to come from future growth.**

This minimizes the risk that increases in current EVA come at the expense of future EVA

**2. The leverage is stable and the cost of capital cannot be altered easily** by the investment decisions made by the firm.

This minimizes the risk that the higher EVA is accompanied by an increase in the cost of capital

**3. The firm is in a sector where investors anticipate little or not surplus returns; i.e., firms in this sector are expected to earn their cost of capital.**

- ■ This minimizes the risk that the increase in EVA is less than what the market expected it to be, leading to a drop in the market price.

# **DANTE MEETS DCF: VALUATION SINS AND REDEMPTION**

“It ain’t over till its over”  
Berra

Yogi

# DANTE MEETS INTRINSIC VALUATION: NINE LAYERS OF VALUATION HELL.. AND A BONUS LAYER..

![](_page_160_Diagram_42.jpeg)

# LAYER 1: BASE YEAR FIXATION...

![](_page_161_Picture_100.jpeg)

- You are valuing Exxon Mobil, using the financial statements of the firm from 2008. The following provides the key numbers:

| Revenues | \$477 billion |
|----------|---------------|
|----------|---------------|

| EBIT (1-t) | \$ 58 billion |
|------------|---------------|
|------------|---------------|

| Net Cap Ex | \$ 3 billion |
|------------|--------------|
|------------|--------------|

| Chg WC | \$ 1 billion |
|--------|--------------|
|--------|--------------|

| FCFF | \$ 54 billion |
|------|---------------|
|------|---------------|

- The cost of capital for the firm is 8% and you use a very conservative stable growth rate of 2% to value the firm. The market cap for the firm is \$373 billion and it has \$ 10 billion in debt outstanding.
  - a. How under or over valued is the equity in the firm?
  - b. Would you buy the stock based on this valuation? Why or why not?

# LAYER 2: TAXES AND VALUE

![](_page_162_Picture_178.jpeg)

- Assume that you have been asked to value a company and have been provided with the most recent year's financial statements:

| ▪ EBITDA         | 140 |
|------------------|-----|
| ▪ - DA           | 40  |
| ▪ EBIT           | 100 |
| ▪ Interest exp   | 20  |
| ▪ Taxable income | 80  |
| ▪ Taxes          | 32  |
| ▪ Net Income     | 48  |

Free Cash flow to firm  
 EBIT (1- tax rate)  
 -(Cap Ex – Depreciation)  
 - Change in non-cash WC  
 =FCFF

- Assume also that cash flows will be constant and that there is no growth in perpetuity.

What is the free cash flow to the firm?

- a. 88 million (Net income + Depreciation)
- b. 108 million (EBIT – taxes + Depreciation)
- c. 100 million (EBIT (1-tax rate)+ Depreciation)
- d. 60 million (EBIT (1- tax rate))
- e. 48 million (Net Income)
- f. 68 million (EBIT – Taxes)

# LAYER 3: HIGH GROWTH FOR HOW LONG...

![](_page_163_Picture_78.jpeg)

- ▪ Assume that you are valuing a young, high growth firm with real potential, just after its initial public offering. How long would you set your high growth period?
- ▪ < 5 years
- ▪ 5 years
- ▪ 10 years
- ▪ >10 years

Typically, the revenue growth rate of a newly public company outpaces its industry average for only about five years.

![](_page_163_Figure_81.jpeg)

Source: Andrew Metrick

The New York Times

# LAYER 4: THE COST OF CAPITAL

![](_page_164_Figure_189.jpeg)

- The cost of capital for Chippewa Technologies, a US technology firm with 20% of its revenues from Brazil, has been computed using the following inputs:

$$\text{Cost of equity} = \text{Riskfree Rate} + \text{Beta} + (\text{ERP}) + \text{Small firm premium} = 14\%$$

*Replaced current T.Bond rate of 3% with normalized rate of 5%*

*"Adjusted" Beta from Bloomberg*

*Both from Ibbotson data base, derived from 1926-2008 data  
ERP: Stocks - T.Bonds (Arithmetic average)  
Small firm: Small stocks - Overall market*

$$\text{Cost of capital} = \text{Cost of equity (Equity/ (Debt + Equity))} + \text{Cost of debt} + (1 - \text{tax rate}) + (\text{Debt/ (Debt + Equity)}) = 14\% + 3\% + (1 - .30) = 14\% = 8.05\%$$

*From above*

*Used market value of equity*

*Company is not rated and has no bonds. Used book interest rate = Int exp/ BV of debt*

*Used effective tax rate of 30%*

*To be conservative, counted all liabilities, other than equity, as debt and used book value.*

# THE CORRECT COST OF CAPITAL FOR CHIPPEWA

| <i>Input</i>                        | <i>What was used...</i>                   | <i>What should have been used...</i>                                                                            |
|-------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Riskfree Rate                       | Corrected treasury bond rate = 5%         | Actual treasury bond rate = 3%                                                                                  |
| Beta                                | Bloomberg adjusted beta = 1.20            | Sector average adjusted beta = 1.60<br>(Based on small cap companies in sector)                                 |
| Equity Risk Premium                 | Ibbotson premium = 5%                     | Updated implied ERP = 6.5%                                                                                      |
| Other adjustments to cost of equity | Small cap premium = 3%                    | No small cap premium<br>Country risk adjustment = Lambda <sub>Brazil</sub> *<br>Brazil CRP = 0.26*6.77% = 2.28% |
| Cost of equity                      | $5\% + 1.2 (5\%) + 3\% = 14\%$            | $3\% + 1.6 (6.5\%) + 2.28\% = 15.68\%$                                                                          |
| Cost of debt (pre-tax)              | 3%                                        | $3\% + 6\%$ (based on synthetic rating) = 9%                                                                    |
| Tax rate                            | Effective tax rate = 30%                  | Marginal tax rate = 40%                                                                                         |
| Cost of debt (after-tax)            | $3\% (1-.3) = 2.1\%$                      | $9\% (1-.4) = 5.4\%$                                                                                            |
| Debt ratio                          | Book ratio: Liabilities=50%<br>Equity=50% | Market ratio: Interest bearing debt = 30%;<br>Equity= 70%                                                       |
| Cost of capital                     | $14\% (.5) + 2.1\% (.5) = 8.05\%$         | $15.68\% (.7) + 5.4\% (.3) = 12.60\%$                                                                           |

# LAYER 5: THE PRICE OF GROWTH..

![](_page_166_Figure_58.jpeg)

- You are looking at the projected cash flows provided by the management of the firm, for use in valuation

| Year           | Current  | 1        | 2        | 3        | 4        |
|----------------|----------|----------|----------|----------|----------|
| Growth rate    |          | 10%      | 10%      | 10%      | 10%      |
| Revenues       | \$100.00 | \$110.00 | \$121.00 | \$133.10 | \$146.41 |
| EBIT (1-t)     | \$30.00  | \$33.00  | \$36.30  | \$39.93  | \$43.92  |
| + Depreciation | \$15.00  | \$16.50  | \$18.15  | \$19.97  | \$21.96  |
| - Cap Ex       | \$18.00  | \$19.80  | \$21.78  | \$23.96  | \$26.35  |
| - Chg in WC    | \$3.00   | \$3.30   | \$3.63   | \$3.99   | \$4.39   |
| FCFF           | \$24.00  | \$26.40  | \$29.04  | \$31.94  | \$35.14  |

 W

# LAYER 6: THE “FIXED DEBT RATIO” ASSUMPTION

![](_page_167_Figure_72.jpeg)

- You have been asked to value Hormel Foods, a firm which currently has the following cost of capital:
  - Cost of capital =  $7.31\% (.9) + 2.36\% (.1) = 6.8\%$
- You believe that the target debt ratio for this firm should be 30%. What will the cost of capital be at the target debt ratio?
  
- Which debt ratio (and cost of capital) should you use in valuing this company?

# LAYER 7: THE TERMINAL VALUE

![](_page_168_Figure_82.jpeg)

- ▪ The best way to compute terminal value is to
  - a. Use a stable growth model and assume cash flows grow at a fixed rate forever
  - b. Use a multiple of EBITDA or revenues in the terminal year
  - c. Use the estimated liquidation value of the assets
- ▪ You have been asked to value a business. The business expects to \$ 120 million in after-tax earnings (and cash flow) next year and to continue generating these earnings in perpetuity. The firm is all equity funded and the cost of equity is 10%; the riskfree rate is 3% and the ERP is 7%. What is the value of the business?
- ▪ Assume now that you were told that the firm can grow earnings at 2% a year forever. Estimate the value of the business.

# ALL GOOD THINGS COME TO AN END..AND THE TERMINAL VALUE IS NOT AN ATM...

![](_page_169_Diagram_16.jpeg)

Myth 5.1: The only way to estimate terminal value is to use the perpetual growth model.

Myth 5.2: The perpetual growth model can give you an infinite value.

Myth 5.3: The growth rate is your biggest driver of terminal value.

Myth 5.4: Your growth rate cannot be negative in a perpetual growth model.

Myth 5.5: If your terminal value is a high proportion of your DCF value, it is flawed.

$$\text{Value of an asset with life } > n \text{ years} = \frac{E(CF_1)}{(1+r)^1} + \frac{E(CF_2)}{(1+r)^2} + \dots + \frac{E(CF_n)}{(1+r)^n} + \frac{\text{Terminal Value}_n}{(1+r)^n}$$

Truth 5.1: The terminal value can be based on annuities or a liquidation value.

Truth 5.2: Not if growth forever is capped at the growth rate of the economy.

Truth 5.3: Growth is not free & increasing growth can add or destroy value.

Truth 5.4: Growth can be negative forever & is often more reflective of reality.

Truth 5.5: The terminal value should be a high percent of value today.

# LAYER 8. FROM FIRM VALUE TO EQUITY VALUE: THE GARNISHING EFFECT...

![](_page_170_Figure_92.jpeg)

- For a firm with consolidated financial statements, you have discounted free cashflows to the firm at the cost of capital to arrive at a firm value of \$ 100 million. The firm has
  - A cash balance of \$ 15 million
  - Debt outstanding of \$ 20 million
  - A 5% holding in another company: the book value of this holding is \$ 5 million. (Market value of equity in this company is \$ 200 million)
  - Minority interests of \$ 10 million on the balance sheet
- What is the value of equity in this firm?
  - How would your answer change if you knew that the firm was the target of a lawsuit it is likely to win but where the potential payout could be \$ 100 million if it loses?

# LAYER 9. FROM EQUITY VALUE TO EQUITY VALUE PER SHARE

![](_page_171_Figure_65.jpeg)

- ▪ You have valued the equity in a firm at \$ 200 million. Estimate the value of equity per share if there are 10 million shares outstanding..
- ▪ How would your answer change if you were told that there are 2 million employee options outstanding, with a strike price of \$ 20 a share and 5 years left to expiration?

# LAYER 10. THE FINAL CIRCLE OF HELL...

![](_page_172_Picture_63.jpeg)

**Exhibit 8**  
**KENNECOTT COPPER CORPORATION**  
**PROJECTED CARBORUNDUM COMPANY FINANCIAL DATA ADJUSTED TO REFLECT THE ACQUISITION OF CARBORUNDUM BY KENNECOTT**  
 AT A PRICE OF \$66 PER SHARE, 1977-1987  
 (\$ millions except for per share and ratio data)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1977    | 1977              | 1978    | 1979    | 1980      | 1981      | 1982      | 1983      | 1984      | 1985      | 1986      | 1987      |         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------------------|---------|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------|
| <b>Income statement</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Sales .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | \$717.6 |                   | \$790.1 | \$885.9 | \$1,005.2 | \$1,129.9 | \$1,265.5 | \$1,392.1 | \$1,531.3 | \$1,684.4 | \$1,852.8 | \$2,058.1 |         |
| Net income (before adjustments) .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 38.4    |                   | 43.1    | 50.7    | 60.1      | 70.6      | 84.7      | 93.2      | 102.5     | 112.7     | 124.0     | 136.4     |         |
| Interest adjustment .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0       |                   | 6.5     | 7.8     | 8.5       | 9.2       | 9.8       | 10.7      | 11.7      | 12.8      | 14.0      | 15.4      |         |
| Goodwill adjustment .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 0       |                   | 2.0     | 2.0     | 2.0       | 2.0       | 2.0       | 2.0       | 2.0       | 2.0       | 2.0       | 2.0       |         |
| Plant write-up adjustment .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 0       |                   | 2.8     | 2.8     | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       |         |
| Net income (after adjustments) .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \$38.4  |                   | \$31.8  | \$38.1  | \$ 46.8   | \$ 56.6   | \$ 70.1   | \$ 77.7   | \$ 86.0   | \$ 95.1   | \$ 105.2  | \$ 116.2  |         |
| <b>Balance sheet</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Working capital .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | \$198.8 | + 37.0<br>+ 100.0 | \$195.8 | \$202.9 | \$223.0   | \$248.1   | \$274.2   | \$302.8   | \$329.3   | \$358.6   | \$390.7   | \$426.1   | \$465.0 |
| Property, plant, and equipment .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 181.8   | + 124.0           | 305.8   | 334.2   | 367.4     | 384.6     | 400.1     | 411.6     | 437.5     | 466.6     | 499.1     | 535.6     | 576.1   |
| Goodwill .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0       | + 80.0            | 80.0    | 78.0    | 76.0      | 74.0      | 72.0      | 70.0      | 68.0      | 66.0      | 64.0      | 62.0      | 60.0    |
| Total assets .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 384.3   | + 201.0           | 785.3   | 824.0   | 889.9     | 948.4     | 1,007.0   | 1,065.8   | 1,135.5   | 1,213.1   | 1,299.0   | 1,394.6   | 1,500.3 |
| Long-term debt .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 86.2    | + 100.0           | 186.2   | 220.9   | 238.8     | 252.9     | 266.8     | 280.1     | 297.7     | 317.5     | 339.4     | 363.9     | 391.0   |
| Shareholders' equity .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 309.0   | + 101.0           | 410.0   | 410.1   | 443.5     | 469.7     | 495.4     | 520.2     | 553.0     | 589.6     | 630.3     | 675.7     | 726.0   |
| Total capital .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 395.2   | + 201.0           | 596.2   | 631.0   | 682.3     | 722.6     | 762.2     | 800.3     | 850.7     | 907.1     | 969.7     | 1,039.6   | 1,117.0 |
| <b>Capital sources</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Profit retentions .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |                   | \$ 0.1  | \$33.4  | \$26.2    | \$25.7    | \$24.8    | \$32.8    | \$36.6    | \$40.7    | \$45.4    | \$50.3    |         |
| Capital contributed by Kennecott .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |                   | -       | -       | -         | -         | -         | -         | -         | -         | -         | -         |         |
| Debt financing (net) .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |                   | 34.7    | 17.9    | 14.1      | 13.9      | 13.3      | 17.6      | 19.8      | 21.9      | 24.5      | 27.1      |         |
| Total capital added .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                   | \$34.8  | \$51.3  | \$40.3    | \$39.6    | \$38.1    | \$50.4    | \$56.4    | \$62.6    | \$69.9    | \$77.4    |         |
| <b>Key financial ratios</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Growth rate in sales (%) .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 16.9    |                   | 10.1    | 12.1    | 13.5      | 12.4      | 12.0      | 10.0      | 10.0      | 10.0      | 10.0      | 10.0      |         |
| Sales/assets .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 1.23    |                   | 0.96    | 1.00    | 1.06      | 1.12      | 1.19      | 1.23      | 1.26      | 1.30      | 1.33      | 1.36      |         |
| Profit/sales .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | .054    |                   | 0.040   | 0.043   | 0.047     | 0.050     | 0.055     | 0.056     | 0.056     | 0.056     | 0.057     | 0.057     |         |
| Assets/net worth .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1.89    |                   | 2.01    | 2.01    | 2.02      | 2.05      | 2.05      | 2.05      | 2.06      | 2.06      | 2.07      |           |         |
| Profit/net worth .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | .124    |                   | 0.078   | 0.086   | 0.100     | 0.114     | 0.135     | 0.141     | 0.146     | 0.151     | 0.156     | 0.160     |         |
| <b>Cash flow to Kennecott</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Acquisition of Carborundum .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         | \$(550.0)         |         |         |           |           |           |           |           |           |           |           |         |
| Dividends to Kennecott .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |         | 140.0             | \$31.7  | \$ 4.7  | \$20.6    | \$30.9    | \$45.3    | \$44.9    | \$49.4    | \$54.4    | \$59.8    | \$ 65.9   |         |
| Utilization of Kennecott tax loss carryforwards .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |                   | -       | 20.0    | 20.0      | -         | -         | -         | -         | -         | -         | -         |         |
| Tax shelter from plant write-up adj. ....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                   | 2.8     | 2.8     | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       | 2.8       |         |
| Terminal value at 10 times earnings .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Net cash flow .....                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |         | \$(410.0)         | \$54.5  | \$27.5  | \$23.4    | \$35.7    | \$48.1    | \$47.7    | \$52.2    | \$57.2    | \$62.6    | \$1,113.6 |         |
| <b>Assumptions:</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| *Kennecott would pay \$550 million to acquire Carborundum's equity which had a book value of \$309 million. The \$241 million in excess of purchase price over book value of assets acquired would be allocated as follows: (a) \$37.0 million would be added to inventory to reflect the replacement cost of inventories; (b) \$11.0 million would be added to land to reflect the market value of land; (c) \$113 million would be added to net plant and equipment to reflect the depreciated replacement cost of plant and equipment; and (d) \$80 million would be added to goodwill. Immediately following the acquisition of Carborundum, Carborundum borrows \$100 million and then pays a \$140 million dividend to Kennecott. This dividend is financed with the \$100 million plus \$40 million of Carborundum's excess cash. |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| *Interest at the rate of 10% (5% after taxes) is paid on the difference between the amount of Carborundum debt outstanding in Exhibit 8 and the amount of debt assumed to be outstanding in Exhibit 5. In Exhibit 8, it is assumed that Carborundum will have 35% debt in its total capital structure after 1977.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| *The \$80 million of goodwill created as a result of the acquisition is amortized over 40 years. This expense is not tax-deductible. Dividends to Kennecott equal the difference between Carborundum's net profit (after adjustment) and the profit retention requirements needed to support Carborundum's growth. The utilization of \$40 million of tax loss carry-forwards and investment tax credit carryforwards available to Kennecott are assumed to be utilized as a result of the Carborundum acquisition and that these would expire unutilized without the acquisition.                                                                                                                                                                                                                                                       |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| *Carborundum is assumed to be sold at the end of ten years at a price equal to ten times earnings. The proceeds from this sale, \$1,162 million, are reduced by \$117.1 million as a result of taxes on the capital gain of \$1,162--\$726. Carborundum's net worth at 12/31/87 is assumed to be \$726 million.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |         |                   |         |         |           |           |           |           |           |           |           |           |         |
| Sources: Exhibit 5 and casewriter projections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         |                   |         |         |           |           |           |           |           |           |           |           |         |

|                           | Cost of Equity | Cost of Capital |
|---------------------------|----------------|-----------------|
| Kennecott Corp (Acquirer) | 13.0%          | 10.5%           |
| Carborundum (Target)      | 16.5%          | 12.5%           |