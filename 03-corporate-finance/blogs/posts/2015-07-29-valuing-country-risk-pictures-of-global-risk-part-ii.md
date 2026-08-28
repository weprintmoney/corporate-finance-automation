---
title: "Valuing Country Risk: Pictures of Global Risk - Part II"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html
published: 2015-07-29
updated_source: 2015-08-08
fetched: 2026-08-27
tags:
  - Country Risk
  - Equity Risk Premiums
---

# Valuing Country Risk: Pictures of Global Risk - Part II

_Source: [https://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html](https://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html) — published 2015-07-29_

In my last post, I looked at the determinants of country risk and attempts to measure that risk, by risk measurement services, ratings agencies and by markets. In this post, I would first like to focus on how investors and business people can incorporate that risk into their decision-making. In the process, I will argue that while it is easy to show that risk varies across countries, significant questions remain on how best to deal with that risk when making investment and valuation judgments.

**Valuing Country Risk**

If the value of an asset is the risk-adjusted present value of its expected cash flows, it stands to reason that cash flow claims in riskier countries should be worth less than otherwise cash flow claims in safer parts of the world. This common-sense principle, though, can be complicated in practice, because there are two ways in which country risk can flow through into value. 

- Adjust expected cash flows: The first is to adjust the expected cash flows for the risk, bringing in the probability of an adverse event occurring and computing the resulting effect on cash flows. In effect, the expected cash flows on an investment will be lower in riskier countries than an otherwise similar investment in safer countries, though the mechanics of how we lower the cash flows has to be made explicit. 

- Modify required return: The second is to augment the required return on your investment to reflect additional country risk. Thus, the discount rate you use for cash flows from an investment in Argentina will be higher than the discount rate that you use for cash flows in Germany, even if you compute the discount rate in the same currency (US dollars or Euros, for instance). The question of whether there should be an additional premium for exchange rate risk is surprisingly difficult to answer, though I will give it my best shot later in this post. 

While both processes are used by analysts, the adjustments made to cash flows and discount rates are often arbitrary and risk is all too often double counted. The questions of which types of risks to bring into the expected cash flows and which ones into discount rates but also how to do so remain open and I will lay out my perspective in this post.

**Adjust Cash Flows**

If there is a probability that your business can be adversely impacted by risk in a country, it stands to reason that you should incorporate this effect into your expected cash flow. There are three ways that you can make this adjustment.

- *Probabilistic adjustment*: The first is to estimate the likelihood that a risky event will occur, the consequences for value and cash flow if it does and to compute an expected value. This is the best route to follow for discrete, country-specific risks that can have large or catastrophic effects on your business value, since discount rates don't lend themselves easily to discrete risk adjustment and the fact that the risk is country-specific suggests that globally diversified investors may be able to diversify away some or much of the risk. A good example would be nationalization risk in a country prone to expropriating private businesses, where bringing in its likelihood will lower expected earnings in future periods and cash flows. 

- *Build in the cost of protection*: The second approach is to estimate the cost of buying protection against the country risk in question and bring in that cost into your expected cash flows. Thus, if you could buy insurance against nationalization, you could reduce your expected earnings by that insurance cost and use those earnings as a basis for estimating cash flows. This approach is best suited to those risks that can be insured against either in the insurance or financial markets. It is also my preferred approach in dealing with corruption risk, which, [as I have argued in a prior post](http://aswathdamodaran.blogspot.com/2012/04/governments-and-value-iii-bribery.html), is more akin to an unofficial tax imposed on the company.

- *Cash flow hair cuts*: The third way to adjust for country risk is to lower expected cash flows in risky countries 10%, 20% or more, with the adjustment varying across countries (with bigger hair cuts for riskier countries) and analysts (with more risk averse analysts making larger cuts). The perils of this approach are numerous. The first is that it is not only arbitrary but it is also specific to the individual making it, causing it to vary from investment decision to decision and from analyst to analyst. The second is that, once made, the adjustment is hidden or implicit and subsequent decision makers may not be aware that it has already been made, resulting in multiple risk adjustments at different levels of the decision-making process.

A key distinction between the first approach (probabilistic) and the other two (building in cost of insuring risk or haircutting cash flows) is that taking into account the probability that your business could be adversely impacted by an event and adjusting the expected cash flows for the impact does not "risk adjust" the cash flows. You will attach the same value to a risky business as you would to a safe business with the same expected cash flows.

**Adjust Required Returns**

The second approach to dealing with country risk is to adjust discount rates, pushing up the required returns (and discount rates) for investments made in riskier countries. Those higher rates will push down value, thus accomplishing the same end result as lowering expected cash flows.

***Fixed Cash Flow Claims (Fixed Income)***

With fixed income claims (bonds, financial guarantees), this is easy enough to do, requiring an additional default spread (for country risk) in the desired interest rate, which, in turn, will lower value. In my last post on country risk, I looked at measures of sovereign default risk including sovereign ratings and credit default swaps. If you have a fixed cash flow claim against a sovereign, you could use these default risk measures to calculate the value of these claims. Thus, if the sovereign CDS spread for Brazil is 2.91% and the risk free rate in US dollars is 2.47%, you would price Brazilian dollar denominated bonds or fixed obligations to earn you 5.38%. 

But what if your claim is against a company or business in a risky country? There are two ways in which you could estimate the default spread that you would use to value this claim:

1. *Company Rating*: Just as ratings agencies and CDS markets estimate default risk in sovereigns, they also estimate default risk in some companies, especially larger ones. If your fixed cash flow claim is against a company where one or both of these are available, you can use them to compute an expected return (and discount your fixed claims at that rate). To illustrate, Vale, a Brazilian mining company, has a bond rating of Baa2 from Moody's in July 2015, and the default spread for a Baa2 rated bond rated bond is 1.75%. Since ratings agencies already incorporate (at least in theory) the fact that Vale is a Brazilian company into the bond rating, there is no need to consider country risk.

*US dollar cost of debt for Vale = US $ Risk free rate + Default Spread based on rating = 2.25%+1.75%  = 4.00%*

2. *Country Default Spread + Company Default Spread*: For many companies in emerging markets, the first approach will be a non-starter, and for these companies, you will have to approach the cost of debt estimation in two steps. In the first step, you will have to assess the default risk of the company, using its financial statements; I use an interest coverage ratio to estimate a synthetic bond rating and a default spread. In the second, you have to estimate the default spread for the country in which the company is incorporated. For smaller companies that have no way of avoiding the country risk, the US dollar cost of debt becomes:

*US dollar cost of debt for company = Risk free rate + Company Default Spread + Country Default Spread*

To illustrate, I estimated a synthetic rating of AAA for Bajaj Auto, an Indian auto manufacturer. To get Bajaj Auto’s cost of debt in US dollars, I would add the default spread based on this rating (0.40%) and the default spread for India (2.20%) to the US dollar risk free rate (2.25%), yielding a composite value of 4.65%. For larger companies with some or a great deal of global exposure, it is possible that only a portion of the country default spread will apply.

***Residual Cash Flow Claims (Equity)***

When valuing equity claims, the process of adjusting for country risk becomes more complicated. First, since equity claim holders don't get paid until the fixed cash flow claims have been met, they face more risk and should demand higher rewards for bearing that risk. Second, since equity investors can diversify away some risks, it is possible for a global investor to be exposed to these risks at the country level and still not demand a higher required return for these risks. Thus, if you are augmenting your required returns for country risk, you are arguing that some country risk is not diversifiable to the investors pricing the company exposed to that risk either because they don't have the capacity to diversify away that risk (by holding a globally diversified portfolio) or because there is correlation across countries that results in even globally diversified portfolios continuing to be exposed to country risk. Third, a multinational company is exposed to risky in many countries and not just to the risk of the country in which it is incorporated. Consequently, you have to separate the estimating of risk premiums for countries from that of risk premiums for companies.

*Equity Risk Premiums*

In earlier posts on this topic, I describe the process by which I estimate equity risk premiums for countries. Briefly summarizing, I start with a premium that I estimate for the S&P 500 at the start of every month as my "mature market premium" and add to that premium an additional country risk premium for riskier countries. I use either the sovereign rating or CDS spread as my measure of country risk, treating all countries with ratings of Aaa (AAA) or sovereign CDS spreads close to the US CDS spread as mature markets and estimating the equity risk premium for other markets as follows:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbucrEhyEjaAo7HjH5HgRy5MeS4kMULZ_84tQOZ05y6N28dMa67ooPz070VHHZYDRmz7G-OZpKmiUc4iGi9EFJ4A5GqWxq_6hev7nT3QD3sJK-55-OrykkbWZzyCJM3Q_d5svSGc2sfPs/s1600/ERPSetup.jpg)

To illustrate, my estimate of the equity risk premium for the S&P 500 at the start of July 2015 was 5.81%, and my estimate of the equity risk premium for Brazil (with its Baa2 sovereign rating and 1.90% default spread at the start of July) is 8.82%:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDa1mSh4LrjDKtRyh8mnabzkYTaf4QMo-sOYbiRfXn4PpviuopavdVN3-yWnSooxdfF9sNEisdbDz1iaNY85Wf18kljFV9TTOFBbyRl2w3UgNx83VLoFpCnt63pLwXXWbX32gN520uMEE/s1600/BrazilERP.jpg)

The standard deviations of the Bovespa (20.25%) and the Brazilian government bond (12.76%) are used to scale up the default spread to yield an equity risk premium of 8.82%.

Using this approach and extrapolating across countries, I obtained [updated equity risk premiums for 169 countries in July](http://www.stern.nyu.edu/~adamodar/pc/ctrypremJuly15.xls) and the results are contained in this data set. The global picture of equity risk, at least as I see it, is in below:

via [chartsbin.com](http://chartsbin.com/view/35568)

*Company Exposure to Equity Risk*

The standard practice in valuation is to look at a company's country of incorporation and assign an equity risk premium to it, based on that choice, a practice that has its roots in simpler times when much or all of most companies' revenues came from domestic markets and where multinationals were the exception, rather than the rule.

That practice is indefensible in today's markets where most companies, including many small firms, derive their revenues from across the globe and often have their production spread over many countries. It makes far more sense to take a weighted average of equity risk premiums across these many markets to get to a company equity risk premium. The equity risk premiums themselves can be weighted on any of the following:

- *Revenues*: To the extent that your revenue stream is dependent upon the economic health of the country from which it is derived, you could argue that it is revenue that you should be focusing on. 

- *EBITDA or Earnings*: Since value is a function of cash flows (and not revenues), you may be inclined to use the EBITDA, by region, to weight equity risk premiums. There are three concerns you should have, though. The first is that many companies don't break down EBITDA, by region, while most break down revenues globally. The second is that accounting judgments come into play when assessing earnings by region, since expenses have to be allocated across regions. Much as we would like to believe that these allocations are driven by economic fundamentals, it is undeniable that tax considerations play a role. Third, unlike revenues which are always positive, the EBITDA for a region can be negative and it is not clear how you deal with negative weights.

- *Assets*: If you are an asset-based company (real estate or hospitality), your primary exposure to country risk may be at the asset level, and your most logical basis for computing an equity risk premium is to weight it based on assets. As with earnings, companies are not always forthcoming breaking down assets and even when broken down, the reported values tend to be book values (rather than market values).

- *Production*: In some cases, your primary exposure to risk may be to your operations rather than your revenue streams. In other words, if country risk leads you to shut down your factories, refineries or mines, it does not matter where you generate your revenues. Thus, with natural resource companies and companies that require significant infrastructure investments, you may choose to weight based upon where your production is centered. This is rarely reported in full in most company financials, though you may be able to guess, if you are familiar with the company.

To illustrate, Coca Cola, while headquartered in the United States, has revenues across much of the globe and its 2014 annual report breaks revenues down into geographical regions. Using that revenue breakdown with the weighted ERP of each region from the last section, we estimate an equity risk premium of 6.90% for Coca Cola.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihsfZ6bdsR8IaqNiHGtZOKEaAfaF2bjAopUG-h49el4NK3YZgdibK2WgSHWC4w5ANJ7ZRnMD88qFSzkrWLOXrZyZy9mljMVmSVriPNS8gsK00_S2SJYlLxPWPoZJNOKqop32L66RHgYmI/s1600/CocaColaERP.jpg)
*Coca Cola Revenue Breakdown (2014)*

Consider Vale, a commodity company, instead. Its revenue breakdown on 2014 is below, with a weighted equity risk premium of 7.39%  for the company.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxm3q-EIWjOpAGJLie9b3dGJ6_hBVwWF4xUMonZ9QtBaUZCQYS9Qg06bCbl-tkRbQuTdzpGTP1LDtcb8TYB96pN14WSGyuimCJdfaydO5HEbagB1Tao7HKfRu4jwB1GLYxNZUd5XHWL3k/s1600/ValeERP.jpg)
*Vale Revenue Breakdown (2014)*

As you can see, Vale is more exposed to Chinese country risk than Brazilian country risk, at least based on revenues. As a commodity company, you could argue that some of Vale's risks come from where its iron ore/mining reserves lie and that the equity risk premium should reflect that at as well. I agree, but Vale is still surprisingly opaque when it comes to the geographical breakdown of its operations.

**Bringing it together**

Since country risk can take many different forms and the way you should deal with it varies widely depending on that form, the picture below is designed to capture how best (at least from my perspective) to incorporate risk into value.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjxGEwGToG3lcQXiltxPSt8NJ062DL_bBmcp_V2hJB_q4D4v6ZkdXFKpMZvU_nqB0HH0T67Os0J5UMWRQ1VihWI1dqzA3yCuNAFM7vNDK6WfgJPptxsL70m2Fc2uOYzgr3DbBmUguFSic/s1600/risk+picture.jpg)

There are three keys to dealing with country risk.

- Look at country risk through the eyes of investors in your company: Many businesses, when looking at country risk, tend to look at how exposed they are to the risk, when they should be looking at risk exposure through the eyes of their investors. 

- Make your risk adjustment(s) transparent: Whatever adjustment you make for country risk, it should be transparent. Put differently, if you adjust discount rates for country risk, your country risk adjustment should be visible to others who may look at your valuation. In far too many valuations, the adjustments for country risk are implicit, thus making it impossible for others to understand the adjustments or take issue with them.

- Do not double count or triple count risk: In a surprisingly large number of valuations, risk is double counted. Thus, it is not uncommon to see government bond rates that are not risk free being used as risk free rates, multiple hair cuts to the same cash flows and the same risk being adjusted for in both the cash flows and discount rate.

One of the key requirements in operating a business globally is understanding how risk varies across countries and incorporating those risk assessments into whether and where you invest your (or your business) money. In these last two posts, I have tried to provide my perspective on both measuring risk differences across countries and how I think this risk should enter your investment decisions. It is true that both posts have avoided the questions of how the market prices these risks and of how currency risk enter the process, which you may view as glaring omissions, I will deal with the pricing question in my next post and look at decoding the currency puzzle in my last one.

**Papers to read**

- [My paper on country risk (July 2015)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2630871)

**Data attachments**

- [Equity Risk Premium by Country (July 2015) ](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJuly15.xls)

**Spreadsheets**

- [Company Risk Premium Calculator](http://www.stern.nyu.edu/~adamodar/pc/blog/wacc2015.xls)

**Posts on Country Risk**

- [Groundhog day in Greece, Hijinks in Brazil and Market Chaos in China: Pictures of Global Risk - Part 1](http://aswathdamodaran.blogspot.com/2015/07/groundhog-day-in-greece-hijinks-in.html)

- [Valuing Country Risk: Pictures of Global Risk - Part II](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html)

- [Pricing Country Risk: Pictures of Global Risk - Part III](http://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html)

- [Decoding Currency Risk: Pictures of Global Risk - Part IV](http://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html)
