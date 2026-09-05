---
title: "Discrate2"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/discrate2.pdf
---

![](_page_0_Picture_13.jpeg)

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

![](_page_2_Figure_10.jpeg)

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

![](_page_3_Figure_39.jpeg)

$$ADJ \text{ BETA} = (0.67) * \text{RAW BETA} + (0.33) * 1.0$$

Copyright 2000 BLOOMBERG L.P. Frankfurt:69-920410 Hong Kong:2-977-6000 London:207-330-7500 New York:212-318-2000  
Princeton:609-279-3000 Singapore:226-3000 Sydney:2-9777-8686 Tokyo:3-3201-8900 Sao Paulo:11-3048-4500  
1653-197-0 11-Aug-00 14:56:13

![](_page_3_Picture_42.jpeg)

# ONE SLICE OF HISTORY.

Market Summary > GameStop Corp.  
NYSE: GME

+ Follow

**50.99** USD **-0.11 (0.22%)** ↓

Feb 12, 2:44 PM EST · Disclaimer

1 day 5 days 1 month 6 months YTD 1 year 5 years Max

![](_page_4_Figure_26.jpeg)

![](_page_4_Figure_27.jpeg)

During 2019 and 2020, GME was an extraordinarily volatile stock, as short sellers and long only investors fought out a battle.

# AND SUBJECT TO GAME PLAYING

![](_page_5_Figure_10.jpeg)

![](_page_5_Figure_11.jpeg)

# MEASURING RELATIVE RISK: YOU DON'T LIKE BETAS OR MODERN PORTFOLIO THEORY? NO PROBLEM.

![](_page_6_Diagram_10.jpeg)

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

![](_page_9_Diagram_159.jpeg)

# IN A PERFECT WORLD... WE WOULD ESTIMATE THE BETA OF A FIRM BY DOING THE FOLLOWING

![](_page_10_Diagram_30.jpeg)

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

![](_page_18_Diagram_92.jpeg)

![](_page_19_Picture_12.jpeg)

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

![](_page_25_Figure_11.jpeg)

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

# DEFAULT SPREADS – JANUARY 2025

*Corporate Bond Default Spreads on January 1, 2025*

![](_page_26_Figure_260.jpeg)

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
  - ■ Estimated market value of debt = 222 million (PV of annuity, 4 years, 9.29%) + \$1,953 million/1.09294 = 2,083 million BR

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
  - ▪ Straight debt =  $(4\% \text{ of } \$125 \text{ million}) (\text{PV of annuity, 10 years, 8\%}) + 125 \text{ million} / 1.0810 = \$91.45 \text{ million}$
  - ▪ Equity portion =  $\$140 \text{ million} - \$91.45 \text{ million} = \$48.55 \text{ million}$
- ▪ The debt portion (\$91.45 million) gets added to debt and the option portion (\$48.55 million) gets added to the market capitalization to get to the debt and equity weights in the cost of capital.

# RECAPPING THE COST OF CAPITAL

![](_page_33_Diagram_49.jpeg)