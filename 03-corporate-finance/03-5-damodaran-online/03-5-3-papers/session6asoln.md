---
title: "Session6Asoln"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session6Asoln.pdf
---

#### **Session 6A: Post Class Test Solutions**

1.

- a. Probability of up day, over the 900-day sample period = 480/900 = 53.33% Probability of down day, over the 900-day sample period = 420/900 = 46.67%
- b. With 900 trading days, the range, if price changes were random (50/50 up or down), the standard error would be  $= (.50) / \sqrt{900} = 0.833\%$   
  The range on up days would be  $50\% \pm 0.933\% = 48.33\%$  to 51.67\%  
  That would put 53.33\% above the range, rejecting the randomness hypothesis.
- c. During the 900 trading days, there were 440 reversals (Up followed by down or down followed by up), yielding a probability of 48.89%.
- d. During the 900 trading days, there were 460 continuations (Up followed by up or down followed by down), yielding a probability of 51.11%.

2.

- a. If past performance has no carry over effect, every number in this table should be 25%. In other words, where a manager fell in the first period (in terms of quartiles) should have no effect on where he or she falls in the next period.
- b. With a sample size of 400, you would expect the estimates to have a range which can be estimated as follows:

Standard error of probability estimate for transition = 
$$\frac{0.25*0.75}{\sqrt{400}} = 0.009375$$

With this standard error, the range on the probability, assuming no performance continuity would be 23.125% to 26.875%, with 95% confidence.

There are a few numbers in this table that fall above or below this bound, but barely. with quartile 3 managers showing more continuity than would be expected (with a 29% chance of staying in quartile 3) and quartile 4 managers showing a greater chance of either staying in the same quartile or jumping to the top quartile than expected (28% chance of both).

- c. The removal of 40 managers who did not make it into the second time period creates a survivor bias. You would need to get the quartiles that these managers were in, and if they were disproportionately in one (say quartile 4), that could alter your conclusions about no predictive power in rankings, at least for that group.

## 3. PROBIT

- a. Step 1: Pick a sample of companies that were listed at the start of your assessment time period. Step 2: Identify which of these companies had a CEO that was fired during the time period. Step 3: Develop hypotheses on what types of firms you are most likely to see a CEO firing, and find variables to back up these hypotheses Step 4: Run a PROBIT, with the CEO firing as your independent variable (taking on a value of one if there was a firing and zero, if not)
- b. Plug in your company's values for the independent variables into the CEO firing PROBIT: CEOFIRED = 0.05 - 0.40 (-.20) + 0.20 (.60) – 0.30 (.10) = 0.22 or 22%
- c. Companies that have had worse stock performance in the past, are more held by institutions and lower profit margins are more likely to see CEO firings. That said, the

R-squared is only 15%, suggesting that there are many other factors that explain CEO firings.

#### 4. Decision Tree

![](_page_1_Figure_2.jpeg)

### 5. Expected value of company:

| Scenario                 | Value of company | Probability | Value * Probability |
|--------------------------|------------------|-------------|---------------------|
| Monopoly + Pricing Power | \$1,500.00       | 20%         | \$300.00            |
| Monopoly Status Quo      | \$900.00         | 50%         | \$450.00            |
| Competition              | \$600.00         | 30%         | \$180.00            |
| Expected Value           |                  |             | \$930.00            |

# Expected margin in a point estimate valuation

| Scenario                 | Expected Operating Margin | Probability | Growth * Probability |
|--------------------------|---------------------------|-------------|----------------------|
| Monopoly + Pricing Power | 15%                       | 20%         | 3.00%                |
| Monopoly Status Quo      | 9%                        | 50%         | 4.50%                |
| Competition              | 6%                        | 30%         | 1.80%                |
| Expected Growth Rate     |                           |             | 9.30%                |

The value from a point estimate analysis will be close but it will not usually be identical to the expected values from across scenarios, even if you are consistent about using expected values across scenarios, because the link between value and the variables is not linear. (As margin increases, the value may not increase proportionately).

If your regulatory risk is continuous, i.e., rather than fall into three discrete choices your margins can vary anywhere from 6% to 15%, depending upon how strict the regulatory overlay is, a

scenario analysis, by artificially breaking the possibilities into three scenarios may be misleading.