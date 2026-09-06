---
title: "PE Regression"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/JapanregrJan08.htm
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
@font-face
{font-family:Calibri;
panose-1:2 15 5 2 2 2 4 3 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:3 0 0 0 1 0;}
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
@list l1
{mso-list-id:1176113454;
mso-list-template-ids:1994058906;}
@list l1:level1
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
   

***PE Regression***

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .439a | .193 | .184 | 1.063308053220541E3 |
| a. Predictors: (Constant), Expected Earnings Growth - next 5 years (if available), Beta, Payout Ratio | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 13.554 | 2.759 |  | 4.913 | .000 |
| Beta | -1.250 | 1.600 | -.047 | -.781 | .435 |
| Payout Ratio | 26.051 | 4.873 | .329 | 5.346 | .000 |
| Expected Earnings Growth - next 5 years (if available) | 11.871 | 3.552 | .196 | 3.342 | .001 |
| a. Dependent Variable: PE | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*PBV Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .590a | .348 | .339 | 1.227668996158165E2 |
| a. Predictors: (Constant), ROE, Expected Earnings Growth - next 5 years (if available), Beta, Payout Ratio | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | .407 | .384 |  | 1.062 | .289 |
| Beta | -.503 | .189 | -.145 | -2.669 | .008 |
| Payout Ratio | .175 | .618 | .017 | .283 | .778 |
| Expected Earnings Growth - next 5 years (if available) | .430 | .416 | .056 | 1.032 | .303 |
| ROE | 19.260 | 1.750 | .623 | 11.007 | .000 |
| a. Dependent Variable: PBV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*PS Regression*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .612a | .375 | .366 | 1.242054942899337E2 |
| a. Predictors: (Constant), Net Margin, Expected Earnings Growth - next 5 years (if available), Beta, Payout Ratio | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | .850 | .328 |  | 2.592 | .010 |
| Beta | -.406 | .191 | -.114 | -2.129 | .034 |
| Payout Ratio | -.019 | .573 | -.002 | -.033 | .974 |
| Expected Earnings Growth - next 5 years (if available) | .406 | .418 | .051 | .972 | .332 |
| Net Margin | 13.513 | 1.068 | .635 | 12.653 | .000 |
| a. Dependent Variable: PS | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | .972 | .259 |  | 3.752 | .000 |
| Beta | -.264 | .186 | -.074 | -1.418 | .157 |
| Expected Earnings Growth - next 5 years (if available) | .173 | .413 | .022 | .420 | .675 |
| Net Margin | 10.300 | .968 | .553 | 10.643 | .000 |
| a. Dependent Variable: PS | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

 

*EV/EBITDA Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .383a | .147 | .146 | 4.996505204756562E2 |
| a. Predictors: (Constant), Tax Rate, Market Debt to Capital, ROIC | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 5.300 | .966 |  | 5.484 | .000 |
| ROIC | 16.383 | 1.648 | .199 | 9.943 | .000 |
| Market Debt to Capital | 20.980 | 1.043 | .401 | 20.118 | .000 |
| Tax Rate | -3.152 | 2.064 | -.029 | -1.527 | .127 |
| a. Dependent Variable: EV/EBITDA | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*EV/EBIT Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .360a | .130 | .129 | 7.196741679521015E2 |
| a. Predictors: (Constant), Tax Rate, Market Debt to Capital, ROIC | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 8.547 | 1.439 |  | 5.939 | .000 |
| ROIC | 6.003 | 2.383 | .052 | 2.519 | .012 |
| Market Debt to Capital | 27.938 | 1.508 | .376 | 18.524 | .000 |
| Tax Rate | 3.238 | 3.082 | .020 | 1.051 | .294 |
| a. Dependent Variable: EV/EBIT | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

*EV/Capital Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .731a | .534 | .534 | 4.123994513321550E1 |
| a. Predictors: (Constant), Market Debt to Capital, ROIC | | | | |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 1.250 | .039 |  | 31.840 | .000 |
| ROIC | 6.735 | .147 | .678 | 45.939 | .000 |
| Market Debt to Capital | -.665 | .087 | -.112 | -7.599 | .000 |
| a. Dependent Variable: Firm Value/BV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

 

 

 

*EV/Sales Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .608a | .369 | .369 | 1.04145655413581E2 |
| a. Predictors: (Constant), After-tax Margin, Market Debt to Capital | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | -.454 | .090 |  | -5.056 | .000 |
| Market Debt to Capital | 4.575 | .201 | .354 | 22.728 | .000 |
| After-tax Margin | 19.950 | .648 | .480 | 30.809 | .000 |
| a. Dependent Variable: EV/Sales | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

Without
intercept

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Squareb | Adjusted R Square | Std. Error of the Estimate |
| 1 | .769a | .592 | .591 | 1.04636093621556E2 |
| a. Predictors: Market Debt to Capital, After-tax Margin | | | | |
| b. For regression through the origin (the no-intercept model), R Square measures the proportion of the variability in the dependent variable about the origin explained by regression. This CANNOT be compared to R Square for models which include an intercept. | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b,c** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | After-tax Margin | 18.183 | .548 | .499 | 33.197 | .000 |
| Market Debt to Capital | 3.954 | .160 | .371 | 24.672 | .000 |
| a. Dependent Variable: EV/Sales | | |  |  |  |  |
| b. Linear Regression through the Origin | | |  |  |  |  |
| c. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |
