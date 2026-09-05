---
title: "Estimating Equity Risk Premiums"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/oplease.htm
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
mso-list-template-ids:0;}
@list l3:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
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

Dealing with Operating Leases in Valuation

            The
operating income is a key input into every firm valuation model, and it is often
obtained from an accounting income statement. In using this measure of earnings,
we implicitly assume that operating expenses include only those expenses
designed to create revenue in the current period, and that they do not include
any financing expenses. For the most part, accounting statements separate out
financing expenses such as interest expense and show them after operating
income. There is one significant exception to this rule, and that is created by
the accounting treatment of operating lease expenses, which are categorized as
operating expenses to arrive at operating income. We will make the argument in
this paper that these expenses are really financing expenses, and that ignoring
this misclassification can create significant problems in measuring and
comparing profitability. We also suggest two ways in which we can recategorize
operating lease expenses as financing expenses.

# The Accounting Treatment of Leases

            Firms
often have a choice between buying assets and leasing them. When, in fact,
assets are leased, the treatment of the lease expenses can vary depending upon
how leases are categorized and this can have a significant effect on measures
of operating income and book value of capital. In this part of the paper, we
will begin by looking at the accounting treatment of leases and how it affects
operating earnings, capital and profitability.

## Operating versus Financial Leases: Basis for Categorization

            An
operating or service lease is usually signed for a period much
shorter than the actual life of the asset, and the present value of lease
payments are generally much lower than the actual price of the asset. At the
end of the life of the lease, the equipment reverts back to the lessor, who
will either offer to sell it to the lessee or lease it to somebody else. The
lessee usually has the option to cancel the lease and return equipment to the
lessor. Thus, the ownership of the asset in an operating lease clearly resides
with the lessor, with the lessee bearing little or no risk if the asset becomes
obsolete. An example of operating leases would be the store spaces that are
leased out by specialty retailing firms like the Gap.

            A
financial or capital lease generally lasts for the life of the
asset, with the present value of lease payments covering the price of the
asset. A financial lease generally cannot be canceled, and the lease can be
renewed at the end of its life at a reduced rate or the asset acquired at a
favorable price. In many cases, the lessor is not obligated to pay insurance
and taxes on the asset, leaving these obligations up to the lessee; the lessee
consequently reduces the lease payments, leading to what are called net
leases. In summary, a financial lease imposes substantial risk on the
shoulders of the lessee.

            While
the differences between operating and financial leases are obvious, some lease
arrangements do not fit neatly into one or another of these extremes; rather,
they share some features of both types of leases. These leases are called combination
leases.

## Accounting For Leases

            The
effects of leasing an asset on accounting statements will depend on how the
lease is categorized by the Internal Revenue Service (for tax purposes) and by
generally accepted accounting standards (for measurement purposes). Since
leasing an asset rather than buying it substitutes lease payments as a tax
deduction for the payments that would have been claimed as tax deductions by
the firm if had owned the asset (depreciation and interest expenses on debt),
the IRS is wary of lease arrangements designed purely to speed up tax
deductions.  Some of the issues the
IRS considers in deciding whether lease payments are tax deductible include the
following:

if !supportLists�     
endifAre the lease payments on the asset spread out over the
life of the asset or are they accelerated over a much shorter period?

if !supportLists�     
endifCan the lessee continue to use the asset after the life
of the lease at preferential rates or nominal amounts?

if !supportLists�     
endifCan the lessee buy the asset at the end of the life of
the lease at a price well below market?

If lease payments are made over a period much shorter than
the asset�s life and the lessee is allowed either to continue leasing the asset
at a nominal amount or to buy the asset at a price below market, the IRS may
view the lease as a loan and prohibit the lessee from deducting the lease
payments in the year(s) in which they are made.

            Lease
arrangements also allow firms to take assets off the balance sheet and reduce
their leverage, at least in cosmetic terms; in other words, leases are
sometimes a source of off-balance sheet financing. Consequently, the
Financial Accounting Standards Board (FASB) has specified that firms must treat
leases as capital leases if any one of the following four conditions hold:

1. The life of the lease is at
least 75% of the asset�s life.

2. The ownership of the asset is
transferred to the lessee at the end of the life of the lease.

3. There is a �bargain purchase�
option, whereby the purchase price is below expected market value, increasing
the likelihood that ownership in the asset will be transferred to the lessee at
the end of the lease.

4. The present value of the lease
payments exceeds 90% of the initial value of the asset.

All other leases are treated as operating leases.

## Effect on Expenses, Income and Taxes

            If,
under the above criteria, a lease qualifies as an operating lease, the lease
payments are operating expenses which are tax deductible. Thus, although lease
payments reduce income, they also provide a tax benefit. The after-tax impact
of the lease payment on income can be written as:

After-tax Effect of
Lease on Net Income = Lease Payment (1 - t)

where t is the marginal tax rate on income.

            Note
the similarity in the impact, on after-tax income, of lease payments and
interest payments. Both create a cash outflow while creating a concurrent tax
benefit, which is proportional to the marginal tax rate.

            The
effect of a capital lease on operating and net income is different than that of
an operating lease because capital leases are treated similarly to assets that
are bought by the firm; that is, the firm is allowed to claim depreciation on
the asset and an imputed interest payment on the lease as tax deductions
rather than the lease payment itself. The imputed interest payment is computed
by assuming that the lease payment is a debt payment and by apportioning it
between interest and principal repaid. Thus, a five-year capital lease with
lease payments of $ 1 million a year for a firm with a cost of debt of 10% will
have the interest payments and depreciation imputed to it shown in Table 1.

*Table 1: Lease
Payments, Imputed Interest and Depreciation*

*if !vml![](oplease_files/image003.gif)endif*The lease liability is estimated by taking the
present value of $ 1 million a year for five years at a discount rate of 10%
(the pre-tax cost of debt), assuming that the payments are made at the end of
each year.

Present Value of Lease Liabilities        = $ 1 million (PV of Annuity,
10%, 5 years)

                                                            =
$ 3,790,787

The imputed interest expense each year is computed by
calculating the interest on the remaining lease liability:

In year 1, the lease
liability = $ 3,790,787 \* .10 = $ 379,079

The balance of the lease payment in that year is considered
a reduction in the lease liability:

In year 1, reduction
in lease liability = $ 1,000,000 - $379,079 = $ 620,921

The lease liability is also depreciated over the life of the
asset, using straight line depreciation in this example.

            If
the imputed interest expenses and depreciation, which comprise the tax deductible
flows arising from the lease, are aggregated over the five years, the total tax
deductions amount to $ 5 million, which is also the sum of the lease payments.
The only difference is in timing �� the capital lease leads to greater
deductions earlier and less later on.

## Effect on Balance Sheet

            The
effect of leased assets on the balance sheet will depend on whether the lease
is classified as an operating lease or a capital lease. In an operating lease,
the leased asset is not shown on the balance sheet; in such cases, leases are a
source of off-balance sheet financing. In a capital lease, the leased asset is
shown as an asset on the balance sheet, with a corresponding liability
capturing the present value of the expected lease payments. Given the discretion,
many firms prefer the first approach, since it hides the potential liability to
the firm and understates its effective financial leverage.

            What
prevents firms from constructing lease arrangements to evade these
requirements? The lessor and the lessee have very different incentives, since
the arrangements that would provide the favorable �operating lease� definition
to the lessee are the same ones under which the lessor cannot claim
depreciation, interest, or other tax benefits on the lease. In spite of this
conflict of interest, the line between operating and capital leases remains a
thin one, and firms constantly figure out ways to cross the line.

            These
conditions for classifying operating and capital leases apply in most
countries; France and Japan are major exceptions �� in these countries, all
leases are treated as operating leases.

## Effect on Financial Ratios

            The
effect of leases on the financial ratios of a firm depends on whether the lease
is classified as an operating or a capital lease. Table 2 summarizes types of
profitability, solvency, and leverage ratios and the effects of operating and
capital leases on each. (The effects are misleading, in a way, because they do
not consider what would have happened if the firm had bought the asset rather
than lease it.)

*Table 2: Effects
of Operating and Capitalized Leases*

|  |  |  |
| --- | --- | --- |
| *Ratio* | *Effect of Operating Lease* | *Effect of Capitalized Lease* |
| Return on Capital | if !supportLists�      endifDecreases EBIT through lease expense  if !supportLists�      endifCapital does not reflect leases  if !supportLists�      endifROC is higher | if !supportLists�      endifDecreases EBIT through depreciation  if !supportLists�      endifCapital increases through present value of operating lease  if !supportLists�      endifROC is lower |
| Return on Equity | if !supportLists�      endifNet income lowered by after-tax lease expense  if !supportLists�      endifBV of Equity Unaffected  if !supportLists�      endifROE effect depends on whether lease expense > (imputed interest + depreciation) | if !supportLists�      endifNet income lowered by after-tax interest expense & depreciation  if !supportLists�      endifBV of Equity unaffected  if !supportLists�      endifROE effect depends on whether lease expense > (imputed interest + depreciation) |
| Interest Coverage | if !supportLists�      endifEBIT(1-t) decreases  if !supportLists�      endifInterest Exp. unaffected  if !supportLists�      endifCoverage ratio generally higher | if !supportLists�      endifEBIT(1-t) decreases  if !supportLists�      endifInterest Exp. increases  if !supportLists�      endifCoverage Ratio generally lower |
| Debt Ratio | if !supportLists�      endifDebt is unaffected  if !supportLists�      endifDebt Ratio is lower | if !supportLists�      endifDebt increases (to account for capitalized leases)  if !supportLists�      endifDebt Ratio is higher |

Since the level of financial ratios, and subsequent predictions,
can vary depending on whether leases are treated as operating or capital
leases, it may make sense to convert operating leases into capitalized leases
when comparing these ratios across firms.

## In Summary �

            When
a lease arrangement qualifies as an operating lease, there are profound
consequences for the reported earnings, book value of debt and capital, and
return ratios of that firm. In general,

if !supportLists�      endifboth
the operating and net income of the firm will be lowered

if !supportLists�      endifthe
debt and capital for the firm will be understated

if !supportLists�      endifthe
return on equity and capital will be much higher

when a lease is treated as an operating lease rather than a
capital lease.

# The Financial View of Operating Lease

            In
finance, our view of all leases, operating as well as capital, is colored by
whether the lease payment represents a commitment similar to interest payments
on debt. If the answer is in the affirmative, leasing becomes an alternative to
borrowing and buying the assets, and lease payments becomes financial expenses
rather than operating expenses. This can have significant implications for the
measurements of income, debt and overall profitability. In this section, we
will explore two ways of adjusting valuation inputs for operating leases.

## The Capital Adjustment

            If
operating lease expenses are to be considered financing expenses, it stands to
reason that the present value of commitments to make such payments in the
future has to be treated as debt. Accounting standards in the United States
require that operating lease commitments for the next five years be reported as
part of the footnotes to financial statements, and that any commitments beyond
that period be cumulated and reported with the commitments five years from now.

            To
convert operating lease commitments into an equivalent debt amount requires that
we discount these commitments back to the present. Again, consistency requires
that we use a pre-tax cost of debt for the discounting, since the commitments
are pre-tax and the lease expenses are being treated as financing expenses. The
cost of debt can, however, vary depending upon whether debt is secured or
unsecured. Since the claims of lessees are similar to the claims of unsecured
debt holders, as opposed to secured debt holders, the firm's cost of unsecured
debt should be used in discounting lease commitments.

            To
compute the �debt� value of operating leases, the present value of actual lease
commitments is computed over time. The cumulation of all lease commitments
after the fifth year into that year's amount does create a discounting problem.
One simple approximation that works is to use the average lease commitment over
the first four years as an approximate annuity in converting the final cumulated
amount into annual amounts. Thus, a firm that has average lease commitments of
$ 2 million for the next 4 years, and shows a cumulated commitment of $ 12
million in year 5, can be considered to have annual lease payments of $ 2
million a year for 6 years starting in year 5 for present value purposes.

            The
book value of equity should be unaffected by either adjustment, but the book
value of capital will then be the sum of the debt, including converted
operating leases, and the book value of equity.

###### Illustration 1: The Home Depot - Capital Estimation with Operating Income Recategorized

            The
Home Depot, as a retail firm which leases most of its store spaces, has
considerable lease commitments outstanding. We begin by reporting the operating
lease commitments that the Home Depot reports in its last annual report
(February 28, 1998), and computing the capitalized value of these operating
lease commitments: To compute the present value of the operating lease expenses,
we use the pre-tax cost of borrowing for the Home Depot of 6.25%.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Year | Operating Lease Expense | | Present Value at 6.25% |  | |
| 1 | $          294 | | $          277 |  | |
| 2 | $          291 | | $          258 |  | |
| 3 | $          264 | | $          220 |  | |
| 4 | $          245 | | $          192 |  | |
| 5 | $          236 | | $          174 |  | |
| Yr 6 -15 | $          270 | | $      1,450 |  | |
|  | | PV of Operating Lease Expenses | | | $      2,571 |
if !supportMisalignedColumns|  |  |  |  |  |  |
endif

The operating lease expenses after year 5 are treated as an
annuity. The present value of operating leases can be treated as the equivalent
of debt.

The following table summarizes the
book value of capital, when operating lease expenses are capitalized, at the
Home Depot:

|  |  |
| --- | --- |
| if !supportEmptyParas endif | *Home Depot* |
| Book Value of Capital | $8,513 |
| +  Present Value of Operating Leases | $2,571 |
| = Adjusted Book Value of Capital | $11,084 |

The capitalization of operating
leases increases the book value of capital substantially. There is no effect on
the book value of equity.

## The Income Adjustment

            If
operating lease expenses represent fixed commitments for the future, then they
have to be treated as financing expenses rather than operating expenses. This
will have a significant impact on operating income, since it is defined to be
net of just operating expenses. Thus, the operating income for a firm will
always increase when operating lease expenses are re-categorized as financing
expenses. To obtain the adjusted operating income, the operating income will be
increased by the imputed interest expense on the capitalized debt.

Adjusted Pre-tax
Operating Income= EBIT + Imputed Interest Expense on Capitalized
Lease

            Moving
operating leases from the operating expense to the financing expense column, by
itself, should have no effect on the net income. If we decide to treat
operating leases as capital leases, and estimate imputed interest and
depreciation on it, there can be timing effects on net income, with the net
income in earlier years being lower and in later years being higher as a result
of the recategorization.

Net Incomecomples
= Net Income + Operating Lease Expenses � Imputed Interest Expense on
Capitalized Lease � Depreciation on Capitalized Lease Asset

If we make the simplifying assumption that the operating
lease expense is equal to the sum of the imputed interest expense and the
depreciation, then the net income will be unaffected by this categorization.

###### Illustration 2: The Home Depot - Income Estimation with Operating Leases Recategorized

            We
will estimate the adjusted operating and net income for the Home Depot, using
the information on operating leases provided in illustration 1.  We use the capitalized value of
operating leases of $2,571 million computed in the previous illustration to adjust
the operating income. We compute the inputed interest expense, using Home Depot�s
pre-tax cost of debt of 6.25% and debt value of operating leases:

Imputed Interest
Expense = $2,571 million \* .0625 = $ 161 million

In the following table, we adjust the operating income,
after-tax operating income and net income at Home Depot for operating lease
expenses.

*Adjusted Operating
Income*

|  |  |
| --- | --- |
| if !supportEmptyParas endif | *Home Depot* |
| Operating Income | $2,016 |
| + Imputed Interest Expense on Operating Leases | $161 |
| = Adjusted Operating Income | $2,177 |

Note that the adjusted operating
income is higher than the reported operating income.

            The
after-tax adjusted operating income is computed in the table below for the Home
Depot.

*Adjusted After-tax
Operating Income*

|  |  |
| --- | --- |
| Operating Income (1-t) | $1,311 |
| + Imputed Interest Expense (1- t) | $104 |
| = Adjusted After-tax Operating Income | $1,415 |

The imputed interest expense
added back here is the after-tax expense, obtained by multiplying the pre-tax
interest expense by (1- marginal tax rate).

            Alternatively,
the adjusted operating income could have been multiplied by (1-t) to arrive at
the same estimate of after-tax operating income.

            The
net income of $1,228 million of the Home Depot is unaffected by the
capitalization of operating lease expenses, because we assume that the
operating lease expense is equal to the sum of depreciation and imputed
interest expenses.

## The Profitability Adjustment

            The
conversion of operating lease expenses into financing expenses increases
operating income and capital, and thus affects any profitability measure using
one or both of these numbers. The most directly affected estimate is the return
on capital, which is the operating income divided by the book value of capital.

if !vml![](oplease_files/image006.gif)endif

            The
effect on return on capital will be determined by the present value of
operating lease commitments over time (PVOL) and the method used to compute
depreciation on the asset created. The return on capital can then be estimated
as follows:

if !vml![](oplease_files/image009.gif)endif

If we assume that the difference between operating lease
expenses and the imputed interest expense is equal to the depreciation on the
asset created by operating leases, this computation can be simplified further:

if !vml![](oplease_files/image012.gif)endif

Whether return on capital will increase or decrease in this
case will depend upon whether the unadjusted pre-tax return on capital is
greater than the pre-tax cost of debt. Thus,

If         Unadjusted
Pre-tax ROC > Pre-tax cost of debt          ROC
will decrease

            Unadjusted
Pre-tax ROC < Pre-tax cost of debt          ROC
will increase

The comparison can also be made entirely in after-tax terms.

With our assumption that the
operating lease expense is equal to the sum of the imputed interest expense and
the depreciation on the capitalized lease asset, the return on equity should be
unaffected by whether we capitalize operating leases or not.

###### Illustration 3: The Home Depot - Profitability Estimation with Operating Income recategorized

            The
following table summarizes the adjusted operating income and capital at the
Home Depot.

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Home Depot* | *Home Depot (Adjusted)* |
| After-tax Operating Income | $1,311 | $1,415 |
| BV of Capital - Beginning | $7,205 | $9,776 |
| BV of Capital - Ending | $8,513 | $11,084 |
| BV of Capital - Average | $7,864 | $10,430 |
| ROC (based on average) | 16.67% | 13.56% |
| ROC (based on beginning) | 18.20% | 14.47% |

Note that the return on capital drops when operating
leases are capitalized because the return on capital is well in excess of the
cost of debt of 6.25%. The return on equity will be unaffected since neither
the net income nor the book value of equity will be affected by the
recategorization of operating lease expenses.

## The Free Cash Flow Adjustment

            In
valuation, it is the free cash flows to the firm, defined as the cash flows
left over after reinvestment needs have been met, that are discounted at the
cost of capital to arrive at firm value. When operating lease expenses are
treated as financing expenses, not only is operating income affected but so is
the net capital expenditure. To be consistent with our treatment of operating
leases as financing expenses in the course of acquiring an asset, we need to
consider changes in the present value of operating lease expenses over time as
the equivalent of capital expenditures.  The net capital expenditures on operating leases is
determined by the increase in the present value of the operating lease
commitments over time.

Net Cap Ext
= (PVOLt - PVOLt-1)

Thus, firms with increasing operating lease expenses over
time will have a net capital expenditure reflecting this growth.

            The
final effect on free cash flow to firm of treating operating lease expenses as
financing expenses will depend upon two factors �

if !supportLists�      endifThe
reclassification of operating expense as financing expenses will increase the
free cash flow to the firm because the imputed interest expense on the
capitalized operating leases has to be added back to the operating income.

if !supportLists�      endifAny
increase in the present value of operating lease expenses over time will have a
negative effect on cash flows because it will be treated as an additional
capital expenditures.

There is no effect on free cash flow to equity of
reclassifying operating lease expenses as financing expenses. This is because
the increase in capital expenditures created by the change in the present value
of operating lease expenses will be exactly offset by the increase in net debt
created by this reclassification.

###### Illustration 4: The Home Depot - Free Cash Flow Estimation with Operating Income recategorized

            The
following table summarizes free cash flows to the firm at the Home Depot with
operating leases reclassified as financing expenses:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Home Depot* | *Home Depot (with Operating Lease Adjustment)* |
| Operating Income (1-t) | $1,311 | $1,415 |
| + Depreciation | 283 | 283 |
| - Capital Expenditures | 1,396 | $       1,453 |
| - Change in Working Capital | 474 | 474 |
| FCFF | ($277) | ($230) |

The adjusted operating income is computed in
illustration 2. The present value of operating leases at the Home Depot
increased from $2,514 million to $2,571 million ove the year. The difference of
$ 57 million is added on to the net capital expenditures. The free cash flows
to the firm are more positive (less negative) if operating lease expenses are
treated as financing expenses, because the imputed interest expense is now
treated as a financing expense.

            The
table below summarizes the effect of capitalizing the operating lease expenses
on the free cash flow to equity:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | Home Depot | Home Depot with  adjustment |
| Net Income | $1,228 | $1,228 |
| + Depreciation | $283 | $283 |
| - Capital Expenditures | $1,396 | $1,453 |
| - Change in Working Capital | $474 | $474 |
| + Net Debt Issued | -25 | $32 |
| = FCFE | ($384) | ($384) |

The
increase in capital expenditures of $57 million, attributable to the increase
in the present value of operating leases, also shows up as an increase to net
debt issued,  leaving the ultimate
FCFE unaffected. Intuitively, this makes sense, since reclassifying an
operating expense as a financing expense should not affect the FCFE, which is
after financing expenses.

## The Effect on Discounted Cash Flow Value

            Looking
back at the last three sections, converting operating lease expenses into
financing expenses affects firm cash flows by changing both the operating
income and the net capital expenditures, and the cost of capital by altering
the debt ratio. It can also affect expected growth in the operating income to
the extent that it has an impact on both the reinvestment rate and the expected
return on capital. Once firm value has been estimated with the modified inputs,
the debt that is netted out to arrive at the market value of equity should
include the debt value of operating leases.

            Converting
operating lease expenses into financing expenses should have no impact on
equity valuation. The free cash flows to equity are after both operating and
financing expenses, and are thus unaffected by recategorizing operating lease
expenses, especially since there is no tax effect from the recategorization.
The cost of equity is not affected by the treatment of the present value of
operating lease expenses as debt.

###### Illustration 5: The Home Depot - DCF Value with Operating Income recategorized

            Converting
operating lease expenses affects both cash flows and discount rates. In the
following illustration, we will value Home Depot twice, once with the
unadjusted operating income and cost of capital and one with the adjusted
operating income and cost of capital.

            We
will begin by summarizing the estimates for cost of capital and operating
leases with and without the operating lease adjustments:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | Current | Adjusted |
| Revenues | $24,156 | $24,156 |
| Operating Income (1-t) | $1,310 | $1,415 |
| + Depreciation | $283 | $283 |
| - Capital Expenditures | $1,396 | $1,453 |
| - Change in Working Capital | $474 | $474 |
| FCFF | ($277) | ($230) |
| if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Market Value of Equity = | 51379 | 51379 |
| Debt Outstanding = | 1205 | 3776 |
| Debt/Capital Ratio = | 2.29% | 6.85% |
| Cost of Equity | 9.80% | 9.80% |
| Cost of Debt | 4.06% | 4.06% |
| Cost of Capital | 9.67% | 9.41% |

To do
the valuation, we will assume that revenues, operating income and depreciation
will grow at 15% a year for the next 5 years and 5% thereafter. Capital
expenditures and capitalized leases are assumed to grow 5% a year for the next
5 years.  After year 5, we will
assume that capital expenditures (not counting capital leases) after year 5
will be 150% of depreciation, and that capitalized leases will continue to grow
at 5% a year.

            In
the following table, we summarize the expected cash flows to the firm on an
annual basis for the next 5 years and the terminal year (year 6) with
unadjusted operating income. We also compute the present value of the cash
flows at the unadjusted cost of capital:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| if !supportEmptyParas endif | *Base* | *1* | *2* | *3* | *4* | *5* | | | *Terminal Year* |
| Revenues | $24,156 | $27,779 | $31,946 | $36,738 | $42,249 | $48,586 | | | $51,016 |
| EBIT(1-t) | $1,310 | $1,507 | $1,733 | $1,993 | $2,292 | $2,636 | | | $2,767 |
| + Depreciation | $283 | $325 | $374 | $430 | $495 | $569 | | | $598 |
| - Cap Ex | $1,396 | $1,466 | $1,539 | $1,616 | $1,697 | $1,782 | | | $897 |
| - Change in WC | $474 | $          290 | $          333 | $          383 | $          441 | $           507 | | | $532 |
| FCFF | ($277) | $77 | $235 | $424 | $649 | $916 | | | $1,936 |
| Terminal Value | | | | | | | $      41,475 |  | |
| PV | if !supportEmptyParas endif | $70 | $195 | $321 | $449 | $26,722 | | |  |
if !supportMisalignedColumns|  |  |  |  |  |  |  |  |  |  |
endif

Summing up the present values of the cash flows gives
us an estimate for the value of the firm, and netting out the unadjusted debt
gives us the value of equity:

Value of Firm =                  $27,757

 - Value of Debt =               $1,205

Value of Equity =               $26,552

            In
the following table, we estimate the value of the firm using the adjusted cash
flows to the firm and the adjusted cost of capital:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| if !supportEmptyParas endif | *Base* | *1* | | *2* | *3* | *4* | | *5* | | *Terminal Year* | |
| Revenues | $24,156 | $27,779 | | $31,946 | $36,738 | $42,249 | | $48,586 | | $51,016 | |
| EBIT(1-t) | $1,415 | $1,627 | | $1,871 | $2,152 | $2,475 | | $2,846 | | $2,988 | |
| + Deprec�n | $283 | $325 | | $374 | $430 | $495 | | $569 | | $598 | |
| - Cap Ex | $1,453 | $1,594 | | $1,674 | $1,758 | $1,846 | | $1,938 | | $1,061 | |
| - D WC | $474 | $290 | | $333 | $383 | $441 | | $507 | | $532 | |
| FCFF | ($230) | $68 | | $238 | $441 | $683 | | $970 | | $1,993 | |
| Terminal Value | | | | | | | | $45,218 |  | | |
| PV | if !supportEmptyParas endif | $62 | | $199 | $337 | $477 | | $29,465 | | if !supportEmptyParas endif | |
| Capitalized Leases | $2,571 | $2,700 | | $2,835 | $2,976 | $3,125 | | $3,281 | | $3,445 | |
| Change in Cap Leases | | $129 | $135 | | $142 | | $149 | $156 | $164 | |  |
if !supportMisalignedColumns|  |  |  |  |  |  |  |  |  |  |  |  |
endif

The change in the capitalized leases from year to
year is added on to capital expenditures each year. The value of the firm and
the value of the equity can then be estimated,  using the adjusted value of debt outstanding:

Value of Firm =                  $30,540

 - Value of Debt =               $3,776

Value of Equity =               $26,764

Note
that the value of the firm increases but so does the value of the debt. The
value of equity is very close to the value of equity estimated using the
unadjusted operating income and the unadjusted cost of capital. This should not
be surprising. As long as the debt ratio stays stable, and the operating leases
are fairly valued, treating operating leases as debt should have a neutral
effect on the value of the equity in the firm.

            Under
what conditions will the two values diverge significantly? If the present value
of the operating leases increases at a rate different from other capital
expenditures, the value of the firm computed using the adjusted cashflows and
cost of capital will change because the debt ratio will change. Under those
conditions, the value obtained using the adjusted estimates will be more
precise.

         The value of the equity will be unaffected by the
treatment of operating leases as debt, 
as long as the leverage is not expected to change over the valuation
period. If it is, there will be an effect, because only because the cost of
equity will change as the leverage changes.

## The Adjustment to Multiples

            Much
the same analysis applies when we look at the impact of capitalizing operating
lease expenses on widely used multiples. If the multiple is an equity multiple,
such as price/earnings or price/book value, there should be no effect from
recategorizing operating lease expenses. If the multiple, however, is a firm
value multiple, there can be significant shifts in the value once operating
lease expenses are recategorized, because of the effects on both operating
income and capital. As an example, the Value/EBITDA multiple with operating
lease expenses recategorized would be:

if !vml![](oplease_files/image015.gif)endif

Whether the Value/EBITDA
multiple will increase or decrease will depend, again, on whether the
unadjusted Value/EBITDA is greater than or lesser than the ratio of the present
value of operating lease expenses to the annual operating lease expense.

            With
the value/sales multiple, converting operating leases to equivalent debt value
will always increase the multiple, since the firm value will increase to
include the present value of operating leases while the denominator will remain
unchanged.

            The
implications for analysis where firm value multiples are compared across
companies can be profound in any of the following scenarios:

if !supportLists�     
endifWhen some firms lease assets and other firms buy them,
converting operating leases to equivalent debt will make the firm value
multiples more comparable.

if !supportLists�     
endifWhen some firms treat leases as capital leases, while
other firms qualify for operating leases, there can be significant changes in
how companies rank on firm value multiples after operating leases are converted
into equivalent debt.

if !supportLists�     
endifEven if all firms treat all leases as operating leases,
there can be significant differences across firms in how large these lease
commitments are as a percent of operating expenses. In these cases, again, the
conversion of operating lease expenses to debt will give more realistic
assessments of where these firms stand.

###### Illustration 6: The Home Depot - Multiples with Operating Income recategorized

            In
the following table, we summarize the firm value multiples for the Home Depot
with and without the operating lease adjustments:

|  |  |  |
| --- | --- | --- |
| if !supportEmptyParas endif | *Home Depot* | *Home Depot (with adjustments)* |
| Market Value of Equity | $51,379 | $51,379 |
| Value of Debt | $1,205 | $3,776 |
| if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| EBITDA | $2,299 | $2,593 |
| EBIT | $2,016 | $2,177 |
| EBIT(1-t) | $1,310 | $1,415 |
| if !supportEmptyParas endif | if !supportEmptyParas endif | if !supportEmptyParas endif |
| Value/EBITDA | 22.87 | 21.27 |
| Value/EBIT | 26.08 | 25.34 |
| Value/EBIT(1-t) | 40.13 | 38.98 |

Note that the adjusted value
multiples are consistently lower than the unadjusted multiples when operating
leases are capitalized.

# Conclusion

            Firm
valuation can be impacted by how we deal with operating leases. While the
accounting distinction between capital and operating leases may seem
reasonable, there seems to be no reason, from a financial standpoint, to
maintain that distinction when it comes to estimating operating income, capital
and profitability. Operating lease expenses need to be reclassified as
financial expenses and this will affect our estimates of operating income. The
present value of future operating lease expenses need to be treated like debt,
and this will have an impact on assessments of capital and leverage for firms.
Finally, in estimating free cash flows for valuation purposes, expected
increases in operating lease commitments over time have to be shown as capital
expenditures.     

if !supportEmptyParas endif

if !supportEmptyParas endif

if !supportEmptyParas endif

           

if !supportEmptyParas endif
