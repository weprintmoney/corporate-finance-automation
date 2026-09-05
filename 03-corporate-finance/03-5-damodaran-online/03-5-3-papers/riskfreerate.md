---
title: "Riskfreerate"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/papers/riskfreerate.pdf
---

# **What is the riskfree rate? A Search for the Basic Building Block**

*Aswath Damodaran*

*Stern School of Business, New York University*

*adamodar@stern.nyu.edu*

*www.damodaran.com*

December 2008

## **What is the riskfree rate? A Search for the Basic Building Block**

In corporate finance and valuation, we start off with the presumption that the riskfree rate is given and easy to obtain and focus the bulk of our attention on estimating the risk parameters of individuals firms and risk premiums. But is the riskfree rate that simple to obtain? Both academics and practitioners have long used government security rates as riskfree rates, though there have been differences on whether to use short term or longterm rates. In this paper, we not only provide a framework for deciding whether to use short or long term rates in analysis but also a roadmap for what to do when there is no government bond rate available or when there is default risk in the government bond. We look at common errors that creep into valuations as a consequence of getting the riskfree rate wrong and suggest a way in which we can preserve consistency in both valuation and capital budgeting.

Most risk and return models in finance start off with an asset that is defined as risk free, and use the expected return on that asset as the risk free rate. The expected returns on risky investments are then measured relative to the risk free rate, with the risk creating an expected risk premium that is added on to the risk free rate.

But what makes an asset risk free? And how do we estimate a riskfree rate? We will consider these questions in this paper. In the process, we have to grapple with why riskfree rates may be different in different currencies and how to adapt our estimates to reflect these differences. We will also look at cases where estimating a riskfree rate becomes difficult to do and the mechanisms that we can use to meet the challenges. We will also look at questionable practices, when it comes to riskfree rates, and the consequences for valuations.

## **What is a risk free asset?**

To understand what makes an asset risk free, let us go back to how risk is measured in investments. Investors who buy assets have returns that they expect to make over the time horizon that they will hold the asset. The actual returns that they make over this holding period may by very different from the expected returns, and this is where the risk comes in. Risk in finance is viewed in terms of the variance in actual returns around the expected return. For an investment to be risk free in this environment, then, the actual returns should always be equal to the expected return.

To illustrate, consider an investor with a 1-year time horizon buying a 1-year Treasury bill (or any other default-free one-year bond) with a 5% expected return. At the end of the 1-year holding period, the actual return that this investor would have on this investment will always be 5%, which is equal to the expected return. The return distribution for this investment is shown in Figure 1.

![](_page_3_Diagram_2.jpeg)

*Figure 1: Probability Distribution for Riskfree Investment*

This investment is risk free because there is no variance around the expected return.

There is a second way in which we can think of a riskfree investment and it is in the context of how the investment behaves, relative to other investments. A riskfree investment should have returns that are uncorrelated with risky investments in a market. Note that if we accept the first definition of a riskfree asset as an investment with a guaranteed return, this property always follows. An investment that delivers the same return, no matter what the scenario, should be uncorrelated with risky investments with returns that vary across scenarios.

# **Why do riskfree rates matter?**

The riskfree rate is the building block for estimating both the cost of equity and capital. The cost of equity is computed by adding a risk premium to the riskfree rate, with the magnitude of the premium being determined by the risk in an investment and the overall equity risk premium (for investing in the average risk investment). The cost of debt is estimated by adding a default spread to the riskfree rate, with the magnitude of the spread depending upon the credit risk in the company. Thus, using a higher riskfree rate, holding all else constant, will increase discount rates and reduce present value in a discounted cash flow valuation.

The level of the riskfree rate matters for other reasons as well. As the riskfree rate rises, and the discount rates rise with it, the breakdown of a firm's value into growth assets and assets in place will also shift. Since growth assets deliver cash flows further into the future, the value of growth assets will decrease more than the value of assets in place, as riskfree rates rise.

![](_page_4_Diagram_3.jpeg)

*Figure 2: Effects on Value - Asset Type*

If we categorize companies, based upon assets in place and growth assets, growth companies should be affected much more adversely when the riskfree rate increases than mature companies, holding all else constant.

Changes in the riskfree rate also have consequences for other valuation inputs. The risk premiums that we use for both equity (equity risk premium) and debt (default spreads) may change as riskfree rates change. In particular, a significant increase in the riskfree rate will generally result in higher risk premiums, thus increasing the effect on discount rates. Investors, who settle for a 4% risk premium, when the riskfree rate is 3%, may demand a much larger risk premium, if riskfree rates rise to 10%. Finally, the factors that cause the shift in riskfree rates – expected inflation and real economic growth – can also affect the expected cash flows for a firm.

# **Estimating a Riskfree Rate**

In this section, we will look at how best to estimate a riskfree rate in markets where a default free entity exists. We will also look at how riskfree rates in nominal terms can be different for real riskfree rates, and why riskfree rates can vary across currencies.

#### **Requirements for an investment to be riskfree**

If we define a riskfree investment as one where we know the expected return with certainty, under what conditions will the actual return on an investment always be equal to the expected return? In our view, there are two basic conditions that have to be met.

- The first is that there can be no default risk. Essentially, this rules out any security issued by a private firm, since even the largest and safest firms have some measure of default risk. The only securities that have a chance of being risk free are government securities, not because governments are better run than corporations, but because they control the printing of currency. At least in nominal terms, they should be able to fulfill their promises. Even this assumption, straightforward though it might seem, does not always hold up, especially when governments refuse to honor claims made by previous regimes and when they borrow in currencies other than their own.
- There is a second condition that riskless securities need to fulfill that is often forgotten. For an investment to have an actual return equal to its expected return, there can be no reinvestment risk. To illustrate this point, assume that you are trying to estimate the expected return over a five-year period, and that you want a risk free rate. A six-month treasury bill rate, while default free, will not be risk free, because there is the reinvestment risk of not knowing what the treasury bill rate will be in six months. Even a 5-year treasury bond is not risk free, since the coupons on the bond will be reinvested at rates that cannot be predicted today. The risk free rate for a five-year time horizon has to be the expected return on a default-free (government) five-year zero coupon bond.

In summary, an investment can be riskfree only if it is issued by an entity with no default risk, and the specific instrument used to derive the riskfree rate will vary depending upon the period over which you want the return to be guaranteed.

## **The Purist Solution**

If we accept both requirements – no default risk and no reinvestment risk –as prerequisites for an investment to be riskfree, the risk free rates will be vary with time horizon. Thus, we would use a one-year default free bond to derive the riskfree rate for a

one-year cash flow and a five-year default free bond to derive the riskfree rate for a fiveyear cash flow.

In fact, a conventional five-year bond will not yield a riskfree return over 5 years, even if it is issued by a default free entity, because the coupons every 6 months will have to be reinvested at uncertain rates. The solution is to strip the coupons from the bond and make it a zero-coupon bond. Thus, the riskfree rates for each period will be measured by using the rate on a zero-coupon default-free bond maturing in that period. In the United States, where zero coupon treasuries have been traded for several years now, this is a trivial task. Even if zero coupon bonds are not traded, we can estimate zero coupon rates for each period by using the rates on coupon bearing bonds. To do this, we start with the single period bond and set the rate on it as the zero coupon rate for that period. We then progressively can move up the maturity ladder, solving for the zero coupon rates for each subsequent period. For example, assume that coupons are annual and that you are provided with the following information on one-year and two-year coupon bonds:

Price of a 2%, 1-year coupon bond = 1000

Price of a 2.5%, 2-year coupon bond = 990

Setting up the one-year coupon bond, we can solve for the one-year rate:

Price of bond = 1000 = 
$$\frac{(\text{Principal} + \text{Coupon})}{(1 + 1 - \text{year zero rate})} = \frac{(1000 + 20)}{(1 + r_1)}$$

| Price of bond= $990= \frac{\text{Coupon}_1}{(1+r_1)} + \frac{(\text{Coupon}_2 + \text{Principal})}{(1+r_2)^2} = \frac{25}{(1.02)} + \frac{1025}{(1+r_2)^2}$ |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|

Since the bond trades at par, the one-year zero rate = coupon rate on the bond =2%.

Moving to the two-year coupon bond, we can solve for the two-year rate:

Solving for the two-year rate, we get  $r_2=3.03\%$ . We can then use the 1-year and 2-year rates, in conjunction with the 3-year bond to get the three-year rate and so on. In September 2008, we used the information available on U.S. treasuries (prices and coupons) to extract the zero-coupon rates in table 1:

*Table 1: Zero Coupon Rates – US Treasuries in September 2008*

| Maturity | Coupon rate | Price  | Yield | Zero rate |
|----------|-------------|--------|-------|-----------|
| 1        | 1.50%       | 100.00 | 1.50% | 1.5000%   |
| 2        | 1.75%       | 99.00  | 1.77% | 2.2739%   |
| 3        | 2.00%       | 98.00  | 2.04% | 2.7172%   |
| 4        | 2.25%       | 97.50  | 2.31% | 2.9411%   |

| 5  | 2.50% | 98.00 | 2.55% | 2.9543% |
|----|-------|-------|-------|---------|
| 6  | 2.75% | 99.00 | 2.78% | 2.9510% |
| 7  | 3.00% | 98.00 | 3.06% | 3.3789% |
| 8  | 3.25% | 97.00 | 3.35% | 3.7884% |
| 9  | 3.50% | 99.00 | 3.54% | 3.7174% |
| 10 | 3.75% | 98.00 | 3.83% | 4.1522% |

If we accept the proposition that the riskfree rate should be matched up to the time period of the cash flow, we would use the rates in this table as the riskfree rates by period – 1.5% for year 1, 2.27% for year 2 and so on.

From a pragmatic standpoint, refining riskfree rates to make them year-specific may not be worth the effort in mature markets for two reasons. The first is that with any well reasonably well behaved yield curve1, the effect on present value of using yearspecific risk free rates is likely to be small, since the rates do not deviate significantly across time. The second is that the rest of the parameters that we use in analysis now have to be defined relative to these riskfree rates; the equity risk premium that we use for the cost of equity in year 1 has to be defined relative to a one-year riskfree rate rather than the more conventional computation, which uses ten-year rates. This will usually result in higher equity risk premiums for the short-term risk free rates, which may nullify the eventual impact on the cost of equity. For instance, assume that the one-year rate is 2% and that the ten-year rate is 4% and that the equity risk premium, relative to the ten-year rate, is 4.5% but is 6% against a one-year rate. The cost of equity for an average risk investment will then be 8% for the one-year cash flow (2%+6%) and 8.5% for the 10 year cashflow (4%+4.5%).

When would it make sense to use year-specific riskfree rates? If the yield curve is downward sloping (short term rates are much higher than long term rates) or excessively upward sloping, with long term rates exceeding short term rates by more than 4%, there is a payoff to being year-specific. In market crises, for instance, it is not uncommon to see big differences (in either direction) between short term and long-term rates. If we decide to use year-specific rates, we should also estimate year-specific equity risk premiums and default spreads to be consistent.

<sup>1</sup> We use historical norms to define "well behaved". In the United States, for instance, yield curves over the last century have been upward sloping, with long term (10-year) treasury rates about 2% higher than short term (3-month) treasury bill rates.

#### **A Practical Compromise**

If we decide not to estimate year-specific riskfree rates, we have to come up with one riskfree rate to use on all of the cash flows. But what rate should we use? One answer exists and it has its roots in an interest-rate risk management strategy that is widely used by banks called duration matching. Put simply, banks that faced interest rate risk in their assets (generally loans made to corporate and individual borrowers) face two choices. The first is to try to match up the cash flows on each asset with a liability with equivalent cash flows, which would fully neutralize interest rate risk but would also be difficult to put into practice. The other is to match up the average duration of the assets to the average duration of the liabilities, resulting in less complete risk hedging, but with far less cost.

In valuation and capital budgeting, we could use a variation on this duration matching strategy, where we use one riskfree rate on all of the cash flows, but set the duration of the default-free security used as the risk free asset to the duration2 of the cash flows in the analysis. In capital budgeting, where we may be called upon to analyze short term as well as wrong term investments, the riskfree rate can vary, depending upon the duration of the investment being analyzed. In most business valuations, we can safely assume that the duration of the cash flows will be high, especially if we assume that cash flows continue into perpetuity. S&P used the dividend discount model to estimate the duration of equity in the S&P 500 to be about 16 years in 2004.3 Since dividends are lower than cashflows to equity, we would expect the true duration to be lower and closer to 8 or 9 years for the S&P 500. Since the duration of a 10-year coupon bond (with a coupon rate of about 4%), priced at par, is close to 8 years4, this would lead to use the 10 year treasury bond rate as the riskfree rate on all cash flows for most mature firms. The duration of equity will rise for higher growth firms and could be as high as 20-25 years for young firms with negative cash flows in the initial years. In valuing these firms, an

<sup>2</sup> In investment analysis, where we look at projects, these durations are usually between 3 and 10 years. In valuation, the durations tend to be much longer, since firms are assumed to have infinite lives. The duration in these cases is often well in excess of ten years, and increase with the expected growth potential of the firm.

<sup>3</sup> The duration of equity in the dividend discount model can be written as: Duration of equity = 1/ (Cost of equity -g) (1-δg/σr), where r is the riskfree rate.

<sup>4</sup> The duration of a 10-year, 4% coupon bond, trading at par, is 8.44 years.

argument can be made that we should be using a 30-year treasury bond rate as the riskfree rate.5

Given that the difference between the 10-year and 30-year bond rates is small6 and that it is much easier estimating equity risk premiums and default spreads against the former rather than the latter, we believe that using the 10-year bond rate as the riskfree rate on all cash flows is a good practice in valuation, at least in mature markets. In exceptional circumstances, where year-specific rates vary widely across time, we should consider using riskfree rates that vary across time.

### **The Currency Effect**

Even if we accept the proposition that the ten-year default free bond rate is the riskfree rate, the number we obtain at any point in time can vary, depending upon the currency that you use for your analysis. On October 20, 2008, for instance, the market interest rate on a ten-year US treasury bond rate was 3.9%; if we assume that the US treasury is default free, this would be the riskfree rate in US dollars. On the same date, the market interest rate on a ten-year Japanese government bond, denominated in yen, was 1.53%; if we assume that the Japanese government will fulfill its contractual obligations with certainty, this would be the riskfree rate in Japanese yen. Using the same logic, Figure 3 lists the two-year and ten-year government bond rates in various currencies, at least for governments that are rated AAA, and are thus unlikely to default.

<sup>5</sup> The duration of a 30-year, 4% coupon bond, trading at par, is close to 18 years.

<sup>6</sup> In the US market, which is the only one with a long history of both bonds, the difference between the two rates has been less than 0.5% for the last 40 years.

![](_page_10_Figure_1.jpeg)

One currency that is missing from this list is the Euro, where at least eleven different governments, that are part of the European Union, issue 10-year bonds, all denominated in Euros, but with differences in interest rates. Figure 4 summarizes the two-year and tenyear rates on October 20, 2008:

![](_page_11_Figure_1.jpeg)

Since none of these governments technically control the Euro money supply, there is some default risk in all of them. However, the market clearly sees more default risk in the Greek and Portuguese government bonds than it does in the German and French issues. To get a riskfree rate in Euros, we use the lowest of the 10-year government Euro bond rates as the riskfree rate; in October 2008, the German 10-year Euro bond rate of 3.81% would then have been the riskfree rate.7

So, the riskfree rate on October 20, 2008, would have ranged from a low of 1.53%, in Japanese Yen, to 5.95% in British pounds. This gives rise to two follow-up questions:

- 1. Why does the riskfree rate vary across currencies? Since the rates that we have specified as riskfree rates are all over the same maturity (ten years) and are default-free, the only significant factor that can cause differences is expected inflation. High inflation currencies will have higher riskfree rates than low inflation currencies. With our numbers, for instance, the market is expecting

<sup>7</sup> If you believe that there is default risk inherent even in this rate, you could subtract out a small default spread from the German rate to get to a Euro riskfree rate.

greater inflation in British pounds than it is in US dollars, and greater inflation in US dollars than it is in Japanese yen.

- 2. Which riskfree rate should we use in capital budgeting and valuation? If higher riskfree rates lead to higher discount rates, and holding all else constant, reduce present value, using a yen riskfree rate seemingly should give a company a higher value than using a US dollar riskfree rate. The fact that expected inflation is the key cause for differences in riskfree rates, though, should give us pause. If we decide to value a company in Japanese yen, because of the allure of the lower riskfree rate and lower discount rates, the cash flows will also have to be in Japanese yen. If expected inflation in the yen is lower, the expected growth rate and cash flows estimated in yen will reflect that fact. Consequently, whatever we gain by using a lower yen-based discount rates will be exactly offset by the loss of having to use yen-based cashflows.

Summarizing, the risk free rate used to come up with expected returns should be measured consistently with the cash flows are measured. Thus, if cash flows are estimated in nominal US dollar terms, the risk free rate will be the US Treasury bond rate. This will remain the case, whether the company being analyzed is a Brazilian, Indian or Russian company. While this may seem illogical, given the higher risk in these countries, the riskfree rate is not the vehicle for conveying concerns about this risk. This also implies that it is not where a project or firm is domiciled that determines the choice of a risk free rate, but the currency in which the cash flows on the project or firm are estimated. Thus, Nestle can be valued using cash flows estimated in Swiss Francs, discounted back at an expected return estimated using a Swiss long term government bond rate as the riskfree rate, or it can be valued in British pounds, with both the cash flows and the risk free rate being British pound rates.

If the difference in interest rates across two currencies does not adequately reflect the difference in expected inflation in these currencies, the values obtained using the different currencies can be different. In particular, projects and assets will be valued more highly when the currency used is the one with low interest rates relative to inflation. The risk, however, is that the interest rates will have to rise at some point to correct for this divergence, at which point the values will also converge.

#### **Real versus Nominal Risk free Rates**

Under conditions of high and unstable inflation, valuation is often done in real terms. Effectively, this means that cash flows are estimated using real growth rates and without allowing for the growth that comes from price inflation. To be consistent, the discount rates used in these cases have to be real discount rates. To get a real expected rate of return, we need to start with a real risk free rate. While government bonds may offer returns that are risk free in nominal terms, they are not risk free in real terms, since expected inflation can be volatile. The standard approach of subtracting an expected inflation rate from the nominal interest rate to arrive at a real risk free rate provides at best an estimate of the real risk free rate.

Until recently, there were few traded default-free securities that could be used to estimate real risk free rates, but the introduction of inflation-indexed treasuries has filled this void. An inflation-indexed treasury security (TIPs) does not offer a guaranteed nominal return to buyers, but instead provides a guaranteed real return. Thus, an inflation-indexed Treasury bond that offers a 3% real return, will yield approximately 7% in nominal terms if inflation is 4%, and only 5% in nominal terms, if inflation is only 2%. In figure 5, we show the rate on ten-year inflation indexed treasuries in the United States, relative to the nominal ten-year Treasury bond rate, from January 2003 to September 2008.

![](_page_14_Figure_1.jpeg)

Note that the difference between the nominal and the real treasury rate can be viewed as a market expectation of inflation.8 During this period, the average expected inflation, based on these rates, was 2.29%.

We could use the inflation-indexed treasury rate as a real riskfree rate in the United States. The only problem is that real valuations are seldom called for or done in markets like the United States, which have stable and low expected inflation. The markets where we would most need to do real valuations, unfortunately, are markets without inflation-indexed, default-free securities. The real risk free rates in these markets can be estimated by using one of two arguments:

- The first argument is that as long as capital can flow freely to those economies with the highest real returns, there can be no differences in real risk free rates across markets. Using this argument, the real risk free rate for the United States, estimated

Expected inflation rate = 
$$\frac{(1 + \text{Nominal Treasury Rate})}{(1 + \text{TIPs rate})}$$

In September 2008, for instance, when the nominal rate was 3.69% and the real rate was 1.85%, the approximate solution would have yielded 1.84% whereas the more precise answer would have been 1.81%.

<sup>8</sup> The difference between the treasury and the TIPs rate is an approximate measure of expected inflation. The more precise number is obtained as follows:

from the inflation-indexed treasury, can be used as the real risk free rate in any market.

- The second argument applies if there are frictions and constraints in capital flowing across markets. In that case, the expected real return on an economy, in the long term, should be equal to the expected real growth rate, again in the long term, of that economy, for equilibrium. Thus, the real risk free rate for a mature economy like Germany should be much lower than the real risk free rate for an economy with greater growth potential, such as Hungary.

Done consistently, the value of a company should be the same whether we discount real cash flows at a real discount rate or nominal cash flows, in any currency, at a nominal discount rate in the same currency.

## **Issues in estimating riskfree rates**

In the last section, we assumed that government bonds were for the most part default free and that the government bond rate was therefore a riskfree rate. Even in the Euro, which was the only currency where there was no entity capable of printing more currency, we assumed that the German government was close to default free and made our estimates accordingly. In this section, we will consider the tougher cases, where governments either have no long-term bonds outstanding in the local currency, or even if they do, are exposed to default risk. We will also look at the special case where we distrust the existing riskfree rate and believe it to be either too low or too high, given history and fundamentals.

## **There are no long term traded government bonds**

In the last section, we used the current market interest rate on government bonds issued by the United States, Japan and the UK as the risk free rates in the respective currencies. But what if there are no long term government bonds in a specific currency, or even if there are such bonds, they are not traded? In this section, we will examine the consequences.

#### *The Scenario*

In many countries (and their associated currencies), the biggest roadblock to finding a riskfree rate is that the government does not issue long term bonds in the local currency. So, how do they borrow? Many choose to use commercial bank loans, the World Bank or the IMF for their borrowing, thus bypassing the rigors of the market; this is true for most of the countries that comprise sub-Saharan Africa, for instance. Quite a few governments issue long term bonds, but in the currencies of more mature markets, rather than their own currencies. From 1992 to 2006, the Brazilian government issued long-term bonds denominated in US dollars rather than Brazilian Reais. In 2008, only 3 of the 12 South American countries had long-term bonds denominated in local currencies. Finally, there are governments that issue long term bonds, but then proceed to either offer special incentives to domestic investors (such as tax breaks) or use coercion to place these bonds, resulting in rates on these bonds that are not realistic.

## *Common (and dangerous) practices*

When there are no long term government bonds in the local currency that are widely traded, analysts valuing companies in that market often take the path of least resistance when estimating both cash flows and discount rates, resulting in currency mismatches in their valuations. With discount rates, analysts decide that is easier to estimate riskfree rates and risk premiums in a mature market currency; with Latin American companies, for instance, the currency of choice is the US dollar and the discount rates are estimated in US dollars. With cash flows, analysts either stick with local currency cash flows or convert those cash flows at the current exchange rate into a mature market currency; with Latin American companies again, the cash flows in the local currency are converted into US dollars using current exchange rates. If the value of the company is computed using these cash flows and discount rates, the resulting value will be fatally flawed because the expected inflation built into the cash flows will be different from the expected inflation built into discount rates. Consider, for instance, a Mexican company where the cash flows are estimated in pesos and the discount rate is estimated in the US dollars. Since the expected inflation rate in pesos is about 5% and the inflation rate built into the US dollar discount rate is only 2%, we will over value the company. Note that converting the peso cash flows into dollar cash flows, using currency exchange rates, does nothing to alleviate this problem.

### *Illustration 1: Currency mismatch effects on valuation*

Assume that you are valuing a Brazilian company and have been provided with the following estimates of cash flows in nominal Brazilian Reais (BR) for the next 3 years and beyond:

| Year   | Expected Cash flow in BR  |
|--------|---------------------------|
| 1      | 100 million BR            |
| 2      | 110 million BR            |
| 3      | 121 million BR            |
| Beyond | Grow at 6% a year forever |

Assume that the current exchange rate is 2 BR/US \$ and that the current cost of capital computed in US dollars, based upon the current Treasury bond rate of 4%, is 9%. Finally, assume that the inflation rate in US dollars is 2% and the inflation rate in BR is 6%. If we use the current exchange rate to convert the cash flows and leave the growth rate after year 3 intact, the value of the business that we arrive at will be \$1,789.55 million (3,579.10 million BR).

| Year            | Cash flow in BR | Exchange rate | Cash Flow in US \$ | Present value |
|-----------------|-----------------|---------------|--------------------|---------------|
| 1               | 100             | 0.50          | \$50.00            | \$45.87       |
| 2               | 110             | 0.50          | \$55.00            | \$46.29       |
| 3               | 121             | 0.50          | \$60.50            | \$46.72       |
| Terminal value  |                 |               | \$2,137.67         | \$1,650.67    |
| Value of firm = |                 |               |                    | \$1,789.55    |

Note that the terminal value is computed at the end of year 3:

Terminal value = 60.50 (1.06)/ (.09-.06) = \$ 2,137.67

 By using the current exchange rate to convert future BR cash flows into US dollars, we have in effect built in the 6% inflation rate in BR into the expected cash flows, while using a discount rate that reflects the 2% inflation rate in US dollars. In addition, the terminal value has been computed using a growth rate in nominal BR and a discount rate in US dollars. Not surprisingly, the mismatch in inflation rates leads us to over value the company.

#### *Possible solutions*

If the government does not issue long-term local currency bonds (or at least ones that you can trust to deliver a market interest rate), we have two solutions that preserve consistency. One is to estimate discount rates in a mature market currency (rather than the local currency) and then convert the cash flows into the mature market currency as well. The other is to try to estimate a local currency discount rate, troubles with the riskfree rate notwithstanding.

### *Mature market currency valuation:*

Since the value of a company, done right, should not be a function of what currency we choose to do the valuation in, one solution is to value the company in an alternate (mature market) currency. If getting a riskfree rate in Brazilian Reais is too difficult to do, a Brazilian company can be valued entirely in US dollars or Euros. To do this right, we have to first estimate the discount rate in US dollars. As we noted in the last section, the right riskfree rate to use will be the US treasury bond rate (and not the tenyear \$ denominated Brazilian bond rate, which has an embedded default spread in it). To be consistent, the cash flows, which will generally be in Reais, will have to be converted into US dollar cash flows. This conversion has to be made using the expected US dollar/ Reai exchange rate and not the current exchange rate. While forward or futures markets may provide estimates for the near term, the best way to estimate future exchange rates is by using purchasing power parity, based on expected inflation in the two currencies:

Expected Reais/ \$ in period 
$$t$$
 = Current Rate\*  $\frac{(1 + \text{Expected Inflation Rate}_{\text{Brazilian Reai}})'}{(1 + \text{Expected Inflation Rate}_{\text{US \$}})'}$ 

Using this expected exchange rate will ensure that the inflation built into the expected cash flows is consistent with the inflation embedded in the discount rate.

## *Illustration 2: Valuing in Mature Market Currency*

Let us revisit the valuation in illustration 2. Instead of using the current exchange rate, we will use the expected BR/\$ exchange rate, estimated using the inflations rates of 6% in BR and 2% in US dollars, to convert the cash flows into dollars:

| Year | Cash flow in BR | Exchange Rate (BR/\$) | Exchange Rate (\$/BR) | Cash fow in US \$ | Present Value |
|------|-----------------|-----------------------|-----------------------|-------------------|---------------|
| 1    | 100             | 2.0784                | 0.481132075           | \$48.11           | \$44.14       |

| 2              | 110 | 2.1599 | 0.462976148 | \$50.93  | \$42.86           |
|----------------|-----|--------|-------------|----------|-------------------|
| 3              | 121 | 2.2446 | 0.44550535  | \$53.91  | \$41.63           |
| Terminal value |     |        |             | \$785.49 | \$606.54 \$735.17 |

The higher inflation rate in BR leads to a depreciation in the currency's value over time. In addition, the terminal value is computed using the US dollar cash flow of \$53.91 million in year 3 and an expected growth rate of 2% (reflecting the inflation rate in US dollars and not in BR):

Terminal value = \$53.91 (1.02)/ (,09-.02) = \$785.49 million

The value that we derive for the firm today is \$735.17 million (1,470.35 million BR) and it reflects more consistent assumptions about inflation in the cash flows and discount rates and is much lower than the value of \$1,789.55 million that we derived in illustration 1.

## *Local Currency valuation*

The valuation can be done in the local currency, with the discount rate converted into a local currency discount rate; the expected cash flows in this case will remain in the local currency. There are three ways in which we can overcome the absence of a local currency, long term government bond rate as a starting point. In the first two, we try to estimate a local currency risk free rate, with estimates of inflation, and in the third, we convert a foreign currency discount rate, using expected inflation rates.

o The build-up option: Since the riskfree rate in any currency can be written as the sum of expected inflation in that currency and the expected real rate, we can try to estimate the two components separately. To estimate expected inflation, we can start with the current inflation rate and extrapolate from that to expected inflation in the future. For the real rate, we can use the rate on the inflation indexed US treasury bond rate, with the rationale that real rates should be the same globally. In 2005, for instance, adding the expected inflation rate of 8%, in India, to the interest rate of 2.12% on the inflation indexed US treasury would have yielded a riskfree rate of 10.12% in Indian rupees.

o The forward exchange rate: Forward and futures contracts on exchange rates provide information about interest rates in the currencies involved, since interest rate parity governs the relationship between spot and forward rates. For instance, the forward rate between the Thai Baht and the US dollar can be written as follows;

$$\text{Forward Rate}^t_{\text{Baht, $}} = \text{Spot Rate}_{\text{Baht, $}} \frac{(1 + \text{Interest Rate}_{\text{Thai Baht}})'}{(1 + \text{Interest Rate}_{\text{US dollar}})'}$$

For example, if the current spot rate is 38.10 Thai Baht per US dollar, the ten-year forward rate is 61.36 Baht per dollar, and the current ten-year US treasury bond rate is 5%, the ten-year Thai risk free rate (in nominal Baht) can be estimated as follows:

$$61.36 = 38.10 \frac{(1 + \text{Interest Rate}_{\text{Thai Baht}})^{10}}{(1.05)^{10}}$$

Solving for the Thai interest rate yields a ten-year risk free rate of 10.12%. The biggest limitation of this approach, however, is that forward rates are difficult to come by for periods beyond a year9 for many of the emerging markets, where we would be most interested in using them.

o The discount rate conversion: Since it far easier to estimate the other inputs to the discount rate computation, such as the equity risk premium and default spreads, in a mature market currency, the third option is to compute the entire discount rate in the mature market currency and to convert that discount rate (r) into the local currency at the last step.

$$r_{\text{Local currency}} = (1 + r_{\text{Foreign currency}})^* \frac{(1 + \text{Expected Inflation}_{\text{Local Currency}})}{(1 + \text{Expected Inflation}_{\text{Foreign Currency}})} - 1$$

For example, assume that the cost of capital computed for an Indonesian company in US dollars is 14% and that the expected inflation rate in Indonesian rupiah is 11% (compared to the 2% inflation rate in US dollars). The Indonesian rupiah cost of capital can be written as follows:

<sup>9</sup> In cases where only a one-year forward rate exists, an approximation for the long term rate can be obtained by first backing out the one-year local currency borrowing rate, taking the spread over the oneyear treasury bill rate, and then adding this spread on to the long term treasury bond rate. For instance, with a one-year forward rate of 39.95 on the Thai bond, we obtain a one-year Thai baht riskless rate of 9.04% (given a one-year T.Bill rate of 4%). Adding the spread of 5.04% to the ten-year treasury bond rate of 5% provides a ten-year Thai Baht rate of 10.04%.

Cost of capitalRupiah = (1.14)\* (1.11) (1.02) <sup>−</sup>1 = 0.24058 or 24.06%

Note that we are building on our earlier theme that the only difference between currencies should be expected inflation. To make this conversion, we still have to estimate the expected inflation in the local currency and the mature market currency. With all three approaches, we will end up with local currency cash flows and local currency discount rates, and a consistent value at the end.

### *Illustration 3: Valuing in the local currency*

In illustration 2, we corrected the inflation mismatch in illustration 1 by doing the entire valuation in US dollars. In this illustration, we will stay will nominal BR cash flows and convert the dollar cost of capital of 9% into a BR cost of capital, using the expected inflation rates of 2% in US dollars and 6% in BR:

$$\begin{aligned} \text{Cost of capital in BR} &= \text{Cost of capital in US $} * \frac{(1 + \text{Expected Inflation}_{\text{BR}})}{(1 + \text{Expected Inflation}_{\text{US $}})} - 1 \\ &= (1.09) * \frac{(1.06)}{(1.02)} - 1 = .1327 \text{ or } 13.27\% \end{aligned}$$

| Year           | Cash flow in BR € | PV          |
|----------------|-------------------|-------------|
| 1              | 100               | 88.28111477 |
| 2              | 110               | 85.72910747 |
| 3              | 121               | 83.25087292 |
| Terminal value | 1763.142857       | 1213.084148 |
| Value of firm  |                   | 1470.345243 |

The cash flows in nominal BR are discounted back at 13.27% to estimate the value today.

The terminal value is estimated using the nominal growth of 6% in BR and the BR cost of capital:

Terminal Value = 121 (1.06)/ (.1327-.06) = 1763.1428 million BR

Note that the value of the firm is 1,470.35 million BR. Identical to the valuation that we obtained when we valued the company in US dollars in illustration 2.

# **The government is not default free**

We have hitherto assumed that governments are default free, at least when it comes to borrowing in the local currency. That assumption, reasonable thought it may seem, can be challenged in some countries where investors build in the likelihood that of default risk into government bonds.

### *The Scenario*

Our discussion, hitherto, has been predicated on the assumption that governments do not default, at least on local currency borrowing. There are many emerging market economies where this assumption might not be viewed as reasonable. Governments in these markets are perceived as capable of defaulting even on local borrowing. The ratings agencies capture this potential by providing two sovereign ratings for most countries, one for foreign currency borrowing and the other for local currency borrowing. While the latter is usually higher than the former, for most countries, there are several countries with local currency ratings that are not Aaa (the standard from Moody's for a default free country). Table 2 lists local currency and foreign currency ratings for selected emerging markets (and appendix 1 has the complete listing):

*Table 2: Local and Foreign currency ratings for selected markets– October 2008*

| Country | Local Currency Rating | Foreign Currency Rating |
|---------|-----------------------|-------------------------|
| Brazil  | Ba1                   | Ba1                     |
| China   | A1                    | A1                      |
| India   | Baa3                  | Baa2                    |
| Russia  | Baa2                  | Baa2                    |

To the extent that we accept Moody's assessment of country risk, the long term, local currency bonds issued by each of these governments will have default risk embedded in them, with the risk being greater in the Brazilian government bond than it is in the Chinese government bond.

## *Common (and dangerous) practices*

When there are local currency long term bonds, analysts often choose to use the market interest rate on these bonds, notwithstanding the default risk embedded in them, as riskfree rates. To illustrate, the interest rate on long term, rupee denominated bonds issued by the Indian government in October 2008, which was 10.7%, would be used as the riskfree rate in computing the rupee cost of equity and capital for an Indian company. As table 2 shows, India's local currency rating of Baa3 suggests that there is default risk in the Indian rupee bond, and that some of the observed interest rate can be attributed to this risk. While it may seem reasonable that rupee discount rates should be higher to reflect the Indian government risk, the danger of building it into the riskfree rate is that the risk may end up being double counted. Analysts who use 10.7% as the riskfree rate for rupee discount rates often also use higher equity risk premiums for India; in fact, one approach to adjusting equity risk premiums in emerging markets is to add the default spread for the country to mature market equity risk premiums.

### *The Solution*

Since the problem in this case is that the local currency bond rate includes a default spread, the solution is a fairly simple one. If we can estimate how much of the current market interest rate on the bond can be attributed to default risk, we can strip this default spread from the rate to arrive at an estimate of the riskfree rate in that currency. Using the Indian rupee bond again as the illustration, we used the local currency rating for India as the measure of default risk to arrive at a default spread of 2.6%. Subtracting this from the market interest rate yields a riskfree rupee rate of 8.10%.

Riskfree rate in Indian rupees = Market interest rate on rupee bond – Default Spread<sub>India</sub>  

$$= 10.70\% - 2.60\% = 8.10\%$$

How did we go from a rating to a default spread? In table 3, we have estimated the typical default spreads for bonds in different sovereign ratings classes. One problem that we had in estimating the numbers for this table is that relatively few emerging markets have dollar or Euro denominated bonds outstanding. Consequently, there were some ratings classes where there was only one country with data and several ratings classes where there were none. To mitigate this problem, we used spreads from the CDS market, referenced in the earlier section. We were able to get default spreads for almost 40 countries, categorized by rating class, and we averaged the spreads across multiple countries in the same ratings class.10 An alternative approach to estimating default spread is to assume that sovereign ratings are comparable to corporate ratings, i.e., a Ba1 rated country bond and a Ba1 rated corporate bond have equal default risk. In this case, we can use the default spreads on corporate bonds for different ratings classes. Table 3 also

<sup>10</sup> For instance, Turkey, Indonesia and Vietnam all share a Ba3 rating, and the CDS spreads as of September 2008 were 2.95%, 3.15% and 3.65% respectively. The average spread across the three countries is 3.25%.

summarizes the typical default spreads for corporate bonds in different ratings classes in September 2008.

*Table 3: Default Spreads by Sovereign Ratings Class – September 2008*

| Rating | Sovereign Bonds/ CDS | Corporate Bonds |
|--------|----------------------|-----------------|
| Aaa    | 0.15%                | 0.50%           |
| Aa1    | 0.30%                | 0.80%           |
| Aa2    | 0.60%                | 1.10%           |
| Aa3    | 0.80%                | 1.20%           |
| A1     | 1.00%                | 1.35%           |
| A2     | 1.30%                | 1.45%           |
| A3     | 1.40%                | 1.50%           |
| Baa1   | 1.70%                | 1.70%           |
| Baa2   | 2.00%                | 2.00%           |
| Baa3   | 2.25%                | 2.60%           |
| Ba1    | 2.50%                | 3.20%           |
| Ba2    | 3.00%                | 3.50%           |
| Ba3    | 3.25%                | 4.00%           |
| B1     | 3.50%                | 4.50%           |
| B2     | 4.25%                | 5.50%           |
| B3     | 5.00%                | 6.50%           |
| Caa1   | 6.00%                | 7.00%           |
| Caa2   | 6.75%                | 9.00%           |
| Caa3   | 7.50%                | 11.00%          |

Note that the corporate bond spreads, at least in September 2008, were larger than the sovereign spreads.

## **The riskfree rate may change over time**

The default-free long-term interest rate in a currency is the riskfree rate that we use to estimate the costs of equity and capital. However, that rate will change over time, and as it does, so will the valuation. While this is always true, there may be times when the current riskfree rate may seem abnormally high or low, relative to history or fundamentals, and the change over time seems more likely to be in one direction than in the other.

#### *The Scenario*

Looking at the history of interest rates in the United States, there are two conclusions that we can draw. The first is that they are volatile and change over time, more so in some periods than others. The other is that there is evidence that interest rates in most periods stay within a 'normal' range and that deviations above or below this range are corrected over time. Figure 6 illustrates both findings by looking at the treasury bond rate from 1928 to 2007:

![](_page_25_Figure_4.jpeg)

While there have been long periods of interest rate stability, they are interspersed with periods of interest rate volatility. Thus, a long period of stable interest rates in the 1960s was followed by a decade of interest rate volatility in the 1970s. In addition, note that interest rates seem to revert back towards a range of 5-7% over time; this would correspond to a normal range of rates for the US. Note, though, that there is a degree of subjective judgment that goes into estimating this range, since it is dependent on the time period that we look at. For instance, the normal interest rate is much higher if we look at only the last 30 years (average rate = 7.40%) rather than the last 50 years (average rate = 6.70%) or the last 80 years (average rate = 5.32%).

There is less historical data on long-term interest rates outside the United States but we can safely argue that the volatility in interest rates has been far higher in emerging markets, especially in Latin America. The volatility has been driven primarily by changes in inflation expectations over time. In addition, it is far more difficult to set a normal range for rates in these markets, where interest rates have been in triple digits in some periods and single digits in others.

### *Common (and dangerous) practices*

When confronted with rates that deviate from what they regard as "normal", analysts often substitute what they feel is a more normal rate when valuing companies. If the Treasury bond rate is 3.5%, an analyst may decide to use 5% as the normal riskfree rate in a valuation. Though this may seem logical, there are three potential problems. The first is that "normal" is in the eyes of the beholder, with different analysts making different judgments on what comprises that number. To provide a simple contrast, analysts who started working in the late 1980s in the United States, use higher normal rates than analysts who joined in 2002 or 2003, reflecting their different experiences. The second is that using a normal riskfree rate, rather than the current interest rate, will have valuation consequences. For instance, using a 5% riskfree rate, when valuing a company, will lower the value that you attach to the company and perhaps make it over valued. However, it is unclear whether that conclusion is a result of the analyst's view on interest rates (i.e., that they are too low) or on the company. Finally, interest rates generally change over time because of changes in the underlying fundamentals. Using a normal riskfree rate, which is different from today's rate, without also adjusting the fundamentals that caused the current rate will result in inconsistent valuation. For example, assume that the riskfree rate is low currently, because inflation has been unusually low and the economy is moribund. If riskfree rates bounce back to normal levels, it will be either because inflation reverts back to historical norms or the economy strengthens. Analysts who use normal interest rates will then have to also use higher inflation and/or real growth numbers when valuing companies.

In relative valuation, the effect of changing riskfree rates is more subtle. While the level of riskfree rates is usually not an explicit factor when comparing PE ratios or

EV/EBITDA multiples across companies, changes in riskfree rates can affect companies differently. Holding all else constant, for instance, an increase in the riskfree rate should affect growth companies much more negatively than mature companies; the value of growth lies entirely in cash flows in the future, whereas cash flows from existing assets are more near term. A careless analyst will tend to find growth companies to be undervalued in high interest rate scenarios and mature companies to be bargains in low interest rate scenarios.

### *Illustration 4: Interest Rate views and Valuation*

You are valuing Dow Chemical as a stable growth firm, in September 2008, and make the following assumptions:

- a. You expect the operating income next year, after taxes, to be \$3 billion. This income is expected to grow 3% a year in perpetuity.
- b. Dow Chemical generated a return on capital of 15% in 2007, and you expect it to maintain this return on capital forever.
- c. The treasury bond rate is 4% and the cost of capital based on this riskfree rate is 8%.

You believe that the treasury bond rate is too low and that it will revert back to its normalized level, which you estimate to be 5%. The cost of capital based on this normalized riskfree rate is 9%.

If you value Dow Chemical, using the cost of capital of 9%, your estimate of value for the firm is as follows:

After-tax Operating income next year = \$3 billion

Reinvestment Rate = Expected growth rate/ Return on capital = 3/15 = 20%

Expected FCFF next year = EBIT (1-t) (1-Reinvestment Rate)

= 3000 (1-.2) = \$2,400 million

Value of firm = Expected FCFF next year/ (Cost of capital –g)

= 2400/(.09-.03) = \$ 40,000 million

Since the market value of the firm was \$ 44 billion at the time of the analysis, you would have concluded that the firm was overvalued. However, one reason for your lower value was your use of the normalized riskfree rate of 5%, instead of the actual rate of 4%. If the firm had been valued using the actual cost of capital of 8%:

Value of firm = Expected FCFF next year/ (Cost of capital - g)  

$$= 2400/(.08 - .03) = \$ 48,000 \text{ million}$$

At its current market value, the firm would have been undervalued. In effect, your initial conclusion that about Dow Chemical being over valued reflected both your assumptions about the company and your views on interest rates, with the latter being the main reason for your final conclusion. In effect, your views on interest rates reduced the value of the firm by \$ 8 billion (from \$48 billion to \$ 40 billion).

### *Solutions*

As a general rule, it is not a good idea to bring in our idiosyncratic views on interest rates, no matter how well thought on and reasoned they may be, into individual company valuations. Does this mean we are stuck using the current riskfree rate when valuing companies today? Not necessarily. We can still draw on market expectations of interest rates in valuing companies. For instance, assume that the current ten-year treasury bond rate is 3.5%. That will be the riskfree rate for the next 10 years. However, we can use futures or forward markets on treasury bonds to get a sense of what the market sees as the expected interest rate ten years from now, and use that as the riskfree rate in the future (perhaps in computing terminal value). Our views on market interest rates can be offered separately, because they do have consequences for the overall value of equities and asset allocation decisions. In effect, we let the users of our research make a judgment on what aspect of the research they trust more. If they trust our macro views but not the micro views, they will attach more weight to the interest rate and asset allocation views that we present. If, on the other hand, they feel more confident in our company analyses than in our interest rate views, they will focus on the corporate valuation and recommendation.

# **Closing Thoughts on Riskfree Rates**

Looking at the bigger picture, we can break down the estimation of a riskfree rate into steps, starting with a choice of currency and working down to include views on future rate levels. The steps are captured in figure 7:

*Figure 7: A Framework for estimating Riskfree Rates*

![](_page_29_Diagram_2.jpeg)

Summarizing the key points that we have made over the paper, we would list the following as the key rules to follow when it comes to riskfree rates.

Rule 1: *A riskfree rate should be truly free of risk*. A rate that has risk spreads embedded in it for default or other factors, is not a riskfree rate. This is why we argued that local currency government bond rates in many emerging markets cannot be used as riskfree rates.

Rule 2: *Choose a riskfree rate that is consistent with how cash flows are defined*. Thus, if the cash flows are real, the riskfree rate should also be real. If the cash flows are in a specific currency, the riskfree rate has to be defined in that currency. In other words, once you choose a currency, the riskfree rate should be for that currency and should not be a function of where a company is incorporated or the investor for whom the valuation is done. When valuing a Russian company in Euros, the riskfree rate should be the Euro riskfree rate (the German 10-year bond rate).

Rule 3: *If you have strong views on interest rates, try to keep them out of the valuation of individual companies*. In other words, even if you believe that riskfree rates will rise or fall over time, it is dangerous to reflect those views in your valuation. If you do so, your final valuation will be a joint result of your views on interest rates and your views on the company, with no easy way of deciphering the results of each effect.

## **Conclusion**

The risk free rate is the starting point for all expected return models. For an investment to be risk free, it has to meet two conditions. The first is that there can be no risk of default associated with its cash flows. The second is that there can be no reinvestment risk in the investment. Using these criteria, the appropriate risk free rate to use to obtain expected returns should be a default-free (government) zero coupon rate that is matched up to when the cash flow or flows that are being discounted occur. In practice, however, it is usually appropriate to match up the duration of the risk free asset to the duration of the cash flows being analyzed. In corporate finance and valuation, this will lead us towards long-term government bond rates as risk free rates.

In this paper, we considered three problem scenarios. The first is when there are no longterm, traded government bonds in a specific currency. We suggested either doing the valuation in a different currency or estimating the riskfree rate from forward markets or fundamentals. The second is when the long-term government bond rate has potential default risk embedded in it, in which case we argued that the riskfree rate in that currency has to be net of the default spread. The third is when the current long term riskfree rate seems too low or high, relative to historic norms. Without passing judgments on the efficacy of this view, we noted that it is better to separate our views about interest rates from our assessment of companies.

### *Appendix 1: Sovereign Ratings by Country (Moody's)*

| Country              | <i>Foreign</i> | <i>Local</i>   | Country          | <i>Foreign</i> | <i>Local</i> | Country                 | <i>Foreign</i> | <i>Local</i> |
|----------------------|----------------|----------------|------------------|----------------|--------------|-------------------------|----------------|--------------|
| Albania              | B1             | B1             | Guatemala        | Ba2            | Ba1          | Peru                    | Ba2            | Ba2          |
| Alderney             | Aaa            | Aaa            | Guernsey         | Aaa            | Aaa          | Philippines             | B1             | B1           |
| Argentina            | Aaa            | Aaa            | Hongary          | B2             | B2           | Portugal                | A2             | A2           |
| Argentina            | B3             | B3             | Hong Kong        | Aa2            | Aa2          | Portugal                | A2             | Aa2          |
| Armenia              | Ba2            | Ba2            | Hungary          | A2             | A2           | Qatar                   | Aa2            | Aa2          |
| Australia            | Aaa            | Aaa            | Iceland          | Aaa            | Aaa          | Romania                 | Baa3           | Baa3         |
| Austria              | Aaa            | Aaa            | India            | Baa3           | Ba2          | Russia                  | Baa2           | Baa2         |
| Azerbaijan           | Ba1            | Ba1            | Indonesia        | Ba3            | Ba3          | San Marino              | Aaa            | Aaa          |
| Bahamas              | A3             | A1             | Ireland          | Aaa            | Aaa          | Sark                    | Aaa            | Aaa          |
| Bahrain              | A2             | A2             | Isle of Man      | Aaa            | Aaa          | Saudi Arabia            | A1             | A1           |
| Barbados             | Baa2           | A3             | Israel           | A1             | A1           | Singapore               | Aaa            | Aaa          |
| Belarus              | B1             | B1             | Italy            | Aa2            | Aa2          | Slovakia                | A1             | A1           |
| Belgium              | Aa1            | Aa1            | Jamaica          | B1             | Ba2          | Slovenia                | Aa2            | Aa2          |
| Belize               | Caa1           | Caa1           | Japan            | Aaa            | A1           | South Africa            | Baa1           | A2           |
| Bermuda              | Aa1            | Aaa            | Jersey           | Aaa            | Aaa          | Spain                   | Aaa            | Aaa          |
| Bolivia              | B3             | B3             | Jordan           | Ba2            | Baa3         | St.Vincent & Grenadines | B1             | B1           |
| Bosnia & Herzogovina | B2             | B2             | Kazakhstan       | Baa2           | Baa1         | Suriname                | B1             | Ba3          |
| Botswana             | A2             | A1             | Korea            | A2             | A2           | Sweden                  | Aaa            | Aaa          |
| Brazil               | Ba1            | Ba1            | Kuwait           | Aa2            | Aa2          | Switzerland             | Aaa            | Aaa          |
| Bulgaria             | Baa3           | Baa3           | Latvia           | A2             | A2           | Taiwan                  | Aa3            | Aa3          |
| Bulgaria             | B2             | B2             | Lebanon          | B3             | B3           | Thailand                | Baa1           | Baa1         |
| Canada               | Aaa            | Aaa            | Liechtenstein    | Aaa            | Aaa          | Trinidad & Tobago       | Baa1           | Baa1         |
| Cayman Islands       | Aa3            | Cayman Islands | Lithuania        | A2             | A2           | Tunisia                 | Baa2           | Baa2         |
| Chile                | A2             | A1             | Luxembourg       | Aaa            | Aaa          | Turkey                  | Ba3            | Ba3          |
| China                | A1             | A1             | Macao            | Aa3            | Aa3          | Turkmenistan            | B2             | B2           |
| Colombia             | Ba2            | Baa3           | Malaysia         | A3             | A3           | Ukraine                 | B1             | B1           |
| Costa Rica           | Ba1            | Ba1            | Malta            | A1             | A1           | United Arab Emirates    | Aa2            | Aa2          |
| Croatia              | Baa3           | Baa1           | Mauritius        | Baa2           | Baa2         | United Kingdom          | Aaa            | Aaa          |
| Cuba                 | Caa1           | NR             | Mexico           | Baa1           | Baa1         | United States           | Aaa            | Aaa          |
| Cyprus               | Aa3            | Aa3            | Moldova          | Caa1           | Caa1         | Uruguay                 | B1             | B1           |
| Czech Republic       | A1             | A1             | Monaco           | Aaa            | Aaa          | Venezuela               | B2             | B1           |
| Denmark              | Aaa            | Aaa            | Mongolia         | B1             | B1           | Vietnam                 | Ba3            | Ba3          |
| Dominican Republic   | B2             | B2             | Montenegro       | Ba2            | -            |                         |                |              |
| Ecuador              | B3             | -              | Morocco          | Ba1            | Ba1          |                         |                |              |
| Egypt                | Ba1            | Baa3           | Netherlands      | Aaa            | Aaa          |                         |                |              |
| El Salvador          | Baa3           | Baa2           | New Zealand      | Aaa            | Aaa          |                         |                |              |
| Estonia              | A1             | A1             | Nicaragua        | Caa1           | B3           |                         |                |              |
| Eurozone             | Aaa            | Aaa            | Norway           | Aaa            | Aaa          |                         |                |              |
| Fiji Islands         | Ba2            | Ba2            | Oman             | A2             | A2           |                         |                |              |
| Finland              | Aaa            | Aaa            | Pakistan         | B1             | B1           |                         |                |              |
| France               | Aaa            | Aaa            | Panama           | Ba1            | -            |                         |                |              |
| Germany              | Aaa            | Aaa            | Papua New Guinea | B1             | B1           |                         |                |              |
| Greece               | A1             | A1             | Paraguay         | B3             | B3           |                         |                |              |