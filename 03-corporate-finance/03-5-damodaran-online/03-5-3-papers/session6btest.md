---
title: "Session6Btest"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session6Btest.pdf
---

## **Session 6B: Post Class Test**

- 1. In a Monte Carlo simulation, you replace point estimates for input variables with distributions reflecting your uncertainty about input variables, and then run simulations to get a distribution of values for the output variable. Since most models connecting input variables to output variable have dozens of inputs, which of the following approaches would you follow, if you were running the simulation:
  - a. Estimate distributions for every input variable in the model
  - b. Estimate distributions for a few input variables, picked at random
  - c. Estimate distributions for the input variables that affect your output variable the most, i.e., when they change, the output variable changes a lot.
  - d. Estimate distributions for the input variables where you feel the most uncertainty about the value of that variable in the future
  - e. Estimate distributions for the input variables that affect your output variable the most, i.e., when they change, the output variable changes a lot, and where you feel the most uncertainty about the value of the variable in the future.
- 2. Once you have picked the input variables that you will estimating probability distributions for, you have find statistical distributions that best fit each variable.
  - a. What are the steps you would go through to find the best fit distribution?
  - b. What if there is neither historical nor cross sectional data on a specific variable?
  - c. What if a variable is discrete rather than continuous?
- 3. In some simulations, the input variables that you are estimating distributions for may be correlated, i.e., when one has a value that is higher than expected, another is likely to as well.
  - a. How would you determine whether there is correlation across two variables?
  - b. How would you bring in this correlation into your simulation?
  - c. If you choose to ignore this simulation, what are the consequences for the distribution of your output variable?
- 4. In the figure and table below, I have summarized the results of a simulation that I ran, when valuing a company (Zomato).

![](_page_1_Figure_0.jpeg)

![](_page_1_Figure_1.jpeg)

![](_page_1_Figure_2.jpeg)

![](_page_1_Figure_4.jpeg)

| <i>Percentile</i> | <i>Value per share</i> |
|-------------------|------------------------|
| 0%                | ₹ 0.22                 |
| 10%               | ₹ 24.49                |
| 20%               | ₹ 27.96                |
| 30%               | ₹ 30.74                |
| 40%               | ₹ 33.35                |
| 50%               | ₹ 36.02                |
| 60%               | ₹ 38.86                |
| 70%               | ₹ 42.11                |
| 80%               | ₹ 46.07                |
| 90%               | ₹ 51.92                |
| 100%              | ₹ 91.69                |

- a. Focusing on the input variables, how would you intuitively explain the choice of distributions and what it tells you about the underlying variable.
- b. Note the correlation of 0.50 between market share and operating margins. Intuitively explain why this correlation exists, and what effect it is having on your value distribution.
- c. Looking at the distribution of the output variable, and the percentile table, how would you intuitively explain the output? What actions would you take, based upon this simulation?
- 5. In capital budgeting, a good project is defined as one that delivers a positive net present value. Assume that you decide to do a simulation on a capital budgeting project, and come up with an average net present value of \$100 million (obtained by discounting expected cash flows at a risk-adjusted rate) across 10,000 simulations, but that you also find that the project has a negative net present value in 30% of the simulations.
  - a. Would you accept or reject the project? Explain.
  - b. Is there anything else that you can do as the decision-maker to use this simulation to improve your decision?