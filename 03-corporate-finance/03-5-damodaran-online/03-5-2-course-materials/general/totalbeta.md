---
title: "Estimating the cost of equity for a private company"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/totalbeta.htm
---

Estimating the cost of equity for a private company

<!--
/\* Font Definitions \*/
@font-face
{font-family:"Times New Roman";
panose-1:0 2 2 6 3 5 4 5 2 3;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h4
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
mso-outline-level:4;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h5
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
line-height:24.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:5;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h6
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
{margin:0in;
margin-bottom:.0001pt;
text-align:center;
mso-pagination:widow-orphan;
font-size:14.0pt;
font-family:Times;
font-weight:bold;}
p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5in;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent3, li.MsoBodyTextIndent3, div.MsoBodyTextIndent3
{margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:none;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:Times;
color:black;}
p.FigureCaption, li.FigureCaption, div.FigureCaption
{mso-style-name:FigureCaption;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:"Times New Roman";
font-weight:bold;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-paper-source:0;}
div.Section1
{page:Section1;}
-->

Estimating the cost of equity for a private company

            In
assessing the cost of equity for publicly traded firms, we looked at the risk
of investments through the eyes of the marginal investors in these firms. With
the added assumption that these investors were well diversified, we were able
to define risk in terms of risk added on to a diversified portfolio or market
risk. The beta (in the CAPM) and betas (in the multi-factor models) that
measure this risk are usually estimated using historical stock prices. The
absence of historical price information for private firm equity and the failure
on the part of many private firm owners to diversify can create serious
problems with estimating and using betas for these firms.

#### Approaches to Estimating Market Betas

            The
standard process of estimating the beta in the capital asset pricing model
involves running a regression of stock returns against market returns.
Multi-factor models use other statistical techniques, but they also require
historical price information. In the absence of such information, as is the
case with private firms, there are three ways in which we can estimate betas.

##### 1. Accounting Betas

While price information is not available
for private firms, accounting earnings information is. We could regress changes
in a private firm�s accounting earnings against changes in earnings for an
equity index (such as the S&P 500) to estimate an accounting beta.

D
EarningsPrivate firm = a + b D EarningsS&P 500

The slope of the regression (b) is the
accounting beta for the firm. Using operating earnings would yield an unlevered
beta, whereas using net income would yield a levered or equity beta.

There are two significant limitations with this approach.
The first is that private firms usually measure earnings only once a year,
leading to regressions with few observations and limited statistical power. The
second is that earnings are often smoothed out and subject to accounting
judgments, leading to mismeasurement of accounting betas.

if !supportEmptyParas endif

##### 2. Fundamental Betas

There have been attempts made by
researchers to relate the betas of publicly traded firms to observable
variables such as earnings growth, debt ratios and variance in earnings.
Beaver, Kettler, and Scholes (1970) examined the relationship between betas and
seven variables - dividend payout, asset growth, leverage, liquidity, asset
size, earnings variability and the accounting beta. Rosenberg and Guy (1976)
also attempted a similar analysis. The following is a regression that we ran
relating the betas of NYSE and AMEX stocks in 1996 to four variables:
coefficient of variation in operating income (CVOI), book
debt/equity (D/E), historical growth in earnings (g) and the book value of
total assets (TA).

Beta = 0.6507   + 0.25 CVOI   +
0.09 D/E + 0.54 g   - 0.000009 TA         R2=18%

where

CVOI    = Coefficient of Variation in Operating Income

= Standard
Deviation in Operating Income/ Average Operating Income

We could measure each of these variables
for a private firm and use these to estimate the beta for the firm. While this
approach is simple, it is only as good as the underlying regression. The low R2
suggests that the beta estimates that emerge from it are likely to have large
standard errors.

##### 3. Bottom-up Betas

When valuing publicly traded firms, we
used the unlevered betas of the businesses that the firms operated in to
estimate bottom-up betas � the costs of equity were based upon these betas. We
did so because of the low standard errors on these estimates (due to the
averaging across large numbers of firms) and the forward looking nature of the
estimates (because the business mix used to weight betas can be changed). We
can estimate bottom-up betas for private firms and these betas have the same
advantages that they do for publicly traded firms. Thus, the beta for a private
steel firm can be estimated by looking at the average betas for publicly traded
steel companies. Any differences in financial or even operating leverage can be
adjusted for in the final estimate.

In making the adjustment of unlevered
betas for financial leverage, we do run into a problem with private firms,
since the debt to equity ratio that should be used is a market value ratio.
While many analysts use the book value debt to equity ratio to substitute for
the market ratio for private firms, we would suggest one of the following
alternatives.

a. Assume that the private firm�s market leverage will
resemble the average for the industry. If this is the case, the levered beta
for the private firm can be written as:

b private firm = bunlevered (1 + (1 - tax rate) (Industry Average
Debt/Equity))

b. Use the private firm�s
target debt to equity ratio (if management is willing to specify such a target)
or its optimal debt ratio (if one can be estimated) to estimate the beta.

b private firm = bunlevered (1 + (1 - tax rate) (Optimal Debt/Equity))

The adjustment for operating leverage is
simpler and is based upon the proportion of the private firm�s costs that are
fixed. If this proportion is greater than is typical in the industry, the beta
used for the private firm should be higher than the average for the industry.

#### Adjusting for Non-Diversification

            Betas
measure the risk added by an investment to a diversified portfolio.
Consequently, they are best suited for firms where the marginal investor is
diversified. With private firms, the owner is often the only investor and thus
can be viewed as the marginal investor. Furthermore, in most private firms, the
owner tends to have much of his or her wealth invested in the private business
and does not have an opportunity to diversify. Consequently, it can be argued
that betas will understate the exposure to market risk in these firms.

            At
the limit, if the owner has all of his or her wealth invested in the private
business and is completely undiversified, that owner is exposed to all risk in
the firm and it is not just the market risk (which is what the beta measures).
There is a fairly simple adjustment that can allow us to bring in this
non-diversifiable risk into the beta computation. To arrive at this adjustment,
assume that the standard deviation in the private firm�s equity value (which
measures total risk) is sj and that the standard
deviation in the market index is sm. If the correlation between
the stock and the index is defined to be rjm, the market beta can be
written as:

Market beta if !vml![](totalbeta_files/image003.gif)endif

To
measure exposure to total risk (sj), we could divide the market
beta by rjm. This would yield the following.

if !vml![](totalbeta_files/image006.gif)endif

This
is a relative standard deviation measure, where the standard deviation of the
private firm�s equity value is scaled against the market index�s standard
deviation to yield what we will call a total beta.

Total Beta if !vml![](totalbeta_files/image009.gif)endif

The
total beta will be higher than the market beta and will depend upon the
correlation between the firm and the market � the lower the correlation, the
higher the total beta.

            You
might wonder how a total beta can be estimated for a private firm, where the
absence of market prices seems to rule out the calculation of either a market
beta or a correlation coefficient. Note though, that we were able to estimate
the market beta of the sector by looking at publicly traded firms in the
business. We can obtain the correlation coefficient by looking at the same
sample and use it to estimate a total beta for a private firm.

            The
question of whether the total beta adjustment should be made cannot be answered
without examining why the valuation of the private firm is being done in the
first place. If the private firm is being valued for sale, whether and how much
the market beta should be adjusted will depend upon the potential buyer or
buyers. If the valuation is for an initial public offering, there should be no
adjustment for non-diversification, since the potential buyers are stock market
investors. If the valuation is for sale to another individual or private
business, the extent of the adjustment will depend upon the degree to which the
buyer�s portfolio is diversified; the more diversified the buyer, the higher
the correlation with the market and the smaller the total beta adjustment.

if !supportEmptyParas endif

if !supportEmptyParas endif

**if !supportEmptyParas endif**
