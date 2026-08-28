## Session 8: Regression Betas

*Stocks are risky! Really!*

*Aswath Damodaran*

---

## Estimating Beta

- The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm):

  `Rj = a + b Rm`

  where `a` is the intercept and `b` is the slope of the regression.

- The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.
- The R-squared (R²) of the regression provides an estimate of the proportion of the risk (variance) of a firm that can be attributed to market risk. The balance `(1 − R²)` can be attributed to firm-specific risk.

---

## Estimating Performance

- The intercept of the regression provides a simple measure of performance during the period of the regression, relative to the capital asset pricing model.
- The difference between the intercept and `Rf(1 − b)` is Jensen's alpha. If it is positive, your stock performed better than expected during the period of the regression.

---

## Setting Up for the Estimation

- Decide on an estimation period:
  - Services use periods ranging from 2 to 5 years for the regression.
  - Longer estimation periods provide more data, but firms change over time.
  - Shorter periods can be affected more easily by significant firm-specific events that occurred during the period.
- Decide on a return interval — daily, weekly, monthly:
  - Shorter intervals yield more observations, but suffer from more noise.
  - Noise is created by stocks not trading and biases all betas towards one.
- Estimate returns (including dividends) on stock:
  - `Return = (PriceEnd − PriceBeginning + DividendsPeriod) / PriceBeginning`
  - Include dividends only in the ex-dividend month.
- Choose a market index, and estimate returns (inclusive of dividends) on the index for each interval over the period.

---

## Choosing the Parameters: Disney

- Period used: 5 years
- Return Interval: Monthly
- Market Index: S&P 500 Index

For instance, to calculate returns on Disney in December 2009:
- Price for Disney at end of November 2009 = $30.22
- Price for Disney at end of December 2009 = $32.25
- Dividends during month = $0.35 (it was an ex-dividend month)
- `Return = ($32.25 − $30.22 + $0.35) / $30.22 = 7.88%`

To estimate returns on the index in the same month:
- Index level at end of November 2009 = 1,095.63
- Index level at end of December 2009 = 1,115.10
- Dividends on index in December 2009 = 1.683
- `Return = (1,115.10 − 1,095.63 + 1.683) / 1,095.63 = 1.78%`

---

## Disney's Historical Beta

*(diagram)*

---

## Analyzing Disney's Performance

- Intercept = 0.712%
  - This is an intercept based on monthly returns. Thus, it has to be compared to a monthly riskfree rate.
  - Between 2008 and 2013:
    - Average Annualized T-Bill rate = 0.50%
    - Monthly Riskfree Rate = 0.5% / 12 = 0.042%
    - Riskfree Rate (1 − Beta) = 0.042% × (1 − 1.252) = −0.0105%
- The comparison is then between:
  - Intercept vs. Riskfree Rate (1 − Beta)
  - 0.712% vs. −0.0105%
  - Jensen's Alpha = 0.7122% − (−0.0105%) = 0.723%
- Disney did 0.723% better than expected per month between October 2008 and September 2013.
  - Annualized, Disney's annual excess return = (1.00723)¹² − 1 = 9.02%
- This positive Jensen's alpha is a sign of good management at the firm.
  - True
  - False

---

## Estimating Disney's Beta

- Slope of the regression of 1.25 is the beta.
- Regression parameters are always estimated with error. The error is captured in the standard error of the beta estimate, which in the case of Disney is 0.10.
- Assume that you were asked what Disney's true beta is, after this regression:
  - What is your best point estimate?
  - What range would you give, with 67% confidence?
  - What range would you give, with 95% confidence?

---

## The Dirty Secret of "Standard Error"

*(diagram)*

---

## Breaking Down Disney's Risk

- R-Squared = 73%
- This implies that:
  - 73% of the risk at Disney comes from market sources.
  - 27%, therefore, comes from firm-specific sources.
- The firm-specific risk is diversifiable and will not be rewarded.
- The R-squared for companies globally has increased significantly since 2008. Why might this be happening?
- What are the implications for investors?

---

## Beta Estimation: Using a Service (Bloomberg)

*(diagram)*

---

## Estimated Expected Returns for Disney in November 2013

Inputs to the expected return calculation:
- Disney's Beta = 1.25
- Riskfree Rate = 2.75% (US ten-year T-Bond rate in November 2013)
- Risk Premium = 5.76% (based on Disney's operating exposure)

`Expected Return = Riskfree Rate + Beta × (Risk Premium)`

`= 2.75% + 1.25 × (5.76%) = 9.95%`

---

## Use to a Potential Investor in Disney

- As a potential investor in Disney, what does this expected return of 9.95% tell you?
  - This is the return that I can expect to make in the long term on Disney, if the stock is correctly priced and the CAPM is the right model for risk.
  - This is the return that I need to make on Disney in the long term to break even on my investment in the stock.
  - Both.
- Assume now that you are an active investor and that your research suggests that an investment in Disney will yield 12.5% a year for the next 5 years. Based upon the expected return of 9.95%, you would:
  - Buy the stock.
  - Sell the stock.

---

## How Managers Use This Expected Return

- Managers at Disney:
  - Need to make at least 9.95% as a return for their equity investors to break even.
  - This is the hurdle rate for projects, when the investment is analyzed from an equity standpoint.
- In other words, Disney's cost of equity is 9.95%.
- What is the cost of not delivering this cost of equity?

---

## Application Test: Analyzing the Risk Regression

- If you can get a beta regression page (or output) for your company against a market index, answer the following questions:
  - How well or badly did your stock do, relative to the market, during the period of the regression?
  - `Intercept − (Riskfree Rate / n) × (1 − Beta) = Jensen's Alpha`
    - where `n` is the number of return periods in a year (12 if monthly; 52 if weekly).
  - What proportion of the risk in your stock is attributable to the market? What proportion is firm-specific?
  - What is the historical estimate of beta for your stock? What is the range on this estimate with 67% probability? With 95% probability?
  - Based upon this beta, what is your estimate of the required return on this stock?
    - `Riskless Rate + Beta × Risk Premium`

---

## Task & Reading

- Task: Break down the beta regression for your company.
- Optional: Read Chapter 4
