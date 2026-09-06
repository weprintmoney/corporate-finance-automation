---
title: "Dcfstabl"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/dcfstabl.pdf
---

![](_page_0_Picture_4.jpeg)

# CLOSURE IN VALUATION

The Big Enchilada

# GETTING CLOSURE IN VALUATION

- ▪ A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

$$\text{Value} = \sum_{t=1}^{t=\infty} \frac{CF_t}{(1+r)^t}$$

- ▪ Since we cannot estimate cash flows forever, we estimate cash flows for a “growth period” and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \sum_{t=1}^{t=N} \frac{CF_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^N}$$

# WAYS OF ESTIMATING TERMINAL VALUE

| Approach                   | Inputs and Value                                                                                        | Types of business                                                                                |
|----------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Liquidation Value          | Liquidation value of assets held by the firm in the terminal year.                                      | Businesses built around a key person or a time-limited competitive advantage (license or patent) |
| Going Concern (Perpetuity) | $TV \text{ in year } n = CF_{n+1} / (r - g)$ , where $g = \text{growth rate forever}$                   | Going concerns with long lives (>40 years)                                                       |
| Going Concern (Finite)     | $TV \text{ in year } n = PV \text{ of } CF \text{ in years } n+1 \text{ to } n+k$ , where $k$ is finite | Going concerns with shorter lives                                                                |
| Pricing                    | Terminal Year Operating Metric<br>* Estimated Multiple of Metric                                        | <b>Never appropriate in an intrinsic valuation.</b>                                              |

# 1. WITH PERPETUAL GROWTH, OBEY THE GROWTH CAP

- ▪ When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

$$\text{Value} = \text{Expected Cash Flow Next Period} / (r - g)$$

$$r = \text{Discount rate (Cost of Equity or Cost of Capital)}$$

$$g = \text{Expected growth rate}$$

- ▪ The stable growth rate cannot exceed the growth rate of the economy, but it can be lower.
  - ▪ If the economy is composed of high growth and stable growth firms, the **growth rate of the latter will be lower than the growth rate of the economy**.
  - ▪ The **stable growth rate can be negative**, for companies in declining businesses.
  - ▪ If you use **nominal cashflows and discount rates**, the growth rate should be nominal in the currency in which the valuation is denominated.

# RISK FREE RATES AND NOMINAL GDP GROWTH

- ▪ **Risk free Rate = Expected Inflation + Expected Real Interest Rate**
- ▪ **Nominal GDP Growth = Expected Inflation + Expected Real Growth**
- ▪ The real interest rate is what borrowers agree to return to lenders in real goods/services.
- ▪ The real growth rate in the economy measures the expected growth in the production of goods and services.

## The argument for Risk free rate = Nominal GDP growth

1. 1. In the long term, the real growth rate cannot be lower than the real interest rate, since the growth in goods/services has to be enough to cover the promised rate.
2. 2. In the long term, the real growth rate can be higher than the real interest rate, to compensate risk taking. However, as economies mature, the difference should get smaller and since there will be growth companies in the economy, it is prudent to assume that the extra growth comes from these companies.

| Time Period | Ten-year T.Bond rate | Inflation rate | Real GDP growth | Nominal GDP Growth Rate |
|-------------|----------------------|----------------|-----------------|-------------------------|
| 1954-2021   | 5.59%                | 3.55%          | 2.94%           | 6.50%                   |
| 1954-1980   | 5.83%                | 4.49%          | 3.50%           | 7.98%                   |
| 1981-2008   | 6.88%                | 3.26%          | 3.04%           | 6.30%                   |
| 2011-2021   | 2.25%                | 1.76%          | 1.70%           | 3.46%                   |

# A PRACTICAL REASON FOR USING THE RISK FREE RATE CAP – PRESERVE CONSISTENCY

- ■ You are implicitly making assumptions about nominal growth in the economy, with your riskfree rate. Thus, with a low risk free rate, you are assuming low nominal growth in the economy (with low inflation and low real growth) and with a high risk free rate, a high nominal growth rate in the economy.
- ■ If you make an explicit assumption about nominal growth in cash flows that is at odds with your implicit growth assumption in the denominator, you are being inconsistent and bias your valuations:
  - ■ If you assume high nominal growth in the economy, with a low risk free rate, you will over value businesses.
  - ■ If you assume low nominal growth rate in the economy, with a high risk free rate, you will under value businesses.

Terminal Value = 2972/(.05-..-(.005)) = 54,034

Discount at Euro Cost of Capital (WACC) = 7.66% (.599) + 1.13% (0.401) = 5.04%

| Region                    | ERP = 6.83% Revenues | Weight  | ERP    |
|---------------------------|----------------------|---------|--------|
| Europe                    | 10348                | 50.24%  | 6.90%  |
| North America             | 5920                 | 28.74%  | 5.75%  |
| Asia                      | 2919                 | 14.17%  | 7.22%  |
| Latin America & Caribbean | 781                  | 3.79%   | 10.53% |
| Africa & Mid East         | 631                  | 3.06%   | 9.30%  |
| Total                     | 20599                | 100.00% | 6.83%  |

Beta = 1.20

Cost of Debt (-0.5%+2%)(1-.25) = 1.13%

Cost of Equity 7.66%

**Stable Growth** g = -0.5%; Cost of capital = 5% ROC= 5%; Reinvestment Rate=-.5%/5% = -10% 

Weights E = 59.9% D = 40.1%

Riskfree Rate: Euro Risk free rate = -0.50% <sup>+</sup> <sup>X</sup>

Firm's D/E RaSo: 66.98%

# Heineken: September 2019 (in Euros)

Euro Cashflows

Cash flows from existing assets The Payoff from growth Maturty and Closure

The Risk in the Cash flows

On September 1, 2019, Heineken was trading at 93.25 Euros/share

Revenues will grow 3.22% a year for next 5 years, tapering down to -0.5% growth in year 10

Operatng margin (per-tax) will drop to 14.00%

Sales/Invested Capital will stay at five-year average of 0.79.

Unlevered beta of alcoholic beverage business = 0.80

| Revenues               | LTM € 23,119 | 2013-2018 Growth rate = 3.22% |
|------------------------|--------------|-------------------------------|
| Operating Margin       | 14.86%       | 14.44%                        |
| Sales/Invested Capital | 0.71         | 0.79                          |
| ROIC                   | 7.46%        | 8.32%                         |
| Effective Tax Rate     | 29.70%       | 27.00%                        |

|                         | 1        | 2        | 3        | 4        | 5        | 6        | 7        | 8        | 9        |      | 10     | Terminal year |
|-------------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|------|--------|---------------|
| Revenue growth rate     | 3.22%    | 3.22%    | 3.22%    | 3.22%    | 3.22%    | 2.48%    | 1.73%    | 0.99%    | 0.24%    |      | -0.50% | -0.50%        |
| Revenues                | € 23,863 | € 24,632 | € 25,425 | € 26,244 | € 27,089 | € 27,759 | € 28,240 | € 28,519 | € 28,589 | €    | 28,446 | € 28,304      |
| EBIT (Operating) margin | 14.38%   | 14.34%   | 14.30%   | 14.26%   | 14.21%   | 14.17%   | 14.13%   | 14.09%   | 14.04%   |      | 14.00% | 14.00%        |
| EBIT (Operating income) | € 3,432  | € 3,532  | € 3,635  | € 3,741  | € 3,850  | € 3,934  | € 3,990  | € 4,017  | € 4,015  | €    | 3,982  | \$ 3,963      |
| Tax rate                | 29.70%   | 29.70%   | 29.70%   | 29.70%   | 29.70%   | 28.76%   | 27.82%   | 26.88%   | 25.94%   |      | 25.00% | \$ 0          |
| EBIT(1-t)               | € 2,413  | € 2,483  | € 2,556  | € 2,630  | € 2,707  | € 2,802  | € 2,880  | € 2,937  | € 2,973  | €    | 2,987  | \$ 2,972      |
| - Reinvestment          | € 942    | € 973    | € 1,004  | € 1,036  | € 1,070  | € 849    | € 609    | € 353    | €        | 88 € | (181)  | \$ (297)      |
| FCFF                    | € 1,471  | € 1,511  | € 1,552  | € 1,594  | € 1,637  | € 1,953  | € 2,271  | € 2,584  | € 2,885  | €    | 3,168  | \$ 3,269      |

PV(Terminal value) € 36,390.85 PV (CF over next 10 years) € 15,300.34 Value of operating assets = € 51,691.19 - Debt € 19,709.52 - Minority interests € 1,069.00 + Cash € 1,751.60 + Non-operating assets € 1,401.00 Value of equity € 34,065.26 Number of shares 571.10 Estimated value /share € 59.65 Price € 93.25 Price as % of value 56.33%

## 2. DON'T WAIT TOO LONG...

- ▪ Most growth firms have difficulty sustaining their growth for long periods, especially while earning excess returns. Assuming long growth periods for all firms is ignoring this reality.
  - ▪ **Proposition 1:** The **larger the potential market** for a company's products and services, the greater the likelihood that you can maintain growth for longer.
  - ▪ **Proposition 2:** The **smaller a company**, relative to the market it aspires to reach, the longer the potential growth period can be.
- ▪ It is not growth per se that creates value but growth with excess returns. For growth firms to continue to generate value-creating growth, they have to be able to keep the competition at bay.
  - ▪ **Proposition 3:** The **stronger and more sustainable the competitive advantages**, the longer a growth company can sustain “value creating” growth.
  - ▪ **Proposition 4:** Growth companies with strong and sustainable competitive advantages are rare.

# 3. DO NOT FORGET THAT GROWTH HAS TO BE EARNED..

- The reinvestment rate in stable growth will be a function of the stable growth rate and return on capital in perpetuity
  - Reinvestment Rate = Stable g/ Stable period ROC = g/ ROC
  - Terminal Value in year n =  $\frac{EBIT_{n+1} (1-t)(1 - \frac{g}{ROC})}{(\text{Cost of Capital} - g)}$

|                     |      | Return on capital in perpetuity |         |         |         |         |
|---------------------|------|---------------------------------|---------|---------|---------|---------|
|                     |      | 6%                              | 8%      | 10%     | 12%     | 14%     |
| Growth rate forever | 0.0% | \$1,000                         | \$1,000 | \$1,000 | \$1,000 | \$1,000 |
|                     | 0.5% | \$965                           | \$987   | \$1,000 | \$1,009 | \$1,015 |
|                     | 1.0% | \$926                           | \$972   | \$1,000 | \$1,019 | \$1,032 |
|                     | 1.5% | \$882                           | \$956   | \$1,000 | \$1,029 | \$1,050 |
|                     | 2.0% | \$833                           | \$938   | \$1,000 | \$1,042 | \$1,071 |
|                     | 2.5% | \$778                           | \$917   | \$1,000 | \$1,056 | \$1,095 |
|                     | 3.0% | \$714                           | \$893   | \$1,000 | \$1,071 | \$1,122 |

# EXCESS RETURNS TO ZERO?

- ■ There are some (McKinsey, for instance) who argue that the return on capital should always be equal to cost of capital in stable growth.
- ■ But excess returns seem to persist for very long time periods.

## A more sustainable measure

Median for top 500 publicly listed US companies by revenues in 1965, 1975, 1985, and 1995

Returns on invested capital (ROIC) is sustainable over time, but growth inevitably declines.

ROIC,<sup>1</sup> %

![](_page_9_Figure_40.jpeg)

Real revenue growth,<sup>1</sup> %

![](_page_9_Figure_42.jpeg)

# AND DON'T FALL FOR SLEIGHT OF HAND...

- ▪ A typical assumption in many DCF valuations, when it comes to stable growth, is that capital expenditures offset depreciation and there are no working capital needs. Stable growth firms, we are told, just have to make maintenance cap ex (replacing existing assets ) to deliver growth.
- a. If you make this assumption, what expected growth rate can you use in your terminal value computation?
- b. What if the stable growth rate = inflation rate? Is it okay to make this assumption then?

## 4. BE INTERNALLY CONSISTENT

- ▪ Risk and costs of equity and capital: Stable growth firms tend to
  - ▪ Have betas closer to one
  - ▪ Have debt ratios closer to industry averages (or mature company averages)
  - ▪ Country risk premiums (especially in emerging markets should evolve over time)
- ▪ The excess returns at stable growth firms should approach (or become) zero. ROC -> Cost of capital and ROE -> Cost of equity
- ▪ The reinvestment needs and dividend payout ratios should reflect the lower growth and excess returns:
  - ▪ Stable period payout ratio =  $1 - g/ROE$
  - ▪ Stable period reinvestment rate =  $g/ROC$