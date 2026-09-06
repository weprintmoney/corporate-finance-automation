---
title: "Session3Slides"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valspr19/session3slides.pdf
---

#### Valuation: Lecture Note Packet 1 Intrinsic Valuation

Aswath Damodaran Updated: January 2019

# The essence of intrinsic value

¨ In intrinsic valuation, you value an asset based upon its fundamentals (or intrinsic characteristics). ¨ For cash flow generating assets, the intrinsic value will be a function of the magnitude of the expected cash flows on the asset over its lifetime and the uncertainty about receiving those cash flows. ¨ Discounted cash flow valuation is a tool for estimating intrinsic value, where the expected value of an asset is written as the present value of the expected cash flows on the asset, with either the cash flows or the discount rate adjusted to reflect the risk.

#### The two faces of discounted cash flow valuation

¨ The value of a risky asset can be estimated by discounting the expected cash flows on the asset over its life at a risk-adjusted discount rate:

| Value of asset | $= \frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$ |
|----------------|---------------------------------------------------------------------------------------------------------------|
|                |                                                                                                               |

where the asset has an n-year life, E(CFt) is the expected cash flow in period t and r is a discount rate that reflects the risk of the cash flows.

¨ Alternatively, we can replace the expected cash flows with the guaranteed cash flows we would have accepted as an alternative (certainty equivalents) and discount these at the riskfree rate:

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

where CE(CFt) is the certainty equivalent of E(CFt) and rf is the riskfree rate.

#### Risk Adjusted Value: Two Basic Propositions

¨ The value of an asset is the risk-adjusted present value of the cash flows:

| Value of asset | $= \frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$ |
|----------------|---------------------------------------------------------------------------------------------------------------|
|                |                                                                                                               |

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

- 1. The "IT" proposition: If IT does not affect the expected cash flows or the riskiness of the cash flows, IT cannot affect value.
- 2. The "DUH" proposition: For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.
- 3. The "DON'T FREAK OUT" proposition: Assets that generate cash flows early in their life will be worth more than assets that generate cash flows later; the latter may however have greater growth and higher cash flows to compensate.

#### DCF Choices: Equity Valuation versus Firm Valuation

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

| Year           | CF to Equity | Interest Expense (1-t) | CF to Firm  |
|----------------|--------------|------------------------|-------------|
| 1              | \$ 50        | \$ 40                  | \$ 90       |
| 2              | \$ 60        | \$ 40                  | \$ 100      |
| 3              | \$ 68        | \$ 40                  | \$ 108      |
| 4              | \$ 76.2      | \$ 40                  | \$ 116.2    |
| 5              | \$ 83.49     | \$ 40                  | \$ 123.49   |
| Terminal Value | \$ 1603.0    |                        | \$ 2363.008 |

¨ Assume also that the cost of equity is 13.625% and the firm can borrow long term at 10%. (The tax rate for the firm is 50%.) ¨ The current market value of equity is \$1,073 and the value of debt outstanding is \$800.

# Equity versus Firm Valuation

¨ Method 1: Discount CF to Equity at Cost of Equity to get value of equity ¤ Cost of Equity = 13.625% ¤ Value of Equity = 50/1.13625 + 60/1.136252 + 68/1.136253 + 76.2/1.136254 + (83.49+1603)/1.136255 = **\$1073** ¨ Method 2: Discount CF to Firm at Cost of Capital to get value of firm ¤ Cost of Debt = Pre-tax rate (1- tax rate) = 10% (1-.5) = 5% Cost of Capital = 13.625% (1073/1873) + 5% (800/1873) = 9.94% ¤ PV of Firm = 90/1.0994 + 100/1.09942 + 108/1.09943 + 116.2/1.09944 + (123.49+2363)/1.09945 = \$1873 ¤ Value of Equity = Value of Firm - Market Value of Debt = \$ 1873 - \$ 800 = **\$1073** 

# First Principle of Valuation

¨ Discounting Consistency Principle: Never mix and match cash flows and discount rates. ¨ Mismatching cash flows to discount rates is deadly. ¤ Discounting cashflows after debt cash flows (equity cash flows) at the weighted average cost of capital will lead to an upwardly biased estimate of the value of equity ¤ Discounting pre-debt cashflows (cash flows to the firm) at the cost of equity will yield a downward biased estimate of the value of the firm.

#### The Effects of Mismatching Cash Flows and Discount Rates

¨ Error 1: Discount CF to Equity at Cost of Capital to get equity value ¤ PV of Equity = 50/1.0994 + 60/1.09942 + 68/1.09943 + 76.2/1.09944 + (83.49+1603)/1.09945 = \$1248 ¤ Value of equity is overstated by \$175. ¨ Error 2: Discount CF to Firm at Cost of Equity to get firm value ¤ PV of Firm = 90/1.13625 + 100/1.136252 + 108/1.136253 + 116.2/1.136254 + (123.49+2363)/1.136255 = \$1613 ¤ PV of Equity = \$1612.86 - \$800 = \$813 ¤ Value of Equity is understated by \$ 260. ¨ Error 3: Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity ¤ Value of Equity = \$ 1613 ¤ Value of Equity is overstated by \$ 540

# **<sup>13</sup>** DCF: First Steps

# Discounted Cash Flow Valuation: The Steps

- 1. Estimate the discount rate or rates to use in the valuation
  - 1. Discount rate can be either a cost of equity (if doing equity valuation) or a cost of capital (if valuing the firm)
  - 2. Discount rate can be in nominal terms or real terms, depending upon whether the cash flows are nominal or real
  - 3. Discount rate can vary across time.
- 2. Estimate the current earnings and cash flows on the asset, to either equity investors (CF to Equity) or to all claimholders (CF to Firm)
- 3. Estimate the future earnings and cash flows on the firm being valued, generally by estimating an expected growth rate in earnings.
- 4. Estimate when the firm will reach stable growth and what characteristics (risk & cash flow) it will have when it does.
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

#### To valuing the entire business: The FCFF model

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

#### ¨ Estimation versus Economic uncertainty

¤ Estimation uncertainty reflects the possibility that you could have the "wrong model" or estimated inputs incorrectly within this model. ¤ Economic uncertainty comes the fact that markets and economies can change over time and that even the best models will fail to capture these unexpected changes.

#### ¨ Micro uncertainty versus Macro uncertainty

¤ Micro uncertainty refers to uncertainty about the potential market for a firm's products, the competition it will face and the quality of its management team. ¤ Macro uncertainty reflects the reality that your firm's fortunes can be affected by changes in the macro economic environment.

#### ¨ Discrete versus continuous uncertainty

¤ Discrete risk: Risks that lie dormant for periods but show up at points in time. (Examples: A drug working its way through the FDA pipeline may fail at some stage of the approval process or a company in Venezuela may be nationalized) ¤ Continuous risk: Risks changes in interest rates or economic growth occur continuously and affect value as they happen.

#### Risk and Cost of Equity: The role of the marginal investor

¨ Not all risk counts: While the notion that the cost of equity should be higher for riskier investments and lower for safer investments is intuitive, what risk should be built into the cost of equity is the question. ¨ Risk through whose eyes? While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment ¨ The diversification effect: Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (i.e, market or non-diversifiable risk). In effect, it is primarily economic, macro, continuous risk that should be incorporated into the cost of equity.

#### The Cost of Equity: Competing " Market Risk" Models

#### **Model Expected Return Inputs Needed**

CAPM  $E(R) = Rf + \beta (R_m - R_f)$  Riskfree Rate

Beta relative to market portfolio Market Risk Premium

APM  $E(R) = Rf + \Sigma\beta_j (R_j - R_f)$ 

- Rf) Riskfree Rate; # of Factors;

Betas relative to each factor Factor risk premiums

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