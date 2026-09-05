---
title: "Estimating Equity Risk Premiums"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/riskfreerates.htm
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
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:14.0pt;
font-family:Times;
mso-font-kerning:0pt;
font-weight:normal;}
h2
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
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
text-indent:-27.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:4;
tab-stops:99.0pt 171.0pt 256.5pt;
font-size:12.0pt;
font-family:Times;
color:black;
font-weight:normal;
font-style:italic;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
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
text-indent:-27.0pt;
mso-pagination:widow-orphan;
tab-stops:1.0in 2.0in 225.0pt;
font-size:12.0pt;
font-family:Times;
color:black;}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-footer:url(":riskfreerates\_files:header.htm") ef1;
mso-footer:url(":riskfreerates\_files:header.htm") f1;
mso-paper-source:0;}
div.Section1
{page:Section1;}
/\* List Definitions \*/
@list l0
{mso-list-id:1;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l0:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l1
{mso-list-id:2;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l1:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l2
{mso-list-id:3;
mso-list-type:simple;
mso-list-template-ids:0;}
@list l2:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l3
{mso-list-id:4;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l3:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l4
{mso-list-id:5;
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
{mso-list-id:6;
mso-list-template-ids:0;}
@list l5:level1
{mso-level-start-at:61;
mso-level-text:%1;
mso-level-tab-stop:34.0pt;
mso-level-number-position:left;
margin-left:34.0pt;
text-indent:-34.0pt;}
@list l5:level2
{mso-level-start-at:36;
mso-level-text:"%1\.%2";
mso-level-tab-stop:34.0pt;
mso-level-number-position:left;
margin-left:34.0pt;
text-indent:-34.0pt;}
@list l5:level3
{mso-level-text:"%1\.%2\.%3";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
margin-left:.5in;
text-indent:-.5in;}
@list l5:level4
{mso-level-text:"%1\.%2\.%3\.%4";
mso-level-tab-stop:.5in;
mso-level-number-position:left;
margin-left:.5in;
text-indent:-.5in;}
@list l5:level5
{mso-level-text:"%1\.%2\.%3\.%4\.%5";
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.75in;}
@list l5:level6
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6";
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.75in;}
@list l5:level7
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7";
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-1.0in;}
@list l5:level8
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7\.%8";
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
margin-left:1.0in;
text-indent:-1.0in;}
@list l5:level9
{mso-level-text:"%1\.%2\.%3\.%4\.%5\.%6\.%7\.%8\.%9";
mso-level-tab-stop:1.25in;
mso-level-number-position:left;
margin-left:1.25in;
text-indent:-1.25in;}
@list l6
{mso-list-id:7;
mso-list-type:simple;
mso-list-template-ids:66569;}
@list l6:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l7
{mso-list-id:8;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l7:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->

if !supportEmptyParas endif

Estimating Risk free Rates

            Most
risk and return models in finance start off with an asset that is defined as
risk free, and use the expected return on that asset as the risk free rate. The
expected returns on risky investments are then measured relative to the risk
free rate, with the risk creating an expected risk premium that is added on to
the risk free rate. But what makes an asset risk free? And what do we do when
we cannot find such an asset? These are the questions that we will deal with in
this paper.

## What is  a risk free asset?

To
understand what makes an asset risk free, let us go back to how risk is
measured in finance. Investors who buys assets have a return that they
expect to make over the time horizon that they will hold the asset. The actual
returns that they make over this holding period may by very different from
the expected returns, and this is where the risk comes in. Risk in finance is
viewed in terms of the variance in actual returns around the expected return.
For an investment to be risk free in this environment, then, the actual returns
should always be equal to the expected return.

To
illustrate, consider an investor with a 1-year time horizon buying a 1-year
Treasury bill (or any other default-free one-year bond) with a 5% expected
return. At the end of the 1-year holding period, the actual return that this
investor would have on this investment will always be 5%, which is equal to the
expected return. The return distribution for this investment is shown in Figure
1.

if !vml![](riskfreerates_files/image003.gif)endif  
if !supportEmptyParas endif

  

This investment
is risk free because there is no variance around the expected return.

## Requirements for an Asset to be Risk free

            Under
what conditions will the actual returns on an investment be equal to the
expected returns? In our view, there are two basic conditions that have to be
met. The first is that there can be no default risk. Essentially, this
rules out any security issued by a private firm, since even the largest and safest
firms have some measure of default risk. The only securities that have a chance
of being risk free are government securities, not because governments are
better run than corporations, but because they control the printing of
currency. At least in nominal terms, they should be able to fulfil their
promises. Even this assumption, straightforward though it might seem, does not
always hold up, especially when governments refuse to honor claims made by
previous regimes and when they borrow in currencies other than their own.

            There
is a second condition that riskless securities need to fulfil that is often
forgotten. For an investment to have an actual return equal to its expected
return, there can be no reinvestment risk. To illustrate this point,
assume that you are trying to estimate the expected return over a five-year
period, and that you want a risk free rate. A six-month treasury bill rate,
while default free, will not be risk free, because there is the reinvestment
risk of not knowing what the treasury bill rate will be in six months. Even a
5-year treasury bond is not risk free, since the coupons on the bond will be
reinvested at rates that cannot be predicted today. The risk free rate for a
five-year time horizon has to be the expected return on a default-free
(government) five-year zero coupon bond. This clearly has painful implications
for anyone doing corporate finance or valuation, where expected returns often
have to be estimated for periods ranging from one to ten years. A purist's view
of risk free rates would then require different risk free rates for each
period, and different expected returns.

            As
a practical compromise, however, it is worth noting that the present value
effect of using year-specific risk free rates tends to be small for most well-behaved[if !supportFootnotes[1]endif](#_ftn1)
term structures. In these cases, we could use a duration matching strategy,
where the duration of the default-free security used as the risk free asset is
matched up to the duration[if !supportFootnotes[2]endif](#_ftn2)
of the cash flows in the analysis. If, however, there are very large
differences, in either direction, between short term and long term rates, it
does pay to stick with year-specific risk free rates in computing expected
returns.

## The Practical Implications when a Default-free Entity  exists

            In
most developed markets, where the government can be viewed as a default free
entity, at least when it comes to borrowing in the local currency, the
implications are simple. When doing investment analysis on longer term projects
or valuation, the risk free rate should be the long term government bond rate.
If the analysis is shorter term, the short term government security rate can be
used as the risk free rate. The choice of a risk free rate also has
implications for how risk premiums are estimated. If, as is often the case,
historical risk premiums are used, where the excess return earned by stocks
over and above a government security rate over a past period is used as the
risk premium, the government security chosen has to be same one as that used
for the risk free rate. Thus, the historical risk premium used in the US should
be the excess return earned by stocks over treasury bonds, and not treasury
bills, for purposes of long term analysis.

## Cash Flows and Risk free Rates: The Consistency Principle

            The
risk free rate used to come up with expected returns should be measured
consistently with the cash flows are measured. Thus, if cash flows are
estimated in nominal US dollar terms, the risk free rate will be the US
treasury bond rate. This also implies that it is not where a project or firm is
domiciled that determines the choice of a risk free rate, but the currency in
which the cash flows on the project or firm are estimated. Thus, Nestle can be
valued using cash flows estimated in Swiss Francs, discounted back at an
expected return estimated using a Swiss long term government bond rate, or it
can be valued in British pounds, with both the cash flows and the risk free
rate being British pound rates. Given that the same project or firm can be
valued in different currencies, will the final results always be consistent? If
we assume purchasing power parity, then differences in interest rates reflect
differences in expected inflation. Both the cash flows and the discount rate
are affected by expected inflation; thus, a low discount rate arising from a
low risk free rate will be exactly offset by a decline in expected nominal
growth rates for cash flows, and the value will remain unchanged.

            If
the difference in interest rates across two currencies does not adequately
reflect the difference in expected inflation in these currencies, the values
obtained using the different currencies can be different. In particular,
projects and assets will be valued more highly when the currency used is the
one with low interest rates relative to inflation. The risk, however, is that
the interest rates will have to rise at some point to correct for this
divergence, at which point the values will also converge.

## Real versus Nominal Risk free Rates

            Under
conditions of high and unstable inflation, valuation is often done in real
terms. Effectively, this means that cash flows are estimated using real growth
rates and without allowing for the growth that comes from price inflation. To
be consistent, the discount rates used in these cases have to be real discount
rates. To get a real expected rate of return, we need to start with a real risk
free rate. While government bills and bonds offer returns that are risk free in
nominal terms, they are not risk free in real terms, since expected inflation
can be volatile.  The standard
approach of subtracting an expected inflation rate from the nominal interest
rate to arrive at a real risk free rate provides at best an estimate of the real
risk free rate.

            Until
recently, there were few traded default-free securities that could be used to estimate
real risk free rates, but the introduction of inflation-indexed treasuries has
filled this void. An inflation-indexed treasury security does not offer a
guaranteed nominal return to buyers, but instead provides a guaranteed real
return. Thus, an inflation-indexed treasury that offers a 3% real return, will
yield approximately 7% in nominal terms if inflation is 4% and only 5% in
nominal terms if inflation is only 2%. 

            The
only problem is that real valuations are seldom called for or done in the United
States, which has stable and low expected inflation. The markets where we would
most need to do real valuations, unfortunately, are markets without
inflation-indexed default-free securities. The real risk free rates in these
markets can be estimated by using one of two arguments:

if !supportLists�     
endifThe first argument is that as long as capital can flow freely
to those economies with the highest real returns, there can be no differences
in real risk free rates across markets. Using this argument, the real risk free
rate for the United States, estimated from the inflation-indexed treasury, can
be used as the real risk free rate in any market.

if !supportLists�     
endifThe second argument applies if there are frictions and
constraints in capital flowing across markets. In that case, the expected real
return on a economy, in the long term, should be equal to the expected real
growth rate, again in the long term, of that  economy, for equilibrium.  Thus, the real risk free rate for a mature economy like
Germany should be much lower than the real risk free rate for a economy with
greater growth potential, such as Hungary.

## Risk free Rates when there is no Default-free Entity

            Our
discussion, hitherto,  has been
predicated on the assumption that governments do not default, at least on local
borrowing. There are many emerging market economies where this assumption might
not be viewed as reasonable. Governments in these markets are perceived as
capable of defaulting even on local borrowing. When this is coupled with the
fact that many governments do not borrow long term locally, there are scenarios
where obtaining a local risk free rate, especially for the long term, becomes
difficult. Under these cases, there are compromises that give us reasonable
estimates of the risk free rate:

if !supportLists�     
endifLook at the largest and safest firms in that market,
and use the rate that they pay on their long term borrowings in the local
currency as a base. Given that these firms, in spite of their size and
stability, still have default risk, I would use a rate that is marginally lower[if !supportFootnotes[3]endif](#_ftn3)
than the corporate borrowing rate.

if !supportLists�     
endifIf there are long term dollar-denominated forward
contracts on the currency, you can use interest rate parity and the dollar
borrowing rate to arrive at an estimate of the local borrowing rate.

Forward Ratet
FC, $ = Spot RateFC,$ (1+ Interest RateFC)t/
(1+ Interest Rate$)t

where,

Forward
RateFC,$ = Forward rate for foreign currency units/$

Spot
RateFC,$ = Spot rate for foreign currency units/$

Interest
RateFC = Interest rate in foreign currency

Interest
Rate$ = Interest rate in US dollars

For
instance, if the current spot rate is 38.10 Thai Baht per US dollar, the
ten-year forward rate is 61.36 Baht per dollar, and the current ten-year US
treasury bond rate is 5%, the ten-year Thai risk free rate (in nominal Baht)
can be estimated as follows:

if !supportLists61.36    endif=
38.10 (1+ Interest RateThai Baht)10/ 1.0510

Solving
for the Thai interest rate yields a ten-year risk free rate of 10.12%. The
biggest limitation of this approach, however, is that forward rates are
difficult to come by for periods beyond a year[if !supportFootnotes[4]endif](#_ftn4)
for many of the emerging markets, where we would be most interested in using
them.

## Summing Up

            The
risk free rate is the starting point for all expected return models. For an
asset to be risk free, it has to meet two conditions �

(1) there can be
no risk of default associated with its cash flows and

(2) there can be
no reinvestment risk

Using these
criteria, the appropriate risk free rate to use to obtain expected returns should
be a default-free (government) zero coupon rate that is matched up to when the
cash flow or flows that are being discounted occur. In practice, however, it is
usually appropriate to match up the duration of the risk free asset to the
duration of the cash flows being analyzed. In corporate finance and valuation,
this will lead us towards long term government bond rates as risk free rates.

            It
is also important that the risk free rate be consistent with the cash flows
being discounted. In particular, the currency in which the risk free rate is
denominated and whether it is a real or nominal risk free rate should be
determined by the currency in which the cash flows are estimated and whether
the estimation is done in real or nominal terms.

if !supportEmptyParas endif

if !supportEmptyParas endif

if !supportFootnotes  

---

endif

[if !supportFootnotes[1]endif](#_ftnref1) By well
behaved term structures, I would include a normal upward sloping yield curve,
where long term rates are at most 2-3% higher than short term rates.

[if !supportFootnotes[2]endif](#_ftnref2) In
investment analysis, where we look at projects, these durations are usually
between 3 and 10 years. In valuation, the durations tend to be much longer,
since firms are assumed to have infinite lives. The duration in these cases is
often well in excess of ten years, and increase with the expected growth
potential of the firm.

[if !supportFootnotes[3]endif](#_ftnref3) I would use
0.50% less than the corporate borrowing rate as my risk free rate. This is
roughly a AA default spread in the US.

[if !supportFootnotes[4]endif](#_ftnref4) In cases
where only a one-year forward rate exists, an approximation for the long term
rate can be obtained by first backing out the one-year local currency borrowing
rate, taking the spread over the one-year treasury bill rate, and then adding
this spread on to the long term treasury bond rate. For instance, with a
one-year forward rate of 39.95 on the Thai bond, we obtain a one-year Thai baht
riskless rate of 9.04% (given a one-year T.Bill rate of 4%). Adding the spread
of 5.04% to the ten-year treasury bond rate of 5% provides a ten-year Thai Baht
rate of 10.04%.
