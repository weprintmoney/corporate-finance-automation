---
title: "Session 5 Part 1 — Estimating the Risk-Free Rate"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Session 5 Part 1 — Estimating the Risk-Free Rate

## Why the Risk-Free Rate Matters

So now that we've talked about risk and return models of finance, let's bring our ambitions down. Before we measure the hurdle rate for a risky investment, we need know what we would make on a risk-free investment and guaranteed investment, right? So this session is all about coming up with that risk-free rate.

So to understand why the risk-free rate matters, go back to the CAPM or any other risk and return model in finance. In the CAPM, the expected return on investment is a risk-free rate plus beta times and expected risk premium, right? So to get the CAPM going I need a risk-free rate, without it I'm going to be stuck.

## Criteria for a Risk-Free Investment

So to come up with a risk-free rate, let's lay out a couple of criteria that we're going to look for to determine whether something is risk-free. So for an investment to be risk-free it has to meet two criteria. There can be no default risk in the entity issuing the security, and second, there can be no reinvestment risk.

You're saying, "What are you talking about?" Well, let's say I have a five-year time horizon. A one year table is not risk-free with a five-year time horizon because at the end of the year I've got to reinvest money at a rate I don't know today, and in two years I've got to do it again. So if I want a pure risk-free rate for a five-year period, I need a five-year government bond, right? And I have to assume the government is not default-free, but I've got to go further. A five-year government bond comes with coupons in six months, a year, or year and a half, and those have to get reinvested at rates I don't know. So if I'm a purist for a five-year time period, I would need a five-year default-free bond as my risk trader, which also means that if I'm doing an analysis of 10 years of cash flows, each cash flow will have its own risk-free rate. The present value effect of approximating might not be great, but it's still the right way to get risk-free rates.

## Time Horizon and Currency Matching

So let's lay out some broad principles on risk-free rates. If you asked me what a risk-free rate is, I would not answer the question until you tell me over what time period, because my risk-free rate over six months is going to be very different than my risk-free rate over 5 years or 10 years or 20 years. So I make things simple for you in corporate finance. In corporate finance almost everything we do is long term. You should not be dealing with tables of one-year rate, you should be dealing with longer term rates.

Second, it's got to be currency match. There is no global risk-free rate. Risk-free rates go with currencies. So if you want to know what the risk-free rate is, you got to specify the currency. Is it in U.S. dollars? Is it in euros? Is it in British pounds? Or is it in Indian rupees?

## Disney Example: U.S. Dollar Risk-Free Rate

In U.S. dollars, in November of 2013 which is when I was looking at Disney, I used the U.S. Treasury bond rate, the 10-year bond rate as my risk-free rate. Let me take that apart and explain why. I used the 10-year bond rate because much as we said in corporate finance is long-term and using a long-term risk-free rate makes more sense. Second, why the U.S. Treasury? Because I'm doing my analysis in U.S. dollars. And third, I am implicitly making the assumption when I do this that the U.S. Treasury is default-free. That rate in November of 2013 would've been 2.75% so almost every calculation you would see for Disney from this point on in November of 2013, the risk-free rate is going to be the 10-year USD bond rate.

Just as an aside, let me explain why I don't use the 30-year U.S. Treasury rate which exists. Technically, the 30-year rate might be a better rate. It's an even more long-term rate but it makes the calculation of other inputs into my calculation, the equity risk premium and the default spread, much more difficult to do. So I'm going to stay with the 10-year rate.

## Euros and Other Currencies

You say, "What if I had a different currency, say the euro?" Things don't get much more difficult. There are 12 government bonds denominated in euros. The rates are all different. You're saying, "Which one should I use?" Let's say you're analyzing a Greek company. You shouldn't be using the Greek government bond rate as your risk-free rate. Why? Because the Greek government is not default-free. I would use the German government bond rate as my risk-free rate. If I'm doing my analysis in euros no matter which country I'm doing the analysis in.

You're saying, "But I don't want to punish the company for being a Spanish company or a Greek company." Don't worry, you get plenty of chances to do it elsewhere in the computation. So if you have a default-free entity in a currency, use that rate on that default-free entity's bonds. So I can get risk-free rates in U.S. dollars, Canadian dollars, euros, Japanese yen to the extent that I can find a default-free entity. So these are my easy currencies. And you're saying, "What if I have Indian rupee, the rupiah, or pesos or rubles where there is no default-free entity?" We'll come back and talk about what to do about those more difficult currencies next.

## Next Steps for Your Company

But at least for the moment, you should have a working definition of a risk-free rate. I've assumed by this point you've thought about a company or even picked a company. If you picked a company, now is the time that you get to pick currency. We'll talk more about this. But it doesn't have to be a local currency, but if you decide to go with your local currency, the next step is to come up with a risk-free rate. If your local currency has a default-free entity like I did for the U.S. Treasury, use the government bond rate as your risk-free rate. If not, you have more work to do.
