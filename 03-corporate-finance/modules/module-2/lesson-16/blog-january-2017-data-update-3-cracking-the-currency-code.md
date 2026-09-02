---
title: "January 2017 Data Update 3: Cracking the Currency Code"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-3-cracking.html
published: 2017-01-20
updated_source: 2017-03-10
fetched: 2026-08-27
tags:
  - Data Update
---

# January 2017 Data Update 3: Cracking the Currency Code

_Source: [https://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-3-cracking.html](https://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-3-cracking.html) — published 2017-01-20_

There was a time in the not so distant past, where analysts could do their analysis in their local currencies and care little or not at all about foreign currencies, how they moved and why. This was particularly true for US analysts in the last half of the last century, where the US dollar was the unchallenged global currency and the US economy bestrode the world. Those days are behind us and it is almost impossible to do valuations or corporate financial analysis without understanding how to deal with currencies correctly. Since the perils of misplaying currencies can be catastrophic, I decided to spend this post getting up to speed on the basics of how currency choices play out in valuation and where the numbers stand at the start of 2017.

****

**A Currency Primer in Valuation**

**
**

In intrinsic valuation, the value of an asset is the expected cash flows on that asset, discounted back at a risk adjusted discount rate.

![](file:////Users/aswath1/Library/Group%20Containers/UBF8T346G9.Office/msoclip1/01/clip_image002.png)

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFfvLH578cCiopvO29XzUD_LNNQcmB5F_5fgt50HYv9m57WE3GqMMbDWonQ-tkYXTMxm9a52yFKHSibUaWDwOw227SywfURQVKe80OfIJ-yzMW2M7UcCw8xnNmYlPrCjbl3FL4G5epBjo/s1600/DCFequation.jpg)

Note that there is no currency specification in the DCF equation and that analysts are given a choice of currencies. So, what currency should you use in valuing a company? While some analysts view this choice rigidly as being determined by the country in which the company operates in or the currency that it reports its financial statements in, there are two basic propositions that govern this choice.

- The first is that currency is a measurement mechanism and that you should be able to value any company in any currency, since all it will require is restating cash flows, growth rates and discount rates in that currency. 

- The second is that in a robust DCF valuation, your value should be currency invariant. Put differently, the value of Petrobras should be unchanged, whether you value the company in nominal Brazilian Reais ($R), US dollars or Euros. 

The second proposition may strike some as impractical, since risk free rates vary across currencies and some currencies, like the $R, have higher risk free rates than others, like the US dollar. But the key to understanding currency invariance is recognizing that currency choices affect both your cash flows and your discount rate and if you are being consistent about your currency estimates, those effects should cancel out.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqk9YrXUt-1V4pseQEtLRMsVxzwE8HkTx2vUR4DqTlq0dOi3JC5rTqRCBkGG9qNJQz87sxycneBlKvecWO_0_92TBwesrZkwEder5Ts-uzBcE2aAj0kLu7AJUvPEWYqRzZb401HxXz-ek/s1600/DCF%2526CurrencySimple.jpg)

Intuitively, picking a high inflation currency will lead to higher discount rates but also to higher cash flows and growth rates. In fact, if the currency effect is a pure inflation effect, you can see very quickly that you could make your valuation currency-free by doing your entire analysis in real terms, where you cash flows reflect only real growth (without the boost offered by inflation) and your discount rate is built on top of a real risk free rate. Your value should be again equivalent to the value you would have obtained by using the currency of your choice in your valuation.

To make these estimation choices real, consider valuing a company that derives half its cash flows in the United States (in US dollars) and half in Brazil (in nominal $R). You can value the company in US dollars, and to do so, you would have to estimate its cost of capital in US $ and convert the portion of its cash flows that are in $R to US$ in future years; that would require forecasting exchange rates. Alternatively, you can value the company in $R, converting the portion of cash flows in US$ to $R and then estimating a cost of capital in $R. This may sound simple, even trivial, but a whole host of estimation challenges lie in wait. 

**Expected Exchange Rates**

If you want to make your valuations currency invariant, and inflation is what sets currencies apart, the way to estimate expected future exchange rates is to assume purchasing power parity, where exchange rates move to capture differential inflation. Specifically, you can get from the current exchange rate of local currency (LC) for the foreign currency (FC) to an expected exchange rate in a future year (t) using the expected inflation rates in the two currencies: 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxhMunf3GetHdlcrp-ATZwLNikO2CEoGYOGxTR7lX4PaNjJeV85KNTok5A7mcHFdkgnN0PdlMml1hJ8SZiwwZkwx4bjywu-DNSUecKuI6mwKg0WidbukBng4m9gJ5GCGMbk7C_gcfqpEg/s1600/Expected+Exchange+Rate.jpg)

Simply put, if the inflation in the local currency is 5% higher than the inflation in the US$, you are assuming that the local currency will depreciate about 5% a year. I know that exchange rate movements deviate from purchasing power parity significantly over short and perhaps even extended periods and that expected inflation can be difficult to estimate in many currencies, but there is a simple reason why you should stick with this simplistic way of forecasting exchange rates, at least when it comes to valuation. First, it is far easier (and less expensive) that creating a full-fledged exchange rate forecasting model or paying a forecaster, especially because you have to forecast exchange rate changes over very long time periods. Second, it forces you to be explicit about your inflation expectations and by extension, at least be aware of inconsistencies, where you assume one measure of inflation for exchange rates (and cash flows) and another for discount rates. (You can use forward exchange rates for the near years, as long as you are willing to then use interest rate differentials as proxies for inflation differentials.)

But what if you have strong views on the future direction of exchange rates that deviate from inflation expectations? I would argue that you should not bring them into your company valuations for a simple reason. If you incorporate your idiosyncratic exchange rate forecasts into cash flows and value, your final valuation of a company will be a joint consequence of your views on the company and of your views on exchange rates, with no easy way to separate the two. Thus, if you expect the Indian rupee to appreciate over the next five years, rather than depreciate (given your expectations of inflation in the rupee), you will find most Indian companies that you value to be cheap. If that conclusion is being driven by your exchange rate views, why invest in Indian companies when there are far easier and more profitable ways of playing the exchange rate game?

**Currency Costs of Capital**

Let's start with the challenge of estimating costs of capital in different currencies. There are two general approaches that you can use to get there. One is to compute the cost of capital in a  currency from the ground up, starting with a risk free rate and then estimating and adding on risk premiums to arrives at costs of equity, debt and capital. The other is to compute the cost of capital in a base currency (say the US dollars) and then converting that cost of capital to the local currency.

***Currency Risk Free Rates***

Every economics student, at some point early in his or her education, has seen the Fisher equation, where the nominal interest rate is broken down into an expected inflation component and an expected real interest rate:

Nominal Interest Rate = Expected Inflation + Expected Real Interest Rate

Note that this is neither a theory nor a hypothesis, but a truism, if you add no constraints on either the expected inflation and real interest rate. It is also a powerful starting point for thinking about what goes into a risk free rate and why it changes over time. It is as you add constraints on the components of interest rates that you start making assumptions which may or may not be true, and require testing. You could assume, for instance, that actual inflation in the most recent periods is a reasonable proxy for expected inflation in the future and that the real interest rate can be approximated to by the real growth rate in the economy in the most recent period (not an unreasonable assumption in mature economies). In fact, it is this proposition that I used in my last post on US markets to estimate intrinsic T.Bond rates that I compared to actual rates. I will use this framework as my back up as I look at four different ways of estimating risk free rates in different currencies.

*1. Government Bond Rate*

In this, the most common practice in valuation, analysts assume that the local currency government bond rate is the risk free rate in that currency. To justify this usage, they argue that governments will not default on local currency bonds, since they can always print off enough currency to pay off debt. In table 1, I graph [local currency 10-year government bond rates as of January 1, 2017](http://www.stern.nyu.edu/~adamodar/pc/blog/currencyriskfree2017.xlsx) for those currencies where I was able to obtain them.  

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPFvI6_Dymbp53CQ_Ytt8EbT-Jk7hHCwLApqnxLgbXrRhrxaWHZ6fex8ScMh6oZ66OiCFMkkGEYplC3WDXC9tUu3qTuwZfnRzSXdsb-4JLs-c51M3ahM7uRY3vYzYEGWXJ7MmtCL0itrI/s1600/govtbondrates.jpg)

This approach has the advantage of simplicity and is perhaps even intuitively defensible but there are real dangers associated with it. The first is that the government bond may not be liquid and traded and/or the government exercises control over the rate, it is not a market-set rate reflecting demand and supply. The second is that implicit in the use of the government bond rate as the risk free rate is the assumption that governments never default in the local currency. That assumption has been violated at least a half a dozen times just in the last twenty years, thus making the government bond rate a "risky", rather than a risk free, rate. The third is that using government bond rates as local currency risk free rates while using actual inflation rates as expected inflation can lead to both inconsistent and currency dependent valuations. For instance, assume that you decide to value Natura, the Brazilian cosmetics company, in $R and use the Brazilian government $R bond rate of 11.37%, on January 1, 2017, as the risk free rate while using the actual inflation rate of 6.29% (inflation rate last year, according to government statistics) as the expected inflation rate. The value that you estimate for the company will be much lower than the value that you estimate for the company if you valued it in US dollars, with a risk free rate of 2.50% and an expected inflation rate of 2%. The reason for the valuation difference is intuitive. By using the $R numbers, you are effectively using a real risk free rate of 5.08%, when you do your valuation in $R, and only 0.5%, when you do your valuation in US dollars.

*
*
*2. Government Bond Rate, net of default spread*

In this approach, you do not start with the presumption that governments are default free. Instead, you start with the local currency government bond rate and subtract out the portion of that rate that you believe is due to perceived default risk:

Risk free rate in local currency = Local Currency Government Bond rate – Default Spread in Local Currency Government Bond rate

The practical question then becomes how best to estimate the local currency default spread and there are a few approaches, though each comes with limitations. The first is to find a US dollar denominated bond issued by the government in question and netting out the US T.Bond rate, thus getting a default spread on the bond. The second is to use a sovereign CDS spread for the country as a proxy for default risk. In the table below,  Subtracting these default spreads from the local currency bond rates, on the assumption that default risk in both local and foreign currency borrowing is equivalent, would yield local currency risk free rates. Using the [sovereign rating-based default spreads](http://www.stern.nyu.edu/~adamodar/pc/blog/currencyriskfree2017.xlsx), we can estimate the risk free rates in different currencies in January 2017:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNIXfItsow9XKeuXfs3zmTx422Iy-8c99JUSXOuFKyIXGny2Ry7v2apyP45DldNt8FXZnAKshu3Gx3Q82pKUF633mrInG2OduLf5kWgBk1dwkEf2-6TW5EL7sHOo1WesKMDRfalRt3QvU/s1600/GovtBondRateNetSpread.jpg)

This approach comes with its own perils that are layered on top of the assumption that the government bond rate is a market-set interest rate. First, it assumes that the local currency sovereign rating is measuring the default risk in the currency and that you can estimate the default spread based on it. Second, both the rating-based and sovereign CDS default spreads are US dollar based and netting it out against a local currency government bond rate can be viewed as inconsistent.

*3. Differential Inflation Based Rates*

The third approach is to ignore government bond rates in the local currency entirely, either because you believe that they are not liquid enough to yield reliable numbers or because they contain default risk. Instead, you start with a risk free rate in a currency where you believe that the government bond rate is a reliable measure of the risk free rate (US Treasury Bond, German Euro Bond) and then add to this number the differential inflation rate between the US dollar and the local currency.

Local Currency Risk free Rate = US $ Risk free Rate + (Expected inflation in local currency – Expected inflation in US $)

This is an approximation that works reasonably well when local currency inflation is low (close to the US dollar inflation rate) but the more precise version of this formulation will be based upon compounding, just as the Fisher equation was:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyYrEh-wmpwfNEqf817_kEl88jrCKTSdHJOdIoR2MRmaJXGiitg7AFcc_A6YUoKCXoyUAgVKmrWlnk6GwNk4oiQW-jwpg8Aal8G1W4sy5YFWPi-pLcrd_LwLcyuquKmVRc8DWYnu7pK2c/s1600/CurrencyRiskfreeLongWay.jpg)

The [linked table lists differential inflation based risk free rates in all currencies](http://www.stern.nyu.edu/~adamodar/pc/blog/FundCurrencyRiskfree2017.xlsx), using expected inflation rates (the World Bank's estimates) and the US dollar (estimated at about 2%, the difference between the US 10-year T.Bond and TIPs rates).  If you are concerned about being able to forecast expected inflation in the local currency, you should rest easy. As long as you use that same expected inflation rate in your cash flow estimation, your valuation will be inflation-invariant and currency consistent, since the effects of under or over estimating inflation will cancel out.

*4. Intrinsic Risk Free Rates*

In the differential inflation approach, using the US dollar risk-free rate as the starting point, you are assuming a global real risk free rate, set equal to that rate embedded in the US treasury bond rate as the base for all local currency risk free rates. If you feel uncomfortable with this assumption, you can estimate a synthetic risk free rate from scratch, drawing on the Fisher equation:

Risk free Rate = Expected Real Interest Rate + Expected inflation rate

You can augment this equation with the assumption that long term real growth in an economy will converge on the long term real interest rate. 

Expected Real Interest Rate = Expected Real Growth Rate

Synthetic Risk free Rate = Expected Real Growth Rate + Expected inflation rate

This approach yields the maximum flexibility but it will also create differences in valuations in different currencies. This l[inked table lists out synthetic risk free rates](http://www.stern.nyu.edu/~adamodar/pc/blog/FundCurrencyRiskfree2017.xlsx) using this approach, using average real GDP growth as your expected real growth rate. The downside of this approach will be that your valuations will vary across currencies, yielding difficult-to-defend conclusions sometimes, where a company looks cheap when analyzed in US dollars but expensive when valued again in the local currency. The advantage of this approach, as with the differential inflation approach, is that you can estimate risk free rates for many more countries than with the government bond approach.

***Currency Cost of Capital***

If you start with a  risk free rate in a local currency and build up to a cost of capital using equity risk premiums and default spreads, often available only in dollar-based markets, you are effectively assuming that risk premiums are absolute numbers that don't change as the risk free rate changes. Thus, the equity risk premium of 5.69%, estimated in a dollar-based US market, applies not only to the US dollar risk free rate of 2.45% but also to the Nigerian Naira risk free rate of 10.77%. That is a stretch, since you would expect to risk premium you charge to be higher with the latter than the former. There is an easy and logical fix for it and it lies in the differential inflation approach. Rather than apply it to adjust the US$ riskfree rate to a local currency rate, you could apply it to the cost of equity or capital instead:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiv5zUV3o4rLaqmjzOrUO0AzyQWMQBbI0pwBf1Q8zkQp7kj07qRPOEJGI3RJWrkug6JmLWDYO9yUOTkgirBcmdDkfwwmwSn0s6h8aQzZTvVjSNUzgW5SLkB7WhGLb7qTYBarvWs8Wz-m78/s1600/CostofCapitalDiffInflation.jpg)

Thus, if your cost of capital in US $ is 8%, the inflation rate in $R is 6% and in US$ is 2%, your cost of capital would be 12.24%. (Using the short cut of just adding the differential inflation would yield 12%). As part of my data update, I have reported costs of capital, by industry, in US dollars, for the last two decades. In this year's update, I have added a differential inflation feature allowing you to [change that cost of capital to any currency of your choice in this spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/waccGlobalPost.xls). You will need to input the inflation rate in the local currency to get the costs of capital to update and you are welcome to use either the estimates that I supply in an additional worksheet or enter your own. Remember, though, that you should stay true to whatever this estimate is when estimating growth rates and cash flows in that currency.

**The Closing**

If your valuations are sensitive to your currency choice, you face a fundamental problem. You can find the same company, at the same pricing and point in time, to be both under and over valued, an indefensible conclusion. That conclusion, though, is being driven by some aspect of your valuation process that is making your company's fundamentals (risk, growth and cash flow potential) look different when you switch currencies. That, in my view, is a violation of intrinsic valuation and it requires you to make your inflation assumptions explicit and check for consistency. 

**YouTube Video**

**
**
**Datasets**

- [Government Bond Rates, Default Spreads and Risk free Rates - By Currency](http://www.stern.nyu.edu/~adamodar/pc/blog/currencyriskfree2017.xlsx)

- [Inflation Rates, GDP Growth and Fundamental Growth - By Country](http://www.stern.nyu.edu/~adamodar/pc/blog/FundCurrencyRiskfree2017.xlsx)

- [Cost of Capital, by Sector - January 2017 (with currency translator)](http://www.stern.nyu.edu/~adamodar/pc/blog/waccGlobalPost.xls)

**Data 2017 Posts**

- [Data Update 1: The Promise and Perils of Big Data](http://aswathdamodaran.blogspot.in/2017/01/january-2017-data-update-1-promise-and.html)

- [Data Update 2: The Resilience of US Equities](http://aswathdamodaran.blogspot.in/2017/01/january-2017-data-update-2-resilience.html)

- [Data Update 3: Cracking the Currency Code - January 2017](http://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-3-cracking.html)

- [Data Update 4: Country Risk and Pricing, January 2017](http://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-4-country-risk.html)

- [Data Update 5: A Taxing Year Ahead?](https://youtu.be/ox1ZQ0sbqc8?list=PLUkh9m2BorqnapcQ03A0a_jsbele2kKbp)

- [Data Update 6: The Cost of Capital in January 2017](http://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-6-cost-of.html)

- [Data Update 7: Profitability, Excess Returns and Corporate Governance- January 2017](http://aswathdamodaran.blogspot.com/2017/01/january-2017-data-update-7.html)

- [Data Update 8: The Debt Trade off in January 2017](http://aswathdamodaran.blogspot.com/2017/02/january-2017-data-update-8-dark-and.html)

- [Data Update 9: Dividends and Buybacks in 2017](http://aswathdamodaran.blogspot.com/2017/02/january-2017-data-update-9-dividends.html)

- [Data Update 10: The Pricing Game](http://aswathdamodaran.blogspot.com/2017/03/january-2017-data-update-10-pricing-game.html)
