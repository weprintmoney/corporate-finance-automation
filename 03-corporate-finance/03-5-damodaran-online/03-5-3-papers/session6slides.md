---
title: "Session6Slides"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valspr19/session6slides.pdf
---

# Why implied premiums matter?

- □ In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. If all analysts in the department used the arithmetic average premium (for stocks over T.Bills) for 1928-2018 of 7.93% to value stocks in January 2019, given the implied premium of 5.96%, what are they likely to find?
  - a. The values they obtain will be too low (most stocks will look overvalued)
  - b. The values they obtain will be too high (most stocks will look under valued)
  - c. There should be no systematic bias as long as they use the same premium to value all stocks.
- □ What if analysts are using the historical geometric average premium of 4.66% from 1928 to 2018 as their ERP?

### Which equity risk premium should you use?

### **If you assume this Premium to use**

Premiums revert back to historical norms and your time period yields these norms

Historical risk premium

Market is correct in the aggregate or that your valuation should be market neutral

Current implied equity risk premium

Marker makes mistakes even in the aggregate but is correct over time

Average implied equity risk premium over time.

| Predictor                             | Correlation with implied premium next year | Correlation with return- next 5 years | Correlation with actual next 10 years |
|---------------------------------------|--------------------------------------------|---------------------------------------|---------------------------------------|
| Current implied premium               | 0.763                                      | 0.427                                 | 0.500                                 |
| Average implied premium: Last 5 years | 0.718                                      | 0.326                                 | 0.450                                 |
| Historical Premium                    | -0.497                                     | -0.437                                | -0.454                                |
| Default Spread based premium          | 0.047                                      | 0.143                                 | 0.160                                 |

# An ERP for the Sensex

¨ Inputs for the computation ¤ Sensex on 9/5/07 = 15446 ¤ Dividend yield on index = 3.05% ¤ Expected growth rate - next 5 years = 14% ¤ Growth rate beyond year 5 = 6.76% (set equal to riskfree rate) ¨ Solving for the expected return:

¨ Expected return on stocks = 11.18% ¨ Implied equity risk premium for India = 11.18% - 6.76% = 4.42%

$$15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$$

# Changing Country Risk: Brazil CRP & Total ERP from 2000 to 2016

![](_page_3_Figure_3.jpeg)

*Figure 15: US ERP and Brazil Implied CRP*

# The evolution of Emerging Market Risk

| Start of year | PBV Developed | PBV Emerging | ROE Developed | ROE Emerging | US T.Bond rate | Growth Rate Developed | Growth Rate Emerging | Cost of Equity (Developed) | Cost of Equity (Emerging) | Differential ERP |
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

- ¨ This beta has three problems:
  - It has high standard error
  - It reflects the firms business mix over the period of the regression, not the current mix
  - It reflects the firms average financial leverage over the period rather than the current leverage.

# Unreliable, when it looks bad..

![](_page_7_Figure_2.jpeg)

# Or when it looks good..

![](_page_8_Figure_26.jpeg)

# One slice of history..

**83**

![](_page_9_Figure_2.jpeg)

During this time period, Valeant was a stock under siege, without a CEO, under legal pressure & lacking financials.

![](_page_9_Figure_4.jpeg)

# And subject to game playing

![](_page_10_Figure_2.jpeg)

![](_page_10_Figure_3.jpeg)

### Measuring Relative Risk: You don't like betas or modern portfolio theory? No problem.

![](_page_11_Diagram_2.jpeg)

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

![](_page_14_Diagram_2.jpeg)

In a perfect world… we would estimate the beta of a firm by doing the following

Start with the beta of the business that the firm is in

Adjust the business beta for the operating leverage of the firm to arrive at the unlevered beta for the firm.

Use the financial leverage of the firm to estimate the equity beta for the firm Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (Debt/Equity))

# Adjusting for operating leverage…

¨ Within any business, firms with lower fixed costs (as a percentage of total costs) should have lower unlevered betas. If you can compute fixed and variable costs for each firm in a sector, you can break down the unlevered beta into business and operating leverage components. ¤ Unlevered beta = Pure business beta \* (1 + (Fixed costs/ Variable costs)) ¨ The biggest problem with doing this is informational. It is difficult to get information on fixed and variable costs for individual firms. ¨ In practice, we tend to assume that the operating leverage of firms within a business are similar and use the same unlevered beta for every firm.

# Adjusting for financial leverage...

91

- □ Conventional approach: If we assume that debt carries no market risk (has a beta of zero), the beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_L = \beta_u (1 + ((1-t)D/E))$$

In some versions, the tax effect is ignored and there is no  $(1-t)$  in the equation.

- □ Debt Adjusted Approach: If beta carries market risk and you can estimate the beta of debt, you can estimate the levered beta as follows:

$$\beta_L = \beta_u (1 + ((1-t)D/E)) - \beta_{\text{debt}} (1-t) (D/E)$$

While the latter is more realistic, estimating betas for debt can be difficult to do.

# Bottom-up Betas

Step 1: Find the business or businesses that your firm operates in.

![](_page_18_Diagram_3.jpeg)

Step 2: Find publicly traded firms in each of these businesses and obtain their regression betas. Compute the simple average across these regression betas to arrive at an average beta for these publicly traded firms. Unlever this average beta using the average debt to equity ratio across the publicly traded firms in the sample. Unlevered beta for business = Average beta across publicly traded firms/ (1 + (1- t) (Average D/E ratio across firms))

![](_page_18_Diagram_5.jpeg)

If you can, adjust this beta for differences between your firm and the comparable firms on operating leverage and product characteristics.

Step 3: Estimate how much value your firm derives from each of the different businesses it is in.

![](_page_18_Diagram_7.jpeg)

While revenues or operating income are often used as weights, it is better to try to estimate the value of each business.

Step 4: Compute a weighted average of the unlevered betas of the different businesses (from step 2) using the weights from step 3. Bottom-up Unlevered beta for your firm = Weighted average of the unlevered betas of the individual business

![](_page_18_Diagram_9.jpeg)

Step 5: Compute a levered beta (equity beta) for your firm, using the market debt to equity ratio for your firm. Levered bottom-up beta = Unlevered beta (1+ (1-t) (Debt/Equity)) If you expect the business mix of your firm to change over time, you can change the weights on a year-to-year basis.

If you expect your debt to equity ratio to change over time, the levered beta will change over time.

### *Possible Refinements*

# Why bottom-up betas?

¨ The standard error in a bottom-up beta will be significantly lower than the standard error in a single regression beta. Roughly speaking, the standard error of a bottom-up beta estimate can be written as follows:

Std error of bottom-up beta = 
$$\frac{\text{Average Std Error across Betas}}{\sqrt{\text{Number of firms in sample}}}$$

¨ The bottom-up beta can be adjusted to reflect changes in the firms business mix and financial leverage. Regression betas reflect the past. ¨ You can estimate bottom-up betas even when you do not have historical stock prices. This is the case with initial public offerings, private businesses or divisions of companies.

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

# Embraers Bottom-up Beta

| Business  | Unlevered Beta | D/E Ratio | Levered beta |
|-----------|----------------|-----------|--------------|
| Aerospace | 0.95           | 18.95%    | 1.07         |

- ¨ Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (D/E Ratio) = 0.95 ( 1 + (1-.34) (.1895)) = 1.07 ¨ Can an unlevered beta estimated using U.S. and European aerospace companies be used to estimate the beta for a Brazilian aerospace company?
- a. Yes
- b. No What concerns would you have in making this assumption?

# Gross Debt versus Net Debt Approaches

¨ Analysts in Europe and Latin America often take the difference between debt and cash (net debt) when computing debt ratios and arrive at very different values. ¨ For Embraer, using the gross debt ratio ¤ Gross D/E Ratio for Embraer = 1953/11,042 = 18.95% ¤ Levered Beta using Gross Debt ratio = 1.07 ¨ Using the net debt ratio, we get ¤ Net Debt Ratio for Embraer = (Debt - Cash)/ Market value of Equity = (1953-2320)/ 11,042 = -3.32% ¤ Levered Beta using Net Debt Ratio = 0.95 (1 + (1-.34) (-.0332)) = 0.93 ¨ The cost of Equity using net debt levered beta for Embraer will be much lower than with the gross debt approach. The cost of capital for Embraer will even out since the debt ratio used in the cost of capital equation will now be a net debt ratio rather than a gross debt ratio.

# The Cost of Equity: A Recap

![](_page_23_Diagram_2.jpeg)