---
title: "Earnmult"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/earnmult.pdf
---

# I. PE RATIOS

- ■ To understand the fundamentals, start with a basic equity discounted cash flow model.

- - ■ With the dividend discount model, 
    $$P_0 = \frac{\text{DPS}_1}{r - g_n}$$

- - ■ Dividing both sides by the current earnings per share,

$$\frac{P_0}{\text{EPS}_0} = \text{PE} = \frac{\text{Payout Ratio} * (1 + g_n)}{r - g_n}$$

- ■ If you believe **that companies don't pay out what they can**:

$$P_0 = \frac{\text{FCFE}_1}{r - g_n} \quad \frac{P_0}{\text{EPS}_0} = \text{PE} = \frac{(\text{FCFE/Earnings}) * (1 + g_n)}{r - g_n}$$

# USING THE FUNDAMENTAL MODEL TO ESTIMATE PE FOR A HIGH GROWTH FIRM

- The price-earnings ratio for a high growth firm can also be related to fundamentals. In the **special case of the two-stage dividend discount model**, this relationship can be made explicit fairly simply:

$$P_0 = \frac{\text{EPS}_0 * \text{Payout Ratio} * (1+g) * \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{r-g} + \frac{\text{EPS}_0 * \text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{(r-g_n)(1+r)^n}$$

- For a firm that **does not pay what it can afford to in dividends**, substitute FCFE/Earnings for the payout ratio.
- Dividing both sides by the earnings per share:

$$\frac{P_0}{\text{EPS}_0} = \frac{\text{Payout Ratio} * (1+g) * \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{r-g} + \frac{\text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{(r-g_n)(1+r)^n}$$

# A SIMPLE EXAMPLE

- Assume that you have been asked to estimate the PE ratio for a firm which has the following characteristics:

| Variable             | High Growth | Stable Growth              |
|----------------------|-------------|----------------------------|
| Expected Growth Rate | 15%         | 1.5%                       |
| Payout Ratio         | 25%         | 92.5% (based on ROE = 20%) |
| Beta                 | 1.00        | 1.00                       |
| Number of years      | 5 years     | Forever after year 5       |

- Riskfree rate = Treasury Bond Rate = 1.5%, ERP = 5%
- Required rate of return =  $1.5\% + 1(5\%) = 6.5\%$

$$PE = \frac{.25 * 1.15 * \left(1 - \frac{1.15^5}{1.065^5}\right)}{(.065 - .15)} + \frac{.925 * 1.15^5 * (1.015)}{(.065 - .015)(1.065)^5} = 29.15$$

# A. PE, GROWTH AND INTEREST RATES

As interest rates rise, holding all else constant, PE ratios drop, but they drop by more for high growth stocks than low growth stocks.

|                                        |        | Riskfree Rate |         |         |         |         | % Change as rate goes from 0% to 6% |
|----------------------------------------|--------|---------------|---------|---------|---------|---------|-------------------------------------|
|                                        |        | 0.00%         | 1.50%   | 3.00%   | 4.50%   | 6.00%   |                                     |
| Expected Growth Rate - Next 5 years    | 0.00%  | 20.00         | 17.86   | 15.91   | 14.13   | 12.50   | 37.50%                              |
|                                        | 3.00%  | 22.18         | 19.74   | 17.51   | 15.48   | 13.62   | 38.59%                              |
|                                        | 6.00%  | 24.57         | 21.79   | 19.26   | 16.95   | 14.84   | 39.60%                              |
|                                        | 9.00%  | 27.19         | 24.04   | 21.16   | 18.54   | 16.16   | 40.57%                              |
|                                        | 12.00% | 30.05         | 26.49   | 23.24   | 20.27   | 17.38   | 42.16%                              |
|                                        | 15.00% | 33.17         | 29.15   | 25.48   | 22.15   | 19.11   | 42.39%                              |
|                                        | 18.00% | 36.57         | 32.04   | 27.92   | 24.17   | 20.75   | 43.26%                              |
|                                        | 21.00% | 40.25         | 35.18   | 30.55   | 26.35   | 22.52   | 44.05%                              |
|                                        | 24.00% | 44.25         | 38.56   | 33.39   | 28.69   | 24.41   | 44.84%                              |
|                                        | 27.00% | 48.56         | 42.22   | 36.45   | 31.20   | 26.43   | 45.57%                              |
| 30.00%                                 | 53.22  | 46.16         | 39.74   | 33.90   | 28.58   | 46.30%  |                                     |
| % Change as growth goes from 0% to 30% |        | 166.10%       | 158.45% | 149.78% | 139.92% | 128.64% |                                     |

Earnings growth surprises have a much bigger impact on PE ratios, when interest rates are low, than high.

# B. PE AND RISK: A FOLLOW UP EXAMPLE

![](_page_4_Picture_14.jpeg)

## Growth Augmentation

If a firm can increase growth, it should see a payoff in higher PE

## Superstars

Combination of low risk and high growth

|      |      | Expected Growth Rate next 5 years |        |        |        |        |
|------|------|-----------------------------------|--------|--------|--------|--------|
|      |      | 5.00%                             | 10.00% | 15.00% | 20.00% | 25.00% |
| Beta | 0.50 | 43.26                             | 52.68  | 63.79  | 76.81  | 91.96  |
|      | 1.00 | 21.09                             | 24.83  | 29.15  | 34.10  | 39.75  |
|      | 1.50 | 13.74                             | 15.67  | 17.84  | 20.25  | 22.91  |
|      | 2.00 | 10.10                             | 11.17  | 12.33  | 13.56  | 14.84  |
|      | 2.50 | 7.93                              | 8.53   | 9.13   | 9.71   | 10.24  |

## Risk Reduction

If a firm can reduce its risk, it should see a payoff in higher PE

## Investment Dogs

Combination of high risk and low growth

# C. PE AND GROWTH QUALITY: VALUE ADDITION AND DESTRUCTION

For any given growth rate, the higher the ROE, the higher the PE ratio of the stock.

| Expected Growth Rate for next 5 years |     |       |       |       |       |           |
|---------------------------------------|-----|-------|-------|-------|-------|-----------|
|                                       |     | 5%    | 10%   | 15%   | 20%   | 25%       |
| ROE on Investments                    | 5%  | 13.24 | 11.19 | 8.2   | 4.04  | Worthless |
|                                       | 10% | 18.47 | 20.28 | 22.16 | 24.08 | 25.99     |
|                                       | 15% | 20.21 | 23.31 | 26.82 | 30.76 | 35.17     |
|                                       | 20% | 21.09 | 24.83 | 29.15 | 34.1  | 39.75     |
|                                       | 25% | 21.61 | 25.74 | 30.55 | 36.11 | 42.5      |

$$\text{Cost of equity} = 6.5\%$$

When ROE < Cost of equity, increasing growth lowers PE ratio

# EXAMPLE 1: THE CHEAPEST MARKETS AT THE START OF 2024

| Country     | # firms | median(EV/EBITDA) | median(Trailing PE) |
|-------------|---------|-------------------|---------------------|
| Zambia      | 15      | 3.75              | 4.31                |
| Kenya       | 50      | 3.70              | 4.43                |
| Ghana       | 23      | 2.74              | 5.34                |
| Cyprus      | 64      | 8.14              | 6.08                |
| Pakistan    | 424     | 5.14              | 6.24                |
| Serbia      | 17      | 5.64              | 6.69                |
| Kazakhstan  | 21      | 5.78              | 6.82                |
| Isle of Man | 16      | 5.34              | 7.32                |
| Sri Lanka   | 262     | 7.09              | 7.49                |
| Mauritius   | 75      | 8.72              | 7.51                |
| Tanzania    | 15      | 6.27              | 7.52                |
| Nigeria     | 126     | 5.40              | 7.90                |
| Macau       | 16      | 4.87              | 8.30                |
| Ivory Coast | 34      | 4.39              | 8.41                |
| Tunisia     | 76      | 7.73              | 8.68                |
| Bermuda     | 62      | 7.46              | 8.69                |
| Malawi      | 14      | 5.02              | 8.71                |
| Colombia    | 28      | 5.36              | 8.71                |
| Chile       | 122     | 6.80              | 8.84                |
| Lithuania   | 29      | 7.47              | 8.87                |

## EXAMPLE 2: CONTROLLING FOR DIFFERENCES - AN OLD EXAMPLE WITH EMERGING MARKETS: JUNE 2000

| <i>Country</i> | <i>PE Ratio</i> | <i>Interest Rates</i> | <i>GDP Real Growth</i> | <i>Country Risk</i> |
|----------------|-----------------|-----------------------|------------------------|---------------------|
| Argentina      | 14              | 18.00%                | 2.50%                  | 45                  |
| Brazil         | 21              | 14.00%                | 4.80%                  | 35                  |
| Chile          | 25              | 9.50%                 | 5.50%                  | 15                  |
| Hong Kong      | 20              | 8.00%                 | 6.00%                  | 15                  |
| India          | 17              | 11.48%                | 4.20%                  | 25                  |
| Indonesia      | 15              | 21.00%                | 4.00%                  | 50                  |
| Malaysia       | 14              | 5.67%                 | 3.00%                  | 40                  |
| Mexico         | 19              | 11.50%                | 5.50%                  | 30                  |
| Pakistan       | 14              | 19.00%                | 3.00%                  | 45                  |
| Peru           | 15              | 18.00%                | 4.90%                  | 50                  |
| Phillipines    | 15              | 17.00%                | 3.80%                  | 45                  |
| Singapore      | 24              | 6.50%                 | 5.20%                  | 5                   |
| South Korea    | 21              | 10.00%                | 4.80%                  | 25                  |
| Thailand       | 21              | 12.75%                | 5.50%                  | 25                  |
| Turkey         | 12              | 25.00%                | 2.00%                  | 35                  |
| Venezuela      | 20              | 15.00%                | 3.50%                  | 45                  |

# REGRESSION RESULTS

- The regression of PE ratios on these variables provides the following –

$$PE = 16.16$$

$$\begin{aligned} & - 7.94 \text{ Interest Rates} \\ & + 154.40 \text{ Growth in GDP} \\ & - 0.1116 \text{ Country Risk} \end{aligned}$$

- R Squared = 73%

- What do the coefficients tell you about how each of these variables play into PE ratio differences across countries?

# PREDICTED PE RATIOS

| <i>Country</i> | <i>PE Ratio</i> | <i>Interest Rates</i> | <i>GDP Real Growth</i> | <i>Country Risk</i> | <i>Predicted PE</i> |
|----------------|-----------------|-----------------------|------------------------|---------------------|---------------------|
| Argentina      | 14              | 18.00%                | 2.50%                  | 45                  | 13.57               |
| Brazil         | 21              | 14.00%                | 4.80%                  | 35                  | 18.55               |
| Chile          | 25              | 9.50%                 | 5.50%                  | 15                  | 22.22               |
| Hong Kong      | 20              | 8.00%                 | 6.00%                  | 15                  | 23.11               |
| India          | 17              | 11.48%                | 4.20%                  | 25                  | 18.94               |
| Indonesia      | 15              | 21.00%                | 4.00%                  | 50                  | 15.09               |
| Malaysia       | 14              | 5.67%                 | 3.00%                  | 40                  | 15.87               |
| Mexico         | 19              | 11.50%                | 5.50%                  | 30                  | 20.39               |
| Pakistan       | 14              | 19.00%                | 3.00%                  | 45                  | 14.26               |
| Peru           | 15              | 18.00%                | 4.90%                  | 50                  | 16.71               |
| Phillippines   | 15              | 17.00%                | 3.80%                  | 45                  | 15.65               |
| Singapore      | 24              | 6.50%                 | 5.20%                  | 5                   | 23.11               |
| South Korea    | 21              | 10.00%                | 4.80%                  | 25                  | 19.98               |
| Thailand       | 21              | 12.75%                | 5.50%                  | 25                  | 20.85               |
| Turkey         | 12              | 25.00%                | 2.00%                  | 35                  | 13.35               |
| Venezuela      | 20              | 15.00%                | 3.50%                  | 45                  | 15.35               |

# EXAMPLE 3: US STOCKS ARE EXPENSIVE, JUST LOOK AT THE PE RATIO

![](_page_10_Figure_9.jpeg)

# A COUNTER: NO, THEY ARE CHEAP, RELATIVE TO THE ALTERNATIVES..

![](_page_11_Figure_9.jpeg)

# THE TIE BREAKER: E/P RATIOS , T.BOND RATES AND TERM STRUCTURE

![](_page_12_Figure_9.jpeg)

# REGRESSION RESULTS

|                     | Earnings Yield | T. Bond Rate | T.Bond minus T.Bill |
|---------------------|----------------|--------------|---------------------|
| Earnings Yield      | 1.0000         |              |                     |
| T. Bond Rate        | 0.6873         | 1.0000       |                     |
| T.Bond minus T.Bill | -0.0544        | -0.0175      | 1.0000              |

Correlation between E/P and interest rate

- ▪ In the following regression, using 1960-2025 data, we regress E/P ratios against the level of T.Bond rates and a term structure variable (T.Bond - T.Bill rate)
  - ▪  $EP \text{ Ratio} = 0.0341 + 0.5618 T.Bond \text{ Rate} - 0.1161 (T.Bond \text{ Rate} - T.Bill \text{ Rate})$   
     $(6.47) \quad (7.45) \quad (-0.08)$
  - ▪  $R^2 \text{ squared} = 47.4\%$
- ▪ In 2008, this is what the regression looked like:
  - ▪  $E/P = 2.56\% + 0.7044 T.Bond \text{ Rate} - 0.3289 (T.Bond \text{ Rate} - T.Bill \text{ Rate})$   
     $(4.71) \quad (7.10) \quad (1.46)$
  - ▪  $R^2 \text{ squared} = 50.71\%$
- ▪ **The R-squared has dropped and the differential with the T.Bill rate has lost significance. How would you read this result?**

# II. PEG RATIO

- ▪ **PEG Ratio = PE ratio/ Expected Growth Rate in EPS**
  - ▪ For consistency, you should make sure that your earnings growth reflects the EPS that you use in your PE ratio computation.
  - ▪ The growth rates should preferably be over the same time period.
- ▪ To understand the fundamentals that determine PEG ratios, let us return again to a 2-stage equity discounted cash flow model:

$$P_0 = \frac{EPS_0 * \text{Payout Ratio} * (1+g)^* \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{r-g} + \frac{EPS_0 * \text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{(r-g_n)(1+r)^n}$$

- ▪ Dividing both sides of the equation by the earnings gives us the equation for the PE ratio. Dividing it again by the expected growth:

$$PEG = \frac{\text{Payout Ratio} * (1+g)^* \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{g(r-g)} + \frac{\text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{g(r-g_n)(1+r)^n}$$

# PEG RATIOS AND FUNDAMENTALS

- ▪ Risk and payout, which affect PE ratios, continue to affect PEG ratios as well.
  - ▪ Implication: When comparing PEG ratios across companies, we are making implicit or explicit assumptions about these variables.
- ▪ Dividing PE by expected growth does not neutralize the effects of expected growth, since the relationship between growth and value is not linear and fairly complex (even in a 2-stage model).
- ▪ In short, using a PEG ratio and assuming that you can ignore growth differences is pricing malpractice.

# A SIMPLE EXAMPLE

- Assume that you have been asked to estimate the PEG ratio for a firm which has the following characteristics:

| Variable             | High Growth Phase | Stable Growth Phase |
|----------------------|-------------------|---------------------|
| Expected Growth Rate | 15%               | 1.5%                |
| Payout Ratio         | 25%               | 92.5%               |
| Beta                 | 1.00              | 1.00                |

- Riskfree rate = Treasury Bond Rate = 1.5%, ERP = 5%
- Required rate of return =  $1.5\% + 1(5\%) = 6.5\%$
- The PEG ratio for this firm can be estimated as follows

$$PEG = \frac{.25 * 1.15 * \left(1 - \frac{1.15^5}{1.065^5}\right)}{.15 * (.065 - .15)} + \frac{.925 * 1.15^5 * (1.015)}{.15(.065 - .015)(1.065)^5} = 1.94$$

# A. PEG RATIOS ARE RISK-SENSITIVE

![](_page_17_Figure_10.jpeg)

# B. PEG RATIOS ARE AFFECTED BY THE QUALITY OF GROWTH

PEG ratios tend to increase with ROE, for every given growth rate.

|                    |     | Expected Growth Rate for next 5 years |      |      |      |      |
|--------------------|-----|---------------------------------------|------|------|------|------|
|                    |     | 5%                                    | 10%  | 15%  | 20%  | 25%  |
| ROE on Investments | 5%  | 2.65                                  | 1.12 | 0.55 | 0.20 | NA   |
|                    | 10% | 3.69                                  | 2.03 | 1.48 | 1.20 | 1.04 |
|                    | 15% | 4.04                                  | 2.33 | 1.79 | 1.54 | 1.41 |
|                    | 20% | 4.22                                  | 2.48 | 1.94 | 1.71 | 1.59 |
|                    | 25% | 4.32                                  | 2.57 | 2.04 | 1.81 | 1.70 |

High growth firms with very low ROE can trade at very low PEG ratios.

# C. PEG RATIOS ARE NOT GROWTH NEUTRAL...

![](_page_19_Picture_12.jpeg)

As **risk free rates rise**, PEG ratios decrease,  
for every growth rate.

|                                          |        | <i>Riskfree Rate</i> |             |             |             |
|------------------------------------------|--------|----------------------|-------------|-------------|-------------|
|                                          |        | 1.50%                | 3.00%       | 4.50%       | 6.00%       |
| <i>Expected Growth<br/>first 5 years</i> | 3.00%  | 4.34                 | 3.89        | 3.48        | 3.10        |
|                                          | 15.00% | 1.94                 | 1.70        | 1.48        | 1.27        |
|                                          | 30.00% | 1.54                 | 1.32        | 1.13        | 0.95        |
|                                          | 45.00% | <b>1.57</b>          | <b>1.33</b> | 1.12        | 0.92        |
|                                          | 60.00% | 1.73                 | 1.45        | <b>1.20</b> | <b>0.97</b> |
|                                          | 75.00% | 1.97                 | 1.63        | 1.33        | 1.06        |

**As growth  
increases, PEG  
ratios initially  
decline, but at a  
high-enough growth  
rate, PEG ratios rise  
again.**

# PEG RATIOS AND FUNDAMENTALS: PROPOSITIONS

- ▪ **Proposition 1: High risk companies will trade at much lower PEG ratios** than low risk companies with the same expected growth rate.
  - ▪ Corollary 1: The company that looks most under valued on a PEG ratio basis in a sector may be the riskiest firm in the sector
- ▪ **Proposition 2: Companies that can attain growth more efficiently by investing less in better return projects will have higher PEG ratios** than companies that grow at the same rate less efficiently.
  - ▪ Corollary 2: Companies that look cheap on a PEG ratio basis may be companies with high reinvestment rates and poor project returns.
- ▪ **Proposition 3: Companies with very low or very high growth rates** will tend to have higher PEG ratios than firms with average growth rates. This bias is worse for low growth stocks.
  - ▪ Corollary 3: PEG ratios do not neutralize the growth effect.