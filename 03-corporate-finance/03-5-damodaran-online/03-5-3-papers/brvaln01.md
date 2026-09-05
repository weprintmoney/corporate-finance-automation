---
title: "Brvaln01"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/country/Brvaln01.pdf
---

# Valuation

Aswath Damodaran

Home Page: http://www.stern.nyu.edu/~adamodar

Email: adamodar@stern.nyu.edu

This presentation is under seminars.

![](_page_1_Picture_3.jpeg)

### Some Initial Thoughts

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

#### Generic DCF Valuation Model

![](_page_7_Diagram_2.jpeg)

#### DISCOUNTED CASHFLOW VALUATION

![](_page_8_Diagram_1.jpeg)

#### DISCOUNTED CASHFLOW VALUATION

![](_page_9_Diagram_1.jpeg)

#### Embraer: Status Quo

![](_page_10_Diagram_1.jpeg)

#### **Discounted Cash Flow Valuation: High Growth with Negative Earnings**

![](_page_11_Diagram_0.jpeg)

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

### Short term Governments are not risk free

- n On a riskfree asset, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. n For an investment to be riskfree, then, it has to have
  - No default risk
- No reinvestment risk n Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time n A simpler approach is to match the duration of the analysis (generally long term) to the duration of the riskfree rate (also long term) n In emerging markets, there are two problems:
  - The government might not be viewed as riskfree (Brazil, Indonesia)
  - There might be no market-based long term government rate (China)

### Estimating a Riskfree Rate

- n Estimate a range for the riskfree rate in local currency terms:
  - *Upper limit*: Obtain the rate at which the largest, safest firms in the country borrow at and use as the upper limit of the riskfree rate.
- *Lower limit*: Use a local bank deposit rate as the lower limit of the riskfree rate n Do the analysis in real terms (rather than nominal terms) using a real riskfree rate, which can be obtained in one of two ways –
  - from an inflation-indexed government bond, if one exists
- set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done. n Do the analysis in another more stable currency, say US dollars.

### A Simple Test

n You are valuing a Brazilian company in U.S. dollars and are attempting to estimate a risk free rate to use in the analysis. The risk free rate that you should use is o The interest rate on a nominal BR Brazilian government bond o The interest rate on a dollar-denominated Brazilian government bond o The interest rate on a US treasury bond

### A Real Riskfree Rate for valuing Embraer

#### n Nominal BR riskfree rate:

- Based upon the prime rate and CD rates: 15%

#### n Real BR riskfree rate

- The real riskfree rate, estimated using the inflation-indexed US treasury bond, is about 3%.
- Real rates in Brazil are much higher. Some of this can be attributed to perceived risk (which we should not be considering in the riskfree rate) and some of this can be attributed to constraints on capital flowing freely between markets.
- I will use 4.5% as my long term real riskfree rate. This is my estimate of the expected long term real growth in the Brazilian economy.
- This assumption is, in a sense, self correcting. If I have under estimated growth, I have also underestimated my discount rate as well.

#### n Dollar based riskfree rate:

- US treasury bond rate of 5.1%.

### Everyone uses historical premiums, but..

- n The historical premium is the premium that stocks have historically earned over riskless securities. n Practitioners never seem to agree on the premium; it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. n For instance, looking at the US:

| Historical period | Arith  | Stocks - T.Bills Geom | Arith  | Stocks - T.Bonds Geom |
|-------------------|--------|-----------------------|--------|-----------------------|
| 1928-2000         | 8.41%  | 7.17%                 | 6.64%  | 5.59%                 |
| 1962-2000         | 6.42%  | 5.25%                 | 5.31%  | 4.52%                 |
| 1990-2000         | 11.31% | 8.35%                 | 12.67% | 8.91%                 |

### If you choose to use historical premiums….

n Go back as far as you can. A risk premium comes with a standard error. Given the annual standard deviation in stock prices is about 25%, the standard error in a historical premium estimated over 25 years is roughly:

Standard Error in Premium = 
$$25\%/\sqrt{25} = 25\%/5 = 5\%$$

n Be consistent in your use of the riskfree rate. Since we argued for long term bond rates, the premium should be the one over T.Bonds n Use the geometric risk premium. It is closer to how investors think about risk premiums over long periods.

### Assessing Country Risk Using Country Ratings: Latin America

| Country   | Rating | Typical Spread | Market Spread |
|-----------|--------|----------------|---------------|
| Argentina | B1     | 450            | 563           |
| Bolivia   | B1     | 450            | 551           |
| Brazil    | B1     | 450            | 537           |
| Colombia  | Ba2    | 300            | 331           |
| Ecuador   | Caa2   | 750            | 787           |
| Guatemala | Ba2    | 300            | 361           |
| Honduras  | B2     | 550            | 581           |
| Mexico    | Baa3   | 145            | 235           |
| Paraguay  | B2     | 550            | 601           |
| Peru      | Ba3    | 400            | 455           |
| Uruguay   | Baa3   | 145            | 193           |
| Venezuela | B2     | 550            | 631           |

### Using Country Ratings to Estimate Equity Spreads

- n Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
  - One way to adjust the country spread upwards is to use information from the US market. In the US, the equity risk premium has been roughly twice the default spread on junk bonds.
  - Another is to multiply the bond spread by the relative volatility of stock and bond prices in that market. For example,
    - Standard Deviation in Bovespa (Equity) = 32.6%
    - Standard Deviation in Brazil C-Bond = 17.1%
- Adjusted Equity Spread = 5.37% (32.6/17.1%) = 10.24% n Ratings agencies make mistakes. They are often late in recognizing and building in risk.

### From Country Spreads to Corporate Risk premiums

n Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country Spread} + \text{Beta (US premium)}$$

Implicitly, this is what you are assuming when you use the local Government's dollar borrowing rate as your riskfree rate.

n Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium} + \text{Country Spread})$$

n Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium})+\lambda (\text{Country Spread})$$

### Estimating Company Exposure to Country Risk

n Different companies should be exposed to different degrees to country risk. For instance, a Brazilian firm that generates the bulk of its revenues in the United States should be less exposed to country risk in Brazil than one that generates all its business within Brazil.

■ The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following:

$$\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{avg firm}}$$

For instance, if a firm gets 35% of its revenues domestically while the average firm in that market gets 70% of its revenues domestically

l = 35%/ 70 % = 0.5

- n There are two implications
  - A company's risk exposure is determined by where it does business and not by where it is located
  - Firms might be able to actively manage their country risk exposures

### Estimating E(Return) for Embraer

<sup>n</sup> Assume that the beta for Embraer is 0.88, and that the riskfree rate used is 4.5%. (Real Riskfree Rate) <sup>n</sup> Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

E(Return) =4.5% + 10.24% + 0.88 (5.59%) = 19.66%

<sup>n</sup> Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

E(Return) = 4.5% + 0.88 (5.59%+ 9.69%) = 18.43%

<sup>n</sup> Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

E(Return)= 4.5% + 0.88(5.59%) + 0.50 (10.24%) = 14.54%

Embraer is less exposed to country risk than the typical Brazilian firm since much of its business is overseas.

#### Implied Equity Premiums

- n If we use a basic discounted cash flow model, we can estimate the implied risk premium from the current level of stock prices. n For instance, if stock prices are determined by the simple Gordon Growth Model:
  - Value = Expected Dividends next year/ (Required Returns on Stocks Expected Growth Rate)
- Plugging in the current level of the index, the dividends on the index and expected growth rate will yield a "implied" expected return on stocks. Subtracting out the riskfree rate will yield the implied premium. n The problems with this approach are:
  - the discounted cash flow model used to value the stock index has to be the right one.
  - the inputs on dividends and expected growth have to be correct
  - it implicitly assumes that the market is currently correctly valued

#### **Implied Premium for US Equity Market**

![](_page_25_Figure_1.jpeg)

### Implied Premium for Brazilian Market: March 1, 2001

- n Level of the Index = 16417 n Dividends on the Index = 4.40% of (Used weighted yield) n Other parameters
  - Riskfree Rate = 4.5% (real riskfree rate)
  - Expected Growth
    - Next 5 years = 13.5% (Used expected real growth rate in Earnings)
- After year 5 = 4.5% (real growth rate in long term) n Solving for the expected return:
  - Expected return on Equity = 11.16%
  - Implied Equity premium = 11.16% -4. 5% = 6.66%

### The Effect of Using Implied Equity Premiums on Value

n Embraer's value per share (using historical premium + country risk adjustment) = 11.22 BR n Embraer's value per share (using implied equity premium of 6.66%) = 20.02 BR n Embraer's stock price (at the time of the valuation) = 15.25 BR

### An Intermediate Solution

- n The historical risk premium of 5.59% for the United States is too high a premium to use in valuation. It is
  - As high as the highest implied equity premium that we have ever seen in the US market (making your valuation a worst case scenario)
- Much higher than the actual implied equity risk premium in the market n The current implied equity risk premium is too low because
- It is lower than the equity risk premiums in the 60s, when inflation and interest rates were as low n The average implied equity risk premium between 1960-2000 in the United States is about 4%. We will use this as the premium for a mature equity market.

### Estimating Beta

<sup>n</sup> The standard procedure for estimating betas is to regress stock returns (R<sup>j</sup> ) against market returns (Rm) -

$$R_j = a + b R_m$$

- where a is the intercept and b is the slope of the regression.

n The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.

n This beta has three problems:

- It has high standard error
- It reflects the firm's business mix over the period of the regression, not the current mix
- It reflects the firm's average financial leverage over the period rather than the current leverage.

#### Beta Estimation for Amazon: The Noise Problem

![](_page_30_Figure_1.jpeg)

# Beta Estimation: The Index Effect

## HISTORICAL BETA

**EMBR3 BZ Equity**  
 Relative Index **IBOV**  
 Period **[ Weekly ]**  
 Range **3/12/99 To 3/ 2/01**  
 Market **[ Trade ]**

| <b>ADJ BETA</b>   | 0.73  |
|-------------------|-------|
| <b>RAW BETA</b>   | 0.60  |
| Alpha(Intercept)  | 2.93  |
| R2 (Correlation)  | 0.06  |
| Std Dev of Error  | 11.12 |
| Std Error of Beta | 0.24  |
| Number of Points  | 103   |

$$\text{ADJ BETA} = (0.67) * \text{RAW BETA} + (0.33) * 1.0$$

Copyright 2001 BLOOMBERG L.P. Frankfurt:69-920410 Hong Kong:2-977-6000 London:207-330-7500 New York:212-318-2000  
 Princeton:609-279-3000 Singapore:65-212-1000 Sydney:2-9777-8686 Tokyo:3-3201-8900 Sao Paulo:11-3048-4500  
 1653-197-0 06-Mar-01 13:31:32

**EMPRESA BRAS DE AERONAUTICA**

**BRAZIL BOVESPA STOCK IDX**  
 \*Identifies latest observation

![](_page_31_Figure_26.jpeg)

<HELP> for explanation, <MENU> for similar functions.

**P059 Equity BETA**

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

- It has lower standard error ( $SE_{\text{average}} = SE_{\text{firm}} / \sqrt{n}$  ( $n$  = number of firms))
- It reflects the firm's current business mix and financial leverage
- It can be estimated for divisions and private firms.

$$\sum_{j=1}^{j=k} \beta_j \left[ \frac{\text{Operating Income}_j}{\text{Operating Income}_{\text{Firm}}} \right]$$

$$\beta_{\text{levered}} = \beta_{\text{unlevered}}[1 + (1 - \text{tax rate}) (\text{Current Debt/Equity Ratio})]$$

### Embraer's Bottom-up Beta

| <i>Business</i> | <i>Unlevered</i>                                    | <i>D/E Ratio</i> | <i>Levered</i> | <i>Proportion of</i> |
|-----------------|-----------------------------------------------------|------------------|----------------|----------------------|
|                 | <i>Beta</i>                                         |                  | <i>Beta</i>    | <i>Value</i>         |
| Aerospace       | 0.87                                                | 2.45%            | 0.88           | 100%                 |
| Levered Beta    | = Unlevered Beta ( 1 + (1 - tax rate) (D/E Ratio) ) |                  |                |                      |
|                 | = 0.87 ( 1 + (1 -.33) (.0245)) = 0.88               |                  |                |                      |

Notes on calculating debt to equity ratio

Market value was used for equity

Net debt was used to compute the debt to equity ratio

#### Amazon's Bottom-up Beta

Unlevered beta for firms in internet retailing = 1.60

Unlevered beta for firms in specialty retailing = 1.00

<sup>n</sup> Amazon is a specialty retailer, but its risk currently seems to be determined by the fact that it is an online retailer. Hence we will use the beta of internet companies to begin the valuation but move the beta, after the first five years, towards to beta of the retailing business. <sup>n</sup> What would the betas that you would move the following internet firms towards?

#### Cost of Debt

- n If the firm has bonds outstanding, and the bonds are traded, the yield to maturity on a long-term, straight (no special features) bond can be used as the interest rate. n If the firm is rated, use the rating and a typical default spread on bonds with that rating to estimate the cost of debt. n If the firm is not rated,
  - and it has recently borrowed long term from a bank, use the interest rate on the borrowing or
- estimate a synthetic rating for the company, and use the synthetic rating to arrive at a default spread and a cost of debt n The cost of debt has to be estimated in the same currency as the cost of equity and the cash flows in the valuation.

### Defining Debt

- n Debt should include all interest-bearing obligations short term as well as long term. n In addition, the present value of commitments - such as operating leases should be treated as debt. n You can use either gross debt (total debt outstanding) or net debt (net out cash and marketable securities from debt) but you have to be consistent.
  - If you use gross debt, you consider total interest expenses and all debt ratios used (to compute levered beta and cost of capital) are gross debt ratios.
  - If you use net debt, you consider net interest expenses and all debt ratios used are net debt ratios. (As a caveat, if the net debt is negative, set it to zero and consider the excess cash and marketable securities separately)

### Estimating Synthetic Ratings

n The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

n For Embraer's interest coverage ratio, we used the net interest expenses (rather than total interest expenses)

Interest coverage ratio for Embraer = 810/28.2 = 28.73

- Amazon.com has negative operating income; this yields a negative interest coverage ratio, which should suggest a low rating. We computed an average interest coverage ratio of 2.82 over the next 5 years.

### Interest Coverage Ratios, Ratings and Default Spreads

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

### Estimating the cost of debt for a firm

<sup>n</sup> The synthetic rating for Embraer is A. The default spread is 1.00%. We also add the country default spreadof 4.83% to the cost of debt (sovereign ceiling effect).

Pre-tax Cost of Debt

= Riskfree Rate + Country default spread + Company Default Spread = 4.5% + 4.83% + 1.00% = 10.33%

<sup>n</sup> The synthetic rating for Amazon.com is BBB. The default spread for AAA rated bond is 1.50%

Pre-tax cost of debt = Riskfree Rate + Default spread = 6.50% + 1.50% = 8.00%

- After-tax cost of debt right now = 8.00% (1- 0) = 8.00%: The firm is paying no taxes currently. As the firm's tax rate changes and its cost of debt changes, the after tax cost of debt will change as well.

|           | 1     | 2     | 3     | 4      | 5     | 6     | 7     | 8     | 9     | 10    |
|-----------|-------|-------|-------|--------|-------|-------|-------|-------|-------|-------|
| Pre-tax   | 8.00% | 8.00% | 8.00% | 8.00%  | 8.00% | 7.80% | 7.75% | 7.67% | 7.50% | 7.00% |
| Tax rate  | 0%    | 0%    | 0%    | 16.13% | 35%   | 35%   | 35%   | 35%   | 35%   | 35%   |
| After-tax | 8.00% | 8.00% | 8.00% | 6.71%  | 5.20% | 5.07% | 5.04% | 4.98% | 4.88% | 4.55% |

### Weights for the Cost of Capital Computation

n The weights used to compute the cost of capital should be the market value weights for debt and equity. n There is an element of circularity that is introduced into every valuation by doing this, since the values that we attach to the firm and equity at the end of the analysis are different from the values we gave them at the beginning. n As a general rule, the debt that you should subtract from firm value to arrive at the value of equity should be the same debt that you used to compute the cost of capital.

### Book Value versus Market Value Weights

n It is often argued that using book value weights is more conservative than using market value weights. Do you agree? o Yes o No n It is also often argued that book values are more reliable than market values since they are not as volatile. Do you agree? o Yes o No

#### Current Cost of Capital: Embraer

#### n Equity

- Cost of Equity = 5.1% + 0.88 (14.24%) = 17.63%
- Market Value of Equity = 595.69\*15.25 \$9,084 million
- Equity/(Debt+Equity ) = 97.6%

#### n Debt

- After-tax Cost of debt = 10.67% (1-.33) = 7.15%
- Market Value of Debt = \$ 223 million
- Debt/(Debt +Equity) = 2.4%

n Cost of Capital = 17.03%(.976)+6.75%(.024) = 16.78%

#### Estimating Cost of Capital: Amazon.com

#### n Equity

- Cost of Equity = 6.50% + 1.60 (4.00%) = 12.90%
- Market Value of Equity = \$ 84/share\* 340.79 mil shs = \$ 28,626 mil (98.8%)

#### n Debt

- Cost of debt = 6.50% + 1.50% (default spread) = 8.00%
- Market Value of Debt = \$ 349 mil (1.2%)

#### n Cost of Capital

Cost of Capital = 12.9 % (.988) + 8.00% (1- 0) (.012)) = 12.84%

### Amazon.com: Book Value Weights

n Amazon.com has a book value of equity of \$ 138 million and a book value of debt of \$ 349 million. Estimate the cost of capital using book value weights instead of market value weights. n Is this more conservative?

### II. Estimating Cash Flows to Firm

EBIT ( 1 - tax rate)

+ Depreciation

- Capital Spending

- Change in Working Capital

= Cash flow to the firm

### What is the EBIT of a firm?

n The EBIT, measured right, should capture the true operating income from assets in place at the firm. n Any expense that is not an operating expense or income that is not an operating income should not be used to compute EBIT. In other words, any financial expense (like interest expenses) or capital expenditure should not affect your operating income.

### Calendar Years, Financial Years and Updated Information

n The operating income and revenue that we use in valuation should be updated numbers. One of the problems with using financial statements is that they are dated. n As a general rule, it is better to use 12-month trailing estimates for earnings and revenues than numbers for the most recent financial year. This rule becomes even more critical when valuing companies that are evolving and growing rapidly.

|          | Last 10-K       | Trailing 12-month |
|----------|-----------------|-------------------|
| Revenues | \$ 610 million  | \$1,117 million   |
| EBIT     | - \$125 million | - \$ 410 million  |

### Normalizing EBIT

#### n Normalizing Current Earnings

- Use average earnings over a prior time period (last 3 or 5 years) instead of the current earnings. {Works best for companies that have stayed the same size over time}
- Use average operating margin earned by the firm over a prior time period to normalize earnings:

Normalized EBIT = Current Revenues \* Average Margin

- Use industry average operating margin on current revenues of the firm

#### n Normalize Future Earnings

- Keep current operating income but change margins over time to move towards a target margin (industry average, for instance)

### Normalizing Amazon's EBIT

| Year   | Revenues | Operating Margin | EBIT                     |
|--------|----------|------------------|--------------------------|
| Tr12m  | \$1,117  | -36.71%          | -\$410                   |
| 1      | \$2,793  | -13.35%          | -\$373                   |
| 2      | \$5,585  | -1.68%           | -\$94                    |
| 3      | \$9,774  | 4.16%            | \$407                    |
| 4      | \$14,661 | 7.08%            | \$1,038                  |
| 5      | \$19,059 | 8.54%            | \$1,628                  |
| 6      | \$23,862 | 9.27%            | \$2,212                  |
| 7      | \$28,729 | 9.64%            | \$2,768                  |
| 8      | \$33,211 | 9.82%            | \$3,261                  |
| 9      | \$36,798 | 9.91%            | \$3,646                  |
| 10     | \$39,006 | 9.95%            | \$3,883                  |
| TY(11) | \$41,346 | 10.00%           | \$4,135 Industry Average |

### Operating Lease Expenses: Operating or Financing Expenses

- n Operating Lease Expenses are treated as operating expenses in computing operating income. In reality, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital:
- Debt Value of Operating Leases = PV of Operating Lease Expenses at the pre-tax cost of debt n Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

#### Operating Leases at The Home Depot in 1998

n The pre-tax cost of debt at the Home Depot is 6.25% Yr Operating Lease Expense Present Value 1 \$ 294 \$ 277 2 \$ 291 \$ 258 3 \$ 264 \$ 220 4 \$ 245 \$ 192 5 \$ 236 \$ 174 6-15 \$ 270 \$ 1,450 (PV of 10-yr annuity) Present Value of Operating Leases =\$ 2,571 n Debt outstanding at the Home Depot = \$1,205 + \$2,571 = \$3,776 mil (The Home Depot has other debt outstanding of \$1,205 million) n Adjusted Operating Income = \$2,016 + 2,571 (.0625) = \$2,177 mil

### R&D Expenses: Operating or Capital Expenses

- n Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. n To capitalize R&D,
  - Specify an amortizable life for R&D (2 10 years)
  - Collect past R&D expenses for as long as the amortizable life
  - Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

### Capitalizing R&D Expenses: Compaq

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

### Should we capitalize advertising and selling expenses?

- n Many brand name companies can argue that a portion of their advertising is designed to augment the value of their brand names rather than sell products today.
- Should a portion of Brahma's advertising expenses be treated as capital expenses? n Many internet companies are arguing that selling and G&A expenses are the equivalent of R&D expenses for a high-technology firms and should be treated as capital expenditures.If we adopt this rationale, we should be computing earnings before these expenses, which will make many of these firms profitable. It will also mean that they are reinvesting far more than we think they are. It will, however, make not their cash flows less negative.
  - Should Amazon.com's selling expenses be treated as cap ex?

### What tax rate?

n The tax rate that you should use in computing the after-tax operating income should be o The effective tax rate in the financial statements (taxes paid/Taxable income) o The tax rate based upon taxes paid and EBIT (taxes paid/EBIT) o The marginal tax rate o None of the above o Any of the above, as long as you compute your after-tax cost of debt using the same tax rate

### The Right Tax Rate to Use

n The choice really is between the effective and the marginal tax rate. In doing projections, it is far safer to use the marginal tax rate since the effective tax rate is really a reflection of the difference between the accounting and the tax books. n By using the marginal tax rate, we tend to understate the after-tax operating income in the earlier years, but the after-tax tax operating income is more accurate in later years n If you choose to use the effective tax rate, adjust the tax rate towards the marginal tax rate over time. n The tax rate used to compute the after-tax cost of debt has to be the same tax rate that you use to compute the after-tax operating income.

### Amazon.com's Tax Rate

| Year      | 1      | 2     | 3     | 4       | 5       |
|-----------|--------|-------|-------|---------|---------|
| EBIT      | -\$373 | -\$94 | \$407 | \$1,038 | \$1,628 |
| Taxes     | \$0    | \$0   | \$0   | \$167   | \$570   |
| EBIT(1-t) | -\$373 | -\$94 | \$407 | \$871   | \$1,058 |
| Tax rate  | 0%     | 0%    | 0%    | 16.13%  | 35%     |
| NOL       | \$500  | \$873 | \$967 | \$560   | \$0     |

After year 5, the tax rate becomes 35%.

### Net Capital Expenditures

n Net capital expenditures represent the difference between capital expenditures and depreciation. Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures. n In general, the net capital expenditures will be a function of how fast a firm is growing or expecting to grow. High growth firms will have much higher net capital expenditures than low growth firms. n Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

### Net Capital expenditures should include

n Research and development expenses, once they have been re-categorized as capital expenses. The adjusted cap ex will be

Adjusted Net Capital Expenditures = Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset

n Acquisitions of other firms, since these are like capital expenditures. The adjusted cap ex will be

Adjusted Net Cap Ex = Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions

Two caveats:

- 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
- 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

### Embraer's Net Capital Expenditures

n In 2000, Embraer's net capital expenditures were \$ 36 million. n In 1999, Embraer had net capital expenditures of \$ 68 million. The net capital expenditures over the last 5 years have been as follows:

| <span></span> | <span></span> | <span></span> | <span></span> | <span></span> | <span></span> |
|---------------|---------------|---------------|---------------|---------------|---------------|
| Net Cap Ex    | \$59.41       | -\$29.38      | -\$16.38      | -\$5.60       | \$2.59        |

n While there has been no clear trend here, we will assume that Embraer will have to increase its reinvestment in future years.

### Working Capital Investments

n In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) n A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable) n Any investment in this measure of working capital ties up cash. Therefore, any increases (decreases) in working capital will reduce (increase) cash flows in that period. n When forecasting future growth, it is important to forecast the effects of such growth on working capital needs, and building these effects into the cash flows.

### Estimating Working Capital Needs: Embraer and Amazon

#### n Embraer

- Change in non-cash working capital in 2000 = \$ 610 million
- Non-cash Working Capital as percent of revenues in 2000 = 20%
- Non-cash working capital in future years assumed to be 20% of change in revenues in those years.

#### n Amazon

- Non-cash working capital has been negative each year since its inception.
- As firm gets larger, we will assume that it will have to maintain a non-cash working capital investment of 3%. This is about one-third of the non-cash working capital investment at brick and mortar retail stores.

### Estimating FCFF: Embraer

n EBIT = \$ 810 n Tax rate = 33% (marginal) n Net Capital expenditures = \$ 106 million n Increase in Non-cash Working Capital = 20%of Change in revenues in 2000= .20 (4560-3366) = \$ 240 million (Normalized)

#### *Estimating FCFF*

| Current EBIT * (1 - tax rate) =     | 810 (1-.33) = | \$ 543 |
|-------------------------------------|---------------|--------|
| - (Capital Spending - Depreciation) |               | \$ 36  |
| - Change in Working Capital         |               | \$ 240 |
| Current FCFF                        |               | \$ 267 |

### Estimating FCFF: Amazon.com

- n EBIT (Trailing 1999) = -\$ 410 million n Tax rate used = 0% (Assumed Effective = Marginal) n Capital spending (Trailing 1999) = \$ 243 million n Depreciation (Trailing 1999) = \$ 31 million n Non-cash Working capital Change (1999) = - 80 million n Estimating FCFF (1999) Current EBIT \* (1 - tax rate) = - 410 (1-0) = - \$410 million
  - (Capital Spending Depreciation) = \$212 million
  - Change in Working Capital = -\$ 80 million Current FCFF = - \$542 million With normalized working capital at 3% of revenues, Current FCFF = -\$ 640 million

### IV. Estimating Growth

n When valuing firms, some people use analyst projections of earnings growth (over the next 5 years) that are widely available in Zacks, I/B/E/S or First Call in the US, and less so overseas. This practice is o Fine. Equity research analysts follow these stocks closely and should be pretty good at estimating growth o Shoddy. Analysts are not that good at projecting growth in earnings in the long term. o Wrong. Analysts do not project growth in operating earnings

### Expected Growth in EBIT and Fundamentals

n Reinvestment Rate and Return on Capital

| $g_{EBIT}$ | = (Net Capital Expenditures + Change in WC)/EBIT(1-t) * ROC |
|------------|-------------------------------------------------------------|
|            | = Reinvestment Rate * ROC                                   |

n **Proposition**: No firm can expect its operating income to grow over time without reinvesting some of the operating income in net capital expenditures and/or working capital. n **Proposition**: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.

#### Expected Growth and Embraer

■ 
$$\text{ROC} = \text{EBIT} (1 - \text{tax rate}) / (\text{BV of Net Debt} + \text{BV of Equity})_{\text{Last year}}$$
  
 $= 810 (1 - .33) / (773 + 697) = 36.94 \%$ 

**Expected ROC = Current**

n Reinv. Rate = (Net Cap Ex + Chg in WC)/EBIT (1-t) = (36+240)/ 810(1-.33) = 50.9%

**Expected Reinvestment rate = 40%**

n Expected Growth Rate = (.3697)\*(.40) = 14.78 %

n Since I used inflation adjusted numbers, this should be a real growth rate.

### Expected Growth and Amazon.com

n With negative operating income and a negative return on capital, the fundamental growth equation is of little use for Amazon.com n For Amazon, the effect of reinvestment shows up in revenue growth rates and changes in expected operating margins: Expected Revenue Growth = Reinvestment (in \$ terms) \* (Sales/ Capital) n The effect on expected margins is more subtle. Amazon's reinvestments (especially in acquisitions) may help create barriers to entry and other competitive advantages that will ultimately translate into high operating margins and high profits.

### Growth in Revenues, Earnings and Reinvestment: Amazon

|    | Year Growth | Revenue Chg in Revenue | Reinvestment | Chg Rev/ Chg Reinvestment | ROC     |
|----|-------------|------------------------|--------------|---------------------------|---------|
| 1  | 150.00%     | \$1,676                | \$559        | 3.00                      | -76.62% |
| 2  | 100.00%     | \$2,793                | \$931        | 3.00                      | -8.96%  |
| 3  | 75.00%      | \$4,189                | \$1,396      | 3.00                      | 20.59%  |
| 4  | 50.00%      | \$4,887                | \$1,629      | 3.00                      | 25.82%  |
| 5  | 30.00%      | \$4,398                | \$1,466      | 3.00                      | 21.16%  |
| 6  | 25.20%      | \$4,803                | \$1,601      | 3.00                      | 22.23%  |
| 7  | 20.40%      | \$4,868                | \$1,623      | 3.00                      | 22.30%  |
| 8  | 15.60%      | \$4,482                | \$1,494      | 3.00                      | 21.87%  |
| 9  | 10.80%      | \$3,587                | \$1,196      | 3.00                      | 21.19%  |
| 10 | 6.00%       | \$2,208                | \$736        | 3.00                      | 20.39%  |

Assume that firm can earn high returns because of established economies of scale.

### Not all growth is equal: Disney versus Hansol Paper

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

![](_page_73_Figure_2.jpeg)

#### Determinants of Growth Patterns

#### n Size of the firm

- Success usually makes a firm larger. As firms become larger, it becomes much more difficult for them to maintain high growth rates

#### n Current growth rate

- While past growth is not always a reliable indicator of future growth, there is a correlation between current growth and future growth. Thus, a firm growing at 30% currently probably has higher growth and a longer expected growth period than one growing 10% a year now.

#### n Barriers to entry and differential advantages

- Ultimately, high growth comes from high project returns, which, in turn, comes from barriers to entry and differential advantages.
- The question of how long growth will last and how high it will be can therefore be framed as a question about what the barriers to entry are, how long they will stay up and how strong they will remain.

### Stable Growth Characteristics

- n In stable growth, firms should have the characteristics of other stable growth firms. In particular,
  - The risk of the firm, as measured by beta and ratings, should reflect that of a stable growth firm.
    - Beta should move towards one
    - The cost of debt should reflect the safety of stable firms (BBB or higher)
  - The debt ratio of the firm might increase to reflect the larger and more stable earnings of these firms.
    - The debt ratio of the firm might moved to the optimal or an industry average
    - If the managers of the firm are deeply averse to debt, this may never happen
  - The reinvestment rate of the firm should reflect the expected growth rate and the firm's return on capital
    - Reinvestment Rate = Expected Growth Rate / Return on Capital

### Embraer and Amazon.com: Stable Growth Inputs

High Growth Stable Growth

#### Embraer

| Beta                 | 0.88   | 0.90                       |
|----------------------|--------|----------------------------|
| Equity risk premium  | 14.24% | 9.37%                      |
| Debt Ratio           | 2.40%  | 2.40% (Should I increase?) |
| Return on Capital    | 36.94% | 15%                        |
| Expected Growth Rate | 14.78% | 4.5%                       |
| Reinvestment Rate    | 40%    | 4.5%/15% = 30%             |

#### Amazon.com

| Beta                 | 1.60     | 1.00         |
|----------------------|----------|--------------|
| Debt Ratio           | 1.20%    | 15%          |
| Return on Capital    | Negative | 20%          |
| Expected Growth Rate | NMF      | 6%           |
| Reinvestment Rate    | >100%    | 6%/20% = 30% |

### Dealing with Cash and Marketable Securities

- n If you use gross debt in your firm value calculations, the simplest and most direct way of dealing with cash and marketable securities is to keep it out of the valuation - the cash flows should be before interest income from cash and securities, and the discount rate should not be contaminated by the inclusion of cash. (Use betas of the operating assets alone to estimate the cost of equity). n If you use net debt, you have already considered cash and marketable securities in your calculations, and you should not add back cash and marketable securities. n Once the firm has been valued, add back the value of cash and marketable securities.
  - If you have a particularly incompetent management, with a history of overpaying on acquisitions, markets may discount the value of this cash.

### Dealing with Cross Holdings

n When the holding is a majority, active stake, the value that we obtain from the cash flows includes the share held by outsiders. While their holding is measured in the balance sheet as a minority interest, it is at book value. To get the correct value, we need to subtract out the estimated market value of the minority interests from the firm value. n When the holding is a minority, passive interest, the problem is a different one. The firm shows on its income statement only the share of dividends it receives on the holding. Using only this income will understate the value of the holdings. In fact, we have to value the subsidiary as a separate entity to get a measure of the market value of this holding. n Proposition 1: It is almost impossible to correctly value firms with minority, passive interests in a large number of private subsidiaries.

![](_page_79_Diagram_0.jpeg)

![](_page_80_Diagram_0.jpeg)

### Variations on DCF Valuation

- n A DCF valuation can be presented in two other formats:
  - In an adjusted present value (APV) valuation, the value of a firm can be broken up into its operating and leverage components separately Firm Value = Value of Unlevered Firm + (PV of Tax Benefits - Exp. Bankruptcy Cost)
- In an excess return model, the value of a firm can be written in terms of the existing capital invested in the firm and the present value of the excess returns that the firm will make on both existing assets and all new investments Firm Value = Capital Invested in Assets in Place + PV of Dollar Excess Returns on Assets in Place + PV of Dollar Excess Returns on All Future Investments n Done right, slicing a DCF valuation and presenting it differently should not change the value of the firm.

## Value Enhancement: Back to Basics

Aswath Damodaran

http://www.stern.nyu.edu/~adamodar

### Price Enhancement versus Value Enhancement

![](_page_83_Figure_1.jpeg)

### The Paths to Value Creation

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

### Value-Neutral Actions

- n Stock splits and stock dividends change the number of units of equity in a firm, but cannot affect firm value since they do not affect cash flows, growth or risk. n Accounting decisions that affect reported earnings but not cash flows should have no effect on value.
  - Changing inventory valuation methods from FIFO to LIFO or vice versa in financial reports but not for tax purposes
  - Changing the depreciation method used in financial reports (but not the tax books) from accelerated to straight line depreciation
  - Major non-cash restructuring charges that reduce reported earnings but are not tax deductible
- Using pooling instead of purchase in acquisitions cannot change the value of a target firm. n Decisions that create new securities on the existing assets of the firm (without altering the financial mix) such as tracking stock cannot create value, though they might affect perceptions and hence the price.

### Value Creation 1: Increase Cash Flows from Assets in Place

- n The assets in place for a firm reflect investments that have been made historically by the firm. To the extent that these investments were poorly made and/or poorly managed, it is possible that value can be increased by increasing the after-tax cash flows generated by these assets. n The cash flows discounted in valuation are after taxes and reinvestment needs have been met: EBIT ( 1-t)
  - (Capital Expenditures Depreciation)
- Change in Non-cash Working Capital = Free Cash Flow to Firm n Proposition 2: A firm that can increase its current cash flows, without significantly impacting future growth or risk, will increase its value.

#### Ways of Increasing Cash Flows from Assets in Place

![](_page_88_Diagram_1.jpeg)

### Value Creation 2: Increase Expected Growth

- n Keeping all else constant, increasing the expected growth in earnings will increase the value of a firm. n The expected growth in earnings of any firm is a function of two variables:
  - The amount that the firm reinvests in assets and projects
  - The quality of these investments

#### Value Enhancement through Growth

![](_page_90_Diagram_1.jpeg)

### The Return Effect: Reinvestment Rate and Value at Embraer

**Reinvestment Rate and Value per share: Embraer**

![](_page_91_Figure_2.jpeg)

### Value Creation 3: Increase Length of High Growth Period

n Every firm, at some point in the future, will become a stable growth firm, growing at a rate equal to or less than the economy in which it operates. n The high growth period refers to the period over which a firm is able to sustain a growth rate greater than this "stable" growth rate. n If a firm is able to increase the length of its high growth period, other things remaining equal, it will increase value. n The length of the high growth period is a direct function of the competitive advantages that a firm brings into the process. Creating new competitive advantage or augmenting existing ones can create value.

### 3.1: The Brand Name Advantage

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

### 3.2: Patents and Legal Protection

n The most complete protection that a firm can have from competitive pressure is to own a patent, copyright or some other kind of legal protection allowing it to be the sole producer for an extended period. n Note that patents only provide partial protection, since they cannot protect a firm against a competitive product that meets the same need but is not covered by the patent protection. n Licenses and government-sanctioned monopolies also provide protection against competition. They may, however, come with restrictions on excess returns; utilities in the United States, for instance, are monopolies but are regulated when it comes to price increases and returns.

### 3.3: Switching Costs

n Another potential barrier to entry is the cost associated with switching from one firm's products to another. n The greater the switching costs, the more difficult it is for competitors to come in and compete away excess returns. n Firms that devise ways to increase the cost of switching from their products to competitors' products, while reducing the costs of switching from competitor products to their own will be able to increase their expected length of growth.

### 3.4: Cost Advantages

- n There are a number of ways in which firms can establish a cost advantage over their competitors, and use this cost advantage as a barrier to entry:
  - In businesses, where scale can be used to reduce costs, economies of scale can give bigger firms advantages over smaller firms
  - Owning or having exclusive rights to a distribution system can provide firms with a cost advantage over its competitors.
- Owning or having the rights to extract a natural resource which is in restricted supply (The undeveloped reserves of an oil or mining company, for instance) n These cost advantages will show up in valuation in one of two ways:
  - The firm may charge the same price as its competitors, but have a much higher operating margin.
  - The firm may charge lower prices than its competitors and have a much higher capital turnover ratio.

#### Gauging Barriers to Entry

n Which of the following barriers to entry are most likely to work for Embraer? p Brand Name p Patents and Legal Protection p Switching Costs p Cost Advantages n What about for Amazon.com? p Brand Name p Patents and Legal Protection p Switching Costs p Cost Advantages

### Value Creation 4: Reduce Cost of Capital

n The cost of capital for a firm can be written as:

Cost of Capital = 
$$k_e (E/(D+E)) + k_d (D/(D+E))$$

Where,

 ke = Cost of Equity for the firm

 kd = Borrowing rate (1 - tax rate)

n The cost of equity reflects the rate of return that equity investors in the firm would demand to compensate for risk, while the borrowing rate reflects the current long-term rate at which the firm can borrow, given current interest rates and its own default risk. n The cash flows generated over time are discounted back to the present at the cost of capital. Holding the cash flows constant, reducing the cost of capital will increase the value of the firm.

#### Estimating Cost of Capital: Amazon.com

#### n Equity

- Cost of Equity = 6.50% + 1.60 (4.00%) = 12.90%
- Market Value of Equity = \$ 84/share\* 340.79 mil shs = \$ 28,626 mil (98.8%)

#### n Debt

- Cost of debt = 6.50% + 1.50% (default spread) = 8.00%
- Market Value of Debt = \$ 349 mil (1.2%)

#### n Cost of Capital

Cost of Capital = 12.9 % (.988) + 8.00% (1- 0) (.012)) = 12.84%

#### Current Cost of Capital: Embraer

#### n Equity

- Cost of Equity = 5.1% + 0.88 (14.24%) = 17.63%
- Market Value of Equity = 595.69\*15.25 \$9,084 million
- Equity/(Debt+Equity ) = 97.6%

#### n Debt

- After-tax Cost of debt = 10.67% (1-.33) = 7.15%
- Market Value of Debt = \$ 223 million
- Debt/(Debt +Equity) = 2.4%

n Cost of Capital = 17.03%(.976)+6.75%(.024) = 16.78%

#### Reducing Cost of Capital

![](_page_102_Diagram_1.jpeg)

### Amazon.com: Optimal Debt Ratio

| Debt Ratio | Beta  | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC   | Firm Value (G) |
|------------|-------|----------------|-------------|-----------------------|----------|--------------------------|--------|----------------|
| 0%         | 1.58  | 12.82%         | AAA         | 6.80%                 | 0.00%    | 6.80%                    | 12.82% | \$29,192       |
| 10%        | 1.76  | 13.53%         | D           | 18.50%                | 0.00%    | 18.50%                   | 14.02% | \$24,566       |
| 20%        | 1.98  | 14.40%         | D           | 18.50%                | 0.00%    | 18.50%                   | 15.22% | \$21,143       |
| 30%        | 2.26  | 15.53%         | D           | 18.50%                | 0.00%    | 18.50%                   | 16.42% | \$18,509       |
| 40%        | 2.63  | 17.04%         | D           | 18.50%                | 0.00%    | 18.50%                   | 17.62% | \$16,419       |
| 50%        | 3.16  | 19.15%         | D           | 18.50%                | 0.00%    | 18.50%                   | 18.82% | \$14,719       |
| 60%        | 3.95  | 22.31%         | D           | 18.50%                | 0.00%    | 18.50%                   | 20.02% | \$13,311       |
| 70%        | 5.27  | 27.58%         | D           | 18.50%                | 0.00%    | 18.50%                   | 21.22% | \$12,125       |
| 80%        | 7.90  | 38.11%         | D           | 18.50%                | 0.00%    | 18.50%                   | 22.42% | \$11,112       |
| 90%        | 15.81 | 69.73%         | D           | 18.50%                | 0.00%    | 18.50%                   | 23.62% | \$10,237       |

### Embraer: Optimal Capital Structure

| Debt Ratio | Beta | Cost of Equity | Bond Rating | Interest rate on debt | Tax Rate | Cost of Debt (after-tax) | WACC   | Firm Value (G) |
|------------|------|----------------|-------------|-----------------------|----------|--------------------------|--------|----------------|
| 0%         | 0.87 | 16.83%         | AAA         | 10.07%                | 33.00%   | 6.75%                    | 16.83% | \$9,267        |
| 10%        | 0.93 | 17.74%         | AA          | 10.37%                | 33.00%   | 6.95%                    | 16.66% | \$9,417        |
| 20%        | 1.01 | 18.89%         | A-          | 11.12%                | 33.00%   | 7.45%                    | 16.60% | \$9,475        |
| 30%        | 1.11 | 20.37%         | BB          | 11.87%                | 33.00%   | 7.95%                    | 16.64% | \$9,438        |
| 40%        | 1.25 | 22.33%         | B           | 13.12%                | 33.00%   | 8.79%                    | 16.92% | \$9,187        |
| 50%        | 1.45 | 25.09%         | CCC         | 14.87%                | 33.00%   | 9.96%                    | 17.52% | \$8,673        |
| 60%        | 1.74 | 29.33%         | CCC         | 14.87%                | 32.40%   | 10.05%                   | 17.76% | \$8,486        |
| 70%        | 2.36 | 38.10%         | CC          | 15.87%                | 26.04%   | 11.74%                   | 19.65% | \$7,238        |
| 80%        | 3.61 | 55.85%         | C           | 17.37%                | 20.85%   | 13.75%                   | 22.17% | \$6,020        |
| 90%        | 7.22 | 107.23%        | C           | 17.37%                | 18.51%   | 14.15%                   | 23.46% | \$5,534        |

### Changing Financing Type

- n The fundamental principle in designing the financing of a firm is to ensure that the cash flows on the debt should match as closely as possible the cash flows on the asset. n By matching cash flows on debt to cash flows on the asset, a firm reduces its risk of default and increases its capacity to carry debt, which, in turn, reduces its cost of capital, and increases value. n Firms which mismatch cash flows on debt and cash flows on assets by using
  - Short term debt to finance long term assets
  - Dollar debt to finance non-dollar assets
  - Floating rate debt to finance assets whose cash flows are negatively or not affected by inflation will end up with higher default risk, higher costs of capital and lower firm value.

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

Aswath Damodaran107

#### **The Value Enhancement Chain**

**Current Cashflow to Firm** EBIT(1-t) : 543 - Nt CpX 36 - Chg WC 610 = FCFF -173 Reinvestment Rate =131.8%

**Expected Growth in EBIT (1-t)** .60\*.35= .21 **21%**

Stable Growth g = 4.5%; Beta = 0.90; Country Premium= 5.37% ROC= 15% Reinvestment Rate=30%

Terminal Value 10= 1736/(.1135-.045) = 25,336

**Cost of Equity 18.88%**

**Cost of Debt** (4.5%+ 5.37%+.%)(1-.33) = 7.45% Synthetic rating = A-

**Weights** E =80% D = 20%

*Discount at* Cost of Capital (WACC) = 18.88% (.80) + 6.75% (0.20) = 16.60%

Firm Value: 9,314 + NO Assets 510 - Net Debt: 284 =Equity 9601 -Options 0 Value/Share \$16.12

> **Riskfree Rate** : Riskfree rate = 4.5% (Real Riskfree rate)

+ **Beta**  1.01 **X** Unlevered Beta for Sectors: 0.87

**Risk Premium** 14.24% Firm's D/E Ratio: 2.45% Mature risk premium 4%

Country Risk Premium 10.24%

#### Embraer: Restructured

Reinvestment Rate 60%

Return on Capital 35%

> Term Yr 2480 744 1736

Transition Period 1 2 3 4 5 6 7 8 9 10 EBIT(1-t) \$657 \$795 \$962 \$1,164 \$1,408 \$1,657 \$1,896 \$2,107 \$2,271 \$2,373 - Reinvestment\$394 \$477 \$577 \$698 \$845 \$895 \$910 \$885 \$818 \$712 = FCFF \$263 \$318 \$385 \$466 \$563 \$762 \$986 \$1,222 \$1,453 \$1,661

> *Move to the optimal debt ratio of 20%. Beta increases to 1.01 and rating drops to A-.*

*Increase reinvestment with lower ROC*

### Amazon.com: Break Even at \$84?

|     | 6%        | 8%       | 10%       | 12%       | 14%       |
|-----|-----------|----------|-----------|-----------|-----------|
| 30% | \$ (1.94) | \$ 2.95  | \$ 7.84   | \$ 12.71  | \$ 17.57  |
| 35% | \$ 1.41   | \$ 8.37  | \$ 15.33  | \$ 22.27  | \$ 29.21  |
| 40% | \$ 6.10   | \$ 15.93 | \$ 25.74  | \$ 35.54  | \$ 45.34  |
| 45% | \$ 12.59  | \$ 26.34 | \$ 40.05  | \$ 53.77  | \$ 67.48  |
| 50% | \$ 21.47  | \$ 40.50 | \$ 59.52  | \$ 78.53  | \$ 97.54  |
| 55% | \$ 33.47  | \$ 59.60 | \$ 85.72  | \$ 111.84 | \$ 137.95 |
| 60% | \$ 49.53  | \$ 85.10 | \$ 120.66 | \$ 156.22 | \$ 191.77 |