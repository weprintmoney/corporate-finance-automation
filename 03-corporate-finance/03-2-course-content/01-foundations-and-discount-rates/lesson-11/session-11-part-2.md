---
title: "Session 11 Part 2 — Estimating Betas and Cost of Equity for Private Businesses"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 11 Part 2 — Estimating Betas and Cost of Equity for Private Businesses

## The Problem With Private Businesses

So far we've talked about publicly traded companies, and with publicly traded companies not only is information based on businesses available, getting a debt to equity ratio or running regression betas is feasible. But what if you have a private business? In this session I'd like to talk about estimating betas and cost of equity for private businesses.

If you have to estimate the beta for a private business, a division of a company, a non-traded asset, obviously you cannot run a regression. Why? Because you don't have past prices. Many people get stymied in estimating beta cost of equity for these businesses precisely for this reason, and there are two ways around the problem.

One is to look at accounting earnings and changes in earnings, and run regressions using accounting on exchanges. These are called accounting betas. I've seen it tried but it doesn't work very well for a simple reason. To run an effective regression you need lots of observations. With stock prices you can get them everyday. With accounting earnings, you'll be lucky to get them once every quarter. You don't have very many observations. You can't trust your regression very much.

So the alternative way of estimating a beta for a private business is to do what we did with public companies. Estimate a bottom up beta. Remember, for a bottom up beta all I need to know is what business you're in or businesses you're in, and I should be able to come up with the beta for your company even though it's a private company.

## Bottom Up Beta for Bookscape

So let's try this for that independent bookstore, Bookscape, that I talked about at the start of this class. I said I was going to take Bookscape through every single part of this process as if it were a public company. So here's what I'm going to do. I'm going to start off by trying to estimate a bottom up beta for Bookscape.

It's in the book retailing business, right? So I went looking for publicly traded book retailers and I very quickly realized I had a problem. I'd only bought three companies. So I expanded my sample by bringing in companies that feed off the book business. I brought in publishers. I ended up with about a dozen companies. I got the regression betas for these companies, since these are all public companies. I did the debt to equity ratio and I looked at the cash, and doing exactly what I do with public businesses I ended up with an unlevered beta of being in the book business of 0.76.

So that's exactly what I do with public companies, right? So all I need to do is take this unlevered beta and do exactly what I did in public companies, and I should be able to come up with the levered beta for Bookscape. But here's where I run into a problem. To get from the unlevered beta to levered beta, I needed debt to equity ratio. I also have a problem in getting that debt to equity ratio because I don't have a market value of equity for Bookscape. So I cheated. I looked at the median debt to equity ratio across book companies of 21.41%. I assumed that because Bookscape is in the book business, it has to have a debt to equity ratio similar to that. I used that debt to equity ratio in conjunction with Bookscape's tax rate to come up with the levered beta of 0.86. I used that levered beta with the riskfree rate and equity risk premium. The equity risk premium is just the US equity risk premium, because Bookscape is a New York based book store, to come up with the cost of equity in US dollar terms of 7.5%.

So if Bookscape were a public company, this is what I'd be using as its cost of equity on the assumption that it has a leverage policy very similar to public companies.

## The Diversification Catch

But here's where I run into a catch. Remember when we use beta we assume that the only risk we build into our hurdle rate is the risk that you cannot diversify away? And we get away with it because we assume that the marginal investor is well diversified? Well, remember, in the case of Bookscape, the marginal investor is the owner of Bookscape. That owner happens to have all of his or her wealth tied up in that company.

So here's a question that I'd like to think about in intuitive terms. If I use a market beta, as I have, to come up with the cost of equity for Bookscape, as I have, of 7.5%, given that the owner of Bookscape is not a diversified investor do you think I've underestimated its cost of equity or overestimated its cost of equity? Think about it for just a moment. I've counted only the risk you cannot diversify away in the beta, right? But this owner is not diversified. Therefore, he or she is going to be exposed to all of the other risks, as well. So intuitively you can already see that if you're looking at a private company, you cannot use a market beta to come up with the cost of equity because that market beta focuses only on the risk you cannot diversify away.

## Total Beta Adjustment

So you say "What do I do now?" If you remember, when I ran those regressions for individual companies I got an R squared for each company, right? The R squared tells me the proportion of the variants in each company that is explained by the market. That average R squared across book companies was about 26%. You're saying "So what?" The market beta measures the risk that a diversified investor is exposed to. That portion of the risk that's market risk, but let's say you're not diversified. You're exposed to the rest of the risks. If I can somehow expand the beta to bring in the rest of the risk I'm home free, and that's exactly what I did.

I took the market beta of 0.86 and I divided by the square root of the R squared, which happens to be the correlation, and that number works out to be about 0.51. For a typical book company, 51% of the risk is market risk and that's captured with that beta of 0.86. But what if I'm exposed to all of the risk? The plain algebra tells me that my beta will be closer to 1.68, rather than 0.86, because I'm exposed to all of that risk. Plugging in that total beta, and I'm calling it a total beta because it reflects total risk, gives me a cost of equity of almost 12%. That is what I'm going to use as my hurdle rate when I look at private businesses.

## Implications for Private vs Public Competition

So with private businesses, you have an extra step to take to come up with the cost of equity. Just in closing, though, think about what I've just done. I've given a private bookstore a much higher cost of equity than a public bookstore, right? And if they both compete in the same city, the public bookstore is going to start off with a significant advantage. You're saying, "That's not fair." Well life's not fair. If you're a private business person, you will face higher hurdle rates and therefore have to work harder just to stay in place. Nothing you can do about it, but that is something that we need to think about when we think about why private businesses get pushed out by public companies.

So at this stage, you have everything you need to come up with the beta and a cost of equity for your company, even if it's a private company. In fact, even if you're doing a public company, why don't you help a friend out? A friend, a relative, a parent who owns a private business. See if you can estimate a cost of equity for that private business. It just takes a little more work, but the mechanics and the logic remain the same.
