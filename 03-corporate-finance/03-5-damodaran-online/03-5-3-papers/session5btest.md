---
title: "Session5Btest"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/Statistics101/postclass/session5Btest.pdf
---

## **Session 5B: Post Class Test**

- 1. If you are trying to explain investment returns using macroeconomic variables in a multiple regression, which of the following processes would you use in building your regression and why?
  - a. Run the regression only with variables that other researchers have found statistically significant in the past
  - b. Search for the variables that have the highest statistical explanatory power and fit them into your regression
  - c. Start with variables that other researchers have found statistically significant and add other variables that improve explanatory power
  - d. Start with variables that other researchers have found statistically significant and add other variables that improve explanatory power, but only if I have a theoretical or common-sense reason for including those variables.
  - e. Stick with only those variables that should matter, based upon theory, even if your explanatory power is low
  - f. None of the above
- 2. You have been given access to a large database containing information over time on hundreds of financial ratios for companies, measuring profitability, growth, leverage and other business model effects, and trying to see if you can use them to see how stocks are being priced by the market. (You also have data on market capitalizations of companies)
  - a. What would you use as your dependent variable and why?
  - b. How would you go about picking the independent variables in your regression?
  - c. Once you pick the independent variables, what would you do (if anything) before you run the regression?
  - d. After you have run your multiple regression, how would you check for statistical significance?
  - e. Before you use the regression for predictions, what final tests would you run to ensure that you can trust your predictions?
- 3. P-hacking refers to the practice that researchers use to arrive at statistical significance (t statistics and p values), when researching a topic. Which of the following practices do phackers use?
  - a. Removing observations from the sample that are "outliers"
  - b. Altering the time period of your analysis (by adding or removing years)
  - c. Capping or flooring the values of independent variables that have extreme values (This refers to the practice of setting a value at a pre-set maximum or minimum, if it exceeds or falls below that value)
  - d. Filling in values for missing values for variables
  - e. All of the above
- 4. You are analyzing the PE ratios of a select list of fifteen tech companies and have collected information on expected growth rates in earnings for each company, as well as on whether the CEO of the company is a founder or a professional manager.

|           | PE    | Expected Growth | Founder/Professional Mgt |
|-----------|-------|-----------------|--------------------------|
| Tech Co 1 | 12.33 | 5.35%           | Professional             |
| Tech Co 2 | 14.60 | 3.80%           | Founder                  |
| Tech Co 3 | 17.50 | 4.22%           | Founder                  |

| Tech Co 4  | 19.00 | 8.05%  | Professional |
|------------|-------|--------|--------------|
| Tech Co 5  | 22.56 | 7.68%  | Founder      |
| Tech Co 6  | 25.48 | 9.35%  | Founder      |
| Tech Co 7  | 27.98 | 12.22% | Professional |
| Tech Co 8  | 29.04 | 10.90% | Founder      |
| Tech Co 9  | 32.12 | 16.50% | Professional |
| Tech Co 10 | 34.77 | 14.44% | Professional |
| Tech Co 11 | 37.65 | 15.02% | Professional |
| Tech Co 12 | 39.18 | 19.19% | Professional |
| Tech Co 13 | 45.27 | 18.50% | Founder      |
| Tech Co 14 | 50.35 | 20.33% | Professional |
| Tech Co 15 | 61.80 | 22.62% | Founder      |

- a. Using this data, analyze the link between PE ratios and expected growth. (Go through the full process, starting with a scatter plot and ending with a regression)
- b. Now assume that you believe that founder-run companies trade at a premium (higher PE) than those run by professional managers. How would you test this proposition?
- c. How would you use this regression to assess whether tech company 1, which has the lowest PE ratio of the group is under or over valued by the market?
- 5. You are reviewing a regression of PEG ratios against expected growth, and note that the researcher has used ln(expected growth) to deal with the nonlinear relationship to arrive at the following equation: PEG = 1.85 + 0.12 ln (Expected Growth Rate) (If the growth rate is 20%, you would use ln(.20) in the regression)
  - a. Estimate the PEG ratio for three companies, one with an expected growth rate of 25%, one with an expected growth rate of 15% and one with an expected growth rate of 2%.
  - b. Assume that you find a company trading at a PEG ratio of 1.60 that you believe is fairly priced (given this regression). Estimate the expected growth rate for this company.