---
title: "PE Regression"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/EuroregrJan2008.htm
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
| 1 | .425a | .180 | .179 | 1.523233323064045E3 |
| a. Predictors: (Constant), Expected Earnings Growth (if available), Payout Ratio, Beta | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 14.148 | 1.301 |  | 10.872 | .000 |
| Beta | -2.620 | .868 | -.074 | -3.018 | .003 |
| Payout Ratio | 7.488 | .654 | .277 | 11.453 | .000 |
| Expected Earnings Growth (if available) | 29.061 | 2.272 | .311 | 12.789 | .000 |
| a. Dependent Variable: PE | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*PBV Regression*

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .623a | .388 | .386 | 2.266149512376126E2 |
| a. Predictors: (Constant), ROE, Expected Earnings Growth (if available), Payout Ratio, Beta | | | | |

 

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 1.475 | .225 |  | 6.547 | .000 |
| Beta | -.881 | .129 | -.144 | -6.803 | .000 |
| Payout Ratio | .051 | .103 | .010 | .491 | .624 |
| Expected Earnings Growth (if available) | 2.374 | .339 | .148 | 7.009 | .000 |
| ROE | 12.581 | .447 | .589 | 28.122 | .000 |
| a. Dependent Variable: PBV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*PS Regression*

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .574a | .330 | .328 | 1.897233704811547E2 |
| a. Predictors: (Constant), Net Margin, Beta, Payout Ratio, Expected Earnings Growth (if available) | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 1.085 | .173 |  | 6.262 | .000 |
| Beta | -.605 | .108 | -.124 | -5.596 | .000 |
| Payout Ratio | -.034 | .082 | -.009 | -.417 | .677 |
| Expected Earnings Growth (if available) | 1.676 | .284 | .130 | 5.913 | .000 |
| Net Margin | 12.343 | .496 | .544 | 24.872 | .000 |
| a. Dependent Variable: PS | |  |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*EV/EBITDA Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .563a | .317 | .315 | 1.725943743700766E3 |
| a. Predictors: (Constant), ROIC, Expected Earnings Growth (if available), Tax Rate, Market Debt to Capital | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 6.540 | 1.535 |  | 4.261 | .000 |
| Expected Earnings Growth (if available) | 2.913 | 1.287 | .047 | 2.264 | .024 |
| Tax Rate | -12.445 | 3.405 | -.077 | -3.655 | .000 |
| Market Debt to Capital | 43.753 | 2.020 | .561 | 21.658 | .000 |
| ROIC | 4.279 | 4.323 | .026 | .990 | .322 |
| a. Dependent Variable: EV/EBITDA | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

*EV/EBIT Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .588a | .346 | .344 | 2.049582855978426E3 |
| a. Predictors: (Constant), ROIC, Expected Earnings Growth (if available), Tax Rate, Market Debt to Capital | | | | |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 15.871 | 1.835 |  | 8.650 | .000 |
| Expected Earnings Growth (if available) | 5.561 | 1.532 | .074 | 3.631 | .000 |
| Tax Rate | -22.014 | 4.074 | -.112 | -5.404 | .000 |
| Market Debt to Capital | 48.663 | 2.407 | .518 | 20.216 | .000 |
| ROIC | -13.087 | 5.159 | -.065 | -2.537 | .011 |
| a. Dependent Variable: EV/EBIT | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

*EV/Capital Regression*

 

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .526a | .277 | .277 | 1.197075458641619E2 |
| a. Predictors: (Constant), Market Debt to Capital, ROIC | | | | |

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | 2.446 | .069 |  | 35.369 | .000 |
| ROIC | 4.702 | .249 | .304 | 18.880 | .000 |
| Market Debt to Capital | -2.290 | .124 | -.297 | -1.842E1 | .000 |
| a. Dependent Variable: Firm Value/BV | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |

 

 

 

 

 

*EV/Sales Regression*

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Model Summary** | | | | |
| Model | R | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1 | .506a | .256 | .256 | 2.243554444495063E2 |
| a. Predictors: (Constant), After-tax Margin, Market Debt to Capital | | | | |

 

 

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Coefficientsa,b** | | | | | | |
| Model | | Unstandardized Coefficients | | Standardized Coefficients | t | Sig. |
| B | Std. Error | Beta |
| 1 | (Constant) | .955 | .097 |  | 9.879 | .000 |
| Market Debt to Capital | 6.785 | .197 | .474 | 34.387 | .000 |
| After-tax Margin | 6.064 | .436 | .192 | 13.894 | .000 |
| a. Dependent Variable: EV/Sales | | |  |  |  |  |
| b. Weighted Least Squares Regression - Weighted by Market Cap (US $) | | | | |  |  |
