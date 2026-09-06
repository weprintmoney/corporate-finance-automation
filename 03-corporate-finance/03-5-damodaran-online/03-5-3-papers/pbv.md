---
title: "Pbv"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/pbv.pdf
---

# Price-Book Value Ratio: Definition

- The price/book value ratio is the ratio of the market value of equity to the book value of equity, i.e., the measure of shareholders' equity in the balance sheet. Price/Book Value = Market Value of Equity Book Value of Equity Consistency Tests:
  - If the market value of equity refers to the market value of equity of common stock outstanding, the book value of common equity should be used in the denominator.
  - If there is more that one class of common stock outstanding, the market values of all classes (even the non-traded classes) needs to be factored in.

## Book Value Multiples: US stocks

![](_page_1_Figure_1.jpeg)

# Price to Book: U.S., Europe, Japan and Emerging Markets – January 2012

![](_page_2_Figure_1.jpeg)

## Price Book Value Ratio: Stable Growth Firm

Going back to a simple dividend discount model,

 Defining the return on equity (ROE) = EPS0 / Book Value of Equity, the value of equity can be written as:

 If the return on equity is based upon expected earnings in the next time period, this can be simplified to,

$$P_0 = \frac{DPS_1}{r - g_n}$$

| $P_0 =$ | $\frac{BV_0 * ROE * Payout Ratio * (1 + g_n)}{r - g_n}$ |
|---------|---------------------------------------------------------|
|---------|---------------------------------------------------------|

| $\frac{P_0}{BV_0} = PBV =$ | ROE * Payout Ratio * ( $1 + g_n$ ) |
|----------------------------|------------------------------------|
| $r - g_n$                  |                                    |

| $\frac{P_0}{BV_0} = \text{PBV} = \frac{\text{ROE} * \text{Payout Ratio}}{\text{r-g}_n}$ |
|-----------------------------------------------------------------------------------------|
|                                                                                         |

# Price Book Value Ratio: Stable Growth Firm Another Presentation

 This formulation can be simplified even further by relating growth to the return on equity:

## $$g = (1 - \text{Payout ratio}) * \text{ROE}$$

Substituting back into the P/BV equation,

 The price-book value ratio of a stable firm is determined by the differential between the return on equity and the required rate of return on its projects.

$$\frac{P_0}{BV_0} = PBV = \frac{ROE - g_n}{r - g_n}$$

# Looking for undervalued securities - PBV Ratios and ROE

 Given the relationship between price-book value ratios and returns on equity, it is not surprising to see firms which have high returns on equity selling for well above book value and firms which have low returns on equity selling at or below book value. The firms which should draw attention from investors are those which provide mismatches of price-book value ratios and returns on equity - low P/BV ratios and high ROE or high P/BV ratios and low ROE.

# An Eyeballing Exercise: European Banks in 2010

| Name                         | PBV Ratio | Return on Equity | Standard Deviation |
|------------------------------|-----------|------------------|--------------------|
| BAYERISCHE HYPO-UND VEREINSB | 0.80      | -1.66%           | 49.06%             |
| COMMERZBANK AG               | 1.09      | -6.72%           | 36.21%             |
| DEUTSCHE BANK AG -REG        | 1.23      | 1.32%            | 35.79%             |
| BANCA INTESA SPA             | 1.66      | 1.56%            | 34.14%             |
| BNP PARIBAS                  | 1.72      | 12.46%           | 31.03%             |
| BANCO SANTANDER CENTRAL HISP | 1.86      | 11.06%           | 28.36%             |
| SANPAOLO IMI SPA             | 1.96      | 8.55%            | 26.64%             |
| BANCO BILBAO VIZCAYA ARGENTA | 1.98      | 11.17%           | 18.62%             |
| SOCIETE GENERALE             | 2.04      | 9.71%            | 22.55%             |
| ROYAL BANK OF SCOTLAND GROUP | 2.09      | 20.22%           | 18.35%             |
| HBOS PLC                     | 2.15      | 22.45%           | 21.95%             |
| BARCLAYS PLC                 | 2.23      | 21.16%           | 20.73%             |
| UNICREDITO ITALIANO SPA      | 2.30      | 14.86%           | 13.79%             |
| KREDIETBANK SA LUXEMBOURGEOI | 2.46      | 17.74%           | 12.38%             |
| ERSTE BANK DER OESTER SPARK  | 2.53      | 10.28%           | 21.91%             |
| STANDARD CHARTERED PLC       | 2.59      | 20.18%           | 19.93%             |
| HSBC HOLDINGS PLC            | 2.94      | 18.50%           | 19.66%             |
| LLOYDS TSB GROUP PLC         | 3.33      | 32.84%           | 18.66%             |
| Average                      | 2.05      | 12.54%           | 24.99%             |
| Median                       | 2.07      | 11.82%           | 21.93%             |

## The median test…

- We are looking for stocks that trade at low price to book ratios, while generating high returns on equity, with low risk. But what is a low price to book ratio? Or a high return on equity? Or a low risk One simple measure of what is par for the sector are the median values for each of the variables. A simplistic decision rule on under and over valued stocks would therefore be:
  - Undervalued stocks: Trade at price to book ratios below the median for the sector, (2.05), generate returns on equity higher than the sector median (11.82%) and have standard deviations lower than the median (21.93%).
  - Overvalued stocks: Trade at price to book ratios above the median for the sector and generate returns on equity lower than the sector median.

## How about this mechanism?

 We are looking for stocks that trade at low price to book ratios, while generating high returns on equity. But what is a low price to book ratio? Or a high return on equity? Taking the sample of 18 banks, we ran a regression of PBV against ROE and standard deviation in stock prices (as a proxy for risk).

PBV = 2.27 + 3.63 ROE - 2.68 Std dev (5.56) (3.32) (2.33)

R squared of regression = 79%

## And these predictions?

| <i>Name</i>                  | <i>PBV Ratio</i> | <i>Return on Equity</i> | <i>Standard Deviation</i> | <i>Predicted PBV</i> | <i>Under/Over (%)</i> |
|------------------------------|------------------|-------------------------|---------------------------|----------------------|-----------------------|
| BAYERISCHE HYPO-UND VEREINSB | 0.80             | -1.66%                  | 49.06%                    | 0.89                 | -10.60%               |
| COMMERZBANK AG               | 1.09             | -6.72%                  | 36.21%                    | 1.05                 | 3.25%                 |
| DEUTSCHE BANK AG -REG        | 1.23             | 1.32%                   | 35.79%                    | 1.36                 | -9.26%                |
| BANCA INTESA SPA             | 1.66             | 1.56%                   | 34.14%                    | 1.41                 | 17.83%                |
| BNP PARIBAS                  | 1.72             | 12.46%                  | 31.03%                    | 1.89                 | -8.75%                |
| BANCO SANTANDER CENTRAL HISP | 1.86             | 11.06%                  | 28.36%                    | 1.91                 | -2.66%                |
| SANPAOLO IMI SPA             | 1.96             | 8.55%                   | 26.64%                    | 1.86                 | 5.23%                 |
| BANCO BILBAO VIZCAYA ARGENTA | 1.98             | 11.17%                  | 18.62%                    | 2.17                 | -9.12%                |
| SOCIETE GENERALE             | 2.04             | 9.71%                   | 22.55%                    | 2.02                 | 1.37%                 |
| ROYAL BANK OF SCOTLAND GROUP | 2.09             | 20.22%                  | 18.35%                    | 2.51                 | -16.65%               |
| HBOS PLC                     | 2.15             | 22.45%                  | 21.95%                    | 2.49                 | -13.71%               |
| BARCLAYS PLC                 | 2.23             | 21.16%                  | 20.73%                    | 2.48                 | -9.96%                |
| UNICREDITO ITALIANO SPA      | 2.30             | 14.86%                  | 13.79%                    | 2.44                 | -5.72%                |
| KREDIETBANK SA LUXEMBOURGEOI | 2.46             | 17.74%                  | 12.38%                    | 2.58                 | -4.79%                |
| ERSTE BANK DER OESTER SPARK  | 2.53             | 10.28%                  | 21.91%                    | 2.05                 | 23.11%                |
| STANDARD CHARTERED PLC       | 2.59             | 20.18%                  | 19.93%                    | 2.47                 | 5.00%                 |
| HSBC HOLDINGS PLC            | 2.94             | 18.50%                  | 19.66%                    | 2.41                 | 21.91%                |
| LLOYDS TSB GROUP PLC         | 3.33             | 32.84%                  | 18.66%                    | 2.96                 | 12.40%                |

## The Valuation Matrix

![](_page_10_Diagram_1.jpeg)

## Price to Book vs ROE: Largest Market Cap Firms in the United States: January 2010

![](_page_11_Figure_1.jpeg)

## What are we missing?

![](_page_12_Figure_1.jpeg)

## What else are we missing? PBV, ROE and Risk: Large Cap US firms

![](_page_13_Figure_1.jpeg)

# Bringing it all together... Largest US stocks

## Model Summary

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .819 <sup>a</sup> | .670     | .661              | 1.19253                    |

a. Predictors: (Constant), ROE, Expected Growth in EPS: next 5 years, Regression Beta

## Coefficients<sup>a</sup>

| Model                                | Unstandardized Coefficients |            | Standardized Coefficients | t      | Sig. |
|--------------------------------------|-----------------------------|------------|---------------------------|--------|------|
|                                      | B                           | Std. Error | Beta                      |        |      |
| 1 (Constant)                         | .406                        | .424       |                           | .958   | .340 |
| Regression Beta                      | -.065                       | .253       | -.015                     | -.256  | .799 |
| Expected Growth in EPS: next 5 years | 9.340                       | 2.366      | .228                      | 3.947  | .000 |
| ROE                                  | 10.546                      | .771       | .777                      | 13.672 | .000 |

a. Dependent Variable: PBV Ratio

# PBV Ratios – Largest Market Cap US companies in January 2012

![](_page_15_Figure_1.jpeg)

Even in chaos, there is order...  
 US Banks (Mkt cap> \$ 1 billion) in January 2009

---

![](_page_16_Figure_5.jpeg)

## In January 2010… Another look at US Banks

![](_page_17_Figure_1.jpeg)

## Banks again.. In January 2012

![](_page_18_Figure_1.jpeg)

# IBM: The Rise and Fall and Rise Again PBV vs ROE: 1983-2010

![](_page_19_Figure_2.jpeg)

# PBV Ratio Regression: US January 2012

## Model Summary

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .733 <sup>a</sup> | .537     | .536              | 125.776416                 |

a. Predictors: (Constant), ROE, Payout Ratio, Expected Growth in EPS: next 5 years, 3-yr Regression Beta

## Coefficients<sup>a,b</sup>

| Model                                | Unstandardized Coefficients |            | Standardized Coefficients | t      | Sig. |
|--------------------------------------|-----------------------------|------------|---------------------------|--------|------|
|                                      | B                           | Std. Error | Beta                      |        |      |
| 1 (Constant)                         | .497                        | .116       |                           | 4.289  | .000 |
| 3-yr Regression Beta                 | -.376                       | .061       | -.101                     | -6.170 | .000 |
| Payout Ratio                         | .529                        | .121       | .070                      | 4.369  | .000 |
| Expected Growth in EPS: next 5 years | 3.126                       | .313       | .160                      | 9.981  | .000 |
| ROE                                  | 12.211                      | .273       | .710                      | 44.724 | .000 |

a. Dependent Variable: PBV Ratio

b. Weighted Least Squares Regression – Weighted by Market Cap

# PBV Ratio Regression- Other Markets January 2012

| Region | Regression – January 2012                       | R squared |
|--------|-------------------------------------------------|-----------|
|        | PBV = 0.90 + 0.92 Payout – 0.18 Beta + 5.43 ROE | 38.6%     |
| Europe | PBV = 1.14 + 0.76 Payout – 0.67 Beta + 7.56 ROE | 47.2%     |
| Japan  | PBV = 1.21 + 0.67 Payout – 0.40 Beta + 3.26 ROE | 22.1%     |
|        | PBV = 0.77 + 1.16 Payout – 0.17 Beta + 5.78 ROE | 20.8%     |

# Value/Book Value Ratio: Definition

 While the price to book ratio is a equity multiple, both the market value and the book value can be stated in terms of the firm. Value/Book Value = Market Value of Equity + Market Value of Debt Book Value of Equity + Book Value of Debt

## Determinants of Value/Book Ratios

 To see the determinants of the value/book ratio, consider the simple free cash flow to the firm model:

Dividing both sides by the book value, we get:

If we replace, FCFF = EBIT(1-t) - (g/ROC) EBIT(1-t),we get

$$V_0 = \frac{\text{FCFF}_1}{\text{WACC-g}}$$

$$\frac{V_0}{BV} = \frac{\text{FCFF}_1/BV}{\text{WACC} - g}$$

$$\frac{V_0}{BV} = \frac{\text{ROC} - g}{\text{WACC} - g}$$

## Value/Book Ratio: An Example

- Consider a stable growth firm with the following characteristics:
  - Return on Capital = 12%
  - Cost of Capital = 10%
- Expected Growth = 5% The value/BV ratio for this firm can be estimated as follows: Value/BV = (.12 - .05)/(.10 - .05) = 1.40 The effects of ROC on growth will increase if the firm has a high growth phase, but the basic determinants will remain unchanged.

# Value/Book and the Return Spread

![](_page_25_Figure_2.jpeg)

# EV/ Invested Capital Regression - US - January 2012

**Model Summary**

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .763 <sup>a</sup> | .582     | .581              | 120.593384                 |

a. Predictors: (Constant), ROIC, Expected Growth in Revenues: next 5 years, Market Debt to Capital

**Coefficients<sup>a,b</sup>**

| Model                                     | Unstandardized Coefficients |            | Standardized Coefficients |         | t    | Sig. |
|-------------------------------------------|-----------------------------|------------|---------------------------|---------|------|------|
|                                           | B                           | Std. Error | Beta                      |         |      |      |
| 1 (Constant)                              | 1.101                       | .116       |                           | 9.495   | .000 |      |
| Expected Growth in Revenues: next 5 years | 5.724                       | .750       | .153                      | 7.635   | .000 |      |
| Market Debt to Capital                    | -2.397                      | .234       | -.220                     | -10.249 | .000 |      |
| ROIC                                      | 7.430                       | .276       | .551                      | 26.935  | .000 |      |

a. Dependent Variable: EV/ Invested Capital

b. Weighted Least Squares Regression – Weighted by Market Cap