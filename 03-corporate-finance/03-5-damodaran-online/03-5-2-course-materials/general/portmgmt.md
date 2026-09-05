---
title: "An Introduction to Portfolio Management"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/background/portmgmt.htm
---

An Introduction to Portfolio Management  
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
text-align:justify;
line-height:150%;
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
font-size:12.0pt;
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
font-family:Times;
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
mso-outline-level:3;
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
tab-stops:27.0pt .5in 4.75in;
border:none;
mso-border-bottom-alt:solid windowtext .75pt;
padding:0in;
mso-padding-alt:0in 0in 0in 0in;
font-size:14.0pt;
font-family:Times;
font-weight:normal;}
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
mso-outline-level:6;
font-size:12.0pt;
font-family:Times;
font-weight:normal;
font-style:italic;}
p.MsoHeading7, li.MsoHeading7, div.MsoHeading7
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:3.0pt;
margin-left:0in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
mso-outline-level:7;
font-size:10.0pt;
font-family:Times;}
p.MsoHeading8, li.MsoHeading8, div.MsoHeading8
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:200%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:8;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
p.MsoHeading9, li.MsoHeading9, div.MsoHeading9
{mso-style-next:Normal;
margin-top:0in;
margin-right:0in;
margin-bottom:0in;
margin-left:20.25pt;
margin-bottom:.0001pt;
text-align:center;
text-indent:-20.25pt;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:9;
tab-stops:2.0in 274.5pt;
font-size:12.0pt;
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
p.MsoCaption, li.MsoCaption, div.MsoCaption
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;
font-style:italic;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;
vertical-align:super;}
span.MsoEndnoteReference
{vertical-align:super;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
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
p.MsoBodyTextIndent2, li.MsoBodyTextIndent2, div.MsoBodyTextIndent2
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.5in;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
p.MsoBodyTextIndent3, li.MsoBodyTextIndent3, div.MsoBodyTextIndent3
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
text-indent:.25in;
line-height:150%;
mso-pagination:widow-orphan;
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
p.MsoPlainText, li.MsoPlainText, div.MsoPlainText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;}
table.MsoNormalTable
{mso-style-parent:"";
font-size:10.0pt;
font-family:"Times New Roman";}
p.Times12, li.Times12, div.Times12
{mso-style-name:Times12;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
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
mso-even-header:url(":portmgmt\_files:header.htm") eh1;
mso-header:url(":portmgmt\_files:header.htm") h1;
mso-paper-source:0;}
div.Section1
{page:Section1;}
@page Section2
{size:11.0in 8.5in;
mso-page-orientation:landscape;
margin:1.25in 1.0in 1.25in 1.0in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":portmgmt\_files:header.htm") eh1;
mso-header:url(":portmgmt\_files:header.htm") h1;
mso-paper-source:0;}
div.Section2
{page:Section2;}
@page Section3
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":portmgmt\_files:header.htm") eh1;
mso-header:url(":portmgmt\_files:header.htm") h1;
mso-paper-source:0;}
div.Section3
{page:Section3;}
@page Section4
{size:11.0in 8.5in;
mso-page-orientation:landscape;
margin:1.25in 1.0in 1.25in 1.0in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":portmgmt\_files:header.htm") eh1;
mso-header:url(":portmgmt\_files:header.htm") h1;
mso-paper-source:0;}
div.Section4
{page:Section4;}
@page Section5
{size:8.5in 11.0in;
margin:1.0in 1.25in 1.0in 1.25in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-even-header:url(":portmgmt\_files:header.htm") eh1;
mso-header:url(":portmgmt\_files:header.htm") h1;
mso-paper-source:0;}
div.Section5
{page:Section5;}
/\* List Definitions \*/
@list l0
{mso-list-id:85922948;
mso-list-type:hybrid;
mso-list-template-ids:626281976 67698703 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l1
{mso-list-id:991060819;
mso-list-type:hybrid;
mso-list-template-ids:1169464086 1639433 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l1:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l2
{mso-list-id:1464999632;
mso-list-type:hybrid;
mso-list-template-ids:-1821712278 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l2:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l3
{mso-list-id:1518999644;
mso-list-type:hybrid;
mso-list-template-ids:-1088671752 -1976809004 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l3:level1
{mso-level-start-at:0;
mso-level-number-format:bullet;
mso-level-text:-;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:"Times New Roman";}
@list l4
{mso-list-id:2119837917;
mso-list-type:hybrid;
mso-list-template-ids:-1646108862 67698703 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l4:level1
{mso-level-number-format:alpha-lower;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
.style1 {color: #000000}
.style2 {color: #0066cc}
-->
   

[![](../Budimage/titlesm.gif)](../home.htm)

What
is Portfolio Management?

# 

We all dream of beating the market
and being super investors and spend an inordinate amount of time and resources
in this endeavor. Consequently, we are easy prey for the magic bullets and the
secret formulae offered by eager salespeople pushing their wares. In spite of
our best efforts, most of us fail in our attempts to be more than �average�
investors. Nonetheless, we keep trying, hoping that we can be more like the
investing legends – another Warren Buffett or Peter Lynch. We read the
words written by and about successful investors, hoping to find in them the key
to their stock-picking abilities, so that we can replicate them and become
wealthy quickly.

In our search, though, we are
whipsawed by contradictions and anomalies. In one corner of the investment
townsquare, stands one advisor, yelling to us to buy businesses with solid cash
flows and liquid assets because that�s what worked for Buffett. In another
corner, another investment expert cautions us that this approach worked only in
the old world, and that in the new world of technology, we have to bet on
companies with solid growth prospects. In yet another corner, stands a silver
tongued salesperson with vivid charts and presents you with evidence of his
capacity to get you in and out of markets at exactly the right times. It is not
surprising that facing this cacophony of claims and counterclaims that we end
up more confused than ever.

In this introduction, we present
the argument that to be successful with any investment strategy, you have to
begin with an investment philosophy that is consistent at its core and which
matches not only the markets you choose to invest in but your individual
characteristics. In other words, the key to success in investing may lie not in
knowing what makes Peter Lynch successful but in finding out more about
yourself.

# What is an investment philosophy?

            An
investment philosophy is a coherent way of thinking about markets, how they
work (and sometimes do not) and the types of mistakes that you believe
consistently underlie investor behavior. Why do we need to make assumptions
about investor mistakes? As we will argue, most investment strategies are
designed to take advantage of errors made by some or all investors in pricing
stocks. Those mistakes themselves are driven by far more basic assumptions
about human behavior. To provide an illustration, the rational or irrational
tendency of human beings to join crowds can result in price momentum –
stocks that have gone up the most in the recent past are more likely to go up
in the near future. Let us consider, therefore, the ingredients of an
investment philosophy.

## Human Frailty

            Underlying
all investment philosophies is a view about human behavior. In fact, one
weakness of conventional finance and valuation has been the short shrift given
to human behavior. It is not that we (in conventional finance) assume that all
investors are rational, but that we assume that irrationalities are random and
cancel out. Thus, for every investor who tends to follow the crowd too much (a
momentum investor), we assume an investor who goes in the opposite direction (a
contrarian), and that their push and pull in prices will ultimately result in a
rational price. While this may, in fact, be a reasonable assumption for the
very long term, it may not be a realistic one for the short term.

Academics and practitioners in
finance who have long viewed the rational investor assumption with skepticism
have developed a new branch of finance called behavioral finance which draws on
psychology, sociology and finance to try to explain both why investors behave
the way they do and the consequences for investment strategies. As we go
through this section, examining different investment philosophies, we will try
at the outset of each philosophy to explore the assumptions about human
behavior that represent its base. 

## Market Efficiency

            A
closely related second ingredient of an investment philosophy is the view of market
efficiency or its absence that you need for the philosophy to be a successful
one. While all active investment philosophies make the assumption that markets
are inefficient, they differ in their views on what parts of the market the
inefficiencies are most likely to show up and how long they will last. Some
investment philosophies assume that markets are correct most of the time but
that they overreact when new and large pieces of information are released about
individual firms – they go up too much on good news and down too much on
bad news. Other investment strategies are founded on the belief that markets
can make mistakes in the aggregate – the entire market can be under or
overvalued – and that some investors (mutual fund managers, for example)
are more likely to make these mistakes than others.  Still other investment strategies may be based on the
assumption that while markets do a good job of pricing stocks where there is a
substantial amount of information – financial statements, analyst reports
and financial press coverage –they systematically misprice stocks on
which such information is not available.

## Tactics and Strategies

            Once
you have an investment philosophy in place, you develop investment strategies
that build on the core philosophy. Consider, for instance, the views on market
efficiency expounded in the last section. The first investor, who believes that
markets over react to news, may develop a strategy of buying stocks after large
negative earnings surprises (where the announced earnings come in well below
expectations) and selling stocks after positive earnings surprises. The second
investor who believes that markets make mistakes in the aggregate may look at
technical indicators (such as mutual fund cash positions and short sales ratios)
to find out whether the market is over bought or over sold and take a contrary
position. The third investor who believes that market mistakes are more likely
when information is absent may look for stocks that are not followed by
analysts or owned by institutional investors.

            It
is worth noting that the same investment philosophy can spawn multiple
investment strategies. Thus, a belief that investors consistently overestimate
the value of growth and under estimate the value of existing assets can manifest
itself in a number of different strategies ranging from a passive one of buying
low PE ratio stocks to a more active one of buying such companies and
attempting to liquidate them for their assets. In other words, the number of
investment strategies will vastly outnumber the number of investment
philosophies.

# Why do you need an investment philosophy?

            Most
investors have no investment philosophy, and the same can be said about many
money managers and professional investment advisors. They adopt investment
strategies that seem to work (for other investors) and abandon them when they
do not. Why, if this is possible, you might ask, do you need an investment
philosophy? The answer is simple. In the absence of an investment philosophy,
you will tend to shift from strategy to strategy simply based upon a strong
sales pitch from a proponent or perceived recent success. There are three
negative consequences for your portfolio:

1. Lacking
   a rudder or a core set of beliefs, you will be easy prey for charlatans
   and pretenders, with each one claiming to have found the magic strategy
   that beats the market.
2. As you
   switch from strategy to strategy, you will have to change your portfolio,
   resulting in high transactions costs and you will pay more in taxes.
3. While
   there may be strategies that do work for some investors, they may not be
   appropriate for you, given your objectives, risk aversion and personal
   characteristics. In addition to having a portfolio that under performs the
   market, you are likely to find yourself with an ulcer or worse.

With a strong sense of core
beliefs, you will have far more control over your destiny. Not only will you be
able to reject strategies that do not fit your core beliefs about markets but
also to tailor investment strategies to your needs.  In addition, you will be able to get much more of a big
picture view of what it is that is truly different across strategies and what
they have in common.

# The Big Picture of Investing

To see where the
different investment philosophies fit into investing, let us begin by looking
at the process of creating an investment portfolio. Note that this is a process
that we all follow – amateur as well as professional investors - though
it may be simpler for an individual constructing his or her own portfolio than
it is for a pension fund manager with a varied and demanding clientele.

## Step 1: Understanding the Client

The process always starts
with the investor and understanding his or her needs and preferences. For a
portfolio manager, the investor is a client, and the first and often most
significant part of the investment process is understanding the client�s needs,
the client�s tax status and most importantly, his or her risk preferences. For
an individual investor constructing his or her own portfolio, this may seem
simpler, but understanding one�s own needs and preferences is just as important
a first step as it is for the portfolio manager.

## Step 2: Portfolio Construction

            The
next part of the process is the actual construction of the portfolio, which we
divide into three sub-parts.

if !supportLists1.    
endifThe first of these is the decision on how to allocate the
portfolio across different asset classes defined broadly as equities, fixed
income securities and real assets (such as real estate, commodities and other
assets).  This asset allocation
decision can also be framed in terms of investments in domestic assets versus
foreign assets, and the factors driving this decision.

if !supportLists2.    
endifThe second component is the asset selection decision, where
individual assets are picked within each asset class to make up the portfolio.
In practical terms, this is the step where the stocks that make up the equity
component, the bonds that make up the fixed income component and the real
assets that make up the real asset component are selected.

if !supportLists3.    
endifThe final component is execution, where the portfolio is
actually put together. Here investors must weigh the costs of trading against
their perceived needs to trade quickly. While the importance of execution will
vary across investment strategies, there are many investors who fail at this
stage in the process.

## Step 3: Evaluate portfolio performance

The final part of the
process, and often the most painful one for professional money managers, is
performance evaluation. Investing is after all focused on one objective and one
objective alone, which is to make the most money you can, given your particular
risk preferences. Investors are not forgiving of failure and unwilling to
accept even the best of excuses, and loyalty to money managers is not a
commonly found trait. By the same token, performance evaluation is just as
important to the individual investor who constructs his or her own portfolio,
since the feedback from it should largely determine how that investor
approaches investing in the future.

These parts of the
process are summarized in Figure 1.1, and we will return to this figure to
emphasize the steps in the process as we consider different investment
philosophies. As you will see, while all investment philosophies may have the
same end objective of beating the market, each philosophy will emphasize a
different component of the overall process and require different skills for
success. 

*if !supportEmptyParas endif*

# if !vmlendif

**if !supportEmptyParas endif**

# Categorizing Investment Philosophies

            We
will present the range of investment philosophies in this section, using the
investment process to illustrate each philosophy. While we will leave much of
the detail for later, we will attempt to present at least the core of each
philosophy here.

## Market Timing versus Asset Selection

            The
broadest categorization of investment philosophies is on whether they are based
upon timing overall markets or finding individual assets that are mispriced.
The first set of philosophies can be categorized as *market timing* philosophies, while the second can be viewed as *security
selection* philosophies.

Within each, though, are numerous
strands that take very different views about markets. Consider market timing
first. While most of us consider market timing only in the context of the stock
market, there are investors who consider market timing to include a much
broader range of markets – currency markets, bond markets and real estate
come to mind.  The range of choices
among security selection philosophies is even wider and can span charting and
technical indicators, fundamentals (earnings, cashflows or growth) and
information (earnings reports, acquisition announcements).

            While
market timing has allure to all of us (because it pays off so well when you are
right), it is difficult to succeed at for exactly that reason. There are all
too often too many investors attempting to time markets, and succeeding
consistently is very difficult to do. If you decide to pick stocks, how do you
choose whether you pick them based upon charts, fundamentals or growth
potential? The answer, as we will see, in the next section will depend not only
on your views of the market and empirical evidence but also on your personal
characteristics.

## Activist versus Passive Investing

            At
the broadest level, investment philosophies can also be categorized as active
or passive strategies. In a *passive strategy*, you invest in a stock or company and wait for your investment to pay
off. Assuming that your strategy is successful, this will come from the market
recognizing and correcting a misvaluation. Thus, a portfolio manager who buys
stocks with low price earnings ratios and stable earnings is following a
passive strategy. So is an index fund manager, who essentially buys all stocks
in the index.  In an *activist
strategy*, you invest in a company and then
try to change the way the company is run to make it more valuable. Venture
capitalists can be categorized as activist investors since they not only take
positions in promising companies but they also provide significant inputs into
how these firms are run. In recent years, we have seen investors like Michael
Price and the California State pension fund (Calpers) bring this activist
philosophy to publicly traded companies, using the clout of large positions to
change the way companies are run. We should hasten to draw a contrast between
activist investing and active investing. Any investor who tries to beat the
market by picking stocks is viewed as an active investor. Thus, active
investors can adopt passive strategies or activist strategies.

## Time Horizon

            Different
investment philosophies require different time horizons. A philosophy based
upon the assumption that markets overreact to new information may generate
short term strategies. For instance, you may buy stocks right after a bad
earnings announcement, hold a few weeks and sell (hopefully at a higher price,
as the market corrects its over reaction). In contrast, a philosophy of buying
neglected companies (stocks that are not followed by analysts or held by
institutional investors) may require much longer time horizons.

            One
factor that will determine the time horizon of an investment philosophy is the
nature of the adjustment that has to occur for you to reap the rewards of a
successful strategy. Passive value investors who buy stocks in companies that
they believe are under valued may have to wait years for the market correction
to occur, even if they are right. Investors who trade ahead or after earnings
reports, because they believe that markets do not respond correctly to such
reports, may hold the stock for only a few days. At the extreme, investors who
see the same (or very similar) assets being priced differently in two markets
may buy the cheaper one and sell the more expensive one, locking in �arbitrage�
profits in a few minutes.

## Coexistence of Contradictory Strategies

            One
of the most fascinating aspects of investment philosophy is the coexistence of
investment philosophies based upon contradictory views of the markets. Thus,
you can have market timers who trade on *price momentum* (suggesting that investors are slow to learn from
information) and market timers who are *contrarians* (which is based on the belief that markets over
react). Among security selectors who use fundamentals, you can have *value
investors* who buy value stocks, because
they believe markets overprice growth, and *growth investors* who buy growth stocks using exactly the opposite
justification. The coexistence of these contradictory impulses for investing
may strike some as irrational, but it is healthy and may actually be
responsible for keeping the market in balance.  In addition, you can have investors with contradictory
philosophies co-existing in the market because of their different time
horizons, views on risk and tax status. For instance, tax exempt investors may
find stocks that pay large dividends a bargain, while taxable investors may
reject these same stocks because dividends are taxed at the ordinary tax rate.

## Investment Philosophies in Context

            We
can consider the differences between investment philosophies in the context of
the investment process, described in figure 1.1. Market timing strategies
primarily affect the asset allocation decision. Thus, investors who believe
that stocks are under valued will invest more of their portfolios in stocks
than would be justified given their risk preferences. Security selection
strategies in all their forms – technical analysis, fundamentals or
private information – all center on the security selection component of
the portfolio management process. You could argue that strategies that are not
based upon grand visions of market efficiency but are designed to take
advantage of momentary mispricing of assets in markets (such as arbitrage)
revolve around the execution segment of portfolio management. It is not
surprising that the success of such opportunistic strategies depend upon
trading quickly to take advantage of pricing errors, and keeping transactions
costs low.  Figure 1.2 presents the
different investment philosophies.

# if !vmlendif

# Developing an Investment Philosophy: The Step

            If
every investor needs an investment philosophy, what is the process that you go
through to come up with such a philosophy? While portfolio management is about the
process, we can lay out the three steps involved in this section.

## Step 1: Understand the fundamentals of risk and valuation

            Before
you embark on the journey of finding an investment philosophy, you need to get
your financial toolkit ready. At the minimum, you should understand

if !supportLists-       endifhow
to measure the risk in an investment and relate it to expected returns.

if !supportLists-       endifhow
to value an asset, whether it be a bond, stock or a business

if !supportLists-       endifthe
ingredients of trading costs, and the trade off between the speed of trading
and the cost of trading

We would hasten to add that you do not need to be a
mathematical wizard to do any of these and it is easy to acquire these basic
tools.

## Step 2: Develop a point of view about how markets work and where they might break down

            Every
investment philosophy is grounded in a point of view about human behavior (and
irrationality). While personal experience often determines how we view our
fellow human beings, we should expand this to consider broader evidence from
markets on how investors act before we make our final judgments.

            Over
the last few decades, it has become easy to test different investment
strategies as data becomes more accessible. There now exists a substantial body
of research on the investment strategies that have beaten the market over time.
For instance, researchers have found convincing evidence that stocks with low
price to book value ratios have earned significantly higher returns than stocks
of equivalent risk but higher price to book value ratios. It would be foolhardy
not to review this evidence in the process of developing your investment
philosophy.  At the same time,
though, you should keep in mind three caveats about this research:

1. Since
   they are based upon the past, they represent a look in the rearview
   mirror. Strategies that earned substantial returns in the 1990s may no
   longer be viable strategies now. In fact, as successful strategies get
   publicized either directly (in books and articles) or indirectly (by
   portfolio managers trading on them), you should expect to see them become
   less effective.
2. Much
   of the research is based upon constructing hypothetical portfolios, where
   you buy and sell stocks at historical prices and little or no attention is
   paid to transactions costs. To the extent that trading can cause prices to
   move, the actual returns on strategies can be very different from the
   returns on the hypothetical portfolio.
3. A
   test of an investment strategy is almost always a joint test of both the
   strategy and a model for risk. To see why, consider the evidence that stocks
   with low price to book value ratios earn higher returns than stocks with
   high price to book value ratios, with similar risk (at least as measured
   by the models we use). To the extent that we mismeasure risk or ignore a
   key component of risk, it is entirely possible that the higher returns are
   just a reward for the greater risk associated with low price to book value
   stocks.

Since
understanding whether a strategy beats the market is such a critical component
of investing, we will consider the approaches that are used to test a strategy,
some basic rules that need to be followed in doing these tests and common
errors that are made (unintentionally or intentionally) when running such
tests. As we look at each investment philosophy, we will review the evidence
that is available on strategies that emerge from that philosophy.

## Step 3: Find the philosophy that provides the best fit for you

            Once
you understand the basics of investing, form your views on human foibles and
behavior and review the evidence accumulated on each of the different
investment philosophies, you are ready to make your choice. In our view, there
is potential for success with almost every investment philosophy (yes, even
charting) but the prerequisites for success can vary. In particular, success
may rest on:

1. *Your
   risk aversion*: Some strategies are
   inherently riskier than others. For instance, venture capital or private
   equity investing, where you invest your funds in small, private businesses
   that show promise is inherently more risky than buying value stocks
   – equity in large, stable, publicly traded companies. The returns
   are also likely to be higher. However, more risk averse investors should
   avoid the first strategy and focus on the second. Picking an investment
   philosophy (and strategy) that requires you to take on more risk than you
   feel comfortable taking can be hazardous to your health and your
   portfolio.
2. *The
   size of your portfolio*: Some
   strategies require larger portfolios for success whereas others work only
   on a smaller scale. For instance, it is very difficult to be an activist
   value investor if you have only $ 100,000 in your portfolio, since firms
   are unlikely to listen to your complaints. On the other hand, a portfolio
   manager with $ 100 billion to invest may not be able to adopt a strategy
   that requires buying small, neglected companies. With such a large
   portfolio, she would very quickly end up becoming the dominant stockholder
   in each of the companies and affecting the price every time she trade.
3. *Your
   time horizon*: Some investment
   philosophies are predicated on a long time horizon, whereas others require
   much shorter time horizons. If you are investing your own funds, your time
   horizon is determined by your personal characteristics – some of us
   are more patient than others – and your needs for cash – the
   greater the need for liquidity, the shorter your time horizon has to be.
   If you are a professional (an investment adviser or portfolio manager),
   managing the funds of others, it is your clients time horizon and cash
   needs that will drive your choice of investment philosophies and
   strategies.
4. *Your
   tax status*: Since such a significant
   portion of your money ends up going to the tax collectors, they have a
   strong influence on your investment strategies and perhaps even the
   investment philosophy you adopt. In some cases, you may have to abandon
   strategies that you find attractive on a pre-tax basis because of the tax
   bite that they expose you to.

Thus, the right investment philosophy for you will reflect
your particular strengths and weaknesses. It should come as no surprise, then,
that investment philosophies that work for some investors do not work for
others. Consequently, there can be no one investment philosophy that can be
labeled �best� for all investors.

# Conclusion

            An
investment philosophy represents a set of core beliefs about how investors
behave and markets work. To be a successful investor, you not only have to
consider the evidence from markets but you also have to examine your own
strengths and weaknesses to come up with an investment philosophy that best
fits you.  Investors without core
beliefs tend to wander from strategy to strategy, drawn by the anecdotal
evidence or recent success, creating transactions costs and incurring losses as
a consequence. Investors with clearly defined investment philosophies tend to
be more consistent and disciplined in their investment choices.

            In
this introduction, we considered a broad range of investment philosophies from
market timing to arbitrage and placed each of them in the broad framework of
portfolio management. We also examined the three steps in the path to an
investment philosophy, beginning with the understanding of the tools of
investing – risk, trading costs and valuation – continuing with an
evaluation of the empirical evidence on whether, when and how markets break
down and concluding with a self-assessment, to find the investment philosophy
that best matches your time horizon, risk preferences and portfolio
characteristics.
