---
title: "Option Pricing"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/problems/optprob.htm
---

Option Pricing

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
margin:0in;
margin-bottom:.0001pt;
text-align:center;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:14.0pt;
font-family:Times;
mso-font-kerning:0pt;}
h2
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
tab-stops:325.0pt 390.0pt;
font-size:12.0pt;
font-family:Times;
color:black;}
h3
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:3;
tab-stops:65.0pt 130.0pt 195.0pt 260.0pt 325.0pt 390.0pt;
font-size:14.0pt;
font-family:Times;
color:black;}
h6
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:18.0pt;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:6;
font-size:11.0pt;
font-family:Times;}
p.MsoFootnoteText, li.MsoFootnoteText, div.MsoFootnoteText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
{margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
{margin:0in;
margin-bottom:.0001pt;
mso-pagination:widow-orphan;
tab-stops:center 3.0in right 6.0in;
font-size:12.0pt;
font-family:Times;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
{margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
font-size:14.0pt;
font-family:"Times New Roman";
font-weight:bold;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin-top:12.0pt;
margin-right:0in;
margin-bottom:0in;
margin-left:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:200%;
mso-pagination:widow-orphan;
mso-list:skip;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyText2, li.MsoBodyText2, div.MsoBodyText2
{margin:0in;
margin-bottom:.0001pt;
line-height:18.0pt;
mso-pagination:widow-orphan;
font-size:11.0pt;
font-family:Times;}
p.Questions0, li.Questions0, div.Questions0
{mso-style-name:Questions;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:9.0pt;
margin-bottom:.0001pt;
line-height:18.0pt;
mso-pagination:widow-orphan;
font-size:11.0pt;
font-family:Times;}
p.Question0, li.Question0, div.Question0
{mso-style-name:Question;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:9.0pt;
margin-bottom:.0001pt;
text-align:justify;
line-height:18.0pt;
mso-pagination:widow-orphan;
tab-stops:9.0pt;
font-size:11.0pt;
font-family:Times;}
p.singlespacing0, li.singlespacing0, div.singlespacing0
{mso-style-name:"single spacing";
mso-style-parent:"";
margin:0in;
margin-bottom:.0001pt;
line-height:12.0pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"Times New Roman";}
@page Section1
{size:8.5in 11.0in;
margin:1.0in 135.35pt 3.0in 135.35pt;
mso-header-margin:.5in;
mso-footer-margin:2.5in;
mso-title-page:yes;
mso-header:url(":eqprob3\_files:header.htm") h1;
mso-footer:url(":eqprob3\_files:header.htm") f1;
mso-paper-source:0;}
div.Section1
{page:Section1;}
@page Section2
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-header:url(":eqprob3\_files:header.htm") h1;
mso-footer:url(":eqprob3\_files:header.htm") f1;
mso-paper-source:0;}
div.Section2
{page:Section2;}
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
{mso-list-id:251790468;
mso-list-template-ids:299039938;}
@list l1:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l1:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l2
{mso-list-id:541525837;
mso-list-type:hybrid;
mso-list-template-ids:695503612 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l2:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l2:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l2:level3
{mso-level-number-format:roman-lower;
mso-level-tab-stop:1.5in;
mso-level-number-position:right;
text-indent:-9.0pt;}
@list l3
{mso-list-id:549732415;
mso-list-type:hybrid;
mso-list-template-ids:1747776560 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l3:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l4
{mso-list-id:873537170;
mso-list-template-ids:-531323304;}
@list l4:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l5
{mso-list-id:902956065;
mso-list-type:hybrid;
mso-list-template-ids:678709830 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l5:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l6
{mso-list-id:1129710706;
mso-list-template-ids:2130606162;}
@list l6:level1
{mso-level-start-at:2;
mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l6:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.75in;
mso-level-number-position:left;
margin-left:.75in;
text-indent:-.25in;}
@list l7
{mso-list-id:1465586995;
mso-list-type:hybrid;
mso-list-template-ids:-376911378 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l7:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:none;
mso-level-number-position:left;
mso-level-legacy:yes;
mso-level-legacy-indent:.25in;
mso-level-legacy-space:0in;
margin-left:.25in;
text-indent:-.25in;
font-family:Symbol;}
@list l8
{mso-list-id:1706639720;
mso-list-type:hybrid;
mso-list-template-ids:-1137161414 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l8:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l9
{mso-list-id:1708140796;
mso-list-type:hybrid;
mso-list-template-ids:1549273556 -1 -1 -1 -1 -1 -1 -1 -1 -1;}
@list l9:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l9:level2
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:1.0in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l0:level1 lfo8
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

Option Pricing

1. The following are prices of options
traded on Microsoft Corporation, which pays no dividends.

                                           Call                              Put

                                    K=85   K=90               K=85   K=90

1 month                       2.75     1.00                 4.50     7.50    

3 month                       4.00     2.75                 5.75     9.00

6 month                       7.75     6.00                 8.00     12.00

The stock is trading at $83, and the
annualized riskless rate is 3.8%. The standard deviation in ln stock prices
(based upon historical data) is 30%.

a. Estimate
the value of a three-month call, with a strike price of 85.

b. Using the
inputs from the Black-Scholes model, specify how you would replicate this call.

c. What is
the implied standard deviation in this call?

d. Assume
now that you buy a call with a strike price of 85 and sell a call with a strike
price of 90. Draw the payoff diagram on this position.

e. Using put-call
parity, estimate the value of a three-month put with a strike price of 85.

2. You are trying to value three-month
call and put options on Merck, with a strike price of 30. The stock is trading
at $28.75, and expects to pay a quarterly dividend per share of $0.28 in two
months. The annualized riskless interest rate is 3.6%, and the standard
deviation in ln stock prices is 20%.

a. Estimate
the value of the call and put options, using the Black-Scholes.

b. What
effect does the expected dividend payment have on call values? on put values?
Why?

3. There is the possibility that the
options on Merck, described above, could be exercised early.

a. Use the
pseudo-American call option technique to determine whether this will affect the
value of the call.

b. Why does
the possibility of early exercise exist? What types of options are most likely
to be exercised early?

4. You have been provided the following
information on a three-month call:

            S
= 95              K=90               t=0.25             r=0.04

            N(d1)
= 0.5750           N(d2)
= 0.4500                      

a. If you
wanted to replicate buying this call, how much money would you need to borrow?

b. If you wanted to
replicate buying this call, how many shares of stock would you need to buy?

5. Go Video, a manufacturer of video
recorders, was trading at $4 per share in May 1994. There were 11 million
shares outstanding. At the same time, it had 550,000 one-year warrants
outstanding, with a strike price of $4.25. The stock has had a standard
deviation (in ln stock prices) of 60%. The stock does not pay a dividend. The
riskless rate is 5%.

a. Estimate
the value of the warrants, ignoring dilution.

b. Estimate
the value of the warrants, allowing for dilution.

c. Why does
dilution reduce the value of the warrants.

6. You are trying to value a long term
call option on the NYSE Composite Index, expiring in five years, with a strike
price of 275. The index is currently at 250, and the annualized standard
deviation in stock prices is 15%. The average dividend yield on the index is
3%, and is expected to remain unchanged over the next five years. The five-year
treasury bond rate is 5%.

a. Estimate
the value of the long term call option.

b. Estimate
the value of a put option, with the same parameters.

c. What are
the implicit assumptions you are making when you use the Black-Scholes model to
value this option? Which of these assumptions are likely to be violated? What
are the consequences for your valuation?

7. 
A new security on AT&T will entitle the investor to all dividends on
AT&T over the next three years, limit upside potential to 20%, but also
provide downside protection below 10%. AT&T stock is trading at $50, and
three-year call and put options are traded on the exchange at the following
prices            

                                             Call
Options                  Put
Options

                   K                    1
year     3 year           1
year          3
year

                   45                   $8.69      $13.34           $1.99           $3.55

                   50                   $5.86      $10.89           $3.92           $5.40

                   55                   $3.78      $8.82             $6.59           $7.63

                   60                   $2.35      $7.11             $9.92         $10.23

How much would you be
willing to pay for this security?

# The Option to Delay

1. A company is considering delaying a project with
   after-tax cash flows of $25 million but costs $300 million to take (the
   life of the project is 20 years and the cost of capital is 16%). A
   simulation of the cash flows leads you to conclude that the standard
   deviation in the present value of cash inflows is 20%. If you can acquire
   the rights to the project for the next ten years, what are the inputs for
   the option pricing model? (The six-month T.Bill rate is 8%, the ten year
   bond-rate is 12% and the 20-year bond rate is 14%.)
2. You are examining the financial
   viability of investing in some abandoned copper mines in Chile, which
   still have significant copper deposits in them. A geologist survey
   suggests that there might be 10 million pounds of copper in the mines
   still and that the cost of opening up the mines will be $3 million (in
   present value dollars). The capacity output rate is 400,000 pounds a year
   and the price of copper is expected to increase 4% a year. The Chilean
   Government is willing to grant a twenty-five year lease on the mine. The
   average production cost is expected to be 40 cents a pound and the current
   price per pound of copper is 85 cents. (The production cost is expected to
   grow 3% a year, once initiated.) The annualized standard deviation in
   copper prices is 25% and the twenty-five year bond rate is 7%.

a. Estimate the value of
the mine using traditional capital budgeting techniques.

b. Estimate the value of
the mine based upon an option pricing model.

c. How would you explain
the difference between the two values?

3. You have been asked to analyze the
   value of an oil company with substantial oil reserves. The estimated
   reserves amount to 10,000,000 barrels and the estimated present value of
   the development cost for each barrel is $12. The current price of oil is
   $20 per barrel and the average production cost is estimated to be $6 per
   barrel. The company has the rights to these reserves for the next twenty
   years and the twenty-year bond rate is 7%.  The company also proposes to extract 4% of its reserves
   each year to meet cashflow needs. The annualized standard deviation in the
   price of the oil is 20%. What is the value of this oil company?
4. You are analyzing a capital
   budgeting project. The project is expected to have a PV of cash inflows of
   $250 million and will cost $200 million (in present value dollars) to take
   on. You have done a simulation of the project cashflows and the simulation
   yields a variance in present value of cash inflows of 0.04.  You have the rights to this
   project for the next five years, during which period you have to pay $12.5
   million a year to retain the project rights. The five-year treasury bond
   rate is 8%.

if !supportListsa.     endifWhat is the value of
project, based upon traditional NPV?

if !supportListsb.     endifWhat is the value of the
project as an option?

if !supportListsc.     endifWhy are the two values
different? What factor or factors determine the magnitude of this difference?

5. Cyclops Inc, a high technology
   company specializing in state-of-the-art visual technology, is considering
   going public. While the company has no revenues or profits yet on its
   products, it has a ten-year patent to a product that will enable contact
   lens users to get no-maintenance lens that will last for years. While the
   product is technically viable, it is exorbitantly expensive to manufacture
   and the potential market for it will be relatively small initially. (A
   cash flow analysis of the project suggests that the present value of the
   cash inflows on the project, if adopted now, would be $250 million, while
   the cost of the project will be $500 million.) The technology is rapidly
   evolving and a simulation of alternative scenarios yields a wide range of
   present values, with an annualized standard deviation of 60%. To move
   towards this adoption, the company will have to continue to invest $10
   million a year in research. The ten-year bond rate is 6%.

if !supportListsa.     endifEstimate the value of
this company.

if !supportListsb.     endifHow sensitive is this
value estimate to the variance in project cash flows? What broader lessons
would you draw from this analysis?

**The
Option to Expand and Abandon**

if !supportLists1.    
endifNBC has the
rights to televise the Winter Olympics in 2 years and is trying to estimate the
value of these rights for possible sale to another network. NBC expects it to
cost $40 million (in present value terms) to televise the Olympics and based
upon current assessments expects to have a Nielsen rating[if !supportFootnotes[1]endif](#_ftn1) of 15 for the games. Each rating point
is expected to yield net revenue of $2 million to NBC (in present value terms).
There is substantial variability in this estimate and the standard deviation in
the expected net revenues is 30%. The riskless rate is 5%.

a. What is the net present value of these
rights, based upon current assessments?  

b. Estimate the value of these rights for
sale to another network.                 

if !supportLists2.    
endifYou are
analyzing Skates Inc., a firm that manufactures skateboards. The firm is
currently unlevered and has a cost of equity of 12%. You estimate that Skates
would have a cost of capital of 11% at its optimal debt ratio of 40%. The
management, however, insists that it will not borrow the money because of the
value of maintaining financial flexibility and they have provided you with the
following information.

if !supportLists·     
endifOver the
last 10 years, reinvestments (net capital expenditures + working capital
investments) have amounted to 10% of firm value, on an annual basis. The
standard deviation in this reinvestment has been 0.30.

if !supportLists·     
endifThe firm
has traditionally used only internal funding (net income + depreciation) to
meet these needs and these have amounted to 6% of firm value.

if !supportLists·     
endifIn the most
recent year, the firm earned $180 million in net income on a book value of
equity of $1 billion and it expects to earn these excess returns on new
investments in the future.

if !supportLists·     
endifThe
riskless rate is 5%.

if !supportListsa.    
endifEstimate
the value of financial flexibility as a percent of firm value, on an annual
basis.

if !supportListsb.    
endifBased upon
part a, would you recommend that Skates use its excess debt capacity?

if !supportLists3.    
endifDisney is
considering entering into a joint venture to build condominiums in Vail,
Colorado, with a local real estate developer. The development is expected to
cost $1 billion overall and, based on Disney’s estimate of the cashflows,
generate $900 million in present value cash flows. Disney will have a 40% share
of the joint venture (requiring it to put up $400 million of the initial
investment and entitling it to 40% of the cashflows) but it will have the right
to sell its share of the venture back to the developer for $300 million anytime
over the next 5 years. (The project life is 25 years)

if !supportListsa.    
endifIf the
standard deviation in real estate values in Vail is 30% and the riskless rate
is 5%, estimate the value of the abandonment option to Disney.

if !supportListsb.    
endifWould you
advice Disney to enter into the joint venture?

if !supportListsc.    
endifIf you were
advising the developer, how much would he need to generate in present value
cashflows from the investment to make this a good investment?

if !supportLists4.    
endifQuality
Wireless is considering making an investment in China. While it knows that the
investment will cost $1 billion and generate only $800 million in cashflows (in
present value terms), the proponents of expansion are arguing that the
potential market is huge and that Quality should go ahead with its investment.

if !supportListsa.    
endifUnder what
conditions will the expansion potential have option value?

if !supportListsb.    
endifAssume now
that there is an option value to expansion that exactly offsets the negative
net present value on the initial investment. If the cost of the subsequent
expansion in 5 years is $2.5 billion, what is your current estimate of the
present value of the cash flows from expansion? (You can assume that the
standard deviation in the present value of the cashflows is 25% and that the
riskless rate is 6%.)

if !supportLists5.    
endifReliable
Machinery Inc. is considering expanding its operations in Thailand. The initial
analysis of the projects yields the following results.

if !supportLists·     
endifThe project
is expected to generate $85 million in after-tax cash flows every year for the
next 10 years.

if !supportLists·     
endifThe initial
investment in the project is expected to be $750 million.

if !supportLists·     
endifThe cost of
capital for the project is 12%.

If the project generates much higher cash
flows than anticipated, you will have the exclusive right for the next 10 years
(from a manufacturing license) to expand operations into the rest of South East
Asia. A current analysis suggests the following about the expansion
opportunity.

if !supportLists·     
endifThe
expansion will cost $2 billion (in current dollars).

if !supportLists·     
endifThe
expansion is expected to generate $150 million in after tax cash flows each
year for 15 years. There is substantial uncertainty about these cash flows and
the standard deviation in the present value is 40%.

if !supportLists·     
endifThe cost of
capital for this investment is expected to be 12% as well. The riskfree rate is
6.5%.

a. Estimate the net present value of the
initial investment.

b. Estimate the value of the expansion
option.

# Equity in a Deeply Troubled Firm as an Option

1. Designate the following statements as
true or false.

a. Equity can be viewed as an option
because equity investors have limited liability (limited to their equity
investment in the firm).                            

b. Equity investors will sometimes take
bad projects (with negative net present value) because they can add to the
value of the firm.                          

c. Investing in a good project (with
positive NPV) -- which is less risky than the average risk of the firm -- can
negatively impact equity investors.   

d. The value of equity in a firm is an
increasing function of the duration of the debt in the firm (i.e., equity will
be more valuable in a firm with longer term debt than an otherwise similar firm
with short term debt).

e. In a merger in which two risky firms
merge and do not borrow more money, equity can become less valuable because
existing debt will become less risky.

2. XYZ Corporation has $500 million in
zero-coupon debt outstanding, due in five years. The firm had earnings before
interest and taxes of $40 million in the most recent year (the tax rate is
40%). These earnings are expected to grow 5% a year in perpetuity and the firm
paid no dividends. The firm had a return on capital of 12% and a cost of
capital of 10%. The annualized standard deviation in firm values of comparable
firms is 12.5%. The five-year bond rate is 5%.

a. Estimate
the value of the firm.

b. Estimate
the value of equity, using an option pricing model.

c. Estimate
the market value of debt and the appropriate interest rate on the debt.

3. McCaw Cellular Communications reported
earnings before interest and taxes of $850 million in 1993, with a depreciation
allowance of $400 million and capital expenditures of $ 550 million in that
year; the working capital requirements were negligible. The earnings before
interest and taxes and net cap ex are expected to grow 20% a year for the next
five years. The cost of capital is 10% and the return on capital is expected to
15% in perpetuity after year 5; the growth rate in perpetuity is 5%. The firm
has $10 billion in debt outstanding with the following characteristics.

*Duration                     Debt*

            1
year                          $2
billion

            2
years                        $4
billion

            5
years                        $4
billion

The annualized standard deviation in the
firm's stock price is 35%, while the annualized standard deviation in the
traded bonds is 15%. The correlation between stock and bond prices has been 0.5
and the average debt ratio over the last few years has been 60%. The three-year
bond rate is 5% and the tax rate is 40%.

a. Estimate the value of
the firm.

b. Estimate the value of
the equity.

c. The stock was trading
at $60 and there were 210 million shares outstanding in January 1994. Estimate
the implied standard deviation in firm value.

d. Estimate the market
value of the debt.

4. You have been asked to analyze the
value of equity in a company that has the following features.

if !supportLists·     
endifThe
earnings before interest and taxes is $25 million and the corporate tax rate is
40%.

if !supportLists·     
endifThe
earnings are expected to grow 4% a year in perpetuity and the return on capital
is 10%. The cost of capital of comparable firms is 9%.

if !supportLists·     
endifThe firm
has two types of debt outstanding - 2-year zero-coupon bonds with a face value
of $250 million and bank debt with ten years to maturity with a face value of
$250 million (The duration of this debt is 4 years.).

if !supportLists·     
endifThe firm is
in two businesses - food processing and auto repair – of equal size. The
average standard deviation in firm value for firms in food processing is 25%,
whereas the standard deviation for firms in auto repair is 40%. The correlation
between the businesses is 0.5.

if !supportLists·     
endifThe
riskless rate is 7%.

Use the option pricing model to value
equity as an option.

5. You are valuing the equity in a firm
with $800 million (face value) in debt with an average duration of 6 years and
assets with an estimated value of $400 million. The standard deviation in asset
value is 30%. With these inputs (and a riskless rate of 6%) we obtain the
following values (approximately) for d1 and d2.

            d1
= - 0.15      d2
= - 0.90

Estimate the default spread (over and
above the riskfree rate) that you would charge for the debt in this firm.

  

**Solutions
to Option Pricing Problems**

###### Question 1

A. The values of the option parameters are as follows:

S = $83

K = $85

t = 0.25

r = 3.80%

Variance = 0.09

Value of call = $4.42

B.
To replicate this call, you would have to:

Buy 0.4919 Shares of Stock (this is
N(d1) from the model)

and

Borrow K e-rt N(d2) =
85 exp-(0.038)(0.25) (0.4324) = $36.40

C.
At an implied variance of 0.075, the call has a
value of approximately $4.00 (the market price).

Implied Standard Deviation =
√0.075 = 0.2739

D.

if !vml
![](eqprob3_files/image003.gif)
endif

if !supportEmptyParas endif

E.

Value of Three-month Put = C - S + Ke-rt = $4.42 - $83 + 85 exp-(0.038)(0.25) = $5.62

###### Question 2

A.        S
= $28.75

            K
= $30

            t
= 0.25

            r
= 3.60%

            s2 = 0.04

            PV
of Expected Dividends = $0.28/(1.036)2/12 = $0.28

            Value
of Call = $0.64

B. The payment of a dividend reduces the expected stock
price, and hence reduces the value of calls and increases the value of puts.

###### Question 3

A. First value the three-month call, as above:

            Value
of Call = $0.64

Then, value a call to the first (and only) dividend
payment,

            S
= $28.75

            K
= $30

            t
= 2/12

            r
= 3.60%

            s2 = 0.04

            y
= 0 (since it assumes exercise before the dividend payment)

            Value
of Call = $0.51

Since the value of the three-month call is higher,
there is no anticipated exercise.

B. If the dividend payment is large enough, it may pay to
exercise the call just before the ex-dividend day (before the stock price
drops) rather than wait until expiration. This early exercise is more likely
for call options:

            (a)
the larger the dividend on the stock, and

            (b)
the closer the option is to expiration.

###### Question 4

A. You would need to borrow Ke-rt N(d2) = 90 exp(-0.04)(0.25) (0.4500) = $40.10

B. You would need to buy 0.575 shares of stock.

###### Question 5

A.        S= $4.00

            K
= $4.25

            r
= 5%

            t
= 1

            Variance
= 0.36

            Value
of Warrant = $0.93

B. Adjusted Stock Price = (Stock Price \* Number of Shares
Outstanding) + (Warrant price \* Number of Warrants Outstanding)/(Number of
Shares+Number of Warrants)

            =
($4.00 \* 11,000,000 + $0.93 \* 550,000)/(11,550,000) = $3.85

(To avoid the circular reasoning problem, the price
from the no-dilution case is used.)

Adjusted Exercise Price = $4.25

r = 5%

t = 1

Variance = 0.36

Value of Warrant = $0.80

(If you are using a spreadsheet with iterations turned
on, and are feeding the option prices back to calculate the adjusted stock
price, the value of the warrants is still $0.80.)

C. Dilution increases the number of shares outstanding.
For any given value of equity, each share is worth less.

###### Question 6

A.        S = 250

            K
= 275

            t
=  5

            r
= 5%

s2 = (0.15)2

            y
= 0.03

            Value
of call = $29.09

B. Value of put with same parameters = $28.09

C.

(1) The variance will be unchanged for the life of the
option. This is likely to be violated because stock price variances do change
substantially over time.

(2) There will be no early exercise. This is
reasonable and is unlikely to be violated.

(3) Any deviations from the option value will be
arbitraged away.

While there are plenty of
arbitrageurs eager to exploit deviations from true value, arbitraging an index
is clearly more difficult to do than arbitraging an individual stock.

###### Question 7

New Security    =
AT & T stock - Call (K=60) + Put (K=45)

                        =
$50 - $7.11 + $3.55 = $46.44

The
call with a strike price of $60 is sold, eliminating upside potential above
$60.

The put with a strike
price of $45 is bought, providing downside protection.

# if !supportEmptyParas endif

  

**Solutions: The Option to Delay**

if !supportEmptyParas endif

**Question 1**

S = PV of $25 million a year
for 20 years at 16% = $148.22 million

K = Cost of Taking Project = $300 million

t = 10 years

Standard Deviation = 20%

r = 12%

y = Dividend Yield = 1/ Project Life = 10%

**Question 2**

a. PV of Inflows         
= 400,000  \* 0.85 \* (1
- 1.04^25/1.07^25)/(.07
- .04) -400,000  \* 0.40  \* (1 - 1.03^25/1.07^25)/(.07 - .03)
= $3,309,756

Fixed Costs associated with opening

            =
-3,000,000

NPV = 3,309,756 -3,000,000 = $309,756

if !supportEmptyParas endif

b.         S
= 3,309,756

            K
= 3,000,000

            t
= 25

            r
= 7%

s = 0.25

            y
= 1/25 = 4%

Value of the Call Option = $828,674

if !supportEmptyParas endif

c. The latter considers the option characteristics of
owning the mine, i.e., that copper prices may go up, and that the mine-owner
will be more likely to develop the mine at higher copper prices.

if !supportEmptyParas endif

**Question 3**

**if !supportEmptyParas endif**

Current Value of Developed Reserve = 10,000,000 \* ($20
- $6) = $140,000,000

Exercise Price = Cost of Developing Reserve =
$120,000,000

t = 20 years

r = 7%

s = 20%

y = 4% (Alternatively, you can use 1/20 or 5% as your
cost of delay)

Value of Call (Natural Resource Reserve) = $37,360,435

**if !supportEmptyParas endif**

**Question 4**

**if !supportEmptyParas endif**

a. NPV of Project = $250 - $200 = $50 million

if !supportEmptyParas endif

b. The option has the following characteristics:

S = 250

K = 200

r = 8%

t = 5

Variance = 0.04

Dividend Yield = 12.5/250 = 5%

Value of Call (Project Rights) = $68.68

if !supportEmptyParas endif

c. The latter captures the value of delaying the
project. The difference between the two values will increase as the variance in
the project cash flows increases.

**if !supportEmptyParas endif**

**Question 5**

a. S = PV of Cash Inflows on Project = 250

K = Cost of Taking Project = 500

t = 10 years

r = 6%

s = 0.6

y = 10/250 = 4%

Value of Call (Product Patent) = $95 million

if !supportEmptyParas endif

b. It is an increasing function of the variance in
project cash flows. This analysis suggests that the rights to products in
technologically volatile areas are likely to be worth a great deal, even though
the products may not be viable now.

  

**Solutions to
the Option to Expand**

**if !supportEmptyParas endif**

**Question 1**

a. Net present value of the project = $ 30 - $ 40 =
- $ 10 million       

b. Inputs                                                                                             

S = Present Value of Net
Revenues =      $
30 million                       

K = Cost of televising the
Olympics =     $ 40
million                       

t = Time until Olympics =                        2
years                               

r = Riskless rate =                                    5%                                     

Variance in value =                                   0.09                                   

y = Cost of delay =                                  0                                        

d1=               -0.2302         N(d1)
=         0.4090                               

d2 =              -0.6545         N(d2)
=         0.2564                               

Value of the Rights = 30 (0.409) - 40 exp
(-0.05)(2) (.2564) = 2.99

c. Probability that rights will be profitable =
0.2564 - 0.4090

if !supportEmptyParas endif

## Question 2

a.

S = Expected
reinvestment needs as percent of firm value = 10%

K = Reinvestment
needs that can be met without excess debt capacity = 6%

T = 1 year

Standard deviation
in reinvestment needs = 0.30

The option pricing
value with these inputs is 4.32%. If we assume that the current excess returns
(18% - 12%) continue in perpetuity, the value of flexibility is

Value of
flexibility (on an annual basis) = 4.32% \* .06/.12 = 2.16%

b.

Based upon part a,
would you recommend that Skates use its excess debt capacity?

The value of
flexibility exceeds what the firm would save by moving to its optimal (only
1%). The firm should not use its excess debt capacity.

if !supportEmptyParas endif

**if !supportEmptyParas endif**

**Question 3**

if !supportListsa.     endifValue of abandonment option

S = PV of cashflows from development = $ 900 million\* 0.4 =
$ 360 million

K = Abandonment value = $ 300 million

T = 5 years

Riskless rate = 5%

Standard deviation = 40%

Value of abandonment option = $ 63.51 million

if !supportListsb.     endifThe net present value of this project to
Disney is -$ 40 million.

Net present value = -400 + 360 = -40 million

The value of the abandonment option is greater than the
negative net present value. I would advice Disney to make the investment.

if !supportListsc.     endifIf you were the developer, you would need
to make a net present value equal to at least $63.51 million to cover the cost
of the abandonment option.

PV of cash flows to developer = (63.51) + .6 (1000) = $
663.51 million

**Question 4**

if !supportListsa.     endifFor the expansion potential to have
option value, Quality Wireless has to have exclusive rights to expand.

if !supportListsb.     endifNet present value of initial investment =
- $ 200 million

S = PV of cashflows from expansion (currently) = ?

K = $2500 million

T = 5 years

Standard deviation in firm value = 25%

Riskless rate = 5%

Setting up the option value = $ 200 million and solving for
S, we get

S = $ 1511 million

(Sorry. The only way to get there is by trial and error. An
approximate answer would have been sufficient)

**Question 5**

if !supportListsa.     endifNet present value of initial investment =
-750 + 85 (PV of annuity, 10 years, 12%)

                                                                        =
- $269.73 million

if !supportListsb.     endifValue of expansion option

S = 150 (PV of annuity, 12%, 15 years) = $1,021.63 million

K = Cost of expansion = $ 2,000 million

Riskless rate = 6.5%

Standard deviation in value = 40%

Life of the option = 10 years

Value of expansion option = $ 477.28 million

  

**Solutions to Equity as an option in a deeply
troubled firm**

### Problem 1

a. True. Equity investors cannot lose more than their
equity investment.

b. False. They can make equity more valuable, not the
firm.

c. True. It transfers wealth to the bondholders.

d. True. This is the equivalent of the life of the
option.

e. True. There is a transfer of wealth to bondholders.

**Problem 2**

a.         Reinvestment
rate = g/ROC = 5%/12% = 41.67%

Value of the firm =
40(1.05)(1-.5)(1-0.4)/(.10-.05) = $294 million

if !supportEmptyParas endif

b.

The value of the equity is computed as a call option
on the value of the firm, using the call option pricing formula, 

if !vml
![](eqprob3_files/image006.gif)
endif

, where 

if !vml
![](eqprob3_files/image009.gif)
endif

, d2 = d1 - sÖt. 

S = $294

K = $500

t = 5 years

r = 5%

s = 0.125

The equity or call option value can be written as 294
N(-0.8657) -500 e^-0.25 N(-1.1452).  Since N(d1) = 0.1933; N(d2) = 0.1261,
the option value is $7.75 million.

Value of Call (Equity) = $7.75 million

if !supportEmptyParas endif

c. Value of Debt = $294 - $7.75 = $286.25 million

Appropriate Interest Rate = (500/286.25)1/5 - 1 = 11.80%

**if !supportEmptyParas endif**

**Problem 3**

if !supportListsa.     endifValue
of firm

Current free cashflow to firm
= $ 850\* (1-.4) – (550 – 400) = $ 700 million

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Year* | *EBIT (1-t)* | *Net cap ex* | *FCFF* | *PV* |
| 1 | $612.00 | $180.00 | $432.00 | $392.73 |
| 2 | $734.40 | $216.00 | $518.40 | $428.43 |
| 3 | $881.28 | $259.20 | $622.08 | $467.38 |
| 4 | $1,057.54 | $311.04 | $746.50 | $509.87 |
| 5 | $1,269.04 | $373.25 | $895.80 | $556.22 |
| Terminal | $1,332.50 | $444.17 | $888.33 | if !supportEmptyParas endif |

I used a reinvestment rate of
33.33% (5/15) in the terminal year.

Terminal value =
888.33/(.10-.05) = $ 17,766

Value of firm = 392.73 +
428.43 + 467.38 + 509.87 + 556.22 + 17766.60/1.15 = $13,386.28
million

if !supportListsb.     endifValue
of equity as an option

S = 13386.28

K = 10000.00

T = Weighted duration of debt = 3 years

Riskless rate = 5%

Variance in firm value = (.35)(.4)^2+(.15)(.6)^2+
2 (.35)(.15)(.5)(.4)(.6) = .20 = 0.0403

Value of equity = $ 4958 million

if !supportListsc.     endifIf
the market value of equity = 30 \* 210 = $ 6300 million

Trial and error yields an
implied standard deviation of 46.53%.

if !supportListsd.     endifValue
of debt = Firm value – Value of equity

= 13386 – 4958 = $8,428
million

if !supportEmptyParas endif

**Problem 4**

 Value of
firm = EBIT (1-t) (1- Reinvestment rate) (1+g)/(r – g)

            =
25 (1-.4) (1 – 4/10) (1.04)/(.09-.04) = $ 187.20 million

Face value of debt = $ 250 + $ 250 = $ 500 million

Average duration of debt = (2+4)/2 = 3 years

Standard deviation in firm value = 0.252(.5)^2+0.42(.5)^2+
2\*.25\*.4\*.5\*(.5)^2 = 28.39%

Riskless rate = 7%

Value of equity as an option = $ 3.30 million

**if !supportEmptyParas endif**

**Problem
5**                                                                                                                                

d1
= -0.15                                                       N(d1)
=0.4404                                                                        

d2=
-0.90                                                        N(d2)
=0.1841                                                                        

                                                                                                                                                                       

Value
of Equity = 400 (.4404) - 800 exp (-.06\*6) (.1841) =$ 73.41                                                             

Value
of Debt = 400 - 73.41=      
$ 326.59                                                                                                              

Interest
rate on debt = (800/326.59)^(1/6) - 1 = 16.08%                                                                            

Default
spread on debt = 16.08% - 6% = 10.08%

if !supportEmptyParas endif

if !supportFootnotes  

---

endif

[if !supportFootnotes[1]endif](#_ftnref1)
There are 99.4 million households in the United States. Each rating point
represents 1% of roughly 994,000 households.
