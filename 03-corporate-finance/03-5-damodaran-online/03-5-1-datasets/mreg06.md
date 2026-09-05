---
title: "Regressions of Multiples"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg06.html
---

Regressions of Multiples     **January 2006** 

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
* Beta = Betas based upon 3 years of data (You can use alternate periods
  or intervals)
* Net Margin = Net Income / Sales
* After-tax Operating Margin = EBIT (1-tax rate) /Sales
* Pre-tax Operating Margin = EBIT/ Sales
* Tax Rate = Effective tax rate in most recent year
* ROE = Net Income / BV of Equity
* ROC + EBIT (1-t)/ (BV of Debt + BV of Equity)
* Reinvestment Rate = (Cap ex - Depreciation + Chg in non-cash WC)/ EBIT
  (1 - tax rate)
* Std dev in Stock Prices = Standard deviation in stock prices over last
  5 years. You can use alternate intervals.

### United States

*Equity Multiples*
> PE = 6.747 + 1.131 g + 0.073 Payout -0.919 Beta (R2 = 30.7%)
> [[Details](regrJan06US.htm#PE "PE Ratio Regression")]
>
> PEG = 4.273 -0.417 Beta + 0.008 Payout - 0.830 ln(g) (R2 =
> 21.5%) [[Details](regrJan06US.htm#PEG "PE Ratio Regression")]
>
> Relative PE =1.381 Relative Growth + 1.065 Relative Payout-1.062
> Beta (R2= 67.8%) [[Details](regrJan06US.htm#RelPE "PE Ratio Regression")]
>
> PBV= 0.170 ROE - 0.841 Beta + 0.117 g +0.001 Payout (R2=
> 55.6%) [[Details](regrJan06US.htm#PBV "PBV Regression")]
>
> PS= 0.0839 g - 0.0069 Payout - 0.832 Beta + 0.218 Net Margin (R2=
> 58.4%) [[Details](regrJan06US.htm#PS "PS Ratio Regression")]

*Firm Value Multiples*

> Enterprise Value/Book Capital= 0.211 g (rev) + .102 (Return
> on Capital) - 0.003 (Debt/Equity) - 0.008 Reinvestment Rate (R2 =
> 57.3%) [[Details](regrJan06US.htm#EVCap "Value/Sales Ratios")]
>
> Enterprise Value/Sales = 0.177 g(rev) + 0.067 Pre-tax Operating
> Margin - 0.0065 Reinvestment Rate (R2 =
> 52.6%) [[Details](regrJan06US.htm#EVSales "Value/Sales Ratios")]
>
> Enterprise Value /EBITDA= 0.03 + 1.296 g(rev) - .051 (Tax rate)
> + 0.012 Return on Capital -0.0168 Reinvestment Rate (R2=50.9
> %) [[Details](regrJan06US.htm#EVEBITDA)]

*To see the more detailed output from the regression, click on 'Details'*.

### Europe

> PE = 29.628 - 0.204 Payout Ratio + 0.547 Beta + 0.237 g (R2 =
> 4.3%) [[Details](Euroregressions2006.htm#PE "Value/Sales Ratios")]
>
> PBV = 1.471 - .009 Payout Ratio +0.372 Beta + .113 ROE (R2 =
> 31.3%) [[Details](Euroregressions2006.htm#PBV "Value/Sales Ratios")]
>
> PS = 2.049 -0.010 Payout Ratio -0.478 Beta + .139 Net Margin (R2 = 30.3%) [[Details](Euroregressions2006.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital= 1.737 +0.138 Return on Capital - 0.002
> Reinvestment Rate - 0.016
> Debt/Capital (R2=52.2%)
> [[Details](Euroregressions2006.htm#EVCap)]
>
> EV/EBITDA = 22.96 + 0.407 (Debt/Capital) - 0.023 Reinvestment Rate-
> .419 Tax Rate (R2=25.4%) [[Details](Euroregressions2006.htm#EVEBITDA)]
>
> EV/Sales = 0.102 (Debt/Capital) -.007 Reinvestment Rate +0.189
> After-tax Operating Margin (R2=59.0%) [[Details](Euroregressions2006.htm#EVSales)]

### Emerging Markets

> PE = 5.579 + .0524 Payout Ratio -0.705 Beta + 0.816 g (R2 =
> 34.5%) [[Details](EmMkRegrJan06.htm#PE "Value/Sales Ratios")]
>
> PBV = 2.446 + .0101 Payout Ratio - 0.349 Beta + 0.124 ROE (R2 =
> 12.0%) [[Details](EmMkRegrJan06.htm#PBV "Value/Sales Ratios")]
>
> PS = 1.453+ .0122 Payout Ratio -0.514 Beta + .185 Net Margin + 0.0232 g
> (R2 =
> 36.8%) [[Details](EmMkRegrJan06.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital = 3.45 +.097 Return on Capital -.067 (Debt/Capital) ( R2 = 35.3%) [[Details](EmMkRegrJan06.htm#EVCap "Value/Sales Ratios")]
>
> EV/EBITDA = 32.534 - 0.441 (Debt/Capital) + 0.0264 Reinvestment Rate- .292
> Tax Rate (R2= 8.4%) [[Details](EmMkRegrJan06.htm#EVEBITDA)]
>
> EV/Sales = 1.613 - 0.059 (Debt/Capital) +.006 Reinvestment Rate +0.214
> After-tax Operating Margin (R2=42.5%) [[Details](EmMkRegrJan06.htm#EVSales)]

### Japan

> PE = 0.457 Payout Ratio + 12.839 Beta + 0.441 g (R2 =
> 46.9%) [[Details](JapanregrJan06.htm#PE "Value/Sales Ratios")]
>
> PBV = 0.983 Beta + .166 ROE +.0026 Payout Ratio (R2 =
> 36.1%) [[Details](JapanregrJan06.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.0014 Payout Ratio + 0.220 Beta + 0.291 Net Margin (R2 =
> 49.6%) [[Details](JapanregrJan06.htm#PS "Value/Sales Ratios")]
>
> EV/EBITDA = 17.60 + 0.320 (Debt/Capital) +0.311 Return on
> Capital - 0.250
> Tax Rate (R2=10.3 %) [[Details](JapanregrJan06.htm#EVEBITDA)]
>
> EV/Book Capital= 1.360 - 0.0208 (Debt/Capital)+ 0.0021 Reinvestment Rate
> + 0.179 Return on
> Capital (R2=
> 45.3%) [[Details](JapanregrJan06.htm#EVCap)]
>
> EV/Sales = 0.0397 (Debt/Capital)+ 0.349 After-tax
> Operating Margin + 0.0040 Reinvestment Rate (R2=
> 51.9%) [[Details](JapanregrJan06.htm#EVSales)]
