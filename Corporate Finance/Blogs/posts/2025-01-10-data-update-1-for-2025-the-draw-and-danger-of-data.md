---
title: "Data Update 1 for 2025: The Draw (and Danger) of Data"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2025/01/data-update-1-for-2025-draw-and-danger.html
published: 2025-01-10
updated_source: 2025-03-25
fetched: 2026-08-27
tags:
  - Data Updates
---

# Data Update 1 for 2025: The Draw (and Danger) of Data

_Source: [https://aswathdamodaran.blogspot.com/2025/01/data-update-1-for-2025-draw-and-danger.html](https://aswathdamodaran.blogspot.com/2025/01/data-update-1-for-2025-draw-and-danger.html) — published 2025-01-10_

For the last four decades, I have spent the first week of each year collecting and analyzing data on publicly traded companies and sharing what I find with anyone who is interested. It is the end of the first full week in 2025, and [my data update for the year](https://pages.stern.nyu.edu/~adamodar/data.html) is now up and running, and I plan to use this post to describe my data sample, my processes for computing industry statistics and the links to finding them. I will also repeat the caveats about how and where the data is best used, that I have always added to my updates.

The Draw (and Dangers) of Data
**   **It is the age of data, as both companies and investors claim to have tamed it to serve their commercial  interests. While I believe that data can lead to better decisions, I am wary about the claims made about what it can and cannot do in terms of optimizing decision making. I find its greatest use is on two dimensions:

- *Fact-checking assertions*: It has always been true that human beings assert beliefs as facts, but with social media at play, they can now make these assertion to much bigger audiences. In corporate finance and investing, which are areas that I work in, I find myself doing double takes as I listen to politicians, market experts and economists making statements about company and market behavior that are fairy tales, and data is often my weapon for discerning the truth. 
- *Noise in predictions*: One reason that the expert class is increasingly mistrusted is because of the unwillingness on the part of many in this class to admit to uncertainty in their forecasts for the future. Hiding behind their academic or professional credentials, they ask people to trust them to be right, but that trust has eroded. If these predictions are based upon data, as they claim they are, it is almost always the case that they come with error (noise) and that admitting to this is not a sign of weakness. In some cases, it is true that the size of that errors may be so large that those listening to the predictions may not act on them, but that is a healthy response.

As I listen to many fall under the spell of data, with AI and analytics add to its allure, I am uncomfortable with the notion that data has all of the answers, and there two reasons why:

- *Data can be biased*: There is a widely held belief that data is objective, at least if it takes numerical form. In the hands of analysts who are biased or have agendas, data can be molded to fit pre-conceptions. I would like to claim to have no bias, but that would be a lie, since biases are often engrained and unconscious, but I have tried, as best as I can, to be transparent about the sample that I use, the data that I work with and how I compute my statistics. In some cases, that may frustrate you, if you are looking for precision, since I offer a range of values, based upon different sampling and estimation choices.  Taking a look at my tax rate calculations, by industry, for US companies, int the start of 2025, I report the following tax rates across companies.[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7VcXRHtktOKA5AAoF6tPfKutcUqEV7_f_qK1xNqeUgvasUC06wy6KSFd720du8TpqQKk2uWyeCSiOvD3hkuFZXQL15VVREjrSDCk2vaSZ9qTUsO5Z_AAwEyjsbx1fsBJWxJT9Bo7Y0kz4PKgWPH4orDYD6kV5uLHRoMOK6vCgAZeuwxuCjBEft5ndik4/s1478/EffTaxRateUS.jpeg)*[Effective tax rates, by Industry (US)](https://pages.stern.nyu.edu/~adamodar/pc/datasets/taxrate.xls)*Note, that the tax rates for US companies range from 6.75% to 26.43%, depending on how I compute the rate, and which companies I use to arrive at that estimate. If you start with the pre-conception that US companies do not pay their fair share in taxes, you will latch on to the 6.75% as your estimated tax rate, whereas if you are in the camp that believes that US companies pay their fair share (or more), you may find 26.43% to be your preferred estimate. 
- *Past versus Future*: Investors and companies often base their future predictions on the past, and while that is entirely understandable, there is a reason why every investment pitch comes with the disclaimer that “past performance is not a reliable indicator of future performance”. I have [written about how mean reversion is at the heart of many active investing strategies](https://aswathdamodaran.blogspot.com/2016/08/mean-reversion-gravitational-super.html), and why assuming that history will repeat can be a mistake. Thus, as you peruse my historical data on implied equity risk premiums or PE ratios for the S&P 500 over time, you may be tempted to compute averages and use them in your investment strategies, or use my industry averages for debt ratios and pricing multiples as the target for every company in the peer group, but you should hold back. 

**The Sample**
    It is undeniable that data is more accessible and available than ever before, and I am a beneficiary. I draw my data from many raw data sources, some of which are freely available to everyone, some of which I pay for and some of which I have access to, because I work at a business school in a university. For company data, my primary source is S&P Capital IQ, augmented with data from a Bloomberg terminal. For the segment of my data that is macroeconomic, my primary source is [FRED, the data set maintained by the Federal Reserve Bank](https://fred.stlouisfed.org), but I supplement with other data that I found online, including [NAIC](https://content.naic.org) for bond spread data and [Political Risk Services (PRS)](https://www.prsgroup.com) for country risk scores. 
    My dataset includes all publicly traded companies listed at the start of the year, with a market price available, and **there were 47810 firms in my sample**, roughly in line with the sample sizes in the last few years. Not surprisingly, the company listings are across the world, and I look at the breakdown of companies, by number and market cap, by geography:
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTJoXsEj_eMisIAMS_TwpjR-ZeuGs8bLSOGaH6Z5wxjz29zw3SIhfo-ZbvDQyuUFTkUuEjdur3LyUH37-P2AuC03cmvL2ApWpt1NY7Y4rNnDEc2pe3xCFsR3QldPogvdg3cY_SFJ-DszQTpYHa8pSj_sjpyw_albxzTHVnVNteDO2ttDlnzFo8iWh1CHM/s1824/SamplePie.jpeg)

As you can see, the market cap of US companies at the start of 2025 accounted for roughly 49% of the market cap of global stocks, up from 44% at the start of 2024 and 42% at the start of 2023. In the table below, we compare the changes in regional market capitalizations (in $ millions) over time.
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkh-QCT7r8-RyoAPkESsIzJx9lT6WiMk-80SeGKOeJBvKs4nA0kejVA0g6cSi06zkdeXOFSIrYYeHfMOlAe0bAnE7_WaotD88CpZm81THpL8LnxNgiYXCtun2icnWUvV6YfIpdDQkLLlPOkxuaASXnv4twPUhxZierTDfU8HumcWCXpmwZcPNt8RwIpmM/s1156/Regionaovertime.jpeg)

Breaking down companies by (S&P) sector,  again both in numbers and market cap, here is what I get:
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBwjkcqLmL11qP7wtsb70iC9Am292l1Jer5iESDg3F5eVADqM41Ye-WyuMbrU_hh1iCSunBV2hi2tOrzBUJBE9IWtY247W9IsDDIlK8BQkyGhKjvGFP_n7uFGjlHkkyvHqbGF3BE1UQxJR-voGghktSWA5FrChpk_cd0LHRzc9R5POhrV44no7Me7RyPE/s1566/SectorPie.jpeg)

While industrials the most listed stocks, technology accounts for 21% of the market cap of all listed stocks, globally, making it the most valuable sector. Thee are wide differences across regions, though, in sector breakdown:
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjz4nMXdWZpWFd66exYQINpJeNNEq2uMstZgnge5HM1ar4zaiiuhGzf_nmGMoU0cZjtmmUDbfXrZyGF6Dg9m7CSbuRQ5OaGgKGkCYBXjwojFJEQ9-dgMoWcJdOhFVuXbBkXNAB3J9hiMZSaf0XMc90p7mbIvpbCQU79YUQyldiE4AKuQ3-ZVwpZtjNJydU/s1754/SectorbyRegionTable.jpeg)

Much of the increase in market capitalization for US equities has come from a surging technology sector, and it is striking that Europe has the lowest percent of value from tech companies of any of the broad subgroups in this table.
    I also create a more detailed breakdown of companies into 94 industry groups, loosely structured to stay with industry groupings that I originally created in the 1990s from Value Line data, to allow for comparisons across time. I know that this classification is at odds with the industry classifications based upon SIC or NAICS codes, but it works well enough for me, at least in the context of corporate finance and valuation. For some of you, my industry classifications may be overly broad, but if you want to use a more focused peer group, I am afraid that you will have to look elsewhere. The industry averages that I report are also provided using the regional breakdown above. If you want to check out which industry group a company falls into, please[click on this file](https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xlsx) (a very large one that may take a while to download) for that detail.

**The Variables**

    The variables that I report industry-average statistics for reflect my interests, and they range the spectrum, with risk, profitability, leverage, and dividend metrics thrown into the mix. Since I teach corporate finance and valuation, I find it useful to break down the data that I report based upon these groupings. The corporate finance grouping includes variables that help in the decisions that businesses need to make on investing, financing and dividends (with links to the US data for 2025, but you can find [more extensive data links here](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html).)

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
 Corporate Governance & Descriptive     1.[ Insider, CEO & Institutional holdings](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/inshold.html)     2.[ Aggregate operating numbers](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/DollarUS.html)     3. [Employee Count & Compensation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Employee.html)         I**nvesting Principle**** ****Financing Principle** **Dividend Principle** *Hurdle Rate**Project Returns**Financing Mix**Financing Type**Cash Return**Dividends/Buyback*s1. [Beta & Risk](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)1. [Return on Equity](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roe.html)1. [Debt Ratios & Fundamentals](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/dbtfund.html)1.[ Debt Details](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/debtdetails.html)1. [Dividends and Potential Dividends (FCFE)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/divfcfe.html)1.[Buybacks](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/divfcfe.html)2. [Equity Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)2. [Return on (invested) capital](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/fundgrEB.html)2. [Ratings & Spreads](https://pages.stern.nyu.edu/~adamodar/pc/datasets/corpdefaultspreads2023.xlsx)2.[ Lease Effect](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/leaseeffect.html)2. [Dividend yield & payout](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/divfund.html) 3. [Default Spreads](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html)3. [Margins & ROC](https://pages.stern.nyu.edu/~adamodar/pc/datasets/mgnroc.xls)3[. Tax rates](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/taxrate.html)   4. [Costs of equity & capital](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html)4. [Excess Returns on investments](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/EVA.html) 4. [Financing Flows](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/finflows.html)    5. [Market alpha](https://pages.stern.nyu.edu/~adamodar/pc/datasets/indreg.xls)   *(If you have trouble with the links, please try a different browser)*
Many of these corporate finance variables, such as the costs of equity and capital, debt ratios and accounting returns also find their way into my valuations, but I add a few variables that are more attuned to my valuation and pricing data needs as well.

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
Valuation Pricing *Growth & Reinvestment**Profitability**Risk**Multiple*s1.[ Historical Growth in Revenues & Earnings](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histgr.html)1. [Profit Margins](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html)1. [Costs of equity & capital](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html)1. [Earnings Multiples](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pedata.html)2. [Fundamental Growth in Equity Earnings](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/fundgr.html)2. [Return on Equity](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roe.html)2. [Standard Deviation in Equity/Firm Value](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/optvar.html)2. [Book Value Multiples](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pbvdata.html)3. [Fundamenal Growth in Operating Earnings](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/fundgrEB.html)
 3.[ Revenue Multiples](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html)4.[ Long term Reinvestment (Cap Ex & Acquisitons)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/capex.html)  4. [EBIT & EBITDA multiple](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html)s5. [R&D](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/R&D.html)   6. [Working capital needs](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wcdata.html)  
*(If you have trouble with the links, please try a different browser)*
Not that while much of this data comes from drawn from financial statements, some of it is market-price driven (betas, standard deviations, trading data), some relates to asset classes (returns on stocks, bonds, real estate) and some are macroeconomic (interest rates, inflation and risk premiums).  While some of the variables are obvious, others are subject to interpretation, and I have a [glossary](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html), where you can see the definitions that I use for the accounting variables. In addition, within each of the datasets (in excel format), you will find a page defining the variables used in that dataset. 

**The Timing**
**    **These datasets were all compiled in the last four days and reflect data available at the start of 2025. For market numbers, like market capitalization, interest rates and risk premiums, these numbers are current, reflecting the market's judgments at the start of 2025. For company financial numbers, I am reliant on accounting information, which gets updated on a quarterly basis. As a consequence, the accounting numbers reflect the most recent financial filings (usually September 30, 2024), and I use the trailing 12-month numbers through the most recent filing for flow numbers (income statement and cash flow statements) and the most recent balance sheet for stock numbers (balance sheet values). 
    While this practice may seem inconsistent, it reflects what investors in the market have available to them, to price stocks. After all, no investor has access to calendar year 2024 accounting numbers at the start of 2025, and it seems entirely consistent to me that the trailing PE ratio at the start of 2025 be computed using the price at the start of 2025 divided by the trailing income in the twelve months ending in September 2024. In the same vein, the expected growth rates for the future and earnings in forward years are obtained by looking at the most updated forecasts from analysts at the start of 2025. 
    Since I update the data only once a year, it will age as we go through 2025, but that aging will be most felt, if you use my pricing multiples (PE, PBV, EV to EBITDA etc.) and not so much with the accounting ratios (accounting returns). To the extent that interest rates and risk premiums will change over the course of the year, the data sets that use them (cost of capital, excess returns) allow for updating these macro numbers. In short, if the ten-year treasury rate climbs to 5% and equity risk premiums surge, you can update those numbers in the [cost of capital worksheet](https://pages.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls), and get updated values.

**
**
**The Estimation Process**
    While I compute the data variables by company, I am restricted from sharing company-specific data by my raw data providers, and most of the data I report is at the industry level. That said, I have wrestled with how best to estimate and report industry statistics, since almost every statistical measure comes with caveats. For a metric like price earnings ratios, computing an average across companies will result in sampling bias (from eliminating money-losing firms) and be skewed by outliers in one direction (mostly positive, since PE ratios cannot be negative). Since this problem occurs across almost all the variables, I use an aggregated variant, where with PE, for instance, I aggregate the market capitalization of all the companies (including money losing firms) in an industry grouping and divide by the aggregated net income of all the companies, including money losers. 
    Since I include all publicly traded firms in my sample, with disclosure requirements varying across firms, there are variables where the data is missing or not disclosed. Rather than throw out these firms from the sample entirely, I keep them in my universe, but report values for only the firms with non-missing data. One example is my [data on employees](https://pages.stern.nyu.edu/~adamodar/pc/datasets/Employee.xls), a dataset that I added two years ago, where I report statistics like revenue per employee and compensation statistics. Since this is not a data item that is disclosed voluntarily only by some firms, the statistics are less reliable than on where there is universal disclosure. 
    On an upbeat note,  and speaking from the perspective of someone who has been doing this for a few decades, accounting standards around the world are less divergent now than in the past, and the data, even in small emerging markets, has far fewer missing items than ten or twenty years ago. 

**Accessing and Using the Data**
    The data that you will find on my website is for public consumption, and I have tried to organize it to make it easily accessible on my webpage. Note that the current year’s data can be accessed here:
[https://pages.stern.nyu.edu/~adamodar//New_Home_Page/datacurrent.html](https://pages.stern.nyu.edu/~adamodar//New_Home_Page/datacurrent.html)
If you click on a link and it does not work, please try a different browser, since Google Chrome, in particular, has had issues with downloads on my server.
    If you are interested in getting the data from previous years, it should be available in the archived data section on my webpage:
[https://pages.stern.nyu.edu/~adamodar//New_Home_Page/dataarchived.html](https://pages.stern.nyu.edu/~adamodar//New_Home_Page/dataarchived.html)
This data goes back more than twenty years, for some data items and for US data, but only a decade or so for global markets.
       Finally, the data is intended primarily for practitioners in corporate finance and valuation, and I hope that I can save you some time and help in valuations in real time. It is worth emphasizing that every data item on my page comes from public sources, and that anyone with time and access to data can recreate it.  For a complete reading of data usage, try this link:
[https://pages.stern.nyu.edu/~adamodar//New_Home_Page/datahistory.html](https://pages.stern.nyu.edu/~adamodar//New_Home_Page/datahistory.html)
If you are in a regulatory or legal dispute, and you are using my data to make your case, you are welcome to do so, but please do not drag me into the fight.  As for acknowledgements when using the data, I will repeat that I said in prior years. If you use my data and want to acknowledge that usage, I thank you, but if you skip that acknowledgement, I will not view it as a slight, and I certainly am not going to threaten you with legal consequences.
    As a final note, please recognize that this I don't have a team working for me, and while that gives me the benefit of controlling the process, unlike the pope, I am extremely fallible. If you find mistakes or missing links, please let me know and I will fix them as quickly as I can. Finally, I have no desire to become a data service, and I cannot meet requests for customized data, no matter how reasonable they may be. I am sorry!

**YouTube Video**

**Links**

- [Current data (start of 2025)](https://people.stern.nyu.edu/adamodar/New_Home_Page/datacurrent.html)
- [Archived data (from prior years)](https://people.stern.nyu.edu/adamodar/New_Home_Page/dataarchived.html)
- [Companies/Industries](https://pages.stern.nyu.edu/~adamodar/pc/datasets/indname.xlsx)
- [Data definitions](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html)

Data Updates for 2025

- [Data Update 1 for 2025: The Draw (and Danger) of Data!](https://aswathdamodaran.blogspot.com/2025/01/data-update-1-for-2025-draw-and-danger.html)
- [Data Update 2 for 2025: The Party continued for US Equities](https://aswathdamodaran.blogspot.com/2025/01/data-update-2-for-2025-party-continued.html)
- [Data Update 3 for 2025: The times they are a'changin'!]( https://aswathdamodaran.blogspot.com/2025/01/data-update-3-for-2025-slicing-and.html)
- [Data Update 4 for 2025: Interest Rates, Inflation and Central Banks!](https://aswathdamodaran.blogspot.com/2025/01/data-update-4-for-2025-interest-rates.html)
- [Data Update 5 for 2025: It's a small world, after all!](https://aswathdamodaran.blogspot.com/2025/02/data-update-5-for-2025-its-small-world.html)
- [Data Update 6 for 2025: From Macro to Micro - The Hurdle Rate Question!](https://aswathdamodaran.blogspot.com/2025/02/data-update-6-for-2025-from-macro-to.html)
- [Data Update 7 for 2025: The End Game in Business!](https://magazine.wharton.upenn.edu/issues/anniversary-issue/a-tough-and-inventive-corporate-lawyer-martin-lipton-w52/)
- [Data Update 8 for 2025: Debt, Taxes and Default - An Unholy Trifecta!](https://aswathdamodaran.blogspot.com/2025/02/data-update-8-for-2025-debt-taxes-and.html)
- [Data Update 9 for 2025: Dividend Policy - Inertia and Me-tooism Rule!](https://aswathdamodaran.blogspot.com/2025/03/data-update-9-for-2025-dividends-and.html)
