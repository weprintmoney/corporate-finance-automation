---
title: "Valuesurvey"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/valuesurvey.pdf
---

# **Valuation Approaches and Metrics: A Survey of the Theory and Evidence**

*Aswath Damodaran*

*Stern School of Business*

*November 2006*

#### **Valuation Approaches and Metrics: A Survey Article**

Valuation lies at the heart of much of what we do in finance, whether it is the study of market efficiency and questions about corporate governance or the comparison of different investment decision rules in capital budgeting. In this paper, we consider the theory and evidence on valuation approaches. We begin by surveying the literature on discounted cash flow valuation models, ranging from the first mentions of the dividend discount model to value stocks to the use of excess return models in more recent years. In the second part of the paper, we examine relative valuation models and, in particular, the use of multiples and comparables in valuation and evaluate whether relative valuation models yield more or less precise estimates of value than discounted cash flow models. In the final part of the paper, we set the stage for further research in valuation by noting the estimation challenges we face as companies globalize and become exposed to risk in multiple countries.

Valuation can be considered the heart of finance. In corporate finance, we consider how best to increase firm value by changing its investment, financing and dividend decisions. In portfolio management, we expend resources trying to find firms that trade at less than their true value and then hope to generate profits as prices converge on value. In studying whether markets are efficient, we analyze whether market prices deviate from value, and if so, how quickly they revert back. Understanding what determines the value of a firm and how to estimate that value seems to be a prerequisite for making sensible decisions.

Given the centrality of its role, you would think that the question of how best to value a business, private or public, would have been well researched. As we will show in this paper, the research into valuation models and metrics in finance is surprisingly spotty, with some aspects of valuation, such as risk assessment, being deeply analyzed and others, such as how best to estimate cash flows and reconciling different versions of models, not receiving the attention that they deserve.

### **Overview of Valuation**

Analysts use a wide spectrum of models, ranging from the simple to the sophisticated. These models often make very different assumptions about the fundamentals that determine value, but they do share some common characteristics and can be classified in broader terms. There are several advantages to such a classification - it makes it is easier to understand where individual models fit in to the big picture, why they provide different results and when they have fundamental errors in logic.

In general terms, there are four approaches to valuation. The first, discounted cashflow valuation, relates the value of an asset to the present value of expected future cashflows on that asset. The second, liquidation and accounting valuation, is built around valuing the existing assets of a firm, with accounting estimates of value or book value often used as a starting point. The third, relative valuation, estimates the value of an asset by looking at the pricing of 'comparable' assets relative to a common variable like earnings, cashflows, book value or sales. The final approach, contingent claim valuation, uses option pricing models to measure the value of assets that share option characteristics. This is what generally falls under the rubric of real options.

Since almost everything in finance can be categorized as a subset of valuation and we run the risk of ranging far from our mission, we will keep a narrow focus in this paper. In particular, we will steer away any work done on real options, since it merits its own survey article. In addition, we will keep our focus on papers that have examined the theory and practice of valuation of companies and stocks, rather than on questions of assessing risk and estimating discount rates that have consumed a great deal of attention in the literature.

#### **Discounted Cash flow Valuation**

In discounted cashflows valuation, the value of an asset is the present value of the expected cashflows on the asset, discounted back at a rate that reflects the riskiness of these cashflows. This approach gets the most play in academia and comes with the best theoretical credentials. In this section, we will look at the foundations of the approach and some of the preliminary details on how we estimate its inputs.

### *Essence of Discounted Cashflow Valuation*

We buy most assets because we expect them to generate cash flows for us in the future. In discounted cash flow valuation, we begin with a simple proposition. The value of an asset is not what someone perceives it to be worth but it is a function of the expected cash flows on that asset. Put simply, assets with high and predictable cash flows should have higher values than assets with low and volatile cash flows.

The notion that the value of an asset is the present value of the cash flows that you expect to generate by holding it is neither new nor revolutionary. While knowledge of compound interest goes back thousands of years1, the concrete analysts of present value was stymied for centuries by religious bans on charging interest on loans, which was treated as usury. In a survey article on the use of discounted cash flow in history, Parker (1968) notes that the earliest interest rate tables date back to 1340 and were prepared by Francesco Balducci Pegolotti, a Florentine merchant and politician, as part of his manuscript titled *Practica della Mercatura*, which was not officially published until

<sup>1</sup> Neugebauer, O.E.H., 1951, The Exact Sciences in Antiquity, Copenhagen, Ejnar Munksgaard. He notes that interest tables existed in Mesopotamia.

1766.2 The development of insurance and actuarial sciences in the next few centuries provided an impetus for a more thorough study of present value. Simon Stevin, a Flemish mathematician, wrote one of the first textbooks on financial mathematics in 1582 and laid out the basis for the present value rule in an appendix.3

The extension of present value from insurance and lending to corporate finance and valuation can be traced to both commercial and intellectual impulses. On the commercial side, the growth of railroads in the United States in the second half of the nineteenth century created a demand for new tools to analyze long-term investments with significant cash outflows in the earlier years being offset by positive cash flows in the later years. A civil engineer, A.M. Wellington, noted not only the importance of the time value of money but argued that the present value of future cash flows should be compared to the cost of up-front investment. <sup>4</sup> He was followed by Walter O. Pennell, an engineer of Southwestern Bell, who developed present value equations for annuities, to examine whether to install new machinery or retain old equipment. 5

The intellectual basis for discounted cash flow valuation were laid by Alfred Marshall and Bohm-Bawerk, who discussed the concept of present value in their works in the early part of the twentieth century. <sup>6</sup> In fact, Bohm-Bawerk (1903) provided an explicit example of present value calculations using the example of a house purchase with twenty annual installment payments. However, the principles of modern valuation were developed by Irving Fisher in two books that he published – *The Rate of Interest* in 1907 and *The Theory of Interest* in 1930.7 In these books, he suggested four alternative approaches for analyzing investments, that he claimed would yield the same results. He argued that when confronted with multiple investments, you should pick the investment (a) that has the highest present value at the market interest rate; (b) where the present

<sup>2</sup> Parker, R.H., 1968, Discounted Cash Flow in Historical Perspective, Journal of Accounting Research, v6, 58-71.

<sup>3</sup> Stevin, S., 1582, Tables of Interest.

<sup>4</sup> Wellington, A.M., 1887, The Economic Theory of the Location of Railways, Wiley, New York.

<sup>5</sup> Pennell, W.O., 1914, Present Worth Calculations in Engineering Studies, Journal of the Association of Engineering Societies.

<sup>6</sup> Marshall, A., 1907, Principles of Economics, Macmillan, London; Bohm-Bawerk, A. V., 1903, Recent Literature on Interest, Macmillan.

<sup>7</sup> Fisher, I., 1907, The Rate of Interest, Macmillan, New York; Fisher, I., 1930, The Theory of Interest, Macmillan, New York.

value of the benefits exceeded the present value of the costs the most; (c) with the "rate of return on sacrifice" that most exceeds the market interest rate or (d) that, when compared to the next most costly investment, yields a rate of return over cost that exceeds the market interest rate. Note that the first two approaches represent the net present value rule, the third is a variant of the IRR approach and the last is the marginal rate of return approach. While Fisher did not delve too deeply into the notion of the rate of return, other economists did. Looking at a single investment, Boulding (1935) derived the internal rate of return for an investment from its expected cash flows and an initial investment. 8 Keynes (1936) argued that the "marginal efficiency of capital" could be computed as the discount rate that makes the present value of the returns on an asset equal to its current price and that it was equivalent to Fisher's rate of return on an investment. <sup>9</sup> Samuelson (1937) examined the differences between the internal rate of return and net present value approaches and argued that rational investors should maximize the latter and not the former. <sup>10</sup> In the last 50 years, we have seen discounted cash flow models extend their reach into security and business valuation, and the growth has been aided and abetted by developments in portfolio theory.

Using discounted cash flow models is in some sense an act of faith. We believe that every asset has an intrinsic value and we try to estimate that intrinsic value by looking at an asset's fundamentals. What is intrinsic value? Consider it the value that would be attached to an asset by an all-knowing analyst with access to all information available right now and a perfect valuation model. No such analyst exists, of course, but we all aspire to be as close as we can to this perfect analyst. The problem lies in the fact that none of us ever gets to see what the true intrinsic value of an asset is and we therefore have no way of knowing whether our discounted cash flow valuations are close to the mark or not.

There are four variants of discounted cash flow models in practice, and theorists have long argued about the advantages and disadvantages of each. In the first, we discount expected cash flows on an asset (or a business) at a risk-adjusted discount rate to

<sup>8</sup> Boulding, K.E., 1935, The Theory of a Single Investment, Quarterly Journal of Economics, v49, 479-494.

<sup>9</sup> Keynes, J.M., 1936, The General Theory of Employment, Macmillan, London.

arrive at the value of the asset. In the second, we adjust the expected cash flows for risk to arrive at what are termed risk-adjusted or certainty equivalent cash flows which we discount at the riskfree rate to estimate the value of a risky asset. In the third, we value a business first, without the effects of debt, and then consider the marginal effects on value, positive and negative, of borrowing money. This approach is termed the adjusted present value approach. Finally, we can value a business as a function of the excess returns we expect it to generate on its investments. As we will show in the following section, there are common assumptions that bind these approaches together, but there are variants in assumptions in practice that result in different values.

#### *Discount Rate Adjustment Models*

Of the approaches for adjusting for risk in discounted cash flow valuation, the most common one is the risk adjusted discount rate approach, where we use higher discount rates to discount expected cash flows when valuing riskier assets, and lower discount rates when valuing safer assets. There are two ways in which we can approach discounted cash flow valuation. The first is to value the entire business, with both assetsin-place and growth assets; this is often termed firm or enterprise valuation.

![](_page_6_Diagram_4.jpeg)

The cash flows before debt payments and after reinvestment needs are termed free cash flows to the firm, and the discount rate that reflects the composite cost of financing from all sources of capital is the cost of capital.

<sup>10</sup> Samuelson, P., 1937, Some Aspects of the Pure Theory of Capital, Quarterly Journal of Economics, v51,

The second way is to just value the equity stake in the business, and this is called equity valuation.

![](_page_7_Diagram_2.jpeg)

The cash flows after debt payments and reinvestment needs are called free cash flows to equity, and the discount rate that reflects just the cost of equity financing is the cost of equity.

Note also that we can always get from the former (firm value) to the latter (equity value) by netting out the value of all non-equity claims from firm value. Done right, the value of equity should be the same whether it is valued directly (by discounting cash flows to equity a the cost of equity) or indirectly (by valuing the firm and subtracting out the value of all non-equity claims).

## *1. Equity DCF Models*

In equity valuation models, we focus our attention of the equity investors in a business and value their stake by discounting the expected cash flows to these investors at a rate of return that is appropriate for the equity risk in the company. The first set of models examined take a strict view of equity cash flows and consider only dividends to be cashflows to equity. These dividend discount models represent the oldest variant of discounted cashflow models. We then consider broader definitions of cash flows to equity, by first including stock buybacks in cash flows to equity and by then expanding out analysis to cover potential dividends or free cash flows to equity.

#### *a. Dividend Discount Model*

The oldest discounted cash flow models in practice tend to be dividend discount models. While many analysts have turned away from dividend discount models on the premise that they yield estimates of value that are far too conservative, many of the fundamental principles that come through with dividend discount models apply when we look at other discounted cash flow models.

#### *Basis for Dividend Discount Models*

When investors buy stock in publicly traded companies, they generally expect to get two types of cashflows - dividends during the holding period and an expected price at the end of the holding period. Since this expected price is itself determined by future dividends, the value of a stock is the present value of dividends through infinity.

$$\text{Value per share of stock} = \sum_{i=1}^{t=\infty} \frac{E(\text{DPS}_i)}{(1+k_e)^t}$$

where,

$$E(\text{DPS}_i) = \text{Expected dividends per share in period } t$$

ke = Cost of equity

The rationale for the model lies in the present value rule - the value of any asset is the present value of expected future cash flows discounted at a rate appropriate to the riskiness of the cash flows. There are two basic inputs to the model - expected dividends and the cost on equity. To obtain the expected dividends, we make assumptions about expected future growth rates in earnings and payout ratios. The required rate of return on a stock is determined by its riskiness, measured differently in different models - the market beta in the CAPM, and the factor betas in the arbitrage and multi-factor models. The model is flexible enough to allow for time-varying discount rates, where the time variation is caused by expected changes in interest rates or risk across time.

While explicit mention of dividend discount models did not show up in research until the last few decades, investors and analysts have long linked equity values to dividends. Perhaps the first book to explicitly connect the present value concept with dividends was *The Theory of Investment Value* by John Burr Williams (1938), where he stated the following:

*"A stock is worth the present value of all the dividends ever to be paid upon it, no more, no less... Present earnings, outlook, financial condition, and capitalization should bear upon the price of a stock only as they assist buyers and sellers in estimating future dividends."*

Williams also laid the basis for forecasting pro forma financial statements and drew a distinction between valuing mature and growth companies.11 While much of his work has become shrouded with myth, Ben Graham (1934) also made the connection between dividends and stock values, but not through a discounted valuation model. He chose to develop instead a series of screening measures that including low PE, high dividend yields, reasonable growth and low risk that highlighted stocks that would be under valued using a dividend discount model. 12

### *Variations on the Dividend Discount Model*

Since projections of dollar dividends cannot be made in perpetuity and publicly traded firms, at least in theory, can last forever, several versions of the dividend discount model have been developed based upon different assumptions about future growth. We will begin with the simplest – a model designed to value stock in a stable-growth firm that pays out what it can afford to in dividends. The value of the stock can then be written as a function of its expected dividends in the next time period, the cost of equity and the expected growth rate in dividends.

Value of Stock = 
$$\frac{\text{Expected Dividends next period}}{(\text{Cost of equity} - \text{Expected growth rate in perpetuity})}$$

Though this model has made the transition into every valuation textbook, its origins are relatively recent and can be traced to early work by David Durand and Myron Gordon. It was Durand (1957) who noted that valuing a stock with dividends growing at a constant rate forever was a variation of The Petersburg Paradox, a seminal problem in utility theory for which a solution was provided by Bernoulli in the eighteenth century.13 It was Gordon, though, who popularized the model in subsequent articles and a book, thus

<sup>11</sup> Williams, J.B., 1938, Theory of Investment Value, Fraser Publishing company (reprint).

<sup>12</sup> Dodd, D. and B. Graham, 1934, Security Analysis, McGraw Hill, New York; Graham, B., 1949, The Intelligent Investor, Collins (reprint).

<sup>13</sup> Durand, D., 1957, Growth Stocks and the St. Petersburg Paradox, Journal of Finance, v12, 348-363.

giving it the title of the Gordon growth model. <sup>14</sup> While the Gordon growth model is a simple approach to valuing equity, its use is limited to firms that are growing at stable rates that can be sustained forever. There are two insights worth keeping in mind when estimating a 'stable' growth rate. First, since the growth rate in the firm's dividends is expected to last forever, it cannot exceed the growth rate of the economy in which the firm operates. The second is that the firm's other measures of performance (including earnings) can also be expected to grow at the same rate as dividends. To see why, consider the consequences in the long term of a firm whose earnings grow 3% a year forever, while its dividends grow at 4%. Over time, the dividends will exceed earnings. On the other hand, if a firm's earnings grow at a faster rate than dividends in the long term, the payout ratio, in the long term, will converge towards zero, which is also not a steady state. Thus, though the model's requirement is for the expected growth rate in dividends, analysts should be able to substitute in the expected growth rate in earnings and get precisely the same result, if the firm is truly in steady state.

In response to the demand for more flexibility when faced with higher growth companies, a number of variations on the dividend discount model were developed over time in practice. The simplest extension is a two-stage growth model allows for an initial phase where the growth rate is not a stable growth rate and a subsequent steady state where the growth rate is stable and is expected to remain so for the long term. While, in most cases, the growth rate during the initial phase will be higher than the stable growth rate, the model can be adapted to value companies that are expected to post low or even negative growth rates for a few years and then revert back to stable growth. The value of equity can be written as the present value of expected dividends during the non-stable growth phase and the present value of the price at the end of the high growth phase, usually computed using the Gordon growth model:

$$P_0 = \sum_{t=1}^{t=n} \frac{E(\text{DPS}_t)}{(1 + \text{Cost of Equity})^t} + \frac{P_n}{(1 + \text{Cost of Equity})^n} \text{ where } P_n = \frac{E(\text{DPS}_{n+1})}{(\text{Cost of Equity} - g)}$$

where E(DPSt ) is the expected dividends per share in period t and g is the stable growth rate after n years. More complicated variants of this model allow for more than two

<sup>14</sup> Gordon, M.J., 1962, The Investment, Financing and Valuation of the Corporation, Homewood, Illinois:

stages of growth, with a concurrent increase in the number of inputs that have to be estimated to value a company, but no real change in the underlying principle that the value of a stock is the present value of the expected dividends. 15

To allow for computational simplicity with higher growth models, some researchers added constraints on other aspects of firm behavior including risk and dividend payout to derive "simpler" high growth models. For instance, the H model is a two-stage model for growth, but unlike the classical two-stage model, the growth rate in the initial growth phase is not constant but declines linearly over time to reach the stable growth rate in steady state. This model was presented in Fuller and Hsia (1984) and is based upon the assumption that the earnings growth rate starts at a high initial rate (ga) and declines linearly over the extraordinary growth period (which is assumed to last 2H periods) to a stable growth rate (gn). <sup>16</sup> It also assumes that the dividend payout and cost of equity are constant over time and are not affected by the shifting growth rates. Figure 1 graphs the expected growth over time in the H Model.

*Figure 1: Expected Growth in the H Model*

![](_page_11_Figure_4.jpeg)

Richard D. Irwin, Inc.

<sup>15</sup> The development of multi-stage dividend discount models can be attributed more to practitioners than academic researchers. For instance, Sanford Bernstein, an investment firm founded in 1967, has used a proprietary two-stage dividend discount model to analyze stocks for decades. An extensive categorization of multi-stage models is provided in Damodaran, A., 1994, Damodaran on Valuation, John Wiley, New York.

<sup>16</sup> Fuller, R.J. and C. Hsia, 1984, A Simplified Common Stock Valuation Model, Financial Analysts Journal, v40, 49-56.

The value of expected dividends in the H Model can be written as:

| $P_0 =$ | $\frac{DPS_0 * (1+g_n)}{(r-g_n)} + \frac{DPS_0 * H * (g_a - g_n)}{(r-g_n)}$ |
|---------|-----------------------------------------------------------------------------|
|---------|-----------------------------------------------------------------------------|

where DPS0 is the current dividend per share and growth is expected to decline linearly over the next 2H years to a stable growth rate of gn. This model avoids the problems associated with the growth rate dropping precipitously from the high growth to the stable growth phase, but it does so at a cost. First, the decline in the growth rate is expected to follow the strict structure laid out in the model -- it drops in linear increments each year based upon the initial growth rate, the stable growth rate and the length of the extraordinary growth period. While small deviations from this assumption do not affect the value significantly, large deviations can cause problems. Second, the assumption that the payout ratio is constant through both phases of growth exposes the analyst to an inconsistency -- as growth rates decline the payout ratio usually increases. The allowance for a gradual decrease in growth rates over time may make this a useful model for firms which are growing rapidly right now, but where the growth is expected to decline gradually over time as the firms get larger and the differential advantage they have over their competitors declines. The assumption that the payout ratio is constant, however, makes this an inappropriate model to use for any firm that has low or no dividends currently. Thus, the model, by requiring a combination of high growth and high payout, may be quite limited in its applicability 17.

# *Applicability of the Dividend Discount Model*

While many analysts have abandoned the dividend discount model, arguing that its focus on dividends is too narrow, the model does have its proponents. The dividend discount model's primary attraction is its simplicity and its intuitive logic. After all, dividends represent the only cash flow from the firm that is tangible to investors. Estimates of free cash flows to equity and the firm remain estimates and conservative investors can reasonably argue that they cannot lay claim on these cash flows. The second advantage of using the dividend discount model is that we need fewer

<sup>17</sup> Proponents of the model would argue that using a steady state payout ratio for firms that pay little or no dividends is likely to cause only small errors in the valuation.

assumptions to get to forecasted dividends than to forecasted free cashflows. To get to the latter, we have to make assumptions about capital expenditures, depreciation and working capital. To get to the former, we can begin with dividends paid last year and estimate a growth rate in these dividends. Finally, it can be argued that managers set their dividends at levels that they can sustain even with volatile earnings. Unlike cash flows that ebb and flow with a company's earnings and reinvestments, dividends remain stable for most firms. Thus, valuations based upon dividends will be less volatile over time than cash flow based valuations.

The dividend discount model's strict adherence to dividends as cash flows does expose it to a serious problem. Many firms choose to hold back cash that they can pay out to stockholders. As a consequence, the free cash flows to equity at these firms exceed dividends and large cash balances build up. While stockholders may not have a direct claim on the cash balances, they do own a share of these cash balances and their equity values should reflect them. In the dividend discount model, we essentially abandon equity claims on cash balances and under value companies with large and increasing cash balances. At the other end of the spectrum, there are also firms that pay far more in dividends than they have available in cash flows, often funding the difference with new debt or equity issues. With these firms, using the dividend discount model can generate value estimates that are too optimistic because we are assuming that firms can continue to draw on external funding to meet the dividend deficits in perpetuity.

Notwithstanding its limitations, the dividend discount model can be useful in three scenarios.

- • It establishes a baseline or floor value for firms that have cash flows to equity that exceed dividends. For these firms, the dividend discount model will yield a conservative estimate of value, on the assumption that the cash not paid out by managers will be wasted n poor investments or acquisitions.
- It yields realistic estimates of value per share for firms that do pay out their free cash flow to equity as dividends, at least on average over time. There are firms, especially in mature businesses, with stable earnings, that try to calibrate their dividends to available cashflows. At least until very recently, regulated utility companies in the United States, such as phone and power, were good examples of such firms.

- • In sectors where cash flow estimation is difficult or impossible, dividends are the only cash flows that can be estimated with any degree of precision. There are two reasons why dividend discount model remain widely used to value financial service companies. The first is that estimating capital expenditures and working capital for a bank, an investment bank or an insurance company is difficult to do.<sup>18</sup> The second is that retained earnings and book equity have real consequences for financial service companies since their regulatory capital ratios are computed on the basis of book value of equity.

In summary, then, the dividend discount model has far more applicability than its critics concede. Even the conventional wisdom that the dividend discount model cannot be used to value a stock that pays low or no dividends is wrong. If the dividend payout ratio is adjusted to reflect changes in the expected growth rate, a reasonable value can be obtained even for non-dividend paying firms. Thus, a high-growth firm, paying no dividends currently, can still be valued based upon dividends that it is expected to pay out when the growth rate declines. In practice, Michaud and Davis (1981) note that the dividend discount model is biased towards finding stocks with high dividend yields and low P/E ratios to be under valued.19 They argue that the anti-growth bias of the dividend discount model can be traced to the use of fixed and often arbitrary risk premiums and costs of equity, and suggest that the bias can be reduced or even eliminated with the use of market implied risk premiums and returns.

# *How well does the dividend discount model work?*

The true measure of a valuation model is how well it works in (i) explaining differences in the pricing of assets at any point in time and across time and (ii) how quickly differences between model and market prices get resolved.

Researchers have come to mixed conclusions on the first question, especially at it relates to the aggregate equity market. Shiller (1981) presents evidence that the volatility

<sup>18</sup> This is true for any firm whose primary asset is human capital. Accounting conventions have generally treated expenditure on human capital (training, recruiting etc.) as operating expenditures. Working capital is meaningless for a bank, at least in its conventional form since current assets and liabilities comprise much of what is on the balance sheet.

<sup>19</sup> Michaud, R.O. and P.L. Davis, 1981, Valuation Model Bias and the Scale Structure of Dividend Discount Returns, Journal of Finance, v37, 563-573.

in stock prices is far too high to be explained by variance in dividends over time; in other words, market prices vary far more than the present value of dividends.20 In attempts to explain the excess market volatility, Poterba and Summers (1988) argue that risk premiums can change over time21 and Fama and French (1988) note that dividend yields are much more variable than dividends.22 Looking at a much longer time period (1871- 2003), Foerster and Sapp (2005) find that the dividend discount model does a reasonably good job of explaining variations in the S&P 500 index, though there are systematic differences over time in how investors value future dividends. 23

To answer the second question, Sorensen and Williamson (1985) valued 150 stocks from the S&P 400 in December 1980, using the dividend discount model. <sup>24</sup> They used the difference between the market price at that time and the model value to form five portfolios based upon the degree of under or over valuation. They made fairly broad assumptions in using the dividend discount model:

- (a) The average of the earnings per share between 1976 and 1980 was used as the current earnings per share.
- (b) The cost of equity was estimated using the CAPM.
- (c) The extraordinary growth period was assumed to be five years for all stocks and the I/B/E/S consensus analyst forecast of earnings growth was used as the growth rate for this period.
- (d) The stable growth rate, after the extraordinary growth period, was assumed to be 8% for all stocks.
- (e) The payout ratio was assumed to be 45% for all stocks.

The returns on these five portfolios were estimated for the following two years (January 1981-January 1983) and excess returns were estimated relative to the S&P 500 Index using the betas estimated at the first stage. Figure 2 illustrates the excess returns earned

<sup>20</sup> Shiller, R., 1981, Do Stock Prices Move Too Much to be Justified by Subsequent Changes in

Dividends? American Economic Review, v71, 421-436. <sup>21</sup> Poterba, J., and L. Summers, 1988, Mean reversion in stock prices: evidence and implications, Journal

of Financial Economics, v22, 27-59. <sup>22</sup> Fama, E. and K. French, 1988, Dividend Yields and Expected Stock Returns, Journal of Financial

Economics 22, 3-25. <sup>23</sup> Foerster, S.R. and S.G. Sapp, 2005, Dividends and Stock Valuation: <sup>A</sup> Study of the Nineteenth to the

Twenty-first Century, Working Paper, University of Western Ontario. <sup>24</sup> Sorensen, E.H. and D.A. Williamson, 1985, Some Evidence on the Value of the Dividend Discount

by the portfolio that was undervalued by the dividend discount model relative to both the market and the overvalued portfolio.

![](_page_16_Figure_3.jpeg)

The undervalued portfolio had a positive excess return of 16% per annum between 1981 and 1983, while the overvalued portfolio had a negative excess return of almost 20% per annum during the same time period. In the long term, undervalued (overvalued) stocks from the dividend discount model outperform (under perform) the market index on a riskadjusted basis. However, this result should be taken with a grain of salt, given that the dividend discount model tends to find stocks with high dividend yields and low PE ratios to be under valued, and there is well established empirical evidence showing that stocks with those characteristics generate excess returns, relative to established risk and return models in finance. In other words, it is unclear how much of the superior performance attributed to the dividend discount model could have been replicated with a far simpler strategy of buying low PE stocks with high dividend yields.

#### *b. Extended Equity Valuation Models*

In the dividend discount model, we implicitly assume that firms pay out what they can afford to as dividends. In reality, though, firms often choose not to do so. In some cases, they accumulate cash in the hope of making investments in the future. In other cases, they find other ways, including buybacks, of returning cash to stockholders. Extended equity valuation models try to capture this cash build-up in value by considering the cash that could have been paid out in dividends rather than the actual dividends.

#### *Dividends versus Potential Dividends*

Fama and French (2001) report that only 20.8% of firms paid dividends in 1999, compared with 66.5% in 1978 and find that only a portion of the decline can be attributed to changes in firm characteristics; there were more small cap, high growth firms in 1999 than in 1978. After controlling for differences, they conclude that firms became less likely to pay dividends over the period. 25

The decline in dividends over time has been attributed to a variety of factors. DeAngelo, DeAngelo and Skinner (2004) argue that aggregate dividends paid by companies has not decreased and that the decreasing dividends can be traced to smaller firms that are uninterested in paying dividends.26 Baker and Wurgler (2004) provide a behavioral rationale by pointing out that the decrease in dividends over time can be attributed to an increasing segment of investors who do not want dividends. <sup>27</sup> Hoberg and Prabhala (2005) posit that the decrease in dividends is because of an increase in risk, by noting that increases in idiosyncratic risk (rather than dividend clientele) explain the drop in dividends. <sup>28</sup> Notwithstanding the reasons, the gap between dividends paid and potential dividends has increased over time both in the aggregate and for individual firms, creating a challenge to those who use dividend discount models.

<sup>25</sup> Fama, E.F. and K.R. French, 2001, 2001, Disappearing dividends: Changing firm characteristics or lower propensity to pay?, Journal of Financial Economics 60, 3–44.

<sup>26</sup> DeAngelo, H., L. DeAngelo, and D. Skinner, 2004, Are dividends disappearing? Dividend concentration and the consolidation of earnings, Journal of Financial Economics, v72, 425–456.

<sup>27</sup> Baker, M., and J. Wurgler, 2004a, Appearing and disappearing dividends: The link to catering incentives, Journal of Financial Economics 73, 271–288. Baker, M., and J. Wurgler 2004b, A catering theory of dividends, The Journal of Finance 59, 1125–1165.

<sup>28</sup> Hoberg, G. and N.R. Prabhala, 2005, Disappearing Dividends: The Importance of idiosyncratic risk and the irrelevance of catering, Working Paper, University of Maryland.

One fix for this problem is to replace dividends in the dividend discount models with potential dividends, but that raises an estimation question: How do we best estimate potential dividends? There are three suggested variants. In the first, we extend our definition of cash returned to stockholders to include stock buybacks, thus implicitly assuming that firms that accumulate cash by not paying dividends return use them to buy back stock. In the second, we try to compute the cash that could have been paid out as dividends by estimating the residual cash flow after meeting reinvestment needs and making debt payments. In the third, we either accounting earnings or variants of earnings as proxies for potential dividends.

#### *Buybacks as Dividends*

One reason for the fall of the dividend discount model from favor has been the increased use of stock buybacks as a way of returning cash to stockholders. A simple response to this trend is to expand the definition of dividends to include stock buybacks and to value stocks based on this composite number. In recent years, firms in the United States have increasingly turned to stock buybacks as a way of returning cash to stockholders. Figure 3 presents the cumulative amounts paid out by firms in the form of dividends and stock buybacks from 1989 to 2002.

![](_page_18_Figure_5.jpeg)

The trend towards stock buybacks is very strong, especially in the 1990s. By early 2000, more cash was being returned to stockholders in stock buybacks than in conventional dividends.

What are the implications for the dividend discount model? Focusing strictly on dividends paid as the only cash returned to stockholders exposes us to the risk that we might be missing significant cash returned to stockholders in the form of stock buybacks. The simplest way to incorporate stock buybacks into a dividend discount model is to add them on to the dividends and compute a modified payout ratio:

Modified dividend payout ratio = Net Income Dividends + Stock Buybacks

While this adjustment is straightforward, the resulting ratio for any year can be skewed by the fact that stock buybacks, unlike dividends, are not smoothed out. In other words, a firm may buy back \$ 3 billion in stock in one year and not buy back stock for the next 3 years. Consequently, a much better estimate of the modified payout ratio can be obtained by looking at the average value over a four or five year period. In addition, firms may sometimes buy back stock as a way of increasing financial leverage. If this is a concern, we could adjust for this by netting out new debt issued from the calculation above:

| Modified dividend payout = $\frac{\text{Dividends} + \text{Stock Buybacks} - \text{Long Term Debt issues}}{\text{Net Income}}$ |
|--------------------------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------------------------|

Damodaran (2006) presents this extension to the basic dividend discount model and argues that it works well in explaining the market prices of companies that follow a policy of returning cash over regular intervals in the form of stock buybacks. 29

# *Free Cash Flow to Equity (FCFE) Model*

The free cash flow to equity model does not represent a radical departure from the traditional dividend discount model. In fact, one way to describe a free cash flow to equity model is that it represents a model where we discount potential dividends rather than actual dividends. Damodaran (1994) a measure of free cash flow to equity that captures the cash flow left over all reinvestment needs and debt payments:

FCFE = Net Income + Depreciation - Capital Expenditures – Change in non-cash Working Capital – (New Debt Issued – Debt repayments)

Practitioners have long used variants of free cash flow to equity to judge the attractiveness of companies as investments. Buffett, for instance, has argued that investors should judge companies based upon what he called "owner's earnings", which he defined to be cash flows left over after capital expenditures and working capital needs, a measure of free cash flow to equity that ignores cash flows from debt. 30

When we replace the dividends with FCFE to value equity, we are doing more than substituting one cash flow for another. We are implicitly assuming that the FCFE will be paid out to stockholders. There are two consequences.

- 1. There will be no future cash build-up in the firm, since the cash that is available after debt payments and reinvestment needs is paid out to stockholders each period.
- 2. The expected growth in FCFE will include growth in income from operating assets and not growth in income from increases in marketable securities. This follows directly from the last point.

How does discounting free cashflows to equity compare with the modified dividend discount model, where stock buybacks are added back to dividends and discounted? You can consider stock buybacks to be the return of excess cash accumulated largely as a consequence of not paying out their FCFE as dividends. Thus, FCFE represent a smoothed out measure of what companies can return to their stockholders over time in the form of dividends and stock buybacks.

The FCFE model treats the stockholder in a publicly traded firm as the equivalent of the owner in a private business. The latter can lay claim on all cash flows left over in the business after taxes, debt payments and reinvestment needs have been met. Since the free cash flow to equity measures the same for a publicly traded firm, we are assuming that stockholders are entitled to these cash flows, even if managers do not choose to pay them out. In essence, the FCFE model, when used in a publicly traded firm, implicitly assumes that there is a strong corporate governance system in place. Even if stockholders cannot force managers to return free cash flows to equity as dividends, they can put pressure on managers to ensure that the cash that does not get paid out is not wasted.

<sup>29</sup> Damodaran, A. 2006, Damodaran on Valuation, Second Edition, John Wiley and Sons, New York.

<sup>30</sup> Hagstrom, R., 2004, The Warren Buffett Way, John Wiley, New York.

As with the dividend discount model, there are variations on the free cashflow to equity model, revolving around assumptions about future growth and reinvestment needs. The constant growth FCFE model is designed to value firms that are growing at a stable rate and are hence in steady state. The value of equity, under the constant growth model, is a function of the expected FCFE in the next period, the stable growth rate and the required rate of return.

$$P_0 = \frac{\text{Expected FCFE}_1}{\text{Cost of Equity - Stable Growth Rate}}$$

The model is very similar to the Gordon growth model in its underlying assumptions and works under some of the same constraints. The growth rate used in the model has to be less than or equal to the expected nominal growth rate in the economy in which the firm operates. The assumption that a firm is in steady state also implies that it possesses other characteristics shared by stable firms. This would mean, for instance, that capital expenditures, relative to depreciation, are not disproportionately large and the firm is of 'average' risk. Damodaran (1994, 2002) examines two-stage and multi-stage versions of these models with the estimation adjustments that have to be made as growth decreases over time. The assumptions about growth are similar to the ones made by the multi-stage dividend discount model, but the focus is on FCFE instead of dividends, making it more suited to value firms whose dividends are significantly higher or lower than the FCFE. In particular, it gives more realistic estimates of value for equity for high growth firms that are expected to have negative cash flows to equity in the near future. The discounted value of these negative cash flows, in effect, captures the effect of the new shares that will be issued to fund the growth during the period, and thus indirectly captures the dilution effect of value of equity per share today.

### *Earnings Models*

The failure of companies to pay out what they can afford to in dividends and the difficulties associated with estimating cash flows has led some to argue that firms are best valued by discounting earnings or variants of earnings. Ohlson (1995) starts with the dividend discount model but adds an overlay of what he terms a "clean surplus" relation, where the goodwill on the balance sheet represents the present value of future abnormal earnings. He goes on to show that the value of a stock can be written in terms of its book value and capitalized current earnings, adjusted for dividends. <sup>31</sup> Feltham and Ohlson (1995) build on the same argument to establish a relationship between value and earnings. <sup>32</sup> Penman and Sougiannis (1997) also argue that GAAP earnings can be substituted for dividends in equity valuation, as long as analysts reduce future earnings and book value to reflect dividend payments.33 Since these models are built as much on book value as they are on earnings, we will return to consider them in the context of accounting valuation models.

While it is possible, on paper, to establish the equivalence of earnings-based and dividend discount models, if done right, the potential for double counting remains high with the former. In particular, discounting earnings as if they were cash flows paid out to stockholders while also counting the growth that is created by reinvesting those earnings will lead to the systematic overvaluation of stocks. In one of the more egregious examples of this double counting, Glassman and Hassett (2000) assumed that equity was close to risk free in the long term and discounted earnings as cash flows, while counting on long term earnings growth set equal to nominal GDP growth, to arrive at the conclusion that the Dow Jones should be trading at three times its then prevailing level. 34

### *Potential Dividend versus Dividend Discount Models*

The FCFE model can be viewed as an alternative to the dividend discount model. Since the two approaches sometimes provide different estimates of value for equity, it is worth examining when they provide similar estimates of value, when they provide different estimates of value and what the difference tells us about the firm.

There are two conditions under which the value from using the FCFE in discounted cashflow valuation will be the same as the value obtained from using the dividend discount model. The first is the obvious one, where the dividends are equal to the FCFE. There are firms that maintain a policy of paying out excess cash as dividends

<sup>31</sup>Ohlson, J. 1995, Earnings, Book values and Dividends in Security Valuation, Contemporary Accounting Research, v11, 661-687.

<sup>32</sup>Feltham, G. and J. Ohlson. 1995. Valuation and Clean Surplus Accounting of Operation and Financial Activities, Contemporary Accounting Research*,* v11, 689-731.

<sup>33</sup> Penman, S. and T. Sougiannis, 1997. The Dividend Displacement Property and the Substitution of Anticipated Earnings for Dividends in Equity Valuation, The Accounting Review, v72, 1-21.

<sup>34</sup> Glassman, J. and K. Hassett, 2000, Dow 36,000: The New Strategy for Profiting from the Coming Rise in the Stock Market, Three Rivers Press.

either because they have pre-committed to doing so or because they have investors who expect this policy of them. The second condition is more subtle, where the FCFE is greater than dividends, but the excess cash (FCFE - Dividends) is invested in fairly priced assets (i.e. assets that earn a fair rate of return and thus have zero net present value). For instance, investing in financial assets that are fairly priced should yield a net present value of zero. To get equivalent values from the two approaches, though, we have to keep track of accumulating cash in the dividend discount model and add it to the value of equity. Damodaran (2006) provides an illustration of this equivalence. 35

There are several cases where the two models will provide different estimates of value. First, when the FCFE is greater than the dividend and the excess cash either earns below-market interest rates or is invested in negative net present value assets, the value from the FCFE model will be greater than the value from the dividend discount model. There is reason to believe that this is not as unusual as it would seem at the outset. There are numerous case studies of firms, which having accumulated large cash balances by paying out low dividends relative to FCFE, have chosen to use this cash to overpay on acquisitions. Second, the payment of dividends less than FCFE lowers debt-equity ratios and may lead the firm to become under levered, causing a loss in value. In the cases where dividends are greater than FCFE, the firm will have to issue either new stock or debt to pay these dividends or cut back on its investments, leading to at least one of three negative consequences for value. If the firm issues new equity to fund dividends, it will face substantial issuance costs that decrease value. If the firm borrows the money to pay the dividends, the firm may become over levered (relative to the optimal) leading to a loss in value. Finally, if paying too much in dividends leads to capital rationing constraints where good projects are rejected, there will be a loss of value (captured by the net present value of the rejected projects). There is a third possibility and it reflects different assumptions about reinvestment and growth in the two models. If the same growth rate used in the dividend discount and FCFE models, the FCFE model will give a higher value than the dividend discount model whenever FCFE ar e higher than dividends and a lower value when dividends exceed FCFE. In reality, the growth rate in FCFE should be different from the growth rate in dividends, because the free cash flow to equity is assumed to be paid out to stockholders. In general, when firms

<sup>35</sup> Damnodaran, A,, 2006, Damodaran on Valuation (Second edition), John Wiley & Sons, New York.

pay out much less in dividends than they have available in FCFE, the expected growth rate and terminal value will be higher in the dividend discount model, but the year-toyear cash flows will be higher in the FCFE model.

When the value using the FCFE model is different from the value using the dividend discount model, with consistent growth assumptions, there are two questions that need to be addressed - What does the difference between the two models tell us? Which of the two models is the appropriate one to use in evaluating the market price? The more common occurrence is for the value from the FCFE model to exceed the value from the dividend discount model. The difference between the value from the FCFE model and the value using the dividend discount model can be considered one component of the value of controlling a firm - it measures the value of controlling dividend policy. In a hostile takeover, the bidder can expect to control the firm and change the dividend policy (to reflect FCFE), thus capturing the higher FCFE value. As for which of the two values is the more appropriate one for use in evaluating the market price, the answer lies in the openness of the market for corporate control. If there is a sizable probability that a firm can be taken over or its management changed, the market price will reflect that likelihood and the appropriate benchmark to use is the value from the FCFE model. As changes in corporate control become more difficult, either because of a firm's size and/or legal or market restrictions on takeovers, the value from the dividend discount model will provide the appropriate benchmark for comparison.

# *2. Firm DCF Models*

The alternative to equity valuation is to value the entire business. The value of the firm is obtained by discounting the free cashflow to the firm at the weighted average cost of capital. Embedded in this value are the tax benefits of debt (in the use of the after-tax cost of debt in the cost of capital) and expected additional risk associated with debt (in the form of higher costs of equity and debt at higher debt ratios).

# *Basis for Firm Valuation Models*

In the cost of capital approach, we begin by valuing the firm, rather than the equity. Netting out the market value of the non-equity claims from this estimate yields the value of equity in the firm. Implicit in the cost of capital approach is the assumption that the cost of capital captures both the tax benefits of borrowing and the expected

bankruptcy costs. The cash flows discounted are the cash flows to the firm, computed as if the firm had no debt and no tax benefits from interest expenses.

The origins of the firm valuation model lie in one of corporate finance's most cited papers by Miller and Modigliani (1958) where they note that the value of a firm can be written as the present value of its after-tax operating cash flows:36

| Value of firm = | $\sum_{i=1}^{I-\infty} \frac{E(X_i - I_i)}{(1 + \text{Cost of Capital})^i}$ |
|-----------------|-----------------------------------------------------------------------------|
|-----------------|-----------------------------------------------------------------------------|

where  $X_t$  is the after-tax operating earnings and  $I_t$  is the investment made back into the firm's assets in year  $t$ . The focus of that paper was on capital structure, with the argument being that the cost of capital would remain unchanged as debt ratio changed in a world with no taxes, default risk and agency issues. While there are varying definitions of the expected after-tax operating cash flow in use, the most common one is the free cash flow to the firm, defined as follows:

Free Cash Flow to Firm = After-tax Operating Income – (Capital Expenditures – Depreciation) – Change in non-cash Working Capital

In essence, this is a cash flow after taxes and reinvestment needs but before any debt payments, thus providing a contrast to free cashflows to equity that are after interest payments and debt cash flows.

There are two things to note about this model. The first is that it is general enough to survive the relaxing of the assuming of financing irrelevance; in other words, the value of the firm is still the present value of the after-tax operating cash flows in a world where the cost of capital changes as the debt ratio changes. Second, while it is a widely held preconception that the cost of capital approach requires the assumption of a constant debt ratio, the approach is flexible enough to allow for debt ratios that change over time. In fact, one of the biggest strengths of the model is the ease with which changes in the financing mix can be built into the valuation through the discount rate rather than through the cash flows.

The most revolutionary and counter intuitive idea behind firm valuation is the notion that equity investors and lenders to a firm are ultimately partners who supply capital to the firm and share in its success. The primary difference between equity and

<sup>36</sup>Modigliani, F. and M. Miller, 1958, The Cost of Capital, Corporation Finance and the Theory of Investment, American Economic Review, v48, 261-297.

debt holders in firm valuation models lies in the nature of their cash flow claims – lenders get prior claims to fixed cash flows and equity investors get residual claims to remaining cash flows.

#### *Variations on firm valuation models*

As with the dividend discount and FCFE models, the FCFF model comes in different forms, largely as the result of assumptions about how high the expected growth is and how long it is likely to continue. As with the dividend discount and FCFE models, a firm that is growing at a rate that it can sustain in perpetuity – a stable growth rate – can be valued using a stable growth mode using the following equation:

$$\text{Value of firm} = \frac{\text{FCF}_1}{\text{WACC} - g_n}$$

where,

FCFF1 = Expected FCFF next year

WACC = Weighted average cost of capital

gn = Growth rate in the FCFF (forever)

There are two conditions that need to be met in using this model, both of which mirror conditions imposed in the dividend discount and FCFE models. First, the growth rate used in the model has to be less than or equal to the growth rate in the economy – nominal growth if the cost of capital is in nominal terms, or real growth if the cost of capital is a real cost of capital. Second, the characteristics of the firm have to be consistent with assumptions of stable growth. In particular, the reinvestment rate used to estimate free cash flows to the firm should be consistent with the stable growth rate. Implicit in the use of a constant cost of capital for a growing firm is the assumption that the debt ratio of the firm is held constant over time. The implications of this assumption were examined in Miles and Ezzel (1980), who noted that the approach not only assumed tax savings that would grow in perpetuity but that these tax savings were, in effect, being discounted as the unlevered cost of equity to arrive at value. 37

Like all stable growth models, this one is sensitive to assumptions about the expected growth rate. This sensitivity is accentuated, however, by the fact that the

<sup>37</sup> Miles, J. and J.R. Ezzell, 1980, The weighted average cost of capital, perfect capital markets and project life: A clarification, Journal of Financial and Quantitative Analysis, v40, 1485-1492.

discount rate used in valuation is the WACC, which is lower than the cost of equity for most firms. Furthermore, the model is sensitive to assumptions made about capital expenditures relative to depreciation. If the inputs for reinvestment are not a function of expected growth, the free cashflow to the firm can be inflated (deflated) by reducing (increasing) capital expenditures relative to depreciation. If the reinvestment rate is estimated from the return on capital, changes in the return on capital can have significant effects on firm value.

Rather than break the free cash flow model into two-stage and three-stage models and risk repeating what was said earlier, we present the general version of the model in this section. The value of the firm, in the most general case, can be written as the present value of expected free cashflows to the firm.

$$\text{Value of Firm} = \sum_{t=1}^{t=\infty} \frac{\text{FCF}_t}{(1 + \text{WACC})^t}$$

### FCFF<sub>t</sub> = Free Cashflow to firm in year t

where,

WACC = Weighted average cost of capital

If the firm reaches steady state after n years and starts growing at a stable growth rate gn after that, the value of the firm can be written as:

Value of Operating Assets of the firm = 
$$\sum_{i=1}^{t=n} \frac{\text{FCFF}_i}{(1 + \text{WACC})^i} + \frac{[\text{FCFF}_{n+1}/(\text{WACC} - g_n)]}{(1 + \text{WACC})^n}$$

Since the cash flows used are cash flows from the operating assets, the cost of capital that is used should reflect only the operating risk of the company. It also follows that the present value of the cash flows obtained by discounting the cash flows at the cost of capital will measure the value of only the operating assets of the firm (which contribute to the operating income). Any assets whose earnings are not part of operating income have not been valued yet. The McKinsey books on valuation have provided extensive

coverage both of the estimation questions associated with discounted cash flow valuation and the link between value and corporate financial decisions.38

To get from the value of operating assets to the value of equity, we have to first incorporate the value of non-operating assets that are owned by the firm and then subtract out all non-equity claims that may be outstanding against the firm. Non-operating assets include all assets whose earnings are not counted as part of the operating income. The most common of the non-operating assets is cash and marketable securities, which can often amount to billions at large corporations and the value of these assets should be added on to the value of the operating assets. In addition, the operating income from minority holdings in other companies is not included in the operating income and FCFF; we therefore need to value these holdings and add them on to the value of the operating assets. Finally, the firm may own idle and unutilized assets that do not generate earnings or cash flows. These assets can still have value and should be added on to the value of the operating assets. The non-equity claims that have to be subtracted out include not only all debt, but all capitalized leases as well as unfunded pension plan and health care obligations. Damodaran (2006) contains extensive discussions of the adjustments that have to be made to arrive at equity value and further still at equity value per share. 39

### *Firm versus Equity Valuation Models*

This firm valuation model, unlike the dividend discount model or the FCFE model, values the firm rather than equity. The value of equity, however, can be extracted from the value of the firm by subtracting out the market value of outstanding debt. Since this model can be viewed as an alternative way of valuing equity, two questions arise - Why value the firm rather than equity? Will the values for equity obtained from the firm valuation approach be consistent with the values obtained from the equity valuation approaches described in the previous section?

The advantage of using the firm valuation approach is that cashflows relating to debt do not have to be considered explicitly, since the FCFF is a pre-debt cashflow, while they have to be taken into account in estimating FCFE. In cases where the leverage is

<sup>38</sup> Copeland, T.E., T. Koller and J. Murrin, 1990, Valuation: Measuring and Managing the Value of Companies, John Wiley and Sons (first three editions) and Koller, T., M. Goedhart and D. Wessels, 2005, Valuation: Measuring and Managing the Value of Companies, John Wiley and Sons (Fourth Edition).

<sup>39</sup> Damodaran, A., 2006, Damodaran on Valuation, Second Edition, John Wiley and Sons, New York.

expected to change significantly over time, this is a significant saving, since estimating new debt issues and debt repayments when leverage is changing can become increasingly difficult, the further into the future you go. The firm valuation approach does, however, require information about debt ratios and interest rates to estimate the weighted average cost of capital.

The value for equity obtained from the firm valuation and equity valuation approaches will be the same if you make consistent assumptions about financial leverage.

Getting them to converge in practice is much more difficult. Let us begin with the simplest case – a no-growth, perpetual firm. Assume that the firm has \$166.67 million in earnings before interest and taxes and a tax rate of 40%. Assume that the firm has equity with a market value of \$600 million, with a cost of equity of 13.87% debt of \$400 million and with a pre-tax cost of debt of 7%. The firm's cost of capital can be estimated.

Cost of capital = 
$$(13.87\% \left( \frac{600}{1000} \right) + (7\%) \left( 1 - 0.4 \right) \left( \frac{400}{1000} \right) = 10\%$$

| Value of the firm = $\frac{\text{EBIT}(1-t)}{\text{Cost of capital}} = \frac{166.67(1-0.4)}{0.10} = \$1,000$ |
|--------------------------------------------------------------------------------------------------------------|
|--------------------------------------------------------------------------------------------------------------|

Note that the firm has no reinvestment and no growth. We can value equity in this firm by subtracting out the value of debt.

Value of equity = Value of firm – Value of debt = \$ 1,000 - \$400 = \$ 600 million

Now let us value the equity directly by estimating the net income:

Net Income = (EBIT – Pre-tax cost of debt \* Debt) (1-t) = (166.67 - 0.07\*400) (1- 0.4) = 83.202 million

The value of equity can be obtained by discounting this net income at the cost of equity:

Value of equity = 
$$\frac{\text{Net Income}}{\text{Cost of equity}} = \frac{83.202}{0.1387} = \$ 600 \text{ million}$$

Even this simple example works because of the following assumptions that we made implicitly or explicitly during the valuation.

- 1. The values for debt and equity used to compute the cost of capital were equal to the values that we obtained in the valuation. Notwithstanding the circularity in reasoning – you need the cost of capital to obtain the values in the first place – it indicates that a cost of capital based upon market value weights will not yield the

same value for equity as an equity valuation model, if the firm is not fairly priced in the first place.

- 2. There are no extraordinary or non-operating items that affect net income but not operating income. Thus, to get from operating to net income, all we do is subtract out interest expenses and taxes.
- 3. The interest expenses are equal to the pre-tax cost of debt multiplied by the market value of debt. If a firm has old debt on its books, with interest expenses that are different from this value, the two approaches will diverge.

If there is expected growth, the potential for inconsistency multiplies. We have to ensure that we borrow enough money to fund new investments to keep our debt ratio at a level consistent with what we are assuming when we compute the cost of capital.

#### *Certainty Equivalent Models*

While most analysts adjust the discount rate for risk in DCF valuation, there are some who prefer to adjust the expected cash flows for risk. In the process, they are replacing the uncertain expected cash flows with the certainty equivalent cashflows, using a risk adjustment process akin to the one used to adjust discount rates.

### *Misunderstanding Risk Adjustment*

At the outset of this section, it should be emphasized that many analysts misunderstand what risk adjusting the cash flows requires them to do. There are some who consider the cash flows of an asset under a variety of scenarios, ranging from best case to catastrophic, assign probabilities to each one, take an expected value of the cash flows and consider it risk adjusted. While it is true that bad outcomes have been weighted in to arrive at this cash flow, it is still an expected cash flow and is not risk adjusted. To see why, assume that you were given a choice between two alternatives. In the first one, you are offered \$ 95 with certainty and in the second, you will receive \$ 100 with probability 90% and only \$50 the rest of the time. The expected values of both alternatives is \$95 but risk averse investors would pick the first investment with guaranteed cash flows over the second one.

If this argument sounds familiar, it is because it is a throwback to the very beginnings of utility theory. In one of the most widely cited thought experiments in economics, Nicholas Bernoulli proposed a hypothetical gamble that updated would look

something like this: He would flip a coin once and would pay you a dollar if the coin came up tails on the first flip; the experiment would stop if it came up heads. If you won the dollar on the first flip, though, you would be offered a second flip where you could double your winnings if the coin came up tails again. The game would thus continue, with the prize doubling at each stage, until you lost. How much, he wanted to know, would you be willing to pay to partake in this gamble? This gamble, called the St. Petersburg Paradox, has an expected value of infinity but no person would be willing to pay that much. In fact, most of us would pay only a few dollars to play this game. In that context, Bernoulli unveiled the notion of a certainty equivalent, a guaranteed cash flow that we would accept instead of an uncertain cash flow and argued that more risk averse investors would settle for lower certainty equivalents for a given set of uncertain cash flows than less risk averse investors. In the example given in the last paragraph, a risk averse investor would have settled for a guaranteed cash flow of well below \$95 for the second alternative with an expected cash flow of \$95.40

The practical question that we will address in this section is how best to convert uncertain expected cash flows into guaranteed certainty equivalents. While we do not disagree with the notion that it should be a function of risk aversion, the estimation challenges remain daunting.

# *Utility Models: Bernoulli revisited*

The first (and oldest) approach to computing certainty equivalents is rooted in the utility functions for individuals. If we can specify the utility function of wealth for an individual, we are well set to convert risky cash flows to certainty equivalents for that individual. For instance, an individual with a log utility function would have demanded a certainty equivalent of \$79.43 for the risky gamble presented in the last section (90% chance of \$ 100 and 10% chance of \$ 50):

Utility from gamble = .90 ln(100) + .10 ln(50) = 4.5359

Certainty Equivalent = 
$$\exp^{4.5359} = \$93.30$$

<sup>40</sup> Bernoulli, D., 1738, Exposition of a New Theory on the Measurement of Risk. Translated into English in Econometrica, January 1954.

The certainty equivalent of \$93.30 delivers the same utility as the uncertain gamble with an expected value of \$95. This process can be repeated for more complicated assets, and each expected cash flow can be converted into a certainty equivalent. 41

One quirk of using utility models to estimate certainty equivalents is that the certainty equivalent of a positive expected cash flow can be negative. Consider, for instance, an investment where you can make \$ 2000 with probability 50% and lose \$ 1500 with probability 50%. The expected value of this investment is \$ 250 but the certainty equivalent may very well be negative, with the effect depending upon the utility function assumed.

There are two problems with using this approach in practice. The first is that specifying a utility function for an individual or analyst is very difficult, if not impossible, to do with any degree of precision. In fact, most utility functions that are well behaved (mathematically) do not seem to explain actual behavior very well. The second is that, even if we were able to specify a utility function, this approach requires us to lay out all of the scenarios that can unfold for an asset (with corresponding probabilities) for every time period. Not surprisingly, certainty equivalents from utility functions have been largely restricted to analyzing simple gambles in classrooms.

# *Risk and Return Models*

A more practical approach to converting uncertain cash flows into certainty equivalents is offered by risk and return models. In fact, we would use the same approach to estimating risk premiums that we employ while computing risk adjusted discount rates but we would use the premiums to estimate certainty equivalents instead.

Certainty Equivalent Cash flow = Expected Cash flow/ (1 + Risk Premium in Risk-adjusted Discount Rate)

Assume, for instance, that Google has a risk-adjusted discount rate of 13.45%, based upon its market risk exposure and current market conditions; the riskfree rate used was 4.25%. Instead of discounting the expected cash flows on the stock at 13.45%, we would

<sup>41</sup> Gregory, D.D., 1978, Multiplicative Risk Premiums, Journal of Financial and Quantitative Analysis, v13, 947-963. This paper derives certainty equivalent functions for quadratic, exponential and gamma distributed utility functions and examines their behavior.

decompose the expected return into a risk free rate of 4.25% and a compounded risk premium of 8.825%. 42

Compounded Risk Premium = 
$$\frac{(1 + \text{Risk adjusted Discount Rate})}{(1 + \text{Riskfree Rate})} - 1 = \frac{(1.1345)}{(1.0425)} - 1 = .08825$$

If the expected cash flow in years 1 and 2 are \$ 100 million and \$ 120 million respectively, we can compute the certainty equivalent cash flows in those years:

Certainty Equivalent Cash flow in year 1 = \$ 100 million/1.08825 = \$ 91.89 million

Certainty Equivalent Cash flow in year 2 = \$120 million/ 1.088252 = \$ 101.33 million

This process would be repeated for all of the expected cash flows and it has two effects.

Formally, the adjustment process for certainty equivalents can be then written more formally as follows (where the risk adjusted return is r and the riskfree rate is rf ):43

$$\text{CE}(\text{CF}_i) = \alpha_i \text{E}(\text{CF}_i) = \frac{(1+r_f)^t}{(1+r)^t} \text{E}(\text{CF}_t)$$

This adjustment has two effects. The first is that expected cash flows with higher uncertainty associated with them have lower certainty equivalents than more predictable cash flows at the same point in time. The second is that the effect of uncertainty compounds over time, making the certainty equivalents of uncertain cash flows further into the future lower than uncertain cash flows that will occur sooner.

# *Cashflow Haircuts*

A far more common approach to adjusting cash flows for uncertainty is to "haircut" the uncertain cash flows subjectively. Thus, an analyst, faced with uncertainty, will replace uncertain cash flows with conservative or lowball estimates. This is a weapon commonly employed by analysts, who are forced to use the same discount rate for projects of different risk levels, and want to even the playing field. They will haircut the cash flows of riskier projects to make them lower, thus hoping to compensate for the failure to adjust the discount rate for the additional risk.

<sup>42</sup> A more common approximation used by many analysts is the difference between the risk adjusted discount rate and the risk free rate. In this case, that would have yielded a risk premium of 9.2% (13.45% - 4.25% = 9.20%)

<sup>43</sup> Robichek, A.A. and S. C. Myers, 1966, Conceptual Problems in the Use of Risk Adjusted Discount Rates, Journal of Finance, v21, 727-730.

In a variant of this approach, there are some investors who will consider only those cashflows on an asset that are predictable and ignore risky or speculative cash flows when valuing the asset. When Warren Buffet expresses his disdain for the CAPM and other risk and return models, and claims to use the riskfree rate as the discount rate, we suspect that he can get away with doing so because of a combination of the types of companies he chooses to invest in and his inherent conservatism when it comes to estimating the cash flows.

While cash flow haircuts retain their intuitive appeal, we should be wary of their usage. After all, gut feelings about risk can vary widely across analysts looking at the same asset; more risk averse analysts will tend to haircut the cashflows on the same asset more than less risk averse analysts. Furthermore, the distinction we drew between diversifiable and market risk when developing risk and return models can be completely lost when analysts are making intuitive adjustments for risk. In other words, the cash flows may be adjusted downwards for risk that will be eliminated in a portfolio. The absence of transparency about the risk adjustment can also lead to the double counting of risk, especially when the analysis passes through multiple layers of analysis. To provide an illustration, after the first analyst looking at a risky investment decides to use conservative estimates of the cash flows, the analysis may pass to a second stage, where his superior may decide to make an additional risk adjustment to the already risk adjusted cash flows.

# *Risk Adjusted Discount Rate or Certainty Equivalent Cash Flow*

Adjusting the discount rate for risk or replacing uncertain expected cash flows with certainty equivalents are alternative approaches to adjusting for risk, but do they yield different values, and if so, which one is more precise? The answer lies in how we compute certainty equivalents. If we use the risk premiums from risk and return models to compute certainty equivalents, the values obtained from the two approaches will be the same. After all, adjusting the cash flow, using the certainty equivalent, and then discounting the cash flow at the riskfree rate is equivalent to discounting the cash flow at a risk adjusted discount rate. To see this, consider an asset with a single cash flow in one

year and assume that r is the risk-adjusted cash flow, rf is the riskfree rate and RP is the compounded risk premium computed as described earlier in this section.

| Certainty Equivalent Value = | CE                  | E(CF)                     | E(CF)                     | E(CF)                     |
|------------------------------|---------------------|---------------------------|---------------------------|---------------------------|
|                              | $\frac{1}{(1+r_f)}$ | $\frac{1}{(1+RP)(1+r_f)}$ | $\frac{(1+r_f)}{(1+r_f)}$ | $\frac{(1+r_f)}{(1+r_f)}$ |

This analysis can be extended to multiple time periods and will still hold.<sup>44</sup> Note, though that if the approximation for the risk premium, computed as the difference between the risk-adjusted return and the risk free rate, had been used, this equivalence will no longer hold. In that case, the certainty equivalent approach will give lower values for any risky asset and the difference will increase with the size of the risk premium.

Are there other scenarios where the two approaches will yield different values for the same risky asset? The first is when the risk free rates and risk premiums change from time period to time period; the risk-adjusted discount rate will also then change from period to period. Robichek and Myers, in the paper we referenced earlier, argue that the certainty equivalent approach yields more precise estimates of value in this case. The other is when the certainty equivalents are computed from utility functions or subjectively, whereas the risk-adjusted discount rate comes from a risk and return model. The two approaches can yield different estimates of value for a risky asset. Finally, the two approaches deal with negative cash flows differently. The risk-adjusted discount rate discounts negative cash flows at a higher rate and the present value becomes less negative as the risk increases. If certainty equivalents are computed from utility functions, they can yield certainty equivalents that are negative and become more negative as you increase risk, a finding that is more consistent with intuition. 45

The biggest dangers arise when analysts use an amalgam of approaches, where the cash flows are adjusted partially for risk, usually subjectively and the discount rate is also adjusted for risk. It is easy to double count risk in these cases and the risk adjustment to value often becomes difficult to decipher.

<sup>44</sup> The proposition that risk adjusted discount rates and certainty equivalents yield identical net present values is shown in the following paper: Stapleton, R.C., 1971, Portfolio Analysis, Stock Valuation and Capital Budgeting Decision Rules for Risky Projects, Journal of Finance, v26, 95-117.

<sup>45</sup> Beedles, W.L., 1978, Evaluating Negative Benefits, Journal of Financial and Quantitative Analysis, v13, 173-176.

#### *Excess Return Models*

The model that we have presented in this section, where expected cash flows are discounted back at a risk-adjusted discount rate is the most commonly used discounted cash flow approach but there are variants. In the excess return valuation approach, we separate the cash flows into excess return cash flows and normal return cash flows. Earning the risk-adjusted required return (cost of capital or equity) is considered a normal return cash flow but any cash flows above or below this number are categorized as excess returns; excess returns can therefore be either positive or negative. With the *excess return valuation* framework, the value of a business can be written as the sum of two components:

Value of business = Capital Invested in firm today + Present value of excess return cash flows from both existing and future projects

If we make the assumption that the accounting measure of capital invested (book value of capital) is a good measure of capital invested in assets today, this approach implies that firms that earn positive excess return cash flows will trade at market values higher than their book values and that the reverse will be true for firms that earn negative excess return cash flows.

# *Basis for Models*

Excess return models have their roots in capital budgeting and the net present value rule. In effect, an investment adds value to a business only if it has positive net present value, no matter how profitable it may seem on the surface. This would also imply that earnings and cash flow growth have value only when it is accompanied by excess returns, i.e., returns on equity (capital) that exceed the cost of equity (capital). Excess return models take this conclusion to the logical next step and compute the value of a firm as a function of expected excess returns.

While there are numerous versions of excess return models, we will consider one widely used variant, which is economic value added (EVA) in this section. The economic value added (EVA) is a measure of the surplus value created by an investment or a portfolio of investments. It is computed as the product of the "excess return" made on an investment or investments and the capital invested in that investment or investments.

Economic Value Added = (Return on Capital Invested – Cost of Capital) (Capital

Invested) = After-tax operating income – (Cost of Capital) (Capital Invested)

Economic value added is a simple extension of the net present value rule. The net present value of the project is the present value of the economic value added by that project over its life. 46

$$\text{NPV} = \sum_{t=1}^{t=n} \frac{\text{EVA}_t}{(1+k_c)^t}$$

where EVAt is the economic value added by the project in year t and the project has a life of n years and kc is the cost of capital.

This connection between economic value added and NPV allows us to link the value of a firm to the economic value added by that firm. To see this, let us begin with a simple formulation of firm value in terms of the value of assets in place and expected future growth. 47

Firm Value = Value of Assets in Place + Value of Expected Future Growth

Note that in a discounted cash flow model, the values of both assets in place and expected future growth can be written in terms of the net present value created by each component.

$$\text{Firm Value} = \text{Capital Invested}_{\text{Assets in Place}} + \text{NPV}_{\text{Assets in Place}} + \sum_{t=1}^{t=\infty} \text{NPV}_{\text{Future Projects}, t}$$

Substituting the economic value added version of net present value into this equation, we get:

$$\text{Firm Value} = \text{Capital Invested}_{\text{Assets in Place}} + \sum_{t=1}^{t=\infty} \frac{\text{EVA}_{t, \text{Assets in Place}}}{(1 + k_c)} + \sum_{t=1}^{t=\infty} \frac{\text{EVA}_{t, \text{Future Projects}}}{(1 + k_c)}$$

Thus, the value of a firm can be written as the sum of three components, the capital invested in assets in place, the present value of the economic value added by these assets and the expected present value of the economic value that will be added by future investments.48

<sup>46</sup> This is true, though, only if the expected present value of the cash flows from depreciation is assumed to be equal to the present value of the return of the capital invested in the project. A proof of this equality can be found in Damodaran, A, 1999, Value Enhancement: Back to Basics, Contemporary Finance Digest, v2, 5-51.

<sup>47</sup> Brealey, R.A. and S. C. Myers, 2003, Principles of Corporate Finance (Seventh Edition), McGraw-Hill Irwin.

<sup>48</sup> Brealery, A., 2004, Investment Valuation, Second Edition, John Wiley & Sons, New York.

#### *Measuring Economic Value Added*

The definition of EVA outlines three basic inputs we need for its computation the return on capital earned on investments, the cost of capital for those investments and the capital invested in them. In measuring each of these, we will make many of the same adjustments we discussed in the context of discounted cash flow valuation. Stewart (1991) and Young and O'Byrne (2000) extensively cover the computation of economic value added in their books on the topic. 49

How much *capital is invested* in existing assets? One obvious answer is to use the market value of the firm, but market value includes capital invested not just in assets in place but in expected future growth50. Since we want to evaluate the quality of assets in place, we need a measure of the capital invested in these assets. Given the difficulty of estimating the value of assets in place, it is not surprising that we turn to the book value of capital as a proxy for the capital invested in assets in place. The book value, however, is a number that reflects not just the accounting choices made in the current period, but also accounting decisions made over time on how to depreciate assets, value inventory and deal with acquisitions. The older the firm, the more extensive the adjustments that have to be made to book value of capital to get to a reasonable estimate of the market value of capital invested in assets in place. Since this requires that we know and take into account every accounting decision over time, there are cases where the book value of capital is too flawed to be fixable. Here, it is best to estimate the capital invested from the ground up, starting with the assets owned by the firm, estimating the market value of these assets and cumulating this market value. To evaluate the return on this invested capital, we need an estimate of the *after-tax operating income* earned by a firm on these investments. Again, the accounting measure of operating income has to be adjusted for operating leases, R&D expenses and one-time charges to compute the return on capital. The third and final component needed to estimate the economic value added is the *cost of capital*. In keeping with arguments both in the investment analysis and the discounted cash flow valuation sections, the cost of capital should be estimated based upon the

<sup>49</sup> Stewart , G. B. (1991), The Quest for Value. The EVA Management Guide. Harper Business; Young, S.D and S.F. OByrne, 2000, EVA and Value-Based Management, McGraw Hill,

<sup>50</sup> As an illustration, computing the return on capital at Google using the market value of the firm, instead of book value, results in a return on capital of about 1%. It would be a mistake to view this as a sign of poor investments on the part of the firm's managers.

market values of debt and equity in the firm, rather than book values. There is no contradiction between using book value for purposes of estimating capital invested and using market value for estimating cost of capital, since a firm has to earn more than its market value cost of capital to generate value. From a practical standpoint, using the book value cost of capital will tend to understate cost of capital for most firms and will understate it more for more highly levered firms than for lightly levered firms. Understating the cost of capital will lead to overstating the economic value added.

In a survey of practices of firms that used economic value added, Weaver (2001) notes that firms make several adjustments to operating income and book capital in computing EVA, and that the typical EVA calculation involves 19 adjustments from a menu of between 9 and 34 adjustments. In particular, firms adjust book value of capital and operating income for goodwill, R&D and leases, before computing return on capital. 51

### *Variants on Economic Value Added*

There are several variants on economic value added that build on excess returns. While they share the same basic foundation – that value is created by generating excess returns on investments – they vary in how excess returns are computed.

- In Economic Profit, the excess return is defined from the perspective of equity investors and thus is based on net income and cost of equity, rather than after-tax operating income and cost of capital

Economic Profit = Net Income – Cost of Equity \* Book Value of Equity

Many of the papers that we referenced in the context of earnings-based valuation models, especially by Ohlson, are built on this theme. We will examine these models in the context of accounting based valuations later in this paper. 52

- In Cash Flow Return on Investment or CFROI models, there are two significant differences. The first is that the return earned on investments is computed not based on accounting earnings but on after-tax cash flow. The second is that both returns and the cost of capital are computed in real terms rather than nominal terms. Madden

<sup>51</sup> Weaver, S. C., 2001, Measuring Economic Value Added: A Survey of the Practices of EVA Proponents, Journal of Applied Finance, Fall/Winter, pp. 7-17.

(1998) provides an extensive analysis of the CFROI approach and what he perceives as its advantages over conventional accounting-based measures.53

While proponents of each measure claim its superiority, they agree on far more than they disagree on. Furthermore, the disagreements are primarily in which approach computes the excess return earned by a firm best, rather than on the basic premise that the value of a firm can be written in terms of its capital invested and the present value of its excess return cash flows.

#### *Equivalence of Excess Return and DCF Valuation Models*

It is relatively simple to show that the discounted cash flow value of a firm should match the value that you obtain from an excess return model, if you are consistent in your assumptions about growth and reinvestment. In particular, excess return models are built around a link between reinvestment and growth; in other words, a firm can generate higher earnings in the future only by reinvesting in new assets or using existing assets more efficiently. Discounted cash flow models often do not make this linkage explicit, even though you can argue that they should. Thus, analysts will often estimate growth rates and reinvestment as separate inputs and not make explicit links between the two.

Illustrating that discounted cash flow models and excess return models converge when we are consistent about growth and reinvestment is simple. The equivalence of discounted cash flow firm valuations and EVA valuations is shown in several papers: Fernandez (2002), Hartman (2000) and Shrieves and Wachowicz (2000).54 In a similar vein, Feltham and Ohlson (1995), Penman (1998) and Lundholm and O'Keefe (2001) all provide proof that equity excess return models converge on equity discounted cash flow models. 55

<sup>52</sup> Ohlson, J. 1995, Earnings, Book values and Dividends in Security Valuation, Contemporary Accounting Research, v11, 661-687.

<sup>53</sup> Madden. B.L., 1998, CFROI Cash Flow Return on Investment Valuation: A Total System Approach to Valuing a Firm, Butterworth-Heinemann.

<sup>54</sup> Fernandez, P., 2002, Three Residual Income Valuation Models and Discounted Cash Flow Valuation, Working Paper, IESE Business School; Hartman, J. C., 2000, On the Equivalence of Net Present Value and Economic Value Added as Measures of a Project's Economic Worth, *The Engineering Economist,* v45, 158-165.*;* Shrieves, R.E. and J.M. Wachowicz, 2000, Free Cash Flow, Economic Value Added and Net Present Value: A Reconciliation of Variations of Discounted Cash Flow Valuation, Working Paper, University of Tennessee.

<sup>55</sup> Feltham, G. and J. Ohlson, 1995, Valuation and Clean Surplus Accounting of Operation and Financial

The model values can diverge because of differences in assumptions and ease of estimation. Penman and Sourgiannis (1998) compared the dividend discount model to excess return models and concluded that the valuation errors in a discounted cash flow model, with a ten-year horizon, significantly exceeded the errors in an excess return model. <sup>56</sup> They attributed the difference to GAAP accrual earnings being more informative than either cash flows or dividends. Francis, Olson and Oswald (1999) concurred with Penman and also found that excess return models outperform dividend discount models.57 Courteau, Kao and Richardson (2001) argue that the superiority of excess return models in these studies can be attributed entirely to differences in the terminal value calculation and that using a terminal price estimated by Value Line (instead of estimating one) results in dividend discount models outperforming excess return models. 58

### *Adjusted Present Value Models*

In the *adjusted present value (APV) approach*, we separate the effects on value of debt financing from the value of the assets of a business. In contrast to the conventional approach, where the effects of debt financing are captured in the discount rate, the APV approach attempts to estimate the expected dollar value of debt benefits and costs separately from the value of the operating assets.

## *Basis for APV Approach*

In the APV approach, we begin with the value of the firm without debt. As we add debt to the firm, we consider the net effect on value by considering both the benefits and the costs of borrowing. In general, using debt to fund a firm's operations creates tax

Activities, Contemporary Accounting Research*,* v11, 689-731; Penman, S.H., 1998, A Synthesis of Equity Valuation Techniques and the Terminal Value Calculation for the Dividend Discount Model, Review of Accounting Studies, *v*2, 303-323; Lundholm, R., and T. O'Keefe. 2001. Reconciling value estimates from the discounted cash flow model and the residual income model. Contemporary Accounting Research*, v*18, 311-35.

<sup>56</sup> Penman, S. and T. Sougiannis. 1998. A Comparison of Dividend, Cash Flow, and Earnings Approaches to Equity Valuation, Contemporary Accounting Research, v15*,* 343-383.

<sup>57</sup> Francis, J., P. Olsson, and D. Oswald. 2000. Comparing the Accuracy and Explainability of Dividend, Free Cash Flow and Abnormal Earnings Equity Value Estimates. Journal of Accounting Research, v38, 45- 70.

<sup>58</sup> Courteau, L., J. Kao and G.D. Richardson, 2001, The Equivalence of Dividend, Cash Flow and Residual Earnings Approaches to Equity Valuation Employing Ideal Terminal Value Calculations, Contemporary Accounting Research, v18 ,625–661.

benefits (because interest expenses are tax deductible) on the plus side and increases bankruptcy risk (and expected bankruptcy costs) on the minus side. The value of a firm can be written as follows:

Value of business = Value of business with 100% equity financing + Present value of Expected Tax Benefits of Debt – Expected Bankruptcy Costs

The first attempt to isolate the effect of tax benefits from borrowing was in Miller and Modigliani (1963), where they valued the present value of the tax savings in debt as a perpetuity using the cost of debt as the discount rate.59 The adjusted present value approach, in its current form, was first presented in Myers (1974) in the context of examining the interrelationship between investment and financing decisions. <sup>60</sup>

Implicitly, the adjusted present value approach is built on the presumption that it is easier and more precise to compute the valuation impact of debt in absolute terms rather than in proportional terms. Firms, it is argued, do not state target debt as a ratio of market value (as implied by the cost of capital approach) but in dollar value terms.

### *Measuring Adjusted Present Value*

In the adjusted present value approach, we estimate the value of the firm in three steps. We begin by estimating the value of the firm with no leverage. We then consider the present value of the interest tax savings generated by borrowing a given amount of money. Finally, we evaluate the effect of borrowing the amount on the probability that the firm will go bankrupt, and the expected cost of bankruptcy.

The first step in this approach is the estimation of the value of the unlevered firm. This can be accomplished by valuing the firm as if it had no debt, i.e., by discounting the expected free cash flow to the firm at the unlevered cost of equity. In the special case where cash flows grow at a constant rate in perpetuity, the value of the firm is easily computed.

Value of Unlevered Firm = 
$$\frac{\text{FCFF}_0(1+g)}{\rho_u - g}$$

<sup>59</sup> Modigliani, F. and M. Miller (1963), Corporate Income Taxes and the Cost of Capital: A Correction, American Economic Review, v53*,* 433-443.

<sup>60</sup> Myers, S., 1974, Interactions in Corporate Financing and Investment Decisions—Implications for Capital Budgeting, Journal of Finance, v29,1-25.

where  $FCF_0$  is the current after-tax operating cash flow to the firm,  $\rho_u$  is the unlevered cost of equity and  $g$  is the expected growth rate. In the more general case, we can value the firm using any set of growth assumptions we believe are reasonable for the firm. The inputs needed for this valuation are the expected cashflows, growth rates and the unlevered cost of equity.

The second step in this approach is the calculation of the expected tax benefit from a given level of debt. This tax benefit is a function of the tax rate of the firm and is discounted to reflect the riskiness of this cash flow.

Value of Tax Benefits = 
$$\sum_{t=1}^{t=\infty} \frac{\text{Tax Rate}_t * \text{Interest Rate}_t * \text{Debt}_t}{(1+r)^t}$$

There are three estimation questions that we have to address here. The first is what tax rate to use in computing the tax benefit and whether than rate can change over time. The second is the dollar debt to use in computing the tax savings and whether that amount can vary across time. The final issue relates to what discount rate to use to compute the present value of the tax benefits. In the early iterations of APV, the tax rate and dollar debt were viewed as constants (resulting in tax savings as a perpetuity) and the pre-tax cost of debt was used as the discount rate leading to a simplification of the tax benefit value:

Value of Tax Benefits = 
$$(\text{Tax Rate})(\text{Debt})$$
  
 $= t_c D$ 

$$= \frac{(\text{Tax Rate})(\text{Cost of Debt})(\text{Debt})}{\text{Cost of Debt}}$$

Subsequent adaptations of the approach allowed for variations in both the tax rate and the dollar debt level, and raised questions about whether it was appropriate to use the cost of debt as the discount rate. Fernandez (2004) argued that the value of tax benefits should be computed as the difference between the value of the levered firm, with the interest tax savings, and the value of the same firm without leverage.<sup>61</sup> Consequently, he arrives at a much higher value for the tax savings than the conventional approach, by a multiple of the unlevered firm's cost of equity to the cost of debt. Cooper and Nyborg (2006) argue

<sup>61</sup> Fernandez, P., P., 2004, The value of tax shields is not equal to the present value of the tax shields, Journal of Financial Economics, v73, 145-165.

that Fernandez is wrong and that the value of the tax shield is the present value of the interest tax savings, discounted back at the cost of debt.62

The third step is to evaluate the effect of the given level of debt on the default risk of the firm and on expected bankruptcy costs. In theory, at least, this requires the estimation of the probability of default with the additional debt and the direct and indirect cost of bankruptcy. If  $\pi_a$  is the probability of default after the additional debt and BC is the present value of the bankruptcy cost, the present value of expected bankruptcy cost can be estimated.

PV of Expected Bankruptcy cost = (Probability of Bankruptcy)(PV of Bankruptcy Cost) = 
$$\pi_a BC$$

This step of the adjusted present value approach poses the most significant estimation problem, since neither the probability of bankruptcy nor the bankruptcy cost can be estimated directly. There are two basic ways in which the probability of bankruptcy can be estimated indirectly. One is to estimate a bond rating, as we did in the cost of capital approach, at each level of debt and use the empirical estimates of default probabilities for each rating. The other is to use a statistical approach to estimate the probability of default, based upon the firm's observable characteristics, at each level of debt. The bankruptcy cost can be estimated, albeit with considerable error, from studies that have looked at the magnitude of this cost in actual bankruptcies. Research that has looked at the direct cost of bankruptcy concludes that they are small63, relative to firm value. In fact, the costs of distress stretch far beyond the conventional costs of bankruptcy and liquidation. The perception of distress can do serious damage to a firm's operations, as employees, customers, suppliers and lenders react. Firms that are viewed as distressed lose customers (and sales), have higher employee turnover and have to accept much tighter restrictions from suppliers than healthy firms. These indirect bankruptcy costs can be catastrophic for many firms and essentially make the perception of distress into a

<sup>62</sup> Cooper, I.A. and K.G. Nyborg, 2006, The value of tax shields is equal to the present value of the tax shields, Journal of Financial Economics, v81, 215-225.

<sup>63</sup> Warner, J.N., 1977, Bankruptcy Costs: Some Evidence, Journal of Finance, v32, 337-347. In this study of railroad bankruptcies, the direct cost of bankruptcy was estimated to be about 5%.

reality. The magnitude of these costs has been examined in studies and can range from 10-25% of firm value. 64

#### *Variants on APV*

While the original version of the adjusted present value model was fairly rigid in its treatment of the tax benefits of debt and expected bankruptcy costs, subsequent variations allow for more flexibility in the treatment of both. Some of these changes can be attributed to pragmatic considerations, primarily because of the absence of information, whereas others represented theoretical corrections.

One adaptation of the model was suggested by Luehrman (1997), where he presents an example where the dollar debt level, rather than remain fixed as it does in conventional APV, changes over time as a fraction of book value. <sup>65</sup> The interest tax savings reflect the changing debt but the present value of the tax savings is still computed using the cost of debt.

Another variation on adjusted present value was presented by Kaplan and Ruback (1995) in a paper where they compared the discounted cash flow valuations of companies to the prices paid in leveraged transactions.66 They first estimated what they termed capital cash flows which they defined to be cash flows to both debt and equity investors and thus inclusive of the tax benefits from interest payments on debt. This is in contrast with the conventional unlevered firm valuation, which uses only operating cash flows and does not include interest tax savings. These capital cash flows are discounted back at the unlevered cost of equity to arrive at firm value. In effect, the compressed adjusted present value approach differs from the conventional adjusted present value approach on two dimensions. First, the tax savings from debt are discounted back at the unlevered cost of equity rather than the cost of debt. Second, the expected bankruptcy costs are effectively

<sup>64</sup> For an examination of the theory behind indirect bankruptcy costs, see Opler, T. and S. Titman, 1994, Financial Distress and Corporate Performance. Journal of Finance 49, 1015-1040. For an estimate on how large these indirect bankruptcy costs are in the real world, see Andrade, G. and S. Kaplan, 1998, How Costly is Financial (not Economic) Distress? Evidence from Highly Leveraged Transactions that Become Distressed. Journal of Finance. 53, 1443-1493. They look at highly levered transactions that subsequently became distressed snd conclude that the magnitude of these costs ranges from 10% to 23% of firm value.

<sup>65</sup> Luehrman, T. A., 1997, Using APV: A Better Tool for Valuing Operations, *Harvard Business Review*, May-June, 145-154.

ignored in the computation. Kaplan and Ruback argue that this approach is simpler to use than the conventional cost of capital approach in levered transactions because the leverage changes over time, which will result in time-varying costs of capital. In effect, they are arguing that it is easier to reflect the effects of changing leverage in the cash flows than it is in debt ratios. Gilson, Hotchkiss and Ruback (2000) use the compressed APV approach to value bankrupt firms that are reorganized and conclude that while the approach yields unbiased estimates of value, the valuation errors remain large.67 The key limitation of the compressed APV approach, notwithstanding its simplicity, is that it ignores expected bankruptcy costs. In fact, using the compressed adjusted present value approach will lead to the conclusion that a firm is always worth more with a higher debt ratio than with a lower one. Kaplan and Ruback justify their approach by noting that the values that they arrive at are very similar to the values obtained using comparable firms, but this cannot be viewed as vindication.

Ruback (2000) provides a more extensive justification of the capital cash flow approach to valuation.68 He notes that the conventional APV's assumption that interest tax savings have the same risk as the debt (and thus get discounted back at the cost of debt) may be justifiable for a fixed dollar debt but that it is more reasonable to assume that interest tax savings share the same risk as the operating assets, when dollar debt is expected to change over time. He also notes that the capital cash flow approach assumes that debt grows with firm value and is thus closer to the cost of capital approach, where free cash flows to the firm are discounted back at a cost of capital. In fact, he shows that when the dollar debt raised each year is such that the debt ratio stays constant, the cost of capital approach and the capital cash flows approach yield identical results.

<sup>66</sup> Kaplan, S.N. and R.S. Ruback, 1995, The Valuation of Cash Flow Forecasts, Journal of Finance, v50, 1059-1093.

<sup>67</sup> Gilson, S.C., E. S. Hotchkiss and R. Ruback, 1998, Valuation of Bankrupt Firms, Review of Financial Studies, v13, 43-74. The one modification they introduce is that the tax savings from net operating loss carryforwards are discounted back at the cost of debt.

<sup>68</sup> Ruback, R.S., 2000, Capital Cash Flows: A Simple Approach to Valuing Risky Cash Flows, Working Paper, Harvard Business School.

#### *Cost of Capital versus APV Valuation*

To understand when the cost of capital approach, the adjusted present value approach and the modified adjusted present value approach (with capital cash flows) yield similar and different results, we consider the mechanics of each approach in table 1:

*Table 1: Cost of Capital, APV and Compressed APV*

|                                                       | <i>Cost of Capital</i>                                                                                              | <i>Conventional APV</i>                                                                                                   | <i>Compressed APV</i>                                                                                                     |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Cash flow discounted                                  | Free Cash Flow to Firm (prior to all debt payments)                                                                 | Free Cash Flow to Firm (prior to debt payments)                                                                           | Free Cash Flow to Firm + Tax Savings from Interest Payments                                                               |
| Discount Rate used                                    | Weighted average of cost of equity and after-tax cost of debt = Cost of capital                                     | Unlevered cost of equity                                                                                                  | Weighted average of cost of equity and pre-tax cost of debt = Unlevered cost of equity                                    |
| Tax Savings from Debt                                 | Shows up through the discount rate                                                                                  | Added on separately as present value of tax savings (using cost of debt as discount rate)                                 | Shows up through cash flow                                                                                                |
| Dollar debt levels                                    | Determined by debt ratios used in cost of capital. If debt ratio stays fixed, dollar debt increases with firm value | Fixed dollar debt                                                                                                         | Dollar debt can change over time – increase or decrease.                                                                  |
| Discount rate for tax benefits from interest expenses | Discounted at unlevered cost of equity                                                                              | Discounted at pre-tax cost of debt                                                                                        | Discounted at unlevered cost of equity                                                                                    |
| Bankruptcy Costs                                      | Reflected as higher costs of equity and debt, as default risk increases.                                            | Can be computed separately, based upon likelihood of distress and the cost of such distress. (In practice, often ignored) | Can be computed separately, based upon likelihood of distress and the cost of such distress. (In practice, often ignored) |

In an APV valuation, the value of a levered firm is obtained by adding the net effect of debt to the unlevered firm value.

Value of Levered Firm = 
$$\frac{\text{FCFF}_0(1+g)}{\rho_u - g} + t_c \text{D} - \pi_a \text{BC}$$

The tax savings from debt are discounted back at the cost of debt. In the cost of capital approach, the effects of leverage show up in the cost of capital, with the tax benefit incorporated in the after-tax cost of debt and the bankruptcy costs in both the levered beta and the pre-tax cost of debt. Inselbag and Kaufold (1997) provide examples where they get identical values using the APV and Cost of Capital approaches, but only because they infer the costs of equity to use in the latter. 69

Will the approaches yield the same value? Not necessarily. The first reason for the differences is that the models consider bankruptcy costs very differently, with the adjusted present value approach providing more flexibility in allowing you to consider indirect bankruptcy costs. To the extent that these costs do not show up or show up inadequately in the pre-tax cost of debt, the APV approach will yield a more conservative estimate of value. The second reason is that the conventional APV approach considers the tax benefit from a fixed dollar debt value, usually based upon existing debt. The cost of capital and compressed APV approaches estimate the tax benefit from a debt ratio that may require the firm to borrow increasing amounts in the future. For instance, assuming a market debt to capital ratio of 30% in perpetuity for a growing firm will require it to borrow more in the future and the tax benefit from expected future borrowings is incorporated into value today. Finally, the discount rate used to compute the present value of tax benefits is the pre-tax cost of debt in the conventional APV approach and the unlevered cost of equity in the compressed APV and the cost of capital approaches. As we noted earlier, the compressed APV approach yields equivalent values to the cost of capital approach, if we allow dollar debt to reflect changing firm value (and debt ratio assumptions) and ignore the effect of indirect bankruptcy costs. The conventional APV approach yields a higher value than either of the other two approaches because it views the tax savings from debt as less risky and assigns a higher value to it.

Which approach will yield more reasonable estimates of value? The dollar debt assumption in the APV approach is a more conservative one but the fundamental flaw with the APV model lies in the difficulties associated with estimating expected bankruptcy costs. As long as that cost cannot be estimated, the APV approach will

<sup>69</sup> Inselbag, I. and H. Kaufold, 1997, Two DCF approaches for valuing companies under alternative financing strategies and how to choose between them, Journal of Applied Corporate Finance, v10, 114-122.

continue to be used in half-baked form where the present value of tax benefits will be added to the unlevered firm value to arrive at total firm value.

#### **Liquidation and Accounting Valuation**

The value of an asset in the discounted cash flow framework is the present value of the expected cash flows on that asset. Extending this proposition to valuing a business, it can be argued that the value of a business is the sum of the values of the individual assets owned by the business. While this may be technically right, there is a key difference between valuing a collection of assets and a business. A business or a company is an on-going entity with assets that it already owns and assets it expects to invest in the future. This can be best seen when we look at the financial balance sheet (as opposed to an accounting balance sheet) for an ongoing company in figure 4:

![](_page_49_Diagram_5.jpeg)

*Figure 4: A Simple View of a Firm*

Note that investments that have already been made are categorized as assets in place, but investments that we expect the business to make in the future are growth assets.

A financial balance sheet provides a good framework to draw out the differences between valuing a business as a going concern and valuing it as a collection of assets. In a going concern valuation, we have to make our best judgments not only on existing investments but also on expected future investments and their profitability. While this may seem to be foolhardy, a large proportion of the market value of growth companies comes from their growth assets. In an asset-based valuation, we focus primarily on the assets in place and estimate the value of each asset separately. Adding the asset values together yields the value of the business. For companies with lucrative growth opportunities, asset-based valuations will yield lower values than going concern valuations.

#### *Book Value Based Valuation*

There are some who contend that the accounting estimate of the value of a business, as embodied by the book value of the assets and equity on a balance sheet, represents a more reliable estimate of value than valuation models based on shaky assumptions about the future. In this section, we examine book value as a measure of the value of going concern and then extend the analysis to look at book value based valuation models that are also use forecasted earnings to estimate value. We end the section with a short discussion of fair value accounting, a movement that has acquired momentum in recent years.

#### *Book Value*

The original ideals for accounting statements were that the income statements would provide a measure of the true earnings potential of a firm and that the balance sheet would yield a reliable estimate of the value of the assets and equity in the firm. Daniels (1934), for instance, lays out these ideals thus:70

*"In short the lay reader of financial statements usually believes that the total asset figure of the balance sheet is indicative, and is intended to be so, of the value of the company. He probably understanding this "value" as what the business could be sold for, market value – the classic meeting of the minds between a willing buyer and seller."*

In the years since, accountants have wrestled with how put this ideal into practice. In the process, they have had the weigh how much importance to give the historical cost of an asset relative to its estimated value today and have settled on different rules. For fixed assets, they have largely concluded that the book value should be reflective of the original cost of the asset and subsequent depletion in and additions to that asset. For current assets, they have been much more willing to consider the alternative of market value. Finally, they have discovered new categories for assets such as brand name where neither the original cost nor the current value is easily accessible.

While there are few accountants who would still contend that the book value of a company is a good measure of its market value, this has not stopped some investors from

implicitly making that assumption. In fact, the notion that a stock is under valued if is market price falls below its book value is deeply entrenched in investing. It is one of the screens that Ben Graham proposed for finding undervalued stocks71 and it remains a rough proxy for what is loosely called value investing.72 Academics have fed into this belief by presenting evidence that low price to book value stocks do earn higher returns than the rest of the market. 73

Is it possible for book value to be a reasonable proxy for the true value of a business? For mature firms with predominantly fixed assets, little or no growth opportunities and no potential for excess returns, the book value of the assets may yield a reasonable measure of the true value of these firms. For firms with significant growth opportunities in businesses where they can generate excess returns, book values will be very different from true value.

### *Book Value plus Earnings*

In the context of equity valuation models, we considered earnings based models that have been developed in recent years, primarily in the accounting community. Most of these models are built on a combination of book values and expected future earnings and trace their antecedents to Ohlson (1995) and Feltham and Ohlson (1995), both works that we referenced earlier in the context of earnings based valuation models. <sup>74</sup> Ohlson's basic model states the true value of equity as a function of its book value of equity and the excess equity returns that the firm can generate in the future. As a consequence, it is termed a residual income model and can be derived from a simple dividend discount model:

$$\text{Value of equity} = \sum_{t=1}^{t=\infty} \frac{\text{E}(\text{Dividends}_t)}{(1 + \text{Cost of Equity})^t}$$

<sup>71</sup> Daniels, M.B., 1934, Principles of Asset Valuation, The Act of 1949, Graham, B., 1949, The Intelligent Investor, HarperCollins.

<sup>70</sup> Daniels, M.B., 1934, Principles of Asset Valuation, The Accounting Review, v9, 114-121.

<sup>72</sup> Morningstar categorizes mutual funds into growth and value, based upon the types of stocks that they invest in. Funds that invest in low price to book stocks are categorized as value funds.

<sup>73</sup> Fama, E.F. and K.R. French, 1992, *The Cross-Section of Expected Returns*, Journal of Finance, v47, 427-466.

<sup>74</sup> Ohlson, J. 1995, Earnings, Book values and Dividends in Security Valuation, Contemporary Accounting Research, v11, 661-687.; Feltham and Ohlson, 1995, Valuation and Clean Surplus Accounting for Operating and Financial Activities, Contemporary Accounting Research, v11, 689-731.

Now substitute in the full equation for book value (BV) of equity as a function of the starting book equity and earnings and dividends during a period (clean surplus relationship):

Book Value of Equityt = BV of Equityt-1 + Net Incomet - Dividendst Substituting back into the dividend discount model, we get

$$\text{Value of Equity}_0 = \text{BV of Equity}_0 + \frac{\sum_{t=1}^{t=\infty} (\text{Net Income}_t - \text{Cost of Equity}_t * \text{BV of Equity}_{t-1})}{(1 + \text{Cost of Equity}_t)'}$$

Thus the value of equity in a firm is the sum of the current book value of equity and the present value of the expected excess returns to equity investors in perpetuity

The enthusiasm with which the Ohlson residual income model has been received by accounting researchers is puzzling, given that it is neither new nor revolutionary. Walter(1966)75 and Mao (1974)76 extended the dividend discount model to incorporate excess returns earned on future investment opportunities. In fact, we used exactly the same rationale to relate enterprise value to EVA earlier in the paper. The only real difference is that the Ohlson model is an extension of the more limiting dividend discount model, whereas the EVA model is an extension of a more general firm valuation model. In fact, Lundholm and O'Keefe (2001) show that discounted cash flow models and residual income models yield identical valuations of companies, if we make consistent assumptions.77 One explanation for the enthusiasm is that the Ohlson model has allowed accountants to argue that accounting numbers are still relevant to value. After all, Lev (1989) had presented evidence on the declining significance of accounting earnings

<sup>7575</sup> Walter, J.E., 1966, Dividend Policies and Common Stock Prices, Journal of Finance, v11, 29-41. Walters modified the dividend discount model as follows:  $P = \frac{D + \frac{ROE}{k_c}(E-D)}{k_c}$ , where E and D are the

<sup>76</sup> Mao, J.C.T., 1974, The Valuation of Growth Stocks: The Investment Opportunities Approach, Journal of Finance, v21, 95-102. The key difference is that rather than build off book value of equity, as Ohlson did, Mao capitalized current earnings (as a perpetuity) and added the present value of future excess returns to this value.

expected earnings and dividends in the next period, ROE is the expected return on equity in perpetuity on retained earnings and ke is the cost of equity. Note that the second term in the numerator is the excess return generated on an annual basis and that dividing by the cost of equity yields its present value in perpetuity.

this value. <sup>77</sup> Lundholm, R., and T. O'Keefe. 2001. Reconciling value estimates from the discounted cash flow model and the residual income model. *Contemporary Accounting Research, v*18, 311-35.

numbers by noting a drop in the correlation between market value and earnings.78 In the years since, a number of studies have claimed to find strong evidence to back up the Ohlson model. For instance, Frankel and Lee (1996)79, Hand and Landsman (1998)80 and Dechow, Hutton and Sloan (1999)81 all find that the residual income model explains 70- 80% of variation in prices across stocks. The high R-squared in these studies is deceptive since they are not testing an equation as much as a truism: the total market value of equity should be highly correlated with the total book value of equity and total net income. Firms with higher market capitalization will tend to have higher book value of equity and higher net income, reflecting their scale and this has little relevance for whether the Ohlson model actually works. <sup>82</sup> A far stronger and more effective test of the model is whether changes in equity value are correlated with changes in book value of equity and net income and the model does no better on these tests than established models.

### *Fair Value Accounting*

In the last decade, there has been a strong push from both accounting rule makers and regulators towards "fair value accounting". Presumably, the impetus for this push has been a return to the original ideal that the book value of the assets on a balance sheet and the resulting net worth for companies be good measures of the fair value of these assets and equity.

The move towards fair value accounting has not been universally welcomed even within the accounting community. On the one hand, there are some who believe that this is a positive development increasing the connection of accounting statements to value and

<sup>78</sup> Lev, B. 1989. On the usefulness of earnings: Lessons and directions from two decades of empirical research, Journal of Accounting Research, v 27 (Supplement): 153-192.

<sup>79</sup> Frankel, R. and C.M.C. Lee. 1998. Accounting Valuation, Market Expectations, and Crosssectional Stock Returns. Journal of Accounting Economics, v25: 283-319.

<sup>80</sup> Hand, J.R.M. and W.R. Landsman. 1999. Testing the Ohlson Model: v or not v, that is the Question. Working Paper, University of North Carolina at Chapel Hill.

<sup>81</sup> Dechow, P., A. Hutton, R. Sloan, 1999. An Empirical Assessment of the Residual Income Valuation Model. Journal of Accounting and Economics 26 (1-3)1-34.

<sup>82</sup> Lo, K. and Lys, T., 2005, The Ohlson Model: Contribution to Valuation Theory, Limitations and Empirical Applications, Working Paper, Kellogg School of Management, Northwestern University.

providing useful information to financial markets.<sup>83</sup> There are others who believe that fair value accounting increases the potential for accounting manipulation, and that financial statements will become less informative as a result.<sup>84</sup> In fact, it used to be common place for firms in the United States to revalue their assets at fair market value until 1934, and the SEC discouraged this practice after 1934 to prevent the widespread manipulation that was prevalent.<sup>85</sup> While this debate rages on, the accounting standards boards have adopted a number of rules that favor fair value accounting, from the elimination of purchase accounting in acquisitions to the requirement that more assets be marked to market on the balance sheet.

The question then becomes an empirical one. Do fair value judgments made by accountants provide information to financial markets or do they just muddy up the waters? In a series of articles, Barth concluded that fair value accounting provided useful information to markets in a variety of contexts.<sup>86</sup> In contrast, Nelson (1996) examines fair value accounting in banking, where marking to market has been convention for a much longer period, and finds the reported fair values of investment securities have little incremental explanatory power when it comes to market values.<sup>87</sup> In an interesting test of the effects of fair value accounting, researchers have begun looking at market reactions in the aftermath of the adoption of SFAS 141 and 142, which together eliminated pooling, while also requiring that firms estimate “fair-value impairments” of goodwill rather than amortizing goodwill. Chen, Kohlbeck and Warfield (2004) find that stock prices react negatively to goodwill impairments, which they construe to indicate that there is

---

<sup>83</sup> Barth, M., W. Beaver and W. Landsman. 2001. The relevance of the value-relevance literature for financial accounting standard setting: another view. *Journal of Accounting and Economics* 31: 77-104

<sup>84</sup> Holthausen, R. and R. Watts. 2001. The relevance of the value-relevance literature for financial accounting standard setting. *Journal of Accounting and Economics*, v31, 3-75.

<sup>85</sup> Fabricant, S. 1938. Capital Consumption and Adjustment, National Bureau of Economic Research.

<sup>86</sup> Barth, M.E., 1994. Fair Value Accounting: Evidence from Investment Securities and the Market Valuation of Banks, *Accounting Review*, v69, No. 1 (January): 1-25; Barth, M.E., W. R. Landsman, and J. M. Whalen. 1995. Fair value accounting: effects on banks' earnings volatility, regulatory capital, and value of contractual cash flows, *Journal of Banking and Finance* v19, No.3-4 (June): 577-605; Barth, M.E., W.H. Beaver, and W.R. Landsman. 1996. Value relevance of banks fair value disclosures under SFAS 107, *The Accounting Review*, v71, No.4 (October): 513-37; Barth, M.E. and G. Clinch. 1998. Revalued financial, tangible, and intangible assets: Associations with share prices and non-market-based value estimates, *Journal of Accounting Research*, v36 (Supplement): 199-233.

<sup>87</sup> Nelson, K.K., 1996, Fair Value Accounting for Commercial Banks: An Empirical Analysis of SFAS 107, *The Accounting Review*, v71, 161-182.

information in these accounting assessments. <sup>88</sup> Note, though, that this price reaction can be consistent with a number of other interpretations as well and can be regarded, at best, as weak evidence that fair value accounting assessments convey information to markets.

We believe that fair value accounting, at best, will provide a delayed reflection of what happens in the market. In other words, goodwill be impaired (as it was in many technology companies in 2000 and 2001) after the market value has dropped and fair value adjustments will convey little, if any, information to financial markets. If in the process of marking to market, some of the raw data that is now provided to investors is replaced or held back, we will end up with accounting statements that neither reflect market value nor invested capital.

#### *Liquidation Valuation*

One special case of asset-based valuation is liquidation valuation, where we value assets based upon the presumption that they have to be sold now. In theory, this should be equal to the value obtained from discounted cash flow valuations of individual assets but the urgency associated with liquidating assets quickly may result in a discount on the value. The magnitude of the discount will depend upon the number of potential buyers for the assets, the asset characteristics and the state of the economy.

The research on liquidation value can be categorized into two groups. The first group of studies examines the relationship between liquidation value and the book value of assets, whereas the second takes apart the deviations of liquidation value from discounted cash flow value and addresses directly the question of how much of a cost you bear when you have to liquidate assets rather than sell a going concern.

While it may seem naïve to assume that liquidation value is equal or close to book value, a number of liquidation rules of thumb are structured around book value. For instance, it is not uncommon to see analysts assume that liquidation value will be a specified percentage of book value. Berger, Ofek and Swary (1996) argue and provide evidence that book value operates as a proxy for abandonment value in many firms. 89

<sup>88</sup> Chen, C., M. Kohlbeck and T. Warfield, 2004, Goodwill Valuation Effects of the Initial Adoption of SFAS 142, Working Paper, University of Wisconsin- Madison.

<sup>89</sup> Berger, P., E. Ofek and I. Swary, 1996, Investor Valuation of the Abandonment Option, Journal of Financial Economics, v42, 257-287.

Lang, Stulz and Walkling (1989) use book value as a proxy for the replacement cost of assets when computing Tobin's Q. 90

The relationship between liquidation and discounted cash flow value is more difficult to discern. It stands to reason that liquidation value should be significantly lower than discounted cash flow value, partly because the latter reflects the value of expected growth potential and the former usually does not. In addition, the urgency associated with the liquidation can have an impact on the proceeds, since the discount on value can be considerable for those sellers who are eager to divest their assets. Kaplan (1989) cited a Merrill Lynch estimate that the speedy sales of the Campeau stake in Federated would bring about 32% less than an orderly sale of the same assets.91 Holland (1990) estimates the discount to be greater than 50% in the liquidation of the assets of machine tool manufacturer. <sup>92</sup> Williamson (1988) makes the very legitimate point that the extent of the discount is likely to be smaller for assets that are not specialized and can be redeployed elsewhere. <sup>93</sup> Shleifer and Vishny (1992) argue that assets with few potential buyers or buyers who are financially constrained are likely to sell at significant discounts on market value.94

In summary, liquidation valuation is likely to yield more realistic estimates of value for firms that are distressed, where the going concern assumption underlying conventional discounted cash flow valuation is clearly violated. For healthy firms with significant growth opportunities, it will provide estimates of value that are far too conservative.

# **Relative Valuation**

In relative valuation, we value an asset based upon how similar assets are priced in the market. A prospective house buyer decides how much to pay for a house by looking at the prices paid for similar houses in the neighborhood. A baseball card

<sup>90</sup> Lang, L.H.P., R.M. Stulz and R.Walking. 1989. Managerial Performance, Tobin's Q, and The Gains from Successful Tender Offers. Journal of Financial Economics, v29, 137-154.

<sup>91</sup> Kaplan, S.N., 1989, Campeau's Acquisition of Federated: Value Destroyed or Value Added? Journal of Financial Economics, v25, 191-212.

<sup>92</sup> Holland, M., 1990, When the Machine Stopped, Harvard Business School Press, Cambridge, MA.

<sup>93</sup> Williamson, O.E., 1988, Corporate Finance and Corporate Governance, Journal of Finance, v43, 567- 592.

<sup>94</sup> Shleifer, A., and R. W. Vishny, 1992, Liquidation Values and Debt Capacity: A Market Equilibrium

collector makes a judgment on how much to pay for a Mickey Mantle rookie card by checking transactions prices on other Mickey Mantle rookie cards. In the same vein, a potential investor in a stock tries to estimate its value by looking at the market pricing of "similar" stocks.

Embedded in this description are the three essential steps in relative valuation. The first step is finding comparable assets that are priced by the market, a task that is easier to accomplish with real assets like baseball cards and houses than it is with stocks. All too often, analysts use other companies in the same sector as comparable, comparing a software firm to other software firms or a utility to other utilities, but we will question whether this practice really yields similar companies later in this paper. The second step is scaling the market prices to a common variable to generate standardized prices that are comparable. While this may not be necessary when comparing identical assets (Mickey Mantle rookie cards), it is necessary when comparing assets that vary in size or units. Other things remaining equal, a smaller house or apartment should trade at a lower price than a larger residence. In the context of stocks, this equalization usually requires converting the market value of equity or the firm into multiples of earnings, book value or revenues. The third and last step in the process is adjusting for differences across assets when comparing their standardized values. Again, using the example of a house, a newer house with more updated amenities should be priced higher than a similar sized older house that needs renovation. With stocks, differences in pricing across stocks can be attributed to all of the fundamentals that we talked about in discounted cash flow valuation. Higher growth companies, for instance, should trade at higher multiples than lower growth companies in the same sector. Many analysts adjust for these differences qualitatively, making every relative valuation a story telling experience; analysts with better and more believable stories are given credit for better valuations.

# *Basis for approach*

There is a significant philosophical difference between discounted cash flow and relative valuation. In discounted cash flow valuation, we are attempting to estimate the intrinsic value of an asset based upon its capacity to generate cash flows in the future. In

relative valuation, we are making a judgment on how much an asset is worth by looking at what the market is paying for similar assets. If the market is correct, on average, in the way it prices assets, discounted cash flow and relative valuations may converge. If, however, the market is systematically over pricing or under pricing a group of assets or an entire sector, discounted cash flow valuations can deviate from relative valuations.

Harking back to our earlier discussion of discounted cash flow valuation, we argued that discounted cash flow valuation was a search (albeit unfulfilled) for intrinsic value. In relative valuation, we have given up on estimating intrinsic value and essentially put our trust in markets getting it right, at least on average. It can be argued that most valuations are relative valuations. Damodaran (2002) notes that almost 90% of equity research valuations and 50% of acquisition valuations use some combination of multiples and comparable companies and are thus relative valuations. 95

### *Standardized Values and Multiples*

When comparing identical assets, we can compare the prices of these assets. Thus, the price of a Tiffany lamp or a Mickey Mantle rookie card can be compared to the price at which an identical item was bought or sold in the market. However, comparing assets that are not exactly similar can be a challenge. After all, the price per share of a stock is a function both of the value of the equity in a company and the number of shares outstanding in the firm. Thus, a stock split that doubles the number of units will approximately halve the stock price. To compare the values of "similar" firms in the market, we need to standardize the values in some way by scaling them to a common variable. In general, values can be standardized relative to the earnings firms generate, to the book values or replacement values of the firms themselves, to the revenues that firms generate or to measures that are specific to firms in a sector.

- One of the more intuitive ways to think of the value of any asset is as a multiple of the earnings that asset generates. When buying a stock, it is common to look at the price paid as a multiple of the earnings per share generated by the company. This price/earnings ratio can be estimated using current earnings per share, yielding a current PE, earnings over the last 4 quarters, resulting in a trailing PE, or an expected earnings per share in the next year, providing a forward PE. When buying a business,

as opposed to just the equity in the business, it is common to examine the value of the firm as a multiple of the operating income or the earnings before interest, taxes, depreciation and amortization (EBITDA). While, as a buyer of the equity or the firm, a lower multiple is better than a higher one, these multiples will be affected by the growth potential and risk of the business being acquired.

- • While financial markets provide one estimate of the value of a business, accountants often provide a very different estimate of value of for the same business. As we noted earlier, investors often look at the relationship between the price they pay for a stock and the book value of equity (or net worth) as a measure of how over- or undervalued a stock is; the price/book value ratio that emerges can vary widely across industries, depending again upon the growth potential and the quality of the investments in each. When valuing businesses, we estimate this ratio using the value of the firm and the book value of all assets or capital (rather than just the equity). For those who believe that book value is not a good measure of the true value of the assets, an alternative is to use the replacement cost of the assets; the ratio of the value of the firm to replacement cost is called Tobin's Q.
- Both earnings and book value are accounting measures and are determined by accounting rules and principles. An alternative approach, which is far less affected by accounting choices, is to use the ratio of the value of a business to the revenues it generates. For equity investors, this ratio is the price/sales ratio (PS), where the market value of equity is divided by the revenues generated by the firm. For firm value, this ratio can be modified as the enterprise value/to sales ratio (VS), where the numerator becomes the market value of the operating assets of the firm. This ratio, again, varies widely across sectors, largely as a function of the profit margins in each. The advantage of using revenue multiples, however, is that it becomes far easier to compare firms in different markets, with different accounting systems at work, than it is to compare earnings or book value multiples.
- • While earnings, book value and revenue multiples are multiples that can be computed for firms in any sector and across the entire market, there are some multiples that are specific to a sector. For instance, when internet firms first appeared on the market in the later 1990s, they had negative earnings and negligible revenues and book value.

<sup>[5]</sup> Damodaran, A., 2002, Investment Valuation (Second Edition), John Wiley and Sons, New York.Analysts looking for a multiple to value these firms divided the market value of each of these firms by the number of hits generated by that firm's web site. Firms with lower market value per customer hit were viewed as under valued. More recently, cable companies have been judged by the market value per cable subscriber, regardless of the longevity and the profitably of having these subscribers. While there are conditions under which sector-specific multiples can be justified, they are dangerous for two reasons. First, since they cannot be computed for other sectors or for the entire market, sector-specific multiples can result in persistent over or under valuations of sectors relative to the rest of the market. Thus, investors who would never consider paying 80 times revenues for a firm might not have the same qualms about paying \$2000 for every page hit (on the web site), largely because they have no sense of what high, low or average is on this measure. Second, it is far more difficult to relate sector specific multiples to fundamentals, which is an essential ingredient to using multiples well. For instance, does a visitor to a company's web site translate into higher revenues and profits? The answer will not only vary from company to company, but will also be difficult to estimate looking forward.

There have been relatively few studies that document the usage statistics on these multiples and compare their relative efficacy. Damodaran (2002) notes that the usage of multiples varies widely across sectors, with Enterprise Value/EBITDA multiples dominating valuations of heavy infrastructure businesses (cable, telecomm) and price to book ratios common in financial service company valuations.96 Fernandez (2001) presents evidence on the relative popularity of different multiples at the research arm of one investment bank – Morgan Stanley Europe – and notes that PE ratios and EV/EBITDA multiples are the most frequently employed.97 Liu, Nissim and Thomas (2002) compare how well different multiples do in pricing 19,879 firm-year observations between 1982 and 1999 and suggest that multiples of forecasted earnings per share do best in explaining pricing differences, that multiples of sales and operating cash flows do

<sup>96</sup> Damodaran, A, 2002, Investment Valuation, Second Edition, John Wiley and Sons, New York.

<sup>97</sup> Fernandez, P., 2001, Valuation using multiples. How do analysts reach their conclusions?, Working Paper, IESE Business School.

worst and that multiples of book value and EBITDA fall in the middle. <sup>98</sup> Lie and Lie (2002) examine 10 different multiples across 8,621 companies between 1998 and 1999 and arrive at similar conclusions. 99

#### *Determinants of Multiples*

In the introduction to discounted cash flow valuation, we observed that the value of a firm is a function of three variables – it capacity to generate cash flows, the expected growth in these cash flows and the uncertainty associated with these cash flows. Every multiple, whether it is of earnings, revenues or book value, is a function of the same three variables – risk, growth and cash flow generating potential. Intuitively, then, firms with higher growth rates, less risk and greater cash flow generating potential should trade at higher multiples than firms with lower growth, higher risk and less cash flow potential.

The specific measures of growth, risk and cash flow generating potential that are used will vary from multiple to multiple. To look under the hood, so to speak, of equity and firm value multiples, we can go back to fairly simple discounted cash flow models for equity and firm value and use them to derive the multiples. In the simplest discounted cash flow model for equity, which is a stable growth dividend discount model, the value of equity is:

$$\text{Value of Equity} = P_0 = \frac{DPS_1}{k_e - g_n}$$

where DPS1 is the expected dividend in the next year, ke is the cost of equity and gn is the expected stable growth rate. Dividing both sides by the earnings, we obtain the discounted cash flow equation specifying the PE ratio for a stable growth firm.

The key determinants of the PE ratio are the expected growth rate in earnings per share, the cost of equity and the payout ratio. Other things remaining equal, we would expect higher growth, lower risk and higher payout ratio firms to trade at higher multiples of earnings than firms without these characteristics. In fact, this model can be expanded to

$$\frac{P_0}{\text{EPS}_0} = \text{PE} = \frac{\text{Payout Ratio}^* (1 + g_n)}{k_e - g_n}$$

<sup>98</sup> Liu, J., D. Nissim, and J. Thomas. 2002. Equity Valuation Using Multiples. *Journal of Accounting Research*, V 40, 135-172.

<sup>99</sup> Lie E., H.J. Lie, 2002, Multiples Used to Estimate Corporate Value. Financial Analysts Journal, v58, 44- 54.

allow for high growth in near years and stable growth beyond.100 Researchers have long recognized that the PE for a stock is a function of both the level and the quality of its growth and its risk. Beaver and Morse (1978) related PE ratios to valuation fundamentals101, as did earlier work by Edwards and Bell (1961).102 Peasnell (1982) made a more explicit attempt to connect market values to accounting numbers.103 Zarowin (1990) looked at the link between PE ratios and analyst forecasts of growth to conclude that PE ratios are indeed positively related to long term expected growth. 104 Leibowitz and Kogelman (1990, 1991, 1992) expanded on the relationship between PE ratios and the excess returns earned on investments, which they titled franchise opportunities, in a series of articles on the topic, noting that for a stock to have a high PE ratio, it needs to generate high growth in conjunction with excess returns on its new investments. <sup>105</sup> Fairfield (1994) provides a generalized version of their model, allowing for changing return on equity over time. <sup>106</sup> While these papers focused primarily on growth and returns, Kane, Marcus and Noe (1996) examine the relationship between PE and risk for the aggregate market and conclude that PE ratios decrease as market volatility increases. 107

Dividing both sides of the stable growth dividend discount model by the book value of equity, we can estimate the price/book value ratio for a stable growth firm.

| <p> </p> |  |
|----------|--|
|          |  |
|          |  |
|          |  |

| $\frac{P_0}{BV_0} = PBV =$ | ROE * Payout Ratio * $(1 + g_n)$ |
|----------------------------|----------------------------------|
| $k_e - g_n$                |                                  |

<sup>100</sup> Damodaran, A., 2002, Investment Valuation, John Wiley and Sons, New York. The expanded versions of the models are available in the chapter on PE ratios.

<sup>101</sup> Beaver, W. and D. Morse, 1978, What do P/E ratios mean?, Financial Analysts Journal, v34, 65-76.

<sup>102</sup> Edwards, E. and P. Bell, 1961, The Theory and Measurement of Business Income, University of California Press, Berkeley.

<sup>103</sup> Peasnell, K., 1982, Some Financial Connections between Economic Values and Accounting Numbers, Journal of Business Finance and Accounting, v9, 361-381.

<sup>104</sup> Zarowin, P. 1990. What determines earnings-price ratios: revisited, Journal of Accounting, Auditing, and Finance, v5: 439-57.

<sup>105</sup> Leibowitz, M.L. and S. Kogelman, 1990, Inside the PE Ratio: The Franchise Factor, Financial Analysts Journal, v46, 17-35; Leibowitz, M.L. and S. Kogelman, 1991, The Franchise Factor for Leveraged Firms, Financial Analysts Journal, v47, 29-43.; Leibowitz, M.L. and S. Kogelman, 1992, Franchise Value and the Growth Factor, Financial Analysts Journal, v48, 16-23.

<sup>106</sup> Fairfield, P., 1994, P/E, P/B and the present value of future dividends, Financial Analysts Journal, v50,

<sup>23-31.</sup> <sup>107</sup> Kane, A., A.J. Marcus and J. Noh, The P/E Multiple and Market Volatility, Financial Analysts Journal, v52, 16-24.

where ROE is the return on equity and is the only variable in addition to the three that determine PE ratios (growth rate, cost of equity and payout) that affects price to book equity. The strong connection between price to book and return on equity was noted by Wilcox (1984), with his argument that cheap stocks are those that trade at low price to book ratios while maintaining reasonable or even high returns on equity.108 The papers we referenced in the earlier section on book-value based valuation approaches centered on the Ohlson model can be reframed as a discussion of the determinants of price to book ratios. Penman (1996) draws a distinction between PE ratios and PBV ratios when it comes to the link with return on equity, by noting that while PBV ratios increase with ROE, the relationship between PE ratios and ROE is weaker. 109

Finally, dividing both sides of the dividend discount model by revenues per share, the price/sales ratio for a stable growth firm can be estimated as a function of its profit margin, payout ratio, risk and expected growth.

The net margin is the new variable that is added to the process. While all of these computations are based upon a stable growth dividend discount model, we will show that the conclusions hold even when we look at companies with high growth potential and with other equity valuation models. While less work has been done on revenue multiples than on book value or earnings multiples, Leibowitz (1997) extends his franchise value argument from PE ratios to revenue multiples and notes the importance of what profit margins.<sup>110</sup>

| $\frac{P_0}{\text{Sales}_0} = \text{PS} =$ | Profit Margin * Payout Ratio * $(1 + g_n)$ |
|--------------------------------------------|--------------------------------------------|
|                                            | $k_e - g_n$                                |

We can do a similar analysis to derive the firm value multiples. The value of a firm in stable growth can be written as:

$$\text{Value of Firm} = V_0 = \frac{\text{FCF}_1}{k_c - g_n}$$

<sup>108</sup> Wilcox, J., 1984, The P/B-ROE Valuation Model, Financial Analysts Journal, 58-66.

<sup>109</sup> Penman, S.H., 1996, The Articulation of Price-Earnings and Market-to-Book Ratios and the Evaluation of Growth, Journal of Accounting Research, v34, 235-259.

<sup>110</sup> Leibowitz, M.L., 1997, Franchise Margins and the Sales-Driven Franchise Value, Financial Analysts Journal, v53, 43-53.

Dividing both sides by the expected free cash flow to the firm yields the Value/FCFF multiple for a stable growth firm.

The multiple of FCFF that a firm commands will depend upon two variables – its cost of capital and its expected stable growth rate. Since the free cash flow the firm is the after-tax operating income netted against the net capital expenditures and working capital needs of the firm, the multiples of EBIT, after-tax EBIT and EBITDA can also be estimated similarly.

$$\frac{V_0}{\text{FCFF}_1} = \frac{1}{k_c - g_n}$$

In short, multiples are determined by the same variables and assumptions that underlie discounted cash flow valuation. The difference is that while the assumptions are explicit in the latter, they are often implicit in the use of the former.

### *Comparable Firms*

When multiples are used, they tend to be used in conjunction with comparable firms to determine the value of a firm or its equity. But what is a comparable firm? A comparable firm is one with cash flows, growth potential, and risk similar to the firm being valued. It would be ideal if we could value a firm by looking at how an exactly identical firm - in terms of risk, growth and cash flows - is priced. Nowhere in this definition is there a component that relates to the industry or sector to which a firm belongs. Thus, a telecommunications firm can be compared to a software firm, if the two are identical in terms of cash flows, growth and risk. In most analyses, however, analysts define comparable firms to be other firms in the firm's business or businesses. If there are enough firms in the industry to allow for it, this list is pruned further using other criteria; for instance, only firms of similar size may be considered. The implicit assumption being made here is that firms in the same sector have similar risk, growth, and cash flow profiles and therefore can be compared with much more legitimacy. This approach becomes more difficult to apply when there are relatively few firms in a sector. In most markets outside the United States, the number of publicly traded firms in a particular sector, especially if it is defined narrowly, is small. It is also difficult to define firms in the same sector as comparable firms if differences in risk, growth and cash flow profiles across firms within a sector are large. The tradeoff is therefore a simple one. Defining an industry more broadly increases the number of comparable firms, but it also results in a

more diverse group of companies. Boatman and Baskin (1981) compare the precision of PE ratio estimates that emerge from using a random sample from within the same sector and a narrower set of firms with the most similar 10-year average growth rate in earnings and conclude that the latter yields better estimates.111

There are alternatives to the conventional practice of defining comparable firms as other firms in the same industry. One is to look for firms that are similar in terms of valuation fundamentals. For instance, to estimate the value of a firm with a beta of 1.2, an expected growth rate in earnings per share of 20% and a return on equity of 40%112, we would find other firms across the entire market with similar characteristics. <sup>113</sup> Alford (1992) examines the practice of using industry categorizations for comparable firms and compares their effectiveness with using categorizations based upon fundamentals such as risk and growth.114 Based upon the prediction error from the use of each categorization, he concludes that industry based categorizations match or slightly outperform fundamental based categorization, which he views as evidence that much of the variation in multiples that can be explained by fundamentals can be also explained by industry. In contrast, Cheng and McNamara (2000) and Bhojraj and Lee (2002) argue that picking comparables using a combination of industry categorization and fundamentals such as total assets yields more precise valuations than using just the industry classification.115

<sup>111</sup> Boatman, J.R. and E.F. Baskin, 1981, Asset Valuation in Incomplete Markets, The Accounting Review, 38-53.

<sup>112</sup> The return on equity of 40% becomes a proxy for cash flow potential. With a 20% growth rate and a 40% return on equity, this firm will be able to return half of its earnings to its stockholders in the form of dividends or stock buybacks.

<sup>113</sup> Finding these firms manually may be tedious when your universe includes 10000 stocks. You could draw on statistical techniques such as cluster analysis to find similar firms.

<sup>114</sup> Alford, A.W., 1992, The Effect of the set of Comparable Firms on the Accuracy of the Price Earnings Valuation Method, Journal of Accounting Research, v30, 94-108.

<sup>115</sup> Cheng, C. S. A. and R. McNamara, 2000, The valuation accuracy of the price-earnings and price-book benchmark valuation methods, Review of Quantitative Finance and Accounting, v15, 349-370; Bhojraj, S. and C. M. C. Lee (2002): Who is my peer? A valuation-based approach to the selection of comparable firms, Journal of Accounting Research*, v*40, 407-439. Bhojraj S., C. M. C. Lee, Oler D. (2003), What's My Line? A Comparison of Industry Classification Schemes for Capital Market Research. Journal of Accounting Research, v41, 745-774.

#### *Controlling for Differences across Firms*

No matter how carefully we construct our list of comparable firms, we will end up with firms that are different from the firm we are valuing. The differences may be small on some variables and large on others and we will have to control for these differences in a relative valuation. There are three ways of controlling for these differences.

#### *1. Subjective Adjustments*

Relative valuation begins with two choices - the multiple used in the analysis and the group of firms that comprises the comparable firms. In many relative valuations, the multiple is calculated for each of the comparable firms and the average is computed. One issue that does come up with subjective adjustments to industry average multiples is how best to compute that average. Beatty, Riffe and Thompson (1999) examine multiples of earnings, book value and total assets and conclude that the harmonic mean provides better estimates of value than the arithmetic mean. <sup>116</sup> To evaluate an individual firm, the analyst then compare the multiple it trades at to the average computed; if it is significantly different, the analyst can make a subjective judgment about whether the firm's individual characteristics (growth, risk or cash flows) may explain the difference. If, in the judgment of the analyst, the difference on the multiple cannot be explained by the fundamentals, the firm will be viewed as over valued (if its multiple is higher than the average) or undervalued (if its multiple is lower than the average). The weakness in this approach is not that analysts are called upon to make subjective judgments, but that the judgments are often based upon little more than guesswork. All too often, these judgments confirm their biases about companies.

## *2. Modified Multiples*

In this approach, we modify the multiple to take into account the most important variable determining it – the companion variable. To provide an illustration, analysts who compare PE ratios across companies with very different growth rates often divide the PE ratio by the expected growth rate in EPS to determine a growth-adjusted PE ratio or the PEG ratio. This ratio is then compared across companies with different growth rates to find under and over valued companies. There are two implicit assumptions that we make

<sup>116</sup> Beatty, R.P., S.M. Riffe, and R. Thompson, 1999, The method of comparables and tax court

when using these modified multiples. The first is that these firms are comparable on all the other measures of value, other than the one being controlled for. In other words, when comparing PEG ratios across companies, we are assuming that they are all of equivalent risk. If some firms are riskier than others, you would expect them to trade at lower PEG ratios. The other assumption generally made is that that the relationship between the multiples and fundamentals is linear. Again, using PEG ratios to illustrate the point, we are assuming that as growth doubles, the PE ratio will double; if this assumption does not hold up and PE ratios do not increase proportional to growth, companies with high growth rates will look cheap on a PEG ratio basis. Easton (2004) notes that one of the weaknesses of the PEG ratio approach is its emphasis on short term growth and provides a way of estimating the expected rate of return for a stock, using the PEG ratio, and concludes that PEG ratios are effective at ranking stocks. 117

# *3. Statistical Techniques*

Subjective adjustments and modified multiples are difficult to use when the relationship between multiples and the fundamental variables that determine them becomes complex. There are statistical techniques that offer promise, when this happens. In this section, we will consider the advantages of these approaches and potential concerns.

### *Sector Regressions*

In a regression, we attempt to explain a dependent variable by using independent variables that we believe influence the dependent variable. This mirrors what we are attempting to do in relative valuation, where we try to explain differences across firms on a multiple (PE ratio, EV/EBITDA) using fundamental variables (such as risk, growth and cash flows). Regressions offer three advantages over the subjective approach:

- a. The output from the regression gives us a measure of how strong the relationship is between the multiple and the variable being used. Thus, if we are contending that higher growth companies have higher PE ratios, the regression should yield clues to both how growth and PE ratios are related (through the coefficient on growth as an

valuations of private firms: an empirical investigation, Accounting Horizons 13, 177–199.

<sup>117</sup> Easton, P., 2004, PE Ratios, PEG Ratios and Estimating the Implied Expected Rate of Return on Equity Capital, The Accounting Review, v79, 79-95.

independent variable) and how strong the relationship is (through the t statistics and R squared).

- b. If the relationship between a multiple and the fundamental we are using to explain it is non-linear, the regression can be modified to allow for the relationship.
- c. Unlike the modified multiple approach, where we were able to control for differences on only one variable, a regression can be extended to allow for more than one variable and even for cross effects across these variables.

In general, regressions seem particularly suited to our task in relative valuation, which is to make sense of voluminous and sometimes contradictory data. There are two key questions that we face when running sector regressions:

- The first relates to how we define the sector. If we define sectors too narrowly, we run the risk of having small sample sizes, which undercut the usefulness of the regression. Defining sectors broadly entails fewer risks. While there may be large differences across firms when we do this, we can control for those differences in the regression.
- • The second involves the independent variables that we use in the regression. While the focus in statistics exercises is increasing the explanatory power of the regression (through the R-squared) and including any variables that accomplish this, the focus of regressions in relative valuations is narrower. Since our objective is not to explain away all differences in pricing across firms but only those differences that are explained by fundamentals, we should use only those variables that are related to those fundamentals. The last section where we analyzed multiples using DCF models should yield valuable clues. As an example, consider the PE ratio. Since it is determined by the payout ratio, expected growth and risk, we should include only those variables in the regression. We should not add other variables to this regression, even if doing so increases the explanatory power, if there is no fundamental reason why these variables should be related to PE ratios.

# *Market Regression*

Searching for comparable firms within the sector in which a firm operates is fairly restrictive, especially when there are relatively few firms in the sector or when a firm operates in more than one sector. Since the definition of a comparable firm is not one that is in the same business but one that has the same growth, risk and cash flow

characteristics as the firm being analyzed, we need not restrict our choice of comparable firms to those in the same industry. The regression introduced in the previous section controls for differences on those variables that we believe cause multiples to vary across firms. Based upon the variables that determine each multiple, we should be able to regress PE, PBV and PS ratios against the variables that should affect them. As shown in the last section, the fundamentals that determine each multiple are summarized in table 2:

*Table 2: Fundamentals Determining Equity Multiples*

| Multiple |            |              | Fundamental      | Determinants |           |        |                 |
|----------|------------|--------------|------------------|--------------|-----------|--------|-----------------|
| Price    | Earnings   | Ratio        | Expected Growth, | Payout,      | Risk      |        |                 |
| Price    | to Book    | Equity Ratio | Expected Growth, | Payout,      | Risk, ROE |        |                 |
| Price    | to Sales   | Ratio        | Expected Growth, | Payout,      | Risk, Net | Margin |                 |
| EV       | to EBITDA  |              | Expected Growth, | Reinvestment |           | Rate,  | Risk, ROC, Tax  |
| EV       | to Capital | Ratio        | Expected Growth, | Reinvestment |           | Rate,  | Risk, ROC       |
| EV       | to Sales   |              | Expected Growth, | Reinvestment |           | Rate,  | Risk, Operating |

It is, however, possible that the proxies that we use for risk (beta), growth (expected growth rate in earnings per share), and cash flow (payout) are imperfect and that the relationship is not linear. To deal with these limitations, we can add more variables to the regression - e.g., the size of the firm may operate as a good proxy for risk.

The first advantage of this market-wide approach over the "subjective" comparison across firms in the same sector, described in the previous section, is that it does quantify, based upon actual market data, the degree to which higher growth or risk should affect the multiples. It is true that these estimates can contain errors, but those errors are a reflection of the reality that many analysts choose not to face when they make subjective judgments. Second, by looking at all firms in the market, this approach allows us to make more meaningful comparisons of firms that operate in industries with relatively few firms. Third, it allows us to examine whether all firms in an industry are under- or overvalued, by estimating their values relative to other firms in the market.

In one of the earliest regressions of PE ratios against fundamentals across the market, Kisor and Whitbeck(1963) used data from the Bank of New York for 135 stocks to arrive at the following result. 118

P/E = 8.2 + 1.5 (Growth rate in Earnings) + 6.7 (Payout ratio) - 0.2 (Standard Deviation in EPS changes)

Cragg and Malkiel (1968) followed up by estimating the coefficients for a regression of the price-earnings ratio on the growth rate, the payout ratio and the beta for stocks for the time period from 1961 to 1965.119

| Year |     |         |        |     | Equation |   |      |   | R2   |
|------|-----|---------|--------|-----|----------|---|------|---|------|
| 1961 | P/E | = 4.73  | + 3.28 | g + | 2.05     | π | 0.85 | β | 0.70 |
| 1962 | P/E | = 11.06 | + 1.75 | g + | 0.78     | π | 1.61 | β | 0.70 |
| 1963 | P/E | = 2.94  | + 2.55 | g + | 7.62     | π | 0.27 | β | 0.75 |
| 1964 | P/E | = 6.71  | + 2.05 | g + | 5.23     | π | 0.89 | β | 0.75 |
| 1965 | P/E | = 0.96  | + 2.74 | g + | 5.01     | π | 0.35 | β | 0.85 |

where,

P/E = Price/Earnings Ratio at the start of the year

### $$g = \text{Growth rate in Earnings}$$

$$\pi = \text{Earnings payout ratio at the start of the year}$$

β = Beta of the stock

They concluded that while such models were useful in explaining PE ratios, they were of little use in predicting performance. In both of these studies, the three variables used – payout, risk and growth – represent the three variables that were identified as the determinants of PE ratios in an earlier section.

The regressions were updated in Damodaran (1996, 2002) using a much broader sample of stocks and for a much wider range of multiples.120 The results for PE ratios from 1987 to 1991 are summarized below.

<sup>118</sup> Kisor, M., Jr., and V.S. Whitbeck, 1963, A New Tool in Investment Decision-Making, Financial Analysts Journal, v19, 55-62.

<sup>119</sup> Cragg, J.G., and B.G. Malkiel, 1968, The Consensus and Accuracy of Predictions of the Growth of Corporate Earnings, Journal of Finance, v23, 67-84.

<sup>120</sup> Damodaran, A., 1996 & 2004, Investment Valuation, John Wiley and Sons (first and second editions). These regressions look at all stocks listed on the COMPUSTAT database and similar regressions are run using price to book, price to sales and enterprise value multiples. The updated versions of these regressions

| Year |    |            |       |        | Regression  |               | R squared |
|------|----|------------|-------|--------|-------------|---------------|-----------|
| 1987 | PE | = 7.1839 + | 13.05 | PAYOUT | 0.6259 BETA | + 6.5659 EGR  | 0.9287    |
| 1988 | PE | = 2.5848 + | 29.91 | PAYOUT | 4.5157 BETA | + 19.9143 EGR | 0.9465    |
| 1989 | PE | = 4.6122 + | 59.74 | PAYOUT | 0.7546 BETA | + 9.0072 EGR  | 0.5613    |
| 1990 | PE | = 3.5955 + | 10.88 | PAYOUT | 0.2801 BETA | + 5.4573 EGR  | 0.3497    |
| 1991 | PE | = 2.7711 + | 22.89 | PAYOUT | 0.1326 BETA | + 13.8653 EGR | 0.3217    |

Note the volatility in the R-squared over time and the changes in the coefficients on the independent variables. For instance, the R squared in the regressions reported above declines from 0.93 in 1987 to 0.32 in 1991 and the coefficients change dramatically over time. Part of the reason for these shifts is that earnings are volatile and the price-earnings ratios reflect this volatility. The low R-squared for the 1991 regression can be ascribed to the recession's effects on earnings in that year. These regressions are clearly not stable, and the predicted values are likely to be noisy. In addition, the regressions for book value and revenue multiples consistently have higher explanatory power than the regressions for price earnings ratios.

### *Limitations of Statistical Techniques*

Statistical techniques are not a panacea for research or for qualitative analysis. They are tools that every analyst should have access to, but they should remain tools. In particular, when applying regression techniques to multiples, we need to be aware of both the distributional properties of multiples that we talked about earlier in the paper and the relationship among and with the independent variables used in the regression.

- The distribution of multiple values across the population is not normal for a very simple reason; most multiples are restricted from taking on values below zero but can be very large positive values.<sup>121</sup> This can pose problems when using standard regression techniques, and these problems are accentuated with small samples, where the asymmetry in the distribution can be magnified by the existence of a few large outliers.

are online at http://www.damodaran.com. The growth rate over the previous 5 years was used as the expected growth rate and the betas were estimated from the CRSP tape.

<sup>121</sup> Damodaran, A., 2006, Damodaran on Valuation (Second Edition), John Wiley and Sons, New York. The distributional characteristics of multiples are described in chapter 7.

- • In a multiple regression, the independent variables are themselves supposed to be independent of each other. Consider, however, the independent variables that we have used to explain valuation multiples – cash flow potential or payout ratio, expected growth and risk. Across a sector and over the market, it is quite clear that high growth companies will tend to be risky and have low payout. This correlation across independent variables creates “multicollinearity” which can undercut the explanatory power of the regression.
- • The distributions for multiples change over time, making comparisons of PE ratios or EV/EBITDA multiples across time problematic. By the same token, a multiple regression where we explain differences in a multiple across companies at a point in time will itself lose predictive power as it ages. A regression of PE ratios against growth rates in early 2005 may therefore not be very useful in valuing stocks in early 2006.
- As a final note of caution, the R-squared on relative valuation regressions will almost never be higher than 70% and it is common to see them drop to 30 or 35%. Rather than ask the question of how high an R-squared has to be to be meaningful, we would focus on the predictive power of the regression. When the R-squared decreases, the ranges on the forecasts from the regression will increase.

### *Reconciling Relative and Discounted Cash Flow Valuations*

The two approaches to valuation – discounted cash flow valuation and relative valuation – will generally yield different estimates of value for the same firm at the same point in time. It is even possible for one approach to generate the result that the stock is under valued while the other concludes that it is over valued. Furthermore, even within relative valuation, we can arrive at different estimates of value depending upon which multiple we use and what firms we based the relative valuation on.

The differences in value between discounted cash flow valuation and relative valuation come from different views of market efficiency, or put more precisely, market inefficiency. In discounted cash flow valuation, we assume that markets make mistakes, that they correct these mistakes over time, and that these mistakes can often occur across entire sectors or even the entire market. In relative valuation, we assume that while markets make mistakes on individual stocks, they are correct on average. In other words,

when we value a new software company relative to other small software companies, we are assuming that the market has priced these companies correctly, on average, even though it might have made mistakes in the pricing of each of them individually. Thus, a stock may be over valued on a discounted cash flow basis but under valued on a relative basis, if the firms used for comparison in the relative valuation are all overpriced by the market. The reverse would occur, if an entire sector or market were underpriced.

Kaplan and Ruback (1995) examine the transactions prices paid for 51 companies in leveraged buyout deals and conclude that discounted cash flow valuations yield values very similar to relative valuations, at least for the firms in their sample. <sup>122</sup> They used the compressed APV approach, described in an earlier section, to estimate discounted cash flow values and multiples of EBIT and EBITDA to estimate relative values. Berkman, Bradbury and Ferguson (2000) use the PE ratio and discounted cash flow valuation models to value 45 newly listed companies on the New Zealand Stock Exchange and conclude that both approaches explain about 70% of the price variation and have similar accuracy.123 In contrast to these findings, Kim and Ritter (1998) value a group of IPOs using PE and price to book ratios and conclude that multiples have only modest predictive ability.124 Lee, Myers and Swaminathan (1999) compare valuations obtained for the Dow 30 stocks using both multiples and a discounted cash flow model, based upon residual income, and conclude that prices are more likely to converge on the latter in the long term. While the evidence seems contradictory, it can be explained by the fact the studies that find relative valuation works well look at cross sectional differences across stocks, whereas studies that look at pricing differences that correct over time conclude that intrinsic valuations are more useful. 125

### **Directions for future research**

As we survey the research done on valuation in the last few decades, there are three key trends that emerge from the research. First, the focus has shifted from valuing

<sup>122</sup> Kaplan, S.N. and R.S. Ruback, 1995, The Valuation of Cash Flow Forecasts: An Empirical Analysis, Journal of Finance, v50, 1059-1093.

<sup>123</sup> Berkman, H., M.E. Bradbury and J. Ferguson, 2000, The Accuracy of Price-Earnings and Discounted Cash Flow Methods of IPO Equity Valuation, Journal of International Financial Management and Accounting, v11, 71-83.

<sup>124</sup> Kim, M. and J. R. Ritter (1999): Valuing IPOs, Journal of Financial Economics, v53, 409-437.

<sup>125</sup> Lee, C.M.C., J. Myers and B.Swaminathan, 1999, What is the intrinsic value of the Dow?, Journal of Finance, v54, 1693-1741.

stocks through models such as the dividend discount model to valuing businesses, representing the increased use of valuation models in acquisitions and corporate restructuring (where the financing mix is set by the acquirer) and the possibility that financial leverage can change quickly over time. Second, the connections between corporate finance and valuation have become clearer as value is linked to a firm's actions. In particular, the excess return models link value directly to the quality of investment decisions, whereas adjusted present value models make value a function of financing choices. Third, the comforting conclusion is that all models lead to equivalent values, with consistent assumptions, which should lead us to be suspicious of new models that claim to be more sophisticated and yield more precise values than prior iterations.

The challenges for valuation research in the future lie in the types of companies that we are called upon to value. First, the shift of investments from developed markets to emerging markets in Asia and Latin America has forced us to re-examine the assumptions we make about value. In particular, the interrelationship between corporate governance and value, and the question of how best to deal with the political and economic risk endemic to emerging markets have emerged as key topics. Second, the entry of young companies into public markets, often well before they have established revenue and profit streams, requires us to turn our attention to estimation questions: How best do we estimate the revenues and margins for a firm that has an interesting product idea but no commercial products? How do we forecast the reinvestment needs and estimate discount rates for such a firm? Third, with both emerging market and young companies, we need to reassess our dependence on current financial statement values as the basis for valuation. For firms in transition, in markets that are themselves changing, we need to be able to allow for significant changes in fundamentals, be they risk parameters, debt ratios and growth rats, over time. In short, we need dynamic valuation models rather than the static ones that we offer as the default currently. Fourth, as the emphasis has shifted from growth to excess returns as the driver of value, the importance of tying corporate strategy to value has also increased. After all, corporate strategy is all about creating new barriers to entry and augmenting or preserving existing ones, and much work needs to be done at the intersection of strategy and valuation. Understanding why a company earns excess returns in the first place and why those excess returns may

come under assault is a pre-requisit for good valuation. Finally, while the increase in computing power and easy access to statistical tools has opened the door to more sophisticated variations in valuation, it has also increased the potential for misuse of these tools. Research on how best to incorporate statistical tools into the conventional task of valuing a business is needed. In particular, is there a place for simulations in valuation and if so, what is it? How about scenario analysis or neural networks? The good news is that there is a great deal of interesting work left to be done in valuation. The bad news is that it will require a mix of interdisciplinary skills including accounting, corporate strategy, statistics and corporate finance for this research to have a significant impact.

#### **Conclusion**

Since valuation is key to so much of what we do in finance, it is not surprising that there are a myriad of valuation approaches in use. In this paper, we examined three different approaches to valuation, with numerous sub-approaches within each. The first is discounted cash flow valuation, where the value of a business or asset is determined by its cash flows and can be estimated in one of four ways: (a) expected cash flows can be discounted back at a risk-adjusted discount rate (b) uncertain cash flows can be converted into certainty equivalents and discounted back at a riskfree rate (c) expected cash flows can be broken down into normal (representing a fair return on capital invested) and excess return cash flows and valued separately and (d) the value of the asset or business is first estimated on an all-equity funded basis and the effects of debt on value are computed separately. Not surprisingly, given their common roots, these valuation approaches can be shown to yield the same value for an asset, if we make consistent assumptions. In practice, though, proponents of these approaches continue to argue for their superiority and arrive at very different asset values, often because of difference in the implicit assumptions that they make within each approach.

The second approach has its roots in accounting, and builds on the notion that there is significant information in the book value of a firm's assets and equity. While there are few who would claim that the book value is a good measure of the true value, there are approaches that build on the book value and accrual earnings to arrive at consistent estimates of value. In recent years, there has also been a push towards fair

value accounting with the ultimate objective of making balance sheets more informative and value relevant.

The third approach to valuation is relative valuation, where we value an asset based upon how similar assets are priced. It is built on the assumption that the market, while it may be wrong in how it prices individual assets, gets it right on average and is clearly the dominant valuation approach in practice. Relative valuation is built on standardized prices, where we scale the market value to some common measure such as earnings, book value or revenues, but the determinants of these multiples are the same ones that underlie discounted cash flow valuation.