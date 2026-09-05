---
title: "Dcfval"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/ovhds/inv2E/dcfval.pdf
---

# Valuation: Lecture Note Packet 1 Intrinsic Valuation

Aswath Damodaran

Updated: September 2011

#### The essence of intrinsic value

 In intrinsic valuation, you value an asset based upon its intrinsic characteristics. For cash flow generating assets, the intrinsic value will be a function of the magnitude of the expected cash flows on the asset over its lifetime and the uncertainty about receiving those cash flows. Discounted cash flow valuation is a tool for estimating intrinsic value, where the expected value of an asset is written as the present value of the expected cash flows on the asset, with either the cash flows or the discount rate adjusted to reflect the risk.

#### The two faces of discounted cash flow valuation

 The value of a risky asset can be estimated by discounting the expected cash flows on the asset over its life at a risk-adjusted discount rate:

| Value of asset = | $\frac{E(CF_1)}{(1+r)} + \frac{E(CF_2)}{(1+r)^2} + \frac{E(CF_3)}{(1+r)^3} \dots + \frac{E(CF_n)}{(1+r)^n}$ |
|------------------|-------------------------------------------------------------------------------------------------------------|
|------------------|-------------------------------------------------------------------------------------------------------------|

where the asset has a n-year life, E(CFt ) is the expected cash flow in period t and r is a discount rate that reflects the risk of the cash flows.

 Alternatively, we can replace the expected cash flows with the guaranteed cash flows we would have accepted as an alternative (certainty equivalents) and discount these at the riskfree rate:

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r_f)} + \frac{\text{CE}(\text{CF}_2)}{(1+r_f)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r_f)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r_f)^n}$$

where CE(CFt ) is the certainty equivalent of E(CFt ) and rf is the riskfree rate.

#### Risk Adjusted Value: Two Basic Propositions

$$\text{Value of asset} = \frac{\text{CE}(\text{CF}_1)}{(1+r)^1} + \frac{\text{CE}(\text{CF}_2)}{(1+r)^2} + \frac{\text{CE}(\text{CF}_3)}{(1+r)^3} \dots + \frac{\text{CE}(\text{CF}_n)}{(1+r)^n}$$

**Proposition 1: For an asset to have value, the expected cash flows have to be positive some time over the life of the asset.**

**Proposition 2: Assets that generate cash flows early in their life will be worth more than assets that generate cash flows later; the latter may however have greater growth and higher cash flows to compensate.**

#### DCF Choices: Equity Valuation versus Firm Valuation

![](_page_4_Diagram_2.jpeg)

**Equity valuation**: Value just the equity claim in the business

**Firm Valuation**: Value the entire business

#### Equity Valuation

![](_page_5_Diagram_2.jpeg)

#### Firm Valuation

![](_page_6_Diagram_1.jpeg)

## Firm Value and Equity Value

- To get from firm value to equity value, which of the following would you need to do?
- A. Subtract out the value of long term debt
- B. Subtract out the value of all debt
- C. Subtract the value of any debt that was included in the cost of capital calculation
- D. Subtract out the value of all liabilities in the firm Doing so, will give you a value for the equity which is
- A. greater than the value you would have got in an equity valuation
- B. lesser than the value you would have got in an equity valuation
- C. equal to the value you would have got in an equity valuation

## Cash Flows and Discount Rates

 Assume that you are analyzing a company with the following cashflows for the next five years.

| Year           | CF to Equity | Interest Exp (1-tax rate) | CF to Firm  |
|----------------|--------------|---------------------------|-------------|
| 1              | \$ 50        | \$ 40                     | \$ 90       |
| 2              | \$ 60        | \$ 40                     | \$ 100      |
| 3              | \$ 68        | \$ 40                     | \$ 108      |
| 4              | \$ 76.2      | \$ 40                     | \$ 116.2    |
| 5              | \$ 83.49     | \$ 40                     | \$ 123.49   |
| Terminal Value | \$ 1603.0    |                           | \$ 2363.008 |

 Assume also that the cost of equity is 13.625% and the firm can borrow long term at 10%. (The tax rate for the firm is 50%.) The current market value of equity is \$1,073 and the value of debt outstanding is \$800.

#### Equity versus Firm Valuation

#### *Method 1: Discount CF to Equity at Cost of Equity to get value of equity*

- Cost of Equity = 13.625%
- Value of Equity = 50/1.13625 + 60/1.136252 + 68/1.136253 + 76.2/1.136254 + (83.49+1603)/1.136255 = \$1073

#### *Method 2: Discount CF to Firm at Cost of Capital to get value of firm*

Cost of Debt = Pre-tax rate (1- tax rate) = 10% (1-.5) = 5%

WACC = 13.625% (1073/1873) + 5% (800/1873) = 9.94%

| <span></span>                                                                                                                                    |  | <span></span> |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--|---------------|
| <div>PV of Firm = <math display="block">90/1.0994 + 100/1.0994^2 + 108/1.0994^3 + 116.2/1.0994^4 + (123.49+2363)/1.0994^5 = \\$1873</math></div> |  |               |

Value of Equity = Value of Firm - Market Value of Debt = \$ 1873 - \$ 800 = \$1073

## First Principle of Valuation

 Never mix and match cash flows and discount rates. The key error to avoid is mismatching cashflows and discount rates, since discounting cashflows to equity at the weighted average cost of capital will lead to an upwardly biased estimate of the value of equity, while discounting cashflows to the firm at the cost of equity will yield a downward biased estimate of the value of the firm.

## The Effects of Mismatching Cash Flows and Discount Rates

*Error 1: Discount CF to Equity at Cost of Capital to get equity value*

PV of Equity = 50/1.0994 + 60/1.09942 + 68/1.09943 + 76.2/1.09944 + (83.49+1603)/ 1.09945 = \$1248

Value of equity is overstated by \$175.

*Error 2: Discount CF to Firm at Cost of Equity to get firm value*

PV of Firm = 
$$90/1.13625 + 100/1.13625^2 + 108/1.13625^3 + 116.2/1.13625^4 + (123.49+2363)/1.13625^5 = \$1613$$

PV of Equity = \$1612.86 - \$800 = \$813

Value of Equity is understated by \$ 260.

*Error 3: Discount CF to Firm at Cost of Equity, forget to subtract out debt, and get too high a value for equity*

Value of Equity = \$ 1613

Value of Equity is overstated by \$ 540

## Discounted Cash Flow Valuation: The Steps

- Estimate the **discount rate** or rates to use in the valuation
  - Discount rate can be either a cost of equity (if doing equity valuation) or a cost of capital (if valuing the firm)
  - Discount rate can be in nominal terms or real terms, depending upon whether the cash flows are nominal or real
- Discount rate can vary across time. Estimate the **current earnings** and **cash flows** on the asset, to either equity investors (CF to Equity) or to all claimholders (CF to Firm) Estimate the **future earnings and cash flows** on the firm being valued, generally by estimating an expected growth rate in earnings. Estimate **when** the firm will reach "**stable growth**" and what characteristics (risk & cash flow) it will have when it does. Choose the **right DCF model** for this asset and value it.

#### Generic DCF Valuation Model

![](_page_13_Diagram_1.jpeg)

![](_page_14_Diagram_1.jpeg)

#### EQUITY VALUATION WITH DIVIDENDS

**Cashflow to Equity**

Net Income

- (Cap Ex - Depr) (1- DR)

- Change in WC (!-DR)

= FCFE

**Expected Growth**

Retention Ratio \*

Return on Equity

FCFE1 FCFE2 FCFE3 FCFE4 FCFE5

Forever

Firm is in stable growth:

Grows at constant rate forever

Terminal Value= FCFE n+1/(ke-gn)

FCFEn .........

**Cost of Equity**

Financing Weights Debt Ratio = DR

*Discount at* Cost of Equity

Value of Equity

**Riskfree Rate** :

- No default risk

- No reinvestment risk

- In same currency and

in same terms (real or nominal as cash flows

+

**Beta**

- Measures market risk **X**

**Risk Premium**

- Premium for average risk investment

Type of Business Operating Leverage

Financial Leverage Base Equity Premium

Country Risk Premium

#### EQUITY VALUATION WITH FCFE

![](_page_16_Diagram_1.jpeg)

#### VALUING A FIRM

# Discounted Cash Flow Valuation: The Inputs

Aswath Damodaran

---

# I. Estimating Discount Rates

## DCF Valuation

## Estimating Inputs: Discount Rates

- **Critical ingredient** in discounted cashflow valuation. Errors in estimating the discount rate or mismatching cashflows and discount rates can lead to serious errors in valuation. At an intuitive level, the discount rate used should be consistent with both the **riskiness** and the **type of cashflow** being discounted.
  - Equity versus Firm: If the cash flows being discounted are cash flows to equity, the appropriate discount rate is a cost of equity. If the cash flows are cash flows to the firm, the appropriate discount rate is the cost of capital.
  - Currency: The currency in which the cash flows are estimated should also be the currency in which the discount rate is estimated.
  - Nominal versus Real: If the cash flows being discounted are nominal cash flows (i.e., reflect expected inflation), the discount rate should be nominal

## Cost of Equity

 The cost of equity should be higher for riskier investments and lower for safer investments While risk is usually defined in terms of the variance of actual returns around an expected return, risk and return models in finance assume that the risk that should be rewarded (and thus built into the discount rate) in valuation should be the risk perceived by the marginal investor in the investment Most risk and return models in finance also assume that the marginal investor is well diversified, and that the only risk that he or she perceives in an investment is risk that cannot be diversified away (I.e, market or non-diversifiable risk)

## The Cost of Equity: Competing Models

| Model  | Expected Return          | Inputs Needed                   |
|--------|--------------------------|---------------------------------|
| CAPM   | E(R) = Rf + β (Rm- Rf    |                                 |
|        | )                        | Riskfree Rate                   |
| APM    | E(R) = Rf + Σ j=1 β j    |                                 |
|        | )                        | Riskfree Rate; # of Factors;    |
| Multi  | E(R) = Rf + Σ j=1,,N β j |                                 |
|        |                          | ) Riskfree Rate; Macro factors  |
| factor |                          | Betas relative to macro factors |
| Proxy  | E(R) = a + Σ j=1..N bj   |                                 |
|        | Yj                       | Proxies                         |

## The CAPM: Cost of Equity

- Consider the standard approach to estimating cost of equity: Cost of Equity = Riskfree Rate + Equity Beta \* (Equity Risk Premium) In practice,
  - Government security rates are used as risk free rates
  - Historical risk premiums are used for the risk premium
  - Betas are estimated by regressing stock returns against market returns

#### A Riskfree Rate

- On a riskfree asset, the actual return is equal to the expected return. Therefore, there is no variance around the expected return. For an investment to be riskfree, then, it has to have
  - No default risk
  - No reinvestment risk
- 1. Time horizon matters: Thus, the riskfree rates in valuation will depend upon when the cash flow is expected to occur and will vary across time.
- 2. Not all government securities are riskfree: Some governments face default risk and the rates on bonds issued by them will not be riskfree.

#### Test 1: A riskfree rate in US dollars!

- In valuation, we estimate cash flows forever (or at least for very long time periods). The right risk free rate to use in valuing a company in US dollars would be
- a) A three-month Treasury bill rate
- b) A ten-year Treasury bond rate
- c) A thirty-year Treasury bond rate
- d) A TIPs (inflation-indexed treasury) rate
- e) None of the above

![](_page_24_Figure_2.jpeg)

#### Test 2: A Riskfree Rate in Euros

![](_page_25_Figure_1.jpeg)

## Test 3: A Riskfree Rate in Indian Rupees

- The Indian government had 10-year Rupee bonds outstanding, with a yield to maturity of about 8.5% on January 1, 2012. In January 2012, the Indian government had a local currency sovereign rating of Baa3. The typical default spread (over a default free rate) for Baa3 rated country bonds in early 2012 was 2%. The riskfree rate in Indian Rupees is
- a) The yield to maturity on the 10-year bond (8.5%)
- b) The yield to maturity on the 10-year bond + Default spread (10.5%)
- c) The yield to maturity on the 10-year bond Default spread (6.5%)
- d) None of the above

## Sovereign Default Spread: Two paths to the same destination…

 Sovereign dollar or euro denominated bonds: Find sovereign bonds denominated in US dollars, issued by emerging markets. The difference between the interest rate on the bond and the US treasury bond rate should be the default spread. For instance, in January 2012, the US dollar denominated 10-year bond issued by the Brazilian government (with a Baa2 rating) had an interest rate of 3.5%, resulting in a default spread of 1.6% over the US treasury rate of 1.9% at the same point in time. (On the same day, the ten-year Brazilian BR denominated bond had an interest rate of 12%) CDS spreads: Obtain the default spreads for sovereigns in the CDS market. In January 2012, the CDS spread for Brazil in that market was 1.43%. Average spread: For countries which don't issue dollar denominated bonds or have a CDS spread, you have to use the average spread for other countries in the same rating class.

# Sovereign Default Spreads: End of 2011

---

| <i>Rating</i> | <i>Default spread in basis points</i> |
|---------------|---------------------------------------|
| Aaa           | 0                                     |
| Aa1           | 25                                    |
| A2            | 50                                    |
| Aa3           | 70                                    |
| A1            | 85                                    |
| A2            | 100                                   |
| A3            | 115                                   |
| Baa1          | 150                                   |
| Baa2          | 175                                   |
| Baa3          | 200                                   |
| Ba1           | 240                                   |
| Ba2           | 275                                   |
| Ba3           | 325                                   |
| B1            | 400                                   |
| B2            | 500                                   |
| B3            | 600                                   |
| Caa1          | 700                                   |
| Caa2          | 850                                   |
| Caa3          | 1000                                  |

#### Revisiting US treasuries: What is the right riskfree rate in US dollars?

![](_page_29_Figure_1.jpeg)

#### Test 4: A Real Riskfree Rate

- In some cases, you may want a riskfree rate in real terms (in real terms) rather than nominal terms. To get a real riskfree rate, you would like a security with no default risk and a guaranteed real return. Treasury indexed securities offer this combination. In January 2012, the yield on a 10-year indexed treasury bond was 1.00%. Which of the following statements would you subscribe to?
- a) This (1.00%) is the real riskfree rate to use, if you are valuing US companies in real terms.
- b) This (1.00%) is the real riskfree rate to use, anywhere in the world Explain.

## No default free entity: Choices with riskfree rates….

- Estimate a range for the riskfree rate in local terms:
  - Approach 1: Subtract default spread from local government bond rate: Government bond rate in local currency terms - Default spread for Government in local currency
- Approach 2: Use forward rates and the riskless rate in an index currency (say Euros or dollars) to estimate the riskless rate in the local currency. Do the analysis in real terms (rather than nominal terms) using a real riskfree rate, which can be obtained in one of two ways –
  - from an inflation-indexed government bond, if one exists
- set equal, approximately, to the long term real growth rate of the economy in which the valuation is being done. Do the analysis in a currency where you can get a riskfree rate, say US dollars or Euros.

## Why do riskfree rates vary across currencies? January 2012 Risk free rates

![](_page_32_Figure_1.jpeg)

#### One more test on riskfree rates…

- In January 2012, the 10-year treasury bond rate in the United States was 1.87%, a historic low. Assume that you were valuing a company in US dollars then, but were wary about the riskfree rate being too low. Which of the following should you do?
- a) Replace the current 10-year bond rate with a more reasonable normalized riskfree rate (the average 10-year bond rate over the last 30 years has been about 4%)
- b) Use the current 10-year bond rate as your riskfree rate but make sure that your other assumptions (about growth and inflation) are consistent with the riskfree rate
- c) Something else…

## B. Equity Risk Premiums The ubiquitous historical risk premium

- The historical premium is the premium that stocks have historically earned over riskless securities. While the users of historical risk premiums act as if it is a fact (rather than an estimate), it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. For instance, looking at the US:

| " "       | Stocks - T. Bills | Arithmetic Average Stocks - T. Bonds | Stocks - T. Bills | Geometric Average Stocks - T. Bonds |
|-----------|-------------------|--------------------------------------|-------------------|-------------------------------------|
| 1928-2011 | 7.55%             | 5.79%                                | 5.62%             | 4.10%                               |
| Std error | 2.22%             | 2.36%                                | "                 | "                                   |
| 1962-2011 | 5.38%             | 3.36%                                | 4.02%             | 2.35%                               |
| Std error | 2.39%             | 2.68%                                | "                 | "                                   |
| 2002-2011 | 3.12%             | -1.92%                               | 1.08%             | -3.61%                              |
| Std error | 6.46%             | 8.94%                                | "                 | "                                   |

## The perils of trusting the past…….

 Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 80 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

Standard Error in Premium = 
$$20\%/\sqrt{80} = 2.26\%$$

(An aside: The implied standard deviation in equities rose to almost 50% during the last quarter of 2008. Think about the consequences for using historical risk premiums, if this volatility persisted)

 Survivorship Bias: Using historical data from the U.S. equity markets over the twentieth century does create a sampling bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

## Risk Premium for a Mature Market? Broadening the sample

![](_page_36_Figure_1.jpeg)

## Two Ways of Estimating Country Equity Risk Premiums for other markets.. Brazil in August 2004

- ■ *Default spread on Country Bond:* In this approach, the country equity risk premium is set equal to the default spread of the bond issued by the country (but only if it is denominated in a currency where a default free entity exists.
- Brazil was rated B2 by Moody's and the default spread on the Brazilian dollar denominated C.Bond at the end of August 2004 was 6.01%. (10.30%-4.29%)
  **Relative Equity Market approach:** The country equity risk premium is based upon the volatility of the market in question relative to U.S market.Total equity risk premium = Risk Premium<sub>US</sub> \*  $\sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$ 

  Using a 4.82% premium for the US (the historical premium from 1928-2003), this approach would yield:

  Total risk premium for Brazil = 4.82% (34.56%/19.01%) = 8.76%

  Country equity risk premium for Brazil = 8.76% - 4.82% = 3.94%

  (The standard deviation in weekly returns from 2002 to 2004 for the Bovespa was 34.56% whereas the standard deviation in the S&P 500 was 19.01%)

#### And a third approach

- Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads. Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. Using this approach for Brazil in August 2004, you would get:
  - Country Equity risk premium = Default spread on country bond\*  $\sigma_{\text{Country Equity}}$  /  $\sigma_{\text{Country Bond}}$
  - Country Equity Risk Premium = 6.01% (34.56%/26.34%) = 7.89%

## Can country risk premiums change? Updating Brazil – January 2007 and January 2009

- In January 2007, Brazil's rating had improved to B1 and the interest rate on the Brazilian \$ denominated bond dropped to 6.2%. The US treasury bond rate that day was 4.7%, yielding a default spread of 1.5% for Brazil.
  - Standard Deviation in Bovespa (Equity) = 24%
  - Standard Deviation in Brazil \$-Bond = 12%
  - Default spread on Brazil \$-Bond = 1.50%
  - Country Risk Premium for Brazil = 1.50% (24/12) = 3.00%

On January 1, 2009, Brazil's rating was Ba1 but the interest rate on the Brazilian \$ denominated bond was 6.3%, 4.1% higher than the US treasury bond rate of 2.2% on that day.

- Standard Deviation in Bovespa (Equity) = 33%
- Standard Deviation in Brazil \$-Bond = 20%
- Default spread on Brazil \$-Bond = 4.1%
- Country Risk Premium for Brazil = 4.10% (33/20) = 6.77%

#### *Country Risk Premiums January 2012*

| Angola       | 10.88% |
|--------------|--------|
| Botswana     | 7.50%  |
| Egypt        | 13.50% |
| Mauritius    | 8.63%  |
| Morocco      | 9.60%  |
| Namibia      | 9.00%  |
| South Africa | 7.73%  |
| Tunisia      | 9.00%  |

| Bangladesh   | 10.88% |
|--------------|--------|
| Cambodia     | 13.50% |
| China        | 7.05%  |
| Fiji Islands | 12.00% |
| Hong Kong    | 6.38%  |
| India        | 9.00%  |
| Indonesia    | 9.60%  |
| Japan        | 7.05%  |
| Korea        | 7.28%  |
| Macao        | 7.05%  |
| Malaysia     | 7.73%  |
| Mongolia     | 12.00% |
| Pakistan     | 15.00% |
| Guinea       | 12.00% |
| Philippines  | 10.13% |
| Singapore    | 6.00%  |
| Sri Lanka    | 12.00% |
| Taiwan       | 7.05%  |
| Thailand     | 8.25%  |
| Turkey       | 10.13% |
| Vietnam      | 12.00% |

|  | Australia   | 6.00% |
|--|-------------|-------|
|  | New Zealand | 6.00% |

| Argentina   | 15.00% |
|-------------|--------|
| Belize      | 15.00% |
| Bolivia     | 12.00% |
| Brazil      | 8.63%  |
| Chile       | 7.05%  |
| Colombia    | 9.00%  |
| Costa Rica  | 9.00%  |
| Ecuador     | 18.75% |
| El Salvador | 10.13% |
| Guatemala   | 9.60%  |
| Honduras    | 13.50% |
| Mexico      | 8.25%  |
| Nicaragua   | 15.00% |
| Panama      | 9.00%  |
| Paraguay    | 12.00% |
| Peru        | 9.00%  |
| Uruguay     | 9.60%  |
| Venezuela   | 12.00% |

| Albania        | 12.00% |
|----------------|--------|
| Armenia        | 10.13% |
| Azerbaijan     | 9.60%  |
| Belarus        | 15.00% |
| Herzegovina    | 13.50% |
| Bulgaria       | 8.63%  |
| Croatia        | 9.00%  |
| Czech Republic | 7.28%  |
| Estonia        | 7.28%  |
| Georgia        | 10.88% |
| Hungary        | 9.60%  |
| Kazakhstan     | 8.63%  |
| Latvia         | 9.00%  |
| Lithuania      | 8.25%  |
| Moldova        | 15.00% |
| Montenegro     | 10.88% |
| Poland         | 7.50%  |
| Romania        | 9.00%  |
| Russia         | 8.25%  |
| Slovakia       | 7.28%  |
| Slovenia [1]   | 7.28%  |
| Ukraine        | 13.50% |

| Bahrain              | 8.25%  |
|----------------------|--------|
| Israel               | 7.28%  |
| Jordan               | 10.13% |
| Kuwait               | 6.75%  |
| Lebanon              | 12.00% |
| Oman                 | 7.28%  |
| Qatar                | 6.75%  |
| Saudi Arabia         | 7.05%  |
| Senegal              | 12.00% |
| United Arab Emirates | 6.75%  |

| Canada                   | 6.00% |
|--------------------------|-------|
| United States of America | 6.00% |

| Austria [1]     | 6.00%  |
|-----------------|--------|
| Belgium [1]     | 7.05%  |
| Cyprus [1]      | 9.00%  |
| Denmark         | 6.00%  |
| Finland [1]     | 6.00%  |
| France [1]      | 6.00%  |
| Germany [1]     | 6.00%  |
| Greece [1]      | 16.50% |
| Iceland         | 9.00%  |
| Ireland [1]     | 9.60%  |
| Italy [1]       | 7.50%  |
| Malta [1]       | 7.50%  |
| Netherlands [1] | 6.00%  |
| Norway          | 6.00%  |
| Portugal [1]    | 10.13% |
| Spain [1]       | 7.28%  |
| Sweden          | 6.00%  |
| Switzerland     | 6.00%  |
| United Kingdom  | 6.00%  |

## From Country Equity Risk Premiums to Corporate Equity Risk premiums

 Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

**$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country ERP} + \text{Beta (US premium)}$$**

Implicitly, this is what you are assuming when you use the local Government's dollar borrowing rate as your riskfree rate.

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

**$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium} + \text{Country ERP})$$**

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

**$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium}) + \lambda (\text{Country ERP})$$**

*ERP: Equity Risk Premium*

## Estimating Company Exposure to Country Risk: Determinants

 Source of revenues: Other things remaining equal, a company should be more exposed to risk in a country if it generates more of its revenues from that country. A Brazilian firm that generates the bulk of its revenues in Brazil should be more exposed to country risk than one that generates a smaller percent of its business within Brazil. Manufacturing facilities: Other things remaining equal, a firm that has all of its production facilities in Brazil should be more exposed to country risk than one which has production facilities spread over multiple countries. The problem will be accented for companies that cannot move their production facilities (mining and petroleum companies, for instance). Use of risk management products: Companies can use both options/ futures markets and insurance to hedge some or a significant portion of country risk.

#### Estimating Lambdas: The Revenue Approach

- ■ The easiest and most accessible data is on revenues. Most companies break their revenues down by region.
   
   $\lambda = \% \text{ of revenues domestically}_{\text{firm}} / \% \text{ of revenues domestically}_{\text{avg firm}}$

  ■ Consider, for instance, Embraer and Embratel, both of which are incorporated and traded in Brazil. Embraer gets 3% of its revenues from Brazil whereas Embratel gets almost all of its revenues in Brazil. The average Brazilian company gets about 77% of its revenues in Brazil:
- LambdaEmbratel = 100%/77% = 1.30 There are two implications
  - A company's risk exposure is determined by where it does business and not by where it is located
- Firms might be able to actively manage their country risk exposures Consider, for instance, the fact that SAP got about 7.5% of its sales in "Emerging Asia", we can estimate a lambda for SAP for Asia (using the assumption that the typical Asian firm gets about 75% of its revenues in Asia)
  - LambdaSAP, Asia = 7.5%/ 75% = 0.10

## Estimating Lambdas: Earnings Approach

![](_page_44_Figure_1.jpeg)

#### Estimating Lambdas: Stock Returns versus C-Bond Returns

Embraer versus C Bond: 2000-2003

![](_page_45_Figure_4.jpeg)

Embratel versus C Bond: 2000-2003

![](_page_45_Figure_6.jpeg)

ReturnEmbraer = 0.0195 + **0.2681** ReturnC Bond

ReturnEmbratel = -0.0308 + **2.0030** ReturnC Bond

## Estimating a US Dollar Cost of Equity for Embraer - September 2004

- ■ Assume that the beta for Embraer is 1.07, and that the riskfree rate used is 4.29%. Also assume that the risk premium for the US is 4.82% and the country risk premium for Brazil is 7.89%.
- ■ Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,  
   $E(\text{Return}) = 4.29\% + 1.07(4.82\%) + 7.89\% = 17.34\%$
- ■ Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.  
   $E(\text{Return}) = 4.29\% + 1.07(4.82\% + 7.89\%) = 17.89\%$
- ■ Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)  
   $E(\text{Return}) = 4.29\% + 1.07(4.82\%) + 0.27(7.89\%) = 11.58\%$

## Valuing Emerging Market Companies with significant exposure in developed markets

- The conventional practice in investment banking is to add the country equity risk premium on to the cost of equity for every emerging market company, notwithstanding its exposure to emerging market risk. Thus, in 2004, Embraer would have been valued with a cost of equity of 17.34% even though it gets only 3% of its revenues in Brazil. As an investor, which of the following consequences do you see from this approach?
- A. Emerging market companies with substantial exposure in developed markets will be significantly over valued by equity research analysts.
- B. Emerging market companies with substantial exposure in developed markets will be significantly under valued by equity research analysts.

Can you construct an investment strategy to take advantage of the misvaluation?

## Implied Equity Premiums

 If we assume that stocks are correctly priced in the aggregate and we can estimate the expected cashflows from buying stocks, we can estimate the expected rate of return on stocks by computing an internal rate of return. Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

#### Implied Equity Premiums: January 2008

 We can use the information in stock prices to back out how risk averse the market is and how much of a risk premium it is demanding.

 If you pay the current level of the index, you can expect to make a return of 8.39% on stocks (which is obtained by solving for r in the following equation)

 Implied Equity risk premium = Expected return on stocks - Treasury bond rate = 8.39% - 4.02% = 4.37%

| $1468.36 = \frac{61.98}{(1+r)} + \frac{65.08}{(1+r)^2} + \frac{68.33}{(1+r)^3} + \frac{71.75}{(1+r)^4} + \frac{75.34}{(1+r)^5} + \frac{75.35(1.0402)}{(r-.0402)(1+r)^5}$ |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](_page_49_Figure_2.jpeg)

## Implied Risk Premium Dynamics

 Assume that the index jumps 10% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease Assume that the earnings jump 10% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease Assume that the riskfree rate increases to 5% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease

## A year that made a difference.. The implied premium in January 2009

|            | Year " Market value of index | Dividends | "       | Buybacks " | Cash to equity " | Dividend yield " | Buyback yield " Total yield | " |
|------------|------------------------------|-----------|---------|------------|------------------|------------------|-----------------------------|---|
| 2001       | " 1148.09                    | 15.74     | " 14.34 | " 30.08    | " 1.37%          | " 1.25%          | " 2.62%                     | " |
| 2002       | " 879.82                     | 15.96     | " 13.87 | " 29.83    | " 1.81%          | " 1.58%          | " 3.39%                     | " |
| 2003       | " 1111.91                    | 17.88     | " 13.70 | " 31.58    | " 1.61%          | " 1.23%          | " 2.84%                     | " |
| 2004       | " 1211.92                    | 19.01     | " 21.59 | " 40.60    | " 1.57%          | " 1.78%          | " 3.35%                     | " |
| 2005       | " 1248.29                    | 22.34     | " 38.82 | " 61.17    | " 1.79%          | " 3.11%          | " 4.90%                     | " |
| 2006       | " 1418.30                    | 25.04     | " 48.12 | " 73.16    | " 1.77%          | " 3.39%          | " 5.16%                     | " |
| 2007       | " 1468.36                    | 28.14     | " 67.22 | " 95.36    | " 1.92%          | " 4.58%          | " 6.49%                     | " |
| 2008       | " 903.25                     | 28.47     | " 40.25 | " 68.72    | " 3.15%          | " 4.61%          | " 7.77%                     | " |
| Normalized | " 903.25 "                   | 28.47     | " 24.11 | " 52.584   | " 3.15%          | " 2.67%          | " 5.82%                     | " |

![](_page_51_Figure_5.jpeg)

*In 2008, the actual cash returned to stockholders was 68.72. However, there was a 41% dropoff in buybacks in Q4. We reduced the total buybacks for the year by that amount.*

Analysts expect earnings to grow 4% a year for the next 5 years. We will assume that dividends & buybacks will keep pace.. Last year's cashflow (52.58) growing at 4% a year

After year 5, we will assume that earnings on the index will grow at 2.21%, the same rate as the entire economy (= riskfree rate).

## The Anatomy of a Crisis: Implied ERP from September 12, 2008 to January 1, 2009

![](_page_52_Figure_1.jpeg)

#### An Updated Equity Risk Premium: January 2012

 On January 1, 2012, the S&P 500 was at 1257.60, essentially unchanged for the year. And it was a year of macro shocks – political upheaval in the Middle East and sovereign debt problems in Europe. The treasury bond rate dropped below 2% and buybacks/dividends surged.

![](_page_53_Figure_5.jpeg)

*In the trailing 12 months, the cash returned to stockholders was 74.17. Using the average cash yield of 4.71% for 2002-2011 the cash returned would have been 59.29.*

Analysts expect earnings to grow 9.6% in 2012, 11.9% in 2013, 8.2% in 2014, 4.5% in 2015 and 2% therafter, resulting in a compounded annual growth rate of 7.18% over the next 5 years. We will assume that dividends & buybacks will grow 7.18% a year for the next 5 years.

After year 5, we will assume that earnings on the index will grow at 1.87%, the same rate as the entire economy (= riskfree rate).

> *Dividends and Buybacks last year*: S&P *Expected growth rate*: News stories, Yahoo! Finance, Bloomberg

#### Implied Premiums in the US: 1960-2011

![](_page_54_Figure_2.jpeg)

## Implied Premium versus Risk Free Rate

![](_page_55_Figure_1.jpeg)

## Equity Risk Premiums and Bond Default Spreads

![](_page_56_Figure_2.jpeg)

## Equity Risk Premiums and Cap Rates (Real Estate)

![](_page_57_Figure_1.jpeg)

#### Why implied premiums matter?

 In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. If all analysts in the department used the geometric average premium for 1928-2011 of 4.1% to value stocks in January 2012, given the implied premium of 6.04%, what were they likely to find? The values they obtain will be too low (most stocks will look overvalued) The values they obtain will be too high (most stocks will look under valued) There should be no systematic bias as long as they use the same premium to value all stocks.

## Which equity risk premium should you use for the US?

*Historical Risk Premium*: When you use the historical risk premium, you are assuming that premiums will revert back to a historical norm and that the time period that you are using is the right norm. *Current Implied Equity Risk premium*: You are assuming that the market is correct in the aggregate but makes mistakes on individual stocks. If you are required to be market neutral, this is the premium you should use. (What types of valuations require market neutrality?) *Average Implied Equity Risk premium*: The average implied equity risk premium between 1960-2011 in the United States is about 4%. You are assuming that the market is correct on average but not necessarily at a point in time.

#### Implied premium for the Sensex (September 2007)

#### Inputs for the computation

- Sensex on 9/5/07 = 15446
- Dividend yield on index = 3.05%
- Expected growth rate next 5 years = 14%
- Growth rate beyond year 5 = 6.76% (set equal to riskfree rate)

#### Solving for the expected return:

#### Expected return on stocks = 11.18%

## Implied equity risk premium for India = 11.18% - 6.76% = 4.42% €

| $15446 = \frac{537.06}{(1+r)} + \frac{612.25}{(1+r)^2} + \frac{697.86}{(1+r)^3} + \frac{795.67}{(1+r)^4} + \frac{907.07}{(1+r)^5} + \frac{907.07(1.0676)}{(r-.0676)(1+r)^5}$ |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Implied Equity Risk Premium comparison: January 2008 versus January 2009

| Country       | ERP (1/1/08) | ERP (1/1/09) |
|---------------|--------------|--------------|
| United States | 4.37%        | 6.43%        |
| UK            | 4.20%        | 6.51%        |
| Germany       | 4.22%        | 6.49%        |
| Japan         | 3.91%        | 6.25%        |
| India         | 4.88%        | 9.21%        |
| China         | 3.98%        | 7.86%        |
| Brazil        | 5.45%        | 9.06%        |

#### Estimating Beta

 The standard procedure for estimating betas is to regress stock returns (Rj) against market returns (Rm) -

$$R_j = a + b R_m$$

- where a is the intercept and b is the slope of the regression.

 The slope of the regression corresponds to the beta of the stock, and measures the riskiness of the stock.

- This beta has three problems:
  - It has high standard error
  - It reflects the firm's business mix over the period of the regression, not the current mix
  - It reflects the firm's average financial leverage over the period rather than the current leverage.

#### Beta Estimation: The Noise Problem

![](_page_63_Figure_1.jpeg)

#### Beta Estimation: The Index Effect

![](_page_64_Figure_1.jpeg)

## Solutions to the Regression Beta Problem

- Modify the regression beta by
  - changing the index used to estimate the beta
- adjusting the regression beta estimate, by bringing in information about the fundamentals of the company Estimate the beta for the firm using
  - the standard deviation in stock prices instead of a regression against an index
- accounting earnings or revenues, which are less noisy than market prices. Estimate the beta for the firm from the bottom up without employing the regression technique. This will require
  - understanding the business mix of the firm
- estimating the financial leverage of the firm Use an alternative measure of market risk not based upon a regression.

## The Index Game…

![](_page_66_Figure_1.jpeg)

#### Determinants of Betas

![](_page_67_Diagram_1.jpeg)

In a perfect world… we would estimate the beta of a firm by doing the following

![](_page_68_Diagram_1.jpeg)

#### Adjusting for operating leverage…

- Within any business, firms with lower fixed costs (as a percentage of total costs) should have lower unlevered betas. If you can compute fixed and variable costs for each firm in a sector, you can break down the unlevered beta into business and operating leverage components.
- Unlevered beta = Pure business beta \* (1 + (Fixed costs/ Variable costs)) The biggest problem with doing this is informational. It is difficult to get information on fixed and variable costs for individual firms. In practice, we tend to assume that the operating leverage of firms within a business are similar and use the same unlevered beta for every firm.

#### Adjusting for financial leverage…

*Conventional approach*: If we assume that debt carries no market risk (has a beta of zero), the beta of equity alone can be written as a function of the unlevered beta and the debt-equity ratio

$$\beta_L = \beta_u (1 + ((1-t)D/E))$$

In some versions, the tax effect is ignored and there is no (1-t) in the equation.

*Debt Adjusted Approach*: If beta carries market risk and you can estimate the beta of debt, you can estimate the levered beta as follows:

$$\beta_L = \beta_u (1 + ((1-t)D/E)) - \beta_{debt} (1-t) (D/E)$$

 While the latter is more realistic, estimating betas for debt can be difficult to do.

#### Bottom-up Betas

![](_page_71_Diagram_1.jpeg)

#### Why bottom-up betas?

- ■ The standard error in a bottom-up beta will be significantly lower than the standard error in a single regression beta. Roughly speaking, the standard error of a bottom-up beta estimate can be written as follows:

| Std error of bottom-up beta | Average Std Error across Betas<br>$\sqrt{\text{Number of firms in sample}}$ |
|-----------------------------|-----------------------------------------------------------------------------|
|                             |                                                                             |

- ■ The bottom-up beta can be adjusted to reflect changes in the firm's business mix and financial leverage. Regression betas reflect the past.
- ■ You can estimate bottom-up betas even when you do not have historical stock prices. This is the case with initial public offerings, private businesses or divisions of companies.

![](_page_73_Figure_5.jpeg)

## Bottom-up Beta: Firm in Multiple Businesses SAP in 2004

#### **Approach 1: Based on business mix**

- SAP is in three business: software, consulting and training. We will aggregate the consulting and training businesses

| Business   | Revenues | EV/Sales | Value | Weights | Beta |
|------------|----------|----------|-------|---------|------|
| Software   | \$ 5.3   | 3.25     | 17.23 | 80%     | 1.30 |
| Consulting | \$ 2.2   | 2.00     | 4.40  | 20%     | 1.05 |
| SAP        | \$ 7.5   |          | 21.63 |         | 1.25 |

#### **Approach 2: Customer Base**

## Embraer's Bottom-up Beta

| <i>Business</i> | <i>Unlevered Beta</i> | <i>D/E Ratio</i> | <i>Levered beta</i> |
|-----------------|-----------------------|------------------|---------------------|
| Aerospace       | 0.95                  | 18.95%           | 1.07                |

Levered Beta = Unlevered Beta ( 1 + (1- tax rate) (D/E Ratio) = 0.95 ( 1 + (1-.34) (.1895)) = 1.07

#### Comparable Firms?

Can an unlevered beta estimated using U.S. and European aerospace companies be used to estimate the beta for a Brazilian aerospace company?

q Yes q No

What concerns would you have in making this assumption?

#### Gross Debt versus Net Debt Approaches

 Gross Debt Ratio for Embraer = 1953/11,042 = 18.95% Levered Beta using Gross Debt ratio = 1.07 Net Debt Ratio for Embraer = (Debt - Cash)/ Market value of Equity = (1953-2320)/ 11,042 = -3.32% Levered Beta using Net Debt Ratio = 0.95 (1 + (1-.34) (-.0332)) = 0.93 The cost of Equity using net debt levered beta for Embraer will be much lower than with the gross debt approach. The cost of capital for Embraer, though, will even out since the debt ratio used in the cost of capital equation will now be a net debt ratio rather than a gross debt ratio.

#### The Cost of Equity: A Recap

![](_page_77_Diagram_1.jpeg)

## Estimating the Cost of Debt

- The cost of debt is the rate at which you can borrow at currently, It will reflect not only your default risk but also the level of interest rates in the market. The two most widely used approaches to estimating cost of debt are:
  - Looking up the yield to maturity on a straight bond outstanding from the firm. The limitation of this approach is that very few firms have long term straight bonds that are liquid and widely traded
- Looking up the rating for the firm and estimating a default spread based upon the rating. While this approach is more robust, different bonds from the same firm can have different ratings. You have to use a median rating for the firm When in trouble (either because you have no ratings or multiple ratings for a firm), estimate a synthetic rating for your firm and the cost of debt based upon that rating.

#### Estimating Synthetic Ratings

 The rating for a firm can be estimated using the financial characteristics of the firm. In its simplest form, the rating can be estimated from the interest coverage ratio

Interest Coverage Ratio = EBIT / Interest Expenses

- For Embraer's interest coverage ratio, we used the interest expenses from 2003 and the average EBIT from 2001 to 2003. (The aircraft business was badly affected by 9/11 and its aftermath. In 2002 and 2003, Embraer reported significant drops in operating income)
  - Interest Coverage Ratio = 462.1 /129.70 = 3.56

## Interest Coverage Ratios, Ratings and Default Spreads: 2003 & 2004

| If Interest Coverage Ratio is |            | Estimated Bond Rating | Default Spread(2003) | Default Spread(2004) |
|-------------------------------|------------|-----------------------|----------------------|----------------------|
| > 8.50                        | (>12.50)   | AAA                   | 0.75%                | 0.35%                |
| 6.50 - 8.50                   | (9.5-12.5) | AA                    | 1.00%                | 0.50%                |
| 5.50 - 6.50                   | (7.5-9.5)  | A+                    | 1.50%                | 0.70%                |
| 4.25 - 5.50                   | (6-7.5)    | A                     | 1.80%                | 0.85%                |
| 3.00 - 4.25                   | (4.5-6)    | A–                    | 2.00%                | 1.00%                |
| 2.50 - 3.00                   | (4-4.5)    | BBB                   | 2.25%                | 1.50%                |
| 2.25- 2.50                    | (3.5-4)    | BB+                   | 2.75%                | 2.00%                |
| 2.00 - 2.25                   | ((3-3.5)   | BB                    | 3.50%                | 2.50%                |
| 1.75 - 2.00                   | (2.5-3)    | B+                    | 4.75%                | 3.25%                |
| 1.50 - 1.75                   | (2-2.5)    | B                     | 6.50%                | 4.00%                |
| 1.25 - 1.50                   | (1.5-2)    | B –                   | 8.00%                | 6.00%                |
| 0.80 - 1.25                   | (1.25-1.5) | CCC                   | 10.00%               | 8.00%                |
| 0.65 - 0.80                   | (0.8-1.25) | CC                    | 11.50%               | 10.00%               |
| 0.20 - 0.65                   | (0.5-0.8)  | C                     | 12.70%               | 12.00%               |
| < 0.20                        | (<0.5)     | D                     | 15.00%               | 20.00%               |

The first number under interest coverage ratios is for larger market cap companies and the second in brackets is for smaller market cap companies. For Embraer , I used the interest coverage ratio table for smaller/riskier firms (the numbers in brackets) which yields a lower rating for the same interest coverage ratio.

#### Cost of Debt computations

 Companies in countries with low bond ratings and high default risk might bear the burden of country default risk, especially if they are smaller or have all of their revenues within the country. Larger companies that derive a significant portion of their revenues in global markets may be less exposed to country default risk. In other words, they may be able to borrow at a rate lower than the government. The synthetic rating for Embraer is A-. Using the 2004 default spread of 1.00%, we estimate a cost of debt of 9.29% (using a riskfree rate of 4.29% and adding in two thirds of the country default spread of 6.01%):

Cost of debt

= Riskfree rate + 2/3(Brazil country default spread) + Company default spread =4.29% + 4.00%+ 1.00% = 9.29%

#### Synthetic Ratings: Some Caveats

 The relationship between interest coverage ratios and ratings, developed using US companies, tends to travel well, as long as we are analyzing large manufacturing firms in markets with interest rates close to the US interest rate They are more problematic when looking at smaller companies in markets with higher interest rates than the US. One way to adjust for this difference is modify the interest coverage ratio table to reflect interest rate differences (For instances, if interest rates in an emerging market are twice as high as rates in the US, halve the interest coverage ratio.

## Default Spreads: The effect of the crisis of 2008.. And the aftermath

| Rating    | 1-Jan-08 | Default spread over treasury 12-Sep-08 | 12-Nov-08 | 1-Jan-09 | 1-Jan-10 | 1-Jan-11 |
|-----------|----------|----------------------------------------|-----------|----------|----------|----------|
| Aaa/AAA   | 0.99%    | 1.40%                                  | 2.15%     | 2.00%    | 0.50%    | 0.55%    |
| Aa1/AA+   | 1.15%    | 1.45%                                  | 2.30%     | 2.25%    | 0.55%    | 0.60%    |
| Aa2/AA    | 1.25%    | 1.50%                                  | 2.55%     | 2.50%    | 0.65%    | 0.65%    |
| Aa3/AA-   | 1.30%    | 1.65%                                  | 2.80%     | 2.75%    | 0.70%    | 0.75%    |
| A1/A+     | 1.35%    | 1.85%                                  | 3.25%     | 3.25%    | 0.85%    | 0.85%    |
| A2/A      | 1.42%    | 1.95%                                  | 3.50%     | 3.50%    | 0.90%    | 0.90%    |
| A3/A-     | 1.48%    | 2.15%                                  | 3.75%     | 3.75%    | 1.05%    | 1.00%    |
| Baa1/BBB+ | 1.73%    | 2.65%                                  | 4.50%     | 5.25%    | 1.65%    | 1.40%    |
| Baa2/BBB  | 2.02%    | 2.90%                                  | 5.00%     | 5.75%    | 1.80%    | 1.60%    |
| Baa3/BBB- | 2.60%    | 3.20%                                  | 5.75%     | 7.25%    | 2.25%    | 2.05%    |
| Ba1/BB+   | 3.20%    | 4.45%                                  | 7.00%     | 9.50%    | 3.50%    | 2.90%    |
| Ba2/BB    | 3.65%    | 5.15%                                  | 8.00%     | 10.50%   | 3.85%    | 3.25%    |
| Ba3/BB-   | 4.00%    | 5.30%                                  | 9.00%     | 11.00%   | 4.00%    | 3.50%    |
| B1/B+     | 4.55%    | 5.85%                                  | 9.50%     | 11.50%   | 4.25%    | 3.75%    |
| B2/B      | 5.65%    | 6.10%                                  | 10.50%    | 12.50%   | 5.25%    | 5.00%    |
| B3/B-     | 6.45%    | 9.40%                                  | 13.50%    | 15.50%   | 5.50%    | 6.00%    |
| Caa/CCC+  | 7.15%    | 9.80%                                  | 14.00%    | 16.50%   | 7.75%    | 7.75%    |
| ERP       | 4.37%    | 4.52%                                  | 6.30%     | 6.43%    | 4.36%    | 5.20%    |

#### Updated Default Spreads - January 2012

| Ra#ng       | 1	  year | 5	  year | 10	  year | 30	  year |
|-------------|-----------|-----------|------------|------------|
| Aaa/AAA     | 0.35%     | 0.70%     | 0.65%      | 0.85%      |
| Aa1/AA+     | 0.45%     | 0.75%     | 0.80%      | 1.10%      |
| Aa2/AA      | 0.50%     | 0.80%     | 0.95%      | 1.15%      |
| Aa3/AA-­‐   | 0.60%     | 0.85%     | 1.05%      | 1.20%      |
| A1/A+       | 0.65%     | 0.90%     | 1.15%      | 1.30%      |
| A2/A        | 0.80%     | 1.05%     | 1.20%      | 1.40%      |
| A3/A-­‐     | 0.95%     | 1.25%     | 1.45%      | 1.65%      |
| Baa1/BBB+   | 1.20%     | 1.70%     | 2.00%      | 2.20%      |
| Baa2/BBB    | 1.30%     | 2.05%     | 2.30%      | 2.50%      |
| Baa3/BBB-­‐ | 2.00%     | 2.80%     | 3.10%      | 3.25%      |
| Ba1/BB+     | 4.00%     | 4.00%     | 3.75%      | 3.75%      |
| Ba2/BB      | 4.50%     | 5.50%     | 4.50%      | 4.75%      |
| Ba3/BB-­‐   | 4.75%     | 5.75%     | 4.75%      | 5.25%      |
| B1/B+       | 5.75%     | 6.75%     | 5.50%      | 5.50%      |
| B2/B        | 6.25%     | 7.75%     | 6.50%      | 6.00%      |
| B3/B-­‐     | 6.50%     | 9.00%     | 6.75%      | 6.25%      |
| Caa/CCC     | 7.25%     | 9.25%     | 8.75%      | 8.25%      |
| CC          | 8.00%     | 9.50%     | 9.50%      | 9.50%      |
| C           | 9.00%     | 10.00%    | 10.50%     | 10.50%     |
| D           | 10.00%    | 12.00%    | 12.00%     | 12.00%     |

#### Subsidized Debt: What should we do?

 Assume that the Brazilian government lends money to Embraer at a subsidized interest rate (say 6% in dollar terms). In computing the cost of capital to value Embraer, should be we use the cost of debt based upon default risk or the subisidized cost of debt? The subsidized cost of debt (6%). That is what the company is paying. The fair cost of debt (9.25%). That is what the company should require its projects to cover. A number in the middle.

## Weights for the Cost of Capital Computation

In computing the cost of capital for a publicly traded firm, the general rule for computing weights for debt and equity is that you use market value weights (and not book value weights). Why?

 Because the market is usually right Because market values are easy to obtain Because book values of debt and equity are meaningless None of the above

## Estimating Cost of Capital: Embraer in 2003

#### Equity

- Cost of Equity = 4.29% + 1.07 (4%) + 0.27 (7.89%) = 10.70%
- Market Value of Equity =11,042 million BR (\$ 3,781 million)

#### Debt

- Cost of debt = 4.29% + 4.00% +1.00%= 9.29%
- Market Value of Debt = 2,083 million BR (\$713 million)

#### Cost of Capital

Cost of Capital = 10.70 % (.84) + 9.29% (1- .34) (0.16)) = 9.97%

The book value of equity at Embraer is 3,350 million BR.

The book value of debt at Embraer is 1,953 million BR; Interest expense is 222 mil BR; Average maturity of debt = 4 years

Estimated market value of debt = 222 million (PV of annuity, 4 years, 9.29%) + \$1,953 million/1.09294 = 2,083 million BR

## If you had to do it….Converting a Dollar Cost of Capital to a Nominal Real Cost of Capital

- Approach 1: Use a BR riskfree rate in all of the calculations above. For instance, if the BR riskfree rate was 12%, the cost of capital would be computed as follows:
  - Cost of Equity = 12% + 1.07(4%) + 0.27 (7.89%) = 18.41%
  - Cost of Debt = 12% + 1% = 13%
- (This assumes the riskfree rate has no country risk premium embedded in it.) Approach 2: Use the differential inflation rate to estimate the cost of capital. For instance, if the inflation rate in BR is 8% and the inflation rate in the U.S. is 2%

Cost of capital=

$$(1 + \text{Cost of Capital}_{\$}) \left[ \frac{1 + \text{Inflation}_{\text{BR}}}{1 + \text{Inflation}_{\$}} \right] = 1.0997 (1.08/1.02) - 1 = 0.1644 \text{ or } 16.44\%$$

#### Dealing with Hybrids and Preferred Stock

 When dealing with hybrids (convertible bonds, for instance), break the security down into debt and equity and allocate the amounts accordingly. Thus, if a firm has \$ 125 million in convertible debt outstanding, break the \$125 million into straight debt and conversion option components. The conversion option is equity. When dealing with preferred stock, it is better to keep it as a separate component. The cost of preferred stock is the preferred dividend yield. (As a rule of thumb, if the preferred stock is less than 5% of the outstanding market value of the firm, lumping it in with debt will make no significant impact on your valuation).

#### Decomposing a convertible bond…

- Assume that the firm that you are analyzing has \$125 million in face value of convertible debt with a stated interest rate of 4%, a 10 year maturity and a market value of \$140 million. If the firm has a bond rating of A and the interest rate on A-rated straight bond is 8%, you can break down the value of the convertible bond into straight debt and equity portions.
  - Straight debt = (4% of \$125 million) (PV of annuity, 10 years, 8%) + 125 million/ 1.0810 = \$91.45 million
  - Equity portion = \$140 million \$91.45 million = \$48.55 million

#### Recapping the Cost of Capital

![](_page_91_Diagram_1.jpeg)

---

## II. Estimating Cash Flows

### DCF Valuation

#### Steps in Cash Flow Estimation

- Estimate the current earnings of the firm
  - If looking at cash flows to equity, look at earnings after interest expenses i.e. net income
- If looking at cash flows to the firm, look at operating earnings after taxes Consider how much the firm invested to create future growth
  - If the investment is not expensed, it will be categorized as capital expenditures. To the extent that depreciation provides a cash flow, it will cover some of these expenditures.
- Increasing working capital needs are also investments for future growth If looking at cash flows to equity, consider the cash flows from net debt issues (debt issued - debt repaid)

#### Measuring Cash Flows

![](_page_94_Diagram_1.jpeg)

#### Measuring Cash Flow to the Firm

EBIT ( 1 - tax rate)

- (Capital Expenditures Depreciation)
- Change in Working Capital

= Cash flow to the firm

Where are the tax savings from interest payments in this cash flow?

#### From Reported to Actual Earnings

![](_page_96_Diagram_1.jpeg)

## I. Update Earnings

- When valuing companies, we often depend upon financial statements for inputs on earnings and assets. Annual reports are often outdated and can be updated by using-
  - Trailing 12-month data, constructed from quarterly earnings reports.
- Informal and unofficial news reports, if quarterly reports are unavailable. Updating makes the most difference for smaller and more volatile firms, as well as for firms that have undergone significant restructuring. *Time saver*: To get a trailing 12-month number, all you need is one 10K and one 10Q (example third quarter). Use the Year to date numbers from the 10Q:

Trailing 12-month Revenue = Revenues (in last 10K) - Revenues from first 3 quarters of last year + Revenues from first 3 quarters of this year.

#### II. Correcting Accounting Earnings

- Make sure that there are no financial expenses mixed in with operating expenses
  - *Financial expense:* Any commitment that is tax deductible that you have to meet no matter what your operating results: Failure to meet it leads to loss of control of the business.
- *Example: Operating Leases*: While accounting convention treats operating leases as operating expenses, they are really financial expenses and need to be reclassified as such. This has no effect on equity earnings but does change the operating earnings Make sure that there are no capital expenses mixed in with the operating expenses
  - *Capital expense:* Any expense that is expected to generate benefits over multiple periods.
  - *R & D Adjustment*: Since R&D is a capital expenditure (rather than an operating expense), the operating income has to be adjusted to reflect its treatment.

#### The Magnitude of Operating Leases

![](_page_99_Figure_1.jpeg)

## Dealing with Operating Lease Expenses

- Operating Lease Expenses are treated as operating expenses in computing operating income. In reality, operating lease expenses should be treated as financing expenses, with the following adjustments to earnings and capital: Debt Value of Operating Leases = Present value of Operating Lease Commitments at the pre-tax cost of debt When you convert operating leases into debt, you also create an asset to counter it of exactly the same value. Adjusted Operating Earnings Adjusted Operating Earnings = Operating Earnings + Operating Lease Expenses - Depreciation on Leased Asset
  - As an approximation, this works: Adjusted Operating Earnings = Operating Earnings + Pre-tax cost of Debt \* PV of Operating Leases.

#### Operating Leases at The Gap in 2003

 The Gap has conventional debt of about \$ 1.97 billion on its balance sheet and its pre-tax cost of debt is about 6%. Its operating lease payments in the 2003 were \$978 million and its commitments for the future are below:

| Year | Commitment (millions) | Present Value (at 6%) |
|------|-----------------------|-----------------------|
| 1    | \$899.00              | \$848.11              |
| 2    | \$846.00              | \$752.94              |
| 3    | \$738.00              | \$619.64              |
| 4    | \$598.00              | \$473.67              |
| 5    | \$477.00              | \$356.44              |

6&7 \$982.50 each year \$1,346.04

Debt Value of leases = \$4,396.85 (Also value of leased asset)

 Debt outstanding at The Gap = \$1,970 m + \$4,397 m = \$6,367 m Adjusted Operating Income = Stated OI + OL exp this year - Deprec' n = \$1,012 m + 978 m - 4397 m /7 = \$1,362 million (7 year life for assets) Approximate OI = \$1,012 m + \$ 4397 m (.06) = \$1,276 m

## The Collateral Effects of Treating Operating Leases as Debt

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

#### The Magnitude of R&D Expenses

![](_page_103_Figure_1.jpeg)

#### R&D Expenses: Operating or Capital Expenses

- Accounting standards require us to consider R&D as an operating expense even though it is designed to generate future growth. It is more logical to treat it as capital expenditures. To capitalize R&D,
  - Specify an amortizable life for R&D (2 10 years)
  - Collect past R&D expenses for as long as the amortizable life
  - Sum up the unamortized R&D over the period. (Thus, if the amortizable life is 5 years, the research asset can be obtained by adding up 1/5th of the R&D expense from five years ago, 2/5th of the R&D expense from four years ago...:

## Capitalizing R&D Expenses: SAP

R & D was assumed to have a 5-year life.

| Year    | R&D Expense |      | Unamortized portion | Amortization this year |
|---------|-------------|------|---------------------|------------------------|
| Current | 1020.02     | 1.00 | 1020.02             |                        |
| -1      | 993.99      | 0.80 | 795.19              | € 198.80               |
| -2      | 909.39      | 0.60 | 545.63              | € 181.88               |
| -3      | 898.25      | 0.40 | 359.30              | € 179.65               |
| -4      | 969.38      | 0.20 | 193.88              | € 193.88               |
| -5      | 744.67      | 0.00 | 0.00                | € 148.93               |

Value of research asset = € 2,914 million

Amortization of research asset in 2004 = € 903 million

Increase in Operating Income = 1020 - 903 = € 117 million

## The Effect of Capitalizing R&D at SAP

| Conventional Accounting  | R&D treated as capital expenditure   |
|--------------------------|--------------------------------------|
| - R&D                    | = 1020                               |
| EBIT                     | = 2025                               |
| EBIT (1-t)               | = 1285 m                             |
|                          | EBIT = 2142 (Increase of 117 m)      |
|                          | EBIT (1-t) = 1359 m                  |
| 3,768 million Euros is   | understated because                  |
| biggest asset is off the | books.                               |
|                          | Asset Liability                      |
|                          | R&D Asset 2914 Book Equity +2914     |
| Conventional net cap ex  | of 2 million Euros                   |
|                          | Net Cap ex = 2+ 1020 – 903 = 119 mil |
| EBIT (1-t)               | = 1285                               |
| - Net Cap Ex             | = 2                                  |
| FCFF                     | = 1283                               |
|                          | EBIT (1-t) = 1402                    |
|                          | - Net Cap Ex = 119                   |
|                          | FCFF = 1283 m                        |

#### III. One-Time and Non-recurring Charges

 Assume that you are valuing a firm that is reporting a loss of \$ 500 million, due to a one-time charge of \$ 1 billion. What is the earnings you would use in your valuation? A loss of \$ 500 million A profit of \$ 500 million

Would your answer be any different if the firm had reported one-time losses like these once every five years?

 Yes No

#### IV. Accounting Malfeasance….

- Though all firms may be governed by the same accounting standards, the fidelity that they show to these standards can vary. More aggressive firms will show higher earnings than more conservative firms. While you will not be able to catch outright fraud, you should look for warning signals in financial statements and correct for them:
  - Income from unspecified sources holdings in other businesses that are not revealed or from special purpose entities.
  - Income from asset sales or financial transactions (for a non-financial firm)
  - Sudden changes in standard expense items a big drop in S,G &A or R&D expenses as a percent of revenues, for instance.
  - Frequent accounting restatements
  - Accrual earnings that run ahead of cash earnings consistently
  - Big differences between tax income and reported income

#### V. Dealing with Negative or Abnormally Low Earnings

![](_page_109_Diagram_1.jpeg)

#### What tax rate?

 The tax rate that you should use in computing the after-tax operating income should be The effective tax rate in the financial statements (taxes paid/Taxable income) The tax rate based upon taxes paid and EBIT (taxes paid/EBIT) The marginal tax rate for the country in which the company operates The weighted average marginal tax rate across the countries in which the company operates None of the above Any of the above, as long as you compute your after-tax cost of debt using the same tax rate

## The Right Tax Rate to Use

- The choice really is between the effective and the marginal tax rate. In doing projections, it is far safer to use the marginal tax rate since the effective tax rate is really a reflection of the difference between the accounting and the tax books. By using the marginal tax rate, we tend to understate the after-tax operating income in the earlier years, but the after-tax tax operating income is more accurate in later years If you choose to use the effective tax rate, adjust the tax rate towards the marginal tax rate over time.
  - While an argument can be made for using a weighted average marginal tax rate, it is safest to use the marginal tax rate of the country

## A Tax Rate for a Money Losing Firm

 Assume that you are trying to estimate the after-tax operating income for a firm with \$ 1 billion in net operating losses carried forward. This firm is expected to have operating income of \$ 500 million each year for the next 3 years, and the marginal tax rate on income for all firms that make money is 40%. Estimate the after-tax operating income each year for the next 3 years.

|            | Year 1 | Year 2 | Year 3 |
|------------|--------|--------|--------|
| EBIT       | 500    | 500    | 500    |
| Taxes      |        |        |        |
| EBIT (1-t) |        |        |        |
| Tax rate   |        |        |        |

## Net Capital Expenditures

 Net capital expenditures represent the difference between capital expenditures and depreciation. Depreciation is a cash inflow that pays for some or a lot (or sometimes all of) the capital expenditures. In general, the net capital expenditures will be a function of how fast a firm is growing or expecting to grow. High growth firms will have much higher net capital expenditures than low growth firms. Assumptions about net capital expenditures can therefore never be made independently of assumptions about growth in the future.

## Capital expenditures should include

- Research and development expenses, once they have been recategorized as capital expenses. The adjusted net cap ex will be Adjusted Net Capital Expenditures = Net Capital Expenditures + Current year's R&D expenses - Amortization of Research Asset Acquisitions of other firms, since these are like capital expenditures. The adjusted net cap ex will be Adjusted Net Cap Ex = Net Capital Expenditures + Acquisitions of other firms - Amortization of such acquisitions Two caveats:
  - 1. Most firms do not do acquisitions every year. Hence, a normalized measure of acquisitions (looking at an average over time) should be used
  - 2. The best place to find acquisitions is in the statement of cash flows, usually categorized under other investment activities

## Cisco's Acquisitions: 1999

| Acquired                    | ! Method of Acquisition | ! Price Paid |
|-----------------------------|-------------------------|--------------|
| GeoTel                      | Pooling                 | \$1,344      |
| Fibex                       | Pooling                 | \$318        |
| Sentient                    | Pooling                 | \$103        |
| American Internent Purchase |                         | \$58         |
| Summa Four                  | Purchase                | \$129        |
| Clarity Wireless            | Purchase                | \$153        |
| Selsius Systems             | Purchase                | \$134        |
| PipeLinks                   | Purchase                | \$118        |
| Amteva Tech                 | Purchase                | \$159        |
|                             |                         | \$2,516 ""   |

## Cisco's Net Capital Expenditures in 1999

| Cap Expenditures (from statement of CF) | = \$ 584 mil  |
|-----------------------------------------|---------------|
| - Depreciation (from statement of CF)   | = \$ 486 mil  |
| Net Cap Ex (from statement of CF)       | = \$ 98 mil   |
| Adjusted Net Capital Expenditures       | = \$3,723 mil |

(Amortization was included in the depreciation number)

## Working Capital Investments

 In accounting terms, the working capital is the difference between current assets (inventory, cash and accounts receivable) and current liabilities (accounts payables, short term debt and debt due within the next year) A cleaner definition of working capital from a cash flow perspective is the difference between non-cash current assets (inventory and accounts receivable) and non-debt current liabilities (accounts payable) Any investment in this measure of working capital ties up cash. Therefore, any increases (decreases) in working capital will reduce (increase) cash flows in that period. When forecasting future growth, it is important to forecast the effects of such growth on working capital needs, and building these effects into the cash flows.

## Working Capital: General Propositions

 Changes in non-cash working capital from year to year tend to be volatile. A far better estimate of non-cash working capital needs, looking forward, can be estimated by looking at non-cash working capital as a proportion of revenues Some firms have negative non-cash working capital. Assuming that this will continue into the future will generate positive cash flows for the firm. While this is indeed feasible for a period of time, it is not forever. Thus, it is better that non-cash working capital needs be set to zero, when it is negative.

## Volatile Working Capital?

| Revenues Non-cash WC  | Amazon \$ 1,640 -\$419 | Cisco \$12,154 -\$404 | Motorol \$30,931 \$2547 |
|-----------------------|------------------------|-----------------------|-------------------------|
| % of Revenues         | -25.53%                | -3.32%                | 8.23%                   |
| Change from last year | \$ (309)               | (\$700)               | (\$829)                 |
| Average: last 3 years | -15.16%                | -3.16%                | 8.91%                   |
| Average: industry     | 8.71%                  | -2.71%                | 7.04%                   |

#### *Assumption in Valuation*

| WC as % of Revenue | 3.00% | 0.00% | 8.23% |
|--------------------|-------|-------|-------|
|                    |       |       |       |

## Dividends and Cash Flows to Equity

- In the strictest sense, the only cash flow that an investor will receive from an equity investment in a publicly traded firm is the dividend that will be paid on the stock. Actual dividends, however, are set by the managers of the firm and may be much lower than the potential dividends (that could have been paid out)
  - managers are conservative and try to smooth out dividends
- managers like to hold on to cash to meet unforeseen future contingencies and investment opportunities When actual dividends are less than potential dividends, using a model that focuses only on dividends will under state the true value of the equity in a firm.

#### Measuring Potential Dividends

- Some analysts assume that the earnings of a firm represent its potential dividends. This cannot be true for several reasons:
  - Earnings are not cash flows, since there are both non-cash revenues and expenses in the earnings calculation
  - Even if earnings were cash flows, a firm that paid its earnings out as dividends would not be investing in new assets and thus could not grow
- Valuation models, where earnings are discounted back to the present, will over estimate the value of the equity in the firm The potential dividends of a firm are the cash flows left over after the firm has made any "investments" it needs to make to create future growth and net debt repayments (debt repayments - new debt issues)
  - The common categorization of capital expenditures into discretionary and nondiscretionary loses its basis when there is future growth built into the valuation.

#### Estimating Cash Flows: FCFE

#### Cash flows to Equity for a Levered Firm

Net Income

- (Capital Expenditures - Depreciation)

- Changes in non-cash Working Capital

- (Principal Repayments - New Debt Issues)

= Free Cash flow to Equity

- I have ignored preferred dividends. If preferred stock exist, preferred dividends will also need to be netted out

## Estimating FCFE when Leverage is Stable

#### Net Income

- ## - (1- δ) (Capital Expenditures - Depreciation)
- -  $(1 - \delta)$  Working Capital Needs
  = Free Cash flow to Equity

## $$\delta = \text{Debt/Capital Ratio}$$

### For this firm,

- Proceeds from new debt issues = Principal Repayments +  $\delta$  (Capital Expenditures - Depreciation + Working Capital Needs)■ In computing FCFE, the book value debt to capital ratio should be used when looking back in time but can be replaced with the market value debt to capital ratio, looking forward.

#### Estimating FCFE: Disney

 Net Income=\$ 1533 Million Capital spending = \$ 1,746 Million Depreciation per Share = \$ 1,134 Million Increase in non-cash working capital = \$ 477 Million Debt to Capital Ratio = 23.83% Estimating FCFE (1997):

| Net Income                  | \$1,533 Mil    |                        |
|-----------------------------|----------------|------------------------|
| - (Cap. Exp - Depr)*(1-DR)  | \$465.90       | [(1746-1134)(1-.2383)] |
| Chg. Working Capital*(1-DR) | \$363.33       | [477(1-.2383)]         |
| = Free CF to Equity         | \$ 704 Million |                        |
| Dividends Paid              | \$ 345 Million |                        |

#### FCFE and Leverage: Is this a free lunch?

![](_page_125_Figure_1.jpeg)

#### FCFE and Leverage: The Other Shoe Drops

![](_page_126_Figure_1.jpeg)

## Leverage, FCFE and Value

 In a discounted cash flow model, increasing the debt/equity ratio will generally increase the expected free cash flows to equity investors over future time periods and also the cost of equity applied in discounting these cash flows. Which of the following statements relating leverage to value would you subscribe to? Increasing leverage will increase value because the cash flow effects will dominate the discount rate effects Increasing leverage will decrease value because the risk effect will be greater than the cash flow effects Increasing leverage will not affect value because the risk effect will exactly offset the cash flow effect Any of the above, depending upon what company you are looking at and where it is in terms of current leverage

## III. Estimating Growth

#### DCF Valuation

## Ways of Estimating Growth in Earnings

#### Look at the past

- The historical growth in earnings per share is usually a good starting point for growth estimation

#### Look at what others are estimating

- Analysts estimate growth in earnings per share for many firms. It is useful to know what their estimates are.

#### Look at fundamentals

- Ultimately, all growth in earnings can be traced to two fundamentals how much the firm is investing in new projects, and what returns these projects are making for the firm.

## I. Historical Growth in EPS

- Historical growth rates can be estimated in a number of different ways
  - Arithmetic versus Geometric Averages
- Simple versus Regression Models Historical growth rates can be sensitive to
- the period used in the estimation In using historical growth rates, the following factors have to be considered
  - how to deal with negative earnings
  - the effect of changing size

#### Motorola: Arithmetic versus Geometric Growth Rates

|                    | Revenues  | % Change | EBITDA   | % Change | EBIT     | % Change |
|--------------------|-----------|----------|----------|----------|----------|----------|
| 1994               | \$ 22,245 |          | \$ 4,151 |          | \$ 2,604 |          |
| 1995               | \$ 27,037 | 21.54%   | \$ 4,850 | 16.84%   | \$ 2,931 | 12.56%   |
| 1996               | \$ 27,973 | 3.46%    | \$ 4,268 | -12.00%  | \$ 1,960 | -33.13%  |
| 1997               | \$ 29,794 | 6.51%    | \$ 4,276 | 0.19%    | \$ 1,947 | -0.66%   |
| 1998               | \$ 29,398 | -1.33%   | \$ 3,019 | -29.40%  | \$ 822   | -57.78%  |
| 1999               | \$ 30,931 | 5.21%    | \$ 5,398 | 78.80%   | \$ 3,216 | 291.24%  |
| Arithmetic Average |           | 7.08%    |          | 10.89%   |          | 42.45%   |
| Geometric Average  |           | 6.82%    |          | 5.39%    |          | 4.31%    |
| Standard deviation |           | 8.61%    |          | 41.56%   |          | 141.78%  |

#### A Test

 You are trying to estimate the growth rate in earnings per share at Time Warner from 1996 to 1997. In 1996, the earnings per share was a deficit of \$0.05. In 1997, the expected earnings per share is \$ 0.25. What is the growth rate? -600% +600% +120% Cannot be estimated

#### Dealing with Negative Earnings

- When the earnings in the starting period are negative, the growth rate cannot be estimated. (0.30/-0.05 = -600%) There are three solutions:
  - Use the higher of the two numbers as the denominator (0.30/0.25 = 120%)
  - Use the absolute value of earnings in the starting period as the denominator (0.30/0.05=600%)
- Use a linear regression model and divide the coefficient by the average earnings. When earnings are negative, the growth rate is meaningless. Thus, while the growth rate can be estimated, it does not tell you much about the future.

## The Effect of Size on Growth: Callaway Golf

| Year | Net Profit | Growth Rate |
|------|------------|-------------|
| 1990 | 1.80       |             |
| 1991 | 6.40       | 255.56%     |
| 1992 | 19.30      | 201.56%     |
| 1993 | 41.20      | 113.47%     |
| 1994 | 78.00      | 89.32%      |
| 1995 | 97.70      | 25.26%      |
| 1996 | 122.30     | 25.18%      |

Geometric Average Growth Rate = 102%

#### Extrapolation and its Dangers

| Year |             | Net Profit |
|------|-------------|------------|
| 1996 | \$          | 122.30     |
| 1997 | \$          | 247.05     |
| 1998 | \$          | 499.03     |
| 1999 | \$ 1,008.05 |            |
| 2000 | \$ 2,036.25 |            |
| 2001 | \$ 4,113.23 |            |

 If net profit continues to grow at the same rate as it has in the past 6 years, the expected net income in 5 years will be \$ 4.113 billion.

#### II. Analyst Forecasts of Growth

- While the job of an analyst is to find under and over valued stocks in the sectors that they follow, a significant proportion of an analyst' s time (outside of selling) is spent forecasting earnings per share.
  - Most of this time, in turn, is spent forecasting earnings per share in the next earnings report
- While many analysts forecast expected growth in earnings per share over the next 5 years, the analysis and information (generally) that goes into this estimate is far more limited. Analyst forecasts of earnings per share and expected growth are widely disseminated by services such as Zacks and IBES, at least for U.S companies.

## How good are analysts at forecasting growth?

 Analysts forecasts of EPS tend to be closer to the actual EPS than simple time series models, but the differences tend to be small

| Study             | Time Period          | Analyst Forecast Error | Time Series Model |
|-------------------|----------------------|------------------------|-------------------|
| Collins & Hopwood | Value Line Forecasts | 31.7%                  | 34.1%             |
| Brown & Rozeff    | Value Line Forecasts | 28.4%                  | 32.2%             |
| Fried & Givoly    | Earnings Forecaster  | 16.4%                  | 19.8%             |

- The advantage that analysts have over time series models
  - tends to decrease with the forecast period (next quarter versus 5 years)
  - tends to be greater for larger firms than for smaller firms
- tends to be greater at the industry level than at the company level Forecasts of growth (and revisions thereof) tend to be highly correlated across analysts.

#### Are some analysts more equal than others?

#### A study of All-America Analysts (chosen by Institutional Investor) found that

- There is no evidence that analysts who are chosen for the All-America Analyst team were chosen because they were better forecasters of earnings. (Their median forecast error in the quarter prior to being chosen was 30%; the median forecast error of other analysts was 28%)
- However, in the calendar year following being chosen as All-America analysts, these analysts become slightly better forecasters than their less fortunate brethren. (The median forecast error for All-America analysts is 2% lower than the median forecast error for other analysts)
- Earnings revisions made by All-America analysts tend to have a much greater impact on the stock price than revisions from other analysts
- The recommendations made by the All America analysts have a greater impact on stock prices (3% on buys; 4.7% on sells). For these recommendations the price changes are sustained, and they continue to rise in the following period (2.4% for buys; 13.8% for the sells).

## The Five Deadly Sins of an Analyst

**Tunnel Vision**: Becoming so focused on the sector and valuations within the sector that you lose sight of the bigger picture. **Lemmingitis**:Strong urge felt to change recommendations & revise earnings estimates when other analysts do the same. **Stockholm Syndrome**: Refers to analysts who start identifying with the managers of the firms that they are supposed to follow. **Factophobia** (generally is coupled with delusions of being a famous story teller): Tendency to base a recommendation on a "story" coupled with a refusal to face the facts. **Dr. Jekyll/Mr.Hyde**: Analyst who thinks his primary job is to bring in investment banking business to the firm.

#### Propositions about Analyst Growth Rates

- **Proposition 1**: There if far less private information and far more public information in most analyst forecasts than is generally claimed. **Proposition 2**: The biggest source of private information for analysts remains the company itself which might explain
  - why there are more buy recommendations than sell recommendations (information bias and the need to preserve sources)
  - why there is such a high correlation across analysts forecasts and revisions
- why All-America analysts become better forecasters than other analysts after they are chosen to be part of the team. **Proposition 3**: There is value to knowing what analysts are forecasting as earnings growth for a firm. There is, however, danger when they agree too much (lemmingitis) and when they agree to little (in which case the information that they have is so noisy as to be useless).

#### III. Fundamental Growth Rates

Investment in Existing Projects \$ 1000 Current Return on Investment on Projects 12% X = Current Earnings \$120 Investment in Existing Projects \$1000 Next Period's Return on Investment 12% X Investment in New Projects \$100 Return on Investment on New Projects 12% + <sup>X</sup> <sup>=</sup> Next Period's Earnings 132 Investment in Existing Projects \$1000 Change in ROI from current to next period: 0% X Investment in New Projects \$100 Return on Investment on New Projects 12% + <sup>X</sup> Change in Earnings = \$ 12

#### Growth Rate Derivations

In the special case where ROI on existing projects remains unchanged and is equal to the ROI on new projects

Investment in New Projects Current Earnings Return on Investment Change in Earnings Current Earnings X =

Reinvestment Rate X Return on Investment = Growth Rate in Earnings 83.33% X 12% = 10%

in the more general case where ROI can change from period to period, this can be expanded as follows:

Investment in Existing Projects\*(Change in ROI) + New Projects (ROI) Investment in Existing Projects\* Current ROI Change in Earnings Current Earnings =

100 <sup>120</sup> X 12% = \$12 \$120

For instance, if the ROI increases from 12% to 13%, the expected growth rate can be written as follows:

$$\frac{\$1,000 * (.13 - .12) + 100 (13\%)}{\$ 1000 * .12} = \frac{\$23}{\$120} = 19.17\%$$

## I. Expected Long Term Growth in EPS

 When looking at growth in earnings per share, these inputs can be cast as follows: Reinvestment Rate = Retained Earnings/ Current Earnings = Retention Ratio Return on Investment = ROE = Net Income/Book Value of Equity In the special case where the current ROE is expected to remain unchanged gEPS = Retained Earningst-1/ NIt-1 \* ROE = Retention Ratio \* ROE = b \* ROE Proposition 1: The expected growth rate in earnings for a company cannot exceed its return on equity in the long term.

## Estimating Expected Growth in EPS: Wells Fargo in 2008

 Return on equity (based on 2008 earnings)= 17.56% Retention Ratio (based on 2008 earnings and dividends) = 45.37% Expected growth rate in earnings per share for Wells Fargo, if it can maintain these numbers.

Expected Growth Rate = 0.4537 (17.56%) = 7.97%

#### Regulatory Effects on Expected EPS growth

 Assume now that the banking crisis of 2008 will have an impact on the capital ratios and profitability of banks. In particular, you can expect that the book capital (equity) needed by banks to do business will increase 30%, starting now. Assuming that Wells continues with its existing businesses, estimate the expected growth rate in earnings per share for the future.

New Return on Equity =

Expected growth rate =

#### One way to pump up ROE: Use more debt

■ 
$$\text{ROE} = \text{ROC} + \text{D/E} (\text{ROC} - i (1-t))$$

where,

ROC = EBITt (1 - tax rate) / Book value of Capitalt-1

D/E = BV of Debt/ BV of Equity

i = Interest Expense on Debt / BV of Debt

t = Tax rate on ordinary income

 Note that Book value of capital = Book Value of Debt + Book value of Equity.

#### Decomposing ROE: Brahma in 1998

- Brahma (now Ambev) had an extremely high return on equity, partly because it borrowed money at a rate well below its return on capital
  - Return on Capital = 19.91%
  - Debt/Equity Ratio = 77%
  - After-tax Cost of Debt = 5.61%
- Return on Equity = ROC + D/E (ROC i(1-t)) 19.91% + 0.77 (19.91% - 5.61%) = 30.92% This seems like an easy way to deliver higher growth in earnings per share. What (if any) is the downside?

## Decomposing ROE: Titan Watches (India)

 Return on Capital = 9.54% Debt/Equity Ratio = 191% (book value terms) After-tax Cost of Debt = 10.125% Return on Equity = ROC + D/E (ROC - i(1-t)) 9.54% + 1.91 (9.54% - 10.125%) = 8.42%

## II. Expected Growth in Net Income

 The limitation of the EPS fundamental growth equation is that it focuses on per share earnings and assumes that reinvested earnings are invested in projects earning the return on equity. A more general version of expected growth in earnings can be obtained by substituting in the equity reinvestment into real investments (net capital expenditures and working capital): Equity Reinvestment Rate = (Net Capital Expenditures + Change in Working Capital) (1 - Debt Ratio)/ Net Income Expected GrowthNet Income = Equity Reinvestment Rate \* ROE

## III. Expected Growth in EBIT And Fundamentals: Stable ROC and Reinvestment Rate

When looking at growth in operating income, the definitions are

Reinvestment Rate = (Net Capital Expenditures + Change in WC)/EBIT(1-t)

Return on Investment = ROC = EBIT(1-t)/(BV of Debt + BV of Equity)

Reinvestment Rate and Return on Capital

$$\begin{aligned} g_{EBIT} &= (\text{Net Capital Expenditures} + \text{Change in WC})/\text{EBIT}(1-t) * \text{ROC} \\ &= \text{Reinvestment Rate} * \text{ROC} \end{aligned}$$

**Proposition: The net capital expenditure needs of a firm, for a given growth rate, should be inversely proportional to the quality of its investments.** 

## Estimating Growth in EBIT: Cisco versus Motorola - 1999

#### *Cisco*'*s Fundamentals*

 Reinvestment Rate = 106.81% Return on Capital =34.07% Expected Growth in EBIT =(1.0681)(.3407) = 36.39%

#### *Motorola*'*s Fundamentals*

 Reinvestment Rate = 52.99% Return on Capital = 12.18% Expected Growth in EBIT = (.5299)(.1218) = 6.45%

## IV. Operating Income Growth when Return on Capital is Changing

 When the return on capital is changing, there will be a second component to growth, positive if the return on capital is increasing and negative if the return on capital is decreasing. If ROCt is the return on capital in period t and ROCt+1 is the return on capital in period t+1, the expected growth rate in operating income will be:

$$\text{Expected Growth Rate} = \text{ROC}_{t+1} * \text{Reinvestment rate} + (\text{ROC}_{t+1} - \text{ROC}_t) / \text{ROC}_t$$

 If the change is over multiple periods, the second component should be spread out over each period.

## Motorola's Growth Rate

 Motorola's current return on capital is 12.18% and its reinvestment rate is 52.99%. We expect Motorola's return on capital to rise to 17.22% over the next 5 years (which is half way towards the industry average)

#### Expected Growth Rate

$$= \text{ROC}_{\text{New Investments}}^* \text{Reinvestment Rate}_{\text{current}} + \{1 + (\text{ROC}_{\text{In 5 years}}^- \text{ROC}_{\text{Current}}) / \text{ROC}_{\text{Current}}\}^{1.5-1}$$

= .1722\*.5299 +{ [1+(.1722-.1218)/.1218]1/5-1}

= .1629 or 16.29%

One way to think about this is to decompose Motorola's expected growth into

Growth from new investments: .1722\*5299= 9.12%

Growth from more efficiently using existing investments: 16.29%-9.12%= 7.17%

{Note that I am assuming that the new investments start making 17.22% immediately, while allowing for existing assets to improve returns gradually}

## The Value of Growth

|                                     | Firm 1        | Firm 2        | Firm 3        | Firm 4        | Firm 5        |
|-------------------------------------|---------------|---------------|---------------|---------------|---------------|
| Reinvestment Rate                   | 20.00%        | 100.00%       | 200.00%       | 20.00%        | 0.00%         |
| ROIC on new investment              | 50.00%        | 10.00%        | 5.00%         | 10.00%        | 10.00%        |
|                                     |               |               |               |               |               |
| ROIC on existing investments before | 10.00%        | 10.00%        | 10.00%        | 10.00%        | 10.00%        |
| ROIC on existing investments after  | 10.00%        | 10.00%        | 10.00%        | 10.80%        | 11.00%        |
|                                     |               |               |               |               |               |
| Expected growth rate                | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> | <b>10.00%</b> |

$$\text{Expected growth} = \text{Growth from new investments} + \text{Efficiency growth} \\ = \text{Reinv Rate} * \text{ROC} + (\text{ROC}_t - \text{ROC}_{t-1})/\text{ROC}_{t-1}$$

**Assume that your cost of capital is 10%. As an investor, rank these firms in the order of most value growth to least value growth.**

## V. Estimating Growth when Operating Income is Negative or Margins are changing

- When operating income is negative or margins are expected to change over time, we use a three step process to estimate growth:
  - Estimate growth rates in revenues over time
    - Use historical revenue growth to get estimates of revenue growth in the near future
    - Decrease the growth rate as the firm becomes larger
    - Keep track of absolute revenues to make sure that the growth is feasible
  - Estimate expected operating margins each year
    - Set a target margin that the firm will move towards
    - Adjust the current margin towards the target margin
  - Estimate the capital that needs to be invested to generate revenue growth and expected margins
    - Estimate a sales to capital ratio that you will use to generate reinvestment needs each year.

## Sirius Radio: Revenues and Revenue Growth-June 2006

| Year Current | Revenue Growth rate | Revenues \$187 | Operating Margin -419.92% | Operating Income -\$787 |
|--------------|---------------------|----------------|---------------------------|-------------------------|
| 1            | 200.00%             | \$562          | -199.96%                  | -\$1,125                |
| 2            | 100.00%             | \$1,125        | -89.98%                   | -\$1,012                |
| 3            | 80.00%              | \$2,025        | -34.99%                   | -\$708                  |
| 4            | 60.00%              | \$3,239        | -7.50%                    | -\$243                  |
| 5            | 40.00%              | \$4,535        | 6.25%                     | \$284                   |
| 6            | 25.00%              | \$5,669        | 13.13%                    | \$744                   |
| 7            | 20.00%              | \$6,803        | 16.56%                    | \$1,127                 |
| 8            | 15.00%              | \$7,823        | 18.28%                    | \$1,430                 |
| 9            | 10.00%              | \$8,605        | 19.14%                    | \$1,647                 |
| 10           | 5.00%               | \$9,035        | 19.57%                    | \$1,768                 |

Target margin based upon Clear Channel

#### Sirius: Reinvestment Needs

| Year    | Revenues | Change in revenue | Sales/Capital Ratio | Reinvestment | Capital Invested | Operating Income (Loss) | Imputed ROC |
|---------|----------|-------------------|---------------------|--------------|------------------|-------------------------|-------------|
| Current | \$187    |                   |                     |              | \$ 1,657         | -\$787                  |             |
| 1       | \$562    | \$375             | 1.50                | \$250        | \$ 1,907         | -\$1,125                | -67.87%     |
| 2       | \$1,125  | \$562             | 1.50                | \$375        | \$ 2,282         | -\$1,012                | -53.08%     |
| 3       | \$2,025  | \$900             | 1.50                | \$600        | \$ 2,882         | -\$708                  | -31.05%     |
| 4       | \$3,239  | \$1,215           | 1.50                | \$810        | \$ 3,691         | -\$243                  | -8.43%      |
| 5       | \$4,535  | \$1,296           | 1.50                | \$864        | \$ 4,555         | \$284                   | 7.68%       |
| 6       | \$5,669  | \$1,134           | 1.50                | \$756        | \$ 5,311         | \$744                   | 16.33%      |
| 7       | \$6,803  | \$1,134           | 1.50                | \$756        | \$ 6,067         | \$1,127                 | 21.21%      |
| 8       | \$7,823  | \$1,020           | 1.50                | \$680        | \$ 6,747         | \$1,430                 | 23.57%      |
| 9       | \$8,605  | \$782             | 1.50                | \$522        | \$ 7,269         | \$1,647                 | 17.56%      |
| 10      | \$9,035  | \$430             | 1.50                | \$287        | \$ 7,556         | \$1,768                 | 15.81%      |

Industry average Sales/Cap Ratio

Capital invested in year t+!= Capital invested in year t + Reinvestment in year t+1

![](_page_158_Diagram_0.jpeg)

---

## IV. Closure in Valuation

### Discounted Cashflow Valuation

#### Getting Closure in Valuation

 A publicly traded firm potentially has an infinite life. The value is therefore the present value of cash flows forever.

 Since we cannot estimate cash flows forever, we estimate cash flows for a "growth period" and then estimate a terminal value, to capture the value at the end of the period:

$$\text{Value} = \frac{t = \infty \quad \text{CF}_t}{\sum_{t=1}^t (1+r)^t}$$

$$\text{Value} = \sum_{t=1}^{t=N} \frac{\text{CF}_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^N}$$

#### Ways of Estimating Terminal Value

![](_page_161_Diagram_1.jpeg)

## Getting Terminal Value Right 1. Obey the growth cap

 When a firm's cash flows grow at a "constant" rate forever, the present value of those cash flows can be written as:

Value = Expected Cash Flow Next Period / (r - g)

where,

r = Discount rate (Cost of Equity or Cost of Capital)

g = Expected growth rate

- The stable growth rate cannot exceed the growth rate of the economy but it can be set lower.
  - If you assume that the economy is composed of high growth and stable growth firms, the growth rate of the latter will probably be lower than the growth rate of the economy.
  - The stable growth rate can be negative. The terminal value will be lower and you are assuming that your firm will disappear over time.
- If you use nominal cashflows and discount rates, the growth rate should be nominal in the currency in which the valuation is denominated. One simple proxy for the nominal growth rate of the economy is the riskfree rate.

#### Getting Terminal Value Right

## 2. Don't wait too long…

Assume that you are valuing a young, high growth firm with great potential, just after its initial public offering. How long would you set your high growth period?

 < 5 years 5 years 10 years >10 years

What high growth period would you use for a larger firm with a proven track record of delivering growth in the past?

 5 years 10 years 15 years Longer

## Some evidence on growth at small firms...

---

- ■ While analysts routinely assume very long high growth periods (with substantial excess returns during the periods), the evidence suggests that they are much too optimistic. A study of revenue growth at firms that make IPOs in the years after the IPO shows the following:

Typically, the revenue growth rate of a newly public company outpaces its industry average for only about five years.

![](_page_164_Figure_31.jpeg)

Don't forget that growth has to be earned..

#### 3. Think about what your firm will earn as returns forever..

 In the section on expected growth, we laid out the fundamental equation for growth:

Growth rate = Reinvestment Rate \* Return on invested capital + Growth rate from improved efficiency

- In stable growth, you cannot count on efficiency delivering growth (why?) and you have to reinvest to deliver the growth rate that you have forecast. Consequently, your reinvestment rate in stable growth will be a function of your stable growth rate and what you believe the firm will earn as a return on capital in perpetuity:
- Reinvestment Rate = Stable growth rate/ Stable period Return on capital A key issue in valuation is whether it okay to assume that firms can earn more than their cost of capital in perpetuity. There are some (McKinsey, for instance) who argue that the return on capital = cost of capital in stable growth…

#### There are some firms that earn excess returns..…

 While growth rates seem to fade quickly as firms become larger, well managed firms seem to do much better at sustaining excess returns for longer periods.

![](_page_166_Figure_6.jpeg)

![](_page_166_Figure_8.jpeg)

## And don't fall for sleight of hand…

 A typical assumption in many DCF valuations, when it comes to stable growth, is that capital expenditures offset depreciation and there are no working capital needs. Stable growth firms, we are told, just have to make maintenance cap ex (replacing existing assets ) to deliver growth. If you make this assumption, what expected growth rate can you use in your terminal value computation? What if the stable growth rate = inflation rate? Is it okay to make this assumption then?

## Getting Terminal Value Right 4. Be internally consistent..

- Risk and costs of equity and capital: Stable growth firms tend to
  - Have betas closer to one
  - Have debt ratios closer to industry averages (or mature company averages)
- Country risk premiums (especially in emerging markets should evolve over time) The excess returns at stable growth firms should approach (or become) zero. ROC -> Cost of capital and ROE -> Cost of equity The reinvestment needs and dividend payout ratios should reflect the lower growth and excess returns:
  - Stable period payout ratio = 1 g/ ROE
  - Stable period reinvestment rate = g/ ROC

# V. Beyond Inputs: Choosing and Using the Right Model

Discounted Cashflow Valuation

#### Summarizing the Inputs

- In summary, at this stage in the process, we should have an estimate of the
  - the current cash flows on the investment, either to equity investors (dividends or free cash flows to equity) or to the firm (cash flow to the firm)
  - the current cost of equity and/or capital on the investment
- the expected growth rate in earnings, based upon historical growth, analysts forecasts and/or fundamentals The next step in the process is deciding
  - which cash flow to discount, which should indicate
  - which discount rate needs to be estimated and
  - what pattern we will assume growth to follow

#### Which cash flow should I discount?

#### Use Equity Valuation

- (a) for firms which have stable leverage, whether high or not, and
- (b) if equity (stock) is being valued

#### Use Firm Valuation

- (a) for firms which have leverage which is too high or too low, and expect to change the leverage over time, because debt payments and issues do not have to be factored in the cash flows and the discount rate (cost of capital) does not change dramatically over time.
- (b) for firms for which you have partial information on leverage (eg: interest expenses are missing..)
- (c) in all other cases, where you are more interested in valuing the firm than the equity. (Value Consulting?)

## Given cash flows to equity, should I discount dividends or FCFE?

#### Use the Dividend Discount Model

- (a) For firms which pay dividends (and repurchase stock) which are close to the Free Cash Flow to Equity (over a extended period)
- (b)For firms where FCFE are difficult to estimate (Example: Banks and Financial Service companies)

#### Use the FCFE Model

- (a) For firms which pay dividends which are significantly higher or lower than the Free Cash Flow to Equity. (What is significant? ... As a rule of thumb, if dividends are less than 80% of FCFE or dividends are greater than 110% of FCFE over a 5 year period, use the FCFE model)
- (b) For firms where dividends are not available (Example: Private Companies, IPOs)

#### What discount rate should I use?

#### Cost of Equity versus Cost of Capital

- If discounting cash flows to equity -> Cost of Equity
- If discounting cash flows to the firm -> Cost of Capital

#### What currency should the discount rate (risk free rate) be in?

- Match the currency in which you estimate the risk free rate to the currency of your cash flows

#### Should I use real or nominal cash flows?

- If discounting real cash flows -> real cost of capital
- If nominal cash flows -> nominal cost of capital
- If inflation is low (<10%), stick with nominal cash flows since taxes are based upon nominal income
- If inflation is high (>10%) switch to real cash flows

## Which Growth Pattern Should I use?

#### If your firm is

- large and growing at a rate close to or less than growth rate of the economy*, or*
- constrained by regulation from growing at rate faster than the economy
- has the characteristics of a stable firm (average risk & reinvestment rates)

#### **Use a Stable Growth Model**

#### If your firm

- is large & growing at a moderate rate (≤ Overall growth rate + 10%) *or*
- has a single product & barriers to entry with a finite life (e.g. patents)

#### **Use a 2-Stage Growth Model**

#### If your firm

- is small and growing at a very high rate (> Overall growth rate + 10%) or
- has significant barriers to entry into the business
- has firm characteristics that are very different from the norm

#### **Use a 3-Stage or n-stage Model**

#### The Building Blocks of Valuation

| <b>Choose a</b>    |                                                                                                                                                                                                                                                                       |                                                                                                                                                                             |                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Cash Flow          | <i>Dividends</i><br>Expected Dividends to Stockholders                                                                                                                                                                                                                | <i>Cashflows to Equity</i><br>Net Income<br>- (1- δ) (Capital Exp. - Deprec'n)<br>- (1- δ) Change in Work. Capital<br>= Free Cash flow to Equity (FCFE)<br>[δ = Debt Ratio] | <i>Cashflows to Firm</i><br>EBIT (1- tax rate)<br>- (Capital Exp. - Deprec'n)<br>- Change in Work. Capital<br>= Free Cash flow to Firm (FCFF) |
|                    | <i>Cost of Equity</i><br>• <i>Basis</i> : The riskier the investment, the greater is the cost of equity.<br>• <i>Models</i> :<br>CAPM: Riskfree Rate + Beta (Risk Premium)<br>APM: Riskfree Rate + Σ Beta <sub>j</sub> (Risk Premium <sub>j</sub> ): <i>n factors</i> |                                                                                                                                                                             |                                                                                                                                               |
| & A Discount Rate  | <i>Cost of Capital</i><br>WACC = k <sub>e</sub> ( E/ (D+E))<br>+ k <sub>d</sub> ( D/(D+E))<br>k <sub>d</sub> = Current Borrowing Rate (1-t)<br>E,D: Mkt Val of Equity and Debt                                                                                        |                                                                                                                                                                             |                                                                                                                                               |
|                    | <i>Cost of Equity</i><br>• <i>Basis</i> : The riskier the investment, the greater is the cost of equity.<br>• <i>Models</i> :<br>CAPM: Riskfree Rate + Σ Beta <sub>j</sub> (Risk Premium <sub>j</sub> ): <i>n factors</i>                                             |                                                                                                                                                                             |                                                                                                                                               |
| & a growth pattern | <i>Stable Growth</i><br>g                                                                                                                                                                                                                                             | <i>Two-Stage Growth</i><br>g                                                                                                                                                | <i>Three-Stage Growth</i><br>g                                                                                                                |
|                    | t                                                                                                                                                                                                                                                                     | High Growth      Stable                                                                                                                                                     | High Growth      Transition      Stable                                                                                                       |

---

## 6. Tying up Loose Ends

#### But what comes next?

| <b>Value of Operating Assets</b>        | Since this is a discounted cashflow valuation, should there be a real option premium?                                                                                                                                       |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>+ Cash and Marketable Securities</b> | Operating versus Non-opeating cash<br>Should cash be discounted for earning a low return?                                                                                                                                   |
| <b>+ Value of Cross Holdings</b>        | How do you value cross holdings in other companies?<br>What if the cross holdings are in private businesses?                                                                                                                |
| <b>+ Value of Other Assets</b>          | What about other valuable assets?<br>How do you consider under utilized assets?                                                                                                                                             |
| <b>Value of Firm</b>                    | Should you discount this value for opacity or complexity?<br>How about a premium for synergy?<br>What about a premium for intangibles (brand name)?                                                                         |
| <b>- Value of Debt</b>                  | What should be counted in debt?<br>Should you subtract book or market value of debt?<br>What about other obligations (pension fund and health care?<br>What about contingent liabilities?<br>What about minority interests? |
| <b>= Value of Equity</b>                | Should there be a premium/discount for control?<br>Should there be a discount for distress                                                                                                                                  |
| <b>- Value of Equity Options</b>        | What equity options should be valued here (vested versus non-vested)?<br>How do you value equity options?                                                                                                                   |
| <b>= Value of Common Stock</b>          | Should you divide by primary or diluted shares?                                                                                                                                                                             |
| <b>/ Number of shares</b>               |                                                                                                                                                                                                                             |
| <b>= Value per share</b>                | Should there be a discount for illiquidity/ marketability?<br>Should there be a discount for minority interests?                                                                                                            |

## 1. The Value of Cash

 The simplest and most direct way of dealing with cash and marketable securities is to keep it out of the valuation - the cash flows should be before interest income from cash and securities, and the discount rate should not be contaminated by the inclusion of cash. (Use betas of the operating assets alone to estimate the cost of equity). Once the operating assets have been valued, you should add back the value of cash and marketable securities. In many equity valuations, the interest income from cash is included in the cashflows. The discount rate has to be adjusted then for the presence of cash. (The beta used will be weighted down by the cash holdings). Unless cash remains a fixed percentage of overall value over time, these valuations will tend to break down.

## An Exercise in Cash Valuation

| Enterprise Value Cash | Company A \$ 1 billion \$ 100 mil | Company B \$ 1 billion \$ 100 mil | Company C \$ 1 billion \$ 100 mil |
|-----------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| Return on Capital     | 10%                               | 5%                                | 22%                               |
| Cost of Capital       | 10%                               | 10%                               | 12%                               |
| Trades in             | US                                | US                                | Argentina                         |

#### Should you ever discount cash for its low returns?

- There are some analysts who argue that companies with a lot of cash on their balance sheets should be penalized by having the excess cash discounted to reflect the fact that it earns a low return.
  - Excess cash is usually defined as holding cash that is greater than what the firm needs for operations.
- A low return is defined as a return lower than what the firm earns on its non-cash investments. This is the wrong reason for discounting cash. If the cash is invested in riskless securities, it should earn a low rate of return. As long as the return is high enough, given the riskless nature of the investment, cash does not destroy value. There is a right reason, though, that may apply to some companies… Managers can do stupid things with cash (overpriced acquisitions, piein-the-sky projects….) and you have to discount for this possibility.

# Cash: Discount or Premium?

---

![](_page_181_Figure_5.jpeg)

#### The Case of Closed End Funds: Price and NAV

![](_page_182_Figure_1.jpeg)

## A Simple Explanation for the Closed End Discount

 Assume that you have a closed-end fund that invests in 'average risk" stocks. Assume also that you expect the market (average risk investments) to make 11.5% annually over the long term. If the closed end fund underperforms the market by 0.50%, estimate the discount on the fund.

## A Premium for Marketable Securities: Berkshire Hathaway

![](_page_184_Figure_1.jpeg)

#### 2. Dealing with Holdings in Other firms

- Holdings in other firms can be categorized into
  - Minority passive holdings, in which case only the dividend from the holdings is shown in the balance sheet
  - Minority active holdings, in which case the share of equity income is shown in the income statements
  - Majority active holdings, in which case the financial statements are consolidated.

#### An Exercise in Valuing Cross Holdings

 Assume that you have valued Company A using consolidated financials for \$ 1 billion (using FCFF and cost of capital) and that the firm has \$ 200 million in debt. How much is the equity in Company A worth? Now assume that you are told that Company A owns 10% of Company B and that the holdings are accounted for as passive holdings. If the market cap of company B is \$ 500 million, how much is the equity in Company A worth? Now add on the assumption that Company A owns 60% of Company C and that the holdings are fully consolidated. The minority interest in company C is recorded at \$ 40 million in Company A's balance sheet. How much is the equity in Company A worth?

#### More on Cross Holding Valuation

- Building on the previous example, assume that
  - You have valued equity in company B at \$ 250 million (which is half the market's estimate of value currently)
  - Company A is a steel company and that company C is a chemical company. Furthermore, assume that you have valued the equity in company C at \$250 million.

Estimate the value of equity in company A.

If you really want to value cross holdings right….

 Step 1: Value the parent company without any cross holdings. This will require using unconsolidated financial statements rather than consolidated ones. Step 2: Value each of the cross holdings individually. (If you use the market values of the cross holdings, you will build in errors the market makes in valuing them into your valuation. Step 3: The final value of the equity in the parent company with N cross holdings will be:

Value of un-consolidated parent company

- 
$$I \sum_{j=1}^N \% \text{ owned of Company j} * (\text{Value of Company j} - \text{Debt of Company j})$$

If you have to settle for an approximation, try this…

- For majority holdings, with full consolidation, convert the minority interest from book value to market value by applying a price to book ratio (based upon the sector average for the subsidiary) to the minority interest.
  - Estimated market value of minority interest = Minority interest on balance sheet \* Price to Book ratio for sector (of subsidiary)
- Subtract this from the estimated value of the consolidated firm to get to value of the equity in the parent company. For minority holdings in other companies, convert the book value of these holdings (which are reported on the balance sheet) into market value by multiplying by the price to book ratio of the sector(s). Add this value on to the value of the operating assets to arrive at total firm value.

#### 3. Other Assets that have not been counted yet..

- **Unutilized assets**: If you have assets or property that are not being utilized to generate cash flows (vacant land, for example), you have not valued it yet. You can assess a market value for these assets and add them on to the value of the firm. **Overfunded pension plans**: If you have a defined benefit plan and your assets exceed your expected liabilities, you could consider the over funding with two caveats:
  - Collective bargaining agreements may prevent you from laying claim to these excess assets.
  - There are tax consequences. Often, withdrawals from pension plans get taxed at much higher rates.

Do not double count an asset. If an asset is contributing to your cashflows, you cannot count the market value of the asset in your value.

## 4. A Discount for Complexity: An Experiment

| Operating Income | Company A \$ 1 billion | Company B \$ 1 billion |
|------------------|------------------------|------------------------|
| Tax rate         | 40%                    | 40%                    |
| ROIC             | 10%                    | 10%                    |
| Expected Growth  | 5%                     | 5%                     |
| Cost of capital  | 8%                     | 8%                     |
| Business Mix     | Single Business        | Multiple Businesses    |
| Holdings         | Simple                 | Complex                |
| Accounting       | Transparent            | Opaque                 |

*Which firm would you value more highly?*

## Measuring Complexity: Volume of Data in Financial Statements

| Company           | Number of pages in last 10Q | Number of pages in last 10K |
|-------------------|-----------------------------|-----------------------------|
| General Electric  | 65                          | 410                         |
| Microsoft         | 63                          | 218                         |
| Wal-mart          | 38                          | 244                         |
| Exxon Mobil       | 86                          | 332                         |
| Pfizer            | 171                         | 460                         |
| Citigroup         | 252                         | 1026                        |
| Intel             | 69                          | 215                         |
| AIG               | 164                         | 720                         |
| Johnson & Johnson | 63                          | 218                         |
| IBM               | 85                          | 353                         |

#### Measuring Complexity: A Complexity Score

| Item                 | Factors                                                                | Follow-up Question                                      | Answer                                          | Weighting factor | Answer | Heavy Score |
|----------------------|------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------|------------------|--------|-------------|
| Operating Income     | 1. Multiple Businesses                                                 | Number of businesses (with more than 10% of revenues) = | 3                                               | 2.00             | 6      |             |
|                      | 2. One-time income and expenses                                        | Percent of operating income =                           | 5%                                              | 10.00            | 0.5    |             |
|                      | 3. Income from unspecified sources                                     | Percent of operating income =                           | 15%                                             | 10.00            | 1.5    |             |
|                      | 4. Items in income statement that are volatile                         | Percent of operating income =                           | 20%                                             | 5.00             | 1      |             |
|                      | Tax Rate                                                               | 1. Income from multiple locales                         | Percent of revenues from non-domestic locales = | 75%              | 3.00   | 2.25        |
|                      |                                                                        | 2. Different tax and reporting books                    | Yes or No                                       | No               | Yes=3  | 0           |
|                      | 3. Headquarters in tax havens                                          | Yes or No                                               | No                                              | Yes=3            | 0      |             |
|                      | 4. Volatile effective tax rate                                         | Yes or No                                               | Yes                                             | Yes=2            | 2      |             |
| Capital Expenditures | 1. Volatile capital expenditures                                       | Yes or No                                               | Yes                                             | Yes=2            | 2      |             |
|                      | 2. Frequent and large acquisitions                                     | Yes or No                                               | No                                              | Yes=4            | 0      |             |
|                      | 3. Stock payment for acquisitions and investments                      | Yes or No                                               | No                                              | Yes=4            | 0      |             |
|                      | Working capital                                                        | 1. Unspecified current assets and current liabilities   | Yes or No                                       | Yes              | Yes=3  | 3           |
|                      | 2. Volatile working capital items                                      | Yes or No                                               | Yes                                             | Yes=2            | 2      |             |
| Expected Growth rate | 1. Off-balance sheet assets and liabilities (operating leases and R&D) | Yes or No                                               | No                                              | Yes=3            | 0      |             |
|                      | 2. Substantial stock buybacks                                          | Yes or No                                               | No                                              | Yes=3            | 0      |             |
|                      | 3. Changing return on capital over time                                | Is your return on capital volatile?                     | Yes                                             | Yes=5            | 5      |             |
|                      | 4. Unsustainably high return                                           | Is your firm's ROC much higher than industry average?   | Yes                                             | Yes=5            | 5      |             |
| Cost of capital      | 1. Multiple businesses                                                 | Number of businesses (more than 10% of revenues) =      | 3                                               | 1.00             | 3      |             |
|                      | 2. Operations in emerging markets                                      | Percent of revenues=                                    | 50%                                             | 5.00             | 2.5    |             |
|                      | 3. Is the debt market traded?                                          | Yes or No                                               | No                                              | No=2             | 2      |             |
|                      | 4. Does the company have a rating?                                     | Yes or No                                               | No                                              | No=2             | 2      |             |
|                      | 5. Does the company have off-balance sheet debt?                       | Yes or No                                               | No                                              | Yes=5            | 0      |             |
| No-operating assets  | Minority holdings as percent of book assets                            | Minority holdings as percent of book assets             | 30%                                             | 20.00            | 6      |             |
| Firm to Equity value | Consolidation of subsidiaries                                          | Minority interest as percent of book value of equity    | 20%                                             | 20.00            | 4      |             |
| Per share value      | Shares with different voting rights                                    | Does the firm have shares with different voting rights? | No                                              | Yes = 10         | 0      |             |
|                      | Equity options outstanding                                             | Options outstanding as percent of shares                | 0%                                              | 10.00            | 0      |             |
|                      |                                                                        | Complexity Score =                                      |                                                 |                  | 49.75  |             |

#### Dealing with Complexity

#### In Discounted Cashflow Valuation

- The Aggressive Analyst: Trust the firm to tell the truth and value the firm based upon the firm's statements about their value. The Conservative Analyst: Don't value what you cannot see. The Compromise: Adjust the value for complexity
  - Adjust cash flows for complexity
  - Adjust the discount rate for complexity
  - Adjust the expected growth rate/ length of growth period
  - Value the firm and then discount value for complexity

#### In relative valuation

In a relative valuation, you may be able to assess the price that the market is charging for complexity:

With the hundred largest market cap firms, for instance:

PBV = 0.65 + 15.31 ROE – 0.55 Beta + 3.04 Expected growth rate – 0.003 # Pages in 10K

## 5. Be circumspect about defining debt for cost of capital purposes…

- **General Rule**: Debt generally has the following characteristics:
  - Commitment to make fixed payments in the future
  - The fixed payments are tax deductible
- Failure to make the payments can lead to either default or loss of control of the firm to the party to whom payments are due. Defined as such, debt should include
  - All interest bearing liabilities, short term as well as long term
- All leases, operating as well as capital Debt should not include
  - Accounts payable or supplier credit

#### Book Value or Market Value

 You are valuing a distressed telecom company and have arrived at an estimate of \$ 1 billion for the enterprise value (using a discounted cash flow valuation). The company has \$ 1 billion in face value of debt outstanding but the debt is trading at 50% of face value (because of the distress). What is the value of the equity? The equity is worth nothing (EV minus Face Value of Debt) The equity is worth \$ 500 million (EV minus Market Value of Debt)

Would your answer be different if you were told that the liquidation value of the assets of the firm today is \$1.2 billion and that you were planning to liquidate the firm today?

## But you should consider other potential liabilities when getting to equity value

- If you have under funded pension fund or health care plans, you should consider the under funding at this stage in getting to the value of equity.
  - If you do so, you should not double count by also including a cash flow line item reflecting cash you would need to set aside to meet the unfunded obligation.
- You should not be counting these items as debt in your cost of capital calculations…. If you have contingent liabilities - for example, a potential liability from a lawsuit that has not been decided - you should consider the expected value of these contingent liabilities
  - Value of contingent liability = Probability that the liability will occur \* Expected value of liability

#### 6. Equity Options issued by the firm..

 Any options issued by a firm, whether to management or employees or to investors (convertibles and warrants) create claims on the equity of the firm. By creating claims on the equity, they can affect the value of equity per share. Failing to fully take into account this claim on the equity in valuation will result in an overstatement of the value of equity per share.

#### Why do options affect equity value per share?

- It is true that options can increase the number of shares outstanding but dilution per se is not the problem. Options affect equity value at exercise because
  - Shares are issued at below the prevailing market price. Options get exercised only when they are in the money.
- Alternatively, the company can use cashflows that would have been available to equity investors to buy back shares which are then used to meet option exercise. The lower cashflows reduce equity value. Options affect equity value before exercise because we have to build in the expectation that there is a probability and a cost to exercise.

#### A simple example…

 XYZ company has \$ 100 million in free cashflows to the firm, growing 3% a year in perpetuity and a cost of capital of 8%. It has 100 million shares outstanding and \$ 1 billion in debt. Its value can be written as follows:

Value of firm = 100 / (.08-.03) = 2000

- Debt = 1000

= Equity = 1000

Value per share = 1000/100 = \$10

#### Now come the options…

- XYZ decides to give 10 million options at the money (with a strike price of \$10) to its CEO. What effect will this have on the value of equity per share?
  - a) None. The options are not in-the-money.
  - b) Decrease by 10%, since the number of shares could increase by 10 million
  - c) Decrease by less than 10%. The options will bring in cash into the firm but they have time value.

## Dealing with Employee Options: The Bludgeon Approach

- The simplest way of dealing with options is to try to adjust the denominator for shares that will become outstanding if the options get exercised. In the example cited, this would imply the following: Value of firm = 100 / (.08-.03) = 2000
  - Debt = 1000 = Equity = 1000 Number of diluted shares = 110 Value per share = 1000/110 = \$9.09

#### Problem with the diluted approach

 The diluted approach fails to consider that exercising options will bring in cash into the firm. Consequently, they will overestimate the impact of options and understate the value of equity per share. The degree to which the approach will understate value will depend upon how high the exercise price is relative to the market price. In cases where the exercise price is a fraction of the prevailing market price, the diluted approach will give you a reasonable estimate of value per share.

#### The Treasury Stock Approach

- The treasury stock approach adds the proceeds from the exercise of options to the value of the equity before dividing by the diluted number of shares outstanding. In the example cited, this would imply the following: Value of firm = 100 / (.08-.03) = 2000
  - Debt = 1000 = Equity = 1000 Number of diluted shares = 110 Proceeds from option exercise = 10 \* 10 = 100 (Exercise price = 10) Value per share = (1000+ 100)/110 = \$ 10

#### Problems with the treasury stock approach

 The treasury stock approach fails to consider the time premium on the options. In the example used, we are assuming that an at the money option is essentially worth nothing. The treasury stock approach also has problems with out-of-the-money options. If considered, they can increase the value of equity per share. If ignored, they are treated as non-existent.

#### Dealing with options the right way…

- Step 1: Value the firm, using discounted cash flow or other valuation models. Step 2:Subtract out the value of the outstanding debt to arrive at the value of equity. Alternatively, skip step 1 and estimate the of equity directly. Step 3:Subtract out the market value (or estimated market value) of other equity claims:
  - Value of Warrants = Market Price per Warrant \* Number of Warrants : Alternatively estimate the value using option pricing model
  - Value of Conversion Option = Market Value of Convertible Bonds Value of Straight Debt Portion of Convertible Bonds
- Value of employee Options: Value using the average exercise price and maturity. Step 4:Divide the remaining value of equity by the number of shares outstanding to get value per share.

## Valuing Equity Options issued by firms… The Dilution Problem

- Option pricing models can be used to value employee options with four caveats –
  - Employee options are long term, making the assumptions about constant variance and constant dividend yields much shakier,
  - Employee options result in stock dilution, and
  - Employee options are often exercised before expiration, making it dangerous to use European option pricing models.
- Employee options cannot be exercised until the employee is vested. These problems can be partially alleviated by using an option pricing model, allowing for shifts in variance and early exercise, and factoring in the dilution effect. The resulting value can be adjusted for the probability that the employee will not be vested.

#### Back to the numbers… Inputs for Option valuation

 Stock Price = \$ 10 Strike Price = \$ 10 Maturity = 10 years Standard deviation in stock price = 40% Riskless Rate = 4%

#### Valuing the Options

 Using a dilution-adjusted Black Scholes model, we arrive at the following inputs:

- N (d1) = 0.8199
- N (d2) = 0.3624
- Value per call = \$ 9.58 (0.8199) \$10 exp-(0.04) (10)(0.3624) = \$5.42

![](_page_209_Picture_3.jpeg)

Dilution adjusted Stock price

## Value of Equity to Value of Equity per share

 Using the value per call of \$5.42, we can now estimate the value of equity per share after the option grant:

Value of firm = 100 / (.08-.03) = 2000

- Debt = 1000

= Equity = 1000

- Value of options granted = \$ 54.2

= Value of Equity in stock = \$945.8

/ Number of shares outstanding / 100

= Value per share = \$ 9.46

#### To tax adjust or not to tax adjust…

 In the example above, we have assumed that the options do not provide any tax advantages. To the extent that the exercise of the options creates tax advantages, the actual cost of the options will be lower by the tax savings. One simple adjustment is to multiply the value of the options by (1 tax rate) to get an after-tax option cost.

#### Option grants in the future…

- Assume now that this firm intends to continue granting options each year to its top management as part of compensation. These expected option grants will also affect value. The simplest mechanism for bringing in future option grants into the analysis is to do the following:
  - Estimate the value of options granted each year over the last few years as a percent of revenues.
  - Forecast out the value of option grants as a percent of revenues into future years, allowing for the fact that as revenues get larger, option grants as a percent of revenues will become smaller.
  - Consider this line item as part of operating expenses each year. This will reduce the operating margin and cashflow each year.

#### When options affect equity value per share the most…

- Option grants affect value more
  - The lower the strike price is set relative to the stock price
  - The longer the term to maturity of the option
- The more volatile the stock price The effect on value will be magnified if companies are allowed to revisit option grants and reset the exercise price if the stock price moves down.