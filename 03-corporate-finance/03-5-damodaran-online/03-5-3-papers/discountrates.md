---
title: "Discountrates"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/ovhds/dam2ed/discountrates.pdf
---

# Estimating Discount Rates

DCF Valuation

### Estimating Inputs: Discount Rates

- **Critical ingredient** in discounted cashflow valuation. Errors in estimating the discount rate or mismatching cashflows and discount rates can lead to serious errors in valuation. At an intuitive level, the discount rate used should be consistent with both the **riskiness** and the **type of cashflow** being discounted.
  - Equity versus Firm: If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital.
  - Currency: The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated.
  - Nominal versus Real: If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

### Cost of Equity

 The cost of equity should be higher for riskier investments and lower for safer investments While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (I.e, market or nondiversifiable risk)

## The Cost of Equity: Competing Models

| Model Expected Return           | Inputs Needed                   |
|---------------------------------|---------------------------------|
| CAPM E(R) = Rf + β (Rm- Rf      |                                 |
| )                               | Riskfree Rate                   |
| APM E(R) = Rf + Σ j=1 β j       |                                 |
| )                               | Riskfree Rate; # of Factors;    |
| Multi E(R) = Rf + Σ j=1,,N β j  |                                 |
| )                               | Riskfree Rate; Macro factors    |
| factor                          | Betas relative to macro factors |
| Proxy E(R) = a + Σ j=1..N bj Yj | Proxies                         |

### The CAPM: Cost of Equity

Consider the standard approach to estimating cost of equity:

Cost of Equity = 
$$R_f + \text{Equity Beta} * (E(R_m) - R_f)$$

where,

Rf = Riskfree rate

$$E(R_m) = \text{Expected Return on the Market Index (Diversified Portfolio)}$$

- In practice,
  - Short term government security rates are used as risk free rates
  - Historical risk premiums are used for the risk premium
  - Betas are estimated by regressing stock returns against market returns

### Short term Governments are not riskfree in valuation….

- On a riskfree asset, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. For an investment to be riskfree, then, it has to have
  - No default risk
- No reinvestment risk Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time. In valuation, the time horizon is generally infinite, leading to the conclusion that a long-term riskfree rate will always be preferable to a short term rate, if you have to pick one.

### Riskfree Rates in 2004

![](_page_6_Figure_1.jpeg)

### Estimating a Riskfree Rate when there are no default free entities….

- Estimate a range for the riskfree rate in local terms:
  - Approach 1: Subtract default spread from local government bond rate: Government bond rate in local currency terms - Default spread for Government in local currency
- Approach 2: Use forward rates and the riskless rate in an index currency (say Euros or dollars) to estimate the riskless rate in the local currency. Do the analysis in real terms (rather than nominal terms) using a real riskfree rate, which can be obtained in one of two ways –
  - from an inflation-indexed government bond, if one exists
- set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done. Do the analysis in a currency where you can get a riskfree rate, say US dollars.

### A Simple Test

- You are valuing Embraer, a Brazilian company, in U.S. dollars and are attempting to estimate a riskfree rate to use in the analysis. The riskfree rate that you should use is
- A. The interest rate on a Brazilian Real denominated long term bond issued by the Brazilian Government (15%)
- B. The interest rate on a US \$ denominated long term bond issued by the Brazilian Government (C-Bond) (10.30%)
- C. The interest rate on a US \$ denominated Brazilian Brady bond (which is partially backed by the US Government) (10.15%)
- D. The interest rate on a dollar denominated bond issued by Embraer (9.25%)
- E. The interest rate on a US treasury bond (4.29%)

### Everyone uses historical premiums, but..

- The historical premium is the premium that stocks have historically earned over riskless securities. Practitioners never seem to agree on the premium; it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. For instance, looking at the US:

| Historical Period | Stocks - T.Bills | Arithmetic average Stocks - T.Bonds | Stocks - T.Bills | Geometric Average Stocks - T.Bonds |
|-------------------|------------------|-------------------------------------|------------------|------------------------------------|
| 1928-2004         | 7.92%            | 6.53%                               | 6.02%            | 4.84%                              |
| 1964-2004         | 5.82%            | 4.34%                               | 4.59%            | 3.47%                              |
| 1994-2004         | 8.60%            | 5.82%                               | 6.85%            | 4.51%                              |

### If you choose to use historical premiums….

 Go back as far as you can. A risk premium comes with a standard error. Given the annual standard deviation in stock prices is about 25%, the standard error in a historical premium estimated over 25 years is roughly:

**Standard Error in Premium = 
$$25\%/\sqrt{25} = 25\%/5 = 5\%$$**

 Be consistent in your use of the riskfree rate. Since we argued for long term bond rates, the premium should be the one over T.Bonds Use the geometric risk premium. It is closer to how investors think about risk premiums over long periods.

### Risk Premium for a Mature Market? Broadening the sample

![](_page_11_Figure_1.jpeg)

### Two Ways of Estimating Country Equity Risk Premiums for other markets..

- *Default spread on Country Bond*: In this approach, the country equity risk premium is set equal to the default spread of the bond issued by the country (but only if it is denominated in a currency where a default free entity exists.
  - Brazil was rated B2 by Moody's and the default spread on the Brazilian dollar denominated C.Bond at the end of August 2004 was 6.01%. (10.30%-4.29%)

*Relative Equity Market approach*: The country equity risk premium is based upon the volatility of the market in question relative to U.S market.

Total equity risk premium = Risk Premium<sub>US</sub> \* 
$$\sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$$

Using a 4.82% premium for the US, this approach would yield:

Total risk premium for Brazil = 4.82% (34.56%/19.01%) = 8.76%

Country equity risk premium for Brazil = 8.76% - 4.82% = 3.94%

(The standard deviation in weekly returns from 2002 to 2004 for the Bovespa was 34.56% whereas the standard deviation in the S&P 500 was 19.01%)

### And a third approach

- Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads. Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. In this approach:
  - •  $\text{Country Equity risk premium} = \text{Default spread on country bond}^* \sigma_{\text{Country Equity}} / \sigma_{\text{Country Bond}}$
  - Country Equity Risk Premium = 6.01% (34.56%/26.34%) = 7.89%

### Can country risk premiums change? Updating Brazil in January 2004

- Brazil's financial standing and country rating improved dramatically towards the end of 2004. Its rating improved to B1. In January 2005, the interest rate on the Brazilian C-Bond dropped to 7.73%. The US treasury bond rate that day was 4.22%, yielding a default spread of 3.51% for Brazil.
  - Standard Deviation in Bovespa (Equity) = 25.09%
  - Standard Deviation in Brazil C-Bond = 15.12%
  - Default spread on C-Bond = 3.51%
  - Country Risk Premium for Brazil = 3.51% (25.09%/15.12%) = 5.82%

### From Country Equity Risk Premiums to Corporate Equity Risk premiums

 Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country ERP} + \text{Beta (US premium)}$$

Implicitly, this is what you are assuming when you use the local Government's dollar borrowing rate as your riskfree rate.

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium} + \text{Country ERP)}$$

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium})+\lambda (\text{Country ERP})$$

*ERP: Equity Risk Premium*

### Estimating Company Exposure to Country Risk: Determinants

 Source of revenues: Other things remaining equal, a company should be more exposed to risk in a country if it generates more of its revenues from that country. A Brazilian firm that generates the bulk of its revenues in Brazil should be more exposed to country risk than one that generates a smaller percent of its business within Brazil. Manufacturing facilities: Other things remaining equal, a firm that has all of its production facilities in Brazil should be more exposed to country risk than one which has production facilities spread over multiple countries. The problem will be accented for companies that cannot move their production facilities (mining and petroleum companies, for instance). Use of risk management products: Companies can use both options/futures markets and insurance to hedge some or a significant portion of country risk.

### Estimating Lambdas: The Revenue Approach

 The easiest and most accessible data is on revenues. Most companies break their revenues down by region. One simplistic solution would be to do the following:

$$\lambda = \%$$
 of revenues domestically\_firm /  $\%$  of revenues domestically\_avg\_firm

 Consider, for instance, Embraer and Embratel, both of which are incorporated and traded in Brazil. Embraer gets 3% of its revenues from Brazil whereas Embratel gets almost all of its revenues in Brazil. The average Brazilian company gets about 77% of its revenues in Brazil:

- LambdaEmbraer = 3%/ 77% = .04
- LambdaEmbratel = 100%/77% = 1.30

- There are two implications
  - A company's risk exposure is determined by where it does business and not by where it is located
  - Firms might be able to actively manage their country risk exposures

### Estimating Lambdas: Earnings Approach

![](_page_18_Figure_2.jpeg)

### Estimating Lambdas: Stock Returns versus C-Bond Returns

ReturnEmbraer = 0.0195 + **0.2681** ReturnC Bond

ReturnEmbratel = -0.0308 + **2.0030** ReturnC Bond

![](_page_19_Figure_4.jpeg)

![](_page_19_Figure_6.jpeg)

### Estimating a US Dollar Cost of Equity for Embraer - September 2004

 Assume that the beta for Embraer is 1.07, and that the riskfree rate used is 4.29%. Also assume that the risk premium for the US is 4.82% and the country risk premium for Brazil is 7.89%. Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

E(Return) = 4.29% + 1.07 (4.82%) + 7.89% = 17.34%

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

E(Return) = 4.29 % + 1.07 (4.82%+ 7.89%) = 17.89%

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

E(Return)= 4.29% + 1.07(4.82%) + 0.27 (7.89%) = 11.58%

### Valuing Emerging Market Companies with significant exposure in developed markets

- The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk. Thus, Embraer would have been valued with a cost of equity of 17.34% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
- A. Emerging market companies with substantial exposure in developed markets will be significantly over valued by equity research analysts.
- B. Emerging market companies with substantial exposure in developed markets will be significantly under valued by equity research analysts. Can you construct an investment strategy to take advantage of the misvaluation?

### Implied Equity Premiums

 If we assume that stocks are correctly priced in the aggregate and we can estimate the expected cashflows from buying stocks, we can estimate the expected rate of return on stocks by computing an internal rate of return. Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

### Implied Equity Premiums

 We can use the information in stock prices to back out how risk averse the market is and how much of a risk premium it is demanding.

If you pay the current level of the index, you can expect to make a return of 7.87% on stocks (which

If you bay the current of the index you can expect to make a return of 
$$\frac{38.13}{(1+r)} + \frac{41.37}{(1+r)^2} + \frac{44.89}{(1+r)^3} + \frac{48.71}{(1+r)^4} + \frac{52.85}{(1+r)^5} + \frac{52.85(1.0422)}{(r-.0422)(1+r)^5}$$

 Implied Equity risk premium = Expected return on stocks - Treasury bond rate = 7.87% - 4.22% = 3.65%

| Business Networks             | Comparable firms                                  | Number of firms       | Average levered beta | Median D/E            | Unlevered beta | Casch/Firm Value | Corrected for cash |
|-------------------------------|---------------------------------------------------|-----------------------|----------------------|-----------------------|----------------|------------------|--------------------|
| Media Networks                | Radia and TV broadcasting companies               | 24                    | 1.23                 | 20.45%                | 1.08           | 0.75%            | 1.093              |
| Parks and Resorts             | Theme park & Entertainment firms                  | 9                     | 1.63                 | 120.76%               | 0.91           | 2.77%            | 0.936              |
| Studio Entertainment          | Movie companies                                   | 11                    | 1.35                 | 27.96%                | 1.14           | 14.08%           | 1.331              |
| Consumer Products             | Toy and apparel retailers; Entertainment software | 77                    | 1.14                 | 9.18%                 | 1.07           | 12.08%           | 1.218              |
| Business                      | Revenues in 2002                                  | EV/Sales              | Estimated Value      | Firm Value Proportion | Unlevered beta |                  |                    |
| Media Networks                | \$9,733                                           | 3.41                  | \$33,162.67          | 47.32%                | 1.0932         |                  |                    |
| Parks and Resorts             | \$6,465                                           | 2.37                  | \$15,334.08          | 21.88%                | 0.9364         |                  |                    |
| Studio Entertainment          | \$6,691                                           | 2.63                  | \$17,618.07          | 25.14%                | 1.3310         |                  |                    |
| Consumer Products             | \$2,440                                           | 1.63                  | \$3,970.60           | 5.67%                 | 1.2188         |                  |                    |
| Disney                        | \$25,329                                          |                       | \$70,085.42          | 100.00%               | 1.1258         |                  |                    |
| <i>Business</i>               | <i>Unlevered Beta</i>                             | <i>D/E Ratio</i>      | <i>Levered beta</i>  |                       |                |                  |                    |
| Aerospace                     | 0.95                                              | 18.95%                | 1.07                 |                       |                |                  |                    |
| If Interest Coverage Ratio is |                                                   | Estimated Bond Rating | Default Spread(2003) | Default Spread(2004)  |                |                  |                    |
| > 8.50                        | (>12.50)                                          | AAA                   | 0.75%                | 0.35%                 |                |                  |                    |
| 6.50 - 8.50                   | (9.5-12.5)                                        | AA                    | 1.00%                | 0.50%                 |                |                  |                    |
| 5.50 - 6.50                   | (7.5-9.5)                                         | A+                    | 1.50%                | 0.70%                 |                |                  |                    |
| 4.25 - 5.50                   | (6-7.5)                                           | A                     | 1.80%                | 0.85%                 |                |                  |                    |
| 3.00 - 4.25                   | (4.5-6)                                           | A–                    | 2.00%                | 1.00%                 |                |                  |                    |
| 2.50 - 3.00                   | (4-4.5)                                           | BBB                   | 2.25%                | 1.50%                 |                |                  |                    |
| 2.25- 2.50                    | (3.5-4)                                           | BB+                   | 2.75%                | 2.00%                 |                |                  |                    |
| 2.00 - 2.25                   | ((3-3.5)                                          | BB                    | 3.50%                | 2.50%                 |                |                  |                    |
| 1.75 - 2.00                   | (2.5-3)                                           | B+                    | 4.75%                | 3.25%                 |                |                  |                    |
| 1.50 - 1.75                   | (2-2.5)                                           | B                     | 6.50%                | 4.00%                 |                |                  |                    |
| 1.25 - 1.50                   | (1.5-2)                                           | B –                   | 8.00%                | 6.00%                 |                |                  |                    |
| 0.80 - 1.25                   | (1.25-1.5)                                        | CCC                   | 10.00%               | 8.00%                 |                |                  |                    |
| 0.65 - 0.80                   | (0.8-1.25)                                        | CC                    | 11.50%               | 10.00%                |                |                  |                    |
| 0.20 - 0.65                   | (0.5-0.8)                                         | C                     | 12.70%               | 12.00%                |                |                  |                    |
| < 0.20                        | (<0.5)                                            | D                     | 15.00%               | 20.00%                |                |                  |                    |