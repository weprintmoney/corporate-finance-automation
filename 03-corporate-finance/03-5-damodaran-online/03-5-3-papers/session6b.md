---
title: "Session6B"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/Slides/Session6B.pdf
---

# SESSION 6B: SIMULATIONS

Session 6 Data, Distributions and Probabilities!

# Point Estimates and Distributions…

¨ In both corporate finance and valuation, much of what we do is built around point estimates, made with the data that we have at the time of estimation. ¨ The reality is that what are estimating are distributions, with an expected value (that should be the point estimate) but also a substantial possibility of error. ¨ Our defense for using point estimates was that we lacked the data to estimate probability distributions and/or that doing valuations with distributions would require machine power that we did not have access to (at a reasonable price).

# A Big Picture View of Simulations

¨ In a simulation, you estimate probability distributions for each variable that goes into an analysis. ¨ In each simulation, you draw an outcome from each of the distributions and estimate the end result with those outcomes. Since these outcomes can come from the low end or high end of the distributions, they will be different. ¨ You run as many simulations as you can and come up with a distribution of the outcomes, which you then use for decision making.

#### Start with a sound model, connecting inputs to your output variable

¨ In running a simulation, you are trying to estimate an output variable, using input variables that have probability distributions estimated for them. ¨ If the model you are using to connect the output variable to your input variables is flawed in terms of construct and connections, your output variable will reflect those flaws. ¨ In building this model, you are aiming for ¤ Simple, over complex, since you have fewer variables to keep track off. ¤ Transparent, rather than opaque, on the connections that underlie models. Models that have black boxes in them are dangerous.

# Which variables? Less is more!

¨ Almost very variable in an analysis has uncertainty attached to it, and the question you face in a simulation is whether you want to build a distribution for each. ¨ As a general rule, focus on ¤ The variables that have the biggest effect on your decision or output variable. ¤ The variables where you feel most uncertain and exposed.

# Classifying uncertainties

- 1. Discrete or Continuous? Risks that either occur or do not are discrete risks; you are not exposed to them much of the time, but when they do happen, they can be catastrophic. Risks that you are exposed to all of the time, albeit often in small does, are continuous risks.
- 2. Symmetric or Asymmetric? If positive and negative outcomes are roughly equivalent in magnitude and probability, you have symmetric risks. If large positive (negative) outcomes are more likely, you have positively (negatively) skewed risks.
- 3. Extreme value likelihood, low or high? If outcomes that are very different from your expected value happen very infrequently, you have thin tailed distributions. If they occur often, you have fat tailed distributions.

# Pick distributions

![](_page_6_Diagram_1.jpeg)

# Simulation in Valuation

![](_page_7_Diagram_2.jpeg)

#### **Value Simulation: The Steps**

# Step 1: Base Case Valuation

Terminal Value= 38,110/(.08-.015) = \$586,304

Cost of capital = 10.59% (.892) + 1.% (.108) = 9.63%

**ERP** 6.66%

**Beta**  1.31 + **<sup>X</sup>**

**Cost of Debt** Bond rating: AA- (1.9%+0.7%)(1-.35) = 1.69%

**Cost of Equity** 10.59%

**Stable Growth** g = 1.5%; Cost of capital = 8% ROC= 12%; Reinvestment Rate=1.5%/12% = 16.67%

**Weights** E = 89.2% D = 10.8% In May 2016, Apple was trading at \$93 a share.

Cost of capital decreases to 8% from years 6-10

#### *Apple: Base Case Valuation (May 2016)*

Revenue growth of **1.5%** a year in perpetuity.

Pre-tax operating margin decreases to **25%** over time.

Sales to capital ratio of 1.60

My Apple Narrative: A mature company that derives the bulk of its value from a franchise (iPhone) in a market where growth is slowing and competition is increaing.

|                         | 1          | 2          | 3          | 4          | 5          | 6          | 7          | 8          | 9          | 10             |
|-------------------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|----------------|
| Revenue growth rate     | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%      | 1.50%          |
| Revenues                | \$ 230,948 | \$ 234,412 | \$ 237,928 | \$ 241,497 | \$ 245,120 | \$ 248,797 | \$ 252,529 | \$ 256,316 | \$ 260,161 | \$ 264,064     |
| EBIT (Operating) margin | 32.45%     | 31.63%     | 30.80%     | 29.97%     | 29.14%     | 28.31%     | 27.48%     | 26.66%     | 25.83%     | 25.00%         |
| EBIT (Operating income) | \$ 74,953  | \$ 74,136  | \$ 73,277  | \$ 72,376  | \$ 71,432  | \$ 70,442  | \$ 69,407  | \$ 68,325  | \$ 67,195  | \$ 66,016      |
| Tax rate                | 26.49%     | 26.49%     | 26.49%     | 26.49%     | 26.49%     | 28.19%     | 29.90%     | 31.60%     | 33.30%     | 35.00%         |
| EBIT(1-t)               | \$ 55,095  | \$ 54,495  | \$ 53,863  | \$ 53,201  | \$ 52,507  | \$ 50,581  | \$ 48,657  | \$ 46,736  | \$ 44,820  | \$ 42,910      |
| - Reinvestment          | \$         | 2,133 \$   | 2,165 \$   | 2,198 \$   | 2,231 \$   | 2,264 \$   | 2,298 \$   | 2,332 \$   | 2,367 \$   | 2,403 \$ 2,439 |
| FCFF                    | \$ 52,962  | \$ 52,330  | \$ 51,666  | \$ 50,971  | \$ 50,243  | \$ 48,283  | \$ 46,325  | \$ 44,369  | \$ 42,417  | \$ 40,471      |

|                         | 11 (TY)    |
|-------------------------|------------|
| Revenue growth rate     | 1.50%      |
| Revenues                | \$ 268,025 |
| EBIT (Operating) margin | 25.00%     |
| EBIT (Operating income) | \$ 67,006  |
| Tax rate                | 35.00%     |
| EBIT(1-t)               | \$ 43,554  |
| - Reinvestment          | \$ 5,444   |
| FCFF                    | \$ 38,110  |

**Riskfree Rate**: Riskfree rate = 1.9%

| Revenues                 | \$ | 227,535 |
|--------------------------|----|---------|
| Operating income or EBIT | \$ | 66,864  |
| Revenue	growth	-	LTM     |    | -5.22%  |
| Pre-tax	Operating	margin |    | 33.28%  |

#### **Most recent twelve months**

| Value of operating assets =     | \$ 552,748 |
|---------------------------------|------------|
| - Debt                          | \$ 64,735  |
| + Cash                          | \$ 204,928 |
| Value of equity                 | \$ 692,941 |
| - Value of options              | \$ 89      |
| Value of equity in common stock | \$ 692,852 |
| Number of shares                | 5,478.45   |
| Estimated value /share          | \$ 126.47  |

# Step 2: Identify value drivers

![](_page_9_Figure_1.jpeg)

# Step 3: Doing your homework

¨ Historical: The obvious place to start to get a sense of what uncertainties you face on a variable is to look at its historical behavior. ¤ How much has it moved over time? ¤ What factors seem to cause it to move? ¨ Cross-sectional: You can also look at differences on this variable across the sample today. Thus, in deciding how profit margins can vary for a software company, you can look at profit margin variations across software companies. ¨ Intuitive: You can keep your analysis grounded by bringing in common sense rules on the range for a variable.

# Apple's historical data

![](_page_11_Figure_1.jpeg)

# The iPhone Decade

![](_page_12_Figure_1.jpeg)

# Revenue Growth at Aging Tech Firms

![](_page_13_Figure_2.jpeg)

# Step 4: Probability Distributions - Choices

![](_page_14_Diagram_1.jpeg)

# For Apple's revenue growth & margin

![](_page_15_Figure_15.jpeg)

Correlation between revenue growth & margin = 0.50

**Distribution:** Lognormal  
**Parameters:** Location = -5%  
Expected value = 1.50%  
Std deviation = 2.5%

![](_page_15_Figure_18.jpeg)

**Distribution:** Triangular  
**Parameters:** Minimum = 15%  
Expected value = 25%  
Maximum = 35%

#### Step 5: Constraints, Correlations and Connections

¨ You can build in constraints that will affect the company's operations, and its value, that are either internally or externally imposed. ¤ Internal constraints can include refusal to issue new stock, borrow money or pay dividends. ¤ External constraints can include failure to make debt payments or meet regulatory capital requirements. ¨ You can also build in correlations between the variables that you are attaching probability distributions to.

# Step 6: Run the Simulation

□ **Crystal Ball:** <http://www.oracle.com/us/products/applications/crystalball/crystal-ball-product/overview/index.html>

![](_page_17_Picture_23.jpeg)

**Define distributions  
for variables**

**Specify output  
variable**

**Number of  
simulations**

# The Value Distribution

![](_page_18_Figure_1.jpeg)

# Conclusion

¨ Not looking at what you are uncertain about does not make it go away. ¨ Ironically, taking a closer look at what you fear (being wrong) can make you less fearful. ¨ Look into the (uncertainty) abyss. It might not be as dark and dangerous as you think it is.