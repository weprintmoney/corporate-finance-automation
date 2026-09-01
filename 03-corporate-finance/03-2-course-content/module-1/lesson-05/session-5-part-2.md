---
title: "Session 5 Part 2 — Risk-Free Rates in Difficult Currencies"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 5 Part 2 — Risk-Free Rates in Difficult Currencies

## Estimating Risk-Free Rates When There Is No Default-Free Entity

So now that we've talked about getting a risk free rate in a currency where there is a default free entity, like the US, Canada, let's talk about estimating risk free rates in difficult currencies. What are difficult currencies? These are currencies where there is no default free entity. When you have no default free entity in a currency, you cannot use the government bond rate as a risk free rate. Why? Because a government bond rate is no longer risk free. So here you three choices.

One is you can start with the local currency government bond rate and try to extract from it, remove from it the portion that is for default risk. So as an example, take the Indian government in November of 2013. I am analyzing Tata Motors in Indian Rupees, so I started with a risk free rate by looking at the government bond rate in Indian Rupees. In November of 2013, that rate was 8.82%. I'm tempted to use this as my risk free rate, but I know I cannot. Why? Because the Indian government is not default free.

In fact, I used a very simple measure of default risk by looking at the sovereign ratings that Moody's attaches to India. Now, ratings agencies actually attach two ratings to every country, a local currency rating and a foreign currency rating. The foreign currency rating for India measures the default risk that Moody's or S&P's sees in India when it borrows money in US dollars or euros. The local currency rating is the default risk that Moody's sees in India when it borrows in Rupees. If that rating had been A, I'd have left the rate at 8.82% and called it my risk free rate. But the rating that I saw for India was Baa3, not an awful rating, but a rating that goes to the default spread of about 2.25%.

I say, what do I do with this? Remember that the Indian government bond rate was 8.82%. If 2.25% of that is for default risk, you subtract that 2.25% from the 8.82%, you end up with a risk free rate in Indian Rupees of 6.57%. Do you see what I'm doing? I'm taking out from the government bond the portion that I think is due to default risk. So that's your first choice when it comes to a foreign currency: to start with a local currency government bond rate and net out the default spread.

In fact, I tried this for the Chinese government as well. The Chinese ten year government bond rate in Renminbi was 4.3%. The default spread for China was 0.8%. You subtract it out, you come up with a risk free rate of 3.5% in Chinese Renminbi. So if you want to stay with the local currency, you can do it as long as you're willing to clean up the government bond rate.

## Switching Currencies and Doing Analysis in Real Terms

But what if I don't trust the local currency bond? Well, you can always do your analysis in a different currency. Currency is a choice. What do I mean by that? I can analyze Tata Motors in Rupees or US dollars or British pounds, and as long as I stay consistent, my analysis should deliver the same results no matter which currency I pick. I'll come back and back this up, but that is a nice choice to have, because in some countries in some currencies, you might actually be better off doing your analysis in a foreign currency. For much of the last two decades, equity research and valuation in Latin America has been done in US dollars, not in the local currency. You might view that as a sign of weakness, but if the local currency is difficult to work with, why not switch?

There's a third choice. When you pick currencies, you bring inflation into your analysis. You bring it into your cash flows, you bring it into your discount rate. You could actually do your analysis in real terms. What does that mean? You don't get any help from inflation when you do your cash flows. Any growth you get has to be real growth. You got to sell more units. And your discount rate then has to be a real discount rate, which means you need a real risk free rate to do your analysis. A real risk free rate might look like it's tough to compute, but I actually can suggest to you a very simple proxy. In the US, you have the US treasury bond rate. You also have what's called the TIPS rate. This is a US treasury bond that's protected against inflation. That rate in November of 2013 would have been about 0.75%. If I were doing my analysis in real terms, that's what I would use as my risk free rate.

Incidentally, when I analyzed Vale, the Brazilian mining company, I chose to do my analysis in US dollars. Not because I was a coward, but because as a commodity company, it actually reported its numbers in US dollars, was easier to do in US dollars. Now what risk free rate I'm going to use, I'm going to use the US T-bond rate of 2.75%, just like I did for Disney. So if you have a currency where there is no default free entity, those are your choices.

## Three Ways to Estimate a Default Spread

Let me back up a little bit though. Remember the 2.25% I netted out from the 8.82% to get to a risk free rate in Indian Rupees. You're saying, where do you come up with a default spread? There are three ways you can get a default spread for a country.

The first is to do what I just did. Look up the rating for the country, Baa3, look up the default spread that goes with that rating. As long as you have a rated country, this will give you a way out. However, the downside is you're trusting the ratings agencies to get the rating right.

There's a second choice. There's a market called the CDS market, the credit default swap market, and in that market, you can buy a sovereign CDS. That actually buys you insurance against default risk by a sovereign government. Think of it as a market set measure of default risk. You can look up that number for your country. That's available for about 60 countries as opposed to the 140 countries which are rated, but for those 60 countries, you have a second measure of risk.

There's a third way in which you can get default risk. If the country you're interested in issues bonds in US dollars. Let's take Brazil. Brazil has dollar denominated bonds. You can take the interest rate on the dollar denominated bond issued by that government and compare to the T-bond rate. So the T-bond rate is 2.75%, and your local government issues dollar denominated bonds with a 6% rate, 6% - 2.75% will be at 3.25% default spread.

Three different default spreads, take your pick and stay consistent. Don't spend days and days trying to pick between these two, the three different ways of getting the default spread. To illustrate that the three approaches can give you very different numbers, I've used four countries in this example: Brazil, India, China, and Poland. Brazil, for instance, I can get the default spreads using all three approaches, and I get very different numbers. For India, I can use only two of the approaches. More generally, though, if you can use more than one approach, go ahead and use more than one approach. If you can use only one, you're kind of stuck with that. But the end game is, you want a default spread for a government, so you can net it out of the government bond rate to get to a risk free rate.

## Why Risk-Free Rates Vary Across Currencies

Now, once you've got a default free rate in different currencies, I put it on a graph here as of January 2017. You say, why? Take a look and there are about 30 currencies for which I've estimated risk free rates, default free rates, and that's the red portion of the graph. I've essentially taken government bonds and cleaned them up to come up with risk free rates.

Notice that risk free rates vary across currencies. There are some currencies where risk free rates are very high: the Nigerian Naira, the Russian Ruble, the Brazilian Real. There are some currencies where risk free rates are not just low, they're even negative. The Swiss Franc rate. Risk free rates vary across currencies. That's stating the obvious, but I have a question. Why do you think risk free rates vary across currencies? It can't be because some countries are riskier than others because these are risk free rates.

Put simply, here's the reason risk free rates vary across currencies. It's inflation. High inflation currencies have higher risk free rates, low inflation currencies have low risk free rates, and therein lies the reason why currency doesn't matter. If you pick a high inflation currency to do your analysis, your risk free rate will be high, your hurdle rates will be high. You think that's bad. But that same inflation that pushes up your risk free rate will also help you on your cash flows, your growth rate and your returns. Stay consistent. If you switch to a low inflation currency, let's say the Swiss Franc, your risk free rate will be lower, your hurdle rate will be lower, but so will your returns and your growth rates. The key to currency is to stay consistent, pick a currency and do both your returns and your hurdle rate in that currency.

## Staying Consistent Across Currencies

So assuming you've decided what currency you're going to do the analysis in, make some choices. Try to estimate a risk free rate in that currency and start thinking also about alternatives. Maybe you want to keep track of your company in two different currencies until you feel comfortable enough to let go. But there will be a point where you will realize that the key here is to do things right with a single currency, to stay consistent rather than do things wrong in three different currencies.
