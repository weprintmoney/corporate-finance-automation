---
title: "Basics"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/basics.pdf
---

# VALUATION: LECTURE NOTE PACKET 1 INTRINSIC VALUATION

Aswath Damodaran

Updated: January 2025

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

- ▪ Cost of Equity = 13.625%

- ▪ Value of Equity =  $50/1.13625 + 60/1.13625 + 68/1.13625 + 76.2/1.136254 + (83.49+1603)/1.136255 = \$1073$

- ▪ **Method 2: Discount CF to Firm at Cost of Capital to get value of firm**

- ▪ Cost of Debt = Pre-tax rate (1- tax rate) = 10% (1-.5) = 5%

- ▪ Cost of Capital = 13.625% (1073/1873) + 5% (800/1873) = 9.94%

- ▪ PV of Firm =  $90/1.0994 + 100/1.09942 + 108/1.09943 + 116.2/1.09944 + (123.49+2363)/1.09945 = \$1873$

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
  - ▪  $PV \text{ of Equity} = 50/1.0994 + 60/1.09942 + 68/1.09943 + 76.2/1.09944 + (83.49+1603)/1.09945 = \$1248$
  - ▪ Value of equity is overstated by \$175.
- ▪ **Error 2:** Discount CF to Firm at Cost of Equity to get firm value
  - ▪  $PV \text{ of Firm} = 90/1.13625 + 100/1.136252 + 108/1.136253 + 116.2/1.136254 + (123.49+2363)/1.136255 = \$1613$
  - ▪  $PV \text{ of Equity} = \$1612.86 - \$800 = \$813$
  - ▪ Value of Equity is understated by \$ 260.
- ▪ **Error 3:** Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity
  - ▪ Value of Equity = \$ 1613
  - ▪ Value of Equity is overstated by \$ 540

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

Start with the past

**Cash flow to Firm**  
Revenues \* Operating Margin  
= Operating Income

| * (1 - tax rate)          | Tax Effect   |
|---------------------------|--------------|
| - (Cap Ex - Depreciation) | Reinvestment |
| - Change in non-cash WC   |              |
| = Free Cash flow to Firm  |              |

\* How quickly is the firm growing?  
\* How efficiently is it growing?  
\* How profitable is the firm?

*If margins & returns are stable*  
Expected growth in operating income = Reinvestment  
Rate \* Return on Invested Capital  
 $FCFF = After-tax Oper. Income (1 - Reinvestment Rate)$ 

*If margins & returns are changing*  
1. Estimate revenue growth & future revenues  
2. Estimate operating margins over time  
3. Estimate reinvestment based on revenues  
 $FCFF = After tax Operating Income - Reinvestment$ 

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

![](_page_19_Diagram_43.jpeg)

Terminal Value =  $FCFF_{n+1} / (r - g_n)$ 

**Long term rate at which you can borrow money, today**  
(Riskfree Rate + Default Spread) (1 - tax rate)

![](_page_19_Diagram_46.jpeg)

# THE SEQUENCE

1. 1. **Get a handle on the past and the cross-section:** While the past is the past (and should have little relevance in determining value), you can get clues about the future by looking at what your firm has done in the past, and what other companies in the business are doing now.
2. 2. **Risk and Discount Rates:** Traditional financial theory (unfortunately) has put too much of a focus on risk and discount rates, but they do remain ingredients in valuing a company.
3. 3. **Estimate growth and future cash flows:** This is where the rubber meets the road in valuation. Estimating future cash flows is never easy, should not be mechanical and should be built around your story.
4. 4. **Apply Closure to cash flows:** Since you cannot estimate cash flows forever, you need to find a way to bring your valuation to closure.
5. 5. Tie up loose ends: Check to see what else in your business needs to be valued or adjusted for to get to value per share.