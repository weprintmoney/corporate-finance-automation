---
title: "Data history"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datahistory.html
---

Data history

<!--
.fontcoloor {
color: #FFF;
}
.fontcolor1 {
color: #FFF;
}
.background {color: #00F;
}
.REd {
color: #F00;
}
.white {
color: #FFF;
}
.red {
color: #F00;
}
.Blueforsite { color: #06C;
}
.Blueforsite font {
color: #06C;
}
-->

|  |  |  |  |
| --- | --- | --- | --- |
| [logo](home.htm) | [about](biomission.html) | [writing](writing.html) | [tools](tools.html) |
| [teaching](teaching.html) | [data](data.html) | [blog](http://aswathdamodaran.blogspot.com) |

![](Budimage/datahistory.jpg)

* [About Data](datahistory.html)
  + [History](datahistory.html#history)
  + [Timing](datahistory.html#timing)
  + [Sources](datahistory.html#sources)
  + [Usage rules](datahistory.html#rules)
* [Data Breakdown](databreakdown.html)
  + [Data Variables](databreakdown.html#variables)
  + [Industry](databreakdown.html#industry)
  + [Region](databreakdown.html#region)
  + [Company lookup](databreakdown.html#company)
* [Current Data](datacurrent.html)
  + [Corporate Governance](datacurrent.html#corpgov)
  + [Risk/ Discount Rate](datacurrent.html#discrate)
  + [Investment Returns](datacurrent.html#returns)
  + [Capital Structure](datacurrent.html#capstru)
  + [Dividend Policy](datacurrent.html#dividends)
  + [Cash Flows](datacurrent.html#cashflows)
    - [Profit Margins](#)
    - [Effective tax rates](#)
    - [Capital Expenditures](#)
    - [Working Capital](#)
    - [Free Cash Flow to Firm](#)
  + [Growth/ Reinvestment](datacurrent.html#growth)
    - [Historical Growth Rates](#)
    - [Fundamental Growth](#)
  + [Multiples](datacurrent.html#multiples)
  + [Option](datacurrent.html#options)
* [Archived Data](dataarchived.html)
  + [Corporate Governance](dataarchived.html#corpgov)
  + [Risk/ Discount Rate](dataarchived.html#discrate)
  + [Investment Returns](dataarchived.html#returns)
  + [Capital Structure](dataarchived.html#capstru)
  + [Dividend Policy](dataarchived.html#dividends)
  + [Cash Flows](dataarchived.html#cashflows)
  + [Growth/ Reinvestment](dataarchived.html#growth)
  + [Multiples](dataarchived.html#multiples)
  + [Option](dataarchived.html#options)
* [Webcasts/Tools](datatools.html)
  + [Webcasts](datatools.html#webcasts)
  + [Tools](datatools.html#tools)
  + [Blog Posts](datatools.html#posts)
  + [Writings](datatools.html#writings)

###

---

# History & Philosophy

You should not care about who I am, since it is the data that you are looking for, but just in case you are curious, [here is my bio](biomission.html). I started putting my datasets online in the early 1990s. Since I teach valuation and corporate finance, I am constantly collecting and analyzing data, and I have found that the data, once analyzed, can be used multiple times. Since I already have the processed data, I could not see any harm from sharing that data with others, thus saving us all some collective time, which we can spend far more productively not just on valuation but also with family and friends. I hope you find this data useful and there are no strings attached. Please do read the rest of this page, if you need more background on the data, where it comes from, how often it is updated and caveats on using it in your valuations or corporate finance analysis.

When I first started, I did not expect my reprocesssed data to be used by anyone other than the students in my classes. In fact, for the first few years, the only datasets I had were for US companies and I had only a handful - average betas by sector, averages of PE, Price to Book and EV to EBITDA multiples and a few dividend/debt ratio statistics. I did not provide the individual company data for downloads. Over the last decade, two things have happened that are probably interrelated. The first is that the number of datasets that I approach each year has exploded to more than a hundred datasets, as I have expanded the coverage to include non-US companies. As a consequence, I now use data from multiple data services, which I collate and merge to create a consolidared data set, which I then use for my industry averages.

# Data Timing

I update most of the data only once a year, in the first two weeks of January. There are a few data items, like equity risk premiums, that I update more frequently and I will be specify those items. As a consequence of how often and when I update the data, the data has a few quirks that you should keep in mind. With market data, I try to update the numbers as of December 31 of the prior year. Thus my update in January 2017 included market capitalization and share price data as of December 31, 2016. With accounting data, there will be a lag, since the data for the calendar year is usually not available until April of the following year (at the earliest). Consequently, the last fiscal year (assuming that the company follows a calendar year) will be a year old, with the January 2017 update containing data for 2015, if it is a fiscal year data item. However, *most of the statistics that I compute are based on the most recent twelve months of data* available at the start of each year. Again, with companies that have calendar years, this will mean that the January 2017 last-12-month data will be from October 2015-September 2016.

# Data Sources

I am dependent upon my data sources for my data, and I draw on many: Bloomberg, Morningstar, Capital IQ and Compustat. I am deeply grateful to have access to this data but I do want to raise your awareness of three issues that follow:

1. *Data errors*: The first is that if the data service makes a mistake, I do as well. I cannot check the raw data on 40,000+ individual companies. To be honest, the effect on sector averages will be small, given the size of the sample, but for individual companies, that is not the case.
2. *Data access*: The second is that I have to be sensitive to the data service's commercial interests (which is to sell the data to subscribers). Consequently, I try my absolute best not to reproduce data on individual companies that the service has provided. That is why I compute all of my multiples (PE, EV/EBITDA etc) and other statistics, rather than reporting the values from the service. It is also the reason that I don't report Capital IQ's industry classifications or betas, but create my own (from Capital IQ's raw data) for companies. It may make your life a little more difficult, but it is the only way I can keep this dance going.
3. *Data definitions*: The third is that I have to navigate the different data definitions that the different services used for the same item and make my own judgments. So, it is possible that my estimate of invested capital for a company may not match up to what you obtain from a different service. To clarify my definitions of variables, I have put together a [document where I explain how I define/measure the variables](datafile/variable.htm).

# **Usage Rules**

I am not good at making rules and thus have very few related to the use of my data. I want the data to be widely used and to be a help, rather than a hindrance.

1. *Acknowledgements*: If you do use my data and wish to acknowledge that you did get the data off my site, I thank you. If not, I will not lose any sleep and you should not either.
2. *Industry statistics*: I am a valuation/corporate finance person. When looking at a company, I am less interested in where it has been and more in where it is going. I look at data as raw material that I can use in making better estimates for the future. Consequently, I use that objective in how I come up with my numbers and what I report. For instance, when defining beta, my primary concern is that I get as good a beta estimate I can for the future and not to get the best estimate I can for the past. In valuing companies, I find that it is invaluable to know what the industry looks like and that is where I use the industry averages (that I report).Thus, the **best use for my data** is in real time corporate financial analysis and valuation.
3. *Individual company data*: My suggestion, if you are valuing or analyzing a company in real time is that you get real time data from the company's filings or annual report. If you are trying to do a relative valuation, it is also best to get updated numbers for all of the companies that you are analyzing at the time of the valuation from a real-time data source.
4. *Research*: If you are interested in assessing the past (doing a post-mortem) or researching a question, you will be better served using a service that focuses on providing just that: historical time series information in far more detail than I can provide. You can try to string together my individual company datasets or sector average datasets over time, but it may not serve your purposes as well.
5. *Legal arena*: I do know that this data ends up in the legal arena more often than it should. If you are using my data from a prior year to back up your position or repudiate your opponent's in a court of law, please leave me (personally) out of that food fight. While I stand behind my data, it was never my intent to use it for that purpose. In fact, I don't put much weight on two factors that the legal system values, precedence and consistency. Put differently, if I feel that I have been computing a ratio incorrectly for ten years, I have no qualms about changing the way I do it in year 11.
6. *Public policy debates*: Finally, this data was never meant for public policy debates. In 2011, for instance, the New York Times used the tax rates that I had computed by sector to make a case that the tax code in the US was unfair. That may very well be, but I computed tax rates for a prosaic purpose, which is to value companies. It was not to make judgments on whether companies pay enough in taxes.

In sum, this data is here for you to use and I hope it makes your life easier and your financial analyses better. If it accomplishes that objective, that is thanks enough.
var MenuBar1 = new Spry.Widget.MenuBar("MenuBar1", {imgDown:"../SpryAssets/SpryMenuBarDownHover.gif", imgRight:"../SpryAssets/SpryMenuBarRightHover.gif"});
