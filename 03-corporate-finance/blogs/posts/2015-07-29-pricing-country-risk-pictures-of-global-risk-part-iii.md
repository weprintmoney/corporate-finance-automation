---
title: "Pricing Country Risk - Pictures of Global Risk - Part III"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html
published: 2015-07-29
updated_source: 2015-08-08
fetched: 2026-08-27
tags:
  - Country Risk
  - Equity Risk Premiums
---

# Pricing Country Risk - Pictures of Global Risk - Part III

_Source: [https://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html](https://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html) — published 2015-07-29_

0
0
1
51
297
Stern School of Business
2
1
347
14.0

Normal
0

false
false
false

EN-US
JA
X-NONE

/* Style Definitions */
table.MsoNormalTable
{mso-style-name:"Table Normal";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-parent:"";
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-para-margin-top:0in;
mso-para-margin-right:0in;
mso-para-margin-bottom:10.0pt;
mso-para-margin-left:0in;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Cambria;
mso-ascii-font-family:Cambria;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Cambria;
mso-hansi-theme-font:minor-latin;
mso-fareast-language:JA;}

In my last two posts, I looked at country risk, starting with an [examination of measures of country risk in this one](http://aswathdamodaran.blogspot.com/2015/07/groundhog-day-in-greece-hijinks-in.html) and how to incorporate that risk into value [in the following post](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html). In this post, I want to look at an alternative way of dealing with country risk, especially in investing, which is to let the market price of country risk govern decisions.

**Pricing Country Risk**

If you are not a believer in discounted cash flow valuations, I understand, but you still have to consider differences in country risk in your investing strategies. If you use pricing multiples (PE, Price to Book, EV to EBITDA) to determine how much you will pay for companies, you could assume that the levels of these multiples in a country already incorporate country risk. Thus, you are assuming that the PE ratios (or any other multiple) will be lower in riskier countries than in safer ones. 

It is easy to illustrate the impact of risk on any pricing multiple, with a basic discounted cash flow model and simple algebra. To illustrate, note that you can use a stable growth dividend discount model to back into an intrinsic PE:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZc-r0ypPJWl-4bmwu0eF3hcYasyzl_6WZrCE2mt6Hwibmb4H3jEyfgN1L9R352EzDeICbeT0G8lpOM6C_dSsWGElMFK87Dw9t2gs95_PiPUZFrd8Ol8SHlYEQCp1U6E6Oz3ldPvHHEZY/s1600/DDMequation.jpg)

Dividing both sides of this equation by earnings, we derive an intrinsic PE ratio:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmmYnJgw6AeSh9h0ubka9_t6hBoeBPT4Kls8LppgN_AaH1GabdtS56UPd2cSzFsh9OVhyjZB3S6m8BdwH3YV8Fl4njqYm1jBst4HGX4CUsYZUIK06-XzemkMK8JNRHuBvR_2QplNTVHtM/s1600/PEequation.jpg)

The PE ratio that you should expect to observe in a country will be a function of the efficiency with which firms generate earnings (measured by the payout ratio), the expected growth in these earnings (g) and the risk in these earnings (captured by the cost of equity). Holding the growth and earnings efficiency constant, then, you should expect to see lower PE ratios in countries with higher risk and higher PE ratios in safer countries. You can use the same process to extract the determinants of price to book ratios or enterprise value multiples and you will arrive at the same conclusion.

**Equity Multiples**

To see how well this pricing paradigm works, I started by looking at PE ratios by country in July 2015. To estimate the PE ratio for a country, I tried three variants. In the first, I compute the PE ratio for each company in the country (where it was computable) and then average across these PE ratios. To the extent that there are small companies with outlandish PE ratios in the sample (and there are many), these ratios will be skewed upwards. In the second, I compute a weighted average PE ratio across companies, with the weights based upon net income. This ratio is less affected by outliers, but it excludes money losing firms (since the PE ratio is not meaningful for these companies). In the third, I add up the market values of equity across all companies in the market and divide by aggregated net income for all companies, including money losing companies, i.e., an aggregated PE ratio. This ratio has the advantage of including all listed firms in a market but big money losing firms will push this measure up. The picture below summarizes differences in PE ratios across the world, with the weighted average PE ratio as the primary measure, but with the all three reported for each country.

via [chartsbin.com](http://chartsbin.com/view/35620)

As you can see PE ratios are noisy, with some very risky countries (like  Venezuela) trading at high PE ratios and safe countries at lower values, not surprising given how much earnings can shift from year to year. For the most part, the riskiest countries are the ones where stocks trade at the lowest multiple of earnings.

To get a more stable measure of pricing, I computed price to book values by country, again using the simple and weighted averages across companies and aggregated values and report the weighted average Price to Book in the picture below:

via [chartsbin.com](http://chartsbin.com/view/35622)

As with PE ratios, there are outliers and Venezuela still stands out with an absurdly high price to book ratio, incongruous given the risk in that country. For the most part, though, the PBV ratio is correlated with country risk, as you can see in this list of the 28 countries that have price to book ratios that are less than one in July 2015:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQNuPwHv4cCaWClJf5Ovd3Bz0YaoSrpvVTdMguKozrkUT6GAUgWBmvLarkGR_mSsDMkb3TNQuRJLN0UuwCOii64axl8oR_UMHSWBqSPMc5gGAasRSlx5Ss_7UNIhOV9q00HBq1frMl8kc/s1600/lowestPBVcountries.jpg)
*Weighted average PBV ratio in July 2015*

**Enterprise Value Multiples**

Both PE and PBV ratios are equity multiples and may reflect not just country risk but also variations in financial leverage across countries. To remedy this problem, I look at EV to EBITDA multiples across countries:

via [chartsbin.com](http://chartsbin.com/view/35624)

Looking at this map, it is quite clear that there is much less correlation between EV/EBITDA multiples and country risk than there is with the equity multiples. While it is true that the lowest EV/EBITDA multiples are found in the riskiest parts of the world (Russia & Eastern Europe, parts of Latin America and Africa), the highest EV/EBITDA multiples are in India and China. 

There are two ways of looking at these results. The optimistic take is that if you have to pick a multiple to use compare companies that are listed in different markets, you should use an enterprise value multiple, since it is less affected by country risk. The pessimistic take is that you are likely to over value emerging market companies, if you use EV/EBITDA multiples, since they are less likely to incorporate country risk.

**Using these multiples **

The standard approach to pricing a company is to choose a multiple and compare how stocks that you deem “comparable” are being priced based on that multiple. This approach can be extended to deal with country risk, albeit with some limitations, in one of four ways: 

- *Compare how stocks listed in a country are priced to find “bargains”:* You could compare PE ratios across Brazilian companies on the assumption that Brazilian country risk is already incorporated in the pricing and buy (sell) the lowest (highest) PE stocks. The danger with this approach is that you are assuming that all Brazilian companies are equally exposed to Brazilian country risk. 

- *Compare how stocks within a sector in a country are priced:* Rather than compare across all stocks in a market, you could compare stocks within a sector in that market, on the assumption that both country and sector risk are already in the prices. Thus, you could compare the EV/Sales ratios of Brazilian retailers and argue that the retailers that trade at the lowest multiples of revenues are cheapest. The downside is that you may not find enough companies in a country, especially in a smaller market. 

- *Compare how stocks within a sector are priced globally*: A logical outgrowth of globalization is to compare companies within a sector, even if they are listed in different countries. Thus, you could compare Vale to other mining companies listed globally and Coca Cola to beverage companies across countries. The benefit is that you have more comparable firms but the danger is that you are ignoring country risk. 

- *Compare stocks within a sector are priced globally, but control for country risk*: In this last approach, you look at the pricing of companies across a sector but try to control for country risk by looking at differences between how the market is pricing companies in developed markets and emerging markets. 

No matter which approach you use, you have the pluses and minuses of pricing. The plus is that you will always be able to find "cheap" stocks, because you are making relative judgments and it is simple to get the data. The minus is that if stocks are collectively over priced, either at a country or sector level, a pricing comparison will just yield the least over priced stock in the country or sector.

**Valuing and Pricing: Final Thoughts**

In [my last post](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html), I looked at ways in which you can try to incorporate country risk into the values of companies. In this one, I looked at how price these companies, based upon how the market is pricing other companies in risky countries. As I have argued in my posts on price versus value, the two approaches can yield divergent numbers and conclusions. Thus, you could value a company with all its operations in China, using an appropriate equity risk premium for China, and conclude that the stock is over valued. You could then compare the PE ratio for the same company to the PE ratio for the Chinese market and decide that it is cheap, because it trades at a lower multiple of earnings than a typical Chinese company.

I tend to go with the first approach, since I have more faith in my valuation abilities than in my pricing abilities, i.e., I am more investor than trader. However, I am not quick to dismiss those who use pricing metrics to pick investments, since a nimble trader can play the pricing game very profitably. If you are unsure about where you fall in this process, I would suggest that you both value and price companies and buy only when both signal that the stock is a bargain.

**Papers to read**

- [My paper on country risk (July 2015)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2630871)

**Data attachments**

- [Equity and EV Multiples by Country: July 2015](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryMultiplesJuly2015.xls)

**Posts on Country Risk**

- [Groundhog day in Greece, Hijinks in Brazil and Market Chaos in China: Pictures of Global Risk - Part 1](http://aswathdamodaran.blogspot.com/2015/07/groundhog-day-in-greece-hijinks-in.html)

- [Valuing Country Risk: Pictures of Global Risk - Part II](http://aswathdamodaran.blogspot.com/2015/07/valuing-country-risk-pictures-of-global.html)

- [Pricing Country Risk: Pictures of Global Risk - Part III](http://aswathdamodaran.blogspot.com/2015/07/pricing-country-risk-pictures-of-global.html)

- [Decoding Currency Risk: Pictures of Global Risk - Part IV](http://aswathdamodaran.blogspot.com/2015/07/decoding-currency-risk-pictures-of.html)
