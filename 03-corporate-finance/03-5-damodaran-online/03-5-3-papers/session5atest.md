---
title: "Session5Atest"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session5Atest.pdf
---

## **Session 5A: Post Class Test**

- 1. The table below lists the EV to Sales ratio (the multiple of revenues that a company trades at) and the pre-tax operating margins of US beverage companies.

| Company Name                                    | EV/Sales | Pre-tax Operating Margin |
|-------------------------------------------------|----------|--------------------------|
| Coca-Cola Consolidated, Inc. (NasdaqGS:COKE)    | 0.72     | 4.90%                    |
| Jones Soda Co. (OTCPK:JSDA)                     | 1.07     | -24.62%                  |
| NewAge, Inc. (NasdaqCM:NBEV)                    | 1.41     | -20.43%                  |
| MOJO Organics, Inc. (OTCPK:MOJO)                | 1.46     | -4.02%                   |
| Primo Water Corporation (TSX:PRMW)              | 1.69     | 5.67%                    |
| Reed's, Inc. (NasdaqCM:REED)                    | 1.78     | -23.90%                  |
| The Alkaline Water Company Inc. (NasdaqCM:WTER) | 1.84     | -29.93%                  |
| National Beverage Corp. (NasdaqGS:FIZZ)         | 3.60     | 20.19%                   |
| PepsiCo, Inc. (NasdaqGS:PEP)                    | 3.60     | 15.76%                   |
| Keurig Dr Pepper Inc. (NasdaqGS:KDP)            | 5.36     | 24.52%                   |
| The Coca-Cola Company (NYSE:KO)                 | 7.48     | 29.33%                   |
| Monster Beverage Corporation (NasdaqGS:MNST)    | 11.37    | 34.98%                   |
| Greene Concepts, Inc. (OTCPK:INKW)              | 28.99    | 60.55%                   |

- a. Estimate the correlation and covariance between EV to Sales ratios and operating margins.
- b. If you are an investor looking at this data, which one of these will you make your dependent variable and which one your independent variable. Why?
- c. Create a scatter plot of your dependent and independent variables.
- d. Run a regression of your dependent variable against your independent variable.
- e. Use the regression to get predicted values for your dependent variable for each company. How would you use it as an investor?
- f. What are your concerns (statistical) about using this regression?
- 2. The dataset below contains data on the PBV ratios and returns on equity (ROE) of insurance companies: http://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/USInsurance2020.xlsx
  - a. Estimate the correlation and covariance between PBV and ROE
  - b. Create a scatter plot of PBV and ROE.
  - c. Run a regression of PBV against ROE
  - d. Run the diagnostics on your regression residuals.
- 3. The dataset below contains data on the earnings yield. T. Bond rates and the unexpected inflation from 1960 to 2020: http://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/StocksvsBonds2020.xls x
  - a. Estimate the correlation matrix for earnings yield, T.Bond rates and unexpected inflation.
  - b. Run a regression of earnings yield against T.Bond rates and unexpected inflation.

- c. Review the regression for statistical significance.
- d. What does the regression output tell you about the relationship between earnings yield, T.Bond rates and unexpected inflation.

4. The following is output from a multiple regression of EV to Invested Capital Ratios of US companies against three independent variables: the effective tax rate, the return on invested capital and the debt ratios, for global companies in 2021.

### Model Summary

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .409 <sup>a</sup> | .167     | .167              | 1.71770677                 |

a. Predictors: (Constant), Market Debt to capital ratio, Effective Tax Rate, Return on Capital (ROC or ROIC)

### ANOVA<sup>a</sup>

| Model | Sum of Squares | df         | Mean Square | F        | Sig.              |
|-------|----------------|------------|-------------|----------|-------------------|
| 1     | 19271.202      | 3          | 6423.734    | 2177.156 | .000 <sup>b</sup> |
|       | Residual       | 32503      | 2.951       |          |                   |
|       | Total          | 115171.841 | 32506       |          |                   |

a. Dependent Variable: EV/Invested Capital

b. Predictors: (Constant), Market Debt to capital ratio, Effective Tax Rate, Return on Capital (ROC or ROIC)

### Coefficients<sup>a</sup>

| Model | Unstandardized Coefficients     |            | Standardized Coefficients<br>Beta | t       | Sig.    |      |
|-------|---------------------------------|------------|-----------------------------------|---------|---------|------|
|       | B                               | Std. Error |                                   |         |         |      |
| 1     | (Constant)                      | 2.970      | .017                              | 174.879 | .000    |      |
|       | Return on Capital (ROC or ROIC) | .009       | .001                              | .083    | <.001   |      |
|       | Effective Tax Rate              | -.008      | .001                              | -.068   | <.001   |      |
|       | Market Debt to capital ratio    | -.028      | .000                              | -.394   | -77.329 | .000 |

a. Dependent Variable: EV/Invested Capital

- a. Assess the statistical significance of this regression.
- b. What are some of the questions that you might have about this regression (how it was run, missing companies, etc.), before using it?

5. Using the regression in the last problem, you decide to assess its statistical reliability.

- a. The correlation between the three independent variables is in the table below. How would you use it in evaluating your regression?