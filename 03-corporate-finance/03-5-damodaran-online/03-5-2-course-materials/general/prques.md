---
title: "Project Questions"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/project/prques.htm
---

Project Questions

**[![](../Budimage/acf2E.gif)](../cfproj.html)**

# troubleshooting

These are a few of the questions that come up in the context of analyzing a
firm. A few of the questions you have may already be answered here. I
am sure that you will come up with a few that I have not answered before.

---

**I. The Stakeholders in the Firm**

*How do I know if managers are responsive to stockholders?*

> Barring the cases where a firm is on the watch list of Calpers or the Lens Fund, this is a subjective judgment that you have to make based upon the evidence you collect. Consider, for instance, the following indicators of managerial interests versus stockholder interests:
>
> *Clear and Compelling Evidence of Managerial Interests Dominating*

- Getting on the watch list for CalPers or the Lens Fund
- Actions taken by management where stockholder interests are clearly
  violated. Examples would include:
  * Greenmail
  * Large increases in compensation while stock price is
    dropping
  * Changing terms of compensation contract to benefit
    existing managers, without stockholder approval (Golden
    parachutes, Changing exercise price or terms on management
    options)
  * Rejecting a higher price in a takeover battle, while
    accepting a lower price

> *Likely Evidence of Managerial Interests Dominating*

- Having a board of directors dominated by insiders or cronies of the
  CEO
- Creating voting and non-voting classes of shares, where the voting
  shares are disproportionately held by managers
- Pushing for and passing anti-takeover amendments

> For many companies outside the United States, the analysis is often driven by broader institutional protection that might exist for incumbent management.

*How do I assess the firm's relationship with financial markets?*

> The dynamics of a firm's relationship to financial markets is best seen around earnings announcements, when analysts following the firm and the managers of the firm duel to control the market reaction to the announcement. Again, it is more or a subjective assessment than an objective one. Generally speaking,
>
> * Firms which are followed by lots of analysts will tend to be more careful
>   about their dealings with markets than those followed by no or few analysts
> * The more independent analysts are of the firm (look at the buy/sell
>   breakdown on recommendations), the more likely it is that unbiased information
>   will reach markets promptly
> * Heavily traded stocks are more likely to have market prices that reflect
>   true value than lightly traded stocks.

*How do I understand a firm's social standing?*

+ Start with the annual report. While talk is cheap, you will still find
  the emphasis on social responsibility varies widely across reports.
+ Check news reports for recent tangles the firm might have had with social
  groups, and see how it deals with these problems, when they arise.

---

**II. Stockholder Type**

*Who is a marginal investor?*

In theory, the marginal investor is the one who trades at the margin and sets prices. No one can really tell who the marginal investor is, but it is reasonable to conclude that

* if most of the stock is held by institutional investors, that the marginal investor is an institutional investor* if the stock is closely held, and if one or more of the large stockholders
    is part of the top management (or the CEO), that the marginal investor
    may be an insider... Even in this case, check to see whether institutional
    investors are active.

*Why do we care?*

Risk and return models assume that the marginal investor is well diversified and that only the non-diversifiable risk matters. If the marginal investor is the institutional investor, this is likely to be true. If, on the other hand, the marginal investor is the insider, this may be a more dangerous assumption, since most insiders are not well diversified.

---

**III. Risk And Return**

**Data**   
You can use the beta calculation page on Bloomberg to get your risk and return
regression. You can skip this section on running a regression and go
to the section on reading the output. If you decide to run your own
regression, you will need to collect the data on stock prices and index
returns for the period.

> *Where do I get the data and what data should I get?*
>
> > The data is easily available on most services. You can get it, for instance, from both Bloomberg and the Dow Jones News Retreival Service.
> >
> > - ***For your stock:*** You need month-end prices for 60 months. If your stock has been traded less than 3 years, get week-end prices for 2 years). In addition, you need
> >
> > * dollar dividends per share during the period and ex-dividend dates
> > * stock splits and split dates (if your prices are not split adjusted)
> >
> >   (Bloomberg prices are split adjusted)
> >
> > - ***For the index***: You need month-end index levels for 60 months, preferably with dividends included.
>
> *Which index should I use?*
>
> > While the services tend to use the S&P 500 index in the US, and
> > the most widely known local index outside the US, it is worth remembering
> > that the index, in the CAPM, should include all traded assets, held in
> > proportion to their market value. Using that definition, we would argue
> > that
> >
> > * broader indices are better than narrower indices (S&P 500 vs
> >   Dow 30)
> > * indices that are value weighted are better than equally weighted
> >   indices
> > * indices that include non-equity assets in addition to stocks are
> >   better than pure equity indices
> >
> > From a practical perspective, start with a fairly well diversified and
> > widely used index (S&P 500 for the US), and then examine what
> > happens when you change the index to a Global index, for instance.
>
> *How far back should I go?*
>
> > I generally go back 5 years, since I use monthly returns. The beta estimates tend to be better with longer return intervals (like months) than with shorter return intervals (days or weeks). If I do have the data for 3 years or less, I would use weekly returns to get the beta.
>
> *\* What should I check for?*
>
> * Make sure prices are month-end and not average prices.
> * Both index and stock are measured on the same day

**Inputting the data**

*\* How do I enter the stock prices?*

- *If you have 60 months of data*: Start with the earliest month in period 1 and work down.

- *If you have less than 60 months of data*:

* Enter the number of periods for which you have data on the top of the spreadsheet.* Enter the data starting the earliest month in period 1 and work down.* **Do not delete the extra rows**.

*\* How do I enter dividends?*

* Enter the dollar dividends per share in the ex-dividend month

*\* What about stock splits?*

* If the prices are split-adjusted -> Ignore stock splits* If not -> Enter the split in the ex-month
    + Enter the split factor (i.e. 2 for a two-for-one split ....)+ Make sure you take out the splits that are already on the spreadsheet

(*Practical hint*: If you enter the split factor and the return jumps to a very high number (80%, 90%..) then you probably entered the data in the wrong month.)

*\* What about the initial inputs?*

- *For current price* : Use as current a price as possible (This will obviously shift on you. Agree on a specific day, if necessary, and use it as the current day)

- *For current DPS*: This is the annualized dividends per share currently paid by the firm. This can be easily calculated by taking the last quarter's dividends (if dividends are quarterly) and multiplying by four.

- *For current riskfree rate*: Use current long-term bond rate

- *For risk premium*: Use the premium, based upon historical data,
that matches your riskfree rate. (For the U.S. : Look at historical
returns in the data page)

- *For riskfree rate during the period of the regression*: Use the average T.Bill rate during the period of the regression. You can get this from the historical return data set that I have on the web.

**Reading the output**

Beta

*Why would my beta be zero or negative?*

*Calculation or Input Errors*

* You mismatched the data - entered stock prices from one point in time and the index from another.* You forgot to update the index.* You forgot to blank out an split factor from a previous regression

      *Other Reasons*

      * If you have a short estimation period, and your stock was exposed to a significant event (bankruptcy, merger etc.) during a portion of the period, the beta can be very low or negative. (These events push the returns in one direction, reducing the correlation with the market)* Your company may be one of those that moves in the opposite direction
          of the economy, in which case it should have a negative beta.

*How do I know how precise my beta estimate is and whether I can depend upon it?*

* Look at the standard error on your beta estimate. High standard errors are usually indicative of imprecise betas.* Check to see if your firm has changed its business and financial mix during the period. If it has, the beta estimate is probably not very useful looking forward.* Estimate a bottom-up beta, by taking a weighted average of the unlevered betas of the sectors in which the firm is currently operating, and then using the firm's current financial leverage to estimate a new beta. If this beta is very different from the regression beta, go with the bottom-up beta.

*If I estimate both a regrssion beta and a bottom-up beta, which one should I use?*

In almost every case, the bottom-up beta will give you a better estimate of the true beta than the regression beta.

*\* How do I know if my beta is different from that estimated by a service?*

Using the standard error estimated on the beta, estimate a range for the beta. In most cases, the service betas and your estimate will fall within the range.

*\* Why is my beta different from the Value Line or S&P estimates?*

Services use:

* different time periods (Bloomberg uses 2 years, for instance)* different return intevals (Value Line uses weekly)* beta adjustments towards one* fundamentals sometimes (Barra)

**Estimating Hurdle Rates**

*Cost of Equity*

*Which riskfree rate should I use for the computation?*

Use the current long term government bond rate. If the market you are working in does not have a long term bond rate, use the short term government bond rate.

*Which beta should I use?*

See answer to earlier question.

*Which risk premium should I use?*

For the United States, use the most recent historical premium or the current
implied equity premium. If you are working on a market outside the
US, check the country's rating, and add a spread
to the U.S. premium based
upon the rating.

*Cost of Capital*

*How do I get a cost of debt?*

1. If your company has long term straight bonds traded on it: Use the yield to maturity on these bonds- If your company is rated: Use the interest rate that corresponds to the rating.- If your company is not rated: Estimate a synthetic rating, based upon the interest coverage ratio, and use the interest rate that corresponds to the rating.

*What weights should I put on debt and equity?*

Use market value weights. For equity, this will be the market price per share times the number of shares outstanding. For debt, you should estimate the market value of the debt.

*What do I do about preferred stock?*

Treat it as a separate component of capital, and estimate the cost of preferred stock to be the preferred yield (Preferred Dividend/Preferred Stock Price)

*What about convertible debt?*

Decompose the convertible debt into straight debt and conversion option components. Add the straight debt to the debt portion and the conversion option to equity.

---

**IV. Measuring Investment Return**

*How do I measure returns on equity and capital?*

> The conventional measures of returns on equity and capital are as follows:
>
> Return on Equity = Net Income in year t/Book Value of Equity at t-1
>
> Return on Capital = EBIT (1-t) / (BV of Debt at t-1 + BV of Equity at
> t-1- Cash at t-1)
>
> (If your companies have had significant cash balances, you should net
> the cash out of the denominator of the return on capital computatin)

*Should I look at income before or after extraordinary items?*

Always look at income before extraordinary items

*What tax rate should I use for return on capital?*

Use the marginal tax rate. In most cases, this should be set by the tax
code (35-38% in the US). If the effective tax rate is greater than
the marginal tax rate, you can use the effective tax rate, but make
sure it is reasonable) If you have a non-US company, check my web site
for margiinal corporate tax rates.

*Should I look at only the most recent year or over several years?*

Start with the most recent year but also look at trends. There might be useful information there.

*What do I do if the book value of equity is negative?*

You cannot compute the return on equity in this case.

*How will equity repurchases or special dividends affect my calculations?*

The immediate effect of an equity repurchase will be a jump in both your returns on equity and capital. You should estimate the returns as if the repurchase did not occur (i.e., use the book value of equity without the repurchase adjustment)

*What beta and debt ratio should I use to compute the costs of equity and capital for the comparison to returns on equity and capital?*

Use the costs of equity and capital you estimated in the previous section.

---

**V and VI. Capital Structure**

**Data**

*\* Which financial year data should I use? Should I use actual or projected numbers?*

> - Use the most updated data you can find. If this means using the operating income from the most recent 12 months, rather than the most recent financial year, do so.

*Do I need to be consistent about how I get my data?*

> The only requirement is that you use the most current data you can for each input. This may mean using operating income from the most recent 12 months and capital expenditures from the most recent financial year.

*\* Should I use total or long term debt?*

> - Use all interest bearing debt (basically all debt except for accounts payable and a few other current liabilities). In general, this will include the short term borrowings in the current liabilities and the long term borrowings.

- **Exception:** If you are analyzing financial service firms, use long term debt.

*\* Should I treat operating leases and preferred stock as debt?*

> - Capitalized leases can be treated like debt, since lease payments share the tax- deductible characteristics of interest payments.
>
> - Do not treat preferred stock as debt, since preferred dividends are not tax deductible. (If preferred stock is a small component of total capital, you can ignore it. Otherwise, the spreadsheet has to be modified to consider preferred stock as a different source of capital.)

*\* Where do I get market values of debt and equity?*

> - If the firm is a publicly traded firm, the market value of equity is the market price multiplied by the number of shares outstanding. If it is a private firm, the equity will have to be valued separately.
>
> - If the bonds are not publicly traded, the market value of the debt can
> be estimated by discounting the interest payments and the book value of
> the debt by the market interest rate that corresponds to the companyís
> bond rating.

*\* Should I compute the cost of equity using short term or long term rates?*

> - Use the long term riskfree rate and the appropriate risk premium.

*\* Should I change the default spreads in the spreadsheets?*

> - If you want the most updated spreads, visit http://www.bondsonline.com

*\* What should I do if my company is not rated?*

> - Use the interest coverage ratio of the firm to assign it a rating, based upon the relationship between interest coverage ratios and bond ratings.

**Output stage**

*\* Why am I getting an optimal debt ratio of zero?*

+ Because that is your optimal
+ Because you micalculated EBITDA
+ Because the EBITDA you have used is abnormally low
  - You can normalize this EBITDA by doing one of the following
    1. average over a recent period (last five years, for
       instance)
    2. use the average return on capital and book capital
       to estimate normal EBIT.
    3. use the current rating of the company to back out EBITDA

- Current Rating -> Interest Coverage ratio -> Normalized
  EBITDA

*\* Why is the cost of capital higher and firm value lower under my optimal?*

> - Firm is currently over-rated (The bond rating claimed by the company is higher than the rating assigned to the company under the current debt ratio in the spreadsheet.)
>
> - You are under-rating the firm
>
> - Old debt at lower rates on the books

- Actual debt ratio is close to the optimal

*\* How do I do my "What -if" analysis?*

> - Decrease the EBITDA, if the firm's earnings are on an upswing.
>
> - Increase the EBITDA, if the firm's earnings are on a downswing.

---

**VII. Details of Debt**

**Input Stage**

*What data do I need to collect to do the capital structure regressions?*

1. You need to collect the following data for your firm

> - firm value (market value of equity + debt) for ten years or more
>
> [If you cannot get market value of debt, use book value]
>
> - EBITDA for each of the same periods

2. You also need to obtain macro economic information on the following ñ

> - Long term bond rates at the same points in time that you measured firm value
>
> - Inflation rates at the same point in time that you measured firm value
>
> - Exchange rates at the same point in time that you estimated firm value
>
> - Real GNP at the same points in time that you estimated firm value

*What do I do next?*

> Run a regression, where
>
> - percentage changes in firm value or EBITDA is the dependent variable (the Y variable)
>
> - changes in the macro economic variable (if it is already a percentage, like interest rates and inflation rates) or percentage changes in the macro economic variable (if it is an absolute value, like real GNP or Exchange rate) is the independent variable (the X variable)

*How do I read the output?*

> The slope coefficient in the regression is a measure of how much firm value (or EBITDA) changes on a percentage basis for a given percentage change in the macro economic variable.
>
> For instance, a coefficient of -2.48 in the regression of firm value on the long term bond rate implies that for every 1% increase in the long bond rate, firm value decreases by 2.48%.

*What if my output looks strange?*

> When you have annual data, and relatively few observations, one or a few outliers can give you strange looking output. You can try to get around this by
>
> - using quarterly or monthly data (at least for firm value)
>
> - looking at the industry averages for these coefficients.

---

**VIII. and IX. Dividend Policy**

**Input stage**

*\* Do I enter the data on a per-share basis or total numbers?*

> Be consistent but it is best to use total numbers all the way through.

*\* Where do I get stock repurchases?*

> This should be in the statement of cash flows under cashflows from financing.

*\* What is the return on stock? Where do I get it?*

> Return on Stock = (Price at t - Price at t-1 + Dividends in t) / Price
> at t-1
>
> If you cannot get prices for some years, use the average prices from the Value Line sheet.

*\* Where do I get the riskfree rate and return on the market?*

> The table at the end of the dividend policy analysis summarizes returns
> on T-Bills, T-Bonds and Stocks from 1928 to the most recent year. Take
> the returns for the years for which you have done the dividend analysis.

*\* Should I use the optimal debt ratio or the actual?*

> When looking at past data - use the actual debt ratio.
>
> When making forecasts for the future -> use the optimal or predicted
> debt ratio.

*\* Should I adjust the beta accordingly?*

> You should continue to use the actual beta of the firm, for looking at past data, and the recalculated beta for looking at the future.

**Output stage**

*\* How do I read the output?*

> Compare Dividends to FCFE
>
> Measure performance (Compare ROE to Required rate of return
>
> Compare Return on stock to Required rate of return)

*\* What if one suggests poor performance and the other suggests good performance?*

> The comparison of ROE to required rate of return is essentially an accounting analysis of past project performance; The comparison of stock returns to requirred returns is a financial market judgement on actions of the company. For long gestation projects, where the returns may lag the investment, management may argue that the latter is more relevant.

---

**X.** Valuation

**Model Choice**

*Which model should I use?*  
The model that has is simplest to use and will work with any company is fcffsimpleginzu.xls. It allows you to change margins and reinvestment assumptions and will value everything from young, start-ups to money losing, distressed firms. It also has default assumptions built into the model (which you can relax if you feel comfortable doing so) that prevent you from creating inconsistent valuations.For financial service firms where you really cannot estimate the cash
flows, use divginzu.xls. This is a dividend discount model. If you want to value a company based upon FCFE, you can try fcfeginzu.xls.

*If I try two different models, will I get the same value per share?*Generally not. You make implicit assumptions in each model that make them
difficult (though not impossible) to reconcile. That will have to wait
for a valuation class, though.

**Input Stage**

*\* What riskfree rate and premium do I use?*

> - Use today's long term risk free rate and an appropriate
> risk premium.

*\* Do I use acutal data or next yearís projections?*

> - Your objective is to make the best estimates for the future that you
> can. If this means using projections, do so.

*\* Can I use different sources of data?*

> Yes.

*\* Where do I get capital spending?*

> Your capital expenditures should be listed on the statement of cash flows.
> If this is not available, take the difference in net fixed assets
> from the previous year. This is the net capital expenditure. Add
> it to the depreciation to get total capital expenditures. Also, check
> for R&D and acquisitions (which are generally not classified as cap
> ex) but should be.

*\* Should I use total debt or long term debt?*

> Use all interest-bearing debt. In fact, be consistent with how you defined
> debt in the capital structure section. That would mean using debt
> inclusive of operating leases.

*\* What happens if I have negative or abnormal earnings?*

> You can normalize this earnings by doing one of the following
>
> - average over a recent period (last five years, for instance)
>
> - use industry average or your firm's own historical average margins (operating
> or net) to back into a normalized earnings number.
>
> - use the current rating of the company to back out EBITDA. Use this EBITDA
> to get earnings. For instance, you can get normalized net income
> by doing the following:
>
> Current Rating -> Interest Coverage ratio -> Normalized EBITDA -> Normalized
> E

*\* Can I change the fundamentals for the high growth period?*

> You can and you should, since the fundamentals will usually change from current numbers.

*\* How do I weight in historical growth and analyst estimates of growth?*

> Work as much as you can with the fundamental growth rate, since you control the inputs to the process. The historical growth rates and analyst estimates are exogeneous and do not relate growth to fundamentals.

*\* What growth rate do I use for capital spending, depreciation and working
capial?*

> While you can look at the company's history of growth on these variables,
> it is far safer to look at the consolidated value of these numbers:  
> Reinvestment = Cap Ex - Depreciation + Change in Working Capital  
> This can be used to compute a reinvestment rate that you can then forecast
> for the future. This forecast should be consistent with your growth assumptions.
> In other words, high growth usually requires high reinvestment rates.

***Terminal price***

*\* Do I use the perpetual growth model or a multiple?*

> If you are doing a discounted cash flow valuation, it is not a good practice
> to estimate the terminal value using a multiple. That introduces
> a relative value component into your DCF valuation.

*\* What growth rate do I use in perpetuity?*

> The stable growth rate should be less than or equal to the growth rate
> of the economy (computed consistently with whether you are doing
> a real or nominal valuation, and if the latter, what currency you
> are using).  
> A good rule of thumb is that the stable growth rate should not exceed the
> riskfree rate in your valuation.

*\* What about other inputs?*

In general, you should try to give your company all of the inputs that
stable growth companies have in the terminal value calculation. Summarizing:

1. Beta
   should move towards one
2. Debt ratio will probably shift higher towards
   an industry average
3. Return on capital should move towards the cost of
   capital
4. Reinvestment rates should ease. In fact, the stable period
   reinvestment rate is best computed as:  
   Stable reinvestment rate = Stable Growth rate/ Stable period Return
   on Capital

**Output Stage**

*\* Why is my value so low?*

> See [figure](valchklist.htm)

*\* Why is my value so high?*

> See [figure](valchklist.htm)

*\* What do I do if my value is very different from the market price?*

> Don't panic. Work methodically through your numbers to make sure that none of them are wrong.   
> If they look reasonable, remind yourself why you do DCF valuation. It is
> because markets sometimes make mistakes.

*\* Is my value correct?*

> Don't ask me. I do not know what the correct value of your company is.
