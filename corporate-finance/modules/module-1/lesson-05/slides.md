## Session 5: The Risk-Free Rate

*Nothing in life is guaranteed, right?*

*Aswath Damodaran*

---

## Inputs Required to Use the CAPM

- The capital asset pricing model yields the following expected return:

  `Expected Return = Riskfree Rate + Beta × (Expected Return on the Market Portfolio − Riskfree Rate)`

- To use the model we need three inputs:
  - The current risk-free rate.
  - The expected market risk premium (the premium expected for investing in risky assets over the riskless asset).
  - The beta of the asset being analyzed.

---

## The Riskfree Rate and Time Horizon

- On a riskfree asset, the actual return is always equal to the expected return. For an investment to be riskfree — i.e., to have an actual return equal to the expected return — two conditions have to be met:
  - There has to be no default risk, which generally implies that the security has to be issued by the government. Note, however, that not all governments can be viewed as default free.
  - There can be no uncertainty about reinvestment rates, which implies that it is a zero-coupon security with the same maturity as the cash flow being analyzed.
- Theoretically, this translates into using different riskfree rates for each cash flow — the 1-year zero coupon rate for the cash flow in year 1, the 2-year zero coupon rate for the cash flow in year 2, and so on.
- Practically speaking, if there is substantial uncertainty about expected cash flows, the present value effect of using time-varying riskfree rates is small enough that it may not be worth it.

---

## The Bottom Line on Riskfree Rates

- Using a long-term government rate (even on a coupon bond) as the riskfree rate on all of the cash flows in a long-term analysis will yield a close approximation of the true value. For short-term analysis, it is entirely appropriate to use a short-term government security rate as the riskfree rate.
- The riskfree rate that you use in an analysis should be in the same currency as your cash flows are estimated in.
  - If your cash flows are in U.S. dollars, your riskfree rate has to be in U.S. dollars as well.
  - If your cash flows are in Euros, your riskfree rate should be a Euro riskfree rate.
- The conventional practice of estimating riskfree rates is to use the government bond rate, with the government being the one that is in control of issuing that currency. In November 2013, for instance, the rate on a ten-year US treasury bond (2.75%) is used as the risk-free rate in US dollars.

---

## What Is the Euro Riskfree Rate? An Exercise in November 2013

Rate on 10-year Euro Government Bonds: November 2013

| Country | Rate |
|---------|------|
| Greece | 8.30% |
| Portugal | 6.42% |
| Slovenia | 5.90% |
| Spain | 3.90% |
| Ireland | 3.95% |
| Italy | 3.30% |
| Belgium | 2.10% |
| France | 2.15% |
| Austria | 2.35% |
| Germany | 1.75% |

---

## When the Government Is Default Free: Risk-Free Rates — November 2013

*(diagram)*

---

## What If There Is No Default-Free Entity? Risk-Free Rates in November 2013

- If the government is perceived to have default risk, the government bond rate will have a default spread component in it and will not be riskfree. There are three choices when this is the case:
  - Adjust the local currency government borrowing rate for default risk to get a riskless local currency rate.
    - In November 2013, the Indian government rupee bond rate was 8.82%. The local currency rating from Moody's was Baa3 and the default spread for a Baa3 rated country bond was 2.25%.

      `Riskfree Rate in Rupees = 8.82% − 2.25% = 6.57%`

    - In November 2013, the Chinese Renminbi government bond rate was 4.30% and the local currency rating was Aa3, with a default spread of 0.8%.

      `Riskfree Rate in Chinese Renminbi = 4.30% − 0.8% = 3.5%`

  - Do the analysis in an alternate currency where getting the riskfree rate is easier. With Vale in 2013, we could choose to do the analysis in US dollars (rather than estimate a riskfree rate in R$). The riskfree rate is then the US treasury bond rate.
  - Do your analysis in real terms, in which case the riskfree rate has to be a real riskfree rate. The inflation-indexed treasury rate is a measure of a real riskfree rate.

---

## Estimating a Sovereign Default Spread

*(diagram)*

---

## Risk-Free Rates Across Currencies: January 2017

*(diagram)*

---

## Task & Reading

- Task: Estimate the risk-free rate in the currency of your choice.
- Optional: Read Chapter 4
