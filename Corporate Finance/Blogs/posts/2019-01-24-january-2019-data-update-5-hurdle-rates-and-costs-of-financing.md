---
title: "January 2019 Data Update 5: Hurdle Rates and Costs of Financing"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-5-hurdle-rates.html
published: 2019-01-24
updated_source: 2019-02-27
fetched: 2026-08-27
tags:
  - Cost of capital
  - Cost of equity
  - Country Risk
  - Currency Risk
  - Hurdle Rates
---

# January 2019 Data Update 5: Hurdle Rates and Costs of Financing

_Source: [https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-5-hurdle-rates.html](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-5-hurdle-rates.html) — published 2019-01-24_

In the last post, I looked at how to measure risk from different perspectives, with the intent of bringing these risk measures into both corporate finance and valuation. In this post, I will close the circle by converting risk measures into hurdle rates, critical in corporate finance, since they drive whether companies should invest or not, and in valuation, because they determine the values of businesses. As with my other data posts, the focus will remain on what these hurdle rates look like for companies around the world at the start of 2019.

**A Quick Introduction**

The simplest way to introduce hurdle rates is to look at them from the perspectives of the capital providers to a business. Using a financial balance sheet as my construct, here is a big picture view of these costs:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSerRGQlnknijRrT9byCijFrfqT6r0EY0W-dvynbOs5lmj1nbl8iODh5s3kNhvCqbtFDXyGWHu20alptwa5jGCTBg6l52iKzMICre5a9_Oy0dBGZZj1tqlNLVRXL3_wt_F4zjhZyvCerA/s1600/FinBalSheetCostofCapital.png)

Thus. the hurdle rate for equity investors, *i.e., the cost of equity*, is the rate that they need to make, to break even, given the risk that they perceive in their equity investments. Lenders, on the other hand, incorporate their concerns about default risk into the interest rates they set on leans, i.e., *the cost of debt*. From the perspective of a business that raises funds from both equity investors and lenders, it is a weighted average of what equity investors need to make and what lenders demand as interest rates on borrowing, that represents the overall cost of funding, i.e.,* the cost of capital*.

I [have described the cost of capital](https://www.cfainstitute.org/research/multimedia/2015/the-cost-of-capital-the-most-misunderstood-misestimated-and-misused-number-in-finance) as the Swiss Army Knife of finance, used in many different contexts and with very different meanings. I have reproduced below the different uses in a picture:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUSl2df6ArqHWpS42v5tfFYTfEwa_yHgpVHipgbYw-_tKdAawSfMfZDXXDt05Xwf3ioabY_kOcSiR7aF3uVHVt9sCjoaXuRYeWv2rmB62f811QB4UZ4bfVZe1ViS2yZAmmbzt9RTsmutQ/s1600/CostofCapitalPicture.png)
[Paper on cost of capital](http://people.stern.nyu.edu/adamodar/pdfiles/papers/costofcapital.pdf)

It is precisely because the cost of capital is used in so many different places that it is also one of the most misunderstood and misused numbers in finance. The best way to reconcile the different perspectives is to remember that the cost of capital is ultimately determined by the risk of the enterprise raising the funding, and that all of the many risks that a firm faces have to find their way into it. I have always found it easiest to break the cost of capital into parts, and let each part convey a specific risk, since if I am careless, I end up missing or double counting risk. In this post, I will break the risks that a company faces into four groups: the business or businesses the company operates in (business risk), the geographies that it operates in (country risk), how much it has chosen to borrow (financial leverage risk) and the currencies its cash flows are in (currency effects). 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXTnMpmnkD6f_OpLg3C2Ode1vnXSfW_JJn9OSjt9vhAFcbT0GBRhMhVl9q1CnM8jaGShBG6-Jbd2LYvxapsy3J6bBma4DrjeWDpy2jzJ2vQ_i5PY1uBaiDnPdv2PCTj3JfSIptol3LXHw/s1600/Cost+of+capital+Risks.png)

Note that each part of the cost of capital has a key risk embedded in it. Thus, when valuing a company, in US dollars, in a safe business in a risky country, with very little financial leverage, you will see the 10-year US treasury bond rate as my risk free rate, a low beta (reflecting the safety of the business and low debt), but a high equity risk premium (reflecting the risk of the country).  The rest of this post will look at each of the outlined risks.

**I. Business Risk**

In [my last post](http://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-4-many-faces.html), where I updated risk measures across the world, I also looked at how these measures varied across different industries/businesses. In particular, I highlighted the ten most risky and safest industries, based upon both price variability and earnings variability, and noted the overlap between the two measures. I also looked at how the perceived risk in a business can change, depending upon investor diversification, and captured this effect with the correlation with the overall market.  If you are diversified, I argued that you would measure the risk in an investment with the covariance of that investment with the market, or in its standardized form, its beta.

To get the beta for a company, then, you can adopt one of two approaches.

- The first, and the one that is taught in every finance class, is to run a regression of returns on the stock against a market index and to use the regression beta. 

- The second, and my preferred approach, is to estimate a beta by looking at the business or businesses a company operates in, and taking a weighted average of the betas of companies in that business. 

To use the second approach, you need betas by business, and each year, I estimate these numbers by averaging the betas of publicly traded companies in each business. These betas, in addition to reflecting the risk of the business, also reflect the financial leverage of companies in that business (with more debt pushing up betas) and their holdings in cash and marketable securities (which, being close to risk less, push down betas). Consequently, I adjust the average beta for both variables to estimate what is called a pure play or a business beta for each business. (Rather than bore you with the mechanics,[please watch this video](https://youtu.be/rxmttgceSjg) on how I make these adjustments). The resulting estimates are shown [at this link, for US companies](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html). (You can also download the spreadsheets that contain the estimates for other parts of the world, as well as global averages, by going to the end of this post).

To get from these business betas to the beta of a company, you need to first identify what businesses the company operates in, and then how much value it derives from each of the businesses. The first part is usually simple to do, though you may face the challenge of finding the right bucket to put a business into, but the second part is usually difficult, because the individual businesses do not trade. You can use revenues or operating income by business as approximations to estimate weights or apply multiples to each of these variables (by looking at what other companies in the business trade at) to arrive at value weights. 

**II. Financial Leverage**

You can run a company, without ever using debt financing, or you can choose to borrow money to finance operations. In some cases, your lack of access to new equity may force you to borrow money and, in others, you may borrow money because you believe it will lower your cost of capital. In general, the choice of whether you use debt or equity remains one of the key parts of corporate finance, and I will discuss it in one of my upcoming data posts. In this post, though, I will just posit that your cost of capital can be affected by how much you borrow, unless you live in a world where there are no taxes, default risk or agency problems, in which case your cost of capital will remain unchanged as your funding mix changes.  If you do borrow money to fund some or a significant portion of your operations, there are three numbers that you need to estimate for your cost of capital:

- Debt Ratio: Th mix of debt and equity that you use represents the weights in your cost of capital.

- Beta Effect: As you borrow money, your equity will become riskier, because it is a residual claim, and having more interest expenses will make that claim more volatile. If you use beta as your measure of risk, this will require you to adjust upwards the business (or unlettered) beta that you obtained in the last part, using the debt to equity ratio of the company. 
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqVp1IP090gZonNL462IRYdVpdR3Z7Em2cBF2poq8JuYSb9Sks7uHIcDsIP1GzLLudQ1q0H7EmJPFAbUX9MpRwtqLf_Qdq0w3v1namsIh3TSjSal4SMvabj-k7EDHxcKJQp65Y8FtvU3M/s1600/LeveredBetaEquation.jpg)

- Cost of Debt: The cost of debt, which is set by lenders based upon how much default risk that they see in a company, will enter the cost of capital equation, with an added twist. To the extent that the tax law is tilted towards debt, the after-tax cost of borrowing will reflect that tax benefit. Since this cost of debt is a cost of borrowing money, long term and today, you cannot use a book interest rate or the interest rate on existing debt. Instead, you have to estimate a default spread for the company, based upon either its bond ratings or financial ratios, and add that spread on to the risk free rate:
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhgmW8wVvkFKeXm30bhXM5-pmm0SMqoHX_KMV8HNFqrVsus9URNLPKeZqlJTXcYfP7WNVrHXQDSntDCfpuxcA2IeVyc0DCImDhOQ84hGQoRj30UZNNF8jWckK01s7KYXglFDkx1MSRquU/s1600/+CostofDebt.jpg)

I look at the debt effect on the cost of capital in each of the industries that I follow, with all three effects incorporated in [this link, for US companies](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wacc.htm). The data, broken down, by other regional sub-groupings is available at the end of this post.

**III. Country Risk**

It strikes me as common sense that operating in some countries will expose you to more risk than operating in others, and that the cost of capital (hurdle rate) you use should reflect that additional risk. While there are some who are resistant to this proposition, making the argument that country risk can be diversified by having a global portfolio, that argument is undercut by rising correlations across markets. Consequently, the question becomes not whether you should incorporate country risk, but how best to do it. There are three broad choices:

- Sovereign Ratings and Default Spreads: The vast majority of countries have sovereign ratings, measuring their default risk, and since these ratings go with default spreads, there are many who use these default spreads as measures of country risk. 

- Sovereign CDS spreads: The Credit Default Swap (CDS) market is one where you can buy insurance against sovereign default, and it offers a market-based estimate of sovereign risk. While the coverage is less than what you get from sovereign ratings, the number of countries where you can obtain these spreads has increased over time to reach 71 in 2019. 

- Country Risk Premiums: I start with the default spreads, but I add a scaling factor to reflect the reality that equities are riskier than government bonds to come up with country risk premiums. The scaling factor that I use is obtained by dividing the volatility of an emerging market equity index by the volatility of emerging market bonds. 

To incorporate the country risk into my cost of capital calculations, I start with the implied equity risk premium that I estimated for the US (see my first data post for 2019) or 5.96% and add to it the country risk premium for each country. The full adjustment process is described in this picture:

I also bring in frontier markets, which have no sovereign ratings, using a country risk score estimated by Political Risk Services. The final estimates of equity risk premiums around the world can be seen in the picture below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeKsWoC2_CsgS8F6vjqNGcMobB_7_A9BXJOa4dz3TQuRyXWO1Z8jLywykJoLThzYMd1q1G9It-lA7KRaV-Ebtc7hM17rPOIO3h0uIiyIj7CCdGnY8Vrbqn0_1LJ6Hm-WvplAmnKdgAigs/s1600/ERP+computation+picture.png)

You can see these equity risk premiums as a list [by clicking here](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/ctryprem.html), or download [the entire spreadsheet here](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls). If you prefer a picture of equity risk around the world, my map is below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjB7wJIkL6NEvZKDhDQoMdV3GmOG7t2V7iElsoffGQlZpi9RIVXalcpS-x0PA7ICUqMTmlNlSQeLsxx5bm1wbQePnywS-DB39LlW1cQo4SwPK0PxQy3WhlSgcvh8oBgNr-GksynnPcr7pk/s1600/ERPMap2019.jpg)
[Download spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

I also report regional equity risk premiums, computed by taking GDP-weighted averages of the equity risk premiums of the countries int he region.

**IV. Currency Risk**

It is natural to mix up countries and currencies, when you do your analysis, because the countries with the most risk often have the most volatile currencies. That said, my suggestion is that you keep it simple, when it comes to currencies, recognizing that they are scaling or measurement variables rather than fundamental risk drivers. Put differently, you can choose to value a Brazilian companies in US dollars, but doing so does not make Brazilian country risk go away.

So, why do currencies matter? It is because each one has different expectations of inflation embedded in it, and when using a currency, you have to remain inflation-consistent. In other words, if you decide to do your analysis in a high inflation currency, your discount rate has to be higher, to incorporate the higher inflation, and so do your cash flows, for the same reason:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNpf4C1cWFKtvNnZZF3ZagW_lq8f-4Hrp2hQcCgutHo2UoMCaFbj9kMWQrqpfRkR4Hhtv-pkvwoCYf_3AMveKS4U-geiGxvQWBmZ2Qs52irlncmJpO99p989BwwqU1MYR9a0tuu-1b8Gc/s1600/CurrencyeffectsonDCF.png)

There are two ways in which you can bring inflation into discount rates.  The first is to use the risk free rate in that currency as your starting point for the calculation, since risk free rates will be higher for high inflation currencies. The challenge is finding a risk free investment in many emerging market currencies, since even the governments bonds, in those currencies, have default risk embedded in them. I attempt to overcome this problem by starting with the government bond but then netting the default spread for the government in question from that bond to arrive at risk free rates:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYj2DILvMoUAqtVK7vo3wqI_Nj0G8MgWM6sjiV3Y3Yp1wwu10IrcS7_SxfgKmqgWNOQih1giSvbxttzC1C_bzEPKONvssRznxKJb8OIYAl3fEJ3t4ff318LZiEr0ScEMBmJtjD-njB2yo/s1600/CurrencyRiskFreeGovtBond.jpg)
[Download raw data](http://www.stern.nyu.edu/~adamodar/pc/datasets/currencyriskfree2019.xls)

These rates are only as reliable as the government bond rates that you start with, and since more than two thirds of all currencies don't even have government bonds and even on those that do, the government bond rate does not come from liquid markets, there a second approach that you can use to adjust for currencies. In this approach, you estimate the cost of capital in a currency that you feel comfortable with (in terms of estimating risk free rates and risk premiums) and then add on or incorporate the differential inflation between that currency and the local currency that you want to convert the cost of capital to. Thus, to convert the cost of capital in US $ terms to a different currency, you would do the following:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBGK8q2tvQU6ixUIZAbAmzdbhg1ErYJTfa677FDvUuKZPeDTeQtDklDowY-JxNIgn0q8gMt2Atqq_LGtHvLt91pgYEGJv4NfMZdbvjEX-ozu3_R7v5oN5ikkk7Ia0suLBgRxrJC3mf4mo/s1600/CostofCapitalDifferential.jpg)

To illustrate, assume that you have a US dollar cost of capital of 12% for an Egyptian company and that the inflation rates are 15% and 2% in Egyptian Pounds and US dollars respectively:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimP6GhPh-qTP2CVQypn9AQAZ63e3vy6yOfsWIjVI94e8nWWCcJJVbPTS_DRqM4Z1zewiAsZP-n3Vj4QKoJXtoee3_gmW6HSAPLeYUwOn8PeHprsKERUC9BIQzChViApV6UGwaVkYNyEoI/s1600/EgyptianPound.jpg)

The Egyptian pound cost of capital is 26.27%. Note that there is an approximation that is often used, where the differential inflation is added to the US dollar cost of capital; in this case your answer would have been 25%. The key to this approach is getting estimates of expected inflation, and while every source will come with warts, you can find the [IMF's estimates of expected inflation in different currencies at this link](https://www.imf.org/external/datamapper/PCPIPCH@WEO/OEMDC/ADVEC/WEOWORLD).

**General Propositions**

Every company, small or large, has a hurdle rate, though the origins of the number are murky at most companies. The approach laid out in this post has implications for how hurdle rates get calculated and used.

- *A hurdle rate for an investment should be more a reflection the risk in the investment, and less your cost of raising funding: *I fault terminology for this, but most people, when asked what a cost of capital is, will respond with the answer that it is the cost of raising capital. In the context of its usage as a hurdle rate, that is not true. It is an opportunity cost, a rate of return that you (as a company or investor) can earn on other investments in the market of equivalent risk. That is why, when valuing a target firm in an acquisition, you should always use the risk characteristics of the target firm (its beta and debt capacity) to compute a cost of capital, rather than the cost of capital of the acquiring firm.

- *A company-wide hurdle rate can be misleading and dangerous: *In corporate finance, the hurdle rate becomes the number to beat, when you do investment analysis. A project that earns more than the hurdle rate becomes an acceptable one, whether you use cash flows (and compute a positive net present value) or income (and generate a return greater than the hurdle rate). Most companies claim to have a corporate hurdle rate, a number that all projects that are assessed within the company get measured against. If your company operates in only one business and one country, this may work, but to the extent that companies operate in many businesses across multiple countries, you can already see that there can be no one hurdle rate. Even if you use only one currency in analysis, your cost of capital will be a function of which business a project is in, and what country it is aimed at. The consequences of not making these differential adjustments will be that your safe businesses will end up subsidizing your risky businesses, and over time, both will be hurt, in what I term the "curse of the lazy conglomerate".

- *Currency is a choice, but once chosen, should not change the outcome of your analysis: *We spend far too much time, in my view, debating what currency to do an analysis in, and too little time working through the implications. If you follow the consistency rule on currency, incorporating inflation into both cash flows and discount rates, your analyses should be currency neutral. In other words, a project that looks like it is a bad project, when the analysis is done in US dollar terms, cannot become a good project, just because you decide to do the analysis in Indian rupees. I know that, in practice, you do get divergent answers with different currencies, but when you do, it is because there are inflation inconsistencies in your assessments of discount rates and cash flows.

- *You cannot (and should not) insulate your cost of capital from market forces: *In both corporate finance and investing, there are many who remain wary of financial markets and their capacity to be irrational and volatile. Consequently, they try to generate hurdle rates that are unaffected by market movements, a futile and dangerous exercise, because we have to be price takers on at least some of the inputs into hurdle rates. Take the risk free rate, for instance. For the last decade, there are many analysts who have replaced the actual risk free rate (US 10-year T.Bond rate, for instance) with a "normalized' higher number, using the logic that interest rates are too low and will go up. Holding all else constant, this will push up hurdle rates and make it less likely that you will invest (either as an investor or as a company), but to what end? That uninvested money cannot be invested at the normalized rate, since it is fictional and exists only in the minds of those who created it, but is invested instead at the "too low" rate. 

- *Have perspective*: In conjunction with the prior point, there seems to be a view in some companies and for some investors, that they can use whatever number they feel comfortable with as hurdle rates. To the extent that hurdle rates are opportunity costs in the market, this is not true. The cost of capital brings together all of the risks that we have listed in this section. If nothing else, to get perspective on what comprises high or low, when it comes to cost of capital, I have computed a histogram of global and US company costs of capital, in US $ terms.
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSSUNyGumwKcWo6rmWwlhddtrTifNbOU30YLj_AHO_KlBv3AX2ZDGvxtGrxfcM4e38G0zXH84egb4TjuzuMjnUJgnMNW-Jgf21CGTE4EF1WtoCodmrUDkkNuTPGVdNqY2KrkZOKfhfxUE/s1600/WACCdistn.jpg)

You can convert this table into any currency you want. The bottom line is that, at least at the start of 2019, a dollar cost of capital of 14% or 15% is an extremely high number for any publicly traded company. You can see the costs of capital, in dollar terms, for US companies [at this link](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wacc.htm), and as with betas, you can download the cost of capital, by industry, for other parts of the world in the data links below this post.

In short, if you work at a company, and you are given a hurdle rate to use, it behooves you to ask questions about its origins and logic. Often, you will find that no one really seems to know and/or the logic is questionable.

**YouTube Video**

**Data Sets**

- Betas by Business: [US](http://www.stern.nyu.edu/~adamodar/pc/datasets/betas.xls), [Global](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls), [Emerging Markets](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaemerg.xls), [Europe](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaEurope.xls), [Japan](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaJapan.xls), [India](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaIndia.xls), [China](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaChina.xls), [Aus & Canada](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaRest.xls)

- [Sovereign Ratings and CDS Spreads by Country in January 2019](http://www.stern.nyu.edu/~adamodar/pc/blog/ctrydefault2019.xlsx)

- [Equity Risk Premiums by Country in January 2019](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

- [Risk free Rates by Currency: Government bond based](http://www.stern.nyu.edu/~adamodar/New_Home_Page/currencyriskfree2019.xls)

- Cost of Capital in US $ (with conversion equation for other currencies): [US](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls), [Global](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls), [Emerging Markets](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccemerg.xls), [Europe](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccEurope.xls), [Japan](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccJapan.xls), [India](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccIndia.xls), [China](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccChina.xls), [Aus & Canada](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccRest.xls)

**January 2019 Data Updates**

- [Data Update 1: A Reminder that equities are risky, in case you forgot!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-1-reminder.html)

- [Data Update 2: The Message from Bond Markets](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-2-message-from.html)

- [Data Update 3: Playing the Numbers Game](https://aswathdamodaran.blogspot.com/2019/01/january-2018-data-update-3-playing.html)

- [Data Update 4: The Many Faces of Risk](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-4-many-faces.html)

- [Data Update 5: Of Hurdle Rates and Funding Costs!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-5-hurdle-rates.html)

- [Data Update 6: Profitability and Value Creation!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-6.html)

- [Data Update 7: Debt, neither poison nor nectar!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-7-debt-neither.html)

- [Data Update 8: Dividends and Buybacks - Fact and Fiction!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-8-dividends.html)

- [Data Update 9: Playing the Pricing Game!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-9-pricing-game.html)
