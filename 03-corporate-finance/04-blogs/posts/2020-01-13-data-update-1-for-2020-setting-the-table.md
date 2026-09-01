---
title: "Data Update 1 for 2020: Setting the table"
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/2020/01/data-update-1-for-2020-setting-table.html
published: 2020-01-13
updated_source: 2020-01-13
fetched: 2026-08-27
tags:
  - Big Data
  - Crowd Wisdom
  - Data Update
---

# Data Update 1 for 2020: Setting the table

_Source: [https://aswathdamodaran.blogspot.com/2020/01/data-update-1-for-2020-setting-table.html](https://aswathdamodaran.blogspot.com/2020/01/data-update-1-for-2020-setting-table.html) — published 2020-01-13_

Starting in the early 1990s, I have spent the first week or two of every new year playing my version of Moneyball, downloading raw market and accounting data on publicly traded companies and using that data to compute operating, pricing and risk metrics for them. This year, I got a later start than usual on January 6, but as the week draws to a close, the results of my data exploration are posted on my [website](http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html) and will be the basis for a series of posts here over the next six weeks. As you look at the data, you will find that the choices I have made on how to classify companies and compute metrics affect my findings, and I will use this post to cast some light on those choices.

**The Data**

Raw Data: We live in an age when accessing raw data is easy, albeit not always cheap, and the tools to analyze that data are also widely available. My raw data is drawn from a variety of sources, ranging from S&P Capital IQ to Bloomberg to the Federal Reserve, and there are two rules that I try to follow. The first is to be careful about attributing sources for the raw data, and the second is to not undercut my raw data providers by replicating their data on my site, if they have commercial interests. 

Data Analysis: Broadly speaking, I would categorize my data updates into three groups. The first is *macro data*, where my ambitions tend to be modest, and the only numbers that I update are numbers that I need and use in my valuation and corporate financial analysis. The second is *business data*, where I consolidate the company-level data into industry groupings, and report statistics on how companies invest, finance their operations and return cash (dividends and buybacks). The third are *my data archives*, where you can look at trend lines in the statistics by accessing my statistics from prior years. 

*A. Macro Data*

I am not a market timer or a macro economist, and my interests in macro data are therefore limited to numbers that I cannot easily look up, or access, on a public database. Thus, there is no point in my reporting exchange rates between major currencies, when you have [FRED](https://fred.stlouisfed.org/), the Federal Reserve site , that I cannot praise more highly for its reach and its accessibility. I do report and update the following:

- Risk free rates in currencies: The way in which currencies are dealt with in valuation and corporate finance leaves us exposed to multiple problems, and I [have written](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1648164) about both why risk free rates vary across currencies and why government bond rates are not always risk free. At the start of every year, I update my currency risk free rates, starting with the government bond rates, and then netting out default spreads and [report them here](http://www.stern.nyu.edu/~adamodar/pc/datasets/currencyriskfree2020.xls). As risk free rates in developed market currencies hit new lows, and central banks are blamed for the phenomenon, I also update an intrinsic measure of the US dollar risk free rate, obtained by adding the inflation rate to real GDP growth each year, and report the time series in[this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/intrinsicvsactualrate.xlsx).

- Equity Risk Premiums: The equity risk premium is the price of risk in equity markets and plays a key role in both corporate finance and valuation. The conventional approach to estimating this risk premium is to look at history, and to compare the returns that you would have earned investing in stocks, as opposed to investing in risk free investments. I update the historical risk premium for US stocks, by bringing in 2019 returns on stocks, treasury bonds and treasury bills [in this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls); my updated geometric average premium for stocks over US treasuries. I don't like the approach, both because it is backward looking and because the risk premium estimates are noisy, and [have argued for a forward looking or implied ERP](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3378246). I estimate the i[mplied ERP to be 5.20% at the start of 2020](http://www.stern.nyu.edu/~adamodar/pc/implprem/ERPJan20.xlsx) and report the [year-end estimates of the premium going back to 1960](http://www.stern.nyu.edu/~adamodar/pc/datasets/histimpl.xls) in this dataset. 

- Corporate Default Spreads: Just as equity risk premiums measure the price of risk in equity markets, default spreads measure the price of risk in the debt markets. I break down bonds into bond rating classes (S&P and Moody's) and report my estimates of default spreads at the start of 2020 in [this spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/ratings.xls) (and it includes a way of estimating a bond rating for a firm that does not have one).

- Corporate Tax Rates: Ultimately, companies and investors count on after-tax income, though companies are adept at keeping taxes paid low. While I will report the [effective tax rates](http://www.stern.nyu.edu/~adamodar/pc/datasets/taxrate.xls) that companies actually pay in my corporate data, I am grateful to KPMG for going through tax codes in different countries and compiling corporate tax rates, which I reproduce [in this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/countrytaxrates.xls).

- Country Risk Premiums: As companies expand their operations beyond domestic markets, we are faced with the challenge of bringing in the risk of foreign markets into our corporate financial analyses and valuation. I have spent much of the last 25 years trying to come up with better ways of estimating risk premiums for countries, and I describe the process I use in [excruciating detail in this paper.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3427863) At the start of 2020, I use my approach, flaws and all, to estimate equity risk premiums for 170 countries and report them [in this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xlsx).

With macro data, it is generally good practice in both corporate finance and valuation to bring in the numbers as they are today, rather than have a strong directional view. So, uncomfortable though it may make you, you should be using today's risk free rates and risk premiums, rather than normalized values, when valuing companies or making investment assessments.

B. Micro Data

The sample: All data analysis is biased and the bias starts with the sampling approach used to arrive at the data set. My data sample includes all publicly traded companies, listed anywhere in the world, and the only criteria that I impose is that they have a market capitalization number available as of December 31, 2019. The resulting sample of 44,394 firms includes firms from 150 countries, some of which have very illiquid markets and questionable disclosure practices. Rather than remove these firms from my sample, which creates its own biases, I will keep them in my sample and deal with the consequences when I compute my statistics.

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisNo8cn5S2XilguJKfXckVo_wuLNTgO6GdHcKIE3xAZ2rwczotniqR2fum0Vfz77IsEB-QAKpRj_pUJAi1Lz2u9CDpJOQaFhBAqrRaDd7Fl2ZHXm5X_6qICbi4Xce0dl6AxMsXb9Q734I/s1600/SampleDescription.jpg)

While this is a comprehensive sample, it is still biased because it includes just publicly listed companies. There are tens of thousands of private businesses that are part of the competitive landscape that are not included here, and the reason is pragmatic: most of these companies are not required to make public disclosures and there are few reliable databases that include data on these firms. 

The Industry Groupings: While I do have a (very large) spreadsheet that has the data at the company level, I am afraid that my raw data providers do not allow me to share that data, even though it is entirely comprised of numbers that I estimate. I consolidate that data into 94 industry groupings, which are loosely based on the industry groupings I created from Value Line in the 1990s when I first started creating my datasets. To see my industry grouping and what companies fall into each one, [try this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xlsx). As you look at individual companies, there are two challenges that I face. First, there are companies that are in many businesses and I classify these companies into the industry groups from which they derive the most revenues. Second, some companies are shape shifters when it comes to industry grouping, and it is unclear which grouping they belong to; for a few high profile examples, consider Apple and Amazon. There is little that I can do about either problem, but consider yourselves forewarned.

The statistics: My interests lie in corporate finance and valuation and selfishly, I report the statistics that matter to me in that pursuit. Luckily, as I described it in my post a few weeks ago, corporate finance is the ultimate big picture class and the statistics cover the spectrum, and I think the best way to organize them is based upon broad corporate finance principles:

[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjofa2_V4P5KoHbd9qCkJquXHq9mOfsG5gMwkWn9VbPiis1e-6Cw7xSt7fpKL1tZlaNgJyYK_IJ0tZw-CysJ6p327cp7RLmFUwcnXBZWikjiYx9mdYl4-C3PwXFBijBvyKPz9-Cb-oOoFk/s1600/DataItems.jpg)
[Picture with live links](http://www.stern.nyu.edu/~adamodar/pc/blog/LinkstoData.xlsx)

If you are interested, you will find more in-depth descriptions of how I compute the statistics that I report both in the [datasets](http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html) themselves as well as in [this glossary](http://www.stern.nyu.edu/~adamodar/New_Home_Page/datafile/variable.htm).

The timing: I use a mix of market and accounting data and that creates a timing problem, since the accounting data is updated at the end of each quarter and the market data is updated continuously. Using the logic that I should be accessing the most updated data for every item, my January 1, 2020, updated has market data (for share prices, interest rates etc) as of December 31, 2019 and the accounting data as of the most recent financial statement (usually September 30, 2019 for most companies). I don't view this an inconsistent but a reflection of the reality that investors face.

*C. Archived Data*

When I first started compiling my datasets, I did not expect them to be widely used, and certainly did not believe that they would be referenced over time. As I starting getting requests for datasets from earlier years, I decided that it would save both me and you a great deal of time to create [an archive of past datasets](http://people.stern.nyu.edu/adamodar/New_Home_Page/dataarchived.html). As you look at these archives, you will notice that not all datasets go back in time to the 1990s, reflecting first the expansion of my analysis from just US companies to global companies about 15 years ago and second the adding on of variables that I either did not or could not report in earlier years.

**The Rationale**

If you are wondering why I collect and analyze the data, let me make a confession, at the risk of sounding like a geek. I enjoy working with the data and more importantly, the data analysis is a gift that keeps on giving for the rest of the year, as I value companies and do corporate financial analysis.

- It gives me perspective: In a world where we suffer from data overload, the week that I spend looking at the numbers gives me perspective not only on what comprises normal in corporate financial behavior, but also on the differences across sectors and geographies. 

- Possible, Plausible and Probable: I have long argued that the valuation of a company always starts with a story but that a critical part of the process of converting narrative to value is checking the story for possibility, plausibility and probability. Having the global data aggregated and analyzed can help significantly in making this assessment, since you can see the cross section of revenues and profit margins of companies in the business and see if your assessments are out of line, and if so, whether you have a justification. 

- Rules of thumb: In spite of all of the data that we now have available, investors and companies seem to still rely on rules of thumb devised in a different time and market. Thus, we are told that companies that trade at less than book value, or six times EBITDA, are cheap, and that the target or right debt ratio for a manufacturing company is 40%. Using the global data, we can back up or dispel these rules of thumb and perhaps replace them with more dynamic and meaningful decision rules.

- Fact-based opinions: Many market prognosticators and economists seem to have no qualms about making up stuff about investor and corporate behavior and stating them as facts. Thus, it has become conventional wisdom that US companies are paying less in taxes that companies operating elsewhere in the globe, and that they have borrowed immense amounts of cash over the last decade to buy back stock. Those "facts" are now driving political debate and may well lead to change in policy, but these are more opinions than facts, and the data can be arbiter.

If you are wondering why I am sharing the data, let's get real. Nothing that I am doing is unique, and I have no secret data stashes. In short, anyone with access to data (and there are literally tens of thousands who do) can do the same analysis. I lose nothing by sharing, and I get immense karmic payoffs. So, please use whatever data you want, and in whatever context, and I hope that it saves you time and helps you in your decision making and analysis. 

**The Caveats**

The last decade has seen big data and crowd wisdom sold as the answers to all of our problems, and as I listen to the sales pitches for both, I would offer a few cautionary notes, born out of spending much of my life time working with data:

- Data is not objective: The notion that using data makes you objective is nonsense. In fact, the most egregious biases are data-backed, as people with agendas pick and choose the data that confirms their priors. Just as an example, take a look at the data that I have in what US companies paid in taxes in 2019 in [this dataset](http://www.stern.nyu.edu/~adamodar/pc/datasets/taxrate.xls). I have reported a variety of tax rates, not with the intent to confuse, but to note how the numbers change, depending on how you compute them.  If you believe, like some do, that US companies are shirking their tax obligations, you can point to average tax rate of 7.32% that I report for all US companies, and note that this is well below the federal corporate tax rate of 21%. However, someone on the other side of this debate can point to the 19.01% average tax rate across only money making companies (since only profits get taxed) as evidence that companies are paying their taxes. 

- Crowds are not always wise: One of the strongest forces in corporate finance is me-tooism, where companies decide how to invest, how much to borrow and what to pay in dividends by looking at what their peers do. In my datasets, I offer them guidance in this process, by reporting debt ratios and dividend payout ratios for sectors, as well as regional breakdowns. The implicit assumption is that what other companies do, on average, must be sensible, but that assumption is not always true. This warning is particularly relevant when you look at the pricing metrics (PE, EV to EBITDA etc.) that I report, by sector and by region. The market may be right, on average, but it can also over price or under price a sector, at times.

I respect data, but I don't revere it. I don't believe that just having data will give me an advantage over other investors or make me a better investor, but harnessing that data with intuition and logic may give me a leg up (or at least I hope it does).

**YouTube Video**

**
**

**Links**

- [Data on my website](http://www.stern.nyu.edu/~adamodar/New_Home_Page/data.html)

- [Federal Reserve Data Site (FRED)](https://fred.stlouisfed.org/)
