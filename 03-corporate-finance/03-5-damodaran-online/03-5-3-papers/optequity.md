---
title: "Optequity"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/optequity.pdf
---

# E. VALUING EQUITY AS AN OPTION

- ■ The **equity in a firm is a residual claim**, i.e., equity holders lay claim to all cashflows left over after other financial claim-holders (debt, preferred stock etc.) have been satisfied.
- ■ If a firm is liquidated, the same principle applies, with **equity investors receiving whatever is left over in the firm** after all outstanding debts and other financial claims are paid off.
- ■ The **principle of limited liability**, **however, protects equity investors** in publicly traded firms if the value of the firm is less than the value of the outstanding debt, and they cannot lose more than their investment in the firm.

# PAYOFF DIAGRAM FOR LIQUIDATION OPTION

![](_page_1_Figure_26.jpeg)

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

- ▪ Interest rate on debt =  $(\$ 80 / \$24.06) 1/10 - 1 =$   
   $12.77\%$

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

![](_page_8_Figure_69.jpeg)

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

![](_page_16_Picture_5.jpeg)

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