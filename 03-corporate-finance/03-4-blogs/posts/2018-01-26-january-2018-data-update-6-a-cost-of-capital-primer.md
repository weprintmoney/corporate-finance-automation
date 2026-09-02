---
title: "January 2018 Data Update 6: A Cost of Capital Primer"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-6-cost-of.html
published: 2018-01-26
updated_source: 2018-02-06
fetched: 2026-08-27
tags:
  - Cost of capital
  - Cost of equity
---

# January 2018 Data Update 6: A Cost of Capital Primer

_Source: [https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-6-cost-of.html](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-6-cost-of.html) — published 2018-01-26_

I have long described [the cost of capital as the Swiss Army Knife of finance](http://people.stern.nyu.edu/adamodar/pdfiles/papers/costofcapital.pdf), since it shows up in so many places in finance, albeit in different forms. In corporate finance, it is not only the cost of raising funding for a business but also the hurdle rate to use in capital budgeting and an optimizing tool for capital structure and dividend policy. In valuation, it is the discount rate that we use to value a business and the only mechanism for incorporating the risk of a business into its value. Along the way, it picks up a variety of other names that are used to describe it (with my least favorite one being the WACC acronym) and gets confused or used interchangeably with the cost of equity. In short, it is not surprising that there seems to be little consensus on how to estimate the cost of capital for a business.

**The Cost of Capital: Definition**

It is unfortunate that the name that we have attached to this ubiquitous number is the cost of capital, since it seems to suggest that it is the cost of raising funding for a company. While that definition may sometimes fit, it often leads to destructive consequences, where companies that are safe and can raise equity or borrow money at low rates (and hence have a low cost of funding) think that they are adding value when they go out and take risky investments that earn more than that cost. A company that has a 5% cost of capital is not always adding value if it takes an investment that generates an 8% return, if the investment is risky enough to require a much higher return. A healthier definition of the cost of capital is to think of it as an opportunity cost, i.e., a rate of return that you (as an investor or by extension, a company that the investor has put money in) can make on an investment of equivalent risk. The key words in this definition are "equivalent risk", because that effectively eliminates the subsidy mistake that occurs when a safe company's cost of capital is used to justify taking a risky investment. This is, of course, one of the first principles of finance and it is astonishing that it is open for debate and that so many companies violate it, in their practices. If you are skeptical of my claim, consider the following manifestations of this malpractice:

- Many multi-business companies continue to have a "single" hurdle rate in capital budgeting: In [a survey of "best" practices across companies and advisors](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2686738), the authors note that almost half of all companies (and advisors) surveyed used a single cost of capital across all investments.  That is not only not good practice, but over time, it will ensure that your entire company will become a riskier company that takes bad investments. While I appreciate the work that went into this survey, I would suggest that the authors seriously reconsider using the word "best" to describe many of the horrendous practices that companies use in computing cost of capital. Looking at surveys of how companies compute costs of capital around the world, it seems clear to me that  bad practices drive out good ones, a manifestation of Gresham's law in corporate finance practice.

- In acquisitions, it is routine for companies (and bankers) to use the acquiring company's cost of capital to value the target company: While I cannot point to surveys to back up this statement, in my experience, this happens in more than 60% of acquisitions, with the logic being that it is the acquiring firm that raises the capital and that its costs should therefore be covered. The fact that will lead safe firms to find any risky firm that they look at to be cheap is glossed over. If you are waffling, let me be absolutist. Valuing a target company using an acquiring company's cost of capital is valuation malpractice, and if you do it, you should be stripped of your license to do valuation.

- Cash is viewed as a value destroying asset: If you follow GAAP or IFRS, for an asset to be categorized with cash and short term investments, it has to be invested in liquid and close to riskless assets. In the last decade, these investments, not surprisingly, have generated extraordinarily low returns, but it is true, no matter what interest rate environment you are in, that cash will earn lower returns than operating investments. There are analysts, and I use the word loosely, who compare the returns generated on cash to the cost of capital of the firm to conclude that cash is a value-destroying asset and that it should be returned. While there are legitimate arguments that can be made that companies should return cash to stockholders, this is not one of them. In fact, cash, if invested in treasury bills or commercial paper, is a value-neutral investment, earning exactly the return that you need it to earn, given its liquid, diskless status.

- A company that earns a higher return on its projects (higher ROIC) should be valued more highly than a company that earns a lower return on its projects: Without controlling for risk, this is not true. In fact, the right assessment would require comparing the ROIC to the cost of capital to estimate an excess return and a company that earns a higher positive excess return should be valued more highly than one that earns a lower excess return.

The key, then, to estimating cost of capital is to to link it directly to a risk measure that can be computed not just for entire companies but for individual projects. It is that pursuit that will drive my estimation process for cost of capital, described in the next section.

**The Cost of Capital: Estimation Process**

There are ultimately only two ways of raising funds to finance a business. One is to borrow the money (debt) and the other is to use your own money (equity). This is captured in one of my favorite corporate finance devices, the financial balance sheet:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4nRliRyjE5Mv9k7sM_Sj0BFw8O60edggDEYN_S2JnRxq8FI1RMnGmkY6Ja712a0qyKHU45wfsn-EY3GJ76aYenmbz9HdRWv3PKwrIMvWgZrRNN2I62iFpMYqHF5hdsrfmBQVoensGTZ4/s1600/finbalsh+%255Bv6.0%255D+%2528Autosaved%2529.png)

With a small private business, the debt will take the form of a bank loan and the equity will be your savings, but as businesses scale up, debt may expand to include corporate bonds and equity may transition to venture capital, private equity and publicly traded stock. The structure also allows us to boil the cost of capital down to its three ingredients: a cost of equity, an after-tax cost of debt and the weights to attach to the two.

*Cost of equity*

*The End game: *In principle, the cost of equity is the rate of return that equity investors in your business need to make to compensate for the risk that they are exposed to.

*The Practice*:  For the last few decades, corporate finance has tried, with mixed success, to devise a risk and return model to estimate the cost of equity. While these models vary in complexity and inputs, they generally share a common theme. They estimate the cost of equity to the marginal investors in the business, i.e., investors who own and trade large blocks of shares, and assume that these investors are diversified. These models all share a common structure; they start with a risk free rate and then estimate a risk premium for an investment, by measuring its relative risk (on one or more market risk factors) and the price of risk or risk premiums (for these factors). While it is the subject of substantial abuse, the capital asset pricing model continues to be the default model that most practitioners use in estimating cost of equity. The resulting inputs are shown below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2hO6s0rBlgmq0ajD7T-7_fC-8U-N3gJJV7iE-ZuKyWRvkv6p0frAlaG5tCHnpCtcsSzfjz92Jo0w8Z95-wspNN6vZvnZ4g2-cxwGc7bqzjy5HTItYMGfH39TBCvBe9Y88MXBd2OEUIJE/s1600/CAPMinputs.png)

I still use the capital asset pricing model in my valuations and I offer no apologies for doing so, since I find it simple, intuitive and at least as effective as the next best alternative models, most of which add more complexity and deliver little in results.  For those who are truly disturbed by the CAPM's limitations, there is an alternative approach worth considering that is agnostic in its assumptions about investor diversification and risk aversion. It is to back out the "implied" cost of equity for stocks within a sector and to use that implied number as the cost of equity in individual companies. If you are puzzled about what this implies, take a look at how I estimated the [implied equity risk premium for the S&P 500 in my second data post](https://aswathdamodaran.blogspot.in/2018/01/january-2017-data-update-2-buoyancy-of.html) from a couple of weeks ago and consider extending that approach to the banking index, to get an implied cost of equity for banks, and the energy sector, to estimate the cost of equity for oil companies.

*Cost of Debt*

*The End Game:* The cost of debt for a firm is the rate at which it can borrow money, long term and today. The after-tax cost of debt is this borrowing rate, adjusted for any tax benefits that accrue to borrowing money.

*The Practice*: By defining the cost of debt as a current cost of borrowing, rather than the rate at which the firm has borrowed money in the past, I have simplified my estimation problem, since the cost of debt can then be written as the sum of the riskless rate and a default spread, reflecting the company's credit risk:

Pre-tax cost of debt = Risk free Rate + Default Spread for the Company

To estimate the default spread, you can use one of three approaches, in order of ease.

- If the firm in question has corporate bonds outstanding, you can use the interest rate on the bond as your pre-tax cost of debt for the firm since it is a current, market-set rate. 

- If a firm has corporate bonds and they are not traded enough or have features that skew the interest rate, you can use the bond rating for the company to estimate a default spread. 

- If the firm has neither bonds nor a rating, a combination that holds for most companies, I would assess a ["synthetic rating"](http://www.stern.nyu.edu/~adamodar/pc/ratings.xls) for the company, based upon the strength of its financials and its capacity to repay debt.

To bring the tax benefit of debt into the after-tax cost of debt, you should use the marginal tax rate, since interest expenses save you taxes at the margin:

After-tax cost of debt = (Risk free Rate + Default Spread) (1- Marginal Tax Rate)

This cost of debt will be much lower than your cost of equity, for almost all firms.

*Debt & Equity Weights*

Market or Book? This choice, at least for me, is an easy one. The cost of capital is a measure for what it will cost you to raise money to fund the business, investment or project today, and since you can raise money only at market value, it is the only relevant number. 

Current or Target? This is an argument that often consumes analyst time and often misses the point. It is true that the debt ratio for a company can change over time, and if management does have a target, the actual debt ratio may move to the target. Unless this change is instantaneous, it is likely to occur over time and my answer to the question is to use the current debt ratio to estimate the cost of capital at the start of the investment and as the debt ratio is changed over time to the optimal, to change the cost of capital as well.

*Cross Sectional Estimation*

In choosing my estimation approach to getting cost of capital, do keep in mind that there are 43,848 firms in my sample and since looking at each one individually is out of the question, I will have to make some bludgeon assumptions (that I would not have made if I were estimating the cost of capital for an individual company). The table below summarizes my estimation choices, with the limitations of each:

table.tableizer-table {
font-size: 12px;
border: 1px solid #CCC;
font-family: Arial, Helvetica, sans-serif;
}
.tableizer-table td {
padding: 4px;
margin: 3px;
border: 1px solid #CCC;
}
.tableizer-table th {
background-color: #104E8B;
color: #FFF;
font-weight: bold;
}

Estimation Approach usedPossible limitations

Risk Free RateUS T.Bond RateCost of equity estimated in US dollars.
BetaStarted with unlevered beta for sector & levered up using company's D/E (including leases as debt)Used only the primary business that the company was in. With multi-business companies, I am missing the effect of oither businesses on beta.
ERP ERP of country that the company is incorporated in.If company operates in other countries, the ERP should be a weighted average.
Default SpreadUsed bond rating, if available, to estimate the default spread. Used interest coverage ratio to estimate ratings and default spread, otherwise.Interest coverage ratios may not capture default risk fully, Bringing in other ratios might have provided more refined estimate.
Marginal tax rateUse the statutory tax rate of the country in which the company is incorporated.If company operates in many countries, it may be able to place its debt in a country with the higher marginal tax rae.
WeightsCurrent market value of equity and debt (including leases) used for weights.Insufficient information to estimate market value of interest-bearing debt.

If you want to estimate the cost of capital, using more refined estimates (country weightings for ERP and business mixes for betas), [you are welcome to try my cost of capital calculator.](http://www.stern.nyu.edu/~adamodar/pc/wacccalculator.xls) If you are working in another currency, converting my estimates of cost of capital to an alternate currency should be a simple exercise of adding the differential inflation rate between the currency in question and the US dollar to my estimate.

**The Cost of Capital - Going Concern Concept**

There is one important caveat to add about cost of capital specifically and discount rates, in discounted cash flow valuations, more generally. In a discounted cash flow valuation, we are implicitly assuming that the business that we are valuing is a going concern that will either survive for a long time or is on its path to a specified and clearly determined liquidation point.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdwEjeoSVJQqDuT4-ugtqSbwKYuDt145WI0C5rZRYpBm6CGX3PXVp8ZZSdgUyfVju9aJWE3mL2C7jnV2lzjMHL62CCWM0TdOaa08FAuVLRaZUFK93xPYPhq6MdoWt1JsU0eTzWXcSBF4k/s1600/DCFequation.png)

So what? The reality is that business is risky and the essence of risk is that it can sometime deal out bad enough outcomes to put a company out of business. With a young start up, this may take the form of running out of cash and access to capital. With a declining company, it can be the failure to make a debt payment and the resulting financial distress. With a bank, it can take the form of a drop in regulatory capital below levels acceptable to the regulatory authorities and a shutting down of the bank. With an emerging market company, even a healthy company may see its survival threatened by a nationalization. These are risks that I call truncation risks and analysts often struggle with how best to bring them into value. One path that they try is to push discount rates (or costs of capital) higher for companies that face significant amounts of truncation risk, but discount rates are blunt instruments for dealing with this type of risk and my suggestion is that you not try to adjust them for the risk. Instead, you should consider using a decision tree front on your valuation, where you can bring in your truncation risk concerns separately from your DCF. With a distressed firm or start up, for instance, where you worry about survival risk, the decision tree will look as follows:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRsiyVOyZWOn2LMH5MSkwPPoH1x_AKQUWC4f5C_c_f9dhgUBdcjT0LXoEKyL6lpdkvb2pobg7ia-CQ7Z0nUG0-HokitwPj9UNGwsXxrRjX2136wHmsuMBWVRtXrJa6aAtQCGuMsiyf4qw/s1600/DecisionTree.png)

This will not only relieve you of the stress of trying to adjust discount rates for risk that they were never meant to convey but will allow you to focus on the truncation risk more directly. Thinking about the probability that you will not survive as a firm and what you will get, if you don't, is a much healthier exercise than arbitrarily pushing up your discount rate another 2%, because you feel the firm is riskier.

**
**

**The Cost of Capital - Perspective**

The cost of capital discussion is permeated with rules of thumb about what comprises reasonable, high or low numbers, many developed in a different time, and for a different market. These rules of thumb skew estimates, since analysts feel the urge to adjust the costs of capitals that they get from models or metrics to match their preconceptions about what they should be. It is my primary objection to the build-up approach for the cost of capital, where analysts add multiple premiums (small cap, illiquidity, company specific) to arrive at a cost of capital that matches what they would have liked to see in the first place. It is to counter this temptation that I will compute costs of capital for US and global companies and present both sector averages as well as the entire distributions for the market. 

*US Companies*

To provide perspective on what the cost of capital for the median US company will look like, start with the US 10-year T.Bond rate of 2.41% on January 1, 2018, as the risk free rate and my estimate of the implied ERP of 5.08% for the US on the same date. For an average risk stock, with a beta of one, that would translate into a cost of equity of 7.49%. Bringing in the debt ratio of 23.51% for the typical US firm and a pre-tax cost of debt of 3.91% (1.5% higher than the risk free rate), results in a cost of capital of 6.43%, if we use the marginal tax rate of 24%, post tax reform:

Cost of capital for median US firm = (2.41%+5.08%)(1-.2351)+3.91%(1-.24) (.2351) = 6.43%

Using the sector-specific debt ratios and betas yields costs of capital for US companies in individual sectors and the resulting costs of capital are reported in the table below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiolmaEe6gdFMrN1J8sBUNyHM4ZsQiSwBmAiJCMjWQMW7On6fQ04BMDeogJEsF8Hh4-SPXLFYZV2sljxI52sFCqhgqaW2V8o3n7uquwg_vRvgsg0pVBgp-vsfd6avRu0zDl9rprFBVI2nA/s1600/USSectorWACC.png)
[Download full sector cost of capital spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)

You can [download the spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)with the details of the cost of capital calculation by clicking on the link below. There is information in the company-specific costs of capital estimates that I have for 7.247 US firms in my sample that I try to capture in a histogram:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbQ4MNgTnMFT-uY6GOjvNHJWIuKWvVNogRfUTJWPdKUuUHKq6fmBE3aKHuY1twaNb8Vvqch3DdQWGEkPRjktmQlLaRl4dB8AggkNh1CKdpwHTziGUVVulTznzRsv4VOqlORP9Yj6hQsrc/s1600/USWACChistogram.png)

To the question of what comprises a high, low or average cost of capital, I would offer the deciles for the cost of capital estimation in 2018, also shown in the histogram. 

*Global Companies*

I estimate the costs of capital for global companies, in US dollars, and using the same template that I use for the US. There are two key differences. The first is that I shift from using the US ERP of 5.08% to a GDP-weighted global average ERP of 6.20%, from a US-average debt ratio of 23.51% to to a global-average debt to capital ratio of 26.67%, from a pre-tax cost of debt of 3.91% to 4.91% (reflecting country default risk) and from a marginal tax rate of 24% to a weighted average of 24.63%. The resulting cost of capital for a median global firm is higher than for the US:

Cost of capital for median global firm = (2.41%+6.20%)(1-.2667)+4.91%(1-.2463) (.2667) = 7.30%

As with the US data, I compute sector averages, using sector average betas and debt ratios and the results are summarized in the picture below:

[](https://www.blogger.com/blogger.g?blogID=8152901575140311047)[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUFRFYEtiTHXnCeq0UoLvnvRqATNsN3xQ66vqEy3pMrIz3Eu8XGlMDBDicc-TNd1vrQmc4jI0GbN_okkV5hM2ukHZH1hEqyXEWA9ARpCPwNf1abkVml8a6f9vk5wF6173P5ffqkKYjOWU/s1600/globalsectorWACC.png)
[Download full sector cost of capital spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls)

Finally, the distribution of costs of capital across global companies are captured in the histogram, with deciles specified:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOM-m1UfAm0D1eyoUktt1-OHnLWchMVFgLRp7z1OHqvOZEAAQHpMm7B3P_MQjUkyQ85MbDNagTlssMHUA02pfdlKWTbRaJyKKzg3ahkE-aef58bwqwQaDDtBTE5Lkn7Sv7p9GPBn1iTQU/s1600/GlobalWACChistogram.png)

Here again, I would use this distribution to make judgments of what a high, low or average cost of capital would look like in January 2018, and adding inflation differentials would provide analogous numbers in other currencies.

**The Conclusion**

Notwithstanding the length of this post, and the ones leading up to it, I do not believe that the cost of capital is the biggest driver of the value of companies. When you make mistakes in valuation, it is almost always true that the big mistakes are in your cash flow and growth estimates, rather than in your cost of capital. This is especially true when you value young companies, and it is one reason that I am almost casual in my choice of costs of capital in my valuation of Twitter, Uber and Snap, where I have attached costs of capital reflective of the 90th percentile in risk. It is true that as companies mature, the cost of capital becomes a more critical input, but even in these valuations, I would argue that if you are spending more than 20% to 25% of your time estimating it, you have lost your way.

**YouTube Video**

**Paper**

- [Cost of Capital - The Swiss Army Knife of Finance](http://people.stern.nyu.edu/adamodar/pdfiles/papers/costofcapital.pdf)\

**Datasets**

- [Cost of Capital, by Industry Group - US data](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)

- [Cost of Capital, by Industry Group - Global](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls)

- [Cost of Capital Calculator (Spreadsheet)](http://www.stern.nyu.edu/~adamodar/pc/wacccalculator.xls)

**Data Update Posts**

- [January 2018 Data Update 1: Numbers don't lie, or do they?](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-1-numbers-dont.html)

- [January 2018 Data Update 2: The Buoyancy of US Equities!](http://bit.ly/2FmB13Z)

- [January 2018 Data Update 3: Taxing Questions on Value](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-3-taxing.html)

- [January 2018 Data Update 4: The Currency Conundrum](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-4-currency.html)

- [January 2018 Data Update 5: Country Risk Update](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-5-country-risk.html)

- [January 2018 Data Update 6: A Cost of Capital Primer](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-6-cost-of.html)

- [January 2018 Data Update 7: Growth and Value - Investment Returns](https://aswathdamodaran.blogspot.in/2018/01/january-2016-data-update-7-growth-and.html)

- [January 2018 Data Update 8: Debt and Taxes](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-8-debt-and.html)

- [January 2018 Data Update 9: Dividends, Buybacks and Cash Holdings](https://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-9-dividends.html)

- [January 2018 Data Update 10: The Price is Right!](https://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-10-price-is.html)
