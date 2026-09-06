---
title: "Chapter 27 Derivations"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/CFTheory/deriv/ch27der.html
---

Chapter 27 Derivations

### *Discussion Issues and Derivations*

1. Option Pricing Models   
   The underlying notion that drives all option pricing models is the idea of replication, i.e. that an option can be valued by valuing a portfolio that has the same cash flows. For a call option, this replicating portfolio can be created by borrowing money and buying units of the underlying asset. For a put option, this replicating portfolio can be created by selling short units of the underlying asset and buying a riskless asset with the cash.  
   In the Black-Scholes model, this replicating portfolio is created under the assumption that prices move continuously and that the replicating portfolio can therefore also be changed continuously.  
   In the binomial model, the replicating portfolio is created under the assumption of discrete price movements, where at each stage in the model prices can move to one of two points.

- Dealing with Dilution in option pricing   
  The derivation of the Black-Scholes model is based upon the assumption that exercising an option does not affect the value of the underlying asset. This may be true for listed options on stocks, but it is not true for some types of options. For instance, the exercise of warrants increases the number of shares outstanding and brings fresh cash into the firm, both of which will affect the stock price. The expected negative impact (dilution) of exercise will decrease the value of warrants compared to otherwise similar call options.
