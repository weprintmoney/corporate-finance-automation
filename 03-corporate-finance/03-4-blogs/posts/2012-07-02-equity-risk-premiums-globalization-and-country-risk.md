---
title: "Equity Risk Premiums: Globalization and Country risk"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2012/07/equity-risk-premiums-globalization-and.html
published: 2012-07-02
updated_source: 2012-07-25
fetched: 2026-08-27
tags:
  - Equity Risk Premiums
---

# Equity Risk Premiums: Globalization and Country risk

_Source: [https://aswathdamodaran.blogspot.com/2012/07/equity-risk-premiums-globalization-and.html](https://aswathdamodaran.blogspot.com/2012/07/equity-risk-premiums-globalization-and.html) — published 2012-07-02_

The equity risk premium reflects what investors expect to earn on equities, as a class, over and above the risk free rate. Implicit in that definition are two key points. The first is that the equity risk premium is a macro number that applies to all stocks. The second is that the equity risk premium is the receptacle, in intrinsic valuation, for all macro economic fears. In fact, I used the equity risk premium as my vehicle for talking about how economic crises (the US rating downgrade of last summer, the Greece default dance…)

On my [web site](http://www.damodaran.com/), I update the equity risk premium for the S&P 500 every month, with my [latest update of 6.17%](http://www.stern.nyu.edu/~adamodar/pc/implprem/ERPJune12.xls) on June 29, 2012. Even if you accept that estimate as a reasonable one for the US, there are many other estimation challenges. If you are valuing a Brazilian company, what equity risk premium would you use? What if you are valuing a multinational like Siemens or GE, with significant revenues in emerging markets, or an oil company with substantial reserves in Nigeria? More generally, in the face of globalization, valuing any company now requires an understanding of how best to evaluate country risk and convert into appropriate equity risk premiums. If you are working for a multinational, understanding how equity risk varies across countries is central to coming up with hurdle rates that vary across countries and lead to a fairer allocation of capital.

***Should equity risk premiums vary across countries? ***

The question of whether equity risk premiums should be different for different countries, at first sight, looks like it has an obvious answer. Of course! After all, Venezuela, Russia and Greece are riskier countries to invest in than Switzerland, Germany or Canada and should have higher equity risk premiums. The answer, though, is not that simple. There are two scenarios where country risk will cease to matter and you will use the same equity risk premium for all companies, no matter which country they operate in. The first is if country risk is idiosyncratic, i.e., specific only to that country, with no spill over effects. If this is the case, diversifying geographically across countries should make this risk disappear in your portfolio, which can be accomplished by companies expanding their reaches across the globe (think Coca Cola or Nestle), or easier still, by investors holding geographically diversified portfolios. The second is to assume that all investors invest in global portfolios, in which case you could compute a global equity risk premium, capturing macro economic risks around the world, and estimate betas for individual companies against a global equity index.

Both assumptions are difficult to sustain. The assumption that country risk is diversifiable is built on the presumption that the correlation across countries is low and that there is no contagion effect. That may have been true in the 1980s but as investors and countries have globalized, the [correlation across countries has risen](http://www.lazardnet.com/lam/us/pdfs/Investment_Research/2011/CountryAndSectorContagionInTheEmerging_LazardInvestmentResearch.pdf). Put differently, country risk is no longer diversifiable and requires a risk premium to those exposed to it. The assumption that investors are global is more reachable now than two decades ago, but institutional restrictions (Indian and Chinese investors still cannot invest easily overseas) and investor behavior (there is a [substantial home bias](http://en.wikipedia.org/wiki/Equity_home_bias_puzzle) in portfolios, where investors over invest in their domestic markets) still stand in the way.

Bottom line: I think that equity risk premiums do vary across countries, with higher equity risk premiums applying to riskier countries. Applying the same equity risk premiums across companies will lead you to over value companies that have higher exposure to emerging markets.

***How do you estimate equity risk premiums for different markets? ***

If you accept the premise that equity risk premiums should be different for different market, the question of how best to estimate these premiums follows. You cannot obtain these premiums using historical data, i.e., by looking at the premiums earned by stocks over riskless investments within each of the markets. Why not? First, there may be no riskless investments in many of these markets, either because governments may have default risk or because government bonds were not issued/traded over the period. Second, these markets are changing so much over the historical period in question that the historical premium you get over the period is not a predicted premium. Third, and more important, equity markets are volatile and the equity risk premiums over 20,30 or even 50 years of data have estimation errors that drown out the estimate.

Here are three alternatives that can be used to estimate the equity risk premiums for other markets:

*A. Country default spreads: *The simplest approach is to start with a mature market premium (say, 6% for the US), and then augment it by adding a country default spread for the country in question. That default spread can be estimated in one of three ways:

- Government bonds in US$/ Euros: If the country in question has dollar or Euro denominated bonds, you can estimate the spread over the US treasury bond or the German ten-year bond rate respectively. 

- Sovereign rating: Moody’s, S&P and Fitch all assign sovereign ratings to countries. You can estimate a typical default spread, based on the sovereign rating, using a lookup table that I update at the start of each year. Using Peru as an example, the sovereign rating of Baa3 for the country yields a default spread of 2.00%. Here are the [latest local currency and foreign currency sovereign ratings](http://www.stern.nyu.edu/~adamodar/pc/blog/sovratings12.xls) from Moody's.

- CDS spreads: The Credit Default Swap market is of more recent origin, but it is a market that allows you to buy insurance against default risk ([see my earlier post on this market](http://aswathdamodaran.blogspot.com/2010/02/credit-default-swap-cds-market.html)). Thus, if you bought a 10-year Peruvian government bond with an interest rate of 4.5%, and were concerned about default, you could have bought a 10-year Peruvian CDS. The price of that CDS in June 2012 was 2.06%, effectively implying that you would need to pay 2.06% out of your 4.5% each year for the next 10 years to get default protection. If you are interested, here are the [ten-year CDS spreads for all of the countries where they are offered as of June 30, 2012](http://www.stern.nyu.edu/~adamodar/pc/blog/CDSspreads12.xls). 

B. Relative Equity Market Volatility: In this approach, you can scale up the equity risk premium for the US by the relative volatility of the country in question, with relative volatility computed as the ratio of the volatility of that market to the volatility in the S&P 500. Thus, if standard deviation of Peruvian equities is 21%, the standard deviation for the S&P 500 is 15% and the equity risk premium in the S&P 500 is 6%, the equity risk premium for Peru will be

Equity Risk premium for Peru = 6% (21%/15%) = 8.4%

Country Risk premium for Peru = 8.4% -6% = 2.4%

While this approach has intuitive appeal, its weakness is that the equity market volatilities are as much a function of country risk as they are a measure of liquidity, with less liquid markets (which are often the most risky) having higher standard deviations. Here are [my estimates for emerging markets as of January 2012](http://www.stern.nyu.edu/~adamodar/pc/blog/ERPRelEqVol.xls).

C. Scaled Default Spread: In this approach, you combine the first two, by starting with the country default spread in approach 1 and then scaling it for relative volatility, but this time of the equity index in the country to the volatility of the government bond in that country. Again, using Peru as the example, assume that the standard deviation in the Peruvian government bond is 14% and that the standard deviation in Peruvian equities stays at 21%:

Default spread for Peru = 2.00% (using the rating)

Country risk premium for Peru = 2.00% (21%/14%) = 3.00%

Total equity risk premium for Peru = 9.00%

By staying within the same market for both volatilities, this approach is less susceptible than the prior one to liquidity variations across markets. The standard deviations can be noisy or difficult to estimate and I prefer to use a median value for the ratio across markets, rather than the ratio for any given market. (See [my January 2012 update of equity to government bond volatilities](http://www.stern.nyu.edu/~adamodar/pc/blog/RelVol12.xls).)

There is one other approach, where you are not dependent upon knowing the mature market premium, historical volatilities or default spreads. You can compute an implied premium for an emerging market, based upon the level of equity prices and expected cash flows. While this is what I do for the S&P 500 each month to get the implied premium for the US, it is far more difficult to use in emerging markets, because of data limitations.

***Where do you use this equity risk premium?***

Equity risk premiums come into play at every step in investing. At the asset allocation stage, where you determine how much of your portfolio you will be allocating to different asset classes (equity, fixed income, real assets) and to different geographical areas, you have to make judgements of which markets you are getting the best risk/return trade off and allocate more money to those markets.

Once you have made your asset allocation judgments, equity risk premiums come into play, when you value individual companies. In intrinsic or discounted cash flow valuation, you need the equity risk premium to get to a cost of equity and capital. The common approach, among many practitioners, is to attach an equity risk premium to a company, based upon its county of incorporation. Thus, when valuing Peruvian companies, you would use 9.00% as your equity risk premium, thus pushing up your cost of equity/capital and pushing down value, and when valuing US companies, you would use the 6% (mature market premium). I would suggest a more nuanced approach (which will take a little more work): compute an equity risk premium for a company that reflects a weighted average of the countries it operates in, with the weights being based upon an observable variable (revenues seem to work best). Thus, if you are valuing a company with 30% of its revenues in Peru (ERP =9%), 30% of its revenues in Venezuela (ERP =12%) and 40% of it revenues in the US (ERP =6%), you would use the following:

Weighted average equity risk premium = .30 (9%) + .30 (12%) + .40 (6%) = 8.7%

If the company breaks down revenues into regions rather than counties, you may have to compute a premium by region (Latin America, South Asia, Eastern Europe, Sub-Saharan Africa etc.) and take a weighted average.

In relative valuation, the use of country risk is usually implicit or qualitative. Thus, when comparing the PE ratios for oil companies, you may choose not to buy Lukoil, even though it trades at a lower PE than Conoci, because you worry about Russian country risk. If you want to be more explicit about how much to adjust multiples for country risk, [download my spreadsheet for computing intrinsic multiples](http://www.stern.nyu.edu/~adamodar/pc/blog/growthbreakdown.xls) and change the equity risk premium to see how much PE or EV/EBITDA multiples change as the equity risk premium changes.

***My latest update ***

I update country risk premiums, by country and region, at the start of every year. Given the turmoil of the last six months, and dramatic changes in country risk (especially in Europe), I have updated the numbers as of **June 30, 2012**. You can get the [latest version of my estimates of country risk premiums](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctrypremJune2012.xls) by clicking here. If you want a blow-by-blow account of my reasoning on equity risk premiums, you can be a glutton for punishment and [download my paper on equity equity risk premiums](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2027211) (the 2012 version).
