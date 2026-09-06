---
title: "Italy"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/country/Italy.pdf
---

# Valuation

Aswath Damodaran

http://www.stern.nyu.edu/~adamodar

![](_page_1_Picture_3.jpeg)

## Some Initial Thoughts

" One hundred thousand lemmings cannot be wrong"

*Graffiti*

#### A philosophical basis for Valuation

n Many investors believe that the pursuit of 'true value' based upon financial fundamentals is a fruitless one in markets where prices often seem to have little to do with value. n There have always been investors in financial markets who have argued that market prices are determined by the perceptions (and misperceptions) of buyers and sellers, and not by anything as prosaic as cashflows or earnings. n Perceptions matter, but they cannot be all the matter. n Asset prices cannot be justified by merely using the "bigger fool" theory.

#### Misconceptions about Valuation

- n Myth 1: A valuation is an objective search for "true" value
  - Truth 1.1: All valuations are biased. The only questions are how much and in which direction.
- Truth 1.2: The direction and magnitude of the bias in your valuation is directly proportional to who pays you and how much you are paid. n Myth 2.: A good valuation provides a precise estimate of value
  - Truth 2.1: There are no precise valuations
- Truth 2.2: The payoff to valuation is greatest when valuation is least precise. n Myth 3: . The more quantitative a model, the better the valuation
  - Truth 3.1: One's understanding of a valuation model is inversely proportional to the number of inputs required for the model.
  - Truth 3.2: Simpler valuation models do much better than complex ones.

#### Approaches to Valuation

n **Discounted cashflow valuation**, relates the value of an asset to the present value of expected future cashflows on that asset. n **Relative valuation**, estimates the value of an asset by looking at the pricing of 'comparable' assets relative to a common variable like earnings, cashflows, book value or sales. n **Contingent claim valuation**, uses option pricing models to measure the value of assets that share option characteristics.

#### Discounted Cash Flow Valuation

- n **What is it**: In discounted cash flow valuation, the value of an asset is the present value of the expected cash flows on the asset. n **Philosophical Basis**: Every asset has an intrinsic value that can be estimated, based upon its characteristics in terms of cash flows, growth and risk. n **Information Needed**: To use discounted cash flow valuation, you need
  - to estimate the life of the asset
  - to estimate the cash flows during the life of the asset
- to estimate the discount rate to apply to these cash flows to get present value n **Market Inefficiency**: Markets are assumed to make mistakes in pricing assets across time, and are assumed to correct themselves over time, as new information comes out about assets.

#### Valuing a Firm

n The value of the firm is obtained by discounting expected cashflows to the firm, i.e., the residual cashflows after meeting all operating expenses and taxes, but prior to debt payments, at the weighted average cost of capital, which is the cost of the different components of financing used by the firm, weighted by their market value proportions.

where,

CF to Firm<sup>t</sup> = Expected Cashflow to Firm in period t

WACC = Weighted Average Cost of Capital

$$\text{Value of Firm} = \sum_{t=1}^{t=n} \frac{\text{CF to Firm}_t}{(1 + \text{WACC})^t}$$

#### Discounted Cash Flow Valuation: The Steps

- n Estimate the **discount rate** or rates to use in the valuation
  - Discount rate can be either a cost of equity (if doing equity valuation) or a cost of capital (if valuing the firm)
  - Discount rate can be in nominal terms or real terms, depending upon whether the cash flows are nominal or real
- Discount rate can vary across time. n Estimate the **current earnings** and **cash flows** on the asset, to either equity investors (CF to Equity) or to all claimholders (CF to Firm) n Estimate the **future earnings and cash flows** on the asset being valued, generally by estimating an expected growth rate in earnings. n Estimate **when** the firm will reach **"stable growth"** and what characteristics (risk & cash flow) it will have when it does. n Choose the **right DCF model** for this asset and value it.

![](_page_8_Diagram_1.jpeg)

#### DISCOUNTED CASHFLOW VALUATION

![](_page_9_Diagram_1.jpeg)

#### Telecom Italia: A Valuation (in Euros)

![](_page_10_Diagram_1.jpeg)

#### Compaq: Status Quo

#### I. Discount Rates: Cost of Equity

n Consider the standard approach to estimating cost of equity:

Cost of Equity = 
$$R_f + \text{Equity Beta} * (E(R_m) - R_f)$$

where,

Rf= Riskfree rate

## $$E(R_m) = \text{Expected Return on the Market Index (Diversified Portfolio)}$$

- n In practice,
  - Short term government security rates are used as risk free rates
  - Historical risk premiums are used for the risk premium
  - Betas are estimated by regressing stock returns against market returns

## Short term Governments are not risk free

- n On a riskfree asset, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. n For an investment to be riskfree, then, it has to have
  - No default risk
- No reinvestment risk n Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time n A simpler approach is to match the duration of the analysis (generally long term) to the duration of the riskfree rate (also long term) n In emerging markets, there are two problems:
  - The government might not be viewed as riskfree (Brazil, Indonesia)
  - There might be no market-based long term government rate (China)

## Estimating a Riskfree Rate

- n Estimate a range for the riskfree rate in local terms:
  - *Upper limit*: Obtain the rate at which the largest, safest firms in the country borrow at and use as the riskfree rate.
- *Lower limit*: Use a local bank deposit rate as the riskfree rate n Do the analysis in real terms (rather than nominal terms) using a real riskfree rate, which can be obtained in one of two ways –
  - from an inflation-indexed government bond, if one exists
- set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done. n Do the analysis in another more stable currency, say US dollars.

## A Simple Test

n You are valuing a Brazilian company in U.S. dollars and are attempting to estimate a risk free rate to use in the analysis. The risk free rate that you should use is o The interest rate on a nominal BR Brazilian government bond o The interest rate on a dollar-denominated Brazilian government bond o The interest rate on a US treasury bond

## Everyone uses historical premiums, but..

- n The historical premium is the premium that stocks have historically earned over riskless securities. n Practitioners never seem to agree on the premium; it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. n For instance, looking at the US:

| Historical period | Arith  | Stocks - T.Bills Geom | Arith  | Stocks - T.Bonds Geom |
|-------------------|--------|-----------------------|--------|-----------------------|
| 1926-1998         | 9.31%  | 7.95%                 | 7.52%  | 6.38%                 |
| 1962-1998         | 6.81%  | 6.03%                 | 5.68%  | 5.29%                 |
| 1981-1998         | 12.96% | 10.72%                | 12.22% | 10.09%                |

## If you choose to use historical premiums….

n Go back as far as you can. A risk premium comes with a standard error. Given the annual standard deviation in stock prices is about 25%, the standard error in a historical premium estimated over 25 years is roughly:

Standard Error in Premium = 
$$25\%/\sqrt{25} = 25\%/5 = 5\%$$

n Be consistent in your use of the riskfree rate. Since we argued for long term bond rates, the premium should be the one over T.Bonds n Use the geometric risk premium. It is closer to how investors think about risk premiums over long periods. n Never use historical risk premiums estimated over short periods. n For emerging markets, start with the base historical premium in the US and add a country spread, based upon the country rating and the relative equity market volatility.

## Assessing Country Risk Using Currency Ratings: Western Europe

| Country        | Rating | Default Spread |
|----------------|--------|----------------|
| Belgium        | Aa1    | 75             |
| Denmark        | Aaa    | 0              |
| France         | Aaa    | 0              |
| Germany        | Aaa    | 0              |
| Greece         | A2     | 120            |
| Ireland        | Aaa    | 0              |
| Italy          | Aa3    | 90             |
| Netherlands    | Aaa    | 0              |
| Norway         | Aaa    | 0              |
| Portugal       | Aa2    | 85             |
| United Kingdom | Aaa    | 0              |

## Assessing Country Risk using Ratings: Eastern Europe

| Country        | Rating | Default Spread (In bp) |
|----------------|--------|------------------------|
| Bulgaria       | B2     | 550                    |
| Croatia        | Baa3   | 145                    |
| Czech Republic | Baa1   | 120                    |
| Hungary        | Baa2   | 130                    |
| Russia         | B3     | 650                    |
| Slovenia       | A3     | 95                     |

## Using Country Ratings to Estimate Equity Spreads

- n Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
  - One way to adjust the country spread upwards is to use information from the US market. In the US, the equity risk premium has been roughly twice the default spread on junk bonds.
  - Another is to multiply the bond spread by the relative volatility of stock and bond prices in that market. For example,
    - Standard Deviation in MIB30 (Equity) = 15.64%
    - Standard Deviation in Italian long bond = 9.2%
- Adjusted Equity Spread = 0.90% (15.64/9.2) = 1.53% n Ratings agencies make mistakes. They are often late in recognizing and building in risk.

#### Ratings Errors: Ratings for Asia

| Country     | July 1997 Rating | January 1998 Ratings |
|-------------|------------------|----------------------|
| China       | BBB+             | BBB+                 |
| Indonesia   | BBB              | CCC+                 |
| India       | BB+              | BB+                  |
| Japan       | AAA              | AAA                  |
| South Korea | AA-              | BB+                  |
| Malaysia    | A+               | A                   |
| Pakistan    | B+               | B                   |
| Philippines | BB+              | BB+                  |
| Singapore   | AAA              | AAA                  |
| Taiwan      | AA+              | AA+                  |
| Thailand    | A                | BBB-                 |

## From Country Spreads to Risk premiums

n Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country Spread} + \text{Beta (US premium)}$$

Implicitly, this is what you are assuming when you use the local Government's dollar borrowing rate as your riskfree rate.

n Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium} + \text{Country Spread})$$

n Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium})+\lambda (\text{Country Spread})$$

## Estimating Exposure to Country Risk

n Different companies should be exposed to different degrees to country risk. For instance, an Italian firm that generates the bulk of its revenues in Western Europe should be less exposed to country risk in Italy than one that generates all its business within Italy.

■ The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:

$$\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{avg firm}}$$

For instance, if a firm gets 35% of its revenues domestically while the average firm in that market gets 70% of its revenues domestically

l = 35%/ 70 % = 0.5

- n There are two implications
  - A company's risk exposure is determined by where it does business and not by where it is located
  - Firms might be able to actively manage their country risk exposures

## Estimating E(Return) for Telecom Italia

n Assume that the beta for Telecom Italia is 0.87, and that the riskfree rate used is 4.24%. (Italian long bond rate) n Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

E(Return) = 4.24% + 1.53% + 0.87 (6.38%) = 11.32%

n Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

E(Return) = 4.24% + 0.87 (6.38%+ 1.53%) = 11.12%

n Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

E(Return)=4.24% + 0.87(6.38%) + 1.25 (1.53%) = 11.70%

Telecom Italia is more exposed to country risk than the typical Italian firm since much of its business is in the country.

#### Implied Equity Premiums

- n If we use a basic discounted cash flow model, we can estimate the implied risk premium from the current level of stock prices. n For instance, if stock prices are determined by the simple Gordon Growth Model:
  - Value = Expected Dividends next year/ (Required Returns on Stocks Expected Growth Rate)
- Plugging in the current level of the index, the dividends on the index and expected growth rate will yield a "implied" expected return on stocks. Subtracting out the riskfree rate will yield the implied premium. n The problems with this approach are:
  - the discounted cash flow model used to value the stock index has to be the right one.
  - the inputs on dividends and expected growth have to be correct
  - it implicitly assumes that the market is currently correctly valued

## Implied Premiums in US Market

![](_page_25_Figure_1.jpeg)

## Implied Premium for Italian Market: June 1, 1999

- n Level of the Index = 35152 n Dividends on the Index = 2.15% of 35152 (Used weighted yield) n Other parameters
  - Riskfree Rate = 4.24%
  - Expected Growth (in nominal dollar terms)
    - Next 5 years = 10% (Used expected growth rate in Earnings)
- After year 5 = 5% n Solving for the expected return:
  - Expected return on Equity = 7.82%
  - Implied Equity premium = 3.58%

## An Intermediate Solution

- n The historical risk premium of 6.38% for the United States is too high a premium to use in valuation. It is
  - As high as the highest implied equity premium that we have ever seen in the US market (making your valuation a worst case scenario)
- Much higher than the actual implied equity risk premium in the market n The current implied equity risk premium is too low because
- It is lower than the equity risk premiums in the 60s, when inflation and interest rates were as low n The average implied equity risk premium between 1960-1998 in the United States is about 4%. We will use this as the premium for a mature equity market.

## Estimating Beta

<sup>n</sup> The standard procedure for estimating betas is to regress stock returns (R<sup>j</sup> ) against market returns (Rm) -

$$R_j = a + b R_m$$

- where a is the intercept and b is the slope of the regression.

n The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.

n This beta has three problems:

- It has high standard error
- It reflects the firm's business mix over the period of the regression, not the current mix
- It reflects the firm's average financial leverage over the period rather than the current leverage.

# Beta Estimation: The Noise Problem

![](_page_29_Figure_29.jpeg)

# Beta Estimation: The Index Effect

![](_page_30_Figure_16.jpeg)

#### Determinants of Betas

- n **Product or Service**: The beta value for a firm depends upon the sensitivity of the demand for its products and services and of its costs to macroeconomic factors that affect the overall market.
  - Cyclical companies have higher betas than non-cyclical firms
- Firms which sell more discretionary products will have higher betas than firms that sell less discretionary products n **Operating Leverage**: The greater the proportion of fixed costs in the cost structure of a business, the higher the beta will be of that business. This is because higher fixed costs increase your exposure to all risk, including market risk. n **Financial Leverage**: The more debt a firm takes on, the higher the beta will be of the equity in that business. Debt creates a fixed cost, interest expenses, that increases exposure to market risk.

#### Equity Betas and Leverage

n The beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_L = \beta_u (1 + ((1-t)D/E))$$

where

### $\beta_L = \text{Levered or Equity Beta}$

 $\beta_u = \text{Unlevered Beta}$ 

t = Corporate marginal tax rate

D = Market Value of Debt

E = Market Value of Equity

n While this beta is estimated on the assumption that debt carries no market risk (and has a beta of zero), you can have a modified version:

$$\beta_L = \beta_u (1 + ((1-t)D/E) - \beta_{debt} (1-t) D/(D+E))$$

#### The Solution: Bottom-up Betas

- n The bottom up beta can be estimated by :
  - Taking a weighted (by sales or operating income) average of the unlevered betas of the different businesses a firm is in.

(The unlevered beta of a business can be estimated by looking at other firms in the same business)

- Lever up using the firm's debt/equity ratio

n The bottom up beta will give you a better estimate of the true beta when

- It has lower standard error ( $SE_{\text{average}} = SE_{\text{firm}} / \sqrt{n}$  ( $n = \text{number of firms}$ )
- It reflects the firm's current business mix and financial leverage
- It can be estimated for divisions and private firms.

$$\sum_{j=1}^{j=k} \beta_j \left[ \frac{\text{Operating Income}_j}{\text{Operating Income}_{\text{Firm}}} \right]$$

$$\beta_{\text{levered}} = \beta_{\text{unlevered}}[1 + (1 - \text{tax rate}) (\text{Current Debt/Equity Ratio})]$$

#### Telecom Italia's Bottom-up Beta

|         | Unlevered | D/E Ratio | Levered | Riskfree | Risk    | Cost of |
|---------|-----------|-----------|---------|----------|---------|---------|
|         | Beta      |           | Beta    | Rate     | Premium | Equity  |
| Telecom | 0.79      | 18.8%     | 0.87    | 4.24%    | 7.03%   | 12.33%  |

Proportion of operating income from telecom = 100%

Unlevered Beta for Telecom Italia= 0.79

Levered Beta for Telecom Italia = 0.79 (1+ (1- .4908)) = 0.87

Assume now that Telecom Italia decides to go into the internet business, and that the unlevered beta for that business is 1.51. Assuming that 25% of Telecom Italia's business looking forward will come from this business, what will the firm's beta be?

## Compaq's Bottom-up Beta

| Business           | Unlevered Beta | D/E Ratio | Levered Beta | Proportion of Value |
|--------------------|----------------|-----------|--------------|---------------------|
| Personal Computers | 1.24           | 0%        | 1.24         | 42.15%              |
| Mainframes         | 1.35           | 0%        | 1.35         | 15.55%              |
| Software & Service | 1.22           | 0%        | 1.22         | 26.79%              |
| Internet           | 1.51           | 0%        | 1.51         | 15.51%              |
| Compaq             | 1.29           | 0%        | 1.29         | 100%                |

Proportion of value wa s estimated for each division by multiplying the revenues of each division by the average value to sales ratios of other firms in that business

| Investor Type                                                                                                                |                  |             | Cares about                      | Risk Measure                  | Cost of Equity | Firm Value   |
|------------------------------------------------------------------------------------------------------------------------------|------------------|-------------|----------------------------------|-------------------------------|----------------|--------------|
| Private Business: Owner has all his wealth invested in the business                                                          |                  |             | Total Risk                       | Standard Deviation            | 40%            | 100/.4=250   |
|                                                                                                                              | Competitive Risk |             |                                  |                               |                |              |
|                                                                                                                              | Sector Risk      |             |                                  |                               |                |              |
|                                                                                                                              | Int'nl Risk      |             |                                  |                               |                |              |
|                                                                                                                              |                  | Market Risk |                                  |                               |                |              |
| Venture Capitalist: Has wealth invested in a number of companies in one sector                                               |                  |             | Risk added to sector portfolio   | Beta relative to sector       | 25%            | 100/.25=400  |
|                                                                                                                              | Sector Risk      |             |                                  |                               |                |              |
|                                                                                                                              | Int'nl Risk      |             |                                  |                               |                |              |
|                                                                                                                              | Market Risk      |             |                                  |                               |                |              |
| Publicly traded company with investors who are diversified domestically or IPO to investors who are domestically diversified |                  |             | Risk added to domestic portfolio | Beta relative to local index  | 15%            | 100/.15=667  |
|                                                                                                                              | Int'nl Risk      |             |                                  |                               |                |              |
|                                                                                                                              | Market Risk      |             |                                  |                               |                |              |
|                                                                                                                              |                  |             |                                  |                               |                |              |
| Publicly traded company with investors who are diversified globally or IPO to global investors                               |                  |             | Risk added to global portfolio   | Beta relative to global index | 10%            | 100/.10=1000 |
|                                                                                                                              | Market Risk      |             |                                  |                               |                |              |

#### **Valuing a Firm from Different Risk Perspectives**

*Firm is assumed to have a cash flow of 100 each year forever.*

#### Cost of Debt

- n If the firm has bonds outstanding, and the bonds are traded, the yield to maturity on a long-term, straight (no special features) bond can be used as the interest rate. n If the firm is rated, use the rating and a typical default spread on bonds with that rating to estimate the cost of debt. n If the firm is not rated,
  - and it has recently borrowed long term from a bank, use the interest rate on the borrowing or
- estimate a synthetic rating for the company, and use the synthetic rating to arrive at a default spread and a cost of debt n The cost of debt has to be estimated in the same currency as the cost of equity and the cash flows in the valuation.

## Estimating Synthetic Ratings

n The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

n For Telecom Italia, for instance

Interest Coverage Ratio = 4313/306 = 14.09

- Based upon the relationship between interest coverage ratios and ratings, we would estimate a rating of AAA for Telecom Italia.

n Compaq has no debt. The rating that we estimate would be irrelevant.

## Interest Coverage Ratios, Ratings and Default Spreads

| If Interest Coverage Ratio is | Estimated Bond Rating | Default Spread |
|-------------------------------|-----------------------|----------------|
| > 8.50                        | AAA                   | 0.20%          |
| 6.50 - 8.50                   | AA                    | 0.50%          |
| 5.50 - 6.50                   | A+                    | 0.80%          |
| 4.25 - 5.50                   | A                     | 1.00%          |
| 3.00 - 4.25                   | A–                    | 1.25%          |
| 2.50 - 3.00                   | BBB                   | 1.50%          |
| 2.00 - 2.50                   | BB                    | 2.00%          |
| 1.75 - 2.00                   | B+                    | 2.50%          |
| 1.50 - 1.75                   | B                     | 3.25%          |
| 1.25 - 1.50                   | B –                   | 4.25%          |
| 0.80 - 1.25                   | CCC                   | 5.00%          |
| 0.65 - 0.80                   | CC                    | 6.00%          |
| 0.20 - 0.65                   | C                     | 7.50%          |
| < 0.20                        | D                     | 10.00%         |

## Estimating the pre-tax cost of debt for a firm

n The synthetic rating for Telecom Italia is AAA. The default spread for AAA rated bond is 0.20% n Pre-tax cost of debt = Riskfree Rate + Default spread = 4.24% + 0.20% = 4.44% n After-tax cost of debt = 4.44% (1-.4908) = 2.26%

## Weights for the Cost of Capital Computation

n The weights used to compute the cost of capital should be the market value weights for debt and equity. n There is an element of circularity that is introduced into every valuation by doing this, since the values that we attach to the firm and equity at the end of the analysis are different from the values we gave them at the beginning. n As a general rule, the debt that you should subtract from firm value to arrive at the value of equity should be the same debt that you used to compute the cost of capital.

## Book Value versus Market Value Weights

n It is often argued that using book value weights is more conservative than using market value weights. Do you agree? o Yes o No n It is also often argued that book values are more reliable than market values since they are not as volatile. Do you agree? o Yes o No

## Estimating Cost of Capital: Telecom Italia

#### n Equity

- Cost of Equity = 4.24% + 0.87 (5.53%) = 9.05%
- Market Value of Equity = 9.92 E/share\* 5255.13 = 52,110 Mil (84.16%)

#### n Debt

- Cost of debt = 4.24% + 0.2% (default spread) = 4.44%
- Market Value of Debt = 9,809 Mil (15.84%)

#### n Cost of Capital

Cost of Capital = 10.36 % (.8416) + 4.44% (1- .4908) (.1584)) = 9.05% (.8416) + 2.26% (.1584) = 7.98%

## Telecom Italia: Book Value Weights

n Telecom Italia has a book value of equity of 17,061 million and a book value of debt of 9,809 million. Estimate the cost of capital using book value weights instead of market value weights. n Is this more conservative?

#### Estimating Cost of Capital: Compaq

#### n Equity

- Cost of Equity = 6% + 1.29 (4%) = 11.16%
- Market Value of Equity = 23.38\*1691 = \$ 39.5 billion

#### n Debt

- Cost of debt = 6% + 1% (default spread) = 7%
- Market Value of Debt = 0

#### n Cost of Capital

Cost of Capital = 11.16 % (1.00) + 7% (1- .35) (0.00)) = 11.16%

## II. Estimating Cash Flows to Firm

EBIT ( 1 - tax rate)

+ Depreciation

- Capital Spending

- Change in Working Capital

= Cash flow to the firm

## What is the EBIT of a firm?

- n The EBIT, measured right, should capture the true operating income from assets in place at the firm. n Any expense that is not an operating expense or income that is not an operating income should not be used to compute EBIT. In other words, any financial expense (like interest expenses) or capital expenditure should not affect your operating income. n Can you name
  - A financing expense that gets treated as an operating expense?
  - A capital expense that gets treated as an operating expense?

## Operating Lease Expenses: Operating or Financing Expenses

n Operating Lease Expenses are treated as operating expenses in computing operating income. In reality, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital: n Debt Value of Operating Leases = PV of Operating Lease Expenses at the pretax cost of debt n Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

#### Operating Leases at The Home Depot in 1998

n The pre-tax cost of debt at the Home Depot is 6.25% Yr Operating Lease Expense Present Value 1 \$ 294 \$ 277 2 \$ 291 \$ 258 3 \$ 264 \$ 220 4 \$ 245 \$ 192 5 \$ 236 \$ 174 6-15 \$ 270 \$ 1,450 (PV of 10-yr annuity) Present Value of Operating Leases =\$ 2,571 n Debt outstanding at the Home Depot = \$1,205 + \$2,571 = \$3,776 mil (The Home Depot has other debt outstanding of \$1,205 million) n Adjusted Operating Income = \$2,016 + 2,571 (.0625) = \$2,177 mil

## R&D Expenses: Operating or Capital Expenses

- n Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. n To capitalize R&D,
  - Specify an amortizable life for R&D (2 10 years)
  - Collect past R&D expenses for as long as the amortizable life
  - Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

## Capitalizing R&D Expenses: Compaq

n R & D was assumed to have a 5-year life.

| Year | R&D Expense |      | Unamortized portion |
|------|-------------|------|---------------------|
| 1998 | 1353.00     | 1.00 | 1353.00             |
| 1997 | 817.00      | 0.80 | 653.60              |
| 1996 | 695.00      | 0.60 | 417.00              |
| 1995 | 270.00      | 0.40 | 108.00              |
| 1994 | 226.00      | 0.20 | 45.20               |

Value of research asset = \$ 2,577 million

Amortization of research asset in 1998 = \$ 515 million

Adjustment to Operating Income = \$ 1,353 million - \$ 515 million =\$ 838 million (increase)

## What tax rate?

n The tax rate that you should use in computing the after-tax operating income should be o The effective tax rate in the financial statements (taxes paid/Taxable income) o The tax rate based upon taxes paid and EBIT (taxes paid/EBIT) o The marginal tax rate o None of the above o Any of the above, as long as you compute your after-tax cost of debt using the same tax rate

## The Right Tax Rate to Use

n The choice really is between the effective and the marginal tax rate. In doing projections, it is far safer to use the marginal tax rate since the effective tax rate is really a reflection of the difference between the accounting and the tax books. n By using the marginal tax rate, we tend to understate the after-tax operating income in the earlier years, but the after-tax tax operating income is more accurate in later years n If you choose to use the effective tax rate, adjust the tax rate towards the marginal tax rate over time. n The tax rate used to compute the after-tax cost of debt has to be the same tax rate that you use to compute the after-tax operating income.

## A Tax Rate for a Money Losing Firm

n Assume that you are trying to estimate the after-tax operating income for a firm with \$ 1 billion in net operating losses carried forward. This firm is expected to have operating income of \$ 500 million each year for the next 3 years, and the marginal tax rate on income for all firms that make money is 40%. Estimate the after-tax operating income each year for the next 3 years.

|            | Year 1 | Year 2 | Year 3 |
|------------|--------|--------|--------|
| EBIT       | 500    | 500    | 500    |
| Taxes      |        |        |        |
| EBIT (1-t) |        |        |        |
| Tax rate   |        |        |        |

## Normalizing Earnings

- n In most valuations, we begin with the current operating income and estimate expected growth. This practice works as long as
  - Current operating income is positive
- Current operating income is normal. (In any given year, the operating income can be too low, if the firm has had a poor year, or too high, if it has had an explosively good year) n If the current operating income is negative, it has to be normalized. How you normalize earnings will depend upon why the earnings are negative in the first place.

#### **A Framework for Analyzing Companies with Negative or Abnormally Low Earnings**

![](_page_56_Diagram_1.jpeg)

## Net Capital Expenditures

n Net capital expenditures represent the difference between capital expenditures and depreciation. Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures. n In general, the net capital expenditures will be a function of how fast a firm is growing or expecting to grow. High growth firms will have much higher net capital expenditures than low growth firms. n Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

## Net Capital expenditures should include

n Research and development expenses, once they have been re-categorized as capital expenses. The adjusted cap ex will be

Adjusted Net Capital Expenditures = Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset

n Acquisitions of other firms, since these are like capital expenditures. The adjusted cap ex will be

Adjusted Net Cap Ex = Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions

Two caveats:

- 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
- 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

## Working Capital Investments

n In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) n A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable) n Any investment in this measure of working capital ties up cash. Therefore, any increases (decreases) in working capital will reduce (increase) cash flows in that period. n When forecasting future growth, it is important to forecast the effects of such growth on working capital needs, and building these effects into the cash flows.

## Estimating FCFF: Telecom Italia

- n EBIT (1997) = 4,313 million n Tax rate used = 49.08% (Assumed Effective = Marginal) n Capital spending (1997) = 7,391 million n Depreciation (1997) = 5,842 million n Non-cash Working capital Change (1997) = 253 million (Normalized) n Estimating FCFF (1998) Current EBIT \* (1 - tax rate) = 739 (1-.3625) = 2,196 million
  - (Capital Spending Depreciation) = 1,549 million
  - Change in Working Capital = 253 million Current FCFF = 394 million

## Estimating FCFF: Compaq

|                                     | Unadjusted  | Adjusted for R&D |
|-------------------------------------|-------------|------------------|
| EBIT (1998) =                       | \$ 858 mil  | \$1,696 mil      |
| EBIT (1-t)                          | \$ 558 mil  | \$1,395 mil      |
| Capital spending (1998) =           | \$1,067 mil | \$ 2,420 mil     |
| Depreciation (1998) =               | \$ 893 mil  | \$ 1,408 mil     |
| Non-cash WC Change (1998) =         | \$ 290 mil  | \$ 290 mil       |
| n Estimating FCFF (1998)            |             |                  |
| Current EBIT * (1 - tax rate) =     |             | \$1,395.34       |
| - (Capital Spending - Depreciation) |             | \$1,011.64       |
| - Change in Working Capital         |             | \$290.00         |
| Current FCFF                        |             | \$93.70          |

## IV. Estimating Growth

n When valuing firms, some people use analyst projections of earnings growth (over the next 5 years) that are widely available in Zacks, I/B/E/S or First Call in the US, and less so overseas. This practice is o Fine. Equity research analysts follow these stocks closely and should be pretty good at estimating growth o Shoddy. Analysts are not that good at projecting growth in earnings in the long term. o Wrong. Analysts do not project growth in operating earnings

## Expected Growth in EBIT and Fundamentals

n Reinvestment Rate and Return on Capital

$$g_{EBIT} = (\text{Net Capital Expenditures} + \text{Change in WC})/\text{EBIT}(1-t) * \text{ROC} = \text{Reinvestment Rate} * \text{ROC}$$

n Proposition: No firm can expect its operating income to grow over time without reinvesting some of the operating income in net capital expenditures and/or working capital. n Proposition: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.

## Expected Growth and Telecom Italia

n Return on Capital = EBIT (1- tax rate) / (BV of Debt + BV of Equity) = 2196/(6,448+15,608) = 9.96% n Reinvestment Rate = (Net Cap Ex + Chg in WC)/EBIT (1-t) = (1549+253)/ 2196= 82.06% n Expected Growth in Operating Income = (.8206) (9.96%) = 8.17%

## Expected Growth and Compaq

n ROC = EBIT (1- tax rate) / (BV of Debt + BV of Equity) = 1395/12,006= 11.62% n Reinv. Rate = (Net Cap Ex + Chg in WC)/EBIT (1-t) = (1012+290)/ 1395 = 93.28% n Expected Growth Rate = (.1162)\*(.9328) = 11.16%

## Not all growth is equal: Disney versus Hansol Paper

#### n Disney

- Reinvestment Rate = 50%
- Return on Capital =18.69%
- Expected Growth in EBIT =.5(18.69%) = 9.35%

#### n Hansol Paper

- Reinvestment Rate = (105,000+1,000)/(109,569\*.7) = 138.20%
- Return on Capital = 6.76%
- Expected Growth in EBIT = 6.76% (1.382) = 9.35%

#### n Both these firms have the same expected growth rate in operating income. Are they equivalent from a valuation standpoint?

#### V. Growth Patterns

- n A key assumption in all discounted cash flow models is the period of high growth, and the pattern of growth during that period. In general, we can make one of three assumptions:
  - there is no high growth, in which case the firm is already in stable growth
  - there will be high growth for a period, at the end of which the growth rate will drop to the stable growth rate (2-stage)
  - there will be high growth for a period, at the end of which the growth rate will decline gradually to a stable growth rate(3-stage)

![](_page_67_Figure_2.jpeg)

#### Determinants of Growth Patterns

#### n Size of the firm

- Success usually makes a firm larger. As firms become larger, it becomes much more difficult for them to maintain high growth rates

#### n Current growth rate

- While past growth is not always a reliable indicator of future growth, there is a correlation between current growth and future growth. Thus, a firm growing at 30% currently probably has higher growth and a longer expected growth period than one growing 10% a year now.

#### n Barriers to entry and differential advantages

- Ultimately, high growth comes from high project returns, which, in turn, comes from barriers to entry and differential advantages.
- The question of how long growth will last and how high it will be can therefore be framed as a question about what the barriers to entry are, how long they will stay up and how strong they will remain.

## Dealing with Cash and Marketable Securities

- n The simplest and most direct way of dealing with cash and marketable securities is to keep it out of the valuation - the cash flows should be before interest income from cash and securities, and the discount rate should not be contaminated by the inclusion of cash. (Use betas of the operating assets alone to estimate the cost of equity). n Once the firm has been valued, add back the value of cash and marketable securities.
  - If you have a particularly incompetent management, with a history of overpaying on acquisitions, markets may discount the value of this cash.

## Dealing with Cross Holdings

n When the holding is a majority, active stake, the value that we obtain from the cash flows includes the share held by outsiders. While their holding is measured in the balance sheet as a minority interest, it is at book value. To get the correct value, we need to subtract out the estimated market value of the minority interests from the firm value. n When the holding is a minority, passive interest, the problem is a different one. The firm shows on its income statement only the share of dividends it receives on the holding. Using only this income will understate the value of the holdings. In fact, we have to value the subsidiary as a separate entity to get a measure of the market value of this holding. n Proposition 1: It is almost impossible to correctly value firms with minority, passive interests in a large number of private subsidiaries.

#### The Choices in DCF Valuation

| <b>Choose a</b>    |                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                         |                                                                                                                                                                 |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cash Flow          | <i>Dividends</i><br>Expected Dividends to Stockholders                                                                                                                                                                                                                             | <i>Cashflows to Equity</i><br><br>Net Income<br>- (1- $\delta$ ) (Capital Exp. - Deprec'n)<br>- (1- $\delta$ ) Change in Work. Capital<br>= Free Cash flow to Equity (FCFE)<br>[ $\delta$ = Debt Ratio] | <i>Cashflows to Firm</i><br><br>EBIT (1- tax rate)<br>- (Capital Exp. - Deprec'n)<br>- Change in Work. Capital<br>= Free Cash flow to Firm (FCFF)               |
| & A Discount Rate  | <i>Cost of Equity</i><br><br>• <i>Basis:</i> The riskier the investment, the greater is the cost of equity.<br><br>• <i>Models:</i><br>CAPM: Riskfree Rate + Beta (Risk Premium)<br>APM: Riskfree Rate + $\Sigma$ Beta <sub>j</sub> (Risk Premium <sub>j</sub> ): <i>n factors</i> |                                                                                                                                                                                                         | <i>Cost of Capital</i><br><br>$WACC = k_e (E/(D+E))$<br><br>$+ k_d (D/(D+E))$<br>$k_d = \text{Current Borrowing Rate (1-t)}$<br>E,D: Mkt Val of Equity and Debt |
| & a growth pattern | <i>Stable Growth</i><br><br>g<br>t                                                                                                                                                                                                                                                 | <i>Two-Stage Growth</i><br><br>g<br>g<br>t                                                                                                                                                              | <i>Three-Stage Growth</i><br><br>g<br>g<br>g<br>t                                                                                                               |

## Variations on DCF Valuation

- n A DCF valuation can be presented in two other formats:
  - In an adjusted present value (APV) valuation, the value of a firm can be broken up into its operating and leverage components separately Firm Value = Value of Unlevered Firm + (PV of Tax Benefits - Exp. Bankruptcy Cost)
- In an excess return model, the value of a firm can be written in terms of the existing capital invested in the firm and the present value of the excess returns that the firm will make on both existing assets and all new investments Firm Value = Capital Invested in Assets in Place + PV of Dollar Excess Returns on Assets in Place + PV of Dollar Excess Returns on All Future Investments n Done right, slicing a DCF valuation and presenting it differently should not change the value of the firm.

## Value Enhancement: Back to Basics

Aswath Damodaran

http://www.stern.nyu.edu/~adamodar

## Price Enhancement versus Value Enhancement

![](_page_74_Figure_1.jpeg)

## The Paths to Value Creation

- n Using the DCF framework, there are four basic ways in which the value of a firm can be enhanced:
  - The cash flows from existing assets to the firm can be increased, by either
    - increasing after-tax earnings from assets in place or
    - reducing reinvestment needs (net capital expenditures or working capital)
  - The expected growth rate in these cash flows can be increased by either
    - Increasing the rate of reinvestment in the firm
    - Improving the return on capital on those reinvestments
  - The length of the high growth period can be extended to allow for more years of high growth.
  - The cost of capital can be reduced by
    - Reducing the operating risk in investments/assets
    - Changing the financial mix
    - Changing the financing composition

#### A Basic Proposition

- n For an action to affect the value of the firm, it has to
  - Affect current cash flows (or)
  - Affect future growth (or)
  - Affect the length of the high growth period (or)
- Affect the discount rate (cost of capital) n **Proposition 1: Actions that do not affect current cash flows, future growth, the length of the high growth period or the discount rate cannot affect value.**

## Value-Neutral Actions

- n Stock splits and stock dividends change the number of units of equity in a firm, but cannot affect firm value since they do not affect cash flows, growth or risk. n Accounting decisions that affect reported earnings but not cash flows should have no effect on value.
  - Changing inventory valuation methods from FIFO to LIFO or vice versa in financial reports but not for tax purposes
  - Changing the depreciation method used in financial reports (but not the tax books) from accelerated to straight line depreciation
  - Major non-cash restructuring charges that reduce reported earnings but are not tax deductible
- Using pooling instead of purchase in acquisitions cannot change the value of a target firm. n Decisions that create new securities on the existing assets of the firm (without altering the financial mix) such as tracking stock cannot create value, though they might affect perceptions and hence the price.

## In-Process R&D

- n In acquisitions of firms with R&D, firms have increasingly taken advantage of a provision that allows them to write off in-process R&D immediately. This reduces the amount that gets charged as goodwill and amortized in future periods; this, in turn, increases reported earnings in future periods. None of this has any tax implications.
  - A study that looked at high-tech firms found that they paid larger premiums for firms when they could qualify for this provision.
- When FASB announced that it was looking at banning this procedure, high-tech firms argued that doing so would make it harder to justify acquisitions. n Does qualifying or not qualifying for this provision affect value?

## Value Creation 1: Increase Cash Flows from Assets in Place

- n The assets in place for a firm reflect investments that have been made historically by the firm. To the extent that these investments were poorly made and/or poorly managed, it is possible that value can be increased by increasing the after-tax cash flows generated by these assets. n The cash flows discounted in valuation are after taxes and reinvestment needs have been met: EBIT ( 1-t)
  - (Capital Expenditures Depreciation)
- Change in Non-cash Working Capital = Free Cash Flow to Firm n Proposition 2: A firm that can increase its current cash flows, without significantly impacting future growth or risk, will increase its value.

#### Ways of Increasing Cash Flows from Assets in Place

![](_page_80_Diagram_1.jpeg)

## Issue: To divest or not to divest

n Assume that you have been called to run Compaq and that its returns on its different businesses are as follows:

| Business  | Capital Invested | ROC  | Cost of Capital |
|-----------|------------------|------|-----------------|
| Mainframe | \$ 3 billion     | 5%   | 10%             |
| PCs       | \$ 2 billion     | 11%  | 11%             |
| Service   | \$ 1.5 billion   | 14%  | 9.5%            |
| Internet  | \$ 1 billion     | 22%* | 14%             |

\* Expected returns; current returns are negative

Which of these businesses should be divested?

## A Divestiture Decision Matrix

n Whether to continue, terminate or divest an investment will depend upon which of the three values - continuing, liquidation or divestiture - is the greatest. n If the continuing value is the greatest, there can be no value created by terminating or liquidating this investment. n If the liquidation or divestiture value is greater than the continuing value, the firm value will increase by the difference between the two values:

If liquidation is optimal: Liquidation Value - Continuing Value

If divestiture is optimal: Divestiture Value - Continuing Value

## Operating Margin for Compaq: A Comparison to the Industry

![](_page_83_Figure_1.jpeg)

## Issue : Operating Margins and R&D

n Assume that analysts focus on the traditional operating margin. Assume that Compaq improves its margin by cutting back on R&D expenses. Is this value creating?

#### The Tax Effect: Telecom Italia

![](_page_85_Figure_1.jpeg)

## The Cash Flow Effects of Working Capital: Telecom Italia

|                     | 1996   | 1997    | Telecoms |
|---------------------|--------|---------|----------|
| Inventory           | 773    | 1092    |          |
| Accounts Receivable | 6193   | 7017    |          |
| Accounts Payable    | 4624   | 5236    |          |
| Non-cash WC         | 2342   | 2873    |          |
| % of Sales          | 11.50% | 12.99%% | 6.75%    |

<sup>n</sup> Expected cash flow with 13% working capital = \$465 million <sup>n</sup> Expected cash flow with 6.75% working capital = \$564 million

## Value Creation 2: Increase Expected Growth

- n Keeping all else constant, increasing the expected growth in earnings will increase the value of a firm. n The expected growth in earnings of any firm is a function of two variables:
  - The amount that the firm reinvests in assets and projects
  - The quality of these investments

#### Value Enhancement through Growth

![](_page_88_Diagram_1.jpeg)

## 2.1: Increase the Reinvestment Rate

- n Holding all else constant, increasing the reinvestment rate will increase the expected growth in earnings of a firm. Increasing the reinvestment rate will, however, reduce the cash flows of the firms. The net effect will determine whether value increases or decreases. n As a general rule,
  - Increasing the reinvestment rate when the ROC is less than the cost of capital will reduce the value of the firm
  - Increasing the reinvestment rate when the ROC is greater than the cost of capital will increase the value of the firm

## Reinvestment and Value Creation at Compaq

n Compaq, in 1998, had a return on capital of 11.62% and a cost of capital of 11.16%. It was reinvesting 93.28% of its earnings back into the firm. Was this reinvestment creating significant value?

#### The Return Effect: Reinvestment Rate

**Compaq: Value/Share and Reinvestment Rate**

![](_page_91_Figure_2.jpeg)

## 2.2: Improve Quality of Investments

- n If a firm can increase its return on capital on new projects, while holding the reinvestment rate constant, it will increase its firm value.
  - The firm's cost of capital still acts as a floor on the return on capital. If the return on capital is lower than the cost of capital, increasing the return on capital will reduce the amount of value destroyed but will not create value. The firm would be better off under those circumstances returning the cash to the owners of the business.
- It is only when the return on capital exceeds the cost of capital, that the increase in value generated by the higher growth will more than offset the decrease in cash flows caused by reinvesting. n This proposition might not hold, however, if the investments are in riskier projects, because the cost of capital will then increase.

## Telecom Italia: Quality of Investments

![](_page_93_Figure_1.jpeg)

## 2.3: The Role of Acquisitions and Divestitures

- n An acquisition is just a large-scale project. All of the rules that apply to individual investments apply to acquisitions, as well. For an acquisition to create value, it has to
  - Generate a higher return on capital, after allowing for synergy and control factors, than the cost of capital.
- Put another way, an acquisition will create value only if the present value of the cash flows on the acquired firm, inclusive of synergy and control benefits, exceeds the cost of the acquisitons n A divestiture is the reverse of an acquisition, with a cash inflow now (from divesting the assets) followed by cash outflows (i.e., cash flows foregone on the divested asset) in the future. If the present value of the future cash outflows is less than the cash inflow today, the divestiture will increase value. n A fair-price acquisition or divestiture is value neutral.

## An Acquisition Choice

n Assume now that Telecom Italia has the opportunity to acquire a internet firm and that you compute the internal rate of return on this firm to 17.50%. TI has a cost of capital of 9.07%, but the cost of capital for firms in the high technology business is 20%. Is this a value enhancing acquisition? n If it does not pass your financial test, can you make the argument that strategic considerations would lead you to override the financials and acquire the firm? n What about synergy?

## A procedure for valuing synergy

- (1) the firms involved in the merger are **valued independently**, by discounting expected cash flows to each firm at the weighted average cost of capital for that firm.
- (2) the **value of the combined firm, with no synergy**, is obtained by adding the values obtained for each firm in the first step.
- (3) The **effects of synergy are built into expected growth rates and cashflows**, and the combined firm is re-valued with synergy.

Value of Synergy = Value of the combined firm, with synergy - Value of the combined firm, without synergy

## Synergy Effects in Valuation Inputs

*If synergy is Valuation Inputs that will be affected are*

Economies of Scale *Operating Margin* of combined firm will be greater than the revenue-weighted operating margin of individual firms.

Growth Synergy More projects:*Higher Reinvestment Rate* (Retention)

Better projects: *Higher Return on Capital* (ROE)

*Longer Growth Period*

Again, these inputs will be estimated for the combined firm.

## Valuing Synergy: Compaq and Digital

n In 1997, Compaq acquired Digital for \$ 30 per share + 0.945 Compaq shares for every Digital share. (\$ 53-60 per share) The acquisition was motivated by the belief that the combined firm would be able to find investment opportunities and compete better than the firms individually could.

## Background Data

| Current EBIT Current Revenues Capital Expenditures - Depreciation | Compaq \$ 2,987 million \$25,484 mil \$ 184 million | Digital: Opt Mgd \$ 522 million \$13,046 mil \$ 14 (offset) |
|-------------------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------|
| Expected growth rate -next 5 years                                | 10%                                                 | 10%                                                         |
| Expected growth rate after year 5                                 | 5%                                                  | 5%                                                          |
| Debt /(Debt + Equity)                                             | 10%                                                 | 20%                                                         |
| After-tax cost of debt                                            | 5%                                                  | 5.25%                                                       |
| Beta for equity - next 5 years                                    | 1.25                                                | 1.25                                                        |
| Beta for equity - after year 5                                    | 1.00                                                | 1.0                                                         |
| Working Capital/Revenues                                          | 15%                                                 | 15%                                                         |

## Digital Valuation: Optimally Managed

| Year | FCFF     | Terminal Value | PV         |
|------|----------|----------------|------------|
| 1    | \$156.29 |                | \$140.36   |
| 2    | \$171.91 |                | \$138.65   |
| 3    | \$189.11 |                | \$136.97   |
| 4    | \$208.02 |                | \$135.31   |
| 5    | \$228.82 | \$6,584.62     | \$3,980.29 |

Terminal Year \$329.23

Value of the Firm: with Control Change = **\$ 4,531 million**

## Valuing Compaq

| Year          | FCFF       | Terminal Value | PV          |
|---------------|------------|----------------|-------------|
| 1             | \$1,518.19 |                | \$1,354.47  |
| 2             | \$1,670.01 |                | \$1,329.24  |
| 3             | \$1,837.01 |                | \$1,304.49  |
| 4             | \$2,020.71 |                | \$1,280.19  |
| 5             | \$2,222.78 | \$56,654.81    | \$33,278.53 |
| Terminal Year | \$2,832.74 |                | \$38,546.91 |

n Value of Compaq = \$ 38,547 million n After year 5, capital expenditures will be 110% of depreciation.

## Combined Firm Valuation

- n The Combined firm will have some economies of scale, allowing it to increase its current after-tax operating margin slightly. The dollar savings will be approximately \$ 100 million.
  - Current Operating Margin = (2987+522)/(25484+13046) = 9.11%
- New Operating Margin = (2987+522+100)/(25484+13046) = 9.36% n The combined firm will also have a slightly higher growth rate of 10.50% over the next 5 years, because of operating synergies. n The beta of the combined firm is computed in two steps:
  - Digital's Unlevered Beta = 1.07; Compaq's Unlevered Beta=1.17
  - Digital's Firm Value = 4.5; Compaq's Firm Value = 38.6
  - Unlevered Beta = 1.07 \* (4.5/43.1) + 1.17 (38.6/43.1) = 1.16
  - Combined Firm's Debt/Equity Ratio = 13.64%
  - New Levered Beta = 1.16 (1+(1-0.36)(.1364)) = 1.26
  - Cost of Capital = 12.93% (.88) + 5% (.12) = 11.98%

## Combined Firm Valuation

| Year          | FCFF                   | Terminal Value PV       |
|---------------|------------------------|-------------------------|
| 1             | \$1,726.65             | \$1,541.95              |
| 2             | \$1,907.95             | \$1,521.59              |
| 3             | \$2,108.28             | \$1,501.50              |
| 4             | \$2,329.65             | \$1,481.68              |
| 5             | \$2,574.26             | \$66,907.52 \$39,463.87 |
| Terminal Year | \$3,345.38             |                         |
|               | Value of Combined Firm | = \$ 45,511             |

## The Value of Synergy

n Value of Combined Firm with Synergy = \$45,511 million n Value of Compaq + Value of Digital = 38,547 + 4532 = \$ 44,079 million n Total Value of Synergy = \$ 1,432 million

## Value Creation 3: Increase Length of High Growth Period

n Every firm, at some point in the future, will become a stable growth firm, growing at a rate equal to or less than the economy in which it operates. n The high growth period refers to the period over which a firm is able to sustain a growth rate greater than this "stable" growth rate. n If a firm is able to increase the length of its high growth period, other things remaining equal, it will increase value. n The length of the high growth period is a direct function of the competitive advantages that a firm brings into the process. Creating new competitive advantage or augmenting existing ones can create value.

## 3.1: The Brand Name Advantage

n Some firms are able to sustain above-normal returns and growth because they have well-recognized brand names that allow them to charge higher prices than their competitors and/or sell more than their competitors. n Firms that are able to improve their brand name value over time can increase both their growth rate and the period over which they can expect to grow at rates above the stable growth rate, thus increasing value.

#### Illustration: Valuing a brand name: Coca Cola

|                     | Coca Cola       | Generic Cola Company |
|---------------------|-----------------|----------------------|
| AT Operating Margin | 18.56%          | 7.50%                |
| Sales/BV of Capital | 1.67            | 1.67                 |
| ROC                 | 31.02%          | 12.53%               |
| Reinvestment Rate   | 65.00% (19.35%) | 65.00% (47.90%)      |
| Expected Growth     | 20.16%          | 8.15%                |
| Length              | 10 years        | 10 yea               |
| Cost of Equity      | 12.33%          | 12.33%               |
| E/(D+E)             | 97.65%          | 97.65%               |
| AT Cost of Debt     | 4.16%           | 4.16%                |
| D/(D+E)             | 2.35%           | 2.35%                |
| Cost of Capital     | 12.13%          | 12.13%               |
| Value               | \$115           | \$13                 |

## 3.2: Patents and Legal Protection

n The most complete protection that a firm can have from competitive pressure is to own a patent, copyright or some other kind of legal protection allowing it to be the sole producer for an extended period. n Note that patents only provide partial protection, since they cannot protect a firm against a competitive product that meets the same need but is not covered by the patent protection. n Licenses and government-sanctioned monopolies also provide protection against competition. They may, however, come with restrictions on excess returns; utilities in the United States, for instance, are monopolies but are regulated when it comes to price increases and returns.

## 3.3: Switching Costs

n Another potential barrier to entry is the cost associated with switching from one firm's products to another. n The greater the switching costs, the more difficult it is for competitors to come in and compete away excess returns. n Firms that devise ways to increase the cost of switching from their products to competitors' products, while reducing the costs of switching from competitor products to their own will be able to increase their expected length of growth.

## 3.4: Cost Advantages

- n There are a number of ways in which firms can establish a cost advantage over their competitors, and use this cost advantage as a barrier to entry:
  - In businesses, where scale can be used to reduce costs, economies of scale can give bigger firms advantages over smaller firms
  - Owning or having exclusive rights to a distribution system can provide firms with a cost advantage over its competitors.
- Owning or having the rights to extract a natural resource which is in restricted supply (The undeveloped reserves of an oil or mining company, for instance) n These cost advantages will show up in valuation in one of two ways:
  - The firm may charge the same price as its competitors, but have a much higher operating margin.
  - The firm may charge lower prices than its competitors and have a much higher capital turnover ratio.

## Gauging Barriers to Entry

n Which of the following barriers to entry are most likely to work for Telecom Italia? p Brand Name p Patents and Legal Protection p Switching Costs p Cost Advantages n What about for Compaq? p Brand Name p Patents and Legal Protection p Switching Costs p Cost Advantages

## Value Creation 4: Reduce Cost of Capital

n The cost of capital for a firm can be written as:

Cost of Capital = 
$$k_e (E/(D+E)) + k_d (D/(D+E))$$

Where,

 ke = Cost of Equity for the firm

 kd = Borrowing rate (1 - tax rate)

n The cost of equity reflects the rate of return that equity investors in the firm would demand to compensate for risk, while the borrowing rate reflects the current long-term rate at which the firm can borrow, given current interest rates and its own default risk. n The cash flows generated over time are discounted back to the present at the cost of capital. Holding the cash flows constant, reducing the cost of capital will increase the value of the firm.

## Estimating Cost of Capital: Telecom Italia

#### n Equity

- Cost of Equity = 4.24% + 0.87 (5.53%) = 9.05%
- Market Value of Equity = 9.92 E/share\* 5255.13 = 52,110 Mil (84.16%)

#### n Debt

- Cost of debt = 4.24% + 0.2% (default spread) = 4.44%
- Market Value of Debt = 9,809 Mil (15.84%)

#### n Cost of Capital

Cost of Capital = 10.36 % (.8416) + 4.44% (1- .4908) (.1584)) = 9.05% (.8416) + 2.26% (.1584) = 7.98%

#### Estimating Cost of Capital: Compaq

#### n Equity

- Cost of Equity = 6% + 1.29 (4%) = 11.16%
- Market Value of Equity = 23.38\*1691 = \$ 39.5 billion

#### n Debt

- Cost of debt = 6% + 1% (default spread) = 7%
- Market Value of Debt = 0

#### n Cost of Capital

Cost of Capital = 11.16 % (1.00) + 7% (1- .35) (0.00)) = 11.16%

#### Reducing Cost of Capital

![](_page_115_Diagram_1.jpeg)

## Telecom Italia: Optimal Debt Ratio

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC   | Firm Value (G) |
|------------|------|----------------|-------------|-----------------------|----------|--------------------------|--------|----------------|
| 0%         | 0.79 | 8.63%          | AAA         | 4.54%                 | 49.08%   | 2.31%                    | 8.63%  | \$45,598       |
| 10%        | 0.84 | 8.88%          | AAA         | 4.54%                 | 49.08%   | 2.31%                    | 8.22%  | \$54,659       |
| 20%        | 0.89 | 9.19%          | A+          | 5.24%                 | 49.08%   | 2.67%                    | 7.89%  | \$65,095       |
| 30%        | 0.97 | 9.59%          | A-          | 5.74%                 | 49.08%   | 2.92%                    | 7.59%  | \$77,927       |
| 40%        | 1.06 | 10.12%         | BB          | 6.74%                 | 49.08%   | 3.43%                    | 7.45%  | \$86,035       |
| 50%        | 1.20 | 10.87%         | B-          | 9.24%                 | 49.08%   | 4.71%                    | 7.79%  | \$68,933       |
| 60%        | 1.40 | 11.98%         | CCC         | 10.24%                | 49.08%   | 5.21%                    | 7.92%  | \$63,772       |
| 70%        | 1.87 | 14.60%         | CC          | 11.74%                | 41.76%   | 6.84%                    | 9.17%  | \$37,267       |
| 80%        | 2.94 | 20.50%         | C           | 13.24%                | 32.40%   | 8.95%                    | 11.26% | \$20,942       |
| 90%        | 5.88 | 36.76%         | C           | 13.24%                | 28.80%   | 9.43%                    | 12.16% | \$17,340       |

## Compaq: Optimal Capital Structure

| Debt Ratio | Beta  | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC   | Firm Value (G) |
|------------|-------|----------------|-------------|-----------------------|----------|--------------------------|--------|----------------|
| 0%         | 1.29  | 11.16%         | AAA         | 6.30%                 | 35.00%   | 4.10%                    | 11.16% | \$38,893       |
| 10%        | 1.38  | 11.53%         | AA          | 6.70%                 | 35.00%   | 4.36%                    | 10.81% | \$41,848       |
| 20%        | 1.50  | 12.00%         | BBB         | 8.00%                 | 35.00%   | 5.20%                    | 10.64% | \$43,525       |
| 30%        | 1.65  | 12.60%         | B-          | 11.00%                | 35.00%   | 7.15%                    | 10.96% | \$40,528       |
| 40%        | 1.85  | 13.40%         | CCC         | 12.00%                | 35.00%   | 7.80%                    | 11.16% | \$38,912       |
| 50%        | 2.28  | 15.12%         | C           | 15.00%                | 23.18%   | 11.52%                   | 13.32% | \$26,715       |
| 60%        | 2.85  | 17.40%         | C           | 15.00%                | 19.32%   | 12.10%                   | 14.22% | \$23,535       |
| 70%        | 3.80  | 21.21%         | C           | 15.00%                | 16.56%   | 12.52%                   | 15.12% | \$20,984       |
| 80%        | 5.70  | 28.81%         | C           | 15.00%                | 14.49%   | 12.83%                   | 16.02% | \$18,890       |
| 90%        | 11.40 | 51.62%         | C           | 15.00%                | 12.88%   | 13.07%                   | 16.92% | \$17,141       |

## Changing Financing Type

- n The fundamental principle in designing the financing of a firm is to ensure that the cash flows on the debt should match as closely as possible the cash flows on the asset. n By matching cash flows on debt to cash flows on the asset, a firm reduces its risk of default and increases its capacity to carry debt, which, in turn, reduces its cost of capital, and increases value. n Firms which mismatch cash flows on debt and cash flows on assets by using
  - Short term debt to finance long term assets
  - Dollar debt to finance non-dollar assets
  - Floating rate debt to finance assetswhose cash flows are negatively or not affected by invlaiton will end up with higher default risk, higher costs of capital and lower firm value.

## Financing Details

n What would the cash flows on a project for Telecom Italia look like in terms of o Project life?: o Cash Flow Patterns?: o Growth?: o Currency?: n Now what kind of debt would be best to finance such a project? n If I told you that Telecom Italia has only short to medium term Lira debt on its books, what action could you take to enhance value?

|                                     |  | <i>Gimme'</i>                                                                                                                                                                                                              | <i>Odds on.</i>                                                                                                                                                                                                                            | <i>Could work if..</i>                                                                                       |
|-------------------------------------|--|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <i>Assets in Place</i>              |  | 1. Divest assets/projects with Divestiture Value > Continuing Value<br>2. Terminate projects with Liquidation Value > Continuing Value<br>3. Eliminate operating expenses that generate no current revenues and no growth. | 1. Reduce net working capital requirements, by reducing inventory and accounts receivable, or by increasing accounts payable.<br>2. Reduce capital maintenance expenditures on assets in place.                                            | 1. Change pricing strategy to maximize the product of profit margins and turnover ratio.                     |
|                                     |  |                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |                                                                                                              |
|                                     |  |                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |                                                                                                              |
|                                     |  |                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |                                                                                                              |
| <i>Expected Growth</i>              |  | Eliminate new capital expenditures that are expected to earn less than the cost of capital                                                                                                                                 | Increase reinvestment rate or marginal return on capital or both in firm's existing businesses.                                                                                                                                            | Increase reinvestment rate or marginal return on capital or both in new businesses.                          |
|                                     |  | If any of the firm's products or services can be patented and protected, do so                                                                                                                                             | Use economies of scale or cost advantages to create higher return on capital.                                                                                                                                                              | 1. Build up brand name<br>2. Increase the cost of switching from product and reduce cost of switching to it. |
| <i>Length of High Growth Period</i> |  | 1. Use swaps and derivatives to match debt more closely to firm's assets<br>2. Recapitalize to move the firm towards its optimal debt ratio.                                                                               | 1. Change financing type and use innovative securities to reflect the types of assets being financed<br>2. Use the optimal financing mix to finance new investments.<br>3. Make cost structure more flexible to reduce operating leverage. | Reduce the operating risk of the firm, by making products less discretionary to customers.                   |
|                                     |  |                                                                                                                                                                                                                            |                                                                                                                                                                                                                                            |                                                                                                              |

Aswath Damodaran121

#### **The Value Enhancement Chain**

![](_page_121_Diagram_1.jpeg)

![](_page_121_Diagram_3.jpeg)

*Discount at* Cost of Capital (WACC) = 10.1% (0.60) + 3.43% (0.40) = 7.43%

#### Telecom Italia: Restructured(in Euros)

**Current Cashflow to Firm** EBIT(1-t) : 1,395 - Nt CpX 1012 - Chg WC 290 = FCFF 94 Reinvestment Rate =93.28%

**Expected Growth in EBIT (1-t)** .9328\*1976-= .1843 **18.43%**

Stable Growth g = 5%; Beta = 1.00; ROC=19.76% Reinvestment Rate= 25.30%

Terminal Value 5= 5942/(.0904-.05) = 147,070

**Cost of Equity 12.00%**

**Cost of Debt** (6%+ 2%)(1-.35) = 5.20%

**Weights** E = 80% D = 20%

*Discount at* Cost of Capital (WACC) = 12.50% (0.80) + 5.20% (0.20) = 10.64%

Firm Value: 54895 + Cash: 4091 - Debt: 0 =Equity 58448 -Options 538 Value/Share \$34.56

> **Riskfree Rate**: Government Bond Rate = 6%

+ **Beta**  1.50 **X** Unlevered Beta for Sectors: 1.29 Firm's D/E Ratio: 0.00%

**Risk Premium** 4.00%

> Mature risk premium 4%

Country Risk Premium 0.00%

#### Compaq: Restructured

Reinvestment Rate 93.28% (1998)

Return on Capital 19.76%

EBIT(1-t) - Reinv FCFF \$1,653 \$1,957 \$2,318 \$2,745 \$3,251 \$3,851 \$4,560 \$5,401 \$6,397 \$7,576 \$1,542 \$1,826 \$2,162 \$2,561 \$3,033 \$3,592 \$4,254 \$5,038 \$5,967 \$7,067 \$111 \$131 \$156 \$184 \$218 \$259 \$306 \$363 \$429 \$509

## Relative Valuation

Aswath Damodaran

#### Why relative valuation?

"If you think I'm crazy, you should see the guy who lives across the hall" *Jerry Seinfeld talking about Kramer in a Seinfeld episode*

" A little inaccuracy sometimes saves tons of explanation"

H.H. Munro

#### Relative Valuation

- n **What is it?**: The value of any asset can be estimated by looking at how the market prices "similar" or 'comparable" assets. n **Philosophical Basis**: The intrinsic value of an asset is impossible (or close to impossible) to estimate. The value of an asset is whatever the market is willing to pay for it (based upon its characteristics) n **Information Needed**: To do a relative valuation, you need
  - an identical asset, or a group of comparable or similar assets
  - a standardized measure of value (in equity, this is obtained by dividing the price by a common variable, such as earnings or book value)
- and if the assets are not perfectly comparable, variables to control for the differences n **Market Inefficiency**: Pricing errors made across similar or comparable assets are easier to spot, easier to exploit and are much more quickly corrected.

#### Advantages of Relative Valuation

- n Relative valuation is much more likely to reflect market perceptions and moods than discounted cash flow valuation. This can be an advantage when it is important that the price reflect these perceptions as is the case when
  - the objective is to sell a security at that price today (as in the case of an IPO)
- investing on "momentum" based strategies n With relative valuation, there will always be a significant proportion of securities that are under valued and over valued. n Since portfolio managers are judged based upon how they perform on a relative basis (to the market and other money managers), relative valuation is more tailored to their needs n Relative valuation generally requires less information than discounted cash flow valuation (especially when multiples are used as screens)

#### Standardizing Value

- n Prices can be standardized using a common variable such as earnings, cashflows, book value or revenues.
  - Earnings Multiples
    - Price/Earnings Ratio (PE) and variants (PEG and Relative PE)
    - Value/EBIT
    - Value/EBITDA
    - Value/Cash Flow
  - Book Value Multiples
    - Price/Book Value(of Equity) (PBV)
    - Value/ Book Value of Assets
    - Value/Replacement Cost (Tobin's Q)
  - Revenues
    - Price/Sales per Share (PS)
    - Value/Sales
  - Industry Specific Variable (Price/kwh, Price per ton of steel ....)

#### The Four Steps to Understanding Multiples

#### n Define the multiple

- In use, the same multiple can be defined in different ways by different users. When comparing and using multiples, estimated by someone else, it is critical that we understand how the multiples have been estimated

#### n Describe the multiple

- Too many people who use a multiple have no idea what its cross sectional distribution is. If you do not know what the cross sectional distribution of a multiple is, it is difficult to look at a number and pass judgment on whether it is too high or low.

#### n Analyze the multiple

- It is critical that we understand the fundamentals that drive each multiple, and the nature of the relationship between the multiple and each variable.

#### n Apply the multiple

- Defining the comparable universe and controlling for differences is far more difficult in practice than it is in theory.

#### Definitional Tests

- n Is the multiple consistently defined?
- **Proposition 1: Both the value (the numerator) and the standardizing variable ( the denominator) should be to the same claimholders in the firm. In other words, the value of equity should be divided by equity earnings or equity book value, and firm value should be divided by firm earnings or book value.** n Is the multiple uniformally estimated?
  - The variables used in defining the multiple should be estimated uniformly across assets in the "comparable firm" list.
  - If earnings-based multiples are used, the accounting rules to measure earnings should be applied consistently across assets. The same rule applies with book-value based multiples.

#### Descriptive Tests

- n What is the average and standard deviation for this multiple, across the universe (market)? n What is the median for this multiple?
- The median for this multiple is often a more reliable comparison point. n How large are the outliers to the distribution, and how do we deal with the outliers?
- Throwing out the outliers may seem like an obvious solution, but if the outliers all lie on one side of the distribution (they usually are large positive numbers), this can lead to a biased estimate. n Are there cases where the multiple cannot be estimated? Will ignoring these cases lead to a biased estimate of the multiple? n How has this multiple changed over time?

#### Analytical Tests

- n What are the fundamentals that determine and drive these multiples?
  - Proposition 2: Embedded in every multiple are all of the variables that drive every discounted cash flow valuation - growth, risk and cash flow patterns.
- In fact, using a simple discounted cash flow model and basic algebra should yield the fundamentals that drive a multiple n How do changes in these fundamentals change the multiple?
  - The relationship between a fundamental (like growth) and a multiple (such as PE) is seldom linear. For example, if firm A has twice the growth rate of firm B, it will generally not trade at twice its PE ratio
  - **Proposition 3: It is impossible to properly compare firms on a multiple, if we do not know the nature of the relationship between fundamentals and the multiple.**

#### Application Tests

- n Given the firm that we are valuing, what is a "comparable" firm?
  - While traditional analysis is built on the premise that firms in the same sector are comparable firms, valuation theory would suggest that a comparable firm is one which is similar to the one being analyzed in terms of fundamentals.
- **Proposition 4: There is no reason why a firm cannot be compared with another firm in a very different business, if the two firms have the same risk, growth and cash flow characteristics.** n Given the comparable firms, how do we adjust for differences across firms on the fundamentals?
  - **Proposition 5: It is impossible to find an exactly identical firm to the one you are valuing.**

#### Price Earnings Ratio: Definition

#### **PE = Market Price per Share / Earnings per Share**

n There are a number of variants on the basic PE ratio in use. They are based upon how the price and the earnings are defined. n Price: is usually the current price is sometimes the average price for the year n EPS: earnings per share in most recent financial year earnings per share in trailing 12 months (Trailing PE) forecaster earnings per share next year (Forward PE) forecaster earnings per share in future year

## PE Ratio: Descriptive Statistics

**PE Ratios: Italy - December 1999**

![](_page_134_Figure_2.jpeg)

#### PE Ratio: Understanding the Fundamentals

n To understand the fundamentals, start with a basic equity discounted cash flow model. n With the dividend discount model,

n Dividing both sides by the earnings per share,

n If this had been a FCFE Model,

$$P_0 = \frac{DPS_1}{r - g_n}$$

$$\frac{P_0}{EPS_0} = PE = \frac{\text{Payout Ratio} * (1 + g_n)}{r - g_n}$$

$$P_0 = \frac{\text{FCFE}_1}{r - g_n}$$

$$\frac{P_0}{\text{EPS}_0} = PE = \frac{(\text{FCF/Earnings}) * (1 + g_n)}{r - g_n}$$

#### PE Ratio and Fundamentals

n **Proposition: Other things held equal, higher growth firms will have higher PE ratios than lower growth firms.** n **Proposition: Other things held equal, higher risk firms will have lower PE ratios than lower risk firms** n **Proposition: Other things held equal, firms with lower reinvestment needs will have higher PE ratios than firms with higher reinvestment rates.** n Of course, other things are difficult to hold equal since high growth firms, tend to have risk and high reinvestment rats.

## Using the Fundamental Model to Estimate PE For a High Growth Firm

n The price-earnings ratio for a high growth firm can also be related to fundamentals. In the special case of the two-stage dividend discount model, this relationship can be made explicit fairly simply:

- For a firm that does not pay what it can afford to in dividends, substitute FCFE/Earnings for the payout ratio.

n Dividing both sides by the earnings per share:

$$P_0 = \frac{\text{EPS}_0 * \text{Payout Ratio} * (\mathbf{g}) * \left(1 - \frac{(1+\mathbf{g})^n}{(1+\mathbf{r})^n}\right)}{\mathbf{r} - \mathbf{g}} + \frac{\text{EPS}_0 * \text{Payout Ratio} * (1+\mathbf{g})^n * (1+\mathbf{g}_n)}{(\mathbf{r} - \mathbf{g}_n)(1+\mathbf{r})^n}$$

$$\frac{P_0}{\text{EPS}_0} = \frac{\text{Payout Ratio} * (1 + g) * \left(1 - \frac{(1 + g)^n}{(1 + r)^n}\right)}{r - g} + \frac{\text{Payout Ratio}_n * (1 + g) * (1 + g_n)}{(r - g_n)(1 + r)^n}$$

#### Expanding the Model

n In this model, the PE ratio for a high growth firm is a function of growth, risk and payout, exactly the same variables that it was a function of for the stable growth firm. n The only difference is that these inputs have to be estimated for two phases the high growth phase and the stable growth phase. n Expanding to more than two phases, say the three stage model, will mean that risk, growth and cash flow patterns in each stage.

# A Simple Example

- ■ Assume that you have been asked to estimate the PE ratio for a firm which has the following characteristics:

| Variable             | High Growth Phase | Stable Growth Phase |
|----------------------|-------------------|---------------------|
| Expected Growth Rate | 25%               | 8%                  |
| Payout Ratio         | 20%               | 50%                 |
| Beta                 | 1.00              | 1.00                |

- ■ Riskfree rate = T.Bond Rate = 6%

- ■ Required rate of return =  $6\% + 1(5.5\%) = 11.5\%$

$$PE = \frac{0.2 * (1.25) * \left(1 - \frac{(1.25)^5}{(1.115)^5}\right)}{(.115 - .25)} + \frac{0.5 * (1.25)^5 * (1.08)}{(.115 - .08)(1.115)^5} = 28.75$$

#### PE and Growth: Firm grows at x% for 5 years, 8% thereafter

**PE Ratios and Expected Growth: Interest Rate Scenarios**

![](_page_140_Figure_2.jpeg)

## PE Ratios and Length of High Growth: 25% growth for n years; 8% thereafter

**PE Ratios and Length of High Growth Period**

![](_page_141_Figure_2.jpeg)

## PE and Risk: Effects of Changing Betas on PE Ratio:

Firm with x% growth for 5 years; 8% thereafter

**PE Ratios and Beta: Growth Scenarios**

![](_page_142_Figure_3.jpeg)

## PE and Payout

**PE Ratios and Payour Ratios: Growth Scenarios**

![](_page_143_Figure_2.jpeg)

## Comparisons of PE across time

**PE Ratio for US stocks over time**

![](_page_144_Figure_2.jpeg)

#### Is low (high) PE cheap (expensive)?

n A market strategist argues that stocks are over priced because the PE ratio today is too high relative to the average PE ratio across time. Do you agree? n Yes n No n If you do not agree, what factors might explain the higer PE ratio today?

#### Comparing PE ratios across firms

| Firm                                             | PE     | Expected Growth Rate |
|--------------------------------------------------|--------|----------------------|
| Korea Telecom ADR                                | 214.92 | 52.00%               |
| Cable & Wireless Comms PLC ADR                   | 76.79  | 16.00%               |
| Nippon Telegraph & Telephone ADR                 | 65.74  | 23.00%               |
| Deutsche Telekom AG ADR                          | 62.64  | 15.00%               |
| France Telecom SA ADR                            | 46.57  | 17.00%               |
| Telefonica SA ADR                                | 46.46  | 15.00%               |
| Telecom Italia SPA ADR                           | 36.33  | 17.00%               |
| Telstra ADR                                      | 35.03  | 10.00%               |
| Royal KPN NV ADR                                 | 34.73  | 8.00%                |
| Telekomunikasi Indonesia ADR                     | 33.62  | 21.00%               |
| British Telecommunications PLC ADR               | 26.85  | 12.00%               |
| Tele Danmark AS ADR                              | 23.13  | 19.00%               |
| Matav RT ADR                                     | 22.92  | 25.00%               |
| Hongkong Telecommunications ADR                  | 21.39  | 3.00%                |
| Cable & Wireless PLC ADR                         | 21.31  | 13.00%               |
| Telefonos de Mexico ADR L                        | 21.09  | 12.00%               |
| Asia Satellite Telecom Holdings ADR              | 18.91  | 29.00%               |
| Portugal Telecom SA ADR                          | 18.60  | 15.00%               |
| Telecom Corporation of New Zealand ADR           | 16.85  | 9.00%                |
| Telecomunicaciones de Chile ADR                  | 15.49  | 11.00%               |
| Telecom Argentina Stet - France Telecom SA ADR B | 15.46  | 10.00%               |
| Hellenic Telecommunication Organization SA ADR   | 15.20  | 14.00%               |
| APT Satellite Holdings ADR                       | 14.93  | 40.00%               |
| BCE                                              | 14.31  | 12.00%               |
| Telefonica del Peru ADR B                        | 13.02  | 11.00%               |
| Compania Anonima Telefonos ADR D                 | 12.98  | 44.00%               |
| Telefonica de Argentina ADR                      | 12.14  | 6.00%                |
| PT Indosat ADR                                   | 12.06  | 11.00%               |
| Empresas Telex-Chile ADR                         | NMF    | 30.00%               |
| GST Telecommunications                           | NMF    | 35.00%               |
| RSL Communications A                             | NMF    | 35.00%               |
| Bell Canada International                        | NMF    | 30.00%               |
| Equant NV                                        | NMF    | 45.00%               |
| Globalstar Telecommunications, Ltd.              | NMF    | 33.00%               |
| Global Crossing                                  | NMF    | 38.00%               |
| Average                                          | 34.62  | 17.50%               |

#### A Question

You are reading an equity research report on Telecom Argentina and the analyst claims that the stock is under valued because it has a PE ratio of 12.14 which is much lower than the average for the sector., which is 34.62. Would you agree?

o Yes o No n Why or why not?

#### Using the entire cross section: A regression approach

n In contrast to the 'comparable firm' approach, the information in the entire cross-section of firms can be used to predict PE ratios. n The simplest way of summarizing this information is with a multiple regression, with the PE ratio as the dependent variable, and proxies for risk, growth and payout forming the independent variables.

#### PE versus Growth: June 1999

![](_page_149_Figure_1.jpeg)

#### PE Ratio: Standard Regression

Equation Number 1 Dependent Variable.. PE

Variable(s) Entered on Step Number

 1.. EXPGR 2.. PAYOUT2 3.. BETA5 Beta 5-Year

Multiple R .52862 R Square .27944 Adjusted R Square .27777 Standard Error 15.97326

Analysis of Variance

 DF Sum of Squares Mean Square Regression 3 128138.03381 42712.67794 Residual 1295 330412.95962 255.14514

F = 167.40541 Signif F = .0000

------------------ Variables in the Equation ------------------

Variable B SE B Beta T Sig T

BETA5 5.522673 1.011961 .134573 5.457 .0000 PAYOUT2 .474274 .082299 .135937 5.763 .0000 EXPGR 105.734255 5.730225 .455002 18.452 .0000 (Constant) 5.079579 1.107271 4.587 .0000

#### PE Regression: June 1999 - No Intercept

Equation Number 1 Dependent Variable.. PE

Variable(s) Entered on Step Number

 1.. EXPGR 2.. PAYOUT2 3.. BETA5 Beta 5-Year

Multiple R .85525 R Square .73145 Adjusted R Square .73083 Standard Error 16.09632

Analysis of Variance

| <b>Regression on</b> | <b>DF</b> | <b>Sum of Squares</b> | <b>Mean Square</b> |
|----------------------|-----------|-----------------------|--------------------|
| Regression on        | 3         | 914568. 21119         | 304856. 07040      |
| Residual             | 1296      | 335782. 47081         | 259. 09141         |

F = 1176.63518 Signif F = .0000

------------------ Variables in the Equation ------------------

| Variable |            | B        | SE B    | Beta T Sig T |
|----------|------------|----------|---------|--------------|
| BETA5    | 8.399842   | .800292  | .274037 | 10.496 .0000 |
| PAYOUT2  | .487946    | .082879  | .085021 | 5.887 .0000  |
| EXPGR    | 117.938784 | 5.114306 | .602071 | 23.061 .0000 |

#### Problems with the regression methodology

n The basis regression assumes a linear relationship between PE ratios and the financial proxies, and that might not be appropriate. n The basic relationship between PE ratios and financial variables itself might not be stable, and if it shifts from year to year, the predictions from the model may not be reliable. n The independent variables are correlated with each other. For example, high growth firms tend to have high risk. This multi-collinearity makes the coefficients of the regressions unreliable and may explain the large changes in these coefficients from period to period.

## The Multicollinearity Problem

|         | BETA5  | PROJGR  | PAYOUT2 | PE     |
|---------|--------|---------|---------|--------|
| BETA5   | 1.0000 | .2915** | -.0111  | .2272  |
| PROJGR  | .2915  | 1.0000  | -.0030  | .5053  |
| PAYOUT2 | -.0111 | -.0030  | 1.0000  | .1088  |
| PE      | .2272  | .5053   | .1088   | 1.0000 |

n The independent variables are correlated with the dependent variable, which is a good thing, but they are also correlated with each other (which is not a good thing) n This will cause the standard errors on the coefficients to become larger and some coefficients may have the wrong sign.

## Using the PE ratio regression

n Assume that you were given the following information for Dell. The firm has an expected growth rate of 40%, a beta of 1.40 and pays no dividends. Based upon the regression, estimate the predicted PE ratio for Dell. n Dell is actually trading at 37 times earnings. What does the predicted PE tell you?

# Value of Firm/FCFF: Determinants

- ■ Reverting back to a two-stage FCFF DCF model, we get:

$$V_0 = \frac{\text{FCFF}_0 (1+g) \left(1 - \frac{(1+g)^n}{(1+\text{WACC})^n}\right)}{\text{WACC} - g} + \frac{\text{FCFF}_0 (1+g)^n (1+g_n)}{(\text{WACC} - g_n)(1 + \text{WACC})^n}$$

- •  $V_0$  = Value of the firm (today)
- •  $\text{FCFF}_0$  = Free Cashflow to the firm in current year
- •  $g$  = Expected growth rate in FCFF in extraordinary growth period (first  $n$  years)
- •  $\text{WACC}$  = Weighted average cost of capital
- •  $g_n$  = Expected growth rate in FCFF in stable growth period (after  $n$  years)

# Value Multiples

- ■ Dividing both sides by the FCFF yields,

$$\frac{V_0}{FCFF_0} = \frac{(1+g) \left( 1 - \frac{(1+g)^n}{(1+WACC)^n} \right)}{WACC - g} + \frac{(1+g)^n (1+g_n)}{(WACC - g_n)(1+WACC)^n}$$

- ■ The value/FCFF multiples is a function of
  - • the cost of capital
  - • the expected growth

#### Alternatives to FCFF - EBIT and EBITDA

- n Most analysts find FCFF to complex or messy to use in multiples (partly because capital expenditures and working capital have to be estimated). They use modified versions of the multiple with the following alternative denominator:
  - after-tax operating income or EBIT(1-t)
  - pre-tax operating income or EBIT
  - net operating income (NOI), a slightly modified version of operating income, where any non-operating expenses and income is removed from the EBIT
  - EBITDA, which is earnings before interest, taxes, depreciation and amortization.

#### Value/FCFF Multiples and the Alternatives

n Assume that you have computed the value of a firm, using discounted cash flow models. Rank the following multiples in the order of magnitude from lowest to highest? o Value/EBIT o Value/EBIT(1-t) o Value/FCFF o Value/EBITDA n What assumption(s) would you need to make for the Value/EBIT(1-t) ratio to be equal to the Value/FCFF multiple?

## Illustration: Using Value/FCFF Approaches to value a firm: MCI Communications

- ■ MCI Communications had earnings before interest and taxes of \$3356 million in 1994 (Its net income after taxes was \$855 million).
- ■ It had capital expenditures of \$2500 million in 1994 and depreciation of \$1100 million; Working capital increased by \$250 million.
- ■ It expects free cashflows to the firm to grow 15% a year for the next five years and 5% a year after that.
- ■ The cost of capital is 10.50% for the next five years and 10% after that.
- ■ The company faces a tax rate of 36%.

$$\frac{V_0}{FCFF_0} = \frac{(1.15) \left( 1 - \frac{(1.15)^5}{(1.105)5} \right)}{.105 - .15} + \frac{(1.15)^5(1.05)}{(.10 - .05)(1.105)^5} = 31.28$$

#### Multiple Magic

n In this case of MCI there is a big difference between the FCFF and short cut measures. For instance the following table illustrates the appropriate multiple using short cut measures, and the amount you would overpay by if you used the FCFF multiple.

Free Cash Flow to the Firm

= EBIT (1-t) - Net Cap Ex - Change in Working Capital

= 3356 (1 - 0.36) + 1100 - 2500 - 250 = \$ 498 million

|               | \$ Value | Correct Multiple |
|---------------|----------|------------------|
| FCFF          | \$498    | 31.28382355      |
| EBIT (1-t)    | \$2,148  | 7.251163362      |
| EBIT \$ 3,356 |          | 4.640744552      |
| EBITDA        | \$4,456  | 3.49513885       |

#### Value/EBITDA Multiple

#### n The Classic Definition

#### n The No-Cash Version

n When cash and marketable securities are netted out of value, none of the income from the cash and securities should be reflected in the denominator.

$$\frac{\text{Value}}{\text{EBITDA}} = \frac{\text{Market Value of Equity} + \text{Market Value of Debt}}{\text{Earnings before Interest, Taxes and Depreciation}}$$

Value EBITDA = Market Value of Equity + Market Value of Debt - Cash Earnings before Interest, Taxes and Depreciation

## Value/EBITDA Multiples

![](_page_162_Figure_2.jpeg)

Value/EBITDA Multiples: US in June 1999

## The Determinants of Value/EBITDA Multiples: Linkage to DCF Valuation

n Firm value can be written as:

n The numerator can be written as follows:

| FCFF | = EBIT (1-t) - (Cex - Depr) - $\Delta$ Working Capital            |
|------|-------------------------------------------------------------------|
|      | = (EBITDA - Depr) (1-t) - (Cex - Depr) - $\Delta$ Working Capital |
|      | = EBITDA (1-t) + Depr (t) - Cex - $\Delta$ Working Capital        |

$$V_0 = \frac{\text{FCFF}_1}{\text{WACC} - \text{g}}$$

#### From Firm Value to EBITDA Multiples

n Now the Value of the firm can be rewritten as,

n Dividing both sides of the equation by EBITDA,

$$\text{Value} = \frac{\text{EBITDA (1\$)} + \text{Depr (t)} - \text{Cex} - \Delta \text{Working Capital}}{\text{WACC-g}}$$

| Value  | $\frac{(1-t)}{\text{EBITDA}} = \frac{\text{WACC-g}}{\text{WACC-g}} + \frac{\text{Depr (t)/EBITDA}}{\text{WACC-g}} - \frac{\text{CEx/EBITDA}}{\text{WACC-g}} - \frac{\Delta \text{Working Capital/EBITDA}}{\text{WACC-g}}$ |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EBITDA |                                                                                                                                                                                                                           |

#### A Simple Example

n Consider a firm with the following characteristics:

- Tax Rate = 36%
- Capital Expenditures/EBITDA = 30%
- Depreciation/EBITDA = 20%
- Cost of Capital = 10%
- The firm has no working capital requirements
- The firm is in stable growth and is expected to grow 5% a year forever.
- Note that the return on capital implied in this growth rate can be calculated as follows:

g = ROC \* Reinvestment Rate

.05 = ROC \* Net Cap Ex/EBIT (1-t)

$$= \text{ROC} * (.30-.20)/[(1-.2)(1-.36)]$$

Solving for ROC, ROC = 25.60%

#### Calculating Value/EBITDA Multiple

n In this case, the Value/EBITDA multiple for this firm can be estimated as follows:

| Value  | $\frac{(1-36)}{10-.05} + \frac{(0.2)(.36)}{.10-.05} - \frac{0.3}{.10-.05} - \frac{0}{.10-.05} = 8.24$ |
|--------|-------------------------------------------------------------------------------------------------------|
| EBITDA |                                                                                                       |

## Value/EBITDA Multiples and Taxes

**VEBITDA Multiples and Tax Rates**

![](_page_167_Figure_2.jpeg)

## Value/EBITDA and Net Cap Ex

**Value/EBITDA and Net Cap Ex Ratios**

![](_page_168_Figure_2.jpeg)

## Value/EBITDA Multiples and Return on Capital

**Value/EBITDA and Return on Capital**

![](_page_169_Figure_2.jpeg)

#### Value/EBITDA Multiple: Trucking Companies

| Company Name              |             | Value  | EBITDA      |        | Value/EBITDA |
|---------------------------|-------------|--------|-------------|--------|--------------|
| KLLM Trans. Svcs.         | \$          | 114.32 | \$          | 48.81  | 2.34         |
| Ryder System              | \$ 5,158.04 |        | \$ 1,838.26 |        | 2.81         |
| Rollins Truck Leasing     | \$ 1,368.35 |        | \$          | 447.67 | 3.06         |
| Cannon Express Inc.       | \$          | 83.57  | \$          | 27.05  | 3.09         |
| Hunt (J.B.)               | \$          | 982.67 | \$          | 310.22 | 3.17         |
| Yellow Corp.              | \$          | 931.47 | \$          | 292.82 | 3.18         |
| Roadway Express           | \$          | 554.96 | \$          | 169.38 | 3.28         |
| Marten Transport Ltd.     | \$          | 116.93 | \$          | 35.62  | 3.28         |
| Kenan Transport Co.       | \$          | 67.66  | \$          | 19.44  | 3.48         |
| M.S. Carriers             | \$          | 344.93 | \$          | 97.85  | 3.53         |
| Old Dominion Freight      | \$          | 170.42 | \$          | 45.13  | 3.78         |
| Trimac Ltd                | \$          | 661.18 | \$          | 174.28 | 3.79         |
| Matlack Systems           | \$          | 112.42 | \$          | 28.94  | 3.88         |
| XTRA Corp.                | \$ 1,708.57 |        | \$          | 427.30 | 4.00         |
| Covenant Transport Inc    | \$          | 259.16 | \$          | 64.35  | 4.03         |
| Builders Transport        | \$          | 221.09 | \$          | 51.44  | 4.30         |
| Werner Enterprises        | \$          | 844.39 | \$          | 196.15 | 4.30         |
| Landstar Sys.             | \$          | 422.79 | \$          | 95.20  | 4.44         |
| AMERCO                    | \$ 1,632.30 |        | \$          | 345.78 | 4.72         |
| USA Truck                 | \$          | 141.77 | \$          | 29.93  | 4.74         |
| Frozen Food Express       | \$          | 164.17 | \$          | 34.10  | 4.81         |
| Arnold Inds.              | \$          | 472.27 | \$          | 96.88  | 4.87         |
| Greyhound Lines Inc.      | \$          | 437.71 | \$          | 89.61  | 4.88         |
| USFreightways             | \$          | 983.86 | \$          | 198.91 | 4.95         |
| Golden Eagle Group Inc.   | \$          | 12.50  | \$          | 2.33   | 5.37         |
| Arkansas Best             | \$          | 578.78 | \$          | 107.15 | 5.40         |
| Airlease Ltd.             | \$          | 73.64  | \$          | 13.48  | 5.46         |
| Celadon Group             | \$          | 182.30 | \$          | 32.72  | 5.57         |
| Amer. Freightways         | \$          | 716.15 | \$          | 120.94 | 5.92         |
| Transfinancial Holdings   | \$          | 56.92  | \$          | 8.79   | 6.47         |
| Vitran Corp. 'A'          | \$          | 140.68 | \$          | 21.51  | 6.54         |
| Interpool Inc.            | \$ 1,002.20 |        | \$          | 151.18 | 6.63         |
| Intrenet Inc.             | \$          | 70.23  | \$          | 10.38  | 6.77         |
| Swift Transportation      | \$          | 835.58 | \$          | 121.34 | 6.89         |
| Landair Services          | \$          | 212.95 | \$          | 30.38  | 7.01         |
| CNF Transportation        | \$ 2,700.69 |        | \$          | 366.99 | 7.36         |
| Budget Group Inc          | \$ 1,247.30 |        | \$          | 166.71 | 7.48         |
| Caliber System            | \$ 2,514.99 |        | \$          | 333.13 | 7.55         |
| Knight Transportation Inc | \$          | 269.01 | \$          | 28.20  | 9.54         |
| Heartland Express         | \$          | 727.50 | \$          | 64.62  | 11.26        |
| Greyhound CDA Transn Corp | \$          | 83.25  | \$          | 6.99   | 11.91        |
| Mark VII                  | \$          | 160.45 | \$          | 12.96  | 12.38        |
| Coach USA Inc             | \$          | 678.38 | \$          | 51.76  | 13.11        |
| US 1 Inds Inc.            | \$          | 5.60   | \$          | (0.17) | NA           |
| Average                   |             |        |             |        | 5.61         |

#### A Test on EBITDA

n Ryder System looks very cheap on a Value/EBITDA multiple basis, relative to the rest of the sector. What explanation (other than misvaluation) might there be for this difference?

#### Value/EBITDA Multiples: Market

- n The multiple of value to EBITDA varies widely across firms in the market, depending upon:
  - how capital intensive the firm is (high capital intensity firms will tend to have lower value/EBITDA ratios), and how much reinvestment is needed to keep the business going and create growth
  - how high or low the cost of capital is (higher costs of capital will lead to lower Value/EBITDA multiples)
  - how high or low expected growth is in the sector (high growth sectors will tend to have higher Value/EBITDA multiples)

#### US Market: Cross Sectional Regression

#### \* \* \* \* M U L T I P L E R E G R E S S I O N \* \* \* \*

Variable(s) Entered on Step Number

| 1.. | PROJGR  | Proj EPS Growth Rate |
|-----|---------|----------------------|
| 2.. | ROC     |                      |
| 3.. | TAXRATE | Income00Tax0Rate     |

Multiple R .41057

R Square .16856

Adjusted R Square .16637

Standard Error 5.38026

Analysis of Variance

| Regression on | FDF  | Sum of Squares | Mean Square |
|---------------|------|----------------|-------------|
| Regression on | 3    | 6660. 96980    | 2220. 32327 |
| Resi dual     | 1135 | 32855. 05082   | 28. 94718   |

F = 76.70257 Signif F = .0000

------------------ Variables in the Equation ------------------

| Variable   |          | B        | SE B     | Beta T Sig T |
|------------|----------|----------|----------|--------------|
| ROC        | 7.513209 | 1.313987 | .154857  | 5.718 .0000  |
| TAXRATE    | -.011212 | .007025  | -.043263 | -1.596 .1108 |
| PROJGR     | .237715  | .017423  | .370070  | 13.644 .0000 |
| (Constant) | 3.967952 | .443839  |          | 8.940 .0000  |

#### Price-Book Value Ratio: Definition

n The price/book value ratio is the ratio of the market value of equity to the book value of equity, i.e., the measure of shareholders' equity in the balance sheet.

n Price/Book Value = Market Value of Equity Book Value of Equity

- n Consistency Tests:
  - If the market value of equity refers to the market value of equity of common stock outstanding, the book value of common equity should be used in the denominator.
  - If there is more that one class of common stock outstanding, the market values of all classes (even the non-traded classes) needs to be factored in.

#### PBV Ratio: Cross Sectional Distribution

**PBV Ratio: Italy - December 1999**

![](_page_175_Figure_2.jpeg)

#### Price Book Value Ratio: Stable Growth Firm

n Going back to a simple dividend discount model,

<sup>n</sup> Defining the return on equity (ROE) = EPS<sup>0</sup> / Book Value of Equity, the value of equity can be written as:

n If the return on equity is based upon expected earnings in the next time period, this can be simplified to,

$$P_0 = \frac{DPS_1}{r - g_n}$$

$$P_0 = \frac{BV_0 *ROE*Payout Ratit(1+g_n)}{r-g_n}$$

$$\frac{P_0}{BV_0} = PBV = \frac{ROE * Payout Ratio (1 + g_n)}{r \cdot g_n}$$

$$\frac{P_0}{BV_0} = \text{PBV} = \frac{\text{ROE } *\text{Payout Ratio}}{\text{r}\cdot g_n}$$

#### PBV/ROE: Oil Companies: 1996

| Company Name                  | P/BV | ROE   |
|-------------------------------|------|-------|
| Total ADR B                   | 0.90 | 4.10  |
| Giant Industries              | 1.10 | 7.20  |
| Royal Dutch Petroleum ADR     | 1.10 | 12.30 |
| Tesoro Petroleum              | 1.10 | 5.20  |
| Petrobras                     | 1.15 | 3.37  |
| YPF ADR                       | 1.60 | 13.40 |
| Ashland                       | 1.70 | 10.60 |
| Quaker State                  | 1.70 | 4.40  |
| Coastal                       | 1.80 | 9.40  |
| Elf Aquitaine ADR             | 1.90 | 6.20  |
| Holly                         | 2.00 | 20.00 |
| Ultramar Diamond Shamrock     | 2.00 | 9.90  |
| Witco                         | 2.00 | 10.40 |
| World Fuel Services           | 2.00 | 17.20 |
| Elcor                         | 2.10 | 10.10 |
| Imperial Oil                  | 2.20 | 8.60  |
| Repsol ADR                    | 2.20 | 17.40 |
| Shell Transport & Trading ADR | 2.40 | 10.50 |
| Amoco                         | 2.60 | 17.30 |
| Phillips Petroleum            | 2.60 | 14.70 |
| ENI SpA ADR                   | 2.80 | 18.30 |
| Mapco                         | 2.80 | 16.20 |
| Texaco                        | 2.90 | 15.70 |
| British Petroleum ADR         | 3.20 | 19.60 |
| Tosco                         | 3.50 | 13.70 |
| Average                       | 2.05 | 11.83 |

#### PBV versus ROE regression

n Regressing PBV ratios against ROE for oil companies yields the following regression:

PBV = 0.96 + 9.28 (ROE) R<sup>2</sup> = 46.67%

n For every 1% increase in ROE, the PBV ratio should increase by 0.0928.

#### Looking for undervalued securities - PBV Ratios and ROE

n Given the relationship between price-book value ratios and returns on equity, it is not surprising to see firms which have high returns on equity selling for well above book value and firms which have low returns on equity selling at or below book value. n The firms which should draw attention from investors are those which provide mismatches of price-book value ratios and returns on equity - low P/BV ratios and high ROE or high P/BV ratios and low ROE.

#### The Valuation Matrix

| MV/BV                                      |                                             | ROE-r |
|--------------------------------------------|---------------------------------------------|-------|
| <i>Overvalued</i><br>Low ROE<br>High MV/BV | High ROE<br>High MV/BV                      |       |
| Low ROE<br>Low MV/BV                       | <i>Undervalued</i><br>High ROE<br>Low MV/BV |       |

## PBV Matrix: Telecom Companies

![](_page_181_Figure_1.jpeg)

#### IBM: The Rise and Fall

**IBM: PBV and ROE**

![](_page_182_Figure_2.jpeg)

## PBV Ratio Regression

 1.. PAYOUT: Dividend Payout Ratio 2.. ROE: Current ROE 3.. EXPGR: Expected Growth Rate in EPS: Next 5 yrs 4.. BETA: Beta

Multiple R .85660 R Square .73376 Adjusted R Square .73298 Standard Error 4.70884

#### Analysis of Variance

|             | DF   | Sum of Squares | Mean Square  |
|-------------|------|----------------|--------------|
| Regressi on | 4    | 82865. 04208   | 20716. 26052 |
| Resi dual   | 1356 | 30066. 86953   | 22. 17321    |

F = 934.29245 Signif F = .0000

#### ------------------ Variables in the Equation ------------------

| Variable |           | B        | SE B     | Beta   | T Sig T |
|----------|-----------|----------|----------|--------|---------|
| ROE      | 17.251308 | .368105  | .742046  | 46.865 | .0000   |
| BETA     | -.919887  | .258805  | -.103865 | -3.554 | .0004   |
| EXPGR    | 17.617391 | 1.566251 | .317885  | 11.248 | .0000   |
| PAYOUT2  | -.014157  | .120198  | -.001704 | -.118  | .9063   |

#### Cross Sectional Regression for Italy: December 1999

n Using data obtained on 247 Italian companies, we ran the regression of PBV ratios against returns on equity and obtained the following:

PBV = 1.33 + 10.84 ROE R<sup>2</sup> = 21.87% (5.48) (6.59)

n For instance, the predicted PBV ratios for the following companies would be:

| Company    | Actual PBV | ROE    | Predicted PBV                  |
|------------|------------|--------|--------------------------------|
| Tel Italia | 3.53       | 11.55% | 1.33 + 10.84(.12)= 2.63        |
|            | TI Mobile  | 22.13  | 49.70% 1.33 + 10.84(.50)= 6.75 |

#### Price Sales Ratio: Definition

- n The price/sales ratio is the ratio of the market value of equity to the sales. n Price/ Sales= Market Value of Equity Total Revenues n Consistency Tests
  - The price/sales ratio is internally inconsistent, since the market value of equity is divided by the total revenues of the firm.

#### Price/Sales Ratio: Cross Sectional Distribution

**PS Ratio: Italy - December 1999**

![](_page_186_Figure_2.jpeg)

#### Price/Sales Ratio: Determinants

n The price/sales ratio of a stable growth firm can be estimated beginning with a 2-stage equity valuation model:

n Dividing both sides by the sales per share:

$$P_0 = \frac{DPS_1}{r - g_n}$$

$$\frac{P_0}{\text{Sales}_0} = PS = \frac{\text{Net Profit Margin} * \text{Payout Ratio} * (1 + g_n)}{r - g_n}$$

#### PS/Margins: European Department Stores

| Company         | PS ratio | Margin |
|-----------------|----------|--------|
| Kaufring        | 0.08     | 0.03%  |
| Galeries        | 0.27     | 0.76%  |
| House of        | 0.27     | 2.76%  |
| Karstadt        | 0.29     | 0.69%  |
| Wessel          | 0.34     | 2.74%  |
| Bazar De        | 0.35     | 1.59%  |
| Storehou        | 0.45     | 6.74%  |
| Metro AG        | 0.74     | 1.09%  |
| Pinault         | 1.12     | 2.97%  |
| Selfridges      | 1.42     | 4.56%  |
| Marks & Spencer | 1.48     | 10.06% |
| Kingfish        | 1.70     | 5.98%  |

#### Regression Results: PS Ratios and Margins

n Regressing PS ratios against net margins,

| $\text{PS} = 0.27 + 13.16 \text{ (Net Margin)}$ | $\text{R}^2 = 48.37\%$ |
|-------------------------------------------------|------------------------|
|-------------------------------------------------|------------------------|

$$R^2 = 48.37\%$$

n Thus, a 1% increase in the margin results in an increase of 0.13 in the price sales ratios. n The regression also allows us to get predicted PS ratios for these firms

#### PS Ratios: Actual versus Predicted Values

| Company         | PS ratio | Margin | Predicted PS Ratio |
|-----------------|----------|--------|--------------------|
| Kaufring        | 0.08     | 0.03%  | 0.27               |
| Galeries        | 0.27     | 0.76%  | 0.37               |
| House of        | 0.27     | 2.76%  | 0.63               |
| Karstadt        | 0.29     | 0.69%  | 0.36               |
| Wessel          | 0.34     | 2.74%  | 0.63               |
| Bazar De        | 0.35     | 1.59%  | 0.48               |
| Storehou        | 0.45     | 6.74%  | 1.16               |
| Metro AG        | 0.74     | 1.09%  | 0.41               |
| Pinault         | 1.12     | 2.97%  | 0.66               |
| Selfridges      | 1.42     | 4.56%  | 0.87               |
| Marks & Spencer | 1.48     | 10.06% | 1.59               |
| Kingfish        | 1.70     | 5.98%  | 1.06               |

## Current versus Predicted Margins

n One of the limitations of the analysis we did in these last few pages is the focus on current margins. Stocks are priced based upon expected margins rather than current margins. n For most firms, current margins and predicted margins are highly correlated, making the analysis still relevant. n For firms where current margins have little or no correlation with expected margins, regressions of price to sales ratios against current margins (or price to book against current return on equity) will not provide much explanatory power. n In these cases, it makes more sense to run the regression using either predicted margins or some proxy for predicted margins.

## A Case Study: The Internet Stocks

| Company Name           | PS Ratio | Revenue Year 2Net Income TTM |            |
|------------------------|----------|------------------------------|------------|
| America Online         | 13.66    | \$1,685.00                   | \$168.00   |
| CNET                   | 18.94    | \$14.80                      | (\$12.40)  |
| EarthWeb               | 138.30   | \$0.50                       | (\$8.10)   |
| Excite                 | 21.66    | \$14.80                      | (\$41.40)  |
| IDT Corp               | 1.91     | \$57.70                      | (\$6.40)   |
| Infoseek               | 17.07    | \$15.10                      | (\$8.40)   |
| Lycos                  | 38.98    | \$5.30                       | (\$96.90)  |
| MindSpring Enterprises | 18.15    | \$18.10                      | \$7.40     |
| Periphonics Corp       | 1.20     | \$111.20                     | \$5.50     |
| PSINET                 | 4.84     | \$89.80                      | (\$147.10) |
| Spyglass               | 15.89    | \$22.30                      | (\$8.00)   |
| Sterling Commerce      | 6.77     | \$267.80                     | (\$61.20)  |
| Sykes Enterprises      | 2.07     | \$219.00                     | (\$2.70)   |
| Yahoo!                 | 126.24   | \$19.70                      | (\$16.30)  |

## PS Ratios and Margins are not highly correlated

n Regressing PS ratios against current margins yields the following

PS = 27.90 - 1.29(Margin) R<sup>2</sup> = 0.02 (0.49)

n This is not surprising. These firms are priced based upon expected margins, rather than current margins. Hypothesizing that firms with higher revenue growth and higher cash balances should have a greater chance of surviving and becoming profitable, we ran the following regression: (The level of revenues was used to control for size)

PS = 40.47 - 11.02 ln(Rev) + 11.37 (Rev Growth) + 32.24 (Cash/Rev) (2.03) (1.27) (2.36)

R squared = 61.67%

#### PS Regression

 1.. PAYOUT: Payout Ratio 2.. MARGIN: Net Income/Sales 3.. EXPGR: Expected growth rate: 5 years 4.. BETA5 Beta 5-Year

Multiple R .84486 R Square .71378 Adjusted R Square .71279 Standard Error 1.47851

#### Analysis of Variance

|             | <b>DF</b> | <b>Sum</b> of Squares | <b>Mean Square</b> |
|-------------|-----------|-----------------------|--------------------|
| Regressi on | 4         | 6274. 66332           | 1568. 66583        |
| Resi dual   | 1151      | 2516. 07354           | 2. 18599           |

F = 717.60000 Signif F = .0000

------------------ Variables in the Equation ------------------

| Variable |           | B       | SE B Beta | T Sig T      |
|----------|-----------|---------|-----------|--------------|
| MARGIN   | 18.641391 | .640321 | .632172   | 29.113 .0000 |
| BETA5    | .090710   | .081657 | .033125   | 1.111 .2669  |
| EXPGR    | 4.362717  | .491218 | .255182   | 8.881 .0000  |
| PAYOUT2  | -.001752  | .007616 | -.003640  | -.230 .8181  |

#### Cross Sectional Regression for Italy in December 1999

n Using data on 247 Italian companies from 1999, we regressed PS ratios against profit margins:

PS = 1.20 + 11.45 Margin (5.03) (5.30) R<sup>2</sup>

= 20.52%

## Choosing Between the Multiples

- n As presented in this section, there are dozens of multiples that can be potentially used to value an individual firm. n In addition, relative valuation can be relative to a sector (or comparable firms) or to the entire market (using the regressions, for instance) n Since there can be only one final estimate of value, there are three choices at this stage:
  - Use a simple average of the valuations obtained using a number of different multiples
  - Use a weighted average of the valuations obtained using a nmber of different multiples
  - Choose one of the multiples and base your valuation on that multiple

## Picking one Multiple

- n This is usually the best way to approach this issue. While a range of values can be obtained from a number of multiples, the "best estimate" value is obtained using one multiple. n The multiple that is used can be chosen in one of two ways:
  - Use the multiple that best fits your objective. Thus, if you want the company to be undervalued, you pick the multiple that yields the highest value.
  - Use the multiple that has the highest R-squared in the sector when regressed against fundamentals. Thus, if you have tried PE, PBV, PS, etc. and run regressions of these multiples against fundamentals, use the multiple that works best at explaining differences across firms in that sector.
  - Use the multiple that seems to make the most sense for that sector, given how value is measured and created.

## A More Intuitive Approach

n As a general rule of thumb, the following table provides a way of picking a multiple for a sector

| Sector                  | Multiple Used   | Rationale                            |
|-------------------------|-----------------|--------------------------------------|
| Cyclical Manufacturing  | PE, Relative PE | Often with normalized earnings       |
| High Tech, High Growth  | PEG             | Big differences in growth across     |
| High Growth/No Earnings | PS, VS          | Assume future margins will be good   |
| Heavy Infrastructure    | VEBITDA         | Firms in sector have losses in early |
| REITa                   | P/CF            | Generally no cap ex investments      |
| Financial Services      | PBV             | Book value often marked to market    |
| Retailing               | PS              | If leverage is similar across firms  |
|                         | VS              | If leverage is different             |

#### Reviewing: The Four Steps to Understanding Multiples

- n Define the multiple
  - Check for consistency
- Make sure that they are estimated uniformally n Describe the multiple
  - Multiples have skewed distributions: The averages are seldom good indicators of typical multiples
- Check for bias, if the multiple cannot be estimated n Analyze the multiple
  - Identify the companion variable that drives the multiple
- Examine the nature of the relationship n Apply the multiple

## Option Pricing Applications in Valuation

Aswath Damodaran

#### Options in Projects/Investments/Acquisitions

- n One of the limitations of traditional investment analysis is that it is static and does not do a good job of capturing the options embedded in investment.
  - The first of these options is the option to delay taking a investment, when a firm has exclusive rights to it, until a later date.
  - The second of these options is taking one investment may allow us to take advantage of other opportunities (investments) in the future
- The last option that is embedded in projects is the option to abandon a investment, if the cash flows do not measure up. n These options all add value to projects and may make a "bad" investment (from traditional analysis) into a good one.

#### The Option to Delay

n When a firm has exclusive rights to a project or product for a specific period, it can delay taking this project or product until a later date. n A traditional investment analysis just answers the question of whether the project is a "good" one if taken today. n Thus, the fact that a project does not pass muster today (because its NPV is negative, or its IRR is less than its hurdle rate) does not mean that the rights to this project are not valuable.

#### Valuing the Option to Delay a Project

![](_page_203_Diagram_1.jpeg)

#### Insights for Investment Analyses

n Having the exclusive rights to a product or project is valuable, even if the product or project is not viable today. n The value of these rights increases with the volatility of the underlying business. n The cost of acquiring these rights (by buying them or spending money on development, for instance) has to be weighed off against these benefits.

## Example 1: Valuing product patents as options

n A product patent provides the firm with the right to develop the product and market it. n It will do so only if the present value of the expected cash flows from the product sales exceed the cost of development. n If this does not occur, the firm can shelve the patent and not incur any further costs. n If I is the present value of the costs of developing the product, and V is the present value of the expected cashflows from development, the payoffs from owning a product patent can be written as:

Payoff from owning a product patent = V - I if V> I = 0 if V £ I

## Payoff on Product Option

![](_page_206_Diagram_1.jpeg)

## Obtaining Inputs for Patent Valuation

| Input                                    | Estimation Process                                |
|------------------------------------------|---------------------------------------------------|
| 1. Value of the Underlying Asset         | Present Value of Cash Inflows from taking project |
| 2. Variance in value of underlying asset | Variance in cash flows of similar assets or firms |
| 3. Exercise Price on Option              | Option is exercised when investment is made.      |
| 4. Expiration of the Option              | Life of the patent                                |
| 5. Dividend Yield                        | Cost of delay                                     |

## Valuing Biogen

- n The firm is receiving royalties from Biogen discoveries (Hepatitis B and Intron) at pharmaceutical companies. These account for FCFE per share of \$1.00 and are expected to grow 10% a year until the patent expires (in 15 years). n Using a beta of 1.1 to value these cash flows (leading to a cost of equity of 13.05%), we arrive at a present value per share:
  - Value of Existing Products = \$ 12.14

## Valuing the Other Component: Avonex

n The firm also has a patent on Avonex, a drug to treat multiple sclerosis, for the next 17 years, and it plans to produce and sell the drug by itself. The key inputs on the drug are as follows:

Present Value of Cash Flows from Introducing the Drug Now = S = \$ 3.422 billion

Present Value of Cost of Developing Drug for Commercial Use = K = \$ 2.875 billion

Patent Life = t = 17 years Riskless Rate = r = 6.7% (17-year T.Bond rate)

**Variance in Expected Present Values =  $\sigma^2 = 0.224$  (Industry average)**

Expected Cost of Delay = y = 1/17 = 5.89%

d1 = 1.1362 N(d1) = 0.8720

d2 = -0.8512 N(d2) = 0.2076

Call Value= 3,422 exp(-0.0589)(17) (0.8720) - 2,875 (exp(-0.067)(17) (0.2076)= \$ 907 million

Call Value per Share from Avonex = \$ 907 million/35.5 million = \$ 25.55

## Biogen's total value per share

n Value of Existing Products = \$ 12.14 n Call Value per Share from Avonex = \$ 907 million/35.5 million = \$ 25.55 n Biogen Value Per Share = Value of Existing Assets + Value of Patent = \$ 12.14 + \$ 25.55 = \$ 37.69

## Example 2: Valuing Natural Resource Options

- ■ In a natural resource investment, the underlying asset is the resource and the value of the asset is based upon two variables - the quantity of the resource that is available in the investment and the price of the resource.
  ■ In most such investments, there is a cost associated with developing the resource, and the difference between the value of the asset extracted and the cost of the development is the profit to the owner of the resource.
  ■ Defining the cost of development as  $X$ , and the estimated value of the resource as  $V$ , the potential payoffs on a natural resource option can be written as follows:

## Payoff Diagram on Natural Resource Firms

![](_page_212_Diagram_1.jpeg)

## Inputs to the Model

*Input to model Corresponding input for valuing firm*

Value of underlying asset Value of cumulated estimated reserves of the resource owned by the firm, discounted back at the dividend yield for the development lag.

Exercise Price Estimated cumulated cost of developing estimated reserves

Time to expiration on option Average relinquishment period across all reserves owned by firm (if known) or estimate of when reserves will be exhausted, given current

production rates.

Riskless rate Riskless rate corresponding to life of the option

Variance in value of asset Variance in the price of the natural resource

Dividend yield Estimated annual net production revenue as percentage of value of the reserve.

## Valuing Gulf Oil

n Gulf Oil was the target of a takeover in early 1984 at \$70 per share (It had 165.30 million shares outstanding, and total debt of \$9.9 billion). n It had estimated reserves of 3038 million barrels of oil and the average cost of developing these reserves was estimated to be \$10 a barrel in present value dollars (The development lag is approximately two years). n The average relinquishment life of the reserves is 12 years. n The price of oil was \$22.38 per barrel, and the production cost, taxes and royalties were estimated at \$7 per barrel. n The bond rate at the time of the analysis was 9.00%. n Gulf was expected to have net production revenues each year of approximately 5% of the value of the developed reserves. The variance in oil prices is 0.03.

## Valuing Undeveloped Reserves

- Value of underlying asset = Value of estimated reserves discounted back for period of development lag= 3038 \* (\$ 22.38 - \$7) / 1.05<sup>2</sup> = **\$42,380.44**
- Exercise price = Estimated development cost of reserves = 3038 \* \$10 = **\$30,380 million**
- Time to expiration = Average length of relinquishment option = **12 years**
- Variance in value of asset = Variance in oil prices = **0.03**
- Riskless interest rate = **9%**
- Dividend yield = Net production revenue/ Value of developed reserves = **5%** n Based upon these inputs, the Black-Scholes model provides the following value for the call: d1 = 1.6548 N(d1) = 0.9510 d2 = 1.0548 N(d2) = 0.8542 n Call Value= 42,380.44 exp(-0.05)(12) (0.9510) -30,380 (exp(-0.09)(12) (0.8542)= **\$ 13,306 million**

## Valuing Gulf Oil

- n In addition, Gulf Oil had free cashflows to the firm from its oil and gas production of \$915 million from already developed reserves and these cashflows are likely to continue for ten years (the remaining lifetime of developed reserves). n The present value of these developed reserves, discounted at the weighted average cost of capital of 12.5%, yields:
- Value of already developed reserves = 915 (1 1.125-10)/.125 = \$5065.83 n Adding the value of the developed and undeveloped reserves Value of undeveloped reserves = \$ 13,306 million Value of production in place = \$ 5,066 million Total value of firm = \$ 18,372 million Less Outstanding Debt = \$ 9,900 million Value of Equity = \$ 8,472 million Value per share = \$ 8,472/165.3 = \$51.25

#### The Option to Expand/Take Other Projects

n Taking a project today may allow a firm to consider and take other valuable projects in the future. n Thus, even though a project may have a negative NPV, it may be a project worth taking if the option it provides the firm (to take other projects in the future) provides a more-than-compensating value. n These are the options that firms often call "strategic options" and use as a rationale for taking on "negative NPV" or even "negative return" projects.

#### The Option to Expand

![](_page_218_Diagram_1.jpeg)

#### An Example of an Expansion Option

n Disney is considering investing \$ 100 million to create a Spanish version of the Disney channel to serve the growing Mexican market. n A financial analysis of the cash flows from this investment suggests that the present value of the cash flows from this investment to Disney will be only \$ 80 million. Thus, by itself, the new channel has a **negative NPV of \$ 20 million**. n If the market in Mexico turns out to be more lucrative than currently anticipated, Disney **could expand** its reach to all of Latin America with **an additional investment of \$ 150 million** any time over the next 10 years. While the current expectation is that the cash flows from having a Disney channel in Latin America is only \$ 100 million, there is considerable uncertainty about both the potential for such an channel and the shape of the market itself, leading to significant variance in this estimate.

#### Valuing the Expansion Option

- n Value of the Underlying Asset (S) = PV of Cash Flows from Expansion to Latin America, if done now =\$ 100 Million n Strike Price (K) = Cost of Expansion into Latin American = \$ 150 Million n We estimate the variance in the estimate of the project value by using the annualized variance in firm value of publicly traded entertainment firms in the Latin American markets, which is approximately 10%.
- Variance in Underlying Asset's Value = 0.10 n Time to expiration = Period for which expansion option applies = 10 years

**Call Value= \$ 45.9 Million**

#### Considering the Project with Expansion Option

n NPV of Disney Channel in Mexico = \$ 80 Million - \$ 100 Million = - \$ 20 Million n Value of Option to Expand = \$ 45.9 Million n NPV of Project with option to expand = - \$ 20 million + \$ 45.9 million = \$ 25.9 million n **Take the project**

## The Link to Strategy

- n In many investments, especially acquisitions, strategic options or considerations are used to take investments that otherwise do not meet financial standards. n These strategic options or considerations are usually related to the expansion option described here. The key differences are as follows:
  - Unlike "strategic options" which are usually qualitative and not valued, expansion options can be assigned a quantitative value and can be brought into the investment analysis.
  - Not all "strategic considerations" have option value. For an expansion option to have value, the first investment (acquisition) must be necessary for the later expansion (investment). If it is not, there is no option value that can be added on to the first investment.

## The Exclusivity Requirement in Option Value

![](_page_223_Diagram_1.jpeg)

## The Determinants of Real Option Value

- n Does taking on the first investment/expenditure provide the firm with an exclusive advantage on taking on the second investment?
  - If yes, the firm is entitled to consider 100% of the value of the real option
- If no, the firm is entitled to only a portion of the value of the real option, with the proportion determined by the degree of exclusivity provided by the first investment? n Is there a possibility of earning significant and sustainable excess returns on the second investment?
  - If yes, the real option will have significant value
  - If no, the real option has no value

## Internet Firms as Options

- n Some analysts have justified the valuation of internet firms on the basis that you are buying the option to expand into a very large market. What do you think of this argument?
  - Is there an option to expand embedded in these firms?
  - Is it a valuable option?

#### The Option to Abandon

n A firm may sometimes have the option to abandon a project, if the cash flows do not measure up to expectations. n If abandoning the project allows the firm to save itself from further losses, this option can make a project more valuable.

![](_page_226_Diagram_2.jpeg)

## Implications for Investment Analysis

- n Having a option to abandon a project can make otherwise unacceptable projects acceptable. n Actions that increase the value of the abandonment option include
  - More cost flexibility, that is, making more of the costs of the projects into variable costs as opposed to fixed costs.
  - Fewer long-term contracts/obligations with employees and customers, since these add to the cost of abandoning a project
- Finding partners in the investment, who are willing to acquire your investment in the future n These actions will undoubtedly cost the firm some value, but this has to be weighed off against the increase in the value of the abandonment option.

## Option Pricing Applications in Valuation

Equity Value in Deeply Troubled Firms

Value of Undeveloped Reserves for Natural Resource Firm

Value of Patent/License

## Option Pricing Applications in Equity Valuation

n Equity in a troubled firm (i.e. a firm with high leverage, negative earnings and a significant chance of bankruptcy) can be viewed as a call option, which is the option to liquidate the firm. n Natural resource companies, where the undeveloped reserves can be viewed as options on the natural resource. n Start-up firms or high growth firms which derive the bulk of their value from the rights to a product or a service (eg. a patent)

## Valuing Equity as an option

n The equity in a firm is a **residual claim**, i.e., equity holders lay claim to all cashflows left over after other financial claim-holders (debt, preferred stock etc.) have been satisfied. n If a firm is liquidated, the same principle applies, with equity investors **receiving whatever is left over in the firm** after all outstanding debts and other financial claims are paid off. n The **principle of limited liability**, however, protects equity investors in publicly traded firms if the value of the firm is less than the value of the outstanding debt, and they cannot lose more than their investment in the firm.

## Equity as a call option

n The payoff to equity investors, on liquidation, can therefore be written as:

| Payoff to equity on liquidation | $= V - D$ | if $V > D$    |
|---------------------------------|-----------|---------------|
|                                 | $= 0$     | if $V \leq D$ |

where,

V = Value of the firm

D = Face Value of the outstanding debt and other external claims

n A call option, with a strike price of K, on an asset with a current value of S, has the following payoffs:

| Payoff on exercise | $= S - K$ | if $S > K$    |
|--------------------|-----------|---------------|
|                    | $= 0$     | if $S \leq K$ |

## Payoff Diagram for Liquidation Option

![](_page_232_Figure_1.jpeg)

## Application to valuation: A simple example

- n Assume that you have a firm whose assets are currently valued at \$100 million and that the standard deviation in this asset value is 40%. n Further, assume that the face value of debt is \$80 million (It is zero coupon debt with 10 years left to maturity). n If the ten-year treasury bond rate is 10%,
  - how much is the equity worth?
  - What should the interest rate on debt be?

## Model Parameters

- ■ Value of the underlying asset =  $S = \text{Value of the firm} = \$ 100 \text{ million}$
- ■ Exercise price =  $K = \text{Face Value of outstanding debt} = \$ 80 \text{ million}$
- ■ Life of the option =  $t = \text{Life of zero-coupon debt} = 10 \text{ years}$
- ■ Variance in the value of the underlying asset =  $\sigma^2 = \text{Variance in firm value} = 0.16$
- ■ Riskless rate =  $r = \text{Treasury bond rate corresponding to option life} = 10\%$

## Valuing Equity as a Call Option

n Based upon these inputs, the Black-Scholes model provides the following value for the call:

• 
$$d1 = 1.5994$$
       $N(d1) = 0.9451$ 

• 
$$d2 = 0.3345$$
       $N(d2) = 0.6310$ 

n Value of the call = 100 (0.9451) - 80 exp(-0.10)(10) (0.6310) = \$75.94 million

n Value of the outstanding debt = \$100 - \$75.94 = \$24.06 million

n Interest rate on debt = (\$ 80 / \$24.06)1/10 -1 = 12.77%

## The Effect of Catastrophic Drops in Value

n Assume now that a catastrophe wipes out half the value of this firm (the value drops to \$ 50 million), while the face value of the debt remains at \$ 80 million. What will happen to the equity value of this firm? o It will drop in value to \$ 25.94 million [ \$ 50 million - market value of debt from previous page] o It will be worth nothing since debt outstanding > Firm Value o It will be worth more than \$ 25.94 million

## Illustration : Value of a troubled firm

n Assume now that, in the previous example, the value of the firm were reduced to \$ 50 million while keeping the face value of the debt at \$80 million. n This firm could be viewed as troubled, since it owes (at least in face value terms) more than it owns. n The equity in the firm will still have value, however.

## Valuing Equity in the Troubled Firm

- ■ Value of the underlying asset =  $S = \text{Value of the firm} = \$ 50 \text{ million}$
- ■ Exercise price =  $K = \text{Face Value of outstanding debt} = \$ 80 \text{ million}$
- ■ Life of the option =  $t = \text{Life of zero-coupon debt} = 10 \text{ years}$
- ■ Variance in the value of the underlying asset =  $\sigma^2 = \text{Variance in firm value} = 0.16$
- ■ Riskless rate =  $r = \text{Treasury bond rate corresponding to option life} = 10\%$

## The Value of Equity as an Option

n Based upon these inputs, the Black-Scholes model provides the following value for the call:

• 
$$d1 = 1.0515$$
       $N(d1) = 0.8534$ 

• 
$$d2 = -0.2135$$
       $N(d2) = 0.4155$ 

n Value of the call = 50 (0.8534) - 80 exp(-0.10)(10) (0.4155) = \$30.44 million

n Value of the bond= \$50 - \$30.44 = \$19.56 million

n The equity in this firm drops by, because of the option characteristics of equity.

n This might explain why stock in firms, which are in Chapter 11 and essentially bankrupt, still has value.

## Equity value persists ..

![](_page_240_Figure_1.jpeg)

## Valuing equity in a troubled firm

n The first implication is that **equity will have value**, even if the **value of the firm** falls well **below the face value of the outstanding debt**. n Such a firm will be viewed as **troubled** by investors, accountants and analysts, but that **does not mean that its equity is worthless**. n Just as deep out-of-the-money traded options command value because of the possibility that the value of the underlying asset may increase above the strike price in the remaining lifetime of the option, **equity will command value because of the time premium on the option** (the time until the bonds mature and come due) and the possibility that the value of the assets may increase above the face value of the bonds before they come due.

## The Conflict between bondholders and stockholders

- n Stockholders and bondholders have different objective functions, and this can lead to conflicts between the two. n For instance, stockholders have an incentive to take riskier projects than bondholders do, and to pay more out in dividends than bondholders would like them to. n This conflict between bondholders and stockholders can be illustrated dramatically using the option pricing model.
  - Since equity is a call option on the value of the firm, **an increase in the variance in the firm value, other things remaining equal, will lead to an increase in the value of equity**.
  - It is therefore conceivable that stockholders can take risky projects with **negative net present values**, which while making them better off, may make the bondholders and the firm less valuable. This is illustrated in the following example.

## Illustration: Effect on value of the conflict between stockholders and bondholders

- n Consider again the firm described in the earlier example , with a value of assets of \$100 million, a face value of zero-coupon ten-year debt of \$80 million, a standard deviation in the value of the firm of 40%. The equity and debt in this firm were valued as follows:
  - Value of Equity = \$75.94 million
  - Value of Debt = \$24.06 million
- Value of Firm == \$100 million n Now assume that the stockholders have the opportunity to take a project with a negative net present value of -\$2 million, but assume that this project is a very risky project that will push up the standard deviation in firm value to 50%.

## Valuing Equity after the Project

n Value of the underlying asset = S = Value of the firm = \$ 100 million - \$2 million = \$ 98 million (The value of the firm is lowered because of the negative net present value project) n Exercise price = K = Face Value of outstanding debt = \$ 80 million n Life of the option = t = Life of zero-coupon debt = 10 years n Variance in the value of the underlying asset = s2 = Variance in firm value = 0.25 n Riskless rate = r = Treasury bond rate corresponding to option life = 10%

## Option Valuation

#### n Option Pricing Results for Equity and Debt Value

- Value of Equity = \$77.71
- Value of Debt = \$20.29
- Value of Firm = \$98.00

n The value of equity rises from \$75.94 million to \$ 77.71 million , even though the firm value declines by \$2 million. The increase in equity value comes at the expense of bondholders, who find their wealth decline from \$24.06 million to \$20.19 million.

## Obtaining option pricing inputs - Some real world problems

- n The examples that have been used to illustrate the use of option pricing theory to value equity have made some simplifying assumptions. Among them are the following:
  - (1) There were only two claim holders in the firm debt and equity.
  - (2) There is only one issue of debt outstanding and it can be retired at face value.
  - (3) The debt has a zero coupon and no special features (convertibility, put clauses etc.)
  - (4) The value of the firm and the variance in that value can be estimated.

## Real World Approaches to Getting inputs

| Input                  | Estimation Process                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Value of the Firm      | <ul> <li>Cumulate market values of equity and debt (or)</li> <li>Value the <u>assets in place</u> using FCFF and WACC (or)</li> <li>Use cumulated market value of assets, if traded.</li> </ul>                                                                                                                                                                                                                                                                                                                                                       |
| Variance in Firm Value | <ul> <li>If stocks and bonds are traded,<br/> <math>\sigma^2_{\text{firm}} = w_e^2 \sigma_e^2 + w_d^2 \sigma_d^2 + 2 w_e w_d \rho_{ed} \sigma_e \sigma_d</math><br/> where <math>\sigma_e^2</math> = variance in the stock price<br/> <math>w_e</math> = MV weight of Equity<br/> <math>\sigma_d^2</math> = the variance in the bond price      <math>w_d</math> = MV weight of debt</li> <li>If not traded, use variances of similarly rated bonds.</li> <li>Use average firm value variance from the industry in which company operates.</li> </ul> |
| Value of the Debt      | <ul> <li>If the debt is short term, you can use only the face or book value of the debt.</li> <li>If the debt is long term and coupon bearing, add the cumulated nominal value of these coupons to the face value of the debt.</li> </ul>                                                                                                                                                                                                                                                                                                             |
| Maturity of the Debt   | <ul> <li>Face value weighted duration of bonds outstanding (or)</li> <li>If not available, use weighted maturity</li> </ul>                                                                                                                                                                                                                                                                                                                                                                                                                           |

#### Valuing Equity as an option - Eurotunnel in early 1998

- n Eurotunnel has been a financial disaster since its opening
  - In 1997, Eurotunnel had earnings before interest and taxes of -£56 million and net income of -£685 million
- At the end of 1997, its book value of equity was -£117 million n It had £8,865 million in face value of debt outstanding
  - The weighted average duration of this debt was 10.93 years Debt Type Face Value Duration Short term 935 0.50 10 year 2435 6.7 20 year 3555 12.6 Longer 1940 18.2 *Total £8,865 mil 10.93 years*

#### The Basic DCF Valuation

- n The value of the firm estimated using projected cashflows to the firm, discounted at the weighted average cost of capital was £2,312 million. n This was based upon the following assumptions –
  - Revenues will grow 5% a year in perpetuity.
  - The COGS which is currently 85% of revenues will drop to 65% of revenues in yr 5 and stay at that level.
  - Capital spending and depreciation will grow 5% a year in perpetuity.
  - There are no working capital requirements.
  - The debt ratio, which is currently 95.35%, will drop to 70% after year 5. The cost of debt is 10% in high growth period and 8% after that.
  - The beta for the stock will be 1.10 for the next five years, and drop to 0.8 after the next 5 years.
  - The long term bond rate is 6%.

#### Other Inputs

- n The stock has been traded on the London Exchange, and the annualized std deviation based upon ln (prices) is 41%. n There are Eurotunnel bonds, that have been traded; the annualized std deviation in ln(price) for the bonds is 17%.
  - The correlation between stock price and bond price changes has been 0.5. The proportion of debt in the capital structure during the period (1992-1996) was 85%.
- Annualized variance in firm value = (0.15)<sup>2</sup> (0.41)<sup>2</sup> + (0.85)<sup>2</sup> (0.17)<sup>2</sup> + 2 (0.15) (0.85)(0.5)(0.41)(0.17)= 0.0335 n The five-year bond rate is 6%.

#### Valuing Eurotunnel Equity and Debt

#### n Inputs to Model

- Value of the underlying asset = S = Value of the firm = £2,312 million
- Exercise price = K = Face Value of outstanding debt = £8,865 million
- Life of the option = t = Weighted average duration of debt = 10.93 years
- Variance in the value of the underlying asset =  $\sigma^2 = \text{Variance in firm value} = 0.0335$
- Riskless rate = r = Treasury bond rate corresponding to option life = 6%

n Based upon these inputs, the Black-Scholes model provides the following value for the call:

$$d1 = -0.8337$$
       $N(d1) = 0.2023$ 

$$d2 = -1.4392$$
       $N(d2) = 0.0751$ 

n Value of the call = 2312 (0.2023) - 8,865 exp(-0.06)(10.93) (0.0751) = £122 million n Appropriate interest rate on debt = (8865/2190)(1/10.93)-1= 13.65%

| <i>Industry Name</i>     | <i>Std Dev(Equity)</i> | <i>Std Dev(Firm)</i> | <i>Industry Name</i>      | <i>Std Dev(Equity)</i> | <i>Std Dev(Firm)</i> |
|--------------------------|------------------------|----------------------|---------------------------|------------------------|----------------------|
| Advertising              | 35.48%                 | 27.11%               | Household Products        | 29.40%                 | 24.91%               |
| Aerospace/Defense        | 37.40%                 | 33.13%               | Industrial Services       | 43.95%                 | 39.62%               |
| Air Transport            | 44.52%                 | 33.80%               | Insurance (Diversified)   | 28.46%                 | 26.99%               |
| Aluminum                 | 29.20%                 | 22.05%               | Insurance (Life)          | 30.61%                 | 29.15%               |
| Apparel                  | 45.25%                 | 37.34%               | Insurance (Prop/Casualty) | 26.98%                 | 25.68%               |
| Auto & Truck             | 31.01%                 | 23.90%               | Investment Co. (Domestic) | 23.40%                 | 22.28%               |
| Auto Parts (OEM)         | 31.21%                 | 26.63%               | Investment Co. (Foreign)  | 28.01%                 | 27.91%               |
| Auto Parts (Replacement) | 33.28%                 | 25.71%               | Investment Co. (Income)   | 10.95%                 | 10.95%               |
| <b>Bank</b>              | <b>24.44%</b>          | <b>22.44%</b>        | <b>Machinery</b>          | <b>35.25%</b>          | <b>30.94%</b>        |
| Bank (Canadian)          | 21.18%                 | 19.12%               | Manuf. Housing/Rec Veh    | 41.09%                 | 36.00%               |
| Bank (Foreign)           | 23.12%                 | 22.39%               | Maritime                  | 33.85%                 | 24.38%               |
| Bank (Midwest)           | 20.13%                 | 19.15%               | Medical Services          | 63.58%                 | 55.77%               |
| Beverage (Alcoholic)     | 22.21%                 | 20.24%               | Medical Supplies          | 54.33%                 | 50.44%               |
| Beverage (Soft Drink)    | 37.59%                 | 32.50%               | Metal Fabricating         | 35.61%                 | 32.85%               |
| Building Materials       | 35.68%                 | 31.08%               | Metals & Mining (Div.)    | 55.48%                 | 50.20%               |
| Cable TV                 | 41.41%                 | 21.67%               | Natural Gas (Distrib.)    | 19.35%                 | 15.23%               |
| Canadian Energy          | 25.24%                 | 21.41%               | Natural Gas (Diversified) | 33.69%                 | 28.21%               |
| Cement & Aggregates      | 32.83%                 | 29.86%               | Newspaper                 | 23.54%                 | 19.99%               |
| Chemical (Basic)         | 29.43%                 | 25.16%               | Office Equip & Supplies   | 34.40%                 | 29.32%               |
| Chemical (Diversified)   | 30.87%                 | 27.01%               | Oilfield Services/Equip.  | 43.25%                 | 39.70%               |
| Chemical (Specialty)     | 33.74%                 | 29.34%               | Packaging & Container     | 37.44%                 | 30.32%               |
| Coal/Alternate Energy    | 40.48%                 | 34.85%               | Paper & Forest Products   | 28.41%                 | 17.50%               |
| Computer & Peripherals   | 64.64%                 | 59.54%               | Petroleum (Integrated)    | 25.66%                 | 20.98%               |
| Computer Software & Svcs | 52.88%                 | 50.35%               | Petroleum (Producing)     | 49.32%                 | 42.47%               |
| Copper                   | 30.41%                 | 12.62%               | Precision Instrument      | 47.36%                 | 44.21%               |
| Diversified Co.          | 42.82%                 | 35.20%               | Publishing                | 35.89%                 | 30.75%               |
| Drug                     | 59.77%                 | 58.50%               | R.E.I.T.                  | 25.06%                 | 24.52%               |
| Drugstore                | 47.64%                 | 36.63%               | Railroad                  | 23.73%                 | 19.37%               |
| Electric Util. (Central) | 14.93%                 | 11.38%               | Recreation                | 50.25%                 | 39.58%               |
| Electric Utility (East)  | 16.56%                 | 11.67%               | Restaurant                | 40.12%                 | 35.55%               |
| Electric Utility (West)  | 18.18%                 | 13.80%               | Retail (Special Lines)    | 51.20%                 | 39.98%               |
| Electrical Equipment     | 43.70%                 | 39.49%               | Retail Building Supply    | 40.55%                 | 33.95%               |
| Electronics              | 53.39%                 | 48.39%               | Retail Store              | 40.14%                 | 29.46%               |
| Entertainment            | 36.01%                 | 28.95%               | Securities Brokerage      | 33.42%                 | 22.74%               |
| Environmental            | 53.98%                 | 43.74%               | Semiconductor             | 54.64%                 | 52.72%               |
| Financial Services       | 36.16%                 | 27.68%               | Semiconductor Cap Equip   | 53.41%                 | 52.50%               |
| Food Processing          | 33.13%                 | 26.83%               | Shoe                      | 44.63%                 | 40.08%               |
| Food Wholesalers         | 27.60%                 | 22.11%               | Steel (General)           | 33.73%                 | 28.96%               |
| Foreign Diversified      | 91.01%                 | 44.08%               | Steel (Integrated)        | 40.34%                 | 27.69%               |
| Foreign Electron/Entertn | 34.03%                 | 29.17%               | Telecom. Equipment        | 61.61%                 | 56.72%               |
| Foreign Telecom.         | 36.18%                 | 32.99%               | Telecom. Services         | 42.29%                 | 35.05%               |
| Furn./Home Furnishings   | 34.62%                 | 30.90%               | Textile                   | 31.60%                 | 24.12%               |
| Gold/Silver Mining       | 49.57%                 | 46.46%               | Thrift                    | 28.94%                 | 26.42%               |
| Grocery                  | 31.64%                 | 21.84%               | Tire & Rubber             | 26.39%                 | 23.60%               |
| Healthcare Info Systems  | 57.80%                 | 54.69%               | Tobacco                   | 33.85%                 | 25.31%               |
| Home Appliance           | 34.82%                 | 29.48%               | Toiletries/Cosmetics      | 42.97%                 | 36.82%               |
| Homebuilding             | 43.66%                 | 27.13%               | Trucking/Transp. Leasing  | 38.09%                 | 29.21%               |
| Hotel/Gaming             | 45.01%                 | 29.76%               | Utility (Foreign)         | 23.17%                 | 18.34%               |
|                          |                        |                      | Water Utility             | 18.53%                 | 14.16%               |