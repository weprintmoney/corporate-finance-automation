---
title: "Alternatives to the CAPM: Part 1: Relative Risk Measures"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-1-relative.html
published: 2011-04-28
updated_source: 2011-04-30
fetched: 2026-08-27
tags:
  - The
---

# Alternatives to the CAPM: Part 1: Relative Risk Measures

_Source: [https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-1-relative.html](https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-1-relative.html) — published 2011-04-28_

The Capital Asset Pricing Model (CAPM) is almost fifty years old and it still evokes strong responses, especially from practitioners. In academia, the CAPM lives on primarily in the archives of old journals and most researchers have moved on to newer asset pricing models.  To practitioners, it represents everything that is wrong with financial theory, and beta is the cudgel that is used to beat up academics, no matter what the topic. I have never been shy about arguing the following:

a. The CAPM is a flawed model for risk and return among many flawed models.

b. The estimates of expected return that we get from the CAPM can be significantly improved if we use more information and remember basic statistics along the way. (I argue for using sector betas rather than a single regression beta.)

c. The expected returns we get from the CAPM (discount rates in valuation and corporate finance) are a small piece of overall corporate finance and valuation. In fact, removing the CAPM from my tool box will in no way paralyze me in my estimation of value.

Notwithstanding this, I understand the discomfort that people feel with the CAPM at several levels. First, by starting with the premise that risk is symmetric - the upside and downside are balanced - it already seems to concede the fight to beat the market. After all, a good investment should have more upside than downside; value investors in particular build their investment strategies around the ethos of minimizing downside risk while expanding upside potential. Second, the model's dependence upon past market prices to get a measure of risk (betas after all come from regressions) should make anyone wary: after all, markets are often volatile for no good fundamental reason. Third, the CAPM's focus on breaking down risk into diversifiable and undiversifiable risk, with only the latter being relevant for beta does not convince some, who believe that the distinction is meaningless or should not be made.

Consequently, both academics and practitioners have been on the lookout for better ways of measuring risk and estimating expected returns. In this post, which will be the first of a few, I want to look at alternatives to the CAPM that stay with its core set-up, where the risk of an investment is measured relative to the average risk investment and expected returns are derived accordingly:

E(Return) = Riskfree Rate + Beta of investment (Expected Risk Premium for all risky investments)

Note that in this set up, the riskfree rate and expected risk premium are the same for all investments in a market and that beta alone carries the burden of measuring risk. The fact that betas are scaled around one provides for a simple intuitive hook: an investment with a beta of 1.2 is 1.2 times more risky than the average investment in the market. I have extended papers on how best to estimate the [riskfree rate](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1317436) and [expected equity risk premium](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1769064).

**I. Multi Beta Models**

Contrary to conventional wisdom, which views theorists as cult followers of beta, the criticism of the CAPM in academia has been around for as long as the model itself. While the initial critiques just argued that CAPM betas did not do very well in explaining past returns, we did see two alternatives emerge by the late 1970s.

- *The Arbitrage Pricing Model*, which stays true to conventional portfolio theory, but allows for multiple (though unidentified) sources of market risk, with betas estimated against each one.

- *The Multifactor model*, which uses historical data to relate stock returns to specific macro economic variables (the level of interest rates, the slope of the yield curve, growth rate in the GDP) and estimates betas for individual companies against these macro factors.

Both models represent extensions of the CAPM, with multiple betas replacing a single market beta, with risk premiums to go with each one.

Pluses: Do better than the CAPM in explaining past return differences across investments.

Minuses: For forward looking estimates (which is what we usually need in corporate finance and valuation), the improvement over the CAPM is debatable.

Bottom line: If you don't like the CAPM because of its complexity and its assumptions about markets, you will like multi beta models even less.

**II. Market Price based Models**

The CAPM beta can be written as follows:

CAPM Beta = Correlation between stock and market * Standard deviation in returns of stock/ Standard deviation in returns of market

The instability in this estimate comes from the correlation input, which can be volatile and change dramatically from period to period. One alternative suggested by some is to dispense with the correlation entirely and to estimate the relative risk of a stock by dividing its standard deviation by the average (or median) standard deviation across all stocks. For instance, the median annualized standard deviation across all US stocks between 2008 and 2010 was 57.01%. The relative standard deviation scores for two firms - Apple and 3M - can be computed using their annualized standard deviations over the same period: Apple's standard deviation was 42.66% and 3M's standard deviation was 25.17%.

Apple's relative standard deviation = 42.66%/ 57.01% = 0.75

3M's relative standard deviation = 25.17%/57.01% = 0.44

These take the place of the CAPM betas and get used with the riskfree rate and equity risk premium to get expected returns.

Pluses: Standard deviations are easier to compute and more stable than correlations (and betas)

Minuses: No real economic rationale behind the model. Treats all risk as equivalent, whether it can be diversified away or not.

Bottom line: For those who want relative risk measures that look closer to what they would intuitively expect, it is an alternative. For those who do not like market based measures, it is more of the same.

**III. Accounting information based Models**

For those who are inherently suspicious of any market based measure, there is always accounting information that can be used to come up with a measure of risk. In particular, firms that have low debt ratios, high dividends, stable and growing accounting earnings and large cash holdings should be less risky to equity investors than firms without these characteristics. While the intuition is impeccable, converting it into an expected return can be problematic, but here are some choices:

a*. Pick one accounting ratio and create scaled risk measures around that ratio*. Thus, the median book debt to capital ratio for US companies at the start of 2011 was 51%. The book debt to capital ratio for 3M at that time 30.91%, yielding a relative risk measure of 0.61 for the company. The perils of this approach should be clear when applied to Apple, since the firm has no debt outstanding, yielding a relative risk of zero (which is an absurd result).

*b. Compute an accounting beta*: Rather than estimate a beta from market prices, an accounting beta is estimated from accounting numbers. One simple approach is to relate changes in accounting earnings at a firm to accounting earnings for the entire market. Firms that have more stable earnings than the rest of the market or whose earnings movements have nothing to do with the rest of the market will have low accounting betas. An extended version of this approach would be to estimate the accounting beta as a function of multiple accounting variables including dividend payout ratios, debt ratios, cash balances and earnings stability for the entire market. Plugging in the values for an individual company into this regression will yield an accounting beta for the firm. While this approach looks promising, here are some cautionary notes: accounting numbers are smoothed out and can hide risk and are estimated at most four times a year (as opposed to market numbers which get minute by minute updates).

Pluses: The risk is related to a company's fundamentals, which seems more in keeping with an intrinsic valuation view of the world.

Minuses: Accounting numbers can be deceptive and the estimates can have significant errors associated with them.

Bottom line: If you truly do not trust market prices, use accounting data to construct your risk measures.

The reason for the CAPM's endurance as a model is simple. It provides a way of estimating the required returns and costs of equity for individual companies at low cost, by requiring only one input: a market beta. For those who like that aspect of the model, but don't like the baggage that comes with the model, relative standard deviations and accounting betas provide an alternative. For those who like the theoretical underpinnings of the model but do not like the poor estimates that it yields, the arbitrage and multifactor models should appeal. For those who contest the very basis of the approach, I will look at alternatives in the next few posts.

**The series on alternatives to the CAPM**

[Alternatives to the CAPM: Part 1: Relative Risk Measures](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-1-relative.html)

[Alternatives to the CAPM: Part 2: Proxy Models](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-2-proxy.html)

[Alternatives to the CAPM: Part 3: Connecting cost of equity to cost of debt](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-3-connecting.html)

[Alternatives to the CAPM: Part 4: Market-implied costs of equity](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-4-market.html)

[Alternatives to the CAPM: Part 5: Risk adjusting the cash flows](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-5-risk-adjusting.html)

[Alternatives to the CAPM: Wrapping up](http://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-wrapping-up.html)
