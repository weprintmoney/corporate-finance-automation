---
title: "Valpacket1Spr24"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket1spr24.pdf
---

# Valuation: Lecture Note Packet 1 Intrinsic Valuation

Aswath Damodaran Updated: January 2024

# The essence of intrinsic value

- □ In intrinsic valuation, you value an asset based upon its fundamentals (or intrinsic characteristics.
- □ For cash flow generating assets, the intrinsic value will be a function of the magnitude of the expected cash flows on the asset over its lifetime and the uncertainty about receiving those cash flows.
  - ■ Discounted cash flow (DCF) valuation is a tool for estimating intrinsic value, where the expected value of an asset is written as the present value of the expected cash flows on the asset, with either the cash flows or the discount rate adjusted to reflect the risk.
  - ■ Intrinsic valuation models predate the modern DCF model, since investors through the ages have found ways to weight in expected cash flows into value.

## The two faces of discounted cash flow valuation

¨ The value of a risky asset can be estimated by discounting the expected cash flows on the asset over its life at a risk-adjusted discount rate:

$$\text{Value of asset} = \frac{E(\text{CF}_1)}{(1+r)} + \frac{E(\text{CF}_2)}{(1+r)^2} + \frac{E(\text{CF}_3)}{(1+r)^3} \dots + \frac{E(\text{CF}_n)}{(1+r)^n}$$

where the asset has an n-year life, E(CFt) is the expected cash flow in period t and r is a discount rate that reflects the risk of the cash flows.

¨ Alternatively, we can replace the expected cash flows with the guaranteed cash flows we would have accepted as an alternative (certainty equivalents) and discount these at the riskfree rate:

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

where CE(CFt) is the certainty equivalent of E(CFt) and rf is the riskfree rate.

## Risk Adjusted Value: Two Basic Propositions

¨ The value of an asset is the risk-adjusted present value of the cash flows:

$$\text{Value of asset} = \frac{E(\text{CF}_1)}{(1+r)} + \frac{E(\text{CF}_2)}{(1+r)^2} + \frac{E(\text{CF}_3)}{(1+r)^3} \dots + \frac{E(\text{CF}_n)}{(1+r)^n}$$

- 1. The "IT" proposition: If IT does not affect the expected cash flows or the riskiness of the cash flows, IT cannot affect value.
- 2. The "DON'T BE A WUSS" proposition: Valuation requires that you make estimates of expected cash flows in the future, not that you be right about those cashflows. So, uncertainty is not an excuse for not making estimates.
- 3. The "DUH" proposition: For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.
- 4. The "DON'T FREAK OUT" proposition: Assets that generate cash flows early in their life will be worth more than assets that generate cash flows later; the latter may however have greater growth and higher cash flows to compensate.

## DCF Choices: Equity Valuation versus Firm Valuation

![](_page_4_Diagram_3.jpeg)

**Equity valuation**: Value just the equity claim in the business

**Firm Valuation**: Value the entire business

# 1. Equity Valuation

| Assets          | Liabilities                      |
|-----------------|----------------------------------|
| Assets in Place | Debt                             |
| Growth Assets   | cost of raising equity financing |

*Figure 5.5: Equity Valuation*

# 2. Firm or Business Valuation

![](_page_6_Diagram_3.jpeg)

*Figure 5.6: Firm Valuation*

# Firm Value and Equity Value

- ¨ To get from firm value to equity value, which of the following would you need to do?
  - a. Subtract out the value of long-term debt
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

¨ Discounting Consistency Principle: Never mix and match cash flows and discount rates. ¨ The Mismatch Effect: Mismatching cash flows to discount rates is deadly. ¤ Discounting cashflows after debt cash flows (equity cash flows) at the weighted average cost of capital will lead to an upwardly biased estimate of the value of equity ¤ Discounting pre-debt cashflows (cash flows to the firm) at the cost of equity will yield a downward biased estimate of the value of the firm.

## The Effects of Mismatching Cash Flows and Discount Rates

¨ Error 1: Discount CF to Equity at Cost of Capital to get equity value ¤ PV of Equity = 50/1.0994 + 60/1.09942 + 68/1.09943 + 76.2/1.09944 + (83.49+1603)/1.09945 = \$1248 ¤ Value of equity is **overstated by \$175**. ¨ Error 2: Discount CF to Firm at Cost of Equity to get firm value ¤ PV of Firm = 90/1.13625 + 100/1.136252 + 108/1.136253 + 116.2/1.136254 + (123.49+2363)/1.136255 = \$1613 ¤ PV of Equity = \$1612.86 - \$800 = \$813 ¤ Value of Equity is **understated by \$ 260**. ¨ Error 3: Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity ¤ Value of Equity = \$ 1613 ¤ Value of Equity is **overstated by \$ 540**

# **<sup>13</sup>** DCF: First Steps

# Generic DCF Valuation Model

![](_page_13_Diagram_3.jpeg)

## DISCOUNTED CASHFLOW VALUATION

# Same ingredients, different approaches…

| Input           | Dividend Discount Model                      | FCFE (Potential dividend) discount model                                                    | FCFF (firm) valuation model                                                    |
|-----------------|----------------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Cash flow       | Dividend                                     | Potential dividends = FCFE = Cash flows after taxes, reinvestment needs and debt cash flows | FCFF = Cash flows before debt payments but after reinvestment needs and taxes. |
| Expected growth | In equity income and dividends               | In equity income and FCFE                                                                   | In operating income and FCFF                                                   |
| Discount rate   | Cost of equity                               | Cost of equity                                                                              | Cost of capital                                                                |
| Steady state    | When dividends grow at constant rate forever | When FCFE grow at constant rate forever                                                     | When FCFF grow at constant rate forever                                        |

# Start easy: The Dividend Discount Model

![](_page_15_Diagram_2.jpeg)

## Moving on up: The "potential dividends" or FCFE model

![](_page_16_Diagram_2.jpeg)

## To valuing the entire business: The FCFF model

![](_page_17_Diagram_2.jpeg)

19

# DCF: The Process

**Cash flow to Firm**

Revenues \* Operating Margin  
= Operating Income

| * (1- tax rate)           | Tax Effect   |
|---------------------------|--------------|
| - (Cap Ex - Depreciation) | Reinvestment |
| - Change in non-cash WC   |              |
| = Free Cash flow to Firm  |              |

- \* How quickly is the firm growing?
- \* How efficiently is it growing?
- \* How profitable is the firm?

If margins & returns are stable  
Expected growth in operating income = Reinvestment  
Rate \* Return on Invested Capital  
FCFF = After-tax Oper. Income (1 - Reinvestment Rate)

If margins & returns are changing

1. 1. Estimate revenue growth & future revenues
2. 2. Estimate operating margins over time
3. 3. Estimate reinvestment based on revenues

FCFF = After tax Operating Income - Reinvestment

**Firm is mature**  
Cashflow/Earnings grow at constant rate forever ( $g_n$ )

Value of Operating Assets  
+ Cash  
+ Non-operating Assets  
- Debt  
= Value of Equity

**Adjust for risk of failure**  
= Probability of failure \*  
Value of Equity in failure

![](_page_19_Diagram_44.jpeg)

Terminal Value =  $FCFF_{n+1} / (r - g_n)$ 

**Return required by "marginal" investors, given perceived risk in equity investment**

**Riskfree Rate**

- - Default free & long term
- - In same currency and in same terms as cash flows

+

**Relative Risk Measure (Beta)**

X

**Equity Risk Premium**

![](_page_19_Diagram_53.jpeg)

# The Sequence

- 1. Get a handle on the past and the cross-section: While the past is the past (and should have little relevance in determining value), you can get clues about the future by looking at what your firm has done in the past, and what other companies in the business are doing now.
- 2. Risk and Discount Rates: Traditional financial theory (unfortunately) has put too much of a focus on risk and discount rates, but they do remain ingredients in valuing a company.
- 3. Estimate growth and future cash flows: This is where the rubber meets the road in valuation. Estimating future cash flows is never easy, should not be mechanical and should be built around your story.
- 4. Apply Closure to cash flows: Since you cannot estimate cash flows forever, you need to find a way to bring your valuation to closure.
- 5. Tie up loose ends: Check to see what else in your business needs to be valued or adjusted for to get to value per share.

22

# Discount Rates

The D in the DCF..

# Estimating Inputs: Discount Rates

¨ While discount rates obviously matter in DCF valuation, they don't matter as much as most analysts think they do. ¨ At an intuitive level, the discount rate used should be consistent with both the riskiness and the type of cashflow being discounted. ¤ Equity versus Firm: If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital. ¤ Currency: The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated. ¤ Nominal versus Real: If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

# Risk in the DCF Model

24

*Expectation of cash flows across all scenarios, good and bad. Incorporates all risks that affect the asset / business.*

---

Expected Cash Flows

Risk Adjusted Discount Rate

*Discount rate should reflect the risk perceived by the marginal investor in the company*

$$\text{Risk Adjusted Cost of equity} = \text{Risk free rate in the currency of analysis} + \text{Relative risk of company/equity in question} \times \text{Equity Risk Premium required for average risk equity}$$

# Not all risk is created equal…

## ¨ Estimation versus Economic uncertainty

¤ Estimation uncertainty reflects the possibility that you could have the "wrong model" or estimated inputs incorrectly within this model. ¤ Economic uncertainty comes the fact that markets and economies can change over time and that even the best models will fail to capture these unexpected changes.

## ¨ Micro uncertainty versus Macro uncertainty

¤ Micro uncertainty refers to uncertainty about the potential market for a firm's products, the competition it will face and the quality of its management team. ¤ Macro uncertainty reflects the reality that your firm's fortunes can be affected by changes in the macro economic environment.

## ¨ Discrete versus continuous uncertainty

¤ Discrete risk: Risks that lie dormant for periods but show up at points in time. (Examples: A drug working its way through the FDA pipeline may fail at some stage of the approval process or a company in Venezuela may be nationalized) ¤ Continuous risk: Risks changes in interest rates or economic growth occur continuously and affect value as they happen.

## Risk and Cost of Equity: The role of the marginal investor

¨ Not all risk counts: While the notion that the cost of equity should be higher for riskier investments and lower for safer investments is intuitive, what risk should be built into the cost of equity is the question. ¨ Risk through whose eyes? While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment ¨ The diversification effect: Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (i.e, market or non-diversifiable risk). In effect, it is primarily economic, macro, continuous risk that should be incorporated into the cost of equity.

## The Cost of Equity: Competing " Market Risk" Models

## **Model Expected Return Inputs Needed**

CAPM 
$$E(R) = Rf + \beta (R_m - R_f)$$
 Riskfree Rate

Beta relative to market portfolio

Market Risk Premium

APM  $E(R) = Rf + \Sigma\beta_j (R_j - R_f)$ 

- Rf) Riskfree Rate; # of Factors;

Betas relative to each factor

Factor risk premiums

Multi  $E(R) = Rf + \Sigma\beta_j (R_j - R_f)$ 

- Rf) Riskfree Rate; Macro factors

factor Betas relative to macro factors

Macro economic risk premiums

Proxy  $E(R) = a + \sum \beta_j Y_j$  Proxies

Regression coefficients

# Classic Risk & Return: Cost of Equity

¨ In the CAPM, the cost of equity:

Cost of Equity = Riskfree Rate + Equity Beta \* (Equity Risk Premium)

¨ In APM or Multi-factor models, you still need a risk free rate, as well as betas and risk premiums to go with each factor. ¨ To use any risk and return model, you need ¨ A risk free rate as a base ¨ A single equity risk premium (in the CAPM) or factor risk premiums, in the the multi-factor models ¨ A beta (in the CAPM) or betas (in multi-factor models)

29

# Discount Rates I

## The Riskfree Rate

# The Risk Free Rate: Laying the Foundations

- ¨ On a riskfree investment, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. ¨ For an investment to be riskfree, then, it has to have ¤ No default risk ¤ No reinvestment risk ¤ It follows then that if asked to estimate a risk free rate:
- 1. Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
- 2. Currencies matter: A risk free rate is currency-specific and can be very different for different currencies.
- 3. Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

# Test 1: A riskfree rate in US dollars!

- ¨ In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be
  - a. A three-month Treasury bill rate (4.42%)
  - b. A ten-year Treasury bond rate (3.88%)
  - c. A thirty-year Treasury bond rate (3.97%)
  - d. A TIPs (inflation-indexed treasury) rate (1.53%)
  - e. The highest of these numbers
  - f. The lowest of these numbers
  - g. Other (Specify)

What are we implicitly assuming about the US treasury when we use any of the treasury numbers?

# Test 2: A Riskfree Rate in Euros?

![](_page_31_Figure_2.jpeg)

# Test 3: A Riskfree Rate in Indian Rupees

- ¨ The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 7.18% on January 1, 2024. ¨ In January 2024, the Indian government had a local currency sovereign rating of Baa3. The typical default spread (over a default free rate) for Baa3 rated country bonds in early 2024 was 2.39%. The risk free rate in Indian Rupees is
  - a. The yield to maturity on the 10-year bond (7.18%)
  - b. The yield to maturity on the 10-year bond + Default spread (9.57%)
  - c. The yield to maturity on the 10-year bond Default spread (4.78%)
  - d. None of the above

# Sovereign Default Spread: Three paths to the same destination…

¨ Sovereign dollar or euro denominated bonds: Find sovereign bonds denominated in US dollars, issued by an emerging sovereign. ¤ Default spread = Emerging Govt Bond Rate (in US \$) – US Treasury Bond rate with same maturity. ¨ CDS spreads: Obtain the traded value for a sovereign Credit Default Swap (CDS) for the emerging government. ¤ Default spread = Sovereign CDS spread (with perhaps an adjustment for CDS market frictions). ¨ Sovereign-rating based spread: For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries with the same sovereign rating.

## Approach 1: Default spread from Government Bonds

| Country  | \$ Bond Rate | Riskfree Rate \$ Bonds | Default Spread |
|----------|--------------|------------------------|----------------|
| Peru     | 5.36%        | 3.88%                  | 1.48%          |
| Brazil   | 5.75%        | 3.88%                  | 1.87%          |
| Colombia | 5.25%        | 3.88%                  | 1.37%          |
| Poland   | 4.39%        | 3.88%                  | 0.51%          |
| Turkey   | 7.10%        | 3.88%                  | 3.22%          |
| Mexico   | 4.75%        | 3.88%                  | 0.87%          |
| Russia   | 11.55%       | 3.88%                  | 7.67%          |
| Bulgaria | 3.50%        | 2.03%                  | 1.47%          |

# Approach 2: CDS Spreads – January 2024

| Country        | 12/31/23     | CDS Spread net of US | Country     | 12/31/23 | CDS Spread net of US | Country        | 12/31/23 | CDS Spread net of US |
|----------------|--------------|----------------------|-------------|----------|----------------------|----------------|----------|----------------------|
| Abu Dhabi      | 0.75%        | 0.17%                | Greece      | 1.28%    | 0.70%                | Panama         | 2.31%    | 1.73%                |
| Algeria        | 1.70%        | 1.12%                | Guatamela   | 2.68%    | 2.10%                | Peru           | 1.37%    | 0.79%                |
| Angola         | 7.82%        | 7.24%                | Hong Kong   | 0.60%    | 0.02%                | Philippines    | 1.18%    | 0.60%                |
| Argentina      | 46.19%       | 45.61%               | Hungary     | 1.95%    | 1.37%                | Poland         | 1.06%    | 0.48%                |
| Australia      | 0.26%        | 0.00%                | Iceland     | 0.88%    | 0.30%                | Portugal       | 0.75%    | 0.17%                |
| Austria        | 0.27%        | 0.00%                | India       | 0.99%    | 0.41%                | Qatar          | 0.83%    | 0.25%                |
| Bahrain        | 2.74%        | 2.16%                | Indonesia   | 1.32%    | 0.74%                | Romania        | 2.31%    | 1.73%                |
| Belgium        | 0.33%        | 0.00%                | Iraq        | 5.14%    | 4.56%                | Russia         | NA       | NA                   |
| <b>Brazil</b>  | <b>2.39%</b> | <b>1.81%</b>         | Ireland     | 0.41%    | 0.00%                | Rwanda         | 5.53%    | 4.95%                |
| Bulgaria       | 1.47%        | 0.89%                | Israel      | 1.57%    | 0.99%                | Saudi Arabia   | 0.85%    | 0.27%                |
| Cameroon       | 9.14%        | 8.56%                | Italy       | 1.34%    | 0.76%                | Senegal        | 6.89%    | 6.31%                |
| Canada         | 0.44%        | 0.00%                | Japan       | 0.43%    | 0.00%                | Serbia         | 2.86%    | 2.28%                |
| Chile          | 1.15%        | 0.57%                | Kazakhstan  | 1.76%    | 1.18%                | Slovakia       | 0.60%    | 0.02%                |
| China          | 0.99%        | 0.41%                | Kenya       | 7.04%    | 6.46%                | Slovenia       | 0.76%    | 0.18%                |
| Colombia       | 2.74%        | 2.16%                | Korea       | 0.37%    | 0.00%                | South Africa   | 3.16%    | 2.58%                |
| Costa Rica     | 3.11%        | 2.53%                | Kuwait      | 0.83%    | 0.25%                | Spain          | 0.78%    | 0.20%                |
| Croatia        | 1.34%        | 0.76%                | Latvia      | 0.94%    | 0.36%                | Sri Lanka      | 59.36%   | NA                   |
| Cyprus         | 1.11%        | 0.53%                | Lebanon     | NA       | NA                   | Sweden         | 0.28%    | 0.00%                |
| Czech Republic | 0.56%        | 0.00%                | Lithuania   | 0.90%    | 0.32%                | Switzerland    | 0.22%    | 0.00%                |
| Denmark        | 0.24%        | 0.00%                | Malaysia    | 0.86%    | 0.28%                | Thailand       | 0.65%    | 0.07%                |
| Dubai          | 1.10%        | 0.52%                | Mexico      | 1.68%    | 1.10%                | Tunisia        | 9.78%    | 9.20%                |
| Ecuador        | 52.74%       | 52.16%               | Mongolia    | 4.02%    | 3.44%                | Turkey         | 3.86%    | 3.28%                |
| Egypt          | 10.13%       | 9.55%                | Morocco     | 1.90%    | 1.32%                | Ukraine        | NA       | NA                   |
| El Salvador    | 8.40%        | 7.82%                | Namibia     | 2.10%    | 1.52%                | United Kingdom | 0.51%    | 0.00%                |
| Estonia        | 0.60%        | 0.02%                | Netherlands | 0.24%    | 0.00%                | United States  | 0.58%    | 0.00%                |
| Ethiopia       | 32.31%       | 31.73%               | New Zealand | 0.29%    | 0.00%                | Uruguay        | 1.14%    | 0.56%                |
| Finland        | 0.34%        | 0.00%                | Nicaragua   | 4.89%    | 4.31%                | Venezuela      | 11.25%   | 10.67%               |
| France         | 0.43%        | 0.00%                | Nigeria     | 6.44%    | 5.86%                | Vietnam        | 1.84%    | 1.26%                |
| Gabon          | 6.85%        | 6.27%                | Norway      | 0.24%    | 0.00%                |                |          |                      |
| Germany        | 0.29%        | 0.00%                | Oman        | 1.92%    | 1.34%                |                |          |                      |

## Approach 3: Typical Default Spreads: January 2024

| S&P Sovereign Rating | Moody's Sovereign Rating | Default Spread |
|----------------------|--------------------------|----------------|
| AAA                  | Aaa                      | 0.00%          |
| AA+                  | Aa1                      | 0.44%          |
| AA                   | Aa2                      | 0.54%          |
| AA-                  | Aa3                      | 0.65%          |
| A+                   | A1                       | 0.77%          |
| A                    | A2                       | 0.92%          |
| A-                   | A3                       | 1.31%          |
| BBB+                 | Baa1                     | 1.74%          |
| BBB                  | Baa2                     | 2.07%          |
| BBB-                 | Baa3                     | 2.39%          |
| BB+                  | Ba1                      | 2.73%          |
| BB                   | Ba2                      | 3.28%          |
| BB                   | Ba3                      | 3.92%          |
| B+                   | B1                       | 4.90%          |
| B                    | B2                       | 5.99%          |
| B-                   | B3                       | 7.08%          |
| CCC+                 | Caa1                     | 8.17%          |
| CCC                  | Caa2                     | 9.81%          |
| CCC-                 | Caa3                     | 10.90%         |
| CC+                  | Ca1                      | 12.25%         |
| CC                   | Ca2                      | 14.00%         |
| CC-                  | Ca3                      | 15.00%         |
| C+                   | C1                       | 15.75%         |
| C                    | C2                       | 16.75%         |
| C-                   | C3                       | 18.00%         |

# Getting to a risk free rate in Brazilian Reais on January 1, 2024

- □ The Brazilian government bond rate in nominal reais on January 1, 2024, was 10.35%. To get to a riskfree rate in nominal reais, we can use one of three approaches.
  - □ Approach 1: Government Bond spread
    - ■ Default Spread = Brazil \$ Bond Rate – US T.Bond Rate =  $5.75\% - 3.88\% = 1.87\%$
    - ■ Riskfree rate in \$R =  $10.35\% - 1.87\% = 8.48\%$
  - □ Approach 2: The CDS Spread
    - ■ The CDS spread for Brazil, adjusted for the US CDS spread was  $1.81\%$ .
    - ■ Riskfree rate in \$R =  $10.35\% - 1.81\% = 8.54\%$
  - □ Approach 3: The Rating based spread
    - ■ Brazil has a Ba2 local currency rating from Moody's. The default spread for that rating is  $3.28\%$
    - ■ Riskfree rate in \$R =  $10.35\% - 3.28\% = 7.07\%$

# Test 4: A Real Riskfree Rate

- ¨ In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms. ¨ To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination. ¨ In January 2024, the yield on a 10-year indexed treasury bond was 1.80%. Which of the following statements would you subscribe to?
  - a. This (1.80%) is the real riskfree rate to use, if you are valuing US companies in real terms.
  - b. This (1.80%) is the real riskfree rate to use, anywhere in the world

Explain.

## Why do risk free rates vary across currencies? January 2024 Risk free rates

![](_page_39_Figure_2.jpeg)

# Or across time...

![](_page_40_Figure_5.jpeg)

# Risk free Rate: Don't have or don't trust the government bond rate?

¨ You can scale up the riskfree rate in a base currency (\$, Euros) by the differential inflation between the base currency and the currency in question. In US \$:

Risk free rate 
$$C_{\text{Currency}} = (1 + \text{Risk free rate}_{US} \$) \frac{(1 + \text{Expected Inflation}_{\text{Foreign Currency}}) - 1}{(1 + \text{Expected Inflation}_{US} \$)}$$

¨ Thus, if the US \$ risk free rate is 2.00%, the inflation rate in Egyptian pounds is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

Risk free rate = 
$$(1.02) \frac{(1.15)}{(1.015)} - 1 = 15.57\%$$

# One more test on riskfree rates…

- ¨ On January 1, 2022, the 10-year treasury bond rate in the United States was 1.51%, low by historic standards. Assume that you are valuing a company in US dollars then but are wary about the riskfree rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate.
  - c. Something else…

# Some perspective on risk free rates

![](_page_43_Figure_2.jpeg)

# Negative Interest Rates?

¨ In 2022, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates? ¤ How negative can rates get? (Is there a bound?) ¤ Would you use these negative interest rates as risk free rates? <sup>n</sup> If no, why not and what would you do instead? <sup>n</sup> If yes, what else would you have to do in your valuation to be internally consistent?

46

# Discount Rates: II

## The Equity Risk Premium

## II. The Equity Risk Premium The ubiquitous historical risk premium

¨ The historical premium is the premium that stocks have historically earned over riskless securities. ¨ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to ¤ How far back you go in history… ¤ Whether you use T.bill rates or T.Bond rates ¤ Whether you use geometric or arithmetic averages. ¨ For instance, looking at the US:

|           | <i>Arithmetic Average</i> |                   | <i>Geometric Average</i> |                   |
|-----------|---------------------------|-------------------|--------------------------|-------------------|
|           | Stocks - T. Bills         | Stocks - T. Bonds | Stocks - T. Bills        | Stocks - T. Bonds |
| 1928-2023 | 8.32%                     | 6.80%             | 6.50%                    | 5.23%             |
| Std Error | 2.03%                     | 2.14%             |                          |                   |
| 1974-2023 | 8.18%                     | 5.95%             | 6.79%                    | 4.97%             |
| Std Error | 2.45%                     | 2.73%             |                          |                   |
| 2014-2023 | 11.70%                    | 11.17%            | 10.63%                   | 10.44%            |
| Std Error | 4.97%                     | 3.86%             |                          |                   |

# The perils of trusting the past…….

¨ Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 90 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

Standard Error in Premium = 20%/√90 = 2.1%

¨ Survivorship Bias: Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

# The simplest way of estimating an additional country risk premium: The country default spread

- □ Default spread for country: In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - ■ The default spread on a dollar denominated bond issued by the country. (In January 2024, that spread was % for the Brazilian \$ bond) was 1.817%.
  - ■ The sovereign CDS spread for the country. In January 2024, the ten-year CDS spread for Brazil, adjusted for the US CDS, was 1.81%.
  - ■ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Ba2 and the default spread for a Ba2 rated sovereign was about 3.28% in January 2024.
- □ Add the default spread to a “mature” market premium: This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 4.60%.
  - ■ Country Risk Premium for Brazil = 3.28%
  - ■ Total ERP for Brazil = 4.60% + 3.28% = 7.88%

## An equity volatility based approach to estimating the country total ERP

- ❑ This approach draws on the standard deviation of two equity markets, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ❑  $\text{Total equity risk premium} = \text{Risk Premium}_{\text{US}} * \sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$
- ❑ The country equity risk premium is based upon the volatility of the market in question relative to U.S market.
  - ❑ Assume that the equity risk premium for the US is 5.94%.
  - ❑ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ❑  $\text{Total Equity Risk Premium for Brazil} = 4.60\% (30\%/18\%) = 7.67\%$
  - ❑  $\text{Country equity risk premium for Brazil} = 7.67\% - 4.60\% = 3.07\%$

## A melded approach to estimating the additional country risk premium

- ❑ Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
- ❑ Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. Using this approach for Brazil in January 2024, you would get:
  - ❑ Country Equity risk premium = Default spread on country bond\*  $\sigma_{\text{Country}}$   
     $\text{Equity} / \sigma_{\text{Country}} \text{ Bond}$ 
    - ■ Standard Deviation in Bovespa (Equity) = 30%
    - ■ Standard Deviation in Brazil government bond = 20%
    - ■ Default spread for Brazil= 3.28%
  - ❑ Brazil Country Risk Premium =  $3.28\% (30\%/20\%) = 4.92\%$
  - ❑ Brazil Total ERP = Mature Market Premium + CRP =  $4.60\% + 4.92\% = 9.52\%$

# A Template for Estimating the ERP

## ERP Estimation Procedure

Step 1: Mature Market Premium

Step 2: Assess country risk

Step 3: Convert country risk measure into an additional country risk premium for equity

Step 4: Estimate an ERP for country

![](_page_51_Diagram_30.jpeg)

*Blue: Moody's Rating Red: Added Country Risk Green #: Total ERP*

| Andorra              | Baal | 2.08% | 2.78% | 7.38%                    | Italy              | Baal         | 2.08%        | 7.81% |
|----------------------|------|-------|-------|--------------------------|--------------------|--------------|--------------|-------|
| Austria              | Aal  | 0.88% | 5.18% | 5.18%                    | Jersey (States of) | Aal          | 0.88%        | 5.48% |
| Belgium              | Aal  | 0.88% | 5.18% | 5.18%                    | Liechtenstein      | Aal          | 0.00%        | 4.60% |
| Cyprus               | Baal | 2.78% | 7.38% | 7.38%                    | Luxembourg         | Aal          | 0.00%        | 4.60% |
| Denmark              | Aal  | 0.00% | 4.60% | Malta                    | Aal                | 2.14%        | 5.84%        |       |
| Finland              | Aal  | 0.58% | 5.18% | Netherlands              | Aal                | 0.00%        | 4.60%        |       |
| France               | Aal  | 0.72% | 5.32% | Norway                   | Aal                | 0.00%        | 4.60%        |       |
| Germany              | Aal  | 0.00% | 4.60% | Portugal                 | Al                 | 1.75%        | 6.35%        |       |
| Greece               | Bal  | 3.66% | 8.26% | Spain                    | Baal               | 2.34%        | 6.94%        |       |
| Guernsey (States of) | Al   | 1.03% | 5.63% | Sweden                   | Aal                | 0.00%        | 4.60%        |       |
| Iceland              | Al   | 1.24% | 5.84% | Switzerland              | Aal                | 0.00%        | 4.60%        |       |
| Ireland              | Aal  | 0.88% | 5.48% | Turkey                   | Bl                 | 9.51%        | 14.11%       |       |
| Isle of Man          | Aal  | 0.88% | 5.48% | United Kingdom           | Aal                | 0.88%        | 5.48%        |       |
|                      |      |       |       | <b>EU &amp; Environs</b> |                    | <b>1.29%</b> | <b>5.89%</b> |       |

| Canada               | Aaa       | 0.00%        | 4.60%        |
|----------------------|-----------|--------------|--------------|
| United States        | Aaa       | 0.00%        | 4.60%        |
| <b>North America</b> | <b>Aa</b> | <b>0.00%</b> | <b>4.60%</b> |

| Caribbean            |      | 14.15%       | 18.75%        |
|----------------------|------|--------------|---------------|
| Argentina            | Ca   | 17.55%       | 22.15%        |
| Belize               | Caa2 | 13.17%       | 17.77%        |
| Bolivia              | Caa1 | 10.97%       | 15.57%        |
| Brazil               | Ba2  | 4.40%        | 9.00%         |
| Chile                | A2   | 1.24%        | 5.84%         |
| Colombia             | Baa2 | 2.78%        | 7.38%         |
| Costa Rica           | B1   | 6.58%        | 11.18%        |
| Ecuador              | Caa3 | 14.63%       | 19.23%        |
| El Salvador          | Caa3 | 14.63%       | 19.23%        |
| Guatemala            | Ba1  | 3.66%        | 8.26%         |
| Honduras             | B1   | 6.58%        | 11.18%        |
| Mexico               | Baa2 | 2.78%        | 7.38%         |
| Nicaragua            | B3   | 9.51%        | 14.11%        |
| Panama               | Baa2 | 2.78%        | 7.38%         |
| Paraguay             | Ba1  | 3.66%        | 8.26%         |
| Peru                 | Baa1 | 2.34%        | 6.94%         |
| Suriname             | Caa3 | 14.63%       | 19.23%        |
| Uruguay              | Baa2 | 2.78%        | 7.38%         |
| Venezuela            | C    | 23.49%       | 28.09%        |
| <b>Latin America</b> |      | <b>5.76%</b> | <b>10.36%</b> |

Aswath Damodaran

| <i>Country</i> | <i>Rating</i> | <i>CRP</i>          | <i>ERP</i>            |
|----------------|---------------|---------------------|-----------------------|
| Angola         | B3            | <b>6.91%</b>        | <b>1.41.1%</b>        |
| Benin          | B1            | <b>6.58%</b>        | <b>1.11.8%</b>        |
| Botswana       | A3            | <b>1.67%</b>        | <b>6.35%</b>          |
| Burkina Faso   | Caa1          | <b>1.07%</b>        | <b>1.57.7%</b>        |
| Cameroon       | Caa1          | <b>1.07%</b>        | <b>1.57.7%</b>        |
| Cape Verde     | B3            | <b>9.51%</b>        | <b>1.41.1%</b>        |
| Congo (DR)     | B3            | <b>9.51%</b>        | <b>1.41.1%</b>        |
| Congo (Rep of) | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Côte d'Ivoire  | Ba3           | <b>5.26%</b>        | <b>9.86%</b>          |
| Egypt          | Caa1          | <b>1.07%</b>        | <b>1.57.7%</b>        |
| Ethiopia       | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Gabon          | Caa1          | <b>1.07%</b>        | <b>1.57.7%</b>        |
| Ghana          | Caa3          | <b>1.46%</b>        | <b>1.93.2%</b>        |
| Kenya          | B3            | <b>6.91%</b>        | <b>1.41.1%</b>        |
| Mali           | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Mauritius      | Baa3          | <b>2.21%</b>        | <b>7.81%</b>          |
| Morocco        | Ba1           | <b>6.66%</b>        | <b>8.26%</b>          |
| Mozambique     | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Namibia        | B1            | <b>6.58%</b>        | <b>1.11.8%</b>        |
| Niger          | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Nigeria        | Caa1          | <b>1.07%</b>        | <b>1.57.7%</b>        |
| Rwanda         | B2            | <b>6.86%</b>        | <b>1.12.6%</b>        |
| Senegal        | Ba3           | <b>5.26%</b>        | <b>9.86%</b>          |
| South Africa   | Ba2           | <b>4.40%</b>        | <b>9.00%</b>          |
| Swaziland      | B3            | <b>9.51%</b>        | <b>1.41.1%</b>        |
| Tanzania       | B2            | <b>8.04%</b>        | <b>1.24.6%</b>        |
| Togo           | B3            | <b>9.51%</b>        | <b>1.41.1%</b>        |
| Tunisia        | Caa2          | <b>1.17%</b>        | <b>1.77.7%</b>        |
| Uganda         | B2            | <b>8.04%</b>        | <b>1.24.6%</b>        |
| Zambia         | Caa3          | <b>1.46%</b>        | <b>1.93.2%</b>        |
| <b>Africa</b>  |               | <b><b>9.16%</b></b> | <b><b>1.17.6%</b></b> |

|  | Albania            | B1   | 6.58%  | 11.18% |
|--|--------------------|------|--------|--------|
|  | Armenia            | Ba3  | 5.26%  | 9.86%  |
|  | Azerbaijan         | Ba1  | 3.66%  | 8.26%  |
|  | Belarus            | C    | 23.49% | 28.09% |
|  | Bosnia and Herzego | B3   | 9.51%  | 14.11% |
|  | Bulgaria           | Baa1 | 2.34%  | 6.94%  |
|  | Croatia            | Baa2 | 2.78%  | 7.38%  |
|  | Czech Republic     | Aa3  | 0.88%  | 5.48%  |
|  | Estonia            | A1   | 1.03%  | 5.63%  |
|  | Georgia            | Ba2  | 4.40%  | 9.09%  |
|  | Hungary            | Baa2 | 2.78%  | 7.38%  |
|  | Kazakhstan         | Baa2 | 2.78%  | 7.38%  |
|  | Kyrgyzstan         | B3   | 9.51%  | 14.11% |
|  | Latvia             | A3   | 1.75%  | 6.35%  |
|  | Lithuania          | A2   | 1.24%  | 5.84%  |
|  | Macedonia          | Ba3  | 5.26%  | 9.86%  |
|  | Moldova            | B3   | 9.51%  | 14.11% |
|  | Montenegro         | B1   | 6.58%  | 11.18% |
|  | Poland             | A2   | 1.24%  | 5.84%  |
|  | Romania            | Baa3 | 3.21%  | 7.81%  |
|  | Russia             | NA   | 6.58%  | 11.18% |
|  | Serbia             | Ba2  | 4.40%  | 9.09%  |
|  | Slovakia           | A2   | 1.24%  | 5.84%  |
|  | Slovenia           | A3   | 1.75%  | 6.35%  |
|  | Tajikistan         | B3   | 9.51%  | 14.11% |
|  | Ukraine            | Ca   | 17.55% | 22.15% |
|  | Uzbekistan         | Ba3  | 5.26%  | 9.86%  |
|  | E. Europe & Russia | B3   | 5.06%  | 9.66%  |

| Abu Dhabi            | Aa2  | 0.72%        | 5.32%        |
|----------------------|------|--------------|--------------|
| Bahrain              | B2   | 8.04%        | 12.64%       |
| Iraq                 | Caa1 | 10.97%       | 15.57%       |
| Israel               | A1   | 1.03%        | 5.63%        |
| Jordan               | B1   | 6.58%        | 11.18%       |
| Kuwait               | A1   | 1.03%        | 5.63%        |
| Lebanon              | C    | 23.49%       | 28.09%       |
| Oman                 | Ba1  | 3.66%        | 8.26%        |
| Oatar                | Aa3  | 0.88%        | 5.48%        |
| Ras Al Khaimah       | A3   | 1.75%        | 6.35%        |
| Saudi Arabia         | A1   | 1.03%        | 5.63%        |
| Sharjah              | Ba1  | 3.66%        | 8.26%        |
| United Arab Emirates | Aa2  | 0.72%        | 5.32%        |
| Middle East          |      | <b>2.16%</b> | <b>6.76%</b> |

| <i>Country</i>  | <i>PRS</i> | <i>CRP</i> | <i>ERP</i> |
|-----------------|------------|------------|------------|
| Algeria         | 67.75      | 6.58%      | 11.18%     |
| Brunei          | 81.5       | 0.88%      | 5.48%      |
| Gambia          | 66.75      | 6.58%      | 11.18%     |
| Guinea          | 60         | 13.17%     | 17.77%     |
| Guinea-Bissau   | 65.25      | 8.04%      | 12.64%     |
| Guyana          | 75.25      | 2.34%      | 6.94%      |
| Haiti           | 56.5       | 14.63%     | 19.23%     |
| Iran            | 63         | 9.51%      | 14.11%     |
| Korea, D.P.R.   | 49.25      | 23.49%     | 28.09%     |
| Liberia         | 55         | 17.55%     | 22.15%     |
| Libya           | 73.75      | 2.78%      | 7.38%      |
| Madagascar      | 62.75      | 9.51%      | 14.11%     |
| Malawi          | 52.75      | 17.55%     | 22.15%     |
| Myanmar         | 57         | 14.63%     | 19.23%     |
| Russia          | 66.75      | 6.58%      | 11.18%     |
| Sierra Leone    | 56.25      | 14.63%     | 19.23%     |
| Somalia         | 51.75      | 17.55%     | 22.15%     |
| Sudan           | 44.75      | 23.49%     | 28.09%     |
| Syria           | 45         | 23.49%     | 28.09%     |
| Yemen, Republic | 55.75      | 14.63%     | 19.23%     |
| Zimbabwe        | 57.5       | 13.17%     | 17.77%     |

| Bangladesh       | B1   | B2           | B3           | B4     | B5     |
|------------------|------|--------------|--------------|--------|--------|
| Cambodia         | B2   | B.04%        | 12.64%       | 11.62% | 11.01% |
| China            | A1   | 1.03%        | 5.63%        | 5.63%  | 5.63%  |
| Fiji             | B1   | 6.58%        | 11.18%       | 11.18% | 11.18% |
| Hong Kong        | Aa3  | 0.88%        | 5.48%        | 5.48%  | 5.48%  |
| India            | Baa3 | 3.21%        | 7.81%        | 7.81%  | 7.81%  |
| Indonesia        | Baa2 | 2.78%        | 7.38%        | 7.38%  | 7.38%  |
| Japan            | A1   | 1.03%        | 5.63%        | 5.63%  | 5.63%  |
| Korea            | Aa2  | 0.72%        | 5.32%        | 5.32%  | 5.32%  |
| Laos             | Caa3 | 14.63%       | 19.23%       | 19.23% | 19.23% |
| Macao            | Aa3  | 0.88%        | 5.48%        | 5.48%  | 5.48%  |
| Malaysia         | A3   | 1.75%        | 6.35%        | 6.35%  | 6.35%  |
| Maldives         | Caa1 | 10.97%       | 15.57%       | 15.57% | 15.57% |
| Mongolia         | B3   | 9.51%        | 14.11%       | 14.11% | 14.11% |
| Pakistan         | Caa3 | 14.63%       | 19.23%       | 19.23% | 19.23% |
| Papua New Guinea | B2   | 8.04%        | 12.64%       | 12.64% | 12.64% |
| Philippines      | Baa2 | 2.78%        | 7.38%        | 7.38%  | 7.38%  |
| Singapore        | Aaa  | 0.00%        | 4.60%        | 4.60%  | 4.60%  |
| Solomon Islands  | Caa1 | 10.97%       | 15.57%       | 15.57% | 15.57% |
| Sri Lanka        | Ca   | 17.55%       | 22.15%       | 22.15% | 22.15% |
| Taiwan           | Aa3  | 0.88%        | 5.48%        | 5.48%  | 5.48%  |
| Thailand         | Baa1 | 2.34%        | 6.94%        | 6.94%  | 6.94%  |
| Vietnam          | Ba2  | 4.40%        | 9.00%        | 9.00%  | 9.00%  |
| <b>Asia</b>      |      | <b>1.68%</b> | <b>6.28%</b> | 6.28%  | 6.28%  |

| <b>Australia</b>          | <b>Aaa</b> | <b>0.00%</b> | <b>4.90%</b>  |
|---------------------------|------------|--------------|---------------|
| Cook Islands              | <b>B1</b>  | <b>6.58%</b> | <b>11.18%</b> |
| New Zealand               | <b>Aaa</b> | <b>0.00%</b> | <b>4.60%</b>  |
| <b>Australia &amp; NZ</b> |            | <b>0.00%</b> | <b>4.60%</b>  |

## From Country Equity Risk Premiums to Corporate Equity Risk premiums

- ❑ Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,
  - ❑  $E(\text{Return}) = \text{Riskfree Rate} + \text{CRP} + \text{Beta} (\text{Mature ERP})$
- ❑ Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.
  - ❑  $E(\text{Return}) = \text{Riskfree Rate} + \text{Beta} (\text{Mature ERP} + \text{CRP})$
- ❑ Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)
  - ❑  $E(\text{Return}) = \text{Riskfree Rate} + \beta (\text{Mature ERP}) + \lambda (\text{CRP})$Mature ERP = Mature market Equity Risk Premium

  CRP = Additional country risk premium

# Estimating country risk premium exposure\_ Vaiants

![](_page_54_Diagram_7.jpeg)

## Operation based CRP: Single versus Multiple Emerging Markets

¨ Single emerging market: Embraer, in 2004, reported that it derived 3% of its revenues in Brazil and the balance from mature markets. The mature market ERP in 2004 was 5% and Brazil's CRP was 7.89%.

|                             | Revenues | Total ERP    | CRP          |
|-----------------------------|----------|--------------|--------------|
| US and other mature markets | 97%      | 5.00%        | 0.00%        |
| Brazil                      | 3%       | 12.89%       | 8%           |
| Embraer                     |          | <b>5.24%</b> | <b>0.24%</b> |

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

## Extending to a multinational: Regional breakdown Coca Cola's revenue breakdown and ERP in 2012

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

| Country               | Oil & Gas Production | % of Total | ERP    |
|-----------------------|----------------------|------------|--------|
| Denmark               | 17396                | 3.83%      | 6.20%  |
| Italy                 | 11179                | 2.46%      | 9.14%  |
| Norway                | 14337                | 3.16%      | 6.20%  |
| UK                    | 20762                | 4.57%      | 6.81%  |
| Rest of Europe        | 874                  | 0.19%      | 7.40%  |
| Brunei                | 823                  | 0.18%      | 9.04%  |
| Iraq                  | 20009                | 4.40%      | 11.37% |
| Malaysia              | 22980                | 5.06%      | 8.05%  |
| Oman                  | 78404                | 17.26%     | 7.29%  |
| Russia                | 22016                | 4.85%      | 10.06% |
| Rest of Asia & ME     | 24480                | 5.39%      | 7.74%  |
| Oceania               | 7858                 | 1.73%      | 6.20%  |
| Gabon                 | 12472                | 2.75%      | 11.76% |
| Nigeria               | 67832                | 14.93%     | 11.76% |
| Rest of Africa        | 6159                 | 1.36%      | 12.17% |
| USA                   | 104263               | 22.95%     | 6.20%  |
| Canada                | 8599                 | 1.89%      | 6.20%  |
| Brazil                | 13307                | 2.93%      | 9.60%  |
| Rest of Latin America | 576                  | 0.13%      | 10.78% |
| Royal Dutch Shell     | 454326               | 100.00%    | 8.26%  |

# Estimate a lambda for country risk

¨ Country risk exposure is affected by where you get your revenues and where your production happens, but there are a host of other variables that also affect this exposure, including: ¤ Use of risk management products: Companies can use both options/futures markets and insurance to hedge some or a significant portion of country risk. ¤ Government "national" interests: There are sectors that are viewed as vital to the national interests, and governments often play a key role in these companies, either officially or unofficially. These sectors are more exposed to country risk. ¨ It is conceivable that there is a richer measure of country risk that incorporates all of the variables that drive country risk in one measure. That way my rationale when I devised "lambda" as my measure of country risk exposure.

# A Revenue-based Lambda

- The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:

$$\lambda$$
 = % of revenues domestically<sub>firm</sub>/ % of revenues domestically<sub>average firm</sub>

- Consider two firms – Tata Motors and Tata Consulting Services, both Indian companies. In 2008-09, Tata Motors got about 91.37% of its revenues in India and TCS got 7.62%. The average Indian firm gets about 80% of its revenues in India:

$$\lambda_{\text{Tata Motors}} = 91\%/80\% = 1.14$$

$$\lambda_{\text{TCS}} = 7.62\%/80\% = 0.09$$

- □ There are two implications
  - ■ A company's risk exposure is determined by where it does business and not by where it is incorporated.
  - ■ Firms might be able to actively manage their country risk exposures

## A Price/Return based Lambda

Embraer versus C Bond: 2000-2003

![](_page_61_Figure_5.jpeg)

Embratel versus C Bond: 2000-2003

![](_page_61_Figure_7.jpeg)

ReturnEmbraer = 0.0195 + **0.2681** ReturnC Bond

ReturnEmbratel = -0.0308 + **2.0030** ReturnC Bond

## Estimating a US Dollar Cost of Equity for Embraer - September 2004

¨ Assume that the beta for Embraer is 1.07, and that the US \$ riskfree rate used is 4%. Also assume that the risk premium for the US is 5% and the country risk premium for Brazil is 7.89%. Finally, assume that Embraer gets 3% of its revenues in Brazil & the rest in the US. ¨ There are five estimates of \$ cost of equity for Embraer: ¤ Approach 1: Constant exposure to CRP, Location CRP n E(Return) = 4% + 1.07 (5%) + 7.89% = 17.24% ¤ Approach 2: Constant exposure to CRP, Operation CRP n E(Return) = 4% + 1.07 (5%) + (0.03\*7.89% +0.97\*0%)= 9.59% ¤ Approach 3: Beta exposure to CRP, Location CRP n E(Return) = 4% + 1.07 (5% + 7.89%)= 17.79% ¤ Approach 4: Beta exposure to CRP, Operation CRP n E(Return) = 4% + 1.07 (5% +( 0.03\*7.89%+0.97\*0%)) = 9.60% ¤ Approach 5: Lambda exposure to CRP n E(Return) = 4% + 1.07 (5%) + 0.27(7.89%) = 11.48%

## Valuing Emerging Market Companies with significant exposure in developed markets

- ¨ The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk. Thus, in 2004, Embraer would have been valued with a cost of equity of 17-18% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
  - a. Emerging market companies with substantial exposure in developed markets will be significantly over valued by analysts
  - b. Emerging market companies with substantial exposure in developed markets will be significantly under valued by analysts

Can you construct an investment strategy to take advantage of the mis-valuation? What would need to happen for you to make money of this strategy?

# Implied Equity Premiums

¨ For a start: If you know the price paid for an asset and have estimates of the expected cash flows on the asset, you can estimate the IRR of these cash flows. If you paid the price, this is your expected return. ¨ Stock Price & Risk: If you assume that stocks are correctly priced in the aggregate and you can estimate the expected cashflows from buying stocks, you can estimate the expected rate of return on stocks by finding that discount rate that makes the present value equal to the price paid. ¨ Implied ERP: Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward-looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

# Equity Risk Premium: January 2020

![](_page_65_Diagram_25.jpeg)

# And in 2020.. COVID effects

![](_page_66_Figure_7.jpeg)

# An Updated Estimate: ERP in 2024

![](_page_67_Diagram_24.jpeg)

# Implied Premiums in the US: 1960-2023

*Implied Equity Risk Premium for US Equity Market: 1960-2023*

![](_page_68_Figure_15.jpeg)

# Implied Premium versus Risk Free Rate

![](_page_69_Figure_2.jpeg)

## Equity Risk Premiums and Bond Default Spreads

![](_page_70_Figure_2.jpeg)

## Equity Risk Premiums and Cap Rates (Real Estate)

![](_page_71_Figure_2.jpeg)

# Why implied premiums matter?

- ¨ In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. ¨ If all analysts in a group used the arithmetic average premium (for stocks over T.Bills) for 1928-2023 of 8.32% to value stocks in January 2022, given the implied premium of 4.60%, what are they likely to find?
  - a. The values they obtain will be too low (most stocks will look overvalued)
  - b. The values they obtain will be too high (most stocks will look under valued)
  - c. There should be no systematic bias as long as they use the same premium to value all stocks.

## Which equity risk premium should you use?

## **If you assume this Premium to use**

Premiums revert back to historical norms and your time period yields these norms

Historical risk premium

Market is correct in the aggregate or that your valuation should be market neutral

Current implied equity risk premium

Marker makes mistakes even in the aggregate but is correct over time

Average implied equity risk premium over time.

| Predictor                             | Correlation with implied premium next year | Correlation with return- next 5 years | Correlation with actual – next 10 years |
|---------------------------------------|--------------------------------------------|---------------------------------------|-----------------------------------------|
| Current implied premium               | 0.763                                      | 0.427                                 | 0.500                                   |
| Average implied premium: Last 5 years | 0.718                                      | 0.326                                 | 0.450                                   |
| Historical Premium                    | -0.497                                     | -0.437                                | -0.454                                  |
| Default Spread based premium          | 0.047                                      | 0.143                                 | 0.160                                   |

# An ERP for the Sensex

¨ Inputs for the computation ¤ Sensex on 9/5/07 = 15446 ¤ Dividend yield on index = 3.05% ¤ Expected growth rate - next 5 years = 14% ¤ Growth rate beyond year 5 = 6.76% (set equal to riskfree rate) ¨ Solving for the expected return:

¨ Expected return on stocks = 11.18% ¨ Implied equity risk premium for India = 11.18% - 6.76% = 4.42%

$$15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$$

# The evolution of Emerging Market Risk

| Start of year | PBV (Developed) | PBV (Emerging) | ROE (Developed) | ROE (Emerging) | US T.Bond Rate | Growth Rate (Developed) | Growth Rate (Emerging) | Cost of Equity (Developed) | Cost of Equity (Emerging) | Differential |
|---------------|-----------------|----------------|-----------------|----------------|----------------|-------------------------|------------------------|----------------------------|---------------------------|--------------|
| 2004          | 2.00            | 1.19           | 10.81%          | 11.65%         | 4.25%          | 3.75%                   | 4.75%                  | 7.28%                      | 10.55%                    | 3.27%        |
| 2005          | 2.09            | 1.27           | 11.12%          | 11.93%         | 4.22%          | 3.72%                   | 4.72%                  | 7.26%                      | 10.40%                    | 3.14%        |
| 2006          | 2.03            | 1.44           | 11.32%          | 12.18%         | 4.39%          | 3.89%                   | 4.89%                  | 7.55%                      | 9.95%                     | 2.40%        |
| 2007          | 1.67            | 1.67           | 10.87%          | 12.88%         | 4.70%          | 4.20%                   | 5.20%                  | 8.19%                      | 9.80%                     | 1.60%        |
| 2008          | 0.87            | 0.83           | 9.42%           | 11.12%         | 4.02%          | 3.52%                   | 4.52%                  | 10.30%                     | 12.47%                    | 2.17%        |
| 2009          | 1.20            | 1.34           | 8.48%           | 11.02%         | 2.21%          | 1.71%                   | 2.71%                  | 7.35%                      | 8.91%                     | 1.56%        |
| 2010          | 1.39            | 1.43           | 9.14%           | 11.22%         | 3.84%          | 3.34%                   | 4.34%                  | 7.51%                      | 9.15%                     | 1.64%        |
| 2011          | 1.12            | 1.08           | 9.21%           | 10.04%         | 3.29%          | 2.79%                   | 3.79%                  | 8.52%                      | 9.58%                     | 1.05%        |
| 2012          | 1.17            | 1.18           | 9.10%           | 9.33%          | 1.88%          | 1.38%                   | 2.38%                  | 7.98%                      | 8.27%                     | 0.29%        |
| 2013          | 1.56            | 1.63           | 8.67%           | 10.48%         | 1.76%          | 1.26%                   | 2.26%                  | 6.01%                      | 7.30%                     | 1.29%        |
| 2014          | 1.95            | 1.50           | 9.27%           | 9.64%          | 3.04%          | 2.54%                   | 3.54%                  | 5.99%                      | 7.61%                     | 1.62%        |
| 2015          | 1.88            | 1.56           | 9.69%           | 9.75%          | 2.17%          | 1.67%                   | 2.67%                  | 5.94%                      | 7.21%                     | 1.27%        |
| 2016          | 1.99            | 1.59           | 9.24%           | 10.16%         | 2.27%          | 1.77%                   | 2.77%                  | 5.52%                      | 7.42%                     | 1.89%        |
| 2017          | 1.76            | 1.48           | 8.71%           | 9.53%          | 2.68%          | 2.18%                   | 3.18%                  | 5.89%                      | 7.47%                     | 1.58%        |
| 2018          | 1.98            | 1.66           | 11.23%          | 11.36%         | 2.68%          | 2.18%                   | 3.18%                  | 6.75%                      | 8.11%                     | 1.36%        |
| 2019          | 1.64            | 1.31           | 12.09%          | 11.35%         | 2.68%          | 2.18%                   | 3.18%                  | 8.22%                      | 9.42%                     | 1.19%        |
| 2020          | 2.26            | 1.64           | 10.41%          | 9.10%          | 1.92%          | 1.42%                   | 2.42%                  | 5.40%                      | 6.49%                     | 1.10%        |
| 2021          | 2.21            | 1.77           | 6.30%           | 7.31%          | 0.93%          | 0.43%                   | 1.43%                  | 3.09%                      | 4.75%                     | 1.67%        |
| 2022          | 2.31            | 1.67           | 13.22%          | 11.99%         | 1.51%          | 1.01%                   | 2.01%                  | 6.30%                      | 7.99%                     | 1.69%        |
| 2023          | 2.28            | 1.44           | 12.90%          | 10.93%         | 3.88%          | 3.38%                   | 4.38%                  | 7.56%                      | 8.93%                     | 1.37%        |

## Relative Risk Measures

# **<sup>77</sup>** Discount Rates: III

# The CAPM Beta: The Most Used (and Misused) Risk Measure

¨ The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm) -

Rj = a + b Rm

where a is the intercept and b is the slope of the regression.

- ¨ The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock. ¨ This beta has three problems:
  - It has high standard error
  - It reflects the firm's business mix over the period of the regression, not the current mix
  - It reflects the firm's average financial leverage over the period rather than the current leverage.

# Unreliable, when it looks bad..

![](_page_78_Figure_2.jpeg)

# Or when it looks good..

![](_page_79_Figure_35.jpeg)

# One slice of history..

**81**

![](_page_80_Figure_5.jpeg)

![](_page_80_Figure_7.jpeg)

During 2019 and 2020, GME was an extraordinarily volatile stock, as short sellers and long only investors fought out a battle.

# And subject to game playing

![](_page_81_Figure_13.jpeg)

![](_page_81_Figure_14.jpeg)

## Measuring Relative Risk: You don't like betas or modern portfolio theory? No problem.

![](_page_82_Diagram_2.jpeg)

# Don't like the diversified investor focus, but okay with price-based measures

84

## 1. Relative Standard Deviation

- • Relative Volatility = Std dev of Stock/ Average Std dev across all stocks
- • Captures all risk, rather than just market risk

## 2. Proxy Models

- • Look at historical returns on all stocks and look for variables that explain differences in returns.
- • You are, in effect, running multiple regressions with returns on individual stocks as the dependent variable and fundamentals about these stocks as independent variables.
- • This approach started with market cap (the small cap effect) and over the last two decades has added other variables (momentum, liquidity etc.)

## 3. CAPM Plus Models

- • Start with the traditional CAPM ( $R_f + Beta$  (ERP)) and then add other premiums for proxies.

# Don't like the price-based approach..

- 1. Accounting risk measures: To the extent that you don't trust market-priced based measures of risk, you could compute relative risk measures based on
  - Accounting earnings volatility: Compute an accounting beta or relative volatility
  - Balance sheet ratios: You could compute a risk score based upon accounting ratios like debt ratios or cash holdings (akin to default risk scores like the Z score)
- 2. Qualitative Risk Models: In these models, risk assessments are based at least partially on qualitative factors (quality of management).
- 3. Debt based measures: You can estimate a cost of equity, based upon an observable costs of debt for the company.
  - Cost of equity = Cost of debt \* Scaling factor
  - The scaling factor can be computed from implied volatilities.

# Determinants of Betas & Relative Risk

![](_page_85_Diagram_2.jpeg)

In a perfect world… we would estimate the beta of a firm by doing the following

Start with the beta of the business that the firm is in

Adjust the business beta for the operating leverage of the firm to arrive at the unlevered beta for the firm.

Use the financial leverage of the firm to estimate the equity beta for the firm Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (Debt/Equity))

# Adjusting for operating leverage…

¨ Within any business, firms with lower fixed costs (as a percentage of total costs) should have lower unlevered betas. If you can compute fixed and variable costs for each firm in a sector, you can break down the unlevered beta into business and operating leverage components. ¤ Unlevered beta = Pure business beta \* (1 + (Fixed costs/ Variable costs)) ¨ The biggest problem with doing this is informational. It is difficult to get information on fixed and variable costs for individual firms. ¨ In practice, we tend to assume that the operating leverage of firms within a business are similar and use the same unlevered beta for every firm.

# Adjusting for financial leverage...

89

- □ Conventional approach: If we assume that debt carries no market risk (has a beta of zero), the beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_L = \beta_u (1 + ((1-t)D/E))$$

In some versions, the tax effect is ignored and there is no  $(1-t)$  in the equation.

- □ Debt Adjusted Approach: If beta carries market risk and you can estimate the beta of debt, you can estimate the levered beta as follows:

$$\beta_L = \beta_u (1 + ((1-t)D/E)) - \beta_{\text{debt}} (1-t) (D/E)$$

While the latter is more realistic, estimating betas for debt can be difficult to do.

# Bottom-up Betas

Step 1: Find the business or businesses that your firm operates in.

![](_page_89_Diagram_3.jpeg)

Step 2: Find publicly traded firms in each of these businesses and obtain their regression betas. Compute the simple average across these regression betas to arrive at an average beta for these publicly traded firms. Unlever this average beta using the average debt to equity ratio across the publicly traded firms in the sample. Unlevered beta for business = Average beta across publicly traded firms/ (1 + (1- t) (Average D/E ratio across firms))

![](_page_89_Diagram_5.jpeg)

If you can, adjust this beta for differences between your firm and the comparable firms on operating leverage and product characteristics.

Step 3: Estimate how much value your firm derives from each of the different businesses it is in.

![](_page_89_Diagram_7.jpeg)

While revenues or operating income are often used as weights, it is better to try to estimate the value of each business.

Step 4: Compute a weighted average of the unlevered betas of the different businesses (from step 2) using the weights from step 3. Bottom-up Unlevered beta for your firm = Weighted average of the unlevered betas of the individual business

![](_page_89_Diagram_9.jpeg)

Step 5: Compute a levered beta (equity beta) for your firm, using the market debt to equity ratio for your firm. Levered bottom-up beta = Unlevered beta (1+ (1-t) (Debt/Equity)) If you expect the business mix of your firm to change over time, you can change the weights on a year-to-year basis.

If you expect your debt to equity ratio to change over time, the levered beta will change over time.

## *Possible Refinements*

# Why bottom-up betas?

- □ **Less Noisy:** The standard error in a bottom-up beta will be significantly lower than the standard error in a single regression beta. Roughly speaking, the standard error of a bottom-up beta estimate can be written as follows:

Std error of bottom-up beta = 
$$\frac{\text{Average Std Error across Betas}}{\sqrt{\text{Number of firms in sample}}}$$

- ❑ Updated: The bottom-up beta can be adjusted to reflect changes in the firm's business mix and financial leverage. Regression betas reflect the past.
- ❑ Don't need prices: You can estimate bottom-up betas even when you do not have historical stock prices. This is the case with initial public offerings, private businesses or divisions of companies.

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

| Business  | Unlevered Beta | D/E Ratio | Levered beta |
|-----------|----------------|-----------|--------------|
| Aerospace | 0.95           | 18.95%    | 1.07         |

- ¨ Levered Beta= Unlevered Beta ( 1 + (1- tax rate) (D/E Ratio) = 0.95 ( 1 + (1-.34) (.1895)) = 1.07 ¨ Can an unlevered beta estimated using U.S. and European aerospace companies be used to estimate the beta for a Brazilian aerospace company?
- a. Yes
- b. No What concerns would you have in making this assumption?

# Gross Debt versus Net Debt Approaches

¨ Analysts in Europe and Latin America often take the difference between debt and cash (net debt) when computing debt ratios and arrive at very different values. ¨ For Embraer, using the gross debt ratio ¤ Gross D/E Ratio for Embraer = 1953/11,042 = 18.95% ¤ Levered Beta using Gross Debt ratio = 1.07 ¨ Using the net debt ratio, we get ¤ Net Debt Ratio for Embraer = (Debt - Cash)/ Market value of Equity = (1953-2320)/ 11,042 = -3.32% ¤ Levered Beta using Net Debt Ratio = 0.95 (1 + (1-.34) (-.0332)) = 0.93 ¨ The cost of Equity using net debt levered beta for Embraer will be much lower than with the gross debt approach. The cost of capital for Embraer will even out since the debt ratio used in the cost of capital equation will now be a net debt ratio rather than a gross debt ratio.

# The Cost of Equity: A Recap

![](_page_94_Diagram_2.jpeg)

96

# Discount Rates: IV

Mopping up

# Estimating the Cost of Debt

¨ The cost of debt is the rate at which you can borrow at currently, It will reflect not only your default risk but also the level of interest rates in the market. ¨ The two most widely used approaches to estimating cost of debt are: ¤ Looking up the yield to maturity on a straight bond outstanding from the firm. The limitation of this approach is that very few firms have long term straight bonds that are liquid and widely traded ¤ Looking up the rating for the firm and estimating a default spread based upon the rating. While this approach is more robust, different bonds from the same firm can have different ratings. You have to use a median rating for the firm ¨ When in trouble (either because you have no ratings or multiple ratings for a firm), estimate a synthetic rating for your firm and the cost of debt based upon that rating.

# Estimating Synthetic Ratings

¨ The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

¨ For Embraer's interest coverage ratio, we used the interest expenses from 2003 and the average EBIT from 2001 to 2003. (The aircraft business was badly affected by 9/11 and its aftermath. In 2002 and 2003, Embraer reported significant drops in operating income)

Interest Coverage Ratio = 462.1 /129.70 = 3.56

## Interest Coverage Ratios, Ratings and Default Spreads: 2004

| If Interest Coverage Ratio is |        |            | Estimated Bond Rating | Default Spread(2004) |
|-------------------------------|--------|------------|-----------------------|----------------------|
| > 8.50                        |        | (>12.50)   | AAA                   | 0.35%                |
| 6.50 -                        | 8.50   | (9.5-12.5) | AA                    | 0.50%                |
| 5.50 -                        | 6.50   | (7.5-9.5)  | A+                    | 0.70%                |
| 4.25 -                        | 5.50   | (6-7.5)    | A                     | 0.85%                |
| 3.00 -                        | 4.25   | (4.5-6)    | A–                    | 1.00%                |
| 2.50 -                        | 3.00   | (4-4.5)    | BBB                   | 1.50%                |
| 2.25-                         | 2.50   | (3.5-4)    | BB+                   | 2.00%                |
| 2.00 -                        | 2.25   | ((3-3.5)   | BB                    | 2.50%                |
| 1.75 -                        | 2.00   | (2.5-3)    | B+                    | 3.25%                |
| 1.50 -                        | 1.75   | (2-2.5)    | B                     | 4.00%                |
| 1.25 -                        | 1.50   | (1.5-2)    | B –                   | 6.00%                |
| 0.80 -                        | 1.25   | (1.25-1.5) | CCC                   | 8.00%                |
| 0.65 -                        | 0.80   | (0.8-1.25) | CC                    | 10.00%               |
| 0.20 -                        | 0.65   | (0.5-0.8)  | C                     | 12.00%               |
| < 0.20                        | (<0.5) | D          |                       | 20.00%               |

# Cost of Debt computations

¨ Based on the interest coverage ratio of 3.56, the synthetic rating for Embraer is A-, giving it a default spread of 1.00% ¨ Companies in countries with low bond ratings and high default risk might bear the burden of country default risk, especially if they are smaller or have all of their revenues within the country. ¨ If I assume that Embraer bears all of the country risk burden, I would add on the country default spread for Brazil in 2004 of 6.01%. ¨ Larger companies that derive a significant portion of their revenues in global markets may be less exposed to country default risk. I am going to add only two thirds of the Brazilian country risk (based upon traded bond spreads of other large Brazilian companies in 2004)

Cost of debt

= Riskfree rate + 2/3(Brazil country default spread) + Company default spread =4.29% + 2/3 (6.01%)+ 1.00% = 9.29%

# Synthetic Ratings: Some Caveats

¨ The relationship between interest coverage ratios and ratings, developed using US companies, tends to travel well, as long as we are analyzing large manufacturing firms in markets with interest rates close to the US interest rate ¨ They are more problematic when looking at smaller companies in markets with higher interest rates than the US. One way to adjust for this difference is modify the interest coverage ratio table to reflect interest rate differences (For instances, if interest rates in an emerging market are twice as high as rates in the US, halve the interest coverage ratio).

# Default Spreads: Change is a constant

![](_page_101_Figure_2.jpeg)

| Date                  | AAA          | AA           | A            | BBB          | BB           | B            | 0            |
|-----------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| 1/1/22                | 0.51%        | 0.62%        | 0.78%        | 1.62%        | 2.11%        | 3.51%        | 6.78%        |
| 2/1/22                | 0.62%        | 0.70%        | 0.87%        | 1.33%        | 2.55%        | 3.83%        | 7.22%        |
| 3/1/22                | 0.70%        | 0.83%        | 1.07%        | 1.64%        | 2.86%        | 4.23%        | 7.82%        |
| 4/1/22                | 0.58%        | 0.73%        | 0.97%        | 1.47%        | 2.33%        | 3.73%        | 7.27%        |
| 5/1/22                | 0.70%        | 0.87%        | 1.17%        | 1.72%        | 2.90%        | 4.30%        | 8.69%        |
| 6/1/22                | 0.60%        | 0.81%        | 1.11%        | 1.70%        | 2.67%        | 4.56%        | 9.70%        |
| 7/1/22                | 0.71%        | 0.97%        | 1.33%        | 2.05%        | 4.19%        | 6.61%        | 12.05%       |
| 8/1/22                | 0.60%        | 0.86%        | 1.21%        | 1.88%        | 3.15%        | 5.35%        | 10.97%       |
| 9/1/22                | 0.65%        | 0.86%        | 1.21%        | 1.91%        | 3.47%        | 5.34%        | 11.89%       |
| 9/23/22               | 0.65%        | 0.86%        | 1.23%        | 1.87%        | 3.46%        | 5.36%        | 12.25%       |
| <b>Change in 2022</b> | <b>0.14%</b> | <b>0.24%</b> | <b>0.45%</b> | <b>0.66%</b> | <b>1.35%</b> | <b>1.85%</b> | <b>5.47%</b> |

# Default Spreads – January 2024

![](_page_102_Figure_1.jpeg)

# Subsidized Debt: What should we do?

- ¨ Assume that the Brazilian government lends money to Embraer at a subsidized interest rate (say 6% in dollar terms). In computing the cost of capital to value Embraer, should be we use the cost of debt based upon default risk or the subsidized cost of debt?
- a. The subsidized cost of debt (6%). That is what the company is paying.
- b. The fair cost of debt (9.25%). That is what the company should require its projects to cover.
- c. A number in the middle.

## Weights for the Cost of Capital Computation

- ¨ In computing the cost of capital for a publicly traded firm, the general rule for computing weights for debt and equity is that you use market value weights (and not book value weights). Why?
  - a. Because the market is usually right
  - b. Because market values are easy to obtain
  - c. Because book values of debt and equity are meaningless
  - d. None of the above

## Estimating Cost of Capital: Embraer in 2004

## ¨ Equity

¤ Cost of Equity = 4.29% + 1.07 (4%) + 0.27 (7.89%) = 10.70% ¤ Market Value of Equity =11,042 million BR (\$ 3,781 million)

## ¨ Debt

¤ Cost of debt = 4.29% + 4.00% +1.00%= 9.29%

¤ Market Value of Debt = 2,083 million BR (\$713 million)

¨ Cost of Capital = 10.70 % (.84) + 9.29% (1- .34) (0.16)) = 9.97%

¤ The book value of equity at Embraer is 3,350 million BR.

¤ The book value of debt at Embraer is 1,953 million BR; Interest expense is 222 mil BR; Average maturity of debt = 4 years

¤ Estimated market value of debt = 222 million (PV of annuity, 4 years, 9.29%) + \$1,953 million/1.09294 = 2,083 million BR

## If you had to do it….Converting a Dollar Cost of Capital to a Nominal Real Cost of Capital

¨ Approach 1: Use a BR riskfree rate in all of the calculations above. For instance, if the BR riskfree rate was 12%, the cost of capital would be computed as follows: ¤ Cost of Equity = 12% + 1.07(4%) + 0.27 (7. 89%) = 18.41% ¤ Cost of Debt = 12% + 1% = 13% ¤ (This assumes the riskfree rate has no country risk premium embedded in it.) ¨ Approach 2: Use the differential inflation rate to estimate the cost of capital. For instance, if the inflation rate in BR is 8% and the inflation rate in the U.S. is 2%

$$\begin{aligned} \text{Cost of capital} &= (1 + \text{Cost of Capital}_{\$}) \left[ \frac{1 + \text{Inflation}_{\text{BR}}}{1 + \text{Inflation}_{\$}} \right] \\ &= 1.0997 (1.08/1.02) - 1 = 0.1644 \text{ or } 16.44\% \end{aligned}$$

# Dealing with Hybrids and Preferred Stock

¨ When dealing with hybrids (convertible bonds, for instance), break the security down into debt and equity and allocate the amounts accordingly. Thus, if a firm has \$ 125 million in convertible debt outstanding, break the \$125 million into straight debt and conversion option components. The conversion option is equity. ¨ When dealing with preferred stock, it is better to keep it as a separate component. The cost of preferred stock is the preferred dividend yield. (As a rule of thumb, if the preferred stock is less than 5% of the outstanding market value of the firm, lumping it in with debt will make no significant impact on your valuation).

# Decomposing a convertible bond…

¨ Assume that the firm that you are analyzing has \$125 million in face value of convertible debt with a stated interest rate of 4%, a 10 year maturity and a market value of \$140 million. If the firm has a bond rating of A and the interest rate on Arated straight bond is 8%, you can break down the value of the convertible bond into straight debt and equity portions. ¤ Straight debt = (4% of \$125 million) (PV of annuity, 10 years, 8%) + 125 million/1.0810 = \$91.45 million ¤ Equity portion = \$140 million - \$91.45 million = \$48.55 million ¨ The debt portion (\$91.45 million) gets added to debt and the option portion (\$48.55 million) gets added to the market capitalization to get to the debt and equity weights in the cost of capital.

# Recapping the Cost of Capital

![](_page_109_Diagram_2.jpeg)

# Estimating Cash Flows

Cash is king...

# Free Cash Flow: FCFE and FCFF

112

## Free Cash Flow to Equity

![](_page_111_Diagram_29.jpeg)

## Free Cash Flow to Firm

![](_page_111_Diagram_31.jpeg)

# Steps in Cash Flow Estimation

¨ Estimate the current earnings of the firm ¤ If looking at cash flows to equity, look at earnings after interest expenses - i.e. net income ¤ If looking at cash flows to the firm, look at operating earnings after taxes ¨ Consider how much the firm invested to create future growth ¤ If the investment is not expensed, it will be categorized as capital expenditures. To the extent that depreciation provides a cash flow, it will cover some of these expenditures. ¤ Increasing working capital needs are also investments for future growth ¨ If looking at cash flows to equity, consider the cash flows from net debt issues (debt issued - debt repaid)

# Measuring Free Cash Flow to the Firm: Three pathways to the same end game

114

$$\begin{array}{lll} \text{EBIT (1 - tax rate)} & \text{minus} & (\text{Cap Ex - Depreciation}) \\ & & + \text{Change in non-cash Working capial} & = & \text{FCFF} \\ \\ \text{EBIT (1 - tax rate)} & \text{minus} & \text{Reinvestment} & = & \text{FCFF} \\ \\ \text{EBIT (1 - tax rate)} & \text{X} & (1 - \text{Reinvestment Rate}) & = & \text{FCFF} \end{array}$$

Where are the tax savings from interest expenses?

# Measuring Free Cash Flow to Equity: Alternative Pathways

| Net Income                                                                                              | minus | (Capital Ex - Depreciation) +<br>Change in non-cash<br>Working Capital | Plus | (New Debt Issued<br>- Debt Repaid) | = | FCFE |
|---------------------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------|------|------------------------------------|---|------|
|                                                                                                         |       |                                                                        |      |                                    |   |      |
| Net Income                                                                                              | minus | Reinvestment                                                           | Plus | Net Debt<br>Cashflow               | = | FCFE |
| Net Income                                                                                              | X     | (1 - Equity Reinvestment Rate)                                         |      |                                    | = | FCFE |
| Equity Reinvestment Rate = $\frac{(\text{Reinvestment} - \text{Net Debt Cashflow})}{\text{Net Income}}$ |       |                                                                        |      |                                    |   |      |

# Microsoft in 2021: FCFE and FCFF

![](_page_115_Figure_8.jpeg)

![](_page_115_Figure_9.jpeg)

117

# Cash Flows I

Accounting Earnings, Flawed but Important

# From Reported to Actual Earnings

![](_page_117_Diagram_2.jpeg)

# 1. Updating Earnings

¨ When valuing companies, we often depend upon financial statements for inputs on earnings and assets. Annual reports are often outdated and can be updated by using- ¤ Trailing 12-month data, constructed from quarterly earnings reports. ¤ Informal and unofficial news reports, if quarterly reports are unavailable. ¨ Updating makes the most difference for smaller and more volatile firms, as well as for firms that have undergone significant restructuring. ¨ Time saver: To get a trailing 12-month number, all you need is one 10K and one 10Q (example third quarter). For example, to get trailing revenues from a third quarter 10Q: ¤ Trailing 12-month Revenue = Revenues (in last 10K) - Revenues from first 3 quarters of last year + Revenues from first 3 quarters of this year.

# 2. Correcting Accounting Earnings

¨ Make sure that there are no financial expenses mixed in with operating expenses ¤ Financial expense: Any commitment that is tax deductible that you have to meet no matter what your operating results: Failure to meet it leads to loss of control of the business. ¤ Until 2019, accounting convention treated operating leases as operating expenses, skewing income statements & balance sheets. ¨ Make sure that there are no capital expenses mixed in with the operating expenses ¤ Capital expense: Any expense that is expected to generate benefits over multiple periods. ¤ There are a shole host of expenses (like R&D) that meet this description that accountants treat as operating expenses.

# A. The Magnitude of Operating Leases

| Highest                             |                         | Lowest                   |                         |
|-------------------------------------|-------------------------|--------------------------|-------------------------|
| Industry Name                       | Lease Expense/<br>Sales | Industry Name            | Lease Expense/<br>Sales |
| Air Transport                       | 12.69%                  | Homebuilding             | 0.24%                   |
| Trucking                            | 7.33%                   | Green & Renewable Energy | 0.26%                   |
| Restaurant/Dining                   | 5.95%                   | Insurance (Life)         | 0.34%                   |
| Telecom (Wireless)                  | 5.75%                   | Steel                    | 0.39%                   |
| Apparel                             | 5.48%                   | Auto & Truck             | 0.41%                   |
| Real Estate (Operations & Services) | 5.41%                   | Food Wholesalers         | 0.45%                   |
| Retail (Special Lines)              | 4.86%                   | Insurance (Prop/Cas.)    | 0.46%                   |

# Dealing with Operating Lease Expenses

¨ Since they give rise to contractual commitments, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital: ¨ **Debt Value of Operating Leases** = Present value of Operating Lease Commitments at the pre-tax cost of debt ¨ **Lease Asset**: When you convert operating leases into debt, you also create an asset to counter it of exactly the same value. ¨ **Adjusted Operating Earnings** = Operating Earnings + Operating Lease Expenses - Depreciation on Leased Asset

As an approximation, this works:

¤ Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

# Operating Leases at The Gap in 2003

¨ The Gap has conventional debt of about \$ 1.97 billion on its balance sheet and its pre-tax cost of debt is about 6%. Its operating lease payments in the 2003 were \$978 million and its commitments for the future are below:

| Year | Commitment (millions) | Present Value (at 6%) |
|------|-----------------------|-----------------------|
| 1    | \$899.00              | \$848.11              |
| 2    | \$846.00              | \$752.94              |
| 3    | \$738.00              | \$619.64              |
| 4    | \$598.00              | \$473.67              |
| 5    | \$477.00              | \$356.44              |
| 6&7  | \$982.50 each year    | \$1,346.04            |

¨ Debt Value of leases = \$4,396.85 (Also value of leased asset) ¨ Debt outstanding at The Gap = \$1,970 m + \$4,397 m = \$6,367 m ¨ Adjusted Operating Income = Stated OI + OL exp this year - Deprec' n = \$1,012 m + 978 m - 4397 m /7 = \$1,362 million (7-year life for assets) ¨ Approximate OI = \$1,012 m + \$ 4397 m (.06) = \$1,276 m

## The Collateral Effects of Treating Operating Leases as Debt

|   | Conventional!Accounting | Operating!Leases!Treated!as!Debt |
|---|-------------------------|----------------------------------|
| 0 | Op&Leases&&&&&&=&&&&978 |                                  |
|   |                         | 0 Deprecn:&OL=&&&&&&628          |

## Miscategorized Financing Expenses as Operating Expenses

### Income Statement

**To correct the accounting mistake**

**To correct operating (net) income:** Stated Operating income + Current year's Lease expense - Amortization of Lease Asset

**To correct financial expenses:** Stated interest expense + imputed interest expense on lease debt

Amortize the lease asset over the commitment lifetime.

**To correct debt & assets:** Take the present value of future financing commitments, using the cost of debt as your discount and show as both an asset (lease asset) and debt (lease debt).

|            | Item                    | Explanation                                                                                                    |
|------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Start with | Revenues                | Accountant's estimate of the revenues/sales generated by any transactions made the business during the period. |
| Net out    | Cost of Goods Sold      | Estimated costs that are directly associated with producing the product/service sold by the company.           |
| To get     | <b>Gross Profit</b>     | Unit profitability, before covering other indirect costs and financial expenses                                |
| Net out    | Operating Expenses      | Include all expenses associated with operations this year, with no benefits spilling over into future years.   |
| To get     | <b>Operating Profit</b> | Profitability of business/ operations                                                                          |
| Net out    | Financial Expenses      | Expenses associated with non-equity financing (debt, for instance)                                             |
| Add in     | Financial Income        | Income earned on cash balance and on financial investments (in companies and securities)                       |
| To get     | <b>Pretax Profit</b>    | Income to equity investors, prior to taxes                                                                     |
| Net out    | Taxes                   | Taxes, based upon taxable income. (May not equate to cash taxes paid)                                          |
| To get     | <b>Net Profit</b>       | Income to equity investors, after taxes                                                                        |

**When accountants treat a financing expense (like lease payment) as an operating expense.**

**Operating income will be misstated, with financing expenses showing up as operating expenses. Net income will be unaffected.**

### Balance Sheet

| Assets                                     |                   | Liabilities         |                             |
|--------------------------------------------|-------------------|---------------------|-----------------------------|
| Long Lived Physical Assets                 | Fixed Assets      | Current Liabilities | Short term obligations      |
| Short Lived Assets                         | Current Assets    | Debt                | Long term debt              |
| Investments in Securities & other business | Financial Assets  | Other Liabilities   | Other long term obligations |
| Assets which are not physical              | Intangible Assets | Equity              | Shareholders' Equity        |

**Book debt and assets will be understated, as you miss the present value of commitments associated with the financing on both sides of the balance sheet.**

### Effects on Ratios/Statistics

| Ratio/Statistic            | Before correction                                                    | After correction                                                                            | Effect of correction |
|----------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------|
| Operating Margin           | Operating income/Sales                                               | Corrected Operating income/Sales                                                            | Increase             |
| Net Margin                 | Net Income/Sales                                                     | Net Income/Sales                                                                            | No change            |
| Return on invested capital | Operating income/ (Book value of equity + Book value of debt - cash) | Corrected Operating income/ (Book value of equity + Book value of debt + Lease debt - cash) | Decrease             |
| Return on equity           | Net Income/Book Equity                                               | Net Income/ Book Equity                                                                     | No change            |
| Debt Ratio (Book)          | Book Debt/(Book Debt + Book Equity)                                  | (Book Debt + Lease Debt)/ (Book Debt + Lease Debt + Equity)                                 | Increase             |
| Debt Ratio (Market)        | Mkt Debt/(Mkt Debt + Mkt Equity)                                     | (Mkt Debt + Lease Debt)/ (Mkt Debt + Lease Debt + Mkt Equity)                               | Increase             |

# Accounting comes to its senses on operating leases

¨ In 2019, both IFRS and GAAP made a major shift on operating leases, requiring companies to capitalize leases and show the resulting debt (and counter asset) on the balance sheets. ¨ That said, the accounting rules for capitalizing leases are far more complex than the simple calculations that I have used, for two reasons: ¤ Accounting has to balance its desire to do the right thing with maintaining some connection to its legacy rules. ¤ Companies have lobbied to modify rules in their sectors to cushion the impact.

# Checking on Accountants.... My lease estimate vs Accountants' Estimate

| Region                 | My Estimate     | Accounting      | Accounting as % of my estimate |
|------------------------|-----------------|-----------------|--------------------------------|
| Australia, NZ & Canada | \$ 13,578.86    | \$ 8,412.39     | 61.95%                         |
| United States          | \$ 1,152,869.85 | \$ 947,989.30   | 82.23%                         |
| Europe                 | \$ 52,172.26    | \$ 24,336.94    | 46.65%                         |
| Emerging Markets       | \$ 109,415.47   | \$ 18,426.24    | 16.84%                         |
| Japan                  | \$ 156,071.83   | \$ 1,719.90     | 1.10%                          |
| Global                 | \$ 1,484,108.27 | \$ 1,000,884.77 | 67.44%                         |

# B. The Magnitude of R&D Expenses

| Highest R&D spenders       |                            |                             | Lowest R&D spenders               |                            |                             |  |
|----------------------------|----------------------------|-----------------------------|-----------------------------------|----------------------------|-----------------------------|--|
| Industry Name              | R&D - LTM (In \$ millions) | Current R&D as % of Revenue | Industry Name                     | R&D - LTM (In \$ millions) | Current R&D as % of Revenue |  |
| Drugs (Biotechnology)      | \$ 75,091.63               | 39.62%                      | Beverage (Alcoholic)              | \$                         | 0.00%                       |  |
| Drugs (Pharmaceutical)     | \$ 80,658.49               | 23.08%                      | Food Wholesalers                  | \$ 0.88                    | 0.00%                       |  |
| Software (Internet)        | \$ 4,177.58                | 18.98%                      | Homebuilding                      | -                          | 0.00%                       |  |
| Semiconductor              | \$ 50,321.60               | 17.40%                      | Hospitals/Healthcare Facilities   | \$ 9.72                    | 0.00%                       |  |
| Software (System & Applica | \$ 72,267.59               | 16.70%                      | Insurance (Life)                  | -                          | 0.00%                       |  |
| Software (Entertainment)   | \$ 58,245.69               | 15.15%                      | Insurance (Prop/Cas.)             | -                          | 0.00%                       |  |
| Telecom. Equipment         | \$ 13,613.55               | 13.27%                      | Oil/Gas Distribution              | -                          | 0.00%                       |  |
| Retail (Online)            | \$ 54,214.00               | 10.09%                      | Real Estate (Development)         | \$ -                       | 0.00%                       |  |
| Semiconductor Equip        | \$ 6,707.74                | 9.38%                       | Real Estate (General/Diversified) | -                          | 0.00%                       |  |
| Healthcare Products        | \$ 14,934.42               | 8.01%                       | Restaurant/Dining                 | \$ 8.82                    | 0.00%                       |  |

## R&D Expenses: Operating or Capital Expenses

¨ Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. ¨ To capitalize R&D, ¤ Specify an amortizable life for R&D (2 - 10 years) ¤ Collect past R&D expenses for as long as the amortizable life ¤ Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

# Capitalizing R&D Expenses: SAP

¨ R & D was assumed to have a 5-year life.

| Year    | R&D Expense |      | Unamortized | Amortization this year |
|---------|-------------|------|-------------|------------------------|
| Current | 1020.02     | 1.00 | 1020.02     |                        |
| -1      | 993.99      | 0.80 | 795.19      | € 198.80               |
| -2      | 909.39      | 0.60 | 545.63      | € 181.88               |
| -3      | 898.25      | 0.40 | 359.30      | € 179.65               |
| -4      | 969.38      | 0.20 | 193.88      | € 193.88               |
| -5      | 744.67      | 0.00 | 0.00        | € 148.93               |

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

## Miscategorized Capital Expenses as Operating Expenses

### Income Statement

*To correct the accounting mistake*

**To correct operating (net) income:** Stated Operating (Net) income + Current year's R&D expense - Amortization of R&D Asset

Amortize the R&D asset over amortizable life.

**To correct debt & assets:** Capitalize past R&D expenses and incorporate that amount into assets (as an R&D asset) and increase book equity by an equal amount.

|            | Item                    | Explanation                                                                                                    |
|------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| Start with | Revenues                | Accountant's estimate of the revenues/sales generated by any transactions made the business during the period. |
| Net out    | Cost of Goods Sold      | Estimated costs that are directly associated with producing the product/service sold by the company.           |
| To get     | <b>Gross Profit</b>     | Unit profitability, before covering other indirect costs and financial expenses                                |
| Net out    | Operating Expenses      | Include all expenses associated with operations this year, with no benefits spilling over into future years.   |
| To get     | <b>Operating Profit</b> | Profitability of business/ operations                                                                          |
| Net out    | Financial Expenses      | Expenses associated with non-equity financing (debt, for instance)                                             |
| Add in     | Financial Income        | Income earned on cash balance and on financial investments (in companies and securities)                       |
| To get     | <b>Pretax Profit</b>    | Income to equity investors, prior to taxes                                                                     |
| Net out    | Taxes                   | Taxes, based upon taxable income. (May not equate to cash taxes paid)                                          |
| To get     | <b>Net Profit</b>       | Income to equity investors, after taxes                                                                        |

*When accountants treat a capital expenditure (like R&D) as an operating expense.*

**Operating income and net income will be misstated and will be too low (high) for companies with growing (declining) R&D expenses.**

#### Balance Sheet

| Assets                                     |                   | Liabilities         |                             |
|--------------------------------------------|-------------------|---------------------|-----------------------------|
| Long Lived Physical Assets                 | Fixed Assets      | Current Liabilities | Short term obligations      |
| Short Lived Assets                         | Current Assets    | Debt                | Long term debt              |
| Investments in Securities & other business | Financial Assets  | Other Liabilities   | Other long term obligations |
| Assets which are not physical              | Intangible Assets | Equity              | Shareholders' Equity        |

**Book equity and assets will be understated, as you miss the capitalized effects of past R&D expenses in both items.**

#### Effects on Ratios/Statistics

| Ratio/Statistic            | Before correction                                                    | After correction                                                                           | Effect of correction                                        |
|----------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Operating Margin           | Operating income/Sales                                               | Corrected Operating income/Sales                                                           | Increase (decrease) for companies with rising R&D expenses. |
| Net Margin                 | Net Income/Sales                                                     | Corrected Net Income/Sales                                                                 | Increase (decrease) for companies with rising R&D expenses. |
| Return on invested capital | Operating income/ (Book value of equity + Book value of debt - cash) | Corrected Operating income/ (Book value of equity + R&D asset + Book value of debt - cash) | Decrease                                                    |
| Return on equity           | Net Income/Book Equity                                               | Corrected Net Income/ (Book Equity + R&D asset)                                            | Decrease                                                    |
| Debt Ratio (Book)          | Book Debt/(Book Debt + Book Equity)                                  | Book Debt / (Book Debt + Equity + R&D asset)                                               | Decrease                                                    |
| Debt Ratio (Market)        | Mkt Debt/(Mkt Debt + Mkt Equity)                                     | Mkt Debt/(Mkt Debt + Mkt Equity)                                                           | No change (The market value already incorporates R&D)       |

# 3. One-Time and Non-recurring Charges

- ¨ Assume that you are valuing a firm that is reporting a loss of \$ 500 million, due to a one-time charge of \$ 1 billion. What is the earnings you would use in your valuation?
  - a. A loss of \$ 500 million
- b. A profit of \$ 500 million ¨ Would your answer be any different if the firm had reported one-time losses like these once every five years?
  - a. Yes
  - b. No

# 4. Accounting Malfeasance….

¨ Though all firms may be governed by the same accounting standards, the fidelity that they show to these standards can vary. More aggressive firms will show higher earnings than more conservative firms. ¨ While you will not be able to catch outright fraud, you should look for warning signals in financial statements and correct for them: ¤ Income from unspecified sources - holdings in other businesses that are not revealed or from special purpose entities. ¤ Income from asset sales or financial transactions (for a non-financial firm) ¤ Sudden changes in standard expense items - a big drop in S,G &A or R&D expenses as a percent of revenues, for instance. ¤ Frequent accounting restatements ¤ Accrual earnings that run ahead of cash earnings consistently ¤ Big differences between tax income and reported income

## 5. Dealing with Negative or Abnormally Low Earnings

|                 | Reason for losses/low earnings                   | Valuation Response                                                                                                   |
|-----------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Quick fixes     | One-time or extraordinary charge                 | Add back the one-time expense to get corrected earnings                                                              |
| Quick fixes     | Macro factor (commodity price drop or recession) | Use earnings across the commodity or economic cycle as normalized earnings.                                          |
| Long term fixes | Young company working on business model          | Estimate the profit margin that mature companies in the business earn and target that margin in the long term.       |
| Long term fixes | Structural problems at company                   | Use an industry average margin as a target and move towards that margin over time, as structural problems are fixed. |

136

# Cash Flows II

## Taxes and Reinvestment

# 1. What tax rate?

- ¨ The tax rate that you should use in computing the aftertax operating income should be
  - a. The effective tax rate in the financial statements (taxes paid/Taxable income)
  - b. The tax rate based upon taxes paid and EBIT (taxes paid/EBIT)
  - c. The marginal tax rate for the country in which the company operates
  - d. The weighted average marginal tax rate across the countries in which the company operates
  - e. None of the above
  - f. Any of the above, as long as you compute your after-tax cost of debt using the same tax rate.

# The Right Tax Rate to Use

¨ The free cash flow to the firm starts with after-tax operating income, where: ¨ After-tax Operating Income = Operating Income (1- tax rate) ¨ In computing free cash flow to the firm, the choice really is between the effective and the marginal tax rate. ¨ By using the marginal tax rate, we tend to understate the after-tax operating income in the earlier years, but the after-tax tax operating income is more accurate in later years. ¨ By using the effective tax rate, we tend to overstate the after-tax operating income in the later years, as effective tax rates move toward the marginal tax rate. ¨ You can have your cake and eat it too, by starting with the effective tax rate, and adjusting towards the marginal tax rate over time.

# A Tax Rate for a Money Losing Firm

- □ Assume that you are trying to estimate the after-tax operating income for a firm **with \$ 1 billion in net operating losses** carried forward.
- □ This firm is **expected to have operating income of \$ 500 million each year for the next 3 years**, and the marginal tax rate on income for all firms that make money is 40%. Estimate the after-tax operating income each year for the next 3 years.

|            | Year 1 | Year 2 | Year 3 |
|------------|--------|--------|--------|
| EBIT       | 500    | 500    | 500    |
| Taxes      |        |        |        |
| EBIT (1-t) |        |        |        |
| Tax rate   |        |        |        |

# 2. Net Capital Expenditures

¨ Net capital expenditures represent the difference between capital expenditures and depreciation.

Net Cap Ex = Capital Expenditures - Depreciation

Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures.

¨ In general, the net capital expenditures will be a function of how fast a firm is growing or expecting to grow. ¨ High growth firms will usually have much higher net capital expenditures than low growth firms. ¨ Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

# Capital expenditures should include

- □ Research and development expenses, once they have been re-categorized as capital expenses. The adjusted net cap ex will be
  - ■ Adjusted Net Capital Expenditures = Net Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset
- □ Acquisitions of other firms, since these are like capital expenditures. The adjusted net cap ex will be
  - ■ Adjusted Net Cap Ex = Net Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions
- □ Two caveats:
  1. 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
  2. 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

# Cisco's Acquisitions: 1999

| Acquired          | Method of Acquisition | Price Paid |
|-------------------|-----------------------|------------|
| GeoTel            | Pooling               | \$1,344    |
| Fibex             | Pooling               | \$318      |
| Sentient          | Pooling               | \$103      |
| American Internet | Purchase              | \$58       |
| Summa Four        | Purchase              | \$129      |
| Clarity Wireless  | Purchase              | \$153      |
| Selsius Systems   | Purchase              | \$134      |
| PipeLinks         | Purchase              | \$118      |
| Amteva Tech       | Purchase              | \$159      |

# Cisco's Net Capital Expenditures in 1999

Cap Expenditures (from statement of CF) = \$ 584 mil

- Depreciation (from statement of CF) = \$ 486 mil

Net Cap Ex (from statement of CF) = \$ 98 mil

+ R & D expense = \$ 1,594 mil

- Amortization of R&D = \$ 485 mil

+ Acquisitions = \$ 2,516 mil

Adjusted Net Capital Expenditures = \$3,723 mil

¨ (Amortization was included in the depreciation number)

# 3. Working Capital Investments

¨ **Accounting definition**: Working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year). ¨ **Valuation definition**: A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable).

# Working Capital: General Propositions

- 1. Working Capital Detail: While some analysts break down working capital into detail, it is a pointless exercise unless you feel that you can bring some specific information that lets you forecast the details.
- 2. Working Capital Volatility: Changes in non-cash working capital from year to year tend to be volatile. It is better to either estimate the change based on working capital as a percent of sales, while keeping an eye on industry averages.
- 3. Negative Working Capital: Some firms have negative non-cash working capital. Assuming that this will continue into the future will generate positive cash flows for the firm and will get more positive as growth increases.

146

# Cash Flows III

From the firm to equity

# Dividends and Cash Flows to Equity

¨ In the strictest sense, the only cash flow from an equity investment in a publicly traded firm is the **dividend that will be paid on the stock**. ¨ Actual dividends, however, are set by the managers of the firm and may be much lower than **the potential dividends (that could have been paid out)** ¤ managers are conservative and try to smooth out dividends ¤ managers like to hold on to cash to meet unforeseen future contingencies and investment opportunities ¨ When actual dividends are less (more) than potential dividends, using a model that focuses only on dividends will under (over) state the true value of the equity in a firm.

# Measuring Potential Dividends

¨ Some analysts assume that the earnings of a firm represent its potential dividends. This cannot be true for several reasons: ¤ Earnings are not cash flows, since there are both non-cash revenues and expenses in the earnings calculation ¤ Even if earnings were cash flows, a firm that paid its earnings out as dividends would not be investing in new assets and thus could not grow ¤ Valuation models, where earnings are discounted back to the present, will over estimate the value of the equity in the firm ¨ The potential dividends of a firm are the cash flows left over after the firm has made any "investments" it needs to make to create future growth and net debt repayments (debt repayments - new debt issues) ¤ The common categorization of capital expenditures into discretionary and non-discretionary loses its basis when there is future growth built into the valuation.

# Estimating Cash Flows: FCFE

¨ Cash flows to Equity for a Levered Firm

Net Income

- (Capital Expenditures Depreciation)
- Changes in non-cash Working Capital + (New Debt Issues – Debt Repaid) = Free Cash flow to Equity

¨ Cash flows to equity represent residual cash flows for equity investors, i.e., cash flows left over after every conceivable need has been met. ¨ That cash flow can be paid out without damaging the operating business of the company and its growth potential. It is thus a potential dividend.

# FCFE from the statement of cash flows

- ¨ The statement of cash flows can be used to back into a FCFE, if you are willing to navigate your way through it and not trust it fully. ¨ FCFE = Cashflow from Operations
  - Capital Expenditures (from the cash flow from investments)
  - Cash Acquisitions (from the cash flow from investments)
- (Debt Repaid Debt Issued) (from financing cash flows) = FCFE ¨ Alternatively, you can also do the following: ¤ FCFE – Dividends + Stock Buybacks – Stock Issuances + Change in Cash Balance

# FCFE across the life cycle

![](_page_150_Figure_2.jpeg)

# FCFE over time: Tesla

Tesla: Net Income and FCFE - 2006 to 2021

![](_page_151_Figure_8.jpeg)

# Dividends versus FCFE: Across the globe

| Sub Group                 | Number of firms | Net Income     | FCFE           | Dividends   | Buybacks    | % from Buybacks | Dividends + Buybacks |
|---------------------------|-----------------|----------------|----------------|-------------|-------------|-----------------|----------------------|
| Africa and Middle East    | 2,423           | \$307,736.16   | \$230,376.04   | \$178,945   | \$13,131    | 6.84%           | \$192,076            |
| Australia & NZ            | 1,798           | \$82,148.86    | \$22,464.54    | \$65,050    | \$9,704     | 12.98%          | \$74,754             |
| Canada                    | 2,791           | \$129,021.51   | -\$11,327.54   | \$74,629    | \$47,476    | 38.88%          | \$122,105            |
| China                     | 7,504           | \$798,823.69   | -\$75,419.80   | \$504,087   | \$72,049    | 12.51%          | \$576,136            |
| EU & Environs             | 5,925           | \$967,493.21   | \$596,696.13   | \$424,707   | \$161,188   | 27.51%          | \$585,896            |
| Eastern Europe & Russia   | 325             | \$13,064.78    | \$7,204.94     | \$6,426     | \$410       | 6.00%           | \$6,836              |
| India                     | 4,446           | \$163,984.70   | \$111,933.10   | \$50,643    | \$6,095     | 10.74%          | \$56,738             |
| Japan                     | 4,020           | \$371,873.39   | \$16,137.31    | \$115,135   | \$63,865    | 35.68%          | \$178,999            |
| Latin America & Caribbean | 984             | \$135,544.59   | \$33,386.50    | \$67,145    | \$16,117    | 19.36%          | \$83,262             |
| Small Asia                | 9,876           | \$331,541.42   | -\$42,424.57   | \$188,287   | \$15,484    | 7.60%           | \$203,772            |
| UK                        | 1,125           | \$245,010.10   | \$178,627.76   | \$114,706   | \$61,037    | 34.73%          | \$175,742            |
| United States             | 6,481           | \$1,785,480.61 | \$563,221.99   | \$700,711   | \$928,104   | 56.98%          | \$1,628,816          |
| Global                    | 47,698          | \$5,331,723.03 | \$1,630,876.38 | \$2,490,471 | \$1,394,660 | 35.90%          | \$3,885,131          |

# Estimating FCFE when Leverage is Stable

## Net Income

- (1- DR) (Capital Expenditures Depreciation)
- (1- DR) Working Capital Needs = Free Cash flow to Equity

DR = Debt/Capital Ratio

For this firm,

¤ Proceeds from new debt issues = Principal Repayments + (Capital Expenditures - Depreciation + Working Capital Needs) ¨In computing FCFE, the book value debt to capital ratio should be used when looking back in time but can be replaced with the market value debt to capital ratio, looking forward.

# Estimating FCFE: Disney

¨ Net Income=\$ 1533 Million ¨ Capital spending = \$ 1,746 Million ¨ Depreciation per Share = \$ 1,134 Million ¨ Increase in non-cash working capital = \$ 477 Million ¨ Debt to Capital Ratio (DR) = 23.83% ¨ Estimating FCFE (1997):

| Net Income                  | \$1,533 Mil                     |
|-----------------------------|---------------------------------|
| (Cap. Exp Depr)*(1-DR)      | \$465.90 [(1746-1134)(1-.2383)] |
| Chg. Working Capital*(1-DR) | \$363.33 [477(1-.2383)]         |
| = Free CF to Equity         | \$ 704 Million                  |

# FCFE and Leverage: Is this a free lunch?

Debt Ratio and FCFE: Disney

![](_page_155_Figure_3.jpeg)

# FCFE and Leverage: The Other Shoe Drops

Debt Ratio and Beta

![](_page_156_Figure_3.jpeg)

# Leverage, FCFE and Value

- ¨ In a discounted cash flow model, increasing the debt/equity ratio will generally increase the expected free cash flows to equity investors over future time periods and also the cost of equity applied in discounting these cash flows. Which of the following statements relating leverage to value would you subscribe to?
  - a. Increasing leverage will increase value because the cash flow effects will dominate the discount rate effects
  - b. Increasing leverage will decrease value because the risk effect will be greater than the cash flow effects
  - c. Increasing leverage will not affect value because the risk effect will exactly offset the cash flow effect
  - d. Any of the above, depending upon what company you are looking at and where it is in terms of current leverage

Growth can be good, bad or neutral…

# **<sup>159</sup>** Estimating Growth

# The Value of Growth

¨ When valuing a company, it is easy to get caught up in the details of estimating growth and start viewing growth as a "good", i.e., that higher growth translates into higher value. ¨ Growth, though, is a double-edged sword. ¤ The good side of growth is that it pushes up revenues and operating income, perhaps at different rates (depending on how margins evolve over time). ¤ The bad side of growth is that you have to set aside money to reinvest to create that growth. ¤ The net effect of growth is whether the good outweighs the bad.

# Ways of Estimating Growth in Earnings

¨ Look at the past ¤ The historical growth in earnings per share is usually a good starting point for growth estimation ¨ Look at what others are estimating ¤ Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are. ¨ Look at fundamentals ¤ With stable margins, operating income growth can be tied to how much a firm reinvests, and the returns it earns. ¤ With changing margins, you have to start with revenue growth, forecast margins and estimate reinvestment.

162

# Growth I

## Historical Growth

# Historical Growth

¨ Historical growth rates can be estimated in a number of different ways ¤ Arithmetic versus Geometric Averages ¤ Simple versus Regression Models ¨ Historical growth rates can be sensitive to ¤ The period used in the estimation (starting and ending points) ¤ The metric that the growth is estimated in.. ¨ In using historical growth rates, you have to wrestle with the following: ¤ How to deal with negative earnings ¤ The effects of scaling up

## Motorola: Arithmetic versus Geometric Growth Rates

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

| Year | Net Profit | Growth Rate |
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

| Year |             | Net Profit |
|------|-------------|------------|
| 1996 | \$          | 122.30     |
| 1997 | \$          | 247.05     |
| 1998 | \$          | 499.03     |
| 1999 | \$ 1,008.05 |            |
| 2000 | \$ 2,036.25 |            |
| 2001 | \$ 4,113.23 |            |

¨ If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

169

# Growth II

## Analyst Estimates

# Analyst Forecasts of Growth

¨ While the job of an analyst is to find under and over valued stocks in the sectors that they follow, a significant proportion of an analyst's time (outside of selling) is spent forecasting earnings per share. ¤ Most of this time, in turn, is spent forecasting earnings per share in the next earnings report ¤ While many analysts forecast expected growth in earnings per share over the next 5 years, the analysis and information (generally) that goes into this estimate is far more limited. ¨ Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

## How good are analysts at forecasting growth?

¨ Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| Study Group tested                     | Error | Analyst Time Series Model Error |
|----------------------------------------|-------|---------------------------------|
| Collins & Hopwood Value Line Forecasts | 31.7% | 34.1%                           |
| Brown & Rozeff Value Line Forecasts    | 28.4% | 32.2%                           |
| Fried & Givoly Earnings Forecaster     | 16.4% | 19.8%                           |

¨ The advantage that analysts have over time series models ¤ tends to decrease with the forecast period (next quarter versus 5 years) ¤ tends to be greater for larger firms than for smaller firms ¤ tends to be greater at the industry level than at the company level ¨ Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

## Are some analysts more equal than others?

¨ A study of All-America Analysts (chosen by Institutional Investor) found that ¤ There is no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%) ¤ However, in the calendar year following being chosen as All-America analysts, these analysts become slightly better forecasters than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts) ¤ Earnings revisions made by All-America analysts tend to have a much greater impact on the stock price than revisions from other analysts ¤ The recommendations made by the All America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (2.4% for buys; 13.8% for the sells).

# The Five Deadly Sins of an Analyst

¨ Tunnel Vision: Becoming so focused on the sector and valuations within the sector that you lose sight of the bigger picture. ¨ Lemmingitis: Strong urge felt to change recommendations & revise earnings estimates when other analysts do the same. ¨ Stockholm Syndrome: Refers to analysts who start identifying with the managers of the firms that they are supposed to follow. ¨ Factophobia (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a "story" coupled with a refusal to face the facts. ¨ Dr. Jekyll/Mr.Hyde: Analyst who thinks his primary job is to bring in investment banking business to the firm.

# Propositions about Analyst Growth Rates

¨ Proposition 1: There if far less private information and far more public information in most analyst forecasts than is generally claimed. ¨ Proposition 2: The biggest source of private information for analysts remains the company itself which might explain ¤ why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources) ¤ why there is such a high correlation across analysts forecasts and revisions ¤ why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team. ¨ Proposition 3: There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

175

# Growth III

## Sustainable growth and Fundamentals

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

| $\frac{\$1,000 * (.13 - .12) + 100 (13\%)}{\$ 1000 * .12}$ | g_{EPS}                 | = Retained Earnings $t_{-1}/NI_{t-1} * ROE$ |
|------------------------------------------------------------|-------------------------|---------------------------------------------|
|                                                            | = Retention Ratio * ROE |                                             |
|                                                            | = b * ROE               |                                             |

¨ In 2008, using this approach on Wells Fargo: ¨ Return on equity (based on 2008 earnings)= 17.56% ¨ Retention Ratio (based on 2008 earnings and dividends) = 45.37% ¨ Expected growth rate in earnings per share for Wells Fargo, if it can maintain these numbers.

Expected Growth Rate = 0.4537 (17.56%) = 7.97%

# One way to pump up ROE: Use more debt

Return on Equity = Return on capital + D/E (ROC - i (1-tax rate))

where

Return on capital = EBITt (1 - tax rate) / Book value of Capitalt-1

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / BV of Debt

¨ In 1998, Brahma (now Ambev) had an extremely high return on equity, partly because it borrowed money at a rate well below its return on capital ¤ Return on Capital = 19.91% ¤ Debt/Equity Ratio = 77% ¤ After-tax Cost of Debt = 5.61% ¤ Return on Equity = ROC + D/E (ROC - i(1-t)) = 19.91% + 0.77 (19.91% - 5.61%) = 30.92%

## II. Expected Growth in Net Income from noncash assets

¨ A more general version of expected growth in earnings can be obtained by substituting in the equity reinvestment into real investments (net capital expenditures and working capital) and modifying the return on equity definition to exclude cash: ¤ Net Income from non-cash assets = Net income – Interest income from cash (1- t) ¤ Equity Reinvestment Rate = (Net Capital Expenditures + Change in Working Capital) (1 - Debt Ratio)/ Net Income from non-cash assets ¤ Non-cash ROE = Net Income from non-cash assets/ (BV of Equity – Cash) ¤ Expected GrowthNet Income = Equity Reinvestment Rate \* Non-cash ROE ¨ Th equity reinvestment rate, unlike the retention ratio, can be higher than 100%, and if it is, the expected growth rate in net income can exceed the return on equity.

## Estimating expected growth in net income from non-cash assets: Coca Cola in 2010

¨ In 2010, Coca Cola reported net income of \$11,809 million. It had a total book value of equity of \$25,346 million at the end of 2009. Coca Cola had a cash balance of \$7,021 million at the end of 2009, on which it earned income of \$105 million in 2010. ¤ Non-cash Net Income = \$11,809 - \$105 = \$ 11,704 million ¤ Non-cash book equity = \$25,346 - \$7021 = \$18,325 million ¤ Non-cash ROE = \$11,704 million/ \$18,325 million **= 63.87%** ¨ Coca Cola had capital expenditures of \$2,215 million, depreciation of \$1,443 million and reported an increase in working capital of \$335 million. Coca Cola's total debt increased by \$150 million during 2010. ¤ Equity Reinvestment = 2215- 1443 + 335-150 = \$957 million ¤ Reinvestment Rate = \$957 million/ \$11,704 million= **8.18%** ¨ Expected growth rate in non-cash Net Income = 8.18% \* 63.87% = 5.22%

## III. Expected Growth in EBIT And Fundamentals: Stable ROC and Reinvestment Rate

¨ When looking at growth in operating income, the definitions are ¤ Reinvestment Rate = (Net Capital Expenditures + Change in WC)/EBIT(1-t) ¤ Return on Investment = ROC = EBIT(1-t)/(BV of Debt + BV of Equity-Cash) ¨ Reinvestment Rate and Return on Capital Expected Growth rate in Operating Income = (Net Capital Expenditures + Change in WC)/EBIT(1-t) \* ROC = Reinvestment Rate \* ROC ¨ *Proposition: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.* 

# Estimating Growth in Operating Income, if fundamentals stay locked in…

- ¨ In 1999, Cisco's fundamentals were as follows: ¤ Reinvestment Rate = 106.81% ¤ Return on Capital =34.07% ¤ Expected Growth in EBIT =(1.0681)(.3407) = 36.39% ¨ As a potential investor in Cisco, what would worry you the most about this forecast?
  - a. That Cisco's return on capital may be overstated (why?)
  - b. That Cisco's reinvestment comes mostly from acquisitions (why?)
  - c. That Cisco is getting bigger as a firm (why?)
  - d. That Cisco is viewed as a star (why?)
  - e. All of the above

# The Magical Number: ROIC (or any accounting return) and its limits

![](_page_184_Diagram_2.jpeg)

## IV. Operating Income Growth when Return on Capital is Changing

¨ When the return on capital is changing, there will be a second component to growth, positive if the return on capital is increasing and negative if the return on capital is decreasing. ¨ If ROCt is the return on capital in period t and ROC t+1 is the return on capital in period t+1, the expected growth rate in operating income will be:

$$\text{Expected Growth Rate} = \text{ROC}_{t+1} * \text{Reinvestment rate} + (\text{ROC}_{t+1} - \text{ROC}_t) / \text{ROC}_t$$

¨ **In general, if return on capital and margins are changing and/or expected to change at a company, you are better off not using any of the sustainable growth equations to estimate growth.**

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

## Top Down Growth

# **<sup>188</sup>** Growth IV

## Estimating Growth when Operating Income is Negative or Margins are changing

¨ All of the fundamental growth equations assume that the firm has a return on equity or return on capital it can sustain in the long term. ¨ When operating income is negative or margins are expected to change over time, we use a three-step process to estimate growth: ¤ Estimate growth rates in revenues over time n Determine the total market (given your business model) and estimate the market share that you think your company will earn. n Decrease the growth rate as the firm becomes larger n Keep track of absolute revenues to make sure that the growth is feasible ¤ Estimate expected operating margins each year n Set a target margin that the firm will move towards n Adjust the current margin towards the target margin ¤ Estimate the capital that needs to be invested to generate revenue growth and expected margins n Estimate a sales to capital ratio that you will use to generate reinvestment needs each year.

# 1. Revenue Growth

190

## Revenue Growth and Magnitude

| Market Size and Growth                                                                                                                                                                                                                       | X | Market Share                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Current Market size: The size of the market for the company's products & services, given geography it is targeting and product type.<br>2. Expected Growth in Market: Growth in total market, as technology and market conditions change. |   | 1. Company's current market share: If company's current market share is low, potential for growth in market share at expense of competition.<br>2. Industry economics: Nature of the business (a few big winners or splintered competition).<br>3. Strength of company's competitive advantages: Stronger and more sustainable competitive advantages should allow for higher market share. |

The potential for revenue growth is greater for companies with small revenues (and market share) in a big and growing market, especially if the company has strong competitive advantages in winner-take-all businesses.

# Airbnb: Total Market

**191**

![](_page_190_Figure_3.jpeg)

![](_page_190_Figure_5.jpeg)

![](_page_190_Figure_7.jpeg)

In its prospectus, Airbnb has expanded its estimate of market potential to \$3.4 trillion, as evidenced in this excerpt from the prospectus:

*We have a substantial market opportunity in the growing travel market and experience economy. We estimate our serviceable addressable market ("SAM") today to be \$1.5 trillion, including \$1.2 trillion for short-term stays and \$239 billion for experiences. We estimate our total addressable market ("TAM") to be \$3.4 trillion, including \$1.8 trillion for short-term stays, \$210 billion for long-term stays, and \$1.4 trillion for experiences.*

# Airbnb: Market Share

![](_page_191_Diagram_2.jpeg)

# 2. Target Margins (and path there)...

193

## Operating Margin: Target and Pathway

![](_page_192_Diagram_10.jpeg)

## Airbnb in November 2020: Growth and Profitability

|               | <i>Gross Bookings</i> | <i>Revenues</i> | <i>Revenue Growth</i> | <i>Operating Margin</i> |
|---------------|-----------------------|-----------------|-----------------------|-------------------------|
| <i>LTM</i>    | \$ 26,491,803.00      | \$ 3,625,731    |                       |                         |
| 1             | \$ 37,088,524.20      | \$ 4,691,698    | 40.00%                | -10.00%                 |
| 2             | \$ 46,360,655.25      | \$ 5,989,797    | 25.00%                | -3.00%                  |
| 3             | \$ 57,950,819.06      | \$ 7,565,479    | 25.00%                | 0.50%                   |
| 4             | \$ 72,438,523.83      | \$ 9,554,641    | 25.00%                | 4.00%                   |
| 5             | \$ 90,548,154.79      | \$ 12,065,542   | 25.00%                | 7.50%                   |
| 6             | \$ 109,019,978.36     | \$ 14,674,089   | 20.40%                | 9.52%                   |
| 7             | \$ 126,245,134.94     | \$ 17,163,026   | 15.80%                | 13.39%                  |
| 8             | \$ 140,384,590.06     | \$ 19,274,804   | 11.20%                | 17.26%                  |
| 9             | \$ 149,649,973.00     | \$ 20,748,969   | 6.60%                 | 21.13%                  |
| 10            | \$ 152,642,972.46     | \$ 21,370,016   | 2.00%                 | 25.00%                  |
| Terminal year | \$ 155,695,831.91     | \$ 21,797,416   | 2.00%                 | 25.00%                  |

|                         | Expedia      |             |                       | Booking.com  |             |                       |
|-------------------------|--------------|-------------|-----------------------|--------------|-------------|-----------------------|
|                         | 2019         | LTM         | % Change (Annualized) | 2019         | LTM         | % Change (Annualized) |
| Gross Bookings          | \$107,870.00 | \$52,470.00 | -61.75%               | \$96,400.00  | \$48,752.00 | -59.71%               |
| Revenues                | \$ 12,067.00 | \$ 7,026.00 | -51.38%               | \$ 15,066.00 | \$ 8,897.00 | -50.46%               |
| Operating Income        | \$ 961.00    | ( 892.00)   | NA                    | \$ 5,345.00  | \$ 1,831.00 | -76.03%               |
| Revenues/Gross Bookings | 11.19%       | 13.39%      |                       | 15.63%       | 18.25%      |                       |
| Operating Margin        | 7.96%        | -12.70%     |                       | 35.48%       | 20.58%      |                       |

# 3. Sales to Invested Capital: A Pathway to estimating Reinvestment

195

## Sales to Invested Capital: Reinvestment

![](_page_194_Diagram_23.jpeg)

A company with higher expected growth in revenues will need to reinvest more, though how much will be determined by the business that it operates in, with less reinvestment needed if it has excess capacity and a lag between reinvestment and growth.

# Airbnb: Reinvestment and Profitability

![](_page_195_Figure_11.jpeg)

# Aggregate versus Marginal Values

- □ While sustainable growth equations are stated in terms of returns on capital (equity) or sales to capital the numbers that drive growth are returns on new investments, i.e., marginal returns on capital (equity) or marginal sales to capital ratios.
- □ The marginal returns and sales to capital ratios can be computed by looking at changes from year to year:
  - ■  $\text{Marginal ROC} = \frac{(\text{Operating Income}_t - \text{Operating Income}_{t-1})}{(\text{Invested Capital}_{t-1} - \text{Invested Capital}_{t-2})}$
  - ■  $\text{Marginal ROC} = \frac{(\text{Sales}_t - \text{Sales}_{t-1})}{(\text{Invested Capital}_{t-1} - \text{Invested Capital}_{t-2})}$
- □ As companies scale up, the marginal values for these variables can diverge from the aggregate values.
  - ■ For companies where there are investing economies to scale, the marginal values can be significantly higher than the aggregate values.
  - ■ For companies that are facing changing competitor or are entering new businesses, the marginal values can be lower than the aggregate values.

# Closure in Valuation

## The Big Enchilada

# Getting Closure in Valuation

¨ A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

¨ Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \sum_{t=1}^{t=\infty} \frac{\text{CF}_t}{(1+r)^t}$$

$$\text{Value} = \sum_{t=1}^{t=N} \frac{\text{CF}_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^N}$$

# Ways of Estimating Terminal Value

| Approach | Inputs and Value                     | Types of business |
|----------|--------------------------------------|-------------------|
|          | TV in year n = CFn+1/ (r – g), where |                   |
| Pricing  | Terminal Year Operating Metric *     |                   |

## 1. With perpetual growth, obey the growth cap

¨ When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

r = Discount rate (Cost of Equity or Cost of Capital)

g = Expected growth rate

- ¨ The stable growth rate cannot exceed the growth rate of the economy but it can be lower.
  - If the economy is composed of **high growth and stable growth firms**, the growth rate of the latter will be lower than the growth rate of the economy.
  - **The stable growth rate can be negative,** for companies in declining businesses.
  - If you use **nominal cashflows and discount rates**, the growth rate should be nominal in the currency in which the valuation is denominated.

# Risk free Rates and Nominal GDP Growth

¨ **Risk free Rate** = Expected Inflation + Expected Real Interest Rate ¨ The real interest rate is what borrowers agree to return to lenders in real goods/services. ¨ **Nominal GDP Growth** = Expected Inflation + Expected Real Growth ¨ The real growth rate in the economy measures the expected growth in the production of goods and services.

## **The argument for Risk free rate = Nominal GDP growth**

- 1. In the long term, the real growth rate cannot be lower than the real interest rate, since the growth in goods/services has to be enough to cover the promised rate.
- 2. In the long term, the real growth rate can be higher than the real interest rate, to compensate risk taking. However, as economies mature, the difference should get smaller and since there will be growth companies in the economy, it is prudent to assume that the extra growth comes from these companies.

| Time Period | <i>Ten-year T.Bond rate</i> | <i>Inflation rate</i> | <i>Real GDP growth</i> | <i>Nominal GDP Growth Rate</i> |
|-------------|-----------------------------|-----------------------|------------------------|--------------------------------|
| 1954-2021   | 5.59%                       | 3.55%                 | 2.94%                  | 6.50%                          |
| 1954-1980   | 5.83%                       | 4.49%                 | 3.50%                  | 7.98%                          |
| 1981-2008   | 6.88%                       | 3.26%                 | 3.04%                  | 6.30%                          |
| 2011-2021   | 2.25%                       | 1.76%                 | 1.70%                  | 3.46%                          |

# A Practical Reason for using the Risk free Rate Cap – Preserve Consistency

¨ You are implicitly making assumptions about nominal growth in the economy, with your risk free rate. Thus, with a low risk free rate, you are assuming low nominal growth in the economy (with low inflation and low real growth) and with a high risk free rate, a high nominal growth rate in the economy. ¨ If you make an explicit assumption about nominal growth in cash flows that is at odds with your implicit growth assumption in the denominator, you are being inconsistent and bias your valuations: ¤ If you assume high nominal growth in the economy, with a low risk free rate, you will over value businesses. ¤ If you assume low nominal growth rate in the economy, with a high risk free rate, you will under value businesses.

Terminal Value = 2972/(.05-..-(.005)) = 54,034

Discount at Euro Cost of Capital (WACC) = 7.66% (.599) + 1.13% (0.401) = 5.04%

| Region                    | ERP = 6.83% Revenues | Weight  | ERP    |
|---------------------------|----------------------|---------|--------|
| Europe                    | 10348                | 50.24%  | 6.90%  |
| North America             | 5920                 | 28.74%  | 5.75%  |
| Asia                      | 2919                 | 14.17%  | 7.22%  |
| Latin America & Caribbean | 781                  | 3.79%   | 10.53% |
| Africa & Mid East         | 631                  | 3.06%   | 9.30%  |
| Total                     | 20599                | 100.00% | 6.83%  |

Beta = 1.20

Cost of Debt (-0.5%+2%)(1-.25) = 1.13%

Cost of Equity 7.66%

**Stable Growth** g = -0.5%; Cost of capital = 5% ROC= 5%; Reinvestment Rate=-.5%/5% = -10% 

Weights E = 59.9% D = 40.1%

Riskfree Rate: Euro Risk free rate = -0.50% <sup>+</sup> <sup>X</sup>

> Firm's D/E RaSo: 66.98%

## Heineken: September 2019 (in Euros)

Euro Cashflows

Cash flows from existing assets The Payoff from growth Maturty and Closure

The Risk in the Cash flows

On September 1, 2019, Heineken was trading at 93.25 Euros/share

Revenues will grow 3.22% a year for next 5 years, tapering down to -0.5% growth in year 10

Operatng margin (per-tax) will drop to 14.00%

Sales/Invested Capital will stay at five-year average of 0.79.

Unlevered beta of alcoholic beverage business = 0.80

| Revenues               | LTM € 23,119 | 2013-2018 Growth rate = 3.22% |
|------------------------|--------------|-------------------------------|
| Operating Margin       | 14.86%       | 14.44%                        |
| Sales/Invested Capital | 0.71         | 0.79                          |
| ROIC                   | 7.46%        | 8.32%                         |
| Effective Tax Rate     | 29.70%       | 27.00%                        |

|                         | 1        | 2        | 3        | 4        | 5        | 6        | 7        | 8        | 9        |      | 10     | Terminal year |
|-------------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|------|--------|---------------|
| Revenue growth rate     | 3.22%    | 3.22%    | 3.22%    | 3.22%    | 3.22%    | 2.48%    | 1.73%    | 0.99%    | 0.24%    |      | -0.50% | -0.50%        |
| Revenues                | € 23,863 | € 24,632 | € 25,425 | € 26,244 | € 27,089 | € 27,759 | € 28,240 | € 28,519 | € 28,589 | €    | 28,446 | € 28,304      |
| EBIT (Operating) margin | 14.38%   | 14.34%   | 14.30%   | 14.26%   | 14.21%   | 14.17%   | 14.13%   | 14.09%   | 14.04%   |      | 14.00% | 14.00%        |
| EBIT (Operating income) | € 3,432  | € 3,532  | € 3,635  | € 3,741  | € 3,850  | € 3,934  | € 3,990  | € 4,017  | € 4,015  | €    | 3,982  | \$ 3,963      |
| Tax rate                | 29.70%   | 29.70%   | 29.70%   | 29.70%   | 29.70%   | 28.76%   | 27.82%   | 26.88%   | 25.94%   |      | 25.00% | \$ 0          |
| EBIT(1-t)               | € 2,413  | € 2,483  | € 2,556  | € 2,630  | € 2,707  | € 2,802  | € 2,880  | € 2,937  | € 2,973  | €    | 2,987  | \$ 2,972      |
| - Reinvestment          | € 942    | € 973    | € 1,004  | € 1,036  | € 1,070  | € 849    | € 609    | € 353    | €        | 88 € | (181)  | \$ (297)      |
| FCFF                    | € 1,471  | € 1,511  | € 1,552  | € 1,594  | € 1,637  | € 1,953  | € 2,271  | € 2,584  | € 2,885  | €    | 3,168  | \$ 3,269      |

|     | 5        |    |
|-----|----------|----|
| %   | 3.22%    | 2. |
| 244 | € 27,089 | €  |
| %   | 14.21%   | 14 |
| 741 | € 3,850  | €  |
| %   | 29.70%   | 28 |
| 630 | € 2,707  | €  |
| 036 | € 1,070  | €  |
| 594 | € 1,637  | €  |

|      | 7        |   |
|------|----------|---|
| %    | 1.73%    | 0 |
| ,759 | € 28,240 | € |
| 7%   | 14.13%   | 1 |
| ,934 | € 3,990  | € |
| 6%   | 27.82%   | 2 |
| ,802 | € 2,880  | € |
| 849  | € 609    | € |
| ,953 | € 2,271  | € |

| 8     |        | 9      |   |
|-------|--------|--------|---|
| 9%    | 0.24%  |        |   |
| 8,519 | €      | 28,589 | € |
| 09%   | 14.04% |        |   |
| 4,017 | €      | 4,015  | € |
| 88%   | 25.94% |        |   |
| 2,937 | €      | 2,973  | € |
| 353   | €      | 88     | € |
| 2,584 | €      | 2,885  | € |

| PV(Terminal value)          | € 36,390.85 |
|-----------------------------|-------------|
| PV (CF over next 10 years)  | € 15,300.34 |
| Value of operating assets = | € 51,691.19 |
| - Debt                      | € 19,709.52 |
| - Minority interests        | € 1,069.00  |
| + Cash                      | € 1,751.60  |
| + Non-operating assets      | € 1,401.00  |
| Value of equity             | € 34,065.26 |
| Number of shares            | 571.10      |
| Estimated value /share      | € 59.65     |
| Price                       | € 93.25     |
| Price as % of value         | 56.33%      |

| <span> </span>                               |
|----------------------------------------------|
| Revenue growth rate                          |
| Revenues                                     |
| EBIT (Operating) matrix                      |
| EBIT (Operating income)                      |
| Tax rate                                     |
| EBIT(1-t)                                    |
| <span> </span> - <span> </span> Reinvestment |
| FCFF                                         |

|    | <i>I</i> |        |
|----|----------|--------|
|    | 3,22%    | 3,22%  |
| n  | € 23,863 | € 24,2 |
| e) | 14,38%   | 14,4%  |
|    | € 3,432  | € 3,42 |
|    | 29,70%   | 29,7%  |
|    | € 2,413  | € 2,2  |
|    | € 942    | € 4    |
|    | € 1,471  | € 1,4  |

## 2. Don't wait too long...

- □ Most growth firms have difficulty sustaining their growth for long periods, especially while earning excess returns. Assuming long growth periods for all firms is ignoring this reality.
- □ It is not growth per se that creates value but growth with excess returns. For growth firms to continue to generate value-creating growth, they have to be able to keep the competition at bay.
  - □ Proposition 1: The stronger and more sustainable the competitive advantages, the longer a growth company can sustain “value creating” growth.
  - □ Proposition 2: Growth companies with strong and sustainable competitive advantages are rare.

# 3. Do not forget that growth has to be earned..

- The reinvestment rate in stable growth will be a function of the stable growth rate and return on capital in perpetuity
  - Reinvestment Rate = Stable growth rate/ Stable period  $ROC = g/ ROC$
  - Terminal Value in year  $n = \frac{EBIT_{n+1} (1-t)(1 - \frac{g}{ROC})}{(\text{Cost of Capital} - g)}$

— 206 —

|      | 6%      | 8%      | 10%     | 12%     | 14%     |
|------|---------|---------|---------|---------|---------|
| 0.0% | \$1,000 | \$1,000 | \$1,000 | \$1,000 | \$1,000 |
| 0.5% | \$965   | \$987   | \$1,000 | \$1,009 | \$1,015 |
| 1.0% | \$926   | \$972   | \$1,000 | \$1,019 | \$1,032 |
| 1.5% | \$882   | \$956   | \$1,000 | \$1,029 | \$1,050 |
| 2.0% | \$833   | \$938   | \$1,000 | \$1,042 | \$1,071 |
| 2.5% | \$778   | \$917   | \$1,000 | \$1,056 | \$1,095 |
| 3.0% | \$714   | \$893   | \$1,000 | \$1,071 | \$1,122 |

# Excess Returns to Zero?

¨ There are some (McKinsey, for instance) who argue that the return on capital should always be equal to cost of capital in stable growth. ¨ But excess returns seem to persist for very long time periods.

![](_page_206_Figure_6.jpeg)

# And don't fall for sleight of hand…

- ¨ A typical assumption in many DCF valuations, when it comes to stable growth, is that capital expenditures offset depreciation and there are no working capital needs. Stable growth firms, we are told, just have to make maintenance cap ex (replacing existing assets ) to deliver growth.
- a. If you make this assumption, what expected growth rate can you use in your terminal value computation?
- b. What if the stable growth rate = inflation rate? Is it okay to make this assumption then?

# 4. Be internally consistent

¨ Risk and costs of equity and capital: Stable growth firms tend to ¤ Have betas closer to one ¤ Have debt ratios closer to industry averages (or mature company averages) ¤ Country risk premiums (especially in emerging markets should evolve over time) ¨ The excess returns at stable growth firms should approach (or become) zero. ROC -> Cost of capital and ROE -> Cost of equity ¨ The reinvestment needs and dividend payout ratios should reflect the lower growth and excess returns: ¤ Stable period payout ratio = 1 - g/ ROE ¤ Stable period reinvestment rate = g/ ROC

Choosing the right model

# Beyond Inputs: Choosing and Using the Right Model

# Summarizing the Inputs

¨ In summary, at this stage in the process, we should have an estimate of the ¤ the current cash flows on the investment, either to equity investors (dividends or free cash flows to equity) or to the firm (cash flow to the firm) ¤ the current cost of equity and/or capital on the investment ¤ the expected growth rate in earnings, based upon historical growth, analysts forecasts and/or fundamentals ¨ The next step in the process is deciding ¤ which cash flow to discount, which should indicate ¤ which discount rate needs to be estimated and ¤ what pattern we will assume growth to follow

# Which cash flow should I discount?

## ¨ Use Equity Valuation

(a) for firms which have stable leverage, whether high or not, and (b) if equity (stock) is being valued

## ¨ Use Firm Valuation

(a) for firms which have leverage which is too high or too low, and expect to change the leverage over time, because debt payments and issues do not have to be factored in the cash flows and the discount rate (cost of capital) does not change dramatically over time.

(b) for firms for which you have partial information on leverage (eg: interest expenses are missing..)

(c) in all other cases, where you are more interested in valuing the firm than the equity. (Value Consulting?)

## Given cash flows to equity, should I discount dividends or FCFE?

## ¨ Use the Dividend Discount Model

(a) For firms which pay dividends (and repurchase stock) which are close to the Free Cash Flow to Equity (over a extended period)

(b)For firms where FCFE are difficult to estimate (Example: Banks and Financial Service companies)

## ¨ Use the FCFE Model

(a) For firms which pay dividends which are significantly higher or lower than the Free Cash Flow to Equity. (What is significant? ... As a rule of thumb, if dividends are less than 80% of FCFE or dividends are greater than 110% of FCFE over a 5-year period, use the FCFE model)

(b) For firms where dividends are not available (Example: Private Companies, IPOs)

# What discount rate should I use?

¨ Cost of Equity versus Cost of Capital ¤ If discounting cash flows to equity -> Cost of Equity ¤ If discounting cash flows to the firm -> Cost of Capital ¨ What currency should the discount rate (risk free rate) be in? ¤ Match the currency in which you estimate the risk free rate to the currency of your cash flows ¨ Should I use real or nominal cash flows? ¤ If discounting real cash flows -> real cost of capital ¤ If nominal cash flows -> nominal cost of capital ¤ If inflation is low (<10%), stick with nominal cash flows since taxes are based upon nominal income ¤ If inflation is high (>10%) switch to real cash flows

# Which Growth Pattern Should I use?

¨ If your firm is ¤ large and growing at a rate close to or less than growth rate of the economy, or ¤ constrained by regulation from growing at rate faster than the economy ¤ has the characteristics of a stable firm (average risk & reinvestment rates)

## Use a Stable Growth Model

¨ If your firm ¤ is large & growing at a moderate rate (≤ Overall growth rate + 10%) or ¤ has a single product & barriers to entry with a finite life (e.g. patents)

## Use a 2-Stage Growth Model

¨ If your firm ¤ is small and growing at a very high rate (> Overall growth rate + 10%) or ¤ has significant barriers to entry into the business ¤ has firm characteristics that are very different from the norm

## Use a 3-Stage or n-stage Model

# The Building Blocks of Valuation

| <b>Choose a</b>    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                   |  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--|
| Cash Flow          | <i>Dividends</i>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | <i>Cashflows to Equity</i>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | <i>Cashflows to Firm</i>                                                                                          |  |
|                    | Expected Dividends to Stockholders                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Net Income<br>- (1- $\delta$ ) (Capital Exp. - Deprec'n)<br>- (1- $\delta$ ) Change in Work. Capital<br>= Free Cash flow to Equity (FCFE)<br>[ $\delta$ = Debt Ratio]                                                                                                                                                                                                                                                                                                                                                                        | EBIT (1- tax rate)<br>- (Capital Exp. - Deprec'n)<br>- Change in Work. Capital<br>= Free Cash flow to Firm (FCFF) |  |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                   |  |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                   |  |
| & A Discount Rate  | <i>Cost of Equity</i>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <i>Cost of Capital</i>                                                                                            |  |
|                    | <ul> <li><i>Basis</i>: The riskier the investment, the greater is the cost of equity.</li> <li><i>Models</i>:<br/>CAPM: Riskfree Rate + Beta (Risk Premium)<br/>APM: Riskfree Rate + <math>\Sigma</math> Beta<sub>j</sub> (Risk Premium<sub>j</sub>): <i>n factors</i></li> </ul>                                                                                                                                                                                                                                                                                                                                                                                                | <p>WACC = <math>k_e</math> ( E/ (D+E))</p> <p>+ <math>k_d</math> ( D/(D+E))</p> <p><math>k_d</math> = Current Borrowing Rate (1-t)</p> <p>E,D: Mkt Val of Equity and Debt</p>                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                   |  |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                   |  |
| & a growth pattern | <b>Stable Growth</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <b>Two-Stage Growth</b>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | <b>Three-Stage Growth</b>                                                                                         |  |
|                    | <img alt="Stable Growth graph: A horizontal graph showing a stable growth pattern. The y-axis is labeled 'g' and has an arrow pointing up. The x-axis is labeled 't' and has an arrow pointing to the right. The graph shows a horizontal line at a constant value on the y-axis for the entire time tract. The graph then shows a step down from the constant value on the y-axis at time t to a horizontal line at a different value on the y-axis at time t+1. The distance between the two lines is labeled 'g'. The graph is continuous and consists of three stages: a horizontal stage from t to t+1, a step down from t to t+1, and a horizontal stage from t+1 to t."/> | <img alt="Two-Stage Growth graph: A horizontal graph showing a stable growth pattern. The y-axis is labeled 'g' and has an arrow pointing up. The x-axis is labeled 't' and has an arrow pointing to the right. The graph shows a horizontal line at a constant value on the y-axis for the entire time tract. The graph then shows a step down from t to t+1. The distance between the two lines is labeled 'g'. The graph is continuous and consists of three stages: a horizontal stage from t to t+1, a step down from t to t+1, and a h |                                                                                                                   |  |

The trouble starts after you tell me you are done..

# Tying up Loose Ends **<sup>217</sup>**

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

**220**

| Enterprise Value Cash      | Company A \$1,000.0 \$100.0 | Company B \$1,000.0 \$100.0 | Company C \$1,000.0 \$100.0 |
|----------------------------|-----------------------------|-----------------------------|-----------------------------|
| Return on invested capital | 10%                         | 5%                          | 22%                         |
| Cost of capital            | 10%                         | 10%                         | 12%                         |
| Trades in                  | US                          | US                          | Argentina                   |

In which of these companies is cash most likely to be

- a) A Neutral Asset (worth \$100 million)
- b) A Wasting Asset (worth less than \$100 million)
- c) A Potential Value Creator (worth >\$100 million)

## Should you ever discount cash for its low returns?

¨ There are some analysts who argue that companies with a lot of cash on their balance sheets should be penalized by having the excess cash discounted to reflect the fact that it earns a low return. ¤ Excess cash is usually defined as holding cash that is greater than what the firm needs for operations. ¤ A low return is defined as a return lower than what the firm earns on its non-cash investments. ¨ This is the wrong reason for discounting cash. If the cash is invested in riskless securities, it should earn a low rate of return. As long as the return is high enough, given the riskless nature of the investment, cash does not destroy value. ¨ There is a right reason, though, that may apply to some companies… Managers can do stupid things with cash (overpriced acquisitions, pie-in-the-sky projects….) and you have to discount for this possibility.

# Cash: Discount or Premium?

222

*Market Value of \$ 1 in cash:  
Estimates obtained by regressing Enterprise Value against Cash Balances*

![](_page_221_Figure_20.jpeg)

# A Detour: Closed End Mutual Funds

¨ Assume that you have a closed-end fund that invests in ' average risk" stocks. Assume also that you expect the market (average risk investments) to make 11.5% annually over the long term. If the closed end fund underperforms the market by 0.50%, estimate the discount on the fund.

![](_page_222_Figure_3.jpeg)

## The Most Famous Closed End Fund in History?

![](_page_223_Figure_3.jpeg)

![](_page_223_Picture_4.jpeg)

# 2. Dealing with Holdings in Other firms

¨ Holdings in other firms can be categorized into ¤ Minority passive holdings, in which case only the dividend from the holdings is shown in the balance sheet ¤ Minority active holdings, in which case the share of equity income is shown in the income statements ¤ Majority active holdings, in which case the financial statements are consolidated. ¨ In an intrinsic valuation, you would like to estimate the intrinsic value of these holdings and including them in your overall intrinsic valuation of the company.

## If you really want to value cross holdings right….

¨ Step 1: Value the parent company without any cross holdings. This will require using unconsolidated financial statements rather than consolidated ones. ¨ Step 2: Value each of the cross holdings individually. (If you use the market values of the cross holdings, you will build in errors the market makes in valuing them into your valuation).

- ¨ Step 3: The final value of the equity in the parent company with N cross holdings will be: Value of unconsolidated parent company
  - – Debt of unconsolidated parent company

    +  $\sum_{j=1}^{j=N} \%$  owned of Company j \* (Value of Company j - Debt of Company j)

# Valuing Yahoo as the sum of its intrinsic pieces

227

100% of Yahoo! US Equity

| Operating assets =\$4383 |
|--------------------------|
| + Cash = \$4,571         |
| - Debt = \$1,591         |
| =Parent Equity = \$7,363 |

+ 35% of Yahoo! Japan Equity

| Operating assets = \$17,884                 |
|---------------------------------------------|
| + Cash = \$3,113                            |
| - Debt = \$0                                |
| Equity = \$20,997<br>35% of value = \$7,349 |

+ 22.1% of Alibaba Equity

| Operating assets = \$127,484                    |
|-------------------------------------------------|
| + Cash = \$27963                                |
| - Debt = \$6,670                                |
| Equity = \$145,587<br>22.1% of value = \$32,175 |

- Loose Ends =

| - Taxes due = \$5,017   |
|-------------------------|
| - Yahoo options = \$298 |

**Equity value= \$41,571  
Per share = \$41.19**

If you have to settle for an approximation, try this…

¨ For majority holdings, with full consolidation, convert the minority interest from book value to market value by applying a price to book ratio (based upon the sector average for the subsidiary) to the minority interest. ¤ Estimated market value of minority interest = Minority interest on balance sheet \* Price to Book ratio for sector (of subsidiary) ¤ Subtract this from the estimated value of the consolidated firm to get to value of the equity in the parent company. ¨ For minority holdings in other companies, convert the book value of these holdings (which are reported on the balance sheet) into market value by multiplying by the price to book ratio of the sector(s). Add this value on to the value of the operating assets to arrive at total firm value.

# Yahoo: A pricing game?

229

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

## 3. Other Assets that have not been counted yet..

¨ Assets that you should not be counting (or adding on to DCF values) ¤ If an asset is contributing to your cashflows, you cannot count the market value of the asset in your value. ¨ Assets that you can count (or add on to your DCF valuation) ¤ Overfunded pension plans: If you have a defined benefit plan and your assets exceed your expected liabilities, you could consider the over funding with two caveats: n Collective bargaining agreements may prevent you from laying claim to these excess assets. n There are tax consequences. Often, withdrawals from pension plans get taxed at much higher rates. ¤ Unutilized assets: If you have assets or property that are not being utilized to generate cash flows (vacant land, for example), you have not valued them yet. You can assess a market value for these assets and add them on to the value of the firm.

# An Uncounted Asset?

231

Price tag: \$200 million

![](_page_230_Picture_23.jpeg)

The longtime home of Playboy magazine founder Hugh Hefner is to be sold to Daren Metropoulos, a principal at private-equity firm Metropoulos & Co. PHOTO: GETTY IMAGES

## 4. A Discount for Complexity: An Experiment

| Operating Income | Company A \$ 1 billion | Company B \$ 1 billion |
|------------------|------------------------|------------------------|
| Tax rate         | 40%                    | 40%                    |
| ROIC             | 10%                    | 10%                    |
| Expected Growth  | 5%                     | 5%                     |
| Cost of capital  | 8%                     | 8%                     |
| Business Mix     | Single                 | Multiple               |
| Holdings         | Simple                 | Complex                |
| Accounting       | Transparent            | Opaque                 |

Which firm would you value more highly?

## Measuring Complexity: Volume of Data in Financial Statements

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

## ¨ In Discounted Cashflow Valuation

¤ The Aggressive Analyst: Trust the firm to tell the truth and value the firm based upon the firm's statements about their value. ¤ The Conservative Analyst: Don't value what you cannot see. ¤ The Compromise: Adjust the value for complexity <sup>n</sup> Adjust cash flows for complexity <sup>n</sup> Adjust the discount rate for complexity <sup>n</sup> Adjust the expected growth rate/ length of growth period <sup>n</sup> Value the firm and then discount value for complexity

## ¨ In relative valuation

¤ In a relative valuation, you may be able to assess the price that the market is charging for complexity: ¤ With the hundred largest market cap firms, for instance:

PBV = 0.65 + 15.31 ROE – 0.55 Beta + 3.04 Expected growth rate – 0.003 # Pages in 10K

## 5. Be circumspect about defining debt for cost of capital purposes…

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

¨ In recent years, firms have turned to giving employees (and especially top managers) equity option or restricted stock packages as part of compensation. If they are options, they usually are long term and on volatile stocks. If restricted stock, the restrictions are usually on trading. ¨ These equity compensation packages are clearly valuable and the question becomes how best to deal with them in valuation. ¨ Two key issues with employee options: ¤ How do options or restricted stock granted in the past affect equity value per share today? ¤ How do expected grants of either, in the future, affect equity value today?

## The Easier Problem: Restricted Stock Grants

**Aswath Damodaran 240**

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

Value of firm = 
$$100 / (.08 - .03)$$
 = 2000

Debt = 1000

= Equity = 1000

Number of diluted shares = 110

Proceeds from option exercise = 10 \* 10 = 100

Value per share = (1000+ 100)/110 = \$ 10

¨ The treasury stock approach fails to consider the time premium on the options. The treasury stock approach also has problems with out-of-the- money options. If considered, they can increase the value of equity per share. If ignored, they are treated as non-existent.

# III. Option Value Drag

¨ Step 1: Value the firm, using discounted cash flow or other valuation models. ¨ Step 2: Subtract out the value of the outstanding debt to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly. ¨ Step 3:Subtract out the market value (or estimated market value) of other equity claims: ¤ Value of Warrants = Market Price per Warrant \* Number of Warrants : Alternatively estimate the value using option pricing model ¤ Value of Conversion Option = Market Value of Convertible Bonds - Value of Straight Debt Portion of Convertible Bonds ¤ Value of employee Options: Value using the average exercise price and maturity. ¨ Step 4:Divide the remaining value of equity by the number of shares outstanding to get value per share.

## Valuing Equity Options issued by firms… The Dilution Problem

¨ Option pricing models can be used to value employee options with four caveats – ¤ Employee options are long term, making the assumptions about constant variance and constant dividend yields much shakier, ¤ Employee options result in stock dilution, and ¤ Employee options are often exercised before expiration, making it dangerous to use European option pricing models. ¤ Employee options cannot be exercised until the employee is vested. ¨ These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and early exercise, and factoring in the dilution effect. The resulting value can be adjusted for the probability that the employee will not be vested.

## Valuing Employee Options

¨ To value employee options, you need the following inputs into the option valuation model: ¤ Stock Price = \$ 10, Adjusted for dilution = \$9.58 ¤ Strike Price = \$ 10 ¤ Maturity = 10 years (Can reduce to reflect early exercise) ¤ Standard deviation in stock price = 40% ¤ Riskless Rate = 4% ¨ Using a dilution-adjusted Black Scholes model, we arrive at the following inputs: ¤ N (d1) = 0.8199 ¤ N (d2) = 0.3624 ¤ Value per call = \$ 9.58 (0.8199) - \$10 e -(0.04) (10)(0.3624) = \$5.42

## Value of Equity to Value of Equity per share

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

# Option grants in the future…

¨ Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value. ¨ The simplest mechanism for bringing in future option grants into the analysis is to do the following: ¤ Estimate the value of options granted each year over the last few years as a percent of revenues. ¤ Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller. ¤ Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.

# NARRATIVE AND NUMBERS: VALUATION AS A BRIDGE

Tell me a story..

# Valuation as a bridge

## *Number Crunchers Story Tellers*

![](_page_250_Diagram_3.jpeg)

# Step 1: Survey the landscape

¨ Every valuation starts with a narrative, a story that you see unfolding for your company in the future. ¨ In developing this narrative, you will be making assessments of ¤ Your company (its products, its management and its history. ¤ The market or markets that you see it growing in. ¤ The competition it faces and will face. ¤ The macro environment in which it operates.

![](_page_252_Diagram_16.jpeg)

# Step 2: Create a narrative for the future

¨ Every valuation starts with a narrative, a story that you see unfolding for your company in the future. ¨ In developing this narrative, you will be making assessments of your company (its products, its management), the market or markets that you see it growing in, the competition it faces and will face and the macro environment in which it operates. ¤ Rule 1: Keep it simple. ¤ Rule 2: Keep it focused. ¤ Rule 3: Stay grounded in reality.

# The Uber Narrative

In June 2014, my initial narrative for Uber was that it would be

- 1. An urban car service business: I saw Uber primarily as a force in urban areas and only in the car service business.
- 2. Which would expand the business moderately (about 40% over ten years) by bringing in new users.
- 3. With local networking benefits: If Uber becomes large enough in any city, it will quickly become larger, but that will be of little help when it enters a new city.
- 4. Maintain its revenue sharing (20%) system due to strong competitive advantages (from being a first mover).
- 5. And its existing low-capital business model, with drivers as contractors and very little investment in infrastructure.

# Step 3: Check the narrative against history, economic first principles & common sense

![](_page_255_Diagram_2.jpeg)

# The Impossible, The Implausible and the Improbable

257

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

Growth

![](_page_256_Diagram_42.jpeg)

# Uber: Possible, Plausible and Probable

![](_page_257_Diagram_1.jpeg)

# The Runaway Story: When you want a story to be true…

- ¨ With a runaway business story, you usually have three ingredients:
  - 1. Charismatic, likeable Narrator: The narrator of the business story is someone that you want to see succeed, either because you like the narrator or because he/she will be a good role model.
  - 2. Telling a story about disrupting a much business, where you dislike the status quo: The status quo in the business that the story is disrupting is dissatisfying (to everyone involved)>
- 3. With a societal benefit as bonus: And if the story holds, society and humanity will benefit. ¨ Since you want this story to work out, you stop asking questions, because the answers may put the story at risk.

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

![](_page_259_Figure_10.jpeg)

The Story The Checks (?)

+ Money

+

## The Impossible: The Runaway Story

![](_page_259_Picture_2.jpeg)

![](_page_259_Picture_3.jpeg)

# When runaway stories melt down..

**Untrustworthy Storyteller** A narrator, who through his/her words or actions has become untrustworthy.

**Story at war with numbers** The company's narrative conflicts with its own actions and/or with the actual results/numbers reported by the company.

**Bad Business Model** The business model has a fundamental flaw that can affect either future profitability or survival, but the management is either in denial about the flaw or opaque in how it plans to deal with it. + + =

**Meltdown Story** Investors, lenders and observers question story, unwilling to accept the company's spin on number, pushing pricing down.

## **The Meltdown Story**

## The Implausible: The Big Market Delusion

![](_page_261_Diagram_1.jpeg)

![](_page_261_Diagram_2.jpeg)

| Company             | Market Cap            | Enterprise Value      | Current Revenues    | Breakeven Revenues (2025) | % from Online Advertising | Imputed Online Ad Revenue (2025) |
|---------------------|-----------------------|-----------------------|---------------------|---------------------------|---------------------------|----------------------------------|
| Google              | \$441,572.00          | \$386,954.00          | \$69,611.00         | \$224,923.20              | 89.50%                    | \$201,306.26                     |
| Facebook            | \$245,662.00          | \$234,696.00          | \$14,640.00         | \$129,375.54              | 92.20%                    | \$119,284.26                     |
| Yahoo!              | \$30,614.00           | \$23,836.10           | \$4,871.00          | \$25,413.13               | 100.00%                   | \$25,413.13                      |
| LinkedIn            | \$23,265.00           | \$20,904.00           | \$2,561.00          | \$22,371.44               | 80.30%                    | \$17,964.26                      |
| Twitter             | \$16,927.90           | \$14,912.90           | \$1,779.00          | \$23,128.68               | 89.50%                    | \$20,700.17                      |
| Pandora             | \$3,643.00            | \$3,271.00            | \$1,024.00          | \$2,915.67                | 79.50%                    | \$2,317.96                       |
| Yelp                | \$1,765.00            | \$0.00                | \$465.00            | \$1,144.26                | 93.60%                    | \$1,071.02                       |
| Zillow              | \$4,496.00            | \$4,101.00            | \$480.00            | \$4,156.21                | 18.00%                    | \$748.12                         |
| Zynga               | \$2,241.00            | \$1,142.00            | \$752.00            | \$757.86                  | 22.10%                    | \$167.40                         |
| <b>Total US</b>     | <b>\$770,185.90</b>   | <b>\$689,817.00</b>   | <b>\$96,183.00</b>  | <b>\$434,185.98</b>       |                           | <b>\$388,972.66</b>              |
| Alibaba             | \$184,362.00          | \$173,871.00          | \$12,598.00         | \$111,414.06              | 60.00%                    | \$66,848.45                      |
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

|                                            | FY 2013      | FY 2014      | FY 2015            | FY 2016      | FY 2017       | FY 2018       | FY 2019       | FY 2020       | FY 2021               | FY 2022       | FY 2023       | FY 2024                       | FY 2025       | FY 2026       | FY 2027       | FY 2028       |
|--------------------------------------------|--------------|--------------|--------------------|--------------|---------------|---------------|---------------|---------------|-----------------------|---------------|---------------|-------------------------------|---------------|---------------|---------------|---------------|
| <b>Unit Volume</b>                         | 24,298       | 36,883       | 64,684             | 86,713       | 149,869       | 214,841       | 291,861       | 384,747       | 466,559               | 550,398       | 643,850       | 726,655                       | 820,645       | 922,481       | 1,034,215     | 1,137,780     |
| % Growth                                   |              | 52%          | 75%                | 34%          | 73%           | 43%           | 36%           | 32%           | 21%                   | 18%           | 17%           | 13%                           | 13%           | 12%           | 12%           | 10%           |
| <b>Automotive Revenue Per Unit (\$)</b>    | 93,403       | 85,342       | 83,432             | 78,932       | 65,465        | 58,258        | 56,407        | 55,553        | 55,991                | 56,586        | 56,969        | 57,540                        | 58,138        | 58,603        | 59,002        | 59,554        |
| % Growth                                   |              | -9%          | -2%                | -5%          | -17%          | -11%          | -3%           | -2%           | 1%                    | 1%            | 1%            | 1%                            | 1%            | 1%            | 1%            | 1%            |
| <b>Automotive Sales</b>                    | 2,462        | 3,321        | 5,613              | 7,051        | 10,025        | 12,720        | 16,685        | 21,595        | 26,347                | 31,357        | 36,897        | 42,022                        | 47,949        | 54,283        | 61,221        | 67,980        |
| <b>Development Service Sales</b>           | 16           | 40           | 42                 | 44           | 46            | 49            | 51            | 54            | 56                    | 59            | 62            | 65                            | 68            | 72            | 75            | 79            |
| <b>Total Sales</b>                         | <b>2,478</b> | <b>3,361</b> | <b>5,655</b>       | <b>7,095</b> | <b>10,072</b> | <b>12,768</b> | <b>16,736</b> | <b>21,648</b> | <b>26,403</b>         | <b>31,416</b> | <b>36,959</b> | <b>42,087</b>                 | <b>48,017</b> | <b>54,355</b> | <b>61,296</b> | <b>68,059</b> |
| % Growth                                   |              | 36%          | 60%                | 25%          | 42%           | 27%           | 31%           | 29%           | 22%                   | 19%           | 18%           | 14%                           | 14%           | 13%           | 13%           | 11%           |
| <b>EBITDA</b>                              | <b>148</b>   | <b>417</b>   | <b>920</b>         | <b>1,042</b> | <b>1,586</b>  | <b>2,150</b>  | <b>3,138</b>  | <b>4,066</b>  | <b>4,857</b>          | <b>5,723</b>  | <b>6,328</b>  | <b>7,182</b>                  | <b>8,144</b>  | <b>9,688</b>  | <b>10,874</b> | <b>12,099</b> |
| % Margin                                   | 6.0%         | 12.4%        | 16.3%              | 14.7%        | 15.7%         | 16.8%         | 18.7%         | 18.8%         | 18.4%                 | 18.2%         | 17.1%         | 17.1%                         | 17.0%         | 17.8%         | 17.7%         | 17.8%         |
| <b>D&amp;A</b>                             | 103          | 158          | 172                | 203          | 301           | 353           | 389           | 537           | 606                   | 696           | 811           | 938                           | 1,088         | 1,260         | 1,451         | 1,661         |
| % of Capex                                 | 41%          | 79%          | 59%                | 65%          | 62%           | 69%           | 78%           | 86%           | 79%                   | 77%           | 75%           | 76%                           | 76%           | 76%           | 76%           | 77%           |
| <b>EBIT</b>                                | <b>45</b>    | <b>259</b>   | <b>748</b>         | <b>839</b>   | <b>1,285</b>  | <b>1,796</b>  | <b>2,749</b>  | <b>3,529</b>  | <b>4,252</b>          | <b>5,027</b>  | <b>5,517</b>  | <b>6,244</b>                  | <b>7,056</b>  | <b>8,429</b>  | <b>9,423</b>  | <b>10,439</b> |
| % Margin                                   | 1.8%         | 7.7%         | 13.2%              | 11.8%        | 12.8%         | 14.1%         | 16.4%         | 16.3%         | 16.1%                 | 16.0%         | 14.9%         | 14.8%                         | 14.7%         | 15.5%         | 15.4%         | 15.3%         |
| <b>Net Interest Income (Expense)</b>       | (27)         | (1)          | 9                  | 33           | 47            | 90            | 108           | 155           | 199                   | 278           | 358           | 445                           | 542           | 651           | 784           | 934           |
| <b>Other Income</b>                        | 28           | 0            | 0                  | 0            | 0             | 0             | 0             | 0             | 0                     | 0             | 0             | 0                             | 0             | 0             | 0             | 0             |
| <b>Pretax Income</b>                       | <b>46</b>    | <b>258</b>   | <b>758</b>         | <b>872</b>   | <b>1,332</b>  | <b>1,886</b>  | <b>2,857</b>  | <b>3,684</b>  | <b>4,451</b>          | <b>5,305</b>  | <b>5,875</b>  | <b>6,688</b>                  | <b>7,598</b>  | <b>9,080</b>  | <b>10,207</b> | <b>11,373</b> |
| <b>Income Taxes</b>                        | 3            | 2            | 14                 | 34           | 86            | 262           | 462           | 641           | 807                   | 1,003         | 1,134         | 1,317                         | 1,470         | 1,761         | 2,028         | 2,323         |
| % Effective Rate                           | 6%           | 1%           | 2%                 | 4%           | 6%            | 14%           | 16%           | 17%           | 18%                   | 19%           | 19%           | 20%                           | 19%           | 19%           | 20%           | 20%           |
| <b>Net Income</b>                          | <b>44</b>    | <b>258</b>   | <b>744</b>         | <b>839</b>   | <b>1,246</b>  | <b>1,624</b>  | <b>2,395</b>  | <b>3,043</b>  | <b>3,644</b>          | <b>4,303</b>  | <b>4,741</b>  | <b>5,372</b>                  | <b>6,128</b>  | <b>7,319</b>  | <b>8,179</b>  | <b>9,050</b>  |
| <b>Elis</b>                                |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               |               |               |
| <b>After-tax Interest Expense (Income)</b> | 27           | 1            | (9)                | (33)         | (47)          | (90)          | (108)         | (154)         | (199)                 | (278)         | (357)         | (444)                         | (541)         | (650)         | (782)         | (932)         |
| <b>Depreciation of PP&amp;E</b>            | 103          | 158          | 172                | 203          | 301           | 353           | 389           | 537           | 606                   | 696           | 811           | 938                           | 1,088         | 1,260         | 1,451         | 1,661         |
| <b>Other</b>                               | 0            | 0            | 0                  | 0            | 0             | 0             | 0             | 0             | 0                     | 0             | 0             | 0                             | 0             | 0             | 0             | 0             |
| <b>Less</b>                                |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               |               |               |
| <b>Change in Working Capital</b>           | (155)        | (14)         | (157)              | (167)        | (172)         | (325)         | (163)         | (81)          | (28)                  | (299)         | (356)         | (328)                         | (219)         | (329)         | (365)         | (376)         |
| % of Change in Sales                       |              | -2%          | -7%                | -12%         | -6%           | -12%          | -4%           | -2%           | -1%                   | -6%           | -6%           | -6%                           | -4%           | -5%           | -5%           | -6%           |
| <b>Capital Expenditures</b>                | 250          | 200          | 312                | 312          | 486           | 510           | 497           | 623           | 765                   | 906           | 1,078         | 1,236                         | 1,437         | 1,660         | 1,898         | 2,149         |
| % of Sales                                 | 10%          | 6%           | 6%                 | 4%           | 5%            | 4%            | 3%            | 3%            | 3%                    | 3%            | 3%            | 3%                            | 3%            | 3%            | 3%            | 3%            |
| <b>Other</b>                               | 0            | 0            | 0                  | 0            | 0             | 0             | 0             | 0             | 0                     | 0             | 0             | 0                             | 0             | 0             | 0             | 0             |
| <b>Unlevered Free Cash Flow</b>            | <b>78</b>    | <b>229</b>   | <b>750</b>         | <b>863</b>   | <b>1,186</b>  | <b>1,702</b>  | <b>2,343</b>  | <b>2,884</b>  | <b>3,314</b>          | <b>4,113</b>  | <b>4,472</b>  | <b>4,959</b>                  | <b>5,456</b>  | <b>6,597</b>  | <b>7,315</b>  | <b>8,005</b>  |
| EBITDA                                     |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               | 12,099        |               |
| Sales                                      |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               | 68,059        |               |
| Net Debt (Cash)                            |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               | (260)         |               |
| Tesla Diluted Shares                       |              |              |                    |              |               |               |               |               |                       |               |               |                               |               |               | 142           |               |
| <b>Exit EBITDA High</b>                    |              |              |                    |              |               | 12.0 x        |               | Exit PPG High |                       | 5.0%          |               | Exit P/Sales High             |               | 180%          |               |               |
| <b>Exit EBITDA Low</b>                     |              |              |                    |              |               | 8.0 x         |               | Exit PPG Low  |                       | 3.0%          |               | Exit P/Sales Low              |               | 130%          |               |               |
|                                            |              |              | Discount Rate High |              |               | 13.0%         |               |               | FY Month of Valuation |               |               | 1.0 (Beginning of this Month) |               |               |               |               |
|                                            |              |              | Discount Rage Low  |              |               | 9.0%          |               |               | Month of FY End       |               |               | 12.0 (End of this Month)      |               |               |               |               |

# Step 4: Connect your narrative to key drivers of value

![](_page_263_Diagram_1.jpeg)

# Step 4: Value the company (Uber)

265

## Uber: Intrinsic valuation - June 8, 2014 (in US \$)

![](_page_264_Figure_10.jpeg)

# Step 5: Keep the feedback loop open…

- 1. Not just car service company.: Uber is a car company, not just a car service company, and there may be a day when consumers will subscribe to a Uber service, rather than own their own cars. It could also expand into logistics, i.e., moving and transportation businesses.
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

- □ The equity risk premiums that I have used in the valuations that follow reflect my thinking (and how it has evolved) on the issue.
  - ■ Pre-1998 valuations: In the valuations prior to 1998, I use a risk premium of 5.5% for mature markets (close to both the historical and the implied premiums then)
  - ■ Between 1998 and Sept 2008: In the valuations between 1998 and September 2008, I used a risk premium of 4% for mature markets, reflecting my belief that risk premiums in mature markets do not change much and revert back to historical norms (at least for implied premiums).
  - ■ Valuations done in 2009: After the 2008 crisis and the jump in equity risk premiums to 6.43% in January 2008, I have used a higher equity risk premium (5-6%) for the next 5 years and will assume a reversion back to historical norms (4%) only after year 5.
  - ■ After 2009: I have used updated equity risk premiums, as of the time that I did the valuations.

# The Valuation Set up

¨ With each company that I value in this next section, I will try to start with a story about the company and use that story to construct a valuation. ¨ With each valuation, rather than focus on all of the details (which will follow the blueprint already laid out), I will focus on a specific component of the valuation that is unique or different.

Stocks that look like Bonds, Things Change and Market Valuations

# **<sup>273</sup>** Training Wheels On?

## *Training Wheels valuation: Con Ed in August 2008*

In trailing 12 months, through June 2008 Earnings per share = \$3.17 Dividends per share = \$2.32 Dividend payout ratio is 73%

## **Why a stable growth dividend discount model?**

- 1. Why stable growth: Company is a regulated utility, restricted from investing in new growth markets. Growth is constrained by the fact that the population (and power needs) of its customers in New York are growing at very low rates. Growth rate forever = 2%
- 2. Why equity: Company's debt ratio has been stable at about 70% equity, 30% debt for decades.
- 3. Why dividends: Company has paid out about 97% of its FCFE as dividends over the last five years.

Riskfree rate 4.10% 10-year T.Bond rate Beta 0.80 Beta for regulated power utilities

Equity Risk Premium 4.5% Implied Equity Risk Premium - US market in 8/2008

Cost of Equity = 4.1% + 0.8 (4.5%) = 7.70%

*Growth rate forever = 2.1%*

Value per share today= Expected Dividends per share next year / (Cost of equity - Growth rate) = 2.32 (1.021)/ (.077 - ,021) = \$42.30

> **On August 12, 2008 Con Ed was trading at \$ 40.76.**

**Test 2: Is the stable growth rate consistent with fundamentals?**

Retention Ratio = 27% ROE =Cost of equity = 7.7% Expected growth = 2.1%

## **Test 3: Is the firm's risk and cost of equity consistent with a stable growith firm?**

Beta of 0.80 is at lower end of the range of stable company betas: 0.8 -1.2

## **Test 1: Is the firm paying dividends like a stable growth firm?**

## From DCF value to target price and returns…

¨ Assume that you believe that your valuation of Con Ed (\$42.30) is a fair estimate of the value, 7.70% is a reasonable estimate of Con Ed's cost of equity and that your expected dividends for next year (2.32\*1.021) is a fair estimate, what is the expected stock price a year from now (assuming that the market corrects its mistake?) ¨ If you bought the stock today at \$40.76, what return can you expect to make over the next year (assuming again that the market corrects its mistake)?

## **Current Cashflow to Firm**

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

Value/Share \$ 83.55

**Riskfree Rate**:

Riskfree rate = 3.72%

+

**Beta**  1.15 **X** **Risk Premium** 4%

Unlevered Beta for Sectors: 1.09

## 3M: A Pre-crisis valuation

Reinvestment Rate 30%

Return on Capital 25%

> Term Yr \$4,758 \$2,113 \$2,645

On September 12, 2008, 3M was trading at \$70/share

First 5 years

D/E=8.8%

Cost of capital = 8.32% (0.92) + 2.91% (0.08) = 7.88%

| Year           | 1       | 2       | 3       | 4       | 5         |
|----------------|---------|---------|---------|---------|-----------|
| EBIT (1-t)     | \$3,734 | \$4,014 | \$4,279 | \$4,485 | \$4,619   |
| - Reinvestment | \$1,120 | \$1,204 | \$1,312 | \$1,435 | \$1,540 , |
| = FCFF         | \$2,614 | \$2,810 | \$2,967 | \$3,049 | \$3,079   |

## **Current Cashflow to Firm**

EBIT(1-t)= 4810 (1-**.35**)= 3,180 - Nt CpX= 350 - Chg WC 691 = FCFF 2139 Reinvestment Rate = 1041/3180 =33% Return on capital = 23.06%

**Expected Growth in EBIT (1-t)** .25\*.20=.05 **5%**

## **Stable Growth**

g = 3%; Beta = 1.00;; ERP =4% Debt Ratio= 8%; Tax rate=35% Cost of capital = 7.55% ROC= 7.55%; Reinvestment Rate=3/7.55=40%

Terminal Value5= 2434/(.0755-.03) = 53,481

**Cost of Equity 10.86%**

**Cost of Debt** (3.96%+.1.5%)(1-.35) = 3.55%

**Weights** E = 92% D = 8%

| Op. Assets | 43,975 |
|------------|--------|
| + Cash:    | 3253   |
| - Debt     | 4920   |
| =Equity    | 42308  |

Value/Share \$ 60.53

**Riskfree Rate**: Riskfree rate = 3.96% + **Beta**  1.15 **X Risk Premium** 6% Unlevered Beta for Sectors: 1.09 D/E=8.8% I*ncreased risk premium to 6% for next 5 years*

## 3M: Post-crisis valuation

Reinvestment Rate

25%

Return on Capital 20%

|  | <b>Term Yr</b> |
|--|----------------|
|  | \$4,038        |
|  | \$1,604        |
|  | \$2,434        |

On October 16, 2008, MMM was trading at \$57/share.

First 5 years

Cost of capital = 10.86% (0.92) + 3.55% (0.08) = 10.27%

| Year           | 1       | 2       | 3       | 4       | 5       |
|----------------|---------|---------|---------|---------|---------|
| EBIT (1-t)     | \$3,339 | \$3,506 | \$3,667 | \$3,807 | \$3,921 |
| - Reinvestment | \$835   | \$877   | \$1,025 | \$1,288 | \$1,558 |
| = FCFF         | \$2,504 | \$2,630 | \$2,642 | \$2,519 | \$2,363 |

*Lowered base operating income by 10%*

*Reduced growth rate to 5%*

*Higher default spread for next 5 years*

*Did not increase debt ratio in stable growth to 20%*

# Valuing the S&P 500 Index (September 2022)

![](_page_277_Diagram_2.jpeg)

# 1. Earnings

| <i>Start of Month</i> | <i>Expected Earnings in 2022</i> | <i>% Change over prior month</i> | <i>% Change over start of year</i> | <i>Expected Earnings in 2023</i> | <i>% Change over prior month</i> | <i>% Change over start of year</i> |
|-----------------------|----------------------------------|----------------------------------|------------------------------------|----------------------------------|----------------------------------|------------------------------------|
| 01/01/22              | 223.34                           |                                  |                                    | 244.94                           |                                  |                                    |
| 02/01/22              | 223.78                           | 0.20%                            | 0.20%                              | 245.93                           | 0.40%                            | 0.40%                              |
| 03/01/22              | 225.43                           | 0.74%                            | 0.94%                              | 247.94                           | 0.82%                            | 1.22%                              |
| 04/01/22              | 227.3                            | 0.83%                            | 1.77%                              | 249.52                           | 0.64%                            | 1.87%                              |
| 05/01/22              | 227.29                           | 0.00%                            | 1.77%                              | 250.11                           | 0.24%                            | 2.11%                              |
| 06/01/22              | 228.03                           | 0.33%                            | 2.10%                              | 248.96                           | -0.46%                           | 1.64%                              |
| 07/01/22              | 229.57                           | 0.68%                            | 2.79%                              | 251.99                           | 1.22%                            | 2.88%                              |
| 08/01/22              | 228.27                           | -0.57%                           | 2.21%                              | 248.35                           | -1.44%                           | 1.39%                              |
| 09/01/22              | 225.36                           | -1.27%                           | 0.90%                              | 243.64                           | -1.90%                           | -0.53%                             |
| 09/20/22              | 225.34                           | -0.01%                           | 0.90%                              | 243.46                           | -0.07%                           | -0.60%                             |

# 2. Cash Return

|              | <i>Year</i> | <i>Earnings</i> | <i>Dividends</i> | <i>Buybacks</i> | <i>Dividend Payout</i> | <i>Cash Payout</i> |
|--------------|-------------|-----------------|------------------|-----------------|------------------------|--------------------|
|              | 2001        | 38.85           | 15.74            | 14.34           | 40.51%                 | 77.43%             |
|              | 2002        | 46.04           | 15.96            | 13.87           | 34.67%                 | 64.78%             |
|              | 2003        | 54.69           | 17.88            | 13.70           | 32.69%                 | 57.74%             |
|              | 2004        | 67.68           | 19.01            | 21.59           | 28.09%                 | 59.99%             |
|              | 2005        | 76.45           | 22.34            | 38.82           | 29.23%                 | 80.01%             |
|              | 2006        | 87.72           | 25.04            | 48.12           | 28.55%                 | 83.40%             |
|              | 2007        | 82.54           | 28.14            | 67.22           | 34.09%                 | 115.53%            |
|              | 2008        | 49.51           | 28.45            | 39.07           | 57.46%                 | 136.37%            |
|              | 2009        | 56.86           | 21.97            | 15.46           | 38.64%                 | 65.82%             |
|              | 2010        | 83.77           | 22.65            | 32.88           | 27.04%                 | 66.28%             |
|              | 2011        | 96.44           | 26.53            | 44.75           | 27.51%                 | 73.91%             |
|              | 2012        | 96.82           | 31.25            | 44.65           | 32.28%                 | 78.39%             |
|              | 2013        | 104.92          | 34.90            | 53.23           | 33.26%                 | 84.00%             |
|              | 2014        | 116.16          | 39.55            | 62.44           | 34.04%                 | 87.79%             |
|              | 2015        | 100.48          | 43.41            | 64.94           | 43.20%                 | 107.83%            |
|              | 2016        | 106.26          | 45.70            | 62.32           | 43.01%                 | 101.66%            |
|              | 2017        | 124.51          | 48.93            | 60.85           | 39.30%                 | 88.17%             |
|              | 2018        | 152.78          | 54.39            | 96.11           | 35.60%                 | 98.51%             |
|              | 2019        | 157.18          | 58.50            | 87.81           | 37.22%                 | 93.08%             |
|              | 2020        | 139.76          | 57.00            | 61.66           | 40.78%                 | 84.90%             |
|              | 2021        | 205.35          | 60.65            | 104.61          | 29.53%                 | 80.48%             |
| Average      |             |                 |                  |                 | 35.56%                 | 85.05%             |
| 1st Quartile |             |                 |                  |                 | 29.53%                 | 73.91%             |
| Median       |             |                 |                  |                 | 34.09%                 | 83.40%             |
| 3rd Quartile |             |                 |                  |                 | 39.30%                 | 93.08%             |

![](_page_279_Figure_4.jpeg)

# My S&P 500 Story

An Intrinsic (and Personal) Valuation of the S&P 500 on September 23, 2022

### My Earnings Estimates

Analysts are underestimating the effect of a recession on future earnings, and I am reducing their 2023 estimates by 15%, with ripple effects on earnings beyond. (I am leaving 2022 estimates untouched, because the bulk of the year is behind us.)

### Cash Return

While companies have collectively returned 90.5% of earnings as dividends and buybacks in the most recent 12 months, recession fears and uncertainty will lead them to reduce this cash returns to 80% of earnings (consistent with growth in long term), over time.

| Intrinsic Value Estimate (based on your choice of ERP) |                |          |          |          |          |             |        | Terminal Year |
|--------------------------------------------------------|----------------|----------|----------|----------|----------|-------------|--------|---------------|
|                                                        | 2021           | 2022     | 2023     | 2024     | 2025     | 2026        |        |               |
| Analyst Estimate of Earnings                           | 208.53         | 225.34   | 243.46   | 259.79   | 273.70   | 284.65      | 296.03 |               |
| My Estimate of Earnings                                | \$208.53       | 225.34   | 206.94   | 225.03   | 243.13   | 252.85      | 262.97 |               |
| Expected Earnings Growth Rate                          |                | 8.06%    | -8.16%   | 6.71%    | 5.35%    | 4.00%       | 4.00%  |               |
| Expected cash payout as % of earnings                  | 90.50%         | 90.50%   | 87.88%   | 85.25%   | 82.63%   | 80.00%      | 80.00% |               |
| Expected Dividends + Buybacks =                        | \$188.72       | \$203.93 | \$181.85 | \$191.84 | \$200.89 | \$202.28    | 210.37 |               |
| Expected Terminal Value =                              |                |          |          |          |          | \$ 4,207.49 |        |               |
| Riskfree Rate                                          | 3.69%          | 3.75%    | 3.81%    | 3.88%    | 3.94%    | 4.00%       | 4.00%  |               |
| Required Return on Stocks                              | 8.69%          | 8.75%    | 8.81%    | 8.88%    | 8.94%    | 9.00%       | 9.00%  |               |
| Present Value =                                        |                | \$187.52 | \$153.67 | \$148.90 | \$143.12 | \$2,882.41  |        |               |
| <b>Intrinsic Value of Index =</b>                      | <b>3515.63</b> |          |          |          |          |             |        |               |
| <b>Actual Index level =</b>                            | <b>3693.23</b> |          |          |          |          |             |        |               |
| <b>% Under or Over Valuation =</b>                     | <b>-4.81%</b>  |          |          |          |          |             |        |               |

### Ten-year Treasury Bond Rate

I will assume that the bulk of the rise in rates has already occurred, and that the T.Bond rate will converge to 4%, over the next five years.

### Equity Risk Premium

The equity risk premium is 5%, close to both the historical average risk premium earned on stocks from 1928 - 2022 and the average implied equity risk premium over the last decade. Adding it to the ten-year bond rate yields the required return on stocks.

*In my overarching story for equities, I am building in the assumption that there will be a recession that creates both short term & long term damage to corporate earnings, but helps in restraining inflation, bringing it down from 2022 levels to about 3% in the long term (above the 2011-2021 average of 1.73%).*

# What if?

|                                                                                |         | Valuing the S&P 500 on Sept 23, 2022  |         |         |                                       |         |         |                             |         |  |
|--------------------------------------------------------------------------------|---------|---------------------------------------|---------|---------|---------------------------------------|---------|---------|-----------------------------|---------|--|
|                                                                                |         | <i>Earnings = 30% below Estimates</i> |         |         | <i>Earnings = 15% below Estimates</i> |         |         | <i>Earnings = Estimates</i> |         |  |
| Riskfree Rate                                                                  | ERP =4% | ERP =5%                               | ERP =6% | ERP =4% | ERP =5%                               | ERP =6% | ERP =4% | ERP =5%                     | ERP =6% |  |
| <b>2%</b>                                                                      | 4276    | 3416                                  | 2842    | 4677    | 3737                                  | 3110    | 5449    | 4348                        | 3615    |  |
| <b>3%</b>                                                                      | 4132    | 3303                                  | 2750    | 4519    | 3613                                  | 3009    | 5169    | 4129                        | 3436    |  |
| <b>4%</b>                                                                      | 3979    | 3183                                  | 2653    | 4352    | 3482                                  | 2903    | 4889    | 3910                        | 3257    |  |
| <b>5%</b>                                                                      | 3819    | 3058                                  | 2551    | 4176    | 3345                                  | 2790    | 4609    | 3690                        | 3078    |  |
| <b>6%</b>                                                                      | 3650    | 2926                                  | 2443    | 3991    | 3200                                  | 2672    | 4328    | 3471                        | 2899    |  |
| <i>Index was trading at 3693 on 9/23/22. Shaded cells are higher than 3693</i> |         |                                       |         |         |                                       |         |         |                             |         |  |

Anyone can value a company that is stable, makes money and has an established business model!

# **<sup>283</sup>** The Dark Side of Valuation

# The fundamental determinants of value…

What are the **cashflows from existing assets**? - Equity: Cashflows after debt payments - Firm: Cashflows before debt payments What is the **value added** by growth assets? Equity: Growth in equity earnings/ cashflows Firm: Growth in operating earnings/ cashflows

How **risky are the cash flows** from both existing assets and growth assets? Equity: Risk in equity in the company Firm: Risk in the firm's operations

When will the firm become a **mature fiirm**, and what are the potential roadblocks?

# The Dark Side of Valuation…

¨ Valuing stable, money making companies with consistent and clear accounting statements, a long and stable history and lots of comparable firms is easy to do. ¨ The true test of your valuation skills is when you have to value "difficult" companies. In particular, the challenges are greatest when valuing: ¤ Young companies, early in the life cycle, in young businesses ¤ Companies that don't fit the accounting mold ¤ Companies that face substantial truncation risk (default or nationalization risk)

# Difficult to value companies…

## ¨ Across the life cycle:

¤ Young, growth firms: Limited history, small revenues in conjunction with big operating losses and a propensity for failure make these companies tough to value. ¤ Mature companies in transition: When mature companies change or are forced to change, history may have to be abandoned and parameters have to be reestimated. ¤ Declining and Distressed firms: A long but irrelevant history, declining markets, high debt loads and the likelihood of distress make them troublesome.

## ¨ Across markets

¤ Emerging market companies are often difficult to value because of the way they are structured, their exposure to country risk and poor corporate governance.

## ¨ Across sectors

¤ Financial service firms: Opacity of financial statements and difficulties in estimating basic inputs leave us trusting managers to tell us what's going on. ¤ Commodity and cyclical firms: Dependence of the underlying commodity prices or overall economic growth make these valuations susceptible to macro factors. ¤ Firms with intangible assets: Accounting principles are left to the wayside on these firms.

# I. The challenge with young companies...

287

*Making judgments on revenues/ profits difficult because you cannot draw on history. If you have no product/ service, it is difficult to gauge market potential or profitability. The company;s entire value lies in future growth but you have little to base your estimate on.*

![](_page_286_Diagram_17.jpeg)

## Upping the ante.. Young companies in young businesses…

¨ When valuing a business, we generally draw on three sources of information ¤ The firm's current financial statement <sup>n</sup> How much did the firm sell? <sup>n</sup> How much did it earn? ¤ The firm's financial history, usually summarized in its financial statements. <sup>n</sup> How fast have the firm's revenues and earnings grown over time? <sup>n</sup> What can we learn about cost structure and profitability from these trends? <sup>n</sup> Susceptibility to macro-economic factors (recessions and cyclical firms) ¤ The industry and comparable firm data <sup>n</sup> What happens to firms as they mature? (Margins.. Revenue growth… Reinvestment needs… Risk) ¨ It is when valuing these companies that you find yourself tempted by the dark side, where ¤ "Paradigm shifts" happen… ¤ New metrics are invented … ¤ The story dominates and the numbers lag…

**Amazon in January 2000**

![](_page_288_Diagram_37.jpeg)

*Sales to capital ratio and expected margin are retail industry average numbers*

![](_page_288_Diagram_39.jpeg)

Terminal Value=  $1881/(.0961-.06) = 52,148$ 

| Value of Op Assets | \$ 15,170 |
|--------------------|-----------|
| + Cash             | \$ 26     |
| = Value of Firm    | \$14,936  |
| - Value of Debt    | \$ 349    |
| = Value of Equity  | \$14,847  |
| - Equity Options   | \$ 2,892  |
| Value per share    | \$ 35.08  |

| Revenue Growth   | 150.00%  | 100.00%  | 75.00%   | 50.00%    | 30.00%    | 25.20%    | 20.40%    | 15.60%    | 10.80%    | 6.00%     |
|------------------|----------|----------|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Revenues         | \$ 2,793 | \$ 5,585 | \$ 9,774 | \$ 14,661 | \$ 19,059 | \$ 23,862 | \$ 28,729 | \$ 33,211 | \$ 36,798 | \$ 39,006 |
| Operating Margin | -13.35%  | -1.68%   | 4.16%    | 7.08%     | 8.54%     | 9.27%     | 9.64%     | 9.82%     | 9.91%     | 9.95%     |
| EBIT             | -\$373   | -\$94    | \$407    | \$1,038   | \$1,628   | \$2,212   | \$2,768   | \$3,261   | \$3,646   | \$3,883   |
| EBIT(1-t)        | -\$373   | -\$94    | \$407    | \$871     | \$1,058   | \$1,438   | \$1,799   | \$2,119   | \$2,370   | \$2,524   |
| - Reinvestment   | \$600    | \$967    | \$1,420  | \$1,663   | \$1,543   | \$1,688   | \$1,721   | \$1,619   | \$1,363   | \$961     |
| FCFF             | -\$931   | -\$1,024 | -\$989   | -\$758    | -\$408    | -\$163    | \$177     | \$625     | \$1,174   | \$1,788   |
|                  | 1        | 2        | 3        | 4         | 5         | 6         | 7         | 8         | 9         | 10        |

| Term. Year |
|------------|
| 6%         |
| \$ 41,346  |
| 10.00%     |
| \$4,135    |
| \$2,688    |
| \$155      |
| \$1,881    |

Forever

*All existing options valued as options, using current stock price of \$84.*

|                        | 12.90% | 12.90% | 12.90% | 12.90% | 12.90% | 12.42% | 11.94% | 11.46% | 10.98% | 10.50% |
|------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Cost of Equity         | 8.00%  | 8.00%  | 8.00%  | 8.00%  | 8.00%  | 7.80%  | 7.75%  | 7.67%  | 7.50%  | 7.00%  |
| Cost of Debt           | 8.00%  | 8.00%  | 8.00%  | 8.00%  | 8.00%  | 7.80%  | 7.75%  | 7.67%  | 7.50%  | 7.00%  |
| After-tax cost of debt | 8.00%  | 8.00%  | 8.00%  | 6.71%  | 5.20%  | 5.07%  | 5.04%  | 4.98%  | 4.88%  | 4.55%  |
| Cost of Capital        | 12.84% | 12.84% | 12.84% | 12.83% | 12.81% | 12.13% | 11.62% | 11.08% | 10.49% | 9.61%  |

Amazon was trading at \$84 in January 2000.

**Cost of Equity**  
12.90%

*Used average interest coverage ratio over next 5 years to get BBB rating.*

**Cost of Debt**  
6.5%+1.5%=8.0%  
Tax rate = 0% -> 35%

**Weights**  
Debt= 1.2% -> 15%

*Pushed debt ratio to retail industry average of 15%.*

*Dot.com retailers for first 5 years  
Conventional retailers after year 5*

![](_page_288_Diagram_54.jpeg)

# Lesson 1: Don't sweat the small stuff

![](_page_289_Figure_1.jpeg)

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

![](_page_291_Figure_41.jpeg)

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

¨ With young growth companies, it is almost a given that the number of shares outstanding will increase over time for two reasons: ¤ To grow, the company will have to issue new shares either to raise cash to take projects or to offer to target company stockholders in acquisitions ¤ Many young, growth companies also offer options to managers as compensation and these options will get exercised, if the company is successful. ¨ Both effects are already incorporated into the value per share, even though we use the current number of shares in estimating value per share ¤ The need for new equity issues is captured in negative cash flows in the earlier years. The present value of these negative cash flows will drag down the current value of equity and this is the effect of future dilution. In the Amazon valuation, the value of equity is reduced by \$3.09 billion (the present value of negative FCFF in the first 6 years), about a 16% reduction. That takes care of new issues in the future. ¤ The existing options are valued and netted out against the current value, taking care of the option overhang. The future earnings are after stock based compensation expenses (don't fall for the "its not a cash expense" ploy) to take care of future option grants.

# Lesson 6: If you are worried about failure, incorporate into value

![](_page_294_Figure_1.jpeg)

# A 2019 Update: Sector Comparison

296

## Sectors with highest and lowest annual survival rate, compared to all sectors

### Management of companies and enterprises

![](_page_295_Figure_22.jpeg)

### Utilities

![](_page_295_Figure_24.jpeg)

### Health care and social assistance

![](_page_295_Figure_26.jpeg)

### Information

![](_page_295_Figure_28.jpeg)

### Transportation and warehousing

![](_page_295_Figure_30.jpeg)

### Wholesale trade

![](_page_295_Figure_32.jpeg)

Source: Bureau of Labor Statistics, Business Employment Dynamics data

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

# Lesson 8: You will be wrong 100% of the time and it really is not your fault…

¨ No matter how careful you are in getting your inputs and how well structured your model is, your estimate of value will change both as new information comes out about the company, the business and the economy. ¨ As information comes out, you will have to adjust and adapt your model to reflect the information. Rather than be defensive about the resulting changes in value, recognize that this is the essence of risk. ¨ A test: If your valuations are unbiased, you should find yourself increasing estimated values as often as you are decreasing values. In other words, there should be equal doses of good and bad news affecting valuations (at least over time).

And the market is often "more wrong"….

![](_page_298_Figure_2.jpeg)

## **Amazon: Value and Price**

# Assessing my 2000 forecasts, in 2014

| Year       | Revenues           |          | Operating Income   |             | Operating Margin   |         |
|------------|--------------------|----------|--------------------|-------------|--------------------|---------|
|            | My forecast (2000) | Actual   | My forecast (2000) | Actual      | My forecast (2000) | Actual  |
| 2000       | \$2,793            | \$2,762  | -\$ 373            | -\$ 664.00  | -13.35%            | -24.04% |
| 2001       | \$5,585            | \$3,122  | -\$ 94             | -\$ 231.00  | -1.68%             | -7.40%  |
| 2002       | \$9,774            | \$3,932  | \$ 407             | \$ 106.00   | 4.16%              | 2.70%   |
| 2003       | \$14,661           | \$5,264  | \$ 1,038           | \$ 271.00   | 7.08%              | 5.15%   |
| 2004       | \$19,059           | \$6,921  | \$ 1,628           | \$ 440.00   | 8.54%              | 6.36%   |
| 2005       | \$23,862           | \$8,490  | \$ 2,212           | \$ 432.00   | 9.27%              | 5.09%   |
| 2006       | \$28,729           | \$10,711 | \$ 2,768           | \$ 389.00   | 9.63%              | 3.63%   |
| 2007       | \$33,211           | \$14,835 | \$ 3,261           | \$ 655.00   | 9.82%              | 4.42%   |
| 2008       | \$36,798           | \$19,166 | \$ 3,646           | \$ 842.00   | 9.91%              | 4.39%   |
| 2009       | \$39,006           | \$24,509 | \$ 3,883           | \$ 1,129.00 | 9.95%              | 4.61%   |
| 2010       | \$41,346           | \$34,204 | \$ 4,135           | \$ 1,406.00 | 10.00%             | 4.11%   |
| 2011       | \$43,827           | \$48,077 | \$ 4,383           | \$ 862.00   | 10.00%             | 1.79%   |
| 2012       | \$46,457           | \$61,093 | \$ 4,646           | \$ 676.00   | 10.00%             | 1.11%   |
| 2013       | \$49,244           | \$74,452 | \$ 4,925           | \$ 745.00   | 10.00%             | 1.00%   |
| 2014 (LTM) | \$51,460           | \$85,247 | \$ 5,146.35        | \$ 97.00    | 10.00%             | 0.11%   |

Amazon will complete its metaphorisis from being a retail company to one that can take its competitive advantages - access to capital & willingness to lose money for long periods, while disrupting and changing the status quo - to any business that it targets, giving it the potential for high revenue growth on top of already-large revenues. It will be able to use the pricing power it accumulates in each business it is in, to increase profit margins, partly through economies of scale and partly through higher prices. Its low debt ratio and divergent business mix give it a low cost of capital.

**The Assumptions**

|                      | Base year  | Years 1-5                   | Years 6-10 |       | After year 10 | Link to story                                         |
|----------------------|------------|-----------------------------|------------|-------|---------------|-------------------------------------------------------|
| Revenues (a)         | \$ 208,125 | 15.00% → → 3.00%            |            |       | 3.00%         | Expanding into new businesses                         |
| Operating margin (b) | 7.71%      | 7.71% → → 12.50%            |            |       | 12.50%        | Economies of scale and pricing power increase margins |
| Tax rate             | 20.20%     | 20.20% → → 24.00%           |            |       | 24.00%        | Converging on a global tax rate of 25%                |
| Reinvestment (c )    |            | Sales to capital ratio 5.95 |            | RIR = | 30.00%        | Big payoffs from investing in technology and content  |
| Return on capital    | 15.24%     | Marginal ROIC = 89.16%      |            |       | 10.00%        | The last man standing...                              |
| Cost of capital (d)  |            | 7.97% → → 7.50%             |            |       | 7.50%         | Low debt & diverse business mix                       |

**The Cash Flows**

|               | Revenues   | Operating Margin | EBIT      | EBIT (1-t) | Reinvestment | FCFF      |
|---------------|------------|------------------|-----------|------------|--------------|-----------|
| 1             | \$ 239,344 | 8.67%            | \$ 20,753 | \$ 16,560  | \$ 5,249     | \$ 11,311 |
| 2             | \$ 275,245 | 9.63%            | \$ 26,501 | \$ 21,147  | \$ 6,037     | \$ 15,110 |
| 3             | \$ 316,532 | 10.59%           | \$ 33,506 | \$ 26,736  | \$ 6,942     | \$ 19,794 |
| 4             | \$ 364,012 | 11.54%           | \$ 42,017 | \$ 33,527  | \$ 7,983     | \$ 25,544 |
| 5             | \$ 418,614 | 12.50%           | \$ 52,327 | \$ 41,754  | \$ 9,181     | \$ 32,573 |
| 6             | \$ 471,359 | 12.50%           | \$ 58,920 | \$ 46,568  | \$ 8,869     | \$ 37,699 |
| 7             | \$ 519,438 | 12.50%           | \$ 64,930 | \$ 50,825  | \$ 8,084     | \$ 42,741 |
| 8             | \$ 559,954 | 12.50%           | \$ 69,994 | \$ 54,258  | \$ 6,813     | \$ 47,446 |
| 9             | \$ 590,191 | 12.50%           | \$ 73,774 | \$ 56,628  | \$ 5,084     | \$ 51,544 |
| 10            | \$ 607,897 | 12.50%           | \$ 75,987 | \$ 57,750  | \$ 2,977     | \$ 54,773 |
| Terminal year | \$ 626,134 | 12.50%           | \$ 78,267 | \$ 59,483  | \$ 17,845    | \$ 41,638 |

**The Value**

| Terminal value                      | \$ 925,287  |  |  |                                   |  |  |
|-------------------------------------|-------------|--|--|-----------------------------------|--|--|
| PV(Terminal value)                  | \$ 435,438  |  |  |                                   |  |  |
| PV (CF over next 10 years)          | \$ 206,707  |  |  |                                   |  |  |
| Value of operating assets =         | \$ 642,144  |  |  |                                   |  |  |
| Adjustment for distress             | \$ -        |  |  | Probability of failure = 0.00%    |  |  |
| - Debt & Mnority Interests          | \$ 45,435   |  |  |                                   |  |  |
| + Cash & Other Non-operating assets | \$ 27,050   |  |  |                                   |  |  |
| Value of equity                     | \$ 623,759  |  |  |                                   |  |  |
| - Value of equity options           | \$ -        |  |  |                                   |  |  |
| Number of shares                    | 497.00      |  |  |                                   |  |  |
| Value per share                     | \$ 1,255.05 |  |  | Stock was trading at = \$1,970.19 |  |  |

# II. Mature Companies in transition..

¨ Mature companies are generally the easiest group to value. They have long, established histories that can be mined for inputs. They have investment policies that are set and capital structures that are stable, thus making valuation more grounded in past data. ¨ However, this stability in the numbers can mask real problems at the company. The company may be set in a process, where it invests more or less than it should and does not have the right financing mix. In effect, the policies are consistent, stable and bad. ¨ If you expect these companies to change or as is more often the case to have change thrust upon them,

# The perils of valuing mature companies...

303

*Lots of historical data on earnings and cashflows. Key questions remain if these numbers are volatile over time or if the existing assets are not being efficiently utilized.*

*Growth is usually not very high, but firms may still be generating healthy returns on investments, relative to cost of funding. Questions include how long they can generate these excess returns and with what growth rate in operations. Restructuring can change both inputs dramatically and some firms maintain high growth through acquisitions.*

What is the value added by growth assets?

What are the cashflows from existing assets?

*Equity claims can vary in voting rights and dividends.*

What is the value of equity in the firm?

How risky are the cash flows from both existing assets and growth assets?

*Operating risk should be stable, but the firm can change its financial leverage This can affect both the cost of equity and capital.*

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Maintaining excess returns or high growth for any length of time is difficult to do for a mature firm.*

## *Hormel Foods: The Value of Control Changing*

Hormel Foods sells packaged meat and other food products and has been in existence as a publicly traded company for almost 80 years.

In 2008, the firm reported after-tax operating income of \$315 million, reflecting a compounded growth of 5% over the previous 5 years.

## *The Status Quo*

Run by existing management, with conservative reinvestment policies (reinvestment rate = 14.34% and debt ratio = 10.4%.

## *New and better management*

More aggressive reinvestment which increases the reinvestment rate (to 40%) and tlength of growth (to 5 years), and higher debt ratio (20%).

## **Operating Restructuring** 1

Expected growth rate = ROC \* Reinvestment Rate

Expected growth rae (status quo) = 14.34% \* 19.14% = 2.75%

Expected growth rate (optimal) = 14.00% \* 40% = 5.60%

ROC drops, reinvestment rises and growth goes up.

## **Financial restructuring** 2

Cost of capital = Cost of equity (1-Debt ratio) + Cost of debt (Debt ratio)

Status quo = 7.33% (1-.104) + 3.60% (1-.40) (.104) = 6.79%

Optimal = 7.75% (1-.20) + 3.60% (1-.40) (.20) = 6.63%

Cost of equity rises but cost of capital drops.

Anemic growth rate and short growth period, due to reinvestment policy Low debt ratio affects cost of capital

| Year                            | Operating income after taxes | Expected growth rate | ROC    | Reinvestment Rate | Reinvestment | FCFF    | Cost of capital | Present Value |
|---------------------------------|------------------------------|----------------------|--------|-------------------|--------------|---------|-----------------|---------------|
| Trailing 12 months              | \$315                        |                      |        |                   |              |         |                 |               |
| 1                               | \$324                        | 2.75%                | 14.34% | 19.14%            | \$62         | \$262   | 6.79%           | \$245         |
| 2                               | \$333                        | 2.75%                | 14.34% | 19.14%            | \$64         | \$269   | 6.79%           | \$236         |
| 3                               | \$342                        | 2.75%                | 14.34% | 19.14%            | \$65         | \$276   | 6.79%           | \$227         |
| Beyond                          | \$350                        | 2.35%                | 7.23%  | 32.52%            | \$114        | \$4,840 | 7.23%           | \$3,974       |
| Value of operating assets       |                              |                      |        |                   |              |         |                 | \$4,682       |
| (Add) Cash                      |                              |                      |        |                   |              |         |                 | \$155         |
| (Subtract) Debt                 |                              |                      |        |                   |              |         |                 | \$491         |
| (Subtract) Management Options   |                              |                      |        |                   |              |         |                 | \$53          |
| Value of equity in common stock |                              |                      |        |                   |              |         |                 | \$4,293       |
| Value per share                 |                              |                      |        |                   |              |         |                 | \$31.91       |

Expected value =\$31.91 (.90) + \$37.80 (.10) = \$32.50Probability of management change = 10%3

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
| Value per Asset                 |                              |                      |        |                   |              |         |                 |               | \$37.80 |

## Financial leverage is a double-edged sword..

*Exhibit 7.1: Optimal Financing Mix: Hormel Foods in January 2009*

![](_page_304_Figure_3.jpeg)

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

| Bed, Bath & Beyond                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |            |                  |            | Sep-2      |                          |                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------|------------|------------|--------------------------|--------------------------------------------------------------------------|
| Incredible Shrinking Store                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  |            |            |                          |                                                                          |
| Bed Bath and Beyond is in a downward spiral, but we see a glimmer of hope, where the company shuts stores that require the most capital and get the least foot traffic over the next decade, shrinking already-shrunk revenues further, but seeing its operating margins improve to the US brick-and-mortar sector average margin, over the next five years. Along the way, the divestitures and shut downs will relase cash that can be returned and used to pay down debt. By the end of the forecast period, BB&B finds a niche market, albeit with a smaller footprint, growing at the same rate as the economy and earning no excess returns.. |            |                  |            |            |                          |                                                                          |
| The Assumptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |                  |            |            |                          |                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Base year  | Next year        | Years 2-5  | Years 6-10 | After year 10            | Link to story                                                            |
| Revenues (a)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \$7,868.00 | -10.0%           | -5.00%     | 3.00%      | 3.00%                    | Disruption platform in multiple businesses                               |
| Operating margin (b)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | -1.00%     | -1.0%            | -1.00%     | 5.54%      | 5.54%                    | Margins improve, aided by cloud business & continued economies of scale. |
| Tax rate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 25.00%     |                  | 25.00%     | 25.00%     | 25.00%                   | Global/US marginal tax rate over time                                    |
| Reinvestment (c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |            | 2.00             | 2.00       | 2.00       | 30.00%                   | Maintined at Amazon's current level                                      |
| Return on capital                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | -2.80%     | Marginal ROIC =  | -57.31%    |            | 10.00%                   | Stronge competitive edges                                                |
| Cost of capital (d)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |            |                  | 8.79%      | 7.50%      | 7.50%                    | Cost of capital close to median company                                  |
| The Cash Flows                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |            |                  |            |            |                          |                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Revenues   | Operating Margin | EBIT       | EBIT (1-t) | Reinvestment             | FCFF                                                                     |
| 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$7,081.20 | -1.00%           | -\$70.81   | -\$70.81   | \$0.00                   | -\$70.81                                                                 |
| 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$6,727.14 | 1.62%            | \$108.72   | \$108.72   | -\$177.03                | \$285.75                                                                 |
| 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$6,390.78 | 2.92%            | \$186.89   | \$186.89   | -\$168.18                | \$355.06                                                                 |
| 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$6,071.24 | 4.23%            | \$256.96   | \$256.96   | -\$159.77                | \$416.73                                                                 |
| 5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$5,767.68 | 5.54%            | \$319.56   | \$244.23   | -\$151.78                | \$396.01                                                                 |
| 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$5,571.58 | 5.54%            | \$308.69   | \$231.52   | -\$98.05                 | \$329.57                                                                 |
| 7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$5,471.29 | 5.54%            | \$303.14   | \$227.35   | -\$50.14                 | \$277.50                                                                 |
| 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$5,460.35 | 5.54%            | \$302.53   | \$226.90   | -\$5.47                  | \$232.37                                                                 |
| 9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$5,536.79 | 5.54%            | \$306.77   | \$230.07   | \$38.22                  | \$191.85                                                                 |
| 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | \$5,702.90 | 5.54%            | \$315.97   | \$236.98   | \$83.05                  | \$153.92                                                                 |
| Terminal year                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | \$5,873.99 | 5.54%            | \$325.45   | \$244.09   | \$73.23                  | \$170.86                                                                 |
| The Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |                  |            |            |                          |                                                                          |
| Terminal value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |            |                  | \$3,796.89 |            |                          |                                                                          |
| PV(Terminal value)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |            |                  | \$1,695.10 |            |                          |                                                                          |
| PV (CF over next 10 years)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |            |                  | \$1,644.97 |            |                          |                                                                          |
| Value of operating assets =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |            |                  | \$3,340.07 |            |                          |                                                                          |
| Adjustment for distress                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |            |                  | \$396.47   |            | Probability of failure = | 23.74%                                                                   |
| - Debt & Minority Interests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |            |                  | \$3,085.00 |            |                          |                                                                          |
| + Cash & Other Non-operating assets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |            |                  | \$440.00   |            |                          |                                                                          |
| Value of equity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |                  | \$298.60   |            |                          |                                                                          |
| - Value of equity options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |            |                  | \$0.00     |            |                          |                                                                          |
| Number of shares                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |            |                  | 92.50      |            |                          |                                                                          |
| Value per share                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            |                  | \$3.23     |            | Stock was trading at =   | \$8.79                                                                   |

# b. Dealing with the "downside" of Distress

¨ A DCF valuation values a firm as a going concern. If there is a significant likelihood of the firm failing before it reaches stable growth and if the assets will then be sold for a value less than the present value of the expected cashflows (a distress sale value), DCF valuations will overstate the value of the firm. ¨ Value of Equity= DCF value of equity (1 - Probability of distress) + Distress sale value of equity (Probability of distress) ¨ There are three ways in which we can estimate the probability of distress: ¤ Use the bond rating to estimate the cumulative probability of distress over 10 years ¤ Estimate the probability of distress with a probit ¤ Estimate the probability of distress by looking at market value of bonds.. ¨ The distress sale value of equity is usually best estimated as a percent of book value (and this value will be lower if the economy is doing badly and there are other firms in the same business also in distress).

![](_page_309_Diagram_0.jpeg)

# Adjusting the value of LVS for distress..

¨ Ratings based approach: In February 2009, Las Vegas Sands was rated B+, and based upon history (previous ten years), the likelihood of default is 28.25%. ¨ Bond Price based: In February 2009, LVS was rated B+ by S&P. Historically, 28.25% of B+ rated bonds default within 10 years. LVS has a 6.375% bond, maturing in February 2015 (7 years), trading at \$529. If we discount the expected cash flows on the bond at the riskfree rate, we can back out the probability of distress from the bond price:

$$\pi_{\text{Distress}} = \text{Annual probability of default} = 13.54\%$$

Cumulative probability of surviving 10 years = 
$$(1 - .1354)^{10} = 23.34\%$$

Cumulative probability of distress over 10 years = 1 - .2334 = .7666 or 76.66% €

¨ If LVS is becomes distressed: ¤ Expected distress sale proceeds = \$2,769 million < Face value of debt ¤ Expected equity value/share = \$0.00 ¨ Expected value per share ¨ With ratings-based approach: \$8.12 (.7175) + \$ 0 (.2825) = \$5.83 ¨ With bond-based approach: \$8.12 (1 - .7666) + \$0.00 (.7666) = \$1.92

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

## *Estimation Issues - Emerging Market Companies*

What is the value of equity in the firm?

*Cross holdings can affect value of equity*

## Lesson 1: Country risk has to be incorporated… but with a scalpel, not a bludgeon

¨ Emerging market companies are undoubtedly exposed to additional country risk because they are incorporated in countries that are more exposed to political and economic risk. ¨ Not all emerging market companies are equally exposed to country risk and many developed markets have emerging market risk exposure because of their operations. ¨ You can use either the "weighted country risk premium", with the weights reflecting the countries you get your revenues from or the lambda approach (which may incorporate more than revenues) to capture country risk exposure.

# Lesson 2: Currency should not matter

¨ You can value any company in any currency. Thus, you can value a Brazilian company in nominal reais, US dollars or Swiss Francs. ¨ For your valuation to stay invariant and consistent, your cash flows and discount rates have to be in the same currency. Thus, if you are using a high inflation currency, both your growth rates and discount rates will be much higher. ¨ For your cash flows to be consistent, you have to use expected exchange rates that reflect purchasing power parity (the higher inflation currency has to depreciate by the inflation differential each year).

# Valuing Infosys: In US\$ and Indian Rupees

|                         | In Indian Rupees | In US \$                                                |
|-------------------------|------------------|---------------------------------------------------------|
| Risk free Rate          | 5.00%            | 2.00%                                                   |
| Expected inflation rate | 4.00%            | 1.00%                                                   |
| Cost of capital         |                  |                                                         |
| - High Growth           | 12.50%           | 9.25%                                                   |
| - Stable Growth         | 10.39%           | 7.21%                                                   |
| Expected growth rate    |                  |                                                         |
| - High Growth           | 12.01%           | 8.78%                                                   |
| - Stable Growth         | 5.00%            | 2.00%                                                   |
| Return on Capital       |                  |                                                         |
| - High Growth           | 17.16%           | 13.78%                                                  |
| - Stable Growth         | 10.39%           | 7.21%                                                   |
| Value per share         | Rs 614           | \$12.79/share (roughly Rs 614 at current exchange rate) |

## Lesson 3: The "corporate governance" drag

- ¨ Stockholders in Asian, Latin American and many European companies have little or no power over the managers of the firm. In many cases, insiders own voting shares and control the firm and the potential for conflict of interests is huge. ¨ This weak corporate governance is often a reason for given for using higher discount rates or discounting the estimated value for these companies. ¨ Would you discount the value that you estimate for an emerging market company to allow for this absence of stockholder power?
- a. Yes
- b. No.

![](_page_316_Diagram_1.jpeg)

# Lesson 4: Watch out for cross holdings…

¨ Emerging market companies are more prone to having cross holdings that companies in developed markets. ¤ This is partially the result of history (since many of the larger public companies used to be family owned businesses until a few decades ago) ¤ And partly because those who run these companies value control (and use cross holdings to preserve this control). ¨ In many emerging market companies, the real process of valuation begins when you have finished your DCF valuation, since the cross holdings (which can be numerous) have to be valued, often with minimal information.

# Tata Companies in 2010: Value Breakdown

![](_page_318_Figure_2.jpeg)

## Lesson 5: Truncation risk can come in many forms…

¨ Natural disasters: Small companies in some economies are much exposed to natural disasters (hurricanes, earthquakes), without the means to hedge against that risk (with insurance or derivative products). ¨ Terrorism risk: Companies in some countries that are unstable or in the grips of civil war are exposed to damage or destruction. ¨ Nationalization risk: While less common than it used to be, there are countries where businesses may be nationalized, with owners receiving less than fair value as compensation.

# Valuing Aramco: Potential Dividends

## A Potential Dividend (FCFE) Discount Model Valuation of Aramco

![](_page_320_Diagram_6.jpeg)

# Adjusting for regime change

¨ If you believe that there is no chance of regime change, your expected value will remain \$1.65 trillion. ¨ If you believe that regime change is imminent, and that your equity will be fully expropriated, your expected value will be zero. ¨ If you believe that there remains a non-trivial chance (perhaps as high as 20%) that there will be a regime change and that if there is one, there will be changes that reduce, but not extinguish, your equity claim:

| House of Saud rules                                                                                                                         |                                                                                                                                  | Regime Change                                                                                                  |  |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--|
| $  \begin{aligned}  \text{Expected Value of Aramco Equity} \\  = \$1.65 (.8) + \$.825 (.2) \\  = \$1.485 \text{ trillion}  \end{aligned}  $ | $  \begin{aligned}  \text{Value of equity} \\  \text{DCF Value of Aramco Equity} \\  = \$1.65 \text{ trillion}  \end{aligned}  $ | $  \begin{aligned}  \text{DCF with higher royalties \& taxes} \\  = \$0.825 \text{ trillion}  \end{aligned}  $ |  |
|                                                                                                                                             | $  \begin{aligned}  \text{X} \\  \text{Probability of political status quo} \\  80\%  \end{aligned}  $                           | $  \begin{aligned}  \text{X} \\  \text{Probability of regime change} \\  20\%  \end{aligned}  $                |  |

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

# CIB Egypt in December 2015 Valuation in Egyptian Pounds

![](_page_323_Diagram_22.jpeg)

## Lesson 1: Financial service companies are opaque…

¨ With financial service firms, we enter into a Faustian bargain. They tell us very little about the quality of their assets (loans, for a bank, for instance are not broken down by default risk status) but we accept that in return for assets being marked to market (by accountants who presumably have access to the information that we don't have). ¨ In addition, estimating cash flows for a financial service firm is difficult to do. So, we trust financial service firms to pay out their cash flows as dividends. Hence, the use of the dividend discount model. ¨ During times of crises or when you don't trust banks to pay out what they can afford to in dividends, using the dividend discount model may not give you a "reliable" value.

## Lesson 2: For financial service companies, book value matters…

¨ The book value of assets and equity is mostly irrelevant when valuing non-financial service companies. After all, the book value of equity is a historical figure and can be nonsensical. (The book value of equity can be negative and is so for more than a 1000 publicly traded US companies) ¨ With financial service firms, book value of equity is relevant for two reasons: ¤ Since financial service firms mark to market, the book value is more likely to reflect what the firms own right now (rather than a historical value) ¤ The regulatory capital ratios are based on book equity. Thus, a bank with negative or even low book equity will be shut down by the regulators. ¨ From a valuation perspective, it therefore makes sense to pay heed to book value. In fact, you can argue that reinvestment for a bank is the amount that it needs to add to book equity to sustain its growth ambitions and safety requirements: ¤ FCFE = Net Income – Reinvestment in regulatory capital (book equity)

## Deutsche Bank: A Crisis Valuation (October 2016)

Risk adjusted assets grows at inflation rate of 1% a year forever.

Tier 1 capital ratio increases to 15.67%, the 75th percentile for all banks

Expected DOJ fine of \$10 billions lower Tier 1 capital today

Common Equity increases in tandem with Tier 1 capital

Cost of equity starts at 10.2% (75th percentile of banks) & decreases after year 5 to 9.44% (median across banks).

|                                                              | Current     | 1           | 2          | 3          | 4          | 5          | 6          | 7          | 8          | 9          | 10         |
|--------------------------------------------------------------|-------------|-------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| Risk Adjusted Assets                                         | \$ 445,570  | \$ 450,026  | \$ 454,526 | \$ 459,071 | \$ 463,662 | \$ 468,299 | \$ 472,982 | \$ 477,711 | \$ 482,488 | \$ 487,313 | \$ 492,186 |
| Tier 1 Capital Ratio                                         | 12.41%      | 13.74%      | 13.95%     | 14.17%     | 14.38%     | 14.60%     | 14.81%     | 15.03%     | 15.24%     | 15.46%     | 15.67%     |
| Tier 1 Capital (Risk Adjusted Assets * Tier 1 capital today) | \$55,282    | \$61,834    | \$63,427   | \$65,045   | \$66,690   | \$68,361   | \$70,059   | \$71,784   | \$73,537   | \$75,317   | \$77,126   |
| Change in regulatory capital (Tier 1)                        |             | \$6,552     | \$1,593    | \$1,619    | \$1,645    | \$1,671    | \$1,698    | \$1,725    | \$1,753    | \$1,780    | \$1,809    |
| Book Equity                                                  | \$64,609    | \$71,161    | \$72,754   | \$74,372   | \$76,017   | \$77,688   | \$79,386   | \$81,111   | \$82,864   | \$84,644   | \$86,453   |
| Expected ROE                                                 | -13.70%     | -7.18%      | -2.84%     | 0.06%      | 1.99%      | 5.85%      | 6.568%     | 7.286%     | 8.004%     | 8.722%     | 9.440%     |
| Net Income (Book Equity * ROE)                               | \$ (8,851)  | \$ (5,111)  | \$ (2,065) | \$ 43      | \$ 1,512   | \$ 4,545   | \$ 5,214   | \$ 5,910   | \$ 6,632   | \$ 7,383   | \$ 8,161   |
| - Investment in Regulatory Capital                           |             | \$ 6,552    | \$ 1,593   | \$ 1,619   | \$ 1,645   | \$ 1,671   | \$ 1,698   | \$ 1,725   | \$ 1,753   | \$ 1,780   | \$ 1,809   |
| FCFE                                                         |             | \$ (11,663) | \$ (3,658) | \$ (1,576) | \$ (133)   | \$ 2,874   | \$ 3,516   | \$ 4,185   | \$ 4,880   | \$ 5,602   | \$ 6,352   |
| Terminal value of equity                                     |             |             |            |            |            |            |            |            |            |            | \$87,317   |
| Present value                                                |             | \$ (10,583) | \$ (3,012) | \$ (1,178) | \$ (90)    | \$ 1,768   | \$ 1,966   | \$ 2,129   | \$ 2,262   | \$ 2,370   | \$ 36,207  |
| Cost of equity                                               | 10.20%      | 10.20%      | 10.20%     | 10.20%     | 10.20%     | 10.20%     | 10.048%    | 9.896%     | 9.744%     | 9.592%     | 9.440%     |
| Cumulative Cost of equity                                    |             | 1.1020      | 1.2144     | 1.3383     | 1.4748     | 1.6252     | 1.7885     | 1.9655     | 2.1570     | 2.3639     | 2.5871     |
| Value of equity today =                                      | \$31,838.74 |             |            |            |            |            |            |            |            |            |            |
| Number of shares outstanding =                               | 1386.00     |             |            |            |            |            |            |            |            |            |            |
| DCF Value per share =                                        | \$ 22.97    |             |            |            |            |            |            |            |            |            |            |
| Probability of equity wipeout                                | 10.00%      |             |            |            |            |            |            |            |            |            |            |
| Adjusted value per share =                                   | \$ 20.67    |             |            |            |            |            |            |            |            |            |            |
| Stock price on October 3, 2016 =                             | \$ 13.33    |             |            |            |            |            |            |            |            |            |            |

Return on equity increases to 5.85% (25th percentile of banks) in year 5 and 9,44% (cost of equity) in year 10

# Lesson 3: Not all financial service firms are built alike..

¨ Financial service is a broad category, and while banks may be its most substantive component, there are a range of other companies, with very different business models. ¨ For instance, payment processing companies and credit card companies are also financial service companies, but they derive their value from ¤ Getting consumers to use their platforms to make payments to businesses or to each other, resulting in transactions on the platform (called Gross Merchandising Value or GMV) ¤ Keeping a slice, called a take rate, of the GMV for themselves.

**The Story**Paytm will continue its dominance of the Indian mobile payment market, while that market continues to grow. Along the way, its management will focus more on converting transactions on its platform into revenues, and revenues into operating income.

**The Assumptions**

|                      | Base year   | Next year       | Years 2-5 | Years 6-10 | After year 10 | Link to story                                                  |
|----------------------|-------------|-----------------|-----------|------------|---------------|----------------------------------------------------------------|
| GMV                  | ₹ 4,033,000 | 40.00%          | 40.00%    | → 4.19%    | 4.19%         | Growing mobile payment market                                  |
| Revenue as % of GMV  | 0.79%       | 0.83%           | 1.00%     | → 2.00%    | 2.00%         | Take rate improves, as company matures                         |
| Operating margin (b) | -49.00%     | -20.0%          | 5.00%     | → 30.00%   | 30.00%        | High-margin intermediary business                              |
| Tax rate             | 25.00%      |                 | 25.00%    | → 25.00%   | 25.00%        | Converge on statutory tax rate                                 |
| Reinvestment (c)     |             | 3.00            | 2.45      | → 2.45     | 27.93%        | Industry average reinvestment, for capital intensive business. |
| Return on capital    | -21.78%     | Marginal ROIC = |           | 80.13%     | 15.00%        | Competitive advantages fade over time.                         |
| Cost of capital (d)  |             |                 | 10.44%    | → 8.91%    | 8.91%         | Cost of capital relatively stable.                             |

**The Cash Flows**

|               | GMV          | Revenues       | Operating Margin | EBIT (1-t)   | Reinvestment | FCFF         |
|---------------|--------------|----------------|------------------|--------------|--------------|--------------|
| 1             | ₹ 5,646,200  | ₹ 46,984.56    | -20.00%          | ₹ -9,396.91  | ₹ 5,038.85   | ₹ -14,435.77 |
| 2             | ₹ 7,904,680  | ₹ 69,095.49    | -10.00%          | ₹ -6,909.55  | ₹ 9,024.87   | ₹ -15,934.42 |
| 3             | ₹ 11,066,552 | ₹ 101,377.63   | -5.00%           | ₹ -5,068.88  | ₹ 13,176.38  | ₹ -18,245.27 |
| 4             | ₹ 15,493,173 | ₹ 148,430.20   | 0.00%            | ₹ -0.00      | ₹ 19,205.13  | ₹ -19,205.13 |
| 5             | ₹ 21,690,442 | ₹ 216,904.42   | 5.00%            | ₹ 10,845.22  | ₹ 27,948.66  | ₹ -17,103.44 |
| 6             | ₹ 28,813,149 | ₹ 345,757.79   | 10.00%           | ₹ 28,564.36  | ₹ 52,593.21  | ₹ -24,028.85 |
| 7             | ₹ 36,211,213 | ₹ 506,956.99   | 15.00%           | ₹ 57,032.66  | ₹ 65,795.59  | ₹ -8,762.93  |
| 8             | ₹ 42,915,357 | ₹ 686,645.72   | 20.00%           | ₹ 102,996.86 | ₹ 73,342.34  | ₹ 29,654.52  |
| 9             | ₹ 47,787,109 | ₹ 860,167.96   | 25.00%           | ₹ 161,281.49 | ₹ 70,825.40  | ₹ 90,456.09  |
| 10            | ₹ 49,789,389 | ₹ 995,787.77   | 30.00%           | ₹ 224,052.25 | ₹ 55,355.03  | ₹ 168,697.22 |
| Terminal year | ₹ 51,875,564 | ₹ 1,037,511.28 | 30.00%           | ₹ 233,440.04 | ₹ 65,207.58  | ₹ 168,232.45 |

**The Value**

| Terminal value                      | ₹ 3,564,246.92 |  |  |                                   |  |
|-------------------------------------|----------------|--|--|-----------------------------------|--|
| PV(Terminal value)                  | ₹ 1,377,090.74 |  |  |                                   |  |
| PV (CF over next 10 years)          | ₹ 36,169.53    |  |  |                                   |  |
| Value of operating assets =         | ₹ 1,413,260.27 |  |  |                                   |  |
| Adjustment for distress             | ₹ 35,331.51    |  |  | Probability of failure = 5.00%    |  |
| - Debt & Minority Interests         | ₹ 12,006.00    |  |  |                                   |  |
| + Cash & Other Non-operating assets | ₹ 7,785.00     |  |  |                                   |  |
| +IPO Proceeds                       | ₹ 83,000.00    |  |  |                                   |  |
| Value of equity                     | ₹ 1,456,707.76 |  |  |                                   |  |
| - Value of equity options           | ₹ 45,696.90    |  |  |                                   |  |
| Number of shares                    | 644.23         |  |  |                                   |  |
| Value per share                     | ₹ 2,190.24     |  |  | Stock was trading at = ₹ 2,950.00 |  |

## VI. Valuing Companies with "intangible" assets

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets? *The capital* roadblocks?

When will the firm become a mature fiirm, and what are the potential

*expenditures associated with acquiring intangible assets (technology, himan capital) are mis-categorized as operating expenses, leading to inccorect accounting earnings and measures of capital invested.*

*It ican be more difficult to borrow against intangible assets than it is against tangible assets. The risk in operations can change depending upon how stable the intangbiel asset is.*

*If capital expenditures are miscategorized as operating expenses, it becomes very difficult to assess how much a firm is reinvesting for future growth and how well its investments are doing.*

> *Intangbile assets such as brand name and customer loyalty can last for very long periods or dissipate overnight.*

## Lesson 1: Accounting rules are cluttered with inconsistencies…

¨ If we start with accounting first principles, capital expenditures are expenditures designed to create benefits over many periods. They should not be used to reduce operating income in the period that they are made, but should be depreciated/amortized over their life. They should show up as assets on the balance sheet. ¨ Accounting is consistent in its treatment of cap ex with manufacturing firms, but is inconsistent with firms that do not fit the mold. ¤ With pharmaceutical and technology firms, R&D is the ultimate cap ex but is treated as an operating expense. ¤ With consulting firms and other firms dependent on human capital, recruiting and training expenses are your long term investments that are treated as operating expenses. ¤ With brand name consumer product companies, a portion of the advertising expense is to build up brand name and is the real capital expenditure. It is treated as an operating expense.

## Lesson 2: And fixing those inconsistencies can alter your view of a company and affect its value

|                   | No R&D adjustment | R&D adjustment |
|-------------------|-------------------|----------------|
| EBIT              | \$5,071           | \$7,336        |
| Invested Capital  | \$25,277          | \$33,173       |
| ROIC              | 14.58%            | 18.26%         |
| Reinvestment Rate | 115.68%           | 106.98%        |
| Value of firm     | \$58,617          | \$95,497       |
| Value of equity   | \$50,346          | \$87,226       |
| Value/share       | \$42.73           | \$74.33        |

# Intangibles in Intrinsic Value

![](_page_332_Diagram_1.jpeg)

## VII. Valuing cyclical and commodity companies

What are the cashflows from existing assets?

What is the value added by growth assets?

How risky are the cash flows from both existing assets and growth assets? *Historial revenue and* roadblocks?

When will the firm become a mature fiirm, and what are the potential

*earnings data are volatile, as the economic cycle and commodity prices change.*

*Primary risk is from the economy for cyclical firms and from commodity price movements for commodity companies. These risks can stay dormant for long periods of apparent prosperity.*

*Company growth often comes from movements in the economic cycle, for cyclical firms, or commodity prices, for commodity companies.*

> *For commodity companies, the fact that there are only finite amounts of the commodity may put a limit on growth forever. For cyclical firms, there is the peril that the next recession may put an end to the firm.*

## Lesson 1: With "macro" companies, it is easy to get lost in "macro" assumptions…

¨ With cyclical and commodity companies, it is undeniable that the value you arrive at will be affected by your views on the economy or the price of the commodity. ¨ Consequently, you will feel the urge to take a stand on these macro variables and build them into your valuation. Doing so, though, will create valuations that are jointly impacted by your views on macro variables and your views on the company, and it is difficult to separate the two. ¨ The best (though not easiest) thing to do is to separate your macro views from your micro views. Use current market based numbers for your valuation, but then provide a separate assessment of what you think about those market numbers.

## Lesson 2: Use probabilistic tools to assess value as a function of macro variables…

¨ If there is a key macro variable affecting the value of your company that you are uncertain about (and who is not), why not quantify the uncertainty in a distribution (rather than a single price) and use that distribution in your valuation. ¨ That is exactly what you do in a Monte Carlo simulation, where you allow one or more variables to be distributions and compute a distribution of values for the company. ¨ With a simulation, you get not only everything you would get in a standard valuation (an estimated value for your company) but you will get additional output (on the variation in that value and the likelihood that your firm is under or over valued)

## Shell: A "Oil Price" Neutral Valuation: March 2016

Revenue calculated from prevailing oil price of \$40/barrel in March 2016  
 Revenue =  $39992.77 + 4039.40 * \$40$   
 $= \$201,569$ 

Compounded revenue growth of 3.91% a year, based on  
 Shell's historical revenue growth rate from 2000 to 2015

|                           | Base Year     |              | 1            | 2            | 3            | 4             | 5            | Terminal Year |  |  |
|---------------------------|---------------|--------------|--------------|--------------|--------------|---------------|--------------|---------------|--|--|
| Revenues                  | \$ 201,569    | \$ 209,450   | \$ 217,639   | \$ 226,149   | \$ 234,991   | \$ 244,180    | \$ 249,063   |               |  |  |
| Operating Margin          | 3.01%         | 6.18%        | 7.76%        | 8.56%        | 8.95%        | 9.35%         | 9.35%        |               |  |  |
| Operating Income          | \$ 6,065.00   | \$ 12,942.85 | \$ 16,899.10 | \$ 19,352.39 | \$ 21,040.39 | \$ 22,830.80  | \$ 23,287.41 |               |  |  |
| Effective tax rate        | 30.00%        | 30.00%       | 30.00%       | 30.00%       | 30.00%       | 30.00%        | 30.00%       |               |  |  |
| AT Operating Income       | \$ 4,245.50   | \$ 9,060.00  | \$ 11,829.37 | \$ 13,546.68 | \$ 14,728.27 | \$ 15,981.56  | \$ 16,301.19 |               |  |  |
| + Depreciation            | \$ 26,714.00  | \$ 27,759    | \$ 28,844    | \$ 29,972    | \$ 31,144    | \$ 32,361     |              |               |  |  |
| - Cap Ex                  | \$ 31,854.00  | \$ 33,099    | \$ 34,394    | \$ 35,738    | \$ 37,136    | \$ 38,588     |              |               |  |  |
| - Chg in WC               |               | \$ 472.88    | \$ 491.37    | \$ 510.58    | \$ 530.55    | \$ 551.29     |              |               |  |  |
| FCFF                      |               | \$ 3,246.14  | \$ 5,788.19  | \$ 7,269.29  | \$ 8,205.44  | \$ 9,203.68   | \$ 13,011.34 |               |  |  |
| Terminal Value            |               |              |              |              |              | \$ 216,855.71 |              |               |  |  |
| Return on capital         |               |              |              |              |              |               |              | 12.37%        |  |  |
| Cost of Capital           |               | 9.91%        | 9.91%        | 9.91%        | 9.91%        | 9.91%         | 8.00%        |               |  |  |
| Cumulated Discount Factor |               | 1.0991       | 1.2080       | 1.3277       | 1.4593       | 1.6039        |              |               |  |  |
| Present Value             |               | \$ 2,953.45  | \$ 4,791.47  | \$ 5,474.95  | \$ 5,622.81  | \$ 140,940.73 |              |               |  |  |
| Value of Operating Assets | \$ 159,783.41 |              |              |              |              |               |              |               |  |  |
| + Cash                    | \$ 31,752.00  |              |              |              |              |               |              |               |  |  |
| + Cross Holdings          | \$ 33,566.00  |              |              |              |              |               |              |               |  |  |
| - Debt                    | \$ 58,379.00  |              |              |              |              |               |              |               |  |  |
| - Minority Interets       | \$ 1,245.00   |              |              |              |              |               |              |               |  |  |
| Value of Equity           | \$ 165,477.41 |              |              |              |              |               |              |               |  |  |
| Number of shares          | 4209.7        |              |              |              |              |               |              |               |  |  |
| Value per share           | \$ 39.31      |              |              |              |              |               |              |               |  |  |

Operating margin converges on Shell's historical average margin of 9.35% from 200-2015

Return on capital reverts and stays at Shell's historic average of 12.37% from 200-2015

# Shell's Revenues & Oil Prices

![](_page_337_Figure_1.jpeg)

![](_page_338_Figure_15.jpeg)

**Revenue calculated from the oil price drawn from distribution**

Revenue =  $39992.77 + 4039.40 * \text{Oil Price/Barrel}$ 

**Pre-tax Operating Income based on revenue & selected margin**

Pre-tax Operating Income = Revenues \* Operating Margin

![](_page_338_Figure_20.jpeg)

Value Shell based on operating income, assuming other assumptions (tax rate, revenue growth, cost of capital)

| Percentiles: | Forecast values |
|--------------|-----------------|
| 0%           | \$6.55          |
| 10%          | \$23.90         |
| 20%          | \$27.73         |
| 30%          | \$30.89         |
| 40%          | \$33.88         |
| 50%          | \$36.99         |
| 60%          | \$40.28         |
| 70%          | \$44.22         |
| 80%          | \$49.24         |
| 90%          | \$57.49         |
| 100%         | \$197.11        |

![](_page_338_Figure_23.jpeg)

# VALUE, PRICE AND INFORMATION: CLOSING THE DEAL

Value versus Price

# Are you valuing or pricing?

INTRINSIC

VALUE PRICE Value Price THE GAP Is there one? Will it close?

![](_page_340_Figure_14.jpeg)

Drivers of intrinsic value

- Cashflows from existing assets
- Growth in cash flows
- Quality of Growth

## *Drivers of price*

- Market moods & momentum
- Surface stories about fundamentals

## *Tools for pricing*

- Multiples and comparables
- Charting and technical indicators
- Pseudo DCF

## *Tools for intrinsic analysis*

- Discounted Cashflow Valuation (DCF)
- Intrinsic multiples
- Book value based approaches
- Excess Return Models

## *Tools for "the gap"*

- Behavioral finance
- Price catalysts

## *Drivers of "the gap"*

- Information
- Liquidity
- Corporate governance

Value of cashflows, adjusted for time and risk

# Value versus Price

| View of the gap | Investment Strategies  |
|-----------------|------------------------|
| (1)             | Look for mispriced     |
| (2)             | Get ahead of shifts in |

## The valuer's dilemma and ways of dealing with it…

## ¨ Uncertainty about the magnitude of the gap:

¤ Margin of safety: Many value investors swear by the notion of the "margin of safety" as protection against risk/uncertainty. ¤ Collect more information: Collecting more information about the company is viewed as one way to make your investment less risky. ¤ Ask what if questions: Doing scenario analysis or what if analysis gives you a sense of whether you should invest. ¤ Confront uncertainty: Face up to the uncertainty, bring it into the analysis and deal with the consequences.

## ¨ Uncertainty about gap closing: This is tougher and you can reduce your exposure to it by

¤ Lengthening your time horizon ¤ Providing or looking for a catalyst that will cause the gap to close.

## Strategies for managing the risk in the "closing" of the gap

¨ The "karmic" approach: In this one, you buy (sell short) under (over) valued companies and sit back and wait for the gap to close. You are implicitly assuming that given time, the market will see the error of its ways and fix that error. ¨ The catalyst approach: For the gap to close, the price has to converge on value. For that convergence to occur, there usually has to be a catalyst. ¤ If you are an activist investor, you may be the catalyst yourself. In fact, your act of buying the stock may be a sufficient signal for the market to reassess the price. ¤ If you are not, you have to look for other catalysts. Here are some to watch for: a new CEO or management team, a "blockbuster" new product or an acquisition bid where the firm is targeted.

# An example: Apple – Price versus Value (my estimates) from 2011 to 2020

![](_page_344_Figure_3.jpeg)

# A closing thought...

![](_page_345_Picture_7.jpeg)