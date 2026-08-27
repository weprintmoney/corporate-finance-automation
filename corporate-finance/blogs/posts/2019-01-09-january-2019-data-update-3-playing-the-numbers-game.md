---
title: "January 2019 Data Update 3: Playing the Numbers Game!"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2019/01/january-2018-data-update-3-playing.html
published: 2019-01-09
updated_source: 2019-02-27
fetched: 2026-08-27
tags:
  - Data Update
---

# January 2019 Data Update 3: Playing the Numbers Game!

_Source: [https://aswathdamodaran.blogspot.com/2019/01/january-2018-data-update-3-playing.html](https://aswathdamodaran.blogspot.com/2019/01/january-2018-data-update-3-playing.html) — published 2019-01-09_

Every year, for the last three decades, I have spent the first week of the year, looking at numbers. Specifically, as the calendar year ends, I download raw data on individual companies and try to decipher trends and patterns in the data. Over the years, the raw data has become more easily accessible and richer, but ironically, I have become more wary about trusting the numbers. In this post, I will describe, in broad terms, what the data for 2019 looks like, in terms of geography and industry, and spend the next few posts eking out as much information as I can out of them.

**The Data: Geography**

My sample includes all publicly traded firms with a market capitalization greater than zero and all of the information that I get from my data providers is in the public domain. Put differently, for an individual firm, you should be able to extract all of the information that I have for the firms in my sample, and compute the statistics and ratios that I do, if you are so inclined. If you are wondering why I don't screen out firms that have small market capitalizations or are in markets where information disclosure is spotty, it is because any sampling choices that I make to restrict my sample will create biases that may skew the statistics.

For my 2019 data update, I have 43,846 firms in my sample. While these companies are incorporated in 148 countries, I classify them broadly into five geographical groups:

table.tableizer-table {
font-size: 12px;
border: 1px solid #CCC;
font-family: Arial, Helvetica, sans-serif;
}
.tableizer-table td {
padding: 4px;
margin: 3px;
border: 1px solid #CCC;
}
.tableizer-table th {
background-color: #104E8B;
color: #FFF;
font-weight: bold;
}

Geographical Grouping

Includes

Rationale

Australia, NZ and Canada

Australia, New Zealand and Canada

Share a reliance on natural resources.

Developed Europe

EU, UK, Switzerland and Scandinavia

Includes riskier EU countries, but reflects European company pricing and choices.

Emerging Markets

Asia other than Japan, Africa, Middle East, Latin America, Eastern Europe & Russia

A really mixed bag of countries from many regions with different characteristics, with variations in added risk.

Japan

Japanese companies

Different enough from the rest of the world that it still deserves its own grouping.

United States

US companies

Accounts for the biggest chunk of world market capitalization.

I will confess up front that there is an element of arbitrariness to this classification, but no classification will ever be immune to that subjectivity.  The breakdown of my sample both in terms of numbers of firms and market capitalization is below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6Eh3lnSZCgWOUPqvHKQz9iNX2gHlbM4cnC9uS0HCqtyBVHxmQOI4PS6Cv4z_MNjw41d2mjATS3u0ZakVYspPRCQaUu_U7v-wvlmyP6CYGuIHGGyMt5kv31NyTYG40H1x-4u51_Y7NxdQ/s1600/Geography.jpg)

US firms are still the leaders in the market capitalization race, accounting for 38% of overall market value. While emerging market firms account for roughly half the firms in my overall sample, their market capitalization is 30% of the overall global market capitalization. The emerging market grouping includes firms from four continents, listed in countries that range in risk from low risk to extraordinarily high risk. The two biggest emerging markets, in terms of listings and market capitalization, are India and China and I will break out companies listed in those countries separately for computing my numbers.

**The Data: Industry Groupings**

To classify companies into industrial groups, I start with the industry listings provided by my raw data providers but add my own twist to create industry groupings. One reason that I do so is to respect my raw data providers' proprietary classifications and the other is to compare across time, since I have classified firms with my groupings for decades. In making my classifications, I will err on the side of broader classifications, rather than narrower one, for two reasons:

- Law of large numbers: The power of averaging gets stronger, as sample sizes increase, and using broader groupings results in larger samples. To illustrate, I have 1148 apparel firms in my global sample, thus allowing for enough firms in every sub grouping. 

- Better measures: In both valuation and corporate finance, there is an argument to be made that the numbers we obtain for broader groups is a better estimate of where companies will converge than focusing on smaller groups. 

That said, there will be times where the broad industry classifications that I use will frustrate you, especially on pricing metrics, like PE ratios and EV to EBITDA multiples. I report the industry average PE ratios and EV to EBITDA multiples for specialty retailers collectively, but if you are valuing a luxury retailer, you would have liked to see these averages reported just for luxury retailers. I apologize in advance for that, but the consolation price is that if you want to compute an average across a small sample of companies just like yours, the data to do so is available online and often for free. 

In sum, I break companies down into 94 industries and you can see the numbers of firms and market capitalizations of each industry in this file. The ten biggest industries, at the start of 2019, based upon the number of publicly traded firms and market capitalization are reported below:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyTh19krlsnZuDWCwQDLf-ciUfL6e-FsUryyRRh8Vkv0pJ1So5oHUEYz9vjgf26C8EgwB2gYZ1msNWM5ApTfI0nhzTnNZlD0KgpcYd5bcmQDiOPwChuIgcYQKqdIi0D7CgFpP_voF3FGY/s1600/largest+industries.jpg)
[Download full list of industries](http://www.stern.nyu.edu/~adamodar/pc/blog/IndustryGroupNumbers.xlsx)

While I used to provide company level data until 2015, my raw data providers have put restrictions on that and I can no longer do that. If you are interested in finding out which industry grouping a specific company that you are interested in belongs to, you can find out by [downloading this file](http://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xlsx). Finally, I separate financial service firms from the rest of the sample in computing my market-wide statistics, simply because they are so different that including them will skew the numbers. You can see for yourself how much of a difference this makes.

**The Data: Statistics**

*Timing*

I download data from both accounting statements and financial markets and in doing so, I do run into a mild timing issue. The accounting data that I have for most firms on January 1, 2019, is as of the third quarter of 2018 (ending September 30, 2018) and I use the trailing 12-month data as of the most recent financial filing. For companies in countries with semi-annual filings, the data will be even mow dated, but there is little that can be done about that. For market data, I use the market prices and rates, as of December 31, 2018. While you may think of that as a timing inconsistency, I do not, since that is most updated information an investor would have had on January 1, 2019.

*Adjustments*

With the accounting information, I use my discretion to change accounting rules that I believe not only make no sense but skew our perspectives on companies. The first adjustment that I make is to convert lease commitments to debt, which alters operating income and debt numbers, a modification that I have made for more than 20 years. I am pleased to note that accounting will finally come to its senses and try to do the same starting in 2019 and you should be able to get a preview of how margins, debt ratios and returns on capital will change from my computations. The second adjustment is to convert R&D expenses from an operating expense (which it clearly is not) to a capital expense, which it clearly is, again affecting operating income and invested capital. For purposes of transparency, I report both the adjusted and the unadjusted numbers for the statistics that are affected by it.

*Statistics and Ratios*

Since my interests lie in corporate finance, valuation and investment management, I compute a wide range of statistics, as can be seen in the table below (reproduced from last year). :

Risk MeasuresCost of FundingPricing Multiples

1.     [Beta](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html)1.     [Cost of Equity](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wacc.html)1.     [PE &PEG](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/pedata.html)
2.     [Standard deviation in stock price](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html)2.     [Cost of Debt](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wacc.html)2.     [Price to Book](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/pbvdata.html)
3.     [Standard deviation in operating income](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html)3.     [Cost of Capital](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wacc.html)3.    [EV/EBIT, EV/EBITDA and EV/EBITDA](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/vebitda.html)
4.     [High-Low Price Risk Measure](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html)4.     [EV/Sales and Price/Sales](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/psdata.html)
**Profitability****Financial Leverage****Cash Flow Add-ons**
1.     [Net Profit Margin](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/margin.html)1.     [D/E ratio & Debt/Capital (book & market)](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/dbtfund.html) (with [lease effect](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/leaseeffect.htm))1.     [Cap Ex & Net Cap Ex](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/capex.html)
2.     [Operating Margin](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/margin.html)2.     [Debt/EBITDA](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/dbtfund.html)2.    [Non-cash Working Capital as % of Revenue](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/wcdata.html)
3.     [EBITDA, EBIT and EBITDAR&D Margins](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/margin.html)3.     [Interest Coverage Ratios](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/dbtfund.html)3.     [Sales/Invested Capital](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/capex.html)
**Returns****Dividend Policy****Risk Premiums**
1.    [Return on Equity](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/roe.html)1.     [Dividend Payout & Yield](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/divfund.html)1.     [Equity Risk Premiums](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/ctryprem.html) (by country)
2.     [Return on Capital](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/fundgrEB.html)2.     [Dividends/FCFE & (Dividends + Buybacks)/ FCFE](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/divfcfe.html)2.     [US equity returns (historical)](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/histretSP.html)
3.     [ROE - Cost of Equity](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/EVA.htm)
4.     [ROIC - Cost of Capital](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/EVA.htm)

You can click on the links to see the US data for the start of 2019, in html, but I would strongly recommend that you download the data in Excel from [my data page](http://www.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html). You will not only get data that is easier to work with but you can also download the data for the global sample and geographical groups (as well as India and China).

**The Data: Use**

It would be presumptuous of me to tell you how to use data, since that is a personal choice, but having worked with this data for almost 30 years, I can offer you some caveats:

- Don't assume that mean reversion is automatic: A great deal of valuation and investment management is built on the presumption that mean reversion will occur. Thus, low PE stocks will deliver high returns, as the PE converges on the average for the sector. While mean reversion is a strong force, it is not immutable, and when you have structural changes in the economy and sectors, it will break down. 

- Trust, but verify: While I would like to believe that my computations of widely used ratios (from accounting ratios like return on equity and ROIC to pricing metrics like EV to EBITDA) are correct, they represent my views and may differ from yours. It is for this reason that I provide a full listing of [how I compute my numbers at this link](http://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/variable.htm). If you do find a statistic that I report that you are not clear about, and you cannot find the description of how I computed it, please let me know.

- The data will age, and some more quickly than others, over the course of the year: I have neither the interest, nor the inclination, to be a full-fledged data service. So, please don't expect daily, weekly or monthly updates of the data. In fact, God willing, the data will be updated a year on January 5, 2020. The only numbers that I plan to update mid year are the country risk premiums.

I hope that you find my data useful in whatever you pursue, and if you do use it, you are welcome to it. I find that sharing data that I will need and use anyway costs me nothing, and the only thing that I will ask of you is that you pass on the sharing.  

**YouTube Video**

**Data links**

- [Sample breakdown- Industry Groups](http://www.stern.nyu.edu/~adamodar/pc/blog/IndustryGroupNumbers.xlsx)

- [Company lookup](http://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xlsx)

- [Current Data page on my website](http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html)

**January 2019 Data Updates**

- [Data Update 1: A Reminder that equities are risky, in case you forgot!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-1-reminder.html)

- [Data Update 2: The Message from Bond Markets](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-2-message-from.html)

- [Data Update 3: Playing the Numbers Game](https://aswathdamodaran.blogspot.com/2019/01/january-2018-data-update-3-playing.html)

- [Data Update 4: The Many Faces of Risk](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-4-many-faces.html)

- [Data Update 5: Of Hurdle Rates and Funding Costs!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-5-hurdle-rates.html)

- [Data Update 6: Profitability and Value Creation!](https://aswathdamodaran.blogspot.com/2019/01/january-2019-data-update-6.html)

- [Data Update 7: Debt, neither poison nor nectar!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-7-debt-neither.html)

- [Data Update 8: Dividends and Buybacks - Fact and Fiction!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-8-dividends.html)

- [Data Update 9: Playing the Pricing Game!](https://aswathdamodaran.blogspot.com/2019/02/january-2019-data-update-9-pricing-game.html)
