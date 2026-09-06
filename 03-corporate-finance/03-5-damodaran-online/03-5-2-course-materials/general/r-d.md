---
title: "Estimating Equity Risk Premiums"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/R&D.htm
---

Estimating Equity Risk Premiums

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
/\* Style Definitions \*/
p.MsoNormal, li.MsoNormal, div.MsoNormal
{mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h1
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:12.0pt;
font-family:Times;
mso-font-kerning:0pt;}
h2
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
h3
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:3;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h4
{mso-style-next:Normal;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:27.0pt;
margin-bottom:.0001pt;
text-align:justify;
text-indent:-27.0pt;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:4;
tab-stops:99.0pt 171.0pt 256.5pt;
font-size:12.0pt;
font-family:Times;
color:black;
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
page-break-after:avoid;
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
span.MsoFootnoteReference
{vertical-align:super;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
{margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:200%;
mso-pagination:widow-orphan;
font-size:14.0pt;
font-family:Times;
font-weight:bold;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
font-size:14.0pt;
font-family:Times;}
p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.25in;
line-height:200%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText2, li.MsoBodyText2, div.MsoBodyText2
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText3, li.MsoBodyText3, div.MsoBodyText3
{margin:0in;
margin-bottom:.0001pt;
line-height:200%;
mso-pagination:widow-orphan;
tab-stops:2.75in 269.0pt;
font-size:12.0pt;
font-family:Times;
color:black;}
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:27.0pt;
margin-bottom:.0001pt;
text-align:justify;
text-indent:-27.0pt;
line-height:200%;
mso-pagination:widow-orphan;
tab-stops:1.0in 2.0in 225.0pt;
font-size:12.0pt;
font-family:Times;
color:black;}
p.Times12, li.Times12, div.Times12
{mso-style-name:Times12;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"New York";}
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
mso-list-template-ids:0;}
@list l1:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l2
{mso-list-id:2;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l2:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l3
{mso-list-id:3;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l3:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l4
{mso-list-id:4;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l4:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l5
{mso-list-id:5;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l5:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l6
{mso-list-id:6;
mso-list-template-ids:0;}
@list l6:level1
{mso-level-start-at:61;
mso-level-text:%1;
mso-level-tab-stop:34.0pt;
mso-level-number-position:left;
margin-left:34.0pt;
text-indent:-34.0pt;}
@list l6:level2
{mso-level-start-at:36;
mso-level-text:"%1\.%2";
mso-level-tab-stop:34.0pt;
mso-level-number-position:left;
margin-left:34.0pt;
text-indent:-34.0pt;}
@list l6:level3
{mso-level-text:"%1\.%2\.%3";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
margin-left:.5in;
text-indent:-.5in;}
@list l6:level4
{mso-level-text:"%1\.%2\.%3\.%4";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
margin-left:.5in;
text-indent:-.5in;}
@list l6:level5
{mso-level-text:"%1\.%2\.%3\.%4\.%5";
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.75in;}
@list l6:level6
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6";
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.75in;}
@list l6:level7
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7";
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-1.0in;}
@list l6:level8
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7\.%8";
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-1.0in;}
@list l6:level9
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7\.%8\.%9";
mso-level-tab-stop:1.25in;
mso-level-number-position:left;
margin-left:1.25in;
text-indent:-1.25in;}
@list l7
{mso-list-id:7;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l7:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l8
{mso-list-id:8;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l8:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l0:level1 lfo25
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
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->

if !supportEmptyParas endif

if !supportEmptyParas endif

if !supportEmptyParas endif

Research and Development Expenses:

Implications for Profitability Measurement and Valuation

            The
operating income for a firm is estimated by netting out all operating expenses
from revenues. When valuing a firm, we usually begin with after-tax operating
income and then reduce it by the reinvestment needs of the firm. The
reinvestment needs cover any investments that the firm needs to make to
generate future growth, and include both capital expenditures and working
capital investments. The distinction between operating and capital expenditures
is critical for tax calculations, and is important in determining both the
amount of capital on a firm's books and how its profitability is measured.

In this paper, we will consider the
accounting treatment of research and development expenses as operating
expenses, and argue that it is not appropriate to do so, at least for valuation
purposes.  Considering research and
development expenses as capital expenses will have profound effects on
estimates of cash flow and growth in valuation, and in determining earnings
multiples for purposes of relative valuation.

# Operating and Capital Expenditures

Accounting statements classify all
expenses into three categories - operating expenses, financing expenses and
capital expenses. Operating expenses are expenses that, at least in theory,
provide benefits only for the current period; the cost of labor and materials
expended to create products which are sold in the current period would be a
good example. Financing expenses are expenses arising from the non-equity
financing used to raise capital for the business; the most common example is
interest expenses. Capital expenses are expenses that are expected to generate
benefits over multiple periods; for instance, the cost of buying land and
buildings is treated as a capital expense. Operating expenses are subtracted
from revenues in the current period to arrive at a measure of operating
earnings from the firm. Financing expenses are subtracted from operating
earnings to estimate earnings to equity investors or net income. Capital
expenses are written off over their useful life (in terms of generating
benefits) as depreciation or amortization.

The distinction between operating
and financing expenses may not be significant for tax purposes, since both are
tax deductible, but the distinction between operating and capital expenses
affects taxes. Operating expenses are deductible in the period in which they
are made, whereas capital expenses are written off over the useful life of the
investment. The distinction also matters for purposes of asset and capital
measurement. Operating expenses create no assets and affect capital only
indirectly through retained earnings. Capital expenses, on the other hand,
create assets and consequently affect capital as well.

# The Accounting Treatment of Research and Development Expenses

            Capital
expenditures are defined as those expenditures that are likely to create
benefits over multiple periods. By this definition, investments in land, plant
and long term equipment are capital investments, but so is research and
development. In fact, a reasonable argument can be made that research and
development expenses (R&D) are more long term than investments in physical
plant and equipment at many firms, especially those in the pharmaceutical and
high technology sectors. Thus, it follows that R&D expenses should be treated
as capital expenditures. In reality, however, accounting standards in the
United States require the treatment of R&D as operating expenses. In this
section, we will examine the consequences of this rule for earnings and capital
measurement at firms with substantial research expenses.

## Accounting Rules Governing R&D Expenses

            Prior
to 1975, companies in the United States were allowed to capitalize R&D
expenses. Accounting rule SFAS 2, which has governed the treatment of research
and development expenses since 1975, requires that all R&D expenses be
expensed in the period incurred. The only exception is for contract R&D
done for unrelated entities.

            The
rationale for treating forcing firms to expense R&D seems to lie in the
belief that the benefits are uncertain, and occur only when the research leads
to a commercial product. Consequently, it is argued that the asset created by
research is not one that can be used by the firm to borrow money. This, to us,
sounds like a dangerous path to follow. Using this reasoning, there are a
number of capital investments, especially those in riskier businesses, which
would qualify for expensing, simply because they have no liquidation value and
have uncertain cash flows.

            Outside
the United States, IAS 9 also requires the expensing of research cost but
allows for the capitalization of development expenses. Development costs are
defined to include all costs involved in turning research into commercial
products or services. In the UK and Canada, firms are permitted, but not
required, to capitalize development costs as the research gets closer to
commercial exploitation. In general, though, most companies in most countries
expense research and development expenses.

## Consequences for Earnings Measurement

            The
treatment of R&D as an operating expense has the immediate effect of
lowering both operating and net income. The tax deductibility of these expenses
buffers the impact somewhat, and the net income and after-tax operating income
are both reduced by the following:

After-tax Effect of
R&D expense on earnings = R&D Expenses (1 - marginal tax rate)

For companies that end up with negative earnings as a
consequence of research expenses, the after-tax effect will be even larger
because the tax benefit has to be deferred until future periods.

            The
treatment of research expenditures as operating expenses also implies that
research expenditures create no assets. Thus, patents that emerge from internal
research will not be shown as assets on the balance sheet. In contrast, patents
acquired from third parties can be treated as assets. This contradiction in the
treatment of patents has given rise to game playing on the part of firms with
substantial research expenditures

## R&D Partnerships

            In
an R&D partnership, a group of investors creates a partnership, which
agrees to cover the entire research and development expense for a firm. In
return, the partnership gets the rights to any products developed by the
partnership. In most cases, however, the firm preserves the right to purchase
the partnership or license the product some time in the future. From the
perspective of the firm, this arrangement essentially means that R&D
expenses are eliminated, because the revenues from the partnership cover the
expenses entirely. For partners in the partnership, there is the potential at
least of a large payoff if the research pays off in the form of commercial
products.

            This
arrangement can clearly be misused by firms that want to move research expenses
off the books, and borrow funds to finance this research. SFAS 68 requires that
there be an actual transfer of risk from the firm to the partnership. In other
words, the firm should not be under any obligation to return cash received from
the partnership, if the research does not pay off.

# A Financial Analysis of Research and Development Expenses

            Research
and development expenses are designed to generate future growth and should be
treated as capital expenditures. In this section, we will consider how to
reclassify research expenses and the consequences for reported earnings,
capital and profitability.

## A Reclassification of R&D Expenses

The first step in the
reclassification of R&D expenses is to remove it from operating expenses
and show it as a capital expenditure. The steps that follow are not as simple.
First, the reclassified R&D expense becomes a capital expense and is no
longer expensed. Second, capital expenses create assets, and R&D is not an
exception. The after-tax R&D expense has to be cumulated over time to
create an asset that we can loosely call the research asset.  Third, like other assets, the research
asset can lose value over time and hence may have to be amortized over its
life.  The amortization that is
generated is not tax deductible, but it will affect operating income.

The movement of R&D from the
operating expense to the capital expenditure column can have profound
implications for profitability measures and for projections of cash flows into
the future.

## The Effect on Assets and Capital

            When
we treat R&D expenses as capital expenditures, we have to maintain
consistency and treat cumulated R&D expenses as an asset. The simplest way
to do this is to cumulate the after-tax research and development expenses[if !supportFootnotes[1]endif](#_ftn1)
over time and create a research asset. This asset will then be amortized over
time, with both the length of the amortization period and the amortization
schedule being determined by the nature of the research expenses, and the
estimated time until there is a payoff to the investment. Thus, for
pharmaceutical companies where FDA approval can take as long as a decade, the
research asset will be amortized over an extended period. In contrast, for high
technology firms where the payoff is much sooner, the research asset will have
to be amortized over a shorter period.

            If
the research is on clearly identified products, there is a more direct approach
to amortization. Research expenses should be completely written off when one of
two scenarios occur. One is if the product is found not to be viable, and is
abandoned. The research expense on that product should then be written off. The
other is if the firm decides to invest in producing the product commercially,
in which case the research expense on the asset has to be written off and
replaced with the physical assets created by the investment.

            The
capital and assets of a firm will increase when R&D expenses are capitalized,
but the extent of the change will depend upon how long the company has been in
existence and its cumulated R&D over that period. Thus, firms which have
been in existence for a long period and have invested substantially in R&D
over that period will see a much bigger change in their capital than firms that
have been around for short period. The amortization schedule can also make a
difference, since the cumulated research asset gets reduced by the amortization
each year. Thus, the research asset for a firm that amortizes its research over
five years, can be estimated by cumulating R&D expenses over the last five
years[if !supportFootnotes[2]endif](#_ftn2)
and reducing this cumulated amount by the amortization on these expenses.

            Is
there a way to estimate the market value of the research asset? The value of
the patents generated by the research can be estimated using real option
models, but basic research will be difficult to value.  

###### Illustration 1: Effect on Capital and Equity of Reclassifying R& D Expenses: Boeing

            To
value the research asset for Boeing, we first need to make an assumption about
the amortizable life of the research asset. In the case of Boeing, the products
are new and improved airplanes that have long commercial lives. Consequently,
we use a ten-year life for Boeing�s research asset, and assume that any
research expenses are amortized uniformally in the ten years after the expense
is incurred.  The following table
values the research asset at Boeing, based upon the R&D expenses at Boeing
over the last 10 years (including the current year):

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | *Year* | *R&D* | *Unamortized Portion* | | *Unamortized Value* | |
|  | 1988 | $751 | 0.10 | | $75 | |
|  | 1989 | $754 | 0.20 | | $151 | |
|  | 1990 | $827 | 0.30 | | $248 | |
|  | 1991 | $1,417 | 0.40 | | $567 | |
|  | 1992 | $1,846 | 0.50 | | $923 | |
|  | 1993 | $1,661 | 0.60 | | $997 | |
|  | 1994 | $1,704 | 0.70 | | $1,193 | |
|  | 1995 | $1,300 | 0.80 | | $1,040 | |
|  | 1996 | $1,633 | 0.90 | | $1,470 | |
|  | 1997 | $1,924 | 1.00 | | $1,924 | |
| Capitalized Value of R& D Expenses = | | | | $8,587 | |  |
if !supportMisalignedColumns|  |  |  |  |  |  |  |
endif

Note that with the assumption of
straight line amortization, only 1/10th of the research expense in
1988 remains amortized, 2/10th of the expense in 1989 and so on The
value of the research asset at Boeing is a substantial $8.587 billion.

            This
research asset augments the assets , equity and capital of the firm. Thus, the
adjusted book value of aasets, equity and capital at Boeing can be estimated as
follows:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | Equity | Capital |
| Book Value | $14,353 | $22,319 |
| + Research Asset | $8,587 | $8,587 |
| = Adjusted Book Value | $21,540 | $30,907 |

Firms with significant research
expenditures will have much higher values for assets, capital and equity once
research expenditures are capitalized.

## The Effect on Operating and Net Income

            Will
treating research and development expenses as capital expenditures increase or
decrease operating income? The effect depends upon the trend in research
expenditures and amortization of previous research expenses. To illustrate, the
following table lays out operating income, with the conventional treatment of
R&D expenses, and operating income, with R&D treated as a capital expenditure:

|  |  |
| --- | --- |
| Conventional Treatment of R&D | R&D as Capital Expenditures |
| Revenues  - Operating Expenses  - R&D  = Operating Income  - Taxes  = Operating Income after taxes | Revenues  - Operating Expenses  - Amortization of Research Asset  = Operating Income  - Taxes (based on conventional treatment)  = Operating Income after taxes |

Whether operating income increases or decreases when R&D
is reclassified will depend upon whether the amortization of the research asset
is greater than or less than the R&D expense in the current year. For high
growth firms, where R&D expenses tend to grow substantially over time, the
reclassification will lead to an increase in operating income. As these firms
mature, and R&D expenses level off, the operating income may well decrease.

###### Illustration 2: Effect of R&D Reclassification on Operating and Net Income

            In
the following analysis, we will examine the effects of reclassifying R&D
expenses as capital expenditures on operating income and net income at Boeing.

|  |  |
| --- | --- |
| Operating Income | $1,078 |
| + Research and Development Expenses | $1,924 |
| - Amortization of Research Asset | $1,272 |
| = Adjusted Operating Income | $1,731 |

We also compute the effect on after-tax operating income
of capitalizing  R&D  expenses as capital expenditures.

|  |  |
| --- | --- |
| Operating Income (1-t) | $701 |
| + Research and Development Expenses | $1,924 |
| - Amortization of Research Asset | $1,272 |
| = Adjusted After-tax  Operating Income | $1,353 |

Note that this estimate of the after-tax operating
income is different from that obtained by multiplying the adjusted operating
income by (1- tax rate). This reflects the tax benefit earned by the firm
because the revenue code allows the entire R&D expense to be deducted for
tax purposes, unlike its treatment of other capital  expenditures. The magnitude of the tax benefit to the firm
from expensing R&D, as opposed to capitalizing it, can be computed as
follows:

Adjusted After-tax Operating Income        =                     $
1,353 million

Adjusted Operating Income (1- tax rate)   =                     $
1,125 million

Tax Benefit                                                =                     $
   208 million

            Finally,
we look at the effect on net income of reclassifying research and development
expenses as capital expenditures.                

|  |  |
| --- | --- |
| Net Income | $721 |
| + R & D expenses | $1,924 |
| - Amortization of Research Asset | $1,272 |
| = Adjusted Net Income | $1,384 |

Again, the adjusted net income
reflects the tax benefit created by the tax treatment of research and
development expenditures.

## The Effects on Profitability

            The
reclassification of R&D from an operating to a capital expense has a
significant impact on both the earnings and the capital estimates for a firm.
Thus, the return on equity and capital for  a firm will change when the reclassification is made. Will
the return on equity and capital increase or decrease when R&D is recategorized?
The return on capital after the recategorization of R&D will look as
follows:

if !vml![](R%26D_files/image003.gif)endif

The effect of reclassifying R&D expenses will depend
upon two factors:

if !supportLists-       endifThe
magnitude of the R&D expense is in the current year relative to R&D
expenses in prior years: When the current R&D expense is significantly
higher than expenses in previous years the returns on equity and capital will
increase on the recategorization. (The increase in operating income in
proportional terms will be greater than the increase in capital invested). When
the current R&D expense is similar to or smaller than R&D expenses in
previous years, the returns on equity and capital will drop when R&D
expenses are recategorized.

if !supportLists-       endifThe
level of the unadjusted return on capital:  Firms with high unadjusted returns on capital are much more
likely to see drops in the return when research and development is classified
as a capital expenditure. This is because the net research expense (After-tax
R&D expense - R&D amortization) as a percent of the research asset is
likely to be lower than the unadjusted return on capital and thus pull the
return down.

            The
effects on return on equity are similar, though the effects will be magnified
because the proportional impact on net income and book value of equity of
reclassifying R&D expenses is likely to be larger.

###### Illustration 3: Effects of R&D Reclassification on Profitability Measures

            To
compute the effects of reclassifying research and development expenses on
profitability measures, we first compute the return on capital using both
adjusted and unadjusted measures of operating income and capital:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Boeing* | *Boeing (Adjusted)* |
| After-tax Operating Income | $701 | $1,353 |
| BV of Capital - Beginning | $21,547 | $30,039 |
| BV of Capital - Ending | $20,363 | $30,907 |
| BV of Capital - Average | $20,955 | $30,473 |
| ROC (based on average) | 3.34% | 4.44% |
| ROC (based on beginning) | 3.25% | 4.51% |

Note that the both beginning and
ending capital are increased by the assessed value of the research asset. The
net effect of reclassifying R&D expenses is an increase in the return on
capital.

            The
effect on return on equity can also be similarly assessed. To do so, we compute
the adjusted net income and book value of equity:

|  |  |  |
| --- | --- | --- |
| ***Return Ratios*** | ***Boeing*** | ***Boeing (Adjusted)*** |
| Net Income | $732 | $1,384 |
| BV of Equity- Beginning | $13,502 | $21,437 |
| BV of Equity- Ending | $12,953 | $22,940 |
| BV of Equity - Average | $13,228 | $22,188 |
| ROE (based on average) | 5.53% | 6.24% |
| ROE (based on beginning) | 5.42% | 6.46% |

Note again that the return on equity increases when net
income and book value of equity are adjusted to reflect the recapitalization of
R&D expenses.

## The Effect on Cash Flows

            Reclassifying
R&D expenses as capital expenses does not affect current cash flows since
it has no tax effect. The following table clearly indicates this:

|  |  |
| --- | --- |
| *Cash Flow with Conventional Treatment of R&D* | *Cash Flow with R&D treated as a Capital Expenditure* |
| EBIT(1-t)  + Depreciation  if !supportLists-       endifCap Ex  if !supportLists-       endifChange in Working Capital  = Free Cash Flow to Firm | EBIT (1-t)  *+ R& D Expense*  if !supportLists-       endif*R & D Amortization*  = Adjusted After-tax Operating Income  *+ R & D Amortization*  + Depreciation  if !supportLists-       endifCap Ex  if !supportLists-       endif*R & D Expense*  if !supportLists-       endifChange in Working Capital  = Free Cash Flow to Firm |

Note that the taxes are still based upon the unadjusted
operating income, and that reclassifying R&D for analysis purposes does not
affect tax calculations. Working through the expanded calculation, we arrive at
the same free cash flow to the firm. The same analysis applies when we look at
free cash flow to equity.

            If
there is no effect on the free cash flows, why bother with the reclassification
in the first place? By separating out R&D expenses from other operating
expenses, we get a cleaner picture of what a firm is actually earning on its
assets in place, and how much it is investing for future growth. This becomes
critical when we project these cash flows into the future.

## The Effects on Expected Growth

            The
real effects of recategorizing R&D show up when we compute the expected
growth in operating income and cash flows. Note that the growth in operating
income can be written in terms of the reinvestment rate and the return on
capital earned on investments.

GrowthEBIT = Reinvestment Rate \* Return on
Capital

Where,

Reinvestment Rate = (Cap Ex - Depreciation + Change in
Working Capital)/ EBIT (1-t)

Return on Capital = EBIT (1-t) / Capital Invested

Firms whose primary capital
expenditures are research and development expenses often have anemic
reinvestment rates, when R&D is classified as an operating expense and thus
look like they should have really low expected growth rates. The return on
capital is also misestimated for the same reasons.

            When
R&D is reclassified as a capital expenditure, the reinvestment rate and
return on capital will be affected:

if !vml![](R%26D_files/image006.gif)endif

if !vml![](R%26D_files/image009.gif)endif

The growth in operating income will then reflect these
changes. Generally, rapidly growing firms that increase research expenditures
proportionately will have much higher reinvestment rates and lower return on
capital after the adjustment. This will then result in higher growth in
operating income.

            The
reclassification of research expenses also allows us to discriminate between
growth firms that are investing in research and growth firms that are not. When
R&D expenses are treated as operating expenses, the latter will look much
better on all measures of profitability from operating margins to returns on
capital. Treating R&D expenses as capital expenditures allows us to bring
both groups of firms to an equal footing in terms of profitability measures,
while giving firms that are investing in research the benefits of higher growth
and potentially higher value.

###### Illustration 4: Effects on Reinvestment Rate and Expected Growth

            In
the following table, we compute the reinvestment rate, return on capital and
expected growth rate for Boeing using unadjusted numbers and estimates adjusted
to reflect the capitalization of research expenses:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Unadjusted* | *With R&D capitalized* |
| Net Cap Ex | $37 | $689 |
| EBIT(1-t) | $701 | $1,353 |
| Reinvestment Rate | 5.28% | 50.94% |
| Return on Capital | 3.25% | 4.51% |
| Expected Growth | 0.17% | 2.29% |

Note that the reinvestment rate increases dramatically when
we count the research expenses as capital expenditures. This reflects the fact
the research expenses at Boeing have been increasing over time.

## The Effect on Discounted Cash Flow Value

            While
reclassifying R&D expenses as capital expenditures might have no effect on
current cash flows, it has profound effects on valuation for the following
reasons:

if !supportLists-       endifThe
estimates of expected growth can be tied much more closely to whether and how
much a firm is investing for that growth (in R&D) and how effective it is
in converting the R&D into profits (through the return on capital). Thus,
it forces analysts to consider not just the magnitude of research expenditures
but the quality of these investments as well.

if !supportLists-       endifIn
valuation we often assume that operating margins and returns on capital at
firms converge on industry averages as we move through time. If these industry
averages are computed using the conventional definition of R&D as an
operating expense, there is no reason to assume that firms will move towards
these averages. If, on the other hand, the industry averages are computed with
R&D reclassified as a capital expenditure, it can be argued that
competitive pressures will push margins towards convergence.

if !supportLists-       endifWhen
computing terminal value, it is critical that assumptions about growth be
consistent with assumptions about reinvestment rates and returns on capital.
This is impossible to do as long as R&D expenses are treated as operating
expenses. When they are reclassified as capital expenditures, the reinvestment
rate can be computed and it will include research and development expenses.

###### Illustration 5: Effects of R& D Reclassification on Value

            In
the following illustration, we value Boeing twice, once with the conventional
treatment of R&D as an expense and once with R&D expenses capitalized. We
first present the valuation of Boeing, using the reported after-tax operating income.
We begin by applying the fundamental growth rate (from the reinvestment rate
and return on capital estimated in illustration 4) to revenues. Since 1997 was
a year in which Boeing reported significantly lower operating income than in
prior year, we projected that the after-tax operating margin would recover to
the average level that Boeing enjoyed between 1992 and 1996. The improvement to
the �target� margin of 4.12% is assumed to occur linearly from the current
level over the next 3 years. After year 3, we assume that the company is in
stable growth.

            For
the other components, we assume that capital expenditures and depreciation grow
at the same rate as revenues, and that non-cash working capital remains 5% of
revenues over the entire period.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| if !supportEmptyParas endif | Base | 1 | 2 | 3 | Terminal Year |
| Revenues | $45,800 | $45,879 | $45,957 | $46,036 | $46,115 |
| Operating Margin | 1.53% | 2.39% | 3.26% | 4.12% | 4.12% |
| EBIT(1-t) | $701 | $1,098 | $1,497 | $1,898 | $1,901 |
| + Deprec�n & Amort. | 1354 | $        1,356 | $        1,359 | $        1,361 | $        1,363 |
| - Capital Exp | -1391 | $      (1,393) | $      (1,396) | $      (1,398) | $      (1,401) |
| - Change in WC | if !supportEmptyParas endif | $               4 | $               4 | $               4 | $               4 |
| FCFF | if !supportEmptyParas endif | $1,057 | $1,456 | $1,856 | $1,860 |
| Terminal Value | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif | $      20,529 | if !supportEmptyParas endif |
| Present Value | if !supportEmptyParas endif | $           968 | $        1,221 | $      17,177 | if !supportEmptyParas endif |
| Value of Firm = | if !supportEmptyParas endif | $      19,365 | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Growth Rate in Revenues = | | 0.17% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Target after-tax Operating Margin = | | 4.12% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Working Capital as % of Revenues = | | 5% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Cost of Capital = | if !supportEmptyParas endif | 9.23% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |

The growth rate used is computed
based upon the reinvestment rate and return on capital computed in illustration
4.

            We
also valued Boeing, with R&D expenses re-categorized as capital expenses.
This affects every aspect of the valuation:

if !supportLists-       endifThe
operating income used is the adjusted operating income estimated in
illustration 2, with R&D expenses capitalized and amortized.

if !supportLists-       endifThe
target after-tax operating margin in stable growth is the pre-R&D margin
estimated for Boeing to be 5.55%, instead of 4.12%.

if !supportLists-       endifThe
depreciation is augmented by the amortization of R&D expenses over time. We
assume that both the R&D expenses and the amortization increase at the
revenue growth rate over this period.

if !supportLists-       endifThe
capital expenditures include the estimated R&D expenses over time

The following table summarizes the valuation of Boeing with
these inputs:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| if !supportEmptyParas endif | Base | 1 | 2 | 3 | Terminal Year |
| Revenues | $45,800.00 | $ 46,850.98 | $ 47,926.08 | $ 49,025.85 | $ 50,150.85 |
| Operating Margin | 2.95% | 3.82% | 4.68% | 5.55% | 5.55% |
| EBIT(1-t) | $1,353 | $   1,788.99 | $   2,244.02 | $   2,718.99 | $   2,781.38 |
| + Deprec'n & Amort | $2,626 | $        2,686 | $        2,748 | $        2,811 | $        2,875 |
| - Capital Exp | ($3,315) | $      (3,391) | $      (3,469) | $      (3,548) | $      (3,630) |
| - Change in WC | if !supportEmptyParas endif | $             53 | $             54 | $             55 | $             56 |
| FCFF | if !supportEmptyParas endif | $        1,031 | $        1,469 | $        1,926 | $        1,970 |
| Terminal Value | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif | $      28,410 | if !supportEmptyParas endif |
| Present Value | if !supportEmptyParas endif | $           944 | $        1,231 | $      23,278 | if !supportEmptyParas endif |
| Value of Firm | if !supportEmptyParas endif | $      25,453 | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Growth Rate in Revenues = | | 2.29% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Target after-tax Operating Margin | | 5.55% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Working Capital as % of Revenues | | 5% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Cost of Capital = | if !supportEmptyParas endif | 9.23% | if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |

Note that the expected growth rate
of 2.29% in revenues is estimated based upon the adjusted reinvestment rate and
return on capital for Boeing. Overall, the value of Boeing as a firm increases
by about $ 6 billion.

            The
effects on valuation of capitalizing R&D expenses tend to be greatest when
the growth rate is computed from the reinvestment rate and the return on
capital. When the growth rate is an exogenous variable, analysts often adjust
the growth rate to reflect the opportunities created by research. In these
cases, the effects on value tend to be unpredictable, and value can be much
higher than or lower than the true value, depending upon whether the growth
rate is over or under estimated.

## The Effects on Earnings Multiples

            When
research and development expenses are reclassified, there will be significant
shifts in some of the multiples commonly used in valuation. All earnings
multiples will have to be re-estimated, since reclassifying R&D as a
capital expenditure changes both operating income and net income. Thus,
price-earnings ratios, PEG ratios, Value/EBIT and Value/EBITDA multiples will
all be affected. The book value ratios will also change since the book value of
capital and equity will both shift when R&D is reclassified as an asset.

            To
the extent that multiples are used to compare how companies within a sector are
valued, there are some who argue that there should be no change in the relative
valuations and rankings when R&D is reclassified. This is clearly not true
since R&D expenses vary across companies, depending upon their relative
size, growth and stage in the life cycle. As a general rule, the earnings
multiples of smaller, higher growth companies will decrease relative to the
earnings multiples of larger, more mature firms.

###### Illustration 6: Effects of R& D Reclassification on Multiples

            In
the following table, we summarize both earnings and book value multiples for
Boeing, when R&D expenses are capitalized, and compare them to the
conventional  measures:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Unadjusted* | *Adjusted* |
| PE Ratio | 36.75 | 23.55 |
| Value/EBITDA | 16.83 | 9.40 |
| Price/Book Value of Equity | 2.52 | 1.51 |
| Value/ Book Value of Capital | 1.83 | 1.32 |

Note that the adjustment reduces
the PE ratio, because the net income is much higher when R&D expenses are
capitalized for Boeing. This reflects the fact that Boeing research expenses
have been increasing over time, and the expense thus outweighs the amortization
charge. There is a similar effect on the Value/EBITDA multiple, but this effect
will occur for all firms with research expenses, since the amortization of the
expense is added back.

            Finally,
the addition of the research asset to the book value of equity and capital
reduces the market to book ratios for all firms with research expenses, though
the magnitude of the impact will vary depending upon how large the expenses are
relative to the size of the firm.

if !supportEmptyParas endif

# Conclusion

                        Accounting
rules clearly specify that operating expenses are expenses designed to generate
income in the current period, whereas capital expenditures are designed to
provide benefits over multiple periods. The current treatment of research and
development expenses are operating expenses seems to violate this distinction.
In this paper, we have argued that R&D expenses are in fact capital
expenditures and should therefore not be shown as part of operating expenses.
To be consistent, we also argue that research and development expenses create a
research asset that has to be amortized over time.

            The
effects of reclassifying R&D expenses on operating income and profitability
ratios will vary across companies. In firms where R&D expenses have been
increasing rapidly over time, reclassifying R&D can push up operating
income significantly and can make return on capital a much higher number. In
mature firms, where R&D expenses have been stable over time, the return on
capital may decrease when R&D is reclassified.

if !supportFootnotes  

---

endif

[if !supportFootnotes[1]endif](#_ftnref1) The reason
we cumulate after-tax  research and
development expenses is because R&D expenses are tax deductible. Amortizing
the entire R&D expense will generate amortization that is too large,
relative to the capital investment from R&D.

[if !supportFootnotes[2]endif](#_ftnref2) There might
have been R&D expenses prior to the five years, but they will have no
material impact on the current value of the research asset since they would
have been entirely amortized by now.
