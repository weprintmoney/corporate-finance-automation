---
title: "Newsletters"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: http://pages.stern.nyu.edu/~adamodar/New_Home_Page/Valuationofweek/ValeValuation2014.html
---

Newsletters  
.background {color: #00F;
}
   

|  |  |  |  |
| --- | --- | --- | --- |
| [title small](../home.htm) | [bio](../biomission.html) | [t4](../public.htm) | [t9](../papers.html) |
| [t1](../guide.html) | [t5](../classlist.htm) | [t10](../country.htm) |
| [t3](../topics.html) | [t6](../data.html) | [t11](../webcast.htm) |
| [t2](../background.html) | [t8](../spreadsh.htm) |  |

# Valuing Vale: Dealing with commodity & country risk

### Background

Vale is a mining company based in Brazil. It is the largest iron-ore producing company in the world and has grown in the last few years through acquisitions to become one of the largest global mining companies. It reports its financials in both Brazilian reals and US dollars.

**Vale's Cost of Capital** ([Download the spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/Vale2014/ValeCostofCapital.xls))

*Currency Choice*: I chose to value Vale in US dollars, because all of its financials are in US dollars and its markets (commodity) are dollar based. This has two effects. One is that the risk free rate that I will be using in this valuation is a US dollar risk free rate, estimated as the US 10-year treasury bond rate (2.65% on February 4, 2014). The other is that the cash flows will be projected in US dolllars and any growth rate used has to reflect the inflation rate in US dollars, not in BRL.

*Business Risk and Beta*: Rather than stake my valuation on a single regression beta (of Vale against the Bovespa, or the Vale ADR against the S&P 500), I broke Vale down into its constituent businesses and estimated betas for each business (by looking at publicly traded companies globally in that space):

| Business | Sample | Sample size | Unlevered beta of business | Revenues | Peer Group EV/Sales | Value of Business | Proportion of Vale |
| Metals & Mining | Global firms in metals & mining, Market cap>$1 billion | 48 | 0.8553 | $9,013 | 1.97 | $17,739 | 16.65% |
| Iron Ore | Global firms in iron ore | 78 | 0.8334 | $32,717 | 2.48 | $81,188 | 76.20% |
| Fertilizers | Global specialty chemical firms | 693 | 0.9900 | $3,777 | 1.52 | $5,741 | 5.39% |
| Logistics | Global transportation firms | 223 | 0.7500 | $1,644 | 1.14 | $1,874 | 1.76% |
| Vale Operations |  |  | 0.8440 | $47,151 |  | $106,543 | 100.00% |

***Financial Leverage*:** To estimate the effect of financial leverage at Vale, I estimated both the market value of the debt and the present value of lease commitments in its most recent financial filing (September 30, 2013). Based on the market capitalization of the company on February 4, 2014, the estimated debt to equity ratio for the firm is 61.36% and the debt to capital ratio is 38.03%. Using the marginal tax rate for Brazil generates a levered beta of 1.1858 for Vale:

Levered Beta = 0.8440 (1 + (1-.34) (.6136)) = 1.1858

***Equity Risk Premium***: While Vale is a Brazil-based company, its revenues are global and its equity risk premium has to reflect that exposure:

|  | Proportion of Vale's revenues in 2012 | ERP for region |
| US & Canada | 4.90% | 5.00% |
| Brazil | 16.90% | 7.85% |
| Rest of Latin America | 1.70% | 10.09% |
| China | 37.00% | 5.90% |
| Japan | 10.30% | 5.90% |
| Rest of Asia | 8.50% | 6.76% |
| Europe | 17.20% | 6.29% |
| Rest of World | 3.50% | 10.06% |
| Company | 100.00% | 6.54% |

The equity risk premiums come from my updated estimated from January 2014. You can get the complete list by [going here](../data.html).

*Cost of debt and capital*: The cost of debt was based upon the S&P rating for Vale of A- (which reflects both country and company default risk). Adding the default spread of 1.30% that this rating commands generates a cost of debt in US dollar terms of 3.95%.

> Debt ratio = 38.03%
>
> After-tax cost of debt = 3.95% (1-.34) = 2.61%
>
> Cost of equity = 2.65% + 1.1858 (6.54%) = 10.41%
>
> Cost of capital = 10.41% (1- .3803) + 2.61% (.3803) = 7.44%

**Vale base case valuation** ([Download the spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/Vale2014/ValeValuation2014.xls))

*Dealing with volatile earnings*: The ups and downs of the commodity price cycle are reflected in volatile earnings at the company. (Notice that the earnings have been converted intio US dollar values, based on the prevailing exchange rate each year).

| Year | Operating Income ($) | Effective tax rate | BV of Debt | BV of Equity | Cash | Invested capital | Return on capital |
| 2009 | $6,057 | 27.79% | $18,168 | $42,556 | $12,639 | $48,085 | 9.10% |
| 2010 | $23,033 | 18.67% | $23,613 | $59,766 | $11,040 | $72,339 | 25.90% |
| 2011 | $30,206 | 18.54% | $27,668 | $70,076 | $9,913 | $87,831 | 28.01% |
| 2012 | $13,346 | 18.96% | $23,116 | $78,721 | $3,538 | $98,299 | 11.00% |
| 2013 (TTM) | $15,487 | 20.65% | $30,196 | $75,974 | $5,818 | $100,352 | 12.25% |
| Average | $17,626 | 20.92% |  |  |  |  | 17.25% |

I will use the average opearing income of $17.626 million and the average effective tax rate of 20.92% as my base year numbers.

*Reinvestment and Growth*: Given Vale's size (it is one of the largest mining companies in the world) and finite resources, I will assume that the company is in mature growth and will grow its normalized income 2% a year in perpetuity. To estimate the reinvestment, I used a return on capital in perpetuity of 12.50%, higher than the cost of capital of 7.44% but lower than the historical average (which I think will be tough to sustain forever).

Reinvestment rate = g/ ROC = 2%/ 12.5% = 16%

*Base case valuation*: The base case valuation is ready to go, with these inputs:

> Normalized after tax operating income = 17626 (1-.2092) = $13,939 million
>
> Value of operating assets = 13,939 (1-.16)/(.0744 - .02) = $219,460 million

Adding the cash ($7,133 million) and the total debt includng leases ($42,879 million) yields an estimated value for the equity of $183713 million. Dividing by the 5,150 million shares (using ADR units) yields a value per share of $35.67, well above the market price of $13.57. It looks like a BUYYYYYY!

**A Conservative Valuation** ([Download the spreadsheet](http://www.stern.nyu.edu/~adamodar/pc/blog/Vale2014/ValeConservativeValuation2014.xls))

Just to stress check the model, I replaced the normalized income with the depressed income in the trailing 12 months ($15.487 million), assumed that they would have to pay the Brazilian marginal tax rate of 34.00% on all their income, that they would no excess returns (return on capital = 7.44%) and that there would be no growth. The value per share drops to $19.74, still weel above the market price of $13.57.
