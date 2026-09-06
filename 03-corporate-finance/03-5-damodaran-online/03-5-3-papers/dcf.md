---
title: "Dcf"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/execval/dcf.pdf
---

# Valuation

Aswath Damodaran

http://www.damodaran.com

For the valuations in this presentation, go to Seminars/ Presentations

![](_page_1_Picture_3.jpeg)

### Some Initial Thoughts

" One hundred thousand lemmings cannot be wrong" 

### Misconceptions about Valuation

- Myth 1: A valuation is an objective search for "true" value
  - Truth 1.1: All valuations are biased. The only questions are how much and in which direction.
- Truth 1.2: The direction and magnitude of the bias in your valuation is directly proportional to who pays you and how much you are paid. Myth 2.: A good valuation provides a precise estimate of value
  - Truth 2.1: There are no precise valuations
- Truth 2.2: The payoff to valuation is greatest when valuation is least precise. Myth 3: . The more quantitative a model, the better the valuation
  - Truth 3.1: One's understanding of a valuation model is inversely proportional to the number of inputs required for the model.
  - Truth 3.2: Simpler valuation models do much better than complex ones.

### Approaches to Valuation

**Discounted cashflow valuation**, relates the value of an asset to the present value of expected future cashflows on that asset. **Relative valuation**, estimates the value of an asset by looking at the pricing of 'comparable' assets relative to a common variable like earnings, cashflows, book value or sales. **Contingent claim valuation**, uses option pricing models to measure the value of assets that share option characteristics.

### Discounted Cash Flow Valuation

- **What is it**: In discounted cash flow valuation, the value of an asset is the present value of the expected cash flows on the asset. **Philosophical Basis**: Every asset has an intrinsic value that can be estimated, based upon its characteristics in terms of cash flows, growth and risk. **Information Needed**: To use discounted cash flow valuation, you need
  - to estimate the life of the asset
  - to estimate the cash flows during the life of the asset
- to estimate the discount rate to apply to these cash flows to get present value **Market Inefficiency**: Markets are assumed to make mistakes in pricing assets across time, and are assumed to correct themselves over time, as new information comes out about assets.

# Discounted Cashflow Valuation: Basis for Approach

where CFt is the expected cash flow in period t, r is the discount rate appropriate given the riskiness of the cash flow and n is the life of the asset.

**Proposition 1: For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.**

**Proposition 2: Assets that generate cash flows early in their life will be worth more than assets that generate cash flows later; the latter may however have greater growth and higher cash flows to compensate.**

$$\text{Value of asset} = \frac{\text{CF}_1}{(1+r)^1} + \frac{\text{CF}_2}{(1+r)^2} + \frac{\text{CF}_3}{(1+r)^3} + \frac{\text{CF}_4}{(1+r)^4} + \dots + \frac{\text{CF}_n}{(1+r)^n}$$

### DCF Choices: Equity Valuation versus Firm Valuation

![](_page_6_Diagram_2.jpeg)

**Equity valuation**: Value just the equity claim in the business

**Firm Valuation**: Value the entire business

### Equity Valuation

![](_page_7_Diagram_2.jpeg)

*Figure 5.5: Equity Valuation*

### Firm Valuation

![](_page_8_Diagram_1.jpeg)

# DISCOUNTED CASHFLOW VALUATION

![](_page_9_Diagram_9.jpeg)

![](_page_10_Diagram_31.jpeg)

![](_page_11_Diagram_1.jpeg)

## Discounted Cash Flow Valuation: High Growth with Negative Earnings

![](_page_12_Diagram_9.jpeg)

![](_page_13_Diagram_0.jpeg)

![]()

### Cost of Equity

![](_page_15_Diagram_1.jpeg)

### A Simple Test

 You are valuing a Greek company in Euros for a US institutional investor and are attempting to estimate a risk free rate to use in the analysis. The risk free rate that you should use is The interest rate on a US \$ denominated treasury bond (4.25%) The interest rate on a Euro-denominated Greek government bond (3.67%) The interest rate on a Euro-denominated bond issued by the German government (3.41%)

### Everyone uses historical premiums, but..

- The historical premium is the premium that stocks have historically earned over riskless securities. Practitioners never seem to agree on the premium; it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. For instance, looking at the US:

| Historical Period | Stocks - T.Bills | Arithmetic average Stocks - T.Bonds | Stocks - T.Bills | Geometric Average Stocks - T.Bonds |
|-------------------|------------------|-------------------------------------|------------------|------------------------------------|
| 1928-2007         | 7.78%            | 6.42%                               | 5.94%            | 4.79%                              |
| 1967-2007         | 5.94%            | 4.33%                               | 4.75%            | 3.50%                              |
| 1997-2007         | 5.26%            | 2.68%                               | 4.69%            | 2.34%                              |

# Assessing Country Risk Using Currency Ratings: Western Europe

| Country  | Rating | Default Spread over German Euro (in bp) |
|----------|--------|-----------------------------------------|
| Austria  | Aaa    | 0                                       |
| Belgium  | Aaa    | 10                                      |
| France   | Aaa    | 4                                       |
| Germany  | Aaa    | 0                                       |
| Greece   | A1     | 26                                      |
| Ireland  | Aaa    | 6                                       |
| Italy    | Aa2    | 16                                      |
| Portugal | Aa2    | 10                                      |
| Spain    | Aaa    | 3                                       |

# Assessing Country Risk using Ratings: Beyond the EU

| Country        | Rating | Default Spread |
|----------------|--------|----------------|
| Croatia        | Baa3   | 145            |
| Cyprus         | A2     | 90             |
| Czech Republic | Baa1   | 120            |
| Hungary        | A3     | 95             |
| Latvia         | Baa2   | 130            |
| Lithuania      | Ba1    | 250            |
| Moldova        | B3     | 650            |
| Poland         | Baa1   | 120            |
| Romania        | B3     | 650            |
| Russia         | B2     | 550            |
| Slovakia       | Ba1    | 250            |
| Slovenia       | A2     | 90             |
| Turkey         | B1     | 450            |

# Using Country Ratings to Estimate Equity Spreads

- Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads.
  - One way to adjust the country spread upwards is to use information from the US market. In the US, the equity risk premium has been roughly twice the default spread on junk bonds.
  - Another is to multiply the bond spread by the relative volatility of stock and bond prices in that market. For example,
    - Standard Deviation in Greek ASE(Equity) = 16%
    - Standard Deviation in Greek Euro Bond = 9%
    - Adjusted Equity Spread = 0.26% (16/9) = 0.46%

### From Country Risk Premiums to Corporate Risk premiums

 Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country ERP} + \text{Beta (US premium)}$$

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium + Country ERP)}$$

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium})+\lambda (\text{Country ERP})$$

Country ERP: Additional country equity risk premium

### Estimating Company Exposure to Country Risk

- ■ Different companies should be exposed to different degrees to country risk. For instance, a Greek firm that generates the bulk of its revenues in the rest of Western Europe should be less exposed to country risk than one that generates all its business within Greece.
  ■ The factor “ $\lambda$ ” measures the relative exposure of a firm to country risk. One simplistic solution would be to do the following: $\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{avg firm}}$ 

  For instance, if a firm gets 35% of its revenues domestically while the average firm in that market gets 70% of its revenues domestically

  $$\lambda = 35\% / 70\% = 0.5$$

  ■ There are two implications

### Estimating E(Return) for Titan Cements

 Assume that the beta for Titan Cements is 0.95, and that the riskfree rate used is 3.41%. Also assume that the historical premium for the US (4.79%) is a reasonable estimate of a mature market risk premium. Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

E(Return) = 3.41% + 0.46% + 0.93 (4.79%) = 8.33%

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

$$E(\text{Return}) = 3.41\% + 0.93 (4.79\% + 0.46\%) = 8.30\%$$

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

E(Return)= 3.41% + 0.93(4.79%) + 0.56 (0.46%) + 0.14(3%) = 8.35%

Titan is less exposed to Greek country risk than the typical Greek firm since it gets about 40% of its revenues in Greece; the average for Greek firms is 70%. In 2004, though, Titan got about 14% of it's revenues from the Balkan states.

### An alternate view of ERP: Watch what I pay, not what I say..

You can back out an equity risk premium from stock prices:

| Year                              | Dividend Yield Buybacks/Index | Yield |
|-----------------------------------|-------------------------------|-------|
| 2001                              | 1.37%                         | 1.25% |
| 2002                              | 1.81%                         | 1.58% |
| 2003                              | 1.61%                         | 1.23% |
| 2004                              | 1.57%                         | 1.78% |
| 2005                              | 1.79%                         | 3.11% |
| 2006                              | 1.77%                         | 3.38% |
| 2007                              | 1.89%                         | 4.00% |
| Average yield between 2001-2007 = |                               |       |

![](_page_24_Figure_6.jpeg)

Between 2001 and 2007 dividends and stock buybacks averaged 4.02% of the index each year.

Analysts expect earnings to grow 5% a year for the next 5 years. We will assume that dividends & buybacks will keep pace.. Last year's cashflow (59.03) growing at 5% a year

After year 5, we will assume that earnings on the index will grow at 4.02%, the same rate as the entire economy (= riskfree rate).

### Solving for the implied premium…

- ■ If we know what investors paid for equities at the beginning of 2007 and we can estimate the expected cash flows from equities, we can solve for the rate of return that they expect to make (IRR):

- ■ Expected Return on Stocks = 8.39%
- ■ Implied Equity Risk Premium = Expected Return on Stocks - T.Bond Rate  
   $= 8.39\% - 4.02\% = 4.37\%$

$$1468.36 = \frac{61.98}{(1+r)} + \frac{65.08}{(1+r)^2} + \frac{68.33}{(1+r)^3} + \frac{71.75}{(1+r)^4} + \frac{75.34}{(1+r)^5} + \frac{75.35(1.0402)}{(r-.0402)(1+r)^5}$$

# Implied Premiums in the US

![](_page_26_Figure_1.jpeg)

# Implied Premium versus RiskFree Rate

![](_page_27_Figure_1.jpeg)

### Equity Risk Premiums and Bond Default Spreads

![](_page_28_Figure_1.jpeg)

### Why implied premiums matter?

 In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. If all analysts in the department used the arithmetic average premium for 1928-2007 of 6.42% to value stocks in January 2008, given the implied premium of 4.37%, what are they likely to find? The values they obtain will be too low (most stocks will look overvalued) The values they obtain will be too high (most stocks will look under valued) There should be no systematic bias as long as they use the same premium (6.42%) to value all stocks.

# Which equity risk premium should you use for the US?

*Historical Risk Premium*: When you use the historical risk premium, you are assuming that premiums will revert back to a historical norm and that the time period that you are using is the right norm. *Current Implied Equity Risk premium*: You are assuming that the market is correct in the aggregate but makes mistakes on individual stocks. If you are required to be market neutral, this is the premium you should use. (What types of valuations require market neutrality?) *Average Implied Equity Risk premium*: The average implied equity risk premium between 1960-2007 in the United States is about 4%. You are assuming that the market is correct on average but not necessarily at a point in time.

# Implied Premium for Greek Market: April 27, 2005

- Level of the Index = 2786 Dividends on the Index = 3.28% of 2467 Other parameters
  - Riskfree Rate = 3.41% (Euros)
  - Expected Growth (in Euros)
    - Next 5 years = 8% (Used expected growth rate in Earnings)
- After year 5 = 3.41% Solving for the expected return:
  - Expected return on Equity = 7.56%
- Implied Equity premium = 7.56% 3.41% = 4.15% Effect on valuation
  - Titan's value with historical premium (4%) + country (.46%) : 32.84 Euros/share
  - Titan's value with implied premium: 32.67 Euros per share

### Estimating Beta

 The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm) -

$$R_j = a + b R_m$$

- where a is the intercept and b is the slope of the regression.

 The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.

This beta has three problems:

- It has high standard error
- It reflects the firm's business mix over the period of the regression, not the current mix
- It reflects the firm's average financial leverage over the period rather than the current leverage.

### Beta Estimation: Amazon

![](_page_33_Figure_1.jpeg)

### Beta Estimation for Titan Cement: The Index Effect

![](_page_34_Figure_1.jpeg)

### Determinants of Betas

![](_page_35_Diagram_1.jpeg)

# Bottom-up Betas

![](_page_36_Diagram_5.jpeg)

### Bottom up Beta Estimates

| Company                | Comparable Companies                  | Unlevered |                                 |
|------------------------|---------------------------------------|-----------|---------------------------------|
| Titan Cement           | Global Cement companies               | 0.80      | 0.80 (1 + (1-.2547) (.2135) =   |
| Amazon (First 5 years) | Internet Retailers                    | 1.58      | 1.58 (1- (1-0) (.0121) = 1.60   |
| Amazon (After year 5)  | Specialty Retailers                   |           | 1.00                            |
| Kristin Kandy          | Food Processing companies with market |           |                                 |
|                        |                                       | 0.78      | 0.78 ( 1+(1-.4) (30/70)) = 0.98 |

### Small Firm and Other Premiums

 It is common practice to add premiums on to the cost of equity for firmspecific characteristics. For instance, many analysts add a small stock premium of 3-3.5% (historical premium for small stocks over the market) to the cost of equity for smaller companies. Adding arbitrary premiums to the cost of equity is always a dangerous exercise. If small stocks are riskier than larger stocks, we need to specify the reasons and try to quantify them rather than trust historical averages. (You could argue that smaller companies are more likely to serve niche (discretionary) markets or have higher operating leverage and adjust the beta to reflect this tendency).

# Is Beta an Adequate Measure of Risk for a Private Firm?

The owners of most private firms are not diversified. Beta measures the risk added on to a diversified portfolio. Therefore, using beta to arrive at a cost of equity for a private firm will

- a) Under estimate the cost of equity for the private firm
- b) Over estimate the cost of equity for the private firm
- c) Could under or over estimate the cost of equity for the private firm

### Total Risk versus Market Risk

 Adjust the beta to reflect total risk rather than market risk. This adjustment is a relatively simple one, since the R squared of the regression measures the proportion of the risk that is market risk.

Total Beta = Market Beta / Correlation of the sector with the market

 To estimate the beta for Kristin Kandy, we begin with the bottom-up unlevered beta of food processing companies:

- Unlevered beta for publicly traded food processing companies = 0.78
- Average correlation of food processing companies with market = 0.333
- Unlevered total beta for Kristin Kandy = 0.78/0.333 = 2.34
- Debt to equity ratio for Kristin Kandy = 0.3/0.7 (assumed industry average)
- Total Beta = 2.34 ( 1- (1-.40)(30/70)) = 2.94
- Total Cost of Equity = 4.50% + 2.94 (4%) = 16.26%

### When would you use this total risk measure?

 Under which of the following scenarios are you most likely to use the total risk measure: when valuing a private firm for an initial public offering when valuing a private firm for sale to a publicly traded firm when valuing a private firm for sale to another private investor Assume that you own a private business. What does this tell you about the best potential buyer for your business?

### From Cost of Equity to Cost of Capital

![](_page_42_Diagram_1.jpeg)

# Estimating Synthetic Ratings

 The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

 For Titan's interest coverage ratio, we used the interest expenses and EBIT from 2004.

Interest Coverage Ratio = 232/ 19.4 = 11.95

 For Kristin Kandy, we used the interest expenses and EBIT from the most recent financial year:

Interest Coverage Ratio = 500,000/ 85,000 = 5.88

 Amazon.com has negative operating income; this yields a negative interest coverage ratio, which should suggest a D rating. We computed an average interest coverage ratio of 2.82 over the next 5 years.

### Interest Coverage Ratios, Ratings and Default Spreads

| If Interest Coverage Ratio is |            | Estimated Bond Rating | Default Spread(1/00) | Default Spread(1/04) |
|-------------------------------|------------|-----------------------|----------------------|----------------------|
| > 8.50                        | (>12.50)   | AAA                   | 0.20%                | 0.35%                |
| 6.50 - 8.50                   | (9.5-12.5) | AA                    | 0.50%                | 0.50%                |
| 5.50 - 6.50                   | (7.5-9.5)  | A+                    | 0.80%                | 0.70%                |
| 4.25 - 5.50                   | (6-7.5)    | A                     | 1.00%                | 0.85%                |
| 3.00 - 4.25                   | (4.5-6)    | A–                    | 1.25%                | 1.00%                |
| 2.50 - 3.00                   | (3.5-4.5)  | BBB                   | 1.50%                | 1.50%                |
| 2.25 - 2.50                   | (3.5 -4)   | BB+                   | 1.75%                | 2.00%                |
| 2.00 - 2.25                   | ((3-3.5)   | BB                    | 2.00%                | 2.50%                |
| 1.75 - 2.00                   | (2.5-3)    | B+                    | 2.50%                | 3.25%                |
| 1.50 - 1.75                   | (2-2.5)    | B                     | 3.25%                | 4.00%                |
| 1.25 - 1.50                   | (1.5-2)    | B –                   | 4.25%                | 6.00%                |
| 0.80 - 1.25                   | (1.25-1.5) | CCC                   | 5.00%                | 8.00%                |
| 0.65 - 0.80                   | (0.8-1.25) | CC                    | 6.00%                | 10.00%               |
| 0.20 - 0.65                   | (0.5-0.8)  | C                     | 7.50%                | 12.00%               |
| < 0.20                        | (<0.5)     | D                     | 10.00%               | 20.00%               |

For Titan and Kristing Kandy, I used the interest coverage ratio table for smaller/riskier firms (the numbers in brackets) which yields a lower rating for the same interest coverage ratio.

### Estimating the cost of debt for a firm

 The synthetic rating for Titan Cement is AA. Using the 2004 default spread of 0.50%, we estimate a cost of debt of 4.17% (using a riskfree rate of 3.41% and adding in the country default spread of 0.26%):

Cost of debt = Riskfree rate + Greek default spread + Company default spread  

$$= 3.41\% + 0.26\% + 0.50\% = 4.17\%$$

 The synthetic rating for Kristin Kandy is A-. Using the 2004 default spread of 1.00% and a riskfree rate of 4.50%, we estimate a cost of debt of 5.50%.

Cost of debt = Riskfree rate + Default spread =4.50% + 1.00% = 5.50%

 The synthetic rating for Amazon.com in 2000 was BBB. The default spread for BBB rated bond was 1.50% in 2000 and the treasury bond rate was 6.5%.

Cost of debt = Riskfree Rate + Default spread = 6.50% + 1.50% = 8.00%

### Weights for the Cost of Capital Computation

- The weights used to compute the cost of capital should be the market value weights for debt and equity. There is an element of circularity that is introduced into every valuation by doing this, since the values that we attach to the firm and equity at the end of the analysis are different from the values we gave them at the beginning. For private companies, neither the market value of equity nor the market value of debt is observable. Rather than use book value weights, you should try
  - Industry average debt ratios for publicly traded firms in the business
  - Target debt ratio (if management has such a target)
  - Estimated value of equity and debt from valuation (through an iterative process)

### Estimating Cost of Capital: Amazon.com

#### Equity

- Cost of Equity = 6.50% + 1.60 (4.00%) = 12.90%
- Market Value of Equity = \$ 84/share\* 340.79 mil shs = \$ 28,626 mil (98.8%)

#### Debt

- Cost of debt = 6.50% + 1.50% (default spread) = 8.00%
- Market Value of Debt = \$ 349 mil (1.2%)

#### Cost of Capital

Cost of Capital = 12.9 % (.988) + 8.00% (1- 0) (.012)) = 12.84%

### Estimating Cost of Capital: Titan Cements

#### Equity

- Cost of Equity = 3.41% + 0.93 (4%+ 0.46%) = 7.56%
- Market Value of Equity =1940 million Euros (82.4%)

#### Debt

- Cost of debt = 3.41% + 0.26% + 0.50%= 4.17%
- Market Value of Debt = 414 million Euros (17.6%)

#### Cost of Capital

Cost of Capital = 7.56 % (.824) + 4.17% (1- .2547) (0.176)) = 6.78%

The book value of equity at Titan Cement is 542 million Euros

The book value of debt at Titan Cement is 405 million; Interest expense is 19 mil; Average maturity of debt = 4 years

Estimated market value of debt = 19 million (PV of annuity, 4 years, 4.17%) + \$ 405 million/1.04174 = 414 million Euros

### Estimating Cost of Capital: Kristin Kandy

#### Equity

- Cost of Equity = 4.50% + 2.94 (4%) = 16.26%
- Equity as percent of capital = 70%

#### Debt

- Pre-tax Cost of debt = 4.50% + 1.00% = 5.50%
- Marginal tax rate = 40%
- Debt as percent of capital = 30% (Industry average)

#### Cost of Capital

Cost of Capital = 16.26% (.70) + 5.50% (1-.40) (.30) = 12.37%

# II. Estimating Cashflows and Growth

### Defining Cashflow

![](_page_51_Diagram_1.jpeg)

### From Reported to Actual Earnings

![](_page_52_Diagram_1.jpeg)

### Dealing with Operating Lease Expenses

- Operating Lease Expenses are treated as operating expenses in computing operating income. In reality, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital: Debt Value of Operating Leases = Present value of Operating Lease Commitments at the pre-tax cost of debt When you convert operating leases into debt, you also create an asset to counter it of exactly the same value. Adjusted Operating Earnings Adjusted Operating Earnings = Operating Earnings + Operating Lease Expenses - Depreciation on Leased Asset
  - As an approximation, this works: Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

### Operating Leases at The Gap in 2003

 The Gap has conventional debt of about \$ 1.97 billion on its balance sheet and its pre-tax cost of debt is about 6%. Its operating lease payments in the 2003 were \$978 million and its commitments for the future are below:

| Year | Commitment (millions)  | Present Value (at 6%)                   |
|------|------------------------|-----------------------------------------|
| 1    | \$899.00               | \$848.11                                |
| 2    | \$846.00               | \$752.94                                |
| 3    | \$738.00               | \$619.64                                |
| 4    | \$598.00               | \$473.67                                |
| 5    | \$477.00               | \$356.44                                |
|      | 6&7 \$982.50 each year | \$1,346.04                              |
|      | Debt Value of leases = | \$4,396.85 (Also value of leased asset) |

 Debt outstanding at The Gap = \$1,970 m + \$4,397 m = \$6,367 m Adjusted Operating Income = Stated OI + OL exp this year - Deprec'n = \$1,012 m + 978 m - 4397 m /7 = \$1,362 million (7 year life for assets) Approximate OI = \$1,012 m + \$ 4397 m (.06) = \$1,276 m

### The Collateral Effects of Treating Operating Leases as Debt

| <i>C o nventional Accounting</i>                                                                                                                                     |  | <i>Operating Leases Treated as Debt</i>                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-----------------------------------------------------------------------------------------------------------------|
| <i>Income Statement</i>                                                                                                                                              |  | <i>Income Statement</i>                                                                                         |
| EBIT& Leases = 1,990                                                                                                                                                 |  | EBIT& Leases = 1,990                                                                                            |
| - Op Leases = 978                                                                                                                                                    |  | - Deprecn: OL= 628                                                                                              |
| EBIT = 1,012                                                                                                                                                         |  | EBIT = 1,362                                                                                                    |
|                                                                                                                                                                      |  | Interest expense will rise to reflect the conversion of operating leases as debt. Net income should not change. |
| <i>Balance Sheet</i>                                                                                                                                                 |  | <i>Balance Sheet</i>                                                                                            |
| Off balance sheet (Not shown as debt or as an asset). Only the conventional debt of \$1,970 million shows up on balance sheet                                        |  | Asset Liability<br>OL Asset 4397 OL Debt 4397<br>Total debt = 4397 + 1970 = \$6,367 million                     |
| Cost of capital = 8.20%(7350/9320) + 4%<br>(1970/9320) = 7.31%<br>Cost of equity for The Gap = 8.20%<br>After-tax cost of debt = 4%<br>Market value of equity = 7350 |  | Cost of capital = 8.20%(7350/13717) + 4%<br>(6367/13717) = 6.25%                                                |
| Return on capital = 1012 (1-.35)/(3130+1970)<br>= 12.90%                                                                                                             |  | Return on capital = 1362 (1-.35)/(3130+6367)<br>= 9.30%                                                         |

### R&D Expenses: Operating or Capital Expenses

- Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. To capitalize R&D,
  - Specify an amortizable life for R&D (2 10 years)
  - Collect past R&D expenses for as long as the amortizable life
  - Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

# Capitalizing R&D Expenses: Cisco in 1999

R & D was assumed to have a 5-year life.

*Year R&D Expense Unamortized portion Amortization this year*

| 1999 (current)            | 1594.00 | 1.00 | 1594.00            |           |
|---------------------------|---------|------|--------------------|-----------|
| 1998                      | 1026.00 | 0.80 | 820.80             | \$205.20  |
| 1997                      | 698.00  | 0.60 | 418.80             | \$139.60  |
| 1996                      | 399.00  | 0.40 | 159.60             | \$79.80   |
| 1995                      | 211.00  | 0.20 | 42.20              | \$42.20   |
| 1994                      | 89.00   | 0.00 | 0.00               | \$17.80   |
| Total                     |         |      | \$ 3,035.40        | \$ 484.60 |
| Value of research asset = |         |      | \$ 3,035.4 million |           |

Amortization of research asset in 1998 = \$ 484.6 million

Adjustment to Operating Income = \$ 1,594 million - 484.6 million = 1,109.4 million

### The Effect of Capitalizing R&D

| <i>C o nventional Accounting</i>                                                                                         |  | <i>R&amp;D treated as capital expenditure</i>    |
|--------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------|
| <i>Income Statement</i>                                                                                                  |  | <i>Income Statement</i>                          |
| EBIT& R&D = 5,049                                                                                                        |  | EBIT& R&D = 5,049                                |
| - R&D = 1,594                                                                                                            |  | - Amort: R&D = 485                               |
| EBIT = 3,455                                                                                                             |  | EBIT = 4,564 (Increase of 1,109)                 |
| EBIT (1-t) = 2,246                                                                                                       |  | EBIT (1-t) = 2,967                               |
|                                                                                                                          |  | Ignored tax benefit = (1594-485)(.35) = 388      |
|                                                                                                                          |  | Adjusted EBIT (1-t) = 2967 + 388 = 3354          |
|                                                                                                                          |  | (Increase of \$1,109 million)                    |
|                                                                                                                          |  | Net Income will also increase by \$1,109 million |
| <i>Balance Sheet</i>                                                                                                     |  | <i>Balance Sheet</i>                             |
| Off balance sheet asset. Book value of equity at \$11,722 million is understated because biggest asset is off the books. |  | Asset Liability                                  |
|                                                                                                                          |  | R&D Asset 3035 Book Equity +3035                 |
|                                                                                                                          |  | Total Book Equity = 11722+3035 = 14757           |
| <i>Capital Expenditures</i>                                                                                              |  | <i>Capital Expenditures</i>                      |
| Conventional net cap ex of \$98 million                                                                                  |  | Net Cap ex = 98 + 1594 - 485 = 1206              |
| <i>Cash Flows</i>                                                                                                        |  | <i>Cash Flows</i>                                |
| EBIT (1-t) = 2246                                                                                                        |  | EBIT (1-t) = 3354                                |
| - Net Cap Ex = 98                                                                                                        |  | - Net Cap Ex = 1206                              |
| FCFF = 2148                                                                                                              |  | FCFF = 2148                                      |
| Return on capital = 2246/11722 (no debt) = 19.16%                                                                        |  | Return on capital = 3354/14757 = 22.78%          |

### What tax rate?

 The tax rate that you should use in computing the after-tax operating income should be The effective tax rate in the financial statements (taxes paid/Taxable income) The tax rate based upon taxes paid and EBIT (taxes paid/EBIT) The marginal tax rate for the country in which the company operates The weighted average marginal tax rate across the countries in which the company operates None of the above Any of the above, as long as you compute your after-tax cost of debt using the same tax rate

# Capital expenditures should include

- Research and development expenses, once they have been re-categorized as capital expenses. The adjusted net cap ex will be Adjusted Net Capital Expenditures = Net Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset Acquisitions of other firms, since these are like capital expenditures. The adjusted net cap ex will be Adjusted Net Cap Ex = Net Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions Two caveats:
  - 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
  - 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

# Cisco's Net Capital Expenditures in 1999

| Cap Expenditures (from statement of CF) | = \$ 584 mil   |
|-----------------------------------------|----------------|
| - Depreciation (from statement of CF)   | = \$ 486 mil   |
| Net Cap Ex (from statement of CF)       | = \$ 98 mil    |
| + R & D expense                         | = \$ 1,594 mil |
| - Amortization of R&D                   | = \$ 485 mil   |
| + Acquisitions                          | = \$ 2,516 mil |
| Adjusted Net Capital Expenditures       | = \$3,723 mil  |

(Amortization was included in the depreciation number)

### Working Capital Investments

 In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable) Any investment in this measure of working capital ties up cash. Therefore, any increases (decreases) in working capital will reduce (increase) cash flows in that period. When forecasting future growth, it is important to forecast the effects of such growth on working capital needs, and building these effects into the cash flows.

### Dealing with Negative or Abnormally Low Earnings

![](_page_63_Diagram_1.jpeg)

### Normalizing Earnings: Amazon

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

### Estimating FCFF: Titan Cement

 EBIT = 232 million Euros Tax rate = 25.47% Net Capital expenditures = Cap Ex - Depreciation = 109.5 - 60.3 = 49.2 million Change in Working Capital = +51.80 million

#### **Estimating FCFF**

| Current EBIT * (1 - tax rate) =     | 232 (1-.2547) = 172.8 Million |
|-------------------------------------|-------------------------------|
| - (Capital Spending - Depreciation) | 49.2                          |
| - Change in Working Capital         | 51.8                          |
| Current FCFF                        | 71.8 Million Euros            |

### Estimating FCFF: Amazon.com

- EBIT (Trailing 1999) = -\$ 410 million Tax rate used = 0% (Assumed Effective = Marginal) Capital spending (Trailing 1999) = \$ 243 million Depreciation (Trailing 1999) = \$ 31 million Non-cash Working capital Change (1999) = - 80 million Estimating FCFF (1999) Current EBIT \* (1 - tax rate) = - 410 (1-0) = - \$410 million
  - (Capital Spending Depreciation) = \$212 million
  - Change in Working Capital = -\$ 80 million Current FCFF 

     = - \$542 million

### Growth in Earnings

- Look at the past
- The historical growth in earnings per share is usually a good starting point for growth estimation Look at what others are estimating
- Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are. Look at fundamentals
  - Ultimately, all growth in earnings can be traced to two fundamentals how much the firm is investing in new projects, and what returns these projects are making for the firm.

### Fundamental Growth when Returns are stable

![](_page_68_Diagram_1.jpeg)

### Measuring Return on Capital (Equity)

![](_page_69_Diagram_1.jpeg)

# Normalizing Reinvestment: Titan Cement

|                              | 2000     | 2001     | 2002     | 2003     | 2004     | Total    |
|------------------------------|----------|----------|----------|----------|----------|----------|
| Cp Ex                        | \$50.54  | \$81.00  | \$113.30 | \$102.30 | \$109.50 | \$456.64 |
| Depreciation                 | \$39.26  | \$40.87  | \$80.94  | \$73.70  | \$60.30  | \$295.07 |
| EBIT                         | \$162.78 | \$186.39 | \$200.60 | \$222.00 | \$231.80 |          |
| EBIT(1-t)                    | \$121.32 | \$138.92 | \$149.51 | \$154.42 | \$172.76 | \$736.92 |
| Net Cap Ex as % of EBIT(1-t) | 9.30%    | 28.89%   | 21.64%   | 18.52%   | 28.48%   | 21.92%   |
| Revenues                     | 622.7    | 982.9    | 1036.1   | 1035.7   | 1104.4   | 4781.8   |
| Non-cashh Current assets     | 248.55   | 342.95   | 352.93   | \$402.10 | \$398.90 |          |
| Non-debt current liabilities | 133.33   | 177.15   | 194.57   | 255      | 190      |          |
| Non-cash WC                  | 115.22   | 165.8    | 158.36   | 147.1    | 208.9    | 795.38   |
| as % of revenues             | 18.50%   | 16.87%   | 15.28%   | 14.20%   | 18.92%   | 16.63%   |

### Expected Growth Estimate: Titan Cement

- Normalized Change in working capital = (Working capital as percent of revenues) \* Change in revenues in 2004 = .1663 (1104.4-1035.7) = 11.4 mil Euros Normalized Net Cap Ex = Net Cap ex as % of EBIT(1-t) \* EBIT (1-t) in 2004 = .2192\*(232 (1-.2547)) = 37.90 million Euros Normalized reinvestment rate = (11.4+37.9)/(232(1-..2547)) = 28.54% Return on capital = 232 (1-.2547)/ (499+399) = 19.25%
- The book value of debt and equity from last year was used. Expected growth rate = .2854\*.1925= 5.49%

# Fundamental Growth when return on equity (capital) is changing

 When the return on equity or capital is changing, there will be a second component to growth, positive if the return is increasing and negative if the return is decreasing. If ROCt is the return on capital in period t and ROCt+1 is the return on capital in period t+1, the expected growth rate in operating income will be:

$$\text{Expected Growth Rate} = \text{ROC}_{t+1} * \text{Reinvestment rate} + (\text{ROC}_{t+1} - \text{ROC}_t) / \text{ROC}_t$$

### An example: Motorola

 Motorola's current return on capital is 12.18% and its reinvestment rate is 52.99%. We expect Motorola's return on capital to rise to 17.22% over the next 5 years (which is half way towards the industry average)

Expected Growth Rate

= 
$$\text{ROC}_{\text{New Investments}}^* \text{Reinvestment Rate}_{\text{current}} + \{1 + (\text{ROC}_{\text{In 5 years}} - \text{ROC}_{\text{Current}}) / \text{ROC}_{\text{Current}}\}^{1.5-1}$$

= .1722\*.5299 +{ [1+(.1722-.1218)/.1218]1/5-1}

= .174 or 17.40%

- One way to think about this is to decompose Motorola's expected growth into
  - Growth from new investments: .1722\*5299= 9.12%
  - Growth from more efficiently using existing investments: 17.40%-9.12%=8.28%

### Revenue Growth and Operating Margins

 With negative operating income and a negative return on capital, the fundamental growth equation is of little use for Amazon.com For Amazon, the effect of reinvestment shows up in revenue growth rates and changes in expected operating margins: Expected Revenue Growth in \$ = Reinvestment (in \$ terms) \* (Sales/ Capital) The effect on expected margins is more subtle. Amazon's reinvestments (especially in acquisitions) may help create barriers to entry and other competitive advantages that will ultimately translate into high operating margins and high profits.

# Growth in Revenues, Earnings and Reinvestment: Amazon

|    | Year Growth | Revenue Chg in | Revenue | Reinvestment | Chg Rev/ Chg Reinvestment ROC |
|----|-------------|----------------|---------|--------------|-------------------------------|
| 1  | 150.00%     | \$1,676        | \$559   | 3.00         | -76.62%                       |
| 2  | 100.00%     | \$2,793        | \$931   | 3.00         | -8.96%                        |
| 3  | 75.00%      | \$4,189        | \$1,396 | 3.00         | 20.59%                        |
| 4  | 50.00%      | \$4,887        | \$1,629 | 3.00         | 25.82%                        |
| 5  | 30.00%      | \$4,398        | \$1,466 | 3.00         | 21.16%                        |
| 6  | 25.20%      | \$4,803        | \$1,601 | 3.00         | 22.23%                        |
| 7  | 20.40%      | \$4,868        | \$1,623 | 3.00         | 22.30%                        |
| 8  | 15.60%      | \$4,482        | \$1,494 | 3.00         | 21.87%                        |
| 9  | 10.80%      | \$3,587        | \$1,196 | 3.00         | 21.19%                        |
| 10 | 6.00%       | \$2,208        | \$736   | 3.00         | 20.39%                        |

Assume that firm can earn high returns because of established economies of scale.

![]()

### Getting Closure in Valuation

 A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

 Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = t = \infty \frac{\text{CF}_t}{\sum_{t=1}^t (1+r)^t}$$

$$\text{Value} = \frac{t = N}{\sum_{t=1}^N \frac{\text{CF}_t}{(1+r)^t}} + \frac{\text{Terminal Value}}{(1+r)^N}$$

### Ways of Estimating Terminal Value

![](_page_78_Diagram_1.jpeg)

### Stable Growth and Terminal Value

 When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

## $$g = \text{Expected growth rate}$$

 This "constant" growth rate is called a stable growth rate and cannot be higher than the growth rate of the economy in which the firm operates. While companies can maintain high growth rates for extended periods, they will all approach "stable growth" at some point in time.

### Limits on Stable Growth

- The stable growth rate cannot exceed the growth rate of the economy but it can be set lower.
  - If you assume that the economy is composed of high growth and stable growth firms, the growth rate of the latter will probably be lower than the growth rate of the economy.
  - The stable growth rate can be negative. The terminal value will be lower and you are assuming that your firm will disappear over time.
- If you use nominal cashflows and discount rates, the growth rate should be nominal in the currency in which the valuation is denominated. One simple proxy for the nominal growth rate of the economy is the riskfree rate.

### Stable Growth and Excess Returns

 Strange though this may seem, the terminal value is not as much a function of stable growth as it is a function of what you assume about excess returns in stable growth. In the scenario where you assume that a firm earns a return on capital equal to its cost of capital in stable growth, the terminal value will not change as the growth rate changes. If you assume that your firm will earn positive (negative) excess returns in perpetuity, the terminal value will increase (decrease) as the stable growth rate increases.

### Getting to stable growth: Determinants

#### Size of the firm

- Success usually makes a firm larger. As firms become larger, it becomes much more difficult for them to maintain high growth rates

#### Current growth rate

- While past growth is not always a reliable indicator of future growth, there is a correlation between current growth and future growth. Thus, a firm growing at 30% currently probably has higher growth and a longer expected growth period than one growing 10% a year now.

#### Barriers to entry and differential advantages

- Ultimately, high growth comes from high project returns, which, in turn, comes from barriers to entry and differential advantages.
- The question of how long growth will last and how high it will be can therefore be framed as a question about what the barriers to entry are, how long they will stay up and how strong they will remain.

### Stable Growth Characteristics

- In stable growth, firms should have the characteristics of other stable growth firms. In particular,
  - The risk of the firm, as measured by beta and ratings, should reflect that of a stable growth firm.
    - Beta should move towards one
    - The cost of debt should reflect the safety of stable firms (BBB or higher)
  - The debt ratio of the firm might increase to reflect the larger and more stable earnings of these firms.
    - The debt ratio of the firm might moved to the optimal or an industry average
    - If the managers of the firm are deeply averse to debt, this may never happen
  - The reinvestment rate of the firm should reflect the expected growth rate and the firm's return on capital
    - Reinvestment Rate = Expected Growth Rate / Return on Capital

### Titan and Amazon.com: Stable Growth Inputs

*High Growth Stable Growth*

#### Titan Cement

- Beta 0.93 1.00
- Debt Ratio 17.6% 17.6%
- Return on Capital 19.25% 6.57%
- Cost of Capital 6.78% 6.57%
- Expected Growth Rate 5.49% 3.41%
- Reinvestment Rate 28.54% 3.41%6.57% = 51.93%

#### Amazon.com

- Beta 1.60 1.00
- Debt Ratio 1.20% 15%
- Return on Capital Negative 20%
- Expected Growth Rate NMF 6%
- Reinvestment Rate >100% 6%/20% = 30%