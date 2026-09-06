---
title: "Session5Asoln"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session5Asoln.pdf
---

### **Session 5A: Post Class Test Solutions**

### 1. a. Correlation

| <span> </span>           | <i>EV/Sales</i> | <i>Pre-tax Operating Margin</i> |
|--------------------------|-----------------|---------------------------------|
| EV/Sales                 | 1.0000          |                                 |
| Pre-tax Operating Margin | 0.7866          | 1.0000                          |

### Covariance

|                          | <i>EV/Sales</i> | <i>Pre-tax Operating Margin</i> |
|--------------------------|-----------------|---------------------------------|
| EV/Sales                 | 54.9521286      |                                 |
| Pre-tax Operating Margin | 1.52622042      | 0.06849944                      |

EV to Sales and operating margin move together; when one is high, the other is as well.

As an investor, I am interested in buying cheap companies, and am looking for those that trade at low EV to Sales ratios. That, therefore, becomes my dependent variable, with operating margin becoming the variable that I hope to use to explain it.

### *Scatter Plot*

*Regression output*

![](_page_0_Figure_9.jpeg)

**Scatter plot (Pearson R = 0.78665, N = 13)**

| <i>Regression Statistics</i> |                     |                         |               |                |                       |                  |                    |                    |
|------------------------------|---------------------|-------------------------|---------------|----------------|-----------------------|------------------|--------------------|--------------------|
| Multiple R                   | 0.78664989          |                         |               |                |                       |                  |                    |                    |
| R Square                     | 0.61881805          |                         |               |                |                       |                  |                    |                    |
| Adjusted R S                 | 0.58416515          |                         |               |                |                       |                  |                    |                    |
| Standard Err                 | 4.97546594          |                         |               |                |                       |                  |                    |                    |
| Observations                 | 13                  |                         |               |                |                       |                  |                    |                    |
|                              |                     |                         |               |                |                       |                  |                    |                    |
| ANOVA                        |                     |                         |               |                |                       |                  |                    |                    |
|                              | <i>df</i>           | <i>SS</i>               | <i>MS</i>     | <i>F</i>       | <i>Significance F</i> |                  |                    |                    |
| Regression                   | 1                   | 442.069798              | 442.069798    | 0.18576099     | 0.00142237            |                  |                    |                    |
| Residual                     | 11                  | 272.307874              | 242.7552613   |                |                       |                  |                    |                    |
| Total                        | 12                  | 714.377672              |               |                |                       |                  |                    |                    |
|                              |                     |                         |               |                |                       |                  |                    |                    |
|                              |                     |                         |               |                |                       |                  |                    |                    |
|                              | <i>Coefficients</i> | <i>t Standard Error</i> | <i>t Stat</i> | <i>P-value</i> | <i>Lower 95%</i>      | <i>Upper 95%</i> | <i>Lower 95.0%</i> | <i>Upper 95.0%</i> |
| Intercept                    | 3.81981681          | 1.43057608              | 2.67012489    | 0.02178915     | 0.67114008            | 6.96849355       | 0.67114008         | 6.96849355         |
| Pre-tax Oper                 | 22.2807719          | 2.57252403              | 42.2582653    | 0.00142237     | 10.6760248            | 33.8855191       | 10.6760248         | 33.8855191         |

### *Predicted versus Actual EV/Sales*

| Company Name                                    | EV/Sales | Pre-tax Operating Margin | Predicted EV/Sales | Residual |
|-------------------------------------------------|----------|--------------------------|--------------------|----------|
| Coca-Cola Consolidated, Inc. (NasdaqGS:COKE)    | 0.72     | 4.90%                    |                    |          |
|                                                 |          |                          | 4.91               | 4.19     |
| Jones Soda Co. (OTCPK:JSDA)                     | 1.07     | -24.62%                  | -1.67              | -2.74    |
| NewAge, Inc. (NasdaqCM:NBEV)                    | 1.41     | -20.43%                  | -0.73              | -2.14    |
| MOJO Organics, Inc. (OTCPK:MOJO)                | 1.46     | -4.02%                   | 2.92               | 1.46     |
| Primo Water Corporation (TSX:PRMW)              | 1.69     | 5.67%                    | 5.08               | 3.40     |
| Reed's, Inc. (NasdaqCM:REED)                    | 1.78     | -23.90%                  | -1.51              | -3.29    |
| The Alkaline Water Company Inc. (NasdaqCM:WTER) | 1.84     | -29.93%                  |                    |          |
|                                                 |          |                          | -2.85              | -4.69    |
| National Beverage Corp. (NasdaqGS:FIZZ)         | 3.60     | 20.19%                   |                    |          |
|                                                 |          |                          | 8.32               | 4.72     |
| PepsiCo, Inc. (NasdaqGS:PEP)                    | 3.60     | 15.76%                   | 7.33               | 3.73     |
| Keurig Dr Pepper Inc. (NasdaqGS:KDP)            | 5.36     | 24.52%                   | 9.28               | 3.92     |
| The Coca-Cola Company (NYSE:KO)                 | 7.48     | 29.33%                   | 10.36              | 2.88     |
| Monster Beverage Corporation (NasdaqGS:MNST)    | 11.37    | 34.98%                   |                    |          |
|                                                 |          |                          | 11.61              | 0.24     |
| Greene Concepts, Inc. (OTCPK:INKW)              | 28.99    | 60.55%                   | 17.31              | -11.68   |

The companies that have actual EV/Sales that are lowest, relative to their predicted values, are cheap.

# *Concerns*

- Small sample size with outliers
- Scatter plot suggests relationship between EV to Sales and margin is non-linear

- Residuals are not normally distributed

2. The results of the analysis of PBV against ROE are below.

| Correlation               |         |                  | Covariance |         |       |
|---------------------------|---------|------------------|------------|---------|-------|
| R                         | PBV     | Return on Equity |            |         |       |
| <b>PBV</b>                | 1       |                  |            |         |       |
| <i>R Std Err</i>          |         |                  |            |         |       |
| <i>t</i>                  |         |                  |            |         |       |
| <i>p-value (2-tailed)</i> |         |                  |            |         |       |
| <b>Return on Equity</b>   | 0.08724 | 1                |            |         |       |
| <i>R Std Err</i>          | 0.01196 |                  |            |         |       |
| <i>t</i>                  | 0.79784 |                  |            |         |       |
| <i>p-value (2-tailed)</i> | 0.42724 |                  |            | 0.06152 | 0.038 |

The correlation is a positive number, but it is not statistically significant.

## *Regression*

| Regression Statistics |                     |                       |               |                |                       |                  |                    |                    |
|-----------------------|---------------------|-----------------------|---------------|----------------|-----------------------|------------------|--------------------|--------------------|
| Multiple R            | 0.087240798         |                       |               |                |                       |                  |                    |                    |
| R Square              | 0.007610957         |                       |               |                |                       |                  |                    |                    |
| Adjusted R Square     | -0.004345538        |                       |               |                |                       |                  |                    |                    |
| Standard Error        | 3.649494546         |                       |               |                |                       |                  |                    |                    |
| Observations          | 85                  |                       |               |                |                       |                  |                    |                    |
|                       |                     |                       |               |                |                       |                  |                    |                    |
|                       |                     |                       |               |                |                       |                  |                    |                    |
| ANOVA                 |                     |                       |               |                |                       |                  |                    |                    |
|                       | <i>df</i>           | <i>SS</i>             | <i>MS</i>     | <i>F</i>       | <i>Significance F</i> |                  |                    |                    |
| Regression            | 1                   | 8.466305293           | 8.466305293   | 0.636554205    | 0.427238101           |                  |                    |                    |
| Residual              | 83                  | 1103.91752            | 13.30021109   |                |                       |                  |                    |                    |
| Total                 | 84                  | 1112.382825           |               |                |                       |                  |                    |                    |
|                       |                     |                       |               |                |                       |                  |                    |                    |
|                       |                     |                       |               |                |                       |                  |                    |                    |
|                       | <i>Oecoficients</i> | <i>Standard Error</i> | <i>t Stat</i> | <i>P-value</i> | <i>Lower 95%</i>      | <i>Upper 95%</i> | <i>Lower 95.0%</i> | <i>Upper 95.0%</i> |
| Intercept             | 1.923830564         | 0.398333802           | 4.829694479   | 6.16718E-06    | 1.131560653           | 2.761004075      | 1.131560653        | 2.761004075        |
| Root on Equity        | 1.618985596         | 2.029202492           | 0.079844371   | 0.427238101    | -2.417061682          | 5.654988102      | -2.417061682       | 5.654988102        |

The regression has minimal explanatory power, with the F statistic, t statistic and p value all indicating that ROE does not do a good job explaining differences in PBV ratios across insurance companies.

# *Residual Analysis*

## **Breusch-Pagan-Godfrey (BPG) test**

| <i>Test Statistic</i> | 0.0181  | <i>p</i> -value | 0.89298 | <i>H0</i> (5%) |
|-----------------------|---------|-----------------|---------|----------------|
| <i>F</i>              | 0.01768 | <i>p</i> -value | 0.89455 |                |

## **White test (All cross-terms)**

| <i>Test Statistic</i> | 0.18819 | <i>p</i> -value | 0.9102  | <i>H0</i> (5%) |
|-----------------------|---------|-----------------|---------|----------------|
| <i>F</i>              | 0.09097 | <i>p</i> -value | 0.91313 |                |

![](_page_2_Figure_1.jpeg)

### **Normality Tests**

| Test                            | Test Statistic | p-value | H0 (5%)       |
|---------------------------------|----------------|---------|---------------|
| Shapiro-Wilk W                  | 0.39315        | 0.      | Rejected      |
| Shapiro-Francia                 | 0.37605        | 0.      | Rejected      |
| Anderson-Darling                | 15.34855       | 0.      | Rejected      |
| Cramer-von Mises                | 3.09441        | 0.355   | Cannot reject |
| Kolmogorov-Smirnov (Lilliefors) | 0.32065        | 0.      | Rejected      |
| D'Agostino Skewness             | 9.63576        | 0       | Rejected      |
| D'Agostino Kurtosis             | 7.17728        | 0.      | Rejected      |
| D'Agostino Omnibus              | 144.36117      | 0       | Rejected      |
| Jarque-Bera                     | 7,250.3238     | 0       | Rejected      |

![](_page_3_Figure_3.jpeg)

**Histogram for "Residuals"**

![](_page_3_Figure_5.jpeg)

**Normal Q-Q Plot - Residuals**

The residuals are not normally distributed, and there seems to be heteroskedasticity.

- 3. The results of the EP ratio against interest rates and unexpected inflation are below: *Correlation*

| R Earnings Yield R Std Err t p-value (2-tailed) | Earnings Yield 1 | T.Bond Rate | Unexpected Inflation |
|-------------------------------------------------|------------------|-------------|----------------------|
| T.Bond Rate                                     | 0.63253          | 1           |                      |
| R Std Err                                       | 0.01017          |             |                      |
| t                                               | 6.27285          |             |                      |
| p-value (2-tailed)                              | 4.53895E-8       |             |                      |
| Unexpected Inflation                            | 0.37748          | 0.05497     | 1                    |
| R Std Err                                       | 0.01453          | 0.0169      |                      |
| t                                               | 3.13114          | 0.42284     |                      |

Earnings yield is positively correlated with both the T.Bond rate and unexpected inflation. In other words, the EP ratio is higher (or PE ratio is lower) when interest rates are high and inflation is higher than expected. Both pass the statistical significant test (t statistics are 6.27 and 3.13), but the T.Bond rate is more strongly correlated with Earnings Yield. *Regression*

![](_page_4_Figure_0.jpeg)

| SUMMARY OUTPUT               |                     |                        |               |                |                       |                  |                    |                    |
|------------------------------|---------------------|------------------------|---------------|----------------|-----------------------|------------------|--------------------|--------------------|
|                              |                     |                        |               |                |                       |                  |                    |                    |
| <i>Regression Statistics</i> |                     |                        |               |                |                       |                  |                    |                    |
| Multiple R                   | 0.71965384          |                        |               |                |                       |                  |                    |                    |
| R Square                     | 0.51790165          |                        |               |                |                       |                  |                    |                    |
| Adjusted R S                 | 0.50127757          |                        |               |                |                       |                  |                    |                    |
| Standard Err                 | 0.01724931          |                        |               |                |                       |                  |                    |                    |
| Observations                 | 61                  |                        |               |                |                       |                  |                    |                    |
|                              |                     |                        |               |                |                       |                  |                    |                    |
| ANOVA                        |                     |                        |               |                |                       |                  |                    |                    |
|                              | <i>df</i>           | <i>SS</i>              | <i>MS</i>     | <i>F</i>       | <i>Significance F</i> |                  |                    |                    |
| Regression                   | 2                   | 0.01853886             | 0.00926943    | 31.1537013     | 6.4704E-10            |                  |                    |                    |
| Residual                     | 58                  | 0.01725725             | 0.00029754    |                |                       |                  |                    |                    |
| Total                        | 60                  | 0.03579611             |               |                |                       |                  |                    |                    |
|                              |                     |                        |               |                |                       |                  |                    |                    |
|                              | <i>Coefficients</i> | <i>t Standard Erro</i> | <i>t Stat</i> | <i>P-value</i> | <i>Lower 95%</i>      | <i>Upper 95%</i> | <i>Lower 95.0%</i> | <i>Upper 95.0%</i> |
| Intercept                    | 0.03551289          | 0.00495921             | 7.160099208   | 1.5724E-09     | 0.02558595            | 0.04543983       | 0.02558595         | 0.04543983         |
| T.Bond Rate                  | 0.51434788          | 0.07653463             | 6.72045966    | 8.6275E-09     | 0.36114717            | 0.66754858       | 0.36114717         | 0.66754858         |
| Unexpected                   | 0.33342095          | 0.08856432             | 3.7647322     | 0.00039126     | 0.1561402             | 0.51070169       | 0.1561402          | 0.51070169         |

The F value suggests that the multiple regression has strong explanatory power, and the t statistics and p values on the two variables (T.Bond rate and Unexpected inflation) backs up the proposition that both variables are adding significant explanatory power. The R-squared, not surprisingly, is solid 0.51, and since the sample size is decent (60 years), the adjusted R-squared is very similar.

Stocks are priced higher, when interest rates are low and when inflation comes in below expectations, and lower, when the interest rates are high and inflation is higher than expected.

## **4.**

- The F value indicates that the multiple regression has strong explanatory power, and the t statistics (p values) suggest that each variable adds to that explanatory power significantly. You may be surprised that, given these findings, the R-squared is only 16.7%, but that seeming contradiction can be explained by the large sample size (>30,000 firms). With a sample that large, a low R-squared and statistical significance can go together.
- The low R-squared indicates that even though the regression has statistical power, the predictions based upon the regression will come with large standard error, yielding a wide range for the predicted value. That said, here are some of the questions I would have:

- c. This is a linear regression. Did you check, with a scatter plot, for the linearity assumption?
- 4. How correlated are the independent variables, with each other?
- e. Do the residuals pass the normality and homoskedasticity tests?

5.

- There is clearly multicollinearity in the data. Effective tax rates are positively correlated with both return on capital and debt ratios and return on capital is negatively correlated with debt ratios. I could look for other measures of tax rates that are less correlated or remove it entirely, but from an overall predictive value basis, I feel that it is better to leave the variables in the regression, not read too much into the individual coefficients, but use the overall regression to make predictions.
- The residuals also have a mild positive skew, violating the normality assumption. It does indicate that using this regression to make forecasts will yield more over estimation than under estimation errors, but not by enough to redo or tweak the regression.