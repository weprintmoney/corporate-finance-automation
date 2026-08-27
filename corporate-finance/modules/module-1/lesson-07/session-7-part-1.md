---
title: "Session 7 Part 1 — Implied Equity Risk Premiums and Country Risk"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 7 Part 1 — Implied Equity Risk Premiums and Country Risk

In the last session, we talked about using historical data to come up with an equity risk premium for a market like that in U.S., where you do have data going back decades and even centuries. But even with all of that data, the historical risk premium is still a soft number. A soft number in what sense? It comes with a big range. In this session, I'd like to talk about a different way of estimating an equity risk premium for the U.S. and use that as my base to come up with equity risk premiums for different countries, and finally, close off by looking at the equity risk premiums for individual companies.

## A Forward-Looking Approach to the Equity Risk Premium

So let's talk about the equity risk premium. It's a price of risk in the equity market, right? We talked about doing surveys, and we talked about how shaky those survey premiums are. We talked about using historical data and how noisy those estimates are, the big standard errors. There is a different way of thinking about equity risk premium which is more forward-looking and more precise.

To get a sense of what I'm going to do here, let me give you an analogy. Let's assume you buy a bond. You know the price you paid for the bond, and I ask you to compute the yield-to-maturity on the bond. If you don't remember, here's the way you compute yield-to-maturity on a bond. You take the bond price, you take the coupons in the face value, and those are promise numbers, and you solve for that discount rate that makes the present value of the cash flows in the bond equal to the price of the bond. We do that in fixed income markets all the time. I'm going to steal that concept and apply it to equity markets.

## Computing the Implied Premium for the S&P 500 in November 2013

In November of 2013, for instance, you could have bought the entire S&P 500 for $1,756. That's about the entire index. So buying a bond, you bought the 500 largest market cap stocks in the U.S. Instead of coupons, here's what you hope and pray you will make. You hope and pray you will make cash flows from dividends and buybacks. Unlike a coupon which is a fixed number, I don't know what those dividends and buybacks will be in the future, but I can tell you what they were in the 12 months leading into November of 2013. And that collective cashflow you'd have earned in those 12 months would have been 82.35%.

Let me complete my story. The S&P 500 is the most tracked and widely followed index in the world. There are analysts who project growth and earnings for the entire index. In November of 2013, those analysts were projecting a growth rate of about 5.59% in earnings for the S&P 500. I'm almost home, and here's what I'm going to do. I'm going to take the cash flows in the most recent 12 months that I know, grow those cash flows at 5.59%, the expected growth. And after year five, I'm going to assume that those cash flows will grow at the same rate as the economy and I'm going to use the risk-free rate as my proxy for that growth rate in the economy. This is something you're going to see me do over and over again. I firmly believe that the best estimate of long-term nominal growth in the economy is the risk-free rate.

So, in this case, here's what I have. I'm expected cash flows for the next five years. And beyond the fifth year, I expect those cash flows to grow at 2.55% a year forever. I ask the same question I asked of a bond. What discount rate will make the present value of my cash flows equal to the level of the index trap? Trial an error. In this case, a solver function in Excel. I come up with 8.04%. You say, "What do I do with that?" The risk-free rate on that day, the 10-year T-bond rate was 2.55%. You take the difference between 8.04% and 2.55%, you get 5.49%. You say, "What does that tell me?" Based on what you were paying for stocks in November of 2013 and the cash flows, your expected equity risk premium, your implied premium, so to speak, is 5.49%.

## Why the Implied Premium Beats the Historical Premium

Watch what I do differently here. Rather than look at the past, I'm looking at the future. And this number that I'm going to get is a dynamic number. Dynamic in what sense? As the index changes, as the cash flows change, as the risk-free rate changes, my equity risk premium will change.

Now, here's what I'm going to do differently now. Rather than build to a risk premium for individual countries based on the historical premium, I'm going to build it off the implied premium, and here's why. When you look at November of 2013, at the choices I have to come up with an equity risk premium for a market like the U.S., I could have gone with the historical data. And the historical data November of 2013 would have given me an equity risk premium of 4.2%, but a standard error of 2.33%. That's a huge range on my beta. Instead, I have an implied premium of 5.49% based on estimates. But those estimates yield a much smaller range. By my judgment, the implied equity risk premium, the range around it, is closer to 5% to 6%. I'm much closer to my true number. I'm going to argue that a better estimate of the equity risk premium November of 2013, for the U.S., would be 5.5%. That's a 5.49% rounded up.

## Building Country Equity Risk Premiums Off the Implied Premium

Now, to get the equity risk premiums for individual countries, I still have to come up with the default spreads and adjust those default spreads. So let me summarize what I'm going to do to get risk premiums for individual countries. For any country which has a AAA rating, countries like Germany, Australia, Singapore, here's what I'm going to do. I'm going to take my implied equity risk premium for the U.S. and make it the risk premium for that country. Why am I doing this? Because my argument is that if you're in five mature markets, their equity risk premiums have to be roughly similar, because if they weren't, money would leave the market with a lower equity risk premium and go to the market with a higher risk premium. So you're going to see 5.5% populate any AAA rated country. If you're not AAA rated, my work has just begun. I'm going to come up with a default spread based on your rating or a sovereign CDS spread. And then I'm going to adjust that spread for the higher risk in equities by looking up the standard deviation in the equity index and the government bond. That adjusted number is what I'm going to report as my equity risk premium for that country.

## The November 2013 Global Risk Premium Map

So you ready? Here's what the world look like to me in November of 2013. I'm going to give you a little time to absorb the data because there's a lot of data on this page because I've taken every country for which there is a rating and estimated an equity risk premium. Let's start off with the easy countries. If you look to the to the left, you'd see the USA and Canada, and they have a 5.5% percent premium. That's a 5.49% implied premium in November of 2013. And Canada has that same premium as the U.S. because it's AAA rated. Germany, Australia, New Zealand, Singapore, all have 5.5% premiums, no country risk.

If you go to Latin America you see the impact of country risk. You take Argentina. You start with a 5.5% premium, but you add an extra 10.13% premium. Why so large? Because Argentina has a low rating. That low rating begets a large default spread, translates into a higher risk premium. So I do this for every country. You can already see within regions like Latin America how much of a spread there is across countries. Chile has a much smaller risk premium than Argentina or Venezuela, but that reflects the reality of different risks within the same region. So those are my risk premiums for individual countries. And again, reminding you how I got there. I started with the risk premium for the U.S., from an implied premium and built up to each country's risk premium.

Just as an aside though, could I compute implied risk premiums for countries outside the U.S.? I think I can, because all I need is not history, but the level of the index right now, my expected cash flows into the future. It's more difficult doing this outside the U.S. because getting that expected growth rate is a much tougher task. But one of these days, this entire table could be constructed of implied premiums. But for the moment, it's just the U.S.-implied premium plus the additional country risk premium.

## Why Global Risk Premiums Matter for Every Company

You may wonder why you need to look at the entire globe. After all, you might be looking at a Chinese company or an Indian company or a US company. You think, "Why should I care about the rest of the world?" You're going to see in the second half of this session why you have to care, because ultimately, a company's risk does not come from where it's incorporated but from where it does business. Coca-Cola might be a U.S company, but it gets more than 50% of its revenues outside the U.S. Your equity risk premium should reflect where you have operating risk.
