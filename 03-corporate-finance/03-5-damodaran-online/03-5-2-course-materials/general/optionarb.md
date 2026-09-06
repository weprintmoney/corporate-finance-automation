---
title: "Options Arbitrage"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/invfables/optionarb.htm
---

Options Arbitrage

<!--
/\* Font Definitions \*/
@font-face
{font-family:"Times New Roman";
panose-1:0 2 2 6 3 5 4 5 2 3;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:"Courier New";
panose-1:0 2 7 3 9 2 2 5 2 4;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:Geneva;
panose-1:0 2 11 5 3 3 4 4 4 2;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:"New York";
panose-1:0 2 2 5 2 6 3 5 6 2;
mso-font-charset:0;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:50331648 0 0 0 1 0;}
@font-face
{font-family:Wingdings;
panose-1:0 5 2 1 2 1 8 4 8 7;
mso-font-charset:2;
mso-generic-font-family:auto;
mso-font-pitch:variable;
mso-font-signature:0 16 0 0 -2147483648 0;}
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h1
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:14.0pt;
font-family:Times;
mso-font-kerning:0pt;}
h2
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
font-size:12.0pt;
font-family:Times;}
h3
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:3;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
h4
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:4;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h5
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
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
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
p.MsoHeading7, li.MsoHeading7, div.MsoHeading7
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:7;
tab-stops:333.0pt 5.0in;
border:none;
mso-border-bottom-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:0in 0in 0in 0in;
font-size:14.0pt;
font-family:Times;}
p.MsoHeading8, li.MsoHeading8, div.MsoHeading8
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:8;
font-size:9.0pt;
font-family:Geneva;
font-style:italic;}
p.MsoHeading9, li.MsoHeading9, div.MsoHeading9
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:9;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
p.MsoToc1, li.MsoToc1, div.MsoToc1
{mso-style-update:auto;
mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc2, li.MsoToc2, div.MsoToc2
{mso-style-update:auto;
mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc3, li.MsoToc3, div.MsoToc3
{mso-style-update:auto;
mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:1.0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoToc6, li.MsoToc6, div.MsoToc6
{mso-style-update:auto;
mso-style-next:Normal;
margin-top:0in;
margin-right:.5in;
margin-bottom:0in;
margin-left:2.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:dotted 5.75in right blank 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;}
span.MsoEndnoteReference
{vertical-align:super;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:1.0pt 1.0pt 1.0pt 1.0pt;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5in;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText2, li.MsoBodyText2, div.MsoBodyText2
{margin-top:12.0pt;
margin-right:-.5in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
tab-stops:22.5pt 2.25in 3.75in 4.5in 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText3, li.MsoBodyText3, div.MsoBodyText3
{margin:0in;
margin-bottom:.0001pt;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"Times New Roman";}
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.25in;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent3, li.MsoBodyTextIndent3, div.MsoBodyTextIndent3
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5pt;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBlockText, li.MsoBlockText, div.MsoBlockText
{margin-top:0in;
margin-right:-.5in;
margin-bottom:0in;
margin-left:.25in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:22.5pt 2.25in 3.75in 4.5in 6.0in;
font-size:12.0pt;
font-family:Times;}
a:link, span.MsoHyperlink
{color:blue;
text-decoration:underline;
text-underline:single;}
a:visited, span.MsoHyperlinkFollowed
{color:purple;
text-decoration:underline;
text-underline:single;}
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
p.Times12, li.Times12, div.Times12
{mso-style-name:Times12;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"New York";}
p.InPractice, li.InPractice, div.InPractice
{mso-style-name:InPractice;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
border:none;
mso-border-alt:solid windowtext .5pt;
padding:0in;
mso-padding-alt:1.0pt 4.0pt 1.0pt 4.0pt;
font-size:12.0pt;
font-family:Times;
font-weight:bold;}
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
{mso-list-id:-2;
mso-list-type:simple;
mso-list-template-ids:-1;}
@list l0:level1
{mso-level-start-at:0;
mso-level-text:\*;
mso-level-tab-stop:none;
mso-level-number-position:left;
margin-left:0in;
text-indent:0in;}
@list l1
{mso-list-id:1;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l1:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l2
{mso-list-id:2;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l2:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l3
{mso-list-id:3;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l3:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l4
{mso-list-id:4;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l4:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l5
{mso-list-id:5;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l5:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l6
{mso-list-id:6;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l6:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l7
{mso-list-id:7;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l7:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l8
{mso-list-id:8;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l8:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l9
{mso-list-id:9;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l9:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l10
{mso-list-id:12;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l10:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l11
{mso-list-id:13;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l11:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l12
{mso-list-id:14;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l12:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l13
{mso-list-id:15;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l13:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l14
{mso-list-id:150369075;
mso-list-type:hybrid;
mso-list-template-ids:1626753814 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l14:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l15
{mso-list-id:1047801579;
mso-list-type:hybrid;
mso-list-template-ids:-1433489054 -172084822 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l15:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l16
{mso-list-id:1080099983;
mso-list-type:hybrid;
mso-list-template-ids:912830810 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l16:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l17
{mso-list-id:1951620269;
mso-list-type:hybrid;
mso-list-template-ids:852243592 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l17:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l18
{mso-list-id:2020540840;
mso-list-type:hybrid;
mso-list-template-ids:1973324560 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l18:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l19
{mso-list-id:2027708386;
mso-list-type:hybrid;
mso-list-template-ids:1010888190 984073 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l19:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l0:level1 lfo1
{mso-level-start-at:1;
mso-level-number-format:bullet;
mso-level-numbering:continue;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l1:level1 lfo15
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
@list l10:level1 lfo16
{mso-level-number-format:arabic;
mso-level-numbering:continue;
mso-level-text:"%1\.";
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->

## Options Arbitrage

            As
derivative securities, options differ from futures in a very important respect.
They represent rights rather than obligations � calls gives you the right to
buy and puts gives you the right to sell. Consequently, a key feature of
options is that the losses on an option position are limited to what you paid
for the option, if you are a buyer. Since there is usually an underlying asset
that is traded, you can, as with futures, construct positions that essentially
are riskfree by combining options with the underlying asset.

### Exercise Arbitrage

            The
easiest arbitrage opportunities in the option market exist when options violate
simple pricing bounds. No option, for instance, should sell for less than its
exercise value. With a call option: Value of call > Value of Underlying
Asset � Strike Price

With a put option: Value of put > Strike Price � Value of
Underlying Asset

For instance, a call option with a strike price of $ 30 on a
stock that is currently trading at $ 40 should never sell for less than $ 10.
It it did, you could make an immediate profit by buying the call for less than
$ 10 and exercising right away to make $ 10.

In fact, you can tighten these
bounds for call options, if you are willing to create a portfolio of the underlying
asset and the option and hold it through the option�s expiration.  The bounds then become:

With a call option: Value of call > Value of Underlying
Asset � Present value of Strike Price

With a put option: Value of put > Present value of Strike
Price � Value of Underlying Asset

Too see why, consider the call option in the previous
example. Assume that you have one year to expiration and that the riskless
interest rate is 10%.

Present value of Strike Price = $ 30/1.10 = $27.27

Lower Bound on call value = $ 40 - $27.27 = $12.73

The call has to trade for more than $12.73. What would
happen if it traded for less, say $ 12? You would buy the call for $ 12, sell
short a share of stock for $ 40 and invest the net proceeds of $ 28 ($40 � 12)
at the riskless rate of 10%. Consider what happens a year from now:

If the stock price > 30: You first collect the proceeds
from the riskless investment ($28(1.10) =$30.80), exercise the option (buy the
share at $ 30) and cover your short sale. You will then get to keep the
difference of $0.80.

If the stock price < 30: You collect the proceeds from
the riskless investment ($30.80), but a share in the open market for the
prevailing price then (which is less than $30) and keep the difference.

In other words, you invest nothing today and are guaranteed
a positive payoff in the future. You could construct a similar example with
puts.

            The
arbitrage bounds work best for non-dividend paying stocks and for options that can
be exercised only at expiration (European options). Most options in the real
world can be exercised only at expiration (American options) and are on stocks
that pay dividends. Even with these options, though, you should not see short
term options trading violating these bounds by large margins, partly because
exercise is so rare even with listed American options and dividends tend to be
small. As options become long term and dividends become larger and more
uncertain, you may very well find options that violate these pricing bounds,
but you may not be able to profit off them.

### Replicating Portfolio

One of the key insights that
Fischer Black and Myron Scholes had about options in the 1970s that revolutionized
option pricing was that a portfolio composed of the underlying asset and the
riskless asset could be constructed to have exactly the same cash flows as a
call or put option. This portfolio is called the replicating portfolio. In
fact, Black and Scholes used the arbitrage argument to derive their option
pricing model by noting that since the replicating portfolio and the traded
option had the same cash flows, they would have to sell at the same price.

            To
understand how replication works, let us consider a very simple model for stock
prices where prices can jump to one of two points in each time period. This
model, which is called a binomial model, allows us to model the replicating
portfolio fairly easily. In the figure below, we have the binomial distribution
of a stock, currently trading at $ 50 for the next two time periods. Note that
in two time periods, this stock can be trading for as much as $ 100 or as
little as $ 25. Assume that the objective is to value a call with a strike
price of 50, which is expected to expire in two time periods:

if !supportEmptyParas endif

|  |
| --- |
| if !vmlendif |

Now assume that the interest rate is
11%. In addition, define

            *�* = Number of shares in the replicating portfolio

            B
= Dollars of borrowing in replicating portfolio

The objective is to combine *�* shares of stock and *B*
dollars of borrowing to replicate the cash flows from the call with a strike
price of 50. Since we know the cashflows on the option with certainty at
expiration, it is best to start with the last period and work back through the
binomial tree.

*Step 1:* Start with the end nodes and work backwards. Note
that the call option expires at t=2, and the gross payoff on the option will be
the difference between the stock price and the exercise price, if the stock
price > exercise price, and zero, if the stock price < exercise price.

if !supportEmptyParas endif

if !vml![](optionarb_files/image006.gif)endif

The objective is to construct a portfolio of D shares of
stock and B in borrowing at t=1,  when the stock price is $ 70, that will have the same
cashflows at t=2 as the call option with a strike price of 50.  Consider what the portfolio will
generate in cash flows under each of the two stock price scenarios, after you
pay back the borrowing with interest (11% per period) and set the cash flows
equal to the cash flows you would have received on the call.

If stock price = $ 100:             Portfolio
Value = 100 D � 1.11 B = 50

If stock price = $ 50:               Portfolio
Value =   50 D � 1.11 B =   0

Drawing on skills that most of us have not used since high
school, we can solve for both the number of shares of stock you will need to
buy (1) and the amount you will need to borrow ($ 45) at t=1.  Thus, if the stock price is $70 at t=1,
borrowing $45 and buying one share of the stock will give the same cash flows
as buying the call. To prevent arbitrage, the value of the call at t=1, if the
stock price is $70, has to be equal to the cost (to you as an investor) of
setting up the replicating position:

            Value
of Call = Cost of Replicating Position = if !vml![](optionarb_files/image009.gif)endif

Considering the other leg of the binomial tree at t=1,

if !vml![](optionarb_files/image012.gif)endif

If the stock price is 35 at t=1, then the call is worth
nothing.

*Step 2:* Now that we know how much the call will be worth at
t=1 ($25 if the stock price goes to $ 70 and $0 if it goes down to $ 35), we
can move backwards to the earlier time period and create a replicating
portfolio that will provide the values that the option will provide.

if !supportEmptyParas endif

if !vml![](optionarb_files/image015.gif)endif

In other words, borrowing $22.5 and buying 5/7 of a share wtoday
ill provide the same cash flows as a call with a strike price of $50. The value
of the call therefore has to be the same as the cost of creating this position.

Value of Call = Cost of replicating position = if !vml![](optionarb_files/image018.gif)endif

Consider for the moment the possibilities for arbitrage if
the call traded at less than $13.21, say $ 13.00. You would buy the call for
$13.00 and sell the replicating portfolio for $13.21 and claim the difference
of $0.21. Since the cashflows on the two positions are identical, you would be
exposed to no risk and make a certain profit. If the call trade for more than
$13.21, say $13.50, you would buy the replicating portfolio, sell the call and
claim the $0.29 difference. Again, you would not have been exposed to any risk.

            You
could construct a similar example using puts. The replicating portfolio in that
case would be created by selling short on the underlying stock and lending the
money at the riskless rate. Again, if puts are priced at a value different from
the replicating portfolio, you could capture the difference and be exposed to
no risk.

            What
are the assumptions that underlie this arbitrage? The first is that both the
traded asset and the option are traded and that you can trade simultaneously in
both markets, thus locking in your profits. The second is that there are no (or
at least very low transactions costs). If transactions costs are large, prices
will have to move outside the band created by these costs for arbitrage to be
feasible. The third is that you can borrow at the riskless rate and sell short,
if necessary. If you cannot, arbitrage may no longer be feasible.

### Arbitrage across options

            When
you have multiple options listed on the same asset, you may be able to take
advantage of relative mispricing � how one option is priced relative to another
- and lock in riskless profits.  We
will look first at the pricing of calls relative to puts and then consider how
options with different exercise prices and maturities should be priced,
relative to each other.

#### Put-Call Parity

            When
you have a put and a call option with the same exercise price and the same
maturity, you can create a riskless position by selling the call, buying the
put and buying the underlying asset at the same time. To see why, consider
selling a call and buying a put with exercise price K and expiration date t,
and simultaneously buying the underlying asset at the current price S. The
payoff from this position is riskless and always yields K at expiration t. To
see this, assume that the stock price at expiration is S\*. The payoff on each
of the positions in the portfolio can be written as follows:

|  |  |  |
| --- | --- | --- |
| Position | Payoffs at t if S\*>K | Payoffs at t if S\*<K |
| Sell call | -(S\*-K) | 0 |
| Buy put | 0 | K-S\* |
| Buy stock | S\* | S\* |
| *Total* | *K* | *K* |

Since this position yields K with
certainty, the cost of creating this position must be equal to the present
value of K at the riskless rate (K e-rt).

            S+P-C
= K e-rt

            C
- P = S - K e-rt

This relationship between
put and call prices is called put call parity. If it is violated, you have
arbitrage.

If C-P > S � Ke-rt,
you would sell the call, buy the put and buy the stock. You would earn more
than the riskless rate on a riskless investment.

If C-P < S � Ke-rt,
you would buy the call, sell the put and sell short the stock. You would then invest
the proceeds at the riskless rate and end up with a riskless profit at
maturity.

Note that put call parity
creates arbitrage only for options that can be exercised only at maturity
(European options) and may not hold if options can be exercise early (American
options).

            Does
put-call parity hold up in practice or are there arbitrage opportunities? One
study examined option pricing data
from the Chicago Board of Options from 1977 to 1978 and found potential
arbitrage opportunities in a few cases. However, the arbitrage opportunities were
small and persisted only for short periods. Furthermore, the options examined
were American options, where arbitrage may not be feasible even if put-call
parity is violated.  A more recent
study by Kamara and Miller of options on the S&P 500 (which are European
options) between 1986 and 1989 finds fewer violations of put-call parity.

#### Mispricing across Strike Prices and Maturities

            A
spread is a combination of two or more options of the same type (call or put)
on the same underlying asset. You can combine two options with the same
maturity but different exercise prices (bull and bear spreads), two options with
the same strike price but different maturities (calendar spreads), two options
with different exercise prices and maturities (diagonal spreads) and more than
two options (butterfly spreads). You may be able to use spreads to take
advantage of relative mispricing of options on the same underlying stock. 

*Strike Prices*: A call with a lower strike price should never sell
for less than a call with a higher strike price, assuming that they both have
the same maturity. If it did, you could buy the lower strike price call and
sell the higher strike price call, and lock in a riskless profit. Similarly, a
put with a lower strike price should never sell for more than a put with a higher
strike price and the same maturity. If it did, you could buy the higher strike
price put, sell the lower strike price put and make an arbitrage profit.

*Maturity*: A call (put) with a shorter time to expiration
should never sell for more than a call (put) with the same strike price with a
long time to expiration. If it did, you would buy the call (put) with the
shorter maturity and sell (put) the call with the longer maturity (i.e, create
a calendar spread) and lock in a profit today. When the first call expires, you
will either exercise the second call (and have no cashflows) or sell it (and
make a further profit).

Even a casual perusal of the option prices listed in the
newspaper each day should make it clear that it is very unlikely that pricing
violations that are this egregious will exist in a market as liquid as the
Chicago Board of Options.

if !supportEmptyParas endif
