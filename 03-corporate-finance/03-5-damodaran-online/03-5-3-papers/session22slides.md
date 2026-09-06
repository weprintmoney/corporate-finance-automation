---
title: "Session22Slides"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/podcasts/valUGspr24/session22slides.pdf
---

# The Negative Intercept Problem

- When the intercept in a multiple regression is negative, there is the possibility that forecasted values can be negative as well.
- One way (albeit imperfect) is to re-run the regression without an intercept. When the intercept in a multiple regression is negative, there is the possibility that forecasted values can be negative as well. One way (albeit imperfect) is to re-run the regression without an intercept.

| Coefficients <sup>a,b,c,d</sup> |                                           |            |                           |      |        |       |
|---------------------------------|-------------------------------------------|------------|---------------------------|------|--------|-------|
| Model                           | Unstandardized Coefficients               |            | Standardized Coefficients | t    | Sig.   |       |
|                                 | B                                         | Std. Error |                           |      |        | Beta  |
| 1                               | Beta                                      | 19.344     | .814                      | .575 | 23.776 | <.001 |
|                                 | Payout ratio                              | 10.368     | 1.131                     | .135 | 9.170  | <.001 |
|                                 | Expected growth rate in EPS- Next 5 years | 68.704     | 5.067                     | .301 | 13.558 | <.001 |

- a. Broad Group = United States
- b. Dependent Variable: Trailing PE
- c. Linear Regression through the Origin
- d. Weighted Least Squares Regression - Weighted by Market Cap (in US \$)

# If a coefficient has the wrong sign: The Multicollinearity Problem

92

### Correlations<sup>a</sup>

|                                           | Trailing PE         | Beta   | Payout ratio | Expected growth rate in EPS- Next 5 years |         |
|-------------------------------------------|---------------------|--------|--------------|-------------------------------------------|---------|
| Trailing PE                               | Pearson Correlation | 1      | .116**       | .167**                                    | .091**  |
|                                           | Sig. (2-tailed)     |        | <.001        | <.001                                     | .002    |
|                                           | N                   | 2607   | 2481         | 2586                                      | 1114    |
| Beta                                      | Pearson Correlation | .116** | 1            | -.005                                     | .140**  |
|                                           | Sig. (2-tailed)     | <.001  |              | .797                                      | <.001   |
|                                           | N                   | 2481   | 5634         | 2589                                      | 1444    |
| Payout ratio                              | Pearson Correlation | .167** | -.005        | 1                                         | -.154** |
|                                           | Sig. (2-tailed)     | <.001  | .797         |                                           | <.001   |
|                                           | N                   | 2586   | 2589         | 2728                                      | 1157    |
| Expected growth rate in EPS- Next 5 years | Pearson Correlation | .091** | .140**       | -.154**                                   | 1       |
|                                           | Sig. (2-tailed)     | .002   | <.001        | <.001                                     |         |
|                                           | N                   | 1114   | 1444         | 1157                                      | 1462    |

\*\*. Correlation is significant at the 0.01 level (2-tailed).

a. Broad Group = United States

# Using the PE ratio regression

¨ Assume that you were given the following information for Disney. The firm has an expected growth rate of 15%, a beta of 0.90 and a 20% dividend payout ratio. Based upon the regression, the predicted PE ratio for Disney is: ¤ Predicted PE = 19.34 (0.9) + 10.37 (.20) ) + 68. 70 (.15) = 29.8 ¨ Disney is trading at 74.7 times earnings. What does the predicted PE tell you? ¨ Assume now that you priced Disney against just its peer group. Will you come to the same pricing judgment as you did when you looked at it relative to the market? Why or why not?

# The value of growth

![](_page_3_Figure_2.jpeg)

### II. PEG Ratio versus the market PEG versus Growth

![](_page_4_Figure_2.jpeg)

## PEG versus ln(Expected Growth)

![](_page_5_Figure_2.jpeg)

# PEG Ratio Regression - US stocks January 2024

97

## Model Summary<sup>a</sup>

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .299 <sup>b</sup> | .089     | .086              | 317.4781994                |

a. Broad Group = United States

b. Predictors: (Constant), InGrowth, Payout ratio, Beta

## Coefficients<sup>a,b,c</sup>

| Model | Unstandardized Coefficients |            | Standardized Coefficients<br>Beta | t     | Sig.   |       |
|-------|-----------------------------|------------|-----------------------------------|-------|--------|-------|
|       | B                           | Std. Error |                                   |       |        |       |
| 1     | (Constant)                  | .239       | .333                              |       | .717   | .474  |
|       | Beta                        | 1.280      | .163                              | .294  | 7.870  | <.001 |
|       | Payout ratio                | .865       | .171                              | .184  | 5.044  | <.001 |
|       | InGrowth                    | -.582      | .103                              | -.202 | -5.625 | <.001 |

a. Broad Group = United States

b. Dependent Variable: PEG

c. Weighted Least Squares Regression - Weighted by Market Cap (in US \$)

# I. PE ratio regressions across markets

gEPS=Expected Growth: Expected growth in EPS or Net Income: Next 5 years (decimals)

Beta: Regression or Bottom up Beta

Payout ratio: Dividends/ Net income from most recent year. Set to zero, if net income < 0

|                                                                                     |  |  |  | Regression |  |  |  |       | R Squared        | Region |
|-------------------------------------------------------------------------------------|--|--|--|------------|--|--|--|-------|------------------|--------|
| PE = 19.34 Beta + 68.70 g_EPS + 10.37 Payout<br>(23.78) (68.70) (10.37)             |  |  |  |            |  |  |  | 33.6% | US               |        |
| PE = 11.89 + 1.47 Beta + 32.44 g_EPS + 13.18 Payout<br>(8.82) (1.93) (9.96) (10.01) |  |  |  |            |  |  |  | 15.5% | Europe           |        |
| PE = 4.65 + 6.94 Beta + 25.75 g_EPS + 17.17 Payout<br>(2.38) (6.92) (3.80) (7.84)   |  |  |  |            |  |  |  | 23.2% | Japan            |        |
| PE = 15.02 + 0.06 Beta + 41.70 g_EPS + 3.71 Payout<br>(15.78) (0.12) (22.31) (3.91) |  |  |  |            |  |  |  | 24.8% | Aus, NZ & Canada |        |
| PE = 14.41 - 1.24 Beta + 92.94 g_EPS + 7.49 Payout<br>(6.91) (0.74) (14.80) (5.31)  |  |  |  |            |  |  |  | 40.5% | Emerging Markets |        |
| PE = 16.90 + 3.20 Beta + 51.53 g_EPS + 2.68 Payout<br>(22.96) (6.53) (27.77) (3.98) |  |  |  |            |  |  |  | 17.2% | Global           |        |

# II. PEG ratio regressions across markets

gEPS=Expected Growth: Expected growth in EPS or Net Income: Next 5 years (decimals)

Beta: Regression or Bottom up Beta

Payout ratio: Dividends/ Net income from most recent year. Set to zero, if net income < 0

|                                                                                                    |  | Regression |  |  |  |           |  |                  |  |
|----------------------------------------------------------------------------------------------------|--|------------|--|--|--|-----------|--|------------------|--|
|                                                                                                    |  | Regression |  |  |  | R Squared |  | Region           |  |
| PEG = 0.24 + 0.87 Payout - 0.58 ln(g <sub>EPS</sub> ) - 1.28 Beta<br>(27.75) (7.71) (19.04) (5.72) |  |            |  |  |  | 8.6%      |  | US               |  |
| PEG = 0.42 + 0.96 Payout - 0.92 ln(g <sub>EPS</sub> ) - 0.12 Beta<br>(1.59) (5.88) (10.82) (1.36)  |  |            |  |  |  | 19.5%     |  | Europe           |  |
| PEG = -0.31 Payout - 1.06 ln(g <sub>EPS</sub> ) + 0.16 Beta<br>(1.40) (14.84) (1.61)               |  |            |  |  |  | 34.9%     |  | Japan            |  |
| PEG = 1.06 + 0.20 Payout - 0.43 ln(g <sub>EPS</sub> ) - 0.12 Beta<br>(8.81) (2.72) (11.24) (2.57)  |  |            |  |  |  | 9.0%      |  | Emerging Markets |  |
| PEG = 0.32 Payout - 1.64 ln(g <sub>EPS</sub> ) - 0.54 Beta<br>(1.09) (16.80) (2.72)                |  |            |  |  |  | 46.2%     |  | Aus, NZ & Canada |  |
| PEG = 1.21 + 0.17 Payout - 0.70 ln(g <sub>EPS</sub> ) + 0.001 Beta<br>(9.82) (2.36) (16.96) (0.02) |  |            |  |  |  | 8.0%      |  | Global           |  |

## III. Price to Book Ratio: Fundamentals hold in every market

gEPS=Expected Growth: Expected growth in EPS/ Net Income: Next 5 years

Beta: Regression or Bottom up Beta

Payout ratio: Dividends/ Net income from most recent year. Set to zero, if net income < 0

ROE: Net Income/ Book value of equity in most recent year.

|                                                                                                             |  | Regression |  | R Squared | Region           |
|-------------------------------------------------------------------------------------------------------------|--|------------|--|-----------|------------------|
| PBV = 2.10 + 6.07 g_EPS + 0.69 Beta + 5.09 ROE - 0.33 Payout Ratio<br>(7.30) (8.96) (3.24) (11.71) (1.76)   |  |            |  | 21.9%     | US               |
| PBV = 1.20 + 3.25 g_EPS + 0.06 Beta + 5.78 ROE + 1.36 Payout Ratio<br>(4.43) (5.65) (0.42) (12.69) (6.29)   |  |            |  | 17.1%     | Europe           |
| PBV = 0.48 g_EPS + 0.78 Beta + 10.30 ROE + 0.10 Payout Ratio<br>(0.76) (8.50) (10.67) (0.05)                |  |            |  | 34.9%     | Japan            |
| PBV = 0.99 + 1.80 g_EPS - 0.13 Beta + 5.52 ROE - 0.09 Payout Ratio<br>(10.73) (7.78) (7.45) (8.87) (0.56)   |  |            |  | 36.9%     | Emerging Markets |
| PBV = 3.07 + 1.80 g_EPS - 1.49 Beta + 9.50 ROE + 1.80 Payout Ratio<br>(6.67) (7.89) (1.77) (27.35) (2.61)   |  |            |  | 32.9%     | Aus, NZ & Canada |
| PBV = 2.29 + 3.12 g_EPS - 0.16 Beta + 6.61 ROE - 0.29 Payout Ratio<br>(20.31) (13.52) (2.49) (29.17) (3.43) |  |            |  | 19.8%     | Global           |

# IV. EV/EBITDA across markets

g = Expected Revenue Growth: Expected growth in revenues: Near term (2 or 5 years)

DFR = Debt Ratio : Total Debt/ (Total Debt + Market value of equity)

Tax Rate: Effective tax rate in most recent year ROIC = Return on Capital

|                                                                                            | Regression |  | R Squared | Region           |
|--------------------------------------------------------------------------------------------|------------|--|-----------|------------------|
| EV/EBITDA= 27.61 + 40.22 g - 25.06 DFR - 37.09 Tax Rate<br>(44.93) (24.65) (18.92) (14.67) |            |  | 45.5%     | US               |
| EV/EBITDA= 21.10 + 26.59 g - 12.75 DFR - 18.40 Tax Rate<br>(43.03) (16.19) (14.78) (11.33) |            |  | 23.6%     | Europe           |
| EV/EBITDA= 16.40 + 29.78 g - 2.07 DFR - 13.21 Tax Rate<br>(19.45) (8.86) (1.91) (4.97)     |            |  | 6.60%     | Japan            |
| EV/EBITDA= 23.99 + 12.69 g - 14.49 DFR - 22.25 Tax Rate<br>(54.14) (14.01) (19.28) (15.67) |            |  | 16.7%     | Emerging Markets |
| EV/EBITDA= 19.73 + 12.89 g - 14.19 DFR - 6.74 Tax Rate<br>(18.06) (4.54) (7.04) (2.13)     |            |  | 10.0%     | Aus, NZ & Canada |
| EV/EBITDA= 24.82 + 26.15 g - 17.85 DFR - 25.43 Tax Rate<br>(95.20) (38.53) (36.49) (27.01) |            |  | 28.9%     | Global           |

# V. EV/Sales Regressions across markets…

g =Expected Revenue Growth: Expected growth in revenues: Near term (2 or 5 years)

Tax Rate: Effective tax rate in most recent year; Operating Margin: Operating Income/ Sales

|                                                                                                                  |  | Regression |  | R Squared | Region           |
|------------------------------------------------------------------------------------------------------------------|--|------------|--|-----------|------------------|
| EV/Sales = 3.81 + 9.86 g + 8.19 Oper Margin - 1.60 DFR - 5.88 Tax rate<br>(29.70) (19.48) (25.12) (7.36) (13.43) |  |            |  | 36.0%     | US               |
| EV/Sales = 1.52 + 5.96 g + 6.13 Oper Margin + 2.04 DFR - 0.15 Tax rate<br>(11.26) (14.61) (16.10) (11.35) (0.40) |  |            |  | 14.3%     | Europe           |
| EV/Sales = 1.13 + 3.82 g + 8.97 Oper Margin + 0.33 DFR - 1.59 Tax rate<br>(8.90) (7.69) (22.25) (2.12) (4.42)    |  |            |  | 29.1%     | Japan            |
| EV/Sales = 3.07 + 1.48 g + 4.29 Oper Margin - 0.24 DFR - 2.22 Tax rate<br>(37.19) (8.97) (18.42) (1.92) (8.18)   |  |            |  | 8.9%      | Emerging Markets |
| EV/Sales = 1.39 + 3.02 g + 4.31 Oper Margin + 1.21 DFR + 3.18 Tax rate<br>(5.82) (5.00) (9.36) (3.15) (4.78)     |  |            |  | 14.7%     | Aus, NZ & Canada |
| EV/Sales = 3.35 + 3.36 g + 6.45 Oper Margin - 0.52 DFR - 3.82 Tax rate<br>(58.99) (21.73) (41.35) (5.85) (20.93) |  |            |  | 18.0%     | Global           |

# VI. EV/Invested Capital

**103**

|             |          |                                      | Regression |  |  |  | R Squared | Region           |
|-------------|----------|--------------------------------------|------------|--|--|--|-----------|------------------|
| EV/Invested | Capital= | 5.78 + 0.66 g + 0.57 ROIC - 6.20 DFR |            |  |  |  | 44.2%     | US               |
|             |          | (54.84) (1.64) (5.95) (39.88)        |            |  |  |  |           |                  |
| EV/Invested | Capital= | 3.56 + 2.82 g + 4.10 ROIC - 3.54 DFR |            |  |  |  | 51.7%     | Europe           |
|             |          | (37.70) (10.07) (19.87) (31.52)      |            |  |  |  |           |                  |
| EV/Invested | Capital= | 3.55 + 1.22 g + 0.64 ROIC - 4.30 DFR |            |  |  |  | 41.1%     | Japan            |
|             |          | (31.39) (2.34) (9.61) (29.28)        |            |  |  |  |           |                  |
| EV/Invested | Capital= | 3.29 + 1.25 g + 0.96 ROIC - 3.76 DFR |            |  |  |  | 50.1%     | Emerging Markets |
|             |          | (64.77) (9.52) (11.37) (59.55)       |            |  |  |  |           |                  |
| EV/Invested | Capital= | 2.38 + 0.71 g + 4.62 ROIC - 2.06 DFR |            |  |  |  | 44.4%     | Aus, NZ & Canada |
|             |          | (17.66) (2.27) (11.40) (12.29)       |            |  |  |  |           |                  |
| EV/Invested | Capital= | 4.70 + 0.70 g + 0.86 ROIC - 5.00 DFR |            |  |  |  | 44.3%     | Global           |
|             |          | (113.51) (5.25) (18.30) (93.76)      |            |  |  |  |           |                  |

g =Expected Revenue Growth: Expected growth in revenues: Near term (2 or 5 years)

DFR: Debt Ratio

ROIC = Return on Invested Capital

# The Pricing Game: Choices

| Measure    | Choices               |    | Considerations/ Questions                    |
|------------|-----------------------|----|----------------------------------------------|
| Value      | Enterprise, Equity or |    |                                              |
|            |                       | 1. | Is this a financial service business?        |
|            |                       | 2. | Are there big differences in leverage?       |
| Scalar     | Revenues, Earnings,   |    |                                              |
|            |                       | 1. | How are you measuring value?                 |
|            |                       | 2. | Is the scaling number positive?              |
|            |                       | 3. | How (and how much) do accounting choices     |
|            | Current, Trailing,    |    |                                              |
|            |                       | 1. | Where are you in the life cycle?             |
|            |                       | 2. | How much cyclicality is there in the number? |
|            |                       | 3. | Can you get forecasted values?               |
| Comparable | What is your peer     |    |                                              |
|            |                       | 1. | How much do companies share in common        |
|            |                       | 2. | Does company size affect business            |
|            |                       | 3. | How big a sample of firms do you need?       |
|            |                       | 4. | How do you plan to control for differences?  |

## Relative Valuation: Some closing propositions

¨ Proposition 1: In a relative valuation, all that you are concluding is that a stock is under or over valued, relative to your comparable group. ¤ Your relative valuation judgment can be right and your stock can be hopelessly over valued at the same time. ¨ Proposition 2: In asset valuation, there are no similar assets. Every asset is unique. ¤ If you do not control for fundamental differences in risk, cash flows and growth across firms when comparing how they are priced, your valuation conclusions will reflect your flawed judgments rather than market misvaluations. ¨ Bottom line: Relative valuation is pricing, not valuation.

## Reviewing: The Four Steps to Understanding Multiples

¨ Define the multiple ¤ Check for consistency ¤ Make sure that they are estimated uniformly ¨ Describe the multiple ¤ Multiples have skewed distributions: The averages are seldom good indicators of typical multiples ¤ Check for bias, if the multiple cannot be estimated ¨ Analyze the multiple ¤ Identify the companion variable that drives the multiple ¤ Examine the nature of the relationship ¨ Apply the multiple

![]()Value assets, not cash flows?

# What is asset-based valuation?

¨ In intrinsic valuation, you value a business based upon the cash flows you expect that business to generate over time. ¨ In relative valuation, you value a business based upon how similar businesses are priced. ¨ In asset-based valuation, you value a business by valuing its individual assets. These individual assets can be tangible or intangible.

# Why would you do asset-based valuation?

¨ Liquidation: If you are liquidating a business by selling its assets piece meal, rather than as a composite business, you would like to estimate what you will get from each asset or asset class individually. ¨ Accounting mission: As both US and international accounting standards have turned to "fair value" accounting, accountants have been called upon to redo balance sheet to reflect the assets at their fair rather than book value. ¨ Sum of the parts: If a business is made up of individual divisions or assets, you may want to value these parts individually for one of two groups: ¤ Potential acquirers may want to do this, as a precursor to restructuring the business. ¤ Investors may be interested because a business that is selling for less than the sum of its parts may be "cheap".

# How do you do asset-based valuation?

¨ Intrinsic value: Estimate the expected cash flows on each asset or asset class, discount back at a risk adjusted discount rate and arrive at an intrinsic value for each asset. ¨ Relative value: Look for similar assets that have sold in the recent past and estimate a value for each asset in the business. ¨ Accounting value: You could use the book value of the asset as a proxy for the estimated value of the asset.

## When is asset-based valuation easiest to do?

¨ Separable assets: If a company is a collection of separable assets (a set of real estate holdings, a holding company of different independent businesses), asset-based valuation is easier to do. If the assets are interrelated or difficult to separate, asset-based valuation becomes problematic. Thus, while real estate or a long-term licensing/franchising contract may be easily valued, brand name (which cuts across assets) is more difficult to value separately. ¨ Stand alone earnings/ cash flows: An asset is much simpler to value if you can trace its earnings/cash flows to it. It is much more difficult to value when the business generates earnings, but the role of individual assets in generating these earnings cannot be isolated. ¨ Active market for similar assets: If you plan to do a relative valuation, it is easier if you can find an active market for "similar" assets which you can draw on for transactions prices.

# I. Liquidation Valuation

- □ In liquidation valuation, you are trying to assess how much you would get from selling the assets of the business today, rather than the business as a going concern.
- □ Consequently, it makes more sense to price those assets (i.e., do relative valuation) than it is to value them (do intrinsic valuation).
  - ■ For assets that are separable and traded (example: real estate), pricing is easy to do.
  - ■ For assets that are not, you often see book value used either as a proxy for liquidation value or as a basis for estimating liquidation value.
- □ To the extent that the liquidation is urgent, you may attach a discount to the estimated value.

# II. Accounting Valuation: Glimmers from FAS

## 157

- □ The ubiquitous “market participant”: Through FAS 157, accountants are asked to attach values to assets/liabilities that market participants would have been willing to pay/ receive.
- □ Tilt towards relative value: “The definition focuses on the price that would be received to sell the asset or paid to transfer the liability (an exit price), not the price that would be paid to acquire the asset or received to assume the liability (an entry price).” The hierarchy puts “market prices”, if available for an asset, at the top with intrinsic value being accepted only if market prices are not accessible.
- □ Split mission: While accounting fair value is titled towards relative valuation, accountants are also required to back their relative valuations with intrinsic valuations. Often, this leads to reverse engineering, where accountants arrive at values first and develop valuations later.

# III. Sum of the parts valuation

¨ You can value a company in pieces, using either relative or intrinsic valuation. Which one you use will depend on who you are and your motives for doing the sum of the parts valuation. ¨ If you are long term, passive investor in the company, your intent may be to find market mistakes that you hope will get corrected over time. If that is the case, you should do an intrinsic valuation of the individual assets. ¨ If you are an activist investor that plans to acquire the company or push for change, you should be more focused on relative valuation, since your intent is to get the company to split up and gain the increase in value.

## Let's try this: United Technologies: Raw Data - 2009

**115**

|                   |               |          | EBITDA  | Pre-tax Operating | Capital      |              | Total    |
|-------------------|---------------|----------|---------|-------------------|--------------|--------------|----------|
| Division          | Business      | Revenues |         |                   |              |              |          |
|                   | Refrigeration |          |         | Income            | Expenditures | Depreciation | Assets   |
| Carrier Pratt &   | systems       | \$14,944 | \$1,510 | \$1,316           | \$191        | \$194        | \$10,810 |
| Whitney           | Defense       | \$12,965 | \$2,490 | \$2,122           | \$412        | \$368        | \$9,650  |
| Otis UTC Fire &   | Construction  | \$12,949 | \$2,680 | \$2,477           | \$150        | \$203        | \$7,731  |
| Security Hamilton | Security      | \$6,462  | \$780   | \$542             | \$95         | \$238        | \$10,022 |
| Sundstrand        | Manufacturing | \$6,207  | \$1,277 | \$1,099           | \$141        | \$178        | \$8,648  |
| Sikorsky          | Aircraft      | \$5,368  | \$540   | \$478             | \$165        | \$62         | \$3,985  |

The company also had corporate expenses, unallocated to the divisions of \$408 million in the most recent year.

## United Technologies: Relative Valuation Median Multiples

| Division            | Business              | EBITDA  | EV/EBITDA for sector | Value of Business |
|---------------------|-----------------------|---------|----------------------|-------------------|
| Carrier             | Refrigeration systems | \$1,510 | 5.25                 | \$7,928           |
| Pratt & Whitney     | Defense               | \$2,490 | 8.00                 | \$19,920          |
| Otis                | Construction          | \$2,680 | 6.00                 | \$16,080          |
| UTC Fire & Security | Security              | \$780   | 7.50                 | \$5,850           |
| Hamilton Sundstrand | Industrial Products   | \$1,277 | 5.50                 | \$7,024           |
| Sikorsky            | Aircraft              | \$540   | 9.00                 | \$4,860           |
| business =          |                       |         |                      | \$61,661          |

## United Technologies: Relative Valuation Plus Scaling variable & Choice of Multiples

| Division            | Business              | Revenues | EBITDA  | Operating Income | Capital Invested |
|---------------------|-----------------------|----------|---------|------------------|------------------|
| Carrier             | Refrigeration systems | \$14,944 | \$1,510 | \$1,316          | \$6,014          |
| Pratt & Whitney     | Defense               | \$12,965 | \$2,490 | \$2,122          | \$5,369          |
| Otis                | Construction          | \$12,949 | \$2,680 | \$2,477          | \$4,301          |
| UTC Fire & Security | Security              | \$6,462  | \$780   | \$542            | \$5,575          |
| Hamilton Sundstrand | Industrial Products   | \$6,207  | \$1,277 | \$1,099          | \$4,811          |
| Sikorsky            | Aircraft              | \$5,368  | \$540   | \$478            | \$2,217          |
| Total               |                       | \$58,895 | \$9,277 | \$8,034          | \$28,287         |

| Business              | Best Multiple | Regression                                         | R <sup>2</sup> |
|-----------------------|---------------|----------------------------------------------------|----------------|
| Refrigeration systems | EV/EBITDA     | EV/EBITDA = 5.35 – 3.55 Tax Rate + 14.17 ROC       | 42%            |
| Defense               | EV/Revenues   | EV/Revenues = 0.85 + 7.32 Pre-tax Operating Margin | 47%            |
| Construction          | EV/EBITDA     | EV/EBITDA = 3.17 – 2.87 Tax Rate + 14.66 ROC       | 36%            |
| Security              | EV/Capital    | EV/ Capital = 0.55 + 8.22 ROC                      | 55%            |
| Industrial Products   | EV/Revenues   | EV/Revenues = 0.51 + 6.13 Pre-tax Operating Margin | 48%            |
| Aircraft              | EV/Capital    | EV/ Capital = 0.65 + 6.98 ROC                      | 40%            |

## United Technologies: Relative Valuation Sum of the Parts value

|                   | Scaling  | Current value for scaling                     |        | Operating | Tax  |                           | Estimated   |
|-------------------|----------|-----------------------------------------------|--------|-----------|------|---------------------------|-------------|
|                   |          | variable                                      | ROC    |           |      |                           |             |
| Division          | Variable |                                               |        |           | Rate | Predicted Multiple        | Value       |
| Carrier           | EBITDA   | \$1,510                                       | 13.57% | 8.81%     | 38%  |                           |             |
|                   |          |                                               |        |           |      | 5.35 – 3.55 (.38) + 14.17 |             |
| Pratt &           |          |                                               |        |           |      | (.1357) =5.92             | \$8,944.47  |
| Whitney           | Revenues | \$12,965                                      | 24.51% | 16.37%    | 38%  | 0.85 + 7.32 (.1637) =2.05 | \$26,553.29 |
| Otis              | EBITDA   | \$2,680                                       | 35.71% | 19.13%    | 38%  |                           |             |
|                   |          |                                               |        |           |      | 3.17 – 2.87 (.38)+14.66   |             |
| UTC Fire &        |          |                                               |        |           |      | (.3571) =7.31             | \$19,601.70 |
| Security Hamilton | Capital  | \$5,575                                       | 6.03%  | 8.39%     | 38%  | 0.55 + 8.22 (.0603) =1.05 | \$5,828.76  |
| Sundstrand        | Revenues | \$6,207                                       | 14.16% | 17.71%    | 38%  | 0.51 + 6.13 (.1771) =1.59 | \$9,902.44  |
| Sikorsky          | Capital  | \$2,217                                       | 13.37% | 8.90%     | 38%  | 0.65 + 6.98 (.1337) =1.58 | \$3,509.61  |
|                   |          | Sum of the parts value for operating assets = |        |           |      |                           | \$74,230.37 |

## United Technologies: DCF parts valuation Cost of capital, by business

| Division          | Unlevered Beta | Debt/Equity Ratio | Levered beta | Cost of equity | After-tax cost of debt | Debt to Capital | Cost of capital |
|-------------------|----------------|-------------------|--------------|----------------|------------------------|-----------------|-----------------|
| Carrier Pratt &   | 0.83           | 30.44%            | 0.97         | 9.32%          | 2.95%                  | 23.33%          | 7.84%           |
| Whitney           | 0.81           | 30.44%            | 0.95         | 9.17%          | 2.95%                  | 23.33%          | 7.72%           |
| Otis UTC Fire &   | 1.19           | 30.44%            | 1.39         | 12.07%         | 2.95%                  | 23.33%          | 9.94%           |
| Security Hamilton | 0.65           | 30.44%            | 0.76         | 7.95%          | 2.95%                  | 23.33%          | 6.78%           |
| Sundstrand        | 1.04           | 30.44%            | 1.22         | 10.93%         | 2.95%                  | 23.33%          | 9.06%           |
| Sikorsky          | 1.17           | 30.44%            | 1.37         | 11.92%         | 2.95%                  | 23.33%          | 9.82%           |

## United Technologies: DCF valuation Fundamentals, by business

|                     | Total    | Capital  |        | Allocated    | Operating income | Return on | Reinvestment |
|---------------------|----------|----------|--------|--------------|------------------|-----------|--------------|
| Division            | Assets   | Invested | Cap Ex | Reinvestment | after taxes      |           |              |
| Carrier Pratt &     | \$10,810 | \$6,014  | \$191  | \$353        | \$816            | 13.57%    | 43.28%       |
| Whitney             | \$9,650  | \$5,369  | \$412  | \$762        | \$1,316          | 24.51%    | 57.90%       |
| Otis UTC Fire       | \$7,731  | \$4,301  | \$150  | \$277        | \$1,536          | 35.71%    | 18.06%       |
| & Security Hamilton | \$10,022 | \$5,575  | \$95   | \$176        | \$336            | 6.03%     | 52.27%       |
| Sundstrand          | \$8,648  | \$4,811  | \$141  | \$261        | \$681            | 14.16%    | 38.26%       |
| Sikorsky            | \$3,985  | \$2,217  | \$165  | \$305        | \$296            | 13.37%    | 102.95%      |

## United Technologies, DCF valuation Growth Choices

| Division            | Cost of capital | Return on capital | Reinvestment Rate | Expected growth | Length of growth period | Stable growth rate | Stable ROC |
|---------------------|-----------------|-------------------|-------------------|-----------------|-------------------------|--------------------|------------|
| Carrier Pratt &     | 7.84%           | 13.57%            | 43.28%            | 5.87%           | 5                       | 3%                 | 7.84%      |
| Whitney             | 7.72%           | 24.51%            | 57.90%            | 14.19%          | 5                       | 3%                 | 12.00%     |
| Otis UTC Fire       | 9.94%           | 35.71%            | 18.06%            | 6.45%           | 5                       | 3%                 | 14.00%     |
| & Security Hamilton | 6.78%           | 6.03%             | 52.27%            | 3.15%           | 0                       | 3%                 | 6.78%      |
| Sundstrand          | 9.06%           | 14.16%            | 38.26%            | 5.42%           | 5                       | 3%                 | 9.06%      |
| Sikorsky            | 9.82%           | 13.37%            | 102.95%           | 13.76%          | 5                       | 3%                 | 9.82%      |

## United Technologies, DCF valuation Values of the parts

| Business          | Cost of capital | PV of FCFF | PV of Terminal Value | Value of Operating Assets |
|-------------------|-----------------|------------|----------------------|---------------------------|
| Carrier           | 7.84%           | \$2,190    | \$9,498              | \$11,688                  |
| Pratt & Whitney   | 7.72%           | \$3,310    | \$27,989             | \$31,299                  |
| Otis UTC Fire &   | 9.94%           | \$5,717    | \$14,798             | \$20,515                  |
| Security Hamilton | 6.78%           | \$0        | \$4,953              | \$4,953                   |
| Sundstrand        | 9.06%           | \$1,902    | \$6,343              | \$8,245                   |
| Sikorsky          | 9.82%           | -\$49      | \$3,598              | \$3,550                   |
| Sum               |                 |            |                      | \$80,250                  |

## United Technologies, DCF valuation Sum of the Parts

**123**

Value of the parts = \$80,250

Value of corporate expenses

$$= \frac{\text{Corporate Expenses}_{\text{Current}} (1-t)(1+g)}{(\text{Cost of capital}_{\text{Company}} - g)} = \frac{408(1-.38)(1.03)}{(.0868 - .03)} = \$ 4,587$$

Value of operating assets (sum of parts DCF) = \$75,663

Value of operating assets (sum of parts RV) = \$74,230

Value of operating assets (company DCF) = \$71,410

Enterprise value (based on market prices) = \$52,261

# GE in 2018: The Parts

| Business         | Revenues- 2017   | Revenue Growth in 2017 | EBIT before G&A | EBIT after G&A | EBIT Margin  | Invested Capital  | ROIC in 2017 | ROIC: 2013-<br>2017 | Cost of capital |
|------------------|------------------|------------------------|-----------------|----------------|--------------|-------------------|--------------|---------------------|-----------------|
| Power            | \$ 36.00         | -1.64%                 | \$ 2.80         | \$ 1.69        | 4.68%        | \$328.34          | 3.85%        | 9.28%               | 4.91%           |
| Renewable Energy | \$ 10.30         | 14.44%                 | \$ 0.70         | \$ 0.41        | 4.00%        | \$49.91           | 6.19%        | 8.00%               | 6.88%           |
| Oil & Gas        | \$ 17.20         | 33.33%                 | \$ 0.20         | \$ (0.31)      | -1.78%       | \$275.95          | -0.83%       | 3.71%               | 8.82%           |
| Aviation         | \$ 27.40         | 4.18%                  | \$ 6.60         | \$ 5.80        | 21.19%       | \$192.73          | 22.59%       | 20.27%              | 8.52%           |
| Healthcare       | \$ 19.10         | 4.37%                  | \$ 3.40         | \$ 2.86        | 15.00%       | \$132.81          | 16.18%       | 15.07%              | 7.97%           |
| Transportation   | \$ 4.20          | -10.64%                | \$ 0.80         | \$ 0.70        | 16.56%       | \$20.73           | 25.17%       | 26.67%              | 7.49%           |
| Lighting         | \$ 2.00          | -58.33%                | \$ 0.10         | \$ 0.03        | 1.59%        | \$3.34            | 7.16%        | 9.66%               | 8.50%           |
| Capital          | \$ 9.10          | -16.51%                | \$ (6.80)       | \$ (7.04)      | -77.40%      | \$723.38          | -7.30%       | -2.81%              | 3.64%           |
| <b>Total</b>     | <b>\$ 125.30</b> | <b>1.29%</b>           | <b>\$ 7.80</b>  | <b>\$ 4.15</b> | <b>3.31%</b> | <b>\$1,727.18</b> | <b>1.80%</b> | <b>4.50%</b>        | <b>6.23%</b>    |

# GE: Value of the Parts

| Business                        | Revenues in 2017 | Average EBIT Margin before G&A, 2013-17 | Normalized EBIT before G&A | Normalized EBIT (with corporate expenses allocated) | Normalized EBIT (1-t) | Cost of Capital | ROIC - Next 5 years | Expected growth next 5 years | Value of Business |
|---------------------------------|------------------|-----------------------------------------|----------------------------|-----------------------------------------------------|-----------------------|-----------------|---------------------|------------------------------|-------------------|
| Power                           | \$ 35,990.00     | 14.34%                                  | \$ 5,161.92                | \$ 4,061.80                                         | \$ 3,046.35           | 4.91%           | 9.28%               | 6.10%                        | \$ 73,138.18      |
| Renewable Energy                | \$ 10,280.00     | 8.24%                                   | \$ 847.46                  | \$ 532.70                                           | \$ 399.53             | 6.88%           | 8.00%               | 16.34%                       | \$ 6,455.88       |
| Oil & Gas                       | \$ 17,231.00     | 10.97%                                  | \$ 1,890.80                | \$ 1,365.19                                         | \$ 1,023.89           | 8.82%           | 3.71%               | -0.13%                       | \$ 11,924.66      |
| Aviation                        | \$ 27,375.00     | 22.09%                                  | \$ 6,046.58                | \$ 5,209.28                                         | \$ 3,906.96           | 8.52%           | 20.27%              | 4.55%                        | \$ 52,849.35      |
| Healthcare                      | \$ 19,116.00     | 17.01%                                  | \$ 3,251.87                | \$ 2,668.20                                         | \$ 2,001.15           | 7.97%           | 15.07%              | 0.99%                        | \$ 26,233.80      |
| Transportation                  | \$ 4,178.00      | 20.71%                                  | \$ 865.41                  | \$ 737.06                                           | \$ 552.80             | 7.49%           | 26.67%              | -6.62%                       | \$ 6,075.26       |
| Lighting                        | \$ 1,987.00      | 5.24%                                   | \$ 104.14                  | \$ 43.03                                            | \$ 32.27              | 8.50%           | 9.66%               | -24.94%                      | \$ 280.49         |
| Total (non-capital)             | \$ 116,157.00    | 15.35%                                  | \$ 17,829.69               | \$ 17,551.60                                        | \$ 13,163.70          |                 |                     |                              | \$ 176,957.62     |
| GE Capital Business             | \$ 9,070.00      | 3.00%                                   | \$ 272.10                  | \$ (5.98)                                           | \$ (4.49)             | 6.23%           | 0.00%               | -4.25%                       | \$ 27,080.96      |
| Value of businesses             |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 204,038.59     |
| - GE Debt                       |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 83,568.00      |
| - GE Capital Debt               |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 51,023.00      |
| - Minority Interests            |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 17,723.00      |
| + Cash                          |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 43,299.00      |
| Value of equity                 |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 95,023.59      |
| - Options                       |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 218.94         |
| Value of equity in common stock |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 94,804.65      |
| Value per share                 |                  |                                         |                            |                                                     |                       |                 |                     |                              | \$ 10.92          |

# GE: Pricing the Parts

| Business                            | Revenues in 2017 | Normalized EBIT,<br>using average<br>margin (2013-17) | DA in 2017 | EBITDA     | Peer Group<br>EV/EBITDA | Estimated Pricing |
|-------------------------------------|------------------|-------------------------------------------------------|------------|------------|-------------------------|-------------------|
| Power                               | \$ 35,990.00     | \$ 4,061.80                                           | \$1,358.00 | \$5,419.80 | 10.55                   | \$ 57,179         |
| Renewable Energy                    | \$ 10,280.00     | \$ 532.70                                             | \$ 259.00  | \$ 791.70  | 15.13                   | \$ 11,978         |
| Oil & Gas                           | \$ 17,231.00     | \$ 1,365.19                                           | \$1,026.00 | \$2,391.19 | 12.15                   | \$ 29,053         |
| Aviation                            | \$ 27,375.00     | \$ 5,209.28                                           | \$ 979.00  | \$6,188.28 | 6.56                    | \$ 40,595         |
| Healthcare                          | \$ 19,116.00     | \$ 2,668.20                                           | \$ 806.00  | \$3,474.20 | 10.97                   | \$ 38,112         |
| Transportation                      | \$ 4,178.00      | \$ 737.06                                             | \$ 135.00  | \$ 872.06  | 11.22                   | \$ 9,785          |
| Lighting                            | \$ 1,987.00      | \$ 43.03                                              | \$ 86.00   | \$ 129.03  | 12.8                    | \$ 1,652          |
| Total (non-capital)                 | \$ 116,157.00    | \$ 17,551.60                                          |            |            |                         | \$ 188,353        |
| GE Capital Business                 | \$ 9,070.00      | \$ (5.98)                                             | \$2,343.00 | \$2,337.02 | 10.13                   | \$ 23,674         |
| Pricing of Business                 |                  |                                                       |            |            |                         | \$ 212,027.44     |
| - GE Debt                           |                  |                                                       |            |            |                         | \$ 83,568.00      |
| - GE Capital Debt                   |                  |                                                       |            |            |                         | \$ 51,023.00      |
| - Minority Interests                |                  |                                                       |            |            |                         | \$ 17,723.00      |
| + Cash                              |                  |                                                       |            |            |                         | \$ 43,299.00      |
| Pricing of Equity                   |                  |                                                       |            |            |                         | \$ 103,012.44     |
| - Options                           |                  |                                                       |            |            |                         | 218.94            |
| Pricing of Equity in common stock   |                  |                                                       |            |            |                         | \$ 102,793.50     |
| <b>Estimating Pricing per share</b> |                  |                                                       |            |            |                         | <b>\$11.84</b>    |

![](_page_36_Picture_2.jpeg)

# Process of Valuing Private Companies

¨ The process of valuing private companies is not different from the process of valuing public companies. You estimate cash flows, attach a discount rate based upon the riskiness of the cash flows and compute a present value. As with public companies, you can either value ¤ The entire business, by discounting cash flows to the firm at the cost of capital. ¤ The equity in the business, by discounting cashflows to equity at the cost of equity. ¨ When valuing private companies, you face two standard problems: ¤ There is no market value for either debt or equity ¤ The financial statements for private firms are likely to go back fewer years, have less detail and have more holes in them.

# 1. No Market Value?

- ¨ Market values as inputs: Since neither the debt nor equity of a private business is traded, any inputs that require them cannot be estimated.
  - 1. Debt ratios for going from unlevered to levered betas and for computing cost of capital.
- 2. Market prices to compute the value of options and warrants granted to employees. ¨ Market value as output: When valuing publicly traded firms, the market value operates as a measure of reasonableness. In private company valuation, the value stands alone. ¨ Market price based risk measures, such as beta and bond ratings, will not be available for private businesses.

# 2. Cash Flow Estimation Issues

¨ Shorter history: Private firms often have been around for much shorter time periods than most publicly traded firms. There is therefore less historical information available on them. ¨ Different Accounting Standards: The accounting statements for private firms are often based upon different accounting standards than public firms, which operate under much tighter constraints on what to report and when to report. ¨ Intermingling of personal and business expenses: In the case of private firms, some personal expenses may be reported as business expenses. ¨ Separating "Salaries" from "Dividends": It is difficult to tell where salaries end and dividends begin in a private firm, since they both end up with the owner.

## Private Company Valuation: Motive matters..

¨ You can value a private company for ¤ 'Show' valuations <sup>n</sup> Curiosity: How much is my business really worth? <sup>n</sup> Legal purposes: Estate tax and divorce court ¤ Transaction valuations <sup>n</sup> Sale or prospective sale to another individual or private entity. <sup>n</sup> Sale of one partner's interest to another <sup>n</sup> Sale to a publicly traded firm ¤ As prelude to setting the offering price in an initial public offering ¨ You can value a division or divisions of a publicly traded firm ¤ As prelude to a spin off ¤ For sale to another entity ¤ To do a sum-of-the-parts valuation to determine whether a firm will be worth more broken up or if it is being efficiently run.

## Private company valuations: Four broad scenarios

- 1. Private to private transactions: You can value a private business for sale by one individual to another.
- 2. Private to public transactions: You can value a private firm for sale to a publicly traded firm.
- 3. Private to IPO: You can value a private firm for an initial public offering.
- 4. Private to VC to Public: You can value a private firm that is expected to raise venture capital along the way on its path to going public.

# I. Private to Private transaction

- □ In private-to-private transactions, a private business is sold by one individual to another. There are three key issues that we need to confront in such transactions:
  - □ Neither the buyer nor the seller is diversified. Consequently, risk and return models that focus on just the risk that cannot be diversified away will seriously under estimate the discount rates.
  - □ The investment is illiquid. Consequently, the buyer of the business will have to factor in an “illiquidity discount” to estimate the value of the business.
  - □ Key person value: There may be a significant personal component to the value. In other words, the revenues and operating profit of the business reflect not just the potential of the business but the presence of the current owner.

# An example: Valuing a restaurant

¨ Assume that you have been asked to value an upscale French restaurant for sale by the owner (who also happens to be the chef). Both the restaurant and the chef are well regarded, and business has been good for the last 3 years. ¤ The potential buyer is a former investment banker, who tired of the rat race, has decide to cash out all of his savings and use the entire amount to invest in the restaurant. ¤ You have access to the financial statements for the last 3 years for the restaurant. In the most recent year, the restaurant reported \$ 1.2 million in revenues and \$ 400,000 in pre-tax operating profit . ¤ While the firm has no conventional debt outstanding, it has a lease commitment of \$120,000 each year for the next 12 years.

# Past income statements…

|                          | 3 years | 2 years |           |                              |
|--------------------------|---------|---------|-----------|------------------------------|
|                          | ago     | ago     | Last year |                              |
| Revenues Operating lease | \$800   | \$1,100 | \$1,200   | Operating at full capacity   |
| expense                  | \$120   | \$120   | \$120     | (12 years left on the lease) |
| Wages                    | \$180   | \$200   | \$200     |                              |
| Material Other operating | \$200   | \$275   | \$300     | (25% of revenues)            |
| expenses                 | \$120   | \$165   | \$180     | (15% of revenues)            |
| Operating income         | \$180   | \$340   | \$400     |                              |
| Taxes                    | \$72    | \$136   | \$160     | (40% tax rate)               |
| Net Income               | \$108   | \$204   | \$240     |                              |

All numbers are in thousands

# Step 1: Estimating discount rates

¨ Conventional risk and return models in finance are built on the presumption that the marginal investors in the company are diversified and that they therefore care only about the risk that cannot be diversified. That risk is measured with a beta or betas, usually estimated by looking at past prices or returns. ¨ In this valuation, both assumptions are likely to be violated: ¤ As a private business, this restaurant has no market prices or returns to use in estimation. ¤ The buyer is not diversified. In fact, he will have his entire wealth tied up in the restaurant after the purchase.

No market price, no problem… Use bottom-up betas to get the unlevered beta

¨ The average unlevered beta across 75 publicly traded restaurants in the US is 0.86. Most of the publicly traded restaurants on this list are fast-food chains (McDonald's, Burger King) or mass restaurants (Applebee's, TGIF…). An upscale restaurant does not fit easily into this mix. ¨ There is an argument to be made that the beta for an upscale restaurant is more likely to be reflect high-end specialty retailers than it is restaurants. The unlevered beta for 45 high-end retailers is 1.18.

## A Data-driven View on Adjusting for Non-Diversification

Completely  
Undiversified

![](_page_47_Diagram_14.jpeg)

![](_page_47_Diagram_15.jpeg)

![](_page_47_Figure_16.jpeg)

![](_page_47_Figure_17.jpeg)