---
title: "Session 6 Part 2 — Estimating Equity Risk Premiums for Markets Without History"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 6 Part 2 — Estimating Equity Risk Premiums for Markets Without History

## The Problem: Markets Without Historical Data

So, we've talked about estimating historical risk premiums from market like the U.S., with lots of data going back decades, perhaps even centuries. But now, let's talk about estimating risk premiums for the markets where you don't have the luxury of that much historical data. In most markets outside the U.S., even markets that have U.S.-developed markets, you don't have the luxury of historical data that you do in the U.S. Most of these markets have not been around for more than three or four decades. And even the markets that have been around prior to them, there was no liquidity in these markets. I would argue that even the West European markets, you have a problem going back more than 40 or 50 years. The markets just did not have enough liquidity.

So the question is, What do we do about markets like these? Remember, I have an Indian company, a Brazilian company, and a Chinese company in my sample. I need an Indian equity risk premium, a Brazilian equity risk premium, and a Chinese equity risk premium, and there is zero chance that I'm going to get data like I did for the U.S. So, since you cannot use historical risk premiums, you have to come up with ways of adjusting.

## Approach 1: Adding Default Spreads to the U.S. Risk Premium

So, let me talk about two ways in which you can get risk premiums, equity risk premiums for markets without a lot of history. The first approach is to actually draw on something we talked about in the context of risk-free rates. Remember how we got the risk-free rate for a currency where there was default risk in the sovereign? We looked up a default spread for that country. In the case of India, it was 2.25%, in the case of China it was 0.8%, and we netted out that default spread against a government bond rate to come up with the risk-free rate. And at that point in time, I ask you not to worry about being too specific about how you estimated the default spread, because we'll come back again in the analysis. Well, here's where it comes back.

The first way in which you can adjust equity risk premiums is to start with an equity risk premium for the U.S. Let's say it's 4.62% as we estimated in the table, just a couple of pages ago, or 4.5%. Once you've got that historical risk premium, you can add on to it. So, let me go back to November of 2013 to illustrate how this process would work. In November of 2013, the historical risk premium for the U.S., the geometric average, stock versus T-bonds was 4.2%. That's my starting point.

To get an equity risk premium for India, here's what I do. I take the 4.2%, and add on the default spread of 2.25% that I got based on its rating. My risk premium for India will be 6.45%. I take the 4.2%, add the 0.8% that I got for China based on its rating, 4.2% plus 0.8% is 5%. I take Brazil, I take the 4.2%, add on the 2% that I got as a default spread based on the rating, and I come up with an equity risk premium for Brazil of 6.2%.

And of course, we also talked about how rating's agencies can sometimes screw up. That rating might not be a good measure of the default spread. So, if you prefer a sovereign CDS, remember we talked about this as an alternative default spread, you can use the sovereign CDS for each of these markets. That will give you a different estimate of the risk premium for the country, but you're still working with the same basic approach. Start with a U.S. risk premium, add the CDS spread, and you come up with a risk premium for that country.

## Approach 2: Scaling the Default Spread for Equity Risk

So, that's using default spreads as a measure of the additional risk premium for a country. And when I first became familiar with this approach, a lot of investment banks were using it, my big concern with this approach was this was the spread, the 2.25%, the 0.8%, the 2%, the spreads for Brazil, India, and China. Those were spreads I would have demanded for buying bonds issued by the governments in these countries. But remember, I'm not thinking about buying bonds, I'm thinking about buying equities in India, China, and Brazil. I would argue that equities are riskier than bonds. And if I'm demanding a 2.25% default spread for buying a bond in India, I would demand the largest spread for buying equity. You're saying, "That's fine, but how do I know how much larger?"

Let's do some algebra. Let's assume I could look up the standard deviation in Indian equities, or Chinese equities, or Brazilian equities. And I could look up the standard deviation in the Indian Government bond. Let me start with Brazil to illustrate this process. The equity risk premium, I'm going to start with is the 4.2% that I got for the U.S. The default spread I have for Brazil is 2%. That's where I stopped last time, right? But I'm going to go on. I looked up two standard deviations. The standard deviation, the BOVESPA, the Brazilian Equity Index was 21%. The standard deviation in the Brazilian Government bond was 14%. So, for the 14% risk investment, I'm demanding a 2% spread, right? And if equity is one and a half times more risky, 21% over 14%, I would assume you'd demand one and a half times 2% which gives you 3%. So, my equity risk premium for Brazil would be 4.2% plus 3%, giving me an equity risk premium of 7.2%.

So, all I've done is augment the default spread. Using that same approach, I come up with equity risk premiums for India and China. And my equity risk premiums are larger using this approach, the adjusted default spread. My risk premium for India is 7.8% now, and my risk premium for China is 5.64%, all reflecting again, the default spread scaledown.

## Applying the Approach to Your Company

So, as you move from a market like the U.S., and perhaps the U.S. is the only market we have the kind of historical data to even trust a historical risk premium, my suggestion is that you use default spreads that come from the bond market, and, in my case, adjust those default spreads or adapt them to make them equity risk premiums, additional premiums, and come up with the equity risk premiums for the country you're interested in.

So, now that we have a way of estimating equity risk premiums for other markets, pick a different market, a market outside the U.S., even if you're doing a U.S. company, and try to estimate the equity risk premium for that market. The process is simple. Start with the equity risk premium for the U.S., and if you want, you can use the 4.62% equity risk premium you got from the historical data. Get a default spread for the country you're interested in and if you can, see if you can look up the standard deviations, the equity index in that market, and that government bond. You're well on your way to getting an equity risk premium for another country and as you'll see, this is a critical input into valuing a company even if you're just in a developed market.
