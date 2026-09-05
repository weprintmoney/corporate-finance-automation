---
title: "Regressions of Multiples- 2007"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg07.html
---

Regressions of Multiples- 2007     **January 2007** 

**Regressions of Multiples on Fundamentals: Market Wide**

The following regressions were run across four groupings. The first and
most comprehensive set of regressions were run across all traded companies
in the United States. The second set of regressions were run across all traded
companies in Western Europe and the UK. The third set of regressions were
run across companies in emerging markets in Asia, Eastern Europe and Latin
America. The final set of regressions were run across just Japanese companies.

1. [United States](#US)
2. [Europe](#Europe)
3. [Emerging Markets](#EmergingMkts)
4. [Japan](#Japan)

I have run the regressions with and without the intercept for most
of
the variables. Where the intercept is positive, I have reported on that regression.
Where the intercept is negative, I have reported the regression without
the
intercept. The R squared reported are from the regressions with intercepts
(since the R squared are artificially high when you remove the intercept).

All
of the percentages are entered as absolute values (I am sorry but I have
gone back and
forth with this...
In this
iteration,
all
numbers
are
absolute values). Thus, a firm with an expected growth rate of 30%, a payout
ratio of 10% and
a beta
of 1.25 can be expected to have a PE of:  
PE = 2.9127 (30) + .3774 (10) - 21.62 (1.25) = 64.13

The variables used in the regressions are listed below.

* g = Expected growth in earnings over the next 5 years
* Relative Growth = Expected growth in earnings/ Average growth rate for
  market
* g(rev) = Expected growth rate in revenues over the next 5 years (If you
  do not have this, use the expected growth rate in EPS)
* PE = Price/ Current EPS
* Relative PE = Current PE for company/ Average for the market
* PBV = Market value of equity/ Book value of equity
* PS = Market value of equity / Revenues in most recent financial year
* Enterprise Value = Market Value of Equity + Market Value of Debt - Cash
  and Marketable Securities
* Payout = DPS/EPS: from most recent year; if dividends are postive and
  earnings are negative, it is set to 100%.
* Relative Payout = Payout/ Average payout ratio for market
* Debt/Equity = Book Value of Debt/ Market value
  of Equity
* Debt/Capital = Book Value of Debt / (Book value of Debt + Market value
  of Equity)
* Beta = Betas based upon 5 years of data (You can use alternate periods,
  intervals or betas from an estimation service)
* Net Margin = Net Income / Sales
* After-tax Operating Margin = EBIT (1-tax rate) /Sales
* Pre-tax Operating Margin = EBIT/ Sales
* Tax Rate = Effective tax rate in most recent year
* ROE = Net Income / BV of Equity
* ROC = EBIT (1-t)/ (BV of Debt + BV of Equity- Cash
  )
* Reinvestment Rate = (Cap ex - Depreciation + Chg in non-cash WC)/ EBIT
  (1 - tax rate)
* Std dev in Stock Prices = Standard deviation in stock prices over last
  5 years. You can use alternate intervals.

### United States

*Equity Multiples*
> PE = 10.645 + 1.178 g + 0.074 Payout - 2.621 Beta (R2 = 41.4%)
> [[Details](regrJan07US.htm#PE "PE Ratio Regression")]
>
> PE = 11.298 + 1.169 g - 2.834 Beta (R2 = 40.0%)
> [[Details](regrJan07US.htm#PE "PE Ratio Regression")]
>
> PEG = 6.480 + 1.060 Beta - 0.007 Payout - 2.140 ln(g) (R2 =
> 21.4%) [[Details](regrJan07US.htm#PEG "PE Ratio Regression")]
>
> Relative PE =0.239+ 0.470 Relative g + 0.012 Relative Payout - 0.060 Beta
> (R2=
> 40.8%) [[Details](regrJan07US.htm#RelPE "PE Ratio Regression")]
>
> PBV= 0.161 ROE - 0.970 Beta + 0.155 g (R2=
> 59.8%) [[Details](regrJan07US.htm#PBV "PBV Regression")]
>
> PS= 0.100 g - 0.0031 Payout - 0.966 Beta + 0.212 Net Margin (R2=
> 63.4%) [[Details](regrJan07US.htm#PS "PS Ratio Regression")]

*Firm Value Multiples*

> Enterprise Value/Book Capital= 0.171 g (rev) + .120 (Return
> on Capital) - 0.002 (Debt/Equity) (R2 =
> 57.1%) [[Details](regrJan07US.htm#EVCAP "Value/Sales Ratios")]
>
> Enterprise Value/Sales = 0.149 g(rev) + 0.080 Pre-tax Operating
> Margin - 0.012 (Debt/Equity) (R2 =
> 47.1%) [[Details](regrJan07US.htm#EVSALES "Value/Sales Ratios")]
>
> Enterprise Value /EBITDA= 6.081 + 0.926 g(rev) - .126 (Tax rate)
> - 0.068 (Debt/Equity)-0.0153 Reinvestment Rate (R2=36.5
> %) [[Details](regrJan07US.htm#EVEBITDA)]

*To see the more detailed output from the regression, click on 'Details'*.

### Europe

> PE = 18.364 + 0.036 Payout Ratio - 4.074 Beta + 0.578 g (R2 =
> 8.6%) [[Details](EuroregrJan2007.htm#PE "Value/Sales Ratios")]
>
> PBV = 0.512 + 0.093 g + .017 Payout Ratio -0.415 Beta + .135 ROE (R2 =
> 20.3%) [[Details](EuroregrJan2007.htm#PBV "Value/Sales Ratios")]
>
> PS = 4.497 -0.017 Payout Ratio -1.368 Beta + .0.075 Net Margin (R2 =
> 15.4%) [[Details](EuroregrJan2007.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital= 1.874 +0.136 Return on Capital - 0.019 Debt/Capital
> (R2=23.8%)
> [[Details](EuroregrJan2007.htm#EVCap)]
>
> EV/EBITDA = 19.069+ 0.412 (Debt/Capital) - 0.229 Return on Capital-
> .242 Tax Rate (R2=34.4%) [[Details](EuroregrJan2007.htm#EVEBITDA)]
>
> EV/Sales = 0.636 + 0.086 (Debt/Capital) +0.096
> After-tax Operating Margin (R2=30.4%) [[Details](EuroregrJan2007.htm#EVSales)]

### Emerging Markets

> PE = 11.603 + .080 Payout Ratio -0.115 Beta + 0.856 g (R2 =
> 26.4%) [[Details](EmMkRegrJan07.htm#PE "Value/Sales Ratios")]
>
> PBV = 0.093 g+ .006 Payout Ratio - 0.414 Beta + 0.188 ROE (R2 =
> 48.4%) [[Details](EmMkRegrJan07.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.564 + .002 Payout Ratio - 1.689 Beta + .281 Net Margin + 0.078
> g (R2 =
> 30.3%) [[Details](EmMkRegrJan07.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital = 1.737 +.138 Return on Capital -.016 (Debt/Capital) -0.002
> Reinvestment Rate (R2 =
> 52.2%) [[Details](EmMkRegrJan07.htm#EVCap "Value/Sales Ratios")]
>
> EV/EBITDA = 36.421 - 0.385 (Debt/Capital) -0.336 Return on Capital-
> .265 Tax Rate + 0.282 g (R2= 14.4%) [[Details](EmMkRegrJan07.htm#EVEBITDA)]
>
> EV/Sales = 5.062 - 0.065 (Debt/Capital) +0.107
> After-tax Operating Margin (R2=25.3%) [[Details](EmMkRegrJan07.htm#EVSales)]

### Japan

> PE = 0.702 Payout Ratio + 6.237 Beta + 0.263 g (R2 =
> 37.3%) [[Details](JapanregrJan07.htm#PE "Value/Sales Ratios")]
>
> PBV = 0.246 Beta + .181 ROE +.010 Payout Ratio (R2 =
> 34.6%) [[Details](JapanregrJan07.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.012 Payout Ratio - 0.017 Beta + 0.203 Net Margin (R2 =
> 54.3%) [[Details](JapanregrJan07.htm#PS "Value/Sales Ratios")]
>
> EV/EBITDA = 10.104 + 0.196 (Debt/Capital) +0.124 Return on
> Capital - 0.065
> Tax Rate (R2=11.5 %) [[Details](JapanregrJan07.htm#EVEBITDA)]
>
> EV/Book Capital= 0.0009 (Debt/Capital)+ 0.268 Return on
> Capital (R2=
> 54.6%) [[Details](JapanregrJan07.htm#EVCap)]
>
> EV/Sales = 0.0497 (Debt/Capital)+ 0.276 After-tax
> Operating Margin - 0.0121 Tax Rate (R2=
> 51.8%) [[Details](JapanregrJan07.htm#EVSales)]
