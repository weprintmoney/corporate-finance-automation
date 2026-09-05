---
title: "Optdelay"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/optdelay.pdf
---

## A. THE OPTION TO DELAY

- ▪ When a firm has **exclusive rights to a project or product** for a specific period, it can delay taking this project or product until a later date.
- ▪ A traditional investment analysis **just answers the question of whether the project is a “good” one if taken today.**
- ▪ Thus, the fact that a project **does not pass muster today** (because its NPV is negative, or its IRR is less than its hurdle rate) does not mean that the rights to this project are not valuable.

# VALUING THE OPTION TO DELAY A PROJECT

![](_page_1_Diagram_39.jpeg)

# EXAMPLE 1: VALUING PRODUCT PATENTS AS OPTIONS

- ▪ A product patent provides the firm with the right to develop the product and market it.
  - ▪ It will do so only if the present value of the expected cash flows from the product sales exceed the cost of development.
  - ▪ If this does not occur, the firm can shelve the patent and not incur any further costs.
- ▪ If  $I$  is the present value of the costs of developing the product, and  $V$  is the present value of the expected cashflows from development, the payoffs from owning a product patent can be written as:
- ▪ Payoff from owning a product patent  $= V - I$  if  $V > I$   
   $= 0$  if  $V \leq I$

# PAYOFF ON PRODUCT OPTION

![](_page_3_Diagram_27.jpeg)

# OBTAINING INPUTS FOR PATENT VALUATION

| Input                                    | Estimation Process                                                                                                                                                                                       |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Value of the Underlying Asset         | <ul> <li>• Present Value of Cash Inflows from taking project now</li> <li>• This will be noisy, but that adds value.</li> </ul>                                                                          |
| 2. Variance in value of underlying asset | <ul> <li>• Variance in cash flows of similar assets or firms</li> <li>• Variance in present value from capital budgeting simulation.</li> </ul>                                                          |
| 3. Exercise Price on Option              | <ul> <li>• Option is exercised when investment is made.</li> <li>• Cost of making investment on the project; assumed to be constant in present value dollars.</li> </ul>                                 |
| 4. Expiration of the Option              | <ul> <li>• Life of the patent</li> </ul>                                                                                                                                                                 |
| 5. Dividend Yield                        | <ul> <li>• Cost of delay = Cash flow next year as % of Value of Underlying asset</li> <li>• If cash flows not available, use <math>1/n</math> (one less year or protection from competition).</li> </ul> |

![](_page_4_Picture_5.jpeg)

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

![](_page_6_Figure_10.jpeg)

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

![](_page_14_Diagram_27.jpeg)

# ESTIMATING INPUTS FOR NATURAL RESOURCE OPTIONS

| Input                                          | Estimation Process                                                                                                                                                                |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Value of Available Reserves of the Resource | <ul> <li>• Expert estimates (Geologists for oil..); The present value of the after-tax cash flows from the resource are then estimated.</li> </ul>                                |
| 2. Cost of Developing Reserve (Strike Price)   | <ul> <li>• Past costs and the specifics of the investment</li> </ul>                                                                                                              |
| 3. Time to Expiration                          | <ul> <li>• Relinquishment Period: if asset has to be relinquished at a point in time.</li> <li>• Time to exhaust inventory - based upon inventory and capacity output.</li> </ul> |
| 4. Variance in value of underlying asset       | <ul> <li>• based upon variability of the price of the resources and variability of available reserves.</li> </ul>                                                                 |
| 5. Net Production Revenue (Dividend Yield)     | <ul> <li>• Net production revenue every year as percent of market value.</li> </ul>                                                                                               |
| 6. Development Lag                             | <ul> <li>• Calculate present value of reserve based upon the lag.</li> </ul>                                                                                                      |

![](_page_15_Picture_5.jpeg)

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