---
title: "Amazon and Apple at a Trillion $: A Follow-up on Uncertainty and Catalysts!"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2018/09/amazon-and-apple-at-trillion-follow-up.html
published: 2018-09-21
updated_source: 2018-09-21
fetched: 2026-08-27
tags:
  - Apple
  - Short selling
  - Value and Pricing
---

# Amazon and Apple at a Trillion $: A Follow-up on Uncertainty and Catalysts!

_Source: [https://aswathdamodaran.blogspot.com/2018/09/amazon-and-apple-at-trillion-follow-up.html](https://aswathdamodaran.blogspot.com/2018/09/amazon-and-apple-at-trillion-follow-up.html) — published 2018-09-21_

In [my last post](https://aswathdamodaran.blogspot.com/2018/09/apple-and-amazon-at-trillion-looking.html), I looked at Apple and Amazon, as their market caps exceeded a trillion dollars, tracing the journey that they took over the last two decades to get to that threshold and valuing them  given their current standing. While you can check out the stories that I told and the details of my valuation in that post, I valued Apple at $200, about 9% less than the market price, and Amazon at abut $1255, about 35% lower than its market price. I concluded the post with a teaser, promising to come back with my decisions on whether I would sell my existing Apple shareholding and/or sell short on Amazon, after reviewing two loose ends. The first is to lay bare the uncertainties inherent in both valuations, to see if there is something in those uncertainties that I can use to make a better decision. The second is to evaluate whether there are catalysts that will convert the gap that I see between value and price into actual profits.

**Facing up to Uncertainty**

One of the recurrent themes in this blog is that we (as human beings) are not good at dealing with uncertainty. We avoid, evade and deny its existence, and in the process end up making unhealthy choices. When valuing companies, uncertainty is a given, a feature and not a bug, and traditional valuation models often give it short shrift. In fact, looking at my valuations of [Apple](http://www.stern.nyu.edu/~adamodar/pc/blog/AppleSept18.xlsx) and [Amazon](http://www.stern.nyu.edu/~adamodar/pc/blog/AmazonSept18.xlsx), you can see that the only place that I explicitly deal with uncertainty is in the discount rate, and even that process is rendered opaque, because I use betas and equity risk premiums to get to my final numbers. My cash flows reflect my expectations, and even in my moments of greatest hubris, I don't believe that I know, with precision, what will happen to Apple's revenue growth over time or how Amazon's operating margin will evolve in the future. So, why bother? In investing, you have no choice but to make your best estimates and value companies, knowing fully well that you will be wrong, no matter how much information you have and how good your models are. 

That said, it is puzzling that we still stick with point estimates (single numbers for revenue growth and operating margins) in conventional valuation, when we have the tools to bring in uncertainty  into our valuation judgments. While our statistics classes in college are a distant (and often painful) memory for most of us, there are statistical tools that can help us. While these tools may have been impractical even a decade ago, they are now more accessible, and when coupled with the richer data that we now have, we have the pieces in place to go beyond single value judgments. It is with this objective in mind that I recently updated a paper that I have on using probabilistic and statistical techniques to enrich valuation online, and you can get the paper [by going to this link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3237778). Consider it a companion to [another paper that I wrote a while back](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2323621), dealing more expansively with uncertainty and healthy ways of dealing with it in investing and valuation.

[Summarizing the probabilistic techniques](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3237778) that may help in valuation, I suggest three: (1) S*cenario Analysis*, for valuing companies that may have different valuations depending upon specific and usually discrete scenarios unfolding (for example a change in regulatory regimes for a bank or telecommunications company), (2) D*ecision Trees*, for valuing companies that face sequential risk, i.e., you have to get through one phase of risk to arrive at the next one, as is the case with young drug companies that have new drugs in the regulatory pipeline and (3) *Monte Carlo Simulations*, the most general technique that can accommodate continuous and even correlated risks that you face in valuation, as is the case when you forecast revenue growth and operating margins for Apple and Amazon, in pursuit of their values.

**Simulated Values: Apple and Amazon**

Before delving into the simulations for Apple and Amazon, it is important that we set up the structure of the simulations first by first deciding what variables to build distributions around. While you may be tempted by the power of the tool to make every input (from risk free rates to terminal growth rates) into a distribution, my suggestion is that you focus on the variables that not only matter the most, but where you feel most uncertain. With Apple, the three inputs that I will build distributions around are revenue growth, operating margins and cost of capital. With Amazon, I will add a fourth variable to the mix, in the sales to invested capital, measuring how efficiently Amazon can deliver its revenue growth.

*Apple: A September 2018 Simulation*

I build around my core story for Apple, which is that it will be a slow growth, cash machine, deriving the bulk of its revenues, profits and value from the iPhone, but allow for uncertainty in each of my key inputs:

- Revenue growth: While my expected growth rate stays 3%, I allow for a range of growth rates from no growth (flat revenues) , if the iPhone's higher prices cost it signifiant market share) to 6% growth, which would require that Apple find a new growth source, perhaps from services or a new product.

- Operating Margin: In my story, I assumed that operating margin would decline to 25% (from  the current 30%) over the next five years. While I still feel that this is the best estimate, I allow for the possibility that competition will be stronger than expected (with margins dropping to 20%), at one end, and that Apple will be able to use its brand name to keep margins at 30%, at the other. 

- Cost of capital: My base case cost of capital is 8.20%, reflecting Apple's mix of businesses, but allowing for errors in my sector risk measures and changes in business mix, I build a distribution centered around 8.20% but with a small standard error (0.40%).  

Since I want to stay market neutral, taking no stand on either the level of interest rates or overall stock prices, I am leaving the ten-year bond rate and equity risk premium untouched. The results of the simulation are below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiObDftrr8jO6gUL0FqQVuIxcHhS_A6H_mmC1urXaGBuX8iIaPwBDWRy8chEV_Hb8cIwUKn0j4alDGUG0PkqDANen6ZcBvVvGxXcNZ3i8yCl2j-3KWaLBSYUZ8Z266Yu02kn0HZrYcX4-U/s1600/AppleSimulation.jpg)
[Valuation](http://www.stern.nyu.edu/~adamodar/pc/blog/AppleSept18.xlsx) & [Simulation Output](http://www.stern.nyu.edu/~adamodar/pc/blog/AppleSimulationSept18.xlsx)

Note that the median, mean and base case valuations are all bunched up at $200 and that the range in value, using the 10th and 90th percentiles, is tight ($176 to $229).

*
*
*Amazon: A September 2018 Simulation*

Moving from Apple to Amazon, my uncertainties multiply partly because my story is of a company that will move into any business where it believes its disruptive platform can deliver results, and there are very few businesses that are immune. Consequently, every input into the valuation is much more volatile, but I will focus on four:

- Revenue Growth: I used an *expected growth rate for Amazon of 15% a year* for the next 5 years, tapering down to lower levels in the future, to push revenues to $626 billion, ten years from now. While that is an ambitious target, Amazon has proved itself capable of beating sky high expectations before and *it is plausible that the growth rate could be as high as 25%* (which would translate to revenues of $1.13 trillion, ten years out). There is also the possibility that regulators and anti-trust enforcers may step in and restrain Amazon's growth plans, which could cause the growth rate to drop significantly to 5% (resulting in revenues of $330 billion in year 10).

- Operating Margin: While Amazon's margins have been on a slow, but steady, climb in the last few years, much of that improvement has come from the cloud services business, and the future course of margins will depend not only on how well Amazon can bring logistics costs under control but also on what new businesses it targets. I will stay with my base cash assumption of a target operating margin of 12.5%, but allow for the possibility that Amazon's margins will stay stagnant (close to today's margins of about 7%), at one extreme, and that there might be a new, very profitable business that Amazon can enter, pushing up the margins above 18%, at the other.

- Sales to Invested Capital: Currently, Amazon is an efficient utilizer of capital, generating $5.95 in revenues for every dollar of capital invested. While this will remain my base case, there may be future businesses that Amazon is targeting that may be more or less capital intensive than its current ones, leading to a significant range (3.95 for the more capital intensive - 7.95 to the less  capital intensive).

- Cost of Capital: I will stick with my base case cost of capital of 7.97%, with the possibility that that it could drop as Amazon's older businesses become profitable (but not by much, since the current cost of capital is close to the median for global companies) as well as the very real chance that it could go up significantly, if Amazon targets risky businesses in emerging markets for its growth.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHYlEEH77PJDSN-yT1hZNCVRhldvjOL9fib5jL1L1oTc8UhubRbGjz5TdKHMlcm6YmnoB5PoyhifUKF36SD4uM6T52LK3nWAcJhyphenhyphenCg_QavTr6SKLOS8AAqINVYb785-S-RQoRe7y9xCsg/s1600/AmazonSimulation.jpg)
[Valuation](http://www.stern.nyu.edu/~adamodar/pc/blog/AmaqzonSept18.xlsx) & [Simulation Output](http://www.stern.nyu.edu/~adamodar/pc/blog/AmazonSimulationSept18.xlsx)

The median value across the simulations is $1242, close to the base case valuation of $1,255. The range on value, using the 10th and 90th percentiles is $705 - $2,152, much wider than the range for Apple.

*
*
*Lessons from Apple and Amazon Simulations*

Simulations yield pretty pictures and if that is all you get out of them, it is time and energy wasted. There are lessons that we can eke out of the Apple and Amazon simulations that may help us in making more informed judgments:

- This is not about getting better estimates of value: If you are running simulations because you think they will give you more precise or better estimates of value than point estimate valuations, you will be disappointed. Since my input distributions are centered around my base case assumptions, and they should be, the median values across 100,000 simulations are close to my base case valuations for both Apple and Amazon.

- If it is a risk proxy, it is a very noisy and dangerous one: It is true that the spread of the distributions provides a measure of estimation uncertainty that you bring into your valuation. Using the Apple and Amazon simulations to illustrate, I face far greater uncertainty with my Amazon story than with my Apple story, and you can see it reflected in a larger range of value for the former. You may be puzzled that my cost of capital is lower for Amazon than for Apple, but that reflects the fact that much of the uncertainty that I face with Amazon is company-specific and should be buffered by other stocks in my portfolio. As a diversified investor, the variance in simulated values is a poor proxy for risk. However, if you are an investor who prefers concentrated portfolios, you can use the variance in simulated value as a measure of risk. 

- There can be no one margin of safety for all companies: I have [written about the margin of safety before](http://aswathdamodaran.blogspot.com/2016/05/dcf-myth-31-margin-of-safety-tool-for.html), often with skepticism, and one of my critiques has been with the way it is used in practice, where it is set at a fixed number for all companies. Thus, you will find value investors who use a margin of safety of 15% or 20% for all stocks, and the Apple and Amazon simulations show the danger in this practice. A 15% margin of safety for Apple may be too large, given how tightly values are distributed for the company, whereas the same 15% margin of safety may be too small for Amazon, with its wider band of values.

- Tails matter: Symmetry or the lack of it in distributions may seem like an inside statistics topic, but with simulated values, it has investment consequences. You can see that Apple's value distribution is  much more symmetric than Amazon's distribution, with the latter having a significant positive skew, reflecting a greater likelihood of big positive surprises in value, than negative ones. With companies with exposure to large and potentially catastrophic news stories (a large lawsuit or debt covenants), you can have value distributions that are negatively skewed.  In general, positive skewed distributions are better for (long) investors than negatively skewed ones, and the reverse is true for investors who are shorting a company.

I ran the simulations after my base case valuations suggested that Apple and Amazon were over valued, to see how they might affect my decision on whether to sell short on either company. The results are mixed.

- While the simulations confirm my over valuations (no surprise there), with both companies, the current stock price is well within the realm of possibilities. While my base case valuation suggested that Apple was far less over valued (10%) than Amazon (55%), there is roughly a 15-20% chance that both companies are under valued, not over valued.

- In addition, with Amazon, there is the added risk, if you are selling short, given the long positive tail on the distribution, that if I am wrong, the price I will pay will be much greater than if I am wrong with Apple.

The bottom line is that while Amazon seemed like a much better short selling target, after my base case valuations, because it was far more over valued than Apple, the simulations that I did on the two companies even out the scales, at least marginally. Apple is more over valued, but the probability of making money, assuming my valuations are on target is about the same with both stocks, and the downside of being wrong is far greater with Amazon than with Apple.

**Value and Price: The Search for Catalysts**

In the post that initiated this series, I looked at why crossing a trillion-dollar threshold may matter to investors, using the contrast between the value process and the pricing process. In effect, I argued that there can be a gap between value and price, and that even if you are right about your value judgment, you will make money only if the gap between the two closes:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjU1QN-sQzu86iGzZxFok8Jg0Mtp5QsczWNrijQqzpB7KL-0yqTe_DBQpd5ocjODFEphry1_0cdOtNIX9rVo57sRCyEb5lCm0ebcrq76ZwBlBkaG31hORlQhD_hl-KvKsVKqLf6kkCJf10/s1600/Price+vs+value+Catalysts.png)

Investment success thus rides not only on the quality of your value judgment, and how much faith you have in it, but on whether there are catalysts that can cause the gap to change. With companies, these catalysts can take different forms:

- Earnings reports: In their earnings reports, in addition to the proverbial bottom line (earnings per share), companies provide information about operating details (growth, margins, capital invested). To the extent that the pricing reflects unrealistic expectations about the future, information that highlights this in an earnings report may cause investors to reassess price. 

- Corporate news: News stories about a company's plans to expand, acquire or divest businesses  or to update or introduce new products can reset the pricing game and change the gap.

- Management Change/Behavior: A change in the ranks of top management or a managerial misjudgment that is made public can cause investors to hit the pause button, and this is especially true for companies that are bound to a single personality (usually a powerful founder/CEO) or derive their value from a key person. 

- Macro/ Government: A change in the macro environment or the regulatory overlay for a company can also cause a reassessment of the gap.

With all of these catalysts, there may be value effects (because the cash flows, growth and risk) as well, and it should also be noted that when the gap changes, it may not always close. In fact, these catalysts can sometime make a gap bigger, by feeding into pricing momentum.

As an investor, I look for catalysts when I invest, but I am even more intent on finding them, when I sell short than when I am long a stock. The reason for that divergence is that I am in far greater control of my time horizon, when I buy a stock, since, as long as I stay disciplined and retain faith in my value, only liquidity needs can cause me to sell. When I sell short, my time horizon is far less under my control, exposing me to timing risk. Put different, I can bet on a company being over valued, be right on my thesis, but still lose money on a short sale, because I am forced to close out my position, in the absence of a catalyst.

Going through the list of catalysts with Apple and Amazon, with both stocks approaching all-time highs, there is no obvious pricing trigger than I can point to, though my technical analyst friends will undoubtedly point to indicators that I did not even know existed. On the earnings front, the earnings reports for both companies are so heavily scripted to expectations that it would take a big surprise to reset stories, and I don't see that happening. In fact, I will predict that Amazon's earnings reports will continue to deliver double digit revenue growth and improving margins for the next few quarters, and investors will react positively, even though the growth may not be high enough or the margin improvement substantial enough to justify the market pricing. On the corporate news front, Apple's smart phone business model, with the pressure it puts on the company every year or two to reinvent itself, with the latest and the best, coupled with its big announcement events, creates catalyst moments. Looking back at Apple's ups and downs over the last few years, the triggers for substantial up and down movements on the stock have been new iPhone models doing better or worse than expected. In contrast, Amazon is remarkably low key in new product introductions, preferring to slip in under the radar. Both companies have well regarded and established CEOs, and neither company is personality-driven, making it unlikely that you will see management changes triggering big price changes. Finally, on the macro front, both companies face potential catalyst moments. For Apple, it is the possibility of a trade war with China, a huge market for its products and devices, and for Amazon, it is talk of regulatory restrictions and anti-trust actions that can constrain the company.  Since I cannot filibuster my way to a non-decision, I decided to compare my Apple and Amazon numbers/analysis, side by side:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmXySH4mNdPsoynCvpr0O79BMVFiDgokv_dc3N5aljXF2NN0LRoZm5el5lMogQ1ituR38jCgcbJL0bm4h133XNssy26KXmgfOXo4in2cz14o3vf5A5jC7zLDVN4o90HEhQrc7aI-TQ74A/s1600/ApplevsAmazonDecision.jpg)

I sold my Apple shares at $220, at the start of trading on Friday (9/21), but while I have not sold short any more shares. I have put in a limit (short) sell, if the price hits $230 (roughly my 90th percentile of value) in the near future. With Amazon, I sold short at $1950 at the start of trading on Friday (9/21).  the first time in twenty years that I have sold short on the company, and one reason that I am pulling the trigger is because I believe that the pushback from regulators and anti-trust enforcers will slow the company down in ways that no competitor ever could. I am doing so, with open eyes, since I believe that Amazon is in one of the best run companies in the world, adept at setting market expectations and beating them, and with a track record of taking short sellers to the graveyard. Time will tell, and I am sure that some of you reading this post will let me know, if my bet goes awry, but I don't plan to lose any sleep over this. 

**YouTube Video**

**
****Trillion Dollar Posts**

- [Trillion Dollar Toppers: Market Drivers, Pricing Triggers and Catalysts](http://aswathdamodaran.blogspot.com/2018/09/trillion-dollar-toppers-market-triggers.html)

- [Amazon and Apple at a Trillion $: Looking back and Looking forward](http://aswathdamodaran.blogspot.com/2018/09/apple-and-amazon-at-trillion-looking.html)

- [Amazon and Apple at a Trillion $: A Follow up on Uncertainty and Catalysts!](http://aswathdamodaran.blogspot.com/2018/09/apple-and-amazon-at-trillion-looking.html)

**Spreadsheets**

- Apple [valuation](http://www.stern.nyu.edu/~adamodar/pc/blog/AppleSept18.xlsx) and [simulation results](http://www.stern.nyu.edu/~adamodar/pc/blog/AppleSimulation18.xlsx)

- Amazon [valuation](http://www.stern.nyu.edu/~adamodar/pc/blog/AmazonSept18.xlsx) and [simulation results](http://www.stern.nyu.edu/~adamodar/pc/blog/AmazonSimulation18.xlsx)

*(I use Crystal Ball, an add-on to Excel, for my simulations. If you don't have that extension (available only on the PC version), you cannot recreate my simulations, but you can d[ownload the program for a trial run](http://www.oracle.com/technetwork/middleware/crystalball/downloads/index.html?ssSourceSiteId=ocomen) on the Oracle website)*

**
**
**Papers/Reading**

- [Facing up to Uncertainty: Using Probabilistic Approaches in Valuation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3237778)

- [Living with Noise: Investing and Valuation in the Face of Uncertainty](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2323621)
