---
title: "An Introduction to Valuation"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/background/valintro.htm
---

An Introduction to Valuation  
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
{font-family:"Lucida Grande";
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
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h1
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:12.0pt;
font-family:Times;
mso-font-kerning:0pt;
font-weight:bold;}
h2
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
font-size:12.0pt;
font-family:Times;
font-weight:bold;
font-style:italic;}
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
tab-stops:346.5pt;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
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
tab-stops:.5in 5.0in;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
h5
{mso-style-next:Normal;
margin-top:6.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
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
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
text-decoration:underline;
text-underline:single;
font-weight:normal;}
p.MsoHeading7, li.MsoHeading7, div.MsoHeading7
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:7;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
p.MsoHeading8, li.MsoHeading8, div.MsoHeading8
{mso-style-next:Normal;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:27.0pt;
margin-bottom:.0001pt;
text-align:justify;
text-indent:-27.0pt;
line-height:150%;
mso-pagination:none;
page-break-after:avoid;
mso-outline-level:8;
tab-stops:2.0in 225.0pt;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:Times;
color:black;
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
font-size:16.0pt;
font-family:Times;
font-style:italic;}
p.MsoToc1, li.MsoToc1, div.MsoToc1
{mso-style-next:Normal;
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
{mso-style-next:Normal;
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
{mso-style-next:Normal;
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
{mso-style-next:Normal;
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
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
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
p.MsoCaption, li.MsoCaption, div.MsoCaption
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:none;
mso-layout-grid-align:none;
text-autospace:none;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;
vertical-align:super;}
span.MsoEndnoteReference
{vertical-align:super;}
p.MsoEndnoteText, li.MsoEndnoteText, div.MsoEndnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
{margin:0in;
margin-bottom:.0001pt;
text-align:center;
text-indent:.25in;
line-height:150%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .5pt;
padding:0in;
mso-padding-alt:1.0pt 4.0pt 1.0pt 4.0pt;
font-size:12.0pt;
font-family:Times;
font-weight:bold;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
tab-stops:.5in 5.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5in;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText2, li.MsoBodyText2, div.MsoBodyText2
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:1.0pt 1.0pt 1.0pt 1.0pt;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText3, li.MsoBodyText3, div.MsoBodyText3
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
border:none;
mso-border-alt:solid windowtext .5pt;
padding:0in;
mso-padding-alt:1.0pt 4.0pt 1.0pt 4.0pt;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:.5in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent3, li.MsoBodyTextIndent3, div.MsoBodyTextIndent3
{margin-top:0in;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:.25in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:8.0pt;
font-family:Times;}
p
{margin-right:0in;
mso-margin-top-alt:auto;
mso-margin-bottom-alt:auto;
margin-left:0in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
table.MsoNormalTable
{mso-style-parent:"";
font-size:10.0pt;
font-family:"Times New Roman";}
p.Questions, li.Questions, div.Questions
{mso-style-name:Questions;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:9.0pt;
margin-bottom:.0001pt;
text-align:justify;
line-height:18.0pt;
mso-pagination:widow-orphan;
font-size:11.0pt;
font-family:Times;}
p.Times12, li.Times12, div.Times12
{mso-style-name:Times12;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
span.msoIns
{mso-style-type:export-only;
mso-style-name:"";
font-style:italic;
color:teal;}
span.msoDel
{mso-style-type:export-only;
mso-style-name:"";
text-decoration:line-through;
display:none;
color:red;}
/\* Page Definitions \*/
@page
{mso-page-border-surround-header:no;
mso-page-border-surround-footer:no;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":valintro\_files:header.htm") eh1;
mso-header:url(":valintro\_files:header.htm") h1;
mso-paper-source:0;}
div.Section1
{page:Section1;}
/\* List Definitions \*/
@list l0
{mso-list-id:53047983;
mso-list-type:hybrid;
mso-list-template-ids:-808922618 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l0:level1
{mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-.25in;}
@list l0:level2
{mso-level-tab-stop:1.5in;
mso-level-number-position:left;
margin-left:1.5in;
text-indent:-.25in;}
@list l0:level3
{mso-level-tab-stop:2.0in;
mso-level-number-position:left;
margin-left:2.0in;
text-indent:-.25in;}
@list l0:level4
{mso-level-tab-stop:2.5in;
mso-level-number-position:left;
margin-left:2.5in;
text-indent:-.25in;}
@list l0:level5
{mso-level-tab-stop:3.0in;
mso-level-number-position:left;
margin-left:3.0in;
text-indent:-.25in;}
@list l0:level6
{mso-level-tab-stop:3.5in;
mso-level-number-position:left;
margin-left:3.5in;
text-indent:-.25in;}
@list l0:level7
{mso-level-tab-stop:4.0in;
mso-level-number-position:left;
margin-left:4.0in;
text-indent:-.25in;}
@list l0:level8
{mso-level-tab-stop:4.5in;
mso-level-number-position:left;
margin-left:4.5in;
text-indent:-.25in;}
@list l0:level9
{mso-level-tab-stop:5.0in;
mso-level-number-position:left;
margin-left:5.0in;
text-indent:-.25in;}
@list l1
{mso-list-id:112287402;
mso-list-type:hybrid;
mso-list-template-ids:-277077484 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l1:level1
{mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-.25in;}
@list l2
{mso-list-id:411006689;
mso-list-type:hybrid;
mso-list-template-ids:-1240011340 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l2:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l3
{mso-list-id:643894136;
mso-list-type:hybrid;
mso-list-template-ids:672927998 1962993086 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l3:level1
{mso-level-number-format:alpha-lower;
mso-level-text:"\(%1\)";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l4
{mso-list-id:923997435;
mso-list-type:hybrid;
mso-list-template-ids:767046464 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l4:level1
{mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-.25in;}
@list l5
{mso-list-id:1751191394;
mso-list-type:hybrid;
mso-list-template-ids:-1815943458 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
.style1 {color: #000000}
.style3 {color: #0066cc}
-->
   

[![](../Budimage/titlesm.gif)](../home.htm)

What
is Valuation?

            Knowing
what an asset is worth and what determines that value is a pre-requisite for
intelligent decision making -- in choosing investments for a portfolio, in
deciding on the appropriate price to pay or receive in a takeover and in making
investment, financing and dividend choices when running a business. The premise
of valuation is that we can make reasonable estimates of value for most assets,
and that the same fundamental principles determine the values of all types of
assets, real as well as financial. Some assets are easier to value than others,
the details of valuation vary from asset to asset, and the uncertainty
associated with value estimates is different for different assets, but the core
principles remain the same. This introduction lays out some general insights
about the valuation process and outlines the role that valuation plays in
portfolio management, acquisition analysis and in corporate finance. It also
examines the three basic approaches that can be used to value an asset.

# A philosophical basis for valuation

            A
postulate of sound investing is that an investor does not pay more for an asset
than it is worth. This statement may seem logical and obvious, but it is
forgotten and rediscovered at some time in every generation and in every
market. There are those who are disingenuous enough to argue that value is in
the eyes of the beholder, and that any price can be justified if there are
other investors willing to pay that price. That is patently absurd. Perceptions
may be all that matter when the asset is a painting or a sculpture, but we do
not and should not buy most assets for aesthetic or emotional reasons; we buy
financial assets for the cashflows we expect to receive from them.
Consequently, perceptions of value have to be backed up by reality, which
implies that the price we pay for any asset should reflect the cashflows it is
expected to generate. Valuation models attempt to relate value to the level of,
uncertainty about and expected growth in these cashflows.

            There
are many aspects of valuation where we can agree to disagree, including
estimates of true value and how long it will take for prices to adjust to that
true value. But there is one point on which there can be no disagreement. Asset
prices cannot be justified by merely using the argument that there will be
other investors around who will pay a higher price in the future. That is the
equivalent of playing a very expensive game of musical chairs, where every
investor has to answer the question, "Where will I be when the music
stops?� before playing. The problem with investing with the expectation that
there will be a bigger fool around to sell an asset to, when the time comes, is
that you might end up being the biggest fool of all.

# Inside the Valuation Process

            There
are two extreme views of the valuation process. At one end are those who
believe that valuation, done right, is a hard science, where there is little
room for analyst views or human error. At the other are those who feel that
valuation is more of an art, where savvy analysts can manipulate the numbers to
generate whatever result they want. The truth does lies somewhere in the middle
and we will use this section to consider three components of the valuation
process that do not get the attention they deserve – the bias that
analysts bring to the process, the uncertainty that they have to grapple with
and the complexity that modern technology and easy access to information have
introduced into valuation.

## Value first, Valuation to follow: Bias in Valuation

            We
almost never start valuing a company with a blank slate.  All too often, our views on a company
are formed before we start inputting the numbers into the models that we use
and not surprisingly, our conclusions tend to reflect our biases. We will begin
by considering the sources of bias in valuation and then move on to evaluate
how bias manifests itself in most valuations. We will close with a discussion
of how best to minimize or at least deal with bias in valuations.

### Sources of Bias

            The
bias in valuation starts with the companies we choose to value. These
choices are almost never random, and how we make them can start laying the
foundation for bias. It may be that we have read something in the press (good
or bad) about the company or heard from an expert that it was under or over
valued.  Thus, we already begin
with a perception about the company that we are about to value. We add to the
bias when we collect the information we need to value the firm. The
annual report and other financial statements include not only the accounting
numbers but also management discussions of performance, often putting the best
possible spin on the numbers. With many larger companies, it is easy to access
what other analysts following the stock think about these companies.
Zacks, I/B/E/S and First Call, to name three services among many, provide
summaries of how many analysts are bullish and bearish about the stock, and we
can often access their complete valuations. Finally, we have the market�s
own estimate of the value of the company- the market price – adding
to the mix. Valuations that stray too far from this number make analysts
uncomfortable, since they may reflect large valuation errors (rather than
market mistakes).

            In
many valuations, there are institutional factors that add to this
already substantial bias. For instance, it is an acknowledged fact that equity
research analysts are more likely to issue buy rather than sell
recommendations, i.e., that they are more likely to find firms to be
undervalued than overvalued.[if !supportFootnotes[1]endif](#_ftn1) This
can be traced partly to the difficulties analysts face in obtaining access and
collecting information on firms that they have issued sell recommendations on,
and partly to pressure that they face from portfolio managers, some of whom
might have large positions in the stock, and from their own firm�s investment
banking arms which have other profitable relationships with the firms in
question.

            The
reward and punishment structure associated with finding companies to be
under and over valued is also a contributor to bias. An analyst whose
compensation is dependent upon whether she finds a firm is under or over valued
will be biased in her conclusions. This should explain why acquisition
valuations are so often biased upwards. The analysis of the deal, which is
usually done by the acquiring firm�s investment banker, who also happens to be
responsible for carrying the deal to its successful conclusion, can come to one
of two conclusions. One is to find that the deal is seriously over priced and recommend
rejection, in which case the analyst receives the eternal gratitude of the
stockholders of the acquiring firm but little else. The other is to find that
the deal makes sense (no matter what the price) and to reap the ample financial
windfall from getting the deal done.

### Manifestations of Bias

            There
are three ways in which our views on a company (and the biases we have) can
manifest themselves in value. The first is in the inputs that we use in the
valuation. When we value companies, we constantly come to forks in the road
where we have to make assumptions to move on. These assumptions can be
optimistic or pessimistic. For a company with high operating margins now, we
can either assume that competition will drive the margins down to industry averages
very quickly (pessimistic) or that the company will be able to maintain its
margins for an extended period (optimistic).  The path we choose will reflect our prior biases.  It should come as no surprise then that
the end value that we arrive at is reflective of the optimistic or pessimistic
choices we made along the way.

            The
second is in what we will call post-valuation tinkering, where analysts
revisit assumptions after a valuation in an attempt to get a value closer to
what they had expected to obtain starting off. Thus, an analyst who values a
company at $ 15 per share, when the market price is $ 25, may revise his growth
rates upwards and his risk downwards to come up a higher value, if she believed
that the company was under valued to begin with.

            The
third is to leave the value as is but attribute the difference between the
value we estimate and the value we think is the right one to a qualitative
factor such as synergy or strategic considerations. This is a common device
in acquisition valuation where analysts are often called upon to justify the
unjustifiable. In fact, the use of premiums and discounts, where we augment or
reduce estimated value, provides a window on the bias in the process. The use
of premiums – control and synergy are good examples – is
commonplace in acquisition valuations, where the bias is towards pushing value
upwards (to justify high acquisition prices). The use of discounts –
illiquidity and minority discounts, for instance – are more typical in
private company valuations for tax and divorce court, where the objective is
often to report as low a value as possible for a company.

### What to do about bias

            Bias
cannot be regulated or legislated out of existence. Analysts are human and
bring their biases to the table. However, there are ways in which we can
mitigate the effects of bias on valuation:

if !supportLists1.     endif*Reduce
institutional pressures*: As we noted
earlier, a significant portion of bias can be attributed to institutional
factors. Equity research analysts in the 1990s, for instance, in addition to
dealing with all of the standard sources of bias had to grapple with the demand
from their employers that they bring in investment banking business.
Institutions that want honest sell-side equity research should protect their
equity research analysts who issue sell recommendations on companies, not only
from irate companies but also from their own sales people and portfolio
managers.

if !supportLists2.     endif*De-link
valuations from reward/punishment*: Any
valuation process where the reward or punishment is conditioned on the outcome
of the valuation will result in biased valuations. In other words, if we want
acquisition valuations to be unbiased, we have to separate the deal analysis
from the deal making to reduce bias.

if !supportLists3.     endif*No
pre-commitments*: Decision makers should avoid
taking strong public positions on the value of a firm before the valuation is
complete. An acquiring firm that comes up with a price prior to the valuation
of a target firm has put  analysts
in an untenable position, where they are called upon to justify this price. In
far too many cases, the decision on whether a firm is under or over valued
precedes the actual valuation, leading to seriously biased analyses.

if !supportLists4.     endif*Self-Awareness*: The best antidote to bias is awareness. An analyst
who is aware of the biases he or she brings to the valuation process can either
actively try to confront these biases when making input choices or open the
process up to more objective points of view about a company�s future.

if !supportLists5.     endif*Honest
reporting*: In Bayesian statistics, analysts
are required to reveal their priors (biases) before they present their results
from an analysis. Thus, an environmentalist will have to reveal that he or she
strongly believes that there is a hole in the ozone layer before presenting
empirical evidence to that effect. The person reviewing the study can then
factor that bias in while looking at the conclusions. Valuations would be much
more useful if analysts revealed their biases up front.

While we cannot eliminate bias in valuations,
we can try to minimize its impact by designing valuation processes that are
more protected from overt outside influences and by report our biases with our
estimated values.

## It is only an estimate: Imprecision and Uncertainty in Valuation

            Starting
early in life, we are taught that if we do things right, we will get the right
answers. In other words, the precision of the answer is used as a measure of
the quality of the process that yielded the answer. While this may be
appropriate in mathematics or physics, it is a poor measure of quality in
valuation. Barring a very small subset of assets, there will always be
uncertainty associated with valuations, and even the best valuations come with
a substantial margin for error. In this section, we examine the sources of
uncertainty and the consequences for valuation.

### Sources of Uncertainty

            Uncertainty
is part and parcel of the valuation process, both at the point in time that we
value a business and in how that value evolves over time as we get new information
that impacts the valuation. That information can be specific to the firm being
valued, more generally about the sector in which the firm operates or even be
general market information (about interest rates and the economy).

When valuing
an asset at any point in time, we make forecasts for the future. Since none
of us possess crystal balls, we have to make our best estimates, given the
information that we have at the time of the valuation. Our estimates of value
can be wrong for a number of reasons, and we can categorize these reasons into
three groups.

a. Estimation Uncertainty:
Even if our information sources are impeccable, we have to convert raw
information into inputs and use these inputs in models. Any mistakes or
mis-assessments that we make at either stage of this process will cause
estimation error.

b. Firm-specific Uncertainty:
The path that we envision for a firm can prove to be hopelessly wrong. The firm
may do much better or much worse than we expected it to perform, and the
resulting earnings and cash flows will be very different from our estimates.

c. Macroeconomic Uncertainty:
Even if a firm evolves exactly the way we expected it to, the macro economic
environment can change in unpredictable ways. Interest rates can go up or down and
the economy can do much better or worse than expected. These macro economic
changes will affect value.

The contribution of each type of
uncertainty to the overall uncertainty associated with a valuation can vary
across companies. When valuing a mature cyclical or commodity company, it may
be macroeconomic uncertainty that is the biggest factor causing actual numbers
to deviate from expectations. Valuing a young technology company can expose
analysts to far more estimation and firm-specific uncertainty. Note that the
only source of uncertainty that can be clearly laid at the feet of the analyst
is estimation uncertainty.

            Even
if we feel comfortable with our estimates of an asset�s values at any point in
time, that value itself will change over time, as a consequence of new
information that comes out both about the firm and about the overall market..
Given the constant flow of information into financial markets, a valuation done
on a firm ages quickly, and has to be updated to reflect current information.  Thus, technology companies that were
valued highly in late 1999, on the assumption that the high growth from the
nineties would continue into the future, would have been valued much less in
early 2001, as the prospects of future growth dimmed. With the benefit of
hindsight, the valuations of these companies (and the analyst recommendations)
made in 1999 can be criticized, but they may well have been reasonable, given
the information available at that time.

### Responses of Uncertainty

            Analysts
who value companies confront uncertainty at every turn in a valuation and they
respond to it in both healthy and unhealthy ways. Among the healthy responses
are the following:

if !supportLists1.     endifBetter
Valuation Models: Building better valuation models that use more of the
information that is available at the time of the valuation is one way of
attacking the uncertainty problem. It should be noted, though, that even the
best-constructed models may reduce estimation uncertainty but they cannot reduce
or eliminate the very real uncertainties associated with the future

if !supportLists2.     endifValuation
Ranges: A few analysts recognize that the value that they obtain for a
business is an estimate and try to quantify a range on the estimate. Some use
simulations and others derive expected, best-case and worst-case estimates of
value.  The output that they
provide therefore yields both their estimates of value and their uncertainty
about that value.

if !supportLists3.     endifProbabilistic
Statements: Some analysts couch their valuations in probabilistic terms to
reflect the uncertainty that they feel. Thus, an analyst who estimates a value
of $ 30 for a stock which is trading at $ 25 will state that there is a 60 or
70% probability that the stock is under valued rather than make the categorical
statement that it is under valued. Here again, the probabilities that accompany
the statements provide insight into the uncertainty that the analyst perceives
in the valuation.

In general, healthy responses to
uncertainty are open about its existence and provide information on its
magnitude to those using the valuation. These users can then decide how much
caution they should exhibit while acting on the valuation.

      Unfortunately,
not all analysts deal with uncertainty in ways that lead to better decisions.
The unhealthy responses to uncertainty include:

if !supportLists1.     endifPassing
the buck: Some analysts try to pass on responsibility for the estimates by
using other people�s numbers in the valuation. For instance, analysts will often
use the growth rate estimated by other analysts valuing a company as their
estimate of growth. If the valuation turns out to be right, they can claim
credit for it, and if it turns out wrong, they can blame other analysts for
leading them down the garden path.

if !supportLists2.     endifGiving
up on fundamentals: A significant number of analysts give up, especially on
full-fledged valuation models, unable to confront uncertainty and deal with it.
All too often, they fall back on more simplistic ways of valuing companies
(multiples and comparables, for example) that do not require explicit
assumptions about the future. A few decide that valuation itself is pointless
and resort to reading charts and gauging market perception.

In closing, it is natural to feel uncomfortable
when valuing equity in a company. We are after all trying to make our best
judgments about an uncertain future. The discomfort will increase as we move
from valuing stable companies to growth companies, from valuing mature
companies to young companies and from valuing developed market companies to
emerging market companies.

### What to do about uncertainty

            The
advantage of breaking uncertainty down into estimation uncertainty,
firm-specific and macroeconomic uncertainty is that it gives us a window on
what we can manage, what we can control and what we should just let pass
through into the valuation. Building better models and accessing superior
information will reduce estimation uncertainty but will do little to reduce
exposure to firm-specific or macro-economic risk. Even the best-constructed
model will be susceptible to these uncertainties.

            In
general, analysts should try to focus on making their best estimates of
firm-specific information – how long will the firm be able to maintain
high growth? How fast will earnings grow during that period? What type of
excess returns will the firm earn?– and steer away from bringing in their
views on macro economic variables. To see why, assume that you believe that
interest rates today are too low and that they will go up by about 1.5% over
the next year. If you build in the expected rise in interest rates into your
discounted cash flow valuations, they will all yield low values for the
companies that you are analyzing. A person using these valuations will be faced
with a conundrum because she will have no way of knowing how much of this over
valuation is attributable to your macroeconomic views and how much to your
views of the company.

            In
summary, analysts should concentrate on building the best models they can with
as much information as they can legally access, trying to make their best
estimates of firm-specific components and being as neutral as they can on macro
economic variables. As new information comes in, they should update their
valuations to reflect the new information. There is no place for false pride in
this process. Valuations can change dramatically over time and they should if
the information warrants such a change.

### The Payoff to Valuation

            Even
at the end of the most careful and detailed valuation, there will be
uncertainty about the final numbers, colored as they are by assumptions that we
make about the future of the company and the economy in which it operates. It
is unrealistic to expect or demand absolute certainty in valuation, since the
inputs are estimated with error. This also means that analysts have to give
themselves reasonable margins for error in making recommendations on the basis
of valuations.

The corollary to
this statement is that a valuation cannot be judged by its precision. Some
companies can be valued more precisely than others simply because there is less
uncertainty about the future. We can value a mature company with relatively few
assumptions and be reasonably comfortable with the estimated value. Valuing a technology
firm will require far more assumptions, as will valuing an emerging market
company.  A scientist looking at
the valuations of these companies (and the associated estimation errors) may
very well consider the mature company valuation the better one, since it is the
most precise, and the technology firms and emerging market company valuations
to be inferior because there is most uncertainty associated with the estimated
values. The irony is that the payoff to valuation will actually be highest when
you are most uncertain about the numbers. After all, it is not how precise a
valuation is that determines its usefulness but how precise the value is
relative to the estimates of other investors trying to value the same company.
Any one can value a zero-coupon default-free bond with absolute precision.
Valuing a young technology firm or an emerging market firm requires a blend of
forecasting skills, tolerance for ambiguity and willingness to make mistakes
that many analysts do not have. Since most analysts tend to give up in the face
of such uncertainty, the analyst who perseveres and makes her best estimates
(error-prone though they might be) will have a differential edge.

We do not want to
leave the impression that we are completely helpless in the face of
uncertainty. Simulations, decision trees and sensitivity analyses are tools
that help us deal with uncertainty but not eliminate it.

## Are bigger models better? Valuation Complexity

            Valuation
models have become more and more complex over the last two decades, as a
consequence of two developments. On the one side, computers and calculators
have become far more powerful and accessible in the last few decades. With
technology as our ally, tasks that would have taken us days in the pre-computer
days can be accomplished in minutes. On the other side, information is both
more plentiful, and easier to access and use. We can download detailed
historical data on thousands of companies and use them as we see fit. The
complexity, though, has come at a cost. In this section, we will consider the
trade off on complexity and how analysts can decide how much to build into
models.

### More detail or less detail

            A
fundamental question that we all face when doing valuations is how much detail
we should break a valuation down into. There are some who believe that more
detail is always better than less detail and that the resulting valuations are
more precise. We disagree. The trade off on adding detail is a simple one. On
the one hand, more detail gives analysts a chance to use specific information
to make better forecasts on each individual item. On the other hand, more
detail creates the need for more inputs, with the potential for error on each
one, and generates more complicated models. Thus, breaking working capital down
into its individual components – accounts receivable, inventory, accounts
payable, supplier credit etc. – gives an analyst the discretion to make
different assumptions about each item, but this discretion has value only if
the analyst has the capacity to differentiate between the items.

### The Cost of Complexity

            A
parallel and related question to how much detail there should be in a valuation
is the one of how complex a valuation model should be. There are clear costs
that we pay as models become more complex and require more information.

if !supportLists1.     endifInformation
Overload: More information does not always lead to better valuations. In
fact, analysts can become overwhelmed when faced with vast amounts of
conflicting information and this can lead to poor input choices.  The problem is exacerbated by the fact
that analysts often operate under time pressure when valuing companies. Models
that require dozens of inputs to value a single company often get short shrift
from users. A model�s output is only as good as the inputs that go into it; it
is garbage in, garbage out.

if !supportLists2.     endifBlack
Box Syndrome: The models become so complicated that the analysts using them
no longer understand their inner workings. They feed inputs into the model�s black
box and the box spits out a value. In effect, the refrain from analysts becomes
�The model valued the company at $ 30 a share� rather than �We valued the
company at $ 30 a share�.  Of
particular concern should be models where portions of the models are
proprietary and cannot be accessed (or modified) by analysts. This is often the
case with commercial valuation models, where vendors have to keep a part of the
model out of bounds to make their services indispensable.

if !supportLists3.     endifBig
versus Small Assumptions: Complex models often generate voluminous and
detailed output and it becomes very difficult to separate the big assumptions
from the small assumptions. In other words, the assumption that pre-tax
operating margins will stay at 20% (a big assumption that doubles the value of
the company) has to compete with the assumption that accounts receivable will
decline from 5% of revenues to 4% of revenues over the next 10 years (a small
assumption that has almost no impact on value).

### The Principle of Parsimony

            In
the physical sciences, the principle of parsimony dictates that we try the
simplest possible explanation for a phenomenon before we move on to more
complicated ones. We would be well served adopting a similar principle in
valuation. When valuing an asset, we want to use the simplest model we can get
away with. In other words, if we can value an asset with three inputs, we
should not be using five. If we can value a company with 3 years of cashflow
forecasts, forecasting ten years of cash flows is asking for trouble.

The problem with
all-in-one models that are designed to value all companies is that they have to
be set up to value the most complicated companies that we will face and not the
least complicated.  Thus, we are forced
to enter inputs and forecast values for simpler companies that we really do not
need to estimate. In the process, we can mangle the values of assets that
should be easy to value. Consider, for instance, the cash and marketable
securities held by firms as part of their assets. The simplest way to value
this cash is to take it at face value. Analysts who try to build discounted
cash flow or relative valuation models to value cash often mis-value it, either
by using the wrong discount rate for the cash income or by using the wrong
multiple for cash earnings.[if !supportFootnotes[2]endif](#_ftn2)

# Approaches to Valuation

Analysts use
a wide spectrum of models, ranging from the simple to the sophisticated. These
models often make very different assumptions about the fundamentals that
determine value, but they do share some common characteristics and can be
classified in broader terms. There are several advantages to such a
classification -- it makes it is easier to understand where individual models
fit in to the big picture, why they provide different results and when they
have fundamental errors in logic.

In general
terms, there are three approaches to valuation. The first, discounted cashflow
valuation, relates the value of an asset to the present value of expected
future cashflows on that asset. The second, relative valuation, estimates the
value of an asset by looking at the pricing of 'comparable' assets relative to
a common variable like earnings, cashflows, book value or sales. The third,
contingent claim valuation, uses option pricing models to measure the value of
assets that share option characteristics. While they can yield different
estimates of value, one of the objectives of discussing valuation models is to
explain the reasons for such differences, and to help in picking the right
model to use for a specific task.

## Discounted Cashflow Valuation

            In
discounted cashflows valuation, the value of an asset is the present value of
the expected cashflows on the asset, discounted back at a rate that reflects
the riskiness of these cashflows. This approach gets the most play in
classrooms and comes with the best theoretical credentials. In this section, we
will look at the foundations of the approach and some of the preliminary
details on how we estimate its inputs.

### Basis for Approach

We buy most
assets because we expect them to generate cash flows for us in the future. In
discounted cash flow valuation, we begin with a simple proposition. The value
of an asset is not what someone perceives it to be worth but it is a function
of the expected cash flows on that asset. Put simply, assets with high and
predictable cash flows should have higher values than assets with low and
volatile cash flows. In discounted cash flow valuation, we estimate the value
of an asset as the present value of the expected cash flows on it.

                                                                                                 if !vml![](valintro_files/image003.png)endif

where,

                                                                                                n
= Life of the asset

                                                                                                E(CFt) = Expected cashflow in
period t

                                                                                                r
= Discount rate reflecting the riskiness of the estimated cashflows

The cashflows
will vary from asset to asset -- dividends for stocks, coupons (interest) and
the face value for bonds and after-tax cashflows for a business. The discount
rate will be a function of the riskiness of the estimated cashflows, with
higher rates for riskier assets and lower rates for safer ones.

                                                                                                Using
discounted cash flow models is in some sense an act of faith. We believe that
every asset has an intrinsic value and we try to estimate that intrinsic value
by looking at an asset�s fundamentals. What is intrinsic value? Consider it the
value that would be attached to an asset by an all-knowing analyst with access
to all information available right now and a perfect valuation model. No such
analyst exists, of course, but we all aspire to be as close as we can to this
perfect analyst. The problem lies in the fact that none of us ever gets to see
what the true intrinsic value of an asset is and we therefore have no way of
knowing whether our discounted cash flow valuations are close to the mark or
not.

### Classifying Discounted Cash Flow Models

            There
are three distinct ways in which we can categorize discounted cash flow models.
In the first, we differentiate between valuing a business as a going concern as
opposed to a collection of assets. In the second, we draw a distinction between
valuing the equity in a business and valuing the business itself. In the third,
we lay out three different and equivalent ways of doing discounted cash flow
valuation – the expected cash flow approach, a value based upon excess
returns and adjusted present value.

#### a. Going Concern versus Asset Valuation

            The
value of an asset in the discounted cash flow framework is the present value of
the expected cash flows on that asset. Extending this proposition to valuing a
business, it can be argued that the value of a business is the sum of the
values of the individual assets owned by the business. While this may be
technically right, there is a key difference between valuing a collection of
assets and a business. A business or a company is an on-going entity with
assets that it already owns and assets it expects to invest in the future. This
can be best seen when we look at the financial balance sheet (as opposed to an
accounting balance sheet) for an ongoing company in figure 1.1:

if !vml![](valintro_files/image006.png)endif

Note that investments that have
already been made are categorized as assets in place, but investments that we
expect the business to make in the future are growth assets.

            A
financial balance sheet provides a good framework to draw out the differences
between valuing a business as a going concern and valuing it as a collection of
assets. In a going concern valuation, we have to make our best judgments not
only on existing investments but also on expected future investments and their
profitability. While this may seem to be foolhardy, a large proportion of the
market value of growth companies comes from their growth assets. In an
asset-based valuation, we focus primarily on the assets in place and estimate
the value of each asset separately. Adding the asset values together yields the
value of the business. For companies with lucrative growth opportunities,
asset-based valuations will yield lower values than going concern valuations.

            One
special case of asset-based valuation is liquidation valuation, where we value
assets based upon the presumption that they have to be sold now. In theory,
this should be equal to the value obtained from discounted cash flow valuations
of individual assets but the urgency associated with liquidating assets quickly
may result in a discount on the value. How large the discount will be will
depend upon the number of potential buyers for the assets, the asset
characteristics and the state of the economy.

#### b. Equity Valuation versus Firm Valuation

There are two
ways in which we can approach discounted cash flow valuation. The first is to
value the entire business, with both assets-in-place and growth assets; this is
often termed firm or enterprise valuation.

if !vml![](valintro_files/image009.png)endif  
The cash flows before debt payments and after reinvestment needs are called free
cash flows to the firm, and the discount rate that reflects the composite
cost of financing from all sources of capital is called the cost of capital.

The second way is
to just value the equity stake in the business, and this is called equity
valuation.

if !vml![](valintro_files/image012.png)endif  
The cash flows after debt payments and reinvestment needs are called free cash flows
to equity, and the discount rate that reflects just the cost of equity
financing is the cost of equity.

            Note
also that we can always get from the former (firm value) to the latter (equity
value) by netting out the value of all non-equity claims from firm value. Done
right, the value of equity should be the same whether it is valued directly (by
discounting cash flows to equity a the cost of equity) or indirectly (by
valuing the firm and subtracting out the value of all non-equity claims).

#### c. Variations on DCF Models

            The
model that we have presented in this section, where expected cash flows are
discounted back at a risk-adjusted discount rate, is the most commonly used
discounted cash flow approach but there are two widely used variants. In the first,
we separate the cash flows into excess return cash flows and normal return cash
flows. Earning the risk-adjusted required return (cost of capital or equity) is
considered a normal return cash flow but any cash flows above or below this
number are categorized as excess returns; excess returns can therefore be
either positive or negative. With the *excess return valuation* framework, the value of a business can be written as
the sum of two components:

Value of business = Capital
Invested in firm today + Present value of excess return cash flows from both
existing and future projects

If we make the assumption that the
accounting measure of capital invested (book value of capital) is a good
measure of capital invested in assets today, this approach implies that firms
that earn positive excess return cash flows will trade at market values higher
than their book values and that the reverse will be true for firms that earn
negative excess return cash flows.

            In
the second variation, called the *adjusted present value (APV) approach*, we separate the effects on value of debt financing
from the value of the assets of a business. In general, using debt to fund a
firm�s operations creates tax benefits (because interest expenses are tax
deductible) on the plus side and increases bankruptcy risk (and expected
bankruptcy costs) on the minus side. In the APV approach, the value of a firm
can be written as follows:

Value of business = Value of
business with 100% equity financing + Present value of Expected Tax Benefits of
Debt – Expected Bankruptcy Costs

In contrast to the conventional
approach, where the effects of debt financing are captured in the discount
rate, the APV approach attempts to estimate the expected dollar value of debt
benefits and costs separately from the value of the operating assets.

            While
proponents of each approach like to claim that their approach is the best and
most precise, we will argue that the three approaches yield the same estimates
of value, if we make consistent assumptions.

### Inputs to Discounted Cash Flow Models

There
are three inputs that are required to value any asset in this model - the *expected
cash flow*, the *timing* of the cash flow and the *discount rate* that is appropriate given the riskiness of these
cash flows.

#### a. Discount Rates

            In
valuation, we begin with the fundamental notion that the discount rate used on
a cash flow should reflect its riskiness, with higher risk cash flows having
higher discount rates. There are two ways of viewing risk. The first is purely
in terms of the likelihood that an entity will default on a commitment to make
a payment, such as interest or principal due, and this is called default
risk. When looking at debt, the cost of debt is the rate that
reflects this default risk.

The second way of
viewing risk is in terms of the variation of actual returns around expected
returns. The actual returns on a risky investment can be very different
from expected returns; the greater the variation, the greater the risk. When
looking at equity, we tend to use measures of risk based upon return variance.
While the discussion of risk and return models elsewhere in this site will look
at the different models that attempt to do this in far more detail, there are
some basic points on which these models agree. The first is that risk in an
investment has to perceived through the eyes of the marginal investor in that
investment, and this marginal investor is assumed to be well diversified across
multiple investments. Therefore, the risk in an investment that should determine
discount rates is the *non-diversifiable or market risk* of that investment. The second is that the expected
return on any investment can be obtained starting with the expected return on a
riskless investment, and adding to it a premium to reflect the amount of market
risk in that investment. This expected return yields the cost of equity.

            The
*cost of capital* can be obtained by
taking an average of the cost of equity, estimated as above, and the after-tax
cost of borrowing, based upon default risk, and weighting by the proportions
used by each. We will argue that the weights used, when valuing an on-going
business, should be based upon the market values of debt and equity. While
there are some analysts who use book value weights, doing so violates a basic principle
of valuation, which is that at a fair value[if !supportFootnotes[3]endif](#_ftn3) , one should be indifferent between buying and selling
an asset.

#### b. Expected Cash Flows

            In
the strictest sense, the only cash flow an equity investor gets out of a
publicly traded firm is the dividend; models that use the dividends as cash
flows are called *dividend discount models*.
A broader definition of cash flows to equity would be the cash flows left over
after the cash flow claims of non-equity investors in the firm have been met
(interest and principal payments to debt holders and preferred dividends) and
after enough of these cash flows has been reinvested into the firm to sustain
the projected growth in cash flows. This is the free cash flow to equity
(FCFE), and models that use these cash flows are called *FCFE discount
models*.

            The
cashflow to the firm is the cumulated cash flow to all claimholders in the
firm. One way to obtain this cashflow is to add the free cash flows to equity to
the cash flows to lenders (debt) and preferred stockholders. A far simpler way
of obtaining the same number is to estimate the cash flows prior to debt  and preferred dividend payments, by
subtracting from the after-tax operating income the net investment needs to
sustain growth. This cash flow is called the free cash flow to the firm (FCFF)
and the models that use these cash flows are called *FCFF models*.

#### c. Expected Growth

            It
is while estimating the expected growth in cash flows in the future that analysts
confront uncertainty most directly. There are three generic ways of estimating
growth. One is to look at a company�s past and use the historical growth rate
posted by that company. The peril is that past growth may provide little
indication of future growth. The second is to obtain estimates of growth from
more informed sources. For some analysts, this translates into using the
estimates provided by a company�s management whereas for others it takes the
form of using consensus estimates of growth made by others who follow the firm.
The bias associated with both these sources should raise questions about the
resulting valuations.

We will promote a
third way, where the expected growth rate is tied to two variables that are
determined by the firm being valued - how much of the earnings are reinvested
back into the firm and how well those earnings are reinvested. In the equity
valuation model, this expected growth rate is a product of the retention ratio,
i.e. the proportion of net income not paid out to stockholders, and the return
on equity on the projects taken with that money. In the firm valuation model,
the expected growth rate is a product of the reinvestment rate, which is the
proportion of after-tax operating income that goes into net new investments and
the return on capital earned on these investments.  The advantages of using these fundamental growth rates are
two fold. The first is that the resulting valuations will be internally
consistent and companies that are assumed to have high growth are required to
pay for the growth with more reinvestment. The second is that it lays the
foundation for considering how firms can make themselves more valuable to their
investors.

### DCF Valuation: Pluses and Minuses

            To
true believers, discounted cash flow valuation is the only way to approach
valuation, but the benefits may be more nuanced that they are willing to admit.
On the plus side, discounted cash flow valuation, done right, requires analysts
to understand the businesses that they are valuing and ask searching questions
about the sustainability of cash flows and risk. Discounted cash flow valuation
is tailor made for those who buy into the Warren Buffett adage that what we are
buying are not stocks but the underlying businesses. In addition, discounted
cash flow valuations is inherently contrarian in the sense that it forces
analysts to look for the fundamentals that drive value rather than what market
perceptions are. Consequently, if stock prices rise (fall) disproportionately
relative to the underlying earnings and cash flows, discounted cash flows
models are likely to find stocks to be over valued (under valued).

            There
are, however, limitations with discounted cash flow valuation. In the hands of
sloppy analysts, discounted cash flow valuations can be manipulated to generate
estimates of value that have no relationship to intrinsic value. We also need
substantially more information to value a company with discounted cash flow
models, since we have to estimate cashflows, growth rates and discount rates.
Finally, discounted cash flow models may very well find every stock in a sector
or even a market to be over valued, if market perceptions have run ahead of
fundamentals. For portfolio managers and equity research analysts, who are
required to find equities to buy even in the most over valued markets, this
creates a conundrum. They can go with their discounted cash flow valuations and
conclude that everything is overvalued, which may put them out of business, or
they can find an alternate approach that is more sensitive to market moods. It
should come as no surprise that many choose the latter.

## Relative Valuation

While the focus in classrooms and academic
discussions remains on discounted cash flow valuation, the reality is that most
assets are valued on a relative basis. In relative valuation, we value an asset
by looking at how the market prices similar assets. Thus, when determining what
to pay for a house, we look at what similar houses in the neighborhood sold for
rather than doing an intrinsic valuation. Extending this analogy to stocks,
investors often decide whether a stock is cheap or expensive by comparing its
pricing to that of similar stocks (usually in its peer group). In this section,
we will consider the basis for relative valuation, ways in which it can be used
and its advantages and disadvantages.

### Basis for approach

In
relative valuation, the value of an asset is derived from the pricing of
'comparable' assets, standardized using a common variable. Included in this
description are two key components of relative valuation. The first is the
notion of comparable or similar assets. From a valuation standpoint,
this would imply assets with similar cash flows, risk and growth potential. In
practice, it is usually taken to mean other companies that are in the same
business as the company being valued. The other is a standardized price.
After all, the price per share of a company is in some sense arbitrary since it
is a function of the number of shares outstanding; a two for one stock split
would halve the price. Dividing the price or market value by some measure that
is related to that value will yield a standardized price. When valuing stocks,
this essentially translates into using multiples where we divide the market
value by earnings, book value or revenues to arrive at an estimate of
standardized value. We can then compare these numbers across companies.

The
simplest and most direct applications of relative valuations are with real
assets where it is easy to find similar assets or even identical ones. The
asking price for a Mickey Mantle rookie baseball card or a 1965 Ford Mustang is
relatively easy to estimate given that there are other Mickey Mantle cards and
1965 Ford Mustangs out there and that the prices at which they have been bought
and sold can be obtained. With equity valuation, relative valuation becomes
more complicated by two realities. The first is the absence of similar assets,
requiring us to stretch the definition of comparable to include companies that
are different from the one that we are valuing. After all, what company in the
world is remotely similar to Microsoft or GE? The other is that different ways
of standardizing prices (different multiples) can yield different values for
the same company.

Harking
back to our earlier discussion of discounted cash flow valuation, we argued
that discounted cash flow valuation was a search (albeit unfulfilled) for
intrinsic value. In relative valuation, we have given up on estimating
intrinsic value and essentially put our trust in markets getting it right, at
least on average.

### Variations on Relative Valuation

            In
relative valuation, the value of an asset is based upon how similar assets are
priced. In practice, there are three variations on relative valuation, with the
differences primarily in how we define comparable firms and control for
differences across firms:

a. *Direct comparison*: In this approach, analysts try to find one or two
companies that look almost exactly like the company they are trying to value
and estimate the value based upon how these �similar� companies are priced. The
key part in this analysis is identifying these similar companies and getting
their market values.

*b*. *Peer Group Average*: In
the second, analysts compare how their company is priced (using a multiple)
with how the peer group is priced (using the average for that multiple). Thus,
a stock is considered cheap if it trade at 12 times earnings and the average
price earnings ratio for the sector is 15. Implicit in this approach is the
assumption that while companies may vary widely across a sector, the average
for the sector is representative for a typical company.

*c. Peer group average adjusted
for differences*: Recognizing that there can
be wide differences between the company being valued and other companies in the
comparable firm group, analysts sometimes try to control for differences
between companies. In many cases, the control is subjective: a company with
higher expected growth than the industry will trade at a higher multiple of
earnings than the industry average but how much higher is left unspecified. In
a few cases, analysts explicitly try to control for differences between
companies by either adjusting the multiple being used or by using statistical
techniques. As an example of the former, consider PEG ratios. These ratios are
computed by dividing PE ratios by expected growth rates, thus controlling (at
least in theory) for differences in growth and allowing analysts to compare
companies with different growth rates. For statistical controls, we can use a
multiple regression where we can regress the multiple that we are using against
the fundamentals that we believe cause that multiple to vary across companies.
The resulting regression can be used to estimate the value of an individual
company. In fact, we will argue that statistical techniques are powerful enough
to allow us to expand the comparable firm sample to include the entire market.

### Applicability of multiples and limitations

The allure of multiples is that they are simple and
easy to relate to. They can be used to obtain estimates of value quickly for
firms and assets, and are particularly useful when there are a large number of
comparable firms being traded on financial markets, and the market is, on
average, pricing these firms correctly. In fact, relative valuation is tailor
made for analysts and portfolio managers who not only have to find under valued
equities in any market, no matter how overvalued, but also get judged on a
relative basis. An analyst who picks stocks based upon their PE ratios,
relative to the sectors they operate in, will always find under valued stocks
in any market; if entire sectors are over valued and his stocks decline, he
will still look good on a relative basis since his stocks will decline less
than comparable stocks (assuming the relative valuation is right).

By
the same token, they are also easy to misuse and manipulate, especially when
comparable firms are used. Given that no two firms are exactly similar in terms
of risk and growth, the definition of 'comparable' firms is a subjective one.
Consequently, a biased analyst can choose a group of comparable firms to
confirm his or her biases about a firm's value. While this potential for bias
exists with discounted cashflow valuation as well, the analyst in DCF valuation
is forced to be much more explicit about the assumptions which determine the
final value. With multiples, these assumptions are often left unstated.

The
other problem with using multiples based upon comparable firms is that it
builds in errors (over valuation or under valuation) that the market might be
making in valuing these firms.  If,
for instance, we find a company to be under valued because it trades at 15
times earnings and comparable companies trade at 25 times earnings, we may
still lose on the investment if the entire sector is over valued. In relative
valuation, all that we can claim is that a stock looks cheap or expensive
relative to the group we compared it to, rather than make an absolute judgment
about value. Ultimately, relative valuation judgments depend upon how well we
have picked the comparable companies and how how good a job the market has done
in pricing them.

## Contingent Claim Valuation

            There
is little in either discounted cashflow or relative valuation that can be
considered new and revolutionary. In recent years, though, analysts have
increasingly used option-pricing models, developed to value listed options, to
value assets, businesses and equity stakes in businesses.  These applications are often
categorized loosely as real options, but they have to be used with caution.

### Basis for Approach

A contingent claim or option is an asset which pays
off only under certain contingencies - if the value of the underlying asset
exceeds a pre-specified value for a call option, or is less than a
pre-specified value for a put option. Much work has been done in the last few
decades in developing models that value options, and these option-pricing
models can be used to value any assets that have option-like features.

            Figure
1.2 illustrates the payoffs on call and put options as a function of the value
of the underlying asset:

*Figure 1.2: Payoffs on Options as a Function of the
Underlying Asset's Value*

    if !vml![](valintro_files/image015.png)endif

             

An option can be valued as a
function of the following variables - the current value and the variance in
value of the underlying asset, the strike price and the time to expiration of
the option and the riskless interest rate. This was first established by Black
and Scholes (1972) and has been extended and refined subsequently in numerous
variants.[if !supportFootnotes[4]endif](#_ftn4) While the Black-Scholes option-pricing model ignored
dividends and assumed that options would not be exercised early, it can be
modified to allow for both. A discrete-time variant, the Binomial
option-pricing model, has also been developed to price options.

            An
asset can be valued as a call option if the payoffs on it are a function of the
value of an underlying asset; if that value exceeds a pre-specified level, the
asset is worth the difference; if not, it is worth nothing. It can be valued as
a put option if it gains value as the value of the underlying asset drops below
a pre- specified level, and if it is worth nothing when the underlying asset's
value exceeds that specified level. There are many assets that generally are
not viewed as options but still share several option characteristics. A patent
can be analyzed as a call option on a product, with the investment outlay
needed to get the project going considered the strike price and the patent life
becoming the life of the option. An undeveloped oil reserve or gold mine
provides its owner with a call option to develop the reserve or mine, if oil or
gold prices increase.

            The
essence of the real options argument is that discounted cash flow models
understate the value of assets with option characteristics. The understatement
occurs because DCF models value assets based upon a set of expected cash flows
and do not fully consider the possibility that firms can learn from real time
developments and respond to that learning. For example, an oil company can
observe what the oil price is each year and adjust its development of new
reserves and production in existing reserves accordingly rather than be locked
into a fixed production schedule. 
As a result, there should be an option premium added on to the
discounted cash flow value of the oil reserves. It is this premium on value
that makes real options so alluring and so potentially dangerous.

### Applicability and Limitations

            Using
option-pricing models in valuation does have its advantages. First, there are
some assets that cannot be valued with conventional valuation models because
their value derives almost entirely from their option characteristics. For
example, a biotechnology firm with a single promising patent for a blockbuster
cancer drug wending its way through the FDA approval process cannot be easily
valued using discounted cash flow or relative valuation models. It can,
however, be valued as an option. The same can be said about equity in a money
losing company with substantial debt; most investors buying this stock are
buying it for the same reasons they buy deep out-of-the-money options. Second,
option-pricing models do yield more realistic estimates of value for assets
where there is a significant benefit obtained from learning and flexibility.
Discounted cash flow models will understate the values of natural resource
companies, where the observed price of the natural resource is a key factor in
decision making. Third, option-pricing models do highlight a very important
aspect of risk. While risk is considered almost always in negative terms in
discounted cash flow and relative valuation (with higher risk reducing value),
the value of options increases as volatility increases. For some assets, at
least, risk can be an ally and can be exploited to generate additional value.

            This
is not to suggest that using real options models is an unalloyed good. Using
real options arguments to justify paying premiums on discounted cash flow
valuations, when the options argument does not hold, can result in overpayment.
While we do not disagree with the notion that firms can learn by observing what
happens over time, this learning has value only if it has some degree of exclusivity.
We will argue that it is usually inappropriate to attach an option premium to
value if the learning is not exclusive and competitors can adapt their behavior
as well.  There are also
limitations in using option pricing models to value long-term options on
non-traded assets. The assumptions made about constant variance and dividend
yields, which are not seriously contested for short term options, are much more
difficult to defend when options have long lifetimes. When the underlying asset
is not traded, the inputs for the value of the underlying asset and the
variance in that value cannot be extracted from financial markets and have to
be estimated. Thus the final values obtained from these applications of option
pricing models have much more estimation error associated with them than the
values obtained in their more standard applications (to value short term traded
options).

# The Role of Valuation

Valuation is useful in a wide range of tasks. The
role it plays, however, is different in different arenas. The following section
lays out the relevance of valuation in portfolio management, in acquisition
analysis and in corporate finance.

## 1. Portfolio Management

            The
role that valuation plays in portfolio management is determined in large part
by the investment philosophy of the investor. Valuation plays a minimal role in
portfolio management for a passive investor, whereas it plays a larger role for
an active investor. Even among active investors, the nature and the role of
valuation is different for different types of active investment. Market timers
use valuation much less than investors who pick stocks, and the focus is on
market valuation rather than on firm-specific valuation. Among security
selectors, valuation plays a central role in portfolio management for
fundamental analysts, and a peripheral role for technical analysts.

            The
following sub-section describes, in broad terms, different investment
philosophies and the roles played by valuation in each one.

*1. Fundamental Analysts:*  The
underlying theme in fundamental analysis is that the true value of the firm can
be related to its financial characteristics -- its growth prospects, risk
profile and cashflows. Any deviation from this true value is a sign that a
stock is under or overvalued. It is a long-term investment strategy, and the
assumptions underlying it are that:

if !supportLists(a)  
endifThe relationship between value and the underlying financial
factors can be measured.

if !supportLists(b) 
endifThe relationship is stable over time.

if !supportLists(c)  
endifDeviations from the relationship are corrected in a reasonable
time period.

Fundamental analysts include both
value and growth investors. The key difference between the two is in where the
valuation focus lies. Reverting back to our break down of assets in figure 1.1,
value investors are primarily interested in assets in place and acquiring them
at less than their true value. Growth investors, on the other hand, are far
more focused on valuing growth assets and buying those assets at a discount.
While valuation is the central focus in fundamental analysis, some analysts use
discounted cashflow models to value firms, while others use multiples and
comparable firms. Since investors using this approach hold a large number of
'undervalued' stocks in their portfolios, their hope is that, on average, these
portfolios will do better than the market.

*2. Activist Investors:* 
Activist investors take positions in firms that have a reputation for
poor management and then use their equity holdings to push for change in the
way the company is run. Their focus is not so much on what the company is worth
today but what its value would be if it were managed well. Investors like Carl
Icahn, Michael Price and Kirk Kerkorian have prided themselves on their
capacity to not only pinpoint badly managed firms but to also create enough
pressure to get management to change its ways. How can valuation skills help in
this pursuit? To begin with, these investors have to ensure that there is
additional value that can be generated by changing management. In other words,
they have to separate how much of a firm�s poor stock price performance has to
do with bad management and how much of it is a function of external factors;
the former are fixable but the latter are not. They then have to consider the
effects of changing management on value; this will require an understanding of
how value will change as a firm changes its investment, financing and dividend
policies. As a consequence, they have to not only know the businesses that the
firm operates in but also have an understanding of the interplay between
corporate finance decisions and value. Activist investors generally concentrate
on a few businesses they understand well, and attempt to acquire undervalued
firms. Often, they wield influence on the management of these firms and can
change financial and investment policy. 

*3. Chartists:* 
Chartists believe that prices are driven as much by investor psychology
as by any underlying financial variables. The information available from
trading measures -- price movements, trading volume and short sales -- gives an
indication of investor psychology and future price movements. The assumptions
here are that prices move in predictable patterns, that there are not enough
marginal investors taking advantage of these patterns to eliminate them, and
that the average investor in the market is driven more by emotion than by
rational analysis.  While valuation
does not play much of a role in charting, there are ways in which an
enterprising chartist can incorporate it into analysis. For instance, valuation
can be used to determine support and resistance lines[if !supportFootnotes[5]endif](#_ftn5) on price charts.

*4. Information Traders:*  Prices
move on information about the firm. Information traders attempt to trade in
advance of new information or shortly after it is revealed to financial
markets.  The underlying assumption
is that these traders can anticipate information announcements and gauge the
market reaction to them better than the average investor in the market. For an
information trader, the focus is on the relationship between information and
changes in value, rather than on value, per se. Thus an information trader may
buy an 'overvalued' firm if he believes that the next information announcement
is going to cause the price to go up, because it contains better than expected
news. If there is a relationship between how undervalued or overvalued a
company is, and how its stock price reacts to new information, then valuation
could play a role in investing for an information trader.

*5. Market Timers:* Market
timers note, with some legitimacy, that the payoff to calling turns in markets
is much greater than the returns from stock picking. They argue that it is
easier to predict market movements than to select stocks and that these
predictions can be based upon factors that are observable. While valuation of
individual stocks may not be of much direct use to a market timer, market
timing strategies can use valuation in one of at least two ways:

if !supportLists(a)  
endifThe overall market itself can be valued and compared to the
current level.

if !supportLists(b) 
endifValuation models can be used to value a large number of  stocks, and the results from the
cross-section can be used to determine whether the market is over or under
valued. For example, as the number of stocks that are overvalued, using the
valuation model, increases relative to the number that are undervalued, there
may be reason to believe that the market is overvalued.

*6. Efficient Marketers:* 
Efficient marketers believe that the market price at any point in time represents
the best estimate of the true value of the firm, and that any attempt to
exploit perceived market efficiencies will cost more than it will make in
excess profits. They assume that markets aggregate information quickly and
accurately, that marginal investors promptly exploit any inefficiencies and
that any inefficiencies in the market are caused by friction, such as
transactions costs, and cannot exploited. For efficient marketers, valuation is
a useful exercise to determine why a stock sells for the price that it does.
Since the underlying assumption is that the market price is the best estimate
of the true value of the company, the objective becomes determining what
assumptions about growth and risk are implied in this market price, rather than
on finding under or over valued firms.                     

## 2. Valuation in Acquisition Analysis

            Valuation
should play a central part of acquisition analysis. The bidding firm or
individual has to decide on a fair value for the target firm before making a
bid, and the target firm has to determine a reasonable value for itself before
deciding to accept or reject the offer.

            There
are special factors to consider in takeover valuation. First, there is synergy,
the increase in value that many managers foresee as occurring after mergers
because the combined firm is able to accomplish things that the individual
firms could not.  The effects of
synergy on the combined value of the two firms (target plus bidding firm) have
to be considered before a decision is made on the bid. Second, the value of
control, which measures the effects on value of changing management and
restructuring the target firm, will have to be taken into account in deciding
on a fair price.  This is of
particular concern in hostile takeovers.

            As
we noted earlier, there is a significant problem with bias in takeover
valuations. Target firms may be over-optimistic in estimating value, especially
when the takeover is hostile, and they are trying to convince their
stockholders that the offer price is too low. Similarly, if the bidding firm
has decided, for strategic reasons, to do an acquisition, there may be strong
pressure on the analyst to come up with an estimate of value that backs up the
acquisition.

## 3. Valuation in Corporate Finance

 There
is a role for valuation at every stage of a firm�s life cycle. For small
private businesses thinking about expanding, valuation plays a key role when
they approach venture capital and private equity investors for more capital.
The share of a firm that a venture capitalist will demand in exchange for a
capital infusion will depend upon the value she estimates for the firm.  As the companies get larger and decide
to go public, valuations determine the prices at which they are offered to the
market in the public offering. Once established, decisions on where to invest,
how much to borrow and how much to return to the owners will be all decisions
that are affected by valuation. If the objective in corporate finance is to
maximize firm value[if !supportFootnotes[6]endif](#_ftn6) , the relationship between financial decisions,
corporate strategy and firm value has to be delineated. 

As a final note,
value enhancement has become the mantra of management consultants and CEOs who
want to keep stockholders happy, and doing it right requires an understanding
of the levers of value. In fact, many consulting firms have come up with their
own measures of value (EVA and CFROI, for instance) that they contend
facilitate value enhancement.

## 4. Valuation for Legal and Tax Purposes

            Mundane
though it may seem, most valuations, especially of private companies, are done
for legal or tax reasons. A partnership has to be valued, whenever a new
partner is taken on or an old one retires, and businesses that are jointly
owned have to be valued when the owners decide to break up. Businesses have to
be valued for estate tax purposes when the owner dies, and for divorce
proceedings when couples break up. While the principles of valuation may not be
different when valuing a business for legal proceedings, the objective often
becomes providing a valuation that the court will accept rather than the
�right� valuation.

# Conclusion

            Valuation
plays a key role in many areas of finance -- in corporate finance, in mergers
and acquisitions and in portfolio management. The models presented will provide
a range of tools that analysts in each of these areas will find of use, but the
cautionary note sounded in this introduction bears repeating. Valuation is not
an objective exercise, and any preconceptions and biases that an analyst brings
to the process will find their way into the value.

### **if !supportEmptyParas endif**

if !supportFootnotes  
 

---

 endif

[if !supportFootnotes[1]endif](#_ftnref1) There
are approximately five times as many buy recommendations issued by analysts on
Wall Street as there are sell recommendations.

[if !supportFootnotes[2]endif](#_ftnref2) The
income from cash is riskless and should be discounted back at a riskless rate.
Instead, analysts use risk adjusted discount rates (costs of equity or capital)
to discount the cash income, thus resulting in a discount on face value. When
analysts use multiples, they often will use the average PE ratio at which peer
group companies as the multiple for cash income.

[if !supportFootnotes[3]endif](#_ftnref3) When
book value weights are used, the costs of capital tend to be much lower for
many U.S. firms, since book equity is lower than market equity. This then pushes
up the value for these firms. While this may make it attractive to the sellers
of these firms, very few buyers would be willing to pay this price for the
firm, since it would require that the debt that they use in their financing
will have to be based upon the book value, often requiring tripling or
quadrupling the dollar debt in the firm.

[if !supportFootnotes[4]endif](#_ftnref4)
Black, F. and M. Scholes, 1972, *The Valuation of Option Contracts and a Test
of Market Efficiency*, Journal of Finance,
v27, 399-417.

[if !supportFootnotes[5]endif](#_ftnref5) On a
chart, the support line usually refers to a lower bound below which prices are
unlikely to move and the resistance line refers to the upper bound above which
prices are unlikely to venture. While these levels are usually estimated using
past prices, the range of values obtained from a valuation model can be used to
determine these levels, i.e., the maximum value will become the resistance
level and the minimum value will become the support line.

[if !supportFootnotes[6]endif](#_ftnref6) Most
corporate financial theory is constructed on this premise.
