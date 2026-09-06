---
title: "MARKET EFFICIENCY - DEFINITION AND TESTS"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/invemgmt/testmkt.html
---

MARKET EFFICIENCY - DEFINITION AND TESTS

 

**TESTING MARKET EFFICIENCY**

* Tests of market efficiency look at the whether specific investment strategies earn excess returns. Some tests also account for transactions costs and execution feasibility. In every case, **a test of market efficiency is a joint test of market efficiency and the efficacy of the model used for expected returns**.* When there is evidence of excess returns in a test of market efficiency, it can indicate **that markets are inefficient or that the model used to compute expected returns is wrong or both**.* There are a number of different ways of testing for market efficiency, and the approach used will depend in great part on the investment scheme being tested.

***A. Event Study*****An event study is designed to examine market reactions to, and excess returns around specific information events**. The information events can be market-wide, such as macro-economic announcements, or firm-specifc, such as earnings or dividend announcements.

**Step 1: Identify the event**

(1) The event to be studied is clearly identified, and the date on which the event was announced pinpointed.

> > > > Announcement Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Step 2: Collecting Returns**

(2) Once the event dates are known, **returns are collected around these dates** for each of the firms in the sample. In doing so, two decisions have to be made.

* First, the analyst has to **decide whether to collect weekly, daily or shorter-interval returns** around the event. This will, in part, be decided by

- how precisely the event date is known

- by how quickly information is reflected in

* Second, the analyst has to determine how many periods of returns before and after the announcement date will be considered as part of the 'event window'.

> > R-jn ............................. Rj0 ...............................R+jn

\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_

Return window: -n to +n

where,

Rjt = Returns on firm j for day t (t = -n, ...,0, .... +n)

**Step 3: Adjust for market performance and risk**

(3) The returns, by period, around the announcement date, are adjusted for market performance and risk to arrive at excess returns for each firm in the sample. For instance, if the capital asset pricing model is used to control for risk -

Excess Return on day t = Return on day t - Beta \* Return on market on day t

> > ER-jn ............................ ERj0 ............................ER+jn

\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_

Return window: -n to +n

where,

ERjt = Excess Returns on firm j for day t (t = -n, ...,0, .... +n)

**Step 4: Calculate the crosssectional average**

(4) The excess returns, by day, are averaged across all firms in the sample and a standard error is computed.

Average excess return on day t= ![](../invphillectures/Image71.gif)

where,

N = Number of events in the event study

**Step 5: Estimate the statistical significance**

(5) The question of whether the excess returns around the announcement are different from zero is answered by estimating the t statistic for each n, by dividing the average excess return by the standard error -

T statistic for excess return on day t = Average Excess Return / Standard Error

If the t statistics are statistically significant, the event affects returns; the sign of the excess return determines whether the effect is positive or negative.

*Illustration 1: Example of an event study - Effects of Option Listing on Stock prices*

* Academics and practitioners have long argued about the **consequences of option listing for stock price volatility**. On the one hand, there are those who argue that options attract speculators and hence increase stock price volatility. On the other hand, there are others who argue that options increase the available choices for investors and increase the flow of information to financial markets, and thus lead to lower stock price volatility and higher stock prices.* One way to test these alternative hypotheses is to do an event study, examining **the effects of listing options on the underlying stocks' prices**. Conrad(1989) did such a study, following these steps -

*Step 1:* The **date on which the announcement that options would be listed** on the Chicago Board of Options on a particular stock was collected.

*Step 2:* The **prices of the underlying stock(j) were collected** for each of the ten days prior to the option listing announcement date, the day of the announcement, and each of the ten days after.

*Step 3:* The **returns on the stock (Rjt) were computed** for each of these trading days.

*Step 4:* The **beta for the stock (bj) was estimated** using the returns from a time period outside the event window (using 100 trading days from before the event and 100 trading days after the event).

*Step 5:* The **returns on the market index (Rmt) were computed** for each of the 21 trading days.

*Step 6:* The **excess returns were computed** for each of the 21 trading days -

ERjt = Rjt - bj Rmt .......... t = -10,-9,-8,....,+8,+9,+10

The excess returns are cumulated for each trading day.

*Step 7:* The **average and standard error of excess returns** across all stocks with option listings were computed for each of the 21 trading days. The t statistics are computed using the averages and standard errors for each trading day.

**Option Listing and Stock Returns: The Results**

|  |  |  |  |
| --- | --- | --- | --- |
| *Trading Day* | *Average Excess* | *Cumulative*  *Excess* *Returns* | *T Statistic* |
| -10 | 0.17% | 0.17% | 1.30 |
| -9 | 0.48% | 0.65% | 1.66 |
| -8 | -0.24% | 0.41% | 1.43 |
| -7 | 0.28% | 0.69% | 1.62 |
| -6 | 0.04% | 0.73% | 1.62 |
| -5 | -0.46% | 0.27% | 1.24 |
| -4 | -0.26% | 0.01% | 1.02 |
| -3 | -0.11% | -0.10% | 0.93 |
| -2 | 0.26% | 0.16% | 1.09 |
| -1 | 0.29% | 0.45% | 1.28 |
| 0 | 0.01% | 0.46% | 1.27 |
| 1 | 0.17% | 0.63% | 1.37 |
| 2 | 0.14% | 0.77% | 1.44 |
| 3 | 0.04% | 0.81% | 1.44 |
| 4 | 0.18% | 0.99% | 1.54 |
| 5 | 0.56% | 1.55% | 1.88 |
| 6 | 0.22% | 1.77% | 1.99 |
| 7 | 0.05% | 1.82% | 2.00 |
| 8 | -0.13% | 1.69% | 1.89 |
| 9 | 0.09% | 1.78% | 1.92 |
| 10 | 0.02% | 1.80% | 1.91 |

* Based upon these excess returns, there is no evidence of an announcement effect on the announcement day alone, but there is mild evidence of a positive effect over the entire announcement period.

***B. Portfolio Study***

* In some investment strategies, **firms with specific characteristics are viewed as more likely to be undervalued**, and therefore have excess returns, than firms without these characteristics.* In these cases, the **strategies can be tested by creating portfolios of firms possessing these characteristics at the beginning of a time period**, and examining returns over the time period. To ensure that these results are not colored by the idiosyncracies of any one time period, this is repeated for a number of periods.

**Steps in doing a portfolio study**

(1) The **variable on which firms will be classified is defined**, using the investment strategy as a guide. This variable has to be observable, though it does not have to be numerical.

(2) The **data on the variable is collected** for every firm in the defined universe at the start of the testing period, and firms are classified into portfolios based upon the magnitude of the variable.

(3) The **returns are collected for each firm** in each portfolio for the testing period, and the returns for each portfolio are computed, generally assuming that the stocks are equally weighted.

(4) The **beta of each portfolio is estimated**, either by taking the average of the betas of the individual stocks in the portfolio or by regressing the portfolio's returns against market returns over a prior period.

(5) The **excess returns** earned by each portfolio are computed, with the standard error of these returns.

(6) There are a **number of statistical tests** available to check whether the average excess returns are, in fact, different across the portfolios.

(7) As a final test, the **extreme portfolios can be matched** against each other to see whether there are statistically significant differences across these portfolios.

*Illustration 8.2: Example of a portfolio study - Price Earnings Ratios*

* Practitioners have claimed that **low price-earnings ratio stocks are generally bargains** and do much better than the market or stocks with high price earnings ratios.

*Step 1:* Using data on **PE ratios from the end of 1987**, firms on the New York Stock Exchange were classified into five groups, the first group consisting of stocks with the lowest PE ratios and the fifth group consisting of stocks with the highest PE ratios. Firms with negative price-earnings ratios were ignored.

Step 2: The **returns on each portfolio were computed** using data from **1988 to 1992**. Stocks which went bankrupt or were delisted were assigned a return of -100%.

Step 3: The **betas for each stock in each portfolio** were computed using monthly returns from 1983 to 1987, and the average beta for each portfolio was estimated. The portfolios were assumed to be equally weighted.

Step 4: The **returns on the market index** was computed from 1988 to 1992.

Step 5: The **excess returns on each portfolio** were computed using data from 1988 to 1992. The following table summarizes the excess returns each year from 1988 to 1992 for each portfolio.

*Table 8.2: Excess Returns from 1988 to 1992 for PE Ratio Portfolios*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| P/E Class | 1988 | 1989 | 1990 | 1991 | 1992 | 1988-1992 |
| Lowest | 3.84% | -0.83% | 2.10% | 6.68% | 0.64% | 2.61% |
| 2 | 1.75% | 2.26% | 0.19% | 1.09% | 0.93% | 1.46% |
| 3 | 0.20% | -3.16% | -0.20% | 0.17% | 0.12% | -0.59% |
| 4 | -1.25% | -0.94% | -0.65% | -2.01% | -0.48% | -1.15% |
| Highest | -1.74% | -0.63% | -1.44% | -4.06% | -1.25% | -1.95% |

**The Cardinal Sins in testing Market Efficiency**

*1. Using 'anecdotal evidence' to support/reject an investment strategy:* Anecdotal evidence is a double edged sword. It can be used to support or reject the same hypothesis. Since stock prices are noisy and all investment schemes (no matter how absurd) will succeed sometimes and fail at other times, there will always be cases where the scheme works or does not work.

*2. Testing an investment strategy on the same data and time period from which it was extracted:* This is the tool of choice for the unscrupulous investment advisor. An investment scheme is extracted from hundreds through an examination of the data for a particular time period. This investment scheme is then tested on the same time period, with predictable results. (The scheme does miraculously well and makes immense returns.)

*An investment scheme should always be tested out on a time period different from the one it is extracted from or on a universe different from the one used to derive the scheme.*

---

*3. Choosing a biased universe*, The universe is the sample on which the test is run. Since there are thousands of stocks that could be considered part of this universe, researchers often choose to use a smaller universe. When this choice is random, this does limited damage to the results of the study. If the choice is biased, it can provide results which are not true in the larger universe.

*4. Failure to control for market performance:* A failure to control for overall market performance can lead one to conclude that your investment scheme works just because it makes good returns (Most schemes will make good returns if the overall market does well; the question is did they make better returns than expected) or does not work just because it makes bad returns (Most schemes will do badly if the overall market performs poorly). It is crucial therefore that investment schemes control for market performance during the period of the test.

*5. Failure to control for risk:* A failure to control for risk leads to a bias towards accepting high-risk investment schemes and rejecting low-risk investment schemes, since the former should make higher returns than the market and the latter lower, without implying any excess returns.

**Some lesser sins that can be a problem**

*1. Survival Bias:* Most researchers start with a existing universe of publicly traded companies and working back through time to test investment strategies. This can create a subtle bias since it automatically eliminates firms that failed during the period, with obvious negative consequences for returns. If the investment scheme is particularly susceptible to picking firms that have high bankruptcy risk, this may lead to an 'overstatement' of returns on the scheme.

For example, assume that the investment scheme recommends investing in stocks which have very negative earnings, using the argument that these stocks are most likely to benefit from a turnaround. Some of the firms in this portfolio will go bankrupt, and a failure to consider these firms will overstate the returns from this strategy.

*An Example of Survivor Bias*

![](../invphillectures/Image72.gif)

*2. Not allowing for transactions Costs:* Some investment schemes are more expensive than others because of transactions costs - execution fees, bid-ask spreads and price impact. A complete test will take these into account before it passes judgment on the strategy. This is easier said than done, because different investors have different transactions costs, and it is unclear which investor's trading cost schedule should be used in the test. Most researchers who ignore transactions costs argue that individual investors can decide for themselves, given their transactions costs, whether the excess returns justify the investment strategy.

![](../invphillectures/Image73.gif)

*3. Not allowing for difficulties in execution:* Some strategies look good on paper but are difficult to execute in practice, either because of impediments to trading or because trading creates a price impact. Thus a strategy of investing in very small companies may seem to create excess returns on paper, but these excess returns may not exist in practice because the price impact is significant.

*Many a slip between the cup and the lip ....*

![](../invphillectures/Image74.gif)

![](../invphillectures/Image75.gif)
