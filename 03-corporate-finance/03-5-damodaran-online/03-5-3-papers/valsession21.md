---
title: "Valsession21"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valfall15/valsession21.pdf
---

#### VALUATION: PACKET 3 REAL OPTIONS, ACQUISITION VALUATION AND VALUE ENHANCEMENT

Aswath Damodaran 

Updated: september 2015 

# REAL OPTIONS: FACT AND

![](_page_1_Picture_2.jpeg)

Aswath Damodaran 

#### Underlying Theme: Searching for an Elusive Premium

**3**

¨ TradiRonal discounted cashflow models under esRmate the value of investments, where there are opRons embedded in the investments to ¤ Delay or defer making the investment (delay) ¤ Adjust or alter producRon schedules as price changes (flexibility) ¤ Expand into new markets or products at later stages in the process, based upon observing favorable outcomes at the early stages (expansion) ¤ Stop producRon or abandon investments if the outcomes are unfavorable at early stages (abandonment) ¨ Put another way, real opRon advocates believe that you should be paying a premium on discounted cashflow value esRmates. 

# A bad investment…

![](_page_3_Diagram_2.jpeg)

Becomes a good one… 

![](_page_4_Diagram_2.jpeg)

# Three Basic QuesRons

**6**

¨ When is there a real opRon embedded in a decision or an asset? ¨ When does that real opRon have significant economic value? ¨ Can that value be esRmated using an opRon pricing model? 

#### When is there an opRon embedded in an acRon?

**7**

¨ An opRon provides the holder with the right to buy or sell a specified quanRty of an underlying asset at a fixed price (called a strike price or an exercise price) at or before the expiraRon date of the opRon. ¨ There has to be a clearly defined underlying asset whose value changes over Rme in unpredictable ways. ¨ The payoffs on this asset (real opRon) have to be conRngent on an specified event occurring within a finite period. 

# Payoff Diagram on a Call

![](_page_7_Diagram_2.jpeg)

# Payoff Diagram on Put OpRon

![](_page_8_Diagram_2.jpeg)

#### When does the opRon have significant economic value?

**10**

¨ For an opRon to have significant economic value, there has to be a restricRon on compeRRon in the event of the conRngency. In a perfectly compeRRve product market, no conRngency, no maaer how posiRve, will generate posiRve net present value. ¨ At the limit, real opRons are most valuable when you have exclusivity - you and only you can take advantage of the conRngency. They become less valuable as the barriers to compeRRon become less steep. 

# Determinants of opRon value

**11**

¨ Variables RelaRng to Underlying Asset ¤ Value of Underlying Asset; as this value increases, the right to buy at a fixed price (calls) will become more valuable and the right to sell at a fixed price (puts) will become less valuable. ¤ Variance in that value; as the variance increases, both calls and puts will become more valuable because all opRons have limited downside and depend upon price volaRlity for upside. ¤ Expected dividends on the asset, which are likely to reduce the price appreciaRon component of the asset, reducing the value of calls and increasing the value of puts. ¨ Variables RelaRng to OpRon ¤ Strike Price of OpRons; the right to buy (sell) at a fixed price becomes more (less) valuable at a lower price. ¤ Life of the OpRon; both calls and puts benefit from a longer life. ¨ Level of Interest Rates; as rates increase, the right to buy (sell) at a fixed price in the future becomes more (less) valuable. 

#### When can you use opRon pricing models to value real opRons?

**12**

¨ The noRon of a replicaRng pordolio that drives opRon pricing models makes them most suited for valuing real opRons where ¤ The underlying asset is traded - this yield not only observable prices and volaRlity as inputs to opRon pricing models but allows for the possibility of creaRng replicaRng pordolios ¤ An acRve marketplace exists for the opRon itself. ¤ The cost of exercising the opRon is known with some degree of certainty. ¨ When opRon pricing models are used to value real assets, we have to accept the fact that ¤ The value esRmates that emerge will be far more imprecise. ¤ The value can deviate much more dramaRcally from market price because of the difficulty of arbitrage. 

# CreaRng a replicaRng pordolio

**13**

¨ The objecRve in creaRng a replicaRng pordolio is to use a combinaRon of riskfree borrowing/lending and the underlying asset to create the same cashflows as the opRon being valued. ¤ Call = Borrowing + Buying D of the Underlying Stock ¤ Put = Selling Short D on Underlying Asset + Lending ¤ The number of shares bought or sold is called the opRon delta. ¨ The principles of arbitrage then apply, and the value of the opRon has to be equal to the value of the replicaRng pordolio. 

# The Binomial OpRon Pricing Model

![](_page_13_Diagram_2.jpeg)

# The LimiRng DistribuRons….

**15**

¨ As the Rme interval is shortened, the limiRng distribuRon, as t -> 0, can take one of two forms. ¤ If as t -> 0, price changes become smaller, the limiRng distribuRon is the normal distribuRon and the price process is a conRnuous one. ¤ If as t->0, price changes remain large, the limiRng distribuRon is the poisson distribuRon, i.e., a distribuRon that allows for price jumps. ¨ The Black-Scholes model applies when the limiRng distribuRon is the normal distribuRon , and explicitly assumes that the price process is conRnuous and that there are no jumps in asset prices. 

# Black and Scholes…

16

- ❑ The version of the model presented by Black and Scholes was designed to value European options, which were dividend-protected.
- ❑ The value of a call option in the Black-Scholes model can be written as a function of the following variables:
  - ❑  $S$  = Current value of the underlying asset
  - ❑  $K$  = Strike price of the option
  - ❑  $t$  = Life to expiration of the option
  - ❑  $r$  = Riskless interest rate corresponding to the life of the option
  - ❑  $\sigma^2$  = Variance in the  $\ln(\text{value})$  of the underlying asset

# The Black Scholes Model

17

Value of call =  $S N (d_1) - K e^{-rt} N(d_2)$ 

where

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r + \frac{\sigma^2}{2})t}{\sigma \sqrt{t}}$$

$$d_2 = d_1 - \sigma vt$$

- □ The replicating portfolio is embedded in the Black-Scholes model. To replicate this call, you would need to
  - □ Buy  $N(d_1)$  shares of stock;  $N(d_1)$  is called the option delta
  - □ Borrow  $K e^{-rt} N(d_2)$

# The Normal DistribuRon

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

# AdjusRng for Dividends

**19**

¨ If the dividend yield (y = dividends/ Current value of the asset) of the underlying asset is expected to remain unchanged during the life of the opRon, the Black-Scholes model can be modified to take dividends into account. ¨ C = S e-yt N(d1) - K e-rtN(d2) 

where, 

d2 = d1 - σ √t 

¨ The value of a put can also be derived: ¨ P = K e-rt (1-N(d2)) - S e-yt (1-N(d1)) 

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + (r - y + \frac{\sigma^2}{2}) t}{\sigma \sqrt{t}}$$