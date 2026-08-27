## Session 11: The "Right" Beta

*The law of large numbers is your best friend.*

*Aswath Damodaran*

---

## Estimating Bottom-Up Betas and Costs of Equity: Vale

*(diagram)*

---

## Vale: Cost of Equity Calculation — In Nominal R$

- To convert a discount rate in one currency to another, all you need are expected inflation rates in the two currencies.
- From US$ to R$: Using 2% as the inflation rate in US dollars and 9% as the inflation rate in Brazil, we can convert Vale's US dollar cost of equity of 11.23% to an R$ cost of equity.
- Alternatively, you can compute a cost of equity starting with the R$ riskfree rate of 10.18%:

  `Cost of Equity in R$ = 10.18% + 1.15 × (7.38%) = 18.67%`

---

## Bottom-Up Betas and Costs of Equity: Tata Motors and Baidu

- **Tata Motors:** We estimated an unlevered beta of 0.8601 across 76 publicly traded automotive companies (globally) and estimated a levered beta based on Tata Motors' D/E ratio of 41.41% and a marginal tax rate of 32.45% for India:

  `Levered Beta for Tata Motors = 0.8601 × (1 + (1 − 0.3245) × 0.4141) = 1.1007`

  `Cost of Equity (Rs) = 6.57% + 1.1007 × (7.19%) = 14.49%`

- **Baidu:** To estimate its beta, we looked at 42 global companies that derive all or most of their revenues from online advertising and estimated an unlevered beta of 1.30 for the business. Incorporating Baidu's current market debt-to-equity ratio of 5.23% and the marginal tax rate for China of 25%, we estimate Baidu's current levered beta to be 1.3560:

  `Levered Beta for Baidu = 1.30 × (1 + (1 − 0.25) × 0.0523) = 1.356`

  `Cost of Equity for Baidu (Renminbi) = 3.50% + 1.356 × (6.94%) = 12.91%`

---

## Bottom-Up Betas and Costs of Equity: Deutsche Bank

- We break Deutsche Bank down into two businesses — commercial and investment banking.
- We do not unlever or relever betas, because estimating debt and equity for banks is an exercise in futility.

*(diagram)*

---

## Estimating Betas for Non-Traded Assets

- The conventional approaches of estimating betas from regressions do not work for assets that are not traded. There are no stock prices or historical returns that can be used to compute regression betas.
- There are two ways in which betas can be estimated for non-traded assets:
  - Using comparable firms.
  - Using accounting earnings.

---

## Using Comparable Firms to Estimate Beta for Bookscape

`Unlevered beta for book company = 0.8130 / (1 + (1 − 0.4) × 0.2141) = 0.7205`

`Unlevered beta for book business = 0.7205 / (1 − 0.05) = 0.7584`

*(diagram)*

---

## Estimating Bookscape's Levered Beta and Cost of Equity

- Because the debt/equity ratios used in computing levered betas are market debt-equity ratios, and the only debt-equity ratio we can compute for Bookscape is a book value debt-equity ratio, we have assumed that Bookscape is close to the book industry median market debt-to-equity ratio of 21.41%.
- Using a marginal tax rate of 40% for Bookscape, we get a levered beta of 0.8558:

  `Levered Beta for Bookscape = 0.7584 × [1 + (1 − 0.40) × 0.2141] = 0.8558`

- Using a riskfree rate of 2.75% (US treasury bond rate) and an equity risk premium of 5.5%:

  `Cost of Equity = 2.75% + 0.8558 × (5.5%) = 7.46%`

---

## Is Beta an Adequate Measure of Risk for a Private Firm?

- Beta measures the risk added on to a diversified portfolio. The owners of most private firms are not diversified. Therefore, using beta to arrive at a cost of equity for a private firm will:
  - a. Under-estimate the cost of equity for the private firm.
  - b. Over-estimate the cost of equity for the private firm.
  - c. Could under- or over-estimate the cost of equity for the private firm.

---

## Total Risk Versus Market Risk

- Adjust the beta to reflect total risk rather than market risk. This adjustment is relatively simple, since the R-squared of the regression measures the proportion of the risk that is market risk.

  `Total Beta = Market Beta / Correlation of the sector with the market`

  In the Bookscape example, where the market beta is 0.8558 and the average R-squared of the comparable publicly traded firms is 26.00%, the correlation with the market is 50.99%.

  `Total Beta = 0.8558 / 0.5099 = 1.6783`

  `Total Cost of Equity = 2.75% + 1.6783 × (5.5%) = 11.98%`

---

## Application Test: Estimating a Bottom-Up Beta

- Based upon the business or businesses that your firm is in right now, and its current financial leverage, estimate the bottom-up unlevered beta for your firm.
- Data Source: You can get a listing of unlevered betas by industry on my website by going to updated data.

---

## Task & Reading

- Task: Estimate the beta your company would have if it were a private business.
- Optional: Read Chapter 4
