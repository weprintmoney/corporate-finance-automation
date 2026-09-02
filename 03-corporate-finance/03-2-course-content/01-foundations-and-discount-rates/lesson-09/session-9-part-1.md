---
title: "Session 9 Part 1 — Determinants of Beta and Regression Pitfalls"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 9 Part 1 — Determinants of Beta and Regression Pitfalls

In the last session I talked about betas as coming from regressions. Well, that's technically true, but it misses the point. Betas don't come from regressions, they come from choices you make as a company. And in this session, I'd like to start off by looking at those determinants. What are the factors that drive the beta of a company?

## Regression Beta for Tata Motors

So when you think about the regression approach to estimating betas, here's what you need to do, right? Get returns in the stock, run a regression against a market index, the slope of the line is the beta. We saw how that worked for Disney and very quickly let's apply this to the other companies in our sample.

I'll run a regression for Tata Motors against the SENSEX. I actually did not pick the SENSEX, but the Bloomberg terminal from which I printed off this page is very parochial. When asked for a beta for an Indian company, it almost automatically runs it against the SENSEX. I let it stay around the regression, and the beta that I got from the regression, the raw beta was 1.83. Based on the standard error, the 67% range on the beta is between 1.67, that's plus or minus 0.16 to 1.99.

If you look at the R squared of this regression, it's 69%. Sixty-nine percent of the risk in Tata Motors comes from the market, the remaining 31% is firm specific and diversifiable.

Let's look at the intercept. The intercept for Tata Motors is 2.28%. You subtract out the risk-free rate on a monthly basis and this is the Indian risk-free rate on a monthly base was 4% you divide by 12, that gives you the monthly risk-free rate times 1 minus beta. I get a Jensen's alpha on a monthly basis of 2.56%. If I annualize it, that gives me a 35% excess return per year. That's an astonishing Jensen's alpha. Between 2008 and 2013 Tata Motors delivered whatever you'd have expected them to deliver, adjusted for the beta plus 35.42%. Why? The acquisition of Jaguar Land Rover I think contributed a great deal, but we'll come back and take a closer look at this.

Finally, now that I have a beta, I can compute an expected return for Tata Motors just like I did for Disney. I'm doing everything in rupee, so I started with the risk-free rate of 6.57%. Remember how I got that? I start with the Indian government bond rate and netted out the default spread for India. 6.57% is my risk-free rate. My beta, in this case, is 1.83, at the point estimate, and the equity risk premium for Tata Motors reflects where it does business, 7.19%. You bring those numbers together, my rupee cost of equity, my expected return for Tata Motors is 19.73%. If that looks high, remember I'm doing everything in rupee terms, you shouldn't be surprised to see a higher number.

## Why Regression Betas Are Troubling

Now I've talked a little bit about why I find regressions troubling. Regression betas are estimates with wide ranges and regression betas can lead to game playing. Game playing in what sense? If you allowed me enough time and access to a Bloomberg terminal, I can deliver whatever beta you want for your company by changing my parameters, starting point, ending point, indices.

Just to illustrate, I took Vale. I could run a regression of Vale against a IBOVESPA, after all it's a Brazilian company, I could take the local listing. I could also run a regression of Vale's ADR against the S&P 500. I get two very different betas. With the IBOVESPA, I get a beta less than one, with the S&P 500 beta, much higher than one. You're saying, "So what?" If my intent as the Vale CFO analyst is to come up with a low hurdle rate, low cost of equity, I'm going to stick with the IBOVESPA beta. My intent is to push up the hurdle rate, I could go with a high beta, another reason to distrust betas.

In fact, building on that index of fact, let me look at Deutsche and Baidue where I just played with the indices. And the keyword here is "play" because there's really no good reason why one index should be better than the other. For Deutsche, run the regression against the DAX and the FTSE, the Euro 100. German stock or as a European stock, I get very different betas, very different intercepts, very different R squards. With Baidu, I ran the regression against the NASDAQ and I ran it against the S&P 500. Again, it's a NASDAQ listed stock, and you could argue maybe I should run it against the NASDAQ. Remember though, all of these are CAPM betas and the best index is the one that is the widest, that has the most listings on it, because you want to get as close as you can to the market portfolio.

The bottom line though is, the numbers you report for companies can be a very specific function of what choices you make on the index you use and how you run the regression.

## Stories Behind Company Betas

So you're saying, "Now what?" I don't like regression betas. In fact, I'd like to bury them. But to bury them I've got to give you an alternative. So I'm going to at least get started in the process of what drives betas by giving you a set of betas. And as I'm giving you the betas for these companies, I'm going to try to tell you a story about each company. And as I tell a story, try to collect the stories together because embedded in these stories are the fundamentals that determine beta.

So a few years ago I looked up the betas for all of these companies on a Bloomberg terminal. If you look at the very top of the list, you see Bulgari, beta of 2.45. What does Bulgari do? Produce really expensive things that nobody really needs. But that's okay. It's a very discretionary product. Companies that produce very discretionary products will have high betas.

Move down the list, you have Qwest Communications, Telecom Company. Telecom companies might not produce very discretionary products, but they have a different problem. They have lots of fixed costs and they borrow a lot of money. When you have lots of fixed cost and you borrow a lot of money, your beta for your equity is going to get pushed up, and that's what you see for Qwest.

Let's keep going down. You see a beta for Microsoft, a little higher than one but not by much. Microsoft as a company, who's beta I've been estimating every year since 1986. When I first estimated Microsoft beta as a young company, its beta was over two. Over time that beta has drifted down. Why? It's become a larger company with a wider customer base and a big cash balance, all of which push beta down.

Then I get to G.E. G.E. is a classic conglomerate in 25 to 30 different businesses. It's beta should move towards one because that's what conglomerate beta should move towards and like mutual funds. The only reason G.E.'s beta is greater than one is because they have a financing arm with a lot of debt. And debt as we said pushes up beta, so acts as a ballast.

Then you get to Exxon Mobil, Oil Company. Are oil companies exposed risk? Sure. But the risk they're exposed to is a oil price risk. When all prices go up, their earnings go up, when all prices go down, their earnings go down. Their biggest source of risk could actually occur in the opposite direction for the rest of the market. Not surprisingly, commodity companies tend to have low betas and in fact in extreme cases like Harmony Gold Mining, you could actually visualize a scenario where a company could have a negative beta. What does that mean? Adding this company to your portfolio can actually reduce risk. You're buying insurance against something. You're saying, "What am I insuring against with a gold mining company?" Probably higher inflation.

Last example is Altria, Philip Morris. Why is its beta so low? Well, if you're a company and you want a really low beta, here's my suggestion. Try to make your product or service an addiction. A little bit tough to sell less when you have an addiction. Tobacco companies will tend to have low betas.

## Start With Common Sense

That's the process by which I want you to start thinking about betas. So once you've run a regression beta, rather than take it as a fact, think about your company. Think about why your company might have a high beta or a low beta and whether the regression beta makes sense. That is the start of good sense when it comes to betas.
