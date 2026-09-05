---
title: "Valsession18"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/podcasts/valfall15/valsession18.pdf
---

# Application Tests

- □ Given the firm that we are valuing, what is a “comparable” firm?
  - ■ While traditional analysis is built on the premise that firms in the same sector are comparable firms, valuation theory would suggest that a comparable firm is one which is similar to the one being analyzed in terms of fundamentals.
  - ■ Proposition 4: There is no reason why a firm cannot be compared with another firm in a very different business, if the two firms have the same risk, growth and cash flow characteristics.
- □ Given the comparable firms, how do we adjust for differences across firms on the fundamentals?
  - ■ Proposition 5: It is impossible to find an exactly identical firm to the one you are valuing.

## Valuing one company rela've to others… Rela've valua'on with comparables

¨ Ideally, you would like to find lots of publicly traded firms that look just like your firm, in terms of fundamentals, and compare the pricing of your firm to the pricing of these other publicly traded firms. Since, they are all just like your firm, there will be no need to control for differences. ¨ In prac'ce, it is very difficult (and perhaps impossible) to find firms that share the same risk, growth and cash flow characteris'cs of your firm. Even if you are able to find such firms, they will very few in number. The trade off then becomes: 

![](_page_1_Diagram_3.jpeg)

# Techniques for comparing across firms

- 1. Direct comparisons: If the comparable firms are "just like" your firm, you can compare mul'ples directly across the firms and conclude that your firm is expensive (cheap) if it trades at a mul'ple higher (lower) than the other firms.
- 2. Story telling: If there is a key dimension on which the firms vary, you can tell a story based upon your understanding of how value varies on that dimension. An example: This company trades at 12 'mes earnings, whereas the rest of the sector trades at 10 'mes earnings, but I think it is cheap because it has a much higher growth rate than the rest of the sector.
- 3. Modified mul'ple: You can modify the mul'ple to incorporate the dimension on which there are differences across firms.
- 4. Sta's'cal techniques: If your firms vary on more than one dimension, you can try using mul'ple regressions (or variants thereof) to arrive at a "controlled" es'mate for your firm.

## Example 1: Let's try some story telling Comparing PE ra'os across firms in a sector

| Company	Name                        | Trailing	PE | Expected	Growth | Standard	Devia<on |
|-------------------------------------|-------------|-----------------|-------------------|
| Coca-Cola	Bo_ling                   | 29.18       | 9.50%           | 20.58%            |
| Molson	Inc.	Ltd.	'A'                | 43.65       | 15.50%          | 21.88%            |
| Anheuser-Busch																24.31 |             | 11.00%          | 22.92%            |
| Corby	Dis'lleries	Ltd.							16.24  |             | 7.50%           | 23.66%            |
| Chalone	Wine	Group                  | 21.76       | 14.00%          | 24.08%            |
| Andres	Wines	Ltd.	'A'								8.96   |             | 3.50%           | 24.70%            |
| Todhunter	Int'l                     | 8.94        | 3.00%           | 25.74%            |
| Brown-Forman	'B'													10.07  |             | 11.50%          | 29.43%            |
| Coors	(Adolph)	'B'                  | 23.02       | 10.00%          | 29.52%            |
| PepsiCo,	Inc.                       | 33.00       | 10.50%          | 31.35%            |
| Coca-Cola                           | 44.33       | 19.00%          | 35.51%            |
| Boston	Beer	'A'                     | 10.59       | 17.13%          | 39.58%            |
| Whitman	Corp.                       | 25.19       | 11.50%          | 44.26%            |
| Mondavi	(Robert)	'A'								16.47   |             | 14.00%          | 45.84%            |
| Coca-Cola	Enterprises							37.14   |             | 27.00%          | 51.34%            |
| Hansen	Natural	Corp											9.70  |             | 17.00%          | 62.45%            |

# A Ques'on

- ¨ You are reading an equity research report on this sector, and the analyst claims that Andres Wine and Hansen Natural are under valued because they have low PE ra'os. Would you agree?
  - a. Yes
- b. No ¨ Why or why not?

## Example 2: Fact-based story telling Comparing PE Ra'os across a Sector: PE

| Company Name                                     | PE    | Growth |
|--------------------------------------------------|-------|--------|
| PT Indosat ADR                                   | 7.8   | 0.06   |
| Telebras ADR                                     | 8.9   | 0.075  |
| Telecom Corporation of New Zealand ADR           | 11 .2 | 0.11   |
| Telecom Argentina Stet - France Telecom SA ADR B | 12.5  | 0.08   |
| Hellenic Telecommunication Organization SA ADR   | 12.8  | 0.12   |
| Telecomunicaciones de Chile ADR                  | 16.6  | 0.08   |
| Swisscom AG ADR                                  | 18.3  | 0.11   |
| Asia Satellite Telecom Holdings ADR              | 19.6  | 0.16   |
| Portugal Telecom SA ADR                          | 20.8  | 0.13   |
| Telefonos de Mexico ADR L                        | 21 .1 | 0.14   |
| Matav RT ADR                                     | 21 .5 | 0.22   |
| Telstra ADR                                      | 21 .7 | 0.12   |
| Gilat Communications                             | 22.7  | 0.31   |
| Deutsche Telekom AG ADR                          | 24.6  | 0.11   |
| British Telecommunications PLC ADR               | 25.7  | 0.07   |
| Tele Danmark AS ADR                              | 27    | 0.09   |
| Telekomunikasi Indonesia ADR                     | 28.4  | 0.32   |
| Cable & Wireless PLC ADR                         | 29.8  | 0.14   |
| APT Satellite Holdings ADR                       | 31    | 0.33   |
| Telefonica SA ADR                                | 32.5  | 0.18   |
| Royal KPN NV ADR                                 | 35.7  | 0.13   |
| Telecom Italia SPA ADR                           | 42.2  | 0.14   |
| Nippon Telegraph & Telephone ADR                 | 44.3  | 0.2    |
| France Telecom SA ADR                            | 45.2  | 0.19   |
| Korea Telecom ADR                                | 71 .3 | 0.44   |

# PE, Growth and Risk

Dependent variable is: PE 

R squared = 66.2% R squared (adjusted) = 63.1% 

| Variable        | Coefficient | SE    | t-ra'o | Probability |
|-----------------|-------------|-------|--------|-------------|
| Constant        | 13.1151     | 3.471 | 3.78   | 0.0010      |
| Growth	rate     | 121.223     | 19.27 | 6.29   | ≤	0.0001    |
| Emerging	Market | -13.8531    | 3.606 | -3.84  | 0.0009      |

Emerging Market is a dummy: 1 if emerging market 0 if not 

# Is Telebras under valued?

¨ Predicted PE = 13.12 + 121.22 (.075) - 13.85 (1) = 8.35 ¨ At an actual price to earnings ra'o of 8.9, Telebras is slightly overvalued. ¨ Bo\_om line: Just because a company trades at a low PE ra'o does not make it cheap. 

## Example 3: An Eyeballing Exercise with P/BV Ra'os European Banks in 2010

| Name                         | PBV Ratio | Return on Equity | Standard Deviation |
|------------------------------|-----------|------------------|--------------------|
| BAYERISCHE HYPO-UND VEREINSB | 0.80      | -1.66%           | 49.06%             |
| COMMERZBANK AG               | 1.09      | -6.72%           | 36.21%             |
| DEUTSCHE BANK AG -REG        | 1.23      | 1.32%            | 35.79%             |
| BANCA INTESA SPA             | 1.66      | 1.56%            | 34.14%             |
| BNP PARIBAS                  | 1.72      | 12.46%           | 31.03%             |
| BANCO SANTANDER CENTRAL HISP | 1.86      | 11.06%           | 28.36%             |
| SANPAOLO IMI SPA             | 1.96      | 8.55%            | 26.64%             |
| BANCO BILBAO VIZCAYA ARGENTA | 1.98      | 11.17%           | 18.62%             |
| SOCIETE GENERALE             | 2.04      | 9.71%            | 22.55%             |
| ROYAL BANK OF SCOTLAND GROUP | 2.09      | 20.22%           | 18.35%             |
| HBOS PLC                     | 2.15      | 22.45%           | 21.95%             |
| BARCLAYS PLC                 | 2.23      | 21.16%           | 20.73%             |
| UNICREDITO ITALIANO SPA      | 2.30      | 14.86%           | 13.79%             |
| KREDIETBANK SA LUXEMBOURGEOI | 2.46      | 17.74%           | 12.38%             |
| ERSTE BANK DER OESTER SPARK  | 2.53      | 10.28%           | 21.91%             |
| STANDARD CHARTERED PLC       | 2.59      | 20.18%           | 19.93%             |
| HSBC HOLDINGS PLC            | 2.94      | 18.50%           | 19.66%             |
| LLOYDS TSB GROUP PLC         | 3.33      | 32.84%           | 18.66%             |
| Average                      | 2.05      | 12.54%           | 24.99%             |
| Median                       | 2.07      | 11.82%           | 21.93%             |

# The median test…

¨ We are looking for stocks that trade at low price to book ra'os, while genera'ng high returns on equity, with low risk. But what is a low price to book ra'o? Or a high return on equity? Or a low risk ¨ One simple measure of what is par for the sector are the median values for each of the variables. A simplis'c decision rule on under and over valued stocks would therefore be: ¤ Undervalued stocks: Trade at price to book ra'os below the median for the sector,(2.07), generate returns on equity higher than the sector median (11.82%) and have standard devia'ons lower than the median (21.93%). ¤ Overvalued stocks: Trade at price to book ra'os above the median for the sector and generate returns on equity lower than the sector median. 

# How about this mechanism?

¨ We are looking for stocks that trade at low price to book ra'os, while genera'ng high returns on equity. But what is a low price to book ra'o? Or a high return on equity? ¨ Taking the sample of 18 banks, we ran a regression of PBV against ROE and standard devia'on in stock prices (as a proxy for risk). 

PBV = 2.27 + 3.63 ROE - 2.68 Std dev (5.56) (3.32) (2.33) 

R squared of regression = 79% 

# And these predic'ons?

| Name                         | PBV Ratio | Return on Equity | Standard Deviation | Predicted PBV | Under/Over (%) |
|------------------------------|-----------|------------------|--------------------|---------------|----------------|
| BAYERISCHE HYPO-UND VEREINSB | 0.80      | -1.66%           | 49.06%             | 0.89          | -10.60%        |
| COMMERZBANK AG               | 1.09      | -6.72%           | 36.21%             | 1.05          | 3.25%          |
| DEUTSCHE BANK AG -REG        | 1.23      | 1.32%            | 35.79%             | 1.36          | -9.26%         |
| BANCA INTESA SPA             | 1.66      | 1.56%            | 34.14%             | 1.41          | 17.83%         |
| BNP PARIBAS                  | 1.72      | 12.46%           | 31.03%             | 1.89          | -8.75%         |
| BANCO SANTANDER CENTRAL HISP | 1.86      | 11.06%           | 28.36%             | 1.91          | -2.66%         |
| SANPAOLO IMI SPA             | 1.96      | 8.55%            | 26.64%             | 1.86          | 5.23%          |
| BANCO BILBAO VIZCAYA ARGENTA | 1.98      | 11.17%           | 18.62%             | 2.17          | -9.12%         |
| SOCIETE GENERALE             | 2.04      | 9.71%            | 22.55%             | 2.02          | 1.37%          |
| ROYAL BANK OF SCOTLAND GROUP | 2.09      | 20.22%           | 18.35%             | 2.51          | -16.65%        |
| HBOS PLC                     | 2.15      | 22.45%           | 21.95%             | 2.49          | -13.71%        |
| BARCLAYS PLC                 | 2.23      | 21.16%           | 20.73%             | 2.48          | -9.96%         |
| UNICREDITO ITALIANO SPA      | 2.30      | 14.86%           | 13.79%             | 2.44          | -5.72%         |
| KREDIETBANK SA LUXEMBOURGEOI | 2.46      | 17.74%           | 12.38%             | 2.58          | -4.79%         |
| ERSTE BANK DER OESTER SPARK  | 2.53      | 10.28%           | 21.91%             | 2.05          | 23.11%         |
| STANDARD CHARTERED PLC       | 2.59      | 20.18%           | 19.93%             | 2.47          | 5.00%          |
| HSBC HOLDINGS PLC            | 2.94      | 18.50%           | 19.66%             | 2.41          | 21.91%         |
| LLOYDS TSB GROUP PLC         | 3.33      | 32.84%           | 18.66%             | 2.96          | 12.40%         |

# A follow up on US Banks

![](_page_12_Figure_2.jpeg)

#### Example 4: A larger sample Price to Book versus ROE: Largest firms in the US: January 2010

![](_page_13_Figure_2.jpeg)

# Missing growth?

![](_page_14_Figure_2.jpeg)

# PBV, ROE and Risk: Large Cap US firms

![](_page_15_Figure_2.jpeg)

# Bringing it all together... Largest US stocks in January 2010

69

**Model Summary**

| Model | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
|-------|-------------------|----------|-------------------|----------------------------|
| 1     | .819 <sup>a</sup> | .670     | .661              | 1.19253                    |

a. Predictors: (Constant), ROE, Expected Growth in EPS: next 5 years, Regression Beta

**Coefficients<sup>a</sup>**

| Model                                | Unstandardized Coefficients |            | Standardized Coefficients | t      | Sig. |
|--------------------------------------|-----------------------------|------------|---------------------------|--------|------|
|                                      | B                           | Std. Error | Beta                      |        |      |
| 1 (Constant)                         | .406                        | .424       |                           | .958   | .340 |
| Regression Beta                      | -.065                       | .253       | -.015                     | -.256  | .799 |
| Expected Growth in EPS: next 5 years | 9.340                       | 2.366      | .228                      | 3.947  | .000 |
| ROE                                  | 10.546                      | .771       | .777                      | 13.672 | .000 |

a. Dependent Variable: PBV Ratio

### Updated PBV Ra'os – Largest Market Cap US companies Updated to January 2015

![](_page_17_Figure_2.jpeg)

## Example 5: Overlooked fundamentals? EV/EBITDA Mul'ple for Trucking Companies

| Company Name              |             | Value  | EBITDA      |        | Value/EBITDA |
|---------------------------|-------------|--------|-------------|--------|--------------|
| KLLM Trans. Svcs.         | \$          | 114.32 | \$          | 48.81  | 2.34         |
| Ryder System              | \$ 5,158.04 |        | \$ 1,838.26 |        | 2.81         |
| Rollins Truck Leasing     | \$ 1,368.35 |        | \$          | 447.67 | 3.06         |
| Cannon Express Inc.       | \$          | 83.57  | \$          | 27.05  | 3.09         |
| Hunt (J.B.)               | \$          | 982.67 | \$          | 310.22 | 3.17         |
| Yellow Corp.              | \$          | 931.47 | \$          | 292.82 | 3.18         |
| Roadway Express           | \$          | 554.96 | \$          | 169.38 | 3.28         |
| Marten Transport Ltd.     | \$          | 116.93 | \$          | 35.62  | 3.28         |
| Kenan Transport Co.       | \$          | 67.66  | \$          | 19.44  | 3.48         |
| M.S. Carriers             | \$          | 344.93 | \$          | 97.85  | 3.53         |
| Old Dominion Freight      | \$          | 170.42 | \$          | 45.13  | 3.78         |
| Trimac Ltd                | \$          | 661.18 | \$          | 174.28 | 3.79         |
| Matlack Systems           | \$          | 112.42 | \$          | 28.94  | 3.88         |
| XTRA Corp.                | \$ 1,708.57 |        | \$          | 427.30 | 4.00         |
| Covenant Transport Inc    | \$          | 259.16 | \$          | 64.35  | 4.03         |
| Builders Transport        | \$          | 221.09 | \$          | 51.44  | 4.30         |
| Werner Enterprises        | \$          | 844.39 | \$          | 196.15 | 4.30         |
| Landstar Sys.             | \$          | 422.79 | \$          | 95.20  | 4.44         |
| AMERCO                    | \$ 1,632.30 |        | \$          | 345.78 | 4.72         |
| USA Truck                 | \$          | 141.77 | \$          | 29.93  | 4.74         |
| Frozen Food Express       | \$          | 164.17 | \$          | 34.10  | 4.81         |
| Arnold Inds.              | \$          | 472.27 | \$          | 96.88  | 4.87         |
| Greyhound Lines Inc.      | \$          | 437.71 | \$          | 89.61  | 4.88         |
| USFreightways             | \$          | 983.86 | \$          | 198.91 | 4.95         |
| Golden Eagle Group Inc.   | \$          | 12.50  | \$          | 2.33   | 5.37         |
| Arkansas Best             | \$          | 578.78 | \$          | 107.15 | 5.40         |
| Airlease Ltd.             | \$          | 73.64  | \$          | 13.48  | 5.46         |
| Celadon Group             | \$          | 182.30 | \$          | 32.72  | 5.57         |
| Amer. Freightways         | \$          | 716.15 | \$          | 120.94 | 5.92         |
| Transfinancial Holdings   | \$          | 56.92  | \$          | 8.79   | 6.47         |
| Vitran Corp. 'A'          | \$          | 140.68 | \$          | 21.51  | 6.54         |
| Interpool Inc.            | \$ 1,002.20 |        | \$          | 151.18 | 6.63         |
| Intrenet Inc.             | \$          | 70.23  | \$          | 10.38  | 6.77         |
| Swift Transportation      | \$          | 835.58 | \$          | 121.34 | 6.89         |
| Landair Services          | \$          | 212.95 | \$          | 30.38  | 7.01         |
| CNF Transportation        | \$ 2,700.69 |        | \$          | 366.99 | 7.36         |
| Budget Group Inc          | \$ 1,247.30 |        | \$          | 166.71 | 7.48         |
| Caliber System            | \$ 2,514.99 |        | \$          | 333.13 | 7.55         |
| Knight Transportation Inc | \$          | 269.01 | \$          | 28.20  | 9.54         |
| Heartland Express         | \$          | 727.50 | \$          | 64.62  | 11.26        |
| Greyhound CDA Transn Corp | \$          | 83.25  | \$          | 6.99   | 11.91        |
| Mark VII                  | \$          | 160.45 | \$          | 12.96  | 12.38        |
| Coach USA Inc             | \$          | 678.38 | \$          | 51.76  | 13.11        |
| US 1 Inds Inc.            | \$          | 5.60   | \$          | (0.17) | NA           |
| Average                   |             |        |             |        | 5.61         |

# A Test on EBITDA

¨ Ryder System looks very cheap on a Value/EBITDA mul'ple basis, rela've to the rest of the sector. What explana'on (other than misvalua'on) might there be for this difference? ¨ What general lessons would you draw from this on the EV/EBITDA mul'ples for infrastructure companies as their infrastructure ages? 

### Example 6: Rela've valua'on across 'me Price to Sales Mul'ples: Grocery Stores - US in January 2007

![](_page_20_Figure_2.jpeg)

Whole Foods: In 2007: Net Margin was 3.41% and Price/ Sales ratio was 1.41 Predicted Price to Sales = 0.07 + 10.49 (0.0341) = 0.43

## Reversion to normalcy: Grocery Stores - US in January 2009

Whole Foods: In 2009, Net Margin had dropped to 2.77% and Price to Sales ratio was down to 0.31.

Predicted Price to Sales = 0.07 + 10.49 (.0277) = 0.36

![](_page_21_Figure_2.jpeg)

# And again in 2010..

Whole Foods: In 2010, Net Margin had dropped to 1.44% and Price to Sales ratio increased to 0.50.

Predicted Price to Sales = 0.06 + 11.43 (.0144) = 0.22

![](_page_22_Figure_2.jpeg)

# Here is 2011…

PS Ratio= - 0.585 + 55.50 (Net Margin) R2= 48.2%

PS Ratio for WFMI = -0.585 + 55.50 (.0273) = 0.93

At a PS ratio of 0.98, WFMI is slightly over valued.

![](_page_23_Figure_2.jpeg)

# Grocery Stores: January 2015

**77**

![](_page_24_Figure_2.jpeg)

PS = 0.557 + 0.085 Net Margin

Whole Foods = 0.557 + 8.50 (0.0408) = 0.90

There is a new star in town (Sprouts)

### Example 7: Despera'on Time Nothing's working!!! Internet Stocks in early 2000..

![](_page_25_Figure_2.jpeg)

## PS Ra'os and Margins are not highly correlated

¨ Regressing PS ra'os against current margins yields the following 

PS = 81.36 - 7.54(Net Margin) R2 = 0.04 (0.49) 

¨ This is not surprising. These firms are priced based upon expected margins, rather than current margins. 

## Solu'on 1: Use proxies for survival and growth: Amazon in early 2000

¨ Hypothesizing that firms with higher revenue growth and higher cash balances should have a greater chance of surviving and becoming profitable, we ran the following regression: (The level of revenues was used to control for size) 

$$PS = 30.61 - 2.77 \ln(\text{Rev}) + 6.42 (\text{Rev Growth}) + 5.11 (\text{Cash/Rev}) \\ (0.66) \quad (2.63) \quad (3.49)$$

R squared = 31.8% 

¨ Predicted PS = 30.61 - 2.77(7.1039) + 6.42(1.9946) + 5.11 (. 3069) = 30.42 ¨ Actual PS = 25.63 

Stock is undervalued, rela've to other internet stocks. 

# Solution 2: Use forward multiples Watch out for bumps in the road (Tesla)

![](_page_28_Figure_7.jpeg)

## Solu'on 3: Let the market tell you what ma\_ers.. Social media in October 2013

| Company     | Market Cap   | Enterprise value | Revenues   | EBITDA     | Net Income | Number of users (millions) | EV/User         | EV/Revenue   | EV/EBITDA     | PE            |
|-------------|--------------|------------------|------------|------------|------------|----------------------------|-----------------|--------------|---------------|---------------|
| Facebook    | \$173,540.00 | \$160,090.00     | \$7,870.00 | \$3,930.00 | \$1,490.00 | 1230.00                    | \$130.15        | 20.34        | 40.74         | 116.47        |
| Linkedin    | \$23,530.00  | \$19,980.00      | \$1,530.00 | \$182.00   | \$27.00    | 277.00                     | \$72.13         | 13.06        | 109.78        | 871.48        |
| Pandora     | \$7,320.00   | \$7,150.00       | \$655.00   | -\$18.00   | -\$29.00   | 73.40                      | \$97.41         | 10.92        | NA            | NA            |
| Groupon     | \$6,690.00   | \$5,880.00       | \$2,440.00 | \$125.00   | -\$95.00   | 43.00                      | \$136.74        | 2.41         | 47.04         | NA            |
| Netflix     | \$25,900.00  | \$25,380.00      | \$4,370.00 | \$277.00   | \$112.00   | 44.00                      | \$576.82        | 5.81         | 91.62         | 231.25        |
| Yelp        | \$6,200.00   | \$5,790.00       | \$233.00   | \$2.40     | -\$10.00   | 120.00                     | \$48.25         | 24.85        | 2412.50       | NA            |
| Open Table  | \$1,720.00   | \$1,500.00       | \$190.00   | \$63.00    | \$33.00    | 14.00                      | \$107.14        | 7.89         | 23.81         | 52.12         |
| Zynga       | \$4,200.00   | \$2,930.00       | \$873.00   | \$74.00    | -\$37.00   | 27.00                      | \$108.52        | 3.36         | 39.59         | NA            |
| Zillow      | \$3,070.00   | \$2,860.00       | \$197.00   | -\$13.00   | -\$12.45   | 34.50                      | \$82.90         | 14.52        | NA            | NA            |
| Trulia      | \$1,140.00   | \$1,120.00       | \$144.00   | -\$6.00    | -\$18.00   | 54.40                      | \$20.59         | 7.78         | NA            | NA            |
| Tripadvisor | \$13,510.00  | \$12,860.00      | \$945.00   | \$311.00   | \$205.00   | 260.00                     | \$49.46         | 13.61        | 41.35         | 65.90         |
|             |              |                  |            |            |            | <b>Average</b>             | <b>\$130.01</b> | <b>11.32</b> | <b>350.80</b> | <b>267.44</b> |
|             |              |                  |            |            |            | <b>Median</b>              | <b>\$97.41</b>  | <b>10.92</b> | <b>44.20</b>  | <b>116.47</b> |

## Read the tea leaves: See what the market cares about

**83**

| Market Cap                 | Market Cap 1. | Enterprise value | Revenues | EBITDA | Net Income | Number of users (millions) |
|----------------------------|---------------|------------------|----------|--------|------------|----------------------------|
| Enterprise value           | 0.9998        | 1.               |          |        |            |                            |
| Revenues                   | 0.8933        | 0.8966           | 1.       |        |            |                            |
| EBITDA                     | 0.9709        | 0.9701           | 0.8869   | 1.     |            |                            |
| Net Income Number of users | 0.8978        | 0.8971           | 0.8466   | 0.9716 | 1.         |                            |
| (millions)                 | 0.9812        | 0.9789           | 0.8053   | 0.9354 | 0.8453     | 1.                         |

Twitter had 240 million users at the time of its IPO. What price would you attach to the company?

## Rela've valua'on across the en're market: Why not?

¨ In contrast to the 'comparable firm' approach, the informa'on in the en're cross-sec'on of firms can be used to predict PE ra'os. ¨ The simplest way of summarizing this informa'on is with a mul'ple regression, with the PE ra'o as the dependent variable, and proxies for risk, growth and payout forming the independent variables. 

## I. PE Ra'o versus the market PE versus Expected EPS Growth: January 2015

![](_page_32_Figure_2.jpeg)

# PE Ratio: Standard Regression for US stocks - January 2015

86

| Model Summary <sup>a</sup> |                   |          |                   |                            |
|----------------------------|-------------------|----------|-------------------|----------------------------|
| Model                      | R                 | R Square | Adjusted R Square | Std. Error of the Estimate |
| 1                          | .597 <sup>b</sup> | .356     | .355              | 1002.538                   |

a. Broad Group = United States

b. Predictors: (Constant), Expected growth rate in EPS- Next 5 years, Beta, Payout ratio

The regression is run with growth and payout entered as decimals, i.e., 25% is entered as 0.25)

| Coefficients <sup>a,b,c</sup>             |                             |            |                           |        |      |
|-------------------------------------------|-----------------------------|------------|---------------------------|--------|------|
| Model                                     | Unstandardized Coefficients |            | Standardized Coefficients | t      | Sig. |
|                                           | B                           | Std. Error | Beta                      |        |      |
| 1 (Constant)                              | 6.479                       | 1.204      |                           | 5.380  | .000 |
| Beta                                      | -3.248                      | .840       | -.108                     | -3.866 | .000 |
| Payout ratio                              | 16.772                      | 1.290      | .365                      | 12.998 | .000 |
| Expected growth rate in EPS- Next 5 years | 98.579                      | 4.428      | .588                      | 22.260 | .000 |

a. Broad Group = United States

b. Dependent Variable: Trailing PE

c. Weighted Least Squares Regression - Weighted by Market Cap (in US \$)

## Problems with the regression methodology

¨ The basic regression assumes a linear rela'onship between PE ra'os and the financial proxies, and that might not be appropriate. ¨ The basic rela'onship between PE ra'os and financial variables itself might not be stable, and if it shivs from year to year, the predic'ons from the model may not be reliable. ¨ The independent variables are correlated with each other. For example, high growth firms tend to have high risk. This mul'-collinearity makes the coefficients of the regressions unreliable and may explain the large changes in these coefficients from period to period. 

# The Mul'collinearity Problem

| Correlations <sup>a</sup>                 |                     |        |              |                                           |
|-------------------------------------------|---------------------|--------|--------------|-------------------------------------------|
|                                           | Trailing PE         | Beta   | Payout ratio | Expected growth rate in EPS- Next 5 years |
| Trailing PE                               | Pearson Correlation | 1      | .038*        | .187**                                    |
|                                           | Sig. (2-tailed)     |        | .031         | .000                                      |
|                                           | N                   | 3307   | 3168         | 1980                                      |
| Beta                                      | Pearson Correlation | .038*  | 1            | -.200**                                   |
|                                           | Sig. (2-tailed)     | .031   |              | .000                                      |
|                                           | N                   | 3168   | 6841         | 1601                                      |
| Payout ratio                              | Pearson Correlation | .187** | -.200**      | 1                                         |
|                                           | Sig. (2-tailed)     | .000   | .000         | .001                                      |
|                                           | N                   | 1628   | 1601         | 1081                                      |
| Expected growth rate in EPS- Next 5 years | Pearson Correlation | .225** | .085**       | 1                                         |
|                                           | Sig. (2-tailed)     | .000   | .000         | .001                                      |
|                                           | N                   | 1980   | 2447         | 2574                                      |

# Using the PE ra'o regression

¨ Assume that you were given the following informa'on for Disney. The firm has an expected growth rate of 15%, a beta of 1.25 and a 20% dividend payout ra'o. Based upon the regression, es'mate the predicted PE ra'o for Disney. ¤ Predicted PE = 6.48 -3.25 Beta + 95.58 Growth + 16.77 (Payout) ¨ Disney is actually trading at 20 'mes earnings. What does the predicted PE tell you? ¨ Assume now that you value Disney against just its peer group. Will you come to the same valua'on judgment as you did when you looked at it rela've to the market? Why or why not? 

# The value of growth

| Date   | Market	price	of	extra	%	growth | Implied	ERP |
|--------|--------------------------------|-------------|
| Jan-15 | 0.99                           | 5.78%       |
| Jan-14 | 1.49                           | 4.96%       |
| Jan-13 | 0.577                          | 5.78%       |
| Jan-12 | 0.408                          | 6.04%       |
| Jan-11 | 0.836                          | 5.20%       |
| Jan-10 | 0.55                           | 4.36%       |
| Jan-09 | 0.78                           | 6.43%       |
| Jan-08 | 1.427                          | 4.37%       |
| Jan-07 | 1.178                          | 4.16%       |
| Jan-06 | 1.131                          | 4.07%       |
| Jan-05 | 0.914                          | 3.65%       |
| Jan-04 | 0.812                          | 3.69%       |
| Jan-03 | 2.621                          | 4.10%       |
| Jan-02 | 1.003                          | 3.62%       |
| Jan-01 | 1.457                          | 2.75%       |
| Jan-00 | 2.105                          | 2.05%       |