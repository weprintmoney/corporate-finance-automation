---
title: "Val"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/cfovhds/val.pdf
---

# Valuation

*Cynic: A person who knows the price of everything but the value of nothing..*

*Oscar Wilde*

### First Principles

- Invest in projects that yield a return greater than the minimum acceptable hurdle rate.
  - The hurdle rate should be higher for riskier projects and reflect the financing mix used - owners' funds (equity) or borrowed money (debt)
- Returns on projects should be measured based on cash flows generated and the timing of these cash flows; they should also consider both positive and negative side effects of these projects. Choose a financing mix that minimizes the hurdle rate and matches the assets being financed. If there are not enough investments that earn the hurdle rate, return the cash to stockholders.
  - The form of returns dividends and stock buybacks will depend upon the stockholders' characteristics.

**Objective: Maximize the Value of the Firm**

### Discounted Cashflow Valuation: Basis for Approach

- where,
- n = Life of the asset
- CFt = Cashflow in period t
- r = Discount rate reflecting the riskiness of the estimated cashflows

$$\text{Value} = \sum_{t=1}^t \frac{\text{CF}_t}{(1+r)^t}$$

### Equity Valuation

 The value of equity is obtained by discounting expected cashflows to equity, i.e., the residual cashflows after meeting all expenses, tax obligations and interest and principal payments, at the cost of equity, i.e., the rate of return required by equity investors in the firm.

where,

CF to Equityt = Expected Cashflow to Equity in period t

ke = Cost of Equity

 The dividend discount model is a specialized case of equity valuation, and the value of a stock is the present value of expected future dividends.

$$\text{Value of Equity} = \sum_{t=1}^{t=n} \frac{\text{CF to Equity}_t}{(1 + k_e)^t}$$

### Firm Valuation

 The value of the firm is obtained by discounting expected cashflows to the firm, i.e., the residual cashflows after meeting all operating expenses and taxes, but prior to debt payments, at the weighted average cost of capital, which is the cost of the different components of financing used by the firm, weighted by their market value proportions.

where,

CF to Firmt = Expected Cashflow to Firm in period t

WACC = Weighted Average Cost of Capital

$$\text{Value of Firm} = \sum_{t=1}^{t=n} \frac{\text{CF to Firm}_t}{(1 + \text{WACC})^t}$$

#### Generic DCF Valuation Model

![](_page_5_Diagram_1.jpeg)

## Estimating Inputs: I. Discount Rates

**Critical ingredient** in discounted cashflow valuation. Errors in estimating the discount rate or mismatching cashflows and discount rates can lead to serious errors in valuation. At an intuitive level, the discount rate used should be consistent with both the **riskiness** and the **type of cashflow** being discounted. The cost of equity is the rate at which we discount cash flows to equity (dividends or free cash flows to equity). The cost of capital is the rate at which we discount free cash flows to the firm.

### Estimating Aracruz's Cost of Equity

 We will do the Aracruz valuation in U.S. dollars. We will therefore use a U.S. dollar cost of equity. We estimated a beta for equity of 0.7576 for the paper business that Aracruz. With a nominal U.S. dollar riskfree rate of 4% and an equity risk premium of 12.49% for Brazil, we arrive at a dollar cost of equity of 13.46%

Cost of equity = 4% + 0.7576 (12.49%) = 13.46%

### Estimating Cost of Equity: Deutsche Bank

- Deutsche Bank is in two different segments of business commercial banking and investment banking.
  - To estimate its commercial banking beta, we will use the average beta of commercial banks in Germany.
- To estimate the investment banking beta, we will use the average bet of investment banks in the U.S and U.K. To estimate the cost of equity in Euros, we will use the German 10 year bond rate of 4.05% as the riskfree rate and the US historical risk premium (4.82%) as our proxy for a mature market premium.

| Business           | Beta   | Cost of Equity | Weights |
|--------------------|--------|----------------|---------|
| Commercial Banking | 0.7345 | 7.59%          | 69.03%  |
| Investment Banking | 1.5167 | 11.36%         | 30.97%  |
| Deutsche Bank      |        | 8.76%          |         |

# Reviewing Disney's Costs of Equity & Debt

| <i>Business</i>      | <i>Unlevered Beta</i> | <i>D/E Ratio</i> | <i>Levered Beta</i> | <i>Cost of Equity</i> |
|----------------------|-----------------------|------------------|---------------------|-----------------------|
| Media Networks       | 1.0850                | 26.62%           | 1.2661              | 10.10%                |
| Parks and Resorts    | 0.9105                | 26.62%           | 1.0625              | 9.12%                 |
| Studio Entertainment | 1.1435                | 26.62%           | 1.3344              | 10.43%                |
| Consumer Products    | 1.1353                | 26.62%           | 1.3248              | 10.39%                |
| Disney               | 1.0674                | 26.62%           | 1.2456              | 10.00%                |

- ■ Disney's Cost of Debt (based upon rating) = 5.25%
- ■ Disney's tax rate = 37.3%

### Current Cost of Capital: Disney

#### Equity

- Cost of Equity = Riskfree rate + Beta \* Risk Premium = 4% + 1.25 (4.82%) = 10.00%
- Market Value of Equity = \$55.101 Billion
- Equity/(Debt+Equity ) = 79%

#### Debt

- After-tax Cost of debt =(Riskfree rate + Default Spread) (1-t) = (4%+1.25%) (1-.373) = 3.29%
- Market Value of Debt = \$ 14.668 Billion
- Debt/(Debt +Equity) = 21%

Cost of Capital = 10.00%(.79)+3.29%(.21) = 8.59%

55.101(55.101+14. 668)

#### II. Estimating Cash Flows

![](_page_11_Diagram_1.jpeg)

### Estimating FCFE : Aracruz

|        |              |              |                | 2003            |        | numbers  | Normalized |        |          |
|--------|--------------|--------------|----------------|-----------------|--------|----------|------------|--------|----------|
| Net    | Income       | from         | operating      | assets \$119.68 |        | million  | \$         | 119.68 | million  |
| Net    | Capital      | Expenditures |                | (1-DR) \$       | 37.31  | million  | \$         | 71.45  | million  |
| -Chg.  | Working      |              | Capital*(1-DR) | \$              | 3.05   | million  | \$         | 7.50   | million  |
| Free   | Cashflow     | to           | Equity         | \$              | 79.32  | million  | \$         | 40.73  | million  |
| DR     | = Debt       | Ratio        | = Industry     | average book    |        | debt to  | capital    | ratio  | = 55.98% |
| Equity | Reinvestment |              | = 71.45        | million         | + 7.50 | million  | = \$       | 78.95  | million  |
| Equity | Reinvestment |              | Rate =         | 78.95/ 119.68   |        | = 65.97% |            |        |          |

### Estimating FCFF in 2003: Disney

EBIT = \$ 2,805 Million Tax rate = 37.30%

Capital spending = \$ 1,735 Million

Depreciation = \$ 1,254 Million

Increase in Non-cash Working capital = \$ 454 Million

Estimating FCFF

| EBIT * (1 - tax rate)      | \$1,759 | : 2805 (1-.373) |
|----------------------------|---------|-----------------|
| - Net Capital Expenditures | \$481   | : (1735 - 1254) |
| -Change in Working Capital | \$454   |                 |
| Free Cashflow to Firm      | \$824   |                 |

Total Reinvestment = Net Cap Ex + Change in WC = 481 + 454 = 935

Reinvestment Rate =935/1759 = 53.18%

## Application Test: Estimating your firm's FCFF

Estimate the FCFF for your firm in its most recent financial year:

In general, If using statement of cash flows

EBIT (1-t) EBIT (1-t)

+ Depreciation + Depreciation

- Capital Expenditures + Capital Expenditures

- Change in Non-cash WC + Change in Non-cash WC

= FCFF = FCFF

Estimate the dollar reinvestment at your firm:

Reinvestment = EBIT (1-t) - FCFF

#### Choosing a Cash Flow to Discount

 When you cannot estimate the free cash flows to equity or the firm, the only cash flow that you can discount is dividends. For financial service firms, it is difficult to estimate free cash flows. For Deutsche Bank, we will be discounting dividends. If a firm's debt ratio is not expected to change over time, the free cash flows to equity can be discounted to yield the value of equity. For Aracruz, we will discount free cash flows to equity. If a firm's debt ratio might change over time, free cash flows to equity become cumbersome to estimate. Here, we would discount free cash flows to the firm. For Disney, we will discount the free cash flow to the firm.

# III. Expected Growth

![](_page_16_Diagram_5.jpeg)

### Expected Growth in EPS

$$\begin{aligned} g_{\text{EPS}} &= \text{Retained Earnings}_{t-1} / \text{NI}_{t-1} * \text{ROE} \\ &= \text{Retention Ratio} * \text{ROE} \\ &= b * \text{ROE} \end{aligned}$$

- Proposition 1: The expected growth rate in earnings for a company cannot exceed its return on equity in the long term.

## Estimating Expected Growth in EPS: Deutsche Bank

- In 2003, Deutsche Bank reported net income of \$1,365 million on a book value of equity of \$29,991 million at the end of 2002.
- Return on Equity = Net Income2003/ Book Value of Equity2002 = 1365/29,991 = 4.55% This is lower than the cost of equity for the firm, which is 8.76%, and the average return on equity for European banks, which is 11.26%. In the four quarters ended in March 2004, Deutsche Bank paid out dividends per share of 1.50 Euros on earnings per share of 4.33 Euros.
- Retention Ratio = 1 Dividends per share/ Earnings per share = 1 1.50/4.33 = 65.36% If Deutsche maintains its existing return on equity and retention ratio for the long term, its expected growth rate will be anemic.
- Expected Growth Rate = Retention Ratio \* ROE = .6536\*.0455 = 2.97% For the next five years, we will assume that the return on equity will improve to the industry average of 11.26% while the retention ratio will stay unchanged at 65.36%. The expected growth in earnings per share is 7.36%.
  - Expected Growth Rate Modified Fundamentals = .6536 \* .1126 = .0736

## Estimating Expected Growth in Net Income: Aracruz

- Rather than base the equity reinvestment rate on the most recent year's numbers, we will use the average values for each of the variables over the last 6 years to compute a "normalized" equity reinvestment rate:
- Normalized Equity Reinvestment Rate = Average Equity Reinvestment99-03/ Average Net Income99-03 = 213.17/323.12 = 65.97% To estimate the return on equity, we look at only the portion of the net income that comes from operations (ignoring the income from cash and marketable securities) and divide by the book value of equity net of cash and marketable securities.
  - Non-cash ROE = (Net Income After-tax Interest income on cash)2003/ (BV of Equity – Cash)2002
- Non-cash ROEAracruz = (148.09 43.04(1-.34))/ (1760.58-273.93) = .0805 or 8.05% Expected Growth in Net Income = Equity Reinvestment Rate \* Non-cash ROE= 65.97% \* 8.05% = 5.31%

### ROE and Leverage

■ 
$$\text{ROE} = \text{ROC} + \text{D/E} (\text{ROC} - i (1-t))$$

where,

ROC = (EBIT (1 - tax rate)) / Book Value of Capital = EBIT (1- t) / Book Value of Capital

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / Book Value of Debt

t = Tax rate on ordinary income

Note that BV of Capital = BV of Debt + BV of Equity.

### Decomposing ROE

 Assume that you are analyzing a company with a 15% return on capital, an after-tax cost of debt of 5% and a book debt to capital ratio of 100%. Estimate the ROE for this company. Now assume that another company in the same sector has the same ROE as the company that you have just analyzed but no debt. Will these two firms have the same growth rates in earnings per share if they have the same dividend payout ratio? Will they have the same equity value?

### Expected Growth in EBIT And Fundamentals

Reinvestment Rate and Return on Capital

$$\begin{aligned} g_{EBIT} &= (\text{Net Capital Expenditures} + \text{Change in WC})/\text{EBIT}(1-t) * \text{ROC} \\ &= \text{Reinvestment Rate} * \text{ROC} \end{aligned}$$

 Proposition 2: No firm can expect its operating income to grow over time without reinvesting some of the operating income in net capital expenditures and/or working capital. Proposition 3: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.

### Estimating Growth in EBIT: Disney

- We begin by estimating the reinvestment rate and return on capital for Disney in 2003, using the numbers from the latest financial statements. We did convert operating leases into debt and adjusted the operating income and capital expenditure accordingly.
  - Reinvestment Rate2003 = (Cap Ex Depreciation + Chg in non-cash WC)/ EBIT (1
    - t) = (1735 1253 + 454)/(2805(1-.373)) = 53.18%
  - Return on capital2003 = EBIT (1-t)2003/ (BV of Debt2002 + BV of Equity2002) = 2805 (1-.373)/ (15,883+23,879) = 4.42%
- Expected Growth Rate from existing fundamentals = 53.18% \* 4.42% = 2.35% We will assume that Disney will be able to earn a return on capital of 12% on its new investments and that the reinvestment rate will be 53.18% for the immediate future.
  - Expected Growth Rate in operating income = Return on capital \* Reinvestment Rate = 12% \* .5318 = 6.38%

## Application Test: Estimating Expected Growth

- Estimate the following:
  - The reinvestment rate for your firm
  - The after-tax return on capital
  - The expected growth in operating income, based upon these inputs

### IV. Getting Closure in Valuation

 A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

 Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \sum_{t=1}^t \frac{\text{CF}_t}{(1+r)^t}$$

| Value | $t = N$ | $\frac{\text{CF}_t}{(1+r)^t}$ | $+ \frac{\text{Terminal Value}}{(1+r)^N}$ |
|-------|---------|-------------------------------|-------------------------------------------|
|       |         |                               |                                           |

### Stable Growth and Terminal Value

 When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

## $$g = \text{Expected growth rate}$$

 This "constant" growth rate is called a stable growth rate and cannot be higher than the growth rate of the economy in which the firm operates. While companies can maintain high growth rates for extended periods, they will all approach "stable growth" at some point in time. When they do approach stable growth, the valuation formula above can be used to estimate the "terminal value" of all cash flows beyond.

### Growth Patterns

- A key assumption in all discounted cash flow models is the period of high growth, and the pattern of growth during that period. In general, we can make one of three assumptions:
  - there is no high growth, in which case the firm is already in stable growth
  - there will be high growth for a period, at the end of which the growth rate will drop to the stable growth rate (2-stage)
- there will be high growth for a period, at the end of which the growth rate will decline gradually to a stable growth rate(3-stage) The assumption of how long high growth will continue will depend upon several factors including:
  - the size of the firm (larger firm -> shorter high growth periods)
  - current growth rate (if high -> longer high growth period)
  - barriers to entry and differential advantages (if high -> longer growth period)

### Length of High Growth Period

 Assume that you are analyzing two firms, both of which are enjoying high growth. The first firm is Earthlink Network, an internet service provider, which operates in an environment with few barriers to entry and extraordinary competition. The second firm is Biogen, a biotechnology firm which is enjoying growth from two drugs to which it owns patents for the next decade. Assuming that both firms are well managed, which of the two firms would you expect to have a longer high growth period? Earthlink Network Biogen Both are well managed and should have the same high growth period

### Choosing a Growth Period: Examples

|                              | <i>Disney</i>                                                                                                                                                          | <i>Aracruz</i>                                                                                                               | <i>Deutsche Bank</i>                                                                                   |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Firm Size/Market Size        | Firm is one of the largest players in the entertainment and theme park businesses but the businesses are red fining themselves and expanding.                          | Firm has a small market share of the paper/pulp business, but the business is mature.                                        | Firm has a significant market share of mature business.                                                |
| Current Excess Returns       | Firm is earning less than its cost of capital, and has done so for last few years                                                                                      | Returns on capital are largely a function of paper/pulp prices but, on average, have been less than the cost of capital.     | Firm has a return on equity that has lagged its cost of equity in recent years.                        |
| Competitive Advantages       | Has some of the most recognized brand names in the world. Knows more about operating theme parks than any other firm in the world. Has skilled animation studio staff. | Cost advantages because of access to Brazilian rainforests. Has invested in newer, updated plants and has skilled workforce. | Has an edge in the commercial banking business in Germany but this advantage is dissipating in the EU. |
| Length of High Growth period | 10 years, entirely because of its strong competitive advantages (which have been wasted over the last few years) but the excess returns are likely to be small.        | 5 years, largely due to access to cheap raw material and labor.                                                              | 5 years, mostly to allow firm to recover to pre-downturn levels.                                       |

### Firm Characteristics as Growth Changes

| Variable          | High Growth Firms tend to     | Stable Growth Firms tend to |
|-------------------|-------------------------------|-----------------------------|
| Risk              | be above-average risk         | be average risk             |
| Dividend Payout   | pay little or no dividends    | pay high dividends          |
| Net Cap Ex        | have high net cap ex          | have low net cap ex         |
| Return on Capital | earn high ROC (excess return) | earn ROC closer to WACC     |
| Leverage          | have little or no debt        | higher leverage             |

### Estimating Stable Growth Inputs

- Start with the fundamentals:
  - Profitability measures such as return on equity and capital, in stable growth, can be estimated by looking at
    - industry averages for these measure, in which case we assume that this firm in stable growth will look like the average firm in the industry
    - cost of equity and capital, in which case we assume that the firm will stop earning excess returns on its projects as a result of competition.
- Leverage is a tougher call. While industry averages can be used here as well, it depends upon how entrenched current management is and whether they are stubborn about their policy on leverage (If they are, use current leverage; if they are not; use industry averages) Use the relationship between growth and fundamentals to estimate payout and net capital expenditures.

### Estimating Stable Period Inputs: Disney

 The beta for the stock will drop to one, reflecting Disney's status as a mature company. This will lower the cost of equity for the firm to 8.82%.

Cost of Equity = Riskfree Rate + Beta \* Risk Premium = 4% + 4.82% = 8.82%

 The debt ratio for Disney will rise to 30%. This is the optimal we computed for Disney in chapter 8 and we are assuming that investor pressure will be the impetus for this change. Since we assume that the cost of debt remains unchanged at 5.25%, this will result in a cost of capital of 7.16%

Cost of capital = 8.82% (.70) + 5.25% (1-.373) (.30) = 7.16%

 The return on capital for Disney will drop from its high growth period level of 12% to a stable growth return of 10%. This is still higher than the cost of capital of 7.16% but the competitive advantages that Disney has are unlikely to dissipate completely by the end of the 10th year. The expected growth rate in stable growth will be 4%. In conjunction with the return on capital of 10%, this yields a stable period reinvestment rate of 40%:

Reinvestment Rate = Growth Rate / Return on Capital = 4% /10% = 40%

## A Dividend Discount Model Valuation: Deutsche Bank

 We estimated the annual growth rate for the next 5 years at Deutsche Bank to be 7.36%, based upon an estimated ROE of 11.26% and a retention ratio of 65.36%. In 2003, the earnings per share at Deutsche Bank were 4.33 Euros, and the dividend per share was 1.50 Euros. The resulting payout ratio is 34.64%. Our earlier analysis of the risk at Deutsche Bank provided us with an estimate of beta of 0.98, which used in conjunction with the Euro riskfree rate of 4.05% and a risk premium of 4.82%, yielded a cost of equity of 8.76%.

#### Expected Dividends and Terminal Value

| Year |         | EPS   | Payout      | Ratio     | DPS  | PV at 8.76% |
|------|---------|-------|-------------|-----------|------|-------------|
| 1    | !       | 4.65  | 34.64%      | !         | 1.61 | ! 1.48      |
| 2    | !       | 4.99  | 34.64%      | !         | 1.73 | ! 1.46      |
| 3    | !       | 5.36  | 34.64%      | !         | 1.86 | ! 1.44      |
| 4    | !       | 5.75  | 34.64%      | !         | 1.99 | ! 1.42      |
| 5    | !       | 6.18  | 34.64%      | !         | 2.14 | ! 1.41      |
|      | Present | value | of expected | dividends | =    | ! 7.22      |

EPS and DPS grow at 7.36% a year for next 5 years

#### Terminal Value and Present Value…

- At the end of year 5, we will assume that Deutsche Bank's earnings growth will drop to 4% and stay at that level in perpetuity. In keeping with the assumption of stable growth, we will also assume that
  - The beta will rise marginally to 1, resulting in a slightly higher cost of equity of 8.87%. Cost of Equity = Riskfree Rate + Beta \* Risk Premium = 4.05%+ 4.82% = 8.87%
  - The return on equity will drop to the cost of equity of 8.87%, thus preventing excess returns from being earned in perpetuity. Stable Period Payout Ratio = 1 – g/ ROE = 1- .04/.0887 = .5490 or 54.9% Expected Dividends in year 6 = Expected EPS6 \* Stable period payout ratio =€6.18 (1.04) \* .549 = €3.5263
  - Terminal Value per share = Expected Dividends in year 6/ (Cost of equity g) = €3.5263/(.0887 - .04) = €72.41
- Present value of terminal value = 72.41/1.08765 = 47.58 Value per share = PV of expected dividends in high growth + PV of terminal value = €7.22 + €47.58 = €54.80 Deutsche Bank was trading at €66 at the time of this analysis.

## What does the valuation tell us? One of three possibilities…

 Stock is overvalued: This valuation would suggest that Deutsche Bank is significantly overvalued, given our estimates of expected growth and risk. Dividends may not reflect the cash flows generated by Deutsche Bank. The FCFE could have been significantly higher than the dividends paid. Estimates of growth and risk are wrong: It is also possible that we have underestimated growth or overestimated risk in the model, thus reducing our estimate of value.

#### The cash problem…

- One of the problems with using total net income and discounting the resulting cash flows to equity is that net income comes from both operating and non-operating assets. In particular, a portion of net income comes from a firm's cash holdings, which are generally invested in riskless or close to riskless assets. We have two choices in equity valuation:
  - We can discount aggregate cash flows to equity at a cost of equity that incorporates the effect of cash (lower unlevered beta -> lower cost of equity)
  - We can discount equity cash flows from operations at a cost of equity that reflects only operating assets (unlevered beta of business) and add cash and non-operating assets to this value.

### A FCFE Valuation: Aracruz Celulose

- The net income for the firm in 2003 was \$148.09 million but \$28.41 million of this income represented income from financial assets. The net income from non-operating assets is \$119.68 million. Inputs estimated for high growth period
  - Expected Growth in Net Income = Equity Reinvestment Rate \* Non-cash ROE = 65.97% \* 8.05% = 5.31%
- Cost of equity = 4% + 0.7576 (12.49%) = 13.46% After year 5, we will assume that the beta will remain at 0.7576 and that the equity risk premium will decline to 8.66%.
  - Cost of equity in stable growth = 4% + 0.7576 (8.66%) = 10.56%
  - We will also assume that the growth in net income will drop to the inflation rate (in U.S. dollar terms) of 2% and that the return on equity will rise to 10.56% (which is also the cost of equity).
  - Equity Reinvestment RateStable Growth = Expected Growth Rate/ Return on Equity = 2%/10.56% = 18.94%

### Aracruz: Estimating FCFE for next 5 years

|                          | 1        | 2        | 3        | 4        | 5        |
|--------------------------|----------|----------|----------|----------|----------|
| Net Income (non-cash)    | \$126.04 | \$132.74 | \$139.79 | \$147.21 | \$155.03 |
| Equity Reinvestment Rate | 65.97%   | 65.97%   | 65.97%   | 65.97%   | 65.97%   |
| FCFE                     | \$42.89  | \$45.17  | \$47.57  | \$50.09  | \$52.75  |
| Present Value at 10.33%  | \$37.80  | \$35.09  | \$32.56  | \$30.23  | \$28.05  |

- FCFE in year 6 = Net Income in year 6 (1- Equity Reinvestment RateStable Growth) = 155.03 (1.02) (1- .1894) = \$128.18 million
- Terminal value of equity = 128.18/(.1056-.02) = \$1497.98 million

Present Value of FCFEs in high growth phase = \$163.73

+ Present Value of Terminal Equity Value = 
$$1497.98/1.1346^5 = \$796.55$$

Value of equity in operating assets = \$960.28

+ Value of Cash and Marketable Securities = \$352.28

Value of equity in firm = \$1,312.56

Value of equity/share = \$1,312.56/859.59 = \$1.53/share

Value of equity/share in BR = \$1.53 \* 3.15 BR/\$ = 4.81 BR/share

Stock price 7.50 BR/share

#### Disney Valuation

#### Model Used:

- Cash Flow: FCFF (since I think leverage will change over time)
- Growth Pattern: 3-stage Model (even though growth in operating income is only 10%, there are substantial barriers to entry)

### Disney: Inputs to Valuation

|                                                                      | <i>High Growth Phase</i>                                                             | <i>Transition Phase</i>                                                                           | <i>Stable Growth Phase</i>                                                                                                                |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Length of Period                                                     | 5 years                                                                              | 5 years                                                                                           | Forever after 10 years                                                                                                                    |
| Tax Rate                                                             | 37.3%                                                                                | 37.3%                                                                                             | 37.3%                                                                                                                                     |
| Return on Capital                                                    | 12% (last year's return on capital was 4.42%)                                        | Declines linearly to 10%                                                                          | Stable ROC of 10%                                                                                                                         |
| Reinvestment Rate<br>(Net Cap Ex + Working Capital Investments/EBIT) | 53.18% (Last year's reinvestment rate)                                               | Declines to 40% as ROC and growth rates drop:<br>Reinvestment Rate = g/ROC                        | 40% of after-tax operating income, estimated from stable growth rate of 4% and return on capital of 10%.<br>Reinvestment rate = 4/10 =40% |
| Expected Growth Rate in EBIT                                         | ROC * Reinvestment Rate = 12%*0.5318 = 6.38%                                         | Linear decline to Stable Growth Rate of 4%                                                        | 4%: Set to riskfree rate                                                                                                                  |
| Debt/Capital Ratio                                                   | 21% (Existing debt ratio)                                                            | Increases linearly to 30%                                                                         | Stable debt ratio of 30%                                                                                                                  |
| Risk Parameters                                                      | Beta = 1.25, k <sub>e</sub> = 10%<br>Cost of Debt = 5.25%<br>Cost of capital = 8.59% | Beta decreases linearly to 1.00;<br>Cost of debt stays at 5.25%<br>Cost of capital drops to 7.16% | Beta = 1.00; k <sub>e</sub> = 8.82%<br>Cost of debt stays at 5.25%<br>Cost of capital = 7.16%                                             |

### Disney: FCFF Estimates

| Growth  |       | EBIT    |          |        |              |            |
|---------|-------|---------|----------|--------|--------------|------------|
|         |       |         | EBIT (1- |        |              |            |
|         |       |         |          | Rate   | Reinvestment | FCFF       |
| Current |       | \$2,805 |          |        |              |            |
| 1       | 6.38% | \$2,984 | \$1,871  | 53.18% | \$994.92     | \$876.06   |
| 2       | 6.38% | \$3,174 | \$1,990  | 53.18% | \$1,058.41   | \$931.96   |
| 3       | 6.38% | \$3,377 | \$2,117  | 53.18% | \$1,125.94   | \$991.43   |
| 4       | 6.38% | \$3,592 | \$2,252  | 53.18% | \$1,197.79   | \$1,054.70 |
| 5       | 6.38% | \$3,822 | \$2,396  | 53.18% | \$1,274.23   | \$1,122.00 |
| 6       | 5.90% | \$4,047 | \$2,538  | 50.54% | \$1,282.59   | \$1,255.13 |
| 7       | 5.43% | \$4,267 | \$2,675  | 47.91% | \$1,281.71   | \$1,393.77 |
| 8       | 4.95% | \$4,478 | \$2,808  | 45.27% | \$1,271.19   | \$1,536.80 |
| 9       | 4.48% | \$4,679 | \$2,934  | 42.64% | \$1,250.78   | \$1,682.90 |
| 10      | 4.00% | \$4,866 | \$3,051  | 40.00% | \$1,220.41   | \$1,830.62 |

#### Disney: Costs of Capital and Present Value

| Year  | Cost of capital  | FCFF          | PV of FCFF |
|-------|------------------|---------------|------------|
| 1     | 8.59%            | \$876.06      | \$806.74   |
| 2     | 8.59%            | \$931.96      | \$790.31   |
| 3     | 8.59%            | \$991.43      | \$774.21   |
| 4     | 8.59%            | \$1,054.70    | \$758.45   |
| 5     | 8.59%            | \$1,122.00    | \$743.00   |
| 6     | 8.31%            | \$1,255.13    | \$767.42   |
| 7     | 8.02%            | \$1,393.77    | \$788.91   |
| 8     | 7.73%            | \$1,536.80    | \$807.42   |
| 9     | 7.45%            | \$1,682.90    | \$822.90   |
| 10    | 7.16%            | \$1,830.62    | \$835.31   |
| PV of | cashflows during | high growth = | \$7,894.66 |

### Disney: Terminal Value and Firm Value

#### Terminal Value

- $$\text{FCFF}_{11} = \text{EBIT}_{11} (1\text{-t}) (1 - \text{Reinvestment Rate}_{\text{Stable Growth}}) / (= 4866 (1.04) (1\text{-.40}) = \$1,903.84 \text{ million})$$
- $\text{Terminal Value} = \text{FCFF}_{11} / (\text{Cost of capital}_{\text{Stable Growth}} - g) = 1903.84 / (.0716 - .04) = \$60,219.11 \text{ million}$

#### Value of firm

PV of cashflows during the high growth phase =\$ 7,894.66 PV of terminal value = PV of \$60,219 in 10 years =\$ 27,477.81 + Cash and Marketable Securities =\$ 1,583.00 + Non-operating Assets (Holdings in other companies) =\$ 1,849.00 Value of the firm =\$ 38,804.48

## From Firm to Equity Value: What do you subtract out?

- The first thing you have to subtract out is the debt that you computed (and used in estimating the cost of capital). If you have capitalized operating leases, you should continue to treat operating leases as debt in this stage in the process. This is also your last chance to consider other potential liabilities that may be faced by the firm including
  - *Expected liabilities on lawsuits*: You could be analyzing a firm that is the defendant in a lawsuit, where it potentially could have to pay tens of millions of dollars in damages. You should estimate the probability that this will occur and use this probability to estimate the expected liability.
  - *Unfunded Pension and Health Care Obligations*: If a firm has significantly under funded a pension or a health plan, it will need to set aside cash in future years to meet these obligations. While it would not be considered debt for cost of capital purposes, it should be subtracted from firm value to arrive at equity value.
  - *Deferred Tax Liability*: The deferred tax liability that shows up on the financial statements of many firms reflects the fact that firms often use strategies that reduce their taxes in the current year while increasing their taxes in the future years.

## From Equity Value to Equity Value per share: The Effect of Options

- When there are warrants and employee options outstanding, the estimated value of these options has to be subtracted from the value of the equity, before we divide by the number of shares outstanding. There are two alternative approaches that are used in practice:
  - One is to divide the value of equity by the *fully diluted number of shares* outstanding rather than by the actual number. This approach will underestimate the value of the equity, because it fails to consider the cash proceeds from option exercise.
  - The other shortcut, which is called the *treasury stock approach*, adds the expected proceeds from the exercise of the options (exercise price multiplied by the number of options outstanding) to the numerator before dividing by the number of shares outstanding. While this approach will yield a more reasonable estimate than the first one, it does not include the time value of the options outstanding.

#### Valuing Disney's options…

 At the end of 2003, Disney had 219 million options outstanding, with a weighted average exercise price of \$26.44 and weighted average life of 6 years. Using the current stock price of \$26.91, an estimated standard deviation of 40, a dividend yield of 1.21%. a riskfree rate of 4% and the Black-Scholes option pricing model we arrived at a value of \$2,129 million. Since options expenses are tax-deductible, we used the tax rate of 37.30% to estimate the value of the employee options: Value of employee options = 2129 (1- .373) = \$1334.67 million

### Disney: Value of Equity per Share

 Subtracting out the market value of debt (including operating leases) of \$14,668.22 million and the value of the equity options (estimated to be worth \$1,334.67 million in illustration 12.10) yields the value of the common stock: Value of equity in common stock = Value of firm – Debt – Equity Options = \$38,804.48 - \$14,668.22 - \$1334.67 = \$ 22,801.59 Dividing by the number of shares outstanding (2047.60 million), we arrive at a value per share of \$11.14, well below the market price of \$ 26.91 at the time of this valuation.

**Current Cashflow to Firm** EBIT(1-t) : 1,759 - Nt CpX 481 - Chg WC 454 = FCFF \$ 824 Reinvestment Rate=(481+454)/1759 = 53.18%

**Expected Growth in EBIT (1-t)** .5318\*.12=.0638 **6.38%**

Stable Growth g = 4%; Beta = 1.00; Cost of capital = 7.16% ROC= 10% Reinvestment Rate=g/ROC =4/ 10= 40%

Terminal Value10= 1,904/(.0716-.04) = 60,219

**Cost of Equity 10%**

**Cost of Debt** (4.00%+1.25%)(1-.373) = 3.29%

**Weights** E = 79% D = 21%

Discount at Cost of Capital (WACC) = 10.00% (.79) + 3.29% (0.21) = 8.59

Op. Assets 35,373 + Cash: 3,432 +Other Inv - Debt 14,668 =Equity 24,136 - Options 1,335 =Equity CS 22,802 Value/Sh \$11.14

> **Riskfree Rate**: Riskfree Rate= 4%

+ **Beta**  1.2456 **X** Unlevered Beta for Sectors: 1.0674

**Mature market premium** 4%

Firm!s D/E Ratio: 24.77%

#### Disney: Valuation

Reinvestment Rate 53.18%%

Return on Capital 12%

> Term Yr 3089 - 864 = 2225

Disney was trading at about \$ 26 at the time of this valuation.

Cashflows

EBIT (1-t) \$1,871 \$1,990 \$2,117 \$2,252 \$2,396 \$2,538 \$2,675 \$2,808 \$2,934 \$3,051 - Reinvestment \$995 \$1,058 \$1,126 \$1,198 \$1,274 \$1,283 \$1,282 \$1,271 \$1,251 \$1,220 FCFF \$876 \$932 \$991 \$1,055 \$1,122 \$1,255 \$1,394 \$1,537 \$1,683 \$1,831

> In transition phase, debt ratio increases to 30% and cost of capital decreases to 7.16%

Growth drops to 4%

| Current EBIT (1-t) | Expected Growth Rate = 12% * 53.18% | Cost of capital = 10% (.79) + 3.29% (.21) = 8.59% |
|--------------------|-------------------------------------|---------------------------------------------------|
| \$ 1,759           | = 6.38%                             |                                                   |

![](_page_50_Diagram_2.jpeg)

#### Investment decision affects risk of assets being finance and financing decision affects hurdle rate

| Year           | Expected Growth | EBIT    | EBIT (1-t) | Reinvestment | Rate Reinvestment | FCFF                   | Cost of capital | PV of FCFF  |
|----------------|-----------------|---------|------------|--------------|-------------------|------------------------|-----------------|-------------|
| Current        |                 | \$2,805 |            |              |                   |                        |                 |             |
| 1              | 6.38%           | \$2,984 | \$1,871    | 53.18%       | \$994.92          | \$876.06               | 8.59%           | \$806.74    |
| 2              | 6.38%           | \$3,174 | \$1,990    | 53.18%       | \$1,058.41        | \$931.96               | 8.59%           | \$790.31    |
| 3              | 6.38%           | \$3,377 | \$2,117    | 53.18%       | \$1,125.94        | \$991.43               | 8.59%           | \$774.22    |
| 4              | 6.38%           | \$3,592 | \$2,252    | 53.18%       | \$1,197.79        | \$1,054.70             | 8.59%           | \$758.45    |
| 5              | 6.38%           | \$3,822 | \$2,396    | 53.18%       | \$1,274.23        | \$1,122.00             | 8.59%           | \$743.00    |
| 6              | 5.90%           | \$4,047 | \$2,538    | 50.54%       | \$1,282.59        | \$1,255.13             | 8.31%           | \$767.42    |
| 7              | 5.43%           | \$4,267 | \$2,675    | 47.91%       | \$1,281.71        | \$1,393.77             | 8.02%           | \$788.92    |
| 8              | 4.95%           | \$4,478 | \$2,808    | 45.27%       | \$1,271.19        | \$1,536.80             | 7.73%           | \$807.43    |
| 9              | 4.48%           | \$4,679 | \$2,934    | 42.64%       | \$1,250.78        | \$1,682.90             | 7.45%           | \$822.90    |
| 10             | 4.00%           | \$4,866 | \$3,051    | 40.00%       | \$1,220.41        | \$1,830.62             | 7.16%           | \$835.31    |
| Terminal Value |                 |         |            |              |                   | \$60,219.11            |                 | \$27,477.93 |
|                |                 |         |            |              |                   | Value per share        |                 |             |
|                |                 |         |            |              |                   | + Cash & Non-op Assets | =               |             |

![](_page_51_Diagram_2.jpeg)

#### Investment decision affects risk of assets being finance and financing decision affects hurdle rate

### Relative Valuation

- In relative valuation, the value of an asset is derived from the pricing of 'comparable' assets, standardized using a common variable such as earnings, cashflows, book value or revenues. Examples include --
  - Price/Earnings (P/E) ratios
    - and variants (EBIT multiples, EBITDA multiples, Cash Flow multiples)
  - Price/Book (P/BV) ratios
    - and variants (Tobin's Q)
  - Price/Sales ratios

### Multiples and Fundamenals

- ■ Gordon Growth Model:  $P_0 = \frac{DPS_1}{r - g_n}$
- ■ Dividing both sides by the earnings,

Dividing both sides by the book value of equity,

 If the return on equity is written in terms of the retention ratio and the expected growth rate

Dividing by the Sales per share,

| $\frac{P_0}{\text{EPS}_0} = \text{PE} =$ | Payout Ratio * ( $1 + g_n$ ) |
|------------------------------------------|------------------------------|
| $r - g_n$                                |                              |

$$\frac{P_0}{BV_0} = PBV = \frac{ROE - g_n}{r - g_n}$$

$$\frac{P_0}{BV_0} = PBV = \frac{ROE * Payout Ratio * (1 + g_n)}{r - g_n}$$

| $\frac{P_0}{\text{Sales}_0} = PS =$ | Profit Margin * Payout Ratio * (1 + $g_n$ ) |
|-------------------------------------|---------------------------------------------|
|                                     | $r - g_n$                                   |

### Disney: Relative Valuation

|               | Company Name    | Ticker Symbol | PE     | Expected Growth Rate | PEG  |
|---------------|-----------------|---------------|--------|----------------------|------|
| Point         | 360             | PTSX          | 10.62  | 5.00%                | 2.12 |
| Fox           | Entmt Group Inc | FOX           | 22.03  | 14.46%               | 1.52 |
| Belo          | Corp. 'A'       | BLC           | 25.65  | 16.00%               | 1.60 |
| Hearst-Argyle | Television      | Inc HTV       | 26.72  | 12.90%               | 2.07 |
| Journal       | Communications  | Inc. JRN      | 27.94  | 10.00%               | 2.79 |
| Saga          | Communic.       |               |        |                      |      |
|               | 'A '            | SGA           | 28.42  | 19.00%               | 1.50 |
| Viacom        | Inc.            |               |        |                      |      |
|               | 'B'             | VIA/B         | 29.38  | 13.50%               | 2.18 |
| Pixar         |                 | PIXR          | 29.80  | 16.50%               | 1.81 |
| Disney        | (Walt)          | DIS           | 29.87  | 12.00%               | 2.49 |
| Westwood      | One             | WON           | 32.59  | 19.50%               | 1.67 |
| World         | Wrestling Ent.  | WWE           | 33.52  | 20.00%               | 1.68 |
| Cox           | Radio 'A' Inc   | CXR           | 33.76  | 18.70%               | 1.81 |
| Beasley       | Broadcast Group | Inc BBGI      | 34.06  | 15.23%               | 2.24 |
| Entercom      | Comm. Corp      | ETM           | 36.11  | 15.43%               | 2.34 |
| Liberty       | Corp.           | LC            | 37.54  | 19.50%               | 1.92 |
| Ballantyne    | of Omaha Inc    | BTNE          | 55.17  | 17.10%               | 3.23 |
| Regent        | Communications  | Inc RGCI      | 57.84  | 22.67%               | 2.55 |
| Emmis         | Communications  | EMMS          | 74.89  | 16.50%               | 4.54 |
| Cumulus       | Media Inc       | CMLS          | 94.35  | 23.30%               | 4.05 |
| Univision     | Communic.       | UVN           | 122.76 | 24.50%               | 5.01 |
| Salem         | Communications  | Corp SALM     | 145.67 | 28.75%               | 5.07 |
| Average       | for sector      |               | 47.08  | 17.17%               | 2.74 |

### Is Disney fairly valued?

 Based upon the PE ratio, is Disney under, over or correctly valued? Under Valued Over Valued Correctly Valued Based upon the PEG ratio, is Disney under valued? Under Valued Over Valued Correctly Valued Will this valuation give you a higher or lower valuation than the discounted cashflow valuation? Higher Lower

### Relative Valuation Assumptions

 Assume that you are reading an equity research report where a buy recommendation for a company is being based upon the fact that its PE ratio is lower than the average for the industry. Implicitly, what is the underlying assumption or assumptions being made by this analyst? The sector itself is, on average, fairly priced The earnings of the firms in the group are being measured consistently The firms in the group are all of equivalent risk The firms in the group are all at the same stage in the growth cycle The firms in the group are of equivalent risk and have similar cash flow patterns All of the above

### First Principles

- Invest in projects that yield a return greater than the minimum acceptable hurdle rate.
  - The hurdle rate should be higher for riskier projects and reflect the financing mix used - owners' funds (equity) or borrowed money (debt)
- Returns on projects should be measured based on cash flows generated and the timing of these cash flows; they should also consider both positive and negative side effects of these projects. Choose a financing mix that minimizes the hurdle rate and matches the assets being financed. If there are not enough investments that earn the hurdle rate, return the cash to stockholders.
  - The form of returns dividends and stock buybacks will depend upon the stockholders' characteristics.

**Objective: Maximize the Value of the Firm**