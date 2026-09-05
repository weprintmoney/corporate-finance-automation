---
title: "Regressions of Multiples- 2008"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg08.html
---

Regressions of Multiples- 2008     **January 2008** 

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
intercept. The R squared reported for regressions without intercepts cannot
be directly compared to the regressions with intercepts - they will be higher.

All
of the percentages are entered in decimals (I am sorry but I have
gone back and
forth with this...
In this
iteration,
all
numbers
are
decimals). Thus, a firm with an expected growth rate of 30%, a payout
ratio of 10% and
a beta
of 1.25 can be expected to have a PE of:  
PE = 2.74 + 142.63 (.30) + 5.67 (.10) + 0.55 (1.25) = 46.78

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
> PE = 2.74 + 142.63 g + 5.67 Payout +0.55 Beta (R2 = 41.8%)
> [[Details](regrJan08US.htm#pe "PE Ratio Regression")]
>
> PEG = 0.133 Beta + 0.541 Payout - 0.78 ln(g) (R2 =
> 82.5%) [[Details](regrJan08US.htm#peg "PE Ratio Regression")]
>
> PBV= 18.02 g - 2.344 Payout - 0.110 Beta + 17.3 ROE (R2=
> 64.0%) [[Details](regrJan08US.htm#pbv "PBV Regression")]
>
> PS= 14.93 g - 1.892 Payout - 0.632 Beta + 21.83 Net Margin (R2=
> 74.3%) [[Details](regrJan08US.htm#ps "PS Ratio Regression")]

*Firm Value Multiples*

> Enterprise Value/Book Capital= 41.33 g (rev) + 11.34 (Return
> on Capital) - 8.67 (Debt/Capital) (R2 =
> 70.0%) [[Details](regrJan08US.htm#evcap "Value/Sales Ratios")]
>
> Enterprise Value/Sales = 26.49 g(rev) + 7.56 Pre-tax Operating
> Margin - 4.67 (Debt/Capital) (R2 =
> 74.7%) [[Details](regrJan08US.htm#evsales "Value/Sales Ratios")]
>
> Enterprise Value /EBITDA= 4.490 + 96.97 g(rev) - 9.28 (Tax rate)
> + 1.745 Return on Capital - 1.837 Reinvestment Rate (R2=44.8
> %) [[Details](regrJan08US.htm#evebitda)]

*To see the more detailed output from the regression, click on 'Details'*.

### Europe

> PE = 14.15 + 7.488 Payout Ratio -2.62 Beta + 29.06 g (R2 =
> 17.9%) [[Details](EuroregrJan2008.htm#PE "Value/Sales Ratios")]
>
> PBV = 1.475 + 2.37 g + 0.05 Payout Ratio - 0.88 Beta + 12.58 ROE
> (R2 =
> 38.6%) [[Details](EuroregrJan2008.htm#PBV "Value/Sales Ratios")]
>
> PS = 1.085 -0.03 Payout Ratio + 1.68 g - 0.605 Beta + 12.34 Net Margin
> (R2 =
> 32.8%) [[Details](EuroregrJan2008.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital= 2.446 + 4.702 Return on Capital - 2.29 Debt/Capital
> (R2= 27.7%)
> [[Details](EuroregrJan2008.htm#EVCap)]
>
> EV/EBITDA = 6.54+ 43.75 (Debt/Capital) + 2.91 g-
> 12.45 Tax Rate (R2=31.5%) [[Details](EuroregrJan2008.htm#EVEBITDA)]
>
> EV/Sales =0.955 + 6.785 (Debt/Capital) +6.064 After-tax Operating
> Margin (R2=25.6%) [[Details](EuroregrJan2008.htm#EVSales)]

### Emerging Markets

> PE = 5.63 + 2.707 Payout Ratio + 11.354 Beta + 92.72 g (R2 =
> 13.9%) [[Details](EmMkRegrJan08.htm#PE "Value/Sales Ratios")]
>
> PBV = 10.02 g + .205 Payout Ratio + 1.362 Beta + 14.27 ROE (R2 =
> 72.1%) [[Details](EmMkRegrJan08.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.071 Payout Ratio + 8.37 g + 1.03 Beta + .16.03 Net Margin (R2 =
> 69.3%) [[Details](EmMkRegrJan08.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital= 5.262 +6.189 Return on Capital - 13.268 Debt/Capital +
> 5.97 g (R2=33.3%) [[Details](EmMkRegrJan08.htm#EVCAP)]
>
> EV/EBITDA = 41.85+ 63.79 (Debt/Capital) + 52.72 g- 46.65 Tax Rate (R2=12.7%)
> [[Details](EmMkRegrJan08.htm#EVEBITDA)]
>
> EV/Sales = 4.412 +7.086 g -10.58 (Debt/Capital) +16.10 After-tax Operating
> Margin (R2=27.5%) [[Details](EmMkRegrJan08.htm#EVSALES)]

### Japan

> PE = 13.55 + 26.05 Payout Ratio + 1.25 Beta + 11.87 g (R2 =
> 18.4%) [[Details](JapanregrJan08.htm#PE "Value/Sales Ratios")]
>
> PBV = 0.407 - 0.503 Beta + 19.26 ROE +.175 Payout Ratio (R2 =
> 33.9%) [[Details](JapanregrJan08.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.85 - 0.019 Payout Ratio - 0.406 Beta + 13.51 Net Margin + 0.405
> g (R2 =
> 36.6%) [[Details](JapanregrJan08.htm#PS "Value/Sales Ratios")]
>
> EV/EBITDA = 5.30 + 20.98 (Debt/Capital) +16.38 Return on
> Capital - 3.15
> Tax Rate (R2=14.6 %) [[Details](JapanregrJan08.htm#EVEBITDA)]
>
> EV/Book Capital= 1.25+ 0.665 (Debt/Capital)+ 6.735 Return on
> Capital (R2=
> 53.4%) [[Details](JapanregrJan08.htm#EVCap)]
>
> EV/Sales = 3.954 (Debt/Capital)+ 18.183 After-tax
> Operating Margin (R2=
> 59.1%) [[Details](JapanregrJan08.htm#EVSales)]
