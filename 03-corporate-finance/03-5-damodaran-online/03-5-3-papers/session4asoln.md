---
title: "Session4Asoln"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session4Asoln.pdf
---

## **Session 4A: Post Class Test Solutions**

- 1. A visual check of the normal distribution suggests that it is a good fit, and the same holds true for the Q-Q plot, where the points are close to the line. If you want more confirmation, you can run statistical tests to check to see whether you can reject the normality assumption:

| Skewness                      | 0.27289 | <i>Fisher's Skewness G1</i> | 0.27739        |                |
|-------------------------------|---------|-----------------------------|----------------|----------------|
| Kurtosis                      | 3.55057 |                             |                |                |
| Kurtosis Excess (-3)          | 0.55057 | <i>Fisher's Kurtosis G2</i> | 0.64876        |                |
|                               |         |                             |                |                |
| Test                          |         | <i>Test Statistic</i>       | <i>p-value</i> | <i>H0 (5%)</i> |
| Shapiro-Wilk W                |         | 0.984                       | 0.35116        | Cannot reject  |
| Shapiro-Francia               |         | 0.98039                     | 0.1535         | Cannot reject  |
| Anderson-Darling              |         | 0.43722                     | 0.29027        | Cannot reject  |
| Cramer-von Mises              |         | 0.06375                     | 0.33429        | Cannot reject  |
| Kolmogorov-Smimov (Liliefors) |         | 0.06166                     | 0.51858        | Cannot reject  |
| D'Agostino Skewness           |         | 1.13164                     | 0.25779        | Cannot reject  |
| D'Agostino Kurtosis           |         | 1.29782                     | 0.19435        | Cannot reject  |
| D'Agostino Omnibus            |         | 2.96495                     | 0.22708        | Cannot reject  |
| Jarue-Bera                    |         | 2.32893                     | 0.31209        | Cannot reject  |

Starting with the simplest tests, the skewness is close to zero and the kurtosis is close to three, conforming to the normal distribution. The other tests range the spectrum, but they all come to the same conclusion, which is that the data is close to normally distributed.

- 2. Applying the normality tests to software company operating margins, here is what I get:

| Skewness             | -0.8159 | Fisher's Skewness G1 | -0.82096 |
|----------------------|---------|----------------------|----------|
| Kurtosis             | 4.31006 |                      |          |
| Kurtosis Excess (-3) | 1.31006 | Fisher's Kurtosis G2 | 1.36231  |

| Test                            | Test Statistic | p-value     | H0 (5%)  |
|---------------------------------|----------------|-------------|----------|
| Shapiro-Wilk W                  | 0.95769        | 1.39558E-6  | Rejected |
| Shapiro-Francia                 | 0.95645        | 4.10772E-6  | Rejected |
| Anderson-Darling                | 2.70102        | 8.00619E-7  | Rejected |
| Cramer-von Mises                | 0.45021        | 8.08769E-6  | Rejected |
| Kolmogorov-Smirnov (Lilliefors) | 0.14616        | 0.00002     | Rejected |
| D'Agostino Skewness             | 4.7588         | 1.94747E-6  | Rejected |
| D'Agostino Kurtosis             | 3.00615        | 0.00265     | Rejected |
| D'Agostino Omnibus              | 31.6831        | 1.31856E-7  | Rejected |
| Jarque-Bera                     | 44.52046       | 2.15033E-10 | Rejected |

![](_page_0_Figure_8.jpeg)

**Histogram for "Pre-tax Operating Margin"**

The distribution is too skewed (negatively) and has too many extreme values to fit the normal distribution. I would look for a distribution that allows for both features (negative skewness and fatter tails); the *minimum extreme value distribution*, with a tweaking of the parameters may work.

3. Applying the normality tests to utility company dividend yields, here is what I get:

| Skewness             | 1.69002  | Fisher's Skewness G1 | 1.73778 |
|----------------------|----------|----------------------|---------|
| Kurtosis             | 10.16989 |                      |         |
| Kurtosis Excess (-3) | 7.16989  | Fisher's Kurtosis G2 | 7.98467 |

| Test                            | Test Statistic | p-value    | H0 (5%)  |
|---------------------------------|----------------|------------|----------|
| Shapiro-Wilk W                  | 0.82099        | 1.1192E-6  | Rejected |
| Shapiro-Francia                 | 0.80864        | 3.15251E-6 | Rejected |
| Anderson-Darling                | 2.06064        | 0.00003    | Rejected |
| Cramer-von Mises                | 0.31065        | 0.00023    | Rejected |
| Kolmogorov-Smirnov (Lilliefors) | 0.15918        | 0.00136    | Rejected |
| D'Agostino Skewness             | 4.31116        | 0.00002    | Rejected |
| D'Agostino Kurtosis             | 4.24321        | 0.00002    | Rejected |
| D'Agostino Omnibus              | 36.5909        | 1.13341E-8 | Rejected |
| Jarque-Bera                     | 143.99008      | 0          | Rejected |

![](_page_1_Figure_1.jpeg)

**Normal Q-Q Plot - Pre-tax Operating Margin**

The distribution has too much of a positive skew, and much fatter tails than a normal distribution. The lognormal or gamma distributions both can be constructed to have positive skew, but the *log normal distribution* allows for fatter tails.

- 4. Applying the normality tests to CPI data, here is what I get:

*Skewness* 0.35153 *Fisher's Skewness G1* 0.35732

*Kurtosis* 6.8239

![](_page_2_Figure_1.jpeg)

**Histogram for "Dividend Yield"**

![](_page_2_Figure_3.jpeg)

**Normal Q-Q Plot - Dividend Yield**

| Kurtosis Excess (-3)            | 3.8239 Fisher's Kurtosis G2 | 4.10514     |               |
|---------------------------------|-----------------------------|-------------|---------------|
| Test                            | Test Statistic              | p-value     | H0 (5%)       |
| Shapiro-Wilk W                  | 0.87737                     | 3.15312E-7  | Rejected      |
| Shapiro-Francia                 | 0.86581                     | 7.72667E-7  | Rejected      |
| Anderson-Darling                | 4.19658                     | 1.64031E-10 | Rejected      |
| Cramer-von Mises                | 0.78171                     | 1.72686E-8  | Rejected      |
| Kolmogorov-Smirnov (Lilliefors) | 0.16694                     | 9.87804E-7  | Rejected      |
| D'Agostino Skewness             | 1.44462                     | 0.14856     | Cannot reject |
| D'Agostino Kurtosis             | 3.80121                     | 0.00014     | Rejected      |
| D'Agostino Omnibus              | 16.5361                     | 0.00026     | Rejected      |
| Jarque-Bera                     | 58.5765                     | 0.          | Rejected      |

![](_page_3_Figure_2.jpeg)

**Histogram for "Actual Inflation Rate"**

![](_page_3_Figure_4.jpeg)

**Normal Q-Q Plot - Actual Inflation Rate**

The distribution looks close to symmetric (skewness is close to zero), but it has fatter tails (and a more pronounced peak) than a normal distribution. A Cauchy distribution, which resembles a normal distribution but allows for fatter tails, may be a better fit.

5. Applying the normality tests to bank PBV data, here is what I get:

| Skewness             | 3.94228  | Fisher's Skewness G1 | 3.95452  |
|----------------------|----------|----------------------|----------|
| Kurtosis             | 31.25424 |                      |          |
| Kurtosis Excess (-3) | 28.25424 | Fisher's Kurtosis G2 | 28.56017 |

| Test                            | Test Statistic | p-value     | H0 (5%)       |
|---------------------------------|----------------|-------------|---------------|
| Shapiro-Wilk W                  | 0.71032        | 0.          | Rejected      |
| Shapiro-Francia                 | 0.70489        | 0           | Rejected      |
| Anderson-Darling                | INF            | 0.          | Rejected      |
| Cramer-von Mises                | 5.18549        | 2.80957E+73 | Cannot reject |
| Kolmogorov-Smirnov (Lilliefors) | 0.36853        | 0.          | Rejected      |
| D'Agostino Skewness             | 17.19508       | 0           | Rejected      |
| D'Agostino Kurtosis             | 12.4563        | 0           | Rejected      |
| D'Agostino Omnibus              | 450.83024      | 0           | Rejected      |
| Jarque-Bera                     | 17,388.62635   | 0           | Rejected      |

![](_page_4_Figure_5.jpeg)

**Histogram for "PBV"**

![](_page_4_Figure_7.jpeg)

**Normal Q-Q Plot - PBV**