---
title: "PE Regression"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/EmMkRegrJan08.htm
---

PE Regression  
<!--
/\* Font Definitions \*/
@font-face
{font-family:Arial;
panose-1:2 11 6 4 2 2 2 2 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
@font-face
{font-family:"Courier New";
panose-1:2 7 3 9 2 2 5 2 4 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
@font-face
{font-family:Wingdings;
panose-1:5 2 1 2 1 8 4 8 7 8;
mso-font-charset:2;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:0 0 65536 0 -2147483648 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
mso-bidi-font-size:10.0pt;
font-family:"Times New Roman";
mso-fareast-font-family:"Times New Roman";
mso-bidi-font-family:"Times New Roman";}
span.SpellE
{mso-style-name:"";
mso-spl-e:yes;}
span.GramE
{mso-style-name:"";
mso-gram-e:yes;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-paper-source:0;}
div.Section1
{page:Section1;}
/\* List Definitions \*/
@list l0
{mso-list-id:252518191;
mso-list-template-ids:614105440;}
@list l0:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
mso-ansi-font-size:10.0pt;
font-family:Symbol;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->
   

*PE Regression*

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .375a | .141 | .139 | 3.77189 |
| a. Predictors: (Constant), Expected Earnings Growth, Payout Ratio, Beta | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 5.630 | 3.625 |  | 1.553 | .121 |
| Beta | 11.354 | 2.205 | .115 | 5.149 | .000 |
| Payout Ratio | 2.707 | .485 | .122 | 5.584 | .000 |
| Expected Earnings Growth | 92.723 | 6.676 | .310 | 13.890 | .000 |
| a. Dependent Variable: PE | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

 

*PBV Regression*

*With intercept*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .540a | .291 | .290 | 4.09162 |
| a. Predictors: (Constant), ROE, Beta, Payout Ratio, Expected Earnings Growth | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | -3.081 | .449 |  | -6.866 | .000 |
| Beta | 2.608 | .239 | .221 | 10.894 | .000 |
| Payout Ratio | .219 | .053 | .083 | 4.153 | .000 |
| Expected Earnings Growth | 10.869 | .724 | .304 | 15.005 | .000 |
| ROE | 17.801 | 1.070 | .332 | 16.641 | .000 |
| a. Dependent Variable: PBV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

*Without intercept*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Squareb | Adjusted R Square | Std. Error of the Estimate |
| 1 | .849a | .721 | .721 | 4.1439330 |
| a. Predictors: ROE, Payout Ratio, Expected Earnings Growth, Beta | | | | |
| b. For regression through the origin (the no-intercept model), R Square measures the proportion of the variability in the dependent variable about the origin explained by regression. This CANNOT be compared to R Square for models which include an intercept. | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b,c** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | Beta | 1.362 | .158 | .245 | 8.614 | .000 |
| Payout Ratio | .205 | .053 | .049 | 3.831 | .000 |
| Expected Earnings Growth | 10.017 | .723 | .292 | 13.859 | .000 |
| ROE | 14.271 | .950 | .367 | 15.022 | .000 |
| a. Dependent Variable: PBV | | |  |  |  |  |
| b. Linear Regression through the Origin | | |  |  |  |  |
| c. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

 

*PS Regression*

*With intercept*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .536a | .288 | .286 | 4.0318556 |
| a. Predictors: (Constant), Net Margin, Beta, Payout Ratio, Expected Earnings Growth | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | -1.765 | .421 |  | -4.197 | .000 |
| Beta | 1.828 | .236 | .158 | 7.753 | .000 |
| Payout Ratio | .077 | .052 | .030 | 1.482 | .139 |
| Expected Earnings Growth | 8.688 | .715 | .248 | 12.145 | .000 |
| Net Margin | 17.275 | .766 | .452 | 22.564 | .000 |
| a. Dependent Variable: PS | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

*No intercept*

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Squareb | Adjusted R Square | Std. Error of the Estimate |
| 1 | .833a | .693 | .692 | 4.0504865 |
| a. Predictors: Net Margin, Payout Ratio, Expected Earnings Growth, Beta | | | | |
| b. For regression through the origin (the no-intercept model), R Square measures the proportion of the variability in the dependent variable about the origin explained by regression. This CANNOT be compared to R Square for models which include an intercept. | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b,c** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | Beta | 1.030 | .140 | .199 | 7.345 | .000 |
| Payout Ratio | .071 | .052 | .018 | 1.370 | .171 |
| Expected Earnings Growth | 8.037 | .702 | .252 | 11.456 | .000 |
| Net Margin | 16.028 | .709 | .465 | 22.611 | .000 |
| a. Dependent Variable: PS | |  |  |  |  |  |
| b. Linear Regression through the Origin | | |  |  |  |  |
| c. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

 

*EV/EBITDA Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .358a | .128 | .127 | 3.6836269 |
| a. Predictors: (Constant), Market Debt to Capital, Tax Rate, Expected Earnings Growth | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 41.850 | 2.639 |  | 15.857 | .000 |
| Expected Earnings Growth | 52.719 | 5.480 | .193 | 9.620 | .000 |
| Tax Rate | -46.649 | 8.582 | -.108 | -5.436 | .000 |
| Market Debt to Capital | -63.794 | 5.113 | -.251 | -1.248E1 | .000 |
| a. Dependent Variable: EV/EBITDA | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

*EV/EBIT Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .340a | .116 | .115 | 4.1268426 |
| a. Predictors: (Constant), Market Debt to Capital, Tax Rate, Expected Earnings Growth | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 47.926 | 2.967 |  | 16.155 | .000 |
| Expected Earnings Growth | 65.922 | 6.173 | .217 | 10.680 | .000 |
| Tax Rate | -48.565 | 9.661 | -.101 | -5.027 | .000 |
| Market Debt to Capital | -59.202 | 5.738 | -.210 | -1.032E1 | .000 |
| a. Dependent Variable: EV/EBIT | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

 

*EV/Capital Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .577a | .333 | .332 | 3.7949791 |
| a. Predictors: (Constant), ROIC, Expected Earnings Growth, Market Debt to Capital | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 5.262 | .215 |  | 24.471 | .000 |
| Expected Earnings Growth | 5.973 | .554 | .189 | 10.778 | .000 |
| Market Debt to Capital | -13.269 | .542 | -.442 | -2.450E1 | .000 |
| ROIC | 6.189 | .632 | .176 | 9.785 | .000 |
| a. Dependent Variable: Firm Value/BV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |

 

 

 

*EV/Sales Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .525a | .276 | .275 | 4.4046801 |
| a. Predictors: (Constant), After-tax Margin, Expected Earnings Growth, Market Debt to Capital | | | | |

 

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 4.412 | .269 |  | 16.374 | .000 |
| Expected Earnings Growth | 7.086 | .634 | .202 | 11.170 | .000 |
| Market Debt to Capital | -10.580 | .609 | -.315 | -1.737E1 | .000 |
| After-tax Margin | 16.103 | .878 | .330 | 18.348 | .000 |
| a. Dependent Variable: EV/Sales | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (in $) | | | | |  |  |
