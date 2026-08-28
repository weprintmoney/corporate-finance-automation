---
title: "Myth 4.3: The D cannot change (over time) in a DCF"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2016/11/myth-43-d-cannot-change-over-time-in-dcf.html
published: 2016-11-04
updated_source: 2016-12-21
fetched: 2026-08-27
tags:
  - DCF Valuation
  - Discount Rates
---

# Myth 4.3: The D cannot change (over time) in a DCF

_Source: [https://aswathdamodaran.blogspot.com/2016/11/myth-43-d-cannot-change-over-time-in-dcf.html](https://aswathdamodaran.blogspot.com/2016/11/myth-43-d-cannot-change-over-time-in-dcf.html) — published 2016-11-04_

In my last post, I argued that academics and practitioners pay too much attention to discount rates in valuation and too little to cash flows. One reason for that attention may by the fear that you have only one shot at estimating the cost of equity or capital, when valuing a firm, and that once estimated, that number becomes the discount rate to use on cash flows in perpetuity. In this post, I will argue that this fear is misplaced and that the DCF approach not only allows for changing discount rates over time but requires it for most firms. 

****

**The Mechanics of Time-varying Discount Rates **

In a discounted cash flow valuation, the value of an asset is the present value of the expected cash flows, with the equation written as follows: 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXA4REu3s66fQAB5T4692HGJ95Ow4VyKkDY5qDT1iy6LEzkSVavZ0qwVTHdj1ke11PvSlUesRwAOVBlB0J1p0wo5FbM5ilWmVOBVBhPpJ0OB1RsIrqi286U_A6qnMksDUcx9-C5A6tcs4/s1600/DCFEquation.png)

Written in this form, the “r” in the denominator is the discount rate and is estimated as the cost of equity (or capital), depending on the cash flows that are being discounted. In practice, analysts seem to operate under the presumption that they get one shot at estimating these discount rates, at the start of the process, and that these discount rates are then fixed in perpetuity.  That presumption is wrong, since the DCF structure is flexible enough to allow for time varying discount rates, with the modified version of the value equation below: 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSqUexBSe-9nGyX4eEL4L6XDD9uNQSpX3b2Yo6NonEeDBo4PPQhcoASq9q3pVx3sOY-nunPQdFplOmGrKZnADt-CJ4QyAAOUrf6uhZq1boJ2NB-Y6kUMy7_bUvI-D5OCxA3jtRocdo23o/s1600/DCFEquationChangingRates.png)

Note that r1 is the discount rate for year 1, r2 is the discount rate in year 2 and so on until your get to your terminal value and the discount rate in perpetuity is rN. There is one minor computational detail which can have major valuation effects. Note that, in the presence of time varying discount rates, the way we do discounting changes. Rather than discount back each year’s cash flow at that year’s discount rate, we compute a compounded discount rate in each period. Thus, if your cost of capital is 12% in year 1, 11% in year 2 and 10% in year 3, the present value of $100 million in year 3 is as follows:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcUF1HwtESLr0GtwfWYzFltCgsynqMXURzp8EWOUaZ3aR-ZE40uTgAitdPNmUiB0b99WH-v30jgrkhqIwrsLwVh5K3cJEMxgYyNBUPoNK-MKFHyoIG1X7Lc62RtQfLZcf4wTeO78LzGpU/s1600/PV+of+100+million.png)

If this cash flow had been discounted back (by mistake) at 10% for 3 years, the present value would have been (wrongly) computed to be $75.13 million. Intuitively, you are adjusting the present value of cash flows later for the risk that you have to live through in the earlier years. 

**The Intuition for Time-varying Discount Rate **

Adjusting discount rates across time may seem like a needless complication but it is a necessary one, if you want your valuation to remain internally consistent. More specifically, if you are assuming changes in your company characteristics (growth, business mix, geographical exposure) in your cash flows, as you move through time, you should be changing the discount rate to reflect these changes. 

While this is true for all companies, the effect will be greater when you are valuing young companies or companies in transition, where you expect large changes in the company as you move through your forecast period. Thus, in my valuations of Uber in 2014 (a young growth company) and Tesla in July 2016 (a growth company in transition) & Apple in 2016 (a mature company with solid cash flows), my discount rates changed over time.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEC8-9QGjWKG2CJAZCA0etK-07TwT8y0np8Yu6TW33XIS5pD0DtR5_t670SRH5lKUYY3dEMTpzdc06-MAwyBDpOqJJWnaJR0kIP4GXzm9p0GpWEExKUTPmB9kjU8WjjZ74hXgvvjIQ5UM/s1600/DiscountRateChangeover+time.png)

How much do these changing discount rates affect the values per share? Considerably, as can be seen in the graph below where I contrast the values that I would have obtained for the three companies with my default assumption of changing discount rates with the values that I would have obtained if the discount rates had been left at the starting levels.

Value with time-varying Discount RateValue with constant discount RateEffect on value

Uber (June 2014)$5,895 $3,601 -38.91%
Tesla (July 2016)$22,364 $17,688 -20.91%
Apple (May 2016)$692,852 $633,336 -8.59%

With Uber, the effect on value is substantial, increasing the value of equity by almost 39%, with Tesla the effect is smaller (21%) and with Apple, even more muted (8.6%).

**Guidelines for Discount Rate Adjustments**

If you buy into the argument that the costs of equity and capital can change over time, it may seem like that your estimation problems have multiplied, since you now have to not only estimate the current cost of capital for a firm but costs of capital every year through your valuation. To simplify the estimation process, here is what I find works for me: 

- To estimate the cost of capital that you will use in the early years (years 1 and 2), start with the current cost of capital for the firm. That will reflect the existing business mix for the firm (in the beta), the geography of its revenues (in the equity risk premium) and the debt policy for the firm (in the cost of debt and debt ratio). 

- If the company has clearly specified plans to change its debt ratio and business mix in the near term, adjust the cost of capital for these changes in the near years (years 3-5) for these changes. If it does not, leave the cost of capital at the current level.

- The cost of capital in steady state (for terminal value) should move towards those of mature firms. If you see your firm growing across multiple businesses, that cost of capital should be that of the market (with a beta of one, a debt ratio close to the market average) but if you see it growing within only its existing business, the cost of capital should be reflecting of the industry average (reflecting the industry average beta and debt ratio). 

- In the transition period (between the near years and steady state), you should adjust the cost of capital from your near-year level to stable growth levels, using linear increments. 

PhaseForecast yearsBeta Equity Risk PremiumDebt RatioCost of debt

Start of valuationYr 1-2Reflects current business mixCurrent geography of operationsCurrent market debt ratioCurrent bond rating or default risk assessment
Build upYrs 3-5Changes in business mix (if any)Changes in geography (if any)Targeted debt ratio (if any)Default risk, given new debt ratio
TransitionYrs 6-10Move incrementally to stable period betaAdjust to stable period ERPAdjust to stable period debt ratioAdjust to stable period cost of debt
Stable growth (Steady State)Year 10 & beyondMove to 1, if company grows across businesses, or to industry average, if it stays within businessSteady state geographic exposure and equity risk premium estimates for long term.Market-average debt ratio (if growth across businesses) or industry-average debt ratio (if single business)Stable company cost of debt

One reason that I compute the costs of capital, by industry grouping, and update it each year is to have access to this information whenever I value a company. If you are interested, you can find the industry average costs of equity and capital [for US firms](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls) and [global firms](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls) on my website. 

If you open the door to adjusting discount rates for changes in company characteristics, you can also consider also bringing in changes in the macroeconomic inputs. In particular, you could allow the risk free rate and risk premiums (in the form of default spreads and equity risk premiums) to change over time, and as they do, so will your discount rate. Thus, if you believe, as many do, that risk free rates are “too low” (given fundamentals) but are wary of replacing actual rates with your estimates, you could have your cake and eat it too, by starting off with current risk free rates and adjusting those rates to what you believe are more normal levels over time. If you do so, though, you should also normalize equity risk premiums and default spreads over time. To provide an illustration, consider the cost of equity for an average-risk (beta =1_ company in US dollars in October 2016, with the US dollar risk free rate at 1.6% and the mature market equity risk premium at about 6%. 

Cost of equity = Risk free rate + Beta (ERP) = 1.6% + 1 (6%) = 7.6% 

Let’s assume that you believe that the risk free rate should be closer to 3%, given inflation and real growth today, and that you believe that the market rate will move towards this number over the next decade. Let’s also assume that you also believe that as risk free rates normalize, the equity risk premium will move back towards its average over the last decade (about 5%) The cost of equity for your company ten years from now (which you will use in your terminal value calculation) will then be 8%: 

Cost of equity in year 10 = Expected Risk free rate + Beta (ERP) = 3% + 1 (5%) = 8% 

If you are a company with substantial emerging market exposure (say in India or Brazil), you may also be adjusting the additional country risk premium that you incorporate into your cost of equity over time. 

**Conclusion **

One reason that analysts often feel helpless, when computing intrinsic value in a DCF, is because they feel that they not only have little control over the discount rate, since all the inputs come from outside, but that they are stuck with this discount rate forever. If your discount rates adjust over time to reflect changes in your company, towards industry or market averages, these rates will start to have a smaller effect on your valuations and that is not only healthy but more realistic (at least in my view).

**YouTube Video**

**
**
**Attachments**

- [Costs of equity & capital by industry: US companies](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)

- [Costs of equity & capital by industry: Global companies](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls)

**DCF Myth Posts**

Introductory Post: [DCF Valuations: Academic Exercise, Sales Pitch or Investor Tool](http://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html)

- [If you have a D(discount rate) and a CF (cash flow), you have a DCF.](http://aswathdamodaran.blogspot.com/2015/02/dcf-myth-1-if-you-have-ddiscount-rate.html)  

- [A DCF is an exercise in modeling & number crunching.](http://bit.ly/1EgfbHl) 

- [You cannot do a DCF when there is too much uncertainty.](http://aswathdamodaran.blogspot.com/2016/05/dcf-myth-3-you-cannot-do-valuation-when.html)

- It's all about D in the DCF (Myths [4.1](http://aswathdamodaran.blogspot.com/2016/11/myth-41-if-you-don-like-betas-or-modern.html), [4.2](http://aswathdamodaran.blogspot.com/2016/11/myth-42-it-all-about-d-in-dcf.html), [4.3](http://aswathdamodaran.blogspot.com/2016/11/myth-43-d-cannot-change-over-time-in-dcf.html), [4.4](http://aswathdamodaran.blogspot.com/2016/11/myth-44-ddiscount-rate-is-receptacle.html) & [4.5](http://aswathdamodaran.blogspot.com/2016/11/myth-45-dcfs-break-down-with-near-zero.html))

- The Terminal Value: Elephant in the Room! (Myths [5.1](http://aswathdamodaran.blogspot.com/2016/11/myth-51-if-you-don-believe-in-forever.html), [5.2](http://aswathdamodaran.blogspot.com/2016/11/myth-52-as-g-rto-infinity-and-beyond.html), [5.3](http://aswathdamodaran.blogspot.com/2016/11/myth-53-growth-is-good-more-growth-is.html), [5.4](http://aswathdamodaran.blogspot.com/2016/11/myth-54-negative-growth-rates-forever.html) & [5.5](http://aswathdamodaran.blogspot.com/2016/11/myth-55-terminal-value-ate-my-dcf.html))

- A DCF requires too many assumptions and can be manipulated to yield any value you want.

- A DCF cannot value brand name or other intangibles. 

- *A* DCF yields a conservative estimate of value. 

- If your DCF value changes significantly over time, there is something wrong with your valuation.

- A DCF is an academic exercise.

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
