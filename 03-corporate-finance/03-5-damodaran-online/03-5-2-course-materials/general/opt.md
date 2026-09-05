---
title: "Option Pricing Applications in Equity Valuation"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/opt.html
---

Option Pricing Applications in Equity Valuation

APPLICATIONS OF OPTION PRICING THEORY TO EQUITY VALUATION  
**Application of option pricing models to valuation**

***A few caveats on applying option pricing models***   
  
*1. The underlying asset is not traded*

* Option pricing theory is built on the premise that a replicating
  portfolio can be created using the underlying asset and riskless
  lending and borrowing.* The options presented in this section are on assets that are not
    traded, and the value from option pricing models have to be interpreted
    with caution.

*2. The price of the asset follows a continuous process*

* The Black-Scholes option pricing model is derived under the assumption
  that the underlying asset's price process is continuous, i.e.,
  there are no price jumps.* If this assumption is violated, as it is with most real options,
    the model will underestimate the value of deep out-of-the-money
    options.
    + One solution is to use a higher variance estimate to value deep
      out-of-the-money options and lower variance estimates for at-the-money
      or in-the-money options.+ Another is to use an option pricing model that explicitly allows
        for price jumps, though the inputs to these models are often difficult
        to estimate.

*3. The variance is known and does not change over the life of
the option*

* The assumption that option pricing models make, that the variance
  is known and does not change over the option lifetime, is not
  unreasonable when applied to listed short-term options on traded
  stocks.* When option pricing theory is applied to long-term real options,
    there are problems with this assumption, since the variance is
    unlikely to remain constant over extended periods of time and
    may in fact be difficult to estimate in the first place.

*4. Exercise is instantaneous*

* The option pricing models are based upon the premise that the
  exercise of an option is instantaneous.* This assumption may be difficult to justify with real options,
    where exercise may require the building of a plant or the construction
    of an oil rig, actions which are unlikely to happen in an instant.* The fact that exercise takes time also implies that the true life
      of a real option is often less than the stated life.

***I. Valuing Equity as an option***

*The General Framework*

* The equity in a firm is a residual claim, i.e., equity holders
  lay claim to all cashflows left over after other financial claim-holders
  (debt, preferred stock etc.) have been satisfied.* If a firm is liquidated, the same principle applies, with equity
    investors receiving whatever is left over in the firm after all
    outstanding debts and other financial claims are paid off.* The principle of limited liability, however, protects equity investors
      in publicly traded firms if the value of the firm is less than
      the value of the outstanding debt, and they cannot lose more than
      their investment in the firm.

**Equity as a call option**

* The payoff to equity investors, on liquidation, can therefore
  be written as:

Payoff to equity on liquidation

= V - D if V > D   
  
= 0 if V   
  
where,   
  
V = Value of the firm   
  
D = Face Value of the outstanding debt and other external claims

* A call option, with a strike price of K, on an asset with a current
  value of S, has the following payoffs:

Payoff on exercise = S - K if S > K   
  
= 0 if S

**Payoff Diagram for Equity as a Call Option**

* Equity can thus be viewed as a **call option** the firm, where exercising the option requires that the firm
  be liquidated and the face value of the debt (which corresponds
  to the exercise price) paid off.

![](Image114.gif)

* If the debt in the firm is a single issue of zero-coupon bonds
  with a fixed lifetime, and the firm can be liquidated by equity
  investors at any time prior, the **life of equity as a call option corresponds to the life of the
  bonds**.

*Illustration 3: Application to valuation: A simple example*

* Assume that you have a firm whose assets are currently valued
  at $100 million and that the standard deviation in this asset
  value is 40%.* Further, assume that the face value of debt is $80 million (It
    is zero coupon debt with 10 years left to maturity).* If the ten-year treasury bond rate is 10%, how much is the equity
      worth? What should the interest rate on debt be?

**Model Parameters**

*The parameters of equity as a call option are as follows:*   
  
Value of the underlying asset = S = Value of the firm = $ 100
million   
  
Exercise price = K = Face Value of outstanding debt = $ 80 million
  
  
Life of the option = t = Life of zero-coupon debt = 10 years   
  
Variance in the value of the underlying asset = s2 = Variance in firm value = 0.16   
  
Riskless rate = r = Treasury bond rate corresponding to option
life = 10%

**Valuing Equity as a Call Option**

Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.5994 N(d1) = 0.9451   
  
d2 = 0.3345 N(d2) = 0.6310

Value of the call = 100 (0.9451) - 80 exp(-0.10)(10) (0.6310)
= $75.94 million

Value of the outstanding debt = $100 - $75.94 = $24.06 million

Interest rate on debt = ($ 80 / $24.06)1/10 -1 = 12.77%

*Implications of viewing equity as a call option*

*A. Valuing equity in a troubled firm*

* The first implication is that **equity will have value, even if the value of the firm falls well
  below the face value of the outstanding debt**.* Such a firm will be viewed as troubled by investors, accountants
    and analysts, but that does not mean that its equity is worthless.* Just as deep out-of-the-money traded options command value because
      of the possibility that the value of the underlying asset may
      increase above the strike price in the remaining lifetime of the
      option, equity will command value because of the **time premium** on the option (the time until the bonds mature and come due)
      and the **possibility that the value of the assets may increase above the
      face value of the bonds** before they come due.

*Illustration 4 : Value of a troubled firm*

*The parameters of equity as a call option are as follows:*   
  
Value of the underlying asset = S = Value of the firm = $ 50 million
  
  
Exercise price = K = Face Value of outstanding debt = $ 80 million
  
  
Life of the option = t = Life of zero-coupon debt = 10 years   
  
Variance in the value of the underlying asset = s2 = Variance in firm value = 0.16   
  
Riskless rate = r = Treasury bond rate corresponding to option
life = 10%

**Valuing Equity in a Troubled Firm**

Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.0515 N(d1) = 0.8534   
  
d2 = -0.2135 N(d2) = 0.4155

---

  
  
Value of the call = 50 (0.8534) - 80 exp(-0.10)(10) (0.4155) =
$30.44 million   
  
Value of the bond= $50 - $30.44 = $19.56 million

* The equity in this firm has substantial value, because of the
  option characteristics of equity. * This might explain why stock in firms, which are in Chapter 11
    and essentially bankrupt, still has value.

*B. The Conflict between bondholders and stockholders*

* Stockholders and bondholders have different objective functions,
  and this can lead to agency problems, where stockholders can expropriate
  wealth from bondholders. * The conflict can manifest itself in a number of ways - for instance,
    stockholders have an incentive to take riskier projects than bondholders
    do, and to pay more out in dividends than bondholders would like
    them to. * This conflict between bondholders and stockholders can be illustrated
      dramatically using the option pricing model. * Since equity is a call option on the value of the firm, an increase
        in the variance in the firm value, other things remaining equal,
        will lead to an increase in the value of equity. * It is therefore conceivable that stockholders can take risky projects
          with negative net present values, which while making them better
          off, may make the bondholders and the firm less valuable. This
          is illustrated in the following example.

*Illustration 5: Effect on value of the conflict between stockholders
and bondholders*

* Consider again the firm described in illustration 16.1 , with
  a value of assets of $100 million, a face value of zero-coupon
  ten-year debt of $80 million, a standard deviation in the value
  of the firm of 40%. The equity and debt in this firm were valued
  as follows:

Value of Equity = $75.94 million   
  
Value of Debt = $24.06 million   
  
Value of Firm == $100 million

* Now assume that the stockholders have the opportunity to take
  a project with a negative net present value of -$2 million, but
  assume that this project is a very risky project that will push
  up the standard deviation in firm value to 50%.

**Valuing Equity after the Project**

* The equity as a call option can then be valued using the following
  inputs:

Value of the underlying asset = S = Value of the firm = $ 100
million - $2 million = $ 98 million (The value of the firm is
lowered because of the negative net present value project)   
  
Exercise price = K = Face Value of outstanding debt = $ 80 million   
  
Life of the option = t = Life of zero-coupon debt = 10 years   
  
Variance in the value of the underlying asset = s2 = Variance in firm value = 0.25   
  
Riskless rate = r = Treasury bond rate corresponding to option
life = 10%   
  
Based upon these inputs, the Black-Scholes model provides the
following value for the equity and debt in this firm.   
  
Value of Equity = $77.71   
  
Value of Debt = $20.29   
  
Value of Firm = $98.00

* The value of equity rises from $75.94 million to $ 77.71 million
  , even though the firm value declines by $2 million. The increase
  in equity value comes at the expense of bondholders, who find
  their wealth decline from $24.06 million to $20.19 million.

*Illustration 6: Effects on equity of a conglomerate merger*   
  
You are provided information on two firms, which operate in unrelated
businesses and hope to merge.   
  
*Firm A Firm B*Value of the firm $100 million $ 150 million   
  
Face Value of Debt $ 80 million $ 50 million (Zero-coupon debt)
  
  
Maturity of debt 10 years 10 years   
  
Std. Dev. in firm value 40 % 50 %   
  
Correlation between firm   
  
cashflows 0.4   
  
The ten-year bond rate is 10%.

* The variance in the value of the firm after the acquisition can
  be calculated as follows:

Variance in combined firm value = w12 s12 + w22 s22 + 2 w1 w2 r12 s1 s2   
  
= (0.4)2 (0.16) + (0.6)2 (0.25) + 2 (0.4) (0.6) (0.4) (0.4) (0.5)   
  
= 0.154

**Valuing the Combined Firm**

The values of equity and debt in the individual firms and the
combined firm can then be estimated using the option pricing model:   
  
Firm A Firm B Combined firm   
  
Value of equity in the firm $75.94 $134.47 $ 207.43   
  
Value of debt in the firm $24.06 $ 15.53 $ 42.57   
  
Value of the firm $100.00 $150.00 $ 250.00

* The combined value of the equity prior to the merger is $ 210.41
  million and it declines to $207.43 million after. * The wealth of the bondholders increases by an equal amount. * There is a transfer of wealth from stockholders to bondholders,
      as a consequence of the merger. Thus, conglomerate mergers that
      are not followed by increases in leverage are likely to see this
      redistribution of wealth occur across claim holders in the firm.

*Obtaining option pricing inputs - Some real world problems*

The examples that have been used to illustrate the use of option
pricing theory to value equity have made some simplifying assumptions.
Among them are the following:   
  
(1) There were only two claim holders in the firm - debt and equity.
  
  
(2) There is only one issue of debt outstanding and it can be
retired at face value.   
  
(3) The debt has a zero coupon and no special features (convertibility,
put clauses etc.)   
  
(4) The value of the firm and the variance in that value can be
estimated.

*Applicability in valuation*

|  |  |
| --- | --- |
| Input | Estimation Process |
| Value of the Firm | * Cumulate market values of equity and debt (or)* Value the firm using FCFF and WACC (or)* Use cumulated market value of assets, if traded. |
| Variance in Firm Value | * If stocks and bonds are traded,   s2firm = we2 se2 + wd2 sd2 + 2 we wd red sesd    where se2 = variance in the stock price we = MV weight of Equity     sd2 = the variance in the bond price wd = MV weight of debt   * If not traded, use variances of similarly rated bonds.* Use average firm value variance from the industry in which company     operates. |
| Maturity of the Debt | * Face value weighted duration of bonds outstanding (or)* If not available, use weighted maturity |

  
  
*Illustration 7: Valuing Equity as an option - The example of an
airline*

* Assume that you have been asked to value an airline. The airline
  owns routes in North America, Europe and South America, with the
  following estimates of current market value:

North America $ 400 million   
  
Europe $ 500 million   
  
South America $ 100 million

* The airline has considerable debt outstanding. It has four debt
  issues outstanding with the following characteristics:

Maturity Face Value Coupon Duration   
  
20 year debt $ 100 mil 11% 14.1 years   
  
15 year debt $ 100 mil 12% 10.2 years   
  
10 year debt $ 200 mil 12% 7.5 years   
  
1 year debt $ 800 mil 12.5% 1 year

* The stock of the airline has been trading on the NYSE. The annualized
  standard deviation in ln(stock prices) has been 25%, and the firm's
  debt has been approximately 90% of the firm value (during the
  variance estimation period). * The firm is rated B. Though its bonds are not traded, other B
    rated bonds have had an annualized standard deviation of 10% (in
    ln(bond prices)). The correlation between B rated bonds and this
    airline's stock price is 0.3. * The firm pays no dividends. The current T. Bond rate is 8%.

**Valuing Equity in the Airline**

Step 1: Estimate the value of the firm = Sum of the value of its
assets = 400 + 500 + 100 = 1,000 million   
  
Step 2: Estimate the average duration of the debt outstanding
= (100/1200) \* 14.1 + (100/1200) \* 10.2 + (200/1200) \* 7.5 + (800/1200)
\* 1 = 3.9417 years   
  
Step 3: Estimate the face value of debt outstanding = 100 + 100
+ 200 + 800 = 1,200 million   
  
Step 4: Estimate the variance in the value of the firm = Weighted
average of the variances in stock and bond prices. =   
  
Variance of the firm = (E/(D+E))2 se2 + (D/(D+E))2 sd2 + 2 (E/(D+E)) (D/(D+E)) red sesd   
  
= (.1)2 (.25)2 + (.9)2 (.10)2 + 2 (.1)(.9)(.3) (.25)(.10) = 0.010075   
  
Step 5: Value equity as an option   
  
d1 = 0.7671 N(d1) = 0.7784   
  
d2 = 0.5678 N(d2) = 0.7148

Value of the call = 1000 (0.7784) - 1200 exp(-0.08)(3.9417) (0.7148)
= $ 152.63 million

---

  
  
*Illustration 8: Valuing Equity as an option - Cablevision Systems*

* Cablevision Systems was a firm in trouble in March 1995. 
  + The book value of equity in March 1995 was negative : - 1820 million+ It lost $315 million in 1994 and was expected to lose equivalent
      amounts in 1995 and 1996. + It had $ 3000 million in face value debt outstanding* The weighted average duration of this debt was 4.62 years

*Debt Type Face Value Duration*   
  
Short term Debt $ 865 mil 0.5 years   
  
Bank Debt $ 480 mil 3.0 years   
  
Senior Debt $ 832 mil 6.0 years   
  
Senior Subordinated $ 823 mil 8.5 years   
  
Total $ 3000 mil 4.62 years

* The value of the firm estimated using projected cashflows to the
  firm, discounted at the weighted average cost of capital was $2,871
  million. This was based upon the following assumptions ñ
  + Revenues will grow 14% a year for the next 5 years, and make a
    linear transition to 5% in 10 years.+ The COGS (not including depreciation), which is currently 69%
      of revenues, will drop to 65% of revenues in year 5 and stay at
      that level. (68% in 1996, 67% in 1997, 66% in 1998, 65% in 1999)+ Capital spending and depreciation will grow 10% a year for the
        next five yearsafter which the growth rate will drop to 5% a year.+ Working capital will remain at 5% of revenues.+ The debt ratio, which is currently 70.14%, will drop to 50% after
            year 10. The cost of debt is 10% in high growth period and 8.5%
            after that.+ The beta for the stock will be 1.55 for the next five years, and
              drop to 1.1 over the next 5 years.+ The treasury bond rate is 7.5%.

Cost of Capital in high growth period = 16.03% (0.2986) + 10%
(1 - 0.36) (0.7014) = 9.27%   
  
Cost of Capital in terminal period = 13.55% (0.50) + 8.50% (1
- 0.36) (0.50) = 9.34%

* The projected cash flows over the next ten years are summarized
  below ñ

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Term. Year |
| Revenues | $954.4 | $1,088.0 | $1,240.3 | $1,414.0 | $1,611.9 | $1,808.6 | $1,996.7 | $2,168.4 | $2,315.8 | $2,431.6 | $2,553.26 |
| - COGS | $658.5 | $739.86 | $831.03 | $933.24 | $1,047.7 | $1,175.6 | $1,297.1 | $1,409.4 | $1,505.3 | $1,580.5 | $1,659.62 |
| - Depreciation | $253.0 | $278.30 | $306.13 | $336.74 | $370.42 | $388.94 | $408.39 | $428.80 | $450.24 | $472.76 | $496.39 |
| EBIT | $42.87 | $69.87 | $103.19 | $144.02 | $193.77 | $244.08 | $290.46 | $330.15 | $360.31 | $378.33 | $397.25 |
| - EBIT\*t | $15.43 | $25.15 | $37.15 | $51.85 | $69.76 | $87.87 | $104.57 | $118.85 | $129.71 | $136.20 | $143.01 |
| EBIT (1-t) | $27.43 | $44.72 | $66.04 | $92.17 | $124.01 | $156.21 | $185.90 | $211.29 | $230.60 | $242.13 | $254.24 |
| + Depreciation | $253.0 | $278.30 | $306.13 | $336.74 | $370.42 | $388.94 | $408.39 | $428.80 | $450.24 | $472.76 | $496.39 |
| -Capital Spending | $275.0 | $302.50 | $332.75 | $366.03 | $402.63 | $422.76 | $443.90 | $466.09 | $489.40 | $513.87 | $496.39 |
| - Æ Wking Capital | $5.86 | $6.68 | $7.62 | $8.68 | $9.90 | $9.83 | $9.40 | $8.59 | $7.37 | $5.79 | $6.08 |
| Free CF to Firm | ($0.43) | $13.83 | $31.80 | $54.21 | $81.90 | $112.56 | $140.98 | $165.42 | $184.08 | $195.23 | $248.16 |
|  |  |  |  |  |  |  |  |  |  |  |  |

* Terminal Value = $248.16 / ( .0934 - .05) = $5725 million* The stock has been traded on the NYSE, and the variance based
    upon ln (monthly prices) between 1990 and 1994 is 0.0133. * There are Cablevision bonds, due in 2002, that have been traded
      from 1990 to 1994, and the variance in ln(monthly price)s for
      these bonds is 0.0012. * The correlation between stock price and bond price changes has
        been 0.25. The proportion of debt in the capital structure during
        the priod (1990-94) was 70%.

*The stock and bond price variance are first annualized:*   
  
Annualized variance in stock price = 0.0133 \* 12 = 0.16 Standard
deviation = 0.40   
  
Annualized variance in bond price = 0.0012 \* 12 = 0.0144 Standard
deviation = 0.12   
  
*Annualized variance in firm value*= (0.30)2 (0.16) + (0.70)2 (0.0.0144) + 2 (0.3) (0.7)(0.25)(0.40)(0.12)=
0.02637668

* The five-year bond rate (corresponding to the weighted average
  duration of 4.62 years) is 7%.

*The parameters of equity as a call option are as follows:*   
  
Value of the underlying asset = S = Value of the firm = $ 2871
million   
  
Exercise price = K = Face Value of outstanding debt = $ 3000 million   
  
Life of the option = t = Weighted average duration of debt = 4.62
years   
  
Variance in the value of the underlying asset = s2 = Variance in firm value = 0.0264   
  
Riskless rate = r = Treasury bond rate corresponding to option
life = 7%   
  
Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 0.9910 N(d1) = 0.8391   
  
d2 = 0.6419 N(d2) = 0.7391

Value of the call = 2871 (0.8391) - 3000 exp(-0.07)(4.62) (0.7395)
= $ 817 million

Cablevision's equity was trading at $1100 million in March 1995.   
  
***II. Valuing Natural Resource Options/ Firms***   
  
*The General Framework*

* In a natural resource investment, the underlying asset is the
  resource and the value of the asset is based upon two variables
  - the quantity of the resource that is available in the investment
  and the price of the resource.* In most such investments, there is a cost associated with developing
    the resource, and the difference between the value of the asset
    extracted and the cost of the development is the profit to the
    owner of the resource.* Defining the cost of development as X, and the estimated value
      of the resource as V, the potential payoffs on a natural resource
      option can be written as follows:

Payoff on natural resource investment = V - X if V > X   
  
= 0 if V

**Payoff on a Natural Resource Investment**  
![](Image115.gif)  
**Obtaining the inputs for valuing natural resource options**

|  |  |
| --- | --- |
| Input | Estimation Process |
| 1. Value of Available Reserves of the Resource | * Expert estimates (Geologists for oil..); The present value of   the after-tax cash flows from the resource are then estimated. |
| 2. Cost of Developing Reserve (Strike Price) | * Past costs and the specifics of the investment |
| 3. Time to Expiration | * Relinqushment Period: if asset has to be relinquished at a point   in time.* Time to exhaust inventory - based upon inventory and capacity     output. |
| 4. Variance in value of underlying asset | * based upon variability of the price of the resources and variability   of available reserves. |
| 5. Net Production Revenue (Dividend Yield) | * Net production revenue every year as percent of market value. |
| 6. Development Lag | * Calculate present value of reserve based upon the lag. |

  
  
*Illustration 9 : Application to valuation: A gold mine*

* Consider a gold mine with an estimated inventory of 1 million
  ounces, and a capacity output rate of 50,000 ounces per year.
  * The price of gold is expected to grow 3% a year. * The firm owns the rights to this mine for the next twenty years.
      * The present value of the cost of opening the mine is $40 million,
        and the average production cost of $250 per ounce. This production
        cost, once initiated, is expected to grow 4% a year. * The standard deviation in gold prices is 20%, and the current
          price of gold is $350 per ounce. The riskless rate is 9%, and
          the cost of capital for operating the mine is 10%. The inputs
          to the model are as follows:

**Inputs for the Option Pricing Model**

Value of the underlying asset = Present Value of expected gold
sales (@ 50,000 ounces a year) = (50,000 \* 350) \* (1- (1.0320/1.1020))/(.10-.03)
- (50,000\*250)\* (1- (1.0420/1.1020))/(.10-.04) = $ 42.40 million   
  
Exercise price = PV of Cost of opening mine = $40 million   
  
Variance in ln(gold price) = 0.04   
  
Time to expiration on the option = 20 years   
  
Riskless interest rate = 9%   
  
Dividend Yield = Loss in production for each year of delay = 1
/ 20 = 5%   
  
(Note: It will take twenty years to empty the mine, and the firm
owns the rights for twenty years. Every year of delay implies
a loss of one year of production.)

**Valuing the Option**

Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.4069 N(d1) = 0.9202   
  
d2 = 0.5124 N(d2) = 0.6958   
  
Call Value= 42.40 exp(-0.05)(20) (0.9202) -40 (exp(-0.09)(20)
(0.6958)= $ 9.75 million   
  
The value of the mine as an option is $ 9.75 million, in contrast
to the static capital budgeting analysis which would have yielded
a net present value of $ 2.40 million ($42.40 million - $ 40 million).
The additional value accrues directly from the mine's option characteristics.

*Illustration 10: Valuing an oil reserve*

* Consider an offshore oil property with an estimated oil reserve
  of 50 million barrels of oil, where the present value of the development
  cost is $12 per barrel and the development lag is two years. * The firm has the rights to exploit this reserve for the next twenty
    years and the marginal value per barrel of oil is $12 per barrel
    currently (Price per barrel - marginal cost per barrel). * Once developed, the net production revenue each year will be 5%
      of the value of the reserves. The riskless rate is 8% and the
      variance in ln(oil prices) is 0.03.

**Inputs to the Black-Scholes Model**

Given this information, the inputs to the Black-Scholes can be
estimated as follows:   
  
Current Value of the asset = S = Value of the developed reserve
discounted back the length of the development lag at the dividend
yield = $12 \* 50 /(1.05)2 = $ 544.22   
  
(If development is started today, the oil will not be available
for sale until two years from now. The estimated opportunity cost
of this delay is the lost production revenue over the delay period.
Hence, the discounting of the reserve back at the dividend yield)   
  
Exercise Price = Present Value of development cost = $12 \* 50
= $600 million   
  
Time to expiration on the option = 20 years   
  
Variance in the value of the underlying asset = 0.03   
  
Riskless rate =8%   
  
Dividend Yield = Net production revenue / Value of reserve = 5%

**Valuing the Option**

Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.0359 N(d1) = 0.8498   
  
d2 = 0.2613 N(d2) = 0.6030   
  
Call Value= 544 .22 exp(-0.05)(20) (0.8498) -600 (exp(-0.08)(20)
(0.6030)= $ 97.08 million   
  
This oil reserve, though not viable at current prices, still is
a valuable property because of its potential to create value if
oil prices go up.   
  
*Extending the option pricing approach to value natural resource
firms*

* Since the assets owned by a natural resource firm can be viewed
  primarily as options, the firm itself can be valued using option
  pricing theory.* The preferred approach would be to consider each option separately,
    value it and cumulate the values of the options to get the value
    of the firm.* Since this information is likely to be difficult to obtain for
      large natural resource firms, such as oil companies, which own
      hundreds of such assets, a variant of this approach is to value
      the entire firm as one option.* A purist would probably disagree, arguing that valuing an option
        on a portfolio of assets (as in this approach) will provide a
        lower value than valuing a portfolio of options (which is what
        the natural resource firm really own). Nevertheless, the value
        obtained from the model still provides an interesting perspective
        on the determinants of the value of natural resource firms.

**Inputs to the Black-Scholes Model**

*Input to model Corresponding input for valuing natural resource
firm*   
  
Value of underlying asset Value of cumulated estimated reserves
of the resource owned by the firm, discounted back at the dividend
yield for the development lag.   
  
Exercise Price Estimated cumulated cost of developing estimated
reserves   
  
Time to expiration on option Average relinquishment period across
all reserves owned by firm (if known) or estimate of when reserves
will be exhausted, given current production rates.   
  
Riskless rate Riskless rate corresponding to life of the option
  
  
Variance in value of asset Variance in the price of the natural
resource   
  
Dividend yield Estimated annual net production revenue as percentage
of value of the reserve.   
  
*Illustration 11: Valuing an oil company - Gulf Oil in 1984*

* Gulf Oil was the target of a takeover in early 1984 at $70 per
  share (It had 165.30 million shares outstanding, and total debt
  of $9.9 billion).* It had estimated reserves of 3038 million barrels of oil and the
    average cost of developing these reserves was estimated to be
    $10 a barrel in present value dollars (The development lag is
    approximately two years).* The average relinquishment life of the reserves is 12 years.* The price of oil was $22.38 per barrel, and the production cost,
        taxes and royalties were estimated at $7 per barrel.* The bond rate at the time of the analysis was 9.00%.* Gulf was expected to have net production revenues each year of
            approximately 5% of the value of the developed reserves. The variance
            in oil prices is 0.03.

**Valuing the Option**

Value of underlying asset = Value of estimated reserves discounted
back for period of development lag= 3038 \* ($ 22.38 - $7) / 1.052
= $42,380.44   
  
Exercise price = Estimated development cost of reserves = 3038
\* $10 = $30,380 million   
  
Time to expiration = Average length of relinquishment option =
12 years   
  
Variance in value of asset = Variance in oil prices = 0.03   
  
Riskless interest rate = 9%   
  
Dividend yield = Net production revenue/ Value of developed reserves
= 5%   
  
Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.6548 N(d1) = 0.9510   
  
d2 = 1.0548 N(d2) = 0.8542   
  
Call Value= 42,380.44 exp(-0.05)(12) (0.9510) -30,380 (exp(-0.09)(12)
(0.8542)= $ 13,306 million

**Valuing Gulf Oil**

* This represents the value of the undeveloped reserves of oil owned
  by Gulf Oil.* In addition, Gulf Oil had free cashflows to the firm from its
    oil and gas production of $915 million from already developed
    reserves and these cashflows are likely to continue for ten years
    (the remaining lifetime of developed reserves).* The present value of these developed reserves, discounted at the
      weighted average cost of capital of 12.5%, yields:

Value of already developed reserves = 915 (1 - 1.125-10)/.125
= $5065.83   
  
Adding the value of the developed and undeveloped reserves of
Gulf Oil provides the value of the firm.   
  
Value of undeveloped reserves = $ 13,306 million   
  
Value of production in place = $ 5,066 million   
  
Total value of firm = $ 18,372 million   
  
Less Outstanding Debt = $ 9,900 million   
  
Value of Equity = $ 8,472 million   
  
Value per share = $ 8,472/165.3 = $51.25   
  
This analysis would suggest that Gulf Oil was overvalued at $70
per share.

***III. Valuing product patents as options***

*The General Framework*

* A product patent provides the firm with the right to develop the
  product and market it.* It will do so only if the present value of the expected cash flows
    from the product sales exceed the cost of development.* If this does not occur, the firm can shelve the patent and not
      incur any further costs.* If I is the present value of the costs of developing the product,
        and V is the present value of the expected cashflows from development,
        the payoffs from owning a product patent can be written as:

Payoff from owning a product patent = V - I if V> I   
  
= 0 if V   
  
![](Image116.gif)   
  
*Obtaining the inputs for option valuation*

|  |  |
| --- | --- |
| Input | Estimation Process |
| 1. Value of the Underlying Asset | * Present Value of Cash Inflows from taking project now* This will be noisy, but that adds value. |
| 2. Variance in value of underlying asset | * Variance in cash flows of similar assets or firms* Variance in present value from capital budgeting simulation. |
| 3. Exercise Price on Option | * Option is exercised when investment is made.* Cost of making investment on the project; assumed to be constant     in present value dollars. |
| 4. Expiration of the Option | * Life of the patent |
| 5. Dividend Yield | * Cost of delay* Each year of delay translates into one less year of value-creating     cashflows |

  
  
*Illustration 12: Valuing a product option*

* Assume that a firm has the patent rights, for the **next twenty years**, to a product which 
  + requires an initial investment of $ 1.5 billion to develop, + and a present value, right now, of cash inflows of only $1 billion.* Assume that a simulation of the project under a variety of technological
    and competitive scenarios yields a variance in the present value
    of inflows of 0.03. * The current riskless twenty-year bond rate is 10%.

**Valuing the Option**

The inputs to the option pricing model are as follows:   
  
Value of the underlying asset = Present value of inflows (current)
= $1,000 million   
  
Exercise price = Present value of cost of developing product =
$1,500 million   
  
Time to expiration = Life of the patent = 20 years   
  
Variance in value of underlying asset = Variance in PV of inflows
= 0.03   
  
Riskless rate = 10%   
  
Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.1548 N(d1) = 0.8759   
  
d2 = 0.3802 N(d2) = 0.6481   
  
Call Value= 1000 exp(-0.05)(20) (0.8759) -1500 (exp(-0.10)(20)
(0.6481)= $ 190.66 million

* This suggests that though this product has a negative net present
  value currently, it is a valuable product when viewed as an option.
  This value can then be added to the value of the other assets
  that the firm possesses, and provides a useful framework for incorporating
  the value of product options and patents.

*Illustration 13: Valuing a firm with only product options*

* Consider a bio-technology firm, which has no cashflow-producing
  assets currently, but has one product in the pipeline that has
  much promise in providing a treatment for diabetes. * The product has not been approved by the FDA, and, even if approved,
    it could be faced with competition from similar products being
    worked on by other firms. * The firm, however, would hold the patent rights to this product
      for the next 25 years. * After a series of simulations, under a variety of technological
        and competitive environments, the expected present value of the
        cash inflows is estimated to be $500 million, with a variance
        of 0.20 (signifying the uncertainty of the process). * The expected present value of the cost of developing the product
          is estimated to be $400 million.* The annual cashflows on the product, once developed, are expected
            to be 4% of the present value of the inflows. The twenty-five
            year bond rate is 7%.

**Inputs to the Option Pricing Model**

The inputs to the option pricing model are as follows:   
  
Value of underlying asset = Present value of expected cashflows
= $ 500 million   
  
Exercise price = Present value of cost of developing product for
commercial use = $400 mil   
  
Time to expiration on the option = Time to expiration on patent
rights = 25 years   
  
Variance in value of underlying asset = 0.20   
  
Riskless rate = 7%   
  
Dividend yield = Expected annual cashflow / PV of cash inflows
= 4%   
  
Based upon these inputs, the Black-Scholes model provides the
following value for the call:   
  
d1 = 1.5532 N(d1) = 0.9398   
  
d2 = -0.6828 N(d2) = 0.2474   
  
Call Value= 500 exp(-0.04)(25) (0.9398) - 400 (exp(-0.07)(25)
(0.2474)= $ 155.66 million

* The estimated value of this firm, based upon an option pricing
  approach, is $155.66 million. This is a more realistic measure
  of value than traditional discounted cashflow valuation (that
  would have provided a value of $100 million) because it reflects
  the underlying uncertainty in the technology and in competition.

**Valuing Biogen**

* The firm is receiving royalties from Biogen discoveries (Hepatitis
  B and Intron) at pharmaceutical companies. These account for FCFE
  per share of $1.00 and are expected to grow 10% a year until the
  patent expires (in 15 years). Using a beta of 1.1 to value these
  cash flows (leading to a cost of equity of 13.05%), we arrive
  at a present value per share:

Value of Existing Products = $ 12.14

* The firm also has a patent on Avonex, a drug to treat multiple
  sclerosis, for the next 17 years, and it plans to produce and
  sell the drug by itself. The key inputs on the drug are as follows:

Present Value of Cash Flows from Introducing the Drug Now = S
= $ 3.422 billion   
  
Present Value of Cost of Developing Drug for Commercial Use =
K = $ 2.875 billion   
  
Patent Life = t = 17 years Riskless Rate = r = 6.7% (17-year T.Bond
rate)   
  
Variance in Expected Present Values =s2 = 0.224 (Industry average firm variance for bio-tech firms)   
  
Expected Cost of Delay = y = 1/17 = 5.89%   
  
d1 = 1.1362 N(d1) = 0.8720   
  
d2 = -0.8512 N(d2) = 0.2076

Call Value= 3,422 exp(-0.0589)(17) (0.8720) - 2,875 (exp(-0.067)(17)
(0.2076)= $ 907 million

Call Value per Share from Avonex = $ 907 million/35.5 million
= $ 25.55   
  
Biogen Value Per Share = Value of Existing Assets + Value of Patent
= $ 12.14 + $ 25.55 = $ 37.69
