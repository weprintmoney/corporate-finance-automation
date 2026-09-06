---
title: "Ddm"
status: active
owner: weprintmoney
created: 2026-09-02
last_updated: 2026-09-02
source_url: https://www.stern.nyu.edu/~adamodar/pdfiles/eqnotes/ddm.pdf
---

# The Dividend Discount Model

Aswath Damodaran

### General Information

<sup>n</sup> The risk premium that I will be using in the 1999 and 2000 valuations for mature equity markets is 4%. This is the average implied equity risk premium from 1960 to 2000. <sup>n</sup> For the valuations from 1998 and earlier, I use a risk premium of 5.5%.

### Con Ed: Rationale for Model

<sup>n</sup> The firm is in stable growth; based upon size and the area that it serves. Its rates are also regulated; It is unlikely that the regulators will allow profits to grow at extraordinary rates.

- <sup>n</sup> Firm Characteristics are consistent with stable, DDM model firm
  - The beta is 0.80 and has been stable over time.
  - The firm is in stable leverage.
  - The firm pays out dividends that are roughly equal to FCFE.
    - Average Annual FCFE between 1994 and 1999 = \$553 million
    - Average Annual Dividends between 1994 and 1999 = \$ 532 million
    - Dividends as % of FCFE = 96.2%

# Con Ed: A Stable Growth DDM: December 31, 2000

<sup>n</sup> Earnings per share for trailing 4 quarters = \$ 3.15 <sup>n</sup> Dividend Payout Ratio over the 4 quarters = 69.21% <sup>n</sup> Dividends per share for last 4 quarters = \$2.18 <sup>n</sup> Expected Growth Rate in Earnings and Dividends =3% <sup>n</sup> Con Ed Beta = 0.80 (Bottom-up beta estimate) <sup>n</sup> Cost of Equity = 5.1% + 0.80\*4% = 8.30%

**Value of Equity per Share = \$2.18 \*1.03 / (.083 -.03) = \$ 42.37**

**The stock was trading at \$ 38.60 on December 31, 2000**

### Con Ed: Break Even Growth Rates

![](_page_4_Figure_1.jpeg)

### Estimating Implied Growth Rate

- <sup>n</sup> To estimate the implied growth rate in Con Ed's current stock price, we set the market price equal to the value, and solve for the growth rate:
  - Price per share = \$ 38.60 = \$2.18 \*(1+g) / (.083 -g)
- Implied growth rate = 2.51**%** <sup>n</sup> Given its retention ratio of 30.79% and its return on equity in 1999 of 10%, the fundamental growth rate for Con Ed is:

Fundamental growth rate = 
$$(.3079 * .10) = 3.08\%$$

# Implied Growth Rates and Valuation Judgments

<sup>n</sup> When you do any valuation, there are three possibilities. The first is that you are right and the market is wrong. The second is that the market is right and that you are wrong. The third is that you are both wrong. In an efficient market, which is the most likely scenario? <sup>n</sup> Assume that you invest in a misvalued firm, and that you are right and the market is wrong. Will you definitely profit from your investment? <sup>o</sup> Yes <sup>o</sup> No

### Con Ed: A Look Back

![](_page_7_Figure_1.jpeg)

### ABN Amro: Rationale for 2-Stage DDM

<sup>n</sup> As a financial service institution, estimating FCFE or FCFF is very difficult. <sup>n</sup> The expected growth rate based upon the current return on equity of 15.56% and a retention ratio of 62.5% is 9.73%. This is higher than what would be a stable growth rate (roughly 5% in Euros)

# ABN Amro: Summarizing the Inputs

#### <sup>n</sup> Market Inputs

- Long Term Riskfree Rate (in Euros) = 5.02%
- Risk Premium = 4% (U.S. premium : Netherlands is AAA rated)

#### <sup>n</sup> Current Earnings Per Share = 1.60 Eur; Current DPS = 0.60 Eur;

| Variable Length Return on Equity | High Growth Phase 5 years 15.56% | Stable Growth Phase Forever after yr 5 15% (Industry average) |
|----------------------------------|----------------------------------|---------------------------------------------------------------|
| Payout Ratio                     | 37.5%                            | 66.67%                                                        |
| Retention Ratio                  | 62.5%                            | 33.33% (b=g/ROE)                                              |
| Expected growth                  | .1556*.625=.0973                 | 5% (Assumed)                                                  |
| Beta                             | 0.95                             | 1.00                                                          |
| Cost of Equity                   | 5.02%+0.95(4%)                   | 5.02%+1.00(4%)                                                |
|                                  | =8.82%                           | =9.02%                                                        |

### ABN Amro: Valuation

| Year | EPS  | DPS  | PV of DPS |
|------|------|------|-----------|
| 1    | 1.76 | 0.66 | 0.60      |
| 2    | 1.93 | 0.72 | 0.61      |
| 3    | 2.11 | 0.79 | 0.62      |
| 4    | 2.32 | 0.87 | 0.62      |
| 5    | 2.54 | 0.95 | 0.63      |

Expected EPS in year 6 = 2.54(1.05) = 2.67 Eur

Expected DPS in year 6 = 2.67\*0.667=1.78 Eur

Terminal Price (in year 5) = 1.78/(.0902-.05) = 42.41 Eur

PV of Terminal Price = 42.41/(1.0882)<sup>5</sup> = 27.79 Eur

**Value Per Share = 0.60 + 0.61+0.62+0.62+0.63+27.79 = 30.87 Eur**

**The stock was trading at 24.33 Euros on December 31, 2000**

![](_page_11_Diagram_1.jpeg)

#### VALUING ABN AMRO

### The Value of Growth

<sup>n</sup> In any valuation model, it is possible to extract the portion of the value that can be attributed to growth, and to break this down further into that portion attributable to "high growth" and the portion attributable to "stable growth". In the case of the 2-stage DDM, this can be accomplished as follows:

| $P_0 =$              | $\left\{ \left( \sum_{t=1}^{t=n} \frac{DPS_t}{(1+r)^t} + \frac{P_n}{(1+r)^n} \right) - \frac{DPS_0 *(1+g_{nn})}{(r-g_n)} \right\}$ | $+$ | $\left\{ \frac{DPS_0 *(1+g_{nn})}{(r-g_n)} - \frac{DPS_0}{r} \right\}$ | $+$             | $\frac{DPS_0}{r}$ |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------|-----------------|-------------------|
| Value of High Growth |                                                                                                                                    |     | Value of Stable Growth                                                 | Assets in Place |                   |

DPS<sup>t</sup> = Expected dividends per share in year t

r = Cost of Equity

Pn = Price at the end of year n

gn = Growth rate forever after year n

### ABN Amro: Decomposing Value

<sup>n</sup> Value of Assets in Place = Current DPS/Cost of Equity = 0.60 Eur/..0882 = 6.65 Eur <sup>n</sup> Value of Stable Growth = 0.60 (1.05)/(.0882-.05) - 6.65 NG = 9.02 Eur <sup>n</sup> Value of High Growth = Total Value - (6.65+ 9.02) = 30.87 - (6.65+9.02) = 15.20 Eur

### S & P 500: Rationale for Use of Model

<sup>n</sup> While markets overall generally do not grow faster than the economies in which they operate, there is reason to believe that the earnings at U.S. companies (which have outpaced nominal GNP growth over the last 5 years) will continue to do so in the next 5 years. The consensus estimate of growth in earnings (from Zacks) is roughly 10% (with bottom-up estimates) and 7.5% (with top-down estimates) <sup>n</sup> Though it is possible to estimate FCFE for many of the firms in the S&P 500, it is not feasible for several (financial service firms). The dividends during the year should provide a reasonable (albeit conservative) estimate of the cash flows to equity investors from buying the index.

### S &P 500: Inputs to the Model (12/31/00)

#### <sup>n</sup> General Inputs

- Long Term Government Bond Rate = 5.1%
- Risk Premium for U.S. Equities = 4%
- Current level of the Index = 1320

#### <sup>n</sup> Inputs for the Valuation

| Length          | High Growth Phase 5 years | Stable Growth Phase Forever after year 5 |
|-----------------|---------------------------|------------------------------------------|
| Dividend Yield  | 1.25%                     | 1.25%                                    |
| Expected Growth | 7.5%                      | 5.5% (Nominal US g)                      |
| Beta            | 1.00                      | 1.00                                     |

# S & P 500: 2-Stage DDM Valuation

Cost of Equity = 5.1% + 1(4%) = 9.1%

Terminal Value = 23.69\*1.055/(.091 -.055) = 691.55

| Intrinsic Value of Index = | \$526.35 |         |         |         |          |
|----------------------------|----------|---------|---------|---------|----------|
| Present Value =            | \$16.26  | \$16.02 | \$15.78 | \$15.55 | \$462.73 |
| Expected Terminal Value=   |          |         |         |         | \$691.55 |
| Expected Dividends =       | \$17.74  | \$19.07 | \$20.50 | \$22.04 | \$23.69  |
|                            | 1        | 2       | 3       | 4       | 5        |

### Explaining the Difference

- <sup>n</sup> The index is at 1320, while the model valuation comes in at 526. This indicates that one or more of the following has to be true.
  - The dividend discount model understates the value because dividends are less than FCFE.
  - The expected growth in earnings over the next 5 years will be much higher than 7.5%.
  - The risk premium used in the valuation (4%) is too high
  - The market is overvalued.

# A More Realistic Valuation of the Index

<sup>n</sup>The median dividend/FCFE ratio for U.S. firms is about 50%. Thus the FCFE yield for the S&P 500 should be around 2.5% (1.25%/.5). <sup>n</sup>The implied risk premium between 1960 and 1970, which was when long term rates were as well behaved as they are today, is 3%. <sup>n</sup>With these inputs in the model:

|                            | 1 2 3 4 5                                  |
|----------------------------|--------------------------------------------|
| Expected Dividends =       | \$35.48 \$38.14 \$41.00 \$44.07 \$47.38    |
| Expected Terminal Value =  | \$1,915.07                                 |
| Present Value =            | \$32.82 \$32.63 \$32.45 \$32.27 \$1,329.44 |
| Intrinsic Value of Index = | \$1,459.62                                 |

**At a level of 1320, the market is undervalued by about 10%.**