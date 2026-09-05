---
title: "Session19Slides"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valUGspr19/session19slides.pdf
---

# b. PE and Risk: A Follow up Example

PE Ratios and Beta: Growth Scenarios

![](_page_0_Figure_3.jpeg)

#### Example 1: Comparing PE ratios across Emerging Markets- March 2014 (pre- Ukraine)

![](_page_1_Figure_2.jpeg)

#### Example 2: An Old Example with Emerging Markets: June 2000

| Country     | PE Ratio | Interest Rates | GDP Real Growth | Country Risk |
|-------------|----------|----------------|-----------------|--------------|
| Argentina   | 14       | 18.00%         | 2.50%           | 45           |
| Brazil      | 21       | 14.00%         | 4.80%           | 35           |
| Chile       | 25       | 9.50%          | 5.50%           | 15           |
| Hong Kong   | 20       | 8.00%          | 6.00%           | 15           |
| India       | 17       | 11.48%         | 4.20%           | 25           |
| Indonesia   | 15       | 21.00%         | 4.00%           | 50           |
| Malaysia    | 14       | 5.67%          | 3.00%           | 40           |
| Mexico      | 19       | 11.50%         | 5.50%           | 30           |
| Pakistan    | 14       | 19.00%         | 3.00%           | 45           |
| Peru        | 15       | 18.00%         | 4.90%           | 50           |
| Phillipines | 15       | 17.00%         | 3.80%           | 45           |
| Singapore   | 24       | 6.50%          | 5.20%           | 5            |
| South Korea | 21       | 10.00%         | 4.80%           | 25           |
| Thailand    | 21       | 12.75%         | 5.50%           | 25           |
| Turkey      | 12       | 25.00%         | 2.00%           | 35           |
| Venezuela   | 20       | 15.00%         | 3.50%           | 45           |

# Regression Results

¨ The regression of PE ratios on these variables provides the following –

PE = 16.16 - 7.94 Interest Rates

+ 154.40 Growth in GDP

- 0.1116 Country Risk

R Squared = 73%

# Predicted PE Ratios

| Country     | PE Ratio | Interest Rates | GDP Real Growth | Country Risk | Predicted PE |
|-------------|----------|----------------|-----------------|--------------|--------------|
| Argentina   | 14       | 18.00%         | 2.50%           | 45           | 13.57        |
| Brazil      | 21       | 14.00%         | 4.80%           | 35           | 18.55        |
| Chile       | 25       | 9.50%          | 5.50%           | 15           | 22.22        |
| Hong Kong   | 20       | 8.00%          | 6.00%           | 15           | 23.11        |
| India       | 17       | 11.48%         | 4.20%           | 25           | 18.94        |
| Indonesia   | 15       | 21.00%         | 4.00%           | 50           | 15.09        |
| Malaysia    | 14       | 5.67%          | 3.00%           | 40           | 15.87        |
| Mexico      | 19       | 11.50%         | 5.50%           | 30           | 20.39        |
| Pakistan    | 14       | 19.00%         | 3.00%           | 45           | 14.26        |
| Peru        | 15       | 18.00%         | 4.90%           | 50           | 16.71        |
| Phillipines | 15       | 17.00%         | 3.80%           | 45           | 15.65        |
| Singapore   | 24       | 6.50%          | 5.20%           | 5            | 23.11        |
| South Korea | 21       | 10.00%         | 4.80%           | 25           | 19.98        |
| Thailand    | 21       | 12.75%         | 5.50%           | 25           | 20.85        |
| Turkey      | 12       | 25.00%         | 2.00%           | 35           | 13.35        |
| Venezuela   | 20       | 15.00%         | 3.50%           | 45           | 15.35        |

# Example 3: PE ratios for the S&P 500 in January 2017

![](_page_5_Figure_2.jpeg)

# Is low (high) PE cheap (expensive)?

- ¨ A market strategist argues that stocks are expensive because the PE ratio in 2017 is high relative to the average PE ratio across time. Do you agree?
  - a. Yes
- b. No ¨ If you do not agree, what factors might explain the higher PE ratio today? ¨ Would you respond differently if the market strategist has a Nobel Prize in Economics?

#### E/P Ratios , T.Bond Rates and Term Structure

![](_page_7_Figure_2.jpeg)

# Regression Results

¨ In the following regression, using 1960-2018 data, we regress E/P ratios against the level of T.Bond rates and a term structure variable (T.Bond - T.Bill rate)

EP Ratio = 0.0376 + 0.5325 T.Bond Rate - 0.1595 (T.Bond Rate - T.Bill Rate) (5.84) (6.22) (-0.78)

R squared = 41.97%

¨ Going back to 2008, this is what the regression looked like:

E/P = 2.56% + 0.7044 T.Bond Rate – 0.3289 (T.Bond Rate-T.Bill Rate) (4.71) (7.10) (1.46)

R squared = 50.71%

The R-squared has dropped and the differential with the T.Bill rate has lost significance. How would you read this result?

**34**

|                       | <i>T. Bond minus T. Bill</i> | <i>T. Bond Rate</i> | <i>T. Bond minus T. Bill</i> |
|-----------------------|------------------------------|---------------------|------------------------------|
| E/P                   | 1.0000                       |                     |                              |
| T. Bond Rate          | 0.6431                       | 1.0000              |                              |
| T. Bond minus T. Bill | -0.1388                      | -0.0944             | 1.0000                       |

Correlation between E/P and interest rates

# II. PEG Ratio

¨ PEG Ratio = PE ratio/ Expected Growth Rate in EPS ¤ For consistency, you should make sure that your earnings growth reflects the EPS that you use in your PE ratio computation. ¤ The growth rates should preferably be over the same time period. ¨ To understand the fundamentals that determine PEG ratios, let us return again to a 2-stage equity discounted cash flow model:

¨ Dividing both sides of the equation by the earnings gives us the equation for the PE ratio. Dividing it again by the expected growth g:

$$P_0 = \frac{\text{EPS}_0 * \text{Payout Ratio} * (1+g) * \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{r-g} + \frac{\text{EPS}_0 * \text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{(r-g_n)(1+r)^n}$$

$$\text{PEG} = \frac{\text{Payout Ratio} * (1+g) * \left(1 - \frac{(1+g)^n}{(1+r)^n}\right)}{g(r-g)} + \frac{\text{Payout Ratio}_n * (1+g)^n * (1+g_n)}{g(r-g_n)(1+r)^n}$$

# PEG Ratios and Fundamentals

¨ Risk and payout, which affect PE ratios, continue to affect PEG ratios as well. ¤ Implication: When comparing PEG ratios across companies, we are making implicit or explicit assumptions about these variables. ¨ Dividing PE by expected growth does not neutralize the effects of expected growth, since the relationship between growth and value is not linear and fairly complex (even in a 2-stage model)

# A Simple Example

¨ Assume that you have been asked to estimate the PEG ratio for a firm which has the following characteristics:

| Variable             | High Growth Phase | Stable Growth Phase |
|----------------------|-------------------|---------------------|
| Expected Growth Rate | 25%               | 8%                  |
| Payout Ratio         | 20%               | 50%                 |
| Beta                 | 1.00              | 1.00                |

¨ Riskfree rate = T.Bond Rate = 6% ¨ Required rate of return = 6% + 1(5.5%)= 11.5% ¨ The PEG ratio for this firm can be estimated as follows:

$$\text{PEG} = \frac{0.2 * (1.25) * \left(1 - \frac{(1.25)^5}{(1.115)^5}\right) + \frac{0.5 * (1.25)^5 * (1.08)}{25(.115 - .25) (1.115)^5}}{25(.115 - .25) (1.115)^5} = 115 \text{ or } 1.15$$

# PEG Ratios and Risk

![](_page_12_Figure_3.jpeg)

# PEG Ratios and Quality of Growth

![](_page_13_Figure_3.jpeg)

# PE Ratios and Expected Growth

![](_page_14_Figure_3.jpeg)

#### PEG Ratios and Fundamentals: Propositions

¨ Proposition 1: High risk companies will trade at much lower PEG ratios than low risk companies with the same expected growth rate. ¤ Corollary 1: The company that looks most under valued on a PEG ratio basis in a sector may be the riskiest firm in the sector ¨ Proposition 2: Companies that can attain growth more efficiently by investing less in better return projects will have higher PEG ratios than companies that grow at the same rate less efficiently. ¤ Corollary 2: Companies that look cheap on a PEG ratio basis may be companies with high reinvestment rates and poor project returns. ¨ Proposition 3: Companies with very low or very high growth rates will tend to have higher PEG ratios than firms with average growth rates. This bias is worse for low growth stocks. ¤ Corollary 3: PEG ratios do not neutralize the growth effect.

# III. Price to Book Ratio

¨ Going back to a simple dividend discount model,

¨ Defining the return on equity (ROE) = EPS0 / Book Value of Equity, the value of equity can be written as:

¨ If the return on equity is based upon expected earnings in the next time period, this can be simplified to,

$$P_0 = \frac{DPS_1}{r - g_n}$$

$$P_0 = \frac{\text{BV}_0 * \text{ROE} * \text{Payout Ratio} * (1 + g_n)}{r - g_n}$$

$$\frac{P_0}{BV_0} = PBV = \frac{ROE * Payout Ratio * (1 + g_n)}{r - g_n}$$

$$\frac{P_0}{BV_0} = PBV = \frac{ROE * Payout Ratio}{r - g_n}$$

#### Price Book Value Ratio: Stable Growth Firm Another Presentation

¨ This formulation can be simplified even further by relating growth to the return on equity:

g = (1 - Payout ratio) \* ROE

¨ Substituting back into the P/BV equation,

¨ The price-book value ratio of a stable firm is determined by the differential between the return on equity and the required rate of return on its projects. ¨ Building on this equation, a company that is expected to generate a ROE higher (lower than, equal to) its cost of equity should trade at a price to book ratio higher (less than, equal to) one.

$$\frac{P_0}{BV_0} = PBV = \frac{ROE - g_n}{r - g_n}$$

#### Now changing to an Enterprise value multiple EV/ Book Capital

¨ To see the determinants of the value/book ratio, consider the simple free cash flow to the firm model:

¨ Dividing both sides by the book value, we get:

¨ If we replace, FCFF = EBIT(1-t) - (g/ROC) EBIT(1-t),we get:

$$V_0 = \frac{\text{FCFF}_1}{\text{WACC} - g}$$

$$\frac{V_0}{BV} = \frac{FCFF_1/BV}{WACC-g}$$

$$\frac{V_0}{BV} = \frac{ROC - g}{WACC - g}$$

# IV. EV to EBITDA - Determinants

¨ The value of the operating assets of a firm can be written as:

¨ Now the value of the firm can be rewritten as

¨ Dividing both sides of the equation by EBITDA,

¨ The determinants of EV/EBITDA are:

¤ The cost of capital ¤ Expected growth rate ¤ Tax rate ¤ Reinvestment rate (or ROC)

$$EV = \frac{EBITDA (1-t) + Depr (t) - Cex - \Delta \text{ Working Capital}}{\text{WACC-g}}$$

$$\text{EV}_0 = \frac{\text{FCFF}_1}{\text{WACC-g}}$$

| EV     | (1-t)                                     | Depr (t)/EBITDA                           | CEx/EBITDA                                | $\Delta$ Working Capital/EBITDA           |
|--------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| EVITDA | $\frac{\text{WACC} - g}{\text{WACC} - g}$ | $\frac{\text{WACC} - g}{\text{WACC} - g}$ | $\frac{\text{WACC} - g}{\text{WACC} - g}$ | $\frac{\text{WACC} - g}{\text{WACC} - g}$ |

# A Simple Example

¨ Consider a firm with the following characteristics: ¤ Tax Rate = 36% ¤ Capital Expenditures/EBITDA = 30% ¤ Depreciation/EBITDA = 20% ¤ Cost of Capital = 10% ¤ The firm has no working capital requirements ¤ The firm is in stable growth and is expected to grow 5% a year forever. ¨ In this case, the Value/EBITDA multiple for this firm can be estimated as follows:

$$\frac{\text{Value}}{\text{EBITDA}} = \frac{(1 - .36)}{.10 - .05} + \frac{(0.2)(.36)}{.10 - .05} - \frac{0.3}{.10 - .05} - \frac{0}{.10 - .05} = 8.24$$

# The Determinants of EV/EBITDA

47

Tax  
Rates

![](_page_21_Figure_15.jpeg)

Excess  
Returns

**Value/EBITDA and Net Cap Ex Ra**

![](_page_21_Figure_19.jpeg)

Reinvestment  
Needs

**Value/EBITDA and Return on Cap**

![](_page_21_Figure_22.jpeg)

# V. EV/Sales Ratio

48

□ If pre-tax operating margins are used, the appropriate value estimate is that of the firm. In particular, if one makes the replaces the FCFF with the expanded version:

□ Free Cash Flow to the Firm = EBIT  $(1 - \text{tax rate}) (1 - \text{Reinvestment Rate})$ 

$$\frac{\text{Value}}{\text{Sales}_0} = \text{After-tax Oper. Margin}^* \left[ \frac{(1 - \text{RIR}_{\text{growth}})(1+g)^* \left( 1 - \frac{(1+g)^n}{(1+\text{WACC})^n} \right)}{\text{WACC}_{-g}} + \frac{(1 - \text{RIR}_{\text{stable}})(1+g)^n * (1+g_n)}{(\text{WACC}_{-g_n})(1+\text{WACC})^n} \right]$$

 $g$  = Growth rate in after-tax operating income for the first  $n$  years

 $g_n$  = Growth rate in after-tax operating income after  $n$  years forever (Stable growth rate)

 $\text{RIR}_{\text{Growth, Stable}}$  = Reinvestment rate in high growth and stable periods

 $\text{WACC}$  = Weighted average cost of capital

# The value of a brand name

¨ One of the critiques of traditional valuation is that is fails to consider the value of brand names and other intangibles. ¨ The approaches used by analysts to value brand names are often ad-hoc and may significantly overstate or understate their value. ¨ One of the benefits of having a well-known and respected brand name is that firms can charge higher prices for the same products, leading to higher profit margins and hence to higher price-sales ratios and firm value. The larger the price premium that a firm can charge, the greater is the value of the brand name. ¨ In general, the value of a brand name can be written as: ¤ Value of brand name ={(V/S)b-(V/S)g }\* Sales ¤ (V/S)b = Value of Firm/Sales ratio with the benefit of the brand name ¤ (V/S)g = Value of Firm/Sales ratio of the firm with the generic product

# Valuing Brand Name

| Current Revenues =                                   | Coca Cola \$21,962.00 | With Cott Margins \$21,962.00 |
|------------------------------------------------------|-----------------------|-------------------------------|
| Length of high-growth period                         | 10                    | 10                            |
| Reinvestment Rate =                                  | 50%                   | 50%                           |
| Operating Margin (after-tax)                         | 15.57%                | 5.28%                         |
| Sales/Capital (Turnover ratio)                       | 1.34                  | 1.34                          |
| Return on capital (after-tax)                        | 20.84%                | 7.06%                         |
| Growth rate during period (g) =                      | 10.42%                | 3.53%                         |
| Cost of Capital during period = Stable Growth Period | 7.65%                 | 7.65%                         |
| Growth rate in steady state =                        | 4.00%                 | 4.00%                         |
| Return on capital =                                  | 7.65%                 | 7.65%                         |
| Reinvestment Rate =                                  | 52.28%                | 52.28%                        |
| Cost of Capital =                                    | 7.65%                 | 7.65%                         |
| Value of Firm =                                      | \$79,611.25           | \$15,371.24                   |

**Value of brand name = \$79,611 -\$15,371 = \$64,240 million**

# The Determinants of Multiples…

![](_page_25_Diagram_2.jpeg)

![](_page_25_Diagram_5.jpeg)

#### **Equity Multiples**

#### **Firm Multiples**

# Application Tests

¨ Given the firm that we are valuing, what is a comparable firm? ¤ While traditional analysis is built on the premise that firms in the same sector are comparable firms, valuation theory would suggest that a comparable firm is one which is similar to the one being analyzed in terms of fundamentals. ¤ There is no reason why a firm cannot be compared with another firm in a very different business, if the two firms have the same risk, growth and cash flow characteristics. ¨ Given the comparable firms, how do we adjust for differences across firms on the fundamentals? ¤ It is impossible to find an exactly identical firm to the one you are valuing. ¤ You need to control for differences across firms.

#### 1. The Sampling Choice

¨ Ideally, you would like to find lots of publicly traded firms that look just like your firm, in terms of fundamentals, and compare the pricing of your firm to the pricing of these other publicly traded firms. Since, they are all just like your firm, there will be no need to control for differences. ¨ In practice, it is very difficult (and perhaps impossible) to find firms that share the same risk, growth and cash flow characteristics of your firm. Even if you are able to find such firms, they will very few in number. The trade off then becomes:

![](_page_27_Diagram_3.jpeg)

# 2. The "Control for Differences" Choices

- 1. Direct comparisons: If the comparable firms are just likeyour firm, you can compare multiples directly across the firms and conclude that your firm is expensive (cheap) if it trades at a multiple higher (lower) than the other firms.
- 2. Story telling: If there is a key dimension on which the firms vary, you can tell a story based upon your understanding of how value varies on that dimension. An example: This company trades at 12 times earnings, whereas the rest of the sector trades at 10 times earnings, but I think it is cheap because it has a much higher growth rate than the rest of the sector.
- 3. Modified multiple: You can modify the multiple to incorporate the dimension on which there are differences across firms.
- 4. Statistical techniques: If your firms vary on more than one dimension, you can try using multiple regressions (or variants thereof) to arrive at a controlledestimate for your firm.

#### 1. Just Story Telling Trailing PE across Beverage Companies

| Company Name            | Trailing PE | Expected Growth | Standard Deviation |
|-------------------------|-------------|-----------------|--------------------|
| Coca-Cola Bottling      | 29.18       | 9.50%           | 20.58%             |
| Molson Inc. Ltd. 'A'    | 43.65       | 15.50%          | 21.88%             |
| Anheuser-Busch          | 24.31       | 11.00%          | 22.92%             |
| Corby Distilleries Ltd. | 16.24       | 7.50%           | 23.66%             |
| Chalone Wine Group      | 21.76       | 14.00%          | 24.08%             |
| Andres Wines Ltd. 'A'   | 8.96        | 3.50%           | 24.70%             |
| Todhunter Int'l         | 8.94        | 3.00%           | 25.74%             |
| Brown-Forman 'B'        | 10.07       | 11.50%          | 29.43%             |
| Coors (Adolph) 'B'      | 23.02       | 10.00%          | 29.52%             |
| PepsiCo, Inc.           | 33.00       | 10.50%          | 31.35%             |
| Coca-Cola               | 44.33       | 19.00%          | 35.51%             |
| Boston Beer 'A'         | 10.59       | 17.13%          | 39.58%             |
| Whitman Corp.           | 25.19       | 11.50%          | 44.26%             |
| Mondavi (Robert) 'A'    | 16.47       | 14.00%          | 45.84%             |
| Coca-Cola Enterprises   | 37.14       | 27.00%          | 51.34%             |
| Hansen Natural Corp     | 9.70        | 17.00%          | 62.45%             |

# A Question

- ¨ You are reading an equity research report on this sector, and the analyst claims that Andres Wine and Hansen Natural are under valued because they have low PE ratios. Would you agree?
  - a. Yes
- b. No ¨ Why or why not?

#### 2: Statistical Controls

#### Comparing PE ratios across Telecom companies

| Company Name                                     | PE    | Growth |
|--------------------------------------------------|-------|--------|
| PT Indosat ADR                                   | 7.8   | 0.06   |
| Telebras ADR                                     | 8.9   | 0.075  |
| Telecom Corporation of New Zealand ADR           | 11 .2 | 0.11   |
| Telecom Argentina Stet - France Telecom SA ADR B | 12.5  | 0.08   |
| Hellenic Telecommunication Organization SA ADR   | 12.8  | 0.12   |
| Telecomunicaciones de Chile ADR                  | 16.6  | 0.08   |
| Swisscom AG ADR                                  | 18.3  | 0.11   |
| Asia Satellite Telecom Holdings ADR              | 19.6  | 0.16   |
| Portugal Telecom SA ADR                          | 20.8  | 0.13   |
| Telefonos de Mexico ADR L                        | 21 .1 | 0.14   |
| Matav RT ADR                                     | 21 .5 | 0.22   |
| Telstra ADR                                      | 21 .7 | 0.12   |
| Gilat Communications                             | 22.7  | 0.31   |
| Deutsche Telekom AG ADR                          | 24.6  | 0.11   |
| British Telecommunications PLC ADR               | 25.7  | 0.07   |
| Tele Danmark AS ADR                              | 27    | 0.09   |
| Telekomunikasi Indonesia ADR                     | 28.4  | 0.32   |
| Cable & Wireless PLC ADR                         | 29.8  | 0.14   |
| APT Satellite Holdings ADR                       | 31    | 0.33   |
| Telefonica SA ADR                                | 32.5  | 0.18   |
| Royal KPN NV ADR                                 | 35.7  | 0.13   |
| Telecom Italia SPA ADR                           | 42.2  | 0.14   |
| Nippon Telegraph & Telephone ADR                 | 44.3  | 0.2    |
| France Telecom SA ADR                            | 45.2  | 0.19   |
| Korea Telecom ADR                                | 71 .3 | 0.44   |

# PE, Growth and Risk

Dependent variable is: PE

R squared = 66.2% R squared (adjusted) = 63.1%

| Variable        | Coefficient | SE    | t-ratio  | Probability |
|-----------------|-------------|-------|----------|-------------|
| Constant        | 13.1151     | 3.471 | 3.78     | 0.0010      |
| Growth rate     | 121.223     | 19.27 | ≤ 0.0001 |             |
| Emerging Market | -13.8531    | 3.606 | -3.84    | 0.0009      |

Emerging Market is a dummy: 1 if emerging market 0 if not

# Is Telebras under valued?

¨ Predicted PE = 13.12 + 121.22 (.075) - 13.85 (1) = 8.35 ¨ At an actual price to earnings ratio of 8.9, Telebras is slightly overvalued. ¨ Bottom line: Just because a company trades at a low PE ratio does not make it cheap.

#### 3: An Eyeballing Exercise

#### PBV Ratios across European Banks in 2010

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

# The median test…

¨ We are looking for stocks that trade at low price to book ratios, while generating high returns on equity, with low risk. But what is a low price to book ratio? Or a high return on equity? Or a low risk ¨ One simple measure of what is par for the sector are the median values for each of the variables. A simplistic decision rule on under and over valued stocks would therefore be: ¤ Undervalued stocks: Trade at price to book ratios below the median for the sector,(2.07), generate returns on equity higher than the sector median (11.82%) and have standard deviations lower than the median (21.93%). ¤ Overvalued stocks: Trade at price to book ratios above the median for the sector and generate returns on equity lower than the sector median.

# The Statistical Alternative

¨ We are looking for stocks that trade at low price to book ratios, while generating high returns on equity. But what is a low price to book ratio? Or a high return on equity? ¨ Taking the sample of 18 banks, we ran a regression of PBV against ROE and standard deviation in stock prices (as a proxy for risk).

PBV = 2.27 + 3.63 ROE - 2.68 Std dev (5.56) (3.32) (2.33)

R squared of regression = 79%

# And these predictions?

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