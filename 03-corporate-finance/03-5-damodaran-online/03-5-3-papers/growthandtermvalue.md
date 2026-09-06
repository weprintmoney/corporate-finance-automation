---
title: "Growthandtermvalue"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/ovhds/dam2ed/growthandtermvalue.pdf
---

# Growth Rates and Terminal Value

DCF Valuation

# Ways of Estimating Growth in Earnings

- Look at the past
- The historical growth in earnings per share is usually a good starting point for growth estimation Look at what others are estimating
- Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are. Look at fundamentals
  - Ultimately, all growth in earnings can be traced to two fundamentals how much the firm is investing in new projects, and what returns these projects are making for the firm.

# I. Historical Growth in EPS

- Historical growth rates can be estimated in a number of different ways
  - Arithmetic versus Geometric Averages
- Simple versus Regression Models Historical growth rates can be sensitive to
- the period used in the estimation In using historical growth rates, the following factors have to be considered
  - how to deal with negative earnings
  - the effect of changing size

# Motorola: Arithmetic versus Geometric Growth Rates

|                    | Revenues  | % Change | EBITDA   | % Change | EBIT     | % Change |
|--------------------|-----------|----------|----------|----------|----------|----------|
| 1994               | \$ 22,245 |          | \$ 4,151 |          | \$ 2,604 |          |
| 1995               | \$ 27,037 | 21.54%   | \$ 4,850 | 16.84%   | \$ 2,931 | 12.56%   |
| 1996               | \$ 27,973 | 3.46%    | \$ 4,268 | -12.00%  | \$ 1,960 | -33.13%  |
| 1997               | \$ 29,794 | 6.51%    | \$ 4,276 | 0.19%    | \$ 1,947 | -0.66%   |
| 1998               | \$ 29,398 | -1.33%   | \$ 3,019 | -29.40%  | \$ 822   | -57.78%  |
| 1999               | \$ 30,931 | 5.21%    | \$ 5,398 | 78.80%   | \$ 3,216 | 291.24%  |
| Arithmetic Average |           | 7.08%    |          | 10.89%   |          | 42.45%   |
| Geometric Average  |           | 6.82%    |          | 5.39%    |          | 4.31%    |
| Standard deviation |           | 8.61%    |          | 41.56%   |          | 141.78%  |

# Cisco: Linear and Log-Linear Models for Growth

| Year | EPS     | ln(EPS) |
|------|---------|---------|
| 1991 | \$ 0.01 | -4.6052 |
| 1992 | \$ 0.02 | -3.9120 |
| 1993 | \$ 0.04 | -3.2189 |
| 1994 | \$ 0.07 | -2.6593 |
| 1995 | \$ 0.08 | -2.5257 |
| 1996 | \$ 0.16 | -1.8326 |
| 1997 | \$ 0.18 | -1.7148 |
| 1998 | \$ 0.25 | -1.3863 |
| 1999 | \$ 0.32 | -1.1394 |

 EPS = -.066 + 0.0383 ( t): EPS grows by \$0.0383 a year Growth Rate = \$0.0383/\$0.13 = 30.5% (\$0.13: Average EPS from 91-99) ln(EPS) = -4.66 + 0.4212 (t): Growth rate approximately 42.12%

# A Test

 You are trying to estimate the growth rate in earnings per share at Time Warner from 1996 to 1997. In 1996, the earnings per share was a deficit of \$0.05. In 1997, the expected earnings per share is \$ 0.25. What is the growth rate? -600% +600% +120% Cannot be estimated

# Dealing with Negative Earnings

- When the earnings in the starting period are negative, the growth rate cannot be estimated. (0.30/-0.05 = -600%) There are three solutions:
  - Use the higher of the two numbers as the denominator (0.30/0.25 = 120%)
  - Use the absolute value of earnings in the starting period as the denominator (0.30/0.05=600%)
- Use a linear regression model and divide the coefficient by the average earnings. When earnings are negative, the growth rate is meaningless. Thus, while the growth rate can be estimated, it does not tell you much about the future.

# The Effect of Size on Growth: Callaway Golf

| Year | Net Profit | Growth Rate |
|------|------------|-------------|
| 1990 | 1.80       |             |
| 1991 | 6.40       | 255.56%     |
| 1992 | 19.30      | 201.56%     |
| 1993 | 41.20      | 113.47%     |
| 1994 | 78.00      | 89.32%      |
| 1995 | 97.70      | 25.26%      |
| 1996 | 122.30     | 25.18%      |

Geometric Average Growth Rate = 102%

# Extrapolation and its Dangers

| Year |             | Net Profit |
|------|-------------|------------|
| 1996 | \$          | 122.30     |
| 1997 | \$          | 247.05     |
| 1998 | \$          | 499.03     |
| 1999 | \$ 1,008.05 |            |
| 2000 | \$ 2,036.25 |            |
| 2001 | \$ 4,113.23 |            |

 If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

# II. Analyst Forecasts of Growth

- While the job of an analyst is to find under and over valued stocks in the sectors that they follow, a significant proportion of an analyst's time (outside of selling) is spent forecasting earnings per share.
  - Most of this time, in turn, is spent forecasting earnings per share in the next earnings report
- While many analysts forecast expected growth in earnings per share over the next 5 years, the analysis and information (generally) that goes into this estimate is far more limited. Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

# How good are analysts at forecasting growth?

 Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| Study             | Time Period          | Analyst Forecast Error | Time Series Model |
|-------------------|----------------------|------------------------|-------------------|
| Collins & Hopwood | Value Line Forecasts | 31.7%                  | 34.1%             |
| Brown & Rozeff    | Value Line Forecasts | 28.4%                  | 32.2%             |
| Fried & Givoly    | Earnings Forecaster  | 16.4%                  | 19.8%             |

- The advantage that analysts have over time series models
  - tends to decrease with the forecast period (next quarter versus 5 years)
  - tends to be greater for larger firms than for smaller firms
- tends to be greater at the industry level than at the company level Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

# Are some analysts more equal than others?

- A study of All-America Analysts (chosen by Institutional Investor) found that
  - There is no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%)
  - However, in the calendar year following being chosen as All-America analysts, these analysts become slightly better forecasters than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts)
  - Earnings revisions made by All-America analysts tend to have a much greater impact on the stock price than revisions from other analysts
  - The recommendations made by the All America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (2.4% for buys; 13.8% for the sells).

# The Five Deadly Sins of an Analyst

**Tunnel Vision**: Becoming so focused on the sector and valuations within the sector that you lose sight of the bigger picture. **Lemmingitis**:Strong urge felt to change recommendations & revise earnings estimates when other analysts do the same. **Stockholm Syndrome**: Refers to analysts who start identifying with the managers of the firms that they are supposed to follow. **Factophobia** (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a "story" coupled with a refusal to face the facts. **Dr. Jekyll/Mr.Hyde**: Analyst who thinks his primary job is to bring in investment banking business to the firm.

# Propositions about Analyst Growth Rates

- **Proposition 1**: There if far less private information and far more public information in most analyst forecasts than is generally claimed. **Proposition 2**: The biggest source of private information for analysts remains the company itself which might explain
  - why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources)
  - why there is such a high correlation across analysts forecasts and revisions
- why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team. **Proposition 3**: There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

### III. Fundamental Growth Rates

![](_page_14_Diagram_1.jpeg)

# Growth Rate Derivations

In the special case where ROI on existing projects remains unchanged and is equal to the ROI on new projects

$$\begin{aligned}
 \text{Investment in New Projects} & \times \text{Return on Investment} = \text{Change in Earnings} \\
 \text{Current Earnings} & \times 12\% = \frac{\$12}{\$120} \\
 \text{Reinvestment Rate} & \times \text{Return on Investment} = \text{Growth Rate in Earnings} \\
 83.33\% & \times 12\% = 10\%
 \end{aligned}$$

in the more general case where ROI can change from period to period, this can be expanded as follows:

$$\text{Investment in Existing Projects} \times (\text{Change in ROI}) + \text{New Projects (ROI)} = \text{Change in Earnings} \\
 \text{Investment in Existing Projects} \times \text{Current ROI} = \text{Current Earnings}$$

For instance, if the ROI increases from 12% to 13%, the expected growth rate can be written as follows:

$$\frac{\$1,000 \times (.13 - .12) + 100 (13\%)}{\$ 1000 \times .12} = \frac{\$23}{\$120} = 19.17\%$$

# I. Expected Long Term Growth in EPS

 When looking at growth in earnings per share, these inputs can be cast as follows: Reinvestment Rate = Retained Earnings/ Current Earnings = Retention Ratio Return on Investment = ROE = Net Income/Book Value of Equity In the special case where the current ROE is expected to remain unchanged gEPS = Retained Earningst-1/ NIt-1 \* ROE = Retention Ratio \* ROE = b \* ROE Proposition 1: The expected growth rate in earnings for a company cannot exceed its return on equity in the long term.

# Estimating Expected Growth in EPS: ABN Amro

 Current Return on Equity = 15.79% Current Retention Ratio = 1 - DPS/EPS = 1 - 1.13/2.45 = 53.88% If ABN Amro can maintain its current ROE and retention ratio, its expected growth in EPS will be:

Expected Growth Rate = 0.5388 (15.79%) = 8.51%

# Expected ROE changes and Growth

 Assume now that ABN Amro's ROE next year is expected to increase to 17%, while its retention ratio remains at 53.88%. What is the new expected long term growth rate in earnings per share? Will the expected growth rate in earnings per share next year be greater than, less than or equal to this estimate? greater than less than equal to

# Changes in ROE and Expected Growth

When the ROE is expected to change,

$$g_{\text{EPS}} = b * \text{ROE}_{t+1} + (\text{ROE}_{t+1} - \text{ROE}_t) / \text{ROE}_t$$

- Proposition 2: Small changes in ROE translate into large changes in the expected growth rate.
- The lower the current ROE, the greater the effect on growth of changes in the ROE. Proposition 3: No firm can, in the long term, sustain growth in earnings per share from improvement in ROE.
  - Corollary: The higher the existing ROE of the company (relative to the business in which it operates) and the more competitive the business in which it operates, the smaller the scope for improvement in ROE.

# Changes in ROE: ABN Amro

 Assume now that ABN's expansion into Asia will push up the ROE to 17%, while the retention ratio will remain 53.88%. The expected growth rate in that year will be:

| $\mathcal{G}_{\text{EPS}}$ | $= b * \text{ROE}_{t+1} + (\text{ROE}_{t+1} - \text{ROE}_t) / \text{ROE}_t$ $= (.5388)(.17) + (.17 - .1579) / (.1579)$ $= 16.83\%$ |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------|

 Note that 1.21% improvement in ROE translates into almost a doubling of the growth rate from 8.51% to 16.83%.

# ROE and Leverage

ROE = ROC + D/E (ROC - i (1-t))

where,

ROC = EBITt (1 - tax rate) / Book value of Capitalt-1

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / BV of Debt

t = Tax rate on ordinary income

Note that Book value of capital = Book Value of Debt + Book value of Equity.

# Decomposing ROE: Brahma in 1998

- Real Return on Capital = 687 (1-.32) / (1326+542+478) = 19.91%
- This is assumed to be real because both the book value and income are inflation adjusted. Debt/Equity Ratio = (542+478)/1326 = 0.77 After-tax Cost of Debt = 8.25% (1-.32) = 5.61% (Real BR) Return on Equity = ROC + D/E (ROC - i(1-t)) 19.91% + 0.77 (19.91% - 5.61%) = 30.92%

# Decomposing ROE: Titan Watches (India)

 Return on Capital = 713 (1-.25)/(1925+2378+1303) = 9.54% Debt/Equity Ratio = (2378 + 1303)/1925 = 1.91 After-tax Cost of Debt = 13.5% (1-.25) = 10.125% Return on Equity = ROC + D/E (ROC - i(1-t)) 9.54% + 1.91 (9.54% - 10.125%) = 8.42%

# II. Expected Growth in Net Income

 The limitation of the EPS fundamental growth equation is that it focuses on per share earnings and assumes that reinvested earnings are invested in projects earning the return on equity. A more general version of expected growth in earnings can be obtained by substituting in the equity reinvestment into real investments (net capital expenditures and working capital): Equity Reinvestment Rate = (Net Capital Expenditures + Change in Working Capital) (1 - Debt Ratio)/ Net Income Expected GrowthNet Income = Equity Reinvestment Rate \* ROE

# III. Expected Growth in EBIT And Fundamentals: Stable ROC and Reinvestment Rate

 When looking at growth in operating income, the definitions are Reinvestment Rate = (Net Capital Expenditures + Change in WC)/EBIT(1-t) Return on Investment = ROC = EBIT(1-t)/(BV of Debt + BV of Equity) Reinvestment Rate and Return on Capital gEBIT = (Net Capital Expenditures + Change in WC)/EBIT(1-t) \* ROC = Reinvestment Rate \* ROC **Proposition: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.** 

# No Net Capital Expenditures and Long Term Growth

 You are looking at a valuation, where the terminal value is based upon the assumption that operating income will grow 3% a year forever, but there are no net cap ex or working capital investments being made after the terminal year. When you confront the analyst, he contends that this is still feasible because the company is becoming more efficient with its existing assets and can be expected to increase its return on capital over time. Is this a reasonable explanation? Yes No Explain.

# Estimating Growth in EBIT: Cisco versus Motorola

#### *Cisco's Fundamentals*

 Reinvestment Rate = 106.81% Return on Capital =34.07% Expected Growth in EBIT =(1.0681)(.3407) = 36.39%

#### *Motorola's Fundamentals*

 Reinvestment Rate = 52.99% Return on Capital = 12.18% Expected Growth in EBIT = (.5299)(.1218) = 6.45%

# IV. Operating Income Growth when Return on Capital is Changing

 When the return on capital is changing, there will be a second component to growth, positive if the return on capital is increasing and negative if the return on capital is decreasing. If ROCt is the return on capital in period t and ROCt+1 is the return on capital in period t+1, the expected growth rate in operating income will be:

Expected Growth Rate = 
$$\text{ROC}_{t+1} * \text{Reinvestment rate}$$

+(ROCt+1 – ROCt ) / ROCt

 If the change is over multiple periods, the second component should be spread out over each period.

# Motorola's Growth Rate

 Motorola's current return on capital is 12.18% and its reinvestment rate is 52.99%. We expect Motorola's return on capital to rise to 17.22% over the next 5 years (which is half way towards the industry average)

#### Expected Growth Rate

= 
$$\text{ROC}_{\text{New Investments}}^* \text{Reinvestment Rate}_{\text{current}} + \{[1 + (\text{ROC}_{\text{In 5 years}}^- \text{ROC}_{\text{Current}}) / \text{ROC}_{\text{Current}}]^{1/5} - 1\}$$

= .1722\*.5299 +{ [1+(.1722-.1218)/.1218]1/5-1}

= .174 or 17.40%

One way to think about this is to decompose Motorola's expected growth into Growth from new investments: .1722\*5299= 9.12%

Growth from more efficiently using existing investments: 17.40%-9.12%=8.28%

{Note that I am assuming that the new investments start making 17.22% immediately, while allowing for existing assets to improve returns gradually}

# V. Estimating Growth when Operating Income is Negative or Margins are changing

- When operating income is negative or margins are expected to change over time, we use a three step process to estimate growth:
  - Estimate growth rates in revenues over time
    - Use historical revenue growth to get estimates of revenue growth in the near future
    - Decrease the growth rate as the firm becomes larger
    - Keep track of absolute revenues to make sure that the growth is feasible
  - Estimate expected operating margins each year
    - Set a target margin that the firm will move towards
    - Adjust the current margin towards the target margin
  - Estimate the capital that needs to be invested to generate revenue growth and expected margins
    - Estimate a sales to capital ratio that you will use to generate reinvestment needs each year.

# Commerce One: Revenues and Revenue Growth

| Year Current | Growth Rate | Revenues \$537 | Operating Margin -79.62% | Operating Income -\$428 |
|--------------|-------------|----------------|--------------------------|-------------------------|
| 1            | 50.00%      | \$806          | -48.17%                  | -\$388                  |
| 2            | 100.00%     | \$1,611        | -27.21%                  | -\$438                  |
| 3            | 80.00%      | \$2,900        | -13.23%                  | -\$384                  |
| 4            | 60.00%      | \$4,640        | -3.91%                   | -\$182                  |
| 5            | 40.00%      | \$6,496        | 2.30%                    | \$149                   |
| 6            | 35.00%      | \$8,770        | 6.44%                    | \$565                   |
| 7            | 30.00%      | \$11,401       | 9.20%                    | \$1,049                 |
| 8            | 20.00%      | \$13,681       | 11.04%                   | \$1,510                 |
| 9            | 10.00%      | \$15,049       | 12.27%                   | \$1,846                 |
| 10           | 5.00%       | \$15,802       | 13.08%                   |                         |

# Commerce One: Reinvestment Needs

| Year    | Revenues | Δ Revenues | Sales/Capital | Reinvestment Capital |         | ROC     |
|---------|----------|------------|---------------|----------------------|---------|---------|
| Current | \$537    |            |               |                      | \$2,744 |         |
| 1       | \$806    | \$269      | 2.20          | \$122                | \$2,866 | -14.14% |
| 2       | \$1,611  | \$806      | 2.20          | \$366                | \$3,232 | -15.30% |
| 3       | \$2,900  | \$1,289    | 2.20          | \$586                | \$3,818 | -11.87% |
| 4       | \$4,640  | \$1,740    | 2.20          | \$791                | \$4,609 | -4.76%  |
| 5       | \$6,496  | \$1,856    | 2.20          | \$844                | \$5,452 | 3.24%   |
| 6       | \$8,770  | \$2,274    | 2.20          | \$1,033              | \$6,486 | 10.36%  |
| 7       | \$11,401 | \$2,631    | 2.20          | \$1,196              | \$7,682 | 16.17%  |
| 8       | \$13,681 | \$2,280    | 2.20          | \$1,036              | \$8,718 | 14.17%  |
| 9       | \$15,049 | \$1,368    | 2.20          | \$622                | \$9,340 | 13.76%  |
| 10      | \$15,802 | \$752      | 2.20          | \$342                | \$9,682 | 14.39%  |

Industry average = 15%

![](_page_33_Diagram_0.jpeg)

![]()Discounted Cashflow Valuation

# Getting Closure in Valuation

 A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

$$\text{Value} = t = \infty \frac{\text{CF}_t}{\sum_{t=1}^t (1+r)^t}$$

 Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \frac{t = N}{\sum_{t=1}^t \frac{\text{CF}_t}{(1+r)^t}} + \frac{\text{Terminal Value}}{(1+r)^N}$$

# Getting Closure in Valuation

 A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

$$\text{Value} = t = \infty \frac{\text{CF}_t}{\sum_{t=1}^t (1+r)^t}$$

 Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \frac{t = N}{\sum_{t=1}^t \frac{\text{CF}_t}{(1+r)^t}} + \frac{\text{Terminal Value}}{(1+r)^N}$$

#### Ways of Estimating Terminal Value

![](_page_37_Diagram_1.jpeg)

# Stable Growth and Terminal Value

 When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

## $$g = \text{Expected growth rate}$$

 This "constant" growth rate is called a stable growth rate and cannot be higher than the growth rate of the economy in which the firm operates. While companies can maintain high growth rates for extended periods, they will all approach "stable growth" at some point in time.

# Limits on Stable Growth

- The stable growth rate cannot exceed the growth rate of the economy but it can be set lower.
  - If you assume that the economy is composed of high growth and stable growth firms, the growth rate of the latter will probably be lower than the growth rate of the economy.
  - The stable growth rate can be negative. The terminal value will be lower and you are assuming that your firm will disappear over time.
- If you use nominal cashflows and discount rates, the growth rate should be nominal in the currency in which the valuation is denominated. One simple proxy for the nominal growth rate of the economy is the riskfree rate.

# Stable Growth and Excess Returns

 Strange though this may seem, the terminal value is not as much a function of stable growth as it is a function of what you assume about excess returns in stable growth. In the scenario where you assume that a firm earns a return on capital equal to its cost of capital in stable growth, the terminal value will not change as the growth rate changes. If you assume that your firm will earn positive (negative) excess returns in perpetuity, the terminal value will increase (decrease) as the stable growth rate increases.

# Getting to Stable Growth: High Growth Patterns

- A key assumption in all discounted cash flow models is the period of high growth, and the pattern of growth during that period. In general, we can make one of three assumptions:
  - there is no high growth, in which case the firm is already in stable growth
  - there will be high growth for a period, at the end of which the growth rate will drop to the stable growth rate (2-stage)
  - there will be high growth for a period, at the end of which the growth rate will decline gradually to a stable growth rate(3-stage)
- Each year will have different margins and different growth rates (n stage) Concurrently, you will have to make assumptions about excess returns. In general, the excess returns will be large and positive in the high growth period and decrease as you approach stable growth (the rate of decrease is often titled the fade factor).

# Determinants of Growth Patterns

#### Size of the firm

- Success usually makes a firm larger. As firms become larger, it becomes much more difficult for them to maintain high growth rates

#### Current growth rate

- While past growth is not always a reliable indicator of future growth, there is a correlation between current growth and future growth. Thus, a firm growing at 30% currently probably has higher growth and a longer expected growth period than one growing 10% a year now.

#### Barriers to entry and differential advantages

- Ultimately, high growth comes from high project returns, which, in turn, comes from barriers to entry and differential advantages.
- The question of how long growth will last and how high it will be can therefore be framed as a question about what the barriers to entry are, how long they will stay up and how strong they will remain.

# Stable Growth Characteristics

- In stable growth, firms should have the characteristics of other stable growth firms. In particular,
  - The risk of the firm, as measured by beta and ratings, should reflect that of a stable growth firm.
    - Beta should move towards one
    - The cost of debt should reflect the safety of stable firms (BBB or higher)
  - The debt ratio of the firm might increase to reflect the larger and more stable earnings of these firms.
    - The debt ratio of the firm might moved to the optimal or an industry average
    - If the managers of the firm are deeply averse to debt, this may never happen
  - The reinvestment rate of the firm should reflect the expected growth rate and the firm's return on capital
    - Reinvestment Rate = Expected Growth Rate / Return on Capital

# Stable Growth and Fundamentals

 The growth rate of a firm is driven by its fundamentals - how much it reinvests and how high project returns are. As growth rates approach "stability", the firm should be given the characteristics of a stable growth firm.

#### *Model High Growth Firms usually Stable growth firms usually*

- DDM 1. Pay no or low dividends 1. Pay high dividends
  - 2. Have high risk 2. Have average risk

- 3. Earn high ROC 3. Earn ROC closer to WACC

#### FCFE/ 1. Have high net cap ex 1. Have lower net cap ex

FCFF 2. Have high risk 2. Have average risk

- 3. Earn high ROC 3. Earn ROC closer to WACC
- 4. Have low leverage 4. Have leverage closer to industry average

# The Dividend Discount Model: Estimating Stable Growth Inputs

 Consider the example of ABN Amro. Based upon its current return on equity of 15.79% and its retention ratio of 53.88%, we estimated a growth in earnings per share of 8.51%. Let us assume that ABN Amro will be in stable growth in 5 years. At that point, let us assume that its return on equity will be closer to the average for European banks of 15%, and that it will grow at a nominal rate of 5% (Real Growth + Inflation Rate in NV) The expected payout ratio in stable growth can then be estimated as follows:

Stable Growth Payout Ratio = 1 - g/ ROE = 1 - .05/.15 = 66.67%

g = b (ROE)

b = g/ROE

Payout = 1- b

# The FCFE/FCFF Models: Estimating Stable Growth Inputs

 The soundest way of estimating reinvestment rates in stable growth is to relate them to expected growth and returns on capital:

Reinvestment Rate = Growth in Operating Income/ROC

 For instance, Cisco is expected to be in stable growth 13 years from now, growing at 5% a year and earning a return on capital of 16.52% (which is the industry average). The reinvestment rate in year 13 can be estimated as follows:

Reinvestment Rate = 5%/16.52% = 30.27%

 If you are consistent about estimating reinvestment rates, you will find that it is not the stable growth rate that drives your value but your excess returns. If your return on capital is equal to your cost of capital, your terminal value will be unaffected by your stable growth assumption.

# Closing Thoughts on Terminal Value

- The terminal value will always be a large proportion of the total value. That is a reflection of the reality that the bulk of your returns from holding a stock for a finite period comes from price appreciation.
  - As growth increases, the proportion of value from terminal value will go up.
- The present value of the terminal value can be greater than 100% of the current value of the stock. The key assumption in the terminal value calculation is not the growth rate but the excess return assumption. The terminal value, if you follow consistency requirements, is not unbounded.