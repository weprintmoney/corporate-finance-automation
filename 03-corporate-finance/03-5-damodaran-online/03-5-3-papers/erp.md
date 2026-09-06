---
title: "Erp"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/country/ERP.pdf
---

# Equity Risk Premiums: Looking backwards and forwards…

Aswath Damodaran

## What is the Equity Risk Premium?

- Intuitively, the equity risk premium measures what investors demand over and above the riskfree rate for investing in equities as a class. It should depend upon
  - The risk aversion of investors
  - The perceived risk of equity as an investment class

## How equity risk premiums lose their meaning…

| Model Expected Return              | Inputs     | Needed   |              |                  |
|------------------------------------|------------|----------|--------------|------------------|
| CAPM E(R) = Rf + β (Rm- Rf         |            |          |              |                  |
| )                                  | Riskfree   | Rate     |              |                  |
|                                    | Beta       | relative | to           | market portfolio |
|                                    | Market     | Risk     | Premium      |                  |
| APM E(R) = Rf + Σ j=1 β j (Rj      |            |          |              |                  |
| )                                  | Riskfree   | Rate;    | # of         | Factors;         |
|                                    | Betas      | relative | to           | each factor      |
|                                    | Factor     | risk     | premiums     |                  |
| Multi E(R) = Rf + Σ j=1,,N β j (Rj |            |          |              |                  |
| )                                  | Riskfree   | Rate;    | Macro        | factors          |
| factor                             | Betas      | relative | to           | macro factors    |
|                                    | Macro      | economic |              | risk premiums    |
| Proxy E(R) = a + Σ j=1..N bj Yj    | Proxies    |          |              |                  |
|                                    | Regression |          | coefficients |                  |

## Why equity risk premiums matter…

 Every statement about whether equity markets are over or under valued is really a statement about the prevailing equity risk premium. Every valuation of an individual stock that you do has embedded in it your implicit or explicit assumptions about the equity risk premium. To the degree that your equity risk premium is incorrect, every valuation that you do will be contaminated. All asset valuations have implicit risk premiums built into them. Getting the premium wrong will lead to misvaluations.

## What is your risk premium?

- Assume that stocks are the only risky assets and that you are offered two investment options:
  - a riskless investment (say a Government Security), on which you can make 4%
  - a mutual fund of all stocks, on which the returns are uncertain

How much of an expected return would you demand to shift your money from the riskless asset to the mutual fund?

 Less than 4% Between 4- 6% Between 6 - 8% Between 8- 10% Between 10 - 12% More than 12%

## Risk Aversion and Risk Premiums

 If this were the capital market line, the risk premium would be a weighted average of the risk premiums demanded by each and every investor. The weights will be determined by the magnitude of wealth that each investor has. Thus, Warren Bufffet's risk aversion counts more towards determining the "equilibrium" premium than yours' and mine. As investors become more risk averse, you would expect the "equilibrium" premium to increase.

# How equity risk premiums are estimated in practice…

 Survey investors on their desired risk premiums and use the average premium from these surveys. Assume that the actual premium delivered over long time periods is equal to the expected premium - i.e., use historical data Estimate the implied premium in today's asset prices.

## The Survey Approach

- Surveying all investors in a market place is impractical. However, you can survey a few investors (especially the larger investors) and use these results. In practice, this translates into surveys of money managers' expectations of expected returns on stocks over the next year. The limitations of this approach are:
  - there are no constraints on reasonability (the survey could produce negative risk premiums or risk premiums of 50%)
  - they are extremely volatile
  - they tend to be short term; even the longest surveys do not go beyond one year

## Everyone uses historical premiums, but..

- The historical premium is the premium that stocks have historically earned over riskless securities. Practitioners never seem to agree on the premium; it is sensitive to
  - How far back you go in history…
  - Whether you use T.bill rates or T.Bond rates
- Whether you use geometric or arithmetic averages. For instance, looking at the US:

| Historical Period | Stocks - T.Bills | Arithmetic average Stocks - T.Bonds | Stocks - T.Bills | Geometric Average Stocks - T.Bonds |
|-------------------|------------------|-------------------------------------|------------------|------------------------------------|
| 1928-2006         | 7.87%            | 6.57%                               | 6.01%            | 4.91%                              |
| 1966-2006         | 5.57%            | 4.13%                               | 4.34%            | 3.25%                              |
| 1996-2006         | 6.91%            | 5.14%                               | 5.42%            | 3.90%                              |

## If you choose to use historical premiums….

 Go back as far as you can. A risk premium comes with a standard error. Given the annual standard deviation in stock prices is about 25%, the standard error in a historical premium estimated over 25 years is roughly:

Standard Error in Premium = 
$$25\%/\sqrt{25} = 25\%/5 = 5\%$$

 Be consistent in your use of the riskfree rate. Since we argued for long term bond rates, the premium should be the one over T.Bonds Use the geometric risk premium. It is closer to how investors think about risk premiums over long periods.

## The perils of trusting the past…….

 Noisy estimates: Even with long time periods of history, the risk premium that you derive will have substantial standard error. For instance, if you go back to 1928 (about 78 years of history) and you assume a standard deviation of 20% in annual stock returns, you arrive at a standard error of greater than 2%:

Standard Error in Premium = 
$$20\%/\sqrt{78} = 2.26\%$$

 Survivorship Bias: Using historical data from the U.S. equtiy markets over the twentieth century does create a samplingl bias. After all, the US economy and equity markets were among the most successful of the global economies that you could have invested in early in the century.

# Risk Premium for a Mature Market? Broadening the sample

![](_page_11_Figure_1.jpeg)

# Two Ways of Estimating Country Equity Risk Premiums for other markets..

- *Default spread on Country Bond*: In this approach, the country equity risk premium is set equal to the default spread of the bond issued by the country (but only if it is denominated in a currency where a default free entity exists.
  - Brazil was rated B2 by Moody's and the default spread on the Brazilian dollar denominated C.Bond at the end of August 2004 was 6.01%. (10.30%-4.29%)

*Relative Equity Market approach*: The country equity risk premium is based upon the volatility of the market in question relative to U.S market.

Total equity risk premium = Risk Premium<sub>US</sub>\* 
$$\sigma_{\text{Country Equity}} / \sigma_{\text{US Equity}}$$

Using a 4.82% premium for the US, this approach would yield:

Total risk premium for Brazil = 4.82% (34.56%/19.01%) = 8.76%

Country equity risk premium for Brazil = 8.76% - 4.82% = 3.94%

(The standard deviation in weekly returns from 2002 to 2004 for the Bovespa was 34.56% whereas the standard deviation in the S&P 500 was 19.01%)

## And a third approach

- Country ratings measure default risk. While default risk premiums and equity risk premiums are highly correlated, one would expect equity spreads to be higher than debt spreads. Another is to multiply the bond default spread by the relative volatility of stock and bond prices in that market. Using this approach for Brazil in August 2004, you would get:
  - Country Equity risk premium = Default spread on country bond\*  $\sigma_{\text{Country}}$  Equity /  $\sigma_{\text{Country Bond}}$
  - Country Equity Risk Premium = 6.01% (34.56%/26.34%) = 7.89%

# Can country risk premiums change? Updating Brazil in January 2007

- Brazil's financial standing and country rating have improved dramatically since 2004. Its rating improved to B1. In January 2007, the interest rate on the Brazilian \$ denominated bond dropped to 6.2%. The US treasury bond rate that day was 4.7%, yielding a default spread of 1.5% for Brazil.
  - Standard Deviation in Bovespa (Equity) = 24%
  - Standard Deviation in Brazil \$-Bond = 12%
  - Default spread on C-Bond = 1.50%
  - Country Risk Premium for Brazil = 1.50% (24/12) = 3.00%

# From Country Equity Risk Premiums to Corporate Equity Risk premiums

 Approach 1: Assume that every company in the country is equally exposed to country risk. In this case,

**$$E(\text{Return}) = \text{Riskfree Rate} + \text{Country ERP} + \text{Beta (US premium)}$$**

Implicitly, this is what you are assuming when you use the local Government's dollar borrowing rate as your riskfree rate.

 Approach 2: Assume that a company's exposure to country risk is similar to its exposure to other market risk.

**$$E(\text{Return}) = \text{Riskfree Rate} + \text{Beta (US premium} + \text{Country ERP})$$**

 Approach 3: Treat country risk as a separate risk factor and allow firms to have different exposures to country risk (perhaps based upon the proportion of their revenues come from non-domestic sales)

**$$E(\text{Return})=\text{Riskfree Rate}+\beta (\text{US premium}) + \lambda (\text{Country ERP})$$**

*ERP: Equity Risk Premium*

## Implied Equity Premiums

 If we assume that stocks are correctly priced in the aggregate and we can estimate the expected cashflows from buying stocks, we can estimate the expected rate of return on stocks by computing an internal rate of return. Subtracting out the riskfree rate should yield an implied equity risk premium. This implied equity premium is a forward looking number and can be updated as often as you want (every minute of every day, if you are so inclined).

## An alternate view of ERP: Watch what I pay, not what I say..

You can back out an equity risk premium from stock prices:

January 1, 2007 S&P 500 is at 1418.3 3.75% of 1418.3 = 53.16

Between 2001 and 2006, dividends and stock buybacks averaged 3.75% of the index each year.

Analysts expect earnings (53.16) to grow 6% a year for the next 5 years .

After year 5, we will assume that earnings on the index will grow at 4.7%, the same rate as the entire economy

![](_page_17_Figure_6.jpeg)

|      | Dividends                         | Buybacks | Yield |
|------|-----------------------------------|----------|-------|
| 2001 | \$36.27                           | \$32.75  | 2.62% |
| 2002 | \$39.22                           | \$30.62  | 3.39% |
| 2003 | \$46.76                           | \$38.53  | 2.84% |
| 2004 | \$49.68                           | \$66.42  | 3.35% |
| 2005 | \$54.83                           | \$104.28 | 4.90% |
| 2006 | \$54.78                           | \$109.81 | 5.39% |
|      | Average yield between 2001-2006 = |          | 3.75% |

## Solving for the implied premium…

 If we know what investors paid for equities at the beginning of 2007 and we can estimate the expected cash flows from equities, we can solve for the rate of return that they expect to make (IRR):

 Expected Return on Stocks = 8.86% Implied Equity Risk Premium = Expected Return on Stocks - T.Bond Rate =8.86% - 4.70% = 4.16%

$$1418.3 = \frac{56.35}{(1+r)} + \frac{59.73}{(1+r)^2} + \frac{63.32}{(1+r)^3} + \frac{67.12}{(1+r)^4} + \frac{71.14}{(1+r)^5} + \frac{71.14(1.047)}{(r-.047)(1+r)^5}$$

## Implied Risk Premium Dynamics

 Assume that the index jumps 10% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease Assume that the earnings jump 10% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease Assume that the riskfree rate increases to 5% on January 2 and that nothing else changes. What will happen to the implied equity risk premium? Implied equity risk premium will increase Implied equity risk premium will decrease

#### Implied Premiums in the US

![](_page_20_Figure_1.jpeg)

#### Implied Premium versus RiskFree Rate

![](_page_21_Figure_1.jpeg)

## Equity Risk Premiums and Bond Default Spreads

![](_page_22_Figure_2.jpeg)

# Implied Premiums: From Bubble to Bear Market… January 2000 to January 2003

![](_page_23_Figure_1.jpeg)

# Effect of Changing Tax Status of Dividends on Stock Prices - January 2003

 Expected Return on Stocks (Implied) in Jan 2003 = 7.91% Dividend Yield in January 2003 = 2.00% Assuming that dividends were taxed at 30% (on average) on 1/1/03 and that capital gains were taxed at 15%. After-tax expected return on stocks = 2%(1-.3)+5.91%(1-.15) = 6.42% If the tax rate on dividends drops to 15% and the after-tax expected return remains the same:

2% (1-.15) + X% (1-.15) = 6.42%

New Pre-tax required rate of return = 7.56%

New equity risk premium = 3.75%

Value of the S&P 500 at new equity risk premium = 965.11

Expected Increase in index due to dividend tax change = 9.69%

## Why implied premiums matter?

 In many investment banks, it is common practice (especially in corporate finance departments) to use historical risk premiums (and arithmetic averages at that) as risk premiums to compute cost of equity. If all analysts in the department used the arithmetic average premium for 1928-2006 of 6.57% to value stocks in January 2007, given the implied premium of 4.16%, what are they likely to find? The values they obtain will be too low (most stocks will look overvalued) The values they obtain will be too high (most stocks will look under valued) There should be no systematic bias as long as they use the same premium (6.57%) to value all stocks.

# Myth 1: Equity Risk Premiums come from Ibbotson, D&P …

- Most practitioners use equity risk premiums provided by services (for a price), rather than estimate their own. The reasons for using a service vary but include:
  - Collecting the raw data and cleaning it up is difficult to do
  - It imposes consistency across users in the same organization
  - It gives you someone to blame if something goes wrong
- It is easier to defend in a court of law While these services all do an excellent job of collecting and processing data, they are all making estimates of the future risk premium and they are all making implicit assumptions about how risk aversion and markets will evolve.

# Myth 2: There are no costs to being too conservative with ERP

- There are many practitioners who argue that while it may be dangerous to use too low a risk premium, there is no cost to using too high a number. This may explain why so many practitioners use risk premiums of 6- 7% for the United States. If you use too high a risk premium, you will end up with too low a value. There are costs to that error:
  - If that value is used as a basis for real decisions (investments, acquisitions) firms will invest too little.
  - If the value is the basis for tax or accounting judgments, there is a loss of credibility over time from delivering numbers that are consistently too low.

# Myth 3: If you use the same ERP all the time, you are being consistent…

- Using the same equity risk premium does not have the same proportional impact on all assets. Since the value of an asset is the present value of expected future cash flows, and the effect of the equity risk premium is magnified for cash flows further out in time, assets (businesses) with significant growth potential will be affected more by using the wrong risk premium:
  - Using too high a risk premium will under value growth assets relative to mature assets.
  - Using too low a risk premium will over value growth assets relative to mature assets.

# Myth 4: Equity Risk Premiums don't change much over time…

 Practitioners often use the same equity risk premium, year in and year out, partly because of inertia and partly out of the belief that the number does not change much. Even those practitioners who use the updated historical risk premium will tend to use very similar numbers from one year to the next because they have long historical time periods to work with. Equity risk premiums are determined not only by how risk averse investors in the market are but by developments in the market changing economic conditions, terrorist attacks etc.. Consequently, you would expect the equity risk premium to change over tiime.