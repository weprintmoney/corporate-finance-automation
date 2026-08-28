---
title: "January 2016 Data Update 4: The Costs of  Capital"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-4-costs-of.html
published: 2016-01-13
updated_source: 2016-02-01
fetched: 2026-08-27
tags:
  - Cost of capital
  - Cost of equity
  - Data Update
---

# January 2016 Data Update 4: The Costs of  Capital

_Source: [https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-4-costs-of.html](https://aswathdamodaran.blogspot.com/2016/01/january-2016-data-update-4-costs-of.html) — published 2016-01-13_

In this post, the fourth in my data update series, I turn my focus to the cost of capital. While the discussion of cost of capital is often obscured by debates about risk and return models, it is a number central to much of what we do in corporate finance and valuation, and it predates modern portfolio theory. You cannot run a business without a sense of what you need to make on your investments to break even and you cannot value a business without a measure of your opportunity cost. 

**The Swiss Army Knife of Finance**

I teach two classes, corporate finance and valuation, and I wear different hats, when looking at the same questions. In corporate finance, my focus is on how to run a business, using fundamental financial principles, and in valuation, I shift my attention to how value that business, using the same principles. Like Waldo, the cost of capital is a constant part of both classes, playing a key role in almost every discussion.

In the corporate finance class, it shows up in each of the three big questions that every business has to answer. It helps you answer the first one, on where you should direct your investments, by suppling your business with a hurdle rate or rates for investments, with riskier investments having to meet a higher threshold, to be acceptable.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwloBE5KCCYm3faaEzZkj_sH3YMtnNyJLT71_02OzsePlfhaihtSoeJbhCkXIc9VD7zyUi9dVpGRi0KErkkwej7sckXEpHuV-dQyMhZBJi67zp2VrJeBoR_Sx-DcWIaDifSI3Ik_lZ748/s1600/Cost+of+capital+as+hurdle+rate.png)

In capital structure, the cost of capital  becomes an optimizing tool that helps you decide the right mix of debt and equity.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA36Z7RssalrA23Yygf5rVUk2rwExyYev5uwZhI4x02kVW6vXO5BnNkhvr2Uo93haXjcHQ14bIpQH53LiWb4vwKrSd28fvZl1QN5EJmAZh_Po6yHL7tsyqtMZxuWmE6CTs_6UZB3OHvhw/s1600/Costofcapitalanddebtradeoff.png)

In dividend policy, the cost of capital becomes the divining rod for whether you should be returning more or less cash to your stockholders. If you operate in a business where your returns on new investments consistently fall short of your cost of capital, you should be returning more cash to your investors. 

In the valuation class, the cost of capital is the discount rate that you use to bring operating cash flows back to today, to arrive at a value for a business. It has, unfortunately, also become the instrument that analysts use to bring their hopes, fears and worries into value, adding premiums to the discount rate, if an asset is illiquid, or reducing it, if it provides other benefits.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrySBQKKzVf1Ft0Frlp74gOC14UpZwNgxQW-oTaSkJkvpALKY2BXyhy0Bejyx26ac7tnH0oJw4KbbguerPm5RQNZUh5nZxEjPvdW4jwfFINVSgPbgnKi5RMesxYRwOVRd6cA7j8jKCx2k/s1600/CostofCapitalDifferentforms.png)

In short, it is difficult to do financial analysis without at least getting a sense of what the cost of capital is, for a business. The many uses to which it is put has also meant that it has become all things to all people, a number that is misused, misestimated and misunderstood.

**
**

**The Mechanics of Estimating Cost of Capital**

About a year ago, in the context of my 2015 data update, I had an extensive post on the mechanics of computing cost of capital. Rather than repeat that post, I will [direct you to](http://aswathdamodaran.blogspot.in/2015/01/putting-d-in-dcf-cost-of-capital.html) it and summarize the process in a picture, for estimating the cost of capital for a company in US dollars:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgELQQ8XMArL_U5f0nintS03F4v84ZYot34lB2NIsST0gp0HJ5TvNsqiOwhGA9A-tMSCcfM_ow7iQ65VDP10JoF3X68gVnZM0coy5OjYxT0VrjuaPZp9I14JgHS7DbHVq3uF6ij9R5mlHM/s1600/costofcapitalcompany.png)

Thus, the cost of capital is a composite cost of equity and debt and incorporates the tax benefits of debt (through the after-tax cost of debt) and the risk added by debt in increased costs for both equity and debt. If you want to estimate the cost of capital in a different currency, you have two choices. The first is to replace the US dollar risk free rate with the other currency's risk free rate (seem my earlier post on currencies) or to add the differential inflation rate between the US dollar and the currency in question to a US dollar cost of capital. Thus, if your US dollar cost of capital is 10%, the inflation rate in rubles is 9.5% and the US dollar inflation rate is 1.5%, your Russian ruble cost of capital will be approximately 18%. (It is a little more precise to compute this rate allowing for the compounding: (1.10) (1.095/1.015) -1, but I will leave it up to you to decide whether it is worth the effort.)

**The Cost of Capital - US companies**

Let me start off with the US-centric portion of this post, where I look at the distribution of costs of capital across my sample of 7480 firms that are listed in the United States. In making my assessments, I made some simplifying assumptions:

- I used the US 10-year bond rate of 2.27%, on January 1, 2016, as my risk free rate. I don't like to play games normalizing risk free rates.

- I used the [average unlevered beta for the sector](http://www.stern.nyu.edu/~adamodar/pc/datasets/betas.xls) as the beta for the company and levered this beta with the current debt to equity ratio of the firm.

- I used the implied equity risk premium for the S&P 500 (6.12% on January 1, 2016, rounded down to 6%) as the equity risk premium for all US companies in estimating the cost of equity. I know that some US companies have operating risk exposure outside the US, but I see no easy way that I can compute regional-weighted ERPs for this many companies.

- For the cost of debt, I used the S&P bond rating, if one was available, to estimate the default spreads and pre-tax cost of debt of the firm. For non-rated company, I used the standard deviation in equity in conjunction with a look up table (see the [cost of capital spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)) to estimate the default spread and pre-tax cost of debt. I used 40% as the marginal tax rate for the US in estimating the after-tax cost of debt.

- I used the current market capitalization as the value of equity and added up all interest bearing debt with the present value of lease commitments (for the next 5 years and beyond) to get to the debt, in computing the weights for debt and equity.

The resulting distribution of costs of capital across US companies is summarized below. Note that 90% of US firms have costs of capital between 5.23% and 10% and 50% of US firms have costs of capital between 6.60% and 9.20%.

**
**

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1gYShi6UEgWTXlnsNmu8dDikBedSu7rcf4Tp3IY0_fpRqacbrYXGHgtN63ogQikex_y4LHmWMEVzUfwpXbNi-KGAZFSQ6a6wjgSNZp3xa6Qe4a39dsQRto4wIcAqXKqAQmwVAAk8Fy44/s1600/WACC+Jan+2012+Picture.jpg)

If you are skeptical about betas and don't like computing costs of equity based upon them, I have a suggestion. Use the distribution of costs of capital in this graph, as your basis, for estimating a cost of capital for your firm. Use the cost of capital at the 90th percentile as your cost of capital for a risky firm, 8% as your cost of capital for a mature firm and 5.23% as your cost of capital for a very safe firm, and you should be relatively safe.

**The Cost of Capital - Global Distribution**

I also computed the cost of capital differences across global regions. Note that the differences are not rooted in currency, since the cost of capital for every firm is computed in US dollars. As to why costs of capital vary across countries, the answer can be traced back to two factors. The first is that debt ratios vary across the world, and that this may explain some of the variation. The second is that the regions of the world with higher sovereign default spreads and equity risk premiums (they go together in my approach) will have higher costs of capital than regions that have less risk. The table below summarizes the difference.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMDtBTk237GhGY5ZwGSTreNEuO7DXBamcD_AcQlllTgxRlyHtPNti-xcr1iN7KUsy8EN2_UPTThQ46xTszGrSguZDP3Ezyl4j1yhP2dV-ZueOFU3jhzd7wJCROdeosVdbjSb0s5fcCBN4/s1600/CostofCapitalbyRegion.png)

US companies have the lowest costs of capital, on average, in the world and East European and Russian companies carry the highest costs of capital. These are all in US dollars, but you can use the differential inflation approach to convert them into other currencies.

**The Cost of Capital - Sector Differences**

 Starting with the 41,889 firms that I have in my global sample at the start of 2016, I estimated the cost of capital for each company in dollar terms and then looked at the average costs of capital by sector. While you can find the [entire sector list for cost of capital](http://www.stern.nyu.edu/~adamodar/pc/blog/sectorwacc.xls) at the bottom of this post, I have listed the ten non-financial sectors with the highest costs of capital and the ten with the lowest:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNG8Cldhct-Rlu-mQyghhPBrRGfbLLwjPhR-TppVo2ePCR8B1QZgNgGLqSmNaGSpJLI5C-4L65OOTh4FiflfNJ40vZg0FrKBs_nnE4gHXxu4mhiF_A4FAmMwPktUrZBsOZLGiaLFoakdk/s1600/2016-01-14_00-45-09.png)
Source: [Damodaran Online](http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html)

So, what now? If you have to estimate the cost of capital for a sector or a company in that sector, in US dollar terms, you could use the cost of capital for any companies that you value, in this sector. Again, adding the inflation differential will give you the cost of capital in any other currency. 

**The Bottom line**

The cost of capital may be the most used number in finance, but it is also the most misused. Companies often use one cost of capital to assess investments with different risk profiles, acting on the presumption that the cost of capital is the cost of raising company, rather than a risk adjusted required return for investing in a  risky asset. Investors use the cost of capital as a dumping ground for all their fears about investments, augmenting the standard risk-adjusted discount rate with premiums for liquidity, small market capitalization and opacity. We can do better!

**Presentation**

- [Cost of Capital: Misused, Misestimated and Misunderstood](http://www.stern.nyu.edu/~adamodar/pdfiles/country/CostofCapitalCFA2015.pdf)

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

- [Putting the D in the DCF: The Cost of Capital](http://aswathdamodaran.blogspot.in/2015/01/putting-d-in-dcf-cost-of-capital.html)
