---
title: "Regressions of Multiples"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/MReg97.html
---

Regressions of Multiples     **January 2005**  

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
* g(rev) = Expected growth rate in revenues over the next 5 years (If you
  do not have this, use the expected growth rate in EPS)
* PE = Price/ Current EPS
* PBV = Market value of equity/ Book value of equity
* PS = Market value of equity / Revenues in most recent financial year
* Enterprise Value = Market Value of Equity + Market Value of Debt - Cash
  and Marketable Securities
* Payout = DPS/EPS: from most recent year; if dividends are postive and
  earnings are negative, it is set to 100%.
* Debt/Capital = Book Value of Debt/ (Book value of Debt + Market value
  of equity)
* Beta = Betas based upon 3 years of data (You can use alternate periods
  or intervals)
* Net Margin = Net Income / Sales
* After-tax Operating Margin = EBIT (1-tax rate) /Sales
* Tax Rate = Effective tax rate in most recent year
* ROE = Net Income / BV of Equity
* ROC + EBIT (1-t)/ (BV of Debt + BV of Equity)
* Reinvestment Rate = (Cap ex - Depreciation + Chg in non-cash WC)/ EBIT
  (1 - tax rate)
* Std dev in Stock Prices = Standard deviation in stock prices over last
  5 years. You can use alternate intervals.

### United States

*Equity Multiples*
> PE = 14.781 + 0.914 g - 0.0489 Payout + 0.220 Beta (R2 = 23.6%)
> [[Details](regrJan05US.htm#PERegression "PE Ratio Regression")]
>
> PEG = 8.530 + 0.730 Beta -0.0008 Payout - 2.727 ln(g) (R2 =
> 31.0%) [[Details](regrJan05US.htm#PEGRegression "PE Ratio Regression")]
>
> Relative PE = 0.392 + 0.522 Relative Growth +0.0151
> Beta (R2= 25.2%) [[Details](regrJan05US.htm#RelativePEregression "PE Ratio Regression")]
>
> PBV= 0.202 ROE - 0.297 Beta + 0.0984 g - 0.0135 Payout (R2=
> 51.5%) [[Details](regrJan05US.htm#PBVRegressionn "PBV Regression")]
>
> PS= 0.0516 g - 0.0069 Payout - 0.0705 Beta + 0.219 Net Margin (R2=
> 61.3%) [[Details](regrJan05US.htm#PSRegression "PS Ratio Regression")]

*Firm Value Multiples*

> Enterprise Value/Book Capital= 1.851 + .149 g (rev) + .0406 (Return
> on Capital) - 0.0413 (Debt/Capital) - 0.0026 Reinvestment Rate(R2 =
> 49.9%) [[Details](regrJan05US.htm#EVBookRegression "Value/Sales Ratios")]
>
> Enterprise Value/Sales = 0.182 g(rev) + 0.0861 After-tax Operating
> Margin -.0256 (Debt/Capital) - 0.0013 Reinvestment Rate (R2 =
> 48.3%) [[Details](regrJan05US.htm#EVSalesNoIntRegression "Value/Sales Ratios")]
>
> Enterprise Value /EBITDA= 8.554 + 1.016 g(rev) - .150 (Tax rate)
> -.0664 (Debt/Capital) -0.0188 Reinvestment Rate (R2=38.0 %)
> [[Details](regrJan05US.htm#EVEBITDARegression)]

*To see the more detailed output from the regression, click on 'Details'*.

### Europe

> PE = 13.325+ .239 Payout Ratio -1.470 Beta + 0.271 g (R2 =
> 6.7%) [[Details](Euroregrjan2005.htm#PE "Value/Sales Ratios")]
>
> PBV = 2.149 + .0015 Payout Ratio -0.464 Beta + .111 ROE (R2 =
> 24.5%) [[Details](Euroregrjan2005.htm#PBV "Value/Sales Ratios")]
>
> PS = 0.418 + .0064 Payout Ratio -0.176 Beta + .184 Net Margin
> (R2 = 38.8%) [[Details](Euroregrjan2005.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital= 1.179 +0.0897 Return on Capital + 0.0071 g - 0.00004
> Reinvestment Rate (R2=40.9%)
> [[Details](Euroregrjan2005.htm#Vbook)]
>
> EV/EBITDA = 16.80 + 0.518 (Debt/Capital) +0.0006 Reinvestment Rate-
> .356 Tax Rate (R2=30.3%) [[Details](Euroregrjan2005.htm#Vebitda)]
>
> EV/Sales = 0.163 + 0.0376 (Debt/Capital) -.00002 Reinvestment Rate +0.202
> After-tax Operating Margin (R2=45.6%) [[Details](Euroregrjan2005.htm#VSales)]

### Emerging Markets

> PE = 7.189 + .0676 Payout Ratio + 3.057 Beta + 0.460 g (R2 =
> 20.2%) [[Details](EmMkRegrJan05.htm#PE "Value/Sales Ratios")]
>
> PBV = 1.337 + 0.0228 g + .0005 Payout Ratio - 0.839Beta + 0.109 ROE (R2 =
> 27.2%) [[Details](EmMkRegrJan05.htm#PBV "Value/Sales Ratios")]
>
> PS =0.053 + .0007 Payout Ratio -0.307 Beta + .155 Net Margin + 0.0232 g
> (R2 =
> 50.6%) [[Details](EmMkRegrJan05.htm#PS "Value/Sales Ratios")]
>
> EV/Book Capital = 2.38 +.05 Return on Capital -.034 (Debt/Capital) +.0009
> Reinvestment Rate ( R2 = 23.7%) [[Details](EmMkRegrJan05.htm#VBook "Value/Sales Ratios")]
>
> EV/EBITDA = 15.619 - 0.135 (Debt/Capital) + 0.0116 Reinvestment Rate- .114
> Tax Rate + 0.178 g (R2= 7.2%) [[Details](EmMkRegrJan05.htm#Vebitda)]
>
> EV/Sales = -0.0345 - 0.0105 (Debt/Capital) +.0003 Reinvestment Rate +0.198
> After-tax Operating Margin + 0.0316 g (R2=41.2%) [[Details](EmMkRegrJan05.htm#Vsales)]

### Japan

> PE = -8.110 + .528 Payout Ratio + 14.605 Beta + 0.799 g (R2 =
> 32.5%) [[Details](JapanregrJan05.htm#PE "Value/Sales Ratios")]
>
> PBV = -0.06 - 0.649 Beta + .217 ROE +.0009 Payout Ratio + 0.0478 g (R2 =
> 54.9%) [[Details](JapanregrJan05.htm#PBV "Value/Sales Ratios")]
>
> PS = -0.760 + 0.0045 Payout Ratio - 0.670 Beta + .325 Net Margin + 0.0456
> g (R2 =
> 60.0%) [[Details](JapanregrJan05.htm#PS "Value/Sales Ratios")]
>
> EV/EBITDA = 24.24 + 0.072 (Debt/Capital) +.0108 Reinvestment Rate- 0.397
> Tax Rate (R2=9.8 %) [[Details](JapanregrJan05.htm#Vebitda)]
>
> EV/Book Capital= -0.246 + 0.0073 (Debt/Capital)+ 0.157 Return on
> Capital + 0.0003 Reinvestment Rate + 0.9272 g (R2=
> 66.3%) [[Details](JapanregrJan05.htm#Vbook)]
>
> EV/Sales = -3.557 + 0.0545 (Debt/Capital)+ 0.508 After-tax
> Operating Margin + 0.0019 Reinvestment Rate + 0.0346 g (R2=
> 69.8%) [[Details](JapanregrJan05.htm#Vsales)]
