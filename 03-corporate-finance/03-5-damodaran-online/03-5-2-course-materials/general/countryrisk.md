---
title: "Measuring Company Exposure to Country Risk: Theory and Practice"
status: active
owner: weprintmoney
created: 2026-09-04
last_updated: 2026-09-04
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/CountryRisk.htm
---

Measuring Company Exposure to Country Risk: Theory and Practice

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
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:Times;}
h1
{mso-style-next:Normal;
margin-top:12.0pt;
margin-right:0in;
margin-bottom:3.0pt;
margin-left:0in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:1;
font-size:14.0pt;
font-family:Times;
mso-font-kerning:16.0pt;}
h2
{mso-style-next:Normal;
margin-top:6.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
page-break-after:avoid;
mso-outline-level:2;
font-size:12.0pt;
font-family:Times;}
h3
{mso-style-next:Normal;
margin-top:6.0pt;
margin-right:0in;
margin-bottom:6.0pt;
margin-left:0in;
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
margin-top:6.0pt;
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
margin:0in;
margin-bottom:.0001pt;
text-align:center;
line-height:150%;
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
line-height:24.0pt;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:"Times New Roman";}
p.MsoCaption, li.MsoCaption, div.MsoCaption
{mso-style-next:Normal;
margin:0in;
margin-bottom:.0001pt;
text-align:justify;
line-height:150%;
mso-pagination:widow-orphan;
font-size:10.0pt;
font-family:Times;
font-style:italic;}
span.MsoFootnoteReference
{font-size:8.0pt;
mso-text-raise:3.0pt;}
p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
{margin:0in;
margin-bottom:.0001pt;
text-align:justify;
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
line-height:24.0pt;
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
@page Section2
{size:11.0in 8.5in;
mso-page-orientation:landscape;
margin:1.25in 1.0in 1.25in 1.0in;
mso-header-margin:.5in;
mso-footer-margin:.5in;
mso-paper-source:0;}
div.Section2
{page:Section2;}
/\* List Definitions \*/
@list l0
{mso-list-id:8;
mso-list-type:simple;
mso-list-template-ids:984073;}
@list l0:level1
{mso-level-tab-stop:.25in;
mso-level-number-position:left;
margin-left:.25in;
text-indent:-.25in;}
@list l1
{mso-list-id:91947161;
mso-list-type:hybrid;
mso-list-template-ids:1740675978 984073 1639433 1770505 984073 1639433 1770505 984073 1639433 1770505;}
@list l1:level1
{mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;}
@list l2
{mso-list-id:244848011;
mso-list-type:hybrid;
mso-list-template-ids:1227125964 -1 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l2:level1
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
@list l3
{mso-list-id:500045995;
mso-list-type:hybrid;
mso-list-template-ids:30071432 -1 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l3:level1
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
@list l4
{mso-list-id:1400596961;
mso-list-type:hybrid;
mso-list-template-ids:1130533968 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l4:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
@list l5
{mso-list-id:1452357632;
mso-list-type:hybrid;
mso-list-template-ids:1288324194 66569 197641 328713 66569 197641 328713 66569 197641 328713;}
@list l5:level1
{mso-level-number-format:bullet;
mso-level-text:\F0B7;
mso-level-tab-stop:.5in;
mso-level-number-position:left;
text-indent:-.25in;
font-family:Symbol;}
ol
{margin-bottom:0in;}
ul
{margin-bottom:0in;}
-->

# if !supportEmptyParas endif

# if !supportEmptyParas endif

# if !supportEmptyParas endif

# if !supportEmptyParas endif

# Measuring Company Exposure to Country Risk: Theory and Practice

*if !supportEmptyParas endif*

if !supportEmptyParas endif

            As
companies and investors globalize and financial markets expand around the
world, we are increasingly faced with estimation questions about the risk
associated with this globalization. When investors invest in Petrobras, Gazprom
and China Power, they may be rewarded with higher returns but they are also
exposed to additional risk. When Coca Cola and Nestle push for growth in Asia
and Latin America, they clearly are exposed to the political and economic
turmoil that often characterize these markets.

In practical terms, how, if at all,
should we adjust for this additional risk? In the first part of the paper, we
will review the discussion on country risk premiums and how to estimate them.
In the latter part of the paper, we will focus on a related question: Once we
have estimated a country risk premium, how do we evaluate a company�s exposure
to country risk? In the process, we will argue that a company�s exposure to
country risk should not be determined by where it is incorporated and traded.
By that measure, neither Coca Cola nor Nestle are exposed to country risk.
Exposure to country risk should come from a company�s operations, making
country risk a critical component of the valuation of almost every large
multinational corporation.

# Country Risk

            There
are two key questions that we face when we are asked to evaluate emerging
markets in Asia, Latin America and Eastern Europe. The first relates to whether
there should be an additional risk premium when valuing equities in these
markets, because of the country risk. As we will see, the answer will depend
upon whether we view markets to be open or segmented and whether we believe in
a one-factor or a multi-factor model. The second question relates to estimating
an equity risk premium for emerging markets. Depending upon our answer to the
first question, we will consider several solutions.

## Should there be a country risk premium?

            Is
there more risk in investing in Malaysian or Brazilian equities than there is
in investing in equities in the United States? The answer, to most, seems to be
obviously affirmative. That, however, does not answer the question of whether
there should be an additional risk premium charged when investing in those
markets.

            Note
that the only risk that is relevant for purposes of estimating a cost of equity
is market risk or risk that cannot be diversified away. The key question then
becomes whether the risk in an emerging market is diversifiable or
non-diversifiable risk. If, in fact, the additional risk of investing in
Malaysia or Brazil can be diversified away, then there should be no additional
risk premium charged. If it cannot, then it makes sense to think about
estimating a country risk premium.

            But
diversified away by whom? Equity in a Brazilian or Malaysian firm can be held
by hundreds or thousands of investors, some of whom may hold only domestic
stocks in their portfolio, whereas others may have more global exposure.  For purposes of analyzing country risk,
we look at the marginal investor � the investor most likely to be trading on
the equity. If that marginal investor is globally diversified, there is at
least the potential for global diversification. If the marginal investor does
not have a global portfolio, the likelihood of diversifying away country risk
declines substantially. Stulz (1999) made a similar point using different
terminology. He differentiated between segmented markets, where risk premiums
can be different in each market, because investors cannot or will not invest
outside their domestic markets, and open markets, where investors can invest
across markets. In a segmented market, the marginal investor will be
diversified only across investments in that market, whereas in an open market,
the marginal investor has the opportunity (even if he or she does not take it)
to invest across markets.

            Even
if the marginal investor is globally diversified, there is a second test that
has to be met for country risk to not matter. All or much of country risk
should be country specific. In other words, there should be low correlation
across markets. Only then will the risk be diversifiable in a globally
diversified portfolio. If, on the other hand, the returns across countries have
significant positive correlation, country risk has a market risk component, is
not diversifiable and can command a premium. Whether returns across countries
are positively correlated is an empirical question. Studies from the 1970s and
1980s suggested that the correlation was low, and this was an impetus for
global diversification. Partly because of the success of that sales pitch and
partly because economies around the world have become increasingly intertwined
over the last decade, more recent studies indicate that the correlation across
markets has risen. This is borne out by the speed with which troubles in one
market, say Russia, can spread to a market with which it has little or no
obvious relationship, say Brazil.

            So
where do we stand? We believe that while the barriers to trading across markets
have dropped, investors still have a home bias in their portfolios and that
markets remain partially segmented. While globally diversified investors are
playing an increasing role in the pricing of equities around the world, the
resulting increase in correlation across markets has resulted in a portion of
country risk being non-diversifiable or market risk. In the next section, we
will consider how best to measure this country risk and build it into expected
returns.

## Estimating a Country Risk Premium

            If
country risk is not diversifiable, either because the marginal investor is not
globally diversified or because the risk is correlated across markets, we are
left with the task of measuring country risk and estimating country risk
premiums. In this section, we will consider two approaches that can be used to
estimate country risk premiums. One approach builds on historical risk premiums
and can be viewed as the *historical risk premium* *plus* approach. In the
other approach, we estimate the equity risk premium by looking at how the
market prices stocks and expected cash flows � this is the *implied
premium approach*.

### 1. Historical Premium

            Most
practitioners, when estimating risk premiums in the United States. look at the
past. In this approach, we look at what we would have earned as investors by
investing in equities as opposed to investing in riskless investments. We will
consider why this approach cannot be used in emerging market and possible
modifications.

#### Historical Premiums in Emerging Markets

            The
argument for using historical risk premiums is a simple one. If investors have,
on average, earned 5% more by investing in stocks than government bonds in the
past, this is a reasonable estimate of what they will continue to make in the
future. Notwithstanding the logic in this statement, the problem with
historical risk premiums remains their imprecision. After all, the historical
premiums are extracted from returns on stocks and bonds, which are volatile over
time. As a consequence, the historical premium of 5% may come with a standard
error that is so large as to make it useless. How can we estimate the standard
error? Roughly speaking, the standard error in the risk premium is a function
of the annual standard deviation in stock returns and the number of years of
data that we have:

Standard Error in the Risk Premium = if !vml![](CountryRisk_files/image003.gif)endif

To illustrate, the standard error in the historical risk
premium for the United States, computed using 75 years of data is calculated
below:

Standard Error in US Risk Premium = if !vml![](CountryRisk_files/image006.gif)endif = 2.31%

With an annualized standard deviation in stock returns of
20%, the standard error, even with 75 years of data, is roughly 2.31%.

            With
emerging markets, we will almost never have access to as much historical data
as we do in the United States. In markets like Brazil, Russia and Indonesia, we
can consider ourselves lucky if we can find 10 to 20 years of reliable
historical data. If we combine this with the high volatility in stock returns
in these markets, the conclusion we have to draw is that historical risk
premiums can be computed for these markets but they will be useless because of
the large standard errors in the estimates.[if !supportFootnotes[1]endif](#_ftn1)

#### Modified Historical Risk Premiums

While historical risk premiums for
markets outside the United States cannot be estimated with much precision, we
still need to estimate a risk premium for use in these markets. To approach
this estimation question, let us start with the basic proposition that the risk
premium in any equity market can be written as:

Equity Risk Premium = Base Premium for Mature Equity Market
+ Country Equity Risk Premium

The country premium could reflect
the extra risk in a specific market, reflecting the fact that it is not a mature
equity market. To estimate the base premium for a mature equity market, we can
look at the US market. Between 1928 and 2002, stocks in the United States
delivered a premium of 4.53% over government bonds. A more expansive look at
all equity markets in the 20th century suggests an equity risk
premium of about 4%.[if !supportFootnotes[2]endif](#_ftn2)
To estimate the country equity risk premium, however, we need to measure
country risk and convert the country risk measure into a country risk premium.

#### Measuring Country Risk

While there are several measures of
country risk, one of the simplest and most easily accessible is the rating
assigned to a country�s debt by a ratings agency (S&P, Moody�s, Fitch and
IBCA all rate countries). These ratings measure default risk (rather than
equity risk) but they are affected by many of the factors that drive equity
risk � the stability of a country�s currency, its budget and trade balances and
its political stability, for instance[if !supportFootnotes[3]endif](#_ftn3).
Consider Brazil, as an example. In September 2003, the Brazilian government has
dollar denominated C-Bonds outstanding, with ten years to maturity.  S&P rated the Brazilian government
C-bond at B+ whereas Moody�s assigned a B2 rating to the same bond.

            While
ratings provide a convenient measure of country risk, there are costs associated
with using them as the only measure. First, ratings agencies often lag markets
when it comes to responding to changes in the underlying default risk. Second,
the ratings agency focus on default risk may obscure other risks that could
still affect equity markets. What are the alternatives? There are numerical
country risk scores that have been developed by some services as much more
comprehensive measures of risk. The Eurasia Group, for instance, has a score
that runs from 0 to 100, where 0 is no risk, and 100 is most risky, that it
uses to rank emerging markets. In September 2003, the country risk score for
Brazil, based upon this measure, was 61. Alternatively, country risk can be
estimated from the bottom-up by looking at economic fundamentals in each
country. This, of course, requires significantly more information than the
other approaches.

#### Measuring Country Risk Premiums

              If
country risk matters and leads to higher premiums for riskier countries, the
obvious follow-up question becomes how we measure this additional premium. In
this section, we will look at three approaches. The first builds on default
spreads on country bonds issued by each country whereas the latter two use
equity market volatility as their basis.

##### 1. Country Bond Default Spreads

The simplest and most widely used measure of
country risk comes from looking at the yields on bonds issued by the country in
a currency (such as the dollar or the euro) where there is a default free bond
yield to which it can be compared.[if !supportFootnotes[4]endif](#_ftn4) 
Consider the dollar denominated Brazilian C-Bond that we highlighted
earlier in this section. The C-Bond is widely traded and both the price and
yield of the bond reflect market views of Brazil. In September 2003, the
10-year C-bond was priced to yield 10.12%. Comparing this yield to the 10-year
U.S. treasury bond rate of 4.11% generates a default spread of 6.01% for
the Brazilian bond.

            While
we can make the argument that the default spread in the C-Bond is a reasonable
measure of the default risk in Brazil, it is also a volatile measure. In figure
1, we have graphed the yields on the C-Bond and the U.S. treasury bond and
highlighted the default spread.

if !vml![](CountryRisk_files/image009.gif)endif

Note that the
spread widened dramatically during 2002, mostly as a result of uncertainty in
neighboring Argentina and concerns about the Brazilian presidential elections.[if !supportFootnotes[5]endif](#_ftn5) After the elections, the spreads decreased
just as quickly. Given this volatility, a reasonable argument can be made that
we should consider the average spread over a period of time such as two years
rather than the default spread at the moment.

            Analysts
who use default spreads as measures of country risk typically add them on to
both the cost of equity and debt of every company traded in that country. For
instance, the cost of equity for a Brazilian company, estimated in U.S.
dollars, will be 6.01% higher than the cost of equity of an otherwise similar
U.S. company, using the September 2003 measure of the default spread. In some
cases, analysts add the default spread to the U.S. risk premium and multiply it
by the beta. This increases the cost of equity for high beta companies and
lowers them for low beta firms. We will consider the relative strengths of both
approaches in the next section.

##### 2. Relative Equity Market Standard Deviations

            There
are some analysts who believe that the equity risk premiums of markets should
reflect the differences in equity risk, as measured by the volatilities of
these markets. A conventional measure of equity risk is the standard deviation
in stock prices; higher standard deviations are generally associated with more
risk. If you scale the standard deviation of one market against another, you
obtain a measure of relative risk.

if !vml![](CountryRisk_files/image012.gif)endif

This relative standard deviation when multiplied by the
premium used for U.S. stocks should yield a measure of the total risk premium
for any market.

if !vml![](CountryRisk_files/image015.gif)endif

Assume, for the moment, that you are using a equity risk
premium for the United States of 4.53%. The annualized standard deviation in
the S&P 500 between 2001 and 2003, using weekly returns, was 18.59%,
whereas the standard deviation in the Bovespa (the Brazilian equity index) over
the same period was 33.37%.[if !supportFootnotes[6]endif](#_ftn6)  Using these values, the estimate of a
total risk premium for Brazil would be as follows.

if !vml![](CountryRisk_files/image018.gif)endif

The country risk premium can be isolated as follows:

if !vml![](CountryRisk_files/image021.gif)endif

While this approach has intuitive appeal, there are problems
with using standard deviations computed in markets with widely different market
structures and liquidity. There are very risky emerging markets that have low
standard deviations for their equity markets because the markets are illiquid.
This approach will understate the equity risk premiums in those markets. The
second problem is related to currencies since the standard deviations are
usually measured in local currency terms; the standard deviation in the U.S.
market is a dollar standard deviation, whereas the standard deviation in the
Brazilian market is a nominal Brazilian Real standard deviation. This is a
relatively simple problem to fix, though, since the standard deviations can be
measured in the same currency � you could estimate the standard deviation in
dollar returns for the Brazilian market.

##### 3. Default Spreads + Relative Standard Deviations

            The
country default spreads that come with country ratings provide an important
first step, but still only measure the premium for default risk. Intuitively,
we would expect the country equity risk premium to be larger than the country
default risk spread. To address the issue of how much higher, we look at the
volatility of the equity market in a country relative to the volatility of the
bond market used to estimate the spread. 
This yields the following estimate for the country equity risk premium.

if !vml![](CountryRisk_files/image024.gif)endif

To illustrate, consider again the case of Brazil. As noted
earlier, the default spread on the Brazilian C-Bond in September 2003 was 6.01%
and the annualized standard deviation in the Brazilian equity index over the
previous year was 33.37%. Using two years of weekly returns, the annualized
standard deviation in the Brazilian dollar denominated C-bond was 26.15%. The
resulting country equity risk premium for Brazil is as follows:

if !vml![](CountryRisk_files/image027.gif)endif

Unlike the equity standard deviation approach, this premium
is in addition to a mature market equity risk premium. Note that this country
risk premium will increase if the country rating drops or if the relative
volatility of the equity market increases.

            Why
should equity risk premiums have any relationship to country bond spreads? A
simple explanation is that an investor who can make 11% on a dollar-denominated
Brazilian government bond would not settle for an expected return of 10.5% (in
dollar terms) on Brazilian equity. Playing devil�s advocate, however, a critic
could argue that the interest rate on a country bond, from which default
spreads are extracted, is not really an expected return since it is based upon
the promised cash flows (coupon and principal) on the bond rather than the expected
cash flows. In fact, if we wanted to estimate a risk premium for bonds, we
would need to estimate the expected return based upon expected cash flows,
allowing for the default risk. This would result in a much lower default spread
and equity risk premium.

            Both
this approach and the previous one use the standard deviation in equity of a
market to make a judgment about country risk premium, but they measure it
relative to different bases. This approach uses the country bond as a base,
whereas the previous one uses the standard deviation in the U.S. market. This
approach assumes that investors are more likely to choose between Brazilian
bonds and Brazilian equity, whereas the previous one approach assumes that the
choice is across equity markets.

##### Choosing between the approaches

            The
three approaches to estimating country risk premiums will generally give you
different estimates, with the bond default spread and relative equity standard
deviation approaches yielding lower country risk premiums than the melded
approach that uses both the country bond default spread and the equity and bond
standard deviations. Table 1 summarizes the estimates of country equity and
total risk premium using the three approaches for Brazil in September 2003:

###### Table 1: Country and Total Equity Risk Premium: Brazil in September 2003

|  |  |  |  |
| --- | --- | --- | --- |
| *Approach* | *Mature Market Equity Premium* | *Brazil Country Risk Premium* | *Total Equity Risk Premium* |
| Country Bond Default Spread | 4.53% | 6.01% | 10.54% |
| Relative Equity Market Standard Deviations | 4.53% | 3.60% | 8.13% |
| Melded Approach (Bond default spread + Relative Standard Deviation) | 4.53% | 7.67% | 12.20% |

We believe that the larger country
risk premiums that emerge from the last approach are the most realistic for the
immediate future, but that country risk premiums will decline over time. Just
as companies mature and become less risky over time, countries can mature and
become less risky as well.

One way to adjust country risk
premiums over time is to begin with the premium that emerges from the melded
approach and to adjust this premium down towards either the country bond
default spread or the country premium estimated from equity standard
deviations. Another way of presenting this argument is to note that the
differences between standard deviations in equity and bond prices narrow over
longer periods and the resulting relative volatility will generally be smaller[if !supportFootnotes[7]endif](#_ftn7).
Thus, the equity risk premium will converge to the country bond default spread
as we look at longer term expected returns. As an illustration, the country
risk premium for Brazil would be 7.67%% for the next year but decline over time
to either the 6.01% (country default spread) or 3.60% (relative standard
deviation).

### II. An Alternative Approach: Implied Equity Premiums

There is an alternative to
estimating risk premiums that does not require historical data or corrections
for country risk, but does assume that the market, overall, is correctly
priced. Consider, for instance, a very simple valuation model for stocks:

Value
= if !vml![](CountryRisk_files/image030.gif)endif

This is essentially the present value of dividends growing
at a constant rate. Three of the four inputs in this model can be obtained
externally - the current level of the market (value), the expected dividends
next period and the expected growth rate in earnings and dividends in the long
term. The only �unknown� is then the required return on equity; when we solve
for it, we get an implied expected return on stocks. Subtracting out the
riskfree rate will yield an implied equity risk premium.

            To
illustrate, assume that the current level of the S&P 500 Index is 900, the
expected dividend yield on the index is 2% and the expected growth rate in
earnings and dividends in the long term is 7%. Solving for the required return
on equity yields the following:

            900
= (.02\*900) /(r - .07)

Solving for r,

            r
= (18+63)/900 = 9%

If the current riskfree rate is 6%, this will yield a
premium of 3%.

            This
approach can be generalized to allow for high growth for a period, and extended
to cover cash flow based, rather than dividend, models. To illustrate this,
consider the S&P 500 Index, as of September 23, 2003. The index was at
1018, and the cash yield (dividends + stock buybacks) on the index over the
previous 12 months was roughly 2.93%; the treasury bond rate on that date was
4.05%. In addition, the consensus estimate[if !supportFootnotes[8]endif](#_ftn8)
of growth in earnings for companies in the index was approximately 9% for the
next 5 years. Since this is not a growth rate that can be sustained forever, we
employ a two-stage valuation model, where we allow growth to continue at 9% for
5 years, and then lower the growth rate to the treasury bond rate of 4.05%
after that.[if !supportFootnotes[9]endif](#_ftn9) The
following table summarizes the expected cash flows for the next 5 years of high
growth, and the first year of stable growth thereafter:

|  |  |
| --- | --- |
| Year | Cash Flow on Index |
| 1 | 32.49 |
| 2 | 35.41 |
| 3 | 38.60 |
| 4 | 42.07 |
| 5 | 45.86 |
| 6 | 48.84 |

aCash flow in the
first year  = 2.93% of 1018 (1.09)

If we assume that these are reasonable estimates of the cash
flows and that the index is correctly priced, then

Level of the index = 1018 =
32.49/(1+r) + 35.41/(1+r)2+ + 38.60/(1+r)3 + 42.07/(1+r)4+ (45.86+(48.84/(r-.0405))/(1+r)5

Note that the last term in the equation is the terminal
value of the index, based upon the stable growth rate of 4.05%, discounted back
to the present. Solving for r in this equation yields us the required return on
equity of 7.84%. Subtracting the treasury bond rate of 4.05% from this return
yields an implied equity premium of 3.79% for the United States in September
2003.

#### Implied Premiums in Emerging Markets

            The
advantage of the implied premium approach is that it is market-driven and
current, and does not require any historical data. Thus, it can be used to
estimate implied equity premiums in any market. It is, however, bounded by
whether the model used for the valuation is the right one and the availability
and reliability of the inputs to that model. For instance, the equity risk
premium for the Brazilian equity market on September 23, 2003, was estimated
from the following inputs. The index (Bovespa) was at 16889 and the current
dividend yield on the index was 4.55%. Earnings in companies in the index are
expected to grow 15% (in US dollar terms) over the next 5 years, and 5%
thereafter.[if !supportFootnotes[10]endif](#_ftn10) These
inputs yield a required return on equity of 12.17%, which when compared to the
treasury bond rate of 4.05% on that day results in an implied equity premium of
8.12%. For simplicity, we have used nominal dollar expected growth rates[if !supportFootnotes[11]endif](#_ftn11)
and treasury bond rates, but this analysis could have been done entirely in the
local currency.

            While
the level of the index and the dividend yield are widely available, earnings
growth estimates are more difficult to come by in many markets. To the extent
that firms do not pay out what they can afford to in dividends and expected
growth rates cannot be easily estimated, implied risk premiums may be
understated. Nevertheless, they offer promise because they offer
forward-looking estimates.

#### Decomposing Implied Equity Risk Premiums

            The
implied equity risk premium for a market can be very different from the
premiums estimated from the three approaches used in the last section. Part of
the reason for that is that the implied equity risk premium is an estimate in
perpetuity whereas the estimates from the last section are estimated for the
immediate future. The other reason for the difference lies in the assumption
that we make when estimating implied equity risk premiums that the market is
correctly priced at the time of the estimation. In essence, we are being
market neutral, i.e., not taking a view on markets, when we use an implied
equity premium.

            Once
we have an estimate of the implied equity risk premium for an emerging market,
we can decompose it into a mature market equity risk premium and a
country-specific equity risk premium by comparing it to the implied equity risk
premium for a mature equity market (the US, for instance). Applying this
approach to Brazil in September 2003, we get the following:

Implied Equity premium for Brazil (see above) = 8.12%

Implied Equity premium for US (see above) = 3.79%

Country Specific Equity Risk Premium for Brazil = 4.33%

# Estimating Asset Exposure to Country Risk Premiums

Once country risk premiums have
been estimated, the final question that we have to address relates to the
exposure of individual companies to country risk. Should all companies in a
country with substantial country risk be equally exposed to country risk? While
intuition suggests that they should not, we will begin by looking at standard
approaches that assume that they are. We will follow up by scaling country risk
exposure to established risk parameters such as betas and complete the
discussion with an argument that individual companies should be evaluated for
exposure to country risk.

## The Bludgeon Approach

The simplest assumption to
make when dealing with country risk, and the one that is most often made, is
that all companies in a market are equally exposed to country risk. The cost of
equity for a firm in a market with country risk can then be written as:

Cost of
equity = Riskfree Rate + Beta (Mature Market Premium) + Country Risk Premium

Thus, for Brazil, where we
have estimated a country risk premium of 7.67% from the melded approach, each
company in the market will have an additional country risk premium of 7.67%
added to its expected returns. For instance, the costs of equity for Embraer,
an aerospace company listed in Brazil, with a beta[if !supportFootnotes[12]endif](#_ftn12)
of 1.07 and Embratel, a Brazilian telecommunications company, with a beta of
0.80, in US dollar terms would be:

Cost of Equity for Embraer = 4.05% + 1.07 (4.53%) +
7.67%= 16.57%

Cost of Equity for Embratel = 4.05% + 0.80 (4.53%) + 7.67% =
15.34%

Note that the riskfree rate that we use is the US treasury
bond rate (4.05%), and that the 4.53% is the equity risk premium for a mature
equity market (estimated from historical data in the US market). It is also
worth noting that analysts estimating cost of equity for Brazilian companies,
in US dollar terms, often use the Brazilian C-Bond rate, a dollar denominated
Brazilian bond, as the riskfree rate. This is dangerous, since it is often also
accompanied with a higher risk premium, and ends up double counting risk. It
also seems inconsistent to use a rate that clearly incorporates default risk as
a riskfree rate. To convert this dollar cost of equity into a cost of equity in
the local currency, all that we need to do is to scale the estimate by relative
inflation. To illustrate, if the BR inflation rate is 7%[if !supportFootnotes[13]endif](#_ftn13)
and the U.S. inflation rate is 2%, the cost of equity for Embraer in BR terms
can be written as:

Expected Cost of EquityBR = 1.1657 (1.07/1.02) �
1 = .2228 or 22.28%

This will ensure consistency across estimates and valuations
in different currencies.

## The Beta Approach

For those investors who
are uncomfortable with the notion that all companies in a market are equally
exposed to country risk, a fairly simple alternative is to assume that a
company's exposure to country risk is proportional to its exposure to all other
market risk, which is measured by the beta.  Thus, the cost of equity for a firm in an emerging market
can be written as follows:

Cost of
equity= Riskfree Rate+ Beta (Mature Market Premium + Country Risk Premium)

In practical terms, scaling the country risk premium to the
beta of a stock implies that stocks with betas above one will be more exposed
to country risk than stocks with a beta below one. For Embraer, with a beta of
1.07, this would lead to a dollar cost of equity estimate of:

Cost of Equity for Embraer = 4.05% + 1.07 (4.53% + 7.67%) =
17.10%

For Embratel, with its lower beta of 0.80, the cost of
equity is:

Cost of Equity for Embraer = 4.05% +  0.80 (4.53% + 7.67%) = 13.81%

The advantage of using betas is that they are freely
available for most firms. The disadvantage is that while betas measure overall
exposure to macro economic risk, they may not be good measures of country risk.

## The Lambda Approach

The most general, and our
preferred approach, is to allow for each company to have an exposure to country
risk that is different from its exposure to all other market risk.  For lack of a better term, let us term
the measure of a company�s exposure to country risk to be lambda (l). Like a beta, a lambda will be scaled
around one, with a lambda of one indicating a company with average exposure to
country risk and a lambda above or below one indicating above or below average
exposure to country risk. The cost of equity for a firm in an emerging market
can then be written as:

Expected Return = Rf
+ Beta (Mature Market Equity Risk Premium) + l
(County Risk Premium)

Note that this approach essentially converts our expected
return model to a two-factor model, with the second factor being country risk,
with l measuring exposure to country
risk.

### Determinants of a company�s exposure to country risk

            Most
investors would accept the general proposition that different companies in a
market should have different exposures to country risk. But what are the
determinants of this exposure? In this section, we will consider the factors
that determine lambdas.

#### Revenue Sources

            The
most obvious determinant of a company�s risk exposure to country risk is how
much of the revenues it derives from the country. A company that derives 30% of
its revenues from Brazil should be less exposed to Brazilian country risk than
a company that derives 70% of its revenues from Brazil. Note, though, that this
then opens up the possibility that a company can be exposed to the risk in many
countries. Thus, the company that derives only 30% of its revenues from Brazil
may derive its remaining revenues from Argentina and Venezuela, exposing it to
country risk in those countries. Extending this argument to multinationals, we would
argue that companies like Coca Cola and Nestle can have substantial exposure to
country risk because so much of their revenues come from emerging markets.

#### Production Facilities

            A
company can be exposed to country risk, even if it derives no revenues from
that country, if its production facilities are in that country. After all,
political and economic turmoil in the country can throw off production
schedules and affect the company�s profits. Companies that can move their
production facilities elsewhere can spread their risk across several countries,
but the problem is exaggerated for those companies that cannot move their
production facilities. Consider the case of mining companies. An African gold
mining company may export all of its production but it will face substantial
country risk exposure because its mines are not moveable.

#### Risk Management

            Companies
that would otherwise be exposed to substantial country risk may be able to
reduce this exposure by buying insurance against specific (unpleasant) contingencies
and by using derivatives. A company that uses risk management products should
have a lower exposure to country risk � a lower lambda � than an otherwise
similar company that does not use these products. Since a lower lambda will
reduce the cost of equity and capital, why would a company choose not to manage
risk? The answer lies in the fact that risk management is not costless.  Insurance costs money and will reduce
the margins and profits of any company that uses it. Futures contracts may be
less expensive but companies that use them lose upside potential while
protecting against downside risk. A gold mining company that uses futures
contracts to hedge against gold pricing risk will be protected from an earnings
decline if gold prices go down but will have to give up higher earnings if gold
prices go up.

### Data Constraints

            In
practical terms, few would argue with the notion that a company�s exposure to
country risk should be a function of a number of variables including the three
listed above � where revenues originate, where production facilities are
located and the use of risk management products. Before we start listing off
more variables, we should be careful to note that much of this information is
not publicly available. Even with the three variables listed above, only one �
revenue origins � is accessible for most companies in emerging markets. A few
firms do provide information about their production facilities and very few
provide details of the extent of risk management.

            It
is possible that managers within a firm and consultants who are allowed access
to internal records can come up with sophisticated measures of lambda for firms
that incorporate more information about the firm.  Investors have access to far less information and therefore have
to settle for less ambitious measure of lambda.

### Measuring Lambda

            The
lambda of a company can be estimated using one of three variables. The first
and simplest measure is based entirely on where a company generates its
revenues. The second measure is based upon accounting earnings in the most
recent period and the variation in these earnings over time. The third measure
uses stock prices, akin to conventional beta estimates, to estimate company
risk exposure.

#### Revenue

            In
the last section, we argued that a company that derives a smaller proportion of
its revenues from a market should be less exposed to country risk. But how do
we go from this statement to an actual measure of lambda?  Given the constraint that the average
lambda across all stocks has to be one (some one has to bear the country risk),
we cannot use the percentage of revenues that a company gets from a market as
lambda. We can, however, scale this measure by dividing it by the percent of
revenues that the average company in the market gets from the country to derive
a lambda.

Lambdaj = % of Revenues in country for company j/
% of revenues for average company

Consider the two large and widely followed Brazilian
companies � Embraer, an aerospace company that manufactures and sells aircraft
to many of the world�s leading airlines and Embratel, the Brazilian
telecommunications giant. In 2002, Embraer generated only 3% of its revenues in
Brazil, whereas the average company in the market obtained 85% of its revenues
in Brazil. Using the measure suggested above, the lambda for Embraer would be:

LambdaEmbraer = 3%/ 85% = 0.04

In contrast, Embratel generated 95% of its revenues from
Brazil, giving it a lambda of

LambdaEmbraer = 95%/ 85% = 1.12

Following up, Embratel is far more exposed to country risk
than Embraer and will have a much higher cost of equity.

To use this approach, we need to
estimate both the percent of revenues for the firm in question and for the
average firm in the market. While the former may be simple to obtain,
estimating the latter can be a time consuming exercise. One simple solution is
to use data that is publicly available on how much of a country�s gross
domestic product comes from exports. In table 2, we list the percentage of the
GDP that comes from exports by region of the world and use it to compute the
percent of GDP that is domestically directed.

###### Table 2: GDP from Exports by Region of the World in 2001

|  |  |  |
| --- | --- | --- |
| Region | Percent of GDP from Exports | Percent of GDP from domestic economy |
| East Asia & Pacific | 61% | 39% |
| Central Asia | 66% | 34% |
| Latin America & Caribbean | 38% | 62% |
| Middle East and N. Africa | 45% | 55% |
| South Asia | 23% | 77% |
| Sub-Saharan Africa | 56% | 44% |

Source: World Bank

The breakdown for individual countries is provided in
appendix 1. According to the World Bank data in this table, Brazil got 23.2% of
its GDP from exports in 2001. If we assume that this is an approximation of
export revenues for the average firm, the average firm can be assumed to
generate 76.8% of its revenues domestically. Using this value would yield
slightly higher betas for both Embraer and Embratel.

#### Accounting Earnings

            As
investors, we are more interested in a company�s earnings than its revenues.
Consequently, an argument can be made that we should be looking at how exposed
a company�s earnings are to country risk. 
In theory, at least, the earnings of a company that is more exposed to
country risk should increase as country risk decreases and decrease as country
risk exposes. There are three practical problems, though, with using accounting
earnings in measuring country risk:

1. Earnings
   often lag changes in the underlying fundamentals at a company. In other
   words, the earnings changes are likely to occur well after the change in
   country risk occurs.
2. Earnings
   can be smoothed out even for companies that are exposed to country risk.
   On the surface, these companies look far safer and less exposed to country
   risk than they truly are.
3. Accounting
   earnings are measured four times a year, at the most, and less often in
   some emerging markets. With the resulting small sample, it may be
   difficult to draw any conclusions.

Consider again Embraer and Embratel. In figure 2, we graph
the percentage changes in quarterly earnings per share for each firm in
Brazilian Real from 1999 to 2002 and compare them to percentage changes in the C-Bond
price each quarter:

if !supportEmptyParas endif

if !vml![](CountryRisk_files/image033.gif)endif  
if !supportEmptyParas endif

  

Note that Embratel earnings are much more sensitive to
country risk than Embraer earnings. In 2002, in particular, Embratel earnings
declined as country risk increased bu Embraer earnings were unaffected.

#### Market Prices

            Unlike
accounting earnings and revenues, which are measured only a few times each year
and lag changes in the firm, stock prices are updated through every trading day
and reflect investor assessments, faulty though they may be sometimes, of the
effects of new information (including changes in country risk). If we can come
up with market measures of country risk, we can measure the sensitivity of a
company�s stock price to country risk to estimate its lambda.

            Bonds
issued by countries offer a simple and updated measure of country risk. As
investor assessments of country risk become more optimistic, bonds issued by
that country go up in price, just as they go down when investors become more
pessimistic. A regression of the returns on a stock against the returns on a
country bond should therefore yield a measure of lambda in the slope
coefficient. Note that this parallels the approach that we often use to get a
company�s beta. The difference lies in the independent variable used, since the
returns on an equity index are used to estimate betas.

            Applying
this approach to Brazil is relatively straightforward. The Brazilian C-Bond,
which we used earlier to get the default spread, is widely traded and returns
on the bond are available going back to 1998. We regressed monthly stock
returns on Embraer and Embratel against monthly returns on the C-Bond and the
resulting graphs are shown in figure 3:

###### Figure 3: Sensitivity to Country Risk: Embraer versus Embratel

if !vml![](CountryRisk_files/image036.gif)endifif !vml![](CountryRisk_files/image039.gif)endif

The regression results are summarized below for the two
companies:

ReturnEmbraer = 0.0195 + 0.2681 ReturnC Bond

ReturnEmbratel = -0.0308 + 2.0030 ReturnC
Bond

Based upon these regressions, Embraer has a lambda of 0.27
and Embratel has a lambda of 2.00. The resulting dollar costs of equity for the
two firms, using a mature market equity risk premium of 4.53% and a country
equity risk premium of 7.67% for Brazil are:

Cost of Equity for Embraer = 4.05% + 1.07 (4.53%) + 0.27
(7.67%) = 10.97%

Cost of Equity for Embratel = 4.05% + 0.80 (4.53%) + 2.00
(7.67%) = 23.01%

            What
are the limitations of this approach? The lambdas estimated from these
regressions are likely to have large standard errors; the standard error in the
lambda estimate of Embratel is 0.35. It also requires that the country have
bonds that are liquid and widely traded, preferably in a more stable currency
(dollar or euro). While there are more country bonds in circulation now, there
are dozens of countries where the data is not available.

### Risk Exposure in Many Countries

            The
discussion of lambdas in the last section should highlight a fact that is often
lost in valuation. The exposure to country risk, whether it is measured in
revenues, earnings or stock prices, does not come from where a company is
incorporated but from its operations. There are U.S. companies that are more
exposed to Brazilian country risk than is Embraer. In fact, companies like
Nestle, Coca Cola and Gillette have built much of their success on expansion
into emerging markets. While this expansion has provided them with growth
opportunities, it has also left them exposed to country risk in multiple
countries.

            In
practical terms, what does this imply? When estimating the costs of equity and
capital for these companies and others like them, we will need to incorporate
an extra premium for country risk. Thus, the net effect on value from their
growth strategies will depend upon whether the growth effect (from expanding
into emerging markets) exceeds the risk effect.

            We
can adapt the measures suggested above to estimate the risk exposure to different
countries for an individual company.

* We can
  break down a company�s revenue by country and use the percent of revenues
  that the company gets from each emerging market as a basis for estimating
  lambda in that market.  While
  the percent of revenues itself can be used as a lambda, a more precise
  estimate would scale this to the percent of revenues that the average
  company in that market gets in the country.
* If
  companies break earnings down by country, these numbers can be used to
  estimate lambdas. The peril with this approach is that the reported
  earnings often reflect accounting allocation decisions and differences in
  tax rates across counties.
* If a
  company is exposed to only a few emerging markets on a large scale, we can
  regress the company�s stock price against the country bond returns from
  those markets to get country specific lambdas.

# Adjusting Cashflows versus Discount Rates

            The
adjustments that we have suggested for country risk so far in this paper have
all been directed at the discount rates � costs of equity and capital. Can we
adjust cashflows for risk? Absolutely, but before we look at how, we should
dispense with some widely held misconceptions about cashflow adjustment:

* Adjusting
  the cashflows to reflect expectations about dire scenarios arising from
  political or economic turmoil is not risk adjustment. For instance, assume
  that you are a company investing in a large telecommunications project in
  China and that you expect to generate $ 1 billion in cashflows each year
  if the economy remains vibrant. However, your risk assessment experts tell
  you that there is a 10% chance of political and economic turmoil, in which
  case you expect to lose $ 500 million a year. You could compute an
  expected cashflow from these inputs:

Expected Cashflow = 1000 (.90) �
500 (.10) = $ 850 million

If you use this expected cashflow
in your analysis, you have not adjusted for risk yet.  All you have done is compute expected cashflows correctly.

* Doing
  Monte Carlo simulations on the cashflows or returns on an investment may
  give you a better sense of the risk in an investment, but they do not
  represent risk adjustments. The expected value across your simulations
  should converge on the expected value that you would have obtained with a
  single, base case analysis, assuming your estimates in the analysis are
  done correctly.
* Arbitrary
  reductions in the cashflows � hair cuts of 10% or 20% to the expected
  cashflows to reflect the fact that they are risky � may yield conservative
  estimates of value but do not represent real risk adjustment.

So, how can we adjust cashflows
for risk? Instead of adding the risk premium to the riskfree rate, as we did in
the earlier sections, we could adjust the expected cashflows for the risk. As
an example, consider the cost of equity that we estimated for Embraer of 10.67%
in the last section, which represents a risk premium of 6.62% over the riskfree
rate.  Assume that you have
projected expected cashflows of $ 200 million for next year and $ 250 million
for the year after for Embraer. The risk adjusted cashflows for these two years
would be:

Risk adjusted cashflow for year 1 = $ 200/ 1.0662 = $187.58
million

Risk adjusted cashflow for year 2 = $ 250/1.06622
= $219.92 million

These cashflows would then be discounted at the riskless
rate to yield almost the same value as you would have obtained with the risk
adjusted discount rate approach.[if !supportFootnotes[14]endif](#_ftn14)

# Conclusion

            As
companies expand operations into emerging markets and investors search for
investment opportunities in Asia and Latin America, the assessment of country
risk has become a central component of valuation.  In this paper, we considered two key questions.

The first is whether there should
be an extra premium assessed for country risk, and if yes how to estimate it.
While it is true that globally diversified investors can eliminate some country
risk by diversifying across equities in many countries, the increasing
correlation across markets suggests that country risk cannot be entirely
diversified away. To estimate the country risk premium, we consider three
measures: the default spread on a government bond issued by that country, a
premium obtained by scaling up the equity risk premium in the United States by
the volatility of the country equity market relative to the US equity market
and a melded premium where the default spread on the country bond is adjusted
for the higher volatility of the equity market. We also estimated an implied
equity premium from stock prices and expected cashflows.

The second question relates to how
this country risk premium should be reflected in the costs of equities of
individual companies in that country. While the standard approaches add the
country risk premium as a constant to the cost of equity of every company in
that market, we argue for a more nuanced approach where a company�s exposure to
country risk is measured with a lambda. This lambda can be estimated either by
looking at how much of a company�s revenues or earnings come from the country �
the greater the percentage, the greater the lambda � or by regressing a
company�s stock returns against country bond returns � the greater the
sensitivity the higher the lambda. If we accept this view of the world, the
costs of equity for multinationals that have significant operations in emerging
markets will have to be adjusted to reflect their exposure to risk in these
markets.

           

if !supportEmptyParas endif

  

**References**

Booth, L., 1999, *Estimating the Equity Risk Premium and
Equity Costs: New Way of Looking at Old Data*,
Journal of Applied Corporate Finance, v12(1), 100-112.

Chan, K.C., G.A. Karolyi and R.M. Stulz, 1992, *Global
Financial Markets and the Risk Premium on U.S. Equity*, Journal of Financial Economics, v32, 132-167.

Dimson, E., P. Marsh and M. Staunton, 2002, *Triumph of
the Optimists*, Princeton University Press

Godfrey, S. and R. Espinosa, 1996, *A Practical Approach
to Calculating the Cost of Equity for Investments in Emerging Markets*, Journal of Applied Corporate Finance, v9(3), 80-81.

Ibbotson and Brinson, 1993, *Global Investing*, McGraw-Hill, New York.

Indro, D.C. and W. Y. Lee, 1997*, Biases in Arithmetic and
Geometric Averages as Estimates of Long-run Expected Returns and Risk Premium*, Financial Management, v26, 81-90.

*Stocks, Bonds, Bills and Inflation*, 1999, Ibbotson Associates

Stulz, R.M., *Globalization, Corporate finance, and the
Cost of Capital,* Journal of Applied
Corporate Finance, v12.

  

###### Appendix 1: Exports as % of GDP in 2001

if !vml![](CountryRisk_files/image042.gif)endif

if !supportFootnotes  

---

endif

[if !supportFootnotes[1]endif](#_ftnref1) Consider the
Brazilian market, where we have about 10 years of reliable historical data on
stock returns since the Real Plan in 1994. With an annualized standard
deviation of about 30% in returns, the standard error in the risk premium,
using 10 years of data, is about 10%.

[if !supportFootnotes[2]endif](#_ftnref2) See �Triumph
of the Optimistis� by Dimson, Marxh and Staunton.

[if !supportFootnotes[3]endif](#_ftnref3)The process
by which country ratings are obtained in explained on the S&P web site at
http://www.ratings.standardpoor.com/criteria/index.htm.

[if !supportFootnotes[4]endif](#_ftnref4) You cannot
compare interest rates across bonds in different currencies. The interest rate
on a peso bond cannot be compared to the interest rate on a dollar denominated
bond.

[if !supportFootnotes[5]endif](#_ftnref5) The polls
throughout 2002 suggested that Lula who was perceived by the market to be a
leftist would beat the establishment candidate.  Concerns about how he would govern roiled markets and any
poll that showed him gaining would be followed

[if !supportFootnotes[6]endif](#_ftnref6) If the
dependence on historical volatility is troubling, the options market can be
used to get implied volatilities for both the US market (about 20%) and for the
Bovespa (about 38%).

[if !supportFootnotes[7]endif](#_ftnref7)
Jeremy Siegel reports on the standard deviation in equity markets in his book
�Stocks for the very long run� and notes that they tend to decrease with time
horizon.

[if !supportFootnotes[8]endif](#_ftnref8) We used the
average of the analyst estimates for individual firms (bottom-up).
Alternatively, we could have used the top-down estimate for the S&P 500
earnings.

[if !supportFootnotes[9]endif](#_ftnref9) The treasury
bond rate is the sum of expected inflation and the expected real rate. If we
assume that real growth is equal to the real  interest rate, the long term stable growth rate should be
equal to the treasury bond rate.

[if !supportFootnotes[10]endif](#_ftnref10) We have
deviated from our rule of setting the stable growth rate equal to the riskfree
rate, because real growth in Brazil is likely to be slightly higher than real
growth in mature economy like the United States.

[if !supportFootnotes[11]endif](#_ftnref11) The input
that is most difficult to estimate for emerging markets is a long term expected
growth rate. For Brazilian stocks, I used the average consensus estimate of
growth in earnings for the largest Brazilian companies which have ADRs listed
on them. This estimate may be biased, as a consequence.

[if !supportFootnotes[12]endif](#_ftnref12) We used a
bottom-up beta for Embraer, based upon an unleverd beta of 0.95 (estimated
using aerospace companies listed globally) and Embraer�s debt to equity ratio
of 19.01%. For more on the rationale for bottom-up betas read the companion
paper on estimating risk parameters.

[if !supportFootnotes[13]endif](#_ftnref13) The average
inflation rate in Brazil between 1998 and 2003 was 7.13%.

[if !supportFootnotes[14]endif](#_ftnref14) If you want
the same value, the risk premium you use will be slightly different and
computed thus:

Risk premium to adjust cash flows =  6.37%
