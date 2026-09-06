---
title: "Statisticsbasics"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/statisticsbasics.pdf
---

![](_page_0_Picture_2.jpeg)

Aswath 
 Damodaran 

# The role of sta7s7cs

**2**

¨ When 
 you 
 are 
 given 
 lots 
 of 
 data, 
 and 
 especially 
 when 
 that 
 data 
 is 
 contradictory 
 and 
 pulls 
 in 
 different 
 direc7ons, 
 sta7s7cs 
 help 
 you 
 make 
 sense 
 of 
 the 
 data 
 and 
 make 
 judgments. 

# Summarizing Data

¨ As 
 human 
 beings, 
 it 
 is 
 difficult 
 for 
 us 
 to 
 digest 
 vast 
 amounts 
 of 
 data. 
 Data 
 summaries 
 help 
 up 
 by 
 presen7ng 
 the 
 data 
 in 
 a 
 more 
 diges7ble 
 form. 
 ¨ One 
 way 
 to 
 summarize 
 data 
 is 
 visually, 
 i.e., 
 a 
 distribu7on 
 that 
 reveals 
 both 
 what 
 the 
 observa7ons 
 share 
 in 
 common 
 and 
 where 
 they 
 are 
 different. 
 ¨ The 
 other 
 is 
 with 
 descrip7ve 
 sta7s7cs: 
 average, 
 standard 
 devia7on 
 etc.. 

# A Dream Distribu7on: The Normal

*Figure A1.1: Normal Distribution*

**4**

Normal distributions and symmetric and can be

![](_page_3_Figure_4.jpeg)

# A more typical distribu7on: Skewed

![](_page_4_Figure_3.jpeg)

*Figure A1.2: Skewed Distributions*

# Summary Sta7s7cs: The most widely used!

**6**

For 
 a 
 data 
 series, 
 X1, 
 X2, 
 X3, 
 . 
 . 
 . 
 X*n*, 
 where 
 *n* 
 is 
 the 
 number 
 of 
 observa7ons 
 in 
 the 
 series, 
 the 
 most 
 widely 
 used 
 summary 
 sta7s7cs 
 are 
 as 
 follows: 

- 1. The mean ( $m$ ), which is the average of all of the observations in the data series.

- 1. The 
   variance, 
   which 
   is 
   a 
   measure 
   of 
   the 
   spread 
   in 
   the 
   distribu7on 
   around 
   the 
   mean 
   and 
   is 
   calculated 
   by 
   first 
   summing 
   up 
   the 
   squared 
   devia7ons 
   from 
   the 
   mean, 
   and 
   then 
   dividing 
   by 
   either 
   the 
   number 
   of 
   observa7ons 
   (if 
   it 
   the 
   popula7on) 
   or 
   one 
   less 
   than 
   that 
   number 
   (if 
   it 
   is 
   a 
   sample). 
   The 
   standard 
   devia7on 
   is 
   the 
   square 
   root 
   of 
   the 
   variance.

$$\text{Mean} = \mu_X = \frac{\sum_{j=1}^{j=n} X_j}{n}$$

$$\text{Variance} = \sigma_x^2 = \frac{\sum_{j=1}^{j=n} (X_j - \mu)^2}{n-1}$$

# More summary sta7s7cs

**7**

¨ The 
 median 
 of 
 a 
 distribu7on 
 is 
 its 
 exact 
 midpoint, 
 with 
 half 
 of 
 all 
 observa7ons 
 having 
 values 
 higher 
 than 
 that 
 number 
 and 
 half 
 lower. 
 In 
 a 
 perfectly 
 symmetric 
 distribu7on 
 (like 
 the 
 normal) 
 the 
 mean 
 = 
 median. 
 ¨ If 
 a 
 distribu7on 
 is 
 not 
 symmetric, 
 the 
 skewness 
 (third 
 moment) 
 measures 
 the 
 direc7on 
 (posi7ve 
 or 
 nega7ve) 
 and 
 degree 
 of 
 asymmetry. 
 ¨ The 
 kurtosis 
 (fourth 
 moment) 
 measures 
 the 
 likelihood 
 of 
 extreme 
 values 
 in 
 the 
 data. 
 A 
 high 
 kurtosis 
 indicates 
 that 
 there 
 are 
 more 
 observa7ons 
 that 
 deviate 
 a 
 lot 
 from 
 the 
 average. 

# Rela7onships between data: Covariance

**8**

¨ For 
 two 
 data 
 series, 
 X 
 (X1, 
 X2,) 
 and 
 Y(Y, 
 Y. 
 . 
 .), 
 the 
 covariance 
 provides 
 a 
 measure 
 of 
 the 
 degree 
 to 
 which 
 they 
 move 
 together 
 and 
 is 
 es7mated 
 by 
 taking 
 the 
 product 
 of 
 the 
 devia7ons 
 from 
 the 
 mean 
 for 
 each 
 variable 
 in 
 each 
 period. 

¨ The sign 
 on 
 the 
 covariance 
 indicates 
 the 
 type 
 of 
 rela7onship 
 the 
 two 
 variables 
 have. 
 A 
 posi7ve 
 sign 
 indicates 
 that 
 they 
 move 
 together 
 and 
 a 
 nega7ve 
 sign 
 that 
 they 
 move 
 in 
 opposite 
 direc7ons. 

$$\text{Covariance} = \sigma_{XY} = \frac{\sum_{j=1}^{j=n} (X_j - \mu_X) (Y_j - \mu_Y)}{n-1}$$

# From covariance to correla7on

**9**

¨ The 
 correla7on 
 is 
 the 
 standardized 
 measure 
 of 
 the 
 rela7onship 
 between 
 two 
 variables. 
 It 
 can 
 be 
 computed 
 from 
 the 
 covariance. 

¨ A 
 correla7on 
 close 
 to 
 zero 
 indicates 
 that 
 the 
 two 
 variables 
 are 
 unrelated. 

 ¨ A 
 posi7ve 
 correla7on 
 indicates 
 that 
 the 
 two 
 variables 
 move 
 together, 
 and 
 the 
 rela7onship 
 is 
 stronger 
 as 
 the 
 correla7on 
 gets 
 closer 
 to 
 one. 
 ¨ 
 A 
 nega7ve 
 correla7on 
 indicates 
 the 
 two 
 variables 
 move 
 in 
 opposite 
 direc7ons, 
 and 
 that 
 rela7onship 
 gets 
 stronger 
 the 
 as 
 the 
 correla7on 
 gets 
 closer 
 to 
 nega7ve 
 one 

$$\text{Correlation} = \rho_{XY} = \sigma_{XY} / \sigma_X \sigma_Y = \frac{\sum_{j=1}^{j=n} (X_j - \mu_X) (Y_j - \mu_Y)}{\sqrt{\sum_{j=1}^{j=n} (X_j - \mu_X)^2} \sqrt{\sum_{j=1}^{j=n} (Y_j - \mu_Y)^2}}$$

### Digging Deeper: ScaYer Plots and Regressions

![](_page_9_Figure_2.jpeg)

# Reading a regression

**11**

¨ In 
 a 
 regression, 
 we 
 aYempt 
 to 
 fit 
 a 
 straight 
 line 
 through 
 the 
 points 
 that 
 best 
 fits 
 the 
 data. 
 In 
 its 
 simplest 
 form, 
 this 
 is 
 accomplished 
 by 
 finding 
 a 
 line 
 that 
 minimizes 
 the 
 sum 
 of 
 the 
 squared 
 devia7ons 
 of 
 the 
 points 
 from 
 the 
 line. 

 ¨ When 
 such 
 a 
 line 
 is 
 fit, 
 two 
 parameters 
 emerge—one 
 is 
 the 
 point 
 at 
 which 
 the 
 line 
 cuts 
 through 
 the 
 *Y*-‐axis, 
 called 
 the 
 intercept 
 (a) 
 of 
 the 
 regression, 
 and 
 the 
 other 
 is 
 the 
 slope 
 (b) 
 of 
 the 
 regression 
 line: 

*Y* 
 = 
 *a* 
 + 
 *bX*

¨ The 
 slope 
 of 
 the 
 regression 
 measures 
 both 
 the 
 direc7on 
 and 
 the 
 magnitude 
 of 
 the 
 rela7onship 
 between 
 the 
 dependent 
 variable 
 (*Y*) 
 and 
 the 
 independent 
 variable 
 (*X*). 
 When 
 the 
 two 
 variables 
 are 
 posi7vely 
 correlated, 
 the 
 slope 
 will 
 also 
 be 
 posi7ve, 
 whereas 
 when 
 the 
 two 
 variables 
 are 
 nega7vely 
 correlated, 
 the 
 slope 
 will 
 be 
 nega7ve. 
 The 
 magnitude 
 of 
 the 
 slope 
 of 
 the 
 regression 
 can 
 be 
 read 
 as 
 follows: 
 For 
 every 
 unit 
 increase 
 in 
 the 
 dependent 
 variable 
 (*X*), 
 the 
 independent 
 variable 
 will 
 change 
 by 
 *b* 
 (slope). 

# How the intercept and slope are es7mated

**12**

¨ The 
 slope 
 of 
 the 
 regression 
 line 
 is 
 a 
 logical 
 extension 
 of 
 the 
 covariance 
 concept 
 introduced 
 in 
 the 
 last 
 sec7on. 
 In 
 fact, 
 the 
 slope 
 is 
 es7mated 
 using 
 the 
 covariance: 

¨ The 
 intercept 
 (*a*) 
 of 
 the 
 regression 
 can 
 be 
 read 
 in 
 a 
 number 
 of 
 ways. 
 One 
 interpreta7on 
 is 
 that 
 it 
 is 
 the 
 value 
 that 
 *Y* 
 will 
 have 
 when 
 *X* 
 is 
 zero. 
 Another 
 is 
 more 
 straigh\_orward 
 and 
 is 
 based 
 on 
 how 
 it 
 is 
 calculated. 
 It 
 is 
 the 
 difference 
 between 
 the 
 average 
 value 
 of 
 *Y*, 
 and 
 the 
 slope-‐adjusted 
 value 
 of 
 *X*. 

$$\text{Slope of the Regression } b = \frac{\text{Covariance}_{\text{YX}}}{\text{Variance of } X} = \frac{\sigma_{\text{YX}}}{\sigma_X^2}$$

Intercept of the Regression = a = 
$$\mu_v - b^*(\mu_x)$$

# Measuring the noise in a regression

**13**

¨ The 
 *R*2 
 of 
 the 
 regression 
 measures 
 the 
 propor7on 
 of 
 the 
 variability 
 in 
 the 
 dependent 
 variable 
 (*Y*) 
 that 
 is 
 explained 
 by 
 the 
 independent 
 variable 
 (*X*). 
 An 
 *R*2 
 value 
 close 
 to 
 one 
 indicates 
 a 
 strong 
 rela7onship 
 between 
 the 
 two 
 variables, 
 though 
 the 
 rela7onship 
 may 
 be 
 either 
 posi7ve 
 or 
 nega7ve. 

 ¨ Another 
 measure 
 of 
 noise 
 in 
 a 
 regression 
 is 
 the 
 standard 
 error, 
 which 
 measures 
 the 
 "spread" 
 around 
 each 
 of 
 the 
 two 
 parameters 
 es7mated—the 
 intercept 
 and 
 the 
 slope. 
 ¨ Dividing 
 the 
 coefficient 
 (intercept 
 or 
 slope) 
 by 
 the 
 standard 
 error 
 of 
 the 
 coefficient 
 yields 
 a 
 t 
 sta7s7c 
 which 
 can 
 be 
 used 
 to 
 judge 
 sta7s7cal 
 significance. 

# Using Regressions for predic7ons

**14**

¨ The 
 regression 
 equa7on 
 described 
 in 
 the 
 last 
 sec7on 
 can 
 be 
 used 
 to 
 es7mate 
 predicted 
 values 
 for 
 the 
 dependent 
 variable, 
 based 
 on 
 assumed 
 or 
 actual 
 values 
 for 
 the 
 independent 
 variable. 
 In 
 other 
 words, 
 for 
 any 
 given 
 *Y*, 
 we 
 can 
 es7mate 
 what 
 *X* 
 should 
 be: 

### $$X = a + b(Y)$$

¨ How 
 good 
 are 
 these 
 predic7ons? 
 That 
 will 
 depend 
 en7rely 
 on 
 the 
 strength 
 of 
 the 
 rela7onship 
 measured 
 in 
 the 
 regression. 
 When 
 the 
 independent 
 variable 
 explains 
 a 
 high 
 propor7on 
 of 
 the 
 varia7on 
 in 
 the 
 dependent 
 variable 
 (R2 
 is 
 high), 
 the 
 predic7ons 
 will 
 be 
 precise. 
 When 
 the 
 R2 
 is 
 low, 
 the 
 predic7ons 
 will 
 have 
 a 
 much 
 wider 
 range. 

# Simple to Mul7ple Regressions

**15**

¨ The 
 regression 
 that 
 measures 
 the 
 rela7onship 
 between 
 two 
 variables 
 becomes 
 a 
 mul7ple 
 regression 
 when 
 it 
 is 
 extended 
 to 
 include 
 more 
 than 
 one 
 independent 
 variables 
 (*X*1, 
 *X*2, 
 *X*3, 
 *X*4 
 . 
 . 
 .) 

$$Y = a + bX1 + cX2 + dX3 + eX4$$

¨ The 
 *R*2 
 s7ll 
 measures 
 the 
 strength 
 of 
 the 
 rela7onship, 
 but 
 an 
 addi7onal 
 *R*2 
 sta7s7c 
 called 
 the 
 adjusted 
 *R*2 
 is 
 computed 
 to 
 counter 
 the 
 bias 
 that 
 will 
 induce 
 the 
 *R*2 
 to 
 keep 
 increasing 
 as 
 more 
 independent 
 variables 
 are 
 added 
 to 
 the 
 regression. 
 If 
 there 
 are 
 k 
 independent 
 variables 
 in 
 the 
 regression, 
 the 
 adjusted 
 *R*2 
 is 
 computed 
 as 
 follows: 

$$\text{Adjusted R squared} = \frac{\left( \sum_{j=1}^{j=n} (Y_j - bX_j)^2 \right)}{n-k}$$

# Caveat Emptor on Regressions

- □ Both the simple and multiple regressions described in this section also assume linear relationships between the dependent and independent variables. If the relationship is not linear, we can either transform the data (either dependent on independent) to make the relationship more linear or run a non-linear regression.
- □ For the coefficients on the individual independent variables to make sense, the independent variable needs to be uncorrelated with each other, a condition that is often difficult to meet. When independent variables are correlated with each other, the statistical hazard that is created is called *multicollinearity*. In its presence, the coefficients on independent variables can take on unexpected signs (positive instead of negative, for instance) and unpredictable values.