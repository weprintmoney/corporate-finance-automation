---
title: "Packet1Fall16"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/packet1fall16.pdf
---

### Valuation: Lecture Note Packet 1 Intrinsic Valuation

Aswath Damodaran

Updated: September 2016

# The essence of intrinsic value

¨ In intrinsic valuation, you value an asset based upon its fundamentals (or intrinsic characteristics). ¨ For cash flow generating assets, the intrinsic value will be a function of the magnitude of the expected cash flows on the asset over its lifetime and the uncertainty about receiving those cash flows. ¨ Discounted cash flow valuation is a tool for estimating intrinsic value, where the expected value of an asset is written as the present value of the expected cash flows on the asset, with either the cash flows or the discount rate adjusted to reflect the risk.

### The two faces of discounted cash flow valuation

¨ The value of a risky asset can be estimated by discounting the expected cash flows on the asset over its life at a risk-adjusted discount rate: 

| Value of asset = | $\frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$ |
|------------------|-------------------------------------------------------------------------------------------------------------|
|------------------|-------------------------------------------------------------------------------------------------------------|

where the asset has an n-year life, E(CFt) is the expected cash flow in period t and r is a discount rate that reflects the risk of the cash flows.

¨ Alternatively, we can replace the expected cash flows with the guaranteed cash flows we would have accepted as an alternative (certainty equivalents) and discount these at the riskfree rate:

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

where CE(CFt) is the certainty equivalent of E(CFt) and rf is the riskfree rate.

### Risk Adjusted Value: Two Basic Propositions

¨ The value of an asset is the risk-adjusted present value of the cash flows:

| Value of asset = | $\frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$ |
|------------------|-------------------------------------------------------------------------------------------------------------|
|------------------|-------------------------------------------------------------------------------------------------------------|

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

- 1. The "IT" proposition: If IT does not affect the expected cash flows or the riskiness of the cash flows, IT cannot affect value.
- 2. The "DUH" proposition: For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.
- 3. The "DON'T FREAK OUT" proposition: Assets that generate cash flows early in their life will be worth more than assets that generate cash flows later; the latter may however have greater growth and higher cash flows to compensate.

### DCF Choices: Equity Valuation versus Firm Valuation

![](_page_4_Diagram_3.jpeg)

**Equity valuation**: Value just the equity claim in the business

**Firm Valuation**: Value the entire business

# Equity Valuation

| Assets          | Liabilities                      |
|-----------------|----------------------------------|
| Assets in Place | Debt                             |
| Growth Assets   | cost of raising equity financing |

*Figure 5.5: Equity Valuation*

# Firm Valuation

| <b>Assets</b>                                                                                                                            |                 | <b>Liabilities</b> |                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------|-------------------------------------------------------------------------------------------------------|
| <p>Cash flows considered are cashflows from assets, prior to any debt payments but after firm has reinvested to create growth assets</p> | Assets in Place | Debt               | Discount rate reflects the cost of raising both debt and equity financing, in proportion to their use |
|                                                                                                                                          | Growth Assets   | Equity             |                                                                                                       |
| <p>Present value is value of the entire firm, and reflects the value of all claims on the firm.</p>                                      |                 |                    |                                                                                                       |

*Figure 5.6: Firm Valuation*

# Firm Value and Equity Value

- ¨ To get from firm value to equity value, which of the following would you need to do?
- a. Subtract out the value of long term debt
- b. Subtract out the value of all debt
- c. Subtract the value of any debt that was included in the cost of capital calculation
- d. Subtract out the value of all liabilities in the firm ¨ Doing so, will give you a value for the equity which is
- a. greater than the value you would have got in an equity valuation
- b. lesser than the value you would have got in an equity valuation
- c. equal to the value you would have got in an equity valuation

# Cash Flows and Discount Rates

¨ Assume that you are analyzing a company with the following cashflows for the next five years. 

| Year           | CF	to	Equity | Interest	Exp (1-tax	rate) | CF	to	Firm  |
|----------------|--------------|---------------------------|-------------|
| 1              | \$	50        | \$	40                     | \$	90       |
| 2              | \$	60        | \$	40                     | \$	100      |
| 3              | \$	68        | \$	40                     | \$	108      |
| 4              | \$	76.2      | \$	40                     | \$	116.2    |
| 5              | \$	83.49     | \$	40                     | \$	123.49   |
| Terminal	Value | \$	1603.0    |                           | \$	2363.008 |

¨ Assume also that the cost of equity is 13.625% and the firm can borrow long term at 10%. (The tax rate for the firm is 50%.) ¨ The current market value of equity is \$1,073 and the value of debt outstanding is \$800.

# Equity versus Firm Valuation

¨ Method 1: Discount CF to Equity at Cost of Equity to get value of equity ¤ Cost of Equity = 13.625% ¤ Value of Equity = 50/1.13625 + 60/1.136252 + 68/1.136253 + 76.2/1.136254 + (83.49+1603)/1.136255 = **\$1073** ¨ Method 2: Discount CF to Firm at Cost of Capital to get value of firm ¤ Cost of Debt = Pre-tax rate (1- tax rate) = 10% (1-.5) = 5% Cost of Capital = 13.625% (1073/1873) + 5% (800/1873) = 9.94% ¤ PV of Firm = 90/1.0994 + 100/1.09942 + 108/1.09943 + 116.2/1.09944 + (123.49+2363)/1.09945 = \$1873 ¤ Value of Equity = Value of Firm - Market Value of Debt = \$ 1873 - \$ 800 = **\$1073** 

# First Principle of Valuation

¨ Discounting Consistency Principle: Never mix and match cash flows and discount rates. ¨ Mismatching cash flows to discount rates is deadly. ¤ Discounting cashflows after debt cash flows (equity cash flows) at the weighted average cost of capital will lead to an upwardly biased estimate of the value of equity ¤ Discounting pre-debt cashflows (cash flows to the firm) at the cost of equity will yield a downward biased estimate of the value of the firm.

### The Effects of Mismatching Cash Flows and Discount Rates

¨ Error 1: Discount CF to Equity at Cost of Capital to get equity value ¤ PV of Equity = 50/1.0994 + 60/1.09942 + 68/1.09943 + 76.2/1.09944 + (83.49+1603)/1.09945 = \$1248 ¤ Value of equity is overstated by \$175. ¨ Error 2: Discount CF to Firm at Cost of Equity to get firm value ¤ PV of Firm = 90/1.13625 + 100/1.136252 + 108/1.136253 + 116.2/1.136254 + (123.49+2363)/1.136255 = \$1613 ¤ PV of Equity = \$1612.86 - \$800 = \$813 ¤ Value of Equity is understated by \$ 260. ¨ Error 3: Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity ¤ Value of Equity = \$ 1613 ¤ Value of Equity is overstated by \$ 540

![]()The devil is in the details..

# Discounted Cash Flow Valuation: The Steps

- 1. Estimate the discount rate or rates to use in the valuation
  - 1. Discount rate can be either a cost of equity (if doing equity valuation) or a cost of capital (if valuing the firm)
  - 2. Discount rate can be in nominal terms or real terms, depending upon whether the cash flows are nominal or real
  - 3. Discount rate can vary across time.
- 2. Estimate the current earnings and cash flows on the asset, to either equity investors (CF to Equity) or to all claimholders (CF to Firm)
- 3. Estimate the future earnings and cash flows on the firm being valued, generally by estimating an expected growth rate in earnings.
- 4. Estimate when the firm will reach "stable growth" and what characteristics (risk & cash flow) it will have when it does.
- 5. Choose the right DCF model for this asset and value it.

# Generic DCF Valuation Model

![](_page_14_Diagram_3.jpeg)

#### DISCOUNTED CASHFLOW VALUATION

# Same ingredients, different approaches…

| Input           | Dividend Discount Model                            | FCFE (Potential dividend) discount model                                                                   | FCFF (firm) valuation model                                                                |
|-----------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Cash flow       | Dividend                                           | Potential dividends<br>= FCFE = Cash flows<br>after taxes,<br>reinvestment needs<br>and debt cash<br>flows | FCFF = Cash flows<br>before debt<br>payments but after<br>reinvestment needs<br>and taxes. |
| Expected growth | In equity income<br>and dividends                  | In equity income<br>and FCFE                                                                               | In operating<br>income and FCFF                                                            |
| Discount rate   | Cost of equity                                     | Cost of equity                                                                                             | Cost of capital                                                                            |
| Steady state    | When dividends<br>grow at constant<br>rate forever | When FCFE grow at<br>constant rate<br>forever                                                              | When FCFF grow at<br>constant rate<br>forever                                              |

# Start easy: The Dividend Discount Model

![](_page_16_Diagram_2.jpeg)

#### Moving on up: The "potential dividends" or FCFE model

![](_page_17_Diagram_2.jpeg)

### To valuing the entire business: The FCFF model

![](_page_18_Diagram_2.jpeg)

![]()The D in the DCF..

# Estimating Inputs: Discount Rates

¨ While discount rates obviously matter in DCF valuation, they don't matter as much as most analysts think they do. ¨ At an intuitive level, the discount rate used should be consistent with both the riskiness and the type of cashflow being discounted. ¤ Equity versus Firm: If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital. ¤ Currency: The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated. ¤ Nominal versus Real: If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

# Risk in the DCF Model

22

*Expectation of cash flows across all scenarios, good and bad. Incorporates all risks that affect the asset / business.*

---

Expected Cash Flows

Risk Adjusted Discount Rate

*Discount rate should reflect the risk perceived by the marginal investor in the company*

$$\text{Risk Adjusted Cost of equity} = \text{Risk free rate in the currency of analysis} + \text{Relative risk of company/equity in question} \times \text{Equity Risk Premium required for average risk equity}$$

# Not all risk is created equal…

¨ Estimation versus Economic uncertainty ¤ Estimation uncertainty reflects the possibility that you could have the "wrong model" or estimated inputs incorrectly within this model. ¤ Economic uncertainty comes the fact that markets and economies can change over time and that even the best models will fail to capture these unexpected changes. ¨ Micro uncertainty versus Macro uncertainty ¤ Micro uncertainty refers to uncertainty about the potential market for a firm's products, the competition it will face and the quality of its management team. ¤ Macro uncertainty reflects the reality that your firm's fortunes can be affected by changes in the macro economic environment. ¨ Discrete versus continuous uncertainty ¤ Discrete risk: Risks that lie dormant for periods but show up at points in time. (Examples: A drug working its way through the FDA pipeline may fail at some stage of the approval process or a company in Venezuela may be nationalized) ¤ Continuous risk: Risks changes in interest rates or economic growth occur continuously and affect value as they happen. 

### Risk and Cost of Equity: The role of the marginal investor

¨ Not all risk counts: While the notion that the cost of equity should be higher for riskier investments and lower for safer investments is intuitive, what risk should be built into the cost of equity is the question. ¨ Risk through whose eyes? While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment ¨ The diversification effect: Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (i.e, market or non-diversifiable risk). In effect, it is primarily economic, macro, continuous risk that should be incorporated into the cost of equity. 

#### The Cost of Equity: Competing " Market Risk" Models

#### **Model Expected Return Inputs Needed**

CAPM  $E(R) = Rf + \beta (R_m - R_f)$  Riskfree Rate

Beta relative to market portfolio

Market Risk Premium

APM  $E(R) = Rf + \Sigma\beta_j (R_j - R_f)$ 

- Rf) Riskfree Rate; # of Factors;

Betas relative to each factor

Factor risk premiums

Multi E(R) = Rf + Σβj (Rj- Rf) factor

- Rf) Riskfree Rate; Macro factors

factor Betas relative to macro factors

Macro economic risk premiums

Proxy  $E(R) = a + \sum \beta_j Y_j$  Proxies

Regression coefficients

# Classic Risk & Return: Cost of Equity

¨ In the CAPM, the cost of equity:

Cost of Equity = Riskfree Rate + Equity Beta \* (Equity Risk Premium)

¨ In APM or Multi-factor models, you still need a risk free rate, as well as betas and risk premiums to go with each factor. ¨ To use any risk and return model, you need ¨ A risk free rate as a base ¨ A single equity risk premium (in the CAPM) or factor risk premiums, in the the multi-factor models ¨ A beta (in the CAPM) or betas (in multi-factor models)

27

# Discount Rates: I

## The Risk Free Rate

# The Risk Free Rate: Laying the Foundations

- ¨ On a riskfree investment, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. ¨ For an investment to be riskfree, then, it has to have ¤ No default risk ¤ No reinvestment risk ¤ It follows then that if asked to estimate a risk free rate:
- 1. Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
- 2. Currencies matter: A risk free rate is currency-specific and can be very different for different currencies.
- 3. Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

# Test 1: A riskfree rate in US dollars!

- ¨ In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be
  - a. A three-month Treasury bill rate (0.2%)
  - b. A ten-year Treasury bond rate (2%)
  - c. A thirty-year Treasury bond rate (3%)
  - d. A TIPs (inflation-indexed treasury) rate (1%)
- e. None of the above ¨ What are we implicitly assuming about the US treasury when we use any of the treasury numbers?

# Test 2: A Riskfree Rate in Euros

**30**

![](_page_29_Figure_3.jpeg)

#### **Euro Government Bond Rates - January 1, 2016**

# Test 3: A Riskfree Rate in Indian Rupees

- ¨ The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 7.73% on January 1, 2016. ¨ In January 2016, the Indian government had a local currency sovereign rating of Baa3. The typical default spread (over a default free rate) for Baa3 rated country bonds in early 2016 was 2.44%. The riskfree rate in Indian Rupees is
  - a. The yield to maturity on the 10-year bond (7.73%)
  - b. The yield to maturity on the 10-year bond + Default spread (10.17%)
  - c. The yield to maturity on the 10-year bond – Default spread (5.29%)
  - d. None of the above

# Sovereign Default Spread: Three paths to the same destination…

¨ Sovereign dollar or euro denominated bonds: Find sovereign bonds denominated in US dollars, issued by an emerging sovereign. ¤ Default spread = Emerging Govt Bond Rate (in US \$) – US Treasury Bond rate with same maturity. ¨ CDS spreads: Obtain the traded value for a sovereign Credit Default Swap (CDS) for the emerging government. ¤ Default spread = Sovereign CDS spread (with perhaps an adjustment for CDS market frictions). ¨ Sovereign-rating based spread: For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries with the same sovereign rating.

# Local Currency Government Bond Rates – January 2016

| Currency          | Govt Bond rate (12/31/15) | Currency           | Govt Bond rate (12/31/15) |
|-------------------|---------------------------|--------------------|---------------------------|
| Australian \$     | 2.88%                     | Malaysian Ringgit  | 4.19%                     |
| Brazilian Reai    | 16.51%                    | Mexican Peso       | 6.31%                     |
| British Pound     | 1.96%                     | Nigerian Naira     | 11.09%                    |
| Bulgarian Lev     | 2.62%                     | Norwegian Krone    | 1.48%                     |
| Canadian \$       | 1.39%                     | NZ \$              | 3.58%                     |
| Chilean Peso      | 4.75%                     | Pakistani Rupee    | 9.00%                     |
| Chinese Yuan      | 2.84%                     | Peruvian Sol       | 6.96%                     |
| Colombian Peso    | 8.27%                     | Phillipine Peso    | 4.10%                     |
| Croatian Kuna     | 4.02%                     | Polish Zloty       | 2.94%                     |
| Czech Koruna      | 0.55%                     | Romanian Leu       | 3.77%                     |
| Danish Krone      | 0.94%                     | Russian Ruble      | 9.74%                     |
| Euro              | 0.63%                     | Singapore \$       | 2.61%                     |
| HK \$             | 1.59%                     | South African Rand | 10.16%                    |
| Hungarian Forint  | 3.42%                     | Swedish Krona      | 0.99%                     |
| Iceland Krona     | 5.88%                     | Swiss Franc        | -0.06%                    |
| Indian Rupee      | 7.73%                     | Taiwanese \$       | 1.02%                     |
| Indonesian Rupiah | 8.87%                     | Thai Baht          | 2.52%                     |
| Israeli Shekel    | 2.09%                     | Turkish Lira       | 10.42%                    |
| Japanese Yen      | 0.27%                     | US \$              | 2.27%                     |
| Kenyan Shilling   | 13.39%                    | Venezuelan Bolivar | 18.00%                    |
| Korean Won        | 2.09%                     | Vietnamese Dong    | 7.05%                     |

# Approach 1: Default spread from Government Bonds

| BONDS: HIGH YIELD & EMERGING MARKET |           |        |         |      |      |            |            |                  |             |              |
|-------------------------------------|-----------|--------|---------|------|------|------------|------------|------------------|-------------|--------------|
| Date                                | Ret. date | Coupon | Ratings |      |      | Ret. price | Ret. yield | Day's chge yield | Mtr's yield | Spread vt US |
|                                     |           |        | I*      | M*   | F*   |            |            |                  |             |              |
| <b>High Yield US\$</b>              |           |        |         |      |      |            |            |                  |             |              |
| Windsorn Services, LLC              | 11/17     | 7.88   | B+      | B2   | BB   | 102.40     | 6.80       | 0.80             | 1.06        | 5.45         |
| <b>High Yield Euro</b>              |           |        |         |      |      |            |            |                  |             |              |
| Rockemerts Int'l EV                 | 03/17     | 6.88   | B       | Cas1 | B    | 97.50      | -          | 0.80             | 0.00        | -            |
| <b>Emerging US\$</b>                |           |        |         |      |      |            |            |                  |             |              |
| Peru                                | 05/18     | 8.38   | BBB+    | A3   | BBB+ | 121.00     | 1.23       | 0.80             | 0.80        | 0.18         |
| Mexico                              | 06/18     | 11.40  | BBB+    | A3   | BBB+ | 106.35     | 1.46       | -0.37            | 0.01        | 0.41         |
| Brazil                              | 07/18     | 8.30   | BB+     | Bas1 | BB+  | 103.15     | 8.30       | 0.04             | 0.36        | 5.25         |
| Russia                              | 07/18     | 11.00  | BB+     | Bar1 | BBB- | 118.32     | 3.54       | 0.01             | 0.28        | 2.49         |
| Peru                                | 03/19     | 7.13   | BBB+    | A3   | BBB+ | 154.21     | 2.54       | 0.80             | 0.18        | 0.75         |
| Brazil                              | 01/21     | 7.88   | BB+     | Bas3 | BB+  | 93.32      | 6.60       | 0.80             | 0.90        | 4.83         |
| Turkey                              | 03/21     | 5.53   | -       | Bas3 | BBB- | 105.88     | 4.45       | 0.21             | 0.18        | 2.85         |
| Poland                              | 04/21     | 5.13   | A       | A2   | A    | 111.37     | 2.86       | 0.80             | 0.10        | 1.87         |
| Colombia                            | 07/21     | 4.38   | BBB     | Bas2 | BBB  | 100.33     | 4.42       | 0.80             | 0.40        | 2.82         |
| Turkey                              | 04/28     | 4.25   | -       | Bas3 | BBB- | 93.32      | 5.12       | 0.80             | 0.21        | 2.80         |
| <b>Emerging Euro</b>                |           |        |         |      |      |            |            |                  |             |              |
| Brazil                              | 03/15     | 7.38   | BBB-    | Bas2 | BBB  | 111.75     | 0.73       | 0.80             | 0.00        | 0.38         |
| Mexico                              | 03/17     | 4.25   | BBB+    | A3   | BBB+ | 111.13     | 1.50       | 0.80             | 0.00        | 0.45         |
| Mexico                              | 03/03     | 5.50   | BBB+    | -    | BBB+ | 108.49     | 3.01       | 0.80             | 0.10        | 1.22         |
| Bulgaria                            | 06/25     | 5.75   | BB+     | -    | BBB- | 114.81     | 3.94       | 0.80             | 0.11        | 1.63         |

Data provided by SIR Financial Information & Tullett Predon Information. US \$ denominated bonds NY close; all other London close. \*S - Standard & Poor's, M - Moody's, F - Fash.

*The Brazil Default Spread*  
 Brazil 2021 Bond: 6.83%  
 US 2021 T.Bond: 2.00%  
 Spread: 4.83%

# Approach 2: CDS Spreads – January 2016

| Country        | CDS Spread | CDS Spread adj for US | Country     | CDS Spread adj for US | Country | CDS Spread     | CDS Spread adj for US |       |
|----------------|------------|-----------------------|-------------|-----------------------|---------|----------------|-----------------------|-------|
| Abu Dhabi      | 1.21%      | 0.82%                 | Hungary     | 2.15%                 | 1.76%   | Peru           | 2.45%                 | 2.06% |
| Australia      | 0.73%      | 0.34%                 | Iceland     | 0.80%                 | 0.41%   | Philippines    | 1.73%                 | 1.34% |
| Austria        | 0.51%      | 0.12%                 | India       | 2.11%                 | 1.72%   | Poland         | 1.22%                 | 0.83% |
| Bahrain        | 3.91%      | 3.52%                 | Indonesia   | 3.25%                 | 2.86%   | Portugal       | 2.44%                 | 2.05% |
| Belgium        | 0.71%      | 0.32%                 | Ireland     | 0.80%                 | 0.41%   | Qatar          | 1.32%                 | 0.93% |
| Brazil         | 5.58%      | 5.19%                 | Israel      | 1.26%                 | 0.87%   | Romania        | 1.74%                 | 1.35% |
| Bulgaria       | 2.20%      | 1.81%                 | Italy       | 1.54%                 | 1.15%   | Russia         | 3.48%                 | 3.09% |
| Chile          | 1.66%      | 1.27%                 | Japan       | 0.93%                 | 0.54%   | Saudi Arabia   | 1.93%                 | 1.54% |
| China          | 1.62%      | 1.23%                 | Kazakhstan  | 3.30%                 | 2.91%   | Slovakia       | 0.94%                 | 0.55% |
| Colombia       | 3.02%      | 2.63%                 | Korea       | 0.79%                 | 0.40%   | Slovenia       | 1.68%                 | 1.29% |
| Costa Rica     | 4.83%      | 4.44%                 | Latvia      | 1.29%                 | 0.90%   | South Africa   | 3.88%                 | 3.49% |
| Croatia        | 3.39%      | 3.00%                 | Lebanon     | 4.87%                 | 4.48%   | Spain          | 1.44%                 | 1.05% |
| Cyprus         | 3.10%      | 2.71%                 | Lithuania   | 1.29%                 | 0.90%   | Sweden         | 0.35%                 | 0.00% |
| Czech Republic | 0.93%      | 0.54%                 | Malaysia    | 2.50%                 | 2.11%   | Switzerland    | 0.42%                 | 0.03% |
| Denmark        | 0.39%      | 0.00%                 | Mexico      | 2.30%                 | 1.91%   | Thailand       | 2.00%                 | 1.61% |
| Egypt          | 5.27%      | 4.88%                 | Morocco     | 2.26%                 | 1.87%   | Tunisia        | 4.58%                 | 4.19% |
| Estonia        | 0.85%      | 0.46%                 | Netherlands | 0.37%                 | 0.00%   | Turkey         | 3.29%                 | 2.90% |
| Finland        | 0.46%      | 0.07%                 | New Zealand | 0.77%                 | 0.38%   | United Kingdom | 0.42%                 | 0.03% |
| France         | 0.60%      | 0.21%                 | Norway      | 0.35%                 | 0.00%   | United States  | <b>0.39%</b>          | 0.00% |
| Germany        | 0.34%      | 0.00%                 | Pakistan    | 5.92%                 | 5.53%   | Vietnam        | 3.53%                 | 3.14% |
| Hong Kong      | 0.78%      | 0.39%                 | Panama      | 2.33%                 | 1.94%   |                |                       |       |

# Approach 3: Typical Default Spreads: January 2016

| <i>Rating</i> | Default Spread (1/1/16) |
|---------------|-------------------------|
| Aaa           | 0                       |
| Aa1           | 44                      |
| Aa2           | 55                      |
| Aa3           | 67                      |
| A1            | 78                      |
| A2            | 94                      |
| A3            | 133                     |
| Baa1          | 177                     |
| Baa2          | 211                     |
| Baa3          | 244                     |
| Ba1           | 277                     |
| Ba2           | 333                     |
| Ba3           | 399                     |
| B1            | 499                     |
| B2            | 610                     |
| B3            | 721                     |
| Caa1          | 831                     |
| Caa2          | 998                     |
| Caa3          | 1108                    |
| Ca            | 1330                    |

# Getting to a risk free rate in a currency: Example

- □ The Brazilian government bond rate in nominal reas on January 1, 2016 was 16.51%. To get to a riskfree rate in nominal reas, we can use one of three approaches.
  - □ Approach 1: Government Bond spread
    - ❑ The 2021 Brazil bond, denominated in US dollars, has a spread of 4.83% over the US treasury bond rate.
    - ❑ Riskfree rate in \$R = 16.51% - 4.83% = 11.68%
  - □ Approach 2: The CDS Spread
    - ❑ The CDS spread for Brazil, adjusted for the US CDS spread was 5.19%.
    - ❑ Riskfree rate in \$R = 16.51% - 5.19% = 11.32%
  - □ Approach 3: The Rating based spread
    - ❑ Brazil has a Baa3 local currency rating from Moody's. The default spread for that rating is 2.44%
    - ❑ Riskfree rate in \$R = 16.51% - 2.44% = 14.07%

# Test 4: A Real Riskfree Rate

- ¨ In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms. ¨ To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination. ¨ In January 2016, the yield on a 10-year indexed treasury bond was 0.75%. Which of the following statements would you subscribe to?
  - a. This (0.75%) is the real riskfree rate to use, if you are valuing US companies in real terms.
  - b. This (0.75%) is the real riskfree rate to use, anywhere in the world

Explain.

### Why do risk free rates vary across currencies? January 2016 Risk free rates

![](_page_38_Figure_2.jpeg)

# Risk free Rate: Don't have or trust the government bond rate?

1. 1. Build up approach: The risk free rate in any currency can be written as the sum of two variables:

Risk free rate = Expected Inflation in currency + Expected real interest rate

The expected real interest rate can be computed in one of two ways: from the US TIPs rate or set equal to real growth in the economy. Thus, if the expected inflation rate in a country is expected to be 15% and the TIPs rate is 1%, the risk free rate is 16%.

1. 2. US \$ Rate & Differential Inflation: Alternatively, you can scale up the US \$ risk free rate by the differential inflation between the US \$ and the currency in question:

$$\text{Risk free rate}_{\text{Currency}} = \frac{(1 + \text{Risk free rate}_{\text{US \$}}) \frac{(1 + \text{Expected Inflation}_{\text{Foreign Currency}})}{(1 + \text{Expected Inflation}_{\text{US \$}})} - 1$$

Thus, if the US \$ risk free rate is 2.00%, the inflation rate in the foreign currency is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

$$\text{Risk free rate} = \frac{(1.02) \frac{(1.15)}{(1.015)} - 1}{(1.015)} = 15.57\%$$

# One more test on riskfree rates…

- ¨ On January 1, 2016, the 10-year treasury bond rate in the United States was 2.27%, a historic low. Assume that you were valuing a company in US dollars then, but were wary about the risk free rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate
  - c. Something else…

# Some perspective on risk free rates

![](_page_41_Figure_2.jpeg)

# Negative Interest Rates?

¨ In 2016, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates? ¨ How negative can rates get? (Is there a bound?) ¨ Would you use these negative interest rates as risk free rates? ¤ If no, why not and what would you do instead? ¤ If yes, what else would you have to do in your valuation to be internally consistent?

44

# Discount Rates: II

## The Equity Risk Premium

# The ubiquitous historical risk premium

¨ The historical premium is the premium that stocks have historically earned over riskless securities. ¨ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to ¤ How far back you go in history… ¤ Whether you use T.bill rates or T.Bond rates ¤ Whether you use geometric or arithmetic averages. ¨ For instance, looking at the US:

|           | <i>Arithmetic Average</i> | <i>Geometric Average</i> |                   |                   |
|-----------|---------------------------|--------------------------|-------------------|-------------------|
|           | Stocks - T. Bills         | Stocks - T. Bonds        | Stocks - T. Bills | Stocks - T. Bonds |
| 1928-2015 | 7.92%                     | 6.18%                    | 6.05%             | 4.54%             |
| Std Error | <i><b>2.15%</b></i>       | <i><b>2.29%</b></i>      |                   |                   |
| 1966-2015 | 6.05%                     | 3.89%                    | 4.69%             | 2.90%             |
| Std Error | <i><b>2.42%</b></i>       | <i><b>2.74%</b></i>      |                   |                   |
| 2006-2015 | 7.87%                     | 3.88%                    | 6.11%             | 2.53%             |
| Std Error | <i><b>6.06%</b></i>       | <i><b>8.66%</b></i>      |                   |                   |

# The perils of trusting the past.....

- □ Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 80 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

$$\text{Standard Error in Premium} = 20\%/\sqrt{80} = 2.26\%$$

- □ Survivorship Bias: Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

### Risk Premium for a Mature Market? Broadening the sample to 1900-2015

| Country       | Geometric	ERP | Arithmetic	ERP | Standard	Error |
|---------------|---------------|----------------|----------------|
| Australia     | 5.00%         | 6.60%          | 1.70%          |
| Austria       | 2.60%         | 21.50%         | 14.30%         |
| Belgium       | 2.40%         | 4.50%          | 2.00%          |
| Canada        | 3.30%         | 4.90%          | 1.70%          |
| Denmark       | 2.30%         | 3.80%          | 1.70%          |
| Finland       | 5.20%         | 8.80%          | 2.80%          |
| France        | 3.00%         | 5.40%          | 2.10%          |
| Germany       | 5.10%         | 9.10%          | 2.70%          |
| Ireland       | 2.80%         | 4.80%          | 1.80%          |
| Italy         | 3.10%         | 6.50%          | 2.70%          |
| Japan         | 5.10%         | 9.10%          | 3.00%          |
| Netherlands   | 3.30%         | 5.60%          | 2.10%          |
| New Zealand   | 4.00%         | 5.50%          | 1.70%          |
| Norway        | 2.30%         | 5.20%          | 2.60%          |
| South Africa  | 5.40%         | 7.20%          | 1.80%          |
| Spain         | 1.80%         | 3.80%          | 1.90%          |
| Sweden        | 3.10%         | 5.40%          | 2.00%          |
| Switzerland   | 2.10%         | 3.60%          | 1.60%          |
| U.K.          | 3.60%         | 5.00%          | 1.60%          |
| U.S.          | 4.30%         | 6.40%          | 1.90%          |
| Europe        | 3.20%         | 4.50%          | 1.50%          |
| World-ex U.S. | 2.80%         | 3.90%          | 1.40%          |
| World         | 3.20%         | 4.40%          | 1.40%          |

# The simplest way of estimating an additional country risk premium: The country default spread

- □ Default spread for country: In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - □ The default spread on a dollar denominated bond issued by the country. (In January 2016, that spread was 4.83% for the Brazilian \$ bond)
  - □ The sovereign CDS spread for the country. In January 2016, the ten year CDS spread for Brazil, adjusted for the US CDS, was 5.19%.
  - □ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Baa3 and the default spread for a Baa3 rated sovereign was about 2.44% in January 2016.
- □ Add the default spread to a “mature” market premium: This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 6.00%.
  - □ Country Risk Premium for Brazil = 2.44%
  - □ Total ERP for Brazil = 6.00% + 2.44% = 8.44%

### An equity volatility based approach to estimating the country total ERP

- ❑ This approach draws on the standard deviation of two equity markets, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ❑  $\text{Total equity risk premium} = \text{Risk Premium}_{\text{US}}^* \sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$
- ❑ The country equity risk premium is based upon the volatility of the market in question relative to U.S market.
  - ❑ Assume that the equity risk premium for the US is 6.00%.
  - ❑ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ❑  $\text{Total Equity Risk Premium for Brazil} = 6.00\% (30\%/18\%) = 10.0\%$
  - ❑  $\text{Country equity risk premium for Brazil} = 10.00\% - 6.00\% = 4.00\%$

— 49 —

### A melded approach to estimating the additional country risk premium

- ❑ Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
- ❑ Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. Using this approach for Brazil in January 2016, you would get:
  - ❑ Country Equity risk premium = Default spread on country bond\*  $\sigma_{\text{Country}}$   
     $\text{Equity} / \sigma_{\text{Country}} \text{ Bond}$ 
    - ■ Standard Deviation in Bovespa (Equity) = 30%
    - ■ Standard Deviation in Brazil government bond = 20%
    - ■ Default spread for Brazil = 2.44%
  - ❑ Brazil Country Risk Premium = 2.44% (30%/20%) = 3.66%
  - ❑ Brazil Total ERP = Mature Market Premium + CRP = 6.00% + 3.66% = 9.66%

# A Template for Country Risk

![](_page_50_Diagram_3.jpeg)

*Black #: Total ERP*

*Red #: Country risk premium*

|               |      | <i>Frontier Marques (not rated)</i> |        |                 |      |        |
|---------------|------|-------------------------------------|--------|-----------------|------|--------|
| Algeria       | 63.0 | 12.71%                              | 6.71%  | Malawi          | 57.0 | 17.17% |
| Brunei        | 72.8 | 14.84%                              | 2.84%  | Mali            | 62.5 | 12.71% |
| Gambia        | 62.0 | 14.20%                              | 8.20%  | Myanmar         | 63.3 | 12.71% |
| Guinea        | 53.8 | 17.17%                              | 11.17% | Niger           | 51.0 | 17.17% |
| Guinea-Bissau | 62.3 | 12.71%                              | 6.71%  | Sierra Leone    | 56.5 | 17.17% |
| Guyana        | 63.5 | 12.71%                              | 6.71%  | Somalia         | 42.5 | 20.90% |
| Haiti         | 57.0 | 17.17%                              | 11.17% | Sudan           | 48.3 | 20.90% |
| Iran          | 67.8 | 10.48%                              | 4.48%  | Syria           | 35.8 | 25.00% |
| Iraq          | 56.0 | 17.17%                              | 11.17% | Tanzania        | 63.0 | 12.71% |
| Korea, D.P.R. | 56.0 | 17.17%                              | 11.17% | Togo            | 63.8 | 12.71% |
| Liberia       | 50.5 | 17.17%                              | 11.17% | Yemen, Republic | 50.3 | 17.17% |
| Libya         | 51.8 | 14.20%                              | 11.17% | Zimbabwe        | 54.5 | 17.17% |
| Madagascar    | 62.3 | 14.20%                              | 8.20%  |                 |      |        |

| <span> </span> | Bangladesh      | 11.37%       | 5.37%        |
|----------------|-----------------|--------------|--------------|
| <span> </span> | Cambodia        | 14.20%       | 8.20%        |
| <span> </span> | China           | 6.90%        | 0.90%        |
| <span> </span> | Fiji            | 12.71%       | 6.71%        |
| <span> </span> | Hong Kong       | 6.59%        | 0.59%        |
| <span> </span> | India           | 9.28%        | 3.28%        |
| <span> </span> | Indonesia       | 9.28%        | 3.28%        |
| <span> </span> | Japan           | 7.05%        | 1.05%        |
| <span> </span> | Korea           | 6.74%        | 0.74%        |
| <span> </span> | Macao           | 6.74%        | 0.74%        |
| <span> </span> | Malaysia        | 7.79%        | 1.79%        |
| <span> </span> | Mauritius       | 8.38%        | 2.38%        |
| <span> </span> | Mongolia        | 14.20%       | 8.20%        |
| <span> </span> | Pakistan        | 15.70%       | 9.70%        |
| <span> </span> | Papua New Guine | 12.71%       | 6.71%        |
| <span> </span> | Philippines     | 8.84%        | 2.84%        |
| <span> </span> | Singapore       | 6.00%        | 0.00%        |
| <span> </span> | Sri Lanka       | 12.71%       | 6.71%        |
| <span> </span> | Taiwan          | 6.90%        | 0.90%        |
| <span> </span> | Thailand        | 8.38%        | 2.38%        |
| <span> </span> | Vietnam         | 12.71%       | 6.71%        |
| <span> </span> | Asia            | <b>7.49%</b> | <b>1.49%</b> |

| <span> </span>                             | <span> </span> Australia | <span> </span> 6,000% | <span> </span> 0,006%        | <span> </span> 0,006%        |
|--------------------------------------------|--------------------------|-----------------------|------------------------------|------------------------------|
| <span> </span> Cook Islands <span> </span> | <span> </span>           | <span> </span> 12,71% | <span> </span> 6,71%         | <span> </span> 6,71%         |
| <span> </span> New Zealand                 | <span> </span>           | <span> </span> 6,00%  | <span> </span> 0,00%         | <span> </span> 0,00%         |
| <b>Australia &amp; NZ</b>                  | <span> </span>           | <b>6,00%</b>          | <span> </span> <b>0,006%</b> | <span> </span> <b>0,006%</b> |

| Andorra     | 9.28%  | <b>3.28%</b>  | Jersey (States of)    | 6.59%        | <b>0.59%</b> |
|-------------|--------|---------------|-----------------------|--------------|--------------|
| Austria     | 6.00%  | <b>0.00%</b>  | Liechtenstein         | 6.00%        | <b>0.00%</b> |
| Belgium     | 6.90%  | <b>0.90%</b>  | Luxembourg            | 6.00%        | <b>0.00%</b> |
| Cyprus      | 12.71% | <b>6.71%</b>  | Malta                 | 7.79%        | <b>1.79%</b> |
| Denmark     | 6.00%  | <b>0.00%</b>  | Netherlands           | 6.00%        | <b>0.00%</b> |
| Finland     | 6.00%  | <b>0.00%</b>  | Norway                | 6.00%        | <b>0.00%</b> |
| France      | 6.74%  | <b>0.74%</b>  | Portugal              | 9.72%        | <b>2.72%</b> |
| Germany     | 6.00%  | <b>0.00%</b>  | Spain                 | 8.84%        | <b>2.84%</b> |
| Greece      | 20.90% | <b>14.90%</b> | Sweden                | 6.00%        | <b>0.00%</b> |
| Guernsey    | 6.59%  | <b>0.59%</b>  | Switzerland           | 6.00%        | <b>0.00%</b> |
| Iceland     | 8.84%  | <b>2.84%</b>  | Turkey                | 9.28%        | <b>2.8%</b>  |
| Ireland     | 8.38%  | <b>2.38%</b>  | United Kingdom        | 6.59%        | <b>0.59%</b> |
| Isle of Man | 6.59%  | <b>0.59%</b>  | <b>Western Europe</b> | <b>7.16%</b> | <b>1.16%</b> |
| Italy       | 8.84%  | <b>2.84%</b>  |                       |              |              |

| <span> </span> | Canada        | 6.00%  | 0.00%  |
|----------------|---------------|--------|--------|
| <span> </span> | US            | 6.00%  | 0.00%  |
| <span> </span> | North America | 6.00%  | 0.00%  |
| <span> </span> | Caribbean     | 14.61% | 8.61%  |
| <span> </span> | Argentina     | 17.17% | 11.17% |
| <span> </span> | Belize        | 19.42% | 13.42% |
| <span> </span> | Bolivia       | 11.37% | 5.37%  |
| <span> </span> | Brazil        | 9.28%  | 3.28%  |
| <span> </span> | Chile         | 6.90%  | 0.90%  |
| <span> </span> | Colombia      | 8.84%  | 2.84%  |
| <span> </span> | Costa Rica    | 9.72%  | 3.72%  |
| <span> </span> | Ecuador       | 15.70% | 9.70%  |
| <span> </span> | El Salvador   | 11.37% | 5.37%  |
| <span> </span> | Guatemala     | 9.72%  | 3.72%  |
| <span> </span> | Honduras      | 15.70% | 9.70%  |
| <span> </span> | Mexico        | 7.79%  | 1.79%  |
| <span> </span> | Nicaragua     | 14.20% | 8.20%  |
| <span> </span> | Panama        | 8.84%  | 2.84%  |
| <span> </span> | Paraguay      | 9.72%  | 3.72%  |
| <span> </span> | Peru          | 7.79%  | 1.79%  |
| <span> </span> | Suriname      | 11.37% | 5.37%  |
| <span> </span> | Uruguay       | 8.84%  | 2.84%  |
| <span> </span> | Venezuela     | 20.90% | 14.90% |
| <span> </span> | Latin America | 10.42% | 4.42%  |

| <i>Country</i>   | <i>ERP</i>    | <i>CRP</i>   |
|------------------|---------------|--------------|
| Angola           | 10.48%        | 4.48%        |
| Botswana         | 7.26%         | 1.26%        |
| Burkina Faso     | 15.70%        | 9.70%        |
| Cameroon         | 14.20%        | 8.20%        |
| Cape Verde       | 14.20%        | 8.20%        |
| Congo (DR        | 15.70%        | 9.70%        |
| Congo (Republic) | 11.13%        | 5.37%        |
| Côte d'Ivoire    | 11.37%        | 5.37%        |
| Egypt            | 15.70%        | 9.70%        |
| Ethiopia         | 12.71%        | 6.71%        |
| Gabon            | 11.37%        | 5.37%        |
| Ghana            | 15.70%        | 9.70%        |
| Kenya            | 12.71%        | 6.71%        |
| Morocco          | 9.72%         | 3.72%        |
| Mozambique       | 14.20%        | 8.20%        |
| Namibia          | 9.28%         | 3.28%        |
| Nigeria          | 11.37%        | 5.37%        |
| Rwanda           | 12.71%        | 6.71%        |
| Senegal          | 12.71%        | 6.71%        |
| South Africa     | 8.84%         | 2.84%        |
| Tunisia          | 11.37%        | 5.37%        |
| Uganda           | 12.71%        | 6.71%        |
| Zambia           | 14.20%        | 8.20%        |
| <b>Africa</b>    | <b>11.76%</b> | <b>5.76%</b> |

| Albania                            | 12.71%       | 6.71%        |
|------------------------------------|--------------|--------------|
| Armenia                            | 11.37%       | 5.37%        |
| Azerbaijan                         | 9.28%        | 3.28%        |
| Belarus                            | 17.17%       | 11.17%       |
| Bosnia                             | 15.70%       | 9.70%        |
| Bulgaria                           | 8.84%        | 2.84%        |
| Croatia                            | 9.72%        | 3.72%        |
| Czech Republic                     | 7.05%        | 1.05%        |
| Estonia                            | 7.05%        | 1.05%        |
| Georgia                            | 11.37%       | 5.37%        |
| Hungary                            | 9.72%        | 3.72%        |
| Kazakhstan                         | 8.84%        | 2.84%        |
| Latvia                             | 7.79%        | 1.79%        |
| Lithuania                          | 7.79%        | 1.79%        |
| Macedonia                          | 11.37%       | 5.37%        |
| Moldova                            | 15.70%       | 9.70%        |
| Montenegro                         | 11.37%       | 5.37%        |
| Poland                             | 7.26%        | 1.26%        |
| Romania                            | 9.28%        | 3.28%        |
| Russia                             | 9.72%        | 3.72%        |
| Serbia                             | 12.71%       | 6.71%        |
| Slovakia                           | 7.26%        | 1.26%        |
| Slovenia                           | 9.28%        | 3.28%        |
| Ukraine                            | 20.90%       | 14.90%       |
| <b>Eastern Europe &amp; Russia</b> | <b>9.67%</b> | <b>3.65%</b> |

| <span> </span> | <span> </span> Abu Dhabi            | <span> </span> 6.7%   | <span> </span> 0.74% |
|----------------|-------------------------------------|-----------------------|----------------------|
| <span> </span> | <span> </span> Bahrain              | <span> </span> 9.28%  | <span> </span> 3.28% |
| <span> </span> | <span> </span> Israel               | <span> </span> 7.05%  | <span> </span> 1.05% |
| <span> </span> | <span> </span> Jordan               | <span> </span> 12.71% | <span> </span> 6.71% |
| <span> </span> | <span> </span> Kuwait               | <span> </span> 6.74%  | <span> </span> 0.74% |
| <span> </span> | <span> </span> Lebanon              | <span> </span> 14.20% | <span> </span> 8.20% |
| <span> </span> | <span> </span> Oman                 | <span> </span> 7.05%  | <span> </span> 1.05% |
| <span> </span> | <span> </span> Qatar                | <span> </span> 6.74%  | <span> </span> 0.74% |
| <span> </span> | <span> </span> Ras Al Khaimah       | <span> </span> 7.26%  | <span> </span> 1.26% |
| <span> </span> | <span> </span> Saudi Arabia         | <span> </span> 6.90%  | <span> </span> 0.90% |
| <span> </span> | <span> </span> Sharjah              | <span> </span> 7.79%  | <span> </span> 1.79% |
| <span> </span> | <span> </span> United Arab Emirates | <span> </span> 6.74%  | <span> </span> 0.74% |
| <span> </span> | <span> </span> Middle East          | <span> </span> 7.41%  | <span> </span> 1.11% |

### From Country Equity Risk Premiums to Corporate Equity Risk premiums

¨ Approach 1: Assume that every company in the country is equally exposed to country risk. In this case, ¤ E(Return) = Riskfree Rate + CRP + Beta (Mature ERP) ¤ Implicitly, this is what you are assuming when you use the local Government' s dollar borrowing rate as your riskfree rate. ¨ Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk. ¤ E(Return) = Riskfree Rate + Beta (Mature ERP+ CRP) ¨ Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales) ¤ E(Return)=Riskfree Rate+ b (Mature ERP) + l (CRP)

Mature ERP = Mature market Equity Risk Premium

CRP = Additional country risk premium

### Approaches 1 & 2: Estimating country risk premium exposure

¨ Location based CRP: The standard approach in valuation is to attach a country risk premium to a company based upon its country of incorporation. Thus, if you are an Indian company, you are assumed to be exposed to the Indian country risk premium. A developed market company is assumed to be unexposed to emerging market risk. ¨ Operation-based CRP: There is a more reasonable modified version. The country risk premium for a company can be computed as a weighted average of the country risk premiums of the countries that it does business in, with the weights based upon revenues or operating income. If a company is exposed to risk in dozens of countries, you can take a weighted average of the risk premiums by region.

### Operation based CRP: Single versus Multiple Emerging Markets

¨ Single emerging market: Embraer, in 2004, reported that it derived 3% of its revenues in Brazil and the balance from mature markets. The mature market ERP in 2004 was 5% and Brazil's CRP was 7.89%.

| <span> </span>              | Revenues | Total ERP    | CRP           |
|-----------------------------|----------|--------------|---------------|
| US and other mature markets | 97%      | 5.00%        | 0.00%         |
| Brazil                      | 3%       | 12.89%       | 8%            |
| <b>Embraer</b>              |          | <b>5.24%</b> | <b>0.024%</b> |

¨ Multiple emerging markets: Ambev, the Brazilian-based beverage company, reported revenues from the following countries during 2011. 

|           | Revenues | %      | Total ERP    | CRP          |
|-----------|----------|--------|--------------|--------------|
| Argentina | 19       | 9.31%  | 15.00%       | 9.00%        |
| Bolivia   | 4        | 1.96%  | 10.88%       | 4.88%        |
| Brazil    | 130      | 63.73% | 8.63%        | 2.63%        |
| Canada    | 23       | 11.27% | 6.00%        | 0.00%        |
| Chile     | 7        | 3.43%  | 7.05%        | 1.05%        |
| Ecuador   | 6        | 2.94%  | 12.75%       | 6.75%        |
| Paraguay  | 3        | 1.47%  | 12.00%       | 6.00%        |
| Peru      | 12       | 5.88%  | 9.00%        | 3.00%        |
| Ambev     | 204      |        | <b>9.11%</b> | <b>3.11%</b> |

#### Extending to a multinational: Regional breakdown Coca Cola's revenue breakdown and ERP in 2012

Things to watch out for

- 1. Aggregation across regions. For instance, the Pacific region often includes Australia & NZ with Asia
- 2. Obscure aggregations including Eurasia and Oceania

| <i>Region</i>           | <i>Revenues</i> | <i>Total ERP</i> | <i>CRP</i> |
|-------------------------|-----------------|------------------|------------|
| Western Europe          | 19%             | 6.67%            | 0.67%      |
| Eastern Europe & Russia | 5%              | 8.60%            | 2.60%      |
| Asia                    | 15%             | 7.63%            | 1.63%      |
| Latin America           | 15%             | 9.42%            | 3.42%      |
| Australia               | 4%              | 6.00%            | 0.00%      |
| Africa                  | 4%              | 9.82%            | 3.82%      |
| North America           | 40%             | 6.00%            | 0.00%      |
| Coca Cola               | 100%            | 7.14%            | 1.14%      |

# Two problems with these approaches..

- □ Focus just on revenues: To the extent that revenues are the only variable that you consider, when weighting risk exposure across markets, you may be missing other exposures to country risk. For instance, an emerging market company that gets the bulk of its revenues outside the country (in a developed market) may still have all of its production facilities in the emerging market.
- □ Exposure not adjusted or based upon beta: To the extent that the country risk premium is multiplied by a beta, we are assuming that beta in addition to measuring exposure to all other macro economic risk also measures exposure to country risk.

# A Production-based ERP: Royal Dutch Shell in 2015

| Country               | Oil	&	Gas	Production | %	of	Total | ERP    |
|-----------------------|----------------------|------------|--------|
| Denmark               | 17396                | 3.83%      | 6.20%  |
| Italy                 | 11179                | 2.46%      | 9.14%  |
| Norway                | 14337                | 3.16%      | 6.20%  |
| UK                    | 20762                | 4.57%      | 6.81%  |
| Rest	of	Europe        | 874                  | 0.19%      | 7.40%  |
| Brunei                | 823                  | 0.18%      | 9.04%  |
| Iraq                  | 20009                | 4.40%      | 11.37% |
| Malaysia              | 22980                | 5.06%      | 8.05%  |
| Oman                  | 78404                | 17.26%     | 7.29%  |
| Russia                | 22016                | 4.85%      | 10.06% |
| Rest	of	Asia	&	ME     | 24480                | 5.39%      | 7.74%  |
| Oceania               | 7858                 | 1.73%      | 6.20%  |
| Gabon                 | 12472                | 2.75%      | 11.76% |
| Nigeria               | 67832                | 14.93%     | 11.76% |
| Rest	of	Africa        | 6159                 | 1.36%      | 12.17% |
| USA                   | 104263               | 22.95%     | 6.20%  |
| Canada                | 8599                 | 1.89%      | 6.20%  |
| Brazil                | 13307                | 2.93%      | 9.60%  |
| Rest	of	Latin	America | 576                  | 0.13%      | 10.78% |
| Royal	Dutch	Shell     | 454326               | 100.00%    | 8.26%  |

### Approach 3: Estimate a lambda for country risk

¨ Country risk exposure is affected by where you get your revenues and where your production happens, but there are a host of other variables that also affect this exposure, including: ¤ Use of risk management products: Companies can use both options/futures markets and insurance to hedge some or a significant portion of country risk. ¤ Government "national" interests: There are sectors that are viewed as vital to the national interests, and governments often play a key role in these companies, either officially or unofficially. These sectors are more exposed to country risk. ¨ It is conceivable that there is a richer measure of country risk that incorporates all of the variables that drive country risk in one measure. That way my rationale when I devised "lambda" as my measure of country risk exposure.

# A Revenue-based Lambda

- The factor “λ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:

 $\lambda$  = % of revenues domestically  $_{\text{firm}}/$  % of revenues domestically  $_{\text{average firm}}$ 

 Consider two firms – Tata Motors and Tata Consulting Services, both Indian companies. In 2008-09, Tata Motors got about 91.37% of its revenues in India and TCS got 7.62%. The average Indian firm gets about 80% of its revenues in India:

$$\lambda_{\text{Tata Motors}} = 91\%/80\% = 1.14$$

$$\lambda_{\text{TCS}} = 7.62\%/80\% = 0.09$$

- □ There are two implications
  - ■ A company's risk exposure is determined by where it does business and not by where it is incorporated.
  - ■ Firms might be able to actively manage their country risk exposures

#### A Price/Return based Lambda

Embraer versus C Bond: 2000-2003

![](_page_60_Figure_5.jpeg)

Embratel versus C Bond: 2000-2003

![](_page_60_Figure_7.jpeg)

ReturnEmbraer = 0.0195 + **0.2681** ReturnCBond

ReturnEmbratel = -0.0308 + **2.0030** ReturnCBond

### Estimating a US Dollar Cost of Equity for Embraer - September 2004

¨ Assume that the beta for Embraer is 1.07, and that the US \$ riskfree rate used is 4%. Also assume that the risk premium for the US is 5% and the country risk premium for Brazil is 7.89%. Finally, assume that Embraer gets 3% of its revenues in Brazil & the rest in the US. ¨ There are five estimates of \$ cost of equity for Embraer: ¤ Approach 1: Constant exposure to CRP, Location CRP n E(Return) = 4% + 1.07 (5%) + 7.89% = 17.24% ¤ Approach 2: Constant exposure to CRP, Operation CRP n E(Return) = 4% + 1.07 (5%) + (0.03\*7.89% +0.97\*0%)= 9.59% ¤ Approach 3: Beta exposure to CRP, Location CRP n E(Return) = 4% + 1.07 (5% + 7.89%)= 17.79% ¤ Approach 4: Beta exposure to CRP, Operation CRP n E(Return) = 4% + 1.07 (5% +( 0.03\*7.89%+0.97\*0%)) = 9.60% ¤ Approach 5: Lambda exposure to CRP n E(Return) = 4% + 1.07 (5%) + 0.27(7.89%) = 11.48%

### Valuing Emerging Market Companies with significant exposure in developed markets

- ¨ The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk. Thus, in 2004, Embraer would have been valued with a cost of equity of 17-18% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
- a. Emerging market companies with substantial exposure in developed markets will be significantly over valued by equity research analysts.
- b. Emerging market companies with substantial exposure in developed markets will be significantly under valued by equity research analysts.

Can you construct an investment strategy to take advantage of the misvaluation? What would need to happen for you to make money of this strategy?

# Implied Equity Premiums

¨ Let's start with a general proposition. If you know the price paid for an asset and have estimates of the expected cash flows on the asset, you can estimate the IRR of these cash flows. If you paid the price, this is what you have priced the asset to earn (as an expected return). ¨ If you assume that stocks are correctly priced in the aggregate and you can estimate the expected cashflows from buying stocks, you can estimate the expected rate of return on stocks by finding that discount rate that makes the present value equal to the price paid. Subtracting out the riskfree rate should yield an implied equity risk premium. ¨ This implied equity premium is a forward looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

# Implied Equity Premiums: January 2008

¨ We can use the information in stock prices to back out how risk averse the market is and how much of a risk premium it is demanding.

¨ If you pay the current level of the index, you can expect to make a return of 8.39% on stocks (which is obtained by solving for r in the following equation)

¨ Implied Equity risk premium = Expected return on stocks - Treasury bond rate = 8.39% - 4.02% = 4.37%

$$1468.36 = \frac{61.98}{(1+r)} + \frac{65.08}{(1+r)^2} + \frac{68.33}{(1+r)^3} + \frac{71.75}{(1+r)^4} + \frac{75.34}{(1+r)^5} + \frac{75.35(1.0402)}{(r-.0402)(1+r)^5}$$

![](_page_64_Figure_6.jpeg)

Between 2001 and 2007 dividends and stock buybacks averaged 4.02% of the index each year.

Analysts expect earnings to grow 5% a year for the next 5 years. We will assume that dividends & buybacks will keep pace.. Last year's cashflow (59.03) growing at 5% a year

After year 5, we will assume that earnings on the index will grow at 4.02%, the same rate as the entire economy (= riskfree rate).

### A year that made a difference.. The implied premium in January 2009

| Year       | Market value of index | Dividends | Buybacks | Cash to equity | Dividend yield | Buyback yield | Total yield |
|------------|-----------------------|-----------|----------|----------------|----------------|---------------|-------------|
| 2001       | 1148.09               | 15.74     | 14.34    | 30.08          | 1.37%          | 1.25%         | 2.62%       |
| 2002       | 879.82                | 15.96     | 13.87    | 29.83          | 1.81%          | 1.58%         | 3.39%       |
| 2003       | 1111.91               | 17.88     | 13.70    | 31.58          | 1.61%          | 1.23%         | 2.84%       |
| 2004       | 1211.92               | 19.01     | 21.59    | 40.60          | 1.57%          | 1.78%         | 3.35%       |
| 2005       | 1248.29               | 22.34     | 38.82    | 61.17          | 1.79%          | 3.11%         | 4.90%       |
| 2006       | 1418.30               | 25.04     | 48.12    | 73.16          | 1.77%          | 3.39%         | 5.16%       |
| 2007       | 1468.36               | 28.14     | 67.22    | 95.36          | 1.92%          | 4.58%         | 6.49%       |
| 2008       | 903.25                | 28.47     | 40.25    | 68.72          | 3.15%          | 4.61%         | 7.77%       |
| Normalized | 903.25                | 28.47     | 24.11    | 52.584         | 3.15%          | 2.67%         | 5.82%       |

January 1, 2009

S&P 500 is at 903.25

Adjusted Dividends &

Buybacks for 2008 = 52.58

*In 2008, the actual cash returned to stockholders was 68.72. However, there was a 41% dropoff in buybacks in Q4. We reduced the total buybacks for the year by that amount.*

Analysts expect earnings to grow 4% a year for the next 5 years. We will assume that dividends & buybacks will keep pace.. Last year's cashflow (52.58) growing at 4% a year

After year 5, we will assume that earnings on the index will grow at 2.21%, the same rate as the entire economy (= riskfree rate).

54.69 56.87 59.15 61.52 63.98

Expected Return on Stocks (1/1/09) = 8.64%

Riskfree rate = 2.21%

Equity Risk Premium = 6.43%

| $903.25 = \frac{54.69}{(1+r)} + \frac{56.87}{(1+r)^2} + \frac{59.15}{(1+r)^3} + \frac{61.52}{(1+r)^4} + \frac{63.98}{(1+r)^5} + \frac{63.98(1.0221)}{(r-.0221)(1+r)^6}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### The Anatomy of a Crisis: Implied ERP from September 12, 2008 to January 1, 2009

![](_page_66_Figure_2.jpeg)

# An Updated Equity Risk Premium: January 2016

![](_page_67_Diagram_2.jpeg)

# Implied Premiums in the US: 1960-2015

![](_page_68_Figure_2.jpeg)

*Implied Premium for US Equity Market: 1960-2015*

# A Buyback Adjusted Version of the US ERP

![](_page_69_Diagram_2.jpeg)

# Implied Premium versus Risk Free Rate

![](_page_70_Figure_2.jpeg)

### Equity Risk Premiums and Bond Default Spreads

![](_page_71_Figure_3.jpeg)

*Equity Risk Premiums and Bond Default Spreads*

### Equity Risk Premiums and Cap Rates (Real Estate)

![](_page_72_Figure_3.jpeg)

# Why implied premiums matter?

- ¨ In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. If all analysts in the department used the arithmetic average premium (for stocks over T.Bills) for 1928-2015 of 7.92% to value stocks in January 2014, given the implied premium of 6.12%, what are they likely to find?
- a. The values they obtain will be too low (most stocks will look overvalued)
- b. The values they obtain will be too high (most stocks will look under valued)
- c. There should be no systematic bias as long as they use the same premium to value all stocks.

### Which equity risk premium should you use?

#### **If you assume this Premium to use**

Premiums revert back to historical norms and your time period yields these norms

Historical risk premium

Market is correct in the aggregate or that your valuation should be market neutral

Current implied equity risk premium

Marker makes mistakes even in the aggregate but is correct over time

Average implied equity risk premium over time.

| Predictor                             | Correlation with implied premium next year | Correlation with return-next 5 years | Correlation with actual next 10 years |
|---------------------------------------|--------------------------------------------|--------------------------------------|---------------------------------------|
| Current implied premium               | 0.750                                      | 0.475                                | 0.541                                 |
| Average implied premium: Last 5 years | 0.703                                      | 0.541                                | 0.747                                 |
| Historical Premium                    | -0.476                                     | -0.442                               | -0.469                                |
| Default Spread based premium          | 0.035                                      | 0.234                                | 0.225                                 |

# An ERP for the Sensex

¨ Inputs for the computation ¤ Sensex on 9/5/07 = 15446 ¤ Dividend yield on index = 3.05% ¤ Expected growth rate - next 5 years = 14% ¤ Growth rate beyond year 5 = 6.76% (set equal to riskfree rate) ¨ Solving for the expected return:

¨ Expected return on stocks = 11.18% ¨ Implied equity risk premium for India = 11.18% - 6.76% = 4.42%

$$15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$$

# Changing Country Risk: Brazil CRP & Total ERP from 2000 to 2015

![](_page_76_Figure_3.jpeg)

# The evolution of Emerging Market Risk

| Start	of	year | PBV Developed | PBV Emerging | ROE Developed | ROE Emerging | US	T.Bond rate | Growth Rate Developed | Growth Rate Emerging | Cost	of Equity (Developed) | Cost	of Equity (Emerging) | Differential ERP |
|---------------|---------------|--------------|---------------|--------------|----------------|-----------------------|----------------------|----------------------------|---------------------------|------------------|
| 2004          | 2.00          | 1.19         | 10.81%        | 11.65%       | 4.25%          | 3.75%                 | 5.25%                | 7.28%                      | 10.63%                    | 3.35%            |
| 2005          | 2.09          | 1.27         | 11.12%        | 11.93%       | 4.22%          | 3.72%                 | 5.22%                | 7.26%                      | 10.50%                    | 3.24%            |
| 2006          | 2.03          | 1.44         | 11.32%        | 12.18%       | 4.39%          | 3.89%                 | 5.39%                | 7.55%                      | 10.11%                    | 2.56%            |
| 2007          | 1.67          | 1.67         | 10.87%        | 12.88%       | 4.70%          | 4.20%                 | 5.70%                | 8.19%                      | 10.00%                    | 1.81%            |
| 2008          | 0.87          | 0.83         | 9.42%         | 11.12%       | 4.02%          | 3.52%                 | 5.02%                | 10.30%                     | 12.37%                    | 2.07%            |
| 2009          | 1.20          | 1.34         | 8.48%         | 11.02%       | 2.21%          | 1.71%                 | 3.21%                | 7.35%                      | 9.04%                     | 1.69%            |
| 2010          | 1.39          | 1.43         | 9.14%         | 11.22%       | 3.84%          | 3.34%                 | 4.84%                | 7.51%                      | 9.30%                     | 1.79%            |
| 2011          | 1.12          | 1.08         | 9.21%         | 10.04%       | 3.29%          | 2.79%                 | 4.29%                | 8.52%                      | 9.61%                     | 1.09%            |
| 2012          | 1.17          | 1.18         | 9.10%         | 9.33%        | 1.88%          | 1.38%                 | 2.88%                | 7.98%                      | 8.35%                     | 0.37%            |
| 2013          | 1.56          | 1.63         | 8.67%         | 10.48%       | 1.76%          | 1.26%                 | 2.76%                | 6.02%                      | 7.50%                     | 1.48%            |
| 2014          | 1.95          | 1.50         | 9.27%         | 9.64%        | 3.04%          | 2.54%                 | 4.04%                | 6.00%                      | 7.77%                     | 1.77%            |
| 2015          | 1.88          | 1.56         | 9.69%         | 9.75%        | 2.17%          | 1.67%                 | 3.17%                | 5.94%                      | 7.39%                     | 1.45%            |
| 2016          | 1.89          | 1.59         | 9.24%         | 10.16%       | 2.27%          | 1.77%                 | 3.27%                | 5.72%                      | 7.60%                     | 1.88%            |

79

# Discount Rates: III

## Relative Risk Measures

# The CAPM Beta: The Most Used (and Misused) Risk Measure

¨ The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm) -

Rj = a + b Rm

where a is the intercept and b is the slope of the regression. 

¨ The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock. 

¨ This beta has three problems:

- It has high standard error
- It reflects the firm's business mix over the period of the regression, not the current mix
- It reflects the firm's average financial leverage over the period rather than the current leverage.

# Unreliable, when it looks bad..

![](_page_80_Figure_2.jpeg)

# Or when it looks good..

![](_page_81_Figure_24.jpeg)

# One slice of history..

**83**

![](_page_82_Figure_2.jpeg)

During this time period, Valeant was a stock under siege, without a CEO, under legal pressure & lacking financials.

![](_page_82_Figure_4.jpeg)

# And subject to game playing

![](_page_83_Figure_20.jpeg)

![](_page_83_Figure_21.jpeg)

### Measuring Relative Risk: You don't like betas or modern portfolio theory? No problem.

![](_page_84_Diagram_2.jpeg)

# Don't like the diversified investor focus, but okay with price-based measures

86

## 1. Relative Standard Deviation

- • Relative Volatility = Std dev of Stock/ Average Std dev across all stocks
- • Captures all risk, rather than just market risk

## 2. Proxy Models

- • Look at historical returns on all stocks and look for variables that explain differences in returns.
- • You are, in effect, running multiple regressions with returns on individual stocks as the dependent variable and fundamentals about these stocks as independent variables.
- • This approach started with market cap (the small cap effect) and over the last two decades has added other variables (momentum, liquidity etc.)

## 3. CAPM Plus Models

- • Start with the traditional CAPM ( $R_f + Beta (ERP)$ ) and then add other premiums for proxies.

# Don't like the price-based approach..

- 1. Accounting risk measures: To the extent that you don't trust market-priced based measures of risk, you could compute relative risk measures based on
  - Accounting earnings volatility: Compute an accounting beta or relative volatility
  - Balance sheet ratios: You could compute a risk score based upon accounting ratios like debt ratios or cash holdings (akin to default risk scores like the Z score)
- 2. Qualitative Risk Models: In these models, risk assessments are based at least partially on qualitative factors (quality of management).
- 3. Debt based measures: You can estimate a cost of equity, based upon an observable costs of debt for the company.
  - Cost of equity = Cost of debt \* Scaling factor
  - The scaling factor can be computed from implied volatilities.

# Determinants of Betas & Relative Risk

![](_page_87_Diagram_2.jpeg)

In a perfect world… we would estimate the beta of a firm by doing the following

Start with the beta of the business that the firm is in

Adjust the business beta for the operating leverage of the firm to arrive at the unlevered beta for the firm.

Use the financial leverage of the firm to estimate the equity beta for the firm Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (Debt/Equity))

# Adjusting for operating leverage…

¨ Within any business, firms with lower fixed costs (as a percentage of total costs) should have lower unlevered betas. If you can compute fixed and variable costs for each firm in a sector, you can break down the unlevered beta into business and operating leverage components. ¤ Unlevered beta = Pure business beta \* (1 + (Fixed costs/ Variable costs)) ¨ The biggest problem with doing this is informational. It is difficult to get information on fixed and variable costs for individual firms. ¨ In practice, we tend to assume that the operating leverage of firms within a business are similar and use the same unlevered beta for every firm. 

# Adjusting for financial leverage…

¨ Conventional approach: If we assume that debt carries no market risk (has a beta of zero), the beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\arccos_L = \arccos_U (1 + ((1-t)D/E))$$

In some versions, the tax effect is ignored and there is no (1-t) in the equation.

¨ Debt Adjusted Approach: If beta carries market risk and you can estimate the beta of debt, you can estimate the levered beta as follows:

$$\phi_L = \phi_u (1 + ((1-t)D/E)) - \phi_{debt} (1-t) (D/E)$$

While the latter is more realistic, estimating betas for debt can be difficult to do. 

# Bottom-up Betas

Step 1: Find the business or businesses that your firm operates in.

![](_page_91_Diagram_3.jpeg)

Step 2: Find publicly traded firms in each of these businesses and obtain their regression betas. Compute the simple average across these regression betas to arrive at an average beta for these publicly traded firms. Unlever this average beta using the average debt to equity ratio across the publicly traded firms in the sample. Unlevered beta for business = Average beta across publicly traded firms/ (1 + (1- t) (Average D/E ratio across firms))

![](_page_91_Diagram_5.jpeg)

If you can, adjust this beta for differences between your firm and the comparable firms on operating leverage and product characteristics.

Step 3: Estimate how much value your firm derives from each of the different businesses it is in.

![](_page_91_Diagram_7.jpeg)

While revenues or operating income are often used as weights, it is better to try to estimate the value of each business.

Step 4: Compute a weighted average of the unlevered betas of the different businesses (from step 2) using the weights from step 3. Bottom-up Unlevered beta for your firm = Weighted average of the unlevered betas of the individual business

![](_page_91_Diagram_9.jpeg)

Step 5: Compute a levered beta (equity beta) for your firm, using the market debt to equity ratio for your firm.

Levered bottom-up beta = Unlevered beta (1+ (1-t) (Debt/Equity))

If you expect the business mix of your firm to change over time, you can change the weights on a year-to-year basis.

If you expect your debt to equity ratio to change over time, the levered beta will change over time.

#### *Possible Refinements*

# Why bottom-up betas?

¨ The standard error in a bottom-up beta will be significantly lower than the standard error in a single regression beta. Roughly speaking, the standard error of a bottom-up beta estimate can be written as follows:

Std error of bottom-up beta = 
$$\frac{\text{Average Std Error across Betas}}{\sqrt{\text{Number of firms in sample}}}$$

¨ The bottom-up beta can be adjusted to reflect changes in the firm's business mix and financial leverage. Regression betas reflect the past. ¨ You can estimate bottom-up betas even when you do not have historical stock prices. This is the case with initial public offerings, private businesses or divisions of companies.

# Estimating Bottom Up Betas & Costs of Equity: Vale

| Business Metals'&' | Sample Global'firms'in'metals'&' mining,'Market'cap>\$1' | Sample' size | Unlevered'beta' of'business | Revenues | Peer'Group' EV/Sales | Value'of' Business | Proportion'of' Vale |
|--------------------|----------------------------------------------------------|--------------|-----------------------------|----------|----------------------|--------------------|---------------------|
| Mining             | billion                                                  | 48           | 0.86                        | \$9,013  | 1.97                 | \$17,739           | 16.65%              |
| Iron'Ore           | Global'firms'in iron'ore Global'specialty'               | 78           | 0.83                        | \$32,717 | 2.48                 | \$81,188           | 76.20%              |
| Fertilizers        | chemical firms Global'transportation                     | 693          | 0.99                        | \$3,777  | 1.52                 | \$5,741            | 5.39%               |
| Logistics Vale'    | firms                                                    | 223          | 0.75                        | \$1,644  | 1.14                 | \$1,874            | 1.76%               |
| Operations         |                                                          |              | 0.8440                      | \$47,151 |                      | \$106,543          | 100.00%             |

| Business        | Unlevered beta | D/E ratio | Levered beta | Risk free rate | ERP   | Cost of Equity |
|-----------------|----------------|-----------|--------------|----------------|-------|----------------|
| Metals & Mining | 0.86           | 54.99%    | 1.1657       | 2.75%          | 7.38% | 11.35%         |
| Iron Ore        | 0.83           | 54.99%    | 1.1358       | 2.75%          | 7.38% | 11.13%         |
| Fertilizers     | 0.99           | 54.99%    | 1.3493       | 2.75%          | 7.38% | 12.70%         |
| Logistics       | 0.75           | 54.99%    | 1.0222       | 2.75%          | 7.38% | 10.29%         |
| Vale Operations | 0.84           | 54.99%    | 1.1503       | 2.75%          | 7.38% | 11.23%         |

# Embraer's Bottom-up Beta

| Business  | Unlevered Beta D/E Ratio | Levered beta |
|-----------|--------------------------|--------------|
| Aerospace | 0.95                     | 1.07         |

- ¨ Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (D/E Ratio) = 0.95 ( 1 + (1-.34) (.1895)) = 1.07 ¨ Can an unlevered beta estimated using U.S. and European aerospace companies be used to estimate the beta for a Brazilian aerospace company?
- a. Yes
- b. No What concerns would you have in making this assumption?

# Gross Debt versus Net Debt Approaches

¨ Analysts in Europe and Latin America often take the difference between debt and cash (net debt) when computing debt ratios and arrive at very different values. ¨ For Embraer, using the gross debt ratio ¤ Gross D/E Ratio for Embraer = 1953/11,042 = 18.95% ¤ Levered Beta using Gross Debt ratio = 1.07 ¨ Using the net debt ratio, we get ¤ Net Debt Ratio for Embraer = (Debt - Cash)/ Market value of Equity = (1953-2320)/ 11,042 = -3.32% ¤ Levered Beta using Net Debt Ratio = 0.95 (1 + (1-.34) (-.0332)) = 0.93 ¨ The cost of Equity using net debt levered beta for Embraer will be much lower than with the gross debt approach. The cost of capital for Embraer will even out since the debt ratio used in the cost of capital equation will now be a net debt ratio rather than a gross debt ratio.

# The Cost of Equity: A Recap

![](_page_96_Diagram_2.jpeg)

Mopping up

# **<sup>98</sup>** Discount Rates: IV

# Estimating the Cost of Debt

¨ The cost of debt is the rate at which you can borrow at currently, It will reflect not only your default risk but also the level of interest rates in the market. ¨ The two most widely used approaches to estimating cost of debt are: ¤ Looking up the yield to maturity on a straight bond outstanding from the firm. The limitation of this approach is that very few firms have long term straight bonds that are liquid and widely traded ¤ Looking up the rating for the firm and estimating a default spread based upon the rating. While this approach is more robust, different bonds from the same firm can have different ratings. You have to use a median rating for the firm ¨ When in trouble (either because you have no ratings or multiple ratings for a firm), estimate a synthetic rating for your firm and the cost of debt based upon that rating.

# Estimating Synthetic Ratings

¨ The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

¨ For Embraer's interest coverage ratio, we used the interest expenses from 2003 and the average EBIT from 2001 to 2003. (The aircraft business was badly affected by 9/11 and its aftermath. In 2002 and 2003, Embraer reported significant drops in operating income)

Interest Coverage Ratio = 462.1 /129.70 = 3.56

### Interest Coverage Ratios, Ratings and Default Spreads: 2003 & 2004

| If	Interest	Coverage	Ratio	is |        |            | Estimated	Bond	Rating | Default	Spread(2003) | Default	Spread(2004) |
|-------------------------------|--------|------------|-----------------------|----------------------|----------------------|
| >	8.50                        |        | (>12.50)   | AAA                   | 0.75%                | 0.35%                |
| 6.50	-                        | 8.50   | (9.5-12.5) | AA                    | 1.00%                | 0.50%                |
| 5.50	-                        | 6.50   | (7.5-9.5)  | A+                    | 1.50%                | 0.70%                |
| 4.25	-                        | 5.50   | (6-7.5)    | A                     | 1.80%                | 0.85%                |
| 3.00	-                        | 4.25   | (4.5-6)    | A–                    | 2.00%                | 1.00%                |
| 2.50	-                        | 3.00   | (4-4.5)    | BBB                   | 2.25%                | 1.50%                |
| 2.25-                         | 2.50   | (3.5-4)    | BB+                   | 2.75%                | 2.00%                |
| 2.00	-                        | 2.25   | ((3-3.5)   | BB                    | 3.50%                | 2.50%                |
| 1.75	-                        | 2.00   | (2.5-3)    | B+                    | 4.75%                | 3.25%                |
| 1.50	-                        | 1.75   | (2-2.5)    | B                     | 6.50%                | 4.00%                |
| 1.25	-                        | 1.50   | (1.5-2)    | B	–                   | 8.00%                | 6.00%                |
| 0.80	-                        | 1.25   | (1.25-1.5) | CCC                   | 10.00%               | 8.00%                |
| 0.65	-                        | 0.80   | (0.8-1.25) | CC                    | 11.50%               | 10.00%               |
| 0.20	-                        | 0.65   | (0.5-0.8)  | C                     | 12.70%               | 12.00%               |
| <	0.20                        | (<0.5) | D          |                       | 15.00%               | 20.00%               |

¨ The first number under interest coverage ratios is for larger market cap companies and the second in brackets is for smaller market cap companies. For Embraer , I used the interest coverage ratio table for smaller/riskier firms (the numbers in brackets) which yields a lower rating for the same interest coverage ratio.

# Cost of Debt computations

¨ Companies in countries with low bond ratings and high default risk might bear the burden of country default risk, especially if they are smaller or have all of their revenues within the country. ¨ Larger companies that derive a significant portion of their revenues in global markets may be less exposed to country default risk. In other words, they may be able to borrow at a rate lower than the government. ¨ The synthetic rating for Embraer is A-. Using the 2004 default spread of 1.00%, we estimate a cost of debt of 9.29% (using a riskfree rate of 4.29% and adding in two thirds of the country default spread of 6.01%):

#### Cost of debt

= Riskfree rate + 2/3(Brazil country default spread) + Company default spread =4.29% + 4.00%+ 1.00% = 9.29%

# Synthetic Ratings: Some Caveats

¨ The relationship between interest coverage ratios and ratings, developed using US companies, tends to travel well, as long as we are analyzing large manufacturing firms in markets with interest rates close to the US interest rate ¨ They are more problematic when looking at smaller companies in markets with higher interest rates than the US. One way to adjust for this difference is modify the interest coverage ratio table to reflect interest rate differences (For instances, if interest rates in an emerging market are twice as high as rates in the US, halve the interest coverage ratio.

| Rating    | 1-Jan-08 | Default spread over treasury 12-Sep-08 | 12-Nov-08 | 1-Jan-09 | 1-Jan-10 | 1-Jan-11 |
|-----------|----------|----------------------------------------|-----------|----------|----------|----------|
| Aaa/AAA   | 0.99%    | 1.40%                                  | 2.15%     | 2.00%    | 0.50%    | 0.55%    |
| Aa1/AA+   | 1.15%    | 1.45%                                  | 2.30%     | 2.25%    | 0.55%    | 0.60%    |
| Aa2/AA    | 1.25%    | 1.50%                                  | 2.55%     | 2.50%    | 0.65%    | 0.65%    |
| Aa3/AA-   | 1.30%    | 1.65%                                  | 2.80%     | 2.75%    | 0.70%    | 0.75%    |
| A1/A+     | 1.35%    | 1.85%                                  | 3.25%     | 3.25%    | 0.85%    | 0.85%    |
| A2/A      | 1.42%    | 1.95%                                  | 3.50%     | 3.50%    | 0.90%    | 0.90%    |
| A3/A-     | 1.48%    | 2.15%                                  | 3.75%     | 3.75%    | 1.05%    | 1.00%    |
| Baa1/BBB+ | 1.73%    | 2.65%                                  | 4.50%     | 5.25%    | 1.65%    | 1.40%    |
| Baa2/BBB  | 2.02%    | 2.90%                                  | 5.00%     | 5.75%    | 1.80%    | 1.60%    |
| Baa3/BBB- | 2.60%    | 3.20%                                  | 5.75%     | 7.25%    | 2.25%    | 2.05%    |
| Ba1/BB+   | 3.20%    | 4.45%                                  | 7.00%     | 9.50%    | 3.50%    | 2.90%    |
| Ba2/BB    | 3.65%    | 5.15%                                  | 8.00%     | 10.50%   | 3.85%    | 3.25%    |
| Ba3/BB-   | 4.00%    | 5.30%                                  | 9.00%     | 11.00%   | 4.00%    | 3.50%    |
| B1/B+     | 4.55%    | 5.85%                                  | 9.50%     | 11.50%   | 4.25%    | 3.75%    |
| B2/B      | 5.65%    | 6.10%                                  | 10.50%    | 12.50%   | 5.25%    | 5.00%    |
| B3/B-     | 6.45%    | 9.40%                                  | 13.50%    | 15.50%   | 5.50%    | 6.00%    |
| Caa/CCC+  | 7.15%    | 9.80%                                  | 14.00%    | 16.50%   | 7.75%    | 7.75%    |
| ERP       | 4.37%    | 4.52%                                  | 6.30%     | 6.43%    | 4.36%    | 5.20%    |

### Default Spreads: The effect of the crisis of 2008.. And the aftermath

# Updated Default Spreads - January 2016

![](_page_104_Figure_2.jpeg)

# Subsidized Debt: What should we do?

- ¨ Assume that the Brazilian government lends money to Embraer at a subsidized interest rate (say 6% in dollar terms). In computing the cost of capital to value Embraer, should be we use the cost of debt based upon default risk or the subsidized cost of debt?
- a. The subsidized cost of debt (6%). That is what the company is paying.
- b. The fair cost of debt (9.25%). That is what the company should require its projects to cover.
- c. A number in the middle.

### Weights for the Cost of Capital Computation

- ¨ In computing the cost of capital for a publicly traded firm, the general rule for computing weights for debt and equity is that you use market value weights (and not book value weights). Why?
  - a. Because the market is usually right
  - b. Because market values are easy to obtain
  - c. Because book values of debt and equity are meaningless
  - d. None of the above

### Estimating Cost of Capital: Embraer in 2004

#### ¨ Equity

¤ Cost of Equity = 4.29% + 1.07 (4%) + 0.27 (7.89%) = 10.70% ¤ Market Value of Equity =11,042 million BR (\$ 3,781 million)

#### ¨ Debt

¤ Cost of debt = 4.29% + 4.00% +1.00%= 9.29% ¤ Market Value of Debt = 2,083 million BR (\$713 million)

#### ¨ Cost of Capital

Cost of Capital = 10.70 % (.84) + 9.29% (1- .34) (0.16)) = 9.97%

¤ The book value of equity at Embraer is 3,350 million BR. ¤ The book value of debt at Embraer is 1,953 million BR; Interest expense is 222 mil BR; Average maturity of debt = 4 years ¤ Estimated market value of debt = 222 million (PV of annuity, 4 years, 9.29%) + \$1,953 million/1.09294 = 2,083 million BR

#### If you had to do it….Converting a Dollar Cost of Capital to a Nominal Real Cost of Capital

¨ Approach 1: Use a BR riskfree rate in all of the calculations above. For instance, if the BR riskfree rate was 12%, the cost of capital would be computed as follows: ¤ Cost of Equity = 12% + 1.07(4%) + 0.27 (7. 89%) = 18.41% ¤ Cost of Debt = 12% + 1% = 13% ¤ (This assumes the riskfree rate has no country risk premium embedded in it.) ¨ Approach 2: Use the differential inflation rate to estimate the cost of capital. For instance, if the inflation rate in BR is 8% and the inflation rate in the U.S. is 2%

$$\text{Cost of capital} = (1 + \text{Cost of Capital}_{\$}) \left[ \frac{1 + \text{Inflation}_{\text{BR}}}{1 + \text{Inflation}_{\$}} \right]$$

= 1.0997 (1.08/1.02)-1 = 0.1644 or 16.44%

# Dealing with Hybrids and Preferred Stock

¨ When dealing with hybrids (convertible bonds, for instance), break the security down into debt and equity and allocate the amounts accordingly. Thus, if a firm has \$ 125 million in convertible debt outstanding, break the \$125 million into straight debt and conversion option components. The conversion option is equity. ¨ When dealing with preferred stock, it is better to keep it as a separate component. The cost of preferred stock is the preferred dividend yield. (As a rule of thumb, if the preferred stock is less than 5% of the outstanding market value of the firm, lumping it in with debt will make no significant impact on your valuation).

# Decomposing a convertible bond…

¨ Assume that the firm that you are analyzing has \$125 million in face value of convertible debt with a stated interest rate of 4%, a 10 year maturity and a market value of \$140 million. If the firm has a bond rating of A and the interest rate on Arated straight bond is 8%, you can break down the value of the convertible bond into straight debt and equity portions. ¤ Straight debt = (4% of \$125 million) (PV of annuity, 10 years, 8%) + 125 million/1.0810 = \$91.45 million ¤ Equity portion = \$140 million - \$91.45 million = \$48.55 million ¨ The debt portion (\$91.45 million) gets added to debt and the option portion (\$48.55 million) gets added to the market capitalization to get to the debt and equity weights in the cost of capital.

# Recapping the Cost of Capital

![](_page_111_Diagram_2.jpeg)

# ESTIMATING CASH FLOWS

Cash is king...

# Steps in Cash Flow Estimation

¨ Estimate the current earnings of the firm ¤ If looking at cash flows to equity, look at earnings after interest expenses - i.e. net income ¤ If looking at cash flows to the firm, look at operating earnings after taxes ¨ Consider how much the firm invested to create future growth ¤ If the investment is not expensed, it will be categorized as capital expenditures. To the extent that depreciation provides a cash flow, it will cover some of these expenditures. ¤ Increasing working capital needs are also investments for future growth ¨ If looking at cash flows to equity, consider the cash flows from net debt issues (debt issued - debt repaid)

# Measuring Cash Flows

**Cash flows can be measured to**

![](_page_114_Diagram_3.jpeg)

# Measuring Cash Flow to the Firm: Three pathways to the same end game

116

$$\begin{array}{lll} \text{EBIT (1 - tax rate)} & minus & (\text{Cap Ex - Depreciation}) \\ & & + \text{Change in non-cash Working capial} & = & \text{FCFF} \\ \\ \text{EBIT (1 - tax rate)} & minus & \text{Reinvestment} & = & \text{FCFF} \\ \\ \text{EBIT (1 - tax rate)} & \times & (1 - \text{Reinvestment Rate}) & = & \text{FCFF} \end{array}$$

Where are the tax savings from interest expenses?

117

# Cash Flows I

Accounting Earnings, Flawed but Important

# From Reported to Actual Earnings

![](_page_117_Diagram_2.jpeg)

# I. Update Earnings

¨ When valuing companies, we often depend upon financial statements for inputs on earnings and assets. Annual reports are often outdated and can be updated by using- ¤ Trailing 12-month data, constructed from quarterly earnings reports. ¤ Informal and unofficial news reports, if quarterly reports are unavailable. ¨ Updating makes the most difference for smaller and more volatile firms, as well as for firms that have undergone significant restructuring. ¨ Time saver: To get a trailing 12-month number, all you need is one 10K and one 10Q (example third quarter). Use the Year to date numbers from the 10Q. For example, to get trailing revenues from a third quarter 10Q: ¤ Trailing 12-month Revenue = Revenues (in last 10K) - Revenues from first 3 quarters of last year + Revenues from first 3 quarters of this year.

# II. Correcting Accounting Earnings

¨ Make sure that there are no financial expenses mixed in with operating expenses ¤ Financial expense: Any commitment that is tax deductible that you have to meet no matter what your operating results: Failure to meet it leads to loss of control of the business. ¤ Example: Operating Leases: While accounting convention treats operating leases as operating expenses, they are really financial expenses and need to be reclassified as such. This has no effect on equity earnings but does change the operating earnings ¨ Make sure that there are no capital expenses mixed in with the operating expenses ¤ Capital expense: Any expense that is expected to generate benefits over multiple periods. ¤ R & D Adjustment: Since R&D is a capital expenditure (rather than an operating expense), the operating income has to be adjusted to reflect its treatment.

# The Magnitude of Operating Leases

Operating Lease expenses as % of Operating Income

![](_page_120_Figure_3.jpeg)

# Dealing with Operating Lease Expenses

¨ Operating Lease Expenses are treated as operating expenses in computing operating income. In reality, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital: ¨ Debt Value of Operating Leases = Present value of Operating Lease Commitments at the pre-tax cost of debt ¨ When you convert operating leases into debt, you also create an asset to counter it of exactly the same value. ¨ Adjusted Operating Earnings ¤ Adjusted Operating Earnings = Operating Earnings + Operating Lease Expenses - Depreciation on Leased Asset As an approximation, this works: ¤ Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

# Operating Leases at The Gap in 2003

¨ The Gap has conventional debt of about \$ 1.97 billion on its balance sheet and its pre-tax cost of debt is about 6%. Its operating lease payments in the 2003 were \$978 million and its commitments for the future are below:

| Year | Commitment         | (millions) Present	Value (at	6%) |
|------|--------------------|----------------------------------|
| 1    | \$899.00           | \$848.11                         |
| 2    | \$846.00           | \$752.94                         |
| 3    | \$738.00           | \$619.64                         |
| 4    | \$598.00           | \$473.67                         |
| 5    | \$477.00           | \$356.44                         |
| 6&7  | \$982.50	each	year | \$1,346.04                       |

¨ Debt Value of leases = \$4,396.85 (Also value of leased asset) ¨ Debt outstanding at The Gap = \$1,970 m + \$4,397 m = \$6,367 m ¨ Adjusted Operating Income = Stated OI + OL exp this year - Deprec' n = \$1,012 m + 978 m - 4397 m /7 = \$1,362 million (7 year life for assets) ¨ Approximate OI = \$1,012 m + \$ 4397 m (.06) = \$1,276 m

### The Collateral Effects of Treating Operating Leases as Debt

| <i>Conventional Accounting</i>                                                                                                                                       |  | <i>Operating Leases Treated as Debt</i>                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-----------------------------------------------------------------------------------------------------------------|
| <i>Income Statement</i>                                                                                                                                              |  | <i>Income Statement</i>                                                                                         |
| EBIT& Leases = 1,990                                                                                                                                                 |  | EBIT& Leases = 1,990                                                                                            |
| - Op Leases = 978                                                                                                                                                    |  | - Deprecn: OL= 628                                                                                              |
| EBIT = 1,012                                                                                                                                                         |  | EBIT = 1,362                                                                                                    |
|                                                                                                                                                                      |  | Interest expense will rise to reflect the conversion of operating leases as debt. Net income should not change. |
| <i>Balance Sheet</i>                                                                                                                                                 |  | <i>Balance Sheet</i>                                                                                            |
| Off balance sheet (Not shown as debt or as an asset). Only the conventional debt of \$1,970 million shows up on balance sheet                                        |  | Asset Liability<br>OL Asset 4397 OL Debt 4397<br>Total debt = 4397 + 1970 = \$6,367 million                     |
| Cost of capital = 8.20%(7350/9320) + 4%<br>(1970/9320) = 7.31%<br>Cost of equity for The Gap = 8.20%<br>After-tax cost of debt = 4%<br>Market value of equity = 7350 |  | Cost of capital = 8.20%(7350/13717) + 4%<br>(6367/13717) = 6.25%                                                |
| Cost of equity for The Gap = 8.20%<br>After-tax cost of debt = 4%<br>Market value of equity = 7350                                                                   |  |                                                                                                                 |
| Return on capital = 1012 (1-.35)/(3130+1970)<br>= 12.90%                                                                                                             |  | Return on capital = 1362 (1-.35)/(3130+6367)<br>= 9.30%                                                         |

# The Magnitude of R&D Expenses

R&D as % of Operating Income

![](_page_124_Figure_3.jpeg)

### R&D Expenses: Operating or Capital Expenses

¨ Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. ¨ To capitalize R&D, ¤ Specify an amortizable life for R&D (2 - 10 years) ¤ Collect past R&D expenses for as long as the amortizable life ¤ Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

# Capitalizing R&D Expenses: SAP

¨ R & D was assumed to have a 5-year life. 

| Year    | R&D	Expense |      | Unamortized | Amortization this	year |
|---------|-------------|------|-------------|------------------------|
| Current | 1020.02     | 1.00 | 1020.02     |                        |
| -1      | 993.99      | 0.80 | 795.19      | €	198.80               |
| -2      | 909.39      | 0.60 | 545.63      | €	181.88               |
| -3      | 898.25      | 0.40 | 359.30      | €	179.65               |
| -4      | 969.38      | 0.20 | 193.88      | €	193.88               |
| -5      | 744.67      | 0.00 | 0.00        | €	148.93               |

Value of research asset = € 2,914 million

Amortization of research asset in 2004 = € 903 million

Increase in Operating Income = 1020 - 903 = € 117 million

# The Effect of Capitalizing R&D at SAP

| <i>Conventional Accounting</i>                                                                                              |  | <i>R&amp;D treated as capital expenditure</i> |  |
|-----------------------------------------------------------------------------------------------------------------------------|--|-----------------------------------------------|--|
| <i>Income Statement</i>                                                                                                     |  | <i>Income Statement</i>                       |  |
| EBIT& R&D = 3045                                                                                                            |  | EBIT& R&D = 3045                              |  |
| - R&D = 1020                                                                                                                |  | - Amort: R&D = 903                            |  |
| EBIT = 2025                                                                                                                 |  | EBIT = 2142 (Increase of 117 m)               |  |
| EBIT (1-t) = 1285 m                                                                                                         |  | EBIT (1-t) = 1359 m                           |  |
|                                                                                                                             |  | Ignored tax benefit = (1020-903)(.3654) = 43  |  |
|                                                                                                                             |  | Adjusted EBIT (1-t) = 1359+43 = 1402 m        |  |
|                                                                                                                             |  | (Increase of 117 million)                     |  |
|                                                                                                                             |  | Net Income will also increase by 117 million  |  |
| <i>Balance Sheet</i>                                                                                                        |  | <i>Balance Sheet</i>                          |  |
| Off balance sheet asset. Book value of equity at 3,768 million Euros is understated because biggest asset is off the books. |  | Asset Liability                               |  |
|                                                                                                                             |  | R&D Asset 2914 Book Equity +2914              |  |
|                                                                                                                             |  | Total Book Equity = 3768+2914= 6782 mil       |  |
| <i>Capital Expenditures</i>                                                                                                 |  | <i>Capital Expenditures</i>                   |  |
| Conventional net cap ex of 2 million Euros                                                                                  |  | Net Cap ex = 2+ 1020 - 903 = 119 mil          |  |
| <i>Cash Flows</i>                                                                                                           |  |                                               |  |
| EBIT (1-t) = 1285                                                                                                           |  | EBIT (1-t) = 1402                             |  |
| - Net Cap Ex = 2                                                                                                            |  | - Net Cap Ex = 119                            |  |
| FCFF = 1283                                                                                                                 |  | FCFF = 1283 m                                 |  |
| Return on capital = 1285/(3768+530)                                                                                         |  | Return on capital = 1402/(6782+530)           |  |

# III. One-Time and Non-recurring Charges

- ¨ Assume that you are valuing a firm that is reporting a loss of \$ 500 million, due to a one-time charge of \$ 1 billion. What is the earnings you would use in your valuation?
  - a. A loss of \$ 500 million
- b. A profit of \$ 500 million ¨ Would your answer be any different if the firm had reported one-time losses like these once every five years?
  - a. Yes
  - b. No

# IV. Accounting Malfeasance….

¨ Though all firms may be governed by the same accounting standards, the fidelity that they show to these standards can vary. More aggressive firms will show higher earnings than more conservative firms. ¨ While you will not be able to catch outright fraud, you should look for warning signals in financial statements and correct for them: ¤ Income from unspecified sources - holdings in other businesses that are not revealed or from special purpose entities. ¤ Income from asset sales or financial transactions (for a non-financial firm) ¤ Sudden changes in standard expense items - a big drop in S,G &A or R&D expenses as a percent of revenues, for instance. ¤ Frequent accounting restatements ¤ Accrual earnings that run ahead of cash earnings consistently ¤ Big differences between tax income and reported income

### V. Dealing with Negative or Abnormally Low Earnings

#### **A Framework for Analyzing Companies with Negative or Abnormally Low Earnings**

![](_page_130_Diagram_3.jpeg)

132

# Cash Flows II

## Taxes and Reinvestment

# What tax rate?

- ¨ The tax rate that you should use in computing the aftertax operating income should be
  - a. The effective tax rate in the financial statements (taxes paid/Taxable income)
  - b. The tax rate based upon taxes paid and EBIT (taxes paid/EBIT)
  - c. The marginal tax rate for the country in which the company operates
  - d. The weighted average marginal tax rate across the countries in which the company operates
  - e. None of the above
  - f. Any of the above, as long as you compute your after-tax cost of debt using the same tax rate

# The Right Tax Rate to Use

¨ The choice really is between the effective and the marginal tax rate. In doing projections, it is far safer to use the marginal tax rate since the effective tax rate is really a reflection of the difference between the accounting and the tax books. ¨ By using the marginal tax rate, we tend to understate the after-tax operating income in the earlier years, but the aftertax tax operating income is more accurate in later years ¨ If you choose to use the effective tax rate, adjust the tax rate towards the marginal tax rate over time. ¤ While an argument can be made for using a weighted average marginal tax rate, it is safest to use the marginal tax rate of the country 

# A Tax Rate for a Money Losing Firm

¨ Assume that you are trying to estimate the after-tax operating income for a firm with \$ 1 billion in net operating losses carried forward. This firm is expected to have operating income of \$ 500 million each year for the next 3 years, and the marginal tax rate on income for all firms that make money is 40%. Estimate the after-tax operating income each year for the next 3 years.

|            | Year 1 | Year 2 | Year 3 |     |
|------------|--------|--------|--------|-----|
| EBIT       | 500    | 500    | 500    | 500 |
| Taxes      |        |        |        |     |
| EBIT (1-t) |        |        |        |     |
| Tax rate   |        |        |        |     |

# Net Capital Expenditures

¨ Net capital expenditures represent the difference between capital expenditures and depreciation. Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures. ¨ In general, the net capital expenditures will be a function of how fast a firm is growing or expecting to grow. High growth firms will have much higher net capital expenditures than low growth firms. ¨ Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

# Capital expenditures should include

- Research and development expenses, once they have been re-categorized as capital expenses. The adjusted net cap ex will be
  - Adjusted Net Capital Expenditures = Net Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset
- Acquisitions of other firms, since these are like capital expenditures. The adjusted net cap ex will be
  - Adjusted Net Cap Ex = Net Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions
- Two caveats:
  1. 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
  2. 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

# Cisco's Acquisitions: 1999

| Acquired          | Method	of	Acquisition | Price	Paid |
|-------------------|-----------------------|------------|
| GeoTel            | Pooling               | \$1,344    |
| Fibex             | Pooling               | \$318      |
| Sentient          | Pooling               | \$103      |
| American	Internet | Purchase              | \$58       |
| Summa	Four        | Purchase              | \$129      |
| Clarity	Wireless  | Purchase              | \$153      |
| Selsius Systems   | Purchase              | \$134      |
| PipeLinks         | Purchase              | \$118      |
| Amteva Tech       | Purchase              | \$159      |

# Cisco's Net Capital Expenditures in 1999

Cap Expenditures (from statement of CF) = \$ 584 mil

- Depreciation (from statement of CF) = \$ 486 mil

Net Cap Ex (from statement of CF)= \$ 98 mil

+ R & D expense = \$ 1,594 mil

- Amortization of R&D = \$ 485 mil

+ Acquisitions = \$ 2,516 mil

Adjusted Net Capital Expenditures = \$3,723 mil

¨ (Amortization was included in the depreciation number)

# Working Capital Investments

¨ In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) ¨ A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable) ¨ For firms in some sectors, it is the investment in working capital that is the bigger part of reinvestment.

# Working Capital: General Propositions

- 1. Working Capital Detail: While some analysts break down working capital into detail (inventory, deferred taxes, payables etc.), it is a pointless exercise unless you feel that you can bring some specific information that lets you forecastthe details.
- 2. Working Capital Volatility: Changes in non-cash working capital from year to year tend to be volatile. So, building of the change in the most recent year is dangerous. It is better to either estimate the change based on working capital as a percent ofsales, while keeping an eye on industry averages.
- 3. Negative Working Capital: Some firms have negative non- cash working capital. Assuming that this will continue into the future will generate positive cash flows for the firm and will get more positive as growth increases.

# Volatile Working Capital?

| Revenues Non-cash	WC  | Amazon \$	1,640 -\$419 | Cisco \$12,154 -\$404 | Motorola \$30,931 \$2547 |
|-----------------------|------------------------|-----------------------|--------------------------|
| %	of	Revenues         | -25.53%                | -3.32%                | 8.23%                    |
| Change	from	last	year | \$			(309)             | (\$700)               | (\$829)                  |
| Average:	last	3	years | -15.16%                | -3.16%                | 8.91%                    |
| Average:	industry     | 8.71%                  | -2.71%                | 7.04%                    |

*My Prediction*

| WC as % of Revenue | 3.00% | 0.00% | 8.23% |
|--------------------|-------|-------|-------|
|                    |       |       |       |

143

# Cash Flows III

From the firm to equity

# Dividends and Cash Flows to Equity

¨ In the strictest sense, the only cash flow that an investor will receive from an equity investment in a publicly traded firm is the dividend that will be paid on the stock. ¨ Actual dividends, however, are set by the managers of the firm and may be much lower than the potential dividends (that could have been paid out) ¤ managers are conservative and try to smooth out dividends ¤ managers like to hold on to cash to meet unforeseen future contingencies and investment opportunities ¨ When actual dividends are less than potential dividends, using a model that focuses only on dividends will under state the true value of the equity in a firm. 

# Measuring Potential Dividends

¨ Some analysts assume that the earnings of a firm represent its potential dividends. This cannot be true for several reasons: ¤ Earnings are not cash flows, since there are both non-cash revenues and expenses in the earnings calculation ¤ Even if earnings were cash flows, a firm that paid its earnings out as dividends would not be investing in new assets and thus could not grow ¤ Valuation models, where earnings are discounted back to the present, will over estimate the value of the equity in the firm ¨ The potential dividends of a firm are the cash flows left over after the firm has made any "investments" it needs to make to create future growth and net debt repayments (debt repayments - new debt issues) ¤ The common categorization of capital expenditures into discretionary and non-discretionary loses its basis when there is future growth built into the valuation.

# Estimating Cash Flows: FCFE

¨ Cash flows to Equity for a Levered Firm

Net Income

- (Capital Expenditures - Depreciation)
- Changes in non-cash Working Capital
- (Principal Repayments - New Debt Issues) = Free Cash flow to Equity

¨ I have ignored preferred dividends. If preferred stock exist, preferred dividends will also need to be netted out

# Estimating FCFE when Leverage is Stable

#### Net Income

- (1- DR) (Capital Expenditures - Depreciation)
- (1- DR) Working Capital Needs = Free Cash flow to Equity

DR = Debt/Capital Ratio

For this firm, 

¤ Proceeds from new debt issues = Principal Repayments + d (Capital Expenditures - Depreciation + Working Capital Needs) ¨In computing FCFE, the book value debt to capital ratio should be used when looking back in time but can be replaced with the market value debt to capital ratio, looking forward.

# Estimating FCFE: Disney

- ¨ Net Income=\$ 1533 Million ¨ Capital spending = \$ 1,746 Million ¨ Depreciation per Share = \$ 1,134 Million ¨ Increase in non-cash working capital = \$ 477 Million ¨ Debt to Capital Ratio (DR) = 23.83% ¨ Estimating FCFE (1997): Net Income \$1,533 Mil
  - (Cap. Exp Depr)\*(1-DR) \$465.90 [(1746-1134)(1-.2383)] Chg. Working Capital\*(1-DR) \$363.33 [477(1-.2383)] = Free CF to Equity \$ 704 Million Dividends Paid \$ 345 Million

# FCFE and Leverage: Is this a free lunch?

Debt Ratio and FCFE: Disney

![](_page_148_Figure_3.jpeg)

# FCFE and Leverage: The Other Shoe Drops

Debt Ratio and Beta

![](_page_149_Figure_3.jpeg)

# Leverage, FCFE and Value

- ¨ In a discounted cash flow model, increasing the debt/equity ratio will generally increase the expected free cash flows to equity investors over future time periods and also the cost of equity applied in discounting these cash flows. Which of the following statements relating leverage to value would you subscribe to?
  - a. Increasing leverage will increase value because the cash flow effects will dominate the discount rate effects
  - b. Increasing leverage will decrease value because the risk effect will be greater than the cash flow effects
  - c. Increasing leverage will not affect value because the risk effect will exactly offset the cash flow effect
  - d. Any of the above, depending upon what company you are looking at and where it is in terms of current leverage

# ESTIMATING GROWTH

Growth can be good, bad or neutral...

# The Value of Growth

¨ When valuing a company, it is easy to get caught up in the details of estimating growth and start viewing growth as a "good", i.e., that higher growth translates into higher value. ¨ Growth, though, is a double-edged sword. ¤ The good side of growth is that it pushes up revenues and operating income, perhaps at different rates (depending on how margins evolve over time). ¤ The bad side of growth is that you have to set aside money to reinvest to create that growth. ¤ The net effect of growth is whether the good outweighs the bad.

# Ways of Estimating Growth in Earnings

¨ Look at the past ¤ The historical growth in earnings per share is usually a good starting point for growth estimation ¨ Look at what others are estimating ¤ Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are. ¨ Look at fundamentals ¤ Ultimately, all growth in earnings can be traced to two fundamentals - how much the firm is investing in new projects, and what returns these projects are making for the firm.

#### Historical Growth

# Growth I **<sup>155</sup>**

# Historical Growth

¨ Historical growth rates can be estimated in a number of different ways ¤ Arithmetic versus Geometric Averages ¤ Simple versus Regression Models ¨ Historical growth rates can be sensitive to ¤ The period used in the estimation (starting and ending points) ¤ The metric that the growth is estimated in.. ¨ In using historical growth rates, you have to wrestle with the following: ¤ How to deal with negative earnings ¤ The effects of scaling up

### Motorola: Arithmetic versus Geometric Growth Rates

|                    | Revenues  | % Change | EBITDA   | % Change | EBIT     | % Change |
|--------------------|-----------|----------|----------|----------|----------|----------|
| 1994               | \$ 22,245 |          | \$ 4,151 |          | \$ 2,604 |          |
| 1995               | \$ 27,037 | 21.54%   | \$ 4,850 | 16.84%   | \$ 2,931 | 12.56%   |
| 1996               | \$ 27,973 | 3.46%    | \$ 4,268 | -12.00%  | \$ 1,960 | -33.13%  |
| 1997               | \$ 29,794 | 6.51%    | \$ 4,276 | 0.19%    | \$ 1,947 | -0.66%   |
| 1998               | \$ 29,398 | -1.33%   | \$ 3,019 | -29.40%  | \$ 822   | -57.78%  |
| 1999               | \$ 30,931 | 5.21%    | \$ 5,398 | 78.80%   | \$ 3,216 | 291.24%  |
| Arithmetic Average |           | 7.08%    |          | 10.89%   |          | 42.45%   |
| Geometric Average  |           | 6.82%    |          | 5.39%    |          | 4.31%    |
| Standard deviation |           | 8.61%    |          | 41.56%   |          | 141.78%  |

# A Test

- ¨ You are trying to estimate the growth rate in earnings per share at Time Warner from 1996 to 1997. In 1996, the earnings per share was a deficit of \$0.05. In 1997, the expected earnings per share is \$ 0.25. What is the growth rate?
- a. -600%
- b. +600%
- c. +120%
- d. Cannot be estimated

# Dealing with Negative Earnings

¨ When the earnings in the starting period are negative, the growth rate cannot be estimated. (0.30/-0.05 = - 600%) ¨ There are three solutions: ¤ Use the higher of the two numbers as the denominator (0.30/0.25 = 120%) ¤ Use the absolute value of earnings in the starting period as the denominator (0.30/0.05=600%) ¤ Use a linear regression model and divide the coefficient by the average earnings. ¨ When earnings are negative, the growth rate is meaningless. Thus, while the growth rate can be estimated, it does not tell you much about the future.

# The Effect of Size on Growth: Callaway Golf

| Year | Net	Profit | Growth	Rate |
|------|------------|-------------|
| 1990 | 1.80       |             |
| 1991 | 6.40       | 255.56%     |
| 1992 | 19.30      | 201.56%     |
| 1993 | 41.20      | 113.47%     |
| 1994 | 78.00      | 89.32%      |
| 1995 | 97.70      | 25.26%      |
| 1996 | 122.30     | 25.18%      |

¨ Geometric Average Growth Rate = 102%

# Extrapolation and its Dangers

Year Net Profit

1996 \$ 122.30 

1997 \$ 247.05 

1998 \$ 499.03 

1999 \$ 1,008.05 

2000 \$ 2,036.25 

2001 \$ 4,113.23

¨ If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

#### Analyst Estimates

# Growth II **<sup>162</sup>**

# Analyst Forecasts of Growth

¨ While the job of an analyst is to find under and over valued stocks in the sectors that they follow, a significant proportion of an analyst's time (outside of selling) is spent forecasting earnings per share. ¤ Most of this time, in turn, is spent forecasting earnings per share in the next earnings report ¤ While many analysts forecast expected growth in earnings per share over the next 5 years, the analysis and information (generally) that goes into this estimate is far more limited. ¨ Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

### How good are analysts at forecasting growth?

¨ Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| Study Group	tested                     | Analyst Error | Time	Series Model	Error |
|----------------------------------------|---------------|-------------------------|
| Collins	&	Hopwood	Value	Line	Forecasts | 31.7%         | 34.1%                   |
| Brown	&	Rozeff Value	Line	Forecasts    | 28.4%         | 32.2%                   |
| Fried	&	Givoly Earnings	Forecaster     | 16.4%         | 19.8%                   |

¨ The advantage that analysts have over time series models ¤ tends to decrease with the forecast period (next quarter versus 5 years) ¤ tends to be greater for larger firms than for smaller firms ¤ tends to be greater at the industry level than at the company level ¨ Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

### Are some analysts more equal than others?

¨ A study of All-America Analysts (chosen by Institutional Investor) found that ¤ There is no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%) ¤ However, in the calendar year following being chosen as All-America analysts, these analysts become slightly better forecasters than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts) ¤ Earnings revisions made by All-America analysts tend to have a much greater impact on the stock price than revisions from other analysts ¤ The recommendations made by the All America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (2.4% for buys; 13.8% for the sells).

# The Five Deadly Sins of an Analyst

¨ Tunnel Vision: Becoming so focused on the sector and valuations within the sector that you lose sight of the bigger picture. ¨ Lemmingitis: Strong urge felt to change recommendations & revise earnings estimates when other analysts do the same. ¨ Stockholm Syndrome: Refers to analysts who start identifying with the managers of the firms that they are supposed to follow. ¨ Factophobia (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a "story" coupled with a refusal to face the facts. ¨ Dr. Jekyll/Mr.Hyde: Analyst who thinks his primary job is to bring in investment banking business to the firm.

# Propositions about Analyst Growth Rates

¨ Proposition 1: There if far less private information and far more public information in most analyst forecasts than is generally claimed. ¨ Proposition 2: The biggest source of private information for analysts remains the company itself which might explain ¤ why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources) ¤ why there is such a high correlation across analysts forecasts and revisions ¤ why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team. ¨ Proposition 3: There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

168

# Growth III

It's all in the fundamentals

# Fundamental Growth Rates

Investment in Existing Projects \$ 1000 Current Return on Investment on Projects 12% X = Current Earnings \$120

Investment in Existing Projects \$1000 Next Period's Return on Investment 12% X Investment in New Projects \$100 Return on Investment on New Projects 12% + <sup>X</sup> <sup>=</sup> Next Period's Earnings 132

Investment in Existing Projects \$1000 Change in ROI from current to next period: 0% X Investment in New Projects \$100 Return on Investment on New Projects 12% + <sup>X</sup> Change in Earnings = \$ 12

# Growth Rate Derivations

In the special case where ROI on existing projects remains unchanged and is equal to the ROI on new projects

Investment in New Projects Current Earnings Return on Investment Change in Earnings Current Earnings X =

Reinvestment Rate X Return on Investment = Growth Rate in Earnings 83.33% X 12% = 10%

in the more general case where ROI can change from period to period, this can be expanded as follows:

Investment in Existing Projects\*(Change in ROI) + New Projects (ROI) Investment in Existing Projects\* Current ROI Change in Earnings Current Earnings =

100 <sup>120</sup> X 12% = \$12 \$120

For instance, if the ROI increases from 12% to 13%, the expected growth rate can be written as follows:

$$\frac{\$1,000 * (.13 - .12) + 100 (13\%)}{\$ 1000 * .12} = \frac{\$23}{\$120} = 19.17\%$$

### Estimating Fundamental Growth from new investments: Three variations

| Earnings Measure                | Reinvestment Measure                                                                           | Return Measure                                                                                             |
|---------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Earnings per share              | Retention Ratio = % of net income retained by the company = 1 – Payout ratio                   | Return on Equity = Net Income/ Book Value of Equity                                                        |
| Net Income from non-cash assets | Equity reinvestment Rate = (Net Cap Ex + Change in non-cash WC – Change in Debt)/ (Net Income) | Non-cash ROE = Net Income from non-cash assets/ (Book value of equity – Cash)                              |
| Operating Income                | Reinvestment Rate = (Net Cap Ex + Change in non-cash WC)/ After-tax Operating Income           | Return on Capital or ROIC = After-tax Operating Income/ (Book value of equity + Book value of debt – Cash) |

# I. Expected Long Term Growth in EPS

¨ When looking at growth in earnings per share, these inputs can be cast as follows: ¤ Reinvestment Rate = Retained Earnings/ Current Earnings = Retention Ratio ¤ Return on Investment = ROE = Net Income/Book Value of Equity ¨ In the special case where the current ROE is expected to remain unchanged

| $g_{EPS}$ | = Retained Earnings <sub>t-1</sub> / NI <sub>t-1</sub> * ROE |
|-----------|--------------------------------------------------------------|
|           | = Retention Ratio * ROE                                      |
|           | = b * ROE                                                    |

¨ Proposition 1: The expected growth rate in earnings for a company cannot exceed its return on equity in the long term. 

### Estimating Expected Growth in EPS: Wells Fargo in 2008

¨ Return on equity (based on 2008 earnings)= 17.56% ¨ Retention Ratio (based on 2008 earnings and dividends) = 45.37% ¨ Expected growth rate in earnings per share for Wells Fargo, if it can maintain these numbers.

Expected Growth Rate = 0.4537 (17.56%) = 7.97%

# Regulatory Effects on Expected EPS growth

¨ Assume now that the banking crisis of 2008 will have an impact on the capital ratios and profitability of banks. In particular, you can expect that the book capital (equity) needed by banks to do business will increase 30%, starting now. ¨ Assuming that Wells continues with its existing businesses, estimate the expected growth rate in earnings per share for the future.

New Return on Equity =

Expected growth rate =

# One way to pump up ROE: Use more debt

ROE = ROC + D/E (ROC - i (1-t))

where,

ROC = EBITt (1 - tax rate) / Book value of Capitalt-1

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / BV of Debt

t = Tax rate on ordinary income

¨ Note that Book value of capital = Book Value of Debt + Book value of Equity- Cash.

# Decomposing ROE: Brahma in 1998

¨ Brahma (now Ambev) had an extremely high return on equity, partly because it borrowed money at a rate well below its return on capital ¤ Return on Capital = 19.91% ¤ Debt/Equity Ratio = 77% ¤ After-tax Cost of Debt = 5.61% ¤ Return on Equity = ROC + D/E (ROC - i(1-t)) = 19.91% + 0.77 (19.91% - 5.61%) = 30.92% ¨ This seems like an easy way to deliver higher growth in earnings per share. What (if any) is the downside?

# Decomposing ROE: Titan Watches (India) in 2000

¨ Return on Capital = 9.54% ¨ Debt/Equity Ratio = 191% (book value terms) ¨ After-tax Cost of Debt = 10.125% ¨ Return on Equity = ROC + D/E (ROC - i(1-t)) = 9.54% + 1.91 (9.54% - 10.125%) = 8.42%

### II. Expected Growth in Net Income from noncash assets

¨ The limitation of the EPS fundamental growth equation is that it focuses on per share earnings and assumes that reinvested earnings are invested in projects earning the return on equity. To the extent that companies retain money in cash balances, the effect on net income can be muted. ¨ A more general version of expected growth in earnings can be obtained by substituting in the equity reinvestment into real investments (net capital expenditures and working capital) and modifying the return on equity definition to exclude cash: ¤ Net Income from non-cash assets = Net income – Interest income from cash (1- t) ¤ Equity Reinvestment Rate = (Net Capital Expenditures + Change in Working Capital) (1 - Debt Ratio)/ Net Income from non-cash assets ¤ Non-cash ROE = Net Income from non-cash assets/ (BV of Equity – Cash) ¤ Expected GrowthNet Income = Equity Reinvestment Rate \* Non-cash ROE

### Estimating expected growth in net income from non-cash assets: Coca Cola in 2010

¨ In 2010, Coca Cola reported net income of \$11,809 million. It had a total book value of equity of \$25,346 million at the end of 2009. ¨ Coca Cola had a cash balance of \$7,021 million at the end of 2009, on which it earned income of \$105 million in 2010. ¨ Coca Cola had capital expenditures of \$2,215 million, depreciation of \$1,443 million and reported an increase in working capital of \$335 million. Coca Cola's total debt increased by \$150 million during 2010. ¤ Equity Reinvestment = 2215- 1443 + 335-150 = \$957 million ¤ Non-cash Net Income = \$11,809 - \$105 = \$ 11,704 million ¤ Non-cash book equity = \$25,346 - \$7021 = \$18,325 million ¤ Reinvestment Rate = \$957 million/ \$11,704 million= 8.18% ¤ Non-cash ROE = \$11,704 million/ \$18,325 million = 63.87% ¤ Expected growth rate = 8.18% \* 63.87% = 5.22%

### III. Expected Growth in EBIT And Fundamentals: Stable ROC and Reinvestment Rate

¨ When looking at growth in operating income, the definitions are ¤ Reinvestment Rate = (Net Capital Expenditures + Change in WC)/EBIT(1-t) ¤ Return on Investment = ROC = EBIT(1-t)/(BV of Debt + BV of Equity-Cash) ¨ Reinvestment Rate and Return on Capital Expected Growth rate in Operating Income = (Net Capital Expenditures + Change in WC)/EBIT(1-t) \* ROC = Reinvestment Rate \* ROC ¨ Proposition: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments. 

# Estimating Growth in Operating Income, if fundamentals stay unchanged

- ¨ Cisco's Fundamentals ¤ Reinvestment Rate = 106.81% ¤ Return on Capital =34.07% ¤ Expected Growth in EBIT =(1.0681)(.3407) = 36.39% ¨ Motorola's Fundamentals ¤ Reinvestment Rate = 52.99% ¤ Return on Capital = 12.18% ¤ Expected Growth in EBIT = (.5299)(.1218) = 6.45% ¨ Cisco's expected growth rate is clearly much higher than Motorola's sustainable growth rate. As a potential investor in Cisco, what would worry you the most about this forecast?
  - a. That Cisco's return on capital may be overstated (why?)
  - b. That Cisco's reinvestment comes mostly from acquisitions (why?)
  - c. That Cisco is getting bigger as a firm (why?)
  - d. That Cisco is viewed as a star (why?)
  - e. All of the above

# The Magical Number: ROIC (or any accounting return) and its limits

![](_page_181_Diagram_2.jpeg)

### IV. Operating Income Growth when Return on Capital is Changing

¨ When the return on capital is changing, there will be a second component to growth, positive if the return on capital is increasing and negative if the return on capital is decreasing. ¨ If ROCt is the return on capital in period t and ROC t+1 is the return on capital in period t+1, the expected growth rate in operating income will be:

$$\text{Expected Growth Rate} = \text{ROC}_{t+1} * \text{Reinvestment rate} + (\text{ROC}_{t+1} - \text{ROC}_t) / \text{ROC}_t$$

¨ If the change is over multiple periods, the second component should be spread out over each period.

# Motorola's Growth Rate

¨ Motorola's current return on capital is 12.18% and its reinvestment rate is 52.99%. ¨ We expect Motorola's return on capital to rise to 17.22% over the next 5 years (which is half way towards the industry average)

Expected Growth Rate 

$$= \text{ROC}_{\text{Current}}^{\text{New Investments}} [1^{1/5-1}]^* \text{Reinvestment Rate}_{\text{Current}} + \{ [1 + (\text{ROC}_{\text{In 5 years}} - \text{ROC}_{\text{Current}})] / \text{ROC}_{\text{Current}} ]^{1/5-1} \}$$

= .1722\*.5299 +{ [1+(.1722-.1218)/.1218]1/5-1} 

= .1629 or 16.29%

¨ One way to think about this is to decompose Motorola's expected growth into 

¤Growth from new investments: .1722\*5299= 9.12%

¤Growth from more efficiently using existing investments: 16.29%-9.12%= 7.17%

Note that I am assuming that the new investments start making 17.22% immediately, while allowing for existing assets to improve returns gradually

# The Value of Growth

$$\begin{aligned} \text{Expected growth} &= \text{Growth from new investments} + \text{Efficiency growth} \\ &= \text{Reinv Rate} * \text{ROC} + (\text{ROC}_t - \text{ROC}_{t-1})/\text{ROC}_{t-1} \end{aligned}$$

**Assume that your cost of capital is 10%. As an investor, rank these firms in the order of most value growth to least value growth.**

|                                     | Firm 1        | Firm 2        | Firm 3        | Firm 4        | Firm 5        |
|-------------------------------------|---------------|---------------|---------------|---------------|---------------|
| Reinvestment Rate                   | 20.00%        | 100.00%       | 200.00%       | 20.00%        | 0.00%         |
| ROIC on new investment              | 50.00%        | 10.00%        | 5.00%         | 10.00%        | 10.00%        |
|                                     |               |               |               |               |               |
| ROIC on existing investments before | 10.00%        | 10.00%        | 10.00%        | 10.00%        | 10.00%        |
| ROIC on existing investments after  | 10.00%        | 10.00%        | 10.00%        | 10.80%        | 11.00%        |
|                                     |               |               |               |               |               |
| <b>Expected growth rate</b>         | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> |

Top Down Growth

# **<sup>186</sup>** Growth IV

### Estimating Growth when Operating Income is Negative or Margins are changing

¨ All of the fundamental growth equations assume that the firm has a return on equity or return on capital it can sustain in the long term. ¨ When operating income is negative or margins are expected to change over time, we use a three step process to estimate growth: ¤ Estimate growth rates in revenues over time n Determine the total market (given your business model) and estimate the market share that you think your company will earn. n Decrease the growth rate as the firm becomes larger n Keep track of absolute revenues to make sure that the growth is feasible ¤ Estimate expected operating margins each year n Set a target margin that the firm will move towards n Adjust the current margin towards the target margin ¤ Estimate the capital that needs to be invested to generate revenue growth and expected margins n Estimate a sales to capital ratio that you will use to generate reinvestment needs each year.

# Tesla in July 2015: Growth and Profitability

188

| Year      | Revenues    | Revenue Growth | Operating Income | Operating Margin |
|-----------|-------------|----------------|------------------|------------------|
| Base year | \$2,013.50  |                | \$(21.81)        | -1.08%           |
| 1         | \$3,322.28  | 65.00%         | \$7.48           | 0.23%            |
| 2         | \$5,481.75  | 65.00%         | \$84.06          | 1.53%            |
| 3         | \$9,044.89  | 65.00%         | \$257.03         | 2.84%            |
| 4         | \$14,924.07 | 65.00%         | \$619.36         | 4.15%            |
| 5         | \$24,624.72 | 65.00%         | \$1,344.12       | 5.46%            |
| 6         | \$37,565.02 | 52.55%         | \$2,541.92       | 6.77%            |
| 7         | \$52,628.59 | 40.10%         | \$4,249.78       | 8.08%            |
| 8         | \$67,180.39 | 27.65%         | \$6,303.78       | 9.38%            |
| 9         | \$77,391.81 | 15.20%         | \$8,274.48       | 10.69%           |
| 10        | \$79,520.08 | 2.75%          | \$9,542.41       | 12.00%           |

Revenues in year 10 reflect successful "high end auto" company revenues (Volvo, Audi, BMW etc.)

Pre-tax operating margin in year 10 is at the 75th pecentile of high end auto companies.

# Tesla: Reinvestment and Profitability

189

Operating losses carried forward  
save taxes in years 3 & 4

Sales/Capital  
measures revenues  
generated for every  
dollar of investment

Reinvestment =  
Change in  
Revenue/ Sales  
to capital

| Year | Revenues     | EBIT        | EBIT (1-t)  | Change in Revenues | Sales/Capital | Reinvestment | FCFF         | Invested Capital | ROIC   | Cost of Capital |
|------|--------------|-------------|-------------|--------------------|---------------|--------------|--------------|------------------|--------|-----------------|
| Base | \$ 2,013.50  | \$ (21.81)  | \$ (21.81)  |                    |               |              |              | \$ 1,045.00      | -2.09% | 8.74%           |
| 1    | \$ 3,322.28  | \$ 7.48     | \$ 7.48     | \$ 1,308.78        | 1.55          | \$ 844.37    | \$ (836.89)  | \$ 1,889.37      | 0.40%  | 8.74%           |
| 2    | \$ 5,481.75  | \$ 84.06    | \$ 84.06    | \$ 2,159.48        | 1.55          | \$ 1,393.21  | \$(1,309.15) | \$ 3,282.58      | 2.56%  | 8.74%           |
| 3    | \$ 9,044.89  | \$ 257.03   | \$ 254.44   | \$ 3,563.14        | 1.55          | \$ 2,298.80  | \$(2,044.36) | \$ 5,581.38      | 4.56%  | 8.74%           |
| 4    | \$ 14,924.07 | \$ 619.36   | \$ 402.58   | \$ 5,879.18        | 1.55          | \$ 3,793.02  | \$(3,390.44) | \$ 9,374.40      | 4.29%  | 8.74%           |
| 5    | \$ 24,624.72 | \$ 1,344.12 | \$ 873.68   | \$ 9,700.65        | 1.55          | \$ 6,258.48  | \$(5,384.81) | \$ 15,632.89     | 5.59%  | 8.59%           |
| 6    | \$ 37,565.02 | \$ 2,541.92 | \$ 1,652.25 | \$ 12,940.29       | 1.55          | \$ 8,348.58  | \$(6,696.33) | \$ 23,981.46     | 6.89%  | 8.44%           |
| 7    | \$ 52,628.59 | \$ 4,249.78 | \$ 2,762.36 | \$ 15,063.57       | 1.55          | \$ 9,718.43  | \$(6,956.08) | \$ 33,699.89     | 8.20%  | 8.29%           |
| 8    | \$ 67,180.39 | \$ 6,303.78 | \$ 4,097.46 | \$ 14,551.80       | 1.55          | \$ 9,388.26  | \$(5,290.81) | \$ 43,088.15     | 9.51%  | 8.15%           |
| 9    | \$ 77,391.81 | \$ 8,274.48 | \$ 5,378.41 | \$ 10,211.42       | 1.55          | \$ 6,588.01  | \$(1,209.60) | \$ 49,676.17     | 10.83% | 8.00%           |
| 10   | \$ 79,520.08 | \$ 9,542.41 | \$ 6,202.57 | \$ 2,128.27        | 1.55          | \$ 1,373.08  | \$ 4,829.49  | \$ 51,049.25     | 12.15% | 8.00%           |

*Tesla Story: Tesla will be able to grow efficiently (sales to capital ratio) and continue to generate excess returns as it gets bigger.*

Invested Capital in year t =  
Invested Capital in year t-1  
+ Reinvestment in year t

Cost of capital  
decreases as  
company gets larger  
and more profitable.

![](_page_189_Diagram_0.jpeg)

![]()The Big Enchilada

# Getting Closure in Valuation

¨ A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

¨ Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \sum_{t=1}^{t=\infty} \frac{\text{CF}_t}{(1+r)^t}$$

$$\text{Value} = \sum_{t=1}^{t=N} \frac{\text{CF}_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^N}$$

# Ways of Estimating Terminal Value

![](_page_192_Diagram_2.jpeg)

# 1. Obey the growth cap

¨ When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

g = Expected growth rate

- ¨ The stable growth rate cannot exceed the growth rate of the economy but it can be set lower.
  - If you assume that the economy is composed of high growth and stable growth firms, the growth rate of the latter will probably be lower than the growth rate of the economy.
  - The stable growth rate can be negative. The terminal value will be lower and you are assuming that your firm will disappear over time.
- If you use nominal cashflows and discount rates, the growth rate should be nominal in the currency in which the valuation is denominated. ¨ One simple proxy for the nominal growth rate of the economy is the riskfree rate.

# Risk free Rates and Nominal GDP Growth

¨ **Risk free Rate** = Expected Inflation + Expected Real Interest Rate ¨ The real interest rate is what borrowers agree to return to lenders in real goods/services. ¨ **Nominal GDP Growth** = Expected Inflation + Expected Real Growth ¨ The real growth rate in the economy measures the expected growth in the production of goods and services.

#### **The argument for Risk free rate = Nominal GDP growth**

- 1. In the long term, the real growth rate cannot be lower than the real interest rate, since you have the growth in goods/services has to be enough to cover the promised rate.
- 2. In the long term, the real growth rate can be higher than the real interest rate, to compensate risk taking. However, as economies mature, the difference should get smaller and since there will be growth companies in the economy, it is prudent to assume that the extra growth comes from these companies.

| Period    | 10-Year	T.Bond Rate | Inflation	Rate | Real	GDP	Growth | Nominal	GDP growth	rate | Nominal	GDP	- T.Bond Rate |
|-----------|---------------------|----------------|-----------------|-------------------------|---------------------------|
| 1954-2015 | 5.93%               | 3.61%          | 3.06%           | 6.67%                   | 0.74%                     |
| 1954-1980 | 5.83%               | 4.49%          | 3.50%           | 7.98%                   | 2.15%                     |
| 1981-2008 | 6.88%               | 3.26%          | 3.04%           | 6.30%                   | -0.58%                    |
| 2009-2015 | 2.57%               | 1.66%          | 1.47%           | 3.14%                   | 0.57%                     |

# A Practical Reason for using the Risk free Rate Cap – Preserve Consistency

¨ You are implicitly making assumptions about nominal growth in the economy, with your risk free rate. Thus, with a low risk free rate, you are assuming low nominal growth in the economy (with low inflation and low real growth) and with a high risk free rate, a high nominal growth rate in the economy. ¨ If you make an explicit assumption about nominal growth in cash flows that is at odds with your implicit growth assumption in the denominator, you are being inconsistent and bias your valuations: ¤ If you assume high nominal growth in the economy, with a low risk free rate, you will over value businesses. ¤ If you assume low nominal growth rate in the economy, with a high risk free rate, you will under value businesses.

# 2. Don't wait too long…

- ¨ Assume that you are valuing a young, high growth firm with great potential, just after its initial public offering. How long would you set your high growth period?
  - a. < 5 years
  - b. 5 years
  - c. 10 years
- d. >10 years ¨ While analysts routinely assume very long high growth periods (with substantial excess returns during the periods), the evidence suggests that they are much too optimistic. Most growth firms have difficulty sustaining their growth for long periods, especially while earning excess returns.

# And tie to competitive advantages

¨ Recapping a key lesson about growth, it is not growth per se that creates value but growth with excess returns. For growth firms to continue to generate value creating growth, they have to be able to keep the competition at bay. ¨ Proposition 1: The stronger and more sustainable the competitive advantages, the longer a growth company can sustain "value creating" growth. ¨ Proposition 2: Growth companies with strong and sustainable competitive advantages are rare.

# 3. Don't forget that growth has to be earned..

¨ In the section on expected growth, we laid out the fundamental equation for growth:

Growth rate = Reinvestment Rate \* Return on invested capital + Growth rate from improved efficiency

¨ In stable growth, you cannot count on efficiency delivering growth and you have to reinvest to deliver the growth rate that you have forecast. ¨ Consequently, your reinvestment rate in stable growth will be a function of your stable growth rate and what you believe the firm will earn as a return on capital in perpetuity: ¤ Reinvestment Rate = Stable growth rate/ Stable period ROC = g/ ROC ¨ Your terminal value equation can then be rewritten as:

Terminal Value in year 
$$n = \frac{\text{EBIT}_{n+1} (1-t)(1 - \frac{g}{\text{ROC}})}{(\text{Cost of Capital} - g)}$$

# The Big Assumption

|      | 6%      | 8%      | 10%     | 12%     | 14%     |
|------|---------|---------|---------|---------|---------|
| 0.0% | \$1,000 | \$1,000 | \$1,000 | \$1,000 | \$1,000 |
| 0.5% | \$965   | \$987   | \$1,000 | \$1,009 | \$1,015 |
| 1.0% | \$926   | \$972   | \$1,000 | \$1,019 | \$1,032 |
| 1.5% | \$882   | \$956   | \$1,000 | \$1,029 | \$1,050 |
| 2.0% | \$833   | \$938   | \$1,000 | \$1,042 | \$1,071 |
| 2.5% | \$778   | \$917   | \$1,000 | \$1,056 | \$1,095 |
| 3.0% | \$714   | \$893   | \$1,000 | \$1,071 | \$1,122 |

**200**

Terminal value for a firm with expected after-tax operating income of \$100 million in year n+1 and a cost of capital of 10%.

# Excess Returns to Zero?

¨ There are some (McKinsey, for instance) who argue that the return on capital should always be equal to cost of capital in stable growth. ¨ But excess returns seem to persist for very long time periods.

![](_page_200_Figure_7.jpeg)

![](_page_200_Figure_9.jpeg)

# And don't fall for sleight of hand…

¨ A typical assumption in many DCF valuations, when it comes to stable growth, is that capital expenditures offset depreciation and there are no working capital needs. Stable growth firms, we are told, just have to make maintenance cap ex (replacing existing assets ) to deliver growth. If you make this assumption, what expected growth rate can you use in your terminal value computation? ¨ What if the stable growth rate = inflation rate? Is it okay to make this assumption then?

# 4. Be internally consistent

¨ Risk and costs of equity and capital: Stable growth firms tend to ¤ Have betas closer to one ¤ Have debt ratios closer to industry averages (or mature company averages) ¤ Country risk premiums (especially in emerging markets should evolve over time) ¨ The excess returns at stable growth firms should approach (or become) zero. ROC -> Cost of capital and ROE -> Cost of equity ¨ The reinvestment needs and dividend payout ratios should reflect the lower growth and excess returns: ¤ Stable period payout ratio = 1 - g/ ROE ¤ Stable period reinvestment rate = g/ ROC

# BEYOND INPUTS: CHOOSING AND USING THE RIGHT MODEL

Choosing the right model

# Summarizing the Inputs

¨ In summary, at this stage in the process, we should have an estimate of the ¤ the current cash flows on the investment, either to equity investors (dividends or free cash flows to equity) or to the firm (cash flow to the firm) ¤ the current cost of equity and/or capital on the investment ¤ the expected growth rate in earnings, based upon historical growth, analysts forecasts and/or fundamentals ¨ The next step in the process is deciding ¤ which cash flow to discount, which should indicate ¤ which discount rate needs to be estimated and ¤ what pattern we will assume growth to follow

# Which cash flow should I discount?

#### ¨ Use Equity Valuation

(a) for firms which have stable leverage, whether high or not, and (b) if equity (stock) is being valued

#### ¨ Use Firm Valuation

(a) for firms which have leverage which is too high or too low, and expect to change the leverage over time, because debt payments and issues do not have to be factored in the cash flows and the discount rate (cost of capital) does not change dramatically over time.

(b) for firms for which you have partial information on leverage (eg: interest expenses are missing..)

(c) in all other cases, where you are more interested in valuing the firm than the equity. (Value Consulting?)

### Given cash flows to equity, should I discount dividends or FCFE?

#### ¨ Use the Dividend Discount Model

(a) For firms which pay dividends (and repurchase stock) which are close to the Free Cash Flow to Equity (over a extended period)

(b)For firms where FCFE are difficult to estimate (Example: Banks and Financial Service companies)

#### ¨ Use the FCFE Model

(a) For firms which pay dividends which are significantly higher or lower than the Free Cash Flow to Equity. (What is significant? ... As a rule of thumb, if dividends are less than 80% of FCFE or dividends are greater than 110% of FCFE over a 5-year period, use the FCFE model)

(b) For firms where dividends are not available (Example: Private Companies, IPOs)

# What discount rate should I use?

¨ Cost of Equity versus Cost of Capital ¤ If discounting cash flows to equity -> Cost of Equity ¤ If discounting cash flows to the firm -> Cost of Capital ¨ What currency should the discount rate (risk free rate) be in? ¤ Match the currency in which you estimate the risk free rate to the currency of your cash flows ¨ Should I use real or nominal cash flows? ¤ If discounting real cash flows -> real cost of capital ¤ If nominal cash flows -> nominal cost of capital ¤ If inflation is low (<10%), stick with nominal cash flows since taxes are based upon nominal income ¤ If inflation is high (>10%) switch to real cash flows

# Which Growth Pattern Should I use?

¨ If your firm is ¤ large and growing at a rate close to or less than growth rate of the economy, or ¤ constrained by regulation from growing at rate faster than the economy ¤ has the characteristics of a stable firm (average risk & reinvestment rates)

Use a Stable Growth Model

¨ If your firm ¤ is large & growing at a moderate rate (≤ Overall growth rate + 10%) or ¤ has a single product & barriers to entry with a finite life (e.g. patents)

Use a 2-Stage Growth Model

¨ If your firm ¤ is small and growing at a very high rate (> Overall growth rate + 10%) or ¤ has significant barriers to entry into the business ¤ has firm characteristics that are very different from the norm

Use a 3-Stage or n-stage Model

# The Building Blocks of Valuation

| <b>Choose a</b>    |                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                     |
|--------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cash Flow          | <i>Dividends</i><br><br>Expected Dividends to Stockholders | <i>Cashflows to Equity</i><br><br>Net Income<br>- (1- $\delta$ ) (Capital Exp. - Deprec'n)<br>- (1- $\delta$ ) Change in Work. Capital<br>= Free Cash flow to Equity (FCFE)<br>[ $\delta$ = Debt Ratio]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <i>Cashflows to Firm</i><br><br>EBIT (1- tax rate)<br>- (Capital Exp. - Deprec'n)<br>- Change in Work. Capital<br>= Free Cash flow to Firm (FCFF)                   |
| & A Discount Rate  |                                                            | <i>Cost of Equity</i><br><br>• <i>Basis</i> : The riskier the investment, the greater is the cost of equity.<br><br>• <i>Models</i> :<br><br>CAPM: Riskfree Rate + Beta (Risk Premium)<br><br>APM: Riskfree Rate + $\Sigma$ Beta <sub>j</sub> (Risk Premium <sub>j</sub> ): <i>n factors</i>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <i>Cost of Capital</i><br><br>WACC = $k_e ( E/ (D+E))$<br><br>+ $k_d ( D/(D+E))$<br><br>$k_d$ = Current Borrowing Rate (1-t)<br><br>E,D: Mkt Val of Equity and Debt |
| & a growth pattern |                                                            | <img alt="Graph of the choice of equity pattern for a growth pattern. The x-axis is time to take the form t-1. The y-axis is growth rate g. The choice between Stable Growth and Two-Stage Growth is indicated by a diagonal line. The Stable Growth pattern is a step up from the origin to a horizontal line at growth rate g. The Two-Stage Growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The diagonal line is at growth rate g. The stable growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The two-stage growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The diagonal line is at the same growth rate g. The stable growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The two-stage growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The diagonal line is at the same growth rate g. The stable growth pattern is a step up from the origin to a horizontal line at the same growth rate g. The two-stage growth pattern is a st |                                                                                                                                                                     |

![](_page_210_Picture_2.jpeg)

# But what comes next?

| <b>Value of Operating Assets</b>        | Since this is a discounted cashflow valuation, should there be a real option premium?                                                                                                                                       |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>+ Cash and Marketable Securities</b> | Operating versus Non-operating cash<br>Should cash be discounted for earning a low return?                                                                                                                                  |
| <b>+ Value of Cross Holdings</b>        | How do you value cross holdings in other companies?<br>What if the cross holdings are in private businesses?                                                                                                                |
| <b>+ Value of Other Assets</b>          | What about other valuable assets?<br>How do you consider under utilized assets?                                                                                                                                             |
| <b>Value of Firm</b>                    | Should you discount this value for opacity or complexity?<br>How about a premium for synergy?<br>What about a premium for intangibles (brand name)?                                                                         |
| <b>- Value of Debt</b>                  | What should be counted in debt?<br>Should you subtract book or market value of debt?<br>What about other obligations (pension fund and health care?<br>What about contingent liabilities?<br>What about minority interests? |
| <b>= Value of Equity</b>                | Should there be a premium/discount for control?<br>Should there be a discount for distress                                                                                                                                  |
| <b>- Value of Equity Options</b>        | What equity options should be valued here (vested versus non-vested)?<br>How do you value equity options?                                                                                                                   |
| <b>= Value of Common Stock</b>          | Should you divide by primary or diluted shares?                                                                                                                                                                             |
| <b>/ Number of shares</b>               |                                                                                                                                                                                                                             |
| <b>= Value per share</b>                | Should there be a discount for illiquidity/ marketability?<br>Should there be a discount for minority interests?                                                                                                            |

# 1. The Value of Cash

¨ The simplest and most direct way of dealing with cash and marketable securities is to keep it out of the valuation - the cash flows should be before interest income from cash and securities, and the discount rate should not be contaminated by the inclusion of cash. (Use betas of the operating assets alone to estimate the cost of equity). ¨ Once the operating assets have been valued, you should add back the value of cash and marketable securities. ¨ In many equity valuations, the interest income from cash is included in the cashflows. The discount rate has to be adjusted then for the presence of cash. (The beta used will be weighted down by the cash holdings). Unless cash remains a fixed percentage of overall value over time, these valuations will tend to break down.

# An Exercise in Cash Valuation

**214**

| Enterprise Value Cash      | Company	A \$1,000.0 \$100.0 | Company	B \$1,000.0 \$100.0 | Company	C \$1,000.0 \$100.0 |
|----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Return	on	invested	capital | 10%                         | 5%                          | 22%                         |
| Cost	of	capital            | 10%                         | 10%                         | 12%                         |
| Trades	in                  | US                          | US                          | Argentina                   |

In which of these companies is cash most likely to be

- a) A Neutral Asset (worth \$100 million)
- b) A Wasting Asset (worth less than \$100 million)
- c) A Potential Value Creator (worth >\$100 million)

### Should you ever discount cash for its low returns?

¨ There are some analysts who argue that companies with a lot of cash on their balance sheets should be penalized by having the excess cash discounted to reflect the fact that it earns a low return. ¤ Excess cash is usually defined as holding cash that is greater than what the firm needs for operations. ¤ A low return is defined as a return lower than what the firm earns on its non-cash investments. ¨ This is the wrong reason for discounting cash. If the cash is invested in riskless securities, it should earn a low rate of return. As long as the return is high enough, given the riskless nature of the investment, cash does not destroy value. ¨ There is a right reason, though, that may apply to some companies… Managers can do stupid things with cash (overpriced acquisitions, pie-in-the-sky projects….) and you have to discount for this possibility.

# Cash: Discount or Premium?

216

*Market Value of \$ 1 in cash:  
Estimates obtained by regressing Enterprise Value against Cash Balances*

![](_page_215_Figure_9.jpeg)

# A Detour: Closed End Mutual Funds

¨ Assume that you have a closed-end fund that invests in ' average risk" stocks. Assume also that you expect the market (average risk investments) to make 11.5% annually over the long term. If the closed end fund underperforms the market by 0.50%, estimate the discount on the fund.

![](_page_216_Figure_3.jpeg)

### The Most Famous Closed End Fund in History?

**218**

![](_page_217_Figure_3.jpeg)

#### *Berkshire Hathaway: The Fading Buffett Premium*

# 2. Dealing with Holdings in Other firms

¨ Holdings in other firms can be categorized into ¤ Minority passive holdings, in which case only the dividend from the holdings is shown in the balance sheet ¤ Minority active holdings, in which case the share of equity income is shown in the income statements ¤ Majority active holdings, in which case the financial statements are consolidated.

# An Exercise in Valuing Cross Holdings

¨ Assume that you have valued Company A using consolidated financials for \$ 1 billion (using FCFF and cost of capital) and that the firm has \$ 200 million in debt. How much is the equity in Company A worth? ¨ Now assume that you are told that Company A owns 10% of Company B and that the holdings are accounted for as passive holdings. If the market cap of company B is \$ 500 million, how much is the equity in Company A worth? ¨ Now add on the assumption that Company A owns 60% of Company C and that the holdings are fully consolidated. The minority interest in company C is recorded at \$ 40 million in Company A's balance sheet. How much is the equity in Company A worth? 

# More on Cross Holding Valuation

¨ Building on the previous example, assume that ¤ You have valued equity in company B at \$ 250 million (which is half the market's estimate of value currently) ¤ Company A is a steel company and that company C is a chemical company. Furthermore, assume that you have valued the equity in company C at \$250 million. ¤ Estimate the value of equity in company A.

### If you really want to value cross holdings right….

- ❑ Step 1: Value the parent company without any cross holdings. This will require using unconsolidated financial statements rather than consolidated ones.
- ❑ Step 2: Value each of the cross holdings individually. (If you use the market values of the cross holdings, you will build in errors the market makes in valuing them into your valuation.
- ❑ Step 3: The final value of the equity in the parent company with  $N$  cross holdings will be:
  - ❑ Value of un-consolidated parent company
  - ❑ - Debt of un-consolidated parent company
  - ❑ +  $\sum_{j=1}^{j=N} \% \text{ owned of Company } j * (\text{Value of Company } j - \text{Debt of Company } j)$

# Valuing Yahoo as the sum of its intrinsic pieces

| 100% of Yahoo! US Equity | + 35% of Yahoo! Japan Equity                | + 22.1% of Alibaba Equity                       | - Loose Ends =          | <b>Equity value= \$41,571</b><br><b>Per share = \$41.19</b> |
|--------------------------|---------------------------------------------|-------------------------------------------------|-------------------------|-------------------------------------------------------------|
| Operating assets =\$4383 | Operating assets = \$17,884                 | Operating assets = \$127,484                    | - Taxes due = \$5,017   |                                                             |
| + Cash = \$4,571         | + Cash = \$3,113                            | + Cash = \$27963                                | - Yahoo options = \$298 |                                                             |
| - Debt = \$1,591         | - Debt = \$0                                | - Debt = \$6,670                                |                         |                                                             |
| =Parent Equity = \$7,363 | Equity = \$20,997<br>35% of value = \$7,349 | Equity = \$145,587<br>22.1% of value = \$32,175 |                         |                                                             |

If you have to settle for an approximation, try this…

¨ For majority holdings, with full consolidation, convert the minority interest from book value to market value by applying a price to book ratio (based upon the sector average for the subsidiary) to the minority interest. ¤ Estimated market value of minority interest = Minority interest on balance sheet \* Price to Book ratio for sector (of subsidiary) ¤ Subtract this from the estimated value of the consolidated firm to get to value of the equity in the parent company. ¨ For minority holdings in other companies, convert the book value of these holdings (which are reported on the balance sheet) into market value by multiplying by the price to book ratio of the sector(s). Add this value on to the value of the operating assets to arrive at total firm value.

# Yahoo: A pricing game?

225

100% of Yahoo! US Equity

| EV/Sales* Sales = 0.63*<br>\$4672 = \$2,948 |
|---------------------------------------------|
| + Cash = \$4,571                            |
| - Debt = \$1,591                            |
| =Parent Equity = \$5,929                    |

+ 35% of Yahoo! Japan Equity

| EV/Sales* Sales = 7.91*<br>\$3929 = \$31,075 |
|----------------------------------------------|
| + Cash = \$3,113                             |
| - Debt = \$0                                 |
| Equity = \$34,188<br>35% of value = \$11,966 |

+ 22.1% of Alibaba Equity

| EV/Sales* Sales = 12.18*<br>\$7911 = \$96,331   |
|-------------------------------------------------|
| + Cash = \$27963                                |
| - Debt = \$6,670                                |
| Equity = \$117,623<br>22.1% of value = \$25,995 |

- Loose Ends =

| Taxes due =<br>\$4,011    |
|---------------------------|
| Yahoo<br>options<br>\$298 |

**Equity value= \$39,580  
Per share = \$39.19**

### 3. Other Assets that have not been counted yet..

¨ Assets that you should not be counting (or adding on to DCF values) ¤ If an asset is contributing to your cashflows, you cannot count the market value of the asset in your value. Thus, you should not be counting the real estate on which your offices stand, the PP&E representing your factories and other productive assets, any values attached to brand names or customer lists and definitely no non- assets (such as goodwill). ¨ Assets that you can count (or add on to your DCF valuation) ¤ Overfunded pension plans: If you have a defined benefit plan and your assets exceed your expected liabilities, you could consider the over funding with two caveats: n Collective bargaining agreements may prevent you from laying claim to these excess assets. n There are tax consequences. Often, withdrawals from pension plans get taxed at much higher rates. ¤ Unutilized assets: If you have assets or property that are not being utilized to generate cash flows (vacant land, for example), you have not valued them yet. You can assess a market value for these assets and add them on to the value of the firm.

# An Uncounted Asset?

227

Price tag: \$200 million

![](_page_226_Picture_24.jpeg)

The longtime home of Playboy magazine founder Hugh Hefner is to be sold to Daren Metropoulos, a principal at private-equity firm Metropoulos & Co. PHOTO: GETTY IMAGES

### 4. A Discount for Complexity: An Experiment

| Operating	Income | Company	A \$	1	billion | Company	B \$	1	billion |
|------------------|------------------------|------------------------|
| Tax	rate         | 40%                    | 40%                    |
| ROIC             | 10%                    | 10%                    |
| Expected	Growth  | 5%                     | 5%                     |
| Cost	of	capital  | 8%                     | 8%                     |
| Business	Mix     | Single                 | Multiple               |
| Holdings         | Simple                 | Complex                |
| Accounting       | Transparent            | Opaque                 |

Which firm would you value more highly?

### Measuring Complexity: Volume of Data in Financial Statements

| Company           | Number of pages in last 10Q | Number of pages in last 10K |
|-------------------|-----------------------------|-----------------------------|
| General Electric  | 65                          | 410                         |
| Microsoft         | 63                          | 218                         |
| Wal-mart          | 38                          | 244                         |
| Exxon Mobil       | 86                          | 332                         |
| Pfizer            | 171                         | 460                         |
| Citigroup         | 252                         | 1026                        |
| Intel             | 69                          | 215                         |
| AIG               | 164                         | 720                         |
| Johnson & Johnson | 63                          | 218                         |
| IBM               | 85                          | 353                         |

# Measuring Complexity: A Complexity Score

| Item                 | Factors                                                                | Follow-up Question                                      | Answer                                             | Weighting factor | Hyundai Heavy Score |
|----------------------|------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------|------------------|---------------------|
| Operating Income     | 1. Multiple Businesses                                                 | Number of businesses (with more than 10% of revenues) = | 3                                                  | 2.00             | 6                   |
|                      | 2. One-time income and expenses                                        | Percent of operating income =                           | 5%                                                 | 10.00            | 0.5                 |
|                      | 3. Income from unspecified sources                                     | Percent of operating income =                           | 15%                                                | 10.00            | 1.5                 |
|                      | 4. Items in income statement that are volatile                         | Percent of operating income =                           | 20%                                                | 5.00             | 1                   |
|                      | Tax Rate                                                               | 1. Income from multiple locales                         | Percent of revenues from non-domestic locales =    | 75%              | 3.00                |
| Capital Expenditures | 2. Different tax and reporting books                                   | Yes or No                                               | No                                                 | Yes=3            | 0                   |
|                      | 3. Headquarters in tax havens                                          | Yes or No                                               | No                                                 | Yes=3            | 0                   |
|                      | 4. Volatile effective tax rate                                         | Yes or No                                               | Yes                                                | Yes=2            | 2                   |
|                      | 1. Volatile capital expenditures                                       | Yes or No                                               | Yes                                                | Yes=2            | 2                   |
|                      | 2. Frequent and large acquisitions                                     | Yes or No                                               | No                                                 | Yes=4            | 0                   |
| Working capital      | 3. Stock payment for acquisitions and investments                      | Yes or No                                               | No                                                 | Yes=4            | 0                   |
|                      | 1. Unspecified current assets and current liabilities                  | Yes or No                                               | Yes                                                | Yes=3            | 3                   |
|                      | 2. Volatile working capital items                                      | Yes or No                                               | Yes                                                | Yes=2            | 2                   |
| Expected Growth rate | 1. Off-balance sheet assets and liabilities (operating leases and R&D) | Yes or No                                               | No                                                 | Yes=3            | 0                   |
|                      | 2. Substantial stock buybacks                                          | Yes or No                                               | No                                                 | Yes=3            | 0                   |
|                      | 3. Changing return on capital over time                                | Is your return on capital volatile?                     | Yes                                                | Yes=5            | 5                   |
|                      | 4. Unsustainably high return                                           | Is your firm's ROC much higher than industry average?   | Yes                                                | Yes=5            | 5                   |
|                      | Cost of capital                                                        | 1. Multiple businesses                                  | Number of businesses (more than 10% of revenues) = | 3                | 1.00                |
| No-operating assets  | 2. Operations in emerging markets                                      | Percent of revenues=                                    | 50%                                                | 5.00             | 2.5                 |
|                      | 3. Is the debt market traded?                                          | Yes or No                                               | No                                                 | No=2             | 2                   |
|                      | 4. Does the company have a rating?                                     | Yes or No                                               | No                                                 | No=2             | 2                   |
|                      | 5. Does the company have off-balance sheet debt?                       | Yes or No                                               | No                                                 | Yes=5            | 0                   |
|                      | No-operating assets                                                    | Minority holdings as percent of book assets             | Minority holdings as percent of book assets        | 30%              | 20.00               |
| Firm to Equity value | Consolidation of subsidiaries                                          | Minority interest as percent of book value of equity    | 20%                                                | 20.00            | 4                   |
| Per share value      | Shares with different voting rights                                    | Does the firm have shares with different voting rights? | No                                                 | Yes = 10         | 0                   |
|                      | Equity options outstanding                                             | Options outstanding as percent of shares                | 0%                                                 | 10.00            | 0                   |
|                      |                                                                        | Complexity Score =                                      |                                                    |                  | 49.75               |

# Dealing with Complexity

#### ¨ In Discounted Cashflow Valuation

¤ The Aggressive Analyst: Trust the firm to tell the truth and value the firm based upon the firm's statements about their value. ¤ The Conservative Analyst: Don't value what you cannot see. ¤ The Compromise: Adjust the value for complexity <sup>n</sup> Adjust cash flows for complexity <sup>n</sup> Adjust the discount rate for complexity <sup>n</sup> Adjust the expected growth rate/ length of growth period <sup>n</sup> Value the firm and then discount value for complexity

#### ¨ In relative valuation

¤ In a relative valuation, you may be able to assess the price that the market is charging for complexity: ¤ With the hundred largest market cap firms, for instance:

PBV = 0.65 + 15.31 ROE – 0.55 Beta + 3.04 Expected growth rate – 0.003 # Pages in 10K

#### 5. Be circumspect about defining debt for cost of capital purposes…

¨ General Rule: Debt generally has the following characteristics: ¤ Commitment to make fixed payments in the future ¤ The fixed payments are tax deductible ¤ Failure to make the payments can lead to either default or loss of control of the firm to the party to whom payments are due. ¨ Defined as such, debt should include ¤ All interest bearing liabilities, short term as well as long term ¤ All leases, operating as well as capital ¨ Debt should not include ¤ Accounts payable or supplier credit ¨ Be wary of your conservative impulses which will tell you to count everything as debt. That will push up the debt ratio and lead you to understate your cost of capital.

# Book Value or Market Value

- ¨ You are valuing a distressed telecom company and have arrived at an estimate of \$ 1 billion for the enterprise value (using a discounted cash flow valuation). The company has \$ 1 billion in face value of debt outstanding but the debt is trading at 50% of face value (because of the distress). What is the value of the equity to you as an investor?
  - a. The equity is worth nothing (EV minus Face Value of Debt)
- b. The equity is worth \$ 500 million (EV minus Market Value of Debt) ¨ Would your answer be different if you were told that the liquidation value of the assets of the firm today is \$1.2 billion and that you were planning to liquidate the firm today?

# But you should consider other potential liabilities when getting to equity value

- □ If you have under funded pension fund or health care plans, you should consider the under funding at this stage in getting to the value of equity.
  - □ If you do so, you should not double count by also including a cash flow line item reflecting cash you would need to set aside to meet the unfunded obligation.
  - □ You should not be counting these items as debt in your cost of capital calculations....
- □ If you have contingent liabilities - for example, a potential liability from a lawsuit that has not been decided - you should consider the expected value of these contingent liabilities
  - □ Value of contingent liability = Probability that the liability will occur \* Expected value of liability

# 6. Equity to Employees: Effect on Value

¨ In recent years, firms have turned to giving employees (and especially top managers) equity option or restricted stock packages as part of compensation. If they are options, they usually are long term and on volatile stocks. If restricted stock, the restrictions are usually on trading. ¨ These equity compensation packages are clearly valuable and the question becomes how best to deal with them in valuation. ¨ Two key issues with employee options: ¤ How do options or restricted stock granted in the past affect equity value per share today? ¤ How do expected grants of either in the future affect equity value today?

### The Easier Problem: Restricted Stock Grants

**Aswath Damodaran 236**

> ¨ When employee compensation takes the form of restricted stock grants, the solution is relatively simple. ¨ To account for restricted stock grants in the past, make sure that you count the restricted stock that have already been granted in shares outstanding today. That will reduce your value per share. ¨ To account for expected stock grants in the future, estimate the value of these grants as a percent of revenue and forecast that as expense as part of compensation expenses. That will reduce future income and cash flows.

# The Bigger Challenge: Employee Options

¨ It is true that options can increase the number of shares outstanding but dilution per se is not the problem. ¨ Options affect equity value at exercise because ¤ Shares are issued at below the prevailing market price. Options get exercised only when they are in the money. ¤ Alternatively, the company can use cashflows that would have been available to equity investors to buy back shares which are then used to meet option exercise. The lower cashflows reduce equity value. ¨ Options affect equity value before exercise because we have to build in the expectation that there is a probability of and a cost to exercise.

# A simple example…

¨ XYZ company has \$ 100 million in free cashflows to the firm, growing 3% a year in perpetuity and a cost of capital of 8%. It has 100 million shares outstanding and \$ 1 billion in debt. Its value can be written as follows:

Value of firm = 100 / (.08-.03) = 2000

Debt = 1000

= Equity = 1000

Value per share = 1000/100 = \$10

- ¨ XYZ decides to give 10 million options at the money (with a strike price of \$10) to its CEO. What effect will this have on the value of equity per share?
  - a. None. The options are not in-the-money.
  - b. Decrease by 10%, since the number of shares could increase by 10 million
  - c. Decrease by less than 10%. The options will bring in cash into the firm but they have time value.

# I. The Diluted Share Count Approach

¨ The simplest way of dealing with options is to try to adjust the denominator for shares that will become outstanding if the options get exercised. In the example cited, this would imply the following:

Value of firm = 
$$100 / (.08-.03) = 2000$$

Debt = 1000

= Equity = 1000

Number of diluted shares = 110

Value per share = 1000/110 = \$9.09

¨ The diluted approach fails to consider that exercising options will bring in cash into the firm. Consequently, they will overestimate the impact of options and understate the value of equity per share.

# II. The Treasury Stock Approach

¨ The treasury stock approach adds the proceeds from the exercise of options to the value of the equity before dividing by the diluted number of shares outstanding.

¨ In the example cited, this would imply the following:

Value of firm = 100 / (.08-.03) = 2000

Debt = 1000

= Equity = 1000

Number of diluted shares = 110

Proceeds from option exercise = 10 \* 10 = 100 

Value per share = (1000+ 100)/110 = \$ 10

¨ The treasury stock approach fails to consider the time premium on the options. The treasury stock approach also has problems with out-of-themoney options. If considered, they can increase the value of equity per share. If ignored, they are treated as non-existent.

# III. Option Value Drag

¨ Step 1: Value the firm, using discounted cash flow or other valuation models. ¨ Step 2: Subtract out the value of the outstanding debt to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly. ¨ Step 3:Subtract out the market value (or estimated market value) of other equity claims: ¤ Value of Warrants = Market Price per Warrant \* Number of Warrants : Alternatively estimate the value using option pricing model ¤ Value of Conversion Option = Market Value of Convertible Bonds - Value of Straight Debt Portion of Convertible Bonds ¤ Value of employee Options: Value using the average exercise price and maturity. ¨ Step 4:Divide the remaining value of equity by the number of shares outstanding to get value per share.

#### Valuing Equity Options issued by firms… The Dilution Problem

¨ Option pricing models can be used to value employee options with four caveats – ¤ Employee options are long term, making the assumptions about constant variance and constant dividend yields much shakier, ¤ Employee options result in stock dilution, and ¤ Employee options are often exercised before expiration, making it dangerous to use European option pricing models. ¤ Employee options cannot be exercised until the employee is vested. ¨ These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and early exercise, and factoring in the dilution effect. The resulting value can be adjusted for the probability that the employee will not be vested.

### Valuing Employee Options

¨ To value employee options, you need the following inputs into the option valuation model: ¤ Stock Price = \$ 10, Adjusted for dilution = \$9.58 ¤ Strike Price = \$ 10 ¤ Maturity = 10 years (Can reduce to reflect early exercise) ¤ Standard deviation in stock price = 40% ¤ Riskless Rate = 4% ¨ Using a dilution-adjusted Black Scholes model, we arrive at the following inputs: ¤ N (d1) = 0.8199 ¤ N (d2) = 0.3624 ¤ Value per call = \$ 9.58 (0.8199) - \$10 e -(0.04) (10)(0.3624) = \$5.42

### Value of Equity to Value of Equity per share

¨ Using the value per call of \$5.42, we can now estimate the value of equity per share after the option grant:

Value of firm = 
$$100 / (.08-.03) = 2000$$

Debt = 1000

= Equity = 1000

Value of options granted = \$ 54.2

= Value of Equity in stock = \$945.8

/ Number of shares outstanding / 100

= Value per share = \$ 9.46

¨ Note that this approach yields a higher value than the diluted share count approach (which ignores exercise proceeds) and a lower value than the treasury stock approach (which ignores the time premium on the options)

# To tax adjust or not to tax adjust…

¨ In the example above, we have assumed that the options do not provide any tax advantages. To the extent that the exercise of the options creates tax advantages, the actual cost of the options will be lower by the tax savings. ¨ One simple adjustment is to multiply the value of the options by (1- tax rate) to get an after-tax option cost.

# Option grants in the future…

¨ Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value. ¨ The simplest mechanism for bringing in future option grants into the analysis is to do the following: ¤ Estimate the value of options granted each year over the last few years as a percent of revenues. ¤ Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller. ¤ Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.

When options affect equity value per share the most…

¨ Option grants affect value more ¤ The lower the strike price is set relative to the stock price ¤ The longer the term to maturity of the option ¤ The more volatile the stock price ¨ The effect on value will be magnified if companies are allowed to revisit option grants and reset the exercise price if the stock price moves down.

# NARRATIVE AND NUMBERS: VALUATION AS A BRIDGE

Tell me a story..

# Valuation as a bridge

# The Numbers People

#### **Favored Tools** - Accounting statements - Excel spreadsheets - Statistical Measures - Pricing Data

#### **Illusions/Delusions** 1. Precision: Data is precise 2. Objectivity: Data has no bias 3. Control: Data can control reality

# The Narrative People

#### **Favored Tools** - Anecdotes - Experience (own or others) - Behavioral evidence

#### **Illusions/Delusions** 1. Creativity cannot be quantified 2. If the story is good, the investment will be. 3. Experience is the best teacher

# A Good Valuation

#### *Number Crunchers Story Tellers*

# Step 1: Survey the landscape

¨ Every valuation starts with a narrative, a story that you see unfolding for your company in the future. ¨ In developing this narrative, you will be making assessments of ¤ Your company (its products, its management and its history. ¤ The market or marketsthat you see it growing in. ¤ The competitionitfaces and will face. ¤ The macro environmentin which it operates.

![](_page_250_Diagram_16.jpeg)

# Step 2: Create a narrative for the future

¨ Every valuation starts with a narrative, a story that you see unfolding for your company in the future. ¨ In developing this narrative, you will be making assessments of your company (its products, its management), the market or markets that you see it growing in, the competition it faces and will face and the macro environment in which it operates. ¤ Rule 1: Keep it simple. ¤ Rule 2: Keep it focused. ¤ Rule 3: Stay grounded in reality.

# The Uber Narrative

In June 2014, my initial narrative for Uber was that it would be

- 1. An urban car service business: I saw Uber primarily as a force in urban areas and only in the car service business.
- 2. Which would expand the business moderately (about 40% over ten years) by bringing in new users.
- 3. With local networking benefits: If Uber becomes large enough in any city, it will quickly become larger, but that will be of little help when it enters a new city.
- 4. Maintain its revenue sharing (20%) system due to strong competitive advantages(from being a first mover).
- 5. And its existing low-capital business model, with drivers as contractors and very little investment in infrastructure.

# Step 3: Check the narrative against history, economic first principles & common sense

![](_page_253_Diagram_2.jpeg)

# The Impossible, The Implausible and the Improbable

255

## The Impossible

### **Bigger than the economy**

Assuming Growth rate for company in perpetuity > Growth rate for economy

### **Bigger than the total market**

Allowing a company's revenues to grow so much that it has more than a 100% market share of whatever business it is in.

### **Profit margin > 100%**

Assuming earnings growth will exceed revenue growth for a long enough period, and pushing margins above 100%

### **Depreciation without cap ex**

Assuming that depreciation will exceed cap ex in perpetuity.

## The Implausible

### **Growth without reinvestment**

Assuming growth forever without reinvestment.

### **Profits without competition**

Assuming that your company will grow and earn higher profits, with no competition.

### **Returns without risk**

Assuming that you can generate high returns in a business with no risk.

## The Improbable

![](_page_254_Diagram_41.jpeg)

# Uber: Possible, Plausible and Probable

![](_page_255_Picture_4.jpeg)

![](_page_255_Diagram_5.jpeg)

| Board Member     | Designation                   | Age |
|------------------|-------------------------------|-----|
| Henry Kissinger  | Former Secretary of State     | 92  |
| Bill Perry       | Former Secretary of Defense   | 88  |
| George Schultz   | Former Secretary of State     | 94  |
| Bill Frist       | Former Senate Majority Leader | 63  |
| Sam Nunn         | Former Senator                | 77  |
| Gary Roughead    | Former Navy Admiral           | 64  |
| James Mattis     | Former Marine Corps General   | 65  |
| Dick Kovocovich  | Former CEO of Wells Fargo     | 72  |
| Riley Bechtel    | Former CEO of Bechtel         | 63  |
| William Foege    | Epidemologist                 | 79  |
| Elizabeth Holmes | Founder & CEO, Theranos       | 31  |
| Sunny Balwani    | President & COO, Theranos     | NA  |

![](_page_256_Figure_10.jpeg)

The Story The Checks (?)

+ Money

+

#### The Impossible: The Runaway Story

![](_page_256_Picture_2.jpeg)

![](_page_256_Picture_3.jpeg)

#### The Implausible: The Big Market Delusion

![](_page_257_Diagram_1.jpeg)

![](_page_257_Diagram_2.jpeg)

| Company             | Market Cap            | Enterprise Value      | Current Revenues    | Breakeven Revenues (2025) | % from Online Advertising | Imputed Online Ad Revenue (2025) |
|---------------------|-----------------------|-----------------------|---------------------|---------------------------|---------------------------|----------------------------------|
| Google              | \$441,572.00          | \$386,954.00          | \$69,611.00         | \$224,923.20              | 89.50%                    | \$201,306.26                     |
| Facebook            | \$245,662.00          | \$234,696.00          | \$14,640.00         | \$129,375.54              | 92.20%                    | \$119,284.12                     |
| Yahoo!              | \$30,614.00           | \$23,836.10           | \$4,871.00          | \$25,413.13               | 100.00%                   | \$25,413.13                      |
| LinkedIn            | \$23,265.00           | \$20,904.00           | \$2,561.00          | \$22,371.44               | 80.30%                    | \$17,964.26                      |
| Twitter             | \$16,927.90           | \$14,912.90           | \$1,779.90          | \$23,128.68               | 89.50%                    | \$20,700.17                      |
| Pandora             | \$3,643.00            | \$3,271.00            | \$1,024.00          | \$2,915.67                | 79.50%                    | \$2,317.96                       |
| Yelp                | \$1,765.00            | \$0.00                | \$465.00            | \$1,144.26                | 93.60%                    | \$1,071.02                       |
| Zillow              | \$4,496.00            | \$4,101.00            | \$480.00            | \$4,156.21                | 18.00%                    | \$748.12                         |
| Zynga               | \$2,241.00            | \$1,142.00            | \$752.00            | \$757.86                  | 22.10%                    | \$167.49                         |
| <b>Total US</b>     | <b>\$770,185.90</b>   | <b>\$689,817.00</b>   | <b>\$96,183.00</b>  | <b>\$434,185.98</b>       |                           | <b>\$388,972.66</b>              |
| Alibaba             | \$184,362.00          | \$173,871.00          | \$12,598.00         | \$111,414.06              | 60.00%                    | \$66,848.43                      |
| Tencent             | \$154,366.00          | \$151,554.00          | \$13,969.00         | \$63,730.36               | 10.50%                    | \$6,691.69                       |
| Baidu               | \$49,991.00           | \$44,864.00           | \$9,172.00          | \$30,999.49               | 98.90%                    | \$30,658.50                      |
| Sohu.com            | \$18,240.00           | \$17,411.00           | \$1,857.00          | \$16,973.01               | 53.70%                    | \$9,114.51                       |
| Naver               | \$13,699.00           | \$12,686.00           | \$2,755.00          | \$12,139.34               | 76.60%                    | \$9,298.74                       |
| Yandex              | \$3,454.00            | \$3,449.00            | \$972.00            | \$2,082.52                | 98.80%                    | \$2,057.52                       |
| Yahoo! Japan        | \$23,188.00           | \$18,988.00           | \$3,591.00          | \$5,707.61                | 69.40%                    | \$3,961.08                       |
| Sina                | \$2,113.00            | \$746.00              | \$808.00            | \$505.09                  | 48.90%                    | \$246.99                         |
| Netease             | \$14,566.00           | \$11,257.00           | \$2,388.00          | \$840.00                  | 11.90%                    | \$3,013.71                       |
| Mail.ru             | \$3,492.00            | \$3,768.00            | \$636.00            | \$1,676.47                | 35.00%                    | \$586.76                         |
| Mixi                | \$3,095.00            | \$2,661.00            | \$1,229.00          | \$777.02                  | 96.00%                    | \$745.94                         |
| Kakaku              | \$3,565.00            | \$3,358.00            | \$404.00            | \$1,650.49                | 11.60%                    | \$191.46                         |
| <b>Total non-US</b> | <b>\$474,131.00</b>   | <b>\$444,613.00</b>   | <b>\$50,379.00</b>  | <b>\$248,495.46</b>       |                           | <b>\$133,415.32</b>              |
| <b>Global Total</b> | <b>\$1,244,316.90</b> | <b>\$1,134,430.00</b> | <b>\$146,562.00</b> | <b>\$682,681.44</b>       |                           | <b>\$522,387.98</b>              |

# The Improbable: Willy Wonkitis

## Tesla: Summary 15-year DCF Analysis (DCF valuation as of mid-year 2013)

|                                     | FY 2013      | FY 2014      | FY 2015      | FY 2016      | FY 2017       | FY 2018       | FY 2019       | FY 2020       | FY 2021       | FY 2022       | FY 2023          | FY 2024       | FY 2025       | FY 2026                       | FY 2027       | FY 2028       |
|-------------------------------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|---------------|---------------|------------------|---------------|---------------|-------------------------------|---------------|---------------|
| Unit Volume                         | 24,298       | 36,883       | 64,684       | 86,713       | 149,869       | 214,841       | 291,861       | 384,747       | 466,559       | 550,398       | 643,850          | 726,655       | 820,645       | 922,481                       | 1,034,215     | 1,137,780     |
| % Growth                            | 52%          | 70%          | 34%          | 73%          | 43%           | 36%           | 32%           | 21%           | 18%           | 17%           | 17%              | 13%           | 13%           | 12%                           | 12%           | 10%           |
| Automotive Revenue Per Unit (\$)    | 93,403       | 85,342       | 83,432       | 78,932       | 65,465        | 58,258        | 56,407        | 55,553        | 55,991        | 56,586        | 56,969           | 57,540        | 58,138        | 58,603                        | 59,002        | 59,554        |
| % Growth                            | -9%          | -2%          | -5%          | -17%         | -11%          | -3%           | -2%           | 1%            | 1%            | 1%            | 1%               | 1%            | 1%            | 1%                            | 1%            | 1%            |
| Automotive Sales                    | 2,462        | 3,321        | 5,613        | 7,051        | 10,025        | 12,720        | 16,885        | 21,595        | 26,347        | 31,357        | 36,897           | 42,022        | 47,949        | 54,283                        | 61,221        | 67,980        |
| Development Service Sales           | 16           | 40           | 42           | 44           | 46            | 49            | 51            | 54            | 56            | 59            | 62               | 65            | 68            | 72                            | 75            | 79            |
| <b>Total Sales</b>                  | <b>2,478</b> | <b>3,361</b> | <b>5,655</b> | <b>7,095</b> | <b>10,072</b> | <b>12,768</b> | <b>16,736</b> | <b>21,648</b> | <b>26,403</b> | <b>31,416</b> | <b>36,959</b>    | <b>42,087</b> | <b>48,017</b> | <b>54,355</b>                 | <b>61,296</b> | <b>68,059</b> |
| % Growth                            |              | 36%          | 68%          | 25%          | 42%           | 27%           | 31%           | 29%           | 22%           | 19%           | 18%              | 14%           | 14%           | 13%                           | 13%           | 11%           |
| <b>EBITDA</b>                       | <b>148</b>   | <b>417</b>   | <b>920</b>   | <b>1,042</b> | <b>1,586</b>  | <b>2,150</b>  | <b>3,138</b>  | <b>4,066</b>  | <b>4,857</b>  | <b>5,723</b>  | <b>6,328</b>     | <b>7,182</b>  | <b>8,144</b>  | <b>9,888</b>                  | <b>10,874</b> | <b>12,099</b> |
| % Margin                            | 6.0%         | 12.4%        | 16.3%        | 14.7%        | 15.7%         | 16.8%         | 18.7%         | 18.8%         | 18.4%         | 18.2%         | 17.1%            | 17.1%         | 17.0%         | 17.8%                         | 17.7%         | 17.8%         |
| D&A                                 | 103          | 158          | 172          | 203          | 301           | 353           | 389           | 537           | 606           | 696           | 811              | 938           | 1,088         | 1,260                         | 1,451         | 1,661         |
| % of Capax                          | 41%          | 79%          | 55%          | 65%          | 62%           | 69%           | 78%           | 86%           | 79%           | 77%           | 79%              | 78%           | 76%           | 76%                           | 76%           | 77%           |
| <b>EBIT</b>                         | <b>45</b>    | <b>259</b>   | <b>748</b>   | <b>839</b>   | <b>1,285</b>  | <b>1,796</b>  | <b>2,749</b>  | <b>3,529</b>  | <b>4,252</b>  | <b>5,027</b>  | <b>5,517</b>     | <b>6,244</b>  | <b>7,056</b>  | <b>8,429</b>                  | <b>9,423</b>  | <b>10,439</b> |
| % Margin                            | 1.8%         | 7.7%         | 13.2%        | 11.8%        | 12.8%         | 14.1%         | 16.4%         | 16.3%         | 16.1%         | 16.0%         | 14.9%            | 14.8%         | 14.7%         | 15.5%                         | 15.4%         | 15.3%         |
| Net Interest Income (Expense)       | (27)         | (1)          | 9            | 33           | 47            | 90            | 108           | 155           | 199           | 278           | 358              | 445           | 542           | 651                           | 784           | 934           |
| Other Income                        | 28           | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0                | 0             | 0             | 0                             | 0             | 0             |
| <b>Pretax Income</b>                | <b>46</b>    | <b>258</b>   | <b>758</b>   | <b>872</b>   | <b>1,332</b>  | <b>1,886</b>  | <b>2,857</b>  | <b>3,684</b>  | <b>4,451</b>  | <b>5,305</b>  | <b>5,875</b>     | <b>6,658</b>  | <b>7,598</b>  | <b>9,080</b>                  | <b>10,207</b> | <b>11,373</b> |
| Income Taxes                        | 3            | 2            | 14           | 34           | 86            | 262           | 462           | 641           | 807           | 1,003         | 1,134            | 1,317         | 1,470         | 1,761                         | 2,028         | 2,323         |
| % Effective Rate                    | 6%           | 1%           | 2%           | 4%           | 6%            | 14%           | 16%           | 17%           | 18%           | 19%           | 19%              | 20%           | 19%           | 19%                           | 20%           | 20%           |
| <b>Net Income</b>                   | <b>44</b>    | <b>256</b>   | <b>744</b>   | <b>839</b>   | <b>1,246</b>  | <b>1,624</b>  | <b>2,395</b>  | <b>3,043</b>  | <b>3,644</b>  | <b>4,303</b>  | <b>4,741</b>     | <b>5,372</b>  | <b>6,128</b>  | <b>7,319</b>                  | <b>8,179</b>  | <b>9,050</b>  |
| <b>Pilot</b>                        |              |              |              |              |               |               |               |               |               |               |                  |               |               |                               |               |               |
| After-tax Interest Expense (Income) | 27           | 1            | (9)          | (33)         | (47)          | (90)          | (108)         | (154)         | (199)         | (278)         | (357)            | (444)         | (541)         | (650)                         | (782)         | (932)         |
| Depreciation of PP&E                | 103          | 158          | 172          | 203          | 301           | 353           | 389           | 537           | 606           | 696           | 811              | 938           | 1,088         | 1,260                         | 1,451         | 1,661         |
| Other                               | 0            | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0                | 0             | 0             | 0                             | 0             | 0             |
| <b>Less</b>                         |              |              |              |              |               |               |               |               |               |               |                  |               |               |                               |               |               |
| Change in Working Capital           | (155)        | (14)         | (157)        | (167)        | (172)         | (325)         | (163)         | (81)          | (28)          | (299)         | (356)            | (328)         | (219)         | (329)                         | (365)         | (376)         |
| % of Change in Sales                | -2%          | -7%          | -12%         | -6%          | -12%          | -4%           | -2%           | -1%           | -6%           | -6%           | -6%              | -4%           | -5%           | -5%                           | -6%           | -6%           |
| Capital Expenditures                | 250          | 200          | 312          | 312          | 486           | 510           | 497           | 623           | 765           | 906           | 1,078            | 1,236         | 1,437         | 1,660                         | 1,898         | 2,149         |
| % of Sales                          | 10%          | 6%           | 6%           | 4%           | 5%            | 4%            | 3%            | 3%            | 3%            | 3%            | 3%               | 3%            | 3%            | 3%                            | 3%            | 3%            |
| Other                               | 0            | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0                | 0             | 0             | 0                             | 0             | 0             |
| <b>Unlevered Free Cash Flow</b>     | <b>78</b>    | <b>229</b>   | <b>750</b>   | <b>863</b>   | <b>1,186</b>  | <b>1,702</b>  | <b>2,343</b>  | <b>2,884</b>  | <b>3,314</b>  | <b>4,113</b>  | <b>4,472</b>     | <b>4,959</b>  | <b>5,456</b>  | <b>6,597</b>                  | <b>7,315</b>  | <b>8,005</b>  |
| EBITDA                              |              |              |              |              |               |               |               |               |               |               |                  |               |               | 12,099                        |               |               |
| Sales                               |              |              |              |              |               |               |               |               |               |               |                  |               |               | 68,059                        |               |               |
| Net Debt (Cash)                     |              |              |              |              |               |               |               |               |               |               |                  |               |               | (260)                         |               |               |
| Tesla Diluted Shares                |              |              |              |              |               |               |               |               |               |               |                  |               |               | 142                           |               |               |
| Ext EBITDA High                     |              |              |              |              | 12.0 x        |               |               |               |               |               |                  |               |               |                               |               |               |
| Ext EBITDA Low                      |              |              |              |              | 8.0 x         |               | Ext PPG High  |               | 5.0%          |               | Ext P/Sales High |               | 180%          |                               |               |               |
|                                     |              |              |              |              |               |               | Ext PPG Low   |               | 3.0%          |               | Ext P/Sales Low  |               | 130%          |                               |               |               |
| Discount Rate High                  |              |              |              |              |               |               |               |               |               |               |                  |               |               | 13.0%                         |               |               |
| Discount Rage Low                   |              |              |              |              |               |               |               |               |               |               |                  |               |               | 9.0%                          |               |               |
| FY Month of Valuation               |              |              |              |              |               |               |               |               |               |               |                  |               |               | 1.0 (Beginning of this Month) |               |               |
| Month of FY End                     |              |              |              |              |               |               |               |               |               |               |                  |               |               | 12.0 (End of this Month)      |               |               |

# Step 4: Connect your narrative to key drivers of value

![](_page_259_Diagram_1.jpeg)

# Step 4: Value the company (Uber)

261

## Uber: Intrinsic valuation - June 8, 2014 (in US \$)

![](_page_260_Figure_10.jpeg)

# Step 5: Keep the feedback loop

- 1. Not just car service company.: Uber is a car company, not just a car service company, and there may be a day when consumers will subscribe to a Uberservice, rather than own their own cars. It could also expand into logistics, i.e., moving and transportation businesses.
- 2. Not just urban: Uber can create new demands for car service in parts of the country where taxis are not used (suburbia, small towns).
- 3. Global networking benefits: By linking with technology and credit card companies, Uber can have global networking benefits.

# Valuing Bill Gurley's Uber narrative

|                      | <i>Uber (Gurley)</i>                                                                                                                                                                                                                                                       | <i>Uber (Gurley Mod)</i>                                                                                                                                                                                                                                                  | <i>Uber (Damodaran)</i>                                                                                                                                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Narrative            | Uber will <u>expand the car service market substantially, bringing in mass transit users &amp; non-users from the suburbs into the market, and use its <u>networking advantage</u> to gain a <u>dominant market share</u>, while maintaining its revenue slice at 20%.</u> | Uber will <u>expand the car service market substantially, bringing in mass transit users &amp; non-users from the suburbs into the market, and use its <u>networking advantage</u> to gain a <u>dominant market share</u>, while cutting prices and margins (to 10%).</u> | Uber will expand the car service market moderately, primarily in urban environments, and use its <u>competitive advantages</u> to get a <u>significant but not dominant market share</u> and maintain its revenue slice at 20%. |
| Total Market         | \$300 billion, growing at 3% a year                                                                                                                                                                                                                                        | \$300 billion, growing at 3% a year                                                                                                                                                                                                                                       | \$100 billion, growing at 6% a year                                                                                                                                                                                             |
| Market Share         | 40%                                                                                                                                                                                                                                                                        | 40%                                                                                                                                                                                                                                                                       | 10%                                                                                                                                                                                                                             |
| Uber's revenue slice | 20%                                                                                                                                                                                                                                                                        | 10%                                                                                                                                                                                                                                                                       | 20%                                                                                                                                                                                                                             |
| Value for Uber       | \$53.4 billion + Option value of entering car ownership market (\$10 billion+)                                                                                                                                                                                             | \$28.7 billion + Option value of entering car ownership market (\$6 billion+)                                                                                                                                                                                             | \$5.9 billion + Option value of entering car ownership market (\$2-3 billion)                                                                                                                                                   |

# Different narratives, Different Numbers

| <i>Total Market</i>   | <i>Growth Effect</i>       | <i>Network Effect</i>             | <i>Competitive Advantages</i> | <i>Value of Uber</i> |
|-----------------------|----------------------------|-----------------------------------|-------------------------------|----------------------|
| A4. Mobility Services | B4. Double market size     | C5. Strong global network effects | D4. Strong & Sustainable      | \$90,457             |
| A3. Logistics         | B4. Double market size     | C5. Strong global network effects | D4. Strong & Sustainable      | \$65,158             |
| A4. Mobility Services | B3. Increase market by 50% | C3. Strong local network effects  | D3. Semi-strong               | \$52,346             |
| A2. All car service   | B4. Double market size     | C5. Strong global network effects | D4. Strong & Sustainable      | \$47,764             |
| A1. Urban car service | B4. Double market size     | C5. Strong global network effects | D4. Strong & Sustainable      | \$31,952             |
| A3. Logistics         | B3. Increase market by 50% | C3. Strong local network effects  | D3. Semi-strong               | \$14,321             |
| A1. Urban car service | B3. Increase market by 50% | C3. Strong local network effects  | D3. Semi-strong               | \$7,127              |
| A2. All car service   | B3. Increase market by 50% | C3. Strong local network effects  | D3. Semi-strong               | \$4,764              |
| A4. Mobility Services | B1. None                   | C1. No network effects            | D1. None                      | \$1,888              |
| A3. Logistics         | B1. None                   | C1. No network effects            | D1. None                      | \$1,417              |
| A2. All car service   | B1. None                   | C1. No network effects            | D1. None                      | \$1,094              |
| A1. Urban car service | B1. None                   | C1. No network effects            | D1. None                      | \$799                |

# Step 6: Be ready to modify narrative as events unfold

| Narrative Break/End                                                                                                                           | Narrative Shift                                                                                                  | Narrative Change<br>(Expansion or Contraction)                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Events, external (legal, political or economic) or internal (management, competitive, default), that can cause the narrative to break or end. | Improvement or deterioration in initial business model, changing market size, market share and/or profitability. | Unexpected entry/success in a new market or unexpected exit/failure in an existing market.   |
| Your valuation estimates (cash flows, risk, growth & value) are no longer operative                                                           | Your valuation estimates will have to be modified to reflect the new data about the company.                     | Valuation estimates have to be redone with new overall market potential and characteristics. |
| Estimate a probability that it will occur & consequences                                                                                      | Monte Carlo simulations or scenario analysis                                                                     | Real Options                                                                                 |

![]()Let's have some fun!

# Equity Risk Premiums in Valuation

¨ The equity risk premiums that I have used in the valuations that follow reflect my thinking (and how it has evolved) on the issue. ¤ Pre-1998 valuations: In the valuations prior to 1998, I use a risk premium of 5.5% for mature markets (close to both the historical and the implied premiums then) ¤ Between 1998 and Sept 2008: In the valuations between 1998 and September 2008, I used a risk premium of 4% for mature markets, reflecting my belief that risk premiums in mature markets do not change much and revert back to historical norms (at least for implied premiums). ¤ Valuations done in 2009: After the 2008 crisis and the jump in equity risk premiums to 6.43% in January 2008, I have used a higher equity risk premium (5-6%) for the next 5 years and will assume a reversion back to historical norms (4%) only after year 5. ¤ After 2009: In 2010, I reverted back to a mature market premium of 4.5%, reflecting the drop in equity risk premiums during 2009. In 2011, I used 5%, reflecting again the change in implied premium over the year. In 2012 and 2013, stayed with 6%, reverted to 5% in 2014 and will be using 5.75% in 2015.

# The Valuation Set up

¨ With each company that I value in this next section, I will try to start with a story about the company and use that story to construct a valuation. ¨ With each valuation, rather than focus on all of the details (which will follow the blueprint already laid out), I will focus on a specific component of the valuation that is unique or different.

Stocks that look like Bonds, Things Change and Market Valuations

# **<sup>269</sup>** Training Wheels On?

#### *Training Wheels valuation: Con Ed in August 2008*

In trailing 12 months, through June Dividend payout ratio is 73%

2008 Earnings per share = \$3.17

Dividends per share = \$2.32

#### **Why a stable growth dividend discount model?**

- 1. Why stable growth: Company is a regulated utility, restricted from investing in new growth markets. Growth is constrained by the fact that the population (and power needs) of its customers in New York are growing at very low rates. Growth rate forever = 2%
- 2. Why equity: Company's debt ratio has been stable at about 70% equity, 30% debt for decades.
- 3. Why dividends: Company has paid out about 97% of its FCFE as dividends over the last five years.

Riskfree rate 4.10% 10-year T.Bond rate Beta 0.80 Beta for regulated power utilities

Equity Risk Premium 4.5% Implied Equity Risk Premium - US market in 8/2008

Cost of Equity = 4.1% + 0.8 (4.5%) = 7.70%

*Growth rate forever = 2.1%*

Value per share today= Expected Dividends per share next year / (Cost of equity - Growth rate) = 2.32 (1.021)/ (.077 - ,021) = \$42.30

> **On August 12, 2008 Con Ed was trading at \$ 40.76.**

#### **Test 2: Is the stable growth rate consistent with fundamentals?**

Retention Ratio = 27%

ROE =Cost of equity = 7.7%

Expected growth = 2.1%

#### **Test 3: Is the firm's risk and cost of equity consistent with a stable growith firm?**

Beta of 0.80 is at lower end of the range of stable company betas: 0.8 -1.2

#### **Test 1: Is the firm paying dividends like a stable growth firm?**

#### A break even growth rate to get to market price…

![](_page_270_Figure_3.jpeg)

*Con Ed: Value versus Growth Rate*

### From DCF value to target price and returns…

¨ Assume that you believe that your valuation of Con Ed (\$42.30) is a fair estimate of the value, 7.70% is a reasonable estimate of Con Ed's cost of equity and that your expected dividends for next year (2.32\*1.021) is a fair estimate, what is the expected stock price a year from now (assuming that the market corrects its mistake?) ¨ If you bought the stock today at \$40.76, what return can you expect to make over the next year (assuming again that the market corrects its mistake)?

#### **Current Cashflow to Firm**

EBIT(1-t)= 5344 (1-**.35**)= 3474 - Nt CpX= 350 - Chg WC 691 = FCFF 2433 Reinvestment Rate = 1041/3474 =29.97% Return on capital = 25.19%

**Expected Growth in EBIT (1-t)** .30\*.25=.075 **7.5%**

**Stable Growth** g = 3%; Beta = 1.10; Debt Ratio= 20%; Tax rate=35% Cost of capital = 6.76% ROC= 6.76%; Reinvestment Rate=3/6.76=44%

Terminal Value5= 2645/(.0676-.03) = 70,409

**Cost of Equity 8.32%**

**Cost of Debt** (3.72%+.75%)(1-.35) = 2.91%

**Weights** E = 92% D = 8%

| Op. Assets | 60607 |
|------------|-------|
| + Cash:    | 3253  |
| - Debt     | 4920  |
| =Equity    | 58400 |

**Riskfree Rate**: Riskfree rate = 3.72%

+

**Beta**  1.15 **X** **Risk Premium** 4%

Unlevered Beta for Sectors: 1.09

#### 3M: A Pre-crisis valuation

Reinvestment Rate 30%

Return on Capital 25%

> Term Yr \$4,758 \$2,113 \$2,645

On September 12, 2008, 3M was trading at \$70/share

First 5 years

D/E=8.8%

| Year           | 1       | 2       | 3       | 4       | 5         |
|----------------|---------|---------|---------|---------|-----------|
| EBIT (1-t)     | \$3,734 | \$4,014 | \$4,279 | \$4,485 | \$4,619   |
| - Reinvestment | \$1,120 | \$1,204 | \$1,312 | \$1,435 | \$1,540 , |
| = FCFF         | \$2,614 | \$2,810 | \$2,967 | \$3,049 | \$3,079   |

#### **Current Cashflow to Firm**

EBIT(1-t)= 4810 (1-**.35**)= 3,180

- Nt CpX= 350

- Chg WC 691

= FCFF 2139

Reinvestment Rate = 1041/3180

=33%

Return on capital = 23.06%

**Expected Growth in** 

**EBIT (1-t)**

.25\*.20=.05

**5%**

**Stable Growth**

g = 3%; Beta = 1.00;; ERP =4%

Debt Ratio= 8%; Tax rate=35%

Cost of capital = 7.55%

ROC= 7.55%;

Reinvestment Rate=3/7.55=40%

Terminal Value5= 2434/(.0755-.03) = 53,481

**Cost of Equity**

**10.86%**

**Cost of Debt**

(3.96%+.1.5%)(1-.35)

= 3.55%

**Weights**

E = 92% D = 8%

| Op. Assets | 43,975 |                |         |         |         |         |                 |
|------------|--------|----------------|---------|---------|---------|---------|-----------------|
| + Cash:    | 3253   |                |         |         |         |         |                 |
| - Debt     | 4920   |                |         |         |         |         |                 |
| =Equity    | 42308  |                |         |         |         |         |                 |
|            |        | Year           | 1       | 2       | 3       | 4       | 5 Term Yr       |
|            |        | EBIT (1-t)     | \$3,339 | \$3,506 | \$3,667 | \$3,807 | \$3,921 \$4,038 |
|            |        | - Reinvestment | \$835   | \$877   | \$1,025 | \$1,288 | \$1,558 \$1,604 |
|            |        | = FCFF         | \$2,504 | \$2,630 | \$2,642 | \$2,519 | \$2,363 \$2,434 |

Value/Share \$ 60.53

**Riskfree Rate**:

Riskfree rate = 3.96%

+

**Beta** 

1.15 **X**

**Risk Premium**

6%

Unlevered Beta for

Sectors: 1.09

#### 3M: Post-crisis valuation

Reinvestment Rate

25%

Return on Capital

20%

On October 16, 2008, MMM was trading at \$57/share.

First 5 years

D/E=8.8%

Cost of capital = 10.86% (0.92) + 3.55% (0.08) = 10.27%

*Lowered base operating income by 10%*

*Reduced growth* 

*rate to 5%*

I*ncreased risk premium to 6% for next 5 years*

*Higher default spread for next 5 years*

*Did not increase debt ratio in stable growth to 20%*

![](_page_274_Diagram_4.jpeg)

#### *From a Company to the Market: Valuing the S&P 500: Dividend Discount Model in January 2015*

#### **Rationale for model**

Why dividends? Because it is the only tangible cash flow, right?

Why 2-stage? Because the expected growth rate in near term is higher than stable growth rate.

![](_page_275_Diagram_4.jpeg)

#### *From a Company to the Market: Valuing the S&P 500: Augmented Dividend Discount Model in January 2015*

#### **Rationale for model**

Why augmented dividends? Because companies are increasing returning cash in the form of stock buybacks

Why 2-stage? Because the expected growth rate in near term is higher than stable growth rate.

![](_page_276_Diagram_4.jpeg)

#### *Valuing the S&P 500: Augmented Dividends and Fundamental Growth January 2015*

#### **Rationale for model**

Why augmented dividends? Because companies are increasing returning cash in the form of stock buybacks

Why 2-stage? Why not?

Anyone can value a company that is stable, makes money and has an established business model!

# **<sup>278</sup>** The Dark Side of Valuation

# The fundamental determinants of value…

What are the **cashflows from existing assets**?

- Equity: Cashflows after debt payments
- Firm: Cashflows before debt payments

What is the **value added** by growth assets?

Equity: Growth in equity earnings/ cashflows

Firm: Growth in operating earnings/ cashflows

How **risky are the cash flows** from both existing assets and growth assets?

Equity: Risk in equity in the company

Firm: Risk in the firm's operations

When will the firm become a **mature fiirm**, and what are the potential roadblocks?

# The Dark Side of Valuation…

¨ Valuing stable, money making companies with consistent and clear accounting statements, a long and stable history and lots of comparable firms is easy to do. ¨ The true test of your valuation skills is when you have to value "difficult" companies. In particular, the challenges are greatest when valuing: ¤ Young companies, early in the life cycle, in young businesses ¤ Companies that don't fit the accounting mold ¤ Companies that face substantial truncation risk (default or nationalization risk)

# Difficult to value companies…

#### ¨ Across the life cycle:

¤ Young, growth firms: Limited history, small revenues in conjunction with big operating losses and a propensity for failure make these companies tough to value. ¤ Mature companies in transition: When mature companies change or are forced to change, history may have to be abandoned and parameters have to be reestimated. ¤ Declining and Distressed firms: A long but irrelevant history, declining markets, high debt loads and the likelihood of distress make them troublesome.

#### ¨ Across markets

¤ Emerging market companies are often difficult to value because of the way they are structured, their exposure to country risk and poor corporate governance.

#### ¨ Across sectors

¤ Financial service firms: Opacity of financial statements and difficulties in estimating basic inputs leave us trusting managers to tell us what's going on. ¤ Commodity and cyclical firms: Dependence of the underlying commodity prices or overall economic growth make these valuations susceptible to macro factors. ¤ Firms with intangible assets: Accounting principles are left to the wayside on these firms.

# I. The challenge with young companies…

**282**

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets?

When will the firm become a mature fiirm, and what are the potential roadblocks?

 *Cash flows from existing assets non-existent or negative.* 

> *Limited historical data on earnings, and no market prices for securities makes it difficult to assess risk.*

*Making judgments on revenues/ profits difficult becaue you cannot draw on history. If you have no product/ service, it is difficult to gauge market potential or profitability. The company;s entire value lies in future growth but you have little to base your estimate on.* 

> *Will the firm will make it through the gauntlet of market demand and competition. Even if it does, assessing when it will become mature is difficult because there is so little to go on.*

What is the value of equity in the firm?

*Different claims on cash flows can affect value of equity at each stage.*

#### Upping the ante.. Young companies in young businesses…

¨ When valuing a business, we generally draw on three sources of information ¤ The firm's current financial statement <sup>n</sup> How much did the firm sell? <sup>n</sup> How much did it earn? ¤ The firm's financial history, usually summarized in its financial statements. <sup>n</sup> How fast have the firm's revenues and earnings grown over time? <sup>n</sup> What can we learn about cost structure and profitability from these trends? <sup>n</sup> Susceptibility to macro-economic factors (recessions and cyclical firms) ¤ The industry and comparable firm data <sup>n</sup> What happens to firms as they mature? (Margins.. Revenue growth… Reinvestment needs… Risk) ¨ It is when valuing these companies that you find yourself tempted by the dark side, where ¤ "Paradigm shifts" happen… ¤ New metrics are invented … ¤ The story dominates and the numbers lag…

![](_page_283_Diagram_1.jpeg)

**Cost of Equity**

**12.90%**

**Cost of Debt** 6.5%+1.5%=8.0% Tax rate = 0% -> 35% **Weights** Debt= 1.2% -> 15%

**Riskfree Rate**: T. Bond rate = 6.5% +

**Beta**

1.60 -> 1.00 **X Risk Premium** 4%

Internet/ Retail

Operating Leverage

Current D/E: 1.21% Base Equity Premium

Country Risk Premium

Cost of Capital 12.84% 12.84% 12.84% 12.83% 12.81% 12.13% 11.96% 11.69% 11.15% 9.61%

Amazon was trading at \$84 in January 2000.

*Dot.com retailers for firrst 5 years Convetional retailers after year 5*

*Used average interest coverage ratio over next 5 years to get BBB* 

*rating. Pushed debt ratio to retail industry average of 15%.*

*All existing options valued as options, using current stock price of \$84.*

# Lesson 1: Don't sweat the small stuff

![](_page_284_Figure_1.jpeg)

¨ Spotlight the business the company is in & use the beta of that business. ¨ Don't try to incorporate failure risk into the discount rate. ¨ Let the cost of capital change over time, as the company changes. ¨ If you are desperate, use the cross section of costs of capital to get your estimation going (use the 90th or 95th percentile across all companies).

# Lesson 2: Work backwards and keep it simple...

| Year       | Revenue Growth | Sales    | Operating Margin | EBIT    | EBIT (1-t) |
|------------|----------------|----------|------------------|---------|------------|
| Tr 12 mths |                | \$1,117  | -36.71%          | -\$410  | -\$410     |
| 1          | 150.00%        | \$2,793  | -13.35%          | -\$373  | -\$373     |
| 2          | 100.00%        | \$5,585  | -1.68%           | -\$94   | -\$94      |
| 3          | 75.00%         | \$9,774  | 4.16%            | \$407   | \$407      |
| 4          | 50.00%         | \$14,661 | 7.08%            | \$1,038 | \$871      |
| 5          | 30.00%         | \$19,059 | 8.54%            | \$1,628 | \$1,058    |
| 6          | 25.20%         | \$23,862 | 9.27%            | \$2,212 | \$1,438    |
| 7          | 20.40%         | \$28,729 | 9.64%            | \$2,768 | \$1,799    |
| 8          | 15.60%         | \$33,211 | 9.82%            | \$3,261 | \$2,119    |
| 9          | 10.80%         | \$36,798 | 9.91%            | \$3,646 | \$2,370    |
| 10         | 6.00%          | \$39,006 | 9.95%            | \$3,883 | \$2,524    |
| TY         | 6.00%          | \$41,346 | 10.00%           | \$4,135 | \$2,688    |

# Lesson 3: Scaling up is hard to do & failure is common

Typically, the revenue growth rate of a newly public company outpaces its industry average for only about five years.

![](_page_286_Figure_41.jpeg)

Source: Andrew Metrick

The New York Times

- □ Lower revenue growth rates, as revenues scale up.
- □ Keep track of dollar revenues, as you go through time, measuring against market size.

# Lesson 4: Don't forget to pay for growth...

| Year       | Revenues | $\Delta$ Revenue | Sales/Cap | $\Delta$ Investment | Invested Capital | EBIT (1-t) | Imputed ROC |
|------------|----------|------------------|-----------|---------------------|------------------|------------|-------------|
| Tr 12 mths | \$1,117  |                  |           |                     | \$ 487           | -\$410     |             |
| 1          | \$2,793  | \$1,676          | 3.00      | \$559               | \$ 1,045         | -\$373     | -76.62%     |
| 2          | \$5,585  | \$2,793          | 3.00      | \$931               | \$ 1,976         | -\$94      | -8.96%      |
| 3          | \$9,774  | \$4,189          | 3.00      | \$1,396             | \$ 3,372         | \$407      | 20.59%      |
| 4          | \$14,661 | \$4,887          | 3.00      | \$1,629             | \$ 5,001         | \$871      | 25.82%      |
| 5          | \$19,059 | \$4,398          | 3.00      | \$1,466             | \$ 6,467         | \$1,058    | 21.16%      |
| 6          | \$23,862 | \$4,803          | 3.00      | \$1,601             | \$ 8,068         | \$1,438    | 22.23%      |
| 7          | \$28,729 | \$4,868          | 3.00      | \$1,623             | \$ 9,691         | \$1,799    | 22.30%      |
| 8          | \$33,211 | \$4,482          | 3.00      | \$1,494             | \$ 11,185        | \$2,119    | 21.87%      |
| 9          | \$36,798 | \$3,587          | 3.00      | \$1,196             | \$ 12,380        | \$2,370    | 21.19%      |
| 10         | \$39,006 | \$2,208          | 3.00      | \$736               | \$ 13,116        | \$2,524    | 20.39%      |
| TY         | \$41,346 | \$2,340          | NA        |                     | Assumed to be =  |            | 20.00%      |

# Lesson 5: The dilution is taken care off..

¨ With young growth companies, it is almost a given that the number of shares outstanding will increase over time for two reasons: ¤ To grow, the company will have to issue new shares either to raise cash to take projects or to offer to target company stockholders in acquisitions ¤ Many young, growth companies also offer options to managers as compensation and these options will get exercised, if the company is successful. ¨ In DCF valuation, both effects are already incorporated into the value per share, even though we use the current number of shares in estimating value per share ¤ The need for new equity issues is captured in negative cash flows in the earlier years. The present value of these negative cash flows will drag down the current value of equity and this is the effect of future dilution. ¤ The options are valued and netted out against the current value. Using an option pricing model allows you to incorporate the expected likelihood that they will be exercised and the price at which they will be exercised.

# Lesson 6: If you are worried about failure, incorporate into value

![](_page_289_Figure_1.jpeg)

# Lesson 7: There are always scenarios where the market price can be justified…

|     | 6%        | 8%       | 10%       | 12%       | 14%       |
|-----|-----------|----------|-----------|-----------|-----------|
| 30% | \$ (1.94) | \$ 2.95  | \$ 7.84   | \$ 12.71  | \$ 17.57  |
| 35% | \$ 1.41   | \$ 8.37  | \$ 15.33  | \$ 22.27  | \$ 29.21  |
| 40% | \$ 6.10   | \$ 15.93 | \$ 25.74  | \$ 35.54  | \$ 45.34  |
| 45% | \$ 12.59  | \$ 26.34 | \$ 40.05  | \$ 53.77  | \$ 67.48  |
| 50% | \$ 21.47  | \$ 40.50 | \$ 59.52  | \$ 78.53  | \$ 97.54  |
| 55% | \$ 33.47  | \$ 59.60 | \$ 85.72  | \$ 111.84 | \$ 137.95 |
| 60% | \$ 49.53  | \$ 85.10 | \$ 120.66 | \$ 156.22 | \$ 191.77 |

# Lesson 8: You will be wrong 100% of the tim and it really is not your fault...

- □ No matter how careful you are in getting your inputs and how well structured your model is, your estimate of value will change both as new information comes out about the company, the business and the economy.
- □ As information comes out, you will have to adjust and adapt your model to reflect the information. Rather than be defensive about the resulting changes in value, recognize that this is the essence of risk.
- □ A test: If your valuations are unbiased, you should find yourself increasing estimated values as often as you are decreasing values. In other words, there should be equal doses of good and bad news affecting valuations (at least over time).

And the market is often "more wrong"….

![](_page_292_Figure_2.jpeg)

#### **Amazon: Value and Price**

# Assessing my 2000 forecasts, in 2014

| Year       | Revenues           |          | Operating Income   |          | Operating Margin   |         |         |
|------------|--------------------|----------|--------------------|----------|--------------------|---------|---------|
|            | My forecast (2000) | Actual   | My forecast (2000) | Actual   | My forecast (2000) | Actual  |         |
| 2000       | \$2,793            | \$2,762  | -\$                | 373      | -\$                | -13.35% | -24.04% |
| 2001       | \$5,585            | \$3,122  | -\$                | 94       | -\$                | -1.68%  | -7.40%  |
| 2002       | \$9,774            | \$3,932  | \$                 | 407      | \$                 | 4.16%   | 2.70%   |
| 2003       | \$14,661           | \$5,264  | \$                 | 1,038    | \$                 | 7.08%   | 5.15%   |
| 2004       | \$19,059           | \$6,921  | \$                 | 1,628    | \$                 | 8.54%   | 6.36%   |
| 2005       | \$23,862           | \$8,490  | \$                 | 2,212    | \$                 | 9.27%   | 5.09%   |
| 2006       | \$28,729           | \$10,711 | \$                 | 2,768    | \$                 | 9.63%   | 3.63%   |
| 2007       | \$33,211           | \$14,835 | \$                 | 3,261    | \$                 | 9.82%   | 4.42%   |
| 2008       | \$36,798           | \$19,166 | \$                 | 3,646    | \$                 | 9.91%   | 4.39%   |
| 2009       | \$39,006           | \$24,509 | \$                 | 3,883    | \$                 | 9.95%   | 4.61%   |
| 2010       | \$41,346           | \$34,204 | \$                 | 4,135    | \$                 | 10.00%  | 4.11%   |
| 2011       | \$43,827           | \$48,077 | \$                 | 4,383    | \$                 | 10.00%  | 1.79%   |
| 2012       | \$46,457           | \$61,093 | \$                 | 4,646    | \$                 | 10.00%  | 1.11%   |
| 2013       | \$49,244           | \$74,452 | \$                 | 4,925    | \$                 | 10.00%  | 1.00%   |
| 2014 (LTM) | \$51,460           | \$85,247 | \$                 | 5,146.35 | \$                 | 10.00%  | 0.11%   |

# Amazon: My "Field of Dreams" Valuation – October 2014

To deliver this high revenue growth, Amazon will continue to sell its products/services at or below cost. Operating margin stays low for the next few years.

Amazon will continue on its path of revenue growth first, pushing into media & cloud services to become the second largest retailer in the world. Revenues grow @15% a year for 5 years, tapering down to 2.2% growth after year 10

|                         | Base year | 1          | 2          | 3          | 4          | 5          | 6         | 7         | 8         | 9         | 10        | Terminal year |
|-------------------------|-----------|------------|------------|------------|------------|------------|-----------|-----------|-----------|-----------|-----------|---------------|
| Revenue growth rate     |           | 15.00%     | 15.00%     | 15.00%     | 15.00%     | 15.00%     | 12.44%    | 9.88%     | 7.32%     | 4.76%     | 2.20%     | 2.20%         |
| Revenues                | \$ 85,246 | \$98,033   | \$112,738  | \$129,649  | \$149,096  | \$171,460  | \$192,790 | \$211,837 | \$227,344 | \$238,166 | \$243,405 | \$ 248,760    |
| EBIT (Operating) margin | 0.58%     | 1.26%      | 1.94%      | 2.62%      | 3.30%      | 3.98%      | 4.66%     | 5.34%     | 6.02%     | 6.70%     | 7.38%     | 7.38%         |
| EBIT (Operating income) | \$ 494    | \$ 1,235   | \$ 2,187   | \$ 3,397   | \$ 4,920   | \$ 6,824   | \$ 8,984  | \$ 11,312 | \$ 13,686 | \$ 15,957 | \$ 17,963 | \$ 18,358     |
| Tax rate                | 31.80%    | 31.80%     | 31.80%     | 31.80%     | 31.80%     | 31.80%     | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%        |
| EBIT(1-t)               | \$ 337    | \$ 842     | \$ 1,492   | \$ 2,317   | \$ 3,356   | \$ 4,654   | \$ 6,127  | \$ 7,715  | \$ 9,334  | \$ 10,883 | \$ 12,251 | \$ 12,520     |
| - Reinvestment          |           | \$ 3,474   | \$ 3,995   | \$ 4,594   | \$ 5,284   | \$ 6,076   | \$ 5,795  | \$ 5,175  | \$ 4,213  | \$ 2,940  | \$ 1,424  | \$ 2,755      |
| FCFF                    |           | \$ (2,632) | \$ (2,504) | \$ (2,278) | \$ (1,928) | \$ (1,422) | \$ 332    | \$ 2,540  | \$ 5,121  | \$ 7,943  | \$ 10,827 | \$ 9,766      |
| Terminal Value          |           |            |            |            |            |            |           |           |           |           | \$168,379 |               |
| Cost of capital         |           | 8.39%      | 8.39%      | 8.39%      | 8.39%      | 8.39%      | 8.32%     | 8.24%     | 8.16%     | 8.08%     | 8.00%     | 8.00%         |
| PV(FCFF)                |           | \$ (2,489) | \$ (2,189) | \$ (1,842) | \$ (1,446) | \$ (994)   | \$ 169    | \$ 1,420  | \$ 2,681  | \$ 3,865  | \$ 80,918 |               |

As Amazon becomes more dominant, it will increase prices, but easy entry into the business will act as a restraint. Operating margin improves to 7.38% in year 10, weighted average of retail & media businesses

Amazon will be able to invest more efficiently that the average retailer. Reinvest \$1 for every \$3.68 in additional revenues

| PV(Terminal value)              | \$ 76,029 |
|---------------------------------|-----------|
| PV (CF over next 10 years)      | \$ 4,064  |
| Value of operating assets =     | \$ 80,093 |
| - Debt                          | \$ 8,353  |
| + Cash                          | \$ 10,252 |
| Value of equity                 | \$ 81,143 |
| - Value of options              | \$ -      |
| Value of equity in common stock | \$ 81,125 |
| Number of shares                | 463.01    |
| Estimated value /share          | \$ 175.25 |
| Price                           | \$ 287.06 |
| Price as % of value             | 163.84%   |

Amazon's technology twist will keep financial leverage low: Debt ratio is 94.7% equity, 5.3% debt, with a pre-tax cost of debt of 5.00%.

Amazon's risk profile will reflect a mix of retail, media and cloud businesses as well as geographic ambitions: Beta used in cost of capital is 1.12, weighted average of online retail, entertainment and business services (cloud). ERP is weighted average of US ERP (5%) and rest of the world (6.45%)

Amazon: A DCF valuation in late October 2014

# Amazon: World Dominator in October 2014

To deliver this high revenue growth, Amazon will continue to sell its products/services at or below cost. Operating margin stays low for the next few years.

Amazon will continue on its path of revenue growth first, pushing **strongly** into media & cloud services to become the second largest retailer in the world. Revenues grow @20% a year for 5 years, tapering down to 2.2% growth after year 10

|                                 | Base year | 1            | 2         | 3         | 4         | 5         | 6         | 7         | 8         | 9         | 10        | Terminal year |
|---------------------------------|-----------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------------|
| Revenue growth rate             |           | 20.00%       | 20.00%    | 20.00%    | 20.00%    | 20.00%    | 16.44%    | 12.88%    | 9.32%     | 5.76%     | 2.20%     | 2.20%         |
| Revenues                        | \$ 85,246 | \$102,295    | \$122,754 | \$147,305 | \$176,766 | \$212,119 | \$246,992 | \$278,804 | \$304,789 | \$322,345 | \$329,436 | \$ 336,684    |
| EBIT (Operating) margin         | 0.47%     | 1.71%        | 2.94%     | 4.18%     | 5.42%     | 6.65%     | 7.89%     | 9.13%     | 10.37%    | 11.60%    | 12.84%    | 12.84%        |
| EBIT (Operating income)         | \$ 400    | \$ 1,746     | \$ 3,613  | \$ 6,158  | \$ 9,576  | \$ 14,116 | \$ 19,492 | \$ 25,451 | \$ 31,594 | \$ 37,401 | \$ 42,300 | \$ 43,230     |
| Tax rate                        | 31.80%    | 31.80%       | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%    | 31.80%        |
| EBIT(1-t)                       | \$ 273    | \$ 1,190     | \$ 2,464  | \$ 4,200  | \$ 6,531  | \$ 9,627  | \$ 13,293 | \$ 17,358 | \$ 21,547 | \$ 25,508 | \$ 28,848 | \$ 29,483     |
| - Reinvestment                  |           | \$ 4,632     | \$ 5,559  | \$ 6,670  | \$ 8,004  | \$ 9,605  | \$ 9,475  | \$ 8,643  | \$ 7,060  | \$ 4,770  | \$ 1,927  | \$ 5,405      |
| FCFF                            |           | -\$ 3,442    | -\$ 3,094 | -\$ 2,470 | -\$ 1,473 | \$ 22     | \$ 3,819  | \$ 8,715  | \$ 14,487 | \$ 20,738 | \$ 26,922 | \$ 24,078     |
| Cost of capital                 |           | 8.39%        | 8.39%     | 8.39%     | 8.39%     | 8.39%     | 8.32%     | 8.24%     | 8.16%     | 8.08%     | 8.00%     | 8.00%         |
| Cumulated discount factor       |           | 0.9226       | 0.8511    | 0.7852    | 0.7244    | 0.6683    | 0.6170    | 0.5700    | 0.5271    | 0.4877    | 0.4515    |               |
| PV(FCFF)                        |           | \$3,175      | \$2,634   | \$1,940   | \$1,067   | \$15      | \$2,356   | \$4,968   | \$7,636   | \$10,113  | \$12,156  |               |
| Terminal value                  |           | \$415,134.21 |           |           |           |           |           |           |           |           |           |               |
| PV(Terminal value)              |           | \$187,447.77 |           |           |           |           |           |           |           |           |           |               |
| PV (CF over next 10 years)      |           | \$ 28,427.49 |           |           |           |           |           |           |           |           |           |               |
| Value of operating assets =     |           | \$215,875.26 |           |           |           |           |           |           |           |           |           |               |
| - Debt                          |           | \$ 9,201.58  |           |           |           |           |           |           |           |           |           |               |
| + Cash                          |           | \$ 10,252.00 |           |           |           |           |           |           |           |           |           |               |
| + Non-operating assets          |           | \$ -         |           |           |           |           |           |           |           |           |           |               |
| Value of equity                 |           | \$216,925.67 |           |           |           |           |           |           |           |           |           |               |
| - Value of options              |           | \$ -         |           |           |           |           |           |           |           |           |           |               |
| Value of equity in common stock |           | 216,925.67   |           |           |           |           |           |           |           |           |           |               |
| Number of shares                |           | 463.01       |           |           |           |           |           |           |           |           |           |               |
| Estimated value /share          |           | \$ 468.51    |           |           |           |           |           |           |           |           |           |               |

As Amazon becomes more dominant, it will increase prices, **with few restraints**. Operating margin improves to 12.84% in year 10, the 75th percentile of retail & media businesses

Amazon will be able to invest more efficiently than the average retailer. Reinvest \$1 for every \$3.68 in additional revenues

Amazon's risk profile will reflect a mix of retail, media and cloud businesses as well as geographic ambitions: Beta used in cost of capital is 1.12, weighted average of online retail, entertainment and business services (cloud). ERP is weighted average of US ERP (5%) and rest of the world (6.45%)

# Amazon: Bezos, the Change-maker

To deliver this high revenue growth, Amazon will continue to sell its products/services at or below cost. Operating margin stays low for the next few years.

Amazon will continue on its path of revenue growth first, pushing into media & cloud services to become the second largest retailer in the world. Revenues grow @15% a year for 5 years, tapering down to 2.2% growth after year 10

|                           | Base year | 1           | 2           | 3           | 4           | 5           | 6           | 7           | 8          | 9          | 10          | Terminal year |
|---------------------------|-----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|------------|------------|-------------|---------------|
| Revenue growth rate       |           | 15.00%      | 15.00%      | 15.00%      | 15.00%      | 15.00%      | 12.44%      | 9.88%       | 7.32%      | 4.76%      | 2.20%       | 2.20%         |
| Revenues                  | \$ 85,246 | \$ 98,033   | \$ 112,738  | \$ 129,649  | \$ 149,096  | \$ 171,460  | \$ 192,790  | \$ 211,837  | \$ 227,344 | \$ 238,166 | \$ 243,405  | \$ 248,760    |
| EBIT (Operating) margin   | 0.47%     | 0.71%       | 0.95%       | 1.18%       | 1.42%       | 1.66%       | 1.90%       | 2.14%       | 2.37%      | 2.61%      | 2.85%       | 2.85%         |
| EBIT (Operating income)   | \$ 400    | \$ 693      | \$ 1,066    | \$ 1,534    | \$ 2,120    | \$ 2,846    | \$ 3,659    | \$ 4,524    | \$ 5,397   | \$ 6,221   | \$ 6,937    | \$ 7,090      |
| Tax rate                  | 31.80%    | 31.80%      | 31.80%      | 31.80%      | 31.80%      | 31.80%      | 31.80%      | 31.80%      | 31.80%     | 31.80%     | 31.80%      | 31.80%        |
| EBIT(1-t)                 | \$ 273    | \$ 473      | \$ 727      | \$ 1,046    | \$ 1,446    | \$ 1,941    | \$ 2,495    | \$ 3,086    | \$ 3,681   | \$ 4,243   | \$ 4,731    | \$ 4,835      |
| - Reinvestment            |           | \$ 3,474    | \$ 3,995    | \$ 4,594    | \$ 5,284    | \$ 6,076    | \$ 5,795    | \$ 5,175    | \$ 4,213   | \$ 2,940   | \$ 1,424    | \$ 1,064      |
| FCFF                      |           | \$ (3,001)  | \$ (3,268)  | \$ (3,548)  | \$ (3,838)  | \$ (4,136)  | \$ (3,300)  | \$ (2,089)  | \$ (532)   | \$ 1,302   | \$ 3,307    | \$ 3,771      |
| Cost of capital           |           | 8.39%       | 8.39%       | 8.39%       | 8.39%       | 8.39%       | 8.32%       | 8.24%       | 8.16%      | 8.08%      | 8.00%       | 8.00%         |
| Cumulated discount factor |           | 0.9226      | 0.8511      | 0.7852      | 0.7244      | 0.6683      | 0.6170      | 0.5700      | 0.5271     | 0.4877     | 0.4515      |               |
| PV(FCFF)                  |           | -\$2,768.76 | -\$2,781.71 | -\$2,785.95 | -\$2,780.38 | -\$2,763.78 | -\$2,036.06 | -\$1,191.09 | -\$ 280.58 | -\$ 635.12 | \$ 1,493.45 |               |

| PV(Terminal value)              | \$29,361 |
|---------------------------------|----------|
| PV (CF over next 10 years)      | \$15,260 |
| Value of operating assets =     | \$14,101 |
| - Debt                          | \$9,202  |
| + Cash                          | \$10,252 |
| Value of equity                 | \$15,151 |
| - Value of options              | \$0      |
| Value of equity in common stock | \$15,151 |
| Number of shares                | 463.01   |
| Estimated value /share          | \$ 32.72 |

Amazon's technology twist will keep financial leverage low: Debt ratio is 94.7% equity, 5.3% debt, with a pre-tax cost of debt of 5.00%.

Amazon's risk profile will reflect a mix of retail, media and cloud businesses as well as geographic ambitions: Beta used in cost of capital is 1.12, weighted average of online retail, entertainment and business services (cloud). ERP is weighted average of US ERP (5%) and rest of the world (6.45%)

Easy entry into the business will push margins down for everyone: Operating margin stays at 2.85% in year 10, in the 25th percentile of retail company margins

Amazon will be able to invest more efficiently that the average retailer. Reinvest \$1 for every \$3.68 in additional revenues

## II. Mature Companies in transition..

- □ Mature companies are generally the easiest group to value. They have long, established histories that can be mined for inputs. They have investment policies that are set and capital structures that are stable, thus making valuation more grounded in past data.
- □ However, this stability in the numbers can mask real problems at the company. The company may be set in a process, where it invests more or less than it should and does not have the right financing mix. In effect, the policies are consistent, stable and bad.
- □ If you expect these companies to change or as is more often the case to have change thrust upon them,

# The perils of valuing mature companies…

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets?

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Lots of historical data on earnings and cashflows. Key questions remain if these numbers are volatile over time or if the existing assets are not being efficiently utilized.*

> *Operating risk should be stable, but the firm can change its financial leverage This can affect both the cost of equtiy and capital.*

*Growth is usually not very high, but firms may still be generating healthy returns on investments, relative to cost of funding. Questions include how long they can generate these excess returns and with what growth rate in operations. Restructuring can change both inputs dramatically and some firms maintain high growth through acquisitions.*

> *Maintaining excess returns or high growth for any length of time is difficult to do for a mature firm.*

*Figure 7.1: Estimation Issues - Mature Companies*

What is the value of equity in the firm?

*Equity claims can vary in voting rights and dividends.*

#### *Hormel Foods: The Value of Control Changing*

Hormel Foods sells packaged meat and other food products and has been in existence as a publicly traded company for almost 80 years. In 2008, the firm reported after-tax operating income of \$315 million, reflecting a compounded growth of 5% over the previous 5 years.

#### *The Status Quo*

Run by existing management, with conservative reinvestment policies (reinvestment rate = 14.34% and debt ratio = 10.4%.

#### *New and better management*

More aggressive reinvestment which increases the reinvestment rate (to 40%) and tlength of growth (to 5 years), and higher debt ratio (20%).

#### **Operating Restructuring** 1

Expected growth rate = ROC \* Reinvestment Rate Expected growth rae (status quo) = 14.34% \* 19.14% = 2.75% Expected growth rate (optimal) = 14.00% \* 40% = 5.60% ROC drops, reinvestment rises and growth goes up.

#### **Financial restructuring** 2

Cost of capital = Cost of equity (1-Debt ratio) + Cost of debt (Debt ratio) Status quo = 7.33% (1-.104) + 3.60% (1-.40) (.104) = 6.79% Optimal = 7.75% (1-.20) + 3.60% (1-.40) (.20) = 6.63% Cost of equity rises but cost of capital drops.

Anemic growth rate and short growth period, due to reinvestment policy Low debt ratio affects cost of capital

| Year                            | Operating income after taxes | Expected growth rate | ROC    | Reinvestment Rate | Reinvestment | FCFF    | Cost of capital | Present Value |         |
|---------------------------------|------------------------------|----------------------|--------|-------------------|--------------|---------|-----------------|---------------|---------|
| Trailing 12 months              | \$315                        |                      |        |                   |              |         |                 |               |         |
| 1                               | \$324                        | 2.75%                | 14.34% | 19.14%            | \$62         | \$262   | 6.79%           | \$245         |         |
| 2                               | \$333                        | 2.75%                | 14.34% | 19.14%            | \$64         | \$269   | 6.79%           | \$236         |         |
| 3                               | \$342                        | 2.75%                | 14.34% | 19.14%            | \$65         | \$276   | 6.79%           | \$227         |         |
| Beyond                          | \$350                        | 2.35%                | 7.23%  | 32.52%            | \$114        | \$4,840 | 7.23%           | \$3,974       |         |
| Value of operating assets       |                              |                      |        |                   |              |         |                 |               | \$4,682 |
| (Add) Cash                      |                              |                      |        |                   |              |         |                 |               | \$155   |
| (Subtract) Debt                 |                              |                      |        |                   |              |         |                 |               | \$491   |
| (Subtract) Management Options   |                              |                      |        |                   |              |         |                 |               | \$53    |
| Value of equity in common stock |                              |                      |        |                   |              |         |                 |               | \$4,293 |
| Value per share                 |                              |                      |        |                   |              |         |                 |               | \$31.91 |

Expected value =\$31.91 (.90) + \$37.80 (.10) = \$32.50Probability of management change = 10%

3

| Year                            | Operating income after taxes | Expected growth rate | ROC    | Reinvestment Rate | Reinvestment | FCFF    | Cost of capital | Present Value |         |
|---------------------------------|------------------------------|----------------------|--------|-------------------|--------------|---------|-----------------|---------------|---------|
| Trailing 12 months              | \$315                        |                      |        |                   |              |         |                 |               |         |
| 1                               | \$333                        | 5.60%                | 14.00% | 40.00%            | \$133        | \$200   | 6.63%           | \$187         |         |
| 2                               | \$351                        | 5.60%                | 14.00% | 40.00%            | \$141        | \$211   | 6.63%           | \$185         |         |
| 3                               | \$371                        | 5.60%                | 14.00% | 40.00%            | \$148        | \$223   | 6.63%           | \$184         |         |
| 4                               | \$392                        | 5.60%                | 14.00% | 40.00%            | \$260        | \$235   | 6.63%           | \$182         |         |
| 5                               | \$414                        | 5.60%                | 14.00% | 40.00%            | \$223        | \$248   | 6.63%           | \$180         |         |
| Beyond                          | \$423                        | 2.35%                | 6.74%  | 34.87%            | \$148        | \$6,282 | 6.74%           | \$4,557       |         |
| Value of operating assets       |                              |                      |        |                   |              |         |                 |               | \$5,475 |
| (Add) Cash                      |                              |                      |        |                   |              |         |                 |               | \$155   |
| (Subtract) Debt                 |                              |                      |        |                   |              |         |                 |               | \$491   |
| (Subtract) Management Options   |                              |                      |        |                   |              |         |                 |               | \$53    |
| Value of equity in common stock |                              |                      |        |                   |              |         |                 |               | \$5,085 |
| 300 Value per Alswath Damodaran |                              |                      |        |                   |              |         |                 |               | \$37.80 |

#### Lesson 1: Cost cutting and increased efficiency are easier accomplished on paper than in practice… and require commitment

![](_page_300_Figure_2.jpeg)

#### Lesson 2: Increasing growth is not always a value creating option.. And it may destroy value at times..

![](_page_301_Figure_2.jpeg)

### Lesson 3: Financial leverage is a double-edged sword..

*Exhibit 7.1: Optimal Financing Mix: Hormel Foods in January 2009*

![](_page_302_Diagram_3.jpeg)

# III. Dealing with decline and distress…

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets?

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Historial data often reflects flat or declining revenues and falling margins. Investments often earn less than the cost of capital.*

> *Depending upon the risk of the assets being divested and the use of the proceeds from the divestuture (to pay dividends or retire debt), the risk in both the firm and its equity can change.*

*Growth can be negative, as firm sheds assets and shrinks. As less profitable assets are shed, the firm's remaining assets may improve in quality.*

> *There is a real chance, especially with high financial leverage, that the firm will not make it. If it is expected to survive as a going concern, it will be as a much smaller entity.*

What is the value of equity in the firm?

*Underfunded pension obligations and litigation claims can lower value of equity. Liquidation preferences can affect value of equity*

# a. Dealing with Decline

¨ In decline, firms often see declining revenues and lower margins, translating in negative expected growth over time. ¨ If these firms are run by good managers, they will not fight decline. Instead, they will adapt to it and shut down or sell investments that do not generate the cost of capital. This can translate into negative net capital expenditures (depreciation exceeds cap ex), declining working capital and an overall negative reinvestment rate. The best case scenario is that the firm can shed its bad assets, make itself a much smaller and healthier firm and then settle into long-term stable growth. ¨ As an investor, your worst case scenario is that these firms are run by managers in denial who continue to expand the firm by making bad investments (that generate lower returns than the cost of capital). These firms may be able to grow revenues and operating income but will destroy value along the way.

Declining business: Revenues expected to drop by 3% a year fo next 5 years

Margins improve gradually to median for US retail sector (6.25%)

The cost of capital is at 9%, higher because of high cost of debt.

As stores shut down, cash released from real estate.

|                             | <i>Base year</i> | <i>1</i>                                                                     | <i>2</i> | <i>3</i> | <i>4</i> | <i>5</i> | <i>6</i> | <i>7</i> | <i>8</i> | <i>9</i> | <i>10</i> |
|-----------------------------|------------------|------------------------------------------------------------------------------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|
| Revenue growth rate         |                  | -3.00%                                                                       | -3.00%   | -3.00%   | -3.00%   | -3.00%   | -2.00%   | -1.00%   | 0.00%    | 1.00%    | 2.00%     |
| Revenues                    | \$ 12,522        | \$12,146                                                                     | \$11,782 | \$11,428 | \$11,086 | \$10,753 | \$10,538 | \$10,433 | \$10,433 | \$10,537 | \$10,748  |
| EBIT (Operating) margin     | 1.32%            | 1.82%                                                                        | 2.31%    | 2.80%    | 3.29%    | 3.79%    | 4.28%    | 4.77%    | 5.26%    | 5.76%    | 6.25%     |
| EBIT (Operating income)     | \$ 166           | \$ 221                                                                       | \$ 272   | \$ 320   | \$ 365   | \$ 407   | \$ 451   | \$ 498   | \$ 549   | \$ 607   | \$ 672    |
| Tax rate                    | 35.00%           | 35.00%                                                                       | 35.00%   | 35.00%   | 35.00%   | 35.00%   | 36.00%   | 37.00%   | 38.00%   | 39.00%   | 40.00%    |
| EBIT(1-t)                   | \$ 108           | \$ 143                                                                       | \$ 177   | \$ 208   | \$ 237   | \$ 265   | \$ 289   | \$ 314   | \$ 341   | \$ 370   | \$ 403    |
| - Reinvestment              |                  | \$ (188)                                                                     | \$ (182) | \$ (177) | \$ (171) | \$ (166) | \$ (108) | \$ (53)  | \$ -     | \$ 52    | \$ 105    |
| FCFF                        |                  | \$ 331                                                                       | \$ 359   | \$ 385   | \$ 409   | \$ 431   | \$ 396   | \$ 366   | \$ 341   | \$ 318   | \$ 298    |
| Cost of capital             |                  | 9.00%                                                                        | 9.00%    | 9.00%    | 9.00%    | 9.00%    | 8.80%    | 8.60%    | 8.40%    | 8.20%    | 8.00%     |
| PV(FCFF)                    |                  | \$ 304                                                                       | \$ 302   | \$ 297   | \$ 290   | \$ 280   | \$ 237   | \$ 201   | \$ 173   | \$ 149   | \$ 129    |
| Terminal value              | \$ 5,710         |                                                                              |          |          |          |          |          |          |          |          |           |
| PV(Terminal value)          | \$ 2,479         |                                                                              |          |          |          |          |          |          |          |          |           |
| PV (CF over next 10 years)  | \$ 2,362         |                                                                              |          |          |          |          |          |          |          |          |           |
| Sum of PV                   | \$ 4,841         |                                                                              |          |          |          |          |          |          |          |          |           |
| Probability of failure =    | 20.00%           | High debt load and poor earnings put survival at risk. Based on bond rating, |          |          |          |          |          |          |          |          |           |
| Proceeds if firm fails =    | \$2,421          | 20% chance of failure and liquidation will                                   |          |          |          |          |          |          |          |          |           |
| Value of operating assets = | \$4,357          | bring in 50% of book value                                                   |          |          |          |          |          |          |          |          |           |

*Figure 14.5: A Valuation of JC Penney*

# b. Dealing with the "downside" of Distress

¨ A DCF valuation values a firm as a going concern. If there is a significant likelihood of the firm failing before it reaches stable growth and if the assets will then be sold for a value less than the present value of the expected cashflows (a distress sale value), DCF valuations will overstate the value of the firm. ¨ Value of Equity= DCF value of equity (1 - Probability of distress) + Distress sale value of equity (Probability of distress) ¨ There are three ways in which we can estimate the probability of distress: ¤ Use the bond rating to estimate the cumulative probability of distress over 10 years ¤ Estimate the probability of distress with a probit ¤ Estimate the probability of distress by looking at market value of bonds.. ¨ The distress sale value of equity is usually best estimated as a percent of book value (and this value will be lower if the economy is doing badly and there are other firms in the same business also in distress).

![](_page_307_Diagram_0.jpeg)

# Adjusting the value of LVS for distress..

- In February 2009, LVS was rated B+ by S&P. Historically, 28.25% of B+ rated bonds default within 10 years. LVS has a 6.375% bond, maturing in February 2015 (7 years), trading at \$529. If we discount the expected cash flows on the bond at the riskfree rate, we can back out the probability of distress from the bond price:

- □ Solving for the probability of bankruptcy, we get:
  - □  $\pi_{\text{istress}}$  = Annual probability of default = 13.54%
  - □ Cumulative probability of surviving 10 years =  $(1 - .1354)^{10} = 23.34\%$
  - □ Cumulative probability of distress over 10 years =  $1 - .2334 = .7666$  or 76.66%
- □ If LVS is becomes distressed:
  - □ Expected distress sale proceeds = \$2,769 million < Face value of debt
  - □ Expected equity value/share = \$0.00
- □ Expected value per share =  $\$8.12 (1 - .7666) + \$0.00 (.7666) = \$1.92$

$$529 = \sum_{t=1}^{t=7} \frac{63.75(1 - \Pi_{\text{Distress}})^t}{(1.03)^t} + \frac{1000(1 - \Pi_{\text{Distress}})^7}{(1.03)^7}$$

# IV. Emerging Market Companies

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets?

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Big shifts in economic environment (inflation, itnerest rates) can affect operating earnings history. Poor corporate governance and weak accounting standards can lead to lack of transparency on earnings.*

> *Even if the company's risk is stable, there can be significant changes in country risk over time.*

*Growth rates for a company will be affected heavily be growth rate and political developments in the country in which it operates.*

> *Economic crises can put many companies at risk. Government actions (nationalization) can affect long term value.*

#### *Estimation Issues - Emerging Market Companies*

What is the value of equity in the firm?

*Cross holdings can affect value of equity*

#### Lesson 1: Country risk has to be incorporated… but with a scalpel, not a bludgeon

¨ Emerging market companies are undoubtedly exposed to additional country risk because they are incorporated in countries that are more exposed to political and economic risk. ¨ Not all emerging market companies are equally exposed to country risk and many developed markets have emerging market risk exposure because of their operations. ¨ You can use either the "weighted country risk premium", with the weights reflecting the countries you get your revenues from or the lambda approach (which may incorporate more than revenues) to capture country risk exposure.

**Current Cashflow to Firm**

EBIT(1-t) : \$ 434 - Nt CpX - 11 - Chg WC 178 = FCFF \$ 267 Reinvestment Rate = 167/289= 56% Effective tax rate = 19.5%

**Expected Growth in EBIT (1-t)**

.40\*.181=.072 **7.2%**

Stable Growth g = 3.8%; Beta = 1.00; Country Premium= 1.5% Cost of capital = 7.38% ROC= 7.38%; Tax rate=34% Reinvestment Rate=g/ROC =3.8/7.38 = 51.47%

Terminal Value5= 254(.0738-.038) = 8,371

**Cost of Equity 8.31%**

**Cost of Debt** (3.8%+1.7%+1.1%)(1-.34) = 4.36%

**Weights** E = 78.8% D = 21.2%

*Discount at* \$ Cost of Capital (WACC) = 8.31% (.788) + 4.36% (0.212) = 7.47%

Op. Assets \$ 6,239 + Cash: 3,068 - Debt 2,070 - Minor. Int. 177 =Equity 7,059 -Options 4 Value/Share \$9.53 R\$ 15.72

> **Riskfree Rate**: US\$ Riskfree Rate= 3.8% +

**Beta**  0.88 **X** **Mature market premium**  4 %

Unlevered Beta for Sectors: 0.75

Firm's D/E Ratio: 26.84%

#### A \$ Valuation of Embraer

Reinvestment Rate 40%

Return on Capital 18.1%

> Term Yr 524 270 = 254

Avg Reinvestment rate =40%

> + **Lambda** 0.27

<sup>X</sup> Country Equity Risk Premium 3.66%

Country Default Spread 2.2%

X

Rel Equity Mkt Vol 1.64

On May 22, 2008 Embraer Price = R\$ 17.2

\$ Cashflows

| Year           | 1     | 2     | 3     | 4     | 5     |
|----------------|-------|-------|-------|-------|-------|
| EBIT (1-t)     | \$465 | \$499 | \$535 | \$574 | \$615 |
| - Reinvestment | \$186 | \$200 | \$214 | \$229 | \$246 |
| FCFF           | \$279 | \$299 | \$321 | \$344 | \$369 |

# Lesson 2: Currency should not matter

¨ You can value any company in any currency. Thus, you can value a Brazilian company in nominal reais, US dollars or Swiss Francs. ¨ For your valuation to stay invariant and consistent, your cash flows and discount rates have to be in the same currency. Thus, if you are using a high inflation currency, both your growth rates and discount rates will be much higher. ¨ For your cash flows to be consistent, you have to use expected exchange rates that reflect purchasing power parity (the higher inflation currency has to depreciate by the inflation differential each year).

### Lesson 3: The "corporate governance" drag

- ¨ Stockholders in Asian, Latin American and many European companies have little or no power over the managers of the firm. In many cases, insiders own voting shares and control the firm and the potential for conflict of interests is huge. ¨ This weak corporate governance is often a reason for given for using higher discount rates or discounting the estimated value for these companies. ¨ Would you discount the value that you estimate for an emerging market company to allow for this absence of stockholder power?
- a. Yes
- b. No.

![](_page_314_Diagram_1.jpeg)

![](_page_314_Diagram_4.jpeg)

#### 6a. Tube Investments: Status Quo (in Rs)

In 2000, the stock was trading at 102 Rupees/share.

![](_page_315_Diagram_1.jpeg)

#### 6b. Tube Investments: Higher Marginal Return(in Rs)

![](_page_316_Diagram_1.jpeg)

![](_page_316_Diagram_3.jpeg)

# Lesson 4: Watch out for cross holdings…

¨ Emerging market companies are more prone to having cross holdings that companies in developed markets. This is partially the result of history (since many of the larger public companies used to be family owned businesses until a few decades ago) and partly because those who run these companies value control (and use cross holdings to preserve this control). ¨ In many emerging market companies, the real process of valuation begins when you have finished your DCF valuation, since the cross holdings (which can be numerous) have to be valued, often with minimal information.

![](_page_318_Diagram_2.jpeg)

#### Tata Chemicals: April 2010

Average reinvestment rate

![](_page_318_Diagram_4.jpeg)

#### Tata Motors: April 2010

Average reinvestment rate from 2005-09: 179.59%;

![](_page_318_Diagram_8.jpeg)

#### TCS: April 2010

Average reinvestment rate

![](_page_318_Diagram_6.jpeg)

#### 8. The Tata Group – April 2010

# Tata Companies: Value Breakdown

![](_page_319_Figure_2.jpeg)

#### Lesson 5: Truncation risk can come in many forms…

¨ Natural disasters: Small companies in some economies are much exposed to natural disasters (hurricanes, earthquakes), without the means to hedge against that risk (with insurance or derivative products). ¨ Terrorism risk: Companies in some countries that are unstable or in the grips of civil war are exposed to damage or destruction. ¨ Nationalization risk: While less common than it used to be, there are countries where businesses may be nationalized, with owners receiving less than fair value as compensation.

# V. Valuing Financial Service Companies

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets?

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Existing assets are usually financial assets or loans, often marked to market. Earnings do not provide much information on underlying risk.*

> *For financial service firms, debt is raw material rather than a source of capital. It is not only tough to define but if defined broadly can result in high financial leverage, magnifying the impact of small operating risk changes on equity risk.*

*Defining capital expenditures and working capital is a challenge.Growth can be strongly influenced by regulatory limits and constraints. Both the amount of new investments and the returns on these investments can change with regulatory changes.* 

> *In addition to all the normal constraints, financial service firms also have to worry about maintaining capital ratios that are acceptable ot regulators. If they do not, they can be taken over and shut down.*

What is the value of equity in the firm?

*Preferred stock is a significant source of capital.*

**323** Aswath Damodaran US \$ risk free rate (2.27%) adjusted for diff inflation (1.0227)\*(1.097/1.015)-1

ROE = 42.48%

Average Beta for Banks

Terminal Value

= EPS6\*Payout/(r-g)

= (37.97\*.6)/(.2325-.10) = 189.20

Equity Risk Premium 0.81 15.7%

**Riskfree Rate**:

In EGP 10.53%

Value of Equity per share = PV of Dividends & Terminal value =

41.93 EGP Cost of Equity 10.53% + 0.81 (15.70%) = 23.25% g =10%: ROE = 25%(=Cost of equity)

Beta = 0.81

Payout = (1- 10/25) = .60

**Dividends**

EPS = 4.04 EGP

\* Payout Ratio 24.75%

DPS = 1.00 EGP

**Expected Growth**

75.25% \* 42.48% = 31.96%

Forever

|                           | 1        | 2        | 3        | 4         | 5         | 6         | 7         | 8         | 9         | 10        |
|---------------------------|----------|----------|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Expected Growth Rate      | 31.96%   | 31.96%   | 31.96%   | 31.96%    | 31.96%    | 27.57%    | 23.18%    | 18.79%    | 14.39%    | 10.00%    |
| Earnings per share        | 5.33 محم | 7.04 محم | 9.28 محم | 12.25 محم | 16.17 محم | 20.63 محم | 25.41 محم | 30.18 محم | 34.52 محم | 37.97 محم |
| Payout ratio              | 24.75%   | 24.75%   | 24.75%   | 24.75%    | 24.75%    | 31.80%    | 38.85%    | 45.90%    | 52.95%    | 60.00%    |
| Dividends per share       | 1.32 محم | 1.74 محم | 2.30 محم | 3.03 محم  | 4.00 محم  | 6.56 محم  | 9.87 محم  | 13.85 محم | 18.28 محم | 22.78 محم |
| Cost of Equity            | 23.25%   | 23.25%   | 23.25%   | 23.25%    | 23.25%    | 35.04%    | 23.25%    | 23.25%    | 23.25%    | 28.25%    |
| Cumulative Cost of Equity | 23.25%   | 21.90%   | 18.21%   | 23.07%    | 24.83%    | 35.04%    | 43.195%   | 52.37%    | 656.13%   | 808.66%   |
| Present Value             | 1.07 محم | 1.15 محم | 1.23 محم | 1.31 محم  | 1.41 محم  | 1.87 محم  | 2.29 محم  | 2.60 محم  | 2.79 محم  | 2.82 محم  |

*Discount at* Cost of Equity

+

**X**

#### **CIB Egypt in December 2015 Valuation in Egyptian Pounds**

Retention Ratio = 75.25%

> *In December 2015, CIB was trading at 36 EGP per share*

100% in Egypt

**Dividends**

EPS = \$16.77 \*

Payout Ratio 8.35%

DPS =\$1.40

(Updated numbers for 2008 financial year ending 11/08)

**Expected Growth in first 5 years =**

91.65%\*13.19% =

12.09%

Forever

g =4%: ROE = 10%(>Cost of equity)

Beta = 1.20

Payout = (1- 4/10) = .60 or 60%

Terminal Value= EPS10\*Payout/(r-g)

= (42.03\*1.04\*.6)/(.095-.04) = 476.86

Cost of Equity 4.10% + 1.40 (4.5%) = 10.4%

*Discount at* Cost of Equity

Value of Equity per share = PV of Dividends & Terminal value = \$222.49

**Riskfree Rate**:

Treasury bond rate 4.10%

+

**Beta**

1.40 **X**

**Risk Premium**

4.5%

Impled Equity Risk premium in 8/08

Average beta for inveestment banks= 1.40 Mature Market

4.5%

Country Risk 0%

#### **2b. Goldman Sachs: August 2008**

Retention Ratio = 91.65%

ROE = 13.19%

**Rationale for model**

Why dividends? Because FCFE cannot be estimated

Why 3-stage? Because the firm is behaving (reinvesting, growing) like a firm with potential.

In August 2008, Goldman was trading at \$ 169/share.

*Left return on equity at 2008 levels. well below 16% in 2007 and 20% in 2004-2006.*

| Year         | 1       | 2       | 3       | 4       | 5       | 6       | 7       | 8       | 9       | 10      |
|--------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| EPS          | \$18.80 | \$21.07 | \$23.62 | \$26.47 | \$29.67 | \$32.78 | \$35.68 | \$38.26 | \$40.41 | \$42.03 |
| Payout ratio | 8.35%   | 8.35%   | 8.35%   | 8.35%   | 8.35%   | 18.68%  | 29.01%  | 39.34%  | 49.67%  | 60.00%  |
| DPS          | \$1.57  | \$1.76  | \$1.97  | \$2.21  | \$2.48  | \$6.12  | \$10.35 | \$15.05 | \$20.07 | \$25.22 |

*Between years 6-10, as growth drops to 4%, payout ratio increases and cost of equity decreases.*

#### Lesson 1: Financial service companies are opaque…

¨ With financial service firms, we enter into a Faustian bargain. They tell us very little about the quality of their assets (loans, for a bank, for instance are not broken down by default risk status) but we accept that in return for assets being marked to market (by accountants who presumably have access to the information that we don't have). ¨ In addition, estimating cash flows for a financial service firm is difficult to do. So, we trust financial service firms to pay out their cash flows as dividends. Hence, the use of the dividend discount model. ¨ During times of crises or when you don't trust banks to pay out what they can afford to in dividends, using the dividend discount model may not give you a "reliable" value.

![](_page_325_Diagram_5.jpeg)

#### **2c. Wells Fargo: Valuation on October 7, 2008**

#### **Rationale for model**

Why dividends? Because FCFE cannot be estimated

Why 2-stage? Because the expected growth rate in near term is higher than stable growth rate.

Assuming that Wells will have to increase its capital base by about 30% to reflect tighter regulatory concerns. (.1756/1.3 =.135

#### Lesson 2: For financial service companies, book value matters…

¨ The book value of assets and equity is mostly irrelevant when valuing non-financial service companies. After all, the book value of equity is a historical figure and can be nonsensical. (The book value of equity can be negative and is so for more than a 1000 publicly traded US companies) ¨ With financial service firms, book value of equity is relevant for two reasons: ¤ Since financial service firms mark to market, the book value is more likely to reflect what the firms own right now (rather than a historical value) ¤ The regulatory capital ratios are based on book equity. Thus, a bank with negative or even low book equity will be shut down by the regulators. ¨ From a valuation perspective, it therefore makes sense to pay heed to book value. In fact, you can argue that reinvestment for a bank is the amount that it needs to add to book equity to sustain its growth ambitions and safety requirements: ¤ FCFE = Net Income – Reinvestment in regulatory capital (book equity)

# FCFE for a bank…

¨ To estimate the FCFE for a bank, we redefine reinvestment as investment in regulatory capital. Since any dividends paid deplete equity capital and retained earnings increase that capital, the FCFE is:

$$FCF_{B_{\text{Bank}}} = \text{Net Income} - \text{Increase in Regulatory Capital (Book Equity)}$$

#### *Deutsche Bank: FCFE*

|                                    | Current   | 1         | 2         | 3         | 4         | 5         | Steady state |
|------------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|--------------|
| Asset Base                         | 312,882 € | 325,398 € | 338,414 € | 351,950 € | 366,028 € | 380,669 € | 392,089 €    |
| Capital ratio                      | 10.20%    | 10.16%    | 10.12%    | 10.08%    | 10.04%    | 10.00%    | 10.00%       |
| Regulatory Capital                 | 31,914 €  | 33,060 €  | 34,247 €  | 35,477 €  | 36,749 €  | 38,067 €  | 39,244 €     |
| Change in regulatory capital       |           | 1,146 €   | 1,187 €   | 1,229 €   | 1,273 €   | 1,318 €   | 1,177 €      |
|                                    |           |           |           |           |           |           |              |
| ROE                                | 9.40%     | 9.56%     | 9.72%     | 9.88%     | 10.04%    | 10.20%    | 10.20%       |
| Net Income                         | 3,000 €   | 3,161 €   | 3,329 €   | 3,505 €   | 3,690 €   | 3,883 €   | 4,003 €      |
| - Investment in Regulatory Capital |           | 1,146 €   | 1,187 €   | 1,229 €   | 1,273 €   | 1,318 €   | 1,177 €      |
| FCFE                               |           | 2,014 €   | 2,142 €   | 2,276 €   | 2,417 €   | 2,565 €   | 2,826 €      |

## 2d. Deutsche Bank: March 2009

### Last 2 years

|                        | 2007     | 2008    |
|------------------------|----------|---------|
| Net Income             | 3,954 m  | -3,855m |
| Dividends              | 2,146 m  | 285 m   |
| Risk adjusted assets = | 312,882m |         |
| Book Equity =          | 31,914 m |         |
| Regulatory Capital =   |          |         |

Normalized  
Net Income  
for base year  
3,000 m  
Normalized  
ROE = 9.4%

Expected  
growth in  
asset base  
4%

Target capital  
ratio 10%

Target ROE  
10.2%

Stable Growth  
g = 3%; Beta = 1.00  
Cost of equity = 10.20%  
Return on equity = 10.20%;  
Reinvestment Rate=g/ROE  
=3/10.20% = 29.41%

### Cashflows

|                    | 1         | 2         | 3         | 4         | 5         |
|--------------------|-----------|-----------|-----------|-----------|-----------|
| Asset Base         | 325,398 € | 338,414 € | 351,950 € | 366,028 € | 380,669 € |
| Capital ratio      | 10.16%    | 10.12%    | 10.08%    | 10.04%    | 10.00%    |
| Regulatory Capital | 33,060 €  | 34,247 €  | 35,477 €  | 36,749 €  | 38,067 €  |
| Change in capital  | 1,146 €   | 1,187 €   | 1,229 €   | 1,273 €   | 1,318 €   |
| ROE                | 9.56%     | 9.72%     | 9.88%     | 10.04%    | 10.20%    |
| Net Income         | 3,161 €   | 3,329 €   | 3,505 €   | 3,690 €   | 3,883 €   |
| -Reinvestment      | 1,146 €   | 1,187 €   | 1,229 €   | 1,273 €   | 1,318 €   |
| FCFE               | 2,014 €   | 2,142 €   | 2,276 €   | 2,417 €   | 2,565 €   |

PV of CF = 31,383 m  
/# shares 581.85  
Value/Share 53.94 €

3,999  
1,176  
2,823

$$\text{Discount at Cost of equity} = 3.60\% + 1.162 \times 6\% + -0.60\% = 11.172\%$$

In March 2009  
Deutsche Bank price = 48  
Euros/share (down from 89  
Euros in early 2008)

Riskfree Rate:  
Euro Riskfree Rate=  
3.6%

+

Beta  
1.162

X

Mature market  
premium  
6%

+

Beta for commercial &  
Investment banking

| Region               | Lambda | CRP   |
|----------------------|--------|-------|
| Western Europe       | 0.68   | 0.00% |
| United States        | 0.42   | 0.00% |
| Latin America        | 0.01   | 4.50% |
| Africa & Middle East | 0.01   | 7.00% |
| Asia                 | 0.11   | 3.50% |
| Eastern Europe       | 0.04   | 3.00% |
| Deutsche Bank        |        | 0.60% |

### VI. Valuing Companies with "intangible" assets

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets? *The capital* roadblocks?

When will the firm become a mature fiirm, and what are the potential

*expenditures associated with acquiring intangible assets (technology, himan capital) are mis-categorized as operating expenses, leading to inccorect accounting earnings and measures of capital invested.*

*It ican be more difficult to borrow against intangible assets than it is against tangible assets. The risk in operations can change depending upon how stable the intangbiel asset is.*

*If capital expenditures are miscategorized as operating expenses, it becomes very difficult to assess how much a firm is reinvesting for future growth and how well its investments are doing.*

> *Intangbile assets such as brand name and customer loyalty can last for very long periods or dissipate overnight.*

#### Lesson 1: Accounting rules are cluttered with inconsistencies…

¨ If we start with accounting first principles, capital expenditures are expenditures designed to create benefits over many periods. They should not be used to reduce operating income in the period that they are made, but should be depreciated/amortized over their life. They should show up as assets on the balance sheet. ¨ Accounting is consistent in its treatment of cap ex with manufacturing firms, but is inconsistent with firms that do not fit the mold. ¤ With pharmaceutical and technology firms, R&D is the ultimate cap ex but is treated as an operating expense. ¤ With consulting firms and other firms dependent on human capital, recruiting and training expenses are your long term investments that are treated as operating expenses. ¤ With brand name consumer product companies, a portion of the advertising expense is to build up brand name and is the real capital expenditure. It is treated as an operating expense.

#### **Step 1: Ddetermining an amortizable life for R & D expenses.** 1

How long will it take, on an expected basis, for research to pay off at Amgen? Given the length of the approval process for new drugs by the Food and Drugs Administration, we will assume that this amortizable life is 10 years.

#### **Step 2: Capitalize historical R&D exoense**

#### **Step 3: Restate earnings, book value and return numbers**

Current year's R&D expense = Cap ex = \$3,030 million R&D amortization = Depreciation = \$ 1,694 million Unamortized R&D = Capital invested (R&D) = \$13,284 million

2 3

| Year    | R&D Expense | Unamortized portion | Amortization this year |            |
|---------|-------------|---------------------|------------------------|------------|
| Current | 3030.00     | 1.00                | 3030.00                |            |
| -1      | 3266.00     | 0.90                | \$326.60               |            |
| -2      | 3366.00     | 0.80                | \$336.60               |            |
| -3      | 2314.00     | 0.70                | \$231.40               |            |
| -4      | 2028.00     | 0.60                | \$202.80               |            |
| -5      | 1655.00     | 0.50                | \$165.50               |            |
| -6      | 1117.00     | 0.40                | \$111.70               |            |
| -7      | 864.00      | 0.30                | \$86.40                |            |
| -8      | 845.00      | 0.20                | \$84.50                |            |
| -9      | 823.00      | 0.10                | \$82.30                |            |
| -10     | 663.00      | 0.00                | \$66.30                |            |
|         |             |                     | \$13283.60             | \$1,694.10 |

4

|                                | <i>Unadjusted</i>              | <i>Adjusted for R&amp;D</i>      | <i>Comments</i>                                                                               |
|--------------------------------|--------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------|
| Net Income                     | \$4,196                        | $4,196 + 3030 - 1694 = \$ 5,532$ | Add current year's R&D and subtract R&D amortization                                          |
| Book value of equity           | \$17,869                       | $17,869 + 13,284 = \$ 31,153$    | Add unamortized R&D from prior years                                                          |
| Return on Equity               | $\frac{4196}{17869} = 23.48\%$ | $\frac{5532}{31153} = 17.75\%$   | Return on equity drops when book equity is augmented by R&D, even though net income rises.    |
| Pre-tax Operating Income       | \$5,594                        | $5,594 + 3030 - 1694 = \$ 6.930$ | Add current year's R&D and subtract R&D amortization                                          |
| Book value of invested capital | \$21,985                       | $\$21,985 + \$13,284 = \$35,269$ | Add unamortized R&D from prior years                                                          |
| Pre-tax Return on Capital      | $\frac{5594}{21985} = 25.44\%$ | $\frac{6930}{35269} = 19.65\%$   | Return on capital drops when capital is augmented by R&D, even though operating income rises. |

**Current Cashflow to Firm**

EBIT(1-t)= :7336(1-**.28**)= 6058 - Nt CpX= 6443 - Chg WC 37 = FCFF - 423 Reinvestment Rate = 6480/6058 =106.98% Return on capital = 16.71%

**Expected Growth in EBIT (1-t)** .60\*.16=.096 **9.6%**

**Stable Growth**

g = 4%; Beta = 1.10; Debt Ratio= 20%; Tax rate=35% Cost of capital = 8.08% ROC= 10.00%; Reinvestment Rate=4/10=40%

Terminal Value10= 7300/(.0808-.04) = 179,099

**Cost of Equity 11.70%**

**Cost of Debt** (4.78%+..85%)(1-.35) = 3.66%

**Weights** E = 90% D = 10%

Cost of Capital (WACC) = 11.7% (0.90) + 3.66% (0.10) = 10.90%

| Op. Assets | 94214 |
|------------|-------|
| + Cash:    | 1283  |
| - Debt     | 8272  |
| =Equity    | 87226 |
| -Options   | 479   |

**Riskfree Rate**: Riskfree rate = 4.78%

+

**Beta**  1.73 **X** **Risk Premium** 4%

Unlevered Beta for Sectors: 1.59

#### 10. Amgen: Status Quo

Reinvestment Rate 60%

Return on Capital 16%

| Term Yr |
|---------|
| 18718   |
| 12167   |
| 4867    |
| 7300    |

On May 1,2007, Amgen was trading at \$ 55/share

First 5 years

Growth decreases gradually to 4%

> Debt ratio increases to 20% Beta decreases to 1.10

D/E=11.06%

Cap Ex = Acc net Cap Ex(255) + Acquisitions (3975) + R&D (2216)

| Year           | 1       | 2        | 3        | 4        | 5        | 6                                            | 7        | 8        | 9        | 10       |
|----------------|---------|----------|----------|----------|----------|----------------------------------------------|----------|----------|----------|----------|
| EBIT           | \$9,221 | \$10,106 | \$11,076 | \$12,140 | \$13,305 | \$14,433                                     | \$15,496 | \$16,463 | \$17,306 | \$17,998 |
| EBIT (1-t)     | \$6,639 | \$7,276  | \$7,975  | \$8,741  | \$9,580  | \$10,392 \$11,157 \$11,853 \$12,460 \$12,958 |          |          |          |          |
| - Reinvestment | \$3,983 | \$4,366  | \$4,785  | \$5,244  | \$5,748  | \$5,820                                      | \$5,802  | \$5,690  | \$5,482  | \$5,183  |
| = FCFF         | \$2,656 | \$2,911  | \$3,190  | \$3,496  | \$3,832  | \$4,573                                      | \$5,355  | \$6,164  | \$6,978  | \$7,775  |

### Lesson 2: And fixing those inconsistencies can alter your view of a company and affect its value

|                   | No R&D adjustment | R&D adjustment |
|-------------------|-------------------|----------------|
| EBIT              | \$5,071           | \$7,336        |
| Invested Capital  | \$25,277          | \$33,173       |
| ROIC              | 14.58%            | 18.26%         |
| Reinvestment Rate | 115.68%           | 106.98%        |
| Value of firm     | \$58,617          | \$95,497       |
| Value of equity   | \$50,346          | \$87,226       |
| Value/share       | \$42.73           | \$74.33        |

### VII. Valuing cyclical and commodity companies

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets? *Historial revenue and* roadblocks?

When will the firm become a mature fiirm, and what are the potential

*earnings data are volatile, as the economic cycle and commodity prices change.*

*Primary risk is from the economy for cyclical firms and from commodity price movements for commodity companies. These risks can stay dormant for long periods of apparent prosperity.*

*Company growth often comes from movements in the economic cycle, for cyclical firms, or commodity prices, for commodity companies.*

> *For commodity companies, the fact that there are only finite amounts of the commodity may put a limit on growth forever. For cyclical firms, there is the peril that the next recession may put an end to the firm.*

#### Lesson 1: With "macro" companies, it is easy to get lost in "macro" assumptions…

¨ With cyclical and commodity companies, it is undeniable that the value you arrive at will be affected by your views on the economy or the price of the commodity. ¨ Consequently, you will feel the urge to take a stand on these macro variables and build them into your valuation. Doing so, though, will create valuations that are jointly impacted by your views on macro variables and your views on the company, and it is difficult to separate the two. ¨ The best (though not easiest) thing to do is to separate your macro views from your micro views. Use current market based numbers for your valuation, but then provide a separate assessment of what you think about those market numbers.

#### Lesson 2: Use probabilistic tools to assess value as a function of macro variables…

¨ If there is a key macro variable affecting the value of your company that you are uncertain about (and who is not), why not quantify the uncertainty in a distribution (rather than a single price) and use that distribution in your valuation. ¨ That is exactly what you do in a Monte Carlo simulation, where you allow one or more variables to be distributions and compute a distribution of values for the company. ¨ With a simulation, you get not only everything you would get in a standard valuation (an estimated value for your company) but you will get additional output (on the variation in that value and the likelihood that your firm is under or over valued)

## Shell: A "Oil Price" Neutral Valuation: March 2016

Revenue calculated from prevailing oil price of \$40/barrel in March 2016  
 Revenue =  $39992.77 + 4039.40 \times \$40$   
 $= \$201,569$ 

Compounded revenue growth of 3.91% a year, based on  
 Shell's historical revenue growth rate from 2000 to 2015

|                           | Base Year     |              | 1            | 2            | 3            | 4             | 5            | Terminal Year |  |
|---------------------------|---------------|--------------|--------------|--------------|--------------|---------------|--------------|---------------|--|
| Revenues                  | \$ 201,569    | \$ 209,450   | \$ 217,639   | \$ 226,149   | \$ 234,991   | \$ 244,180    | \$ 249,063   |               |  |
| Operating Margin          | 3.01%         | 6.18%        | 7.76%        | 8.56%        | 8.95%        | 9.35%         | 9.35%        |               |  |
| Operating Income          | \$ 6,065.00   | \$ 12,942.85 | \$ 16,899.10 | \$ 19,352.39 | \$ 21,040.39 | \$ 22,830.80  | \$ 23,287.41 |               |  |
| Effective tax rate        | 30.00%        | 30.00%       | 30.00%       | 30.00%       | 30.00%       | 30.00%        | 30.00%       |               |  |
| AT Operating Income       | \$ 4,245.50   | \$ 9,060.00  | \$ 11,829.37 | \$ 13,546.68 | \$ 14,728.27 | \$ 15,981.56  | \$ 16,301.19 |               |  |
| + Depreciation            | \$ 26,714.00  | \$ 27,759    | \$ 28,844    | \$ 29,972    | \$ 31,144    | \$ 32,361     |              |               |  |
| - Cap Ex                  | \$ 31,854.00  | \$ 33,099    | \$ 34,394    | \$ 35,738    | \$ 37,136    | \$ 38,588     |              |               |  |
| - Chg in WC               |               | \$ 472.88    | \$ 491.37    | \$ 510.58    | \$ 530.55    | \$ 551.29     |              |               |  |
| FCFF                      |               | \$ 3,246.14  | \$ 5,788.19  | \$ 7,269.29  | \$ 8,205.44  | \$ 9,203.68   | \$ 13,011.34 |               |  |
| Terminal Value            |               |              |              |              |              | \$ 216,855.71 |              |               |  |
| Return on capital         |               |              |              |              |              |               |              | 12.37%        |  |
| Cost of Capital           |               | 9.91%        | 9.91%        | 9.91%        | 9.91%        | 9.91%         | 8.00%        |               |  |
| Cumulated Discount Factor |               | 1.0991       | 1.2080       | 1.3277       | 1.4593       | 1.6039        |              |               |  |
| Present Value             |               | \$ 2,953.45  | \$ 4,791.47  | \$ 5,474.95  | \$ 5,622.81  | \$ 140,940.73 |              |               |  |
| Value of Operating Assets | \$ 159,783.41 |              |              |              |              |               |              |               |  |
| + Cash                    | \$ 31,752.00  |              |              |              |              |               |              |               |  |
| + Cross Holdings          | \$ 33,566.00  |              |              |              |              |               |              |               |  |
| - Debt                    | \$ 58,379.00  |              |              |              |              |               |              |               |  |
| - Minority Interets       | \$ 1,245.00   |              |              |              |              |               |              |               |  |
| Value of Equity           | \$ 165,477.41 |              |              |              |              |               |              |               |  |
| Number of shares          | 4209.7        |              |              |              |              |               |              |               |  |
| Value per share           | \$ 39.31      |              |              |              |              |               |              |               |  |

Operating margin converges on Shell's historical average margin of 9.35% from 200-2015

Return on capital reverts and stays at Shell's historic average of 12.37% from 200-2015

# Shell's Revenues & Oil Prices

![](_page_338_Figure_2.jpeg)

*Shell: Revenues vs Oil Price*

![](_page_339_Figure_15.jpeg)

**Revenue calculated from the oil price drawn from distribution**

$$\text{Revenue} = 39992.77 + 4039.40 * \text{Oil Price/Barrel}$$

**Pre-tax Operating Income based on revenue & selected margin**

$$\text{Pre-tax Operating Income} = \text{Revenues} * \text{Operating Margin}$$

![](_page_339_Figure_20.jpeg)

**Value Shell based on operating income, assuming other assumptions (tax rate, revenue growth, cost of capital)**

| Percentiles:      | Forecast values |
|-------------------|-----------------|
| $\frac{0}{100}$   | \$6.55          |
| $\frac{10}{100}$  | \$23.90         |
| $\frac{20}{100}$  | \$27.73         |
| $\frac{30}{100}$  | \$30.89         |
| $\frac{40}{100}$  | \$33.88         |
| $\frac{50}{100}$  | \$36.99         |
| $\frac{60}{100}$  | \$40.28         |
| $\frac{70}{100}$  | \$44.22         |
| $\frac{80}{100}$  | \$49.24         |
| $\frac{90}{100}$  | \$57.49         |
| $\frac{100}{100}$ | \$197.11        |

![](_page_339_Figure_23.jpeg)

# VALUE, PRICE AND INFORMATION: CLOSING THE DEAL

Value versus Price

# Are you valuing or pricing?

INTRINSIC

VALUE PRICE Value Price THE GAP Is there one? Will it close?

![](_page_341_Figure_11.jpeg)

Drivers of intrinsic value - Cashflows from existing assets - Growth in cash flows - Quality of Growth

*Drivers of price* - Market moods & momentum - Surface stories about fundamentals

*Tools for pricing* - Multiples and comparables - Charting and technical indicators - Pseudo DCF

*Tools for intrinsic analysis* - Discounted Cashflow Valuation (DCF) - Intrinsic multiples - Book value based approaches - Excess Return Models

*Tools for "the gap"* - Behavioral finance - Price catalysts

*Drivers of "the gap"* - Information - Liquidity - Corporate governance

Value of cashflows, adjusted for time and risk

# Test 1: Are you pricing or valuing?

![](_page_342_Figure_2.jpeg)

![](_page_342_Figure_3.jpeg)

# Test 2: Are you pricing or valuing?

344

Rating  
Buy

Europe  
Switzerland

Biotechnology  
Biotechnology

Company  
BB BIOTECH

| Reuters<br>BION.S | Bloomberg<br>BION SW | Exchange<br>SWX | Ticker<br>BION |
|-------------------|----------------------|-----------------|----------------|
|-------------------|----------------------|-----------------|----------------|

Date  
13 August 2013

## Forecast Change

| Price at 12 Aug 2013 (CHF) | 124.00         |
|----------------------------|----------------|
| Price Target (CHF)         | 164.50         |
| 52-week range (CHF)        | 128.40 - 84.90 |

## Strong sector and stock-picking continue

### Impressive performance

Over the past two years, BB Biotech shares have roughly tripled, which could tempt investors to take profits. However, this performance has been well backed by a deserved revival of the biotech industry, encouraging fundamental news, M&A, and increased money flow into health care stocks. In addition, BBB returned to index outperformance by modifying its stock-picking approach. Hence, despite excellent performance, the shares still trade at a 23% discount to the net asset value of the portfolio. Hence, the shares are an attractive value vehicle to capture growth opportunities in an attractive sector.

### Biotech industry remains attractive

With the re-rating of the pharma sector, investors have also showed increased interest in biotech stocks. Established biotech stocks have delivered encouraging financial results and approvals, while there has also been substantial industry consolidation, which is not surprising in times of "cheap" money and high liquidity. BB Biotech remains an attractive vehicle to capture the future potential of the biotech sector. In addition, investors benefit from a 23% discount to NAV and attractive cash distribution policy of 5% yield p.a. Hence, we reiterate our Buy on BB Biotech shares.

### BB Biotech shares remain attractive

In the first 6M of 2013, BB Biotech increased its NAV by 36%, which marks good outperformance against the Nasdaq Biotech Index (NBI)'s 27%. This is a remarkable performance after 2012 when BBB's NAV increase of 45% also

### Key changes

| Target Price | 106.50 to 164.50 | ↑ | 54.5% |
|--------------|------------------|---|-------|
|--------------|------------------|---|-------|

Source: Deutsche Bank

### Price/price relative

![](_page_343_Figure_58.jpeg)

| Performance (%)          | 1m   | 3m   | 12m  |
|--------------------------|------|------|------|
| Absolute                 | -1.4 | 5.4  | 37.4 |
| SPI Swiss Performance IX | 0.5  | -1.4 | 26.4 |

Source: Deutsche Bank

# The drivers of value

What are the **cashflows from existing assets**? - Equity: Cashflows after debt payments - Firm: Cashflows before debt payments What is the **value added** by growth assets?

Equity: Growth in equity earnings/ cashflows

Firm: Growth in operating earnings/ cashflows

How **risky are the cash flows** from both existing assets and growth assets?

Equity: Risk in equity in the company

Firm: Risk in the firm's operations

When will the firm become a **mature fiirm**, and what are the potential roadblocks?

# The determinants of price

#### The Market Price

#### **Mood and Momentum**

Price is determined in large part by mood and momentum, which, in turn, are driven by behavioral factors (panic, fear, greed).

#### **Liquidity & Trading Ease**

While the value of an asset may not change much from period to period, liquidity and ease of trading can, and as it does, so will the price.

#### **Incremental information**

Since you make money on price changes, not price levels, the focus is on incremental information (news stories, rumors, gossip) and how it measures up, relative to expectations

#### **Group Think**

To the extent that pricing is about gauging what other investors will do, the price can be determined by the "herd".

# Three views of "the gap"

| View	of	the	gap                 | Investment	Strategies        |
|---------------------------------|------------------------------|
| You	view	pricers	as	dilettantes | who                          |
| Value	is	only	in	the	heads      | of	the                       |
| “eggheads”.                     | Even	if	it	exists (and	it	is |
| questionable),                  | price	may	never              |
|                                 | (1) Look	for	mispriced       |
|                                 | (2) Get	ahead	of	shifts	in   |

# The "pricers" dilemma..

¨ No anchor: If you do not believe in intrinsic value and make no attempt to estimate it, you have no moorings when you invest. You will therefore be pushed back and forth as the price moves from high to low. In other words, everything becomes relative and you can lose perspective. ¨ Reactive: Without a core measure of value, your investment strategy will often be reactive rather than proactive. ¨ Crowds are fickle and tough to get a read on: The key to being successful as a pricer is to be able to read the crowd mood and to detect shifts in that mood early in the process. By their nature, crowds are tough to read and almost impossible to model systematically.

#### The valuer's dilemma and ways of dealing with it…

¨ Uncertainty about the magnitude of the gap: ¤ Margin of safety: Many value investors swear by the notion of the "margin of safety" as protection against risk/uncertainty. ¤ Collect more information: Collecting more information about the company is viewed as one way to make your investment less risky. ¤ Ask what if questions: Doing scenario analysis or what if analysis gives you a sense of whether you should invest. ¤ Confront uncertainty: Face up to the uncertainty, bring it into the analysis and deal with the consequences. ¨ Uncertainty about gap closing: This is tougher and you can reduce your exposure to it by ¤ Lengthening your time horizon ¤ Providing or looking for a catalyst that will cause the gap to close.

#### Strategies for managing the risk in the "closing" of the gap

¨ The "karmic" approach: In this one, you buy (sell short) under (over) valued companies and sit back and wait for the gap to close. You are implicitly assuming that given time, the market will see the error of its ways and fix that error. ¨ The catalyst approach: For the gap to close, the price has to converge on value. For that convergence to occur, there usually has to be a catalyst. ¤ If you are an activist investor, you may be the catalyst yourself. In fact, your act of buying the stock may be a sufficient signal for the market to reassess the price. ¤ If you are not, you have to look for other catalysts. Here are some to watch for: a new CEO or management team, a "blockbuster" new product or an acquisition bid where the firm is targeted.

# An example: Apple – Price versus Value (my estimates) from 2011 to 2015

Figure 11.3: Apple, Price and Value - 2010 to 2015

![](_page_350_Figure_25.jpeg)

# A closing thought...

![](_page_351_Picture_7.jpeg)