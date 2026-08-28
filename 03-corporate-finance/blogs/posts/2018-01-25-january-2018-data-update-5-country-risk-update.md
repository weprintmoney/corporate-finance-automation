---
title: "January 2018 Data Update 5: Country Risk Update"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-5-country-risk.html
published: 2018-01-25
updated_source: 2018-02-06
fetched: 2026-08-27
tags:
  - Country Risk
  - Equity Risk Premiums
---

# January 2018 Data Update 5: Country Risk Update

_Source: [https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-5-country-risk.html](https://aswathdamodaran.blogspot.com/2018/01/january-2018-data-update-5-country-risk.html) — published 2018-01-25_

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

In [my last post](https://aswathdamodaran.blogspot.in/2018/01/january-2018-data-update-4-currency.html), I looked at the currency confusions that globalization has brought into financial analysis, and how to clean up for them. In this post, I discuss the other aspect of globalization that is forcing analysts to change long accepted practices in estimating equity risk premiums for companies. Taking what they have learned from finance textbooks blindly, practitioners have taken what they learned about equity risk premiums to emerging and frontier equity markets, often with disastrous results. Not only have they practiced denial when it comes to the additional risk that investors face in many markets, from political, economic and legal sources, but they have also considered risk by looking at where a company is incorporated, instead of where it does business. In this post, I will update my country risk measures for the start of 2018, and build on them to measure the equity risk premiums for companies.

**
**

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

**Country Default Risk****

The more widely measured and accessible measures of sovereign
risk are related to sovereign default, and as we noted in the post on currency
risk free rates, there are three ways in which default risk in countries can be
measured. The first is to use government bonds, denominated in US dollars or Euros, issued by sovereigns and to compare the rates on these bonds to a US treasury or German Euro bond rate. The second is to
use the sovereign CDS spreads for countries, market-driven numbers, as default
risk measures. The third is to use the sovereign ratings of countries as proxies of default risk and to convert these ratings to default spreads. 

*1. Sovereign
Rating/Spread*

The leading ratings agencies including S&P, Moody’s and
Fitch have long since expanded their business of rating bonds for default risk
from corporations to looking at entire countries. These “sovereign”
ratings are estimated on both foreign currency and local currency terms, with
the ratings spectrum ranging from Aaa to D, just as with corporate bonds. One way of capturing the default risk variations across the
world is with a heat map, based upon local currency sovereign ratings:

via [chartsbin.com](http://chartsbin.com/view/46406)

Note that while there are clear differences across regions,
with Latin America and Africa containing more risky (red) areas than Europe and
North America, there are also differences within regions. You can download the S&P and Moody's ratings, by country, at the start of 2018, by [clicking on this link](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryRiskAll.xlsx).

*2. Sovereign CDS
Spreads*

While sovereign ratings provide accessible measures of
default risk in countries, they come with limitations. The ratings agencies are
not only sometimes wrong in their default risk assessments, but they are often
late in reassessing default risk (and sovereign ratings), when conditions
change quickly in countries. It is these weaknesses that are remedied, at least partly, by the sovereign
credit default swap (CDS) market, where investors can buy insurance against sovereign
default. The market-set prices for sovereign credit default swaps provide updated
measures of default risk, at least for the 70 countries that they exist for,
and the levels of these spreads are in the table below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkIC8NiewyU2H2mcK8FxTKLnEQiWnoybGsb1UWRLscS9cVaoHrOdQrk5YOczy8DuiPT4f7UmtzWdwV4b5R2r787g5BteuY3qFDEHmN0Li06VI_aI8C7lFdQbtbl_l9HME6b8YO3LN0et8/s1600/SovrCDSPicture.png)
[Download spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryRiskAll.xlsx)

I don’t want to oversell these CDS spreads as better proxies
of default risk. While they are certainly more dynamic and reflective of
current risk that sovereign ratings, they are market numbers and like all
market numbers, they are volatile and reflect market mood and momentum, as much
as they do fundamentals.

**Country Equity Risk****

Sovereign or country equity risk measures are more difficult
to come by than sovereign default spreads. First, there are services that try
to measure the political and economic risk in countries with scores, albeit
with no standardization. Second, the default risk measures can be converted
into equity risk measures by scaling them for the additional risk in equities.

*a. Risk Scores*

The World Bank, Political Risk Services (PRS) and the
Economist, among others, try to measure the total risk in countries. Those
scores have no standardization and cannot be compared across services, but they still represent
more comprehensive measures of risk than sovereign ratings or CDS spreads. In
the heat map below, you can see the country risk scores reported by PRS, with higher scores indicating lower risk.

via [chartsbin.com](http://chartsbin.com/view/46407)

Comparing this picture to the sovereign ratings map, there are
clearly overlaps, where the country risk scores from PRS and the ratings
deliver the same message; Latin America, Eurasia and Africa remain high risk zones and European
countries have lower risk. 

*b. Equity Risk
Premiums*

The problem with risk scores is that they cannot be easily
converted into risk premiums to use in cost of equity calculations. It is to
overcome this problem that I return to sovereign default spreads, not as
measures of equity risk, as is often the practice, but to use them as starting points
for measuring the equity risk in countries. In particular, I estimate the
relative equity market volatility, computed by scaling the volatility or
standard deviation in equity to the standard deviation of government bond, and use
that to scale up sovereign default risk to sovereign equity risk:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfX6E1ACTVORZ0aDkXkxbD1o43bwLMRhOEUlMMYCAQ2pJx7I-0dy43f94Zo-ZMxwVO9sTVBOi3vE23qXlFg4joOjQAEJUCu8RSZWZ3Aa6Oqrunsb2CBU_GpXNtICxP0lWZaElUp4vaKoQ/s1600/ERP+equation+for+country.jpg)

Using this approach does require traded government bonds, available for only a handful of countries. To generalize this approach, I use the ratio of the volatility in an emerging market equity index to the volatility of an emerging market government bond index, using the most recent five years of data. That ratio, which is 1.12 at the start of January 2018, is used to convert sovereign default spreads to country risk premiums. 

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhI-oeaWTW6PvOVSIKn9NhWyEksdO3xPCE2SaTdeeLBH94zGrxSJO-0ndnG0pnggMveXxalEvhNtj8A94iGnDYSunuEscdLpvuokO1rpabAPrkinjmQem9vEcKj9vQyUzr6_ylDpAvQ33w/s1600/ERP+computation+picture.png)

These country risk
premiums, when added to the implied US equity risk premium of 5.08%, yield
equity risk premiums for countries. The picture below summarizes equity risk premiums around the world.

via [chartsbin.com](http://chartsbin.com/view/46409)

If the heat map does not provide enough specifics, this picture may be better:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgC4Bhubk8VSeKcnrMnQVae8lBLMgFGeiVaECv32MfFiGJCTM_2diDkEmcmEh2f_ZRWMzaaQkotpRSRiNbYKqNRSFnfwYsHJZpHJYvDDcvPXfbbEZ4BH9hAkXxpqB9lpOHC3VOjK0xxDgU/s1600/ERPGlobal.png)

Finally, if you prefer the data as a table, you can [download the spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryRiskAll.xlsx) with the data or my [more detailed country risk premium dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls). 

**Company Equity Risk**

A company's risk does not come from where it is incorporated, but where it does business. If we adopt this perspective, it is clear that to value a company, you need to see its risk exposure to different countries, either because it has its production and operations in those countries or because it sells its products or services there. That risk exposure, in conjunction with the equity risk premiums of the countries estimated in the earlier section, can be used to compute the company's equity risk premium. To illustrate this concept, consider LATAM, the Chile-based airline. To compute its equity risk premium, I would compute the weighted average of the countries that LATAM derives revenues from which includes most of Latin America and the US. For companies like Coca Cola, which may be in too many countries for this approach to be easily applied or where the country breakdowns are not available, you can use regional equity risk premiums. In the table above, I report on the GDP-weighted average ERP for regions of the world. If you accept this rationale, the following implications follow:

- A company cannot change its risk profile by delisting in one market and resisting in another: It is a common play for emerging market companies to delist on their "risky" local markets and to re-list on a more developed markets. While there are some good reasons for doing so, which can potentially increase value, like increased liquidity and transparency, one reason that does not stand up to scrutiny is that the company has become safer, just because of the listing change. A South African mining company that delists in Johannesburg and lists on the London Stock Exchange is still exposed to South African country risk, after the move.

- A company's equity risk premium should change, as its geographic exposure changes: In estimating the equity risk premium for a company today, we need to consider where it operates today. If we expect that geographic mix to change over time, as it usually will, the equity risk premium that we use in future years should reflect these expected changes. And yes, that will mean that your cost of equity and capital can change over time. Welcome to globalization!

- When multinationals assess projects, their hurdle rates should vary across geographies: When multinationals assess hurdle rates for projects, those hurdle rates should vary, depending upon where a project will be, even if the hurdle rates are estimated in the same currency. Thus, the US dollar cost of equity that Coca Cola should use for a Canadian beverage expansion should be far lower than the US dollar cost of equity for a Russian investment.

It is a pity that accounting disclosure requirements have been so focused on trivial matters that have little effect on value and have not really paid attention to the type of information companies should be disclosing to investors on geographic operations.

**Conclusion**

If, as the Chinese symbol ([危机](https://en.wiktionary.org/wiki/%E5%8D%B1%E6%9C%BA)) for crisis suggests, danger plus opportunity equals risk, it is not surprising that the most risky parts of the world also often provide the most potential for growth. By demanding higher equity risk premiums for investing in these parts of the world, I am not suggesting that you hold back from investing in these risky regions, but only that you demand enough of a premium for exposing yourself to additional risk. After all, investing should never be bungee jumping, where you take risk for the sake of taking risk!

**
YouTube Video**

**Datasets**

- [Country Ratings, PRS scores and Equity Risk Premiums (January 2018)](http://www.stern.nyu.edu/~adamodar/pc/blog/CountryRiskAll.xlsx)

- [Equity Risk Premiums, by Country - Detailed (January 2018)](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xls)

- [Company Risk Premium Calculator (Spreadsheet)](http://www.stern.nyu.edu/~adamodar/pc/CompanyERP.xls)

**Papers**

- [Country Risk Premiums: Data, Measures and Implications, A 2017 Update (Last version from July 2017)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3000499)

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
