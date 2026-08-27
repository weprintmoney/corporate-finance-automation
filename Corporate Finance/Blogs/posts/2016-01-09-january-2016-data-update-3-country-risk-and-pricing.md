---
title: "January 2016 Data Update 3: Country Risk and Pricing"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-3-country-risk.html
published: 2016-01-09
updated_source: 2016-02-01
fetched: 2026-08-27
tags:
  - Country Risk
  - Data Update
---

# January 2016 Data Update 3: Country Risk and Pricing

_Source: [https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-3-country-risk.html](https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-3-country-risk.html) — published 2016-01-09_

I had a long [ post on country risk](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html) in July 2015, as part of series of posts on the topic. At the time of the post, the Chinese market was in the midst of a meltdown, emerging markets were in turmoil and exchange rates were on the move. It is six months later, and nothing seems to have changed, but I think that the core lesson is worth reemphasizing. In a world of multinational businesses and global investors, there is no place to hide from country risk. 

**Country Risk Measurement**

I will not bore you by repeating much of what I said in my earlier post on how I view country risk in valuation, but it is built on two presumptions. First, *a company's risk exposure is based on where it does business, not where it is incorporated or headquartered*. Thus, Coca Cola and Nestle may be incorporated in developed markets (US and Switzerland) but derive a significant portion of their revenues from emerging markets and are thus exposed to risk in those markets. By the same token, Embraer is a Brazilian company that derives a substantial portion of its revenues in developed markets. Second, *the risk of investing in equities varies across the world, resulting in higher equity risk premiums in some markets than others*.  To estimate these risk premiums, I follow a four-step process:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-Tx9cRIhAlMYVOlJjofhIvzsd2eL3YPepI1XKpdQke24y60CkBlwhcDLpds1amNmY3XAXoq3cAkvl3Vpfoge-eUIcABvxUXKXQmARp1WwbxQUMiYo5sXPwp2f1AsNtB07ujJJy8gpLAA/s1600/ERP+computation+picture.jpg)
[My paper on equity risk premiums](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2581517)

As an example, let's assume that I want to estimate the equity risk premium for operating in India in January 2016. 

- I start with the [implied equity risk premium for the S&P in January 2016](http://www.stern.nyu.edu/~adamodar/pc/implprem/ERPJan16.xls), which I [estimated to be 6.12% in my first data post](http://aswathdamodaran.blogspot.ae/2016/01/january-2016-data-update-1-us-equity.html) a few days ago. I use a rounded down estimate of 6% as my mature market premium for the start of 2016.

- As a second step, I look up the [local currency sovereign rating for India from Moody's](https://www.moodys.com/research/Sovereign-Supranational-Rating-List--PBC_186519) and arrive at a Baa3 rating; the typical default spread for a Baa3 rated country at the start of 2016 was 2.44%.  I check this estimate against the sovereign CDS spread for India, which was 2.11% on January 1, 2016. I use the ratings-based spread of 2.44% as the default spread for India, though I would not raise too much of a fight, if you insisted on using the CDS spread.

- In the third step, I try to estimate how much riskier equities are than government bonds in emerging markets by using proxies for each one: the [S&P Emerging BMI Index](http://us.spindices.com/indices/equity/sp-emerging-bmi-us-dollar) (an index of emerging market equities) for stocks, and the [S&P Emerging Market Public (government and quasi government) bond index yield](https://research.stlouisfed.org/fred2/series/BAMLEMPUPUBSLCRPIUSEY). The standard deviation in the former is 17.36% and the coefficient of variation in the latter is 12.91% and the ratio of the former to the latter is 1.34. Multiplying this ratio by the default spread in step 2 yields a country risk premium for India of 3.28%. (CRP for India = 2.44% * 1.34 = 3.28%)

- In the fourth step, I add the country risk premium to the implied premium of 6% that I estimated in step 1 to arrive at an equity risk premium for India of 9.28%.

Is this number an estimate? Of course! Would you get a different number if you used the CDS spread as your measure of default risk and different indices for emerging market equities and bonds? The answer is yes. It is for this reason that the [spreadsheet that I create for equity risk premiums](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls) allows you to replace my defaults with yours for any or all of these variables. Before you exhaust yourself in this effort, I would suggest that small differences in this number will not make or break your valuation. So, make your best estimates and move on!

**Country Risk Update - January 2016**

Using the approach described for India, I compute equity risk premiums for the 130 countries with a Moody's sovereign rating. For about fourteen more, with no Moody's rating for the country, I was able to find a sovereign rating on S&P that I convert to a Moody's rating and estimate an ERP. Finally, there are about 20 countries, loosely categorized as frontier markets, for which there is no rating or CDS spread; these include the hot spots of the world such as Syria and Iraq. For these, I use the only measure of country risk that I can find, a composite risk score from [Political Risk Services (PRS)](https://www.prsgroup.com/) and use that score to compute an equity risk premium; I create a look up table using the countries that have both PRS scores and ERP to make these judgments. Desperation move? Perhaps, but if you can find a better way of doing it, I would be glad to follow your lead. The resulting equity risk premiums by country are available in the spreadsheet that I referenced earlier but are also in the map below (which adds nothing in terms of content but looks much better):

via [chartsbin.com](http://chartsbin.com/view/38643)

**
**

**Country Pricing Update - January 2016**

In my July 2016 updates, I also included [one on how stocks are priced around the world](http://aswathdamodaran.blogspot.ae/2015/07/pricing-country-risk-pictures-of-global.html), using multiples (PE, PBV, EV/Sales, EV/EBITDA, EV/Invested Capital). While that post has a more extensive explanation of why stocks should trade at different multiples around the world, I have updated the multiples, by country, in this spreadsheet. As you peruse these numbers, keep in mind that the number of companies that I have in data set is very small for some countries and the multiples can therefore yield strange values. To prevent outliers from hijacking my estimation, I also compute the multiple using aggregated values; thus, the PE ratio for China is computed by adding the market capitalizations of all companies listed in the market and dividing by the aggregated net income of these companies. 

via [chartsbin.com](http://chartsbin.com/view/38644)

Much as I would like to read more into this picture (especially about cheap and expensive markets), these country numbers are more a first step in the investment process than a last one. 

**Bottom line**

I think that we are far too casual in our treatment of country risk, estimating equity risk premiums on auto pilot for countries and attaching these premiums to companies based on where they are incorporated, rather than where they do business. If there is a lesson from the last week's implosion in the Chinese market, it is that the emerging market growth story that so many developed market companies have pushed for the last two decades has a dark side, and that dark side takes the form of higher risk. It is easy to forget this intuitive concept in the good times, but the market lulls us into complacency before shocking us. 

**Datasets**

- [Equity Risk Premiums - By Country](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

- [Pricing Multiples - By Country](http://www.stern.nyu.edu/~adamodar/pc/datasets/countrystats.xls)

**Data Update Posts**

- [January 2016 Data Update 1: The US Equity Market](http://bit.ly/1OGnaBk) 

- [January 2016 Data Update 2: Interest Rates and Exchange Rates - Currencies ](http://bit.ly/1MXaVPA)

- [January 2016 Data Update 3: Country Risk and Pricing](http://bit.ly/1ZiZ5f3)

- [January 2016 Data Update 4: Costs of Equity and Capital](http://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-4-costs-of.html)

- [January 2016 Data Update 5: Investment Returns and Profitability](http://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-5-making-case.html)

- [January 2016 Data Update 6: Capital Structure](http://bit.ly/1S6mUmB)

- [January 2016 Data Update 7: Dividend Policy](http://bit.ly/20tbSZD)

- [January 2016  Data Update 8: Pricing, with an end of month update](http://bit.ly/202Jco9)

**Past Blog Posts on Interest Rates and Currencies**

- [Valuing Country Risk - Pictures of Global Risk](http://aswathdamodaran.blogspot.ae/2015/07/valuing-country-risk-pictures-of-global.html)

- [Pricing Country Risk - Pictures of Global Risk](http://aswathdamodaran.blogspot.ae/2015/07/pricing-country-risk-pictures-of-global.html)
