---
title: "Valpacket1Spr26"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket1spr26.pdf
---

# VALUATION: LECTURE NOTE PACKET 1 INTRINSIC VALUATION

Aswath Damodaran

Updated: January 2026

1

# THE ESSENCE OF INTRINSIC VALUE

- ▪ In intrinsic valuation, you value an asset based upon its **fundamentals** (or intrinsic characteristics).
- ▪ For **cash flow generating assets**, the intrinsic value will be a function of the magnitude of the expected cash flows on the asset over its lifetime and the uncertainty about receiving those cash flows.
  - ▪ **Discounted cash flow (DCF)** valuation is a tool for estimating intrinsic value, where the expected value of an asset is written as the present value of the expected cash flows on the asset, with either the cash flows or the discount rate adjusted to reflect the risk.
  - ▪ Intrinsic valuation models predate the modern DCF model, since investors through the ages have found ways to weight in expected cash flows into value.

# THE TWO FACES OF DISCOUNTED CASH FLOW VALUATION

- The value of a risky asset can be estimated by discounting the expected cash flows on the asset over its life at a risk-adjusted discount rate.

$$\text{Value of asset} = \frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$$

where the asset has an n-year life,  $E(CF_t)$  is the expected cash flow in period  $t$  and  $r$  is a discount rate that reflects the risk of the cash flows.

- Alternatively, we can replace the expected cash flows with the guaranteed cash flows we would have accepted as an alternative (certainty equivalents) and discount these at the riskfree rate:

$$\text{Value of asset} = \frac{CE(CF_1)}{(1+r_f)} + \frac{CE(CF_2)}{(1+r_f)^2} + \frac{CE(CF_3)}{(1+r_f)^3} \dots + \frac{CE(CF_n)}{(1+r_f)^n}$$

where  $CE(CF_t)$  is the certainty equivalent of  $E(CF_t)$  and  $r_f$  is the riskfree rate.

# RISK ADJUSTED VALUE: TWO BASIC PROPOSITIONS

- ▪ The value of an asset is the risk-adjusted present value of the cash flows:

$$\text{Value of asset} = \frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} + \dots + \frac{E(CF_n)}{(1+r)^n}$$

- ▪ **The “IT” proposition:** If IT does not affect the expected cash flows or the riskiness of the cash flows, IT cannot affect value.
- ▪ **The “DON’T BE A WUSS” proposition:** Valuation requires that you make estimates of expected cash flows in the future, not that you be right about those cashflows. So, uncertainty is not an excuse for not making estimates.
- ▪ **The “DUH” proposition:** For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.
- ▪ **The “DON’T FREAK OUT” proposition:** A business with negative cash flows in the early years can still be valuable if it has more than proportionate positive cash flows in the later years.

# DCF CHOICES: EQUITY VALUATION VERSUS FIRM VALUATION

**Firm Valuation:** Value the entire business

![](_page_4_Diagram_82.jpeg)

**Equity valuation:** Value just the equity claim in the business

# 1. EQUITY VALUATION

*Figure 5.5: Equity Valuation*

![](_page_5_Diagram_55.jpeg)

## 2. FIRM OR BUSINESS VALUATION

*Figure 5.6: Firm Valuation*

![](_page_6_Diagram_68.jpeg)

# FIRM VALUE AND EQUITY VALUE

- ▪ To get from firm value to equity value, which of the following would you need to do?
  - a. Subtract out the value of long-term debt
  - b. Subtract out the value of all debt
  - c. Subtract the value of any debt that was included in the cost of capital calculation
  - d. Subtract out the value of all liabilities in the firm
- ▪ Doing so, will give you a value for the equity which is
  - a. greater than the value you would have got in an equity valuation
  - b. lesser than the value you would have got in an equity valuation
  - c. equal to the value you would have got in an equity valuation

# CASH FLOWS AND DISCOUNT RATES

- Assume that you are analyzing a company with the following cashflows for the next five years.

| Year       | CF to Equity | Interest Expense (1-t) | CF to Firm  |
|------------|--------------|------------------------|-------------|
| 1          | \$ 50        | \$ 40                  | \$ 90       |
| 2          | \$ 60        | \$ 40                  | \$ 100      |
| 3          | \$ 68        | \$ 40                  | \$ 108      |
| 4          | \$ 76.2      | \$ 40                  | \$ 116.2    |
| 5          | \$ 83.49     | \$ 40                  | \$ 123.49   |
| Term Value | \$ 1603.0    |                        | \$ 2363.008 |

- Assume also that the cost of equity is 13.625% and the firm can borrow long term at 10%. (The tax rate for the firm is 50%.)
- The current market value of equity is \$1,073 and the value of debt outstanding is \$800.

# EQUITY VERSUS FIRM VALUATION

- ▪ **Method 1: Discount CF to Equity at Cost of Equity to get value of equity**

- - ▪ Cost of Equity = 13.625%
  - ▪ Value of Equity =  $50/1.13625 + 60/1.13625^2 + 68/1.13625^3 + 76.2/1.13625^4 + (83.49+1603)/1.13625^5 = \$1073$

- ▪ **Method 2: Discount CF to Firm at Cost of Capital to get value of firm**

- - ▪ Cost of Debt = Pre-tax rate (1- tax rate) = 10% (1-.5) = 5%
  - ▪ Cost of Capital = 13.625% (1073/1873) + 5% (800/1873) = 9.94%
  - ▪ PV of Firm =  $90/1.0994 + 100/1.0994^2 + 108/1.0994^3 + 116.2/1.0994^4 + (123.49+2363)/1.0994^5 = \$1873$
  - ▪ Value of Equity = Value of Firm - Market Value of Debt
  - ▪ 
    $$= \$ 1873 - \$ 800 = \$1073$$

# FIRST PRINCIPLE OF VALUATION

- ■ **Discounting Consistency Principle:** Never mix and match cash flows and discount rates. If your cash flows are after debt payments, i.e., to equity, the discount rate has to be the cost of equity. If your cash flows are pre-debt cash flows, i.e., to the firm, the discount rate has to be the cost of capital.
- ■ **The Mismatch Effect:** Mismatching cash flows to discount rates is deadly.
  - ■ Discounting cashflows after debt cash flows (equity cash flows) at the cost of capital will lead to an upwardly biased estimate of the value of equity.
  - ■ Discounting pre-debt cashflows (cash flows to the firm) at the cost of equity will yield a downward biased estimate of the value of the firm.

# THE EFFECTS OF MISMATCHING CASH FLOWS AND DISCOUNT RATES

- ▪ **Error 1:** Discount CF to Equity at Cost of Capital to get equity value

- - ▪  $PV \text{ of Equity} = 50/1.0994 + 60/1.0994^2 + 68/1.0994^3 + 76.2/1.0994^4 + (83.49+1603)/1.0994^5 = \$1248$

- - - ▪ Value of equity is overstated by \$175.

- ▪ **Error 2:** Discount CF to Firm at Cost of Equity to get firm value

- - - ▪  $PV \text{ of Firm} = 90/1.13625 + 100/1.13625^2 + 108/1.13625^3 + 116.2/1.13625^4 + (123.49+2363)/1.13625^5 = \$1613$

- - - ▪  $PV \text{ of Equity} = \$1612.86 - \$800 = \$813$

- - - - ▪ Value of Equity is understated by \$ 260.

- ▪ **Error 3:** Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity

- - - - ▪ Value of Equity = \$ 1613

- - - - - ▪ Value of Equity is overstated by \$ 540

![](_page_12_Picture_12.jpeg)

# DCF: FIRST STEPS

The Big Picture

# GENERIC DCF VALUATION MODEL

## DISCOUNTED CASHFLOW VALUATION

![](_page_13_Diagram_98.jpeg)

# SAME INGREDIENTS, DIFFERENT APPROACHES...

| Input           | Dividend Discount Model                      | FCFE (Potential dividend) discount model                                       | FCFF (firm) valuation model                                                      |
|-----------------|----------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Cash flow       | Dividend                                     | $FCFE = \text{Cash flows after taxes, reinvestment needs and debt cash flows}$ | $FCFF = \text{Cash flows before debt payments but after reinvestment \& taxes.}$ |
| Expected growth | In equity income and dividends               | In equity income and FCFE                                                      | In operating income and FCFF                                                     |
| Discount rate   | Cost of equity                               | Cost of equity                                                                 | Cost of capital                                                                  |
| Steady state    | When dividends grow at constant rate forever | When FCFE grow at constant rate forever                                        | When FCFF grow at constant rate forever                                          |

# START EASY: THE DIVIDEND DISCOUNT MODEL

![](_page_15_Diagram_76.jpeg)

# MOVING ON UP: THE “POTENTIAL DIVIDENDS” OR FCFE MODEL

![](_page_16_Diagram_85.jpeg)

# TO VALUING THE ENTIRE BUSINESS: THE FCFF MODEL

![](_page_17_Diagram_88.jpeg)

![](_page_18_Picture_4.jpeg)

# DCF: THE PROCESS

Above the fray!

**Cash flow to Firm**

Revenues \* Operating Margin = Operating Income

\* (1- tax rate)                      Tax Effect  
- (Cap Ex - Depreciation)                      Reinvestment  
- Change in non-cash WC                      Free Cash flow to Firm

\* How quickly is the firm growing?  
\* How efficiently is it growing?  
\* How profitable is the firm?

Value of Operating Assets  
+ Cash  
+ Non-operating Assets  
- Debt  
= Value of Equity

Adjust for risk of failure  
= Probability of failure \*  
Value of Equity in failure

If margins & returns are stable  
Expected growth in operating income = Reinvestment  
Rate \* Return on Invested Capital  
FCFF = After-tax Oper. Income (1 - Reinvestment Rate)

If margins & returns are changing  
1. Estimate revenue growth & future revenues  
2. Estimate operating margins over time  
3. Estimate reinvestment based on revenues  
FCFF = After tax Operating Income - Reinvestment

**Firm is mature**  
Cashflow/Earnings grow at constant rate forever (g<sub>n</sub>)

Terminal Value = FCFF\_{n+1} / (r - g<sub>n</sub>)

![](_page_19_Diagram_46.jpeg)

![](_page_19_Diagram_47.jpeg)

**Long term rate at which you can borrow money, today**  
(Riskfree Rate + Default Spread) (1- tax rate)

**Return required by "marginal" investors, given perceived risk in equity investment**

![](_page_19_Diagram_50.jpeg)

# THE SEQUENCE

1. 1. **Get a handle on the past and the cross-section:** While the past is the past (and should have little relevance in determining value), you can get clues about the future by looking at what your firm has done in the past, and what other companies in the business are doing now.
2. 2. **Risk and Discount Rates:** Traditional financial theory (unfortunately) has put too much of a focus on risk and discount rates, but they do remain ingredients in valuing a company.
3. 3. **Estimate growth and future cash flows:** This is where the rubber meets the road in valuation. Estimating future cash flows is never easy, should not be mechanical and should be built around your story.
4. 4. **Apply Closure to cash flows:** Since you cannot estimate cash flows forever, you need to find a way to bring your valuation to closure.
5. 5. **Tie up loose ends:** Check to see what else in your business needs to be valued or adjusted for to get to value per share.

![](_page_21_Picture_4.jpeg)

# DISCOUNT RATES

The D in the DCF..

# ESTIMATING INPUTS: DISCOUNT RATES – EXTENDING THE CONSISTENCY RULE

- ▪ While discount rates obviously matter in DCF valuation, they don't matter as much as most analysts think they do.
- ▪ At an intuitive level, the discount rate used should be consistent with both the riskiness and the type of cashflow being discounted.
  - ▪ **Equity versus Firm:** If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital.
  - ▪ **Currency:** The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated.
  - ▪ **Nominal versus Real:** If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

# RISK IN THE DCF MODEL

*Expectation of cash flows across all scenarios, good and bad. Incorporates all risks that affect the asset / business.*

Expected Cash Flows

---

Risk Adjusted Discount Rate

*Discount rate should reflect the risk perceived by the marginal investor in the company*

$$\text{Risk Adjusted Cost of equity} = \frac{\text{Risk free rate in the currency of analysis} + \text{Relative risk of company/equity in question}}{\text{Equity Risk Premium required for average risk equity}}$$

# NOT ALL RISK IS CREATED EQUAL...

- ▪ Estimation versus Economic uncertainty
  - ▪ **Estimation uncertainty** reflects the possibility that you could have the “wrong model” or estimated inputs incorrectly within this model.
  - ▪ **Economic uncertainty** comes the fact that markets and economies can change over time and that even the best models will fail to capture these unexpected changes.
- ▪ Micro uncertainty versus Macro uncertainty
  - ▪ **Micro uncertainty** refers to uncertainty about the potential market for a firm’s products, the competition it will face and the quality of its management team.
  - ▪ **Macro uncertainty** reflects the reality that your firm’s fortunes can be affected by changes in the macro economic environment.
- ▪ Discrete versus continuous uncertainty
  - ▪ **Discrete risk** lie dormant for periods but show up at points in time.  
    (Examples: A drug working its way through the FDA pipeline may fail at some stage of the approval process or a company in Venezuela may be nationalized)
  - ▪ **Continuous risks** like changes in interest rates or economic growth occur continuously and affect value as they happen.

# RISK AND COST OF EQUITY: THE ROLE OF THE MARGINAL INVESTOR

- ▪ **Not all risk counts:** While the notion that the cost of equity should be higher for riskier investments and lower for safer investments is intuitive, what risk should be built into the cost of equity is the question.
- ▪ **Risk through whose eyes?** While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment
- ▪ **The diversification effect:** Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (i.e, market or non-diversifiable risk). In effect, it is primarily economic, macro, continuous risk that should be incorporated into the cost of equity.

# THE COST OF EQUITY: COMPETING “ MARKET RISK” MODELS

## Model Expected Return

$$\text{CAPM} \quad E(R) = Rf + \beta (R_m - Rf)$$

$$\text{APM} \quad E(R) = Rf + \sum \beta_j (R_j - Rf)$$

$$\text{Multi factor} \quad E(R) = Rf + \sum \beta_j (R_j - Rf)$$

$$\text{Proxy} \quad E(R) = a + \sum \beta_j Y_j$$

## Inputs Needed

Riskfree Rate

Beta relative to market portfolio

Market Risk Premium

Riskfree Rate; # of Factors;

Betas relative to each factor

Factor risk premiums

Riskfree Rate; Macro factors

Betas relative to macro factors

Macro economic risk premiums

Proxies

Regression coefficients

# THE PARAMETERS: COST OF EQUITY

- ▪ In the CAPM, the cost of equity:
  - ▪  $\text{Cost of Equity} = \text{Riskfree Rate} + \text{Equity Beta} * (\text{Equity Risk Premium})$
- ▪ In APM or Multi-factor models, you still need a risk free rate, as well as betas and risk premiums to go with each factor.
- ▪ To use any risk and return model, you need
  - ▪ A **riskfree rate** as a base
  - ▪ A single **equity risk premium** (in the CAPM) or **factor risk premiums**, in the multi-factor models
  - ▪ A **beta** (in the CAPM) or **betas** (in multi-factor models)

![](_page_28_Picture_4.jpeg)

# DISCOUNT RATES I

The Riskfree Rate

# THE RISK FREE RATE: LAYING THE FOUNDATIONS

- ▪ On a riskfree investment, the actual return is equal to the expected return. Therefore, there is no variance around the expected return.
- ▪ For an investment to be riskfree, then, it has to have
  - ▪ No default risk
  - ▪ No reinvestment risk
- ▪ It follows then that if asked to estimate a risk free rate:
  - ▪ Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
  - ▪ Currencies matter: A risk free rate is currency-specific and can be very different for different currencies.
  - ▪ Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

# TEST 1: A RISKFREE RATE IN US DOLLARS!

- ▪ In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be (at the start of 2026):
  - a. A three-month Treasury bill rate (3.27%)
  - b. A ten-year Treasury bond rate (4.18%)
  - c. A thirty-year Treasury bond rate (4.80%)
  - d. A TIPs (inflation-indexed treasury) rate (2.16%)
  - e. Other (Specify)
- ▪ What are we implicitly assuming about the US treasury when we use any of the treasury numbers?
- ▪ Has your thinking on this implicit assumption changed in the recent past?

# TEST 2: A RISKFREE RATE IN EUROS?

Ten-year Euro Government Bond Rates on 1/1/25

![](_page_31_Figure_64.jpeg)

# TEST 3: A RISKFREE RATE IN INDIAN RUPEES

- ▪ The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 6.61% on January 1, 2026.
- ▪ In January 2026, the Indian government had a local currency sovereign rating of Baa3. The typical default spread (over a default free rate) for Baa3 rated country bonds in early 2025 was 1.87%. The riskfree rate in Indian Rupees is
  - a. The yield to maturity on the 10-year bond (6.61%)
  - b. The yield to maturity on the 10-year bond – Default spread (4.74%)
  - c. The yield to maturity on the 10-year bond + Default spread (8.48%)
  - d. None of the above

# SOVEREIGN DEFAULT SPREAD: THREE PATHS TO THE SAME DESTINATION...

- ▪ **Sovereign dollar or euro denominated bonds:** Find sovereign bonds denominated in US dollars, issued by an emerging sovereign.
  - ▪ Default spread = Emerging Govt Bond Rate (in US \$) – US Treasury Bond rate with same maturity.
- ▪ **Sovereign CDS spreads:** Obtain the traded value for a sovereign Credit Default Swap (CDS) for the emerging government.
  - ▪ Default spread = Sovereign CDS spread (with perhaps an adjustment for CDS market frictions).
- ▪ **Sovereign-rating based spread:** For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries with the same sovereign rating.

# APPROACH 1: DEFAULT SPREAD FROM GOVERNMENT BONDS

| Country       | \$ Bond Rate | Riskfree Rate | Default Spread |
|---------------|--------------|---------------|----------------|
| \$            |              |               |                |
| Peru          | 6.27%        | 3.95%         | 2.32%          |
| <b>Brazil</b> | <b>6.60%</b> | <b>3.95%</b>  | <b>2.65%</b>   |
| Colombia      | 6.68%        | 3.95%         | 2.73%          |
| Poland        | 4.95%        | 3.95%         | 1.00%          |
| Turkey        | 16.18%       | 3.95%         | 12.23%         |
| Mexico        | 4.96%        | 3.95%         | 1.01%          |
| Euro Bonds    |              |               |                |
| Bulgaria      | 3.30%        | 2.90%         | 0.50%          |

# APPROACH 2: CDS SPREADS – JANUARY 2026

| Country        | Sovr CDS | Net of Swiss | Country    | Sovr CDS | Net of Swiss | Country      | Sovr CDS | Net of Swiss | Country        | Sovr CDS | Net of Swiss |
|----------------|----------|--------------|------------|----------|--------------|--------------|----------|--------------|----------------|----------|--------------|
| Abu Dhabi      | 0.60%    | 0.46%        | Ethiopia   | NA       | NA           | Mexico       | 1.66%    | 1.52%        | South Africa   | 2.40%    | 2.26%        |
| Algeria        | 1.34%    | 1.20%        | Finland    | 0.26%    | 0.12%        | Mongolia     | 3.26%    | 3.12%        | Spain          | 0.45%    | 0.31%        |
| Angola         | 6.24%    | 6.10%        | France     | 0.64%    | 0.50%        | Morocco      | 1.30%    | 1.16%        | Sri Lanka      | NA       | NA           |
| Argentina      | 6.94%    | 6.80%        | Gabon      | 8.54%    | 8.40%        | Namibia      | 3.41%    | 3.27%        | Sweden         | 0.20%    | 0.06%        |
| Australia      | 0.19%    | 0.05%        | Germany    | 0.21%    | 0.07%        | Netherlands  | 0.20%    | 0.06%        | Switzerland    | 0.14%    | 0.00%        |
| Austria        | 0.28%    | 0.14%        | Greece     | 0.75%    | 0.61%        | New Zealand  | 0.23%    | 0.09%        | Thailand       | 0.66%    | 0.52%        |
| Bahrain        | 2.47%    | 2.33%        | Guatemala  | 1.71%    | 1.57%        | Nicaragua    | 5.29%    | 5.15%        | Tunisia        | 7.01%    | 6.87%        |
| Belgium        | 0.40%    | 0.26%        | Hong Kong  | 0.44%    | 0.30%        | Nigeria      | 3.91%    | 3.77%        | Turkey         | 2.99%    | 2.85%        |
| Brazil         | 2.35%    | 2.21%        | Hungary    | 1.60%    | 1.46%        | Norway       | 0.18%    | 0.04%        | Ukraine        | NA       | NA           |
| Bulgaria       | 0.77%    | 0.63%        | Iceland    | 0.45%    | 0.31%        | Oman         | 1.30%    | 1.16%        | United Kingdom | 0.37%    | 0.23%        |
| Cameroon       | 6.87%    | 6.73%        | India      | 0.80%    | 0.66%        | Pakistan     | 5.23%    | 5.09%        | United States  | 0.44%    | 0.30%        |
| Canada         | 0.33%    | 0.19%        | Indonesia  | 1.19%    | 1.05%        | Panama       | 2.22%    | 2.08%        | Uruguay        | 0.77%    | 0.63%        |
| Chile          | 0.87%    | 0.73%        | Iraq       | 2.89%    | 2.75%        | Peru         | 1.26%    | 1.12%        | Venezuela      | 9.29%    | 9.15%        |
| China          | 0.64%    | 0.50%        | Ireland    | 0.34%    | 0.20%        | Philippines  | 1.02%    | 0.88%        | Vietnam        | 1.51%    | 1.37%        |
| Colombia       | 3.34%    | 3.20%        | Israel     | 1.13%    | 0.99%        | Poland       | 1.00%    | 0.86%        | Zambia         | 4.08%    | 3.94%        |
| Costa Rica     | 1.75%    | 1.61%        | Italy      | 0.61%    | 0.47%        | Portugal     | 0.45%    | 0.31%        |                |          |              |
| Croatia        | 1.02%    | 0.88%        | Japan      | 0.44%    | 0.30%        | Qatar        | 0.61%    | 0.47%        |                |          |              |
| Cyprus         | 0.75%    | 0.61%        | Kazakhstan | 1.31%    | 1.17%        | Romania      | 2.11%    | 1.97%        |                |          |              |
| Czech Republic | 0.48%    | 0.34%        | Kenya      | 4.51%    | 4.37%        | Russia       | NA       | NA           |                |          |              |
| Denmark        | 0.18%    | 0.04%        | Korea      | 0.34%    | 0.20%        | Rwanda       | 4.03%    | 3.89%        |                |          |              |
| Dubai          | 0.82%    | 0.68%        | Kuwait     | 0.87%    | 0.73%        | Saudi Arabia | 1.12%    | 0.98%        |                |          |              |
| Ecuador        | 5.67%    | 5.53%        | Latvia     | 0.82%    | 0.68%        | Senegal      | 9.93%    | 9.79%        |                |          |              |
| Egypt          | 3.55%    | 3.41%        | Lebanon    | NA       | #VALUE!      | Serbia       | 1.96%    | 1.82%        |                |          |              |
| El Salvador    | 3.40%    | 3.26%        | Lithuania  | 0.82%    | 0.68%        | Slovakia     | 0.57%    | 0.43%        |                |          |              |
| Estonia        | 1.00%    | 0.86%        | Malaysia   | 0.67%    | 0.53%        | Slovenia     | 0.67%    | 0.53%        |                |          |              |

# APPROACH 3: TYPICAL DEFAULT SPREADS: JANUARY 2024

| S&P Sovereign Rating | Moody's Sovereign Rating | Default Spread |
|----------------------|--------------------------|----------------|
| AAA                  | Aaa                      | 0.00%          |
| AA+                  | Aa1                      | 0.40%          |
| AA                   | Aa2                      | 0.49%          |
| AA-                  | Aa3                      | 0.59%          |
| A+                   | A1                       | 0.70%          |
| A                    | A2                       | 0.84%          |
| A-                   | A3                       | 1.19%          |
| BBB+                 | Baa1                     | 1.58%          |
| BBB                  | Baa2                     | 1.89%          |
| BBB-                 | Baa3                     | 2.18%          |
| BB+                  | Ba1                      | 2.48%          |
| <b>BB</b>            | <b>Ba2</b>               | <b>2.98%</b>   |
| BB                   | Ba3                      | 3.56%          |
| B+                   | B1                       | 4.46%          |
| B                    | B2                       | 5.45%          |
| B-                   | B3                       | 6.44%          |
| CCC+                 | Caa1                     | 7.43%          |
| CCC                  | Caa2                     | 8.92%          |
| CCC-                 | Caa3                     | 9.91%          |
| CC+                  | Ca1                      | 11.88%         |
| CC                   | Ca2                      | 14.00%         |
| CC-                  | Ca3                      | 16.00%         |
| C+                   | C1                       | 17.50%         |
| C                    | C2                       | 19.00%         |
| C-                   | C3                       | 21.00%         |

# GETTING TO A RISK FREE RATE IN BRAZILIAN REAIS ON JANUARY 1, 2026

- ▪ The Brazilian government bond rate in nominal reais on January 1, 2026, was 13.86%. To get to a riskfree rate in nominal reais, we can use one of three approaches.
  - ▪ **Approach 1: Government Bond spread**
    - ▪ Default Spread = Brazil \$ Bond Rate – US T.Bond Rate = 6.60%- 3.95% = 2.65%
    - ▪ Riskfree rate in \$R = 13.86% - 2.65% = 11.21%
  - ▪ **Approach 2: The CDS Spread**
    - ▪ The CDS spread for Brazil, adjusted for the US CDS spread was 2.21%.
    - ▪ Riskfree rate in \$R = 13.86% - 2.21% = 11.65%
  - ▪ **Approach 3: The Rating based spread**
    - ▪ Brazil has a Ba2 local currency rating from Moody's. The default spread for that rating is 2.98%
    - ▪ Riskfree rate in \$R = 13.86% - 2.98% = 10.88%

# TEST 4: A REAL RISKFREE RATE

- ▪ In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms.
- ▪ To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination.
- ▪ In January 2026, the yield on a 10-year indexed treasury bond was 2.16%. Which of the following statements would you subscribe to?
  - a. This (2.16%) is the real riskfree rate to use, if you are valuing US companies in real terms.
  - b. This (2.16%) is the real riskfree rate to use, anywhere in the world
  - c. Explain.

# WHY DO RISK FREE RATES VARY ACROSS CURRENCIES? JANUARY 2026 RISK FREE RATES

![](_page_39_Figure_10.jpeg)

# OR ACROSS TIME...

![](_page_40_Figure_10.jpeg)

# RISK FREE RATE: DON'T HAVE OR DON'T TRUST THE GOVERNMENT BOND RATE?

- ■ You can scale up the riskfree rate in a base currency (\$, Euros) by the differential inflation between the base currency and the currency in question. In US \$:

- - ■ Risk free rate<sub>Currency</sub> =  $(1 + \text{Riskfree rate}_{US \$}) \frac{(1 + \text{Expected Inflation}_{\text{Foreign Currency}})}{(1 + \text{Expected Inflation}_{US \$})} - 1$

- ■ Thus, if the US \$ risk free rate is 2.00%, the inflation rate in Egyptian pounds is 15% and the inflation rate in US \$ is 1.5%, the foreign currency risk free rate is as follows:

- - ■ Risk free rate =  $(1.02) \frac{(1.15)}{(1.015)} - 1 = 15.57\%$

# ONE MORE TEST ON RISKFREE RATES...

- ■ On January 1, 2022, the 10-year treasury bond rate in the United States was 1.51%, low by historic standards. Assume that you are valuing a company in US dollars then but are wary about the riskfree rate being too low. Which of the following should you do?
  - a. Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 5-6%)
  - b. Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate.
  - c. Something else...

# SOME PERSPECTIVE ON RISK FREE RATES

![](_page_43_Figure_10.jpeg)

# NEGATIVE INTEREST RATES?

- ■ In 2022, there were at least three currencies (Swiss Franc, Japanese Yen, Euro) with negative interest rates. Using the fundamentals (inflation and real growth) approach, how would you explain negative interest rates?
  - ■ How negative can rates get? (Is there a lower bound?)
  - ■ Would you use these negative interest rates as risk free rates?
    - a. If no, why not and what would you do instead?
    - b. If yes, what else would you have to do in your valuation to be internally consistent?

![](_page_45_Picture_12.jpeg)

# DISCOUNT RATES: II

The price of risk

# THE DRIVERS OF EQUITY RISK PREMIUMS

## Risk Aversion

Thesis: As investors become more (less) risk averse, equity risk premiums should rise (fall).  
Implication: Markets with aging investors should have higher risk premiums that markets with younger investors.

## Economic Uncertainty

Thesis: As uncertainty about the economy increases (decreases), equity risk premiums should increase (decrease).  
Implication: Equity risk premiums should rise during economic crises, and be higher in younger & growing economies.

## Inflation and Interest Rates

Thesis: As inflation rises (falls), uncertainty about inflation will increase (decrease), pushing up (down) equity risk premiums.  
Implication: Equity risk premiums should rise during periods of high and volatile inflation.

## Information

Thesis: As corporate disclosures becomes more (less) informative, equity risk premiums should fall (rise).  
Implication: Markets with better disclosure rules and requirements should have lower equity risk premiums that markets without.

Equity Risk Premium

## Liquidity and Fund Flows

Thesis: As liquidity increases and funds flow into equity markets, equity risk premiums should decrease.  
Implication: Events or actions (crises, regulation) that stymie fund flows and liquidity will increase equity risk premiums

## Catastrophic Risk

Thesis: As the likelihood of catastrophic events (low probability events with large consequences) increases, equity risk premiums should rise.  
Implication: As investor worries about large consequence events (pandemics, nuclear war) increases, equity risk premiums will go up.

## Government Policy

Thesis: Governments that are more capricious, with changing economic rules/policies, will give rise to higher equity risk premiums.  
Implication: Equity risk premiums should be higher in countries/markets where there is less continuity in economic policy and regulation.

## Central Banks & Monetary Policy

Thesis: Central banks that are less predictable in policy responses and more inconsistent in their actions will push up equity risk premiums.  
Implication: As monetary policy becomes more unpredictable, for political reasons or because of inflation, equity risk premiums will rise.

# LOOKING BACK: HISTORICAL EQUITY RISK RISK PREMIUMS

- ▪ The **historical premium** is the premium that stocks have historically earned over riskless securities.
- ▪ While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to
  - ▪ How far back you go in history...
  - ▪ Whether you use T.bill rates or T.Bond rates
  - ▪ Whether you use geometric or arithmetic averages.
- ▪ For instance, looking at the US:

|           |        | <i>Arithmetic Average</i> |                   | <i>Geometric Average</i> |                   |
|-----------|--------|---------------------------|-------------------|--------------------------|-------------------|
|           |        | Stocks - T. Bills         | Stocks - T. Bonds | Stocks - T. Bills        | Stocks - T. Bonds |
| 1928-2025 | 8.44%  | 7.03%                     | 6.65%             | 5.48%                    |                   |
| Std Error | 2.00%  | 2.12%                     |                   |                          |                   |
| 1976-2025 | 8.80%  | 6.56%                     | 7.61%             | 5.79%                    |                   |
| Std Error | 2.30%  | 2.67%                     |                   |                          |                   |
| 2016-2025 | 13.50% | 14.52%                    | 12.44%            | 13.79%                   |                   |
| Std Error | 5.04%  | 3.65%                     |                   |                          |                   |

# THE PERILS OF TRUSTING THE PAST.....

- ▪ **Noisy estimates:** Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 90 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

$$\text{Standard Error in Premium} = 20\% / \sqrt{90} = 2.1\%$$

- ▪ **Survivorship Bias:** Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

# THE SIMPLEST WAY OF ESTIMATING AN ADDITIONAL COUNTRY RISK PREMIUM: THE COUNTRY DEFAULT SPREAD

- ▪ **Estimate default spread for country:** In this approach, the country equity risk premium is set equal to the default spread for the country, estimated in one of three ways:
  - ▪ The default spread on a dollar denominated bond issued by the country. (In January 2025, that spread was % for the Brazilian \$ bond) was 1.817%.
  - ▪ The sovereign CDS spread for the country. In January 2025, the ten-year CDS spread for Brazil, adjusted for the US CDS, was 3.17%.
  - ▪ The default spread based on the local currency rating for the country. Brazil's sovereign local currency rating is Ba2 and the default spread for a Ba2 rated sovereign was about 2.83% in January 2025.
- ▪ **Add the default spread to a “mature” market premium:** This default spread is added on to the mature market premium to arrive at the total equity risk premium for Brazil, assuming a mature market premium of 4.23%.
  - ▪ Country Risk Premium for Brazil = 2.98%
  - ▪ Total ERP for Brazil = 4.23% + 2.98% = 7.21%

# AN EQUITY VOLATILITY BASED APPROACH TO ESTIMATING THE COUNTRY TOTAL ERP

- ▪ This approach draws on the **standard deviation of two equity markets**, the emerging market in question and a base market (usually the US). The total equity risk premium for the emerging market is then written as:
  - ▪ Equity risk premium = Risk Premium<sub>US</sub> × (  $\sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$  )
- ▪ The country equity risk premium is based upon the **volatility of the market in question relative to U.S market**.
  - ▪ Assume that the equity risk premium for the US is 4.23%.
  - ▪ Assume that the standard deviation in the Bovespa (Brazilian equity) is 30% and that the standard deviation for the S&P 500 (US equity) is 18%.
  - ▪ Total Equity Risk Premium for Brazil =  $4.23\% (30\%/18\%) = 7.05\%$
  - ▪ Country equity risk premium for Brazil =  $7.05\% - 4.23\% = 2.82\%$

# A MELDED APPROACH TO ESTIMATING THE ADDITIONAL COUNTRY RISK PREMIUM

- ▪ **Country ratings measure default risk.** While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
- ▪ Another is to **multiply the bond default spread by the relative volatility of stock and bond prices in that market.** Using this approach for Brazil in January 2025, you would get:
  - ▪ Country Equity risk premium = Default spread on country bond\*  
     $\sigma_{\text{Country Equity}} / \sigma_{\text{Country Bond}}$ 
    - ▪ Standard Deviation in Bovespa (Equity) = 30%
    - ▪ Standard Deviation in Brazil government bond = 20%
    - ▪ Default spread for Brazil= 2.98%
  - ▪ Brazil Country Risk Premium =  $2.98\% (30\%/20\%) = 4.41\%$
  - ▪ Brazil Total ERP = Mature Market Premium + CRP =  $4.23\% + 4.41\% = 8.64\%$

# A TEMPLATE FOR ESTIMATING THE ERP

## ERP Estimation Procedure - January 1, 2026

*Step 1: Mature Market Premium*

*Step 2: Assess country risk*

*Step 3: Convert country risk measure into an additional country risk premium for equity*

*Step 4: Estimate an ERP for country*

![](_page_52_Diagram_31.jpeg)

*Blue: Moody's Rating Red: Added Country Risk Green #: Total ERP*

| Andorra (Principality of) | Baal | <b>0.07%</b> | 6.30% | Jessey (States of)    | Aac | <b>0.78%</b> | 5.01%  |
|---------------------------|------|--------------|-------|-----------------------|-----|--------------|--------|
| Austria                   | Aal  | <b>0.36%</b> | 4.59% | Liechtenstein         | Aaa | <b>0.00%</b> | 4.23%  |
| Belgium                   | Aa3  | <b>0.78%</b> | 5.01% | Luxembourg            | Aaa | <b>0.00%</b> | 4.23%  |
| Cyprus                    | A3   | <b>1.55%</b> | 5.78% | Malta                 | A2  | <b>1.10%</b> | 5.33%  |
| Denmark                   | Aaa  | <b>0.00%</b> | 4.23% | Netherlands           | Aaa | <b>0.00%</b> | 4.23%  |
| Finland                   | Aal  | <b>0.36%</b> | 4.59% | Norway                | Aaa | <b>0.00%</b> | 4.23%  |
| France                    | Aa3  | <b>0.78%</b> | 5.01% | Portugal              | A3  | <b>1.55%</b> | 5.78%  |
| Germany                   | Aaa  | <b>0.00%</b> | 4.23% | Spain                 | A3  | <b>0.55%</b> | 5.78%  |
| Greece                    | Baal | <b>2.85%</b> | 5.08% | Sweden                | Aaa | <b>0.00%</b> | 4.23%  |
| Guernsey (States of)      | A1   | <b>0.91%</b> | 5.14% | Switzerland           | Aaa | <b>0.00%</b> | 4.23%  |
| Iceland                   | A1   | <b>0.91%</b> | 5.14% | Turkey                | B1  | <b>5.83%</b> | 10.06% |
| Ireland                   | Aa3  | <b>0.78%</b> | 5.01% | United Kingdom        | Aa3 | <b>0.78%</b> | 5.01%  |
| Isle of Man               | Aa3  | <b>0.78%</b> | 5.01% | <b>Western Europe</b> |     | <b>1.04%</b> | 5.78%  |
| Italy                     | Baa2 | <b>2.46%</b> | 6.69% |                       |     |              |        |

| Canada               | <b>Aaa</b> | <b>0.00%</b> | <b>4.23%</b> |  |  |  |  |  |
|----------------------|------------|--------------|--------------|--|--|--|--|--|
| United States        | <b>Aal</b> | <b>0.23%</b> | <b>4.46%</b> |  |  |  |  |  |
| <b>North America</b> |            | <b>0.22%</b> | <b>4.45%</b> |  |  |  |  |  |

| Caribbean            |             | <b>7.49%</b>        | <b>11.72%</b>       | Benin          | <b>5.83%</b> | <b>10.6%</b>  |
|----------------------|-------------|---------------------|---------------------|----------------|--------------|---------------|
|                      |             |                     |                     | Botswana       | <b>Baal</b>  | <b>2.07%</b>  |
|                      |             |                     |                     | Burkina Faso   | <b>Caal</b>  | <b>9.71%</b>  |
| Argentina            | <b>Caal</b> | <b>9.71%</b>        | <b>13.94%</b>       | Cameroon       | <b>Caal</b>  | <b>9.71%</b>  |
| Belize               | <b>Caal</b> | <b>9.71%</b>        | <b>13.94%</b>       | Cape Verde     | <b>B2</b>    | <b>7.12%</b>  |
| Bolivia              | <b>Ca</b>   | <b>15.54%</b>       | <b>19.77%</b>       | Congo (Dem Re. | <b>B3</b>    | <b>8.41%</b>  |
| Brazil               | <b>Bal</b>  | <b>3.24%</b>        | <b>7.47%</b>        | Congo (Rep. of | <b>Caa2</b>  | <b>11.66%</b> |
| Chile                | <b>A2</b>   | <b>1.10%</b>        | <b>5.33%</b>        | Côte d'Ivoire  | <b>Ba2</b>   | <b>3.90%</b>  |
| Colombia             | <b>Baa3</b> | <b>2.85%</b>        | <b>7.08%</b>        | Egypt          | <b>Caal</b>  | <b>9.71%</b>  |
| Costa Rica           | <b>Ba2</b>  | <b>3.90%</b>        | <b>8.13%</b>        | Ethiopia       | <b>Caa2</b>  | <b>11.66%</b> |
| Ecuador              | <b>Caa3</b> | <b>12.95%</b>       | <b>17.18%</b>       | Gabon          | <b>Caa2</b>  | <b>11.66%</b> |
| El Salvador          | <b>B3</b>   | <b>8.41%</b>        | <b>12.64%</b>       | Ghana          | <b>Caal</b>  | <b>9.71%</b>  |
| Guatemala            | <b>Bal</b>  | <b>3.24%</b>        | <b>7.47%</b>        | Kenya          | <b>Caal</b>  | <b>9.71%</b>  |
| Honduras             | <b>B1</b>   | <b>5.83%</b>        | <b>10.06%</b>       | Mali           | <b>Caa2</b>  | <b>11.66%</b> |
| Mexico               | <b>Baa2</b> | <b>2.46%</b>        | <b>6.69%</b>        | Mauritius      | <b>Baa3</b>  | <b>2.85%</b>  |
| Nicaragua            | <b>B2</b>   | <b>7.12%</b>        | <b>11.35%</b>       | Morocco        | <b>Bal</b>   | <b>3.24%</b>  |
| Panama               | <b>Baa3</b> | <b>2.85%</b>        | <b>7.08%</b>        | Mozambique     | <b>Caa3</b>  | <b>12.95%</b> |
| Paraguay             | <b>Baa3</b> | <b>2.85%</b>        | <b>7.08%</b>        | Namibia        | <b>B1</b>    | <b>5.83%</b>  |
| Peru                 | <b>Baal</b> | <b>2.07%</b>        | <b>6.30%</b>        | Niger          | <b>Caa3</b>  | <b>12.95%</b> |
| Suriname             | <b>Caal</b> | <b>9.71%</b>        | <b>13.94%</b>       | Nigeria        | <b>B3</b>    | <b>8.41%</b>  |
| Uruguay              | <b>Baal</b> | <b>2.07%</b>        | <b>6.30%</b>        | Rwanda         | <b>B2</b>    | <b>7.12%</b>  |
| Venezuela            | <b>C</b>    | <b>26.66%</b>       | <b>30.89%</b>       | Senegal        | <b>Caal</b>  | <b>9.71%</b>  |
| <b>Latin America</b> |             | <b><b>4.23%</b></b> | <b><b>8.46%</b></b> | South Africa   | <b>Ba2</b>   | <b>3.90%</b>  |
|                      |             |                     |                     | Swaziland      | <b>B2</b>    | <b>7.12%</b>  |
|                      |             |                     |                     | Tanzania       | <b>B1</b>    | <b>5.83%</b>  |
|                      |             |                     |                     | Togo           | <b>B3</b>    | <b>8.41%</b>  |
|                      |             |                     |                     | <b>Tunisia</b> | <b>Caal</b>  | <b>9.71%</b>  |

|  | Albania                | Baz  | 6.66%        | 8.89%  |
|--|------------------------|------|--------------|--------|
|  | Armenia                | Baz  | 6.66%        | 8.89%  |
|  | Azerbaijan             | Baz  | 2.66%        | 7.08%  |
|  | Belarus                | C    | 2.65%        | 30.89% |
|  | Bosnia and Herzegovina | Baz  | 6.41%        | 12.64% |
|  | Bulgaria               | Baal | 2.07%        | 6.30%  |
|  | Croatia                | A3   | 1.55%        | 5.78%  |
|  | Czech Republic         | Aa3  | 2.08%        | 5.01%  |
|  | Estonia                | A1   | 0.91%        | 5.14%  |
|  | Georgia                | Ba2  | 3.90%        | 8.13%  |
|  | Hungary                | Baa2 | 2.46%        | 6.69%  |
|  | Kazakhstan             | Baal | 2.07%        | 6.30%  |
|  | Kyrgyzstan             | B3   | 8.41%        | 12.64% |
|  | Latvia                 | A3   | 1.55%        | 5.78%  |
|  | Lithuania              | A2   | 1.10%        | 5.33%  |
|  | Macedonia              | Ba3  | 4.66%        | 8.89%  |
|  | Moldova                | B3   | 8.41%        | 12.64% |
|  | Montenegro             | B1   | 5.83%        | 10.06% |
|  | Poland                 | A2   | 1.10%        | 5.33%  |
|  | Romania                | Baa3 | 2.85%        | 7.08%  |
|  | Serbia                 | Ba2  | 3.90%        | 8.13%  |
|  | Slovakia               | A3   | 1.55%        | 5.78%  |
|  | Slovenia               | A3   | 2.07%        | 5.78%  |
|  | Tajikistan             | B3   | 8.41%        | 12.64% |
|  | Ukraine                | Ca   | 15.54%       | 19.77% |
|  | Uzbekistan             | Ba3  | 4.66%        | 8.89%  |
|  | E. Europe (no Russia)  |      | <b>3.35%</b> | 7.58%  |

| Abu Dhabi            | Aaa        | 0.64%        | 4.87%        |
|----------------------|------------|--------------|--------------|
| Bahrain              | B2         | 7.12%        | 11.35%       |
| Iraq                 | Caal       | 9.71%        | 13.94%       |
| Israel               | Baal       | 2.07%        | 6.30%        |
| Jordan               | Ba3        | 4.66%        | 8.89%        |
| Kuwait               | A1         | 0.91%        | 5.14%        |
| Lebanon              | C          | 26.66%       | 30.89%       |
| Oman                 | Baa3       | 2.85%        | 7.08%        |
| Qatar                | Aa2        | 0.64%        | 4.87%        |
| Ras Al Khaimah       | A3         | 1.55%        | 5.78%        |
| Saudi Arabia         | Aa3        | 0.78%        | 5.01%        |
| Sharjah              | Bal        | 3.24%        | 7.47%        |
| United Arab Emirates | Aa2        | 0.64%        | 4.87%        |
| <b>Middle East</b>   | <b>Aa2</b> | <b>2.01%</b> | <b>6.24%</b> |

Aswath Damodaran **Region: GDPweighted average**

|               | <i>Chapter</i> | <i>CPP</i> | <i>CPP</i> |
|---------------|----------------|------------|------------|
| Algeria       | 67             | 0.83%      | 10.06%     |
| Brunei        | 80.75          | 0.78%      | 0.01%      |
| Gambia        | 65.5           | 7.12%      | 11.35%     |
| Guinea        | 59.5           | 11.66%     | 15.79%     |
| Guinea-Bissa  | 60.75          | 9.71%      | 13.94%     |
| Guyana        | 75.5           | 2.07%      | 6.30%      |
| Haiti         | 56.75          | 12.95%     | 17.18%     |
| Iran          | 61.25          | 9.71%      | 13.94%     |
| Korea, D.P.R. | 51             | 15.54%     | 19.77%     |
| Liberia       | 57.5           | 11.66%     | 15.89%     |
| Libya         | 71.5           | 3.90%      | 8.13%      |
| Madagascar    | 62.5           | 8.41%      | 12.64%     |
| Malawi        | 56             | 12.95%     | 17.18%     |
| Myanmar       | 54.75          | 15.54%     | 19.77%     |
| Russia        | 70.25          | 3.90%      | 8.13%      |
| Sierra Leone  | 62.75          | 8.41%      | 12.64%     |
| Somalia       | 55.5           | 12.95%     | 17.18%     |
| Sudan         | 47.75          | 26.66%     | 30.89%     |
| Syria         | 51.5           | 15.54%     | 19.77%     |
| Yemen, Repub  | 51.75          | 15.54%     | 19.77%     |
| Zimbabwe      | 58.5           | 11.66%     | 15.89%     |

| Bangladesh       | B2   | 0.12%         | 11.35%        |
|------------------|------|---------------|---------------|
| Cambodia         | B2   | <b>7.12%</b>  | <b>11.35%</b> |
| China            | A1   | <b>0.91%</b>  | <b>5.14%</b>  |
| Fiji             | B1   | <b>5.83%</b>  | <b>10.06%</b> |
| Hong Kong        | Aa3  | <b>0.78%</b>  | <b>5.01%</b>  |
| India            | Baa3 | <b>2.46%</b>  | <b>7.08%</b>  |
| Indonesia        | Baa2 | <b>2.46%</b>  | <b>5.01%</b>  |
| Japan            | A1   | <b>0.91%</b>  | <b>5.14%</b>  |
| Korea            | Aa2  | <b>0.64%</b>  | <b>4.87%</b>  |
| Laos             | Caa2 | <b>11.66%</b> | <b>15.89%</b> |
| Macao            | Aa3  | <b>0.78%</b>  | <b>5.01%</b>  |
| Malaysia         | A1   | <b>1.55%</b>  | <b>4.87%</b>  |
| Maldives         | Caa2 | <b>11.66%</b> | <b>15.89%</b> |
| Mongolia         | B1   | <b>5.83%</b>  | <b>10.06%</b> |
| Nepal            | Ba3  | <b>4.66%</b>  | <b>8.89%</b>  |
| Pakistan         | Caa1 | <b>7.91%</b>  | <b>13.94%</b> |
| Papua New Guinea | B2   | <b>7.12%</b>  | <b>11.35%</b> |
| Philippines      | Baa2 | <b>2.46%</b>  | <b>6.08%</b>  |
| Singapore        | Aaa  | <b>0.00%</b>  | <b>4.23%</b>  |
| Solomon Islands  | Caa1 | <b>7.91%</b>  | <b>13.94%</b> |
| Sri Lanka        | Ca   | <b>15.54%</b> | <b>19.77%</b> |
| Taiwan           | Aa3  | <b>0.78%</b>  | <b>5.01%</b>  |
| Thailand         | Baa1 | <b>2.07%</b>  | <b>6.08%</b>  |
| Vietnam          | Ba2  | <b>3.90%</b>  | <b>8.13%</b>  |
| <b>Asia</b>      |      | <b>1.49%</b>  | <b>5.72%</b>  |

| <b>Australia</b>          | <b>Aaa</b>   | <b>0.00%</b> | <b>0.43%</b>  |
|---------------------------|--------------|--------------|---------------|
| Cook Islands              |              | <b>5.83%</b> | <b>10.06%</b> |
| New Zealand               | <b>Aaa</b>   | <b>0.00%</b> | <b>4.23%</b>  |
| <b>Australia &amp; NZ</b> | <b>0.00%</b> | <b>0.00%</b> | <b>4.23%</b>  |

# FROM COUNTRY EQUITY RISK PREMIUMS TO CORPORATE EQUITY RISK PREMIUMS

- ▪ **Approach 1:** Assume that every company in the country is equally exposed to country risk. In this case,
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \text{CRP} + \text{Beta (Mature ERP)}$
- ▪ **Approach 2:** Assume that a company's exposure to country risk is similar to its exposure to other market risk.
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (Mature ERP} + \text{CRP})$
- ▪ **Approach 3:** Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)
  - ▪  $E(\text{Return}) = \text{Riskfree Rate} + \beta (\text{Mature ERP}) + \lambda (\text{CRP})$
  - ▪  $\text{Mature ERP} = \text{Mature market Equity Risk Premium}$
  - ▪  $\text{CRP} = \text{Additional country risk premium}$

# ESTIMATING COUNTRY RISK PREMIUM EXPOSURE\_ VARIANTS

![](_page_55_Diagram_10.jpeg)

# OPERATION BASED CRP: SINGLE VERSUS MULTIPLE EMERGING MARKETS

- Single emerging market: Embraer, in 2004, reported that it derived 3% of its revenues in Brazil and the balance from mature markets. The mature market ERP in 2004 was 5% and Brazil's CRP was 7.89%.

|                             | Revenues | Total ERP    | CRP          |
|-----------------------------|----------|--------------|--------------|
| US and other mature markets | 97%      | 5.00%        | 0.00%        |
| Brazil                      | 3%       | 12.89%       | 8%           |
| <b>Embraer</b>              |          | <b>5.24%</b> | <b>0.24%</b> |

- Multiple emerging markets: Ambev, the Brazilian-based beverage company, reported revenues from the following countries during 2011.

|              | Revenues   | %      | Total ERP    | CRP          |
|--------------|------------|--------|--------------|--------------|
| Argentina    | 19         | 9.31%  | 15.00%       | 9.00%        |
| Bolivia      | 4          | 1.96%  | 10.88%       | 4.88%        |
| Brazil       | 130        | 63.73% | 8.63%        | 2.63%        |
| Canada       | 23         | 11.27% | 6.00%        | 0.00%        |
| Chile        | 7          | 3.43%  | 7.05%        | 1.05%        |
| Ecuador      | 6          | 2.94%  | 12.75%       | 6.75%        |
| Paraguay     | 3          | 1.47%  | 12.00%       | 6.00%        |
| Peru         | 12         | 5.88%  | 9.00%        | 3.00%        |
| <b>Ambev</b> | <b>204</b> |        | <b>9.11%</b> | <b>3.11%</b> |

# EXTENDING TO A MULTINATIONAL: REGIONAL BREAKDOWN COCA COLA'S REVENUE BREAKDOWN AND ERP IN 2012

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

Things to watch out for

1. 1. Aggregation across regions. For instance, the Pacific region often includes Australia & NZ with Asia
2. 2. Obscure aggregations including Eurasia and Oceania

# TWO PROBLEMS WITH THESE APPROACHES..

- ▪ **Focus just on revenues:** To the extent that revenues are the only variable that you consider, when weighting risk exposure across markets, you may be missing other exposures to country risk. For instance, an emerging market company that gets the bulk of its revenues outside the country (in a developed market) may still have all of its production facilities in the emerging market.
- ▪ **Exposure not adjusted or based upon beta:** To the extent that the country risk premium is multiplied by a beta, we are assuming that beta in addition to measuring exposure to all other macro economic risk also measures exposure to country risk.

# A PRODUCTION-BASED ERP: ROYAL DUTCH SHELL IN 2015

| Country                  | Oil & Gas Production | % of Total     | ERP          |
|--------------------------|----------------------|----------------|--------------|
| Denmark                  | 17396                | 3.83%          | 6.20%        |
| Italy                    | 11179                | 2.46%          | 9.14%        |
| Norway                   | 14337                | 3.16%          | 6.20%        |
| UK                       | 20762                | 4.57%          | 6.81%        |
| Rest of Europe           | 874                  | 0.19%          | 7.40%        |
| Brunei                   | 823                  | 0.18%          | 9.04%        |
| Iraq                     | 20009                | 4.40%          | 11.37%       |
| Malaysia                 | 22980                | 5.06%          | 8.05%        |
| Oman                     | 78404                | 17.26%         | 7.29%        |
| Russia                   | 22016                | 4.85%          | 10.06%       |
| Rest of Asia & ME        | 24480                | 5.39%          | 7.74%        |
| Oceania                  | 7858                 | 1.73%          | 6.20%        |
| Gabon                    | 12472                | 2.75%          | 11.76%       |
| Nigeria                  | 67832                | 14.93%         | 11.76%       |
| Rest of Africa           | 6159                 | 1.36%          | 12.17%       |
| USA                      | 104263               | 22.95%         | 6.20%        |
| Canada                   | 8599                 | 1.89%          | 6.20%        |
| Brazil                   | 13307                | 2.93%          | 9.60%        |
| Rest of Latin America    | 576                  | 0.13%          | 10.78%       |
| <b>Royal Dutch Shell</b> | <b>454326</b>        | <b>100.00%</b> | <b>8.26%</b> |

# ESTIMATE A LAMBDA FOR COUNTRY RISK

- ■ Country risk exposure is affected by **where you get your revenues and where your production happens**, but there are a host of other variables that also affect this exposure, including:
  - ■ Use of risk management products: Companies can use both options/futures markets and insurance to hedge some or a significant portion of country risk.
  - ■ Government “national” interests: There are sectors that are viewed as vital to the national interests, and governments often play a key role in these companies, either officially or unofficially. These sectors are more exposed to country risk.
- ■ It is conceivable that there is a **richer measure of country risk that incorporates all the variables that drive country risk in one measure**. That way my rationale when I devised “lambda” as my measure of country risk exposure.

# A REVENUE-BASED LAMBDA

- ▪ The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:
  - ▪  $\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{average firm}}$
- ▪ Consider two firms – Tata Motors and Tata Consulting Services, both Indian companies. In 2008-09, Tata Motors got about 91.37% of its revenues in India and TCS got 7.62%. The average Indian firm gets about 80% of its revenues in India:
  - ▪  $\lambda_{\text{Tata Motors}} = 91\%/80\% = 1.14$
  - ▪  $\lambda_{\text{TCS}} = 7.62\%/80\% = 0.09$
- ▪ There are two implications
  - ▪ A company's risk exposure is determined by where it does business and not by where it is incorporated.
  - ▪ Firms might be able to actively manage their country risk exposures

# A PRICE/RETURN BASED LAMBDA

$$\text{Return}_{\text{Embraer}} = 0.0195 + 0.2681 \text{ Return}_{\text{C Bond}}$$

$$\text{Return}_{\text{Embratel}} = -0.0308 + 2.0030 \text{ Return}_{\text{C Bond}}$$

![](_page_62_Figure_152.jpeg)

![](_page_62_Figure_153.jpeg)

# ESTIMATING A US DOLLAR COST OF EQUITY FOR EMBRAER - SEPTEMBER 2004

- ▪ Assume that the beta for Embraer is 1.07, and that the US \$ riskfree rate used is 4%. Also assume that the risk premium for the US is 5% and the country risk premium for Brazil is 7.89%. Finally, assume that Embraer gets 3% of its revenues in Brazil & the rest in the US.
- ▪ There are five estimates of \$ cost of equity for Embraer:
  - ▪ **Approach 1:** Constant exposure to CRP, Location CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + 7.89\% = 17.24\%$
  - ▪ **Approach 2:** Constant exposure to CRP, Operation CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + (0.03 * 7.89\% + 0.97 * 0\%) = 9.59\%$
  - ▪ **Approach 3:** Beta exposure to CRP, Location CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\% + 7.89\%) = 17.79\%$
  - ▪ **Approach 4:** Beta exposure to CRP, Operation CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\% + (0.03 * 7.89\% + 0.97 * 0\%)) = 9.60\%$
  - ▪ Approach 5: Lambda exposure to CRP
    - ▪  $E(\text{Return}) = 4\% + 1.07 (5\%) + 0.27(7.89\%) = 11.48\%$

# VALUING EMERGING MARKET COMPANIES WITH SIGNIFICANT EXPOSURE IN DEVELOPED MARKETS

- ■ The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk.
- ■ Thus, in 2004, Embraer would have been valued with a cost of equity of 17-18% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
  - ■ Emerging market companies with substantial exposure in developed markets will be assessed too low a value (look significantly over valued) by analysts
  - ■ Emerging market companies with substantial exposure in developed markets assessed too high a value (look significantly under valued) by analysts
- ■ Can you construct an investment strategy to take advantage of the mis-valuation? What would need to happen for you to make money of this strategy?

# IMPLIED EQUITY PREMIUMS

- ▪ **For a start:** If you know the price paid for an asset and have estimates of the expected cash flows on the asset, you can estimate the IRR of these cash flows. If you paid the price, this is your expected return.
- ▪ **Stock Price & Risk:** If you assume that stocks are correctly priced in the aggregate and you can estimate the expected cashflows from buying stocks, you can estimate the expected rate of return on stocks by finding that discount rate that makes the present value equal to the price paid.
- ▪ **Implied ERP:** Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward-looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

# A FORWARD-LOOKING NUMBER

## Implied Equity Risk Premium: Generic Version

Analyst estimates of growth in earnings for the near term, scaling down to a growth rate = riskfree rate, in perpetuity.

Growth rate in perpetuity = Riskfree Rate

Base year Cash flows from owning Equities = Dividends + Buybacks

Cash payout as a percent of earnings, adjusted for changing growth over time.

CFs continue in perpetuity

![](_page_66_Figure_19.jpeg)

Solve for  $r$ 

 $E(\text{Return on Stocks}) = \text{Discount rate that makes the present value of the expected cash flows equal to stock (index) price today}$   
 $ERP = E(\text{Return on Stocks}) - \text{Riskfree Rate}$ 

The implied equity risk premium is a number backed out from what investors are paying for stocks and their expected cash flows from holding stocks. It is an internal rate of return for equity investors, analogous to a yield to maturity for a bondholder.

# EQUITY RISK PREMIUM: JANUARY 2020

![](_page_67_Diagram_21.jpeg)

# AND IN 2020.. COVID EFFECTS

![](_page_68_Figure_10.jpeg)

# AN UPDATED ESTIMATE: ERP IN 2026

![](_page_69_Diagram_19.jpeg)

# IMPLIED PREMIUMS IN THE US: 1960-2025

*Implied Equity Risk Premium for US Equity Market: 1960-2025*

![](_page_70_Figure_11.jpeg)

# IMPLIED PREMIUM VERSUS RISK FREE RATE

![](_page_71_Figure_10.jpeg)

# EQUITY RISK PREMIUMS AND BOND DEFAULT SPREADS

![](_page_72_Figure_10.jpeg)

# EQUITY RISK PREMIUMS AND CAP RATES (REAL ESTATE)

![](_page_73_Figure_10.jpeg)

# WHY IMPLIED PREMIUMS MATTER?

- ■ In many investment banks, it is **common practice (especially in corporate finance departments) to use historical risk premiums** (and arithmetic averages at that) as risk premiums to compute cost of equity. Often, the defense they offer is that as long as **everyone uses the same premium, there is no cost to being wrong**.
- ■ If all analysts in a group used the arithmetic average premium (for stocks over T.Bills) for 1928-2024 of 8.44% to value stocks in January 2025, given the implied premium of 4.33%, what are they likely to find?
  - a. The values they obtain will be too low (most stocks will look overvalued)
  - b. The values they obtain will be too high (most stocks will look under valued)
  - c. There should be no systematic bias as long as they use the same premium to value all stocks.

# WHICH EQUITY RISK PREMIUM SHOULD YOU USE?

| If you assume this                                                                 | Premium to use                                 |
|------------------------------------------------------------------------------------|------------------------------------------------|
| Premiums revert back to historical norms and your time period yields these norms   | Historical risk premium                        |
| Market is correct in the aggregate or that your valuation should be market neutral | Current implied equity risk premium            |
| Marker makes mistakes even in the aggregate but is correct over time               | Average implied equity risk premium over time. |

| Predictor                           | Correlation with implied premium next year | Correlation with actual return- next 5 years | Correlation with actual return – next 10 years |
|-------------------------------------|--------------------------------------------|----------------------------------------------|------------------------------------------------|
| <b>Current implied premium</b>      | 0.763                                      | 0.427                                        | 0.500                                          |
| <b>Average implied premium:</b>     | 0.718                                      | 0.326                                        | 0.450                                          |
| <b>Last 5 years</b>                 |                                            |                                              |                                                |
| <b>Historical Premium</b>           | -0.497                                     | -0.437                                       | -0.454                                         |
| <b>Default Spread based premium</b> | 0.047                                      | 0.143                                        | 0.160                                          |

# AN ERP FOR THE SENSEX

- ▪ Inputs for the computation
  - ▪ Sensex on 9/5/07 = 15446
  - ▪ Dividend yield on index = 3.05%
  - ▪ Expected growth rate - next 5 years = 14%
  - ▪ Growth rate beyond year 5 = 6.76% (set equal to riskfree rate)
- ▪ Solving for the expected return:

$$15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$$

- ▪ Expected return on stocks = 11.18%
- ▪ Implied equity risk premium for India = 11.18% - 6.76% = 4.42%

# THE EVOLUTION OF EMERGING MARKET RISK

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

![](_page_78_Picture_13.jpeg)

# DISCOUNT RATES: III

## Relative Risk Measures

# THE CAPM BETA: THE MOST USED (AND MISUSED) RISK MEASURE

- ▪ The standard procedure for estimating betas is to regress stock returns ( $R_j$ ) against market returns ( $R_m$ ) -
  - ▪  $R_j = a + b R_m$
  - ▪ where  $a$  is the intercept and  $b$  is the slope of the regression.
- ▪ The **slope of the regression** corresponds to the beta of the stock and measures the riskiness of the stock.
- ▪ This beta has three problems:
  - ▪ It has high standard error
  - ▪ It reflects the firm's business mix over the period of the regression, not the current mix
  - ▪ It reflects the firm's average financial leverage over the period rather than the current leverage.

# UNRELIABLE, WHEN IT LOOKS BAD..

![](_page_80_Figure_10.jpeg)

# OR WHEN IT LOOKS GOOD..

<HELP> for explanation, <MENU> for similar functions.  
Screen Printed

P255 Equity BETA

## HISTORICAL BETA

**NOKIV FH Equity**

Relative Index **HEX**

Period **Weekly**  
Range **8/14/98** To **8/4/00**  
Market **Trade**

| <b>ADJ BETA</b>   | 1.18 |
|-------------------|------|
| <b>RAW BETA</b>   | 1.27 |
| Alpha(Intercept)  | 0.42 |
| R2 (Correlation)  | 0.94 |
| Std Dev of Error  | 1.87 |
| Std Error of Beta | 0.03 |
| Number of Points  | 103  |

NOKIA OYJ

HEX GENERAL INDEX  
\*Indentifies latest observation

![](_page_81_Figure_39.jpeg)

$$ADJ \text{ BETA} = (0.67) * \text{RAW BETA} + (0.33) * 1.0$$

Copyright 2000 BLOOMBERG L.P. Frankfurt:69-920410 Hong Kong:2-977-6000 London:207-330-7500 New York:212-318-2000  
Princeton:609-279-3000 Singapore:226-3000 Sydney:2-9777-8686 Tokyo:3-3201-8900 Sao Paulo:11-3048-4500  
1653-197-0 11-Aug-00 14:56:13

![](_page_81_Picture_42.jpeg)

# ONE SLICE OF HISTORY.

Market Summary > GameStop Corp.  
NYSE: GME

+ Follow

**50.99** USD **-0.11 (0.22%)** ↓

Feb 12, 2:44 PM EST · Disclaimer

1 day 5 days 1 month 6 months YTD 1 year 5 years Max

![](_page_82_Figure_26.jpeg)

![](_page_82_Figure_27.jpeg)

During 2019 and 2020, GME was an extraordinarily volatile stock, as short sellers and long only investors fought out a battle.

# AND SUBJECT TO GAME PLAYING

![](_page_83_Figure_10.jpeg)

![](_page_83_Figure_11.jpeg)

# MEASURING RELATIVE RISK: YOU DON'T LIKE BETAS OR MODERN PORTFOLIO THEORY? NO PROBLEM.

![](_page_84_Diagram_10.jpeg)

# DON'T LIKE THE DIVERSIFIED INVESTOR FOCUS, BUT OKAY WITH PRICE-BASED MEASURES

- ▪ Relative Standard Deviation
  - ▪ Relative Volatility = Std dev of Stock/ Average Std dev across all stocks
  - ▪ Captures all risk, rather than just market risk
- ▪ Proxy Models
  - ▪ Look at historical returns on all stocks and look for variables that explain differences in returns.
  - ▪ You are, in effect, running multiple regressions with returns on individual stocks as the dependent variable and fundamentals about these stocks as independent variables.
  - ▪ This approach started with market cap (the small cap effect) and over the last two decades has added other variables (momentum, liquidity etc.)
- ▪ CAPM Plus Models
  - ▪ Start with the traditional CAPM ( $R_f + Beta (ERP)$ ) and then add other premiums for proxies.

# DON'T LIKE THE PRICE-BASED APPROACH..

- ▪ **Accounting risk measures:** To the extent that you don't trust market-priced based measures of risk, you could compute relative risk measures based on
  - ▪ *Accounting earnings volatility:* Compute an accounting beta or relative volatility
  - ▪ *Balance sheet ratios:* You could compute a risk score based upon accounting ratios like debt ratios or cash holdings (akin to default risk scores like the Z score)
- ▪ **Qualitative Risk Models:** In these models, risk assessments are based at least partially on qualitative factors (quality of management).
- ▪ **Debt based measures:** You can estimate a cost of equity, based upon an observable costs of debt for the company.
  - ▪ Cost of equity = Cost of debt \* Scaling factor
  - ▪ The scaling factor can be computed from implied volatilities.

# DETERMINANTS OF BETAS & RELATIVE RISK

## Beta of Equity (Levered Beta)

![](_page_87_Diagram_159.jpeg)

# IN A PERFECT WORLD... WE WOULD ESTIMATE THE BETA OF A FIRM BY DOING THE FOLLOWING

![](_page_88_Diagram_30.jpeg)

# ADJUSTING FOR OPERATING LEVERAGE...

- ▪ Within any business, firms with **lower fixed costs (as a percentage of total costs) should have lower unlevered betas**. If you can compute fixed and variable costs for each firm in a sector, you can break down the unlevered beta into business and operating leverage components.
  - ▪ Unlevered beta = Pure business beta \* (1 + (Fixed costs/ Variable costs))
- ▪ The biggest problem with doing this is **informational**. It is difficult to get information on fixed and variable costs for individual firms.
- ▪ In practice, **we tend to assume that the operating leverage of firms within a business are similar** and use the same unlevered beta for every firm.

# ADJUSTING FOR FINANCIAL LEVERAGE...

- ▪ **Conventional approach:** If we assume that debt carries no market risk (has a beta of zero), the beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio
  - ▪  $\beta_L = \beta_u (1 + ((1-t)D/E))$
  - ▪ In some versions, the tax effect is ignored and there is no  $(1-t)$  in the equation.
- ▪ **Debt Adjusted Approach:** If beta carries market risk and you can estimate the beta of debt, you can estimate the levered beta as follows:
  - ▪  $\beta_L = \beta_u (1 + ((1-t)D/E)) - \beta_{\text{debt}} (1-t) (D/E)$
  - ▪ While the latter is more realistic, estimating betas for debt can be difficult to do.

# BOTTOM-UP BETAS

Step 1: Find the business or businesses that your firm operates in.

**Possible Refinements**

Step 2: Find publicly traded firms in each of these businesses and obtain their regression betas. Compute the simple average across these regression betas to arrive at an average beta for these publicly traded firms. Unlever this average beta using the average debt to equity ratio across the publicly traded firms in the sample.  
 Unlevered beta for business = Average beta across publicly traded firms/  $(1 + (1-t))$  (Average D/E ratio across firms))

If you can, adjust this beta for differences between your firm and the comparable firms on operating leverage and product characteristics.

Step 3: Estimate how much value your firm derives from each of the different businesses it is in.

While revenues or operating income are often used as weights, it is better to try to estimate the value of each business.

Step 4: Compute a weighted average of the unlevered betas of the different businesses (from step 2) using the weights from step 3.  
 Bottom-up Unlevered beta for your firm = Weighted average of the unlevered betas of the individual business

If you expect the business mix of your firm to change over time, you can change the weights on a year-to-year basis.

Step 5: Compute a levered beta (equity beta) for your firm, using the market debt to equity ratio for your firm.  
 Levered bottom-up beta = Unlevered beta  $(1 + (1-t))$  (Debt/Equity))

If you expect your debt to equity ratio to change over time, the levered beta will change over time.

# WHY BOTTOM-UP BETAS?

- ▪ **Less Noisy:** The standard error in a bottom-up beta will be significantly lower than the standard error in a single regression beta. Roughly speaking, the standard error of a bottom-up beta estimate can be written as follows:

- - ▪ Std error of bottom-up beta =  $\frac{\text{Average Std Error across Betas}}{\sqrt{\text{Number of firms in sample}}}$

- ▪ **Updated:** The bottom-up beta can be adjusted to reflect changes in the firm's business mix and financial leverage. Regression betas reflect the past.
- ▪ **Don't need prices:** You can estimate bottom-up betas even when you do not have historical stock prices. This is the case with initial public offerings, private businesses or divisions of companies.

# ESTIMATING BOTTOM UP BETAS & COSTS OF EQUITY: VALE

| Business        | Sample                                                  | Sample size | Unlevered beta of business | Revenues | Peer Group EV/Sales | Value of Business | Proportion of Vale |
|-----------------|---------------------------------------------------------|-------------|----------------------------|----------|---------------------|-------------------|--------------------|
| Metals & Mining | Global firms in metals & mining, Market cap>\$1 billion | 48          | 0.86                       | \$9,013  | 1.97                | \$17,739          | 16.65%             |
| Iron Ore        | Global firms in iron ore                                | 78          | 0.83                       | \$32,717 | 2.48                | \$81,188          | 76.20%             |
| Fertilizers     | Global specialty chemical firms                         | 693         | 0.99                       | \$3,777  | 1.52                | \$5,741           | 5.39%              |
| Logistics       | Global transportation firms                             | 223         | 0.75                       | \$1,644  | 1.14                | \$1,874           | 1.76%              |
| Vale Operations |                                                         |             | 0.8440                     | \$47,151 |                     | \$106,543         | 100.00%            |

| Business        | Unlevered beta | D/E ratio | Levered beta | Risk free rate | ERP   | Cost of Equity |
|-----------------|----------------|-----------|--------------|----------------|-------|----------------|
| Metals & Mining | 0.86           | 54.99%    | 1.1657       | 2.75%          | 7.38% | 11.35%         |
| Iron Ore        | 0.83           | 54.99%    | 1.1358       | 2.75%          | 7.38% | 11.13%         |
| Fertilizers     | 0.99           | 54.99%    | 1.3493       | 2.75%          | 7.38% | 12.70%         |
| Logistics       | 0.75           | 54.99%    | 1.0222       | 2.75%          | 7.38% | 10.29%         |
| Vale Operations | 0.84           | 54.99%    | 1.1503       | 2.75%          | 7.38% | 11.23%         |

# EMBRAER'S BOTTOM-UP BETA

| <i>Business</i> | <i>Unlevered Beta D/E Ratio</i> | <i>Levered beta</i> |      |
|-----------------|---------------------------------|---------------------|------|
| Aerospace       | 0.95                            | 18.95%              | 1.07 |

$$\begin{aligned}\text{Levered Beta}_{\text{Embraer}} &= \text{Unlevered Beta} \left( 1 + (1 - \text{tax rate}) \left( \frac{D/E \text{ Ratio}}{0.95} \right) \right) \\ &= 0.95 \left( 1 + (1 - .34) (.1895) \right) = 1.07\end{aligned}$$

- ■ Can an unlevered beta estimated using U.S. and European aerospace companies be used to estimate the beta for a Brazilian aerospace company?
  - a. Yes
  - b. No

What concerns would you have in making this assumption?

# GROSS DEBT VERSUS NET DEBT APPROACHES

- ▪ Analysts in Europe and Latin America often take **the difference between debt and cash (net debt)** when computing debt ratios and arrive at very different values.
- ▪ For Embraer, using the **gross debt ratio**
  - ▪ Gross D/E Ratio for Embraer =  $1953/11,042 = 18.95\%$
  - ▪ Levered Beta using Gross Debt ratio =  $1.07$
- ▪ Using the **net debt ratio**, we get
  - ▪ Net Debt Ratio for Embraer =  $(\text{Debt} - \text{Cash})/ \text{Market value of Equity}$   
     $= (1953-2320)/ 11,042 = -3.32\%$
  - ▪ Levered Beta using Net Debt Ratio =  $0.95 (1 + (1-3.34)(-0.0332)) = 0.93$
- ▪ The cost of Equity using net debt levered beta for Embraer will be much lower than with the gross debt approach. The cost of capital for Embraer will even out since the debt ratio used in the cost of capital equation will now be a net debt ratio rather than a gross debt ratio.

# THE COST OF EQUITY: A RECAP

![](_page_96_Diagram_92.jpeg)

![](_page_97_Picture_12.jpeg)

# DISCOUNT RATES: IV

Mopping up

# ESTIMATING THE COST OF DEBT

- ▪ The **cost of debt is the rate at which you can borrow money, long term right now**, It will reflect not only your default risk but also the level of interest rates in the market.
- ▪ The cost of debt is not the rate at which you have borrowed money in the past or a current book interest rate (interest expense/debt).
- ▪ The two most widely used approaches to estimating cost of debt are:
  - ▪ Looking up the **yield to maturity on a straight bond outstanding from the firm**. The limitation of this approach is that very few firms have long term straight bonds that are liquid and widely traded
  - ▪ Looking up the rating for the firm and **estimating a default spread based upon the rating**. While this approach is more robust, different bonds from the same firm can have different ratings. You have to use a median rating for the firm
- ▪ When in trouble (either because you have no ratings or multiple ratings for a firm), estimate a **synthetic rating for your firm** and the cost of debt based upon that rating.

# ESTIMATING SYNTHETIC RATINGS

- ▪ The rating for a firm can be estimated using **the financial characteristics of the firm**. In its simplest form, the rating can be estimated from the interest coverage ratio
  - ▪ Interest Coverage Ratio =  $\frac{\text{EBIT}}{\text{Interest Expenses}}$
- ▪ For Embraer's interest coverage ratio, we used the interest expenses from 2003 and the **average EBIT from 2001 to 2003**. (The aircraft business was badly affected by 9/11 and its aftermath. In 2002 and 2003, Embraer reported significant drops in operating income)
  - ▪ Interest Coverage Ratio =  $462.1 / 129.70 = 3.56$

# INTEREST COVERAGE RATIOS, RATINGS AND DEFAULT SPREADS: 2004

If Interest Coverage Ratio is

| > 8.50      | (>12.50)   |
|-------------|------------|
| 6.50 - 8.50 | (9.5-12.5) |
| 5.50 - 6.50 | (7.5-9.5)  |
| 4.25 - 5.50 | (6-7.5)    |
| 3.00 - 4.25 | (4.5-6)    |
| 2.50 - 3.00 | (4-4.5)    |
| 2.25- 2.50  | (3.5-4)    |
| 2.00 - 2.25 | ((3-3.5)   |
| 1.75 - 2.00 | (2.5-3)    |
| 1.50 - 1.75 | (2-2.5)    |
| 1.25 - 1.50 | (1.5-2)    |
| 0.80 - 1.25 | (1.25-1.5) |
| 0.65 - 0.80 | (0.8-1.25) |
| 0.20 - 0.65 | (0.5-0.8)  |
| < 0.20      | (<0.5)     |

Estimated Bond Rating

| AAA |
|-----|
| AA  |
| A+  |
| A   |
| A-  |
| BBB |
| BB+ |
| BB  |
| B+  |
| B   |
| B - |
| CCC |
| CC  |
| C   |
| D   |

Default  
Spread

| 0.35%  |
|--------|
| 0.50%  |
| 0.70%  |
| 0.85%  |
| 1.00%  |
| 1.50%  |
| 2.00%  |
| 2.50%  |
| 3.25%  |
| 4.00%  |
| 6.00%  |
| 8.00%  |
| 10.00% |
| 12.00% |
| 20.00% |

# COST OF DEBT COMPUTATIONS

- ▪ Based on the interest coverage ratio of 3.56, the synthetic rating for Embraer is A-, giving it a default spread of 1.00%
- ▪ Companies in countries with low bond ratings and high default risk **might bear the burden of country default risk**, especially if they are smaller or have all of their revenues within the country.
  - ▪ If I assume that Embraer bears all of the country risk burden, I would add on the country default spread for Brazil in 2004 of 6.01%.
  - ▪ Larger companies that **derive a significant portion of their revenues in global markets may be less exposed to country default risk**. I am going to add only two thirds of the Brazilian country risk (based upon traded bond spreads of other large Brazilian companies in 2004)

$$\text{Cost of debt} = \text{Riskfree rate} + 2/3(\text{Brazil country default spread}) + \text{Company default spread} = 4.29\% + 2/3 (6.01\%) + 1.00\% = 9.29\%$$

# SYNTHETIC RATINGS: SOME CAVEATS

- ■ The relationship between interest coverage ratios and ratings, developed using US companies, **tends to travel well**, as long as we are analyzing large manufacturing firms in markets with interest rates close to the US interest rate
- ■ They are more problematic when looking at smaller companies in **markets with higher interest rates** than the US. One way to adjust for this difference is modify the interest coverage ratio table to reflect interest rate differences (For instances, if interest rates in an emerging market are twice as high as rates in the US, halve the interest coverage ratio).

# DEFAULT SPREADS: CHANGE IS A CONSTANT

![](_page_103_Figure_11.jpeg)

| Date                  | AAA          | AA           | A            | BBB          | BB           | B            | 0            |
|-----------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| 1/1/22                | 0.51%        | 0.62%        | 0.78%        | 1.21%        | 2.11%        | 3.51%        | 6.78%        |
| 2/1/22                | 0.62%        | 0.70%        | 0.87%        | 1.33%        | 2.55%        | 3.83%        | 7.22%        |
| 3/1/22                | 0.70%        | 0.83%        | 1.07%        | 1.64%        | 2.86%        | 4.23%        | 7.82%        |
| 4/1/22                | 0.58%        | 0.73%        | 0.97%        | 1.47%        | 2.33%        | 3.73%        | 7.27%        |
| 5/1/22                | 0.70%        | 0.87%        | 1.17%        | 1.72%        | 2.90%        | 4.30%        | 8.69%        |
| 6/1/22                | 0.60%        | 0.81%        | 1.11%        | 1.70%        | 2.67%        | 4.56%        | 9.70%        |
| 7/1/22                | 0.71%        | 0.97%        | 1.33%        | 2.05%        | 4.19%        | 6.61%        | 12.05%       |
| 8/1/22                | 0.60%        | 0.86%        | 1.21%        | 1.91%        | 3.15%        | 5.35%        | 10.97%       |
| 9/1/22                | 0.65%        | 0.86%        | 1.21%        | 1.88%        | 3.47%        | 5.34%        | 11.89%       |
| 9/23/22               | 0.65%        | 0.86%        | 1.23%        | 1.87%        | 3.46%        | 5.36%        | 12.25%       |
| <b>Change in 2022</b> | <b>0.14%</b> | <b>0.24%</b> | <b>0.45%</b> | <b>0.66%</b> | <b>1.35%</b> | <b>1.85%</b> | <b>5.47%</b> |

# DEFAULT SPREADS – JANUARY 2026

*Corporate Bond Default Spreads on January 1, 2026*

![](_page_104_Figure_261.jpeg)

# SUBSIDIZED DEBT: WHAT SHOULD WE DO?

- ▪ Assume that the Brazilian government lends money to Embraer at a subsidized interest rate (say 6% in dollar terms). In computing the cost of capital to value Embraer, should we use the cost of debt based upon default risk or the subsidized cost of debt?
  - a. The subsidized cost of debt (6%). That is what the company is paying.
  - b. The fair cost of debt (9.25%). That is what the company should require its projects to cover.
  - c. A number in the middle.

# WEIGHTS FOR THE COST OF CAPITAL COMPUTATION

- ▪ In computing the cost of capital for a publicly traded firm, the general rule for computing weights for debt and equity is that you use market value weights (and not book value weights). Why?
  - a. Because the market is usually right
  - b. Because market values are easy to obtain
  - c. Because book values of debt and equity are meaningless
  - d. None of the above
- ▪ If a company is not traded, and there is no market value available, would it be reasonable to use book value?
  - a. Yes. There is no choice
  - b. No. There is a choice  
    If there is a choice, what is it?

# ESTIMATING COST OF CAPITAL: EMBRAER IN 2004

- ■ Equity

- - ■ Cost of Equity =  $4.29\% + 1.07 (4\%) + 0.27 (7.89\%) = 10.70\%$
  - ■ Market Value of Equity = 11,042 million BR (\$ 3,781 million)

- ■ Debt

- - ■ Cost of debt =  $4.29\% + 4.00\% + 1.00\% = 9.29\%$
  - ■ Market Value of Debt = 2,083 million BR (\$713 million)

- ■ Cost of Capital =  $10.70 \% (.84) + 9.29\% (1 - .34) (0.16)) = 9.97\%$

- - ■ The book value of equity at Embraer is 3,350 million BR.
  - ■ The book value of debt at Embraer is 1,953 million BR; Interest expense is 222 mil BR; Average maturity of debt = 4 years
  - ■ Estimated market value of debt = 222 million (PV of annuity, 4 years, 9.29%) +  $\$1,953 \text{ million} / 1.0929^4 = 2,083 \text{ million BR}$

# IF YOU HAD TO DO IT...CONVERTING A DOLLAR COST OF CAPITAL TO A NOMINAL REAL COST OF CAPITAL

- ▪ **Approach 1:** Use a **\$R riskfree rate** in all of the calculations above. For instance, if the \$R riskfree rate was 12%, the cost of capital would be computed as follows:
  - ▪ Cost of Equity = 12% + 1.07(4%) + 0.27 (7.89%) = 18.41%
  - ▪ Cost of Debt = 12% + 1% = 13%
  - ▪ (This assumes the riskfree rate has no country risk premium embedded in it.)
- ▪ **Approach 2:** Use the differential inflation rate to estimate the cost of capital. For instance, if the inflation rate in \$R is 8% and the inflation rate in the U.S. is 2%

- ▪ 
  $$1 + \text{Cost of capital}_{\$R} = (1 + \text{Cost of Capital}_{\$}) \left[ \frac{1 + \text{Inflation}_{\text{BR}}}{1 + \text{Inflation}_{\$}} \right]$$
  $$= 1.0997 (1.08/1.02) - 1 = 0.1644 \text{ or } 16.44\%$$

# DEALING WITH HYBRIDS AND PREFERRED STOCK

- ■ When dealing with hybrids (convertible bonds, for instance), **break the security down into debt and equity** and allocate the amounts accordingly. Thus, if a firm has \$ 125 million in convertible debt outstanding, break the \$125 million into straight debt and conversion option components. The conversion option is equity.
- ■ When dealing with **preferred stock**, **it is better to keep it as a separate component**. The cost of preferred stock is the preferred dividend yield. (As a rule of thumb, if the preferred stock is less than 5% of the outstanding market value of the firm, lumping it in with debt will make no significant impact on your valuation).

# DECOMPOSING A CONVERTIBLE BOND . . .

- ▪ Assume that the firm that you are analyzing has \$125 million in face value of convertible debt with a stated interest rate of 4%, a 10-year maturity and a market value of \$140 million. If the firm has a bond rating of A and the interest rate on A-rated straight bond is 8%, you can break down the value of the convertible bond into straight debt and equity portions.
  - ▪ Straight debt =  $(4\% \text{ of } \$125 \text{ million}) (\text{PV of annuity, 10 years, 8\%}) + 125 \text{ million} / 1.08^{10} = \$91.45 \text{ million}$
  - ▪ Equity portion =  $\$140 \text{ million} - \$91.45 \text{ million} = \$48.55 \text{ million}$
- ▪ The debt portion (\$91.45 million) gets added to debt and the option portion (\$48.55 million) gets added to the market capitalization to get to the debt and equity weights in the cost of capital.

# RECAPPING THE COST OF CAPITAL

![](_page_111_Diagram_49.jpeg)

![](_page_112_Picture_4.jpeg)

# ESTIMATING CASH FLOWS

Cash is king...

# FREE CASH FLOW: FCFE AND FCFF

*Free Cash Flow to Equity*

![](_page_113_Diagram_15.jpeg)

*Free Cash Flow to Firm*

![](_page_113_Diagram_17.jpeg)

# STEPS IN CASH FLOW ESTIMATION

- ▪ Estimate the **current earnings of the firm**
  - ▪ If looking at cash flows to equity, look at earnings after interest expenses - i.e. **net income**
  - ▪ If looking at cash flows to the firm, look at **operating earnings after taxes**
- ▪ Consider **how much the firm invested to create future growth**
  - ▪ If the investment is not expensed, it will be categorized as capital expenditures. To the extent that depreciation provides a cash flow, it will cover some of these expenditures.
  - ▪ Increasing working capital needs are also investments for future growth
- ▪ If looking at cash flows to equity, consider **the cash flows from net debt issues** (debt issued - debt repaid)

# MEASURING FREE CASH FLOW TO THE FIRM: THREE PATHWAYS TO THE SAME END GAME

$$\frac{\text{EBIT (1 - tax rate)}}{minus} + \frac{\text{(Cap Ex - Depreciation)}}{\text{Change in non-cash Working capial}} = \frac{\text{FCFF}}{\text{Reinvestment}}$$
$$\frac{\text{EBIT (1 - tax rate)}}{minus} = \frac{\text{FCFF}}{\text{(1 - Reinvestment Rate)}}$$
$$\frac{\text{EBIT (1 - tax rate)}}{x} = \frac{\text{FCFF}}{\text{(1 - Reinvestment Rate)}}$$

Where are the tax savings from interest expenses?

# MEASURING FREE CASH FLOW TO EQUITY: ALTERNATIVE PATHWAYS

$$\text{Net Income} \quad \text{minus} \quad \frac{(\text{Capital Ex - Depreciation}) + \text{Change in non-cash Working Capital}}{\text{Working Capital}} \quad \text{Plus} \quad \frac{(\text{New Debt Issued - Debt Repaid})}{} = \text{FCFE}$$

$$\text{Net Income} \quad \text{minus} \quad \text{Reinvestment} \quad \text{Plus} \quad \frac{\text{Net Debt Cashflow}}{} = \text{FCFE}$$

$$\text{Net Income} \quad \times \quad \frac{(1 - \text{Equity Reinvestment Rate})}{} = \text{FCFE}$$

$$\text{Equity Reinvestment Rate} = \frac{(\text{Reinvestment - Net Debt Cashflow})}{\text{Net Income}}$$

# MICROSOFT IN 2021: FCFE AND FCFF

![](_page_117_Figure_11.jpeg)

![](_page_117_Figure_12.jpeg)

![](_page_118_Picture_4.jpeg)

# CASH FLOWS I

Accounting Earnings, Flawed but Important

# FROM REPORTED TO ACTUAL EARNINGS

![](_page_119_Diagram_74.jpeg)

# 1. UPDATING EARNINGS

- ▪ When valuing companies, we often depend upon financial statements for inputs on earnings and assets. Annual reports are often outdated and can be updated by using-
  - ▪ **Trailing 12-month data**, constructed from quarterly earnings reports.
  - ▪ **Informal and unofficial news reports**, if quarterly reports are unavailable.
- ▪ Updating makes the **most difference for smaller and more volatile firms**, as well as for firms that have undergone significant restructuring.
- ▪ **Time saver:** To get a trailing 12-month number, all you need is one 10K and one 10Q (example third quarter). For example, to get trailing revenues from a third quarter 10Q:
  - ▪ Trailing 12-month Revenue = Revenues (in last 10K) - Revenues from first 3 quarters of last year + Revenues from first 3 quarters of this year.

## 2. CORRECTING ACCOUNTING EARNINGS

- ▪ Make sure that there are no financial expenses mixed in with operating expenses
  - ▪ **Financial expense:** Any commitment that is tax deductible that you have to meet no matter what your operating results: Failure to meet it leads to loss of control of the business.
  - ▪ Until 2019, accounting convention treated operating leases as operating expenses, skewing income statements & balance sheets.
- ▪ Make sure that there are no capital expenses mixed in with the operating expenses
  - ▪ **Capital expense:** Any expense that is expected to generate benefits over multiple periods.
  - ▪ There are a shole host of expenses (like R&D) that meet this description that accountants treat as operating expenses.

# A. THE MAGNITUDE OF OPERATING LEASES

| <i>Highest</i>                      |                                 | <i>Lowest</i>            |                                 |
|-------------------------------------|---------------------------------|--------------------------|---------------------------------|
| <i>Industry Name</i>                | <i>Lease Expense/<br/>Sales</i> | <i>Industry Name</i>     | <i>Lease Expense/<br/>Sales</i> |
| Air Transport                       | 12.69%                          | Homebuilding             | 0.24%                           |
| Trucking                            | 7.33%                           | Green & Renewable Energy | 0.26%                           |
| Restaurant/Dining                   | 5.95%                           | Insurance (Life)         | 0.34%                           |
| Telecom (Wireless)                  | 5.75%                           | Steel                    | 0.39%                           |
| Apparel                             | 5.48%                           | Auto & Truck             | 0.41%                           |
| Real Estate (Operations & Services) | 5.41%                           | Food Wholesalers         | 0.45%                           |
| Retail (Special Lines)              | 4.86%                           | Insurance (Prop/Cas.)    | 0.46%                           |

# DEALING WITH OPERATING LEASE EXPENSES

- ▪ Since they give rise to contractual commitments, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital:
  - ▪ **Debt Value of Operating Leases** = Present value of Operating Lease Commitments at the pre-tax cost of debt
  - ▪ **Lease Asset:** When you convert operating leases into debt, you also create an asset to counter it of exactly the same value.
  - ▪ **Adjusted Operating Earnings** = Operating Earnings + Operating Lease Expenses - Depreciation on Leased Asset
  - ▪ As an approximation, this works:  
    Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

# OPERATING LEASES AT THE GAP IN 2003

- The Gap has conventional debt of about \$ 1.97 billion on its balance sheet and its pre-tax cost of debt is about 6%. Its operating lease payments in the 2003 were \$978 million and its commitments for the future are below:

| Year | Commitment (millions) | Present Value (at 6%) |
|------|-----------------------|-----------------------|
| 1    | \$899.00              | \$848.11              |
| 2    | \$846.00              | \$752.94              |
| 3    | \$738.00              | \$619.64              |
| 4    | \$598.00              | \$473.67              |
| 5    | \$477.00              | \$356.44              |
| 6&7  | \$982.50 each year    | \$1,346.04            |

- Debt Value of leases = \$4,396.85 (Also value of leased asset)
- Debt outstanding at The Gap = \$1,970 m + \$4,397 m = \$6,367 m
- Adjusted Operating Income = Stated OI + OL exp this year - Deprec'n
  - = \$1,012 m + 978 m - 4397 m / 7 = \$1,362 million (7-year life for assets)
- Approximate OI = \$1,012 m + \$ 4397 m (.06) = \$1,276 m

# THE COLLATERAL EFFECTS OF TREATING OPERATING LEASES AS DEBT

| <i>Conventional Accounting</i>                                                                                                                                                                                                                     | <i>Operating Leases Treated as Debt</i>                                                                                                                                                                                                     |       |           |          |         |      |      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-----------|----------|---------|------|------|
| <p><i>Income Statement</i></p> <p>EBIT&amp; Leases = 1,990</p> <p>- Op Leases = 978</p> <p>EBIT = 1,012</p>                                                                                                                                        | <p><i>Income Statement</i></p> <p>EBIT&amp; Leases = 1,990</p> <p>- Deprecn: OL= 628</p> <p>EBIT = 1,362</p> <p>Interest expense will rise to reflect the conversion of operating leases as debt. Net income should not change.</p>         |       |           |          |         |      |      |
| <p><i>Balance Sheet</i></p> <p>Off balance sheet (Not shown as debt or as an asset). Only the conventional debt of \$1,970 million shows up on balance sheet</p>                                                                                   | <p><i>Balance Sheet</i></p> <table border="0"> <tr> <td>Asset</td> <td>Liability</td> </tr> <tr> <td>OL Asset</td> <td>OL Debt</td> </tr> <tr> <td>4397</td> <td>4397</td> </tr> </table> <p>Total debt = 4397 + 1970 = \$6,367 million</p> | Asset | Liability | OL Asset | OL Debt | 4397 | 4397 |
| Asset                                                                                                                                                                                                                                              | Liability                                                                                                                                                                                                                                   |       |           |          |         |      |      |
| OL Asset                                                                                                                                                                                                                                           | OL Debt                                                                                                                                                                                                                                     |       |           |          |         |      |      |
| 4397                                                                                                                                                                                                                                               | 4397                                                                                                                                                                                                                                        |       |           |          |         |      |      |
| <p>Cost of capital = <math>8.20\%(7350/9320) + 4\%</math><br/> <math>(1970/9320) = 7.31\%</math></p> <p>Cost of equity for The Gap = <math>8.20\%</math></p> <p>After-tax cost of debt = <math>4\%</math></p> <p>Market value of equity = 7350</p> | <p>Cost of capital = <math>8.20\%(7350/13717) + 4\%</math><br/> <math>(6367/13717) = 6.25\%</math></p>                                                                                                                                      |       |           |          |         |      |      |
| <p>Return on capital = <math>1012 (1-.35)/(3130+1970)</math><br/> <math>= 12.90\%</math></p>                                                                                                                                                       | <p>Return on capital = <math>1362 (1-.35)/(3130+6367)</math><br/> <math>= 9.30\%</math></p>                                                                                                                                                 |       |           |          |         |      |      |

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

# ACCOUNTING COMES TO ITS SENSES ON OPERATING LEASES

- ▪ In 2019, both IFRS and GAAP made a major shift on operating leases, requiring companies to capitalize leases and show the resulting debt (and counter asset) on the balance sheets.
- ▪ That said, the accounting rules for capitalizing leases are far more complex than the simple calculations that I have used, for two reasons:
  - ▪ Accounting has to balance its desire to do the right thing with maintaining some connection to its legacy rules.
  - ▪ Companies have lobbied to modify rules in their sectors to cushion the impact.

# CHECKING ON ACCOUNTANTS.... MY LEASE ESTIMATE VS ACCOUNTANTS' ESTIMATE

| Region                 | My Estimate     | Accounting      | Accounting as % of my estimate |
|------------------------|-----------------|-----------------|--------------------------------|
| Australia, NZ & Canada | \$ 13,578.86    | \$ 8,412.39     | 61.95%                         |
| United States          | \$ 1,152,869.85 | \$ 947,989.30   | 82.23%                         |
| Europe                 | \$ 52,172.26    | \$ 24,336.94    | 46.65%                         |
| Emerging Markets       | \$ 109,415.47   | \$ 18,426.24    | 16.84%                         |
| Japan                  | \$ 156,071.83   | \$ 1,719.90     | 1.10%                          |
| Global                 | \$ 1,484,108.27 | \$ 1,000,884.77 | 67.44%                         |

## B. THE MAGNITUDE OF R&D EXPENSES

| Highest R&D spenders             |                            |                             | Lowest R&D spenders               |                            |                             |
|----------------------------------|----------------------------|-----------------------------|-----------------------------------|----------------------------|-----------------------------|
| Industry Name                    | R&D - LTM (In \$ millions) | Current R&D as % of Revenue | Industry Name                     | R&D - LTM (In \$ millions) | Current R&D as % of Revenue |
| Drugs (Biotechnology)            | \$ 75,091.63               | 39.62%                      | Beverage (Alcoholic)              | \$                         | 0.00%                       |
| Drugs (Pharmaceutical)           | \$ 80,658.49               | 23.08%                      | Food Wholesalers                  | \$ 0.88                    | 0.00%                       |
| Software (Internet)              | \$ 4,177.58                | 18.98%                      | Homebuilding                      | -                          | 0.00%                       |
| Semiconductor                    | \$ 50,321.60               | 17.40%                      | Hospitals/Healthcare Facilities   | \$ 9.72                    | 0.00%                       |
| Software (System & Applications) | \$ 72,267.59               | 16.70%                      | Insurance (Life)                  | -                          | 0.00%                       |
| Software (Entertainment)         | \$ 58,245.69               | 15.15%                      | Insurance (Prop/Cas.)             | -                          | 0.00%                       |
| Telecom. Equipment               | \$ 13,613.55               | 13.27%                      | Oil/Gas Distribution              | -                          | 0.00%                       |
| Retail (Online)                  | \$ 54,214.00               | 10.09%                      | Real Estate (Development)         | \$ -                       | 0.00%                       |
| Semiconductor Equip              | \$ 6,707.74                | 9.38%                       | Real Estate (General/Diversified) | -                          | 0.00%                       |
| Healthcare Products              | \$ 14,934.42               | 8.01%                       | Restaurant/Dining                 | \$ 8.82                    | 0.00%                       |

# **R&D EXPENSES: OPERATING OR CAPITAL EXPENSES**

- ▪ Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures.
- ▪ To capitalize R&D,
  - ▪ Specify an amortizable life for R&D (2 - 10 years)
  - ▪ Collect past R&D expenses for as long as the amortizable life
  - ▪ Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

# CAPITALIZING R&D EXPENSES: SAP

- R & D was assumed to have a 5-year life.

| Year    | R&D Expense | Unamortized | Amortization    |
|---------|-------------|-------------|-----------------|
| Current | € 1020.02   | 1.00        | 1020.02         |
| -1      | € 993.99    | 0.80        | 795.19          |
| -2      | € 909.39    | 0.60        | 545.63          |
| -3      | € 898.25    | 0.40        | 359.30          |
| -4      | € 969.38    | 0.20        | 193.88          |
| -5      | € 744.67    | 0.00        | 0.00            |
|         |             |             | € 2,914 million |
|         |             |             | € 903 million   |
|         |             |             | € 117 million   |
|         |             |             |                 |

# THE EFFECT OF CAPITALIZING R&D AT SAP

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

#### Balance Sheet

| Assets                                     |                   | Liabilities         |                             |
|--------------------------------------------|-------------------|---------------------|-----------------------------|
| Long Lived Physical Assets                 | Fixed Assets      | Current Liabilities | Short term obligations      |
| Short Lived Assets                         | Current Assets    | Debt                | Long term debt              |
| Investments in Securities & other business | Financial Assets  | Other Liabilities   | Other long term obligations |
| Assets which are not physical              | Intangible Assets | Equity              | Shareholders' Equity        |

*When accountants treat a capital expenditure (like R&D) as an operating expense.*

**Operating income and net income will be misstated and will be too low (high) for companies with growing (declining) R&D expenses.**

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

# 3. ONE-TIME AND NON-RECURRING CHARGES

- ▪ Assume that you are valuing a firm that is reporting a loss of \$ 500 million, due to a one-time charge of \$ 1 billion. What is the earnings you would use in your valuation?
  - a. A loss of \$ 500 million
  - b. A profit of \$ 500 million
- ▪ Would your answer be any different if the firm had reported one-time losses like these once every five years?
  - a. Yes
  - b. No

## 4. ACCOUNTING MALFEASANCE....

- ■ Though all firms may be governed by the same accounting standards, the fidelity that they show to these standards can vary. More aggressive firms will show higher earnings than more conservative firms.
- ■ While you will not be able to catch outright fraud, you should look for warning signals in financial statements and correct for them:
  - ■ Income from unspecified sources - holdings in other businesses that are not revealed or from special purpose entities.
  - ■ Income from asset sales or financial transactions (for a non-financial firm)
  - ■ Sudden changes in standard expense items - a big drop in S,G &A or R&D expenses as a percent of revenues, for instance.
  - ■ Frequent accounting restatements
  - ■ Accrual earnings that run ahead of cash earnings consistently
  - ■ Big differences between tax income and reported income

# 5. DEALING WITH NEGATIVE OR ABNORMALLY LOW EARNINGS

|                 | Reason for losses/low earnings                   | Valuation Response                                                                                                   |
|-----------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Quick fixes     | One-time or extraordinary charge                 | Add back the one-time expense to get corrected earnings                                                              |
|                 | Macro factor (commodity price drop or recession) | Use earnings across the commodity or economic cycle as normalized earnings.                                          |
| Long term fixes | Young company working on business model          | Estimate the profit margin that mature companies in the business earn and target that margin in the long term.       |
|                 | Structural problems at company                   | Use an industry average margin as a target and move towards that margin over time, as structural problems are fixed. |

![](_page_137_Picture_12.jpeg)

# CASH FLOWS II

## Taxes and Reinvestment

# 1. WHAT TAX RATE?

- ▪ The tax rate that you should use in computing the after-tax operating income should be
  - a. The effective tax rate in the financial statements (taxes paid/Taxable income)
  - b. The tax rate based upon taxes paid and EBIT (taxes paid/EBIT)
  - c. The marginal tax rate for the country in which the company operates
  - d. The weighted average marginal tax rate across the countries in which the company operates
  - e. None of the above
  - f. Any of the above, as long as you compute your after-tax cost of debt using the same tax rate.

# THE RIGHT TAX RATE TO USE

- ▪ The free cash flow to the firm starts with after-tax operating income, where:
  - ▪ After-tax Operating Income = Operating Income (1- tax rate)
- ▪ In computing free cash flow to the firm, the choice really is between the effective and the marginal tax rate.
  - ▪ By using **the marginal tax rate**, we tend to understate the after-tax operating income in the earlier years, but the after-tax tax operating income is more accurate in later years.
  - ▪ By using **the effective tax rate**, we tend to overstate the after-tax operating income in the later years, as effective tax rates move toward the marginal tax rate.
- ▪ You can have your cake and eat it too, by starting with the effective tax rate, and adjusting towards the marginal tax rate over time.

# A TAX RATE FOR A MONEY LOSING FIRM

- ▪ Assume that you are trying to estimate the after-tax operating income for a firm with \$ 1 billion in net operating losses carried forward.
- ▪ This firm is expected to have operating income of \$ 500 million each year for the next 3 years, and the marginal tax rate on income for all firms that make money is 40%. Estimate the after-tax operating income each year for the next 3 years.

|      | Year 1 | Year 2 | Year 3 |
|------|--------|--------|--------|
| EBIT | 500    | 500    | 500    |

Taxes

EBIT (1-t)

Tax rate

## 2. NET CAPITAL EXPENDITURES

- ▪ Net capital expenditures represent the difference between capital expenditures and depreciation.

$$\text{Net Cap Ex} = \text{Capital Expenditures} - \text{Depreciation}$$

- ▪ Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures.
- ▪ In general, the **net capital expenditures will be a function of how fast a firm is growing or expecting to grow**.
  - ▪ High growth firms will usually have much higher net capital expenditures than low growth firms.
  - ▪ Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

# CAPITAL EXPENDITURES SHOULD INCLUDE

- ▪ **Research and development expenses**, once they have been re-categorized as capital expenses. The adjusted net cap ex will be
  - ▪ Adjusted Net Capital Expenditures = Net Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset
- ▪ **Acquisitions of other firms**, since these are like capital expenditures. The adjusted net cap ex will be
  - ▪ Adjusted Net Cap Ex = Net Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions
- ▪ Two caveats:
  1. 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
  2. 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

# CISCO'S ACQUISITIONS: 1999

| <i>Acquired</i>    | <i>Method of Acquisition</i> | <i>Price Paid</i> |
|--------------------|------------------------------|-------------------|
| GeoTel             | Pooling                      | \$1,344           |
| Fibex              | Pooling                      | \$318             |
| Sentient           | Pooling                      | \$103             |
| American Internet  | Purchase                     | \$58              |
| Summa Four         | Purchase                     | \$129             |
| Clarity Wireless   | Purchase                     | \$153             |
| Selsius Systems    | Purchase                     | \$134             |
| PipeLinks          | Purchase                     | \$118             |
| Amteva Tech        | Purchase                     | \$159             |
| Total acquisitions |                              | \$2,516           |

# CISCO'S NET CAPITAL EXPENDITURES IN 1999

| Cap Expenditures (from statement of CF) | = \$ 584 mil   |
|-----------------------------------------|----------------|
| - Depreciation (from statement of CF)   | = \$ 486 mil   |
| Net Cap Ex (from statement of CF)       | = \$ 98 mil    |
| + R & D expense                         | = \$ 1,594 mil |
| - Amortization of R&D                   | = \$ 485 mil   |
| + Acquisitions                          | = \$ 2,516 mil |
| Adjusted Net Capital Expenditures       | = \$3,723 mil  |

# 3. WORKING CAPITAL INVESTMENTS

- ■ **Accounting definition:** Working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year).
- ■ **Valuation definition:** A cleaner definition of working capital from a cash flow perspective is the difference **between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable, supplier credit etc.)**.

# WORKING CAPITAL: GENERAL PROPOSITIONS

- ▪ **Working Capital Detail:** While some analysts break down working capital into detail, it is a pointless exercise unless you feel that you can bring some specific information that lets you forecast the details.
- ▪ **Working Capital Volatility:** Changes in non-cash working capital from year to year tend to be volatile. It is better to either estimate the change based on working capital as a percent of sales, while keeping an eye on industry averages.
- ▪ **Negative Working Capital:** Some firms have negative non-cash working capital. Assuming that this will continue into the future will generate positive cash flows for the firm and will get more positive as growth increases.

![](_page_147_Picture_12.jpeg)

# CASH FLOWS III

From the firm to equity

![]()

# DIVIDENDS AND CASH FLOWS TO EQUITY

- ▪ In the strictest sense, the only cash flow from an equity investment in a publicly traded firm is **the dividend that will be paid on the stock.**
- ▪ Actual dividends, however, are set by the managers of the firm and may be much lower than the potential dividends (that could have been paid out)
  - ▪ managers are **conservative and try to smooth out dividends**
  - ▪ managers like to **hold on to cash** to meet unforeseen future contingencies and investment opportunities
- ▪ When actual dividends are less (more) than potential dividends, using a model that focuses only on dividends will under (over) state the true value of the equity in a firm.

# MEASURING POTENTIAL DIVIDENDS

- ▪ Some analysts assume that the earnings of a firm represent its potential dividends. This cannot be true for several reasons:
  - ▪ **Earnings are not cash flows**, since there are both non-cash revenues and expenses in the earnings calculation
  - ▪ Even if earnings were cash flows, a firm that **paid its earnings out as dividends would not be investing in new assets** and thus could not grow
  - ▪ Valuation models, where earnings are discounted back to the present, will overestimate the value of the equity in the firm
- ▪ The **potential dividends** of a firm are the cash flows left over after the firm has made any “investments” it needs to make to create future growth and net debt repayments (debt repayments - new debt issues)
  - ▪ The common categorization of capital expenditures into discretionary and non-discretionary loses its basis when there is future growth built into the valuation.

# ESTIMATING CASH FLOWS: FCFE

- ▪ Cash flows to Equity for a Levered Firm
  - Net Income
    - - (Capital Expenditures - Depreciation)
    - - Changes in non-cash Working Capital
    - + (New Debt Issues – Debt Repaid)
    - = Free Cash flow to Equity
- ▪ Cash flows to equity represent **residual cash flows for equity investors**, i.e., cash flows left over after every conceivable need has been met.
- ▪ That **cash flow can be paid out without damaging the operating business of the company and its growth potential**. It is thus a potential dividend.

# FCFE FROM THE STATEMENT OF CASH FLOWS

- ▪ The statement of cash flows can be used to back into a FCFE, if you are willing to navigate your way through it and not trust it fully.
- ▪ FCFE
  - = Cashflow from Operations
  - + Capital Expenditures (from the cash flow from investments)
  - + Cash Acquisitions (from the cash flow from investments)
  - +(Debt Repaid – Debt Issued) (from financing cash flows)
  - = FCFE

# FCFE ACROSS THE LIFE CYCLE

![](_page_152_Figure_10.jpeg)

# FCFE OVER TIME: TESLA

*Tesla: Net Income and FCFE - 2006 to 2021*

![](_page_153_Figure_12.jpeg)

# DIVIDENDS VERSUS FCFE: ACROSS THE GLOBE

| Sub-region                | # firms | Net Income  | Dividends   | Payout Ratio | Buybacks    | % from buybacks | Dividends + Buybacks | FCFE       |
|---------------------------|---------|-------------|-------------|--------------|-------------|-----------------|----------------------|------------|
| Africa and Middle East    | 1,958   | \$214,627   | \$164,862   | 76.81%       | \$11,524    | 6.53%           | \$176,386            | \$114,892  |
| Australia & NZ            | 1,559   | \$41,439    | \$34,413    | 83.05%       | \$5,636     | 14.07%          | \$40,049             | \$887      |
| Canada                    | 2,392   | \$92,170    | \$48,896    | 53.05%       | \$35,039    | 41.75%          | \$83,935             | \$7,836    |
| China                     | 7,451   | \$459,532   | \$407,212   | 88.61%       | \$81,931    | 16.75%          | \$489,143            | -\$268,924 |
| EU & Environs             | 4,951   | \$615,630   | \$356,832   | 57.96%       | \$157,469   | 30.62%          | \$514,301            | \$158,410  |
| Eastern Europe & Russia   | 372     | \$9,302     | \$4,595     | 49.39%       | \$140       | 2.96%           | \$4,735              | \$3,595    |
| India                     | 4,520   | \$137,252   | \$46,229    | 33.68%       | \$4,571     | 9.00%           | \$50,801             | \$82,500   |
| Japan                     | 3,760   | \$367,319   | \$132,590   | 36.10%       | \$100,816   | 43.19%          | \$233,407            | \$124,177  |
| Latin America & Caribbean | 807     | \$80,090    | \$52,431    | 65.46%       | \$9,916     | 15.90%          | \$62,347             | \$5,571    |
| Small Asia                | 9,503   | \$348,239   | \$950,113   | 272.83%      | \$27,689    | 2.83%           | \$977,801            | -\$8,122   |
| UK                        | 835     | \$119,271   | \$91,313    | 76.56%       | \$62,480    | 40.63%          | \$153,793            | \$7,722    |
| United States             | 4,770   | \$1,652,526 | \$623,801   | 37.75%       | \$904,006   | 59.17%          | \$1,527,807          | \$533,286  |
| Global                    | 42,878  | \$4,137,396 | \$2,913,287 | 70.41%       | \$1,401,217 | 32.48%          | \$4,314,504          | \$761,831  |

# ESTIMATING FCFE WHEN LEVERAGE IS STABLE

## Net Income

- - (1- DR) (Capital Expenditures - Depreciation)

- - (1- DR) Working Capital Needs

= Free Cash flow to Equity

- ▪ DR = Debt/Capital Ratio

- ▪ For this firm,

- - ▪ Proceeds from new debt issues = Principal Repayments + □ (Capital Expenditures - Depreciation + Working Capital Needs)

- ▪ In computing FCFE, the book value debt to capital ratio should be used when looking back in time but can be replaced with the market value debt to capital ratio, looking forward.

# ESTIMATING FCFE: DISNEY

- ▪ Net Income=\$ 1533 Million
- ▪ Capital spending = \$ 1,746 Million
- ▪ Depreciation per Share = \$ 1,134 Million
- ▪ Increase in non-cash working capital = \$ 477 Million
- ▪ Debt to Capital Ratio (DR) = 23.83%
- ▪ Estimating FCFE (1997):
  - Net Income \$1,533 Mil
  - - (Cap Exp - Depr)\*(1-DR) \$465.90 [(1746-1134)(1-.2383)]
  - Chg. Working Capital\*(1-DR) \$363.33 [477(1-.2383)]
  - = Free CF to Equity \$ 704 Million
- ▪ Dividends Paid \$ 345 Million

# FCFE AND LEVERAGE: IS THIS A FREE LUNCH?

Debt Ratio and FCFE: Disney

![](_page_157_Figure_69.jpeg)

# FCFE AND LEVERAGE: THE OTHER SHOE DROPS

Debt Ratio and Beta

![](_page_158_Figure_69.jpeg)

# LEVERAGE, FCFE AND VALUE

- ▪ In a discounted cash flow model, increasing the debt/equity ratio will generally increase the expected free cash flows to equity investors over future time periods and also the cost of equity applied in discounting these cash flows. Which of the following statements relating leverage to value would you subscribe to?
  - a. Increasing leverage will increase value because the cash flow effects will dominate the discount rate effects
  - b. Increasing leverage will decrease value because the risk effect will be greater than the cash flow effects
  - c. Increasing leverage will not affect value because the risk effect will exactly offset the cash flow effect
  - d. Any of the above, depending upon what company you are looking at and where it is in terms of current leverage

![](_page_160_Picture_4.jpeg)

# ESTIMATING GROWTH

Growth can be good, bad or neutral...

# THE VALUE OF GROWTH

- ■ When valuing a company, it is easy to get caught up in the details of estimating growth and start viewing growth as a “good”, i.e., that higher growth translates into higher value.
- ■ Growth, though, is a double-edged sword.
  - ■ The good side of growth is that it pushes up revenues and operating income, perhaps at different rates (depending on how margins evolve over time).
  - ■ The bad side of growth is that you have to set aside money to reinvest to create that growth.
  - ■ The net effect of growth is whether the good outweighs the bad.

# WAYS OF ESTIMATING GROWTH IN EARNINGS

- ▪ Look at the past
  - ▪ The historical growth in earnings per share is usually a good starting point for growth estimation
- ▪ Look at what others are estimating
  - ▪ Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are.
- ▪ Look at fundamentals
  - ▪ With stable margins, operating income growth can be tied to how much a firm reinvests, and the returns it earns.
  - ▪ With changing margins, you have to start with revenue growth, forecast margins and estimate reinvestment.

![](_page_163_Picture_12.jpeg)

# GROWTH I

## Historical Growth

# HISTORICAL GROWTH

- ▪ Historical growth rates can be estimated in a number of different ways
  - ▪ Arithmetic versus Geometric Averages
  - ▪ Simple versus Regression Models
- ▪ Historical growth rates can be sensitive to
  - ▪ The **period used in the estimation** (starting and ending points)
  - ▪ The **metric** that the growth is estimated in..
- ▪ In using historical growth rates, you have to wrestle with the following:
  - ▪ How to deal with **negative earnings**
  - ▪ The effects of **scaling up**

# MOTOROLA: ARITHMETIC VERSUS GEOMETRIC GROWTH RATES

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

- § You are trying to estimate the growth rate in earnings per share at Time Warner from 1996 to 1997. In 1996, the earnings per share was a deficit of \$0.05. In 1997, the expected earnings per share is \$ 0.25. What is the growth rate?
  - a. -600%
  - b. +600%
  - c. +120%
  - d. Cannot be estimated

# DEALING WITH NEGATIVE EARNINGS

- ■ When the earnings in the starting period are negative, the growth rate cannot be estimated. ( $0.30/-0.05 = -600\%$ )
- ■ There are three solutions:
  - ■ Use the higher of the two numbers as the denominator ( $0.30/0.25 = 120\%$ )
  - ■ Use the absolute value of earnings in the starting period as the denominator ( $0.30/0.05=600\%$ )
  - ■ Use a linear regression model and divide the coefficient by the average earnings.
- ■ When earnings are negative, the growth rate is meaningless. Thus, while the growth rate can be estimated, it does not tell you much about the future.

# THE EFFECT OF SIZE ON GROWTH: CALLAWAY GOLF

| Year | Net Profit | Growth Rate |
|------|------------|-------------|
| 1990 | 1.80       |             |
| 1991 | 6.40       | 255.56%     |
| 1992 | 19.30      | 201.56%     |
| 1993 | 41.20      | 113.47%     |
| 1994 | 78.00      | 89.32%      |
| 1995 | 97.70      | 25.26%      |
| 1996 | 122.30     | 25.18%      |

- ■ Geometric Average Growth Rate = 102%

# EXTRAPOLATION AND ITS DANGERS

| Year | Net Profit  |
|------|-------------|
| 1996 | \$ 122.30   |
| 1997 | \$ 247.05   |
| 1998 | \$ 499.03   |
| 1999 | \$ 1,008.05 |
| 2000 | \$ 2,036.25 |
| 2001 | \$ 4,113.23 |

- ■ If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

![](_page_170_Picture_12.jpeg)

# GROWTH II

## Analyst Estimates

# ANALYST FORECASTS OF GROWTH

- ▪ While the job of an analyst is to find under and overpriced stocks in the sectors that they follow, a significant proportion of an analyst's time (outside of selling) is spent forecasting earnings per share.
  - ▪ Most of this time, in turn, is **spent forecasting earnings per share** in the next earnings report
  - ▪ While **many analysts forecast expected growth in earnings per share over the next 5 years**, the analysis and information (generally) that goes into this estimate is far more limited.
- ▪ Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

# HOW GOOD ARE ANALYSTS AT FORECASTING GROWTH?

- ▪ Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| <i>Study</i>      | <i>Group tested</i>  | <i>Analyst</i> | <i>Time Series</i> |
|-------------------|----------------------|----------------|--------------------|
|                   |                      | <i>Error</i>   | <i>Model Error</i> |
| Collins & Hopwood | Value Line Forecasts | 31.7%          | 34.1%              |
| Brown & Rozeff    | Value Line Forecasts | 28.4%          | 32.2%              |
| Fried & Givoly    | Earnings Forecaster  | 16.4%          | 19.8%              |

- ▪ The advantage that analysts have over time series models
  - ▪ tends to **decrease with the forecast period** (next quarter versus 5 years)
  - ▪ tends to be **greater for larger firms** than for smaller firms
  - ▪ tends to be **greater at the industry level** than at the company level
- ▪ Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

# ARE SOME ANALYSTS MORE EQUAL THAN OTHERS?

- ▪ A study of All-America Analysts (chosen by Institutional Investor) found that
  - ▪ There is **no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings**. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%)
- ▪ However, in the **calendar year following** being chosen as All-America analysts, **these analysts become slightly better forecasters** than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts)
- ▪ Earnings revisions made by All-America analysts tend to **have a much greater impact on the stock price** than revisions from other analysts
- ▪ The recommendations made by the All-America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (**2.4% for buys; 13.8% for the sells**).

# THE FIVE DEADLY SINS OF AN ANALYST

- ▪ **Tunnel Vision:** Becoming so focused on the sector and valuations within the sector that you lose sight of the bigger picture.
- ▪ **Lemmingitis:** Strong urge felt to change recommendations & revise earnings estimates when other analysts do the same.
- ▪ **Stockholm Syndrome:** Refers to analysts who start identifying with the managers of the firms that they are supposed to follow.
- ▪ **Factophobia** (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a “story” coupled with a refusal to face the facts.
- ▪ **Dr. Jekyll/Mr.Hyde:** Analyst who thinks his primary job is to bring in investment banking business to the firm.

# PROPOSITIONS ABOUT ANALYST GROWTH RATES

- ▪ **Proposition 1:** There is far less private information and far more public information in most analyst forecasts than is generally claimed.
- ▪ **Proposition 2:** The biggest source of private information for analysts remains the company itself which might explain
  - ▪ why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources)
  - ▪ why there is such a high correlation across analysts forecasts and revisions
  - ▪ why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team.
- ▪ **Proposition 3:** There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

![](_page_176_Picture_12.jpeg)

# GROWTH III

Sustainable growth and Fundamentals

# FUNDAMENTAL GROWTH RATES

Investment in Existing Projects  
\$ 1000

X

Current Return on Investment on Projects  
12%

=

Current Earnings  
\$120

Investment in Existing Projects  
\$1000

X

Next Period's Return on Investment  
12%

+

Investment in New Projects  
\$100

X

Return on Investment on New Projects  
12%

=

Next Period's Earnings  
132

Investment in Existing Projects  
\$1000

X

Change in ROI from current to next period: 0%

+

Investment in New Projects  
\$100

X

Return on Investment on New Projects  
12%

= Change in Earnings  
\$ 12

# GROWTH RATE DERIVATIONS

In the special case where ROI on existing projects remains unchanged and is equal to the ROI on new projects

Investment in New Projects  
Current Earnings

$$\frac{100}{120}$$

$$\times \text{Return on Investment} = \text{Change in Earnings}$$

$$\times 12\% = \frac{\$12}{\$120}$$

Reinvestment Rate

$$83.33\%$$

$$\times \text{Return on Investment} = \text{Growth Rate in Earnings}$$

$$\times 12\% = 10\%$$

in the more general case where ROI can change from period to period, this can be expanded as follows:

$$\frac{\text{Investment in Existing Projects} \times (\text{Change in ROI}) + \text{New Projects (ROI)}}{\text{Investment in Existing Projects} \times \text{Current ROI}} = \frac{\text{Change in Earnings}}{\text{Current Earnings}}$$

For instance, if the ROI increases from 12% to 13%, the expected growth rate can be written as follows:

$$\frac{\$1,000 \times (.13 - .12) + 100 (13\%)}{\$1,000 \times .12} = \frac{\$23}{\$120} = 19.17\%$$

# ESTIMATING FUNDAMENTAL GROWTH FROM NEW INVESTMENTS: THREE VARIATIONS

| Earnings Measure                | Reinvestment Measure                                                                                                          | Return Measure                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Earnings per share              | Retention Ratio = % of net income retained by the company = $1 - \text{Payout ratio}$                                         | Return on Equity = Net Income/ Book Value of Equity                                                        |
| Net Income from non-cash assets | Equity reinvestment Rate = $(\text{Net Cap Ex} + \text{Change in non-cash WC} - \text{Change in Debt}) / (\text{Net Income})$ | Non-cash ROE = Net Income from non-cash assets/ (Book value of equity – Cash)                              |
| Operating Income                | Reinvestment Rate = $(\text{Net Cap Ex} + \text{Change in non-cash WC}) / \text{After-tax Operating Income}$                  | Return on Capital or ROIC = After-tax Operating Income/ (Book value of equity + Book value of debt – Cash) |

# I. EXPECTED LONG TERM GROWTH IN EPS

- ▪ When looking at growth in earnings per share, these inputs can be cast as follows:
  - ▪ Reinvestment Rate = Retained Earnings/ Current Earnings = Retention Ratio
  - ▪ Return on Investment = ROE = Net Income/Book Value of Equity
- ▪ In the special case where the current ROE is expected to remain unchanged

$$\begin{aligned} g_{EPS} &= \text{Retained Earnings}_{t-1} / NI_{t-1} * \text{ROE} \\ &= \text{Retention Ratio} * \text{ROE} \\ &= b * \text{ROE} \end{aligned}$$

- ▪ In 2008, using this approach on Wells Fargo:
  - ▪ Return on equity (based on 2008 earnings)= 17.56%
  - ▪ Retention Ratio (based on 2008 earnings and dividends) = 45.37%
  - ▪ Expected Growth Rate =  $0.4537 (17.56\%) = 7.97\%$

# ONE WAY TO PUMP UP ROE: USE MORE DEBT

ROE = Return on capital + D/E (ROC - i (1-tax rate))

where,

Return on capital = EBIT<sub>t</sub> (1 - tax rate) / Book value of Capital<sub>t-1</sub>

D/E = BV of Debt / BV of Equity

i = Interest Expense on Debt / BV of Debt

- ■ In 1998, Brahma (now Ambev) had an extremely high return on equity, partly because it borrowed money at a rate well below its return on capital
  - ■ Return on Capital = 19.91%
  - ■ Debt/Equity Ratio = 77%
  - ■ After-tax Cost of Debt = 5.61%
  - ■ Return on Equity = ROC + D/E (ROC - i(1-t))
    - ■ 
      $$= 19.91\% + 0.77 (19.91\% - 5.61\%) = 30.92\%$$

# II. EXPECTED GROWTH IN NET INCOME FROM NON-CASH ASSETS

- ▪ A more general version of expected growth in earnings can be obtained by **substituting in the equity reinvestment** into real investments (net capital expenditures and working capital) and **modifying the return on equity definition to exclude cash**:
  - ▪ Net Income from non-cash assets = Net income – Interest income from cash ( $1 - t$ )
  - ▪ Equity Reinvestment Rate =  $(\text{Net Capital Expenditures} + \text{Change in Working Capital}) / (1 - \text{Debt Ratio})$  / Net Income from non-cash assets
  - ▪ Non-cash ROE = Net Income from non-cash assets / (BV of Equity – Cash)
  - ▪ Expected Growth  $\text{Net Income} = \text{Equity Reinvestment Rate} * \text{Non-cash ROE}$
- ▪ The equity reinvestment rate, unlike the retention ratio, can be higher than 100%, and if it is, the expected growth rate in net income can exceed the return on equity.

# ESTIMATING EXPECTED GROWTH IN NET INCOME FROM NON-CASH ASSETS: COCA COLA IN 2010

- ■ In 2010, Coca Cola reported net income of \$11,809 million. It had a total book value of equity of \$25,346 million at the end of 2009. Coca Cola had a cash balance of \$7,021 million at the end of 2009, on which it earned income of \$105 million in 2010.
  - ■ Non-cash Net Income =  $\$11,809 - \$105 = \$11,704$  million
  - ■ Non-cash book equity =  $\$25,346 - \$7021 = \$18,325$  million
  - ■ Non-cash ROE =  $\$11,704$  million/  $\$18,325$  million = 63.87%
- ■ Coca Cola had capital expenditures of \$2,215 million, depreciation of \$1,443 million and reported an increase in working capital of \$335 million. Coca Cola's total debt increased by \$150 million during 2010.
  - ■ Equity Reinvestment =  $2215 - 1443 + 335 - 150 = \$957$  million
  - ■ Reinvestment Rate =  $\$957$  million/  $\$11,704$  million = 8.18%
- ■ Expected growth rate in non-cash Net Income =  $8.18\% * 63.87\%$  = 5.22%

# III. EXPECTED GROWTH IN EBIT AND FUNDAMENTALS: STABLE ROC AND REINVESTMENT RATE

- ▪ When looking at growth in operating income, the definitions are
  - ▪ Reinvestment Rate =  $(\text{Net Capital Expenditures} + \text{Change in WC})/\text{EBIT}(1-t)$
  - ▪ Return on Investment =  $\text{ROC} = \text{EBIT}(1-t)/(\text{BV of Debt} + \text{BV of Equity-Cash})$
- ▪ Reinvestment Rate and Return on Capital
  - Expected Growth rate in Operating Income  
     $= (\text{Net Capital Expenditures} + \text{Change in WC})/\text{EBIT}(1-t) * \text{ROC}$   
     $= \text{Reinvestment Rate} * \text{ROC}$
- ▪ **Proposition:** The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.

# ESTIMATING GROWTH IN OPERATING INCOME, IF FUNDAMENTALS STAY LOCKED IN...

- ▪ In 1999, Cisco's fundamentals were as follows:
  - ▪ Reinvestment Rate = 106.81%
  - ▪ Return on Capital = 34.07%
  - ▪ Expected Growth in EBIT =  $(1.0681)(.3407) = 36.39\%$
- ▪ As a potential investor in Cisco, what would worry you the most about this forecast?
  - a. That Cisco's return on capital may be overstated (why?)
  - b. That Cisco's reinvestment comes mostly from acquisitions (why?)
  - c. That Cisco is getting bigger as a firm (why?)
  - d. That Cisco is viewed as a star (why?)
  - e. All of the above

# THE MAGICAL NUMBER: ROIC (OR ANY ACCOUNTING RETURN) AND ITS LIMITS

## **Abnormal earnings**

Last 12 months might have been unusually good or bad

## **Accounting Issues**

Operating income can be skewed by accounting misclassification (leases and R&D) and by unusual expenses/income.

Computed as operating income in most recent 12 months, net of the effective tax rate paid during those 12 months

## **Life Cycle Effect**

Current earnings are not indicative of long term earnings potential for young & infrastructure firms

**Return on Invested Capital =**

After-tax Operating Income

Capital Invested in existing assets

## **Accounting Write offs**

Writing off mistakes can reduce invested capital & make it look better than it should.

Invested Capital = Book value of equity + Book value of debt - Cash & Cross holdings

## **Accounting misclassification**

When capital expenses (R&D) and financial expenses (leases) are miscategorized as operating expenses, invested capital will be understated.

*This is your proxy for returns made on existing assets and for continuing returns from those assets*

## **Inflation**

If asset book value is not adjusted for inflation, capital invested in older assets will be understated.

## IV. OPERATING INCOME GROWTH WHEN RETURN ON CAPITAL IS CHANGING

- ■ When the return on capital is changing, there will be a second component to growth, positive if the return on capital is increasing and negative if the return on capital is decreasing.
- ■ If  $ROC_t$  is the return on capital in period  $t$  and  $ROC_{t+1}$  is the return on capital in period  $t+1$ , the expected growth rate in operating income will be:

$$\text{Expected Growth Rate} = ROC_{t+1} * \text{Reinvestment rate} \\ + (ROC_{t+1} - ROC_t) / ROC_t$$

- ■ In general, if return on capital and margins are changing and/or expected to change at a company, you are better off not using any of the sustainable growth equations to estimate growth.

# THE VALUE OF GROWTH

|                                     | Firm 1        | Firm 2        | Firm 3        | Firm 4        | Firm 5        |
|-------------------------------------|---------------|---------------|---------------|---------------|---------------|
| Reinvestment Rate                   | 20.00%        | 100.00%       | 200.00%       | 20.00%        | 0.00%         |
| ROIC on new investment              | 50.00%        | 10.00%        | 5.00%         | 10.00%        | 10.00%        |
|                                     |               |               |               |               |               |
| ROIC on existing investments before | 10.00%        | 10.00%        | 10.00%        | 10.00%        | 10.00%        |
| ROIC on existing investments after  | 10.00%        | 10.00%        | 10.00%        | 10.80%        | 11.00%        |
|                                     |               |               |               |               |               |
| <b>Expected growth rate</b>         | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> |

$$\begin{aligned}
 \text{Expected growth} &= \text{Growth from new investments} + \text{Efficiency growth} \\
 &= \text{Reinv Rate} * \text{ROC} + (\text{ROC}_t - \text{ROC}_{t-1}) / \text{ROC}_{t-1}
 \end{aligned}$$

**Assume that your cost of capital is 10%. As an investor, rank these firms in the order of most value growth to least value growth.**

![](_page_189_Picture_12.jpeg)

# GROWTH IV

Top Down Growth

# ESTIMATING GROWTH WHEN OPERATING INCOME IS NEGATIVE OR MARGINS ARE CHANGING

- ▪ All of the fundamental growth equations assume that the firm has a return on equity or return on capital it can sustain in the long term.
- ▪ When operating income is negative or margins are expected to change over time, we use a three-step process to estimate growth:
  - ▪ Estimate growth rates in revenues over time
    - ▪ Determine the **total market** (given your business model) and estimate the market share that you think your company will earn.
    - ▪ **Decrease the growth rate** as the firm becomes larger
    - ▪ Keep **track of absolute revenues** to make sure that the growth is feasible
  - ▪ Estimate expected operating margins each year
    - ▪ Set a **target margin** that the firm will move towards
    - ▪ **Adjust** the current margin **towards** the target margin
  - ▪ Estimate the capital that needs to be invested to generate revenue growth and expected margins
    - ▪ Estimate a sales to capital ratio that you will use to generate reinvestment needs each year.

# 1. REVENUE GROWTH

## Revenue Growth and Magnitude

| Market Size and Growth                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. <i>Current Market size:</i> The size of the market for the company's products & services, given geography it is targeting and product type.<br>2. <i>Expected Growth in Market:</i> Growth in total market, as technology and market conditions change. |

X

| Market Share                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. <i>Company's current market share:</i> If company's current market share is low, potential for growth in market share at expense of competition.<br>2. <i>Industry economics:</i> Nature of the business (a few big winners or splintered competition).<br>3. <i>Strength of company's competitive advantages:</i> Stronger and more sustainable competitive advantages should allow for higher market share. |

The potential for revenue growth is greater for companies with small revenues (and market share) in a big and growing market, especially if the company has strong competitive advantages in winner-take-all businesses.

# AIRBNB: TOTAL MARKET

![](_page_192_Figure_40.jpeg)

![](_page_192_Figure_41.jpeg)

![](_page_192_Figure_42.jpeg)

In its prospectus, Airbnb has expanded its estimate of market potential to \$3.4 trillion, as evidenced in this excerpt from the prospectus:

*We have a substantial market opportunity in the growing travel market and experience economy. We estimate our serviceable addressable market (“SAM”) today to be \$1.5 trillion, including \$1.2 trillion for short-term stays and \$239 billion for experiences. We estimate our total addressable market (“TAM”) to be \$3.4 trillion, including \$1.8 trillion for short-term stays, \$210 billion for long-term stays, and \$1.4 trillion for experiences.*

# AIRBNB: MARKET SHARE

![](_page_193_Diagram_10.jpeg)

# 2. TARGET MARGINS (AND PATH THERE)...

## Operating Margin: Target and Pathway

![](_page_194_Diagram_13.jpeg)

While all companies would like higher margins in steady state, the level of these margins will be determined by the sector in which a firm operates and its choice of business model, and the speed with which you move towards those target margins will be determined by a company's ambitions and business model choices.

# AIRBNB IN NOVEMBER 2020: GROWTH AND PROFITABILITY

|               | Gross Bookings    | Revenues      | Revenue Growth | Operating Margin |
|---------------|-------------------|---------------|----------------|------------------|
| LTM           | \$ 26,491,803.00  | \$ 3,625,731  |                |                  |
| 1             | \$ 37,088,524.20  | \$ 4,691,698  | 40.00%         | -10.00%          |
| 2             | \$ 46,360,655.25  | \$ 5,989,797  | 25.00%         | -3.00%           |
| 3             | \$ 57,950,819.06  | \$ 7,565,479  | 25.00%         | 0.50%            |
| 4             | \$ 72,438,523.83  | \$ 9,554,641  | 25.00%         | 4.00%            |
| 5             | \$ 90,548,154.79  | \$ 12,065,542 | 25.00%         | 7.50%            |
| 6             | \$ 109,019,978.36 | \$ 14,674,089 | 20.40%         | 9.52%            |
| 7             | \$ 126,245,134.94 | \$ 17,163,026 | 15.80%         | 13.39%           |
| 8             | \$ 140,384,590.06 | \$ 19,274,804 | 11.20%         | 17.26%           |
| 9             | \$ 149,649,973.00 | \$ 20,748,969 | 6.60%          | 21.13%           |
| 10            | \$ 152,642,972.46 | \$ 21,370,016 | 2.00%          | 25.00%           |
| Terminal year | \$ 155,695,831.91 | \$ 21,797,416 | 2.00%          | 25.00%           |

|                         | Expedia       |              |                       | Booking.com  |              |                       |
|-------------------------|---------------|--------------|-----------------------|--------------|--------------|-----------------------|
|                         | 2019          | LTM          | % Change (Annualized) | 2019         | LTM          | % Change (Annualized) |
| Gross Bookings          | \$ 107,870.00 | \$ 52,470.00 | -61.75%               | \$ 96,400.00 | \$ 48,752.00 | -59.71%               |
| Revenues                | \$ 12,067.00  | \$ 7,026.00  | -51.38%               | \$ 15,066.00 | \$ 8,897.00  | -50.46%               |
| Operating Income        | \$ 961.00     | \$ (892.00)  | NA                    | \$ 5,345.00  | \$ 1,831.00  | -76.03%               |
| Revenues/Gross Bookings | 11.19%        | 13.39%       |                       | 15.63%       | 18.25%       |                       |
| Operating Margin        | 7.96%         | -12.70%      |                       | 35.48%       | 20.58%       |                       |

# 3. SALES TO INVESTED CAPITAL: A PATHWAY TO ESTIMATING REINVESTMENT

## Sales to Invested Capital: Reinvestment

![](_page_196_Diagram_13.jpeg)

A company with higher expected growth in revenues will need to reinvest more, though how much will be determined by the business that it operates in, with less reinvestment needed if it has excess capacity and a lag between reinvestment and growth.

# AIRBNB: REINVESTMENT AND PROFITABILITY

### Taxes

Note that losses are carried forward and the company starts paying taxes only in year 5. Target tax rate is 25%.

### Reinvestment

$$\text{Reinvestment} = \text{Net Cap Ex} + \text{Acquisitions} + \text{Capitalized R\&D} + \text{Chg in Working Capital}$$

To estimate the reinvestment, I divide the change in sales in that year by the sales to invested capital ratio.

| Year | Revenues      | Operating Margin | EBIT         | EBIT (1-t)   | Change in Sales | Sales to Capital | Reinvestment | FCFF           | Invested Capital | ROIC    |
|------|---------------|------------------|--------------|--------------|-----------------|------------------|--------------|----------------|------------------|---------|
|      | \$ 3,625,731  | -13.69%          | \$ (496,542) | \$ (496,542) |                 | 1.92             |              |                | \$ 1,370,158     | -36.24% |
| 1    | \$ 4,691,698  | -10.00%          | \$ (469,170) | \$ (469,170) | \$ 1,065,967    | 2.00             | \$ 532,984   | \$ (1,002,153) | \$ 1,903,142     | -24.65% |
| 2    | \$ 5,989,797  | -3.00%           | \$ (179,694) | \$ (179,694) | \$ 1,298,098    | 2.00             | \$ 649,049   | \$ (828,743)   | \$ 2,552,191     | -7.04%  |
| 3    | \$ 7,565,479  | 0.50%            | \$ 37,827    | \$ 37,827    | \$ 1,575,683    | 2.00             | \$ 787,841   | \$ (750,014)   | \$ 3,340,033     | 1.13%   |
| 4    | \$ 9,554,641  | 4.00%            | \$ 382,186   | \$ 382,186   | \$ 1,989,162    | 2.00             | \$ 994,581   | \$ (612,395)   | \$ 4,334,613     | 8.82%   |
| 5    | \$ 12,065,542 | 7.50%            | \$ 904,916   | \$ 777,799   | \$ 2,510,900    | 2.00             | \$ 1,255,450 | \$ (477,651)   | \$ 5,590,064     | 13.91%  |
| 6    | \$ 14,674,089 | 9.52%            | \$ 1,397,269 | \$ 1,047,952 | \$ 2,608,547    | 2.00             | \$ 1,304,274 | \$ (256,322)   | \$ 6,894,337     | 15.20%  |
| 7    | \$ 17,163,026 | 13.39%           | \$ 2,298,389 | \$ 1,723,792 | \$ 2,488,937    | 2.00             | \$ 1,244,469 | \$ 479,323     | \$ 8,138,806     | 21.18%  |
| 8    | \$ 19,274,804 | 17.26%           | \$ 3,327,026 | \$ 2,495,269 | \$ 2,111,778    | 2.00             | \$ 1,055,889 | \$ 1,439,380   | \$ 9,194,695     | 27.14%  |
| 9    | \$ 20,748,969 | 21.13%           | \$ 4,384,362 | \$ 3,288,271 | \$ 1,474,165    | 2.00             | \$ 737,082   | \$ 2,551,189   | \$ 9,931,777     | 33.11%  |
| 10   | \$ 21,370,016 | 25.00%           | \$ 5,342,504 | \$ 4,006,878 | \$ 621,047      | 2.00             | \$ 310,524   | \$ 3,696,354   | \$ 10,242,301    | 39.12%  |

### Invested Capital

Invested Capital in year t = Invested Capital in year t + Reinvestment

### Investment Returns

ROIC = EBIT (1-t) / Invested Capital in year t

# AGGREGATE VERSUS MARGINAL VALUES

- ▪ While **sustainable growth equations** are stated in terms of returns on capital (equity) or sales to capital the numbers that drive growth are returns on new investments, i.e., **marginal returns on capital (equity) or marginal sales to capital ratios**.
- ▪ The marginal returns and sales to capital ratios can be computed by looking at changes from year to year:
  - ▪  $\text{Marginal ROC} = \frac{(\text{Operating Income}_t - \text{Operating Income}_{t-1})}{(\text{Invested Capital}_{t-1} - \text{Invested Capital}_{t-2})}$
  - ▪  $\text{Marginal ROC} = \frac{(\text{Sales}_t - \text{Sales}_{t-1})}{(\text{Invested Capital}_{t-1} - \text{Invested Capital}_{t-2})}$
- ▪ As companies scale up, **the marginal values for these variables can diverge from the aggregate values**.
  - ▪ For companies where there are investing economies to scale, the marginal values can be significantly higher than the aggregate values.
  - ▪ For companies that are facing changing competitor or are entering new businesses, the marginal values can be lower than the aggregate values.

![](_page_199_Picture_4.jpeg)

# CLOSURE IN VALUATION

The Big Enchilada

# GETTING CLOSURE IN VALUATION

- ▪ A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

$$\text{Value} = \sum_{t=1}^{t=\infty} \frac{CF_t}{(1+r)^t}$$

- ▪ Since we cannot estimate cash flows forever, we estimate cash flows for a “growth period” and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \sum_{t=1}^{t=N} \frac{CF_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^N}$$

# WAYS OF ESTIMATING TERMINAL VALUE

| Approach                   | Inputs and Value                                                                                        | Types of business                                                                                |
|----------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Liquidation Value          | Liquidation value of assets held by the firm in the terminal year.                                      | Businesses built around a key person or a time-limited competitive advantage (license or patent) |
| Going Concern (Perpetuity) | $TV \text{ in year } n = CF_{n+1} / (r - g)$ , where $g = \text{growth rate forever}$                   | Going concerns with long lives (>40 years)                                                       |
| Going Concern (Finite)     | $TV \text{ in year } n = PV \text{ of } CF \text{ in years } n+1 \text{ to } n+k$ , where $k$ is finite | Going concerns with shorter lives                                                                |
| Pricing                    | Terminal Year Operating Metric<br>* Estimated Multiple of Metric                                        | <b>Never appropriate in an intrinsic valuation.</b>                                              |

# 1. WITH PERPETUAL GROWTH, OBEY THE GROWTH CAP

- ▪ When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

$$\text{Value} = \text{Expected Cash Flow Next Period} / (r - g)$$

$$r = \text{Discount rate (Cost of Equity or Cost of Capital)}$$

$$g = \text{Expected growth rate}$$

- ▪ The stable growth rate cannot exceed the growth rate of the economy, but it can be lower.
  - ▪ If the economy is composed of high growth and stable growth firms, the **growth rate of the latter will be lower than the growth rate of the economy**.
  - ▪ The **stable growth rate can be negative**, for companies in declining businesses.
  - ▪ If you use **nominal cashflows and discount rates**, the growth rate should be nominal in the currency in which the valuation is denominated.

# RISK FREE RATES AND NOMINAL GDP GROWTH

- ▪ **Risk free Rate = Expected Inflation + Expected Real Interest Rate**
- ▪ **Nominal GDP Growth = Expected Inflation + Expected Real Growth**
- ▪ The real interest rate is what borrowers agree to return to lenders in real goods/services.
- ▪ The real growth rate in the economy measures the expected growth in the production of goods and services.

## The argument for Risk free rate = Nominal GDP growth

1. 1. In the long term, the real growth rate cannot be lower than the real interest rate, since the growth in goods/services has to be enough to cover the promised rate.
2. 2. In the long term, the real growth rate can be higher than the real interest rate, to compensate risk taking. However, as economies mature, the difference should get smaller and since there will be growth companies in the economy, it is prudent to assume that the extra growth comes from these companies.

| Time Period | Ten-year T.Bond rate | Inflation rate | Real GDP growth | Nominal GDP Growth Rate |
|-------------|----------------------|----------------|-----------------|-------------------------|
| 1954-2021   | 5.59%                | 3.55%          | 2.94%           | 6.50%                   |
| 1954-1980   | 5.83%                | 4.49%          | 3.50%           | 7.98%                   |
| 1981-2008   | 6.88%                | 3.26%          | 3.04%           | 6.30%                   |
| 2011-2021   | 2.25%                | 1.76%          | 1.70%           | 3.46%                   |

# A PRACTICAL REASON FOR USING THE RISK FREE RATE CAP – PRESERVE CONSISTENCY

- ■ You are implicitly making assumptions about nominal growth in the economy, with your riskfree rate. Thus, with a low risk free rate, you are assuming low nominal growth in the economy (with low inflation and low real growth) and with a high risk free rate, a high nominal growth rate in the economy.
- ■ If you make an explicit assumption about nominal growth in cash flows that is at odds with your implicit growth assumption in the denominator, you are being inconsistent and bias your valuations:
  - ■ If you assume high nominal growth in the economy, with a low risk free rate, you will over value businesses.
  - ■ If you assume low nominal growth rate in the economy, with a high risk free rate, you will under value businesses.

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

Firm's D/E RaSo: 66.98%

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

PV(Terminal value) € 36,390.85 PV (CF over next 10 years) € 15,300.34 Value of operating assets = € 51,691.19 - Debt € 19,709.52 - Minority interests € 1,069.00 + Cash € 1,751.60 + Non-operating assets € 1,401.00 Value of equity € 34,065.26 Number of shares 571.10 Estimated value /share € 59.65 Price € 93.25 Price as % of value 56.33%

## 2. DON'T WAIT TOO LONG...

- ▪ Most growth firms have difficulty sustaining their growth for long periods, especially while earning excess returns. Assuming long growth periods for all firms is ignoring this reality.
  - ▪ **Proposition 1:** The **larger the potential market** for a company's products and services, the greater the likelihood that you can maintain growth for longer.
  - ▪ **Proposition 2:** The **smaller a company**, relative to the market it aspires to reach, the longer the potential growth period can be.
- ▪ It is not growth per se that creates value but growth with excess returns. For growth firms to continue to generate value-creating growth, they have to be able to keep the competition at bay.
  - ▪ **Proposition 3:** The **stronger and more sustainable the competitive advantages**, the longer a growth company can sustain “value creating” growth.
  - ▪ **Proposition 4:** Growth companies with strong and sustainable competitive advantages are rare.

# 3. DO NOT FORGET THAT GROWTH HAS TO BE EARNED..

- The reinvestment rate in stable growth will be a function of the stable growth rate and return on capital in perpetuity
  - Reinvestment Rate = Stable g/ Stable period ROC = g/ ROC
  - Terminal Value in year n =  $\frac{EBIT_{n+1} (1-t)(1 - \frac{g}{ROC})}{(\text{Cost of Capital} - g)}$

|                     |      | Return on capital in perpetuity |         |         |         |         |
|---------------------|------|---------------------------------|---------|---------|---------|---------|
|                     |      | 6%                              | 8%      | 10%     | 12%     | 14%     |
| Growth rate forever | 0.0% | \$1,000                         | \$1,000 | \$1,000 | \$1,000 | \$1,000 |
|                     | 0.5% | \$965                           | \$987   | \$1,000 | \$1,009 | \$1,015 |
|                     | 1.0% | \$926                           | \$972   | \$1,000 | \$1,019 | \$1,032 |
|                     | 1.5% | \$882                           | \$956   | \$1,000 | \$1,029 | \$1,050 |
|                     | 2.0% | \$833                           | \$938   | \$1,000 | \$1,042 | \$1,071 |
|                     | 2.5% | \$778                           | \$917   | \$1,000 | \$1,056 | \$1,095 |
|                     | 3.0% | \$714                           | \$893   | \$1,000 | \$1,071 | \$1,122 |

# EXCESS RETURNS TO ZERO?

- ■ There are some (McKinsey, for instance) who argue that the return on capital should always be equal to cost of capital in stable growth.
- ■ But excess returns seem to persist for very long time periods.

## A more sustainable measure

Median for top 500 publicly listed US companies by revenues in 1965, 1975, 1985, and 1995

Returns on invested capital (ROIC) is sustainable over time, but growth inevitably declines.

ROIC,<sup>1</sup> %

![](_page_208_Figure_40.jpeg)

Real revenue growth,<sup>1</sup> %

![](_page_208_Figure_42.jpeg)

# AND DON'T FALL FOR SLEIGHT OF HAND...

- ▪ A typical assumption in many DCF valuations, when it comes to stable growth, is that capital expenditures offset depreciation and there are no working capital needs. Stable growth firms, we are told, just have to make maintenance cap ex (replacing existing assets ) to deliver growth.
- a. If you make this assumption, what expected growth rate can you use in your terminal value computation?
- b. What if the stable growth rate = inflation rate? Is it okay to make this assumption then?

## 4. BE INTERNALLY CONSISTENT

- ▪ Risk and costs of equity and capital: Stable growth firms tend to
  - ▪ Have betas closer to one
  - ▪ Have debt ratios closer to industry averages (or mature company averages)
  - ▪ Country risk premiums (especially in emerging markets should evolve over time)
- ▪ The excess returns at stable growth firms should approach (or become) zero. ROC -> Cost of capital and ROE -> Cost of equity
- ▪ The reinvestment needs and dividend payout ratios should reflect the lower growth and excess returns:
  - ▪ Stable period payout ratio =  $1 - g/ROE$
  - ▪ Stable period reinvestment rate =  $g/ROC$

![](_page_211_Picture_12.jpeg)

# BEYOND INPUTS: CHOOSING AND USING THE RIGHT MODEL

Choosing the right model

# SUMMARIZING THE INPUTS

- ▪ In summary, at this stage in the process, we should have an estimate of the
  - ▪ the **current cash flows on the investment**, either to equity investors (dividends or free cash flows to equity) or to the firm (cash flow to the firm)
  - ▪ the **current cost of equity and/or capital** on the investment
  - ▪ the **expected growth rate in earnings**, based upon historical growth, analysts forecasts and/or fundamentals
- ▪ The next step in the process is deciding
  - ▪ which cash flow to discount, which should indicate
  - ▪ which discount rate needs to be estimated and
  - ▪ what pattern we will assume growth to follow

# WHICH CASH FLOW SHOULD I DISCOUNT?

- ▪ Use Equity Valuation
  - (a) for firms which have stable leverage, whether high or not...
  - (b) For all financial service firms
- ▪ Use Firm Valuation
  - (a) for firms which have leverage which is too high or too low, and expect to change the leverage over time, because debt payments and issues do not have to be factored in the cash flows and the discount rate (cost of capital) does not change dramatically over time.
  - (b) for firms for which you have partial information on leverage (eg: interest expenses are missing..)
  - (c) in all other cases, where you are more interested in valuing the firm than the equity. (Value Consulting?)

# GIVEN CASH FLOWS TO EQUITY, SHOULD I DISCOUNT DIVIDENDS OR FCFE?

- ■ Use the **Dividend Discount Model**

- (a) For firms which pay dividends (and repurchase stock) which are close to the Free Cash Flow to Equity (over a extended period)

- (b) For firms where FCFE are difficult to estimate (Example: Banks and Financial Service companies)

- ■ Use the **FCFE Model**

- (a) For **firms which pay dividends which are significantly higher or lower than the Free Cash Flow to Equity**. (What is significant? ... As a rule of thumb, if dividends are less than 80% of FCFE or dividends are greater than 110% of FCFE over a 5-year period, use the FCFE model)

- (b) For **firms where dividends are not available** (Example: Private Companies, IPOs)

# WHAT DISCOUNT RATE SHOULD I USE?

- ▪ Cost of Equity versus Cost of Capital
  - ▪ If discounting cash flows to equity -> Cost of Equity
  - ▪ If discounting cash flows to the firm -> Cost of Capital
- ▪ What currency should the discount rate (risk free rate) be in?
  - ▪ Match the currency in which you estimate the risk free rate to the currency of your cash flows
- ▪ Should I use real or nominal cash flows?
  - ▪ If discounting real cash flows -> real cost of capital
  - ▪ If nominal cash flows -> nominal cost of capital
  - ▪ If inflation is low (<10%), stick with nominal cash flows since taxes are based upon nominal income
  - ▪ If inflation is high (>10%) switch to real cash flows

# WHICH GROWTH PATTERN SHOULD I USE?

## Use a Stable Growth Model

- ▪ If your firm is
  - ▪ large and growing at a rate close to or less than growth rate of the economy, or
  - ▪ constrained by regulation from growing at rate faster than the economy
  - ▪ has the characteristics of a stable firm (average risk & reinvestment rates)

## Use a 2-Stage Growth Model

- ▪ If your firm
  - ▪ is large & growing at a moderate rate ( $\leq$  Overall growth rate + 10%) or
  - ▪ has a single product & barriers to entry with a finite life (e.g. patents)

## Use a 3-Stage or n-stage Model

- ▪ If your firm
  - ▪ is small and growing at a very high rate ( $>$  Overall growth rate + 10%) or
  - ▪ has significant barriers to entry into the business
  - ▪ has firm characteristics that are very different from the nor

# THE BUILDING BLOCKS OF VALUATION

![]()![](_page_218_Picture_12.jpeg)

# TYING UP LOOSE ENDS

The trouble starts after you tell me you are done..

# BUT WHAT COMES NEXT?

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

# 1. THE VALUE OF CASH

- ■ The simplest and most direct way of dealing with cash and marketable securities is to keep it out of the valuation - the cash flows should be before interest income from cash and securities, and the discount rate should not be contaminated by the inclusion of cash. (Use betas of the operating assets alone to estimate the cost of equity).
- ■ Once the operating assets have been valued, you should add back the value of cash and marketable securities.
- ■ In many equity valuations, the interest income from cash is included in the cashflows. The discount rate has to be adjusted then for the presence of cash. (The beta used will be weighted down by the cash holdings). Unless cash remains a fixed percentage of overall value over time, these valuations will tend to break down.

# AN EXERCISE IN CASH VALUATION

|                            | Company A | Company B | Company C |
|----------------------------|-----------|-----------|-----------|
| Enterprise Value           | \$1,000.0 | \$1,000.0 | \$1,000.0 |
| Cash                       | \$100.0   | \$100.0   | \$100.0   |
| Return on invested capital | 10%       | 5%        | 22%       |
| Cost of capital            | 10%       | 10%       | 12%       |
| Trades in                  | US        | US        | Argentina |

In which of these companies is cash most likely to be

1. A Neutral Asset (worth \$100 million)
2. A Wasting Asset (worth less than \$100 million)
3. A Potential Value Creator (worth >\$100 million)

# SHOULD YOU EVER DISCOUNT CASH FOR ITS LOW RETURNS?

- ■ There are some analysts who argue that companies with a lot of cash on their balance sheets should be penalized by having the excess cash discounted to reflect the fact that it earns a low return.
  - ■ Excess cash is usually defined as holding cash that is greater than what the firm needs for operations.
  - ■ A low return is defined as a return lower than what the firm earns on its non-cash investments.
- ■ This is the wrong reason for discounting cash. If the cash is invested in riskless securities, it should earn a low rate of return. As long as the return is high enough, given the riskless nature of the investment, cash does not destroy value.
- ■ There is a right reason, though, that may apply to some companies... Managers can do stupid things with cash (overpriced acquisitions, pie-in-the-sky projects....) and you have to discount for this possibility.

# CASH: DISCOUNT OR PREMIUM?

*Market Value of \$ 1 in cash:  
Estimates obtained by regressing Enterprise Value against Cash Balances*

![](_page_223_Figure_12.jpeg)

# A DETOUR: CLOSED END MUTUAL FUNDS

![](_page_224_Figure_56.jpeg)

- ■ Assume that you have a closed-end fund that invests in ‘average risk’ stocks. Assume also that you expect the market (average risk investments) to make 11.5% annually over the long term. If the closed end fund underperforms the market by 0.50%, estimate the discount on the fund.

# THE MOST FAMOUS CLOSED END FUND IN HISTORY?

Berkshire Hathaway: Price to Book - 1993 to 2022

![](_page_225_Figure_14.jpeg)

![](_page_225_Picture_15.jpeg)

**Buffett (93)**  
**Munger (RIP)**

## 2. DEALING WITH HOLDINGS IN OTHER FIRMS

- ■ Holdings in other firms can be categorized into
  - ■ Minority passive holdings, in which case only the dividend from the holdings is shown in the balance sheet
  - ■ Minority active holdings, in which case the share of equity income is shown in the income statements
  - ■ Majority active holdings, in which case the financial statements are consolidated.
- ■ In an intrinsic valuation, you would like to estimate the intrinsic value of these holdings and including them in your overall intrinsic valuation of the company.

# IF YOU REALLY WANT TO VALUE CROSS HOLDINGS RIGHT....

- ▪ Step 1: Value the parent company without any cross holdings. This will require using unconsolidated financial statements rather than consolidated ones.
- ▪ Step 2: Value each of the cross holdings individually. (If you use the market values of the cross holdings, you will build in errors the market makes in valuing them into your valuation).
- ▪ Step 3: The final value of the equity in the parent company with N cross holdings will be:
  - Value of parent company
  - – Debt of parent company
  - +  $\sum_{j=1}^{j=N} \% \text{ owned of Company } j * (\text{Value of Company } j - \text{Debt of Company } j)$

# VALUING YAHOO AS THE SUM OF ITS INTRINSIC PIECES

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

| Operating assets =<br>\$127,484                 |
|-------------------------------------------------|
| + Cash = \$27963                                |
| - Debt = \$6,670                                |
| Equity = \$145,587<br>22.1% of value = \$32,175 |

- Loose Ends =

- Taxes due  
= \$5,017

- Yahoo  
options =  
\$298

**Equity value= \$41,571  
Per share = \$41.19**

# IF YOU HAVE TO SETTLE FOR AN APPROXIMATION, TRY THIS...

- ▪ For majority holdings, **with full consolidation**, convert the minority interest from book value to market value by **applying a price to book ratio** (based upon the sector average for the subsidiary) to the minority interest.
  - ▪ Estimated market value of minority interest = Minority interest on balance sheet \* Price to Book ratio for sector (of subsidiary)
  - ▪ Subtract this from the estimated value of the consolidated firm to get to value of the equity in the parent company.
- ▪ For minority holdings in other companies, convert the **book value of these holdings (which are reported on the balance sheet) into market value by multiplying by the price to book ratio of the sector(s)**. Add this value on to the value of the operating assets to arrive at total firm value.

# YAHOO: A PRICING GAME?

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

# 3. OTHER ASSETS THAT HAVE NOT BEEN COUNTED YET..

- ▪ Assets that you should not be counting (or adding on to DCF values)
  - ▪ **If an asset is contributing to your cashflows, you cannot count the market value of the asset in your value.**
- ▪ Assets that you can count (or add on to your DCF valuation)
  - ▪ **Overfunded pension plans:** If you have a defined benefit plan and your assets exceed your expected liabilities, you could consider the over funding with two caveats:
    - ▪ Collective bargaining agreements may prevent you from laying claim to these excess assets.
    - ▪ There are tax consequences. Often, withdrawals from pension plans get taxed at much higher rates.
  - ▪ **Unutilized assets:** If you have assets or property that are not being utilized to generate cash flows (vacant land, for example), you have not valued them yet. You can assess a market value for these assets and add them on to the value of the firm.

# AN UNCOUNTED ASSET?

Price tag: \$200 million

![](_page_232_Picture_15.jpeg)

The longtime home of Playboy magazine founder Hugh Hefner is to be sold to Daren Metropoulos, a principal at private-equity firm Metropoulos & Co. PHOTO: GETTY IMAGES

# 4. A DISCOUNT FOR COMPLEXITY: AN EXPERIMENT

|                  | <i>Company A</i> | <i>Company B</i> |
|------------------|------------------|------------------|
| Operating Income | \$ 1 billion     | \$ 1 billion     |
| Tax rate         | 40%              | 40%              |
| ROIC             | 10%              | 10%              |
| Expected Growth  | 5%               | 5%               |
| Cost of capital  | 8%               | 8%               |
| Business Mix     | Single           | Multiple         |
| Holdings         | Simple           | Complex          |
| Accounting       | Transparent      | Opaque           |

- ▪ Which firm would you value more highly?

# MEASURING COMPLEXITY: VOLUME OF DATA IN FINANCIAL STATEMENTS

| <i>Company</i>    | <i>Number of pages in last 10Q</i> | <i>Number of pages in last 10K</i> |
|-------------------|------------------------------------|------------------------------------|
| General Electric  | 65                                 | 410                                |
| Microsoft         | 63                                 | 218                                |
| Wal-mart          | 38                                 | 244                                |
| Exxon Mobil       | 86                                 | 332                                |
| Pfizer            | 171                                | 460                                |
| Citigroup         | 252                                | 1026                               |
| Intel             | 69                                 | 215                                |
| AIG               | 164                                | 720                                |
| Johnson & Johnson | 63                                 | 218                                |
| IBM               | 85                                 | 353                                |

# MEASURING COMPLEXITY: A COMPLEXITY SCORE

| Item                 | Factors                                                                | Follow-up Question                                      | Answer | Weighting factor | Hyundai Heavy Score |
|----------------------|------------------------------------------------------------------------|---------------------------------------------------------|--------|------------------|---------------------|
| Operating Income     | 1. Multiple Businesses                                                 | Number of businesses (with more than 10% of revenues) = | 3      | 2.00             | 6                   |
|                      | 2. One-time income and expenses                                        | Percent of operating income =                           | 5%     | 10.00            | 0.5                 |
|                      | 3. Income from unspecified sources                                     | Percent of operating income =                           | 15%    | 10.00            | 1.5                 |
|                      | 4. Items in income statement that are volatile                         | Percent of operating income =                           | 20%    | 5.00             | 1                   |
| Tax Rate             | 1. Income from multiple locales                                        | Percent of revenues from non-domestic locales =         | 75%    | 3.00             | 2.25                |
|                      | 2. Different tax and reporting books                                   | Yes or No                                               | No     | Yes=3            | 0                   |
|                      | 3. Headquarters in tax havens                                          | Yes or No                                               | No     | Yes=3            | 0                   |
|                      | 4. Volatile effective tax rate                                         | Yes or No                                               | Yes    | Yes=2            | 2                   |
| Capital Expenditures | 1. Volatile capital expenditures                                       | Yes or No                                               | Yes    | Yes=2            | 2                   |
|                      | 2. Frequent and large acquisitions                                     | Yes or No                                               | No     | Yes=4            | 0                   |
|                      | 3. Stock payment for acquisitions and investments                      | Yes or No                                               | No     | Yes=4            | 0                   |
| Working capital      | 1. Unspecified current assets and current liabilities                  | Yes or No                                               | Yes    | Yes=3            | 3                   |
|                      | 2. Volatile working capital items                                      | Yes or No                                               | Yes    | Yes=2            | 2                   |
| Expected Growth rate | 1. Off-balance sheet assets and liabilities (operating leases and R&D) | Yes or No                                               | No     | Yes=3            | 0                   |
|                      | 2. Substantial stock buybacks                                          | Yes or No                                               | No     | Yes=3            | 0                   |
|                      | 3. Changing return on capital over time                                | Yes or No                                               | Yes    | Yes=5            | 5                   |
|                      | 4. Unsustainably high return                                           | Yes or No                                               | Yes    | Yes=5            | 5                   |
| Cost of capital      | 1. Multiple businesses                                                 | Number of businesses (more than 10% of revenues) =      | 3      | 1.00             | 3                   |
|                      | 2. Operations in emerging markets                                      | Percent of revenues=                                    | 50%    | 5.00             | 2.5                 |
|                      | 3. Is the debt market traded?                                          | Yes or No                                               | No     | No=2             | 2                   |
|                      | 4. Does the company have a rating?                                     | Yes or No                                               | No     | No=2             | 2                   |
|                      | 5. Does the company have off-balance sheet debt?                       | Yes or No                                               | No     | Yes=5            | 0                   |
| No-operating assets  | Minority holdings as percent of book assets                            | Minority holdings as percent of book assets             | 30%    | 20.00            | 6                   |
| Firm to Equity value | Consolidation of subsidiaries                                          | Minority interest as percent of book value of equity    | 20%    | 20.00            | 4                   |
| Per share value      | Shares with different voting rights                                    | Does the firm have shares with different voting rights? | No     | Yes = 10         | 0                   |
|                      | Equity options outstanding                                             | Options outstanding as percent of shares                | 0%     | 10.00            | 0                   |
|                      |                                                                        | Complexity Score =                                      |        |                  | 49.75               |

# DEALING WITH COMPLEXITY

- ▪ In Discounted Cashflow Valuation
  - ▪ **The Aggressive Analyst:** Trust the firm to tell the truth and value the firm based upon the firm's statements about their value.
  - ▪ **The Conservative Analyst:** Don't value what you cannot see.
  - ▪ The Compromise: Adjust the value for complexity
    - ▪ **Adjust cash flows** for complexity
    - ▪ **Adjust the discount rate** for complexity
    - ▪ Adjust the **expected growth rate**/ length of growth period
    - ▪ Value the firm and then **discount value for complexity** (a complexity discount)
- ▪ In relative valuation
  - ▪ In a relative valuation, you may be able to assess the price that the market is charging for complexity:
  - ▪ With the hundred largest market cap firms, for instance:  
    $$PBV = 0.65 + 15.31 ROE - 0.55 Beta + 3.04 Expected growth rate - \mathbf{0.003} \#$$
      
    Pages in 10K

# 5. BE CIRCUMSPECT ABOUT DEFINING DEBT FOR COST OF CAPITAL PURPOSES...

- ▪ **General Rule:** Debt generally has the following characteristics:
  - ▪ **Contractual commitment** to make fixed payments in the future
  - ▪ The fixed payments **are tax deductible**
  - ▪ Failure to make the payments can **lead to either default or loss of control** of the firm to the party to whom payments are due.
- ▪ Defined as such, debt should include
  - ▪ All interest bearing liabilities, short term as well as long term
  - ▪ All leases, operating as well as capital
- ▪ Debt should not include
  - ▪ Accounts payable or supplier credit
- ▪ Be wary of your conservative impulses which will tell you to count everything as debt. That will push up the debt ratio and lead you to understate your cost of capital.

# BOOK VALUE OR MARKET VALUE

- ■ You are valuing a **distressed telecom company** and have arrived at an **estimate of \$ 1 billion for the enterprise value** (using a discounted cash flow valuation). The company has **\$ 1 billion in face value of debt outstanding** but the debt is **trading at 50% of face value (because of the distress)**. What is the value of the equity to you as an investor?
  - ■ The equity is worth nothing (EV minus Face Value of Debt)
  - ■ The equity is worth \$ 500 million (EV minus Market Value of Debt)
- ■ Would your answer be different if you were told that the liquidation value of the assets of the firm today is \$1.2 billion and that you were planning to liquidate the firm today?

# BUT YOU SHOULD CONSIDER OTHER POTENTIAL LIABILITIES WHEN GETTING TO EQUITY VALUE

- ▪ If you have **under funded pension fund or health care plans**, you should consider the under funding at this stage in getting to the value of equity.
  - ▪ If you do so, you should not double count by also including a cash flow line item reflecting cash you would need to set aside to meet the unfunded obligation.
  - ▪ You should not be counting these items as debt in your cost of capital calculations....
- ▪ If you have **contingent liabilities** - for example, a potential liability from a lawsuit that has not been decided - you should consider the expected value of these contingent liabilities
  - ▪ Value of contingent liability = Probability that the liability will occur \*  
    Expected value of liability

## 6. EQUITY TO EMPLOYEES: EFFECT ON VALUE

- ▪ In recent years, firms have turned to **giving employees (and especially top managers) equity option or restricted stock packages** as part of compensation. If they are options, they usually are long term and on volatile stocks. If restricted stock, the restrictions are usually on trading.
- ▪ These equity compensation packages are clearly valuable and the question becomes how best to deal with them in valuation.
- ▪ Two key issues with employee options:
  1. 1. How do options or restricted stock **granted in the past** affect equity value per share today?
  2. 2. How do **expected grants of either, in the future**, affect equity value today?

# THE EASIER PROBLEM: RESTRICTED STOCK GRANTS

- ■ When employee compensation takes the form of restricted stock grants, the solution is relatively simple.
  - ■ To account for restricted stock grants in the past, make sure that you count the restricted stock that have already been granted **in shares outstanding today**. That will reduce your value per share.
  - ■ To account for expected stock grants in the future, estimate the value of these grants as a percent of revenue and forecast that as expense **as part of compensation expenses**. That will reduce future income and cash flows.
- ■ This process has been made easier by accounting rules that have changed to require that stock based compensation be expensed in the year that they are granted. Thus, extrapolating past margins already incorporates stock based compensation.

# THE BIGGER CHALLENGE: EMPLOYEE OPTIONS

- ▪ It is true that options can increase the number of shares outstanding but dilution per se is not the problem.
- ▪ Options affect equity value at exercise because
  - ▪ Shares are **issued at below the prevailing market price**. Options get exercised only when they are in the money.
  - ▪ Alternatively, the company can use cashflows that would have been available to equity investors to **buy back shares which are then used to meet option exercise**. The lower cashflows reduce equity value.
- ▪ Options affect equity value before exercise because we have to build in the expectation that there is a probability of and a cost to exercise.

# A SIMPLE EXAMPLE...

- ■ XYZ company has \$ 100 million in free cashflows to the firm, growing 3% a year in perpetuity and a cost of capital of 8%. It has 100 million shares outstanding and \$ 1 billion in debt. Its value can be written as follows:

$$\text{Value of firm} = 100 / (.08 - .03) = 2000$$

$$\text{Debt} = 1000$$

$$= \text{Equity} = 1000$$

$$\text{Value per share} = 1000/100 = \$10$$

- ■ XYZ decides to give 10 million options at the money (with a strike price of \$10) to its CEO. What effect will this have on the value of equity per share?
  - a. None. The options are not in-the-money.
  - b. Decrease by 10%, since the number of shares could increase by 10 million
  - c. Decrease by less than 10%. The options will bring in cash into the firm but they have time value.

# I. THE DILUTED SHARE COUNT APPROACH

- The simplest way of dealing with options is to try to adjust the denominator for shares that will become outstanding if the options get exercised. In the example cited, this would imply the following:

$$\text{Value of firm} = 100 / (.08 - .03) = 2000$$

$$\text{Debt} = 1000$$

$$= \text{Equity} = 1000$$

$$\text{Number of diluted shares} = 110$$

$$\text{Value per share} = 1000/110 = \$9.09$$

- The diluted approach **fails to consider that exercising options will bring in cash into the firm**. Consequently, they will overestimate the impact of options and understate the value of equity per share.

## II. THE TREASURY STOCK APPROACH

- ■ The treasury stock approach adds the proceeds from the exercise of options to the value of the equity before dividing by the diluted number of shares outstanding.
- ■ In the example cited, this would imply the following:
  - Value of firm =  $100 / (.08 - .03)$  = 2000
  - Debt = 1000
  - = Equity = 1000
  - Number of diluted shares = 110
  - Proceeds from option exercise =  $10 * 10 = 100$
  - Value per share =  $(1000 + 100) / 110 = \$ 10$
- ■ The treasury stock approach **fails to consider the time premium on the options**. The treasury stock approach also has problems with out-of-the-money options. If considered, they can increase the value of equity per share. If ignored, they are treated as non-existent.

# III. OPTION VALUE DRAG

- ▪ Step 1: **Value the firm**, using discounted cash flow or other valuation models.
- ▪ Step 2: Subtract out the **value of the outstanding debt** to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly.
- ▪ Step 3: Subtract out the **market value (or estimated market value) of other equity claims**:
  - ▪  $\text{Value of Warrants} = \text{Market Price per Warrant} \times \text{Number of Warrants}$   
    : Alternatively estimate the value using option pricing model
  - ▪  $\text{Value of Conversion Option} = \text{Market Value of Convertible Bonds} - \text{Value of Straight Debt Portion of Convertible Bonds}$
  - ▪  $\text{Value of employee Options}$ : Value using the average exercise price and maturity.
- ▪ Step 4: Divide the remaining value of equity by the **number of shares outstanding** to get value per share.

# VALUING EQUITY OPTIONS ISSUED BY FIRMS... THE DILUTION PROBLEM

- ▪ Option pricing models can be used to value employee options with four caveats –
  - ▪ Employee options are **long term**, making the assumptions about constant variance and constant dividend yields much shakier,
  - ▪ Employee options **result in stock dilution**, and
  - ▪ Employee options are **often exercised before expiration**, making it dangerous to use European option pricing models.
  - ▪ Employee options cannot be exercised until the employee is vested.
- ▪ These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and **early exercise**, and **factoring in the dilution effect**. The resulting value can be adjusted for the **probability that the employee will not be vested**.

# VALUING EMPLOYEE OPTIONS

- ▪ To value employee options, you need the following inputs into the option valuation model:
  - ▪ Stock Price = \$ 10, Adjusted for dilution = \$9.58
  - ▪ Strike Price = \$ 10
  - ▪ Maturity = 10 years (Can reduce to reflect early exercise)
  - ▪ Standard deviation in stock price = 40%
  - ▪ Riskless Rate = 4%
- ▪ Using a dilution-adjusted Black Scholes model, we arrive at the following inputs:
  - ▪  $N(d1) = 0.8199$
  - ▪  $N(d2) = 0.3624$
  - ▪ Value per call =  $\$ 9.58 (0.8199) - \$10 e^{-(0.04) (10)(0.3624)} = \$5.42$

# VALUE OF EQUITY TO VALUE OF EQUITY PER SHARE

- ▪ Using the value per call of \$5.42, we can now estimate the value of equity per share after the option grant:
  - ▪ Value of firm =  $100 / (.08 - .03)$  = 2000
  - ▪ Debt = 1000
  - ▪ = Equity = 1000
  - ▪ Value of options granted = \$ 54.2
  - ▪ = Value of Equity in stock = \$945.8
  - ▪ / Number of shares outstanding / 100
  - ▪ = Value per share = \$ 9.46
- ▪ Note that this approach yields a higher value than the diluted share count approach (which ignores exercise proceeds) and a lower value than the treasury stock approach (which ignores the time premium on the options)

# OPTION GRANTS IN THE FUTURE...

- ▪ Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value.
- ▪ The simplest mechanism for bringing in future option grants into the analysis is to do the following:
  - ▪ Estimate the value of options granted each year over the last few years as a percent of revenues.
  - ▪ Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller.
  - ▪ Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.
- ▪ To the extent that accountants have been treating option grants as expenses in the year that they are granted already, you are effectively forecasting their continuance, when you keep those margins.

# AND DON'T PLAY THE ADJUSTED EARNINGS GAME

- ■ Over the last decade, just as accountants have come to their senses and treated stock-based compensation as an operating expense, companies and analysts have tried to reverse this move by adding back these expenses to arrive at “adjusted” EBITDA and earnings numbers.
- ■ The rationale that they provide is that options are non-cash expenses, and that they should be added back, just as we do depreciation.
- ■ The truth is that options are not non-cash expenses, but in-kind expenses, where equity in the firm is being paid out to employees. Consequently, you should not be adding them back.

# NARRATIVE AND NUMBERS: VALUATION AS A BRIDGE

Tell me a story..

# VALUATION AS A BRIDGE

## *Number Crunchers*

## *Story Tellers*

![](_page_253_Diagram_28.jpeg)

# STEP 1: SURVEY THE LANDSCAPE

- ▪ Every valuation starts with a narrative, a story that you see unfolding for your company in the future.
- ▪ In developing this narrative, you will be making assessments of
  - ▪ Your **company** (its products, its management and its history.
  - ▪ The **market or markets** that you see it growing in.
  - ▪ The **competition** it faces and will face.
  - ▪ The **macro environment** in which it operates.
- ▪ If understanding the products and services that a business sells makes it easier to construct a story, it follows that B2C (sell to final consumer) businesses will be easier to value than B2B businesses.

![](_page_255_Diagram_17.jpeg)

Aswath Damodaran

## **STEP 2: CREATE A NARRATIVE FOR THE FUTURE**

- ▪ Every valuation starts with a narrative, a story that you see unfolding for your company in the future.
- ▪ In developing this narrative, you will be making assessments of your company (its products, its management), the market or markets that you see it growing in, the competition it faces and will face and the macro environment in which it operates.
  - ▪ Rule 1: Keep it simple.
  - ▪ Rule 2: Keep it focused.
  - ▪ Rule 3: Stay grounded in reality.

# THE UBER NARRATIVE

- ▪ In June 2014, my initial narrative for Uber was that it would be
- ▪ An urban car service business: I saw Uber primarily as a force in urban areas and only in the car service business.
- ▪ Which would expand the business moderately (about 40% over ten years) by bringing in new users.
- ▪ With local networking benefits: If Uber becomes large enough in any city, it will quickly become larger, but that will be of little help when it enters a new city.
- ▪ Maintain its revenue sharing (20%) system due to strong competitive advantages (from being a first mover).
- ▪ And its existing low-capital business model, with drivers as contractors and very little investment in infrastructure.

# STEP 3: CHECK THE NARRATIVE AGAINST HISTORY, ECONOMIC FIRST PRINCIPLES & COMMON SENSE

![](_page_258_Diagram_10.jpeg)

# THE IMPOSSIBLE, THE IMPLAUSIBLE AND THE IMPROBABLE

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

### **Growth**

![](_page_259_Diagram_42.jpeg)

Risk

# UBER: POSSIBLE, PLAUSIBLE AND PROBABLE

Uber (My narrative))

![](_page_260_Diagram_11.jpeg)

# THE RUNAWAY STORY: WHEN YOU WANT A STORY TO BE TRUE...

- ■ With a runaway business story, you usually have three ingredients:
  - ■ Charismatic, likeable Narrator: The narrator of the business story is someone that you want to see succeed, either because you like the narrator or because he/she will be a good role model.
  - ■ Telling a story about disrupting a much business, where you dislike the status quo: The status quo in the business that the story is disrupting is dissatisfying (to everyone involved)>
  - ■ With a societal benefit as bonus: And if the story holds, society and humanity will benefit.
- ■ Since you want this story to work out, you stop asking questions, because the answers may put the story at risk.

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

![](_page_262_Figure_10.jpeg)

The Story The Checks (?)

+ Money

+

# The Impossible: The Runaway Story

![](_page_262_Picture_2.jpeg)

![](_page_262_Picture_3.jpeg)

# WHEN RUNAWAY STORIES MELT DOWN..

## The Meltdown Story

**Untrustworthy Storyteller**  
A narrator, who through his/her words or actions has become untrustworthy.

+

**Story at war with numbers**  
The company's narrative conflicts with its own actions and/or with the actual results/numbers reported by the company.

+

**Bad Business Model**  
The business model has a fundamental flaw that can affect either future profitability or survival, but the management is either in denial about the flaw or opaque in how it plans to deal with it.

=

**Meltdown Story**  
Investors, lenders and observers question story, unwilling to accept the company's spin on number, pushing pricing down.

# The Implausible: The Big Market Delusion

![](_page_264_Diagram_11.jpeg)

![](_page_264_Diagram_12.jpeg)

| Company             | Market Cap            | Enterprise Value      | Current Revenues    | Breakeven Revenues (2025) | % from Online Advertising | Imputed Online Ad Revenue (2025) |
|---------------------|-----------------------|-----------------------|---------------------|---------------------------|---------------------------|----------------------------------|
| Google              | \$441,572.00          | \$386,954.00          | \$69,611.00         | \$224,923.20              | 89.50%                    | \$201,306.26                     |
| Facebook            | \$245,662.00          | \$234,696.00          | \$14,640.00         | \$129,375.54              | 92.20%                    | \$119,284.25                     |
| Yahoo!              | \$30,614.00           | \$23,836.10           | \$4,871.00          | \$25,413.13               | 100.00%                   | \$25,413.13                      |
| LinkedIn            | \$23,265.00           | \$20,904.00           | \$2,561.00          | \$22,371.44               | 80.30%                    | \$17,964.26                      |
| Twitter             | \$16,927.90           | \$14,912.90           | \$1,779.00          | \$23,128.68               | 89.50%                    | \$20,700.17                      |
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

|                                     | FY 2013      | FY 2014      | FY 2015      | FY 2016      | FY 2017       | FY 2018       | FY 2019       | FY 2020       | FY 2021       | FY 2022       | FY 2023       | FY 2024       | FY 2025       | FY 2026       | FY 2027              | FY 2028       |                       |                               |
|-------------------------------------|--------------|--------------|--------------|--------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|----------------------|---------------|-----------------------|-------------------------------|
| Unit Volume                         | 24,298       | 36,883       | 64,684       | 86,713       | 149,869       | 214,841       | 291,861       | 384,747       | 466,559       | 550,398       | 643,850       | 726,655       | 820,645       | 922,481       | 1,034,215            | 1,137,780     |                       |                               |
| % Growth                            |              | 52%          | 75%          | 34%          | 73%           | 43%           | 36%           | 32%           | 21%           | 18%           | 17%           | 13%           | 13%           | 12%           | 12%                  | 10%           |                       |                               |
| Automotive Revenue Per Unit (\$)    | 93,403       | 85,342       | 83,432       | 78,932       | 65,465        | 58,258        | 56,407        | 55,553        | 55,991        | 56,586        | 56,969        | 57,540        | 58,138        | 58,603        | 59,002               | 59,554        |                       |                               |
| % Growth                            |              | -9%          | -2%          | -5%          | -17%          | -11%          | -3%           | -2%           | 1%            | 1%            | 1%            | 1%            | 1%            | 1%            | 1%                   | 1%            |                       |                               |
| Automotive Sales                    | 2,462        | 3,321        | 5,613        | 7,051        | 10,025        | 12,720        | 16,685        | 21,595        | 26,347        | 31,357        | 36,897        | 42,022        | 47,949        | 54,283        | 61,221               | 67,980        |                       |                               |
| Development Service Sales           | 16           | 40           | 42           | 44           | 46            | 49            | 51            | 54            | 56            | 59            | 62            | 65            | 68            | 72            | 75                   | 79            |                       |                               |
| <b>Total Sales</b>                  | <b>2,478</b> | <b>3,361</b> | <b>5,655</b> | <b>7,095</b> | <b>10,072</b> | <b>12,768</b> | <b>16,736</b> | <b>21,648</b> | <b>26,403</b> | <b>31,416</b> | <b>36,959</b> | <b>42,087</b> | <b>48,017</b> | <b>54,355</b> | <b>61,296</b>        | <b>68,059</b> |                       |                               |
| % Growth                            |              | 36%          | 60%          | 25%          | 42%           | 27%           | 31%           | 29%           | 22%           | 19%           | 18%           | 14%           | 14%           | 13%           | 13%                  | 11%           |                       |                               |
| <b>EBITDA</b>                       | <b>148</b>   | <b>417</b>   | <b>920</b>   | <b>1,042</b> | <b>1,586</b>  | <b>2,150</b>  | <b>3,138</b>  | <b>4,066</b>  | <b>4,857</b>  | <b>5,723</b>  | <b>6,328</b>  | <b>7,182</b>  | <b>8,144</b>  | <b>9,688</b>  | <b>10,874</b>        | <b>12,099</b> |                       |                               |
| % Margin                            | 6.0%         | 12.4%        | 16.3%        | 14.7%        | 15.7%         | 16.8%         | 18.7%         | 18.8%         | 18.4%         | 18.2%         | 17.1%         | 17.1%         | 17.0%         | 17.8%         | 17.7%                | 17.8%         |                       |                               |
| D&A                                 | 103          | 158          | 172          | 203          | 301           | 353           | 389           | 537           | 606           | 696           | 811           | 938           | 1,088         | 1,260         | 1,451                | 1,661         |                       |                               |
| % of Capex                          | 41%          | 79%          | 59%          | 65%          | 62%           | 69%           | 78%           | 86%           | 79%           | 77%           | 75%           | 76%           | 76%           | 76%           | 76%                  | 77%           |                       |                               |
| <b>EBIT</b>                         | <b>45</b>    | <b>259</b>   | <b>748</b>   | <b>839</b>   | <b>1,285</b>  | <b>1,796</b>  | <b>2,749</b>  | <b>3,529</b>  | <b>4,252</b>  | <b>5,027</b>  | <b>5,517</b>  | <b>6,244</b>  | <b>7,056</b>  | <b>8,429</b>  | <b>9,423</b>         | <b>10,439</b> |                       |                               |
| % Margin                            | 1.8%         | 7.7%         | 13.2%        | 11.8%        | 12.8%         | 14.1%         | 16.4%         | 16.3%         | 16.1%         | 16.0%         | 14.9%         | 14.8%         | 14.7%         | 15.5%         | 15.4%                | 15.3%         |                       |                               |
| Net Interest Income (Expense)       | (27)         | (1)          | 9            | 33           | 47            | 90            | 108           | 155           | 199           | 278           | 358           | 445           | 542           | 651           | 784                  | 934           |                       |                               |
| Other Income                        | 28           | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0                    | 0             |                       |                               |
| <b>Pretax Income</b>                | <b>46</b>    | <b>258</b>   | <b>758</b>   | <b>872</b>   | <b>1,332</b>  | <b>1,886</b>  | <b>2,857</b>  | <b>3,684</b>  | <b>4,451</b>  | <b>5,305</b>  | <b>5,875</b>  | <b>6,688</b>  | <b>7,598</b>  | <b>9,080</b>  | <b>10,207</b>        | <b>11,373</b> |                       |                               |
| Income Taxes                        | 3            | 2            | 14           | 34           | 86            | 262           | 462           | 641           | 807           | 1,003         | 1,134         | 1,317         | 1,470         | 1,761         | 2,028                | 2,323         |                       |                               |
| % Effective Rate                    | 6%           | 1%           | 2%           | 4%           | 6%            | 14%           | 16%           | 17%           | 18%           | 19%           | 19%           | 20%           | 19%           | 19%           | 20%                  | 20%           |                       |                               |
| <b>Net Income</b>                   | <b>44</b>    | <b>256</b>   | <b>744</b>   | <b>839</b>   | <b>1,246</b>  | <b>1,624</b>  | <b>2,395</b>  | <b>3,043</b>  | <b>3,644</b>  | <b>4,303</b>  | <b>4,741</b>  | <b>5,372</b>  | <b>6,128</b>  | <b>7,319</b>  | <b>8,179</b>         | <b>9,050</b>  |                       |                               |
| <b>Plus</b>                         |              |              |              |              |               |               |               |               |               |               |               |               |               |               |                      |               |                       |                               |
| After-tax Interest Expense (Income) | 27           | 1            | (9)          | (33)         | (47)          | (90)          | (108)         | (154)         | (199)         | (278)         | (357)         | (444)         | (541)         | (650)         | (782)                | (932)         |                       |                               |
| Depreciation of PP&E                | 103          | 158          | 172          | 203          | 301           | 353           | 389           | 537           | 606           | 696           | 811           | 938           | 1,088         | 1,260         | 1,451                | 1,661         |                       |                               |
| Other                               | 0            | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0                    | 0             |                       |                               |
| <b>Loss</b>                         |              |              |              |              |               |               |               |               |               |               |               |               |               |               |                      |               |                       |                               |
| Change in Working Capital           | (155)        | (14)         | (157)        | (167)        | (172)         | (325)         | (163)         | (81)          | (28)          | (299)         | (356)         | (328)         | (219)         | (329)         | (365)                | (376)         |                       |                               |
| % of Change in Sales                | -2%          | -7%          | -12%         | -6%          | -12%          | -4%           | -2%           | -1%           | -6%           | -6%           | -6%           | -4%           | -5%           | -5%           | -6%                  | -6%           |                       |                               |
| Capital Expenditures                | 250          | 200          | 312          | 312          | 486           | 510           | 497           | 623           | 765           | 906           | 1,078         | 1,236         | 1,437         | 1,660         | 1,898                | 2,149         |                       |                               |
| % of Sales                          | 10%          | 6%           | 6%           | 4%           | 5%            | 4%            | 3%            | 3%            | 3%            | 3%            | 3%            | 3%            | 3%            | 3%            | 3%                   | 3%            |                       |                               |
| Other                               | 0            | 0            | 0            | 0            | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0             | 0                    | 0             |                       |                               |
| <b>Unlevered Free Cash Flow</b>     | <b>78</b>    | <b>229</b>   | <b>750</b>   | <b>863</b>   | <b>1,186</b>  | <b>1,702</b>  | <b>2,343</b>  | <b>2,884</b>  | <b>3,314</b>  | <b>4,113</b>  | <b>4,472</b>  | <b>4,959</b>  | <b>5,456</b>  | <b>6,597</b>  | <b>7,315</b>         | <b>8,005</b>  |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | EBITDA               | 12,099        |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Sales                | 68,059        |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Net Debt (Cash)      | (260)         |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Tesla Diluted Shares | 142           |                       |                               |
| Exit EBITDA High                    |              |              |              |              |               | 12.0 x        |               |               |               |               |               |               |               |               |                      |               |                       |                               |
| Exit EBITDA Low                     |              |              |              |              |               | 8.0 x         |               |               |               |               |               |               |               |               |                      |               |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Exit PPG High        | 5.0%          | Exit P/Sales High     | 180%                          |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Exit P/Sales Low     | 130%          |                       |                               |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Discount Rate High   | 13.0%         | FY Month of Valuation | 1.0 (Beginning of this Month) |
|                                     |              |              |              |              |               |               |               |               |               |               |               |               |               |               | Discount Rate Low    | 9.0%          | Month of FY End       | 12.0 (End of this Month)      |

# STEP 4: CONNECT YOUR NARRATIVE TO KEY DRIVERS OF VALUE

The Uber narrative (June 2014)

![](_page_266_Diagram_174.jpeg)

# STEP 4: VALUE THE COMPANY (UBER)

*Uber: Intrinsic valuation - June 8, 2014 (in US \$)*

![](_page_267_Figure_13.jpeg)

| <b>Value of operating assets = \$6,595</b> | <i>Discount back the cash flows (including terminal value) at the cumulated cost of capital.</i> |  |  |  |                                      |  |  |  |  |  |  |
|--------------------------------------------|--------------------------------------------------------------------------------------------------|--|--|--|--------------------------------------|--|--|--|--|--|--|
| Adust for probability of failure (10%)     | Cost of capital for first 5 years =                                                              |  |  |  | Cost of capital declines from 12% to |  |  |  |  |  |  |
| Expected value = \$6,595 (.9) = \$5,895    | Top decile of US companies =                                                                     |  |  |  | 8% from years 6 to 10.               |  |  |  |  |  |  |

*Based on the investment of \$1.2 billion made by investors, the imputed value for Uber's operating assets, in June 2014, was \$17 billion.*

## **STEP 5: KEEP THE FEEDBACK LOOP OPEN...**

- ▪ Not just car service company.: Uber is a car company, not just a car service company, and there may be a day when consumers will subscribe to a Uber service, rather than own their own cars. It could also expand into logistics, i.e., moving and transportation businesses.
- ▪ Not just urban: Uber can create new demands for car service in parts of the country where taxis are not used (suburbia, small towns).
- ▪ Global networking benefits: By linking with technology and credit card companies, Uber can have global networking benefits.

# VALUING BILL GURLEY'S UBER NARRATIVE

|                      | <i>Uber (Gurley)</i>                                                                                                                                                                                                                                         | <i>Uber (Gurley Mod)</i>                                                                                                                                                                                                                                    | <i>Uber (Damodaran)</i>                                                                                                                                                                                                         |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Narrative            | Uber will <u>expand the car service market substantially, bringing in mass transit users &amp; non-users from the suburbs into the market, and use its networking advantage to gain a dominant market share, while maintaining its revenue slice at 20%.</u> | Uber will <u>expand the car service market substantially, bringing in mass transit users &amp; non-users from the suburbs into the market, and use its networking advantage to gain a dominant market share, while cutting prices and margins (to 10%).</u> | Uber will expand the car service market moderately, primarily in urban environments, and use its <u>competitive advantages</u> to get a <u>significant but not dominant market share and maintain its revenue slice at 20%.</u> |
| Total Market         | \$300 billion, growing at 3% a year                                                                                                                                                                                                                          | \$300 billion, growing at 3% a year                                                                                                                                                                                                                         | \$100 billion, growing at 6% a year                                                                                                                                                                                             |
| Market Share         | 40%                                                                                                                                                                                                                                                          | 40%                                                                                                                                                                                                                                                         | 10%                                                                                                                                                                                                                             |
| Uber's revenue slice | 20%                                                                                                                                                                                                                                                          | 10%                                                                                                                                                                                                                                                         | 20%                                                                                                                                                                                                                             |
| Value for Uber       | \$53.4 billion + Option value of entering car ownership market (\$10 billion+)                                                                                                                                                                               | \$28.7 billion + Option value of entering car ownership market (\$6 billion+)                                                                                                                                                                               | \$5.9 billion + Option value of entering car ownership market (\$2-3 billion)                                                                                                                                                   |

# DIFFERENT NARRATIVES, DIFFERENT NUMBERS

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

# STEP 6: BE READY TO MODIFY NARRATIVE AS EVENTS UNFOLD

| Narrative Break/End                                                                                                                           | Narrative Shift                                                                                                  | Narrative Change (Expansion or Contraction)                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Events, external (legal, political or economic) or internal (management, competitive, default), that can cause the narrative to break or end. | Improvement or deterioration in initial business model, changing market size, market share and/or profitability. | Unexpected entry/success in a new market or unexpected exit/failure in an existing market.   |
| Your valuation estimates (cash flows, risk, growth & value) are no longer operative                                                           | Your valuation estimates will have to be modified to reflect the new data about the company.                     | Valuation estimates have to be redone with new overall market potential and characteristics. |
| Estimate a probability that it will occur & consequences                                                                                      | Monte Carlo simulations or scenario analysis                                                                     | Real Options                                                                                 |

![]()Let's have some fun!

**273**

# EQUITY RISK PREMIUMS IN VALUATION

- ▪ The equity risk premiums that I have used in the valuations that follow reflect my thinking (and how it has evolved) on the issue.
  - ▪ **Pre-1998 valuations:** In the valuations prior to 1998, I use a **risk premium of 5.5% for mature markets** (close to both the historical and the implied premiums then)
  - ▪ **Between 1998 and Sept 2008:** In the valuations between 1998 and September 2008, I used a **risk premium of 4% for mature markets**, reflecting my belief that risk premiums in mature markets do not change much and revert back to historical norms (at least for implied premiums).
  - ▪ **Valuations done in 2009:** After the 2008 crisis and the jump in equity risk premiums to 6.43% in January 2008, I have used a higher equity risk premium (5-6%) for the next 5 years and will assume a reversion back to historical norms (4%) only after year 5.
  - ▪ **After 2009:** I have used **updated implied equity risk premiums**, as of the time that I did the valuations.

# THE VALUATION SET UP

- ▪ With each company that I value in this next section, I will try to start with a story about the company and use that story to construct a valuation.
- ▪ With each valuation, rather than focus on all of the details (which will follow the blueprint already laid out), I will focus on a specific component of the valuation that is unique or different.
- ▪ Finally, while the valuations are scattered over time, they all represent valuations done in real time, with decisions that followed, and without the benefit of hindsight.

![](_page_275_Picture_15.jpeg)

# TRAINING WHEELS ON?

Stocks that look like Bonds, Things Change and Market Valuations

*Training Wheels valuation: Con Ed in August 2008*

In trailing 12 months, through June 2008 Earnings per share = \$3.17 Dividends per share = \$2.32 Dividend payout ratio is 73%

**Why a stable growth dividend discount model?**

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

**Test 3: Is the firm's risk and cost of equity consistent with a stable growith firm?** Beta of 0.80 is at lower end of the range of stable company betas: 0.8 -1.2

**Test 1: Is the firm paying dividends like a stable growth firm?**

# FROM DCF VALUE TO TARGET PRICE AND RETURNS...

- ▪ Assume that you believe that your valuation of Con Ed (\$42.30) is a fair estimate of the value, 7.70% is a reasonable estimate of Con Ed's cost of equity and that your expected dividends for next year ( $2.32 \times 1.021$ ) is a fair estimate, **what is the expected stock price a year from now (assuming that the market corrects its mistake)?**
- ▪ If you **bought the stock today at \$40.76**, what return can you expect to make over the next year (assuming again that the market corrects its mistake)?

### **Current Cashflow to Firm**

EBIT(1-t)= 5344 (1-**.35**)= 3474 - Nt CpX= 350 - Chg WC 691 = FCFF 2433 Reinvestment Rate = 1041/3474 =29.97% Return on capital = 25.19%

### **Expected Growth in**

**EBIT (1-t)** .30\*.25=.075 **7.5%**

### **Stable Growth**

g = 3%; Beta = 1.10; Debt Ratio= 20%; Tax rate=35% Cost of capital = 6.76% ROC= 6.76%; Reinvestment Rate=3/6.76=44%

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

### **Riskfree Rate**:

Riskfree rate = 3.72%

+

**Beta**  1.15 **X** **Risk Premium** 4%

Unlevered Beta for Sectors: 1.09

## 3M: A Pre-crisis valuation

Reinvestment Rate 30%

Return on Capital 25%

Term Yr

\$4,758 \$2,113 \$2,645

On September 12, 2008, 3M was trading at \$70/share

First 5 years

D/E=8.8%

Cost of capital = 8.32% (0.92) + 2.91% (0.08) = 7.88%

| Year           | 1       | 2       | 3       | 4       | 5         |
|----------------|---------|---------|---------|---------|-----------|
| EBIT (1-t)     | \$3,734 | \$4,014 | \$4,279 | \$4,485 | \$4,619   |
| - Reinvestment | \$1,120 | \$1,204 | \$1,312 | \$1,435 | \$1,540 , |
| = FCFF         | \$2,614 | \$2,810 | \$2,967 | \$3,049 | \$3,079   |

![](_page_279_Diagram_3.jpeg)

![](_page_279_Diagram_4.jpeg)

![](_page_279_Diagram_7.jpeg)

## 3M: Post-crisis valuation

On October 16, 2008, MMM was trading at \$57/share.

*Lowered base operating income by 10%*

*Higher default spread for next 5 years*

*Did not increase debt ratio in stable growth* 

# VALUING THE S&P 500 INDEX (SEPTEMBER 2022)

## Inflation and Equity Value: The Drivers

![](_page_280_Diagram_11.jpeg)

# 1. EARNINGS

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

# 2. CASH RETURN

**S&P 500 Aggregate Earnings, Dividends and Buybacks: 2001-2021**

| Year                | Earnings | Dividends | Buybacks | Dividend Payout | Cash Payout   |
|---------------------|----------|-----------|----------|-----------------|---------------|
| 2001                | 38.85    | 15.74     | 14.34    | 40.51%          | 77.43%        |
| 2002                | 46.04    | 15.96     | 13.87    | 34.67%          | 64.78%        |
| 2003                | 54.69    | 17.88     | 13.70    | 32.69%          | 57.74%        |
| 2004                | 67.68    | 19.01     | 21.59    | 28.09%          | 59.99%        |
| 2005                | 76.45    | 22.34     | 38.82    | 29.23%          | 80.01%        |
| 2006                | 87.72    | 25.04     | 48.12    | 28.55%          | 83.40%        |
| 2007                | 82.54    | 28.14     | 67.22    | 34.09%          | 115.53%       |
| 2008                | 49.51    | 28.45     | 39.07    | 57.46%          | 136.37%       |
| 2009                | 56.86    | 21.97     | 15.46    | 38.64%          | 65.82%        |
| 2010                | 83.77    | 22.65     | 32.88    | 27.04%          | 66.28%        |
| 2011                | 96.44    | 26.53     | 44.75    | 27.51%          | 73.91%        |
| 2012                | 96.82    | 31.25     | 44.65    | 32.28%          | 78.39%        |
| 2013                | 104.92   | 34.90     | 53.23    | 33.26%          | 84.00%        |
| 2014                | 116.16   | 39.55     | 62.44    | 34.04%          | 87.79%        |
| 2015                | 100.48   | 43.41     | 64.94    | 43.20%          | 107.83%       |
| 2016                | 106.26   | 45.70     | 62.32    | 43.01%          | 101.66%       |
| 2017                | 124.51   | 48.93     | 60.85    | 39.30%          | 88.17%        |
| 2018                | 152.78   | 54.39     | 96.11    | 35.60%          | 98.51%        |
| 2019                | 157.18   | 58.50     | 87.81    | 37.22%          | 93.08%        |
| 2020                | 139.76   | 57.00     | 61.66    | 40.78%          | 84.90%        |
| 2021                | 205.35   | 60.65     | 104.61   | 29.53%          | 80.48%        |
| <b>Average</b>      |          |           |          | <b>35.56%</b>   | <b>85.05%</b> |
| <b>1st Quartile</b> |          |           |          | <b>29.53%</b>   | <b>73.91%</b> |
| <b>Median</b>       |          |           |          | <b>34.09%</b>   | <b>83.40%</b> |
| <b>3rd Quartile</b> |          |           |          | <b>39.30%</b>   | <b>93.08%</b> |

*Quarterly Data on Earnings, Dividends and Buybacks: S&P 500*

![](_page_282_Figure_15.jpeg)

# MY S&P 500 STORY

An Intrinsic (and Personal) Valuation of the S&P 500 on September 23, 2022

### My Earnings Estimates

Analysts are underestimating the effect of a recession on future earnings, and I am reducing their 2023 estimates by 15%, with ripple effects on earnings beyond. (I am leaving 2022 estimates untouched, because the bulk of the year is behind us.)

### Cash Return

While companies have collectively returned 90.5% of earnings as dividends and buybacks in the most recent 12 months, recession fears and uncertainty will lead them to reduce this cash returns to 80% of earnings (consistent with growth in long term), over time.

| Intrinsic Value Estimate (based on your choice of ERP) |                |          |          |          |          |             |               |
|--------------------------------------------------------|----------------|----------|----------|----------|----------|-------------|---------------|
|                                                        | 2021           | 2022     | 2023     | 2024     | 2025     | 2026        | Terminal Year |
| Analyst Estimate of Earnings                           | 208.53         | 225.34   | 243.46   | 259.79   | 273.70   | 284.65      | 296.03        |
| My Estimate of Earnings                                | \$208.53       | 225.34   | 206.94   | 225.03   | 243.13   | 252.85      | 262.97        |
| Expected Earnings Growth Rate                          |                | 8.06%    | -8.16%   | 6.71%    | 5.35%    | 4.00%       | 4.00%         |
| Expected cash payout as % of earnings                  | 90.50%         | 90.50%   | 87.88%   | 85.25%   | 82.63%   | 80.00%      | 80.00%        |
| Expected Dividends + Buybacks =                        | \$188.72       | \$203.93 | \$181.85 | \$191.84 | \$200.89 | \$202.28    | 210.37        |
| Expected Terminal Value =                              |                |          |          |          |          | \$ 4,207.49 |               |
| Riskfree Rate                                          | 3.69%          | 3.75%    | 3.81%    | 3.88%    | 3.94%    | 4.00%       | 4.00%         |
| Required Return on Stocks                              | 8.69%          | 8.75%    | 8.81%    | 8.88%    | 8.94%    | 9.00%       | 9.00%         |
| Present Value =                                        |                | \$187.52 | \$153.67 | \$148.90 | \$143.12 | \$2,882.41  |               |
| <b>Intrinsic Value of Index =</b>                      | <b>3515.63</b> |          |          |          |          |             |               |
| <b>Actual Index level =</b>                            | <b>3693.23</b> |          |          |          |          |             |               |
| <b>% Under or Over Valuation =</b>                     | <b>-4.81%</b>  |          |          |          |          |             |               |

### Ten-year Treasury Bond Rate

I will assume that the bulk of the rise in rates has already occurred, and that the T.Bond rate will converge to 4%, over the next five years.

### Equity Risk Premium

The equity risk premium is 5%, close to both the historical average risk premium earned on stocks from 1928 - 2022 and the average implied equity risk premium over the last decade. Adding it to the ten-year bond rate yields the required return on stocks.

*In my overarching story for equities, I am building in the assumption that there will be a recession that creates both short term & long term damage to corporate earnings, but helps in restraining inflation, bringing it down from 2022 levels to about 3% in the long term (above the 2011-2021 average of 1.73%).*

|               |         | Valuing the S&P 500 on Sept 23, 2022 |         |         |                                |         |         |                      |         |
|---------------|---------|--------------------------------------|---------|---------|--------------------------------|---------|---------|----------------------|---------|
|               |         | Earnings = 30% below Estimates       |         |         | Earnings = 15% below Estimates |         |         | Earnings = Estimates |         |
| Riskfree Rate | ERP =4% | ERP =5%                              | ERP =6% | ERP =4% | ERP =5%                        | ERP =6% | ERP =4% | ERP =5%              | ERP =6% |
| <b>2%</b>     | 4276    | 3416                                 | 2842    | 4677    | 3737                           | 3110    | 5449    | 4348                 | 3615    |
| <b>3%</b>     | 4132    | 3303                                 | 2750    | 4519    | 3613                           | 3009    | 5169    | 4129                 | 3436    |
| <b>4%</b>     | 3979    | 3183                                 | 2653    | 4352    | 3482                           | 2903    | 4889    | 3910                 | 3257    |
| <b>5%</b>     | 3819    | 3058                                 | 2551    | 4176    | 3345                           | 2790    | 4609    | 3690                 | 3078    |
| <b>6%</b>     | 3650    | 2926                                 | 2443    | 3991    | 3200                           | 2672    | 4328    | 3471                 | 2899    |

Index was trading at 3693 on 9/23/22. Shaded cells are higher than 3693

![](_page_285_Picture_4.jpeg)

# THE DARK SIDE OF VALUATION

Anyone can value a company that is stable, makes money and has an established business model!

# THE FUNDAMENTAL DETERMINANTS OF VALUE...

![](_page_286_Diagram_81.jpeg)

# THE DARK SIDE OF VALUATION...

- ▪ Valuing stable, money making companies with consistent and clear accounting statements, a long and stable history and lots of comparable firms is easy to do.
- ▪ The true test of your valuation skills is when you have to value “difficult” companies. In particular, the challenges are greatest when valuing:
  - ▪ **Young companies**, early in the life cycle, in young businesses
  - ▪ Companies that **don’t fit the accounting mold**
  - ▪ Companies that **face substantial truncation risk** (default or nationalization risk)

# DIFFICULT TO VALUE COMPANIES...

- ▪ Across the life cycle:
  - ▪ **Young, growth firms:** Limited history, small revenues in conjunction with big operating losses and a propensity for failure make these companies tough to value.
  - ▪ **Mature companies in transition:** When mature companies change or are forced to change, history may have to be abandoned and parameters have to be reestimated.
  - ▪ Declining and Distressed firms: A long but irrelevant history, declining markets, high debt loads and the likelihood of distress make them troublesome.
- ▪ Across markets
  - ▪ **Emerging market companies** are often difficult to value because of the way they are structured, their exposure to country risk and poor corporate governance.
- ▪ Across sectors
  - ▪ **Financial service firms:** Opacity of financial statements and difficulties in estimating basic inputs leave us trusting managers to tell us what's going on.
  - ▪ **Commodity and cyclical firms:** Dependence of the underlying commodity prices or overall economic growth make these valuations susceptible to macro factors.
  - ▪ **Firms with intangible assets:** Accounting principles are left to the wayside on these firms.

# I. THE CHALLENGE WITH YOUNG COMPANIES...

*Making judgments on revenues/ profits difficult because you cannot draw on history. If you have no product/ service, it is difficult to gauge market potential or profitability. The company's entire value lies in future growth but you have little to base your estimate on.*

*Cash flows from existing assets non-existent or negative.*

What is the value added by growth assets?

What are the cashflows from existing assets?

*Different claims on cash flows can affect value of equity at each stage.*

What is the value of equity in the firm?

How risky are the cash flows from both existing assets and growth assets?

*Limited historical data on earnings, and no market prices for securities makes it difficult to assess risk.*

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Will the firm will make it through the gauntlet of market demand and competition. Even if it does, assessing when it will become mature is difficult because there is so little to go on.*

# UPPING THE ANTE.. YOUNG COMPANIES IN YOUNG BUSINESSES...

- ▪ When valuing a business, we generally draw on three sources of information
  - ▪ The firm's **current financial statements**
    - ▪ How much did the firm sell?
    - ▪ How much did it earn?
  - ▪ The firm's **financial history**, usually summarized in its financial statements.
    - ▪ How fast have the firm's revenues and earnings grown over time?
    - ▪ What can we learn about cost structure and profitability from these trends?
    - ▪ Susceptibility to macro-economic factors (recessions and cyclical firms)
  - ▪ The industry and **peer group firms**
    - ▪ What happens to firms as they mature?
- ▪ It is when valuing these companies that you find yourself tempted by the dark side, where
  - ▪ “Paradigm shifts” happen...
  - ▪ New metrics are invented ...
  - ▪ The story dominates and the numbers lag...

![](_page_291_Diagram_21.jpeg)

# LESSON 1: DON'T SWEAT THE SMALL STUFF

![](_page_292_Figure_59.jpeg)

- ■ Spotlight the business the company is in & use the beta of that business.
- ■ Don't try to incorporate failure risk into the discount rate.
- ■ Let the cost of capital change over time, as the company changes.
- ■ If you are desperate, use the cross section of costs of capital to get your estimation going (use the 90th or 95th percentile across all companies).

# LESSON 2: WORK BACKWARDS AND KEEP IT SIMPLE...

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

# LESSON 3: SCALING UP IS HARD TO DO & FAILURE IS COMMON

Typically, the revenue growth rate of a newly public company outpaces its industry average for only about five years.

![](_page_294_Figure_55.jpeg)

Source: Andrew Metrick

The New York Times

- ▪ Lower revenue growth rates, as revenues scale up.
- ▪ Keep track of dollar revenues, as you go through time, measuring against market size.
- ▪ If you set your growth period to be much longer than ten years, you are already building in the expectation that your firm is an exceptional firm.

# LESSON 4: DON'T FORGET TO PAY FOR GROWTH...

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

# LESSON 5: THE DILUTION IS TAKEN CARE OFF.

- ■ With young growth companies, it is almost a given that **the number of shares outstanding will increase over time** for two reasons:
  - ■ To grow, the company will have to **issue new shares** either to raise cash to take projects or to offer to target company stockholders in acquisitions
  - ■ Many young, growth companies **also offer options to managers as compensation and these options will get exercised**, if the company is successful.
- ■ Both effects are **already incorporated into the value per share**, even though we use the current number of shares in estimating value per share
  - ■ The **need for new equity issues is captured in negative cash flows in the earlier years**. The present value of these negative cash flows will drag down the current value of equity and this is the effect of future dilution. In the Amazon valuation, the value of equity is reduced by \$3.09 billion (the present value of negative FCFF in the first 6 years), about a 16% reduction. That takes care of new issues in the future.
  - ■ The **existing options are valued and netted out against the current value**, taking care of the option overhang. The future earnings are after stock based compensation expenses (don't fall for the "its not a cash expense" ploy) to take care of future option grants.

# LESSON 6: IF YOU ARE WORRIED ABOUT FAILURE, INCORPORATE INTO VALUE

Figure 2.7: Failure Rate by Sector (2006 Cohort of US start-ups)

![](_page_297_Figure_11.jpeg)

# LESSON 7: THERE ARE ALWAYS SCENARIOS WHERE THE MARKET PRICE CAN BE JUSTIFIED...

|     | 6%        | 8%       | 10%       | 12%       | 14%       |
|-----|-----------|----------|-----------|-----------|-----------|
| 30% | \$ (1.94) | \$ 2.95  | \$ 7.84   | \$ 12.71  | \$ 17.57  |
| 35% | \$ 1.41   | \$ 8.37  | \$ 15.33  | \$ 22.27  | \$ 29.21  |
| 40% | \$ 6.10   | \$ 15.93 | \$ 25.74  | \$ 35.54  | \$ 45.34  |
| 45% | \$ 12.59  | \$ 26.34 | \$ 40.05  | \$ 53.77  | \$ 67.48  |
| 50% | \$ 21.47  | \$ 40.50 | \$ 59.52  | \$ 78.53  | \$ 97.54  |
| 55% | \$ 33.47  | \$ 59.60 | \$ 85.72  | \$ 111.84 | \$ 137.95 |
| 60% | \$ 49.53  | \$ 85.10 | \$ 120.66 | \$ 156.22 | \$ 191.77 |

# **LESSON 8: YOU WILL BE WRONG 100% OF THE TIME AND IT REALLY IS NOT YOUR FAULT...**

- ▪ No matter how careful you are in getting your inputs and how well structured your model is, **your estimate of value will change** both as new information comes out about the company, the business and the economy.
- ▪ As **information comes out**, you will have to adjust and adapt your model to reflect the information. Rather than be defensive about the resulting changes in value, recognize that this is the essence of risk.
- ▪ A test: **If your valuations are unbiased, you should find yourself increasing estimated values as often as you are decreasing values. In other words, there should be equal doses of good and bad news affecting valuations (at least over time).**

# AND THE MARKET IS OFTEN “MORE WRONG” ....

Amazon: Value and Price

![](_page_300_Figure_63.jpeg)

# ASSESSING MY 2000 FORECASTS, IN 2014

| Year       | Revenues                  |               | Operating Income          |               | Operating Margin          |               |
|------------|---------------------------|---------------|---------------------------|---------------|---------------------------|---------------|
|            | <i>My forecast (2000)</i> | <i>Actual</i> | <i>My forecast (2000)</i> | <i>Actual</i> | <i>My forecast (2000)</i> | <i>Actual</i> |
| 2000       | \$2,793                   | \$2,762       | -\$ 373                   | -\$ 664.00    | -13.35%                   | -24.04%       |
| 2001       | \$5,585                   | \$3,122       | -\$ 94                    | -\$ 231.00    | -1.68%                    | -7.40%        |
| 2002       | \$9,774                   | \$3,932       | \$ 407                    | \$ 106.00     | 4.16%                     | 2.70%         |
| 2003       | \$14,661                  | \$5,264       | \$ 1,038                  | \$ 271.00     | 7.08%                     | 5.15%         |
| 2004       | \$19,059                  | \$6,921       | \$ 1,628                  | \$ 440.00     | 8.54%                     | 6.36%         |
| 2005       | \$23,862                  | \$8,490       | \$ 2,212                  | \$ 432.00     | 9.27%                     | 5.09%         |
| 2006       | \$28,729                  | \$10,711      | \$ 2,768                  | \$ 389.00     | 9.63%                     | 3.63%         |
| 2007       | \$33,211                  | \$14,835      | \$ 3,261                  | \$ 655.00     | 9.82%                     | 4.42%         |
| 2008       | \$36,798                  | \$19,166      | \$ 3,646                  | \$ 842.00     | 9.91%                     | 4.39%         |
| 2009       | \$39,006                  | \$24,509      | \$ 3,883                  | \$ 1,129.00   | 9.95%                     | 4.61%         |
| 2010       | \$41,346                  | \$34,204      | \$ 4,135                  | \$ 1,406.00   | 10.00%                    | 4.11%         |
| 2011       | \$43,827                  | \$48,077      | \$ 4,383                  | \$ 862.00     | 10.00%                    | 1.79%         |
| 2012       | \$46,457                  | \$61,093      | \$ 4,646                  | \$ 676.00     | 10.00%                    | 1.11%         |
| 2013       | \$49,244                  | \$74,452      | \$ 4,925                  | \$ 745.00     | 10.00%                    | 1.00%         |
| 2014 (LTM) | \$51,460                  | \$85,247      | \$ 5,146.35               | \$ 97.00      | 10.00%                    | 0.11%         |

| Amazon                                                                                                                                                                                                                                                                                                                                                                                                                                              |                | Feb-22           |                |              |                                   |                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------|----------------|--------------|-----------------------------------|--------------------------------------------------------------------------|
| <i>The Disruption Platform Rolls on</i>                                                                                                                                                                                                                                                                                                                                                                                                             |                |                  |                |              |                                   |                                                                          |
| Amazon continues on its transformation from online retailer to disruption platform, willing to enter any business that it perceives as inefficiently run, and changing it. Along the way, it will invest large amounts of capital and wait for long periods to attain profitability. In 2020 and 2021, Amazon benefited from the COVID shut down to increase growth and improve its profitability, making its dominant position even more dominant. |                |                  |                |              |                                   |                                                                          |
| <i>The Assumptions</i>                                                                                                                                                                                                                                                                                                                                                                                                                              |                |                  |                |              |                                   |                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Base year      | Next year        | Years 2-5      | Years 6-10   | After year 10                     | Link to story                                                            |
| Revenues (a)                                                                                                                                                                                                                                                                                                                                                                                                                                        | \$469,822.00   | 15.0%            | 15.00%         | 3.00%        | 3.00%                             | Disruption platform in multiple businesses                               |
| Operating margin (b)                                                                                                                                                                                                                                                                                                                                                                                                                                | 9.60%          | 10.0%            | 10.00%         | 12.50%       | 12.50%                            | Margins improve, aided by cloud business & continued economies of scale. |
| Tax rate                                                                                                                                                                                                                                                                                                                                                                                                                                            | 12.60%         |                  | 12.60%         | 25.00%       | 25.00%                            | Global/US marginal tax rate over time                                    |
| Reinvestment (c )                                                                                                                                                                                                                                                                                                                                                                                                                                   |                | 1.69             | 1.69           | 1.69         | 25.00%                            | Maintined at Amazon's current level                                      |
| Return on capital                                                                                                                                                                                                                                                                                                                                                                                                                                   | 14.17%         | Marginal ROIC =  | 23.66%         |              | 12.00%                            | Stronge competitive edges                                                |
| Cost of capital (d)                                                                                                                                                                                                                                                                                                                                                                                                                                 |                |                  | 6.74%          | 6.11%        | 6.11%                             | Cost of capital close to median company                                  |
| <i>The Cash Flows</i>                                                                                                                                                                                                                                                                                                                                                                                                                               |                |                  |                |              |                                   |                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Revenues       | Operating Margin | EBIT           | EBIT (1-t)   | Reinvestment                      | FCFF                                                                     |
| 1                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$540,295.30   | 10.00%           | \$54,029.53    | \$47,221.81  | \$41,723.60                       | \$5,498.21                                                               |
| 2                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$621,339.60   | 10.50%           | \$65,240.66    | \$57,020.33  | \$47,982.14                       | \$9,038.19                                                               |
| 3                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$714,540.53   | 10.75%           | \$76,813.11    | \$67,134.66  | \$55,179.46                       | \$11,955.19                                                              |
| 4                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$821,721.61   | 11.00%           | \$90,389.38    | \$79,000.32  | \$63,456.38                       | \$15,543.94                                                              |
| 5                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$944,979.86   | 11.25%           | \$106,310.23   | \$92,915.14  | \$72,974.84                       | \$19,940.31                                                              |
| 6                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$1,064,047.32 | 11.34%           | \$120,655.80   | \$102,460.90 | \$70,493.69                       | \$31,967.21                                                              |
| 7                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$1,172,580.14 | 11.63%           | \$136,365.15   | \$112,419.43 | \$64,256.68                       | \$48,162.75                                                              |
| 8                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$1,264,041.40 | 11.92%           | \$150,669.48   | \$120,475.31 | \$54,149.48                       | \$66,325.83                                                              |
| 9                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \$1,332,299.63 | 12.21%           | \$162,671.54   | \$126,037.91 | \$40,412.17                       | \$85,625.74                                                              |
| 10                                                                                                                                                                                                                                                                                                                                                                                                                                                  | \$1,372,268.62 | 12.50%           | \$171,533.58   | \$128,650.18 | \$23,663.57                       | \$104,986.61                                                             |
| Terminal year                                                                                                                                                                                                                                                                                                                                                                                                                                       | \$1,413,436.68 | 12.50%           | \$176,679.58   | \$132,509.69 | \$33,127.42                       | \$99,382.27                                                              |
| <i>The Value</i>                                                                                                                                                                                                                                                                                                                                                                                                                                    |                |                  |                |              |                                   |                                                                          |
| Terminal value                                                                                                                                                                                                                                                                                                                                                                                                                                      |                |                  | \$3,195,571.27 |              |                                   |                                                                          |
| PV(Terminal value)                                                                                                                                                                                                                                                                                                                                                                                                                                  |                |                  | \$1,694,040.21 |              |                                   |                                                                          |
| PV (CF over next 10 years)                                                                                                                                                                                                                                                                                                                                                                                                                          |                |                  | \$244,983.86   |              |                                   |                                                                          |
| Value of operating assets =                                                                                                                                                                                                                                                                                                                                                                                                                         |                |                  | \$1,939,024.07 |              |                                   |                                                                          |
| Adjustment for distress                                                                                                                                                                                                                                                                                                                                                                                                                             |                | \$0.00           |                |              | Probability of failure = 0.00%    |                                                                          |
| - Debt & Minority Interests                                                                                                                                                                                                                                                                                                                                                                                                                         |                |                  | \$139,439.00   |              |                                   |                                                                          |
| + Cash & Other Non-operating assets                                                                                                                                                                                                                                                                                                                                                                                                                 |                |                  | \$96,049.00    |              |                                   |                                                                          |
| Value of equity                                                                                                                                                                                                                                                                                                                                                                                                                                     |                |                  | \$1,895,634.07 |              |                                   |                                                                          |
| - Value of equity options                                                                                                                                                                                                                                                                                                                                                                                                                           |                |                  | \$0.00         |              |                                   |                                                                          |
| Number of shares                                                                                                                                                                                                                                                                                                                                                                                                                                    |                |                  | 506.00         |              |                                   |                                                                          |
| Value per share                                                                                                                                                                                                                                                                                                                                                                                                                                     |                | \$3,746.31       |                |              | Stock was trading at = \$3,068.57 |                                                                          |

Aswath Damodaran **303**

## II. MATURE COMPANIES IN TRANSITION..

- ▪ Mature companies are **generally the easiest group to value**. They have long, established histories that can be mined for inputs. They have investment policies that are set and capital structures that are stable, thus making valuation more grounded in past data.
- ▪ However, **this stability in the numbers can mask real problems at the company**. The company may be set in a process, where it invests more or less than it should and does not have the right financing mix. In effect, the policies are consistent, stable and bad.
- ▪ If you **expect these companies to change** or as is more often the case to have change thrust upon them, you will have to revalue the firm, with the changes built in.

# THE PERILS OF VALUING MATURE COMPANIES...

*Lots of historical data on earnings and cashflows. Key questions remain if these numbers are volatile over time or if the existing assets are not being efficiently utilized.*

*Growth is usually not very high, but firms may still be generating healthy returns on investments, relative to cost of funding. Questions include how long they can generate these excess returns and with what growth rate in operations. Restructuring can change both inputs dramatically and some firms maintain high growth through acquisitions.*

*What are the cashflows from existing assets?*

*Equity claims can vary in voting rights and dividends.*

*What is the value of equity in the firm?*

*What is the value added by growth assets?*

*How risky are the cash flows from both existing assets and growth assets?*

*Operating risk should be stable, but the firm can change its financial leverage. This can affect both the cost of equity and capital.*

*When will the firm become a mature fiirm, and what are the potential roadblocks?*

*Maintaining excess returns or high growth for any length of time is difficult to do for a mature firm.*

### *Hormel Foods: The Value of Control Changing*

Hormel Foods sells packaged meat and other food products and has been in existence as a publicly traded company for almost 80 years.

In 2008, the firm reported after-tax operating income of \$315 million, reflecting a compounded growth of 5% over the previous 5 years.

### *The Status Quo*

Run by existing management, with conservative reinvestment policies (reinvestment rate = 14.34% and debt ratio = 10.4%.

### *New and better management*

More aggressive reinvestment which increases the reinvestment rate (to 40%) and tlength of growth (to 5 years), and higher debt ratio (20%).

### **Operating Restructuring** 1

Expected growth rate = ROC \* Reinvestment Rate

Expected growth rae (status quo) = 14.34% \* 19.14% = 2.75%

Expected growth rate (optimal) = 14.00% \* 40% = 5.60%

ROC drops, reinvestment rises and growth goes up.

### **Financial restructuring** 2

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

4

| Year                            | Operating income after taxes | Expected growth rate | ROC    | Reinvestment Rate | Reinvestment | FCFF    | Cost of capital | Present Value |
|---------------------------------|------------------------------|----------------------|--------|-------------------|--------------|---------|-----------------|---------------|
| Trailing 12 months              | \$315                        |                      |        |                   |              |         |                 |               |
| 1                               | \$333                        | 5.60%                | 14.00% | 40.00%            | \$133        | \$200   | 6.63%           | \$187         |
| 2                               | \$351                        | 5.60%                | 14.00% | 40.00%            | \$141        | \$211   | 6.63%           | \$185         |
| 3                               | \$371                        | 5.60%                | 14.00% | 40.00%            | \$148        | \$223   | 6.63%           | \$184         |
| 4                               | \$392                        | 5.60%                | 14.00% | 40.00%            | \$260        | \$235   | 6.63%           | \$182         |
| 5                               | \$414                        | 5.60%                | 14.00% | 40.00%            | \$223        | \$248   | 6.63%           | \$180         |
| Beyond                          | \$423                        | 2.35%                | 6.74%  | 34.87%            | \$148        | \$6,282 | 6.74%           | \$4,557       |
| Value of operating assets       |                              |                      |        |                   |              |         |                 | \$5,475       |
| (Add) Cash                      |                              |                      |        |                   |              |         |                 | \$155         |
| (Subtract) Debt                 |                              |                      |        |                   |              |         |                 | \$491         |
| (Subtract) Management Options   |                              |                      |        |                   |              |         |                 | \$53          |
| Value of equity in common stock |                              |                      |        |                   |              |         |                 | \$5,085       |
| Value per Asset                 |                              |                      |        |                   |              |         |                 | \$37.80       |

# FINANCIAL LEVERAGE IS A DOUBLE-EDGED SWORD..

Exhibit 7.1: Optimal Financing Mix: Hormel Foods in January 2009

![](_page_306_Figure_90.jpeg)

# III. DEALING WITH DECLINE AND DISTRESS...

*Historial data often reflects flat or declining revenues and falling margins. Investments often earn less than the cost of capital.*

*Growth can be negative, as firm sheds assets and shrinks. As less profitable assets are shed, the firm's remaining assets may improve in quality.*

What is the value added by growth assets?

What are the cashflows from existing assets?

*Underfunded pension obligations and litigation claims can lower value of equity. Liquidation preferences can affect value of equity*

What is the value of equity in the firm?

How risky are the cash flows from both existing assets and growth assets?

*Depending upon the risk of the assets being divested and the use of the proceeds from the divesture (to pay dividends or retire debt), the risk in both the firm and its equity can change.*

When will the firm become a mature fiirm, and what are the potential roadblocks?

*There is a real chance, especially with high financial leverage, that the firm will not make it. If it is expected to survive as a going concern, it will be as a much smaller entity.*

# A. DEALING WITH DECLINE

- ▪ **In decline, firms often see declining revenues and lower margins**, translating in negative expected growth over time.
  - ▪ If these firms are **run by good managers**, they will not fight decline. Instead, they will adapt to it and shut down or sell investments that do not generate the cost of capital. This can translate into negative net capital expenditures (depreciation exceeds cap ex), declining working capital and an overall negative reinvestment rate. The best case scenario is that the firm can shed its bad assets, make itself a much smaller and healthier firm and then settle into long-term stable growth.
  - ▪ As an investor, your worst case scenario is that these firms **are run by managers in denial** who continue to expand the firm by making bad investments (that generate lower returns than the cost of capital). These firms may be able to grow revenues and operating income but will destroy value along the way.

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
| Value per share                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |            | \$3.23           |            |            | Stock was trading at =   | \$8.79                                                                   |

## B. DEALING WITH THE “DOWNSIDE” OF DISTRESS

- ▪ **A DCF valuation values a firm as a going concern.** If there is a significant likelihood of the firm failing before it reaches stable growth and if the assets will then be sold for a value less than the present value of the expected cashflows (a distress sale value), DCF valuations will overstate the value of the firm.

$$\text{Value of Equity} = \text{DCF value of equity (1 - \text{Probability of distress}) + \text{Distress sale value of equity (Probability of distress)}$$

- ▪ There are three ways in which we can estimate the probability of distress:
  - ▪ **Use the bond rating** to estimate the cumulative probability of distress  
    Estimate the probability of distress **with a probit**
  - ▪ Estimate the probability of distress by **looking at market value of bonds..**
- ▪ The **distress sale value of equity** is usually best estimated as a percent of book value (and this value will be lower if the economy is doing badly and there are other firms in the same business also in distress).

![](_page_311_Diagram_0.jpeg)

# ADJUSTING THE VALUE OF LVS FOR DISTRESS..

- ▪ Ratings based approach: In February 2009, Las Vegas Sands was rated B+, and based upon history (previous ten years), the **likelihood of default is 28.25%**.
- ▪ Bond Price based: In February 2009, LVS was rated B+ by S&P. Historically, 28.25% of B+ rated bonds default within 10 years. LVS has a 6.375% bond, maturing in February 2015 (7 years), trading at \$529. If we discount the expected cash flows on the bond at the riskfree rate, we can back out the probability of distress from the bond price:

$$529 = \sum_{t=1}^{t=7} \frac{63.75(1 - \Pi_{\text{Distress}})^t}{(1.03)^t} + \frac{1000(1 - \Pi_{\text{Distress}})^7}{(1.03)^7}$$

$$\pi_{\text{Distress}} = \text{Annual probability of default} = 13.54\%$$

$$\text{Cumulative probability of surviving 10 years} = (1 - .1354)^{10} = 23.34\%$$

$$\text{Cumulative probability of distress over 10 years} = 1 - .2334 = .7666 \text{ or } 76.66\%$$

- ▪ If LVS is becomes distressed:
  - ▪ Expected distress sale proceeds = \$2,769 million < Face value of debt
  - ▪ Expected equity value/share = \$0.00
- ▪ Expected value per share
  - ▪ With ratings-based approach:  $\$8.12 (.7175) + \$0 (.2825) = \$5.83$
  - ▪ With bond-based approach:  $\$8.12 (1 - .7666) + \$0.00 (.7666) = \$1.92$

# IV. EMERGING MARKET COMPANIES

## Estimation Issues - Emerging Market Companies

Big shifts in economic environment (inflation, itinerest rates) can affect operating earnings history. Poor corporate governance and weak accounting standards can lead to lack of transparency on earnings.

Growth rates for a company will be affected heavily by growth rate and political developments in the country in which it operates.

What is the value added by growth assets?

What are the cashflows from existing assets?

Cross holdings can affect value of equity

What is the value of equity in the firm?

How risky are the cash flows from both existing assets and growth assets?

Even if the company's risk is stable, there can be significant changes in country risk over time.

When will the firm become a mature fiirm, and what are the potential roadblocks?

Economic crises can put many companies at risk. Government actions (nationalization) can affect long term value.

# **LESSON 1: COUNTRY RISK HAS TO BE INCORPORATED... BUT WITH A SCALPEL, NOT A BLUDGEON**

- ■ Emerging market companies are undoubtedly exposed to additional country risk because they are incorporated in countries that are more exposed to political and economic risk.
- ■ Not all emerging market companies are equally exposed to country risk and many developed markets have emerging market risk exposure because of their operations.
- ■ You can use either the “weighted country risk premium”, with the weights reflecting the countries you get your revenues from or the lambda approach (which may incorporate more than revenues) to capture country risk exposure.

# LESSON 2: CURRENCY SHOULD NOT MATTER

- ▪ You can value any company in any currency. Thus, you can value a Brazilian company in nominal reals, US dollars or Swiss Francs.
- ▪ For your valuation to stay invariant and consistent, your cash flows and discount rates have to be in the same currency. Thus, if you are using a high inflation currency, both your growth rates and discount rates will be much higher.
- ▪ For your cash flows to be consistent, you have to use expected exchange rates that reflect purchasing power parity (the higher inflation currency has to depreciate by the inflation differential each year).

# VALUING INFOSYS: IN US\$ AND INDIAN RUPEES

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

# LESSON 3: THE “CORPORATE GOVERNANCE” DRAG

- ■ Stockholders in Asian, Latin American and many European companies have little or no power over the managers of the firm. In many cases, insiders own voting shares and control the firm and the potential for conflict of interests is huge.
- ■ This weak corporate governance is often a reason for given for using higher discount rates or discounting the estimated value for these companies.
- ■ Would you discount the value that you estimate for an emerging market company to allow for this absence of stockholder power?
- ■ Yes
- ■ No.

![](_page_318_Diagram_1.jpeg)

**discount in this** 

# LESSON 4: WATCH OUT FOR CROSS HOLDINGS...

- ▪ Emerging market companies are more prone to having cross holdings than companies in developed markets.
  - ▪ This is partially the result of history (since many of the larger public companies used to be family owned businesses until a few decades ago)
  - ▪ And partly because those who run these companies value control (and use cross holdings to preserve this control).
- ▪ In many emerging market companies, the real process of valuation begins when you have finished your DCF valuation, since the cross holdings (which can be numerous) have to be valued, often with minimal information.

# TATA COMPANIES IN 2010: VALUE BREAKDOWN

![](_page_320_Figure_78.jpeg)

# LESSON 5: TRUNCATION RISK CAN COME IN MANY FORMS...

- ▪ Natural disasters: Small companies in some economies are much exposed to natural disasters (hurricanes, earthquakes), without the means to hedge against that risk (with insurance or derivative products).
- ▪ Terrorism risk: Companies in some countries that are unstable or in the grips of civil war are exposed to damage or destruction.
- ▪ Nationalization risk: While less common than it used to be, there are countries where businesses may be nationalized, with owners receiving less than fair value as compensation.

# VALUING ARAMCO: POTENTIAL DIVIDENDS

A Potential Dividend (FCFE) Discount Model Valuation of Aramco

![](_page_322_Diagram_11.jpeg)

# ADJUSTING FOR REGIME CHANGE

- If you believe that there is no chance of regime change, your expected value will remain \$1.65 trillion.
- If you believe that regime change is imminent, and that your equity will be fully expropriated, your expected value will be zero.
- If you believe that there remains a non-trivial chance (perhaps as high as 20%) that there will be a regime change and that if there is one, there will be changes that reduce, but not extinguish, your equity claim:

$$\begin{aligned}
 & \text{House of Saud rules} \\
 & = \frac{\text{Value of equity =} \\
 & \quad \text{DCF Value of Aramco Equity =} \\
 & \quad \$1.65 \text{ trillion}}{\text{X}} + \frac{\text{DCF with higher royalties \& taxes =} \\
 & \quad \$0.825 \text{ trillion}}{\text{Probability of political status quo} \\
 & \quad 80\%}{\text{Probability of regime change} \\
 & \quad 20\%}
 \end{aligned}$$

# V. VALUING FINANCIAL SERVICE COMPANIES

*Existing assets are usually financial assets or loans, often marked to market. Earnings do not provide much information on underlying risk.*

*Defining capital expenditures and working capital is a challenge. Growth can be strongly influenced by regulatory limits and constraints. Both the amount of new investments and the returns on these investments can change with regulatory changes.*

What is the value added by growth assets?

What are the cashflows from existing assets?

*Preferred stock is a significant source of capital.*

What is the value of equity in the firm?

How risky are the cash flows from both existing assets and growth assets?

*For financial service firms, debt is raw material rather than a source of capital. It is not only tough to define but if defined broadly can result in high financial leverage, magnifying the impact of small operating risk changes on equity risk.*

When will the firm become a mature fiirm, and what are the potential roadblocks?

*In addition to all the normal constraints, financial service firms also have to worry about maintaining capital ratios that are acceptable of regulators. If they do not, they can be taken over and shut down.*

# CIB Egypt in December 2015 Valuation in Egyptian Pounds

![](_page_325_Diagram_23.jpeg)

# LESSON 1: FINANCIAL SERVICE COMPANIES ARE OPAQUE...

- ■ With financial service firms, we enter into a Faustian bargain. They tell us very little about the quality of their assets (loans, for a bank, for instance are not broken down by default risk status) but we accept that in return for assets being marked to market (by accountants who presumably have access to the information that we don't have).
- ■ In addition, estimating cash flows for a financial service firm is difficult to do. So, we trust financial service firms to pay out their cash flows as dividends. Hence, the use of the dividend discount model.
- ■ During times of crises or when you don't trust banks to pay out what they can afford to in dividends, using the dividend discount model may not give you a "reliable" value.

# LESSON 2: FOR FINANCIAL SERVICE COMPANIES, BOOK VALUE MATTERS...

- ■ The book value of assets and equity is mostly irrelevant when valuing non-financial service companies. After all, the book value of equity is a historical figure and can be nonsensical. (The book value of equity can be negative and is so for more than a 1000 publicly traded US companies)
- ■ With financial service firms, book value of equity is relevant for two reasons:
  - ■ Since financial service firms mark to market, the book value is more likely to reflect what the firms own right now (rather than a historical value)
  - ■ The regulatory capital ratios are based on book equity. Thus, a bank with negative or even low book equity will be shut down by the regulators.
- ■ From a valuation perspective, it therefore makes sense to pay heed to book value. In fact, you can argue that reinvestment for a bank is the amount that it needs to add to book equity to sustain its growth ambitions and safety requirements:
  - ■  $\text{FCFE} = \text{Net Income} - \text{Reinvestment in regulatory capital (book equity)}$

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

# **LESSON 3: NOT ALL FINANCIAL SERVICE FIRMS ARE BUILT ALIKE..**

- ▪ Financial service is a broad category, and while banks may be its most substantive component, there are a range of other companies, with very different business models.
- ▪ For instance, payment processing companies and credit card companies are also financial service companies, but they derive their value from
  - ▪ Getting consumers to use their platforms to make payments to businesses or to each other, resulting in transactions on the platform (called Gross Merchandising Value or GMV)
  - ▪ Keeping a slice, called a take rate, of the GMV for themselves.

|                                                                                                                                                                                                                                                         |              | Paytm           |                  | Sep-21                                                                                     |                                |                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|------------------|--------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------|
| The Story                                                                                                                                                                                                                                               |              |                 |                  |                                                                                            |                                |                                                                |
| Paytm will continue its dominance of the Indian mobile payment market, while that market continues to grow. Along the way, its management will focus more on converting transactions on its platform into revenues, and revenues into operating income. |              |                 |                  |                                                                                            |                                |                                                                |
| The Assumptions                                                                                                                                                                                                                                         |              |                 |                  |                                                                                            |                                |                                                                |
|                                                                                                                                                                                                                                                         | Base year    | Next year       | Years 2-5        | Years 6-10                                                                                 | After year 10                  | Link to story                                                  |
| GMV                                                                                                                                                                                                                                                     | ₹ 4,033,000  | 40.00%          | 40.00%           | 4.19%                                                                                      | 4.19%                          | Growing mobile payment market                                  |
| Revenue as % of GMV                                                                                                                                                                                                                                     | 0.79%        | 0.83%           | 1.00%            | 2.00%                                                                                      | 2.00%                          | Take rate improves, as company matures                         |
| Operating margin (b)                                                                                                                                                                                                                                    | -49.00%      | -20.0%          | 5.00%            | 30.00%                                                                                     | 30.00%                         | High-margin intermediary business                              |
| Tax rate                                                                                                                                                                                                                                                | 25.00%       |                 | 25.00%           | 25.00%                                                                                     | 25.00%                         | Converge on statutory tax rate                                 |
| Reinvestment (c)                                                                                                                                                                                                                                        |              | 3.00            | 2.45             | 2.45                                                                                       | 27.93%                         | Industry average reinvestment, for capital intensive business. |
| Return on capital                                                                                                                                                                                                                                       | -21.78%      | Marginal ROIC = | 80.13%           |                                                                                            | 15.00%                         | Competitive advantages fade over time.                         |
| Cost of capital (d)                                                                                                                                                                                                                                     |              |                 | 10.44%           | 8.91%                                                                                      | 8.91%                          | Cost of capital relatively stable.                             |
| The Cash Flows                                                                                                                                                                                                                                          |              |                 |                  |                                                                                            |                                |                                                                |
|                                                                                                                                                                                                                                                         | GMV          | Revenues        | Operating Margin | EBIT (1-t)                                                                                 | Reinvestment                   | FCFF                                                           |
| 1                                                                                                                                                                                                                                                       | ₹ 5,646,200  | ₹ 46,984.56     | -20.00%          | ₹ -9,396.91                                                                                | ₹ 5,038.85                     | -14,435.77                                                     |
| 2                                                                                                                                                                                                                                                       | ₹ 7,904,680  | ₹ 69,095.49     | -10.00%          | ₹ -6,909.55                                                                                | ₹ 9,024.87                     | -15,934.42                                                     |
| 3                                                                                                                                                                                                                                                       | ₹ 11,066,552 | ₹ 101,377.63    | -5.00%           | ₹ -5,068.88                                                                                | ₹ 13,176.38                    | -18,245.27                                                     |
| 4                                                                                                                                                                                                                                                       | ₹ 15,493,173 | ₹ 148,430.20    | 0.00%            | ₹ -0.00                                                                                    | ₹ 19,205.13                    | -19,205.13                                                     |
| 5                                                                                                                                                                                                                                                       | ₹ 21,690,442 | ₹ 216,904.42    | 5.00%            | ₹ 10,845.22                                                                                | ₹ 27,948.66                    | -17,103.44                                                     |
| 6                                                                                                                                                                                                                                                       | ₹ 28,813,149 | ₹ 345,757.79    | 10.00%           | ₹ 28,564.36                                                                                | ₹ 52,593.21                    | -24,028.85                                                     |
| 7                                                                                                                                                                                                                                                       | ₹ 36,211,213 | ₹ 506,956.99    | 15.00%           | ₹ 57,032.66                                                                                | ₹ 65,795.59                    | -8,762.93                                                      |
| 8                                                                                                                                                                                                                                                       | ₹ 42,915,357 | ₹ 686,645.72    | 20.00%           | ₹ 102,996.86                                                                               | ₹ 73,342.34                    | 29,654.52                                                      |
| 9                                                                                                                                                                                                                                                       | ₹ 47,787,109 | ₹ 860,167.96    | 25.00%           | ₹ 161,281.49                                                                               | ₹ 70,825.40                    | 90,456.09                                                      |
| 10                                                                                                                                                                                                                                                      | ₹ 49,789,389 | ₹ 995,787.77    | 30.00%           | ₹ 224,052.25                                                                               | ₹ 55,355.03                    | 168,697.22                                                     |
| Terminal year                                                                                                                                                                                                                                           | ₹ 51,875,564 | ₹ 1,037,511.28  | 30.00%           | ₹ 233,440.04                                                                               | ₹ 65,207.58                    | 168,232.45                                                     |
| The Value                                                                                                                                                                                                                                               |              |                 |                  |                                                                                            |                                |                                                                |
| Terminal value                                                                                                                                                                                                                                          |              |                 | ₹ 3,564,246.92   |                                                                                            |                                |                                                                |
| PV(Terminal value)                                                                                                                                                                                                                                      |              |                 | ₹ 1,377,090.74   |                                                                                            |                                |                                                                |
| PV (CF over next 10 years)                                                                                                                                                                                                                              |              |                 | ₹ 36,169.53      |                                                                                            |                                |                                                                |
| Value of operating assets =                                                                                                                                                                                                                             |              |                 | ₹ 1,413,260.27   |                                                                                            |                                |                                                                |
| Adjustment for distress                                                                                                                                                                                                                                 |              |                 | ₹ 35,331.51      |                                                                                            | Probability of failure = 5.00% |                                                                |
| - Debt & Minority Interests                                                                                                                                                                                                                             |              |                 | ₹ 12,006.00      |                                                                                            |                                |                                                                |
| + Cash & Other Non-operating assets                                                                                                                                                                                                                     |              |                 | ₹ 7,785.00       |                                                                                            |                                |                                                                |
| +IPO Proceeds                                                                                                                                                                                                                                           |              |                 | ₹ 83,000.00      | Total proceeds expected to be 166,000, but half will be cashing out existing stockholders. |                                |                                                                |
| Value of equity                                                                                                                                                                                                                                         |              |                 | ₹ 1,456,707.76   |                                                                                            |                                |                                                                |
| - Value of equity options                                                                                                                                                                                                                               |              |                 | ₹ 45,696.90      |                                                                                            |                                |                                                                |
| Number of shares                                                                                                                                                                                                                                        |              |                 | 644.23           |                                                                                            |                                |                                                                |
| Value per share                                                                                                                                                                                                                                         |              | ₹ 2,190.24      |                  | Stock was trading at =                                                                     | ₹ 2,950.00                     |                                                                |

# VI. VALUING COMPANIES WITH “INTANGIBLE” ASSETS

*If capital expenditures are miscategorized as operating expenses, it becomes very difficult to assess how much a firm is reinvesting for future growth and how well its investments are doing.*

What is the value added by growth assets?

What are the cashflows from existing assets?

*The capital expenditures associated with acquiring intangible assets (technology, human capital) are mis-categorized as operating expenses, leading to incorrect accounting earnings and measures of capital invested.*

How risky are the cash flows from both existing assets and growth assets?

*It can be more difficult to borrow against intangible assets than it is against tangible assets. The risk in operations can change depending upon how stable the intangible asset is.*

When will the firm become a mature fiirm, and what are the potential roadblocks?

*Intangible assets such as brand name and customer loyalty can last for very long periods or dissipate overnight.*

# LESSON 1: ACCOUNTING RULES ARE CLUTTERED WITH INCONSISTENCIES...

- ■ If we start with accounting first principles, capital expenditures are expenditures designed to create benefits over many periods. They should not be used to reduce operating income in the period that they are made, but should be depreciated/amortized over their life. They should show up as assets on the balance sheet.
- ■ Accounting is consistent in its treatment of cap ex with manufacturing firms, but is inconsistent with firms that do not fit the mold.
  - ■ With pharmaceutical and technology firms, R&D is the ultimate cap ex but is treated as an operating expense.
  - ■ With consulting firms and other firms dependent on human capital, recruiting and training expenses are your long term investments that are treated as operating expenses.
  - ■ With brand name consumer product companies, a portion of the advertising expense is to build up brand name and is the real capital expenditure. It is treated as an operating expense.

# LESSON 2: AND FIXING THOSE INCONSISTENCIES CAN ALTER YOUR VIEW OF A COMPANY AND AFFECT ITS VALUE

|                   | No R&D adjustment | R&D adjustment |
|-------------------|-------------------|----------------|
| EBIT              | \$5,071           | \$7,336        |
| Invested Capital  | \$25,277          | \$33,173       |
| ROIC              | 14.58%            | 18.26%         |
| Reinvestment Rate | 115.68%           | 106.98%        |
| Value of firm     | \$58,617          | \$95,497       |
| Value of equity   | \$50,346          | \$87,226       |
| Value/share       | \$42.73           | \$74.33        |

# LESSON 3: IN A DCE, INTANGIBLES ARE IN YOUR CASH FLOWS (OR RISK)..

![](_page_334_Diagram_9.jpeg)

# **MULTIPLE INTANGIBLES: VALUING BIRKENSTOCK'S MANY INTANGIBLES!**

1. 1. Brand Name: It is undeniable that Birkenstock not only has a brand name, in terms of recognition and visibility, but has the pricing power and operating margins to back up that brand name.
2. 2. Celebrity Customer Base: Birkenstock attracts celebrities in different age groups, from Gwyneth Paltrow & Heidi Klum to Paris Jackson & Kendall Jenner, and more impressively, it does so without paying them sponsorship fees. If the best advertising is unsolicited, Birkenstock clearly has mastered the game.
3. 3. Good Management: Birkenstock seems to have struck gold with Oliver Reichert. Not only has he steered the company towards high growth, but he has done so without upsetting the balance that lies behind its brand name.
4. 4. The Barbie Buzz: Margot Robbie's pink Birkenstock sandals in that movie, which has been the blockbuster hit of the year, hyper charged the demand for the company's footwear. It is true that buzzes fade, but not before they create a revenue bump and perhaps even increase the customer base for the long term.

**Birkenstock IPO ValuationSep-23**

| <b>Base Year and Comparison</b> |             | <b>Growth Story</b> |                                                                             | <b>Profitability Story</b>                            |             | <b>Growth Efficiency Story</b>                                      |                                                                                 | <b>Terminal Value</b> |             |             |             |             |               |             |
|---------------------------------|-------------|---------------------|-----------------------------------------------------------------------------|-------------------------------------------------------|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------|-----------------------|-------------|-------------|-------------|-------------|---------------|-------------|
| <b>Company</b>                  |             | <b>Big Apparel</b>  |                                                                             | Growth of 25% in year 1, followed by 15% in years 2-5 |             | Set to third quartile (2.62) of big brand apparel & footwear firms. |                                                                                 | Growth Rate           | 2.74%       |             |             |             |               |             |
| CAGR in Revenues (2013-22)      | 18.20%      | 8.66%               |                                                                             |                                                       |             |                                                                     |                                                                                 | Growth Rate           | 7.74%       |             |             |             |               |             |
| Revenue (LTM)                   | € 1,439,976 |                     |                                                                             |                                                       |             |                                                                     |                                                                                 | Cost of capital       | 7.74%       |             |             |             |               |             |
| Operating Margin (LTM)          | 22.31%      | 14.74%              |                                                                             |                                                       |             |                                                                     |                                                                                 | Return on capital     | 12.00%      |             |             |             |               |             |
| Operating Income                | € 321,230   |                     |                                                                             |                                                       |             |                                                                     |                                                                                 | Reinvestment Rate     | 22.83%      |             |             |             |               |             |
| EBIT (1-t)                      | € 224,861   |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             |               |             |
|                                 |             |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             |               |             |
| PV(Terminal value)              | € 6,087,285 |                     | 1                                                                           | 2                                                     | 3           | 4                                                                   | 5                                                                               | 6                     | 7           | 8           | 9           | 10          | Terminal year |             |
| PV (CF over next 10 years)      | € 2,862,595 |                     | Revenue Growth                                                              | 25.00%                                                | 15.00%      | 15.00%                                                              | 15.00%                                                                          | 12.55%                | 10.10%      | 7.64%       | 5.19%       | 2.74%       | 2.74%         |             |
| Probability of failure =        | 0.00%       |                     | Revenue                                                                     | € 1,799,970                                           | € 2,069,966 | € 2,380,460                                                         | € 2,737,529                                                                     | € 3,148,159           | € 3,543,190 | € 3,900,910 | € 4,199,096 | € 4,417,113 | € 4,538,142   | € 4,662,487 |
| Value of operating assets =     | € 8,949,880 |                     | Operating Margin                                                            | 23.00%                                                | 23.80%      | 24.20%                                                              | 24.60%                                                                          | 25.00%                | 25.00%      | 25.00%      | 25.00%      | 25.00%      | 25.00%        | 25.00%      |
| - Debt                          | € 1,874,002 |                     | Operating Income                                                            | € 413,993                                             | € 492,652   | € 576,071                                                           | € 673,432                                                                       | € 787,040             | € 885,797   | € 975,228   | € 1,049,774 | € 1,104,278 | € 1,134,535   | € 1,165,622 |
| - Minority interests            | € -         |                     | EBIT (1-t)                                                                  | € 289,795                                             | € 344,856   | € 403,250                                                           | € 471,403                                                                       | € 550,928             | € 620,058   | € 682,659   | € 734,842   | € 772,995   | € 794,175     | € 815,935   |
| + Cash                          | € 307,078   |                     | Reinvestment                                                                | € 103,052                                             | € 118,509   | € 136,286                                                           | € 156,729                                                                       | € 150,775             | € 136,535   | € 113,811   | € 83,213    | € 46,194    | € 47,460      | € 186,305   |
| + Non-operating assets          | € -         |                     | FCFF                                                                        | € 186,743                                             | € 226,347   | € 266,964                                                           | € 314,674                                                                       | € 400,153             | € 483,524   | € 568,848   | € 651,629   | € 726,801   | € 746,715     | € 629,630   |
| Value of equity                 | € 8,382,956 |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             | € 12,592,600  |             |
| - Value of options              | € -         |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             |               |             |
| Value of equity (common stock)  | € 8,382,956 |                     | Cost of Capital                                                             | 7.45%                                                 | 7.45%       | 7.45%                                                               | 7.45%                                                                           | 7.51%                 | 7.57%       | 7.63%       | 7.68%       | 7.74%       |               |             |
| Number of shares                | 202,853.00  |                     | Cumulated WACC                                                              | 0.9306                                                | 0.8661      | 0.8060                                                              | 0.7501                                                                          | 0.6980                | 0.6493      | 0.6036      | 0.5608      | 0.5208      | 0.4834        |             |
| Estimated value /share          | € 41.33     |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             |               |             |
|                                 |             |                     | Sales to Capital                                                            | 2.62                                                  | 2.62        | 2.62                                                                | 2.62                                                                            | 2.62                  | 2.62        | 2.62        | 2.62        | 2.62        |               |             |
| Price per share                 | € 46.50     |                     | ROIC                                                                        | 7.38%                                                 | 8.56%       | 9.73%                                                               | 11.01%                                                                          | 12.41%                | 13.51%      | 14.44%      | 15.18%      | 15.70%      | 15.98%        | 12.00%      |
| % Under or Over Valued          | 12.52%      |                     |                                                                             |                                                       |             |                                                                     |                                                                                 |                       |             |             |             |             |               |             |
|                                 |             |                     | <b>Risk Story</b>                                                           |                                                       |             |                                                                     | <b>Competitive Advantages</b>                                                   |                       |             |             |             |             |               |             |
|                                 |             |                     | Cost of capital reflecting business mix, geography & debt policy.           |                                                       |             |                                                                     | Competive advantages will persist.                                              |                       |             |             |             |             |               |             |
|                                 |             |                     | <b>Centering production in Germany</b> reduces supply chain & country risk. |                                                       |             |                                                                     | Intangibles collectively sustain a return on capital above the cost of capital. |                       |             |             |             |             |               |             |

# BIRKENSTOCK: INTANGIBLES IN VALUE

![](_page_337_Figure_6.jpeg)

# VII. VALUING CYCLICAL AND COMMODITY COMPANIES

*Company growth often comes from movements in the economic cycle, for cyclical firms, or commodity prices, for commodity companies.*

![](_page_338_Diagram_110.jpeg)

# **LESSON 1: WITH “MACRO” COMPANIES, IT IS EASY TO GET LOST IN “MACRO” ASSUMPTIONS...**

- ▪ With cyclical and commodity companies, it is undeniable that the value you arrive at will be affected by your views on the economy or the price of the commodity.
- ▪ Consequently, you will feel the urge to take a stand on these macro variables and build them into your valuation. Doing so, though, will create valuations that are jointly impacted by your views on macro variables and your views on the company, and it is difficult to separate the two.
- ▪ The best (though not easiest) thing to do is to separate your macro views from your micro views. Use current market based numbers for your valuation, but then provide a separate assessment of what you think about those market numbers.

# LESSON 2: USE PROBABILISTIC TOOLS TO ASSESS VALUE AS A FUNCTION OF MACRO VARIABLES...

- ■ If there is a key macro variable affecting the value of your company that you are uncertain about (and who is not), why not quantify the uncertainty in a distribution (rather than a single price) and use that distribution in your valuation.
- ■ That is exactly what you do in a Monte Carlo simulation, where you allow one or more variables to be distributions and compute a distribution of values for the company.
- ■ With a simulation, you get not only everything you would get in a standard valuation (an estimated value for your company) but you will get additional output (on the variation in that value and the likelihood that your firm is under or over valued)

### Shell: A "Oil Price" Neutral Valuation: March 2016

Revenue calculated from prevailing oil price of \$40/barrel in March 2016  
 Revenue =  $39992.77 + 4039.40 * \$40$   
 $= \$201,569$ 

Compounded revenue growth of 3.91% a year, based on  
 Shell's historical revenue growth rate from 2000 to 2015

|                           | Base Year     | 1            | 2            | 3            | 4            | 5             | Terminal Year |
|---------------------------|---------------|--------------|--------------|--------------|--------------|---------------|---------------|
| Revenues                  | \$ 201,569    | \$ 209,450   | \$ 217,639   | \$ 226,149   | \$ 234,991   | \$ 244,180    | \$ 249,063    |
| Operating Margin          | 3.01%         | 6.18%        | 7.76%        | 8.56%        | 8.95%        | 9.35%         | 9.35%         |
| Operating Income          | \$ 6,065.00   | \$ 12,942.85 | \$ 16,899.10 | \$ 19,352.39 | \$ 21,040.39 | \$ 22,830.80  | \$ 23,287.41  |
| Effective tax rate        | 30.00%        | 30.00%       | 30.00%       | 30.00%       | 30.00%       | 30.00%        | 30.00%        |
| AT Operating Income       | \$ 4,245.50   | \$ 9,060.00  | \$ 11,829.37 | \$ 13,546.68 | \$ 14,728.27 | \$ 15,981.56  | \$ 16,301.19  |
| + Depreciation            | \$ 26,714.00  | \$ 27,759    | \$ 28,844    | \$ 29,972    | \$ 31,144    | \$ 32,361     |               |
| - Cap Ex                  | \$ 31,854.00  | \$ 33,099    | \$ 34,394    | \$ 35,738    | \$ 37,136    | \$ 38,588     |               |
| - Chg in WC               |               | \$ 472.88    | \$ 491.37    | \$ 510.58    | \$ 530.55    | \$ 551.29     |               |
| FCFF                      |               | \$ 3,246.14  | \$ 5,788.19  | \$ 7,269.29  | \$ 8,205.44  | \$ 9,203.68   | \$ 13,011.34  |
| Terminal Value            |               |              |              |              |              | \$ 216,855.71 |               |
| Return on capital         |               |              |              |              |              |               | 12.37%        |
| Cost of Capital           |               | 9.91%        | 9.91%        | 9.91%        | 9.91%        | 9.91%         | 8.00%         |
| Cumulated Discount Factor |               | 1.0991       | 1.2080       | 1.3277       | 1.4593       | 1.6039        |               |
| Present Value             |               | \$ 2,953.45  | \$ 4,791.47  | \$ 5,474.95  | \$ 5,622.81  | \$ 140,940.73 |               |
| Value of Operating Assets | \$ 159,783.41 |              |              |              |              |               |               |
| + Cash                    | \$ 31,752.00  |              |              |              |              |               |               |
| + Cross Holdings          | \$ 33,566.00  |              |              |              |              |               |               |
| - Debt                    | \$ 58,379.00  |              |              |              |              |               |               |
| - Minority Interets       | \$ 1,245.00   |              |              |              |              |               |               |
| Value of Equity           | \$ 165,477.41 |              |              |              |              |               |               |
| Number of shares          | 4209.7        |              |              |              |              |               |               |
| Value per share           | \$ 39.31      |              |              |              |              |               |               |

Operating margin converges on Shell's historical average margin of 9.35% from 200-2015

Return on capital reverts and stays at Shell's historic average of 12.37% from 200-2015

# SHELL'S REVENUES & OIL PRICES

*Shell: Revenues vs Oil Price*

![](_page_342_Figure_165.jpeg)

![](_page_343_Figure_16.jpeg)

**Revenue calculated from the oil price drawn from distribution**

Revenue =  $39992.77 + 4039.40 * \text{Oil Price/Barrel}$ 

**Pre-tax Operating Income based on revenue & selected margin**

Pre-tax Operating Income = Revenues \* Operating Margin

![](_page_343_Figure_21.jpeg)

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

![](_page_343_Figure_25.jpeg)

# VALUE, PRICE AND INFORMATION: CLOSING THE DEAL

Value versus Price

345

# ARE YOU VALUING OR PRICING?

## *Tools for intrinsic analysis*

- - Discounted Cashflow Valuation (DCF)
- - Intrinsic multiples
- - Book value based approaches
- - Excess Return Models

## *Tools for "the gap"*

- - Behavioral finance
- - Price catalysts

## *Tools for pricing*

- - Multiples and comparables
- - Charting and technical indicators
- - Pseudo DCF

Value of cashflows, adjusted for time and risk

INTRINSIC VALUE

Value

THE GAP  
Is there one?  
Will it close?

Price

PRICE

![](_page_345_Figure_140.jpeg)

## Drivers of intrinsic value

- - Cashflows from existing assets
- - Growth in cash flows
- - Quality of Growth

## *Drivers of "the gap"*

- - Information
- - Liquidity
- - Corporate governance

## *Drivers of price*

- - Market moods & momentum
- - Surface stories about fundamentals

# VALUE VERSUS PRICE

|                        | View of the gap                                                                                                              | Investment Strategies                                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| The Efficient Marketer | The gaps between price and value, if they do occur, are random.                                                              | Index funds                                                                                                                                |
| The “value” extremist  | You view pricers as dilettantes who will move on to fad and fad. Eventually, the price will converge on value.               | Buy and hold stocks where value < price                                                                                                    |
| The pricing extremist  | Value is only in the heads of the “eggheads”. Even if it exists (and it is questionable), price may never converge on value. | <ol style="list-style-type: none;"> <li>(1) Look for mispriced securities.</li> <li>(2) Get ahead of shifts in demand/momentum.</li> </ol> |

# THE VALUER'S DILEMMA AND WAYS OF DEALING WITH IT...

- ▪ Uncertainty about the magnitude of the gap:
  - ▪ Margin of safety: Many value investors swear by the notion of the “margin of safety” as protection against risk/uncertainty.
  - ▪ Collect more information: Collecting more information about the company is viewed as one way to make your investment less risky.
  - ▪ Ask what if questions: Doing scenario analysis or what if analysis gives you a sense of whether you should invest.
  - ▪ Confront uncertainty: Face up to the uncertainty, bring it into the analysis and deal with the consequences.
- ▪ Uncertainty about gap closing: This is tougher and you can reduce your exposure to it by
  - ▪ Lengthening your time horizon
  - ▪ Providing or looking for a catalyst that will cause the gap to close.

# STRATEGIES FOR MANAGING THE RISK IN THE “CLOSING” OF THE GAP

- ▪ The “karmic” approach: In this one, you buy (sell short) under (over) valued companies and sit back and wait for the gap to close. You are implicitly assuming that given time, the market will see the error of its ways and fix that error.
- ▪ The catalyst approach: For the gap to close, the price has to converge on value. For that convergence to occur, there usually has to be a catalyst.
  - ▪ If you are an activist investor, you may be the catalyst yourself. In fact, your act of buying the stock may be a sufficient signal for the market to reassess the price.
  - ▪ If you are not, you have to look for other catalysts. Here are some to watch for: a new CEO or management team, a “blockbuster” new product or an acquisition bid where the firm is targeted.

# AN EXAMPLE: APPLE – PRICE VERSUS VALUE (MY ESTIMATES) FROM 2011 TO 2020

Apple: Stock Price - 2011 to 2020

![](_page_349_Figure_12.jpeg)

# A CLOSING THOUGHT...

![](_page_350_Picture_10.jpeg)