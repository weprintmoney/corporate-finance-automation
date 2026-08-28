---
title: "Putting the D in the DCF: The Cost of Capital"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2015/01/putting-d-in-dcf-cost-of-capital.html
published: 2015-01-19
updated_source: 2015-01-19
fetched: 2026-08-27
---

# Putting the D in the DCF: The Cost of Capital

_Source: [https://aswathdamodaran.blogspot.com/2015/01/putting-d-in-dcf-cost-of-capital.html](https://aswathdamodaran.blogspot.com/2015/01/putting-d-in-dcf-cost-of-capital.html) — published 2015-01-19_

If there were a contest for the most measured number in finance, the winner would be the cost of capital. Corporate finance departments around the world compute it as an integral part of investment analysis. Appraisers estimate it as a step towards estimating intrinsic or discounted cash flow value. Analysts spend disproportionate amounts of their time working on it, though not always for the right reasons or with the right inputs. Since I have spent a significant portion of my life, writing and talking about cost of capital, it stands to reason that it is one of the numbers that I compute for all the companies in my data base at the start of every year.

**Defining the cost of capital**

There are three different ways to frame the cost of capital and each has its use. Much of the confusion about measuring and using cost of capital stem from mixing up the different definitions:

- For businesses, the cost of capital is a cost of raising financing: The first is to read the cost of capital literally as the cost of raising funding to run a business and thus build up to it by estimating the costs of raising different types of financing and the proportions used of each. This is what we do when we estimate a cost of equity, based on a beta, betas or some other risk proxy, a cost of debt, based upon what the business can borrow money at and adjusting for any tax advantages that might accrue from borrowing.

- For businesses, the cost of capital is an opportunity cost for investing in projects: The cost of capital is also an opportunity cost, i.e., the rate of return that the business can expect to make on other investments, of equivalent risk. The logic is simple. If you are considering investing in a new asset or security, you have to earn more than you could make by investing the money elsewhere. There are two subparts to this statement. The first is that it is the choices that you have today that should determine this opportunity cost, not choices that you might have had in the past. The second is that it has to be on investments of equivalent risk. Thus, the cost of capital should be higher for riskier investments than safe ones.

- For investors, the cost of capital is a discount rate to value a business: Investors looking at buying into a business are effectively buying a portfolio of investments, current and future, and to value the business, they have to make an assessment of the collective risk in the portfolio and how it may change over time. 

A good measure of cost of capital will find a way to bridge the differences between the three definitions and I believe that we can do so, with a little common sense and some data.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6WrArP74BG-BSekX3sjQDXVUir0ithfc_Hh_m27d-ZjWN2OBD-cGb-lPyS4gWSshdAujmtqpbZMM9uMFCuH2-ZIVfTzsrJLgU7qahDSeIV2PAbw-4j6Vg7_lUFkU49K9JLtsdpipHJaM/s1600/costofcapitalpicture.jpg)

For this process to yield a number to meet all three requirements for cost of capital, i.e., that it be a cost of raising funding, an opportunity cost and a required return for investors, here are the requirements:

- Investors price companies based upon a reasonable assessment of the company’s business mix (and country risk exposure) and what they can generate as expected returns on alternative choices of equivalent risk. The former requires companies to provide information on their business mixes and the latter generally is easier to do in a liquid, public market.

- A company that operates in multiple businesses and many countries cannot use a single, “company-wide” cost of capital as its hurdle rate in investments. It has to adjust the cost of capital for both the riskiness of the business in which the investment is being planned and the part of the world that it is going to be located in.

- The overall company’s cost of capital has to be a weighted average of the costs of capitals of the businesses that it operates in, and as the business mix changes, the cost of capital will, as well.

**Estimating the Cost of Capital**

Having laid the groundwork, let’s get down to specifics. If you, as an investor, are given the task of estimating the cost of capital for a company, here is the sequence of steps. First, you have to estimate the business risk in the company by taking a weighted average of the risks of the businesses that the company operates. Second, you have to adjust that risk measure for the effects of debt, which effectively magnifies your business risk exposure, and use the consolidated risk measure to estimate a cost of equity. Third, you have to bring in the cost of borrowing, net of any tax benefit, which will reflect the default risk in the company. Finally, taking a weighted average of the cost of equity and after-tax cost of debt yields a cost of capital. If you are approaching the same task as a CFO, you have to follow the same sequence to get a cost of capital for the company but you have to go further and estimate the costs of capital for the individual businesses that the company is invested in.

As someone who teaches corporate finance and valuation, I am equally interested in both sides of this estimation process and one of my objectives in providing data is to help both sides. To help companies in investment analysis, I try to estimate costs of capital by sector, in the hope that a multi-business company will be able to find the information here to build up business-specific costs of capital. While investors may also find this information useful in valuation/investment analysis, I also estimate costs of capital for individual companies, and while my data providers no longer allow me to share these company-specific costs of capital, I can still provide information on the distribution of costs of capital across companies that can be useful to investors.

***a. Cost of capital by sector***

In my data updates each year, I estimate the cost of capital, by sector, for companies both globally and classified by region (US, Europe, Japan, Emerging Markets). In making these estimates, I first begin by breaking my total sample of 41,410 companies down into 96 industry groups, some of which may be far broader than you would like to see. I prefer this broad categorization for two reasons. First, I estimate a beta for each industry group by averaging the betas of the individual companies in that group, and these estimates are more precise with larger sample sizes. Second, from a first principles perspective, I believe that since betas measure risk from a macro risk perspective, you are better served with broader categories than narrow ones. Thus, rather than estimate the beta for shrimp fishing as a business, I would rather estimate the beta for food processing businesses (assuming that the only reason that people buy shrimp is to eat them.). Once I have the industry groups, I estimate the cost of equity for each group (in US dollar terms, by using a US dollar risk free rate and a equity risk premium in US dollar terms, though the magnitude of the premium can vary across countries and regions) by using the average beta across companies in the sector. For the cost of debt, I do have a problem, since all I usually have at the industry level is a book interest rate (obtained by dividing the interest expense by the book value of debt) which is not very useful from a cost of capital perspective. I use the variance in stock prices as an indicator of the risk and use it to estimate a default spread in US dollar terms, which then allows me to compute a cost of debt. As the final step, I use the industry average debt to capital ratios (in market value terms) to compute a cost of capital; in keeping with my view that lease commitments are debt, I convert lease commitments to debt for all companies in my database:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgx428rr3G4Ra80H-8bKVU1FEiAHUigfRFuey3NizV_hMGPiO4tEmWlm5Z73oym8EjP3IfO74PmSe4sQZ5UFM9USLf5_bhpl6WMVS1H1uKaKyMmlfeXrElypX9_5Nk3RByP5Yh9Fsi3gbE/s1600/costofcapitalsector.jpg)

The results from the start of 2015 are captured in the [attached spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/waccall.xls), which includes costs of capital by sector not only for global companies, but also includes my regional estimates.

***b. Cost of Capital - By company***

As part of my data analysis, I also try to estimate the cost of capital for each of the 42,410 companies in my database. Since it is impractical to analyze each company in detail, I do have to make some simplifying assumptions.

- First, I assign each company to one primary business in estimating business risk and use the unlevered beta for that business as the beta for the company. Optimally, I would compute the unlevered beta for each company, using the mix of businesses it is in, but with my sample size and data access, it is close to impossible to do. 

- Second, I assume that the company gets all its revenues in the country in which it is incorporated and assign it the equity risk premium of that country. Thus, a Russian company’s cost of equity is computed using the Russian ERP (see my earlier post on country risk) and a German company’s cost of equity is computed based on the German ERP. I know that this violates my earlier point of multinational companies, and I would never make this assumption in building up an individual company’s cost of capital but I am afraid I have no choice with the larger sample. 

- Third, I estimate a default spread for the company by using the variance in its stock prices. It is true that some of the companies (about 4000 or about 10% of my sample) have bond ratings available on them, but the bulk of my companies do not. In addition, if the company is incorporated in a country with sovereign default risk, I add the default spread for the country on to that of the company. I also use the marginal tax rate of the country that the company is incorporated in to estimate an after-tax cost of debt. 

- Finally, to keep the numbers comparable, I compute the costs of capital for all companies in US dollars.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEju_nyiFoaQWu2FHhx41MyyKb2MSlW9Eag3ERbpEja_RnoHRqfuKgGy_vKTOEvWjIqfwc2T-oY6t6UYuoeb7K7zcRi14rRyTIhKsygNki5Lc4nbf_mr3BXHpY7nWOpOuDDThdgQgB8muxI/s1600/costofcapitalcompany.jpg)

While I cannot provide you with the company-level costs of capital, I can provide the cross sectional distribution of my estimates. As you look at companies, I hope that you can use this for perspective, i.e., in making judgments on what comprises a high, low and median cost of capital. With US companies, the cost of capital distribution across all companies is below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg79RzHLVWbZmiRVtPD9lr4Z35G4SsX09CAGJ2KUNNSIDLFtk1yPcAvYfWi16MKllvNV8Fh4lmiUlmkcQ7lVsRy7yzqM4CY8i8m-rAwI63NVTnFf2u-pBalEA04s7iadpsyEjrMGyHoINc/s1600/WACCUSchart.jpg)
*Cost of capital in US dollars: US companies in January 2015*

Thus, if you use a cost of capital of 10% in the United States, you would effectively be assuming that your company is in the 98th percentile of US companies, in terms of cost of capital. With global companies, the cost of capital distribution is as follows:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjk28T4lw_mLoHVweC4cJXCN6oNnultZ-VneMEC6SIObX-GYQGSmJeNxZzS9Y4W_RYz-TUMH7D8Hxvhzhl0OTaPPuMoVM4EqPGbz-iiXFQcHlc7eejUR1RW6jRoyBPa7-awfY56j0oKMp0/s1600/WACCglobalchart.jpg)
Cost of capital in US dollars: Global companies in January 2015

Note that I have used a larger equity risk premium and incorporated sovereign default spreads into the cost of debt, yielding a larger spread in the cost of capital. A cost of capital of 12.5% for a global company would put it in the 94th percentile of companies.

**A Cost of Capital Computation Template**

If you work in finance, you will run into the challenge of estimating the cost of capital for a company sometime during the course of the year. I hope that the datasets that I have created are useful to you in that endeavor and if you decide to use them, here is a simple template for arriving a company's cost of capital in the currency of your choice.

0
0
1
432
2469
Stern School of Business
20
5
2896
14.0

Normal
0

false
false
false

EN-US
JA
X-NONE

/* Style Definitions */
table.MsoNormalTable
{mso-style-name:"Table Normal";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-parent:"";
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-para-margin-top:0in;
mso-para-margin-right:0in;
mso-para-margin-bottom:10.0pt;
mso-para-margin-left:0in;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Cambria;
mso-ascii-font-family:Cambria;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Cambria;
mso-hansi-theme-font:minor-latin;
mso-fareast-language:JA;}
table.MsoTableGrid
{mso-style-name:"Table Grid";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-priority:59;
mso-style-unhide:no;
border:solid windowtext 1.0pt;
mso-border-alt:solid windowtext .5pt;
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-border-insideh:.5pt solid windowtext;
mso-border-insidev:.5pt solid windowtext;
mso-para-margin:0in;
mso-para-margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Cambria;
mso-ascii-font-family:Cambria;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Cambria;
mso-hansi-theme-font:minor-latin;
mso-fareast-language:JA;}

[](https://www.blogger.com/blogger.g?blogID=8152901575140311047)[Step](https://www.blogger.com/blogger.g?blogID=8152901575140311047)

Input

Measure

Comments/ Data sets

1

Risk free rate

Use the prevailing 10-year US
T.Bond rate as the risk free rate in US dollars, even if you plan to
compute the cost of capital in another currency.

Fight the urge to normalize, tweak
or otherwise mess with this rate. It is
what you can make today on a risk less investment, no matter what your views
on it being too low or high.

2

Business Risk (Unlevered beta)

Break the company down into
businesses, using an operating metric (revenues work best) and compute the
weighted unlevered beta across the businesses.

Company breakdown: In company’s
annual report or financial filings

Beta of businesses: [My unlevered betas by business](http://www.stern.nyu.edu/~adamodar/pc/datasets/betaGlobal.xls)(broad groups) or you can create your own subgroups.

3

Financial Risk (Debt to equity and
levered beta)

Lever the beta using the market
debt to equity ratio for the company today. (If you prefer to use a target
debt to equity ratio, make sure it is based on market values.

Market value of equity: Use the market capitalization as
market value of equity. 

Market value of debt: For debt, use book value as your proxy for market
value, or better still convert book value to market value.  Add[the present value of operating leases](http://www.stern.nyu.edu/~adamodar/pc/oplease.xls)
to debt.

4

Equity Risk Premium

Obtain the geographical breakdown
of the company’s revenues (or other operating metric, if you don’t like
revenues). Take a weighted average of the ERP of the countries/regions that
the company operates in.

Geographical Breakdown:  The company’s revenues will be in its
financial statements, though it is not always as clear and detailed as you
would like it to be.

ERP by country: My [ERP by country.](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

5

Cost of debt

If you can find a corporate bond
rating for your company, use it to get a default spread and a cost of debt.
If you cannot find a bond rating, estimate a bond rating for the company and
a default spread on that basis. If you are doing the latter, add a default
spread for the country to get the pre-tax cost of debt.

Bond Rating: If available, you
should be able to find it at [S&P](http://www.standardandpoors.com/ratings/en/us/) or online.

Synthetic Rating: You can use this
spreadsheet to get a [synthetic rating for your company](http://www.stern.nyu.edu/~adamodar/pc/ratings.xls).

Rating-based default spread: [My lookup table](http://www.stern.nyu.edu/~adamodar/pc/ratings.xls) of default spreads for ratings classes.

Country default spreads: [My estimates](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

6

Marginal tax rate

Multiply the pre-tax cost of debt
by (1- marginal tax rate) to get the after-tax cost

Marginal tax rate by country: [KPMG estimates of country tax rates](http://www.stern.nyu.edu/~adamodar/pc/datasets/countrytaxrates.xls)

7

Debt Ratio

Use the market values of debt and
equity (from step 3)

See step 3

8

Currency change

If you want to convert the US
dollar cost of capital into another currency, add the differential inflation
rate (between that currency and the US dollar) or better still, scale up
the  US$ cost of capital for the
difference in inflation.

The inflation rate in the US can
be estimated as the difference between the US 10-year T.Bond Rate and the US
TIPs rate. For other countries, you can use the actual inflation rate last
year as a proxy for expected inflation. 

If you are interested, I have a [spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/wacccalc.xls) that has these steps incorporated into it. Give it a shot!

**Implications**

Looking at the costs of capital across sectors and companies, there are lessons that I take away for valuation and corporate finance:

- *A rising (falling) tide lifts (lowers) all boats: *The first reaction that most analysts and CFOs will have to my estimates of the cost of capital is that they look too low, with a median value of 7.40% for US companies and 8.32% for global companies. In fact, the longer that you have been around in markets, the lower today's numbers will look like to you, because what you consider a normal cost of capital will reflect your experiences. The low costs of capital, though, are appropriate, given the level of risk free rates today.

- *The cost of capital does not (and should not) reflect all risk faced by a business*: Even if you accept the proposition that the costs of capital are lower because of low risk free rates, you may still feel that the costs of capital don't look high enough for what you view as the riskiest companies in the market. You are right but that is because the cost of capital captures risk to a diversified investor in a going concern. Consequently, it will not reflect risks that are sector-specific but not market-wide, such as the risk to a biotechnology company that its newest drug will not be approved for production. Those risks are better reflected in the expected cash flows. The cost of capital also does not reflect truncation risk, i.e., that a firm may not survive the early stages of the life cycle or an overwhelming debt burden. That risk is better captured through decision trees and probabilistic approaches.

- *Don't sweat the small stuff*: In my view, analysts spend too much time finessing and tweaking the cost of capital and not enough on the cash flows. After all, the cost of capital, even if you go with the global distribution, varies within a tight range (6% to 12%, if you use the 10th and 90th percentile) and your potential for making mistakes is therefore also restricted. In contrast, profit margins and returns on capital have a much wider distribution across companies and getting those numbers right has a much bigger pay off.

**Dataset attachments**

- Cost of capital by sector ([US](http://www.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls), [Emerging Markets](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccemerg.xls), [Europe](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccEurope.xls), [Japan](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccJapan.xls), [Global](http://www.stern.nyu.edu/~adamodar/pc/datasets/waccGlobal.xls))

- [Tax rates by country](http://www.stern.nyu.edu/~adamodar/pc/datasets/countrytaxrates.xls)

- [Ratings and default spreads](http://www.stern.nyu.edu/~adamodar/pc/ratings.xls) 

**Spreadsheet attachments**

- [Cost of capital worksheet](http://www.stern.nyu.edu/~adamodar/pc/wacccalc.xls)

**Data update blog posts**

- [An ERP Retrospective: Looking back (2014) and Looking forward (2015)](http://bit.ly/1xok8NO)

- [Country Risk, Return and Pricing: The Global Landscape in January 2015](http://bit.ly/1xMEE6n)

- [The Tax Story (in January 2015): Myths, Misconceptions and Reality Checks](http://bit.ly/1BWkcGv)

- [Putting the D in the DCF- The Cost of Capital](http://bit.ly/1BuzuU3)

- [The X Factor in Business: Excess Returns and Value](http://bit.ly/1CHMqmP)
