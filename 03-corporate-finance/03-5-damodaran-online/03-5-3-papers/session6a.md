---
title: "Session6A"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/Slides/Session6A.pdf
---

### SESSION 6A: PROBABILITIES & DECISION TREES IN FINANCE

Session 6

There is a chance!

# 1. Stock Market as a Random Walk

- □ One of the simplest, albeit weakest, tests of randomness is to test to see whether there is a 50:50 chance that markets will go up (or down). Thus, if you have a hundred days of market changes, you would expect to see 50 up and 50 down days.
- □ To test this proposition, you can look at price changes for  $n$  trading days, and compute the number of days that the market was up (and down). However, even if markets are random, the actual number that you find will deviate from 50:50. The standard error is a function of the number of trading days and can be computed as follows:
  - ■ Std Error in probability =  $\sqrt{\frac{0.5 * 0.5}{n}}$  where  $n$  = Number of days in your sample.
  - ■ This can be generalized more generally to any two-outcome experiment as
     
    $$\text{Std Error in probability} = \sqrt{\frac{p(1-p)}{n}}$$
     where  $p$  = Probability of one of the outcomes
  - ■ Thus, if you observe a hundred trading days, the range, with 95% probability, on up (or down) days, even if markets have a 50:50 chance of going up and down, would be 45-55. (Std Error = 2.5%)

### Probability that the market will go up (or down)…

- □ There were 1257 trading days between January 1, 2016 and December 31, 2020. Over that period, the S&P 500 was
  - □ Up on 700 trading days
  - □ Down on 557 trading days
- □ Based upon that data, the probability that the market was up during the period was 55.69% and the probability that the market was down was 44.31%.
- □ *Can you use this to accept or reject the hypothesis that there was a 50% chance of up/down days., at least during this period?*
  - □ *Std Error in probability, if random =  $\sqrt{\frac{0.5 * 0.5}{1257}} = 0.0141$  or 1.41%*
  - □ *Range with 95% confidence, on up probability =  $0.5569 \pm 2(0.0141)$  : Range: 52.87% to 58.51% probability of up (or down) days, during this period*
  - □ *At least during this period, you can reject the 50:50 up/down hypothesis.*
- □ *Can you extrapolate from this that there will be more up than down days in the market in the future?*

# Conditional Probabilities…

¨ Using the same data )returns on the S&P 500 on a daily basis from January 1, 2016, to December 31, 2020), and breaking down into up and down days:

|               |             | <b>Market tomorrow</b> |             |
|---------------|-------------|------------------------|-------------|
|               |             | <i>Up</i>              | <i>Down</i> |
| <b>Market</b> | <i>Up</i>   | <b>367</b>             | <b>333</b>  |
| <b>today</b>  | <i>Down</i> | <b>332</b>             | <b>225</b>  |

¨ Converting these numbers into probabilities, you get:

|                     |             | <b>Market tomorrow</b> |             |
|---------------------|-------------|------------------------|-------------|
|                     |             | <i>Up</i>              | <i>Down</i> |
| <b>Market today</b> | <i>Up</i>   | 52.43%                 | 47.57%      |
|                     | <i>Down</i> | 59.61%                 | 40.39%      |

# Cumulative Probabilities…

¨ If the probability that the market will go up (down) on a given day was 55.69% (44.31%), all through the time period, you can estimate the probabilities of the market going up or down two, three or even ten days in a row. ¨ Thus, to estimate the probability that the market was up three or five days in a row: ¤ Probability of three up days in a row = (0.5569)3 = .1727 ¤ Probability of five up days in a row = (0.5569)5 = .0536 ¨ Similarly, to estimate the probability that the market was down three or five days in a row: ¤ Probability of three up days in a row = (0.4431)3 = .0870 ¤ Probability of five up days in a row =(0.4431)5 = .0171

# 2. Transition Probabilities

¨ In investing and finance, it is common to put portfolio managers and companies into groupings, reflecting their standing on a metric (returns, debt ratios, dividends) or rankings in performance. ¨ Those rankings are not only used to judge investors and companies, but are also used as predictors for the future. While every mutual or hedge fund touts the warning that past performance is not a predictor of the future, it is undeniable that funds that have performed/ranked well in the past market themselves on that basis, and that investors redirect their money to these funds. ¨ The test of whether chasing past performance is a good strategy can be converted into a test of whether there is stickiness in rankings. Put simply, if you ranked funds into groups based upon success, do these rankings persist?

# Money Manager Performance

**Report 5: Five-Year Transition Matrix – Performance over Two Non-Overlapping Five-Year Periods (Based on Quartile)**

| ALL DOMESTIC FUNDS | FUND COUNT AT START (SEPTEMBER 2014) | FIVE-YEAR PERCENTAGES AT END |                  |                  |                  |                        |                   |
|--------------------|--------------------------------------|------------------------------|------------------|------------------|------------------|------------------------|-------------------|
|                    |                                      | 1ST QUARTILE (%)             | 2ND QUARTILE (%) | 3TH QUARTILE (%) | 4TH QUARTILE (%) | MERGED/ LIQUIDATED (%) | STYLE CHANGED (%) |
| 1st Quartile       | 485                                  | 31.75                        | 21.44            | 18.14            | 20.21            | 8.04                   | 0.41              |
| 2nd Quartile       | 484                                  | 23.76                        | 21.69            | 21.07            | 18.18            | 14.88                  | 0.41              |
| 3rd Quartile       | 485                                  | 14.02                        | 22.47            | 23.30            | 17.53            | 21.86                  | 0.82              |
| 4th Quartile       | 484                                  | 10.54                        | 14.46            | 17.56            | 24.17            | 30.99                  | 2.27              |

The performance persistence varies across

- - Markets (Geographical, asset class)
- - Time (Some periods have more persistence than others)
- - Style classes (value versus growth, small vs large cap)

It is also difficult for investors to convert this statistical persistence into returns.

Each of these probability estimates has a standard error that will decrease as the sample size increases.

# 3. Probability of Corporate Default

![](_page_7_Figure_1.jpeg)

# Conditional Probabilities: Bond Ratings and Default Rates

**Global Corporate Average Cumulative Default Rates By Rating (1981-2019)**

![](_page_8_Figure_16.jpeg)

Sources: S&P Global Ratings Research and S&P Global Market Intelligence's CreditPro®.

Copyright © 2020 by Standard & Poor's Financial Services LLC. All rights reserved.

### A Multiple Discriminant Model of Default: The Altman Z Score

**Altman Z Score Formula**

$$Z = \left( 1.2 \times \left( \frac{\text{Working Capital}}{\text{Total Assets}} \right) + 1.4 \times \left( \frac{\text{Retained Earnings}}{\text{Total Assets}} \right) + 3.3 \times \left( \frac{\text{Task Payment}}{\text{Total Assets}} \right) \right) + 1.6 \times \left( \frac{\text{The equity's Market Value}}{\text{Total Sales}} \right)$$

![](_page_9_Figure_2.jpeg)

Altman analyzed 66 manufacturing companies, of which 33 became bankrupt within the years 1946- 1965 and the other half were existing companies in 1966.

![](_page_9_Figure_4.jpeg)

# A Probit Model: Hostile Acquisitions

¨ While there are no easy pathways to making money, it seems clear that investors in companies that are targeted in acquisitions (especially hostile ones) earn high returns, but only if they invest before the event. ¨ There are probit models for predicting companies that will be targeted, and they involve: ¤ You start with all firms that publicly traded at the start of a period ¤ The dependent variable becomes the stand-in for whether a firm is targeted in a hostile acquisition ¤ The independent variables reflect what you believe are key drivers of hostile acquisitions, including poor stock price performance, lagging accounting returns and managers with little or no shareholdings. ¤ You build a probit model that will yield as output an equation that resembles a regression, but will yield a probability of a hostile acquisition.

## Hostility Prediction Models, 1975–1996

Probit models predicting whether successful and unsuccessful takeover bids for exchange-listed target firms from 1975 to 1996 are hostile, using four measures of hostility. The dependent variables are dummy variables that equal one when a hostile bid is made for a target firm, and zero otherwise. Host(WSJ) is based on descriptions in the *Wall Street Journal Index* or *Dow Jones News Retrieval*, Host(SDC) is based on whether the target firm resisted an unsolicited offer as determined by the Securities Data Company (SDC), Host(Uns) is based on whether the initial or winning bid is unsolicited, and Host(Pre) is based on whether the target firm is in play (someone has filed a 13D form with the SEC showing an accumulation of shares within the past 12 months) or the subject of a takeover rumor reported in *DJNR*. Several variables measuring the performance of the target firm before the first bid are used in the model. ROE is earnings divided by average stockholder's (book) equity and Sales Growth is the growth in sales over the fiscal year before the first bid. Liquidity is the ratio of net liquid assets to total assets, D/E is the long-term debt to book equity, M/B is the ratio of market to book value of stockholder's equity, P/E is the ratio of stock price to the earnings for the last fiscal year, and Size is the logarithm of the market value of common stock, all measured at the end of the fiscal year before the first bid. Dummy variables are equal to one when the first bid occurs during 1980 to 1984, or 1985 to 1989, or 1990 to 1996, and zero otherwise, allowing for secular variation. The last two columns contain the coefficients and *t*-statistics for a regression of the hostility factor (principal component), Host(Factor), created from the three hostility variables with complete data (Host(WSJ), Host(Uns), and Host(Pre)) on the explanatory variables from the probit model. The marginal effect column transforms the probit coefficient into the marginal effect of the variable on the estimated probability, evaluated at the sample means of the explanatory variables.

| Variable       | Host(WSJ) |                     |                 | Host(SDC) |                     |                 | Host(Uns) |                     |                 | Host(Pre) |                     |                 | Host(Factor) |                     |
|----------------|-----------|---------------------|-----------------|-----------|---------------------|-----------------|-----------|---------------------|-----------------|-----------|---------------------|-----------------|--------------|---------------------|
|                | Coef.     | <i>t</i> -statistic | Marginal Effect | Coef.     | <i>t</i> -statistic | Marginal Effect | Coef.     | <i>t</i> -statistic | Marginal Effect | Coef.     | <i>t</i> -statistic | Marginal Effect | Coef.        | <i>t</i> -statistic |
| Constant       | -4.692    | -7.66               | -0.638          | -3.145    | -4.57               | -0.882          | -0.153    | -0.43               | -0.056          | -1.660    | -4.57               | -0.603          | -0.092       | -1.36               |
| ROE            | -2.413    | -2.79               | -0.328          | -0.104    | -0.12               | -0.029          | -1.192    | -2.11               | -0.439          | -0.483    | -0.90               | -0.175          | -0.321       | -3.65               |
| Sales Growth   | -0.715    | -1.83               | -0.097          | -0.187    | -0.54               | -0.052          | -0.433    | -1.89               | -0.159          | -0.268    | -1.19               | -0.097          | -0.121       | -3.29               |
| Liquidity      | 0.386     | 1.02                | 0.052           | 0.236     | 0.66                | 0.066           | -0.027    | -0.12               | -0.010          | -0.262    | -1.13               | -0.095          | 0.003        | 0.07                |
| D/E            | -0.243    | -1.55               | -0.033          | -0.082    | -0.72               | -0.023          | 0.018     | 0.32                | 0.007           | 0.117     | 2.24                | 0.042           | 0.007        | 0.93                |
| M/B            | -0.068    | -0.82               | -0.009          | -0.226    | -2.83               | -0.063          | -0.151    | -3.01               | -0.055          | -0.055    | -1.48               | -0.020          | -0.018       | -2.59               |
| P/E            | -0.020    | -2.21               | -0.003          | -0.006    | -0.89               | -0.002          | -0.003    | -0.66               | -0.001          | -0.003    | -0.65               | -0.001          | -0.002       | -2.64               |
| Size           | 0.359     | 7.49                | 0.049           | 0.256     | 5.68                | 0.072           | 0.032     | 1.11                | 0.012           | 0.124     | 4.29                | 0.045           | 0.038        | 6.73                |
| 1980–1984      | -0.511    | -2.85               | -0.069          | -0.508    | -1.39               | -0.142          | -0.114    | -1.05               | -0.042          | 0.363     | 3.30                | 0.132           | -0.018       | -0.94               |
| 1985–1989      | -0.188    | -1.11               | -0.026          | -0.016    | -0.04               | -0.004          | 0.402     | 3.59                | 0.148           | 0.687     | 6.07                | 0.250           | 0.088        | 4.14                |
| 1990–1996      | -0.675    | -2.88               | -0.092          | -0.457    | -1.24               | -0.128          | -0.356    | -2.43               | -0.131          | -0.134    | -0.93               | -0.049          | -0.096       | -3.37               |
| R <sup>2</sup> |           | 0.108               |                 |           | 0.119               |                 |           | 0.078               |                 |           | 0.099               |                 |              | 0.133               |
| Log-likelihood |           | -275.6              |                 |           | -304.0              |                 |           | -704.5              |                 |           | -697.0              |                 |              |                     |
| Sample size, N |           | 1,096               |                 |           | 593                 |                 |           | 1,096               |                 |           | 1,096               |                 |              | 1,096               |

Source: *Hostility in Takeovers: In the Eyes of the Beholder*, G.W. Schwert, JF 2000

# 3. Decision Tree: An Example

¨ Consider a pharmaceutical drug for treating Type 1 diabetes that has gone through preclinical testing and is about to enter phase 1 of the FDA approval process. ¤ Phase 1 is expected to cost \$ 50 million and will involve 100 volunteers to determine safety and dosage; it is expected to last 1 year. There is a 70% chance that the drug will successfully complete the first phase. ¤ In phase 2, the drug will be tested on 250 volunteers for effectiveness in treating diabetes over a two-year period. This phase will cost \$ 100 million and the drug will have to show a statistically significant impact on the disease to move on to the next phase. There is only a 30% chance that the drug will prove successful in treating type 1 diabetes but there is a 10% chance that it will be successful in treating both type 1 and type 2 diabetes and a 10% chance that it will succeed only in treating type 2 diabetes. ¤ In phase 3, the testing will expand to 4,000 volunteers to determine the long-term consequences of taking the drug. If the drug is tested on only type 1 or type 2 diabetes patients, this phase will last 4 years and cost \$ 250 million; there is an 80% chance of success. If it is tested on both types, the phase will last 4 years and cost \$ 300 million; there is a 75% chance of success. ¨ If the drug passes through all 3 phases, the costs and annual cash flows are below:

| Disease treatment     | Cost of Development | Annual Cash Flow            |
|-----------------------|---------------------|-----------------------------|
| Type 1 diabetes only  | \$ 500 million      | \$ 300 million for 15 years |
| Type 2 diabetes only  | \$ 500 million      | \$ 125 million for 15 years |
| Type 1 and 2 diabetes | \$ 600 million      | \$ 400 million for 15 years |

# The Tree...

![](_page_13_Diagram_4.jpeg)

# The Fold Back

![](_page_14_Diagram_1.jpeg)

### 4. Scenario Analysis: easyJet and Brexit in 2019

| Restructuring cost (up front) | No Deal Brexit £500 million | Bad Deal Brexit £300 million | Soft or No Brexit \$0 |
|-------------------------------|-----------------------------|------------------------------|-----------------------|
| Revenue growth                | 3.00%                       | 5.00%                        | 5.00%                 |
| Operating Margin              | 6.00%                       | 7.00%                        | 8.00%                 |
| Sales to Capital Ratio        | 1.73                        | 1.73                         | 1.73                  |

**16**

|                 | No Deal Brexit | Delayed & Messy Brexit | Soft or No Brexit |  |
|-----------------|----------------|------------------------|-------------------|--|
| Probability     | 25%            | 50%                    | 25%               |  |
| Value Per Share | £12.02         | £15.70                 | £19.38            |  |

Expected Value per share = .25 (£12.02) + .50 (£15.70) + .25 (£19.38) = £15.70