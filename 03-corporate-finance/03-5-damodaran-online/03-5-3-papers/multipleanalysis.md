---
title: "Multipleanalysis"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/webcasts/multipleanalysis/multipleanalysis.pdf
---

## RELATIVE VALUATION: DATA ANALYSIS

Aswath Damodaran

# Se1ng the table

Sector being assessed: Banks in the US

Multiple chosen: Price to Book Ratios

Variables that should matter:

### 1. Quality of growth

- 1. Return on equity
- 2. Payout Ratio

### 2. Expected growth

- 1. Historic growth
- 2. Expected growth in EPS

### 3. Risk measure

- 1. Beta
- 2. Standard Deviation
- 3. Tier 1 Capital Ratio
- 4. Non-performing loans

# The Data

The 
 raw 
 data 
 on 
 all 
 publicly 
 traded 
 banks 
 was 
 drawn 
 from 
 Capital 
 IQ, 
 with 
 the 
 following 
 screens: 

Only 
 banks 
 with 
 market 
 cap 
 > 
 \$1 
 billion 
 were 
 considered 

Only 
 US 
 banks 
 were 
 included 

Of 
 these 
 banks, 
 I 
 included 
 those 
 banks 
 where 
 I 
 could 
 get 
 Tier 
 1 
 Capital 
 and 
 Risk 
 Adjusted 
 Assets 

The 
 final 
 sample 
 contains 
 36 
 banks. 

# Step 1: DescripQve StaQsQcs

¨ Compute 
 the 
 standard 
 descripQve 
 staQsQcs 
 for 
 each 
 variable 
 in 
 the 
 data 
 base. 
 ¨ You 
 are 
 trying 
 to 
 get 
 a 
 sense 
 of 
 the 
 distribuQon, 
 not 
 just 
 the 
 high 
 and 
 the 
 low, 
 but 
 also 
 the 
 median 
 and 
 the 
 25th 
 and 
 75th 
 percenQles. 
 ¨ In 
 the 
 process, 
 you 
 are 
 also 
 looking 
 for 
 potenQal 
 trouble: 
 ¤ Abnormally 
 low 
 or 
 high 
 numbers 
 ¤ NegaQve 
 numbers 
 that 
 may 
 throw 
 off 
 your 
 assessment 

# Step 2: Correlations

| Correlations           |                     |             |       |            |                        |        |              |                      |                     |
|------------------------|---------------------|-------------|-------|------------|------------------------|--------|--------------|----------------------|---------------------|
|                        |                     | PricetoBook | ROE   | Tier1Ratio | Nonperforming loanspct | Beta   | Stddeviation | DividendPayout Ratio | ExpectedgrowthinEPS |
| PricetoBook            | Pearson Correlation | 1           | .374* | .170       | -.175                  | -.414* | -.371*       | .083                 | -.084               |
|                        | Sig. (2-tailed)     |             | .025  | .322       | .306                   | .012   | .026         | .630                 | .628                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| ROE                    | Pearson Correlation | .374*       | 1     | -.096      | -.212                  | -.112  | -.146        | .073                 | -.063               |
|                        | Sig. (2-tailed)     | .025        |       | .576       | .214                   | .515   | .396         | .674                 | .715                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| Tier1Ratio             | Pearson Correlation | .170        | -.096 | 1          | .289                   | -.047  | .043         | -.121                | .242                |
|                        | Sig. (2-tailed)     | .322        | .576  |            | .087                   | .785   | .801         | .481                 | .154                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| Nonperforming loanspct | Pearson Correlation | -.175       | -.212 | .289       | 1                      | .445** | .545**       | -.296                | -.114               |
|                        | Sig. (2-tailed)     | .306        | .214  | .087       |                        | .007   | .001         | .080                 | .509                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| Beta                   | Pearson Correlation | -.414*      | -.112 | -.047      | .445**                 | 1      | .944**       | -.339*               | .017                |
|                        | Sig. (2-tailed)     | .012        | .515  | .785       | .007                   |        | .000         | .043                 | .921                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| Stddeviation           | Pearson Correlation | -.371*      | -.146 | .043       | .545**                 | .944** | 1            | -.338*               | -.061               |
|                        | Sig. (2-tailed)     | .026        | .396  | .801       | .001                   | .000   |              | .044                 | .726                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| DividendPayoutRatio    | Pearson Correlation | .083        | .073  | -.121      | -.296                  | -.339* | -.338*       | 1                    | -.171               |
|                        | Sig. (2-tailed)     | .630        | .674  | .481       | .080                   | .043   | .044         |                      | .318                |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |
| ExpectedgrowthinEPS    | Pearson Correlation | -.084       | -.063 | .242       | -.114                  | .017   | -.061        | -.171                | 1                   |
|                        | Sig. (2-tailed)     | .628        | .715  | .154       | .509                   | .921   | .726         | .318                 |                     |
|                        | N                   | 36          | 36    | 36         | 36                     | 36     | 36           | 36                   | 36                  |

\*. Correlation is significant at the 0.05 level (2-tailed).

\*\*. Correlation is significant at the 0.01 level (2-tailed).

# Step 3: ScaWer plots

![](_page_5_Figure_1.jpeg)

## Step 4: Regressions: Start with the standard

| Coefficients <sup>a</sup> |                             |            |      |                           |        |      |
|---------------------------|-----------------------------|------------|------|---------------------------|--------|------|
| Model                     | Unstandardized Coefficients |            |      | Standardized Coefficients | t      | Sig. |
|                           | B                           | Std. Error | Beta |                           |        |      |
| 1                         | (Constant)                  | 2.196      | .506 |                           | 4.341  | .000 |
|                           | ROE                         | .038       | .018 | .328                      | 2.175  | .037 |
|                           | Beta                        | -.560      | .224 | -.377                     | -2.500 | .018 |
|                           | ExpectedgrowthinEPS         | -.014      | .038 | -.057                     | -.377  | .709 |

## Step 5: Take out the variables that are not staQsQcally significant

| Coefficients <sup>a</sup> |                             |            |                           |       |      |
|---------------------------|-----------------------------|------------|---------------------------|-------|------|
| Model                     | Unstandardized Coefficients |            | Standardized Coefficients | t     | Sig. |
|                           | B                           | Std. Error |                           |       |      |
| (Constant)                | 2.094                       | .421       |                           | 4.976 | .000 |
| 1                         | ROE                         | .039       | .017                      | 2.231 | .033 |
|                           | Beta                        | -.561      | .221                      | -.377 | .016 |

# Step 6: Tweak the regression

¨ Try 
 different 
 proxies 
 for 
 growth, 
 risk 
 and 
 quality 
 of 
 growth. 
 See 
 if 
 one 
 of 
 them 
 works. 
 ¨ If 
 you 
 have 
 outliers, 
 you 
 can 
 consider 
 removing 
 them 
 but 
 try 
 to 
 be 
 symmetric. 
 If 
 you 
 remove 
 a 
 really 
 high 
 number, 
 remove 
 one 
 that 
 is 
 really 
 low 
 as 
 well. 
 ¨ Don't 
 fight 
 the 
 data. 

# Step 7: The final regression

| <b>Coefficients<sup>a</sup></b> |                             |            |                           |       |        |      |
|---------------------------------|-----------------------------|------------|---------------------------|-------|--------|------|
| Model                           | Unstandardized Coefficients |            | Standardized Coefficients | t     | Sig.   |      |
|                                 | B                           | Std. Error |                           |       |        | Beta |
| 1                               | (Constant)                  | 1.377      | .703                      |       | 1.958  | .059 |
|                                 | ROE                         | .041       | .017                      | .351  | 2.369  | .024 |
|                                 | Beta                        | -.545      | .219                      | -.366 | -2.482 | .019 |
|                                 | Tier1Ratio                  | .051       | .040                      | .186  | 1.265  | .215 |

# Step 8: Check your predicted values

¨ Rank 
 the 
 companies 
 based 
 on 
 actual 
 values 
 for 
 the 
 mulQple. 
 ¨ Look 
 at 
 percent 
 under 
 or 
 over 
 value 
 for 
 each 
 company, 
 based 
 upon 
 predicted 
 value 
 from 
 regression. 
 ¨ See 
 if 
 you 
 get 
 a 
 bunching 
 together 
 of 
 under 
 valued 
 companies 
 near 
 the 
 top 
 of 
 the 
 list 
 and 
 over 
 valued 
 companies 
 near 
 the 
 boWom.