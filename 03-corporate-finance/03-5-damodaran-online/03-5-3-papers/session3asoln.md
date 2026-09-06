---
title: "Session3Asoln"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session3Asoln.pdf
---

## **Session 3A: Post Class Test Solutions**

1. See table below for calculations:

|               | S&P 500 | 10-yr T.Bond | S&P 500: Squared Difference | T.Bond: Squared Difference |
|---------------|---------|--------------|-----------------------------|----------------------------|
| 2010          | 14.82%  | 8.46%        | 0.000019                    | 0.001209                   |
| 2011          | 2.10%   | 16.04%       | 0.015096                    | 0.012210                   |
| 2012          | 15.89%  | 2.97%        | 0.000227                    | 0.000406                   |
| 2013          | 32.15%  | -9.10%       | 0.031542                    | 0.019853                   |
| 2014          | 13.52%  | 10.75%       | 0.000074                    | 0.003319                   |
| 2015          | 1.38%   | 1.28%        | 0.016916                    | 0.001370                   |
| 2016          | 11.77%  | 0.69%        | 0.000682                    | 0.001845                   |
| 2017          | 21.61%  | 2.80%        | 0.005213                    | 0.000477                   |
| 2018          | -4.23%  | -0.02%       | 0.034640                    | 0.002502                   |
| 2019          | 31.21%  | 9.64%        | 0.028313                    | 0.002163                   |
| 2020          | 18.01%  | 11.33%       | 0.001317                    | 0.004028                   |
| Sum           | 158.24% | 54.84%       | 0.134040                    | 0.049380                   |
| Average       | 14.39%  | 4.99%        |                             |                            |
| Median        | 14.82%  | 2.97%        |                             |                            |
| Variance      |         |              | 0.0134                      | 0.0049                     |
| Std Deviation |         |              | 11.58%                      | 7.03%                      |

Using the Excel function for standard deviation (STDEV) delivers the same result.

2. Using the excel functions on the operating margin data, here is what I get:

| Average = | -6.96% | Median = | -2.16% |
|-----------|--------|----------|--------|
|           |        |          |        |

| Highest = | 65.42% | Variance = | 0.06852272 |
|-----------|--------|------------|------------|
|           |        |            |            |

| Lowest = | -99.54% | Std Dev = | 26.18% |
|----------|---------|-----------|--------|
|          |         |           |        |

| Range = | 164.96%       |               |               |
|---------|---------------|---------------|---------------|
|         | <span></span> | <span></span> | <span></span> |

| Skewness = | -0.8209591 |
|------------|------------|
|            |            |

| Kurtosis = | 1.36230991 |
|------------|------------|
|            |            |

The typical software company lost money, on an operating basis, in 2020; both the average and the median are negative. There is substantial variability across companies in margins, with both the range and standard deviation reflecting that variability. The data series is negatively skewed (the outliers are bigger on the negative side), perhaps because margins are constrained to be less than 100%. That explains why the average is higher (less negative) than the median.

To compute the squared difference, I revert to decimals. In 2010, for the S&P 500: (.1482- .1439)2 = .000019

To get the median, I listed the returns for the S&P 500 and the T.Bond from lowest to highest and picked the 6th highest or lowest. If the sample size had been an even number (say 10), I would have picked the middle two numbers (5th and 6th) and averaged them.

To get the variance, I divide the sum of the squared differences by 10 (n minus 1).

- 3. Using the excel functions on the dividend yield data, here is what I get:

| Average = | 3.08% | Median = | 3.37% |
|-----------|-------|----------|-------|
|-----------|-------|----------|-------|

| Highest = | 14.02% | Variance = | 0.00054264 |
|-----------|--------|------------|------------|
| Lowest =  | 0.00%  | Std Dev =  | 2.33%      |
| Range =   | 14.02% |            |            |

|  | <b>Skewness =</b> | <b>1.73778083</b> |
|--|-------------------|-------------------|
|  | <b>Kurtosis =</b> | <b>7.98466897</b> |

Of the 56 utility companies in the sample, 11 paid no dividends, and the average (median) dividend yield across all companies, including the non-dividend paying ones, is 3.08% (3.37%). The variation in dividend yields is low, notwithstanding the range (which is high because the 14.02% is an outlier); the standard deviation is only 2.33%. The data series is positive skewed (the outliers are bigger on the positive side), perhaps because yields cannot be lower than zero. That explains why the average is lower than the median.

- 4. Using the excel functions on the inflation time series data, here is what I get:

| <span></span> | <span></span> | <span></span> | <span></span> |
|---------------|---------------|---------------|---------------|
| Average =     | 3.03%         | Median =      | 2.68%         |

| Highest = | 18.13%  | Variance = | 0.00156999 |
|-----------|---------|------------|------------|
| Lowest =  | -10.27% | Std Dev =  | 3.96%      |
| Range =   | 28.41%  |            |            |

| Skewness = | 0.35731917 |  |  |
|------------|------------|--|--|
| Kurtosis = | 4.10514047 |  |  |

Between 1928 and 2020, the inflation rate averaged 3.03% a year, in the US. In half the years, inflation exceeded 2.68% (the median) and in the other half, it was lower than 2.68%. The variation is again low, but the range is pushed out by a few outliers. The data is close to symmetric (the skewness is only 0.357).

- 5. Using the excel functions on the inflation time series data, here is what I get:

| <b>Average =</b> | <b>1.01</b> | <b>Median =</b> | <b>0.93</b> |
|------------------|-------------|-----------------|-------------|

| Highest = | 4.91 | Variance = | 0.1426 |
|-----------|------|------------|--------|
| Lowest =  | 0.42 | Std Dev =  | 0.3777 |
| Range =   | 4.48 |            |        |

| Skewness = | 3.95451882 |
|------------|------------|
| Kurtosis = | 28.5601684 |

The typical US bank traded at roughly book value (price to book is close to one) in 2020, since the average price to book ratio is 1.03 with the median being 0.93. Across the sample, there are banks that trade at much higher and lower values, with the range from 4.91 at the high end to 0.42 at the low end. The price to book ratio is bounded at zero, yielding a positive skewness, and the outliers are significantly beyond what you would expect if the distribution had "normal" tails.