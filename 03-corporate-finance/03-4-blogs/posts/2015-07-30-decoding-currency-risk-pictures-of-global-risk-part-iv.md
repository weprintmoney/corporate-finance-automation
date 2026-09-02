---
title: "Decoding Currency Risk: Pictures of Global Risk - Part IV"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html
published: 2015-07-30
updated_source: 2015-08-06
fetched: 2026-08-27
tags:
  - Country Risk
  - Currency Risk
---

# Decoding Currency Risk: Pictures of Global Risk - Part IV

_Source: [https://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html](https://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html) — published 2015-07-30_

In my last three posts, I have looked at country risk, starting with [measures of that risk](http://aswathdamodaran.blogspot.com/2015/07/groundhog-day-in-greece-hijinks-in.html) and then moving on to [valuing](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html) and [pricing](http://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html) that risk. You may find it strange that I have not mentioned currency risk in any of these posts on country risk, but in this one, I hope to finish this series by looking first at how currency choices affect value and then at the dynamics of currency risk.  

**Currency Consistency**

A fundamental tenet in valuation is that you have to match the currency in which you estimate your cash flows with the currency that you estimate the discount rate that you use to discount those cash flows. Stripped down to basics, the only reason that the currency in which you choose to do your analysis matters is that different currencies have different expected inflation rates embedded in them. Those differences in expected inflation affect both our estimates of expected cash flows and discount rates. When working with a high inflation currency, we should therefore expect to see higher discount rates and higher cash flows and with a lower inflation currency, both discount rates and cash flows will be lower. In fact, we could choose to remove inflation entirely out of the process by using real cash flows and a real discount rate. 

***Currencies and Discount Rates***

There are two ways in which you can incorporate the expected inflation in a currency into the discount rate that you estimate in that currency. The first is through the risk free rate that you use for the currency, since higher expected inflation should result in a higher risk free rate. The second is by converting the discount rate that you estimate in a base currency into a discount rate in an alternate currency, using the differential inflation between the currencies.

*a. Risk free rate*

A risk free rate is more than just a number that you look up to estimate discount rates. In a functioning market, investors should set the risk free rate in a currency high enough to cover not only expected inflation in that currency but also to earn a sufficient real interest rate to compensate for deferring consumption.

Risk free rate in a currency = Expected inflation in that currency + Real interest rate

The risk free rate should therefore be higher in a high-inflation currency than using that higher rate should bring inflation into your discount rate.

But how do we get risk free rates in different currencies? While most textbooks would suggest using the rate on a government bond, denominated in the currency in question, that presumes that governments are default free and that the government bond rate is a market-determined rate. However, governments are not always default free (even with local currency borrowings) and the rate may not be market-set. In July 2015, I started with the government bond rates in 42 currencies and cleansed them of default risk by subtracting out the sovereign default spreads (based on local currency sovereign ratings) from them to arrive at risk free rates in these currencies, which you can find in the table below:

*
*

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_OSlmAhPMgQJhMNlQ1HKNTt_k8dd-Db1Bfq75SdHiBjBWBZ_Lyeg29mALNv9Wjcl6TcCj5iegDl2CpfofY2P03jNJmYIultqRZqsHsezOLs5G4VwM4M4OZZndDj0Pp94FIXhqu_ddAkA/s1600/riskfreerates.jpg)
*Risk free rates in July 2015*

Note that the default spread is set to zero for all Aaa rated governments, and the government bond rate becomes the risk free rate in the currency. Thus, the risk free rates in US dollars is 2.47% and in Swiss Francs is 0.16%. To compute the risk free rate in $R (Brazilian Reais), I subtract out my estimate of the default spread for Brazil (1.90%, based on its Baa2 rating) from the government bond rate of 12.58% to arrive at a risk free rate of 10.68%. To estimate a cost of equity in nominal $R for an average risk company with all of its operations in Brazil, you would use the 10.68% risk free rate in $R and the equity risk premium of 8.82% that I reported in my last post to arrive at a cost of equity of 19.50% in $R. That number would be higher for above-average risk companies, with a beta operating as your scaling mechanism.

*b. Differential inflation*

There are two problems with the risk free rate approach. The first is that it not only requires that you be able to find a government bond rate in the currency that you are working with, but also that the rate be a market-determined number. It remains true that in much of the world, government bond rates are either artificially set by governments or actively manipulated to yield unrealistic values. The second is that you are adding equity risk premiums that are computed in dollar-based markets (since the default spreads that they are built upon are from dollar-based bond or CDS markets) to risk free rates in other currencies. You could legitimately argue that the equity risk premium that you add on to a $R risk free rate of 10.68% should be higher than the 8.82% that you added to a US $ riskfree rate of 2.25% in July 2015.

If the differences between currencies lies in the fact that there are different expectations of inflation embedded in them, you should be able to use that differential inflation to adjust discount rates in one currency to another. Thus, if the cost of capital is computed in US dollars and you intend to convert it into a nominal $R cost of capital, you could do so with the following equation:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDlE3Pa-2ONwcRt9r0wqMOlhtRKAi3YSUPmyLk2WEFAyZxF57IIyxitZnVpS3eaYFrR5D3VlBAaxWJ4R9RZYoZvO9gcA48FZDipFFOJ7HDTauE8SU1Lee1EM1OWEqAplxkO8Ionqzv3Hw/s1600/diffinflationdiscrate.jpg)

To illustrate, if you assume that the expected inflation rate in $R is 9.5% and in US $ is 1.5%, you could compute the cost of equity in US$ and then adjust for the differential inflation to arrive at a cost of equity in $R:

*Cost of equity for average risk Brazilian company in US $ = 2.25% + 8.66% = 10.91%*

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX5VLLobBXS9zNNAOa8qiNx909lcHW-cLlMATSPAOzCK8JLDZAvWqz0bAIIJ-kUegKdxhggaS0EDgWZqdmbLEL4NHm449AZ2X9stiI2xA5q_eiSaJt9D7Xt3SoGmEETTBN58d6nDs7kG0/s1600/costofequity%2524R.jpg)

The cost of equity of 19.65% that we derive from this approach is higher than the 19.50% that we obtained from the risk free rate approach and is perhaps a better measure of cost of equity in $R.

This approach rests on being able to estimate expected inflation in different currencies, a task that is easier in some than others. For instance, getting an expected inflation rate in US dollars is simple, since you can use the difference between the 10-year T.Bond rate and the TIPs (inflation-indexed) 10-year bond rate as a proxy. In other currencies, it can be more difficult, and you often only have past inflation rates to go with, numbers that are prone to government meddling and imperfect measurement mechanisms. Notwithstanding these problems, I report inflation rates in different countries, using the average inflation rate from 2010-2014 for each country.

I also report the inflation rate in 2014 and the IMF expectations for inflation (though I remain dubious about their quality) for each country.

***Currencies and Cash Flows***

Following the currency consistency principle is often easier with discount rates, where your inflation assumptions are generally either explicit or easily monitored, than it is with cash flows, where these same assumptions are implicit or borrowed from others. If you add in accounting efforts to adjust for inflation and inconsistencies in dealing with it to the mix, it should come as no surprise that in many valuations, it is not clear what inflation rate is embedded in the cash flows.

*a. Inflation in your growth rates*

In most valuations, you start with base year accounting numbers on revenues, earnings and cash flows and then attach growth rates to one or more of these numbers to get to expected cash flows in the future. At the risk of stating the obvious, the expected inflation rate embedded in this growth rate has to be the same inflation rate that you are incorporating in your discount rate. This simple proposition is put to the test, though, by the ways in which we estimate these expected growth rates, which is to use history, trust management/analyst projections for the future or base it on fundamentals (how much the company is reinvesting and how well it is reinvesting):

- Past Growth: With historical growth, where you estimate growth by looking at the past, your biggest exposure to mismatches occur in currencies where inflation rates have shifted significantly over time. For instance, assume that you are valuing your company in Indian rupees in July 2015 and that the average inflation rate in India, which was 8% between 2010 and 2014 is expected to decline to 4% in the future. If you use historical growth rates in earnings, between 2010 and 2014, for an Indian company, you are likely to over value the company because its past growth rate will reflect past inflation (8%) but your discount rates, computed using expected inflation or current risk free rates in rupees, will reflect a much lower inflation rate. 

- Management/Analyst Forecasts: With management or analyst forecasts, the problem is a different one, since the expected inflation rates that individuals use in their forecasts can vary widely. While there is no reason to believe that your estimate of expected inflation is better than theirs, it is undeniably inconsistent to use management estimates of expected inflation for growth rates and your own or the market's estimates of inflation, when estimating discount rates.

- Fundamental or Sustainable Growth: I believe that the best way to keep your valuations internally consistent is to tie growth to how much a company is reinvesting and how well it is reinvesting. The measures we use to measure reinvestment and the quality of investment are accounting numbers and inflation mismatches can enter insidiously into valuations. Assume, for instance, that you are estimating reinvestment rates and returns on capital for a Brazilian company, using its Brazilian financial statements. Since Brazilian accounting allows for inflation adjustments to assets, the return on capital that you compute is closer to a real return on capital (with no or low inflation embedded in it) than to a nominal $R return on capital, if inflation accounting works as advertised. In countries like the United States, where assets are not adjusted for inflation, you can argue that the return on capital is a nominal number, but one that reflects past inflation, not expected future inflation.  In either case, the growth rate that you compute from these numbers will be skewed.

*b. Expected Exchange Rates*

It is common practice, in some valuation practices, to forecast cash flows in a base currency (even if it is not the currency that you plan to use to estimate your discount rate) and then convert into your desired currency, using expected exchange rates. Thus, a Brazilian analyst who wants to value a Brazilian company in US dollars may estimate expected cash flows in nominal $R first and then convert these cash flow into US $, using an $R/US $ exchange rate.  The big estimation question then becomes how best to estimate expected exchange rates and there are three choices. 

- Use the currency exchange rate: The first one, especially in the absence of futures or forward markets, is to use the current exchange rate to convert all future cash flows. This will result in an erroneous value for a simple reason: it creates an inflation mismatch. If, for instance, the expected inflation rate in $R in 9.5% and in US$ is 1.5%, you will significantly over value your company with this approach, because you have effectively built into a 9.5% inflation rate into your cash flows (by using a constant exchange rate) and a 1.5% inflation rate into your discount rate (since you are estimating it in US dollars).

- Use futures and forward market exchange rates: This is more defensible but only if you then extract risk free rates from these same futures/forward market prices. (This will require that you assume interest rate parity in exchange rates and derive the interest rate in $R from the $R/US$ forward rate). In addition, in many emerging market currencies, the forward and futures markets tend to be operational only at the short end of the maturity spectrum, i.e., you can get 1-year forward rates but not 10-year rates.

- Use purchasing power parity: With purchasing power parity, the expected exchange rates are driven by differential inflation in the currencies in question. Thus, if purchasing power parity holds and the inflation rates are 9.5% in $R and 1.5% in US$, the $R will depreciate roughly 8% every year. While I am sure that you can find substantial evidence of deviation from purchasing power parity for short or even extended periods, here is why I continue to stick with it in valuation. By bringing in the differential inflation into both your cash flows and the discount rate, it cancels out its effect and thus makes it less critical that you get the inflation numbers right. Put differently, you can under or over estimate inflation in $R (or US $) and it will have no effect on your value.

***Currencies and Value***

If you can make it through the minefields to estimate cash flows and discount rates consistently, i.e., have the same expected inflation rate in both inputs, the value of a company or a capital investment should be currency invariant. In other words, if you value Tata Motors in Indian rupees, you should get the same value for the company, if you value it entirely in US dollars. If you don't get the same value, I would argue that the difference comes from one or two sources:

- Inflation inconsistencies: It is stemming from inconsistencies in the way that you have dealt with inflation in different currencies, since a company's value should come from its fundamentals and not from which currency you chose to evaluate it in. 

- Currency views: You have built in a currency view into your company valuation. Thus, if you assume that the $R will strengthen against the US dollar in the next 5 years,  when estimating cash flows, notwithstanding the higher inflation rate, you will find your company to be under valued, when you value it in $R. If that is the case, my suggestion to you would be to just buy currency futures or options, since you are making a bet on the currency, not the company.

The bottom line is that your currency choice should neither make nor break your valuation. A well-run company that takes good investments should stay valuable, whether I value it in US dollars, Euros, Yen or Rubles, just as a badly run or risky company will have a low value, no matter what currency I value it in.

**Currency Risk**

When working with cash flows in a foreign currency, it is understandable that analysts worry about currency risk, though their measurement of and prescriptions for that risk are often misplaced. First, it is not the fact that exchange rates change over time that creates risk, it is that they change in unexpected ways. Thus, if the Brazilian Reai depreciates over the next five years in line with the expectations, based upon differential inflation, there is no risk, but if it depreciates less or more, that is risk. Second, even allowing for the fact that there is currency risk in investments in foreign markets, it is not clear that analysts should be adjusting value for that risk, especially if exchange rate risk is diversifiable to investors in the companies making these investments. If this is the case, you are best served forecasting expected cash flows (using expected exchange rates) and not adjusting discount rates for additional currency risk. 

It is true that currency and country risk tend to be correlated and that countries with high country risk also tend to have the most volatile currencies. If so, the discount rates will be higher for investments in these countries but that augmentation is attributable to the country risk, not currency risk.

**Currency Rules for the Road**

It is easy to get entangled in the web of currency effects and lose sight of your quest for value, but here are few rules that I think may help you avoid distractions.

- Currencies are measurement mechanisms, not value drivers: As I write this post, it is a hot day in New York, with temperatures hitting 95 degrees in fahrenheit. Restating that temperature as 35 degrees celsius may make it seem cooler (it is after all a lower number) but does not alter the reality that I will be sweating the minute that I step out of my office. In the same vein, if I value an Argentine company in a risky business, converting its cash flows from Argentine pesos to US dollars will not make it less risky or less exposed to Argentine country risk.

- Pick a currency and stick with it: The good news is that if your valuations are currency invariant, all you have to do is pick one currency (preferably one that you are comfortable with) and stick with it through your entire analysis. 

- Make your inflation assumptions explicit: While this may cost you some time and effort along the way, it is best to be explicit about what inflation you are assuming, especially when you estimate cash flows or exchange rates, to make sure that it matches the inflation assumptions that you may be building into your discount rates,

- Separate your currency views from your company valuations: It is perfectly reasonable to have views on currency movements in the future but you should separate your currency views from your company valuations. If you do not, it will be impossible for those using your valuations to  determine whether your judgments about valuation are based upon what you think about the company or what you feel about the currency. It is this separation argument that is my rationale for sticking with much maligned purchasing power parity in estimating future exchange rates.

- You can run, but you cannot hide: If inflation is high and volatile in your local currency, it is easy to see why you may prefer working with a different, more stable currency. It is the reason why so much valuation and investment analysis in Latin America was done in US dollars. The bad news, though, is that while switching to US dollars may help you avoid dealing with inflation in your discount rate, you will have to deal with it in your cash flows (where you will be called upon to forecast exchange rates). 

**Papers to read**

- [My paper on country risk (July 2015)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2630871)

**Data attachments**

- [Risk free rates in different currencies (July 2015)](http://www.stern.nyu.edu/~adamodar/pc/blog/riskfreeratesJuly2015.xls)

- [Inflation rates, by country (July 2015)](http://www.stern.nyu.edu/~adamodar/pc/blog/countryinflationratesJuly2015.xls)

**Posts on Country Risk**

- [Groundhog day in Greece, Hijinks in Brazil and Market Chaos in China: Pictures of Global Risk - Part 1](http://aswathdamodaran.blogspot.com/2015/07/groundhog-day-in-greece-hijinks-in.html)

- [Valuing Country Risk: Pictures of Global Risk - Part II](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html)

- [Pricing Country Risk: Pictures of Global Risk - Part III](http://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html)

- [Decoding Currency Risk: Pictures of Global Risk - Part IV](http://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html)
