---
title: "January 2018 Data Update 4: The Currency Conundrum"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-4-currency.html
published: 2018-01-24
updated_source: 2018-02-06
fetched: 2026-08-27
tags:
  - Risk free Rates
---

# January 2018 Data Update 4: The Currency Conundrum

_Source: [https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-4-currency.html](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-4-currency.html) — published 2018-01-24_

96

Normal
0

false
false
false

EN-US
X-NONE
X-NONE

/* Style Definitions */
table.MsoNormalTable
{mso-style-name:"Table Normal";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-parent:"";
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-para-margin:0in;
mso-para-margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"Calibri",sans-serif;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin;}

There is perhaps no more mangled nor misunderstood part of financial analysis than the handling of currencies, and globalization has only made the problems worse. From the laziness of assuming that government bond rate in a currency is always the risk free rate in that currency, to nonsensical notions like a global risk free rate, to bad practices like discounting peso cash flows with dollar discount rates, the list of currency sins is long. In this post, I look at three of the most common misconceptions related to currencies and use them to update currency related numbers at the start of 2018.

96

Normal
0

false
false
false

EN-US
X-NONE
X-NONE

/* Style Definitions */
table.MsoNormalTable
{mso-style-name:"Table Normal";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-parent:"";
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-para-margin:0in;
mso-para-margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"Calibri",sans-serif;
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin;}

**Misconception 1: Governments are Default Free (when they borrow in the local currencies)**

I was taught, in my first finance class, to use the US treasury bond rate as the risk free rate, when estimating expected return, reflecting the dollar-centric world of my MBA studies. The notion, though, that the government bond rate, denominated in the local currency, is the risk free rate in that currency persists, albeit expanded to include other currencies. Thus, we are told to use the Brazilian Government $R bond as the $R risk free rate and the Indian Rupee Government bond rate as the Indian Rupee risk free rate. Its proponents argue that governments control the printing of money and hence never have to default, but what they fail to note is that in the last three decades, a significant [proportion of all sovereign defaults have been local currency defaults](https://www.cass.city.ac.uk/__data/assets/pdf_file/0009/219978/120.-Jeanneret-v2.pdf); of the 58 sovereign defaults between 1996 and 2012, 31 were in the local currency. As to why countries would choose to default in the local currency, when they can print enough money to pay off debt, the answer is straight forward. Printing more money debases your currency, and countries, faced with a choice between defaulting and debasing their currencies, often conclude that default is a better option.

So what if sovereigns default on local currency bonds? If a sovereign entity (or government) can default on local currency debt, it stands to reason that the rate on a bond issued by it is no longer a risk free rate. Using that government bond rate, as if it were a risk free rate, can lead to the double counting of risk, especially if analysts use a higher equity risk premium to capture additional country risk. For instance, consider the Nigerian Naira 10-year government bond, trading to yield 14.12% on January 1, 2018. If that rate is used as the risk free rate in Naira for a Nigerian company, in conjunction with a high equity risk premium for Nigeria, you are counting risk twice in your computation, once in your “risky” risk free rate and again in your equity risk premium.  To avoid double counting, you have to cleanse the government bond of default risk and to do so, you have to estimate how much of the interest rate on the bond can be attributed to default risk. There are three ways that you can estimate this default spread, though they all come with a catch.

- Government Bond Spread: The first is to find a US dollar or Euro government bond issued by the sovereign in question and to net out the US Treasury Bond rate or the German Euro bond rate as the risk free rates. 

- Sovereign CDS Spread: The second is to observe the sovereign Credit Default Swap on the sovereign in question, which is a measure of the default spread of the sovereign. 

- Local Currency Rating: The third is to use the sovereign rating estimated by S&P, Moody’s or Fitch for a country and to estimate the typical spread at which other bonds with the same rating trade at. 

With the Nigerian Naira, for instance, you have two choices for the default spread; the first is the sovereign CDS spread for Nigeria, which on January 1, 2018, was 4.68% and the second was the 5.64% spread associated with Nigeria's local currency rating of B2 (from Moody's). Using the latter estimate would yield a risk free rate of 8.48% for the Nigerian Naira:

Risk free Rate in Nigerian Naira (1/1/18) = 14.12% - 5.64% = 8.48%

The problem with all these spreads is that they are dollar-based, not local currency-based, and netting these spreads out from the local currency government bond can create an inconsistency. 

This process of estimating risk free rates in different currencies requires the presence of local currency long term government bonds, a requirement that is met by less than fifty currencies at the start of 2018. I used the sovereign ratings to extract default spreads (the third approach described in the last paragraph) and estimated risk free rates in those currencies in the chart below: 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7SyiDKWe1_VJajIOa9V5TDeIOgqMkrmPb15JaQwvC1yl6wPUBzuiaAuv6QmOAyp2dGMzAjYC2fG8n5djKkUM6qoo7rHXTSSrbXM55TAEoc6gi8tJ2ZhauTdSicAJ3isQvj9Mwk50mj7E/s1600/CurrencyRiskfree.png)
[Download spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/currencyriskfree2018.xlsx)

There are three obvious points to make. The first is that risk free rates vary across currencies, ranging from less than zero in a handful of currencies (Yen, Swiss Franc, Croatian Kuna) to more than 8% in  others (Nigerian Naira, Turkish Lira and the Venezuelan Bolivar). The second is that for the risk free rates that are negative, it is either because the government bond rate was negative (Swiss Franc or Japanese Yen) or because of the netting out of the default spread from the government bond rate (Croatian Kuna and Hungarian Forint). The third is quality of precision of the risk free rate you get in a currency is only as good as the government bond rate that you start the process with. To the extent that some of the government bond rates on my list do not represent traded bond rates but are government set or manipulated, the rates that emerge from them are flawed. For instance, I don't, for a moment, believe that the risk free rate in Venezuelan Bolivar is less than 10%.

**Misconception 2: There is a Global Risk Free Rate **

It is perhaps understandable that an analyst who looks at the differences in rates across currencies, before or after adjusting for default risk, will conclude that since the risk free rate is the lowest of the rates at which an entity can borrow money, the lowest of the rates across currencies, perhaps the Swiss Franc or the Japanese Yen, is the global risk free rate and that all other currencies are risky. That is a dangerous delusion, since there is a simple reason why risk free rates vary across currencies. The risk free rate in a currency is a reflection of expected inflation in that currency, and risk free rates will be higher in high-inflation currencies than in low-inflation ones, and can become negative in deflationary currencies. There are three implications that follow:

*1. You cannot blend multiple currencies in the same analysis/valuation*: When valuing a company that has operations in many countries and derives its revenues in multiple currencies, you cannot create blended averages of risk free rates or growth rates in different currencies. Doing so would be akin to averaging the temperature in New York (measured in fahrenheit) with the temperature in Frankfurt (measured in celsius) to arrive at an average temperature for the two cities. 

*2. If you can estimate the expected inflation rate in a currency, you can estimate a risk free rate in that currency*: In fact, the risk free rate in a currency can simply be stated as the sum of the expected inflation rate in that currency and the real interest rate. If you are willing to buy into the notion that the real interest rate around the globe should converge on a  single number (as would be the case, if capital could flow easily across markets), the risk free rate in any currency can then be estimated by using the differential inflation rate between that currency and one where a risk free rate is observable (like the US dollar or the Euro).

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7R2AzrFOvhPt7HPLfu2TQTqaUsFdralUB3iyZLXJzj-dU6VeMu3MS0jt1AJowf0spQq7z4ZEESYh6_UnKcYsJtTzKuDZmQLffUmutxn4KQ-Teu02qfZGbrMDPsziGUO8RnsFXSKrTwA8/s1600/CurrencyRiskfreeLongWay.jpg)

Note that there is an approximate version of this rate that can be obtained by adding the differential inflation rate to the US dollar risk free rate. If the risk free rate in US dollars is 2.41%, the expected inflation rate in the US is 1.75% and the expected inflation in India is 6%, the risk free rate in Indian rupees can be written as follows;

Approximate form = 2.41% + (6% - 1.75%) = 6.66%

Precise version = (1.0241) (1.06/1.0175) -1 = 6.68%

There are two advantages to the differential inflation approach. The first is that it does not assume that the government bond is traded and it does not have to deal with the currency mismatch of default spreads in US dollars being netted out against local currency bond rates. The second is that this approach can be extended to almost all currencies, since it is built around expected inflation. I have used IMF estimates of expected inflation in currencies to derive local currency risk free rates in more than 150 currencies in [the linked dataset](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryInflationRates.xlsx). Incidentally, using expected inflation rates yields a risk free rate in Venezuelan Bolivar of 3814%, a much more believable number given the hyper inflation in that country.

3. Pegged exchange rates may be a delusion: There are some currencies that are pegged to the US dollar and for analysts working with these currencies, it has become standard practice to use the US treasury bond rate as the risk free rate in the currency. The danger, though, is that governments that peg currencies can also unpeg them and the differential inflation approach yields a way of finding out when you should worry. If you have a currency pegged to the US dollar, but the inflation rate in that currency is 4% higher than the US dollar, it is only a question of time before the peg will break. In such cases, it may be prudent to replace the US treasury bond rate with a calculated risk free rate, using the differential inflation. (*Warning to Middle Eastern analysts: This will cause a significant markdown in value for your Saudi and Emirate equites, but..*)

**Misconception 3: Currency Choice can drive your valuation**

When valuing a company, analysts often default to valuing it in the local currency, but currency is a choice. I can value Severstal, a Russian steel company, in Russian rubles, US dollars or Euros. At first sight, the fact that risk free rates are lower in US dollars and Euros, relative to the ruble, may seem to suggest that you could inflate Severstal’s value, by switching the valuation currency from rubles to dollars, but you will not. The answer to why lies in the last section, where we noted that risk free rates vary across currencies, because of differential inflation, and tying it in with a simple consistency rule in valuation and capital budgeting: if the cash flows in an analysis are forecast in a specific currency, the discount rate used has to be in the same currency. Consequently, if you value Severstal in Euros, instead of rubles, it is true that your discount rate will be lower (because inflation in the US dollar is lower than in rubles) but it is also true that your cash flows will also grow at lower rates, for the same reason. This is captured in the picture below: 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaKK5UZ-V37AMQuVrIsFALz7euZt0iHdtwk5yz1O7FnUc9gbkiPPXBqj5XfmmoGRic2ApanH7M8fmoxVqup0iOaP5173b0uigiL1wQ-CXfz2ZKN1YDkYtMLPia56ObE-vSOSweAE-hdo8/s1600/DCF%2526CurrencySimple.jpg)

The proposition that the value of a company should not be a function of the currency that you choose to value that company should also cast as a lie the notion that using an emerging market currency in a valuation brings additional risk into a valuation. If Severstal is a riskier company because of its Russian roots, and it is, that risk premium should be part of the discount rate estimated in US dollar or ruble terms. 

The other push back that you will get is that your views on a currency can cause the value estimated in that currency can diverge. For instance, if you expect the Brazilian Reai to appreciate against the US dollar for the next few years, the value of Embraer will be higher, estimated in $R than in US$. While that is true, the reason for the divergence has nothing to do with the use of the currency and everything to do with bringing your currency views into your valuation. Thus, if the value of Embraer is 20% higher, when you value it in $R than in US$, that 20% difference is entirely due to your view that the $R will strengthen, which if true, you can profit from in simpler and more direct ways than buying Embraer.

One of the most common and deadly mistakes in valuation is mixing different currencies in the same valuation. Valuing an Indian company, by projecting the cash flows in rupees and discounting those cash flows at a US dollar cost of capital, will result in too high a value, since the inflation rate in US$ is significantly lower than the inflation rate in rupees. While that may seem like an obvious mistake, and one easy to avoid, it happens because we are often not explicit about currencies when making estimates. Thus, a US company that estimates a dollar cost of capital for acquiring an Indian company and then obtains expected growth rates for the cash flows from the managers of the Indian company, who naturally think in rupee terms, is setting itself up for the mismatch. 

**Conclusion **

If there are lessons to be learned from looking at the dangers of mixing currencies, it is that it is time that we stopped being casual about the currencies that we measure and use in our analysis. At the risk of sounding pedantic, we should never estimate a growth rate, without being explicit about what currency that growth rate is estimated in, or talk about cash flows, without thinking about the inflation that we have embedded in them. 

**YouTube Video**

**
**
**Datasets/Spreadsheets**

- [Riskfree Rate Estimator (Spreadsheet for estimating riskfree rates)](http://www.stern.nyu.edu/~adamodar/pc/Riskfreecalc.xls)

- [Riskfree Rates in Currencies (using Local Currency Government Bonds)](http://www.stern.nyu.edu/~adamodar/pc/blog/currencyriskfree2018.xlsx)

- [Riskfree Rates in Currencies (using Differential Inflation Rates)](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryInflationRates.xlsx)

**Data Update Posts**

- [January 2018 Data Update 1: Numbers don't lie, or do they?](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-1-numbers-dont.html)

- [January 2018 Data Update 2: The Buoyancy of US Equities!](http://bit.ly/2FmB13Z)

- [January 2018 Data Update 3: Taxing Questions on Value](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-3-taxing.html)

- [January 2018 Data Update 4: The Currency Conundrum](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-4-currency.html)

- [January 2018 Data Update 5: Country Risk Update](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-5-country-risk.html)

- [January 2018 Data Update 6: A Cost of Capital Primer](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-6-cost-of.html)

- [January 2018 Data Update 7: Growth and Value - Investment Returns](https://aswathdamodaran.blogspot.in/2018/01/january-2016-data-update-7-growth-and.html)

- [January 2018 Data Update 8: Debt and Taxes](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-8-debt-and.html)

- [January 2018 Data Update 9: Dividends, Buybacks and Cash Holdings](https://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-9-dividends.html)

- [January 2018 Data Update 10: The Price is Right!](https://aswathdamodaran.blogspot.com/2018/02/january-2018-data-update-10-price-is.html)
